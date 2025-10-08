---
title: Sin título
author: Eduardo Henriquez
date: D:20191121075221-03'00'
language: es
type: report
pages: 50
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CORRENTOMETRÍA ADCP SECTOR: Concesión 276
  - Tabla de Contenidos
  - 1. INTRODUCCIÓN
  - 2.- MATERIALES Y MÉTODOS
  - 3. RESULTADOS
  - 4. CONCLUSIÓN Y DISCUSIÓN
  - 5. ANEXO
-->

# CORRENTOMETRÍA ADCP SECTOR: Concesión 276

# Tabla de Contenidos

**1.** **INTRODUCCIÓN ..................................................................................................................................... 3**

**2.- MATERIALES Y MÉTODOS ...................................................................................................................... 4**

**2.1 Antecedentes generales ..................................................................................................................................... 4**
**2.2 Tipos de Mediciones ........................................................................................................................................... 5**
**2.3 Procesamiento de Datos ADCP ......................................................................................................................... 9**

**3. RESULTADOS .......................................................................................................................................... 11**

**3.1.- Parámetros de funcionamiento ...................................................................................................................... 11**
**3.2- Velocidad y dirección de corrientes ............................................................................................................... 13**

**4. CONCLUSIÓN Y DISCUSIÓN ................................................................................................................... 17**

**5. ANEXO ...................................................................................................................................................... 18**

**5.1- Tablas estadísticas .......................................................................................................................................... 18**
**5.2 Velocidades promedio en perfil de profundidad ............................................................................................ 24**
**5.3 Grafica de contornos ........................................................................................................................................ 26**
**5.4 Gráficas polares ................................................................................................................................................ 27**
**5.5 Componentes u y v ........................................................................................................................................... 35**
**5.6 Vector Progresivo ............................................................................................................................................. 43**

2

www.innovex.cl

# 1. INTRODUCCIÓN

El presente estudio corresponde a las mediciones de velocidad y dirección de corrientes en la Concesión 276,

en el sector del Golfo de Xaltegua, ubicado en la región de Magallanes y la Antártica Chilena.

Las mediciones se realizaron con dos correntómetros eulerianos del tipo ADCP (Acoustic Doppler Current

Profilers), siendo uno de los ADCP instalado mirando hacia arriba a una profundidad promedio de 71.1 metros,

mientras que el otro ADCP fue instalado mirando hacia abajo a una profundidad promedio de 72.2 metros,

este diseño de anclaje se realizó con la finalidad de abarcar toda la columna de agua. Los equipos estuvieron

monitoreando durante 42 días consecutivos, desde el jueves 25 de Julio hasta el jueves 5 de Septiembre del

2019, con un intervalo de medición de 10 min para la dirección y velocidad de la corriente.

Este estudio fue realizado con la finalidad de tener una línea base, y con esto obtener una visión de la dinámica

en la Concesión 276, con esta información se pretende poder mejorar la toma de decisiones asociadas a el

desarrollo de la acuicultura en el lugar.

3

www.innovex.cl

# 2.- MATERIALES Y MÉTODOS

**2.1 Antecedentes generales**

El presente estudio describe el comportamiento dinámico de las corrientes marinas en la Concesión 276,

ubicada en el Golfo de Xaltegua, en la región de Magallanes y la Antártica Chilena. Las mediciones de

corrientes se realizaron con dos correntómetros eulerianos del tipo ADCP (Acoustic Doppler Current Profilers),

fondeados uno a 71.1 metros y el otro a 72,2 metros de profundidad, con el primero midiendo hacia la

superficie y el otro midiendo hacia el fondo respectivamente . Con estos dos correntómetros fondeados a

distintas profundidades se pudo abarcar toda la columna de agua del sector ya mencionado de 140 metros

de profundidad (Figura 1).

|Tabla 1: coordenadas del equipo.|Col2|Col3|
|---|---|---|
|**Coordenada**|**Geográficas**|**UTM**|
|**Latitud**|53° 8’ 11.0'' Sur|651834.07 m Este|
|**Longitud**<br>|72° 43' 48.8'' Oeste|4110150.45 m Sur|

Estas mediciones se realizaron de manera continua durante 42 días, comprendidos desde el jueves 25 de

Julio hasta el jueves 5 de Septiembre del 2019.

**Figura 1.-** Imagen del sitio de estudio y el punto de instalación de los equipos ADCP, en color rojo los ADCP

fondeados a 71 y 72 metros de profundidad.

4

www.innovex.cl

Durante el tiempo de muestreo se presentaron tres mareas de sicigia y dos mareas de cuadratura. El día 31

de Julio a las 23:12 (Luna Nueva), el día 7 de Agosto a las 13:31 (Creciente), el día 15 de Agosto a las 8:29

(Luna Llena), el día 23 de Agosto a las 10:56 (Menguante) y el día 30 de Agosto a las 6:37 (Luna Nueva).

**2.2 Tipos de Mediciones**

**2.2.1 Correntómetros ADCP**

Para realizar el estudio de correntometría se utilizaron dos equipos ADCP (Acoustic Doppler Current Profiler),

modelos LinkQuest 600 (Figura 2). Estos equipos midieron la velocidad y dirección de corrientes de manera

continua durante 42 días desde el 25 de Julio hasta el 5 de Septiembre de 2019.

Estos equipos poseen una batería y memoria interna con capacidad de almacenamiento suficiente para

realizar los trabajos proyectados en este estudio. El registro de coordenadas para ubicación de equipo fue

realizado con un GPS con una precisión menor a 10 m.

La línea de fondeo utilizó dos correntómetros, el primer equipo quedo fondeado a 71,1 metros con el cabezal

apuntando a la superficie para medir la primera parte de la columna de agua (desde los 7 a 65 metros) y el

segundo equipo quedo fondeado a 72,2 metros con el cabezal apuntando al fondo para medir la capa más

profunda de la columna de agua (desde los 76 a 130 metros). En suma, con estos dos equipos fondeados a

distintas profundidades se pudo medir prácticamente la totalidad de la columna de agua.

Los ADCP se programaron para realizar mediciones de dirección y velocidad de la corriente cada 10 min con

una resolución vertical (capas) de 2 metros, generando entre ambos ADCP 58 capas validas de medición a

lo largo de la columna de agua, 30 capas que abarcan desde los 7 a los 65 metros y 28 capas que abarcan

desde los 76 hasta los 130 metros.

5

www.innovex.cl

**Figura 2.-** Imagen que muestra el esquema de fondeo de los equipos a 71 y 72 metros respectivamente (derecha) y

ficha técnica del correntómetro ADCP FlowQuest 600 (izquierda).

6

www.innovex.cl

El blanking del equipo FlowQuest 600 es de 70 cm, pero además debemos aplicar una formula indicada por

el fabricante, con la cual determinamos desde que capa es posible comenzar a tener datos sin ruido en el

fondo. Una vez aplicada esta fórmula nos da como resultado que podemos comenzar a trabajar con los datos

desde los 65 metros hacia la superficie con el primer equipo y desde los 76 metros hacia el fondo con el

segundo equipo.

La fórmula es descrita a continuación:

_(User set trasducer depth) +/- (Blanck_dist + (n+1.5)* bin_length)_

_Where n=0,1,2...; +/- stands for downwards or upwards._

Por sugerencia del fabricante, se elimina un rango de profundidad que tiene que ver con la distancia que existe

entre el transductor y la interfaz, ya sea océano-atmósfera o fondo marino, de esta distancia cerca de un 10%

debe ser eliminado por tener ruido.

Al graficar todas las celdas medidas desde el transductor a superficie(Figura 3) se puede observar que a partir

de los 7 metros hasta la superficie la señal se observa con ruido, se puede identificar claramente las capas

que fueron eliminadas.

7

www.innovex.cl

**Figura 3.-** Grafica de las componentes u, v, y w para todas las celdas registradas por el ADCP anclado mirando hacia
superficie.

Al graficar todas las celdas medidas desde el transductor al fondo(Figura 4) se puede observar que a partir

de los 130 metros hasta el fondo, la señal se observa con ruido, se puede identificar claramente las capas

que fueron eliminadas por este motivo.

**Figura 4.-** Grafica de las componentes u, v, y w para todas las celdas registradas por el ADCP desde la celda más
cercana al transductor hasta la máxima profundidad del punto registrado

8

www.innovex.cl

**2.3 Procesamiento de datos ADCP**

Cabe destacar que los datos de corrientes fueron analizados en forma de componentes ortogonales (u,v),

donde la componente "u" representa las corrientes registradas en el eje Este-Oeste, mientras que la

componente "v" representa las corrientes registradas en el eje Norte-Sur.

Un segundo criterio consideró la corrección de la dirección, debido a que el compás magnético del ADCP es

afectado por la desviación magnética local.

Los registros de la dirección de las corrientes se encuentran referidos al norte magnético, para el análisis de

la información, la dirección fue referida al norte geográfico, empleándose para tal efecto la corrección de 14.5°

Este(2019 - 0.08° Oeste/año) de desviación magnética local, calculada utilizando el módelo geo-magnético

del National Geophysical Data Centercalculada utilizando el modelo geo-magnético del Nacional Geophysical

[Data Center.( (https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml?useFullSite=true).](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml?useFullSite=true)

Los datos de los dos correntómetros fueron procesados en el software Matlab. Mediante este programa fueron

calculados los diferentes parámetros de interés, para la realización del informe. El informe que se entrega

contiene los siguientes cálculos:

 Tabla Excel con los datos de correntometría (día, hora, velocidad y dirección).

 Serie de tiempo (velocidad N-S y O-E).

 - Gráfico Polar.

 Gráfico de Vector Progresivo.

 - Gráfico de contornos

 Gráfico de parámetros de funcionamiento del equipo

Las estadísticas realizadas sobre las series incluyen los valores máximos y promedios de velocidades de

corrientes, además estadígrafos como la desviación estándar, moda y mediana.

9

www.innovex.cl

La totalidad de las gráficas de vectores polares o vector progresivo, están orientadas en el plano cartesiano

de forma tal que la componente de velocidad Norte calce con el eje Y del mapa cartesiano, y la componente

Este Oeste con el eje X (positivo hacia el Este).

El cálculo del vector progresivo representa el movimiento teórico de una partícula considerando la velocidad

y dirección horaria, en un ambiente que no considera costas cercanas que influyan en la variación de este

avance. Cabe hacer notar que el diagrama de vector progresivo no representa la trayectoria del mismo

volumen de agua a intervalos sucesivos de tiempo. Por el contrario simula la trayectoria que tendría una

partícula en caso que toda el agua, dentro de varios kilómetros del punto de medición, tuviese la misma

velocidad constante.

En la gráfica polar se observa la totalidad de registros de velocidad y dirección en una sola vista, es decir,

cada registro de corrientes que se tomó está representado por un punto. Mientras más lejos los puntos del

centro, mayor es la velocidad representada.

10

www.innovex.cl

# 3. RESULTADOS

**3.1.- Parámetros de funcionamiento**

Los parámetros de funcionamiento de los equipos durante el estudio de correntometría indican un correcto

funcionamiento de los dos correntómetros ADCP.

Se observa que el primer equipo estuvo fondeado a 71,1 metros de profundidad en promedio, en esta

profundidad el sensor de temperatura registró que el agua se encuentra en promedio a los 9 °C mostrando

una leve variabilidad. Se observa que los parámetros de inclinación (Pitch, Roll y Heading) están dentro de lo

indicado por el fabricante del equipo (hasta 15o pitch y roll). El voltaje de la batería disminuyó de manera

paulatina a través del estudio, manteniéndose siempre por sobre el umbral mínimo para el correcto

funcionamiento. Por su parte el sensor de presión muestra que el equipo estuvo fondeado a 71,1 metros con

variaciones mareales de aproximadamente 1,5 metros (Figura 5).

**Figura 5.-** Parámetros de funcionamiento del equipo instalado a 71,1 metros midiendo la parte superficial de la

columna de agua.

11

www.innovex.cl

Se observa que el segundo equipo estuvo fondeado a 72,2 metros de profundidad en promedio, en esta

profundidad el sensor de temperatura registró que el agua se encuentra en promedio a los 9,2 °C mostrando

una leve variabilidad. Se observa que los parámetros de inclinación (Pitch, Roll y Heading) están dentro de lo

indicado por el fabricante del equipo (hasta 15o pitch y roll). El voltaje de la batería disminuyó de manera

paulatina a través del estudio, manteniéndose siempre por sobre el umbral mínimo para el correcto

funcionamiento. Por su parte el sensor de presión muestra que el equipo estuvo fondeado a 72,2 metros con

variaciones mareales de aproximadamente 1,5 metros (Figura 6).

**Figura 6.-** Parámetros de funcionamiento del equipo instalado a 72,2 metros midiendo la parte más profunda de la

columna de agua.

12

www.innovex.cl

**3.2- Velocidad y dirección de corrientes**

En la Concesión 276 se observa que la magnitud promedio de la velocidad fluctúa entre 1,65 (110 metros) y

30,78 cm/s (7 metros) en toda la columna de agua, encontrándose las mayores velocidades promedios en la

parte superficial de la columna desde los 7 a los 13 metros, mientras que las menores velocidades promedios

se encontraron desde los 98 a 112 metros de profundidad. En líneas generales se aprecia que la velocidad

tiende a disminuir a medida que aumenta la profundidad y los valores máximos registrados fluctuaron entre

9,34 y 77,77 cm/s (Anexo 5.1 - Tabla 1).

Al observar las velocidades agrupadas por rangos de velocidad en la tabla de frecuencias, se puede apreciar

que en la primera capa a los 7 metros la mayor cantidad de datos se agrupa entre los 30 y 250 cm/s, a los 9

metros los datos se agrupan de 10 a 20 cm/s, a los 11 metros de 15 a 25 cm/s y finalmente a los 13 metros

de los 5 a 15 cm/s. Posteriormente, desde los 15 a los 76 metros la mayoría de los datos se agrupa en los

rangos que van desde 1,5 a 10 cm/s con aproximadamente el 80% de los datos. Luego, desde los 78 a los

130 metros los rangos que predominan van desde 0 a 5 cm/s por sobre el 95% de los datos en la mayoría de

las capas (Anexo 5.1 - Tabla 2).

En cuanto a los registros de la dirección de la corriente, a los 7 metros la dirección de la corriente es Noreste

(NE) y Suroeste (SO). Luego, desde los 9 a los 23 metros toma mayor importancia la componente Oeste (O),

seguido de las componentes Noroeste (NO) y Suroeste (SO). Posteriormente, desde los 25 a los 84 metros

la componente Sur (S) es la predominante, seguida de la componente Suroeste (SO) hasta los 39 metros y la

componente Norte (N) desde los 41 metros . Siguiendo con la columna, desde los 86 a los 120 metros

predomina la dirección Norte (N). Por último, desde los 122 a los 130 metros la dirección predomínate es Este

(E), seguida de la componente Norte (N) hasta los 126 metros y la componente Sureste (SE) desde los 126

metros (Anexo 5.1 - Tabla 3).

En las velocidades promedio en un perfil de profundidad, estas velocidades darían una idea del lugar hacia

donde se estarían acumulando las partículas en el agua en el sector de estudio.

En la componente V (Norte-Sur) es posible distinguir que de los 7 hasta los 13 metros de profundidad la

columna de agua va en dirección Sur (S) con una velocidad máxima de 3 cm/s, desde los 15 a los 19 metros

la columna va en dirección Norte (N) con magnitudes inferiores a 1 cm/s. Desde los 21 a 86 metros de

13

www.innovex.cl

profundidad la columna de agua vuelve a ir en dirección Sur (S) con velocidades inferiores a 3 cm/s. Por

último, desde los 88 a 130 metros de profundidad la columna se orienta en dirección Norte (N) con velocidades

inferiores a 1 cm/s (Anexo 5.2 - Velocidades Promedios en Perfil de Profundidad).

En la componente Este-Oeste (U) se puede observar que en la primera capa a los 7 metros la dirección es

Este (E) con una velocidad inferior a 8 cm/s. Luego, desde los 9 a los 110 metros la dirección de la velocidad

promedio es Oeste (O) disminuyendo en función de la profundidad. Por último, en la parte más profunda de

la columna desde 112 hasta 130 metros la dirección predominante vuelve a ser Este (E) con velocidades

inferiores a 1 cm/s .

La componente W (ascendente-descendente) nos muestra las velocidades y dirección en el eje vertical de la

columna de agua. En este caso valores positivos es una masa de agua ascendente (hacia superficie) y valores

negativos una masa de agua descendente (hacia el fondo). En este estudio, podemos observar que desde

los 7 a 25 metros tiene dirección descendente con velocidades promedio inferiores a 3 cm/s. Luego, de los 27

a los 76 metros tiene dirección ascendente con valores inferiores a 0,4 cm/s. Posteriormente, desde los 78 a

112 metros vuelve a tener una dirección descendente con velocidades inferiores a 0,2 cm/s. Por último, en la

parte final de la columna de agua desde los 114 hasta los 130 metros de profundidad la columna de agua

tiene dirección ascendente con una velocidad promedio que va aumentando en función de la profundidad

llegando hasta los 0,6 cm/s (Anexo 5.2 - Velocidades Promedios en Perfil de Profundidad).

La gráfica de contornos con flujos instantáneos muestra los valores de velocidad y dirección de corrientes

medidos, los que posteriormente fueron promediados horariamente. En las gráficas de contornos están

incluidos el 100% de los datos para cada profundidad promediados cada una hora, lo que nos permite

visualizar el comportamiento de la masa de agua completa durante los 42 días de mediciones en las distintas

componentes. Los colores indican dirección, y la intensidad de los colores indican una mayor o menor

velocidad de corrientes.

Si analizamos solamente la componente V (Norte-Sur) podemos observar que las velocidades y direcciones

van variando a través del tiempo, alcanzando magnitudes que llegan a los 40 cm/s hacia el Sur (S) y 40 cm/s

hacia el Norte (N) en algunos períodos. Así mismo, desde los 82 hasta los 130 metros podemos observar que

las velocidades y direcciones van variando a través del tiempo (Anexo 5.3 - Grafica de Contornos).

14

www.innovex.cl

En general, al observar la componente V, podemos ver que predomina el movimiento en dirección Norte (N),

pero con bajas velocidades, con algunos cambios en la magnitud a través del tiempo (Anexo 5.3 - Grafica de

Contornos).

Para el caso de la componente U, predomina la dirección Este (E) con alguna variaciones al Oeste (O) durante

el tiempo de muestreo (Anexo 5.3 - Grafica de Contornos).

La componente vertical W, muestra leves velocidades en dirección y descendente la mayor parte del

monitoreo (Anexo 5.3 - Grafica de Contornos).

En las gráficas polares se puede observar la magnitud y dirección de la velocidad, donde cada punto indica

una medición. Estas muestran que la capa de los 7 metros hay una marcada dirección Noreste (NE) y Suroeste

(SO), luego los 9 a 21 metros la nube se hace algo más difusa pero se aprecia el dominio de la componente

Oeste (O). Desde los 23 hasta los 82 metros se aprecia con claridad la dirección de la corriente de Sur (S).

Desde los 84 a los 120 metros la componentes Norte (N) es la predominante y en cuanto a la intensidad esta

disminuye en función de la profundidad. Por último, desde los 122 a 130 metros la componente predominante

es Este (E) apreciándose con mayor claridad en la última capa (Anexo 5.4 - Gráficas polares).

Las gráficas de las componentes Norte-Sur (meridional) y Este-Oeste (zonal) a través del tiempo muestran

las variaciones de la velocidad para las distintas profundidades de la columna. Se observa que en la primera

capa tanto la componente zonal como meridional alcanzan su mayor valor llegando por sobre los 50 cm/s.

Luego, a medida que aumenta la profundidad comienza a disminuir la intensidad de la corriente y la mayor

amplitud se da en las componentes meridionales. En la parte más profunda de la columna de agua desde 126

a los 130 metros tanto la componente zonal vuelve a ser la predominante alcanzando su mayor amplitud a los

130 metros (Anexo 5.5 - Componentes _u_ y _v_ ).

En la gráfica del vector progresivo se observa la trayectoria que seguiría una partícula. En base a eso podemos

ver en las gráficas que de los 7 a 13 metros las partículas alcanzan su mayor desplazamiento llegando en la

capa de los 11 metros a 80 km al Sur (S) y 280 km al Oeste (O). De los 15 a los 19 metros las partículas

siguen trayectorias similares y el desplazamiento va disminuyendo paulatinamente. Luego, desde los 21 a 86

metros la posición final de las partículas es Suroeste (SO) con excepción de la capa de los 76 metros que

15

www.innovex.cl

termina en posición Sureste (SE). Desde los 88 a 108 metros la posición final es Noroeste (NO) y el

desplazamiento cada vez es menor. Luego, desde los 112 a los 128 metros la posición final de las partículas

es Noreste (NE) con un aumento de trayectoria en las ultimas capas y finalmente en la última capa la partícula

termina en una posición final Sureste (SE), exactamente 3,5 km al Sur (S) y 38 km al Este (E) (Anexo 5.6Vector progresivo).

16

www.innovex.cl

# 4. CONCLUSIÓN Y DISCUSIÓN

La correntometría euleriana mostró que la corriente en la primera capa es de Suroeste (SO) a Noreste (NE) y

en la mayor parte de la columna de agua es en dirección predominante es Sur (S) y Norte (N), con variaciones

en menor medida a través de las diferentes capas especialmente en la parte superficial y en la parte más

profunda de la columna.

En cuanto a la magnitud promedio de la velocidad en la Concesión 276 esta fluctúa entre 1,65 y 30,78 cm/s,

siendo la máxima magnitud registrada de 77,77 cm/s correspondiente a los 7 metros de profundidad. Se

aprecia que la magnitud de la corriente va disminuyendo paulatinamente con la profundidad, aunque presenta

un leve aumento en las celdas cercanas al fondo de la columna.

Mediante las gráficas de vector progresivo, es posible observar que el grado de dispersión en el sector es

mayor en las capas superficiales hacia una posición final Suroeste (SO). A medida que aumenta la profundidad

la capacidad de dispersión es menor, salvo las últimas celdas de la columna.

17

www.innovex.cl

# 5. ANEXO

**5.1- Tablas estadísticas**

**Tabla 2.-** Estadística descriptiva de la magnitud de la corriente. Velocidad en cm/s.

|Profundidad|X|Min|Max|D.E.|Moda|Mediana|
|---|---|---|---|---|---|---|
|**-7**|30,78|0,30|77,77|17,15|18,92|31,21|
|**-9**|14,09|0,00|40,02|7,15|10,26|14,45|
|**-11**|16,14|0,00|33,75|8,27|1,30|17,62|
|**-13**|10,83|0,00|29,12|5,38|8,32|10,76|
|**-15**|5,91|0,00|22,13|3,19|4,74|5,49|
|**-17**|5,84|0,00|24,81|3,32|3,61|5,36|
|**-19**|5,68|0,00|21,77|3,21|3,40|5,24|
|**-21**|5,61|0,00|21,93|3,10|4,10|5,20|
|**-23**|5,65|0,00|18,68|3,05|4,30|5,23|
|**-25**|5,66|0,00|20,11|3,18|4,00|5,26|
|**-27**|5,63|0,00|23,65|3,38|5,10|5,07|
|**-29**|5,44|0,00|21,21|3,40|1,30|4,77|
|**-31**|5,20|0,00|22,05|3,44|1,70|4,48|
|**-33**|5,03|0,00|22,17|3,41|3,00|4,22|
|**-35**|4,85|0,00|20,22|3,25|1,80|4,10|
|**-37**|4,64|0,00|21,42|3,14|1,70|3,93|
|**-39**|4,44|0,00|19,07|3,04|1,70|3,77|
|**-41**|4,49|0,00|21,71|2,99|3,00|3,81|
|**-43**|4,69|0,00|24,03|3,08|1,80|3,96|
|**-45**|4,79|0,00|20,52|3,18|1,20|4,07|
|**-47**|4,79|0,00|19,04|3,25|1,70|4,04|
|**-49**|4,76|0,00|20,93|3,30|1,30|3,96|
|**-51**|4,69|0,00|22,01|3,40|1,30|3,83|
|**-53**|4,65|0,00|22,99|3,42|1,30|3,76|
|**-55**|4,64|0,00|23,56|3,48|1,30|3,70|
|**-57**|4,65|0,00|24,14|3,61|1,20|3,70|
|**-59**|4,62|0,00|27,12|3,66|1,30|3,58|
|**-61**|4,56|0,00|25,65|3,70|2,20|3,45|
|**-63**|4,53|0,00|26,01|3,81|1,30|3,34|
|**-65**|4,58|0,00|25,55|3,98|1,30|3,32|
|**-76**|4,07|0,00|26,25|3,03|1,70|3,45|
|**-78**|2,57|0,00|26,38|2,53|1,00|1,97|
|**-80**|2,28|0,00|24,96|2,10|0,00|1,80|

www.innovex.cl

18

|-82|2,09|0,00|18,94|1,76|1,00|1,70|
|---|---|---|---|---|---|---|
|**-84**|1,95|0,00|14,27|1,50|1,00|1,63|
|**-86**|1,85|0,00|11,98|1,32|0,00|1,60|
|**-88**|1,80|0,00|13,24|1,20|1,00|1,58|
|**-90**|1,77|0,00|13,46|1,16|0,00|1,60|
|**-92**|1,73|0,00|14,33|1,14|0,00|1,53|
|**-94**|1,71|0,00|9,42|1,12|0,00|1,53|
|**-96**|1,71|0,00|9,95|1,08|0,00|1,56|
|**-98**|1,68|0,00|11,04|1,06|0,00|1,52|
|**-100**|1,64|0,00|9,34|1,04|0,00|1,50|
|**-102**|1,65|0,00|9,49|1,05|0,00|1,50|
|**-104**|1,67|0,00|10,10|1,06|1,30|1,50|
|**-106**|1,66|0,00|14,78|1,08|0,00|1,50|
|**-108**|1,66|0,00|25,51|1,11|1,00|1,50|
|**-110**|1,65|0,00|27,31|1,11|0,00|1,50|
|**-112**|1,67|0,00|21,71|1,10|1,00|1,50|
|**-114**|1,71|0,00|13,67|1,08|1,00|1,56|
|**-116**|1,80|0,00|18,88|1,16|0,50|1,61|
|**-118**|1,87|0,00|23,01|1,21|1,30|1,70|
|**-120**|1,97|0,00|20,84|1,26|1,30|1,77|
|**-122**|2,07|0,00|13,84|1,29|1,20|1,84|
|**-124**|2,19|0,00|11,11|1,35|1,00|1,97|
|**-126**|2,32|0,00|14,04|1,47|1,00|2,06|
|**-128**|2,51|0,00|11,77|1,56|1,70|2,22|
|**-130**<br>|3,54|0,00|19,39|2,43|1,70|3,00|

www.innovex.cl

19

**Tabla 3.-** Distribución de frecuencia de la magnitud para el período completo de muestreo, expresado en porcentaje.

|Profundi<br>dad|[0,0 -<br>1,5]|[01,5-<br>3,0]|[3,0 -<br>5,0]|[5,0 -<br>10,0]|[10,0 -<br>15,0]|[15,0 -<br>20,0]|[20,0 -<br>25,0]|[25,0 -<br>30,0]|[30,0 -<br>250,0]|
|---|---|---|---|---|---|---|---|---|---|
|**-7**|0,78|2,59|3,33|9,23|6,90|7,17|8,45|9,01|52,54|
|**-9**|2,46|5,27|6,19|14,95|24,53|26,26|14,25|4,77|1,31|
|**-11**|2,88|5,36|6,92|11,71|13,52|20,04|25,11|12,91|1,56|
|**-13**|2,25|5,32|9,31|28,31|31,45|18,71|4,46|0,20|0,00|
|**-15**|5,57|13,85|24,28|45,24|10,19|0,81|0,05|0,00|0,00|
|**-17**|6,07|14,83|24,43|43,31|10,09|1,20|0,07|0,00|0,00|
|**-19**|6,45|15,38|25,41|42,23|9,76|0,73|0,03|0,00|0,00|
|**-21**|6,65|15,35|25,54|43,37|8,56|0,50|0,02|0,00|0,00|
|**-23**|6,29|14,54|26,04|43,14|9,65|0,35|0,00|0,00|0,00|
|**-25**|6,69|16,50|23,93|42,57|9,80|0,50|0,02|0,00|0,00|
|**-27**|7,83|16,36|24,88|39,73|9,96|1,16|0,07|0,00|0,00|
|**-29**|8,51|17,65|26,91|36,62|8,73|1,50|0,08|0,00|0,00|
|**-31**|9,01|20,24|27,51|33,76|7,65|1,70|0,13|0,00|0,00|
|**-33**|10,06|20,66|29,60|30,35|7,35|1,95|0,03|0,00|0,00|
|**-35**|11,21|21,47|29,42|29,35|7,52|1,00|0,03|0,00|0,00|
|**-37**|11,64|23,27|29,64|27,97|6,44|1,03|0,02|0,00|0,00|
|**-39**|13,65|24,26|28,37|27,47|5,49|0,75|0,00|0,00|0,00|
|**-41**|12,96|24,86|27,31|28,89|5,60|0,37|0,02|0,00|0,00|
|**-43**|11,57|23,05|27,99|30,40|6,52|0,45|0,02|0,00|0,00|
|**-45**|11,79|22,67|26,97|30,92|6,95|0,68|0,02|0,00|0,00|
|**-47**|12,32|22,90|26,64|29,62|7,75|0,77|0,00|0,00|0,00|
|**-49**|12,39|23,18|27,16|29,24|6,84|1,16|0,03|0,00|0,00|
|**-51**|14,32|23,37|26,23|28,29|6,24|1,51|0,05|0,00|0,00|
|**-53**|14,00|24,55|26,71|26,91|6,30|1,40|0,13|0,00|0,00|
|**-55**|13,82|25,43|26,43|25,91|6,79|1,28|0,35|0,00|0,00|
|**-57**|14,67|25,64|25,43|25,49|6,69|1,61|0,47|0,00|0,00|
|**-59**|15,58|25,64|25,16|24,65|7,18|1,30|0,43|0,05|0,00|
|**-61**|18,71|26,14|22,78|23,03|6,69|2,10|0,53|0,02|0,00|
|**-63**|18,71|26,14|22,78|23,03|6,69|2,10|0,53|0,02|0,00|
|**-65**|17,05|27,61|24,06|21,75|6,02|2,81|0,65|0,05|0,00|
|**-76**|14,64|27,70|30,48|23,43|2,29|1,01|0,40|0,05|0,00|
|**-78**|35,76|38,83|16,62|6,35|1,61|0,58|0,23|0,02|0,00|
|**-80**|39,75|38,63|14,89|5,48|0,71|0,47|0,07|0,00|0,00|
|**-82**|39,75|38,63|14,89|5,48|0,71|0,47|0,07|0,00|0,00|
|**-84**|45,35|38,47|12,35|3,41|0,43|0,00|0,00|0,00|0,00|
|**-86**|46,83|38,47|12,01|2,61|0,08|0,00|0,00|0,00|0,00|
|**-88**|47,36|39,13|11,60|1,88|0,03|0,00|0,00|0,00|0,00|

20

www.innovex.cl

|-90|47,04|39,95|11,58|1,40|0,03|0,00|0,00|0,00|0,00|
|---|---|---|---|---|---|---|---|---|---|
|**-92**|49,04|38,80|10,73|1,41|0,02|0,00|0,00|0,00|0,00|
|**-94**|49,25|38,95|10,67|1,13|0,00|0,00|0,00|0,00|0,00|
|**-96**|48,70|40,08|10,17|1,05|0,00|0,00|0,00|0,00|0,00|
|**-98**|49,65|39,56|9,97|0,80|0,02|0,00|0,00|0,00|0,00|
|**-100**|51,33|38,45|9,59|0,63|0,00|0,00|0,00|0,00|0,00|
|**-102**|50,88|39,00|9,45|0,66|0,00|0,00|0,00|0,00|0,00|
|**-104**|50,52|38,60|10,09|0,78|0,02|0,00|0,00|0,00|0,00|
|**-106**|51,28|38,30|9,47|0,91|0,03|0,00|0,00|0,00|0,00|
|**-108**|51,23|38,38|9,27|1,10|0,00|0,00|0,00|0,02|0,00|
|**-110**|51,10|38,42|9,52|0,95|0,00|0,00|0,00|0,02|0,00|
|**-112**|50,80|38,20|10,02|0,96|0,00|0,00|0,02|0,00|0,00|
|**-114**|48,17|40,66|10,19|0,95|0,03|0,00|0,00|0,00|0,00|
|**-116**|46,44|39,90|12,31|1,31|0,02|0,02|0,00|0,00|0,00|
|**-118**|43,95|40,30|14,16|1,58|0,00|0,00|0,02|0,00|0,00|
|**-120**|41,44|41,11|15,02|2,36|0,05|0,00|0,02|0,00|0,00|
|**-122**|38,04|42,02|17,20|2,71|0,03|0,00|0,00|0,00|0,00|
|**-124**|34,68|42,06|19,47|3,76|0,03|0,00|0,00|0,00|0,00|
|**-126**|33,18|40,00|21,50|5,22|0,10|0,00|0,00|0,00|0,00|
|**-128**|29,54|37,52|25,79|7,08|0,07|0,00|0,00|0,00|0,00|
|**-130**|20,59|29,51|27,28|20,54|2,04|0,03|0,00|0,00|0,00|

www.innovex.cl

21

**Tabla 4.-** Distribución de frecuencia de la dirección para el período completo de muestreo, expresado en porcentaje.

|Profundi<br>dad|[-22,5 -<br>22,5]|[22,5 -<br>67,5]|[67,5 -<br>112,5]|[112,5 -<br>157,5]|[157,5 -<br>202,5]|[202,5 -<br>247,5]|[247,5 -<br>292,5]|[292,5 -<br>337,5]|
|---|---|---|---|---|---|---|---|---|
|**Profundi**<br>**dad**|**N **|**NE**|**E **|**SE**|**S **|**SO**|**O **|**NO**|
|**-7**|3,69|31,30|18,68|6,32|12,57|19,09|5,55|2,79|
|**-9**|7,65|4,74|5,94|7,98|13,17|19,47|29,94|11,11|
|**-11**|2,99|8,75|15,13|2,21|4,51|22,48|41,49|2,43|
|**-13**|6,02|13,42|6,24|1,20|5,52|28,65|31,96|6,98|
|**-15**|12,64|5,99|3,48|2,79|11,86|16,60|23,62|23,03|
|**-17**|15,03|5,11|2,76|2,44|12,66|17,81|23,15|21,04|
|**-19**|14,50|5,44|2,64|2,61|14,65|17,81|21,20|21,14|
|**-21**|14,07|5,40|2,43|3,19|16,10|17,38|21,10|20,32|
|**-23**|14,67|5,32|2,88|3,63|18,61|18,21|17,94|18,74|
|**-25**|15,37|5,24|2,39|3,58|21,80|18,39|15,95|17,28|
|**-27**|14,25|5,22|2,83|3,11|24,56|20,46|13,79|15,78|
|**-29**|14,83|5,01|2,86|3,39|27,71|20,19|12,37|13,64|
|**-31**|14,77|5,60|2,93|3,74|28,14|20,52|11,91|12,39|
|**-33**|14,39|5,95|3,54|3,76|27,64|20,29|11,62|12,81|
|**-35**|15,53|6,05|4,06|3,89|27,36|18,31|12,22|12,57|
|**-37**|15,90|6,37|4,06|3,94|25,74|18,96|12,11|12,92|
|**-39**|16,16|6,27|4,51|4,54|25,15|17,96|11,41|14,00|
|**-41**|18,94|5,39|4,54|4,62|24,51|16,02|11,62|14,35|
|**-43**|21,24|5,40|4,22|5,11|24,61|14,73|10,36|14,32|
|**-45**|23,42|5,65|3,51|5,44|26,64|13,04|9,96|12,34|
|**-47**|23,57|4,79|3,53|5,55|28,06|12,16|9,31|13,04|
|**-49**|24,28|4,96|3,63|6,62|28,02|11,72|7,95|12,82|
|**-51**|24,21|5,47|4,22|7,22|27,77|10,38|7,77|12,96|
|**-53**|24,83|5,50|4,27|7,18|29,07|9,48|7,32|12,34|
|**-55**|24,90|5,72|3,44|6,64|29,42|10,33|6,93|12,62|
|**-57**|25,91|5,22|3,61|6,09|28,52|10,11|7,27|13,27|
|**-59**|26,18|4,47|3,16|5,82|27,22|10,78|7,77|14,60|
|**-61**|25,30|5,01|3,34|4,94|27,14|10,54|8,66|15,07|
|**-63**|24,38|5,69|3,74|5,21|26,64|9,86|9,06|15,42|
|**-65**|22,98|5,77|3,84|4,79|26,34|11,72|9,71|14,83|
|**-76**|8,36|8,33|14,57|13,43|24,88|14,02|10,17|6,25|
|**-78**|14,59|7,56|7,79|7,53|21,97|15,79|15,45|9,32|
|**-80**|15,07|7,68|8,77|8,74|19,52|15,29|14,96|9,97|
|**-82**|15,64|7,31|9,65|8,06|19,04|15,10|15,27|9,92|
|**-84**|16,35|8,06|9,39|8,26|16,98|14,31|15,57|11,08|
|**-86**|18,58|8,01|10,50|7,63|15,34|13,38|16,20|10,37|

22

www.innovex.cl

|-88|19,31|8,39|10,19|7,68|14,84|12,25|15,95|11,40|
|---|---|---|---|---|---|---|---|---|
|**-90**|20,09|9,04|9,54|7,64|14,82|11,10|16,42|11,35|
|**-92**|20,84|8,79|9,99|7,38|14,32|11,17|15,82|11,70|
|**-94**|20,82|8,74|10,10|7,08|14,46|10,80|15,95|12,05|
|**-96**|19,91|8,96|10,19|7,24|13,71|10,92|16,15|12,93|
|**-98**|21,07|9,11|10,27|6,70|13,84|10,65|16,58|11,78|
|**-100**|21,75|8,57|10,30|7,33|13,23|10,80|16,18|11,83|
|**-102**|20,54|9,22|11,28|7,64|13,84|11,32|14,76|11,40|
|**-104**|20,51|9,52|11,43|7,84|15,07|10,39|15,02|10,22|
|**-106**|20,12|9,82|11,83|7,98|15,35|9,85|13,92|11,12|
|**-108**|19,87|10,24|12,55|8,81|14,72|9,74|13,73|10,35|
|**-110**|19,29|10,45|12,94|9,31|15,57|9,44|13,04|9,95|
|**-112**|19,01|10,75|13,38|9,12|14,92|10,05|12,98|9,79|
|**-114**|18,39|11,48|14,32|9,67|15,47|9,04|12,58|9,04|
|**-116**|18,13|11,81|14,41|10,39|14,92|9,22|12,11|9,01|
|**-118**|17,76|12,50|15,37|10,55|13,73|9,27|11,95|8,87|
|**-120**|15,89|14,16|15,45|11,38|13,19|8,96|10,90|10,07|
|**-122**|16,18|13,76|17,65|11,73|13,09|8,91|10,27|8,41|
|**-124**|15,09|14,46|17,86|12,45|13,68|7,79|10,27|8,41|
|**-126**|14,31|14,52|17,96|12,96|13,11|8,39|10,54|8,21|
|**-128**|13,16|15,29|17,81|14,07|12,20|8,99|9,95|8,52|
|**-130**|10,78|10,78|25,46|16,07|9,77|7,13|11,40|8,61|

www.innovex.cl

23

**5.2 Velocidades promedio en perfil de profundidad**

www.innovex.cl

24

25

www.innovex.cl

**5.3 Grafica de contornos**

26

www.innovex.cl

**5.4 Gráficas polares**

27

www.innovex.cl

28

www.innovex.cl

29

www.innovex.cl

30

www.innovex.cl

31

www.innovex.cl

32

www.innovex.cl

33

www.innovex.cl

34

www.innovex.cl

**5.5 Componentes u y v**

35

www.innovex.cl

36

www.innovex.cl

37

www.innovex.cl

38

www.innovex.cl

39

www.innovex.cl

40

www.innovex.cl

41

www.innovex.cl

42

www.innovex.cl

**5.6 Vector Progresivo**

43

www.innovex.cl

44

www.innovex.cl

45

www.innovex.cl

46

www.innovex.cl

47

www.innovex.cl

48

www.innovex.cl

49

www.innovex.cl

50

www.innovex.cl

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.-: ** Estadística descriptiva de la magnitud de la corriente. Velocidad en cm/s.**

| Profundidad | X | Min | Max | D.E. | Moda | Mediana |
| --- | --- | --- | --- | --- | --- | --- |
| **-7** | 30,78 | 0,30 | 77,77 | 17,15 | 18,92 | 31,21 |
| **-9** | 14,09 | 0,00 | 40,02 | 7,15 | 10,26 | 14,45 |
| **-11** | 16,14 | 0,00 | 33,75 | 8,27 | 1,30 | 17,62 |
| **-13** | 10,83 | 0,00 | 29,12 | 5,38 | 8,32 | 10,76 |
| **-15** | 5,91 | 0,00 | 22,13 | 3,19 | 4,74 | 5,49 |
| **-17** | 5,84 | 0,00 | 24,81 | 3,32 | 3,61 | 5,36 |
| **-19** | 5,68 | 0,00 | 21,77 | 3,21 | 3,40 | 5,24 |
| **-21** | 5,61 | 0,00 | 21,93 | 3,10 | 4,10 | 5,20 |
| **-23** | 5,65 | 0,00 | 18,68 | 3,05 | 4,30 | 5,23 |
| **-25** | 5,66 | 0,00 | 20,11 | 3,18 | 4,00 | 5,26 |
| **-27** | 5,63 | 0,00 | 23,65 | 3,38 | 5,10 | 5,07 |
| **-29** | 5,44 | 0,00 | 21,21 | 3,40 | 1,30 | 4,77 |
| **-31** | 5,20 | 0,00 | 22,05 | 3,44 | 1,70 | 4,48 |
| **-33** | 5,03 | 0,00 | 22,17 | 3,41 | 3,00 | 4,22 |
| **-35** | 4,85 | 0,00 | 20,22 | 3,25 | 1,80 | 4,10 |
| **-37** | 4,64 | 0,00 | 21,42 | 3,14 | 1,70 | 3,93 |
| **-39** | 4,44 | 0,00 | 19,07 | 3,04 | 1,70 | 3,77 |
| **-41** | 4,49 | 0,00 | 21,71 | 2,99 | 3,00 | 3,81 |
| **-43** | 4,69 | 0,00 | 24,03 | 3,08 | 1,80 | 3,96 |
| **-45** | 4,79 | 0,00 | 20,52 | 3,18 | 1,20 | 4,07 |
| **-47** | 4,79 | 0,00 | 19,04 | 3,25 | 1,70 | 4,04 |
| **-49** | 4,76 | 0,00 | 20,93 | 3,30 | 1,30 | 3,96 |
| **-51** | 4,69 | 0,00 | 22,01 | 3,40 | 1,30 | 3,83 |
| **-53** | 4,65 | 0,00 | 22,99 | 3,42 | 1,30 | 3,76 |
| **-55** | 4,64 | 0,00 | 23,56 | 3,48 | 1,30 | 3,70 |
| **-57** | 4,65 | 0,00 | 24,14 | 3,61 | 1,20 | 3,70 |
| **-59** | 4,62 | 0,00 | 27,12 | 3,66 | 1,30 | 3,58 |
| **-61** | 4,56 | 0,00 | 25,65 | 3,70 | 2,20 | 3,45 |
| **-63** | 4,53 | 0,00 | 26,01 | 3,81 | 1,30 | 3,34 |
| **-65** | 4,58 | 0,00 | 25,55 | 3,98 | 1,30 | 3,32 |
| **-76** | 4,07 | 0,00 | 26,25 | 3,03 | 1,70 | 3,45 |
| **-78** | 2,57 | 0,00 | 26,38 | 2,53 | 1,00 | 1,97 |
| **-80** | 2,28 | 0,00 | 24,96 | 2,10 | 0,00 | 1,80 |

**Tabla 3.-: ** Distribución de frecuencia de la magnitud para el período completo de muestreo, expresado en porcentaje.**

| Profundi<br>dad | [0,0 -<br>1,5] | [01,5-<br>3,0] | [3,0 -<br>5,0] | [5,0 -<br>10,0] | [10,0 -<br>15,0] | [15,0 -<br>20,0] | [20,0 -<br>25,0] | [25,0 -<br>30,0] | [30,0 -<br>250,0] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **-7** | 0,78 | 2,59 | 3,33 | 9,23 | 6,90 | 7,17 | 8,45 | 9,01 | 52,54 |
| **-9** | 2,46 | 5,27 | 6,19 | 14,95 | 24,53 | 26,26 | 14,25 | 4,77 | 1,31 |
| **-11** | 2,88 | 5,36 | 6,92 | 11,71 | 13,52 | 20,04 | 25,11 | 12,91 | 1,56 |
| **-13** | 2,25 | 5,32 | 9,31 | 28,31 | 31,45 | 18,71 | 4,46 | 0,20 | 0,00 |
| **-15** | 5,57 | 13,85 | 24,28 | 45,24 | 10,19 | 0,81 | 0,05 | 0,00 | 0,00 |
| **-17** | 6,07 | 14,83 | 24,43 | 43,31 | 10,09 | 1,20 | 0,07 | 0,00 | 0,00 |
| **-19** | 6,45 | 15,38 | 25,41 | 42,23 | 9,76 | 0,73 | 0,03 | 0,00 | 0,00 |
| **-21** | 6,65 | 15,35 | 25,54 | 43,37 | 8,56 | 0,50 | 0,02 | 0,00 | 0,00 |
| **-23** | 6,29 | 14,54 | 26,04 | 43,14 | 9,65 | 0,35 | 0,00 | 0,00 | 0,00 |
| **-25** | 6,69 | 16,50 | 23,93 | 42,57 | 9,80 | 0,50 | 0,02 | 0,00 | 0,00 |
| **-27** | 7,83 | 16,36 | 24,88 | 39,73 | 9,96 | 1,16 | 0,07 | 0,00 | 0,00 |
| **-29** | 8,51 | 17,65 | 26,91 | 36,62 | 8,73 | 1,50 | 0,08 | 0,00 | 0,00 |
| **-31** | 9,01 | 20,24 | 27,51 | 33,76 | 7,65 | 1,70 | 0,13 | 0,00 | 0,00 |
| **-33** | 10,06 | 20,66 | 29,60 | 30,35 | 7,35 | 1,95 | 0,03 | 0,00 | 0,00 |
| **-35** | 11,21 | 21,47 | 29,42 | 29,35 | 7,52 | 1,00 | 0,03 | 0,00 | 0,00 |
| **-37** | 11,64 | 23,27 | 29,64 | 27,97 | 6,44 | 1,03 | 0,02 | 0,00 | 0,00 |
| **-39** | 13,65 | 24,26 | 28,37 | 27,47 | 5,49 | 0,75 | 0,00 | 0,00 | 0,00 |
| **-41** | 12,96 | 24,86 | 27,31 | 28,89 | 5,60 | 0,37 | 0,02 | 0,00 | 0,00 |
| **-43** | 11,57 | 23,05 | 27,99 | 30,40 | 6,52 | 0,45 | 0,02 | 0,00 | 0,00 |
| **-45** | 11,79 | 22,67 | 26,97 | 30,92 | 6,95 | 0,68 | 0,02 | 0,00 | 0,00 |
| **-47** | 12,32 | 22,90 | 26,64 | 29,62 | 7,75 | 0,77 | 0,00 | 0,00 | 0,00 |
| **-49** | 12,39 | 23,18 | 27,16 | 29,24 | 6,84 | 1,16 | 0,03 | 0,00 | 0,00 |
| **-51** | 14,32 | 23,37 | 26,23 | 28,29 | 6,24 | 1,51 | 0,05 | 0,00 | 0,00 |
| **-53** | 14,00 | 24,55 | 26,71 | 26,91 | 6,30 | 1,40 | 0,13 | 0,00 | 0,00 |
| **-55** | 13,82 | 25,43 | 26,43 | 25,91 | 6,79 | 1,28 | 0,35 | 0,00 | 0,00 |
| **-57** | 14,67 | 25,64 | 25,43 | 25,49 | 6,69 | 1,61 | 0,47 | 0,00 | 0,00 |
| **-59** | 15,58 | 25,64 | 25,16 | 24,65 | 7,18 | 1,30 | 0,43 | 0,05 | 0,00 |
| **-61** | 18,71 | 26,14 | 22,78 | 23,03 | 6,69 | 2,10 | 0,53 | 0,02 | 0,00 |
| **-63** | 18,71 | 26,14 | 22,78 | 23,03 | 6,69 | 2,10 | 0,53 | 0,02 | 0,00 |
| **-65** | 17,05 | 27,61 | 24,06 | 21,75 | 6,02 | 2,81 | 0,65 | 0,05 | 0,00 |
| **-76** | 14,64 | 27,70 | 30,48 | 23,43 | 2,29 | 1,01 | 0,40 | 0,05 | 0,00 |
| **-78** | 35,76 | 38,83 | 16,62 | 6,35 | 1,61 | 0,58 | 0,23 | 0,02 | 0,00 |
| **-80** | 39,75 | 38,63 | 14,89 | 5,48 | 0,71 | 0,47 | 0,07 | 0,00 | 0,00 |
| **-82** | 39,75 | 38,63 | 14,89 | 5,48 | 0,71 | 0,47 | 0,07 | 0,00 | 0,00 |
| **-84** | 45,35 | 38,47 | 12,35 | 3,41 | 0,43 | 0,00 | 0,00 | 0,00 | 0,00 |
| **-86** | 46,83 | 38,47 | 12,01 | 2,61 | 0,08 | 0,00 | 0,00 | 0,00 | 0,00 |
| **-88** | 47,36 | 39,13 | 11,60 | 1,88 | 0,03 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 4.-: ** Distribución de frecuencia de la dirección para el período completo de muestreo, expresado en porcentaje.**

| Profundi<br>dad | [-22,5 -<br>22,5] | [22,5 -<br>67,5] | [67,5 -<br>112,5] | [112,5 -<br>157,5] | [157,5 -<br>202,5] | [202,5 -<br>247,5] | [247,5 -<br>292,5] | [292,5 -<br>337,5] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Profundi**<br>**dad** | **N ** | **NE** | **E ** | **SE** | **S ** | **SO** | **O ** | **NO** |
| **-7** | 3,69 | 31,30 | 18,68 | 6,32 | 12,57 | 19,09 | 5,55 | 2,79 |
| **-9** | 7,65 | 4,74 | 5,94 | 7,98 | 13,17 | 19,47 | 29,94 | 11,11 |
| **-11** | 2,99 | 8,75 | 15,13 | 2,21 | 4,51 | 22,48 | 41,49 | 2,43 |
| **-13** | 6,02 | 13,42 | 6,24 | 1,20 | 5,52 | 28,65 | 31,96 | 6,98 |
| **-15** | 12,64 | 5,99 | 3,48 | 2,79 | 11,86 | 16,60 | 23,62 | 23,03 |
| **-17** | 15,03 | 5,11 | 2,76 | 2,44 | 12,66 | 17,81 | 23,15 | 21,04 |
| **-19** | 14,50 | 5,44 | 2,64 | 2,61 | 14,65 | 17,81 | 21,20 | 21,14 |
| **-21** | 14,07 | 5,40 | 2,43 | 3,19 | 16,10 | 17,38 | 21,10 | 20,32 |
| **-23** | 14,67 | 5,32 | 2,88 | 3,63 | 18,61 | 18,21 | 17,94 | 18,74 |
| **-25** | 15,37 | 5,24 | 2,39 | 3,58 | 21,80 | 18,39 | 15,95 | 17,28 |
| **-27** | 14,25 | 5,22 | 2,83 | 3,11 | 24,56 | 20,46 | 13,79 | 15,78 |
| **-29** | 14,83 | 5,01 | 2,86 | 3,39 | 27,71 | 20,19 | 12,37 | 13,64 |
| **-31** | 14,77 | 5,60 | 2,93 | 3,74 | 28,14 | 20,52 | 11,91 | 12,39 |
| **-33** | 14,39 | 5,95 | 3,54 | 3,76 | 27,64 | 20,29 | 11,62 | 12,81 |
| **-35** | 15,53 | 6,05 | 4,06 | 3,89 | 27,36 | 18,31 | 12,22 | 12,57 |
| **-37** | 15,90 | 6,37 | 4,06 | 3,94 | 25,74 | 18,96 | 12,11 | 12,92 |
| **-39** | 16,16 | 6,27 | 4,51 | 4,54 | 25,15 | 17,96 | 11,41 | 14,00 |
| **-41** | 18,94 | 5,39 | 4,54 | 4,62 | 24,51 | 16,02 | 11,62 | 14,35 |
| **-43** | 21,24 | 5,40 | 4,22 | 5,11 | 24,61 | 14,73 | 10,36 | 14,32 |
| **-45** | 23,42 | 5,65 | 3,51 | 5,44 | 26,64 | 13,04 | 9,96 | 12,34 |
| **-47** | 23,57 | 4,79 | 3,53 | 5,55 | 28,06 | 12,16 | 9,31 | 13,04 |
| **-49** | 24,28 | 4,96 | 3,63 | 6,62 | 28,02 | 11,72 | 7,95 | 12,82 |
| **-51** | 24,21 | 5,47 | 4,22 | 7,22 | 27,77 | 10,38 | 7,77 | 12,96 |
| **-53** | 24,83 | 5,50 | 4,27 | 7,18 | 29,07 | 9,48 | 7,32 | 12,34 |
| **-55** | 24,90 | 5,72 | 3,44 | 6,64 | 29,42 | 10,33 | 6,93 | 12,62 |
| **-57** | 25,91 | 5,22 | 3,61 | 6,09 | 28,52 | 10,11 | 7,27 | 13,27 |
| **-59** | 26,18 | 4,47 | 3,16 | 5,82 | 27,22 | 10,78 | 7,77 | 14,60 |
| **-61** | 25,30 | 5,01 | 3,34 | 4,94 | 27,14 | 10,54 | 8,66 | 15,07 |
| **-63** | 24,38 | 5,69 | 3,74 | 5,21 | 26,64 | 9,86 | 9,06 | 15,42 |
| **-65** | 22,98 | 5,77 | 3,84 | 4,79 | 26,34 | 11,72 | 9,71 | 14,83 |
| **-76** | 8,36 | 8,33 | 14,57 | 13,43 | 24,88 | 14,02 | 10,17 | 6,25 |
| **-78** | 14,59 | 7,56 | 7,79 | 7,53 | 21,97 | 15,79 | 15,45 | 9,32 |
| **-80** | 15,07 | 7,68 | 8,77 | 8,74 | 19,52 | 15,29 | 14,96 | 9,97 |
| **-82** | 15,64 | 7,31 | 9,65 | 8,06 | 19,04 | 15,10 | 15,27 | 9,92 |
| **-84** | 16,35 | 8,06 | 9,39 | 8,26 | 16,98 | 14,31 | 15,57 | 11,08 |
| **-86** | 18,58 | 8,01 | 10,50 | 7,63 | 15,34 | 13,38 | 16,20 | 10,37 |
