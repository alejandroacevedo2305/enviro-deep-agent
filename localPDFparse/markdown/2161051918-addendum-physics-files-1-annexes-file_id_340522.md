---
title: Sin título
author: Hugo Toledo (Flow)
date: D:20240626090410-04'00'
language: es
type: report
pages: 56
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - EQUIPO TÉCNICO RESPONSABLE
  - CONTENIDOS DEL INFORME
  - 1 INTRODUCCIÓN
  - 2 DESCRIPCIÓN DEL ENTORNO DEL PROYECTO
  - 3 RECOPILACIÓN DE ANTECEDENTES
  - 4 METODOLOGÍA
  - 5 RESULTADOS OBTENIDOS
  - 6 CONCLUSIONES
  - 7 REFERENCIAS
  - 8 APÉNDICES
-->

|Título del documento:|Estudio Hidrológico e Hidráulico de Crecidas - DIA Obras Complementarias y Ajustes<br>Operacionales|
|---|---|
|**Tipo de documento:**|Reporte Técnico - Rev. 0|
|**Código del documento:**|FLOW-COD007-REP-HID-001R0|
|**Suscribe el documento:**|Flow Hydro Consulting Group|
|**Enviado a:**|Jorge Jemio F.|
|**Empresa:**|Codelco|
|**Fecha**|26 de junio de 2024|

|Revisión|Fecha|Emitido para|Preparó|Revisó|Aprobó|Cliente|
|---|---|---|---|---|---|---|
|A|05/06/2024|Codelco|FF|HT|JY|-|
|B|13/06/2024|Codelco|HT|HT|JY|JJ|
|C|25/06/2024|Codelco|HT|HT|JY|JJ|
|0|26/06/2024|Codelco|HT|HT|JY|JJ|
||||||||
||||||||

# EQUIPO TÉCNICO RESPONSABLE

**José Yáñez - Hidrogeólogo Principal**

Ingeniero Civil, P. Universidad Católica de Chile, MSc. U. Politécnica de Cataluña, España. CGWP-NGWA, USA.

**Hugo Toledo - Hidrólogo Senior**

Ingeniero Civil, Mención en Hidráulica, Sanitaria y Ambiental, Universidad de Chile.

**Felipe Figueroa - Hidrólogo de Proyecto**

Ingeniero Civil, Universidad de Valparaíso.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 Página iii

# CONTENIDOS DEL INFORME

**1** **INTRODUCCIÓN .........................................................................................................................** **1**

1.1 Generalidades .........................................................................................................................................1

1.2 Objetivo ...................................................................................................................................................1

1.3 Alcances ..................................................................................................................................................1

1.4 Estructura del informe ............................................................................................................................2

**2** **DESCRIPCIÓN DEL ENTORNO DEL PROYECTO ..............................................................................** **3**

2.1 Ubicación .................................................................................................................................................3

2.2 Obras del proyecto ..................................................................................................................................3

2.3 Caracterización hidrológica .....................................................................................................................4

**3** **RECOPILACIÓN DE ANTECEDENTES .............................................................................................** **6**

3.1 Pluviometría ............................................................................................................................................6

3.2 Cartografía IGM .......................................................................................................................................6

3.3 Topografía ...............................................................................................................................................8

3.4 Otros antecedentes de interés................................................................................................................8

**4** **METODOLOGÍA .........................................................................................................................** **9**

4.1 Definición de cuencas hidrográficas .......................................................................................................9

4.2 Analisis de precipitación .........................................................................................................................9

4.3 Analisis de frecuencias ......................................................................................................................... 12

4.4 Analisis de bondad del ajuste ............................................................................................................... 13

4.5 Estimación de caudales de crecidas ..................................................................................................... 15

4.6 Modelación hidráulica .......................................................................................................................... 18

**5** **RESULTADOS OBTENIDOS ..........................................................................................................** **21**

5.1 Hidrografía y cuencas de interés .......................................................................................................... 21

5.2 Precipitaciones de diseño .................................................................................................................... 24

5.3 Estimación de caudales de crecidas ..................................................................................................... 30

5.4 Modelación hidráulica .......................................................................................................................... 31

**6** **CONCLUSIONES .........................................................................................................................** **47**

**7** **REFERENCIAS ............................................................................................................................** **50**

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 Página iv

**8** **APÉNDICES ................................................................................................................................** **51**

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 Página v

# 1 INTRODUCCIÓN

##### 1.1 GENERALIDADES

El presente Informe se refiere a la estimación de los niveles de escurrimiento superficial en el sector de
emplazamiento de las obras complementarias que forman parte del proyecto Minero Chuquicamata
Subterráneo (PMCHS), en el marco de la DIA “Obras Complementarias y Ajustes Operacionales Mina
Chuquicamata Subterránea”.

El análisis hidrológico e hidráulico se desarrolla con la finalidad de estimar los caudales de crecida para un período
de retorno de 100 años y evaluar la relevancia de los niveles de inundación en el trazado y emplazamiento de la
línea de transmisión eléctrica, el área de emplazamiento de los portales de los túneles de extracción y las zonas
de instalaciones de faenas que se desarrollan como parte de las obras complementarias, con el propósito de dar
respaldo a la solicitud indicada en el ICSARA N°1 del Proyecto, en relación con la posible intervención por cruces
de quebradas existentes en el área del Proyecto.

La estimación de los caudales de crecidas y el modelo hidráulico necesarios para la estimación de los niveles de
inundación son desarrollados por Flow Hydro Consulting Group SpA sobre la base de la información existente y
disponible, la cual corresponde tanto a antecedentes entregados por la Gerencia de Planificación del Distrito
Norte (GPDN) como a antecedentes de carácter público.

La zona de estudio abarca una superficie aproximada de 87 km [2], la cual se ubica aproximadamente 15 km al
norte de la ciudad de Calama, en la región de Antofagasta. El sector forma parte de la hoya hidrográfica del río
San Salvador, específicamente en la denominada subsubcuenca Río San Salvador (código BNA 02111).

El diagnóstico de inundabilidad de los cauces del sector de estudio, que simula el eje hidráulico asociado a la
crecida de diseño, se desarrolla utilizando el programa computacional HEC-RAS, en su versión 5.0.7 del año 2019.

##### 1.2 OBJETIVO

El objetivo general del análisis es realizar un diagnóstico hidráulico de los cruces de cauces presentes en el área
de emplazamiento de la línea de transmisión eléctrica (LTE), el área de emplazamiento de los portales de los
túneles de extracción y las instalaciones de faenas de los contratistas, que forman parte de las obras
complementarias del Proyecto, estimando alturas de escurrimiento y evaluando la situación de inundabilidad de
las obras proyectadas en aquel sector. El análisis se desarrolla considerando la crecida de diseño de 100 años de
período de retorno.

##### 1.3 ALCANCES

El alcance del presente estudio considera el análisis hidrológico e hidráulico relativo a los cruces de cauces del
sector de estudio. Para esto, se contemplan las siguientes actividades:

 - Análisis de antecedentes.

 - Definición de la red hídrica del sector.

 - Determinación de la precipitación de diseño.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

 - Estimación de caudales de crecidas para un período de retorno de 100 años en zona de estudio

 - Desarrollo del modelo hidráulico de flujo unidimensional en software HEC-RAS.

 - Obtención del álveo de inundación para la crecida de 100 años de período de retorno (T=100), según

modelación hidráulica.

 - Indicación de inundabilidad respecto del emplazamiento de las obras en relación con la posible

intervención por cruces de quebradas existentes en el área del Proyecto.

##### 1.4 ESTRUCTURA DEL INFORME

El presente Informe está estructurado en 6 capítulos, según se detalla a continuación:

 - El Capítulo 1 corresponde a la presente Introducción.

 - El Capítulo 2 describe el entorno del Proyecto, en relación con su ubicación, obras y características

hidrológicas.

 - En el Capítulo 3 se lleva a cabo un análisis de los antecedentes disponibles para el desarrollo de esta

consultoría. Incluye información pluviométrica, cartográfica, topográfica e información adicional de

utilidad para los fines del estudio.

 - En el Capítulo 4 se describe la metodología empleada en el presente estudio.

 - El Capítulo 5 presenta los resultados obtenidos para el estudio hidrológico e hidráulico desarrollado en

el área de estudio, para las condiciones de diseño supuestas y las características particulares del sector.

 - En el Capítulo 6 se entregan las conclusiones relevantes de la situación analizada.

 - En el Capítulo 7 se indican las referencias bibliográficas utilizadas en el presente estudio.

 - Finalmente, en el Capítulo 8 se incluyen los Anexos que complementan los resultados del estudio

hidrológico e hidráulico desarrollado.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

# 2 DESCRIPCIÓN DEL ENTORNO DEL PROYECTO

##### 2.1 UBICACIÓN

El Proyecto se localiza al interior de las servidumbres mineras de la División Chuquicamata, en la Región de
Antofagasta, provincia de El Loa, comuna de Calama, a 8,6 km del casco urbano de Calama y a 200 km al noreste
de la ciudad de Antofagasta, aproximadamente.

En la Figura 2-1 se muestra la ubicación general de sector de estudio.

Fuente: Elaboración propia.

Figura 2-1: Ubicación general del sector de estudio

##### 2.2 OBRAS DEL PROYECTO

Las obras complementarias incluidas en el análisis hidrológico e hidráulico corresponden al trazado de la línea
eléctrica (compuesta por 127 estructuras), las superficies definidas para el emplazamiento de la plataforma de

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

los portales de túneles de extracción, de la sala eléctrica de túneles de extracción y de la sala eléctrica de túneles
de inyección y los polígonos propuestos para las instalaciones de faenas.

En la Figura 2-2 se presenta el detalle de ubicación de las obras indicadas anteriormente.

Fuente: Elaboración propia.

Figura 2-2: Ubicación general de las obras del Proyecto

##### 2.3 CARACTERIZACIÓN HIDROLÓGICA

De acuerdo con el inventario de cuencas, subcuencas y subsubcuencas de Chile, el sector de estudio forma parte
de la cuenca del río Loa (código BNA 021), subcuenca del Loa Medio (entre R. Salado y Q. de Barrera) (código
BNA 0211), subsubcuenca del río San Salvador (código BNA 02111).

Este sector se encuentra en la clasificación climática BWk(w), que se define como clima desértico frío de lluvia
estival, el cual corresponde a un clima árido con escasez de lluvia durante la mayor parte del año, cuya vegetación
predominante es de tipo xerófila (adaptadas a climas con escasa o nula presencia de agua).

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

En cuanto a las precipitaciones en el sector, la extrema aridez experimenta puntuales eventos de precipitación
durante el año hidrológico, las cuales se originan principalmente en los meses de verano y no sobrepasan los 75

mm anuales.

Respecto de la hidrografía, el área de estudio no cuenta con escorrentías permanentes ni acumulación de aguas
superficiales naturales estancadas, sino sólo quebradas de escorrentía intermitente y de características
endorreicas que se activan sólo cuando ocurren eventos esporádicos de precipitación.

El principal afluente de importancia corresponde al río San Salvador, el cual nace de la reunión de varias
quebradas secas con cabeceras en las proximidades de salares de la pampa, aproximadamente 17 km al suroeste
del área del proyecto, en un sector denominado Ojos de Opache.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

# 3 RECOPILACIÓN DE ANTECEDENTES

Para llevar a cabo el análisis hidrológico e hidráulico en el sector de estudio, se recopiló un conjunto de
información relevante para su desarrollo, los que corresponden principalmente a datos observados de
precipitación máxima en 24 hr, información topográfica y cartográfica y otros antecedentes de interés para el

estudio.

A continuación, se presenta una descripción de la información recopilada.

##### 3.1 PLUVIOMETRÍA

En la Tabla 3-1 y Figura 3-1 se presenta la ubicación y características de las estaciones seleccionadas para realizar
el análisis de frecuencias para precipitaciones máximas en 24 horas.

Tabla 3-1: Estaciones meteorológicas seleccionadas para el análisis hidrológico

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ##### 3.1 PLUVIOMETRÍA En la Tabla 3-1 y Figura 3-1 se presenta la ubicación y características de las estaciones seleccionadas para realizar el análisis de frecuencias para precipitaciones máximas en 24 horas. -->

**Tabla 3-1: Estaciones meteorológicas seleccionadas para el análisis hidrológico**

| Código | Nombre Estación | Operador | Coordenadas UTM<br>WGS84 - 19S | Col5 | Altitud<br>(m s.n.m.) | Tipo |
| --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Nombre Estación** | **Operador** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| 02110013-7 | Calama | DGA | 509.639 | 7.517.059 | 2.300 | Meteorológica |
| 220002 | El Loa, Calama Ad. | DMC | 511.057 | 7.512.040 | 2.321 | Meteorológica |

<!-- Estadísticas: 3 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia en base a información de la DGA y DMC. ##### 3.2 CARTOGRAFÍA IGM -->
<!-- FIN TABLA 3-1 -->


|Código|Nombre Estación|Operador|Coordenadas UTM<br>WGS84 - 19S|Col5|Altitud<br>(m s.n.m.)|Tipo|
|---|---|---|---|---|---|---|
|**Código**|**Nombre Estación**|**Operador**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|02110013-7|Calama|DGA|509.639|7.517.059|2.300|Meteorológica|
|220002|El Loa, Calama Ad.|DMC|511.057|7.512.040|2.321|Meteorológica|

Fuente: Elaboración propia en base a información de la DGA y DMC.

##### 3.2 CARTOGRAFÍA IGM

Para la definición de la red hidrográfica existente en el sector de estudio, se ha utilizado la cartografía definida
por el Instituto Geográfico Militar (IGM), en escala 1:50.000, para el sector de Calama.

Las cartas utilizadas son las siguientes:

 - Carta 41B Cerros de Paqui.

 - Carta 51B Calama.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia en base a información de la DGA, DMC e IGM.

Figura 3-1: Ubicación de estaciones meteorológicas seleccionadas

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

##### 3.3 TOPOGRAFÍA

Para definir las características del relieve del sector de estudio, se han utilizado los Modelos de Elevación Digital
(DEM, por su sigla en inglés) aportados por el cliente y especificados a continuación:

 - DEM_Hidrologia_Talabre_a_nov2014_al-3m: levantamiento aerofotogramétrico que incluye la totalidad

del área de estudio, para análisis general de las características geomorfométricos de las cuencas

aportantes a los sectores de cruces de quebradas con el emplazamiento de la LTE.

 - DEM_1m_vf: levantamiento topográfico del área al norte del sector de estudio, para caracterización

geomorfométrica del sector de emplazamiento de la plataforma de los portales de los túneles de

extracción.

 - DEM_AREA_1: levantamiento topográfico específico del área de emplazamiento de las estructuras 56 a

la 64 de la LTE.

 - DEM_AREA_2: levantamiento topográfico específico del área de emplazamiento de las estructuras 78 a

la 93 de la LTE.

 - DEM_AREA_3: levantamiento topográfico específico del área de emplazamiento de las estructuras 103

a la 111 de la LTE.

##### 3.4 OTROS ANTECEDENTES DE INTERÉS

A continuación, se enumeran otros antecedentes que son de utilidad para el desarrollo del estudio hidrológico e

hidráulico en el sector de estudio:

 - Resolución DGA N°135/2020: Establece los aspectos relevantes para la correcta aplicación del artículo

41 del Código de Aguas. En este caso, se establece que la fuente oficial que aplica para la identificación

de los cauces naturales es la cartografía IGM 1:50.000 y la crecida de análisis corresponde a la de 100

años de período de retorno.

 - Definición de cuenca aportante al sector de Proyecto: En este caso, el aporte principal está delimitado

por la subsubcuenca del río San Salvador (código BNA 02111), la cual forma parte de la subcuenca del río

Loa Medio entre río Salado y quebrada de Barrera (código BNA 0211), perteneciente a la cuenca del río

Loa.

 - Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin Información Fluviométrica: Manual

de procedimientos de la Dirección General de Aguas (DGA) para el cálculo de caudales máximos y

mínimos en Chile.

 - Guías Metodológicas para Presentación y Revisión Técnica de Proyectos de Modificación de Cauces

Naturales y Artificiales (DGA)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

# 4 METODOLOGÍA

##### 4.1 DEFINICIÓN DE CUENCAS HIDROGRÁFICAS

Para definir el área de drenaje y bordes de las cuencas ubicadas en la zona del Proyecto se utilizó el modelo de
elevación digital (DEM) aportado por el cliente para la totalidad del sector de estudio, además de un DEM
obtenido a través del producto satelital SRTM (Shuttle Radar Topography Mission, sistema de radar
especialmente diseñado para crear mapas topográficos de la superficie terrestre), al cual se accedió a través de
la plataforma Earth Explorer del USGS y posee una resolución de 1 arc-sec, lo cual es aproximadamente 30 m.

También se utilizó la red hidrográfica propuesta por el IGM, en escala 1:50.000, con la cual se verificaron los
sectores de cruce de cauces con el emplazamiento de las obras del Proyecto.

Las cuencas hidrográficas y sus características geomorfométricas particulares son definidas en función de esta
red de drenaje y de las líneas divisorias de aguas obtenidas del relieve del sector de estudio.

##### 4.2 ANALISIS DE PRECIPITACIÓN

Para el análisis de la precipitación, se dispuso de la información proporcionada por la DGA y DMC de las
estaciones pluviométricas cercanas al área de estudio, teniendo en cuenta la altitud y la extensión de sus datos.
También se comparan los valores de precipitación máxima diaria expuestas en línea de base clima y meteorología
para la declaración de impacto ambiental proyecto “Obras Complementarias y Ajustes Operacionales Mina
Chuquicamata Subterránea”.

Una vez definidas las estaciones meteorológicas, se realiza un análisis estadístico de sus registros, con el
propósito de completar, rellenar, extender y establecer posibles inconsistencias en sus datos.

4.2.1 Selección de la estación patrón

Su selección está basada en la elección de las estadísticas más largas y mejor observadas durante un período
específico. Los criterios para la determinación de la Estación Patrón se exponen a continuación:

 - Frente a una serie de datos de distinta longitud, se eligen las tendencias más largas, dado que debido a

su longevidad se obtiene una menor probabilidad de error.

 - Frente a series de datos de distinta longitud, se eligen las de más reciente data, por cuanto se supone la

utilización de equipos más confiables.

 - Frente a una serie de datos de cualidades similares, se eligen las más cercanas al sector de estudio.

Con los datos acumulados promedio, que corresponden en una primera aproximación a lo que se denomina
estación patrón, se establece un análisis de doble masa entre estos valores y los valores acumulados de cada
estación componente de dicho promedio.

Si las “n” estaciones no presentan tendencias con quiebres, se asume que el valor promedio anual de las “n”
estaciones seleccionadas, corresponde a los valores representativos de la estación patrón.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Si alguna de las “n” estaciones presenta algún tipo de quiebre en las tendencias, ésta es eliminada calculándose
un nuevo promedio para cada año, con las estaciones restantes.

Posteriormente se repite el análisis de doble masa con cada estación componente, hasta llegar a un patrón de
masa depurado.

4.2.2 Análisis de consistencia

El método de las curvas másicas o dobles acumuladas permite estudiar y corregir, en una estadística
pluviométrica de una estación, los efectos de un cambio de exposición o ubicación del pluviómetro o pluviógrafo,
los cambios en las técnicas de observación e incluso algunos errores instrumentales o de lectura.

Detectar estos cambios o errores en una estadística es muy importante, ya que en la solución de problemas
hidrológicos interesa asegurarse que los cambios de tendencia en el tiempo se deban sólo a causas
meteorológicas y no a la manera en que se hacen las observaciones. De este modo, se logra también una
consistencia en el tiempo del registro pluviométrico para que pueda ser comparado con el de otra estación

vecina.

El método está basado en que generalmente los valores acumulados del promedio de las precipitaciones anuales
de varias estaciones contiguas, no se ve afectado por un cambio en la estación individual, ya que existe una
compensación entre ellas. Consecuentemente, el procedimiento consiste en ubicar en el eje de las abscisas la
suma acumulada promedio de un conjunto de estaciones y en el eje de las ordenadas, la suma acumulada de la
estación en estudio, como se ejemplifica en la Figura 4-1.

Fuente: UdeC, 2024.

Figura 4-1: Curva másica o doble acumulada de precipitaciones

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Si la resultante es una línea recta, se puede suponer que no ha habido cambios en los métodos de observación
en la instalación de la estación en estudio. Si no es una recta, el cambio de pendientes se puede asociar a un
cambio en el régimen de la estación (exposición, ubicación, errores instrumentales o cambio de técnicas de
observación). En este caso el ajuste respectivo se puede lograr a partir de la expresión:

## _S aj_

=
## _P aj S ob P ob_

_aj_

_aj_

_ob_

Donde:

P aj = precipitación ajustada
P ob = precipitación observada
S aj = pendiente recta período más reciente
S ob = pendiente recta período cuando ocurre Pob

Finalmente, es necesario recalcar algunas sugerencias para el uso adecuado del método de la curva másica:

 - Es conveniente adoptar un criterio conservador en el ajuste, es decir, es preferible un ajuste por defecto

antes que por exceso.

 - Un cambio de pendiente no debe considerarse significativo, a no ser que se mantenga, a lo menos, por

unos cinco años.

Es necesario tener en cuenta que hay consistencia para períodos largos de tiempos en la distribución regional de
la precipitación, pero que esta consistencia no necesariamente tiene que producirse para períodos cortos de
tiempo. Por lo tanto, el análisis con curvas másicas no es aplicable a precipitaciones diarias o de duración menor.
Usualmente se aplica para períodos anuales o para la precipitación estacional. Desgraciadamente no existen
métodos cuantitativos para probar y lograr la consistencia de datos pluviométricos para períodos cortos.

4.2.3 Relleno de la estadística

Además de comprobar la consistencia del registro pluviométrico, antes de usar los datos de lluvia es necesario
completar las estadísticas por medio de algún proceso de interpolación.

Es frecuente que en una estación falten datos de la precipitación caída en uno o más días, meses o años. Por lo
tanto, es conveniente disponer de un método o criterio para estimarlas y así poder calcular las precipitaciones
mensuales y anuales. Algunos métodos factibles son los presentados a continuación.

_4.2.3.1 Curva másica_

Para interpolar años en que la precipitación de una estación no ha sido medida, es posible utilizar la pendiente
de la recta para el último período de observación de una curva másica. La relación es:

###### _S X_ P x = P A _S A_

_X_

_x_

###### = P

_A_

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Donde:

P X : precipitación no medida en estación x durante año n.
P A : precipitación medida en estación A durante el año n.
S X : pendiente de la curva másica para estación X.
S A : pendiente de la curva másica para estación A.

_4.2.3.2 Módulo pluviométrico_

Se entiende por “módulo pluviométrico anual de una estación”, al promedio aritmético de las precipitaciones
anuales registradas en una estación. Generalmente se utiliza un período de 10 años. Existen dos alternativas:

a) El módulo pluviométrico de una estación no difiere en más de un 10% del módulo pluviométrico de

cualquiera de tres estaciones base. En este caso se supone que la precipitación en la estación incompleta

es aproximadamente igual al promedio aritmético de las precipitaciones registradas en las estaciones

base durante el mismo período.

b) El módulo pluviométrico de una estación difiere en más de un 10% del módulo pluviométrico de

cualquiera de tres estaciones base. En este caso:

_B_

_X_

_X_

### P X = P A + P B + P C



_M_ _X_ _M_
_P_ _A_ +
_M_ _A_ _M_

_X_

_B_

_X_

_1_  _M_ _X_ _M_ _X_ _M_ _X_

= _P_ _A_ + _P_ _B_ + _P_

_3_  _M_ _A_ _M_ _B_ _M_ _C_

_1_ _M_ _X_ _M_ _X_ _M_ _X_

_P_ _A_ + _P_ _B_ + _P_ _C_

_3_  _M_ _A_ _M_ _B_ _M_ _C_ 



_A_

_A_

_C_

Donde:

M : módulos pluviométricos
P : precipitación
A, B y C : estaciones base

X : estación en estudio

Este método es particularmente apropiado cuando el régimen de precipitaciones es de tipo orográfico.

##### 4.3 ANALISIS DE FRECUENCIAS

El análisis de frecuencia relaciona la magnitud de un evento con su frecuencia de ocurrencia, mediante el uso de
distribuciones de probabilidad. Eventos severos ocurren con menor frecuencia que eventos más moderados.

Para este estudio el análisis se hará en forma analítica pudiéndose realizar, además, de forma gráfica.

Como la zona en estudio es conocida como una zona árida donde se presentan años con precipitación nula, es
necesario utilizar una metodología que represente esta situación, los cuales no pueden ser utilizados en
distribuciones comunes, pues éstos no se ajustan a una serie datos con esas características. El método está
basado en probabilidades condicionadas e incorpora el evento de que no llueva asignándole una probabilidad
de ocurrencia asociada a un periodo de retorno.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

En estos lugares la probabilidad de que la precipitación sea nula es mayor que cero, P(x=0)>0, llegando a ser
P(x=0)=1 durante algunos años; siendo _x_ un evento de precipitación.

La probabilidad de que el evento lluvia sea nulo se representa como la cantidad de eventos cero en el total de
registros de la estación:

_n_
_Weibull_ : _p_ =

_N_ + 1

Donde:

P : Probabilidad de que la precipitación nula, sea igualada o superada.

n : Número de eventos de lluvia nula.

N : Número total de registros.

De acuerdo con lo anterior, para obtener las probabilidades de excedencia de una serie con valores nulos,
primero, se efectúa un análisis de frecuencia de la serie que contiene sólo los eventos no nulos, G(y).
Posteriormente, se multiplica el valor de la probabilidad que arroja la función de distribución por la probabilidad
condicional del evento no nulo. Lo que queda representado en espacio continuo, con la siguiente distribución

acumulada mixta:

_F_ ( _y_ ) =  _p_ + (1 − _p_ ) - _G_ ( _y_ ); _y_  0

Donde:

P : Probabilidad, de que la precipitación nula, sea igualada o superada.
G(y) : Función de Distribución de Probabilidad para Eventos no nulos.
F(y) : Función acumulada de distribución.

A los valores obtenidos, se le ajustaron el modelo probabilístico de Valores Extremos Tipo I o Distribución de
Gumbel, Distribución Log-Normal, el modelo probabilístico Log-Pearson III, Normal y Gamma para distintos
períodos de retorno.

Se efectuó un análisis de frecuencias de las series en cada una de las estaciones pluviométricas seleccionadas,
con el propósito de obtener precipitaciones máximas en 24 hrs, para distintos períodos de retorno. Para ello, se
utilizaron las funciones de distribución probabilísticas; Normal, Log Normal, Gamma, Log Pearson III y Gumbel.

##### 4.4 ANALISIS DE BONDAD DEL AJUSTE

4.4.1 Test chi-cuadrado

Para el análisis de bondad del ajuste, en términos estadísticos, se utilizó el test Chi-cuadrado (2), el cual consiste
en comparar, en intervalos previamente definidos de la variable aleatoria en análisis, el número de casos
observados en ese intervalo con el número de casos teóricos, función del modelo probabilístico en estudio. Para
que el ajuste de la distribución a la muestra sea aceptable, se requiere que el valor Chi-cuadrado (2) calculado,
sea menor o a lo sumo igual al valor teórico que toma el estadígrafo Chi-cuadrado para un cierto nivel de

confianza.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

La bondad del ajuste de una distribución de probabilidad puede probarse comparando los valores teóricos y

muestrales de las funciones de frecuencia relativa o de frecuencia acumulada.

4.4.2 Prueba de la bondad del ajuste Kolmogorov-Smirnov

Esta prueba consiste en comparar el máximo valor absoluto de la diferencia “D” entre la función de distribución
de probabilidad observada y la estimada, con un valor crítico “d” que depende del número de datos y el nivel de
significancia seleccionado.

###### D = máx F x − F x
##### 0 ( m ) ( m )

Donde:

F 0 (x m ) : Probabilidad observada para el dato x m
F(x m ) : Probabilidad estimada para el dato x m

Si D < d se acepta la hipótesis nula.

La función de distribución de probabilidad observada se calcula como sigue.

_m_
###### F 0 ( x m ) = 1 −

_n_ + 1

Donde:

m : Número de orden del dato X m

n : Número total de datos.

4.4.3 Calidad del ajuste, coeficiente del error estándar de ajustes (EE)

Kite (1988) propuso un estadístico que permite seleccionar la mejor opción, entre diferentes modelos en
competencia, para el ajuste de una muestra de datos x i [j ] para i=1, 2, ..., x j, de un sitio j.

Este estadístico conocido como Error Estándar de Ajuste (EE) tiene siguiente forma:










1
2

_n_ _j_

###### ( x ˆ Tj − x Tj ) 2

ˆ 2










####   ( x ˆ Tj −

=  _i_ = 1

_Tj_ − _x_ _Tj_

_x_ _T_ − _x_
_EE_ =  _i_ = 1

_i_

= 1

=

_n_ − _mp_

−

_j_

Donde:

_X_ T [j] : Son los eventos _X_ i [j] ordenados de mayor a menor con periodo de retorno asignado T=(n j +1)/m y
una probabilidad de no excedencia P=1 - 1/T
n j : Longitud en años del registro analizado.
M : Número de orden del registro.
m=1 : Para el evento más grande.
m=n j : Para el evento más chico.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

###### ˆ j _x_

_T_ : Eventos estimados por una cierta distribución de probabilidad para cada periodo de retorno T
asignado a la muestra ordenada _X_ T [j]
mp : Número de parámetros de la distribución ajustada.
mp=1 : Exponencial-1
mp=2 : Normal, Log Normal-2, Exponencial-2, Gamma-2, Gumbel
mp=3 : Log Normal-3, Gamma-3, Log Pearson III, GVE.
mp=4 : Valores extremos de dos componentes TCEG.
mp=5 : Gumbel de dos poblaciones, Wakeby.

##### 4.5 ESTIMACIÓN DE CAUDALES DE CRECIDAS

Para la determinación de los caudales de cuencas sin control fluviométrico se utilizan métodos indirectos que
relacionan la precipitación y escorrentía para obtener un caudal en función del período de retorno.

El método utilizado es el Método Racional, que tiene una amplia aplicación para estimar el caudal de diseño en
cuencas nivopluviales, pero tiene la desventaja de sobrestimar los caudales en proporción al área, al suponer
una escorrentía constante. Este método establece que el caudal máximo a evacuar está relacionado linealmente
con la lluvia mediante la expresión:

_T_
= _C_  _I_ _tc_ 

= _C_  _I_ _tc_  _A_

_Q_

360

Donde:

Q : Caudal en m [3] /s para un determinado período de retorno.
I tc [T] : Intensidad en mm/hr para el período de retorno seleccionado y duración igual al tiempo de

concentración.

C : Coeficiente de escurrimiento de la cuenca.
A : Área aportante en ha (hasta 25 km [2] )

Para determinar la intensidad de lluvia en el tiempo de concentración de cada cuenca, se ha tenido en cuenta lo
siguiente:

_T_ = 1.1* _CD_ _tc_ - _P_ _T_ = 1.1* _P_ _tcT_ = _PDiseño_ _tcT_
_tc_

1.1* _CD_

_I_ _T_ = 1.1* _CD_ _tc_ - _P_

1.1*

- _P_ _tc_ = _PDiseño_

_tc_ _tc_

_tc_ - _P_ = 1.1* _P_

_tc_ _tc_

60

60 60

Donde:

tc : tiempo de concentración de la cuenca en min.
CD tc : Coeficiente de duración de tc horas
P [T] : precipitación en mm del período de retorno T.
P tc [T] : precipitación en mm del período de retorno T y duración igual a tc.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

El período de retorno de diseño se selecciona de acuerdo con el grado de seguridad que se quiere dar al diseño

o verificación de cada obra en cuestión.

A continuación, se detallan los parámetros más relevantes del método Racional.

4.5.1 Coeficiente de escorrentía

Los coeficientes de escorrentía propuestos en la tabla 3.702.503B del Manual de Carreteras (ver Tabla 4-1) en
función de las características de relieve, infiltración, vegetación y almacenamiento son mayormente utilizados
para la zona centro y sur de Chile, mientras que para la zona norte no es recomendable considerar los tres
últimos, ya que, más que aportar al escurrimiento superficial, restringen o disminuyen los caudales.

Por lo anterior, se utilizó solamente la característica de relieve para estimar los coeficientes de escorrentía para
cada periodo de retorno.

Tabla 4-1: Coeficientes de escorrentía (C) para T=10 años

Fuente: Tabla 3.702.503.B, Manual de Carreteras 2015, Vol. N°3.

Respecto a la tabla anterior, el método racional supone que el coeficiente de escorrentía se mantiene constante
para distintas tormentas. Esto es efectivo para suelos impermeables, pero no así para caudales asociados a altos
períodos de retorno. Por esta razón se aplican los factores de mayoración. Para periodos de retorno mayores a
100 años se sugiere mantener el factor 1,25.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

4.5.2 Tiempo de concentración

En cada cuenca aportante se determina el tiempo de concentración con distintos métodos, para luego comparar
y establecer una relación analítica entre los distintos resultados, según corresponda al rango de validez de estos
y siempre considerando la experiencia obtenida por el consultor en terreno.

Los resultados de las fórmulas utilizadas serán válidos para tiempos de concentración mayores a 10 minutos,
mientras que para tiempos menores este resultado será reemplazando por el valor de dicho umbral, para para
evitar intensidades de lluvia poco representativas.

Existe una gran cantidad de métodos de cálculo para la determinación del tiempo de concentración, métodos
que han sido concebidos bajo condiciones controladas y en cuencas con ciertas características específicas. Las
condiciones teóricas bajo las cuales fueron concebidos estos métodos no siempre se replican en cualquier
cuenca, razón por la cual, no es posible afirmar que un método de cálculo sea más apropiado que otro, sobre
todo cuando los campos de aplicación de ambos son parecidos.

Para determinar los tiempos de concentración se utilizan las fórmulas empíricas y parámetros siguientes:

Tc : Tiempo de Concentración (min.)
S : Pendiente promedio de la cuenca (m/m)
L 1 : Longitud del Cauce principal (Km)
H : Diferencia de altura en cuenca (m).
H 1 : Desnivel entre la salida y el nivel medio de la cuenca (m).
V : Velocidad promedio del flujo

1. Kirpich (1940) (Pequeñas Cuencas de Pendiente Fuerte)

,077

_L_

1
,397 

_L_
_T_ _c_ =,397 

_S_

,0385

2. California Culverts Practice (Kirpich para Pequeñas Cuencas de Montaña)

######  L 13 ,0385 60   [],087   []  H 

######  L 13 T c = 60 ,087   [] _H_

######  L 13   [],087   []  H 

3. U.S. Soil Conservation Service (cuencas de A > 200 ha)

 _L_ 3 ,0385

1
,095 

 _H_ 


= 

 _L_ 3 

1

 _H_ 

_L_

1

_T_ _c_ =,095 

 _H_

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

4. Giandotti (Cuencas de A [] 100 ha)

4 _A_ + 5,1

_T_ _c_ = 4 _A_ + 5,1 _L_ 1

 _T_ _c_ 

+

=

1

4,5 6,3
;

_L_ _L_
1  _T_ 1

5. Texas Highway

_L_

1

_T_ =
_c_ 6,3 - _V_

Tabla 4-2: Velocidades Promedios de Flujo en m/s. (Departamento de Carreteras de Texas)

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 1 _T_ = _c_ 6,3 - _V_ -->

**Tabla 4-2: Velocidades Promedios de Flujo en m/s. (Departamento de Carreteras de Texas)**

| Pendientes<br>% | Valor zona de bosques en<br>partes altas de las cuencas | Zonas con poca vegetación en<br>partes altas de las cuencas | Cauce natural no<br>muy bien definido |
| --- | --- | --- | --- |
| 0 - 3 | 0,3048 | 0,4572 | 0,3048 |
| 4 - 7 | 0,6096 | 0,9144 | 0,9144 |
| 8 - 11 | 0,9144 | 1,2192 | 1,524 |
| 12 - 15 | 1,0668 | 1,3716 | 2,4384 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Pág. “Desing of Sedimentation Basing” Publication of National Research Council, Washington D.C. Junio 1980 Considerando la sensibilidad del tiempo de concentración en la aplicación del método, se adoptará el valor más representativo para cada cuenca, obtenido de la aplicación de las fórmulas descritas anteriormente. -->
<!-- FIN TABLA 4-2 -->


|Pendientes<br>%|Valor zona de bosques en<br>partes altas de las cuencas|Zonas con poca vegetación en<br>partes altas de las cuencas|Cauce natural no<br>muy bien definido|
|---|---|---|---|
|0 - 3|0,3048|0,4572|0,3048|
|4 - 7|0,6096|0,9144|0,9144|
|8 - 11|0,9144|1,2192|1,524|
|12 - 15|1,0668|1,3716|2,4384|

Fuente: Pág. “Desing of Sedimentation Basing” Publication of National Research Council, Washington D.C. Junio 1980

Considerando la sensibilidad del tiempo de concentración en la aplicación del método, se adoptará el valor más
representativo para cada cuenca, obtenido de la aplicación de las fórmulas descritas anteriormente.

##### 4.6 MODELACIÓN HIDRÁULICA

4.6.1 Modelo numérico

La extensión de la modelación en HEC-RAS comprende un tramo como mínimo de 100 m aguas arriba y 100 m
aguas abajo de la intersección de las obras proyectadas con los cauces definidos, tal como se establece en el
acápite 2.5.2.1.2 del documento “Guía de presentación y revisión técnica de proyectos de modificación de cauces
naturales y artificiales, DGA, 2016”.

La geometría del modelo es determinada a partir del DEM aportado por el Cliente para el sector de estudio, con
el cual se construye un archivo TIN con ayuda de las herramientas QGis 3.34.6, desde la cual se extrae la
geometría de cada cauce de estudio y se desarrolla un modelo en el software HEC-RAS, desarrollado por US Army
Corps of Engineers, según el procedimiento descrito a continuación.

Primero se define el centro de río, el límite del cauce y las superficies de inundación, para luego definir la cantidad
de secciones transversales, las cuales están distanciadas 50 m entre sí, en base a lo exigido por el acápite 2.5.2.1.4
del documento “Guía de presentación y revisión técnica de proyectos de modificación de cauces naturales y
artificiales, DGA, 2016”, variando para cada cauce según sus características particulares. Mientras más

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

singularidades se presenten deben ser mayores los perfiles a utilizar, por el contrario, en cauces sin muchas
singularidades los perfiles a usar pueden ser menos y más espaciados.

4.6.2 Eje del cauce y secciones transversales

Para la modelación 1D se consideró la topografía extraída de los distintos DEM aportados por el cliente, para
cada uno de los sectores de análisis. Estas topografías tienen una precisión de 0,5 m en la sección del cauce y
para el resto del dominio.

Con estos DEM se obtuvieron las elevaciones del eje del cauce cada 50 m, luego, a partir del DEM con los perfiles
considerados en la capacidad de porteo, se calculó un perfil transversal con la herramienta “Terrain profile” de

QGis.

4.6.3 Condiciones de borde y configuración del modelo

Para las modelaciones realizadas se considera un régimen de escurrimiento mixto y/o supercrítico, considerando
como condición de borde aguas arriba altura crítica y aguas abajo altura normal en función de la pendiente local,

las cuales deben ser concordantes con los números de Froude obtenidos.

4.6.4 Coeficientes de rugosidad

Todos los atraviesos corresponden a cauces naturales de flujo intermitente en sectores áridos, cuyo coeficiente
de Manning es obtenido por el método de Cowan, en base a lo recomendado por la “Guía de presentación y
revisión técnica de proyectos de modificación de cauces naturales y artificiales”, DGA, 2016.

Dicho autor desarrolló un método sistemático para definir la rugosidad de Manning ( n ) como se describe en el
acápite 1.3.9 de la misma guía, donde se puede encontrar la siguiente fórmula y su descripción:

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) × m

n 0 = Valor básico del coeficiente de rugosidad para un tramo recto y uniforme.
n 1 = Incremento por irregularidades de las secciones.
n 2 = Incremento por variaciones de forma y dimensiones de las secciones.
n 3 = Incremento por obstrucciones.
n 4 = Incremento por vegetación en el cauce
m= Factor correctivo por curvas y meandros del río.

En la tabla 4-3 se indican los valores que adoptan los distintos términos según el procedimiento de Cowan.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Tabla 4-3: Velocidades Promedios de Flujo en m/s. (Departamento de Carreteras de Texas)

<!-- INICIO TABLA 4-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas 26 de junio de 2024 -->

**Tabla 4-3: Velocidades Promedios de Flujo en m/s. (Departamento de Carreteras de Texas)**

| Características de la canalización | Características | Valor medio del coeficiente<br>n. |
| --- | --- | --- |
| Material del lecho: n**0** | Tierra | 0,020 |
| Material del lecho: n**0** | Roca cortada | 0,025 |
| Material del lecho: n**0** | Grava fina | 0,024 |
| Material del lecho: n**0** | Grava gruesa | 0,028 |
| Grado de irregularidades: n**1** | Suaves | 0,000 |
| Grado de irregularidades: n**1** | Pocas | 0,005 |
| Grado de irregularidades: n**1** | Moderadas | 0,010 |
| Grado de irregularidades: n**1** | Severas | 0,020 |
| Variaciones de la sección: n**2** | Graduales | 0,000 |
| Variaciones de la sección: n**2** | Ocasionales | 0,005 |
| Variaciones de la sección: n**2** | Frecuentes | 0,010 - 0,015 |
| Obstrucciones: n**3** | Despreciables | 0,000 |
| Obstrucciones: n**3** | Pocas | 0,010 - 0,015 |
| Obstrucciones: n**3** | Muchas | 0,020 - 0,030 |
| Obstrucciones: n**3** | Severas | 0,040 - 0,060 |
| Vegetación: n**4** | Poca | 0,005 - 0,010 |
| Vegetación: n**4** | Regular | 0,010 - 0,025 |
| Vegetación: n**4** | Mucha | 0,025 - 0,050 |
| Vegetación: n**4** | Gran cantidad | 0,050 - 0,100 |
| Curvas: m | Pocas | 1,000 |
| Curvas: m | Regular | 1,050 |
| Curvas: m | Muchas | 1,100 |

<!-- Estadísticas: 22 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Pág. “Desing of Sedimentation Basing” Publication of National Research Council, Washington D.C. Junio 1980 Los valores asociados a la rugosidad de Manning escogidos y utilizados para la modelación hidráulica son considerados igual a 0,035 para todo el cauce, ya que no existen mayores diferencias entre los grados de -->
<!-- FIN TABLA 4-3 -->


|Características de la canalización|Características|Valor medio del coeficiente<br>n.|
|---|---|---|
|Material del lecho: n**0**|Tierra|0,020|
|Material del lecho: n**0**|Roca cortada|0,025|
|Material del lecho: n**0**|Grava fina|0,024|
|Material del lecho: n**0**|Grava gruesa|0,028|
|Grado de irregularidades: n**1**|Suaves|0,000|
|Grado de irregularidades: n**1**|Pocas|0,005|
|Grado de irregularidades: n**1**|Moderadas|0,010|
|Grado de irregularidades: n**1**|Severas|0,020|
|Variaciones de la sección: n**2**|Graduales|0,000|
|Variaciones de la sección: n**2**|Ocasionales|0,005|
|Variaciones de la sección: n**2**|Frecuentes|0,010 - 0,015|
|Obstrucciones: n**3**|Despreciables|0,000|
|Obstrucciones: n**3**|Pocas|0,010 - 0,015|
|Obstrucciones: n**3**|Muchas|0,020 - 0,030|
|Obstrucciones: n**3**|Severas|0,040 - 0,060|
|Vegetación: n**4**|Poca|0,005 - 0,010|
|Vegetación: n**4**|Regular|0,010 - 0,025|
|Vegetación: n**4**|Mucha|0,025 - 0,050|
|Vegetación: n**4**|Gran cantidad|0,050 - 0,100|
|Curvas: m|Pocas|1,000|
|Curvas: m|Regular|1,050|
|Curvas: m|Muchas|1,100|

Fuente: Pág. “Desing of Sedimentation Basing” Publication of National Research Council, Washington D.C. Junio 1980

Los valores asociados a la rugosidad de Manning escogidos y utilizados para la modelación hidráulica son
considerados igual a 0,035 para todo el cauce, ya que no existen mayores diferencias entre los grados de
irregularidades, obstrucciones y vegetación entre las riberas izquierda y derecha con el centro del cauce.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

# 5 RESULTADOS OBTENIDOS

##### 5.1 HIDROGRAFÍA Y CUENCAS DE INTERÉS

La caracterización de la hidrografía del sector de estudio se determinó por medio de la identificación de cauces
establecidos en las cartas IGM de escala 1:50.000, según lo especificado en la Resolución DGA N°135/2020. En
este caso, se observa que todos los cauces considerados en el sector de estudio corresponden a quebradas

endorreicas de escorrentía intermitente.

Luego, para definir las cuencas afluentes a los cauces de interés se consideró la visualización de imágenes
satelitales según herramienta de Google Earth Pro, las características de relieve del sector de estudio entregado
por los DEM aportados por el Cliente, el emplazamiento de las obras del Proyecto y la identificación de cauces
establecidos en las cartas IGM de escala 1:50.000. Posteriormente, la delimitación de cuencas se realizó

mediante la herramienta de delimitación incluido en el software QGis.

Este análisis permitió identificar cinco sectores de interés en los cuales existen cruces de cauces que podrían ser
afectados por las obras del Proyecto, los cuales se indican a continuación:

 - Sector 1: Cauce aledaño al sector de emplazamiento propuesto para la plataforma de portales de los

túneles de extracción.

 - Sector 2: Cauce cercano al emplazamiento propuesto para la estructura 110 de la LTE.

 - Sector 3: Cauce cercano al emplazamiento propuesto para las estructuras 81 y 89 de la LTE.

 - Sector 4: Cauce cercano al emplazamiento propuesto para la estructura 59 de la LTE.

 - Sector 5: Cauce cercano al emplazamiento propuesto para la instalación de faenas 23 E.

Aun cuando todos los cauces identificados en el sector de estudio corresponden a quebradas endorreicas de
escorrentía intermitente que se activan sólo ante eventos puntuales de precipitación, se observa que los cauces
cercanos a los Sectores 1, 2, 3 y 4 poseen secciones bien definidas y sus drenajes fluyen a zonas de acumulación
y/o infiltración que se ubican aguas abajo de estos sectores, por lo que se debe realizar su evaluación de
inundabilidad respecto de las obras que allí se proyectan.

Sin embargo, el cauce cercano al denominado Sector 5, está ubicado en una zona altamente intervenida
antrópicamente, con presencia de caminos, algunas instalaciones industriales y una vía férrea existentes. Ésta
última, delimita la zona de infiltración de aquel cauce endorreico, luego, los polígonos propuestos para las
instalaciones de faenas que se encuentran al sur de esta línea férrea no afectan tal cauce. Lo anterior, se presenta
en la Figura 5-1.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-1: Situación hidrográfica Sector 5

Así, los estudios hidrológicos e hidráulicos que se desarrollan a continuación evalúan la situación de
inundabilidad de los cruces de cauces con las obras del Proyecto que se emplazan en los Sectores 1, 2, 3 y 4.

En la Figura 5-2 se presentan las cuencas delimitadas para los sectores de interés y sus cauces correspondientes.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-2: Cuencas delimitadas para Estudio Hidrológico.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

En base a las cuencas delimitadas, se calcularon los parámetros morfométricos de cada una de ellas mediante la
utilización de herramientas SIG y las cartas IGM disponibles, obteniéndose los parámetros mínimos para una
buena definición de cada cuenca, como se establece en el acápite 2.2 del Manual de Cálculo de Crecidas y

Caudales mínimos en cuencas sin información Fluviométrica de la DGA.

A continuación, en la Tabla 5-1 se presentan los parámetros geomorfológicos más relevantes de las cuencas

determinadas.

Tabla 5-1: Parámetros Geomorfológicos Relevantes para determinación de caudales de crecidas

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A continuación, en la Tabla 5-1 se presentan los parámetros geomorfológicos más relevantes de las cuencas determinadas. -->

**Tabla 5-1: Parámetros Geomorfológicos Relevantes para determinación de caudales de crecidas**

| N° Cuenca | Área (km2) | L (km) | Lg (km) | H (m) | S (%) |
| --- | --- | --- | --- | --- | --- |
| 1 | 0,99 | 0,97 | 0,95 | 190 | 25,86 |
| 2 | 1,44 | 1,73 | 1,60 | 236 | 17,85 |
| 3 | 5,68 | 6,03 | 4,24 | 557 | 20,90 |
| 4 | 6,95 | 5,11 | 3,60 | 395 | 22,13 |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Donde: -->
<!-- FIN TABLA 5-1 -->


|N° Cuenca|Área (km2)|L (km)|Lg (km)|H (m)|S (%)|
|---|---|---|---|---|---|
|1|0,99|0,97|0,95|190|25,86|
|2|1,44|1,73|1,60|236|17,85|
|3|5,68|6,03|4,24|557|20,90|
|4|6,95|5,11|3,60|395|22,13|

Fuente: Elaboración propia.

Donde:

L : Longitud del cauce principal.
Lg : Longitud desde el centro de gravedad hasta el punto de salida de la cuenca.

H : Desnivel máximo de la cuenca.

S : Pendiente promedio de la cuenca.

##### 5.2 PRECIPITACIONES DE DISEÑO

Teniendo en cuenta la metodología especificada en la sección 4.2, a continuación, se presentan los resultados
del análisis de precipitaciones para el sector de estudio.

En este caso, las estaciones utilizadas corresponden a las denominadas estación Calama (DGA) y estación El Loa,
Calama Ad (DMC), las cuales presentan un extenso y muy completo registro de precipitaciones máximas en 24
hr, desde el año 1976 hasta el 2023, donde la estación Calama (DGA) presenta un vacío de registros para los años
1990 y 1991.

En la Figura 5-3 se presenta el análisis de consistencia de los datos de precipitaciones máximas en 24 hr para las
estaciones consideradas. En ella se observa que la resultante se asimila a una línea recta, sin cambios de
pendiente significativos, por lo que se puede suponer que no ha habido cambios en los métodos de observación

en la instalación de las estaciones en estudio.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-3: Curva másica o doble acumulada de precipitaciones

Para completar la estadística de precipitaciones máximas en 24 hr para la estación Calama (DGA)
correspondiente a los años 1991 y 1992, se utiliza el método de la curva másica. El análisis permite obtener los
datos corregidos y rellenados que se presentan en la Tabla 5-2, los cuales serán utilizados posteriormente en el

análisis de frecuencias.

Tabla 5-2: Resultados Pp máx 24 hr extendidas

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- correspondiente a los años 1991 y 1992, se utiliza el método de la curva másica. El análisis permite obtener los datos corregidos y rellenados que se presentan en la Tabla 5-2, los cuales serán utilizados posteriormente en el análisis de frecuencias. -->

**Tabla 5-2: Resultados Pp máx 24 hr extendidas**

| AÑO | El Loa (DMC) | Calama (DGA) |
| --- | --- | --- |
| **AÑO**<br> | **Precipitación (mm)** | **Precipitación (mm)** |
| 1976 | 9,9 | 6,0 |
| 1977 | 0,1 | 1,5 |
| 1978 | 0,0 | 0,0 |
| 1979 | 2,8 | 4,0 |
| 1980 | 0,0 | 0,0 |
| 1981 | 0,0 | 0,0 |
| 1982 | 1,2 | 0,5 |
| 1983 | 25,4 | 13,5 |
| 1984 | 11,0 | 5,2 |
| 1985 | 0,2 | 0,0 |
| 1986 | 2,6 | 1,5 |
| 1987 | 0,0 | 3,0 |

<!-- Estadísticas: 13 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas 26 de junio de 2024 -->
<!-- FIN TABLA 5-2 -->


|AÑO|El Loa (DMC)|Calama (DGA)|
|---|---|---|
|**AÑO**<br>|**Precipitación (mm)**|**Precipitación (mm)**|
|1976|9,9|6,0|
|1977|0,1|1,5|
|1978|0,0|0,0|
|1979|2,8|4,0|
|1980|0,0|0,0|
|1981|0,0|0,0|
|1982|1,2|0,5|
|1983|25,4|13,5|
|1984|11,0|5,2|
|1985|0,2|0,0|
|1986|2,6|1,5|
|1987|0,0|3,0|

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

|AÑO|El Loa (DMC)|Calama (DGA)|
|---|---|---|
|**AÑO**<br>|**Precipitación (mm)**|**Precipitación (mm)**|
|1988|1,7|3,1|
|1989|0,9|2,0|
|1990|0,0|0,7|
|1991|1,2|1,3|
|1992|22,2|7,5|
|1993|0,3|0,0|
|1994|0,1|0,0|
|1995|0,3|0,0|
|1996|6,4|3,5|
|1997|0,2|0,5|
|1998|2,3|0,5|
|1999|0,0|0,0|
|2000|3,3|1,5|
|2001|9,9|7,7|
|2002|9,7|3,7|
|2003|6,5|7,5|
|2004|0,5|0,5|
|2005|2,0|3,5|
|2006|5,0|0,5|
|2007|0,0|0,0|
|2008|0,0|0,0|
|2009|0,3|0,2|
|2010|0,8|0,0|
|2011|7,4|4,0|
|2012|2,6|4,0|
|2013|1,0|2,0|
|2014|3,0|4,4|
|2015|9,9|7,4|
|2016|4,6|0,3|
|2017|2,6|1,3|
|2018|3,0|3,5|
|2019|12,0|6,0|
|2020|10,6|1,1|
|2021|3,2|3,3|
|2022|1,2|2,8|
|2023|2,4|0,0|

Nota: Los valores destacados en amarillo corresponden a valores rellenados.

Fuente: Elaboración propia.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

En la Figura 5-4 y en Figura 5-5 se presentan los gráficos de los distintos ajustes de probabilidades para el análisis
de precipitaciones de las estaciones Calama (DGA) y El Loa (DMC), respectivamente.

Fuente: Elaboración propia.

Figura 5-4: Gráfico probabilidades de precipitación máxima diaria Estación Calama, DGA

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-5: Gráfico probabilidades de precipitación máxima diaria Estación Loa, DMC

En la Tabla 5-3 y en la Tabla 5-4 se presenta la matriz de resultados de los análisis de bondad de ajuste para las
distintas distribuciones de probabilidad utilizadas, para las estaciones Calama (DGA) y El Loa (DMC),
respectivamente.

Tabla 5-3:Resultados análisis de bondad de ajuste de distribuciones de probabilidad, Calama (DGA)

<!-- INICIO TABLA 5-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 5-3 y en la Tabla 5-4 se presenta la matriz de resultados de los análisis de bondad de ajuste para las distintas distribuciones de probabilidad utilizadas, para las estaciones Calama (DGA) y El Loa (DMC), respectivamente. -->

**Tabla 5-3: Resultados análisis de bondad de ajuste de distribuciones de probabilidad, Calama (DGA)**

| Distribución | X2 | Kolmogorov - Smirnov | Error Estándar de Ajuste |
| --- | --- | --- | --- |
| Gumbel | Rechazo r=1,48 | Acepta D=0,11 | 0,73 |
| Log Normal | Rechazo r=1,61 | Acepta D=0,14 | 0,98 |
| Normal | Rechazo r=1,43 | Acepta D=0,14 | 1,11 |
| Pearson III | Rechazo r=2,43 | Acepta D=0,10 | 0,65 |
| Log Pearson III | Rechazo r=2,43 | Acepta D=0,15 | 1,16 |
| Gamma | Rechazo r=2,43 | Acepta D=0,10 | 0,64 |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas -->
<!-- FIN TABLA 5-3 -->


|Distribución|X2|Kolmogorov - Smirnov|Error Estándar de Ajuste|
|---|---|---|---|
|Gumbel|Rechazo r=1,48|Acepta D=0,11|0,73|
|Log Normal|Rechazo r=1,61|Acepta D=0,14|0,98|
|Normal|Rechazo r=1,43|Acepta D=0,14|1,11|
|Pearson III|Rechazo r=2,43|Acepta D=0,10|0,65|
|Log Pearson III|Rechazo r=2,43|Acepta D=0,15|1,16|
|Gamma|Rechazo r=2,43|Acepta D=0,10|0,64|

Fuente: Elaboración propia.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Tabla 5-4:Resultados análisis de bondad de ajuste de distribuciones de probabilidad, El Loa (DMC)

<!-- INICIO TABLA 5-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas 26 de junio de 2024 -->

**Tabla 5-4: Resultados análisis de bondad de ajuste de distribuciones de probabilidad, El Loa (DMC)**

| Distribución | X2 | Kolmogorov - Smirnov | Error Estándar de Ajuste |
| --- | --- | --- | --- |
| Gumbel | Rechazo r=2,06 | Rechazo | 2,16 |
| Log Normal | Rechazo r=2,62 | Rechazo | 2,49 |
| Normal | Rechazo r=1,87 | Rechazo | 2,98 |
| Pearson III | Rechazo r=3,73 | Rechazo | - |
| Log Pearson III | Rechazo r=3,73 | Rechazo | 3,09 |
| Gamma | Rechazo r=3,73 | Rechazo | 1,41 |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Luego, en función del análisis de precipitaciones desarrollado, en la Tabla 5-5 se presentan los resultados de precipitaciones máximas en 24 hr para los periodos retorno de 2, 10 y 100 años para las estaciones -->
<!-- FIN TABLA 5-4 -->


|Distribución|X2|Kolmogorov - Smirnov|Error Estándar de Ajuste|
|---|---|---|---|
|Gumbel|Rechazo r=2,06|Rechazo|2,16|
|Log Normal|Rechazo r=2,62|Rechazo|2,49|
|Normal|Rechazo r=1,87|Rechazo|2,98|
|Pearson III|Rechazo r=3,73|Rechazo|-|
|Log Pearson III|Rechazo r=3,73|Rechazo|3,09|
|Gamma|Rechazo r=3,73|Rechazo|1,41|

Fuente: Elaboración propia.

Luego, en función del análisis de precipitaciones desarrollado, en la Tabla 5-5 se presentan los resultados de
precipitaciones máximas en 24 hr para los periodos retorno de 2, 10 y 100 años para las estaciones
meteorológicas analizadas.

Tabla 5-5:Evento de Precipitación (mm) máxima en 24 horas, según periodo de retorno

<!-- INICIO TABLA 5-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Luego, en función del análisis de precipitaciones desarrollado, en la Tabla 5-5 se presentan los resultados de precipitaciones máximas en 24 hr para los periodos retorno de 2, 10 y 100 años para las estaciones meteorológicas analizadas. -->

**Tabla 5-5: Evento de Precipitación (mm) máxima en 24 horas, según periodo de retorno**

| Distribución | Estación | T=2 (años) | T=10 (años) | T=100 (años) |
| --- | --- | --- | --- | --- |
| Gumbel | Calama | 1,7 | 6,9 | 12,9 |
| Gumbel | El Loa | 2,5 | 12,4 | 24,2 |
| Log Normal | Calama | 1,4 | 6,9 | 22,0 |
| Log Normal | El Loa | 1,5 | 12,0 | 57,6 |
| Normal | Calama | 2,1 | 6,5 | 9,7 |
| Normal | El Loa | 3,3 | 11,5 | 17,7 |
| Pearson III | Calama | 1,6 | 6,3 | 12,5 |
| Pearson III | El Loa | 1,9 | 10,9 | 25,3 |
| Log Pearson III | Calama | 1,3 | 6,9 | 24,0 |
| Log Pearson III | El Loa | 1,5 | 12,1 | 65,3 |
| Gamma | Calama | 1,6 | 6,3 | 12,5 |
| Gamma | El Loa | 1,9 | 10,9 | 25,3 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Teniendo en cuenta el ajuste probabilístico, los gráficos de distribución y la cercanía de las estaciones con el sector de estudio, se define que la estación más representativa corresponde a la estación Calama (DGA) y la -->
<!-- FIN TABLA 5-5 -->


|Distribución|Estación|T=2 (años)|T=10 (años)|T=100 (años)|
|---|---|---|---|---|
|Gumbel|Calama|1,7|6,9|12,9|
|Gumbel|El Loa|2,5|12,4|24,2|
|Log Normal|Calama|1,4|6,9|22,0|
|Log Normal|El Loa|1,5|12,0|57,6|
|Normal|Calama|2,1|6,5|9,7|
|Normal|El Loa|3,3|11,5|17,7|
|Pearson III|Calama|1,6|6,3|12,5|
|Pearson III|El Loa|1,9|10,9|25,3|
|Log Pearson III|Calama|1,3|6,9|24,0|
|Log Pearson III|El Loa|1,5|12,1|65,3|
|Gamma|Calama|1,6|6,3|12,5|
|Gamma|El Loa|1,9|10,9|25,3|

Fuente: Elaboración propia.

Teniendo en cuenta el ajuste probabilístico, los gráficos de distribución y la cercanía de las estaciones con el
sector de estudio, se define que la estación más representativa corresponde a la estación Calama (DGA) y la
distribución de probabilidad escogida es la Gumbel. Luego, los valores mostrados en la tabla anterior son
amplificados en un 13%, siguiendo la recomendación típica para pasar las precipitaciones máximas en 24 hr
(datos medidos) a precipitaciones máximas diarias (peak de precipitación real). Con lo anterior, se obtiene que
la precipitación de diseño, correspondiente a la precipitación de 100 años de período de retorno, es de 14,5 mm.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Tabla 5-6: Precipitación de diseño adoptada (mm)

<!-- INICIO TABLA 5-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas 26 de junio de 2024 -->

**Tabla 5-6: Precipitación de diseño adoptada (mm)**

| T=2 (años) | T=10 (años) | T=100 (años) |
| --- | --- | --- |
| 1,9 | 7,8 | 14,5 |

<!-- Estadísticas: 1 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. ##### 5.3 ESTIMACIÓN DE CAUDALES DE CRECIDAS -->
<!-- FIN TABLA 5-6 -->


|T=2 (años)|T=10 (años)|T=100 (años)|
|---|---|---|
|1,9|7,8|14,5|

Fuente: Elaboración propia.

##### 5.3 ESTIMACIÓN DE CAUDALES DE CRECIDAS

Siguiendo las consideraciones estipuladas en el numeral 4.5.1 para definir el coeficiente de escurrimiento (C) de
cada cuenca de análisis, se ha privilegiado únicamente la característica de relieve de cada sector de análisis, ya
que para la zona norte (y especialmente en zonas áridas) no es recomendable considerar aspectos de infiltración,
cobertura vegetal y almacenamiento superficial, ya que estos 3 aspectos restringen o disminuyen los caudales y
el escurrimiento superficial. Además, se han aplicado los factores de mayoración propuestos para la definición
del coeficiente de escorrentía asociado a altos períodos de retorno.

En la Tabla 5-7 se presentan los coeficientes de escurrimiento adoptados para cada sector de análisis.

Tabla 5-7: Coeficientes de escurrimiento (C) definidos

<!-- INICIO TABLA 5-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- el escurrimiento superficial. Además, se han aplicado los factores de mayoración propuestos para la definición del coeficiente de escorrentía asociado a altos períodos de retorno. En la Tabla 5-7 se presentan los coeficientes de escurrimiento adoptados para cada sector de análisis. -->

**Tabla 5-7: Coeficientes de escurrimiento (C) definidos**

| Coeficiente de escurrimiento, C | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Cuenca** | **T=2** | **T=10** | **T=100** |
| 1 | 0,08 | 0,08 | 0,10 |
| 2 | 0,16 | 0,16 | 0,20 |
| 3 | 0,12 | 0,12 | 0,15 |
| 4 | 0,10 | 0,10 | 0,13 |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Para la definición de los tiempos de concentración ( _tc_ ) de cada cuenca de análisis, se utilizaron los diferentes métodos propuestos, teniendo en consideración sus recomendaciones de aplicación. En la Tabla 5-8 se presenta -->
<!-- FIN TABLA 5-7 -->


|Coeficiente de escurrimiento, C|Col2|Col3|Col4|
|---|---|---|---|
|**Cuenca**|**T=2**|**T=10**|**T=100**|
|1|0,08|0,08|0,10|
|2|0,16|0,16|0,20|
|3|0,12|0,12|0,15|
|4|0,10|0,10|0,13|

Fuente: Elaboración propia.

Para la definición de los tiempos de concentración ( _tc_ ) de cada cuenca de análisis, se utilizaron los diferentes
métodos propuestos, teniendo en consideración sus recomendaciones de aplicación. En la Tabla 5-8 se presenta
el análisis para definición del _tc_ adoptado para cada cuenca de estudio.

Tabla 5-8: Determinación del tiempo de concentración, tc (min)

<!-- INICIO TABLA 5-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para la definición de los tiempos de concentración ( _tc_ ) de cada cuenca de análisis, se utilizaron los diferentes métodos propuestos, teniendo en consideración sus recomendaciones de aplicación. En la Tabla 5-8 se presenta el análisis para definición del _tc_ adoptado para cada cuenca de estudio. -->

**Tabla 5-8: Determinación del tiempo de concentración, tc (min)**

| Cuenca | Tiempo de Concentración, tc (min) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Cuenca** | **Texas Highways** | **Kirpich** | **Giandotti** | **U.S.SOIL** | **C.C.P.** | **tc adopt. (min)** |
| 1 | 15 | 10 | - | - | 10 | 10 |
| 2 | 27 | 12 | - | - | 13 | 12 |
| 3 | 94 | 29 | - | 40 | - | 35 |
| 4 | 80 | 25 | - | 38 | - | 35 |

<!-- Estadísticas: 5 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. De la tabla anterior, se observa que el método Texas Highways tiende a sobreestimar los tiempos de concentración, en comparación con los demás métodos. Por otra parte, la metodología de Giandotti no cumple -->
<!-- FIN TABLA 5-8 -->


|Cuenca|Tiempo de Concentración, tc (min)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Cuenca**|**Texas Highways**|**Kirpich**|**Giandotti**|**U.S.SOIL**|**C.C.P.**|**tc adopt. (min)**|
|1|15|10|-|-|10|10|
|2|27|12|-|-|13|12|
|3|94|29|-|40|-|35|
|4|80|25|-|38|-|35|

Fuente: Elaboración propia.

De la tabla anterior, se observa que el método Texas Highways tiende a sobreestimar los tiempos de
concentración, en comparación con los demás métodos. Por otra parte, la metodología de Giandotti no cumple
con los límites de validez de resultados del método, además que 3 de las 4 cuencas son mayores a las 100 ha
recomendadas para su aplicación. Así, los valores de tiempo de concentración adoptados para las distintas

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

cuencas de análisis se presentan en la última columna de la tabla anterior, correspondiendo a un promedio de
los métodos válidos para cada cuenca de análisis.

En la Tabla 5-9 se muestran los caudales de diseño adoptados para cada una de las cuencas de estudio, según la
metodología descrita en el numeral 4.5, correspondiente al Método Racional.

Tabla 5-9: Resumen de Caudales de Diseño Adoptados para distintos periodos de retorno.

<!-- INICIO TABLA 5-9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- los métodos válidos para cada cuenca de análisis. En la Tabla 5-9 se muestran los caudales de diseño adoptados para cada una de las cuencas de estudio, según la metodología descrita en el numeral 4.5, correspondiente al Método Racional. -->

**Tabla 5-9: Resumen de Caudales de Diseño Adoptados para distintos periodos de retorno.**

| Cuenca | Área | Intensidad de diseño (mm/hr) | Col4 | Col5 | Caudal (m3/s) | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **N°** | **Km2 ** | **T=2 (años)** | **T=10 (años)** | **T=100 (años)** | **T=2 (años)** | **T=10 (años)** | **T=100 (años)** |
| 1 | 0,99 | 0,70 | 2,80 | 5,24 | 0,02 | 0,06 | 0,14 |
| 2 | 1,44 | 0,58 | 2,33 | 4,37 | 0,04 | 0,15 | 0,35 |
| 3 | 5,68 | 0,57 | 2,29 | 4,28 | 0,11 | 0,43 | 1,01 |
| 4 | 6,95 | 0,57 | 2,29 | 4,28 | 0,11 | 0,44 | 1,03 |

<!-- Estadísticas: 5 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Siguiendo las recomendaciones especificadas en la Resolución DGA N°135/2020, la modelación hidráulica para evaluar las condiciones de inundabilidad de los cuatro sectores de cruces de cauces con las obras del Proyecto, -->
<!-- FIN TABLA 5-9 -->


|Cuenca|Área|Intensidad de diseño (mm/hr)|Col4|Col5|Caudal (m3/s)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**N°**|**Km2 **|**T=2 (años)**|**T=10 (años)**|**T=100 (años)**|**T=2 (años)**|**T=10 (años)**|**T=100 (años)**|
|1|0,99|0,70|2,80|5,24|0,02|0,06|0,14|
|2|1,44|0,58|2,33|4,37|0,04|0,15|0,35|
|3|5,68|0,57|2,29|4,28|0,11|0,43|1,01|
|4|6,95|0,57|2,29|4,28|0,11|0,44|1,03|

Fuente: Elaboración propia.

Siguiendo las recomendaciones especificadas en la Resolución DGA N°135/2020, la modelación hidráulica para
evaluar las condiciones de inundabilidad de los cuatro sectores de cruces de cauces con las obras del Proyecto,
será desarrollada con el caudal determinado para un período de retorno de 100 años, indicadas en la Tabla 5-10.

<!-- INICIO TABLA 5-10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Siguiendo las recomendaciones especificadas en la Resolución DGA N°135/2020, la modelación hidráulica para evaluar las condiciones de inundabilidad de los cuatro sectores de cruces de cauces con las obras del Proyecto, será desarrollada con el caudal determinado para un período de retorno de 100 años, indicadas en la Tabla 5-10. -->

**Tabla 5-10: Caudales de crecidas (m3/s) para modelación hidráulica.**

| Cuenca<br>N° | Área<br>Km2 | Q (m3/s)<br>crecida<br>T=100 (años) |
| --- | --- | --- |
| 1 | 0,99 | 0,14 |
| 2 | 1,44 | 0,35 |
| 3 | 5,68 | 1,01 |
| 4 | 6,95 | 1,03 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Los análisis y resultados del estudio hidrológico desarrollado se incluyen como archivo digital de esta consultoría, y forman parte del Apéndice A de este Informe. -->
<!-- FIN TABLA 5-10 -->


Tabla 5-10: Caudales de crecidas (m3/s) para modelación hidráulica.

|Cuenca<br>N°|Área<br>Km2|Q (m3/s)<br>crecida<br>T=100 (años)|
|---|---|---|
|1|0,99|0,14|
|2|1,44|0,35|
|3|5,68|1,01|
|4|6,95|1,03|

Fuente: Elaboración propia.

Los análisis y resultados del estudio hidrológico desarrollado se incluyen como archivo digital de esta consultoría,
y forman parte del Apéndice A de este Informe.

##### 5.4 MODELACIÓN HIDRÁULICA

En las siguientes figuras se presentan los ejes de cauces y la ubicación de los perfiles transversales definidos para
la confección de los modelos hidráulicos 1D en el software HEC-RAS, para cada sector de análisis, según la
metodología especificada en el numeral 4.6.2.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-6: Eje de cauce y perfiles transversales sector 1

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-7: Eje de cauce y perfiles transversales sector 2

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-8: Eje de cauce y perfiles transversales sector 3

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-9: Eje de cauce y perfiles transversales sector 4

La geometría e implementación de los 4 modelos hidráulicos desarrollados para análisis de inundabilidad (1 para
cada cuenca de estudio) es determinada a partir de los distintos DEM aportados por el Cliente, con los cuales se
construye un archivo TIN con ayuda de las herramientas incluidas en el software QGis 3.34.6, desde la cual se
extrae la geometría de cada perfil transversal definido y se desarrolla el modelo en el software HEC-RAS,
considerando aquella geometría, la definición del cauce y sus planicies de inundación, los coeficientes de
rugosidad adoptados, los caudales de crecidas determinados y las condiciones de borde establecidas para el

análisis en cada sector.

Los modelos hidráulicos desarrollados en el software HEC-RAS se incluyen como archivo digital de esta
consultoría y forman parte del Apéndice B de este Informe.

A continuación, desde la Tabla 5-11 a la Tabla 5-14 se presenta un resumen con los resultados obtenidos para la
modelación hidráulica de 100 años de período de retorno, para cada uno de los sectores de análisis.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico e Hidráulico de Crecidas

26 de junio de 2024 

|Perfil|Q<br>crecida<br>(m3/s)|Cota min<br>(msnm)|Cota E.H.<br>(msnm)|h<br>agua<br>(m)|Cota Crítica<br>(msnm)|L. Energía<br>(msnm)|Pérdida<br>(m/m)|Vel<br>(m/s)|Ancho inund<br>(m)|N° Froude|
|---|---|---|---|---|---|---|---|---|---|---|
|550|0,14|2784,40|2784,46|0,06|2784,46|2784,48|0,033854|0,58|6,54|0,97|
|500|0,14|2780,98|2781,02|0,04|2781,02|2781,03|0,034481|0,51|9,09|0,94|
|450|0,14|2777,74|2777,78|0,04|2777,79|2777,82|0,158473|0,91|6,84|1,93|
|400|0,14|2774,99|2775,02|0,03|2775,02|2775,03|0,036799|0,51|9,67|0,97|
|350|0,14|2771,22|2771,29|0,07|2771,31|2771,34|0,215356|1,02|6,37|2,23|
|300|0,14|2768,52|2768,58|0,06|2768,58|2768,6|0,032937|0,60|5,93|0,97|
|250|0,14|2765,69|2765,75|0,06|2765,78|2765,85|0,422206|1,37|5,07|3,09|
|200|0,14|2762,73|2762,79|0,06|2762,79|2762,81|0,033188|0,59|6,13|0,97|
|150|0,14|2758,99|2759,08|0,09|2759,12|2759,25|0,41094|1,85|2,34|3,29|
|100|0,14|2757,66|2757,73|0,07|2757,73|2757,75|0,029169|0,51|8,07|0,89|

Tabla 5-11: Resultados modelación hidráulica Sector 1 (T= 100 años)

<!-- INICIO TABLA 5-11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |250|0,14|2765,69|2765,75|0,06|2765,78|2765,85|0,422206|1,37|5,07|3,09| |200|0,14|2762,73|2762,79|0,06|2762,79|2762,81|0,033188|0,59|6,13|0,97| |150|0,14|2758,99|2759,08|0,09|2759,12|2759,25|0,41094|1,85|2,34|3,29| |100|0,14|2757,66|2757,73|0,07|2757,73|2757,75|0,029169|0,51|8,07|0,89| -->

**Tabla 5-11: Resultados modelación hidráulica Sector 1 (T= 100 años)**

| Perfil | Q<br>crecida<br>(m3/s) | Cota min<br>(msnm) | Cota E.H.<br>(msnm) | h<br>agua<br>(m) | Cota Crítica<br>(msnm) | L. Energía<br>(msnm) | Pérdida<br>(m/m) | Vel<br>(m/s) | Ancho inund<br>(m) | N° Froude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 450 | 0,35 | 2713,41 | 2713,53 | 0,12 | 2713,53 | 2713,56 | 0,031876 | 0,75 | 8,89 | 1,01 |
| 400 | 0,35 | 2710,17 | 2710,25 | 0,08 | 2710,27 | 2710,32 | 0,135587 | 1,20 | 7,47 | 1,95 |
| 350 | 0,35 | 2706,65 | 2706,74 | 0,09 | 2706,76 | 2706,81 | 0,119549 | 1,15 | 7,61 | 1,84 |
| 300 | 0,35 | 2703,07 | 2703,22 | 0,15 | 2703,23 | 2703,29 | 0,034663 | 1,13 | 3,12 | 1,15 |
| 250 | 0,35 | 2704,14 | 2704,30 | 0,16 | 2704,30 | 2704,34 | 0,02453 | 0,95 | 3,68 | 0,96 |
| 200 | 0,35 | 2697,76 | 2697,83 | 0,07 | 2697,86 | 2697,93 | 0,205466 | 1,40 | 7,04 | 2,37 |
| 150 | 0,35 | 2695,51 | 2695,60 | 0,09 | 2695,60 | 2695,63 | 0,028966 | 0,72 | 8,50 | 0,96 |
| 100 | 0,35 | 2692,76 | 2692,83 | 0,07 | 2692,86 | 2692,91 | 0,136806 | 1,21 | 7,38 | 1,96 |
| 50 | 0,35 | 2690,12 | 2690,21 | 0,09 | 2690,21 | 2690,23 | 0,03324 | 0,67 | 11,33 | 1,00 |
| 0 | 0,35 | 2686,27 | 2686,38 | 0,11 | 2686,42 | 2686,54 | 0,185279 | 1,75 | 3,67 | 2,40 |

<!-- Estadísticas: 10 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 5-12: Resultados modelación hidráulica Sector 2 (T= 100 años) Fuente: Elaboración propia a partir de modelación en HecRas. -->
<!-- FIN TABLA 5-11 -->


Fuente: Elaboración propia a partir de modelación en HecRas.

|Perfil|Q<br>crecida<br>(m3/s)|Cota min<br>(msnm)|Cota E.H.<br>(msnm)|h<br>agua<br>(m)|Cota Crítica<br>(msnm)|L. Energía<br>(msnm)|Pérdida<br>(m/m)|Vel<br>(m/s)|Ancho inund<br>(m)|N° Froude|
|---|---|---|---|---|---|---|---|---|---|---|
|450|0,35|2713,41|2713,53|0,12|2713,53|2713,56|0,031876|0,75|8,89|1,01|
|400|0,35|2710,17|2710,25|0,08|2710,27|2710,32|0,135587|1,20|7,47|1,95|
|350|0,35|2706,65|2706,74|0,09|2706,76|2706,81|0,119549|1,15|7,61|1,84|
|300|0,35|2703,07|2703,22|0,15|2703,23|2703,29|0,034663|1,13|3,12|1,15|
|250|0,35|2704,14|2704,30|0,16|2704,30|2704,34|0,02453|0,95|3,68|0,96|
|200|0,35|2697,76|2697,83|0,07|2697,86|2697,93|0,205466|1,40|7,04|2,37|
|150|0,35|2695,51|2695,60|0,09|2695,60|2695,63|0,028966|0,72|8,50|0,96|
|100|0,35|2692,76|2692,83|0,07|2692,86|2692,91|0,136806|1,21|7,38|1,96|
|50|0,35|2690,12|2690,21|0,09|2690,21|2690,23|0,03324|0,67|11,33|1,00|
|0|0,35|2686,27|2686,38|0,11|2686,42|2686,54|0,185279|1,75|3,67|2,40|

Tabla 5-12: Resultados modelación hidráulica Sector 2 (T= 100 años)

<!-- INICIO TABLA 5-12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |150|0,35|2695,51|2695,60|0,09|2695,60|2695,63|0,028966|0,72|8,50|0,96| |100|0,35|2692,76|2692,83|0,07|2692,86|2692,91|0,136806|1,21|7,38|1,96| |50|0,35|2690,12|2690,21|0,09|2690,21|2690,23|0,03324|0,67|11,33|1,00| |0|0,35|2686,27|2686,38|0,11|2686,42|2686,54|0,185279|1,75|3,67|2,40| -->

**Tabla 5-12: Resultados modelación hidráulica Sector 2 (T= 100 años)**

| Perfil | Q<br>crecida<br>(m3/s) | Cota min<br>(msnm) | Cota E.H.<br>(msnm) | h<br>agua<br>(m) | Cota Crítica<br>(msnm) | L. Energía<br>(msnm) | Pérdida<br>(m/m) | Vel<br>(m/s) | Ancho inund<br>(m) | N° Froude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 950 | 1,01 | 2653,01 | 2653,19 | 0,18 | 2653,20 | 2653,24 | 0,047988 | 1,07 | 13,44 | 1,28 |
| 900 | 1,01 | 2650,59 | 2650,78 | 0,19 | 2650,80 | 2650,83 | 0,048361 | 0,99 | 16,10 | 1,26 |
| 850 | 1,01 | 2648,13 | 2648,29 | 0,16 | 2648,30 | 2648,35 | 0,05102 | 1,08 | 13,71 | 1,31 |
| 800 | 1,01 | 2645,71 | 2645,88 | 0,17 | 2645,90 | 2645,95 | 0,057249 | 1,18 | 13,76 | 1,40 |
| 750 | 1,01 | 2643,07 | 2643,26 | 0,19 | 2643,27 | 2643,32 | 0,048107 | 1,09 | 12,76 | 1,29 |
| 700 | 1,01 | 2640,63 | 2640,83 | 0,20 | 2640,86 | 2640,93 | 0,053564 | 1,38 | 7,57 | 1,42 |
| 650 | 1,01 | 2638,21 | 2638,41 | 0,20 | 2638,44 | 2638,51 | 0,051132 | 1,45 | 6,55 | 1,42 |
| 600 | 1,01 | 2636,00 | 2636,23 | 0,23 | 2636,23 | 2636,28 | 0,03886 | 1,08 | 11,13 | 1,19 |
| 550 | 1,01 | 2633,66 | 2633,86 | 0,20 | 2633,88 | 2633,94 | 0,050691 | 1,22 | 9,87 | 1,34 |
| 500 | 1,01 | 2631,16 | 2631,33 | 0,17 | 2631,37 | 2631,43 | 0,049473 | 1,39 | 7,06 | 1,39 |
| 450 | 1,01 | 2629,05 | 2629,33 | 0,28 | 2629,35 | 2629,39 | 0,040069 | 1,08 | 11,16 | 1,19 |
| 400 | 1,01 | 2626,27 | 2626,56 | 0,29 | 2626,58 | 2626,64 | 0,068267 | 1,25 | 11,49 | 1,51 |
| 350 | 1,01 | 2623,86 | 2624,06 | 0,20 | 2624,09 | 2624,17 | 0,037305 | 1,44 | 5,18 | 1,25 |
| 300 | 1,01 | 2621,49 | 2621,78 | 0,29 | 2621,82 | 2621,92 | 0,055402 | 1,66 | 4,80 | 1,49 |
| 250 | 1,01 | 2619,21 | 2619,50 | 0,29 | 2619,54 | 2619,64 | 0,037983 | 1,68 | 3,39 | 1,27 |
| 200 | 1,01 | 2616,64 | 2616,92 | 0,28 | 2617,00 | 2617,18 | 0,065372 | 2,28 | 2,45 | 1,71 |
| 150 | 1,01 | 2614,72 | 2615,00 | 0,28 | 2615,00 | 2615,06 | 0,028428 | 1,13 | 7,83 | 1,07 |
| 100 | 1,01 | 2612,41 | 2612,72 | 0,31 | 2612,79 | 2612,90 | 0,072355 | 1,90 | 4,47 | 1,71 |
| 50 | 1,01 | 2610,48 | 2610,64 | 0,16 | 2610,64 | 2610,68 | 0,035144 | 0,90 | 17,25 | 1,09 |
| 0 | 1,01 | 2608,06 | 2608,25 | 0,19 | 2608,27 | 2608,32 | 0,077902 | 1,16 | 15,61 | 1,57 |

<!-- Estadísticas: 20 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 5-13: Resultados modelación hidráulica Sector 3 (T= 100 años) Fuente: Elaboración propia a partir de modelación en HecRas. -->
<!-- FIN TABLA 5-12 -->


Fuente: Elaboración propia a partir de modelación en HecRas.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

|Perfil|Q<br>crecida<br>(m3/s)|Cota min<br>(msnm)|Cota E.H.<br>(msnm)|h<br>agua<br>(m)|Cota Crítica<br>(msnm)|L. Energía<br>(msnm)|Pérdida<br>(m/m)|Vel<br>(m/s)|Ancho inund<br>(m)|N° Froude|
|---|---|---|---|---|---|---|---|---|---|---|
|950|1,01|2653,01|2653,19|0,18|2653,20|2653,24|0,047988|1,07|13,44|1,28|
|900|1,01|2650,59|2650,78|0,19|2650,80|2650,83|0,048361|0,99|16,10|1,26|
|850|1,01|2648,13|2648,29|0,16|2648,30|2648,35|0,05102|1,08|13,71|1,31|
|800|1,01|2645,71|2645,88|0,17|2645,90|2645,95|0,057249|1,18|13,76|1,40|
|750|1,01|2643,07|2643,26|0,19|2643,27|2643,32|0,048107|1,09|12,76|1,29|
|700|1,01|2640,63|2640,83|0,20|2640,86|2640,93|0,053564|1,38|7,57|1,42|
|650|1,01|2638,21|2638,41|0,20|2638,44|2638,51|0,051132|1,45|6,55|1,42|
|600|1,01|2636,00|2636,23|0,23|2636,23|2636,28|0,03886|1,08|11,13|1,19|
|550|1,01|2633,66|2633,86|0,20|2633,88|2633,94|0,050691|1,22|9,87|1,34|
|500|1,01|2631,16|2631,33|0,17|2631,37|2631,43|0,049473|1,39|7,06|1,39|
|450|1,01|2629,05|2629,33|0,28|2629,35|2629,39|0,040069|1,08|11,16|1,19|
|400|1,01|2626,27|2626,56|0,29|2626,58|2626,64|0,068267|1,25|11,49|1,51|
|350|1,01|2623,86|2624,06|0,20|2624,09|2624,17|0,037305|1,44|5,18|1,25|
|300|1,01|2621,49|2621,78|0,29|2621,82|2621,92|0,055402|1,66|4,80|1,49|
|250|1,01|2619,21|2619,50|0,29|2619,54|2619,64|0,037983|1,68|3,39|1,27|
|200|1,01|2616,64|2616,92|0,28|2617,00|2617,18|0,065372|2,28|2,45|1,71|
|150|1,01|2614,72|2615,00|0,28|2615,00|2615,06|0,028428|1,13|7,83|1,07|
|100|1,01|2612,41|2612,72|0,31|2612,79|2612,90|0,072355|1,90|4,47|1,71|
|50|1,01|2610,48|2610,64|0,16|2610,64|2610,68|0,035144|0,90|17,25|1,09|
|0|1,01|2608,06|2608,25|0,19|2608,27|2608,32|0,077902|1,16|15,61|1,57|

Tabla 5-13: Resultados modelación hidráulica Sector 3 (T= 100 años)

<!-- INICIO TABLA 5-13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |150|1,01|2614,72|2615,00|0,28|2615,00|2615,06|0,028428|1,13|7,83|1,07| |100|1,01|2612,41|2612,72|0,31|2612,79|2612,90|0,072355|1,90|4,47|1,71| |50|1,01|2610,48|2610,64|0,16|2610,64|2610,68|0,035144|0,90|17,25|1,09| |0|1,01|2608,06|2608,25|0,19|2608,27|2608,32|0,077902|1,16|15,61|1,57| -->

**Tabla 5-13: Resultados modelación hidráulica Sector 3 (T= 100 años)**

| Perfil | Q<br>crecida<br>(m3/s) | Cota min<br>(msnm) | Cota E.H.<br>(msnm) | h<br>agua<br>(m) | Cota Crítica<br>(msnm) | L. Energía<br>(msnm) | Pérdida<br>(m/m) | Vel<br>(m/s) | Ancho inund<br>(m) | N° Froude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 550 | 1,03 | 2563,75 | 2563,90 | 0,15 | 2563,90 | 2563,94 | 0,03 | 0,87 | 15,35 | 1,00 |
| 500 | 1,03 | 2561,79 | 2561,95 | 0,16 | 2561,98 | 2562,05 | 0,05 | 1,40 | 7,37 | 1,41 |
| 450 | 1,03 | 2560,07 | 2560,25 | 0,18 | 2560,25 | 2560,28 | 0,03 | 0,75 | 22,21 | 0,96 |
| 400 | 1,03 | 2558,09 | 2558,23 | 0,14 | 2558,26 | 2558,32 | 0,06 | 1,34 | 12,56 | 1,45 |
| 350 | 1,03 | 2556,22 | 2556,36 | 0,14 | 2556,36 | 2556,39 | 0,03 | 0,81 | 19,96 | 0,96 |
| 300 | 1,03 | 2554,17 | 2554,38 | 0,21 | 2554,41 | 2554,48 | 0,06 | 1,40 | 7,95 | 1,46 |
| 250 | 1,03 | 2552,35 | 2552,51 | 0,16 | 2552,52 | 2552,55 | 0,04 | 0,85 | 19,55 | 1,10 |
| 200 | 1,03 | 2550,25 | 2550,39 | 0,14 | 2550,40 | 2550,43 | 0,04 | 0,90 | 17,38 | 1,12 |
| 150 | 1,03 | 2547,99 | 2548,17 | 0,18 | 2548,19 | 2548,23 | 0,05 | 1,07 | 14,34 | 1,32 |
| 100 | 1,03 | 2546,72 | 2546,88 | 0,16 | 2546,88 | 2546,90 | 0,03 | 0,70 | 24,56 | 0,91 |
| 50 | 1,03 | 2544,47 | 2544,69 | 0,22 | 2544,73 | 2544,81 | 0,08 | 1,57 | 9,41 | 1,69 |
| 0 | 1,03 | 2542,49 | 2542,66 | 0,17 | 2542,66 | 2542,69 | 0,03 | 0,83 | 23,65 | 1,03 |

<!-- Estadísticas: 12 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 5-14: Resultados modelación hidráulica Sector 4 (T= 100 años) Fuente: Elaboración propia a partir de modelación en HecRas. -->
<!-- FIN TABLA 5-13 -->


Fuente: Elaboración propia a partir de modelación en HecRas.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

|Perfil|Q<br>crecida<br>(m3/s)|Cota min<br>(msnm)|Cota E.H.<br>(msnm)|h<br>agua<br>(m)|Cota Crítica<br>(msnm)|L. Energía<br>(msnm)|Pérdida<br>(m/m)|Vel<br>(m/s)|Ancho inund<br>(m)|N° Froude|
|---|---|---|---|---|---|---|---|---|---|---|
|550|1,03|2563,75|2563,90|0,15|2563,90|2563,94|0,03|0,87|15,35|1,00|
|500|1,03|2561,79|2561,95|0,16|2561,98|2562,05|0,05|1,40|7,37|1,41|
|450|1,03|2560,07|2560,25|0,18|2560,25|2560,28|0,03|0,75|22,21|0,96|
|400|1,03|2558,09|2558,23|0,14|2558,26|2558,32|0,06|1,34|12,56|1,45|
|350|1,03|2556,22|2556,36|0,14|2556,36|2556,39|0,03|0,81|19,96|0,96|
|300|1,03|2554,17|2554,38|0,21|2554,41|2554,48|0,06|1,40|7,95|1,46|
|250|1,03|2552,35|2552,51|0,16|2552,52|2552,55|0,04|0,85|19,55|1,10|
|200|1,03|2550,25|2550,39|0,14|2550,40|2550,43|0,04|0,90|17,38|1,12|
|150|1,03|2547,99|2548,17|0,18|2548,19|2548,23|0,05|1,07|14,34|1,32|
|100|1,03|2546,72|2546,88|0,16|2546,88|2546,90|0,03|0,70|24,56|0,91|
|50|1,03|2544,47|2544,69|0,22|2544,73|2544,81|0,08|1,57|9,41|1,69|
|0|1,03|2542,49|2542,66|0,17|2542,66|2542,69|0,03|0,83|23,65|1,03|

Tabla 5-14: Resultados modelación hidráulica Sector 4 (T= 100 años)

Fuente: Elaboración propia a partir de modelación en HecRas.

A continuación, desde la Figura 5-10 a la Figura 5-13 se muestran los resultados de eje hidráulico sobre los perfiles longitudinales representativos

de cada uno de los sectores modelados en HEC-RAS.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Fuente: Elaboración propia a partir de modelación en HecRas.

Figura 5-10: Perfil longitudinal cauce Sector 1, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Fuente: Elaboración propia a partir de modelación en HecRas.

Figura 5-11: Perfil longitudinal cauce Sector 2, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Fuente: Elaboración propia a partir de modelación en HecRas.

Figura 5-12: Perfil longitudinal cauce Sector 3, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Fuente: Elaboración propia a partir de modelación en HecRas.

Figura 5-13: Perfil longitudinal cauce Sector 4, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Finalmente, desde la Figura 5-14 a la Figura 5-17 se presentan los álveos de inundación para la crecida de 100
años de período de retorno para cada uno de los sectores modelados en HEC-RAS y su relación con el
emplazamiento de las obras proyectadas en cada sector.

Fuente: Elaboración propia.

Figura 5-14: Álveo de inundación Sector 1, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-15: Álveo de inundación Sector 2, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-16: Álveo de inundación Sector 3, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

Fuente: Elaboración propia.

Figura 5-17: Álveo de inundación Sector 4, periodo de retorno (T=100 años)

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

# 6 CONCLUSIONES

El análisis hidrológico desarrollado en el presente Informe ha permitido identificar 2 estaciones meteorológicas
en las cercanías del área del Proyecto, específicamente en las inmediaciones de la ciudad de Calama. Las series
estadísticas obtenidas para ambas estaciones muestran que el sector se caracteriza por presentar escasas
precipitaciones, incluso existiendo años en los cuales no ocurren lluvias, un rasgo distintivo y propio de los

sectores áridos.

Las series estadísticas presentan una larga data y son bastante completas, existiendo sólo 2 años sin información
para la estación Calama (DGA), la cual se considera como la más representativa del área de estudio, debido a que
forma parte de la misma cuenca de estudio, se encuentra muy cercana al área del Proyecto y forma parte de la
red hidrometeorológica de la Dirección General de Aguas (DGA), la cual corresponde a la infraestructura de
medición oficial para nuestro país.

En este caso, el análisis de frecuencias desarrollado para la serie estadística de la estación Calama se considera
adecuada, y se encuentra en el orden de magnitud de las precipitaciones máximas diarias de período de retorno
de 10 años para el sector, cercana a los 8 mm.

Por otra parte, el Método Racional, utilizado para el cálculo de los caudales de crecidas de las cuencas de estudio
mediante un análisis de precipitación-escorrentía, es el más recomendable para utilizar en el sector, ya que es el
método que mejor se ajusta a los resultados de análisis de frecuencias que se han desarrollado para el Norte
Grande de nuestro país y es uno de los métodos utilizables en cuencas pequeñas (menores a 25km [2] ) con mejor
representatividad. Además, el supuesto de que el escurrimiento máximo proveniente de una tormenta es
proporcional a la lluvia caída, se cumple de mejor manera en la medida que la magnitud de lluvia crece y el área
aportante se satura, tal como es el caso de las cuencas analizadas en el presente estudio.

Por otra parte, el desarrollo del modelo hidráulico en el software HEC-RAS es ampliamente utilizado en los
proyectos y estudios de crecidas en nuestro país. En este caso, las características geomorfológicas de las cuencas
de estudio han sido determinadas en una escala adecuada para el análisis, gracias a los modelos de elevación
digital aportados por el Cliente y desarrollados específicamente para los sectores de estudio.

Finalmente, los resultados de los álveos de inundación determinados, en relación con la disposición de las obras,
permiten indicar lo siguiente:

 - Sector 1 (ubicación plataforma de portales de túneles de extracción): En este caso, se observa que la

crecida de período de retorno de 100 años se desarrolla por el cauce identificado, con anchos de

inundación que varían entre los 2m y los 10m, aproximadamente, llegando a comprometer la zona

propuesta para el emplazamiento de la plataforma. Se recomienda desplazar el área propuesta, de

manera tal que el borde norte de esta plataforma se aleje unos 10m del álveo de inundación

determinado. Respecto de la sala eléctrica de los túneles de extracción emplazada al oriente de la

superficie definida para la plataforma, también se ve afectada por la crecida de diseño y el álveo de

inundación determinado, frente al perfil transversal 200, por lo que se recomienda desplazar la ubicación

propuesta para la sala eléctrica. Respecto de la estructura N°122 que se emplaza en el extremo

suroriente de la plataforma, ésta se encuentra aproximadamente a 10m de la mancha de inundación

determinada, por lo que no sería afectada por la crecida de diseño. Las estructuras N°121 y N°120, que

también se encuentran en el sector suroriente de la plataforma de portales de túneles de extracción se

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

encuentran a más de 20m de la mancha de inundación determinada para el Sector 1, por lo que no serían

afectadas por la crecida de período de retorno de 100 años.

 - Sector 2 (cruce de estructuras LTE N°108 a N°110): En este caso, se observa que la crecida de período de

retorno de 100 años se desarrolla por el cauce identificado, con anchos de inundación que varían entre

los 3m y los 11m, aproximadamente, y alturas de escurrimiento máximas de 16cm, llegando a

comprometer la estructura N°109 de la LTE que se proponen en el sector, por lo que se recomienda su

reubicación. En particular, la estructura N°108 se encuentra a más de 70m de distancia del álveo de

inundación determinado, mientras que la estructura N°110 se encuentra a más de 20m, por lo que no se

verían afectadas por la crecida de diseño.

 - Sector 3 (cruce de estructuras LTE N°87 a N°88 y cruce de estructuras LTE N°81 a N°82): En este caso, se

aprecia que la crecida de período de retorno de 100 años se desarrolla por el cauce identificado, con

anchos de inundación que varían entre los 2,5m y los 17,5m, aproximadamente, y alturas de

escurrimiento que varían entre 15cm y 30cm, sin llegar a comprometer las estructuras de la LTE que se

proponen en el sector. En particular, las estructuras N°87 y N°88 se emplazan a menos de 10m de la

mancha de inundación determinada para el sector, por lo cual, se recomienda su reubicación, de manera

que se ubiquen a no menos de 20m del álveo de inundación de 100 años de período de retorno.

 - Sector 4 (cruce de estructuras LTE N°58, 59 y 60): En este caso, se aprecia que la crecida de período de

retorno de 100 años se desarrolla por el cauce identificado, con anchos de inundación que varían entre

los 7m y los 25m, aproximadamente, con alturas de escurrimiento que no superan los 25cm, llegando a

comprometer la estructura N°59 de la LTE que se proponen en el sector, por lo que se recomienda su

reubicación. En particular, las estructuras N°58 y N°60 se encuentran a una distancia mayor a los 30m

respecto de la mancha de inundación determinada, razón por la cual no se verían afectadas por la crecida

de diseño.

 - Sector 5 (ubicación instalación de faenas polígono 23 E): Tal cómo se indicó en el capítulo 5.1, este sector

se encuentra altamente intervenido antrópicamente y la zona de infiltración de la quebrada intermitente

indicada en la cartografía IGM para este sector, se encuentra al norte de la línea férrea que se desarrolla

en aquella zona, luego, aquel cauce no se ve afectado por el emplazamiento de la instalación de faenas.

Sin embargo, como una medida de seguridad, se recomienda reubicar el polígono 23 E fuera del tramo

de cauce indicado en la cartografía IGM o su eliminación de las instalaciones para EECC.

Dados los resultados obtenidos en este estudio, el titular decidió modificar el emplazamiento de las obras
afectadas, en específico, el área de los portales de los túneles de extracción, la sala eléctrica de los túneles de
extracción, los postes de la línea eléctrica correspondientes a las estructuras N°122, N°121, N°120, N°119, N°110,
N°109, N°88, N°87 y N°59 y la eliminación del polígono asociado a la instalación de faenas denominada 23 E.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

En base a todo el análisis expuesto y desarrollado en el presente Informe, sumado a las modificaciones del _layout_
indicadas en el párrafo anterior, se puede señalar que los álveos de inundación asociados al estudio de crecidas
para un período de retorno de 100 años de todos los cruces de cauces identificados, no interfieren con los nuevos
emplazamientos propuestos para las obras y estructuras relacionadas con las líneas de transmisión eléctrica, la
plataforma de portales para los túneles de extracción, las salas eléctricas para túneles de extracción e inyección
y los polígonos referentes a las instalaciones de faenas incluidas en el proyecto Minero Chuquicamata
Subterráneo (PMCHS), en el marco de la DIA “Obras Complementarias y Ajustes Operacionales Mina
Chuquicamata Subterránea”.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

# 7 REFERENCIAS

Codelco, 2024. Anexo 9.A de Línea de Base Clima y Meteorología para Declaración de impacto ambiental

proyecto “Obras Complementarias y Ajustes Operacionales Mina Chuquicamata Subterránea”.

DGA-MOP, 2016. Guías Metodológicas para Presentación y Revisión Técnica de Proyectos de Modificación de

Cauces Naturales y Artificiales

DGA-MOP, 2014. Informe Técnico Inventario de Cuencas, Subcuencas y Subsubcuencas de Chile.

DGA-MOP, 1995. Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin Información Fluviométrica.

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 

# 8 APÉNDICES

**APÉNDICE A - HIDROLOGÍA**
**APÉNDICE B - MODELACIÓN HIDRÁULICA**

FLOW-COD007-REP-HID-001R0 Estudio Hidrológico y Modelación Hidráulico

26 de junio de 2024 