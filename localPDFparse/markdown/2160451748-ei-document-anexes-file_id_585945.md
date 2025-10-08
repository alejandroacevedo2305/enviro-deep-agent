---
title: Sin título
author: CSW
date: D:20231114110810-03'00'
language: es
type: report
pages: 55
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Declaración de Impacto Ambiental Proyecto Nueva Subestación Seccionadora Buli
-->

# Declaración de Impacto Ambiental Proyecto Nueva Subestación Seccionadora Buli

## Anexo 17.2 Modelación de emisiones atmosféricas

Noviembre, 2023

Consultoría y Tecnología al Servicios del Medio Ambiente

Nva de Lyon 96, Of 307, Providencia

+56 2 3224 9095 contacto@csw.cl

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Índice de contenido

1 Introducción ................................................................................................................................ 5

2 Justificación del modelo a utilizar ................................................................................................ 5

2.1 Modelo de dispersión de contaminantes CALPUFF ............................................................. 6

2.2 Fundamentos del modelo .................................................................................................... 7

3 Parámetros de entrada modelo CALPUFF ................................................................................... 9

3.1 Escenario meteorológico ..................................................................................................... 9

3.2 Dominio de modelación .................................................................................................... 10

3.3 Uso de suelos .................................................................................................................... 11

3.4 Escenario de emisiones ..................................................................................................... 12

3.5 Escenario de receptores .................................................................................................... 14

4 Resultados de la modelación ..................................................................................................... 17

4.1 Escenario geofísico ............................................................................................................ 17

4.2 Modelo meteorológico ...................................................................................................... 22

4.3 Resultados modelación CALPUFF ...................................................................................... 33

4.3.1 Material particulado .................................................................................................. 33

5 Cuerpo normativo ...................................................................................................................... 37

5.1 Normativa nacional de calidad del aire ............................................................................. 37

5.2 Normativa internacional de referencia .............................................................................. 37

6 Evaluación de impactos ............................................................................................................. 39

6.1 Evaluación de impactos sobre la salud de la población ..................................................... 39

6.2 Evaluación de impactos sobre la calidad del aire, flora y vegetación, fauna, aguas

superficiales y suelo ...................................................................................................................... 42

7 Análisis de significancia de MP10 y MP2.5 en Zonas Saturadas ................................................ 45

Página 2 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

8 Área de influencia ...................................................................................................................... 49

9 Conclusiones .............................................................................................................................. 51

10 Bibliografía ............................................................................................................................. 53

Índice de Figuras

Figura 1. Representación Gráfica del Modelo Tipo Puff y de Pluma .................................................... 7

Figura 2. Grilla meteorológica y grilla computacional ........................................................................ 10

Figura 3. Uso de suelo dominio de modelación ................................................................................. 11

Figura 4. Escenario de fuentes ........................................................................................................... 13

Figura 5. Receptores .......................................................................................................................... 16

Figura 6. Topografía ........................................................................................................................... 17

Figura 7. Albedo ................................................................................................................................. 18

Figura 8. Rugosidad superficial .......................................................................................................... 19

Figura 9. Leaf Area Index ................................................................................................................... 20

Figura 10. Razón de Bowen ............................................................................................................... 21

Figura 11. Rosa de los vientos año 2022 ............................................................................................ 25

Figura 12. Variabilidad temporal del viento ....................................................................................... 26

Figura 13. Serie de tiempo dirección del viento ................................................................................ 27

Figura 14. Variación dirección del viento ........................................................................................... 28

Figura 15. Serie de tiempo velocidad del viento ................................................................................ 29

Figura 16. Ciclo diario velocidad del viento ....................................................................................... 29

Figura 17. Velocidad del viento ......................................................................................................... 30

Figura 18. Mapa de isoconcentraciones de MP10 promedio anual ................................................... 34

Página 3 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 19. Mapa de isoconcentraciones de MP10 promedio 24h ..................................................... 35

Figura 20. Mapa de isoconcentraciones de MP2.5 promedio anual .................................................. 35

Figura 21. Mapa de isoconcentraciones de MP2.5 promedio 24h .................................................... 36

Figura 22. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio anual ............ 36

Figura 23. Modelo conceptual ........................................................................................................... 39

Figura 24. Área de influencia calidad del aire ..................................................................................... 50

Índice de Tablas

Tabla 1. Construcción detalle del dominio de los datos meteorológicos............................................. 9

Tabla 2. Resumen tasa de emisiones atmosféricas para el año 1 ...................................................... 13

Tabla 3. Receptores modelación........................................................................................................ 14

Tabla 4. Campo de vientos................................................................................................................. 22

Tabla 5. Altura de la capa de mezcla.................................................................................................. 31

Tabla 6. Resultados modelación año 1 material particulado ............................................................. 33

Tabla 7. Cuerpo normativo ................................................................................................................ 37

Tabla 8. Cuerpo normativo ................................................................................................................ 38

Tabla 9. Comparación material particulado con normas de calidad primaria y secundaria .............. 40

Tabla 10. Potenciales impactos sobre componente calidad del aire ................................................. 42

Tabla 11. Evaluación de impactos ...................................................................................................... 43

Tabla 12. Análisis de significancia MP10 y MP2.5 en Zonas saturadas .............................................. 46

Página 4 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

1 Introducción

El presente documento tiene como objetivo establecer el impacto de las emisiones del "Proyecto

Nueva Subestación Seccionadora Buli" en la calidad del aire, utilizando los resultados del Inventario

de emisiones atmosféricas, detallado en el Anexo 17 de la DIA.

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

kilómetros, abarcando fuentes y receptores sensibles.

Página 5 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Por lo tanto, siguiendo las directrices de la "Guía para el Uso de Modelos de Calidad del Aire en el

SEIA" (SEA, 2023), se utilizará un modelo que permita simular la meteorología heterogénea. En este

sentido, se ha seleccionado un modelo de tipo "puff" para llevar a cabo la modelación de calidad del

aire. A continuación, se proporciona el detalle del modelo de tipo "puff" que se utilizará.

2.1 Modelo de dispersión de contaminantes CALPUFF

El sistema de modelación, tal como su nombre lo indica, incluye dos componentes principales: WRF

y CALPUFF, además de una larga selección de preprocesadores, diseñados para incluir en el modelo

datos geofísicos y de usos de suelos, y postprocesadores como por ejemplo CALPOST, que permiten

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

Página 6 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 1. Representación Gráfica del Modelo Tipo Puff y de Pluma

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

Página 7 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

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

Página 8 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

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
|Punto de Referencia|Latitud: - 36.381 S<br>Longitud: - 71.904 W|
|Área de Dominio|50x50 km|
|Proyección|Lambert Conic Conformal|
|Datum|NWS-84 6370 km Radius, Global Sphere|

Página 9 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

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

Figura 2. Grilla meteorológica y grilla computacional

Fuente: Elaboración propia.

Página 10 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

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

Figura 3. Uso de suelo dominio de modelación

Fuente: Elaboración propia.

Página 11 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

De la figura anterior el uso de suelo 40 corresponde a “Bosques”, el uso de suelo 30 corresponde a

“Pastizales”, el uso de suelo 20 corresponde a “Tierra agrícola” y el uso de suelo 10 corresponde a

“Urbano”.

Se aprecia que en el sector de emplazamiento del proyecto se identifica el uso de suelo de tipo “Tierra

agrícola”.

3.4 Escenario de emisiones

A continuación, se presenta el escenario a modelar, donde se contemplan las fuentes de emisión de

material particulado para el peor escenario posible a modo de descartar afectaciones a la salud de la

población. Cabe destacar, que se considera la construcción y operación del proyecto dentro del año

1, dado que es el período más crítico del Proyecto, el cual abarca el primer año de la fase de

construcción (12 meses).

De manera conservadora, se considera que todas las emisiones de las actividades constructivas son

producidas de manera simultánea en el predio del Proyecto, lo que en la práctica no ocurrirá, puesto

que las actividades constructivas son realizadas de forma secuencial.

En el contexto de la modelación, se han considerado las emisiones generadas por el tránsito y la

combustión en caminos pavimentados, las cuales están representadas en color rojo. Además, se han

tenido en cuenta las emisiones provenientes de caminos no pavimentados, las cuales están

representadas en color verde. Por otro lado, se han considerado las emisiones generadas por diversas

actividades en el área del proyecto, como maquinaria fuera de ruta, grupos electrógenos,

excavaciones, nivelación, perforaciones y movimiento de tierra, las cuales se han representado en

color azul.

Página 12 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 4. Escenario de fuentes

Fuente: Elaboración propia.

De las emisiones presentadas en la estimación de emisiones para el año 1, la resuspensión por

tránsito en vías pavimentadas se asocian a la fuente denominada “Caminos pavimentados”, en el

caso de la resuspensión por tránsito en vías no pavimentadas se asocian a la fuente denominada

“Caminos No pavimentados”, finalmente, las emisiones asociadas a excavaciones, movimiento de

tierra, compactación, nivelación, perforación, maquinaria fuera de ruta y grupos electrógenos, se
asocia a la fuente de área denominada “Área Proyecto”, como se detalla en la siguiente Tabla.

Tabla 2. Resumen tasa de emisiones atmosféricas para el año 1

|Contamina<br>nte|Resultados estimación de emisiones|Col3|Col4|Datos entrada CALPUFF|Col6|Col7|
|---|---|---|---|---|---|---|
|Contamina<br>nte|Tasa emisión<br>Área Proyecto|Caminos No<br>pavimentados|Caminos<br>pavimentados|Tasa emisión<br>Área Proyecto|Caminos<br>pavimentados|Caminos No<br>pavimentados|
|Unidad|t/año|t/año|t/año|g/s/m2|g/s/m|g/s/m|
|MP10|0,43772|1,62608|1,16148|5,49,E-07|5,75,E-08|3,29,E-10|

Página 13 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Contamina<br>nte|Resultados estimación de emisiones|Col3|Col4|Datos entrada CALPUFF|Col6|Col7|
|---|---|---|---|---|---|---|
|Contamina<br>nte|Tasa emisión<br>Área Proyecto|Caminos No<br>pavimentados|Caminos<br>pavimentados|Tasa emisión<br>Área Proyecto|Caminos<br>pavimentados|Caminos No<br>pavimentados|
|Unidad|t/año|t/año|t/año|g/s/m2|g/s/m|g/s/m|
|MP2.5|0,31919|0,16261|0,30156|4,00,E-07|5,75,E-09|8,54,E-11|
|MPS|0,65896|5,31186|5,93676|8,26,E-07|1,88,E-07|1,68,E-09|
|Tipo de<br>fuente|Areal|Lineal|Lineal|Areal|Lineal|Lineal|

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
|Agrícola|R1|239442|5969714|107|Cultivos|
|Humano|R2|239176|5970068|266|Viviendas|

Página 14 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Tipo Receptor|Id|Coordenadas|Col4|Distancia<br>al<br>Proyecto<br>[m]|Descripción|
|---|---|---|---|---|---|
|Tipo Receptor|Id|WGS84 Huso 19S|WGS84 Huso 19S|WGS84 Huso 19S|WGS84 Huso 19S|
|Tipo Receptor|Id|Este [m]|Sur [m]|Sur [m]|Sur [m]|
|Agrícola|R3|239796|5970267|395|Cultivos|
|Red Hidrográfica|R4|239851|5969999|257|Estero Dollimo|
|Red Hidrográfica|R5|240984|5971406|2041|Escuela Buli-Caserío|
|Humano|R6|243095|5969675|3408|Posta de Salud Rural La<br>Gloria|
|Agrícola|R7|239819|5969230|570|Cultivos|
|Agrícola|R8|238054|5969810|1342|Cultivos|
|Red Hidrográfica|R9|237852|5968341|2201|Estero Verquico|
|Red Hidrográfica|R10|237058|5971257|2694|Estero Millauquén|
|Humano|R11|236754|5972266|3532|Escuela Buli|
|Humano|R12|244433|5973717|6155|Escuela Puertas de Virguin|
|Humano|R13|245857|5968853|6240|Liceo Tiuquilemu|
|Humano|R14|245207|5966092|6646|Escuela Agua Buena|
|Humano|R15|237608|5963910|6191|Liceo Agrícola San Carlos|
|Humano|R16|235606|5965524|5786|Colegio Concepción de San<br>Carlos|
|Humano|R17|235413|5965129|6209|Centro Comunitario de<br>Salud Familiar Valle Hondo|
|Atractivo Turístico|R18|234842|5964841|6806|Agroexpo Exposición<br>ganadera agrícola y<br>artesanal|
|Monumento Histórico|R19|235116|5964590|6812|Casa donde nació Violeta<br>Parra|
|Zona de Conservación<br>Histórica|R20|234914|5964734|6836|Zona de Conservación<br>Histórica|
|Humano|R21|235110|5964621|6792|Viviendas|
|Atractivo Turístico|R22|234763|5963688|7736|Rodeo de San Carlos|
|Atractivo Turístico|R23|234807|5963642|7745|Medialuna monumental de<br>San Carlos|
|Humano|R24|222824|5947893|27450|Viviendas Chillán|

Fuente: Elaboración propia.

Página 15 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 5. Receptores

Fuente: Elaboración propia.

Página 16 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

4 Resultados de la modelación

A continuación, se presentan los resultados obtenidos, en cuanto a la concentración estimada de

contaminantes respecto a las distancias discretas establecidas (receptores). En el Apéndice A se

incluyen los resultados del modelo CALPUFF.

4.1 Escenario geofísico

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1, cuya resolución

es aproximadamente 30 m.

Figura 6. Topografía

Fuente: Elaboración propia.

El Proyecto se encuentra ubicado en un sector donde la topografía es de mediana y baja altura y se

encuentra a una distancia donde no posee influencia del borde costero.

En los siguientes gráficos se presentan los datos de terreno obtenidos para la modelación.

Página 17 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 7. Albedo

Fuente: Elaboración propia.

Página 18 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 8. Rugosidad superficial

Fuente: Elaboración propia.

Página 19 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 9. Leaf Area Index

Fuente: Elaboración propia.

Página 20 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 10. Razón de Bowen

Fuente: Elaboración propia.

Página 21 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

4.2 Modelo meteorológico

Mediante el uso del modelo CALMET y en función de los datos de entrada WRF descritos en el

escenario meteorológico, se procedió a generar una matriz de vientos predominantes y alturas

aproximadas de capas de mezclas al interior del dominio de la modelación, para cada hora del año

2022.

Con el fin de presentar los resultados a través de una gráfica de campos de viento, se ha seleccionado

el día 8 de marzo de 2022 como una fecha representativa dentro del dominio de modelación. La

siguiente tabla muestra el comportamiento de los vientos a una altura de 10 metros sobre el nivel

del suelo, para diferentes horarios de la fecha mencionada.

|Tabla 4. Campo de vientos|Col2|
|---|---|
|Campo de Viento|Descripción|
|<br>|Comportamiento de<br>los vientos a una<br>altura 10 metros<br>sobre el nivel de<br>suelo a las 08:00<br>horas<br>como<br>una<br>hora representativa<br>del 8 de marzo de<br>2022 al interior del<br>dominio<br>de<br>la<br>modelación.|

Página 22 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Campo de Viento|Descripción|
|---|---|
||Comportamiento de<br>los vientos a una<br>altura 10 metros<br>sobre el nivel de<br>suelo a las 12:00<br>horas<br>como<br>una<br>hora representativa<br>del 8 de marzo de<br>2022 al interior del<br>dominio<br>de<br>la<br>modelación.|
|<br>|Comportamiento de<br>los vientos a una<br>altura 10 metros<br>sobre el nivel de<br>suelo a las 16:00<br>horas<br>como<br>una<br>hora representativa<br>del 8 de marzo de<br>2022 al interior del<br>dominio<br>de<br>la<br>modelación.|

Página 23 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Campo de Viento|Descripción|
|---|---|
||Comportamiento de<br>los vientos a una<br>altura 10 metros<br>sobre el nivel de<br>suelo a las 20:00<br>horas<br>como<br>una<br>hora representativa<br>del 8 de marzo de<br>2022 al interior del<br>dominio<br>de<br>la<br>modelación.|
||Comportamiento de<br>los vientos a una<br>altura 10 metros<br>sobre el nivel de<br>suelo a las 24:00<br>horas<br>como<br>una<br>hora representativa<br>del 8 de marzo de<br>2022 al interior del<br>dominio<br>de<br>la<br>modelación.|

Fuente: Elaboración propia.

Página 24 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Dirección del viento

Con respecto a la dirección del viento, en la siguiente Figura presenta la rosa de los vientos

correspondiente al dominio de modelación. La componente principal corresponde al viento Sur
Oeste (SO).

Figura 11. Rosa de los vientos año 2022

Fuente: Elaboración propia.

A continuación, se presentan las rosas de los vientos que muestran la variabilidad temporal de la

velocidad y dirección del viento durante el periodo de modelación.

Página 25 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 12. Variabilidad temporal del viento

|Rosa de los vientos período 00:00 AM - 05:00 AM<br>entre el 01/01/2022 - 31/12/2022|Rosa de los vientos período 06:00 AM - 11:00 AM<br>entre el 01/01/2022 - 31/12/2022|
|---|---|
|Rosa de los vientos período 12:00 PM - 17:00 PM<br>entre el 01/01/2022 - 31/12/2022|Rosa de los vientos período 18:00 PM - 23:00 PM<br>entre el 01/01/2022 - 31/12/2022|

Fuente: Elaboración propia.

Página 26 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 13. Serie de tiempo dirección del viento

Fuente: Elaboración propia.

Página 27 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 14. Variación dirección del viento

Fuente: Elaboración propia.

Velocidad del viento:

Con respecto a la velocidad del ciento, a continuación, se presentan gráficos de velocidad de viento

y ciclos, diarios, semanales y mensuales de la velocidad del viento.

Página 28 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 15. Serie de tiempo velocidad del viento

Fuente: Elaboración propia.

Figura 16. Ciclo diario velocidad del viento

Fuente: Elaboración propia.

Página 29 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 17. Velocidad del viento

Fuente: Elaboración propia.

Altura de la capa de mezcla

Por otra parte, la profundidad vertical de la atmósfera donde se produce el mezclado, se denomina

capa de mezcla. La parte superior de esta capa se conoce como altura de mezcla, la cual determina

el alcance vertical del proceso de dispersión de los contaminantes liberados debajo de ella, a

continuación, se representa la altura de la capa de mezcla mediante procesamiento de datos

meteorológicos en el software CALPUFF View.

Página 30 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Tabla 5. Altura de la capa de mezcla|Col2|
|---|---|
|Altura de la capa de mezcla|Descripción|
||Presentación<br>del<br>comportamiento<br>de<br>la<br>altura de capa de mezcla en<br>horarios<br>representativos,<br>entre las 00:00 y las 08:00<br>del<br>día<br>escogido<br>para<br>exponer los resultados del<br>módulo<br>micro<br>meteorológico (8 de marzo<br>de<br>2022)<br>como<br>representativo de verano<br>como<br>peor<br>escenario<br>(menor humedad ambiental<br>y <br>menor<br>presencia<br>de<br>lluvias). En ese sentido, se<br>puede observar que, por la<br>temperatura ambiente y las<br>variables ambientales, la<br>altura de la capa de mezcla<br>se mantiene a una altura<br>media, sin sobrepasar los<br>600 metros en la mayoría<br>de los puntos.|
|<br>|<br>|

Página 31 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Altura de la capa de mezcla|Descripción|
|---|---|
||Presentación<br>del<br>comportamiento<br>de<br>la<br>altura de capa de mezcla en<br>horarios<br>representativos,<br>entre las 16:00 y las 20:00<br>del<br>día<br>escogido<br>para<br>exponer los resultados del<br>módulo<br>micro<br>meteorológico. Se puede<br>observar<br>que,<br>por<br>la<br>temperatura ambiente y las<br>variables<br>ambientales<br>diurnas, la altura de la capa<br>de mezcla se expande por<br>sobre los 2600 metros. De<br>manera que se alcanzan los<br>2200 metros en la mayoría<br>de los puntos, volviendo a<br>contraerse en la tarde a los<br>644 metros.|
|||

Fuente: Elaboración propia.

Página 32 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

4.3 Resultados modelación CALPUFF

4.3.1 Material particulado

Con el fin de determinar la eventual influencia que tiene el Proyecto en la calidad del aire sobre la

localidad y los receptores identificados, en función de los análisis antes realizados, se determinaron

las concentraciones de MP10, MP2.5 y MPS para cada una de las horas del año sobre los receptores

considerados. A continuación, se presenta el aporte del proyecto sobre a los receptores antes

mencionados, segregado según los períodos de la norma de calidad del aire aplicable.

Tabla 6. Resultados modelación año 1 material particulado

|Receptor|MP10 (μg/m3)|Col3|MP2,5 (μg/m3)|Col5|MPS<br>(mg/m2/día)|
|---|---|---|---|---|---|
|Receptor|24 h|Anual|24 h|Anual|Anual|
|R1|0,559455|0,557920|0,407486|0,40637|4,140527|
|R2|0,148258|0,147443|0,10791|0,10732|0,770999|
|R3|0,308406|0,287283|0,22459|0,20920|1,461582|
|R4|0,246790|0,233267|0,17975|0,16990|1,413874|
|R5|0,007410|0,006821|0,00539|0,00497|0,000039|
|R6|0,000755|0,000639|0,00055|0,00047|0,000001|
|R10|0,061385|0,058021|0,04471|0,04226|0,186304|
|R7|0,005485|0,005244|0,00399|0,00382|0,000847|
|R8|0,004510|0,004509|0,00328|0,00328|0,000060|
|R9|0,000937|0,000865|0,00068|0,00063|0,000001|
|R11|0,000595|0,000548|0,00043|0,00040|0,000000|
|R12|0,000708|0,000598|0,00052|0,00044|0,000002|
|R13|0,000190|0,000155|0,00014|0,00011|0,000000|
|R14|0,000171|0,000141|0,00012|0,00010|0,000000|
|R15|0,000467|0,000422|0,00034|0,00031|0,000004|
|R16|0,000462|0,000462|0,00033|0,00033|0,000190|
|R17|0,000411|0,000411|0,00030|0,00030|0,000103|
|R18|0,000312|0,000312|0,00023|0,00023|0,000024|

Página 33 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Receptor|MP10 (μg/m3)|Col3|MP2,5 (μg/m3)|Col5|MPS<br>(mg/m2/día)|
|---|---|---|---|---|---|
|Receptor|24 h|Anual|24 h|Anual|Anual|
|R19|0,000349|0,000349|0,00025|0,00025|0,000068|
|R20|0,000320|0,000320|0,00023|0,00023|0,000035|
|R21|0,000347|0,000347|0,00025|0,00025|0,000072|
|R22|0,000302|0,000301|0,00021|0,00021|0,000421|
|R23|0,000317|0,000317|0,00022|0,00022|0,000874|
|R24|0,000024|0,000019|0,00002|0,00001|0,00000002|

Fuente: Elaboración propia.

A continuación, se presentan los mapas de isoconcentraciones asociados a cada uno de los

parámetros para el material particulado MP10, MP2,5 y MPS, tanto para las concentraciones anuales

como para las concentraciones diarias.

Figura 18. Mapa de isoconcentraciones de MP10 promedio anual

Fuente: Elaboración propia.

Página 34 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 19. Mapa de isoconcentraciones de MP10 promedio 24h

Fuente: Elaboración propia.

Figura 20. Mapa de isoconcentraciones de MP2.5 promedio anual

Fuente: Elaboración propia.

Página 35 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 21. Mapa de isoconcentraciones de MP2.5 promedio 24h

Fuente: Elaboración propia.

Figura 22. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio anual

Fuente: Elaboración propia.

Página 36 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

5 Cuerpo normativo

5.1 Normativa nacional de calidad del aire

En el contexto legal, la normativa nacional vigente referente a las normas primarias y secundarias de

calidad del aire, aplicables a todo el territorio nacional, establecen límites máximos de concentración

de contaminantes, como se detalla en la siguiente Tabla.

Tabla 7. Cuerpo normativo

|Parámetro|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|
|MP10|Primaria|Promedio anual|50 μg/m3|DS N°12/2022 MMA|
|MP10|Primaria|Promedio 24 horas<br>(Percentil 98)|130 μg/m3|130 μg/m3|
|MP2.5|Primaria|Promedio anual|20 μg/m3|DS N°12/2012 MMA|
|MP2.5|Primaria|Promedio 24 horas<br>(Percentil 98)|50 μg/m3|50 μg/m3|

Fuente: Elaboración propia en base a MINSEGPRES (2002), MINSEGPRES (2010), MMA (2011), MMA (2018),

MMA (2022).

5.2 Normativa internacional de referencia

Con respecto al contaminante MPS no existe normativa nacional aplicable a la ubicación del Proyecto,

por lo tanto, se utilizará una norma de referencia internacional para comparar las emisiones de este
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

Página 37 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

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

En el Apéndice B de este informe se incluye un ejemplar íntegro y vigente de la Ordenanza de la

Confederación Suiza sobre control de la contaminación atmosférica.

A continuación, se presenta un resumen de los límites de MPS establecidos en las normativas

internacionales a utilizar como referencia.

Tabla 8. Cuerpo normativo

|Contaminante|País|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|---|
|MPS <br>(Partículas<br>sedimentables)|Confederación<br>Suiza|-|Promedio<br>anual|200<br>(mg/m2día)|Ordenanza de la<br>Confederación<br>Suiza, Sobre Control<br>de Contaminación<br>del Aire 1993|

Página 38 de 55

Fuente: Elaboración propia.

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

6 Evaluación de impactos

6.1 Evaluación de impactos sobre la salud de la población

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

a viviendas, establecimientos educacionales y establecimientos de salud, además de cultivos

agrícolas.

Figura 23. Modelo conceptual

Fuente: Elaboración propia.

A continuación, se presenta la comparación de las emisiones del Proyecto con las normas de calidad

primaria vigentes y secundarias de referencia.

Página 39 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Tabla 9. Comparación material particulado con normas de calidad primaria y secundaria

|Receptor|Tipo Receptor|MP10 (ug/m3)|Col4|% DS N°12/2022 MMA|Col6|MP2,5 (ug/m3)|Col8|% DS N°12/2012 MMA|Col10|MPS<br>(mg/m2dia)|Ordenanza<br>Confederación<br>Suiza|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Tipo Receptor|24 horas|Anual|24 horas|Anual|24 horas|Anual|24 horas|Anual|Anual|30 días|
|R1|Agrícola|0,559455|0,557920|0,430%|1,116%|0,407486|0,406368|0,815%|2,032%|4,1405|0,04141%|
|R2|Humano|0,148258|0,147443|0,114%|0,295%|0,107910|0,107318|0,216%|0,537%|0,7710|0,00771%|
|R3|Agrícola|0,308406|0,287283|0,237%|0,575%|0,224585|0,209203|0,449%|1,046%|1,4616|0,01462%|
|R4|Red Hidrográfica|0,246790|0,233267|0,190%|0,467%|0,179749|0,169899|0,359%|0,849%|1,4139|0,01414%|
|R5|Red Hidrográfica|0,007410|0,006821|0,006%|0,014%|0,005395|0,004966|0,011%|0,025%|0,0000|0,00000%|
|R6|Humano|0,000755|0,000639|0,001%|0,001%|0,000550|0,000465|0,001%|0,002%|0,0000|0,00000%|
|R10|Agrícola|0,061385|0,058021|0,047%|0,116%|0,044711|0,042261|0,089%|0,211%|0,1863|0,00186%|
|R7|Agrícola|0,005485|0,005244|0,004%|0,010%|0,003991|0,003816|0,008%|0,019%|0,0008|0,00001%|
|R8|Red Hidrográfica|0,004510|0,004509|0,003%|0,009%|0,003282|0,003282|0,007%|0,016%|0,0001|0,00000%|
|R9|Red Hidrográfica|0,000937|0,000865|0,001%|0,002%|0,000682|0,000630|0,001%|0,003%|0,0000|0,00000%|
|R11|Humano|0,000595|0,000548|0,000%|0,001%|0,000433|0,000399|0,001%|0,002%|0,0000|0,00000%|
|R12|Humano|0,000708|0,000598|0,001%|0,001%|0,000516|0,000435|0,001%|0,002%|0,0000|0,00000%|
|R13|Humano|0,000190|0,000155|0,000%|0,000%|0,000138|0,000113|0,000%|0,001%|0,0000|0,00000%|
|R14|Humano|0,000171|0,000141|0,000%|0,000%|0,000124|0,000102|0,000%|0,001%|0,0000|0,00000%|
|R15|Humano|0,000467|0,000422|0,000%|0,001%|0,000340|0,000307|0,001%|0,002%|0,0000|0,00000%|
|R16|Humano|0,000462|0,000462|0,000%|0,001%|0,000333|0,000333|0,001%|0,002%|0,0002|0,00000%|
|R17|Humano|0,000411|0,000411|0,000%|0,001%|0,000297|0,000297|0,001%|0,001%|0,0001|0,00000%|
|R18|Atractivo<br>Turístico|0,000312|0,000312|0,000%|0,001%|0,000226|0,000226|0,000%|0,001%|0,0000|0,00000%|
|R19|Monumento<br>Histórico|0,000349|0,000349|0,000%|0,001%|0,000252|0,000252|0,001%|0,001%|0,0001|0,00000%|
|R20|Zona de<br>Conservación<br>Histórica|0,000320|0,000320|0,000%|0,001%|0,000232|0,000232|0,000%|0,001%|0,0000|0,00000%|
|R21|Humano|0,000347|0,000347|0,000%|0,001%|0,000251|0,000251|0,001%|0,001%|0,0001|0,00000%|

Página 40 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Receptor|Tipo Receptor|MP10 (ug/m3)|Col4|% DS N°12/2022 MMA|Col6|MP2,5 (ug/m3)|Col8|% DS N°12/2012 MMA|Col10|MPS<br>(mg/m2dia)|Ordenanza<br>Confederación<br>Suiza|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Tipo Receptor|24 horas|Anual|24 horas|Anual|24 horas|Anual|24 horas|Anual|Anual|30 días|
|R22|Atractivo<br>Turístico|0,000302|0,000301|0,000%|0,001%|0,000213|0,000213|0,000%|0,001%|0,0004|0,00000%|
|R23|Atractivo<br>Turístico|0,000317|0,000317|0,000%|0,001%|0,000218|0,000218|0,000%|0,001%|0,0009|0,00001%|
|R24|Humano|0,000024|0,000019|0,00002%|0,00004%|0,000017|0,000014|0,0000%|0,0001%|0,00000002|0,00000%|

Fuente: Elaboración propia.

.

Página 41 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Según los resultados de la modelación de dispersión atmosférica del material particulado generado

durante el primer año del proyecto, se ha determinado que las concentraciones resultantes son de

baja magnitud. El receptor humano donde se presentarán mayores concentraciones de material
particulado será R2, cuyas concentraciones máximas de MP10 serán de 0,147 μg/m [3] en el período

anual, lo cual representa aproximadamente el 0,295% del límite establecido por la normativa D.S.
N°12/22 MMA. En relación al MP2.5, el Proyecto alcanza como máximo el 0,537% del límite anual
establecido por la norma D.S. N°12/11 MMA, en el receptor humano R2. Por lo tanto, las emisiones

del Proyecto representan menos del 1% de los umbrales establecidos en las normas de calidad

primaria del aire para material particulado.

En conclusión, de acuerdo a lo expuesto, se puede afirmar que la ejecución del Proyecto en cuanto a

las concentraciones de material particulado no generará un impacto significativo en la salud de las

personas, ya que no excede los límites establecidos por las normas de calidad primaria del aire, que

tienen como objetivo proteger la salud de la población.

6.2 Evaluación de impactos sobre la calidad del aire, flora y vegetación, fauna, aguas superficiales y

suelo

A continuación, se procede a realizar un análisis de los aportes del proyecto en su etapa de

construcción, para determinar si el proyecto generará efectos adversos significativos sobre la calidad

del aire, flora y vegetación, fauna, aguas superficiales y suelo, según los lineamientos establecidos en

la “Guía de evaluación de efectos adversos sobre recursos naturales renovables” (SEA, 2022).

La siguiente Tabla presenta una lista de potenciales impactos que el Proyecto puede generar o

presentar sobre la calidad del aire.

Tabla 10. Potenciales impactos sobre componente calidad del aire

|Recurso|Impacto|Posibles impactos|
|---|---|---|
|Aire|Impactos en la calidad del<br>aire| <br>Posible aumento en la concentración de material particulado<br>en el área de influencia.|
|Aire|Impacto en la calidad del<br>aire que ocasiona<br>impactos sobre otro<br>recurso natural renovable| <br>El impacto en la calidad del aire producto del aumento de<br>concentraciones de contaminantes, ocasionar impactos sobre<br>ciertas poblaciones de especies de flora y fauna, así como<br>también sobre la calidad del suelo y cultivos.<br> <br>El impacto en la calidad del aire producto del aumento de<br>concentraciones de material particulado sedimentable puede<br>producir depositación de contaminantes en la vegetación.|

Página 42 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Recurso|Impacto|Posibles impactos|
|---|---|---|
||Impacto en un recurso<br>natural renovable que<br>causa impacto en otros<br>componentes del artículo<br>11 de la Ley 19.300| <br>Un impacto sobre la calidad del aire, debido a las emisiones<br>atmosféricas del proyecto, puede generar riesgo para la salud<br>de la población, señalado en la letra a) del artículo 11 de la Ley<br>N° 19.300.<br> <br>Un impacto sobre la calidad del aire, debido a las emisiones<br>atmosféricas del proyecto, puede producir depositación de<br>contaminantes en la vegetación utilizada como sustento<br>económico de grupos humanos, ocasionando una alteración<br>en los sistemas de vida y costumbres de dicho grupo.|

Fuente: Elaboración propia.

A continuación, se presenta la evaluación de los posibles impactos identificados en la Tabla anterior.

|Col1|Col2|Tabla 11. Evaluación de impactos|Col4|
|---|---|---|---|
|Recurso|Potencial<br>impacto|Evaluación cualitativa|Evaluación cuantitativa|
|Aire|Impactos en<br>la calidad del<br>aire|Las emisiones de Material Particulado<br>(MP10, MP2.5 y MPS) que generará el<br>Proyecto no ocasionarán un impacto<br>significativo sobre la capacidad del aire,<br>para<br>mantener<br>las<br>funciones<br>de<br>procreación,<br>reproducción,<br>crecimiento,<br>transformación<br>o <br>restablecimiento de recursos naturales,<br>debido a que las normas de calidad<br>primarias y secundarias no se ven<br>sobrepasadas con las emisiones del<br>Proyecto durante el año de mayor<br>emisión.<br> <br>Adicionalmente es importante destacar<br>que las mayores tasas de emisión se<br>generarán durante el año 1 del<br>Proyecto, el cual considera la fase de<br>construcción.|Las emisiones que generará el<br>Proyecto representan menos del<br>2% de los límites establecidos en las<br>normas de calidad primaria para<br>material particulado en todos los<br>receptores identificados, y menos<br>del 1%% de las normas de calidad<br>secundaria del aire para MPS.|
|Aire|Impacto en la<br>calidad<br>del<br>aire<br>que<br>ocasiona<br>impactos<br>sobre<br>otro<br>recurso<br>natural<br>renovable|Se<br>establece<br>que<br>las<br>emisiones<br>partículas que generará el Proyecto<br>(MP10, MP2.5 y MPS), no ocasionarán<br>un impacto significativo sobre la<br>vegetación, cultivos cercanos, cursos de<br>agua, flora, fauna u otros recursos<br>naturales de la zona debido a que las<br>normas<br>de<br>calidad<br>secundarias<br>utilizadas como referencia (Norma|<br>En los receptores correspondientes<br>a recursos naturales las emisiones<br>de MPS que generará el Proyecto<br>representan menos del 0,04% de<br>los límites establecidos en la norma<br>de calidad secundaria del aire. Por<br>lo tanto, no se ocasiona un impacto|

Página 43 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Recurso|Potencial<br>impacto|Evaluación cualitativa|Evaluación cuantitativa|
|---|---|---|---|
|||Confederación<br>Suiza),<br>no<br>se<br>ven<br>sobrepasadas con las emisiones del<br>Proyecto, considerando que las normas<br>de calidad secundaria apuntan a<br>proteger los recursos naturales. Por lo<br>tanto, se puede concluir que, a nivel de<br>calidad del aire, el Proyecto no genera<br>un impacto significativo en la calidad de<br>los recursos naturales del área de<br>influencia.<br> <br>Adicionalmente es importante destacar<br>que las mayores tasas de emisión se<br>generarán durante el año 1 del<br>Proyecto, el cual considera la fase de<br>construcción.|significativo sobre los recursos<br>naturales cercanos.|
||Impacto en un<br>recurso<br>natural<br>renovable<br>que<br>causa<br>impacto<br>en<br>otros<br>componentes<br>del artículo 11<br>de<br>la<br>Ley<br>19.300|Se<br>establece<br>que<br>las<br>emisiones<br>partículas que generará el Proyecto<br>(MP10, MP2.5 y MPS), no ocasionarán<br>un impacto significativo sobre la<br>vegetación, cultivos cercanos, cursos de<br>agua, flora, fauna u otros recursos<br>naturales de la zona debido a que las<br>normas<br>de<br>calidad<br>secundarias<br>utilizadas como referencia (Norma<br>Confederación<br>Suiza),<br>no<br>se<br>ven<br>sobrepasadas con las emisiones del<br>Proyecto, considerando que las normas<br>de calidad secundaria apuntan a<br>proteger los recursos naturales. Por lo<br>tanto, se puede concluir que, a nivel de<br>calidad del aire, el Proyecto no genera<br>un impacto significativo en la calidad de<br>los recursos naturales del área de<br>influencia.<br> <br>Adicionalmente es importante destacar<br>que las mayores tasas de emisión se<br>generarán durante el año 1 del<br>Proyecto, el cual considera la fase de<br>construcción.<br>|<br>En los receptores correspondientes<br>a recursos naturales las emisiones<br>de MPS que generará el Proyecto<br>representan menos del 0,04% de<br>los límites establecidos en la norma<br>de calidad secundaria del aire. Por<br>lo tanto, no se ocasiona un impacto<br>significativo sobre los recursos<br>naturales cercanos..|

Fuente: Elaboración propia.

En términos de calidad y cantidad, se establece que el Proyecto no genera efectos adversos

significativos en los recursos naturales mencionados: aire, flora y vegetación, fauna, aguas

superficiales y suelo, considerando que las condiciones que permiten la presencia y desarrollo de

Página 44 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

especies y la funcionalidad de los ecosistemas dependientes de la calidad del aire en la zona no se

ven afectadas por la presencia del Proyecto.

Además, no se produce una modificación sustancial en la composición, estructura o funcionamiento

del ecosistema que impida la manifestación de los procesos e interrelaciones característicos. Esto se
debe a que el Proyecto no supera los límites establecidos en las normas de calidad del aire (tanto

primarias como secundarias) y las tasas de emisión del Proyecto se mantienen por debajo del 10% de

dichos límites, según las regulaciones aplicables.

En consecuencia, se puede afirmar que el ecosistema original se mantiene sin cambios significativos

debido a las emisiones atmosféricas generadas por el Proyecto. Por lo tanto, la ejecución del Proyecto

no afecta la permanencia ni la capacidad de generación de los recursos naturales mencionados: aire,

flora y vegetación, fauna, aguas superficiales y suelo. Esto implica que la disponibilidad, utilización y

aprovechamiento racional futuro de dichos recursos no se ven comprometidos. Asimismo, la

capacidad de regeneración y renovación de estos recursos no se ve alterada por la ejecución del

Proyecto.

En resumen, se concluye que las emisiones atmosféricas generadas por el Proyecto no tienen un

impacto significativo en los recursos naturales mencionados y no comprometen su disponibilidad,

utilización, aprovechamiento racional ni su capacidad de regeneración o renovación.

7 Análisis de significancia de MP10 y MP2.5 en Zonas Saturadas

En base a lo establecido en el documento “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de

emisiones en zonas saturadas por material particulado respirable MP10 y material particulado fino

respirable MP2,5” (SEA, 2023), se realizó un análisis de significancia de los aportes de MP10 y MP2.5,

dado que parte del proyecto está inserto en las siguientes zonas saturadas:

 - Decreto N°36/2012. Declara zona saturada por MP10 y por MP2,5, ambas como

concentración diaria; y zona latente por MP10, como concentración anual, a las comunas

de Chillán y Chillán Viejo del Ministerio del Medio Ambiente.

 - Decreto N°69/2022. Declara zona saturada por norma diaria y latente por norma anual,

ambas por material particulado fino respirable MP2,5, a la macrozona del Valle Central

del Ñuble.

A continuación, se presenta el análisis para cada normativa:

Página 45 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Decreto N°36/2012. Declara zona saturada por MP10 y por MP2,5, ambas como concentración diaria;

y zona latente por MP10, como concentración anual, a las comunas de Chillán y Chillán Viejo del

Ministerio del Medio Ambiente:

Para llevar a cabo este análisis, se optó por seleccionar el año con las condiciones más desfavorables

en términos de emisiones para la simulación de dispersión de contaminantes, en concreto, el año 1

de la fase de construcción del proyecto. Es importante señalar que se escogió un receptor humano

específico (R24) situado en la mencionada zona saturada, a una distancia superior a 25 km del

proyecto.

A continuación, se expone el análisis de significancia realizado al comparar las emisiones del proyecto

en el receptor humano R24, con los niveles de significancia relativos al incremento de

concentraciones de MP10 y M2,5 durante un período de 1 año.

Tabla 12. Análisis de significancia MP10 y MP2.5 en Zonas saturadas

|Zona Saturada|Contaminan<br>te Saturado|Receptor<br>humano Zona<br>saturada|Concentraci<br>ón proyecto<br>(ug/m3)|Valores de<br>significancia para<br>el aumento de<br>concentraciones<br>con una duración<br>1 año (ug/m3)|Resultado|Conclusión|
|---|---|---|---|---|---|---|
|Decreto<br>N°36/2012 MMA|MP10 anual|R24|0,000019|3|MP10 anual < 3<br>ug/m3<br>en todos los<br>receptores<br>humanos|El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP10 anual.|
|Decreto<br>N°36/2012 MMA|MP10 24<br>horas|R24|0,000024|10|MP10 24 h < 10<br>ug/m3<br>en todos los<br>receptores<br>humanos|El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP10 en 24 h.|
|Decreto<br>N°36/2012 MMA|MP2.5<br>anual|R24|0,00001|0,99|MP2.5 anual <<br>0,99 ug/m3<br>en todos los<br>receptores|El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP2.5 anual.|
|Decreto<br>N°36/2012 MMA|MP2.5 24<br>horas|R24|0,00002|5,13|MP2.5 24 h <<br>5,13 ug/m3<br>en todos los<br>receptores|El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP2.5 en 24 h.|

Fuente: Elaboración propia en base a “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de emisiones en zonas
saturadas por material particulado respirable MP10 y material particulado fino respirable MP2,5” (SEA, 2023).

Las emisiones anuales y diarias de MP10 que el proyecto generará en el receptor humano durante la

fase de construcción no exceden los umbrales de significancia establecidos para el aumento de

concentraciones con una duración de 1 año.

Página 46 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Del mismo modo, las emisiones anuales y diarias de MP2.5 generadas por el proyecto en el receptor

humano durante la fase de construcción tampoco superan los límites de significancia establecidos

para incrementos de concentraciones con una duración de 1 año.

En consecuencia, se concluye que el proyecto no genera un impacto ambiental significativo en

términos de la extensión, magnitud y duración de las emisiones de MP10 y MP2.5 en las zona

saturada por MP10 y por MP2,5, ambas como concentración diaria; y zona latente por MP10, como
concentración anual, a las comunas de Chillán y Chillán Viejo (Decreto N°36/2012 MMA), bajo los
lineamientos señalados en el documento “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de

emisiones en zonas saturadas por material particulado respirable MP10 y material particulado fino

respirable MP2,5” (SEA, 2023).

Decreto N°69/2022. Declara zona saturada por norma diaria y latente por norma anual, ambas por
material particulado fino respirable MP2,5, a la macrozona del Valle Central del Ñuble:

Para llevar a cabo este análisis, se optó por seleccionar el año con las condiciones más desfavorables

en términos de emisiones para la simulación de dispersión de contaminantes, en concreto, el año 1

de la fase de construcción del proyecto. Cabe destacar que se consideran todos los receptores

humanos del Proyecto, al localizarse dentro de la Zona saturada definida por este Decreto.

A continuación, se expone el análisis de significancia realizado al comparar las emisiones del proyecto

en los receptores humanos, con los niveles de significancia relativos al incremento de

concentraciones de M2,5 durante un período de 1 año.

Tabla 13. Análisis de significancia MP2.5 en Zonas saturada Valle Central del Ñuble

|Zona Saturada|Contaminante<br>Saturado|Receptor<br>humano<br>Zona<br>saturada|Concentración<br>proyecto<br>(ug/m3)|Valores de<br>significancia para<br>el aumento de<br>concentraciones<br>con una duración<br>1 año (ug/m3)|Resultado|Conclusión|
|---|---|---|---|---|---|---|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R2|0,223493|0,99|MP2.5<br>anual <<br>0,99 ug/m3 <br>en todos<br>los<br>receptores<br>humanos|El Proyecto<br>genera aportes<br>no significativos<br>en las<br>concentraciones<br>de MP2.5 anual.|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R6|0,000978|0,000978|0,000978|0,000978|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R11|0,000833|0,000833|0,000833|0,000833|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R12|0,000906|0,000906|0,000906|0,000906|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R13|0,000237|0,000237|0,000237|0,000237|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R14|0,000215|0,000215|0,000215|0,000215|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R15|0,000643|0,000643|0,000643|0,000643|
|Decreto<br>N°66/2022<br>MMA|MP2.5 anual|R16|0,000726|0,000726|0,000726|0,000726|

Página 47 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

|Zona Saturada|Contaminante<br>Saturado|Receptor<br>humano<br>Zona<br>saturada|Concentración<br>proyecto<br>(ug/m3)|Valores de<br>significancia para<br>el aumento de<br>concentraciones<br>con una duración<br>1 año (ug/m3)|Resultado|Conclusión|
|---|---|---|---|---|---|---|
|Zona Saturada|Contaminante<br>Saturado|R17|0,000640|0,000640|0,000640|0,000640|
|Zona Saturada|Contaminante<br>Saturado|R21|0,000541|0,000541|0,000541|0,000541|
|Zona Saturada|Contaminante<br>Saturado|R24|0,000029|0,000029|0,000029|0,000029|
|Zona Saturada|MP2.5 24<br>horas|R2|0,22473|5,13|MP2.5 24<br>h < 5,13<br>ug/m3 en<br>todos los<br>receptores<br>humanos|El Proyecto<br>genera aportes<br>no significativos<br>en las<br>concentraciones<br>de MP2.5 en 24<br>h.|
|Zona Saturada|MP2.5 24<br>horas|R6|0,00116|0,00116|0,00116|0,00116|
|Zona Saturada|MP2.5 24<br>horas|R11|0,00091|0,00091|0,00091|0,00091|
|Zona Saturada|MP2.5 24<br>horas|R12|0,00107|0,00107|0,00107|0,00107|
|Zona Saturada|MP2.5 24<br>horas|R13|0,00029|0,00029|0,00029|0,00029|
|Zona Saturada|MP2.5 24<br>horas|R14|0,00026|0,00026|0,00026|0,00026|
|Zona Saturada|MP2.5 24<br>horas|R15|0,00071|0,00071|0,00071|0,00071|
|Zona Saturada|MP2.5 24<br>horas|R16|0,00073|0,00073|0,00073|0,00073|
|Zona Saturada|MP2.5 24<br>horas|R17|0,00064|0,00064|0,00064|0,00064|
|Zona Saturada|MP2.5 24<br>horas|R21|0,00054|0,00054|0,00054|0,00054|
|Zona Saturada|MP2.5 24<br>horas|R24|0,00004|0,00004|0,00004|0,00004|

Fuente: Elaboración propia en base a “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de emisiones en zonas saturadas

por material particulado respirable MP10 y material particulado fino respirable MP2,5” (SEA, 2023).

Las emisiones anuales y diarias de MP2.5 que el proyecto generará en los receptores humano durante

la fase de construcción no exceden los umbrales de significancia establecidos para el aumento de

concentraciones con una duración de 1 año.

En consecuencia, se concluye que el proyecto no genera un impacto ambiental significativo en

términos de la extensión, magnitud y duración de las emisiones de MP2.5 en la zona saturada por

norma diaria y latente por norma anual, ambas por material particulado fino respirable MP2,5, a la
macrozona del Valle Central del Ñuble (Decreto N°66/2022 MMA), bajo los lineamientos señalados
en el documento “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de emisiones en zonas saturadas

por material particulado respirable MP10 y material particulado fino respirable MP2,5” (SEA, 2023).

Página 48 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

8 Área de influencia

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

los contaminantes atmosféricos extendiéndose en un radio de 1000 m alrededor del Proyecto,

considerando que las máximas concentraciones de contaminantes se perciben a 250 m de este.

Además, a la distancia de 1000 m desde las obras ejecutadas, las concentraciones de todos los

contaminantes generados están por debajo del 1% de los límites máximos establecidos en las

normativas de calidad del aire.

A continuación, se presenta una figura que detallada el Área de Influencia del Proyecto con respecto

al componente calidad del aire. En el Apéndice C se presenta un kmz con esta área.

Página 49 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

Figura 24. Área de influencia calidad del aire

Fuente: Elaboración propia.

Página 50 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

9 Conclusiones

Los resultados de la modelación de las concentraciones de contaminantes atmosféricos a distintas

distancias desde el Proyecto, muestran que los mayores aportes se producen a una distancia de 490

metros del Proyecto, durante el primer año del Proyecto, correspondiente a la fase de construcción.

De esta forma, se delimitó un área de influencia de la calidad del aire, con la concentración

correspondiente a un 1% del valor de las normas de calidad del aire para los contaminantes

atmosféricos MP10, MP2.5 y MPS. Por lo tanto, el área de influencia quedó definida hasta una

distancia de 1000 metros desde el perímetro del Proyecto.

Es importante mencionar que el Área de influencia definida para el Proyecto no confluye con el área

de influencia de calidad del aire de proyectos con RCA favorable que no hayan sido ejecutados, por

lo que no se consideran para la sinergia con estos proyectos. El receptor humano de máximo impacto

corresponde al receptor R2, donde se ocasionarán aportes poco significativos de concentraciones de

contaminantes atmosféricos. Lo anterior es debido a que los porcentajes de comparación de las

emisiones del Proyecto respecto a la normativa de calidad primaria del aire, no superan el 0,114%

para concentraciones diarias, y el 0,295% para concentraciones anuales, tanto para material
particulado fino como grueso (MP2.5 y MP10).

Respecto a la depositación de MPS, se establece que las emisiones del Proyecto representan menos

del 1% de las normativas secundarias de referencia de calidad del aire para MPS, de manera que el

Proyecto no generará un impacto significativo debido a la depositación de material particulado y no

afectará la vegetación ni cultivos cercanos, ni flora o fauna presente en el área de influencia.

Por lo tanto, es posible inferir que las emisiones asociadas a la fase de construcción del Proyecto no

se afectará la calidad del aire en los receptores cercanos, dado que las emisiones atmosféricas del

Proyecto no sobrepasan los límites de concentración establecidos en las normas de calidad del aire

primarias y secundarias, además es importante destacar que para efectos de la modelación se
consideró la simultaneidad en la construcción de las obras (en la práctica la construcción del Proyecto

no es simultánea, puesto que las actividades constructivas son realizadas de forma secuencial).

Expuesto lo detallado, se determina que el Proyecto Nueva Subestación Seccionadora Buli, no genera

un efecto adverso significativo, ni un impacto adverso para la salud de las personas ni en calidad del

aire y tampoco en las poblaciones cercanas, ni en los cultivos aledaños, ni en los recursos naturales

de la zona, ya que no sobrepasa los límites establecidos en las normativas de calidad primaria tanto

sus criterios diarios y anuales, teniendo en cuenta que los límites establecidos en las normas de

calidad primaria apuntan a proteger la salud de la población, es por esto que estas normas establecen

límites más estrictos que las normas de calidad secundaria, de igual manera las emisiones del

Proyecto cumplen con las normas de calidad secundaria, las cuales apuntan a proteger el medio

ambiente. Es importante considerar, además, que las emisiones atmosféricas generadas tanto

generadas en el Año 1 tendrán una duración acotada.

Página 51 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

En base a lo anterior es posible afirmar que el Proyecto genera un aumento marginal y despreciable

en las concentraciones de contaminantes atmosféricos producto a las emisiones acotadas a la fase

de construcción y operación, por lo tanto, no se generará una modificación en la calidad del aire de

la zona, de manera que el Proyecto no genera riesgos adicionales a la salud de población.

Página 52 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

10 Bibliografía

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

Página 53 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

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

Página 54 de 55

Declaración de Impacto Ambiental
Proyecto Nueva Subestación Seccionadora Buli

- SEA. (2022). _Guía de evaluación de efectos adversos sobre recursos naturales renovables._

- SEA, (2022). _Criterio de Evaluación en el SEIA: Objetos de protección._

- SEA. (2023). _Guía para el uso de modelos de calidad del aire en el SEIA._

- SINCA. (2023). Sistema de Información Nacional de Calidad del Aire, información histórica.

- Vargas, C. (2011). _Efectos de la fracción gruesa (PM10-2.5) del material particulado sobre la salud_

_humana._ Ministerio de Salud del Gobierno de Chile.

Página 55 de 55

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Construcción detalle del dominio de los datos meteorológicos**

| Periodo de datos de los datos | 1 enero a 31 de diciembre de 2022 |
| --- | --- |
| Punto de Referencia | Latitud: - 36.381 S<br>Longitud: - 71.904 W |
| Área de Dominio | 50x50 km |
| Proyección | Lambert Conic Conformal |
| Datum | NWS-84 6370 km Radius, Global Sphere |

**Tabla 2.: Resumen tasa de emisiones atmosféricas para el año 1**

| Contamina<br>nte | Resultados estimación de emisiones | Col3 | Col4 | Datos entrada CALPUFF | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Contamina<br>nte | Tasa emisión<br>Área Proyecto | Caminos No<br>pavimentados | Caminos<br>pavimentados | Tasa emisión<br>Área Proyecto | Caminos<br>pavimentados | Caminos No<br>pavimentados |
| Unidad | t/año | t/año | t/año | g/s/m2 | g/s/m | g/s/m |
| MP10 | 0,43772 | 1,62608 | 1,16148 | 5,49,E-07 | 5,75,E-08 | 3,29,E-10 |

**Tabla 6.: Resultados modelación año 1 material particulado**

| Receptor | MP10 (μg/m3) | Col3 | MP2,5 (μg/m3) | Col5 | MPS<br>(mg/m2/día) |
| --- | --- | --- | --- | --- | --- |
| Receptor | 24 h | Anual | 24 h | Anual | Anual |
| R1 | 0,559455 | 0,557920 | 0,407486 | 0,40637 | 4,140527 |
| R2 | 0,148258 | 0,147443 | 0,10791 | 0,10732 | 0,770999 |
| R3 | 0,308406 | 0,287283 | 0,22459 | 0,20920 | 1,461582 |
| R4 | 0,246790 | 0,233267 | 0,17975 | 0,16990 | 1,413874 |
| R5 | 0,007410 | 0,006821 | 0,00539 | 0,00497 | 0,000039 |
| R6 | 0,000755 | 0,000639 | 0,00055 | 0,00047 | 0,000001 |
| R10 | 0,061385 | 0,058021 | 0,04471 | 0,04226 | 0,186304 |
| R7 | 0,005485 | 0,005244 | 0,00399 | 0,00382 | 0,000847 |
| R8 | 0,004510 | 0,004509 | 0,00328 | 0,00328 | 0,000060 |
| R9 | 0,000937 | 0,000865 | 0,00068 | 0,00063 | 0,000001 |
| R11 | 0,000595 | 0,000548 | 0,00043 | 0,00040 | 0,000000 |
| R12 | 0,000708 | 0,000598 | 0,00052 | 0,00044 | 0,000002 |
| R13 | 0,000190 | 0,000155 | 0,00014 | 0,00011 | 0,000000 |
| R14 | 0,000171 | 0,000141 | 0,00012 | 0,00010 | 0,000000 |
| R15 | 0,000467 | 0,000422 | 0,00034 | 0,00031 | 0,000004 |
| R16 | 0,000462 | 0,000462 | 0,00033 | 0,00033 | 0,000190 |
| R17 | 0,000411 | 0,000411 | 0,00030 | 0,00030 | 0,000103 |
| R18 | 0,000312 | 0,000312 | 0,00023 | 0,00023 | 0,000024 |

**Tabla 7.: Cuerpo normativo**

| Parámetro | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio anual | 50 μg/m3 | DS N°12/2022 MMA |
| MP10 | Primaria | Promedio 24 horas<br>(Percentil 98) | 130 μg/m3 | 130 μg/m3 |
| MP2.5 | Primaria | Promedio anual | 20 μg/m3 | DS N°12/2012 MMA |
| MP2.5 | Primaria | Promedio 24 horas<br>(Percentil 98) | 50 μg/m3 | 50 μg/m3 |

**Tabla 8.: Cuerpo normativo**

| Contaminante | País | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- | --- |
| MPS <br>(Partículas<br>sedimentables) | Confederación<br>Suiza | - | Promedio<br>anual | 200<br>(mg/m2día) | Ordenanza de la<br>Confederación<br>Suiza, Sobre Control<br>de Contaminación<br>del Aire 1993 |

**Tabla 9.: Comparación material particulado con normas de calidad primaria y secundaria**

| Receptor | Tipo Receptor | MP10 (ug/m3) | Col4 | % DS N°12/2022 MMA | Col6 | MP2,5 (ug/m3) | Col8 | % DS N°12/2012 MMA | Col10 | MPS<br>(mg/m2dia) | Ordenanza<br>Confederación<br>Suiza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Tipo Receptor | 24 horas | Anual | 24 horas | Anual | 24 horas | Anual | 24 horas | Anual | Anual | 30 días |
| R1 | Agrícola | 0,559455 | 0,557920 | 0,430% | 1,116% | 0,407486 | 0,406368 | 0,815% | 2,032% | 4,1405 | 0,04141% |
| R2 | Humano | 0,148258 | 0,147443 | 0,114% | 0,295% | 0,107910 | 0,107318 | 0,216% | 0,537% | 0,7710 | 0,00771% |
| R3 | Agrícola | 0,308406 | 0,287283 | 0,237% | 0,575% | 0,224585 | 0,209203 | 0,449% | 1,046% | 1,4616 | 0,01462% |
| R4 | Red Hidrográfica | 0,246790 | 0,233267 | 0,190% | 0,467% | 0,179749 | 0,169899 | 0,359% | 0,849% | 1,4139 | 0,01414% |
| R5 | Red Hidrográfica | 0,007410 | 0,006821 | 0,006% | 0,014% | 0,005395 | 0,004966 | 0,011% | 0,025% | 0,0000 | 0,00000% |
| R6 | Humano | 0,000755 | 0,000639 | 0,001% | 0,001% | 0,000550 | 0,000465 | 0,001% | 0,002% | 0,0000 | 0,00000% |
| R10 | Agrícola | 0,061385 | 0,058021 | 0,047% | 0,116% | 0,044711 | 0,042261 | 0,089% | 0,211% | 0,1863 | 0,00186% |
| R7 | Agrícola | 0,005485 | 0,005244 | 0,004% | 0,010% | 0,003991 | 0,003816 | 0,008% | 0,019% | 0,0008 | 0,00001% |
| R8 | Red Hidrográfica | 0,004510 | 0,004509 | 0,003% | 0,009% | 0,003282 | 0,003282 | 0,007% | 0,016% | 0,0001 | 0,00000% |
| R9 | Red Hidrográfica | 0,000937 | 0,000865 | 0,001% | 0,002% | 0,000682 | 0,000630 | 0,001% | 0,003% | 0,0000 | 0,00000% |
| R11 | Humano | 0,000595 | 0,000548 | 0,000% | 0,001% | 0,000433 | 0,000399 | 0,001% | 0,002% | 0,0000 | 0,00000% |
| R12 | Humano | 0,000708 | 0,000598 | 0,001% | 0,001% | 0,000516 | 0,000435 | 0,001% | 0,002% | 0,0000 | 0,00000% |
| R13 | Humano | 0,000190 | 0,000155 | 0,000% | 0,000% | 0,000138 | 0,000113 | 0,000% | 0,001% | 0,0000 | 0,00000% |
| R14 | Humano | 0,000171 | 0,000141 | 0,000% | 0,000% | 0,000124 | 0,000102 | 0,000% | 0,001% | 0,0000 | 0,00000% |
| R15 | Humano | 0,000467 | 0,000422 | 0,000% | 0,001% | 0,000340 | 0,000307 | 0,001% | 0,002% | 0,0000 | 0,00000% |
| R16 | Humano | 0,000462 | 0,000462 | 0,000% | 0,001% | 0,000333 | 0,000333 | 0,001% | 0,002% | 0,0002 | 0,00000% |
| R17 | Humano | 0,000411 | 0,000411 | 0,000% | 0,001% | 0,000297 | 0,000297 | 0,001% | 0,001% | 0,0001 | 0,00000% |
| R18 | Atractivo<br>Turístico | 0,000312 | 0,000312 | 0,000% | 0,001% | 0,000226 | 0,000226 | 0,000% | 0,001% | 0,0000 | 0,00000% |
| R19 | Monumento<br>Histórico | 0,000349 | 0,000349 | 0,000% | 0,001% | 0,000252 | 0,000252 | 0,001% | 0,001% | 0,0001 | 0,00000% |
| R20 | Zona de<br>Conservación<br>Histórica | 0,000320 | 0,000320 | 0,000% | 0,001% | 0,000232 | 0,000232 | 0,000% | 0,001% | 0,0000 | 0,00000% |
| R21 | Humano | 0,000347 | 0,000347 | 0,000% | 0,001% | 0,000251 | 0,000251 | 0,001% | 0,001% | 0,0001 | 0,00000% |

**Tabla 10.: Potenciales impactos sobre componente calidad del aire**

| Recurso | Impacto | Posibles impactos |
| --- | --- | --- |
| Aire | Impactos en la calidad del<br>aire |  <br>Posible aumento en la concentración de material particulado<br>en el área de influencia. |
| Aire | Impacto en la calidad del<br>aire que ocasiona<br>impactos sobre otro<br>recurso natural renovable |  <br>El impacto en la calidad del aire producto del aumento de<br>concentraciones de contaminantes, ocasionar impactos sobre<br>ciertas poblaciones de especies de flora y fauna, así como<br>también sobre la calidad del suelo y cultivos.<br> <br>El impacto en la calidad del aire producto del aumento de<br>concentraciones de material particulado sedimentable puede<br>producir depositación de contaminantes en la vegetación. |

**Tabla 12.: Análisis de significancia MP10 y MP2.5 en Zonas saturadas**

| Zona Saturada | Contaminan<br>te Saturado | Receptor<br>humano Zona<br>saturada | Concentraci<br>ón proyecto<br>(ug/m3) | Valores de<br>significancia para<br>el aumento de<br>concentraciones<br>con una duración<br>1 año (ug/m3) | Resultado | Conclusión |
| --- | --- | --- | --- | --- | --- | --- |
| Decreto<br>N°36/2012 MMA | MP10 anual | R24 | 0,000019 | 3 | MP10 anual < 3<br>ug/m3<br>en todos los<br>receptores<br>humanos | El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP10 anual. |
| Decreto<br>N°36/2012 MMA | MP10 24<br>horas | R24 | 0,000024 | 10 | MP10 24 h < 10<br>ug/m3<br>en todos los<br>receptores<br>humanos | El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP10 en 24 h. |
| Decreto<br>N°36/2012 MMA | MP2.5<br>anual | R24 | 0,00001 | 0,99 | MP2.5 anual <<br>0,99 ug/m3<br>en todos los<br>receptores | El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP2.5 anual. |
| Decreto<br>N°36/2012 MMA | MP2.5 24<br>horas | R24 | 0,00002 | 5,13 | MP2.5 24 h <<br>5,13 ug/m3<br>en todos los<br>receptores | El Proyecto genera<br>aportes no<br>significativos en las<br>concentraciones de<br>MP2.5 en 24 h. |

**Tabla 13.: Análisis de significancia MP2.5 en Zonas saturada Valle Central del Ñuble**

| Zona Saturada | Contaminante<br>Saturado | Receptor<br>humano<br>Zona<br>saturada | Concentración<br>proyecto<br>(ug/m3) | Valores de<br>significancia para<br>el aumento de<br>concentraciones<br>con una duración<br>1 año (ug/m3) | Resultado | Conclusión |
| --- | --- | --- | --- | --- | --- | --- |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R2 | 0,223493 | 0,99 | MP2.5<br>anual <<br>0,99 ug/m3 <br>en todos<br>los<br>receptores<br>humanos | El Proyecto<br>genera aportes<br>no significativos<br>en las<br>concentraciones<br>de MP2.5 anual. |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R6 | 0,000978 | 0,000978 | 0,000978 | 0,000978 |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R11 | 0,000833 | 0,000833 | 0,000833 | 0,000833 |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R12 | 0,000906 | 0,000906 | 0,000906 | 0,000906 |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R13 | 0,000237 | 0,000237 | 0,000237 | 0,000237 |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R14 | 0,000215 | 0,000215 | 0,000215 | 0,000215 |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R15 | 0,000643 | 0,000643 | 0,000643 | 0,000643 |
| Decreto<br>N°66/2022<br>MMA | MP2.5 anual | R16 | 0,000726 | 0,000726 | 0,000726 | 0,000726 |
