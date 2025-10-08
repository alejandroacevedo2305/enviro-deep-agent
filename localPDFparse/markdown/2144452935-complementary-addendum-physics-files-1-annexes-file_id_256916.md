---
title: Sin título
author: Pablo
date: D:20200909234227-03'00'
language: es
type: report
pages: 37
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. INTRODUCCIÓN
  - 1 Plano de Zonificación PRC1 . Plan Regulador Comunal de Linares. 2017. Chile.
  - 2. MODELACIÓN DE VARIABLES METEOROLÓGICAS
  - 2 The Weather Research & Forecasting Model, NCAR/UCAR, https://www.mmm.ucar.edu/weather-research-and-forecasting
  - 3. CÁLCULO DE INCERTIDUMBRE
  - 4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE
  - 4 A User’s Guide for the CALPUFF Dispersion Model (Version 5), Earth Tech Inc., enero de 2000.
  - 5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS
  - 6. RESULTADOS DE LA DISPERSIÓN E IMPACTO POR OLORES
  - 7. CONCLUSIONES
  ... y 1 secciones más
-->

**Modelación de**

**Dispersión e Impacto**

**por Olores**

**Engorda Los Queltehues**

**Santiago - Chile**

**Septiembre 2020**

**CONFIDENCIAL**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**CONTENIDO**

1. INTRODUCCIÓN ..................................................................................................................................................... 2

2. MODELACIÓN DE VARIABLES METEOROLÓGICAS ..................................................................................................... 3

3. CÁLCULO DE INCERTIDUMBRE .............................................................................................................................. 12

4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE ....................................................................... 17

5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS ............................................................................ 18

6. RESULTADOS DE LA DISPERSIÓN E IMPACTO POR OLORES ..................................................................................... 25

7. CONCLUSIONES ................................................................................................................................................... 28

Página **1** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

# 1. INTRODUCCIÓN

El presente informe da cuenta de los resultados obtenidos de la modelación de dispersión de olores y los

impactos asociados al proyecto “Engorda Los Queltehues”, para ser presentado al Servicio de Evaluación

Ambiental por medio de la Declaración de Impacto Ambiental correspondiente.

Las instalaciones del proyecto se ubican en Camino a Palmilla S/N, Comuna de Linares, Provincia de Linares,

Región del Maule. La ubicación se encuentra fuera del área comprendida en el Plan Regulador Comunal de

Linares, sin embargo, se encuentra inmediatamente adyacente a una zona de tipificación ZAP (Zona de

Actividades Productivas) [1] .

**Tabla 1.** Coordenadas punto representativo del proyecto (Datum WGS 84).

|Coordenadas UTM Engorda Los Queltehues.|Col2|
|---|---|
|Coordenada Este (m)|Coordenada Norte (m)|
|261480|6029364|

Las actividades de engorda de bovinos se concentran en un área de 5,1 hectáreas aproximadamente, en

donde se encuentran las principales unidades de producción, como los galpones de animales, zona de

acopio y compostaje de guano, zona de recepción y acopio de alimentos (silo de chala de maíz). Además,

se cuenta con un predio de 110 hectáreas en los cuales se realiza la incorporación del guano compostado

proveniente de las camas retiradas de cada uno de los galpones de animales. Todas las actividades

mencionadas anteriormente son susceptibles de emitir olores molestos, cuyo impacto será estimado en la

presente modelación.

____________________________________________________

# 1 Plano de Zonificación PRC1 . Plan Regulador Comunal de Linares. 2017. Chile.

[http://www.goremaule.cl/goremaulenuevo/index.php/concursos/2-uncategorised/434-plan-regulador-comuna-de-linares](http://www.goremaule.cl/goremaulenuevo/index.php/concursos/2-uncategorised/434-plan-regulador-comuna-de-linares)

Página **2** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

# 2. MODELACIÓN DE VARIABLES METEOROLÓGICAS

Para la generación de la base de datos de variables meteorológicas, se utilizó el modelo WRF versión 3.9.1.
Éste es un modelo meteorológico de alta resolución, desarrollado para la simulación de variables

meteorológicas, mediante la resolución de las ecuaciones físicas que describen los movimientos de la

atmósfera, utilizando aproximaciones basadas en métodos numéricos. Este modelo se encuentra en

constante desarrollo y mejora por medio de una asociación colaborativa, principalmente entre el National

Center for Atmospheric Research (NCAR, USA), National Oceanic and Atmospheric Administration (NCEP,

USA), Forecast Systems Laboratory (FSL, USA), Air Force Weather Agency (AFWA, USA), el Naval Research

Laboratory, University of Oklahoma, y la Federal Aviation Administration (FAA, USA). WRF es un Software

Libre y comunitario, por lo que su desarrollo y mejoramiento se realiza en distintos sitios alrededor del
mundo por voluntarios que deseen contribuir al proyecto [2] .

En el presente informe se utilizó la información meteorológica correspondiente al último año

meteorológico (2018). Esta información se obtuvo a partir del CISL Research Data Archive (NCAR, USA),

utilizándose el conjunto de datos de entrada ds083.2. NCAR (National Center for Atmospherical Reseach)

ofrece a los científicos de Estados Unidos y del mundo, una gran cantidad de herramientas, desde modelos

comunitarios hasta aviones de investigación, supercomputadores y talleres. Los científicos internos de

NCAR colaboran con sus colegas en el mundo académico, el gobierno y el sector privado para construir,
refinar y ampliar los recursos de la comunidad de NCAR para que sean lo más relevantes y útiles posible. [3]

Para el área de influencia, la configuración del modelo WRF, comprendió la parametrización de variables

propias de los fenómenos de micro escala que inciden en la dispersión de los contaminantes, esto es:

parametrizaciones de microfísica de nubes, fenómenos radiativos, altura de la capa de mezcla y fenómenos

turbulentos causados por la orografía. En la Tabla 2 se detallan las configuraciones de importancia con las

cuales se ejecutó la modelación.

____________________________________________________

# 2 The Weather Research & Forecasting Model, NCAR/UCAR, https://www.mmm.ucar.edu/weather-research-and-forecasting
model (Visitado en agosto de 2019).

3 **National Center for Atmospheric Research** [, NCAR/UCAR, https://ncar.ucar.edu/what-we-offer](https://ncar.ucar.edu/what-we-offer) (Visitado en agosto de 2019).

Página **3** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

|Tabla 2. Configuración física del mo Centro Latitud|odelo WRF 3.9.1, dominio más pequeño. -35.8544|
|---|---|
|~~Centro Latitud ~~<br>|~~-35.8544 ~~<br>|
|~~Centro Longitud ~~<br>|~~-71.64776 ~~<br>|
|~~Condiciones de entrada ~~<br>|~~FNL DS083.2 2017 ~~<br>|
|~~Proyección cartográfica ~~<br>|~~Mercator ~~<br>|
|~~Puntos en X ~~<br>|~~60 ~~<br>|
|~~Puntos en Y ~~<br>|~~60 ~~<br>|
|~~Topografía ~~<br>|~~SRTM3 (Aproximadamente 100 metros) ~~<br>|
|~~Uso de suelo ~~<br>|~~USGS (Aproximadamente 1 Kilómetro) ~~<br>|
|~~Resolución horizontal (Km) ~~<br>|~~0,5 ~~<br>|
|~~Resolución vertical (niveles) ~~|~~27 niveles hasta 10 hPa ~~<br>|
|Microfísica|~~“WRF Single-Moment 8-class scheme”.~~<br>Esquema micro físico de 8 clases, que<br>incorpora además de líquidos, hielo y nieve.<br>Parametrización ideal para simulaciones a<br>alta resolución. <br>|
|Radiación (Onda larga y Corta)|~~“RRTMG”. Esquema radiativo simple y~~<br>eficiente, capaz de simular los fenómenos<br>radiativos de onda larga a través del<br>solapamiento de capas nubosas. <br>|
|Modelo de suelo|~~“ETA Similarity”. Esquema fenómenos suelo-~~<br>atmósfera ampliamente utilizado por otros<br>modelos numéricos además de WRF, basado<br>en Monin-Obukhov (esquema requerido por<br>el modelo de dispersión) que incorpora la<br>longitud de rugosidad térmica Zilitinkevich y<br>funciones de similitud estándar desde tablas<br>predefinidas. <br>|
|Interacción suelo atmósfera|~~“Noah Land Surface Model”. Esquema~~<br>utilizado por NCEP/NCAR/AFWA que<br>incorpora temperatura y humedad del suelo<br>en cuatro capas. <br>|
|Capa planetaria|~~“Mellor-Yamada- Janjic”. Ampliamente~~<br>utilizado operacionalmente por otros<br>modelos además de WRF. Basado en un<br>régimen turbulento unidimensional de<br>energía cinética vertical local.|

Página **4** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

El dominio más pequeño definido, considera una zona de 10x10 kilómetros, con un dominio superior

de 30x30 kilómetros y otro principal de 90x90 kilómetros, los que se consideran lo suficientemente

amplios como para incorporar fenómenos de escala sinóptica, propios de la zona como los sistemas

frontales o la incursión de altas frías migratorias, configurado además a una alta resolución de 100

metros en su dominio más pequeño, con la capacidad de incorporar fenómenos de meso escala como

oscilaciones en la capa altura de la mezcla por efecto radiativo o fenómenos de intercambio turbulento

causados por la orografía. En la Figura 1, Figura 2 y Figura 3, se presentan detalles del dominio

considerado en la modelación.

**Figura 1.** Emplazamiento geográfico del dominio considerado para la modelación de variables
meteorológicas y de dispersión.

Página **5** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 2.** Detalle del dominio considerado para la modelación de variables meteorológicas y de
dispersión, información topográfica utilizada por el modelo (SRTM3 a 90 metros de resolución).

Página **6** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 3.** Grilla de modelación de 60x60, a 500 metros de resolución espacial, definiendo un dominio de

30x30 kilómetros de extensión.

De este modo, se logró tener una base de datos de variables meteorológicas para el área de interés, con

resolución horizontal de 500x500 metros, con una grilla de 60x60 para 27 niveles de altitud llegando al

tope de la atmósfera y resolución temporal de una hora para todo 2018, información requerida como base

por el modelo de dispersión.

A continuación, en la Figura 4, Figura 5, Figura 6 y Figura 7 se muestran los campos de vientos

característicos de la zona para las estaciones del año cálidas durante el período diurno y el período

nocturno, como también los campos de vientos característicos de la zona para las estaciones del año frías

durante el período diurno y nocturno.

Página **7** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 4.** Campos de vientos durante el período diurno en estaciones cálidas. Se observa el efecto brisa

valle-montaña.

Página **8** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 5.** Campos de vientos durante el período nocturno en estaciones cálidas. Se observa el sentido
contrario del régimen de vientos respecto al día (efecto brisa montaña-valle).

Página **9** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 6.** Campos de vientos durante el período diurno en estaciones frías. Se observa un incremento en
la magnitud respecto al viento diurno durante el período cálido.

Página **10** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 7.** Campos de vientos durante el período nocturno en estaciones frías. Se observa un incremento
en la magnitud respecto al viento nocturno durante el período frío.

Página **11** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

# 3. CÁLCULO DE INCERTIDUMBRE

Para el cálculo de incertidumbre, la estación más cercana con información pública disponible corresponde

a la estación de monitoreo Linares, emplazada en la zona urbana de la ciudad del mismo nombre, estación

propiedad del Ministerio del Medio Ambiente, cuyos datos públicos se encuentran en el Sistema de

Información Nacional de Calidad del Aire (SINCA).

**Tabla 3.** Información de la estación Linares.

|Estación|UTM Este (m)|UTM Norte (m)|Altitud (m)|
|---|---|---|---|
|Linares|265805|6031030|160|

La variable a analizar corresponde a la Magnitud y Dirección del viento, puesto que esta combinación de

variables crucial en el transporte y difusión de contaminantes. Se extrajo desde el dominio de modelación,

el punto de grilla correspondiente a la posición de la estación, de manera de calcular la incertidumbre de

los datos modelados versus los datos observados.

Página **12** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 8** . Rosa de vientos observada en la estación Linares.

Página **13** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 9.** Rosa de vientos modelada para el punto de grilla ubicado en la estación Linares.

Página **14** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 10.** Ciclo diario de la magnitud del viento observada y modelada en la estación Linares.

**Figura 11.** Ciclo anual de la magnitud del viento observada y modelada en la estación Linares.

Página **15** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

Según se observa en la Figura 8 y Figura 9, se puede ver una correcta representación de las frecuencias de

las componentes, no ocurre lo mismo con la magnitud, donde se puede apreciar una sobreestimación de

las magnitudes del viento.

En la Figura 10 y Figura 11, se observa una constante sobreestimación de las magnitudes del viento de

parte del modelo, constante durante todo el día y constante durante todo el año, a diferencia del mes de

enero.

Para propósitos de determinar la incertidumbre del modelo, se toma de base la siguiente información:

 Magnitud del viento promedio observado: 1,75 m/s

 Magnitud del viento promedio modelado: 2,37 m/s

De los datos anteriores se desprende que el error porcentual de la velocidad del viento está determinado

por la fórmula:

((2,37 - 1,75) * 100 / 1,75) = 35,43%

Dado que la magnitud del viento modelada sobreestima los valores observados, su efecto consiste en una

disminución de las unidades de olor, este efecto debe ser considerado en la corrección por incertidumbre.

Corregido = (1 + 0,3543) * Modelado

Corregido = 1,3543 * Modelado

De esta forma los resultados modelados deberían ser multiplicados por 1,3543 de manera de corregir el

sesgo del modelo. Para propósitos de la presente evaluación, se aplicará esta corrección por exceso, de

manera de considerar un escenario conservador.

A continuación, se presentan los estadísticos requeridos para asegurar la incertidumbre de la información

modelada versus observada:

**Tabla 4** . Análisis de incertidumbre.

|Estadístico|Viento|Temperatura|
|---|---|---|
|~~Sesgo~~<br>|~~1,39307754~~<br>|~~3,286493~~<br>|
|~~Error Medio Cuadrático~~<br>|~~1,05158088~~<br>|~~2,720727~~<br>|
|~~Coeficiente de Correlación~~<br>|~~0,61361588~~|~~0,897536~~|

Tal como se puede apreciar, el coeficiente de correlación es mayor que 0,5 para la variable viento, y

respecto a la temperatura, el coeficiente de correlación es de 0,9, asegurando que la modelación, tiene

una buena captura de las tendencias en general. De todas maneras, según lo anteriormente expuesto, de

acuerdo al cálculo de incertidumbre, el modelo tiende a sobreestimar las magnitudes del viento,

mejorando la dispersión y con ello, reduciendo las concentraciones, por lo que se aplicará el factor de

corrección antes calculado.

Página **16** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

# 4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE

Para la presente modelación se han seguido los procedimientos establecidos por la “Guía metodológica de

uso de modelos de dispersión en el SEIA”, la cual recomienda el uso de CALPUFF como modelo de

dispersión de contaminantes. Para propósitos particulares de este estudio, se ha utilizado la versión 6.4.

CALPUFF es un modelo lagrangiano de dispersión de contaminantes basado en un sistema de “puffs”, los

cuales varían en su forma y posición en función del tiempo, del espacio, la estabilidad atmosférica y los

vientos, entre otros parámetros. Es un modelo que soporta múltiples tipos de fuentes con diferentes tipos

de tratamiento para cada una de ellas: Fuentes de área, fuentes de volumen, fuentes puntuales y fuentes

de línea [4] .

**Tabla 5.** Configuración del dominio del modelo CALPUFF.

|Ítem|Valor|
|---|---|
|~~Centro UTM E (m)~~<br>|~~260899~~<br>|
|~~Centro UTM N (m)~~<br>|~~6028963~~<br>|
|~~Resolución espacial (m)~~<br>|~~500~~<br>|
|~~Puntos en X~~<br>|~~60~~<br>|
|~~Puntos en Y~~<br>|~~60~~<br>|
|~~Topografía~~<br>|~~SRTM3 (Aproximadamente 90 metros de resolución)~~<br>|
|~~Uso de suelo~~|~~GLCC (USGS30 aproximadamente a 1 Kilómetro e resolución)~~|

____________________________________________________

# 4 A User’s Guide for the CALPUFF Dispersion Model (Version 5), Earth Tech Inc., enero de 2000.

Página **17** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

# 5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS

Para la modelación se consideraron 8 fuentes emisoras de olor. El detalle de cada fuente se describe a

continuación:

**Tabla 6** . Fuentes de olor consideradas para la modelación.

|Zona o Proceso|Fuente de<br>Olor|Tipo de<br>Fuente|Dimensiones<br>(m)|Área<br>(m2)|Coordenada<br>UTM Este<br>(m)|Coordenada<br>UTM Norte<br>(m)|Horas de<br>Emisión<br>por<br>Jornada<br>Laboral|Actividad/Material|
|---|---|---|---|---|---|---|---|---|
|**Almacenamiento**<br>**de Alimentos**|Acopio<br>Chala Maíz|Superficial<br>Pasiva|19.6 x 4.5 x 2|120|328706|6307686|24, todos<br>los días|Acopio de<br>alimento / Silo<br>|
|**Galpones**|Galpón 1|Superficial<br>Pasiva|117 x 25.5 x<br>2|2984|260868|6028984|24, todos<br>los días|~~Engorda de~~<br>Animales / Cama<br>Caliente<br>|
|**Galpones**|Galpón 2|Superficial<br>Pasiva|103 x 30 x 2|3090|260900|6028998|24, todos<br>los días|~~Engorda de~~<br>Animales / Cama<br>Caliente<br>|
|**Galpones**|Galpón 3|Superficial<br>Pasiva|130 x 30 x 2|3900|260972|6028906|24, todos<br>los días|~~Engorda de~~<br>Animales / Cama<br>Caliente|
|**Acopio de Cama**<br>**Caliente**|Patio de<br>Compostaje|Superficial<br>Pasiva|61 x 27 x 2<br>|1647|260922|6028912|24, todos<br>los días|Acopio de guano /<br>Guano<br>|
|**Cementerio de**<br>**Animales**|Cementerio|Superficial<br>Pasiva|~~Campo de~~<br>dimensiones<br>irregulares|2500|260855|6028876|24, todos<br>los días|~~Disposición~~<br>(entierro) de<br>animales muertos<br>|
|**Fosa Séptica**<br>|Fosa<br>Séptica|Superficial<br>Pasiva|1.5 x 1.5 x 2<br>|2.25|260857|6028898|24, una vez<br>al mes<br>|~~Acumulación de~~<br>aguas servidas<br>domiciliarias<br>|
|~~**Incorporación de**~~<br>**Enmienda a**<br>**Suelo Agrícola**<br>|Campo San<br>Luis|Superficial<br>Pasiva|~~Campo de~~<br>dimensiones<br>irregulares|200000|261101|6029218|~~20 días x~~<br>año,<br>septiembre|~~Incorporación de~~<br>guano animal al<br>suelo|

Página **18** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Tabla 7** . Caracterización de olores.

|Zona o Proceso|Fuente de Olor|Calidad|Olor|Tono<br>Hedónico|Intensidad|Concentración<br>(Uo/Nm3)|
|---|---|---|---|---|---|---|
|~~**Almacenamiento de**~~<br>**Alimentos**|~~Acopio Chala~~<br>Maíz|Vinagre, dulce<br>|Compuesto|~~- 2~~<br>Desagradable<br>|Medio|555|
|**Galpones**|Galpón 1*|~~Amoniaco,~~<br>guano<br>|Compuesto|~~-2~~<br>Desagradable<br>|Medio|201|
|**Galpones**|Galpón 2*|~~Amoniaco,~~<br>guano<br>|Compuesto|~~-2~~<br>Desagradable<br>|Medio|201|
|**Galpones**|Galpón 3|~~Amoniaco,~~<br>guano|Compuesto|~~-2~~<br>Desagradable<br>|Medio|201|
|**Acopio de Cama**<br>**Caliente**<br>|Patio de<br>Compostaje|Guano|Compuesto|~~-1~~<br>Levemente<br>Desagradable|Suave|No Aplica**|
|~~**Cementerio de**~~<br>**Animales**|Cementerio|Tierra mojada|Compuesto|0 neutro<br>|Muy Suave<br>|74|
|**Fosa Séptica**<br>|Fosa Séptica|Agua|Compuesto|~~0 neutro (Sin~~<br>Olor)<br>|~~Muy Suave, Sin~~<br>Olor|101|
|~~**Incorporación de**~~<br>**Enmienda a Suelo**<br>**Agrícola**|Campo San Luis|Tierra húmeda,<br>guano|Compuesto|~~-1~~<br>Levemente<br>Desagradable|Muy Suave|242|

- Galpones 1 y 2 se homologaron a Galpón 3

** No se realizó medición debido a que no existía acopio de guano en ese momento, ya que fue utilizado

como enmienda y por labores de construcción de loza en el lugar, que albergará las labores de compostaje

en el futuro cercano. Para efectos de modelación, se homologará a la tasa de emisión para Galpón 3.

Página **19** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figuras 12 y 13** . Ubicación de las fuentes de emisión.

Página **20** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

Las fuentes fueron seleccionadas mediante una visita a terreno por parte de panelistas expertos en

monitoreo de olores. Estas fuentes representan los principales focos de emisión de olor dentro del proceso

de engorda de animales. También se agregaron fuentes a solicitud de la autoridad (Fosa Séptica,

Cementerio de Animales), posterior a visitas de fiscalización.

Respecto del tiempo de emisión de olores asociado a la incorporación de guano compostado en suelos

agrícolas, se relacionó esta característica con la descomposición de la materia orgánica presente en la

enmienda aplicada, para poder realizar una estimación del tiempo de olor asociado a esta actividad. Según
algunas investigaciones [5], se puede estimar la descomposición de la materia orgánica presente en

enmiendas, al ser incorporada a suelos, en 10-20 días aproximadamente. Esto puede observarse en el

siguiente gráfico.

**Figura 14.** Actividad biológica, medida como evolución de CO 2, para 3 tipos de suelo y 3 dosis de aplicación de
biosólidos. Adicionalmente, se muestra el ajuste a un modelo cinético de primer orden [5] .

___________________________________________

5 Actividad biológica en suelos de las series Colina, Lonquén y Los Morros (RM), tratados con dosis crecientes de biosólidos

urbanos. Riquelme, Paula. Fac. de Cs. Agronómicas, Universidad de Chile. 2013. Chile.

Página **21** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

Se puede apreciar claramente para los distintos tipos de suelo y dosis de aplicación de enmienda, un rápido

aumento en la emisión de CO2, para luego alcanzar una estabilización entre los días 10 y 20. Relacionando

la estabilización con la descomposición de materia orgánica, podría asumirse que se produce en su mayoría

entre los 10-20 días posteriores a su aplicación. Por otra parte, considerando que la materia orgánica

presente en los biosólidos, o guanos compostados para el presente caso, es gran causante de la emisión

de olores molestos, podemos estimar, para un peor escenario, un total de 20 días de emisión de olores

desde el momento de la incorporación del guano compostado al suelo. Es importante mencionar que, en

la incorporación de guano, a diferencia de la aplicación, se produce el mezclado y tapado inmediato del

material incorporado, lo que ayuda a disminuir la emisión de olores molestos y favorece la descomposición

de la materia orgánica existente.

Para la presente modelación se utilizaron datos de tasas de emisión obtenidos a partir de una campaña de
muestreo y determinación mediante olfatometría dinámica, realizada el día 3 de Julio de 2020, por la
empresa CGA Ambiental.

De acuerdo al reporte:

- La toma de muestra se realizó en función de la Norma Chilena 3386:2015. [6]

- El análisis de las muestras se realizó según NCh 3190:2010 [7]

Las normas mencionadas anteriormente dan cuenta de la metodología y procedimientos
adecuados para la toma de muestra y la determinación de su concentración.

__________________________________________________

6 Instituto Nacional de Normalización (2015). Norma Chilena 3386:2015 “Muestreo estático para olfatometría”. Chile.
7 Instituto Nacional de Normalización (2010). Norma Chilena 3190:2010 “Calidad del aire - Determinación de la concentración
de olor por olfatometría dinámica”. Chile.

Página **22** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

Los valores de emisión utilizados se muestran en la Tabla 8.

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues Los valores de emisión utilizados se muestran en la Tabla 8. -->

**Tabla 8: ** . Tasas de emisión por unidad.**

| Fuente de Olor | Factor de Emisión<br>(Uo/s*m2) | Tasa de Emisión Total<br>(Uo/s) |
| --- | --- | --- |
| Área Expuesta Silo | 4,624 | 554,9 |
| Galpón 1* | 1,675 | 2351,7 |
| Galpón 2* | 1,675 | 1646,5 |
| Galpón 3 | 1,675 | 2155,7 |
| Patio de Compostaje* | 1,28 | 2758,7 |
| Cementerio | 0,614 | 1535 |
| Fosa Séptica | 0,839 | 1,9 |
| Campo San Luis | 2,014<br> | 402800<br> |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- - Homologado a Galpón 3 Respecto a los receptores definidos, se consideraron 10 receptores discretos alrededor del proyecto, tal -->
<!-- FIN TABLA 8 -->


**Tabla 8** . Tasas de emisión por unidad.

|Fuente de Olor|Factor de Emisión<br>(Uo/s*m2)|Tasa de Emisión Total<br>(Uo/s)|
|---|---|---|
|Área Expuesta Silo|4,624|554,9|
|Galpón 1*|1,675|2351,7|
|Galpón 2*|1,675|1646,5|
|Galpón 3|1,675|2155,7|
|Patio de Compostaje*|1,28|2758,7|
|Cementerio|0,614|1535|
|Fosa Séptica|0,839|1,9|
|Campo San Luis|2,014<br>|402800<br>|

 - Homologado a Galpón 3

Respecto a los receptores definidos, se consideraron 10 receptores discretos alrededor del proyecto, tal

como lo muestra la Figura 15.

**Figura 15.** Receptores definidos dentro del dominio de modelación.

Página **23** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

La ubicación en detalles de los receptores definidos se presenta en la Tabla 9.

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues La ubicación en detalles de los receptores definidos se presenta en la Tabla 9. -->

**Tabla 9: ** . Ubicación de los receptores discretos definidos dentro del dominio de la modelación.**

| Punto | UTM E (m) | UTM N (m) | Altitud<br>(m) | Altura<br>(m) | Distancia aproximada<br>al proyecto (m) |
| --- | --- | --- | --- | --- | --- |
| 1 | 260988 | 6030345 | 143,36 | 2 | 873 |
| 2 | 262817 | 6030555 | 149,51 | 2 | 1857 |
| 3 | 263888 | 6030030 | 154,73 | 2 | 2508 |
| 4 | 262816 | 6027694 | 155,15 | 2 | 1954 |
| 5 | 259214 | 6027299 | 143,69 | 2 | 2198 |
| 6 | 257785 | 6029706 | 135,51 | 2 | 3012 |
| 7 | 259696 | 6031070 | 136,79 | 2 | 2002 |
| 8 | 261616 | 6029545 | 146,01 | 2 | 326 |
| 9 | 259849 | 6029452 | 142,19 | 2 | 974 |
| 10 | 262112 | 6028126 | 150,18 | 2 | 1154 |

<!-- Estadísticas: 10 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas cercanas al proyecto, ya que principalmente en estas se concentra la población susceptible de ser afectada por -->
<!-- FIN TABLA 9 -->


**Tabla 9** . Ubicación de los receptores discretos definidos dentro del dominio de la modelación.

|Punto|UTM E (m)|UTM N (m)|Altitud<br>(m)|Altura<br>(m)|Distancia aproximada<br>al proyecto (m)|
|---|---|---|---|---|---|
|1|260988|6030345|143,36|2|873|
|2|262817|6030555|149,51|2|1857|
|3|263888|6030030|154,73|2|2508|
|4|262816|6027694|155,15|2|1954|
|5|259214|6027299|143,69|2|2198|
|6|257785|6029706|135,51|2|3012|
|7|259696|6031070|136,79|2|2002|
|8|261616|6029545|146,01|2|326|
|9|259849|6029452|142,19|2|974|
|10|262112|6028126|150,18|2|1154|

Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas cercanas al

proyecto, ya que principalmente en estas se concentra la población susceptible de ser afectada por

potenciales emisiones de malos olores. Se agregaron también, a solicitud de la autoridad, los puntos

receptores utilizados en el estudio de impacto por ruidos.

Página **24** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

# 6. RESULTADOS DE LA DISPERSIÓN E IMPACTO POR OLORES

A continuación, se presentan los resultados obtenidos para la modelación de olores correspondiente al

proyecto en evaluación.

La Figura 16 corresponde a una vista general de todo el dominio considerado, donde se puede apreciar el
área comprendida por la isodora 1 Uo/m [3], utilizando el criterio de Percentil 98 para los valores promedios

horarios diarios.

**Figura 16.** Resultados de la modelación de dispersión de olores, P98.

Página **25** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

A continuación, se presenta el detalle del área de influencia [6], definida por la isodora correspondiente a 1
Uo/m [3], utilizando el criterio de Percentil 98.

**Figura 17.** Área de influencia por olores para el presente proyecto.

____________________________________________________

6 Guía para la predicción y evaluación de impactos por olor en el SEIA, Servicio de Evaluación Ambiental (SEA), 2017.

Página **26** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

Se puede apreciar claramente que los receptores 2 y 8 quedan dentro del área de influencia por olores del

proyecto, mientras que los demás receptores quedan fuera de la misma. El receptor 8 está dentro del

mismo terreno del cual es parte el proyecto actual.

En la Tabla 10 se presenta un detalle de los máximos valores horarios del día calculados para cada receptor

discreto definido, junto a los valores obtenidos para el Punto de Máximo Impacto.

**Tabla 10** . Valores de concentración (Uo/m [3] ) modelados para cada uno de los receptores discretos

definidos.

|Receptor|P98|
|---|---|
|~~1 ~~<br>|~~0,52~~<br>|
|~~2 ~~<br>|~~1,50~~<br>|
|~~3 ~~<br>|~~0,37~~<br>|
|~~4 ~~<br>|~~0,12~~<br>|
|~~5 ~~<br>|~~0,24~~<br>|
|~~6 ~~<br>|~~0,02~~<br>|
|~~7 ~~<br>|~~0,05~~<br>|
|~~8 ~~<br>|~~11,13~~<br>|
|~~9 ~~<br>|~~0,17~~<br>|
|~~10~~<br>|~~0,29~~<br>|
|~~PMI (261149E, 6029214N)~~|~~60,80~~|

En el caso del receptor 2, que queda inmerso dentro del área de influencia, es interesante analizar el valor
máximo obtenido, correspondiente a 1,5 Uo/m [3] . Este valor no es demasiado alto e incluso está por debajo

del valor máximo observado en algunos casos de legislación internacional en relación a olores.

El punto de máximo impacto presenta un alto valor, 60,8 Uo/m [3], igualmente el valor de concentración en
el receptor 8 se puede considerar alto (11,13 Uo/m [3] ), pero ambos se encuentran dentro de las

dependencias del proyecto en evaluación, por lo tanto, no presentan una molestia para el entorno cercano

al proyecto.

Página **27** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

# 7. CONCLUSIONES

Los resultados permiten cuantificar las molestias causadas por las emisiones de olores. La escala de
percepciones y concentración de olores generalmente aceptada a nivel internacional se resumen en la
siguente estructura :

**Tabla 11.** Concentración y percepción.

|Concentracion|Percepcion|
|---|---|
|1 Uo/m3|50% de la población puede comenzar a percibir un olor|
|3 Uo/m3|50% de la población puede reconocer o comenzar a reconocer un olor<br>|
|5 Uo/m3|~~El olor es calificable y puede comenzar a recibirse quejas (puede ser~~<br>identificado)|
|10 Uo/m3|Los olores son reconocibles y se pueden recibir reclamos|

Es importante considerar el limite que se debe alcanzar para que exista una queja, ya que estas no
dependen en exclusiva de un valor fijo; la percepción de olores molestos es un tema subjetivo, relacionado
con la sensibilidad individual de cada persona ante la presencia de olores molestos; la existencia de quejas
dependerá también de otros factores como la intensidad de los olores percibidos, de su agresividad, de su
apreciación (agradable o desagradable), de su frecuencia y de su permanencia. Varias jurisdicciones
alrededor del mundo han implementado con éxito programas de gestión de olores, que proponen criterios
de percepción de olor que oscilan entre 1 y 10 Uo/m3.

Como referencia, se cita la Guía Técnica Preliminar “Horizontal Guidance for Odour Part 1 - Regulation and
Permitting” [7] de la Integrated Pollution Prevention and Control (IPPC), mecanismo regulatorio
medioambiental de la Unión Europea. En este documento se proponen los siguientes criterios de inmisión
según el tipo de actividad.

____________________________________________________

# 7 Horizontal Guidance for Odour Part 1 - Regulation and Permitting. Scotish Environment Prevention Agency/Environment and

[Heritage Service/UK Environmet Agency. 2002. https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-](https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-Prevention-and-Control-part1.pdf)

[Prevention-and-Control-part1.pdf](https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-Prevention-and-Control-part1.pdf)

Página **28** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Tabla 12.** Valores de inmisión según actividad, IPPC.

|Ofensividad<br>Relativa del<br>Olor|Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales)|Tipo de Actividad Relacionada|
|---|---|---|
|ALTA|1,5 Uo/m3|Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales|
|MEDIA|3 Uo/m3|Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva|
|BAJA<br>|6 Uo/m3|Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías|

Esta guía recomienda valores de concentración según el nivel de ofensividad (alta, media o baja) para cada

olor molesto asociado a cada tipo de faena, indicando algunos ejemplos de ellas. Esta guía considera el

percentil 98 de los valores horarios promedio para un año.

Considerando los resultados obtenidos para el presente proyecto, ligado a la actividad ganadera, sería
aceptable una emisión que no supere las 3 unidades de olor por metro cubico (3 Uo/m [3] ). Para los
receptores propuestos, este valor es superado solamente en el receptor 8 (11,13 Uo/m [3] ), pero como se

mencionó anteriormente, este receptor se encuentra dentro del terreno al cual se circunscribe el proyecto
(Fundo San Luis). **Todos los demás receptores presentan valores bajo 3 Uo/m** **[3]** **.**

Página **29** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

En lo concerniente a la incorporación de enmienda orgánica al suelo agrícola, cabe mencionar que el olor

percibido al momento de la incorporación para la medición de olfatometría fue relativamente bajo, y esto
se ve reflejado en su tasa de emisión específica (1,28 Uo/m [2] *s), valor relativamente bajo comparado con

el de otras fuentes; también se ve reflejado en su clasificación de tono hedónico, que presenta un valor de

-1 (Levemente Desagradable, Tabla 6). Sin embargo, debido a su larga extensión, termina representando
un 97,3% (402800 Uo/s) de la tasa de emisión total (413804,4 Uo/s). En ese sentido, los resultados indican

que es el principal aporte a las emisiones de olor del proyecto. Se puede deducir que el principal factor

que influye en el aporte de esta fuente a las emisiones totales es la extensión de su superficie.

Tomando en cuenta lo anterior, además del “Informe Técnico: Balance nutricional en cultivos de Agrícola

Y Comercial Los Queltehues Ltda. Temporada 2020-2021”, elaborado para el presente proyecto por Irrifer

Ltda., el titular tomó la decisión de distribuir el total del guano compostado en distintos campos de su

propiedad destinados a proyectos agrícolas, con el fin de evitar un exceso de algunos nutrientes como
fósforo y/o potasio que pudiesen afectar acuíferos cercanos, y a la vez disminuir la emisión de olores.

Junto con esta medida, también se decidió aplicar la enmienda en la parte central del predio, con el fin de
que esta actividad quede lo más lejos posible de los receptores y/o potenciales afectados.

Como se mencionó anteriormente, la incorporación de guano compostado en suelos agrícolas presenta el

mayor aporte a la emisión de olores, en el resultado global. Sin embargo, es muy importante mencionar

que, debido a la estimación realizada, el impacto producido por esta actividad se ve reducido a solamente

20 días en el año, lo que representa el 5,48% del total de horas modeladas (480 de 8760). Esto implica que

las posibles molestias por olores no se extenderían a lo largo de todo el año, sino que se concentrarían en

el periodo de aplicación de enmienda, e incluso en esta circunstancia, no se sobrepasan los valores

máximos de emisión utilizados como referencia.

Como una manera de graficar lo anterior, a continuación, se presentan los resultados de modelación

comparados del proyecto completo comparados con la modelación incluyendo solamente la incorporación

de guanos compostados en suelos.

Página **30** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 18.** Comparativa de modelación, proyecto actual versus solo aplicación de enmienda.

Página **31** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

Se observa en las imágenes que gran parte de los resultados son atribuibles a la incorporación de enmienda

orgánica en suelos. También se observa que el valor máximo, en un punto dentro del predio del proyecto,
varía de 60,8 Uo/m [2] *s a 58,42 Uo/m [2] *s.

De esta manera, se demuestra que el potencial impacto por olores asociado al proyecto se limita a 20 días

durante la incorporación de enmienda (septiembre), y que incluso en estas condiciones, el único receptor
alcanzado (Receptor 2) no sobrepasa las 3 Uo/m [2] *s.

Respecto de los predios en que se pretende disponer del guano para su utilización como mejorador de

suelos, estos se encuentran dentro de la VII región, por lo que los traslados de camiones no implicarán

grandes trayectos.

**Tabla 13** . Distancias entre el proyecto y otros fundos.

|N° Campo|Superficie<br>(ha)|Sector|Distancia a Engorda<br>Los Queltehues (km)|Coordenada Norte<br>(m)|Coordenada Este<br>(m)|
|---|---|---|---|---|---|
|~~1 ~~<br>|~~100~~<br>|~~Palmilla~~<br>|~~Mismo predio~~<br>|~~261479~~<br>|~~6029393~~<br>|
|~~2 ~~<br>|~~57~~<br>|~~Los Batros~~<br>|~~14,9~~<br>|~~269674~~<br>|~~6035219~~<br>|
|~~3 ~~<br>|~~100~~<br>|~~El Refugio~~<br>|~~16,3~~<br>|~~270315~~<br>|~~6035864~~<br>|
|~~4 ~~<br>|~~110~~<br>|~~San Juan - Peñasco~~<br>|~~18,0~~<br>|~~272932~~<br>|~~6037705~~<br>|
|~~5 ~~<br>|~~128~~<br>|~~San Ramon de Bodega~~<br>|~~21,0~~<br>|~~250206~~<br>|~~6029761~~<br>|
|~~6 ~~<br>|~~39~~|~~Miraflores~~|~~10,0~~|~~258544~~|~~6023639~~|

Página **32** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**Figura 19** . Ubicación de los distintos campos en que se utilizará el guano compostado como mejorador

de suelos.

Página **33** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

El traslado será realizado en camiones cerrados, para evitar la caída de material y emisión de olores. Estos

camiones serán lavados antes de salir del predio. Además, permanecerán en la cancha de compostaje del

proyecto actual todo el tiempo que sea necesario, y serán trasladados solamente al momento de la

incorporación, de manera que no permanecerán almacenados en ninguno de los distintos campos en que

serán utilizados.

**Figura 20.** Camiones para traslado de guano compostado.

Página **34** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

 - En el área de influencia no se registran actividades de tipo turístico, ni de culto religioso u otras

actividades relacionadas; no existen asentamientos ni comunidades indígenas. Tampoco se observa

existencia de equipamiento como hospitales, colegios, etc., que pudiesen verse afectados por el

proyecto.

 - Según los resultados de la modelación, el mayor impacto por olores provenientes del proyecto se
registra dentro de las dependencias del proyecto, con un valor de 60,8 Uo/m [3], considerando el

Percentil 98 de los valores promedios horarios diarios.

 - Según los resultados entregados en la Tabla 8, los valores de inmisión en los posibles receptores

están bajo el máximo recomendado por la legislación internacional, a excepción del receptor 8
(11,13 Uo/m [3] ); sin embargo, este receptor se encuentra dentro del predio correspondiente al

proyecto.

 - Como se puede apreciar en la Tabla 6, el mayor factor de emisión corresponde a la actividad de
ensilaje o acopio de silo, con un valor de 4,624 Uo/m [2] *s. Sin embargo, el mayor aporte a las

emisiones está dado por el Campo San Luis (aplicación de enmienda), que, a pesar de tener una
tasa de emisión mucho menor (2,014 Uo/m [2] *s), presenta un área de emisión considerablemente

mayor, lo que termina siendo un factor relevante.

 - El área de influencia del proyecto tiene una dimensión de 7 km [2], con una distancia de impacto

máxima de 3 kilómetros aproximadamente, en línea recta desde el punto representativo del

proyecto hacia el Noreste, correspondiente al acceso a la ciudad de Linares desde la carretera

Panamericana.

 - Considerando que las personas son susceptibles de ser afectadas por la emisión de malos olores,

es importante considerar que la zona de emplazamiento del proyecto presenta una baja densidad

poblacional, lo que ayuda a disminuir el número de individuos que pudiesen ser afectados en las

proximidades del proyecto. Pese a lo anterior, debido al alcance observado en los resultados, el

proyecto podría afectar parte de la zona urbana correspondiente a la ciudad de Linares,

específicamente la zona occidental de dicha ciudad, que es el acceso principal a la ciudad desde la

carretera Panamericana; sin embargo, también se debe indicar que esta zona de la ciudad está
catalogada como ZAP y ZAV (Zona de Actividades Productivas y Zona de Áreas Verdes,

respectivamente) según el Plan Regulador Comunal de Linares, por lo que en ningún caso se estaría

afectando zonas residenciales o densamente pobladas.

En conclusión, los resultados permiten afirmar que el presente proyecto no generaría impactos de

consideración en el medio ambiente ni en las personas cercanas al mismo. De todos modos, se recomienda

adoptar las medidas necesarias en el Plan de Gestión de Olores, que permitan mantener esta condición,

logrando un equilibrio entre la actividad productiva y su entorno inmediato.

Página **35** de **36**

Modelación de Dispersión e Impacto por Olores Engorda Los Queltehues

**www.essconsultores.cl**

**La Capitanía 80, Oficina 108, Las Condes**
**Santiago, Chile**

**+562 23034022**

**+569 82234583**

Página **36** de **36**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Coordenadas punto representativo del proyecto (Datum WGS 84).**

| Coordenadas UTM Engorda Los Queltehues. | Col2 |
| --- | --- |
| Coordenada Este (m) | Coordenada Norte (m) |
| 261480 | 6029364 |

**Tabla 3.: ** Información de la estación Linares.**

| Estación | UTM Este (m) | UTM Norte (m) | Altitud (m) |
| --- | --- | --- | --- |
| Linares | 265805 | 6031030 | 160 |

**Tabla 4: ** . Análisis de incertidumbre.**

| Estadístico | Viento | Temperatura |
| --- | --- | --- |
| ~~Sesgo~~<br> | ~~1,39307754~~<br> | ~~3,286493~~<br> |
| ~~Error Medio Cuadrático~~<br> | ~~1,05158088~~<br> | ~~2,720727~~<br> |
| ~~Coeficiente de Correlación~~<br> | ~~0,61361588~~ | ~~0,897536~~ |

**Tabla 5.: ** Configuración del dominio del modelo CALPUFF.**

| Ítem | Valor |
| --- | --- |
| ~~Centro UTM E (m)~~<br> | ~~260899~~<br> |
| ~~Centro UTM N (m)~~<br> | ~~6028963~~<br> |
| ~~Resolución espacial (m)~~<br> | ~~500~~<br> |
| ~~Puntos en X~~<br> | ~~60~~<br> |
| ~~Puntos en Y~~<br> | ~~60~~<br> |
| ~~Topografía~~<br> | ~~SRTM3 (Aproximadamente 90 metros de resolución)~~<br> |
| ~~Uso de suelo~~ | ~~GLCC (USGS30 aproximadamente a 1 Kilómetro e resolución)~~ |

**Tabla 6: ** . Fuentes de olor consideradas para la modelación.**

| Zona o Proceso | Fuente de<br>Olor | Tipo de<br>Fuente | Dimensiones<br>(m) | Área<br>(m2) | Coordenada<br>UTM Este<br>(m) | Coordenada<br>UTM Norte<br>(m) | Horas de<br>Emisión<br>por<br>Jornada<br>Laboral | Actividad/Material |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Almacenamiento**<br>**de Alimentos** | Acopio<br>Chala Maíz | Superficial<br>Pasiva | 19.6 x 4.5 x 2 | 120 | 328706 | 6307686 | 24, todos<br>los días | Acopio de<br>alimento / Silo<br> |
| **Galpones** | Galpón 1 | Superficial<br>Pasiva | 117 x 25.5 x<br>2 | 2984 | 260868 | 6028984 | 24, todos<br>los días | ~~Engorda de~~<br>Animales / Cama<br>Caliente<br> |
| **Galpones** | Galpón 2 | Superficial<br>Pasiva | 103 x 30 x 2 | 3090 | 260900 | 6028998 | 24, todos<br>los días | ~~Engorda de~~<br>Animales / Cama<br>Caliente<br> |
| **Galpones** | Galpón 3 | Superficial<br>Pasiva | 130 x 30 x 2 | 3900 | 260972 | 6028906 | 24, todos<br>los días | ~~Engorda de~~<br>Animales / Cama<br>Caliente |
| **Acopio de Cama**<br>**Caliente** | Patio de<br>Compostaje | Superficial<br>Pasiva | 61 x 27 x 2<br> | 1647 | 260922 | 6028912 | 24, todos<br>los días | Acopio de guano /<br>Guano<br> |
| **Cementerio de**<br>**Animales** | Cementerio | Superficial<br>Pasiva | ~~Campo de~~<br>dimensiones<br>irregulares | 2500 | 260855 | 6028876 | 24, todos<br>los días | ~~Disposición~~<br>(entierro) de<br>animales muertos<br> |
| **Fosa Séptica**<br> | Fosa<br>Séptica | Superficial<br>Pasiva | 1.5 x 1.5 x 2<br> | 2.25 | 260857 | 6028898 | 24, una vez<br>al mes<br> | ~~Acumulación de~~<br>aguas servidas<br>domiciliarias<br> |
| ~~**Incorporación de**~~<br>**Enmienda a**<br>**Suelo Agrícola**<br> | Campo San<br>Luis | Superficial<br>Pasiva | ~~Campo de~~<br>dimensiones<br>irregulares | 200000 | 261101 | 6029218 | ~~20 días x~~<br>año,<br>septiembre | ~~Incorporación de~~<br>guano animal al<br>suelo |

**Tabla 7: ** . Caracterización de olores.**

| Zona o Proceso | Fuente de Olor | Calidad | Olor | Tono<br>Hedónico | Intensidad | Concentración<br>(Uo/Nm3) |
| --- | --- | --- | --- | --- | --- | --- |
| ~~**Almacenamiento de**~~<br>**Alimentos** | ~~Acopio Chala~~<br>Maíz | Vinagre, dulce<br> | Compuesto | ~~- 2~~<br>Desagradable<br> | Medio | 555 |
| **Galpones** | Galpón 1* | ~~Amoniaco,~~<br>guano<br> | Compuesto | ~~-2~~<br>Desagradable<br> | Medio | 201 |
| **Galpones** | Galpón 2* | ~~Amoniaco,~~<br>guano<br> | Compuesto | ~~-2~~<br>Desagradable<br> | Medio | 201 |
| **Galpones** | Galpón 3 | ~~Amoniaco,~~<br>guano | Compuesto | ~~-2~~<br>Desagradable<br> | Medio | 201 |
| **Acopio de Cama**<br>**Caliente**<br> | Patio de<br>Compostaje | Guano | Compuesto | ~~-1~~<br>Levemente<br>Desagradable | Suave | No Aplica** |
| ~~**Cementerio de**~~<br>**Animales** | Cementerio | Tierra mojada | Compuesto | 0 neutro<br> | Muy Suave<br> | 74 |
| **Fosa Séptica**<br> | Fosa Séptica | Agua | Compuesto | ~~0 neutro (Sin~~<br>Olor)<br> | ~~Muy Suave, Sin~~<br>Olor | 101 |
| ~~**Incorporación de**~~<br>**Enmienda a Suelo**<br>**Agrícola** | Campo San Luis | Tierra húmeda,<br>guano | Compuesto | ~~-1~~<br>Levemente<br>Desagradable | Muy Suave | 242 |

**Tabla 10: ** . Valores de concentración (Uo/m [3] ) modelados para cada uno de los receptores discretos**

| Receptor | P98 |
| --- | --- |
| ~~1 ~~<br> | ~~0,52~~<br> |
| ~~2 ~~<br> | ~~1,50~~<br> |
| ~~3 ~~<br> | ~~0,37~~<br> |
| ~~4 ~~<br> | ~~0,12~~<br> |
| ~~5 ~~<br> | ~~0,24~~<br> |
| ~~6 ~~<br> | ~~0,02~~<br> |
| ~~7 ~~<br> | ~~0,05~~<br> |
| ~~8 ~~<br> | ~~11,13~~<br> |
| ~~9 ~~<br> | ~~0,17~~<br> |
| ~~10~~<br> | ~~0,29~~<br> |
| ~~PMI (261149E, 6029214N)~~ | ~~60,80~~ |

**Tabla 11.: ** Concentración y percepción.**

| Concentracion | Percepcion |
| --- | --- |
| 1 Uo/m3 | 50% de la población puede comenzar a percibir un olor |
| 3 Uo/m3 | 50% de la población puede reconocer o comenzar a reconocer un olor<br> |
| 5 Uo/m3 | ~~El olor es calificable y puede comenzar a recibirse quejas (puede ser~~<br>identificado) |
| 10 Uo/m3 | Los olores son reconocibles y se pueden recibir reclamos |

**Tabla 12.: ** Valores de inmisión según actividad, IPPC.**

| Ofensividad<br>Relativa del<br>Olor | Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales) | Tipo de Actividad Relacionada |
| --- | --- | --- |
| ALTA | 1,5 Uo/m3 | Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales |
| MEDIA | 3 Uo/m3 | Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva |
| BAJA<br> | 6 Uo/m3 | Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías |

**Tabla 13: ** . Distancias entre el proyecto y otros fundos.**

| N° Campo | Superficie<br>(ha) | Sector | Distancia a Engorda<br>Los Queltehues (km) | Coordenada Norte<br>(m) | Coordenada Este<br>(m) |
| --- | --- | --- | --- | --- | --- |
| ~~1 ~~<br> | ~~100~~<br> | ~~Palmilla~~<br> | ~~Mismo predio~~<br> | ~~261479~~<br> | ~~6029393~~<br> |
| ~~2 ~~<br> | ~~57~~<br> | ~~Los Batros~~<br> | ~~14,9~~<br> | ~~269674~~<br> | ~~6035219~~<br> |
| ~~3 ~~<br> | ~~100~~<br> | ~~El Refugio~~<br> | ~~16,3~~<br> | ~~270315~~<br> | ~~6035864~~<br> |
| ~~4 ~~<br> | ~~110~~<br> | ~~San Juan - Peñasco~~<br> | ~~18,0~~<br> | ~~272932~~<br> | ~~6037705~~<br> |
| ~~5 ~~<br> | ~~128~~<br> | ~~San Ramon de Bodega~~<br> | ~~21,0~~<br> | ~~250206~~<br> | ~~6029761~~<br> |
| ~~6 ~~<br> | ~~39~~ | ~~Miraflores~~ | ~~10,0~~ | ~~258544~~ | ~~6023639~~ |
