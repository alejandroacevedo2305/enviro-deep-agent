---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 42
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de la pluma térmica salina de Central Termoeléctrica Angamos, Bahía de Mejillones del Sur, Región de Antofagasta
-->

## INFORME TECNICO

# Modelación de la pluma térmica salina de Central Termoeléctrica Angamos, Bahía de Mejillones del Sur, Región de Antofagasta

## Realizado por S Magister Oceanógrafo JUNIO 2015

## Índice de Contenidos

Índice de Figuras .................................................................................................................................. iii

Índice de Tablas ................................................................................................................................... iv

**1.** **Introducción** ............................................................................................................................... 5

**2.** **Metodología** ............................................................................................................................... 7

**2.1.** **Área de estudio** ....................................................................................................................... 7

**2.2.** **Esquema de Modelación** ....................................................................................................... 8

**2.2.1.** **Modelación de Campo Cercano** ................................................................................... 9

**2.2.2.** **Modelación de Campo Lejano** .................................................................................... 11

**2.3.** **Batimetría, condiciones iniciales, condiciones de borde y forzantes** .............................. 14

**2.3.1.** **Batimetría** ..................................................................................................................... 14

**2.3.2.** **Meteorología** ................................................................................................................ 16

**2.3.3.** **Marea** ............................................................................................................................ 16

**2.3.4.** **Temperatura, Salinidad y Corrientes** .......................................................................... 16

**2.4.** **Proyectos con descargas en la Bahía de Mejillones del Sur** ............................................. 17

**3.** **Resultados** ................................................................................................................................ 17

**3.1.** **Malla Flexible** ....................................................................................................................... 17

**3.2.** **Modelo Campo Cercano** ...................................................................................................... 18

**3.3.** **Modelo Campo Lejano** ........................................................................................................ 21

**4.** **Discusión y Conclusiones** ....................................................................................................... 40

**5.** **Referencias Bibliográficas** ....................................................................................................... 41

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _ii_

## Índice de Figuras

F IGURA 1. I MAGEN DE G OOGLE E ARTH DE LA B AHÍA DE M EJILLONES DEL S UR, SE INDICA LA

UBICACIÓN DE LAS INSTALACIONES DE E LÉCTRICA A NGAMOS . .................................................. 6

F IGURA 2. U BICACIÓN DE LAS INSTALACIONES DE E LÉCTRICA A NGAMOS EN EL SECTOR DE

ESTUDIO Y DE OTRAS ACTIVIDADES PRODUCTIVAS EN SUS CERCANÍAS . ..................................... 7

F IGURA 3. D OMINIO DE MODELACIÓN DELIMITADO POR LA COSTA Y EL POLÍGONO BLANCO EN

EL ÁREA OCEÁNICA . ............................................................................................................................. 8

F IGURA 4. E SQUEMA DE MODELACIÓN EMPLEADO EN EL ESTUDIO . .................................................. 9

F IGURA 5. R EPRESENTACIÓN DEL FLUJO DE AGUA INCLUYENDO PÉRDIDAS Y GANANCIAS DE

CALOR Y DE SALINIDAD DEL AGUA DE MAR . .................................................................................. 10

F IGURA 6. D ISEÑO DE LAS PORTAS DE CT A NGAMOS . ........................................................................ 11
F IGURA 7. Á REA DE ESTUDIO, LÍNEA DE COSTA Y SONDAS DEL SECTOR COSTERO DE INTERÉS,

CARTA NÁUTICA SHOA N o 1331 EDICIÓN 2011. ........................................................................... 14
F IGURA 8. Á REA DE ESTUDIO, LÍNEA DE COSTA Y SONDAS DEL ÁREA DE INTERÉS, CARTA

NÁUTICA SHOA N o 1300 EDICIÓN 1993. ........................................................................................ 15

F IGURA 9. M ALLA FLEXIBLE IMPLEMENTADA EN EL DOMINIO DE MODELACIÓN Y BATIMETRÍA

INTERPOLADA . .................................................................................................................................... 18

F IGURA 10. P ERFILES PROMEDIO DE TEMPERATURA, SALINIDAD Y CORRIENTES ( MAGNITUD Y

DIRECCIÓN ) EN LA B AHÍA DE M EJILLONES DEL S UR . .................................................................. 19
F IGURA 11. C AMBIO DE LA TEMPERATURA, SALINIDAD Y DENSIDAD DEL AGUA DESCARGADA EN

VERANO E INVIERNO . L ÍNEA DISCONTINUA SE UTILIZA PARA ANALIZAR LOS CAMBIOS A 1 M

DE LAS PORTAS . .................................................................................................................................. 20

F IGURA 12. P LANOS HORIZONTALES DE TEMPERATURA SUPERFICIAL OBTENIDOS EN 4 PVA DE

CT A NGAMOS DURANTE EL AÑO 2014. T OMADOS DE LOS PVA REALIZADOS POR OIKOS. 21

F IGURA 13. S ECCIONES VERTICALES UTILIZADAS EN LOS ANÁLISIS DE LOS RESULTADOS . ............. 23

F IGURA 14. E XCESOS DE TEMPERATURA SUPERFICIAL EN LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN EL CASO 1. ................................................................................................................ 25

F IGURA 15. E XCESOS DE TEMPERATURA SUPERFICIAL EN LOS CASOS 2 Y 3. ..................................... 26

F IGURA 16. E XCESOS DE TEMPERATURA EN EL FONDO EN LA CONDICIÓN APROBADA POR LA

RCA 023/2009 Y EN EL CASO 3. ...................................................................................................... 27

F IGURA 17. E XCESOS DE SALINIDAD SUPERFICIAL EN LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN EL CASO 1. ................................................................................................................ 28

F IGURA 18. E XCESOS DE SALINIDAD SUPERFICIAL EN LOS CASOS 2 Y 3. ............................................ 29

F IGURA 19. E XCESOS DE SALINIDAD DEL FONDO EN LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN EL CASO 3. ................................................................................................................ 30

F IGURA 20. E XCESOS DE TEMPERATURA EN LA SECCIÓN 1 DE LA CONDICIÓN APROBADA POR LA

RCA 023/2009 Y EN LOS TRES CASOS EVALUADOS . ..................................................................... 31

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _iii_

F IGURA 21. E XCESOS DE SALINIDAD EN LA SECCIÓN 1 DE LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN LOS TRES CASOS EVALUADOS . ............................................................................... 32

F IGURA 22. E XCESOS DE TEMPERATURA EN LA SECCIÓN 2 DE LA CONDICIÓN APROBADA POR LA

RCA 023/2009 Y EN LOS TRES CASOS EVALUADOS . ..................................................................... 33

F IGURA 23. E XCESOS DE SALINIDAD EN LA SECCIÓN 2 DE LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN LOS 3 CASOS EVALUADOS . ...................................................................................... 34

F IGURA 24. E XCESOS DE TEMPERATURA EN LA SECCIÓN 3 DE LA CONDICIÓN APROBADA POR LA

RCA 023/2009 Y EN LOS 3 CASOS EVALUADOS . ............................................................................ 35

F IGURA 25. E XCESOS DE SALINIDAD EN LA SECCIÓN 3 DE LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN LOS 3 CASOS EVALUADOS . ...................................................................................... 36

F IGURA 26. E XCESOS DE TEMPERATURA EN LA SECCIÓN 4 DE LA CONDICIÓN APROBADA POR LA

RCA 023/2009 Y EN LOS 3 CASOS EVALUADOS . ............................................................................ 37

F IGURA 27. E XCESOS DE SALINIDAD EN LA SECCIÓN 4 DE LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN LOS 3 CASOS EVALUADOS . ...................................................................................... 38

F IGURA 28. E XCESOS DE TEMPERATURA EN LA SECCIÓN 5 DE LA CONDICIÓN APROBADA POR LA

RCA 023/2009 Y EN LOS 3 CASOS EVALUADOS . ............................................................................ 39

F IGURA 29. E XCESOS DE SALINIDAD EN LA SECCIÓN 5 DE LA CONDICIÓN APROBADA POR LA RCA

023/2009 Y EN LOS 3 CASOS EVALUADOS . ...................................................................................... 40

## Índice de Tablas

T ABLA 1. C ASOS A SER EVALUADOS EN EL ESTUDIO . .............................................................................. 6

T ABLA 2. C ARACTERÍSTICAS DEL DIFUSOR DE CT A NGAMOS . ............................................................ 10

T ABLA 3. I NFORMACIÓN DISPONIBLE PARA FORZAR EL MODELO HIDRODINÁMICO . ...................... 13

T ABLA 4. EIA Y DIA RELACIONADOS CON LAS DESCARGAS Y CAPTACIONES DE CADA PROYECTO

EN LA B AHÍA DE M EJILLONES DEL S UR . ........................................................................................ 17

T ABLA 5. C AUDALES Y SALINIDAD DE LA DESCARGA DE CT A NGAMOS PARA LOS CASOS

CONSIDERADOS EN EL ESTUDIO ...................................................................................................... 19

T ABLA 6. Á REAS CUBIERTAS POR LOS EXCESOS DE 0.1 °C Y 0.1 PSU EN CADA CASO . ....................... 24

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _iv_

**1.** **Introducción**

La Empresa Eléctrica Angamos S.A., solicito la evaluación del cambio del comportamiento de
la pluma térmica-salina de la Central Termoeléctrica Angamos (en adelante CT Angamos) que
se producirá con el incremento de la capacidad de producción de agua desalinizada, y su
interacción (sinergia) con los proyectos en operación y aprobados en el Sistema de Evaluación
Ambiental. Este informe será incluido en la DIA “Ampliación Planta Desalinizadora de agua de
mar, Central Termoeléctrica Angamos.” a ser presentada para la aprobación del proyecto de
incremento de la generación de agua desalada.

Las instalaciones se encuentran en la costa al noreste del Puerto Angamos, el incremento de la
capacidad de producción de agua desalinizada sólo modificara los caudales de captación,
descarga y excesos térmicos y salinos. CT Angamos se encuentra en la Bahía de Mejillones del
Sur (Figura 1) y en sus cercanías existen en operación otras centrales, así como otros proyectos
con descargas térmicas y/o salinas, siendo el más cercano es el proyecto Central Termoeléctrica
Cochrane (en adelante CT Cochrane), de la Empresa Eléctrica Cochrane SpA.

En este estudio se evaluará tres opciones de incremento de la producción de agua desalinizada,
las que se compararan con la descarga actualmente autorizada por la RCA 023/2009 de la CT
Angamos (Tabla 1). Para efectos de evaluar el máximo impacto térmico se utiliza como
temperatura de descarga el máximo permitido por la normativa Chilena (DS 90/2000 del
MINSEGPRES, Tabla 4) que es de 30°C, de forma de mantener sólo el efecto del cambio de
caudal y salinidad variable.

_Modelación de la pluma térmica salina de Central Termoeléctrica Angamos, Bahía de Mejillones del Sur._ _5_

**2.** **Metodología**

**2.1.** **Área de estudio**

CT Angamos se ubica al noreste del Puerto Angamos en la Bahía de Mejillones del Sur (Figura
1), estando en sus cercanías (Figura 2) las instalaciones de Eléctrica Cochrane, y GNL Mejillones.
Como la dinámica de la Bahía de Mejillones del Sur está dominada por el proceso de surgencia
costera permanente de la Península de Mejillones y su zona de sombra, se implementó el dominio
de modelación presentado en la Figura 3. De esta manera se incluyen la mayor parte de los
procesos locales de circulación y los efectos de mesoescala sobre el patrón de circulación en el
sector donde están las instalaciones de Eléctrica Angamos.

**Figura 2.** Ubicación de las instalaciones de Eléctrica Angamos en el sector de estudio y de otras
actividades productivas en sus cercanías.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _7_

**Figura 3.** Dominio de modelación delimitado por la costa y el polígono blanco en el área
oceánica.

**2.2.** **Esquema de Modelación**

Para el desarrollo del estudio de modelación se utilizó el esquema de modelación mostrado en
la Figura 4. La primera etapa corresponde al a simulación mediante el modelo Visual Plumes del
campo cercano mediante las características de las descargas y de los campos de temperatura,
salinidad y corriente de la columna de agua en el sector de cada descarga. Con los resultados
obtenidos del modelo Visual Plumes de dilución de la salinidad y la perdida de calor de cada
pluma se realizara la simulación del campo lejano con el modelo MIKE 3 FM utilizando datos

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _8_

de batimetría, meteorología, y condiciones oceanográficas para la evaluación de la dinámica de
cada pluma descargada.

**Figura 4.** Esquema de modelación empleado en el estudio.

**2.2.1.** **Modelación de Campo Cercano**

Para determinar las pérdidas de calor y dilución de la salinidad que se producen al momento de
incorporarse al mar el agua emitida por cada descarga, ya sea por medio de una descarga directa
o a través de un difusor, se utilizó el programa Visual Plumes v1.0 creado por la U.S.
Environmental Protection Agency que incluye el modelo el modelo UM3 (three-dimensional
Update Merge) que es de tipo lagrangiano y simula una descarga por medio de una puerta simple
o de varias puertas sumergidas en función de las características de la descarga y del medio
ambiente (Frick _et al_ 2003). Este modelo caracteriza la hipótesis del área proyectada del
“entrainment” (PAE, en su sigla en inglés projected-area-entrainment, que cuantifica la fuerza
(Rawn _et al_ 1960), tasa en que la masa de la pluma es incorporada a la corriente asumiendo que
la pluma está en un estado estacionario y la formulación lagrangiana implica que sucesivos
elementos siguen la misma trayectoria (Baumgartner _et al_ 1994), sin embargo, tanto el ambiente
como las condiciones de la descarga cambian en el tiempo, entonces se comparan condiciones
en que se alcanza la fase final de la dilución inicial, usualmente el punto de máximo del proceso.

La información que requiere VisualPlume es:

 - **Parámetros físicos del flujo de descarga** : caudal, temperatura y salinidad que es
determinada del análisis del diagrama de flujo de agua de mar (Figura 5) desde su

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _9_

߲ݑ
߲ݐ [൅߲ݑ] ߲ݔ [ଶ] [൅߲ݒݑ] ߲ݕ [൅߲ݓݑ] ߲ݖ

ൌ݂ݒ-- ݃ [߲ߟ]
߲ݔ [െ1] ߩ ଴

ఎ

ߩ ଴ ׬ ௭ [߲] ߲ݔ [ߩ]

ఎ [ߩ]
݀ݖ
௭ ߲ݔ

߲݌ ௔ ݃
߲ݔ [െ] ఎ

െ [1]
ߩ ଴ ݄ [ቆ߲ܵ] ߲ݔ [௫௫] [൅߲ܵ] ߲ݕ [௫][௬] ~~[ቇ]~~ [൅ܨ] [௨]

߲ݑ
൅ [߲]
߲ݖ [൬ߥ] [௧] ߲ݖ [൅ݑ] [௦] [ܵ൰]

߲ݒ
߲ݐ [൅߲ݑݒ] ߲ݔ [൅߲ݒ] ߲ݕ [ଶ] [൅߲ݓݒ] ߲ݖ

ൌെ݂ݑ-- ݃ [߲ߟ]
߲ݕ [െ1] ߩ ଴

߲ݒ
൅ [߲]
߲ݖ [൬ߥ] [௧] ߲ݖ [൅ݒ] [௦] [ܵ൰]

߲݌ ௔ ݃
߲ݕ [െ] ఎ

ఎ

ߩ ଴ ׬ ௭ [߲][ߩ]
߲ݕ

ఎ [ߩ]
݀ݖ
௭

െ [1]
ߩ ଴ ݄ [ቆ߲ܵ] ߲ݔ [௬][௫] [൅߲ܵ] ߲ݕ [௬௬] [ቇ൅ܨ] [௩]

donde t es el tiempo; x, y, z son las coordenadas cartesianas; η es la elevación de la superficie; h
es la profundidad total; d = h-η; _u_, _v_ y _w_ son las componentes de la velocidad en las direcciones
x, y, z; ݂ൌ2Ω sin ߶ es el parámetro de Coriolis (Ω es la velocidad angular de rotación de la
Tierra, y ߶ es la latitud); _g_ es la aceleración de gravedad; ߩ es la densidad del agua; _S_ _xx_ _, S_ _xy_ _, S_ _yx,_ y
_S_ _yy_ son las componentes del tensor de estrés; ν _t_ es la viscosidad turbulenta vertical; _p_ a es la presión

atmosférica; ߩ ଴ es la densidad de referencia del agua; _S_ es la magnitud de la descarga de los
emisarios y _u_ _s_ _, v_ _s_ es la velocidad del agua descargada; _F_ _u_ y _F_ _v_ son los términos de estrés horizontal.

El transporte y difusión de temperatura ( _T_ ) y salinidad ( _s_ ) está dado por las ecuaciones:

߲ܶ ߲ܶ
߲ݐ [൅߲ݑܶ] ߲ݔ [൅߲ݒܶ] ߲ݕ [൅߲ݓܶ] ߲ݖ [ൌܨ] [்] [൅߲] ߲ݖ [൬ܦ] [௩] ߲ݖ ~~[൰]~~ [൅ܪ෡൅ܶ] [௦] [ܵ]

߲ݏ ߲ݏ
߲ݐ [൅߲ݑݏ] ߲ݔ [൅߲ݒݏ] ߲ݕ [൅߲ݓݏ] ߲ݖ [ൌܨ] [௦] [൅߲] ߲ݖ [൬ܦ] [௩] ߲ݖ ~~[൰]~~ [൅ݏ] [௦] [ܵ]

donde _D_ _v_ es el coeficiente vertical de difusión turbulenta, ܪ [෡] es el intercambio de calor con la

atmósfera, _T_ _s_ y _S_ _s_ son la temperatura y salinidad de las descargas. _F_ _t_ y _F_ _s_ son los términos de
difusión turbulenta de temperatura y salinidad. La turbulencia es modelada utilizando un
esquema de clausura, y la viscosidad vertical es calculada por la expresión:

ݖ൅݀
ߥ ௧ ൌܷ ఛ ଵ ݄ ൅ܿ ଶ ൬ [ݖ൅݀] ݄ ~~൰~~
݄ቆܿ

ଶ ቇ

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _12_

**2.3.** **Batimetría, condiciones iniciales, condiciones de borde y forzantes**

**2.3.1.** **Batimetría**

La información batimétrica para caracterizar el dominio de modelación fue obtenida desde las
cartas náuticas del SHOA del área de estudio (Figura 7 y 8). Esta información se obtuvo mediante
digitalización de las sondas de las cartas náuticas BlueChart g2 de Garmin (HSA002R - South
America West Coast).

**Figura 7.** Área de estudio, línea de costa y sondas del sector costero de interés, carta náutica
SHOA No1331 edición 2011.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _14_

**Figura 8.** Área de estudio, línea de costa y sondas del área de interés, carta náutica SHOA
No1300 edición 1993.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _15_

**2.3.2.** **Meteorología**

Para inicializar y forzar el modelo se utilizó las salidas cada 6 horas del modelo Global Forecast
System (GFS) producido por National Centers for Environmental Predcition (NCEP)
perteneciente a National Oceanic and Atmospheric Administration (NOAA) del gobierno de
Estados Unidos. Los resultados de este modelo son utilizados para inicializar y forzar modelos
como el WRF que es utilizado en Chile por la Dirección Meteorológica de Chile para la
obtención de los pronósticos del tiempo.

De los archivos del modo de ejecución hindcasting del modelo GFS se obtuvieron los datos
cada seis horas de las variables utilizadas son: viento (magnitud y dirección), presión atmosférica,
temperatura del aire y humedad relativa, y mediante interpolación son traspasados a la malla de
simulación en su respectivo tiempo.

**2.3.3.** **Marea**

Del modelo global de mareas TPXO (Egbert y Erofeeva, 2002) se obtuvo para cada uno de los

nodos de la malla a intervalos de una hora la información de marea referida al nivel medio del

mar. Como la información batimétrica está referida al nivel de reducción de sonda (NRS) en el
modelo al momento de su ejecución se le incrementa la diferencia entre el NRS y el nivel medio
del mar, de esta manera las variaciones de la superficie libre (marea) quedaron referidas al nivel

medio del mar.

**2.3.4.** **Temperatura, Salinidad y Corrientes**

Las condiciones iniciales tridimensionales y forzantes (bidimensionales) en las fronteras abiertas
se generaron mediante la interpolación de las condiciones promedio diarias de temperatura,
salinidad y corrientes por medio de los datos obtenidos del modelo regional HYCOM. Este
modelo es producido por un consorcio multi-institucional financiado por NOPP (National
Ocean Partnership Program) como parte del GODAE (US Global Ocean Data Assimilation
Experiment).

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _16_

**Figura 9.** Malla flexible implementada en el dominio de modelación y batimetría interpolada.

**3.2.** **Modelo Campo Cercano**

Como se indicó en la metodología el modelo UM3 (incorporado en el programa Visual Plumes)
requiere las características del emisario como del medio ambiente, en este caso se consideraron
las descargas actualmente autorizadas ambientalmente por RCA 023/2009 de CT Angamos, y
de los proyectos activos en la Bahía de Mejillones, así como de aquellos proyectos que tienen
una RCA. En este estudio la configuración del difusor de la CT Angamos no se modifica y la
temperatura de la descarga se consideró a 30°C que corresponde al máximo que permite la
normativa chilena. Las diferencias entre cada caso están asociadas al caudal y salinidad de la
descarga (Tabla 5).

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _18_

**3.3.** **Modelo Campo Lejano**

Los patrones de circulación y de los parámetros térmicos y salinos durante la mayor parte del
año son muy parecidos como lo muestran los resultados de los PVA (Figura 12 e informes PVA
realizados por OIKOS durante el 2014) que CT Angamos realiza en función de su RCA. En los
resultados de los PVA se aprecia que la pluma térmica de la descarga de CT Angamos es
consistente en el tiempo con un flujo hacia el Puerto Angamos.

Una condición similar respecto a las variaciones térmicas y salinas en la Bahía de Mejillones se
observa en los datos de HYCOM utilizados para inicializar y forzar el modelo. Las condiciones
meteorológicas obtenidas del modelo GFS también muestran una condición muy similar durante
todo el año, lo mismo se obtiene de la revisión de los datos entregados por distintos proyectos
en sus líneas base meteorológicas en DIAs y EIAs (ver EIA de KELAR, DIAs e EIAs
presentados por E-CL, y DIAs y EIAs presentado por las Eléctrica Angamos y Eléctrica
Cochrane, estas últimas empresas del grupo AES Gener).

14 Enero 2014 24 Abril 2014

8 Julio 2014 23 Octubre 2014

**Figura 12.** Planos horizontales de temperatura superficial obtenidos en 4 PVA de CT Angamos
durante el año 2014. Tomados de los PVA realizados por OIKOS.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _21_

Las mediciones de corrientes muestran en el sector de estudio un flujo neto al SW paralelo a la
costa, hacia el pueblo de Mejillones, y los registros de viento históricos [2] indican la dominancia
de viento del S y SSE, y bajas intensidades. Condiciones que difieren de lo observado en la zona
marítima de la Península de Mejillones donde predominan los vientos del SW con intensidades
más altas y corrientes que al norte y que de acuerdo a los pulsos de la surgencia se produce la
rotación de las corrientes hacia el noroeste produciendo remolinos y filamentos típicos de las
zonas de surgencia costera permanentes.

Las simulaciones se realizaron para los dos períodos estudiados en las la Línea Base marina
correspondientes a los periodos estival e invernal del año 2014, con el objetivo de analizar los
patrones de circulación y las variaciones espacio-temporales de la pluma de la situación aprobada
por la RCA 023/2009 de la descarga de CT Angamos, y los cambios producidos en cada uno de
los casos. En total se realizaron 10 simulaciones, 5 para cada periodo de mediciones, consistentes
en una basal, en la cual no hay descargas y que se utiliza como nivel de referencia para el cálculo
de los excesos en la situación aprobada por la RCA 023/2009 y en los 3 casos de incrementó de
la producción de agua desalinizada, y que respecto a la descarga significa cambios en los caudales
descargados y en el exceso de salinidad producido por la purga del sistema de desalinización
(Tabla 1).

En el proceso de post-procesamiento de los resultados de las simulaciones para ver primero las
diferencias entre los dos períodos de estudio como las variaciones diarias y sinópticas, se
confirmó lo observado en los PVA, en los cuales aún no estaba en operación la descarga y
captación de CT Cochrane que introducirá una sinergia con CT Angamos al momento que
empiece su operación.

Por otra parte las principales diferencias entre la situación aprobada por la RCA 023/2009 y los
casos considerados son los caudales y salinidades de la descarga de la central, que ya en el análisis
del campo cercano mostraba que los efectos de las variaciones en la descarga sólo producen un
cambio en el exceso de salinidad en relación con la condición aprobada por la RCA 023/2009,
en los tres casos los excesos de salinidad son más altos, pero similares entre ellos.

Temporalmente en cada periodo sólo se presenta una situación ya que como se indicó
previamente al no estar expuesto el sector directamente a los cambios sinópticos del proceso de
surgencia no se presentan diferencias marcadas en el comportamiento de la pluma como en otras
zonas del país.

Los resultados que se presentan a continuación son de excesos de temperatura y salinidad en
superficie y en el fondo. Hay que indicar que el fondo del sector de estudio es bastante

2 Información obtenida de la revisión de los informes de Líneas de Base marinas de los proyectos E-CL, KELAR, Luz Minera
disponibles en el sitio www.sea.gob.cl

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _22_

homogéneo en su cambio en profundidad desde la orilla hacia el centro de la Bahía, no
presentando elementos topográficos que modifique las corrientes. Además de estos planos
horizontales se presentan los excesos en 6 secciones verticales, tres de ellas paralelas a la orilla y
tres perpendiculares a esta (Figura 13).

**Figura 13.** Secciones verticales utilizadas en los análisis de los resultados.

Los resultados obtenidos en estas simulaciones utilizando la descarga mediante una fuente del
tipo jet, es decir que produce la descarga de acuerdo con el diámetro de cada porta, ángulo de la
porta respeto al norte y el ángulo vertical de la elevación han permitido una representación más
realista de cada una de las plumas. Esto se refleja en que en las cercanías al difusor la pluma no
refleja cambios en la dirección de la pluma; recién cuando el patrón de circulación del sector
predomina por sobre el patrón del flujos generado por la descarga en cada porta, se observan
leves cambios debido a que las condiciones oceanográficas en el sector son relativamente
contante en el tiempo.

Los excesos de temperatura superficial en la condición aprobada por la RCA 023/2009 (Figura
14) presentó un exceso de temperatura de 2,00°C en el sector de los difusores, mientras que en
el caso 3 (Figura 15) dicho máximo se redujo a 1,26°C, cambio que está asociado a la reducción
del caudal de descarga desde los 4500 m [3] /h a los 3954 m [3] /h del caso 3, y a un incremento de la

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _23_

**Figura 14.** Excesos de temperatura superficial en la condición aprobada por la RCA 023/2009

y en el caso 1.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _25_

**Figura 15.** Excesos de temperatura superficial en los casos 2 y 3.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _26_

**Figura 16.** Excesos de temperatura en el fondo en la condición aprobada por la RCA 023/2009
y en el caso 3.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _27_

**Figura 17.** Excesos de salinidad superficial en la condición aprobada por la RCA 023/2009 y en
el caso 1.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _28_

**Figura 18.** Excesos de salinidad superficial en los casos 2 y 3.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _29_

**Figura 19.** Excesos de salinidad del fondo en la condición aprobada por la RCA 023/2009 y en
el caso 3.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _30_

Las secciones verticales de excesos de temperatura y salinidad en los casos aprobada por la RCA
023/2009 y los 3 casos evaluados (Figuras 20 a 29) muestran que en las secciones paralelas a la

costa los excesos de temperatura y salinidad se concentran en la capa superficial de la columna de

agua. En el caso de la sección 1 el espesor de la pluma se aproximadamente del primer metro de la

columna de agua, en las otras dos secciones paralelas a la costa los excesos se concentran

aproximadamente hasta 2 m de profundidad en la columna de agua, bajo esta profundidad los

excesos se reducen bajo los 0,05°C que es menor a la variabilidad ambiental. En estas tres secciones

paralelas los excesos se ubican desde la descarga combinada de la CT Angamos y CT Cochrane hacia

el Puerto de Angamos. En las secciones perpendiculares a la orilla se observa que el exceso de 0,01

ya sea de temperatura o salinidad se encuentra hasta unos 250 m aproximadamente de la orilla en

la sección 4. En la sección 5 en el caso 3 se ve un leve exceso de temperatura y salinidad, en las otras

simulaciones no se aprecian los excesos. La sección 6 no se muestra por no mostrar la influencia de

la CT Angamos lo que es concordante con el patrón de las corrientes y el ángulo respecto al norte

de las portas del difusor.

**Figura 20.** Excesos de temperatura en la sección 1 de la condición aprobada por la RCA
023/2009 y en los tres casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _31_

**Figura 21.** Excesos de salinidad en la sección 1 de la condición aprobada por la RCA 023/2009
y en los tres casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _32_

**Figura 22.** Excesos de temperatura en la sección 2 de la condición aprobada por la RCA
023/2009 y en los tres casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _33_

**Figura 23.** Excesos de salinidad en la sección 2 de la condición aprobada por la RCA 023/2009
y en los 3 casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _34_

**Figura 24.** Excesos de temperatura en la sección 3 de la condición aprobada por la RCA
023/2009 y en los 3 casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _35_

**Figura 25.** Excesos de salinidad en la sección 3 de la condición aprobada por la RCA 023/2009
y en los 3 casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _36_

**Figura 26.** Excesos de temperatura en la sección 4 de la condición aprobada por la RCA
023/2009 y en los 3 casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _37_

**Figura 27.** Excesos de salinidad en la sección 4 de la condición aprobada por la RCA 023/2009
y en los 3 casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _38_

**Figura 28.** Excesos de temperatura en la sección 5 de la condición aprobada por la RCA
023/2009 y en los 3 casos evaluados.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _39_

**Figura 29.** Excesos de salinidad en la sección 5 de la condición aprobada por la RCA 023/2009
y en los 3 casos evaluados.

Los resultados obtenidos en las simulaciones del periodo invernal son similares con leves
diferencias, por lo que no han sido presentados en este informe, ya que no aportan información

.
distinta a la ya entregada

**4.** **Discusión y Conclusiones**

Los resultados obtenidos en estas simulaciones son consistentes con lo ya se ha demostrado en
otros estudios sobre el comportamiento de plumas térmicas y/o salinas en la Bahía de Mejillones
del Sur al Sistema de Evaluación Ambiental en los últimos años (por ejemplo EIA de Kelar, y
EIA de Luz Minera (información disponible en el Sistema de Evaluación Ambiental
www.sea.gob).

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _40_

Como se puede concluir de la Tabla 6 el área de influencia definida por el exceso de 0,1°C
muestra leves cambios producto de las variaciones de caudal entre los casos, mientras que el área
de influencia definida por el exceso de 0,1 psu muestra que entre el caso RCA 023/2009 y los
otros tres caso el área se duplica, y que hay un incremento del área desde 204.084 m2 en el caso
1 a 241,684 m2 en el caso 3, lo que corresponde a un 12% de incremento del área entre ambos

casos.

Al comparar los excesos de temperatura obtenidos en la configuración aprobada por la RCA
023/2009 (Figura 14) con los resultados de temperatura superficial obtenidos en los PVA (Figura
12) se observa que esta simulación muestra el mismo comportamiento de la pluma que se obtuvo
en los PVA, con diferencias que están asociadas a la resolución utilizada en cada una de las grillas
de muestreo de la columna de agua en los PVA.

En relación al efecto de la descarga de CT Angamos producto del incremento de la producción
de agua desalinizada y que significara un incremento del caudal de rechazo y de la salinidad de la
planta RO, que finalmente se descargará por el emisario submarino existente el cual no ha
modificado su configuración aprobada por la RCA 023/2009 del difusor y se mantiene un
máximo de temperatura en la descarga de 30° C, se puede indicar debido a las condiciones
ambientales y del difusor en uso que cuenta con 20 portas con orientación paralela a la orilla en
el sentido de la corriente y con un ángulo vertical que favorece la mezcla turbulenta reduciendo
en forma significativa los excesos de salinidad y temperatura Lo que se aprecia claramente en los
resultados presentados.

En conclusión este estudio indica que cualquiera de las opciones planteadas en la DIA no
producirán efectos adversos al medio marino debido a que los excesos que se generaran serán
superficiales y no exceden la variabilidad propia del medio, con la excepción en las cercanías de
las portas cuando recién sale el chorro de agua desde el difusor. Alteraciones que tampoco
generaran sinergia con otros proyectos activos o con RCA aprobados en el sector.

**5.** **Referencias Bibliográficas**

Baumgartner DJ, WE Frick, CG FOX. 1994. Improved prediction of bending plumes, Journal
of Hydraulic Research 32(6).

Egbert, GD, SY Erofeeva. 2002. Efficient Inverse Modeling of Barotropic Ocean Tides _. J._
_Atmos. Oceanic Technol._, 19, 183-204. doi: http://dx.doi.org/10.1175/15200426(2002)019<0183:EIMOBO>2.0.CO;

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _41_

Escribano, R, S Rosales, JL Blanco. 2004. Understanding upwelling circulation off Antofagasta
(northern Chile): A three-dimensional numerical-modeling approach. _Continental Shelf_

_Research_ : 24: 37-53.

Frick, WE, PJW Roberts, LR Davis, J Keyes, DJ Baumgartner, KP George. 2003. Dilution
models for effluent discharges. 4 [th] Edition (Visual Plumes). Ecosystems Research
Division, NERL, ORD. US Environmental Protection Agency. 960 College Station
Road, Athens Georgia 30605-2700.

Marín, VH, LE Delgado, R Escribano, 2003. Upwelling shadows at Mejillones Bay (northern
Chilean coast): a remote sensing _in situ_ analysis. _Invest. Mar. Valapraiso_, 31(2):47-55

OIKOS CHILE SA. 2014. Programa de vigilancia ambiental Central Termoeléctrica Angamos.
Fase Operación. Monitoreo Mensual 11. 32 pp.

OIKOS CHILE SA. 2014. Programa de vigilancia ambiental Central Termoeléctrica Angamos.
Fase Operación. Monitoreo Mensual 12. 33 pp.

OIKOS CHILE SA. 2014. Monitoreo julio 2014 programa de vigilancia ambiental Central
Termoeléctrica Angamos. Fase Operación. 30 pp.

OIKOS CHILE SA. 2014. Monitoreo octubre 2014 programa de vigilancia ambiental Fase
Operación Central Termoeléctrica Angamos. 156 pp.

Smagorisky. 1963. General circulation experimental with primitive equations. _Monthly weather_
_review_ 91(3):99-164.

_Modelación de la pluma térmica salina de Eléctrica Angamos, Bahía de Mejillones del Sur._ _42_