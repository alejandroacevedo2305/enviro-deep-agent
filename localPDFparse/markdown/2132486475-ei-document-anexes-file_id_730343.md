---
title: Estudio Hidráulico PAS 156_PEPV-R2
author: Macarena Rivera
date: D:20170608211633Z
language: es
type: report
pages: 29
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - N
  - ANEXO A. PERFILES TRANSVERSALES HEC-RAS SITUACIÓN SIN PROYECTO
  - ANEXO B. PERFILES TRANSVERSALES HEC-RAS SITUACIÓN CON PROYECTO
-->

**INFORME FINAL**
**ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS**

Rev. 2

**PROYECTO PARQUE EMPRESARIAL PUERTO VARAS**

INMOBILIARIA Y AGROINDUSTRIAL DEL LAGO LTDA.

**Fecha: 26/04/2016**

**Realizado por:**
Sebastián Rivadeneira Simpson
Ingeniero Civil Hidráulico

Universidad de Chile

2

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**CONTENIDO**

**1.** **INTRODUCCIÓN ................................................................................................................ 5**

**2.** **OBJETIVOS ....................................................................................................................... 5**

**3.** **REFERENCIAS .................................................................................................................. 5**

**4.** **UBICACIÓN Y DESCRIPCIÓN GENERAL ....................................................................... 6**

**5.** **HIDROLOGÍA ..................................................................................................................... 9**

5.1 Situación actual ..................................................................................................................................... 9

5.2 Obtención de las precipitaciones de diseño ....................................................................................... 10

5.3 Cuencas de estudio ............................................................................................................................ 11

5.3.1 Situación sin proyecto ......................................................................................................................... 12

5.3.2 Situación con proyecto ........................................................................................................................ 13

5.4 Obtención de los caudales de diseño ................................................................................................ 14

5.4.1 Criterios generales de cálculo ............................................................................................................ 14

1.1.1 Método Racional ................................................................................................................................. 14

5.4.2 Coeficientes de escorrentía ................................................................................................................ 15

5.4.3 Tiempos de concentración .................................................................................................................. 15

5.4.4 Cálculo de la intensidad de diseño ..................................................................................................... 16

5.4.5 Caudal de diseño ................................................................................................................................ 16

**6.** **EJE HIDRÁULICO ........................................................................................................... 17**

6.1 Descripción y criterios generales de cálculo ...................................................................................... 17

6.2 Cálculo del Coeficiente de Rugosidad. .............................................................................................. 17

6.3 Perfiles Transversales ........................................................................................................................ 19

6.4 Resultados modelación sin proyecto .................................................................................................. 21

6.5 Resultados modelación con proyecto ................................................................................................ 22

**7.** **CONCLUSIONES ............................................................................................................. 24**

3

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**TABLAS**

Tabla 1. Coordenadas Propiedad ................................................................................................................. 6
Tabla 2: Coeficientes de escorrentía para T=10 años (Manual de Carreteras) .......................................... 15
Tabla 3. Caudales de Diseño ...................................................................................................................... 16
Tabla 4. Valores adoptados coeficiente de rugosidad ................................................................................ 18
Tabla 5. Resultados Eje Hidráulico por PTs, T=100 años (sin proyecto) .................................................... 21
Tabla 6. Resultados Eje Hidráulico por PTs, T=100 años (con proyecto) ................................................... 23

**FIGURAS**

Figura 1: Ubicación general área de proyecto .............................................................................................. 6
Figura 2: Trazados en planta de fosos proyectados ..................................................................................... 7
Figura 3: Descargas a cauce natural ............................................................................................................ 8
Figura 4: Situación hídrica natural sector proyecto ....................................................................................... 9
Figura 5: Áreas de drenaje natural de cuenca ............................................................................................ 10
Figura 6: Plano de Isoyetas de Precipitación Media Anual en el área del proyecto ................................... 11
Figura 7: Cuencas situación sin proyecto ................................................................................................... 12
Figura 8: Cuencas situación con proyecto .................................................................................................. 13
Figura 9. Planta topográfica cauce natural con perfiles transversales ........................................................ 19
Figura 10. Planta esquemática con perfiles transversales cauce natural en Hec-Ras ............................... 20
Figura 11. Perfil longitudinal cauce natural sin proyecto T=100 años ......................................................... 21
Figura 12. Perfil longitudinal cauce natural con proyecto T=100 años ........................................................ 22

**ANEXOS**

**ANEXO A:** PERFILES TRANSVERSALES HEC-RAS SITUACIÓN SIN PROYECTO

**ANEXO B:** PERFILES TRANSVERSALES HEC-RAS SITUACIÓN CON PROYECTO

4

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**1.** **INTRODUCCIÓN**

En el marco de la ampliación del proyecto de urbanización del Parque Empresarial Puerto Varas,

emplazado en la comuna del mismo nombre en el sector La Laja, resulta necesario realizar una

verificación de la posible afectación de cauces naturales por descargas de aguas asociadas a las obras de

evacuación de aguas lluvias del parque.

El proyecto propone la división del terreno de 119,64 há., a parcelas industriales de 5.000 m [2] cada una

aprox; que podrán destinarse a uso industrial, más las correspondientes zonas de dominio común

destinadas a equipamiento, áreas verdes y vialidad interior. El loteo ha sido concebido a partir de la

necesidad de nuevos espacios para el desarrollo de actividades industriales, por sobre los límites de las

ciudades de Puerto Varas y Puerto Montt.

Como parte necesaria para el desarrollo del proyecto, en el contexto de la primera ampliación de éste, la

Dirección General de Aguas (DGA), a través del Servicio de Evaluación Ambiental (SEA), solicitó la

elaboración del Permiso Ambiental Sectorial para modificación de cauces del artículo 156 de la ley

19.300 (PAS 156), toda vez que el manejo de aguas lluvias del proyecto considera evacuación de estas

aguas hacia un cauce natural. Para ello se debió modelar hidráulicamente el cauce en las situaciones con

y sin proyecto.

Cabe hacer presente que, para la realización de la primera ampliación, el Estudio Hidráulico consideró el

peor escenario posible; esto es, que la totalidad del terreno era parcelado. En este contexto, esta

ampliación que se presenta al SEIA no genera cambios en los resultados de dicho informe; sin embargo,

igual fue revisado y se reproduce a continuación.

El presente documento, y en el contexto de esta segunda ampliación del proyecto en 30 parcelas,

corresponde al estudio hidrológico e hidráulico del cauce natural

**2.** **OBJETIVOS**

Los objetivos principales de este estudio son:

 - Revisión del estudio hidrológico realizado para el diseño de las obras de evacuación de aguas

lluvias.

 - Determinación de caudales asociados al cauce de interés en la situación con y sin proyecto.

 - Modelación hidráulica del cauce de interés para las situaciones con y sin proyecto.

**3.** **REFERENCIAS**

1. “Manual de cálculo de crecidas y caudales mínimos en cuencas sin información fluviométrica”,

DGA, 1995.

2. Manual de Carreteras del Ministerio de Obras Públicas de Chile (MOP), 2014.

3. “Guía de diseño y especificaciones de elementos urbanos de infraestructura de aguas lluvias” del

Ministerio de Vivienda y Urbanismo, año 2005.

4. “Precipitaciones máximas en 1, 2 y 3 días”, Dirección General de Aguas del MOP, 2014.

5

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

5. “Balance Hídrico de chile”, Dirección General de Aguas del MOP, 2014.

6. “Hidráulica de Canales Abiertos”, Ven Te Chow, McGraw-Hill, 1959.

7. Informe Técnico, Estudio Hidrológico de mini cuenca, Parque Empresarial Puerto Varas Primera

etapa. CMC Ingeniería y Construcción, 2015.

8. Informe Final - Estudio Hidrológico y Obras de evacuación de aguas lluvias, Parque Empresarial

Puerto Varas, 2016.

**4.** **UBICACIÓN Y DESCRIPCIÓN GENERAL**

Tal como se hizo mención en la introducción del presente documento, el proyecto se emplaza en el

sector la Laja, al costado oeste de la Ruta 5 Km. 1.012, comuna de Puerto Varas, provincia de Llanquihue,

Región de Los Lagos.

**Figura 1: Ubicación general área de proyecto**

El proyecto contempla la división del terreno de 119,64 há., a parcelas industriales de 5.000 m [2] cada una

aproximadamente. En la Tabla 1 se muestran las coordenadas del punto centro del predio del proyecto.

**Tabla 1. Coordenadas Propiedad**

|Col1|Este (m)|Norte (m)|
|---|---|---|
|Propiedad|669.664 (E)|5.416.290 (S)|

**Datum: SIRGAS (WGS84) Huso: 18**

6

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

El estudio de obras de evacuación de aguas lluvias del proyecto (Referencia 8), propuso un diseño de

obras interiores de evacuación de aguas lluvias, el cual se muestra en la Figura 2.

**Figura 2: Trazados en planta de fosos proyectados**

7

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

De la figura anterior, se desprende que existen dos descargas al “foso sur” señalado en el informe de la

Referencia 8, el cual corresponde en realidad a un cauce natural sin nombre que recorre todo el borde

sur del Parque Empresarial. Dichas descargas se muestran con mayor detalle en la Figura 3.

# N

PREDIO PARQUE

EMPRESARIAL

**CAUCE NATURAL**

**"FOSO SUR"**

**FOSO OESTE**

**PUNTO**

**DESCARGA**

**OBRAS INTERIORES**

**AGUAS LLUVIAS**

**DESCARGA**

**FOSO OESTE**

**Figura 3: Descargas a cauce natural**

El foso oeste es un cauce artificial que existe antes de la materialización del proyecto, por lo tanto, este

estudio considera solamente la descarga de las obras interiores de aguas lluvias como posible afectación

al cauce natural, aun cuando en la modelación hidráulica el caudal asociado al foso oeste será

debidamente incorporado.

8

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**5.** **HIDROLOGÍA**

**5.1** **Situación actual**

Como ya se ha mencionado, el terreno se encuentra limitado en su deslinde sur por un cauce natural

cuyo origen atraviesa desde el lado este de la carretera y conduce las aguas como afluente del río negro,

tal como se muestra en la Figura 4.

### N

**PARQUE**

**EMPRESARIAL**

**FOSOS**
**CAUCE**
**EXISTENTES**
**NATURAL**

**SUR**

**Figura 4: Situación hídrica natural sector proyecto**

El resto del terreno se encuentra rodeado en todo su perímetro por fosos de drenaje preexistentes

elaborados mayoritariamente durante la construcción del tramo concesionado de la ruta 5.

Se define de este modo una mini cuenca de aproximadamente 119,64 hectáreas, la cual presenta el

esquema de descarga natural de aguas lluvia, mostrado en la **Figura 5** .

9

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**Figura 5: Áreas de drenaje natural de cuenca**

**5.2** **Obtención de las precipitaciones de diseño**

Para el diseño de obras hidráulicas de pequeña y mediana envergadura en cuencas sin información

fluviométrica ni pluviométrica, la Dirección General de Aguas (DGA) desarrolló un Manual de

procedimientos de cálculo de caudales máximos y mínimos en Chile a partir de los registros de las

estaciones hidrométricas distribuidas en el país, lo cual permitió desarrollar mapas de isoyetas para el

Balance Hídrico Nacional y Precipitaciones Máximas en 1, 2 y 3 días de las precipitaciones medias

anuales y las máximas diarias con período de retorno 10 años (Referencia 4).

**Datos pluviométricos**

10

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**Precipitación máxima diaria con período de retorno 10 años**,

Según acápite 2.6 Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin información

Fluviométrica, en base a los planos de isoyetas del estudio Precipitaciones Máximas en 1, 2 y 3 días.

P 2410 = 65 mm

**Precipitación media anual**

Según acápite 2.7, Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin información

Fluviométrica, estimada en base a los planos de isoyetas del estudio Balance Hídrico.

PMA = 2000 mm

**Figura 6: Plano de Isoyetas de Precipitación Media Anual en el área del proyecto**

**5.3** **Cuencas de estudio**

La materialización del proyecto en la zona de estudio, define dos situaciones para el drenaje de las aguas

lluvias; estas son (1) sin proyecto y (2) con proyecto.

11

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**5.3.1** **Situación sin proyecto**

Para la situación sin proyecto, se tiene la configuración mostrada en la Figura 7.

**CAUCE**

**NATURAL**

### N

**MINI**

**CUENCA**

**FOSO OESTE**

**SUR**

**CUENCA**

**CAUCE**

**NATURAL**

**Figura 7: Cuencas situación sin proyecto**

Para la cuenca asociada al cauce natural en la situación sin proyecto, se tienen los siguientes datos:

**Área aportante**

- Latitud: 41o 22’

- Línea de nieves: 770 msnm (Referencia 1)

Área pluvial (Ap)= 638 Ha

- Área nival (An)= 0 km2

**Parámetros morfológicos**

- Longitud cauce principal: L= 3,93 Km

- Longitud centro de gravedad hasta punto de salida Lg=2,3 km

- Desnivel máximo cuenca= 35 m

Para la mini cuenca asociada al foso oeste mostrada en Figura 7, los caudales por periodo de retorno se
obtienen del estudio de la Referencia 8, siento 1,15 m [3] /s el caudal asociado a T = 100 años.

12

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**5.3.2** **Situación con proyecto**

Para la situación con proyecto, cambia la distribución de áreas aportantes, pues existe una porción del

predio Parque empresarial que drena por las obras interiores de evacuación de aguas lluvias para

posteriormente descargar al cauce natural. Por lo tanto, se tiene la configuración mostrada en la Figura

8.

## N

**MINI**

**CUENCA**

**FOSO OESTE**

**MINI CUENCA**

**OBRAS INTERIORES**
**DE EVACUACIÓN DE**

**AGUAS LLUVIAS**

**CAUCE**

**NATURAL**

**SUR**

**CUENCA**

**CAUCE**

**NATURAL**

**Figura 8: Cuencas situación con proyecto**

En este caso, para la cuenca asociada al cauce natural en la situación con proyecto, se tienen los

siguientes datos:

**Área aportante**

- Latitud: 41o 22’

- Línea de nieves: 770 msnm (Referencia 1)

Área pluvial (Ap)= 597 Ha

- Área nival (An)= 0 km2

13

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**Parámetros morfológicos**

- Longitud cauce principal: L= 3,93 Km

- Longitud centro de gravedad hasta punto de salida Lg=2,3 km

- Desnivel máximo cuenca= 35 m

Como se señaló en numeral anterior, para la mini cuenca asociada al foso oeste mostrada en la Figura 8,
los caudales por período de retorno se obtienen del estudio de la Referencia 8, siendo 1,15 m [3] /s el

caudal asociado a T = 100 años.

Para la mini cuenca asociada a la descarga de obras interiores de evacuación de aguas lluvias mostrada

en la misma Figura 8, se considerará el caudal asociado a la mini cuenca completa del Parque
Empresarial, el cual corresponde a **2,01 m** **[3]** **/s** para T = 100 años. Vale mencionar, que este caudal incluye
los 1,15 m [3] /s del foso oeste. (ver numeral 6 de Referencia 8), sin embargo, por criterio conservador, se

considerarán ambos caudales como si fueran independientes.

**5.4** **Obtención de los caudales de diseño**

**5.4.1** **Criterios generales de cálculo**

Del numeral precedente, se desprende que se deben calcular los caudales de diseño para las cuencas en

las situaciones con y sin proyecto.

El método de cálculo a utilizar será la fórmula racional, pues de los estudios anteriores (Referencias 7 y

8) se sabe que entrega resultados más conservadores para la zona de estudio.

1.1.1 Método Racional

Este método relaciona el empleo de coeficientes de escorrentía que mayor se ajustan a los resultados de

los análisis de frecuencias efectuados en el estudio desarrollado para su elaboración.

El cálculo de caudales que se realiza a través del Método Racional, utiliza la siguiente fórmula:

 ́ _I_ ́ _A_
_Q =_ _[C ]_
_3.6_

En que:

#### = _Q_

Gastos máximos en crecida, en m [3] /s

_C_ = Coeficiente de escorrentía

#### I =

Intensidad máxima, correspondiente a una lluvia de duración igual al tiempo de concentración

del sector analizado, en mm/hr

#### A =

Superficie pluvial de la cuenca aportante en km [2]

Como se observa, es necesario determinar el coeficiente de escorrentía y la intensidad de diseño para la

superficie.

14

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**5.4.2** **Coeficientes de escorrentía**

Este parámetro depende de las características geomorfológicas del sector a analizar, por ejemplo: la

topografía, la vegetación, la capacidad de almacenamiento, etc. Por tal motivo, depende

fundamentalmente de la inspección del terreno.

Una vez reconocido el terreno, se emplea la Tabla 3.702.503.B del Manual de Carreteras Vol. 3 para

definir el valor de este coeficiente. Con esto se estima un coeficiente de escorrentía de 0,29 para T=10

años (Relieve bajo a normal 0,10; infiltración normal 0,07; cobertura vegetal abundante 0,05 y

almacenamiento superficial normal 0,07).

**Tabla 2: Coeficientes de escorrentía para T=10 años (Manual de Carreteras)**

**5.4.3** **Tiempos de concentración**

El tiempo de concentración se calcula a partir de la relación del Manual de Carreteras:

t " = 0,95 ∙ H

15

,,*-.

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

Donde:

t c = Tiempo de concentración de la cuenca [hr]

L = longitud del cauce principal [km]

H = Desnivel máximo de la cuenca [m]

Con esto se tiene un tiempo de concentración de **1,17 hrs** o **70 min** para ambas cuencas (con y sin

proyecto), pues los parámetros longitud cauce principal y desnivel máximo, son los mismos en ambos

casos.

**5.4.4** **Cálculo de la intensidad de diseño**

El periodo de retorno considerado, de acuerdo a las recomendaciones del Manual de Carreteras

(Referencia 2) y las exigencias del PAS 156, será de **100 años.**

Por lo tanto, se consideran las intensidades de lluvia de la estación Puerto Montt (más cercana a zona de

estudio) para 100 años de periodo de retorno y duraciones de 1 y 2 horas.

I 00,, = 21,54 mm/hr

I 90,, = 17,64 mm/hr

Haciendo una regresión entre ambos valores para el tiempo de concentración de las cuencas, se tiene

que la intensidad de diseño es:

100
I 1,17 = 20,9 mm/hr

**5.4.5** **Caudal de diseño**

Finalmente, se presentan los caudales de diseño para las cuencas en situación con y sin proyecto:

**Tabla 3. Caudales de Diseño**

|Cuenca|Caudal [m3/s]|
|---|---|
|Sin proyecto|13,4|
|Con Proyecto|12,6|

16

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**6.** **EJE HIDRÁULICO**

**6.1** **Descripción y criterios generales de cálculo**

Para el análisis del comportamiento hidráulico del cauce natural se utilizará el software de aplicación

específica del Hydrologic Engineering Center - U.S. Army Corps of Engineers, HEC-RAS (Hidraulic

Engineering Center - River Analisis System) versión 4.1.

Hec-Ras es un programa de dominio público cuyo principal objetivo es el de calcular la elevación de la

superficie de la lámina de agua para un caudal y condiciones de flujo dadas, (flujo permanente o

estacionario), aunque HEC-RAS también puede ser empleado para movimientos transitorios, (no

permanentes) unidimensionales y para el cálculo de transporte de sedimentos.

Los fundamentos teóricos aplicados en este programa son los convencionales y el procedimiento de

cálculo se basa en la resolución de la ecuación unidimensional de la energía usando el método de etapas

fijas (Hydraulic References Manual Hec-Ras 4.1).

**Criterios generales**

 - Se consideraron tres situaciones para obtener el eje hidráulico: régimen subcrítico, régimen

supercrítico y el régimen mixto que representan la presencia del flujo súper y sub crítico en

forma alternada, tal y como se presenta en la naturaleza.

 - Para las condiciones de borde se utiliza la altura normal calculada con la ecuación de Manning

(Hidráulica de Canales Abiertos, Ven Te Chow). Este parámetro en general carece de

importancia cuando la extensión de la topografía es suficiente como para que el eje se

estabilice.

 - En el caso del cálculo de la altura normal, si no se conoce la pendiente de la línea de energía, se

ingresa un valor cercano a ésta, que es la pendiente del fondo del lecho; en la altura crítica,

existe la posibilidad de que el cálculo matemático de esta altura puede resultar en más de un

valor, por lo que se seleccionará aquel valor que entregue la menor altura o energía.

 - Es básico detectar en terreno, el nivel histórico alcanzado por las aguas, ya sea considerando

los rastros que dejó en el cauce o los sedimentos en las planicies de inundación, y así predecir

crecidas futuras.

**6.2** **Cálculo del Coeficiente de Rugosidad.**

De lo observado en terreno, es posible caracterizar al estero desde el punto de vista de su rugosidad.

Esto de acuerdo a la relación de COWAN, en los términos establecidos en la publicación Hidráulica de

Canales Abiertos Ven Te Chow, Tabla 5-5. La cual estima el coeficiente de rugosidad de Manning, a partir

de la separación de factores de incidencia:

_n = m ( n0 + n1 + n2 + n3 + n4 )_

17

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

Donde:

n : coeficiente de rugosidad de Manning.

m : factor de corrección por sinuosidad del cauce (meandros).

n0 : valor base, suponiendo cauce ideal.

n1 : valor adicional por irregularidades superficiales.

n2 : valor adicional por variaciones de forma y tamaño de las secciones transversales.

n3 : valor adicional por obstrucciones.

n4 : valor adicional según presencia de vegetación y condiciones del flujo.

**Tabla 4. Valores adoptados coeficiente de rugosidad**

|CONDICIONES DEL CAUCE|Col2|VALOR|Col4|Planicie|Cauce ppal.|
|---|---|---|---|---|---|
|<br> <br>MATERIAL<br>|Tierra|<br>n0 <br> <br>|0.020|0.020|0.020|
|<br> <br>MATERIAL<br>|Roca|Roca|0.022|0.022|0.022|
|<br> <br>MATERIAL<br>|Grava Fina|Grava Fina|0.024|0.024|0.024|
|<br> <br>MATERIAL<br>|Grava Gruesa|Grava Gruesa|0.028|0.028|0.028|
|<br> <br>GRADO DE IRREGULARIDAD<br>|Despreciable|<br>n1 <br> <br>|0.000|0.005|0.005|
|<br> <br>GRADO DE IRREGULARIDAD<br>|Leve|Leve|0.005|0.005|0.005|
|<br> <br>GRADO DE IRREGULARIDAD<br>|Moderado|Moderado|0.010|0.010|0.010|
|<br> <br>GRADO DE IRREGULARIDAD<br>|Alto|Alto|0.020|0.020|0.020|
|<br>VARIACIONES DE LAS SECCIONES<br>A LO LARGO DE LA SECCION<br> <br>|Graduales|<br> <br>n2 <br> <br>|0.000|0.003|0.003|
|<br>VARIACIONES DE LAS SECCIONES<br>A LO LARGO DE LA SECCION<br> <br>|Alternándose<br>Gradualmente|Alternándose<br>Gradualmente|<br>0.005|<br>0.005|<br>0.005|
|<br>VARIACIONES DE LAS SECCIONES<br>A LO LARGO DE LA SECCION<br> <br>|Alternándose<br>Frecuentemente|Alternándose<br>Frecuentemente|0.010|0.010|0.010|
|<br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br>|Despreciable|<br>n3 <br> <br>|0.000|0.013|0.015|
|<br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br>|Leve|Leve|0.010<br>0.015|0.010<br>0.015|0.010<br>0.015|
|<br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br>|Apreciable|Apreciable|0.020<br>|0.020<br>|0.020<br>|
|<br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br>|Alto|Alto|0.040<br>|0.040<br>|0.040<br>|
|<br>DENSIDAD DE VEGETACION<br> <br>|Baja|<br>n4 <br> <br>|0.005<br>|0.016|0.025|
|<br>DENSIDAD DE VEGETACION<br> <br>|Media|Media|0.010<br>0.015|0.010<br>0.015|0.010<br>0.015|
|<br>DENSIDAD DE VEGETACION<br> <br>|Alta|Alta|0.025<br>|0.025<br>|0.025<br>|
|<br>DENSIDAD DE VEGETACION<br> <br>|Muy Alta|Muy Alta|0.050<br>|0.050<br>|0.050<br>|
|<br>FRECUENCIA DE MEANDROS<br>|Leve|<br>m <br>|1.000|1|1|
|<br>FRECUENCIA DE MEANDROS<br>|Apreciable|Apreciable|1.150|1.150|1.150|
|<br>FRECUENCIA DE MEANDROS<br>|Alto|Alto|1.300|1.300|1.300|
||Valor de n|Valor de n|Valor de n|**0.057**|**0.068**|

18

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**6.3** **Perfiles Transversales**

Los perfiles transversales del cauce natural en el sector a analizar, fueron obtenidos mediante topografía

in situ. En la Figura 9 se muestra la planta topográfica con los perfiles transversales considerados.

**Figura 9. Planta topográfica cauce natural con perfiles transversales**

En Total son 25 perfiles transversales enumerados del 0 al 24 desde aguas abajo hacia aguas arriba

distanciados entre sí cada 20 m aproximadamente. En la siguiente figura se muestra la planta en Hec-Ras

con cada uno de los perfiles.

19

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**Figura 10. Planta esquemática con perfiles transversales cauce natural en Hec-Ras**

La incorporación del caudal asociado a las obras interiores de evacuación de aguas lluvias para la
situación con proyecto, correspondiente a 2,01 m [3] /s, se realiza en el perfil 8, mientras que el caudal

asociado al foso oeste (tanto con y sin proyecto) se incorpora en el perfil N° 1.

20

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**6.4** **Resultados modelación sin proyecto**

Se modeló el eje hidráulico considerando el caudal asociado al cauce natural en la situación sin proyecto.

El perfil longitudinal con eje hidráulico se muestra a continuación:

PEPV Plan: Plan 05 05-09-2016

Cauce Natural Sur

94

92

90

88

86

84

82

|Col1|Col2|Col3|Col4|Col5|Col6|Legend|
|---|---|---|---|---|---|---|
|||||||EG 100 años<br>WS 100 años<br>Crit 100 años<br>Ground<br>Left Levee<br>Right Levee|
||||||||
||||||||
||||||||
||||||||
||||||||

0 100 200 300 400 500 600

Main Channel Distance (m)

**Figura 11. Perfil longitudinal cauce natural sin proyecto T=100 años**

En la Tabla 5 se entregan los resultados de los principales parámetros hidráulicos por PTs.

**Tabla 5. Resultados Eje Hidráulico por PTs, T=100 años (sin proyecto)**

|Transversal|Caudal<br>(m3/s)|Cota Lecho<br>(msnm)|Eje<br>Hidráulico<br>(msnm)|Altura<br>Crítica<br>(msnm)|Altura<br>Energía<br>(msnm)|Pendiente<br>Energía<br>(m/m)|Vel.<br>Prom.<br>(m/s)|Area<br>(m2)|Ancho<br>Superfic. (m)|Froude<br>Transv.|
|---|---|---|---|---|---|---|---|---|---|---|
|**24.0**|13.40|92.97|93.69|93.51|93.75|0.00992|1.19|13.44|34.30|0.51|
|**23.0**|13.40|92.68|93.58|0.00|93.63|0.00529|1.16|16.12|29.89|0.40|
|**22.0**|13.40|91.86|93.57|0.00|93.59|0.00130|0.76|23.37|30.37|0.21|
|**21.0**|13.40|92.37|93.40|0.00|93.55|0.01559|2.02|9.82|22.34|0.68|
|**20.0**|13.40|91.70|93.20|0.00|93.37|0.01126|1.86|7.82|10.60|0.57|
|**19.0**|13.40|91.53|92.91|0.00|93.10|0.01248|1.98|7.31|8.54|0.61|
|**18.0**|13.40|91.27|92.61|0.00|92.81|0.01651|2.06|7.22|9.68|0.66|
|**17.0**|13.40|91.06|92.34|0.00|92.49|0.01526|1.83|8.16|12.70|0.65|
|**16.0**|13.40|90.58|91.93|91.84|92.14|0.01848|2.22|7.59|13.43|0.71|
|**15.0**|13.40|90.07|91.87|0.00|91.93|0.00305|1.23|12.95|11.68|0.31|
|**14.0**|13.40|90.29|91.43|91.43|91.79|0.02976|2.79|5.39|9.98|0.91|
|**13.0**|13.40|89.79|90.22|90.39|90.82|0.27011|3.44|3.91|16.60|2.26|
|**12.0**|13.40|88.89|90.25|90.04|90.29|0.00582|0.94|16.20|29.73|0.38|
|**11.0**|13.40|88.53|89.76|89.76|89.94|0.02437|2.06|8.35|23.41|0.77|
|**10.0**|13.40|88.31|89.28|89.32|89.54|0.04690|2.69|6.49|15.38|1.06|
|**9.0**|13.40|87.99|88.92|88.92|88.95|0.00711|1.07|17.43|38.65|0.42|
|**8.0**|13.40|87.28|88.33|88.38|88.58|0.03797|2.44|7.25|22.69|0.98|
|**7.0**|13.40|86.76|87.95|87.84|88.04|0.01225|1.58|11.49|25.34|0.58|
|**6.0**|13.40|85.84|87.18|87.18|87.56|0.02917|2.75|5.35|8.86|0.88|
|**5.0**|13.40|85.52|86.56|86.66|86.99|0.04202|3.08|5.21|9.96|1.07|
|**4.0**|13.40|85.09|86.52|86.23|86.56|0.00411|1.11|17.82|32.69|0.34|
|**3.0**|13.40|84.64|86.22|86.11|86.38|0.01038|1.94|10.05|23.41|0.54|
|**2.0**|13.40|84.38|85.82|85.82|86.12|0.01893|2.52|6.54|13.85|0.73|
|**1.0**|14.55|84.41|85.81|85.51|85.86|0.00437|1.23|18.18|33.35|0.37|
|**0.0**|14.55|83.97|85.42|85.33|85.65|0.01741|2.16|8.53|29.88|0.70|

21

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

Se observa de la tabla anterior, que los números de Froude resultan ser menores a 1, indicando un

régimen subcrítico o de río. Por otro lado, se tiene que el promedio de velocidad de escurrimiento es de

1,92 m/s.

El esquema con alturas de escurrimiento de cada uno de los perfiles transversales se entrega en el

ANEXO A al final de este documento.

**6.5** **Resultados modelación con proyecto**

Se modeló el eje hidráulico considerando el caudal asociado al cauce natural en la situación con proyecto
e incorporando el caudal de 2,01 m [3] /s asociado a las obras interiores de evacuación de aguas lluvias en

el perfil N°8. El perfil longitudinal con eje hidráulico se muestra a continuación:

PEPV Plan: Plan 06 05-09-2016

Cauce Natural Sur

94

92

90

88

86

84

82

|Col1|Col2|Col3|Col4|Col5|Col6|Legend|
|---|---|---|---|---|---|---|
|||||||EG 100 años<br>WS 100 años<br>Crit 100 años<br>Ground<br>Left Levee<br>Right Levee|
||||||||
||||||||
||||||||
||||||||
||||||||

0 100 200 300 400 500 600

Main Channel Distance (m)

**Figura 12. Perfil longitudinal cauce natural con proyecto T=100 años**

22

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

En la Tabla 6 se entregan los resultados de los principales parámetros hidráulicos por PTs.

**Tabla 6. Resultados Eje Hidráulico por PTs, T=100 años (con proyecto)**

|Transversal|Caudal<br>(m3/s)|Cota Lecho<br>(msnm)|Eje<br>Hidráulico<br>(msnm)|Altura<br>Crítica<br>(msnm)|Altura<br>Energía<br>(msnm)|Pendiente<br>Energía<br>(m/m)|Vel.<br>Prom.<br>(m/s)|Area<br>(m2)|Ancho<br>Superfic. (m)|Froude<br>Transv.|
|---|---|---|---|---|---|---|---|---|---|---|
|**24.0**|12.60|92.97|93.66|93.50|93.73|0.01067|1.19|12.52|34.10|0.52|
|**23.0**|12.60|92.68|93.55|0.00|93.60|0.00562|1.16|15.11|29.40|0.41|
|**22.0**|12.60|91.86|93.54|0.00|93.56|0.00128|0.74|22.38|29.01|0.21|
|**21.0**|12.60|92.37|93.35|93.21|93.51|0.01728|2.06|8.83|21.64|0.71|
|**20.0**|12.60|91.70|93.16|0.00|93.32|0.01133|1.82|7.42|10.31|0.57|
|**19.0**|12.60|91.53|92.88|0.00|93.06|0.01231|1.93|7.04|8.44|0.60|
|**18.0**|12.60|91.27|92.58|0.00|92.77|0.01624|2.00|6.95|9.60|0.65|
|**17.0**|12.60|91.06|92.31|0.00|92.46|0.01478|1.77|7.90|12.52|0.64|
|**16.0**|12.60|90.58|91.88|91.81|92.10|0.02010|2.24|6.97|12.87|0.74|
|**15.0**|12.60|90.07|91.83|0.00|91.89|0.00298|1.20|12.48|11.53|0.31|
|**14.0**|12.60|90.29|91.37|91.37|91.75|0.03309|2.82|4.91|6.76|0.95|
|**13.0**|12.60|89.79|90.22|90.38|90.75|0.23279|3.21|3.94|16.63|2.10|
|**12.0**|12.60|88.89|90.23|90.02|90.27|0.00580|0.92|15.60|29.63|0.38|
|**11.0**|12.60|88.53|89.74|89.74|89.92|0.02464|2.03|7.87|22.94|0.77|
|**10.0**|12.60|88.31|89.26|89.30|89.52|0.04739|2.65|6.19|15.10|1.06|
|**9.0**|12.60|87.99|88.92|88.92|88.95|0.00628|1.00|17.43|38.65|0.39|
|**8.0**|14.61|87.28|88.41|88.40|88.60|0.02600|2.18|9.05|23.58|0.83|
|**7.0**|14.61|86.76|87.99|0.00|88.08|0.01143|1.58|12.52|25.50|0.56|
|**6.0**|14.61|85.84|87.24|87.24|87.62|0.02792|2.79|5.88|9.64|0.87|
|**5.0**|14.61|85.52|86.59|86.70|87.05|0.04378|3.21|5.49|10.26|1.10|
|**4.0**|14.61|85.09|86.56|86.34|86.60|0.00415|1.14|19.14|34.19|0.34|
|**3.0**|14.61|84.64|86.27|86.16|86.42|0.00989|1.94|11.22|24.32|0.53|
|**2.0**|14.61|84.38|85.87|85.87|86.17|0.01843|2.56|7.27|14.19|0.72|
|**1.0**|15.76|84.41|85.83|85.51|85.88|0.00467|1.29|18.81|33.35|0.38|
|**0.0**|15.76|83.97|85.50|85.50|85.68|0.01371|2.02|11.17|39.41|0.63|

Se observa de la tabla anterior, que los números de Froude resultan ser menores a 1, indicando un

régimen subcrítico o de río. Por otro lado, se tiene que el promedio de velocidad de escurrimiento es de

1,90 m/s.

El esquema con alturas de escurrimiento de cada uno de los perfiles transversales se entrega en el

ANEXO B al final de este documento.

De la comparación entre la Tabla 5 y la Tabla 6 se desprende que la incorporación del caudal asociado a

las obras de evacuación de aguas lluvias del Parque Empresarial a partir del perfil 8, no afecta

significativamente el comportamiento hidráulico del cauce. La diferencia máxima en términos de cota

del eje hidráulico se produce precisamente en el perfil 8 y es menor a 10 cms.

23

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

**7.** **CONCLUSIONES**

Las conclusiones más significativas del estudio hidráulico del cauce natural son las siguientes.

**En cuanto a los caudales de diseño:**

 - El periodo de retorno seleccionado fue de 100 años según los requerimientos del Manual de

Carreteras y del PAS 156.

 - El cálculo se desarrolló a través del método racional, pues de los estudios anteriores

(Referencias 7 y 8) se sabe que entrega resultados más conservadores para la zona de

estudio.

 - Los caudales para la cuenca asociada al cauce natural en estudio, en situación con y sin

proyecto, son:

|Cuenca|Caudal [m3/s]|
|---|---|
|Sin proyecto|13,4|
|Con Proyecto|12,6|

**En cuanto a la modelación hidráulica:**

 - El cauce natural posee una sección transversal medianamente regular en el lecho con

abundante vegetación en los bordes. Esto se refleja en el n de Manning escogido para el

cálculo, el cual corresponde a 0,058 para el cauce y de 0,068 para la planicie.

 - Los perfiles transversales se obtuvieron mediante batimetría del cauce, considerando 300 m

aguas arriba y 200 m aguas del punto de descarga de las obras interiores de evacuación de

aguas lluvias.

 - Para la situación sin proyecto se obtuvo un régimen subcrítico o de río en el cauce natural,

con un promedio de velocidad de escurrimiento de 1,92 m/s.

 - Para la situación con proyecto, también se obtuvo un régimen subcrítico o de río en el cauce

natural, con un promedio de velocidad de escurrimiento de 1,90 m/s.

 - De la comparación de ejes hidráulicos entre las situaciones con y sin proyecto, se desprende

que la incorporación del caudal asociado a las obras de evacuación de aguas lluvias del

Parque Empresarial a partir del perfil 8, no afecta significativamente el comportamiento

hidráulico del cauce. La diferencia máxima en términos de cota del eje hidráulico se produce

precisamente en el perfil 8 y es menor a 8 cms, siendo aún menor en otros perfiles

transversales.

 - La disminución de velocidad de escurrimiento en ciertos perfiles para la situación con

proyecto pese a tener mayor caudal, se explica por el leve incremento de área transversal de

escurrimiento.

 - Se concluye que el cauce natural no se ve afectado por la incorporación puntual de caudal

asociada a las obras interiores de evacuación de aguas lluvias del Parque Empresarial Puerto

24

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

Varas. Si bien las riberas de dicho cauce se ven levemente inundadas en ciertos tramos para la

crecida de diseño (ver Anexo B), esta situación ocurre naturalmente en la situación sin

proyecto y se debe a la geomorfología del cauce, situación que no varía significativamente

con la incorporación de la descarga desde las obras de evacuación de aguas lluvias.

 - Respecto de las inundaciones sobre las riberas en ciertos perfiles transversales, se señala que

ocurren en su mayoría hacia el sector contrario al Parque Empresarial, pero son flujos de agua

con alturas y velocidades de escurrimiento menores, no significando un riesgo para las

personas ni mucho menos para las edificaciones ante una crecida de la magnitud considerada

(ver Anexos A y B).

 - El caudal de aguas lluvias seleccionado para la modelación fue el de periodo de retorno 100

años, es decir, es eventual y con probabilidad de ocurrir una vez en 100 años, aun cuando no

provoca alteraciones significativas en el normal escurrimiento del cauce natural. Este criterio

se utilizó de forma conservadora, siendo los periodos de retorno de diseño para obras de

drenaje, generalmente, menores a éste.

 - La obra de disposición final de aguas lluvias debe construirse de forma tal, que el flujo de

aguas desde el Parque Empresarial se realice en la misma dirección que tiene el cauce

natural, de manera de minimizar los impactos por fenómenos hidráulicos de segundo orden

como ondas superficiales, ondas cruzadas, corrientes secundarias, resaltos ondulares, etc, los

cuales podrían desordenar la confluencia.

 - Si bien no se vislumbra necesario construir una obra civil especial para la descarga, si se

recomienda proteger el fondo de ésta con enrocado simple en una longitud de 5 m antes de

la confluencia con el cauce natural.

 - Finalmente, es importante señalar que las aguas lluvias asociadas al drenaje del predio del

Parque Empresarial, han escurrido siempre naturalmente por pendiente hacia el cauce

natural analizado.

25

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

26

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

# ANEXO A. PERFILES TRANSVERSALES HEC-RAS SITUACIÓN SIN PROYECTO

27

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

28

ESTUDIO HIDRÁULICO PAS 156 PARQUE EMPRESARIAL PUERTO VARAS Rev. 2

# ANEXO B. PERFILES TRANSVERSALES HEC-RAS SITUACIÓN CON PROYECTO

29

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Coordenadas Propiedad****

| Col1 | Este (m) | Norte (m) |
| --- | --- | --- |
| Propiedad | 669.664 (E) | 5.416.290 (S) |

**Tabla 3.: Caudales de Diseño****

| Cuenca | Caudal [m3/s] |
| --- | --- |
| Sin proyecto | 13,4 |
| Con Proyecto | 12,6 |

**Tabla 4.: Valores adoptados coeficiente de rugosidad****

| CONDICIONES DEL CAUCE | Col2 | VALOR | Col4 | Planicie | Cauce ppal. |
| --- | --- | --- | --- | --- | --- |
| <br> <br>MATERIAL<br> | Tierra | <br>n0 <br> <br> | 0.020 | 0.020 | 0.020 |
| <br> <br>MATERIAL<br> | Roca | Roca | 0.022 | 0.022 | 0.022 |
| <br> <br>MATERIAL<br> | Grava Fina | Grava Fina | 0.024 | 0.024 | 0.024 |
| <br> <br>MATERIAL<br> | Grava Gruesa | Grava Gruesa | 0.028 | 0.028 | 0.028 |
| <br> <br>GRADO DE IRREGULARIDAD<br> | Despreciable | <br>n1 <br> <br> | 0.000 | 0.005 | 0.005 |
| <br> <br>GRADO DE IRREGULARIDAD<br> | Leve | Leve | 0.005 | 0.005 | 0.005 |
| <br> <br>GRADO DE IRREGULARIDAD<br> | Moderado | Moderado | 0.010 | 0.010 | 0.010 |
| <br> <br>GRADO DE IRREGULARIDAD<br> | Alto | Alto | 0.020 | 0.020 | 0.020 |
| <br>VARIACIONES DE LAS SECCIONES<br>A LO LARGO DE LA SECCION<br> <br> | Graduales | <br> <br>n2 <br> <br> | 0.000 | 0.003 | 0.003 |
| <br>VARIACIONES DE LAS SECCIONES<br>A LO LARGO DE LA SECCION<br> <br> | Alternándose<br>Gradualmente | Alternándose<br>Gradualmente | <br>0.005 | <br>0.005 | <br>0.005 |
| <br>VARIACIONES DE LAS SECCIONES<br>A LO LARGO DE LA SECCION<br> <br> | Alternándose<br>Frecuentemente | Alternándose<br>Frecuentemente | 0.010 | 0.010 | 0.010 |
| <br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br> | Despreciable | <br>n3 <br> <br> | 0.000 | 0.013 | 0.015 |
| <br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br> | Leve | Leve | 0.010<br>0.015 | 0.010<br>0.015 | 0.010<br>0.015 |
| <br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br> | Apreciable | Apreciable | 0.020<br> | 0.020<br> | 0.020<br> |
| <br>EFECTO RELATIVO DE LAS<br>OBSTRUCCIONES<br> | Alto | Alto | 0.040<br> | 0.040<br> | 0.040<br> |
| <br>DENSIDAD DE VEGETACION<br> <br> | Baja | <br>n4 <br> <br> | 0.005<br> | 0.016 | 0.025 |
| <br>DENSIDAD DE VEGETACION<br> <br> | Media | Media | 0.010<br>0.015 | 0.010<br>0.015 | 0.010<br>0.015 |
| <br>DENSIDAD DE VEGETACION<br> <br> | Alta | Alta | 0.025<br> | 0.025<br> | 0.025<br> |
| <br>DENSIDAD DE VEGETACION<br> <br> | Muy Alta | Muy Alta | 0.050<br> | 0.050<br> | 0.050<br> |
| <br>FRECUENCIA DE MEANDROS<br> | Leve | <br>m <br> | 1.000 | 1 | 1 |
| <br>FRECUENCIA DE MEANDROS<br> | Apreciable | Apreciable | 1.150 | 1.150 | 1.150 |
| <br>FRECUENCIA DE MEANDROS<br> | Alto | Alto | 1.300 | 1.300 | 1.300 |
|  | Valor de n | Valor de n | Valor de n | **0.057** | **0.068** |

**Tabla 5.: Resultados Eje Hidráulico por PTs, T=100 años (sin proyecto)****

| Transversal | Caudal<br>(m3/s) | Cota Lecho<br>(msnm) | Eje<br>Hidráulico<br>(msnm) | Altura<br>Crítica<br>(msnm) | Altura<br>Energía<br>(msnm) | Pendiente<br>Energía<br>(m/m) | Vel.<br>Prom.<br>(m/s) | Area<br>(m2) | Ancho<br>Superfic. (m) | Froude<br>Transv. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **24.0** | 13.40 | 92.97 | 93.69 | 93.51 | 93.75 | 0.00992 | 1.19 | 13.44 | 34.30 | 0.51 |
| **23.0** | 13.40 | 92.68 | 93.58 | 0.00 | 93.63 | 0.00529 | 1.16 | 16.12 | 29.89 | 0.40 |
| **22.0** | 13.40 | 91.86 | 93.57 | 0.00 | 93.59 | 0.00130 | 0.76 | 23.37 | 30.37 | 0.21 |
| **21.0** | 13.40 | 92.37 | 93.40 | 0.00 | 93.55 | 0.01559 | 2.02 | 9.82 | 22.34 | 0.68 |
| **20.0** | 13.40 | 91.70 | 93.20 | 0.00 | 93.37 | 0.01126 | 1.86 | 7.82 | 10.60 | 0.57 |
| **19.0** | 13.40 | 91.53 | 92.91 | 0.00 | 93.10 | 0.01248 | 1.98 | 7.31 | 8.54 | 0.61 |
| **18.0** | 13.40 | 91.27 | 92.61 | 0.00 | 92.81 | 0.01651 | 2.06 | 7.22 | 9.68 | 0.66 |
| **17.0** | 13.40 | 91.06 | 92.34 | 0.00 | 92.49 | 0.01526 | 1.83 | 8.16 | 12.70 | 0.65 |
| **16.0** | 13.40 | 90.58 | 91.93 | 91.84 | 92.14 | 0.01848 | 2.22 | 7.59 | 13.43 | 0.71 |
| **15.0** | 13.40 | 90.07 | 91.87 | 0.00 | 91.93 | 0.00305 | 1.23 | 12.95 | 11.68 | 0.31 |
| **14.0** | 13.40 | 90.29 | 91.43 | 91.43 | 91.79 | 0.02976 | 2.79 | 5.39 | 9.98 | 0.91 |
| **13.0** | 13.40 | 89.79 | 90.22 | 90.39 | 90.82 | 0.27011 | 3.44 | 3.91 | 16.60 | 2.26 |
| **12.0** | 13.40 | 88.89 | 90.25 | 90.04 | 90.29 | 0.00582 | 0.94 | 16.20 | 29.73 | 0.38 |
| **11.0** | 13.40 | 88.53 | 89.76 | 89.76 | 89.94 | 0.02437 | 2.06 | 8.35 | 23.41 | 0.77 |
| **10.0** | 13.40 | 88.31 | 89.28 | 89.32 | 89.54 | 0.04690 | 2.69 | 6.49 | 15.38 | 1.06 |
| **9.0** | 13.40 | 87.99 | 88.92 | 88.92 | 88.95 | 0.00711 | 1.07 | 17.43 | 38.65 | 0.42 |
| **8.0** | 13.40 | 87.28 | 88.33 | 88.38 | 88.58 | 0.03797 | 2.44 | 7.25 | 22.69 | 0.98 |
| **7.0** | 13.40 | 86.76 | 87.95 | 87.84 | 88.04 | 0.01225 | 1.58 | 11.49 | 25.34 | 0.58 |
| **6.0** | 13.40 | 85.84 | 87.18 | 87.18 | 87.56 | 0.02917 | 2.75 | 5.35 | 8.86 | 0.88 |
| **5.0** | 13.40 | 85.52 | 86.56 | 86.66 | 86.99 | 0.04202 | 3.08 | 5.21 | 9.96 | 1.07 |
| **4.0** | 13.40 | 85.09 | 86.52 | 86.23 | 86.56 | 0.00411 | 1.11 | 17.82 | 32.69 | 0.34 |
| **3.0** | 13.40 | 84.64 | 86.22 | 86.11 | 86.38 | 0.01038 | 1.94 | 10.05 | 23.41 | 0.54 |
| **2.0** | 13.40 | 84.38 | 85.82 | 85.82 | 86.12 | 0.01893 | 2.52 | 6.54 | 13.85 | 0.73 |
| **1.0** | 14.55 | 84.41 | 85.81 | 85.51 | 85.86 | 0.00437 | 1.23 | 18.18 | 33.35 | 0.37 |
| **0.0** | 14.55 | 83.97 | 85.42 | 85.33 | 85.65 | 0.01741 | 2.16 | 8.53 | 29.88 | 0.70 |

**Tabla 6.: Resultados Eje Hidráulico por PTs, T=100 años (con proyecto)****

| Transversal | Caudal<br>(m3/s) | Cota Lecho<br>(msnm) | Eje<br>Hidráulico<br>(msnm) | Altura<br>Crítica<br>(msnm) | Altura<br>Energía<br>(msnm) | Pendiente<br>Energía<br>(m/m) | Vel.<br>Prom.<br>(m/s) | Area<br>(m2) | Ancho<br>Superfic. (m) | Froude<br>Transv. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **24.0** | 12.60 | 92.97 | 93.66 | 93.50 | 93.73 | 0.01067 | 1.19 | 12.52 | 34.10 | 0.52 |
| **23.0** | 12.60 | 92.68 | 93.55 | 0.00 | 93.60 | 0.00562 | 1.16 | 15.11 | 29.40 | 0.41 |
| **22.0** | 12.60 | 91.86 | 93.54 | 0.00 | 93.56 | 0.00128 | 0.74 | 22.38 | 29.01 | 0.21 |
| **21.0** | 12.60 | 92.37 | 93.35 | 93.21 | 93.51 | 0.01728 | 2.06 | 8.83 | 21.64 | 0.71 |
| **20.0** | 12.60 | 91.70 | 93.16 | 0.00 | 93.32 | 0.01133 | 1.82 | 7.42 | 10.31 | 0.57 |
| **19.0** | 12.60 | 91.53 | 92.88 | 0.00 | 93.06 | 0.01231 | 1.93 | 7.04 | 8.44 | 0.60 |
| **18.0** | 12.60 | 91.27 | 92.58 | 0.00 | 92.77 | 0.01624 | 2.00 | 6.95 | 9.60 | 0.65 |
| **17.0** | 12.60 | 91.06 | 92.31 | 0.00 | 92.46 | 0.01478 | 1.77 | 7.90 | 12.52 | 0.64 |
| **16.0** | 12.60 | 90.58 | 91.88 | 91.81 | 92.10 | 0.02010 | 2.24 | 6.97 | 12.87 | 0.74 |
| **15.0** | 12.60 | 90.07 | 91.83 | 0.00 | 91.89 | 0.00298 | 1.20 | 12.48 | 11.53 | 0.31 |
| **14.0** | 12.60 | 90.29 | 91.37 | 91.37 | 91.75 | 0.03309 | 2.82 | 4.91 | 6.76 | 0.95 |
| **13.0** | 12.60 | 89.79 | 90.22 | 90.38 | 90.75 | 0.23279 | 3.21 | 3.94 | 16.63 | 2.10 |
| **12.0** | 12.60 | 88.89 | 90.23 | 90.02 | 90.27 | 0.00580 | 0.92 | 15.60 | 29.63 | 0.38 |
| **11.0** | 12.60 | 88.53 | 89.74 | 89.74 | 89.92 | 0.02464 | 2.03 | 7.87 | 22.94 | 0.77 |
| **10.0** | 12.60 | 88.31 | 89.26 | 89.30 | 89.52 | 0.04739 | 2.65 | 6.19 | 15.10 | 1.06 |
| **9.0** | 12.60 | 87.99 | 88.92 | 88.92 | 88.95 | 0.00628 | 1.00 | 17.43 | 38.65 | 0.39 |
| **8.0** | 14.61 | 87.28 | 88.41 | 88.40 | 88.60 | 0.02600 | 2.18 | 9.05 | 23.58 | 0.83 |
| **7.0** | 14.61 | 86.76 | 87.99 | 0.00 | 88.08 | 0.01143 | 1.58 | 12.52 | 25.50 | 0.56 |
| **6.0** | 14.61 | 85.84 | 87.24 | 87.24 | 87.62 | 0.02792 | 2.79 | 5.88 | 9.64 | 0.87 |
| **5.0** | 14.61 | 85.52 | 86.59 | 86.70 | 87.05 | 0.04378 | 3.21 | 5.49 | 10.26 | 1.10 |
| **4.0** | 14.61 | 85.09 | 86.56 | 86.34 | 86.60 | 0.00415 | 1.14 | 19.14 | 34.19 | 0.34 |
| **3.0** | 14.61 | 84.64 | 86.27 | 86.16 | 86.42 | 0.00989 | 1.94 | 11.22 | 24.32 | 0.53 |
| **2.0** | 14.61 | 84.38 | 85.87 | 85.87 | 86.17 | 0.01843 | 2.56 | 7.27 | 14.19 | 0.72 |
| **1.0** | 15.76 | 84.41 | 85.83 | 85.51 | 85.88 | 0.00467 | 1.29 | 18.81 | 33.35 | 0.38 |
| **0.0** | 15.76 | 83.97 | 85.50 | 85.50 | 85.68 | 0.01371 | 2.02 | 11.17 | 39.41 | 0.63 |
