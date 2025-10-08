---
title: Sin título
author: Microsoft Office User
date: D:20240315121158-03'00'
language: es
type: report
pages: 27
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA PARQUE SOLAR FOTOVOLTAICO PLANCHÓN APÉNDICE 2-4-1 ANÁLISIS DE RIESGO DE ACTIVACIÓN DE PROCESOS EROSIVOS
-->

# ADENDA PARQUE SOLAR FOTOVOLTAICO PLANCHÓN APÉNDICE 2-4-1 ANÁLISIS DE RIESGO DE ACTIVACIÓN DE PROCESOS EROSIVOS

Elaborado por

|Col1|ANEXOS|TEBAL-DOC-032|
|---|---|---|
||**ANEXOS**|**VER 02**|
||**ANEXOS**|**Agosto 2022**|
|AREA: GERENCIA ESTUDIOS Y<br>DESARROLLO / OPERACIONES|RESPONSABLE: GERENTE GENERAL FECHA ACTUALIZACION: 000000|RESPONSABLE: GERENTE GENERAL FECHA ACTUALIZACION: 000000|

Documento preparado por: TEBAL, Estudios e Ingeniería Ambiental Ltda.

Andrés de Fuenzalida 17, Oficina 34, Providencia, Santiago de Chile.

Teléfono: +56 2 2222 7059

Email: [info@tebal.cl](mailto:info@tebal.cl)

Website: www.tebal.cl

### REGISTRO DE CONTROL DE DOCUMENTO

|ANEXO 2.3.1 ANÁLISIS DE RIESGO DE ACTIVACIÓN DE PROCESOS EROSIVOS|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Versión|Elaboración y<br>Fecha|Firma|Revisión y<br>Fecha|Firma|Aprobación<br>TEBAL y<br>Fecha|Firma|Aprobación<br>Cliente y<br>Fecha|Firma|
|00|JMO Y JCC<br>8-3-2024||||||||
||||||||||
||||||||||

## ÍNDICE DE CONTENIDOS

1. INTRODUCCIÓN ....................................................................................................................... 1

2. OBJETIVOS ............................................................................................................................... 1

2.1 Objetivo general ...................................................................................................................... 1

2.2 Objetivos específicos ............................................................................................................... 1

3. METODOLOGÍA ........................................................................................................................ 1

3.1 Elaboración de cartografía base .............................................................................................. 2

3.1.1 Erodabilidad ................................................................................................................ 2

3.1.2 Clases de pendiente .................................................................................................... 3

3.1.3 Desprotección ............................................................................................................. 3

3.1.4 Agresividad climática ................................................................................................... 3

3.2 Procesamiento matricial de datos .......................................................................................... 4

3.3 Obtención de capas en la situación con obras ........................................................................ 5

3.4 Proyección escenario considerando cambio climático ........................................................... 5

4. RESULTADOS ........................................................................................................................... 6

4.1 Erodabilidad ............................................................................................................................ 6

4.2 Clases de pendiente ................................................................................................................ 8

4.3 Riesgo edafotopográfico ......................................................................................................... 9

4.4 Clases de desprotección ........................................................................................................ 10

4.5 Vulnerabilidad ....................................................................................................................... 11

4.6 Agresividad climática ............................................................................................................. 12

4.7 Riesgo de activación de procesos erosivos ........................................................................... 15

4.8 Situación con obras ............................................................................................................... 16

4.9 Situación con obras y cambio climático ................................................................................ 20

5. CONCLUSIONES ..................................................................................................................... 22

6. BIBLIOGRAFÍA ........................................................................................................................ 23

i

## ÍNDICE DE TABLAS

Tabla 1. Matriz de erodabilidad (clase textural x profundidad). ......................................................... 3

Tabla 2. Matriz de riesgo edafotopográfico (erodabilidad x pendiente). ........................................... 5

Tabla 3. Matriz de vulnerabilidad (riesgo edafotopográfico x desprotección). .................................. 5

Tabla 4. Matriz de riesgo de activación de procesos erosivos (vulnerabilidad x agresividad climática).

............................................................................................................................................................. 5

Tabla 5. Precipitaciones promedio de los últimos años en las estaciones de referencia. ................ 13

Tabla 6. IF por estación. .................................................................................................................... 13

Tabla 7. Porcentaje de clases de riesgo de activación de procesos erosivos en el AI....................... 16

Tabla 8. Porcentaje de clases de riesgo de activación de procesos erosivos, situación con Proyecto.

........................................................................................................................................................... 20

Tabla 9. Precipitaciones proyectadas para Teno. ............................................................................. 21

Tabla 10. IF escenario con cambio climático. .................................................................................... 21

Tabla 11. Porcentaje de clases de riesgo de activación de procesos erosivos en AI, situación sin

Proyecto y situación con Proyecto. ................................................................................................... 22

## ÍNDICE DE FIGURAS

Figura 1. Flujo básico para la obtención de la cartografía de riesgo de activación de procesos

erosivos. .............................................................................................................................................. 2

Figura 2. Índice de Fournier. ............................................................................................................... 4

Figura 3. Flujo de procesamiento para la elaboración de cartografía de riesgo ................................. 4

Figura 4. Profundidad de los suelos en el área de influencia. ............................................................. 6

Figura 5. Texturas en el área de influencia. ........................................................................................ 7

Figura 6. Modelo de erodabilidad. ...................................................................................................... 8

Figura 7. Clases de riesgo de pendiente. ............................................................................................. 9

Figura 8. Modelo edafotopográfico. ................................................................................................. 10

Figura 9. Clases de desprotección en el AI. ....................................................................................... 11

Figura 10. Modelo de vulnerabilidad. ............................................................................................... 12

Figura 11. IF en el AI. ......................................................................................................................... 14

Figura 12. Agresividad climática en el AI. .......................................................................................... 15

Figura 13. Riesgo de activación de procesos erosivos en el AI. ........................................................ 16
Figura 14. Área de intervención directa. ........................................................................................... 17

Figura 15. Modelo de desprotección, situación con obras. .............................................................. 18

Figura 16. Modelo de vulnerabilidad, situación con obras. .............................................................. 19

Figura 17. Riesgo de activación de procesos erosivos, situación con obras. .................................... 20

ii

## 1. INTRODUCCIÓN

Se realizó un análisis del riesgo de activación de procesos erosivos en el área de influencia (AI) sobre

el componente suelo del Proyecto Parque Solar Fotovoltaico Planchón, emplazado en la Región del

Maule. El Proyecto contempla la construcción y operación de un Parque Fotovoltaico para

generación de energía eléctrica, constituido por un total de 136.560 paneles fotovoltaicos bifaciales

monocristalinos de silicio de elevado rendimiento, con una capacidad nominal por panel de 655
(Wp) [1], que en conjunto tendrán una potencia total instalada de 89,45 WMp y una potencia nominal

de 75 MWn, que serán inyectados al Sistema Eléctrico Nacional (SEN).

Para trasmitir e inyectar la energía generada al Sistema Eléctrico Nacional (SEN), el Proyecto incluye

la construcción y operación de dos Líneas de Alta Tensión (LAT) soterradas en 33 kV que contarán

con una longitud aproximada de 45 m la LAT-1 y 284 m la LAT-2, hasta la conexión con la subestación

S/E Solís de 132 kV, perteneciente al Proyecto Parque Fotovoltaico Gran Teno 200 MW, aprobada

mediante RCA N°06/2021. Adicionalmente, el Proyecto contará con un Centro de Baterías BESS por

medio de baterías del tipo ion-litio, con una potencia máxima de 30 MW y duración de

almacenamiento de 5 horas.

## 2. OBJETIVOS

### 2.1 Objetivo general

 - Determinar el riesgo de activación de procesos erosivos en el AI de suelos del Proyecto.

### 2.2 Objetivos específicos

 - Determinar la superficie, proporción y ubicación de las actuales clases de riesgo de

activación de procesos erosivos en el área de influencia de suelos del Proyecto.

 - Determinar la superficie, proporción y ubicación de las clases de riesgo de activación de

procesos erosivos en el área de influencia de suelos del Proyecto, considerando una

situación con obras.

## 3. METODOLOGÍA

Según la guía “Evaluación de impactos de riesgos de activación de procesos erosivos, 2016” [2], el

estudio de riesgo de activación de procesos erosivos consta del análisis combinado de las principales

variables que determinan el riesgo de erosión de suelo como son:

1 Este tipo de módulo y su potencia puede variar según tecnología vigente durante la ingeniería de detalle del Parque

Fotovoltaico.

2 Servicio Agrícola y Ganadero. (SAG). (2016). Evaluación de impactos de riesgos de activación de procesos erosivos.

1

 - Erodabilidad (que está en función de la textura y profundidad del suelo).

 - Pendiente.

 - Cobertura vegetacional/desprotección.

 - Agresividad climática.

Para lo anterior, en primer lugar, se elabora cartografía base relacionada a las variables descritas.

Luego se interceptan los datos de las capas a través de un modelo matricial hasta obtener una

cartografía de riesgo de procesos erosivos. El esquema general de la metodología se presenta a

continuación:

**Figura 1. Flujo básico para la obtención de la cartografía de riesgo de activación de procesos**

**erosivos.**

Fuente: elaboración propia.

### 3.1 Elaboración de cartografía base

La metodología para la elaboración de cartografía base para cada capa se detalla a continuación:

**3.1.1** **Erodabilidad**

Se preparó cartografía básica sobre la textura del suelo y profundidad, ambas propiedades descritas

en la línea base de suelos del Proyecto (Anexo 2.5 de la DIA, Línea base de suelos), y clasificadas
según las categorías relacionadas al riesgo de erosión presentadas por la guía de SAG [3] . Finalmente

se cruzaron los datos, a través de procesamiento vectorial en Qgis, de las clases de profundidad y

textura según el modelo de la matriz presentado en la Tabla 1, obteniendo una cartografía de

erodabilidad con las clases respectivas asignadas según el modelo propuesto.

3 Servicio Agrícola y Ganadero. (SAG). (2016). Evaluación de impactos de riesgos de activación de procesos erosivos.

2

**Tabla 1. Matriz de erodabilidad (clase textural x profundidad).**

|CLASE DE PROFUNDIDAD|CLASE DE TEXTURA|Col3|Col4|Col5|
|---|---|---|---|---|
|**CLASE DE PROFUNDIDAD**|**BAJA**|**MEDIA**|**ALTA**|**MUY ALTA**|
|**BAJA**|Baja (1)4|Baja (1)|Media (2)|Alta (3)|
|**MEDIA**|Baja (1)|Media (2)|Alta (3)|Alta (3)|
|**ALTA**|Media (2)|Alta (3)|Alta (3)|Muy alta (4)|
|**MUY ALTA**|Media (2)|Alta (3)|Muy alta (4)|Muy alta (4)|

Fuente: evaluación de impactos de riesgos de activación de procesos erosivos SAG (2016).

**3.1.2** **Clases de pendiente**

Para el modelo de pendientes se utilizó un modelo de elevación digital generado a partir de curvas

de nivel levantadas (cada 50 cm) correspondiente a levantamiento topográfico realizado por el

Titular en el AI Proyecto. Luego se clasificaron las pendientes según lo propuesto por SAG, que para

esta zona presenta las siguientes categorías: riesgo bajo, pendiente de 0 a 4,5%; riesgo medio,

pendiente de 4,5 a 10,5%; riesgo alto, pendiente de 10,5 a 17,5% y riesgo muy alto, pendiente de

más de 17,5%.

**3.1.3** **Desprotección**

Para el modelo de desprotección primero se calificaron las clases vegetacionales presentes en el AI
del Proyecto según fotointerpretación y complementado con el mapa de formaciones vegetales [5] .

Luego se calificó la clase de desprotección respectiva para cada clase vegetacional, siguiendo las
correspondencias presentadas por SAG [6] .

**3.1.4** **Agresividad climática**

Para la determinación de la agresividad climática se calculó el Índice de Fournier (IF) según lo

propuesto por SAG para la zona central de Chile y cuya fórmula se muestra en la Figura 2. Para esto

se recopiló la información disponible de la red agrometeorológica del INIA, donde se analizaron los
datos de las precipitaciones medias mensuales de los últimos años [7] de las estaciones Peor es nada,

Aeródromo General Freire, Los Niches y San Jorge los Niches, que están cercanas al AI del Proyecto.

Calculado el IF de cada estación, se espacializaron los resultados a través del método Kriging.

4 En los modelos propuestos por SAG las clases de riesgo se presentan en 4 categorías, que van desde riesgo “bajo” hasta
“muy alto”, y que, para efectos de procesamiento, se presentan indistintamente con los números del 1 al 4, siendo 1 riesgo
“bajo” y 4 riesgo “muy alto”.
5 Anexo 2.6. Caracterización ambiental Flora y vegetación, DIA de Proyecto.
6 Tabla de asignación de clases de desprotección y clases vegetacionales, pag. 32, Servicio Agrícola y Ganadero. (SAG).
(2016). Evaluación de impactos de riesgos de activación de procesos erosivos.
7 Los datos disponibles corresponden a los últimos 6 años para las estaciones Aeródromo General Freire y San Jorge los
Niches, y últimos 2 años para las estaciones Los Niches y Peor es Nada.

3

**Figura 2. Índice de Fournier.**

Fuente: evaluación de impactos de riesgos de activación de procesos erosivos SAG (2016).

Finalmente, se cruzó la capa del IF espacializado con el polígono del AI, de modo de obtener los

valores de IF dentro del AI. Con este resultado, se clasificó la agresividad climática del AI, en

concordancia con lo que se menciona en la guía de evaluación de SAG, donde se proponen las

siguientes clases de agresividad climática en función del IF: agresividad baja con un IF menor a 50;

agresividad media con un IF entre 50 y 150; agresividad alta con un IF entre 150 a 200 y agresividad

muy alta con IF mayor a 200.

### 3.2 Procesamiento matricial de datos

Con las capas básicas generadas se cruzaron los datos sucesivamente siguiendo la ruta propuesta

por SAG, presentada en la Figura 3, interceptando las capas a través de procesamiento vectorial en

Qgis. De este modo se obtuvieron nuevas capas cuyas clases fueron asignadas según lo determinado

por las matrices propuestas.

**Figura 3. Flujo de procesamiento para la elaboración de cartografía de riesgo**

Fuente: Evaluación de impactos de riesgos de activación de procesos erosivos SAG (2016).

EL AI del Proyecto corresponde a la Zona de erosión IV (Valle Central de Valparaíso a Los Lagos)

cuyos modelos matriciales se muestran a continuación:

4

**Tabla 2. Matriz de riesgo edafotopográfico (erodabilidad x pendiente).**

|CLASE DE ERODABILIDAD|CLASE DE PENDIENTE|Col3|Col4|Col5|
|---|---|---|---|---|
|**CLASE DE ERODABILIDAD**|**BAJA(1)**|**MEDIA(2)**|**ALTA(3)**|**MUY ALTA(4)**|
|**BAJA(1)**|1|1|2|3|
|**MEDIA(2)**|2|2|3|3|
|**ALTA(3)**|2|3|3|4|
|**MUY ALTA(4)**|3|3|4|4|

Fuente: evaluación de impactos de riesgos de activación de procesos erosivos SAG (2016).

**Tabla 3. Matriz de vulnerabilidad (riesgo edafotopográfico x desprotección).**

|RIESGO EDAFOTOPOGRÁFICO|DESPROTECCIÓN|Col3|Col4|Col5|
|---|---|---|---|---|
|**RIESGO EDAFOTOPOGRÁFICO**|**BAJA(1)**|**MEDIA(2)**|**ALTA(3)**|**MUY ALTA(4)**|
|**BAJA(1)**|1|1|2|3|
|**MEDIA(2)**|2|2|3|3|
|**ALTA(3)**|2|3|3|4|
|**MUY ALTA(4)**|3|3|4|4|

Fuente: evaluación de impactos de riesgos de activación de procesos erosivos SAG (2016).

**Tabla 4. Matriz de riesgo de activación de procesos erosivos (vulnerabilidad x agresividad**

**climática).**

|VULNERABILIDAD|AGRESIVIDAD CLIMÁTICA|Col3|Col4|Col5|
|---|---|---|---|---|
|**VULNERABILIDAD**|**BAJA(1)**|**MEDIA(2)**|**ALTA(3)**|**MUY ALTA(4)**|
|**BAJA(1)**|1|1|2|2|
|**MEDIA(2)**|1|2|3|3|
|**ALTA(3)**|2|3|3|4|
|**MUY ALTA(4)**|3|4|4|4|

Fuente: evaluación de impactos de riesgos de activación de procesos erosivos SAG (2016).

Producto de los continuos cruces, finalmente se obtuvo la capa de riesgo de activación de procesos

erosivos con sus respectivas clases de riesgo.

### 3.3 Obtención de capas en la situación con obras

Para la determinación de la cartografía de riesgo de procesos erosivos en una situación con obras

(con Proyecto) se siguió el mismo flujo de procesamiento de datos descrito anteriormente, pero

asumiendo para las partes del Proyecto que modificaran la cobertura vegetal (área de intervención

directa), una clase de desprotección “Muy alta”, correspondiente a suelo desnudo, obteniendo así

finalmente la cartografía de riesgo de activación de procesos erosivos para una situación con obras.

### 3.4 Proyección escenario considerando cambio climático

El último análisis correspondió a la determinación de la cartografía de riesgo de procesos erosivos

en una situación con obras (con Proyecto) y escenario de cambio climático, para esto se calculó el
índice de Fournier en un escenario de cambio climático, usando los datos de la plataforma ARCLIM [8]

8 Ministerio del Medio ambiente. (2020). Atlas de riesgos climáticos.

5

que proyecta las precipitaciones para los años 2035-2065 en el escenario RCP 8.5 para la comuna

de Teno, donde se localiza el Proyecto.

## 4. RESULTADOS

### 4.1 Erodabilidad

En base a la prospección de suelos realizada en terreno se desarrolló la cartografía de erodabilidad

según la profundidad y la textura. La profundidad de los suelos y su clase respectiva para el análisis

matricial se presenta en la Figura 4. Las texturas predominantes y su clase respectiva, para el análisis

matricial, se presenta en la Figura 5.

**Figura 4. Profundidad de los suelos en el área de influencia.**

Fuente: elaboración propia.

6

**Figura 5. Texturas en el área de influencia.**

Fuente: elaboración propia.

Del cruce de las clases de riesgo según textura y profundidad, propiedades presentadas en las figuras

anteriores, y según el modelo matricial correspondiente (Tabla 1), se desprende el modelo de

erodabilidad presentado en la Figura 6.

7

**Figura 6. Modelo de erodabilidad.**

Fuente: elaboración propia.

### 4.2 Clases de pendiente

Se clasificó la pendiente a partir de un modelo de elevación digital (basado en curvas de nivel) según

los rangos establecidos por SAG para el sector. Las clases de riesgo de pendiente resultantes se

presentan en la Figura 7.

8

**Figura 7. Clases de riesgo de pendiente.**

Fuente: elaboración propia.

### 4.3 Riesgo edafotopográfico

La combinación de la cartografía de clases de riesgo de pendiente con la de erodabilidad, aplicando

el modelo matricial presentado en la Tabla 2, determina el grado de riesgo edafotopográfico del

área de influencia de suelos del Proyecto. El resultado de las clases de riesgo edafotopográfico se

presenta en la Figura 8.

9

**Figura 8. Modelo edafotopográfico.**

Fuente: elaboración propia.

### 4.4 Clases de desprotección

Con el fin de determinar las clases de desprotección en el área de influencia, se caracterizó la

cobertura vegetacional con las clases “Rotación cultivo pradera” (clase de desprotección muy alta),

y “Cortina arbórea” (clase de desprotección baja). Las clases de desprotección se muestran en la

Figura 9.

10

**Figura 9. Clases de desprotección en el AI.**

Fuente: elaboración propia.

### 4.5 Vulnerabilidad

La vulnerabilidad se determinó combinando las clases de riesgo edafotopográfico y las clases de

desprotección, según la matriz presentada en la Tabla 3. La representación del modelo de

vulnerabilidad se muestra en la Figura 10.

11

**Figura 10. Modelo de vulnerabilidad.**

Fuente: elaboración propia.

### 4.6 Agresividad climática

Para la determinación de la agresividad climática se calculó en Índice de Fournier (IF), recomendado
para la zona central de Chile. El promedio de precipitación mensual de los últimos años [9] y los

resultados de IF para las estaciones meteorológicas de referencia se presentan en la Tabla 5 y Tabla

6. Para toda el área de influencia se obtuvieron valores del IF menores a 50, como se muestra en la

Figura 11, lo que califica el AI con una clase de agresividad climática baja, como se muestra en la

Figura 12.

9 Los datos disponibles corresponden a los últimos 6 años para las estaciones Aeródromo General Freire y San Jorge los
Niches, y últimos 2 años para las estaciones Los Niches y Peor es Nada.

12

**Tabla 5. Precipitaciones promedio de los últimos años en las estaciones de referencia.**

|MES|PP (mm) PEOR ES NADA|PP (mm)<br>AERÓDROMO<br>GENERAL FREIRE|PP (mm) LOS<br>NICHES|PP (mm) SAN<br>JORGE LOS<br>NICHES|
|---|---|---|---|---|
|Enero|0,00|6,67|11,70|13,70|
|Febrero|0,00|0,33|45,20|0,60|
|Marzo|0,05|5,67|6,30|11,83|
|Abril|48,45|17,80|91,70|42,32|
|Mayo|30,60|29,53|54,90|65,77|
|Junio|98,95|83,77|112,20|149,38|
|Julio|110,00|60,23|120,80|79,28|
|Agosto|152,00|90,83|252,50|140,53|
|Septiembre|64,75|37,77|105,50|72,22|
|Octubre|15,00|14,17|26,60|25,58|
|Noviembre|28,50|8,37|47,40|18,90|
|Diciembre|0,30|0,20|0,50|0,73|

Fuente: elaboración propia.

**Tabla 6. IF por estación.**

|Col1|PEOR ES NADA|AERÓDROMO<br>GENERAL FREIRE|LOS NICHES|SAN JORGE<br>LOS NICHES|
|---|---|---|---|---|
|**PP ANUAL (mm)**|548,6|355,33|875,3|620,85|
|**PROMEDIO PP MES MÁS LLUVIOSO (mm)**|152|90,83|252,5|149,38|
|**IF**|42,11|23,21|72,83|35,94|

Fuente: elaboración propia.

13

**Figura 11. IF en el AI.**

Fuente: elaboración propia.

14

**Figura 12. Agresividad climática en el AI.**

Fuente: elaboración propia.

### 4.7 Riesgo de activación de procesos erosivos

Siguiendo el modelo matricial propuesto (Tabla 4), se determinó el riesgo de activación de procesos

erosivos combinando los resultados de las clases de vulnerabilidad y agresividad climática. Las clases

de riesgo resultantes se presentan en la en la Figura 13 y en la Tabla 7.

15

**Figura 13. Riesgo de activación de procesos erosivos en el AI.**

Fuente: elaboración propia.

**Tabla 7. Porcentaje de clases de riesgo de activación de procesos erosivos en el AI.**

|CLASE DE RIESGO|ÁREA (Ha)|%|
|---|---|---|
|Riesgo bajo|2,104|1,308|
|Riesgo medio|158,295|98,415|
|Riesgo alto|0,446|0,277|

Fuente: elaboración propia.

### 4.8 Situación con obras

La situación con obras modifica principalmente la clase de desprotección al despejar el suelo para

la instalación de algunas obras del Proyecto, lo que califica a ciertas partes del AI, específicamente

el área de intervención directa (AID) con una clase de desprotección muy alta, aumentando de este

modo, eventualmente, la vulnerabilidad y subsecuentemente el riesgo de activación de procesos

erosivos. El área de intervención directa sobre el suelo considerada para la estimación del modelo,

en una situación con obras, se muestra en la Figura 14. El modelo de desprotección, en la situación

con obras, considerando lo anterior, se muestra en la Figura 15 . El modelo de vulnerabilidad en la

situación con obras se muestra en la Figura 16 y el modelo de riesgo de activación de procesos

16

erosivos, en la situación con obras, se muestra en la Figura 17. El área y porcentaje de superficie

clasificada en función del riesgo de activación de procesos erosivos, en una situación con obras, se

muestra en la Tabla 8.

**Figura 14. Área de intervención directa.**

Fuente: elaboración propia.

17

**Figura 15. Modelo de desprotección, situación con obras.**

Fuente: elaboración propia.

18

**Figura 16. Modelo de vulnerabilidad, situación con obras.**

Fuente: elaboración propia.

19

**Figura 17. Riesgo de activación de procesos erosivos, situación con obras.**

Fuente: elaboración propia.

**Tabla 8. Porcentaje de clases de riesgo de activación de procesos erosivos, situación con**

**Proyecto.**

|CLASE DE RIESGO|ÁREA (Ha)|%|
|---|---|---|
|Riesgo bajo|1,872|1,164|
|Riesgo medio|158,522|98,556|
|Riesgo alto|0,451|0,280|

Fuente: elaboración propia.

### 4.9 Situación con obras y cambio climático

Los resultados del IF en un escenario de cambio climático, obtenidos usando los datos de la

plataforma ARCLIM [10] que proyecta las precipitaciones para los años 2035-2065 en el escenario RCP

8.5 para la comuna de Teno, donde se localiza el Proyecto se muestran a continuación:

10 Ministerio del Medio ambiente. (2020). Atlas de riesgos climáticos.

20

**Tabla 9. Precipitaciones proyectadas para Teno.**

|MES|PP PROMEDIO ARCLIM TENO (mm)|
|---|---|
|Enero|4,30|
|Febrero|6,40|
|Marzo|11,70|
|Abril|43,50|
|Mayo|123,30|
|Junio|168,00|
|Julio|149,50|
|Agosto|123,60|
|Septiembre|72,30|
|Octubre|34,30|
|Noviembre|16,50|
|Diciembre|8,20|

Fuente: ARCLIM (Ministerio del Medio Ambiente).

|Tabla 10. IF escenario|con cambio climático.|
|---|---|
||**ARCLIM TENO**|
|**PP PROMEDIO ANNUAL (mm)**|761,6|
|**PROMEDIO PP MES MAS LLUVIOSO (mm)**|168|
|**IF**|37,05|

Fuente: ARCLIM (Ministerio del Medio Ambiente).

De este modo, al considerar los datos proyectados en un escenario de cambio climático, el IF se

mantiene en los rangos presentados en el punto 4.6 del presente informe, que califica toda el AI con

una agresividad climática baja. Dado lo anterior, en un escenario con cambio climático no hay

variación en la clase de agresividad climática y, subsecuentemente, en el riesgo de activación de

procesos erosivos presentados previamente.

21

## 5. CONCLUSIONES

Los resultados indican que la superficie del área de influencia de suelos presenta las clases de riesgo

de activación de procesos erosivos “bajo”, en un 1,3 % de la superficie; clase de riesgo “medio”, en

un 98,4% de la superficie, y clase de riesgo “alto”, en un 0,27% de la superficie. En una situación con

obras, existe una variación mínima de las clases de riesgo, alcanzando la clase de riesgo “bajo” un

1,1 % de la superficie, la clase de riesgo “medio” un 98,5% de la superficie y la clase de riesgo “alto”,

un 0,28% de la superficie del AI.

**Tabla 11. Porcentaje de clases de riesgo de activación de procesos erosivos en AI, situación sin**

**Proyecto y situación con Proyecto.**

|CLASE DE RIESGO|Situación sin obras|Col3|Situación con obras|Col5|
|---|---|---|---|---|
|**CLASE DE RIESGO**|**ÁREA (Ha)**|**% **|**ÁREA (Ha)**|**% **|
|Riesgo bajo|2,104|1,308|1,872|1,164|
|Riesgo medio|158,295|98,415|158,522|98,556|
|Riesgo alto|0,446|0,277|0,451|0,280|

Fuente: elaboración propia.

Dado que el 98,5% de la superficie del área de influencia se encuentra en una clase de riego “medio”,

el Proyecto debe considerar dentro de sus Compromisos Ambientales Voluntarios (CAV) el

monitoreo de activación de procesos erosivos, el cual se detalla en el Anexo 4-1 de la presente

Adenda.

22

## 6. BIBLIOGRAFÍA

Servicio agrícola y ganadero (SAG). (2016). _Evaluación de impactos de riesgos de activación de_

_procesos erosivos._

Ministerio del Medio ambiente. (2020). _Atlas de riesgos climáticos_ .

23

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Matriz de erodabilidad (clase textural x profundidad).****

| CLASE DE PROFUNDIDAD | CLASE DE TEXTURA | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **CLASE DE PROFUNDIDAD** | **BAJA** | **MEDIA** | **ALTA** | **MUY ALTA** |
| **BAJA** | Baja (1)4 | Baja (1) | Media (2) | Alta (3) |
| **MEDIA** | Baja (1) | Media (2) | Alta (3) | Alta (3) |
| **ALTA** | Media (2) | Alta (3) | Alta (3) | Muy alta (4) |
| **MUY ALTA** | Media (2) | Alta (3) | Muy alta (4) | Muy alta (4) |

**Tabla 2.: Matriz de riesgo edafotopográfico (erodabilidad x pendiente).****

| CLASE DE ERODABILIDAD | CLASE DE PENDIENTE | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **CLASE DE ERODABILIDAD** | **BAJA(1)** | **MEDIA(2)** | **ALTA(3)** | **MUY ALTA(4)** |
| **BAJA(1)** | 1 | 1 | 2 | 3 |
| **MEDIA(2)** | 2 | 2 | 3 | 3 |
| **ALTA(3)** | 2 | 3 | 3 | 4 |
| **MUY ALTA(4)** | 3 | 3 | 4 | 4 |

**Tabla 3.: Matriz de vulnerabilidad (riesgo edafotopográfico x desprotección).****

| RIESGO EDAFOTOPOGRÁFICO | DESPROTECCIÓN | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **RIESGO EDAFOTOPOGRÁFICO** | **BAJA(1)** | **MEDIA(2)** | **ALTA(3)** | **MUY ALTA(4)** |
| **BAJA(1)** | 1 | 1 | 2 | 3 |
| **MEDIA(2)** | 2 | 2 | 3 | 3 |
| **ALTA(3)** | 2 | 3 | 3 | 4 |
| **MUY ALTA(4)** | 3 | 3 | 4 | 4 |

**Tabla 4.: Matriz de riesgo de activación de procesos erosivos (vulnerabilidad x agresividad****

| VULNERABILIDAD | AGRESIVIDAD CLIMÁTICA | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **VULNERABILIDAD** | **BAJA(1)** | **MEDIA(2)** | **ALTA(3)** | **MUY ALTA(4)** |
| **BAJA(1)** | 1 | 1 | 2 | 2 |
| **MEDIA(2)** | 1 | 2 | 3 | 3 |
| **ALTA(3)** | 2 | 3 | 3 | 4 |
| **MUY ALTA(4)** | 3 | 4 | 4 | 4 |

**Tabla 5.: Precipitaciones promedio de los últimos años en las estaciones de referencia.****

| MES | PP (mm) PEOR ES NADA | PP (mm)<br>AERÓDROMO<br>GENERAL FREIRE | PP (mm) LOS<br>NICHES | PP (mm) SAN<br>JORGE LOS<br>NICHES |
| --- | --- | --- | --- | --- |
| Enero | 0,00 | 6,67 | 11,70 | 13,70 |
| Febrero | 0,00 | 0,33 | 45,20 | 0,60 |
| Marzo | 0,05 | 5,67 | 6,30 | 11,83 |
| Abril | 48,45 | 17,80 | 91,70 | 42,32 |
| Mayo | 30,60 | 29,53 | 54,90 | 65,77 |
| Junio | 98,95 | 83,77 | 112,20 | 149,38 |
| Julio | 110,00 | 60,23 | 120,80 | 79,28 |
| Agosto | 152,00 | 90,83 | 252,50 | 140,53 |
| Septiembre | 64,75 | 37,77 | 105,50 | 72,22 |
| Octubre | 15,00 | 14,17 | 26,60 | 25,58 |
| Noviembre | 28,50 | 8,37 | 47,40 | 18,90 |
| Diciembre | 0,30 | 0,20 | 0,50 | 0,73 |

**Tabla 6.: IF por estación.****

| Col1 | PEOR ES NADA | AERÓDROMO<br>GENERAL FREIRE | LOS NICHES | SAN JORGE<br>LOS NICHES |
| --- | --- | --- | --- | --- |
| **PP ANUAL (mm)** | 548,6 | 355,33 | 875,3 | 620,85 |
| **PROMEDIO PP MES MÁS LLUVIOSO (mm)** | 152 | 90,83 | 252,5 | 149,38 |
| **IF** | 42,11 | 23,21 | 72,83 | 35,94 |

**Tabla 7.: Porcentaje de clases de riesgo de activación de procesos erosivos en el AI.****

| CLASE DE RIESGO | ÁREA (Ha) | % |
| --- | --- | --- |
| Riesgo bajo | 2,104 | 1,308 |
| Riesgo medio | 158,295 | 98,415 |
| Riesgo alto | 0,446 | 0,277 |

**Tabla 8.: Porcentaje de clases de riesgo de activación de procesos erosivos, situación con****

| CLASE DE RIESGO | ÁREA (Ha) | % |
| --- | --- | --- |
| Riesgo bajo | 1,872 | 1,164 |
| Riesgo medio | 158,522 | 98,556 |
| Riesgo alto | 0,451 | 0,280 |

**Tabla 9.: Precipitaciones proyectadas para Teno.****

| MES | PP PROMEDIO ARCLIM TENO (mm) |
| --- | --- |
| Enero | 4,30 |
| Febrero | 6,40 |
| Marzo | 11,70 |
| Abril | 43,50 |
| Mayo | 123,30 |
| Junio | 168,00 |
| Julio | 149,50 |
| Agosto | 123,60 |
| Septiembre | 72,30 |
| Octubre | 34,30 |
| Noviembre | 16,50 |
| Diciembre | 8,20 |

**Tabla 11.: Porcentaje de clases de riesgo de activación de procesos erosivos en AI, situación sin****

| CLASE DE RIESGO | Situación sin obras | Col3 | Situación con obras | Col5 |
| --- | --- | --- | --- | --- |
| **CLASE DE RIESGO** | **ÁREA (Ha)** | **% ** | **ÁREA (Ha)** | **% ** |
| Riesgo bajo | 2,104 | 1,308 | 1,872 | 1,164 |
| Riesgo medio | 158,295 | 98,415 | 158,522 | 98,556 |
| Riesgo alto | 0,446 | 0,277 | 0,451 | 0,280 |
