---
title: Sin título
author: Aldo Hernández
date: D:20240910102951-03'00'
language: es
type: report
pages: 17
has_toc: True
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1 PRESENTACIÓN
  - 1
  - 2 OBJETIVO
  - 3 MATERIALES Y MÉTODO
  - 2
  - 4 RESULTADOS
  - 5 CONCLUSIONES
  - 6 REFERENCIAS
  - 7 ANEXOS
-->

**ESTUDIO DE CORRENTOMETRÍA**

**EULERIANA**

Respuesta a observaciones ICSASA

Proyecto “Optimización Operacional Planta Lota”, sector

Bahía Lota, Región del Biobío.

**Requirente: Industrias Isla Quihua S.A.**

Concepción, julio de 2023

**EQUIPO DE TRABAJO**

**Aldo Hernández** Jefe de Proyecto

Dinámica costera y
**Daniela Henríquez**

Modelación

Biólogo Marino
Dr. Manejo Recursos

Acuáticos Renovables

Bióloga Marina
MSc. en Oceanografía

_Análisis de corrientes_

_Revisión y edición informe_

_Análisis de corrientes_

_Elaboración de informe_

Holon SpA. 2023. Estudio de Correntometría Euleriana. Proyecto Proyecto “Optimización

Operacional Planta Lota”, sector Bahía Lota, Región del Biobío. Industrias Isla Quihua S.A. 17

pp.

i

**TABLA DE CONTENIDO**

**1** **PRESENTACIÓN .................................................................................................................... 1**

**2** **OBJETIVO .............................................................................................................................. 2**

**3** **MATERIALES Y MÉTODO ..................................................................................................... 2**

3.1 Á REA DE ESTUDIO ......................................................................................................................... 2

3.2 I NFORMACIÓN DE CAMPO ............................................................................................................... 3

3.3 I NFORMACIÓN SECUNDARIA ........................................................................................................... 4

3.4 P ROCESAMIENTO DE DATOS Y ANÁLISIS DE LA INFORMACIÓN ........................................................... 4

**4** **RESULTADOS ........................................................................................................................ 5**

4.1 A NÁLISIS DE MAREAS Y CORRENTOMETRÍA EULERIANA .................................................................... 5

**5** **CONCLUSIONES .................................................................................................................. 11**

**6** **REFERENCIAS ..................................................................................................................... 12**

ii

# 1 PRESENTACIÓN

Se entregan resultados asociados al estudio de correntometría euleriana para el sector donde se

encuentra ubicado el emisario de descarga de Industrias Isla Quihua S.A., en marco del proyecto

“Optimización Operacional Planta Lota”, sector Bahía Lota, Región del Biobío.

La zona de estudio se encuentra enfocada en la bahía Lota, situada en el litoral de la Región del

Biobío, en la zona centro sur de Chile. Esta zona se caracteriza por presentar una alta variabilidad

estacional en las condiciones oceanográficas, asociado con el forzamiento físico. La alternancia

estacional de procesos de surgencia y convergencia genera importantes cambios en la

circulación costera y en particular sobre los procesos de intercambio, exportación, advección y

retención, con importantes implicancias sobre los tiempos de residencia de aguas en el sistema

de bahías y golfos.

Considerando las implicancias de la circulación costera en la dispersión de contaminantes, se

plantea la necesidad de estudiar la variabilidad en la dinámica de corrientes dentro de la bahía, y

su respuesta frente a eventos de forzamiento local (e.g. mareas). La aproximación metodológica

será tomada como dato de entrada a la modelación de la pluma de descarga del emisario de

Industrias Isla Quihua S.A., mediante la aplicación de herramientas numéricas, bajo escenarios

de fase lunar de sicigia y cuadratura en mareas llenante y vaciante.

A continuación, se presenta la metodología y resultados relativos a la dinámica de corrientes para

la zona de estudio, orientado a dar respuesta a las observaciones formuladas por la autoridad

ambiental en el ICSARA I.

# 1

# 2 OBJETIVO

Caracterizar la dinámica de corrientes costera del sector de bahía Lota, en marco del Proyecto

“Optimización Operacional Planta Lota”, sector Bahía Lota, Región del Biobío.

# 3 MATERIALES Y MÉTODO

## 3.1 Área de estudio

El área de estudio del proyecto se ubica en la localidad de Lota, Comuna de Coronel, Región del

Biobío. El emisario realiza su trazado perpendicular a línea de costa hasta una profundidad de

7,5 m referido al nivel medio del mar ( **Figura 1** ).

**Figura 1** . Ubicación referencial del área de estudio. Coordenadas en UTM, Datum WGS84 Huso
18H.

# 2

## 3.2 Información de campo

La información de campo asociada a la dinámica de corrientes costera se obtuvo utilizando un

equipo ADCP marca Linkquest, modelo 600 kh, fondeado en las cercanías del sistema de

descarga de Industrias Isla Quihua S.A, (coordenadas geográficas 37o05’57,21’’S;

73o09’40,03’’W) a una profundidad aproximada de 7,5 metros ( **Figura 2** ). En el Anexo I se entrega

el permiso SHOA que autoriza la instalación del equipo.

El periodo de medición de corrientes cubrió 37 días, iniciando el 25 de enero y finalizando el 02

de marzo del 2022, y a una frecuencia de muestreo de 10 minutos.

**Figura 2.** Ubicación espacial de instalación de ADCP con respecto al emisario de descarga de
efluentes. Coordenadas en UTM. Datum WGS84, Huso 18H.

## 3

## 3.3 Información secundaria

Para evaluar el efecto de las mareas sobre las corrientes costeras dentro del área de estudio, se

obtuvo información adicional de la base de datos desde la plataforma Tabla de Mareas

(https://tablademareas.com/), para Lota (37o04’47’’S, 73o09’58’’W).

El rango medio de la marea en fase lunar de sicigia y cuadratura se obtuvo a partir de lo indicado

en las Instrucciones Oceanográficas No2 “Método oficial para el cálculo de los valores no

armónicos de la marea” del SHOA (SHOA, 1999).

Para este estudio se consideraron los días donde se observó condiciones de sicigia (luna nueva

y luna llena) y cuadratura (cuarto menguante y cuarto creciente) ( **Tabla 1** ). La altura de marea

utilizada para la modelación en cada uno de los escenarios corresponde a la altura promedio de

mareas registradas en cada fase lunar.

**Tabla 1.** Registro de mareas en fase lunar de sicigia y cuadratura registradas para el periodo de
muestreo. Elaboración propia.

**Fase lunar** **Fecha**

Luna nueva 01/02 y 02/03
Sicigia
Luna llena 16/02

23/02
Cuadratura [Cuarto menguante ]
Cuarto creciente 25/01 y 08/02

## 3.4 Procesamiento de datos y análisis de la información

Para el análisis de la información, la dirección de las corrientes fue referida al norte geográfico.

El análisis estadístico involucró la construcción del componente armónico de mareas y su

contraste con la serie de datos de corrientes registrada por el ADCP.

Con la finalidad de determinar las frecuencias temporales que dominaron en la variabilidad de las

series de tiempo de la magnitud de las corrientes medidas, se realizó un análisis espectral, el cual

permite identificar la correlación de las funciones seno y coseno de diferentes frecuencias

observadas en las series de datos.

Para visualizar gráficamente el comportamiento integrado de la velocidad y dirección de las

corrientes, se construyeron series de tiempo y diagramas de espiral de Ekman, los cuales

4

permiten visualizar la dirección predominante y la variabilidad en la frecuencia de las diferentes

magnitudes registradas a lo largo de la columna de agua.

A partir de la evaluación integrada de los resultados del análisis estadístico, se determinaron

escenarios contrastantes que representan la mayor variabilidad del cuerpo de agua, los cuales

fueron utilizados como datos de entrada para la modelación de la pluma de descarga.

# 4 RESULTADOS

## 4.1 Análisis de mareas y correntometría euleriana

El análisis de la serie de tiempo de mareas ( **Figura 3** ) determinó la presencia de un régimen de

marea semidiurna mixta, con amplitudes que variaron entre 2 m y 0,1 m, para pleamar y bajamar

respectivamente.

**Figura** **3.** Serie temporal de mareas durante el periodo de estudio. Lota
[(https://tablademareas.com/). Los segmentos destacados en celeste y naranja indican fase lunar](https://tablademareas.com/)
de cuadratura y sicigia, respectivamente. Elaboración propia.

El análisis espectral de las series temporales de corrientes por estrato ( **Figura 4** ) revela que la

mayor densidad espectral registra una oscilación periódica cada 12 y 24 horas, indicando que la

variabilidad de las corrientes a lo largo de la columna de agua se encuentra modulada por

procesos semidiurnos y mareales. Este patrón fue más notorio en las capas medias (estratos

entre 5,5 a 7,5 m) y profundas (9,5 m)

5

**Figura 4.** Análisis espectral para series temporales de marea por estrato. Elaboración propia.

6

El resultado del análisis de las series temporales para las velocidades de corrientes ( **Figura 5** )

revela una alta variabilidad entre las distintas capas de la columna de agua. Las velocidades

superficiales (estratos 1,5 y 3,5 m) registraron magnitudes promedio que oscilaron entre 11,4 y

14,4 cm/s, con máximos superiores a 50 cm/s. Las velocidades subsuperficiales y de fondo

(estratos 5,5 a 9,5 m) mostraron corrientes menos intensas que en superficie, con magnitudes

promedio que oscilaron entre 5,6 y 6,6 cm/s y máximos superiores a 20 cm/s. Cabe destacar que,

los peaks de máxima variabilidad se registran durante la tercera semana de febrero, lo cual

coincide con mareas de cuadratura.

El análisis de espiral de Ekman revela un comportamiento similar en la dirección de las corrientes,

registrando corrientes con mayor intensidad en superficie, mostrando una orientación hacia el E

NE (primeros 4 m de profundidad) para la mayoría de los escenarios, excepto durante el

escenario de vaciante en fase de sicigia, donde las corrientes a lo largo de toda la columna de

agua son de baja intensidad (<5 cm/s). Cabe destacar que, para los estratos más profundos de

la columna de agua, no se registró cambios notables en la dirección de las corrientes.

7

**Figura 5.** Series temporales de velocidad y dirección de corrientes durante el periodo de estudio
por estrato de profundidad. En celeste se destacan los periodos de cuadratura y en naranjo los
periodos de sicigia. Elaboración propia.

8

**Figura 6.** Espiral de Ekman de corrientes durante escenarios de llenante y vaciante, en fase lunar
de sicigia y cuadratura. Elaboración propia.

Con base en estos resultados, y considerando que en todos los niveles de la columna de agua

se detectó una fuerte influencia de las mareas, se han incorporado 3 escenarios de entrada a la

modelación, considerando 3 estratos de profundidad promedio (superficie, medio y fondo), en

escenarios de sicigia y cuadratura para mareas vaciante y llenante ( **Tabla 2** ).

9

A partir de la observación de estos escenarios, es posible detectar para la capa superficial,

mayores velocidades en el escenario de marea llenante (6,3 a 10,0 cm/s), mientras que las capas

medias y de fondo, las corrientes presentan una menor magnitud, oscilando entre 0,15 (llenante)

y 3,7 cm/s (vaciante).

En cuanto a la dirección de las corrientes, se observa una alta variabilidad a lo largo de toda la

columna de agua, destacando cambios notorios tanto en fase lunar de sicigia como cuadratura.

En condición de sicigia, para la capa superficial (1,5 metros) se registran un cambio de orientación

de NE en llenante (40,6o) a SW en vaciante (138,8o), mientras que para la capa media (5,5 metros)

la dirección de las corrientes cambia de sentido E en llenante (95,9o) a SW en vaciante (227,6o)

y para la capa de fondo (7,5 metros) se observan un cambio de sentido S en llenante (181,1o) a

N en vaciante (358,9o).

En condición de cuadratura, para la capa superficial (1,5 metros) se registran un cambio de

orientación de SE en llenante (125,7o) a N en vaciante (8,4o), mientras que para la capa media

(5,5 metros) las dirección de las corrientes cambia de sentido E en llenante (86,4o) a NW en

vaciante (303,1o) y para la capa de fondo (7,5 metros) se observan un cambio de sentido N en

llenante (9,9o) a NW en vaciante (319,2o).

**Tabla 2.** Escenarios de modelación propuestos para la dinámica de corrientes en la zona de
estudio. Elaboración propia.

**Cuadratura** **Sicigia**

**Estrato** **Variable** **Unidad Llenante Vaciante Llenante Vaciante**

Superficie Dirección grados-N 125,7 8,4 40,6 138,8

1.5 m Velocidad cm/s 10,0 3,4 6,3 2,4

Medio Dirección grados-N 86,4 303,1 95,9 227,6

5.5 m Velocidad cm/s 2,16 2,38 0,61 0,75

Fondo Dirección grados-N 9,87 319,15 181,13 358,90

7.5 m Velocidad cm/s 1,03 3,69 0,15 1,80

10

# 5 CONCLUSIONES

El análisis de la información de campo reveló que en la zona de estudio la dinámica de corrientes

posee una fuerte influencia de las mareas en fase lunar de sicigia y cuadratura, observándose en

las capas superficiales velocidades normalmente inferiores a 15 cm s-1, con máximos superiores

a 50 cm/s y velocidades medias y de fondo de menor magnitud (en torno a 6 cm/s).

Se registraron cambios notables en la dirección de las corrientes en toda la columna de agua,

tanto en fase lunar de sicigia como cuadratura, los que fueron más notorios en el escenario de

sicigia.

En condición de sicigia, las tres capas analizadas (superficie, medio y fondo) presentaron cambios

de orientación de las corrientes en llenante y vaciante, con tendencias de NE a SW (capa

superficial), E a SW (capa media), y de S a N (capa de fondo).

En condición de cuadratura, los cambios más notorios fueron observados en la capa superficial,

con tendencias de SE en llenante a N en vaciante.

**Dr. Aldo Hernández Rodríguez**

Representante Legal

HOLON SpA.

11

# 6 REFERENCIAS

**SHOA. 1999.** Instrucciones Oceanográficas No2. Método oficial para el cálculo de los valores no
armónicos de las mareas. 2da. Edición. Armada de Chile. 26pp.

12

# 7 ANEXOS

13

## 7.1 Anexo I: Permiso SHOA 711 instalación ADCP

14