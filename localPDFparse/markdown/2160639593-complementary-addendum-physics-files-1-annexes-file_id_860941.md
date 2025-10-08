---
title: Sin título
author: CSW
date: D:20250307182701-03'00'
language: es
type: report
pages: 59
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Adenda Complementaria Proyecto Parque Fotovoltaico Leones Solar Anexo 2.3. Modelación de emisiones atmosféricas
-->

# Adenda Complementaria Proyecto Parque Fotovoltaico Leones Solar Anexo 2.3. Modelación de emisiones atmosféricas

Documento elaborado para

Marzo, 2025

Consultoría y Tecnología al Servicios del Medio Ambiente

Nva de Lyon 96, Of 307, Providencia

+56 2 3224 9095 contacto@csw.cl

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Índice de contenido

1 Introducción ................................................................................................................................... 6

2 Justificación del modelo a utilizar .................................................................................................. 6

2.1 Modelo de dispersión de contaminantes CALPUFF ............................................................... 7

2.2 Fundamentos del modelo ....................................................................................................... 9

3 Parámetros de entrada modelo CALPUFF ................................................................................... 11

3.1 Escenario meteorológico ...................................................................................................... 11

3.2 Dominio de modelación ........................................................................................................ 12

3.3 Uso de suelos ........................................................................................................................ 13

3.4 Escenario de emisiones ........................................................................................................ 14

3.5 Escenario de receptores ....................................................................................................... 15

4 Caracterización Meteorológica del Área del Proyecto ................................................................ 17

4.1 Estación Catapilco Zapallar ................................................................................................... 18

5 Resultados de la modelación ....................................................................................................... 22

5.1 Escenario geofísico ............................................................................................................... 22

5.2 Modelo meteorológico ......................................................................................................... 25

5.3 Resultados modelación CALPUFF ......................................................................................... 35

5.3.1 Material particulado ...................................................................................................... 35

6 Análisis de incertidumbre modelo WRF ...................................................................................... 39

6.1 Análisis cualitativo ................................................................................................................ 39

6.2 Análisis cuantitativo .............................................................................................................. 43

7 Cuerpo normativo ........................................................................................................................ 44

7.1 Normativa nacional de calidad del aire ................................................................................ 44

Página 2 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

7.2 Normativa internacional de referencia ................................................................................ 44

8 Evaluación de impactos ............................................................................................................... 47

8.1 Evaluación de impactos sobre la salud de la población ....................................................... 47

8.2 Evaluación de impactos sobre la calidad del aire, flora y vegetación, fauna, aguas

superficiales y suelo .......................................................................................................................... 49

9 Área de influencia ........................................................................................................................ 53

10 Conclusiones ........................................................................................................................... 55

11 Bibliografía .............................................................................................................................. 57

Índice de Figuras

Figura 1. Perfil de elevación ................................................................................................................... 7

Figura 2. Representación Gráfica del Modelo Tipo Puff y de Pluma ..................................................... 9

Figura 3. Grilla meteorológica y grilla computacional ......................................................................... 12

Figura 4. Uso de suelo dominio de modelación .................................................................................. 13

Figura 5. Escenario de fuentes ............................................................................................................. 14

Figura 6. Receptores ............................................................................................................................ 17

Figura 21. Serie de tiempo velocidad viento Estación Catapilco Zapallar ........................................... 18

Figura 22. Velocidad del viento Estación Catapilco Zapallar ............................................................... 19

Figura 23. Rosa de los vientos Estación Catapilco Zapallar ................................................................. 20

Figura 24. Dirección del viento Estación Catapilco Zapallar ................................................................ 20

Figura 25. Serie de tiempo temperatura Estación Catapilco Zapallar ................................................. 21

Figura 26. Ciclo diario y estacional temperatura Estación Catapilco Zapallar .................................... 21

Figura 7. Topografía ............................................................................................................................. 22

Figura 8. Albedo ................................................................................................................................... 23

Página 3 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 9. Rugosidad superficial ............................................................................................................ 23

Figura 10. Leaf Area Index .................................................................................................................... 24

Figura 11. Razón de Bowen .................................................................................................................. 24

Figura 12. Rosa de los vientos año 2022 .............................................................................................. 27

Figura 13. Variabilidad temporal del viento ........................................................................................ 28

Figura 14. Variación dirección del viento ............................................................................................. 29

Figura 15. Serie de tiempo velocidad del viento ................................................................................. 30

Figura 16. Ciclo diario velocidad del viento ......................................................................................... 30

Figura 17. Velocidad del viento ............................................................................................................ 31

Figura 15. Serie de tiempo temperatura ............................................................................................. 31

Figura 18. Mapa de isoconcentraciones de MP10 promedio anual .................................................... 36

Figura 19. Mapa de isoconcentraciones de MP10 promedio 24h ...................................................... 37

Figura 20. Mapa de isoconcentraciones de MP2.5 promedio anual ................................................... 37

Figura 21. Mapa de isoconcentraciones de MP2.5 promedio 24h ..................................................... 38

Figura 22. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio anual ............ 39

Figura 23. Área de influencia calidad del aire ...................................................................................... 54

Índice de Tablas

Tabla 1. Construcción detalle del dominio de los datos meteorológicos ........................................... 11

Tabla 2. Resumen tasa de emisiones atmosféricas para el año 1 ....................................................... 15

Tabla 3. Receptores modelación .......................................................................................................... 16

Tabla 95. Estaciones caracterización meteorológica ........................................................................... 17

Tabla 96. Estación Bomberos ............................................................................................................... 18

Tabla 4. Campo de vientos ................................................................................................................... 25

Página 4 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Tabla 5. Altura de la capa de mezcla .................................................................................................... 33

Tabla 6. Resultados modelación año 1 material particulado .............................................................. 35

Tabla 97. Análisis de incertidumbre cuantitativo velocidad del viento ............................................... 43

Tabla 98. Análisis de incertidumbre cuantitativo temperatura .......................................................... 44

Tabla 7. Cuerpo normativo .................................................................................................................. 44

Tabla 8. Cuerpo normativo .................................................................................................................. 46

Tabla 9. Comparación material particulado con normas primarias de calidad del aire ..................... 48

Tabla 9. Comparación material particulado con normas de calidad secundarias de calidad del aire 50

Tabla 10. Potenciales impactos sobre componente calidad del aire .................................................. 49

Tabla 11. Evaluación de impactos ........................................................................................................ 51

Página 5 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

1 Introducción

El presente documento tiene como objetivo establecer el impacto de las emisiones del "Proyecto

Fotovoltaico Leones Solar" en la calidad del aire, utilizando los resultados del Inventario de emisiones

atmosféricas, detallado en el Anexo 3.1 de la Adenda.

Según lo establecido por la “Guía para el uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2023),

la selección del modelo meteorológico utilizado en el presente estudio se realizó fundamentándose

en las condiciones del dominio de modelación, motivo por el cual la Guía recomienda un modelo que

permita simular una meteorología heterogénea. Por esta razón, el campo meteorológico

tridimensional horario del año 2022 completo, fue generado utilizando el modelo meteorológico

WRF en su versión 4.0.3, y procesado con MMIF v3.2. Posteriormente esta información fue utilizada

como parámetro de entrada del modelo de calidad de aire CALPUFF.

Las tasas de emisión se consideraron para el escenario más desfavorable, es decir para el año en que

el Proyecto genera mayor cantidad de emisiones atmosféricas, correspondiente al Año 1, el cual

comprende el primer año de la fase de construcción. A partir de las emisiones estimadas, se

proyectan mediante el modelo CALPUFF, valores de concentración para material particulado, los que

posteriormente serán comparados con las normas de calidad el aire.

2 Justificación del modelo a utilizar

La "Guía para el Uso de Modelos de Calidad del Aire en el SEIA" (SEA, 2023) establece dos criterios

para la selección de un modelo de dispersión de contaminantes. El primer criterio se basa en la

distancia a lo largo del territorio nacional, donde se considera que a menor distancia existe una mayor

probabilidad de que el terreno sea homogéneo, lo que significa que habrá menos factores que alteren

significativamente el transporte y la dilución de contaminantes. Para el análisis del modelo a elegir,

este criterio considerará una distancia lineal referencial de 5 km desde la fuente de emisión hasta la

zona de impacto de las emisiones atmosféricas. El segundo criterio se refiere al tipo de contaminante

a modelar, distinguiendo entre contaminantes primarios, que son emitidos directamente a la

atmósfera, y contaminantes secundarios, que son productos de reacciones fisicoquímicas en la

atmósfera.

En el caso específico del Proyecto, se aplicará el criterio recomendado por la "Guía para el Uso de

Modelos de Calidad del Aire en el SEIA" (SEA, 2023) para contaminantes primarios, considerando un

alcance de los impactos de las emisiones mayor a los 5 km. Para esta situación, la Guía recomienda

utilizar un modelo que permita simular la meteorología heterogénea. Los modelos de tipo "puff" y

Eulerianos son capaces de representar esta variabilidad meteorológica. La elección del modelo se

basó en las recomendaciones del apartado 3.2 de la Guía, ya que las emisiones a considerar son de

tipo primario y provienen de una fuente de emisión en un área de modelación de más de 5

kilómetros, abarcando fuentes y receptores sensibles. Además, existen factores en la topografía del

área circundante al Proyecto, donde el perfil de elevación presenta diferencias de altura mayores a

Página 6 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

1200 metros, lo que podría afectar el carácter lineal de los vientos, como se presenta en la siguiente

Figura.

Figura 1. Perfil de elevación

Fuente: Elaboración propia mediante Google Earth Pro.

Por lo tanto, siguiendo las directrices de la "Guía para el Uso de Modelos de Calidad del Aire en el

SEIA" (SEA, 2023), se utilizará un modelo que permita simular la meteorología heterogénea. En este

sentido, se ha seleccionado un modelo de tipo "puff" para llevar a cabo la modelación de calidad del

aire. A continuación, se proporciona el detalle del modelo de tipo "puff" que se utilizará.

2.1 Modelo de dispersión de contaminantes CALPUFF

El sistema de modelación, tal como su nombre lo indica, incluye dos componentes principales: WRF

y CALPUFF, además de una larga selección de preprocesadores, diseñados para incluir en el modelo

datos geofísicos y de usos de suelos, y postprocesadores como por ejemplo CALPOST, que permiten

Página 7 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

convertir los resultados a los estadísticos considerados por las normas primarias y secundarias de

calidad del aire.

En cuanto a la meteorología base utilizada en la modelación, se desarrolló un modelo de retrospectiva

(Hindcast) WRF (Weather Research and Forecasting, por sus siglas en ingles), el cual provee los datos

de entrada que simulan la meteorología de un año pasado y permiten modelar la dispersión de las

emisiones en la atmósfera mediante el software CALPUFF. En cuanto a esto, cabe destacar que, el

modelo cumple con las recomendaciones de configuración definidas por el Servicio de Evaluación

Ambiental, particularmente respecto de los documentos “Configuración WRF” y “Namelist.input”.

Adicionalmente, la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA" (SEA, 2023), establece

que el modelo numérico recomendado para la generación de datos meteorológicos es el WR, el cual

corresponde a uno de simuladores meteorológicos de pronóstico más avanzados, completos y en
constante mejora, mantenido por NCAR/NOAA de Estados Unidos. Además, ha sido utilizado en la

mayoría de los proyectos relacionados con el comportamiento atmosférico encargados por la

Comisión Nacional de Energía, Ministerio del Medio Ambiente.

Por otra parte, CALPUFF es un modelo tipo “puff”, corresponde a una combinación entre los modelos

Gaussianos y los modelos Lagrangeanos. Lo que hacen estos modelos es esencialmente calcular la

dispersión de una emisión puntual (puntual en el tiempo), llamado puff, a lo largo de una trayectoria.

Su aproximación matemática es estimar la dispersión en forma Gaussiana en cada punto de una

trayectoria. Es decir, a diferencia de los modelos Langrangeanos que necesitan el cálculo de un gran

número de trayectorias para una fuente, en el caso de los modelos tipo puff sólo se requiere una

trayectoria por puff lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se

simulan trayectorias y la dispersión Gaussiana de muchos puff. Además, son capaces de simular

muchas fuentes y fuentes de distinto tipo al mismo tiempo (SEA, 2023). Los modelos tipo “puff”

representan una pluma de contaminantes continua como un número discreto de paquetes de

material contaminante, tal como se muestra la siguiente Figura:

Página 8 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 2. Representación Gráfica del Modelo Tipo Puff y de Pluma

Fuente: Lakes Environmental (2006).

2.2 Fundamentos del modelo

CALMET

CALMET es un modelo de diagnóstico meteorológico que consta de dos módulos principales:

 - Módulo de campo de vientos.

 - Módulo de capa límite

La aproximación usada por CALMET para calcular el campo de viento consiste en dos pasos:

En el primer paso, se obtiene un campo de vientos inicial considerando únicamente los efectos que

sobre el flujo atmosférico tienen las características físicas del terreno: efectos cinemáticos, efectos

producidos por las laderas y posibilidad de bloqueos. En el segundo paso se aplica un procedimiento

objetivo sobre la base de los vientos observados en estaciones de monitoreo, obteniendo el campo

de vientos final después de un proceso iterativo para minimizar la divergencia del campo de viento y

garantizar el cumplimiento de la ecuación de conservación de mas (EPA, 2017).

Página 9 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Cabe señalar, que en este caso solo se cargaron los datos tipo CALMET-Ready WRF usándolos

directamente, puesto que por recomendación del SEA en la “Guía para el Uso de Modelos de Calidad

del Aire en el SEIA" (SEA, 2023).

CALPUFF

El modelo CALPUFF junto con el modelo meteorológico CALMET constituye un sistema de modelos

enfocados a tratar la dispersión de contaminantes en la atmósfera.

Es un modelo Lagrangiano-Gaussiano de transporte y dispersión de soplos o “puff” emitidos por las

fuentes consideradas por el proyecto que se simulan considerando el efecto de las condiciones

meteorológicas (simuladas con CALMET) variando en el tiempo y en el espacio sobre el transporte,

transformación y eliminación de varios contaminantes. En cuanto a distancia, puede aplicarse a

escalas desde decenas a centenas de kilómetros. Incluye algoritmos para tratar procesos a escala

subgrid, así como, efectos a gran escala. Puede tratar los efectos de terreno complejo, zonas costeras,

cizalla del viento permitiendo la división de las nubes de contaminantes, efectos de estelas de

edificios, depósito de contaminantes por vía seca y húmeda (EPA, 2023).

El modelo evalúa la contribución de un “puff” en la concentración atmosférica de un punto de la grilla

en un instante determinado, para luego permitir que el “puff” se mueva, evolucione en tamaño,

fuerza, etc., hasta la próxima iteración, en el próximo punto de la grilla, respondiendo a la

meteorología del sector en la que se encuentre inmerso el “puff” en cada instante. Luego, la

concentración total en un receptor resultará de la sumatoria de las contribuciones de todos los

“puff”. La ecuación básica del modelo se muestra a continuación:

Dónde:

_C:_ Concentración [g/m3].

_Q:_ Masa del contaminante en el “puff” [g].

_σx:_ Coeficiente de dispersión en dirección del viento [m].

_σy:_ Coeficiente de dispersión en dirección perpendicular al viento [m].

_σz:_ Coeficiente de dispersión vertical [m].

_da:_ Distancia desde el centro del “puff” hacia el receptor en el eje de la dirección del viento

[m].

_dc:_ Distancia desde el centro del “puff” hacia el receptor en el eje perpendicular a la dirección

del viento [m].

Página 10 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

_g:_ Altura de la ecuación gaussiana [m].

_H:_ Altura efectiva del “puff” [m].

_h:_ Altura de la capa de mezcla [m].

Para casos que involucran un alto grado de variabilidad espacial del flujo dentro de la capa límite,

tales como flujos ascendentes o descendentes o flujos a lo largo de un valle fluvial sinuoso, la

suposición de estado estacionario en línea recta puede ser poco válida incluso a algunos kilómetros

de la fuente, por lo que un modelo del tipo “puff” puede ser el más apropiado (EPA, 2017).

CALPOST

Parte fundamental del proceso de modelación con la plataforma CALMET/CALPUFF, es el módulo

CALPOST quien procesa las salidas de CALPUFF creando los archivos que permiten realizar la

evaluación de los resultados, según lo establecido en las normas de calidad del aire. Además, es capaz

de gestionar los datos de cada contaminante según el período de tiempo requerido, ordenando las

máximas concentraciones obtenidas e identificando el momento en que cada una de éstas suceden

(hora, día, mes y año) (EPA, 2017).

3 Parámetros de entrada modelo CALPUFF

El modelo para poder ejecutarse requiere una grilla de información, la construcción de los escenarios

a evaluar, dichos escenarios son procesados sobre la información geofísica del área de modelación.
Una vez generada esta información, se establecen las fuentes emisoras asociadas y/o actividades a

realizar por el proyecto. Lo antes mencionado es integrado en paralelo a los receptores establecidos

sobre el dominio de la modelación. Las magnitudes de las emisiones generadas por el proyecto

provienen de la estimación de emisiones realizada con los factores AP-42 de la EPA. Estos valores en

conjunto con los obtenidos de información satelital consolidan la información real del área de

influencia directa a modelar.

3.1 Escenario meteorológico

El escenario meteorológico se construyó a partir de la información meteorológica generado por el

modelo WRF que se utilizó para desarrollar esta componente. El dominio de modelación presenta las

siguientes características:

Tabla 1. Construcción detalle del dominio de los datos meteorológicos

|Periodo de datos de los datos|1 enero a 31 de diciembre de 2022|
|---|---|
|Punto de Referencia|Latitud: - 32.392 S<br>Longitud: - 71.343 W|
|Área de Dominio|50x50 km|
|Proyección|Lambert Conic Conformal|
|Datum|NWS-84 6370 km Radius, Global Sphere|

Página 11 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Periodo de datos de los datos|1 enero a 31 de diciembre de 2022|
|---|---|
|Resolución|1 km|
|Numero de Celdas en dirección x|50|
|Numero de Celdas en dirección y|50|
|Numero de Capas Verticales|11 (entre 0 y 4000 metros de altura)|
|Tipo de dato|CALPUFF-Ready WRF Data (WRF.MET Format)|

Fuente: Elaboración propia.

Una vez definido los datos meteorológicos se construye el dominio a procesar. Este se implementó

sobre un área de 25 km dirección Norte y Sur y 25 km dirección Este y Oeste, desde el origen ubicado

en el punto de referencia mencionado.

3.2 Dominio de modelación

El dominio de modelación del Sistema Calpuff-WRF se compone de tres tipos de grilla, la

meteorológica, la computacional y la de muestreo (sampling grid), donde: El dominio meteorológico

comprende un área de 50 [km] x 50 [km], correspondiente a la grilla del WRF ocupado.

Figura 3. Grilla meteorológica y grilla computacional

Fuente: Elaboración propia.

Página 12 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Por otra parte, para definir la grilla de muestreo, se han seguido los lineamientos establecidos en la

"Guía para el Uso de Modelos de Calidad del Aire en el SEIA" (SEA, 2023). Esta guía señala que es

necesario asegurarse de que el tamaño de la grilla sea lo suficientemente amplio para garantizar la

medición precisa de la concentración máxima a nivel del suelo.

Al seguir estos criterios, se busca obtener una representación precisa de la calidad del aire en el área

de estudio, considerando la cuantificación de la concentración máxima y garantizando la fiabilidad

de los resultados obtenidos. Es importante destacar que el uso de estas grillas de muestreo en

conformidad con las recomendaciones de la Guía contribuye a fortalecer la robustez de la evaluación

de la calidad del aire.

3.3 Uso de suelos

La información relacionada con el uso de suelo de la zona se obtiene a través de los archivos Global

Land Cover Characterization (GLCC) publicados por el U.S Geological Survey (USGS). En la siguiente

Figura se presenta el uso de suelos para el dominio de modelación.

Figura 4. Uso de suelo dominio de modelación

Fuente: Elaboración propia, 2023.

De la figura anterior el uso de suelo 51 corresponde a “Corrientes y canales”, el uso de suelo 40

corresponde a “Bosques”, el uso de suelo 30 corresponde a “Pastizales”, el uso de suelo 20

corresponde a “Tierra agrícola” y el uso de suelo 10 corresponde a “Urbano”.

Página 13 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

De la figura anterior se aprecia que en el dominio de modelación existen diversos usos de suelo. En

el sector de emplazamiento del proyecto se aprecian los usos de suelo de tipo “Pastizales” y “Tierra

agrícola”.

3.4 Escenario de emisiones

A continuación, se presenta el escenario a modelar, donde se contemplan las fuentes de emisión de

material particulado para el peor escenario posible a modo de descartar afectaciones a la salud de la

población. Cabe destacar, que se considera la construcción y operación del proyecto dentro del año

1, dado que es el período más crítico del Proyecto, el cual abarca la fase de construcción (12 meses).

De manera conservadora, se considera que todas las emisiones de las actividades constructivas son

producidas de manera simultánea en el predio del Proyecto, lo que en la práctica no ocurrirá, puesto

que las actividades constructivas son realizadas de forma secuencial.

En el contexto de la modelación, se han considerado las emisiones generadas por el tránsito y la

combustión en caminos pavimentados y no pavimentados, los cuales están representadas en color

azul. Por otro lado, se han considerado las emisiones generadas por diversas actividades en el área

del proyecto, como maquinaria fuera de ruta, grupos electrógenos, excavaciones, nivelación,

perforaciones y movimiento de tierra, los cuales se han representado en color rojo.

Figura 5. Escenario de fuentes

Fuente: Elaboración propia.

Página 14 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

De las emisiones presentadas en la estimación de emisiones para el año 1, la resuspensión por

tránsito en vías pavimentadas se asocian a la fuente denominada “Caminos pavimentados”, en el

caso de la resuspensión por tránsito en vías no pavimentadas se asocian a la fuente denominada

“Caminos No pavimentados”, por otra parte, las emisiones asociadas a excavaciones, movimiento de

tierra, compactación, nivelación, perforación, maquinaria fuera de ruta y grupos electrógenos, se
asocia a la fuente de área denominada “Área Proyecto”, y las emisiones para la construcción de la

línea eléctrica, como excavación de fundaciones y movimientos de tierra, se denominan “LAT”, como

se detalla en la siguiente Tabla.

Tabla 2. Resumen tasa de emisiones atmosféricas para el año 1

|Contami<br>nante|Resultados estimación de emisiones|Col3|Col4|Col5|Datos entrada CALPUFF|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Contami<br>nante|Área<br>Proyecto|LAT|Caminos<br>No<br>pavimenta<br>dos|Caminos<br>pavimentad<br>os|Área<br>Proyecto|LAT|Caminos<br>pavimentad<br>os|Caminos<br>No<br>pavimenta<br>dos|
|Unidad|t/año|t/año|t/año|t/año|g/s/m2|g/s/m2|g/s/m|g/s/m|
|MP10|1,2259|0,0055|2,0822|1,5105|6,91E-08|5,00E-08|4,59E-09|2,36E-10|
|MP2.5|0,7420|0,0028|0,2082|0,4112|4,19E-08|2,50E-08|4,59E-10|6,42E-11|
|MPS|1,9444|0,0265|6,8018|7,6146|1,10E-07|2,39E-07|1,50E-08|1,19E-09|
|Tipo de<br>fuente|Areal|Areal|Lineal|Lineal|Areal|Areal|Lineal|Lineal|

Fuente: Elaboración propia.

3.5 Escenario de receptores

Los receptores discretos han sido definidos siguiendo las directrices establecidas en la "Guía para el

uso de modelos de calidad del aire en el SEIA" (SEA, 2023). Esta guía señala que los receptores deben

ser seleccionados considerando las características específicas del lugar, la duración de su presencia y

los usos permitidos del suelo. Además, se deben tener en cuenta los objetivos de protección

identificados en la zona, los cuales se han establecido siguiendo las directrices del documento

"Criterio de Evaluación en el SEIA: Objetos de protección" (SEA, 2022). En dicho documento, los

objetos de protección se definen como elementos o componentes del medio ambiente que se

derivan del marco legal vigente, en particular del artículo 11 de la Ley N°19.300 Sobre Bases
Generales del Medio Ambiente, y de los artículos 5° al 10 del Decreto Supremo N°40/2012 del

Ministerio del Medio Ambiente, que establece el Reglamento del SEIA (RSEIA). Estos objetos de

protección deben ser salvaguardados de los posibles impactos ambientales que pueda generar la

ejecución de un proyecto o actividad dentro del marco del Sistema de Evaluación de Impacto

Ambiental (SEIA).

Página 15 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Adicionalmente, la “Guía para el uso de modelos de calidad del aire en el SEIA" (SEA, 2023), señala

que para el caso de los receptores humanos se debe considerar una altura de inmisión de entre 1,5

a 1,8 metros, correspondiente a la altura promedio de la zona de inhalación de los contaminantes

atmosféricos por el cuerpo humano.

A continuación, se presentan los receptores identificados.

|Col1|Col2|Tabla 3. Receptores modelación|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Tipo Receptor|Id|Coordenadas|Coordenadas|Distancia<br>al<br>Proyecto<br>[m]|Descripción|
|Tipo Receptor|Id|WGS84 Huso 19S|WGS84 Huso 19S|WGS84 Huso 19S|WGS84 Huso 19S|
|Tipo Receptor|Id|Este [m]|Sur [m]|Sur [m]|Sur [m]|
|Red Hidrográfica|R1|279542,79|6408222,32|647|Río La Ligua|
|Humano|R2|278380,73|6408669,41|505|Viviendas|
|Humano|R3|281656,25|6408607,70|1659|Posta de Salud Pullally|
|Humano|R4|282184,29|6407984,32|1785|Viviendas Papudo|
|Red Hidrográfica|R5|281704,82|6407540,91|1222|Estero Jaruro|
|Humano|R6|284660,56|6407425,09|4173|Viviendas La Ligua|
|Humano|R7|285392,57|6407555,86|4906|Viviendas La Ligua|
|Atractivo Turístico|R8|280995,00|6409802,00|2395|Camino Longotoma-La<br>ligua|
|Santuario de la<br>naturaleza|R9|275592,95|6407415,01|2546|Humedal Salinas de<br>Pullally - Dunas de<br>Longotoma|
|Atractivo Turístico|R10|276284,00|6413297,00|5441|Longotoma|
|Sitio Prioritario|R11|273534,15|6412561,20|6351|Estuario Río La Ligua|
|Sitio Prioritario|R12|271468,28|6405872,52|6931|Papudo|
|Agrícola|R13|281716,47|6406861,64|1289|Cultivos|
|Humano|R14|277612,19|6405337,64|1554|Viviendas|
|Humano|R15|276712,17|6405497,10|2291|Viviendas|
|Industrial|RH1|278681|6406086|247|Recinto antena telefónica|
|Grupos humanos|RH2|281519|6407654|814|Vivienda/Almacén en área<br>rural|
|Grupos humanos|RH3|281387|6408746|65|Vivienda en área rural|
|Grupos humanos|RH4|280858|6408332|115|Vivienda en área rural|
|Grupos humanos|RH5|280369|6407982|271|Vivienda/Almacén en área<br>rural|
|Grupos humanos|RH6|279407|6408289|654|Vivienda en área rural|
|Grupos humanos|RH7|278134|6408733|555|Vivienda en área rural|

Fuente: Elaboración propia.

Página 16 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 6. Receptores

Fuente: Elaboración propia.

4 Caracterización Meteorológica del Área del Proyecto

La meteorología de superficie utilizada para caracterizar el área del Proyecto corresponde a los

registros horarios de velocidad y dirección del viento, pertenecientes a la estación meteorológica

Catapilco Zapallar, ubicada dentro del dominio de modelación, a 14 km del Proyecto. Cabe destacar

que esta estación corresponde a la Red Agrometeorológica del INIA (INIA, 2024).

Las coordenadas UTM de la estación indicada se presentan en la siguiente Tabla junto con las

variables monitoreadas.

Tabla 4. Estaciones caracterización meteorológica

|Estación|Coordenadas UTM|Col3|Variables Meteorológicas<br>Registradas|
|---|---|---|---|
|Estación|Este (m)|Norte (m)|Norte (m)|
|Estación Catapilco<br>Zapallar|286647|6393218|Dirección del viento<br>Velocidad del viento<br>Temperatura|

Página 17 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Fuente: Elaboración propia en base a INIA (2024).

4.1 Estación Catapilco Zapallar

En la siguiente Tabla se presentan las variables meteorológicas medidas en la estación, junto con el

porcentaje de registros válidos. Se destaca que el porcentaje de datos válidos es del 95%, cumpliendo

así con las recomendaciones establecidas en la "Guía para el uso de modelos de calidad del aire en el

SEIA" (2023). Esta guía sugiere que el porcentaje de datos válidos en un año debe ser superior al 75%.

Tabla 5. Estación Bomberos

|Variable|Año|N° Registros válidos|% Registros válidos|
|---|---|---|---|
|Dirección del viento|2022|7890|95%|
|Velocidad del viento|2022|8060|96%|
|Temperatura|2022|8060|96%|

Fuente: Elaboración propia en base a INIA (2024).

Velocidad del viento

La serie de tiempo de la velocidad del viento registrada en la estación Catapilco Zapallar durante el

año 2022 se presenta en la siguiente Figura. La velocidad del viento promedio registrada en la
estación Catapilco Zapallar es de 1,307 m/s. Las velocidades del viento más bajas se presentan

durante el período nocturno (entre las 0:00 y las 6:00 horas) y comienzan a aumentar desde las 6:00

am. En promedio, las velocidades más altas se registran entre las 12:00 y las 15:00 hora, con valores

cercanos a 3 m/s.

Figura 7. Serie de tiempo velocidad viento Estación Catapilco Zapallar

Fuente: Elaboración propia en base a INIA (2024).

Página 18 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 8. Velocidad del viento Estación Catapilco Zapallar

Fuente: Elaboración propia.

Dirección del viento

En la siguiente Figura se muestran los registros horarios de la dirección del viento, obtenidos en la

estación Aeródromo Rodelillo, además se presenta la rosa de viento elaborada con dichos registros.

Cabe destacar que la dirección del viento predominante corresponde a la dirección sur (S).

Página 19 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 9. Rosa de los vientos Estación Catapilco Zapallar

Fuente: Elaboración propia en base a INIA (2024).

Figura 10. Dirección del viento Estación Catapilco Zapallar

Fuente: Elaboración propia en base a INIA (2024).

Página 20 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Temperatura

La serie de tiempo de la temperatura registrada en la estación Catapilco Zapallar durante el año 2022

se presenta en la siguiente Figura. La temperatura promedio registrada en la estación es de 12,4 °C.

Las temperaturas más bajas se presentan durante el período nocturno (entre las 0:00 y las 5:00 horas)

y comienzan a aumentar desde las 6:00 am. En promedio, las temperaturas más altas se registran

entre las 12:00 y las 15:00 horas, alcanzando alrededor de 25 °C.

Figura 11. Serie de tiempo temperatura Estación Catapilco Zapallar

Fuente: Elaboración propia en base a INIA (2024).

Figura 12. Ciclo diario y estacional temperatura Estación Catapilco Zapallar

Fuente: Elaboración propia.

Página 21 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

5 Resultados de la modelación

A continuación, se presentan los resultados obtenidos, en cuanto a la concentración estimada de

contaminantes respecto a las distancias discretas establecidas (receptores). En el Apéndice A se

incluyen los resultados del modelo CALPUFF.

5.1 Escenario geofísico

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1, cuya resolución

es aproximadamente 30 m.

Figura 13. Topografía

Fuente: Elaboración propia.

El proyecto se encuentra ubicado en un sector donde la topografía es suave, puesto que se emplaza

entre cerros de baja altura y a una distancia donde posee influencia del borde costero, por lo que se

consideran aquellos accidentes geográficos o relieve en altura, dentro del modelo.

En los siguientes gráficos se presentan los datos de terreno obtenidos para la modelación.

Página 22 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

En los siguientes gráficos se presentan los datos de terreno obtenidos para la modelación.

Figura 14. Albedo

Fuente: Elaboración propia, 2023.

Figura 15. Rugosidad superficial

Fuente: Elaboración propia, 2023.

Página 23 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 16. Leaf Area Index

Fuente: Elaboración propia, 2023.

Figura 17. Razón de Bowen

Fuente: Elaboración propia, 2023.

Página 24 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

5.2 Modelo meteorológico

Mediante el uso del modelo CALMET y en función de los datos de entrada WRF descritos en el

escenario meteorológico, se procedió a generar una matriz de vientos predominantes y alturas

aproximadas de capas de mezclas al interior del dominio de la modelación, para cada hora del año

2022.

Con el fin de presentar los resultados a través de una gráfica de campos de viento, se ha seleccionado

el día 8 de marzo de 2022 como una fecha representativa dentro del dominio de modelación. La

siguiente tabla muestra el comportamiento de los vientos a una altura de 10 metros sobre el nivel

del suelo, para diferentes horarios de la fecha mencionada.

|Tabla 6. Campo de vientos|Col2|
|---|---|
|Campo de Viento|Descripción|
||Comportamiento de<br>los vientos a una<br>altura 10 metros<br>sobre el nivel de<br>suelo a las 16:00<br>horas<br>como<br>una<br>hora representativa<br>del 8 de marzo de<br>2022 al interior del<br>dominio<br>de<br>la<br>modelación.|

Página 25 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Fuente: Elaboración propia.

Página 26 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Dirección del viento

Con respecto a la dirección del viento, en la siguiente Figura presenta la rosa de los vientos

correspondiente al dominio de modelación. La componente principal corresponde al viento Oeste

(O).

Figura 18. Rosa de los vientos año 2022

Fuente: Elaboración propia.

A continuación, se presentan las rosas de los vientos que muestran la variabilidad temporal de la

velocidad y dirección del viento durante el periodo de modelación.

Página 27 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Figura 19. Variabilidad|temporal del viento|
|---|---|
|<br>Rosa de los vientos período 00:00 AM - 05:00 AM<br>entre el 01/01/2022 - 31/12/2022|<br>Rosa de los vientos período 06:00 AM - 11:00 AM<br>entre el 01/01/2022 - 31/12/2022|
|<br>Rosa de los vientos período 12:00 PM - 17:00 PM<br>entre el 01/01/2022 - 31/12/2022|<br>Rosa de los vientos período 18:00 PM - 23:00 PM<br>entre el 01/01/2022 - 31/12/2022|

Fuente: Elaboración propia.

Página 28 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 20. Variación dirección del viento

Fuente: Elaboración propia.

Velocidad del viento:

Con respecto a la velocidad del viento, a continuación, se presentan gráficos de velocidad de viento

y ciclos, diarios, semanales y mensuales de la velocidad del viento.

Página 29 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 21. Serie de tiempo velocidad del viento

Fuente: Elaboración propia.

Figura 22. Ciclo diario velocidad del viento

Fuente: Elaboración propia.

Página 30 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 23. Velocidad del viento

Fuente: Elaboración propia.

Temperatura:

Con respecto a la temperatura, a continuación, se presentan gráficos de la serie de tiempo para esta

variable.

Figura 24. Serie de tiempo temperatura

Fuente: Elaboración propia.

Página 31 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Altura de la capa de mezcla

Por otra parte, la profundidad vertical de la atmósfera donde se produce el mezclado, se denomina

capa de mezcla. La parte superior de esta capa se conoce como altura de mezcla, la cual determina

el alcance vertical del proceso de dispersión de los contaminantes liberados debajo de ella, a

continuación, se representa la altura de la capa de mezcla mediante procesamiento de datos

meteorológicos en el software CALPUFF View.

Página 32 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Tabla 7. Altura de la capa de mezcla|Col2|
|---|---|
|Altura de la capa de mezcla|Descripción|
||Presentación<br>del<br>comportamiento<br>de<br>la<br>altura de capa de mezcla en<br>horarios<br>representativos,<br>entre las 00:00 y las 08:00<br>del<br>día<br>escogido<br>para<br>exponer los resultados del<br>módulo<br>micro<br>meteorológico (8 de marzo<br>de<br>2022)<br>como<br>representativo de verano<br>como<br>peor<br>escenario<br>(menor humedad ambiental<br>y <br>menor<br>presencia<br>de<br>lluvias). En ese sentido, se<br>puede observar que, por la<br>temperatura ambiente y las<br>variables<br>ambientales<br>nocturnas, la altura de la<br>capa de mezcla se mantiene<br>relativamente<br>baja,<br>sin<br>pasar los 700 metros en la<br>mayoría de los puntos.|
|||

Página 33 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Col1|Presentación del<br>comportamiento de la<br>altura de capa de mezcla en<br>horarios representativos,<br>entre las 16:00 y las 20:00<br>del día escogido para<br>exponer los resultados del<br>módulo micro<br>meteorológico. Se puede<br>observar que, por la<br>temperatura ambiente y las<br>variables ambientales<br>diurnas, la altura de la capa<br>de mezcla se expande a los<br>sobre los 1500 metros. De<br>manera que se alcanzan los<br>1000 metros en la mayoría<br>de los puntos, volviendo a<br>contraerse en la tarde a los<br>404 metros.|
|---|---|
|||

Fuente: Elaboración propia.

Página 34 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

5.3 Resultados modelación CALPUFF

5.3.1 Material particulado

Con el fin de determinar la eventual influencia que tiene el Proyecto en la calidad del aire sobre la

localidad y los receptores identificados, en función de los análisis antes realizados, se determinaron

las concentraciones de MP10, MP2.5 y MPS para cada una de las horas del año sobre los receptores

considerados. A continuación, se presenta el aporte del proyecto sobre a los receptores antes

mencionados, segregado según los períodos de la norma de calidad del aire aplicable.

Tabla 8. Resultados modelación año 1 material particulado

|Receptor|MP10 (μg/m3)|Col3|MP2,5 (μg/m3)|Col5|MPS<br>(mg/m2/día)|
|---|---|---|---|---|---|
|Receptor|24 h|Anual|24 h|Anual|Anual|
|R1|0,1761602|0,1761603|0,1069572|0,1069571|0,000000|
|R2|0,1062904|0,1062902|0,0645800|0,0645800|0,000000|
|R3|0,0386698|0,0386697|0,0232327|0,0232327|0,000000|
|R4|0,0424391|0,0424391|0,0257205|0,0257205|0,000000|
|R5|0,0907580|0,0907579|0,0550190|0,0550190|0,000000|
|R6|0,0156795|0,0156796|0,0095484|0,0095484|0,000000|
|R7|0,0128282|0,0128282|0,0078163|0,0078163|0,000000|
|R8|0,0267774|0,0267773|0,0162790|0,0162790|0,000000|
|R9|0,0496211|0,0496211|0,0302657|0,0302656|0,000000|
|R10|0,0080107|0,0080107|0,0048866|0,0048866|0,000000|
|R11|0,0073069|0,0073069|0,0044579|0,0044579|0,000000|
|R12|0,0084828|0,0084828|0,0051847|0,0051847|0,000000|
|R13|0,1322659|0,1322661|0,0804084|0,0804083|0,000000|
|R14|0,0872357|0,0872357|0,0530937|0,0530937|0,000000|
|R15|0,0556857|0,0556857|0,0339093|0,0339092|0,000000|
|RH1|0,1090110|0,1090109|0,0662797|0,0662797|0,005166|
|RH2|0,0597675|0,0597675|0,0360522|0,0360522|0,005041|
|RH3|0,0372633|0,0372632|0,0218390|0,0218391|0,008782|

Página 35 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Receptor|MP10 (μg/m3)|Col3|MP2,5 (μg/m3)|Col5|MPS<br>(mg/m2/día)|
|---|---|---|---|---|---|
|Receptor|24 h|Anual|24 h|Anual|Anual|
|RH4|0,0657198|0,0657197|0,0389177|0,0389176|0,010441|
|RH5|0,1108893|0,1108893|0,0666957|0,0666958|0,013265|
|RH6|0,0896529|0,0896530|0,0544217|0,0544216|0,007981|
|RH7|0,0548798|0,0548797|0,0333499|0,0333499|0,002831|

Fuente: Elaboración propia.

A continuación, se presentan los mapas de isoconcentraciones asociados a cada uno de los

parámetros para el material particulado MP10, MP2,5 y MPS, tanto para las concentraciones anuales

como para las concentraciones diarias.

Figura 25. Mapa de isoconcentraciones de MP10 promedio anual

Fuente: Elaboración propia.

Página 36 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 26. Mapa de isoconcentraciones de MP10 promedio 24h

Fuente: Elaboración propia.

Figura 27. Mapa de isoconcentraciones de MP2.5 promedio anual

Fuente: Elaboración propia.

Página 37 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 28. Mapa de isoconcentraciones de MP2.5 promedio 24h

Fuente: Elaboración propia.

Página 38 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 29. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio anual

Fuente: Elaboración propia.

6 Análisis de incertidumbre modelo WRF

Para validar los resultados del modelo WRF, a continuación, se presenta un Análisis de Incertidumbre,

de acuerdo con los lineamientos de la “Guía para el uso de Modelos de Calidad del Aire en el SEIA”

(SEA, 2023). Para efectos de la Guía se indica que la incertidumbre será expresada a través de las

diferencias, tanto cualitativas como cuantitativas, entre los datos modelados y observados en el

dominio de modelación. Es imprescindible analizar la incertidumbre del modelo meteorológico para

expresar cuán “válida” es la simulación de la dispersión de contaminantes respecto a la información

disponible al momento de presentar un proyecto en el SEIA.

6.1 Análisis cualitativo

A continuación, para la variable meteorológica velocidad del viento, en la siguiente Ilustración, se

presentan la comparación de los ciclos diarios junto con los ciclos mensuales.

Página 39 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

En relación al ciclo diario de la velocidad del viento observada y modelada, es posible indicar que el

modelo se adapta de buena forma a la realidad, ya que logra reproducir la variación promedio a

través de las horas del día.

Página 40 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Con respecto a la dirección del viento, a continuación, se analizan las rosas de los vientos para el

escenario modelado y observado. Tal como puede observarse, el modelo predice las componentes

observadas durante el año 2022, sin embargo, se aprecia que el modelo tiende a subestimar la

frecuencia de los vientos en dirección Norte (N).

Página 41 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

En relación a la temperatura observada y modelada, es posible indicar que el modelo se adapta de

buena forma a la realidad, ya que logra reproducir la variación promedio mensual de temperatura.

Página 42 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

6.2 Análisis cuantitativo

Según establece la “Guía para el uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2023), el análisis

cuantitativo se debe realizar calculando como mínimo las métricas estadísticas del sesgo (error medio

o BIAS), error absoluto medio (MAE) y la raíz del error cuadrático medio (RMSE). Tanto BIAS como

MAE son estimadores de la diferencia entre el valor modelado y observado de un mismo fenómeno,

en este caso meteorológico. De igual forma, RMSE es un estimador de la frecuencia de las diferencias

entre los valores observados y modelados, siendo especialmente sensible a los valores atípicos, por

lo tanto, a mayor diferencia entre estos valores menor será el grado de ajuste de este estadístico.

Adicionalmente, la “Guía para el uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2023),

recomienda incorporar el coeficiente de correlación (r), que corresponde a una medida de la

correlación lineal entre dos conjuntos de variables, siendo para este caso, los valores modelados y

observados.

A continuación, se presentan los parámetros estadísticos calculados entre los valores observados de

velocidad del viendo y los valores modelados.

Tabla 9. Análisis de incertidumbre cuantitativo velocidad del viento

|Estadístico|Valor|Valor aceptable según “Guía para el<br>uso de Modelos de Calidad del Aire<br>en el SEIA” (SEA, 2023).|Cumplimiento|
|---|---|---|---|
|BIAS|0,74 (m/s)|[-2,5 ; 2,5] (m/s)|Cumple|
|MAE|0,97 (m/s)|≤3 (m/s)|Cumple|
|RMSE|1,37 (m/s)|≤3,5 (m/s)|Cumple|
|Coeficiente de<br>correlación (r)|0,77|>0,6|Cumple|

Fuente: Elaboración propia.

Se establece que las diferencias entre valores modelados y observados de velocidad del viento están

dentro de un rango aceptable, considerando que los estadísticos BIAS, MAE y RMSE presentan valores
por debajo de los 1,37 m/s. Adicionalmente. se observa un coeficiente de correlación de 0,77 entre

valores modelados y observados, lo que permite concluir que el modelo WRF se ajusta

satisfactoriamente a los valores observados en cuanto a la velocidad del viento.

Por otra parte, a continuación, se presenta el análisis de incertidumbre para la temperatura.

Página 43 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Tabla 10. Análisis de incertidumbre cuantitativo temperatura

|Estadístico|Valor|Valor aceptable según “Guía para el<br>uso de Modelos de Calidad del Aire<br>en el SEIA” (SEA, 2023).|Cumplimiento|
|---|---|---|---|
|BIAS|1,08 (°C)|[-4 ; 4] (°C)|Cumple|
|MAE|2,88 (°C)|≤4 (°C)|Cumple|
|RMSE|4,37 (°C)|≤4,5 (°C)|Cumple|
|Coeficiente de<br>correlación (r)|0,88|>0,8|Cumple|

Fuente: Elaboración propia.

Se establece que las diferencias entre valores modelados y observados para la temperatura están

dentro de un rango aceptable, considerando que los estadísticos BIAS, MAE y RMSE presentan valores

por debajo de los 4,37 °C. Adicionalmente. se observa un coeficiente de correlación de 0,88 entre

valores modelados y observados, lo que permite concluir que el modelo WRF se ajusta

satisfactoriamente a los valores observados de temperatura.

7 Cuerpo normativo

7.1 Normativa nacional de calidad del aire

En el contexto legal, la normativa nacional vigente referente a las normas primarias y secundarias de

calidad del aire, aplicables a todo el territorio nacional, establecen límites máximos de concentración

de contaminantes, como se detalla en la siguiente Tabla.

Tabla 11. Cuerpo normativo

|Parámetro|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|
|MP10|Primaria|Promedio anual|50 μg/m3|DS N°12/2022 MMA|
|MP10|Primaria|Promedio 24 horas<br>(Percentil 98)|130 μg/m3|130 μg/m3|
|MP2.5|Primaria|Promedio anual|20 μg/m3|DS N°12/2012 MMA|
|MP2.5|Primaria|Promedio 24 horas<br>(Percentil 98)|50 μg/m3|50 μg/m3|

Fuente: Elaboración propia en base a MINSEGPRES (2002), MINSEGPRES (2010), MMA (2011), MMA (2018),

MMA (2022).

7.2 Normativa internacional de referencia

Con respecto al contaminante MPS no existe normativa nacional aplicable a la ubicación del Proyecto,

por lo tanto, se utilizará una norma de referencia internacional para comparar las emisiones de este

Página 44 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

contaminante. De acuerdo a lo establecido en el artículo 11 del DS N°40/2012 del SEIA, para la

utilización de las normas de referencia, se priorizará aquel Estado que posea similitud en sus
componentes ambientales, con la situación nacional y/o local, por ello se consideró utilizar la

normativa de la Confederación Suiza. A continuación, se justifica su utilización:

- Normativa Confederación Suiza:

En términos climáticos, según la clasificación climática de Köppen, Chile presenta los siguientes

climas: Desértico (BWh, BWk), Semiárido (BWk, BSk), Mediterráneo (Csa, Csb), Tropical (Cfa),

Templado oceánico (Cfb), Subpolar oceánico (Cfc), Semiárido (Bsk), Alpino, Tundra (ET) y Clima polar

(EF), en tanto Suiza presenta los siguientes climas: Semiárido (BSh, Bsk), Templado oceánico (Cfb),

Subpolar oceánico (Cfc), Tropical (Cfa), Boreal (Dfc), Alpino, Tundra (ET) y Polar (EF) (Koppen, 1918).

De acuerdo a lo anterior, ambos países comparten 7 tipos de climas, siendo el clima templado

oceánico (Cfb) el más representativo.

En términos de especies vegetales, es posible afirmar que, en Suiza, se catalogan alrededor de 2592

especies de flora vascular, de las cuales 790 (30,5%) se encuentran en alguna categoría de amenaza

(Cordillot & Klaus, 2011), en tanto para Chile se reconocen alrededor de 5471 plantas vasculares de

las cuales 443 (8,1%), están en alguna categoría de amenaza (Rodríguez et al, 2018).

Por otro lado, la Ordenanza que establece la norma de calidad de aire para la Confederación Suiza

indica en su Capítulo 1, artículo 1 que: “La norma está orientada a proteger seres humanos, animales

y plantas, sus comunidades biológicas y hábitats, y el suelo, de los efectos dañinos o perjuicios

causados por la contaminación del aire”. Mientras que en su artículo 2 define “Los niveles de

contaminación del aire son excesivos si uno o más de los valores límite para un contaminante

especificado en el anexo 7 es excedido. En caso que el valor límite para un contaminante no este

especificado, se considerará excesivo si:

`o` Ponen en peligro a seres humanos, animales, plantas o sus comunidades biológicas

o hábitats.

`o` Un estudio establezca que afecta significativamente el bienestar de una proporción

sustancial de la población.

`o` Provoque daño a edificaciones.

`o` Dañe la fertilidad del suelo, vegetación o aguas.”

Conforme a lo anterior, es posible concluir que Chile y Suiza presentan una composición climática

relativamente similar en tanto, la magnitud de plantas vasculares en categoría de amenaza en la

situación suiza es mayor a la chilena. Por otra parte, la norma de la Confederación Suiza, señala como

objeto de protección a las comunidades biológicas o hábitats de plantas y animales, suelo, vegetación

y aguas, lo que le otorga validez a esta norma, para ser usada como referencia en el establecimiento

de límites para contaminantes ambientales como MPS, toda vez que, en el entorno del área del

Proyecto, existe presencia de recursos naturales susceptibles de ser impactados por MPS.

Página 45 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

En el Apéndice B de este informe se incluye un ejemplar íntegro y vigente de la Ordenanza de la

Confederación Suiza sobre control de la contaminación atmosférica.

A continuación, se presenta un resumen de los límites de MPS establecidos en las normativas

internacionales a utilizar como referencia.

Tabla 12. Cuerpo normativo

|Contaminante|País|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|---|
|MPS <br>(Partículas<br>sedimentables)|Confederación<br>Suiza|-|Promedio<br>anual|200<br>(mg/m2día)|Ordenanza de la<br>Confederación<br>Suiza, Sobre Control<br>de Contaminación<br>del Aire 1993|

Página 46 de 59

Fuente: Elaboración propia.

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

8 Evaluación de impactos

8.1 Evaluación de impactos sobre la salud de la población

Siguiendo los lineamientos establecidos en la “Guía para la Evaluación de Impacto Ambiental de

Riesgo para la Salud de la Población en el SEIA” (SEA, 2023), se procede a realizar un análisis de los

aportes del Proyecto, para determinar si generan un incremento significativo en las concentraciones

de material particulado en el área de influencia.

Ruta de exposición:

Los contaminantes serán emitidos a la atmósfera directamente desde la fuente de generación, ya sea

por alguna actividad de movimiento de tierra, o mediante el funcionamiento de algún vehículo o

maquinaria que los ocasione. Los contaminantes se transportarán a través de la atmósfera, pudiendo

sedimentar si se dieran las condiciones. Los puntos de exposición de esos contaminantes se

encontrarán dentro de los límites del área del proyecto, además de las rutas externas de transporte.

La vía de exposición de estos contaminantes es por inhalación, y la población receptora corresponde

a viviendas y establecimientos de salud.

A continuación, se presenta la comparación de las emisiones del Proyecto con las normas de calidad

primaria vigentes y secundarias de referencia.

Página 47 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Tabla 13. Comparación material particulado con normas primarias de calidad del aire en Receptores humanos

|Receptor|Tipo<br>Receptor|Descripción receptores|MP10 (ug/m3)|Col5|% DS N°12/2022 MMA|Col7|MP2,5 (ug/m3)|Col9|% DS N°12/2012 MMA|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Tipo<br>Receptor|Descripción receptores|24 horas|Anual|24 horas|Anual|24 horas|Anual|24 horas|Anual|
|R2|Humano|Viviendas|0,1062904|0,1062902|0,082%|0,213%|0,0645800|0,0645800|0,129%|0,323%|
|R3|Humano|Posta de Salud Pullally|0,0386698|0,0386697|0,030%|0,077%|0,0232327|0,0232327|0,046%|0,116%|
|R4|Humano|Viviendas Papudo|0,0424391|0,0424391|0,033%|0,085%|0,0257205|0,0257205|0,051%|0,129%|
|R6|Humano|Viviendas La Ligua|0,0156795|0,0156796|0,012%|0,031%|0,0095484|0,0095484|0,019%|0,048%|
|R7|Humano|Viviendas La Ligua|0,0128282|0,0128282|0,010%|0,026%|0,0078163|0,0078163|0,016%|0,039%|
|R14|Humano|Viviendas|0,0872357|0,0872357|0,067%|0,174%|0,0530937|0,0530937|0,106%|0,265%|
|R15|Humano|Viviendas|0,0556857|0,0556857|0,043%|0,111%|0,0339093|0,0339092|0,068%|0,170%|
|RH2|Grupos<br>humanos|Vivienda/Almacén en<br>área rural|0,0597675|0,0597675|0,046%|0,120%|0,0360522|0,0360522|0,072%|0,180%|
|RH3|Grupos<br>humanos|Vivienda en área rural|0,0372633|0,0372632|0,029%|0,075%|0,0218390|0,0218391|0,044%|0,109%|
|RH4|Grupos<br>humanos|Vivienda en área rural|0,0657198|0,0657197|0,051%|0,131%|0,0389177|0,0389176|0,078%|0,195%|
|RH5|Grupos<br>humanos|Vivienda/Almacén en<br>área rural|0,1108893|0,1108893|0,085%|0,222%|0,0666957|0,0666958|0,133%|0,333%|
|RH6|Grupos<br>humanos|Vivienda en área rural|0,0896529|0,0896530|0,069%|0,179%|0,0544217|0,0544216|0,109%|0,272%|
|RH7|Grupos<br>humanos|Vivienda en área rural|0,0548798|0,0548797|0,042%|0,110%|0,0333499|0,0333499|0,067%|0,167%|

Fuente: Elaboración propia.

Página 48 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Según los resultados de la modelación de dispersión atmosférica del material particulado generado

durante el primer año del proyecto, se ha determinado que las concentraciones resultantes son de

baja magnitud. El receptor humano donde se presentarán mayores concentraciones de material
particulado será RH5, cuya concentración promedio de MP10 anual será de 0,111 μg/m [3], lo cual
representa aproximadamente el 0,085% del límite establecido por la normativa D.S. N°12/22 MMA.

Para el caso del MP10 en 24 horas, el Proyecto representa un máximo del 0,222% de la norma en 24
horas establecida en el D.S. N°12/22 MMA. En relación al MP2.5, el Proyecto alcanza como máximo
el 0,333% del límite anual establecido por la norma D.S. N°12/11 MMA, en el receptor humano RH5.

Por lo tanto, las emisiones del Proyecto representan menos del 1% de los umbrales establecidos en

las normas de calidad primaria del aire para material particulado MP10 y MP2.5 en los receptores

humanos.

En conclusión, de acuerdo a lo expuesto, se puede afirmar que la ejecución del Proyecto en cuanto a

las concentraciones de material particulado no generará un impacto significativo en la salud de las

personas, ya que no excede los límites establecidos por las normas de calidad primaria del aire, que

tienen como objetivo proteger la salud de la población.

En base a lo anterior es posible afirmar que el Proyecto genera un aumento marginal y despreciable

en las concentraciones de material particulado producto a las emisiones acotadas a la fase de

construcción del Proyecto, por lo tanto, no se generará una modificación en la calidad del aire de la

zona, de manera que el Proyecto no genera riesgos a la salud de población.

8.2 Evaluación de impactos sobre la calidad del aire, flora y vegetación, fauna, aguas superficiales

y suelo

A continuación, se procede a realizar un análisis de los aportes del proyecto en su etapa de

construcción, para determinar si el proyecto generará efectos adversos significativos sobre la calidad

del aire, flora y vegetación, fauna, aguas superficiales y suelo, según los lineamientos establecidos en

la “Guía de evaluación de efectos adversos sobre recursos naturales renovables” (SEA, 2022).

La siguiente Tabla presenta una lista de potenciales impactos que el Proyecto puede generar o

presentar sobre la calidad del aire.

Tabla 14. Potenciales impactos sobre componente calidad del aire

|Recurso|Impacto|Posibles impactos|
|---|---|---|
|Aire|Impactos en la calidad del<br>aire|• <br>Posible aumento en la concentración de material particulado<br>en el área de influencia.|
|Aire|Impacto en la calidad del<br>aire que ocasiona<br>impactos sobre otro<br>recurso natural renovable|• <br>El impacto en la calidad del aire producto del aumento de<br>concentraciones de contaminantes, ocasionar impactos sobre<br>ciertas poblaciones de especies de flora y fauna, así como<br>también sobre la calidad del suelo y cultivos.|

Página 49 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Recurso|Impacto|Posibles impactos|
|---|---|---|
|||~~•~~ <br>El impacto en la calidad del aire producto del aumento de<br>concentraciones de material particulado sedimentable puede<br>producir depositación de contaminantes en la vegetación.|
||Impacto en un recurso<br>natural renovable que<br>causa impacto en otros<br>componentes del artículo<br>11 de la Ley 19.300|• <br>Un impacto sobre la calidad del aire, debido a las emisiones<br>atmosféricas del proyecto, puede generar riesgo para la salud<br>de la población, señalado en la letra a) del artículo 11 de la Ley<br>N° 19.300.<br>• <br>Un impacto sobre la calidad del aire, debido a las emisiones<br>atmosféricas del proyecto, puede producir depositación de<br>contaminantes en la vegetación utilizada como sustento<br>económico de grupos humanos, ocasionando una alteración<br>en los sistemas de vida y costumbres de dicho grupo.|

Fuente: Elaboración propia.

Al respecto, a continuación, se presenta el análisis del cumplimiento de la norma de calidad

secundaria para MPS con respecto a los receptores correspondientes a recursos naturales.

Tabla 15. Comparación material particulado con normas de calidad secundarias de calidad del aire

|Receptor|Tipo Receptor|Descripción<br>receptores|MPS (mg/m2/día)|Norma<br>confederación Suiza|
|---|---|---|---|---|
|Receptor|Tipo Receptor|Descripción<br>receptores|Anual|Anual|
|R1|Red Hidrográfica|Río La Ligua|0,0000|0,000%|
|R5|Red Hidrográfica|Estero Jaruro|0,0000|0,000%|
|R8|Atractivo Turístico|Camino<br>Longotoma-La<br>ligua|0,0000|0,000%|
|R9|Santuario de la<br>naturaleza|Humedal Salinas<br>de Pullally - Dunas<br>de Longotoma|0,0000|0,000%|
|R10|Atractivo Turístico|Longotoma|0,0000|0,000%|
|R11|Sitio Prioritario|Estuario Río La<br>Ligua|0,0000|0,000%|
|R12|Sitio Prioritario|Papudo|0,0000|0,000%|
|R13|Agrícola|Cultivos|0,0000|0,000%|
|RH1|Industrial|Recinto antena<br>telefónica|0,0052|0,003%|

Fuente: Elaboración propia.

A continuación, se presenta la evaluación de los posibles impactos identificados en la Tabla anterior.

Página 50 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Col1|Col2|Tabla 16. Evaluación de impactos|Col4|
|---|---|---|---|
|Recurso|Potencial<br>impacto|Evaluación cualitativa|Evaluación cuantitativa|
|Aire|Impactos en<br>la calidad del<br>aire|Las emisiones de Material Particulado<br>(MP10, MP2.5 y MPS) que generará el<br>Proyecto no ocasionarán un impacto<br>significativo sobre la capacidad del aire,<br>para<br>mantener<br>las<br>funciones<br>de<br>procreación,<br>reproducción,<br>crecimiento,<br>transformación<br>o <br>restablecimiento de recursos naturales,<br>debido a que las normas de calidad<br>primarias y secundarias no se ven<br>sobrepasadas con las emisiones del<br>Proyecto durante el año de mayor<br>emisión.<br> <br>Adicionalmente es importante destacar<br>que las mayores tasas de emisión se<br>generarán durante el año 1 del<br>Proyecto, el cual considera la fase de<br>construcción.|Las emisiones que generará el<br>Proyecto representan menos del<br>0,4% de los límites establecidos en<br>las normas de calidad primaria para<br>material particulado en todos los<br>receptores humanos identificados,<br>y el 0,003% de las normas de<br>calidad secundaria del aire para<br>MPS<br>en<br>los<br>receptores<br>correspondientes<br>a <br>recursos<br>naturales.|
|Aire|Impacto en la<br>calidad<br>del<br>aire<br>que<br>ocasiona<br>impactos<br>sobre<br>otro<br>recurso<br>natural<br>renovable|Se<br>establece<br>que<br>las<br>emisiones<br>partículas que generará el Proyecto<br>(MP10, MP2.5 y MPS), no ocasionarán<br>un impacto significativo sobre la<br>vegetación, cultivos cercanos, cursos de<br>agua, flora, fauna u otros recursos<br>naturales de la zona debido a que las<br>normas<br>de<br>calidad<br>secundarias<br>utilizadas como referencia (Norma<br>Confederación<br>Suiza),<br>no<br>se ven<br>sobrepasadas con las emisiones del<br>Proyecto, considerando que las normas<br>de calidad secundaria apuntan a<br>proteger los recursos naturales. Por lo<br>tanto, se puede concluir que, a nivel de<br>calidad del aire, el Proyecto no genera<br>un impacto significativo en la calidad de<br>los recursos naturales del área de<br>influencia.<br> <br>Adicionalmente es importante destacar<br>que las mayores tasas de emisión se<br>generarán durante el año 1 del<br>Proyecto, el cual considera la fase de<br>construcción.|<br>En los receptores correspondientes<br>a recursos naturales las emisiones<br>de MPS que generará el Proyecto<br>representan el 0,0,03% de los<br>límites establecidos en la norma de<br>calidad secundaria del aire. Por lo<br>tanto, no se ocasiona un impacto<br>significativo sobre los recursos<br>naturales cercanos.|

Página 51 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

|Recurso|Potencial<br>impacto|Evaluación cualitativa|Evaluación cuantitativa|
|---|---|---|---|
||Impacto en un<br>recurso<br>natural<br>renovable<br>que<br>causa<br>impacto<br>en<br>otros<br>componentes<br>del artículo 11<br>de<br>la<br>Ley<br>19.300|Se<br>establece<br>que<br>las<br>emisiones<br>partículas que generará el Proyecto<br>(MP10, MP2.5 y MPS), no ocasionarán<br>un impacto significativo sobre la<br>vegetación, cultivos cercanos, cursos de<br>agua, flora, fauna u otros recursos<br>naturales de la zona debido a que las<br>normas<br>de<br>calidad<br>secundarias<br>utilizadas como referencia (Norma<br>Confederación<br>Suiza),<br>no<br>se ven<br>sobrepasadas con las emisiones del<br>Proyecto, considerando que las normas<br>de calidad secundaria apuntan a<br>proteger los recursos naturales. Por lo<br>tanto, se puede concluir que, a nivel de<br>calidad del aire, el Proyecto no genera<br>un impacto significativo en la calidad de<br>los recursos naturales del área de<br>influencia.<br> <br>Adicionalmente es importante destacar<br>que las mayores tasas de emisión se<br>generarán durante el año 1 del<br>Proyecto, el cual considera la fase de<br>construcción.<br>|<br>En los receptores correspondientes<br>a recursos naturales las emisiones<br>de MPS que generará el Proyecto<br>representan el 0,03% de los límites<br>establecidos en la norma de calidad<br>secundaria del aire. Por lo tanto, no<br>se ocasiona un impacto significativo<br>sobre<br>los<br>recursos<br>naturales<br>cercanos.|

Fuente: Elaboración propia.

En términos de calidad y cantidad, se establece que el Proyecto no genera efectos adversos

significativos en los recursos naturales mencionados: aire, flora y vegetación, fauna, aguas

superficiales y suelo, considerando que las condiciones que permiten la presencia y desarrollo de

especies y la funcionalidad de los ecosistemas dependientes de la calidad del aire en la zona no se

ven afectadas por la presencia del Proyecto.

Además, no se produce una modificación sustancial en la composición, estructura o funcionamiento

del ecosistema que impida la manifestación de los procesos e interrelaciones característicos. Esto se

debe a que el Proyecto no supera los límites establecidos en las normas de calidad del aire (tanto

primarias como secundarias) y las tasas de emisión del Proyecto se mantienen por debajo del 0,2%

de dichos límites, según las regulaciones aplicables.

En consecuencia, se puede afirmar que el ecosistema original se mantiene sin cambios significativos

debido a las emisiones atmosféricas generadas por el Proyecto. Por lo tanto, la ejecución del Proyecto

no afecta la permanencia ni la capacidad de generación de los recursos naturales mencionados: aire,

flora y vegetación, fauna, aguas superficiales y suelo. Esto implica que la disponibilidad, utilización y

aprovechamiento racional futuro de dichos recursos no se ven comprometidos. Asimismo, la

Página 52 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

capacidad de regeneración y renovación de estos recursos no se ve alterada por la ejecución del

Proyecto.

En resumen, se concluye que las emisiones atmosféricas generadas por el Proyecto no tienen un

impacto significativo en los recursos naturales mencionados y no comprometen su disponibilidad,

utilización, aprovechamiento racional ni su capacidad de regeneración o renovación.

9 Área de influencia

El área de influencia corresponde al espacio geográfico cuyos atributos, elementos naturales o

socioculturales deben ser considerados con la finalidad de definir si el proyecto o actividad genera o

presenta alguno de los efectos, características o circunstancias del Artículo 11 de la Ley N° 19.300, o

bien para justificar su inexistencia (Ref. letra a) del Artículo 2 del Reglamento del SEIA).

Dada esta definición, se efectuó una delimitación del área de influencia considerando los siguientes
factores y criterios definidos en la “Guía Área de Influencia en el Sistema de Evaluación de Impacto

Ambiental” (SEA, 2017) y “Guía Calidad del aire en el área de influencia de proyectos que ingresan al

SEIA (SEA, 2015):

 - El área de influencia debe comprender el espacio desde donde se generan las emisiones

(fuente de la emisión) más el comprendido por la dispersión de contaminantes emitidos. Por

su parte, para predecir y evaluar el riesgo para la salud de la población, el AI del elemento

‘salud de la población’ debe comprender el espacio con presencia de población expuesta a

los contaminantes emitidos por el Proyecto.

 - Las partículas sedimentables de los contaminantes de dichas emisiones pueden depositarse

en el suelo y vegetación, por lo tanto, el área de influencia de estos elementos comprende

el área o espacio geográfico donde dicho material se sedimenta.

 - Aporte de contaminantes debido a la construcción y operación del Proyecto, cuyos

antecedentes fueron obtenidos a través de la modelación de MP10, MP2.5, y MPS.

 - Distancia de receptores de interés cercanos al Proyecto.

Con todo lo anterior, se definió un Área de influencia para la componente calidad del aire asociado a

los contaminantes atmosféricos, extendiéndose en un radio de 1700 m alrededor del Proyecto,

considerando que las máximas concentraciones de contaminantes se perciben a 830 m de este.

Además, a la distancia de 1700 m desde las obras ejecutadas, las concentraciones de todos los

contaminantes generados están por debajo del 1% de los límites máximos establecidos en las

normativas de calidad del aire.

A continuación, se presenta una figura que detallada el Área de Influencia del Proyecto con respecto

al componente calidad del aire. En el Apéndice C se presenta un kmz con esta área.

Página 53 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

Figura 30. Área de influencia calidad del aire

Fuente: Elaboración propia.

Página 54 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

10 Conclusiones

Los resultados de la modelación de las concentraciones de contaminantes atmosféricos a distintas

distancias desde el Proyecto, muestran que los mayores aportes se producen hasta una distancia de

830 metros del Proyecto, durante el primer año del Proyecto, correspondiente a la fase de

construcción.

De esta forma, se delimitó un área de influencia de la calidad del aire, con la concentración

correspondiente a un 1% del valor de las normas de calidad del aire para los contaminantes

atmosféricos MP10, MP2.5 y MPS. Por lo tanto, el área de influencia quedó definida hasta una

distancia de 100 metros desde el perímetro del Proyecto.

El receptor humano donde se presentarán mayores concentraciones de material particulado será
RH5, cuyas concentración promedio de MP10 anual será de 0,111 μg/m [3], lo cual representa
aproximadamente el 0,085% del límite establecido por la normativa D.S. N°12/22 MMA. Para el caso

del MP10 en 24 horas, el Proyecto representa un máximo del 0,222% de la norma en 24 horas
establecida en el D.S. N°12/22 MMA. En relación al MP2.5, el Proyecto alcanza como máximo el
0,333% del límite anual establecido por la norma D.S. N°12/11 MMA, en el receptor humano RH5.

Por lo tanto, las emisiones del Proyecto representan menos del 1% de los umbrales establecidos en

las normas de calidad primaria del aire para material particulado MP10 y MP2.5 en los receptores

humanos.

Respecto a la depositación de MPS, se establece que las emisiones del Proyecto representan el

0,003% de las normativas secundarias de referencia de calidad del aire para MPS en los receptores

relacionados con recursos naturales y medio ambiente, de manera que el Proyecto no generará un

impacto significativo debido a la depositación de material particulado y no afectará la vegetación ni

cultivos cercanos, ni flora o fauna presente en el área de influencia.

Por lo tanto, es posible inferir que las emisiones asociadas a la fase de construcción del Proyecto no

se afectará la calidad del aire en los receptores cercanos, dado que las emisiones atmosféricas del

Proyecto no sobrepasan los límites de concentración establecidos en las normas de calidad del aire

primarias y secundarias, además es importante destacar que para efectos de la modelación se

consideró la simultaneidad en la construcción de las obras (en la práctica la construcción del Proyecto

no es simultánea, puesto que las actividades constructivas son realizadas de forma secuencial).

Expuesto lo detallado, se determina que el Proyecto Parque Fotovoltaico Leones Solar, no genera un

efecto adverso significativo, ni un impacto adverso para la salud de las personas ni en calidad del aire

y tampoco en las poblaciones cercanas, ni en los cultivos aledaños, ni en los recursos naturales de la

zona, ya que no sobrepasa los límites establecidos en las normativas de calidad primaria tanto sus

criterios diarios y anuales, teniendo en cuenta que los límites establecidos en las normas de calidad

primaria apuntan a proteger la salud de la población, es por esto que estas normas establecen límites

más estrictos que las normas de calidad secundaria, de igual manera las emisiones del Proyecto

cumplen con las normas de calidad secundaria, las cuales apuntan a proteger el medio ambiente. Es

Página 55 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

importante considerar, además, que las emisiones atmosféricas generadas tanto generadas en el Año

1 tendrán una duración acotada.

En base a lo anterior es posible afirmar que el Proyecto genera un aumento marginal y despreciable

en las concentraciones de contaminantes atmosféricos producto a las emisiones acotadas a la fase

de construcción y operación, por lo tanto, no se generará una modificación en la calidad del aire de

la zona, de manera que el Proyecto no genera riesgos adicionales a la salud de población.

Página 56 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

11 Bibliografía

- Cámara Chilena de la Construcción CCHC (s.f.). _Manual de la construcción limpia_, Tema N° 2
Control de polvo en obras en construcción.

- Caterpillar. (2017). _Caterpillar Performance Handbook._

- Confederación Suiza. (1993). _Ordenanza de la Confederación Suiza, Sobre Control de_

_Contaminación del Aire._

- COPEC. (2021). _Especificaciones Diesel._ Recuperado el 1 de abril de 2021, desde:
https://ww2.copec.cl/combustibles/products/diesel-ultra.

- Cordillot, F. & Klaus, G. (2011). _Gefährdete Arten in der Schweiz. Synthese Rote Listen, Stand 2010._

_Bundesamt für Umwelt, Bern._

- Decreto N°12/2010, Establece Norma de calidad del aire para MP2.5, Ministerio del Medio

Ambiente. Diario Oficial de la República de Chile, 9 de mayo de 2011, Santiago, Chile.

- Decreto N°22/2010, Establece norma de calidad secundaria de aire para anhídrido sulfuroso

(SO2), Ministerio Secretaría General de la Presidencia. Diario Oficial de la República de Chile, 16

de abril de 2010, Santiago, Chile.

- Decreto N°114/2002, Establece Norma de calidad del aire para NO2, Ministerio Secretaría

General de la Presidencia. Diario Oficial de la República de Chile, 6 de marzo de 2003, Santiago,

Chile.

- Decreto N°115/2002, Establece Norma de calidad del aire para CO, Ministerio Secretaría General

de la Presidencia. Diario Oficial de la República de Chile, 10 de septiembre de 2002, Santiago,

Chile.

- Decreto N°104/2018, Establece Norma de calidad del aire para SO2, Ministerio del Medio

Ambiente. Diario Oficial de la República de Chile, 16 de mayo de 2019, Santiago, Chile.

- Decreto N°12/2022, Establece Norma de calidad ambiental para material particulado respirable

MP10, Ministerio del Medio Ambiente. Diario Oficial de la República de Chile, 4 de junio de 2022,

Santiago, Chile.

- Decreto N°1074/2018. Aprueba la reglamentación de la Ley 5965 de protección a las fuentes de
provisión y a los cursos y cuerpos receptores de agua y a la atmósfera. Deroga el DEC.3395/96.

Designa autoridad de aplicación al Organismo Provincial para el Desarrollo Sostenible (OPD).

Gobierno de la Provincia de Buenos Aires. Boletín Oficial de la República Argentina, 5 de octubre

de 2018, Buenos Aires, Argentina.

- Department for Environment, Food and Rural Affairs [DEFRA]. (2014). _What are the causes of air_

_Pollution. United Kingdom Government._

- Díaz, V. y Páez C. (2006). _Contaminación por material particulado en Quito y caracterización_

_química de las muestras._ Corporación para el Mejoramiento del Aire de Quito. Revista Acta Nova

Vol.3, Nro 2.

- EMEP/EEA. (2019). _Air Pollutant Emission Inventory Guidebook, Ch. 1.A.4 Non Road Mobile_
_Machinery._

Página 57 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

- ENAP. (2022). _Petróleo Diesel Grado A1._

- EPA. (s.f.). _AP-42, Fifth Edition Compilation of Air Pollutant Emission Factors, Volume 1: Stationary_

_Point and Area Sources._

- EPA. (1996). _Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition, Ch. 3.3 Gasoline_
_and Diesel Industrial Engines._

- EPA. (1998a). _“Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition, Ch.11.9 Western_
_surface coal mining”._

- EPA. (1998b). _Screening procedures for estimating the air quality impact of stationary sources,_

- EPA. (2000). _Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition, Ch.3 Stationary_

_Internal Combustion Sources._

- EPA. (2002). _Median Life, Annual Activity, and Load Factor Values for Nonroad Engine Emissions_
_Modeling._

- EPA. (2006a). _Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition, Ch.13.2.2 Unpaved_

_Roads._

- EPA. (2006b). _Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition, Ch.13.2.4_
_Aggregate Handling and Storage Piles._

- EPA. (2011). _Compilation of air emission factor, AP-42”: Chapter 13, Section 13.2.1 “Paved Road”._

- Explorador Eólico. (2021).

- Figueruelo, J. y Marino, M. (2004). _Química Física del Ambiente y de los Procesos_

_Medioambientales_

- Google Earth Pro (2023). _Perfiles de elevación._

- Grossi, M., Gutierréz, D. & Deluchi, G. (2013). _Una mirada sobre el estado actual de la_

_conservación de la flora Argentina._

- INN Chile. (2000). _NCh 353.Of2000 "Construcción - Cubicación de obras de edificación -_
_Requisitos._

- Koppen, W. (1918). _Clasificación de climas según temperatura, precipitación y ciclo estacional._

- Lakes Environmental. (2006). _CALPUF View Leading interface for puff dispersion._

- MMA. (2017). _Manual para el Desarrollo de Inventarios de Emisiones Atmosféricas._

- Organización Mundial de la Salud [OMS]. (2006). _Guías de calidad del aire de la OMS relativas al_

_material particulado, el ozono, el dióxido de nitrógeno y el dióxido de azufre._

- Rodriguez, R., Marticorena, C., Alarcón, D., Baeza, D., Cavieres, L., Finot, L., Fuentes, N., Kiessling,

A., Mihoc, M., Pauchard, A., Ruiz, E., Sanchez, P. & Marticorena, A. (2018). _Catálogo de las plantas_

_vasculares de Chile._

Página 58 de 59

Declaración de Impacto Ambiental
Proyecto Parque Fotovoltaico Leones Solar

- SEA. (2022). _Guía de evaluación de efectos adversos sobre recursos naturales renovables._

- SEA, (2022). _Criterio de Evaluación en el SEIA: Objetos de protección._

- SEA. (2023). _Guía para el uso de modelos de calidad del aire en el SEIA._

- SINCA. (2023). Sistema de Información Nacional de Calidad del Aire, información histórica.

- Vargas, C. (2011). _Efectos de la fracción gruesa (PM10-2.5) del material particulado sobre la salud_

_humana._ Ministerio de Salud del Gobierno de Chile.

Página 59 de 59

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Construcción detalle del dominio de los datos meteorológicos**

| Periodo de datos de los datos | 1 enero a 31 de diciembre de 2022 |
| --- | --- |
| Punto de Referencia | Latitud: - 32.392 S<br>Longitud: - 71.343 W |
| Área de Dominio | 50x50 km |
| Proyección | Lambert Conic Conformal |
| Datum | NWS-84 6370 km Radius, Global Sphere |

**Tabla 2.: Resumen tasa de emisiones atmosféricas para el año 1**

| Contami<br>nante | Resultados estimación de emisiones | Col3 | Col4 | Col5 | Datos entrada CALPUFF | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contami<br>nante | Área<br>Proyecto | LAT | Caminos<br>No<br>pavimenta<br>dos | Caminos<br>pavimentad<br>os | Área<br>Proyecto | LAT | Caminos<br>pavimentad<br>os | Caminos<br>No<br>pavimenta<br>dos |
| Unidad | t/año | t/año | t/año | t/año | g/s/m2 | g/s/m2 | g/s/m | g/s/m |
| MP10 | 1,2259 | 0,0055 | 2,0822 | 1,5105 | 6,91E-08 | 5,00E-08 | 4,59E-09 | 2,36E-10 |
| MP2.5 | 0,7420 | 0,0028 | 0,2082 | 0,4112 | 4,19E-08 | 2,50E-08 | 4,59E-10 | 6,42E-11 |
| MPS | 1,9444 | 0,0265 | 6,8018 | 7,6146 | 1,10E-07 | 2,39E-07 | 1,50E-08 | 1,19E-09 |
| Tipo de<br>fuente | Areal | Areal | Lineal | Lineal | Areal | Areal | Lineal | Lineal |

**Tabla 4.: Estaciones caracterización meteorológica**

| Estación | Coordenadas UTM | Col3 | Variables Meteorológicas<br>Registradas |
| --- | --- | --- | --- |
| Estación | Este (m) | Norte (m) | Norte (m) |
| Estación Catapilco<br>Zapallar | 286647 | 6393218 | Dirección del viento<br>Velocidad del viento<br>Temperatura |

**Tabla 5.: Estación Bomberos**

| Variable | Año | N° Registros válidos | % Registros válidos |
| --- | --- | --- | --- |
| Dirección del viento | 2022 | 7890 | 95% |
| Velocidad del viento | 2022 | 8060 | 96% |
| Temperatura | 2022 | 8060 | 96% |

**Tabla 8.: Resultados modelación año 1 material particulado**

| Receptor | MP10 (μg/m3) | Col3 | MP2,5 (μg/m3) | Col5 | MPS<br>(mg/m2/día) |
| --- | --- | --- | --- | --- | --- |
| Receptor | 24 h | Anual | 24 h | Anual | Anual |
| R1 | 0,1761602 | 0,1761603 | 0,1069572 | 0,1069571 | 0,000000 |
| R2 | 0,1062904 | 0,1062902 | 0,0645800 | 0,0645800 | 0,000000 |
| R3 | 0,0386698 | 0,0386697 | 0,0232327 | 0,0232327 | 0,000000 |
| R4 | 0,0424391 | 0,0424391 | 0,0257205 | 0,0257205 | 0,000000 |
| R5 | 0,0907580 | 0,0907579 | 0,0550190 | 0,0550190 | 0,000000 |
| R6 | 0,0156795 | 0,0156796 | 0,0095484 | 0,0095484 | 0,000000 |
| R7 | 0,0128282 | 0,0128282 | 0,0078163 | 0,0078163 | 0,000000 |
| R8 | 0,0267774 | 0,0267773 | 0,0162790 | 0,0162790 | 0,000000 |
| R9 | 0,0496211 | 0,0496211 | 0,0302657 | 0,0302656 | 0,000000 |
| R10 | 0,0080107 | 0,0080107 | 0,0048866 | 0,0048866 | 0,000000 |
| R11 | 0,0073069 | 0,0073069 | 0,0044579 | 0,0044579 | 0,000000 |
| R12 | 0,0084828 | 0,0084828 | 0,0051847 | 0,0051847 | 0,000000 |
| R13 | 0,1322659 | 0,1322661 | 0,0804084 | 0,0804083 | 0,000000 |
| R14 | 0,0872357 | 0,0872357 | 0,0530937 | 0,0530937 | 0,000000 |
| R15 | 0,0556857 | 0,0556857 | 0,0339093 | 0,0339092 | 0,000000 |
| RH1 | 0,1090110 | 0,1090109 | 0,0662797 | 0,0662797 | 0,005166 |
| RH2 | 0,0597675 | 0,0597675 | 0,0360522 | 0,0360522 | 0,005041 |
| RH3 | 0,0372633 | 0,0372632 | 0,0218390 | 0,0218391 | 0,008782 |

**Tabla 9.: Análisis de incertidumbre cuantitativo velocidad del viento**

| Estadístico | Valor | Valor aceptable según “Guía para el<br>uso de Modelos de Calidad del Aire<br>en el SEIA” (SEA, 2023). | Cumplimiento |
| --- | --- | --- | --- |
| BIAS | 0,74 (m/s) | [-2,5 ; 2,5] (m/s) | Cumple |
| MAE | 0,97 (m/s) | ≤3 (m/s) | Cumple |
| RMSE | 1,37 (m/s) | ≤3,5 (m/s) | Cumple |
| Coeficiente de<br>correlación (r) | 0,77 | >0,6 | Cumple |

**Tabla 10.: Análisis de incertidumbre cuantitativo temperatura**

| Estadístico | Valor | Valor aceptable según “Guía para el<br>uso de Modelos de Calidad del Aire<br>en el SEIA” (SEA, 2023). | Cumplimiento |
| --- | --- | --- | --- |
| BIAS | 1,08 (°C) | [-4 ; 4] (°C) | Cumple |
| MAE | 2,88 (°C) | ≤4 (°C) | Cumple |
| RMSE | 4,37 (°C) | ≤4,5 (°C) | Cumple |
| Coeficiente de<br>correlación (r) | 0,88 | >0,8 | Cumple |

**Tabla 11.: Cuerpo normativo**

| Parámetro | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio anual | 50 μg/m3 | DS N°12/2022 MMA |
| MP10 | Primaria | Promedio 24 horas<br>(Percentil 98) | 130 μg/m3 | 130 μg/m3 |
| MP2.5 | Primaria | Promedio anual | 20 μg/m3 | DS N°12/2012 MMA |
| MP2.5 | Primaria | Promedio 24 horas<br>(Percentil 98) | 50 μg/m3 | 50 μg/m3 |

**Tabla 12.: Cuerpo normativo**

| Contaminante | País | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- | --- |
| MPS <br>(Partículas<br>sedimentables) | Confederación<br>Suiza | - | Promedio<br>anual | 200<br>(mg/m2día) | Ordenanza de la<br>Confederación<br>Suiza, Sobre Control<br>de Contaminación<br>del Aire 1993 |

**Tabla 13.: Comparación material particulado con normas primarias de calidad del aire en Receptores humanos**

| Receptor | Tipo<br>Receptor | Descripción receptores | MP10 (ug/m3) | Col5 | % DS N°12/2022 MMA | Col7 | MP2,5 (ug/m3) | Col9 | % DS N°12/2012 MMA | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Tipo<br>Receptor | Descripción receptores | 24 horas | Anual | 24 horas | Anual | 24 horas | Anual | 24 horas | Anual |
| R2 | Humano | Viviendas | 0,1062904 | 0,1062902 | 0,082% | 0,213% | 0,0645800 | 0,0645800 | 0,129% | 0,323% |
| R3 | Humano | Posta de Salud Pullally | 0,0386698 | 0,0386697 | 0,030% | 0,077% | 0,0232327 | 0,0232327 | 0,046% | 0,116% |
| R4 | Humano | Viviendas Papudo | 0,0424391 | 0,0424391 | 0,033% | 0,085% | 0,0257205 | 0,0257205 | 0,051% | 0,129% |
| R6 | Humano | Viviendas La Ligua | 0,0156795 | 0,0156796 | 0,012% | 0,031% | 0,0095484 | 0,0095484 | 0,019% | 0,048% |
| R7 | Humano | Viviendas La Ligua | 0,0128282 | 0,0128282 | 0,010% | 0,026% | 0,0078163 | 0,0078163 | 0,016% | 0,039% |
| R14 | Humano | Viviendas | 0,0872357 | 0,0872357 | 0,067% | 0,174% | 0,0530937 | 0,0530937 | 0,106% | 0,265% |
| R15 | Humano | Viviendas | 0,0556857 | 0,0556857 | 0,043% | 0,111% | 0,0339093 | 0,0339092 | 0,068% | 0,170% |
| RH2 | Grupos<br>humanos | Vivienda/Almacén en<br>área rural | 0,0597675 | 0,0597675 | 0,046% | 0,120% | 0,0360522 | 0,0360522 | 0,072% | 0,180% |
| RH3 | Grupos<br>humanos | Vivienda en área rural | 0,0372633 | 0,0372632 | 0,029% | 0,075% | 0,0218390 | 0,0218391 | 0,044% | 0,109% |
| RH4 | Grupos<br>humanos | Vivienda en área rural | 0,0657198 | 0,0657197 | 0,051% | 0,131% | 0,0389177 | 0,0389176 | 0,078% | 0,195% |
| RH5 | Grupos<br>humanos | Vivienda/Almacén en<br>área rural | 0,1108893 | 0,1108893 | 0,085% | 0,222% | 0,0666957 | 0,0666958 | 0,133% | 0,333% |
| RH6 | Grupos<br>humanos | Vivienda en área rural | 0,0896529 | 0,0896530 | 0,069% | 0,179% | 0,0544217 | 0,0544216 | 0,109% | 0,272% |
| RH7 | Grupos<br>humanos | Vivienda en área rural | 0,0548798 | 0,0548797 | 0,042% | 0,110% | 0,0333499 | 0,0333499 | 0,067% | 0,167% |

**Tabla 14.: Potenciales impactos sobre componente calidad del aire**

| Recurso | Impacto | Posibles impactos |
| --- | --- | --- |
| Aire | Impactos en la calidad del<br>aire | • <br>Posible aumento en la concentración de material particulado<br>en el área de influencia. |
| Aire | Impacto en la calidad del<br>aire que ocasiona<br>impactos sobre otro<br>recurso natural renovable | • <br>El impacto en la calidad del aire producto del aumento de<br>concentraciones de contaminantes, ocasionar impactos sobre<br>ciertas poblaciones de especies de flora y fauna, así como<br>también sobre la calidad del suelo y cultivos. |

**Tabla 15.: Comparación material particulado con normas de calidad secundarias de calidad del aire**

| Receptor | Tipo Receptor | Descripción<br>receptores | MPS (mg/m2/día) | Norma<br>confederación Suiza |
| --- | --- | --- | --- | --- |
| Receptor | Tipo Receptor | Descripción<br>receptores | Anual | Anual |
| R1 | Red Hidrográfica | Río La Ligua | 0,0000 | 0,000% |
| R5 | Red Hidrográfica | Estero Jaruro | 0,0000 | 0,000% |
| R8 | Atractivo Turístico | Camino<br>Longotoma-La<br>ligua | 0,0000 | 0,000% |
| R9 | Santuario de la<br>naturaleza | Humedal Salinas<br>de Pullally - Dunas<br>de Longotoma | 0,0000 | 0,000% |
| R10 | Atractivo Turístico | Longotoma | 0,0000 | 0,000% |
| R11 | Sitio Prioritario | Estuario Río La<br>Ligua | 0,0000 | 0,000% |
| R12 | Sitio Prioritario | Papudo | 0,0000 | 0,000% |
| R13 | Agrícola | Cultivos | 0,0000 | 0,000% |
| RH1 | Industrial | Recinto antena<br>telefónica | 0,0052 | 0,003% |
