---
title: Sin título
author: Estación 9
date: D:20240220143043-03'00'
language: es
type: report
pages: 44
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO HIDRÁULICO CANAL PERIMETRAL REVESTIDO PARA AGUAS LLUVIAS PLANTA TALTAL
-->

## INFORME 2

# ESTUDIO HIDRÁULICO CANAL PERIMETRAL REVESTIDO PARA AGUAS LLUVIAS PLANTA TALTAL

**PROYECTO**

## DECLARACIÓN DE IMPACTO AMBIENTAL _“Readecuación depósito de ripios y transición para el cierre de_ _Planta Taltal, ENAMI”_

**Guillaume Julien Mankoch Soriano**

**Ingeniero Civil**

**Febrero 2024**

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|2 de 44|

**ÍNDICE DE CONTENIDOS**

**1** **OBJETIVO Y ALCANCE.................................................................................................. 3**

**2** **TRANSPORTE Y EVACUACIÓN DE AGUAS LLUVIAS ................................................. 3**

**3** **ESTUDIO HIDRÁULICO .................................................................................................. 7**

3.1 C AUDALES DE CRECIDAS ............................................................................................................................................ 7

3.2 A NTECEDENTES T OPOGRÁFICOS ................................................................................................................................. 9

3.3 COEFICIENTE DE RUGOSIDAD DE MANNING .................................................................................................... 15

3.4 ANÁLISIS HIDRÁULICO CANAL DE CONTORNO REVESTIDO Y QUEBRADAS ....................................................... 18

3.5 ANÁLISIS DE RESULTADOS ........................................................................................................................................ 33

**4** **SOCAVACIÓN ................................................................................................................36**

4.1 S OCAVACIÓN G ENERAL .......................................................................................................................................... 36

4.2 ANÁLISIS RESULTADOS ..................................................................................................................................... 44

2

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|3 de 44|

## 1 OBJETIVO Y ALCANCE

Se desarrolla la siguiente modelación hidráulica para canal perimetral mejorado de la planta José

Antonio Moreno, denominada Planta Taltal, para el proyecto “Readecuación Depósito de ripios y

Transición para el Cierre de Planta Taltal, ENAMI”, ubicada en la Comuna de Taltal, Región de

Antofagasta, la cual opera desde el año 1966.

El objetivo de este documento es representar la modelación hidráulica del canal perimetral

mejorado y quebradas involucradas en el transporte para la recolección y evacuación de las

aguas lluvias del sector mediante la herramienta computacional HEC-RAS.

En el Informe 1 se presentó la situación base del proyecto, es decir un canal existente sin

revestimientos. En esta presentación se incluirán todas las mejoras necesarias y se simulará la

actuación del canal en caso de eventos extremos. El modelo busca observar y predecir el

comportamiento de las aguas lluvias hasta este sector, trasladando las aguas lluvias y dejando

finalmente que a su salida escurran libremente por la Quebrada San Ramón.

## 2 TRANSPORTE Y EVACUACIÓN DE AGUAS LLUVIAS

Las aguas lluvias son transportadas por dos quebradas, la primera conduce las aguas hacia un

canal perimetral proyectado, el cual recibe el aporte de 5 cuencas, y la otra es la quebrada San

Ramón. Según los lineamientos establecidos por la DGA, se hará la verificación hidráulica del

canal existente y la quebrada san Ramón que se conecta a este último, como se muestra en la

figura 2.1.

3

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|4 de 44|

**Figura 2.1: Tramo de estudio hidráulica Canal interceptor.**

Fuente: Elaboración propia.

Como se expuso en el Informe 1- Situación Sin Proyecto, debido a problemas de posibles

desbordes en ciertos tramos del canal, éste será revestido mediante gaviones y mampostería de

piedra, como se puede ver en la figura 2.2:

4

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|5 de 44|

**Figura 2.2: Sección transversal canal existente mejorado.**

Fuente: Better, 2018.

En este caso, el mejoramiento que se realizó es proyectar una sección trapecial de 2.5 m de

ancho basal, con un talud de 1:1 (H:V) por la ribera derecha, talud vertical por la ribera izquierda

compuesto por los gaviones.

Se proyectó además una obra de cruce de camino tipo cajón de 3,0 y 2,0 m, diseño típico según

manual de carreteras, la obra se aprecia en la figura 2.3.

**Figura 2.3: Cajón de hormigón tipo.**

Fuente: Better, 2018.

5

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|6 de 44|

**Tabla 2.1: Dimensiones** **cajón proyectado**

<!-- INICIO TABLA 2.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4| |---|---|---|---| |**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**| |**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|6 de 44| -->

**Tabla 2.1: Dimensiones** **cajón proyectado****

| Parámetro | Unidad | Valor |
| --- | --- | --- |
| Ancho cajón (B) | m | 3,0 |
| Alto cajón (H) | m | 2,0 |
| Parámetro T1 | m | 0,3 |
| Parámetro T2 | m | 0,3 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Modificado de Better, 2018. Finalmente, además se proyectó una obra de descarga tipo enrocado para la unión hacia la -->
<!-- FIN TABLA 2.1 -->


|Parámetro|Unidad|Valor|
|---|---|---|
|Ancho cajón (B)|m|3,0|
|Alto cajón (H)|m|2,0|
|Parámetro T1|m|0,3|
|Parámetro T2|m|0,3|

Fuente: Modificado de Better, 2018.

Finalmente, además se proyectó una obra de descarga tipo enrocado para la unión hacia la

quebrada San Ramón, como se muestra en la próxima figura.

**Figura 2.4: Obra de Descarga.**

Fuente: Modificado de Better, 2018.

6

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|7 de 44|

## 3 ESTUDIO HIDRÁULICO

**3.1** **CAUDALES DE CRECIDAS**

En este capítulo de mostrará el estudio hidráulico del canal y quebradas involucradas para así

observar el escurrimiento a partir de los caudales de las cuencas aportantes en el estudio

hidrológico. Se caracterizan los escurrimientos de crecida, para identificar y/o determinar los

niveles de inundación que se alcanzarían.

La caracterización de los escurrimientos se refiere a la determinación de los niveles de agua,

distribución de caudales en el cauce principal y en las áreas de inundación, como también los

parámetros hidráulicos básicos asociados a los caudales de crecidas para periodos de retorno

de 100, 1.000 y 10.000 años.

Los parámetros morfológicos de las cuencas aportantes se presentan en la tabla 3.1.

**Tabla** **3.1: Parámetros Morfométricos** **de la** **Cuencas.**

|Cuenca|Perímetro<br>(m)|Área<br>(km2)|Longitud<br>de<br>Cauce<br>(km)|HM<br>(m)|Hm<br>(m)|Desnivel<br>(m)|Pendiente<br>en %|
|---|---|---|---|---|---|---|---|
|Cuenca 1|6,87|1,73|2,81|697|70|627|22,313|
|Cuenca 2|2|0,2|0,66|204|58|146|22,121|
|Cuenca 3|2,27|0,25|0,98|268|61|207|21,122|
|Cuenca 4|0,86|0,04|0,15|107|55|52|34,667|
|Cuenca 5|0,91|0,03|0,37|150|48|102|27,568|
|Cuenca 6 (Qda. San<br>Ramón)<br>|92<br> <br>|269<br>|43<br>|1.940<br>|40<br>|1.900|4,419|

Fuente: Estudios hidrológicos 4G Ingeniería Integral Spa.

Para la estimación de caudal máximo asociado a cuencas pequeñas se utilizó el método racional

simplificado recomendado por la DGA el documento Guías Metodológicas para Proyectos de

Modificación de Cauces de Construcción, DGA (2016), para Áreas Menores a 20 Km [2] .

Por otro lado, para cuencas de mayor tamaño se utilizaron los métodos de la formula racional,

Verni & King Modificado (DGA 1995) y Método DGA-AC.

7

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|8 de 44|

El Método Racional (Mulvaney, 1850; Kuichling, 1889; Lloyd-Davies, 1906), es un método

empírico y aplicable en general a pequeñas cuencas y, mediante determinadas modificaciones,

a cuencas medianas. Mediante este método, se puede estimar el caudal Q de avenida a partir

del tiempo de concentración de la cuenca.

El caudal calculado para las cuencas pequeñas es presentado en la tabla 3.2.

<!-- INICIO TABLA 3.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- distribución granulométrica de las mismas para así caracterizar el tipo de suelo en cual se producirá el escurrimiento de las aguas lluvias. -->

**Tabla 3.2: Coordenadas de Ubicación Puntos de Muestreo. Datum WGS 84 / H 19 S.****

| Guillaume Mankoch Soriano<br>Ingeniero civil | READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI | Col3 | Col4 |
| --- | --- | --- | --- |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **Fecha:** | **Página:** |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | Febrero 2024 | 13 de 44 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 3.4: Ubicación calicatas sector canal interceptor.** Fuente: 4G Ingeniería Integral Spa. -->
<!-- FIN TABLA 3.2 -->


**Tabla 3.2: Caudales máximos de cuencas pequeñas mediante el método racional simplificado.**

|Cuenca|T= 100 años Q<br>(m3/s)|T= 1.000 años Q<br>(m3/s)|T= 10.000 años Q<br>(m3/s)|
|---|---|---|---|
|Cuenca 1|3.11|4.13|5.14|
|Cuenca 2|0.45|0.60|0.75|
|Cuenca 3|0.54|0.72|0.90|
|Cuenca 4|0.09|0.12|0.15|
|Cuenca 5<br>|0.07 <br>|0.09 <br>|0.11|

Fuente: Estudios hidrológicos 4G Ingeniería Integral Spa.

El área de la Cuenca San Ramón es 269 km2 y el tiempo de concentración es de 4 h. El

coeficiente de escorrentía calculado para 10 años es 0,53. En la siguiente tabla se resumen los

caudales obtenidos para esta cuenca mediante los métodos recomendados por la DGA.

**Tabla 3.3: Cuadro comparativo de caudales según los métodos empleados, cuenca 6.**

<!-- INICIO TABLA 3.3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- coeficiente de escorrentía calculado para 10 años es 0,53. En la siguiente tabla se resumen los caudales obtenidos para esta cuenca mediante los métodos recomendados por la DGA. -->

**Tabla 3.3: Cuadro comparativo de caudales según los métodos empleados, cuenca 6.****

| T (años)<br>10<br>50<br>100 | Método Fórmula<br>Racional (Q m3/s) | Verni y King Modificado<br>(Q m3/s) | Método DGA-AC<br>(Q m3/s) |
| --- | --- | --- | --- |
| **T (años)**<br>10<br>50<br>100 | 100,997 | 19,588 | 0,42 |
| **T (años)**<br>10<br>50<br>100 | 226,341 | 50,696 | 0,60 |
| **T (años)**<br>10<br>50<br>100 | 272,499<br> | 62,743<br> | 0,68 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Estudios hidrológicos 4G Ingeniería Integral Spa. Al realizar una evaluación de los caudales obtenidos para la Cuenca 6- Quebrada San Ramón, -->
<!-- FIN TABLA 3.3 -->


|T (años)<br>10<br>50<br>100|Método Fórmula<br>Racional (Q m3/s)|Verni y King Modificado<br>(Q m3/s)|Método DGA-AC<br>(Q m3/s)|
|---|---|---|---|
|**T (años)**<br>10<br>50<br>100|100,997|19,588|0,42|
|**T (años)**<br>10<br>50<br>100|226,341|50,696|0,60|
|**T (años)**<br>10<br>50<br>100|272,499<br>|62,743<br>|0,68|

Fuente: Estudios hidrológicos 4G Ingeniería Integral Spa.

Al realizar una evaluación de los caudales obtenidos para la Cuenca 6- Quebrada San Ramón,

mediante los tres métodos empleados, se observa que el mayor caudal obtenido para un periodo

de retorno de 100 años es de 272,5 m [3] /s, calculado por el Método Formula Racional. Luego, se

puede apreciar que los métodos DGA-AC y Verni King subestiman los valores de los caudales

de cuencas de mayor área, en comparación con los estimados por el método racional.

En efecto, los caudales calculados para cuencas pequeñas por el Método Racional Modificado

son mayores a los estimados por los métodos indicados anteriormente, aun cuando las áreas de

cuenca de estas son mucho menores al área de la Cuenca 6.

8

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|9 de 44|

**3.1.1 Caudales con aporte de detritos**

Según lo anterior, usando un 30% de concentración de sólidos, se presentan en la tabla 3.7 los

Caudales de diseño con aporte de detritos.

Finalmente, estos son los caudales a ingresar en el software de modelación, calculados mediante

el método racional al ser el caso más conservador.

**Tabla** **3.4: Caudales** **utilizados** **para** **el diseño** **de** **obras** **con aporte** **de** **detritos.**

|ID Cuenca|10 años|100 años|150 años|1.000 años|10.000 años|
|---|---|---|---|---|---|
|Cuenca 1|2.40|4.45|4.70|5.89|7.34|
|Cuenca 2|0.35|0.65|0.68|0.86|1.07|
|Cuenca 3|0.42|0.78|0.82|1.03|1.28|
|Cuenca 4|0.07|0.13|0.13|0.17|0.21|
|Cuenca 5|0.05|0.09|0.10|0.12|0.15|
|Cuenca 6<br>Qda. San<br>Ramón|121.03<br>|379.62<br>|422.01<br>|624.91<br>|877.68|

Fuente: Estudios hidrológicos 4G Ingeniería Integral Spa.

**3.2** **ANTECEDENTES TOPOGRÁFICOS**

Para efectos de contar con la información topográfica, se muestran los perfiles longitudinales de

terreno que ingresarán al software de modelación HEC RAS.

9

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|10 de 44|

**Figura 3.1: Perfil longitudinal canal existente mejorado.**

Fuente: Elaboración propia.

**Figura 3.2: Perfil longitudinal tramo final quebrada san Ramón (se conecta con canal existente).**

Fuente: Elaboración propia.

10

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|11 de 44|

**Figura 3.3: Perfil longitudinal tramo Quebrada san Ramón más canal existente.**

Fuente: Elaboración propia.

11

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|12 de 44|

**3.2.1 ESTUDIO DE MECÁNICA DE SUELOS**

Se recopilaron los antecedentes que permitieron caracterizar los suelos del sector con el fin de

analizar el tipo de material granular en los sectores de inundación, ya que se eso dependerá si

es susceptible a erosionar debido a la velocidad del escurrimiento y el comportamiento del flujo

a raíz del coeficiente de rugosidad de Manning.

Para esto, se realizó una descripción estratigráfica de las muestras extraídas, como también la

distribución granulométrica de las mismas para así caracterizar el tipo de suelo en cual se

producirá el escurrimiento de las aguas lluvias.

**Tabla 3.2: Coordenadas de Ubicación Puntos de Muestreo. Datum WGS 84 / H 19 S.**

Fuente: 4G Ingeniería Integral Spa.

12

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|13 de 44|

**Figura 3.4: Ubicación calicatas sector canal interceptor.**

Fuente: 4G Ingeniería Integral Spa.

Para la clasificación de suelos se realizaron dos muestras compuestas, cada una formada por el

material extraído de los tres horizontes visualizados en las calicatas. A continuación, se pueden

observar los resultados obtenidos para los ensayos de granulometría, límites de consistencia,

densidad de partículas y porcentaje de humedad.

**Tabla 3.5: Límites de Atterberg obtenidos.**

<!-- INICIO TABLA 3.5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- observar los resultados obtenidos para los ensayos de granulometría, límites de consistencia, densidad de partículas y porcentaje de humedad. -->

**Tabla 3.5: Límites de Atterberg obtenidos.****

| Guillaume Mankoch Soriano<br>Ingeniero civil | READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI | Col3 | Col4 |
| --- | --- | --- | --- |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **Fecha:** | **Página:** |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | Febrero 2024 | 14 de 44 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 3.6: Clasificación SUCS de muestras de suelos obtenidas.** Fuente: 4G Ingeniería Integral Spa. -->
<!-- FIN TABLA 3.5 -->


13

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|14 de 44|

**Tabla 3.6: Clasificación SUCS de muestras de suelos obtenidas.**

Fuente: 4G Ingeniería Integral Spa.

**Tabla 3.7: densidad de suelos obtenidos.**

<!-- INICIO TABLA 3.7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Tabla 3.6: Clasificación SUCS de muestras de suelos obtenidas.** Fuente: 4G Ingeniería Integral Spa. -->

**Tabla 3.7: densidad de suelos obtenidos.****

| Guillaume Mankoch Soriano<br>Ingeniero civil | READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI | Col3 | Col4 |
| --- | --- | --- | --- |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **Fecha:** | **Página:** |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | Febrero 2024 | 15 de 44 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 3.8: Determinación humedad de suelos.** Fuente: 4G Ingeniería Integral Spa. -->
<!-- FIN TABLA 3.7 -->


Fuente: 4G Ingeniería Integral Spa.

14

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|15 de 44|

**Tabla 3.8: Determinación humedad de suelos.**

Fuente: 4G Ingeniería Integral Spa.

**3.3** **COEFICIENTE DE RUGOSIDAD DE MANNING**

**3.3.1 COEFICIENTE PARA CANAL NATURAL**

Cuando no se tiene claro el valor del coeficiente de Manning para un cauce natural, lo que

comúnmente se realiza es utilizar el método de Cowan o Multiparamétrico.

Cowan, en 1956, desarrolló una expresión que permite determinar el valor del coeficiente de

Manning a través de la interacción de diferentes parámetros que permiten describir o valorar

características concretas de un cauce. La expresión es la siguiente:

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) m

En esta expresión, el valor del coeficiente de rugosidad de Manning n depende de:

**n** **0** : valor base de n para un cauce recto, uniforme y liso en función del material del fondo.

**n** **1** : coeficiente de corrección para implementar el efecto de las irregularidades superficiales.

**n** **2** : coeficiente que añade las variaciones de forma y tamaño de la sección del cauce.

**n** **3** : coeficiente que considera el efecto de obstrucciones.

**n** **4** : coeficiente que incorpora el efecto de presencia de vegetación.

15

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|16 de 44|

**m** : factor corrector que considera la sinuosidad del cauce.

En la tabla 3.9 se resumen los criterios y los valores numéricos que los corresponden, por medio

de la ecuación de Cowan para la quebrada San Ramón.

**Tabla 3.9: Valores relativos de la expresión de Cowan.**

<!-- INICIO TABLA 3.9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la tabla 3.9 se resumen los criterios y los valores numéricos que los corresponden, por medio de la ecuación de Cowan para la quebrada San Ramón. -->

**Tabla 3.9: Valores relativos de la expresión de Cowan.****

| Condiciones del canal | Col2 | Col3 | Valores |
| --- | --- | --- | --- |
| Material | Tierra | n0 | 0.020 |
| Material | Roca | Roca | 0.025 |
| Material | Grava fina | Grava fina | 0.024 |
| Material | Grava gruesa | Grava gruesa | 0.028 |
| Grado de Irregularidad | Ligero | n1 | 0.000 |
| Grado de Irregularidad | Menor | Menor | 0.005 |
| Grado de Irregularidad | Moderado | Moderado | 0.010 |
| Grado de Irregularidad | Severo | Severo | 0.020 |
| Variaciones en la sección transversal del canal | Gradual | n2 | 0.000 |
| Variaciones en la sección transversal del canal | Ocasional | Ocasional | 0.005 |
| Variaciones en la sección transversal del canal | Frecuente | Frecuente | 0.010-0.015 |
| Efecto relativo de Obstáculos | Despreciable | n3 | 0.000 |
| Efecto relativo de Obstáculos | Menor | Menor | 0.010 - 0.015 |
| Efecto relativo de Obstáculos | Apreciable | Apreciable | 0.020 - 0.030 |
| Efecto relativo de Obstáculos | Severo | Severo | 0.040 - 0.060 |
| Vegetación | Baja | n4 | 0.005 - 0.010 |
| Vegetación | Media | Media | 0.010 - 0.025 |
| Vegetación | Alta | Alta | 0.025 - 0.050 |
| Vegetación | Muy Alta | Muy Alta | 0.050 - 0.100 |
| Grado de sinuosidad<br> | Menor | m | 1.000 |
| Grado de sinuosidad<br> | Apreciable | Apreciable | 1.150 |
| Grado de sinuosidad<br> | Severo<br> | Severo<br> | 1.300 |

<!-- Estadísticas: 22 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Manual HEC RAS. Según el análisis granulométrico se tiene que el tipo de material del cauce presenta un material -->
<!-- FIN TABLA 3.9 -->


|Condiciones del canal|Col2|Col3|Valores|
|---|---|---|---|
|Material|Tierra|n0|0.020|
|Material|Roca|Roca|0.025|
|Material|Grava fina|Grava fina|0.024|
|Material|Grava gruesa|Grava gruesa|0.028|
|Grado de Irregularidad|Ligero|n1|0.000|
|Grado de Irregularidad|Menor|Menor|0.005|
|Grado de Irregularidad|Moderado|Moderado|0.010|
|Grado de Irregularidad|Severo|Severo|0.020|
|Variaciones en la sección transversal del canal|Gradual|n2|0.000|
|Variaciones en la sección transversal del canal|Ocasional|Ocasional|0.005|
|Variaciones en la sección transversal del canal|Frecuente|Frecuente|0.010-0.015|
|Efecto relativo de Obstáculos|Despreciable|n3|0.000|
|Efecto relativo de Obstáculos|Menor|Menor|0.010 - 0.015|
|Efecto relativo de Obstáculos|Apreciable|Apreciable|0.020 - 0.030|
|Efecto relativo de Obstáculos|Severo|Severo|0.040 - 0.060|
|Vegetación|Baja|n4|0.005 - 0.010|
|Vegetación|Media|Media|0.010 - 0.025|
|Vegetación|Alta|Alta|0.025 - 0.050|
|Vegetación|Muy Alta|Muy Alta|0.050 - 0.100|
|Grado de sinuosidad<br>|Menor|m|1.000|
|Grado de sinuosidad<br>|Apreciable|Apreciable|1.150|
|Grado de sinuosidad<br>|Severo<br>|Severo<br>|1.300|

Fuente: Manual HEC RAS.

Según el análisis granulométrico se tiene que el tipo de material del cauce presenta un material

grava fina, grado de irregularidad Menor, una variación de sección transversal Gradual, efecto

de obstáculos menor y vegetación baja. Además, el grado de sinuosidad apreciable.

Considerando estas características se tiene que el valor de la rugosidad de la quebrada San

Ramón se estimó en 0.048, lo cual se presenta en la tabla 3.10:

<!-- INICIO TABLA 3.10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4| |---|---|---|---| |**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**| |**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|17 de 44| -->

**Tabla 3.10: Coeficiente de Manning, según método de Cowan.****

| Determinación Manning | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **n0 ** | Material | Grava gruesa | 0.028 |
| **n1 ** | Grado de irregularidad | Moderado | 0.010 |
| **n2 ** | Variación en la sección transversal del<br>canal | Gradual | 0.000 |
| **n3 ** | Efecto relativo de Obstáculos | Menor | 0.010 |
| **n4 ** | Vegetación | Despreciable | 0.000 |
| **m ** | Grado de sinuosidad | Apreciable | 1.000 |
| <br> | <br> | **n = 0.048**<br> | **n = 0.048**<br> |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Por lo tanto los coeficientes de rugosidad adoptados para las quebradas en terreno natural son -->
<!-- FIN TABLA 3.10 -->


16

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|17 de 44|

**Tabla 3.10: Coeficiente de Manning, según método de Cowan.**

|Determinación Manning|Col2|Col3|Col4|
|---|---|---|---|
|**n0 **|Material|Grava gruesa|0.028|
|**n1 **|Grado de irregularidad|Moderado|0.010|
|**n2 **|Variación en la sección transversal del<br>canal|Gradual|0.000|
|**n3 **|Efecto relativo de Obstáculos|Menor|0.010|
|**n4 **|Vegetación|Despreciable|0.000|
|**m **|Grado de sinuosidad|Apreciable|1.000|
|<br>|<br>|**n = 0.048**<br>|**n = 0.048**<br>|

Fuente: Elaboración propia.

Por lo tanto los coeficientes de rugosidad adoptados para las quebradas en terreno natural son

como sigue:

**Tabla 3.11: Coeficiente de Manning adoptado quebrada San Ramón y descarga.**

<!-- INICIO TABLA 3.11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Por lo tanto los coeficientes de rugosidad adoptados para las quebradas en terreno natural son como sigue: -->

**Tabla 3.11: Coeficiente de Manning adoptado quebrada San Ramón y descarga.****

| Coeficiente | Ribera Izquierda | Centro | Ribera derecha |
| --- | --- | --- | --- |
| n | 0.048<br> | 0.048<br> | 0.048 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Para los coeficientes de rugosidad en el revestimiento, se proyecta la utilización de shotcrete en -->
<!-- FIN TABLA 3.11 -->


|Coeficiente|Ribera Izquierda|Centro|Ribera derecha|
|---|---|---|---|
|n|0.048<br>|0.048<br>|0.048|

Fuente: Elaboración propia.

Para los coeficientes de rugosidad en el revestimiento, se proyecta la utilización de shotcrete en

toda la extensión del canal, tanto en la sección de mampostería como para los gaviones. De

manera conservadora, se considera una rugosidad de n=0,020 para el shotcrete.

**Tabla 3.12: Coeficiente de Manning adoptado para canal mejorado.**

<!-- INICIO TABLA 3.12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- toda la extensión del canal, tanto en la sección de mampostería como para los gaviones. De manera conservadora, se considera una rugosidad de n=0,020 para el shotcrete. -->

**Tabla 3.12: Coeficiente de Manning adoptado para canal mejorado.****

| Coeficiente | Ribera Izquierda | Centro | Ribera derecha |
| --- | --- | --- | --- |
| n0 | 0.020<br> | 0.020<br> | 0.020 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 17 -->
<!-- FIN TABLA 3.12 -->


|Coeficiente|Ribera Izquierda|Centro|Ribera derecha|
|---|---|---|---|
|n0|0.020<br>|0.020<br>|0.020|

Fuente: Elaboración propia.

17

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|18 de 44|

**3.4 ANÁLISIS HIDRÁULICO CANAL DE CONTORNO REVESTIDO Y QUEBRADAS**

**3.4.1 MÉTODO DE CÁLCULO**

Sobre la base de los antecedentes hidrológicos y topográficos disponibles, se evaluaron los

niveles de escurrimiento y principales parámetros hidráulicos que definen el escurrimiento

asociado a los caudales de crecida de 100, 1000 y 10000 años de período de retorno para el

canal proyectado y la quebrada San Ramón.

Para evaluar los escurrimientos críticos y normales se utilizó el programa HEC-RAS versión 6.1

del Hydrologic Engineering Center del Cuerpo de Ingenieros del Ejército de los EE.UU. el cual

permite calcular, en base a la metodología del escurrimiento gradualmente variado y a los

factores de conducción hidráulica, ejes hidráulicos en cauces naturales, los cuales se

caracterizan por presentar secciones irregulares donde normalmente existen un cauce principal

y áreas de inundación.

El algoritmo de cálculo utiliza el “Standard Sted Method” para determinar el nivel de escurrimiento

en una sección, cuando se conoce el nivel de escurrimiento y demás parámetros hidráulicos en

una sección adyacente a ésta. Para evaluar los ejes hidráulicos, el programa requiere de

información topográfica (perfiles transversales al escurrimiento por el cauce y distancia entre las

secciones) e hidráulica (caudales de crecida y coeficientes de rugosidad).

**3.4.1.1** **ECUACIÓN DE ENERGÍA ESPECÍFICA**

Para el cálculo de estas variables el software utiliza la ecuación de la energía a través de un

proceso iterativo entre una sección y la que le sigue.

Donde:

WS1, WS2: Elevaciones de la superficie del agua en las secciones transversales 1 y 2 [m].

V1, V2: Velocidades promedias (caudal/área de flujo) [m/s].

α1, α2: Coeficientes para ponderar las velocidades [ ].

18

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|19 de 44|

g: Aceleración de gravedad [m/s2].

he: Pérdida de carga [m].

**Figura 3.5: representación de las líneas de energía, línea de agua y fondo de canal.**

Fuente: Manual de usuario HEC RAS.

**3.4.1.2** **ECUACIÓN DE PÉRDIDAS**

La pérdida de carga (he) entre dos secciones transversales está compuesta de la pérdida por

fricción y la pérdida por contracción o expansión. La ecuación para calcular la pérdida total de

energía es:

Donde:

L : Longitud del tramo equivalente [m].

J : Pendiente de fricción representativa entre dos secciones [m].

19

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|20 de 44|

C : Coeficiente de pérdida por expansión o contracción [ ].

**3.4.1.3** **Cálculo de caudales de transporte**

Para el cálculo de la capacidad del canal se puede utilizar la ecuación de escurrimiento

uniforme de Manning:

Donde,

_Q_ : Caudal [m3/s].

_n_ : Coeficiente de rugosidad de Manning [ ].

_Ω_ : Área de la sección transversal de escurrimiento [m2].

_R_ : Radio hidráulico del escurrimiento (razón entre el área y perímetro mojado) [m].

_i_ : Pendiente de fondo del canal [m/m].

En resumen, el cálculo dependerá del tipo de régimen seleccionado para la modelación, ya que

en función de las condiciones de borde que se ingresen al programa, este comenzará a iterar

desde aguas arriba, aguas abajo o ambas, por ejemplo, si la simulación se hace en régimen

subcrítico solo se ingresarán condiciones de borde aguas abajo, desde este punto se comienza

a iterar hacia aguas arriba debido a que las perturbaciones ocasionadas por singularidades

aguas abajo se propagan hacia aguas arriba en este tipo de régimen, obteniendo alturas de

escurrimiento, críticas, velocidades, número de Froude, etc.

En la figura 3.7 se muestra la geometría del cauce modelado por donde escurrirían las aguas

lluvias.

20

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|21 de 44|

**Figura 3.6: Representación geometría canal de estudio.**

Fuente: Elaboración propia.

Se modelaron 56 secciones transversales para el canal, 9 secciones transversales para la

quebrada San Ramón y 12 secciones transversales para el canal que recibe los aportes de la

quebrada y el canal existente. Para esto se definieron las secciones transversales cada 20

metros.

21

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|22 de 44|

**Figura 3.7: Incorporación secciones transversales quebrada previa al canal existente mejorado.**

Fuente: HEC RAS.

**Figura 3.8: Incorporación secciones transversales quebrada san Ramón.**

Fuente: HEC RAS.

22

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|23 de 44|

Una vez definida completamente la geometría de los cauces a modelar se procede a ingresar los

caudales de crecidas para 100, 1000 y 10000 años indicados en la tabla 3.4 del documento.

Luego de disponer de los caudales, se deben definir las condiciones de contorno al programa,

los cuales están referidos a los límites del tramo en estudio, para el presente proyecto se

seleccionaron las siguientes condiciones, las cuales se dividieron en 3 cauces separados por

una “junction” que une la quebrada san ramón y el canal proyectado.

**Figura 3.9: Condiciones de contorno de flujo**

Fuente: HEC RAS.

Debido a las condiciones del cauce, tales como cambios de pendiente y secciones, se hizo la

modelación en régimen mixto para la condición de profundidad normal conocidas las pendientes

de energía de los tramos de influencia aguas arriba y aguas abajo. Como no se conoce la

pendiente de la línea de energía se pueden utilizar las pendientes de fondo del canal.

Después de ingresar los datos anteriormente definidos, como resultado el programa entrega,

para cada perfil transversal, los principales parámetros que definen el escurrimiento tales como:

niveles del eje hidráulico, caudales y velocidades por sub-secciones, profundidad máxima, ancho

superficial, número de Froude, profundidades críticas, entre otros. Estos últimos parámetros se

presentarán en los siguientes puntos.

**3.4.2 EJES HIDRÁULICOS**

Sobre la base de los antecedentes topográficos (perfiles longitudinales y transversales del

cauce), caudales de crecida, coeficientes de rugosidad estimados y la metodología anteriormente

23

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|24 de 44|

señalada, se evaluaron las alturas de escurrimiento críticas, normales y los ejes hidráulicos

asociados a los caudales de crecida.

**Figura 3.10: Eje hidráulico canal proyectado.**

Fuente: HEC RAS.

24

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|25 de 44|

**Figura 3.11: Eje hidráulico quebrada San Ramón.**

Fuente: HEC RAS.

**Figura 3.12: Eje hidráulico cauce aportes quebrada San Ramón + canal proyectado.**

Fuente: HEC RAS.

25

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|26 de 44|

**3.4.3 Tablas de resultados**

En el siguiente apartado se muestra la tabla resumen que entrega HEC RAS.

**Tabla 3.13: Resultados modelación canal Proyectado.**

<!-- INICIO TABLA 3.13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **3.4.3 Tablas de resultados** En el siguiente apartado se muestra la tabla resumen que entrega HEC RAS. -->

**Tabla 3.13: Resultados modelación canal Proyectado.****

| Guillaume Mankoch Soriano<br>Ingeniero civil | READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI | Col3 | Col4 |
| --- | --- | --- | --- |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **Fecha:** | **Página:** |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | Febrero 2024 | 27 de 44 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 27 |Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4| |---|---|---|---| -->
<!-- FIN TABLA 3.13 -->


26

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|27 de 44|

27

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|28 de 44|

28

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|29 de 44|

29

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|30 de 44|

30

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|31 de 44|

**Figura 3.13: Resultados modelación Quebrada San Ramón aguas arriba.**

31

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|32 de 44|

**Figura 3.14: Resultados modelación Quebrada San Ramón + canal Proyectado.**

Fuente: HEC RAS.

32

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|33 de 44|

**3.5** **ANÁLISIS DE RESULTADOS**

Debido a la topografía particular del sector, el canal mejorado evacua los caudales aportantes a

una alta velocidad, presentándose flujo supercrítico en casi todos los tramos, esto también debido

a la disminución de la cota de agua al utilizar un coeficiente de rugosidad menor (0.020).

Si el canal perimetral estuviese en terreno natural, el análisis para el caso sin proyecto arrojaba

importantes riesgos de rebalse en los sectores cercanos al depósito de ripios, considerando un

coeficiente de rugosidad de Manning de 0.048 debido al tipo de suelo de carácter más grueso y

pocos finos. Como se mencionó, el nivel de agua está bajo las alturas críticas en casi todas las

secciones del canal por lo que el revestimiento aminora el riesgo de inundación. En la figura 3.15

se aprecia la sección típica del canal mejorado con la altura de flujo obtenida.

**Figura 3.15: Resultado modelación canal proyectado.**

Según la topografía, los cambios de pendiente y sección aluden a una introducción de

condiciones de contorno tanto aguas como aguas abajo, es decir, un régimen de flujo mixto. En

cuanto a la quebrada San Ramón se aprecia una elevación relevante en los primeros tramos

debido a que la sección es más pequeña, sobre todo para los casos de análisis de periodos de

33

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|34 de 44|

retorno de 1.000 y 10.000 años, ya cuando las sección se ensancha y hay un cambio de

pendiente disminuye la cota de agua, lo que se replica hacia la descarga.

**Figura 3.16: Modelo 3D de todos los cauces.**

En cuanto a la obra de arte en el canal mejorado se obtuvieron las siguientes alturas de

escurrimientos:

34

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|35 de 44|

**Figura 3.17: Sección transversal culvert aguas arriba.**

**Figura 3.18: Sección transversal Culvert aguas abajo.**

35

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|36 de 44|

## 4 SOCAVACIÓN

La socavación puede distinguirse entre socavación general del fondo y socavación local. La

primera se puede explicar por la acción de un flujo de agua sobre el fondo del cauce. La

socavación local, en cambio, se explica por la acción de un flujo más complejo; se presenta

asociada a singularidades como obstáculos o a sectores curvos del cauce.

En este estudio se determinará la socavación general en el cauce, debido a la ausencia de

singularidades en la zona de interés.

**4.1** **SOCAVACIÓN GENERAL**

La socavación general es aquella producida por un estrechamiento artificial o natural del cauce,

que provoca un descenso del lecho en un determinado tramo, debido a un desequilibrio de la

tasa de salida y entrada del sedimento.

Se considerarán dos métodos para la estimación de la socavación general, expuestos en el

Manual de Carreteras Vol. 3 (2016), el método de Neill y el Método de Lischtvan-Levediev.

**4.1.1 Método de Neill**

Para sedimentos gruesos se puede utilizar la siguiente ecuación:

−0.33

V c
~~√~~ g h c

= 1.81
~~(~~ [h] D [c]

[c]

D [)]

Donde:

V c : Velocidad crítica de arrastre [m/s]

h c : Altura de escurrimiento para la condición de arrastre crítico [m]

D : Diámetro representativo del sedimento del lecho [m]

g : Aceleración de gravedad [m/s [2] ]

Para sedimentos gruesos se utiliza D= D84, D= D90 o D= D95 según la mayor dispersión

granulométrica que presente la distribución.

La Figura 4.4.1 muestra la forma de realizar el cálculo.

36

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|37 de 44|

**Figura 4.4.1: Esquema para cálculo de socavación general, método de Neill (M.C. Vol. 3).**

La socavación de la franja o subsección _j_ denominada en la figura _Sj_, queda definida como:

S = h −h
j cj j

Donde:

h cj : Altura de la franja socavada.

h j : Altura de la franja sin socavar.

Finalmente igualando caudales la expresión anterior queda:

h
cj
= (

0.855

q j
1.81 ∙ ~~√~~ g∙D [0.33] ~~[)]~~

Donde q j es el caudal por unidad de ancho, y se calcula de la siguiente expresión:

- [n]

n j

q j = [Q] [j]

B
j

= [1]

B
j

R [j] [)]

-Q

2/3

- [Ω] [j]

[j]

Ω [∙(R] R [j]

Donde:

Q j : Caudal total de la franja j [m [3] /s]

B j : Ancho de la franja j [m]

Ω j : Área de la franja j [m [2] ]

37

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|38 de 44|

R j : Radio hidráulico de la franja j [m] R j = Ω j /B j

Ω, R, n, Q : Las mismas variables anteriores, definidas para la sección total

**4.1.2 Método de Litschvan-Levediev**

Para sedimentos no cohesivos se usa la siguiente relación:

1

q j 1+x
h =
j
~~(~~ 0.68 ∙β∙D [0.28] ∙Ψ ~~[)]~~

Donde:

h j : Altura de escurrimiento de la franja socavada j [m]

q j : Caudal por unidad de ancho de la franja socavada j [m [3] /m/s]

D : Diámetro medio del sedimento obtenido de la curva granulométrica [mm]

β : Coeficiente función de la probabilidad de excedencia según tabla 3.707.405.A del M.C.

Ψ : Coeficiente que considera la influencia del sedimento en suspensión según tabla

3.707.405.B del M.C.

x : Parámetro de la fórmula de arrastre crítico según tabla 3.707.405.C del M.C.

n : Rugosidad de Manning.

i : Pendiente media del lecho.

En el caso de estudio, se tienen los siguientes valores, los cuales fueron obtenidos de los

ensayos de granulometría del presente informe, como promedio de las calicatas en torno al canal

perimetral. Se consideró el caso para 1000 años.

D50 = 8.50 [mm]

D65 = 15.00 [mm]

D84 = 33.00 [mm]

D90 = 42.00 [mm]

38

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|39 de 44|

β= 1.07 Para 1000 años de periodo de retorno.

Ψ = 1.60, Considerando un Gs = 2.85 y humedad = 4.1% (suelo seco), por lo tanto, γs = 2.85

ton/m3, al ser suelo seco γs ~ γd, por lo tanto, peso específico de la mezcla se asumirá de 1.40.

(mayor valor de la tabla 3.707.405.B del M.C).

x= 0.35 Considerando un D50 = 8.50 [mm] .

**4.1.3 Resultados socavación**

En las siguientes tablas se pueden apreciar los valores de socavación para las secciones más

representativas del canal proyectado. Los tramos considerados para el cálculo de socavación

van de izquierda a derecha (Variable x) en el modelo de perfiles transversales en HEC RAS. Se

realizó el cálculo para los perfiles para la quebrada San Ramón, las siguientes tablas muestran

los parámetros utilizados en el método de Litschvan - Levediev (Fuente: Manual de carreteras).

**Tablas 4.1: Coeficiente Beta**

**Tabla 4.2: Coeficiente X**

<!-- INICIO TABLA 4.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- los parámetros utilizados en el método de Litschvan - Levediev (Fuente: Manual de carreteras). **Tablas 4.1: Coeficiente Beta** -->

**Tabla 4.2: Coeficiente X****

| Guillaume Mankoch Soriano<br>Ingeniero civil | READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI | Col3 | Col4 |
| --- | --- | --- | --- |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **Fecha:** | **Página:** |
| **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | **INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br> | Febrero 2024 | 40 de 44 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Perfil 400 Quebrada San Ramón** |x|hj|nj|bj|Aj|Rj|Qj|qj|NEIL|Col10|LITSCHVAN-<br>LEVEDIEV|Col12| |---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 4.2 -->


39

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|40 de 44|

**Perfil 400 Quebrada San Ramón**

|x|hj|nj|bj|Aj|Rj|Qj|qj|NEIL|Col10|LITSCHVAN-<br>LEVEDIEV|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**x **|**hj**|**nj**|**bj**|**Aj**|**Rj**|**Qj**|**qj**|**hcj**|**Sj**|**hcj**|**Sj**|
|1.91|1.59|0.048|1.91|1.52|0.80|15.82|8.30|2.14|0.55|2.67|1.08|
|3.81|2.46|0.048|1.91|3.86|2.03|40.29|21.13|3.16|0.70|5.23|2.77|
|5.72|4.10|0.048|1.91|6.25|3.28|65.27|34.22|4.05|0.00|7.40|3.30|
|7.63|4.51|0.048|1.91|8.21|4.31|85.66|44.92|4.71|0.20|9.00|4.49|
|9.54|4.30|0.048|1.91|8.40|4.41|87.65|45.96|4.77|0.47|9.15|4.85|
|11.44|4.05|0.048|1.91|7.96|4.18|83.07|43.56|4.63|0.58|8.80|4.75|
|13.35|3.80|0.048|1.91|7.48|3.93|78.10|40.95|4.47|0.67|8.42|4.62|
|15.26|3.64|0.048|1.91|7.09|3.72|74.02|38.82|4.34|0.70|8.10|4.46|
|17.16|2.96|0.048|1.91|6.29|3.30|65.66|34.43|4.06|1.10|7.43|4.47|
|19.07|2.96|0.048|1.91|2.82|1.48|29.45|15.44|2.74|0.00|4.17|1.21|

40

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|41 de 44|

**Perfil 380 Quebrada San Ramón**

|x|hj|nj|bj|Aj|Rj|Qj|qj|NEIL|Col10|LITSCHVAN-<br>LEVEDIEV|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**x **|**hj**|**nj**|**bj**|**Aj**|**Rj**|**Qj**|**qj**|**hcj**|**Sj**|**hcj**|**Sj**|
|1.81|5.38|0.048|1.81|4.87|2.69|32.41|17.88|2.93|0.00|4.64|0.00|
|3.62|6.61|0.048|1.81|10.86|6.00|72.22|39.86|4.40|0.00|8.26|1.65|
|5.44|7.07|0.048|1.81|12.39|6.84|82.40|45.48|4.74|0.00|9.08|2.01|
|7.25|7.43|0.048|1.81|13.14|7.25|87.34|48.20|4.91|0.00|9.47|2.04|
|9.06|7.43|0.048|1.81|13.46|7.43|89.51|49.40|4.98|0.00|9.63|2.20|
|10.87|7.43|0.048|1.81|13.46|7.43|89.51|49.40|4.97|0.00|9.63|2.20|
|12.68|5.45|0.048|1.81|11.67|6.44|77.58|42.82|4.58|0.00|8.69|3.24|
|14.50|3.17|0.048|1.81|7.81|4.31|51.92|28.65|3.69|0.52|6.51|3.34|
|16.31|1.91|0.048|1.81|4.60|2.54|30.60|16.89|2.85|0.94|4.45|2.54|
|18.12|1.91|0.048|1.81|1.73|0.96|11.50|6.35|1.96|0.05|2.20|0.29|

41

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|42 de 44|

**PERFIL 220 Descarga Qda San Ramón + Canal Proyectado**

|x|hj|nj|bj|Aj|Rj|Qj|qj|NEIL|Col10|LITSCHVAN-<br>LEVEDIEV|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**x **|**hj**|**nj**|**bj**|**Aj**|**Rj**|**Qj**|**qj**|**hcj**|**Sj**|**hcj**|**Sj**|
|**[m]**|**[m]**|**- **|**[m]**|**[m2]**|**[m]**|**[m3/s]**|**[m3/s/m]**|**[m]**|**[m]**|**[m]**|**[m]**|
|5.05|2.25|0.048|5.05|11.70|2.32|84.13|16.68|2.83|0.58|4.41|2.16|
|10.09|2.39|0.048|5.05|11.70|2.32|84.13|16.68|2.83|0.44|4.41|2.02|
|15.14|2.12|0.048|5.05|11.38|2.26|81.78|16.21|2.80|0.68|4.32|2.20|
|20.18|2.55|0.048|5.05|11.78|2.34|84.68|16.78|2.84|0.29|4.43|1.88|
|25.23|2.48|0.048|5.05|12.69|2.52|91.21|18.08|2.94|0.46|4.67|2.19|
|30.27|1.43|0.048|5.05|9.86|1.96|70.90|14.05|2.63|1.20|3.90|2.47|
|35.32|1.11|0.048|5.05|6.41|1.27|46.06|9.13|2.22|1.11|2.86|1.75|
|40.36|1.11|0.048|5.05|5.60|1.11|40.25|7.98|2.11|1.00|2.60|1.49|
|45.41|0.82|0.048|5.05|4.87|0.97|35.00|6.94|2.02|1.20|2.35|1.53|
|50.45|0.82|0.048|5.05|2.07|0.41|14.87|2.95|1.61|0.79|1.27|0.45|

42

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|43 de 44|

**Perfil 200 Descarga Qda San Ramón + Canal Proyectado**

|x|hj|nj|bj|Aj|Rj|Qj|qj|NEIL|Col10|LITSCHVAN-<br>LEVEDIEV|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**x **|**hj**|**nj**|**bj**|**Aj**|**Rj**|**Qj**|**qj**|**hcj**|**Sj**|**hcj**|**Sj**|
|**[m]**|**[m]**|**- **|**[m]**|**[m2]**|**[m]**|**[m3/s]**|**[m3/s/m]**|**[m]**|**[m]**|**[m]**|**[m]**|
|6.05|1.29|0.048|6.05|10.89|1.80|73.94|12.22|2.48|1.19|3.53|2.24|
|12.10|2.31|0.048|6.05|14.34|2.37|97.35|16.09|2.79|0.48|4.30|1.99|
|18.15|2.43|0.048|6.05|16.67|2.76|113.17|18.71|2.99|0.56|4.79|2.36|
|24.20|3.08|0.048|6.05|16.30|2.70|110.70|18.30|2.96|0.00|4.72|1.64|
|30.25|2.31|0.048|6.05|10.95|1.81|74.35|12.29|2.49|0.18|3.54|1.23|
|36.30|1.31|0.048|6.05|7.87|1.30|53.40|8.83|2.19|0.88|2.79|1.48|
|42.35|1.29|0.048|6.05|7.87|1.30|53.40|8.83|2.19|0.90|2.79|1.50|
|48.40|1.31|0.048|6.05|4.84|0.80|32.86|5.43|1.87|0.56|1.97|0.66|
|54.45|0.29|0.048|6.05|1.75|0.29|11.91|1.97|1.50|1.21|0.95|0.66|
|60.50|0.29|0.048|6.05|1.75|0.29|11.91|1.97|1.50|1.21|0.95|0.66|

43

|Guillaume Mankoch Soriano<br>Ingeniero civil|READECUACIÓN DEPÓSITO DE RIPIOS Y TRANSICIÓN PARA EL CIERRE DE<br>PLANTA TALTAL, ENAMI|Col3|Col4|
|---|---|---|---|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**Fecha:**|**Página:**|
|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|**INFORME:**<br>Estudio Hidráulico Canal revestido para aguas lluvias planta<br>Taltal<br>|Febrero 2024|44 de 44|

**4.2** **ANÁLISIS RESULTADOS**

De los resultados de socavación general se obtiene que, con el método de Neill, la socavación

es nula, mientras que con el método de Litschvan-Levediev sí existe socavación, esto se analizó

para la quebrada San Ramón y su descarga debido a que es colindante con la planta Taltal y

tiene por finalidad transportar y evacuar las aguas desde la cuenca aportante 6, cuya caudal

estimado es de 630 m3/s para el caso de T=1000 años.

De los resultados del modelamiento hidráulico para el caudal de diseño asociado al periodo de

retorno de 10.000 años, se concluye que el canal tiene la capacidad para conducir el

escurrimiento proveniente de las cuencas 1, 2, 3, 4 y 5 a lo largo de toda su extensión hasta la

unión con la quebrada San Ramón. Por otra parte, las velocidades obtenidas si bien son elevadas

en algunos tramos (sobre 6 m/s) no se considera erosiva ni perjudicaría el funcionamiento del

canal debido a que se presentan sólo para el caso eventual para el periodo de retorno

mencionado a causa del proceso de cierre de la planta, la cual exige por seguridad analizar

hidráulicamente el canal para 10.000 años.

En cuanto a los niveles de socavación se aprecia un máximo valor estimado de casi 5 metros en

la quebrada San Ramón para la sección 400, los demás niveles calculados se encuentran entre

el orden de 1 y 3 metros, esto debido al gran cantidad de caudal para el caso de 1000 años y la

composición del suelo, el cual es principalmente grava con mezcla de algunos finos, por tal razón

la socavación es considerablemente mayor para estos caudales. Por otra parte, se aprecia que

no hay una influencia relevante de los caudales del canal perimetral mejorado ya que las

velocidades se mantienen respecto a lo que proviene desde aguas arriba de la unión de la

quebrada San Ramón y el canal.

44