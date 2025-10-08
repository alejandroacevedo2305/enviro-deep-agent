---
title: Sin título
author: Envirometrika
date: D:20210318001704-03'00'
language: es
type: report
pages: 112
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO: P6343-Modelación de Impacto Odorante SOLICITANTE: ECOMAULE S.A.
  - Fecha: Marzo 2021
  - At: Sra. Alejandra Barrero.
-->

# PROYECTO: P6343-Modelación de Impacto Odorante SOLICITANTE: ECOMAULE S.A.

# Fecha: Marzo 2021

# At: Sra. Alejandra Barrero.

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 2 de 112

Modelación de Impacto Odorante
Nombre Ficha:
Centro de Tratamiento de Residuos

Reporte no: Versión Final 1.0

Código de proyecto: P 6343

Palabras claves

Concentración de olor, descriptor, dispersión, emisión,
modelación odorante, área de influencia, tasa de emisión
odorante.

Preparado a petición de: ECOMAULE S.A.

Sra. Alejandra Barrero - Subgerente de Medio Ambiente y
Contacto:
Seguridad

Preparado por:

Envirometrika
Europa 2066 - Providencia - Santiago - Chile  56 2 2668 1260
Arturo Prat 199 -Torre A of 1401 Concepción  56 41 383 3978
[e-mail: info@envirometrika.com](mailto:info@envirometrika.com)
[www.envirometrika.com](http://www.envirometrika.com/)

Autores: Ricardo Guerra

Firmado y aprobado por: Envirometrika por Héctor Vergara

Fecha: Marzo 2021

CONTROL DE CAMBIOS www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 3 de 112

**CONTROL DE CAMBIOS**

|DESARROLLADO POR:|FIRMA|ÁREA|
|---|---|---|
|Maximiliano Muñoz||Modelación y Simulación|
|Camila Reyes||Modelación y Simulación|
|Tamara Araya||Modelación y Simulación|

|REVISADO POR:|FIRMA|ÁREA|
|---|---|---|
|Ricardo Guerra||Modelación y Simulación|

|APROBADO POR:|FIRMA|ÁREA|
|---|---|---|
|Héctor Vergara||Sub-Gerencia|

**REVISIONES**

|REVISIÓN|TIPO DE CAMBIO|FECHA|
|---|---|---|
|V 0.1|1a revisión reporte borrador para<br>entrega al cliente|12 de marzo de 2021|
|V 1.0|Versión final|17 de marzo de 2021|

CONTROL DE CAMBIOS www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 4 de 112

**GLOSARIO**

**Altura de mezcla:** Parte superior de la capa de
mezcla. Determina el alcance vertical del proceso de
dispersión de los contaminantes liberados debajo de
ella.

**Análisis de incertidumbre:** Cuantificación de las
diferencias (errores del modelo) entre lo estimado y
las observaciones. Tiene por objetivo evaluar la
capacidad de un modelo de representar una cierta
situación atmosférica.

**Área de influencia:** Área o espacio geográfico
cuyos atributos, elementos naturales o
socioculturales deben ser considerados con la
finalidad de definir si el proyecto o actividad genera o
presenta alguno de los efectos, características o
circunstancias del artículo 11 de la Ley, o bien para
justificar la inexistencia de dichos efectos,
características o circunstancias.

**Área de percepción** : Superficie determinada en la
cual existe la probabilidad de percepción de olor,
generados por una instalación en estudio, bajo un
criterio de calidad definido.

**Calpuff** : Modelo de dispersión no estacionario (tipo
“puff”) Lagrangiano Gaussiano, capaz de representar
el transporte y dispersión de contaminantes sobre
una base de campos de viento construido con Calmet.
El modelo evalúa la contribución de un “puff” en la
concentración atmosférica de una especie de interés
sobre un receptor, en un instante determinado.

**Capa de mezcla** : Profundidad vertical donde se
produce el mezclado de contaminantes atmosféricos.

**Ciclo de operación** : Periodo de tiempo que indica el
funcionamiento efectivo de una unidad de proceso o
planta.

**Concentración de olor** : Número de unidades de
olor europeas en un metro cúbico de gas en
condiciones normales.

**Dirección de viento** : Punto cardinal desde donde
procede el viento.

**Dispersión** : Conjunto de procesos complejos de
transporte, mezcla y transformaciones químicas que
dan lugar a una distribución variable (espacial y
temporal) de la concentración de una especie.

**Dominio** : Área de estudio determinada en función
de la magnitud del proyecto, sus emisiones y
presencia de receptores.

**Escenario de modelación** : Conjunto de variables
que conforman los datos de entrada (input) para un
modelo y que en su combinación representan una
condición específica de operación o emisión.

**Estación superficial** : Conjunto de instrumentos
destinados a medir y registrar regularmente diversas
variables meteorológicas. Estos datos se utilizan tanto
para la elaboración de predicciones meteorológicas a
partir de modelos numéricos como para estudios
[climáticos.](http://es.wikipedia.org/wiki/Clima)

**Fuente difusa** : Fuentes con dimensiones definidas
(mayoritariamente fuentes superficiales), que no
tienen un flujo de aire definido, tales como:
vertederos de residuos, lagunas, campos después de
extender el estiércol, montones de compost sin
aireación. Relacionada con actividades que son
generalmente dominadas por fuentes de emisión de
olor fugitivas de área o volumen, los cuales pueden
ser relativamente difícil de controlar, por ejemplo,
actividades agro-culturales intensivas.

**Fuente fugitiva:** Fuentes esquivas o de difícil
identificación que liberan cantidades indefinidas de
sustancias olorosas (por ejemplo, fugas de válvulas y
juntas, aperturas de ventilación pasiva, otros).

**Fuente puntual** : Fuente estacionaria discreta, de
emisión de gases a la atmósfera a través de
conductos, de dimensión y caudal de aire definidos
(por ejemplo: chimeneas, venteos). Fuente
relacionada con actividades que involucran emisiones
de olor desde una chimenea, estas son relativamente
fáciles de controlar usando reducción de residuos,
minimización de residuos y principios de producción
limpia o equipamiento convencional de control de
emisiones.

**Grilla** : Subdivisión de un dominio de modelación.
Define la resolución utilizada en un modelo en base a
la dimensión de cada celda.

**Isolínea** : Línea que conecta concentraciones de
igual valor de una especie.

**Inmisión de olor:** Es el impacto de olor en el ser
humano (olores en el aire ambiente). Ellos pueden ser
descritos en términos de frecuencia, duración, calidad
(tipo), intensidad y disgusto subjetivo (efecto

GLOSARIO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 5 de 112

hedónico) de las concentraciones de olores por
encima del umbral de olor.

**Meteorología** **de** **pronóstico** : Datos
meteorológicos obtenidos a partir de un modelo de
predicción que integran información meteorológica
tridimensional, abarcando varias capas verticales a
una resolución determinada sobre un dominio
especificado.

**Meteorología superficial** : Registros de parámetros
meteorológicos medidos por una estación superficial.

**MMIF** : Programa de interfase para modelos de
mesoescala, que convierte los campos de salida del
modelo meteorológico de pronóstico a parámetros y
formatos requeridos para el ingreso directo a los
modelos de dispersión. En Calpuff, surge como una
alternativa para CALMET generando campos de
entrada meteorológicos tridimensionales para la
evaluación de impacto de modelaciones de calidad del
aire.

**Modelo / Modelización odorante** : Herramienta de
pronóstico aplicada en la evaluación de impacto
odorífero, que incluye las ecuaciones que describen
la relación entre la concentración de olor de una zona,
con la tasa de emisión de una instalación, y los
factores que afectan a la dispersión y la dilución
atmosférica.

**Olfatometría:** Medición de la respuesta de los
panelistas a estímulos olfativos.

**Olfatometría dinámica:** Olfatometría que usa un
olfatómetro dinámico.

**Olor:** Propiedad organoléptica perceptible por el
órgano olfativo cuando inspira determinadas
sustancias volátiles.

**Olor compuesto** : es el que se percibe como
consecuencia de la mezcla de más de un olor simple.
En la mezcla de sustancias olorosas pueden
producirse fenómenos de sinergias, interferencias e
inhibiciones, y por lo mismo, en la percepción del olor
compuesto no siempre es fácil definir y atribuir las
moléculas que lo causan (Iglesias, 2012). De esta
manera la percepción fisiológica del conjunto no es el
resultado de la suma sensorial de sustancias olorosas
individuales, es decir, el olor no puede ser definido
como la suma de las sustancias olorosas que lo
conforman.

**Olor simple** : es el que percibe el olfato como
consecuencia de la emisión de un compuesto químico
o sustancia olorosa determinada. Por ejemplo, el
ácido sulfhídrico (H2S) es una sustancia olorosa. Los
olores de tipo simple suelen ser fácilmente
identificables (Díaz et al., 2013).

**Percentil** : Es una medida estadística de posición no
central, que representa los valores de cierta variable
que están por debajo de un porcentaje, el cual puede
ser un valor de 1% a 100% (en otras palabras, el
total de los datos es dividido en 100 partes iguales).
Se representa con la letra P y los más utilizados son
el percentil 99.5 y 98. Dentro de un modelo de
dispersión un percentil representa la excedencia
permitida.

**Perfiles de percepción** : Caracterización de un
periodo de tiempo en el cual un receptor evidencia
probabilidad de percepción de una emisión bajo un
criterio de calidad determinado. Puede ser expresado
como el número de horas del mes o del año que
excede un criterio definido.

**Radio de influencia** : Área para la cual una o un
conjunto de variables son representativas.

**Receptores** : Punto de interés dentro del dominio de
modelación, donde se evalúa el grado de percepción
de las emisiones de una o más fuentes de una
instalación en estudio. Un receptor podría representar
una población, escuela, hospital, parque, flora, fauna,
plantaciones agrícolas, entre otros.

**Sentido** : Vector que indica hacia dónde va el viento.

**Simulación** : Representación futura de una
instalación o unidad de proceso.

**Tasa de emisión odorante** : Cantidad de sustancias
olorosas pasando a través de un área definida en
cada unidad de tiempo. Esto es producto de la
concentración de olor y de la velocidad y área de
salida o el producto de la concentración de olor y la
pertinente tasa de volumen de flujo, por ejemplo, en

[m [3] /h]. Esta unidad es [ou E /h] (o [ou E /min] o

[ou E /s]).

**Unidad de olor:** Una unidad de olor es la cantidad
de (una mezcla de) sustancias olorosas presentes en
un metro cúbico de gas oloroso (en condiciones

GLOSARIO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 6 de 112

normales) en el umbral del panel. La sigla utilizada
para esta unidad es [ou [1] ].

**Unidad de olor europea:** Cantidad de sustancia(s)
olorosa(s) que, cuando se evapora en 1 metro cúbico
de un gas neutro en condiciones normales, origina
una respuesta fisiológica de un panel (umbral de
detección) equivalente al que origina una Masa de
Olor de referencia (MORE) evaporada en un metro
cúbico de un gas neutro en condiciones normales. La
sigla utilizada para esta unidad es [ou E ].

1 Sigla en inglés, Odour Unit

GLOSARIO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 7 de 112

**RESUMEN EJECUTIVO**
El presente reporte, corresponde a los resultados de la
actualización de la Modelación de Impacto Odorante,
solicitado por ECOMAULE S.A., para el proyecto
“Mejoramiento y Transformación Ecomaule: Plataforma de
Reciclaje y Valorización”. Incorporando la evaluación de dos
nuevas fuentes (área de riego 1 y 2) en la operación del
proyecto. Esto bajo el marco de la Declaración de Impacto
Ambiental (DIA) sometida al Sistema de Evaluación de
Impacto Ambiental (SEIA).

Figura 1 - Localización del Proyecto

Fuente: Elaboración propia, a partir de Google Earth 2021.

El objetivo fue proyectar mediante modelación el alcance
odorante del Centro de Tratamiento de Residuos, bajo
condición operacional actual y futura, ambas definidas por
el Titular.

El plan de trabajo consideró el desarrollo de las siguientes
etapas:
1. Recopilación de antecedentes. Titular indica el utilizar
las tasas de emisión levantadas en el 2019, en
proyectos N°s 5838 y P5052, para la situación actual.
2. Revisión de emisiones de referencia aplicables.
3. Identificación y caracterización de fuentes emisoras.
4. Preparación de datos de entrada al software de
modelación.
5. Estimación del área de influencia para la componente
olor.
6. Obtención de resultados.

7. Informe de resultados.

Las emisiones de referencia aplicadas fueron obtenidas a
partir de lo muestreado en la planta el año 2019, cuyas
unidades y emisiones son asimilables a la operación actual
y fueron obtenidas en cumplimiento a la normativa vigente
aplicable NCh3386:2015 [2] y NCh3190:2010 [3] .

2 Instituto Nacional de Normalización. (2015). NCh 3386:2015

Calidad del aire - Muestreo estático para olfatometría. Chile

Basado en las partes, obras y acciones del Proyecto,
declaradas por el Titular, se identificaron y caracterizaron
aquellas fuentes con emisión de olor al aire ambiente para
2 escenarios operacionales: Situación actual (Proyecto en
ejecución) y Situación futura (Proyecto en evaluación). Lo
anterior, según se describe en las siguientes tablas:

Tabla 1 - Fuentes odorantes Situación actual

|Área|Nombre fuente|Emisión<br>de Olor<br>[ouE/m2s]|Tasa de<br>Emisión de<br>Olor<br>[ouE/s]|
|---|---|---|---|
|Compostaje|Pila Lodo Agroindustrial - Edad 1<br>Pila Lodo Agroindustrial - Edad 2<br>Pila Lodo Agroindustrial - Edad 3<br>Pila lodo sanitario - Edad 1 Curicó<br>Pila lodo sanitario - Edad 1 Otras Loc.<br>Pila lodo sanitario - Edad 2 Curicó<br>Pila lodo sanitario - Edad 2 Otras Loc.<br>Pila lodo sanitario - Edad 3 Curicó<br>Pila lodo sanitario - Edad 3 Otras Loc.|14,7<br>8,3<br>1,6<br>5,7<br>3,8<br>11,4<br>5,9<br>5,6<br>1,7|181.530,30<br>61.876,50<br>3.840,00<br>45.446,10<br>90.892,20<br>72.982,80<br>113.315,40<br>6.493,20<br>5.913,45|
|PTRILes|Laguna de percolados|81,6|81.600,00|
|PTRILes|Laguna de agua rechazo|81,6|12.566,40|
|PTRILes|Reactor aerobio 1|31,8|2.497,57|
|PTRILes|Reactor aerobio 2|31,8|2.497,57|
|PTRILes|Clarificador|14,2|343,64|
|PTRILes|Floculador|14,2|100,37|
|PTRILes|Laguna lodos biológicos|21,2|1.433,12|
|PTRILes|Laguna lodo físico/químico|2,3|140,76|
|PTRILes|Lechos de secado 1|4,2|1.268,40|
|PTRILes|Lechos de secado 2 (lav. de camiones)|32,8|8.757,60|
|PTRILes|Laguna agua tratada|2,4|904,80|
|Rell.<br>San.|Monorelleno - Frente de trabajo|11,1|50.038,80|
|Rell.<br>San.|Relleno Sanitario - Frente de trabajo|21,3|18.105,00|

|Área|Nombre fuente|Emisión<br>de Olor<br>[ouE/m2s]|Tasa de<br>Emisión de<br>Olor<br>[ouE/s]|
|---|---|---|---|
|Compostaje|Cancha de compostaje 1|0,53|5.283,75|
|Compostaje|Cancha de compostaje 2|0,53|2.610,30|
|Compostaje|Cancha de compostaje 3|0,53|7.441,46|
|Compostaje|Cancha de compostaje 4|0,53|8.420,32|
|Compostaje|Galpón de comp. 1 (sist. de abatimiento)|1.128,86|1.276,71|
|Compostaje|Galpón de comp. 2 (sist. de abatimiento)|1.438,43|1.626,82|
|Compostaje|Galpón de comp. 3 (sist. de abatimiento)|1.438,43|1.626,82|
|Compostaje|Galpón de comp. 4 (sist. de abatimiento)|1.438,43|1.626,82|
|Digestión<br>anaeróbica|Est. acumulación clarificado - Etapa 1|0,32|64,34|
|Digestión<br>anaeróbica|Est. acumulación de digestato - Etapa 1|0,32|2,94|
|Digestión<br>anaeróbica|Cont. deshidratado mecánico - Etapa 1|0,32|4,07|
|Digestión<br>anaeróbica|Est. acumulación clarificado - Etapa 2|0,32|64,34|
|Digestión<br>anaeróbica|Cont. deshidratado mecánico - Etapa 2|0,32|4,07|

3 Instituto Nacional de Normalización. (2010). NCh 3190:2010

Calidad del aire - Determinación de la concentración de olor por
olfatometría dinámica. Chile.

Tabla 2 - Fuentes odorantes Situación futura

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 8 de 112

industriales, los límites utilizados serían en base a la
distancia de los receptores desde el perímetro de la
instalación, para receptores entre 0 y 200 [m] se aplicó
como límite 5 [ou E /m [3] ], entre 200 y 500 [m] 4 [ou E /m [3] ] y
mayor a 500 [m] se aplicó 3 [ou E /m [3] ], estos bajo percentil
98 para ambos escenarios operacionales.

Tabla 4 - Escenario operacional para modelación

|Área|Nombre fuente|Emisión<br>de Olor<br>[ouE/m2s]|Tasa de<br>Emisión de<br>Olor<br>[ouE/s]|
|---|---|---|---|
||Galpón de recepción (Sist. de abatim.1)|47,23|53,42|
||Galpón de recepción (Sist. de abatim.2)|47,23|53,42|
||Unidad de almacenamiento de digestato|0,32|1.705,28|

Tabla 3 - Fuentes odorantes Situación futura (Cont.)

|Escenario Operacional|Col2|Modelos|Criterio de<br>calidad<br>[ou/m3]<br>E|PC|
|---|---|---|---|---|
|E1|Situación actual<br>(Proy. en ejecución)|M1<br>M2<br>M3<br>M4|3, 4 y 5|98|
|E2|Situación futura<br>(Proy. en evaluación)|Situación futura<br>(Proy. en evaluación)|Situación futura<br>(Proy. en evaluación)|Situación futura<br>(Proy. en evaluación)|

|Área|Nombre fuente|Emisión de<br>Olor<br>[ouE/m2s]|Tasa de<br>Emisión de<br>Olor<br>[ouE/s]|
|---|---|---|---|
|PTRILes|Laguna anaeróbica|5,71|11.424,00|
|PTRILes|Laguna de percolados|5,71|5.710,00|
|PTRILes|Reactor aerobio 1|19,08|1.498,54|
|PTRILes|Reactor aerobio 2<br>|19,08<br>|1.498,54<br>|
|PTRILes|Reactor aerobio 3|19,08|1.498,54|
|PTRILes|Reactor aerobio 4|19,08|1.498,54|
|PTRILes|Clarificador|8,52|206,18|
|PTRILes|Floculador|8,52|60,22|
|PTRILes|Laguna lodos biológicos|21,20|1.433,12|
|PTRILes|Laguna lodo físico/químico|2,30|140,76|
|PTRILes|Laguna agua tratada|0,25|94,25|
|Relleno|Alvéolo 7 - Frente de trabajo|21,30|18.105,00|
|Riego|Zona de riego 1|0,32|4.217,60|
|Riego|Zona de riego 2|0,32|5.729,96|

La representación operacional y estructural de las fuentes,
siguió los lineamientos y recomendaciones descritos en la
Guía para el uso de modelos de calidad del aire en el SEIA [4]
(SEA, 2012) y la Guía de evaluación de impacto ambiental
por olores [5] (SEA, 2017).

La evaluación del Proyecto consideró lo señalado en la Guía
para la Predicción y Evaluación de Impactos por Olor en el
SEIA [6], de modo que el Servicio de Evaluación Ambiental
pueda evaluar si la modificación se encuentra en obligación
de someterse al SEIA. Lo anterior en base al artículo 10 de
la Ley N° 19.300, modificada por la Ley 20.417, y
especificadas en el artículo 3° del D.S. N° 40/12 del
Ministerio del Medio Ambiente y en lo dispuesto en el
artículo 2° literal g) del mismo Reglamento.

Para efectos de la Declaración de Impacto Ambiental (DIA),
se consideró lo establecido en las normas de calidad
ambiental y de emisión vigentes utilizando como referencia
la norma de Lombardía [7], la cual establece los límites en
función del uso de territorio y diferenciación de actividades
existentes o nuevas. Según los antecedentes para la
determinación del área de influencia, el proyecto se
emplaza en una zona no regulada por los IPT, por lo tanto
se utilizarían los criterios para las zonas agrícolas o

M1: Isolíneas de olor.
M2: Frecuencias de percepción de olor (horario).
M3: Frecuencia de percepción de olor (mensual).
M4: Concentración máxima horaria.

PC: Percentil.

El software empleado para la modelación de la dispersión
atmosférica de olores corresponde a Calpuff View, versión
8.6.0, el cual requiere de datos de entrada, tales como, de
características físicas de las fuentes, valores de emisión,
variables meteorológicas e información topográfica y de uso
de suelos.
La base meteorológica fue procesada mediante MMIF,
integra datos de pronóstico WRF [8] 2019 con resolución de 1

[km] (espaciado de la cuadrícula). Se aplicó una grilla de
muestreo con un factor de anidamiento igual a 4, para
alcanzar mayor resolución de las isolíneas de concentración
resultantes del modelo.
El dominio meteorológico WRF cubrió un área de
aproximadamente 75 x 75 [km].

Los puntos receptores de interés considerados en el estudio
se describen en la siguiente tabla.

Tabla 5 - Receptores con distancia y rango

4 Servicio de Evaluación Ambiental. (2012). Guía para el uso de

modelos de calidad del aire en el SEIA. Chile.
5 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción

y Evaluación de Impactos por Olor en el SEIA. Ministerio del

Medio Ambiente. Chile .
6 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción

y Evaluación de Impactos por Olor en el SEIA. Ministerio del
Medio Ambiente. Chile.

7 Cusano, Gianluca & Licotti, Carlo & Sironi, Selena & Capelli, Laura

& Rossi, Andrea & Grande, Massimiliano. (2010). Odour
regulation in Italy: The regional guidelines on odour emissions in
Lombardia. Chem.
8 Weather Research and Forecasting Model, WRF

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 9 de 112

|ID|Nombre|Distancia\a<br>[m]|Rango<br>distancia<br>[m]|
|---|---|---|---|
|R1|Vivienda 1|73|<200|
|R2|Vivienda 2|1.018|>500|
|R3|Vivienda 3|618|>500|
|R4|Vivienda 4|900|>500|
|R5|Vivienda 5|448|200 - 500|
|R6|Vivienda 6|1.036|>500|
|R7|Sector Los Robles|3.196|>500|
|R8|Sector Escudo de Chile|1.760|>500|
|R9|Sector El Umbral|2.666|>500|
|R10|Escuela Juan Luis Sanfuentes A.|2.917|>500|
|R11|Sector Camarico|2.898|>500|
|R12|Peaje Troncal Río Claro|1.484|>500|

\a Distancia medidas desde el perímetro del Centro de Tratamiento
de Residuos.
Figura 2 - Puntos receptores de interés

Fuente: Elaboración propia, a partir de Google Earth 2021.

Tanto para la determinación del área de influencia de olor
como para la cuantificación del impacto por olores, se
siguieron los lineamientos de la Guía para la Predicción y
Evaluación de impactos por Olor (SEIA, 2017).
Considerando como herramienta de predicción del impacto,
un modelo complejo de dispersión: Calpuff.

La estimación del Área de Influencia consideró como criterio
el área proyectada con 1 [ou E /m [3] ], que corresponde al
umbral de detección del olor.
La cuantificación del impacto se realizó a través de la
excedencia del criterio de calidad y la cantidad de horas al
año con probabilidad de percepción de olor en los puntos
receptores evaluados.

**Resultados**
La Tasa de Emisión de Olor de los escenarios evaluados se
describe en la siguiente tabla:

Tabla 6 - TEO y alcance odorante

9 No considera el área [ha] interna del proyecto.

|Escenario<br>Operacional|TEO<br>[ouE/s]|Alcance [ha]\a|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Escenario<br>Operacional|TEO<br>[ouE/s]|1<br>[ouE/m3]|3<br>[ouE/m3]|4<br>[ouE/m3]|5<br>[ouE/m3]|
|E1: Sit. actual<br>E2: Sit. futura|762.544<br>75.033|8.204<br>454|2.774<br>218|2.118<br>175|1.715<br>144|

\a : No considera el perímetro del proyecto

El alcance se consideró para las isolíneas de 3, 4 y 5

[ou E /m [3] ], que son las concentraciones límites definidas por
la normativa de Lombardía según la distancia entre el
perímetro del proyecto y los receptores en estudio.

Figura 3 - Estimación del área de influencia según nivel
umbral del C P98-1hr = 1 [ou E /m [3] ] - Situación futura

Fuente: Elaboración propia, a partir de Google Earth 2021.

El área de influencia determinada para la componente olor
mediante modelación de dispersión para el proyecto en
evaluación, arrojó un área aproximada de 454 [ha] [9] .

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 10 de 112

Figura 4 - Curvas isodoras a C P98-1hr = 3 [ou E /m [3] ] - Situación
actual

Fuente: Elaboración propia, a partir de Google Earth 2021.

La modelación de la Situación actual acusaría excedencia
en 5 de los 10 receptores para los que aplicaría el criterio
de calidad 3 [ou E /m [3] ].

Figura 5 - Curvas isodoras a C P98-1hr = 4 [ou E /m [3] ] - Situación
actual

Fuente: Elaboración propia, a partir de Google Earth 2021.

La modelación de la Situación actual acusaría excedencia
en 1 receptor bajo el criterio de calidad aplicable de 4

[ou E /m [3] ].

Figura 6 - Curvas isodoras a C P98-1hr = 5 [ou E /m [3] ] - Situación
actual

Fuente: Elaboración propia, a partir de Google Earth 2021.

La modelación de la Situación actual acusaría excedencia
en 1 receptor bajo el criterio de calidad aplicable de 5

[ou E /m [3] ].

Figura 7 - Curvas isodoras a C P98-1hr = 3 [ou E /m [3] ] - Situación
futura

Fuente: Elaboración propia, a partir de Google Earth 2021.

La modelación de la Situación futura no acusaría excedencia
del criterio de calidad 3 [ou E /m [3] ] en ninguno de los
receptores evaluados.

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 11 de 112

Figura 8 - Curvas isodoras a C P98-1hr = 4 [ou E /m [3] ] - Situación
futura

Fuente: Elaboración propia, a partir de Google Earth 2021.

La modelación de la Situación futura no acusaría excedencia
del criterio de calidad 4 [ou E /m [3] ] en el receptor evaluado.

Figura 9 - Curvas isodoras a C P98-1hr = 5 [ou E /m [3] ] - Situación
futura

Fuente: Elaboración propia, a partir de Google Earth 2021.

La modelación de la Situación futura no acusaría excedencia
del criterio de calidad 5 [ou E /m [3] ] en el receptor evaluado.

Tabla 7 - Evaluación de molestia en receptores a los que
aplica 3 [ou E /m [3] ] - Situación futura

|Receptor|Percepción de olor<br>sobre 3 [ou/m3]<br>E|Cantidad de horas<br>de exposición de<br>olor ≥ 3 [ou E/m3]|Molestia|
|---|---|---|---|
|R2|No|0|No|
|R3|No|0|No|
|R4|No|0|No|
|R6|No|0|No|
|R7|No|0|No|
|R8|No|0|No|
|R9|No|0|No|
|R10|No|0|No|
|R11|No|0|No|
|R12|No|0|No|

Tabla 8 - Evaluación de molestia en receptores a los que
aplica 4 [ou E /m [3] ] - Situación futura

|Receptor|Percepción de olor<br>sobre 4 [ou/m3]<br>E|Cantidad de horas<br>de exposición de<br>olor ≥ 4 [ou E/m3]|Molestia|
|---|---|---|---|
|R5|No|0|No|

Tabla 9 - Evaluación de molestia en receptores a los que
aplica 5 [ou E /m [3] ] - Situación futura

|Receptor|Percepción de olor<br>sobre 5 [ou/m3]<br>E|Cantidad de horas<br>de exposición de<br>olor ≥ 5 [ou E/m3]|Molestia|
|---|---|---|---|
|R1|No|0|No|

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 12 de 112

**Conclusión**

Los resultados de la proyección del alcance odorante del
proyecto Centro de Tratamiento de Residuos en “situación
futura”, arrojó para los 12 receptores definidos niveles de
exposición bajo los límites de exposición establecidos en la
normativa de Lombardía.

Para la situación futura la estimación de emisión muestra
una reducción del 89% de la TEO actual y 92% en el área
de alcance de la pluma de olor (para el umbral de
reconocimiento 3 [ou E /m [3] ]).

Al proyectar las TEO levantadas en el 2019, para la
situación futura se obtuvo que para la componente olor, el
proyecto no generaría o presentaría algún efecto,
características o circunstancias contempladas en el artículo
11 de la Ley 19.300.

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 13 de 112

**ÍNDICE**

CONTROL DE CAMBIOS ................................................................................................................................. 3

GLOSARIO .................................................................................................................................................... 4

RESUMEN EJECUTIVO ................................................................................................................................... 7

1 ANTECEDENTES ................................................................................................................................... 17
1.1 Antecedentes generales ................................................................................................................ 17
Descripción operacional del Proyecto en ejecución ...................................................................... 18
1.2 Antecedentes específicos .............................................................................................................. 18
1.3 Diagrama general de procesos ...................................................................................................... 19
1.4 Antecedentes para el área de influencia ......................................................................................... 23
2 OBJETIVOS .......................................................................................................................................... 24
2.1 Objetivo general ........................................................................................................................... 24
2.2 Objetivos específicos .................................................................................................................... 24
3 ESTIMACIÓN DE EMISIONES ................................................................................................................ 25

3.1 Emisiones de referencia ................................................................................................................ 25
3.2 Emisiones según olor simple o compuesto...................................................................................... 28
3.3 Ranking de emisiones ................................................................................................................... 36
4 PREDICCIÓN DE IMPACTOS POR OLOR ................................................................................................. 38
4.1 Metodologías para la predicción de impactos por olor ..................................................................... 38
4.2 Determinación del área de influencia del proyecto .......................................................................... 39
Descripción del área de influencia según elementos del medio ambiente ...................................... 39
Identificación de receptores de olor ........................................................................................... 39
Olor base en situación sin proyecto ............................................................................................ 40
5 ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR ................................................................... 42
5.1 Estimación concentración límite de exposición ................................................................................ 42
5.2 Estimación de los impactos por emisiones de olor ........................................................................... 44
5.3 Predicción de Área de Influencia del Proyecto ................................................................................ 45
5.4 Cuantificación según curva de isoconcentración de olor .................................................................. 46
5.5 Cuantificación de la frecuencia de percepción de olor ..................................................................... 52
5.6 Concentración máxima .................................................................................................................. 55
6 CONCLUSIÓN ....................................................................................................................................... 56
7 BIBLIOGRAFÍA ..................................................................................................................................... 57
8 ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES ..................................................................... 58
9 ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES ............................................................. 62
10 ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA ............................................................................... 68
10.1 Plan de trabajo ............................................................................................................................. 68
10.2 Fuentes de emisión ...................................................................................................................... 69

Detalle operacional ................................................................................................................ 69
Rueda de olor ....................................................................................................................... 73
11 ANEXO 4 - MODELO DE DISPERSIÓN ............................................................................................... 74

11.1 Alcances del modelo ..................................................................................................................... 74
11.2 Descripción del modelo ................................................................................................................. 74
11.3 Dominio de modelación................................................................................................................. 75
11.4 Base meteorológica y grilla de muestreo ........................................................................................ 75
11.5 Elevaciones de terreno .................................................................................................................. 76

11.6 Uso de suelo ................................................................................................................................ 77
11.7 Caracterización meteorológica anual .............................................................................................. 78
11.8 Caracterización meteorológica anual horaria ................................................................................... 79
12 ANEXO 5 - ANÁLISIS METEOROLÓGICO ........................................................................................... 80
12.1 Rosas y campos de viento ............................................................................................................. 81
12.2 Altura de mezcla........................................................................................................................... 87
13 ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE ........................................................................................ 89
13.1 Levantamiento y selección de información meteorológica observada................................................ 90
13.2 Diagnóstico de datos meteorológicos ............................................................................................. 92

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 14 de 112

Datos meteorológicos ............................................................................................................ 92
Series de tiempo ................................................................................................................... 95
Ciclos diarios ......................................................................................................................... 97
13.3 Comparación entre pronóstico y observaciones ............................................................................ 105

Análisis cualitativo de serie de pronóstico y observada .......................................................... 105
Análisis cuantitativo de serie de pronóstico y observada ........................................................ 110
13.4 ANÁLISIS DE RESULTADOS ......................................................................................................... 111
13.5 BIBLIOGRAFÍA ANEXOS .............................................................................................................. 112

**ÍNDICE DE TABLAS**
Tabla 1 - Fuentes odorantes Situación actual ................................................................................................. 7
Tabla 2 - Fuentes odorantes Situación futura ................................................................................................. 7
Tabla 3 - Fuentes odorantes Situación futura (Cont.) ...................................................................................... 8
Tabla 4 - Escenario operacional para modelación ............................................................................................ 8
Tabla 5 - Receptores con distancia y rango .................................................................................................... 8
Tabla 6 - TEO y alcance odorante .................................................................................................................. 9
Tabla 7 - Evaluación de molestia en receptores a los que aplica 3 [ou E /m [3] ] - Situación futura ......................... 11
Tabla 8 - Evaluación de molestia en receptores a los que aplica 4 [ou E /m [3] ] - Situación futura ......................... 11
Tabla 9 - Evaluación de molestia en receptores a los que aplica 5 [ou E /m [3] ] - Situación futura ......................... 11
Tabla 10 - Coordenadas referenciales de localización del Proyecto ................................................................. 17
Tabla 11 - Fuentes odorantes - Situación actual ........................................................................................... 21
Tabla 12 - Fuentes odorantes - Situación futura ........................................................................................... 22
Tabla 13 - Proyecto de referencia aplicable .................................................................................................. 25
Tabla 14 - Emisiones de referencia aplicados en Situación actual ................................................................... 26
Tabla 15 - Emisiones de referencia aplicados en la Situación futura ............................................................... 27
Tabla 16 - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 1 ...................................... 29
Tabla 17 - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 2 ...................................... 30
Tabla 18 - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 3 ...................................... 31
Tabla 19 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 1 ...................................... 32
Tabla 20 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 2 ...................................... 33
Tabla 21 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 3 ...................................... 34
Tabla 22 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 4 ...................................... 35
Tabla 23 - Ranking TEO [ou E /s] por fuente modelada - Situación actual ........................................................ 36
Tabla 24 - Ranking TEO [ou E /s] por fuente modelada - Situación futura ........................................................ 37
Tabla 25 - Puntos receptores de interés ....................................................................................................... 39
Tabla 26 - Situación olor base - Proyectos aprobados en SEIA ...................................................................... 40
Tabla 27 - Situación olor base - Establecimientos identificados en terreno [/a] ................................................... 41
Tabla 28 - Concentraciones máximas en receptores según normativa de Lombardía. ...................................... 43
Tabla 29 - Valores límites en receptores de interés ....................................................................................... 43
Tabla 30 - Descripción escenarios simulados ................................................................................................ 44
Tabla 31 - E1/M2: Frecuencia de percepción de olor horaria [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación actual .... 52
Tabla 32 - E1/M3: Frecuencia de percepción de olor mensual [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación actual .. 53
Tabla 33 - E1/M2: Frecuencia de percepción de olor horaria [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación futura.... 53
Tabla 34 - E1/M3: Frecuencia de percepción de olor mensual [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación futura .. 54
Tabla 35 - Concentración máxima - Percentil 98 y 99,5 - Situación actual ..................................................... 55
Tabla 36 - Concentración máxima - Percentil 98 y 99,5 - Situación futura ..................................................... 55
Tabla 37 - Situación actual: Caracterización de fuentes de olor (parte 1) ....................................................... 58
Tabla 38 - Situación actual: Caracterización de fuentes de olor (parte 2) ....................................................... 59
Tabla 39 - Situación futura: Caracterización de fuentes de olor (parte 1) ....................................................... 60
Tabla 40 - Situación futura: Caracterización de fuentes de olor (parte 2) ....................................................... 61
Tabla 41 - Características de galpones de compostaje (confinado) ................................................................. 62
Tabla 42 - Curva de estabilización de compostaje en cancha ......................................................................... 63
Tabla 43 - Caracterización de emisión de olor de galpón de recepción ........................................................... 64
Tabla 44 - Eficiencia de abatimiento de olor de cubiertas flotantes según % de variación ............................... 65

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 15 de 112

Tabla 45 - Caracterización de laguna anaeróbica y laguna de percolados ....................................................... 65
Tabla 46 - Caracterización de fuentes PTRILes optimizadas ........................................................................... 66
Tabla 47 - Emisión de olor en fuentes PTRILes optimizadas .......................................................................... 66
Tabla 48 - Curva de emisión de olor post aplicación de digestato tratado ....................................................... 67
Tabla 49 - Situación actual: Características operacionales de fuentes emisoras (parte 1)................................. 69
Tabla 50 - Situación actual: Características operacionales de fuentes emisoras (parte 2)................................. 70
Tabla 51 - Situación futura: Características operacionales de fuentes emisoras (parte 1) ................................ 71
Tabla 52 - Situación futura: Características operacionales de fuentes emisoras (parte 2) ................................ 72
Tabla 53 - Coordenada central Centro de Tratamiento de Residuos ............................................................... 78
Tabla 54 - Distribución de rosas de viento anual horaria ............................................................................... 79
Tabla 55 - Coordenadas representativas de Centro de Tratamiento de Residuos ............................................. 80
Tabla 56 - Descripción de ciclos de análisis meteorológicos ........................................................................... 80
Tabla 57 - Rosas y campos de viento pronóstico anual.................................................................................. 81
Tabla 58 - Rosas y campos de viento pronóstico estacional - Verano ............................................................. 82
Tabla 59 - Rosas y campos de viento pronóstico estacional - Otoño ............................................................... 83
Tabla 60 - Rosas y campos de viento pronóstico estacional - Invierno ........................................................... 84
Tabla 61 - Rosas y campos de viento pronóstico estacional - Primavera ......................................................... 85
Tabla 62 - Registro de ortofotografías - Isolíneas de altura de mezcla ............................................................ 88
Tabla 63 - Altura de mezcla - promedios por periodo estacional y horario [m] ............................................... 88
Tabla 64 - Estaciones meteorológicas superficiales en el dominio de modelación WRF .................................... 90
Tabla 65 - Coordenada de localización, serie de pronóstico WRF ................................................................... 92
Tabla 66 - Coordenada de localización estación meteorológica ...................................................................... 93
Tabla 67 - Porcentaje datos válidos en parámetros evaluados ....................................................................... 94
Tabla 68 - Ciclos diarios de la temperatura - serie pronóstico ........................................................................ 97
Tabla 69 - Ciclos diarios de la temperatura - serie observada ........................................................................ 98
Tabla 70 - Ciclos diarios promedios serie pronóstico ..................................................................................... 99
Tabla 71 - Ciclos diarios promedios serie observada.................................................................................... 100
Tabla 72 - Ciclos diarios de dirección del viento serie pronóstico .................................................................. 101
Tabla 73 - Ciclos diarios de dirección del viento serie observada .................................................................. 102
Tabla 74 - Frecuencia mensual de vientos calmos - serie pronóstico ............................................................ 103
Tabla 75 - Frecuencia horaria de vientos calmos - serie pronóstico .............................................................. 103
Tabla 76 - Frecuencia mensual de vientos calmos - serie observada ............................................................ 104

Tabla 77 - Frecuencia horaria de vientos calmos - serie observada .............................................................. 104
Tabla 78 - Error medio cuadrático, sesgo, coeficiente de correlación, IOA, velocidad del viento y temperatura110

**ÍNDICE DE FIGURAS**
Figura 1 - Localización del Proyecto ............................................................................................................... 7
Figura 2 - Puntos receptores de interés .......................................................................................................... 9
Figura 3 - Estimación del área de influencia según nivel umbral del C P98-1hr = 1 [ou E /m [3] ] - Situación futura ........ 9
Figura 4 - Curvas isodoras a C P98-1hr = 3 [ou E /m [3] ] - Situación actual ............................................................... 10
Figura 5 - Curvas isodoras a C P98-1hr = 4 [ou E /m [3] ] - Situación actual ............................................................... 10
Figura 6 - Curvas isodoras a C P98-1hr = 5 [ou E /m [3] ] - Situación actual ............................................................... 10
Figura 7 - Curvas isodoras a C P98-1hr = 3 [ou E /m [3] ] - Situación futura ............................................................... 10
Figura 8 - Curvas isodoras a C P98-1hr = 4 [ou E /m [3] ] - Situación futura ............................................................... 11
Figura 9 - Curvas isodoras a C P98-1hr = 5 [ou E /m [3] ] - Situación futura ............................................................... 11
Figura 10 - Localización del Proyecto ........................................................................................................... 17
Figura 11 - Diagrama de proceso de compostaje .......................................................................................... 19
Figura 12 - Diagrama de flujo de Digestión Anaeróbica ................................................................................. 20
Figura 13 - Localización del Proyecto según Límite Urbano de PRC de Río Claro ............................................. 23
Figura 14 - Ubicación geográfica de los puntos receptores de interés ............................................................. 40
Figura 15 -Proyectos aprobados por el Servicio de Evaluación Ambiental........................................................ 41
Figura 16 - AI: Área de influencia del Proyecto, C P98-1hr = 1 [ou E /m [3] ] .............................................................. 45
Figura 17 - E1: Curvas isodoras Situación actual, C P98-1hr = 3 [ou E /m [3] ] ............................................................ 46

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 16 de 112

Figura 18 - E1: Curvas isodoras Situación actual, C P98-1hr = 4 [ou E /m [3] ] ............................................................ 47
Figura 19 - E1: Curvas isodoras Situación actual, C P98-1hr = 5 [ou E /m [3] ] ............................................................ 48
Figura 20 - E2: Curvas isodoras Situación futura, C P98-1hr = 3 [ou E /m [3] ] ............................................................ 49
Figura 21 - E2: Curvas isodoras Situación futura, C P98-1hr = 4 [ou E /m [3] ] ............................................................ 50
Figura 22 - E2: Curvas isodoras Situación futura, C P98-1hr = 5 [ou E /m [3] ] ............................................................ 51
Figura 23 - Esquema de plan de trabajo y metodología aplicada .................................................................... 68
Figura 24 - Rueda de olor compostaje ......................................................................................................... 73
Figura 25 - Dominio de modelación ............................................................................................................. 75
Figura 26 - Elevación de terreno del dominio ................................................................................................ 76
Figura 27 - Uso de suelo del dominio ........................................................................................................... 77
Figura 28 - Distribución de rosa de viento anual ........................................................................................... 78
Figura 29 - Comportamiento de campos de viento ........................................................................................ 86
Figura 30 - Distribución general de altura de mezcla (ortofotografías) ............................................................ 87
Figura 31 - Localización de estación meteorológica ....................................................................................... 93

**ÍNDICE ESQUEMA**
Esquema 1 - Método para la predicción de impactos por olor ........................................................................ 38

RESUMEN EJECUTIVO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 17 de 112

**1** **ANTECEDENTES**

En el marco de la Declaración de Impacto Ambiental (DIA) sometida al Sistema de Evaluación de Impacto
Ambiental (SEIA), Ecomaule S.A. ha solicitado a TSG Environmental SpA., área Envirometrika, actualizar la
modelación de impacto odorante del proyecto "Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje
y Valorización", incorporando la evaluación de dos nuevas fuentes "área de riego 1 y área de riego 2".

**1.1** **Antecedentes generales**

El proyecto se localiza en el fundo Palermo donde opera actualmente el Centro de Tratamiento de Residuos,
ubicado en la comuna de Río Claro, provincia de Talca, Región del Maule. La coordenada central la Planta se
describe en la siguiente tabla:

Tabla 10 - Coordenadas referenciales de localización del Proyecto

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|282.341|6.101.435|19 H|WGS 84|

Figura 10 - Localización del Proyecto

Fuente: Envirometrika - Google Earth, 2021.

ANTECEDENTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 18 de 112

**Descripción operacional del Proyecto en ejecución**

El Centro de Tratamiento de Residuos actualmente incluye un Relleno Sanitario para residuos sólidos
domiciliarios y asimilables, una Planta de Compostaje que actualmente opera mediante un proceso de
compostaje tradicional, y un Monorelleno de lodos sanitarios.

Actualmente los residuos orgánicos son sometidos a un proceso de compostaje, mientras que los lodos
sanitarios son tratados mediante proceso de biosecado para su posterior disposición final en
monorelleno, las canchas de compostaje y biosecado operan al aire libre.

La planta de tratamiento de lixiviados cuenta con un sistema de tratamiento biológico de aireación
extendida cumpliendo con la norma de descarga a cuerpos de aguas superficiales.

**1.2** **Antecedentes específicos**

El proyecto tiene como finalidad garantizar una operación sustentable en el tiempo, adoptando estándares
actualizados y tecnologías de alto nivel, dando cumplimiento a la normativa ambiental vigente.

El proyecto considera las siguientes obras:

 Aprovechamiento energético de los residuos orgánicos a través de la digestión anaeróbica, ya sea para

uso como energía eléctrica a través de un generador a biogás o como energía térmica para mantener la
temperatura de los reactores anaeróbicos.

 Valorización de residuos orgánicos mediante compostaje mejorado, para lo cual se considera la

construcción de galpones en 1 hectárea aproximadamente para confinar el compostaje en las primeras
semanas de tratamiento.

 Reciclaje de sólidos domiciliarios y asimilables recuperables, los cuales se encuentran preclasificados en

el origen y corresponden a cartón, papel, plástico, vidrio, madera y metal.

 Centro de residuos sólidos con tratamiento de residuos de la construcción y demolición RCD, de los cuales

se espera valorizar entre un 30 y 40%, se construirá un sector para la recuperación y valorización de
materiales y un sector para la disposición final de la fracción que no se pueda valorizar.

 Valorización del material del monorelleno y rediseño de alveolos 5-II, 6, 7, 8 y 9 del relleno sanitario.

 Mejoramiento de la planta de tratamiento de líquidos lixiviados, incorporando un estanque y una laguna

anaeróbica de pretratamiento de RILes.

ANTECEDENTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 19 de 112

**1.3** **Diagrama general de procesos**

Los diagramas de flujo de los procesos de compostaje y digestión anaeróbica se describen a continuación:

Figura 11 - Diagrama de proceso de compostaje

Fuente: DIA “Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización”.

ANTECEDENTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 20 de 112

Figura 12 - Diagrama de flujo de Digestión Anaeróbica

Fuente: DIA “Mejoramiento y Transformación Ecomaule: Plataforma de Reciclaje y Valorización”.

Uno de los aspectos relevantes del proyecto es el aprovechamiento energético de residuos orgánicos a través
de la digestión anaeróbica. Este proceso se lleva a cabo en un reactor cerrado hermético e impermeable,
donde se metaboliza la materia orgánica en ausencia de oxígeno. Del proceso de degradación se obtiene
biogás, de alto potencial calorífico, el cual es almacenado en gasómetro para su uso como combustible en
equipo de cogeneración eléctrica y térmica.

El efluente resultante de los digestores (digestato) será conducido a un post-digestor para su posterior
conducción a unidad de almacenamiento de digestato (riego/fertilización, compostaje y comercialización a
terceros) o deshidratado mecánico. De esta última unidad se obtiene digestato clarificado, el que será
canalizado mediante red de tuberías existentes o mediante camiones aljibe a la planta de tratamiento de
lixiviados o podrá ser usado como agua industrial dentro de los procesos del proyecto y para el riego de
digestato dentro de la misma planta.

ANTECEDENTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 21 de 112

Las siguientes tablas describen las fuentes odorantes identificadas en la operación actual y futura de la planta.

Tabla 11 - Fuentes odorantes - Situación actual

|ID|Área|Nombre fuente|Tipo de<br>fuente|Coordenadas UTM [m]<br>WGS84 19K|Col6|
|---|---|---|---|---|---|
|ID|Área|Nombre fuente|Tipo de<br>fuente|Este|Norte|
|1|Compostaje|Pila Lodo Agroindustrial - Edad 1|Difusa|282.608|6.101.746|
|2|2|Pila Lodo Agroindustrial - Edad 1|Difusa|282.477|6.101.593|
|3|3|Pila Lodo Agroindustrial - Edad 2|Difusa|282.491|6.101.572|
|4|4|Pila Lodo Agroindustrial - Edad 3a|Difusa|282.599|6.101.756|
|5|5|Pila Lodo Agroindustrial - Edad 3b|Difusa|282.671|6.101.810|
|6|6|Pila lodo sanitario - Edad 1 Curicó|Difusa|282.791|6.101.622|
|7|7|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|282.815|6.101.660|
|8|8|Pila lodo sanitario - Edad 2 Curicó|Difusa|282.743|6.101.660|
|9|9|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|282.771|6.101.696|
|10|10|Pila lodo sanitario - Edad 1 Curicó|Difusa|282.712|6.101.692|
|11|11|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|282.740|6.101.731|
|12|12|Pila lodo sanitario - Edad 2 Curicó|Difusa|282.682|6.101.715|
|13|13|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|282.705|6.101.743|
|14|14|Pila lodo sanitario - Edad 1 Curicó|Difusa|282.669|6.101.464|
|15|15|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|282.669|6.101.464|
|16|16|Pila lodo sanitario - Edad 2 Curicó|Difusa|282.712|6.101.566|
|17|17|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|282.644|6.101.488|
|18|18|Pila lodo sanitario - Edad 3 Curicó|Difusa|282.567|6.101.489|
|19|19|Pila lodo sanitario - Edad 3 Otras Localidades|Difusa|282.587|6.101.467|
|20|20|Pila lodo sanitario - Edad 1 Curicó|Difusa|282.587|6.101.503|
|21|21|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|282.606|6.101.483|
|22|22|Pila lodo sanitario - Edad 2 Curicó|Difusa|282.594|6.101.512|
|23|23|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|282.614|6.101.491|
|24|24|Pila lodo sanitario - Edad 1 Curicó|Difusa|282.637|6.101.675|
|25|25|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|282.556|6.101.580|
|26|26|Pila lodo sanitario - Edad 2 Curicó|Difusa|282.671|6.101.601|
|27|27|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|282.603|6.101.521|
|28|28|Pila lodo sanitario - Edad 3 Curicó|Difusa|282.759|6.101.572|
|29|29|Pila lodo sanitario - Edad 3 Otras Localidades|Difusa|282.766|6.101.566|
|30|PTRILes|Laguna de percolados|Difusa|282.122|6.101.571|
|31|31|Laguna de agua rechazo|Difusa|282.194|6.101.668|
|32|32|Reactor aerobio 1|Difusa|282.183|6.101.641|
|33|33|Reactor aerobio 2|Difusa|282.191|6.101.631|
|34|34|Clarificador|Difusa|282.199|6.101.628|
|35|35|Floculador|Difusa|282.206|6.101.636|
|36|36|Laguna lodos biológicos|Difusa|282.186|6.101.657|
|37|37|Laguna lodo físico/químico|Difusa|282.182|6.101.652|
|38|38|Lechos de secado 1|Difusa|282.212|6.101.589|
|39|39|Lechos de secado 2 (lavado de camiones)|Difusa|282.200|6.101.596|
|40|40|Laguna agua tratada|Difusa|282.165|6.101.663|
|41|Relleno|Monorelleno - Frente de trabajo|Difusa|282.277|6.101.239|
|42|42|Relleno Sanitario - Frente de trabajo|Difusa|282.314|6.101.479|

ANTECEDENTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 22 de 112

Tabla 12 - Fuentes odorantes - Situación futura

|ID|Área|Nombre fuente|Tipo de<br>fuente|Coordenadas UTM [m]<br>WGS84 19K|Col6|
|---|---|---|---|---|---|
|ID|Área|Nombre fuente|Tipo de<br>fuente|Este|Norte|
|1|Compostaje|Cancha de compostaje 1|Difusa|282.627|6.101.766|
|2|2|Cancha de compostaje 2|Difusa|282.745|6.101.658|
|3|3|Cancha de compostaje 3|Difusa|282.770|6.101.646|
|4|4|Cancha de compostaje 4|Difusa|282.623|6.101.534|
|5|5|Galpón de compostaje 1 (sist. de abatimiento)|Puntual|282.579|6.101.700|
|6|6|Galpón de compostaje 2 (sist. de abatimiento)|Puntual|282.591|6.101.720|
|7|7|Galpón de compostaje 3 (sist. de abatimiento)|Puntual|282.609|6.101.736|
|8|8|Galpón de compostaje 4 (sist. de abatimiento)|Puntual|282.623|6.101.755|
|9|Digestión|Estanque acumulación clarificado - Etapa 1|Difusa|282.607|6.101.593|
|10|10|Estanque acumulación de digestato - Etapa 1|Difusa|282.614|6.101.585|
|11|11|Contenedor deshidratado mecánico - Etapa 1|Difusa|282.610|6.101.606|
|12|12|Estanque acumulación clarificado - Etapa 2|Difusa|282.655|6.101.641|
|13|13|Contenedor deshidratado mecánico - Etapa 2|Difusa|282.615|6.101.613|
|14|14|Galpón de recepción (Sist. de abatimiento olores - Etapa 1)|Puntual|282.610|6.101.579|
|15|15|Galpón de recepción (Sist. de abatimiento olores - Etapa 2)|Puntual|282.651|6.101.629|
|16|16|Unidad de almacenamiento de digestato|Difusa|282.569|6.101.487|
|17|PTRILes|Laguna anaeróbica|Difusa|282.130|6.101.544|
|18|18|Laguna de percolados|Difusa|282.122|6.101.571|
|19|19|Reactor aerobio 1|Difusa|282.183|6.101.640|
|20|20|Reactor aerobio 2|Difusa|282.191|6.101.631|
|21|21|Reactor aerobio 3|Difusa|282.175|6.101.629|
|22|22|Reactor aerobio 4|Difusa|282.168|6.101.618|
|23|23|Clarificador|Difusa|282.198|6.101.627|
|24|24|Floculador|Difusa|282.206|6.101.635|
|25|25|Laguna lodos biológicos|Difusa|282.186|6.101.657|
|26|26|Laguna lodo físico/químico|Difusa|282.182|6.101.652|
|27|27|Laguna agua tratada|Difusa|282.165|6.101.662|
|28|Relleno|Alvéolo 7 - Frente de trabajo|Difusa|282.290|6.101.242|
|29|Riego|Zona de riego 1|Difusa|281.821|6.101.645|
|30|30|Zona de riego 2|Difusa|282.053|6.101.591|

ANTECEDENTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 23 de 112

**1.4** **Antecedentes para el área de influencia**

El presente estudio se basó en los lineamientos establecidos en la “Guía para la Descripción del Área de
Influencia” [10] y la “Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA” [11] del Servicio de
Evaluación Ambiental, como parte de la DIA. Lo anterior, abordando y justificando las letras a), c), d) y e)
del artículo 11 de la Ley No 19.300 [12], aplicables para la componente olor del proyecto en evaluación.

Basado en los Instrumentos de Planificación Territorial vigentes, el proyecto se emplaza a una distancia
aproximada de 2,6 [km] al noreste del límite urbano definido por el Plan Regulador Comunal de Río Claro.

Figura 13 - Localización del Proyecto según Límite Urbano de PRC de Río Claro

Fuente: Envirometrika - Google Earth, 2021.

10 Servicio de Evaluación Ambiental. (2017). Guía para la Descripción de la Calidad del Aire en el Área de Influencia de Proyectos que Ingresan

al SEIA. Departamento de Estudios y Desarrollo - División de Evaluación y Participación Ciudadana. Chile.
11 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
12 Ministerio del Medio Ambiente. (2011). Ley No 19.300, sobre Bases Generales del Medio Ambiente - Ley Orgánica de la Superintendencia

del Medio Ambiente. División Jurídica del Medio Ambiente. Chile.

ANTECEDENTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 24 de 112

**2** **OBJETIVOS**

**2.1** **Objetivo general**

Proyectar el alcance odorante del Centro de Tratamiento de Residuos, bajo condición operacional actual y
futura definidas por el Titular.

**2.2** **Objetivos específicos**

 Recopilación de antecedentes operacionales de las fuentes odorantes del Centro de Tratamiento de

Residuos, incluyendo zonas de riego 1 y 2.

 Recopilación de emisiones de referencia aplicables al proyecto.

 Caracterización estructural, espacial y operacional de fuentes de emisión de olor

 Proyectar el alcance odorante actual y futura, vía modelación de dispersión odorante, según criterio de

calidad de C P98-1hr = 3, 4 y 5 [ou E /m [3] ].

 Determinar el área de influencia del proyecto para la componente olor.

 Evaluar alcance odorante de las emisiones del proyecto en actual y futuro.

 Cuantificar niveles de concentración de olor generados por el proyecto en receptores.

OBJETIVOS www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 25 de 112

**3** **ESTIMACIÓN DE EMISIONES**

De acuerdo con lo señalado en la “Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA” [13], las
emisiones de referencia son aquellas que han sido estimadas a partir de la toma de muestras de olor en la fuente
y su respectiva caracterización. La selección y aplicación de emisiones de referencia, se realiza sobre la base de
proyectos o actividades similares al proyecto que se somete a evaluación ambiental. Es importante considerar que
las condiciones de operación o funcionamiento de las fuentes existentes o de referencia también sean análogas
al proyecto.

Respecto al uso de factores de emisión de olor, se define como la relación entre la cantidad de contaminante
emitido a la atmósfera y una unidad de actividad. La unidad de actividad puede consistir en datos de producción,
horas de operación de la fuente, área superficial involucrada u otros.

El uso de factores de emisión es aconsejable sólo en proyectos nuevos, y siempre que no se cuente con emisiones
de referencia, en este caso, se deben utilizar preferentemente factores publicados por agencias estatales de
protección del medio ambiente, normas o guías técnicas relacionadas [14] .

Por lo tanto, para representar las condiciones operacionales actuales y futuras se consideró el uso de emisiones
de referencia obtenidas del estudio “Levantamiento de Emisión de Olor - Ecomaule S.A.” [15], cuyas emisiones fueron
muestreadas y analizadas, bajo la normativa de olor vigente NCh 3190:2010 [16] y NCh 3386:2015 [17] .

**3.1** **Emisiones de referencia**

Los valores de emisión utilizados para caracterizar el ciclo de emisión de olor de las fuentes asociadas a la
operación del Centro de Manejo de Residuos de Ecomaule S.A., provienen del muestreo realizado entre 22 y
23 de mayo del 2019.
Dado que el proyecto futuro contempla la implementación de tecnología de abatimiento de olor, se consideró
información de eficiencia de remoción de olor proveniente de los siguientes estudios y fichas técnicas
proporcionadas por el Titular según se describe en la siguiente tabla:

Tabla 13 - Proyecto de referencia aplicable

|Proyecto|Tipo de<br>estudio|Establecimiento|Año de<br>ejecución|Norma<br>aplicada al<br>muestreo|Norma<br>aplicada al<br>análisis<br>olfatométrico|Referencia aplicada en|
|---|---|---|---|---|---|---|
|P5838|EO|Centro de Manejo<br>de Residuos<br>Ecomaule|2019|NCh3386:2015<br>VDI<br>4285:2011 -|NCh3190:2010|Fuentes de emisión|
|P5052|EO|Invennto|2017|/a|NCh3190:2010|Cobertura flotante|
|EC-VLT-<br>FB20|Ficha<br>Técnica|Ecozone|2020|/b|-|Abatimiento galpón de<br>compostaje y recepción|

/a Muestreo realizado por solicitante Invennto.
/b Referencia de eficiencia de remoción de olor.

13 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Chile.
14 Ibid.
15 Muestreo olfatométrico ejecutado en año 2019; Informe presentado en año 2020.
16 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.
17 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 26 de 112

El levantamiento de emisión de olor en Centro de Manejo de Residuos se realizó acorde a la metodología de
muestreo NCh 3386:2015 [18] y NCh3431:2020 [19] . Las muestras fueron analizadas en laboratorio para la
determinación de la concentración de olor por olfatometría dinámica acorde a los estándares indicados en la
NCh 3190:2010 [20] .

Tabla 14 - Emisiones de referencia aplicados en Situación actual

|ID|Área|Fuente|EO por sup. [ou/m2s]/a<br>E|Tasa de Emisión de Olor<br>[ou/s]/b<br>E|
|---|---|---|---|---|
|1|Compostaje|Pila Lodo Agroindustrial - Edad 1|14,7|96.402,60|
|2|2|Pila Lodo Agroindustrial - Edad 1|14,7|85.127,70|
|3|3|Pila Lodo Agroindustrial - Edad 2|8,3|61.876,50|
|4|4|Pila Lodo Agroindustrial - Edad 3a|1,6|1.920,00|
|5|5|Pila Lodo Agroindustrial - Edad 3b|1,6|1.920,00|
|6|6|Pila lodo sanitario - Edad 1 Curicó|5,7|19.704,90|
|7|7|Pila lodo sanitario - Edad 1 Otras Localidades|3,8|39.409,80|
|8|8|Pila lodo sanitario - Edad 2 Curicó|11,4|23.697,75|
|9|9|Pila lodo sanitario - Edad 2 Otras Localidades|5,9|36.793,88|
|10|10|Pila lodo sanitario - Edad 1 Curicó|5,7|6.421,05|
|11|11|Pila lodo sanitario - Edad 1 Otras Localidades|3,8|12.842,10|
|12|12|Pila lodo sanitario - Edad 2 Curicó|11,4|11.060,85|
|13|13|Pila lodo sanitario - Edad 2 Otras Localidades|5,9|17.173,43|
|14|14|Pila lodo sanitario - Edad 1 Curicó|5,7|6.059,10|
|15|15|Pila lodo sanitario - Edad 1 Otras Localidades|3,8|12.118,20|
|16|16|Pila lodo sanitario - Edad 2 Curicó|11,4|13.913,70|
|17|17|Pila lodo sanitario - Edad 2 Otras Localidades|5,9|21.602,85|
|18|18|Pila lodo sanitario - Edad 3 Curicó|5,6|3.579,80|
|19|19|Pila lodo sanitario - Edad 3 Otras Localidades|1,7|3.260,18|
|20|20|Pila lodo sanitario - Edad 1 Curicó|5,7|1.913,78|
|21|21|Pila lodo sanitario - Edad 1 Otras Localidades|3,8|3.827,55|
|22|22|Pila lodo sanitario - Edad 2 Curicó|11,4|4.312,05|
|23|23|Pila lodo sanitario - Edad 2 Otras Localidades|5,9|6.695,03|
|24|24|Pila lodo sanitario - Edad 1 Curicó|5,7|11.347,28|
|25|25|Pila lodo sanitario - Edad 1 Otras Localidades|3,8|22.694,55|
|26|26|Pila lodo sanitario - Edad 2 Curicó|11,4|19.998,45|
|27|27|Pila lodo sanitario - Edad 2 Otras Localidades|5,9|31.050,23|
|28|28|Pila lodo sanitario - Edad 3 Curicó|5,6|2.913,40|
|29|29|Pila lodo sanitario - Edad 3 Otras Localidades|1,7|2.653,28|
|30|PTRILes|Laguna de percolados|81,6|81.600,00|
|31|31|Laguna de agua rechazo|81,6|12.566,40|
|32|32|Reactor aerobio 1|31,8|2.497,57|
|33|33|Reactor aerobio 2|31,8|2.497,57|
|34|34|Clarificador|14,2|343,64|
|35|35|Floculador|14,2|100,37|
|36|36|Laguna lodos biológicos|21,2|1.433,12|
|37|37|Laguna lodo físico/químico|2,3|140,76|
|38|38|Lechos de secado 1|4,2|1.268,40|
|39|39|Lechos de secado 2 (lavado de camiones)|32,8|8.757,60|
|40|40|Laguna agua tratada|2,4|904,8|
|41|Relleno Sanitario|Monorelleno - Frente de trabajo|11,1|50.038,80|
|42|42|Relleno Sanitario - Frente de trabajo|21,3|18.105,00|

/a Emisión de Olor por superficie expuesta al ambiente.
/b Contribución de olor al ambiente.

18 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para olfatometría. Chile.
19 Instituto Nacional de Normalización. (2020). NCh 3431:2020 Calidad del aire - Muestreo para fuentes fugitivas o de volumen. Chile.
20 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la concentración de olor por olfatometría

dinámica. Chile.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 27 de 112

Tabla 15 - Emisiones de referencia aplicados en la Situación futura

|ID|Área|Fuente|EO por sup. [ou/m2s]/a<br>E|Tasa de Emisión de<br>Olor [ou/s]/b<br>E|
|---|---|---|---|---|
|1|Compostaje|Cancha de compostaje 1|0,53/c|5.283,75|
|2|2|Cancha de compostaje 2|0,53/c|2.610,30|
|3|3|Cancha de compostaje 3|0,53/c|7.441,46|
|4|4|Cancha de compostaje 4|0,53/c|8.420,32|
|5|5|Galpón de compostaje 1 (sist. de abatimiento)|1.128,86|1.276,71/d|
|6|6|Galpón de compostaje. 2 (sist. de abatimiento)|1.438,43|1.626,82/d|
|7|7|Galpón de compostaje 3 (sist. de abatimiento)|1.438,43|1.626,82/d|
|8|8|Galpón de compostaje 4 (sist. de abatimiento)|1.438,43|1.626,82/d|
|9|Digestión|Estanque de acumulación clarificado - Etapa 1|0,32/e|64,34|
|10|10|Estanque de acumulación de digestato - Etapa 1|0,32/e|2,94|
|11|11|Contenedor deshidratado mecánico - Etapa 1|0,32/e|4,07|
|12|12|Estanque de acumulación clarificado - Etapa 2|0,32/e|64,34|
|13|13|Contenedor deshidratado mecánico - Etapa 2|0,32/e|4,07|
|14|14|Galpón de recepción (Sist. de abatimiento olores - Etapa 1)|47,23|53,42/f|
|15|15|Galpón de recepción (Sist. de abatimiento olores - Etapa 2)|47,23|53,42/f|
|16|16|Unidad de almacenamiento de digestato|0,32/e|1.705,28|
|17|PTRILes|Laguna anaeróbica|5,71/f|11.424,00|
|18|18|Laguna de percolados|5,71/f|5.710,00|
|19|19|Reactor aerobio 1|19,08/g|1.498,54|
|20|20|Reactor aerobio 2|19,08/g|1.498,54|
|21|21|Reactor aerobio 3|19,08/g|1.498,54|
|22|22|Reactor aerobio 4|19,08/g|1.498,54|
|23|23|Clarificador|8,52/g|206,18|
|24|24|Floculador|8,52/g|60,22|
|25|25|Laguna lodos biológicos|21,2/h|1.433,12|
|26|26|Laguna lodo físico/químico|2,3/h|140,76|
|27|27|Laguna agua tratada|0,25/i|94,25|
|28|Relleno|Alvéolo 7 - Frente de trabajo|21,3/h|18.105,00|
|28|Riego|Zona de riego 1|0,32/h|4.217,60|
|28|28|Zona de riego 2|0,32/h|5.729,96|

/a Emisión de Olor por superficie expuesta al ambiente.
/b Contribución de olor al ambiente.
/c Emisión de Olor promedio, basado en curva de estabilización de pilas de compostaje con aireación (ver anexo 2)
/d Tasa de Emisión de Olor, basado en compostaje confinado de pilas agroindustrial con implementación de sistema de abatimiento

fotocatalítico UV (ver anexo 2).
/e Emisión de Olor de digestato de biodigestor anaeróbico de purines 21 .
/f Emisión de Olor, basado en implementación de cubierta flotante (ver anexo 2).
/g Emisión de Olor, basado en optimización de procesos (ver anexo 2).
/h Emisión de Olor, basado en muestreo realizado 2019.
/i Emisión de Olor, basado en factor tranque de agua tratada de Ecobio. 22
/e Emisión de Olor, basado en digestato tratado desde unidades de proceso de digestión anaeróbica.

21 Coexca S.A, (2019). DIA: Mejora del desempeño ambiental mediante biodigestor anaeróbico, modernización y ampliación plantel de cerdos

Santa Francisca. Chile.
22 Dunabin, E., McIntyre, A., Longhurst, P. (2017). Seafield Wastewater Treatment Works Strategic Odour Review. Cranfield University - Amec

Foster Wheeler Environment & Infrastructures UK Limited. United Kingdom.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 28 de 112

**3.2** **Emisiones según olor simple o compuesto**

De la Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA (2017-página 18), se tiene que:
El olor simple es el que percibe el olfato como consecuencia de la emisión de un compuesto químico o
sustancia olorosa determinada. Los olores de tipo simple suelen ser fácilmente identificables (Díaz et al.,
2013), por ejemplo, el ácido sulfhídrico (H 2 S) siendo una sustancia olorosa que se identifica fácilmente con
el descriptor de huevos podridos. En cambio, el olor compuesto es el que se percibe como consecuencia de
la mezcla de más de un olor simple, pudiendo producirse fenómenos de sinergias, interferencias e
inhibiciones, y por lo mismo, en la percepción del olor compuesto no siempre es fácil definir y atribuir las
moléculas que lo causan, no pudiendo identificarlo con un único descriptor de olor.

El presente proyecto considera una serie de operaciones potencialmente generadoras de olor atribuibles a
olores compuestos ya que no es una actividad que genera un olor simple o una única sustancia o compuesto

gaseoso.

Existe una forma de acceder al menos a la familia de compuestos e idealmente al gas precursor del olor
analizando los descriptores o notas de olor con la rueda de olor, en este caso se utilizó la rueda de olor
asociada al proceso de compostaje, la cual sería asimilable a la disposición de residuos sólidos domiciliarios
y asimilables, planta de compostaje y tratamiento de lodos sanitarios. A continuación, se indican las notas de
olor consideradas como ofensivas, asimilables al proyecto:

 Sulfuroso.

 Descomposición.

 - Agrio.

 Ácido.

 Percolado.

 - Terroso.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 29 de 112

A continuación, se detallan las fuentes odorantes del proyecto:

Tabla 16 - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 1

|Requisito|Col2|Pila Lodo<br>Agroindustrial -<br>Edad 1|Pila Lodo<br>Agroindustrial -<br>Edad 2|Pila Lodo<br>Agroindustrial -<br>Edad 3|Pila lodo<br>sanitario -<br>Edad 1 Curicó|Pila lodo<br>sanitario - Edad<br>1 Otras<br>Localidades|Pila lodo<br>sanitario -<br>Edad 2 Curicó|Pila lodo<br>sanitario - Edad<br>2 Otras<br>Localidades|Pila lodo<br>sanitario -<br>Edad 3 Curicó|Pila lodo<br>sanitario -<br>Edad 3 Otras<br>Localidades|
|---|---|---|---|---|---|---|---|---|---|---|
|Fase del proyecto que genera<br>olor|Fase del proyecto que genera<br>olor|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Actividad que genera emisiones<br>de olor|Actividad que genera emisiones<br>de olor|Compostaje en<br>cancha|Compostaje en<br>cancha|Compostaje en<br>cancha|Biosecado en<br>cancha|Biosecado en<br>cancha|Biosecado en<br>cancha|Biosecado en<br>cancha|Biosecado en<br>cancha|Biosecado en<br>cancha|
|Identificación del material o<br>sustancia olorosa|Identificación del material o<br>sustancia olorosa|Lodo<br>Agroindustrial|Lodo<br>Agroindustrial|Lodo<br>Agroindustrial|Lodo Sanitario|Lodo Sanitario|Lodo Sanitario|Lodo Sanitario|Lodo Sanitario|Lodo Sanitario|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|
|Régimen de<br>emisión de<br>olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de<br>olor|Horas de<br>operación|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|
|Régimen de<br>emisión de<br>olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor [ouE/m2*s]|Emisión de olor [ouE/m2*s]|14,70|8,30|1,60|5,70|3,80|11,4|5,90|5,60|1,70|
|Tasa de emisión de olor|Tasa de emisión de olor|181.530,30|61.876,50|3.840,00|45.446,10|90.892,20|72.982,80|113.315,40|6.493,20|5.913,45|
|Calidad|Calidad|Humedad,<br>percolado,<br>agrio|Basura,<br>descomposición,<br>agrio|Tierra,<br>humedad,<br>basura|Humedad,<br>mohoso, tierra|Descomposición,<br>tierra, humedad|Tierra,<br>humedad,<br>vegetales<br>descomp.|Descomposición,<br>agrio, podrido|Humedad,<br>tierra|Humedad,<br>tierra,<br>detergente|

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 30 de 112

Tabla 17 - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 2

|Requisito|Col2|Laguna de<br>percolados|Laguna de<br>agua rechazo|Reactor<br>aerobio 1|Reactor<br>aerobio 2|Clarificador|Floculador|Laguna lodos<br>biológicos|Laguna lodos<br>físico/químico|Lecho de<br>secado 1|
|---|---|---|---|---|---|---|---|---|---|---|
|Fase del proyecto que genera<br>olor|Fase del proyecto que genera<br>olor|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Actividad que genera emisiones<br>de olor|Actividad que genera emisiones<br>de olor|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|
|Identificación del material o<br>sustancia olorosa|Identificación del material o<br>sustancia olorosa|RILes|RILes|RILes|RILes|RILes|RILes|RILes|RILes|RILes|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|
|Régimen de<br>emisión de olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de olor|Horas de<br>operación|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|
|Régimen de<br>emisión de olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor [ouE/m2*s]|Emisión de olor [ouE/m2*s]|81,60|81,60|31,80|31,80|14,20|14,20|21,20|2,30|4,20|
|Tasa de emisión de olor|Tasa de emisión de olor|81.600,00|12.566,00|2.497,57|2.497,57|343,64|100,37|1.433.12|140,76|1.268,40|
|Calidad|Calidad|Ácido, basura,<br>fermentación|Ácido, basura,<br>fermentación|Detergente,<br>humedad,<br>ácido|Detergente,<br>humedad,<br>ácido|Humedad,<br>ácido|Humedad,<br>ácido|Sulfuroso, gas,<br>percolado|Tierra,<br>humedad|Humedad,<br>rancio, tierra|

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 31 de 112

Tabla 18 - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 3

|Requisito|Col2|Lecho de<br>secado 2<br>(lavado de<br>camiones)|Laguna de<br>agua tratada|Monorelleno -<br>Frente de<br>trabajo|Relleno<br>sanitario -<br>Frente de<br>trabajo|
|---|---|---|---|---|---|
|Fase del proyecto que genera<br>olor|Fase del proyecto que genera<br>olor|Operación|Operación|Operación|Operación|
|Actividad que genera emisiones<br>de olor|Actividad que genera emisiones<br>de olor|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Disposición de<br>residuos<br>sólidos|Disposición de<br>residuos<br>sólidos|
|Identificación del material o<br>sustancia olorosa|Identificación del material o<br>sustancia olorosa|RILes|Agua tratada|Residuos<br>sólidos<br>(orgánicos)|Residuos<br>sólidos<br>(orgánicos)|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Difusa|
|Régimen de<br>emisión de olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de olor|Horas de<br>operación|24 [h]|24 [h]|24 [h]|24 [h]|
|Régimen de<br>emisión de olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor [ouE/m2*s]|Emisión de olor [ouE/m2*s]|32,80|2,40|11,10|21,30|
|Tasa de emisión de olor|Tasa de emisión de olor|8.757,60|904,80|50.038,80|18.105,00|
|Calidad|Calidad|Percolado,<br>humedad, gas|Tierra,<br>humedad|Terroso,<br>humedad|Percolado,<br>fermentación|

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 32 de 112

Tabla 19 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 1

|Requisito|Col2|Cancha de<br>compostaje 1|Cancha de<br>compostaje 2|Cancha de<br>compostaje 3|Cancha de<br>compostaje 4|Galpón<br>compostaje 1<br>(sist. de<br>abatimiento)|Galpón<br>compostaje 2<br>(sist. de<br>abatimiento)|Galpón<br>compostaje 3<br>(sist. de<br>abatimiento)|Galpón<br>compostaje 4<br>(sist. de<br>abatimiento)|Estanque de<br>acumulación<br>clarificado -<br>Etapa 1|
|---|---|---|---|---|---|---|---|---|---|---|
|Fase del proyecto que genera<br>olor|Fase del proyecto que genera<br>olor|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Actividad que genera emisiones<br>de olor|Actividad que genera emisiones<br>de olor|Estabilización<br>de compost en<br>cancha|Estabilización<br>de compost en<br>cancha|Estabilización<br>de compost en<br>cancha|Estabilización<br>de compost en<br>cancha|Compostaje<br>aireado<br>(confinado)|Compostaje<br>aireado<br>(confinado)|Compostaje<br>aireado<br>(confinado)|Compostaje<br>aireado<br>(confinado)|Digestión<br>anaeróbica|
|Identificación del material o<br>sustancia olorosa|Identificación del material o<br>sustancia olorosa|Compost|Compost|Compost|Compost|Compost|Compost|Compost|Compost|Digestato|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Difusa|Puntual|Puntual|Puntual|Puntual|Difusa|
|Régimen de<br>emisión de olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de olor|Horas de<br>operación|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|
|Régimen de<br>emisión de olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor [ouE/m2*s]|Emisión de olor [ouE/m2*s]|0,53|0,53|0,53|0,53|1.128,86|1.438,43|1.438,43|1.438,43|0,32|
|Tasa de emisión de olor|Tasa de emisión de olor|5.283,75|2.610,30|7.441,46|8.420,32|1.276,71|1.626,82|1.626,82|1.626,82|64,34|
|Calidad|Calidad|/a|/a|/a|/a|/a|/a|/a|/a|/a|

/a Fuente inexistente/modificada/optimizada que forma parte de proyecto futuro.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 33 de 112

Tabla 20 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 2

|Requisito|Col2|Estanque de<br>acumulación<br>digestato -<br>Etapa 1|Cont.<br>deshidratado<br>mecánico -<br>Etapa 1|Estanque de<br>acumulación<br>clarificado -<br>Etapa 2|Cont.<br>deshidratado<br>mecánico -<br>Etapa 2|Galpón de<br>recepción (sist.<br>de abatimiento<br>etapa 1)|Galpón de<br>recepción (sist.<br>de abatimiento<br>etapa 1)|Unidad de<br>almacenamiento<br>de digestato|Laguna<br>anaeróbica|Laguna de<br>percolados|
|---|---|---|---|---|---|---|---|---|---|---|
|Fase del proyecto que genera<br>olor|Fase del proyecto que genera<br>olor|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Actividad que genera emisiones<br>de olor|Actividad que genera emisiones<br>de olor|Digestión<br>anaeróbica|Digestión<br>anaeróbica|Digestión<br>anaeróbica|Digestión<br>anaeróbica|Digestión<br>anaeróbica|Digestión<br>anaeróbica|Digestión<br>anaeróbica|Tratamiento de<br>RILes|Tratamiento de<br>RILes|
|Identificación del material o<br>sustancia olorosa|Identificación del material o<br>sustancia olorosa|Digestato|Digestato|Digestato|Digestato|Digestato|Digestato|Digestato|RILes|RILes|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Difusa|Puntual|Puntual|Difusa|Difusa|Difusa|
|Régimen de<br>emisión de<br>olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de<br>olor|Horas de<br>operación|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|
|Régimen de<br>emisión de<br>olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor [ouE/m2*s]|Emisión de olor [ouE/m2*s]|0,32|0,32|0,32|0,32|47,23|47,23|0,32|5,71|5,71|
|Tasa de emisión de olor|Tasa de emisión de olor|2,94|4,07|64,34|4,07|53,42|53,42|1.705,28|11.424,00|5.710,00|
|Calidad<br>|Calidad<br>|/a <br>|/a <br>|/a <br>|/a|/a|/a|/a|/a|/a|

/a Fuente inexistente/modificada/optimizada que forma parte de proyecto futuro.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 34 de 112

Tabla 21 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 3

|Requisito|Col2|Reactor<br>aerobio 1|Reactor<br>aerobio 2|Clarificador|Floculador|Laguna lodos<br>biológicos|Laguna lodo<br>físico/químico|Laguna de agua<br>tratada|Reactor<br>aerobio 3|Reactor<br>aerobio 4|
|---|---|---|---|---|---|---|---|---|---|---|
|Fase del proyecto que genera<br>olor|Fase del proyecto que genera<br>olor|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Actividad que genera emisiones<br>de olor|Actividad que genera emisiones<br>de olor|Tratamiento<br>de RILes|Tratamiento<br>de RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|Tratamiento de<br>RILes|
|Identificación del material o<br>sustancia olorosa|Identificación del material o<br>sustancia olorosa|RILes|RILes|RILes|RILes|RILes|RILes|RILes|RILes|RILes|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|Difusa|
|Régimen de<br>emisión de<br>olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de<br>olor|Horas de<br>operación|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|24 [h]|
|Régimen de<br>emisión de<br>olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|12 meses|
|Emisión de olor [ouE/m2*s]|Emisión de olor [ouE/m2*s]|19,08|19,08|8,52|8,52|21,20|2,30|0,25|19,08|19,08|
|Tasa de emisión de olor|Tasa de emisión de olor|1.498,54|1.498,54|206,18|60,22|1.433,12|140,76|94,25|1.498,54|1.498,54|
|Calidad<br>|Calidad<br>|/a <br>|/a <br>|/a <br>|/a|/a|/a|/a|/a|/a|

/a Fuente inexistente/modificada/optimizada que forma parte de proyecto futuro.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 35 de 112

Tabla 22 - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 4

|Requisito|Col2|Alvéolo 7 -<br>Frente de<br>trabajo|Zona de<br>riego 1|Zona de<br>riego 2|
|---|---|---|---|---|
|Fase del proyecto que genera<br>olor|Fase del proyecto que genera<br>olor|Operación|Operación|Operación|
|Actividad que genera emisiones<br>de olor|Actividad que genera emisiones<br>de olor|Disposición de<br>residuos<br>sólidos|Riego de<br>digestato|Riego de<br>digestato|
|Identificación del material o<br>sustancia olorosa|Identificación del material o<br>sustancia olorosa|Residuos<br>sólidos|Digestato<br>tratado|Digestato<br>tratado|
|Tipo de fuente|Tipo de fuente|Difusa|Difusa|Difusa|
|Régimen de<br>emisión de<br>olor|Ciclo<br>operacional|Continuo|Continuo|Continuo|
|Régimen de<br>emisión de<br>olor|Horas de<br>operación|24 [h]|24 [h]|24 [h]|
|Régimen de<br>emisión de<br>olor|Frecuencia<br>mensual|12 meses|12 meses|12 meses|
|Emisión de olor [ouE/m2*s]|Emisión de olor [ouE/m2*s]|21,30|0,32|0,32|
|Tasa de emisión de olor|Tasa de emisión de olor|18.105,00|4.217,60|5.729,96|
|Calidad|Calidad|/a|/a|/a|

/a Fuente inexistente/modificada/optimizada que forma parte de proyecto futuro.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 36 de 112

**3.3** **Ranking de emisiones**

Una fuente con la mayor concentración no necesariamente se relaciona con una mayor emisión, ya que esta
última dependerá de sus características operacionales y estructurales. A su vez, una fuente con la mayor
emisión no siempre genera mayor exposición en las zonas de percepción de olor, ya que éste último
dependerá de diversos factores como: variables meteorológicas, geográficas y topográficas de la zona en
estudio, las características particulares del terreno, de emplazamiento de las fuentes, de la zona de inmisión,
las características estructurales de las fuentes, como la altura y el área de exposición. También influye el tipo
de fuente ya sea puntual, difusa o fugitiva.

Todo lo anterior deriva en que un mismo valor de emisión puede generar un mayor o menor nivel de
exposición dependiendo de las características antes mencionadas. Por lo tanto, mediante la modelación de
esta emisión, se pueden determinar las fuentes que generen mayores niveles de exposición, y en cuál de
éstas es recomendable realizar modificaciones estructurales u operacionales para poder obtener una
reducción relevante en el área de percepción.

A continuación, se indican las TEO [ou E /s] para cada fuente emisora, considerados en los 2 escenarios
operacionales evaluados: actual y futuro. Las fuentes emisoras están ordenadas en forma descendente en
función de su valor de TEO.

Tabla 23 - Ranking TEO [ou E /s] por fuente modelada - Situación actual

|Unidad|EO<br>[ou /m2*s]<br>E|TEO [ou /s]<br>E|% TEO|% TEO<br>acum.|
|---|---|---|---|---|
|Pila Lodo Agroindustrial - Edad 1|14,70|181.530,30|23,81%|23,81%|
|Pila lodo sanitario - Edad 2 Otras Localidades|5,90|113.315,40|14,86%|38,67%|
|Pila lodo sanitario - Edad 1 Otras Localidades|3,80|90.892,20|11,92%|50,59%|
|Laguna de percolados|81,60|81.600,00|10,70%|61,29%|
|Pila lodo sanitario - Edad 2 Curicó|11,40|72.982,80|9,57%|70,86%|
|Pila Lodo Agroindustrial - Edad 2|8,30|61.876,50|8,11%|78,97%|
|Monorelleno - Frente de trabajo|11,10|50.038,80|6,56%|85,53%|
|Pila lodo sanitario - Edad 1 Curicó|5,70|45.446,10|5,96%|91,49%|
|Relleno Sanitario - Frente de trabajo|21,30|18.105,00|2,37%|93,87%|
|Laguna de agua rechazo|81,60|12.566,40|1,65%|95,52%|
|Lechos de secado 2 (lavado de camiones)|32,80|8.757,60|1,15%|96,66%|
|Pila lodo sanitario - Edad 3 Curicó|5,60|6.493,20|0,85%|97,52%|
|Pila lodo sanitario - Edad 3 Otras Localidades|1,70|5.913,45|0,78%|98,29%|
|Pila Lodo Agroindustrial - Edad 3|1,60|3.840,00|0,50%|98,80%|
|Reactor aerobio 1|31,80|2.497,57|0,33%|99,12%|
|Reactor aerobio 2|31,80|2.497,57|0,33%|99,45%|
|Laguna lodos biológicos|21,20|1.433,12|0,19%|99,64%|
|Lechos de secado 1|4,20|1.268,40|0,17%|99,80%|
|Laguna agua tratada|2,40|904,80|0,12%|99,92%|
|Clarificador|14,20|343,64|0,05%|99,97%|
|Laguna lodo físico/químico|2,30|140,76|0,02%|99,99%|
|Floculador|14,20|100,37|0,01%|100,00%|

**TEO Total** **762.544** **100%**

EO: Emisión Odorante
TEO: Tasa de Emisión de Olor.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 37 de 112

Tabla 24 - Ranking TEO [ou E /s] por fuente modelada - Situación futura

|Unidad|EO [ou/m2*s]<br>E|TEO [ou/s]<br>E|% TEO|% TEO<br>acumulado|
|---|---|---|---|---|
|Alvéolo 7 - Frente de trabajo|21,30|18.105,00|21,30%|21,30%|
|Laguna de anaeróbica|5,71|11.424,00|13,44%|34,75%|
|Cancha de compostaje 4|0,53|8.420,32|9,91%|44,66%|
|Cancha de compostaje 3|0,53|7.441,46|8,76%|53,41%|
|Zona de riego 2|0,32|5.729,96|6,74%|60,16%|
|Laguna de percolados|5,71|5.710,00|6,72%|66,88%|
|Cancha de compostaje 1|0,53|5.283,75|6,22%|73,09%|
|Zona de riego 1|0,32|4.217,60|4,96%|78,06%|
|Cancha de compostaje 2|0,53|2.610,30|3,07%|81,13%|
|Unidad de alm. de digestato|0,32|1.705,28|2,01%|83,13%|
|Galpón de comp. 2 (sist. de abatimiento)|1.438,43|1.626,82|1,91%|85,05%|
|Galpón de comp. 3 (sist. de abatimiento)|1.438,43|1.626,82|1,91%|86,96%|
|Galpón de comp. 4 (sist. de abatimiento)|1.438,43|1.626,82|1,91%|88,88%|
|Reactor aerobio 1|19,08|1.498,54|1,76%|90,64%|
|Reactor aerobio 2|19,08|1.498,54|1,76%|92,40%|
|Reactor aerobio 3|19,08|1.498,54|1,76%|94,17%|
|Reactor aerobio 4|19,08|1.498,54|1,76%|95,93%|
|Laguna lodos biológicos|21,20|1.433,12|1,69%|97,62%|
|Galpón de comp. 1 (sist. de abatimiento)|1.128,86|1.276,71|1,50%|99,12%|
|Clarificador|8,52|206,18|0,24%|99,36%|
|Laguna lodo físico/químico|2,30|140,76|0,17%|99,53%|
|Laguna agua tratada|0,25|94,25|0,11%|99,64%|
|Est. acumulación clarificado - Etapa 1|0,32|64,34|0,08%|99,71%|
|Est. acumulación clarificado - Etapa 2|0,32|64,34|0,08%|99,79%|
|Floculador|8,52|60,22|0,07%|99,86%|
|Sistema de abatimiento olores - Etapa 1|47,23|53,42|0,06%|99,92%|
|Sistema de abatimiento olores - Etapa 2|47,23|53,42|0,06%|99,99%|
|Cont. deshidratado mecánico - Etapa 1|0,32|4,07|0,00%|99,99%|
|Cont. deshidratado mecánico - Etapa 2|0,32|4,07|0,00%|100,00%|
|Est. acumulación de disgestato - Etapa 1|0,32|2,94|0,00%|100,00%|

**TEO Total** **84.980** **100%**

EO: Emisión Odorante
TEO: Tasa de Emisión de Olor.

ESTIMACIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 38 de 112

**4** **PREDICCIÓN DE IMPACTOS POR OLOR**

**4.1** **Metodologías para la predicción de impactos por olor**

La metodología para realizar la predicción de impactos por olor del presente estudio sigue los lineamientos
de la “Guía para la predicción y evaluación de impactos por olor en el SEIA” [23], en la cual se presentan los
métodos que se utilizan para la predicción de impactos por olor, donde se desarrollan las obras o acciones
contenidas en un proyecto o actividad tendientes a materializar una o más de sus fases de operación, como
se observa en la siguiente figura:

Esquema 1 - Método para la predicción de impactos por olor

Fuente: Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA [24]

23 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Ministerio del Medio

Ambiente. Chile.
24 Ibid.

PREDICCIÓN DE IMPACTOS POR OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 39 de 112

**4.2** **Determinación del área de influencia del proyecto**

**Descripción del área de influencia según elementos del medio ambiente**

Tal como señala la Guía de Olores [25] (SEA, 2017), las personas son las que perciben el olor y, por lo
tanto, son las receptoras de impactos por este tipo de emisiones. En coherencia a lo anterior, se adapta
al ámbito de olores el concepto de la norma de emisión de ruido [26], la cual define como receptor toda
persona que habite, resida o permanezca en un recinto, ya sea en un domicilio particular o en un lugar
de trabajo, que esté o pueda estar expuesta a olores generados por una fuente emisora de olor
externa. De acuerdo con lo establecido en el artículo 11 de la Ley N° 19.300 [27], las personas receptoras
de impactos por olor se asocian con los siguientes elementos del medio ambiente:

 Población, en cuanto a salud de la población (letra a).

 - Grupos humanos, en cuanto a sus sistemas de vida y costumbres (letra c).

 Población protegida (letra d).

 Visitantes o turistas, en cuanto componen el valor turístico de una zona (letra e).

**Identificación de receptores de olor**

Los receptores de olor corresponden a las personas que perciben el olor y, por lo tanto, los posibles
impactos por emisiones de esta componente. Además de la presencia de personas, también se debe
considerar como receptores, los sitios donde los grupos humanos realizan sus actividades, incluyendo
actividades que desarrollan los visitantes o turista, por ejemplo: viviendas; instalaciones asociadas al
asentamiento de los grupos humanos en el territorio, como bodegas de granos y talleres, hospitales,
establecimientos educacionales y de recreación.

De acuerdo con lo anterior, los puntos receptores de interés considerados en el estudio se
georreferencian a continuación:

Tabla 25 - Puntos receptores de interés

|Receptores|Col2|Coordenadas UTM [m]<br>(WGS84-H19Sur)|Col4|Distancia del<br>receptor al<br>perímetro [m]|Orientación|
|---|---|---|---|---|---|
|Receptores|Receptores|X: Este|Y: Sur|Y: Sur|Y: Sur|
|R1|Vivienda 1|281.592|6.102.008|73|NO|
|R2|Vivienda 2|281.249|6.100.732|1.018|OSO|
|R3|Vivienda 3|282.640|6.100.524|618|SSE|
|R4|Vivienda 4|283.523|6.101.049|900|ESE|
|R5|Vivienda 5|283.564|6.101.675|448|E|
|R6|Vivienda 6|282.268|6.102.799|1.036|N|
|R7|Sector Los Robles|285.389|6.099.690|3.196|ESE|
|R8|Sector Escudo de Chile|282.974|6.099.435|1.760|SSE|
|R9|Sector El Umbral|281.385|6.098.648|2.666|SSO|
|R10|Escuela Juan Luis Sanfuentes A.|279.809|6.099.482|2.917|SO|
|R11|Sector Camarico|279.789|6.099.541|2.898|OO|
|R12|Peaje Troncal Río Claro|280.532|6.101.093|1.484|OSO|

25 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Chile.
26 Ministerio del Medio Ambiente. (2012). Decreto Supremo N°38/11 del Ministerio del Medio Ambiente - Norma de Emisión de Ruidos

Generados por Fuentes que Indica. Publicado en el Diario Oficial el 12 de junio de 2012.
27 Ministerio Secretaría General de la Presidencia. (2016). Ley 19.300 Aprueba Ley Sobre Bases Generales del Medio Ambiente. Ministerio

Secretaría General de la Presidencia. Chile.

PREDICCIÓN DE IMPACTOS POR OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 40 de 112

Figura 14 - Ubicación geográfica de los puntos receptores de interés

Fuente: Envirometrika - Google Earth, 2020.

**Olor base en situación sin proyecto**

La Guía para la predicción y evaluación de impactos por olor en el SEIA [28], señala: “es necesario
considerar el olor al que están expuestos los receptores en el AI de la situación sin proyecto”. Para
caracterizar la zona de emplazamiento con respecto a otras actividades que puedan ser potenciales
generadores de olor en la situación proyecto en ejecución, se utilizó la plataforma de Mapa de Proyectos
del Servicio de Evaluación Ambiental (SEA) [29] . Esta herramienta permite visualizar todos los proyectos
de la zona de interés, y así caracterizar el tipo de industria o emisión de olor base.

Se describen los proyectos potencialmente generadores de olor, dentro del radio generado por la
distancia entre el proyecto y el receptor más distante evaluado para este estudio.

Tabla 26 - Situación olor base - Proyectos aprobados en SEIA

|ID|Nombre del proyecto|Titular del proyecto|No RCA|Coordenadas UTM|Col6|
|---|---|---|---|---|---|
|ID|Nombre del proyecto|Titular del proyecto|No RCA|X: Este|Y: Norte|
|PA1|Alcantarillado Camarico|Ilustre Municipalidad de<br>Río Claro|65/99|279.275|6.099.857|
|PA2|Planta compostaje Los<br>Robles|Constructora Cordero y<br>Asalgado Ltda.|182/2003|280.462|6.100.186|

28 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Chile.
29 [Servicio de Evaluación Ambiental (2019). Mapa de proyectos http://sig.sea.gob.cl/mapadeproyectos/Chile.](http://sig.sea.gob.cl/mapadeproyectos/)

PREDICCIÓN DE IMPACTOS POR OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 41 de 112

Tabla 27 - Situación olor base - Establecimientos identificados en terreno [/a]

|ID|Nombre del proyecto|Coordenadas UTM|Col4|
|---|---|---|---|
|ID|Nombre del proyecto|X: Este|Y: Norte|
|E1|Fosa séptica comunitaria Raquel de Chanceaulme|279.716|6.099.885|
|E2|Almazara aceite oliva Camarico|280.417|6.099.797|
|E3|Planta de aguas servidas El Umbral|281.242|6.098.843|
|E4|Bodega vinificación|283.677|6.100.092|

/a Identificados en terreno por Titular.

Figura 15 -Proyectos aprobados por el Servicio de Evaluación Ambiental

Fuente: Envirometrika, 2021 - en base a Mapa de proyectos, SEA.

PREDICCIÓN DE IMPACTOS POR OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 42 de 112

**5** **ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR**

**5.1** **Estimación concentración límite de exposición**

Los modelos de dispersión odorante normalmente utilizan un criterio horario (1 hora), basado en la evaluación
odorante alemana. Por lo tanto, la evaluación de olor está basada en la frecuencia de ocurrencia de las horas
de olor en el año [30] . La mayoría de las guías de modelación de olor toman en cuenta al menos un 98% de las
horas del año para evaluar el impacto de las emisiones generadas por las fuentes representadas. En relación
con lo anterior, se recomienda el uso de percentil 98 para propósitos comparativos. [31-32]
Environment Agency (UK) recomienda el percentil 98, como el adecuado para estimar concentraciones de
olor, a través de modelación de dispersión atmosférica, debido a que este percentil tiene una relación directa
con la molestia producida por olor [33] .

En la actualidad, en Chile no se han definido criterios de calidad o normas de emisión específicas para la
evaluación de impactos por olor, sólo se han desarrollado propuestas como primeros antecedentes de
clasificación de olores molestos como lo es el Anteproyecto de Norma de Emisión de Contaminantes en
Planteles Porcinos que, en función de sus olores, generan Molestia y Constituyen un Riesgo a la Calidad de
Vida de la Población (Ministerio del Medio Ambiente), único referente a nivel nacional relativo al tema de
olores.

En base a lo anteriormente descrito, se consultaron las **normativas vigentes** de olor de los Estados de
referencia descritos en el art. 11 del Reglamento del SEA, considerando que para su aplicabilidad se priorizará
aquel Estado que posea similitud en sus componentes ambientales, con la situación nacional y/o local. De la
revisión del listado se tiene que sólo los Estados de **Alemania, Australia, Canadá, Nueva Zelandia,**
**Reino de los Países Bajos e Italia** cuentan con normativa, guía o lineamientos regulatorios que podrían
ajustarse a nuestro territorio. Posteriormente se analizó su aplicabilidad según normativa (excluyendo guías,
borradores y/o estándares regulatorios), percentil, descripción de actividad regulada y planificación territorial,
de acuerdo con lo señalado en la Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA (SEA,
2017).

Del análisis de los criterios descritos se desprende lo siguiente:

 Normativa vigente: Se descarta Australia, España, Irlanda, Nueva Zelandia, Panamá y Reino Unido.
Debido a que sólo disponen de guías/estándares regulatorios y no de normativas.

 Unidades comparables para niveles límites: Se descarta Bélgica, Brasil, Corea del Sur y Estados
Unidos de América, dado que utilizan unidades de medición distintas a las descritas en la Guía de
Olores del SEA.

 Percentil: Se descarta normas de Alemania, Australia, Canadá, Dinamarca, Hong Kong, Israel y
Noruega, dado que no son compatibles con el criterio de percentil 98 descrito en la Guía de Olores
del SEA.

 Actividad aplicable: Se descarta las normas de Francia, Puglia (Italia) y Países Bajos, dado que no
abordan la actividad a evaluar en el presente proyecto.

En coherencia al análisis de criterios se tiene que sólo los Estados de Colombia e Italia podrían ser aplicables
a nuestro territorio, de acuerdo con los criterios de normativa vigente, unidad del nivel límite, percentil y
actividad regulada.
Finalmente, se define la normativa del Estado de Italia (provincia de Lombardía [34] ) como aplicable al proyecto
en función de lo establecido en el Reglamento del SEIA y la Guía de Olores del SEA. Respecto a la normativa

30 Environment Agency. (2007). Review of Dispersion Modelling for Odour Predictions. Environment Agency.
31 Environment Agency. (2009). Horizontal Guidance: Technical Guidance Note - H4 Odour Management. Environment Agency.
32 Ibid.
33 Environment Agency. (2007). Review of Dispersion Modelling for Odour Predictions. Environment Agency.
34 Cusano, Gianluca & Licotti, Carlo & Sironi, Selena & Capelli, Laura & Rossi, Andrea & Grande, Massimiliano. (2010). Odour regulation in

Italy: The regional guidelines on odour emissions in Lombardia. Chem.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 43 de 112

de Colombia, dado que no se encuentra dentro del listado de Estados del art. 11 del Reglamento del SEA se
privilegió por la del Estado de Italia.
Los límites establecidos en esta norma están en función del uso del territorio: residencial; comercial; agrícola;
o industrial; y difieren para actividades existentes o nuevas. Este criterio indicaría el nivel de concentración
de olor sobre el cual olores generados en el Proyecto pudiesen ser percibidos por los receptores y, en
consecuencia, con la probabilidad de generar molestia.

Según los antecedentes para la determinación del área de influencia, el área de emplazamiento del proyecto
se encuentra fuera de las zonas reguladas por los IPT. Por lo tanto, la definición del criterio correspondiente
a las señaladas para zonas agrícolas o industriales:

Tabla 28 - Concentraciones máximas en receptores según normativa de Lombardía.

|Receptores|Percentil|Valores [ou /m3]<br>E|
|---|---|---|
|Primer receptor a una distancia >500 m desde el deslinde de la planta|98|3|
|Primer receptor a una distancia entre 200 y 500 m desde el deslinde de la planta|Primer receptor a una distancia entre 200 y 500 m desde el deslinde de la planta|4|
|Primer receptor a una distancia <200 m desde el deslinde de la planta|Primer receptor a una distancia <200 m desde el deslinde de la planta|5|

Tabla 29 - Valores límites en receptores de interés

|ID|Nombre|Distancia al<br>perímetro de la<br>planta [m]|Rango distancia [m]|Valor límite norma<br>Lombardía<br>CO [ou /m3]<br>E|
|---|---|---|---|---|
|R1|Vivienda 1|73|<200|5|
|R2|Vivienda 2|1,018|>500|3|
|R3|Vivienda 3|706|>500|3|
|R4|Vivienda 4|900|>500|3|
|R5|Vivienda 5|448|> 200 - < 500|4|
|R6|Vivienda 6|1,036|>500|3|
|R7|Sector Los Robles|3,196|>500|3|
|R8|Sector Escudo de Chile|1,855|>500|3|
|R9|Sector El Umbral|2,666|>500|3|
|R10|Escuela Juan Luis Sanfuentes A.|2,917|>500|3|
|R11|Sector Camarico|2,898|>500|3|
|R12|Peaje Troncal Río Claro|1,484|>500|3|

Los resultados son evaluados en términos de área y alcance odorante bajo el criterio de calidad definido, en
función de los objetivos del estudio. Se presentan los resultados de los valores límites de exposición:

`o` Concentración límite = 3, 4 y 5 [ou E /m [3] ].

`o` Criterio de cumplimiento = P98.

`o` Tiempo de evaluación = 1 hora.

`o` Tasa de Emisión de Olor - E1: Situación actual = 762.544 [ou E /s].

`o` Tasa de Emisión de Olor - E2: Situación futura = 84.980 [ou E /s].

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 44 de 112

**5.2** **Estimación de los impactos por emisiones de olor**

Para la estimación cuantitativa y cualitativa de los impactos por olor, producto de la operación del Proyecto,
se evaluaron siguientes escenarios:

Tabla 30 - Descripción escenarios simulados

|Escenario Operacional|Modelo|Percentil|Criterio de<br>calidad|
|---|---|---|---|
|E1: Situación actual<br>E2: Situación futura|M1: Curvas de isoconcentración de olor<br>M2: Frecuencia de percepción de olor (horaria)<br>M3: Frecuencia de percepción de olor (mensual)<br>M4: Concentración máxima horaria|98|3, 4 y 5<br>[ouE/m3]|

A partir de lo obtenido en el modelo anual (WRF-MMIF, 2019), se evaluaron los siguientes resultados:

 - Área de influencia

Corresponde al área en la cual se libera olor por un emisor observado [35] y que se define por la isolínea de
olor resultante de la proyección, bajo un criterio de calidad de 1 [ou E /m [3] ] considerado como umbral de
percepción (olor no reconocible). Se consideró el escenario de la situación futura, correspondiente a la
operación del proyecto presentado en el marco de esta Declaración de Impacto Ambiental.

 Cuantificación según curvas de isoconcentraciones de olor (M1)

Corresponde al percentil 98 anual de los promedios horarios de las concentraciones de olor (175 horas al
año), utilizando meteorología de pronóstico, bajo un criterio de calidad de 3 y 4 [ou E /m [3] ] considerado
como umbral de reconocimiento (se identifica claramente la nota de olor). Se presentan como isolíneas
de olor (alcance o nivel de exposición de olor) desde el criterio definido.

 - Cuantificación de la frecuencia de percepción de olor (M2 M3)

Corresponde a la frecuencia de ocurrencia de concentraciones horarias medias por encima del criterio de
calidad de 3 y 4 [ou E /m [3] ], describiéndose como la sumatoria de horas anuales de excedencia, distribuidas
en horas del día y del mes. Debido a variaciones meteorológicas de carácter estacional, se recomienda el
uso del criterio de percentil 98 el cual permite visualizar los porcentajes de horas en que se supera el valor
definido para las 8.760 horas del año [36] .

 Estimación de Concentración máxima horaria (M4)

Corresponde al límite superior de los promedios horarios de concentración de olor registrados en un punto
receptor, bajo percentil 98 para la totalidad del periodo anual y es expresada en [ou E /m [3] ].

 - Análisis de incertidumbre

Corresponde a la evaluación de los datos meteorológicos tridimensionales generados del modelo de
pronóstico WRF, mediante la comparación de las observaciones con las simulaciones del modelo en el
punto de medición de los datos observados y así determinar el Error e Incertidumbre en forma cualitativa
(comparaciones gráficas) y cuantitativa - Cálculo de las métricas de estadísticas del sesgo (BIAS),
Error medio cuadrático (RSME) y Coeficiente de correlación entre las variables meteorológicas
pronosticadas y observadas.

 Análisis cualitativo: Comparaciones gráficas para datos meteorológicos observados y simulados,
principalmente, a través de los ciclos diarios.

 Cálculo de las métricas de estadísticas del sesgo (BIAS), Error medio cuadrático (RSME) y Coeficiente
de correlación entre las variables meteorológicas pronosticadas y observadas.

35 Ministerio del Medio Ambiente. (2013). Estudio: Antecedentes para la Regulación de Olores en Chile. Subsecretaría del Medio Ambiente,

Chile.
36 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. Chile.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 45 de 112

**5.3** **Predicción de Área de Influencia del Proyecto**

Figura 16 - AI: Área de influencia del Proyecto, C P98-1hr = 1 [ou E /m [3] ]

|Alcance|Sentido|[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|1.180<br>1.192<br>1.071<br>835<br>645<br>854<br>500<br>494|

Fuente: Envirometrika. “Situación futura: Isolíneas de olor, C P98-1hr = 1 [ou E /m [3] ].” [Cartografía]. 1:45.000. Febrero 2021.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2021.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 46 de 112

**5.4** **Cuantificación según curva de isoconcentración de olor**

Figura 17 - E1: Curvas isodoras Situación actual, C P98-1hr = 3 [ou E /m [3] ]

|Alcance|Sentido|[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|2.902<br>4.925<br>2.875<br>2.059<br>1.944<br>3.311<br>1.225<br>1.291|

Fuente: Envirometrika. “E1-Situación actual: Isolíneas de olor, C P98-1hr = 3 [ou E /m [3] ].” [Cartografía]. 1:50.000. Febrero 2021.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2021.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 47 de 112

Figura 18 - E1: Curvas isodoras Situación actual, C P98-1hr = 4 [ou E /m [3] ]

|Alcance|Sentido|[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|2.537<br>4.324<br>2.574<br>1.825<br>1.682<br>2.750<br>971<br>1.037|

Fuente: Envirometrika. “E1-Situación actual: Isolíneas de olor, C P98-1hr = 4 [ou E /m [3] ].” [Cartografía]. 1:45.000. Febrero 2021.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2021.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 48 de 112

Figura 19 - E1: Curvas isodoras Situación actual, C P98-1hr = 5 [ou E /m [3] ]

|Alcance|Sentido|[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|2.291<br>3.811<br>2.306<br>1.597<br>1.475<br>2.383<br>780<br>844|

Fuente: Envirometrika. “E1-Situación actual: Isolíneas de olor, C P98-1hr = 5 [ou E /m [3] ].” [Cartografía]. 1:45.000. Febrero 2021.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2021.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 49 de 112

Figura 20 - E2: Curvas isodoras Situación futura, C P98-1hr = 3 [ou E /m [3] ]

|Alcance|Sentido|[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|810<br>686<br>716<br>530<br>335<br>509<br>272<br>260|

Fuente: Envirometrika. “E2-Situación futura: Isolíneas de olor, C P98-1hr = 3 [ou E /m [3] ].” [Cartografía]. 1:45.000. Febrero 2021.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2021.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 50 de 112

Figura 21 - E2: Curvas isodoras Situación futura, C P98-1hr = 4 [ou E /m [3] ]

|Alcance|Sentido|[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|740<br>588<br>627<br>459<br>249<br>402<br>212<br>181|

Fuente: Envirometrika. “E2-Situación futura: Isolíneas de olor, C P98-1hr = 4 [ou E /m [3] ].” [Cartografía]. 1:45.000. Febrero 2021.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2021.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 51 de 112

Figura 22 - E2: Curvas isodoras Situación futura, C P98-1hr = 5 [ou E /m [3] ]

|Alcance|Sentido|[m]|
|---|---|---|
|**Alcance**|N <br>NE<br>E <br>SE<br>S <br>SO<br>O <br>NO|665<br>519<br>522<br>371<br>249<br>346<br>161<br>137|

Fuente: Envirometrika. “E2-Situación futura: Isolíneas de olor, C P98-1hr = 5 [ou E /m [3] ].” [Cartografía]. 1:45.000. Febrero 2021.
Software: ArcGIS [software GIS]. Versión 10.2 Redlands, CA: Environmental Systems Research Institute, Inc., 2021.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 52 de 112

**5.5** **Cuantificación de la frecuencia de percepción de olor**

La frecuencia de ocurrencia de concentración de olor para 3, 4 y 5 [ou E /m [3] ], se presenta como tablas y
gráficos que muestran la sumatoria de horas anuales, distribuidas en horas del día y meses del año. Estos
resultados indicarían la probabilidad de superar concentraciones de olor de ambos niveles de concentración
de olor en los puntos evaluados.

La nomenclatura para este análisis corresponderá a:

✓ **Frecuencia horaria** = Cantidad de horas con olor del año, distribuidas en horas del día, en que existe la

probabilidad de superar las 3 [ou E /m [3] ] (en receptor sobre 500 [m] de distancia), 4 [ou E /m [3] ] (en receptor
situado a una distancia entre 200 [m] y 500 [m]) y 5 [ou E /m [3] ] (en receptor menor a 200 [m] de distancia).

✓ **Frecuencia mensual** = Cantidad de horas con olor del año, distribuidas en meses del año, en que existe

la probabilidad de superar las 3 [ou E /m [3] ] (en receptor sobre 500 [m] de distancia), 4 [ou E /m [3] ] (en receptor
situado a una distancia entre 200 [m] y 500 [m]) y 5 [ou E /m [3] ] (en receptor menor a 200 [m] de distancia).

A continuación, se presentan los resultados de frecuencia de percepción de olor, evaluada en percentil C P98
1hr =3, 4 y 5 [ou E /m [3] ] para ambos escenarios.

Tabla 31 - E1/M2: Frecuencia de percepción de olor horaria [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación actual

|Valor<br>límite C<br>P98|3 [ou /m3]<br>E|4<br>[ou /m3]<br>E|5<br>[ou /m3]<br>E|
|---|---|---|---|
|**Hora del**<br>**día**|**R2**<br>**R3**<br>**R4**<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12**|**R5/b **|**R1/c **|
|0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23|29<br>31<br>29<br>42<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>30<br>27<br>24<br>51<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>28<br>26<br>25<br>43<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>34<br>20<br>19<br>35<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>39<br>28<br>19<br>38<br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>41<br>26<br>22<br>44<br>0 <br>4 <br>0 <br>0 <br>0 <br>0 <br>28<br>19<br>21<br>22<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>24<br>9 <br>9 <br>18<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>12<br>9 <br>5 <br>6 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>9 <br>6 <br>3 <br>5 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>5 <br>0 <br>4 <br>4 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>3 <br>1 <br>3 <br>4 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>1 <br>2 <br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>2 <br>3 <br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>4 <br>4 <br>2 <br>1 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>6 <br>2 <br>4 <br>2 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>5 <br>10<br>9 <br>10<br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>11<br>16<br>21<br>24<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>20<br>26<br>36<br>42<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>28<br>44<br>53<br>61<br>0 <br>5 <br>0 <br>0 <br>0 <br>0 <br>26<br>45<br>47<br>50<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>28<br>38<br>45<br>41<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>36<br>40<br>37<br>43<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>33<br>35<br>33<br>39<br>0 <br>3 <br>0 <br>0 <br>0 <br>0|32<br>24<br>27<br>27<br>25<br>27<br>29<br>11<br>8 <br>4 <br>4 <br>2 <br>5 <br>7 <br>19<br>22<br>33<br>37<br>72<br>86<br>72<br>59<br>44<br>32|26<br>25<br>28<br>25<br>22<br>19<br>15<br>11<br>7 <br>2 <br>3 <br>1 <br>0 <br>0 <br>1 <br>1 <br>4 <br>3 <br>27<br>31<br>32<br>31<br>31<br>19|
|**Total**|**482**<br>**467**<br>**470**<br>**628**<br>**0 **<br>**31**<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**708**|**364**|

/a Valores en “cero” indican que habría superación del límite de concentración definido para cada receptor.
/b R5 por encontrarse a una distancia entre 200 [m] y 500 [m] del perímetro debe ser evaluado con 4 [ou E /m 3 ] según lo que establece

como limite la normativa de Lombardía.
/c R1 por encontrarse a una distancia menor a 200 [m] del perímetro debe ser evaluado con 5 [ou E /m 3 ] según lo que establece como

limite la normativa de Lombardía.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 53 de 112

Tabla 32 - E1/M3: Frecuencia de percepción de olor mensual [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación actual

|Valor<br>límite C<br>P98|3<br>[ou /m3]<br>E|4<br>[ou /m3]<br>E|5<br>[ou /m3]<br>E|
|---|---|---|---|
|**Mes**|**R2**<br>**R3**<br>**R1/c **<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12**|**R5/b **|**R1/c **|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|28<br>38<br>40<br>68<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>26<br>40<br>47<br>54<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>26<br>25<br>37<br>54<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>37<br>43<br>51<br>67<br>0 <br>4 <br>0 <br>0 <br>0 <br>0 <br>74<br>66<br>64<br>57<br>0 <br>7 <br>0 <br>0 <br>0 <br>0 <br>75<br>64<br>37<br>49<br>0 <br>5 <br>0 <br>0 <br>0 <br>0 <br>60<br>39<br>34<br>61<br>0 <br>4 <br>0 <br>0 <br>0 <br>0 <br>32<br>18<br>22<br>43<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>40<br>37<br>35<br>43<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>50<br>50<br>51<br>52<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>18<br>16<br>18<br>34<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>16<br>31<br>34<br>46<br>0 <br>0 <br>0 <br>0 <br>0 <br>0|84<br><br>70<br><br>55<br><br>78<br><br>60<br><br>38<br><br>44<br><br>38<br><br>65<br><br>74<br><br>48<br><br>54|25<br>32<br>29<br>35<br>39<br>31<br>34<br>28<br>30<br>41<br>13<br>27|
|Total|**482**<br>**467**<br>**470**<br>**628**<br>**0 **<br>**31**<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**708**|**364**|

/a Valores en “cero” indican que habría superación del límite de concentración definido para cada receptor.
/b R5 por encontrarse a menos de 500 [m] de distancia del perímetro debe ser evaluado con 4 [ou E /m 3 ] según lo que establece como

limite la normativa de Lombardía.
/c R1 por encontrarse a una distancia menor a 200 [m] del perímetro debe ser evaluado con 5 [ou E /m 3 ] según lo que establece como

limite la normativa de Lombardía.

Tabla 33 - E1/M2: Frecuencia de percepción de olor horaria [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación futura

|Valor<br>limite C<br>P98|3<br>[ou /m3]<br>E|4<br>[ou /m3]<br>E|5<br>[ou /m3]<br>E|
|---|---|---|---|
|**Hora del**<br>**día**|**R2**<br>**R3**<br>**R5/b **<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12**|**R5/b **|**R1/c **|
|0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|
|**Total**|**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**0 **|**0 **|

/a Valores en “cero” indican que habría superación del límite de concentración definido para cada receptor.
/b R5 por encontrarse a menos de 500 [m] de distancia del perímetro debe ser evaluado con 4 [ou E /m 3 ] según lo que establece como

limite la normativa de Lombardía.
/c R1 por encontrarse a una distancia menor a 200 [m] del perímetro debe ser evaluado con 5 [ou E /m 3 ] según lo que establece como

limite la normativa de Lombardía.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 54 de 112

Tabla 34 - E1/M3: Frecuencia de percepción de olor mensual [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación futura

|Valor<br>límite C<br>P98|3<br>[ou /m3]<br>E|4<br>[ou /m3]<br>E|5<br>[ou /m3]<br>E|
|---|---|---|---|
|**Mes**|**R2**<br>**R3**<br>**R1/c **<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12**|**R5/b **|**R1/c **|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|
|Total|**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **|**0 **|**0 **|

/a Valores en “cero” indican que habría superación del límite de concentración definido para cada receptor.
/b R5 por encontrarse a menos de 500 [m] de distancia del perímetro debe ser evaluado con 4 [ou E /m 3 ] según lo que establece como

limite la normativa de Lombardía.
/c R1 por encontrarse a una distancia menor a 200 [m] del perímetro debe ser evaluado con 5 [ou E /m 3 ] según lo que establece como

limite la normativa de Lombardía.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 55 de 112

**5.6** **Concentración máxima**

En la siguiente tabla se informa el valor máximo de concentración odorante que percibirían los receptores
analizados para la situacion actual y futura:

Tabla 35 - Concentración máxima - Percentil 98 y 99,5 - Situación actual

|ID|Concentración máxima [ou /m3]<br>E|Col3|
|---|---|---|
|ID|Percentil 99,5|Percentil 98|
|R1|42|16|
|R2|33|12|
|R3|71|22|
|R4|70|26|
|R5|144|65|
|R6|48|19|
|R7|4|1|
|R8|13|3|
|R9|5|2|
|R10|7|2|
|R11|7|2|
|R12|12|2|

La modelación a percentil C p98 de la situación operacional actual, no acusaría concentraciones de olor sobre
el criterio de calidad de 3, 4 y 5 [ou E /m [3] ] en 7 de los 12 receptores evaluados.

Tabla 36 - Concentración máxima - Percentil 98 y 99,5 - Situación futura

|ID|Concentración máxima [ou /m3]<br>E|Col3|Limite Norma<br>Lombardía<br>CO [ou /m3]<br>E|Cumplimiento|
|---|---|---|---|---|
|ID|Percentil 99,5|Percentil 98|Percentil 98|Percentil 98|
|R1|4|1|5|Si|
|R2|1|<1|3|Si|
|R3|3|1|3|Si|
|R4|3|1|3|Si|
|R5|6|2|4|Si|
|R6|2|1|3|Si|
|R7|<1|<1|3|Si|
|R8|<1|<1|3|Si|
|R9|<1|<1|3|Si|
|R10|<1|<1|3|Si|
|R11|<1|<1|3|Si|
|R12|<1|<1|3|Si|

La modelación a percentil C p98 de la situación operacional futura, no acusaría concentraciones de olor sobre
el criterio de calidad de 3, 4 y 5 [ou E /m [3] ] en ninguno de los 12 receptores evaluados.

ESTIMACIÓN DE LOS IMPACTOS POR EMISIONES DE OLOR www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 56 de 112

**6** **CONCLUSIÓN**

Los resultados de la proyección del alcance odorante del proyecto Centro de Tratamiento de Residuos en “situación
futura”, arrojó para los 12 receptores definidos niveles de exposición bajo los límites establecidos en la normativa
de Lombardía.

Para la situación futura la estimación de emisión muestra una reducción del 89% de la TEO actual y 92% en el
área de alcance de la pluma de olor (para el umbral de reconocimiento 3 [ou E /m [3] ]).

Al proyectar las TEO levantadas en el 2019, para la situación futura se obtuvo que para la componente olor, el
proyecto no generaría o presentaría algún efecto, características o circunstancias contempladas en el artículo 11
de la Ley 19.300.

CONCLUSIÓN www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 57 de 112

**7** **BIBLIOGRAFÍA**

 Coexca S.A, (2019). DIA: Mejora del desempeño ambiental mediante biodigestor anaeróbico, modernización y

ampliación plantel de cerdos Santa Francisca. Chile.

 - Cusano, Gianluca & Licotti, Carlo & Sironi, Selena & Capelli, Laura & Rossi, Andrea & Grande, Massimiliano.

(2010). Odour regulation in Italy: The regional guidelines on odour emissions in Lombardia. Chem.

 Dunabin, E., McIntyre, A., Longhurst, P. (2017). Seafield Wastewater Treatment Works Strategic Odouyr

Review. Cranfield University - Amec Foster Wheeler Environment & Infrastructures UK Limited. United Kingdom.

 Environment Agency. (2007). Review of Dispersion Modelling for Odour Predictions. Environment Agency.

 - Environment Agency. (2009). Horizontal Guidance: Technical Guidance Note - H4 Odour Management.

Environment Agency.

 Instituto Nacional de Normalización. (2010). NCh 3190:2010 Calidad del aire - Determinación de la

concentración de olor por olfatometría dinámica. Chile.

 Instituto Nacional de Normalización. (2015). NCh 3386:2015 Calidad del aire - Muestreo estático para

olfatometría. Chile.

 Instituto Nacional de Normalización. (2020). NCh 3431:2020 Calidad del aire - Muestreo para fuentes fugitivas

o volumen. Chile

 - Ministerio del Medio Ambiente. (2011). Ley No 19.300, sobre Bases Generales del Medio Ambiente - Ley

Orgánica de la Superintendencia del Medio Ambiente. División Jurídica del Medio Ambiente. Chile.

 - Ministerio del Medio Ambiente. (2012). Decreto Supremo N°38/11 del Ministerio del Medio Ambiente - Norma

de Emisión de Ruidos Generados por Fuentes que Indica. Publicado en el Diario Oficial el 12 de junio de 2012.

 Ministerio del Medio Ambiente. (2013). Estudio: Antecedentes para la Regulación de Olores en Chile.

Subsecretaría del Medio Ambiente, Chile.

 Ministerio Secretaría General de la Presidencia. (2016). Ley 19.300 Aprueba Ley Sobre Bases Generales del

Medio Ambiente. Ministerio Secretaría General de la Presidencia. Chile.

 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Chile.

 Servicio de Evaluación Ambiental. (2017). Guía para la Descripción de la Calidad del Aire en el Área de Influencia

de Proyectos que Ingresan al SEIA. Departamento de Estudios y Desarrollo - División de Evaluación y
Participación Ciudadana. Chile.

 Servicio de Evaluación Ambiental. (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el

SEIA. Ministerio del Medio Ambiente. Chile.

 - [Servicio de Evaluación Ambiental (2019). Mapa de proyectos http://sig.sea.gob.cl/mapadeproyectos/ Chile.](http://sig.sea.gob.cl/mapadeproyectos/)

BIBLIOGRAFÍA www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 58 de 112

**8** **ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES**

Tabla 37 - Situación actual: Caracterización de fuentes de olor (parte 1)

|ID|Fuente|Coordenadas UTM [m]|Col4|Altura<br>desde<br>suelo [m]|Vel.<br>salida<br>[m/s]|Temp.<br>salida<br>[oK]|Diám.<br>ducto [m]|Largo<br>[m]/a|Ancho<br>[m]/a|Radio<br>[m]|Área<br>[m2]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID|Fuente|X: Este|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|
|1|Pila Lodo Agroindustrial - Edad 1|282.608|6.101.746|1,6|-|-|-|86,00|76,26|-|6.558,00|
|2|Pila Lodo Agroindustrial - Edad 1|282.477|6.101.593|1,6|-|-|-|152,39|38,00|-|5.791,00|
|3|Pila Lodo Agroindustrial - Edad 2|282.491|6.101.572|1,6|-|-|-|207,08|36,00|-|7.455,00|
|4|Pila Lodo Agroindustrial - Edad 3a|282.599|6.101.756|1,6|-|-|-|100,00|12,00|-|1.200,00|
|5|Pila Lodo Agroindustrial - Edad 3b|282.671|6.101.810|1,6|-|-|-|60,00|20,00|-|1.200,00|
|6|Pila lodo sanitario - Edad 1 Curicó|282.791|6.101.622|1,6|-|-|-|46,72|74,00|-|3.457,00|
|7|Pila lodo sanitario - Edad 1 Otras Localidades|282.815|6.101.660|1,6|-|-|-|140,15|74,00|-|10.371,00|
|8|Pila lodo sanitario - Edad 2 Curicó|282.743|6.101.660|1,6|-|-|-|40,76|51,00|-|2.078,75|
|9|Pila lodo sanitario - Edad 2 Otras Localidades|282.771|6.101.696|1,6|-|-|-|122,28|51,00|-|6.236,25|
|10|Pila lodo sanitario - Edad 1 Curicó|282.712|6.101.692|1,6|-|-|-|33,13|34,00|-|1.126,50|
|11|Pila lodo sanitario - Edad 1 Otras Localidades|282.740|6.101.731|1,6|-|-|-|99,40|34,00|-|3.379,50|
|12|Pila lodo sanitario - Edad 2 Curicó|282.682|6.101.715|1,6|-|-|-|29,40|33,00|-|970,25|
|13|Pila lodo sanitario - Edad 2 Otras Localidades|282.705|6.101.743|1,6|-|-|-|88,20|33,00|-|2.910,75|
|14|Pila lodo sanitario - Edad 1 Curicó|282.669|6.101.464|1,6|-|-|-|35,43|30,00|-|1.063,00|
|15|Pila lodo sanitario - Edad 1 Otras Localidades|282.669|6.101.464|1,6|-|-|-|106,30|30,00|-|3.189,00|
|16|Pila lodo sanitario - Edad 2 Curicó|282.712|6.101.566|1,6|-|-|-|34,87|35,00|-|1.220,50|
|17|Pila lodo sanitario - Edad 2 Otras Localidades|282.644|6.101.488|1,6|-|-|-|104,61|35,00|-|3.661,50|
|18|Pila lodo sanitario - Edad 3 Curicó|282.567|6.101.489|1,6|-|-|-|27,79|23,00|-|639,25|
|19|Pila lodo sanitario - Edad 3 Otras Localidades|282.587|6.101.467|1,6|-|-|-|83,38|23,00|-|1.917,75|
|20|Pila lodo sanitario - Edad 1 Curicó|282.587|6.101.503|1,6|-|-|-|27,98|12,00|-|335,75|
|21|Pila lodo sanitario - Edad 1 Otras Localidades|282.606|6.101.483|1,6|-|-|-|83,94|12,00|-|1.007,25|
|22|Pila lodo sanitario - Edad 2 Curicó|282.594|6.101.512|1,6|-|-|-|27,02|14,00|-|378,25|
|23|Pila lodo sanitario - Edad 2 Otras Localidades|282.614|6.101.491|1,6|-|-|-|81,05|14,00|-|1.134,75|
|24|Pila lodo sanitario - Edad 1 Curicó|282.637|6.101.675|1,6|-|-|-|40,63|49,00|-|1.990,75|
|25|Pila lodo sanitario - Edad 1 Otras Localidades|282.556|6.101.580|1,6|-|-|-|121,88|49,00|-|5.972,25|

ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 59 de 112

Tabla 38 - Situación actual: Caracterización de fuentes de olor (parte 2)

|ID|Fuente|Coordenadas UTM [m]|Col4|Altura<br>desde<br>suelo [m]|Vel.<br>salida<br>[m/s]|Temp.<br>salida<br>[oK]|Diám.<br>ducto [m]|Largo<br>[m]/a|Ancho<br>[m]/a|Radio<br>[m]|Área<br>[m2]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID|Fuente|X: Este|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|
|26|Pila lodo sanitario - Edad 2 Curicó|282.671|6.101.601|1,6|-|-|-|35,09|50,00|-|1.754,25|
|27|Pila lodo sanitario - Edad 2 Otras Localidades|282.603|6.101.521|1,6|-|-|-|105,26|50,00|-|5.262,75|
|28|Pila lodo sanitario - Edad 3 Curicó|282.759|6.101.572|1,6|-|-|-|56,24|9,25|-|520,25|
|29|Pila lodo sanitario - Edad 3 Otras Localidades|282.766|6.101.566|1,6|-|-|-|56,24|27,75|-|1.560,75|
|30|Laguna de percolados|282.122|6.101.571|0,0|-|-|-|18,09|55,29|-|1.000,00|
|31|Laguna de agua rechazo|282.194|6.101.668|0,0|-|-|-|14,00|11,00|-|154,00|
|32|Reactor aerobio 1|282.183|6.101.641|2,1|-|-|-|-|-|5,00|78,54|
|33|Reactor aerobio 2|282.191|6.101.631|2,1|-|-|-|-|-|5,00|78,54|
|34|Clarificador|282.199|6.101.628|0,0|-|-|-|4,50|5,38|-|24,20|
|35|Floculador|282.206|6.101.636|0,0|-|-|-|-|-|1,50|7,07|
|36|Laguna lodos biológicos|282.186|6.101.657|0,0|-|-|-|10,20|6,63|-|67,60|
|37|Laguna lodo físico/químico|282.182|6.101.652|0,0|-|-|-|10,20|6,00|-|61,20|
|38|Lechos de secado 1|282.212|6.101.589|0,0|-|-|-|10,00|30,20|-|302,00|
|39|Lechos de secado 2 (lavado de camiones)|282.200|6.101.596|0,0|-|-|-|10,00|26,70|-|267,00|
|40|Laguna agua tratada|282.165|6.101.663|0,0|-|-|-|11,09|34,00|-|377,00|
|41|Monorelleno - Frente de trabajo|282.277|6.101.239|2,5|-|-|-|98,00|46,00|-|4.508,00|
|42|Relleno Sanitario - Frente de trabajo|282.314|6.101.479|10,0|-|-|-|42,50|20,00|-|850,00|

ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 60 de 112

Tabla 39 - Situación futura: Caracterización de fuentes de olor (parte 1)

|ID|Fuente|Coordenadas UTM [m]|Col4|Altura<br>desde<br>suelo [m]|Vel.<br>salida<br>[m/s]|Temp.<br>salida<br>[oK]|Diám.<br>ducto [m]|Largo<br>[m]/a|Ancho<br>[m]/a|Radio<br>[m]|Área<br>[m2]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID|Fuente|X: Este|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|
|1|Cancha de compostaje 1|282.627|6.101.766|1,6|-|-|-|154,46|65,00|-|10.040,00|
|2|Cancha de compostaje 2|282.745|6.101.658|1,6|-|-|-|154,46|32,11|-|4.960,00|
|3|Cancha de compostaje 3|282.770|6.101.646|1,6|-|-|-|154,46|91,54|-|14.140,00|
|4|Cancha de compostaje 4|282.623|6.101.534|1,6|-|-|-|125,00|128,00|-|16.000,00|
|5|Galpón de compostaje 1 (sistema de abatimiento)|282.579|6.101.700|4,0|3,05|295,15|1,20|-|-|-|1,13|
|6|Galpón de compostaje 2 (sistema de abatimiento)|282.591|6.101.720|4,0|3,05|295,15|1,20|-|-|-|1,13|
|7|Galpón de compostaje 3 (sistema de abatimiento)|282.609|6.101.736|4,0|3,05|295,15|1,20|-|-|-|1,13|
|8|Galpón de compostaje 4 (sistema de abatimiento)|282.623|6.101.755|4,0|3,05|295,15|1,20|-|-|-|1,13|
|9|Estanque acumulación clarificado - Etapa 1|282.607|6.101.593|4,0|-|-|-|-|-|8,00|201,06|
|10|Estanque acumulación de digestato - Etapa 1|282.614|6.101.585|4,0|-|-|-|-|-|1,71|9,19|
|11|Contenedor deshidratado mecánico - Etapa 1|282.610|6.101.606|2,0|-|-|-|2,40|5,30|-|12,72|
|12|Estanque acumulación clarificado - Etapa 2|282.655|6.101.641|4,0|-|-|-|-|-|8,00|201,06|
|13|Contenedor deshidratado mecánico - Etapa 2|282.615|6.101.613|2,0|-|-|-|2,40|5,30|-|12,72|
|14|Sistema de abatimiento olores - Etapa 1|282.610|6.101.579|4,0|3,05|295,15|1,20|-|-|-|1,13|
|15|Sistema de abatimiento olores - Etapa 2|282.651|6.101.629|4,0|3,05|295,15|1,20|-|-|-|1,13|
|16|Unidad de almacenamiento de digestato|282.569|6.101.487|1,0|-|-|-|73,00|73,00|-|5.329,00|
|17|Laguna de anaeróbica|282.130|6.101.544|0,0|-|-|-|64,00|31,25|-|2.000,00|
|18|Laguna de percolados|282.122|6.101.571|0,0|-|-|-|18,09|55,29|-|1.000,00|
|19|Reactor aerobio 1|282.183|6.101.640|2,1|-|-|-|-|-|5,00|78,54|
|20|Reactor aerobio 2|282.191|6.101.631|2,1|-|-|-|-|-|5,00|78,54|

ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 61 de 112

Tabla 40 - Situación futura: Caracterización de fuentes de olor (parte 2)

|ID|Fuente|Coordenadas UTM [m]|Col4|Altura<br>desde<br>suelo [m]|Vel.<br>salida<br>[m/s]|Temp.<br>salida<br>[oK]|Diám.<br>ducto [m]|Largo<br>[m]/a|Ancho<br>[m]/a|Radio<br>[m]|Área<br>[m2]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ID|Fuente|X: Este|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|Y: Norte|
|21|Reactor aerobio 3|282.175|6.101.629|2,1|-|-|-|-|-|5,00|78,54|
|22|Reactor aerobio 4|282.168|6.101.618|2,1|-|-|-|-|-|5,00|78,54|
|23|Clarificador|282.198|6.101.627|0,0|-|-|-|4,50|5,38|-|24,20|
|24|Floculador|282.206|6.101.635|0,0|-|-|-|-|-|1,50|7,07|
|25|Laguna lodos biológicos|282.186|6.101.657|0,0|-|-|-|10,20|6,63|-|67,60|
|26|Laguna lodo físico/químico|282.182|6.101.652|0,0|-|-|-|10,20|6,00|-|61,20|
|27|Laguna agua tratada|282.165|6.101.662|0,0|-|-|-|11,09|34,00|-|377,00|
|28|Alvéolo 7 - Frente de trabajo|282.290|6.101.242|15,0|-|-|-|20,00|42,50|-|850,00|
|29|Zona de riego 1|281.821|6.101.645|0,0|-|-|-|114,80|114,80|-|4.217,60|
|30|Zona de riego 2|282.053|6.101.591|0,0|-|-|-|358,12|50,00|-|5.729,96|

ANEXO 1 - CARACTERIZACIÓN DE FUENTES ODORANTES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 62 de 112

**9** **ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES**

Los valores de emisión proyectados para las fuentes galpón de compostaje, canchas de compostaje y galpón de
recepción, se basaron en emisiones de referencia según se describe a continuación:

**Galpón de compostaje** : Tasa de Emisión de Olor proyectada en base a la superficie efectiva de compostaje de
cada galpón (ver tabla 41), considerando emisiones de referencia de pilas agroindustrial en estado inicial, cuyo

<!-- INICIO TABLA 41 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- muestreo fue realizado en el mismo Centro de Manejo de Residuos Ecomaule (2019), bajo los estándares definidos por las normativas NCh3386:2015 y NCh3190:2010. La emisión de referencia aplicada correspondió a 14,7 [ou E /m [2] s]. -->

**Tabla 41: - Características de galpones de compostaje (confinado)**

| Tipo de<br>galpón | Largo<br>[m] | Ancho<br>[m] | Área<br>[m2] | N° de pilas | Largo pila<br>[m] | Ancho pila<br>[m] | Área de<br>emisión<br>[m2] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 140 | 20 | 2.800 | 4 | 115 | 3,7 | 553,34 |
| B | 115 | 20 | 2.300 | 4 | 90 | 3,7 | 434,26 |

<!-- Estadísticas: 2 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Para la obtención de la Tasa de Emisión de Olor, en base a la emisión de referencia este tipo de fuente, se aplicó la siguiente ecuación: TEO= AE pila [m [2] ] x EO Agroindustrial [m [ou] [2] ∗s [E] [] x N] -->
<!-- FIN TABLA 41 -->

muestreo fue realizado en el mismo Centro de Manejo de Residuos Ecomaule (2019), bajo los estándares definidos
por las normativas NCh3386:2015 y NCh3190:2010. La emisión de referencia aplicada correspondió a 14,7

[ou E /m [2] s].

Tabla 41 - Características de galpones de compostaje (confinado)

|Tipo de<br>galpón|Largo<br>[m]|Ancho<br>[m]|Área<br>[m2]|N° de pilas|Largo pila<br>[m]|Ancho pila<br>[m]|Área de<br>emisión<br>[m2]|
|---|---|---|---|---|---|---|---|
|A|140|20|2.800|4|115|3,7|553,34|
|B|115|20|2.300|4|90|3,7|434,26|

Para la obtención de la Tasa de Emisión de Olor, en base a la emisión de referencia este tipo de fuente, se aplicó
la siguiente ecuación:

TEO= AE pila [m [2] ] x EO Agroindustrial [m [ou] [2] ∗s [E] [] x N]

Donde:
TEO: Tasa de Emisión de Olor de la fuente.
AE: Área de emisión de olor o superficie que emite olor de cada pila al interior del galpón.
EO: Emisión de Olor por m [2] de pila. El valor de referencia corresponde a lo muestreado en pila agroindustrial en
estado inicial (edad 1). Para representar la condición más desfavorable se proyectó la emisión de forma constante
durante el proceso de compostaje (4 semanas).
N: Número de pilas compostadas al interior del galpón.

Por lo tanto, la TEO se obtiene del siguiente cálculo:

TEO [ou] [E]
Galpón A = 553,34 [m2] x 14,7 [m [2] ∗s ~~[]]~~ [ x 4]

TEO
Galpón A = 32. 536, 47 [ [ou] s [E] ~~[]]~~

TEO [ou] [E]
Galpón B = 434,26 [m2] x 14,7 [m [2] ∗s ~~[]]~~ [ x 4]

TEO
Galpón A = 25. 534, 26 [ [ou] s [E] ~~[]]~~

De los valores de TEO correspondiente a cada tipo de galpón, se aplicó el porcentaje de eficiencia de remoción
de olor asociado a la implementación del sistema de fotocatalítico UV, correspondiente a un 95%. Por lo tanto, de
lo anterior se obtiene para cada galpón lo siguiente:

TEO Galpón A = 32.536,47 ~~[~~ [ou] s [E] ~~[]]~~ [ x 0,95]

TEO
Galpón A = 1. 626, 82 [ [ou] s [E] ~~[]]~~

TEO Galpón B = 25.534,26 ~~[~~ [ou] s [E] ~~[]]~~ [ x 0,95]

TEO Galpón B = 1. 276, 71 ~~[~~ [ou] s [E] ~~[]]~~

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 63 de 112

Finalmente, para representar la contribución de olor de cada galpón se consideró una velocidad de salida de 3,05

[m/s] y una temperatura de 22 [°C], basado en las características descritas en ficha técnica EC-VTL-FB20.

**Cancha de compostaje** : Emisión de Olor proyectada en base a la superficie efectiva de compostaje de cada
pila, luego de finalizado el proceso de compostaje en galpón. El proceso de compostaje contempla una duración
total de 12 semanas, donde las primeras 4 semanas son realizadas en galpón bajo condiciones de compostaje
aireado. Finalizada la semana 4, las pilas son retiradas y dispuestas en cancha donde continúa el proceso de
compostaje hasta su estabilización. Dado que no se dispone de mediciones de referencia nacionales en pilas
compostadas bajo este tipo de tecnología, se aplicó una curva de estabilización basado en la función que describe
el comportamiento de emisión de olor para compostaje aireado del estudio de referencia “Compost Science and
Technology [37] ”. La función de referencia fue aplicada sobre el valor de emisión de olor muestreado en pila
agroindustrial en el Centro de Manejo de Residuos Ecomaule durante la campaña realizada el año 2019,
correspondiente a 14,7 [ou E /m [2] s].

Tabla 42 - Curva de estabilización de compostaje en cancha

|Función|Y=18.419*EXP(-0.516*X)|Col3|
|---|---|---|
|Semana|Curva exponencial de<br>Emisión de Olor<br>[ouE/m2s]/a|Etapa de compostaje|
|1|10,99|Con aireación en galpón<br>confinado|
|2|6,56|6,56|
|3|3,92|3,92|
|4|2,34|2,34|
|5|1,40|Maduración en cancha<br>(etapa 1)|
|6|0,83|0,83|
|7|0,50|0,50|
|8|0,30|0,30|
|9|0,29|Estabilización en cancha<br>(etapa 2)/b|
|10|0,29|0,29|
|11|0,29|0,29|
|12|0,29|0,29|
|**Promedio de emisión de**<br>**olor del ciclo [ouE/m2s]**|**0,53**||

/a Emisión de Olor al término de cada semana de compostaje.
/b En etapa final, se consideró de forma conservadora el valor de emisión de 0,29 [ou E /m 2 s], correspondiente a la condición de estabilización
de la semana 9, para la proyección de las últimas 4 semanas. De forma referencial, el valor final descrito en el estudio señalado para compostaje
de estas características correspondió a 0,08-0,21 [ou E /m [2] s].

Basado en la curva de emisión descrita y considerando que el proceso de compostaje en cancha tiene una duración
de 8 semanas, se representó la emisión en ciclos de 2 meses para todo el periodo anual.

37 Bidlingmaier, W., et al. (2007). Compost Science and Technology: Chap.11: Odor Emissions from Composting Plants. Waste Management

Series, Vol.8.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 64 de 112

**Galpón de recepción (Sist. de abatimiento olores)** : Tasa de Emisión de Olor proyectada en base a la
contribución de olor de las distintas unidades confinadas al interior del galpón según se describe en la siguiente
tabla.

Tabla 43 - Caracterización de emisión de olor de galpón de recepción

|Fuente|Largo<br>[m]|Ancho<br>[m]|Diámetro<br>[m]|Área<br>[m2]|Emisión de<br>Olor<br>[ou /m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou /s]<br>E|
|---|---|---|---|---|---|---|
|Estanque de mezcla<br>Estanque recepción<br>Triturado<br>Higienizado 1<br>Higienizado 2|- <br>- <br>5,00<br>- <br>-|- <br>- <br>4,00<br>- <br>-|16,00<br>6,00<br>- <br>4,50<br>4,50|201,06<br>28,27<br>20,00<br>15,90<br>15,90|3,80<br>3,80<br>3,80<br>3,80<br>3,80|764,04<br>107,44<br>76,00<br>60,44<br>60,44|

**Emisión total [ou** **E** **/s]** **1.068,35**

El valor de referencia aplicado a las fuentes de emisión de olor confinadas en galpón correspondió al valor
muestreado en pilas de Otras Localidades (estado inicial) en Centro de Manejo de Residuos Ecomaule durante la
campaña realizada el año 2019, correspondiente a 3,8 [ou E /m [2] s]. En base a lo descrito se obtuvo para cada galpón
de recepción (etapa 1 y 2) una Tasa de Emisión de Olor correspondiente a 1.068,35 [ou E /s]. A partir de este valor
de TEO, se aplicó el porcentaje de eficiencia de remoción de olor asociado a la implementación del sistema de
fotocatalítico UV, correspondiente a un 95%. Por lo tanto, de lo anterior se obtiene para cada galpón lo siguiente:

TEO Galpón recepción etapa 1 = TEO galpón [ [ou] s [E] ~~[]]~~ [ x (1 −Eficiencia de remoción de Olor] [Sist.fotocatalítico UV] [)]

TEO
Galpón recepción etapa 1 = 1.068,35 [ [ou] s [E] ~~[]]~~ [ x (1 −0,95) ]

TEO
Galpón recepción etapa 1 = 53, 42 [ [ou] s [E] ~~[]]~~

TEO
Galpón recepción etapa 2 = 1.068,35 [ [ou] s [E] ~~[]]~~ [ x (1 −0,95) ]

TEO
Galpón recepción etapa 2 = 53, 42 [ [ou] s [E] ~~[]]~~

Finalmente, para representar la contribución de olor de cada galpón se consideró una velocidad de salida de 3,05

[m/s] y una temperatura de 22 [°C], basado en las características descritas en ficha técnica EC-VTL-FB20.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 65 de 112

**Laguna anaeróbica/Laguna de percolados** : Emisión de Olor proyectada en base al valor muestreado en
laguna de percolados en Centro de Manejo de Residuos Ecomaule durante campaña realizada el año 2019,
correspondiente a 81,6 [ou E /m [2] s]. A partir de la Tasa de Emisión de Olor asociada a la superficie de emisión de
cada laguna, se proyectó la implementación de coberturas flotantes, cuya eficiencia de abatimiento correspondió
a 93%. De acuerdo con lo descrito en estudio P5052 “Evaluación Olfatometría Dinámica - Muestras Gaseosas,
Invennto” [38], realizado en año 2017. El valor de eficiencia aplicado corresponde al promedio del resultado de 6
mediciones informadas en el estudio según se detalla a continuación:

Tabla 44 - Eficiencia de abatimiento de olor de cubiertas flotantes según % de variación

|ID Prueba|% de variación|
|---|---|
|PS-6<br>PS-8<br>PS-10<br>PS-12<br>PL-2<br>PL-4|95,3%<br>86,9%<br>90,4%<br>88,7%<br>97,4%<br>99,2%|
|**Variación Promedio**|93%|

Tabla 45 - Caracterización de laguna anaeróbica y laguna de percolados

|Fuentes|Largo [m]|Ancho [m]|Área de<br>emisión [m2]|EO<br>[ouE/m2s]|TEO [ouE/S]|
|---|---|---|---|---|---|
|Laguna anaeróbica|64,00|31,25|2.000,00|81,60|163.200|
|Laguna de percolados|18,09|55,29|1.000,00|81,60|81.600|

Basado en lo anteriormente descrito se tiene lo siguiente:

TEO = TEO
Laguna+cobertura laguna ~~[~~ [ou] s [E] ~~[]]~~ [ x (1 −Eficiencia de abatimiento de Olor] [cobertura flotante] [)]

TEO = 163.200
Laguna anaeróbica+cobertura ~~[~~ [ou] s [E] [] x (1 −0,93) ]

TEO = 11. 424
Laguna anaeróbica ~~[~~ [ou] s [E] ~~[]]~~

TEO = 81.600
Laguna de percolados ~~[~~ [ou] s [E] ~~[]]~~ [ x (1 −0,93) ]

TEO = 5. 712
Laguna de percolados ~~[~~ [ou] s [E] []]

De los valores de emisión resultantes para cada fuente, se proyectó de forma constante durante todo el periodo
anual.

38 Invennto, (2017). P5052: Evaluación Olfatometría Dinámica - Muestras Gaseosas. Envirometrika. Chile.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 66 de 112

**Optimización de Sistema de Tratamiento de RILes** : Emisión de Olor proyectada en base al valor muestreado en
Centro de Manejo de Residuos Ecomaule durante campaña realizada el año 2019, para las siguientes fuentes de
emisión:

Tabla 46 - Caracterización de fuentes PTRILes optimizadas

|Fuentes|Largo [m]|Ancho [m]|Diámetro [m]|Área de<br>emisión [m2]|EO [ou /m2s]<br>E|TEO [ou /s]<br>E|
|---|---|---|---|---|---|---|
|Reactor aerobio 1<br>Reactor aerobio 2<br>Clarificador<br>Floculador<br>Reactor aerobio 3<br>Reactor aerobio 4|- <br>- <br>4,50<br>- <br>- <br>-|- <br>- <br>5,38<br>- <br>- <br>-|10,00<br>10,00<br>- <br>3,00<br>10,00<br>10,00|78,54<br>78,54<br>24,20<br>7,07<br>78,54<br>78,54|31,80<br>31,80<br>14,20<br>14,20<br>31,80<br>31,80|2.497,57<br>2.497,57<br>343,64<br>100,37<br>2.497,57<br>2.497,57|

En base a lo señalado por el Titular, la modificación de la Planta de Tratamiento de RILes contempla un desempeño
más eficiente a partir de la optimización de los procesos asociados a las unidades descritas. De acuerdo con lo
anterior, la emisión de olor optimizada para representar la contribución de olor de cada fuente consideró lo
siguiente:

TEO Unidad de tratamiento optimizada = TEO unidad de tratamiento [ [ou] s [E] ~~[]]~~ [ x (1 −Eficiencia] [optimización] [)]

Tabla 47 - Emisión de olor en fuentes PTRILes optimizadas

|Fuentes|Área de emisión<br>[m2]|EO<br>[ou /m2s]<br>E|TEO<br>[ou /s]<br>E|%Eficiencia<br>(Optimización<br>de sistema de<br>tratamiento)|TEO Optimizada<br>[ouE/s]|
|---|---|---|---|---|---|
|Reactor aerobio 1<br>Reactor aerobio 2<br>Clarificador<br>Floculador<br>Reactor aerobio 3<br>Reactor aerobio 4|78,54<br>78,54<br>24,20<br>7,07<br>78,54<br>78,54|31,80<br>31,80<br>14,20<br>14,20<br>31,80<br>31,80|2.497,57<br>2.497,57<br>343,64<br>100,37<br>2.497,57<br>2.497,57|40%<br>40%<br>40%<br>40%<br>40%<br>40%|1.498,54<br>1.498,54<br>206,18<br>60,22<br>1.498,54<br>1.498,54|

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 67 de 112

**Riego de digestato** : Emisión de Olor proyectada en base al valor de emisión de olor de referencia de digestato
tratado correspondiente a 0,32 [ou E /m [2] s]. El valor proviene de muestreo olfatométrico de digestato tratado en el
sector porcino. Dado que las características de los olores de este tipo de actividad industrial son ampliamente
reconocidas como ofensivas (Ej. Purines), se consideró como un valor de referencia adecuado para representar la
condición más desfavorable de emisión de olor.

El ciclo de operación de regadío agrícola y de digestato es realizado en un rango horario de 9 horas (09:00 a
17:59) durante los 7 días de la semana entre los meses de septiembre - abril. En la operación diaria se realizará
un riego secuencial de los tramos que componen ambas zonas de riego hasta alcanzar una aplicación en la
totalidad de la superficie disponibles, tanto en zona de riego 1 (118.620 [m [2] ]) como de zona de riego 2 (161.155

[m [2] ]). Por lo tanto, se consideró respectivamente un riego efectivo de 118.620 [m [2] /h] y 161.155 [m [2] /h] para cada
zona y así representar la emisión odorante de forma continua en los meses de regadío.

La contribución de olor para la aplicación de digestato tratado en riego agrícola, están asociadas al ciclo de
operación, donde la superficie regada desde un tiempo “cero” (t=0) experimenta una disminución gradual de la
carga odorante a medida que transcurre el tiempo. El comportamiento de esta curva de emisión es de tipo
exponencial, como se describe en el estudio realizado por el Departamento de Biosistemas y Ciencia Animal de la
Universidad de Manitoba [39] . Basado en esta curva de referencia se construyó una función de emisión de olor,
dependiente de la variable tiempo, donde se alcanza la condición base (previa a la aplicación) luego de
transcurridas 6 horas.

Tabla 48 - Curva de emisión de olor post aplicación de digestato tratado

|Función|Y= 0,134*(LN(H))+0,2281|
|---|---|
|Cantidad de horas desde<br>aplicación|Curva exponencial de Emisión de Olor<br>[ouE/m2s]/a|
|0 (Inicio de riego)|0,32|
|1|0,23|
|2|0,14|
|3|0,08|
|4|0,04|
|5|0,01|
|6|0,00|

Para representar la contribución de olor de cada zona de riego (TEO), se consideró lo siguiente:

TEO = EO
zona de riego digestato tratdo ~~[~~ m [ou] [2][E] s ~~[]]~~ [ x Superficie regada [m] [2] []]

39 Manitoba Livestock Manure Management Initiative Inc. (2002). Odour Production, Evaluation and Control. University of Manitoba. Canadá.

ANEXO 2 - BASE DE CÁLCULO DE PROYECCIÓN DE EMISIONES www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 68 de 112

**10** **ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA**

**10.1** **Plan de trabajo**

La metodología aplicada en el desarrollo del servicio de Modelación de Impacto Odorante para la Situación Actual y Futura se detalla en la siguiente
figura:

Figura 23 - Esquema de plan de trabajo y metodología aplicada

Fuente: Envirometrika, 2021.

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 69 de 112

**10.2** **Fuentes de emisión**

**Detalle operacional**

La Emisión de Olor (EO) es definida como la cantidad de olor emitida por una superficie o área respecto a una unidad de tiempo, representada
por la unidad [ou E /m [2] s], la cual es calculada a partir del muestreo de una fuente odorante. Para calcular la Tasa de Emisión de Olor (TEO) de
la fuente muestreada se multiplica la Emisión de Olor (EO) por el área de emisión de esta fuente, como se describe en la siguiente ecuación [40] :

TEO= EO ~~[~~ [ou] [E]

m [2] s ~~[]]~~ [ ∗Área[m] [2] []]

La configuración espacial, área de emisión, Tasa de Emisión de Olor (TEO) y ciclo de emisión de las fuentes modeladas, se basaron en la
información declarada por el Titular, según la siguiente descripción:

Tabla 49 - Situación actual: Características operacionales de fuentes emisoras (parte 1)

|ID|Fuente|Tipo de<br>fuente|Área [m2]|EO por<br>sup.<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|Ciclo de<br>operación|Horas de<br>operación|Días de<br>operación|Meses de<br>operación|
|---|---|---|---|---|---|---|---|---|---|
|1|Pila Lodo Agroindustrial - Edad 1|Difusa|6.558,00|14,7|96.402,60|Continuo|24 horas|7 días|12 meses|
|2|Pila Lodo Agroindustrial - Edad 1|Difusa|5.791,00|14,7|85.127,70|Continuo|24 horas|7 días|12 meses|
|3|Pila Lodo Agroindustrial - Edad 2|Difusa|7.455,00|8,3|61.876,50|Continuo|24 horas|7 días|12 meses|
|4|Pila Lodo Agroindustrial - Edad 3a|Difusa|1.200,00|1,6|1.920,00|Continuo|24 horas|7 días|12 meses|
|5|Pila Lodo Agroindustrial - Edad 3b|Difusa|1.200,00|1,6|1.920,00|Continuo|24 horas|7 días|12 meses|
|6|Pila lodo sanitario - Edad 1 Curicó|Difusa|3.457,00|5,7|19.704,90|Continuo|24 horas|7 días|12 meses|
|7|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|10.371,00|3,8|39.409,80|Continuo|24 horas|7 días|12 meses|
|8|Pila lodo sanitario - Edad 2 Curicó|Difusa|2.078,75|11,4|23.697,75|Continuo|24 horas|7 días|12 meses|
|9|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|6.236,25|5,9|36.793,88|Continuo|24 horas|7 días|12 meses|
|10|Pila lodo sanitario - Edad 1 Curicó|Difusa|1.126,50|5,7|6.421,05|Continuo|24 horas|7 días|12 meses|
|11|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|3.379,50|3,8|12.842,10|Continuo|24 horas|7 días|12 meses|
|12|Pila lodo sanitario - Edad 2 Curicó|Difusa|970,25|11,4|11.060,85|Continuo|24 horas|7 días|12 meses|
|13|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|2.910,75|5,9|17.173,43|Continuo|24 horas|7 días|12 meses|
|14|Pila lodo sanitario - Edad 1 Curicó|Difusa|1.063,00|5,7|6.059,10|Continuo|24 horas|7 días|12 meses|

40 Department of Water and Environmental Regulation. (2019). Guideline: Odour Emissions. Govermment of Western Australia. Australia.

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 70 de 112

Tabla 50 - Situación actual: Características operacionales de fuentes emisoras (parte 2)

|ID|Fuente|Tipo de<br>fuente|Área<br>[m2]|EO por<br>sup.<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|Ciclo de<br>operación|Horas de<br>operación|Días de<br>operación|Meses de<br>operación|
|---|---|---|---|---|---|---|---|---|---|
|15|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|3.189,00|3,8|12.118,20|Continuo|24 horas|7 días|12 meses|
|16|Pila lodo sanitario - Edad 2 Curicó|Difusa|1.220,50|11,4|13.913,70|Continuo|24 horas|7 días|12 meses|
|17|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|3.661,50|5,9|21.602,85|Continuo|24 horas|7 días|12 meses|
|18|Pila lodo sanitario - Edad 3 Curicó|Difusa|639,25|5,6|3.579,80|Continuo|24 horas|7 días|12 meses|
|19|Pila lodo sanitario - Edad 3 Otras Localidades|Difusa|1.917,75|1,7|3.260,18|Continuo|24 horas|7 días|12 meses|
|20|Pila lodo sanitario - Edad 1 Curicó|Difusa|335,75|5,7|1.913,78|Continuo|24 horas|7 días|12 meses|
|21|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|1.007,25|3,8|3.827,55|Continuo|24 horas|7 días|12 meses|
|22|Pila lodo sanitario - Edad 2 Curicó|Difusa|378,25|11,4|4.312,05|Continuo|24 horas|7 días|12 meses|
|23|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|1.134,75|5,9|6.695,03|Continuo|24 horas|7 días|12 meses|
|24|Pila lodo sanitario - Edad 1 Curicó|Difusa|1.990,75|5,7|11.347,28|Continuo|24 horas|7 días|12 meses|
|25|Pila lodo sanitario - Edad 1 Otras Localidades|Difusa|5.972,25|3,8|22.694,55|Continuo|24 horas|7 días|12 meses|
|26|Pila lodo sanitario - Edad 2 Curicó|Difusa|1.754,25|11,4|19.998,45|Continuo|24 horas|7 días|12 meses|
|27|Pila lodo sanitario - Edad 2 Otras Localidades|Difusa|5.262,75|5,9|31.050,23|Continuo|24 horas|7 días|12 meses|
|28|Pila lodo sanitario - Edad 3 Curicó|Difusa|520,25|5,6|2.913,40|Continuo|24 horas|7 días|12 meses|
|29|Pila lodo sanitario - Edad 3 Otras Localidades|Difusa|1.560,75|1,7|2.653,28|Continuo|24 horas|7 días|12 meses|
|30|Laguna de percolados|Difusa|1.000,00|81,6|81.600,00|Continuo|24 horas|7 días|12 meses|
|31|Laguna de agua rechazo|Difusa|154,00|81,6|12.566,40|Continuo|24 horas|7 días|12 meses|
|32|Reactor aerobio 1|Difusa|78,54|31,8|2.497,57|Continuo|24 horas|7 días|12 meses|
|33|Reactor aerobio 2|Difusa|78,54|31,8|2.497,57|Continuo|24 horas|7 días|12 meses|
|34|Clarificador|Difusa|24,20|14,2|343,64|Continuo|24 horas|7 días|12 meses|
|35|Floculador|Difusa|7,07|14,2|100,37|Continuo|24 horas|7 días|12 meses|
|36|Laguna lodos biológicos|Difusa|67,60|21,2|1.433,12|Continuo|24 horas|7 días|12 meses|
|37|Laguna lodo físico/químico|Difusa|61,20|2,3|140,76|Continuo|24 horas|7 días|12 meses|
|38|Lechos de secado 1|Difusa|302,00|4,2|1.268,40|Continuo|24 horas|7 días|12 meses|
|39|Lechos de secado 2 (lavado de camiones)|Difusa|267,00|32,8|8.757,60|Continuo|24 horas|7 días|12 meses|
|40|Laguna agua tratada|Difusa|377,00|2,4|904,80|Continuo|24 horas|7 días|12 meses|
|41|Monorelleno - Frente de trabajo|Difusa|4.508,00|11,1|50.038,80|Continuo|24 horas|7 días|12 meses|
|42|Relleno Sanitario - Frente de trabajo|Difusa|850,00|21,3|18.105,00|Continuo|24 horas|7 días|12 meses|

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 71 de 112

Tabla 51 - Situación futura: Características operacionales de fuentes emisoras (parte 1)

|ID|Fuente|Tipo de<br>fuente|Área [m2]|EO por<br>sup.<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|Ciclo de<br>operación|Horas de<br>operación|Días de<br>operación|Meses de<br>operación|
|---|---|---|---|---|---|---|---|---|---|
|1|Cancha de compostaje 1|Difusa|10.040,00|0,53|5.283,75|Continuo|24 horas|7 días|12 meses|
|2|Cancha de compostaje 2|Difusa|4.960,00|0,53|2.610,30|Continuo|24 horas|7 días|12 meses|
|3|Cancha de compostaje 3|Difusa|14.140,00|0,53|7.441,46|Continuo|24 horas|7 días|12 meses|
|4|Cancha de compostaje 4|Difusa|16.000,00|0,53|8.420,32|Continuo|24 horas|7 días|12 meses|
|5|Galpón de compostaje 1 (sistema de abatimiento)|Puntual|1,13|1128,86|1.276,71|Continuo|24 horas|7 días|12 meses|
|6|Galpón de compostaje 2 (sistema de abatimiento)|Puntual|1,13|1438,43|1.626,82|Continuo|24 horas|7 días|12 meses|
|7|Galpón de compostaje 3 (sistema de abatimiento)|Puntual|1,13|1438,43|1.626,82|Continuo|24 horas|7 días|12 meses|
|8|Galpón de compostaje 4 (sistema de abatimiento)|Puntual|1,13|1438,43|1.626,82|Continuo|24 horas|7 días|12 meses|
|9|Estanque acumulación clarificado - Etapa 1|Difusa|201,06|0,32|64,34|Continuo|24 horas|7 días|12 meses|
|10|Estanque acumulación de digestato - Etapa 1|Difusa|9,19|0,32|2,94|Continuo|24 horas|7 días|12 meses|
|11|Contenedor deshidratado mecánico - Etapa 1|Difusa|12,72|0,32|4,07|Continuo|24 horas|7 días|12 meses|
|12|Estanque acumulación clarificado - Etapa 2|Difusa|201,06|0,32|64,34|Continuo|24 horas|7 días|12 meses|
|13|Contenedor deshidratado mecánico - Etapa 2|Difusa|12,72|0,32|4,07|Continuo|24 horas|7 días|12 meses|
|14|Sistema de abatimiento olores - Etapa 1|Puntual|1,13|47,23|53,42|Continuo|24 horas|7 días|12 meses|
|15|Sistema de abatimiento olores - Etapa 2|Puntual|1,13|47,23|53,42|Continuo|24 horas|7 días|12 meses|
|16|Unidad de almacenamiento de digestato|Difusa|5.329,00|0,32|1.705,28|Continuo|24 horas|7 días|12 meses|
|17|Laguna anaeróbica|Puntual|2.000,00|5,71|11.424,00|Continuo|24 horas|7 días|12 meses|
|18|Laguna de percolados|Puntual|1.000,00|5,71|5.710,00|Continuo|24 horas|7 días|12 meses|
|19|Reactor aerobio 1|Puntual|78,54|19,08|1.498,54|Continuo|24 horas|7 días|12 meses|

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 72 de 112

Tabla 52 - Situación futura: Características operacionales de fuentes emisoras (parte 2)

|ID|Fuente|Tipo de<br>fuente|Área [m2]|EO por<br>sup.<br>[ou/m2s]<br>E|Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E|Ciclo de<br>operación|Horas de<br>operación|Días de<br>operación|Meses de<br>operación|
|---|---|---|---|---|---|---|---|---|---|
|20|Reactor aerobio 2|Difusa|78,54|19,08|1.498,54|Continuo|24 horas|7 días|12 meses|
|21|Reactor aerobio 3|Difusa|78,54|19,08|1.498,54|Continuo|24 horas|7 días|12 meses|
|22|Reactor aerobio 4|Difusa|78,54|19,08|1.498,54|Continuo|24 horas|7 días|12 meses|
|23|Clarificador|Difusa|24,20|8,52|206,18|Continuo|24 horas|7 días|12 meses|
|24|Floculador|Difusa|7,07|8,52|60,22|Continuo|24 horas|7 días|12 meses|
|25|Laguna lodos biológicos|Difusa|67,60|21,2|1.433,12|Continuo|24 horas|7 días|12 meses|
|26|Laguna lodo físico/químico|Difusa|61,20|2,3|140,76|Continuo|24 horas|7 días|12 meses|
|27|Laguna agua tratada|Difusa|377,00|0,25|94,25|Continuo|24 horas|7 días|12 meses|
|28|Alvéolo 7 - Frente de trabajo|Difusa|850,00|21,30|18.105,00|Continuo|24 horas|7 días|12 meses|
|29|Zona de riego 1|Difusa|13.180,00|0,32|4.217,60|Continuo|9 horas|7 días|Sept.- Abril|
|30|Zona de riego 2|Difusa|17.906,11|0,32|5.729,96|Continuo|9 horas|7 días|Sept.- Abril|

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 73 de 112

**Rueda de olor**

En la siguiente figura se muestra la rueda de olor aplicable al Proyecto, asociada a actividades de
disposición de residuos, planta de compostaje y tratamiento de lodos sanitarios, para la identificación
de las notas de olor características de este tipo de operación.

Figura 24 - Rueda de olor compostaje

Fuente: Suffet, I., H., et al., (2009) [41] .

41 Suffet, I., H., et al., (2009). Sensory Assessment and Characterization of Odor Nuisance Emissions during the Composting of Wastewater

Biosolids. Water Environment Research, Vol. 81, No. 7.

ANEXO 3 - PLAN DE TRABAJO Y METODOLOGÍA www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 74 de 112

**11** **ANEXO 4 - MODELO DE DISPERSIÓN**

**11.1** **Alcances del modelo**

Los criterios aplicados al modelo de dispersión contemplaron:

 Base meteorológica de pronóstico preprocesada mediante MMIF, para generar archivo de campos de

viento tridimensionales y otras variables meteorológicas de ingreso al software de modelación, en
cumplimiento a los criterios señalados en la Guía para el uso de modelos de calidad del aire en el
SEIA [43] .

 Meteorología de pronóstico WRF año 2019.

 Dominio de modelación correspondiente a 77 x 77 [km].

 Resolución de 1 [km] (espaciado de la cuadrícula), aplicando grilla de muestreo hasta un espaciado de

receptor igual a 250 [m], con el fin de obtener isolíneas más definidas en los puntos de evaluación.

 Período de emisión anual, basado en recomendaciones descritas en la “Guía para el uso de modelos

de calidad del aire en el SEIA” [44] .

**11.2** **Descripción del modelo**

La proyección de dispersión odorante considera la aplicación del software de modelación atmosférica
“CALPUFF VIEW” versión 8.6.0, modelo alternativo indicado por EPA [45] (USA). El software contempla 3
módulos de análisis numérico: CALMET, CALPUFF (v7.2.1) y CALPOST.

CALMET es un modelo que simula campos de viento, temperaturas y otras variables meteorológicas, en
un dominio de modelación tridimensional. Sin embargo, en la Guía para el uso de modelos de calidad del
aire en el SEIA se menciona que “...En el caso de CALPUFF, se recomienda usar la información del modelo
de pronóstico directamente, sin usar el preprocesador CALMET” [46] .
De acuerdo con lo anterior, se utilizó como preprocesador meteorológico el modelo MMIF [47] recomendado
por EPA (USA), siendo una alternativa a CALMET en la generación de los campos tridimensionales para la
evaluación en el análisis de impacto en la calidad del aire [48] .

CALPUFF es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario, capaz de modelar el transporte
y dispersión de contaminantes sobre un campo de viento tridimensional.
Este tipo de modelo permite la representación de una pluma de emisión continua como un número discreto
de paquetes de material correspondiente a la especie de interés.
El modelo evalúa la contribución de un “puff” en la concentración atmosférica de un receptor en un
instante determinado. Luego, la concentración total en un receptor resultará de la sumatoria de las
contribuciones de todos los “puff” [49] .
Finalmente, el modelo CALPOST procesa las salidas de CALPUFF creando así, los archivos con las
tabulaciones necesarias para la evaluación de los resultados según los percentiles definidos en el modelo.

43 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Servicio de Evaluación Ambiental,

Chile.
44 ibid.
45 Environmental Protection Agency, U.S.
46 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Chile. Servicio de Evaluación Ambiental,

Chile.
47 Mesoscale Model Interface Program, MMIF.
48 Brashers, B., Emery, C. (2014). Draft User’s Manual: The Mesoscale Model Interface Program (MMIF), Version 3.1. U.S. Environmental

Protection Agency.
49 Scire, J., Strimaitis, D., Yamartino, R. (2000). A User's Guide for the Calpuff Dispersion Model. Earth Tech, Inc.

P6343 - Modelación de impacto odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 75 de 112

**11.3** **Dominio de modelación**

El dominio o área de modelación se determinó en función de la magnitud del proyecto y sus emisiones,
así como la presencia de receptores [50] . El área de modelación cubrió un dominio de aproximadamente 77
x 77 [km], abarcando una superficie de 5.929 [km [2] ].

Figura 25 - Dominio de modelación

Fuente: Envirometrika - Google Earth, 2021.

**11.4** **Base meteorológica y grilla de muestreo**

Los datos meteorológicos utilizados corresponden a los generados por el modelo numérico de pronóstico
WRF [51], según recomendación del SEA [52] en la Guía para el uso de modelos de calidad del aire en el SEIA,
y fueron preprocesados mediante el modelo MMIF [53] .

Los datos de pronóstico corresponden al año 2019 (enero 01 00:00 a diciembre 31 23:00), con una
resolución inicial de 1 [km], considerando 11 niveles verticales de datos meteorológicos siendo el nivel
más bajo de aproximadamente 0 [m] a nivel del suelo, centrado en las coordenadas: Latitud 35,24825°
S, Longitud 71,455267 ° O. Adicionalmente, se aplicó una grilla de muestreo, cubriendo un área
aproximada de 480 [km [2] ] con un espaciado de receptor de hasta 250 [m].

50 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Chile.
51 Weather Research and Forecasting Model, WRF.
52 Servicio de Evaluación Ambiental, SEA.
53 Mesoscale Model Interface Program, MMIF.

ANEXO 4 - MODELO DE DISPERSIÓN www.envirometrika.com

P6343 - Modelación de impacto odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 76 de 112

**11.5** **Elevaciones de terreno**

Los componentes geofísicos del dominio de modelación fueron adquiridos desde la base de “U.S.
Geological Survey (USGS) - Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010)” con curvas
de nivel de resolución 30 [arc-second], equivalente a 1 [km] aproximadamente.

Figura 26 - Elevación de terreno del dominio

Fuente: Envirometrika. “Uso de suelo - Dominio de modelación” [Ortofoto]. Febrero 2021. Software: Calpuff View.
Versión 8.6.0 Toronto, ON: Lakes Environmental Software, 1995-2020.

ANEXO 4 - MODELO DE DISPERSIÓN www.envirometrika.com

P6343 - Modelación de impacto odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 77 de 112

**11.6** **Uso de suelo**

El uso de suelo fue provisto desde la base de datos “Moderate Resolution Imaging Spectroradiometer
(MODIS)” para Sudamérica con una resolución 15 [arc-second], cercano a 500 [m] aproximadamente.

Figura 27 - Uso de suelo del dominio

Fuente: Envirometrika. “Uso de suelo - Dominio de modelación” [Ortofoto]. Febrero 2021. Software: Calpuff View.
Versión 8.6.0 Toronto, ON: Lakes Environmental Software, 1995-2020.

ANEXO 4 - MODELO DE DISPERSIÓN www.envirometrika.com

P6343 - Modelación de impacto odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 78 de 112

**11.7** **Caracterización meteorológica anual**

La evaluación del comportamiento de los parámetros meteorológicos de velocidad y dirección del viento;
y su interacción a nivel local, se obtuvo a partir de la serie de datos de la grilla meteorológica de pronóstico
WRF-MMIF’19, en base a coordenadas representativas del Centro de Tratamiento de Residuos, donde se
encuentran localizadas las fuentes de emisión consideradas en el estudio. Los datos horarios comprenden
el periodo anual entre 00:00 01ene’19 y 23:00 de 31dic’19.

Tabla 53 - Coordenada central Centro de Tratamiento de Residuos

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|282.341|6.101.435|19 H|WGS 84|

Figura 28 - Distribución de rosa de viento anual

Fuente: Envirometrika - Google Earth, 2021.

ANEXO 4 - MODELO DE DISPERSIÓN www.envirometrika.com

P6343 - Modelación de impacto odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 79 de 112

**11.8** **Caracterización meteorológica anual horaria**

Los campos de viento están determinados por intensidad y las componentes vectoriales de dirección,
producto del comportamiento dinámico de las masas de aire. La interacción de estas componentes
caracteriza su variabilidad estacional y su efecto en la dispersión de contaminantes en el área de interés.

Tabla 54 - Distribución de rosas de viento anual horaria

|Col1|Rosa de vientos|Col3|Distribución de velocidad del viento|Características|
|---|---|---|---|---|
|Anual Nocturno<br>(00:00 a 6:59 horas)|||<br>8,41<br>14,21<br>40,39<br>22,27<br>9,67<br>3,41<br>1,02<br>0,47<br>0,12<br>0,04<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de vientos predominaron desde la<br>dirección SO con un 44% de la frecuencia.<br>La velocidad varió de ventolina54 a brisa débil. La<br>distribución del viento tuvo una tendencia<br>asimétrica positiva. <br> <br>Velocidad promedio de viento: 1,84 [m/s].<br> <br>Frecuencia de vientos calmos: 8,41%.|
|Anual AM<br>(7:00 a 14:59 horas)|||<br>5,17<br>8,87<br>23,66<br>30,96<br>20,00<br>7,09<br>2,60<br>1,30<br>0,27<br>0,07<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron en mayor<br>frecuencia desde el rango SSO-SO, con un 65%<br>de la frecuencia.<br>La velocidad varió de ventolina a brisa<br>moderada55.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,45 [m/s].<br> <br>Frecuencia de vientos calmos: 5,17%.|
|Anual PM<br>(15:00 a 23:59 horas)|||<br>6,42<br>11,51<br>30,41<br>23,38<br>15,31<br>7,06<br>3,90<br>1,43<br>0,33<br>0,24<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, se observó una<br>predominancia de los vientos desde el rango<br>SSO-SO, con un 54% de la frecuencia. La<br>velocidad de los vientos varió de ventolina a brisa<br>moderada56.<br>La distribución de los vientos se observó con una<br>tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,31 [m/s]<br> <br>Frecuencia de vientos calmos: 6,42%|

54 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A - Claves alfanuméricas - Escala

Beaufort de Viento. OMM-N°306, Suiza: OMM.
55 Ibid.
56 Ibid.

ANEXO 4 - MODELO DE DISPERSIÓN www.envirometrika.com

P6343 - Modelación de impacto odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 80 de 112

**12** **ANEXO 5 - ANÁLISIS METEOROLÓGICO**

La evaluación del comportamiento de los parámetros meteorológicos y su interacción a nivel local, se realizó a
partir de series de datos horarios para el periodo de un año, extraídas desde la grilla meteorológica de pronóstico
WRF-MMIF’19. Cuya extracción fue en base a coordenadas representativas de la instalación, donde se localizan
las fuentes de emisión consideradas en el presente estudio.

Tabla 55 - Coordenadas representativas de Centro de Tratamiento de Residuos

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|282.341|6.101.435|19 Sur|WGS-84|

Los parámetros meteorológicos considerados fueron:

 - Velocidad del viento [m/s].

 Dirección del viento [grados].

 - Altura de capa de mezcla [m].

 - Temperatura [°C].

El análisis se realizó bajo el formato de:

 Rosas de viento y gráficos de distribución de velocidad del viento.

 - Campos de viento.

 - Altura de capa de mezcla.

Los resultados se analizaron de acuerdo con el comportamiento anual, estacional y horario. La descripción de cada
ciclo se indica en la siguiente tabla:

Tabla 56 - Descripción de ciclos de análisis meteorológicos

|Ciclo|Descripción|Col3|
|---|---|---|
|Anual|12 meses|Enero a diciembre|
|Estacional|Verano|22 de diciembre a 21 de marzo|
|Estacional|Otoño|22 de marzo a 21 de junio|
|Estacional|Invierno|22 de junio a 21 de septiembre|
|Estacional|Primavera|22 de septiembre a 21 de diciembre|
|Horario|Nocturno|00:00 a 06:59|
|Horario|AM|07:00 a 14:59|
|Horario|PM|15:00 a 23:59|

La evaluación de campos de viento incluyó antecedentes bibliográficos topoclimáticos que describen la dinámica
y cinética de las masas de aire que interactúan en la zona de estudio. Esta información permite evaluar la
coherencia de las series de datos obtenidas de la meteorología de pronóstico e interpretar las variables de
influencia en las condiciones de dispersión.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343 - Modelación de impacto odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 81 de 112

**12.1** **Rosas y campos de viento**

Los campos de viento están determinados por la velocidad del viento y las componentes vectoriales de
dirección, producto del comportamiento dinámico de las masas de aire. La interacción de estas componentes
caracteriza el comportamiento del viento y cómo intervienen en la dispersión de contaminantes en el área de
interés.

Tabla 57 - Rosas y campos de viento pronóstico anual

|Col1|Rosa de vientos|Col3|Distribución de velocidad del viento|Características|
|---|---|---|---|---|
|Anual Nocturno|||<br>8,41<br>14,21<br>40,39<br>22,27<br>9,67<br>3,41<br>1,02<br>0,47<br>0,12<br>0,04<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de vientos predominaron desde la<br>dirección SO con un 44% de la frecuencia anual.<br>La velocidad varió de ventolina57 a brisa débil. La<br>distribución del viento tuvo un comportamiento<br>asimétrico positivo. <br> <br>Velocidad promedio de viento: 1,84 [m/s].<br> <br>Frecuencia de vientos calmos: 8,41%.|
|Anual AM|||<br>5,17<br>8,87<br>23,66<br>30,96<br>20,00<br>7,09<br>2,60<br>1,30<br>0,27<br>0,07<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron en mayor<br>frecuencia desde el rango SO-SSO, con un 65%<br>de la frecuencia.<br>La velocidad varió de ventolina a brisa débil58.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia a la normalidad.<br> <br>Velocidad promedio de viento: 2,45 [m/s].<br> <br>Frecuencia de vientos calmos: 5,17%.|
|Anual PM|||<br>6,42<br>11,51<br>30,41<br>23,38<br>15,31<br>7,06<br>3,90<br>1,43<br>0,33<br>0,24<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, se observó una<br>predominancia de los vientos desde el rango<br>SSO-SO con un 54% de la frecuencia. La<br>velocidad de los vientos varió de ventolina a brisa<br>débil59.<br>La distribución de los vientos se observó con una<br>tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,31 [m/s]<br> <br>Frecuencia de vientos calmos: 6,42%|

Fuente: Envirometrika, 2021.

Del análisis meteorológico anual WRF-MMIF’19 se resume que:
Las masas de aire describieron un comportamiento homogéneo en cuando a la variable direccional del viento,
siendo predominante la dirección SO, principalmente en horario nocturno. En cuanto a la velocidad del viento,
está osciló principalmente de ventolina a brisa débil. En horario nocturno destacan las ventolinas, con
intensidades cercanas a 2 [m/s]. Respecto a los vientos calmos oscilan en el rango de 6 a 8%, y la mayor
frecuencia se presentaría en horario nocturno.

57 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A - Claves alfanuméricas - Escala

Beaufort de Viento. OMM-N°306, Suiza: OMM.
58 Ibíd.
59 Ibíd.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343 - Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 82 de 112

Tabla 58 - Rosas y campos de viento pronóstico estacional - Verano

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Verano Nocturno||||6,03<br>12,22<br>53,17<br>19,52<br>6,67<br>1,90<br>0,32<br>0,16<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|El viento predominó desde la componente SO,<br>con un 52% de la frecuencia. En general, la<br>intensidad del viento se caracterizó por variar<br>de ventolina a brisa muy débil.<br>La distribución de frecuencia de velocidad del<br>presentó una asimetría positiva. <br> <br>Promedio velocidad del viento: 1,72 [m/s].<br> <br>Frecuencia de vientos calmos: 6,03%.|
|Verano AM||||3,33<br>6,67<br>21,25<br>34,58<br>25,97<br>5,28<br>1,25<br>1,39<br>0,28<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron con mayor<br>frecuencia desde el rango SSO-SO, con un 74%<br>de la frecuencia. La velocidad del viento varió<br>de brisa muy débil a débil. La distribución<br>presento una asimetría positiva.<br> <br>Promedio velocidad del viento: 2,55 [m/s].<br> <br>Frecuencia de vientos calmos: 3,33%.|
|Verano PM||||5,68<br>7,53<br>28,27<br>26,67<br>21,85<br>5,06<br>3,21<br>1,36<br>0,37<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de viento predominaron desde la<br>componente SSO y SO, con un 34% y 23% de<br>la frecuencia respectivamente. La intensidad<br>del viento fluctuó de brisa muy débil a<br>moderada. La curva de distribución tuvo una<br>tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,42 [m/s].<br> <br>Frecuencia de vientos calmos: 5,68%.|

Centro de Tratamiento de Residuos.
Fuente: Envirometrika, 2021.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343 - Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 83 de 112

Tabla 59 - Rosas y campos de viento pronóstico estacional - Otoño

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Otoño Nocturno||||10,56<br>16,15<br>39,91<br>23,29<br>7,61<br>1,71<br>0,62<br>0,16<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de viento provinieron con mayor<br>frecuencia desde la componente SO con un<br>33% de predominancia. La intensidad del<br>viento varió mayormente de calmos a brisa muy<br>débil<br>La distribución de frecuencia de velocidad del<br>viento muestra una tendencia asimétrica<br>positiva. <br> <br>Promedio velocidad del viento: 1,66 [m/s].<br> <br>Frecuencia de vientos calmos: 10,56%.|
|Otoño AM||||6,79<br>11,68<br>31,11<br>29,89<br>13,18<br>4,62<br>1,49<br>0,68<br>0,27<br>0,27<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|El viento presentó una predominancia desde las<br>componentes SO y SSO con un 35% y 23% de<br>la frecuencia respectivamente. La intensidad<br>del viento fluctuó de ventolina a brisa muy<br>débil.<br>Respecto a la distribución, ésta tuvo una<br>tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,13 [m/s].<br> <br>Frecuencia de vientos calmos: 6,79%.|
|Otoño PM||||9,06<br>18,00<br>36,72<br>20,41<br>8,33<br>3,99<br>1,69<br>0,97<br>0,00<br>0,85<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron en mayor<br>frecuencia desde el componente SO y SSO con<br>un<br>25%<br>y <br>17%<br>de<br>la<br>frecuencia<br>respectivamente. En general, la velocidad del<br>viento varió de ventolina a brisa muy débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo un comportamiento asimétrico<br>positivo. <br> <br>Promedio velocidad del viento: 1,88 [m/s].<br> <br>Frecuencia de vientos calmos: 9,06%.|

Centro de Tratamiento de Residuos.
Fuente: Envirometrika, 2021.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343 - Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 84 de 112

Tabla 60 - Rosas y campos de viento pronóstico estacional - Invierno

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Invierno Nocturno||||6,68<br>14,75<br>32,30<br>18,94<br>12,73<br>9,32<br>3,11<br>1,55<br>0,47<br>0,16<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario nocturno los vientos<br>provinieron mayormente desde la componente<br>SO con un 36% de la frecuencia. La intensidad<br>del viento osciló de ventolina a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,23 [m/s].<br> <br>Frecuencia de vientos calmos: 6,68%.|
|Invierno AM||||7,20<br>10,33<br>21,47<br>28,13<br>17,39<br>8,70<br>3,67<br>2,58<br>0,54<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron mayormente del<br>rango SSO-SO con un 54% de la frecuencia. La<br>velocidad fluctuó de ventolina a brisa débil.<br>La<br>intensidad<br>del<br>viento<br>presentó<br>una<br>distribución mesocúrtica. <br> <br>Promedio velocidad del viento: 2,51 [m/s].<br> <br>Frecuencia de vientos calmos: 7,2%.|
|Invierno PM||||6,16<br>11,96<br>32,37<br>18,00<br>14,37<br>7,85<br>5,92<br>2,42<br>0,85<br>0,12<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de vientos provinieron con mayor<br>frecuencia desde la componente SO con un<br>35% de la frecuencia. En general, la intensidad<br>del viento varió de ventolina a brisa débil y la<br>distribución presentó una tendencia asimétrica<br>positiva.<br> <br>Promedio velocidad del viento: 2,42 [m/s].<br> <br>Frecuencia de vientos calmos: 6,16%.|

Centro de Tratamiento de Residuos.
Fuente: Envirometrika, 2021.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343 - Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 85 de 112

Tabla 61 - Rosas y campos de viento pronóstico estacional - Primavera

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Primavera Nocturno||||10,36<br>13,66<br>36,42<br>27,32<br>11,62<br>0,63<br>0,00<br>0,00<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Predominio de los vientos desde la componente<br>SO con un 56% de la frecuencia. La velocidad<br>del viento fluctuó de calmo a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica negativa. <br> <br>Promedio velocidad del viento: 1,75 [m/s].<br> <br>Frecuencia de vientos calmos: 10,36%.|
|Primavera AM||||3,30<br>6,73<br>20,74<br>31,32<br>23,63<br>9,75<br>3,98<br>0,55<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron el rango SSO-SO<br>con un 73% de la frecuencia. La velocidad del<br>viento osciló de ventolina a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento exhibió una curva mesocurtica. <br> <br>Promedio velocidad del viento: 2,64 [m/s].<br> <br>Frecuencia de vientos calmos: 3,3%.|
|Primavera PM||<br>||<br>4,76<br>8,42<br>24,18<br>28,57<br>16,85<br>11,36<br>4,76<br>0,98<br>0,12<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, los vientos provinieron<br>desde el rango SSO-SO con un 61% de la<br>frecuencia. La velocidad del viento osciló de<br>ventolina a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento exhibió una curva mesocurtica. <br> <br>Promedio velocidad del viento: 2,54 [m/s].<br> <br>Frecuencia de vientos calmos: 4,76%.|

Centro de Tratamiento de Residuos.
Fuente: Envirometrika, 2021.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 86 de 112

Figura 29 - Comportamiento de campos de viento

Fuente: Envirometrika, 2021.

A nivel regional, el área de estudio se localiza en la cuenca hidrográfica Río Maule, compuesta principalmente
por las subcuencas del río Claro, inserta en la unidad geomorfológica fluvial glacio-volcánico. En la región es
posible identificar tres unidades de relieve, la Cordillera de Los Andes, Depresión Intermedia y la Cordillera
de la Costa.

La localidad más cercana es Camarico, perteneciente tanto a la Provincia de Talca como a la Comuna de Río
Claro Santa Cruz se ubica en el valle Tinguiririca, específicamente en un sector caracterizado por un relieve
que se conforma por un valle originado a partir de material de arrastre depositado en las riberas de los ríos,
esteros y otros cursos de agua, que presenta suelos de riego, planos, profundos.

El área donde se inserta el proyecto, se inscribe en el tipo climático templado cálido con lluvias invernales, el
cual presenta variaciones por encontrarse en la depresion intermedia entre cordilleras. La estacion seca y
calurosa se prologa por alrededor de 4 a 6 meses con temperaturas máximas cercanas a los 30 [°C]. En la
época de frio y lluvia las temperaturas minimas se estiman bajo los 7 [°C] [59] con precipitaciones concentradas
en los meses de invierno.

La temperatura media anual oscila entre los 13 [°C] y 15 [°C] y el registro de precipitaciones en un año
normal oscila entre los 740 y 1000 [mm] [60] .

59 Gobierno Regional del Maule. (2015). Atlas Territorial Región del Maule. Programa Gestión Territorial para Zonas Rezagadas. Gobierno de

Chile.
60 Ibíd.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 87 de 112

**12.2** **Altura de mezcla**

La altura de mezcla depende fuertemente del calentamiento superficial, ya que éste determina el ascenso de
las masas de aire (boyancia) y, en consecuencia, la inestabilidad atmosférica que determina la altura a la
cual las emisiones se dispersan. Por esta razón, la variación de la altura de mezcla es de ciclo diario y
estacional.
A continuación, se presentan isolíneas de alturas de mezclas para cuatro períodos estacionales en tres ciclos
horarios, dentro del dominio de modelación.

Figura 30 - Distribución general de altura de mezcla (ortofotografías)

Fuente: Envirometrika, 2021.

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 88 de 112

Los periodos de obtención de las isolíneas de altura de mezcla, desde el modelo de dispersión, se detallan a
continuación:

Tabla 62 - Registro de ortofotografías - Isolíneas de altura de mezcla

Gráfico 1 - Altura de mezcla y temperatura - Serie de tiempo

Fuente: Envirometrika, 2021.

Tabla 63 - Altura de mezcla - promedios por periodo estacional y horario [m]

ANEXO 5 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 89 de 112

**13** **ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE**

Los modelos meteorológicos o de calidad del aire utilizados para representar una aproximación a la realidad,
incorporan dentro de sus resultados, incertidumbres. Estas incertidumbres se expresan a través de las
diferencias entre lo estimado y las observaciones (o errores del modelo) [61] .

El objetivo de realizar un análisis de incertidumbre es evaluar la capacidad de un modelo de representar una
cierta situación atmosférica [62] .

Considerando que la meteorología es el componente principal que determina la variabilidad espacial y
temporal de las concentraciones de contaminantes dentro de un dominio específico, es necesario realizar un
análisis de incertidumbre a las variables meteorológicas más relevantes en términos de dispersión como son
la velocidad del viento, la dirección del viento, la temperatura y la humedad relativa [63] . Aunque se debe tener
en cuenta que no siempre es posible contar con registros de las variables más relevantes.
El análisis debiera incorporar incertidumbre de las variables meteorológicas de superficie y de altura, sin
embargo, en Chile, los datos meteorológicos de altura provienen principalmente de los radiosondeos que
realiza la Dirección Meteorológica de Chile (DCM) en Antofagasta, Santo Domingo, Puerto Montt y Punta
Arenas, lugares que se encuentran fuera del área de modelación en donde se emplaza la zona de estudio y,
por lo tanto, no son representativos de la zona evaluada. Cabe destacar, que, en tales casos, la información
de altura medida representa la estructura vertical de la costa y esta difiere de la continental [64] . Debido a lo
anterior, el análisis de incertidumbre solo aborda las diferencias entre los parámetros meteorológicos
superficiales (observado) y lo modelado (estimado).

El análisis consiste en realizar:

a) **Diagnóstico de datos meteorológicos:** Este diagnóstico tiene por objeto determinar la variabilidad

temporal de cada uno de los parámetros meteorológicos. Debe incluir series de tiempo y ciclos diarios.

b) **Comparación entre pronóstico y observaciones** : La finalidad de esta comparación es determinar

Error e Incertidumbre en forma cualitativa y cuantitativa.

 Análisis cualitativo: Comparaciones gráficas para datos meteorológicos observados y simulados,
principalmente, a través de los ciclos diarios.

 Análisis cuantitativo: Cálculo de las métricas de estadísticas del sesgo (BIAS), Error medio cuadrático
(RSME) y Coeficiente de correlación entre las variables meteorológicas pronosticadas y observadas.

61 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.
62 Ibíd.
63 Ibíd.
64 Ibíd.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 90 de 112

**13.1** **Levantamiento y selección de información meteorológica observada**

Con el objeto de evaluar los datos meteorológicos tridimensionales generados del modelo de pronóstico WRF,
la comparación de las observaciones con las simulaciones del modelo en el punto de medición de los datos
observados permite evaluar la incertidumbre asociada [65] . Para lograr este objetivo se hace necesario levantar
la información meteorológica en el área de estudio. Por lo anterior se realizó una búsqueda en las fuentes
públicas de información, aplicándose criterios de validación de los datos [66], tales como: representatividad de
la estación meteorológica, estándares de instalación WMO [67], porcentaje de datos válidos, variables
meteorológicas mínimas, entre otras.

La información se resume en la siguiente tabla:

Tabla 64 - Estaciones meteorológicas superficiales en el dominio de modelación WRF

|ID|Nombre estación|Coordenadas geográficas UTM<br>Huso 19|Col4|Datos válidos %|Col6|Col7|
|---|---|---|---|---|---|---|
|ID|Nombre estación|Este [m]|Sur [m]|Temperatura|Velocidad<br>viento|Dirección<br>viento|
|1|U. C. del Maule68|262.216|6.075.477|99,19|88,34|98,97|
|2|Tres Esquinas69|298.116|6.108.659|82,19|44,22|49,81|
|3|Aresti70|290.666|6.107.751|98,53|65,88|0,0|
|4|San Rafael71|274.890|6.090.475|87,21|42,83|73,76|

En relación con el análisis de la representatividad de los datos observados (registros de concentración de
contaminantes), la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”(SEA, 2012), señala en el
punto 6.6.1 Datos de calidad del aire observados que los **valores de calidad del aire** a ser sumados a los
resultados de la modelación de calidad del aire deben indicar claramente el periodo de las mediciones y la
justificación y análisis de la representatividad de dichas mediciones del dominio de modelación. Por lo tanto,
dado que para la componente olor no se dispone de algún tipo de dispositivo/sensor/estación que permita el
registro de los niveles de concentración de olor en las estaciones de monitoreo, no es aplicable su
incorporación al modelo ni la realización del análisis de representatividad de estos registros de concentración
de calidad del aire en el dominio de modelación. Siendo este análisis aplicable para contaminantes como
material particulado y/o gases. Donde el área de representatividad de una estación para contaminantes
primarios depende fuertemente de las características particulares de su lugar de emplazamiento.

Por otra parte, la representatividad meteorológica de las estaciones observadas, según lo señalado en la
“Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2012), sección 4.2 - Modelos
recomendados, aclara que el radio de 5 [km] definido para las estaciones meteorológicas tiene relación con
la distancia entre la estación y las fuentes de emisión. Esto para alcanzar un mayor grado de representatividad
meteorológica al momento de ser aplicable su **ingreso al modelo**, teniendo en consideración las
características de terreno de complejo del territorio nacional (meteorología heterogénea).

En el caso que se disponga de una sola estación dentro del radio de representatividad meteorológica, la Guía
señala que el modelo de dispersión debiera ser utilizado sólo con datos provenientes de un modelo
meteorológico de pronóstico y de forma directa sin usar el preprocesador Calmet. Por lo tanto, para la

65 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.
66 Ibíd.
67 World Meteorological Organization (2010). Guide to Meteorological Instruments and Methods of Observation-WMO-No. 8, Geneva,

Switzerland.
68 Ministerio del Medio Ambiente (2018). Sistema de Información Nacional de Calidad del Aire (SINCA). Adquirido 05 febrero de 2021:

https://sinca.mma.gob.cl/index.php/estacion/index/key/710
69 Ministerio de Agricultura (2020). Red Agrometeorológica Nacional (AGROMET). Adquirido 05 febrero de 2021:

https://www.agromet.cl/datos-historicos
70 Ibíd.
71 Ibíd.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 91 de 112

modelación del proyecto, en cumplimiento a lo anteriormente descrito, se utilizó meteorología de pronóstico
WRF-MMIF en formato Calpuff-ready o para uso directo en el modelo de dispersión.

En el uso de meteorología de pronóstico, se entiende que cualquier dato proveniente de este tipo de modelo
(meteorológico), representa una aproximación a la realidad y, en consecuencia, sus resultados tienen
incertidumbres asociadas. Estas incertidumbres se expresan a través de las diferencias entre lo estimado y
las observaciones (o errores del modelo). Siendo aplicable el desarrollo de un análisis de incertidumbre, cuyo
objetivo es evaluar la capacidad del modelo de representar una cierta situación atmosférica y no es ningún
juicio sobre la bondad del modelo o su usuario, sino sólo un reconocimiento de que ningún modelo es capaz
de representar la atmósfera en forma exacta y que, además, su desempeño depende de cada situación
particular.

Respecto a la realización del análisis de incertidumbre la Guía de Modelación, sección 6.8 - Análisis de los
datos meteorológicos y capítulo 7 - Presentación de análisis de incertidumbre, señala que se debe realizar
una comparación entre los datos meteorológicos tridimensionales generados del modelo de pronóstico WRF
y las observaciones (estación superficial) en el punto de medición de los datos observados. Dado que las
fuentes públicas de información meteorológica no informan la incertidumbre de las mediciones registradas,
se excluye este criterio del análisis, asumiendo que los datos no presentan esta variable.

En relación con lo anterior, la Guía de Modelación no describe restricciones en cuanto a distancia de la
estación para su utilización en el análisis de incertidumbre, sobre la base que la estación seleccionada se
emplaza dentro del dominio meteorológico definido para el proyecto.

Por lo tanto, para el desarrollo del análisis de incertidumbre se seleccionó la Estación U. C. del Maule (MMA),
basado en la mayor representatividad de los registros válidos de velocidad del viento (88%), bajo la cual se
desarrollarían las condiciones desfavorables de dispersión (vientos calmos).

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 92 de 112

**13.2** **Diagnóstico de datos meteorológicos**

**Datos meteorológicos**

Los datos meteorológicos corresponden a datos de pronóstico y observados. Los datos de pronóstico
son aquellos generados por el modelo numérico de pronóstico WRF [72] y los datos observados son los
registrados por la estación meteorológica superficial.

De pronóstico, WRF

La serie de pronóstico representa los datos de la meteorología de pronóstico del año 2019. La
coordenada utilizada para la extracción de datos pronosticados corresponde a la misma coordenada
de localización de la estación meteorológica superficial seleccionada, con el fin de comparar los datos
del mismo periodo y lugar [73] .

Tabla 65 - Coordenada de localización, serie de pronóstico WRF

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|262.216|6.075.477|19 Sur|WGS 84|

Los parámetros meteorológicos considerados para el análisis corresponden a:

 - Velocidad del viento [m/s].

 Dirección del viento [grados].

 - Temperatura [°C].

En función del total de horas teóricas (8.760 horas) se determinó el porcentaje de datos existentes
para los datos de pronóstico WRF corresponden al 100% de los registros esperados para el periodo
anual.

72 Weather Research and Forecasting Model.
73 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 93 de 112

Observados, estación meteorológica superficial

La serie observada corresponde a datos meteorológicos registrados por la Estación Universidad Católica
del Maule, año 2019, perteneciente al Ministerio de Medio Ambiente [74], la cual se localiza en las
siguientes coordenadas:

Tabla 66 - Coordenada de localización estación meteorológica

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|262.216|6.075.477|19 Sur|WGS 84|

Figura 31 - Localización de estación meteorológica

Fuente: Envirometrika, 2021.

El análisis estadístico de incertidumbre entre las series de datos de pronóstico y observados, requirió
de un contraste de información de los mismos parámetros meteorológicos para ambas series y
obtenidas del mismo período. Los parámetros disponibles y considerados por la estación corresponden

a:

 - Velocidad del viento [m/s].

 Dirección del viento [grados].

 - Temperatura [°C].

74 Ministerio del Medio Ambiente (2018). Sistema de Información Nacional de Calidad del Aire (SINCA). Adquirido 5 febrero de

2021:https://sinca.mma.gob.cl/index.php/estacion/index/key/710

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 94 de 112

Los datos de la serie fueron validados siguiendo los lineamientos definidos en la guía “Meteorological
Monitoring Guidance for Regulatory Modeling Applications” [75], donde se definen distintos niveles de
validación. Para los parámetros meteorológicos considerados se realizó la validación Nivel 3 que implica
un análisis más detallado, debido a que los errores de las mediciones podrían causar inconsistencias
en el análisis y modelación de los resultados [76] .

Luego de la validación de la serie de datos, se debe tener en consideración que la “Guía para el Uso
de Modelos de Calidad del Aire en el SEIA” señala lo siguiente: “Se recomienda que el porcentaje de
datos válidos de las series de tiempo sea siempre superior al 75%...” [77] . De acuerdo a lo anterior, la
serie de datos de la estación meteorológica cumplió con la recomendación, pues los porcentajes de
datos válidos para cada parámetro resultó ser:

Tabla 67 - Porcentaje datos válidos en parámetros evaluados

|Parámetro meteorológico<br>evaluado|% datos válidos|Cumple con<br>recomendación SEA<br>(>75%)|
|---|---|---|
|Velocidad del viento [m/s]<br>Dirección del viento [°]<br>Temperatura [°C]|88,3<br>99,0<br>99,2|<br><br>|

75 Environmental Protection Agency(2000). Meteorological Monitoring Guidance for Regulatory Modeling Applications. Office of Air and

Radiation. Office of Air Quality Planning and Standards Research Triangle Park, NC 27711.
76 Ibíd.
77 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 95 de 112

**Series de tiempo**

Con la finalidad de analizar la calidad de la información, se graficaron las series de tiempo completas
de los datos de pronóstico y observados [78] para las variables meteorológicas de temperatura [°C] y
velocidad del viento [m/s].

Temperatura, [°C]

Gráfico 2 - Serie pronóstico, temperatura [°C]

Fuente: Envirometrika, 2021.

Gráfico 3 - Serie observada, temperatura [°C]

Fuente: Envirometrika, 2021.

78 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 96 de 112

Velocidad del viento, [m/s]

Gráfico 4 - Serie pronóstico, velocidad del viento [m/s]

Fuente: Envirometrika, 2021.

Gráfico 5 - Serie observada, velocidad del viento [m/s]

Fuente: Envirometrika, 2021.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 97 de 112

**Ciclos diarios**

Para visualizar fluctuaciones típicas de las variables meteorológicas, se obtuvieron los ciclos horarios
promedios de cada parámetro, junto con su variabilidad en términos de los percentiles 5 y 95 [79] .

Temperatura, [°C]

Se graficaron los ciclos diarios promedios de temperaturas [°C], para las series pronóstico y observada.

Tabla 68 - Ciclos diarios de la temperatura - serie pronóstico

|Hora|Promedio de<br>Temperatura [°C]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|11,03<br>4,31<br>17,24<br>10,51<br>4,11<br>16,41<br>10,06<br>3,54<br>15,76<br>9,70<br>3,44<br>14,99<br>9,38<br>3,45<br>14,45<br>9,05<br>3,34<br>14,38<br>8,72<br>3,01<br>14,07<br>8,92<br>2,75<br>14,34<br>9,64<br>2,77<br>15,85<br>10,75<br>3,10<br>17,91<br>12,20<br>3,81<br>19,69<br>13,87<br>4,60<br>21,70<br>15,58<br>5,95<br>23,58<br>17,04<br>8,01<br>25,17<br>18,14<br>9,36<br>26,41<br>18,76<br>9,83<br>27,23<br>18,84<br>9,70<br>27,57<br>18,42<br>8,96<br>27,63<br>17,16<br>7,84<br>26,94<br>15,32<br>7,03<br>24,72<br>13,78<br>6,29<br>22,00<br>13,03<br>5,78<br>20,53<br>12,36<br>5,30<br>19,31<br>11,58<br>4,92<br>18,35|11,03<br>4,31<br>17,24<br>10,51<br>4,11<br>16,41<br>10,06<br>3,54<br>15,76<br>9,70<br>3,44<br>14,99<br>9,38<br>3,45<br>14,45<br>9,05<br>3,34<br>14,38<br>8,72<br>3,01<br>14,07<br>8,92<br>2,75<br>14,34<br>9,64<br>2,77<br>15,85<br>10,75<br>3,10<br>17,91<br>12,20<br>3,81<br>19,69<br>13,87<br>4,60<br>21,70<br>15,58<br>5,95<br>23,58<br>17,04<br>8,01<br>25,17<br>18,14<br>9,36<br>26,41<br>18,76<br>9,83<br>27,23<br>18,84<br>9,70<br>27,57<br>18,42<br>8,96<br>27,63<br>17,16<br>7,84<br>26,94<br>15,32<br>7,03<br>24,72<br>13,78<br>6,29<br>22,00<br>13,03<br>5,78<br>20,53<br>12,36<br>5,30<br>19,31<br>11,58<br>4,92<br>18,35|11,03<br>4,31<br>17,24<br>10,51<br>4,11<br>16,41<br>10,06<br>3,54<br>15,76<br>9,70<br>3,44<br>14,99<br>9,38<br>3,45<br>14,45<br>9,05<br>3,34<br>14,38<br>8,72<br>3,01<br>14,07<br>8,92<br>2,75<br>14,34<br>9,64<br>2,77<br>15,85<br>10,75<br>3,10<br>17,91<br>12,20<br>3,81<br>19,69<br>13,87<br>4,60<br>21,70<br>15,58<br>5,95<br>23,58<br>17,04<br>8,01<br>25,17<br>18,14<br>9,36<br>26,41<br>18,76<br>9,83<br>27,23<br>18,84<br>9,70<br>27,57<br>18,42<br>8,96<br>27,63<br>17,16<br>7,84<br>26,94<br>15,32<br>7,03<br>24,72<br>13,78<br>6,29<br>22,00<br>13,03<br>5,78<br>20,53<br>12,36<br>5,30<br>19,31<br>11,58<br>4,92<br>18,35|

Gráfico 6 - Ciclos diarios promedios de la temperatura - serie pronóstico

Fuente: Envirometrika, 2021.

79 Servicio de Evaluación Ambiental. (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 98 de 112

Tabla 69 - Ciclos diarios de la temperatura - serie observada

|Hora|Promedio de<br>temperatura [°C]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|12,14<br>4,16<br>19,91<br>11,50<br>3,57<br>18,72<br>10,91<br>3,53<br>17,93<br>10,36<br>3,26<br>17,14<br>9,89<br>2,97<br>16,31<br>9,48<br>2,35<br>15,60<br>9,51<br>1,84<br>15,78<br>10,36<br>1,81<br>18,15<br>11,70<br>2,79<br>20,05<br>13,46<br>3,74<br>22,97<br>15,37<br>5,52<br>25,02<br>17,21<br>6,97<br>27,07<br>18,93<br>8,94<br>28,96<br>20,40<br>10,28<br>30,79<br>21,20<br>10,78<br>31,61<br>21,64<br>10,84<br>32,47<br>21,47<br>10,69<br>32,63<br>20,62<br>10,01<br>32,35<br>19,08<br>8,54<br>31,43<br>17,33<br>7,47<br>28,89<br>15,83<br>6,54<br>25,76<br>14,68<br>5,94<br>23,84<br>13,73<br>5,44<br>22,09<br>12,90<br>4,71<br>20,85|12,14<br>4,16<br>19,91<br>11,50<br>3,57<br>18,72<br>10,91<br>3,53<br>17,93<br>10,36<br>3,26<br>17,14<br>9,89<br>2,97<br>16,31<br>9,48<br>2,35<br>15,60<br>9,51<br>1,84<br>15,78<br>10,36<br>1,81<br>18,15<br>11,70<br>2,79<br>20,05<br>13,46<br>3,74<br>22,97<br>15,37<br>5,52<br>25,02<br>17,21<br>6,97<br>27,07<br>18,93<br>8,94<br>28,96<br>20,40<br>10,28<br>30,79<br>21,20<br>10,78<br>31,61<br>21,64<br>10,84<br>32,47<br>21,47<br>10,69<br>32,63<br>20,62<br>10,01<br>32,35<br>19,08<br>8,54<br>31,43<br>17,33<br>7,47<br>28,89<br>15,83<br>6,54<br>25,76<br>14,68<br>5,94<br>23,84<br>13,73<br>5,44<br>22,09<br>12,90<br>4,71<br>20,85|12,14<br>4,16<br>19,91<br>11,50<br>3,57<br>18,72<br>10,91<br>3,53<br>17,93<br>10,36<br>3,26<br>17,14<br>9,89<br>2,97<br>16,31<br>9,48<br>2,35<br>15,60<br>9,51<br>1,84<br>15,78<br>10,36<br>1,81<br>18,15<br>11,70<br>2,79<br>20,05<br>13,46<br>3,74<br>22,97<br>15,37<br>5,52<br>25,02<br>17,21<br>6,97<br>27,07<br>18,93<br>8,94<br>28,96<br>20,40<br>10,28<br>30,79<br>21,20<br>10,78<br>31,61<br>21,64<br>10,84<br>32,47<br>21,47<br>10,69<br>32,63<br>20,62<br>10,01<br>32,35<br>19,08<br>8,54<br>31,43<br>17,33<br>7,47<br>28,89<br>15,83<br>6,54<br>25,76<br>14,68<br>5,94<br>23,84<br>13,73<br>5,44<br>22,09<br>12,90<br>4,71<br>20,85|

Gráfico 7 - Ciclos diarios promedios de la temperatura - serie observada

Fuente: Envirometrika, 2021.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 99 de 112

Velocidad del viento, [m/s]

Se graficaron los ciclos diarios promedios de la velocidad del viento [m/s] para cada serie, junto a los
percentiles 5 y 95, para cada horario analizado.

Tabla 70 - Ciclos diarios promedios serie pronóstico

|Hora|Promedio velocidad<br>del viento [m/s]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|1,14<br>0,21<br>2,69<br>1,11<br>0,14<br>2,88<br>1,13<br>0,16<br>2,97<br>1,17<br>0,12<br>3,29<br>1,15<br>0,08<br>3,18<br>1,12<br>0,14<br>3,16<br>1,09<br>0,09<br>3,12<br>1,15<br>0,09<br>3,22<br>1,37<br>0,07<br>3,66<br>1,51<br>0,08<br>3,92<br>1,61<br>0,14<br>4,16<br>1,64<br>0,18<br>4,21<br>1,72<br>0,18<br>4,29<br>1,84<br>0,22<br>4,33<br>1,92<br>0,28<br>4,40<br>1,99<br>0,29<br>4,43<br>2,02<br>0,39<br>4,24<br>1,86<br>0,22<br>4,28<br>1,56<br>0,10<br>3,92<br>1,41<br>0,19<br>3,48<br>1,30<br>0,21<br>3,16<br>1,28<br>0,23<br>3,09<br>1,23<br>0,22<br>2,82<br>1,16<br>0,17<br>2,89|1,14<br>0,21<br>2,69<br>1,11<br>0,14<br>2,88<br>1,13<br>0,16<br>2,97<br>1,17<br>0,12<br>3,29<br>1,15<br>0,08<br>3,18<br>1,12<br>0,14<br>3,16<br>1,09<br>0,09<br>3,12<br>1,15<br>0,09<br>3,22<br>1,37<br>0,07<br>3,66<br>1,51<br>0,08<br>3,92<br>1,61<br>0,14<br>4,16<br>1,64<br>0,18<br>4,21<br>1,72<br>0,18<br>4,29<br>1,84<br>0,22<br>4,33<br>1,92<br>0,28<br>4,40<br>1,99<br>0,29<br>4,43<br>2,02<br>0,39<br>4,24<br>1,86<br>0,22<br>4,28<br>1,56<br>0,10<br>3,92<br>1,41<br>0,19<br>3,48<br>1,30<br>0,21<br>3,16<br>1,28<br>0,23<br>3,09<br>1,23<br>0,22<br>2,82<br>1,16<br>0,17<br>2,89|1,14<br>0,21<br>2,69<br>1,11<br>0,14<br>2,88<br>1,13<br>0,16<br>2,97<br>1,17<br>0,12<br>3,29<br>1,15<br>0,08<br>3,18<br>1,12<br>0,14<br>3,16<br>1,09<br>0,09<br>3,12<br>1,15<br>0,09<br>3,22<br>1,37<br>0,07<br>3,66<br>1,51<br>0,08<br>3,92<br>1,61<br>0,14<br>4,16<br>1,64<br>0,18<br>4,21<br>1,72<br>0,18<br>4,29<br>1,84<br>0,22<br>4,33<br>1,92<br>0,28<br>4,40<br>1,99<br>0,29<br>4,43<br>2,02<br>0,39<br>4,24<br>1,86<br>0,22<br>4,28<br>1,56<br>0,10<br>3,92<br>1,41<br>0,19<br>3,48<br>1,30<br>0,21<br>3,16<br>1,28<br>0,23<br>3,09<br>1,23<br>0,22<br>2,82<br>1,16<br>0,17<br>2,89|

Gráfico 8 - Ciclos diarios promedios de velocidad del viento - serie pronóstico

Fuente: Envirometrika, 2021.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 100 de 112

Tabla 71 - Ciclos diarios promedios serie observada

|Hora|Promedio velocidad<br>del viento [m/s]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|1,07<br>0,20<br>2,45<br>1,07<br>0,20<br>2,55<br>1,06<br>0,25<br>2,53<br>1,01<br>0,23<br>2,45<br>1,01<br>0,19<br>2,28<br>1,00<br>0,18<br>2,41<br>1,10<br>0,23<br>2,41<br>1,36<br>0,31<br>2,74<br>1,52<br>0,30<br>2,89<br>1,62<br>0,38<br>3,17<br>1,66<br>0,42<br>3,27<br>1,77<br>0,42<br>3,46<br>1,86<br>0,40<br>3,60<br>1,89<br>0,47<br>3,57<br>2,00<br>0,56<br>3,74<br>2,08<br>0,75<br>3,85<br>2,08<br>0,79<br>3,63<br>1,93<br>0,47<br>3,39<br>1,61<br>0,22<br>3,04<br>1,37<br>0,20<br>2,86<br>1,28<br>0,20<br>2,58<br>1,21<br>0,24<br>2,57<br>1,16<br>0,21<br>2,49<br>1,11<br>0,21<br>2,32|1,07<br>0,20<br>2,45<br>1,07<br>0,20<br>2,55<br>1,06<br>0,25<br>2,53<br>1,01<br>0,23<br>2,45<br>1,01<br>0,19<br>2,28<br>1,00<br>0,18<br>2,41<br>1,10<br>0,23<br>2,41<br>1,36<br>0,31<br>2,74<br>1,52<br>0,30<br>2,89<br>1,62<br>0,38<br>3,17<br>1,66<br>0,42<br>3,27<br>1,77<br>0,42<br>3,46<br>1,86<br>0,40<br>3,60<br>1,89<br>0,47<br>3,57<br>2,00<br>0,56<br>3,74<br>2,08<br>0,75<br>3,85<br>2,08<br>0,79<br>3,63<br>1,93<br>0,47<br>3,39<br>1,61<br>0,22<br>3,04<br>1,37<br>0,20<br>2,86<br>1,28<br>0,20<br>2,58<br>1,21<br>0,24<br>2,57<br>1,16<br>0,21<br>2,49<br>1,11<br>0,21<br>2,32|1,07<br>0,20<br>2,45<br>1,07<br>0,20<br>2,55<br>1,06<br>0,25<br>2,53<br>1,01<br>0,23<br>2,45<br>1,01<br>0,19<br>2,28<br>1,00<br>0,18<br>2,41<br>1,10<br>0,23<br>2,41<br>1,36<br>0,31<br>2,74<br>1,52<br>0,30<br>2,89<br>1,62<br>0,38<br>3,17<br>1,66<br>0,42<br>3,27<br>1,77<br>0,42<br>3,46<br>1,86<br>0,40<br>3,60<br>1,89<br>0,47<br>3,57<br>2,00<br>0,56<br>3,74<br>2,08<br>0,75<br>3,85<br>2,08<br>0,79<br>3,63<br>1,93<br>0,47<br>3,39<br>1,61<br>0,22<br>3,04<br>1,37<br>0,20<br>2,86<br>1,28<br>0,20<br>2,58<br>1,21<br>0,24<br>2,57<br>1,16<br>0,21<br>2,49<br>1,11<br>0,21<br>2,32|

Gráfico 9 - Ciclos diarios promedios de velocidad del viento - serie observada

Fuente: Envirometrika, 2021.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 101 de 112

Dirección del viento, [grados]

Se graficó la frecuencia de la dirección del viento en grados, para un año, durante periodos horarios
de 1 hora para las series de pronóstico y observada.

Tabla 72 - Ciclos diarios de dirección del viento serie pronóstico

|Col1|Dirección del viento [grados]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hora<br>del día|0-20|20-40|40-60|60-80|80-100|100-120|120-140|140-160|160-180|180-200|200-220|220-240|240-260|260-280|280-300|300-320|320-340|340-360|
|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8|
|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16|
|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9|

Gráfico 10 - Ciclos diarios de dirección del viento - serie pronóstico

Fuente: Envirometrika, 2021.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 102 de 112

Tabla 73 - Ciclos diarios de dirección del viento serie observada

|Col1|Dirección del viento [grados]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hora<br>Del día|0-20|20-40|40-60|60-80|80-100|100-120|120-140|140-160|160-180|180-200|200-220|220-240|240-260|260-280|280-300|300-320|320-340|340-360|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10|
|07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11|
|15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9|

Gráfico 11 - Ciclos diarios de dirección del viento - serie observada

Fuente: Envirometrika, 2021.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 103 de 112

Vientos calmos, < 0,5 [m/s]

La condición de calma o cuasi-calma (velocidades de viento menores a 0,5 [m/s] [80] ), es de especial
interés en calidad del aire, pues son las condiciones en que el movimiento del aire es casi nulo
(estancamiento). Lo anterior puede ser crítico para fuentes emisoras a nivel de superficie, ya que
puede: Condicionar la acumulación de contaminantes en su lugar de origen, incrementar en la
concentración en el tiempo o que las masas de aire no se renueven en forma efectiva y recirculen [81] .
La información a continuación indica el período del día y del año en que se presenta el mayor porcentaje
de vientos calmos, según la serie de pronóstico y observada.

Tabla 74 - Frecuencia mensual de vientos calmos - serie pronóstico

Nota: Sumatoria de horas/mes de vientos calmos.

|Mes|Frecuencia de<br>vientos calmos|N°<br>días|%|
|---|---|---|---|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|148<br>133<br>136<br>162<br>167<br>154<br>130<br>140<br>106<br>117<br>68<br>117|744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744|20%<br>20%<br>18%<br>23%<br>22%<br>21%<br>17%<br>19%<br>15%<br>16%<br>9%<br>16%|

Fuente: Envirometrika, 2021.

Tabla 75 - Frecuencia horaria de vientos calmos - serie pronóstico

|Hora|Frecuencia de<br>vientos calmos|%|
|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|76<br>84<br>78<br>90<br>80<br>84<br>84<br>106<br>96<br>84<br>72<br>62<br>55<br>46<br>32<br>35<br>26<br>36<br>60<br>61<br>50<br>52<br>61<br>68|21%<br>23%<br>21%<br>25%<br>22%<br>23%<br>23%<br>29%<br>26%<br>23%<br>20%<br>17%<br>15%<br>13%<br>9%<br>10%<br>7%<br>10%<br>16%<br>17%<br>14%<br>14%<br>17%<br>19%|

Fuente: Envirometrika, 2021.

Nota: Sumatoria de horas/año de vientos calmos.

80 Barclay, J. Scire, J. (2011). Generic Guidance and Optimum Model Settings for the CALPUFF Modeling System for Inclusion into the Approved

Methods for the Modeling and Assessments of Air Pollutants in NSW, Australia. TRC Environmental Corporation.
81 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 104 de 112

Tabla 76 - Frecuencia mensual de vientos calmos - serie observada

|Mes|Frecuencia de<br>vientos calmos|N°<br>días|%|
|---|---|---|---|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|36<br>37<br>79<br>156<br>97<br>112<br>120<br>112<br>75<br>68<br>27<br>14|744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744|5%<br>6%<br>11%<br>22%<br>13%<br>16%<br>16%<br>15%<br>10%<br>9%<br>4%<br>2%|

Fuente: Envirometrika, 2021.

Nota: Sumatoria de horas/mes de vientos calmos.

Tabla 77 - Frecuencia horaria de vientos calmos - serie observada

Nota: Sumatoria de horas/año de vientos calmos.

|Hora|Frecuencia de<br>vientos calmos|%|
|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|25<br>28<br>42<br>46<br>50<br>40<br>51<br>74<br>53<br>51<br>26<br>23<br>16<br>7 <br>8 <br>8 <br>6 <br>9 <br>13<br>15<br>19<br>20<br>26<br>21|7 <br>8 <br>12<br>13<br>14<br>11<br>14<br>20<br>15<br>14<br>7 <br>6 <br>4 <br>2 <br>2 <br>2 <br>2 <br>2 <br>4 <br>4 <br>5 <br>5 <br>7 <br>6|

Fuente: Envirometrika, 2021.

Del análisis cualitativo de la frecuencia de vientos calmos, arrojó que la serie pronóstico sobrestima a
lo observado. En relación con la frecuencia mensual y horaria de vientos calmos, la condición de
sobrestimación se observó durante todo el periodo anual en mayor medida durante la temporada
estival, y dentro del ciclo diario en el horario AM. Por lo tanto, la meteorología de pronóstico permitiría
representar aquellas condiciones más desfavorables de dispersión de las emisiones, debido a la mayor
frecuencia de vientos calmos (estancamiento de las emisiones) y de vientos de baja intensidad (menor
dilución de las emisiones).

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 105 de 112

**13.3** **Comparación entre pronóstico y observaciones**

La comparación de las observaciones (serie de datos obtenida de registros de la estación meteorológica
superficial) con las simulaciones del modelo de pronóstico (serie de datos obtenida del modelo numérico
WRF) en el punto de medición, permite evaluar la incertidumbre de los datos meteorológicos tridimensionales
generados y de los resultados del modelo de dispersión y así poder analizar una posible sobre o
subestimación [82] . Para poder determinar un grado de incertidumbre, se deben evaluar las diferencias de lo
observado versus lo modelado realizando un análisis cuantitativo y cualitativo, según se recomienda en la
guía de modelación [83] .

**Análisis cualitativo de serie de pronóstico y observada**

El análisis cualitativo se determinó en base a la comparación de la serie de pronóstico versus la
observada, mediante gráficos de ciclos diarios promedios para las variables de temperatura, velocidad
y dirección del viento.

Temperatura, [°C]

Gráfico 12 - Ciclos diarios promedios de temperatura, serie pronóstico y observado.

Fuente: Envirometrika, 2021.

82 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.
83 Ibíd.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 106 de 112

Velocidad del viento, [m/s]

Gráfico 13 - Ciclos diarios promedios de velocidad del viento, serie pronóstico y observada

Fuente: Envirometrika, 2021.

Gráfico 14 - Distribución anual de frecuencia de velocidad del viento serie pronóstico y observada.

WRF-MMIF, 2019 Estación U.C. del Maule, 2019

En términos generales, ambas series presentan una distribución asimétrica positiva para el periodo
anual analizado. La serie de pronóstico presentaría una mayor frecuencia de vientos de baja intensidad
respecto a la serie observada, además la serie observada presenta menor frecuencia de vientos de
mayor velocidad que la serie pronóstico. Del análisis de la distribución de datos, se observó que la
serie pronóstico sobrestima la frecuencia de vientos calmos [84] en un 7,36% respecto a la serie
observada.

84 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A - Claves alfanuméricas - Escala

Beaufort de Viento. OMM-N°306. OMM. Suiza.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 107 de 112

Dirección del viento, [grados]

Gráfico 15 - Ciclos diarios de variación del viento, serie pronóstico

Fuente: Envirometrika, 2021.

Gráfico 16 - Ciclos diarios de variación del viento, serie observada

Fuente: Envirometrika, 2021.

Al comparar ambas gráficas, se observa que la serie de pronóstico reproduce de forma coherente la
serie observada. Con una mayor frecuencia de vientos en el rango de dirección 180-220 [grados] (SSO).
En relación a la distribución de frecuencia horaria, la serie de pronóstico representaría los rangos donde
ocurriría la mayor frecuencia de los datos observados.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 108 de 112

Gráfico 17 - Rosas de viento anual por periodo horario, serie pronóstico y observada

Meteorología pronóstico Meteorología observada

|Col1|Col2|Anual Nocturno|Anual AM|Anual PM|
|---|---|---|---|---|
|Pronóstico|||||
|Observado|||||

Fuente: Envirometrika, 2021.

Del análisis anual de las rosas de viento, arrojó lo siguiente:

La serie pronóstico presentó una distribución de dirección de los vientos, coherente a los descrito

por la serie observada, tanto de los vientos predominantes como de los rangos de menor frecuencia.
En relación a la intensidad de los vientos pronosticados, aquellos de menor intensidad superan lo
registrado por la estación meteorológica para el periodo anual 2019, lo que representaría el
escenario más desfavorable de dispersión de las emisiones de la planta.

En cuanto al análisis horario, se tiene que:

En cuanto al horario nocturno, la frecuencia de vientos de la serie pronostico reproduce de forma

coherente la frecuencia de la serie observada.

En el horario AM, la serie pronostico sobrestimaría la frecuencia de vientos provenientes desde los

rangos SSO, respecto descrito en la serie observada. En cuanto a la intensidad de vientos, la serie

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 109 de 112

pronostico presentaría condiciones más desfavorables de dispersión que las observadas en Estación
U.C del Maule.

 Por otra parte en el horario PM, se aprecia distribución de frecuencia de vientos coherente entre

ambas series, con cierto grado sobrestimación de los vientos provenientes desde el SSO. En cuanto
a la intensidad de los vientos la serie de pronóstico presentaría una mayor frecuencia de vientos de
baja intensidad, lo cual propiciaría un menor grado de dilución de las emisiones debido a la mayor
ocurrencia de condiciones de estancamiento.

Gráfico 18 - Rosas de viento anual por periodo estacional, serie pronóstico y observada.

|Col1|Verano|Otoño|Invierno|Primavera|
|---|---|---|---|---|
|Pronóstico|||||
|Observado|||||

Fuente: Envirometrika, 2021.

Del análisis estacional de distribución de vientos en Estación U.C del Maule, se tiene que:
Lo pronosticado presentaría un comportamiento coherente a lo descrito por la estación observada en
los 4 periodos estacionales analizados. Sin embargo, se aprecia una leve sobrestimación de la
intensidad de los viento en el periodo anual, principalmente desde la dirección SSO. A pesar de lo
anterior la frecuencia de vientos de baja intensidad (para el análisis se consideraron aquellas entre 0,5
y 3 [m/s]) es mayor en la serie pronóstico, lo que permitiría alcanzar un mayor grado de
representatividad de condiciones desfavorables de dispersión de las emisiones.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 110 de 112

**Análisis cuantitativo de serie de pronóstico y observada**

El análisis cuantitativo se realizó en base a una metodología celda-punto, el cual comparó los datos de
la meteorología de pronóstico con los registrados por la estación superficial, de cada dato horario. Se
calcularon las métricas de estadísticas de error medio cuadrático (RSME), sesgo (BIAS), coeficiente de
correlación, índice de concordancia (IOA), entre las variables meteorológicas pronosticadas y
observadas.

Tabla 78 - Error medio cuadrático, sesgo, coeficiente de correlación, IOA, velocidad del viento y temperatura

|Estadístico|Descripción|Fórmula|Resultado|Col5|
|---|---|---|---|---|
|Estadístico|Descripción|Fórmula|Velocidad del<br>viento [m/s]|Temperatura<br>[°C]|
|RMSE|Error medio cuadrático (Root mean<br>square Error), nos indica la medida de<br>las diferencias en promedio entre<br>valores pronosticados y observados||0,85|3,24|
|NRMSD|Error medio cuadrático normalizado<br>(Normalized<br>Root<br>mean<br>square<br>deviation) señala la varianza residual<br>entre los valores pronosticados y<br>observados||0,18|0,09|
|NMAE|Error medio absoluto normalizado,<br>toma en cuenta el peso del error<br>respecto al valor de la variable medida,<br>normaliza el error absoluto||0,14|0,07|
|BIAS|Sesgo, proporciona información sobre<br>la tendencia del modelo a sobrestimar<br>o subestimar una variable||0,02|-1,93|
|Coeficiente de<br>correlación de<br>Pearson|Un índice que mide el grado de relación<br>de dos variables siempre y cuando<br>ambas sean cuantitativas.||0,67|0,94|
|IOA|El IOA (Index Of Agreement) acuerdo<br>es una medida de la coincidencia<br>entre la salida de cada predicción de<br>la media observada y la salida de cada<br>observación de la media observada.||0,79|1,00|

Los índices RMSE, NRMSD y NMAE, arrojaron que las variables de velocidad del viento y la temperatura
pronosticadas presentarían una diferencia promedio de 0,85 [m/s] y 3,24 [°C], respecto a lo observado
para el periodo anual.

Los estadísticos de Sesgo (BIAS) indicarían la meteorología del modelo de pronóstico WRF-MMIF,
sobrestima en promedio la velocidad del viento en 0,02 [m/s] y subestima la temperatura en 1,93 [°C].

La correlación arrojó asociación positiva media para velocidad del viento y Correlación positiva
considerable para la variable de temperatura [85] [/] [86] .

El IOA exhibió un nivel de 0,79 categorizado como acuerdo para velocidad del viento. La temperatura
arrojó acuerdo perfecto con un valor de 1. Ambas variables se encuentran dentro de los rangos
aceptables según puntos de referencias Emery et al. (2001), correspondientes a 0,6 y 0,8
respectivamente.

85 Correlación positiva débil=+0,10, Correlación positiva media=+0,50, Correlación positiva considerable=+0,75.
86 Castejón Sandoval, O. (2011). Diseño y Análisis de Experimentos con Statistix. Universidad Rafael Urdaneta, Fondo editorial biblioteca.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 111 de 112

**13.4** **ANÁLISIS DE RESULTADOS**

Del análisis de incertidumbre, se concluye que:

 Del levantamiento meteorológico realizado, la estación meteorológica U. C. del Maule, cumplió con los

requerimientos señaladas en la Guía del SEA [87], para la realización del análisis.

 Del análisis cualitativo y comparativo de las series, se desprende que la serie pronostico anual presentaría

de forma coherente la distribución de frecuencia de vientos de la serie observada. En relación a la intensidad
de los vientos, la serie de pronóstico sobrestimaría la frecuencia de vientos de baja intensidad. Por lo tanto
el modelo meteorológico sería representativo de las condiciones más desfavorables de dispersión (vientos
calmos y estancamiento de emisiones), describiendo un 7,4% de vientos calmos por sobre lo registrado en
la estación analizada.

 En cuanto al análisis de temperatura, la serie pronostico reproduciría la serie observada de los ciclos diarios

promedios de la estación U.C. del Maule.

 Del análisis de los estadísticos de incertidumbre se obtiene que la meteorología de pronóstico estaría dentro

de los rangos aceptables acordados por las distintas agencias ambientales internacionales. De acuerdo a lo
anterior, la meteorología aplicada sobrestimaría las condiciones más desfavorables de dispersión
permitiendo evaluar los niveles de concentración en los receptores bajo el escenario más crítico respecto a
las emisiones del proyecto.

87 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6343- Modelación de Impacto Odorante Marzo 2021
ECOMAULE S.A. - Centro de Tratamiento de Residuos Página 112 de 112

**13.5** **BIBLIOGRAFÍA ANEXOS**

 Barclay, J. Scire, J. (2011). Generic Guidance and Optimum Model Settings for the CALPUFF Modeling

System for Inclusion into the Approved Methods for the Modeling and Assessments of Air Pollutants in
NSW, Australia. TRC Environmental Corporation.

 Bidlingmaier, W., et al. (2007). Compost Science and Technology: Chap.11: Odor Emissions from

Composting Plants. Waste Management Series, Vol.8.

 Brashers, B., Emery, C. (2014). Draft User’s Manual: The Mesoscale Model Interface Program (MMIF),

Version 3.1. U.S. Environmental Protection Agency.

 Castejón Sandoval, O. (2011). Diseño y Análisis de Experimentos con Statistix. Universidad Rafael


Department of Water and Environmental Regulation. (2019). Guideline: Odour Emissions. Govermment of

Western Australia. Australia.

 Environmental Protection Agency. (2000). Meteorological Monitoring Guidance for Regulatory Modeling

Applications. Office of Air and Radiation. Office of Air Quality Planning and Standards Research Triangle
Park, NC 27711.

 Gobierno Regional del Maule. (2015). Atlas Territorial Región del Maule. Programa Gestión Territorial para

Zonas Rezagadas. Gobierno de Chile.

 Invennto, (2017). P5052: Evaluación Olfatometría Dinámica - Muestras Gaseosas. Envirometrika. Chile.

 - Manitoba Livestock Manure Management Initiative Inc. (2002). Odour Production, Evaluation and Control.

University of Manitoba. Canadá.

 Ministerio del Medio Ambiente (2018). Sistema de Información Nacional de Calidad del Aire (SINCA).

Adquirido 05 febrero de 2021:https://sinca.mma.gob.cl/index.php/estacion/index/key/710

 Ministerio de Agricultura (2020). Red Agrometeorológica Nacional (AGROMET). Adquirido 05 febrero de

2021: https://www.agromet.cl/datos-historicos

 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A

- Claves alfanuméricas - Escala Beaufort de Viento. OMM-N°306. OMM. Suiza.

 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA.

Santiago, Chile.

 Suffet, I., H., et al., (2009). Sensory Assessment and Characterization of Odor Nuisance Emissions during

the Composting of Wastewater Biosolids. Water Environment Research, Vol. 81, No. 7.

 Scire, J., Strimaitis, D., Yamartino, R. (2000). A User's Guide for the Calpuff Dispersion Model. Earth Tech,

Inc.

 World Meteorological Organization (2010). Guide to Meteorological Instruments and Methods of

Observation-WMO-No. 8, Geneva, Switzerland.

ANEXO 6 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: - Fuentes odorantes Situación actual**

| Área | Nombre fuente | Emisión<br>de Olor<br>[ouE/m2s] | Tasa de<br>Emisión de<br>Olor<br>[ouE/s] |
| --- | --- | --- | --- |
| Compostaje | Pila Lodo Agroindustrial - Edad 1<br>Pila Lodo Agroindustrial - Edad 2<br>Pila Lodo Agroindustrial - Edad 3<br>Pila lodo sanitario - Edad 1 Curicó<br>Pila lodo sanitario - Edad 1 Otras Loc.<br>Pila lodo sanitario - Edad 2 Curicó<br>Pila lodo sanitario - Edad 2 Otras Loc.<br>Pila lodo sanitario - Edad 3 Curicó<br>Pila lodo sanitario - Edad 3 Otras Loc. | 14,7<br>8,3<br>1,6<br>5,7<br>3,8<br>11,4<br>5,9<br>5,6<br>1,7 | 181.530,30<br>61.876,50<br>3.840,00<br>45.446,10<br>90.892,20<br>72.982,80<br>113.315,40<br>6.493,20<br>5.913,45 |
| PTRILes | Laguna de percolados | 81,6 | 81.600,00 |
| PTRILes | Laguna de agua rechazo | 81,6 | 12.566,40 |
| PTRILes | Reactor aerobio 1 | 31,8 | 2.497,57 |
| PTRILes | Reactor aerobio 2 | 31,8 | 2.497,57 |
| PTRILes | Clarificador | 14,2 | 343,64 |
| PTRILes | Floculador | 14,2 | 100,37 |
| PTRILes | Laguna lodos biológicos | 21,2 | 1.433,12 |
| PTRILes | Laguna lodo físico/químico | 2,3 | 140,76 |
| PTRILes | Lechos de secado 1 | 4,2 | 1.268,40 |
| PTRILes | Lechos de secado 2 (lav. de camiones) | 32,8 | 8.757,60 |
| PTRILes | Laguna agua tratada | 2,4 | 904,80 |
| Rell.<br>San. | Monorelleno - Frente de trabajo | 11,1 | 50.038,80 |
| Rell.<br>San. | Relleno Sanitario - Frente de trabajo | 21,3 | 18.105,00 |

**Tabla 4: - Escenario operacional para modelación**

| Área | Nombre fuente | Emisión<br>de Olor<br>[ouE/m2s] | Tasa de<br>Emisión de<br>Olor<br>[ouE/s] |
| --- | --- | --- | --- |
|  | Galpón de recepción (Sist. de abatim.1) | 47,23 | 53,42 |
|  | Galpón de recepción (Sist. de abatim.2) | 47,23 | 53,42 |
|  | Unidad de almacenamiento de digestato | 0,32 | 1.705,28 |

**Tabla 3: - Fuentes odorantes Situación futura (Cont.)**

| Área | Nombre fuente | Emisión de<br>Olor<br>[ouE/m2s] | Tasa de<br>Emisión de<br>Olor<br>[ouE/s] |
| --- | --- | --- | --- |
| PTRILes | Laguna anaeróbica | 5,71 | 11.424,00 |
| PTRILes | Laguna de percolados | 5,71 | 5.710,00 |
| PTRILes | Reactor aerobio 1 | 19,08 | 1.498,54 |
| PTRILes | Reactor aerobio 2<br> | 19,08<br> | 1.498,54<br> |
| PTRILes | Reactor aerobio 3 | 19,08 | 1.498,54 |
| PTRILes | Reactor aerobio 4 | 19,08 | 1.498,54 |
| PTRILes | Clarificador | 8,52 | 206,18 |
| PTRILes | Floculador | 8,52 | 60,22 |
| PTRILes | Laguna lodos biológicos | 21,20 | 1.433,12 |
| PTRILes | Laguna lodo físico/químico | 2,30 | 140,76 |
| PTRILes | Laguna agua tratada | 0,25 | 94,25 |
| Relleno | Alvéolo 7 - Frente de trabajo | 21,30 | 18.105,00 |
| Riego | Zona de riego 1 | 0,32 | 4.217,60 |
| Riego | Zona de riego 2 | 0,32 | 5.729,96 |

**Tabla 6: - TEO y alcance odorante**

| Escenario<br>Operacional | TEO<br>[ouE/s] | Alcance [ha]\a | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| Escenario<br>Operacional | TEO<br>[ouE/s] | 1<br>[ouE/m3] | 3<br>[ouE/m3] | 4<br>[ouE/m3] | 5<br>[ouE/m3] |
| E1: Sit. actual<br>E2: Sit. futura | 762.544<br>75.033 | 8.204<br>454 | 2.774<br>218 | 2.118<br>175 | 1.715<br>144 |

**Tabla 7: - Evaluación de molestia en receptores a los que**

| Receptor | Percepción de olor<br>sobre 3 [ou/m3]<br>E | Cantidad de horas<br>de exposición de<br>olor ≥ 3 [ou E/m3] | Molestia |
| --- | --- | --- | --- |
| R2 | No | 0 | No |
| R3 | No | 0 | No |
| R4 | No | 0 | No |
| R6 | No | 0 | No |
| R7 | No | 0 | No |
| R8 | No | 0 | No |
| R9 | No | 0 | No |
| R10 | No | 0 | No |
| R11 | No | 0 | No |
| R12 | No | 0 | No |

**Tabla 8: - Evaluación de molestia en receptores a los que**

| Receptor | Percepción de olor<br>sobre 4 [ou/m3]<br>E | Cantidad de horas<br>de exposición de<br>olor ≥ 4 [ou E/m3] | Molestia |
| --- | --- | --- | --- |
| R5 | No | 0 | No |

**Tabla 9: - Evaluación de molestia en receptores a los que**

| Receptor | Percepción de olor<br>sobre 5 [ou/m3]<br>E | Cantidad de horas<br>de exposición de<br>olor ≥ 5 [ou E/m3] | Molestia |
| --- | --- | --- | --- |
| R1 | No | 0 | No |

**Tabla 10: - Coordenadas referenciales de localización del Proyecto**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| X: Este | Y: Sur | Huso | Datum |
| 282.341 | 6.101.435 | 19 H | WGS 84 |

**Tabla 11: - Fuentes odorantes - Situación actual**

| ID | Área | Nombre fuente | Tipo de<br>fuente | Coordenadas UTM [m]<br>WGS84 19K | Col6 |
| --- | --- | --- | --- | --- | --- |
| ID | Área | Nombre fuente | Tipo de<br>fuente | Este | Norte |
| 1 | Compostaje | Pila Lodo Agroindustrial - Edad 1 | Difusa | 282.608 | 6.101.746 |
| 2 | 2 | Pila Lodo Agroindustrial - Edad 1 | Difusa | 282.477 | 6.101.593 |
| 3 | 3 | Pila Lodo Agroindustrial - Edad 2 | Difusa | 282.491 | 6.101.572 |
| 4 | 4 | Pila Lodo Agroindustrial - Edad 3a | Difusa | 282.599 | 6.101.756 |
| 5 | 5 | Pila Lodo Agroindustrial - Edad 3b | Difusa | 282.671 | 6.101.810 |
| 6 | 6 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 282.791 | 6.101.622 |
| 7 | 7 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 282.815 | 6.101.660 |
| 8 | 8 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 282.743 | 6.101.660 |
| 9 | 9 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 282.771 | 6.101.696 |
| 10 | 10 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 282.712 | 6.101.692 |
| 11 | 11 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 282.740 | 6.101.731 |
| 12 | 12 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 282.682 | 6.101.715 |
| 13 | 13 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 282.705 | 6.101.743 |
| 14 | 14 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 282.669 | 6.101.464 |
| 15 | 15 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 282.669 | 6.101.464 |
| 16 | 16 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 282.712 | 6.101.566 |
| 17 | 17 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 282.644 | 6.101.488 |
| 18 | 18 | Pila lodo sanitario - Edad 3 Curicó | Difusa | 282.567 | 6.101.489 |
| 19 | 19 | Pila lodo sanitario - Edad 3 Otras Localidades | Difusa | 282.587 | 6.101.467 |
| 20 | 20 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 282.587 | 6.101.503 |
| 21 | 21 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 282.606 | 6.101.483 |
| 22 | 22 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 282.594 | 6.101.512 |
| 23 | 23 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 282.614 | 6.101.491 |
| 24 | 24 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 282.637 | 6.101.675 |
| 25 | 25 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 282.556 | 6.101.580 |
| 26 | 26 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 282.671 | 6.101.601 |
| 27 | 27 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 282.603 | 6.101.521 |
| 28 | 28 | Pila lodo sanitario - Edad 3 Curicó | Difusa | 282.759 | 6.101.572 |
| 29 | 29 | Pila lodo sanitario - Edad 3 Otras Localidades | Difusa | 282.766 | 6.101.566 |
| 30 | PTRILes | Laguna de percolados | Difusa | 282.122 | 6.101.571 |
| 31 | 31 | Laguna de agua rechazo | Difusa | 282.194 | 6.101.668 |
| 32 | 32 | Reactor aerobio 1 | Difusa | 282.183 | 6.101.641 |
| 33 | 33 | Reactor aerobio 2 | Difusa | 282.191 | 6.101.631 |
| 34 | 34 | Clarificador | Difusa | 282.199 | 6.101.628 |
| 35 | 35 | Floculador | Difusa | 282.206 | 6.101.636 |
| 36 | 36 | Laguna lodos biológicos | Difusa | 282.186 | 6.101.657 |
| 37 | 37 | Laguna lodo físico/químico | Difusa | 282.182 | 6.101.652 |
| 38 | 38 | Lechos de secado 1 | Difusa | 282.212 | 6.101.589 |
| 39 | 39 | Lechos de secado 2 (lavado de camiones) | Difusa | 282.200 | 6.101.596 |
| 40 | 40 | Laguna agua tratada | Difusa | 282.165 | 6.101.663 |
| 41 | Relleno | Monorelleno - Frente de trabajo | Difusa | 282.277 | 6.101.239 |
| 42 | 42 | Relleno Sanitario - Frente de trabajo | Difusa | 282.314 | 6.101.479 |

**Tabla 12: - Fuentes odorantes - Situación futura**

| ID | Área | Nombre fuente | Tipo de<br>fuente | Coordenadas UTM [m]<br>WGS84 19K | Col6 |
| --- | --- | --- | --- | --- | --- |
| ID | Área | Nombre fuente | Tipo de<br>fuente | Este | Norte |
| 1 | Compostaje | Cancha de compostaje 1 | Difusa | 282.627 | 6.101.766 |
| 2 | 2 | Cancha de compostaje 2 | Difusa | 282.745 | 6.101.658 |
| 3 | 3 | Cancha de compostaje 3 | Difusa | 282.770 | 6.101.646 |
| 4 | 4 | Cancha de compostaje 4 | Difusa | 282.623 | 6.101.534 |
| 5 | 5 | Galpón de compostaje 1 (sist. de abatimiento) | Puntual | 282.579 | 6.101.700 |
| 6 | 6 | Galpón de compostaje 2 (sist. de abatimiento) | Puntual | 282.591 | 6.101.720 |
| 7 | 7 | Galpón de compostaje 3 (sist. de abatimiento) | Puntual | 282.609 | 6.101.736 |
| 8 | 8 | Galpón de compostaje 4 (sist. de abatimiento) | Puntual | 282.623 | 6.101.755 |
| 9 | Digestión | Estanque acumulación clarificado - Etapa 1 | Difusa | 282.607 | 6.101.593 |
| 10 | 10 | Estanque acumulación de digestato - Etapa 1 | Difusa | 282.614 | 6.101.585 |
| 11 | 11 | Contenedor deshidratado mecánico - Etapa 1 | Difusa | 282.610 | 6.101.606 |
| 12 | 12 | Estanque acumulación clarificado - Etapa 2 | Difusa | 282.655 | 6.101.641 |
| 13 | 13 | Contenedor deshidratado mecánico - Etapa 2 | Difusa | 282.615 | 6.101.613 |
| 14 | 14 | Galpón de recepción (Sist. de abatimiento olores - Etapa 1) | Puntual | 282.610 | 6.101.579 |
| 15 | 15 | Galpón de recepción (Sist. de abatimiento olores - Etapa 2) | Puntual | 282.651 | 6.101.629 |
| 16 | 16 | Unidad de almacenamiento de digestato | Difusa | 282.569 | 6.101.487 |
| 17 | PTRILes | Laguna anaeróbica | Difusa | 282.130 | 6.101.544 |
| 18 | 18 | Laguna de percolados | Difusa | 282.122 | 6.101.571 |
| 19 | 19 | Reactor aerobio 1 | Difusa | 282.183 | 6.101.640 |
| 20 | 20 | Reactor aerobio 2 | Difusa | 282.191 | 6.101.631 |
| 21 | 21 | Reactor aerobio 3 | Difusa | 282.175 | 6.101.629 |
| 22 | 22 | Reactor aerobio 4 | Difusa | 282.168 | 6.101.618 |
| 23 | 23 | Clarificador | Difusa | 282.198 | 6.101.627 |
| 24 | 24 | Floculador | Difusa | 282.206 | 6.101.635 |
| 25 | 25 | Laguna lodos biológicos | Difusa | 282.186 | 6.101.657 |
| 26 | 26 | Laguna lodo físico/químico | Difusa | 282.182 | 6.101.652 |
| 27 | 27 | Laguna agua tratada | Difusa | 282.165 | 6.101.662 |
| 28 | Relleno | Alvéolo 7 - Frente de trabajo | Difusa | 282.290 | 6.101.242 |
| 29 | Riego | Zona de riego 1 | Difusa | 281.821 | 6.101.645 |
| 30 | 30 | Zona de riego 2 | Difusa | 282.053 | 6.101.591 |

**Tabla 13: - Proyecto de referencia aplicable**

| Proyecto | Tipo de<br>estudio | Establecimiento | Año de<br>ejecución | Norma<br>aplicada al<br>muestreo | Norma<br>aplicada al<br>análisis<br>olfatométrico | Referencia aplicada en |
| --- | --- | --- | --- | --- | --- | --- |
| P5838 | EO | Centro de Manejo<br>de Residuos<br>Ecomaule | 2019 | NCh3386:2015<br>VDI<br>4285:2011 - | NCh3190:2010 | Fuentes de emisión |
| P5052 | EO | Invennto | 2017 | /a | NCh3190:2010 | Cobertura flotante |
| EC-VLT-<br>FB20 | Ficha<br>Técnica | Ecozone | 2020 | /b | - | Abatimiento galpón de<br>compostaje y recepción |

**Tabla 14: - Emisiones de referencia aplicados en Situación actual**

| ID | Área | Fuente | EO por sup. [ou/m2s]/a<br>E | Tasa de Emisión de Olor<br>[ou/s]/b<br>E |
| --- | --- | --- | --- | --- |
| 1 | Compostaje | Pila Lodo Agroindustrial - Edad 1 | 14,7 | 96.402,60 |
| 2 | 2 | Pila Lodo Agroindustrial - Edad 1 | 14,7 | 85.127,70 |
| 3 | 3 | Pila Lodo Agroindustrial - Edad 2 | 8,3 | 61.876,50 |
| 4 | 4 | Pila Lodo Agroindustrial - Edad 3a | 1,6 | 1.920,00 |
| 5 | 5 | Pila Lodo Agroindustrial - Edad 3b | 1,6 | 1.920,00 |
| 6 | 6 | Pila lodo sanitario - Edad 1 Curicó | 5,7 | 19.704,90 |
| 7 | 7 | Pila lodo sanitario - Edad 1 Otras Localidades | 3,8 | 39.409,80 |
| 8 | 8 | Pila lodo sanitario - Edad 2 Curicó | 11,4 | 23.697,75 |
| 9 | 9 | Pila lodo sanitario - Edad 2 Otras Localidades | 5,9 | 36.793,88 |
| 10 | 10 | Pila lodo sanitario - Edad 1 Curicó | 5,7 | 6.421,05 |
| 11 | 11 | Pila lodo sanitario - Edad 1 Otras Localidades | 3,8 | 12.842,10 |
| 12 | 12 | Pila lodo sanitario - Edad 2 Curicó | 11,4 | 11.060,85 |
| 13 | 13 | Pila lodo sanitario - Edad 2 Otras Localidades | 5,9 | 17.173,43 |
| 14 | 14 | Pila lodo sanitario - Edad 1 Curicó | 5,7 | 6.059,10 |
| 15 | 15 | Pila lodo sanitario - Edad 1 Otras Localidades | 3,8 | 12.118,20 |
| 16 | 16 | Pila lodo sanitario - Edad 2 Curicó | 11,4 | 13.913,70 |
| 17 | 17 | Pila lodo sanitario - Edad 2 Otras Localidades | 5,9 | 21.602,85 |
| 18 | 18 | Pila lodo sanitario - Edad 3 Curicó | 5,6 | 3.579,80 |
| 19 | 19 | Pila lodo sanitario - Edad 3 Otras Localidades | 1,7 | 3.260,18 |
| 20 | 20 | Pila lodo sanitario - Edad 1 Curicó | 5,7 | 1.913,78 |
| 21 | 21 | Pila lodo sanitario - Edad 1 Otras Localidades | 3,8 | 3.827,55 |
| 22 | 22 | Pila lodo sanitario - Edad 2 Curicó | 11,4 | 4.312,05 |
| 23 | 23 | Pila lodo sanitario - Edad 2 Otras Localidades | 5,9 | 6.695,03 |
| 24 | 24 | Pila lodo sanitario - Edad 1 Curicó | 5,7 | 11.347,28 |
| 25 | 25 | Pila lodo sanitario - Edad 1 Otras Localidades | 3,8 | 22.694,55 |
| 26 | 26 | Pila lodo sanitario - Edad 2 Curicó | 11,4 | 19.998,45 |
| 27 | 27 | Pila lodo sanitario - Edad 2 Otras Localidades | 5,9 | 31.050,23 |
| 28 | 28 | Pila lodo sanitario - Edad 3 Curicó | 5,6 | 2.913,40 |
| 29 | 29 | Pila lodo sanitario - Edad 3 Otras Localidades | 1,7 | 2.653,28 |
| 30 | PTRILes | Laguna de percolados | 81,6 | 81.600,00 |
| 31 | 31 | Laguna de agua rechazo | 81,6 | 12.566,40 |
| 32 | 32 | Reactor aerobio 1 | 31,8 | 2.497,57 |
| 33 | 33 | Reactor aerobio 2 | 31,8 | 2.497,57 |
| 34 | 34 | Clarificador | 14,2 | 343,64 |
| 35 | 35 | Floculador | 14,2 | 100,37 |
| 36 | 36 | Laguna lodos biológicos | 21,2 | 1.433,12 |
| 37 | 37 | Laguna lodo físico/químico | 2,3 | 140,76 |
| 38 | 38 | Lechos de secado 1 | 4,2 | 1.268,40 |
| 39 | 39 | Lechos de secado 2 (lavado de camiones) | 32,8 | 8.757,60 |
| 40 | 40 | Laguna agua tratada | 2,4 | 904,8 |
| 41 | Relleno Sanitario | Monorelleno - Frente de trabajo | 11,1 | 50.038,80 |
| 42 | 42 | Relleno Sanitario - Frente de trabajo | 21,3 | 18.105,00 |

**Tabla 15: - Emisiones de referencia aplicados en la Situación futura**

| ID | Área | Fuente | EO por sup. [ou/m2s]/a<br>E | Tasa de Emisión de<br>Olor [ou/s]/b<br>E |
| --- | --- | --- | --- | --- |
| 1 | Compostaje | Cancha de compostaje 1 | 0,53/c | 5.283,75 |
| 2 | 2 | Cancha de compostaje 2 | 0,53/c | 2.610,30 |
| 3 | 3 | Cancha de compostaje 3 | 0,53/c | 7.441,46 |
| 4 | 4 | Cancha de compostaje 4 | 0,53/c | 8.420,32 |
| 5 | 5 | Galpón de compostaje 1 (sist. de abatimiento) | 1.128,86 | 1.276,71/d |
| 6 | 6 | Galpón de compostaje. 2 (sist. de abatimiento) | 1.438,43 | 1.626,82/d |
| 7 | 7 | Galpón de compostaje 3 (sist. de abatimiento) | 1.438,43 | 1.626,82/d |
| 8 | 8 | Galpón de compostaje 4 (sist. de abatimiento) | 1.438,43 | 1.626,82/d |
| 9 | Digestión | Estanque de acumulación clarificado - Etapa 1 | 0,32/e | 64,34 |
| 10 | 10 | Estanque de acumulación de digestato - Etapa 1 | 0,32/e | 2,94 |
| 11 | 11 | Contenedor deshidratado mecánico - Etapa 1 | 0,32/e | 4,07 |
| 12 | 12 | Estanque de acumulación clarificado - Etapa 2 | 0,32/e | 64,34 |
| 13 | 13 | Contenedor deshidratado mecánico - Etapa 2 | 0,32/e | 4,07 |
| 14 | 14 | Galpón de recepción (Sist. de abatimiento olores - Etapa 1) | 47,23 | 53,42/f |
| 15 | 15 | Galpón de recepción (Sist. de abatimiento olores - Etapa 2) | 47,23 | 53,42/f |
| 16 | 16 | Unidad de almacenamiento de digestato | 0,32/e | 1.705,28 |
| 17 | PTRILes | Laguna anaeróbica | 5,71/f | 11.424,00 |
| 18 | 18 | Laguna de percolados | 5,71/f | 5.710,00 |
| 19 | 19 | Reactor aerobio 1 | 19,08/g | 1.498,54 |
| 20 | 20 | Reactor aerobio 2 | 19,08/g | 1.498,54 |
| 21 | 21 | Reactor aerobio 3 | 19,08/g | 1.498,54 |
| 22 | 22 | Reactor aerobio 4 | 19,08/g | 1.498,54 |
| 23 | 23 | Clarificador | 8,52/g | 206,18 |
| 24 | 24 | Floculador | 8,52/g | 60,22 |
| 25 | 25 | Laguna lodos biológicos | 21,2/h | 1.433,12 |
| 26 | 26 | Laguna lodo físico/químico | 2,3/h | 140,76 |
| 27 | 27 | Laguna agua tratada | 0,25/i | 94,25 |
| 28 | Relleno | Alvéolo 7 - Frente de trabajo | 21,3/h | 18.105,00 |
| 28 | Riego | Zona de riego 1 | 0,32/h | 4.217,60 |
| 28 | 28 | Zona de riego 2 | 0,32/h | 5.729,96 |

**Tabla 16: - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 1**

| Requisito | Col2 | Pila Lodo<br>Agroindustrial -<br>Edad 1 | Pila Lodo<br>Agroindustrial -<br>Edad 2 | Pila Lodo<br>Agroindustrial -<br>Edad 3 | Pila lodo<br>sanitario -<br>Edad 1 Curicó | Pila lodo<br>sanitario - Edad<br>1 Otras<br>Localidades | Pila lodo<br>sanitario -<br>Edad 2 Curicó | Pila lodo<br>sanitario - Edad<br>2 Otras<br>Localidades | Pila lodo<br>sanitario -<br>Edad 3 Curicó | Pila lodo<br>sanitario -<br>Edad 3 Otras<br>Localidades |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase del proyecto que genera<br>olor | Fase del proyecto que genera<br>olor | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Actividad que genera emisiones<br>de olor | Actividad que genera emisiones<br>de olor | Compostaje en<br>cancha | Compostaje en<br>cancha | Compostaje en<br>cancha | Biosecado en<br>cancha | Biosecado en<br>cancha | Biosecado en<br>cancha | Biosecado en<br>cancha | Biosecado en<br>cancha | Biosecado en<br>cancha |
| Identificación del material o<br>sustancia olorosa | Identificación del material o<br>sustancia olorosa | Lodo<br>Agroindustrial | Lodo<br>Agroindustrial | Lodo<br>Agroindustrial | Lodo Sanitario | Lodo Sanitario | Lodo Sanitario | Lodo Sanitario | Lodo Sanitario | Lodo Sanitario |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa |
| Régimen de<br>emisión de<br>olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de<br>olor | Horas de<br>operación | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] |
| Régimen de<br>emisión de<br>olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor [ouE/m2*s] | Emisión de olor [ouE/m2*s] | 14,70 | 8,30 | 1,60 | 5,70 | 3,80 | 11,4 | 5,90 | 5,60 | 1,70 |
| Tasa de emisión de olor | Tasa de emisión de olor | 181.530,30 | 61.876,50 | 3.840,00 | 45.446,10 | 90.892,20 | 72.982,80 | 113.315,40 | 6.493,20 | 5.913,45 |
| Calidad | Calidad | Humedad,<br>percolado,<br>agrio | Basura,<br>descomposición,<br>agrio | Tierra,<br>humedad,<br>basura | Humedad,<br>mohoso, tierra | Descomposición,<br>tierra, humedad | Tierra,<br>humedad,<br>vegetales<br>descomp. | Descomposición,<br>agrio, podrido | Humedad,<br>tierra | Humedad,<br>tierra,<br>detergente |

**Tabla 17: - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 2**

| Requisito | Col2 | Laguna de<br>percolados | Laguna de<br>agua rechazo | Reactor<br>aerobio 1 | Reactor<br>aerobio 2 | Clarificador | Floculador | Laguna lodos<br>biológicos | Laguna lodos<br>físico/químico | Lecho de<br>secado 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase del proyecto que genera<br>olor | Fase del proyecto que genera<br>olor | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Actividad que genera emisiones<br>de olor | Actividad que genera emisiones<br>de olor | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes |
| Identificación del material o<br>sustancia olorosa | Identificación del material o<br>sustancia olorosa | RILes | RILes | RILes | RILes | RILes | RILes | RILes | RILes | RILes |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa |
| Régimen de<br>emisión de olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de olor | Horas de<br>operación | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] |
| Régimen de<br>emisión de olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor [ouE/m2*s] | Emisión de olor [ouE/m2*s] | 81,60 | 81,60 | 31,80 | 31,80 | 14,20 | 14,20 | 21,20 | 2,30 | 4,20 |
| Tasa de emisión de olor | Tasa de emisión de olor | 81.600,00 | 12.566,00 | 2.497,57 | 2.497,57 | 343,64 | 100,37 | 1.433.12 | 140,76 | 1.268,40 |
| Calidad | Calidad | Ácido, basura,<br>fermentación | Ácido, basura,<br>fermentación | Detergente,<br>humedad,<br>ácido | Detergente,<br>humedad,<br>ácido | Humedad,<br>ácido | Humedad,<br>ácido | Sulfuroso, gas,<br>percolado | Tierra,<br>humedad | Humedad,<br>rancio, tierra |

**Tabla 18: - Descriptores de las fuentes emisoras de olor - Situación actual - Parte 3**

| Requisito | Col2 | Lecho de<br>secado 2<br>(lavado de<br>camiones) | Laguna de<br>agua tratada | Monorelleno -<br>Frente de<br>trabajo | Relleno<br>sanitario -<br>Frente de<br>trabajo |
| --- | --- | --- | --- | --- | --- |
| Fase del proyecto que genera<br>olor | Fase del proyecto que genera<br>olor | Operación | Operación | Operación | Operación |
| Actividad que genera emisiones<br>de olor | Actividad que genera emisiones<br>de olor | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Disposición de<br>residuos<br>sólidos | Disposición de<br>residuos<br>sólidos |
| Identificación del material o<br>sustancia olorosa | Identificación del material o<br>sustancia olorosa | RILes | Agua tratada | Residuos<br>sólidos<br>(orgánicos) | Residuos<br>sólidos<br>(orgánicos) |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Difusa |
| Régimen de<br>emisión de olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de olor | Horas de<br>operación | 24 [h] | 24 [h] | 24 [h] | 24 [h] |
| Régimen de<br>emisión de olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor [ouE/m2*s] | Emisión de olor [ouE/m2*s] | 32,80 | 2,40 | 11,10 | 21,30 |
| Tasa de emisión de olor | Tasa de emisión de olor | 8.757,60 | 904,80 | 50.038,80 | 18.105,00 |
| Calidad | Calidad | Percolado,<br>humedad, gas | Tierra,<br>humedad | Terroso,<br>humedad | Percolado,<br>fermentación |

**Tabla 19: - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 1**

| Requisito | Col2 | Cancha de<br>compostaje 1 | Cancha de<br>compostaje 2 | Cancha de<br>compostaje 3 | Cancha de<br>compostaje 4 | Galpón<br>compostaje 1<br>(sist. de<br>abatimiento) | Galpón<br>compostaje 2<br>(sist. de<br>abatimiento) | Galpón<br>compostaje 3<br>(sist. de<br>abatimiento) | Galpón<br>compostaje 4<br>(sist. de<br>abatimiento) | Estanque de<br>acumulación<br>clarificado -<br>Etapa 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase del proyecto que genera<br>olor | Fase del proyecto que genera<br>olor | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Actividad que genera emisiones<br>de olor | Actividad que genera emisiones<br>de olor | Estabilización<br>de compost en<br>cancha | Estabilización<br>de compost en<br>cancha | Estabilización<br>de compost en<br>cancha | Estabilización<br>de compost en<br>cancha | Compostaje<br>aireado<br>(confinado) | Compostaje<br>aireado<br>(confinado) | Compostaje<br>aireado<br>(confinado) | Compostaje<br>aireado<br>(confinado) | Digestión<br>anaeróbica |
| Identificación del material o<br>sustancia olorosa | Identificación del material o<br>sustancia olorosa | Compost | Compost | Compost | Compost | Compost | Compost | Compost | Compost | Digestato |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Difusa | Puntual | Puntual | Puntual | Puntual | Difusa |
| Régimen de<br>emisión de olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de olor | Horas de<br>operación | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] |
| Régimen de<br>emisión de olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor [ouE/m2*s] | Emisión de olor [ouE/m2*s] | 0,53 | 0,53 | 0,53 | 0,53 | 1.128,86 | 1.438,43 | 1.438,43 | 1.438,43 | 0,32 |
| Tasa de emisión de olor | Tasa de emisión de olor | 5.283,75 | 2.610,30 | 7.441,46 | 8.420,32 | 1.276,71 | 1.626,82 | 1.626,82 | 1.626,82 | 64,34 |
| Calidad | Calidad | /a | /a | /a | /a | /a | /a | /a | /a | /a |

**Tabla 20: - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 2**

| Requisito | Col2 | Estanque de<br>acumulación<br>digestato -<br>Etapa 1 | Cont.<br>deshidratado<br>mecánico -<br>Etapa 1 | Estanque de<br>acumulación<br>clarificado -<br>Etapa 2 | Cont.<br>deshidratado<br>mecánico -<br>Etapa 2 | Galpón de<br>recepción (sist.<br>de abatimiento<br>etapa 1) | Galpón de<br>recepción (sist.<br>de abatimiento<br>etapa 1) | Unidad de<br>almacenamiento<br>de digestato | Laguna<br>anaeróbica | Laguna de<br>percolados |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase del proyecto que genera<br>olor | Fase del proyecto que genera<br>olor | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Actividad que genera emisiones<br>de olor | Actividad que genera emisiones<br>de olor | Digestión<br>anaeróbica | Digestión<br>anaeróbica | Digestión<br>anaeróbica | Digestión<br>anaeróbica | Digestión<br>anaeróbica | Digestión<br>anaeróbica | Digestión<br>anaeróbica | Tratamiento de<br>RILes | Tratamiento de<br>RILes |
| Identificación del material o<br>sustancia olorosa | Identificación del material o<br>sustancia olorosa | Digestato | Digestato | Digestato | Digestato | Digestato | Digestato | Digestato | RILes | RILes |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Difusa | Puntual | Puntual | Difusa | Difusa | Difusa |
| Régimen de<br>emisión de<br>olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de<br>olor | Horas de<br>operación | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] |
| Régimen de<br>emisión de<br>olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor [ouE/m2*s] | Emisión de olor [ouE/m2*s] | 0,32 | 0,32 | 0,32 | 0,32 | 47,23 | 47,23 | 0,32 | 5,71 | 5,71 |
| Tasa de emisión de olor | Tasa de emisión de olor | 2,94 | 4,07 | 64,34 | 4,07 | 53,42 | 53,42 | 1.705,28 | 11.424,00 | 5.710,00 |
| Calidad<br> | Calidad<br> | /a <br> | /a <br> | /a <br> | /a | /a | /a | /a | /a | /a |

**Tabla 21: - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 3**

| Requisito | Col2 | Reactor<br>aerobio 1 | Reactor<br>aerobio 2 | Clarificador | Floculador | Laguna lodos<br>biológicos | Laguna lodo<br>físico/químico | Laguna de agua<br>tratada | Reactor<br>aerobio 3 | Reactor<br>aerobio 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase del proyecto que genera<br>olor | Fase del proyecto que genera<br>olor | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Actividad que genera emisiones<br>de olor | Actividad que genera emisiones<br>de olor | Tratamiento<br>de RILes | Tratamiento<br>de RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes | Tratamiento de<br>RILes |
| Identificación del material o<br>sustancia olorosa | Identificación del material o<br>sustancia olorosa | RILes | RILes | RILes | RILes | RILes | RILes | RILes | RILes | RILes |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa | Difusa |
| Régimen de<br>emisión de<br>olor | Ciclo<br>operacional | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de<br>olor | Horas de<br>operación | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] | 24 [h] |
| Régimen de<br>emisión de<br>olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses | 12 meses |
| Emisión de olor [ouE/m2*s] | Emisión de olor [ouE/m2*s] | 19,08 | 19,08 | 8,52 | 8,52 | 21,20 | 2,30 | 0,25 | 19,08 | 19,08 |
| Tasa de emisión de olor | Tasa de emisión de olor | 1.498,54 | 1.498,54 | 206,18 | 60,22 | 1.433,12 | 140,76 | 94,25 | 1.498,54 | 1.498,54 |
| Calidad<br> | Calidad<br> | /a <br> | /a <br> | /a <br> | /a | /a | /a | /a | /a | /a |

**Tabla 22: - Descriptores de las fuentes emisoras de olor - Situación futura - Parte 4**

| Requisito | Col2 | Alvéolo 7 -<br>Frente de<br>trabajo | Zona de<br>riego 1 | Zona de<br>riego 2 |
| --- | --- | --- | --- | --- |
| Fase del proyecto que genera<br>olor | Fase del proyecto que genera<br>olor | Operación | Operación | Operación |
| Actividad que genera emisiones<br>de olor | Actividad que genera emisiones<br>de olor | Disposición de<br>residuos<br>sólidos | Riego de<br>digestato | Riego de<br>digestato |
| Identificación del material o<br>sustancia olorosa | Identificación del material o<br>sustancia olorosa | Residuos<br>sólidos | Digestato<br>tratado | Digestato<br>tratado |
| Tipo de fuente | Tipo de fuente | Difusa | Difusa | Difusa |
| Régimen de<br>emisión de<br>olor | Ciclo<br>operacional | Continuo | Continuo | Continuo |
| Régimen de<br>emisión de<br>olor | Horas de<br>operación | 24 [h] | 24 [h] | 24 [h] |
| Régimen de<br>emisión de<br>olor | Frecuencia<br>mensual | 12 meses | 12 meses | 12 meses |
| Emisión de olor [ouE/m2*s] | Emisión de olor [ouE/m2*s] | 21,30 | 0,32 | 0,32 |
| Tasa de emisión de olor | Tasa de emisión de olor | 18.105,00 | 4.217,60 | 5.729,96 |
| Calidad | Calidad | /a | /a | /a |

**Tabla 23: - Ranking TEO [ou E /s] por fuente modelada - Situación actual**

| Unidad | EO<br>[ou /m2*s]<br>E | TEO [ou /s]<br>E | % TEO | % TEO<br>acum. |
| --- | --- | --- | --- | --- |
| Pila Lodo Agroindustrial - Edad 1 | 14,70 | 181.530,30 | 23,81% | 23,81% |
| Pila lodo sanitario - Edad 2 Otras Localidades | 5,90 | 113.315,40 | 14,86% | 38,67% |
| Pila lodo sanitario - Edad 1 Otras Localidades | 3,80 | 90.892,20 | 11,92% | 50,59% |
| Laguna de percolados | 81,60 | 81.600,00 | 10,70% | 61,29% |
| Pila lodo sanitario - Edad 2 Curicó | 11,40 | 72.982,80 | 9,57% | 70,86% |
| Pila Lodo Agroindustrial - Edad 2 | 8,30 | 61.876,50 | 8,11% | 78,97% |
| Monorelleno - Frente de trabajo | 11,10 | 50.038,80 | 6,56% | 85,53% |
| Pila lodo sanitario - Edad 1 Curicó | 5,70 | 45.446,10 | 5,96% | 91,49% |
| Relleno Sanitario - Frente de trabajo | 21,30 | 18.105,00 | 2,37% | 93,87% |
| Laguna de agua rechazo | 81,60 | 12.566,40 | 1,65% | 95,52% |
| Lechos de secado 2 (lavado de camiones) | 32,80 | 8.757,60 | 1,15% | 96,66% |
| Pila lodo sanitario - Edad 3 Curicó | 5,60 | 6.493,20 | 0,85% | 97,52% |
| Pila lodo sanitario - Edad 3 Otras Localidades | 1,70 | 5.913,45 | 0,78% | 98,29% |
| Pila Lodo Agroindustrial - Edad 3 | 1,60 | 3.840,00 | 0,50% | 98,80% |
| Reactor aerobio 1 | 31,80 | 2.497,57 | 0,33% | 99,12% |
| Reactor aerobio 2 | 31,80 | 2.497,57 | 0,33% | 99,45% |
| Laguna lodos biológicos | 21,20 | 1.433,12 | 0,19% | 99,64% |
| Lechos de secado 1 | 4,20 | 1.268,40 | 0,17% | 99,80% |
| Laguna agua tratada | 2,40 | 904,80 | 0,12% | 99,92% |
| Clarificador | 14,20 | 343,64 | 0,05% | 99,97% |
| Laguna lodo físico/químico | 2,30 | 140,76 | 0,02% | 99,99% |
| Floculador | 14,20 | 100,37 | 0,01% | 100,00% |

**Tabla 24: - Ranking TEO [ou E /s] por fuente modelada - Situación futura**

| Unidad | EO [ou/m2*s]<br>E | TEO [ou/s]<br>E | % TEO | % TEO<br>acumulado |
| --- | --- | --- | --- | --- |
| Alvéolo 7 - Frente de trabajo | 21,30 | 18.105,00 | 21,30% | 21,30% |
| Laguna de anaeróbica | 5,71 | 11.424,00 | 13,44% | 34,75% |
| Cancha de compostaje 4 | 0,53 | 8.420,32 | 9,91% | 44,66% |
| Cancha de compostaje 3 | 0,53 | 7.441,46 | 8,76% | 53,41% |
| Zona de riego 2 | 0,32 | 5.729,96 | 6,74% | 60,16% |
| Laguna de percolados | 5,71 | 5.710,00 | 6,72% | 66,88% |
| Cancha de compostaje 1 | 0,53 | 5.283,75 | 6,22% | 73,09% |
| Zona de riego 1 | 0,32 | 4.217,60 | 4,96% | 78,06% |
| Cancha de compostaje 2 | 0,53 | 2.610,30 | 3,07% | 81,13% |
| Unidad de alm. de digestato | 0,32 | 1.705,28 | 2,01% | 83,13% |
| Galpón de comp. 2 (sist. de abatimiento) | 1.438,43 | 1.626,82 | 1,91% | 85,05% |
| Galpón de comp. 3 (sist. de abatimiento) | 1.438,43 | 1.626,82 | 1,91% | 86,96% |
| Galpón de comp. 4 (sist. de abatimiento) | 1.438,43 | 1.626,82 | 1,91% | 88,88% |
| Reactor aerobio 1 | 19,08 | 1.498,54 | 1,76% | 90,64% |
| Reactor aerobio 2 | 19,08 | 1.498,54 | 1,76% | 92,40% |
| Reactor aerobio 3 | 19,08 | 1.498,54 | 1,76% | 94,17% |
| Reactor aerobio 4 | 19,08 | 1.498,54 | 1,76% | 95,93% |
| Laguna lodos biológicos | 21,20 | 1.433,12 | 1,69% | 97,62% |
| Galpón de comp. 1 (sist. de abatimiento) | 1.128,86 | 1.276,71 | 1,50% | 99,12% |
| Clarificador | 8,52 | 206,18 | 0,24% | 99,36% |
| Laguna lodo físico/químico | 2,30 | 140,76 | 0,17% | 99,53% |
| Laguna agua tratada | 0,25 | 94,25 | 0,11% | 99,64% |
| Est. acumulación clarificado - Etapa 1 | 0,32 | 64,34 | 0,08% | 99,71% |
| Est. acumulación clarificado - Etapa 2 | 0,32 | 64,34 | 0,08% | 99,79% |
| Floculador | 8,52 | 60,22 | 0,07% | 99,86% |
| Sistema de abatimiento olores - Etapa 1 | 47,23 | 53,42 | 0,06% | 99,92% |
| Sistema de abatimiento olores - Etapa 2 | 47,23 | 53,42 | 0,06% | 99,99% |
| Cont. deshidratado mecánico - Etapa 1 | 0,32 | 4,07 | 0,00% | 99,99% |
| Cont. deshidratado mecánico - Etapa 2 | 0,32 | 4,07 | 0,00% | 100,00% |
| Est. acumulación de disgestato - Etapa 1 | 0,32 | 2,94 | 0,00% | 100,00% |

**Tabla 25: - Puntos receptores de interés**

| Receptores | Col2 | Coordenadas UTM [m]<br>(WGS84-H19Sur) | Col4 | Distancia del<br>receptor al<br>perímetro [m] | Orientación |
| --- | --- | --- | --- | --- | --- |
| Receptores | Receptores | X: Este | Y: Sur | Y: Sur | Y: Sur |
| R1 | Vivienda 1 | 281.592 | 6.102.008 | 73 | NO |
| R2 | Vivienda 2 | 281.249 | 6.100.732 | 1.018 | OSO |
| R3 | Vivienda 3 | 282.640 | 6.100.524 | 618 | SSE |
| R4 | Vivienda 4 | 283.523 | 6.101.049 | 900 | ESE |
| R5 | Vivienda 5 | 283.564 | 6.101.675 | 448 | E |
| R6 | Vivienda 6 | 282.268 | 6.102.799 | 1.036 | N |
| R7 | Sector Los Robles | 285.389 | 6.099.690 | 3.196 | ESE |
| R8 | Sector Escudo de Chile | 282.974 | 6.099.435 | 1.760 | SSE |
| R9 | Sector El Umbral | 281.385 | 6.098.648 | 2.666 | SSO |
| R10 | Escuela Juan Luis Sanfuentes A. | 279.809 | 6.099.482 | 2.917 | SO |
| R11 | Sector Camarico | 279.789 | 6.099.541 | 2.898 | OO |
| R12 | Peaje Troncal Río Claro | 280.532 | 6.101.093 | 1.484 | OSO |

**Tabla 26: - Situación olor base - Proyectos aprobados en SEIA**

| ID | Nombre del proyecto | Titular del proyecto | No RCA | Coordenadas UTM | Col6 |
| --- | --- | --- | --- | --- | --- |
| ID | Nombre del proyecto | Titular del proyecto | No RCA | X: Este | Y: Norte |
| PA1 | Alcantarillado Camarico | Ilustre Municipalidad de<br>Río Claro | 65/99 | 279.275 | 6.099.857 |
| PA2 | Planta compostaje Los<br>Robles | Constructora Cordero y<br>Asalgado Ltda. | 182/2003 | 280.462 | 6.100.186 |

**Tabla 27: - Situación olor base - Establecimientos identificados en terreno [/a]**

| ID | Nombre del proyecto | Coordenadas UTM | Col4 |
| --- | --- | --- | --- |
| ID | Nombre del proyecto | X: Este | Y: Norte |
| E1 | Fosa séptica comunitaria Raquel de Chanceaulme | 279.716 | 6.099.885 |
| E2 | Almazara aceite oliva Camarico | 280.417 | 6.099.797 |
| E3 | Planta de aguas servidas El Umbral | 281.242 | 6.098.843 |
| E4 | Bodega vinificación | 283.677 | 6.100.092 |

**Tabla 28: - Concentraciones máximas en receptores según normativa de Lombardía.**

| Receptores | Percentil | Valores [ou /m3]<br>E |
| --- | --- | --- |
| Primer receptor a una distancia >500 m desde el deslinde de la planta | 98 | 3 |
| Primer receptor a una distancia entre 200 y 500 m desde el deslinde de la planta | Primer receptor a una distancia entre 200 y 500 m desde el deslinde de la planta | 4 |
| Primer receptor a una distancia <200 m desde el deslinde de la planta | Primer receptor a una distancia <200 m desde el deslinde de la planta | 5 |

**Tabla 29: - Valores límites en receptores de interés**

| ID | Nombre | Distancia al<br>perímetro de la<br>planta [m] | Rango distancia [m] | Valor límite norma<br>Lombardía<br>CO [ou /m3]<br>E |
| --- | --- | --- | --- | --- |
| R1 | Vivienda 1 | 73 | <200 | 5 |
| R2 | Vivienda 2 | 1,018 | >500 | 3 |
| R3 | Vivienda 3 | 706 | >500 | 3 |
| R4 | Vivienda 4 | 900 | >500 | 3 |
| R5 | Vivienda 5 | 448 | > 200 - < 500 | 4 |
| R6 | Vivienda 6 | 1,036 | >500 | 3 |
| R7 | Sector Los Robles | 3,196 | >500 | 3 |
| R8 | Sector Escudo de Chile | 1,855 | >500 | 3 |
| R9 | Sector El Umbral | 2,666 | >500 | 3 |
| R10 | Escuela Juan Luis Sanfuentes A. | 2,917 | >500 | 3 |
| R11 | Sector Camarico | 2,898 | >500 | 3 |
| R12 | Peaje Troncal Río Claro | 1,484 | >500 | 3 |

**Tabla 30: - Descripción escenarios simulados**

| Escenario Operacional | Modelo | Percentil | Criterio de<br>calidad |
| --- | --- | --- | --- |
| E1: Situación actual<br>E2: Situación futura | M1: Curvas de isoconcentración de olor<br>M2: Frecuencia de percepción de olor (horaria)<br>M3: Frecuencia de percepción de olor (mensual)<br>M4: Concentración máxima horaria | 98 | 3, 4 y 5<br>[ouE/m3] |

**Tabla 31: - E1/M2: Frecuencia de percepción de olor horaria [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación actual**

| Valor<br>límite C<br>P98 | 3 [ou /m3]<br>E | 4<br>[ou /m3]<br>E | 5<br>[ou /m3]<br>E |
| --- | --- | --- | --- |
| **Hora del**<br>**día** | **R2**<br>**R3**<br>**R4**<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12** | **R5/b ** | **R1/c ** |
| 0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23 | 29<br>31<br>29<br>42<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>30<br>27<br>24<br>51<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>28<br>26<br>25<br>43<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>34<br>20<br>19<br>35<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>39<br>28<br>19<br>38<br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>41<br>26<br>22<br>44<br>0 <br>4 <br>0 <br>0 <br>0 <br>0 <br>28<br>19<br>21<br>22<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>24<br>9 <br>9 <br>18<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>12<br>9 <br>5 <br>6 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>9 <br>6 <br>3 <br>5 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>5 <br>0 <br>4 <br>4 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>3 <br>1 <br>3 <br>4 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>1 <br>2 <br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>2 <br>3 <br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>4 <br>4 <br>2 <br>1 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>6 <br>2 <br>4 <br>2 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>5 <br>10<br>9 <br>10<br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>11<br>16<br>21<br>24<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>20<br>26<br>36<br>42<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>28<br>44<br>53<br>61<br>0 <br>5 <br>0 <br>0 <br>0 <br>0 <br>26<br>45<br>47<br>50<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>28<br>38<br>45<br>41<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>36<br>40<br>37<br>43<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>33<br>35<br>33<br>39<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 | 32<br>24<br>27<br>27<br>25<br>27<br>29<br>11<br>8 <br>4 <br>4 <br>2 <br>5 <br>7 <br>19<br>22<br>33<br>37<br>72<br>86<br>72<br>59<br>44<br>32 | 26<br>25<br>28<br>25<br>22<br>19<br>15<br>11<br>7 <br>2 <br>3 <br>1 <br>0 <br>0 <br>1 <br>1 <br>4 <br>3 <br>27<br>31<br>32<br>31<br>31<br>19 |
| **Total** | **482**<br>**467**<br>**470**<br>**628**<br>**0 **<br>**31**<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **708** | **364** |

**Tabla 32: - E1/M3: Frecuencia de percepción de olor mensual [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación actual**

| Valor<br>límite C<br>P98 | 3<br>[ou /m3]<br>E | 4<br>[ou /m3]<br>E | 5<br>[ou /m3]<br>E |
| --- | --- | --- | --- |
| **Mes** | **R2**<br>**R3**<br>**R1/c **<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12** | **R5/b ** | **R1/c ** |
| Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre | 28<br>38<br>40<br>68<br>0 <br>3 <br>0 <br>0 <br>0 <br>0 <br>26<br>40<br>47<br>54<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>26<br>25<br>37<br>54<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>37<br>43<br>51<br>67<br>0 <br>4 <br>0 <br>0 <br>0 <br>0 <br>74<br>66<br>64<br>57<br>0 <br>7 <br>0 <br>0 <br>0 <br>0 <br>75<br>64<br>37<br>49<br>0 <br>5 <br>0 <br>0 <br>0 <br>0 <br>60<br>39<br>34<br>61<br>0 <br>4 <br>0 <br>0 <br>0 <br>0 <br>32<br>18<br>22<br>43<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>40<br>37<br>35<br>43<br>0 <br>2 <br>0 <br>0 <br>0 <br>0 <br>50<br>50<br>51<br>52<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>18<br>16<br>18<br>34<br>0 <br>1 <br>0 <br>0 <br>0 <br>0 <br>16<br>31<br>34<br>46<br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 84<br><br>70<br><br>55<br><br>78<br><br>60<br><br>38<br><br>44<br><br>38<br><br>65<br><br>74<br><br>48<br><br>54 | 25<br>32<br>29<br>35<br>39<br>31<br>34<br>28<br>30<br>41<br>13<br>27 |
| Total | **482**<br>**467**<br>**470**<br>**628**<br>**0 **<br>**31**<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **708** | **364** |

**Tabla 33: - E1/M2: Frecuencia de percepción de olor horaria [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación futura**

| Valor<br>limite C<br>P98 | 3<br>[ou /m3]<br>E | 4<br>[ou /m3]<br>E | 5<br>[ou /m3]<br>E |
| --- | --- | --- | --- |
| **Hora del**<br>**día** | **R2**<br>**R3**<br>**R5/b **<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12** | **R5/b ** | **R1/c ** |
| 0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 |
| **Total** | **0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **0 ** | **0 ** |

**Tabla 34: - E1/M3: Frecuencia de percepción de olor mensual [/a] - C P98-1hr =3, 4 y 5 [ou E /m [3] ] - Situación futura**

| Valor<br>límite C<br>P98 | 3<br>[ou /m3]<br>E | 4<br>[ou /m3]<br>E | 5<br>[ou /m3]<br>E |
| --- | --- | --- | --- |
| **Mes** | **R2**<br>**R3**<br>**R1/c **<br>**R6**<br>**R7**<br>**R8**<br>**R9**<br>**R10**<br>**R11**<br>**R12** | **R5/b ** | **R1/c ** |
| Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 | 0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 |
| Total | **0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 **<br>**0 ** | **0 ** | **0 ** |

**Tabla 35: - Concentración máxima - Percentil 98 y 99,5 - Situación actual**

| ID | Concentración máxima [ou /m3]<br>E | Col3 |
| --- | --- | --- |
| ID | Percentil 99,5 | Percentil 98 |
| R1 | 42 | 16 |
| R2 | 33 | 12 |
| R3 | 71 | 22 |
| R4 | 70 | 26 |
| R5 | 144 | 65 |
| R6 | 48 | 19 |
| R7 | 4 | 1 |
| R8 | 13 | 3 |
| R9 | 5 | 2 |
| R10 | 7 | 2 |
| R11 | 7 | 2 |
| R12 | 12 | 2 |

**Tabla 36: - Concentración máxima - Percentil 98 y 99,5 - Situación futura**

| ID | Concentración máxima [ou /m3]<br>E | Col3 | Limite Norma<br>Lombardía<br>CO [ou /m3]<br>E | Cumplimiento |
| --- | --- | --- | --- | --- |
| ID | Percentil 99,5 | Percentil 98 | Percentil 98 | Percentil 98 |
| R1 | 4 | 1 | 5 | Si |
| R2 | 1 | <1 | 3 | Si |
| R3 | 3 | 1 | 3 | Si |
| R4 | 3 | 1 | 3 | Si |
| R5 | 6 | 2 | 4 | Si |
| R6 | 2 | 1 | 3 | Si |
| R7 | <1 | <1 | 3 | Si |
| R8 | <1 | <1 | 3 | Si |
| R9 | <1 | <1 | 3 | Si |
| R10 | <1 | <1 | 3 | Si |
| R11 | <1 | <1 | 3 | Si |
| R12 | <1 | <1 | 3 | Si |

**Tabla 37: - Situación actual: Caracterización de fuentes de olor (parte 1)**

| ID | Fuente | Coordenadas UTM [m] | Col4 | Altura<br>desde<br>suelo [m] | Vel.<br>salida<br>[m/s] | Temp.<br>salida<br>[oK] | Diám.<br>ducto [m] | Largo<br>[m]/a | Ancho<br>[m]/a | Radio<br>[m] | Área<br>[m2] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Fuente | X: Este | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte |
| 1 | Pila Lodo Agroindustrial - Edad 1 | 282.608 | 6.101.746 | 1,6 | - | - | - | 86,00 | 76,26 | - | 6.558,00 |
| 2 | Pila Lodo Agroindustrial - Edad 1 | 282.477 | 6.101.593 | 1,6 | - | - | - | 152,39 | 38,00 | - | 5.791,00 |
| 3 | Pila Lodo Agroindustrial - Edad 2 | 282.491 | 6.101.572 | 1,6 | - | - | - | 207,08 | 36,00 | - | 7.455,00 |
| 4 | Pila Lodo Agroindustrial - Edad 3a | 282.599 | 6.101.756 | 1,6 | - | - | - | 100,00 | 12,00 | - | 1.200,00 |
| 5 | Pila Lodo Agroindustrial - Edad 3b | 282.671 | 6.101.810 | 1,6 | - | - | - | 60,00 | 20,00 | - | 1.200,00 |
| 6 | Pila lodo sanitario - Edad 1 Curicó | 282.791 | 6.101.622 | 1,6 | - | - | - | 46,72 | 74,00 | - | 3.457,00 |
| 7 | Pila lodo sanitario - Edad 1 Otras Localidades | 282.815 | 6.101.660 | 1,6 | - | - | - | 140,15 | 74,00 | - | 10.371,00 |
| 8 | Pila lodo sanitario - Edad 2 Curicó | 282.743 | 6.101.660 | 1,6 | - | - | - | 40,76 | 51,00 | - | 2.078,75 |
| 9 | Pila lodo sanitario - Edad 2 Otras Localidades | 282.771 | 6.101.696 | 1,6 | - | - | - | 122,28 | 51,00 | - | 6.236,25 |
| 10 | Pila lodo sanitario - Edad 1 Curicó | 282.712 | 6.101.692 | 1,6 | - | - | - | 33,13 | 34,00 | - | 1.126,50 |
| 11 | Pila lodo sanitario - Edad 1 Otras Localidades | 282.740 | 6.101.731 | 1,6 | - | - | - | 99,40 | 34,00 | - | 3.379,50 |
| 12 | Pila lodo sanitario - Edad 2 Curicó | 282.682 | 6.101.715 | 1,6 | - | - | - | 29,40 | 33,00 | - | 970,25 |
| 13 | Pila lodo sanitario - Edad 2 Otras Localidades | 282.705 | 6.101.743 | 1,6 | - | - | - | 88,20 | 33,00 | - | 2.910,75 |
| 14 | Pila lodo sanitario - Edad 1 Curicó | 282.669 | 6.101.464 | 1,6 | - | - | - | 35,43 | 30,00 | - | 1.063,00 |
| 15 | Pila lodo sanitario - Edad 1 Otras Localidades | 282.669 | 6.101.464 | 1,6 | - | - | - | 106,30 | 30,00 | - | 3.189,00 |
| 16 | Pila lodo sanitario - Edad 2 Curicó | 282.712 | 6.101.566 | 1,6 | - | - | - | 34,87 | 35,00 | - | 1.220,50 |
| 17 | Pila lodo sanitario - Edad 2 Otras Localidades | 282.644 | 6.101.488 | 1,6 | - | - | - | 104,61 | 35,00 | - | 3.661,50 |
| 18 | Pila lodo sanitario - Edad 3 Curicó | 282.567 | 6.101.489 | 1,6 | - | - | - | 27,79 | 23,00 | - | 639,25 |
| 19 | Pila lodo sanitario - Edad 3 Otras Localidades | 282.587 | 6.101.467 | 1,6 | - | - | - | 83,38 | 23,00 | - | 1.917,75 |
| 20 | Pila lodo sanitario - Edad 1 Curicó | 282.587 | 6.101.503 | 1,6 | - | - | - | 27,98 | 12,00 | - | 335,75 |
| 21 | Pila lodo sanitario - Edad 1 Otras Localidades | 282.606 | 6.101.483 | 1,6 | - | - | - | 83,94 | 12,00 | - | 1.007,25 |
| 22 | Pila lodo sanitario - Edad 2 Curicó | 282.594 | 6.101.512 | 1,6 | - | - | - | 27,02 | 14,00 | - | 378,25 |
| 23 | Pila lodo sanitario - Edad 2 Otras Localidades | 282.614 | 6.101.491 | 1,6 | - | - | - | 81,05 | 14,00 | - | 1.134,75 |
| 24 | Pila lodo sanitario - Edad 1 Curicó | 282.637 | 6.101.675 | 1,6 | - | - | - | 40,63 | 49,00 | - | 1.990,75 |
| 25 | Pila lodo sanitario - Edad 1 Otras Localidades | 282.556 | 6.101.580 | 1,6 | - | - | - | 121,88 | 49,00 | - | 5.972,25 |

**Tabla 38: - Situación actual: Caracterización de fuentes de olor (parte 2)**

| ID | Fuente | Coordenadas UTM [m] | Col4 | Altura<br>desde<br>suelo [m] | Vel.<br>salida<br>[m/s] | Temp.<br>salida<br>[oK] | Diám.<br>ducto [m] | Largo<br>[m]/a | Ancho<br>[m]/a | Radio<br>[m] | Área<br>[m2] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Fuente | X: Este | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte |
| 26 | Pila lodo sanitario - Edad 2 Curicó | 282.671 | 6.101.601 | 1,6 | - | - | - | 35,09 | 50,00 | - | 1.754,25 |
| 27 | Pila lodo sanitario - Edad 2 Otras Localidades | 282.603 | 6.101.521 | 1,6 | - | - | - | 105,26 | 50,00 | - | 5.262,75 |
| 28 | Pila lodo sanitario - Edad 3 Curicó | 282.759 | 6.101.572 | 1,6 | - | - | - | 56,24 | 9,25 | - | 520,25 |
| 29 | Pila lodo sanitario - Edad 3 Otras Localidades | 282.766 | 6.101.566 | 1,6 | - | - | - | 56,24 | 27,75 | - | 1.560,75 |
| 30 | Laguna de percolados | 282.122 | 6.101.571 | 0,0 | - | - | - | 18,09 | 55,29 | - | 1.000,00 |
| 31 | Laguna de agua rechazo | 282.194 | 6.101.668 | 0,0 | - | - | - | 14,00 | 11,00 | - | 154,00 |
| 32 | Reactor aerobio 1 | 282.183 | 6.101.641 | 2,1 | - | - | - | - | - | 5,00 | 78,54 |
| 33 | Reactor aerobio 2 | 282.191 | 6.101.631 | 2,1 | - | - | - | - | - | 5,00 | 78,54 |
| 34 | Clarificador | 282.199 | 6.101.628 | 0,0 | - | - | - | 4,50 | 5,38 | - | 24,20 |
| 35 | Floculador | 282.206 | 6.101.636 | 0,0 | - | - | - | - | - | 1,50 | 7,07 |
| 36 | Laguna lodos biológicos | 282.186 | 6.101.657 | 0,0 | - | - | - | 10,20 | 6,63 | - | 67,60 |
| 37 | Laguna lodo físico/químico | 282.182 | 6.101.652 | 0,0 | - | - | - | 10,20 | 6,00 | - | 61,20 |
| 38 | Lechos de secado 1 | 282.212 | 6.101.589 | 0,0 | - | - | - | 10,00 | 30,20 | - | 302,00 |
| 39 | Lechos de secado 2 (lavado de camiones) | 282.200 | 6.101.596 | 0,0 | - | - | - | 10,00 | 26,70 | - | 267,00 |
| 40 | Laguna agua tratada | 282.165 | 6.101.663 | 0,0 | - | - | - | 11,09 | 34,00 | - | 377,00 |
| 41 | Monorelleno - Frente de trabajo | 282.277 | 6.101.239 | 2,5 | - | - | - | 98,00 | 46,00 | - | 4.508,00 |
| 42 | Relleno Sanitario - Frente de trabajo | 282.314 | 6.101.479 | 10,0 | - | - | - | 42,50 | 20,00 | - | 850,00 |

**Tabla 39: - Situación futura: Caracterización de fuentes de olor (parte 1)**

| ID | Fuente | Coordenadas UTM [m] | Col4 | Altura<br>desde<br>suelo [m] | Vel.<br>salida<br>[m/s] | Temp.<br>salida<br>[oK] | Diám.<br>ducto [m] | Largo<br>[m]/a | Ancho<br>[m]/a | Radio<br>[m] | Área<br>[m2] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Fuente | X: Este | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte |
| 1 | Cancha de compostaje 1 | 282.627 | 6.101.766 | 1,6 | - | - | - | 154,46 | 65,00 | - | 10.040,00 |
| 2 | Cancha de compostaje 2 | 282.745 | 6.101.658 | 1,6 | - | - | - | 154,46 | 32,11 | - | 4.960,00 |
| 3 | Cancha de compostaje 3 | 282.770 | 6.101.646 | 1,6 | - | - | - | 154,46 | 91,54 | - | 14.140,00 |
| 4 | Cancha de compostaje 4 | 282.623 | 6.101.534 | 1,6 | - | - | - | 125,00 | 128,00 | - | 16.000,00 |
| 5 | Galpón de compostaje 1 (sistema de abatimiento) | 282.579 | 6.101.700 | 4,0 | 3,05 | 295,15 | 1,20 | - | - | - | 1,13 |
| 6 | Galpón de compostaje 2 (sistema de abatimiento) | 282.591 | 6.101.720 | 4,0 | 3,05 | 295,15 | 1,20 | - | - | - | 1,13 |
| 7 | Galpón de compostaje 3 (sistema de abatimiento) | 282.609 | 6.101.736 | 4,0 | 3,05 | 295,15 | 1,20 | - | - | - | 1,13 |
| 8 | Galpón de compostaje 4 (sistema de abatimiento) | 282.623 | 6.101.755 | 4,0 | 3,05 | 295,15 | 1,20 | - | - | - | 1,13 |
| 9 | Estanque acumulación clarificado - Etapa 1 | 282.607 | 6.101.593 | 4,0 | - | - | - | - | - | 8,00 | 201,06 |
| 10 | Estanque acumulación de digestato - Etapa 1 | 282.614 | 6.101.585 | 4,0 | - | - | - | - | - | 1,71 | 9,19 |
| 11 | Contenedor deshidratado mecánico - Etapa 1 | 282.610 | 6.101.606 | 2,0 | - | - | - | 2,40 | 5,30 | - | 12,72 |
| 12 | Estanque acumulación clarificado - Etapa 2 | 282.655 | 6.101.641 | 4,0 | - | - | - | - | - | 8,00 | 201,06 |
| 13 | Contenedor deshidratado mecánico - Etapa 2 | 282.615 | 6.101.613 | 2,0 | - | - | - | 2,40 | 5,30 | - | 12,72 |
| 14 | Sistema de abatimiento olores - Etapa 1 | 282.610 | 6.101.579 | 4,0 | 3,05 | 295,15 | 1,20 | - | - | - | 1,13 |
| 15 | Sistema de abatimiento olores - Etapa 2 | 282.651 | 6.101.629 | 4,0 | 3,05 | 295,15 | 1,20 | - | - | - | 1,13 |
| 16 | Unidad de almacenamiento de digestato | 282.569 | 6.101.487 | 1,0 | - | - | - | 73,00 | 73,00 | - | 5.329,00 |
| 17 | Laguna de anaeróbica | 282.130 | 6.101.544 | 0,0 | - | - | - | 64,00 | 31,25 | - | 2.000,00 |
| 18 | Laguna de percolados | 282.122 | 6.101.571 | 0,0 | - | - | - | 18,09 | 55,29 | - | 1.000,00 |
| 19 | Reactor aerobio 1 | 282.183 | 6.101.640 | 2,1 | - | - | - | - | - | 5,00 | 78,54 |
| 20 | Reactor aerobio 2 | 282.191 | 6.101.631 | 2,1 | - | - | - | - | - | 5,00 | 78,54 |

**Tabla 40: - Situación futura: Caracterización de fuentes de olor (parte 2)**

| ID | Fuente | Coordenadas UTM [m] | Col4 | Altura<br>desde<br>suelo [m] | Vel.<br>salida<br>[m/s] | Temp.<br>salida<br>[oK] | Diám.<br>ducto [m] | Largo<br>[m]/a | Ancho<br>[m]/a | Radio<br>[m] | Área<br>[m2] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Fuente | X: Este | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte | Y: Norte |
| 21 | Reactor aerobio 3 | 282.175 | 6.101.629 | 2,1 | - | - | - | - | - | 5,00 | 78,54 |
| 22 | Reactor aerobio 4 | 282.168 | 6.101.618 | 2,1 | - | - | - | - | - | 5,00 | 78,54 |
| 23 | Clarificador | 282.198 | 6.101.627 | 0,0 | - | - | - | 4,50 | 5,38 | - | 24,20 |
| 24 | Floculador | 282.206 | 6.101.635 | 0,0 | - | - | - | - | - | 1,50 | 7,07 |
| 25 | Laguna lodos biológicos | 282.186 | 6.101.657 | 0,0 | - | - | - | 10,20 | 6,63 | - | 67,60 |
| 26 | Laguna lodo físico/químico | 282.182 | 6.101.652 | 0,0 | - | - | - | 10,20 | 6,00 | - | 61,20 |
| 27 | Laguna agua tratada | 282.165 | 6.101.662 | 0,0 | - | - | - | 11,09 | 34,00 | - | 377,00 |
| 28 | Alvéolo 7 - Frente de trabajo | 282.290 | 6.101.242 | 15,0 | - | - | - | 20,00 | 42,50 | - | 850,00 |
| 29 | Zona de riego 1 | 281.821 | 6.101.645 | 0,0 | - | - | - | 114,80 | 114,80 | - | 4.217,60 |
| 30 | Zona de riego 2 | 282.053 | 6.101.591 | 0,0 | - | - | - | 358,12 | 50,00 | - | 5.729,96 |

**Tabla 42: - Curva de estabilización de compostaje en cancha**

| Función | Y=18.419*EXP(-0.516*X) | Col3 |
| --- | --- | --- |
| Semana | Curva exponencial de<br>Emisión de Olor<br>[ouE/m2s]/a | Etapa de compostaje |
| 1 | 10,99 | Con aireación en galpón<br>confinado |
| 2 | 6,56 | 6,56 |
| 3 | 3,92 | 3,92 |
| 4 | 2,34 | 2,34 |
| 5 | 1,40 | Maduración en cancha<br>(etapa 1) |
| 6 | 0,83 | 0,83 |
| 7 | 0,50 | 0,50 |
| 8 | 0,30 | 0,30 |
| 9 | 0,29 | Estabilización en cancha<br>(etapa 2)/b |
| 10 | 0,29 | 0,29 |
| 11 | 0,29 | 0,29 |
| 12 | 0,29 | 0,29 |
| **Promedio de emisión de**<br>**olor del ciclo [ouE/m2s]** | **0,53** |  |

**Tabla 43: - Caracterización de emisión de olor de galpón de recepción**

| Fuente | Largo<br>[m] | Ancho<br>[m] | Diámetro<br>[m] | Área<br>[m2] | Emisión de<br>Olor<br>[ou /m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou /s]<br>E |
| --- | --- | --- | --- | --- | --- | --- |
| Estanque de mezcla<br>Estanque recepción<br>Triturado<br>Higienizado 1<br>Higienizado 2 | - <br>- <br>5,00<br>- <br>- | - <br>- <br>4,00<br>- <br>- | 16,00<br>6,00<br>- <br>4,50<br>4,50 | 201,06<br>28,27<br>20,00<br>15,90<br>15,90 | 3,80<br>3,80<br>3,80<br>3,80<br>3,80 | 764,04<br>107,44<br>76,00<br>60,44<br>60,44 |

**Tabla 44: - Eficiencia de abatimiento de olor de cubiertas flotantes según % de variación**

| Fuentes | Largo [m] | Ancho [m] | Área de<br>emisión [m2] | EO<br>[ouE/m2s] | TEO [ouE/S] |
| --- | --- | --- | --- | --- | --- |
| Laguna anaeróbica | 64,00 | 31,25 | 2.000,00 | 81,60 | 163.200 |
| Laguna de percolados | 18,09 | 55,29 | 1.000,00 | 81,60 | 81.600 |

**Tabla 46: - Caracterización de fuentes PTRILes optimizadas**

| Fuentes | Largo [m] | Ancho [m] | Diámetro [m] | Área de<br>emisión [m2] | EO [ou /m2s]<br>E | TEO [ou /s]<br>E |
| --- | --- | --- | --- | --- | --- | --- |
| Reactor aerobio 1<br>Reactor aerobio 2<br>Clarificador<br>Floculador<br>Reactor aerobio 3<br>Reactor aerobio 4 | - <br>- <br>4,50<br>- <br>- <br>- | - <br>- <br>5,38<br>- <br>- <br>- | 10,00<br>10,00<br>- <br>3,00<br>10,00<br>10,00 | 78,54<br>78,54<br>24,20<br>7,07<br>78,54<br>78,54 | 31,80<br>31,80<br>14,20<br>14,20<br>31,80<br>31,80 | 2.497,57<br>2.497,57<br>343,64<br>100,37<br>2.497,57<br>2.497,57 |

**Tabla 47: - Emisión de olor en fuentes PTRILes optimizadas**

| Fuentes | Área de emisión<br>[m2] | EO<br>[ou /m2s]<br>E | TEO<br>[ou /s]<br>E | %Eficiencia<br>(Optimización<br>de sistema de<br>tratamiento) | TEO Optimizada<br>[ouE/s] |
| --- | --- | --- | --- | --- | --- |
| Reactor aerobio 1<br>Reactor aerobio 2<br>Clarificador<br>Floculador<br>Reactor aerobio 3<br>Reactor aerobio 4 | 78,54<br>78,54<br>24,20<br>7,07<br>78,54<br>78,54 | 31,80<br>31,80<br>14,20<br>14,20<br>31,80<br>31,80 | 2.497,57<br>2.497,57<br>343,64<br>100,37<br>2.497,57<br>2.497,57 | 40%<br>40%<br>40%<br>40%<br>40%<br>40% | 1.498,54<br>1.498,54<br>206,18<br>60,22<br>1.498,54<br>1.498,54 |

**Tabla 48: - Curva de emisión de olor post aplicación de digestato tratado**

| Función | Y= 0,134*(LN(H))+0,2281 |
| --- | --- |
| Cantidad de horas desde<br>aplicación | Curva exponencial de Emisión de Olor<br>[ouE/m2s]/a |
| 0 (Inicio de riego) | 0,32 |
| 1 | 0,23 |
| 2 | 0,14 |
| 3 | 0,08 |
| 4 | 0,04 |
| 5 | 0,01 |
| 6 | 0,00 |

**Tabla 49: - Situación actual: Características operacionales de fuentes emisoras (parte 1)**

| ID | Fuente | Tipo de<br>fuente | Área [m2] | EO por<br>sup.<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E | Ciclo de<br>operación | Horas de<br>operación | Días de<br>operación | Meses de<br>operación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Pila Lodo Agroindustrial - Edad 1 | Difusa | 6.558,00 | 14,7 | 96.402,60 | Continuo | 24 horas | 7 días | 12 meses |
| 2 | Pila Lodo Agroindustrial - Edad 1 | Difusa | 5.791,00 | 14,7 | 85.127,70 | Continuo | 24 horas | 7 días | 12 meses |
| 3 | Pila Lodo Agroindustrial - Edad 2 | Difusa | 7.455,00 | 8,3 | 61.876,50 | Continuo | 24 horas | 7 días | 12 meses |
| 4 | Pila Lodo Agroindustrial - Edad 3a | Difusa | 1.200,00 | 1,6 | 1.920,00 | Continuo | 24 horas | 7 días | 12 meses |
| 5 | Pila Lodo Agroindustrial - Edad 3b | Difusa | 1.200,00 | 1,6 | 1.920,00 | Continuo | 24 horas | 7 días | 12 meses |
| 6 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 3.457,00 | 5,7 | 19.704,90 | Continuo | 24 horas | 7 días | 12 meses |
| 7 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 10.371,00 | 3,8 | 39.409,80 | Continuo | 24 horas | 7 días | 12 meses |
| 8 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 2.078,75 | 11,4 | 23.697,75 | Continuo | 24 horas | 7 días | 12 meses |
| 9 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 6.236,25 | 5,9 | 36.793,88 | Continuo | 24 horas | 7 días | 12 meses |
| 10 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 1.126,50 | 5,7 | 6.421,05 | Continuo | 24 horas | 7 días | 12 meses |
| 11 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 3.379,50 | 3,8 | 12.842,10 | Continuo | 24 horas | 7 días | 12 meses |
| 12 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 970,25 | 11,4 | 11.060,85 | Continuo | 24 horas | 7 días | 12 meses |
| 13 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 2.910,75 | 5,9 | 17.173,43 | Continuo | 24 horas | 7 días | 12 meses |
| 14 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 1.063,00 | 5,7 | 6.059,10 | Continuo | 24 horas | 7 días | 12 meses |

**Tabla 50: - Situación actual: Características operacionales de fuentes emisoras (parte 2)**

| ID | Fuente | Tipo de<br>fuente | Área<br>[m2] | EO por<br>sup.<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E | Ciclo de<br>operación | Horas de<br>operación | Días de<br>operación | Meses de<br>operación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 3.189,00 | 3,8 | 12.118,20 | Continuo | 24 horas | 7 días | 12 meses |
| 16 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 1.220,50 | 11,4 | 13.913,70 | Continuo | 24 horas | 7 días | 12 meses |
| 17 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 3.661,50 | 5,9 | 21.602,85 | Continuo | 24 horas | 7 días | 12 meses |
| 18 | Pila lodo sanitario - Edad 3 Curicó | Difusa | 639,25 | 5,6 | 3.579,80 | Continuo | 24 horas | 7 días | 12 meses |
| 19 | Pila lodo sanitario - Edad 3 Otras Localidades | Difusa | 1.917,75 | 1,7 | 3.260,18 | Continuo | 24 horas | 7 días | 12 meses |
| 20 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 335,75 | 5,7 | 1.913,78 | Continuo | 24 horas | 7 días | 12 meses |
| 21 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 1.007,25 | 3,8 | 3.827,55 | Continuo | 24 horas | 7 días | 12 meses |
| 22 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 378,25 | 11,4 | 4.312,05 | Continuo | 24 horas | 7 días | 12 meses |
| 23 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 1.134,75 | 5,9 | 6.695,03 | Continuo | 24 horas | 7 días | 12 meses |
| 24 | Pila lodo sanitario - Edad 1 Curicó | Difusa | 1.990,75 | 5,7 | 11.347,28 | Continuo | 24 horas | 7 días | 12 meses |
| 25 | Pila lodo sanitario - Edad 1 Otras Localidades | Difusa | 5.972,25 | 3,8 | 22.694,55 | Continuo | 24 horas | 7 días | 12 meses |
| 26 | Pila lodo sanitario - Edad 2 Curicó | Difusa | 1.754,25 | 11,4 | 19.998,45 | Continuo | 24 horas | 7 días | 12 meses |
| 27 | Pila lodo sanitario - Edad 2 Otras Localidades | Difusa | 5.262,75 | 5,9 | 31.050,23 | Continuo | 24 horas | 7 días | 12 meses |
| 28 | Pila lodo sanitario - Edad 3 Curicó | Difusa | 520,25 | 5,6 | 2.913,40 | Continuo | 24 horas | 7 días | 12 meses |
| 29 | Pila lodo sanitario - Edad 3 Otras Localidades | Difusa | 1.560,75 | 1,7 | 2.653,28 | Continuo | 24 horas | 7 días | 12 meses |
| 30 | Laguna de percolados | Difusa | 1.000,00 | 81,6 | 81.600,00 | Continuo | 24 horas | 7 días | 12 meses |
| 31 | Laguna de agua rechazo | Difusa | 154,00 | 81,6 | 12.566,40 | Continuo | 24 horas | 7 días | 12 meses |
| 32 | Reactor aerobio 1 | Difusa | 78,54 | 31,8 | 2.497,57 | Continuo | 24 horas | 7 días | 12 meses |
| 33 | Reactor aerobio 2 | Difusa | 78,54 | 31,8 | 2.497,57 | Continuo | 24 horas | 7 días | 12 meses |
| 34 | Clarificador | Difusa | 24,20 | 14,2 | 343,64 | Continuo | 24 horas | 7 días | 12 meses |
| 35 | Floculador | Difusa | 7,07 | 14,2 | 100,37 | Continuo | 24 horas | 7 días | 12 meses |
| 36 | Laguna lodos biológicos | Difusa | 67,60 | 21,2 | 1.433,12 | Continuo | 24 horas | 7 días | 12 meses |
| 37 | Laguna lodo físico/químico | Difusa | 61,20 | 2,3 | 140,76 | Continuo | 24 horas | 7 días | 12 meses |
| 38 | Lechos de secado 1 | Difusa | 302,00 | 4,2 | 1.268,40 | Continuo | 24 horas | 7 días | 12 meses |
| 39 | Lechos de secado 2 (lavado de camiones) | Difusa | 267,00 | 32,8 | 8.757,60 | Continuo | 24 horas | 7 días | 12 meses |
| 40 | Laguna agua tratada | Difusa | 377,00 | 2,4 | 904,80 | Continuo | 24 horas | 7 días | 12 meses |
| 41 | Monorelleno - Frente de trabajo | Difusa | 4.508,00 | 11,1 | 50.038,80 | Continuo | 24 horas | 7 días | 12 meses |
| 42 | Relleno Sanitario - Frente de trabajo | Difusa | 850,00 | 21,3 | 18.105,00 | Continuo | 24 horas | 7 días | 12 meses |

**Tabla 51: - Situación futura: Características operacionales de fuentes emisoras (parte 1)**

| ID | Fuente | Tipo de<br>fuente | Área [m2] | EO por<br>sup.<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E | Ciclo de<br>operación | Horas de<br>operación | Días de<br>operación | Meses de<br>operación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cancha de compostaje 1 | Difusa | 10.040,00 | 0,53 | 5.283,75 | Continuo | 24 horas | 7 días | 12 meses |
| 2 | Cancha de compostaje 2 | Difusa | 4.960,00 | 0,53 | 2.610,30 | Continuo | 24 horas | 7 días | 12 meses |
| 3 | Cancha de compostaje 3 | Difusa | 14.140,00 | 0,53 | 7.441,46 | Continuo | 24 horas | 7 días | 12 meses |
| 4 | Cancha de compostaje 4 | Difusa | 16.000,00 | 0,53 | 8.420,32 | Continuo | 24 horas | 7 días | 12 meses |
| 5 | Galpón de compostaje 1 (sistema de abatimiento) | Puntual | 1,13 | 1128,86 | 1.276,71 | Continuo | 24 horas | 7 días | 12 meses |
| 6 | Galpón de compostaje 2 (sistema de abatimiento) | Puntual | 1,13 | 1438,43 | 1.626,82 | Continuo | 24 horas | 7 días | 12 meses |
| 7 | Galpón de compostaje 3 (sistema de abatimiento) | Puntual | 1,13 | 1438,43 | 1.626,82 | Continuo | 24 horas | 7 días | 12 meses |
| 8 | Galpón de compostaje 4 (sistema de abatimiento) | Puntual | 1,13 | 1438,43 | 1.626,82 | Continuo | 24 horas | 7 días | 12 meses |
| 9 | Estanque acumulación clarificado - Etapa 1 | Difusa | 201,06 | 0,32 | 64,34 | Continuo | 24 horas | 7 días | 12 meses |
| 10 | Estanque acumulación de digestato - Etapa 1 | Difusa | 9,19 | 0,32 | 2,94 | Continuo | 24 horas | 7 días | 12 meses |
| 11 | Contenedor deshidratado mecánico - Etapa 1 | Difusa | 12,72 | 0,32 | 4,07 | Continuo | 24 horas | 7 días | 12 meses |
| 12 | Estanque acumulación clarificado - Etapa 2 | Difusa | 201,06 | 0,32 | 64,34 | Continuo | 24 horas | 7 días | 12 meses |
| 13 | Contenedor deshidratado mecánico - Etapa 2 | Difusa | 12,72 | 0,32 | 4,07 | Continuo | 24 horas | 7 días | 12 meses |
| 14 | Sistema de abatimiento olores - Etapa 1 | Puntual | 1,13 | 47,23 | 53,42 | Continuo | 24 horas | 7 días | 12 meses |
| 15 | Sistema de abatimiento olores - Etapa 2 | Puntual | 1,13 | 47,23 | 53,42 | Continuo | 24 horas | 7 días | 12 meses |
| 16 | Unidad de almacenamiento de digestato | Difusa | 5.329,00 | 0,32 | 1.705,28 | Continuo | 24 horas | 7 días | 12 meses |
| 17 | Laguna anaeróbica | Puntual | 2.000,00 | 5,71 | 11.424,00 | Continuo | 24 horas | 7 días | 12 meses |
| 18 | Laguna de percolados | Puntual | 1.000,00 | 5,71 | 5.710,00 | Continuo | 24 horas | 7 días | 12 meses |
| 19 | Reactor aerobio 1 | Puntual | 78,54 | 19,08 | 1.498,54 | Continuo | 24 horas | 7 días | 12 meses |

**Tabla 52: - Situación futura: Características operacionales de fuentes emisoras (parte 2)**

| ID | Fuente | Tipo de<br>fuente | Área [m2] | EO por<br>sup.<br>[ou/m2s]<br>E | Tasa de<br>Emisión de<br>Olor<br>[ou/s]<br>E | Ciclo de<br>operación | Horas de<br>operación | Días de<br>operación | Meses de<br>operación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | Reactor aerobio 2 | Difusa | 78,54 | 19,08 | 1.498,54 | Continuo | 24 horas | 7 días | 12 meses |
| 21 | Reactor aerobio 3 | Difusa | 78,54 | 19,08 | 1.498,54 | Continuo | 24 horas | 7 días | 12 meses |
| 22 | Reactor aerobio 4 | Difusa | 78,54 | 19,08 | 1.498,54 | Continuo | 24 horas | 7 días | 12 meses |
| 23 | Clarificador | Difusa | 24,20 | 8,52 | 206,18 | Continuo | 24 horas | 7 días | 12 meses |
| 24 | Floculador | Difusa | 7,07 | 8,52 | 60,22 | Continuo | 24 horas | 7 días | 12 meses |
| 25 | Laguna lodos biológicos | Difusa | 67,60 | 21,2 | 1.433,12 | Continuo | 24 horas | 7 días | 12 meses |
| 26 | Laguna lodo físico/químico | Difusa | 61,20 | 2,3 | 140,76 | Continuo | 24 horas | 7 días | 12 meses |
| 27 | Laguna agua tratada | Difusa | 377,00 | 0,25 | 94,25 | Continuo | 24 horas | 7 días | 12 meses |
| 28 | Alvéolo 7 - Frente de trabajo | Difusa | 850,00 | 21,30 | 18.105,00 | Continuo | 24 horas | 7 días | 12 meses |
| 29 | Zona de riego 1 | Difusa | 13.180,00 | 0,32 | 4.217,60 | Continuo | 9 horas | 7 días | Sept.- Abril |
| 30 | Zona de riego 2 | Difusa | 17.906,11 | 0,32 | 5.729,96 | Continuo | 9 horas | 7 días | Sept.- Abril |

**Tabla 53: - Coordenada central Centro de Tratamiento de Residuos**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| X: Este | Y: Sur | Huso | Datum |
| 282.341 | 6.101.435 | 19 H | WGS 84 |

**Tabla 54: - Distribución de rosas de viento anual horaria**

| Col1 | Rosa de vientos | Col3 | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- |
| Anual Nocturno<br>(00:00 a 6:59 horas) |  |  | <br>8,41<br>14,21<br>40,39<br>22,27<br>9,67<br>3,41<br>1,02<br>0,47<br>0,12<br>0,04<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de vientos predominaron desde la<br>dirección SO con un 44% de la frecuencia.<br>La velocidad varió de ventolina54 a brisa débil. La<br>distribución del viento tuvo una tendencia<br>asimétrica positiva. <br> <br>Velocidad promedio de viento: 1,84 [m/s].<br> <br>Frecuencia de vientos calmos: 8,41%. |
| Anual AM<br>(7:00 a 14:59 horas) |  |  | <br>5,17<br>8,87<br>23,66<br>30,96<br>20,00<br>7,09<br>2,60<br>1,30<br>0,27<br>0,07<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron en mayor<br>frecuencia desde el rango SSO-SO, con un 65%<br>de la frecuencia.<br>La velocidad varió de ventolina a brisa<br>moderada55.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,45 [m/s].<br> <br>Frecuencia de vientos calmos: 5,17%. |
| Anual PM<br>(15:00 a 23:59 horas) |  |  | <br>6,42<br>11,51<br>30,41<br>23,38<br>15,31<br>7,06<br>3,90<br>1,43<br>0,33<br>0,24<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario PM, se observó una<br>predominancia de los vientos desde el rango<br>SSO-SO, con un 54% de la frecuencia. La<br>velocidad de los vientos varió de ventolina a brisa<br>moderada56.<br>La distribución de los vientos se observó con una<br>tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,31 [m/s]<br> <br>Frecuencia de vientos calmos: 6,42% |

**Tabla 55: - Coordenadas representativas de Centro de Tratamiento de Residuos**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| X: Este | Y: Sur | Huso | Datum |
| 282.341 | 6.101.435 | 19 Sur | WGS-84 |

**Tabla 56: - Descripción de ciclos de análisis meteorológicos**

| Ciclo | Descripción | Col3 |
| --- | --- | --- |
| Anual | 12 meses | Enero a diciembre |
| Estacional | Verano | 22 de diciembre a 21 de marzo |
| Estacional | Otoño | 22 de marzo a 21 de junio |
| Estacional | Invierno | 22 de junio a 21 de septiembre |
| Estacional | Primavera | 22 de septiembre a 21 de diciembre |
| Horario | Nocturno | 00:00 a 06:59 |
| Horario | AM | 07:00 a 14:59 |
| Horario | PM | 15:00 a 23:59 |

**Tabla 57: - Rosas y campos de viento pronóstico anual**

| Col1 | Rosa de vientos | Col3 | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- |
| Anual Nocturno |  |  | <br>8,41<br>14,21<br>40,39<br>22,27<br>9,67<br>3,41<br>1,02<br>0,47<br>0,12<br>0,04<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de vientos predominaron desde la<br>dirección SO con un 44% de la frecuencia anual.<br>La velocidad varió de ventolina57 a brisa débil. La<br>distribución del viento tuvo un comportamiento<br>asimétrico positivo. <br> <br>Velocidad promedio de viento: 1,84 [m/s].<br> <br>Frecuencia de vientos calmos: 8,41%. |
| Anual AM |  |  | <br>5,17<br>8,87<br>23,66<br>30,96<br>20,00<br>7,09<br>2,60<br>1,30<br>0,27<br>0,07<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron en mayor<br>frecuencia desde el rango SO-SSO, con un 65%<br>de la frecuencia.<br>La velocidad varió de ventolina a brisa débil58.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia a la normalidad.<br> <br>Velocidad promedio de viento: 2,45 [m/s].<br> <br>Frecuencia de vientos calmos: 5,17%. |
| Anual PM |  |  | <br>6,42<br>11,51<br>30,41<br>23,38<br>15,31<br>7,06<br>3,90<br>1,43<br>0,33<br>0,24<br>0<br>10<br>20<br>30<br>40<br>50<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario PM, se observó una<br>predominancia de los vientos desde el rango<br>SSO-SO con un 54% de la frecuencia. La<br>velocidad de los vientos varió de ventolina a brisa<br>débil59.<br>La distribución de los vientos se observó con una<br>tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,31 [m/s]<br> <br>Frecuencia de vientos calmos: 6,42% |

**Tabla 58: - Rosas y campos de viento pronóstico estacional - Verano**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Verano Nocturno |  |  |  | 6,03<br>12,22<br>53,17<br>19,52<br>6,67<br>1,90<br>0,32<br>0,16<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | El viento predominó desde la componente SO,<br>con un 52% de la frecuencia. En general, la<br>intensidad del viento se caracterizó por variar<br>de ventolina a brisa muy débil.<br>La distribución de frecuencia de velocidad del<br>presentó una asimetría positiva. <br> <br>Promedio velocidad del viento: 1,72 [m/s].<br> <br>Frecuencia de vientos calmos: 6,03%. |
| Verano AM |  |  |  | 3,33<br>6,67<br>21,25<br>34,58<br>25,97<br>5,28<br>1,25<br>1,39<br>0,28<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron con mayor<br>frecuencia desde el rango SSO-SO, con un 74%<br>de la frecuencia. La velocidad del viento varió<br>de brisa muy débil a débil. La distribución<br>presento una asimetría positiva.<br> <br>Promedio velocidad del viento: 2,55 [m/s].<br> <br>Frecuencia de vientos calmos: 3,33%. |
| Verano PM |  |  |  | 5,68<br>7,53<br>28,27<br>26,67<br>21,85<br>5,06<br>3,21<br>1,36<br>0,37<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de viento predominaron desde la<br>componente SSO y SO, con un 34% y 23% de<br>la frecuencia respectivamente. La intensidad<br>del viento fluctuó de brisa muy débil a<br>moderada. La curva de distribución tuvo una<br>tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,42 [m/s].<br> <br>Frecuencia de vientos calmos: 5,68%. |

**Tabla 59: - Rosas y campos de viento pronóstico estacional - Otoño**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Otoño Nocturno |  |  |  | 10,56<br>16,15<br>39,91<br>23,29<br>7,61<br>1,71<br>0,62<br>0,16<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de viento provinieron con mayor<br>frecuencia desde la componente SO con un<br>33% de predominancia. La intensidad del<br>viento varió mayormente de calmos a brisa muy<br>débil<br>La distribución de frecuencia de velocidad del<br>viento muestra una tendencia asimétrica<br>positiva. <br> <br>Promedio velocidad del viento: 1,66 [m/s].<br> <br>Frecuencia de vientos calmos: 10,56%. |
| Otoño AM |  |  |  | 6,79<br>11,68<br>31,11<br>29,89<br>13,18<br>4,62<br>1,49<br>0,68<br>0,27<br>0,27<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | El viento presentó una predominancia desde las<br>componentes SO y SSO con un 35% y 23% de<br>la frecuencia respectivamente. La intensidad<br>del viento fluctuó de ventolina a brisa muy<br>débil.<br>Respecto a la distribución, ésta tuvo una<br>tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,13 [m/s].<br> <br>Frecuencia de vientos calmos: 6,79%. |
| Otoño PM |  |  |  | 9,06<br>18,00<br>36,72<br>20,41<br>8,33<br>3,99<br>1,69<br>0,97<br>0,00<br>0,85<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron en mayor<br>frecuencia desde el componente SO y SSO con<br>un<br>25%<br>y <br>17%<br>de<br>la<br>frecuencia<br>respectivamente. En general, la velocidad del<br>viento varió de ventolina a brisa muy débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo un comportamiento asimétrico<br>positivo. <br> <br>Promedio velocidad del viento: 1,88 [m/s].<br> <br>Frecuencia de vientos calmos: 9,06%. |

**Tabla 60: - Rosas y campos de viento pronóstico estacional - Invierno**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Invierno Nocturno |  |  |  | 6,68<br>14,75<br>32,30<br>18,94<br>12,73<br>9,32<br>3,11<br>1,55<br>0,47<br>0,16<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario nocturno los vientos<br>provinieron mayormente desde la componente<br>SO con un 36% de la frecuencia. La intensidad<br>del viento osciló de ventolina a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,23 [m/s].<br> <br>Frecuencia de vientos calmos: 6,68%. |
| Invierno AM |  |  |  | 7,20<br>10,33<br>21,47<br>28,13<br>17,39<br>8,70<br>3,67<br>2,58<br>0,54<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron mayormente del<br>rango SSO-SO con un 54% de la frecuencia. La<br>velocidad fluctuó de ventolina a brisa débil.<br>La<br>intensidad<br>del<br>viento<br>presentó<br>una<br>distribución mesocúrtica. <br> <br>Promedio velocidad del viento: 2,51 [m/s].<br> <br>Frecuencia de vientos calmos: 7,2%. |
| Invierno PM |  |  |  | 6,16<br>11,96<br>32,37<br>18,00<br>14,37<br>7,85<br>5,92<br>2,42<br>0,85<br>0,12<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de vientos provinieron con mayor<br>frecuencia desde la componente SO con un<br>35% de la frecuencia. En general, la intensidad<br>del viento varió de ventolina a brisa débil y la<br>distribución presentó una tendencia asimétrica<br>positiva.<br> <br>Promedio velocidad del viento: 2,42 [m/s].<br> <br>Frecuencia de vientos calmos: 6,16%. |

**Tabla 61: - Rosas y campos de viento pronóstico estacional - Primavera**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Primavera Nocturno |  |  |  | 10,36<br>13,66<br>36,42<br>27,32<br>11,62<br>0,63<br>0,00<br>0,00<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Predominio de los vientos desde la componente<br>SO con un 56% de la frecuencia. La velocidad<br>del viento fluctuó de calmo a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica negativa. <br> <br>Promedio velocidad del viento: 1,75 [m/s].<br> <br>Frecuencia de vientos calmos: 10,36%. |
| Primavera AM |  |  |  | 3,30<br>6,73<br>20,74<br>31,32<br>23,63<br>9,75<br>3,98<br>0,55<br>0,00<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron el rango SSO-SO<br>con un 73% de la frecuencia. La velocidad del<br>viento osciló de ventolina a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento exhibió una curva mesocurtica. <br> <br>Promedio velocidad del viento: 2,64 [m/s].<br> <br>Frecuencia de vientos calmos: 3,3%. |
| Primavera PM |  | <br> |  | <br>4,76<br>8,42<br>24,18<br>28,57<br>16,85<br>11,36<br>4,76<br>0,98<br>0,12<br>0,00<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario PM, los vientos provinieron<br>desde el rango SSO-SO con un 61% de la<br>frecuencia. La velocidad del viento osciló de<br>ventolina a brisa débil.<br>La distribución de frecuencia de velocidad del<br>viento exhibió una curva mesocurtica. <br> <br>Promedio velocidad del viento: 2,54 [m/s].<br> <br>Frecuencia de vientos calmos: 4,76%. |

**Tabla 64: - Estaciones meteorológicas superficiales en el dominio de modelación WRF**

| ID | Nombre estación | Coordenadas geográficas UTM<br>Huso 19 | Col4 | Datos válidos % | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| ID | Nombre estación | Este [m] | Sur [m] | Temperatura | Velocidad<br>viento | Dirección<br>viento |
| 1 | U. C. del Maule68 | 262.216 | 6.075.477 | 99,19 | 88,34 | 98,97 |
| 2 | Tres Esquinas69 | 298.116 | 6.108.659 | 82,19 | 44,22 | 49,81 |
| 3 | Aresti70 | 290.666 | 6.107.751 | 98,53 | 65,88 | 0,0 |
| 4 | San Rafael71 | 274.890 | 6.090.475 | 87,21 | 42,83 | 73,76 |

**Tabla 65: - Coordenada de localización, serie de pronóstico WRF**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Este | Sur | Huso | Datum |
| 262.216 | 6.075.477 | 19 Sur | WGS 84 |

**Tabla 66: - Coordenada de localización estación meteorológica**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Este | Sur | Huso | Datum |
| 262.216 | 6.075.477 | 19 Sur | WGS 84 |

**Tabla 67: - Porcentaje datos válidos en parámetros evaluados**

| Parámetro meteorológico<br>evaluado | % datos válidos | Cumple con<br>recomendación SEA<br>(>75%) |
| --- | --- | --- |
| Velocidad del viento [m/s]<br>Dirección del viento [°]<br>Temperatura [°C] | 88,3<br>99,0<br>99,2 | <br><br> |

**Tabla 68: - Ciclos diarios de la temperatura - serie pronóstico**

| Hora | Promedio de<br>Temperatura [°C] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 11,03<br>4,31<br>17,24<br>10,51<br>4,11<br>16,41<br>10,06<br>3,54<br>15,76<br>9,70<br>3,44<br>14,99<br>9,38<br>3,45<br>14,45<br>9,05<br>3,34<br>14,38<br>8,72<br>3,01<br>14,07<br>8,92<br>2,75<br>14,34<br>9,64<br>2,77<br>15,85<br>10,75<br>3,10<br>17,91<br>12,20<br>3,81<br>19,69<br>13,87<br>4,60<br>21,70<br>15,58<br>5,95<br>23,58<br>17,04<br>8,01<br>25,17<br>18,14<br>9,36<br>26,41<br>18,76<br>9,83<br>27,23<br>18,84<br>9,70<br>27,57<br>18,42<br>8,96<br>27,63<br>17,16<br>7,84<br>26,94<br>15,32<br>7,03<br>24,72<br>13,78<br>6,29<br>22,00<br>13,03<br>5,78<br>20,53<br>12,36<br>5,30<br>19,31<br>11,58<br>4,92<br>18,35 | 11,03<br>4,31<br>17,24<br>10,51<br>4,11<br>16,41<br>10,06<br>3,54<br>15,76<br>9,70<br>3,44<br>14,99<br>9,38<br>3,45<br>14,45<br>9,05<br>3,34<br>14,38<br>8,72<br>3,01<br>14,07<br>8,92<br>2,75<br>14,34<br>9,64<br>2,77<br>15,85<br>10,75<br>3,10<br>17,91<br>12,20<br>3,81<br>19,69<br>13,87<br>4,60<br>21,70<br>15,58<br>5,95<br>23,58<br>17,04<br>8,01<br>25,17<br>18,14<br>9,36<br>26,41<br>18,76<br>9,83<br>27,23<br>18,84<br>9,70<br>27,57<br>18,42<br>8,96<br>27,63<br>17,16<br>7,84<br>26,94<br>15,32<br>7,03<br>24,72<br>13,78<br>6,29<br>22,00<br>13,03<br>5,78<br>20,53<br>12,36<br>5,30<br>19,31<br>11,58<br>4,92<br>18,35 | 11,03<br>4,31<br>17,24<br>10,51<br>4,11<br>16,41<br>10,06<br>3,54<br>15,76<br>9,70<br>3,44<br>14,99<br>9,38<br>3,45<br>14,45<br>9,05<br>3,34<br>14,38<br>8,72<br>3,01<br>14,07<br>8,92<br>2,75<br>14,34<br>9,64<br>2,77<br>15,85<br>10,75<br>3,10<br>17,91<br>12,20<br>3,81<br>19,69<br>13,87<br>4,60<br>21,70<br>15,58<br>5,95<br>23,58<br>17,04<br>8,01<br>25,17<br>18,14<br>9,36<br>26,41<br>18,76<br>9,83<br>27,23<br>18,84<br>9,70<br>27,57<br>18,42<br>8,96<br>27,63<br>17,16<br>7,84<br>26,94<br>15,32<br>7,03<br>24,72<br>13,78<br>6,29<br>22,00<br>13,03<br>5,78<br>20,53<br>12,36<br>5,30<br>19,31<br>11,58<br>4,92<br>18,35 |

**Tabla 69: - Ciclos diarios de la temperatura - serie observada**

| Hora | Promedio de<br>temperatura [°C] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 12,14<br>4,16<br>19,91<br>11,50<br>3,57<br>18,72<br>10,91<br>3,53<br>17,93<br>10,36<br>3,26<br>17,14<br>9,89<br>2,97<br>16,31<br>9,48<br>2,35<br>15,60<br>9,51<br>1,84<br>15,78<br>10,36<br>1,81<br>18,15<br>11,70<br>2,79<br>20,05<br>13,46<br>3,74<br>22,97<br>15,37<br>5,52<br>25,02<br>17,21<br>6,97<br>27,07<br>18,93<br>8,94<br>28,96<br>20,40<br>10,28<br>30,79<br>21,20<br>10,78<br>31,61<br>21,64<br>10,84<br>32,47<br>21,47<br>10,69<br>32,63<br>20,62<br>10,01<br>32,35<br>19,08<br>8,54<br>31,43<br>17,33<br>7,47<br>28,89<br>15,83<br>6,54<br>25,76<br>14,68<br>5,94<br>23,84<br>13,73<br>5,44<br>22,09<br>12,90<br>4,71<br>20,85 | 12,14<br>4,16<br>19,91<br>11,50<br>3,57<br>18,72<br>10,91<br>3,53<br>17,93<br>10,36<br>3,26<br>17,14<br>9,89<br>2,97<br>16,31<br>9,48<br>2,35<br>15,60<br>9,51<br>1,84<br>15,78<br>10,36<br>1,81<br>18,15<br>11,70<br>2,79<br>20,05<br>13,46<br>3,74<br>22,97<br>15,37<br>5,52<br>25,02<br>17,21<br>6,97<br>27,07<br>18,93<br>8,94<br>28,96<br>20,40<br>10,28<br>30,79<br>21,20<br>10,78<br>31,61<br>21,64<br>10,84<br>32,47<br>21,47<br>10,69<br>32,63<br>20,62<br>10,01<br>32,35<br>19,08<br>8,54<br>31,43<br>17,33<br>7,47<br>28,89<br>15,83<br>6,54<br>25,76<br>14,68<br>5,94<br>23,84<br>13,73<br>5,44<br>22,09<br>12,90<br>4,71<br>20,85 | 12,14<br>4,16<br>19,91<br>11,50<br>3,57<br>18,72<br>10,91<br>3,53<br>17,93<br>10,36<br>3,26<br>17,14<br>9,89<br>2,97<br>16,31<br>9,48<br>2,35<br>15,60<br>9,51<br>1,84<br>15,78<br>10,36<br>1,81<br>18,15<br>11,70<br>2,79<br>20,05<br>13,46<br>3,74<br>22,97<br>15,37<br>5,52<br>25,02<br>17,21<br>6,97<br>27,07<br>18,93<br>8,94<br>28,96<br>20,40<br>10,28<br>30,79<br>21,20<br>10,78<br>31,61<br>21,64<br>10,84<br>32,47<br>21,47<br>10,69<br>32,63<br>20,62<br>10,01<br>32,35<br>19,08<br>8,54<br>31,43<br>17,33<br>7,47<br>28,89<br>15,83<br>6,54<br>25,76<br>14,68<br>5,94<br>23,84<br>13,73<br>5,44<br>22,09<br>12,90<br>4,71<br>20,85 |

**Tabla 70: - Ciclos diarios promedios serie pronóstico**

| Hora | Promedio velocidad<br>del viento [m/s] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 1,14<br>0,21<br>2,69<br>1,11<br>0,14<br>2,88<br>1,13<br>0,16<br>2,97<br>1,17<br>0,12<br>3,29<br>1,15<br>0,08<br>3,18<br>1,12<br>0,14<br>3,16<br>1,09<br>0,09<br>3,12<br>1,15<br>0,09<br>3,22<br>1,37<br>0,07<br>3,66<br>1,51<br>0,08<br>3,92<br>1,61<br>0,14<br>4,16<br>1,64<br>0,18<br>4,21<br>1,72<br>0,18<br>4,29<br>1,84<br>0,22<br>4,33<br>1,92<br>0,28<br>4,40<br>1,99<br>0,29<br>4,43<br>2,02<br>0,39<br>4,24<br>1,86<br>0,22<br>4,28<br>1,56<br>0,10<br>3,92<br>1,41<br>0,19<br>3,48<br>1,30<br>0,21<br>3,16<br>1,28<br>0,23<br>3,09<br>1,23<br>0,22<br>2,82<br>1,16<br>0,17<br>2,89 | 1,14<br>0,21<br>2,69<br>1,11<br>0,14<br>2,88<br>1,13<br>0,16<br>2,97<br>1,17<br>0,12<br>3,29<br>1,15<br>0,08<br>3,18<br>1,12<br>0,14<br>3,16<br>1,09<br>0,09<br>3,12<br>1,15<br>0,09<br>3,22<br>1,37<br>0,07<br>3,66<br>1,51<br>0,08<br>3,92<br>1,61<br>0,14<br>4,16<br>1,64<br>0,18<br>4,21<br>1,72<br>0,18<br>4,29<br>1,84<br>0,22<br>4,33<br>1,92<br>0,28<br>4,40<br>1,99<br>0,29<br>4,43<br>2,02<br>0,39<br>4,24<br>1,86<br>0,22<br>4,28<br>1,56<br>0,10<br>3,92<br>1,41<br>0,19<br>3,48<br>1,30<br>0,21<br>3,16<br>1,28<br>0,23<br>3,09<br>1,23<br>0,22<br>2,82<br>1,16<br>0,17<br>2,89 | 1,14<br>0,21<br>2,69<br>1,11<br>0,14<br>2,88<br>1,13<br>0,16<br>2,97<br>1,17<br>0,12<br>3,29<br>1,15<br>0,08<br>3,18<br>1,12<br>0,14<br>3,16<br>1,09<br>0,09<br>3,12<br>1,15<br>0,09<br>3,22<br>1,37<br>0,07<br>3,66<br>1,51<br>0,08<br>3,92<br>1,61<br>0,14<br>4,16<br>1,64<br>0,18<br>4,21<br>1,72<br>0,18<br>4,29<br>1,84<br>0,22<br>4,33<br>1,92<br>0,28<br>4,40<br>1,99<br>0,29<br>4,43<br>2,02<br>0,39<br>4,24<br>1,86<br>0,22<br>4,28<br>1,56<br>0,10<br>3,92<br>1,41<br>0,19<br>3,48<br>1,30<br>0,21<br>3,16<br>1,28<br>0,23<br>3,09<br>1,23<br>0,22<br>2,82<br>1,16<br>0,17<br>2,89 |

**Tabla 71: - Ciclos diarios promedios serie observada**

| Hora | Promedio velocidad<br>del viento [m/s] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 1,07<br>0,20<br>2,45<br>1,07<br>0,20<br>2,55<br>1,06<br>0,25<br>2,53<br>1,01<br>0,23<br>2,45<br>1,01<br>0,19<br>2,28<br>1,00<br>0,18<br>2,41<br>1,10<br>0,23<br>2,41<br>1,36<br>0,31<br>2,74<br>1,52<br>0,30<br>2,89<br>1,62<br>0,38<br>3,17<br>1,66<br>0,42<br>3,27<br>1,77<br>0,42<br>3,46<br>1,86<br>0,40<br>3,60<br>1,89<br>0,47<br>3,57<br>2,00<br>0,56<br>3,74<br>2,08<br>0,75<br>3,85<br>2,08<br>0,79<br>3,63<br>1,93<br>0,47<br>3,39<br>1,61<br>0,22<br>3,04<br>1,37<br>0,20<br>2,86<br>1,28<br>0,20<br>2,58<br>1,21<br>0,24<br>2,57<br>1,16<br>0,21<br>2,49<br>1,11<br>0,21<br>2,32 | 1,07<br>0,20<br>2,45<br>1,07<br>0,20<br>2,55<br>1,06<br>0,25<br>2,53<br>1,01<br>0,23<br>2,45<br>1,01<br>0,19<br>2,28<br>1,00<br>0,18<br>2,41<br>1,10<br>0,23<br>2,41<br>1,36<br>0,31<br>2,74<br>1,52<br>0,30<br>2,89<br>1,62<br>0,38<br>3,17<br>1,66<br>0,42<br>3,27<br>1,77<br>0,42<br>3,46<br>1,86<br>0,40<br>3,60<br>1,89<br>0,47<br>3,57<br>2,00<br>0,56<br>3,74<br>2,08<br>0,75<br>3,85<br>2,08<br>0,79<br>3,63<br>1,93<br>0,47<br>3,39<br>1,61<br>0,22<br>3,04<br>1,37<br>0,20<br>2,86<br>1,28<br>0,20<br>2,58<br>1,21<br>0,24<br>2,57<br>1,16<br>0,21<br>2,49<br>1,11<br>0,21<br>2,32 | 1,07<br>0,20<br>2,45<br>1,07<br>0,20<br>2,55<br>1,06<br>0,25<br>2,53<br>1,01<br>0,23<br>2,45<br>1,01<br>0,19<br>2,28<br>1,00<br>0,18<br>2,41<br>1,10<br>0,23<br>2,41<br>1,36<br>0,31<br>2,74<br>1,52<br>0,30<br>2,89<br>1,62<br>0,38<br>3,17<br>1,66<br>0,42<br>3,27<br>1,77<br>0,42<br>3,46<br>1,86<br>0,40<br>3,60<br>1,89<br>0,47<br>3,57<br>2,00<br>0,56<br>3,74<br>2,08<br>0,75<br>3,85<br>2,08<br>0,79<br>3,63<br>1,93<br>0,47<br>3,39<br>1,61<br>0,22<br>3,04<br>1,37<br>0,20<br>2,86<br>1,28<br>0,20<br>2,58<br>1,21<br>0,24<br>2,57<br>1,16<br>0,21<br>2,49<br>1,11<br>0,21<br>2,32 |

**Tabla 72: - Ciclos diarios de dirección del viento serie pronóstico**

| Col1 | Dirección del viento [grados] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hora<br>del día | 0-20 | 20-40 | 40-60 | 60-80 | 80-100 | 100-120 | 120-140 | 140-160 | 160-180 | 180-200 | 200-220 | 220-240 | 240-260 | 260-280 | 280-300 | 300-320 | 320-340 | 340-360 |
| 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 | 00:00<br>8 <br>12<br>26<br>32<br>19<br>7 <br>7 <br>10<br>16<br>21<br>104<br>61<br>15<br>4 <br>5 <br>3 <br>6 <br>8 <br>01:00<br>10<br>19<br>23<br>39<br>18<br>11<br>9 <br>13<br>15<br>31<br>105<br>41<br>10<br>3 <br>1 <br>7 <br>5 <br>5 <br>02:00<br>2 <br>18<br>27<br>29<br>27<br>7 <br>7 <br>13<br>21<br>37<br>108<br>23<br>15<br>4 <br>5 <br>9 <br>6 <br>7 <br>03:00<br>10<br>15<br>32<br>27<br>19<br>12<br>9 <br>19<br>15<br>41<br>115<br>15<br>11<br>5 <br>7 <br>4 <br>5 <br>4 <br>04:00<br>6 <br>20<br>30<br>27<br>22<br>9 <br>9 <br>13<br>22<br>48<br>112<br>12<br>12<br>3 <br>9 <br>7 <br>3 <br>1 <br>05:00<br>6 <br>25<br>37<br>29<br>13<br>18<br>9 <br>15<br>24<br>61<br>89<br>8 <br>12<br>6 <br>3 <br>7 <br>2 <br>1 <br>06:00<br>7 <br>26<br>43<br>25<br>11<br>8 <br>10<br>17<br>26<br>75<br>75<br>12<br>4 <br>4 <br>3 <br>6 <br>5 <br>8 |
| 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 | 07:00<br>10<br>26<br>30<br>37<br>11<br>10<br>14<br>11<br>25<br>88<br>74<br>7 <br>6 <br>2 <br>3 <br>5 <br>1 <br>5 <br>08:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>09:00<br>11<br>24<br>31<br>22<br>4 <br>4 <br>5 <br>5 <br>20<br>103<br>92<br>15<br>7 <br>0 <br>2 <br>2 <br>3 <br>15<br>10:00<br>19<br>29<br>37<br>13<br>8 <br>3 <br>1 <br>4 <br>25<br>108<br>88<br>9 <br>3 <br>4 <br>2 <br>2 <br>5 <br>5 <br>11:00<br>24<br>26<br>23<br>11<br>3 <br>3 <br>1 <br>7 <br>29<br>141<br>61<br>11<br>5 <br>3 <br>1 <br>5 <br>4 <br>7 <br>12:00<br>21<br>23<br>13<br>8 <br>4 <br>0 <br>5 <br>10<br>59<br>131<br>50<br>4 <br>6 <br>4 <br>3 <br>8 <br>3 <br>13<br>13:00<br>25<br>17<br>10<br>5 <br>3 <br>1 <br>4 <br>14<br>56<br>135<br>49<br>9 <br>2 <br>2 <br>2 <br>7 <br>8 <br>16<br>14:00<br>18<br>14<br>14<br>2 <br>5 <br>1 <br>6 <br>5 <br>57<br>128<br>50<br>14<br>4 <br>6 <br>3 <br>6 <br>16<br>16 |
| 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 | 15:00<br>14<br>15<br>9 <br>8 <br>3 <br>1 <br>5 <br>7 <br>54<br>119<br>61<br>11<br>3 <br>4 <br>10<br>15<br>11<br>15<br>16:00<br>9 <br>14<br>9 <br>8 <br>3 <br>4 <br>2 <br>10<br>57<br>113<br>65<br>12<br>3 <br>6 <br>13<br>14<br>14<br>9 <br>17:00<br>11<br>9 <br>8 <br>9 <br>3 <br>1 <br>5 <br>10<br>53<br>98<br>62<br>15<br>10<br>15<br>15<br>19<br>12<br>10<br>18:00<br>19<br>16<br>12<br>9 <br>3 <br>5 <br>6 <br>12<br>31<br>70<br>68<br>21<br>12<br>20<br>16<br>20<br>11<br>14<br>19:00<br>29<br>20<br>22<br>8 <br>3 <br>3 <br>3 <br>5 <br>12<br>28<br>67<br>36<br>41<br>42<br>12<br>13<br>8 <br>13<br>20:00<br>18<br>22<br>20<br>15<br>5 <br>5 <br>3 <br>9 <br>7 <br>20<br>71<br>45<br>70<br>21<br>10<br>10<br>6 <br>8 <br>21:00<br>7 <br>21<br>18<br>14<br>9 <br>2 <br>7 <br>4 <br>4 <br>22<br>75<br>74<br>68<br>17<br>6 <br>4 <br>3 <br>10<br>22:00<br>9 <br>11<br>24<br>19<br>7 <br>3 <br>2 <br>9 <br>8 <br>20<br>95<br>83<br>42<br>12<br>4 <br>4 <br>4 <br>9 <br>23:00<br>11<br>15<br>22<br>28<br>10<br>7 <br>8 <br>8 <br>7 <br>26<br>106<br>66<br>22<br>10<br>5 <br>3 <br>2 <br>9 |

**Tabla 73: - Ciclos diarios de dirección del viento serie observada**

| Col1 | Dirección del viento [grados] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hora<br>Del día | 0-20 | 20-40 | 40-60 | 60-80 | 80-100 | 100-120 | 120-140 | 140-160 | 160-180 | 180-200 | 200-220 | 220-240 | 240-260 | 260-280 | 280-300 | 300-320 | 320-340 | 340-360 |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 | 9 <br>16<br>24<br>23<br>13<br>10<br>16<br>10<br>17<br>31<br>115<br>39<br>8 <br>10<br>2 <br>2 <br>8 <br>7 <br>14<br>26<br>19<br>21<br>22<br>11<br>19<br>16<br>19<br>37<br>103<br>27<br>12<br>4 <br>0 <br>1 <br>3 <br>8 <br>20<br>27<br>22<br>25<br>13<br>10<br>15<br>16<br>16<br>40<br>95<br>29<br>9 <br>10<br>2 <br>4 <br>4 <br>7 <br>15<br>35<br>22<br>21<br>8 <br>17<br>11<br>26<br>20<br>61<br>75<br>18<br>9 <br>9 <br>2 <br>5 <br>5 <br>5 <br>20<br>28<br>28<br>29<br>17<br>12<br>16<br>16<br>22<br>63<br>77<br>9 <br>7 <br>4 <br>3 <br>0 <br>7 <br>7 <br>19<br>23<br>42<br>33<br>9 <br>16<br>13<br>22<br>28<br>54<br>60<br>16<br>8 <br>2 <br>6 <br>3 <br>2 <br>9 <br>23<br>32<br>30<br>29<br>16<br>12<br>11<br>25<br>26<br>71<br>52<br>13<br>8 <br>3 <br>1 <br>1 <br>1 <br>10 |
| 07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 | 20<br>30<br>43<br>25<br>12<br>7 <br>15<br>21<br>20<br>92<br>47<br>9 <br>6 <br>1 <br>4 <br>1 <br>2 <br>9 <br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>12<br>28<br>26<br>24<br>10<br>6 <br>8 <br>13<br>43<br>97<br>53<br>13<br>4 <br>4 <br>2 <br>2 <br>2 <br>12<br>10<br>23<br>24<br>19<br>8 <br>11<br>7 <br>23<br>31<br>84<br>67<br>16<br>7 <br>3 <br>2 <br>4 <br>5 <br>14<br>17<br>17<br>18<br>16<br>7 <br>5 <br>8 <br>13<br>40<br>100<br>56<br>14<br>12<br>2 <br>3 <br>5 <br>8 <br>15<br>17<br>17<br>20<br>8 <br>4 <br>6 <br>4 <br>28<br>33<br>107<br>52<br>14<br>4 <br>9 <br>5 <br>11<br>6 <br>10<br>15<br>11<br>16<br>7 <br>9 <br>8 <br>13<br>27<br>45<br>91<br>36<br>22<br>11<br>6 <br>8 <br>7 <br>14<br>7 <br>14<br>10<br>9 <br>11<br>5 <br>10<br>14<br>28<br>67<br>69<br>50<br>16<br>13<br>7 <br>10<br>8 <br>7 <br>11 |
| 15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 | 12<br>9 <br>13<br>10<br>6 <br>7 <br>13<br>39<br>61<br>78<br>43<br>14<br>5 <br>10<br>12<br>11<br>10<br>7 <br>10<br>13<br>8 <br>13<br>7 <br>7 <br>11<br>41<br>71<br>74<br>36<br>10<br>5 <br>17<br>14<br>10<br>6 <br>8 <br>12<br>14<br>8 <br>9 <br>11<br>4 <br>12<br>40<br>62<br>74<br>44<br>7 <br>12<br>19<br>16<br>8 <br>7 <br>4 <br>8 <br>16<br>13<br>11<br>13<br>4 <br>9 <br>20<br>49<br>69<br>49<br>15<br>18<br>22<br>26<br>9 <br>7 <br>4 <br>12<br>16<br>17<br>10<br>8 <br>6 <br>3 <br>8 <br>16<br>65<br>62<br>27<br>40<br>31<br>23<br>10<br>3 <br>5 <br>6 <br>7 <br>19<br>21<br>10<br>13<br>4 <br>1 <br>9 <br>42<br>70<br>48<br>57<br>20<br>11<br>10<br>6 <br>10<br>11<br>16<br>14<br>15<br>16<br>11<br>6 <br>8 <br>7 <br>23<br>86<br>69<br>50<br>5 <br>9 <br>7 <br>7 <br>4 <br>9 <br>17<br>14<br>23<br>21<br>20<br>4 <br>12<br>7 <br>22<br>97<br>65<br>19<br>10<br>7 <br>4 <br>3 <br>7 <br>12<br>13<br>22<br>15<br>19<br>14<br>9 <br>7 <br>9 <br>31<br>105<br>63<br>14<br>5 <br>4 <br>5 <br>5 <br>9 |

**Tabla 74: - Frecuencia mensual de vientos calmos - serie pronóstico**

| Mes | Frecuencia de<br>vientos calmos | N°<br>días | % |
| --- | --- | --- | --- |
| Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre | 148<br>133<br>136<br>162<br>167<br>154<br>130<br>140<br>106<br>117<br>68<br>117 | 744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744 | 20%<br>20%<br>18%<br>23%<br>22%<br>21%<br>17%<br>19%<br>15%<br>16%<br>9%<br>16% |

**Tabla 75: - Frecuencia horaria de vientos calmos - serie pronóstico**

| Hora | Frecuencia de<br>vientos calmos | % |
| --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 76<br>84<br>78<br>90<br>80<br>84<br>84<br>106<br>96<br>84<br>72<br>62<br>55<br>46<br>32<br>35<br>26<br>36<br>60<br>61<br>50<br>52<br>61<br>68 | 21%<br>23%<br>21%<br>25%<br>22%<br>23%<br>23%<br>29%<br>26%<br>23%<br>20%<br>17%<br>15%<br>13%<br>9%<br>10%<br>7%<br>10%<br>16%<br>17%<br>14%<br>14%<br>17%<br>19% |

**Tabla 76: - Frecuencia mensual de vientos calmos - serie observada**

| Mes | Frecuencia de<br>vientos calmos | N°<br>días | % |
| --- | --- | --- | --- |
| Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre | 36<br>37<br>79<br>156<br>97<br>112<br>120<br>112<br>75<br>68<br>27<br>14 | 744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744 | 5%<br>6%<br>11%<br>22%<br>13%<br>16%<br>16%<br>15%<br>10%<br>9%<br>4%<br>2% |

**Tabla 77: - Frecuencia horaria de vientos calmos - serie observada**

| Hora | Frecuencia de<br>vientos calmos | % |
| --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 25<br>28<br>42<br>46<br>50<br>40<br>51<br>74<br>53<br>51<br>26<br>23<br>16<br>7 <br>8 <br>8 <br>6 <br>9 <br>13<br>15<br>19<br>20<br>26<br>21 | 7 <br>8 <br>12<br>13<br>14<br>11<br>14<br>20<br>15<br>14<br>7 <br>6 <br>4 <br>2 <br>2 <br>2 <br>2 <br>2 <br>4 <br>4 <br>5 <br>5 <br>7 <br>6 |

**Tabla 78: - Error medio cuadrático, sesgo, coeficiente de correlación, IOA, velocidad del viento y temperatura**

| Estadístico | Descripción | Fórmula | Resultado | Col5 |
| --- | --- | --- | --- | --- |
| Estadístico | Descripción | Fórmula | Velocidad del<br>viento [m/s] | Temperatura<br>[°C] |
| RMSE | Error medio cuadrático (Root mean<br>square Error), nos indica la medida de<br>las diferencias en promedio entre<br>valores pronosticados y observados |  | 0,85 | 3,24 |
| NRMSD | Error medio cuadrático normalizado<br>(Normalized<br>Root<br>mean<br>square<br>deviation) señala la varianza residual<br>entre los valores pronosticados y<br>observados |  | 0,18 | 0,09 |
| NMAE | Error medio absoluto normalizado,<br>toma en cuenta el peso del error<br>respecto al valor de la variable medida,<br>normaliza el error absoluto |  | 0,14 | 0,07 |
| BIAS | Sesgo, proporciona información sobre<br>la tendencia del modelo a sobrestimar<br>o subestimar una variable |  | 0,02 | -1,93 |
| Coeficiente de<br>correlación de<br>Pearson | Un índice que mide el grado de relación<br>de dos variables siempre y cuando<br>ambas sean cuantitativas. |  | 0,67 | 0,94 |
| IOA | El IOA (Index Of Agreement) acuerdo<br>es una medida de la coincidencia<br>entre la salida de cada predicción de<br>la media observada y la salida de cada<br>observación de la media observada. |  | 0,79 | 1,00 |
