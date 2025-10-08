---
title: Microsoft Word - Anexo 1 Modelo olores.doc
author: Jorge
date: D:20200327205923-03'00'
language: es
type: report
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Anexo 1**

|Modelo de dispersión de olores Tabla de contenido|Pág.|
|---|---|
|1.‐ Introducción........................................................................................................................................|1|
|2.‐ Modelación matemática....................................................................................................................|2|
|3.‐ Modelo dispersivo Gaussiano...........................................................................................................|3|
|3.1.‐ Ecuaciones.................................................................................................................................|3|
|3.2.‐ Estimación del flujo de emisión.............................................................................................|5|
|3.3.‐ Estimación de los parámetros de dispersión........................................................................|7|
|3.4.‐ Características meteorológicas en San Felipe....................................................................|8|
|3.5.‐ Resultados de las simulaciones..............................................................................................|15|
|3.5.1.‐ Generación de olores para una fuente de 75 OUE/s..............................................|15|
|3.5.2.‐ Generación de olores para una fuente de 505 OUE/s............................................|17|
|3.5.3.‐ Generación de olor para una fuente de 935 OUE/s...............................................|20|
|3.5.4.‐ Comparación del impacto de fuentes de olor de 75, 505 y 935 OUE/s................|23|
|3.5.5.‐ Distancia de la fuente a la que se alcanza el umbral de olor bajo diferentes<br>condiciones...................................................................................................................|24|
|4.‐ Conclusiones........................................................................................................................................|27|

**Lista de tablas**

i

|No|Título|Pág.|
|---|---|---|
|1|Factores de emisión de olores para sistemas aeróbicos de tratamiento de aguas<br>residuales......................................................................................................|6|
|2|Fuentes de olor considerados en las simulaciones.................................................|7|
|3|Categorías de Pasquill de estabilidad de la atmósfera............................................|7|
|4|Fórmulas de Griffiths para los coeficientes de dispersión para suelos urbanos..............|8|
|5|Velocidad del viento en San Felipe.....................................................................|10|
|6|Dirección del viento en San Felipe (% del tiempo > a 1,6 km/h).................................|12|
|7|Resumen de estabilidad atmosférica en San Felipe................................................|15|
|8|Olor Vs. distancia para vientos medios anuales. Fuente de 75 OUE/s........................|15|
|9|Distanciaspara 1,0 OUE/m3 en función del viento para fuente de 75 OUE/s.................|17|
|10|Olor Vs. distancia para vientos medios anuales. Fuente de 505 OUE/s.......................|18|
|11|Distanciaspara 1,0 OUE/m3 en función del viento para fuente de 505 OUE/s...............|19|
|12|Resumen olor-distancia para promedios anuales. Fuente de 935 OUE/s.....................|20|
|13|Distanciaspara 1,0 OUE/m3 en función del viento para fuente de 935 OUE/s............... <br>|22|
|14|Distancia para 1 OUE/m~~3~~. Vientos promedios anuales.............................................|24|

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Lista de figuras**

ii

|No|Título|Pág.|
|---|---|---|
|1|Esquema gráfico de las categorías de estabilidad atmosférica de Pasquill........................|8|
|2|Distribución de la velocidad del viento en el año...................................................................|11|
|3|Curvas de probabilidad de excedencia de la velocidad del viento por mes.......................|11|
|4|Frecuencia (% del tiempo) de la dirección del viento por mes.............................................|14|
|5|Olor Vs. distancia para vientos medios anuales. Fuente 75 OUE/s......................................|16|
|6|Distancia para 1 OUE/m3 para vientos con diferentes probabilidades de excedencia y<br>por mes para fuente de 75 OUE/s.............................................................................................|17|
|7|Olor vs. Distancia para vientos medios anuales. Fuente 505 OUE/s....................................|18|
|8|Distancia para 1 OUE/m3 para vientos con diferentes probabilidades de excedencia y<br>por mes para fuente de 505 OUE/s...........................................................................................|19|
|9|Olor vs. Distancia para vientos medios anuales. Fuente 935 OUE/s....................................|21|
|10|Distancia para 1 OUE/m3 para vientos con diferentes probabilidades de excedencia y<br>por mes para fuente de 935 OUE/s...........................................................................................|22|
|11|Concentración de olor Vs. distancia para condiciones medias anuales, vientos con<br>probabilidad de excedencia de 10% y diferentes magnitudes de fuentes..........................|23|
|12|Concentración de olor Vs. distancia para condiciones medias anuales, vientos con<br>probabilidad de excedencia de 50% y diferentes magnitudes de fuentes..........................|23|
|13|Concentración de olor Vs. distancia para condiciones medias anuales, vientos con<br>probabilidad de excedencia de 90% y diferentes magnitudes de fuentes..........................|24|
|14|Distancia a la que la concentración de olor disminuye hasta el nivel umbral para<br>vientos con probabilidad de excedencia de 10%..............................................................|25|
|15|Distancia a la que la concentración de olor disminuye hasta el nivel umbral para<br>vientos con probabilidad de excedencia de 50%..............................................................|26|
|16|Distancia a la que la concentración de olor disminuye hasta el nivel umbral para<br>vientos con probabilidad de excedencia de 90% ....................................................................|26|

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**1.‐ Introducción**

Este documento responde a la observación No 14 a la Adenda 1 de la Declaración de Impacto Ambiental
**"** Modificación Planta de Tratamiento d e Residuos Industriales Líquidos a Sistema Lombrifiltro"
presentada por la empresa Exportadores del Agro S. A. en agosto de 2017. En efecto, la observación No
14 establece lo siguiente:

“Se reitera al titular, presentar los antecedentes técnicos respecto a la estimación de olor, eventual
generación de olores asociados a la fase de operación del proyecto, para lo cual se solicita observar
lo establecido en la Guía para la Predicción y Evaluación de Impactos de Olor en el SEIA, disponible
en el siguiente enlace:

https://www.sea.gob.cl/sites/default/files/imce/archivos/2018/01/24/guia_pye_impactos_por_olor.pdf

Considerando que existe un receptor a una distancia de 10 metros aproximadamente y que en el año
2018 se generó una denuncia a la SEREMI de Salud, por olores molestos hacia las instalaciones del
proyecto, **se debe** considerar realizar y presentar la modelación de dispersión de olores.”

De acuerdo con la Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA [1], se entiende por
olor la “sensación que ocurre cuando los compuestos o sustancias olorosas estimulan los receptores en
la cavidad nasal” (Schiffman y Williams, 2005). También, se incluye la definición del INN que establece
que el olor es la “propiedad organoléptica perceptible por el órgano olfativo cuando inspira
determinadas sustancias volátiles” (INN, 2010).

Las características e intensidad del olor a nivel de los eventuales afectados están determinadas por la
combinación de las características de la emisión, las condiciones atmosféricas y las condiciones de la
percepción. Dependiendo de las características e intensidad de la relación del afectado con la fuente de
olor y el tipo de zona en que se encuentra, es posible que este pueda percibir una molestia y,
eventualmente, dar lugar a una queja.

La emisión depende de las características del olor y de la forma como éste se libera hacia la atmósfera.
Las condiciones atmosféricas incluyen la estabilidad de la atmósfera, la velocidad y dirección del viento,
la humedad y la temperatura de aire.

En la misma publicación del SEA [1 ] se caracteriza el olor mediante los siguientes cuatro parámetros:

**“Concentración:** se entiende por concentración de olor al número de unidades de olor europeas en un
metro cúbico de gas en condiciones normales (OU E /m [3] ).

El umbral de detección (odour threshold) se refiere a la concentración teórica mínima para generar un
estímulo que pueda ser detectado en un porcentaje específico de la población; por convención
generalmente se usa el 50% de la población.

1 Servicio de Evaluación Ambiental, Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA, 2017.

1

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

La concentración de olor al umbral de detección es por definición 1 OU E /m [3], por consiguiente, la
concentración de olor se expresa como múltiplos del umbral de detección.

La concentración de un compuesto o sustancia olorosa se mide en unidades de masa/volumen como
μg/m [3], ppm o ppb. A las sustancias olorosas también se les puede asignar un umbral de detección en

función de su concentración.”

**“Intensidad:** se refiere a la fuerza con la que el olor se percibe, la cual aumenta en función de la
concentración del olor. Dicha intensidad no está relacionada directamente con la molestia, sino que es
un parámetro independiente de esta, es decir, se pueden tener intensidades altas de olor que no
producen molestia. La intensidad de un olor se determina mediante olfatómetros por panelistas
calibrados. La metodología para medir intensidad se describe en la norma técnica VDI 3882 Blatt1:1992‐
10 (VDI, 1992).”

**“Calidad:** indica como huele, permitiendo clasificar e identificar los olores en diversos grupos en función
de descriptores como floral, frutal, vegetal, medicinal, etc.
La calidad del olor normalmente es reportada usando listas de descriptores estandarizados que se
ilustran en las denominadas “ruedas de descriptores de olor”.

El olor asociado los sistemas de tratamiento de aguas residuales por lombrifiltros tiene características de
moho, tierra y humus, asociados a las geosminas, también presentes en el compostaje, debido a la
naturaleza similar del proceso. En particular, las aguas residuales del proceso de lavado de pasas
también tiene notas frutales y alcohólicas, por la presencia de azúcares provenientes de la uva y su
eventual descomposición.

**“Tono hedónico** (o aceptabilidad) **:** es la propiedad de un olor relativa a su agrado y desagrado, es decir,
es un juicio de categoría del placer o no placer relativo del olor y se refiere a las asociaciones mentales
hechas por el sujeto al percibirlo, en forma cualitativa (negativo o positivo) en una escala que va desde 4
(muy agradable) a ‐4 (muy desagradable) siendo el cero un olor neutral. La metodología para medir el
tono hedónico se describe en la norma alemana VDI 3882 Blatt 2:1994‐09 (VDI, 1994).”

**2.‐ Modelación matemática**

La predicción de impactos por emisiones de olor se realiza utilizando modelos. En la predicción de
impactos por emisiones de olor pueden considerarse dos grupos de modelos: modelos simples o
indicativos y modelos matemáticos complejos de dispersión atmosférica.

Los modelos simples o indicativos permiten determinar el potencial de percepción de olor en el
entorno de la ubicación del proyecto o actividad, por ejemplo mediante nomogramas que entregan
gráficamente el valor de la emisión de olor en función de la distancia a la que se estima
que existe una determinada concentración odorífera.

2

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

Los modelos de dispersión atmosférica integran las tasas de emisión del proyecto o actividad y las
variables meteorológicas del área de interés permitiendo estimar la concentración de olor en los

receptores.

De acuerdo con la Guía para el uso de modelos de calidad del aire del SEIA [2] los principales tipos de
modelos de dispersión son los denominados Gaussianos, Eulerianos, Langrangeanos y tipo “puff”.

Los modelos Gaussianos describen la distribución de una pluma bajo condiciones meteorológicas y de
emisiones estacionarias, en base a una distribución Gaussiana cuyos parámetros dependen de las
condiciones meteorológicas.

Los modelos Eulerianos traducen las leyes físicas y químicas relevantes a ecuaciones matemáticas de tipo
diferencial que se integran numéricamente en una grilla (o malla) tridimensional discretizada.

El concepto detrás de un modelo Lagrangeano consiste, en lugar de establecer ecuaciones diferenciales
en un sistema de coordenadas fijo en el espacio, en seguir matemáticamente la trayectoria de muchas
partículas en la atmósfera, tanto por fenómenos advectivos como dispersivos, de manera que la
integración de éstas. La combinación de las trayectorias de una gran cantidad de estas partículas permite
conocer su concentración y evolución en el tiempo.

Los modelos tipo “puff” esencialmente calculan la dispersión Gaussiana de contaminantes provenientes
de una emisión instantánea a lo largo de una trayectoria, o de una serie de emisiones instantáneas que

simula una emisión continua.

En este caso se utilizará un modelo de tipo Gaussiano, por ser el más ampliamente utilizado y requerir de
información disponible en relativa abundancia.

Para llevar a cabo la modelación es necesario contar con las tasas de emisión de las distintas fuentes del

proyecto, las cuales deben presentarse en OU E /s, la ubicación de éstas en relación a los puntos de interés
de las inmisiones y las condiciones atmosféricas de la zona afectada. Otros factores que pueden incidir
son la topografía, especialmente en relación a su capacidad de forzar las corrientes de aire en una
dirección o con características diferentes a las que existirían en una zona sin accidentes.

**3.‐ Modelo dispersivo Gaussiano**

**3.1.‐ Ecuaciones**

Son los más utilizados y se basan en la ecuación de dispersión ley de Fick que establece que el flujo de
masa en un sistema es proporcional al gradiente de concentraciones, denominándose coeficiente de
dispersión el que establece la proporcionalidad entre el flujo y el gradiente. La ecuación general del flujo
de contaminantes es la siguiente:

2 Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Servicio de Evaluación Ambiental. 2012.

3

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

∂ _C_ ∂ _C_ ∂ ∂ _C_ ∂ ∂ _C_
+ _U_ = ( _K_ _y_ ) + ( _K_ _z_ ) + _S_
∂ _t_ ∂ _x_ ∂ _y_ ∂ _y_ ∂ _z_ ∂ _z_

Cuya solución general es:

2

2

_C_ ( _x_, _y_, _z_ ) = 2 π _UG_ σ σ exp( − 2 _y_ σ 2 − 2 _z_ σ

( _x_, _y_, _z_ ) = 2 π _U_ σ σ exp( − 2 σ 2 − 2 σ 2 )

2

_x_ _z_ _y_ _z_

Para la condición en que la fuente está a nivel del suelo ( _z=0_ ) la ecuación anterior se transforma a

2

_C_ ( _x_, _y_ ) = _G_ exp( − _y_
π _U_ σ σ 2 σ

( _x_, _y_ ) = π _U_ σ σ exp( − 2 σ 2 )

_y_ _z_ _y_

En que

_**C(x,y)**_ es la concentración de olor ( OU E /m [3] ) a lo largo del eje _**x**_ longitudinal y el eje _**y**_ transversal al flujo
_**G**_ es el flujo de emisión de la fuente contaminante, en OU E /s
_**U**_ es la velocidad media del viento en m/s
_**σ**_ _**y**_ parámetro de dispersión en el sentido y (es una función de _**x**_ )
_**σ**_ _**z**_ parámetro de dispersión en el sentido z (es una función de _**x**_ )

En la última ecuación el término **exp** _**(- y**_ _**[2]**_ _**/2**_ σ _**y2**_ _**)**_ indica que el olor se distribuye a lo largo del eje _**y**_
(transversal al flujo de aire) como una función de Gauss, con un valor máximo igual a la unidad para _**y=0**_,
es decir, en el eje _**x**_, y con valores que tienden a _**0**_ a medida que se alejan de dicho eje. _**G/**_ π _**U**_ σ _**y**_ σ _**z**_
representa el máximo valor del olor a lo largo del eje x, en función de dicha variable. Los parámetros σ _**y**_ y
σ _**zy**_ son equivalentes a la desviación estándar de la distribución normal y representan la dispersión del
olor a lo largo de los ejes _**y**_ y _**z**_, respectivamente. Los coeficientes de dispersión son crecientes con la
distancia a la fuente de olor, lo que significa que a medida que se aleja el punto de cálculo de la fuente
de olor, se incrementa la dispersión de la concentración de éste y disminuyen los valores máximos y se
aumenta la distancia transversal en que se pueden percibir los olores. En el caso de olores normalmente
se considera que la fuente y los puntos de inmisión de interés se encuentran a nivel del suelo, por lo que
se considera el valor de _**z = 0**_ . En el sentido del eje _**z**_ (vertical) las máximas concentraciones de olor se
producen en _**z=0**_, es decir, a nivel del suelo y hacia arriba decrecen según el parámetro σ _**z**_ .

4

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**3.2.‐ Estimación del flujo de emisión**

**Factores de emisión**

Un factor de emisión es una relación entre la cantidad de contaminante emitido a la atmósfera por
unidad de tiempo y el nivel de actividad de la fuente. La unidad de actividad puede consistir en datos de
producción, horas de operación de la fuente por día, área superficial involucrada; o en datos como
número de empleados u otros (Radian Corporation, 1996). Es aconsejable el uso de factores de emisión
publicados por agencias estatales de protección del medio ambiente, normas técnicas o guías técnicas

relacionadas.

La ecuación general para la estimación de emisiones utilizando factores de emisión corresponde a:

_**G = A·F**_ _**E**_

Donde:

_**G**_ es el flujo de emisión de la fuente contaminante, en OU E /s emisiones;
_**A**_ es nivel de actividad;
_**F**_ _**E**_ = factor de emisión.

La fuente de olor se debe estimar en términos de producción de unidades de olor (OU) por unidad de
tiempo, típicamente, OU E /s. La forma más común de hacer esto, cuando no se cuenta con mediciones, es
mediante el uso de factores de emisión, típicamente en términos de unidades de olor por unidad de
superficie y de tiempo (OU E /m [2] ∙s), característicos de una actividad o instalación en particular, y que
multiplicado por la superficie que ocupa, permite estimar la fuente de olor en unidades de olor por
segundo.

Los factores de emisión de olor se encuentran en numerosas publicaciones internacionales,
principalmente para actividades productivas que emiten intensos olores, como la ganadería, mataderos,
etc., y otras como los sistemas de tratamiento de agua, lodos y sólidos orgánicos. Una búsqueda
intensiva de las fuentes de información disponibles en Internet no arrojó ningún resultado positivo para
sistema de tratamiento de aguas residuales mediante lombrifiltros. Sin embargo, es posible utilizar la
información disponible para sistemas de similar naturaleza biológica, como son los sistemas de
tratamiento de aguas residuales aeróbicos y los sistemas de compostaje de residuos sólidos orgánicos.

En la publicación **Legislación sobre Olores en los Países Bajos** de F. Montalván [3] **,** y en la Directriz
holandesa de emisión a la atmósfera [4] que es parte de la bibliografía digital contenida en el
Informe final de la Recopilación y Sistematización de Factores de Emisión al Aire, confeccionado por BS
Consultores para el Servicio de Evaluación Ambiental, se presentan factores de emisión para olores
generados desde la línea de agua de diferentes tipos de plantas de tratamiento de aguas residuales,

3 F. Montalván, **Legislación sobre Olores en los Países Bajos**, Facultad de Biología de la Universidad de Sevilla. 2009.
4 NeR c3s3‐G3 **Sewage Treatment Installations** . Informe final de Recopilación y Sistematización de Factores de Emisión al Aire.
Confeccionado por BS Consultores para el Servicio de Evaluación Ambiental. Abril 2003.

5

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

tanto de origen doméstico como industrial, los que se presentan en la tabla No 1. Aunque no se
presentan factores de emisión de olores generados por sistemas de lombrifiltros para el tratamiento de
aguas residuales, se ha considerado que el tratamiento aeróbico mediante aireación por burbujas podría
ser más o menos representativo del dicho sistema de tratamiento, dada su similitud en términos del uso
de oxígeno del proceso.

Los factores de emisión se presentan en función de la concentración de sólidos finos presentes en el
agua residual, expresados como kg DBO/kg sólidos secos‐día.

**Tabla No 1. Factores de emisión de olores para sistemas aeróbicos de tratamiento de aguas residuales**

|Tipo de tratamiento|Factor de emisión<br>(OU/s∙m2)<br>E|Condiciones|
|---|---|---|
|Línea de agua/estanque de aireación/zona<br>aeróbica/aireación por burbujas o aireación<br>en punto único totalmente cubierto o<br>aireación tipo "brush" totalmente cubierto<br>|0,20<br>0,35<br>0,65<br>1,05<br>1,65|0 ≤ S ≤ 0,05.<br>0,05 < S ≤ 0,10<br>0,10 < S ≤ 0,20<br>0,20 < S ≤ 0,30<br>S > 0,30|
|Línea de agua/estanque de aireación/zona<br>aeróbica/aireación en punto único sin<br>cobertura|0,30<br>0,55<br>1,0<br>1,6<br>2,5|0 ≤ S ≤ 0,05<br>0,05 < S ≤ 0,10<br>0,10 < S ≤ 0,20<br>0,20 < S ≤ 0,30<br>S > 0,30|

S = Contenido de limo del afluente (kg DBO/kg sólidos secos‐día).

En todo caso, se puede suponer que el factor de emisión de un sistema aeróbico está entre 0,2 y 2,5
OU E /s∙m [2] .

También existen referencias de factores de emisión para plantas de compostaje, pero éstas se presentan
en términos de generación de olor por unidad de producción de sólidos (OU E /Ton‐hora) por lo que no es
posible transformarlos directamente a sistemas de tratamiento de residuos líquidos [5,6,7,8] .

**Estimación de la fuente de olor**

Las emisiones de olor, en términos de OU E /s se pueden calcular como el producto del factor de emisión y
la superficie del sistema de tratamiento. En este caso, la unidad de tratamiento propiamente tal son los
lombrifiltros, cuya superficie es de 374 m [2] (10x22,4 + 10x15 m).

5 Australian Government, National Pollutant Inventory (NPI), " **Emission Estimation Technique for Sewage and Wastewater**
**Treatment** ", Version 2.1, junio 2011.
6 Netherlands Emission Guidelines for Air, Chapter 3. **3 Special Regulations for Specific Processes**, Section G.3 "Sewage
Treatment Installations, abril 2003".
7 EMEP/European Environment Agency. **Air Pollutant Emission Inventory Guidebook 2013**, EEA Technical Report No 12/2013,
Section 5.B.1 "Biological Treatment of Waste ‐ Composting".
8 **Compilation of Air Pollutant Emission Factors**, AP 42, Volume I, Stationary Point and Area Sources: Chapter 4, Section 4.3
“Waste Water Collection, Treatment and Storage", Septiembre 1991 (reformateado en Enero 1995)”. En Informe final de
Recopilación y Sistematización de Factores de Emisión al Aire confeccionado por BS Consultores para el Servicio de Evaluación

Ambiental. Abril 2003.

6

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

Considerando válida la hipótesis de que los factores de emisión de los olores generados por las unidades
de lombrifiltros son similares a las de sistemas aeróbicos de tratamiento de aguas residuales, se puede
suponer que éstos se encuentran entre _**0,2**_ y _**2,5**_ OU E /s∙m [2] .

Para los límites indicados, se puede estimar la fuente de olor asociada a los lombrifiltros entre 0,2
OU E /s∙m2 ∙ 374 m2 = _**75**_ **OU** **E** **/s** y 2,5 OU E /s∙m2 ∙ 374 m2 = _**935**_ **OU** **E** **/s** . Para efectos de los cálculos,
también se ha considerado una fuente de olor con un valor intermedio a los extremos calculados,
equivalente al promedio de ambos, de _**505**_ **OU** **E** **/s** . En la tabla No 2 se presentan los valores de fuentes

de olor considerados en las simulaciones.

**Tabla No 2. Fuentes de olor considerados en las simulaciones**

|Valor fuente (OU s)<br>E|Origen|
|---|---|
|75|Valor mínimo para tratamiento aeróbico según referencias 3 y 4.|
|505|Valor intermedio = promedio de los extremos|
|935|Valor máximo para tratamiento aeróbico según referencias 3 y 4|

**3.3.‐ Estimación de los parámetros de dispersión**

Los parámetros de dispersión σ dependen de la distancia de la fuente emisora (distancia _**x**_ ) y del nivel de
turbulencia o estabilidad de la atmósfera. Esta última se puede aproximar a través de las categorías de
Pasquill [9], que se presentan en la tabla No 3:

**Tabla No 3. Categorías de Pasquill de estabilidad de la atmósfera**

|Velocidad<br>del viento<br>(m/s)|Insolación diurna|Col3|Col4|Día o<br>noche|Condiciones nocturnas de<br>nubosidad|Col7|
|---|---|---|---|---|---|---|
|**Velocidad**<br>**del viento**<br>**(m/s)**|**Fuerte**|**Moderada**|**Débil**|**Cubierto**<br>**(8/8)**|**Seminublado**<br>**>4/8**|**Despejado**<br>**<3/8**|
|<2|A|A‐B|B|D|||
|2‐3|A‐B|B|C|D|E|F|
|3‐4|B|B‐C|C|D|D|E|
|4‐6|C|C‐D|D|D|D|D|
|>6|C|D|D|D|D|D|

**Categorías**

A Extremadamente inestable

B Moderadamente inestable

C Ligeramente inestable

D Condiciones neutras

E Ligeramente estable

F Moderadamente estable

9 **Modelización matemática de la contaminación por olores procedentes de explotaciones ganaderas en la Comunidad**

**Valenciana** . Universidad Politécnica de Valencia. 2018.

7

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

La estabilidad atmosférica correspondiente a las diversas categorías de Pasquill, se muestra
esquemáticamente en la figura No1 [10] .

**Figura No 1. Esquema gráfico de las categorías de estabilidad atmosférica de Pasquill**

Para suelos urbanos, los coeficientes de dispersión σ se pueden aproximar mediante las fórmulas de
Griffiths, en función de estabilidad atmosférica y de la distancia a los puntos de generación de olor, tal
como se presentan en la tabla No 4 [11] .

**Tabla No 4. Fórmulas de Griffiths para los coeficientes de dispersión para suelos urbanos**

|Estabilidad|σ<br>y|σ<br>z|
|---|---|---|
|A‐B|0,32 x (1 + 0,0004 x)~~‐1/2~~ <br>|0,24 x (1 + 0,0001 x)~~‐1/2~~|
|C|0,22 x (1 + 0,0004 x)~~‐1/2~~ <br>|0,20 x<br>|
|D|0,16 x (1 + 0,0004 x)~~‐1/2~~ <br>|0,14 x (1 + 0,0003 x)~~‐1/2~~ <br>|
|E‐F|0,11 x (1 + 0,0004 x)~~‐1/2~~|0,08 x (1 + 0,0015 x)~~‐1/2~~|

**3.4.‐ Características meteorológicas en San Felipe**

Para estimar las características climáticas en San Felipe, se utilizó la información contenida en la página de
internet https://es.weatherspark.com/y/26535/Clima‐promedio‐en‐San‐Felipe‐Chile‐durante‐todo‐el‐
a%C3%B1o, perteneciente a la empresa Weather Spark, que utiliza como fuentes originales mediciones
existentes e información satelital. A continuación se presenta un resumen de la información disponible, en
la que se ha hecho énfasis en las características del viento, por ser esta la variable más influyente en la
propagación de olores.

10 **Cálculo del alcance del olor.** Salvador Calvet Sanz - Ingeniería Ambiental en la Producción Animal. Departamento de Ciencia
Animal, Universidad Politécnica de Valencia.
11 **Dispersión de contaminantes atmosféricos: Modelo Gaussiano de la columna de humo** . Universidad Pablo Olavide, Sevilla.

8

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Temperatura**
De acuerdo con la referencia, en San Felipe los veranos son calientes, áridos y despejados y los inviernos
son fríos y parcialmente nublados. Durante el transcurso del año, la temperatura generalmente varía de
5 oC a 28oC y rara vez baja a menos de 0 oC y más de 31 oC.

**Nubes**

En San Felipe, el promedio del porcentaje del cielo cubierto con nubes varía _considerablemente_ en el
transcurso del año. La parte más despejada del año en San Felipe comienza aproximadamente a
mediados de octubre; dura 6,1 meses y se termina aproximadamente a fines de abril. A fines de enero se
produce el día más despejado del año, en que el cielo está despejado, mayormente
despejado o parcialmente nublado _el_ _92 %_ del tiempo y nublado o mayormente nublado el 8 % del
tiempo.

La parte más nublada del año comienza aproximadamente a fines de abril, dura 5,9 meses y se termina
aproximadamente a mediados de octubre. El día más nublado del año se produce a fines de mayo, el
cielo está nublado o mayormente nublado el 51 % del tiempo y despejado, mayormente despejado o
parcialmente nublado el 49 % del tiempo.

**Sol**

La duración del día en San Felipe varía considerablemente durante el año. En 2020, el día más corto es el
20 de junio, con 10 horas y 0 minutos de luz natural; el día más largo es el 21 de diciembre, con 14 horas
y 19 minutos de luz natural.

La salida del sol más temprana es a las 6:27 el 4 de diciembre, y la salida del sol más tardía es 1 hora y 58
minutos más tarde a las 8:25 el 9 de agosto. La puesta del sol más temprana es a las 17:43 el 10 de junio,
y la puesta del sol más tardía es 3 horas y 12 minutos más tarde a las 20:54 el 8 de enero.

Se observó el horario de verano (HDV) en San Felipe durante el 2020; comenzó en la primavera el 9 de
agosto y se terminó en el otoño el 9 de mayo.

**Humedad**

Basamos el nivel de comodidad de la humedad en el punto de rocío, ya que éste determina si el sudor se
evaporará de la piel enfriando así el cuerpo. Cuando los puntos de rocío son más bajos se siente más
seco y cuando son altos se siente más húmedo. A diferencia de la temperatura, que generalmente varía
considerablemente entre la noche y el día, el punto de rocío tiende a cambiar más lentamente, así es
que aunque la temperatura baje en la noche, en un día húmedo generalmente la noche es húmeda.

El nivel de humedad percibido en San Felipe, medido por el porcentaje de tiempo en el cual el nivel de
comodidad de humedad es bochornoso, opresivo o insoportable, no varía considerablemente durante el
año, y permanece prácticamente constante en 0 %.

**Viento**

La velocidad promedio del viento por hora en San Felipe tiene variaciones estacionales leves en el
transcurso del año. En la tabla No 5 y en la figura No 2 se muestra, para los diferentes meses del año, la

9

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

distribución anual de la velocidad promedio mensual y los rangos de velocidad máxima que se producen
entre el 25 y el 75% del tiempo y entre el 10 y 90% del tiempo (percentiles 50% superior y 80% superior).
En la figura No 3 se muestra las curvas de probabilidad de excedencia de las velocidades de los vientos
para cada mes del año.

La época más ventosa del año dura 4,8 meses, desde fines de octubre hasta mediados de marzo, con
velocidades promedio del viento que pueden superar los 3 metros por segundo. Los meses más ventosos
del año son diciembre y enero, con una velocidad promedio del viento de 3,28 metros por segundo.

El tiempo más calmado del año dura 7,2 meses, de mediados de marzo a fines de octubre. El mes más
calmado del año es mayo, con una velocidad promedio del viento de 2,25 metros por segundo.

En términos de probabilidad de excedencia, los vientos de menor velocidad, que son superados el 90%
del tiempo, son prácticamente uniformes a lo largo del año, del orden de 1 m/s. El rango de valores altos
de la velocidad del viento se amplía a lo largo del año a medida que diminuye su probabilidad de
excedencia, llegando para 90% al intervalo desde 3,4 m/s en julio hasta 6,3 m/s para en enero.

**Tabla No 5. Velocidad del viento en San Felipe**

10

|Mes|Promedio|Rango 10-90%|Col4|Rango 25-75%|Col6|
|---|---|---|---|---|---|
|**Mes**|**(m/s)**|**Inferior**|**Superior**|**Inferior**|**Superior**|
|Ene|3,28|1,1|6,3|1,5|5,3|
|Feb|2,86|1,1|6,1|1,5|5,0|
|Mar|2,78|1,1|5,4|1,5|4,2|
|Abr|2,44|1,0|4,6|1,5|3,3|
|May|2,25|1,0|3,8|1,5|2,8|
|Jun|2,31|1,1|3,6|1,6|2,8|
|Jul|2,31|1,0|3,4|1,5|2,8|
|Ago|2,33|1,0|3,9|1,5|2,9|
|Sep|2,44|0,9|4,4|1,4|3,3|
|Oct|2,78|0,9|5,3|1,4|4,2|
|Nov|3,06|1,0|5,9|1,5|4,8|
|Dic|3,28|1,1|6,2|1,5|5,3|

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Figura No 2. Distribución de la velocidad del viento en el año**

**Figura No 3.‐ Curvas de probabilidad de excedencia de la velocidad del viento por mes**

7,0

6,0

5,0

4,0

3,0

2,0

1,0

0,0

|Col1|Oct<br>Feb|Col3|
|---|---|---|
||Mar<br>Abr<br>||
||~~may~~<br>Jun<br>||
||~~Jul~~<br>Ago<br>~~Sep~~||
||Nov<br>~~Dic~~||
||Ene|Ene|
||||

0 10 20 30 40 50 60 70 80 90 100

**Probabilidad de excedencia (%)**

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

11

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

La dirección predominante promedio del viento en San Felipe varía durante el año de la forma como se
muestra en la tabla No 6 en que aparece, para cada mes, el porcentaje del tiempo en que ocurren
vientos superiores a 1,6 km/hr (0,44 m/s) asociado a cada dirección. El viento con más frecuencia viene
del Este durante el período de enero al octubre, con un porcentaje máximo del 36,9% en marzo. Si se
consideran las componentes NE, E y SE, se tiene un predominio de estas direcciones en los meses de
marzo a septiembre. Los vientos del Oeste y Sur Oeste predominan en los meses de verano, de
noviembre a febrero. Tanto los vientos del norte como del sur son de menor ocurrencia, con un
predominio de los primeros en los meses de invierno y de los segundos en los de verano.

**Tabla No 6. Dirección del viento en San Felipe (% del tiempo > a 1,6 km/h)**

12

|Mes|Norte|NE|Este|SE|Sur|SO|Oeste|NO|
|---|---|---|---|---|---|---|---|---|
|Enero|0,7|3,3|25,8|14,2|5,3|34,0|16,7|0,0|
|Febrero|1,3|3,3|32,4|10,9|2,7|32,0|17,3|0,0|
|Marzo|1,3|5,6|36,9|8,8|3,3|25,3|17,3|1,3|
|Abril|5,5|13,1|34,7|6,0|2,7|16,7|15,3|6,1|
|Mayo|13,3|21,3|30,0|4,0|2,0|9,3|8,7|11,3|
|Junio|16,7|26,7|28,7|2,7|2,7|4,7|5,3|12,7|
|Julio|18,0|22,7|30,7|1,3|3,3|5,7|5,6|12,7|
|Agosto|14,0|20,7|28,0|3,3|3,3|8,0|9,1|13,6|
|Septiembre|8,3|15,7|28,4|4,9|3,3|12,7|15,5|11,2|
|Octubre|4,0|10,7|28,7|7,3|2,7|17,3|21,3|8,0|
|Noviembre|2,0|7,3|28,4|9,6|2,7|22,7|22,0|5,3|
|Diciembre|1,3|4,7|26,7|11,7|4,3|30,7|19,3|1,3|
|**Promedios**|**7,2**|**12,9**|**29,9**|**7,1**|**3,2**|**18,3**|**14,5**|**7,0**|
|**Promedios**|**7,2**|**49,9**|**49,9**|**49,9**|**3,2**|**39,7**|**39,7**|**39,7**|

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

En la figura No 4 se muestra, para cada mes, la distribución del tiempo (%) en que el viento viene de las
diferentes direcciones de la rosa de los vientos. Se observa que hay dos claros patrones de distribución
de vientos. Uno es el correspondiente a los meses de verano (octubre a abril), en que las direcciones
predominantes son las correspondientes al Este, con sus componentes SE y NE, y la correspondiente al
Oeste, con su componente Sur Oeste. Típicamente en este período los vientos del Este se producen
durante la noche y los vientos del Oeste y Sur Oeste durante el día. El otro patrón de flujo ocurre en los
meses de invierno (mayo a septiembre) en que la dirección predominante sigue siendo la Este, con una
reducción de las componentes Oeste y Sur Oeste y un incremento de las componentes Nor Este, Norte y

Nor Oeste.

En términos de la velocidad del viento promedio, ésta disminuye levemente en los meses de invierno,
manteniéndose los vientos más bajos, asociados a los percentiles 10 y 25%, y disminuyendo los vientos
más altos, asociados a los percentiles 90 y 75%. Así, por ejemplo, los vientos con probabilidad de
excedencia de 90% se mantienen todo el año entre 0,9 y 1,1 m/s y los con probabilidad de excedencia de
75% entre 1,4 y 1,6 m/s. En cambio, los vientos más fuertes con probabilidad de excedencia de 10%
están en el rango 6,2‐6,3 m/s en enero‐diciembre y se reducen al rango 3,2‐3,4 m/s en junio‐julio.
Asimismo, los vientos con probabilidad de excedencia de 25% son del orden de 5,3 m/s en enero‐
diciembre y se reducen a 2,8 m/s en junio‐julio.

En términos de la estabilidad atmosférica en San Felipe, y considerando las categorías descritas por
Pasquill y que se presentan resumidamente en la tabla No 3 y en la figura No 1, es posible construir la
tabla No 7, en que se presenta las categorías correspondientes a cada mes para vientos con probabilidad
de excedencia de 10, 25, 50, 75, y 90%. SI bien no se cuenta con la estadística de los vientos con
probabilidad de excedencia 50%, se ha aproximado estos valores por las velocidades medias, lo cual es
matemáticamente correcto para una distribución de vientos simétrica, en que la mediana coincide con el

valor medio.

Para construir la tabla de estabilidad atmosférica de San Felipe se consideró que la insolación diurna es
**fuerte** en los meses cercanos al verano, entre noviembre y marzo, y débil en los meses de invierno, entre
junio y agosto. Para los meses característicos de la primavera y el otoño, más exactamente abril mayo,
septiembre y octubre, se asumió que la insolación diurna es **moderada** . En términos de la nubosidad
nocturna, se asumió que ésta corresponde a cielos despejados entre septiembre y abril y seminublados
entre mayo y agosto. De esta manera resultan estabilidades típicamente C y D para vientos con
velocidades altas y probabilidades de excedencia del orden de 10‐25% y estabilidades de los tipos A y B
para vientos más suaves con probabilidades de excedencia de sobre 75%. Para vientos medios, con
probabilidades de excedencia del orden de 50%, resultan estabilidades de los tipos B, C, E y F, con
variaciones a lo largo del año.

Las estabilidades que se presentan en la tabla No 7 se utilizaron para calcular los coeficientes de
dispersión σ _**y**_ y σ _**z**_, en función de la distancia a la fuente de olor, de acuerdo con las fórmulas de Griffiths
que se presentan en la tabla No 4. Cuando en una condición resultan dos o más categorías de estabilidad
atmosférica, se utilizó el promedio de los valores de los coeficientes de dispersión para todas las
categorías resultantes.

13

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Figura No 4. Frecuencia (% del tiempo) de la dirección del viento por mes**

14

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Tabla No 7.** **Resumen de estabilidad atmosférica en San Felipe**

|Mes|Insolación<br>diurna|Nubosidad<br>nocturna|Probabilidad de excedencia del viento|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Mes**|**Insolación**<br>**diurna**|**Nubosidad**<br>**nocturna**|**10%**|**25%**|**50%**|**75%**|**90%**|
|Ene|Fuerte|Despejado|C‐D|C‐D|B‐E|A|A|
|Feb|Fuerte|Despejado|C‐D|C‐D|A‐B‐F|A|A|
|Mar|Fuerte|Despejado|C‐D|C‐D|A‐B‐F|A|A|
|Abr|Moderada|Despejado|C‐D|B‐C‐E|B‐F|A‐B|A‐B|
|may|Moderada|Seminublado|B‐C‐D|B‐E|B‐E|A‐B|A‐B|
|Jun|Débil|Seminublado|C‐D|C‐E|C‐E|B|B|
|Jul|Débil|Seminublado|C‐D|C‐E|C‐E|B|B|
|Ago|Débil|Seminublado|C‐D|C‐E|C‐E|B|B|
|Sep|Moderada|Despejado|C‐D|B‐C‐E|B‐F|A‐B|A‐B|
|Oct|Moderada|Despejado|C‐D|C‐D|B‐F|A‐B|A‐B|
|Nov|Fuerte|Despejado|C‐D|C‐D|B‐E|A|A|
|Dic|Fuerte|Despejado|C‐D|C‐D|B‐E|A|A|

**3.5.‐ Resultados de las simulaciones**

Las ecuaciones presentadas en el punto 3.1, la estimación de las velocidades de los vientos, la definición
de condiciones de estabilidad atmosférica y la capacidad de generación de olor de las fuentes, permiten
estimar la concentración de olor en diversos puntos de inmisión, valores que se presentan a

continuación en diferentes formatos.

**3.5.1.‐ Generación de olores para una fuente de 75 OU** **E** **/s**

En la tabla número 8 y en la figura No 5 se presenta, para los vientos promedios anuales con
probabilidades de ocurrencia entre 10 y 90% y para una fuente de emisión estimada en 75 OU E /s, la
concentración de olor en función de la distancia. Se observa que para una distancia de aproximadamente
15 m se reduce la concentración de olor a valores cercanos a 1 OU E /m [3], definida como la concentración
umbral a la cual recién es posible percibir el olor. En la figura No 5 es posible percibir que la
concentración del olor se reduce rápidamente hasta unos 12 metros de la fuente y, a partir de esa
distancia, la reducción se hace más lenta.

**Tabla No 8. Olor Vs. distancia para vientos medios anuales. Fuente de 75 OU** **E** **/s**

|Viento<br>(%)|m/s|Estabilidad<br>aplicada|Distancia (m)|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Viento**<br>**(%)**|**m/s**|**Estabilidad**<br>**aplicada**|**5 **|**10**|**15**|**20**|**25**|
|10|4,9|C‐D|6,0|1,5|0,7|0,4|0,2|
|25|3,9|C‐D|7,6|1,9|0,8|0,5|0,2|
|50|2,7|B‐F|10,4|2,6|1,2|0,7|0,4|
|75|1,5|A|8,4|2,1|0,9|0,5|0,3|
|90|1,0|A‐B|12,0|3,0|1,3|0,8|0,5|

15

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

En la tabla No 9 y en la figura No 6 se muestra la distancia a la cual la concentración de olor se reduce al
valor umbral, de 1 OU E /m [3], para cada mes y para vientos con velocidades con probabilidades de
excedencia de entre 10 y 90 %, para la fuente estimada en 75 OU E /s. Por ejemplo, para los vientos
mayores, con probabilidad de excedencia de sólo 10%, la distancia a la cual la concentración olor se
reduce al valor umbral de 1 OU E /m [3] va entre 10,87 m, para el mes de enero, y 14,8 m, para el mes de
julio, con un promedio anual de 12,33 m. Para los vientos menores, con probabilidad de excedencia de
90%, la distancia a la cual la concentración olor se reduce al valor umbral de 1 OU E /m [3] va entre 16,74 m,
para los meses de enero, febrero, marzo y junio, y 18,76 m, para los meses de septiembre y octubre, con
un promedio anual de 17,37 m. Es notorio que los vientos de mayor velocidad producen una mayor
dilución de los olores emitidos por la fuente y una mayor dispersión transversal, por lo que generan
menores concentraciones de olor que los vientos más lentos. Asimismo, los vientos de mayor velocidad
presentan mayores variaciones y, por lo tanto, generan una mayor variación de las concentraciones de
olor, en cambio los vientos de menor velocidad son más uniformes y generan concentraciones de olor
poco variables.

**Fig. No 5. Olor Vs. distancia para vientos medios anuales. Fuente 75 OU** **E** **/s**

14

12

10

8

6

4

2

0

|10 C-D|Col2|Col3|
|---|---|---|
|10 C-D|10 C-D|10 C-D|
||25 C-D<br>~~50 B-F~~||
||75 A||
|90 A-B|90 A-B|90 A-B|
||||
||||
||||

5 7 9 11 13 15 17 19 21 23 25

**metros**

En la figura No 6 se presenta en forma gráfica la información contenida en la tabla No 9, pudiéndose
apreciar claramente que los vientos con probabilidades de excedencia de 10, 25 y 50% generan bastante
dispersión de las distancias a las cuales se produce la concentración de umbral de olor de 1 OU E /m [3], a lo
largo del año, en cambio los vientos con probabilidades de excedencia de 75 y 90% generan distancias
más uniformes a lo largo del año para la concentración de umbral de olor de 1 OU E /m [3] .

16

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Tabla No 9. Distancias** **para 1,0 OU** **E** **/m** **[3]** **en función del viento para fuente de 75 OU** **E** **/s**

|Mes|10%|Distancia*|25%|Distancia*|50%|Distancia*|75%|Distancia*|90%|Distancia*|
|---|---|---|---|---|---|---|---|---|---|---|
|Ene|6,3|10,87|5,3|11,79|3,28|14,59|1,5|14,40|1,1|16,74|
|Feb|6,1|11,01|5,0|12,18|2,86|13,41|1,5|14,27|1,1|16,74|
|Mar|5,4|11,67|4,2|13,30|2,78|13,61|1,5|14,40|1,1|16,74|
|Abr|4,6|12,76|3,3|13,90|2,44|16,91|1,5|14,54|1,0|17,65|
|May|3,8|11,85|2,8|15,70|2,25|17,63|1,5|14,40|1,0|17,41|
|Jun|3,6|14,33|2,8|19,36|2,31|21,26|1,6|14,14|1,1|16,74|
|Jul|3,4|14,80|2,8|19,17|2,31|21,26|1,5|14,40|1,0|17,64|
|Ago|3,9|13,81|2,9|18,99|2,33|21,13|1,5|14,54|1,0|17,65|
|Sep|4,4|12,92|3,3|13,84|2,44|16,90|1,4|14,68|0,9|18,16|
|Oct|5,3|11,85|4,2|13,34|2,78|15,85|1,4|14,97|0,9|18,16|
|Nov|5,9|11,22|4,8|12,39|3,06|15,12|1,5|14,40|1,0|17,64|
|Dic|6,2|10,91|5,3|11,85|3,28|14,59|1,5|14,40|1,1|17,17|
|Promedio|4,9|12,33|3,9|14,65|2,7|16,86|1,5|14,46|1,0|17,37|

- Distancia a la que la concentración del olor se reduce al umbral de 1,0 OU E /m ~~[3]~~

**Fig. No 6. Distancia para 1 OU** **E** **/m** **[3]** **para vientos con diferentes probabilidades de excedencia y por mes**
**para fuente de 75 OU** **E** **/s**

**3.5.2.‐ Generación de olores para una fuente de 505 OU** **E** **/s**

En la tabla número 10 y en la figura No 7 se presenta, para los vientos promedios anuales con
probabilidades de ocurrencia entre 10 y 90% y para una fuente de emisión estimada en 505 OU E /s, la
concentración de olor en función de la distancia. Se observa que para una distancia de entre 30 y 40 m se
reduce la concentración de olor a valores cercanos a 1 OU E /m [3], definida como la concentración umbral a
la cual recién es posible percibir el olor. En la figura No 7 es posible percibir que la concentración del olor

17

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

se reduce rápidamente hasta unos 15 metros de la fuente y, a partir de esa distancia, la reducción se

hace más lenta.

**Tabla No 10. Olor Vs. distancia para vientos medios anuales. Fuente de 505 OU** **E** **/s**

|Viento (%)|Col2|Distancia (m)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Viento (%)**|**Estabilidad**|**5 **|**10**|**15**|**20**|**25**|**30**|**40**|** 60**|**80**|
|10|C‐D|40,6|10,2|4,5|2,5|1,2|1,1|0,6|0,3|0,2|
|25|C‐D|51,1|12,8|5,7|3,2|1,5|1,4|0,8|0,4|0,2|
|50|B‐F|70,0|17,5|7,8|4,4|2,8|2,0|1,1|0,5|0,3|
|75|A|56,3|14,1|6,3|3,5|2,3|1,6|0,9|0,4|0,2|
|90|A‐B|81,0|20,2|9,0|5,1|3,2|2,3|1,3|0,6|0,3|

En la tabla No 11 y en la figura No 8 se muestra la distancia a la cual la concentración de olor se reduce al
valor umbral, de 1 OU E /m [3], para cada mes y para vientos con velocidades con probabilidades de
excedencia de entre 10 y 90 %, para la fuente estimada en 505 OU E /s. Por ejemplo, para los vientos
mayores, con probabilidad de excedencia de sólo 10%, la distancia a la cual la concentración olor se
reduce al valor umbral de 1 OU E /m [3] va entre 28,26 m, para el mes de enero, y 38,51 m, para el mes de
julio, con un promedio anual de 32,42m. Para los vientos menores, con probabilidad de excedencia de
90%, la distancia a la cual la concentración olor se reduce al valor umbral de 1 OU E /m [3] va entre 43,49 m,
para los meses de enero, febrero, marzo y junio, y 47,18 m, para los meses de septiembre y octubre, con
un promedio anual de 45,18 m. Tal como en el caso de la fuente de 75 OU E /S, los vientos de mayor
velocidad producen mayor dilución y dispersión transversal y, por lo tanto, menores concentraciones de
olor que los vientos más lentos. Asimismo, los vientos de mayor velocidad presentan mayores
variaciones y una mayor variación de las concentraciones de olor, en cambio los vientos de menor
velocidad son más uniformes y generan concentraciones de olor poco variables.

**Fig. No 7. Olor vs. Distancia para vientos medios anuales. Fuente 505 OU** **E** **/s**

90

80

70

60

50

40

30

20

10

0

|10 C-D|Col2|Col3|
|---|---|---|
|10 C-D|10 C-D|10 C-D|
||25 C-D<br>50 B-F||
||75 A<br>90 A-B||
||||
||||
||||
||||
||||
||||

5 15 25 35 45 55 65 75

**metros**

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

18

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Tabla No 11. Distancias** **para 1,0 OU** **E** **/m** **[3]** **en función del viento para fuente de 505 OU** **E** **/s**

|Mes|10%|Distancia*|25%|Distancia*|50%|Distancia*|75%|Distancia*|90%|Distancia*|
|---|---|---|---|---|---|---|---|---|---|---|
|**Ene**|6,3|28,26|5,3|30,67|3,28|38,06|1,5|37,42|1,1|43,49|
|Feb|6,1|28,64|5,0|31,68|2,86|34,91|1,5|37,08|1,1|43,49|
|Mar|5,4|30,35|4,2|34,60|2,78|35,43|1,5|37,42|1,1|43,49|
|Abr|4,6|33,19|3,3|36,20|2,44|44,12|1,5|37,77|1,0|45,85|
|may|3,8|30,83|2,8|40,96|2,25|46,01|1,5|37,42|1,0|45,23|
|Jun|3,6|37,30|2,8|50,56|2,31|55,55|1,6|36,75|1,1|43,49|
|Jul|3,4|38,51|2,8|50,06|2,31|55,55|1,5|37,42|1,0|45,85|
|Ago|3,9|35,94|2,9|49,57|2,33|55,22|1,5|37,77|1,0|45,85|
|Sep|4,4|33,61|3,3|36,05|2,44|44,12|1,4|38,14|0,9|47,18|
|Oct|5,3|30,83|4,2|34,71|2,78|41,37|1,4|38,89|0,9|47,18|
|Nov|5,9|29,18|4,8|32,22|3,06|39,43|1,5|37,42|1,0|45,85|
|Dic|6,2|28,38|5,3|30,83|3,28|38,06|1,5|37,42|1,1|44,63|
|Promedio<br>|4,8<br>|32,42<br>|3,8<br>|38,84<br>|2,6<br>|44,52<br>|1,5<br>|37,59|1,0|45,18|

- Distancia a la que la concentración de olor se reduce al umbral de 1=OU E /m ~~[3]~~

En la figura No 8 se presenta en forma gráfica la información contenida en la tabla No 11, pudiéndose
apreciar claramente que los vientos con probabilidades de excedencia de 10, 25 y 50% generan bastante
dispersión a lo largo del año de las distancias a las cuales se produce la concentración de umbral de olor
de 1 OU E /m [3], en cambio los vientos con probabilidades de excedencia de 75 y 90% generan distancias
más uniformes a lo largo del año para la concentración de umbral de olor de 1 OU E /m [3] .

**Figura No 8.** **Distancia para 1 OU** **E** **/m** **[3]** **para vientos con diferentes probabilidades de excedencia y por**
**mes para fuente de 505 OU** **E** **/s**

60

50

40

30

20

10

0

|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||Viento 10%<br>Viento 25%<br>Viento 50%||
|Viento 75%<br>Viento 90%|Viento 75%<br>Viento 90%|Viento 75%<br>Viento 90%|

Ene Feb Mar Abr may Jun Jul Ago Sep Oct Nov Dic

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

19

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**3.5.3.‐ Generación de olor para una fuente de 935 OUE/s**

En la tabla número 12 y en la figura No 9 se presenta, para los vientos promedios anuales con
probabilidades de ocurrencia entre 10 y 90% y para una fuente de emisión estimada en 935 OU E /s, la
concentración de olor en función de la distancia. Se observa que para una distancia de entre 40 y 60 m se
reduce la concentración de olor a valores cercanos a 1 OU E /m [3], definida como la concentración umbral a
la cual recién es posible percibir el olor. En la figura No 9 es posible percibir que la concentración del olor
se reduce rápidamente hasta unos 15 metros de la fuente y, a partir de esa distancia, la reducción se

hace más lenta.

En la tabla No 13 y en la figura No 10 se muestra la distancia a la cual la concentración de olor se reduce
al valor umbral, de 1 OU E /m [3], para cada mes y para vientos con velocidades con probabilidades de
excedencia de entre 10 y 90 %, para la fuente estimada en 935 OU E /s. Por ejemplo, para los vientos
mayores, con probabilidad de excedencia de sólo 10%, la distancia a la cual la concentración olor se
reduce al valor umbral de 1 OU E /m [3] va entre 38,50 m, para el mes de enero, y 52,50 m, para el mes de
julio, con un promedio anual de 44,19 m. Para los vientos menores, con probabilidad de excedencia de
90%, la distancia a la cual la concentración olor se reduce al valor umbral de 1 OU E /m [3] va entre 59,23 m,
para los meses de enero, febrero, marzo y junio, y 64,26 m, para los meses de septiembre y octubre, con
un promedio anual de 61,53 m. Tal como en el caso de las fuentes de 75 y de 505 OU E /s, los vientos de
mayor velocidad producen mayor dispersión transversal y menores concentraciones de olor que los
vientos más lentos. Asimismo, los vientos de mayor velocidad presentan mayores variaciones y una
mayor variación de las concentraciones de olor, en cambio los vientos de menor velocidad son más
uniformes y generan concentraciones de olor poco variables.

**Tabla No 12. Resumen olor-distancia para promedios anuales. Fuente de 935 OU** **E** **/s**

|Viento<br>(%)|Estabilidad<br>aplicada|Distancia (m)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Viento**<br>**(%)**|**Estabilidad**<br>**aplicada**|**5 **|**10**|**15**|**20**|**25**|**30**|**40**|**60**|**80**|** 100**|
|10|C‐D|75,2|18,8|8,4|4,7|2,2|2,1|1,2|0,5|0,3|0,2|
|25|C‐D|94,7|23,7|10,5|5,9|2,7|2,6|1,5|0,7|0,4|0,2|
|50|B‐F|129,6|32,5|14,5|8,2|5,2|3,6|2,1|0,9|0,5|0,3|
|75|A|104,2|26,1|11,6|6,5|4,2|2,9|1,6|0,7|0,4|0,3|
|90|A‐B|149,9|37,5|16,7|9,4|6,0|4,2|2,4|1,0|0,8|0,6|

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

20

90

80

70

60

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Fig. No 9. Olor vs. Distancia para vientos medios anuales. Fuente 935 OU** **E** **/s**

50

40

30

20

10

0

|10 C-D|Col2|Col3|Col4|
|---|---|---|---|
|10 C-D|10 C-D|10 C-D|10 C-D|
|||25 C-D<br>50 B-F||
|||75 A<br>90 A-B||
|||||
|||||
|||||
|||||
|||||
|||||

5 15 25 35 45 55 65 75

**metros**

En la figura No 10 se presenta en forma gráfica la información contenida en la tabla No 13, pudiéndose
apreciar que los vientos con probabilidades de excedencia de 10, 25 y 50% generan bastante dispersión
a lo largo del año de las distancias a las cuales se produce la concentración de umbral de olor de 1
OU E /m [3], en cambio los vientos con probabilidades de excedencia de 75 y 90% generan distancias más
uniformes a lo largo del año para la concentración de umbral de olor de 1 OU E /m [3] .

21

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Tabla No13. Distancias** **para 1,0 OU** **E** **/m** **[3]** **en función del viento para fuente de 935 OU** **E** **/s**

|Mes|10%|Distancia*|25%|Distancia*|50%|Distancia*|75%|Distancia*|90%|Distancia*|
|---|---|---|---|---|---|---|---|---|---|---|
|Ene|6,3|38,50|5,3|41,79|3,28|51,93|1,5|50,96|1,1|59,23|
|Feb|6,1|39,03|5,0|43,17|2,86|47,60|1,5|50,49|1,1|59,23|
|Mar|5,4|41,36|4,2|47,16|2,78|48,31|1,5|50,96|1,1|59,23|
|Abr|4,6|45,24|3,3|49,36|2,44|60,23|1,5|51,44|1,0|62,45|
|May|3,8|42,01|2,8|55,90|2,25|62,82|1,5|50,96|1,0|61,59|
|Jun|3,6|50,85|2,8|69,05|2,31|75,89|1,6|50,04|1,1|59,23|
|Jul|3,4|52,50|2,8|68,36|2,31|75,89|1,5|50,96|1,0|62,45|
|Ago|3,9|48,99|2,9|67,69|2,33|75,43|1,5|51,44|1,0|62,45|
|Sep|4,4|45,80|3,3|49,16|2,44|60,23|1,4|51,93|0,9|64,26|
|Oct|5,3|42,01|4,2|47,31|2,78|56,46|1,4|52,96|0,9|64,26|
|Nov|5,9|39,76|4,8|43,91|3,06|53,81|1,5|50,96|1,0|62,45|
|Dic|6,2|38,68|5,3|42,01|3,28|51,93|1,5|50,96|1,1|60,77|
|**Promedio**|4,9|43,57|3,8|48,93|2,6|57,56|1,5|51,16|1,0|61,39|

- Distancia a la que la concentración del olor se reduce al valor umbral de 1,0 OU E /m ~~[3]~~

**Fig. No 10. Distancia para 1 OU** **E** **/m** **[3]** **para vientos con diferentes probabilidades de excedencia y por**
**mes para fuente de 935 OU** **E** **/s**

80

70

60

50

40

30

20

10

0

|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
|Viento 10%|Viento 10%|Viento 10%|
|Viento 10%|Viento 10%|Viento 10%|
||Viento 25%<br>Viento 50%<br>~~Viento 75%~~||
|Viento 90%|Viento 90%|Viento 90%|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

22

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**3.5.4.‐ Comparación del impacto de fuentes de olor de 75, 505 y 935 OU** **E** **/s**

En las figuras números 11, 12 y 13 se presenta, para condiciones medias mensuales para vientos con
probabilidades de excedencia de 10, 50 y 90%, respectivamente, la variación de la concentración de olor
en función de la distancia a la fuente y en forma comparativa para los valores de fuentes consideradas,
de 75, 505 y 935 OU E /s.

**Fig. No 11. Concentración de olor Vs. distancia para condiciones medias anuales, vientos con**
**probabilidad de excedencia de 10% y diferentes magnitudes de fuentes**

|Viento 10%<br>160<br>75 OU/s<br>140<br>505 OU/s<br>935 OU/s<br>120<br>100<br>OU/m3<br>80<br>60<br>40<br>20<br>0<br>5 10 15 20 25 30 35 40 45 50 55 60<br>metros|Col2|
|---|---|
|**Viento 10%**<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>160<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>60<br>**metros**<br>**OU/m3**<br>75 OU/s<br>505 OU/s<br>935 OU/s||

|75 OU/s|Col2|Col3|
|---|---|---|
|75 OU/s|75 OU/s|75 OU/s|
||505 OU/s<br>935 OU/s||
||||
||||
||||
||||
||||
||||

**Fig. No 12. Concentración de olor Vs. distancia para condiciones medias anuales, vientos con**
**probabilidad de excedencia de 50% y diferentes magnitudes de fuentes**

|75 OU/s|Col2|Col3|
|---|---|---|
|75 OU/s|75 OU/s|75 OU/s|
||505 OU/s<br>935 OU/s||
||||
||||
||||
||||
||||
||||

|Viento 50%<br>160<br>75 OU/s<br>140<br>505 OU/s<br>935 OU/s<br>120<br>100<br>OU/m3<br>80<br>60<br>40<br>20<br>0<br>5 10 15 20 25 30 35 40 45 50 55 60<br>metros|Col2|
|---|---|
|**Viento 50%**<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>160<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>60<br>**metros**<br>**OU/m3**<br>75 OU/s<br>505 OU/s<br>935 OU/s||

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

23

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Fig. No 13. Concentración de olor Vs. distancia para condiciones medias anuales, vientos con**
**probabilidad de excedencia de 90% y diferentes magnitudes de fuentes**

|Viento 90%<br>160<br>75 OU/s<br>140 505 OU/s<br>935 OU/s<br>120<br>100<br>OU/m3<br>80<br>60<br>40<br>20<br>0<br>5 10 15 20 25 30 35 40 45 50 55 60<br>metros|Col2|
|---|---|
|**Viento 90%**<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>160<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>60<br>**metros**<br>**OU/m3**<br>75 OU/s<br>~~505 OU/s~~<br>935 OU/s||

|75 OU/s|Col2|
|---|---|
|~~505 OU/s~~<br>935 OU/s|~~505 OU/s~~<br>935 OU/s|
|||
|||
|||
|||
|||
|||

**3.5.5.‐ Distancia de la fuente a la que se alcanza el umbral de olor bajo diferentes condiciones**

En la tabla No 14 se presenta la distancia desde el centro de gravedad de la superficie de los lombrifiltros
a la que se generan una concentración de olor igual al umbral de 1 OU E /m [3], para los diferentes flujos de
emisión considerados y para diferentes condiciones atmosféricas. Estas últimas consideran vientos
medios anuales con diferentes probabilidades de excedencia. Como es de esperar, según los resultados
del modelo, la distancia hasta la cual se perciben los olores aumenta al aumentar la magnitud de la fuente
(flujos de emisión) y al aumentar la probabilidad de excedencia de la velocidad del viento. Esto último se
produce porque los vientos más lentos generan una menor dilución y dispersión de los olores y, por lo
tanto, una mayor concentración de éstos. Por otra parte, los vientos más lentos generan altas
concentraciones de olor al circunscribirlo a una zona de menores dimensiones que los vientos más
fuertes, en cambio estos últimos disminuyen la concentración máxima del olor, pero la distribuyen en una
zona de mayor amplitud. Por último, tal como se puede apreciar de las tablas y figuras que caracterizan el
viento, los vientos con velocidades cuya probabilidad de excedencia es de 90% tiene una muy baja
variabilidad a lo largo del año, por lo que los resultados calculados para las condiciones medias anuales
son también válidas para las condiciones que se generan a lo largo del año.

**Tabla No 14. Distancia para 1 OU** **E** **/m** **[3]** **. Vientos promedios anuales**

24

|Viento (%)|75 OU /s<br>E|505 OU /s<br>E|935 OU /s<br>E|
|---|---|---|---|
|10|12,29|31,98|43,57|
|25|13,79|35,90|48,93|
|50|16,16|42,16|57,56|
|75|14,46|37,57|51,16|
|90|17,34|45,08|61,39|

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

En las figuras No 14, 15 y 16 se presenta la distancia desde el centro de gravedad de los lombrifiltros a la
cual la concentración de olor disminuye hasta el nivel umbral, de 1 OU E /m [3], para diferentes flujos de
emisión y para vientos con probabilidad de excedencia de 10, 50 y 90%. Se observa que dicha distancia
va desde los 12,3 metros hasta los 61,4 metros, siendo la primera distancia la correspondiente a vientos
con 95% de probabilidad de excedencia y un flujo de emisión de 75 OU E /s. La distancia de 61,4 metros
corresponde a vientos lentos, con probabilidad de excedencia de 90%, y un flujo de emisión de 935
OU E /s, condición que corresponde a la más extrema de las simuladas. Si bien el viento 90% corresponde
a un valor medio anual, estos vientos tienen muy poca variabilidad, pudiendo reducirse a valores de 0,9
m/s en los meses de septiembre y octubre, para los cuales la distancia a la cual se percibe el olor
aumenta a sólo 64,3 metros, como se muestra en la tabla No 13.

En las mismas figuras se ha superpuesto dos diagramas de frecuencia de la dirección del viento
correspondiente uno a un mes representativo del patrón de vientos del verano y otro representativo del
patrón de vientos del invierno, orientados hacia el norte según la figura, de manera que permitan
determinar rápidamente las direcciones de los vientos predominantes. Como se muestra en la figura No
4, los patrones de dirección del flujo del viento son sumamente característicos y uniformes para los
períodos de verano e invierno.

En la figura No 14 se muestran en forma de círculos concéntricos las distancias a que, de acuerdo con las
simulaciones, alcanzan los olores antes de reducirse a la concentración umbral de 1 OU E /m [3], para los
vientos con probabilidad de excedencia de 10 % y para las diferentes magnitudes de la fuente de olor

consideradas.

**Fig. 14. Distancia a la que la concentración de olor disminuye hasta el nivel umbral para vientos con**
**probabilidad de excedencia de 10%**

25

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

**Fig. 15. Distancia a la que la concentración de olor disminuye hasta el nivel umbral para vientos con**
**probabilidad de excedencia de 50%**

**Fig. 16. Distancia a la que la concentración de olor disminuye hasta el nivel umbral para vientos con**
**probabilidad de excedencia de 90%**

26

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

Dentro del entorno de las figuras, se observa que existe sólo una vivienda, ubicada al poniente de la
planta de tratamiento de aguas residuales, que queda dentro de la zona con olores perceptibles para las
fuentes de 505 y de 935 UO E /s consideradas y cuya distancia mínima a la planta es de 10 metros
(distancia entre los puntos más cercanos de la vivienda y de la planta de tratamiento). El resto de las
edificaciones corresponde a bodegas o galpones industriales. Consultado el habitante de la vivienda
señalada [12], manifestó que no ha detectado olores molestos atribuibles a la operación de la planta de
tratamiento, lo cual puede ser explicado por lo siguiente:

a) La hipótesis de que el tratamiento por lombrifiltros genera muy pocos olores molestos hacia su

entorno.

b) La existencia de vientos predominantes desde el Oeste y Sur Oeste durante el día en los meses
de verano. Los vientos, también frecuentes, provenientes del Este y del Sur Este en estos mismos
meses se producen preferentemente en la noche, cuando la industria y la planta de tratamiento
no están en operación.
c) Los vientos predominantes en la época de invierno vienen del Este y Nor Este, principalmente
nocturnos, y diurnos del Norte y Nor Oeste.
d) La existencia de una pandereta de 2,2 metros de altura en todo el límite Oeste de la industria, lo
cual genera un barrera para la transmisión de olores en esa dirección.

Aparte de la vivienda indicada, no existen otras en la zona próxima a la planta de tratamiento de aguas
residuales y, de acuerdo con los resultados del modelo, bajo las peores condiciones de velocidad del
viento y estabilidad atmosférica la distancia la que es posible percibir los olores de la planta de
tratamiento no supera los 65 metros.

**4.‐ Conclusiones**

Se elaboró un modelo de dispersión de olores desde las planta de tratamiento de aguas residuales de la
planta San Felipe, de la empresa Exportadores del Agro S. A., según lo requerido en las observaciones a
la Adenda 1 a la DIA “Modificación Planta de Tratamiento de Residuos Industriales Líquidos a Sistema
Lombrifiltro". El modelo se basa en lo establecido en la Guía para la Predicción y Evaluación de Impactos
de Olor en el SEIA, y corresponde a uno de dispersión, del tipo Gaussiano, y considera la información
disponible de las características topográficas y meteorológicas del sector en cuestión.

Dada la inexistencia de factores de emisión de olores para sistemas de tratamiento mediante
lombrifiltros [13] se utilizó factores correspondientes a otros sistemas de tratamiento aeróbicos,
convencionales, debido a que existe cierta similitud entre estos procesos, lo que permitió hacer una
aproximación paramétrica a la valoración de las fuentes de olor.

12 Trabajador del predio agrícola ubicado al poniente de la industria, que ocupa una vivienda aislada dentro de dicho terreno.
13 Se hizo búsquedas exhaustivas en Internet, no encontrándose ningún factor de emisión de olores asociados a sistemas de
tratamiento por lombrifiltros. Probablemente esto se debe a que Chile es uno de los países precursores de la aplicación de
esta tecnología debido a la contribución de las investigaciones realizadas a partir de la década de 1990 por el profesor José
Tohá en el Departamento de Física de la facultad de Ciencias Físicas y Matemáticas de la Universidad de Chile.

27

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**

INGENIERÍA Y GESTIÓN DE SISTEMAS AMBIENTALES LTDA.

Para la planta de tratamiento de aguas residuales mediante lombrifiltros se utilizó los factores de
emisión mencionados para estimar la generación de olores entre 75 y 935 OU E /s, valores que fueron
utilizados para aplicados al modelo de dispersión Gaussiano para estimar la evolución del olor con la
distancia a la fuente, en función de la estabilidad atmosférica y la velocidad del viento.
También se estimaron las distancias, bajo diferentes condiciones atmosféricas, a las cuales se alcanza a
percibir el olor del lombrifiltro, información que se presenta en gráfica y tabular. Según esta información,
la máxima distancia a la cual el olor generado por los lombrifiltros, bajo la hipótesis que son válidos los
factores de emisión utilizados, es de 61,4 metros, valor que corresponde a una emisión de 935 OU E /s y
para una velocidad de viento con probabilidad de excedencia de 90%, equivalente a 1 m/s. Para
velocidades de viento mayores se genera una mayor dispersión de los olores y se alcanzan
concentraciones umbral (1 OU E /m [3] ) a distancias menores.

28

**General García 25, Depto. 31, Santiago, Chile, Fono-fax: (56-2) 696 2827**
**Web:** **www.ingesaltda.cl, E-Mail: jorgecastillo@ingesaltda.cl**