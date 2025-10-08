---
title: Anexo 1  Hidrologia
author: admin
date: D:20180911155443-04'00'
language: es
type: report
pages: 11
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 1 HIDROLOGIA
  - 1.1) ANÁLISIS DE CRECIDAS
  - 1.2) CUENCA ÁREA DE ESTUDIO
-->

# ANEXO 1 HIDROLOGIA

# 1.1) ANÁLISIS DE CRECIDAS

2

ANALISIS HIDROLÓGICO
CÁLCULO DE CAUDALES MÁXIMOS INSTANTÁNEOS

1) Determinación de Caudales de Crecida en Area de Estudio

Como parte de este proyecto, se realizó un estudio de crecidas con el objeto de
determinar el caudal máximo instantáneo para diferentes períodos de retorno en la Quebrada Sin
Nombre en el Parque Fotovoltaico Barriles. Esta quebrada pertenece a la Subcuenca No 0221
Costeras entre Quebrada Iquiñe y Quebrada Tocopilla inclusive. La subcuenca No 0221 posee una
superficie total de 1222,6 km2, y es parte de la Cuenca No 022 Costeras entre Río Loa y Quebrada
Camarones,que posee una superficie de 8377,4 km2.

Dado que la Quebrada Sin Nombre no cuenta con control fluviométrico, fue
necesario recurrir a métodos basados en fórmulas empíricas para el cálculo de los caudales de
crecidas. Los métodos considerados fueron: la Fórmula Racional, la Fórmula de Verni-King
Modificada y el Método AC-DGA, que son aplicables a cuencas pluviales.

Como antecedentes previos se consignan en el Cuadro No1 los datos

morfométricos de la cuenca estudiada.

Cuadro No1

Antecedentes Morfométricos

Quebrada Sin Nombre en Estación Tamaya

|A|L|Ce|Cg|Cs|S|
|---|---|---|---|---|---|
|(km2)|(km)|(msnm)|(msnm)|(msnm)||
|12,687|7,541|1607|1388|1169|0,058|

donde A: superficie de la cuenca, L: longitud del cauce principal, Ce : cota del punto más alto de la
cuenca, Cg: cota del centro de gravedad de la cuenca, Cs: cota de salida de la cuenca, s : pendiente
media del cauce principal

Un antecedente pluviométrico relevante para este cálculo, es la precipitación
máxima en 24 horas, para un período de retorno de 10 años P(10, 24). Según el estudio “
Precipitaciones Máximas en 1,2,3 días ” (DGA, 1989), para la estación Tocopilla se tiene que este
valor es 9,5 mm. Por seguridad se adopta P(10,24) = 10 mm.

3

a) Fórmula Racional

La fórmula racional para el cálculo de caudales máximos ha sido bastante aplicada
para estimar el caudal de diseño en cuencas pequeñas. Se ha recomendado para cuencas menores
de 1000 has, pero se reportan casos de aplicación a cuencas del orden de 30000 has.

Este método permite determinar el caudal máximo instantáneo que se produce
para una lluvia de intensidad constante I sobre un área A, de acuerdo a la siguiente relación :

Q = C *I* A / 3,6 (m3/s) (1)

Q : caudal máximo instantáneo (m3/s)
C : coeficiente de escorrentía de período de retorno T años.
I : intensidad de la lluvia de período de retorno T y duración igual al tiempo de
concentración de la cuenca. I en (mm/hora)
A : área de la cuenca (km [2] )

La intensidad de diseño se obtiene a partir de la relación:

I = I (T,t) = P(T,t)/t (2)

donde t corresponde a la duración de la lluvia de diseño P, y T el período de retorno utilizado. El
valor de t habitualmente se considera igual al tiempo de concentración de la cuenca de interés. En
tanto, el valor de P se obtiene de la relación:

P(T,t) = 1,1* CF(T)*CD(t)*P24 (10) (3)

donde :

CF = coeficiente de frecuencia. Se adopta los valores de estación Lequena (es la más cercana
documentada en el Manual de Carreteras,Vol3)
CD= coeficiente de duración. Se adopta CD ( 1 hora) de estación Lequena, y se calcula luego CD
(t<1 hora) con corrección de Bell.
P24(10) = precipitación máxima en 24 horas, con período de retorno de 10 años.

4

Cuadro No2

Coeficientes de Frecuencia para Diferentes Períodos de Retorno
Estación: Lequena

|T (años)|2|5|10|25|50|100|200|
|---|---|---|---|---|---|---|---|
|CF|0,490|0,800|1,000|1,260|1,450|1,640|1,830|

(*) Manual de Carretera,Vol 3, Cuadro 3.702.403 B

Cuadro No3

Coeficientes de Duración para Diferentes Duraciones
Estación: Lequena

|t (horas)|1|2|4|6|8|10|12|14|18|24|
|---|---|---|---|---|---|---|---|---|---|---|
|CD|0,34|0,52|0,75|0,87|0,93|0,94|0,95|0,96|0,96|1,00|

(*) Manual de Carretera,Vol 3, Cuadro 3.702.403 A

Para duraciones t menores a 1 hora,se aplica la corrección de Bell, según la

relación:

CD (t,T) = (0,54 * t [0,25] -0,5) * (0,21 * Ln(T) + 0,58) * CD (1 hora,T = 10 años)

t en minutos.

El factor 1,1 de la relación (3) es un coeficiente de seguridad que se aplica, debido
a que el valor de P24(10) considera lluvias máximas caídas entre las 0 y 24 horas de cada día, en
circunstancias de que las lluvias máximas anuales de 24 horas de duración son normalmente
mayores, pues ocurren en horas de un día y en horas del día siguiente.

El valor de t se determinó mediante la relación de California, que considera como
parámetros relevantes la longitud del cauce principal y la diferencia de nivel entre el punto más
alto y el punto de salida de la cuenca.

5

|Cuadro No4 Tiempo de Concentración Quebrada Sin Nombre en Parque Fotovoltaico Barriles|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Tiempo de Concentración (hrs)|Tiempo de Concentración (hrs)|Tiempo de Concentración (hrs)|Tiempo de Concentración (hrs)|Tiempo de Concentración (hrs)|Tiempo de Concentración (hrs)|
|Giandotti|Giandotti|Giandotti|California|Kirpich|Adoptado|
|tmin|tmax|t||||
|1,396|2,095|2,159|0,942|0,935|0,942|

Cuadro No5

Coeficiente de Duración CD (tc =0,942 hrs,T)
Quebrada Sin Nombre en Parque Fotovoltaico Barriles

|T (años)|CD (t)|
|---|---|
|2|0,222|
|5|0,286|
|10|0,335|
|25|0,399|
|50|0,447|
|100|0,496|
|200|0,544|

En tanto, el coeficiente de escorrentía se obtuvo de la publicación “Manual de
Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin Información Fluviométrica” (DGA, 1995).
Se consideraron los valores de la III Región, dado que en esta publicación no se consideró la II
región para este coeficiente.

Cuadro No6
Coeficiente de Escorrentía en Área de Estudio

|Periodo de retorno T|C(T)/C(10)|C(T)|
|---|---|---|
|(años)|||
|2|0,90|0,0081|
|5|0,95|0,0086|
|10|1,00|0,0090|
|25|1,14|0,0103|
|50|1,23|0,0111|
|100|1,32|0,0119|
|200|1,50|0,0135|

Cuadro No 7

Caudal Máximo Instantáneo según Método Racional
Quebrada Sin Nombre en Parque Fotovoltaico Barriles

6

|Periodo de retorno T|P(T,t)|I(T,t)|Qmax(T,t)|
|---|---|---|---|
|(años)|(mm)|(mm/hora)|(m3/s)|
|2|1,2|1,269|0,036|
|5|2,5|2,672|0,081|
|10|3,7|3,906|0,124|
|25|5,5|5,866|0,212|
|50|7,1|7,572|0,295|
|100|8,9|9,493|0,397|
|200|11,0|11,630|0,553|

b) Fórmula de Verni-King Modificada

Si bien se señala que esta Fórmula es aplicable a cuencas de superficie mayor a 20
km2, que es mayor al área de la cuenca de estudio, igual se aplicó, con el objeto de tener fórmulas

alternativas al método racional.

Q = C(T) *0,00618* P 241,24 *A 0,88 (4)

Q : caudal máximo instantáneo (m3/s)
C(T) : coeficiente empírico de período de retorno T años
P 24 : precipitación máxima diaria de período de retorno T, expresada en mm
A : área de la cuenca (km [2] )

Cuadro No8

Caudal Máximo Instantáneo según Verni-King
Quebrada Sin Nombre en Parque Fotovoltaico Barriles

|Periodo de retorno T|C(T)/C(10)|C(T)|P(T)|Qmax(T,t)|
|---|---|---|---|---|
|(años)|||(mm)|(m3/s)|
|2|0,90|0,024|4,900|0,010|
|5|0,95|0,026|8,000|0,020|
|10|1,00|0,027|10,000|0,027|
|25|1,14|0,031|12,600|0,041|
|50|1,23|0,033|14,500|0,053|
|100|1,32|0,036|16,400|0,066|
|200|1,50|0,041|18,300|0,086|

c) Método AC-DGA

En este caso, se plantea una ecuación para calcular el caudal máximo medio diario,
que varía en función de la región de Chile en que ella sea aplicada. Las regiones consideradas van
desde la III a la IX región. Para el área de estudio, se consideró válida la relación de la III Región
que se presenta a continuación:

Q = (1,94 * 10 [-7] ) *CF(T)* P 243,108 *A 0,776 (5)

Q : caudal máximo medio diario (m3/s)
CF(T) : coeficiente de frecuencia de período de retorno T.
P 24 : precipitación máxima diaria de período de retorno T= 10 años, expresada en mm.
A : área de la cuenca (km [2] )

En este último método el caudal máximo instantáneo se obtiene amplificando la
ecuación (5) por un factor. En este caso, se utilizó 1,40, obtenido de la publicación de la DGA antes
mencionada, que corresponde a la Zona Homogénea Gp C Loa Controlada .

7

Cuadro No9

Caudal Máximo Instantáneo según DGA-AC
Quebrada Sin Nombre en Parque Fotovoltaico Barriles

|Periodo de retorno T|CF(T)|Qmax(T,t)|
|---|---|---|
|(años)||(m3/s)|
|2|0,650|0,002|
|5|0,860|0,002|
|10|1,000|0,003|
|25|1,230|0,003|
|50|1,400|0,004|
|100|1,560|0,004|
|200|1,880|0,005|

(*) Coeficientes de Frecuencia según Manual DGA. Para T = 200 años se extrapoló

d) Resumen de Caudales de Crecida según los diferentes Métodos

En el Cuadro No 10 se presentan los caudales obtenidos con los distintos métodos.

Cuadro No 10

Caudal máximo instantáneo (m3/s) según los diferentes métodos
Quebrada Sin Nombre en Parque Fotovoltaico Barriles

8

|T (años)|Método|Col3|Col4|
|---|---|---|---|
||Racional|Verni-King|DGA-AC|
|2|0,036|0,010|0,002|
|5|0,081|0,020|0,002|
|10|0,124|0,027|0,003|
|25|0,212|0,041|0,003|
|50|0,295|0,053|0,004|
|100|0,397|0,066|0,004|
|200|0,553|0,086|0,005|

e) Elección del método para el cálculo del caudal de crecida

Según los resultados obtenidos se seleccionan los caudales del Método de
Racional, por ser el que entrega mayores caudales para el período de retorno T = 200 años, que es
el caudal de diseño de las obras, los que se presentan en el Cuadro No 11.

Cuadro No 11

Caudal Máximo Instantáneo Adoptado
Quebrada Sin Nombre en Parque Fotovoltaico Barriles

9

|Periodo de retorno T|Q|
|---|---|
|(años)|(m3/s)|
|2|0,036|
|5|0,081|
|10|0,124|
|25|0,212|
|50|0,295|
|100|0,397|
|200|0,553|

# 1.2) CUENCA ÁREA DE ESTUDIO

10

FIGURA 1 Cuenca aportante a zona de estudio

11