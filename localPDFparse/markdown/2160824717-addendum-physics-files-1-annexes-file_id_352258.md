---
title: Sin título
author: Diego Campos
date: D:20240429174138-04'00'
language: es
type: manual
pages: 41
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14 ANEXO 2.1 ESTUDIO DE INUNDACIÓN TR100 años ABRIL 2024 ELABORADO PARA
  - Tabla de contenido
-->

OENERGY MODELING

# PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14 ANEXO 2.1 ESTUDIO DE INUNDACIÓN TR100 años ABRIL 2024 ELABORADO PARA

[www.modeling.cl](http://www.modeling.cl/) [contacto@modeling.cl](mailto:contacto@modeling.cl)

OENERGY MODELING

# Tabla de contenido

**1** **INTRODUCCIÓN ........................................................................................................ 5**

**2** **OBJETIVOS ............................................................................................................... 6**

**3** **ANTECEDENTES ....................................................................................................... 7**

3.1 Á REA DE E STUDIO ................................................................................................ 8

3.2 V ISITA A T ERRENO ............................................................................................... 9

**4** **METODOLOGÍA ....................................................................................................... 10**

4.1 C ARACTERÍSTICAS G EOMORFOLÓGICAS DE LA C UENCA ....................................... 10

4.2 E STIMACIÓN DE P RECIPITACIONES DE C RECIDA ................................................... 11

_4.2.1_ _Análisis y Relleno de Datos ......................................................................................... 11_
_4.2.2_ _Análisis de Frecuencias en Precipitaciones ................................................................ 12_
_4.2.3_ _Consideración del efecto del Cambio Climático .......................................................... 14_
4.3 D ETERMINACIÓN DE LOS CAUDALES DE CRECIDA .................................................. 16

_4.3.1_ _Método Fórmula Racional ........................................................................................... 16_
_4.3.2_ _Transposición de Caudales ......................................................................................... 17_
_4.3.3_ _Hidrograma Unitario SCS ............................................................................................ 18_
4.4 M ODELACIÓN H IDRÁULICA .................................................................................. 19

_4.4.1_ _Topografía ................................................................................................................... 20_
_4.4.2_ _Coeficiente de Rugosidad ........................................................................................... 20_
_4.4.3_ _Geometría del Modelo ................................................................................................. 20_

_4.4.4_ _Método de cálculo HEC-RAS ...................................................................................... 22_
**5** **RESULTADOS ......................................................................................................... 23**

5.1 C ARACTERÍSTICAS G EOMORFOLÓGICAS DE LAS C UENCAS A PORTANTES ............... 23

5.2 E STIMACIÓN DE PRECIPITACIONES DE C RECIDA .................................................... 25

_5.2.1_ _Análisis de Frecuencia de precipitaciones .................................................................. 29_
_5.2.2_ _Consideración del Efecto del Cambio Climático ......................................................... 30_
5.3 D ETERMINACIÓN DE LOS C AUDALES DE C RECIDA ................................................. 31

_5.3.1_ _Método Fórmula Racional ........................................................................................... 31_
_5.3.2_ _Transposición de Caudales ......................................................................................... 32_
_5.3.3_ _Hidrograma Unitario SCS ............................................................................................ 32_
5.4 M ODELACIÓN H IDRÁULICA .................................................................................. 33

_5.4.1_ _Topografía ................................................................................................................... 33_
_5.4.2_ _Coeficiente de Rugosidad ........................................................................................... 34_
_5.4.3_ _Condiciones de borde .................................................................................................. 34_

_5.4.1_ _Geometría del Modelo ................................................................................................. 35_

_5.4.2_ _Resultados Modelación ............................................................................................... 36_
**6** **ANÁLISIS ................................................................................................................. 39**

**7** **CONCLUSIONES ..................................................................................................... 40**

**8** **BIBLIOGRAFIA ........................................................................................................ 41**

**9** **APENDICE ............................................................................................................... 41**

2
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**Tabla de Figuras**

F IGURA 1.1 U BICACIÓN DEL P ROYECTO F UENTE : E LABORACIÓN P ROPIA, MODELING 2024. ............ 6

F IGURA 3.1 C ARTOGRAFÍA IGM A RICA (A-012) ................................................................................ 7

F IGURA 3.2 Á REA DE E STUDIO .................................................................................................... 8

F IGURA 3.3 I MAGEN DE CAUCE EN ESTUDIO ...................................................................................... 9

F IGURA 3.4 I MAGEN DE CAUCE EN ESTUDIO .................................................................................... 10

F IGURA 4.1 S ECTORIZACIÓN DE PROYECCIONES DE PRECIPITACIÓN C AMBIO C LIMÁTICO ................................. 15

F IGURA 4.2 E JEMPLO DE MALLA HEC-RAS 2D ................................................................................ 21

F IGURA 5.1 C UENCA A PORTANTE Y P UNTO DE C ONTROL ..................................................................... 23

F IGURA 5.2 U BICACIÓN E STACIONES M ETEOROLÓGICAS DGA .............................................................. 25

F IGURA 5.3 P RECIPITACIONES MÁXIMAS EN 24 HORAS ANUALES DISPONIBLES EN E STACIONES DGA .................. 28

F IGURA 5.4 A NÁLISIS DE FRECUENCIAS ESTACIÓN A RICA O FICINA ........................................................... 29

F IGURA 5.5 C OMPARACIÓN ESCENARIOS PRECIPITACIÓN MÁXIMA ANUAL EN 24 HRS .................................... 30

F IGURA 5.6 H IDROGRAMA TR100 AÑOS SCS Q UEBRADA S/N.............................................................. 33

F IGURA 5.7 R EPRESENTACIÓN DE T OPOGRAFÍA P ROYECTO ................................................................... 34

F IGURA 5.8 M ALLA DE MODELO HEC-RAS 2D ................................................................................ 35

F IGURA 5.8 C OMPARATIVA I NUNDACIÓN TR100 AÑOS Y TR100 AÑOS CON C AMBIO C LIMÁTICO
MODELO HEC-RAS 2D ...................................................................................................... 37

F IGURA 5.9 P ROFUNDIDAD TR100 AÑOS MODELO Q UEBRADA S/N HEC-RAS 2D ................. 38

F IGURA 5.10 V ELOCIDAD TR100 AÑOS MODELO Q UEBRADA S/N HEC-RAS 2D .................... 38

F IGURA 6.1 C AMBIO DE EMPLAZAMIENTO DE LTE P ROYECTO SEGÚN I NUNDACIÓN TR 100 AÑOS

........................................................................................................................................ 39

3
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**Tabla de Cuadros**

C UADRO 4.1 V ALORES DE CAMBIO PORCENTUAL ESPERADO DE PRECIPITACIÓN SEGÚN
ZONIFICACIÓN CON RESPECTO AL PERIODO HISTÓRICO ........................................................ 15

C UADRO 4.2 C OEFICIENTES DE ESCORRENTÍA PARA T = 10 AÑOS ........................................................... 17

C UADRO 5.1 C OORDENADAS P UNTOS DE C ONTROL ........................................................................... 24

C UADRO 5.2 C ARACTERÍSTICAS M ORFOLÓGICAS DE LAS C UENCAS A PORTANTES ......................................... 24

C UADRO 5.3 U BICACIÓN DE ESTACIONES METEOROLÓGICAS SELECCIONADAS ............................................. 25

C UADRO 5.4 P RECIPITACIONES MÁXIMAS EN 24 HORAS ANUAL DISPONIBLES ............................................. 26

C UADRO 5.5 R ESUMEN DE D ISTRIBUCIÓN A DOPTADA ........................................................................ 29

C UADRO 5.6 R ESUMEN DE P RECIPITACIONES A DOPTADAS ................................................................... 30

C UADRO 5.7 R ESUMEN DE P RECIPITACIONES C ALCULADAS CONSIDERANDO CC P25 Y P75 ............................ 30

C UADRO 5.8 C ÁLCULO COEFICIENTE DE ESCORRENTÍA ........................................................................ 31

C UADRO 5.9 E STIMACIÓN DE C AUDALES DE C RECIDA PARA DIFERENTES T M ÉTODO R ACIONAL MC V OL .3 .......... 31

C UADRO 5.10 R ESULTADOS T RANSPOSICIÓN DE C AUDALES ................................................................. 32

C UADRO 5.11 R ESULTADOS H IDROGRAMA U NITARIOS SCS ................................................................. 32

C UADRO 5.12 C OEFICIENTE D E R UGOSIDAD M ANNING S EGÚN C OWAN .................................................. 34

C UADRO 5.13 C ONDICIÓN DE B ORDE ........................................................................................... 35

4
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**1** **INTRODUCCIÓN**

El Proyecto corresponde a una central de almacenamiento de energía eléctrica con su respectiva
línea de transmisión de alta tensión (66 kV) de aproximadamente 3.06 km de longitud, además de
la construcción de un tap-off de alta tensión para interconectar la línea de transmisión con la línea

existente del SEN bajo el nombre de “66 kV Central Diesel Arica - Arica”. Este proyecto se localiza al
este de la ciudad de Arica, comuna de Arica, provincia de Arica, Región de Arica y Parinacota.

El Proyecto aportará suficiencia y eficiencia económica al Sistema Eléctrico Nacional, continuando

de esta forma con la descarbonización acelerada en Chile. Permitirá la alta penetración de
generación eléctrica de fuentes como la solar y eólica.

Tendrá una potencia nominal de 30 MW y una capacidad de almacenamiento de 158.4 MWh. Estará

compuesto por 11 unidades de almacenamiento, cada unidad consistirá en 2 contenedores BESS de
7.2 MWh cada uno y 1 transformador de 0.8k/33kV - 4.5MVA

El Proyecto tendrá una vida útil de 30 años y se contempla la utilización de una superficie

aproximada de 8.6 hectáreas, considerando el total de las instalaciones y de la línea eléctrica de

3.06 km.

Respecto a la Línea Eléctrica del Proyecto, se plantea su trayectoria en las cercanías de una quebrada
identificada por IGM (sin nombre). Es en esta situación que nace la interrogante de comprender los
límites del cauce natural ante una crecida con periodo de retorno de 100 años, por lo que, basado

en ello se materializa el presente documento técnico que justifica dichos limites según estimaciones
de caudales de crecida y modelo hidráulico computacional en la trayectoria de esta quebrada.

En el marco regional, el área de estudio donde se ubica el Proyecto se encuentra dentro de la zona

climática identificada por Köppen-Geiger como “Clima desértico cálido” abreviatura Bwh, con una

temperatura media de 18° Celsius y precipitaciones escasas. Este clima se caracteriza por veranos

cálidos o muy cálidos, con temperaturas extremadamente altas, e inviernos suaves pero que en

zonas al interior las temperaturas se acercan a 0°C.

A continuación, se presenta la Figura 1.1 que contiene la ubicación a nivel regional del área del

Proyecto, la cual está contenida en: dos (2) cuencas, Río Lluta (BNA-012) y Río San José (BNA-013);

dos (2) subcuencas, Río San José (BNA-0131) y Río Lluta Bajo (BNA-0121); y dos (2) subsubcuencas,
Río San José (BNA-01310) y Río Lluta entre junta Quebrada Poconchile y Desembocadura (BNA
01211). Todas identificadas por DGA en su mapoteca digital.

5
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Figura 1.1 Ubicación del Proyecto

Fuente: Elaboración Propia, MODELING 2024.

**2** **OBJETIVOS**

El objetivo principal de esta memoria de cálculo es determinar las trazas de crecida TR100 años para
quebrada IGM identificada por el Instituto Geográfico Militar (IGM) en posible interacción con el

Proyecto.

Los objetivos secundarios corresponden a determinar mediante un estudio hidrológico los caudales
de crecida para periodos de retorno de 2, 5, 10, 20, 25, 50 y 100 años. Y junto a ello, mediante el
software HEC-RAS versión 6.4.1 establecer una modelación computacional de carácter hidráulico
con los caudales ya estimados anteriormente y la topografía disponible.

Asimismo, se tomarán en cuenta los potenciales impactos futuros del cambio climático en los
patrones de precipitación en la región, lo cual incide directamente en las proyecciones de caudales

estimados.

.

6
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**3** **ANTECEDENTES**

Uno de los antecedentes principales para el reconocimiento hidrográfico de la componente
hidrológica, además de visita a terreno, fue la utilización del insumo cartográfico del IGM Escala
1:50.000, cartografía que fue adquirida en la plataforma en línea del Instituto Geográfico Militar de
Chile de nombre Arica (A-012). Dicha cartografía fue superpuesta con el área del Proyecto de donde
se obtiene la siguiente Figura representativa.

Figura 3.1 Cartografía IGM Arica (A-012)

Fuente: Elaboración propia en base a Cartografía IGM 1:50.000, MODELING 2024.

De la Figura anterior se logra identificar un (1) cauce natural que tendría posible interacción con el

Proyecto.

7
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**3.1** **Área de Estudio**

El Proyecto se emplazará en la Región de Arica y Parinacota, en la Provincia de Arica, Comuna de
Arica, aproximadamente a 1 km al este de la ciudad de Arica, su superficie comprenderá
aproximadamente 8.6 ha.

El área de Estudio definida corresponde al tramo de la LTE ubicado al suroeste del área de
almacenamiento de energía eléctrica.

A continuación, se muestra el área de Proyecto cercano a la zona a estudiar.

Figura 3.2 Área de Estudio

Fuente: Elaboración propia en base a IGM y DGA, MODELING 2024.

8
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**3.2** **Visita a Terreno**

Según la visita a terreno efectuada el día 6 de marzo del año 2024. Mediante un vuelo realizado con
Dron sobre el área de estudio es que se permite ver a mayor detalle las características del cauce y
de esta manera poder establecer un valor de coeficiente de rugosidad más exacto y fundamentado
para así realizar un modelo cercano a la realidad de un escenario de inundación. A continuación, se
adjuntan imágenes obtenidas.

Figura 3.3 Imagen de cauce en estudio

Fuente: Elaboración propia, MODELING 2024.

9
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Figura 3.4 Imagen de cauce en estudio

Fuente: Elaboración propia, MODELING 2024.

**4** **METODOLOGÍA**

**4.1** **Características Geomorfológicas de la Cuenca**

Para estimar caudales de crecida en el cauce a estudiar se deben conocer las características

geomorfológicas de la cuenca aportante, es por ello que para la determinación de la hidrología de
crecida en el presente estudio se utiliza la metodología establecida en el Manual de Cálculo de
Crecidas y Caudales Mínimos en Cuencas Sin Información Fluviométrica, DGA, 1995 y Manual de
Carretera Volumen 2 y 3. Dichas metodologías requieren de las características geomorfológicas de
cada cuenca aportante a analizar, de tal manera se puedan establecer parámetros que permitan
conocer el comportamiento de la cuenca ante una crecida provocada por un evento de tipo pluvial.

En primer lugar, se debe identificar el punto de control del cauce identificado por el IGM en su
cartografía 1:50.000 en torno al área de estudio definida para el Proyecto, de esta manera se logra
determinar la cuenca aportante a este punto y se logra cuantificar la superficie de entrega de aporte
pluvial al mismo.

Para poder determinar el Caudal de crecida del cauce en estudio, es necesario realizar una
determinación de parámetros geomorfológicos de las cuencas aportantes, los cuales se presentan

a continuación.

 - L: Longitud del cauce principal (Km)

 - Área: Área de la cuenca aportante (Km [2] )

 - H min: Cota mínima de la cuenca aportante (punto de salida) (m.s.n.m.)

 - H max: Cota máxima de la cuenca aportante (m.s.n.m.)

 - H media: Cota media de la cuenca (m.s.n.m.)

 - H: Diferencia de nivel total entre cotas extremas de la cuenca (m)

 - H med: Diferencia de nivel entre la cota media de la cuenca y la cota de salida (m)

10
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

 - S: Pendiente promedio cauce principal (m/m)

Para el presente estudio los datos anteriores son extraídos del Modelo de Elevación Digital (MED)
ALOSPALSAR correspondiente a la región de Arica y Parinacota, obtenido de la plataforma de
Infraestructura de Datos Geoespaciales (IDE).

**4.2** **Estimación de Precipitaciones de Crecida**

Se ejecuta un levantamiento de información del registro de precipitaciones máximas en 24 horas
históricas disponibles en la plataforma de DGA por estaciones meteorológicas, luego se procede al
relleno de datos faltantes según correlación lineal, y finalmente se determinan las precipitaciones
máximas en 24 horas según diferentes periodos de retorno mediante un análisis de frecuencia.

**4.2.1 Análisis y Relleno de Datos**

Dado que raramente se puede realizar el análisis de frecuencias sin examinar previamente posibles
errores de observación e inconsistencia. La representatividad y consistencia de los datos es esencial
para que los valores usados representen observaciones correctas y precisas.

Los errores más comunes son debido a un cambio de ubicación del pluviógrafo o pluviómetro, los
cambios de técnica de observación y errores instrumentales o de lectura.

Para el relleno de datos pluviométricos se utiliza el método de correlación lineal. Para aplicarlo, se
requiere establecer una correlación entre una estación patrón y una estación carente de datos. Lo
que se debe conseguir es la estimación de datos faltantes en función de la información patrón y
mediante una ecuación lineal de datos variables del tipo:

_Y_ = _a_ + _b_  _X_

Dónde:

Y = Valor de precipitación para la estación en (mm)
X = Valor de precipitación registrado en la estación patrón en (mm).

Por otra parte, existen valores reales de precipitación de la estación carente. Se define el siguiente

sistema de ecuaciones:

∑Y= n x a x ∑X

∑X x Y= a x ∑X+ b x ∑x2

El cual permite la obtención de los parámetros a y b para la determinación de datos en la estación

carente.

Dado que este relleno de estadística se realiza desde la estación patrón hacia la estación carente,
es necesario determinar el grado de correlación que existe entre ambas estaciones a modo de

11
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

determinar qué tan confiable será el relleno y si es que la estación patrón se encuentra bien

realizado.

Para realizar el método de relleno por correlación lineal se adoptó un valor de corte de r ≥ 0.6.

**4.2.2** Análisis de Frecuencias en Precipitaciones

 - **Modelo probabilístico**

Acorde al Manual de Carretera Volumen 2, El objetivo del análisis de frecuencia de cualquier variable
aleatoria es asociar a cada valor de la variable una probabilidad de ocurrencia. Ello se logra
representando la variable con un determinado modelo probabilístico y estimando los parámetros
de dicho modelo. Logrado este objetivo se permite construir un modelo probabilístico del
fenómeno, pudiendo obtenerse estimados de los valores de la variable asociados a cualquier
probabilidad de ocurrencia.

Sin embargo, el estimado del valor asociado a un período de retorno o probabilidad, es también una
variable aleatoria, por ser una función de variables aleatorias y, por consiguiente, se puede asociar
a dicha estimación no sólo un valor puntual, sino también un error de estimación y un intervalo de

confianza.

En base a esto es que, para el presente estudio, se evaluarán las siguientes distribuciones: Normal,
Log Normal, Pearson III, Gumbel, EV2 y GEV.

 - **Criterios de Selección de modelo**

**Criterio de información de Akaike**

El Criterio de Información de Akaike (AIC, por sus siglas en inglés) es una métrica estadística que
permite comparar y seleccionar modelos matemáticos en función de su capacidad para describir
adecuadamente un conjunto de datos observados.

El AIC fue desarrollado por el estadístico japonés Hirotugu Akaike en 1973 y se basa en la teoría de
la información. El AIC busca equilibrar la bondad de ajuste del modelo a los datos y la complejidad
del modelo, evitando así el sobreajuste (overfitting) y el subajuste (underfitting). El AIC se calcula
mediante la siguiente fórmula:

AIC= −2 ∗ln(L) + 2 ∗k

Donde L es la verosimilitud máxima del modelo y k es el número de parámetros estimados. Un AIC
más bajo indica un mejor equilibrio entre la complejidad y la capacidad predictiva del modelo.

**Criterio de información de Akaike corregido**

El Criterio de Información de Akaike Corregido (AICc) es una variante del AIC que tiene en cuenta el
tamaño de la muestra al comparar y seleccionar modelos matemáticos. El AICc es especialmente
útil en situaciones donde el tamaño de la muestra es pequeño en relación con el número de
parámetros estimados.

12
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

El AICc es una extensión del AIC que incorpora una corrección basada en el tamaño de la muestra
(n) y el número de parámetros estimados (k) en el modelo. El AICc se calcula mediante la siguiente

fórmula:

AICc= AIC+ [2k] [2] [ + 2k]

n−k−1

Esta corrección se añade al AIC original para penalizar modelos más complejos cuando el tamaño
de la muestra es pequeño. Al igual que en el AIC, un AICc más bajo indica un mejor equilibrio entre
la complejidad del modelo y su capacidad predictiva.

**Criterio de información Bayesiano**

El Criterio de Información Bayesiano, conocido también como BIC (por sus siglas en inglés), es un
indicador estadístico fundamentado en la teoría bayesiana. Su propósito es facilitar la comparación
y elección de modelos matemáticos, basándose en su habilidad para representar de manera
apropiada un conjunto de datos observados.

El BIC fue desarrollado por el estadístico Gideon E. Schwarz en 1978 y, al igual que el AIC, busca
equilibrar la bondad de ajuste del modelo a los datos y la complejidad del modelo. La principal
diferencia entre el BIC y el AIC es la penalización que se aplica a la complejidad del modelo, siendo
el BIC más severo en este aspecto. El BIC se calcula mediante la siguiente fórmula:

BIC= −2 ∗ln(L) + k∗ln (n)

Donde L es la verosimilitud máxima del modelo, k es el número de parámetros estimados y n es el
tamaño de la muestra. Un BIC más bajo indica un mejor equilibrio entre la complejidad y la
capacidad predictiva del modelo.

**Criterio de Anderson-Darling**

El Criterio de Anderson-Darling es una prueba estadística no paramétrica que se utiliza para evaluar
si una muestra de datos sigue una distribución teórica específica. En el campo de la hidrología, la
aplicación del criterio de Anderson-Darling es fundamental para determinar la idoneidad de las
distribuciones de probabilidad en el análisis de eventos extremos.

El criterio de Anderson-Darling fue desarrollado por Theodore W. Anderson y Donald A. Darling en
1952. La prueba se basa en la comparación de la función de distribución empírica (Fn) de los datos
observados con la función de distribución teórica (F) de una distribución de probabilidad específica.
El estadístico de Anderson-Darling (A2) se calcula mediante la siguiente fórmula:

N

A [2]
= −∑ [(2i−1)] n

[ln F(X i ) + ln(1 −F(X n+1−i ))]
n

−n

i=1

Donde n es el tamaño de la muestra, Xi es el i-ésimo dato ordenado y F(Xi) es la función de
distribución acumulativa teórica evaluada en Xi. Un valor de A2 más pequeño indica una mejor
concordancia entre la distribución empírica y la teórica.

13
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**4.2.3** Consideración del efecto del Cambio Climático

A modo de complementar esta estimación es que se considera el criterio de evaluación en el SEA

llamado “Cambio climático en la evaluación ambiental del recurso hídrico”, SEA, 2023.

Para contextualizar sobre el contenido, el documento proporciona una metodología para calcular la

variación en precipitación y temperatura en Chile, con el fin de predecir los impactos en el

componente hídrico en casos donde se identifiquen sinergias negativas entre un Proyecto y el
cambio climático (CC) bajo un escenario AR 8.5.

El Capítulo 2 de la guía Cambio climático en la evaluación ambiental del recurso hídrico, SEA 2023,

presenta el marco conceptual detrás de las proyecciones de variables hidrometeorológicas bajo

escenarios de CC, proporcionando conocimientos básicos sobre escenarios de emisión de Gases de

Efecto Invernadero (GEI), modelos climáticos globales y proyecciones de CC.

El Capítulo 3 de la guía presenta las proyecciones actuales de las variaciones futuras de precipitación

y temperatura para Chile, utilizando el Atlas de Riesgos Climáticos (ARClim) del MMA y el Balance

Hídrico Nacional (BHN) de la DGA como fuentes de información.

En el Capítulo 4, se explica la metodología que deben aplicar los titulares y consultores, su revisión

por parte de los evaluadores competentes, y se incluyen ejemplos para facilitar su comprensión.

En base al Capítulo 4 y a una zonificación de proyecciones de precipitaciones realizada es que

podemos estimar la afectación sobre la precipitación calculada. A continuación, se presenta la Figura

6.5 que representa las zonificaciones realizadas por el estudio y la tabla que cuantifica el cambio de

precipitación a escala porcentual.

14
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Figura 4.1 Sectorización de proyecciones de precipitación Cambio Climático

Fuente: Guía Cambio climático en la evaluación ambiental del recurso hídrico, SEA 2023.

Finalmente, se presentan anexos que ofrecen más detalles sobre la construcción de la metodología

y proporcionan una vía para la elaboración de proyecciones propias por parte de los titulares,

cuando sea necesario.

**Cuadro 4.1 Valores de cambio porcentual esperado de precipitación según zonificación con respecto al**

**periodo histórico**

|SECTOR|ELEVACIÓN MEDIA (MSNM)|CAMBIO EN LA PRECIPITACIÓN (%)|Col4|
|---|---|---|---|
|**SECTOR**|**ELEVACIÓN MEDIA (MSNM)**|**P25**|**P75**|
|A|4.140|-11,6|15,8|
|B|2.491|-17,6|13,5|
|C|960|33,7|165,6|
|D|1.948|-5,5|35,9|
|E|1.122|2,9|99,0|
|F|1.160|-24,1|19,8|
|G|3.459|-23,8|10,0|
|H|512|-30,5|0,2|

15
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

|SECTOR|ELEVACIÓN MEDIA (MSNM)|CAMBIO EN LA PRECIPITACIÓN (%)|Col4|
|---|---|---|---|
|**SECTOR**|**ELEVACIÓN MEDIA (MSNM)**|**P25**|**P75**|
|I|1.992|-28,5|0,0|
|J|1.283|-18,8|-8,3|
|K|292|-20,1|-9,5|
|L|317|-8,8|-3,3|
|M|857|-6,8|-1,4|
|N|312|1,2|6,1|

Fuente: Cambio climático en la evaluación ambiental del recurso hídrico, SEA 2023.

**4.3** **Determinación de los caudales de crecida**

Con los datos de estimación de precipitaciones y las propiedades geomorfológicas de la cuenca
aportante al punto de control a estudiar se realiza una estimación hidrológica de caudales de crecida
según la metodología que establece la DGA en su manual Cálculo de crecidas sin información
Fluviométrica, Método DGA-AC, Método de Verni-King Modificado y Método Racional, también se
considera las metodologías planteadas por el MOP en el Manual de Carretera.

Cabe destacar que se debe hacer una distinción en el cálculo de las estimaciones de caudales de
crecida para cuencas de áreas mayores a 25 km [2] y cuencas de áreas menores a 25 km [2] . Para cuencas
mayores se utiliza la metodología de DGA y para cuencas menores se procede de acuerdo con el
método Racional explicitado en el Manual de Carreteras Volumen 3.

Dado que la cuenca a estudiar tiene un área menor a 25 km [2], a continuación, se muestra el
desarrollo del cálculo de las estimaciones de caudales de crecida para la metodología entregada por
el Manual de Carretera, Volumen 3.

**4.3.1** Método Fórmula Racional

La fórmula por utilizar corresponde a la misma expuesta en el Manual de Cálculo de Crecidas y
Caudales Mínimos en Cuencas Sin Información Fluviométrica, DGA, 1995:

Q=

C(T)∗I(T)∗A p

en m [3] /seg
3,6

 - Q : Caudal instantáneo máximo de período de retorno T, expresado en m3/s.

 - C : Coeficiente de escorrentía asociado al período de retorno T según Manual

de Carretera Vol.3.

 - I : Intensidad media de lluvia asociada al período de retorno T y a una duración
igual al tiempo de concentración de la cuenca pluvial, expresada en mm/hr.

 - A : Área pluvial aportante expresada en km2.

La principal diferencia con el método descrito en el manual de carreteras es respecto a la obtención

del factor C, el cual debe determinarse en base a la tabla 3.702.503.B del Manual de Carreteras

Volumen 3 expuesta a continuación:

16
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Cuadro 4.2 Coeficientes de escorrentía para T = 10 años

|Factor|Extremo|Alto|Normal|Bajo|
|---|---|---|---|---|
|**Relieve**|0,28-0,35<br>Escarpados con<br>pendientes<br>mayores que 30%|0,20-0,28<br>Montañoso con<br>pendientes<br>entre 10 y 30%|0,14-0,20<br>Con cerros y pendientes<br>entre 5 y 10%|0,08-0,14<br>Relativamente plano con<br>pendientes menores al 5%|
|**Infiltración**|0,12-0,16<br>Suelo rocoso, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable|0,08-0,12<br>Suelos arcillosos<br>o limosos con<br>baja capacidad<br>de infiltración,<br>mal drenados|0,06-0,08<br>Normales, bien drenados,<br>textura mediana, limos<br>arenosos, suelos<br>arenosos|0,04-0,06<br>Suelos profundos de<br>arena u otros suelos bien<br>drenados con alta<br>capacidad de infiltración|
|**Cobertura**<br>**Vegetal**|0,12-0,16<br>Cobertura escasa.<br>Terreno sin<br>vegetación o<br>escasa cobertura|0,08-0,12<br>Poca<br>vegetación,<br>terrenos<br>cultivados o<br>naturales,<br>menos del 20%<br>del área con<br>buena<br>cobertura<br>vegetal|0,06-0,08<br>Normal, posibilidad de<br>almacenamiento buena,<br>zonas húmedas,<br>pantanos, lagunas y lagos|0,04-0,06<br>Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas planicies<br>de inundación o gran<br>cantidad de zonas<br>húmedas, lagunas o<br>pantanos.|
|**Almacenamiento**<br>**Superficial**|0,10-0,12<br>Despreciable,<br>pocas depresiones<br>superficiales, sin<br>zonas húmedas|0,08-0,10<br>Baja, sistema de<br>cauces<br>superficiales<br>pequeños bien<br>definidos, sin<br>zonas húmedas|0,06-0,08<br>Posibilidad de<br>almacenamiento buena,<br>zonas húmedas,<br>pantanos, lagunas, lagos|0,04-0,06<br>Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas planicies<br>de inundación o gran<br>cantidad de zonas<br>húmedas, lagunas o<br>pantanos|
|Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25|Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25|Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25|Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25|Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25|

Fuente: Elaboración propia en base a Manual de Carretera V3, MODELING 2024.

**4.3.2** Transposición de Caudales

 - **Selección de la estación de referencia:**

Se elige una estación hidrológica cercana a la cuenca de interés que tenga datos históricos bien
registrados de caudales. La estación de referencia debe tener características hidrológicas y
climáticas similares a la cuenca objetivo para garantizar la validez del método.

 - **Análisis de características físicas y climáticas:**

Se comparan las características físicas y climáticas entre la cuenca de referencia y la cuenca objetivo.
Estas características pueden incluir la precipitación media, altitud, pendiente del terreno, cobertura
vegetal, entre otros factores relevantes que influyen en la generación de caudales.

17
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

 - **Ajuste de datos de la estación de referencia:**

Los datos de caudales de la estación de referencia se ajustan para reflejar las condiciones específicas
de la cuenca objetivo. Esto puede implicar el uso de coeficientes de ajuste basados en la
comparación de las características físicas y climáticas entre ambas cuencas.

 - **Estimación de caudales en la cuenca objetivo:**

Se aplican los coeficientes de ajuste a los datos de caudales de la estación de referencia para estimar
los caudales en la cuenca objetivo. Estos caudales estimados se consideran una aproximación de los
flujos de agua en ausencia de datos directos de caudales. El coeficiente de ajuste estándar que se
suele usar se determina de la siguiente manera.

K= [A] [1] [ ∗P] [1]

A 2 ∗P 2

Donde:

A 1 : Área de la cuenca en estudio.
A 2 : Área de la Cuenca base (Estación Fluviométrica).
P 1 : Precipitación de la cuenca en estudio.
P 2 : Precipitación de la cuenca base (Estación Fluviométrica).

Finalmente, para determinar los caudales en el punto de interés es que se emplea la siguiente

formula.

Q P(y) = K∗Q bP(y)

Donde:

Q P ( y ) : Caudal asociado a una probabilidad de excedencia P(y), en la cuenca de estudio.

Q bP ( y ) : Caudal asociado a una probabilidad de excedencia P(y), en la cuenca base (Estación

Fluviométrica).
K : Factor de transposición adimensional.

**4.3.3** Hidrograma Unitario SCS

La lluvia efectiva (Q), se calcula en función de la lluvia (P), del potencial máximo de retención de
agua y de las pérdidas iniciales, las cuales se estiman en un 20% del potencial máximo, por medio
de la siguiente expresión:

Q= [(P−0.2 S)] [2]

P+ 0.8 S

El potencial máximo de retención de agua es función de la curva número y se calcula como sigue:

S= [1000]

CN [−10]

18
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

El factor CN o curva número depende del tipo de suelo, de la naturaleza y cobertura del suelo y las
condiciones previas de humedad.

Para estimar la forma y el gasto máximo el SCS propone también el uso de un hidrograma triangular
que se asemeja a una curva de hidrograma adimensional derivado a partir de muchos hidrogramas
calculados. Las expresiones propuestas son las siguientes:

q p = 0.75Q/T p = 1.12Q/T c

T b = 2.67T p = 1.8T c

T p = 0.67T c

Siendo:

q p : Caudal máximo.
T c : Tiempo de concentración.
T b : Tiempo de la base del hidrograma.
T p : Tiempo al máximo.
Q : Volumen escurrido expresado en alturas de aguas.

**4.4** **Modelación Hidráulica**

Para calcular el comportamiento hidráulico de la quebrada, se utiliza el Programa Computacional
HEC-RAS 6.4.1. Este software fue desarrollado por el Centro de Ingeniería Hidrológica de Texas,
Estados Unidos (Hydrologic Engineering Center, US Army Corps of Engineers). En este estudio, se
emplea la mencionada herramienta para desarrollar un modelo hidráulico computacional 2D.

Es crucial destacar que el modelo hidráulico propuesto se desarrolló en formato bidimensional (2D).
Esto significa que toda su estructura y geometría se basan en un modelo de elevación digital, el cual
cubre toda la superficie del área de estudio y permite el flujo en dos direcciones. En contraste, el
tradicional modelo HEC-RAS en una dimensión (1D) efectúa perfiles transversales en cada cauce y
calcula el comportamiento hidráulico entre estos, representando los efectos del flujo en una sola

dirección.

El objetivo es establecer las trazas de inundación para una crecida centenaria en un cauce estudiado,
en este caso, la quebrada, considerando el efecto de los afluentes en las mismas. Como resultado,
se proporcionarán las profundidades y velocidades de flujo en el área de estudio.

El modelo computacional utiliza insumos topográficos, caudales de crecida en m3/s, condiciones de
borde y parámetros de rugosidad, estos últimos estimados según el tipo de cauce. Adicionalmente,
se incorpora toda obra de cruce existente en el área de estudio para el desarrollo del modelo

hidráulico.

19
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**4.4.1** Topografía

Para cumplir con la metodología de modelaciones hidráulicas computacionales se debe cumplir con
lo estipulado por las entidades fiscalizadoras (DGA-DOH) en sus documentos “Permiso Ambiental
Sectorial 155, 156 y 157”, “Guías Metodológicas para Proyectos de Modificación de Cauces” y la
resolución N°135 del año 2020 de la DGA. Bajo estos lineamientos, es necesario basar los estudios
presentados en información topográfica de gran resolución en el desarrollo de las modelaciones:
Dicha información debe cumplir como mínimo con identificar curvas de nivel cada 0,5 metros y un
área de modelación que contenga 100 metros en dirección a aguas arriba y 100 metros en dirección
a aguas abajo de la posible área de interacción del Proyecto con el cauce.

**4.4.2** Coeficiente de Rugosidad

En vista que la rugosidad de los cauces no es homogénea, los valores de rugosidad de Manning para

el cauce se determinan mediante el método de Cowan o multiparamétrico según cauce central y

zonas de riberas, los parámetros se determinan a continuación.

Valor de Manning en cauce método de Cowan

La expresión es la siguiente:

n= (n b + n 1 + n 2 + n 3 + n 4 ) ∗m

Donde:

 - n b = un valor de n para un cauce recto, uniforme y liso en función del material de fondo.

 - n 1 = factor de corrección para considerar el efecto de las irregularidades superficiales.
Cuando la razón entre el ancho y profundidad del cauce es pequeña.

 - n 2 = un valor que añade las variaciones de forma y tamaño de la sección del cauce. El
valor de n2 no es afectado significativamente por cambios relativamente grandes en la
forma y tamaño de la sección del cauce si los cambios son graduales y uniformes.

 - n 3 = un valor que considera el efecto de las obstrucciones, tales como troncos, tacos,
cantos rodados, escombros, pilotes y muelles, perturba el flujo y aumenta la rugosidad del
cauce. Chow (1959) asigna valores de ajuste para 4 niveles de obstrucción: despreciable,
menor, apreciable y severa.

 - n 4 = un valor que incorpora el efecto de la presencia de vegetación y condiciones del
flujo. El efecto de la vegetación n4 depende de la profundidad del flujo y del perímetro
mojado cubierto por vegetación.

 - m = un factor que implementa la sinuosidad del cauce. El grado de sinuosidad del
cauce será considerado sólo cuando el flujo es confinado al cauce.

**4.4.3** Geometría del Modelo

Los modelos computacionales bidimensionales (2D) se ejecutan mediante una serie de elementos

geométricos que conforman una malla, dicha malla simula las condiciones de cauces basándose en

la topografía base.

20
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

El modelo del Proyecto es ejecutado mediante una geometría mallada que se establece según la

magnitud del área a modelar, en el caso del presente estudio se estudian áreas de dimensiones

variables. No obstante, se ejecutaron e iteraron distintas magnitudes de células desde 1 metro hasta

10 metros por cara a modo de escoger la dimensión correcta de modelación y generar un modelo

estable.

En definitiva, el modelo computacional final es ejecutado con células en el área de los cauces y

riberas a 1 metros por cada cara y en áreas externas a las riberas con células a 5 metros. A

continuación, se agrega una figura que demuestra el contexto de mallado y como es ejecutado en

el modelo 2D, cuáles son sus partes e identificación de cada elemento.

Figura 4.2 Ejemplo de malla HEC-RAS 2D

Fuente: Elaboración propia en base a manual HEC-RAS, MODELING 2024.

21
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**4.4.4** Método de cálculo HEC-RAS

Para el modelo 2D HEC-RAS, el software resuelve las ecuaciones 2D de Saint-Venant, a menudo
denominadas ecuaciones de aguas poco profundas (con adiciones de momento opcionales para
efectos de turbulencia y Coriolis) o las ecuaciones de onda de difusión 2D. El solucionador de
ecuaciones de aguas poco profundas ignora las velocidades verticales y asume la presión
hidrostática, mientras que el solucionador de aproximación de onda difusiva omite además los
términos viscosos inestables, de advección y turbulentos, lo que reduce el rango de aplicabilidad,
pero tiene muchas ventajas computacionales. Por lo tanto, en general, la selección de las ecuaciones
de onda de difusión 2D permite que el software se ejecute más rápido y tiene mayores propiedades
de estabilidad, mientras que las ecuaciones de Saint-Venant 2D son aplicables a una gama más
amplia de problemas. El solucionador de ecuaciones de flujo no estacionario 2D utiliza un algoritmo
de volumen finito implícito. El algoritmo de solución implícito permite pasos de tiempo
computacional más grandes que los métodos explícitos.

El presente modelo se trabaja en unidades internacionales (métricas), y mediante la herramienta
“Gis tools” se importa el DEM con su propia georrefenciación. Una vez importado el DEM podemos
visualizar la geometría en “Geometric Data”, luego se procederá a añadir el área de flujo en 2
dimensiones, esto se logra dibujando el área de interés, luego se procede a dibujar con la
herramienta “SA/2d Área BC Lines” las cuales permiten establecer las condiciones de borde en el
modelo, y así se establecen dichas condiciones.

Luego se procede a editar el área de flujo dibujada previamente, escogemos la opción para Generar
puntos de cálculo en intervalos regulares con todas las líneas de corte, generando así dimensiones
de 5 x 5 metros para zonas fuera de los cauces, dimensiones de 1 x 1 metros para zonas del cauce y
forzamos la creación de la células o celdas de estas dimensiones, se acoge el coeficiente de Manning
calculado previamente para el área de estudio.

Posterior a ello se agregan las obras de atravieso existentes en el área de estudio, obras que
permiten cruzar caminos en la trayectoria de cada cauce, en lo cual se consideraran las
características geométricas y de materiales de cada una de ellas. A su vez, se agregan los caudales
del cauce estudiado según hidrogramas de crecidas desarrollados y argumentados anteriormente.

Finalmente se corre un plan de modelación según geometría, hidrograma de caudales y ecuación
requerida.

22
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**5** **RESULTADOS**

**5.1** **Características Geomorfológicas de las Cuencas Aportantes**

A continuación, se determinan el cauce a estudiar, el punto de control respetivos y la cuenca
aportante a este punto de control. Lo anterior se presenta en la siguiente figura y definido en el
cuadro posterior.

Figura 5.1 Cuenca Aportante y Punto de Control

Fuente: Elaboración Propia, MODELING 2024.

23
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Cuadro 5.1 Coordenadas Puntos de Control

|PUNTO DE CONTROL|COORDENADAS PUNTO DE ENCUENTRO OBRAS PROYECTO UTM|Col3|
|---|---|---|
|**PUNTO DE CONTROL**|**DATUM UTM WGS 84, HUSO 19 S**|**DATUM UTM WGS 84, HUSO 19 S**|
|**PUNTO DE CONTROL**|**ESTE**|**NORTE**|
|**QUEBRADA BESS 14**|364.750|7.959.921|

Fuente: Elaboración Propia, MODELING 2024.

A continuación, se muestran los parámetros geomorfológicos para la cuenca aportante.

Cuadro 5.2 Características Morfológicas de las Cuencas Aportantes

|PUNTO<br>DE<br>CONTROL|CARACTERÍSTICAS DE LA CUENCA APORTANTE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**PUNTO**<br>**DE**<br>**CONTROL**|**Área**<br>**aportante**<br>**(Km2)**|**Largo**<br>**(km)**|**H min**<br>**(msnm)**|**H max**<br>**(msnm)**|**H media**<br>**(Msnm)**|**H med (m)**|**Desnivel**<br>**H (m)**|**Pendiente**<br>**media**<br>**cuenca**<br>**(m/m)**|
|**QUEBRAD**<br>**A BESS 14**|17.986|10.39|62|556|389.520|327.520|494|0.059|

Fuente: Elaboración propia, MODELING 2024.

De manera adicional, la cuenca estudiada presenta un régimen exclusivamente pluvial, esto dado
que la isoterma cero de la región de Arica y Parinacota generalmente se encuentra por sobre los
5000 m.s.n.m. según indica la Dirección Meteorológica de Chile, y las alturas máximas de la cuenca
solo llegan hasta los 556 m.s.n.m.

24
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**5.2** **Estimación de precipitaciones de Crecida**

Para el análisis pluviométrico se utilizarán las estaciones meteorológicas más cercanas a la cuenca
en estudio. La principal fuente de información corresponde a la Dirección General de Aguas (DGA),
cabe destacar que el área de estudio no cuenta con información Fluviométrica que pueda
caracterizar hidrológicamente los cauces que forman parte del estudio.

Cuadro 5.3 Ubicación de estaciones meteorológicas seleccionadas

|N°|ESTACIÓN METEOROLÓGICA DGA|CÓDIGO BNA|DATUM WGS 84,<br>HUSO 19 S|Col5|ALTITUD<br>(msnm)|
|---|---|---|---|---|---|
|**N°**|**ESTACIÓN METEOROLÓGICA DGA**|**CÓDIGO BNA**|**ESTE**|**NORTE**|**NORTE**|
|1|Arica Oficina|01310018-7|360.557|7.956.456|20|
|2|Azapa|01310019-5|375.451|7.952.288|365|

Fuente: Elaboración propia, MODELING 2024.

La figura siguiente muestra la ubicación geográfica de las estaciones seleccionadas para el estudio.
En el cuadro siguientes se muestran los datos de precipitaciones máximas diarias registradas
obtenidos en estas estaciones meteorológicas de su registro histórico.

Figura 5.2 Ubicación Estaciones Meteorológicas DGA

Fuente: Elaboración propia, 2024.

25
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Cuadro 5.4 Precipitaciones máximas en 24 horas anual disponibles

|AÑO|AZAPA|ARICA OFICINA|
|---|---|---|
|1966|0.00||
|1967|0.00|<br>|
|1968|5.00|<br>|
|1969|1.00|<br>|
|1970|0.50||
|1971|0.00|<br>|
|1972|0.00|<br>|
|1973|0.90||
|1974|0.60<br>|0.00|
|1975|<br>|1.80|
|1976||0.40|
|1977|<br>|0.40|
|1978|<br>|0.00|
|1979||0.00|
|1980|1.00|0.00|
|1981|1.10|0.00|
|1982|0.00|1.10|
|1983|0.00|0.00|
|1984|0.00|1.00|
|1985|0.00|0.00|
|1986|0.00|2.10|
|1987|0.00|1.80|
|1988|0.00|0.20|
|1989|0.00|0.20|
|1990|0.00|0.90|
|1991|0.00|0.00|
|1992|0.00|0.00|
|1993|1.50|3.00|
|1994|0.00|0.00|
|1995|0.00|2.00|
|1996|0.00|0.10|
|1997|3.00|4.10|
|1998|0.00|0.00|
|1999|0.00|0.00|
|2000|0.00|0.30|
|2001|0.00|0.50|
|2002|2.00|4.00|
|2003|8.20|2.00|
|2004|0.00|1.00|
|2005|0.00|0.00|

26
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

|AÑO|AZAPA|ARICA OFICINA|
|---|---|---|
|2006|0.00|0.50|
|2007|0.00|0.80|
|2008|1.80|1.00|
|2009|0.00|0.00|
|2010|0.00|0.00|
|2011|4.50|2.00|
|2012|0.00|2.00|
|2013|0.00|0.00|
|2014|0.50|0.00|
|2015|0.00|0.00|
|2016|0.00|0.00|
|2017|0.00|0.00|
|2018|3.00|0.00|
|2019|7.80|5.00|
|2020|7.50|2.00|
|2021|0.40|1.80|
|2022|0.20|0.00|
|**MIN**|**0.00**|**0.00**|
|**MAX**|**8.20**|**5.00**|
|**MEDIA**|**0.97**|**0.86**|
|**N° DE DATOS**|**52**|**49**|

Fuente: Elaboración propia en base a DGA, MODELING 2024.

En una observación preliminar de los datos pluviométricos disponibles para la zona de estudio, se
puede apreciar que la estación Azapa, la cuál es la más lejana al área de estudio, presenta un registro
discontinuo de datos a diferencia de la estación Arica Oficina, sin embargo, todas las estaciones
tienen un registro superior a 30 años.

En general, las precipitaciones máximas en 24 horas del registro históricos de las estaciones DGA
varían entre los 5 y 8.2 mm aproximadamente y los promedios presentan valores que van desde los
0.86 a 0.97 mm. Dado que las estaciones presentan una baja correlación no se aplica el relleno de
datos entre estaciones, además dado que la estación Arica oficina se encuentra más cerca del área
de proyecto es que se utilizan los datos de precipitación de esta estación. Cabe mencionar que para
efectos del análisis de frecuencia y ante la gran cantidad de datos nulos presentados en la zona, es
que dichos valores se reemplazan por 0.01, el cuál corresponde a un valor bajo pero que permite
trabajar con los modelos de distribución y selección de datos

En la figura siguiente se puede apreciar la magnitud de las precipitaciones de las estaciones
pluviométricas seleccionadas.

27
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Figura 5.3 Precipitaciones máximas en 24 horas anuales disponibles en Estaciones DGA

Fuente: Elaboración propia en base a DGA, MODELING 2024.

28
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

**5.2.1** Análisis de Frecuencia de precipitaciones

A continuación, se presentan los gráficos correspondientes a las distintas distribuciones evaluadas
para el análisis de frecuencia en la estación DGA Arica Oficia.

Figura 5.4 Análisis de frecuencias estación Arica Oficina

Fuente: Elaboración propia, MODELING 2024

Por lo cual a continuación se muestra un resumen de las distribuciones adoptada.

Cuadro 5.5 Resumen de Distribución Adoptada

|ESTACIÓN|DISTRIBUCIÓN|AIC|AICc|BIC|ADC|DISTRIBUCIÓN ADOPTADA|
|---|---|---|---|---|---|---|
|**ARICA OFICINA**|**NORM**|161.38|161.64|165.17|6.82|**GEV **|
|**ARICA OFICINA**|**LN**|29.94|30.20|33.73|6.74|6.74|
|**ARICA OFICINA**|**GUMBEL**|136.01|136.27|139.80|**6.44**|**6.44**|
|**ARICA OFICINA**|**GEV**|**-329.71**|**-329.18**|**-324.03**|4791.89|4791.89|

Fuente: Elaboración Propia, MODELING 2024.

De los resultados obtenidos se concluye que la distribución adoptada depende del cumplimiento de
los criterios y de un buen ajuste gráfico y espacial, para representar adecuadamente los fenómenos
registrados por cada estación. Para este estudio la distribución General de Valores Extremos (GEV)
es la que mejor describe el fenómeno ocurrido en la estación seleccionada.

Finalmente, con la estadística planteada se presentan a continuación las precipitaciones de crecida
para distintos periodos de retorno estimados en cada estación en estudio y los caudales de la
estación fluviométrica para distintos periodos de retorno.

29
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

ADENDA - DIA

OENERGY MODELING

Cuadro 5.6 Resumen de Precipitaciones Adoptadas

|ESTACIÓN<br>DGA|RESUMEN DE PRECIPITACIONES (mm) (MÉTODO DE ANÁLISIS DE FRECUENCIAS)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ESTACIÓN**<br>**DGA**|**T=2**<br>**(Años)**|**T=5**<br>**(Años)**|**T=10**<br>**(Años)**|**T=20**<br>**(Años)**|**T=25**<br>**(Años)**|**T=50**<br>**(Años)**|**T=100**<br>**(Años)**|
|Arica Oficina|0.44|1.27|2.07|3.10|3.50|4.98|6.94|

Fuente: Elaboración Propia, MODELING 2024.

**5.2.2** Consideración del Efecto del Cambio Climático

En base a la información presentada en el capítulo de metodología es que se identifica que el
proyecto está ubicado en el **Sector B**, por lo que el escenario más desfavorable para el proyecto
corresponde a un **P75** para precipitaciones máximas, con un cambio de 13,5%, ya que provoca un
aumento en las precipitaciones máximas, a diferencia de un caso de P25 con -17,6%. De esta forma
obtenemos los siguientes valores de precipitaciones para un escenario que considera el impacto del

cambio climático ante un escenario AR 8.5.

Cuadro 5.7 Resumen de Precipitaciones Calculadas considerando CC P25 y P75

|ESTACIÓN DGA|RESUMEN DE PRECIPITACIONES (mm) (CAMBIO CLIMÁTICO)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ESTACIÓN DGA**|**T=2 (Años)**|**T=5 (Años)**|**T=10 (Años)**|**T=20 (Años)**|**T=25 (Años)**|**T=50 (Años)**|**T=100 (Años)**|
|Arica Oficina (P25)|0.36|1.05|1.70|2.56|2.88|4.10|5.72|
|Arica Oficina (P75)|0.50|1.44|2.35|3.52|3.97|5.65|7.88|

Fuente: Elaboración Propia, MODELING 2024.

A modo de comparar resultados es que se presenta el siguiente gráfico representando los dos
escenarios calculados, escenario actual según análisis de frecuencia y escenario de análisis de
frecuencia considerando el efecto cambio climático AR 8.5 según guía SEA y ARCLIM.

Figura 5.5 Comparación escenarios precipitación máxima anual en 24 hrs

Fuente: Elaboración Propia, MODELING 2024.

30
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

**5.3** **Determinación de los Caudales de Crecida**

**5.3.1** Método Fórmula Racional

En base a la tabla presentada (Cuadro 4.2), a continuación, se presenta la tabla que determina el

cálculo del coeficiente CT.

Cuadro 5.8 Cálculo coeficiente de escorrentía

|FACTOR|INCIDENCIA|RANGO|VALOR|
|---|---|---|---|
|Relieve|Normal|0.14-0.20|0.14|
|Infiltración|Normal|0.06-0.08|0.06|
|Cobertura Vegetal|Extremo|0.12-0.16|0.16|
|Almacenamiento superficial|Alto|0.08 - 0.10|0.08|
|**C(T=10)**|**C(T=10)**|**C(T=10)**|**0.44**|

Fuente: Elaboración propia, MODELING 2024.

A continuación, se presentan los resultados de los caudales de crecida obtenidos mediante el

Método Racional.

Cuadro 5.9 Estimación de Caudales de Crecida para diferentes T Método Racional MC Vol.3

|P. Control|Área<br>(km2)|T<br>(años)|C(10<br>)|C(T)/C(10<br>)|C(T)|PPT/2<br>4h|CDtc|K|PP T/tc<br>(mm)|tc<br>(h)|I T<br>tc|Q<br>(m3/seg)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**P. Control**|**Área**<br>**(km2)**|**T **<br>**(años)**|**C(10**<br>**) **|**C(T)/C(10**<br>**) **|**C(T)**|**(mm)**|**(mm)**|**(mm)**|**(mm)**|**(mm)**|**(mm)**|**(mm)**|
|Quebrada<br>S/N|17.99|2|0.44|1|0.44|0.44|0.495|1.1|0.24|1.3|0.18|0.40|
|Quebrada<br>S/N|17.99|5|5|1|0.44|1.27|1.27|1.27|0.69|0.69|0.53|1.17|
|Quebrada<br>S/N|17.99|10|10|1|0.44|2.07|2.07|2.07|1.13|1.13|0.86|1.89|
|Quebrada<br>S/N|17.99|20|20|1.05|0.462|3.1|3.1|3.1|1.69|1.69|1.3|3.00|
|Quebrada<br>S/N|17.99|25|25|1.1|0.484|3.5|3.5|3.5|1.91|1.91|1.46|3.53|
|Quebrada<br>S/N|17.99|50|50|1.2|0.528|4.98|4.98|4.98|2.71|2.71|2.08|5.49|
|Quebrada<br>S/N|17.99|100|100|1.25|0.55|6.94|6.94|6.94|3.78|3.78|2.9|7.97|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25|17.99|2|0.44|1|0.44|0.36|0.495|1.1|0.20|1.3|0.15|0.33|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25|17.99|5|5|1|0.44|1.05|1.05|1.05|0.57|0.57|0.44|0.97|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25|17.99|10|10|1|0.44|1.7|1.7|1.7|0.93|0.93|0.71|1.57|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25|17.99|20|20|1.05|0.462|2.56|2.56|2.56|1.40|1.40|1.07|2.48|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25|17.99|25|25|1.1|0.484|2.88|2.88|2.88|1.57|1.57|1.21|2.92|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25|17.99|50|50|1.2|0.528|4.1|4.1|4.1|2.23|2.23|1.72|4.53|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25|17.99|100|100|1.25|0.55|5.72|5.72|5.72|3.12|3.12|2.40|6.59|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75|17.99|2|0.44|1|0.44|0.5|0.495|1.1|0.27|1.3|0.21|0.46|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75|17.99|5|5|1|0.44|1.44|1.44|1.44|0.78|0.78|0.60|1.33|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75|17.99|10|10|1|0.44|2.35|2.35|2.35|1.28|1.28|0.99|2.17|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75|17.99|20|20|1.05|0.462|3.52|3.52|3.52|1.92|1.92|1.48|3.41|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75|17.99|25|25|1.1|0.484|3.97|3.97|3.97|2.16|2.16|1.66|4.03|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75|17.99|50|50|1.2|0.528|5.65|5.65|5.65|3.08|3.08|2.37|6.25|
|Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75|17.99|100|100|1.25|0.55|7.88|7.88|7.88|4.29|4.29|3.30|9.08|

31
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

Fuente: Elaboración propia, MODELING 2024.

**5.3.2** Transposición de Caudales

Dado que en la zona a estudiar los registros de precipitaciones presentan una gran cantidad de
valores nulos, es que se emplea un factor de transposición que solo considera las áreas de las

cuencas.

Como estación base es que se emplea la estación fluviométrica Río Lluta en Panamericana, la cual
cuenta con una cuenca de un área de 3340.2 km [2] . El valor correspondiente al factor de transposición
resulta ser 0.00538 lo que nos da valores de caudales como los presentes en el siguiente cuadro.

Cuadro 5.10 Resultados Transposición de Caudales

|T RETORNO|CAUDAL (m3/s)|
|---|---|
|**T RETORNO**|**QUEBRADA BESS14**|
|2|0.19|
|5|0.40|
|10|0.59|
|20|0.81|
|25|0.89|
|50|1.16|
|100|1.48|

Fuente: Elaboración propia, MODELING 2024.

**5.3.3** Hidrograma Unitario SCS

A continuación, se prestan los resultados de los principales parámetros determinados para el
método del hidrograma unitario.

|CN|88|
|---|---|
|**S **|1.36|
|**tb**|2.35|
|**tp**|0.87|

Cuadro 5.11 Resultados Hidrograma Unitarios SCS

|TR|Pt|Q|qp|
|---|---|---|---|
|2|0.21|0.00|0.003|
|5|0.60|0.06|0.060|
|10|0.98|0.24|0.228|
|20|1.47|0.56|0.528|
|50|2.36|1.26|1.192|
|100|3.29|2.08|1.960|

Fuente: Elaboración propia, MODELING 2024.

A continuación, se representa el hidrograma de crecida para un caudal TR100 años método SCS.

32
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

Figura 5.6 Hidrograma TR100 años SCS Quebrada S/N

Fuente: Elaboración Propia, MODELING 2024.

Finalmente, de los 3 métodos expuestos es que se opta por emplear los resultados determinados
mediante el **método racional**, ya que dichos valores resultan ser los más desfavorables para la zona
y permiten, de esta manera, anteponerse a cualquier eventualidad en un futuro.

**5.4** **Modelación Hidráulica**

Las modelaciones hidráulicas computacionales se realizaron en base a los valores de caudales
máximos de crecida para un periodo de retorno de 100 años en la quebrada estudiada, con estos
caudales de crecida estimados se simula una situación de crecida centenaria en la quebrada
mediante el software computacional HEC-RAS.

Para el cálculo del comportamiento hidráulico de la quebrada, se utiliza el Programa Computacional
HEC-RAS 6.4.1 desarrollado por el Centro de Ingeniería Hidrológica de Texas, Estados Unidos
(Hydrologic Engineering Center, US Army Corps of Engineers), el que es una herramienta
computacional versátil y útil para el cálculo de ejes hidráulicos en ríos y canales.

**5.4.1** Topografía

La topografía por utilizar es la levantada por el titular, la cual abarca el área de estudio en la
quebrada. Dicha topografía presenta características de identificar curvas de nivel cada 20

centímetros de terreno.

A continuación, se demuestra la figura del Modelo de Elevación Digital (MED) para el área de estudio
en torno a la LMT del Proyecto.

33
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

Figura 5.7 Representación de Topografía Proyecto

Fuente: Elaboración Propia, MODELING 2024.

**5.4.2** Coeficiente de Rugosidad

A continuación, se muestra un cuadro que identifica el valor de Manning adoptado tanto para el
cauce como para la ribera según metodología de Cowan.

Cuadro 5.12 Coeficiente De Rugosidad Manning Según Cowan

|LUGAR|VALORES DE COWAN|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**LUGAR**|**nb**|**n1**|**n2**|**n3**|**n4**|**m **|**MANNING (n)**|
|Cauce y ribera|0.02|0.008|0.005|0.02|0.005|1|0.058|

Fuente: Elaboración propia en base a Guide for Selecting Manning's Roughness Coefficients for Natural

Channels and Flood Plains, United States Geological Survey Water-Supply Paper 2339, 1989.

**5.4.3** Condiciones de borde

Se ingresó al modelo las condiciones de borde la quebrada, considerando como condición de borde
la pendiente del fondo del cauce según “Normal Depth” para HEC-RAS, estas fueron estimadas
mediante modelo de elevación digital (DEM) de la topografía entregada por el titular y se presentan

a continuación:

34
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

Cuadro 5.13 Condición de Borde

|CAUCE|PENDIENTE (m/m)|
|---|---|
|Quebrada|0.08|

Fuente: Elaboración propia, MODELING 2024.

Las condiciones de borde fueron incluidas en la ventada de Unsteady Flow data, Boundary
Condition, de manera independiente junto a los datos de caudales determinados.

**5.4.1** Geometría del Modelo

En la siguiente figura se visualiza el mallado utilizado en el modelo computacional. En el caso del

lecho de la quebrada el tamaño de la celda fue ajustado a 2 metros x 2 metros para lograr modelar

de manera precisa el escurrimiento superficial, para la zona aledaña se utilizan celdas de 5 x 5

metros.

**F** igura 5.8 Malla de modelo HEC-RAS 2D

Fuente: Elaboración propia, MODELING 2024.

35
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

**5.4.2** Resultados Modelación

A continuación, se demuestran los resultados entregados por los Modelos Computacionales HECRAS 2D, estos archivos tipo vectorial en Shape y tipo ráster en Geo TIFF fueron exportados de
manera íntegra sin modificación desde la plataforma HEC-RAS hasta la plataforma QGIS.

Las siguientes figuras demuestran los siguientes resultados:

 - Figura 5.8 demuestra la comparación de inundación entre un escenario de TR100 y ante un

escenario TR100 años considerando los efectos del cambio climático P25 Y P75.

 - Figura 5.9 demuestra resultados de profundidad del flujo en condiciones de una crecida TR

100años.

 - Figura 5.10 demuestra resultados de velocidad del flujo en condiciones de una crecida TR

100años.

Como es de conocimiento técnico en el desarrollo del modelo, el área de estudio presenta
pendientes de tipo medias, lo que condiciona el comportamiento hidráulico en tipo supercrítico
(torrente), con numero de Froude superior a 1 en varias zonas del modelo. No obstante, el cauce es
capaz de contener en gran manera la crecida de periodo de retorno 100 años, se visualiza que hay
desbordes leves del cauce con bajas profundidades y velocidades. Esto condicionado a la
intervención antrópica en el lecho de este

Las profundidades del modelo resultante van desde los 0,01 metros en el flujo hasta los 1,2 metros
en sectores puntuales. Las velocidades que presentan como resultado el modelo en el total del área
de estudio, van desde los 0.001 m/s hasta los 3,41 m/s.

36
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

**Figura 5.9 Comparativa Inundación TR100 años y TR100 años con Cambio Climático modelo HEC-RAS 2D**

Fuente: Elaboración propia, MODELING 2024.

37
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

**Figura 5.10 Profundidad TR100 años modelo Quebrada S/N HEC-RAS 2D**

Fuente: Elaboración propia, MODELING 2024.

**Figura 5.11 Velocidad TR100 años modelo Quebrada S/N HEC-RAS 2D**

Fuente: Elaboración propia, MODELING 2024.

38
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

**6** **ANÁLISIS**

En virtud de los resultados obtenidos en el presente estudio hidrológico e hidráulico, se opta por
ubicar la totalidad de los postes de la Línea de Transmisión Eléctrica (LTE) del Proyecto fuera de la
inundación TR100 años CC P75, al ser este el escenario con resultado más desfavorable respecto a
la magnitud de inundación.

**Figura 6.1 Cambio de emplazamiento de LTE Proyecto según Inundación TR 100 años**

Fuente: Elaboración propia, MODELING 2024.

Las trazas de inundación determinadas en el presente estudio consideran y argumentan un
resultado conservador en vista de las metodologías descritas y de la ubicación geográfica del

Proyecto.

39
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

**7** **CONCLUSIONES**

De lo mostrado en la estimación hidrológica para caudales de crecida y junto a la modelación
hidráulica respectiva al caudal de crecida TR100 años se logra concluir que, la inundación producida
en la quebrada es capas de ser contenida por la trayectoria de la quebrada sin demostrar

inundaciones fuera de esta.

Las precipitaciones máximas en 24 horas en la zona de estudios fueron estimadas entre 0.44 mm
para un periodo de retorno de 2 años y de 6.94 mm para un periodo de retorno de 100 años, estas
precipitaciones se obtuvieron mediante el análisis estadístico de los registros históricos de las
estaciones meteorológicas de la Dirección General de Aguas (DGA), Arica Oficina.

En base a tres metodologías de estimaciones de caudales de crecida, Método Racional, Método de
Transposición de Cuencas y Método de Hidrograma Unitario SCS, se logra determinar que para la
Quebrada S/N se demuestra un caudal de crecida TR100 años de 7.96 m [3] /s según el Método
Racional el cual es el que entrega un mayor caudal por lo tanto es más desfavorable si de inundación
se trata. Esta caudal resulta según la pequeña superficie de la cuenca aportante al punto de control
(área de 17,9 km [2] ) y la baja magnitud de precipitaciones.

El modelo hidráulico resultante a caudal TR100 años presenta valores de bajas profundidades y en
algunas zonas de considerables velocidades, alcanzando profundidades de 1,2 m y velocidades de
aproximadamente 3,41 m/s en el área de estudio del Proyecto.

En la quebrada se demuestra un caudal de crecida TR100 años de 7.96 m [3] /s según la metodología
empleada, esto resulta según la pequeña superficie de la cuenca aportante (área de 17,9 km [2] ).

Se comprende que el efecto de cambio climático compromete tanto una disminución como un
aumento de los caudales de crecida según indica la metodología “Cambio climático en la evaluación
ambiental del recurso hídrico”, SEA, 2023. Disminuyendo un 17,6% para P25 y aumentando un
13,5% para un P75.

Adicionalmente es importante destacar que el área de estudio se encuentra inmersa en una región
geográfica que presenta registros históricos de precipitaciones de magnitudes bajas a nulas
producto de su ubicación climatológica, por lo que estimar caudales de crecida en dicha zona
representa un desafío técnico mayor. No obstante, el presente documento fue argumentado con
bases empíricas y comparativas entre tres metodologías distintas para la estimación de caudales de
crecida TR100 años, además, fueron considerados los efectos del cambio climático en torno a dicha

estimación.

Finalmente, junto a los argumentos mostrados en el estudio: características geomorfológicas de la
cuenca, hidrología planteada y modelación hidráulica desarrollada, se asume que el Proyecto Línea
De Transmisión Y Central Bess Halcón 14 establece el emplazamiento de todos los postes de la línea
de transmisión eléctrica (LTE) fuera de las trazas de inundaciones resultantes al caudal de crecida
centenaria (TR100 años) considerando el efecto de cambio climático P75. Debido a lo anterior se
descarta la aplicabilidad del PAS 156 y se descarta la aplicabilidad del PAS 157.

40
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

OENERGY MODELING

**8** **BIBLIOGRAFIA**

 - Manual de Carreteras V3 (2016), MOP Chile.

 - Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin Información
Fluviométrica (1995), DGA.

 - Hidrología Aplicada (1994) Ven Te Chow

 - Guide for Selecting Manning's Roughness Coefficients for Natural Channels and Flood
Plains, United States Geological Survey Water-Supply Paper 2339, 1989

 - Manual Básico de HEC-RAS 3.1.3 y HEC-GeoRAS 3.1.1 (2007), Universidad de Granada

 - Cambio climático en la evaluación ambiental del recurso hídrico (2023), SEA.

**9** **APENDICE**

 - Apéndice A - Resultados Modelo Quebrada S/N

41
ESTUDIO DE INUNDACIÓN
PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 14

DIA

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4.1: Valores de cambio porcentual esperado de precipitación según zonificación con respecto al****

| SECTOR | ELEVACIÓN MEDIA (MSNM) | CAMBIO EN LA PRECIPITACIÓN (%) | Col4 |
| --- | --- | --- | --- |
| **SECTOR** | **ELEVACIÓN MEDIA (MSNM)** | **P25** | **P75** |
| A | 4.140 | -11,6 | 15,8 |
| B | 2.491 | -17,6 | 13,5 |
| C | 960 | 33,7 | 165,6 |
| D | 1.948 | -5,5 | 35,9 |
| E | 1.122 | 2,9 | 99,0 |
| F | 1.160 | -24,1 | 19,8 |
| G | 3.459 | -23,8 | 10,0 |
| H | 512 | -30,5 | 0,2 |

**Tabla 4.2: Coeficientes de escorrentía para T = 10 años**

| Factor | Extremo | Alto | Normal | Bajo |
| --- | --- | --- | --- | --- |
| **Relieve** | 0,28-0,35<br>Escarpados con<br>pendientes<br>mayores que 30% | 0,20-0,28<br>Montañoso con<br>pendientes<br>entre 10 y 30% | 0,14-0,20<br>Con cerros y pendientes<br>entre 5 y 10% | 0,08-0,14<br>Relativamente plano con<br>pendientes menores al 5% |
| **Infiltración** | 0,12-0,16<br>Suelo rocoso, o<br>arcilloso con<br>capacidad de<br>infiltración<br>despreciable | 0,08-0,12<br>Suelos arcillosos<br>o limosos con<br>baja capacidad<br>de infiltración,<br>mal drenados | 0,06-0,08<br>Normales, bien drenados,<br>textura mediana, limos<br>arenosos, suelos<br>arenosos | 0,04-0,06<br>Suelos profundos de<br>arena u otros suelos bien<br>drenados con alta<br>capacidad de infiltración |
| **Cobertura**<br>**Vegetal** | 0,12-0,16<br>Cobertura escasa.<br>Terreno sin<br>vegetación o<br>escasa cobertura | 0,08-0,12<br>Poca<br>vegetación,<br>terrenos<br>cultivados o<br>naturales,<br>menos del 20%<br>del área con<br>buena<br>cobertura<br>vegetal | 0,06-0,08<br>Normal, posibilidad de<br>almacenamiento buena,<br>zonas húmedas,<br>pantanos, lagunas y lagos | 0,04-0,06<br>Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas planicies<br>de inundación o gran<br>cantidad de zonas<br>húmedas, lagunas o<br>pantanos. |
| **Almacenamiento**<br>**Superficial** | 0,10-0,12<br>Despreciable,<br>pocas depresiones<br>superficiales, sin<br>zonas húmedas | 0,08-0,10<br>Baja, sistema de<br>cauces<br>superficiales<br>pequeños bien<br>definidos, sin<br>zonas húmedas | 0,06-0,08<br>Posibilidad de<br>almacenamiento buena,<br>zonas húmedas,<br>pantanos, lagunas, lagos | 0,04-0,06<br>Capacidad alta, sistema<br>hidrográfico poco<br>definido, buenas planicies<br>de inundación o gran<br>cantidad de zonas<br>húmedas, lagunas o<br>pantanos |
| Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25 | Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25 | Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25 | Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25 | Si T > 10 años amplificar resultado por:<br>T = 25; C x 1,10 T = 50; C x 1,20 T = 100; C x 1,25 |

**Tabla 5.1: Coordenadas Puntos de Control**

| PUNTO DE CONTROL | COORDENADAS PUNTO DE ENCUENTRO OBRAS PROYECTO UTM | Col3 |
| --- | --- | --- |
| **PUNTO DE CONTROL** | **DATUM UTM WGS 84, HUSO 19 S** | **DATUM UTM WGS 84, HUSO 19 S** |
| **PUNTO DE CONTROL** | **ESTE** | **NORTE** |
| **QUEBRADA BESS 14** | 364.750 | 7.959.921 |

**Tabla 5.2: Características Morfológicas de las Cuencas Aportantes**

| PUNTO<br>DE<br>CONTROL | CARACTERÍSTICAS DE LA CUENCA APORTANTE | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **PUNTO**<br>**DE**<br>**CONTROL** | **Área**<br>**aportante**<br>**(Km2)** | **Largo**<br>**(km)** | **H min**<br>**(msnm)** | **H max**<br>**(msnm)** | **H media**<br>**(Msnm)** | **H med (m)** | **Desnivel**<br>**H (m)** | **Pendiente**<br>**media**<br>**cuenca**<br>**(m/m)** |
| **QUEBRAD**<br>**A BESS 14** | 17.986 | 10.39 | 62 | 556 | 389.520 | 327.520 | 494 | 0.059 |

**Tabla 5.3: Ubicación de estaciones meteorológicas seleccionadas**

| N° | ESTACIÓN METEOROLÓGICA DGA | CÓDIGO BNA | DATUM WGS 84,<br>HUSO 19 S | Col5 | ALTITUD<br>(msnm) |
| --- | --- | --- | --- | --- | --- |
| **N°** | **ESTACIÓN METEOROLÓGICA DGA** | **CÓDIGO BNA** | **ESTE** | **NORTE** | **NORTE** |
| 1 | Arica Oficina | 01310018-7 | 360.557 | 7.956.456 | 20 |
| 2 | Azapa | 01310019-5 | 375.451 | 7.952.288 | 365 |

**Tabla 5.4: Precipitaciones máximas en 24 horas anual disponibles**

| AÑO | AZAPA | ARICA OFICINA |
| --- | --- | --- |
| 1966 | 0.00 |  |
| 1967 | 0.00 | <br> |
| 1968 | 5.00 | <br> |
| 1969 | 1.00 | <br> |
| 1970 | 0.50 |  |
| 1971 | 0.00 | <br> |
| 1972 | 0.00 | <br> |
| 1973 | 0.90 |  |
| 1974 | 0.60<br> | 0.00 |
| 1975 | <br> | 1.80 |
| 1976 |  | 0.40 |
| 1977 | <br> | 0.40 |
| 1978 | <br> | 0.00 |
| 1979 |  | 0.00 |
| 1980 | 1.00 | 0.00 |
| 1981 | 1.10 | 0.00 |
| 1982 | 0.00 | 1.10 |
| 1983 | 0.00 | 0.00 |
| 1984 | 0.00 | 1.00 |
| 1985 | 0.00 | 0.00 |
| 1986 | 0.00 | 2.10 |
| 1987 | 0.00 | 1.80 |
| 1988 | 0.00 | 0.20 |
| 1989 | 0.00 | 0.20 |
| 1990 | 0.00 | 0.90 |
| 1991 | 0.00 | 0.00 |
| 1992 | 0.00 | 0.00 |
| 1993 | 1.50 | 3.00 |
| 1994 | 0.00 | 0.00 |
| 1995 | 0.00 | 2.00 |
| 1996 | 0.00 | 0.10 |
| 1997 | 3.00 | 4.10 |
| 1998 | 0.00 | 0.00 |
| 1999 | 0.00 | 0.00 |
| 2000 | 0.00 | 0.30 |
| 2001 | 0.00 | 0.50 |
| 2002 | 2.00 | 4.00 |
| 2003 | 8.20 | 2.00 |
| 2004 | 0.00 | 1.00 |
| 2005 | 0.00 | 0.00 |

**Tabla 5.5: Resumen de Distribución Adoptada**

| ESTACIÓN | DISTRIBUCIÓN | AIC | AICc | BIC | ADC | DISTRIBUCIÓN ADOPTADA |
| --- | --- | --- | --- | --- | --- | --- |
| **ARICA OFICINA** | **NORM** | 161.38 | 161.64 | 165.17 | 6.82 | **GEV ** |
| **ARICA OFICINA** | **LN** | 29.94 | 30.20 | 33.73 | 6.74 | 6.74 |
| **ARICA OFICINA** | **GUMBEL** | 136.01 | 136.27 | 139.80 | **6.44** | **6.44** |
| **ARICA OFICINA** | **GEV** | **-329.71** | **-329.18** | **-324.03** | 4791.89 | 4791.89 |

**Tabla 5.6: Resumen de Precipitaciones Adoptadas**

| ESTACIÓN<br>DGA | RESUMEN DE PRECIPITACIONES (mm) (MÉTODO DE ANÁLISIS DE FRECUENCIAS) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ESTACIÓN**<br>**DGA** | **T=2**<br>**(Años)** | **T=5**<br>**(Años)** | **T=10**<br>**(Años)** | **T=20**<br>**(Años)** | **T=25**<br>**(Años)** | **T=50**<br>**(Años)** | **T=100**<br>**(Años)** |
| Arica Oficina | 0.44 | 1.27 | 2.07 | 3.10 | 3.50 | 4.98 | 6.94 |

**Tabla 5.7: Resumen de Precipitaciones Calculadas considerando CC P25 y P75**

| ESTACIÓN DGA | RESUMEN DE PRECIPITACIONES (mm) (CAMBIO CLIMÁTICO) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ESTACIÓN DGA** | **T=2 (Años)** | **T=5 (Años)** | **T=10 (Años)** | **T=20 (Años)** | **T=25 (Años)** | **T=50 (Años)** | **T=100 (Años)** |
| Arica Oficina (P25) | 0.36 | 1.05 | 1.70 | 2.56 | 2.88 | 4.10 | 5.72 |
| Arica Oficina (P75) | 0.50 | 1.44 | 2.35 | 3.52 | 3.97 | 5.65 | 7.88 |

**Tabla 5.8: Cálculo coeficiente de escorrentía**

| FACTOR | INCIDENCIA | RANGO | VALOR |
| --- | --- | --- | --- |
| Relieve | Normal | 0.14-0.20 | 0.14 |
| Infiltración | Normal | 0.06-0.08 | 0.06 |
| Cobertura Vegetal | Extremo | 0.12-0.16 | 0.16 |
| Almacenamiento superficial | Alto | 0.08 - 0.10 | 0.08 |
| **C(T=10)** | **C(T=10)** | **C(T=10)** | **0.44** |

**Tabla 5.9: Estimación de Caudales de Crecida para diferentes T Método Racional MC Vol.3**

| P. Control | Área<br>(km2) | T<br>(años) | C(10<br>) | C(T)/C(10<br>) | C(T) | PPT/2<br>4h | CDtc | K | PP T/tc<br>(mm) | tc<br>(h) | I T<br>tc | Q<br>(m3/seg) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **P. Control** | **Área**<br>**(km2)** | **T **<br>**(años)** | **C(10**<br>**) ** | **C(T)/C(10**<br>**) ** | **C(T)** | **(mm)** | **(mm)** | **(mm)** | **(mm)** | **(mm)** | **(mm)** | **(mm)** |
| Quebrada<br>S/N | 17.99 | 2 | 0.44 | 1 | 0.44 | 0.44 | 0.495 | 1.1 | 0.24 | 1.3 | 0.18 | 0.40 |
| Quebrada<br>S/N | 17.99 | 5 | 5 | 1 | 0.44 | 1.27 | 1.27 | 1.27 | 0.69 | 0.69 | 0.53 | 1.17 |
| Quebrada<br>S/N | 17.99 | 10 | 10 | 1 | 0.44 | 2.07 | 2.07 | 2.07 | 1.13 | 1.13 | 0.86 | 1.89 |
| Quebrada<br>S/N | 17.99 | 20 | 20 | 1.05 | 0.462 | 3.1 | 3.1 | 3.1 | 1.69 | 1.69 | 1.3 | 3.00 |
| Quebrada<br>S/N | 17.99 | 25 | 25 | 1.1 | 0.484 | 3.5 | 3.5 | 3.5 | 1.91 | 1.91 | 1.46 | 3.53 |
| Quebrada<br>S/N | 17.99 | 50 | 50 | 1.2 | 0.528 | 4.98 | 4.98 | 4.98 | 2.71 | 2.71 | 2.08 | 5.49 |
| Quebrada<br>S/N | 17.99 | 100 | 100 | 1.25 | 0.55 | 6.94 | 6.94 | 6.94 | 3.78 | 3.78 | 2.9 | 7.97 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25 | 17.99 | 2 | 0.44 | 1 | 0.44 | 0.36 | 0.495 | 1.1 | 0.20 | 1.3 | 0.15 | 0.33 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25 | 17.99 | 5 | 5 | 1 | 0.44 | 1.05 | 1.05 | 1.05 | 0.57 | 0.57 | 0.44 | 0.97 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25 | 17.99 | 10 | 10 | 1 | 0.44 | 1.7 | 1.7 | 1.7 | 0.93 | 0.93 | 0.71 | 1.57 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25 | 17.99 | 20 | 20 | 1.05 | 0.462 | 2.56 | 2.56 | 2.56 | 1.40 | 1.40 | 1.07 | 2.48 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25 | 17.99 | 25 | 25 | 1.1 | 0.484 | 2.88 | 2.88 | 2.88 | 1.57 | 1.57 | 1.21 | 2.92 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25 | 17.99 | 50 | 50 | 1.2 | 0.528 | 4.1 | 4.1 | 4.1 | 2.23 | 2.23 | 1.72 | 4.53 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P25 | 17.99 | 100 | 100 | 1.25 | 0.55 | 5.72 | 5.72 | 5.72 | 3.12 | 3.12 | 2.40 | 6.59 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75 | 17.99 | 2 | 0.44 | 1 | 0.44 | 0.5 | 0.495 | 1.1 | 0.27 | 1.3 | 0.21 | 0.46 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75 | 17.99 | 5 | 5 | 1 | 0.44 | 1.44 | 1.44 | 1.44 | 0.78 | 0.78 | 0.60 | 1.33 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75 | 17.99 | 10 | 10 | 1 | 0.44 | 2.35 | 2.35 | 2.35 | 1.28 | 1.28 | 0.99 | 2.17 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75 | 17.99 | 20 | 20 | 1.05 | 0.462 | 3.52 | 3.52 | 3.52 | 1.92 | 1.92 | 1.48 | 3.41 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75 | 17.99 | 25 | 25 | 1.1 | 0.484 | 3.97 | 3.97 | 3.97 | 2.16 | 2.16 | 1.66 | 4.03 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75 | 17.99 | 50 | 50 | 1.2 | 0.528 | 5.65 | 5.65 | 5.65 | 3.08 | 3.08 | 2.37 | 6.25 |
| Quebrada<br>S/N<br>CAMBIO<br>CLIMATICO<br>P75 | 17.99 | 100 | 100 | 1.25 | 0.55 | 7.88 | 7.88 | 7.88 | 4.29 | 4.29 | 3.30 | 9.08 |

**Tabla 5.10: Resultados Transposición de Caudales**

| T RETORNO | CAUDAL (m3/s) |
| --- | --- |
| **T RETORNO** | **QUEBRADA BESS14** |
| 2 | 0.19 |
| 5 | 0.40 |
| 10 | 0.59 |
| 20 | 0.81 |
| 25 | 0.89 |
| 50 | 1.16 |
| 100 | 1.48 |

**Tabla 5.11: Resultados Hidrograma Unitarios SCS**

| TR | Pt | Q | qp |
| --- | --- | --- | --- |
| 2 | 0.21 | 0.00 | 0.003 |
| 5 | 0.60 | 0.06 | 0.060 |
| 10 | 0.98 | 0.24 | 0.228 |
| 20 | 1.47 | 0.56 | 0.528 |
| 50 | 2.36 | 1.26 | 1.192 |
| 100 | 3.29 | 2.08 | 1.960 |

**Tabla 5.12: Coeficiente De Rugosidad Manning Según Cowan**

| LUGAR | VALORES DE COWAN | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **LUGAR** | **nb** | **n1** | **n2** | **n3** | **n4** | **m ** | **MANNING (n)** |
| Cauce y ribera | 0.02 | 0.008 | 0.005 | 0.02 | 0.005 | 1 | 0.058 |

**Tabla 5.13: Condición de Borde**

| CAUCE | PENDIENTE (m/m) |
| --- | --- |
| Quebrada | 0.08 |
