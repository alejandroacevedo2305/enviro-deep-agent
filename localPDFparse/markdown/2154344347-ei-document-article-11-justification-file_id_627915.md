---
title: Sin título
author: Julio Moraga
date: D:20211207121839-03'00'
language: es
type: manual
pages: 9
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO C2-20
-->

# ANEXO C2-20

## ESTUDIO DE HIDROLOGÍA DE CRECIDAS

**ÍNDICE**

**1.** **ASPECTOS GENERALES ............................................................................................................ 1**

**2.** **ANÁLISIS DE PRECIPITACIONES ........................................................................................... 2**

**3.** **TIEMPO DE CONCENTRACIÓN .............................................................................................. 4**

**4.** **CAUDALES DE CRECIDA .......................................................................................................... 4**

4.1. HIDROGRAMA TRIANGULAR ............................................................................................ 4

4.2. HEC-HMS ............................................................................................................................. 6

4.3. CAUDALES DE CRECIDAS ADOPTADOS.......................................................................... 6
**5.** **CAUDAL DETRÍTICO ................................................................................................................. 7**

**TABLAS**

TABLA-1: Precipitaciones Máx. en 24 Horas.......................................................... 3

TABLA-2: Tiempo de Concentración Estimado y Adoptado ............................... 4

TABLA-3: Caudales de Crecidas - Hidrograma Unitario Triangular [m [3] /s] ........ 5

TABLA-4: Caudales de Crecidas - HEC-HMS [m [3] /s] .............................................. 6

TABLA-5: Caudales de Crecidas con Flujo Detrítico [m [3] /s] ................................. 7

**FIGURAS**

FIGURA-1: Cuencas Aportantes .................................................................................. 1

FIGURA-2: Ubicación de las Estaciones Meteorológicas ........................................ 2

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

**1.** **ASPECTOS GENERALES**

El estudio de caudales de crecidas se plantea para dos cuencas aportantes, denominadas

como:

 Cuenca Obra de Desvío: es aquella que cierra en el sitio de implantación del pretil
proyectado para interceptar y desviar los caudales afluentes al área a proteger.

 Cuenca Completa: es la prolongación de la cuenca anterior hasta la Ruta 5 Norte.

En la siguiente figura se presenta la delimitación de ambas cuencas.

FIGURA-1: Cuencas Aportantes

Fuente: Elaboración Propia. Imágenes Satelitales

Para el cálculo de crecidas pluviales en cuencas naturales que no cuentan con información
fluviométrica, como es el presente caso, se dispone de una serie de métodos de cálculo,
tales como el Hidrograma Unitario Triangular, la fórmula Racional y los propuestos en el
“Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin Información
Fluviométrica” de la DGA (1995), dentro de los cuales se tiene el Método Racional
Modificado, Verni-King Modificado y la fórmula DGA-AC.

Con excepción del Hidrograma Unitario Triangular, las otras relaciones de cálculo
mencionadas no son aplicables a las cuencas en estudio, ya que éstas son válidas entre la III
y IX región del país, mientras que las cuencas en estudio se ubican en la II región. De este
modo y con el objeto de verificar los resultados que presenta el Hidrograma Unitario
Triangular, también se estimarán los caudales de crecidas con el HEC-HMS.

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

**2.** **ANÁLISIS DE PRECIPITACIONES**

Considerando lo expuesto, la estimación de los caudales de crecidas se realizó mediante la
relación precipitación escorrentía. Para estos fines se utilizó el registro estadístico
pluviométrico de los últimos 40 años, es decir la estadística entre los años hidrológicos 1980
a 2019, ambos inclusive, por considerar que este período es suficiente y representa de mejor
manera los eventos de crecidas de la situación actual y futura en el área de estudio.

Aun cuando en la zona de interés para el estudio existen nueve estaciones meteorológicas,
para obtener los valores de precipitación máximas en 24 horas asociados a distintos
períodos de retorno, solamente se utilizaron las series de datos de las estaciones
meteorológicas Antofagasta y Baquedano, pues son las únicas que disponen de un amplio
registro de precipitaciones medidas. En la siguiente figura se presenta la ubicación de las
estaciones meteorológicas mencionadas.

FIGURA-2: Ubicación de las Estaciones Meteorológicas

Fuente: Elaboración Propia. Imágenes Satelitales

A los valores de precipitación máximas diarias de las estaciones previamente identificadas,

se les realizó un análisis de frecuencia sobre la base de las funciones de densidad de

probabilidades Normal, Log Normal, Pearson, Log-Pearson y Gumbel (Ver Anexo A). En una
primera instancia del cálculo, en el ajuste de la función densidad de probabilidad, no se
incluyen valores nulos. Luego, se realiza un ajuste de la probabilidad de ocurrencia para
considerar el efecto de los valores nulos en el registro de la información.

La selección de la función de mejor ajuste se realizó mediante la aplicación del test ChiCuadrado y a través de la inspección de la representación gráfica de los puntos observados,

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

empleando para ello la distribución empírica de Weibull para asignar probabilidades de
excedencia. Para el test Chi-Cuadrada se utilizó un nivel de significancia de 0,05.

Cabe destacar que la selección de la mejor función de ajuste prioriza el ajuste de los eventos
extremos, con el objetivo de estimar de mejor manera los eventos de precipitación que
condicionarán el diseño de las obras (T=100 años de período de retorno), resultando
seleccionadas la distribución Gumbel para Baquedano y Log Normal para Antofagasta

Así, considerando los resultados obtenidos de la correspondiente función de probabilidad
para cada una de las estaciones, se calcularon los valores de precipitaciones máximas diarias
para 2, 5, 10, 25, 50, 100, 150 y 200 años de período de retorno.

Para convertir las precipitaciones máximas diarias a precipitaciones máximas en 24 horas, las
máximas diarias se amplifican por 1,1.

Debido a las características climáticas de la zona en estudio, donde la mayor parte de las
precipitaciones son de origen convectivo y al análisis de eventos importantes en la ciudad
de Antofagasta comparándoles con los registros de la estación Baquedano, se concluye que
no existe una correlación entre ambas estaciones.

De acuerdo con lo anterior y la ubicación de la zona de estudio, se adoptó como resultado
el promedio de las precipitaciones máximas en 24 horas de las estaciones Antofagasta y
Baquedano. Los valores obtenidos se presentan en la Tabla 1.

TABLA-1: Precipitaciones Máx. en 24 Horas

|T|Precipitaciones Máx en<br>24 Hrs|
|---|---|
|~~**[años]**~~|~~**[mm]**~~|
|2 <br>|0,3<br>|
|~~5 ~~<br>|~~3,7~~<br>|
|~~10~~|~~9,8~~|
|25<br>|19,8<br>|
|~~50~~<br>|~~30,2~~<br>|
|~~100~~|~~44,1~~|
|150<br>|54,3<br>|
|~~200~~<br>|~~62,6~~|

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

**3.** **TIEMPO DE CONCENTRACIÓN**

En atención a las diferentes fórmulas para estimar el tiempo de concentración en cuencas
no urbanas, se consideraron las más utilizadas normalmente de modo de tener un amplio
espectro de resultados para tomar la decisión respecto a la elección de uno de ellos o la
combinación de dos o más resultados. Así, a continuación, en la Tabla 2 se presentan las
fórmulas utilizadas y sus respectivos resultados.

TABLA-2: Tiempo de Concentración Estimado y Adoptado

(1) Promedio de los valores obtenidos.

(2) Promedio de los valores obtenidos, descartando los valores extremos

**4.** **CAUDALES DE CRECIDA**

**4.1.** **HIDROGRAMA TRIANGULAR**

El cálculo de los caudales de crecida en los puntos de interés, mediante el Hidrograma
Triangular (Soil Conservation Service, S.C.S) se realiza utilizando las siguientes expresiones:

### C  A q p = T

_P_

### _t_

_r_
### T = + t

P _P_
### 2

Donde:

A: Área pluvial aportante de la cuenca (km [2] ).
C: Factor de Forma.
t r : Tiempo de duración del intervalo de lluvia (h).
t P : Tiempo de retardo (t P = 0,6∙t C ) (h).
t C : Tiempo de concentración de la cuenca (h)
Tp: Tiempo al peak (h)

Además, la duración de la recesión del hidrograma se estima en función del tiempo al peak,
mediante un coeficiente que varía según la forma del hidrograma Tp.

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

Considerando las características de la zona en estudio se acepta que las cuencas de interés
pueden asociarse a “zonas rurales con pendientes leves” y, de acuerdo a la bibliografía
especializada, el factor de forma y la relación entre el tiempo de recesión y el tiempo al peak
tienen valores de 0,86 y 5,50 respectivamente.

Por otra parte, para la determinación de las precipitaciones efectivas asociadas a estos
eventos se adopta el método de la Curva Número, el cual permite estimar las precipitaciones
de escorrentía directa e infiltraciones como función de las características morfológicas y de
uso de suelo de las cuencas. La referencia Urban Hydrology for Small Watersheds (TR-55).
Departamento de Agricultura de Estados Unidos (USDA). 2004, para zonas semiáridas para
un suelo tipo C, cubierto de hierbas y malezas con condiciones pobres, recomienda un valor
Curva Número de 85 (ver Tabla 9-2d de dicho documento). Además, considerando las
características áridas de la zona, se estima razonable suponer condiciones antecedentes de
humedad secas, sin embargo, se considerará conservadoramente condiciones antes de
humedad normales.

Finalmente, adoptando la distribución de precipitaciones propuesta por Espíldora y
Echavarría, se definen los siguientes caudales de crecidas para las dos cuencas consideradas
en este estudio.

TABLA-3: Caudales de Crecidas - Hidrograma Unitario Triangular [m [3] /s]

|T<br>[años]|Obra de Desvío<br>[m3/s]|Completa<br>[m3/s]|
|---|---|---|
|2|0.00|0.00|
|5 <br>|0.00<br>|0.00<br>|
|~~10~~<br>|~~0.02~~<br>|~~0.02~~<br>|
|~~25~~<br>|~~1.5~~<br>|~~1.9~~<br>|
|~~50~~<br>|~~4.4~~<br>|~~5.5~~<br>|
|~~100~~|~~9.1~~|~~11.4~~|
|150|12.9|16.2|
|200<br>|16.2<br>|20.4|

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

**4.2.** **HEC-HMS**

Para el verificar los resultados de los caudales de crecidas en las cuencas en estudio, se utilizó
el software HEC-HMS, desarrollado por el U.S. Army Corps of Engineers.

El hidrograma de crecida es estimado aplicando el hidrograma unitario del Soil Conservation
Service (SCS, Unit Hydrograph). Se utiliza un valor de PRF para este hidrograma de 484 (valor
estándar).

El lag time o tiempo de retardo es estimado como un 60% del tiempo de concentración de
la respectiva cuenca.

La infiltración de las aguas es estimada utilizando el método Curva Número. Se utilizar un
valor de 85, definido en el capítulo 3.4.2 de este documento.

Para la distribución de las precipitaciones a lo largo del tiempo, y al igual que para el método
del Hidrograma Triangular, se utiliza la distribución G propuestas por Espíldora y Echavarría.

Los resultados obtenidos mediante este método de cálculo se presentan en la Tabla 4, a
continuación.

TABLA-4: Caudales de Crecidas - HEC-HMS [m [3] /s]

|T<br>[años]|Obra de Desvío<br>[m3/s]|Completa<br>[m3/s]|
|---|---|---|
|2 <br>|0.0<br>|0.0<br>|
|~~5 ~~<br>|~~0.0~~<br>|~~0.0~~<br>|
|~~10~~<br>|~~0.0~~<br>|~~0.0~~<br>|
|~~25~~<br>|~~1.8~~<br>|~~2.3~~<br>|
|~~50~~<br>|~~4.9~~<br>|~~6.3~~<br>|
|~~100~~<br>|~~10.1~~<br>|~~12.8~~<br>|
|~~150~~<br>|~~14.2~~<br>|~~18.1~~<br>|
|~~200~~|~~17.7~~|~~22.6~~|

**4.3.** **CAUDALES DE CRECIDAS ADOPTADOS**

Considerando los valores de caudales de crecidas obtenidos con ambos métodos,

considerando un criterio conservador para efectos del diseño de las obras, se adopta como
caudal de crecida el obtenido a través del HEC-HMS. Los resultados han sido presentados
en la Tabla 4.

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

**5.** **CAUDAL DETRÍTICO**

De acuerdo al documento “Guías Metodológicas para Presentación y Revisión Técnica de
Proyectos de Modificación de Cauces Naturales y Artificiales”, se indica que la concentración
de detritos puede alcanzar hasta el 50% con respecto al volumen total de la crecida. Por otro
lado, se indica y recomienda que la concentración de los sedimentos no sea inferior al 30%.

De acuerdo con lo anterior, se adopta una concentración promedio de 40% (C = 0,4).

La relación para el cálculo del caudal detrítico se presenta a continuación:

Q detr =

Q liq

1 −C

Dónde:

Qdetr: Caudal sólido más caudal líquido
Qlíq: Caudal líquido
C: Concentración en volumen de sólidos

Luego, los resultados de caudal de crecidas que incluyen flujo detrítico se presentan en la
Tabla 5.

TABLA-5: Caudales de Crecidas con Flujo Detrítico [m [3] /s]

|T<br>[años]|Obra de Desvío<br>[m3/s]|Completa<br>[m3/s]|
|---|---|---|
|2|0,0|0,0|
|5|0,0|0,0|
|10|0,0|0,0|
|25|3,0|3,8|
|50|8,2|10,5|
|100|16,8|21,3|
|150<br>|23,7<br>|30,2<br>|
|~~200~~|~~29,5~~|~~37,7~~|

APÉNDICE PAS157-2: ESTUDIOS HIDROLÓGICOS E HIDRÁULICOS

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 5.**

| T<br>[años] | Obra de Desvío<br>[m3/s] | Completa<br>[m3/s] |
| --- | --- | --- |
| 2 | 0,0 | 0,0 |
| 5 | 0,0 | 0,0 |
| 10 | 0,0 | 0,0 |
| 25 | 3,0 | 3,8 |
| 50 | 8,2 | 10,5 |
| 100 | 16,8 | 21,3 |
| 150<br> | 23,7<br> | 30,2<br> |
| ~~200~~ | ~~29,5~~ | ~~37,7~~ |
