---
title: CAPITULO I
author: WinuE
date: D:20250604020336-04'00'
language: es
type: report
pages: 64
has_toc: False
has_tables: True
extraction_quality: high
keywords: [CAPÍTULO I]
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA COMPLEMENTARIA MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS APARTADO 8 - PAS 137 ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
-->

# ADENDA COMPLEMENTARIA MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS APARTADO 8 - PAS 137 ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS

**Comuna de Empedrado - Región del Maule**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

|ELABORADO POR|REVISADO POR|APROBADO POR|
|---|---|---|
|Francisco Parra, Geólogo, MSc.<br>|PM|AAC|
|**FECHA EMISIÓN**|**FECHA REVISIÓN**|**VoBo AUTORIZADO**<br>**PARA ENTREGA**|
|27/05/25|30/05/25|30/05/25|

MINA LAS PIEDRAS - MIGRIN S.A7237- EMI0 - MAYO 2025 i

EMPEDRADO - VII REGIÓN

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

## APARTADO 8 ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS -MINA LAS PIEDRAS, EMPEDRADO, VII REGIÓN, CHILE

**TABLA DE CONTENIDO**

**CONTENIDO**

**APARTADO 4 ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS -MINA LAS**
**PIEDRAS, EMPEDRADO, VII REGIÓN, CHILE ......................................................................... II**

**1.** **INTRODUCCIÓN ............................................................................................................... 1**

**1.1** **ANTECEDENTES DEL PROYECTO .............................................................................. 1**

**1.2** **OBJETIVOS DEL ANÁLISIS DE RIESGOS ................................................................... 1**

**1.3** **ALCANCE DEL ESTUDIO .............................................................................................. 2**

**1.4** **UBICACIÓN GEOGRÁFICA Y CONTEXTO GENERAL ................................................. 3**

**2.** **METODOLOGÍA DE EVALUACIÓN DE RIESGOS .......................................................... 4**

**2.1** **ENFOQUE GENERAL .................................................................................................... 4**

**2.2** **METODOLOGÍA PARA EVALUACIÓN DE SUSCEPTIBILIDAD ................................... 5**

2.2.1 E NFOQUE BASADO EN APRENDIZAJE NO SUPERVISADO ............................................. 5

2.2.2 V ARIABLES PREDICTORAS UTILIZADAS ..................................................................... 6

2.2.3 I MPLEMENTACIÓN DEL MODELO ............................................................................... 7

2.2.4 D ETERMINACIÓN DEL NÚMERO DE CLUSTERS ........................................................... 8

2.2.5 I NTERPRETACIÓN Y ASIGNACIÓN DE NIVELES DE SUSCEPTIBILIDAD ............................ 9

**2.3** **METODOLOGÍA PARA LA EVALUACIÓN DE VULNERABILIDAD ............................ 10**

2.3.1 E NFOQUE HÍBRIDO ............................................................................................... 10

2.3.2 V ULNERABILIDAD SOCIAL EXTERNA ....................................................................... 11

2.3.3 V ULNERABILIDAD INTERNA DE LA FAENA ................................................................ 12

2.3.4 G ENERACIÓN DEL MAPA DE VULNERABILIDAD COMBINADO ...................................... 13

2.3.5 A SIGNACIÓN DE NIVELES DE VULNERABILIDAD ........................................................ 14

**2.4** **METODOLOGÍA PARA ESTIMACIÓN DEL RIESGO .................................................. 14**

2.4.1 C OMBINACIÓN DE LA SUSCEPTIBILIDAD CON LA VULNERABILIDAD ............................. 15

2.4.2 M ATRIZ DE RIESGO UTILIZADA ............................................................................... 16

2.4.3 G ENERACIÓN DE MAPAS DE RIESGO POR PELIGRO ................................................. 16

**2.5** **ARQUITECTURA DEL FLUJO DE TRABAJO Y HERRAMIENTAS IMPLEMENTADAS**
**17**

2.5.1 A RQUITECTURA DEL FLUJO DE TRABAJO ................................................................ 17

MINA LAS PIEDRAS - MIGRIN S.A7237- EMI0 - MAYO 2025 ii

EMPEDRADO - VII REGIÓN

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

2.5.2 T ECNOLOGÍAS Y HERRAMIENTAS R IMPLEMENTADAS .............................................. 19

**3.** **CARACTERIZACIÓN DEL CONJUNTO DE DATOS ...................................................... 20**

**3.1** **FUENTES DE DATOS UTILIZADAS ............................................................................ 20**

3.1.1 D ATOS ESPACIALES BASE ..................................................................................... 20

3.1.2 D ATOS PRIMARIOS Y SECUNDARIOS CONTEXTUALES .............................................. 20

**3.2** **PREPROCESAMIENTO Y DERIVACIÓN DE VARIABLES .......................................... 21**

3.2.1 A RMONIZACIÓN ESPACIAL Y PREPROCESAMIENTO BASE ......................................... 21

3.2.2 V ARIABLES PREDICTORAS DERIVADAS ................................................................... 22

**4.** **RESULTADOS DEL ANÁLISIS DE SUSCEPTIBILIDAD ................................................ 23**

**4.1** **ZONIFICACIÓN DE SUSCEPTIBILIDAD A REMOCIONES EN MASA ........................ 23**

**4.2** **ZONIFICACIÓN DE SUSCEPTIBILIDAD A INUNDACIONES (FLUVIAL LOCAL /**
**PLUVIAL) ................................................................................................................................. 26**

**4.3** **ZONIFICACIÓN DE SUSCEPTIBILIDAD A EROSIÓN HÍDRICA ................................. 29**

**4.4** **TABLA RESUMEN DE SUSCEPTIBILIDAD POR CLUSTER Y PELIGRO .................. 31**

**5.** **EVALUACIÓN DE LA VULNERABILIDAD ..................................................................... 33**

**5.1** **VULNERABILIDAD SOCIAL DEL ENTORNO .............................................................. 33**

**5.1** **VULNERABILIDAD OPERACIONAL/FÍSICA ............................................................... 36**

**5.2** **MAPA DE VULNERABILIDAD COMBINADO .............................................................. 37**

**6.** **ESTIMACIÓN DEL RIESGO GEOLÓGICO Y GEOMORFOLÓGICO ............................. 41**

**6.1** **RIESGO POR REMOCIONES EN MASA ..................................................................... 41**

**6.2** **RIESGO POR INUNDACIONES ................................................................................... 44**

**6.3** **RIESGO POR EROSIÓN HÍDRICA ............................................................................... 47**

**6.4** **CONSIDERACIONES SOBRE RIESGO SÍSMICO ....................................................... 49**

**7.** **MEDIDAS DE MITIGACIÓN ............................................................................................ 50**

**7.1** **MEDIDAS DE MITIGACIÓN POR ZONA DE RIESGO ................................................. 50**

7.1.1 C ONTROL DE REMOCIONES EN MASA ..................................................................... 50

7.1.2 C ONTROL DE INUNDACIONES ................................................................................ 51

7.1.3 C ONTROL DE EROSIÓN HÍDRICA ............................................................................ 52

**8.** **CONCLUSIONES Y RECOMENDACIONES ................................................................... 54**

MINA LAS PIEDRAS - MIGRIN S.A7237- EMI0 - MAYO 2025 iii

EMPEDRADO - VII REGIÓN

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**8.1** **CONCLUSIONES PRINCIPALES ................................................................................. 54**

**8.2** **RECOMENDACIONES ................................................................................................. 55**

**9.** **BIBLIOGRAFÍA ............................................................................................................... 56**

MINA LAS PIEDRAS - MIGRIN S.A7237- EMI0 - MAYO 2025 iv

EMPEDRADO - VII REGIÓN

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**1.** **ÍNDICE DE TABLAS**

TABLA 1: MATRIZ DE RIESGO ...................................................................................................................15

TABLA 2: SIGNIFICADO DE CLUSTERS ....................................................................................................32

**2.** **ÍNDICE DE FIGURAS**

FIGURA 1: LOCALIZACIÓN DEL ÁREA DEL PROYECTO ........................................................................... 4

FIGURA 2: DIAGRAMA DE FLUJO ..............................................................................................................18

FIGURA 3: MAPA DE SUSCEPTIBILIDAD DE REMOCIONES EN MASA ..................................................25

FIGURA 4: MAPA DE SUSCEPTIBILIDAD DE INUNDACIONES ................................................................28
FIGURA 5: MAPA DE SUSCEPTIBILIDAD DE EROSIÓN ...........................................................................30

FIGURA 6: MAPA DE VULNERABILIDAD SOCIAL .....................................................................................35

FIGURA 7: MAPA DE VULNERABILIDAD DENTRO DE LA FAENA ...........................................................36

FIGURA 8: MAPA DE VULNERABILIDAD DE REMOCIONES EN MASA ...................................................38

FIGURA 9: MAPA DE VULNERABILIDAD DE INUNDACIONES .................................................................39
FIGURA 10: MAPA DE VULNERABILIDAD DE EROSIÓN ..........................................................................40

FIGURA 11: MAPA DE RIESGO DE REMOCIONES EN MASA ..................................................................43

FIGURA 12: MAPA DE RIESGO DE INUNDACIONES ................................................................................46
FIGURA 13: MAPA DE RIESGO DE EROSIÓN ...........................................................................................48

MINA LAS PIEDRAS - MIGRIN S.A7237- EMI0 - MAYO 2025 v

EMPEDRADO - VII REGIÓN

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**1.** **INTRODUCCIÓN**

**1.1 ANTECEDENTES DEL PROYECTO**

El presente análisis de riesgos geológicos y geomorfológicos se enmarca en el proyecto
"Modificación y Optimización Faena Minera de Cuarzo Planta Las Piedras", propiedad de
MIGRIN S.A., ubicado en la comuna de Empedrado, Región del Maule, Chile. La faena
minera Las Piedras se dedica a la extracción y procesamiento de rocas no metálicas,
principalmente cuarzo y sílice, destinadas a diversas aplicaciones industriales. Las
operaciones y modificaciones contempladas en el proyecto se desarrollan dentro del área
ambientalmente aprobada según la Resolución de Calificación Ambiental (RCA)
N°214/2009.

Este informe evalúa específicamente los riesgos geológicos y geomorfológicos asociados
al área de emplazamiento de la faena, utilizando una metodología actualizada que integra
análisis espacial y técnicas de aprendizaje automático, como se detallará en las secciones
siguientes.

**1.2 OBJETIVOS DEL ANÁLISIS DE RIESGOS**

El presente estudio tiene como finalidad principal evaluar de manera integral los riesgos
geológicos y geomorfológicos asociados al área de emplazamiento de la Faena Minera Las
Piedra. Para lograr esto, se establecieron los siguientes objetivos específicos:

 - Identificar y Caracterizar la Susceptibilidad Espacial: Determinar las zonas dentro
del área de estudio que presentan una mayor o menor propensión intrínseca a la
ocurrencia de los principales procesos geomorfológicos relevantes: remociones en
masa, inundaciones (de tipo fluvial local y/o pluvial) y erosión hídrica. Esto se
realizará mediante la integración de datos topográficos, de cobertura superficial
(índices satelitales), geológicos y de proximidad (a cauces y fallas) utilizando
técnicas de aprendizaje no supervisado (clustering).

 - Desarrollar una Zonificación de Susceptibilidad: Generar mapas temáticos
espacialmente explícitos que clasifiquen el área de estudio en diferentes niveles de
susceptibilidad (ej. Baja, Media, Alta) para cada uno de los peligros analizados,
basados en los patrones identificados por los modelos de clustering.

 - Evaluar la Vulnerabilidad de Forma Híbrida: Caracterizar la vulnerabilidad de los
elementos expuestos dentro del área de estudio, aplicando un enfoque diferenciado:

`o` Evaluar la vulnerabilidad social de las localidades rurales circundantes

mediante indicadores derivados de datos censales (Censo 2017).
`o` Evaluar la vulnerabilidad operacional y física dentro del perímetro de la faena

minera, considerando la exposición del personal (~53 trabajadores) y la
ubicación/criticidad de la infraestructura existente (depósitos, planta,
oficinas, etc.) basada en información específica del proyecto.
`o` Generar un mapa de vulnerabilidad integrado que combine ambas

evaluaciones.

 - Estimar el Riesgo Geomorfológico: Combinar los mapas de susceptibilidad (Peligro)
con el mapa de vulnerabilidad integrada para obtener una estimación espacial del
nivel de riesgo (ej. Bajo, Medio, Alto, Muy Alto) para cada uno de los peligros

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

analizados (remociones en masa, inundaciones, erosión hídrica), utilizando una
matriz de riesgo definida.

 - Proporcionar Insumos para la Gestión: Entregar resultados (mapas,
interpretaciones, conclusiones) que sirvan como base técnica sólida para:

`o` La priorización de medidas de control y mitigación.
`o` El diseño enfocado de planes de monitoreo y seguimiento.
`o` La actualización y mejora de los planes de contingencia.
`o` La toma de decisiones informada respecto a la seguridad y sostenibilidad de

la faena.

**1.3 ALCANCE DEL ESTUDIO**

El presente análisis de riesgos se enfoca en la evaluación de la susceptibilidad,
vulnerabilidad y riesgo asociados a los principales procesos geológicos y geomorfológicos
superficiales que pueden afectar el área de estudio definida por el polígono de alcance
proporcionado, la cual incluye la Faena Minera Las Piedras y su entorno inmediato.

El alcance específico comprende:

 - Identificación y Análisis de Peligros: Se evalúan tres peligros geomorfológicos
principales:

`o` Remociones en Masa: Incluyendo deslizamientos superficiales y procesos

asociados a la inestabilidad de laderas naturales y taludes modificados por
la actividad minera.
`o` Inundaciones: Enfocado en inundaciones de tipo fluvial local (crecidas en

esteros/quebradas dentro o cercanos al área) y pluvial (encharcamiento por
lluvias intensas), dada la ubicación interior del sitio. No se incluye el análisis
de inundación costera por tsunami.
`o` Erosión Hídrica: Evaluación de la propensión a la pérdida de suelo por acción

de la escorrentía superficial (laminar, surcos, cárcavas).

 - Evaluación de Susceptibilidad: Se realiza una zonificación espacial de la
susceptibilidad relativa para cada uno de los tres peligros mencionados, mediante
la aplicación de clustering K-Means sobre un conjunto integrado de variables
predictoras (topográficas, índices satelitales, geológicas, proximidad).

 - Evaluación de Vulnerabilidad: Se caracteriza la vulnerabilidad de forma híbrida:

`o` Vulnerabilidad Social (Externa): Evaluación de las localidades rurales en el

entorno de la faena, basada en indicadores socio-demográficos y de vivienda
derivados de datos censales (Censo 2017).
`o` Vulnerabilidad Operacional/Física (Interna): Evaluación del área operativa

de la faena, considerando la exposición del personal (aproximadamente 50
trabajadores) y la ubicación/criticidad de la infraestructura minera (depósitos,
planta, oficinas, etc.).

 - Estimación del Riesgo: Se integran los resultados de susceptibilidad y vulnerabilidad
mediante una matriz de riesgo definida para generar mapas de nivel de riesgo (Bajo,
Medio, Alto, Muy Alto) para cada uno de los tres peligros evaluados.

 - Fuentes de Datos: El estudio se basa fundamentalmente en el análisis de datos
espaciales base (modelos de elevación digital de alta resolución, imágenes Sentinel2, cartografía geológica, estructural e hidrográfica) y datos operacionales
proporcionados, complementados con información contextual de estudios técnicos
previos del proyecto citados en este informe.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

 - Limitaciones

`o` Este estudio no realizauna evaluación de la susceptibilidad sísmica

(amplificación del terreno) puesto que ya existe un estudio realizado el año
2017 que cubre ese aspecto (SIRVE, 2017).
`o` Este análisis no reemplaza ni valida los diseños geotécnicos específicos de

las obras mineras (estabilidad de taludes del rajo, muros de depósitos, etc.),
los cuales deben basarse en estudios de ingeniería detallados con
parámetros de sitio.
`o` La evaluación de vulnerabilidad social se basa en datos del Censo 2017 y

puede no reflejar completamente las condiciones socioeconómicas actuales.
`o` No se incluyen en el alcance riesgos de naturaleza no
geológica/geomorfológica (ej. financieros, operacionales puros, legales,
sociales más allá de la vulnerabilidad demográfica/vivienda).

**1.4 UBICACIÓN GEOGRÁFICA Y CONTEXTO GENERAL**

La Faena Minera Las Piedras se emplaza en la VII Región del Maule, Provincia de Talca,
en la comuna de Empedrado. Las coordenadas geográficas centrales aproximadas del área
del proyecto son 6.059.800 N y 735.530 E (Datum WGS84 18S), situándose a una altitud
media de 347.5 metros sobre el nivel del mar (Figura 1).

Geográficamente, el proyecto se localiza en el sector occidental de la Cordillera de la Costa.
Esta zona se caracteriza por un relieve de lomajes y colinas suaves, cuyas altitudes
generalmente no superan los 600 msnm. Climática e hidrológicamente, el área se inserta
en la Zona Central de Chile, clasificada como de Ríos en Torrente de Régimen Mixto dentro
de la Zona Subhúmeda.

La faena minera se encuentra a una distancia aproximada de 12 km al oeste de la localidad
de Empedrado y a unos 2.5 km lineales del poblado más cercano, Pueblecillo. El acceso
principal se realiza desde la Ruta M-40, continuando por la Ruta M-420 (camino de ripio)
por cerca de 11 km, para finalmente tomar un camino de acceso a faena de
aproximadamente 1.1 km. El entorno inmediato del proyecto está dominado por
plantaciones forestales, principalmente pinos.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 1: LOCALIZACIÓN DEL ÁREA DEL PROYECTO**

**Fuente: Elaboración propia**

**2.** **METODOLOGÍA DE EVALUACIÓN DE RIESGOS**

**2.1 ENFOQUE GENERAL**

La evaluación de los riesgos geológicos y geomorfológicos asociados a la Faena Minera
Las Piedras y su entorno se aborda mediante un enfoque conceptual estándar,
ampliamente aceptado en la gestión de desastres y análisis de ingeniería, que define el
Riesgo como el producto de la interacción entre el Peligro y la Vulnerabilidad de los
elementos expuestos:

Riesgo= Peligro∗Vulnerabilidad

Este marco permite una evaluación sistemática que considera no solo la probabilidad o
propensión de que ocurra un evento adverso, sino también las potenciales consecuencias
negativas sobre los elementos presentes en el área afectada. En el contexto de este
estudio:

 - Peligro (Evaluado mediante Susceptibilidad): Se refiere a la probabilidad o
propensión de que un proceso geológico o geomorfológico potencialmente dañino
(específicamente, remociones en masa, inundaciones locales/pluviales, y erosión

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

hídrica) ocurra en una determinada área. En este estudio, la dimensión espacial del
peligro se evalúa mediante el análisis de Susceptibilidad, que identifica las zonas
con mayor o menor propensión intrínseca a estos fenómenos basándose en las
características físicas del sitio (topografía, geología, cobertura del suelo,
condiciones hidrológicas, proximidad a estructuras). La metodología detallada para
la evaluación de la susceptibilidad mediante aprendizaje no supervisado se describe
en la Sección 2.2.

 - Vulnerabilidad: Representa el grado en que un elemento o sistema expuesto
(personas, infraestructura física, componentes ambientales) es susceptible a sufrir
daños o pérdidas cuando es impactado por un evento peligroso de cierta intensidad.
La evaluación de la vulnerabilidad en este estudio adopta un enfoque híbrido para
diferenciar las características del entorno rural y las de la operación minera,
considerando tanto aspectos sociales como físicos/operacionales, como se detalla
en la Sección 2.3.

La integración de estos dos componentes (Susceptibilidad y Vulnerabilidad) mediante una
matriz definida (Sección 2.4) permite estimar el nivel de Riesgo de forma espacialmente
explícita, identificando aquellas áreas donde la alta propensión a un peligro coincide con
una alta vulnerabilidad, requiriendo por tanto atención prioritaria en términos de medidas de
control, mitigación y monitoreo. Las secciones subsiguientes de este informe detallan la
aplicación de este enfoque, presentando las metodologías específicas y los resultados
obtenidos para cada componente (Susceptibilidad, Vulnerabilidad y Riesgo) para los
peligros analizados.

**2.2 METODOLOGÍA PARA EVALUACIÓN DE SUSCEPTIBILIDAD**

**2.2.1 Enfoque basado en aprendizaje no supervisado**

Para la evaluación espacial de la susceptibilidad a los diferentes peligros geomorfológicos
(remociones en masa, inundaciones, erosión), se optó por un enfoque basado en
aprendizaje automático no supervisado de clustering. Específicamente, se seleccionó el
algoritmo K-Means por su capacidad robusta y computacionalmente eficiente para
identificar patrones y agrupaciones naturales en conjuntos de datos multidimensionales, sin
requerir información previa sobre la ocurrencia histórica de eventos (como un inventario de
deslizamientos o inundaciones pasadas). Se optó por esta modalidad debido a la falta de
datos etiquetados en la zona referente a los riesgos estudiados.

El objetivo principal de aplicar K-Means en este contexto es agrupar objetivamente áreas
del terreno que comparten características biofísicas y topográficas similares, basándose en
un conjunto de variables predictoras relevantes para cada peligro. Se parte de la premisa
de que áreas con combinaciones similares de factores condicionantes (como pendiente,
tipo de cobertura vegetal, características geológicas, potencial de acumulación de agua,
proximidad a estructuras o cauces, etc.) presentarán un comportamiento y una propensión
similar frente a un determinado proceso geomorfológico.

El algoritmo K-Means funciona particionando el conjunto de datos (representado por los
valores de las variables predictoras extraídas en puntos de muestreo espacial) en un
número predefinido de clusters (k). Luego, se busca minimizar la varianza intra-cluster, es
decir, agrupa los puntos de manera que la distancia euclidiana entre cada punto y el
centroide (promedio multidimensional) de su cluster asignado sea mínima.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

El resultado directo de la aplicación de K-Means es la asignación de cada punto (y, por
extensión, del píxel correspondiente en el mapa) a uno de los k clusters. Esta asignación
forma la base para la zonificación de susceptibilidad, donde cada cluster representa una
zona con un perfil de características homogéneo. La interpretación de qué nivel de
susceptibilidad (ej. Baja, Media, Alta) corresponde a cada cluster se realiza posteriormente,
mediante el análisis de las características promedio (centroides) de las variables predictoras
para cada grupo, como se detalla más adelante. Este enfoque permite una clasificación
espacialmente explícita y basada en datos de la propensión relativa del terreno a los
peligros estudiados.

**2.2.2 Variables predictoras utilizadas**

La identificación de zonas con susceptibilidad homogénea mediante K-Means Clustering se
basó en un conjunto de variables predictoras espacialmente explícitas, derivadas de las
fuentes de datos base (descritas en la Sección 3.1) y procesadas como se detalla en la
Sección 3.2. Estas variables fueron seleccionadas por su relevancia física conocida para
influir en los procesos de remociones en masa, inundaciones y/o erosión hídrica. El conjunto
completo de variables consideradas y utilizadas (para cada modelo el subconjunto final es
diferente) incluye:

a) Variables Derivadas del Modelo Digital de Elevación (MDE): Representan las

características morfométricas e hidrológicas del terreno. Calculadas principalmente
con WhiteboxTools:

a. Pendiente: Inclinación del terreno en grados. Factor clave para la energía

potencial (remociones, erosión) y la velocidad de escorrentía/drenaje
(inundación).
b. Índice Topográfico de Humedad (twi): Logaritmo del área de aporte sobre la

tangente de la pendiente. Indica el potencial de acumulación de humedad en
el suelo debido a la forma del terreno. Relevante para remociones
(saturación) e inundaciones (encharcamiento).
c. Curvatura Planar: Curvatura perpendicular a la dirección de máxima

pendiente. Valores negativos indican convergencia de flujo (favorece
acumulación/incisión), valores positivos indican divergencia. Relevante para
erosión, inundación y algunos tipos de remociones.
d. Curvatura de Perfil: Curvatura en la dirección de la máxima pendiente.

Valores negativos indican concavidad (zonas de acumulación potencial),
valores positivos indican convexidad (zonas de aceleración/erosión).
Relevante para remociones y erosión.
e. Índice de Potencia Fluvial (spi): Producto del área de aporte y la tangente de

la pendiente. Representa la capacidad erosiva del flujo de agua concentrado.
Relevante para erosión en cauces/cárcavas.
f. Elevación: Altitud sobre el nivel del mar. Usada principalmente como

predictor directo para inundaciones (zonas bajas más propensas).
b) Variables Derivadas de Imágenes Satelitales (Sentinel-2): Caracterizan la cobertura

superficial y condiciones de humedad.

a. Índice de Vegetación de Diferencia Normalizada ( _ndvi_ ): Indicador del vigor y

densidad de la vegetación fotosintéticamente activa. Cobertura vegetal
densa (alto NDVI) protege contra erosión y estabiliza taludes
superficialmente.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

b. Índice de Vegetación Mejorado ( _evi_ ): Índice de vegetación alternativo, menos

sensible a efectos atmosféricos y de suelo que el NDVI. Complementa la
información de cobertura vegetal
c. Índice de Suelo Desnudo ( _bsi_ ): Indicador de la proporción de suelo o roca

expuesta, sin cobertura vegetal. Un alto BSI se asocia a mayor
susceptibilidad a erosión y potencialmente a remociones superficiales.
d. Índice de Agua de Diferencia Normalizada ( _ndwi_ ): Sensible a la humedad

contenida en la vegetación y la superficie del suelo. Valores altos indican
mayor humedad, relevante para remociones (saturación) e inundaciones
(encharcamiento).
e. Índice de Agua Normalizado Modificado ( _mndwi_ ): Optimizado para la

detección de cuerpos de agua superficiales. Relevante para el análisis de
inundaciones.
c) Variables Derivadas de Cartografía Geológica: Representan las propiedades del

material subyacente.

a. Grupos Geológicos: Cuatro capas ráster binarias ( _geo_Metamorfica,_

_geo_Sedimentaria, geo_Cuaternario, geo_Faena_ ) indicando la presencia (1)
o ausencia (0) de cada uno de los 4 grupos litológicos principales
reclasificados a partir del mapa geológico detallado. Permiten evaluar la
influencia del tipo general de material en la susceptibilidad.
b. Variables Derivadas de Cartografía Estructural e Hidrográfica (Proximidad):

Representan la influencia espacial de elementos lineales.

i. Distancia a Fallas ( _dist_fallas_ ): Distancia a la estructura geológica

(falla) mapeada más cercana. Proxy para zonas de potencial
debilidad/fracturamiento de la roca, relevante para remociones y
secundariamente para erosión.
ii. Distancia a Cauces ( _dist_cauces_ ): Distancia a la red hidrográfica

mapeada más cercana (líneas y polígonos). Factor clave para
evaluar la susceptibilidad a inundaciones fluviales y secundariamente
para remociones (socavación basal).

El subconjunto específico de estas variables utilizado para modelar cada peligro
(remociones en masa, inundaciones, erosión hídrica) fue seleccionado buscando incluir los
factores condicionantes más relevantes para dicho proceso, como se detalla implícitamente
en los análisis de resultados presentados en la Sección 5. Todas las variables
seleccionadas para cada modelo fueron estandarizadas antes de la aplicación del algoritmo
K-Means.

**2.2.3 Implementación del modelo**

La implementación del algoritmo de agrupamiento K-Means para la zonificación de
susceptibilidad se realizó íntegramente en el entorno de programación **R**, aprovechando las
capacidades del moderno framework de aprendizaje automático **mlr3** y su extensión
específica para tareas de clustering **mlr3cluster** . Este ecosistema proporciona una
estructura robusta, modular y orientada a objetos para el desarrollo y ejecución de flujos de
trabajo de machine learning.

El proceso de implementación siguió los pasos estándar dentro del paradigma mlr3:

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

1. Definición de la Tarea de Clustering: Para cada análisis de susceptibilidad

(remociones en masa, inundación, erosión), se definió una Tarea de Clustering
específica. Esta tarea encapsuló el conjunto de datos de entrada, que consistía en
los valores de las variables predictoras seleccionadas (Sección 2.2.2), previamente
extraídas para los puntos de muestreo aleatorio y estandarizadas (Z-score).
2. Selección y Configuración del Modelo: Se seleccionó el algoritmo K-Means como el

aprendiz (`Learner`) para el agrupamiento. Se configuraron los siguientes
hiperparámetros clave para controlar su ejecución:

a. _centers_ : Se estableció en `k=5`, indicando al algoritmo que buscara 5

clusters en los datos para cada análisis de peligro.
b. _nstart_ : Se fijó en 25, lo que instruye al algoritmo a ejecutarse 25 veces con

diferentes conjuntos de centroides iniciales aleatorios y seleccionar la mejor
solución (aquella con la menor suma de cuadrados intra-cluster), reduciendo
así el riesgo de converger a un óptimo local subóptimo.
c. _iter.max_ : Se estableció en 100, definiendo el número máximo de iteraciones

permitidas para que el algoritmo converja en cada ejecución.
3. Entrenamiento del Modelo: Una vez definida la tarea, se procedió al entrenamiento

del modelo K-Means. Este paso ejecutó el algoritmo sobre los datos escalados para
encontrar los centroides finales de los clusters y asignar cada punto de muestreo al
cluster más cercano.
4. Extracción de Resultados: La asignación final de cada punto de muestreo a uno de

los 5 clusters (resultado principal utilizado para la interpretación y mapeo) se extrajo
directamente del modelo entrenado.

**2.2.4 Determinación del número de clusters**

Para este estudio, se determinó utilizar un valor de k = 5 clusters para los análisis finales
de susceptibilidad presentados para cada uno de los peligros geomorfológicos (remociones
en masa, inundaciones y erosión hídrica). Esta decisión se basó en un balance entre la
información proporcionada por métodos exploratorios estándar y, fundamentalmente, la
capacidad de los clusters resultantes para representar condiciones geomorfológicas y
ambientales distintas y significativas dentro del área de estudio. Si bien, se pueden utilizar
métricas estadísticas como el método del codo (análisis de la reducción de la varianza intracluster al aumentar `k`) o el índice de silueta (medida de cuán bien separados están los
clusters) como guía inicial, la experiencia en aplicaciones geoespaciales indica que estas
métricas no siempre señalan un número óptimo único o directamente interpretable en
términos físicos.

Para llegar a esto, evaluaron soluciones con diferentes valores de `k` (incluyendo k=3,
discutido como alternativa para simplificación) y se seleccionó k=5 porque ofrecía el mejor
compromiso entre detalle y generalización. Específicamente, k=5 permitió:

1. Diferenciar condiciones de riesgo clave: Separar zonas con alta susceptibilidad

debida a factores distintos (ej. alta pendiente vs. baja cobertura vegetal vs. material
geológico débil vs. concentración de flujo). Una solución con menos clusters tendía
a agrupar estas condiciones distintas, dificultando la interpretación de las causas
raíz del riesgo en cada zona.
2. Identificar Zonas de Transición: Facilitar la aparición de clusters con características

intermedias, representando zonas de transición entre condiciones de muy baja y
muy alta susceptibilidad.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

3. Capturar la Influencia Antrópica: Permitir que las áreas significativamente alteradas

por la actividad minera (con perfiles de cobertura y humedad particulares)
emergieran como clusters diferenciados (ej. Cluster 3 en Inundaciones, parte de
Clusters 1 y 3 en Remociones).

Aunque la solución con k=5 resultó en algunos clusters con menor número de puntos
muestreados (representando condiciones más localizadas o específicas), se consideró que
mantener este nivel de detalle era valioso para una caracterización más completa de la
variabilidad espacial de la susceptibilidad en el área de la Faena Las Piedras,
proporcionando una base más rica para la posterior evaluación de riesgos y la definición de
medidas de mitigación específicas.

**2.2.5 Interpretación y asignación de niveles de susceptibilidad**

Una vez que el algoritmo K-Means asignó cada punto de muestreo (y por extensión, cada
píxel del área de estudio) a uno de los 5 clusters definidos, el siguiente paso correspondió
a interpretar el significado geomorfológico y ambiental de cada cluster para asignarle un
nivel de susceptibilidad cualitativo y ordenado frente al peligro específico analizado.

Este proceso de interpretación se basó en los siguientes pasos:

1. Análisis de Centroides: Para cada cluster identificado en cada modelo de peligro, se

calcularon los valores medios (centroides) de todas las variables predictoras
originales (no escaladas) utilizadas en dicho modelo. Esto permitió obtener un perfil
característico para cada cluster, resumiendo la combinación típica de condiciones
topográficas, de cobertura superficial, geológicas y de proximidad que representan
las áreas agrupadas en él.
2. Evaluación Experta Basada en Criterios: La asignación de un nivel de

susceptibilidad cualitativo (variando desde "Muy Baja" hasta "Muy Alta",
representada numéricamente de 1 a 5 en análisis posteriores) a cada cluster se
realizó mediante evaluación experta, basada en el conocimiento establecido sobre
los factores que controlan cada proceso geomorfológico:

 - Se analizó la combinación de las características promedio del cluster (ej.
pendiente media, NDVI medio, TWI medio, predominancia de grupo
geológico, distancia media a fallas/cauces).

 - Se evaluó cómo dicha combinación de factores favorece o dificulta la
ocurrencia del peligro específico. Por ejemplo, para remociones en masa,
clusters con alta pendiente media, baja cobertura vegetal (bajo NDVI/EVI,
alto BSI) y/o geología poco competente (Cuaternario, Faena) o cercanía a
fallas, fueron generalmente asociados a niveles de susceptibilidad más altos.
Para inundaciones, se consideraron claves la baja elevación, baja pendiente,
alto TWI/MNDWI y baja distancia a cauces. Para erosión, la alta pendiente,
baja cobertura y alto SPI fueron indicadores de alta susceptibilidad.

 - Se buscaron **contrastes significativos** entre los perfiles de los diferentes
clusters para establecer una jerarquía relativa de susceptibilidad dentro del
área de estudio.
3. Asignación de Nivel Cualitativo/Ordinal: A cada cluster se le asignó una etiqueta

descriptiva del nivel de susceptibilidad relativo (ej. "Alta", "Baja-Moderada", etc.) y
su correspondiente valor numérico ordinal (ej. 3, 2, etc.) para facilitar la
representación cartográfica y los análisis de riesgo posteriores.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

Los resultados detallados de esta interpretación y la descripción específica de las
características y nivel de susceptibilidad asignado a cada cluster para cada uno de los tres
peligros analizados (remociones en masa, inundaciones, erosión hídrica) se presentan en
la Sección 5 de este informe.

**2.3 METODOLOGÍA PARA LA EVALUACIÓN DE VULNERABILIDAD**

La evaluación de la vulnerabilidad, entendida como la susceptibilidad de los elementos
expuestos a sufrir daños o pérdidas ante la ocurrencia de un peligro, requiere un enfoque
adaptado a las distintas realidades presentes dentro del área de estudio. Dada la naturaleza
del proyecto minero y su interacción con el entorno rural circundante, se adoptó un enfoque
híbrido para caracterizar la vulnerabilidad, diferenciando entre las áreas externas a la
operación principal y el área interna de la faena.

**2.3.1 Enfoque híbrido**

Se reconoció que un único método de evaluación de vulnerabilidad sería insuficiente, ya
que los elementos expuestos y los factores que determinan su susceptibilidad al daño
varían significativamente entre el entorno rural y el sitio industrial minero. Por lo tanto, se
implementó un enfoque dual:

1. Vulnerabilidad Social (Externa a la Faena): Para las áreas ubicadas fuera del

perímetro operativo principal de la Faena Las Piedras, pero dentro del polígono de
alcance del estudio (incluyendo pequeñas localidades rurales o viviendas aisladas),
la vulnerabilidad se evaluó principalmente desde una perspectiva social y
demográfica. Se utilizaron indicadores derivados de datos del Censo de Población
y Vivienda 2017, agregados a nivel de localidad. Estos indicadores buscan reflejar
factores como la estructura etaria (dependencia demográfica), condiciones de la
vivienda (materialidad), acceso a servicios básicos (agua potable, saneamiento) y
características de grupos específicos (población indígena), los cuales influyen en la
capacidad de preparación, respuesta y recuperación de la población residente ante
un evento adverso. La metodología específica se detalla en la Sección 2.3.2.
2. Vulnerabilidad Operacional/Física (Interna a la Faena): Para el área _dentro_ del

perímetro operativo de la Faena Las Piedras, se constató (basado en información
del proyecto y Censo 2017) la ausencia de residentes permanentes. Por lo tanto, la
vulnerabilidad en esta zona se define principalmente por factores operacionales y
físicos:

a. Exposición Humana: Se consideró la presencia y distribución espacial de la

fuerza laboral durante los turnos operativos (aproximadamente 53 personas
en total, incluyendo trabajadores y chóferes) en las distintas áreas de trabajo
(oficinas, planta, talleres, frentes de extracción).
b. Vulnerabilidad de Infraestructura: Se evaluó la exposición y criticidad de las

instalaciones mineras clave (depósitos de lodos/agua, planta de procesos,
talleres, oficinas, estanques de combustible, bodegas de residuos
peligrosos, etc.) frente a los peligros analizados, considerando las
potenciales consecuencias operacionales, ambientales y de seguridad en
caso de daño o falla. La metodología para evaluar esta vulnerabilidad
interna, basada en indicadores espaciales derivados de planos de la faena y
criterios de criticidad/exposición, se describe en la Sección 2.3.3.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

Este enfoque híbrido permite obtener una caracterización de la vulnerabilidad más completa
y realista para el área de estudio, reconociendo las distintas naturalezas de los elementos
expuestos y los factores que determinan su fragilidad en el entorno rural versus el industrialminero. La integración de ambas evaluaciones genera el mapa de vulnerabilidad combinado
utilizado en la estimación final del riesgo (Sección 2.3.4).

**2.3.2 Vulnerabilidad social externa**

Para evaluar la vulnerabilidad de las comunidades y la población residente en las áreas
externas al perímetro operativo principal de la Faena Minera Las Piedras, pero dentro del
área de influencia definida por el polígono de alcance, se utilizó un enfoque basado en
indicadores socio-demográficos derivados del Censo de Población y Vivienda 2017.

La metodología específica comprendió los siguientes pasos:

1. Fuente de Datos: Se utilizaron datos censales a nivel de entidad censal, extraídos

de archivos GeoJSON pre-procesados correspondientes a las comunas de
Empedrado, Constitución y Chanco.
2. Unidad de Análisis: La información fue agregada espacial y estadísticamente al nivel

de “Localidad Censal” (identificada por el campo `NOMBRE_LOCALIDAD`),
considerándola como la unidad territorial representativa para el análisis de la
vulnerabilidad social en el entorno rural.
3. Procesamiento de Datos Censales: Se realizó un preprocesamiento exhaustivo de

los datos originales

a. Se cargaron y combinaron los archivos GeoJSON de las tres comunas.
b. Se limpiaron las columnas de atributos que contenían cuentas numéricas

(población por edad, tipos de vivienda, acceso a servicios, etc.), convirtiendo
valores textuales como "Indeterminado" a ‘NA’ y transformando las columnas
a formato numérico. Se asignó un valor de 0 a los `NA` resultantes en estas
columnas de conteo.
c. Se realizó una agregación espacial y estadística, agrupando los datos por

`NOMBRE_LOCALIDAD`. Se sumaron todas las cuentas numéricas
relevantes y se unieron las geometrías de las entidades censales
correspondientes a cada localidad.
4. Cálculo de Indicadores de Vulnerabilidad: Sobre la base de datos agregada por

localidad, se calcularon diversos indicadores porcentuales y ratios diseñados para
reflejar dimensiones clave de la vulnerabilidad social, tales como:

a. Dependencia Demográfica: Porcentaje de población menor de 15 años y

mayor de 65 años, e Índice de Dependencia total.
b. Condiciones de Vivienda: Porcentaje de viviendas con materialidad

irrecuperable y porcentaje de viviendas de tipo precario.
c. Acceso a Servicios Básicos: Porcentaje de viviendas sin conexión a la red

pública de agua potable.
d. Hacinamiento (Proxy): Número promedio de personas por hogar.
e. Grupos Específicos: Porcentaje de población perteneciente a pueblos

indígenas u originarios.
5. Recorte Espacial: Las geometrías resultantes de las localidades agregadas fueron

recortadas espacialmente utilizando el polígono de alcance para asegurar que el
análisis se centrara exclusivamente en el área de interés directo del estudio. Se
mantuvieron las estadísticas completas calculadas para cada localidad, incluso si
su geometría quedaba parcialmente cubierta.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

6. Clustering de Vulnerabilidad Social: Se aplicó el algoritmo K-Means (k=3) sobre un

conjunto seleccionado de los indicadores calculados para agrupar las localidades
externas en tres categorías con perfiles de vulnerabilidad social homogéneos (Baja,
Media, Alta), como se detalla en la Sección 5.1.

Este proceso permitió obtener una caracterización espacial de la vulnerabilidad social en el
entorno de la faena, basada en datos objetivos del censo y agregada a un nivel territorial
pertinente (localidad), la cual fue posteriormente integrada con la evaluación de
vulnerabilidad interna de la faena.

**2.3.3 Vulnerabilidad interna de la faena**

Dada la naturaleza industrial del área operativa principal de la Faena Minera Las Piedras y
la ausencia de población residente permanente, la evaluación de la vulnerabilidad dentro
de este perímetro se enfocó en la exposición del personal operativo y la susceptibilidad al
daño de la infraestructura física, utilizando un enfoque espacialmente explícito basado en
celdas de grilla.

La metodología implementada fue la siguiente:

1. Fuente de Datos Espaciales Internos: Se utilizó una capa vectorial detallada

derivada de planos de la faena, que contiene la ubicación y tipo de las distintas
instalaciones (depósitos, plantas, oficinas tipo contenedor, talleres tipo contenedor,
caminos, etc.).
2. Grilla de Análisis: Se utilizó la misma grilla ráster de referencia que en los análisis

de susceptibilidad (resolución ~3.88m, CRS EPSG:32718), asegurando la
alineación espacial para la posterior integración.
3. Cálculo de Indicadores de Vulnerabilidad por Celda: Se generaron las siguientes

capas ráster de indicadores, calculadas para cada celda _dentro_ del polígono del
footprint operativo de la faena (definido por el polígono "RCA"):

a. Exposición Humana Normalizada: Se estimó la distribución de la población

operacional (~53 personas) en las zonas de trabajo habitual (oficinas,
plantas, talleres, casino, frentes activos). Se asignó el número estimado de
personas a los polígonos correspondientes y se calculó la densidad (ej.
personas/hectárea). Este valor fue rasterizado y normalizado a una escala
0-1, donde 1 representa la máxima concentración estimada de personal.
b. Impacto/Criticidad de Infraestructura: Se asignó un índice de criticidad

ordinal (escala 1=Bajo a 5=Muy Alto/Crítico) a cada tipo de infraestructura
presente en la capa de layout, basado en las potenciales consecuencias
(operacionales, ambientales, de seguridad) de su falla (ej. Depósitos=5,
Planta=3, Oficinas=2, Caminos=1). Estos puntajes fueron rasterizados,
utilizando la función `max` para asignar el valor más crítico en caso de
superposición de elementos en una celda.
c. Densidad de Edificaciones (`densidad_edif`): Se identificaron los polígonos

correspondientes a edificaciones (oficinas, talleres, plantas, bodegas, etc.) y
se calculó el porcentaje de área cubierta por estas estructuras en cada celda
, resultando en un valor entre 0 y 1.
d. Dificultad de Acceso/Evacuación (`dif_acceso`): Se calculó la distancia

euclidiana desde cada celda a la red vial interna de la faena. Este valor se
combinó (mediante suma ponderada normalizada 0-1) con la pendiente del
terreno (`slope`) para obtener un índice donde valores más altos indican

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

mayor dificultad de acceso o evacuación (mayor distancia a caminos y/o
mayor pendiente).
4. Stack de Indicadores Internos: Las capas ráster resultantes para cada indicador se

combinaron en un stack multi-capa, representando la distribución espacial de
diferentes facetas de la vulnerabilidad operacional y física dentro de la faena.

Estos indicadores rasterizados específicos para la faena fueron luego integrados con los
indicadores de vulnerabilidad social externa (descritos en 2.3.2) para generar el mapa de
vulnerabilidad combinado final (descrito en 2.3.4).

**2.3.4 Generación del mapa de vulnerabilidad combinado**

Para obtener una representación espacialmente continua de la vulnerabilidad en toda el
área de estudio, integrando las evaluaciones diferenciadas realizadas para el entorno
externo y el área operativa interna de la faena, se procedió a combinar ambas fuentes de
información mediante las siguientes etapas:

1. Rasterización de la Vulnerabilidad Social Externa: Los indicadores de vulnerabilidad

social calculados para cada localidad externa (Sección 2.3.2), o el nivel de
vulnerabilidad cualitativo/ordinal asignado a cada una (ej. Baja=1, Media=2, Alta=3),
fueron transferidos a una capa ráster utilizando la grilla de referencia del proyecto
(definida por el MDE base y sus derivados). Cada píxel perteneciente a una
determinada localidad recibió el valor del indicador o nivel de vulnerabilidad
correspondiente a esa localidad. Los píxeles fuera de las áreas de localidad
definidas (o dentro del footprint de la faena) quedaron inicialmente con valor `NA`.
2. Preparación de la Vulnerabilidad Interna: Se utilizaron los mapas ráster que

representan la vulnerabilidad operacional/física _dentro_ del polígono de la faena
minera (calculados como se describe en la Sección 2.3.3), asegurando que
estuvieran alineados a la misma grilla de referencia y con valores en la escala
numérica definida (ej. 1, 2, 3).
3. Fusión Espacial con Prioridad Interna: En este paso se fusionaron los rásters de

vulnerabilidad interna y externa. Esta función opera "superponiendo" el ráster de
vulnerabilidad interna sobre el ráster de vulnerabilidad externa. El resultado es un

nuevo ráster combinado donde:

a. Los píxeles dentro del polígono de la faena minera retienen los valores

específicos de vulnerabilidad operacional/física calculados para esa área.
b. Los píxeles fuera del polígono de la faena toman los valores de

vulnerabilidad social correspondientes a la localidad en la que se ubican.
4. Mapa de Vulnerabilidad Combinado Final: El producto de esta fusión es un único

mapa ráster (Mapa 6) que representa la distribución espacial de la vulnerabilidad
(en la escala numérica definida, ej. 1 a 3 o 4) en toda el área de estudio, respetando
las diferentes fuentes de datos y metodologías aplicadas dentro y fuera del
perímetro operativo de la faena. Este mapa constituye el insumo clave de
vulnerabilidad para el cálculo final del riesgo (Sección 2.4).

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**2.3.5 Asignación de niveles de vulnerabilidad**

Para facilitar la integración de los análisis de susceptibilidad y vulnerabilidad en la
estimación final del riesgo, y para permitir una interpretación clara de los resultados, se
asignó un nivel de vulnerabilidad cualitativo y ordinal (Baja, Media, Alta) a cada unidad
espacial (localidad externa o celda ráster interna) basado en los resultados de las
evaluaciones descritas en las secciones anteriores (2.3.2 y 2.3.3). Se utilizó una escala
numérica correspondiente (1=Baja, 2=Media, 3=Alta) para los cálculos posteriores en la
matriz de riesgo.

El proceso de asignación se realizó de forma diferenciada:

1. Para la Vulnerabilidad Social Externa (Localidades):

 - Se utilizó la interpretación de los clusters (k=3) resultantes del análisis de los
indicadores censales (Sección 2.3.2).

 - A cada cluster se le asignó un nivel cualitativo basado en el perfil de
vulnerabilidad predominante de las localidades que agrupaba. Según el
análisis realizado:

`o` Cluster 1 (principalmente falta de agua): Asignado a Vulnerabilidad

Media (2).
`o` Cluster 2 (falta de agua + dependencia demográfica): Asignado a

Vulnerabilidad Alta (3).
`o` Cluster 3 (falta de agua + vivienda precaria): Asignado a

Vulnerabilidad Alta (3).

 - Este nivel asignado fue posteriormente rasterizado para representar la
vulnerabilidad social en las áreas fuera de la faena.
2. Para la Vulnerabilidad Operacional/Física Interna (Faena):

 - Se utilizaron los rásters específicos de vulnerabilidad proporcionados para
la faena, los cuales ya contenían una clasificación intrínseca con valores 0.3,
0.6 y 1.0.

 - Estos valores fueron reclasificados directamente a la escala numérica ordinal

común:

`o` Valor original 0.3 -> Nivel 1 (Baja)
`o` Valor original 0.6 -> Nivel 2 (Media)
`o` Valor original 1.0 -> Nivel 3 (Alta)

 - Esta reclasificación se aplicó al ráster específico correspondiente a cada
peligro antes de la combinación final (ej., se usó `vuln_talud.tif` reclasificado
para la vulnerabilidad combinada en el análisis de riesgo de remociones).

Este proceso de asignación aseguró que tanto la vulnerabilidad social externa como la
vulnerabilidad operacional/física interna estuvieran representadas en una escala ordinal
común (1 a 3), permitiendo su integración coherente en el mapa de vulnerabilidad
combinado (Mapa 6) y su posterior utilización en la matriz para la estimación del riesgo
(Sección 6).

**2.4 METODOLOGÍA PARA ESTIMACIÓN DEL RIESGO**

La estimación del riesgo geológico y geomorfológico se basa en la premisa fundamental de
que el Riesgo es una función tanto de la probabilidad o propensión de ocurrencia de un
evento peligroso (Peligro, evaluado a través de la Susceptibilidad) como de las

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

consecuencias adversas que dicho evento podría generar sobre los elementos expuestos
(Vulnerabilidad).

**2.4.1 Combinación de la susceptibilidad con la vulnerabilidad**

Para integrar espacialmente la información de susceptibilidad y vulnerabilidad, se empleó
un enfoque basado en matriz de riesgo. Este método combina las clasificaciones ordinales
de susceptibilidad y vulnerabilidad obtenidas en los pasos anteriores para asignar un nivel
de riesgo resultante a cada unidad espacial (píxel) del área de estudio.

El proceso específico fue el siguiente:

1. Entradas Requeridas: Para cada peligro analizado (remociones en masa,

inundaciones, erosión hídrica), se utilizaron como entrada dos capas ráster
alineadas espacialmente:

 - Ráster de Susceptibilidad Reclasificado: El mapa resultante del clustering KMeans (Sección 4), reclasificado a una escala numérica ordinal que
representa los niveles de susceptibilidad (ej. 1=Baja, 2=Media, 3=Alta).

 - Ráster de Vulnerabilidad Combinado y Reclasificado: El mapa de
vulnerabilidad híbrido (Sección 5.3 y Mapa 6), que integra la vulnerabilidad
social externa y la vulnerabilidad operacional/física interna, también
reclasificado a la misma escala numérica ordinal (ej. 1=Baja, 2=Media,
3=Alta). Se utilizó el mapa de vulnerabilidad específico para cada peligro.
2. Definición de la Matriz de Riesgo: Se estableció una matriz de combinación (3x3 en

este caso, dado que la vulnerabilidad y susceptibilidad se clasificaron en 3 niveles
principales) que define el nivel de Riesgo resultante para cada posible combinación
de los niveles de entrada. La matriz utilizada asigna un nivel de riesgo ordinal
(1=Bajo, 2=Medio, 3=Alto, 4=Muy Alto) de la siguiente manera:

**TABLA 1: MATRIZ DE RIESGO**

3. Aplicación Espacial (Álgebra de Mapas): La lógica de la matriz de riesgo se aplicó

píxel a píxel a las capas ráster de susceptibilidad y vulnerabilidad mediante
funciones de álgebra de mapas implementadas en el paquete `terra` de R. Para
cada píxel, se tomaron sus valores correspondientes de susceptibilidad y
vulnerabilidad numérica, se utilizaron como índices para consultar la matriz de
riesgo, y se asignó el valor de riesgo resultante a ese píxel en el mapa de salida.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

4. Salida - Mapas de Riesgo: El resultado de este proceso es un conjunto de mapas

ráster finales (uno para cada peligro: remociones en masa, inundación, erosión
hídrica), donde el valor de cada píxel representa el nivel de riesgo estimado (1 a 4),
integrando la propensión espacial del peligro con la fragilidad/exposición de los
elementos presentes. Estos mapas se presentan y analizan en la Sección 6.

**2.4.2 Matriz de riesgo utilizada**

La estimación del nivel de riesgo en cada unidad espacial (píxel) se realizó mediante la
aplicación de una matriz de riesgo predefinida. Esta matriz combina los niveles ordinales
de Susceptibilidad (S) y Vulnerabilidad (V) para determinar un nivel de Riesgo (R)
resultante.

Las capas de entrada para la matriz fueron los rásters reclasificados de:

 - Susceptibilidad (S): Valores 1 (Baja/Muy Baja), 2 (Media/Baja-Moderada), 3 (Alta).

 - Vulnerabilidad (V): Valores 1 (Baja), 2 (Media), 3 (Alta).

**Definición de los Niveles de Riesgo Resultantes**

Los valores numéricos (1 a 4) obtenidos de la aplicación de esta matriz se interpretan
cualitativamente como los siguientes niveles de riesgo:

 - Nivel 1: Riesgo Bajo: Indica condiciones donde tanto la susceptibilidad al peligro
como la vulnerabilidad de los elementos expuestos son bajas. Requiere monitoreo
estándar.

 - Nivel 2: Riesgo Medio: Representa situaciones donde la susceptibilidad o la
vulnerabilidad son medias, pero no ambas altas simultáneamente, o donde una
susceptibilidad baja coincide con una vulnerabilidad media. Requiere monitoreo
periódico y posibles medidas preventivas.

 - Nivel 3: Riesgo Alto: Ocurre cuando la susceptibilidad es alta y la vulnerabilidad es
al menos baja, o cuando la susceptibilidad es media y la vulnerabilidad es media, o
cuando la susceptibilidad es baja pero la vulnerabilidad es alta. Indica una
combinación significativa que requiere atención prioritaria, medidas de control
específicas y monitoreo frecuente.

 - Nivel 4: Riesgo Muy Alto / Crítico: Representa las condiciones más desfavorables,
donde la susceptibilidad es media o alta y la vulnerabilidad también es media o alta.
Estas zonas demandan la máxima atención, medidas de mitigación robustas y/o
urgentes, monitoreo intensivo y planes de contingencia específicos.

Esta matriz proporciona un marco consistente y sistemático para traducir las evaluaciones
espaciales de susceptibilidad y vulnerabilidad en un mapa final de nivel de riesgo para cada
peligro analizado.

**2.4.3 Generación de mapas de riesgo por peligro**

El paso final de la estimación del riesgo consistió en la aplicación espacial de la matriz de
riesgo definida (Sección 2.4.2) para generar mapas que representan la distribución del nivel
de riesgo para cada uno de los peligros geomorfológicos analizados.

Este proceso se realizó de la siguiente manera:

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

1. Cálculo por Peligro: La estimación del riesgo se llevó a cabo de forma independiente

para cada uno de los tres peligros: remociones en masa, inundaciones
(locales/pluviales) y erosión hídrica.
2. Combinación Espacial (Álgebra de Mapas): Para cada peligro, se realizó una

operación espacial píxel a píxel utilizando funciones del paquete `terra` en R. En
cada píxel del área de estudio:

 - Se obtuvo el valor numérico del nivel de Susceptibilidad (1, 2 o 3) a partir del
ráster reclasificado correspondiente a ese peligro.

 - Se obtuvo el valor numérico del nivel de Vulnerabilidad (1, 2 o 3) a partir del
ráster de vulnerabilidad unificado relevante para ese peligro

 - Estos dos valores (Susceptibilidad y Vulnerabilidad) se utilizaron como
índices para consultar la Matriz de Riesgo definida (Sección 2.4.2).

 - El valor de Riesgo correspondiente (1, 2, 3 o 4) obtenido de la matriz fue
asignado al píxel en el mapa de riesgo de salida para ese peligro.
3. Generación de Mapas de Riesgo Finales: Como resultado de este proceso, se

generaron tres mapas ráster de riesgo distintos:

 - Mapa de Riesgo por Remociones en Masa (Mapa 7).

 - Mapa de Riesgo por Inundaciones (Mapa 8).

 - Mapa de Riesgo por Erosión Hídrica (Mapa 9).

 - Cada uno de estos mapas presenta la distribución espacial de los niveles de
riesgo (1=Bajo, 2=Medio, 3=Alto, 4=Muy Alto) para su respectivo peligro en
toda el área de estudio.
4. Exportación y Visualización: Los mapas de riesgo resultantes fueron exportados en

formato GeoTIFF para su posterior análisis, visualización (utilizando una paleta de
colores ordenada e intuitiva, como se discutió) e integración con otras capas de
información en un Sistema de Información Geográfica (SIG).

Estos mapas finales de riesgo constituyen el producto principal de la evaluación,
identificando las áreas prioritarias para la implementación de medidas de control y
monitoreo, como se detalla en la Sección 6.

**2.5 ARQUITECTURA DEL FLUJO DE TRABAJO Y HERRAMIENTAS IMPLEMENTADAS**

**2.5.1 Arquitectura del flujo de trabajo**

El proceso metodológico utilizado para la evaluación de susceptibilidad, vulnerabilidad y
riesgo se esquematiza en el diagrama de flujo presentado en la Figura X. Este diagrama
ilustra la secuencia lógica de las operaciones, desde la adquisición y preprocesamiento de
los datos espaciales base, pasando por la derivación de variables predictoras (topográficas,
satelitales, geológicas, de proximidad), la alineación espacial y el ensamblaje de estas
variables en stacks multi-capa, hasta la aplicación del clustering no supervisado (K-Means),
la interpretación de resultados, la evaluación de vulnerabilidad híbrida y el cálculo final de
los mapas de riesgo por peligro.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 2: DIAGRAMA DE FLUJO**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**2.5.2 Tecnologías y herramientas R implementadas**

El procesamiento de datos, análisis espacial, implementación de modelos de clustering y
generación de resultados se realizó utilizando el lenguaje de programación R y un conjunto
de paquetes especializados de código abierto, las cuales son:

 - Procesamiento Geoespacial:

`o` `sf`: Paquete fundamental para la lectura, escritura, manipulación

(transformación de CRS, operaciones geométricas, validación) y análisis de
datos vectoriales (Shapefiles, GeoJSON, GeoPackages conteniendo
polígonos de área de estudio, geología, hidrografía, fallas, localidades,
infraestructura).
`o` `terra`: Paquete moderno y eficiente para la lectura, escritura, manipulación

y análisis de datos ráster (MDE, índices satelitales, derivados topográficos,
distancias, resultados de clustering y riesgo). Se utilizó extensivamente para
álgebra de mapas, alineación espacial, cálculo de distancias y rasterización.
`o` `elevatr`: Utilizado para la descarga programática del Modelo Digital de

Elevación (MDE) base (USGS).

 - Interfaz a Software Externo:

`o` `whitebox`: Interfaz en R para ejecutar funciones de la suite WhiteboxTools.

Se utilizó para el cálculo de derivados topográficos avanzados como el Índice
Topográfico de Humedad (TWI), el Índice de Potencia Fluvial (SPI) y
curvaturas, aprovechando algoritmos optimizados implementados en
WhiteboxTools.

 - Manipulación de Datos:

`o` `dplyr`: Utilizado para la manipulación eficiente y legible de data frames y

tablas de atributos de objetos `sf`.
`o` `data.table`: Requerido por el ecosistema `mlr3` para el manejo eficiente de

los datos de entrada a los modelos de machine learning.
`o` `stringr`, `tidyr`: Paquetes auxiliares para manipulación de texto (ej. limpieza

de nombres de unidades geológicas) y datos.

 - Aprendizaje Automático (Machine Learning):

`o` `mlr3`: Framework principal para la definición y ejecución de las tareas de

aprendizaje automático.
`o` `mlr3cluster`: Extensión de `mlr3` que proporciona los objetos y métodos

específicos para realizar el clustering K-Means.

 - Software GIS Complementario:

`o` QGIS: Utilizado para la preparación inicial de algunas capas vectoriales (ej.

digitalización del layout de la faena), la verificación visual interactiva de
resultados intermedios y la producción de cartografía final para el informe.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**3.** **CARACTERIZACIÓN DEL CONJUNTO DE DATOS**

**3.1 FUENTES DE DATOS UTILIZADAS**

El presente análisis de susceptibilidad geomorfológica se sustenta en la integración de
datos espaciales base, datos complementarios de terreno y gabinete, y variables derivadas
específicamente para alimentar los modelos de aprendizaje no supervisado. Las fuentes se
detallan a continuación:

**3.1.1 Datos espaciales base**

Estos datos constituyeron la base fundamental para la derivación de las variables
predictoras espaciales utilizadas en los modelos de susceptibilidad:

 - Modelo Digital de Elevación (MDE): Se utilizó el producto USGS 3DEP (Programa
de Elevación 3D del Servicio Geológico de Estados Unidos), con una resolución
espacial nativa de aproximadamente 3.88 metros por píxel en esta zona.

 - Imágenes Satelitales: Se emplearon datos multiespectrales pre-procesados (Nivel
2A - corrección atmosférica) correspondientes a una imagen del satélite Sentinel-2,
adquirida el 27 de febrero de 2024. Se utilizaron las bandas espectrales relevantes
(Azul-B02, Verde-B03, Rojo-B04, Infrarrojo Cercano-NIR B08, SWIR1-B11)
proporcionadas como archivos GeoTIFF locales.

 - Cartografía Vectorial: Se recopilaron las siguientes capas en formato Shapefile:

`o` Geología: El cual contiene las unidades geológicas superficiales mapeadas

en el área y el campo de atributo `Unidad` [Fuente: Adaptado de
Sernageomin / Mapeo interno].
`o` Hidrografía: Archivos que representan por un lado cuerpos de agua o ríos

anchos como polígonos o la red de drenaje como líneas, describiendo los
cauces permanentes e intermitentes [Fuente: IGM].
`o` Estructuras: Representan las fallas geológicas y otras estructuras lineales

mapeadas en la zona de interés [Fuente: Interno / SERNAGEOMIN].
`o` Límite Área de Estudio: Define el polígono específico para el cual se realizó

el análisis de susceptibilidad y riesgo.
`o` Datos Socio-Demográficos (Censo 2017): Se emplearon datos del Censo de

Población y Vivienda 2017, procesados a nivel de localidad (como se detalla
en la Sección 2.3.2), específicamente para la evaluación de la vulnerabilidad
social en las áreas externas a la faena minera.

Estos datos base fueron posteriormente procesados y transformados para generar las
variables derivadas utilizadas en los modelos, como se detalla en las secciones siguientes.

**3.1.2 Datos primarios y secundarios contextuales**

Además de los datos espaciales base utilizados para generar las variables predictoras, se
recopiló y revisó información primaria y secundaria que proporcionó un contexto para
comprender las condiciones del sitio, interpretar los resultados de los modelos de
susceptibilidad y facilitar la futura validación de los mismos. Estas fuentes incluyen:

 - Investigaciones Geofísicas: Se utilizó información proveniente de 9 Sondeos
Eléctricos Verticales (SEV) distribuidos en el área para inferir la estratigrafía del

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

subsuelo, así como datos de gravimetría regional para el contexto geológico
general.

 - Datos Hidrogeológicos: Se consideraron los registros históricos del monitoreo
piezométrico de la faena (ej. 10 piezómetros, período 2015-2023) para comprender
el comportamiento del agua subterránea en el sitio.

 - Información de Sismicidad: Se revisaron catálogos de sismicidad regional (19852023) y, fundamentalmente, los resultados del "Estudio de Amenaza Sísmica y
Espectro de Sitio" (SIRVE, 2017), que proporciona los parámetros sísmicos de
diseño (ej. PGA) para diferentes períodos de retorno, relevantes para evaluar la
estabilidad bajo condiciones sísmicas.

Si bien estos datos contextuales son cruciales para una comprensión integral del sitio y la
validación de los modelos, es importante reiterar que no fueron incorporados directamente
como variables predictoras espaciales en los análisis de clustering K-Means utilizados para
generar los mapas de susceptibilidad presentados en este informe (Sección 5), los cuales
se basaron en las variables derivadas descritas en la Sección 3.

**3.2 PREPROCESAMIENTO Y DERIVACIÓN DE VARIABLES**

**3.2.1 Armonización espacial y preprocesamiento base**

Se procedió a realizar las siguientes tareas:

 - Estandarización del Sistema de Coordenadas (CRS): Todas las capas espaciales,
tanto vectoriales (geología, hidrografía, fallas, límite de área, layout faena, datos
censales GeoJSON) como ráster (MDE), fueron sistemáticamente transformadas o
verificadas para asegurar el uso del CRS proyectado definido para el proyecto:
(EPSG:32718).

 - Alineación de Capas Ráster: Se definió una grilla ráster de referencia basada en el
MDE procesado (recortado al área de estudio), con una resolución espacial de 3.88
metros. Todas las capas ráster (incluyendo las derivadas en pasos posteriores)
fueron rigurosamente alineadas a esta grilla mediante una combinación de
funciones del paquete `terra`, incluyendo el resampleo (utilizando interpolación por
vecino más cercano), corte para ajuste dimensional y enmascaramiento para aplicar
la máscara del área de estudio

 - Limpieza de Datos Censales/Tabulares: Los atributos de los archivos GeoJSON del
Censo 2017 que contenían información numérica (población, viviendas) pero
estaban almacenados como texto, fueron procesados para: (a) identificar y tratar
valores no numéricos como "Indeterminado" (convirtiéndolos a `NA`), (b)
transformar las columnas a formato numérico, y (c) reemplazar los `NA` resultantes
(originados por "Indeterminado" o fallas en la conversión) por ceros, bajo el supuesto
de que representan ausencia o no reporte de la característica para las cuentas
agregadas.

 - Recorte Espacial (Vulnerabilidad Externa): Para el análisis de vulnerabilidad social,
las geometrías de las localidades (previamente agregadas desde los datos
censales) fueron espacialmente intersectadas con el polígono del área de alcance
del estudio, manteniendo únicamente las porciones de las localidades que caen
dentro del área de interés directo.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**3.2.2 Variables predictoras derivadas**

A partir de los datos espaciales base y mediante los procesos descritos en la sección
anterior (3.2.1), se generó un conjunto final de variables predictoras rasterizadas y
alineadas espacialmente. Estas variables, seleccionadas por su relevancia teórica y
práctica para influir en los procesos de remociones en masa, inundaciones y/o erosión
hídrica, fueron utilizadas como entrada para los modelos de clustering K-Means. El listado
completo de las variables derivadas consideradas en los análisis se encuentra en la sección
2.2.2

Cabe notar que, si bien esta lista representa el conjunto completo de predictores generados
y considerados, el subconjunto específico de variables utilizado como entrada para cada
modelo de susceptibilidad individual (remociones, inundación, erosión) fue seleccionado en
función de la relevancia conceptual de cada variable para el proceso modelado, como se
refleja implícitamente en los resultados presentados en la Sección 5.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**4.** **RESULTADOS DEL ANÁLISIS DE SUSCEPTIBILIDAD**

Mediante la aplicación de la metodología de aprendizaje no supervisado (clustering KMeans) descrita en la Sección 4, se generaron zonificaciones espaciales que clasifican el
área de estudio según su susceptibilidad relativa a los principales procesos
geomorfológicos identificados: remociones en masa, inundaciones (fluvial local y pluvial) y
erosión hídrica. A continuación, se presentan los resultados para cada peligro.

**4.1 ZONIFICACIÓN DE SUSCEPTIBILIDAD A REMOCIONES EN MASA**

El análisis, que integró variables topográficas (pendiente, curvaturas, TWI), índices
satelitales (NDVI, NDWI, BSI, EVI), proximidad a fallas y 4 categorías geológicas
principales, identificó 5 clusters o zonas con diferentes perfiles de susceptibilidad (Figura
3). La interpretación de estos clusters es la siguiente:

Cluster 3 (Alta Susceptibilidad - por Cobertura Pobre/Proximidad a Fallas en Sedimentario):

[~12% del área muestreada] Presenta pendientes suaves (~7.4°) sobre roca sedimentaria,
pero también con cobertura vegetal deficiente, alta humedad superficial y muy cercano a
fallas mapeadas (distancia media ~521m). La combinación de estos factores genera una
alta susceptibilidad. Su extensión es limitada.

Cluster 1 (Alta Susceptibilidad - por Cobertura Pobre/Humedad en Metamórfico): [~21% del
área muestreada] Caracterizado por pendientes moderadas (~8.1°) sobre roca
metamórfica, pero con cobertura vegetal muy deficiente (NDVI/EVI bajos, BSI alto) y alta
firma de humedad superficial (NDWI alto). Aunque la roca es competente y está lejos de
fallas, la falta de protección superficial lo hace altamente propenso a erosión severa y
deslizamientos superficiales. Cubre áreas significativas dentro y alrededor de la faena.

Cluster 2 (Moderada-Alta Susceptibilidad - por Material No Consolidado): [~6% del área
muestreada] Agrupa zonas con pendientes suaves (~7.6°) desarrolladas exclusivamente
sobre depósitos Cuaternarios no consolidados (Hf), y relativamente cercanas a fallas
(~605m). La debilidad intrínseca de estos materiales define el nivel de susceptibilidad, a
pesar de la pendiente moderada y la vegetación intermedia. Su extensión es limitada.

Cluster 5 (Baja-Moderada Susceptibilidad - por Pendiente Alta Mitigada): [~31% del área
muestreada] Corresponde a las laderas naturales más empinadas (~13.5°) sobre roca
metamórfica competente y lejos de fallas. Sin embargo, la excelente cobertura vegetal
(NDVI/EVI altos, BSI bajo) mitiga fuertemente el riesgo superficial actual. El riesgo potencial
es alto, pero el riesgo efectivo actual es menor que en C1 o C3.

Cluster 4 (Baja Susceptibilidad): [~29% del área muestreada] Representa las condiciones
más estables sobre roca sedimentaria: pendientes moderadas (~10.9°), buena cobertura
vegetal, humedad baja y distancia moderada a fallas.

Implicaciones para la Faena: La zonificación revela que una parte significativa del área
operativa de la Faena Las Piedras y sus caminos/plataformas asociadas (unidad geológica
'Faena', incluida principalmente en los Clusters 1 y 3) presenta una Alta susceptibilidad a
remociones en masa superficiales y procesos erosivos severos, debido fundamentalmente
a la alteración y/o eliminación de la cobertura vegetal protectora. Esto demanda un manejo
riguroso del agua superficial, controles de erosión continuos y un diseño geotécnico
cuidadoso de todos los taludes artificiales.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

Adicionalmente, la faena debe considerar los riesgos provenientes de zonas adyacentes:

 - Las laderas naturales muy empinadas (Cluster 5) requieren preservación absoluta
de su cobertura vegetal para mantener su estabilidad actual y evitar que se
conviertan en fuentes de deslizamientos mayores.

 - Las áreas con depósitos Cuaternarios (Cluster 2), aunque de extensión limitada,
representan zonas de debilidad intrínseca donde la fundación de cualquier
estructura o la creación de taludes requiere estudios geotécnicos específicos y
diseños conservadores.

 - Las zonas identificadas con alta susceptibilidad cercanas a fallas (Cluster 3)
ameritan una evaluación estructural detallada para descartar problemas asociados
a fracturamiento incrementado.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 3: MAPA DE SUSCEPTIBILIDAD DE REMOCIONES EN MASA**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**4.2 ZONIFICACIÓN DE SUSCEPTIBILIDAD A INUNDACIONES (FLUVIAL LOCAL /**

**PLUVIAL)**

El análisis (k=5), integrando elevación, pendiente, TWI, curvaturas, índices satelitales
(NDVI, NDWI, MNDWI, BSI), distancia a cauces y geología agrupada, generó la siguiente
zonificación (Figura 4):

Cluster 3 (Baja Externa / Mod-Alta Interna): [~29% del área muestreada] Identifica
claramente el área de la faena y zonas alteradas circundantes. Se ubica en cotas altas
(~391m) y lejos de cauces mapeados (~232m), protegiéndola de inundaciones fluviales
externas. Sin embargo, su baja cobertura vegetal (NDVI bajo, BSI alto) y alta firma de
humedad/agua superficial (NDWI/MNDWI altos) la hacen altamente susceptible a la
generación de escorrentía rápida y encharcamiento/saturación interna por lluvias (riesgo
pluvial y operacional).

Cluster 2 (Moderada por Proximidad): [~4% del área muestreada] Agrupa las zonas de
menor cota media (~248m), aunque sobre laderas empinadas (~15.7°) y roca metamórfica.
Su riesgo deriva principalmente de la posibilidad de ser alcanzadas por crecidas externas,
aunque su distancia media a los cauces mapeados resultó inesperadamente alta (~253m),
lo que requiere verificación del modelo o de la red hidrográfica.

Cluster 5 (Moderada por Proximidad): [~6% del área muestreada] También en cotas bajas
(~258m), sobre roca sedimentaria y con pendientes moderadas (~12.3°). Presenta la menor
distancia media a cauces (~171m) entre los clusters principales, reforzando su
susceptibilidad por proximidad a crecidas locales.

Cluster 1 (Baja Susceptibilidad): [~29% del área muestreada] Zonas de cota intermedia
(~289m), bien vegetadas, sobre roca sedimentaria y a distancia moderada de cauces
(~181m). Bajo riesgo general.

Cluster 4 (Muy Baja Susceptibilidad): [~33% del área muestreada] Las zonas más altas
(~401m) y con pendiente, bien drenadas, bien vegetadas, sobre roca metamórfica y
relativamente alejadas de cauces (~154m).

Implicaciones para la Faena: El análisis de susceptibilidad a inundaciones es crucial para
la gestión hídrica y de riesgos dentro de la faena:

 - Riesgo Interno Dominante: El resultado más significativo es que el área operativa
principal (Cluster 3), presenta una alta susceptibilidad intrínseca a problemas de
manejo de aguas lluvias (pluvial). Esto exige un diseño y mantenimiento riguroso del
sistema de drenaje superficial interno (canales, cunetas, piscinas de decantación)
para evacuar eficientemente la alta escorrentía generada por las superficies
alteradas y prevenir encharcamientos o flujos no controlados que puedan afectar
instalaciones o la estabilidad de taludes.

 - Riesgo Externo Localizado: Las zonas de la faena que se extiendan hacia las cotas
más bajas o que colinden con las áreas clasificadas como Cluster 2 o Cluster 5
(Moderada por Proximidad) deben ser evaluadas específicamente frente a los
niveles de crecida estimados para los esteros y quebradas locales con periodos de
retorno adecuados (ej. 100 años). Es necesario asegurar que las obras de
protección o la cota de emplazamiento de instalaciones críticas en estas zonas sean
suficientes.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

 - Descargas Controladas: Las aguas manejadas dentro de la faena (Cluster 3) deben
ser descargadas de forma controlada para no exacerbar riesgos de erosión o
inundación en las zonas receptoras aguas abajo.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 4: MAPA DE SUSCEPTIBILIDAD DE INUNDACIONES**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**4.3 ZONIFICACIÓN DE SUSCEPTIBILIDAD A EROSIÓN HÍDRICA**

Este análisis (k=5), utilizando pendiente, TWI, curvatura planiforme, SPI, índices de
cobertura (NDVI, EVI, BSI) y geología agrupada, diferenció las siguientes zonas (Figura 5):

Cluster 3 (Alta Susceptibilidad - por Cobertura Pobre): [~30% del área muestreada] Zonas
extensas con pendiente moderada (~7.5°) pero cobertura vegetal muy deficiente (NDVI
bajo, BSI alto, EVI bajo), sobre geología mixta (Metamórfica/Sedimentaria). Principalmente
áreas intervenidas o degradadas propensas a erosión laminar y en surcos.

Cluster 4 (Alta Susceptibilidad - por Flujo Concentrado): [~2% del área muestreada] Zonas
localizadas con formas convergentes, TWI alto y SPI extremadamente alto, indicando alta
energía erosiva en cauces y cárcavas. Requieren obras de protección específicas.

Cluster 1 (Alta Susceptibilidad - Localizada en Faena): [~0.5% del área muestreada] Puntos
muy específicos dentro de la unidad 'Faena' con cobertura vegetal nula y BSI alto. Riesgo
superficial extremo localizado.

Cluster 2 (Baja-Moderada Susceptibilidad): [~32% del área muestreada] Laderas con
pendiente relativamente alta (~13.5°) pero excelente cobertura vegetal sobre roca
metamórfica. El riesgo potencial por pendiente está bien mitigado.

Cluster 5 (Baja Susceptibilidad): [~35% del área muestreada] Laderas con pendiente
moderada (~10.4°), buena cobertura vegetal sobre roca sedimentaria. Condición más
estable y extendida.

Implicaciones para la Faena: Este análisis resalta dos problemáticas principales de erosión
para la Faena Las Piedras:

 Erosión Superficial Generalizada en Áreas Intervenidas: Una parte muy significativa
del área operativa y sus alrededores inmediatos (Cluster 3 y Cluster 1) presenta Alta
susceptibilidad a la erosión laminar y en surcos debido a la remoción o degradación
de la cobertura vegetal. Esto exige la implementación prioritaria y continua de
medidas de control de erosión superficial (manejo de aguas lluvias, cobertura
temporal, revegetación progresiva) en plataformas, caminos y taludes expuestos
dentro de la faena.

 - Riesgo de Erosión Concentrada en Cauces: Las zonas identificadas con muy alta
energía de flujo (Cluster 4), que pueden corresponder a los cauces naturales que
reciben drenaje o a cárcavas formadas, requieren medidas específicas de
estabilización (ej. check dams, revestimientos) para prevenir su incisión y el
transporte de los sedimentos generados aguas arriba (particularmente desde las
zonas del Cluster 3). Es crucial asegurar que las descargas de agua de la faena no
incrementen la energía erosiva en estos puntos.

La gestión efectiva de la erosión en la faena deberá, por tanto, abordar tanto la protección
de las superficies expuestas como la estabilización de las vías de flujo concentrado.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 5: MAPA DE SUSCEPTIBILIDAD DE EROSIÓN**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**4.4 TABLA RESUMEN DE SUSCEPTIBILIDAD POR CLUSTER Y PELIGRO**

La siguiente tabla resume los niveles de susceptibilidad relativa asignados a los cinco
clusters identificados en cada uno de los análisis independientes realizados para
remociones en masa, inundaciones y erosión hídrica. Se incluyen también las
características más determinantes que definen el perfil de cada cluster para cada peligro
específico.

Es importante notar que el número de cluster (1-5) se refiere al resultado del algoritmo KMeans para cada análisis por separado. Aunque puede haber solapamiento espacial, un
cluster con el mismo número puede representar combinaciones de variables y, por lo tanto,
niveles de susceptibilidad diferentes dependiendo del peligro que se esté evaluando.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**TABLA 2: SIGNIFICADO DE CLUSTERS**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**5.** **EVALUACIÓN DE LA VULNERABILIDAD**

**5.1 VULNERABILIDAD SOCIAL DEL ENTORNO**

La vulnerabilidad social de las áreas pobladas o con presencia residencial ubicadas fuera
del perímetro operativo principal de la Faena Las Piedras, pero dentro del área de alcance
del estudio, se evaluó utilizando datos del Censo de Población y Vivienda 2017. La
información, proveniente de archivos GeoJSON para las comunas de Empedrado,
Constitución y Chanco, fue agregada a nivel de Localidad Censal. Se calcularon indicadores
porcentuales representativos de diferentes dimensiones de la vulnerabilidad, incluyendo
dependencia demográfica (población menor de 15 y mayor de 65 años), condiciones de la
vivienda (materialidad irrecuperable), acceso a servicios básicos (agua potable por red
pública), hacinamiento (proxy: personas por hogar) y pertenencia a pueblos indígenas.
Posteriormente, se aplicó un algoritmo de clustering K-Means (con k=3) sobre un conjunto
seleccionado de estos indicadores para agrupar las localidades con perfiles de
vulnerabilidad similares (ver Sección 2.3.2 para detalles metodológicos). El análisis se
aplicó a las 9 localidades con datos válidos que intersectan el polígono de alcance.

**Interpretación de Clusters de Vulnerabilidad Social:**

El análisis K-Means diferenció tres grupos principales de localidades en el entorno de la
faena, según su perfil de vulnerabilidad social:

 - Cluster 1 (Vulnerabilidad Media): Compuesto por 5 localidades (Colmenares, El
Litre, Indeterminada_a, Pueblecillo, San Pedro) pertenecientes a la comuna de
Empedrado. Estas áreas se caracterizan por una ausencia total de conexión a la red
pública de agua potable (100% sin agua de red), lo que constituye su principal factor
de vulnerabilidad en términos de servicios básicos. Sin embargo, presentan
indicadores favorables en otras dimensiones: muy baja o nula dependencia
demográfica (según los datos procesados), ausencia de viviendas con materialidad
irrecuperable, y bajo nivel de hacinamiento promedio (1.5-3.0 personas/hogar).

 - Cluster 2 (Vulnerabilidad Alta): Agrupa 3 localidades (La Gloria [Chanco], San José

[Chanco], San Pedro [Constitución]). Comparte con el Cluster 1 la carencia total de
agua potable por red (100%), pero se distingue por una dependencia demográfica
significativamente mayor (índice de dependencia entre 20% y 49%), indicando una
proporción más alta de niños y/o adultos mayores respecto a la población en edad
de trabajar. La materialidad de la vivienda es relativamente buena (% irrecuperable
bajo, 2-6%) y el hacinamiento es moderado (2.7-3.4 personas/hogar). La
vulnerabilidad aquí está definida por la combinación de falta de servicios y una
estructura demográfica más dependiente.

 - Cluster 3 (Vulnerabilidad Alta): Incluye 1 localidad (Indeterminada_b [Empedrado]).
Similar al Cluster 1 en cuanto a baja dependencia demográfica y bajo hacinamiento,
y comparte la falta total de agua de red (100%). Sin embargo, se diferencia
claramente por presentar el mayor porcentaje de viviendas con materialidad
irrecuperable (7.7%) entre todos los grupos. Su vulnerabilidad está marcada por la
combinación de falta de servicios básicos y precariedad habitacional.

En resumen, si bien la densidad poblacional en el entorno inmediato es baja, todas las
localidades analizadas presentan una vulnerabilidad significativa por la falta de acceso a

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

agua potable de red. Los clusters permiten diferenciar además aquellas con mayor carga
demográfica (Cluster 2) o mayor precariedad habitacional (Cluster 3) como las de mayor
vulnerabilidad social relativa dentro del área de estudio externa a la faena.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 6: MAPA DE VULNERABILIDAD SOCIAL**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**5.1 VULNERABILIDAD OPERACIONAL/FÍSICA**

Utilizando la metodología descrita en la sección, se muestran a continuación los mapas
correspondientes a las vulnerabilidades dentro de la faena de cada uno de los peligros
estudiados

**FIGURA 7: MAPA DE** **VULNERABILIDAD** **DENTRO DE LA FAENA**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**5.2 MAPA DE VULNERABILIDAD COMBINADO**

Estos mapas de vulnerabilidad combinada constituyen el insumo final de vulnerabilidad que
se integra con los mapas de susceptibilidad para la estimación del riesgo detallada en la
Sección 6.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 8: MAPA DE VULNERABILIDAD DE REMOCIONES EN MASA**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 9: MAPA DE VULNERABILIDAD DE INUNDACIONES**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 10: MAPA DE VULNERABILIDAD DE EROSIÓN**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**6.** **ESTIMACIÓN DEL RIESGO GEOLÓGICO Y GEOMORFOLÓGICO**

Habiendo caracterizado espacialmente la susceptibilidad a los peligros geomorfológicos
(Sección 5) y la vulnerabilidad de los elementos expuestos (Sección 6), el paso final
consiste en integrar ambos componentes para obtener una estimación del nivel de riesgo
en el área de estudio. El riesgo, en este contexto, representa la probabilidad de
consecuencias adversas, considerando tanto la propensión del sitio a un evento peligroso
como la fragilidad o valor de lo que podría ser afectado.

**6.1 RIESGO POR REMOCIONES EN MASA**

El mapa de riesgo por remociones en masa (Mapa 7) se generó combinando espacialmente
el mapa de susceptibilidad a remociones en masa (Mapa 1, basado en clustering con DEM,
satélite, geología agrupada y distancia a fallas) con el mapa de vulnerabilidad unificado
relevante para este peligro (Mapa 6 - Remociones, que integra vulnerabilidad social externa
y vulnerabilidad específica a taludes/remociones dentro de la faena). La combinación se
realizó aplicando la matriz de riesgo definida en la Sección 2.4.2, resultando en una
clasificación del área de estudio en cuatro niveles de riesgo: Bajo (1), Medio (2), Alto (3) y
Muy Alto (4).

La distribución espacial del riesgo por remociones en masa muestra los siguientes patrones
principales:

 - Nivel 4 (Riesgo Muy Alto): Estas zonas representan la combinación más crítica de
alta propensión a la inestabilidad y alta vulnerabilidad de los elementos expuestos.
Se localizan principalmente donde:

`o` La Susceptibilidad es Alta (S=3), correspondiente a áreas con cobertura

vegetal pobre/suelo desnudo (Clusters 1 y 3 de susceptibilidad) o sobre
material Cuaternario débil cerca de fallas (Cluster 2), Y coincide con zonas
de Vulnerabilidad Media o Alta (V=2 o V=3) (ej. infraestructura crítica, zonas
de alta concentración de personal dentro de la faena, o localidades externas
con alta vulnerabilidad social).
`o` La Susceptibilidad es Media (S=2), correspondiente a laderas con pendiente

alta pero buena cobertura (Cluster 5), Y coincide con zonas de
Vulnerabilidad Alta (V=3) (ej. depósitos o instalaciones críticas de la faena
ubicadas directamente bajo estas laderas, o localidades externas muy
vulnerables). Estas áreas requieren la máxima prioridad en términos de
monitoreo y medidas de mitigación.

 - Nivel 3 (Riesgo Alto): Esta categoría es predominante en gran parte del área
intervenida por la faena minera. Resulta de combinaciones como:

`o` Alta Susceptibilidad (S=3) (Clusters 1 y 3: mala cobertura; Cluster 2:

Cuaternario) en zonas con Baja Vulnerabilidad (V=1) (ej. áreas generales de
la faena con baja criticidad o exposición humana según `vuln_talud.tif`).
`o` Media Susceptibilidad (S=2) (Cluster 5: pendiente alta bien vegetada) en

zonas con Media Vulnerabilidad (V=2) (ej. áreas operativas generales,
talleres, o localidades externas con vulnerabilidad media).
`o` Baja Susceptibilidad (S=1) (Cluster 4: laderas estables sedimentarias) en

zonas con Alta Vulnerabilidad (V=3) (ej. instalaciones críticas o localidades
muy vulnerables ubicadas sobre terreno estable). La extensión de este nivel
dentro de la faena subraya la importancia de los controles operacionales y

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

geotécnicos continuos, dado que la susceptibilidad es elevada debido a la
alteración superficial, incluso si la vulnerabilidad específica del elemento no
es la máxima.

 - Nivel 2 (Riesgo Medio): Representa condiciones intermedias, resultantes de
(S=Media x V=Baja) o (S=Baja x V=Media). Se localiza típicamente en:

`o` Laderas naturales de pendiente alta pero bien vegetadas (S=2, Cluster 5)

que se encuentran en áreas de baja vulnerabilidad (V=1).
`o` Zonas muy estables (S=1, Cluster 4) pero que coinciden con áreas de

vulnerabilidad media (V=2), como algunas localidades externas o zonas
operativas menos críticas. Requiere monitoreo y mantenimiento preventivo.

 - Nivel 1 (Riesgo Bajo): Indica la combinación de Baja Susceptibilidad (S=1) y Baja
Vulnerabilidad (V=1). Corresponde a las áreas más estables (laderas suaves a
moderadas, bien vegetadas, sobre roca competente) donde además no existen
elementos vulnerables significativos. Su extensión en el mapa final debe ser
verificada, pero probablemente sea limitada dada la distribución de la vulnerabilidad.

En síntesis, el mapa de riesgo por remociones en masa resalta el área operativa de la faena
como la zona de mayor preocupación general (predominio de Riesgo Alto), debido a la alta
susceptibilidad inducida por la alteración superficial. Adicionalmente, identifica puntos o
zonas específicas de Riesgo Muy Alto donde esta alta susceptibilidad (o la presencia de
materiales débiles/pendientes altas) coincide con elementos de alta vulnerabilidad. Este
mapa es una herramienta clave para enfocar las medidas de mitigación geotécnica, los
programas de revegetación, el monitoreo instrumental y los planes de respuesta a
emergencias detallados en la Sección 7.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 11: MAPA DE RIESGO DE REMOCIONES EN MASA**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**6.2 RIESGO POR INUNDACIONES**

El mapa de riesgo por inundaciones (Mapa 8) se obtuvo mediante la combinación espacial
del mapa de susceptibilidad a inundaciones locales/pluviales (Mapa 2) y el mapa de
vulnerabilidad unificado relevante (Mapa 6 - Inundación), aplicando la matriz de riesgo
definida (Sección 2.4.2). El mapa resultante clasifica el área de estudio en niveles de riesgo
Bajo (1), Medio (2), Alto (3) y Muy Alto (4), reflejando la interacción entre la propensión a la
acumulación de agua o alcance por crecidas y la vulnerabilidad de los elementos presentes.

La distribución espacial del riesgo por inundaciones revela lo siguiente:

 - Nivel 4 (Riesgo Muy Alto): Estas zonas representan la condición más crítica.
Resultan de la combinación de Susceptibilidad Media (S=2) con Vulnerabilidad Alta
(V=3), o de Susceptibilidad Alta (S=3) con Vulnerabilidad Media (V=2) o Alta (V=3).

`o` Ubicación Probable: Se esperarían en (a) sectores dentro del área operativa

de la faena (S=3) que coincidan con infraestructura de alta criticidad o alta
concentración de personal (V=3 o V=2) y/o (b) las zonas externas de menor
cota y proximidad a cauces (S=2) que además presenten alta vulnerabilidad
social (V=3) (localidades de Cluster Social 2 o 3). Estas áreas requieren
máxima atención en diseño de drenajes, protección directa y planes de
evacuación.

 - Nivel 3 (Riesgo Alto): Esta categoría cubre áreas significativas, incluyendo
probablemente gran parte del área operativa de la faena. Resulta de combinaciones
como (S=Alta x V=Baja), (S=Media x V=Media) o (S=Baja x V=Alta).

`o` Ubicación Probable: Principalmente en (a) el área de la faena (S=3) donde

la vulnerabilidad interna específica para inundación es Baja o Media (V=1 o
V=2); o (b) las zonas externas de menor cota (S=2) que coinciden con áreas
de Vulnerabilidad Media (V=2) (localidades Cluster Social 1); o (c) zonas
altas y estables (S=1) que, sin embargo, están cerca o contienen localidades
de Alta Vulnerabilidad social (V=3) (Clusters Sociales 2 o 3). El riesgo dentro
de la faena se debe a la alta susceptibilidad interna a problemas hídricos,
mientras que en el exterior se debe a la vulnerabilidad de las comunidades
en zonas estables o a una combinación moderada de S y V en zonas bajas.

 - Nivel 2 (Riesgo Medio): Representa un riesgo tolerable que requiere seguimiento.
Resulta de (S=Media x V=Baja) o (S=Baja x V=Media).

`o` Ubicación Probable: Zonas de menor cota y proximidad relativa a cauces

(S=2) que coinciden con áreas de Baja Vulnerabilidad (V=1); o zonas altas y
bien drenadas (S=1) que coinciden con áreas de Vulnerabilidad Media (V=2)
(como localidades externas del Cluster Social 1).

 - Nivel 1 (Riesgo Bajo): Es la condición más favorable, resultado de Baja
Susceptibilidad (S=1) x Baja Vulnerabilidad (V=1).

`o` Ubicación Probable: Zonas altas, con pendiente, bien vegetadas y alejadas

de cauces (S=1), donde además la vulnerabilidad (social o física) es mínima
(V=1).

En resumen, el mapa de riesgo por inundación destaca la importancia de la gestión hídrica
interna dentro de la faena (área con S=3 y predominio de R=3 o 4) para controlar la
escorrentía y el encharcamiento. Adicionalmente, señala un riesgo moderado a alto en las
zonas de menor cota (S=2), cuya criticidad final dependerá de la vulnerabilidad específica
de los elementos (residencias o infraestructura de faena) ubicados allí y del alcance real de

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

las crecidas locales. Las medidas de mitigación deben enfocarse en el control del agua
dentro de la faena y la protección o restricción de uso en las áreas bajas más vulnerables.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 12: MAPA DE RIESGO DE INUNDACIONES**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**6.3 RIESGO POR EROSIÓN HÍDRICA**

El mapa de riesgo por erosión hídrica (Mapa 9) se generó mediante la combinación espacial
del mapa de susceptibilidad a la erosión (Mapa 3, basado en clustering con DEM, satélite
incluyendo SPI y geología agrupada) y el mapa de vulnerabilidad unificado relevante (Mapa
6 - Erosión), utilizando la matriz de riesgo definida (Sección 2.4.2). Es importante destacar
que, según los resultados obtenidos, el nivel de Riesgo Bajo (1) no se presenta en el área
de estudio, indicando que todas las zonas poseen al menos un nivel de riesgo medio debido
a la combinación de susceptibilidad y vulnerabilidad presentes. Los niveles de riesgo
observados (Medio=2, Alto=3, Muy Alto=4) se interpretan de la siguiente manera:

 - Nivel 4 (Riesgo Muy Alto): Representa las condiciones más críticas para la erosión
y sus consecuencias. Resulta de la combinación de Susceptibilidad Alta (S=3) con
Vulnerabilidad Media (V=2) o Alta (V=3); o de Susceptibilidad Media (S=2) con
Vulnerabilidad Alta (V=3).

`o` Ubicación e interpretación:_ Se espera encontrar estas zonas donde: (a) Las

áreas con muy alta energía de flujo concentrado (S=3, Cluster 4 Erosión)
coinciden con zonas de vulnerabilidad Media o Alta (infraestructura crítica
cercana, áreas operativas de faena con V=2 o V=3, o localidades externas
vulnerables); y/o (b) Áreas extensas con cobertura vegetal muy pobre (S=3,
Cluster 3 Erosión) que además presentan Vulnerabilidad Media o Alta. Estas
son las áreas de máxima prioridad para medidas de control de erosión y
estabilización.

 - Nivel 3 (Riesgo Alto): Esta es la categoría predominante en gran parte del área
intervenida por la faena minera. Resulta principalmente de la combinación de Alta
Susceptibilidad (S=3) con Vulnerabilidad Media (V=2).

`o` Ubicación e interpretación: Corresponde mayoritariamente a las áreas

operativas y degradadas (Cluster 3 Erosión: baja cobertura) que se
encuentran dentro de zonas clasificadas con Vulnerabilidad Media (V=2).
También puede incluir, en menor medida, zonas de Media Susceptibilidad
(S=2) (laderas empinadas bien vegetadas) con Media Vulnerabilidad (V=2),
o zonas de Baja Susceptibilidad (S=1) con Alta Vulnerabilidad (V=3)
(localidades externas vulnerables sobre terreno estable).

 - Nivel 2 (Riesgo Medio): Representa un riesgo tolerable que requiere seguimiento.
Dado que V=1 (Baja Vulnerabilidad) parece estar ausente o no solaparse con S=1
(Baja Susceptibilidad), este nivel resulta principalmente de la combinación de Baja
Susceptibilidad (S=1) x Media Vulnerabilidad (V=2).

`o` Ubicación e Interpretación: Corresponde a las zonas intrínsecamente más

estables frente a la erosión (Cluster 5 Erosión: pendiente moderada, buena
cobertura, sobre Sedimentario) pero que se encuentran en un contexto de
Vulnerabilidad Media.

En conclusión, el análisis de riesgo por erosión hídrica subraya la criticidad de las áreas
intervenidas por la faena (predominantemente Riesgo Alto) como principal fuente potencial
de pérdida de suelo y generación de sedimentos. Identifica también puntos específicos de
muy alto riesgo asociados a la concentración de flujo y zonas donde la vulnerabilidad (media
o alta) eleva el riesgo incluso en áreas de baja o media susceptibilidad intrínseca. Las
medidas de mitigación deben enfocarse prioritariamente en las zonas de Riesgo Alto y Muy
Alto, abordando tanto el control de la escorrentía superficial y la revegetación en áreas
degradadas, como la estabilización de cauces y zonas de flujo concentrado.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**FIGURA 13: MAPA DE RIESGO DE EROSIÓN**

**Fuente: Elaboración propia**

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**6.4 CONSIDERACIONES SOBRE RIESGO SÍSMICO**

Si bien la Región del Maule y el emplazamiento de la Faena Las Piedras se encuentran en
una zona de alta actividad sísmica, es importante aclarar el alcance del presente estudio
respecto a este peligro específico.

La metodología de evaluación de susceptibilidad basada en clustering K-Means sobre
variables topográficas y de superficie (Sección 2.2) no es adecuada para caracterizar
directamente la susceptibilidad del terreno a los efectos primarios de un sismo, como son
la amplificación de las ondas sísmicas en el suelo o el potencial de licuefacción. Estos
fenómenos están fundamentalmente controlados por las propiedades dinámicas del
subsuelo (tipo de suelo/roca, espesor de estratos, velocidad de onda de corte Vs30, nivel
freático) y la geometría profunda, variables que no fueron incorporadas directamente como
predictores en los modelos de clustering espacial desarrollados en este trabajo.

Por lo tanto, no se generó un mapa de Riesgo Sísmico (entendido como Susceptibilidad a
la Amplificación x Vulnerabilidad) comparable en metodología a los presentados para
remociones en masa, inundaciones y erosión.

La evaluación del riesgo sísmico para la Faena Las Piedras debe basarse en los resultados
de estudios específicos de ingeniería y geociencias, destacando:

 - Estudio de Amenaza Sísmica y Espectro de Sitio (SIRVE, 2017): Este estudio,
referenciado en los antecedentes del proyecto, proporciona los parámetros sísmicos
de diseño relevantes para el emplazamiento, incluyendo las aceleraciones máximas
del suelo (PGA) esperadas para diferentes períodos de retorno (ej., 0.34g para T=72
años, 0.79g para T=475 años, 1.46g para T=2475 años ). Estos parámetros son los
que deben utilizarse para el diseño estructural y la verificación de la estabilidad
pseudoestática de todas las instalaciones críticas de la faena.

 - Evaluación de Vulnerabilidad Sísmica de Infraestructura: Si bien no se calculó un
riesgo SxV, sí se generó un mapa ráster específico (`vuln_sismo.tif`) que estima la
vulnerabilidad relativa de la infraestructura _existente_ dentro de la faena ante un
evento sísmico, basándose en el tipo de construcción (ej. edificios modulares y
plantas industriales como más vulnerables que depósitos de lodos bien construidos
o caminos). Este mapa de vulnerabilidad debe ser considerado en conjunto con los
resultados del estudio de amenaza sísmica para identificar los elementos que
podrían sufrir mayores daños ante la ocurrencia del sismo de diseño.

 - Análisis de Riesgos Sísmicos Inducidos:

`o` Remociones en Masa: El mapa de Riesgo por Remociones en Masa (Mapa

7) presentado en la Sección 6.2 considera implícitamente los sismos como
un factor desencadenante principal. Las zonas identificadas con Riesgo Alto
o Muy Alto en ese mapa son aquellas donde es más probable que un sismo
genere inestabilidad de laderas, afectando potencialmente a los elementos
vulnerables allí ubicados.

La evaluación detallada del riesgo sísmico directo para la Faena Las Piedras debe integrar
los resultados del estudio especializado de amenaza sísmica (SIRVE 2017) y la evaluación
de la vulnerabilidad sísmica de la infraestructura aquí presentada. Los mapas de riesgo por
remociones en masa e inundación de este informe ayudan a identificar los peligros
secundarios inducidos por sismos.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**7.** **MEDIDAS DE MITIGACIÓN**

**7.1 MEDIDAS DE MITIGACIÓN POR ZONA DE RIESGO**

Las siguientes medidas de control y mitigación se definen en función de los niveles de riesgo
identificados en los Mapas 9, 10 y 11, priorizando las acciones en las zonas de mayor riesgo
y abordando las causas subyacentes identificadas en los análisis de susceptibilidad y
vulnerabilidad. Estas medidas complementan los diseños de ingeniería específicos
desarrollados para las instalaciones mineras individuales.

**7.1.1 Control de remociones en masa**

Las acciones para controlar el riesgo por remociones en masa se enfocarán según el nivel
de riesgo mapeado (1=Bajo, 2=Medio, 3=Alto, 4=Muy Alto):

 - Zonas de Riesgo Muy Alto (Nivel 4):

`o` Medidas Prioritarias:

 - Investigación Geotécnica Detallada: Realizar estudios específicos
(calicatas, sondajes, ensayos) en estas zonas si se planea o existe
infraestructura crítica, enfocándose en las características de los
materiales Cuaternarios (Cluster 2) o el grado de
fracturamiento/meteorización cerca de fallas (Cluster 3).

 - Estabilización Activa: Considerar e implementar, según diseño de
ingeniería, medidas como reperfilado de taludes, construcción de
bermas, instalación de sistemas de drenaje subsuperficial, muros de
contención, anclajes o soil nailing en puntos críticos.

 - Protección Superficial Intensiva: Para áreas con mala cobertura
(Clusters 1 y 3), aplicar revegetación agresiva con especies de rápido
anclaje, combinada con geomallas o hidromantas de alta resistencia.

 - Monitoreo Intensivo: Instalar instrumentación geotécnica avanzada
(inclinómetros, extensómetros, piezómetros de lectura frecuente)
para detectar movimientos precursores. Implementar vigilancia
topográfica de alta frecuencia.

 - Zonas de Riesgo Alto (Nivel 3):

`o` Medidas Específicas:

 - Control Riguroso de Aguas Superficiales: Diseño, construcción y
mantenimiento exhaustivo de sistemas de drenaje (cunetas, canales,
bajadas de agua) para evitar la infiltración y la erosión concentrada
que puedan desestabilizar taludes, especialmente en zonas de
Clusters 1 y 3.

 - Revegetación Progresiva y Control de Erosión: Implementar
sistemáticamente la revegetación en todos los taludes y superficies
perturbadas inactivas correspondientes a Clusters 1 y 3. Usar
controles temporales (hidrosiembra, mantas) en áreas activas
expuestas por períodos prolongados.

 - Diseño Geotécnico Adecuado: Asegurar que todos los taludes
artificiales (cortes, rellenos, depósitos) se diseñen con factores de
seguridad apropiados para condiciones estáticas y pseudoestáticas
(considerando PGA de SIRVE 2017), prestando especial atención a

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

los emplazados sobre material Cuaternario (Cluster 2) o cerca de
fallas (Cluster 3).

 - Monitoreo Geotécnico Estándar: Mantener red de control topográfico
(monolitos) y piezométrico (si aplica) con frecuencia regular.

 - Inspecciones Geotécnicas Periódicas: Realizar inspecciones
visuales detalladas por personal calificado, enfocándose en detectar
signos de inestabilidad (grietas, abultamientos, humedad anómala),
especialmente en las zonas correspondientes a los clusters de mayor
susceptibilidad (C1, C2, C3, C5).

 - Zonas de Riesgo Medio (Nivel 2):

`o` Medidas Preventivas y Monitoreo:

 - Preservación de Cobertura Vegetal: Mantener y proteger la
vegetación existente en las laderas naturales estables (Clusters 4 y
5).

 - Mantenimiento de Drenajes: Asegurar la funcionalidad de los
sistemas de drenaje superficial estándar.

 - Inspecciones Visuales Regulares: Incluir estas zonas en las rondas
de inspección periódica, buscando cambios o signos incipientes de
problemas.

**7.1.2 Control de inundaciones**

Las medidas para controlar y mitigar el riesgo por inundaciones locales (fluviales/pluviales)
se enfocarán en las zonas identificadas en el Mapa 8, abordando tanto la gestión del agua
generada internamente en la faena como la protección frente a potenciales crecidas
externas en las zonas más bajas. Las acciones se priorizarán según el nivel de riesgo
(1=Bajo, 2=Medio, 3=Alto, 4=Muy Alto):

 - Zonas de Riesgo Muy Alto (Nivel 4):

`o` Medidas Prioritarias:

 - Infraestructura Crítica en Faena (S=3, V=2/3): Realizar inspecciones
detalladas y mantenimiento preventivo riguroso de los sistemas de
drenaje superficial (canales, cunetas, sumideros, piscinas de
sedimentación) en las áreas operativas de alta vulnerabilidad (ej.
cerca de depósitos, planta, talleres) para asegurar su máxima
capacidad hidráulica ante lluvias intensas. Considerar sistemas de
bombeo de emergencia redundantes.

 - Zonas Externas Bajas con Alta Vulnerabilidad (S=2, V=3): Realizar
(o referenciar si existe) estudios hidrológicos/hidráulicos detallados
para determinar las cotas de inundación asociadas a crecidas de
periodos de retorno relevantes (ej. 50-100 años) en los
esteros/quebradas cercanas a estas zonas. Si la vulnerabilidad
corresponde a viviendas o comunidades externas, evaluar la
necesidad de sistemas de alerta temprana comunitarios o defensas
fluviales (en coordinación con autoridades). Si corresponde a
infraestructura de la faena en estas zonas bajas, evaluar su
protección directa (pretiles) o reubicación.

 - Zonas de Riesgo Alto (Nivel 3):

`o` Medidas Específicas:

 - Gestión Integral de Aguas Lluvias en Faena: Diseño, implementación
y mantenimiento sistemático y frecuente de toda la red de drenaje

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

interna para manejar eficientemente la alta escorrentía generada por
las superficies alteradas/impermeables. Incluir limpieza regular de
canales, verificación de capacidad de alcantarillas y correcto
funcionamiento de piscinas de sedimentación/regulación.

 - Control Operacional: Minimizar áreas de acumulación de agua no
planificadas. Establecer protocolos claros para el manejo de aguas
durante eventos de lluvia intensa, incluyendo la operación de bombas
y posibles descargas controladas.

 - Protección de Elementos Vulnerables en Zonas Estables: Si el
Riesgo Alto se debe a elementos de Alta Vulnerabilidad (V=3)
ubicados en zonas de Baja Susceptibilidad (S=1), asegurar que
dichos elementos estén adecuadamente protegidos contra la
escorrentía superficial local o efectos indirectos.

 - Zonas de Riesgo Medio (Nivel 2):

`o` Medidas Preventivas y Monitoreo:

 - Mantenimiento Estándar de Drenajes: Asegurar la limpieza y
funcionalidad de los sistemas de drenaje existentes en estas áreas.

 - Vigilancia de Cauces Cercanos: Inspeccionar periódicamente los
cauces próximos a las zonas S=2 para detectar obstrucciones o
cambios que puedan aumentar el riesgo de desborde.

 - Monitoreo Meteorológico: Utilizar pronósticos de lluvia intensa para
activar inspecciones preventivas o pre-alerta en estas zonas.

 - Verificar Revancha: Asegurar que cualquier depósito o piscina
ubicada en estas zonas mantenga la revancha hidráulica de diseño.

**7.1.3 Control de erosión hídrica**

Las medidas para controlar la erosión hídrica y el transporte de sedimentos se enfocarán
en las zonas identificadas en el Mapa 9, abordando tanto las áreas fuente de erosión
superficial como las vías de flujo concentrado, según el nivel de riesgo (Medio=2, Alto=3,
Muy Alto=4). Se constata la ausencia de zonas clasificadas como de Riesgo Bajo (1) en el
área de estudio para este peligro.

 - Zonas de Riesgo Muy Alto (Nivel 4):

`o` Medidas Prioritarias

 - Estabilización de Cauces/Cárcavas (si S=3 por Cluster 4): En las
zonas identificadas con muy alta energía de flujo (alto SPI),
implementar de forma prioritaria obras de control de erosión
concentrada como check dams (pequeños diques transversales) de
roca, gaviones o materiales geosintéticos, revestimiento de cauces
con enrocado o bioingeniería (ej. fajinas, mantas orgánicas
reforzadas), especialmente si se ubican aguas arriba de
infraestructura crítica o puntos de descarga.

 - Protección Intensiva de Superficies Expuestas (si S=3 por Cluster 1
o 3): En áreas con cobertura nula o muy pobre que coinciden con alta
vulnerabilidad, aplicar inmediatamente cubiertas protectoras
robustas (ej. geomallas de control de erosión, mantas orgánicas
gruesas, mulch aplicado con tackifier) combinado con revegetación
agresiva (hidrosiembra con mezcla de especies nativas y pioneras de
rápido establecimiento).

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

 - Control de Sedimentos en Origen: Instalar barreras de sedimentos
reforzadas (ej. silt fences dobles, barreras de roca) inmediatamente
aguas abajo de estas zonas críticas para capturar el material
erosionado antes de que se movilice.

 - Zonas de Riesgo Alto (Nivel 3):

`o` Medidas Específicas:

 - Programa de Revegetación Sistemática y Progresiva: Es la medida
fundamental a mediano y largo plazo para las áreas extensas con
cobertura pobre (Cluster 3) que dominan este nivel de riesgo.
Implementar la revegetación en todas las áreas perturbadas tan
pronto como dejen de estar operativamente activas.

 - Manejo Riguroso de Escorrentía Superficial: Asegurar que toda la red
de drenaje (cunetas de caminos, canales de contorno de plataformas,
etc.) en estas zonas esté correctamente diseñada, construida y
mantenida limpia y funcional para conducir el agua sin causar erosión
adicional. Incluir disipadores de energía en puntos de descarga.

 - Controles Superficiales Temporales: En áreas activas o donde la
revegetación tarda en establecerse, utilizar medidas como riego
controlado para compactación superficial, aplicación de supresores
de polvo con agentes ligantes, o instalación de bermas temporales
de contorno o micro-terrazas.

 - Protección de Elementos Vulnerables: Si el riesgo alto se debe a V=3
sobre S=1, asegurar que la escorrentía proveniente de las zonas de
alta susceptibilidad no impacte directamente estos elementos
vulnerables (ej. mediante canales de desviación).

 - Zonas de Riesgo Medio (Nivel 2):

`o` Medidas Preventivas y Monitoreo:

 - Mantenimiento de Cobertura y Drenajes: Preservar la buena
cobertura vegetal existente y asegurar el mantenimiento estándar de
los sistemas de drenaje superficiales.

 - Control de Sedimentos Estándar: Aplicar prácticas habituales de
control de sedimentos (barreras simples, piscinas de decantación)
durante cualquier actividad constructiva o de movimiento de tierras
realizada en estas zonas o aguas arriba de ellas.

 - Inspecciones Regulares: Incluir estas áreas en las inspecciones
periódicas para detectar signos tempranos de erosión incipiente
(pequeños surcos) y actuar correctivamente antes de que se

agraven.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**8.** **CONCLUSIONES Y RECOMENDACIONES**

**8.1 CONCLUSIONES PRINCIPALES**

La presente evaluación integral de los riesgos asociados a la Faena Minera Las Piedras y
su entorno inmediato, se ha basado en una metodología que combina información detallada
del sitio con técnicas de análisis espacial y aprendizaje automático no supervisado
(Clustering K-Means). Las principales conclusiones son:

1. Metodología Efectiva para Zonificación de Susceptibilidad: El enfoque metodológico

implementado, basado en clustering K-Means sobre un conjunto integrado de
variables geoespaciales, demostró ser efectivo para identificar y delimitar
espacialmente zonas con características homogéneas y susceptibilidad relativa
diferenciada a los peligros analizados dentro del área de estudio.
2. Identificación de Factores Clave de Susceptibilidad: Los análisis permitieron

identificar los factores dominantes que controlan la susceptibilidad a cada proceso
en esta área específica:

a. Remociones en Masa: La susceptibilidad Alta está fuertemente asociada a

la alteración de la superficie y falta de cobertura vegetal (bajo NDVI/EVI, alto
BSI) en pendientes moderadas (Cluster 1 y 3, incluyendo área de faena), y
secundariamente a la presencia de materiales geológicos no consolidados
(Cuaternario) cerca de fallas (Cluster 2). La proximidad a fallas (<600m)
caracteriza a los clusters de mayor susceptibilidad por material débil o
cobertura pobre (C2, C3). Las pendientes naturales muy altas (Cluster 5)
tienen un riesgo potencial significativo, aunque actualmente mitigado por la
buena cobertura vegetal existente.
b. Inundaciones (Locales/Pluviales): El riesgo principal dentro del área

operativa (Cluster 3) está ligado a la alta generación de escorrentía y
potencial de encharcamiento/saturación interna debido a la baja
cobertura/alta BSI y alta firma de humedad (NDWI/MNDWI), más que a
inundaciones externas dada su elevación. Las zonas de menor cota absoluta
(Clusters 2 y 5) presentan una susceptibilidad moderada por proximidad
potencial a crecidas de cauces locales, aunque la variable `dist_cauces` no
fue un fuerte diferenciador en el modelo final.
c. Erosión Hídrica: La susceptibilidad Alta se asocia principalmente a áreas con

cobertura vegetal pobre en pendientes moderadas (Cluster 3, generando
erosión laminar/surcos) y a zonas de flujo concentrado con alta energía
(Cluster 4, TWI/SPI altos, riesgo de cárcavas). Las áreas bien vegetadas,
incluso en pendientes fuertes, muestran menor susceptibilidad actual.
3. Impacto Significativo de la Faena: Los resultados confirman que las áreas

intervenidas por la Faena Minera Las Piedras (unidad 'Han' y zonas asociadas a
baja cobertura/alto BSI) presentan una elevada susceptibilidad a la erosión y a las
remociones en masa superficiales,, subrayando la importancia de los controles
operacionales y de diseño.
4. Vulnerabilidad Híbrida Reconocida: Se establece la necesidad de evaluar la

vulnerabilidad de forma diferenciada: (a) La vulnerabilidad social del entorno
(caracterizada por baja densidad poblacional, indicadores censales de
dependencia, vivienda y acceso a servicios) y (b) la vulnerabilidad operacional/física
dentro de la faena (determinada por la exposición de ~53 trabajadores y la presencia
de infraestructura crítica).

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

5. Niveles de Riesgo Gestionables con Medidas Específicas: La combinación de las

zonas de susceptibilidad identificadas con la vulnerabilidad híbrida genera niveles
de riesgo diferenciados espacialmente (Figuras 11, 12 y 13). Si bien existen zonas
con riesgo Alto y Muy Alto (especialmente dentro y alrededor de la faena), estos han
sido gestionados y mitigados adecuadamente mediante la implementación rigurosa
y focalizada de las medidas de control, monitoreo y contingencia propuestas,
complementando los análisis geotécnicos e hidrológicos específicos del proyecto.

**8.2 RECOMENDACIONES**

Derivado de las conclusiones anteriores, se formulan las siguientes recomendaciones:

1. Utilizar Mapas de Susceptibilidad: Incorporar activamente las figuras 3, 4 y 5 como

base para la planificación detallada de operaciones, diseño de obras, planes de
cierre y gestión ambiental de la Faena Las Piedras.

2. Priorizar Medidas de Mitigación: Enfocar la implementación de las medidas

detalladas en la Sección 6 en las zonas identificadas con susceptibilidad Alta y
Moderada-Alta en cada mapa, abordando las causas específicas:

 - Remociones/Erosión (Cobertura): Implementar revegetación y control de erosión
superficial (biomantos, etc.) en las áreas intervenidas con baja cobertura
(Clusters 1 y 3 de Remociones; Cluster 3 y 1 de Erosión).

 - Inundación (Interna/Faena): Optimizar y mantener rigurosamente el sistema de
Manejo de Aguas Lluvias de la Faena (Cluster 3 de Inundación) para manejar la
alta escorrentía generada y prevenir encharcamientos.

 - Remociones/Erosión (Pendiente Alta): Mantener la cobertura vegetal en las
laderas naturales muy empinadas (Cluster 5 de Remociones, Cluster 2 de
Erosión).

 - Inundación (Externa/Proximidad): Verificar los niveles de crecida estimados para
los esteros locales y confirmar el grado de exposición real de las zonas de baja
cota (Clusters 2 y 5 de Inundación).

3. Validación y Actualización: Realizar verificaciones en terreno de las zonificaciones

de susceptibilidad Establecer un protocolo para actualizar periódicamente los
análisis de susceptibilidad a medida que se disponga de nuevos datos (nuevas
imágenes satelitales, datos de monitoreo).
4. Utilizar Mapas de Riesgo Detallados: Utilizar estos mapas como herramienta de

apoyo para la toma de decisiones sobre priorización de inversiones, definición de
protocolos y planificación del uso del suelo interno.
5. Gestión Adaptativa y Actualización: Establecer un ciclo de revisión periódica (ej.

anual o bianual) de los mapas de susceptibilidad y riesgo, incorporando nuevos
datos de monitoreo, cambios operativos, eventos ocurridos, o mejoras en los datos
base (ej. MDE), para asegurar una gestión de riesgos dinámica y actualizada.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

**9.** **BIBLIOGRAFÍA**

 - Alegría Calvo, M. A. (2014). Levantamiento hidrogeológico en cuencas pluviales
costeras en la Región del Libertador Bernardo O'Higgins, del Maule y del Bío-Bío,
etapa 2.

 - Biró-Bagóczky, L. (1982). Revisión y redefinición de los "Estratos de Quiriquina",
Campaniano-Maastrichtiano, en su localidad tipo, en la Isla Quiriquina, 36°37' Lat.
Sur, Chile, Sudamérica, con un perfil complementario en Cocholgüe. In Congreso
Geológico Chileno, No. 3, Actas 1: A29-A64. Concepción.

 - Cecioni, G. (1983). Chanco Formation, a potential Cretaceous reservoir, central
Chile. Journal of Petroleum Geology 6(1): 89-93.

 - Creixell, C., Oliveros, V., Vásquez, P., Navarro, J., Vallejos, D., Valin, X., Godoy, E.,
& Ducea, M.N. (2016). Geodynamics of Late Carboniferous Early Permian forearc in
north Chile (28°30'-29°30' S). Journal of the Geological Society 173(5): 757-772.

 - Deckart, K., Hervé, F., Fanning, C.M., Ramírez, V., Calderón, M., & Godoy, E.
(2014). U-Pb Geochronology and Hf-O Isotopes of zircons from the Pennsylvanian
Coastal Batholith, South-Central Chile. Andean Geology 41(1): 49-82.

 - Gajardo, A., & Carrasco, R. (1997). Recursos no metálicos de la Región del Maule.
Servicio Nacional de Geología y Minería-Gobierno Regional de la Región del Maule,
Informe Registrado IR-97-11: 221 p.

 - Gana, P., & Hervé, F. (1983). Geología del Basamento Cristalino en la Cordillera de
la Costa entre los ríos Mataquito y Maule, VII Región. Revista Geológica de Chile
19-20: 37-56.

 - García, F., & Valdivia, H. (1970). Informe geológico de Chanco, Provincia del Maule.
Empresa Nacional del Petróleo: 42 p.

 - García-Sansegundo, J., Rubio-Ordóñez, A., Heredia, N., Santos-Martínez, J.,
Palape, C., Cuesta, A., Farías, P., Gallastegui, G., García-Moreno, O., MartínGonzález, F., & Hyppolito, T. (2018). La estructura de la Serie Oriental en la zona
del Río Maule, Constitución (Chile). In Congreso Geológico Chileno, No. 15, Actas
1: 920-923.

 - Hawker, L., Uhe, P., Paulo, L., Sosa, J., Savage, J., Sampson, C., & Neal, J. (2022).
A 30 m global map of elevation with forests and buildings removed. Environmental
Research Letters, 17(2), 024016.

 - Hervé, F., Godoy, E., Parada, M.A., Ramos, V., Rapela, C., Mpodozis, C., & Davison,
J. (1987). A general view on the Chilean-Argentine Andes, with emphasis on their
early history. In Circum-pacific Orogenic belts and evolutions of the Pacific area
Ocean Basin. American Geophysical Union, Geodynamic Series 18: 97-113.

 - Hyppolito, T., García-Casco, A., Juliani, C., Meira, V.T., & Hall, C. (2014a). Late
Paleozoic onset of subduction and exhumation at the western margin of Gondwana
(Chilenia Terrane): Counterclockwise P-T paths and timing of metamorphism of
deep-seated garnet-mica schist and amphibolite of Punta Sirena, Coastal
Accretionary Complex. Lithos 206-207: 409-434.

 - Hyppolito, T., Juliani, C., García-Casco, A., Meira, V., Bustamante, A., & Hervé, F.
(2014b). The nature of the Palaeozoic oceanic basin at the southwestern margin of
Gondwana and implications for the origin of the Chilenia terrane (Pichilemu region,
central Chile). International Geology Review 56(9): 1097-1121.

 - Jorquera, R., Domagala, J.-P., Villa, V., & Astudillo, N. (2023). Geología del área
Pichibelco-Cauquenes, región del Maule. Servicio Nacional de Geología y Minería,
Carta Geológica de Chile, Serie Geología Básica 214: 151 p.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

 - Lindsay, J. B. (2014, April). The whitebox geospatial analysis tools project and openaccess GIS. In Proceedings of the GIS research UK 22nd annual conference, The
University of Glasgow (pp. 16-18).

 - López, L., Vergara, C., Fuentes, P., Jorquera, R., Domagala, J. P., Cifuentes, J. L.,
& Cáceres, D. (2020). Caracterización hidrogeológica de la cuenca del río
Cauquenes, regiones del Maule y Ñuble.

 - Parra, F. (2024). Sistema de predicción, detección y simulación de remociones en
masa [Tesis doctoral no publicada]. Universidad de Santiago de Chile.

 - Richter, P.P., Ring, U., Willner, A.P., & Leiss, B. (2007). Structural contacts in
subduction complexes and their tectonic significance: the Late Palaeozoic coastal
accretionary wedge of central Chile. Journal of the Geological Society 164(1): 203214.

 - Salazar, C., Stinnesbeck, W., & Quinzio-Sinn, L.A. (2010). Ammonites from the
Maastrichtian (Upper Cretaceous) Quiriquina Formation in central Chile. Neues
Jahrbuch Für Geologie und Paläontologie-Abhandlungen Band 257(2): 181-236.

 - Shen, Z., Yong, B., Gourley, J. J., Qi, W., Lu, D., Liu, J., ... & Zhang, J. (2020). Recent
global performance of the Climate Hazards group Infrared Precipitation (CHIRP) with
Stations (CHIRPS). Journal of Hydrology, 591, 125284.

 - Valenzuela, H., & Young, G. (1979). Geología marina entre Constitución y
Concepción. Empresa Nacional del Petróleo: 48 p.

 - WaterWays, Portugal; Broschek, U., Galleguillos, C., Matus, P., Díaz, G., Cárdenas,
V., Dourojeanni, P., López, A.; Centro de Ecología Aplicada (Contreras, M., &
Peralta, J. M.). (2022). _Estimación de la recarga en dos cuencas costeras en la_
_región del Maule a través del modelo WetSpass_ . Fundación Chile, Fundación Futuro
Latinoamericano, Fundación Avina.

 - Willner, A.P., Thomson, S.N., Kröner, A., Wartho, J.A., Wijbrans, J.R., & Hervé, F.
(2005). Time markers for the evolution and exhumation history of a Late Palaeozoic
paired metamorphic belt in north-central Chile (34°-35°30'S). Journal of Petrology
46(9): 1835-1858.

 - Wright, M. N., & Ziegler, A. (2015). Ranger: A fast implementation of random forests
for high dimensional data in C++ and R. arXiv preprint arXiv:1508.04409.

 - Aron, F.; Cembrano, J.; Astudillo, F.; Allmendinger, R.W.; Arancibia, G. (2015).
Constructing forearc architecture over megathrust seismic cycles: Geological
snapshots from the Maule earthquake region, Chile. The Geological Society of
America, Bulletin 127 (3-4): 464-479.

 - Geostudios (2022). Informe Geotécnico Complementario. Informe técnico preparado
para Migrin S.A.

 - Geostudios (2023). Estudio Geotécnico para Instalaciones Remanentes. Informe
técnico preparado para Migrin S.A.

 - Geostudios (2023). Levantamiento Estructural Complementario. Informe técnico
preparado para Migrin S.A.

 - GTECT Consultores (2005). Estudio Geológico-Minero Yacimiento Las Piedras,
Región del Maule. Informe técnico preparado para Inversiones El Alto.

 - Hazen, A. (1911). Discussion of 'Dams on sand foundations' by A.C. Koenig.
Transactions of the American Society of Civil Engineers, 73, 199-203.

 - Hidroambiente Consultores (2022). Informe Hidrogeológico Las Piedras. Informe
técnico preparado para Migrin S.A.

 - Kozeny, J. (1927). Uber kapillare Leitung des Wassers im Boden. Sitzungsber Akad.
Wiss., Wien, 136(2a): 271-306.

ANÁLISIS DE RIESGOS GEOLÓGICOS Y GEOMORFOLÓGICOS
MODIFICACIÓN Y OPTIMIZACIÓN FAENA MINERA DE CUARZO PLANTA LAS PIEDRAS

 - Migrin S.A. (2023). Informe de Monitoreo Hidrogeológico Anual 2023. Informe
interno

 - Muñoz, C. (1993). Metodologías de exploración de yacimientos metalíferos en la
Cordillera de la Costa, entre las latitudes 34°45' y 36°00' Sur, VII Región, Chile.
Memoria de título, Universidad de Chile.