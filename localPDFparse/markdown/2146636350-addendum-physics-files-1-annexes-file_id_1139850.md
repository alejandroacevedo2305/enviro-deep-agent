---
title: Sin título
author: Aldo Hernández
date: D:20201211110830-03'00'
language: es
type: report
pages: 43
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Estudio de dinámica costera y modelación de la pluma de descarga
-->

# Estudio de dinámica costera y modelación de la pluma de descarga

## Sección I

### Respuesta a observaciones 5.7a y 5.7b ICSARA I Proyecto “Ampliación Planta Procesadora de Algas Marinas”

**Requirente: Algas Marinas S.A.**

Concepción, noviembre de 2020

**EQUIPO DE TRABAJO**

**Aldo Hernández** Jefe de Proyecto

Dinámica costera y
**Daniela Henríquez**

Modelación

Biólogo Marino
Dr(c). Manejo Recursos

Acuáticos Renovables

Biólogo Marino
MSc. en Oceanografía

_Coordinación general_
_Modelación Visual Plumes_

_Revisión y edición informe_

_Análisis de corrientes_

_Modelación OpenFOAM_

_Elaboración de informe_

Biólogo Marino
**Nicolás Muñoz** Modelación _Modelación OpenFOAM_
MSc. en Pesquerías

Holon SpA. 2020. Estudio de dinámica costera y modelación de la pluma de descarga. Sección I:

Respuesta a observaciones 5.7a y 5.7b ICSARA I. Proyecto “Ampliación Planta Procesadora de

Algas Marinas”. 39 pp + Anexos.

i

**TABLA DE CONTENIDO**

**1** **INTRODUCCIÓN ................................................................................................................... 1**

**2** **OBJETIVO ............................................................................................................................ 3**

**3** **MATERIALES Y MÉTODO ................................................................................................... 3**

3.1 I NFORMACIÓN DE CAMPO ................................................................................................................. 3

3.1.1 Diseño de muestreo y área de estudio ............................................................................................. 4

3.1.2 Procesamiento de datos y análisis de la información ....................................................................... 6

3.2 M ODELACIÓN DE LA DESCARGA ........................................................................................................ 6

3.2.1 Data de entrada a la modelación ...................................................................................................... 6

3.2.2 Modelación mediante Visual Plumes ................................................................................................ 8

3.2.3 Modelación mediante OpenFOAM .................................................................................................... 9

3.3 D ETERMINACIÓN DEL ÁREA DE INFLUENCIA ..................................................................................... 12

**4** **RESULTADOS .................................................................................................................... 13**

4.1 I NFORMACIÓN DE CAMPO ............................................................................................................... 13

4.2 M ODELACIÓN DE LA DESCARGA ...................................................................................................... 20

4.2.1 Modelación mediante Visual Plumes .............................................................................................. 20

4.2.2 Modelación mediante OpenFOAM .................................................................................................. 25

4.3 D ETERMINACIÓN DEL ÁREA DE INFLUENCIA ..................................................................................... 33

**5** **CONCLUSIONES ................................................................................................................ 36**

**6** **REFERENCIAS ................................................................................................................... 38**

**7** **ANEXOS ............................................................................................................................. 39**

7.1 A NEXO I. P ERMISO SHOA PARA INSTALACIÓN DE CORRENTÓMETROS EN B AHÍA A NCUD . ................. 40

ii

**1** **INTRODUCCIÓN**

La modelación de las descargas ambientales representa una clase de diseños orientados a

determinar el grado de dilución de un efluente, cerca del punto de descarga (Lee & Chu, 2003).

La densidad del efluente determina el comportamiento de la pluma de la descarga, pudiendo ser

positiva, cuando la densidad del efluente es menor que la densidad de la columna de agua en la

zona de descarga, o negativa, cuando la densidad de la descarga es mayor a la del ambiente

(Inan, 2018).

La hidrodinámica de un efluente que se descarga continuamente en un cuerpo de agua receptor

puede conceptualizarse como un proceso de mezcla que ocurre en dos regiones separadas. En

la primera región, las características iniciales del chorro de flujo de momento, flujo de flotabilidad

y geometría de descarga influyen en la trayectoria y la mezcla del chorro. Esta región se denomina

"campo cercano" y abarca el flujo de chorro flotante y cualquier interacción de la superficie, el

fondo o la capa terminal. A medida que la pluma turbulenta se aleja más de la fuente, las

características de la descarga se vuelven menos importantes, haciendo que las condiciones

advectivas del entorno controlen la trayectoria y la dilución de la columna turbulenta, a través de

movimientos de propagación flotantes y difusión pasiva, o "campo lejano" (Dokener & Jirka,

2007).

Una comprensión integral de los procesos de mezcla inicial hidrodinámica, incluidas las

interacciones de borde de las aguas residuales, es un requisito relevante para controlar las

descargas de aguas residuales y minimizar el impacto en el medio ambiente acuático. Las

investigaciones orientadas mejorar la comprensión del comportamiento de mezcla inicial de las

descargas de efluentes a través de estudios experimentales, han conducido al desarrollo de

modelos matemáticos semiempíricos, tales como Visual Plumes (Frick et al. 2003) VISJET

(Cheung et al. 2000) y CORMIX (Jirka et al. 1996). Estos modelos (denominados modelos de

plumas) predicen las trayectorias de la columna de estado estable hasta la finalización de la

dilución inicial cerca de la profundidad de atrapamiento de la pluma o cuando la pluma llega a la

superficie, con base en la simplificación analítica de fenómenos de mezcla turbulentos complejos,

y no siempre pueden proporcionar detalles de la hidrodinámica tridimensional en la zona de

mezcla inicial (Tang et al. 2008).

1

Alternativamente, los modelos basados en dinámica de fluidos computacional (CFD por sus siglas

en inglés) tienen el potencial de mejorar las deficiencias inherentes de los modelos de plumas.

La dinámica de fluidos computacional (CFD) es una rama de la mecánica de fluidos que utiliza

análisis numérico y estructuras de datos para analizar y resolver problemas que involucran flujos

de fluidos compresibles e incompresibles, permitiendo simular el flujo libre del fluido y su

interacción con las superficies definidas por las condiciones de contorno o de borde (Rapp, 2017).

Una forma de generar aproximaciones realistas para un dominio espacial acotado es el uso del

método de volumen finito (FVM), el cual es un enfoque común utilizado en CFD, ya que posee

ventajas en el uso de la memoria y velocidad de la solución, especialmente para grandes

problemas, flujos turbulentos y combinaciones de diferentes tipos de fluidos (Blazek, 2015). En el

método de volumen finito, las ecuaciones diferenciales parciales que gobiernan (por lo general,

las ecuaciones de Navier-Stokes, las ecuaciones de conservación de masa y energía y las

ecuaciones de turbulencia) se reformulan de forma conservadora y luego se resuelven sobre

volúmenes de control discretos. Esta discretización garantiza la conservación de los flujos a

través de un volumen de control particular (Tang et al. 2008).

Con base en estas consideraciones, para el caso de la modelación de la pluma de descarga del

emisario de Algas Marinas S.A, se ha considerado adecuado el empleo de dos tipos de modelos

para la modelación de la pluma de descarga del efluente: Visual Plumes (Frick et al. 2005) y,

alternativamente, el empleo de modelos CFD utilizando la plataforma de código abierto

[OpenFOAM (https://www.openfoam.com).](https://www.openfoam.com/)

Los resultados del estudio de modelación han sido desarrollados en el marco de la primera

Adenda de la DIA del Proyecto “Ampliación Planta Procesadora Algas Marinas”, presentada al

SEIA por Algas Marinas S.A.

El análisis que se entrega se encuentra orientado a dar respuesta a las observaciones formuladas

por la autoridad ambiental en el ICSARA I, específicamente en los puntos 5.7a) y 5.7b), los que

dicen relación con la entrega de los datos crudos y procesados utilizados en la modelación (5.7a)

y con la incorporación de escenarios de fases lunares de cuadratura y sicigia para las mareas

llenante y variante en la modelación (5.7b). Para dar respuesta a estas observaciones, en el

presente informe se hace entrega del Anexo Digital “ **Base de datos.zip** ” que incluye las bases

de datos crudas y de entrada al modelo y, adicionalmente, se incorpora en la modelación los

escenarios de mareas vaciante y llenante, en cada fase lunar de cuadratura y sicigia,

2

independientemente, generándose 4 escenarios de entrada para los modelos de plumas de

dispersión.

**2** **OBJETIVO**

Evaluar el comportamiento de la pluma de descarga del emisario de Algas Marinas S.A., mediante

la aplicación de herramientas numéricas e información de campo, que permitan dar respuesta a

las observaciones planteadas por la autoridad ambiental, bajo escenarios de marea llenante y

vaciante en fase lunar de cuadratura y sicigia, y determinar el área de influencia de la descarga.

**3** **MATERIALES Y MÉTODO**

3.1 Información de campo

La información de campo asociada a la dinámica de corrientes fue obtenida por correntometría

euleriana, la cual fue determinada mediante la instalación de una línea de correntómetros

electromecánicos dispuestos cada 2 metros. Para evaluar el efecto de las mareas sobre las

corrientes costeras en el área de estudio, se obtuvo información de la base de datos del SHOA

[(https://www.shoa.cl/php/mareas.php) para el Puerto Ancud.](https://www.shoa.cl/php/mareas.php)

El rango medio de la marea en fase lunar de sicigia y cuadratura se obtuvo a partir de lo indicado

en las Instrucciones Oceanográficas No2 “Método oficial para el cálculo de los valores no

armónicos de la marea” del SHOA [(http://www.shoa.cl/s3/shoa-](http://www.shoa.cl/s3/shoa-cl/descargas/descargas/pub_3202_2da_1999.pdf)

[cl/descargas/descargas/pub_3202_2da_1999.pdf).](http://www.shoa.cl/s3/shoa-cl/descargas/descargas/pub_3202_2da_1999.pdf)

En este caso, se consideraron los días donde se observó condiciones de sicigia (luna nueva y

luna llena) y cuadratura (cuarto menguante y cuarto creciente) ( **Tabla 1** ). La altura de marea

utilizada para la modelación en cada uno de los escenarios corresponde a la altura promedio de

mareas registradas en cada fase lunar.

3

**Tabla 1.** Registro de mareas en fase lunar de sicigia y cuadratura registradas para el periodo de
muestreo.

**Escenario Fase lunar** **Fecha**

Luna nueva 9 de febrero
Sicigia
Luna llena 23 de febrero

Cuadratura [Cuarto men][g][uante 15 de febrero ]

Cuarto creciente 2 de marzo

_3.1.1 Diseño de muestreo y área de estudio_

La dinámica de corrientes fue analizada a partir de mediciones de la velocidad y dirección de las

corrientes locales, utilizando correntómetros electromecánicos de punto fijo, marca Innovex,

modelo Stream 300-DI.

El método consistió en un anclaje con una línea de 4 correntómetros, la cual fue instalada en las

cercanías del sistema de descarga de Algas Marinas S.A. (<200 m), en el sector de

desembocadura del río Pudeto, Bahía de Ancud, Región de Los Lagos ( **Figura 1** ). En el **Anexo I**

se entrega el permiso SHOA que autoriza la instalación de los equipos.

Los correntómetros fueron instalados a profundidades equidistantes, separados cada 2 metros

de profundidad. La posición de instalación del anclaje y la profundidad de cada equipo se detalla

en la **Tabla 2** .

Los registros de velocidad y dirección de las corrientes fueron realizados cada 10 minutos, con

una resolución de velocidad de 0,2 cm/s. El periodo de medición de corrientes cubrió 32 días,

iniciando el 4 febrero y finalizando el 7 de marzo del 2020.

4

**Figura 1.** Ubicación espacial del sistema de instalación de anclajes para la línea de
correntómetros con respecto al punto de descarga de efluentes. Coordenadas en UTM. Datum
WGS84, Huso 18G.

**Tabla 2.** Posición geográfica del anclaje y profundidad de instalación de los equipos de medición
de corrientes.

**Latitud (S)** **Longitud (W)**
**Coordenadas Geográficas**
41o 51' 58,20'' 73o 47' 12,50''

**UTM - N** **UTM - E**
**Coordenadas UTM**
5364371 600684

**Profundidad del equipo**

Correntómetro 1 2 m

Correntómetro 2 4 m

Correntómetro 3 6 m

Correntómetro 4 8 m

Profundidad de la Columna de agua 9 m

5

_3.1.2 Procesamiento de datos y análisis de la información_

Para el análisis de la información, la dirección de las corrientes fue referida al norte

geográfico, mediante la corrección de 9,01oE de desviación magnética local, calculada

utilizando el modelo geo-magnético del Nacional Geophysical Data Center

[(https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml?useFullSite=true).](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml?useFullSite=true)

El análisis estadístico involucró la construcción del componente armónico de mareas y su

contraste con la serie de datos de los correntómetros independientemente. La determinación

de la dependencia entre las mediciones de corrientes y las mareas fue evaluada mediante

un análisis de correlaciones cruzadas. Con la finalidad de determinar las frecuencias

temporales que dominaron en la variabilidad de las series de tiempo de la magnitud de las

corrientes medidas, se realizó un análisis espectral, el cual permite identificar la correlación

de las funciones seno y coseno de diferentes frecuencias observadas en las series de datos.

Para visualizar gráficamente el comportamiento integrado de la velocidad y dirección de las

corrientes, se construyeron diagramas de rosas, los cuales permiten incorporar la dirección

predominante de las corrientes y la frecuencia de las diferentes magnitudes registradas.

Adicionalmente, y con la finalidad de analizar la variabilidad de los componentes perpendiculares

a los vectores de corrientes, se estimó las componentes ortogonales _u_ y _v_, donde _u_ corresponde

a la componente zonal de la velocidad de la corriente (E-W) y _v_ corresponde a la componente

meridional de la velocidad de la corriente (N-S).

A partir de la evaluación integrada de los resultados del análisis estadístico, se pudo determinar

escenarios que explican la variabilidad del cuerpo de agua analizados, los cuales fueron utilizados

como datos de entrada para la modelación de la pluma de descarga.

3.2 Modelación de la descarga

_3.2.1 Data de entrada a la modelación_

Los datos de entrada a la modelación se resumen en las **Tablas 3** a **5** . En las cuales se entregan

las características del sistema de descarga ( **Tabla 3** ) y las características del efluente ( **Tabla 4** ),

considerando como parámetros clave los sólidos suspendidos totales (SST) y los sólidos

sedimentables (SSD), utilizando como concentración de descarga el valor límite de la Tabla 5,

6

del DS 90/2000. En la **Tabla 5** se entregan las características del cuerpo receptor, utilizando como

valores de referencia los valores mínimos observados en las estaciones de monitoreo del

Programa de Vigilancia Ambiental “Sistema de tratamiento y disposición final de RILes del

Proceso de Algas”, para la campaña de muestreo correspondiente al segundo semestre 2019.

Por otro lado, se realizó la estimación de la distancia en la cual la pluma de descarga alcanza las

concentraciones de SST y SSD indicadas en la Tabla 4 del DS 90, a saber: 100 mg/l de SST y 5

ml/l/h para SSD.

Adicionalmente, y con base en los resultados del análisis estadístico de corrientes, se generaron

escenarios que recogen la variabilidad del medio receptor, los que formaron parte de los datos

de entrada a la modelación.

**Tabla 3.** Características del sistema de descarga del efluente utilizadas en la modelación.

**SISTEMA DE DESCARGA**

Número de difusores 1

Diámetro externo
250 mm
difusor

Grosor del tubo 14 mm

Caudal máximo 85 m3/hora

Profundidad emisario 9 m

**Tabla 4.** Características del sistema de efluente utilizadas en la modelación. SST: Sólidos
Suspendidos Totales, SSD: Sólidos Sedimentables.

**EFLUENTE**

Concentración de SST 300 mg/l

Concentración de SSD 20 ml/l/h

Temperatura promedio 12,6 oC

Salinidad promedio 15,8 psu

Densidad promedio 1.011,6 kg/m [3]

7

**Tabla 5.** Características del cuerpo de agua receptor utilizadas en la modelación. SST: Sólidos
Suspendidos Totales, SSD: Sólidos Sedimentables.

**MEDIO RECEPTOR**

Concentración de SST 5 mg/l

Concentración de SSD 0,1 ml/l/h

Temperatura promedio 14,0 oC

Salinidad promedio 31,8 psu

Densidad promedio 1.024,5 kg/m [3 ]

_3.2.2 Modelación mediante Visual Plumes_

Para la modelación inicial de la pluma de descarga se utilizó el programa Visual Plumes (VP)

v1.0, desarrollado la Agencia de Protección Ambiental de Estados Unidos (USEPA). El software

incorpora modelos que tienen la capacidad de simular plumas sumergidas con descargas simples

y con múltiples difusores en un ambiente estratificado, además de descargas boyantes en

superficie, considerando las condiciones ambientales del medio receptor.

En el caso particular de la modelación que se presenta, se utilizó el módulo denominado UM3

(Three Dimensional Update Merge), el cual desarrolla una aproximación de tipo lagrangiana que

simula una descarga por medio de uno o más difusores, en función de las características de la

descarga y del medio ambiente, permitiendo describir el comportamiento de la pluma en términos

de profundidad y en el espacio (Frick et al., 2003).

El modelo UM3 se caracteriza de tres puntos importantes para resolver el comportamiento de la

descarga en el medio receptor:

 Hipótesis del área proyectada del PAE (Projected Area Entrainment), la cual cuantifica la

fuerza (Rawn et al., 1960).

 - Tasa en que la masa de la pluma es incorporada a la corriente, asumiendo que la pluma

se encuentra en estado estacionario y,

 Formulación lagrangiana, que implica que sucesivos elementos siguen la misma

trayectoria (Baumgartner et al., 1994).

8

_3.2.3 Modelación mediante OpenFOAM_

OpenFOAM es un software de código abierto, desarrollado por OpenCFD Ltd desde 2004, que

desarrolla métodos y algoritmos numéricos para resolver y analizar problemas relacionados con

la dinámica de fluidos computacional (CFD), incluyendo flujos de fluidos complejos que involucren

reacciones químicas, turbulencia, transferencia de calor, acústica, mecánica de sólidos y

electromagnetismo.

En caso particular de la modelación que se presenta, se realizó una simulación 3D para fluidos

incompresibles. El modelo generado simula el desarrollo de la capa de mezcla y de la columna

de turbidez, para así determinar el área de impacto, a través de la modelación del campo de

velocidades, a partir de la cual se modela el comportamiento de los parámetros objetivo (SST,

SSD) como una modelación escalar. En términos generales, la aproximación metodológica que

desarrolla OpenFOAM involucra las siguientes etapas:

**Dominio computacional y construcción del** _**mesh (**_ **NMA)**

El dominio de estudio se corresponde a la zona ubicada en torno al punto de descarga del

emisario ( **Figura 2** ), considerando un área de dimensiones de 40 m x 40 m, donde la zona de

descarga (punto rojo) corresponde al centro del dominio. La profundidad de esta área va desde

los 8 m, en el extremo más costero, hasta los 10 m, en la zona más profunda. La descarga se

ubica a una profundidad de 9 m.

9

**Figura 2.** Área geográfica de ubicación del dominio para la modelación de la descarga del
emisario

La construcción de la geometría del dominio se realizó utilizando el software SALOME v9.4.0,

elaborándose un modelo espacial compuesto por 6 capas (Weste, Este, Atmosfera, Océano,

Fondo, Costa) al interior del cual se ubica el ducto de descarga ( **Figura 3** ). La geometría completa

genera la grilla del dominio o “ _mesh_ ” que contiene la topología completa del modelo, que

corresponde a las capas desde donde provienen los flujos que conforman la modelación.

10

**Figura 3.** Estructura general del dominio general de la modelación (arriba) indicando las capas
de la modelación (vista desde la capa Weste) y acercamiento al emisario submarino.

**Solvers o solucionadores**

Etapa donde se selecciona el método empleado para la solución de los escenarios a modelar. El

Método de Volumen Finito (VOF) genera soluciones de ecuaciones algebraicas, mediante un

método iterativo que divide el dominio físico en estudio en subdominios, estableciendo la

generación de mallas. Las ecuaciones son resueltas en cada subdominio (volumen finito) a través

de un conjunto de ecuaciones algebraicas que describen el valor de la variable objetivo en cada

volumen finito.

La interpretación numérica del método descrito se realiza utilizando el solver _interMixingFoam,_ el

cual resuelve ecuaciones para fluidos incompresibles, en base a la interacción de 3 fases:

atmósfera, efluente y medio receptor (simulación 3D).

11

**Condiciones de borde del modelo**

Etapa donde se configuran las propiedades de contorno (a partir del mesh) y las condiciones de

flujo del modelo (en nuestro caso velocidad ortogonal ( _u, v_ ) y presión), así como los directorios

(carpetas) que operan en la modelación, todo lo cual representa la estructura inicial del modelo.

Es importante en esta fase definir cuales con las capas que interactúan en la modelación (desde

donde provienen los flujos a modelar, como las Capas Océano y Este) y cuales no (por ejemplo,

la Capa Fondo) y las condiciones iniciales o de partida del modelo (tiempo 0).

Paralelamente, en nuestro caso, se incluyó como transporte escalar de contaminantes, la

concentración de los dos parámetros a modelar (SST y SSD), lo que implicó introducir

modificaciones en la estructura basal del modelo, incluyendo los solucionadores o solvers

utlizados.

**Visualización de resultados**

Etapa de post-procesamiento, en el cual es posible observar las salidas computacionales de los

escenarios simulados. En este caso se utilizó la herramienta de visualización de alto rendimiento

[ParaView (https://www.paraview.org), software de código abierto que permite explorar las salidas](https://www.paraview.org/)

resultantes de la modelación en OpenFOAM en vistas 3D y que puede ser utilizado mediante

programación o interactivamente con el usuario.

3.3 Determinación del área de influencia

El área de influencia de la pluma de descarga fue determinada a partir de los resultados de la

modelación, y calculada como la superficie radial en la cual se produce la máxima dilución de la

descarga. Para esto se utilizaron los resultados de las plumas máximas (peor escenario)

calculadas para cada parámetro analizado (SST y SSD), independientemente, trazándose un

círculo de radio igual a la longitud de la pluma en la cual se alcanza la concentración de la Tabla

4 del DS 90/2000 y otro círculo de radio igual a la a la longitud de la pluma en la cual se alcanza

la concentración del medio.

Las áreas de influencia estimadas fueron construidas y calculadas en ArcGis v12.0.

12

**4** **RESULTADOS**

4.1 Información de campo

El análisis de la serie de tiempo de mareas ( **Figura 4** ) determinó la presencia de un régimen de

marea semidiurna mixta, con amplitudes que variaron entre 2,5 m y 0,6 m, para pleamar y bajamar

respectivamente.

**Figura 4.** [Serie temporal de mareas durante el periodo de estudio. Puerto Ancud (www.shoa.cl).](http://www.shoa.cl/)
Elaboración propia.

El resultado del análisis de las series temporales para las velocidades de corrientes ( **Figura 5** )

revela una alta variabilidad entre las distintas capas de la columna de agua. Las velocidades

superficiales (estrato 2 m) registraron magnitudes promedio de 20,5 cm s [-1] en promedio. Se

observó un comportamiento similar en las velocidades subsuperficiales (estrato 4 m), con

magnitudes promedio de 19,8 cm s [-1] . En ambos casos, se destaca un peak de máxima

variabilidad en torno a 70 cm s [-1], durante la última semana de febrero, que es coincidente con las

mareas de sicigia (ver **Figuras 4** y **5** ).

La serie de tiempo analizada en el estrato de 6 m de profundidad solo presentó registros entre el

5 y el 8 de febrero, con magnitudes máximas más intensas, que superaron los 100 cm s [-1] .

Finalmente, las corrientes de fondo (estrato 8 m), presentaron una alta variabilidad, con

magnitudes promedio de 25,9 cm s [-1], y máximas que superaron los 70 cm s [-1] .

13

**Figura 5.** Series temporales de velocidades de corrientes durante el periodo de estudio por
estrato (v2m=velocidad en el estrato de 2 m; v4m=velocidad en el estrato de 4 m; v6m=velocidad
en el estrato de 6 m; v8m=velocidad en el estrato de 8 m). Elaboración propia.

Un análisis de correlaciones cruzadas entres las series temporales de mareas y las series de

tiempo de velocidades de corrientes por estrato ( **Figura 6** ) entrega correlaciones significativas

entre la marea y las corrientes medidas, destacando una mayor influencia en el caso de los

estratos de 2 y 4 m. Los datos de corrientes también muestran altas correlaciones entre sí,

particularmente entre estratos colindantes, salvo en el caso del estrato de 8 m, que muestra

correlaciones más bajas con los estratos superficiales (2 y 4 m) y con la marea, lo que revela la

existencia de un cambio en el patrón de velocidades en el estrato más profundo.

14

**Figura 6.** Análisis de correlaciones entre series temporales de marea y de corrientes por estrato.
Elaboración propia.

El análisis espectral de las series temporales de corrientes por estrato ( **Figura 7** ) permite observar

que la mayor densidad espectral registra una oscilación periódica cada 12 y 24 horas, lo cual

indica que la variabilidad de las corrientes a lo largo de la columna de agua se encuentra

principalmente modulada por procesos semidiurnos y mareales. Este patrón fue mas notorio en

las capas superficiales (estratos entre 2 a 4 m).

15

**Figura 7.** Análisis espectral para series temporales de marea por estrato. Elaboración propia.

El patrón general de circulación ( **Figura 8** ) permite observar que las corrientes superficiales

(estrato 2 m), registraron velocidades máximas cercanas a 60 cm s [-1], con una dirección

predominante hacia el SW. Bajo esta profundidad (estrato 4 m), la dirección de las corrientes

tiende a cambiar en sentido SSW, alcanzando valores máximos entre 40 y 60 cm s [-1] . En la capa

de 6 metros, las velocidades aumentan hasta alcanzar niveles superiores a 100 cm s [-1],

manteniendo la dominancia de las corrientes hacia el SSW. En el fondo (estrato 8 m), las

corrientes también registran velocidades altas, con máximos cercanos a 100 cm s [-1], aunque con

una mayor variabilidad y con predominio de velocidades inferiores a 40 cm s [-1] . La dirección

dominante en este estrato es SW.

En general, en los estratos superficiales se registró velocidades más bajas (< 40 cm s [-1] ), con un

predominio de direcciones hacia el SW (2 m) y SSW (4m). En la capa más superficial (2 m), se

16

observó además una menor frecuencia de cambio de dirección en sentido NW. En las capas más

profundas (6 y 8 m) se registró mayor velocidad de corrientes, con predominio de direcciones

SSW (6 m) y SW (8m).

**Figura 8.** Rosa de direcciones de corrientes marinas para estratos de 2, 4, 6 y 8 m de profundidad,
durante el periodo de estudio. Elaboración propia.

El análisis de las series temporales de las componentes zonal (E-W; _u_ ) y meridional (N-S; _v_ ) de

la velocidad de las corrientes ( **Figura 9** ), revela una alta variabilidad a nivel de estratos. En el

estrato superficial (2 m) se observan velocidades máximas superiores a 40 cm s [-1], para la

componente meridional con una dirección predominante hacia el Norte, mientras que para la

componente zonal se registran velocidades máximas cercanas a 60 cm s [-1], en sentido Weste. A

profundidades medias (estrato 4 m), la velocidad de las corrientes tiende a dominar en sentido

SW, alcanzando máximos superiores a 40 cm s [-1] en la componente meridional y máximos

cercanos a 20 cm s [-1] en la componente zonal. A los 6 m de profundidad, la velocidad de las

componentes de las corrientes registra magnitudes superiores a 100 cm s [-1], con una dirección

dominante hacia el SW, donde la componente meridional (N-S) es la dominante. Cerca del fondo

(8 m) las componentes de la corriente presentaron tendencias similares a lo observado en 6 m,

17

aunque con mayor variabilidad, observándose velocidades máximas cercanas a 100 cm s [-1] en

dirección SW.

En general, ambas componentes ( _u, v_ ) presentaron un patrón similar a lo largo de toda la columna

de agua, destacando un mayor dominio de la componente zonal (E-W) en superficie y un mayor

dominio de la componente meridional (N-S) en las capas mas profundas.

**Figura 9.** Serie de tiempo de las componentes zonal ( _u_ ) y meridional ( _v_ ) de la velocidad de la
corriente en niveles 2, 4, 6 y 8 m de profundidad, durante el periodo de estudio. Elaboración
propia.

Con base en estos resultados, considerando que en todos los niveles de la columna de agua se

detectó una fuerte influencia de las mareas, se han incorporado 4 escenarios de corrientes como

datos de entrada a la modelación. El primero, correspondiente un escenario de marea llenante

en fase lunar de sicigia; el segundo considerando un escenario de marea vaciante en fase lunar

de sicigia; el tercero considerando un escenario de marea llenante en fase lunar de cuadratura;

y el cuarto considerando un escenario de marea vaciante en fase lunar de cuadratura ( **Tabla 6** ).

Para la generación de estos escenarios no fue considerado el estrato de 6 m de profundidad,

debido a que el periodo de mediciones de corrientes efectivo fue inferior a 5 días.

18

**Tabla 6.** Escenarios de modelación propuestos para la dinámica de corrientes en la zona de
estudio. Los periodos de sicigia y cuadratura considerados para la generación de los escenarios

|propuestos se entregan en la Tabla 1.|Col2|Col3|
|---|---|---|
|<br> <br>|**Sicigia**|**Cuadratura**|
|**Estrato**<br>**Variable**<br>**Unidad**|**Llenante**<br>**Vaciante**|**Llenante**<br>**Vaciante**|
|2 m<br>Dirección<br>grados-N<br>Velocidad<br>cm/s|112,9<br>243,9<br>18,8<br>35,8|146,5<br>246,0<br>14,6<br>19,6|
|4 m<br>Dirección<br>grados-N<br>Velocidad<br>cm/s|190,3<br>206,3<br>16,4<br>33,1|192,2<br>205,9<br>17,1<br>27,3|
|8 m<br>Dirección<br>grados-N<br>Velocidad<br>cm/s|137,3<br>220,5<br>18,2<br>53,1|255,0<br>212,1<br>6,5<br>6,3|

Los escenarios entregados responden cabalmente a la observación 5.7b) planteada por

Subsecretaría de Pesca y Acuicultura, donde _“... se solicita modelar en escenarios que_

_consideren la marea vaciante y llenante, en cada fase lunar de cuadratura y sicigia..._ ”.

Adicionalmente, adjunto a este informe se hace entrega del Anexo Digital “ **Base de datos.zip** ”,

lo que da respuesta a la observación 5.7a), donde “... _se solicita incorporar los datos crudos y_

_procesados utilizados en la modelación_ ...”.

A partir de la observación de las velocidades y direcciones obtenidas al formular estos escenarios,

es posible detectar mayores velocidades en el escenario vaciante en fase lunar de sicigia, con

máximos de 53,1 cm s [-1] registrados en la capa de 8 metros de profundidad. En cuanto a la

dirección de las corrientes, tanto en la capa superficial (2 metros) como en la capa de fondo (8

metros), se observa un cambio notable de dirección de corrientes en fase lunar de sicigia, siendo

de 112,9o y 137,3o en llenante (dirección ESE y SE respectivamente) y de 243,9o y 220,5o en

vaciante (WSW y SW respectivamente). No obstante, en fase lunar de cuadratura, las direcciones

predominantes de corrientes se orientan en sentido SSE en la capa superficial y SW en la capa

de fondo.

Por otro lado, las direcciones predominantes en la capa de 4 metros se orientan en sentido SW

y SSW, en fase de Sigicia y Cuadratura.

19

4.2 Modelación de la descarga

_4.2.1 Modelación mediante Visual Plumes_

En las **Figuras 10**, **11** y **12** se entrega el resultado de la modelación en Visual Plumes (Modelo

UM3) para SST utilizando como datos de entrada los indicados en las **Tablas 3**, **4**, **5** y **6.** Como

es posible apreciar, en todos los escenarios modelados, la pluma de descarga tiende a

mantenerse bajo los 4 metros de profundidad y en dirección SSW.

En términos generales, la modelación de SST arroja plumas en dirección hacia la costa en todos

los escenarios, destacando en el caso de la modelación en escenario de sicigia llenante, que la

pluma toma una dirección hacia el Sureste, mientras que en los demás escenarios, las

direcciones de las plumas se orientan hacia el Weste y Surweste ( **Figura 10** ). Las longitudes de

las plumas modeladas en cada escenario se indican en la esquina superior derecha de cada una

de las figuras; la pluma de mayor longitud (9 m) se produce en el escenario sicigia vaciante.

a) b)

**4 m** **9 m**

c) d)

**2 m** **2 m**

**Figura 10.** Vista superior (Plan View) resultado de la modelación VISUAL PLUMES UM3 para
SST en 4 escenarios. a) Sicigia-llenante; b) Sicigia-vaciante; c) Cuadratura-llenante; d)
Cuadratura-vaciante. En la esquina superior derecha se entrega la longitud de las plumas en cada
escenario.

20

La vista lateral de las plumas ( **Figura 11** ), permite observar con mayor claridad la longitud de

éstas, observándose además que las plumas modeladas bajo los escenarios de cuadratura

tienden a elevarse en la columna de agua, alcanzando hasta la profundidad de 4 metros, mientras

que las plumas modeladas bajo los escenarios de sicigia permanecen cerca del fondo.

a) b)

**4 m** **9 m**

c) d)

**2 m** **2 m**

**Figura 11.** Vista lateral (Plume Elavation) resultado de la modelación VISUAL PLUMES UM3 para
SST en 4 escenarios. a) Sicigia-llenante; b) Sicigia-vaciante; c) Cuadratura-llenante; d)
Cuadratura-vaciante. En la esquina superior derecha se entrega la longitud de las plumas en cada
escenario.

El análisis de las diluciones ( **Figura 12** ) permite observar que, en todos los escenarios, la dilución

a cuerpo receptor (dilución 60: 300 mg/l en la descarga _vs_ 5 mg/l en el cuerpo receptor) se alcanza

al nivel máximo de la longitud de las plumas, que para SST oscila entre 2 y 9 metros. La dilución

a Tabla 4 del DS90 (dilución 3: 300 mg/l en la descarga _vs_ 100 mg/l en Tabla 4) se alcanza a una

distancia inferior a 1 m desde la descarga en todos los escenarios.

21

a) b)

**4 m** **9 m**

c) d)

**2 m** **2 m**

**Figura 12.** Predicción de la dilución (Plumes Dilution Prediction) resultado de la modelación
VISUAL PLUMES UM3 para SST en 4 escenarios. a) Sicigia-llenante; b) Sicigia-vaciante; c)
Cuadratura-llenante; d) Cuadratura-vaciante. En la esquina superior derecha se entrega la
longitud de las plumas en cada escenario. El punto rojo señala en cada escenario la longitud de
la pluma para la dilución a Tabla 4.

En las **Figuras 13**, **14** y **15** se entrega el resultado de la modelación en Visual Plumes (Modelo

UM3) para SSD, utilizando como datos de entrada los indicados en las **Tablas 3**, **4**, **5** y **6** .

En términos generales, la modelación de SSD arroja plumas en dirección hacia la costa para

todos los escenarios, destacando en el caso de la modelación en escenario de sicigia llenante,

que la pluma se orienta en dirección Sureste, mientras que en los demás escenarios, las

direcciones de las plumas se orientan hacia el Surweste y Sur-Surweste ( **Figura 13** ). Las

longitudes de las plumas modeladas en cada escenario se indican en la esquina superior derecha

de cada una de las figuras, observándose que la pluma de mayor longitud (25 m) se alcanza en

el escenario de sicigia vaciante.

22

a) b)

**14 m** **25 m**

c) d)

**6 m** **7 m**

**Figura 13.** Vista superior (Plan View) resultado de la modelación VISUAL PLUMES UM3 para
SSD en 4 escenarios. a) Sicigia-llenante; b) Sicigia-vaciante; c) Cuadratura-llenante; d)
Cuadratura-vaciante. En la esquina superior derecha se entrega la longitud de las plumas en cada
escenario.

La vista lateral de las plumas ( **Figura 14** ), permite determinar de mejor forma la longitud de éstas,

observándose que las plumas modeladas bajo los escenarios de cuadratura alcanzan hasta los

estratos más superficiales (<2 metros en el caso de cuadratura llenante), mientras que las plumas

modeladas bajo los escenarios de sicigia tienden a permanecer bajo los 4 metros de profundidad.

23

a) b)

**14 m** **25 m**

c) d)

**6 m** **7 m**

**Figura 14.** Vista lateral (Plume Elavation) resultado de la modelación VISUAL PLUMES UM3 para
SSD en 4 escenarios. a) Sicigia-llenante; b) Sicigia-vaciante; c) Cuadratura-llenante; d)
Cuadratura-vaciante. En la esquina superior derecha se entrega la longitud de las plumas en cada
escenario.

El análisis de las diluciones ( **Figura 15** ) permite observar que, en todos los escenarios, las plumas

no alcanzan a llegar a la dilución máxima al cuerpo receptor (dilución 200: 20 mg/l en la descarga

_vs_ 0,1 mg/l en el cuerpo receptor). Para SSD la longitud de las plumas a dilución máxima oscila

entre 6 y 25 metros. La dilución a Tabla 4 del DS90 (dilución 4: 200 mg/l en la descarga _vs_ 50

mg/l en Tabla 4) se alcanza a una distancia inferior a 1 m desde la descarga en todos los

escenarios.

24

a) b)

**14 m** **25 m**

c) d)

**6 m** **7 m**

**Figura 15.** Predicción de la dilución (Plumes Dilution Prediction) resultado de la modelación
VISUAL PLUMES UM3 para SSD en 4 escenarios. a) Sicigia-llenante; b) Sicigia-vaciante; c)
Cuadratura-llenante; d) Cuadratura-vaciante. En la esquina superior derecha se entrega la
longitud de las plumas en cada escenario. El punto rojo señala en cada escenario la longitud de
la pluma para la dilución a Tabla 4.

_4.2.2 Modelación mediante OpenFOAM_

Los resultados de la modelación con OpenFOAM se muestran dos vistas que permiten observar

las características generales de las plumas modeladas: una vista frontal (desde la capa Océano)

y una vista superior (desde la capa Atmósfera, ver **Figura 3** ). En cada caso se señalan los

nombres de las capas visibles, además de la altura y longitud de las plumas resultantes de cada

modelación. La pluma modelada en tonalidades anaranjadas se extiende hasta el momento en el

cual la concentración de la descarga (300 mg/l para SST y 20 ml/l para SSD) se iguala con la

concentraciones establecidas en la Tabla 4 del DS 90 (100 mg/l para SST y 5 ml/l para SSD),

mientras que la pluma de tonos celestes se extiende hasta el momento en el cual la concentración

de la descarga (300 mg/l para SST y 20 ml/l para SSD) se iguala con la concentración del medio

receptor (5 mg/l para SST y 0,1 ml/l para SSD).

25

**Modelación de Sólidos Suspendidos Totales (SST)**

Los resultados de la modelación para SST en fase lunar de sicigia ( **Figuras 16** y **17** ) permiten

observar que, la altura de la pluma de dilución estimada hasta alcanzar la concentración de la

Tabla 4 del DS 90 (100 mg/l) fluctúa entre 0,73 y 0,78 metros desde el fondo, dependiendo del

escenario de corrientes, mientras que la longitud máxima de la pluma oscila entre 0,43 y 0,46

metros. La pluma de dilución estimada hasta alcanzar las concentraciones típicas del medio

receptor (5 mg/l) muestra una altura que fluctúa entre 2,72 y 3,43 metros desde el fondo, con

longitudes que oscilan entre 9,35 y 10,4 metros.

**Figura 16.** Resultado de la modelación OpenFOAM para SST en escenario de marea llenante en
fase lunar de sicigia. Arriba se muestra una vista frontal, desde la capa Océano, y abajo una vista
superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

26

Similar a lo observado en la modelación con Visual Plumes, los resultados revelan que las plumas

tienden a mantenerse cercanas al fondo, observándose que la pluma tiende a cambiar de

dirección entre los escenarios modelados, siendo predominante hacia el SE en marea llenante y

hacia el SW en marea vaciante. La pluma de mayor longitud (10,4 m) se obtuvo en el escenario

Vaciante.

**Figura 17.** Resultado de la modelación OpenFOAM para SST en escenario de marea vaciante
en fase lunar de sicigia. Arriba se muestra una vista frontal, desde la capa Océano, y abajo una
vista superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

En el caso de los escenarios de Cuadratura ( **Figuras 18** y **19** ) es posible observar que la longitud

de la pluma a la dilución de Tabla 4 del DS90 (100 mg/l) oscila entre 1,06 y 0,73 metros. La pluma

27

de dilución estimada hasta alcanzar las concentraciones típicas del medio receptor (5 mg/l)

muestra una altura que fluctúa entre 3,28 y 4,23 metros desde el fondo, con longitudes que oscilan

entre 10,3 y 11,1 metros.

Concordante con lo observado en las modelaciones previas, estos resultados señalan que las

plumas modeladas para SST tienden a mantenerse cercanas al fondo y que, para los escenarios

de Cuadratura, la dirección de la pluma se orienta hacia el SW. La pluma de mayor longitud (11,1

m) se obtuvo en el escenario Vaciante.

**Figura 18.** Resultado de la modelación OpenFOAM para SST en escenario de marea llenante en
fase lunar de cuadratura. Arriba se muestra una vista frontal, desde la capa Océano, y abajo una
vista superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

28

**Figura 19.** Resultado de la modelación OpenFOAM para SST en escenario de marea vaciante
en fase lunar de cuadratura. Arriba se muestra una vista frontal, desde la capa Océano, y abajo
una vista superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

**Modelación de Sólidos Sedimentables (SSD)**

Los resultados de la modelación para SSD en fase lunar de sicigia ( **Figuras 20** y **21** ) permiten

observar que la altura de la pluma de dilución estimada hasta alcanzar la concentración de la

Tabla 4 del DS 90 (5 ml/l/h) fluctúa entre 0,84 y 0,91 metros desde el fondo, mientras que la

longitud de la pluma oscila entre 0,83 y 1,07 metros. La pluma de dilución que alcanza las

concentraciones típicas del medio receptor (0,1 ml/l/h) muestra una altura que fluctúa entre 4,41

y 5,23 metros desde el fondo, con longitudes que oscilan entre 15,4 y 15,5 metros. Del mismo

modo, estos resultados señalan que las plumas tienden a mantenerse en el fondo y que, la pluma

29

cambia de dirección dependiendo de la marea, siendo predominante hacia el Sureste en marea

llenante y hacia el Sur-Surweste en marea vaciante. La pluma de mayor longitud (15,5 m) se

obtuvo en el escenario Llenante, aunque fue levemente superior a lo observado en marea

vaciante, aunque su longitud es muy cercana a la observada en llenante.

**Figura 20.** Resultado de la modelación OpenFOAM para SSD en escenario de marea llenante
en fase lunar de sicigia. Arriba se muestra una vista frontal, desde la capa Océano, y abajo una
vista superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

30

**Figura 21.** Resultado de la modelación OpenFOAM para SSD en escenario de marea vaciante
en fase lunar de sicigia. Arriba se muestra una vista frontal, desde la capa Océano, y abajo una
vista superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

Los resultados de la modelación de SSD en fase lunar de cuadratura ( **Figuras 22** y **23** ) permiten

observar que la altura de la pluma de dilución estimada hasta alcanzar la concentración de la

Tabla 4 del DS 90 (5 ml/l/h) fluctúa entre 0,31 y 0,65 metros desde el fondo, mientras que la

longitud de la pluma oscila entre 0,96 y 1,79 metros. La pluma de dilución que alcanza las

concentraciones típicas del medio receptor (0,1 ml/l/h) muestra una altura se eleva hasta los 5,16

y 5,63 metros desde el fondo, con longitudes máximas que oscilan entre 18,2 y 18,8 metros.

31

Concordante con lo observado en las modelaciones anteriores, estos resultados señalan que las

plumas tienden a mantenerse en el fondo, elevándose hasta cerca de 6 metros desde el fondo y

que, en las modelaciones de cuadratura, la dirección de la pluma tiende a ser hacia el Weste en

escenario de llenante y hacia el Sur-Surweste en escenario vaciante. La pluma de mayor longitud

(18,8 m) se obtuvo en el escenario llenante.

Estos resultados concuerdan, en cuanto a comportamiento de las plumas, longitud y dirección

con los obtenidos mediante Visual Plumes, siendo algo más conservadores para la mayoría de

los escenarios, salvo en el caso de la modelación de sicigia-vaciante, donde la modelación

mediante Visual Plumes alcanza una mayor longitud.

**Figura 22.** Resultado de la modelación OpenFOAM para SSD en escenario de marea llenante
en fase lunar de cuadratura. Arriba se muestra una vista frontal, desde la capa Océano, y abajo
una vista superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

32

**Figura 23.** Resultado de la modelación OpenFOAM para SSD en escenario de marea vaciante
en fase lunar de cuadratura. Arriba se muestra una vista frontal, desde la capa Océano, y abajo
una vista superior de la pluma. El dominio de la modelación se entrega en la Figura 3.

4.3 Determinación del área de influencia

En las **Tablas 7** y **8** se entrega el resultado de la estimación de la longitud máxima de las plumas

de descarga por escenario ( **Tabla 6** ), parámetro (SST, SSD) y plataforma de modelación utilizada

(Visual Plumes vs OpenFOAM). Con base en estos resultados, es posible establecer que, para

la mayoría de los escenarios modelados, las mayores longitudes de plumas de descarga ocurren

en la modelación con OpenFOAM ( **Tabla 8** ), en particular, para el caso del parámetro SSD. No

obstante en el caso de la modelación de sicigia-vaciante, la modelación con Visual Plumes

alcanza una longitud máxima de 25 metros ( **Tabla 7** ), mientras que en OpenFOAM alcanza una

longitud de 15,4 m ( **Tabla 8** ).

33

A partir de este resultado, en la **Figura 24** se entrega la estimación del área de influencia de la

pluma de descarga, considerando un radio de 1,78 metros para el momento en el cual se alcanza

la dilución del parámetro SSD a 5 ml/l/h ( **Tabla 8** ) y 25 metros para el momento en el cual se

alcanza la dilución de SSD a 0,1 ml/l/h ( **Tabla 7** ). Las superficies estimadas alcanzan a 9,96 m [2]

y 1.963 m [2], respectivamente. En la figura se entrega además la Zona de Protección Litoral (ZPL)

calculada a 230 metros desde la línea baja marea (línea segmentada roja), lo que permite

corroborar que, de acuerdo a los escenarios y parámetros modelados, la dilución de la descarga

a Tabla 4 se alcanza prácticamente inmediatamente en torno a la descarga y que la dilución a las

concentraciones típicas del medio receptor, se alcanza entrando a la ZPL.

**Tabla 7.** Síntesis de los resultados de estimaciones de plumas de descarga por escenario para
la plataforma Visual Plumes. En rojo se destacan las plumas de mayor longitud estimadas.

**Longitud de la pluma (m)**

**Plataforma** **Escenario** **Dilución** **SST** **SSD**

Visual-Plumes Llenante-Sicigia Tabla 4 DS90 <1 <1

Vaciante-Sicigia Tabla 4 DS90 <1 <1

Llenante-Cuadratura Tabla 4 DS90 <1 <1

Vaciante-Cuadratura Tabla 4 DS90 <1 <1

Llenante-Sicigia Medio receptor 6 14

Vaciante-Sicigia Medio receptor **9** **25**

Llenante-Cuadratura Medio receptor 3 12

Vaciante-Cuadratura Medio receptor 3 5

34

**Tabla 8.** Síntesis de los resultados de estimaciones de plumas de descarga por escenario para
la plataforma OpenFOAM. En rojo se destacan las plumas de mayor longitud.

**Longitud de la pluma (m)**

**Plataforma** **Escenario** **Dilución** **SST** **SSD**

OpenFOAM Llenante-Sicigia Tabla 4 DS90 0,46 1,07

Vaciante-Sicigia Tabla 4 DS90 0,43 0,83

Llenante-Cuadratura Tabla 4 DS90 **1,06** 0,96

Vaciante-Cuadratura Tabla 4 DS90 0,73 **1,79**

Llenante-Sicigia Medio receptor 9,35 15,5

Vaciante-Sicigia Medio receptor **10,4** 15,4

Llenante-Cuadratura Medio receptor 10,3 **18,8**

Vaciante-Cuadratura Medio receptor 11,1 18,2

**Figura 22.** Áreas de influencia de la pluma de descarga hasta llegar a la concentración de Tabla
4 (color rojizo: radio 1,78 m) y hasta llegar a la concentración del medio receptor (color celeste:
radio 25 m).

35

**5** **CONCLUSIONES**

El análisis de la información de campo reveló que en la zona de estudio la dinámica de corrientes

posee una fuerte influencia de las mareas en fase lunar de sicigia y cuadratura, observándose en

las capas superficiales velocidades normalmente inferiores a 40 cm s [-1], con cambios notables en

la dirección de corrientes en fase lunar de sicigia, destacando una dirección Este-Sureste en

marea llenante y en sentido Weste-Surweste en marea vaciante. En la capa más profunda (8

metros), las velocidades tienden a ser superiores, con máximos que eventualmente superan 100

cm s [-1], y la dirección de corrientes mantiene la misma tendencia que en superficie (dirección

Sureste en llenante y Surweste en vaciante). En la fase lunar de cuadratura, en cambio, las

direcciones predominantes se orientan en sentido Sur-sureste en superficie y Surweste en el

fondo, sin registrarse diferencias notables entre marea llenante y vaciante. Por otro lado, las

direcciones de corrientes a media agua (4 metros), se orientaron en sentido Surweste y Sur

Surweste en fase lunar de sicigia y cuadratura, respectivamente, sin observarse diferencias entre

marea llenante y vaciante.

Los resultados de la modelación mediante Visual Plumes UM3 indican que, para el caso de SST

y en todos los escenarios modelados, la pluma tiende a mantenerse bajo los 4 metros alcanzando

longitudes máximas de 9 metros. Para SSD las plumas alcanzan longitudes entre 7 y 25 metros,

observándose que las plumas tienden a elevarse hacia los estratos superficiales bajo los

escenarios de cuadratura.

El resultado de la modelación mediante OpenFOAM muestra resultados que son consistentes

con Visual Plumes, con resultados más conservadores en la mayoría de los escenarios, salvo en

el caso de la fase lunar sicigia y marea vaciante. En este caso, la pluma de dilución modelada

mediante Visual Plumes alcanza una longitud máxima de 25 metros, mientras que la modelación

con OpenFOAM alcanza 15,4 metros. En la mayoría de los casos analizados, las plumas

modeladas con OpenFOAM tienden a mantenerse cercanas al fondo y con dirección SSW,

excepto en el escenario de marea llenante en fase lunar de sicigia, donde la dirección

predominante de las plumas modeladas es en sentido SE. Adicionalmente, en los escenarios de

cuadratura para SSD, las plumas tienden a elevarse, superando los 5 metros desde el fondo (<

4 metros desde la superficie).

36

Con base en estos resultados, se determinó como escenario más conservador o peor escenario,

que el área de influencia de la pluma de descarga alcanza un radio de 1,79 metros para diluirse

a las concentraciones establecidas en la Tabla 4 del DS90 y a un radio de 25 metros para el

momento en el que la pluma alcanza la concentración del medio receptor. La dilución de la

descarga a las concentraciones límites de la Tabla 4 del DS90 se alcanza prácticamente

inmediatamente en torno a la descarga, mientras que la dilución a las concentraciones típicas del

medio receptor, se alcanza entrando a la Zona de Protección Litoral.

37

**6** **REFERENCIAS**

**Blazek, J. 2015.** Computational Fluid Dynamics: Principles and Applications. Elsevier Ltd. 446

pp.

**Cheung, S.K.B., D.Y.L. Leung, W. Wang, J.H.W. Lee & V. Cheung, V. 2000.** VISJET-a
computer ocean outfall modelling system. Proceedings Computer Graphics International 2000.
doi:10.1109/cgi.2000.852322

**Dokener, R.L. & G. Jirka. 2007.** CORMIX User Manual. A Hydrodynamic Mixing Zone Model and
Decision Support System for Pollutant Discharges into Surface Waters. U.S. Environmental
Protection Agency. 206 pp.

**Frick, W. E., Roberts, P. J. W., Davis, L. R., Keyes, J., Baumgartner, D. J., & George, K. P.**
**2003.** Dilution Models for Effluent Discharges,4th Edition (Visual Plumes). U.S. Environmental
Protection.

**Frick, W. E., D. Baumgartner, L. Davis, Z. Ge, K, George, P. Roberts. 2005.** Visual Plumes
2005. Model Update Documentation. U.S. Environmental Protection Agency. 90 pp.

**Inan, A. 2018.** Modeling of Hydrodynamics and Dilution in Coastal Waters. Water 2019, 11, 83;
doi:10.3390/w11010083.

**Jirka, G. H., R. L. Doneker & S.W. Hinton. 1996.** “MANUAL FOR CORMIX: A Hydrodynamic
Mixing Zone Model and Decision Support System for Pollutant Discharges into Surface Waters”.
U.S.EPA, Office of Science and Technology, Washington.

**Lee J. H. & V.H. Chu. 2003.** Turbulent Jets and Plumes: A Lagrangian Approach. Kluwer
Academic Publishers. Springer. U.S.A. 389 pp.

**Rapp, B. E. 2017** . Computational Fluid Dynamics. Microfluidics: Modelling, Mechanics and
Mathematics, 609-622. doi:10.1016/b978-1-4557-3141-1.50029-0

**SHOA. 1999.** Instrucciones Oceanográficas No2. Método oficial para el cálculo de los valores no
armónicos de las mareas. 2da. Edición. Armada de Chile. 26pp.

**Tang, H.S., J. Paik, F. Sotiropoulos & T. Khangaonkar. 2008.** Three-Dimensional Numerical
Modeling of Initial Mixing of Thermal Discharges at Real-Life Configurations. Journal of Hydraulic
Engineering, 134(9), 1210-1224. doi:10.1061/(asce)0733-9429(2008)134:9(1210)

38

**7** **Anexos**

39

7.1 Anexo I. Permiso SHOA para instalación de correntómetros en Bahía Ancud.

40

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 6.: ** Escenarios de modelación propuestos para la dinámica de corrientes en la zona de**

| propuestos se entregan en la Tabla 1. | Col2 | Col3 |
| --- | --- | --- |
| <br> <br> | **Sicigia** | **Cuadratura** |
| **Estrato**<br>**Variable**<br>**Unidad** | **Llenante**<br>**Vaciante** | **Llenante**<br>**Vaciante** |
| 2 m<br>Dirección<br>grados-N<br>Velocidad<br>cm/s | 112,9<br>243,9<br>18,8<br>35,8 | 146,5<br>246,0<br>14,6<br>19,6 |
| 4 m<br>Dirección<br>grados-N<br>Velocidad<br>cm/s | 190,3<br>206,3<br>16,4<br>33,1 | 192,2<br>205,9<br>17,1<br>27,3 |
| 8 m<br>Dirección<br>grados-N<br>Velocidad<br>cm/s | 137,3<br>220,5<br>18,2<br>53,1 | 255,0<br>212,1<br>6,5<br>6,3 |
