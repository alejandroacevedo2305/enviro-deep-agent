---
title: Sin título
author: INGECAM Consultores
date: D:20230710095114-04'00'
language: es
type: manual
pages: 86
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Declaración de Impacto Ambiental “Energía Esmeralda” Anexo 4.2 Modelación de Emisiones Atmosféricas
-->

# Declaración de Impacto Ambiental “Energía Esmeralda” Anexo 4.2 Modelación de Emisiones Atmosféricas

## Energía Esmeralda SpA

Desarrollado por:

## Junio de 2023

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**INDICE DE CONTENIDOS**

1. INTRODUCCIÓN..................................................................................................................7

2. JUSTIFICACIÓN DEL MODELO A UTILIZAR ...................................................................7

2.1. Modelo de dispersión de contaminantes CALPUFF ................................................. 8

2.2. Fundamentos del modelo .......................................................................................... 10

3. PARÁMETROS DE ENTRADA MODELO CALPUFF ..................................................... 12

3.1.1. Escenario meteorológico ................................................................................... 12

3.1.1. Dominio de modelación ..................................................................................... 13

3.1.1. Uso de suelos ..................................................................................................... 15

3.1.1. Escenario de emisiones..................................................................................... 15

3.1.2. Escenario de receptores .................................................................................... 17

4. RESULTADOS MODELACIÓN ......................................................................................... 21

4.1. Escenario geofísico ................................................................................................... 21

4.1. Modelo meteorológico ............................................................................................... 26

4.2. Resultados modelación CALPUFF ........................................................................... 37

4.2.1. Material particulado ............................................................................................ 37

4.2.2. Gases de combustión ........................................................................................ 42

5. CARACTERIZACIÓN METEOROLÓGICA DEL ÁREA DEL PROYECTO ................... 48

5.1. Estación Bomberos .................................................................................................... 49

5.2. Estación San Pedro ................................................................................................... 52

6. ANALISIS DE INCERTIDUMBRE MODELO WRF ......................................................... 54

6.1. Análisis cualitativo ...................................................................................................... 54

6.2. Análisis cuantitativo ................................................................................................... 57

7. CUERPO NORMATIVO ..................................................................................................... 58

7.1. Normativa nacional de calidad del aire .................................................................... 58

P á g i n a 2 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

7.2. Normativa internacional de referencia ..................................................................... 59

8. CARACTERIZACIÓN CALIDAD DEL AIRE ..................................................................... 63

9. EVALUACIÓN DE IMPACTOS ......................................................................................... 64

9.1. Evaluación de impactos sobre la salud de la población ......................................... 64

9.2. Evaluación de impactos sobre la calidad del aire, flora y vegetación, fauna, aguas
superficiales y suelo .............................................................................................................. 76

10. ÁREA DE INFLUENCIA ..................................................................................................... 80

11. CONCLUSIONES ............................................................................................................... 83

12. BIBLIOGRAFÍA ................................................................................................................... 85

**INDICE DE TABLAS**

Tabla 1. Construcción detalle del dominio de los datos meteorológicos ........................... 13

Tabla 2. Resumen tasa de emisiones atmosféricas para el año 1 .................................... 17

Tabla 3. Receptores modelación...................................................................................... 18

Tabla 4. Campo de vientos .............................................................................................. 26

Tabla 5. Altura de la capa de mezcla ............................................................................... 35

Tabla 6. Resultados modelación año 1 material particulado ............................................ 37

Tabla 7. Resultados modelación año 1 gases de combustión .......................................... 42

Tabla 8. Estaciones caracterización meteorológica .......................................................... 48

Tabla 9. Estación Bomberos ............................................................................................ 49

Tabla 10. Estación San Pedro ......................................................................................... 52

Tabla 11. Cuerpo normativo ............................................................................................. 59

Tabla 12. Cuerpo normativo ............................................................................................. 61

Tabla 13. Resumen caracterización calidad del aire ........................................................ 63

Tabla 14. Comparación material particulado con normas de calidad primaria y secundaria
........................................................................................................................................ 66

P á g i n a 3 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Tabla 15. Comparación gases de combustión con normas de calidad primaria y
secundaria ....................................................................................................................... 69

Tabla 16. Aporte del Proyecto a condición base .............................................................. 72

Tabla 17. Nivel de significancia aporte Proyecto en Estación Bomberos ......................... 75

Tabla 18. Comparación con límites Anteproyecto PPDA ................................................. 76

Tabla 19. Potenciales impactos sobre componente calidad del aire ................................ 76

Tabla 20. Evaluación de impactos ................................................................................... 78

**INDICE DE FIGURAS**

Figura 1. Perfil de elevación ............................................................................................... 8

Figura 2. Representación Gráfica del Modelo Tipo Puff y de Pluma ................................ 10

Figura 3. Grilla meteorológica y grilla computacional ....................................................... 14

Figura 4. Uso de suelo dominio de modelación ................................................................ 15

Figura 5. Escenario de fuentes ........................................................................................ 16

Figura 6. Receptores ....................................................................................................... 20

Figura 7. Topografía ........................................................................................................ 21

Figura 8. Albedo .............................................................................................................. 22

Figura 9. Rugosidad superficial ........................................................................................ 23

Figura 10. Leaf Area Index............................................................................................... 24

Figura 11. Razón de Bowen ............................................................................................. 25

Figura 12. Rosa de los vientos año 2022 ......................................................................... 29

Figura 13. Variabilidad temporal del viento ...................................................................... 30

Figura 14. Serie de tiempo dirección del viento ................................................................ 31

Figura 15. Variación dirección del viento .......................................................................... 31

Figura 16. Serie de tiempo velocidad del viento ............................................................... 32

Figura 17. Velocidad del viento ciclo anual ...................................................................... 33

Figura 18. Ciclo diario velocidad del viento ...................................................................... 33

P á g i n a 4 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Figura 19. Velocidad del viento ........................................................................................ 34

Figura 20. Mapa de isoconcentraciones de MP10 promedio anual .................................. 39

Figura 21. Mapa de isoconcentraciones de MP10 promedio 24h ..................................... 39

Figura 22. Mapa de isoconcentraciones de MP2.5 promedio anual ................................. 40

Figura 23. Mapa de isoconcentraciones de MP2.5 promedio 24h .................................... 41

Figura 24. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio anual

........................................................................................................................................ 41

Figura 25. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio
mensual ........................................................................................................................... 41

Figura 26. Mapa de isoconcentraciones de NOx promedio anual .................................... 45

Figura 27. Mapa de isoconcentraciones de NOx 1 hora ................................................... 45

Figura 28. Mapa de isoconcentraciones de SOx promedio anual ..................................... 45

Figura 29. Mapa de isoconcentraciones de SOx promedio 24h ....................................... 46

Figura 30. Mapa de isoconcentraciones de SOx 1 hora ................................................... 47

Figura 31. Mapa de isoconcentraciones CO promedio 8 horas ........................................ 47

Figura 32. Mapa de isoconcentraciones CO 1 hora ......................................................... 48

Figura 33. Serie de tiempo velocidad viento Estación Bomberos ..................................... 49

Figura 34. Velocidad del viento ........................................................................................ 50

Figura 35. Serie de tiempo dirección viento Estación Bomberos ...................................... 50

Figura 36. Rosa de los vientos EMRP Bomberos ............................................................ 51

Figura 37. Dirección del viento EMRP Bomberos ............................................................ 51

Figura 38. Serie de tiempo velocidad viento Estación San Pedro .................................... 52

Figura 39. Velocidad del viento ........................................................................................ 52

Figura 40. Serie de tiempo dirección viento Estación EMRP San Pedro .......................... 53

Figura 41. Dirección del viento EMRP San Pedro ............................................................ 54

Figura 42. Análisis de incertidumbre cuantitativo velocidad del viento ............................. 58

Figura 43. Modelo conceptual .......................................................................................... 65

P á g i n a 5 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 44. Área de influencia calidad del aire** .............................................................. 82

P á g i n a 6 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**1. INTRODUCCIÓN**

El presente documento tiene como objetivo establecer el impacto de las emisiones del
"Proyecto Energía Esmeralda" en la calidad del aire, utilizando los resultados de la
estimación de emisiones atmosféricas, detallado en el Anexo 4.1 de la DIA.

El Proyecto se ubica en la comuna de Quillota, región de Valparaíso, la cual corresponde
a una zona declarada como saturada por material particulado MP10 en su estadístico
anual y latente por MP10 en su estadístico diario, de acuerdo con el Decreto 107 de junio
de 2019, que se enmarca sobre la provincia de Quillota y las comunas de Catemu,
Panquehue y Llay-Llay de la provincia de San Felipe de Aconcagua.

Según lo establecido por la “Guía para el uso de Modelos de Calidad del Aire en el SEIA”
(SEA, 2023), la selección del modelo meteorológico utilizado en el presente estudio se
realizó fundamentándose en las condiciones del dominio de modelación, motivo por el
cual la Guía recomienda un modelo que permita simular una meteorología heterogénea.
Por esta razón, el campo meteorológico tridimensional horario del año 2022 completo, fue
generado utilizando el modelo meteorológico WRF en su versión 4.0.3, y procesado con
MMIF v3.2. Posteriormente esta información fue utilizada como parámetro de entrada del
modelo de calidad de aire CALPUFF.

Las tasas de emisión se consideraron para el escenario más desfavorable, es decir para
el año en que el Proyecto genera mayor cantidad de emisiones atmosféricas,
correspondiente al Año 1, el cual comprende la fase de construcción completa (5 meses)
y 7 meses de la fase de operación. A partir de las emisiones estimadas, se proyectan
mediante el modelo CALPUFF, valores de concentración para material particulado y
gases de combustión, los que posteriormente serán comparados con las normas de
calidad el aire.

**2. JUSTIFICACIÓN DEL MODELO A UTILIZAR**

La "Guía para el Uso de Modelos de Calidad del Aire en el SEIA" (SEA, 2023) establece
dos criterios para la selección de un modelo de dispersión de contaminantes. El primer
criterio se basa en la distancia a lo largo del territorio nacional, donde se considera que a
menor distancia existe una mayor probabilidad de que el terreno sea homogéneo, lo que
significa que habrá menos factores que alteren significativamente el transporte y la
dilución de contaminantes. Para el análisis del modelo a elegir, este criterio considerará
una distancia lineal referencial de 5 km desde la fuente de emisión hasta la zona de

impacto de las emisiones atmosféricas. El segundo criterio se refiere al tipo de
contaminante a modelar, distinguiendo entre contaminantes primarios, que son emitidos
directamente a la atmósfera, y contaminantes secundarios, que son productos de
reacciones fisicoquímicas en la atmósfera.

En el caso específico del Proyecto, se aplicará el criterio recomendado por la "Guía para
el Uso de Modelos de Calidad del Aire en el SEIA" (SEA, 2023) para contaminantes

P á g i n a 7 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

primarios, considerando un alcance de los impactos de las emisiones mayor a los 5 km.
Para esta situación, la Guía recomienda utilizar un modelo que permita simular la
meteorología heterogénea. Los modelos de tipo "puff" y Eulerianos son capaces de
representar esta variabilidad meteorológica. La elección del modelo se basó en las
recomendaciones del apartado 3.2 de la Guía, ya que las emisiones a considerar son de
tipo primario y provienen de una fuente de emisión en un área de modelación de más de 5
kilómetros, abarcando fuentes y receptores sensibles. Además, existen factores en la
topografía del área circundante al Proyecto, donde el perfil de elevación presenta
diferencias de altura mayores a 500 metros, lo que podría afectar el carácter lineal de los

vientos.

**Figura 1. Perfil de elevación**

Fuente: Elaboración propia mediante Google Earth Pro.

Por lo tanto, siguiendo las directrices de la "Guía para el Uso de Modelos de Calidad del
Aire en el SEIA" (SEA, 2023), se utilizará un modelo que permita simular la meteorología
heterogénea. En este sentido, se ha seleccionado un modelo de tipo "puff" para llevar a
cabo la modelación de calidad del aire. A continuación, se proporciona el detalle del
modelo de tipo "puff" que se utilizará.

**2.1. Modelo de dispersión de contaminantes CALPUFF**

El sistema de modelación, tal como su nombre lo indica, incluye dos componentes
principales: WRF y CALPUFF, además de una larga selección de preprocesadores,
diseñados para incluir en el modelo datos geofísicos y de usos de suelos, y

P á g i n a 8 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

postprocesadores como por ejemplo CALPOST, que permiten convertir los resultados a
los estadísticos considerados por las normas primarias y secundarias de calidad del aire.

En cuanto a la meteorología base utilizada en la modelación, se desarrolló un modelo de
retrospectiva (Hindcast) WRF (Weather Research and Forecasting, por sus siglas en
ingles), el cual provee los datos de entrada que simulan la meteorología de un año
pasado y permiten modelar la dispersión de las emisiones en la atmósfera mediante el
software CALPUFF. En cuanto a esto, cabe destacar que, el modelo cumple con las
recomendaciones de configuración definidas por el Servicio de Evaluación Ambiental,
particularmente respecto de los documentos “Configuración WRF” y “Namelist.input”.
Adicionalmente, la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA" (SEA,
2023), establece que el modelo numérico recomendado para la generación de datos
meteorológicos es el WR, el cual corresponde a uno de simuladores meteorológicos de
pronóstico más avanzados, completos y en constante mejora, mantenido por
NCAR/NOAA de Estados Unidos. Además, ha sido utilizado en la mayoría de los
proyectos relacionados con el comportamiento atmosférico encargados por la Comisión
Nacional de Energía, Ministerio del Medio Ambiente.

Por otra parte, CALPUFF es un modelo tipo “puff”, corresponde a una combinación entre
los modelos Gaussianos y los modelos Lagrangeanos. Lo que hacen estos modelos es
esencialmente calcular la dispersión de una emisión puntual (puntual en el tiempo),
llamado puff, a lo largo de una trayectoria. Su aproximación matemática es estimar la
dispersión en forma Gaussiana en cada punto de una trayectoria. Es decir, a diferencia de
los modelos Langrangeanos que necesitan el cálculo de un gran número de trayectorias
para una fuente, en el caso de los modelos tipo puff sólo se requiere una trayectoria por
puff lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se
simulan trayectorias y la dispersión Gaussiana de muchos puff. Además, son capaces de
simular muchas fuentes y fuentes de distinto tipo al mismo tiempo (SEA, 2023). Los
modelos tipo “puff” representan una pluma de contaminantes continua como un número
discreto de paquetes de material contaminante, tal como se muestra la siguiente Figura:

P á g i n a 9 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 2. Representación Gráfica del Modelo Tipo Puff y de Pluma**

Fuente: Lakes Environmental (2006).

**2.2. Fundamentos del modelo**

CALMET

CALMET es un modelo de diagnóstico meteorológico que consta de dos módulos
principales:

 Módulo de campo de vientos.

 Módulo de capa límite

La aproximación usada por CALMET para calcular el campo de viento consiste en dos

pasos:

En el primer paso, se obtiene un campo de vientos inicial considerando únicamente los
efectos que sobre el flujo atmosférico tienen las características físicas del terreno: efectos
cinemáticos, efectos producidos por las laderas y posibilidad de bloqueos. En el segundo
paso se aplica un procedimiento objetivo sobre la base de los vientos observados en
estaciones de monitoreo, obteniendo el campo de vientos final después de un proceso
iterativo para minimizar la divergencia del campo de viento y garantizar el cumplimiento de
la ecuación de conservación de mas (EPA, 2017).

P á g i n a 10 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Cabe señalar, que en este caso solo se cargaron los datos tipo CALMET-Ready WRF
usándolos directamente, puesto que por recomendación del SEA en la “Guía para el Uso
de Modelos de Calidad del Aire en el SEIA" (SEA, 2023).

CALPUFF

El modelo CALPUFF junto con el modelo meteorológico CALMET constituye un sistema
de modelos enfocados a tratar la dispersión de contaminantes en la atmósfera.

Es un modelo Lagrangiano-Gaussiano de transporte y dispersión de soplos o “puff”
emitidos por las fuentes consideradas por el proyecto que se simulan considerando el
efecto de las condiciones meteorológicas (simuladas con CALMET) variando en el tiempo
y en el espacio sobre el transporte, transformación y eliminación de varios contaminantes.
En cuanto a distancia, puede aplicarse a escalas desde decenas a centenas de
kilómetros. Incluye algoritmos para tratar procesos a escala subgrid, así como, efectos a
gran escala. Puede tratar los efectos de terreno complejo, zonas costeras, cizalla del
viento permitiendo la división de las nubes de contaminantes, efectos de estelas de
edificios, depósito de contaminantes por vía seca y húmeda (EPA, 2023).

El modelo evalúa la contribución de un “puff” en la concentración atmosférica de un punto
de la grilla en un instante determinado, para luego permitir que el “puff” se mueva,
evolucione en tamaño, fuerza, etc., hasta la próxima iteración, en el próximo punto de la
grilla, respondiendo a la meteorología del sector en la que se encuentre inmerso el “puff”
en cada instante. Luego, la concentración total en un receptor resultará de la sumatoria de
las contribuciones de todos los “puff”. La ecuación básica del modelo se muestra a

continuación:

Dónde:

_C:_ Concentración [g/m3].
_Q:_ Masa del contaminante en el “puff” [g].
_σx:_ Coeficiente de dispersión en dirección del viento [m].
_σy:_ Coeficiente de dispersión en dirección perpendicular al viento [m].
_σz:_ Coeficiente de dispersión vertical [m].
_da:_ Distancia desde el centro del “puff” hacia el receptor en el eje de la dirección
del viento [m].
_dc:_ Distancia desde el centro del “puff” hacia el receptor en el eje perpendicular a
la dirección del viento [m].
_g:_ Altura de la ecuación gaussiana [m].

P á g i n a 11 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

_H:_ Altura efectiva del “puff” [m].
_h:_ Altura de la capa de mezcla [m].

Para casos que involucran un alto grado de variabilidad espacial del flujo dentro de la
capa límite, tales como flujos ascendentes o descendentes o flujos a lo largo de un valle
fluvial sinuoso, la suposición de estado estacionario en línea recta puede ser poco válida
incluso a algunos kilómetros de la fuente, por lo que un modelo del tipo “puff” puede ser el
más apropiado (EPA, 2017).

CALPOST

Parte fundamental del proceso de modelación con la plataforma CALMET/CALPUFF, es
el módulo CALPOST quien procesa las salidas de CALPUFF creando los archivos que
permiten realizar la evaluación de los resultados, según lo establecido en las normas de
calidad del aire. Además, es capaz de gestionar los datos de cada contaminante según el
período de tiempo requerido, ordenando las máximas concentraciones obtenidas e
identificando el momento en que cada una de éstas suceden (hora, día, mes y año) (EPA,
2017).

**3. PARÁMETROS DE ENTRADA MODELO CALPUFF**

El modelo para poder ejecutarse requiere una grilla de información, la construcción de los
escenarios a evaluar, dichos escenarios son procesados sobre la información geofísica
del área de modelación. Una vez generada esta información, se establecen las fuentes
emisoras asociadas y/o actividades a realizar por el proyecto. Lo antes mencionado es
integrado en paralelo a los receptores establecidos sobre el dominio de la modelación.
Las magnitudes de las emisiones generadas por el proyecto provienen de la estimación
de emisiones realizada con los factores AP-42 de la EPA. Estos valores en conjunto con
los obtenidos de información satelital consolidan la información real del área de influencia

directa a modelar.

**3.1.1. Escenario meteorológico**

El escenario meteorológico se construyó a partir de la información meteorológica
generado por el modelo WRF que se utilizó para desarrollar esta componente. El dominio
de modelación presenta las siguientes características:

P á g i n a 12 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Tabla 1. Construcción detalle del dominio de los datos meteorológicos**

|Periodo de datos de los datos|1 enero a 31 de diciembre de 2022|
|---|---|
|**Punto de Referencia**|Latitud: - 32.914 S<br>Longitud: - 71.268 W|
|**Área de Dominio**|50x50 km|
|**Proyección**|Lambert Conic Conformal|
|**Datum**|NWS-84 6370 km Radius, Global Sphere|
|**Resolución**|1 km|
|**Numero de Celdas en dirección x**|50|
|**Numero de Celdas en dirección y**|50|
|**Numero de Capas Verticales**|11 (entre 0 y 4000 metros de altura)|
|**Tipo de dato**|CALPUFF-Ready WRF Data (WRF.MET<br>Format)|

Fuente: Elaboración propia.

Una vez definido los datos meteorológicos se construye el dominio a procesar. Este se
implementó sobre un área de 25 km dirección Norte y Sur y 25 km dirección Este y Oeste,
desde el origen ubicado en el punto de referencia mencionado.

**3.1.1. Dominio de modelación**

El dominio de modelación del Sistema Calpuff-WRF se compone de tres tipos de grilla, la
meteorológica, la computacional y la de muestreo (sampling grid), donde: El dominio
meteorológico comprende un área de 50 [km] x 50 [km], correspondiente a la grilla del
WRF ocupado.

P á g i n a 13 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 3. Grilla meteorológica y grilla computacional**

Fuente: Elaboración propia.

Por otra parte, para definir la grilla de muestreo, se han seguido los lineamientos
establecidos en la "Guía para el Uso de Modelos de Calidad del Aire en el SEIA" (SEA,
2023). Esta guía señala que es necesario asegurarse de que el tamaño de la grilla sea lo
suficientemente amplio para garantizar la medición precisa de la concentración máxima a

nivel del suelo.

En concordancia con estas recomendaciones, se han utilizado 5 grillas de muestreo con
una configuración y espaciado óptimos para lograr un mejor desempeño del modelo.
Estas configuraciones se han basado en las recomendaciones detalladas en la
mencionada "Guía para el Uso de Modelos de Calidad del Aire en el SEIA" (SEA, 2023).

Al seguir estos criterios, se busca obtener una representación precisa de la calidad del
aire en el área de estudio, considerando la cuantificación de la concentración máxima y
garantizando la fiabilidad de los resultados obtenidos. Es importante destacar que el uso
de estas grillas de muestreo en conformidad con las recomendaciones de la Guía
contribuye a fortalecer la robustez de la evaluación de la calidad del aire.

P á g i n a 14 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**3.1.1. Uso de suelos**

La información relacionada con el uso de suelo de la zona se obtiene a través de los

archivos Global Land Cover Characterization (GLCC) publicados por el U.S Geological
Survey (USGS). En la siguiente Figura se presenta el uso de suelos para el dominio de
modelación.

**Figura 4. Uso de suelo dominio de modelación**

Fuente: Elaboración propia.

De la Figura anterior el uso de suelo 51 corresponde a “Corrientes y canales”, el uso de
suelo 40 corresponde a “Bosques”, el uso de suelo 30 corresponde a “Pastizales”, el uso
de suelo 20 corresponde a “Tierra agrícola” y el uso de suelo 10 corresponde a “Urbano”.

Se aprecia que en el dominio de modelación existen diversos usos de suelo. En el sector
de emplazamiento del proyecto se identifica el uso de suelo de tipo “Tierra agrícola”.

**3.1.1. Escenario de emisiones**

A continuación, se presenta el escenario a modelar, donde se contemplan las fuentes de
emisión de material particulado y gases de combustión para el peor escenario posible a
modo de descartar afectaciones a la salud de la población. Cabe destacar, que se
considera la construcción del proyecto dentro del año 1 de este, dado que es el período

P á g i n a 15 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

más crítico del Proyecto, el cual abarca la fase de construcción (5 meses), más 7 meses
de la fase de operación.

De manera conservadora, se considera que todas las emisiones de las actividades
constructivas son producidas de manera simultánea en el predio del Proyecto, lo que en la
práctica no ocurrirá, puesto que las actividades constructivas son realizadas de forma
secuencial.

En el contexto de la modelación, se han considerado las emisiones generadas por el
tránsito y la combustión en caminos pavimentados, las cuales están representadas en
color azul. Además, se han tenido en cuenta las emisiones provenientes de caminos no
pavimentados, las cuales están representadas en color verde. Por otro lado, se han
considerado las emisiones generadas por diversas actividades en el área del proyecto,
como maquinaria fuera de ruta, grupos electrógenos, excavaciones, nivelación,
perforaciones y movimiento de tierra, y se han representado en color rojo.

**Figura 5. Escenario de fuentes**

Fuente: Elaboración propia.

De las emisiones presentadas en la estimación de emisiones para el año 1, la
resuspensión por tránsito en vías pavimentadas se asocian a la fuente denominada
“Caminos pavimentados”, en el caso de la resuspensión por tránsito en vías no
pavimentadas se asocian a la fuente denominada “Caminos No pavimentados”,

P á g i n a 16 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

finalmente, las emisiones asociadas a excavaciones, movimiento de tierra, compactación,
nivelación, perforación, maquinaria fuera de ruta y grupos electrógenos, se asocia a la
fuente de área denominada “Área Proyecto”, como se detalla en la siguiente Tabla.

**Tabla 2. Resumen tasa de emisiones atmosféricas para el año 1**

|Contami<br>nante|Resultados estimación de emisiones|Col3|Col4|Datos entrada CALPUFF|Col6|Col7|
|---|---|---|---|---|---|---|
|**Contami**<br>**nante**|**Tasa**<br>**emisión**<br>**Área**<br>**Proyecto**|**Caminos No**<br>**pavimentad**<br>**os**|**Caminos**<br>**pavimentado**<br>**s **|**Tasa emisión**<br>**Área Proyecto**|**Caminos**<br>**pavimentad**<br>**os**|**Caminos No**<br>**pavimentad**<br>**os**|
|**Unidad**|**t/año**|**t/año**|**t/año**|**g/s/m2 **|**g/s/m**|**g/s/m**|
|**MP10**|0,57565|0,11332|1,39000|5,893, E-08|6,654, E-08|1,102, E-05|
|**MP2.5**|0,11939|0,02935|0,13370|1,222, E-08|1,724, E-08|1,060, E-06|
|**MPS**|1,73983|0,57958|4,36330|1,781, E-07|3,403, E-07|3,459, E-05|
|**No**|0,48155|0,12231|0,00644|4,930, E-08|7,182, E-08|5,103, E-08|
|**SOx**|0,02757|0,00012|0,00001|2,822, E-09|7,060, E-11|5,016, E-11|
|**CO**|0,13740|0,02762|0,00145|1,407, E-08|1,622, E-08|1,152, E-08|
|**Tipo de**<br>**fuente**|Areal|Lineal|Lineal|Areal|Lineal|Lineal|

Fuente: Elaboración propia.

**3.1.2. Escenario de receptores**

Los receptores discretos han sido definidos siguiendo las directrices establecidas en la
"Guía para el uso de modelos de calidad del aire en el SEIA" (SEA, 2023). Esta guía
señala que los receptores deben ser seleccionados considerando las características
específicas del lugar, la duración de su presencia y los usos permitidos del suelo.
Además, se deben tener en cuenta los objetivos de protección identificados en la zona,
los cuales se han establecido siguiendo las directrices del documento "Criterio de
Evaluación en el SEIA: Objetos de protección" (SEA, 2022). En dicho documento, los
objetos de protección se definen como elementos o componentes del medio ambiente que
se derivan del marco legal vigente, en particular del artículo 11 de la Ley N°19.300 Sobre
Bases Generales del Medio Ambiente, y de los artículos 5° al 10 del Decreto Supremo
N°40/2012 del Ministerio del Medio Ambiente, que establece el Reglamento del SEIA
(RSEIA). Estos objetos de protección deben ser salvaguardados de los posibles impactos
ambientales que pueda generar la ejecución de un proyecto o actividad dentro del marco
del Sistema de Evaluación de Impacto Ambiental (SEIA).

Adicionalmente, la “Guía para el uso de modelos de calidad del aire en el SEIA" (SEA,
2023), señala que para el caso de los receptores humanos se debe considerar una altura

P á g i n a 17 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

de inmisión de entre 1,5 a 1,8 metros, correspondiente a la altura promedio de la zona de
inhalación de los contaminantes atmosféricos por el cuerpo humano.

A continuación, se presentan los receptores identificados.

**Tabla 3. Receptores modelación**

|Tipo Receptor|Id|Coordenadas|Col4|Distanc<br>ia al<br>Proyect<br>o [m]|Descripción|
|---|---|---|---|---|---|
|**Tipo Receptor**|**Id**|**WGS84 Huso 19S**|**WGS84 Huso 19S**|**WGS84 Huso 19S**|**WGS84 Huso 19S**|
|**Tipo Receptor**|**Id**|**Este [m]**|**Sur [m]**|**Sur [m]**|**Sur [m]**|
|**Sitio Prioritario**|R1|286097,04|6356959,13|1295|Humedal Río<br>Aconcagua/Rio A|
|**Atractivo Turístico**|R2|291530,00|6355927,00|2898|Hacienda Patrimonial<br>San Isidro|
|**Monumento**<br>**Histórico**|R3|289654,00|6359611,00|3883|Casa Colonial|
|**Atractivo Turístico**|R4|289702,00|6359822,00|4095|Cruz de Mayo Quillota|
|**Atractivo Turístico**|R5|289773,00|6359762,00|4070|Plaza de Armas Quillota|
|**Atractivo Turístico**|R6|289821,00|6359732,00|4063|Templo de Santo<br>Domingo|
|**Reserva de la**<br>**Biósfera**|R10|301345,72|6351464,10|13428|La Campana-Peñuelas|
|**Atractivo Turístico**|R7|290072,00|6359778,00|4212|Turístico Museo Casa<br>del Huasco|
|**Atractivo Turístico**|R8|289944,00|6360284,00|4615|Turístico Museo<br>Histórico Arqueológico|
|**Industrial**|R9|284144,14|6363242,49|7529|Viña El Sauce|
|**Industrial**|R11|280836,00|6350953,00|8227|Viña Narbona Wines|
|**Establecimiento de**<br>**salud**|R12|287054,04|6353236,13|2671|SAPU y CESFAM San<br>Pedro|
|**Establecimiento de**<br>**salud**|R13|288424,95|6358420,32|2274|CESFAM Cardenal Raúl<br>Silva Henríquez|
|**Establecimiento de**<br>**salud**|R14|288783,04|6359763,99|3644|Hospital San Martín<br>Quillota|
|**Establecimiento de**<br>**salud**|R15|290578,61|6359334,07|4037|Centro Comunitario de<br>Salud Familiar<br>(CECOSF)|
|**Establecimiento**<br>**educacional**|R16|287604,99|6356829,60|485|Liceo Agrícola de<br>Quillota|
|**Establecimiento**<br>**educacional**|R17|288585,68|6357973,88|1943|Escuela Especial Los<br>Robles|
|**Establecimiento**<br>**educacional**|R18|288750,87|6358367,73|2369|Colegio República de<br>México|
|**Establecimiento**<br>**educacional**|R19|287561,70|6353308,34|2377|Escuela Básica Abel<br>Guerrero Aguirre|
|**Sitio Prioritario**|R20|283661,32|6348674,83|8301|Sitio Prioritario Estero<br>Limache|
|**Cuerpos de agua**|R21|288694,12|6354518,85|1007|Estero San Isidro|
|**Cuerpos de agua**|R22|290578,95|6355880,43|1946|Quebrada Sin Nombre|
|**Humano**|R23|287279,00|6355968,00|163|Viviendas|

P á g i n a 18 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Tipo Receptor|Id|Coordenadas|Col4|Distanc<br>ia al<br>Proyect<br>o [m]|Descripción|
|---|---|---|---|---|---|
|**Tipo Receptor**|**Id**|**WGS84 Huso 19S**|**WGS84 Huso 19S**|**WGS84 Huso 19S**|**WGS84 Huso 19S**|
|**Tipo Receptor**|**Id**|**Este [m]**|**Sur [m]**|**Sur [m]**|**Sur [m]**|
|**Humano**|R24|287744,00|6355788,00|172|Viviendas|
|**Humano**|R25|287936,00|6355776,00|21|Viviendas|
|**Humano**|R26|288145,00|6355627,00|51|Viviendas|
|**Humano**|R27|287860,00|6355545,00|260|Viviendas|
|**Humano**|R28|288398,00|6356737,00|747|Viviendas|
|**Agrícola**|R29|287301,00|6356135,00|6|Cultivos|
|**Agrícola**|R30|287506,16|6356385,46|42|Cultivos|
|**Agrícola**|R31|287534,79|6355884,48|149|Instalaciones agrícolas|
|**Agrícola**|R32|287305,77|6356428,40|28|Instalaciones agrícolas|
|**Estación EMRP**|R33|291759,00|6363531,00|8325|Estación SINCA La Cruz|
|**Estación EMRP**|R35|293403,00|6358533,00|5498|Estación SINCA La<br>Palma|
|**Estación EMRP**|R34|289818,00|6359202,00|3583|Estación SINCA Cuerpo<br>de Bomberos Quillota|
|**Estación EMRP**|R36|287422,00|6353393,00|2358|Estación SINCA San<br>Pedro|
|**Estación EMRP**|R37|278154,00|6355829,00|9013|Estación SINCA<br>Manzanar|
|**Humano**|R38|287417,97|6353995,72|1830|Viviendas|
|**Humano**|R39|287945,00|6354669,00|986|Viviendas|
|**Humano**|R40|288721,00|6355623,00|157|Viviendas|
|**Humano**|R41|288941,00|6355962,00|348|Viviendas|
|**Humano**|R42|289539,00|6356970,00|1482|Viviendas|
|**Humano**|R43|288551,00|6355373,00|149|Viviendas|
|**Humano**|R44|282513,00|6352672,00|5844|Viviendas|
|**Humano**|R45|282346,00|6352894,00|5849|Viviendas|
|**Humano**|R46|281925,00|6353163,00|6060|Viviendas|
|**Humano**|R47|281704,00|6353159,00|6254|Viviendas|
|**Humano**|R48|281119,00|6352492,00|7096|Viviendas|
|**Humano**|R49|281368,00|6352312,00|6985|Viviendas|

Fuente: Elaboración propia.

P á g i n a 19 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 6. Receptores**

Fuente: Elaboración propia.

P á g i n a 20 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**4. RESULTADOS MODELACIÓN**

A continuación, se presentan los resultados obtenidos, en cuanto a la concentración
estimada de contaminantes respecto a las distancias discretas establecidas (receptores).
En el Apéndice A y en el Apéndice B se incluyen los resultados del modelo WRF y
CALPUFF respectivamente.

**4.1. Escenario geofísico**

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1,
cuya resolución es aproximadamente 30 m.

**Figura 7. Topografía**

Fuente: Elaboración propia.

El Proyecto se encuentra ubicado en un sector donde la topografía resulta pronunciada en
algunos sectores, puesto que se emplaza entre cerros de mediana y baja altura y a una
distancia donde posee influencia del borde costero, por lo que se consideran aquellos
accidentes geográficos o relieve en altura, dentro del modelo.

En los siguientes gráficos se presentan los datos de terreno obtenidos para la modelación.

P á g i n a 21 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 8. Albedo**

Fuente: Elaboración propia.

P á g i n a 22 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 9. Rugosidad superficial**

Fuente: Elaboración propia.

P á g i n a 23 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 10. Leaf Area Index**

Fuente: Elaboración propia.

P á g i n a 24 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 11. Razón de Bowen**

Fuente: Elaboración propia.

P á g i n a 25 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**4.1. Modelo meteorológico**

Mediante el uso del modelo CALMET y en función de los datos de entrada WRF descritos
en el escenario meteorológico, se procedió a generar una matriz de vientos
predominantes y alturas aproximadas de capas de mezclas al interior del dominio de la
modelación, para cada hora del año 2022.

Con el fin de presentar los resultados a través de una gráfica de campos de viento, se ha
seleccionado el día 8 de marzo de 2022 como una fecha representativa dentro del
dominio de modelación. La siguiente tabla muestra el comportamiento de los vientos a
una altura de 10 metros sobre el nivel del suelo, para diferentes horarios de la fecha
mencionada.

|Tabla 4. Campo de vientos|Col2|
|---|---|
|**Campo de Viento**|**Descripción**|
|<br>|Comportamiento<br>de los vientos a<br>una altura 10<br>metros sobre el<br>nivel de suelo a<br>las 08:00 horas<br>como una hora<br>representativa<br>del 8 de marzo<br>de<br>2022<br>al<br>interior<br>del<br>dominio de la<br>modelación.|

P á g i n a 26 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Campo de Viento|Descripción|
|---|---|
||Comportamiento<br>de los vientos a<br>una altura 10<br>metros sobre el<br>nivel de suelo a<br>las 12:00 horas<br>como una hora<br>representativa<br>del 8 de marzo<br>de<br>2022<br>al<br>interior<br>del<br>dominio de la<br>modelación.|
|<br> <br>|Comportamiento<br>de los vientos a<br>una altura 10<br>metros sobre el<br>nivel de suelo a<br>las 16:00 horas<br>como una hora<br>representativa<br>del 8 de marzo<br>de<br>2022<br>al<br>interior<br>del<br>dominio de la<br>modelación.|

P á g i n a 27 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Campo de Viento|Descripción|
|---|---|
||Comportamiento<br>de los vientos a<br>una altura 10<br>metros sobre el<br>nivel de suelo a<br>las 20:00 horas<br>como una hora<br>representativa<br>del 8 de marzo<br>de<br>2022<br>al<br>interior<br>del<br>dominio de la<br>modelación.|
||<br>Comportamiento<br>de los vientos a<br>una altura 10<br>metros sobre el<br>nivel de suelo a<br>las 24:00 horas<br>como una hora<br>representativa<br>del 8 de marzo<br>de<br>2022<br>al<br>interior<br>del<br>dominio de la<br>modelación.|

Fuente: Elaboración propia.

P á g i n a 28 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Dirección del viento

Con respecto a la dirección del viento, en la siguiente Figura presenta la rosa de los
vientos correspondiente al dominio de modelación. La componente principal corresponde
al viento Suroeste (SO).

**Figura 12. Rosa de los vientos año 2022**

Fuente: Elaboración propia.

A continuación, se presentan las rosas de los vientos que muestran la variabilidad
temporal de la velocidad y dirección del viento durante el periodo de modelación.

P á g i n a 29 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 13. Variabilidad temporal del viento**

|Rosa de los vientos período 00:00 AM - 05:00<br>AM entre el 01/01/2022 - 31/12/2022|Rosa de los vientos período 06:00 AM -<br>11:00 AM entre el 01/01/2022 - 31/12/2022|
|---|---|
|**Rosa de los vientos período 12:00 PM - 17:00**<br>**PM entre el 01/01/2022 - 31/12/2022**|**Rosa de los vientos período 18:00 PM -**<br>**23:00 PM entre el 01/01/2022 - 31/12/2022**|

Fuente: Elaboración propia.

P á g i n a 30 | 86

Velocidad del viento:

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 14. Serie de tiempo dirección del viento**

Fuente: Elaboración propia.

**Figura 15. Variación dirección del viento**

Fuente: Elaboración propia, 2022.

P á g i n a 31 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Con respecto a la velocidad del ciento, a continuación, se presentan gráficos de velocidad
de viento y ciclos, diarios, semanales y mensuales de la velocidad del viento.

**Figura 16. Serie de tiempo velocidad del viento**

Fuente: Elaboración propia.

P á g i n a 32 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 17. Velocidad del viento ciclo anual**

Fuente: Elaboración propia.

**Figura 18. Ciclo diario velocidad del viento**

Fuente: Elaboración propia.

P á g i n a 33 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 19. Velocidad del viento**

Fuente: Elaboración propia.

Altura de la capa de mezcla

Por otra parte, la profundidad vertical de la atmósfera donde se produce el mezclado, se
denomina capa de mezcla. La parte superior de esta capa se conoce como altura de
mezcla, la cual determina el alcance vertical del proceso de dispersión de los
contaminantes liberados debajo de ella, a continuación, se representa la altura de la capa
de mezcla mediante procesamiento de datos meteorológicos en el software CALPUFF
View.

P á g i n a 34 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Tabla 5. Altura de la capa de mezcla|Col2|
|---|---|
|**Altura de la capa de mezcla**|**Descripción**|
|<br> <br>|Presentación<br>del<br>comportamiento de la<br>altura de<br>capa<br>de<br>mezcla<br>en<br>horarios<br>representativos, entre<br>las 00:00 y las 08:00<br>del día escogido para<br>exponer los resultados<br>del<br>módulo<br>micro<br>meteorológico (8 de<br>marzo de 2022) como<br>representativo<br>de<br>verano<br>como<br>peor<br>escenario<br>(menor<br>humedad ambiental y<br>menor presencia de<br>lluvias).<br>En<br>ese<br>sentido,<br>se<br>puede<br>observar que, por la<br>temperatura ambiente<br>y <br>las<br>variables<br>ambientales<br>nocturnas, la altura de<br>la capa de mezcla se<br>mantiene<br>relativamente baja, sin<br>sobrepasar<br>los<br>700<br>metros en la mayoría<br>de los puntos.|
|||

P á g i n a 35 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Altura de la capa de mezcla|Descripción|
|---|---|
|<br> <br>|Presentación<br>del<br>comportamiento de la<br>altura de<br>capa<br>de<br>mezcla<br>en<br>horarios<br>representativos, entre<br>las 16:00 y las 20:00<br>del día escogido para<br>exponer los resultados<br>del<br>módulo<br>micro<br>meteorológico.<br>Se<br>puede observar que,<br>por<br>la<br>temperatura<br>ambiente<br>y <br>las<br>variables ambientales<br>diurnas, la altura de la<br>capa de mezcla se<br>expande por sobre los<br>2300<br>metros.<br>De<br>manera<br>que<br>se<br>alcanzan<br>los<br>1800<br>metros en la mayoría<br>de<br>los<br>puntos,<br>volviendo a contraerse<br>en la tarde a los 1400<br>metros.|
|||

Fuente: Elaboración propia.

P á g i n a 36 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**4.2. Resultados modelación CALPUFF**

**4.2.1. Material particulado**

Con el fin de determinar la eventual influencia que tiene el Proyecto en la calidad del aire
sobre la localidad y los receptores identificados, en función de los análisis antes
realizados, se determinaron las concentraciones de MP10, MP2.5 y MPS para cada una
de las horas del año sobre los receptores considerados. A continuación, se presenta el
aporte del proyecto sobre a los receptores antes mencionados, segregado según los
períodos de la norma de calidad del aire aplicable.

**Tabla 6. Resultados modelación año 1 material particulado**

|Receptor|MP10 (μg/m3)|Col3|MP2,5 (μg/m3)|Col5|MPS (mg/m2/día)|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**24 h**|**Anual**|**24 h**|**Anual**|**30 días**|**Anual**|
|**R1 **|0,0653|0,0653|0,0087|0,0087|0,0222|0,0221|
|**R2 **|0,0292|0,0292|0,0040|0,0040|0,0002|0,0002|
|**R3 **|0,0180|0,0180|0,0027|0,0027|0,0024|0,0024|
|**R4 **|0,0161|0,0161|0,0024|0,0024|0,0024|0,0025|
|**R5 **|0,0169|0,0169|0,0026|0,0026|0,0032|0,0033|
|**R6 **|0,0174|0,0174|0,0027|0,0027|0,0040|0,0040|
|**R10 **|0,0200|0,0200|0,0034|0,0034|0,0132|0,0132|
|**R7 **|0,0141|0,0141|0,0023|0,0023|0,0058|0,0058|
|**R8 **|0,0019|0,0019|0,0003|0,0003|0,0000|0,0000|
|**R9 **|0,0008|0,0008|0,0001|0,0001|0,0000|0,0000|
|**R11 **|0,0019|0,0019|0,0003|0,0003|0,0000|0,0000|
|**R12 **|0,0135|0,0135|0,0019|0,0019|0,0003|0,0003|
|**R13 **|0,0433|0,0433|0,0061|0,0061|0,0064|0,0064|
|**R14 **|0,0154|0,0154|0,0022|0,0022|0,0003|0,0003|
|**R15 **|0,0250|0,0250|0,0040|0,0040|0,0096|0,0095|
|**R16 **|0,6200|0,6200|0,0907|0,0907|0,6673|0,6642|
|**R17 **|0,0931|0,0931|0,0155|0,0155|0,0889|0,0886|
|**R18 **|0,0484|0,0484|0,0070|0,0070|0,0108|0,0108|
|**R19 **|0,0149|0,0149|0,0020|0,0020|0,0003|0,0003|

P á g i n a 37 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Receptor|MP10 (μg/m3)|Col3|MP2,5 (μg/m3)|Col5|MPS (mg/m2/día)|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**24 h**|**Anual**|**24 h**|**Anual**|**30 días**|**Anual**|
|**R20 **|0,0016|0,0016|0,0002|0,0002|0,0000|0,0000|
|**R21 **|0,0927|0,0927|0,0128|0,0128|0,0395|0,0392|
|**R22 **|0,0568|0,0568|0,0077|0,0077|0,0042|0,0042|
|**R23 **|0,9081|0,9081|0,1314|0,1314|0,0000|0,0000|
|**R24 **|1,1196|1,1196|0,1596|0,1596|0,0000|0,0000|
|**R25 **|2,4951|2,4951|0,3662|0,3662|0,0000|0,0000|
|**R26 **|2,5370|2,5370|0,3957|0,3957|0,0000|0,0000|
|**R27 **|0,8252|0,8252|0,1193|0,1193|0,0000|0,0000|
|**R28 **|0,5229|0,5229|0,0731|0,0731|0,0000|0,0000|
|**R29 **|2,8227|2,8227|0,3824|0,3824|4,8613|4,8357|
|**R30 **|3,2069|3,2069|0,4183|0,4183|5,6326|5,6174|
|**R31 **|0,9487|0,9487|0,1400|0,1400|1,0739|1,0657|
|**R32 **|2,7003|2,7003|0,4006|0,4006|4,6613|4,6612|
|**R33 **|0,0060|0,0060|0,0010|0,0010|0,0029|0,0029|
|**R35 **|0,0243|0,0243|0,0037|0,0037|0,0054|0,0054|
|**R34 **|0,0141|0,0141|0,0020|0,0020|0,0000|0,0000|
|**R36 **|0,0141|0,0141|0,0019|0,0019|0,0003|0,0003|
|**R37 **|0,0010|0,0010|0,0002|0,0002|0,0001|0,0001|
|**R38 **|0,0243|0,0243|0,0033|0,0033|0,0016|0,0016|
|**R39 **|0,1437|0,1437|0,0201|0,0201|0,0827|0,0821|
|**R40 **|1,0137|1,0137|0,1523|0,1523|1,3373|1,3298|
|**R41 **|0,8480|0,8480|0,1247|0,1247|0,9206|0,9203|
|**R42 **|0,1294|0,1294|0,0173|0,0173|0,0276|0,0274|
|**R43 **|0,5576|0,5576|0,0843|0,0843|0,6482|0,6427|
|**R44 **|0,0053|0,0053|0,0009|0,0009|0,0035|0,0035|
|**R45 **|0,0064|0,0064|0,0012|0,0012|0,0074|0,0074|

P á g i n a 38 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Receptor|MP10 (μg/m3)|Col3|MP2,5 (μg/m3)|Col5|MPS (mg/m2/día)|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**24 h**|**Anual**|**24 h**|**Anual**|**30 días**|**Anual**|
|**R46 **|0,0146|0,0146|0,0034|0,0034|0,0349|0,0351|
|**R47 **|0,0210|0,0210|0,0051|0,0051|0,0584|0,0586|
|**R48 **|0,0039|0,0039|0,0008|0,0008|0,0021|0,0021|
|**R49 **|0,0037|0,0037|0,0007|0,0007|0,0014|0,0014|

Fuente: Elaboración propia.

A continuación, se presentan los mapas de isoconcentraciones asociados a cada uno de
los parámetros para el material particulado MP10, MP2,5, MPS, tanto para las
concentraciones anuales como para las concentraciones diarias.

**Figura 20. Mapa de isoconcentraciones de MP10 promedio anual**

Fuente: Elaboración propia.

**Figura 21. Mapa de isoconcentraciones de MP10 promedio 24h**

P á g i n a 39 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Fuente: Elaboración propia.

**Figura 22. Mapa de isoconcentraciones de MP2.5 promedio anual**

Fuente: Elaboración propia.

P á g i n a 40 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 23. Mapa de isoconcentraciones de MP2.5 promedio 24h**

Fuente: Elaboración propia.

**Figura 24. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio anual**

Fuente: Elaboración propia.

**Figura 25. Mapa de isoconcentraciones depositación húmeda y seca MPS promedio mensual**

P á g i n a 41 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Fuente: Elaboración propia.

**4.2.2. Gases de combustión**

**Tabla 7. Resultados modelación año 1 gases de combustión**

|Receptor|NOx (μg/m3)|Col3|SOx (μg/m3)|Col5|Col6|CO (μg/m3)|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**1 h**|**Anual**|**1 hora**|**24 h**|**Anual**|**1 hora**|**8 horas**|
|**R1 **|0,01925|0,01000|0,00927|0,00271|5,36,E-04|0,01093|0,00383|
|**R2 **|0,01715|0,00588|0,00846|0,00151|3,22,E-04|0,00934|0,00208|
|**R3 **|0,00849|0,00432|0,00406|0,00104|1,62,E-04|0,00472|0,00146|
|**R4 **|0,00878|0,00393|0,00420|0,00094|1,43,E-04|0,00479|0,00132|
|**R5 **|0,01023|0,00437|0,00490|0,00102|1,49,E-04|0,00555|0,00143|
|**R6 **|0,01237|0,00470|0,00594|0,00108|1,53,E-04|0,00662|0,00152|
|**R10 **|0,01611|0,00775|0,00773|0,00154|1,55,E-04|0,00875|0,00220|
|**R7 **|0,01653|0,00447|0,00793|0,00096|1,14,E-04|0,00856|0,00137|
|**R8 **|0,01628|0,00031|0,00784|0,00009|1,55,E-05|0,00789|0,00012|
|**R9 **|0,01754|0,00014|0,00844|0,00004|7,45,E-06|0,00846|0,00005|
|**R11 **|0,01857|0,00040|0,00892|0,00011|1,62,E-05|0,00898|0,00015|
|**R12 **|0,02025|0,00257|0,00970|0,00069|1,28,E-04|0,01010|0,00093|
|**R13 **|0,02351|0,00832|0,01128|0,00212|3,65,E-04|0,01259|0,00298|

P á g i n a 42 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Receptor|NOx (μg/m3)|Col3|SOx (μg/m3)|Col5|Col6|CO (μg/m3)|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**1 h**|**Anual**|**1 hora**|**24 h**|**Anual**|**1 hora**|**8 horas**|
|**R14 **|0,02088|0,00283|0,01000|0,00077|1,36,E-04|0,01047|0,00107|
|**R15 **|0,02353|0,00832|0,01125|0,00168|2,29,E-04|0,01237|0,00248|
|**R16 **|0,10639|0,17430|0,05303|0,04065|9,35,E-03|0,07696|0,05719|
|**R17 **|0,03759|0,03709|0,01780|0,00707|6,52,E-04|0,02255|0,01012|
|**R18 **|0,02433|0,01112|0,01166|0,00262|4,14,E-04|0,01331|0,00370|
|**R19 **|0,01987|0,00278|0,00947|0,00075|1,44,E-04|0,00990|0,00101|
|**R20 **|0,01841|0,00035|0,00877|0,00009|1,81,E-05|0,00882|0,00012|
|**R21 **|0,02690|0,01795|0,01257|0,00457|1,00,E-03|0,01535|0,00655|
|**R22 **|0,02318|0,01105|0,01127|0,00283|6,12,E-04|0,01293|0,00393|
|**R23 **|0,15126|0,26777|0,07366|0,06409|1,51,E-02|0,10864|0,08503|
|**R24 **|0,17665|0,31905|0,08814|0,07548|1,81,E-02|0,12965|0,10110|
|**R25 **|0,44522|0,85666|0,23187|0,19271|4,86,E-02|0,33669|0,25831|
|**R26 **|0,54303|1,05266|0,28439|0,23314|5,99,E-02|0,41146|0,31408|
|**R27 **|0,13908|0,24508|0,07073|0,05888|1,39,E-02|0,10269|0,07777|
|**R28 **|0,07937|0,12616|0,03825|0,03030|7,08,E-03|0,05586|0,04230|
|**R29 **|0,39016|0,74803|0,20070|0,17078|4,21,E-02|0,29252|0,22580|
|**R30 **|0,37832|0,72471|0,19386|0,16271|4,07,E-02|0,28429|0,22156|
|**R31 **|0,16275|0,29399|0,08037|0,06974|1,66,E-02|0,11903|0,09395|
|**R32 **|0,49947|0,96741|0,25664|0,21497|5,43,E-02|0,37388|0,28874|
|**R33 **|0,01662|0,00235|0,00795|0,00051|5,02,E-05|0,00827|0,00068|
|**R35 **|0,01860|0,00665|0,00893|0,00151|2,19,E-04|0,00988|0,00213|
|**R34 **|0,01678|0,00326|0,00812|0,00082|1,74,E-04|0,00857|0,00109|
|**R36 **|0,01634|0,00270|0,00783|0,00073|1,37,E-04|0,00824|0,00096|
|**R37 **|0,01513|0,00032|0,00727|0,00007|7,99,E-06|0,00732|0,00010|
|**R38 **|0,01704|0,00458|0,00817|0,00123|2,34,E-04|0,00887|0,00164|
|**R39 **|0,03057|0,03183|0,01479|0,00824|1,78,E-03|0,01946|0,01112|

P á g i n a 43 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Receptor|NOx (μg/m3)|Col3|SOx (μg/m3)|Col5|Col6|CO (μg/m3)|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**1 h**|**Anual**|**1 hora**|**24 h**|**Anual**|**1 hora**|**8 horas**|
|**R40 **|0,18648|0,34378|0,09367|0,07578|1,95,E-02|0,13796|0,10812|
|**R41 **|0,14205|0,25512|0,07285|0,05918|1,45,E-02|0,10709|0,08296|
|**R42 **|0,02647|0,02418|0,01303|0,00606|1,33,E-03|0,01664|0,00855|
|**R43 **|0,10659|0,18436|0,05124|0,04165|1,05,E-02|0,07564|0,05922|
|**R44 **|0,01532|0,00208|0,00737|0,00044|3,42,E-05|0,00765|0,00060|
|**R45 **|0,01590|0,00333|0,00765|0,00064|3,44,E-05|0,00807|0,00088|
|**R46 **|0,02041|0,01239|0,00983|0,00205|3,91,E-05|0,01129|0,00293|
|**R47 **|0,02399|0,01956|0,01153|0,00321|4,41,E-05|0,01380|0,00454|
|**R48 **|0,01501|0,00174|0,00719|0,00039|2,12,E-05|0,00743|0,00050|
|**R49 **|0,01484|0,00142|0,00713|0,00033|2,22,E-05|0,00733|0,00043|

Fuente: Elaboración propia.

A continuación, se presentan los mapas de isoconcentraciones asociados a cada uno de
los parámetros para gases de combustión, tanto para las concentraciones anuales como
para las concentraciones diarias.

P á g i n a 44 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 26. Mapa de isoconcentraciones de NOx promedio anual**

Fuente: Elaboración propia.

**Figura 27. Mapa de isoconcentraciones de NOx 1 hora**

Fuente: Elaboración propia.

**Figura 28. Mapa de isoconcentraciones de SOx promedio anual**

P á g i n a 45 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Fuente: Elaboración propia.

**Figura 29. Mapa de isoconcentraciones de SOx promedio 24h**

Fuente: Elaboración propia.

P á g i n a 46 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 30. Mapa de isoconcentraciones de SOx 1 hora**

Fuente: Elaboración propia.

**Figura 31. Mapa de isoconcentraciones CO promedio 8 horas**

Fuente: Elaboración propia.

P á g i n a 47 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 32. Mapa de isoconcentraciones CO 1 hora**

Fuente: Elaboración propia.

**5. CARACTERIZACIÓN METEOROLÓGICA DEL ÁREA DEL PROYECTO**

La meteorología de superficie utilizada para caracterizar el área del Proyecto corresponde
a los registros horarios de velocidad y dirección del viento, pertenecientes a las
estaciones meteorológicas San Pedro y Bomberos, ubicadas cercanas al Proyecto. Es
importante mencionar que ambas estaciones son parte de la red de monitoreo del SINCA
y cuentan con representatividad poblacional.

Las coordenadas UTM de la estación indicada se presentan en la siguiente Tabla junto

con las variables monitoreadas.

**Tabla 8. Estaciones caracterización meteorológica**

|Estación SINCA|Coordenadas UTM|Col3|Variables<br>Meteorológicas<br>Registradas|
|---|---|---|---|
|**Estación SINCA**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|**Estación San**<br>**Pedro**|287422,00|6353393,00|Dirección del viento<br>Velocidad del viento|
|**Estación**<br>**Bomberos**|289818,00|6359202,00|Dirección del viento<br>Velocidad del viento|

Fuente: Elaboración propia en base a SINCA (2023).

P á g i n a 48 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**5.1. Estación Bomberos**

En la siguiente Tabla se presentan las variables meteorológicas medidas en la estación,
junto con el porcentaje de registros válidos. Se destaca que el porcentaje de datos válidos
es del 91,4%, cumpliendo así con las recomendaciones establecidas en la "Guía para el
uso de modelos de calidad del aire en el SEIA" (2023). Esta guía sugiere que el
porcentaje de datos válidos en un año debe ser superior al 75%.

**Tabla 9. Estación Bomberos**

|Variable|Año|N° Registros<br>válidos|% Registros<br>válidos|
|---|---|---|---|
|**Dirección del**<br>**viento**|2022|8010|91,4%|
|**Velocidad del**<br>**viento**|2022|8010|91,4%|

Fuente: Elaboración propia en base a SINCA (2023).

Velocidad del viento

La serie de tiempo de la velocidad del viento registrada en la estación Bomberos durante
el año 2022 se presenta en la siguiente Figura. La velocidad del viento promedio
registrada en la estación Bomberos es de 1,7 m/s. Las velocidades del viento más bajas
se presentan durante el período nocturno y comienzan a aumentar desde las 7 de la
mañana. En promedio, las velocidades más altas se registran entre las 15 y las 16 horas
(3,4 m/s).

**Figura 33. Serie de tiempo velocidad viento Estación Bomberos**

Fuente: Elaboración propia en base a SINCA (2023).

P á g i n a 49 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 34. Velocidad del viento**

Fuente: Elaboración propia.

Dirección del viento

En la siguiente Figura se muestran los registros horarios de la dirección del viento,
obtenidos en la estación Bomberos, además se presenta la rosa de viento elaborada con
dichos registros. Cabe destacar que la dirección del viento predominante corresponde a la
dirección suroeste (SO).

**Figura 35. Serie de tiempo dirección viento Estación Bomberos**

Fuente: Elaboración propia en base a SINCA (2023).

P á g i n a 50 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 36. Rosa de los vientos EMRP Bomberos**

Fuente: Elaboración propia en base a SINCA (2023).

**Figura 37. Dirección del viento EMRP Bomberos**

Fuente: Elaboración propia en base a SINCA (2023).

P á g i n a 51 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**5.2. Estación San Pedro**

En la siguiente Tabla se presentan las variables meteorológicas medidas en la estación,
junto con el porcentaje de registros válidos. Se destaca que el porcentaje de datos válidos
está sobre 79,73%, cumpliendo así con las recomendaciones establecidas en la "Guía
para el uso de modelos de calidad del aire en el SEIA" (2023). Esta guía sugiere que el
porcentaje de datos válidos en un año debe ser superior al 75%.

|Col1|Tabla 10. Estación San Pedro|Col3|
|---|---|---|
|**Variable**|**Año**|**% Registros válidos**|
|**Velocidad y dirección del**<br>**viento**|2018|99,69%|
|**Velocidad y dirección del**<br>**viento**|2019|79,73%|
|**Velocidad y dirección del**<br>**viento**|2020|99,99%|

Fuente: Elaboración propia en base a SINCA (2023).

Velocidad del viento

La serie de tiempo de la velocidad del viento registrada en la estación San Pedro durante
los años 2018, 2019 y 2020, se presenta en la siguiente Figura. La velocidad del viento
promedio registrada el 2020 es de 1,33 m/s, al igual que para el año 2018. Las
velocidades del viento más bajas se presentan durante el período nocturno y comienzan a
aumentar desde las 8 de la mañana. En promedio, las velocidades más altas se registran
entre las 14 y las 15 horas, con velocidades promedio de 3,7 m/s.

**Figura 38. Serie de tiempo velocidad viento Estación San Pedro**

Fuente: Elaboración propia en base a SINCA (2023).

**Figura 39. Velocidad del viento**

P á g i n a 52 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Fuente: Elaboración propia.

Dirección del viento

En la siguiente Figura se muestran los registros horarios de la dirección del viento,
obtenidos en la estación San Pedro.

**Figura 40. Serie de tiempo dirección viento Estación EMRP San Pedro**

Fuente: Elaboración propia en base a SINCA (2023).

P á g i n a 53 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Figura 41. Dirección del viento EMRP San Pedro**

Fuente: Elaboración propia en base a SINCA (2023).

**6. ANALISIS DE INCERTIDUMBRE MODELO WRF**

Para validar los resultados del modelo WRF, a continuación, se presenta un Análisis de
Incertidumbre, de acuerdo con los lineamientos de la “Guía para el uso de Modelos de
Calidad del Aire en el SEIA” (SEA, 2023). Para efectos de la Guía se indica que la
incertidumbre será expresada a través de las diferencias, tanto cualitativas como
cuantitativas, entre los datos modelados y observados en el dominio de modelación. Es
imprescindible analizar la incertidumbre del modelo meteorológico para expresar cuán
“válida” es la simulación de la dispersión de contaminantes respecto a la información
disponible al momento de presentar un proyecto en el SEIA.

**6.1. Análisis cualitativo**

A continuación, para la variable meteorológica velocidad del viento, en la siguiente
Ilustración, se presentan la comparación de los ciclos diarios junto con los ciclos

mensuales.

P á g i n a 54 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

En relación al ciclo diario de la velocidad del viento observada y modelada, es posible
indicar que el modelo se adapta de buena forma a la realidad, ya que logra reproducir la
variación promedio a través de las horas del día, simulando de buena forma los valores
extremos. Por otra parte, se observa que el modelo sobrestima ligeramente las
velocidades durante el ciclo diario.

Con respecto a la dirección del viento, a continuación, se analizan las rosas de los vientos
para el escenario modelado y observado.

**Rosa de los vientos observada EMRP Bomberos**

P á g i n a 55 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Col1|Col2|Col3|
|---|---|---|
|**Rosa de los vientos**<br> <br>|**Rosa de los vientos**<br> <br>|**Rosa de los vientos**<br> <br>|

**Diagrama dirección vientos EMRP Bomberos**

P á g i n a 56 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

Tal como puede observarse, el modelo predice de forma satisfactoria la principal
componente suroeste observadas durante el año 2022. Adicionalmente, el modelo
también reconoce la componente secundaria de vientos proveniente del noreste. Por otra
parte, se observa que el modelo durante el día y la noche predice de manera satisfactoria
la dirección de viento.

**6.2. Análisis cuantitativo**

Según establece la “Guía para el uso de Modelos de Calidad del Aire en el SEIA” (SEA,
2023), el análisis cuantitativo se debe realizar calculando como mínimo las métricas

P á g i n a 57 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

estadísticas del sesgo (error medio o BIAS), error absoluto medio (MAE) y la raíz del error
cuadrático medio (RMSE). Tanto BIAS como MAE son estimadores de la diferencia entre
el valor modelado y observado de un mismo fenómeno, en este caso meteorológico. De
igual forma, RMSE es un estimador de la frecuencia de las diferencias entre los valores
observados y modelados, siendo especialmente sensible a los valores atípicos, por lo
tanto, a mayor diferencia entre estos valores menor será el grado de ajuste de este
estadístico.

Adicionalmente, la “Guía para el uso de Modelos de Calidad del Aire en el SEIA” (SEA,
2023), recomienda incorporar el coeficiente de correlación (r), que corresponde a una
medida de la correlación lineal entre dos conjuntos de variables, siendo para este caso,
los valores modelados y observados.

A continuación, se presentan los parámetros estadísticos calculados entre los valores
observados de velocidad del viendo y los valores modelados.

**Figura 42. Análisis de incertidumbre cuantitativo velocidad del viento**

|Estadístico|Valor|Valor aceptable según “Guía<br>para el uso de Modelos de<br>Calidad del Aire en el SEIA”<br>(SEA, 2023).|Cumplimiento|
|---|---|---|---|
|**BIAS**|-0,514 (m/s)|[-2,5 ; 2,5] (m/s)|Cumple|
|**MAE**|0,514 (m/s)|≤3 (m/s)|Cumple|
|**RMSE**|1,378 (m/s)|≤3,5 (m/s)|Cumple|
|**Coeficiente de**<br>**correlación (r)**|0,749|>0,6|Cumple|

Fuente: Elaboración propia.

Se establece que las diferencias entre valores modelados y observados de velocidad del
viento están dentro de un rango aceptable, considerando que los estadísticos BIAS, MAE
y RMSE presentan valores por debajo de los 2 m/s. Adicionalmente. se observa un
coeficiente de correlación de 0,749 entre valores modelados y observados, lo que permite
concluir que el modelo WRF se ajusta satisfactoriamente a los valores observados.

**7. CUERPO NORMATIVO**

**7.1. Normativa nacional de calidad del aire**

En el contexto legal, la normativa nacional vigente referente a las normas primarias y
secundarias de calidad del aire, aplicables a todo el territorio nacional, establecen límites
máximos de concentración de contaminantes, como se detalla en la siguiente Tabla.

P á g i n a 58 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**Tabla 11. Cuerpo normativo**

|Parámetro|Norma|Estadístico|Valor<br>límite|Referencia|
|---|---|---|---|---|
|**MP10**|Primaria|Promedio anual|50 μg/m3|DS N°12/2022 MMA|
|**MP10**|Primaria|Promedio 24 horas<br>(Percentil 98)|130 μg/m3|130 μg/m3|
|**MP2.5**|Primaria|Promedio anual|20 μg/m3|DS N°12/2012 MMA|
|**MP2.5**|Primaria|Promedio 24 horas<br>(Percentil 98)|50 μg/m3|50 μg/m3|
|**NO2 **|Primaria|Promedio Anual|100 μg/m3|DS N°114/2002<br>MINSEGPRES|
|**NO2 **|Primaria|Promedio 1 hora<br>(Percentil 99)|400 μg/m3|400 μg/m3|
|**CO**|Primaria|Promedio horario<br>(Percentil 99)|30000<br>μg/m3|DS N°115/2002<br>MINSEGPRES|
|**CO**|Primaria|Promedio 8 horas<br>(Percentil 99)|10000<br>μg/m3|10000<br>μg/m3|
|**SO2**|Primaria|Promedio Anual|60 μg/m3|DS N°104/2018 MMA|
|**SO2**|Primaria|Promedio 24 horas<br>(Percentil 99)|150 μg/m3|150 μg/m3|
|**SO2**|Primaria|Promedio 1 hora<br>(Percentil 98,5)|350 μg/m3|350 μg/m3|
|**SO2**|Secundaria<br>Zona norte|Promedio Anual|80 μg/m3|DS N°22/2010<br>MINSEGPRES|
|**SO2**|Secundaria<br>Zona norte|Promedio 24 horas<br>(Percentil 99,7)|365 μg/m3|365 μg/m3|
|**SO2**|Secundaria<br>Zona norte|Promedio 1 hora<br>(Percentil 99,73)|1000 μg/m3|1000 μg/m3|

Fuente: Elaboración propia en base a MINSEGPRES (2002), MINSEGPRES (2010), MMA (2011),

MMA (2018), MMA (2022).

**7.2. Normativa internacional de referencia**

Con respecto al contaminante MPS no existe normativa nacional aplicable a la ubicación
del Proyecto, por lo tanto, se utilizará una norma de referencia internacional para
comparar las emisiones de este contaminante. De acuerdo a lo establecido en el artículo
11 del DS N°40/2012 del SEIA, para la utilización de las normas de referencia, se
priorizará aquel Estado que posea similitud en sus componentes ambientales, con la
situación nacional y/o local, por ello se consideró utilizar la normativa argentina y
normativa de la Confederación Suiza. A continuación, se justifica su utilización:

- **Normativa Argentina:**

Según la clasificación climática de Köppen, Chile presenta los siguientes climas: Desértico
(BWh, BWk), Semiárido (BWk, BSk), Mediterráneo (Csa, Csb), Tropical (Cfa), Templado
oceánico (Cfb), Subpolar oceánico (Cfc), Semiárido (Bsk), Alpino, Tundra (ET) y Clima
polar (EF). En tanto Argentina presenta los siguientes climas: Tropical monzónico (Am),
Tropical de sabana con invierno seco (Aw), Árido (BWh, BWk), Semiárido (BSh, BSk),
Mediterráneo oceánico (verano suave) (Csb), Mediterráneo subalpino con verano seco

P á g i n a 59 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

(Csc), Subtropical con invierno seco (verano cálido) (Cwa), Templado de montaña con
invierno seco (verano suave) (Cwb), Subalpino con invierno seco (Cwc), Subtropical
húmedo o sin estación seca (verano cálido) (Cfa), Oceánico templado (verano suave)
(Cfb), Subpolar oceánico (Cfc), Hemiboreal mediterráneo (verano suave) (Dsb), Subpolar
con verano seco (verano breve) (Dsc), Subpolar sin estación seca (verano breve) (Dfc),
Tundra (ET) y Clima polar (EF) (Koppen, 1918). De acuerdo a lo anterior, ambos países
comparten 9 tipos de climas.

En términos de especies vegetales, es posible afirmar que, en Argentina se catalogan
alrededor de 9938 especies de flora vascular, de las cuales 1800 (18%) se encuentran en
alguna categoría de amenaza (Grossi, Gutiérrez y Deluchi, 2013), en tanto para Chile se
reconocen alrededor de 5471 plantas vasculares de las cuales 443 (8,1%), están en
alguna categoría de amenaza (Rodríguez et al, 2018).

Respecto a la legislación ambiental Argentina, el Decreto 1.074/2018 que establece las
normas de calidad de aire para Argentina, indica que su propósito es “la protección a las
fuentes de provisión y a los cursos y cuerpos receptores de agua y a la atmósfera”.

Conforme a lo anterior, es posible concluir que Chile y Argentina presentan una
composición climática relativamente similar en tanto, la magnitud de plantas vasculares en
categoría de amenaza en la situación argentina es mayor a la chilena. Por otra parte, la
normativa argentina señala como objeto de protección a cursos y cuerpos receptores de
agua y la atmósfera, lo que le otorga validez a esta norma, para ser usada como
referencia en el establecimiento de límites para contaminantes ambientales como MPS,
toda vez que, en el entorno del área del Proyecto, existe presencia recursos naturales
como agua y aire susceptibles de ser impactados por MPS.

En el Apéndice C del Anexo 4.2 de la DIA (Modelación de Emisiones Atmosféricas) se
incluye un ejemplar íntegro y vigente del Decreto 1.074/2018.

- **Normativa Confederación Suiza:**

En términos climáticos, según la clasificación climática de Köppen, Chile presenta los
siguientes climas: Desértico (BWh, BWk), Semiárido (BWk, BSk), Mediterráneo (Csa,
Csb), Tropical (Cfa), Templado oceánico (Cfb), Subpolar oceánico (Cfc), Semiárido (Bsk),
Alpino, Tundra (ET) y Clima polar (EF), en tanto Suiza presenta los siguientes climas:
Semiárido (BSh, Bsk), Templado oceánico (Cfb), Subpolar oceánico (Cfc), Tropical (Cfa),
Boreal (Dfc), Alpino, Tundra (ET) y Polar (EF) (Koppen, 1918). De acuerdo a lo anterior,
ambos países comparten 7 tipos de climas, siendo el clima templado oceánico (Cfb) el
más representativo.

En términos de especies vegetales, es posible afirmar que, en Suiza, se catalogan
alrededor de 2592 especies de flora vascular, de las cuales 790 (30,5%) se encuentran en
alguna categoría de amenaza (Cordillot & Klaus, 2011), en tanto para Chile se reconocen

P á g i n a 60 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

alrededor de 5471 plantas vasculares de las cuales 443 (8,1%), están en alguna categoría
de amenaza (Rodríguez et al, 2018).

Por otro lado, la Ordenanza que establece la norma de calidad de aire para la
Confederación Suiza indica en su Capítulo 1, artículo 1 que: “La norma está orientada a
proteger seres humanos, animales y plantas, sus comunidades biológicas y hábitats, y el
suelo, de los efectos dañinos o perjuicios causados por la contaminación del aire”.
Mientras que en su artículo 2 define “Los niveles de contaminación del aire son excesivos
si uno o más de los valores límite para un contaminante especificado en el anexo 7 es
excedido. En caso que el valor límite para un contaminante no este especificado, se
considerará excesivo si:

`o` Ponen en peligro a seres humanos, animales, plantas o sus comunidades

biológicas o hábitats.
`o` Un estudio establezca que afecta significativamente el bienestar de una

proporción sustancial de la población.
`o` Provoque daño a edificaciones.
`o` Dañe la fertilidad del suelo, vegetación o aguas.”

Conforme a lo anterior, es posible concluir que Chile y Suiza presentan una composición
climática relativamente similar en tanto, la magnitud de plantas vasculares en categoría de
amenaza en la situación suiza es mayor a la chilena. Por otra parte, la norma de la
Confederación Suiza señala como objeto de protección a las comunidades biológicas o
hábitats de plantas y animales, suelo, vegetación y aguas, lo que le otorga validez a esta
norma, para ser usada como referencia en el establecimiento de límites para
contaminantes ambientales como MPS, toda vez que, en el entorno del área del Proyecto,
existe presencia de recursos naturales susceptibles de ser impactados por MPS.

En el Apéndice C del Anexo 4.2 de la DIA (Modelación de Emisiones Atmosféricas) se
incluye un ejemplar íntegro y vigente de la Ordenanza de la Confederación Suiza sobre
control de la contaminación atmosférica.

A continuación, se presenta un resumen de los límites de MPS establecidos en las
normativas internacionales a utilizar como referencia.

**Tabla 12. Cuerpo normativo**

|Contaminante|País|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|---|
|**MPS** <br>**(Partículas**<br>**sedimentables)**|Confederación<br>Suiza|-|Promedio<br>anual|200<br>(mg/m2día)|Ordenanza de la<br>Confederación<br>Suiza, Sobre<br>Control de<br>Contaminación<br>del Aire 1993|

P á g i n a 61 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Contaminante|País|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|---|
||Argentina|-|Promedio<br>mensual|1 (mg/cm2 30<br>días)<br>= <br>10000 (mg/m2 <br>30 días)|Decreto<br>1.074/2018<br>Argentina|

Fuente: Elaboración propia.

P á g i n a 62 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

**8. CARACTERIZACIÓN CALIDAD DEL AIRE**

A continuación, se describe el resumen de la caracterización de la calidad del aire en el
área de influencia del Proyecto, considerando las estaciones meteorológicas del Sistema
de Información Nacional de Calidad del Aire.

**Tabla 13. Resumen caracterización calidad del aire**

|Estación<br>EMRP|Contaminan<br>te|Periodo|Estadígrafo|Valo<br>r|Unida<br>d|Norm<br>a|%<br>Norm<br>a|
|---|---|---|---|---|---|---|---|
|**Bombero**<br>**s **|MP2,5|2020|P9824 horas|47|ug/m3|50|94%|
|**Bombero**<br>**s **|MP2,5|2019-2020|Promedio|22|ug/m3|20|111%|
|**Bombero**<br>**s **|MP10|2020|P9824 horas|75|ug/m3|130|58%|
|**Bombero**<br>**s **|MP10|2018-2020|Promedio anual|43|ug/m3|50|87%|
|**Bombero**<br>**s **|CO|2020|P99 máximo diarios 8<br>horas|3|mg/m3|10|31%|
|**Bombero**<br>**s **|CO|2020|P99 máximos diarios 1<br>hora|2|mg/m3|30|16%|
|**Bombero**<br>**s **|NO2|2020|P99 máximos diarios 1<br>hora|61|ug/m3|400|15%|
|**Bombero**<br>**s **|NO2|2018-2020|Promedio anual|17|ug/m3|100|17%|
|**Bombero**<br>**s **|SO2|2020|P98,5 1 hora|23|ug/m3|350|7%|
|**Bombero**<br>**s **|SO2|2020|P99 24 horas|18|ug/m3|150|12%|
|**Bombero**<br>**s **|SO2|2018-2020|Promedio anual|4|ug/m3|60|7%|
|**La Cruz**|MP10|2020|P9824 horas|77|ug/m3|130|59%|
|**La Cruz**|MP10|2018-2020|Promedio anual|39|ug/m3|50|78%|
|**La Cruz**|CO|2020|P99 máximo diarios 8<br>horas|2|mg/m3|10|20%|
|**La Cruz**|CO|2020|P99 máximos diarios 1<br>hora|1|mg/m3|30|5%|
|**La Cruz**|NO2|2020|P99 máximos diarios 1<br>hora|82|ug/m3|400|21%|
|**La Cruz**|NO2|2018-2020|Promedio anual|17|ug/m3|100|17%|
|**La Cruz**|SO2|2020|P98,5 1 hora|22|ug/m3|350|6%|
|**La Cruz**|SO2|2020|P99 24 horas|14|ug/m3|150|9%|
|**La Cruz**|SO2|2018-2020|Promedio anual|5|ug/m3|60|9%%|
|**La Palma**|MP10|2020|P9824 horas|61|ug/m3|130|50%|
|**La Palma**|MP10|2018-2020|Promedio anual|37|ug/m3|50|74%|
|**La Palma**|CO|2020|P99 máximo diarios 8<br>horas|2|mg/m3|10|15%|
|**La Palma**|CO|2020|P99 máximos diarios 1<br>hora|1|mg/m3|30|3%|
|**La Palma**|NO2|2020|P99 máximos diarios 1<br>hora|49|ug/m3|400|12%|
|**La Palma**|NO2|2018-2020|Promedio anual|10|ug/m3|100|20%|
|**La Palma**|SO2|2020|P98,5 1 hora|20|ug/m3|350|65%|
|**La Palma**|SO2|2020|P99 24 horas|12|ug/m3|150|8%|
|**La Palma**|SO2|2018-2020|Promedio anual|4|ug/m3|60|7%|
|**Manzana**<br>**r **|MP10|2020|P9824 horas|72|ug/m3|130|55%|
|**Manzana**<br>**r **|MP10|2018-2020|Promedio anual|36|ug/m3|50|72%|

P á g i n a 63 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

|Estación<br>EMRP|Contaminan<br>te|Periodo|Estadígrafo|Valo<br>r|Unida<br>d|Norm<br>a|%<br>Norm<br>a|
|---|---|---|---|---|---|---|---|
||CO|2020|P99 máximo diarios 8<br>horas|1|mg/m3|10|14%|
||CO|2020|P99 máximos diarios 1<br>hora|1|mg/m3|30|3%|
||NO2|2020|P99 máximos diarios 1<br>hora|68|ug/m3|400|17%|
||NO2|2018-2020|Promedio anual|11|ug/m3|100|22%|
||SO2|2020|P98,5 1 hora|25|ug/m3|350|7%|
||SO2|2020|P99 24 horas|16|ug/m3|150|11%|
||SO2|2018-2020|Promedio anual|5|ug/m3|60|8%|
|**San**<br>**Pedro**|MP2,5|2020|P9824 horas|36|ug/m3|50|71%|
|**San**<br>**Pedro**|MP2,5|2019-2020|Promedio|19|ug/m3|20|93%|
|**San**<br>**Pedro**|MP10|2020|P9824 horas|67|ug/m3|130|52%|
|**San**<br>**Pedro**|MP10|2018-2020|Promedio anual|38|ug/m3|50|77%|
|**San**<br>**Pedro**|CO|2020|P99 máximo diarios 8<br>horas|1|mg/m3|10|14%|
|**San**<br>**Pedro**|CO|2020|P99 máximos diarios 1<br>hora|1|mg/m3|30|3%|
|**San**<br>**Pedro**|NO2|2020|P99 máximos diarios 1<br>hora|83|ug/m3|400|21%|
|**San**<br>**Pedro**|NO2|2018-2020|Promedio anual|14|ug/m3|100|28%|
|**San**<br>**Pedro**|SO2|2020|P98,5 1 hora|23|ug/m3|350|6%|
|**San**<br>**Pedro**|SO2|2020|P99 24 horas|13|ug/m3|150|9%|
|**San**<br>**Pedro**|SO2|2018-2020|Promedio anual|5|ug/m3|60|8%|

Fuente: Elaboración propia en base a SINCA (2023).

**9. EVALUACIÓN DE IMPACTOS**

**9.1. Evaluación de impactos sobre la salud de la población**

Siguiendo los lineamientos establecidos en la “Guía para la Evaluación de Impacto
Ambiental de Riesgo para la Salud de la Población en el SEIA” (SEA, 2023), se procede a
realizar un análisis de los aportes del Proyecto, para determinar si generan un incremento
significativo en las concentraciones de material particulado y gases de combustión en el
área de influencia.

**Ruta de exposición:**

Los contaminantes serán emitidos a la atmósfera directamente desde la fuente de

generación, ya sea por alguna actividad de movimiento de tierra, o mediante el
funcionamiento de algún vehículo o maquinaria que los ocasione. Los contaminantes se
transportarán a través de la atmósfera, pudiendo sedimentar si se dieran las condiciones.
Los puntos de exposición de esos contaminantes se encontrarán dentro de los límites del
área del proyecto, además de las rutas externas de transporte. La vía de exposición de
estos contaminantes es por inhalación, y la población receptora corresponde a viviendas,

P á g i n a 64 | 86

Anexo 11 Consideración del Cambio Climático

DIA Energía Esmeralda

establecimientos educacionales y establecimientos de salud, además de cultivos
agrícolas.

**Figura 43. Modelo conceptual**

Fuente: Elaboración propia.

A continuación, se presenta la comparación de las emisiones del Proyecto con las normas
de calidad primaria vigentes y secundarias de referencia.

P á g i n a 65 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

**Tabla 14. Comparación material particulado con normas de calidad primaria y secundaria**

|Recepto<br>r|MP10 (ug/m3)|Col3|% DS N°12/2022<br>MMA|Col5|MP2,5 (ug/m3)|Col7|% DS N°12/2012<br>MMA|Col9|MPS<br>(mg/m2dia)|Col11|Ordenanza<br>Confederación<br>Suiza|Decreto<br>1.074/201<br>8<br>Argentina|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Recepto**<br>**r **|**24**<br>**horas**|**Anual**|**24 horas**|**Anual**|**24**<br>**horas**|**Anual**|**24 horas**|**Anual**|**30**<br>**días**|**Anual**|**30 días**|**Anual**|
|**R1**|0,06534|0,0653<br>4|0,050%|0,131%|0,00868|0,0086<br>8|0,017%|0,043%|0,0222|0,022<br>1|0,011%|0,000%|
|**R2**|0,02915|0,0291<br>5|0,022%|0,058%|0,00400|0,0040<br>0|0,008%|0,020%|0,0002|0,000<br>2|0,000%|0,000%|
|**R3**|0,01802|0,0180<br>2|0,014%|0,036%|0,00268|0,0026<br>8|0,005%|0,013%|0,0024|0,002<br>4|0,001%|0,000%|
|**R4**|0,01610|0,0161<br>0|0,012%|0,032%|0,00241|0,0024<br>1|0,005%|0,012%|0,0024|0,002<br>5|0,001%|0,000%|
|**R5**|0,01693|0,0169<br>3|0,013%|0,034%|0,00256|0,0025<br>6|0,005%|0,013%|0,0032|0,003<br>3|0,002%|0,000%|
|**R6**|0,01744|0,0174<br>4|0,013%|0,035%|0,00267|0,0026<br>7|0,005%|0,013%|0,0040|0,004<br>0|0,002%|0,000%|
|**R10**|0,02000|0,0200<br>0|0,015%|0,040%|0,00337|0,0033<br>7|0,007%|0,017%|0,0132|0,013<br>2|0,007%|0,000%|
|**R7**|0,01412|0,0141<br>2|0,011%|0,028%|0,00227|0,0022<br>7|0,005%|0,011%|0,0058|0,005<br>8|0,003%|0,000%|
|**R8**|0,00187|0,0018<br>7|0,001%|0,004%|0,00026|0,0002<br>6|0,001%|0,001%|0,0000|0,000<br>0|0,000%|0,000%|
|**R9**|0,00076|0,0007<br>6|0,001%|0,002%|0,00010|0,0001<br>0|0,000%|0,001%|0,0000|0,000<br>0|0,000%|0,000%|
|**R11**|0,00186|0,0018<br>6|0,001%|0,004%|0,00028|0,0002<br>8|0,001%|0,001%|0,0000|0,000<br>0|0,000%|0,000%|
|**R12**|0,01346|0,0134<br>6|0,010%|0,027%|0,00187|0,0018<br>7|0,004%|0,009%|0,0003|0,000<br>3|0,000%|0,000%|
|**R13**|0,04329|0,0432<br>9|0,033%|0,087%|0,00607|0,0060<br>7|0,012%|0,030%|0,0064|0,006<br>4|0,003%|0,000%|
|**R14**|0,01540|0,0154<br>0|0,012%|0,031%|0,00218|0,0021<br>8|0,004%|0,011%|0,0003|0,000<br>3|0,000%|0,000%|
|**R15**|0,02500|0,0250<br>0|0,019%|0,050%|0,00397|0,0039<br>7|0,008%|0,020%|0,0096|0,009<br>5|0,005%|0,000%|
|**R16**|0,61995|0,6199<br>5|0,477%|1,240%|0,09066|0,0906<br>6|0,181%|0,453%|0,6673|0,664<br>2|0,334%|0,007%|

P á g i n a 66 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

|Recepto<br>r|MP10 (ug/m3)|Col3|% DS N°12/2022<br>MMA|Col5|MP2,5 (ug/m3)|Col7|% DS N°12/2012<br>MMA|Col9|MPS<br>(mg/m2dia)|Col11|Ordenanza<br>Confederación<br>Suiza|Decreto<br>1.074/201<br>8<br>Argentina|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Recepto**<br>**r **|**24**<br>**horas**|**Anual**|**24 horas**|**Anual**|**24**<br>**horas**|**Anual**|**24 horas**|**Anual**|**30**<br>**días**|**Anual**|**30 días**|**Anual**|
|**R17**|0,09312|0,0931<br>2|0,072%|0,186%|0,01548|0,0154<br>8|0,031%|0,077%|0,0889|0,088<br>6|0,044%|0,001%|
|**R18**|0,04839|0,0483<br>9|0,037%|0,097%|0,00700|0,0070<br>0|0,014%|0,035%|0,0108|0,010<br>8|0,005%|0,000%|
|**R19**|0,01492|0,0149<br>2|0,011%|0,030%|0,00205|0,0020<br>5|0,004%|0,010%|0,0003|0,000<br>3|0,000%|0,000%|
|**R20**|0,00164|0,0016<br>4|0,001%|0,003%|0,00023|0,0002<br>3|0,000%|0,001%|0,0000|0,000<br>0|0,000%|0,000%|
|**R21**|0,09272|0,0927<br>2|0,071%|0,185%|0,01276|0,0127<br>6|0,026%|0,064%|0,0395|0,039<br>2|0,020%|0,000%|
|**R22**|0,05683|0,0568<br>3|0,044%|0,114%|0,00773|0,0077<br>3|0,015%|0,039%|0,0042|0,004<br>2|0,002%|0,000%|
|**R23**|0,90809|0,9080<br>9|0,699%|1,816%|0,13137|0,1313<br>7|0,263%|0,657%|0,0000|0,000<br>0|0,000%|0,000%|
|**R24**|1,11961|1,1196<br>0|0,861%|2,239%|0,15962|0,1596<br>2|0,319%|0,798%|0,0000|0,000<br>0|0,000%|0,000%|
|**R25**|2,49513|2,4951<br>2|1,919%|4,990%|0,36622|0,3662<br>2|0,732%|1,831%|0,0000|0,000<br>0|0,000%|0,000%|
|**R26**|2,53703|2,5370<br>3|1,952%|5,074%|0,39572|0,3957<br>2|0,791%|1,979%|0,0000|0,000<br>0|0,000%|0,000%|
|**R27**|0,82518|0,8251<br>7|0,635%|1,650%|0,11933|0,1193<br>3|0,239%|0,597%|0,0000|0,000<br>0|0,000%|0,000%|
|**R28**|0,52291|0,5229<br>1|0,402%|1,046%|0,07315|0,0731<br>5|0,146%|0,366%|0,0000|0,000<br>0|0,000%|0,000%|
|**R29**|2,82272|2,8227<br>1|2,171%|5,645%|0,38237|0,3823<br>7|0,765%|1,912%|4,8613|4,835<br>7|2,431%|0,048%|
|**R30**|3,20689|3,2069<br>0|2,467%|6,414%|0,41829|0,4182<br>9|0,837%|2,091%|5,6326|5,617<br>4|2,816%|0,056%|
|**R31**|0,94868|0,9486<br>8|0,730%|1,897%|0,14003|0,1400<br>3|0,280%|0,700%|1,0739|1,065<br>7|0,537%|0,011%|
|**R32**|2,70033|2,7003<br>2|2,077%|5,401%|0,40056|0,4005<br>6|0,801%|2,003%|4,6613|4,661<br>2|2,331%|0,047%|
|**R33**|0,00605|0,0060|0,005%|0,012%|0,00104|0,0010|0,002%|0,005%|0,0029|0,002|0,001%|0,000%|

P á g i n a 67 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

|Recepto<br>r|MP10 (ug/m3)|Col3|% DS N°12/2022<br>MMA|Col5|MP2,5 (ug/m3)|Col7|% DS N°12/2012<br>MMA|Col9|MPS<br>(mg/m2dia)|Col11|Ordenanza<br>Confederación<br>Suiza|Decreto<br>1.074/201<br>8<br>Argentina|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Recepto**<br>**r **|**24**<br>**horas**|**Anual**|**24 horas**|**Anual**|**24**<br>**horas**|**Anual**|**24 horas**|**Anual**|**30**<br>**días**|**Anual**|**30 días**|**Anual**|
|||5||||4||||9|||
|**R35**|0,02429|0,0242<br>9|0,019%|0,049%|0,00370|0,0037<br>0|0,007%|0,018%|0,0054|0,005<br>4|0,003%|0,000%|
|**R34**|0,01415|0,0141<br>5|0,011%|0,028%|0,00196|0,0019<br>6|0,004%|0,010%|0,0000|0,000<br>0|0,000%|0,000%|
|**R36**|0,01408|0,0140<br>8|0,011%|0,028%|0,00194|0,0019<br>4|0,004%|0,010%|0,0003|0,000<br>3|0,000%|0,000%|
|**R37**|0,00101|0,0010<br>1|0,001%|0,002%|0,00017|0,0001<br>7|0,000%|0,001%|0,0001|0,000<br>1|0,000%|0,000%|
|**R38**|0,02426|0,0242<br>6|0,019%|0,049%|0,00332|0,0033<br>2|0,007%|0,017%|0,0016|0,001<br>6|0,001%|0,000%|
|**R39**|0,14370|0,1437<br>0|0,111%|0,287%|0,02009|0,0200<br>9|0,040%|0,100%|0,0827|0,082<br>1|0,041%|0,001%|
|**R40**|1,01369|1,0136<br>9|0,780%|2,027%|0,15225|0,1522<br>5|0,305%|0,761%|1,3373|1,329<br>8|0,669%|0,013%|
|**R41**|0,84799|0,8479<br>9|0,652%|1,696%|0,12474|0,1247<br>4|0,249%|0,624%|0,9206|0,920<br>3|0,460%|0,009%|
|**R42**|0,12942|0,1294<br>1|0,100%|0,259%|0,01732|0,0173<br>2|0,035%|0,087%|0,0276|0,027<br>4|0,014%|0,000%|
|**R43**|0,55759|0,5575<br>8|0,429%|1,115%|0,08430|0,0843<br>0|0,169%|0,421%|0,6482|0,642<br>7|0,324%|0,006%|
|**R44**|0,00528|0,0052<br>8|0,004%|0,011%|0,00092|0,0009<br>2|0,002%|0,005%|0,0035|0,003<br>5|0,002%|0,000%|
|**R45**|0,00640|0,0064<br>0|0,005%|0,013%|0,00123|0,0012<br>3|0,002%|0,006%|0,0074|0,007<br>4|0,004%|0,000%|
|**R46**|0,01457|0,0145<br>7|0,011%|0,029%|0,00339|0,0033<br>9|0,007%|0,017%|0,0349|0,035<br>1|0,017%|0,000%|
|**R47**|0,02098|0,0209<br>8|0,016%|0,042%|0,00508|0,0050<br>8|0,010%|0,025%|0,0584|0,058<br>6|0,029%|0,001%|
|**R48**|0,00391|0,0039<br>1|0,003%|0,008%|0,00075|0,0007<br>5|0,002%|0,004%|0,0021|0,002<br>1|0,001%|0,000%|
|**R49**|0,00367|0,0036<br>7|0,003%|0,007%|0,00067|0,0006<br>7|0,001%|0,003%|0,0014|0,001<br>4|0,001%|0,000%|

P á g i n a 68 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

Fuente: Elaboración propia.

**Tabla 15. Comparación gases de combustión con normas de calidad primaria y secundaria**

|Receptor|NOx|Col3|% DS N°114/2002 MINSEGPRES|Col5|SOx|Col7|Col8|% Norma primaria<br>DS N°104/2018 MMA|Col10|Col11|% Norma secundaria<br>DS N°22/2010 MINSEGPRES|Col13|Col14|CO|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor <br>|**1 hora**|**anual**|**1 hora**|A**nual**|**1 hora**|**24 horas**|**Anual**|**1 hora**|**24 horas**|**Anual**|**1 hora**|**24 horas**|**Anual**|**1 hora**|**8 horas**|**1 hora**|
|**R1 **|0,01925|0,01000|0,005%|0,010%|0,00927|0,00271|0,00054|0,0026%|0,0018%|0,0009%|0,0009%|0,0007%|0,0007%|0,01093|0,00383|0,00004%|
|**R2 **|0,01715|0,00588|0,004%|0,006%|0,00846|0,00151|0,00032|0,0024%|0,0010%|0,0005%|0,0008%|0,0004%|0,0004%|0,00934|0,00208|0,00003%|
|**R3 **|0,00849|0,00432|0,002%|0,004%|0,00406|0,00104|0,00016|0,0012%|0,0007%|0,0003%|0,0004%|0,0003%|0,0002%|0,00472|0,00146|0,00002%|
|**R4 **|0,00878|0,00393|0,002%|0,004%|0,00420|0,00094|0,00014|0,0012%|0,0006%|0,0002%|0,0004%|0,0003%|0,0002%|0,00479|0,00132|0,00002%|
|**R5 **|0,01023|0,00437|0,003%|0,004%|0,00490|0,00102|0,00015|0,0014%|0,0007%|0,0002%|0,0005%|0,0003%|0,0002%|0,00555|0,00143|0,00002%|
|**R6 **|0,01237|0,00470|0,003%|0,005%|0,00594|0,00108|0,00015|0,0017%|0,0007%|0,0003%|0,0006%|0,0003%|0,0002%|0,00662|0,00152|0,00002%|
|**R10 **|0,01611|0,00775|0,004%|0,008%|0,00773|0,00154|0,00016|0,0022%|0,0010%|0,0003%|0,0008%|0,0004%|0,0002%|0,00875|0,00220|0,00003%|
|**R7 **|0,01653|0,00447|0,004%|0,004%|0,00793|0,00096|0,00011|0,0023%|0,0006%|0,0002%|0,0008%|0,0003%|0,0001%|0,00856|0,00137|0,00003%|
|**R8 **|0,01628|0,00031|0,004%|0,000%|0,00784|0,00009|0,00002|0,0022%|0,0001%|0,0000%|0,0008%|0,0000%|0,0000%|0,00789|0,00012|0,00003%|
|**R9 **|0,01754|0,00014|0,004%|0,000%|0,00844|0,00004|0,00001|0,0024%|0,0000%|0,0000%|0,0008%|0,0000%|0,0000%|0,00846|0,00005|0,00003%|
|**R11 **|0,01857|0,00040|0,005%|0,000%|0,00892|0,00011|0,00002|0,0025%|0,0001%|0,0000%|0,0009%|0,0000%|0,0000%|0,00898|0,00015|0,00003%|
|**R12 **|0,02025|0,00257|0,005%|0,003%|0,00970|0,00069|0,00013|0,0028%|0,0005%|0,0002%|0,0010%|0,0002%|0,0002%|0,01010|0,00093|0,00003%|
|**R13 **|0,02351|0,00832|0,006%|0,008%|0,01128|0,00212|0,00037|0,0032%|0,0014%|0,0006%|0,0011%|0,0006%|0,0005%|0,01259|0,00298|0,00004%|
|**R14 **|0,02088|0,00283|0,005%|0,003%|0,01000|0,00077|0,00014|0,0029%|0,0005%|0,0002%|0,0010%|0,0002%|0,0002%|0,01047|0,00107|0,00003%|
|**R15 **|0,02353|0,00832|0,006%|0,008%|0,01125|0,00168|0,00023|0,0032%|0,0011%|0,0004%|0,0011%|0,0005%|0,0003%|0,01237|0,00248|0,00004%|
|**R16 **|0,10639|0,17430|0,027%|0,174%|0,05303|0,04065|0,00935|0,0152%|0,0271%|0,0156%|0,0053%|0,0111%|0,0117%|0,07696|0,05719|0,00026%|
|**R17 **|0,03759|0,03709|0,009%|0,037%|0,01780|0,00707|0,00065|0,0051%|0,0047%|0,0011%|0,0018%|0,0019%|0,0008%|0,02255|0,01012|0,00008%|
|**R18 **|0,02433|0,01112|0,006%|0,011%|0,01166|0,00262|0,00041|0,0033%|0,0017%|0,0007%|0,0012%|0,0007%|0,0005%|0,01331|0,00370|0,00004%|
|**R19 **|0,01987|0,00278|0,005%|0,003%|0,00947|0,00075|0,00014|0,0027%|0,0005%|0,0002%|0,0009%|0,0002%|0,0002%|0,00990|0,00101|0,00003%|
|**R20 **|0,01841|0,00035|0,005%|0,000%|0,00877|0,00009|0,00002|0,0025%|0,0001%|0,0000%|0,0009%|0,0000%|0,0000%|0,00882|0,00012|0,00003%|
|**R21 **|0,02690|0,01795|0,007%|0,018%|0,01257|0,00457|0,00100|0,0036%|0,0030%|0,0017%|0,0013%|0,0013%|0,0013%|0,01535|0,00655|0,00005%|
|**R22 **|0,02318|0,01105|0,006%|0,011%|0,01127|0,00283|0,00061|0,0032%|0,0019%|0,0010%|0,0011%|0,0008%|0,0008%|0,01293|0,00393|0,00004%|
|**R23 **|0,15126|0,26777|0,038%|0,268%|0,07366|0,06409|0,01505|0,0210%|0,0427%|0,0251%|0,0074%|0,0176%|0,0188%|0,10864|0,08503|0,00036%|
|**R24 **|0,17665|0,31905|0,044%|0,319%|0,08814|0,07548|0,01806|0,0252%|0,0503%|0,0301%|0,0088%|0,0207%|0,0226%|0,12965|0,10110|0,00043%|
|**R25 **|0,44522|0,85666|0,111%|0,857%|0,23187|0,19271|0,04862|0,0662%|0,1285%|0,0810%|0,0232%|0,0528%|0,0608%|0,33669|0,25831|0,00112%|

P á g i n a 69 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

|Receptor|NOx|Col3|% DS N°114/2002 MINSEGPRES|Col5|SOx|Col7|Col8|% Norma primaria<br>DS N°104/2018 MMA|Col10|Col11|% Norma secundaria<br>DS N°22/2010 MINSEGPRES|Col13|Col14|CO|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor <br>|**1 hora**|**anual**|**1 hora**|A**nual**|**1 hora**|**24 horas**|**Anual**|**1 hora**|**24 horas**|**Anual**|**1 hora**|**24 horas**|**Anual**|**1 hora**|**8 horas**|**1 hora**|
|**R26 **|0,54303|1,05266|0,136%|1,053%|0,28439|0,23314|0,05986|0,0813%|0,1554%|0,0998%|0,0284%|0,0639%|0,0748%|0,41146|0,31408|0,00137%|
|**R27 **|0,13908|0,24508|0,035%|0,245%|0,07073|0,05888|0,01389|0,0202%|0,0393%|0,0231%|0,0071%|0,0161%|0,0174%|0,10269|0,07777|0,00034%|
|**R28 **|0,07937|0,12616|0,020%|0,126%|0,03825|0,03030|0,00708|0,0109%|0,0202%|0,0118%|0,0038%|0,0083%|0,0088%|0,05586|0,04230|0,00019%|
|**R29 **|0,39016|0,74803|0,098%|0,748%|0,20070|0,17078|0,04210|0,0573%|0,1139%|0,0702%|0,0201%|0,0468%|0,0526%|0,29252|0,22580|0,00098%|
|**R30 **|0,37832|0,72471|0,095%|0,725%|0,19386|0,16271|0,04067|0,0554%|0,1085%|0,0678%|0,0194%|0,0446%|0,0508%|0,28429|0,22156|0,00095%|
|**R31 **|0,16275|0,29399|0,041%|0,294%|0,08037|0,06974|0,01663|0,0230%|0,0465%|0,0277%|0,0080%|0,0191%|0,0208%|0,11903|0,09395|0,00040%|
|**R32 **|0,49947|0,96741|0,125%|0,967%|0,25664|0,21497|0,05428|0,0733%|0,1433%|0,0905%|0,0257%|0,0589%|0,0679%|0,37388|0,28874|0,00125%|
|**R33 **|0,01662|0,00235|0,004%|0,002%|0,00795|0,00051|0,00005|0,0023%|0,0003%|0,0001%|0,0008%|0,0001%|0,0001%|0,00827|0,00068|0,00003%|
|**R35 **|0,01860|0,00665|0,005%|0,007%|0,00893|0,00151|0,00022|0,0026%|0,0010%|0,0004%|0,0009%|0,0004%|0,0003%|0,00988|0,00213|0,00003%|
|**R34 **|0,01678|0,00326|0,004%|0,003%|0,00812|0,00082|0,00017|0,0023%|0,0005%|0,0003%|0,0008%|0,0002%|0,0002%|0,00857|0,00109|0,00003%|
|**R36 **|0,01634|0,00270|0,004%|0,003%|0,00783|0,00073|0,00014|0,0022%|0,0005%|0,0002%|0,0008%|0,0002%|0,0002%|0,00824|0,00096|0,00003%|
|**R37 **|0,01513|0,00032|0,004%|0,000%|0,00727|0,00007|0,00001|0,0021%|0,0000%|0,0000%|0,0007%|0,0000%|0,0000%|0,00732|0,00010|0,00002%|
|**R38 **|0,01704|0,00458|0,004%|0,005%|0,00817|0,00123|0,00023|0,0023%|0,0008%|0,0004%|0,0008%|0,0003%|0,0003%|0,00887|0,00164|0,00003%|
|**R39 **|0,03057|0,03183|0,008%|0,032%|0,01479|0,00824|0,00178|0,0042%|0,0055%|0,0030%|0,0015%|0,0023%|0,0022%|0,01946|0,01112|0,00006%|
|**R40 **|0,18648|0,34378|0,047%|0,344%|0,09367|0,07578|0,01953|0,0268%|0,0505%|0,0326%|0,0094%|0,0208%|0,0244%|0,13796|0,10812|0,00046%|
|**R41 **|0,14205|0,25512|0,036%|0,255%|0,07285|0,05918|0,01448|0,0208%|0,0395%|0,0241%|0,0073%|0,0162%|0,0181%|0,10709|0,08296|0,00036%|
|**R42 **|0,02647|0,02418|0,007%|0,024%|0,01303|0,00606|0,00133|0,0037%|0,0040%|0,0022%|0,0013%|0,0017%|0,0017%|0,01664|0,00855|0,00006%|
|**R43 **|0,10659|0,18436|0,027%|0,184%|0,05124|0,04165|0,01047|0,0146%|0,0278%|0,0175%|0,0051%|0,0114%|0,0131%|0,07564|0,05922|0,00025%|
|**R44 **|0,01532|0,00208|0,004%|0,002%|0,00737|0,00044|0,00003|0,0021%|0,0003%|0,0001%|0,0007%|0,0001%|0,0000%|0,00765|0,00060|0,00003%|
|**R45 **|0,01590|0,00333|0,004%|0,003%|0,00765|0,00064|0,00003|0,0022%|0,0004%|0,0001%|0,0008%|0,0002%|0,0000%|0,00807|0,00088|0,00003%|
|**R46 **|0,02041|0,01239|0,005%|0,012%|0,00983|0,00205|0,00004|0,0028%|0,0014%|0,0001%|0,0010%|0,0006%|0,0000%|0,01129|0,00293|0,00004%|
|**R47 **|0,02399|0,01956|0,006%|0,020%|0,01153|0,00321|0,00004|0,0033%|0,0021%|0,0001%|0,0012%|0,0009%|0,0001%|0,01380|0,00454|0,00005%|
|**R48 **|0,01501|0,00174|0,004%|0,002%|0,00719|0,00039|0,00002|0,0021%|0,0003%|0,0000%|0,0007%|0,0001%|0,0000%|0,00743|0,00050|0,00002%|
|**R49 **|0,01484|0,00142|0,004%|0,001%|0,00713|0,00033|0,00002|0,0020%|0,0002%|0,0000%|0,0007%|0,0001%|0,0000%|0,00733|0,00043|0,00002%|

Fuente: Elaboración propia.

P á g i n a 70 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

Según los resultados de la modelación de dispersión atmosférica del material particulado
generado durante el primer año del proyecto, se ha determinado que las concentraciones
resultantes son de baja magnitud. En el receptor agrícola R30, las concentraciones
máximas de MP10 serán de 3,21 μg/m [3] en el período anual, lo cual representa
aproximadamente el 6,4% del límite establecido por la normativa D.S. N°12/22 MMA. En
relación al MP2.5, el Proyecto alcanza como máximo el 2,1% del límite diario establecido
por la norma D.S. N°12/11 MMA, en el receptor humano R30. Para el caso del MPS, el
Proyecto genera en R30 un total de 5,63 μg/m [3], lo cual equivale al 2,81% de la
Ordenanza de la Confederación Suiza.

En cuanto a los gases de combustión, el Proyecto genera como máximo en el receptor
R32, una concentración horaria de SOx de 0,28 μg/m [3], lo cual representa menos del 1%
de los límites establecidos en las normas de calidad primaria y secundaria para este
contaminante. En relación con el NOx, el Proyecto genera en R32 un total de 0,54 μg/m [3 ]

como concentración horaria de NOx, lo que equivale a menos del 1% límite de establecido
en la norma DS N°104/18 MMA. Para el caso del CO, en el receptor R32 se generan 0,41
μg/m [3] como concentración en 1 horas, lo cual en comparación con la norma DS
N°115/2002 MINSEGPRES, representa menos del 1% del límite mencionado en dicho
cuerpo normativo.

Adicionalmente se hará un análisis de las concentraciones de contaminantes

considerando el estado actual de la zona, la cual fue declarada como zona saturada por
Material Particulado MP10 como Concentración Anual, y Latente por MP10 como
Concentración Diaria mediante el D.S. N°107/2018 del Ministerio del Medio Ambiente.

P á g i n a 71 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

**Tabla 16. Aporte del Proyecto a condición base**

|Estación EMRP|Contaminante|Periodo|Estadígrafo|Valor|Aporte<br>proyecto|Condición<br>base +<br>proyecto|Unidad|Norma|% Norma<br>Condición<br>base +<br>aporte<br>proyecto|
|---|---|---|---|---|---|---|---|---|---|
|**Bomberos**|MP2,5|2020|P9824 horas|47|0,01415|47,014|ug/m3|50|94%|
|**Bomberos**|MP2,5|2019-2020|Promedio|22|0,01415|22,014|ug/m3|20|110%|
|**Bomberos**|MP10|2020|P9824 horas|75|0,00196|75,002|ug/m3|130|58%|
|**Bomberos**|MP10|2018-2020|Promedio anual|43|0,00196|43,002|ug/m3|50|86%|
|**Bomberos**|CO|2020|P99 máximo diarios 8 horas|3|0,00857|3,009|mg/m3|10|30%|
|**Bomberos**|CO|2020|P99 máximos diarios 1 hora|2|0,00109|2,001|mg/m3|30|7%|
|**Bomberos**|NO2|2020|P99 máximos diarios 1 hora|61|0,01678|61,017|ug/m3|400|15%|
|**Bomberos**|NO2|2018-2020|Promedio anual|17|0,00326|17,003|ug/m3|100|17%|
|**Bomberos**|SO2|2020|P98,5 1 hora|23|0,00812|23,008|ug/m3|350|7%|
|**Bomberos**|SO2|2020|P99 24 horas|18|0,00082|18,001|ug/m3|150|12%|
|**Bomberos**|SO2|2018-2020|Promedio anual|4|0,00017|4,000|ug/m3|60|7%|
|**La Cruz**|MP10|2020|P9824 horas|77|0,00605|77,006|ug/m3|130|59%|
|**La Cruz**|MP10|2018-2020|Promedio anual|39|0,00605|39,006|ug/m3|50|78%|
|**La Cruz**|CO|2020|P99 máximo diarios 8 horas|2|0,00068|2,001|mg/m3|10|20%|
|**La Cruz**|CO|2020|P99 máximos diarios 1 hora|1|0,00827|1,008|mg/m3|30|3%|
|**La Cruz**|NO2|2020|P99 máximos diarios 1 hora|82|0,01662|82,017|ug/m3|400|21%|
|**La Cruz**|NO2|2018-2020|Promedio anual|17|0,00235|17,002|ug/m3|100|17%|
|**La Cruz**|SO2|2020|P98,5 1 hora|22|0,00795|22,008|ug/m3|350|6%|
|**La Cruz**|SO2|2020|P99 24 horas|14|0,00051|14,001|ug/m3|150|9%|
|**La Cruz**|SO2|2018-2020|Promedio anual|5|0,00005|5,000|ug/m3|60|8%|
|**La Palma**|MP10|2020|P9824 horas|61|0,02429|61,024|ug/m3|130|47%|
|**La Palma**|MP10|2018-2020|Promedio anual|37|0,02429|37,024|ug/m3|50|74%|

P á g i n a 72 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

|Estación EMRP|Contaminante|Periodo|Estadígrafo|Valor|Aporte<br>proyecto|Condición<br>base +<br>proyecto|Unidad|Norma|% Norma<br>Condición<br>base +<br>aporte<br>proyecto|
|---|---|---|---|---|---|---|---|---|---|
||CO|2020|P99 máximo diarios 8 horas|2|0,00213|2,002|mg/m3|10|20%|
||CO|2020|P99 máximos diarios 1 hora|1|0,00988|1,010|mg/m3|30|3%|
||NO2|2020|P99 máximos diarios 1 hora|49|0,01860|49,019|ug/m3|400|12%|
||NO2|2018-2020|Promedio anual|10|0,00665|10,007|ug/m3|100|10%|
||SO2|2020|P98,5 1 hora|20|0,00893|20,009|ug/m3|350|6%|
||SO2|2020|P99 24 horas|12|0,00151|12,002|ug/m3|150|8%|
||SO2|2018-2020|Promedio anual|4|0,00022|4,000|ug/m3|60|7%|
|**Manzanar**|MP10|2020|P9824 horas|72|0,00101|72,001|ug/m3|130|55%|
|**Manzanar**|MP10|2018-2020|Promedio anual|36|0,00101|36,001|ug/m3|50|72%|
|**Manzanar**|CO|2020|P99 máximo diarios 8 horas|1|0,00010|1,000|mg/m3|10|10%|
|**Manzanar**|CO|2020|P99 máximos diarios 1 hora|1|0,00732|1,007|mg/m3|30|3%|
|**Manzanar**|NO2|2020|P99 máximos diarios 1 hora|68|0,01513|68,015|ug/m3|400|17%|
|**Manzanar**|NO2|2018-2020|Promedio anual|11|0,00032|11,000|ug/m3|100|11%|
|**Manzanar**|SO2|2020|P98,5 1 hora|25|0,00727|25,007|ug/m3|350|7%|
|**Manzanar**|SO2|2020|P99 24 horas|16|0,00007|16,000|ug/m3|150|11%|
|**Manzanar**|SO2|2018-2020|Promedio anual|5|0,00001|5,000|ug/m3|60|8%|
|**San Pedro**|MP2,5|2020|P9824 horas|36|0,01408|36,014|ug/m3|50|72%|
|**San Pedro**|MP2,5|2019-2020|Promedio|19|0,01408|19,014|ug/m3|20|95%|
|**San Pedro**|MP10|2020|P9824 horas|67|0,00194|67,002|ug/m3|130|52%|
|**San Pedro**|MP10|2018-2020|Promedio anual|38|0,00194|38,002|ug/m3|50|76%|
|**San Pedro**|CO|2020|P99 máximo diarios 8 horas|1|0,00096|1,001|mg/m3|10|10%|
|**San Pedro**|CO|2020|P99 máximos diarios 1 hora|1|0,00824|1,008|mg/m3|30|3%|
|**San Pedro**|NO2|2020|P99 máximos diarios 1 hora|83|0,01634|83,016|ug/m3|400|21%|

P á g i n a 73 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

|Estación EMRP|Contaminante|Periodo|Estadígrafo|Valor|Aporte<br>proyecto|Condición<br>base +<br>proyecto|Unidad|Norma|% Norma<br>Condición<br>base +<br>aporte<br>proyecto|
|---|---|---|---|---|---|---|---|---|---|
|||2018-2020|Promedio anual|14|0,00270|14,003|ug/m3|100|14%|
||SO2|2020|P98,5 1 hora|23|0,00783|23,008|ug/m3|350|7%|
||SO2|2020|P99 24 horas|13|0,00073|13,001|ug/m3|150|9%|
||SO2|2018-2020|Promedio anual|5|0,00014|5,000|ug/m3|60|8%|

Fuente: Elaboración propia en base a SINCA (2023).

P á g i n a 74 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

En conclusión, de acuerdo a lo expuesto, se puede afirmar que la ejecución del Proyecto
en cuanto a las concentraciones de material particulado y gases de combustión no
generará un impacto significativo en la salud de las personas, ya que no excede los
límites establecidos por las normas de calidad primaria del aire, que tienen como objetivo
proteger la salud de la población.

Con respecto a la estación Bomberos, en el periodo anual para MP2.5, se mantiene la
condición de saturación, sin embargo, es posible señalar que el Proyecto no modifica la
condición basal existente, toda vez que el aporte del Proyecto es considerado
despreciables, ya que el aporte del Proyecto equivale al 0,07% del límite establecido en la
normativa DS N°12/2012 MMA (20 ug/m [3] ).

De igual manera, para evaluar el riesgo incremental de estos contaminantes, a
continuación, se presentan los resultados de material particulado en la Estación
Bomberos, comparados con los valores de referencia del Título 40 del Código de
Regulaciones Federales de EE. UU. (CFR), sección 51.165 (EPA, 2011) más conocidos
como SILs (Nivel de Impacto Significativo, por sus siglas en inglés “Significant Impact
Level)”. De acuerdo con dicha sección del Código de Regulaciones Federales
estadounidense, se considerará que una fuente o una modificación importante causa o
contribuye a una infracción de una norma nacional de calidad del aire cuando dicha fuente
o modificación supere, como mínimo, tales niveles de significancia en cualquier localidad
que no cumpla o que no cumplirá con la norma nacional aplicable.

**Tabla 17. Nivel de significancia aporte Proyecto en Estación Bomberos**

|Contaminantes|Aporte Proyecto<br>(ug/m3)|SIL (ug/m3)|Porcentaje SIL|
|---|---|---|---|
|**MP10 anual**|0,00196|1|0,20%|
|**MP10 24 horas**|0,00196|5|0,04%|
|**MP2.5 anual**|0,01415|0,2|7,08%|

Fuente: Elaboración propia en base a EPA (2011).

Al analizar los valores y compararlos con los SILs, se observa que, en la Estación
Bomberos, la significancia del impacto (SIL) se encuentran por debajo del nivel de
referencia. Por lo tanto, el Proyecto no presenta un riesgo para la salud de la población,
de acuerdo con los lineamientos establecidos en la Guía Riesgo para la Salud de la
Población” (SEA, 2023).

Cabe destacar que la autoridad ambiental ha elaborado el Anteproyecto del Plan de
Prevención y Descontaminación Atmosférica para la Provincia de Quillota y las comunas
de Catemu, Panquehue y Llay Llay de la Provincia de San Felipe de Aconcagua. Por lo

P á g i n a 75 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

tanto, se realizará una comparación de las emisiones totales del Año 1 del Proyecto (año
de mayor emisión), con los valores que determinan la obligación de compensar

emisiones:

**Tabla 18. Comparación con límites Anteproyecto PPDA**

|Contaminante|Emisiones Año 1<br>Proyecto|Límite emisión<br>Anteproyecto|Cumplimiento|
|---|---|---|---|
|**MP10**|**2,0790**|5|Sí|
|**MP2.5**|**0,2824**|2,5|Sí|
|**NOx**|**0,6103**|20|Sí|
|**SOx**|**0,0277**|10|Sí|

Fuente: Elaboración propia en base a Res. Exenta N°82 del Ministerio del Medio Ambiente (MMA,

2018).

Se concluye que el Proyecto se encuentra en coherencia y compatibilidad del con el
Anteproyecto del Plan de Prevención y Descontaminación Atmosférica para la Provincia
de Quillota y las comunas de Catemu, Panquehue y Llay Llay de la Provincia de San
Felipe de Aconcagua, dado que las emisiones que generará el Proyecto no sobrepasan
los límites establecidos en esta normativa, de manera que el Proyectó no deberá
compensar sus emisiones atmosféricas.

**9.2. Evaluación de impactos sobre la calidad del aire, flora y vegetación,**

**fauna, aguas superficiales y suelo**

A continuación, se procede a realizar un análisis de los aportes del proyecto en su etapa
de construcción, para determinar si el proyecto generará efectos adversos significativos
sobre la calidad del aire, flora y vegetación, fauna, aguas superficiales y suelo, según los
lineamientos establecidos en la “Guía de evaluación de efectos adversos sobre recursos

naturales renovables” (SEA, 2022).

La siguiente Tabla presenta una lista de potenciales impactos que el Proyecto puede
generar o presentar sobre la calidad del aire.

|Col1|Tabla 19. Potenciales|impactos sobre componente calidad del aire|
|---|---|---|
|**Recurso**|**Impacto**|**Posibles impactos**|
|**Aire**|Impactos en la<br>calidad del aire|• <br>Posible aumento en la concentración de material<br>particulado en el área de influencia.<br>• <br>Posible aumento en la concentración de gases en el<br>área de influencia.|

P á g i n a 76 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

|Recurso|Impacto|Posibles impactos|
|---|---|---|
||Impacto en la calidad<br>del aire que ocasiona<br>impactos sobre otro<br>recurso natural<br>renovable|• <br>El impacto en la calidad del aire producto del aumento<br>de<br>concentraciones<br>de<br>contaminantes,<br>ocasionar<br>impactos sobre ciertas poblaciones de especies de flora<br>y fauna, así como también sobre la calidad del suelo y<br>cultivos.<br>• <br>El impacto en la calidad del aire producto del aumento<br>de concentraciones de material particulado sedimentable<br>puede producir depositación de contaminantes en la<br>vegetación.|
||Impacto en un recurso<br>natural renovable que<br>causa impacto en otros<br>componentes del<br>artículo 11 de la Ley<br>19.300<br>|• <br>Un impacto sobre la calidad del aire, debido a las<br>emisiones atmosféricas del proyecto, puede generar<br>riesgo para la salud de la población, señalado en la letra<br>a) del artículo 11 de la Ley N° 19.300.<br>• <br>Un impacto sobre la calidad del aire, debido a las<br>emisiones atmosféricas del proyecto, puede producir<br>depositación de contaminantes en la vegetación utilizada<br>como<br>sustento<br>económico<br>de<br>grupos<br>humanos,<br>ocasionando una alteración en los sistemas de vida y<br>costumbres de dicho grupo.<br>|

Fuente: Elaboración propia.

A continuación, se presenta la evaluación de los posibles impactos identificados en la

Tabla anterior.

P á g i n a 77 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

**Tabla 20. Evaluación de impactos**

|Recurso|Potencial<br>impacto|Evaluación cualitativa|Evaluación cuantitativa|
|---|---|---|---|
|**Aire**|Impactos en<br>la calidad del<br>aire|Las<br>emisiones<br>de<br>Material<br>Particulado (MP10, MP2.5 y MPS) y<br>gases de combustión que generará<br>el Proyecto no ocasionarán un<br>impacto<br>significativo<br>sobre<br>la<br>capacidad del aire, para mantener<br>las<br>funciones<br>de<br>procreación,<br>reproducción,<br>crecimiento,<br>transformación o restablecimiento<br>de recursos naturales, debido a que<br>las normas de calidad primarias y<br>secundarias<br>no<br>se<br>ven<br>sobrepasadas con las emisiones del<br>Proyecto en ninguna sus fases.<br> <br>Adicionalmente<br>es<br>importante<br>destacar que las mayores tasas de<br>emisión se generarán durante el año<br>1 del Proyecto, el cual considera la<br>fase de construcción y operación.<br>|Las emisiones que generará el<br>Proyecto representan menos del<br>7% de los límites establecidos<br>en<br>las<br>normas<br>de<br>calidad<br>primaria y secundaria del aire.|
|**Aire**|Impacto en la<br>calidad<br>del<br>aire<br>que<br>ocasiona<br>impactos<br>sobre<br>otro<br>recurso<br>natural<br>renovable|Se establece que las emisiones<br>partículas que generará el Proyecto<br>(MP10, MP2.5 y MPS) y gases de<br>combustión,<br>no<br>ocasionarán<br>un<br>impacto<br>significativo<br>sobre<br>la<br>vegetación,<br>cultivos<br>cercanos,<br>cursos de agua, flora, fauna u otros<br>recursos<br>naturales<br>de<br>la<br>zona<br>debido a que las normas de calidad<br>secundarias<br>utilizadas<br>como<br>referencia (Norma Confederación<br>Suiza<br>y <br>Decreto<br>1.074/2018<br>Argentina), no se ven sobrepasadas<br>con las emisiones del Proyecto,<br>considerando que las normas de<br>calidad<br>secundaria<br>apuntan<br>a <br>proteger los recursos naturales. Por<br>lo tanto, se puede concluir que, a<br>nivel de calidad del aire, el Proyecto<br>no genera un impacto significativo<br>en la calidad de los recursos<br>naturales del área de influencia.<br> <br>Adicionalmente<br>es<br>importante<br>destacar que las mayores tasas de<br>emisión se generarán durante el año<br>1 del Proyecto, el cual considera la<br>fase de construcción y operación.|<br>En<br>los<br>receptores<br>correspondientes a cultivos las<br>emisiones<br>de<br>MPS<br>que<br>generará<br>el<br>Proyecto<br>representan menos del 2,81%<br>de los límites establecidos en<br>las<br>normas<br>de<br>calidad<br>secundaria del aire. Por lo tanto,<br>no se ocasiona un impacto<br>significativo en los cultivos y<br>vegetación cercana al Proyecto.|

P á g i n a 78 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

|Recurso|Potencial<br>impacto|Evaluación cualitativa|Evaluación cuantitativa|
|---|---|---|---|
||Impacto<br>en<br>un<br>recurso<br>natural<br>renovable<br>que<br>causa<br>impacto<br>en<br>otros<br>componentes<br>del<br>artículo<br>11 de la Ley<br>19.300|Se establece que las emisiones<br>partículas que generará el Proyecto<br>(MP10, MP2.5 y MPS) y gases de<br>combustión,<br>no<br>ocasionarán<br>un<br>impacto<br>significativo<br>sobre<br>la<br>vegetación,<br>cultivos<br>cercanos,<br>cursos de agua, flora, fauna u otros<br>recursos<br>naturales<br>de<br>la<br>zona<br>debido a que las normas de calidad<br>secundarias<br>utilizadas<br>como<br>referencia (Norma Confederación<br>Suiza<br>y <br>Decreto<br>1.074/2018<br>Argentina), no se ven sobrepasadas<br>con las emisiones del Proyecto,<br>considerando que las normas de<br>calidad<br>secundaria<br>apuntan<br>a <br>proteger los recursos naturales. Por<br>lo tanto, se puede concluir que, a<br>nivel de calidad del aire, el Proyecto<br>no genera un impacto significativo<br>en la calidad de los recursos<br>naturales del área de influencia.<br> <br>Adicionalmente<br>es<br>importante<br>destacar que las mayores tasas de<br>emisión se generarán durante el año<br>1 del Proyecto, el cual considera la<br>fase de construcción y operación.<br>|<br>En<br>los<br>receptores<br>correspondientes a cultivos, las<br>emisiones<br>de<br>MPS<br>que<br>generará<br>el<br>Proyecto<br>representan menos del 2,81%<br>de los límites establecidos en<br>las<br>normas<br>de<br>calidad<br>secundaria del aire. Por lo tanto,<br>no se ocasiona un impacto<br>significativo en los cultivos y<br>vegetación cercana al Proyecto.|

Fuente: Elaboración propia.

En términos de calidad y cantidad, se establece que el Proyecto no genera efectos
adversos significativos en los recursos naturales mencionados: aire, flora y vegetación,
fauna, aguas superficiales y suelo, considerando que las condiciones que permiten la
presencia y desarrollo de especies y la funcionalidad de los ecosistemas dependientes de
la calidad del aire en la zona no se ven afectadas por la presencia del Proyecto.

Además, no se produce una modificación sustancial en la composición, estructura o
funcionamiento del ecosistema que impida la manifestación de los procesos e
interrelaciones característicos. Esto se debe a que el Proyecto no supera los límites
establecidos en las normas de calidad del aire (tanto primarias como secundarias) y las
tasas de emisión del Proyecto se mantienen por debajo del 10% de dichos límites, según
las regulaciones aplicables.

En consecuencia, se puede afirmar que el ecosistema original se mantiene sin cambios
significativos debido a las emisiones atmosféricas generadas por el Proyecto. Por lo tanto,

P á g i n a 79 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

la ejecución del Proyecto no afecta la permanencia ni la capacidad de generación de los
recursos naturales mencionados: aire, flora y vegetación, fauna, aguas superficiales y
suelo. Esto implica que la disponibilidad, utilización y aprovechamiento racional futuro de
dichos recursos no se ven comprometidos. Asimismo, la capacidad de regeneración y
renovación de estos recursos no se ve alterada por la ejecución del Proyecto.

En resumen, se concluye que las emisiones atmosféricas generadas por el Proyecto no
tienen un impacto significativo en los recursos naturales mencionados y no comprometen
su disponibilidad, utilización, aprovechamiento racional ni su capacidad de regeneración o
renovación.

**10. ÁREA DE INFLUENCIA**

El área de influencia corresponde al espacio geográfico cuyos atributos, elementos
naturales o socioculturales deben ser considerados con la finalidad de definir si el

proyecto o actividad genera o presenta alguno de los efectos, características o
circunstancias del Artículo 11 de la Ley N° 19.300, o bien para justificar su inexistencia
(Ref. letra a) del Artículo 2 del Reglamento del SEIA).

Dada esta definición, se efectuó una delimitación del área de influencia considerando los
siguientes factores y criterios definidos en la “Guía Área de Influencia en el Sistema de
Evaluación de Impacto Ambiental” (SEA, 2017) y “Guía Calidad del aire en el área de
influencia de proyectos que ingresan al SEIA (SEA, 2015):

 El área de influencia debe comprender el espacio desde donde se generan las
emisiones (fuente de la emisión) más el comprendido por la dispersión de
contaminantes emitidos. Por su parte, para predecir y evaluar el riesgo para la
salud de la población, el AI del elemento ‘salud de la población’ debe comprender
el espacio con presencia de población expuesta a los contaminantes emitidos por
el Proyecto.

 Las partículas sedimentables de los contaminantes de dichas emisiones pueden
depositarse en el suelo y vegetación, por lo tanto, el área de influencia de estos
elementos comprende el área o espacio geográfico donde dicho material se
sedimenta.

 Aporte de contaminantes debido a la construcción y operación del Proyecto, cuyos
antecedentes fueron obtenidos a través de la modelación de MP10, MP2.5, MPS,
NOx, SOx y CO.

 Distancia de receptores de interés cercanos al Proyecto.

Con todo lo anterior, se definió un Área de influencia para la componente calidad del aire
asociado a los contaminantes atmosféricos extendiéndose en un radio de 2000 m

alrededor del Proyecto, considerando que las máximas concentraciones de contaminantes
se perciben a 50 m de este. Además, a la distancia de 2000 m desde las obras

P á g i n a 80 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

ejecutadas, las concentraciones de los contaminantes generados están por debajo del 1%
de los límites máximos establecidos en las normativas de calidad primaria del aire.

A continuación, se presenta una figura que detallada el Área de Influencia del Proyecto
con respecto al componente calidad del aire, la cual se incluye en formato kmz en el
Apéndice D.

P á g i n a 81 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

**Figura 44. Área de influencia calidad del aire**

Fuente: Elaboración propia.

P á g i n a 82 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

**11. CONCLUSIONES**

Los resultados de la modelación de las concentraciones de contaminantes atmosféricos a

distintas distancias desde el Proyecto muestran que los mayores aportes se producen a
una distancia de 298 metros del Proyecto, durante el primer año de funcionamiento del
Proyecto, el cual contempla fase de construcción y 7 meses de la fase de operación.

Respecto al análisis de incertidumbre del modelo WRF, se establece que las diferencias
entre valores modelados y observados de velocidad del viento están dentro de un rango
aceptable, considerando que los estadísticos BIAS, MAE y RMSE presentan valores por
debajo de los 2 m/s. Adicionalmente. se observa un coeficiente de correlación de 0,749
entre valores modelados y observados, lo que permite concluir que el modelo WRF se
ajusta satisfactoriamente a los valores observados.

De esta forma, se delimitó un área de influencia de la calidad del aire, con la
concentración correspondiente a un 1% del valor de las normas de calidad del aire para
los contaminantes atmosféricos MP10, MP2.5, MPS, NOx, SOx y CO, considerando un
escenario conservador y desfavorable en cuanto a la velocidad del viento y estabilidad de
la atmósfera. Por lo tanto, el área de influencia quedó definida hasta una distancia de
2000 metros desde el perímetro del Proyecto.

El receptor humano de máximo impacto corresponde al receptor R30, donde se
ocasionarán aportes poco significativos de concentraciones de contaminantes
atmosféricos. Lo anterior es debido a que los porcentajes de comparación de las
emisiones del Proyecto respecto a la normativa de calidad primaria del aire no superan el
2,8% para concentraciones diarias, y el 6,4% para concentraciones anuales, tanto para
material particulado (MP2.5, MP10 y MPS) como para gases de combustión (NOx, SOx y
CO).

Con respecto a la estación EMRP Bomberos, en el periodo anual para MP2.5, se
mantiene la condición de saturación, sin embargo, es posible señalar que el Proyecto no
modifica la condición basal existente, toda vez que el aporte del Proyecto es considerado
despreciables, ya que el aporte del Proyecto equivale al 0,07% del límite establecido en la
normativa DS N°12/2012 MMA (20 ug/m [3] ). Además, a analizar la significancia del aporte
del Proyecto a la condición de saturación, el aporte del Proyecto resulta bajo los valores
de referencia del Título 40 del Código de Regulaciones Federales de EE. UU. (CFR),
sección 51.165 (EPA, 2011).

Respecto a la depositación de MPS, se establece que las emisiones del Proyecto
representan menos del 2,81% de las normativas secundarias de referencia de calidad del
aire para MPS, de manera que el Proyecto no generará un impacto significativo debido a
la depositación de material particulado y no afectará la vegetación ni cultivos cercanos, ni
flora o fauna presente en el área de influencia.

P á g i n a 83 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

Adicionalmente, se concluye que el Proyecto se encuentra en coherencia y compatibilidad
con el Anteproyecto del Plan de Prevención y Descontaminación Atmosférica para la
Provincia de Quillota y las comunas de Catemu, Panquehue y Llay Llay de la Provincia de
San Felipe de Aconcagua, dado que las emisiones que generará el Proyecto no
sobrepasan los límites establecidos en esta normativa, de manera que el Proyectó no
deberá compensar sus emisiones atmosféricas.

Por lo tanto, es posible inferir que las emisiones asociadas a las fases de construcción y
operación del Proyecto no afectarán a la calidad del aire en los receptores cercanos, de
manera que se descarta la ejecución de un modelo más refinado para calidad del aire,
dado que las emisiones atmosféricas del Proyecto No sobrepasan los límites de
concentración establecidos en las normas de calidad del aire primarias y secundarias,
además es importante destacar que la modelación se realizó considerando un escenario
muy conservador respecto a la meteorología (condiciones desfavorables de velocidad del
viento y estabilidad de la atmosfera) y a la simultaneidad de la construcción de las obras
(en la práctica la construcción del Proyecto no es simultánea, puesto que las actividades
constructivas son realizadas de forma secuencial).

Expuesto lo detallado, se determina que el Proyecto Energía Esmeralda no genera un
efecto adverso significativo, ni un impacto adverso para la salud de las personas ni en
calidad del aire en el área del Proyecto y tampoco en las poblaciones cercanas, ni en los
cultivos aledaños, ni en los recursos naturales de la zona, ya que no sobrepasa los límites
establecidos en las normativas de calidad primaria tanto sus criterios horarios, diarios y
anuales, teniendo en cuenta que los límites establecidos en las normas de calidad
primaria apuntan a proteger la salud de la población, es por esto que estas normas
establecen límites más estrictos que las normas de calidad secundaria, de igual manera
las emisiones del Proyecto cumplen con las normas de calidad secundaria, las cuales
apuntan a proteger el medio ambiente. Es importante considerar, además, que las
emisiones atmosféricas generadas tanto generadas en el Año 1 tendrán una duración
acotada.

En base a lo anterior es posible afirmar que el Proyecto genera un aumento marginal y
despreciable en las concentraciones de contaminantes atmosféricos producto a las
emisiones acotadas a la fase de construcción y operación, por lo tanto, no se generará
una modificación en la calidad del aire de la zona, de manera que el Proyecto no genera
riesgos adicionales a la salud de población.

P á g i n a 84 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

**12. BIBLIOGRAFÍA**

 Cordillot, F. & Klaus, G. (2011). _Gefährdete Arten in der Schweiz. Synthese Rote_
_Listen, Stand 2010. Bundesamt für Umwelt, Bern._

 - Decreto N°12/2010, Establece Norma de calidad del aire para MP2.5, Ministerio
del Medio Ambiente. Diario Oficial de la República de Chile, 9 de mayo de 2011,
Santiago, Chile.

 Decreto N°22/2010, Establece norma de calidad secundaria de aire para anhídrido
sulfuroso (SO2), Ministerio Secretaría General de la Presidencia. Diario Oficial de
la República de Chile, 16 de abril de 2010, Santiago, Chile.

 Decreto N°114/2002, Establece Norma de calidad del aire para NO2, Ministerio
Secretaría General de la Presidencia. Diario Oficial de la República de Chile, 6 de
marzo de 2003, Santiago, Chile.

 Decreto N°115/2002, Establece Norma de calidad del aire para CO, Ministerio
Secretaría General de la Presidencia. Diario Oficial de la República de Chile, 10 de
septiembre de 2002, Santiago, Chile.

 Decreto N°104/2018, Establece Norma de calidad del aire para SO2, Ministerio del
Medio Ambiente. Diario Oficial de la República de Chile, 16 de mayo de 2019,
Santiago, Chile.

 - Decreto N°12/2022, Establece Norma de calidad ambiental para material
particulado respirable MP10, Ministerio del Medio Ambiente. Diario Oficial de la
República de Chile, 4 de junio de 2022, Santiago, Chile.

 Decreto N°1074/2018. Aprueba la reglamentación de la Ley 5965 de protección a
las fuentes de provisión y a los cursos y cuerpos receptores de agua y a la
atmósfera. Deroga el DEC.3395/96. Designa autoridad de aplicación al Organismo
Provincial para el Desarrollo Sostenible (OPD). Gobierno de la Provincia de
Buenos Aires. Boletín Oficial de la República Argentina, 5 de octubre de 2018,
Buenos Aires, Argentina.

 - Department for Environment, Food and Rural Affairs [DEFRA]. (2014). _What are_
_the causes of air Pollution. United Kingdom Government._

 Díaz, V. y Páez C. (2006). _Contaminación por material particulado en Quito y_
_caracterización química de las muestras._ Corporación para el Mejoramiento del
Aire de Quito. Revista Acta Nova Vol.3, Nro 2.

 - EPA. (2023). _Air Quality Dispersion Modeling - Alternative Models._

 - EPA. (2017). _Guideline on Air Quality Models_

 - Figueruelo, J. y Marino, M. (2004). _Química Física del Ambiente y de los Procesos_
_Medioambientales_

 - Google Earth Pro (2023). _Perfiles de elevación._

 - Grossi, M., Gutierréz, D. & Deluchi, G. (2013). _Una mirada sobre el estado actual_
_de la conservación de la flora argentina._

 - Koppen, W. (1918). _Clasificación de climas según temperatura, precipitación y_
_ciclo estacional._

 - Lakes Environmental. (2006). _CALPUF View Leading interface for puff dispersion._

P á g i n a 85 | 86

Anexo 4.2 Modelación de la calidad del aire

Declaración de Impacto Ambiental Proyecto Energía Esmeralda

- MMA. (2017). _Manual para el Desarrollo de Inventarios de Emisiones_
_Atmosféricas._

- MMA. (2018) _. Res. Exenta N°82 del Ministerio del Medio Ambiente._ _Anteproyecto_
_del Plan de Prevención y Descontaminación Atmosférica para la Provincia de_
_Quillota y las comunas de Catemu, Panquehue y Llay Llay de la Provincia de San_
_Felipe de Aconcagua._

- Organización Mundial de la Salud [OMS]. (2006). _Guías de calidad del aire de la_
_OMS relativas al material particulado, el ozono, el dióxido de nitrógeno y el dióxido_
_de azufre._

Rodriguez, R., Marticorena, C., Alarcón, D., Baeza, D., Cavieres, L., Finot, L.,
Fuentes, N., Kiessling, A., Mihoc, M., Pauchard, A., Ruiz, E., Sanchez, P. &
Marticorena, A. (2018). _Catálogo de las plantas vasculares de Chile._

- SEA. (2022). _Guía de evaluación de efectos adversos sobre recursos naturales_
_renovables._

SEA, (2022). _Criterio de Evaluación en el SEIA: Objetos de protección._

SEA. (2023). _Guía para el uso de modelos de calidad del aire en el SEIA._

SINCA. (2023). Sistema de Información Nacional de Calidad del Aire, información
histórica.

Vargas, C. (2011). _Efectos de la fracción gruesa (PM10-2.5) del material_
_particulado sobre la salud humana._ Ministerio de Salud del Gobierno de Chile.

P á g i n a 86 | 86

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Construcción detalle del dominio de los datos meteorológicos****

| Periodo de datos de los datos | 1 enero a 31 de diciembre de 2022 |
| --- | --- |
| **Punto de Referencia** | Latitud: - 32.914 S<br>Longitud: - 71.268 W |
| **Área de Dominio** | 50x50 km |
| **Proyección** | Lambert Conic Conformal |
| **Datum** | NWS-84 6370 km Radius, Global Sphere |
| **Resolución** | 1 km |
| **Numero de Celdas en dirección x** | 50 |
| **Numero de Celdas en dirección y** | 50 |
| **Numero de Capas Verticales** | 11 (entre 0 y 4000 metros de altura) |
| **Tipo de dato** | CALPUFF-Ready WRF Data (WRF.MET<br>Format) |

**Tabla 2.: Resumen tasa de emisiones atmosféricas para el año 1****

| Contami<br>nante | Resultados estimación de emisiones | Col3 | Col4 | Datos entrada CALPUFF | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Contami**<br>**nante** | **Tasa**<br>**emisión**<br>**Área**<br>**Proyecto** | **Caminos No**<br>**pavimentad**<br>**os** | **Caminos**<br>**pavimentado**<br>**s ** | **Tasa emisión**<br>**Área Proyecto** | **Caminos**<br>**pavimentad**<br>**os** | **Caminos No**<br>**pavimentad**<br>**os** |
| **Unidad** | **t/año** | **t/año** | **t/año** | **g/s/m2 ** | **g/s/m** | **g/s/m** |
| **MP10** | 0,57565 | 0,11332 | 1,39000 | 5,893, E-08 | 6,654, E-08 | 1,102, E-05 |
| **MP2.5** | 0,11939 | 0,02935 | 0,13370 | 1,222, E-08 | 1,724, E-08 | 1,060, E-06 |
| **MPS** | 1,73983 | 0,57958 | 4,36330 | 1,781, E-07 | 3,403, E-07 | 3,459, E-05 |
| **No** | 0,48155 | 0,12231 | 0,00644 | 4,930, E-08 | 7,182, E-08 | 5,103, E-08 |
| **SOx** | 0,02757 | 0,00012 | 0,00001 | 2,822, E-09 | 7,060, E-11 | 5,016, E-11 |
| **CO** | 0,13740 | 0,02762 | 0,00145 | 1,407, E-08 | 1,622, E-08 | 1,152, E-08 |
| **Tipo de**<br>**fuente** | Areal | Lineal | Lineal | Areal | Lineal | Lineal |

**Tabla 3.: Receptores modelación****

| Tipo Receptor | Id | Coordenadas | Col4 | Distanc<br>ia al<br>Proyect<br>o [m] | Descripción |
| --- | --- | --- | --- | --- | --- |
| **Tipo Receptor** | **Id** | **WGS84 Huso 19S** | **WGS84 Huso 19S** | **WGS84 Huso 19S** | **WGS84 Huso 19S** |
| **Tipo Receptor** | **Id** | **Este [m]** | **Sur [m]** | **Sur [m]** | **Sur [m]** |
| **Sitio Prioritario** | R1 | 286097,04 | 6356959,13 | 1295 | Humedal Río<br>Aconcagua/Rio A |
| **Atractivo Turístico** | R2 | 291530,00 | 6355927,00 | 2898 | Hacienda Patrimonial<br>San Isidro |
| **Monumento**<br>**Histórico** | R3 | 289654,00 | 6359611,00 | 3883 | Casa Colonial |
| **Atractivo Turístico** | R4 | 289702,00 | 6359822,00 | 4095 | Cruz de Mayo Quillota |
| **Atractivo Turístico** | R5 | 289773,00 | 6359762,00 | 4070 | Plaza de Armas Quillota |
| **Atractivo Turístico** | R6 | 289821,00 | 6359732,00 | 4063 | Templo de Santo<br>Domingo |
| **Reserva de la**<br>**Biósfera** | R10 | 301345,72 | 6351464,10 | 13428 | La Campana-Peñuelas |
| **Atractivo Turístico** | R7 | 290072,00 | 6359778,00 | 4212 | Turístico Museo Casa<br>del Huasco |
| **Atractivo Turístico** | R8 | 289944,00 | 6360284,00 | 4615 | Turístico Museo<br>Histórico Arqueológico |
| **Industrial** | R9 | 284144,14 | 6363242,49 | 7529 | Viña El Sauce |
| **Industrial** | R11 | 280836,00 | 6350953,00 | 8227 | Viña Narbona Wines |
| **Establecimiento de**<br>**salud** | R12 | 287054,04 | 6353236,13 | 2671 | SAPU y CESFAM San<br>Pedro |
| **Establecimiento de**<br>**salud** | R13 | 288424,95 | 6358420,32 | 2274 | CESFAM Cardenal Raúl<br>Silva Henríquez |
| **Establecimiento de**<br>**salud** | R14 | 288783,04 | 6359763,99 | 3644 | Hospital San Martín<br>Quillota |
| **Establecimiento de**<br>**salud** | R15 | 290578,61 | 6359334,07 | 4037 | Centro Comunitario de<br>Salud Familiar<br>(CECOSF) |
| **Establecimiento**<br>**educacional** | R16 | 287604,99 | 6356829,60 | 485 | Liceo Agrícola de<br>Quillota |
| **Establecimiento**<br>**educacional** | R17 | 288585,68 | 6357973,88 | 1943 | Escuela Especial Los<br>Robles |
| **Establecimiento**<br>**educacional** | R18 | 288750,87 | 6358367,73 | 2369 | Colegio República de<br>México |
| **Establecimiento**<br>**educacional** | R19 | 287561,70 | 6353308,34 | 2377 | Escuela Básica Abel<br>Guerrero Aguirre |
| **Sitio Prioritario** | R20 | 283661,32 | 6348674,83 | 8301 | Sitio Prioritario Estero<br>Limache |
| **Cuerpos de agua** | R21 | 288694,12 | 6354518,85 | 1007 | Estero San Isidro |
| **Cuerpos de agua** | R22 | 290578,95 | 6355880,43 | 1946 | Quebrada Sin Nombre |
| **Humano** | R23 | 287279,00 | 6355968,00 | 163 | Viviendas |

**Tabla 6.: Resultados modelación año 1 material particulado****

| Receptor | MP10 (μg/m3) | Col3 | MP2,5 (μg/m3) | Col5 | MPS (mg/m2/día) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **24 h** | **Anual** | **24 h** | **Anual** | **30 días** | **Anual** |
| **R1 ** | 0,0653 | 0,0653 | 0,0087 | 0,0087 | 0,0222 | 0,0221 |
| **R2 ** | 0,0292 | 0,0292 | 0,0040 | 0,0040 | 0,0002 | 0,0002 |
| **R3 ** | 0,0180 | 0,0180 | 0,0027 | 0,0027 | 0,0024 | 0,0024 |
| **R4 ** | 0,0161 | 0,0161 | 0,0024 | 0,0024 | 0,0024 | 0,0025 |
| **R5 ** | 0,0169 | 0,0169 | 0,0026 | 0,0026 | 0,0032 | 0,0033 |
| **R6 ** | 0,0174 | 0,0174 | 0,0027 | 0,0027 | 0,0040 | 0,0040 |
| **R10 ** | 0,0200 | 0,0200 | 0,0034 | 0,0034 | 0,0132 | 0,0132 |
| **R7 ** | 0,0141 | 0,0141 | 0,0023 | 0,0023 | 0,0058 | 0,0058 |
| **R8 ** | 0,0019 | 0,0019 | 0,0003 | 0,0003 | 0,0000 | 0,0000 |
| **R9 ** | 0,0008 | 0,0008 | 0,0001 | 0,0001 | 0,0000 | 0,0000 |
| **R11 ** | 0,0019 | 0,0019 | 0,0003 | 0,0003 | 0,0000 | 0,0000 |
| **R12 ** | 0,0135 | 0,0135 | 0,0019 | 0,0019 | 0,0003 | 0,0003 |
| **R13 ** | 0,0433 | 0,0433 | 0,0061 | 0,0061 | 0,0064 | 0,0064 |
| **R14 ** | 0,0154 | 0,0154 | 0,0022 | 0,0022 | 0,0003 | 0,0003 |
| **R15 ** | 0,0250 | 0,0250 | 0,0040 | 0,0040 | 0,0096 | 0,0095 |
| **R16 ** | 0,6200 | 0,6200 | 0,0907 | 0,0907 | 0,6673 | 0,6642 |
| **R17 ** | 0,0931 | 0,0931 | 0,0155 | 0,0155 | 0,0889 | 0,0886 |
| **R18 ** | 0,0484 | 0,0484 | 0,0070 | 0,0070 | 0,0108 | 0,0108 |
| **R19 ** | 0,0149 | 0,0149 | 0,0020 | 0,0020 | 0,0003 | 0,0003 |

**Tabla 7.: Resultados modelación año 1 gases de combustión****

| Receptor | NOx (μg/m3) | Col3 | SOx (μg/m3) | Col5 | Col6 | CO (μg/m3) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **1 h** | **Anual** | **1 hora** | **24 h** | **Anual** | **1 hora** | **8 horas** |
| **R1 ** | 0,01925 | 0,01000 | 0,00927 | 0,00271 | 5,36,E-04 | 0,01093 | 0,00383 |
| **R2 ** | 0,01715 | 0,00588 | 0,00846 | 0,00151 | 3,22,E-04 | 0,00934 | 0,00208 |
| **R3 ** | 0,00849 | 0,00432 | 0,00406 | 0,00104 | 1,62,E-04 | 0,00472 | 0,00146 |
| **R4 ** | 0,00878 | 0,00393 | 0,00420 | 0,00094 | 1,43,E-04 | 0,00479 | 0,00132 |
| **R5 ** | 0,01023 | 0,00437 | 0,00490 | 0,00102 | 1,49,E-04 | 0,00555 | 0,00143 |
| **R6 ** | 0,01237 | 0,00470 | 0,00594 | 0,00108 | 1,53,E-04 | 0,00662 | 0,00152 |
| **R10 ** | 0,01611 | 0,00775 | 0,00773 | 0,00154 | 1,55,E-04 | 0,00875 | 0,00220 |
| **R7 ** | 0,01653 | 0,00447 | 0,00793 | 0,00096 | 1,14,E-04 | 0,00856 | 0,00137 |
| **R8 ** | 0,01628 | 0,00031 | 0,00784 | 0,00009 | 1,55,E-05 | 0,00789 | 0,00012 |
| **R9 ** | 0,01754 | 0,00014 | 0,00844 | 0,00004 | 7,45,E-06 | 0,00846 | 0,00005 |
| **R11 ** | 0,01857 | 0,00040 | 0,00892 | 0,00011 | 1,62,E-05 | 0,00898 | 0,00015 |
| **R12 ** | 0,02025 | 0,00257 | 0,00970 | 0,00069 | 1,28,E-04 | 0,01010 | 0,00093 |
| **R13 ** | 0,02351 | 0,00832 | 0,01128 | 0,00212 | 3,65,E-04 | 0,01259 | 0,00298 |

**Tabla 8.: Estaciones caracterización meteorológica****

| Estación SINCA | Coordenadas UTM | Col3 | Variables<br>Meteorológicas<br>Registradas |
| --- | --- | --- | --- |
| **Estación SINCA** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| **Estación San**<br>**Pedro** | 287422,00 | 6353393,00 | Dirección del viento<br>Velocidad del viento |
| **Estación**<br>**Bomberos** | 289818,00 | 6359202,00 | Dirección del viento<br>Velocidad del viento |

**Tabla 9.: Estación Bomberos****

| Variable | Año | N° Registros<br>válidos | % Registros<br>válidos |
| --- | --- | --- | --- |
| **Dirección del**<br>**viento** | 2022 | 8010 | 91,4% |
| **Velocidad del**<br>**viento** | 2022 | 8010 | 91,4% |

**Tabla 11.: Cuerpo normativo****

| Parámetro | Norma | Estadístico | Valor<br>límite | Referencia |
| --- | --- | --- | --- | --- |
| **MP10** | Primaria | Promedio anual | 50 μg/m3 | DS N°12/2022 MMA |
| **MP10** | Primaria | Promedio 24 horas<br>(Percentil 98) | 130 μg/m3 | 130 μg/m3 |
| **MP2.5** | Primaria | Promedio anual | 20 μg/m3 | DS N°12/2012 MMA |
| **MP2.5** | Primaria | Promedio 24 horas<br>(Percentil 98) | 50 μg/m3 | 50 μg/m3 |
| **NO2 ** | Primaria | Promedio Anual | 100 μg/m3 | DS N°114/2002<br>MINSEGPRES |
| **NO2 ** | Primaria | Promedio 1 hora<br>(Percentil 99) | 400 μg/m3 | 400 μg/m3 |
| **CO** | Primaria | Promedio horario<br>(Percentil 99) | 30000<br>μg/m3 | DS N°115/2002<br>MINSEGPRES |
| **CO** | Primaria | Promedio 8 horas<br>(Percentil 99) | 10000<br>μg/m3 | 10000<br>μg/m3 |
| **SO2** | Primaria | Promedio Anual | 60 μg/m3 | DS N°104/2018 MMA |
| **SO2** | Primaria | Promedio 24 horas<br>(Percentil 99) | 150 μg/m3 | 150 μg/m3 |
| **SO2** | Primaria | Promedio 1 hora<br>(Percentil 98,5) | 350 μg/m3 | 350 μg/m3 |
| **SO2** | Secundaria<br>Zona norte | Promedio Anual | 80 μg/m3 | DS N°22/2010<br>MINSEGPRES |
| **SO2** | Secundaria<br>Zona norte | Promedio 24 horas<br>(Percentil 99,7) | 365 μg/m3 | 365 μg/m3 |
| **SO2** | Secundaria<br>Zona norte | Promedio 1 hora<br>(Percentil 99,73) | 1000 μg/m3 | 1000 μg/m3 |

**Tabla 12.: Cuerpo normativo****

| Contaminante | País | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- | --- |
| **MPS** <br>**(Partículas**<br>**sedimentables)** | Confederación<br>Suiza | - | Promedio<br>anual | 200<br>(mg/m2día) | Ordenanza de la<br>Confederación<br>Suiza, Sobre<br>Control de<br>Contaminación<br>del Aire 1993 |

**Tabla 13.: Resumen caracterización calidad del aire****

| Estación<br>EMRP | Contaminan<br>te | Periodo | Estadígrafo | Valo<br>r | Unida<br>d | Norm<br>a | %<br>Norm<br>a |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Bombero**<br>**s ** | MP2,5 | 2020 | P9824 horas | 47 | ug/m3 | 50 | 94% |
| **Bombero**<br>**s ** | MP2,5 | 2019-2020 | Promedio | 22 | ug/m3 | 20 | 111% |
| **Bombero**<br>**s ** | MP10 | 2020 | P9824 horas | 75 | ug/m3 | 130 | 58% |
| **Bombero**<br>**s ** | MP10 | 2018-2020 | Promedio anual | 43 | ug/m3 | 50 | 87% |
| **Bombero**<br>**s ** | CO | 2020 | P99 máximo diarios 8<br>horas | 3 | mg/m3 | 10 | 31% |
| **Bombero**<br>**s ** | CO | 2020 | P99 máximos diarios 1<br>hora | 2 | mg/m3 | 30 | 16% |
| **Bombero**<br>**s ** | NO2 | 2020 | P99 máximos diarios 1<br>hora | 61 | ug/m3 | 400 | 15% |
| **Bombero**<br>**s ** | NO2 | 2018-2020 | Promedio anual | 17 | ug/m3 | 100 | 17% |
| **Bombero**<br>**s ** | SO2 | 2020 | P98,5 1 hora | 23 | ug/m3 | 350 | 7% |
| **Bombero**<br>**s ** | SO2 | 2020 | P99 24 horas | 18 | ug/m3 | 150 | 12% |
| **Bombero**<br>**s ** | SO2 | 2018-2020 | Promedio anual | 4 | ug/m3 | 60 | 7% |
| **La Cruz** | MP10 | 2020 | P9824 horas | 77 | ug/m3 | 130 | 59% |
| **La Cruz** | MP10 | 2018-2020 | Promedio anual | 39 | ug/m3 | 50 | 78% |
| **La Cruz** | CO | 2020 | P99 máximo diarios 8<br>horas | 2 | mg/m3 | 10 | 20% |
| **La Cruz** | CO | 2020 | P99 máximos diarios 1<br>hora | 1 | mg/m3 | 30 | 5% |
| **La Cruz** | NO2 | 2020 | P99 máximos diarios 1<br>hora | 82 | ug/m3 | 400 | 21% |
| **La Cruz** | NO2 | 2018-2020 | Promedio anual | 17 | ug/m3 | 100 | 17% |
| **La Cruz** | SO2 | 2020 | P98,5 1 hora | 22 | ug/m3 | 350 | 6% |
| **La Cruz** | SO2 | 2020 | P99 24 horas | 14 | ug/m3 | 150 | 9% |
| **La Cruz** | SO2 | 2018-2020 | Promedio anual | 5 | ug/m3 | 60 | 9%% |
| **La Palma** | MP10 | 2020 | P9824 horas | 61 | ug/m3 | 130 | 50% |
| **La Palma** | MP10 | 2018-2020 | Promedio anual | 37 | ug/m3 | 50 | 74% |
| **La Palma** | CO | 2020 | P99 máximo diarios 8<br>horas | 2 | mg/m3 | 10 | 15% |
| **La Palma** | CO | 2020 | P99 máximos diarios 1<br>hora | 1 | mg/m3 | 30 | 3% |
| **La Palma** | NO2 | 2020 | P99 máximos diarios 1<br>hora | 49 | ug/m3 | 400 | 12% |
| **La Palma** | NO2 | 2018-2020 | Promedio anual | 10 | ug/m3 | 100 | 20% |
| **La Palma** | SO2 | 2020 | P98,5 1 hora | 20 | ug/m3 | 350 | 65% |
| **La Palma** | SO2 | 2020 | P99 24 horas | 12 | ug/m3 | 150 | 8% |
| **La Palma** | SO2 | 2018-2020 | Promedio anual | 4 | ug/m3 | 60 | 7% |
| **Manzana**<br>**r ** | MP10 | 2020 | P9824 horas | 72 | ug/m3 | 130 | 55% |
| **Manzana**<br>**r ** | MP10 | 2018-2020 | Promedio anual | 36 | ug/m3 | 50 | 72% |

**Tabla 14.: Comparación material particulado con normas de calidad primaria y secundaria****

| Recepto<br>r | MP10 (ug/m3) | Col3 | % DS N°12/2022<br>MMA | Col5 | MP2,5 (ug/m3) | Col7 | % DS N°12/2012<br>MMA | Col9 | MPS<br>(mg/m2dia) | Col11 | Ordenanza<br>Confederación<br>Suiza | Decreto<br>1.074/201<br>8<br>Argentina |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recepto**<br>**r ** | **24**<br>**horas** | **Anual** | **24 horas** | **Anual** | **24**<br>**horas** | **Anual** | **24 horas** | **Anual** | **30**<br>**días** | **Anual** | **30 días** | **Anual** |
| **R1** | 0,06534 | 0,0653<br>4 | 0,050% | 0,131% | 0,00868 | 0,0086<br>8 | 0,017% | 0,043% | 0,0222 | 0,022<br>1 | 0,011% | 0,000% |
| **R2** | 0,02915 | 0,0291<br>5 | 0,022% | 0,058% | 0,00400 | 0,0040<br>0 | 0,008% | 0,020% | 0,0002 | 0,000<br>2 | 0,000% | 0,000% |
| **R3** | 0,01802 | 0,0180<br>2 | 0,014% | 0,036% | 0,00268 | 0,0026<br>8 | 0,005% | 0,013% | 0,0024 | 0,002<br>4 | 0,001% | 0,000% |
| **R4** | 0,01610 | 0,0161<br>0 | 0,012% | 0,032% | 0,00241 | 0,0024<br>1 | 0,005% | 0,012% | 0,0024 | 0,002<br>5 | 0,001% | 0,000% |
| **R5** | 0,01693 | 0,0169<br>3 | 0,013% | 0,034% | 0,00256 | 0,0025<br>6 | 0,005% | 0,013% | 0,0032 | 0,003<br>3 | 0,002% | 0,000% |
| **R6** | 0,01744 | 0,0174<br>4 | 0,013% | 0,035% | 0,00267 | 0,0026<br>7 | 0,005% | 0,013% | 0,0040 | 0,004<br>0 | 0,002% | 0,000% |
| **R10** | 0,02000 | 0,0200<br>0 | 0,015% | 0,040% | 0,00337 | 0,0033<br>7 | 0,007% | 0,017% | 0,0132 | 0,013<br>2 | 0,007% | 0,000% |
| **R7** | 0,01412 | 0,0141<br>2 | 0,011% | 0,028% | 0,00227 | 0,0022<br>7 | 0,005% | 0,011% | 0,0058 | 0,005<br>8 | 0,003% | 0,000% |
| **R8** | 0,00187 | 0,0018<br>7 | 0,001% | 0,004% | 0,00026 | 0,0002<br>6 | 0,001% | 0,001% | 0,0000 | 0,000<br>0 | 0,000% | 0,000% |
| **R9** | 0,00076 | 0,0007<br>6 | 0,001% | 0,002% | 0,00010 | 0,0001<br>0 | 0,000% | 0,001% | 0,0000 | 0,000<br>0 | 0,000% | 0,000% |
| **R11** | 0,00186 | 0,0018<br>6 | 0,001% | 0,004% | 0,00028 | 0,0002<br>8 | 0,001% | 0,001% | 0,0000 | 0,000<br>0 | 0,000% | 0,000% |
| **R12** | 0,01346 | 0,0134<br>6 | 0,010% | 0,027% | 0,00187 | 0,0018<br>7 | 0,004% | 0,009% | 0,0003 | 0,000<br>3 | 0,000% | 0,000% |
| **R13** | 0,04329 | 0,0432<br>9 | 0,033% | 0,087% | 0,00607 | 0,0060<br>7 | 0,012% | 0,030% | 0,0064 | 0,006<br>4 | 0,003% | 0,000% |
| **R14** | 0,01540 | 0,0154<br>0 | 0,012% | 0,031% | 0,00218 | 0,0021<br>8 | 0,004% | 0,011% | 0,0003 | 0,000<br>3 | 0,000% | 0,000% |
| **R15** | 0,02500 | 0,0250<br>0 | 0,019% | 0,050% | 0,00397 | 0,0039<br>7 | 0,008% | 0,020% | 0,0096 | 0,009<br>5 | 0,005% | 0,000% |
| **R16** | 0,61995 | 0,6199<br>5 | 0,477% | 1,240% | 0,09066 | 0,0906<br>6 | 0,181% | 0,453% | 0,6673 | 0,664<br>2 | 0,334% | 0,007% |

**Tabla 15.: Comparación gases de combustión con normas de calidad primaria y secundaria****

| Receptor | NOx | Col3 | % DS N°114/2002 MINSEGPRES | Col5 | SOx | Col7 | Col8 | % Norma primaria<br>DS N°104/2018 MMA | Col10 | Col11 | % Norma secundaria<br>DS N°22/2010 MINSEGPRES | Col13 | Col14 | CO | Col16 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor <br> | **1 hora** | **anual** | **1 hora** | A**nual** | **1 hora** | **24 horas** | **Anual** | **1 hora** | **24 horas** | **Anual** | **1 hora** | **24 horas** | **Anual** | **1 hora** | **8 horas** | **1 hora** |
| **R1 ** | 0,01925 | 0,01000 | 0,005% | 0,010% | 0,00927 | 0,00271 | 0,00054 | 0,0026% | 0,0018% | 0,0009% | 0,0009% | 0,0007% | 0,0007% | 0,01093 | 0,00383 | 0,00004% |
| **R2 ** | 0,01715 | 0,00588 | 0,004% | 0,006% | 0,00846 | 0,00151 | 0,00032 | 0,0024% | 0,0010% | 0,0005% | 0,0008% | 0,0004% | 0,0004% | 0,00934 | 0,00208 | 0,00003% |
| **R3 ** | 0,00849 | 0,00432 | 0,002% | 0,004% | 0,00406 | 0,00104 | 0,00016 | 0,0012% | 0,0007% | 0,0003% | 0,0004% | 0,0003% | 0,0002% | 0,00472 | 0,00146 | 0,00002% |
| **R4 ** | 0,00878 | 0,00393 | 0,002% | 0,004% | 0,00420 | 0,00094 | 0,00014 | 0,0012% | 0,0006% | 0,0002% | 0,0004% | 0,0003% | 0,0002% | 0,00479 | 0,00132 | 0,00002% |
| **R5 ** | 0,01023 | 0,00437 | 0,003% | 0,004% | 0,00490 | 0,00102 | 0,00015 | 0,0014% | 0,0007% | 0,0002% | 0,0005% | 0,0003% | 0,0002% | 0,00555 | 0,00143 | 0,00002% |
| **R6 ** | 0,01237 | 0,00470 | 0,003% | 0,005% | 0,00594 | 0,00108 | 0,00015 | 0,0017% | 0,0007% | 0,0003% | 0,0006% | 0,0003% | 0,0002% | 0,00662 | 0,00152 | 0,00002% |
| **R10 ** | 0,01611 | 0,00775 | 0,004% | 0,008% | 0,00773 | 0,00154 | 0,00016 | 0,0022% | 0,0010% | 0,0003% | 0,0008% | 0,0004% | 0,0002% | 0,00875 | 0,00220 | 0,00003% |
| **R7 ** | 0,01653 | 0,00447 | 0,004% | 0,004% | 0,00793 | 0,00096 | 0,00011 | 0,0023% | 0,0006% | 0,0002% | 0,0008% | 0,0003% | 0,0001% | 0,00856 | 0,00137 | 0,00003% |
| **R8 ** | 0,01628 | 0,00031 | 0,004% | 0,000% | 0,00784 | 0,00009 | 0,00002 | 0,0022% | 0,0001% | 0,0000% | 0,0008% | 0,0000% | 0,0000% | 0,00789 | 0,00012 | 0,00003% |
| **R9 ** | 0,01754 | 0,00014 | 0,004% | 0,000% | 0,00844 | 0,00004 | 0,00001 | 0,0024% | 0,0000% | 0,0000% | 0,0008% | 0,0000% | 0,0000% | 0,00846 | 0,00005 | 0,00003% |
| **R11 ** | 0,01857 | 0,00040 | 0,005% | 0,000% | 0,00892 | 0,00011 | 0,00002 | 0,0025% | 0,0001% | 0,0000% | 0,0009% | 0,0000% | 0,0000% | 0,00898 | 0,00015 | 0,00003% |
| **R12 ** | 0,02025 | 0,00257 | 0,005% | 0,003% | 0,00970 | 0,00069 | 0,00013 | 0,0028% | 0,0005% | 0,0002% | 0,0010% | 0,0002% | 0,0002% | 0,01010 | 0,00093 | 0,00003% |
| **R13 ** | 0,02351 | 0,00832 | 0,006% | 0,008% | 0,01128 | 0,00212 | 0,00037 | 0,0032% | 0,0014% | 0,0006% | 0,0011% | 0,0006% | 0,0005% | 0,01259 | 0,00298 | 0,00004% |
| **R14 ** | 0,02088 | 0,00283 | 0,005% | 0,003% | 0,01000 | 0,00077 | 0,00014 | 0,0029% | 0,0005% | 0,0002% | 0,0010% | 0,0002% | 0,0002% | 0,01047 | 0,00107 | 0,00003% |
| **R15 ** | 0,02353 | 0,00832 | 0,006% | 0,008% | 0,01125 | 0,00168 | 0,00023 | 0,0032% | 0,0011% | 0,0004% | 0,0011% | 0,0005% | 0,0003% | 0,01237 | 0,00248 | 0,00004% |
| **R16 ** | 0,10639 | 0,17430 | 0,027% | 0,174% | 0,05303 | 0,04065 | 0,00935 | 0,0152% | 0,0271% | 0,0156% | 0,0053% | 0,0111% | 0,0117% | 0,07696 | 0,05719 | 0,00026% |
| **R17 ** | 0,03759 | 0,03709 | 0,009% | 0,037% | 0,01780 | 0,00707 | 0,00065 | 0,0051% | 0,0047% | 0,0011% | 0,0018% | 0,0019% | 0,0008% | 0,02255 | 0,01012 | 0,00008% |
| **R18 ** | 0,02433 | 0,01112 | 0,006% | 0,011% | 0,01166 | 0,00262 | 0,00041 | 0,0033% | 0,0017% | 0,0007% | 0,0012% | 0,0007% | 0,0005% | 0,01331 | 0,00370 | 0,00004% |
| **R19 ** | 0,01987 | 0,00278 | 0,005% | 0,003% | 0,00947 | 0,00075 | 0,00014 | 0,0027% | 0,0005% | 0,0002% | 0,0009% | 0,0002% | 0,0002% | 0,00990 | 0,00101 | 0,00003% |
| **R20 ** | 0,01841 | 0,00035 | 0,005% | 0,000% | 0,00877 | 0,00009 | 0,00002 | 0,0025% | 0,0001% | 0,0000% | 0,0009% | 0,0000% | 0,0000% | 0,00882 | 0,00012 | 0,00003% |
| **R21 ** | 0,02690 | 0,01795 | 0,007% | 0,018% | 0,01257 | 0,00457 | 0,00100 | 0,0036% | 0,0030% | 0,0017% | 0,0013% | 0,0013% | 0,0013% | 0,01535 | 0,00655 | 0,00005% |
| **R22 ** | 0,02318 | 0,01105 | 0,006% | 0,011% | 0,01127 | 0,00283 | 0,00061 | 0,0032% | 0,0019% | 0,0010% | 0,0011% | 0,0008% | 0,0008% | 0,01293 | 0,00393 | 0,00004% |
| **R23 ** | 0,15126 | 0,26777 | 0,038% | 0,268% | 0,07366 | 0,06409 | 0,01505 | 0,0210% | 0,0427% | 0,0251% | 0,0074% | 0,0176% | 0,0188% | 0,10864 | 0,08503 | 0,00036% |
| **R24 ** | 0,17665 | 0,31905 | 0,044% | 0,319% | 0,08814 | 0,07548 | 0,01806 | 0,0252% | 0,0503% | 0,0301% | 0,0088% | 0,0207% | 0,0226% | 0,12965 | 0,10110 | 0,00043% |
| **R25 ** | 0,44522 | 0,85666 | 0,111% | 0,857% | 0,23187 | 0,19271 | 0,04862 | 0,0662% | 0,1285% | 0,0810% | 0,0232% | 0,0528% | 0,0608% | 0,33669 | 0,25831 | 0,00112% |

**Tabla 16.: Aporte del Proyecto a condición base****

| Estación EMRP | Contaminante | Periodo | Estadígrafo | Valor | Aporte<br>proyecto | Condición<br>base +<br>proyecto | Unidad | Norma | % Norma<br>Condición<br>base +<br>aporte<br>proyecto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bomberos** | MP2,5 | 2020 | P9824 horas | 47 | 0,01415 | 47,014 | ug/m3 | 50 | 94% |
| **Bomberos** | MP2,5 | 2019-2020 | Promedio | 22 | 0,01415 | 22,014 | ug/m3 | 20 | 110% |
| **Bomberos** | MP10 | 2020 | P9824 horas | 75 | 0,00196 | 75,002 | ug/m3 | 130 | 58% |
| **Bomberos** | MP10 | 2018-2020 | Promedio anual | 43 | 0,00196 | 43,002 | ug/m3 | 50 | 86% |
| **Bomberos** | CO | 2020 | P99 máximo diarios 8 horas | 3 | 0,00857 | 3,009 | mg/m3 | 10 | 30% |
| **Bomberos** | CO | 2020 | P99 máximos diarios 1 hora | 2 | 0,00109 | 2,001 | mg/m3 | 30 | 7% |
| **Bomberos** | NO2 | 2020 | P99 máximos diarios 1 hora | 61 | 0,01678 | 61,017 | ug/m3 | 400 | 15% |
| **Bomberos** | NO2 | 2018-2020 | Promedio anual | 17 | 0,00326 | 17,003 | ug/m3 | 100 | 17% |
| **Bomberos** | SO2 | 2020 | P98,5 1 hora | 23 | 0,00812 | 23,008 | ug/m3 | 350 | 7% |
| **Bomberos** | SO2 | 2020 | P99 24 horas | 18 | 0,00082 | 18,001 | ug/m3 | 150 | 12% |
| **Bomberos** | SO2 | 2018-2020 | Promedio anual | 4 | 0,00017 | 4,000 | ug/m3 | 60 | 7% |
| **La Cruz** | MP10 | 2020 | P9824 horas | 77 | 0,00605 | 77,006 | ug/m3 | 130 | 59% |
| **La Cruz** | MP10 | 2018-2020 | Promedio anual | 39 | 0,00605 | 39,006 | ug/m3 | 50 | 78% |
| **La Cruz** | CO | 2020 | P99 máximo diarios 8 horas | 2 | 0,00068 | 2,001 | mg/m3 | 10 | 20% |
| **La Cruz** | CO | 2020 | P99 máximos diarios 1 hora | 1 | 0,00827 | 1,008 | mg/m3 | 30 | 3% |
| **La Cruz** | NO2 | 2020 | P99 máximos diarios 1 hora | 82 | 0,01662 | 82,017 | ug/m3 | 400 | 21% |
| **La Cruz** | NO2 | 2018-2020 | Promedio anual | 17 | 0,00235 | 17,002 | ug/m3 | 100 | 17% |
| **La Cruz** | SO2 | 2020 | P98,5 1 hora | 22 | 0,00795 | 22,008 | ug/m3 | 350 | 6% |
| **La Cruz** | SO2 | 2020 | P99 24 horas | 14 | 0,00051 | 14,001 | ug/m3 | 150 | 9% |
| **La Cruz** | SO2 | 2018-2020 | Promedio anual | 5 | 0,00005 | 5,000 | ug/m3 | 60 | 8% |
| **La Palma** | MP10 | 2020 | P9824 horas | 61 | 0,02429 | 61,024 | ug/m3 | 130 | 47% |
| **La Palma** | MP10 | 2018-2020 | Promedio anual | 37 | 0,02429 | 37,024 | ug/m3 | 50 | 74% |

**Tabla 17.: Nivel de significancia aporte Proyecto en Estación Bomberos****

| Contaminantes | Aporte Proyecto<br>(ug/m3) | SIL (ug/m3) | Porcentaje SIL |
| --- | --- | --- | --- |
| **MP10 anual** | 0,00196 | 1 | 0,20% |
| **MP10 24 horas** | 0,00196 | 5 | 0,04% |
| **MP2.5 anual** | 0,01415 | 0,2 | 7,08% |

**Tabla 18.: Comparación con límites Anteproyecto PPDA****

| Contaminante | Emisiones Año 1<br>Proyecto | Límite emisión<br>Anteproyecto | Cumplimiento |
| --- | --- | --- | --- |
| **MP10** | **2,0790** | 5 | Sí |
| **MP2.5** | **0,2824** | 2,5 | Sí |
| **NOx** | **0,6103** | 20 | Sí |
| **SOx** | **0,0277** | 10 | Sí |

**Tabla 20.: Evaluación de impactos****

| Recurso | Potencial<br>impacto | Evaluación cualitativa | Evaluación cuantitativa |
| --- | --- | --- | --- |
| **Aire** | Impactos en<br>la calidad del<br>aire | Las<br>emisiones<br>de<br>Material<br>Particulado (MP10, MP2.5 y MPS) y<br>gases de combustión que generará<br>el Proyecto no ocasionarán un<br>impacto<br>significativo<br>sobre<br>la<br>capacidad del aire, para mantener<br>las<br>funciones<br>de<br>procreación,<br>reproducción,<br>crecimiento,<br>transformación o restablecimiento<br>de recursos naturales, debido a que<br>las normas de calidad primarias y<br>secundarias<br>no<br>se<br>ven<br>sobrepasadas con las emisiones del<br>Proyecto en ninguna sus fases.<br> <br>Adicionalmente<br>es<br>importante<br>destacar que las mayores tasas de<br>emisión se generarán durante el año<br>1 del Proyecto, el cual considera la<br>fase de construcción y operación.<br> | Las emisiones que generará el<br>Proyecto representan menos del<br>7% de los límites establecidos<br>en<br>las<br>normas<br>de<br>calidad<br>primaria y secundaria del aire. |
| **Aire** | Impacto en la<br>calidad<br>del<br>aire<br>que<br>ocasiona<br>impactos<br>sobre<br>otro<br>recurso<br>natural<br>renovable | Se establece que las emisiones<br>partículas que generará el Proyecto<br>(MP10, MP2.5 y MPS) y gases de<br>combustión,<br>no<br>ocasionarán<br>un<br>impacto<br>significativo<br>sobre<br>la<br>vegetación,<br>cultivos<br>cercanos,<br>cursos de agua, flora, fauna u otros<br>recursos<br>naturales<br>de<br>la<br>zona<br>debido a que las normas de calidad<br>secundarias<br>utilizadas<br>como<br>referencia (Norma Confederación<br>Suiza<br>y <br>Decreto<br>1.074/2018<br>Argentina), no se ven sobrepasadas<br>con las emisiones del Proyecto,<br>considerando que las normas de<br>calidad<br>secundaria<br>apuntan<br>a <br>proteger los recursos naturales. Por<br>lo tanto, se puede concluir que, a<br>nivel de calidad del aire, el Proyecto<br>no genera un impacto significativo<br>en la calidad de los recursos<br>naturales del área de influencia.<br> <br>Adicionalmente<br>es<br>importante<br>destacar que las mayores tasas de<br>emisión se generarán durante el año<br>1 del Proyecto, el cual considera la<br>fase de construcción y operación. | <br>En<br>los<br>receptores<br>correspondientes a cultivos las<br>emisiones<br>de<br>MPS<br>que<br>generará<br>el<br>Proyecto<br>representan menos del 2,81%<br>de los límites establecidos en<br>las<br>normas<br>de<br>calidad<br>secundaria del aire. Por lo tanto,<br>no se ocasiona un impacto<br>significativo en los cultivos y<br>vegetación cercana al Proyecto. |
