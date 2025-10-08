---
title: Sin título
author: Desconocido
date: D:20221108194425-03'00'
language: es
type: report
pages: 27
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Apéndice C Caracterización de Campos Electromagnéticos
-->

# Apéndice C Caracterización de Campos Electromagnéticos

#### Fecha: Noviembre, 2022

Declaración de Impacto Ambiental - Proyecto Fractura Hidráulica Pozo Exploratorio Picuyo ZG-A
Tabla

Capítulo 7: Ficha Resumen

|0|08/11/2022|Sergio Arriaza|Paulina Medina|Nicole González|
|---|---|---|---|---|
|0|08/11/2022|Ingeniero Eléctrico|Coord. Proyectos|Jefa Proyectos|
|**Revisión**|**Fecha**|**Elaboró**|**Revisó**|**Aprobó**|

Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C Caracterización de Campos Electromagnéticos

## Tabla de Contenido

1. INTRODUCCIÓN ............................................................................................................... 1

2. OBJETIVOS ....................................................................................................................... 2

3. METODOLOGÍA ................................................................................................................ 2

3.1. Aspectos Generales.................................................................................................. 2

3.2. Cálculo del campo eléctrico ..................................................................................... 2

4. NORMATIVA APLICABLE .................................................................................................. 3

5. MEDICIONES .................................................................................................................... 4

5.1. Mediciones puntuales .............................................................................................. 5

5.2. Verificación de los puntos registrados en el trazado .............................................. 6

6. MODELACIÓN .................................................................................................................. 8

6.1. Características de las instalaciones del Proyecto .................................................... 8

7. RESULTADOS DE LA MODELACIÓN ................................................................................ 12

7.1. Línea aérea ............................................................................................................. 12

7.2. Línea subterránea .................................................................................................. 14

8. CONCLUSIONES .............................................................................................................. 16

9. REGISTRO FOTOGRÁFICO .............................................................................................. 17

10. REFERENCIAS ................................................................................................................. 22

Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C Caracterización de Campos Electromagnéticos

## Figuras

Figura 1. Ubicación y Accesos al Área de Emplazamiento del Proyecto ..................................... 1

Figura 2. Esquema Referencial de las mediciones realizadas ..................................................... 4

Figura 3. Estructura de paso línea de media tensión en 23 [kV] (típico) .................................... 8

Figura 4. Zanja típica conductores de media tensión 23 [kV] (típico) ....................................... 10

Figura 5. Perfil de campo eléctrico Línea de evacuación .......................................................... 12

Figura 6. Perfil de campo magnético línea de evacuación ........................................................ 13

Figura 7. Perfil de campo magnético línea de evacuación ........................................................ 14

Figura 8. Registro fotográfico .................................................................................................... 17

Figura 9. Registro fotográfico .................................................................................................... 18

Figura 10. Registro fotográfico .................................................................................................. 19

Figura 11. Registro fotográfico .................................................................................................. 20

Figura 12. Registro fotográfico .................................................................................................. 21

## Tablas

Tabla 1. Descripción de las variables de entrada al software ..................................................... 3

Tabla 2. Mediciones puntuales de campo N°1 (en rojo valores máximos registrados) .............. 5

Tabla 3. Verificación de los valores más desfavorables para cada medición ............................. 7

Tabla 4. Ubicación espacial de los conductores de fase ............................................................. 9

Tabla 5. Parámetros eléctricos de la línea de 23 kV del Proyecto (9 MVA) ................................ 9

Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C Caracterización de Campos Electromagnéticos

Tabla 6. Ubicación espacial de los conductores de fase ........................................................... 11

Tabla 7. Parámetros eléctricos de la línea de 23 kV del Proyecto (9 MVA) .............................. 11

Tabla 8. Valores máximos y en franja de campo eléctrico línea de evacuación PMGD ............ 13

Tabla 9. Valores máximos y en franja de campo magnético línea de evacuación PMGD ........ 14

Tabla 10. Valores máximos y en franja de campo magnético línea de evacuación PMGD ...... 15

Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C Caracterización de Campos Electromagnéticos

### 1. INTRODUCCIÓN

El proyecto PMGD Eólico Oxypora consiste en la construcción y operación de dos (2)

aerogeneradores para la generación de electricidad localizados en la comuna de Ancud,

provincia de Chiloé, región de Los Lagos.

Cada uno de los aerogeneradores tiene una potencia de hasta 4,5MW interconectados por una

línea eléctrica de media tensión (23 KV) que une a los aerogeneradores y que se conectará con

la línea de distribución local en el punto de conexión N° S893326 correspondiente al

alimentador de Quemchi.

El Proyecto se ubica en la Comuna de Ancud, Provincia de Chiloé, Región de Los Lagos,

específicamente en el Sector El Degañ. En la Figura 1 se detalla la ubicación y los accesos al

Proyecto.

**Figura 1. Ubicación y Accesos al Área de Emplazamiento del Proyecto**

Fuente: Elaboración propia, 2022.

Página 1 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

### 2. OBJETIVOS

Los objetivos del presente informe son los siguientes:

 - Realizar mediciones puntuales de campo eléctrico y magnético en la vecindad del

punto de conexión del proyecto PMGD Eólico Oxypora, ubicados en la Ruta W-35,

comuna de Ancud.

 - Realizar los cálculos para determinar el perfil de campo eléctrico y campo magnético

provocados por las líneas de media tensión aéreas y soterradas del proyecto eólico.

### 3. METODOLOGÍA 3.1. Aspectos Generales

Se realizarán simulaciones, utilizando la implementación computacional del método de las

imágenes para determinar los campos eléctricos y magnéticos, a un metro del suelo.

Los valores de campo eléctrico y magnéticos obtenidos mediante simulación computacional

serán comparados con los límites de exposición humana admisibles para un entorno

ocupacional y de público general.

Para del cálculo del campo eléctrico y magnético, se utilizará el método de las imágenes, el

cual fue implementado en el lenguaje de programación GNU Octave 4.4.0.

### 3.2. Cálculo del campo eléctrico

El método de las imágenes permite resolver problemas electromagnéticos en campos

considerados estáticos o cuasi-estacionarios. Para fines prácticos, el campo eléctrico de 50 [Hz]

se comporta como un campo cuasi-estacionario en las inmediaciones de las fuentes que lo

producen.

Los datos de entrada para la función que determina el campo eléctrico son los siguientes:

Página 2 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Tabla 1. Descripción de las variables de entrada al software**

|Variable|Unidad|Descripción|
|---|---|---|
|**POS**|[m]|Matriz de Nx2, donde N es el número de conductores y cada fila<br>representa la ubicación espacial x,y de cada fase.|
|**V **|[V]|Matriz de Nx1 donde N es el número de conductores, matriz de<br>tensiones eficaces instantáneas en cada conductor.|
|**r **|[m]|Radio del conductor de fase utilizado.|
|**N **||Número de conductores por fase.|
|**e_0**|[C2/Nm2]|Constante dieléctrica.|
|**X **|[m]|Vector que contiene las abscisas de los puntos donde se calculará<br>el campo.|
|**Y **|[m]|Vector que contiene las ordenadas de los puntos donde se<br>calculará el campo.|

Los datos de salida son tres matrices de dimensiones X-Y, que contienen los resultados de los

campos vectoriales en X e Y, y la resultante de ambas componentes.

Como los campos electromagnéticos corresponden a un campo vectorial complejo, este puede

estar polarizado circular ó elípticamente, en este informe se determina el valor eficaz máximo

de campo eléctrico a un metro sobre el nivel del suelo

### 4. NORMATIVA APLICABLE

En nuestro país los valores límites permitidos de exposición de las personas a los campos

electromagnéticos de frecuencia industrial provocados por líneas y subestaciones eléctricas,

está definido por el punto 4.7 del RPTD N°07 (Pliego Técnico Normativo), Franja y distancia de

seguridad, y por el punto 5.1.9 del RPTD N°10 (Pliego Técnico Normativo), Centrales de

producción.

La recomendación de uso más frecuente para público general y exposición permanente es la

publicada por la ICNIRP ( _International Commission On Non-Ionizing Radiation Protection_ ), que

establece 5.000 [V/m] para el campo eléctrico y 200 [μT] para la inducción magnética.

Sin embargo, la normativa nacional vigente es más estricta respecto del campo magnético y

limita su exposición a 100 [μT]. Cabe notar que 0.1 [μT] equivale a 1 [mG], por lo tanto este

limite expresado en miliGauss [mG] corresponde a 1000 [mG].

Página 3 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

A continuación, se destacan los párrafos de la normativa nacional, aplicable al proyecto, donde

se indican los límites máximos de exposición:

Punto 4.7 RPTD N°07:

_Los límites máximos permisibles para la seguridad de las personas, en cuanto a la emisión de campo electromagnético para el_

_diseño de líneas aéreas de corriente alterna de 50 Hz de frecuencia, y que será evaluado en el exterior de la franja de seguridad,_

_a 1 metro sobre el nivel del suelo, en condiciones normales de operación de la línea, con los conductores en reposo, serán los_

_que determinen las normas respectivas. En ausencia de regulación técnica nacional, se debe cumplir con lo siguiente:_

_5 kV/m para campo eléctrico (valor RMS)_

_100 μT para campo magnético (valor RMS) (1000 mG)_

Punto 5.1.9 RPTD N°10:

_Los límites máximos permisibles para la seguridad de las personas, en cuanto a la emisión de campo electromagnético para el_

_diseño de líneas aéreas de corriente alterna de 50 Hz de frecuencia, y que será evaluado en el exterior de la franja de seguridad,_

_a 1 metro sobre el nivel del suelo, en condiciones normales de operación de la línea, con los conductores en reposo, serán los_

_que determinen las normas respectivas. En ausencia de regulación técnica nacional, se debe cumplir con lo siguiente:_

_5 kV/m para campo eléctrico (valor RMS)_

_100 μT para campo magnético (valor RMS) (1000 mG)_

### 5. MEDICIONES

Las mediciones fueron realizadas el día 21 de Agosto de 2022, entre las 15:00 y las 17:00 Hrs

aproximadamente, por el Ingeniero Civil Sr. Sergio Arriaza Sánchez.

Al momento de la medición el cielo estaba totalmente despejado, y el suelo seco, con vestigios

de precipitaciones recientes.

Se utilizó el equipo Holaday HI-3604, N° de Serie 75921.

Las mediciones de campo magnético se presentan y verifican en la unidad original del equipo

de medida que corresponde as miliGauss [mG]. En el acápite 7 se indican las características

principales del equipo de medición.

**Figura 2. Esquema Referencial de las mediciones realizadas**

Página 4 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

Fuente: Elaboración propia, 2022.

### 5.1. Mediciones puntuales

**Tabla 2. Mediciones puntuales de campo N°1 (en rojo valores máximos registrados)**

|N°<br>Medida|Coordenadas UTM WGS84<br>Huso 18 Sur|Col3|Campo<br>Eléctrico<br>[V/m]|Campo<br>magnético<br>[mG]|Observaciones|
|---|---|---|---|---|---|
|**N°**<br>**Medida**|**Este**|**Norte**|**Norte**|**Norte**|**Norte**|
|1|609.975|5.332.159|167,5|0,161|Cercano a poste 893342|
|2|609.895|5.332.191|162,1|2,21|Frontis casa|
|3|609.818|5.332.230|172,9|0,155|Cercano a poste 893339|
|4|609.671|5.332.287|313|0,573|Cercano a poste 893338|
|5|609.629|5.332.301|268|0,235|Cercano a poste 893337|
|6|609.559|5.332.334|127,9|0,868|Cercano a poste 893336|
|7|609.458|5.332.371|444|0,871|Cercano a poste 893335|

Página 5 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

|N°<br>Medida|Coordenadas UTM WGS84<br>Huso 18 Sur|Col3|Campo<br>Eléctrico<br>[V/m]|Campo<br>magnético<br>[mG]|Observaciones|
|---|---|---|---|---|---|
|**N°**<br>**Medida**|**Este**|**Norte**|**Norte**|**Norte**|**Norte**|
|8|609.344|5.332.422|**451 **|0,733|Cercano a poste 893334|
|9|609.207|5.332.478|192,8|0,68|Cercano a poste 893333|
|10|609.130|5.332.506|222|2,02|Cercano a poste 893331|
|11|609.028|5.332.550|242|4,56|Cercano a poste 893330|
|12|608.977|5.332.569|383|**4,6 **||
|13|608.928|5.332.587|144,3|3,46|Cercano a poste 893329|
|14|608.886|5.332.609|303|2,12|Cercano a poste 893328|
|15|608.837|5.332.628|226|0,769|Cercano a poste 893327|
|16|608.783|5.332.651|25,8|0,533||
|17|608.727|5.332.676|7,93|0,302||
|18|608.673|5.332.696|1,25|0,208||
|19|608.602|5.332.725|1,13|0,155||
|20|608.561|5.332.735|1,37|0,136||
|21|608.450|5.332.752|2,94|0,132||
|22|608.412|5.332.753|8,53|0,132||
|23|608.344|5.332.754|1,12|0,131||
|24|608.265|5.332.760|1,05|0,148||
|25|608.203|5.332.762|2,23|0,16||
|26|608.146|5.332.763|3,08|0,185||
|27|608.081|5.332.766|8,49|0,234||
|28|607.995|5.332.767|30,7|0,535||
|29|607.943|5.332.768|109,8|0,779||
|30|607.862|5.332.783|226|0,527||

Fuente: Elaboración propia, 2022.

### 5.2. Verificación de los puntos registrados en el trazado

A continuación, se presentan los peores valores de las medidas de campo eléctrico y magnético

obtenidas en el entorno del proyecto “PMGD Eólico Oxypora”, las cuales fueron marcadas en

rojo en la Tabla 2 y se comparan con los límites establecidos para la normativa indica en el

punto 4.1.

Página 6 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Tabla 3. Verificación de los valores más desfavorables para cada medición**

|Medida|Campo<br>Eléctrico<br>[V/m]|Límite<br>RPTD<br>[V/m]|Cumple<br>(Si/No)|Campo<br>magnético<br>[mG]|Límite<br>RPTD<br>[mG]|Cumple<br>(Si/No)|
|---|---|---|---|---|---|---|
|Puntual N°1|451|5.000|Si|4,6|1000|Si|

Fuente: Elaboración propia, 2022.

Por lo tanto, los valores medidos en terreno están bajo los límites establecidos por la normativa

nacional.

Página 7 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

### 6. MODELACIÓN 6.1. Características de las instalaciones del Proyecto

**Línea aérea en media tensión**

Se modelará la ubicación horizontal de los conductores (coordenada X), a partir de los datos

de las estructuras típicas de líneas de media tensión en disposición horizontal,

correspondientes a estructuras de suspensión y anclaje, en postes de hormigón de 11,5 [m].

**Figura 3. Estructura de paso línea de media tensión en 23 [kV] (típico)**

Fuente: Elaboración propia, 2022.

A fin de determinar la altura de los conductores al suelo, como criterio conservador se

establecerá en la mínima admisible, para zonas no transitables, de acuerdo con el según

Artículo 6.3 del reglamento RPTD N°07.

En este caso, para líneas de 23 kV, se establece una distancia mínima al suelo de 6 metros,

para regiones no transitables.

Las coordenadas cartesianas de ubicación relativa de cada fase en el espacio y los parámetros

eléctricos utilizados para la modelación de la estructura de anclaje, se presentan en la Tabla 4

y Tabla 5 respectivamente.

Página 8 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Tabla 4. Ubicación espacial de los conductores de fase**

|Estructura de anclaje|Ubicación espacial de los conductores|Col3|
|---|---|---|
|**Fases**|**X [m]**|**Y [m]**|
|A|-1,1|6,00|
|B|0,|6,00|
|C|1,1|6,00|

Fuente: Elaboración Propia, 2022.

**Tabla 5. Parámetros eléctricos de la línea de 23 kV del Proyecto (9 MVA)**

|Parámetro|Valor|Unidad|
|---|---|---|
|Potencia Nominal|9|MVA|
|Tensión Nominal|23|kV|
|Corriente Nominal|226|A|
|Conductores por fase|1|-|
|Nombre comercial del conductor|Al. 120 mm2 (Alliance)|-|
|Diámetro del conductor|14,31|mm|
|Separación entre subconductores|N/A|mm|

Fuente: Elaboración Propia, 2022.

**Conductor soterrado**

Se considera una zanja típica. Se modelará la ubicación horizontal de los conductores
(coordenada X), separados 20 [cm] entre sí, y a una profundidad de 1 [m] bajo el nivel del
suelo, tal como se presenta en la Figura 4.

Página 9 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Figura 4. Zanja típica conductores de media tensión 23 [kV] (típico)**

Fuente: Elaboración propia, 2022.

Las coordenadas cartesianas de ubicación relativa de cada fase en el espacio y los parámetros

eléctricos utilizados para la modelación de los conductores se presentan en la Tabla 6 y Tabla

7.

Página 10 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Tabla 6. Ubicación espacial de los conductores de fase**

|Estructura de anclaje|Ubicación espacial de los conductores|Col3|
|---|---|---|
|**Fases**|**X [m]**|**Y [m]**|
|A|-0,2|-1|
|B|0,|-1|
|C|0,2|-1|

Fuente: Elaboración Propia, 2022.

**Tabla 7. Parámetros eléctricos de la línea de 23 kV del Proyecto (9 MVA)**

|Parámetro|Valor|Unidad|
|---|---|---|
|Potencia Nominal|9|MVA|
|Tensión Nominal|23|kV|
|Corriente Nominal|226|A|
|Conductores por fase|1|-|
|Nombre comercial del conductor|XLPE Cu 240 mm2|-|
|Diámetro del conductor|25,2|mm|
|Separación entre subconductores|N/A|mm|

Fuente: Elaboración Propia, 2022.

Página 11 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

### 7. RESULTADOS DE LA MODELACIÓN

A continuación, se presentan los resultados de la simulación de las emisiones de campo

electromagnético provocadas por las instalaciones presentes y proyectadas, junto con su

eventual interacción.

Se contrastan los valores obtenidos, contra los máximos admisibles del Pliego Técnico RPTD

N°07 de la Superintendencia de Electricidad y Combustibles.

### 7.1. Línea aérea

En este punto, se presentan los resultados de simulación respecto a la relación con la Línea de

evacuación del PMGD de 9 MW:

**Figura 5. Perfil de campo eléctrico Línea de evacuación**

|Perfil de campo electrico<br>Linea de media tensión 23 kV<br>0.50<br>[kV/m]<br>0.40<br>eléctrico<br>0.30<br>campo<br>0.20|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0.20<br>0.30<br>0.40<br>0.50<br> campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>Linea de media tensión 23 kV||||||||||||
|0.20<br>0.30<br>0.40<br>0.50<br> campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>Linea de media tensión 23 kV|||||0.40|||||||
|0.20<br>0.30<br>0.40<br>0.50<br> campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>Linea de media tensión 23 kV||||||||||||
|0.20<br>0.30<br>0.40<br>0.50<br> campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>Linea de media tensión 23 kV|||||0.30|||||||
|0.20<br>0.30<br>0.40<br>0.50<br> campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>Linea de media tensión 23 kV||||||||||||
|0.20<br>0.30<br>0.40<br>0.50<br> campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>Linea de media tensión 23 kV|||||0.20|||||||
|0.20<br>0.30<br>0.40<br>0.50<br> campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>Linea de media tensión 23 kV||||||||||||
|Intensidad de||||||||||||
|Intensidad de|||||0.10|||||||
|Intensidad de||||||||||||
|Intensidad de||||||||||||
|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.00~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|

Fuente: Elaboración propia, 2022.

Página 12 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Tabla 8. Valores máximos y en franja de campo eléctrico línea de evacuación PMGD**

|Punto de medida|x [m]|y[m]|Campo<br>Eléctrico<br>[kV/m]|Límite<br>[kV/m]|% Valor<br>límite|
|---|---|---|---|---|---|
|**Limite franja seguridad derecha**|4,00|1|0,167|5|3,3 %|
|**Limite franja seguridad izquierda**|-4,00|1|0,167|5|3,3 %|
|**Valor máximo en perfil**|3,50|1|0,171|5|3,4 %|

Fuente: Elaboración propia, 2022.

A 4 [m] del eje de la línea, los valores de campo eléctrico son del orden del 3,3% del máximo

tolerable por la normativa nacional. El valor máximo de 0,17 [kV] se registra a 3,5 [m] del eje

de la línea eléctrica.

**Figura 6. Perfil de campo magnético línea de evacuación**

|Perfil de campo magnético<br>Linea de media tensión 23 kV<br>8.0<br>[μT]<br>6.0<br>magnético<br>4.0<br>o|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|4.0<br>6.0<br>8.0<br>o magnético [μT]<br>**Perfil de campo magnético**<br>Linea de media tensión 23 kV|||||||||||
|4.0<br>6.0<br>8.0<br>o magnético [μT]<br>**Perfil de campo magnético**<br>Linea de media tensión 23 kV|||||6.0||||||
|4.0<br>6.0<br>8.0<br>o magnético [μT]<br>**Perfil de campo magnético**<br>Linea de media tensión 23 kV|||||||||||
|4.0<br>6.0<br>8.0<br>o magnético [μT]<br>**Perfil de campo magnético**<br>Linea de media tensión 23 kV|||||4.0||||||
|4.0<br>6.0<br>8.0<br>o magnético [μT]<br>**Perfil de campo magnético**<br>Linea de media tensión 23 kV|||||||||||
|Camp|||||||||||
|Camp|||||2.0||||||
|Camp|||||||||||
|Camp|||||||||||
|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|

Fuente: Elaboración propia, 2022.

Página 13 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Tabla 9. Valores máximos y en franja de campo magnético línea de evacuación PMGD**

|Punto de medida|x [m]|y[m|Campo<br>]<br>Magnético [μT]|Límite<br>[μT]|% Valor<br>límite|
|---|---|---|---|---|---|
|**Limite franja seguridad derecha**|4,00|1|2,10|100|2,1 %|
|**Limite franja seguridad izquierda**|-4,00|1|2,10|100|2,1 %|
|**Valor máximo en perfil**|0,00|1|3,31|100|3,3 %|

Fuente: Elaboración propia, 2022.

A 4 [m] del eje de la línea, los valores de campo magnético son del orden del 2,1% del máximo

tolerable por la normativa nacional. El valor máximo de 3,31 [μT] se registra en el eje de la

línea de evacuación.

### 7.2. Línea subterránea

En este punto, se presentan los resultados de simulación respecto a la relación con la Línea de

evacuación del PMGD en tramo soterrado.

Los conductores enterrados son una fuente nula de campo eléctrico.

**Figura 7. Perfil de campo magnético línea de evacuación**

|Perfil de campo magnético<br>Línea soterrada en 23 kV<br>8.0<br>[μT]<br>6.0<br>agnético<br>4.0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|4.0<br>6.0<br>8.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Línea soterrada en 23 kV||||||||||||
|4.0<br>6.0<br>8.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Línea soterrada en 23 kV|||||6.0|||||||
|4.0<br>6.0<br>8.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Línea soterrada en 23 kV||||||||||||
|4.0<br>6.0<br>8.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Línea soterrada en 23 kV|||||4.0|||||||
|Campo m||||||||||||
|Campo m|||||2.0|||||||
|Campo m||||||||||||
|Campo m||||||||||||
|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|

Fuente: Elaboración propia, 2022.

Página 14 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Tabla 10. Valores máximos y en franja de campo magnético línea de evacuación PMGD**

|Punto de medida|x [m]|y[m]|Campo<br>Magnético<br>[μT]|Límite|% Valor<br>límite|
|---|---|---|---|---|---|
|**Limite franja seguridad derecha**|2,00|1|1,96|100|2 %|
|**Limite franja seguridad izquierda**|-2,00|1|1,96|100|2 %|
|**Valor máximo en perfil**|0,00|1|3,88|100|3,9 %|

Fuente: Elaboración propia, 2022.

A 2 [m] del eje de la línea, los valores de campo magnético son del orden del 2% del máximo

tolerable por la norma 62-814.450 Electric and Magnetic Field Standards, del estado de Florida.

El valor máximo de 3,88 [μT] se registra en el eje de la línea de evacuación.

Página 15 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

### 8. CONCLUSIONES

En el presente informe se utilizó la normativa nacional para determinar los valores máximos

admisibles de campos electromagnéticos en el Proyecto PMGD Eólico Oxypora.

En el acápite 5 se presentan los resultados de las mediciones en terreno efectuadas en zonas

públicas aledañas a las líneas de alta tensión existentes en la zona del Proyecto, y se ha

verificado que los niveles de campos electromagnéticos obtenidos en aquellas mediciones se

encuentran bajo los valores máximos establecidos por la norma de referencia.

En el acápite 7 se presentan los resultados de los cálculos de los campos electromagnéticos

originados por la operación a potencia máxima de las líneas de media tensión del Proyecto, los

que a su vez presentan valores inferiores a los máximos permitidos en la normativa de

referencia.

Considerando los límites máximos de exposición establecidos en la normativa aplicable, Pliego

Técnico Normativo RPTD N°07, Franja y distancia de seguridad, y Pliego Técnico Normativo

RPTD N°10, Centrales, producción y subestaciones, de la Superintendencia de Electricidad y

Combustibles, **el proyecto dará cumplimiento a los límites establecidos** .

Página 16 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

## 9. REGISTRO FOTOGRÁFICO

**Figura 8. Registro fotográfico**

Página 17 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Figura 9. Registro fotográfico**

Página 18 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Figura 10. Registro fotográfico**

Página 19 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Figura 11. Registro fotográfico**

Página 20 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

**Figura 12. Registro fotográfico**

Página 21 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

## 10. REFERENCIAS

 - Comisión Internacional sobre Protección Frente a Radiaciones No Ionizantes. (1998).

Recomendaciones para limitar la exposición a campos eléctricos, magnéticos y

electromagnéticos. International Commission on Non-Ionizing Radiation Protection.

 - Superintendencia de Electricidad y Combustibles (2020). RPTD N°07 - Franja y

distancias eléctricas de seguridad.

 - Superintendencia de Electricidad y Combustibles (2020). RPTD N°10 - Centrales,

producción y subestaciones.

Página 22 de 22 Declaración de Impacto Ambiental - Proyecto PMGD Eólico Oxypora

Anexo 2-1. Medio Físico

Apéndice C. Caracterización de Campos Electromagnéticos

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Descripción de las variables de entrada al software****

| Variable | Unidad | Descripción |
| --- | --- | --- |
| **POS** | [m] | Matriz de Nx2, donde N es el número de conductores y cada fila<br>representa la ubicación espacial x,y de cada fase. |
| **V ** | [V] | Matriz de Nx1 donde N es el número de conductores, matriz de<br>tensiones eficaces instantáneas en cada conductor. |
| **r ** | [m] | Radio del conductor de fase utilizado. |
| **N ** |  | Número de conductores por fase. |
| **e_0** | [C2/Nm2] | Constante dieléctrica. |
| **X ** | [m] | Vector que contiene las abscisas de los puntos donde se calculará<br>el campo. |
| **Y ** | [m] | Vector que contiene las ordenadas de los puntos donde se<br>calculará el campo. |

**Tabla 2.: Mediciones puntuales de campo N°1 (en rojo valores máximos registrados)****

| N°<br>Medida | Coordenadas UTM WGS84<br>Huso 18 Sur | Col3 | Campo<br>Eléctrico<br>[V/m] | Campo<br>magnético<br>[mG] | Observaciones |
| --- | --- | --- | --- | --- | --- |
| **N°**<br>**Medida** | **Este** | **Norte** | **Norte** | **Norte** | **Norte** |
| 1 | 609.975 | 5.332.159 | 167,5 | 0,161 | Cercano a poste 893342 |
| 2 | 609.895 | 5.332.191 | 162,1 | 2,21 | Frontis casa |
| 3 | 609.818 | 5.332.230 | 172,9 | 0,155 | Cercano a poste 893339 |
| 4 | 609.671 | 5.332.287 | 313 | 0,573 | Cercano a poste 893338 |
| 5 | 609.629 | 5.332.301 | 268 | 0,235 | Cercano a poste 893337 |
| 6 | 609.559 | 5.332.334 | 127,9 | 0,868 | Cercano a poste 893336 |
| 7 | 609.458 | 5.332.371 | 444 | 0,871 | Cercano a poste 893335 |

**Tabla 3.: Verificación de los valores más desfavorables para cada medición****

| Medida | Campo<br>Eléctrico<br>[V/m] | Límite<br>RPTD<br>[V/m] | Cumple<br>(Si/No) | Campo<br>magnético<br>[mG] | Límite<br>RPTD<br>[mG] | Cumple<br>(Si/No) |
| --- | --- | --- | --- | --- | --- | --- |
| Puntual N°1 | 451 | 5.000 | Si | 4,6 | 1000 | Si |

**Tabla 4.: Ubicación espacial de los conductores de fase****

| Estructura de anclaje | Ubicación espacial de los conductores | Col3 |
| --- | --- | --- |
| **Fases** | **X [m]** | **Y [m]** |
| A | -1,1 | 6,00 |
| B | 0, | 6,00 |
| C | 1,1 | 6,00 |

**Tabla 5.: Parámetros eléctricos de la línea de 23 kV del Proyecto (9 MVA)****

| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Potencia Nominal | 9 | MVA |
| Tensión Nominal | 23 | kV |
| Corriente Nominal | 226 | A |
| Conductores por fase | 1 | - |
| Nombre comercial del conductor | Al. 120 mm2 (Alliance) | - |
| Diámetro del conductor | 14,31 | mm |
| Separación entre subconductores | N/A | mm |

**Tabla 6.: Ubicación espacial de los conductores de fase****

| Estructura de anclaje | Ubicación espacial de los conductores | Col3 |
| --- | --- | --- |
| **Fases** | **X [m]** | **Y [m]** |
| A | -0,2 | -1 |
| B | 0, | -1 |
| C | 0,2 | -1 |

**Tabla 7.: Parámetros eléctricos de la línea de 23 kV del Proyecto (9 MVA)****

| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Potencia Nominal | 9 | MVA |
| Tensión Nominal | 23 | kV |
| Corriente Nominal | 226 | A |
| Conductores por fase | 1 | - |
| Nombre comercial del conductor | XLPE Cu 240 mm2 | - |
| Diámetro del conductor | 25,2 | mm |
| Separación entre subconductores | N/A | mm |

**Tabla 8.: Valores máximos y en franja de campo eléctrico línea de evacuación PMGD****

| Punto de medida | x [m] | y[m] | Campo<br>Eléctrico<br>[kV/m] | Límite<br>[kV/m] | % Valor<br>límite |
| --- | --- | --- | --- | --- | --- |
| **Limite franja seguridad derecha** | 4,00 | 1 | 0,167 | 5 | 3,3 % |
| **Limite franja seguridad izquierda** | -4,00 | 1 | 0,167 | 5 | 3,3 % |
| **Valor máximo en perfil** | 3,50 | 1 | 0,171 | 5 | 3,4 % |

**Tabla 9.: Valores máximos y en franja de campo magnético línea de evacuación PMGD****

| Punto de medida | x [m] | y[m | Campo<br>]<br>Magnético [μT] | Límite<br>[μT] | % Valor<br>límite |
| --- | --- | --- | --- | --- | --- |
| **Limite franja seguridad derecha** | 4,00 | 1 | 2,10 | 100 | 2,1 % |
| **Limite franja seguridad izquierda** | -4,00 | 1 | 2,10 | 100 | 2,1 % |
| **Valor máximo en perfil** | 0,00 | 1 | 3,31 | 100 | 3,3 % |

**Tabla 10.: Valores máximos y en franja de campo magnético línea de evacuación PMGD****

| Punto de medida | x [m] | y[m] | Campo<br>Magnético<br>[μT] | Límite | % Valor<br>límite |
| --- | --- | --- | --- | --- | --- |
| **Limite franja seguridad derecha** | 2,00 | 1 | 1,96 | 100 | 2 % |
| **Limite franja seguridad izquierda** | -2,00 | 1 | 1,96 | 100 | 2 % |
| **Valor máximo en perfil** | 0,00 | 1 | 3,88 | 100 | 3,9 % |
