---
title: Microsoft Word - Informe de Modelación ANASAC.docx
author: Desconocido
date: D:20190724173252Z00'00'
language: es
type: report
pages: 31
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de Dispersión e Impacto por Olores “Planta ANASAC Lampa”
-->

# Modelación de Dispersión e Impacto por Olores “Planta ANASAC Lampa”

## Santiago - Chile Julio 2019

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

## CONTENIDO

**1.** **INTRODUCCIÓN** ............................................................................................................................................ 2

**2.** **MODELACIÓN** **DE VARIABLES METEOROLÓGICAS** ............................................................................. 3

**3.** **CÁLCULO DE INCERTIDUMBRE** ................................................................................................................ 12

**4.** **MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE** .......................................... 17

**5.** **FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS** ............................................... 18

**6.** **RESULTADOS DE LA DISPERSIÓN E IMPACTO POR OLORES** ............................................................ 23

**7.** **CONCLUSIONES** .......................................................................................................................................... 27

Página **1** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

## 1. INTRODUCCIÓN

El presente informe da cuenta de los resultados obtenidos de la modelación de dispersión de olores y los
impactos asociados al proyecto “Modificación y Adecuación de Áreas Productivas, Planta ANASAC

LAMPA”, en cumplimiento a lo solicitado por el Servicio de Evaluación Ambiental por medio del Informe

Consolidado de Solicitud de Aclaraciones, Rectificaciones y/o Ampliaciones a la Declaración de Impacto

Ambiental (ICSARA) asociado al proyecto.

Las instalaciones del proyecto se ubican en Camino El Noviciado km. 23, lote 73 B, Comuna de Lampa,

Provincia de Chacabuco, Región Metropolitana.

**Tabla 1.** Coordenadas punto representativo del proyecto (Datum WGS 84).

|Coordenadas UTM Planta ANASAC Lampa.|Col2|
|---|---|
|Coordenada Este (m)|Coordenada Norte<br>(m)|
|328596|6307668|

ANASAC Chile S.A es una empresa que desde hace 70 años, se dedica a la generación de soluciones

agrícolas, dirigidas a empresas y hogares, en la Protección de Cultivos, en proveer Semillas, Mecanización
Agrícola, Nutrición vegetal, Jardín y Hogar, Sanidad Ambiental, Mascotas, Higiene y Desinfección [1] .

La Planta ANASAC- Lampa, R.M., cuenta con una diversidad de productos agroindustriales formulados o

importados, que luego son envasados para abastecer el mercado. La capacidad de producción de la

planta alcanza un promedio nominal de 10.000.000 kg/L (10.000 toneladas/año) entre productos sólidos
y líquidos [1] . En la elaboración y tratamiento de residuos producidos en la actividad productiva, se podrían

generar malos olores, por lo que se hace necesario una evaluación que permita determinar si el impacto

es realmente significativo para las personas y el medio ambiente.

___________________________________________________

1 DIA “MODIFICACIÓN Y ADECUACIÓN ÁREAS PRODUCTIVAS, PLANTA ANASAC LAMPA”. Futuro Sustentable. 2018.

Página **2** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

## 2. MODELACIÓN DE VARIABLES METEOROLÓGICAS

Para generar la base de datos de variables meteorológicas, se utilizó el modelo WRF versión 3.9.1. Éste es

un modelo meteorológico de alta resolución, desarrollado para la simulación de variables

meteorológicas, mediante la resolución de las ecuaciones físicas que describen los movimientos de la

atmósfera, utilizando aproximaciones basadas en métodos numéricos. Este modelo se encuentra en

constante desarrollo y mejora por medio de una asociación colaborativa, principalmente entre el

National Center for Atmospheric Research (NCAR, USA), National Oceanic and Atmospheric

Administration (NCEP, USA), Forecast Systems Laboratory (FSL, USA), Air Force Weather Agency (AFWA,

USA), el Naval Research Laboratory, University of Oklahoma, y la Federal Aviation Administration (FAA,

USA). WRF es un Software Libre y comunitario, por lo que su desarrollo y mejoramiento se realiza en
distintos sitios alrededor del mundo por voluntarios que deseen contribuir al proyecto [3] .

En el presente informe se utilizó la información meteorológica correspondiente al último año

meteorológico (2018). Esta información se obtuvo a partir del CISL Research Data Archive (NCAR, USA),

utilizándose el conjunto de datos de entrada ds083.2. NCAR (National Center for Atmospherical Reseach)

que ofrece a los científicos de Estados Unidos y del mundo, una gran cantidad de herramientas, desde

modelos comunitarios hasta aviones de investigación, supercomputadores y talleres. Los científicos

internos de NCAR colaboran con sus colegas en el mundo académico, el gobierno y el sector privado para

construir, refinar y ampliar los recursos de la comunidad de NCAR para que sean lo más relevantes y
útiles posible. [4]

Para el área de influencia, la configuración del modelo WRF, comprendió la parametrización de variables

propias de los fenómenos de micro escala que inciden en la dispersión de los contaminantes, esto es:

parametrizaciones de microfísica de nubes, fenómenos radiativos, altura de la capa de mezcla y

fenómenos turbulentos causados por la orografía. En la Tabla 2 se detallan las configuraciones de

importancia con las cuales se ejecutó la modelación.

____________________________________________________

3 The Weather Research & Forecasting Model, NCAR/UCAR, https://www.mmm.ucar.edu/weather-research-and-forecasting
model (Visitado en julio de 2019).

4 National Center for Atmospheric Research, NCAR/UCAR, https://ncar.ucar.edu/what-we-offer (Visitado en julio de 2019).

Página **3** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Tabla 2.** Configuración física del modelo WRF 3.9.1, dominio más pequeño.

|Centro Latitud|-33.356631|
|---|---|
|Centro Longitud <br>|-70.842430 <br>|
|Condiciones de entrada <br>|FNL DS083.2 2017 <br>|
|Proyección cartográfica <br>|Mercator <br>|
|Puntos en X <br>|60 <br>|
|Puntos en Y <br>|60 <br>|
|Topografía <br>|SRTM3 (Aproximadamente 100 metros) <br>|
|Uso de suelo <br>|USGS (Aproximadamente 1 Kilómetro) <br>|
|Resolución horizontal (Km) <br>|0,5 <br>|
|Resolución vertical (niveles)|27 niveles hasta 10 hPa|
|Microfísica|“WRF Single-Moment 8-class scheme”.<br>Esquema microfísico de 8 clases, que<br>incorpora además de líquidos, hielo y nieve.<br>Parametrización ideal para simulaciones a<br>alta resolución.|
|Radiación (Onda larga y Corta)|“RRTMG”. Esquema radiativo simple y<br>eficiente, capaz de simular los fenómenos<br>radiativos de onda larga a través del<br>solapamiento de capas nubosas.|
|Modelo de suelo|“ETA Similarity”. Esquema fenómenos suelo-<br>atmósfera ampliamente utilizado por otros<br>modelos numéricos además de WRF, basado<br>en Monin-Obukhov (esquema requerido por<br>el modelo de dispersión) que incorpora la<br>longitud de rugosidad térmica Zilitinkevich y<br>funciones de similitud estándar desde tablas<br>predefinidas.|
|Interacción suelo atmósfera|“Noah Land Surface Model”. Esquema<br>utilizado por NCEP/NCAR/AFWA que<br>incorpora temperatura y humedad del suelo<br>en cuatro capas.|
|Capa planetaria|“Mellor-Yamada- Janjic”. Ampliamente<br>utilizado operacionalmente por otros<br>modelos además de WRF. Basado en un<br>régimen turbulento unidimensional de<br>energía cinética vertical local.|

Página **4** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

El dominio más pequeño definido, considera una zona de 10x10 kilómetros, con un dominio superior

de 30x30 kilómetros y otro principal de 90x90 kilómetros, los que se consideran lo suficientemente

amplios para incorporar fenómenos de escala sinóptica, propios de la zona como los sistemas

frontales o la incursión de altas frías migratorias, configurado además a una alta resolución de 100

metros en su dominio más pequeño, con la capacidad de incorporar fenómenos de mesoescala como

oscilaciones en la capa altura de la mezcla por efecto radiativo o fenómenos de intercambio

turbulento causados por la orografía. En la Figura 1, Figura 2 y Figura 3, se presentan detalles del

dominio considerado en la modelación.

**Figura 1.** Emplazamiento geográfico del dominio considerado para la modelación de variables

meteorológicas y de dispersión.

Página **5** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 2.** Detalle del dominio considerado para la modelación de variables meteorológicas y de
dispersión, información topográfica utilizada por el modelo (SRTM3 a 90 metros de resolución).

Página **6** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 3.** Grilla de modelación de 60x60, a 500 metros de resolución espacial, definiendo un dominio de

30x30 kilómetros de extensión.

De este modo, se logró tener una base de datos de variables meteorológicas para el área de interés, con

resolución horizontal de 500x500 metros, con una grilla de 60x60 para 27 niveles de altitud llegando al

tope de la atmósfera y resolución temporal de una hora para todo 2018, información requerida como

base por el modelo de dispersión.

A continuación, en la **Figura 4**, **Figura 5**, **Figura 6** y **Figura 7** se muestran los campos de vientos

característicos de la zona para las estaciones del año cálidas durante el período diurno y el período

nocturno, como también los campos de vientos característicos de la zona para las estaciones del año frías

durante el período diurno y nocturno.

Página **7** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 4.** Campos de vientos durante el período diurno en estaciones cálidas. Se observa el efecto brisa

valle-montaña. Los puntos azules corresponden a los receptores definidos.

Página **8** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 5.** Campos de vientos durante el período nocturno en estaciones cálidas. Se observa el sentido

contrario del régimen de vientos respecto al día (efecto brisa montaña-valle). Los puntos azules

corresponden a los receptores definidos.

Página **9** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 6.** Campos de vientos durante el período diurno en estaciones frías. Los puntos azules

corresponden a los receptores definidos.

Página **10** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 7.** Campos de vientos durante el período nocturno en estaciones frías. Los puntos azules

corresponden a los receptores definidos.

Página **11** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

## 3. CÁLCULO DE INCERTIDUMBRE

Para el cálculo de incertidumbre, la estación más cercana con información pública disponible,

corresponde a la estación de monitoreo Pudahuel Santiago, emplazada en las instalaciones del

Aeropuerto Arturo Merino Benítez, estación propiedad de la Dirección Meteorológica de Chile, cuyos
datos públicos se encuentran en el Portal de Servicios Climáticos de la Institución [5], cabe destacar que, al

ser una estación de monitoreo automática, los datos disponibles para descarga son datos crudos y no

cuentan con control de calidad.

**Tabla 3.** Información de la estación Pudahuel Santiago.

|Estación|Latitud (°)|Longitud (°)|Altitud (m)|
|---|---|---|---|
|Pudahuel Santiago|-33.391944|-70.794444|482|

La variable a analizar corresponde a la Magnitud y Dirección del viento, puesto que esta combinación de

variables crucial en el transporte y difusión de contaminantes. Se extrajo desde el dominio de

modelación, el punto de grilla correspondiente a la posición de la estación, de manera de calcular la

incertidumbre de los datos modelados versus los datos observados.

___________________________________________________

5 Portal de Servicios Climáticos. Dirección Meteorológica de Chile.
https://climatologia.meteochile.gob.cl/application/historicos/datosDescarga/330021 (Visitado en julio de 2019).

Página **12** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 8** . Rosa de vientos observada en la estación Pudahuel Santiago.

Página **13** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 9.** Rosa de vientos modelada para el punto de grilla ubicado en la estación Pudahuel Santiago.

Página **14** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 10.** Ciclo diario de la magnitud del viento observada y modelada en la estación Pudahuel Santiago.

**Figura 11.** Ciclo anual de la magnitud del viento observada y modelada en la estación Pudahuel Santiago.

Página **15** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

Según se observa en la Figura 8 y en la Figura 9, se puede ver una subestimación de las frecuencias de la

componente suroeste, no ocurre lo mismo con la segunda componente en importancia, que corresponde

a la del sureste, la que sí está correctamente descrita en la modelación.

En la Figura 10 y Figura 11, se observa una constante subestimación de las magnitudes del viento de

parte del modelo, en horas de finales de la tarde y durante los meses cálidos.

Para propósitos de determinar la incertidumbre del modelo, se toma de base la siguiente información:

 - Magnitud del viento promedio observado: 3,04 m/s

 - Magnitud del viento promedio modelado: 2,01 m/s

De los datos anteriores se desprende que el error porcentual de la velocidad del viento está determinado

por la fórmula:

((2,01 - 3,04) * 100 / 3,04) = -33,88%

Dado que la magnitud del viento modelada subestima los valores observados, su efecto consiste en un

aumento de las unidades de olor, este efecto debe ser considerado en la corrección por incertidumbre.

Corregido = (1 - 0,3388) * Modelado

Corregido = 0,6612 * Modelado

De esta forma los resultados modelados deberían ser multiplicados por 0,6612 de manera de corregir el

sesgo del modelo. Sin embargo, este valor por ser muy bajo, es despreciable y la corrección por

incertidumbre no será aplicada con la finalidad de disminuir las unidades de olor presentadas por el

modelo.

Página **16** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

## 4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE

Para la presente modelación se han seguido los procedimientos establecidos por la “Guía metodológica

de uso de modelos de dispersión en el SEIA”, la cual recomienda el uso de CALPUFF como modelo de

dispersión de contaminantes. Para propósitos particulares de este estudio, se ha utilizado la versión 6.4.

CALPUFF es un modelo lagrangiano de dispersión de contaminantes basado en un sistema de “puffs”, los

cuales varían en su forma y posición en función del tiempo, del espacio, la estabilidad atmosférica y los

vientos, entre otros parámetros. Es un modelo que soporta múltiples tipos de fuentes con diferentes

tipos de tratamiento para cada una de ellas: Fuentes de área, fuentes de volumen, fuentes puntuales y
fuentes de línea [5] .

**Tabla 4.** Configuración del dominio del modelo CALPUFF.

|Ítem|Valor|
|---|---|
|Centro UTM E (m)|328571.8|
|Centro UTM N (m)|6307659.9|
|Resolución espacial (m)|500|
|Puntos en X|60|
|Puntos en Y|60|
|Topografía|SRTM3 (Aproximadamente 90 metros de resolución)|
|Uso de suelo|GLCC (USGS30 aproximadamente a 1 Kilómetro e<br>resolución)|

____________________________________________________

Página **17** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

5 A User’s Guide for the CALPUFF Dispersion Model (Version 5). Earth Tech Inc.2000.

## 5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS

Para la modelación se consideraron 11 fuentes emisoras, descritas a continuación:

**Tabla 5** . Fuentes de olor consideradas para la modelación.

|Zona o Proceso|Fuente de<br>Olor|Tipo de Fuente|Principales<br>factores<br>operacionales que<br>influyen en la<br>emisión de olor|Coordenada<br>geográfica<br>Este (m)|Coordenada<br>geográfica<br>Norte (m)|Horas de<br>Emisión<br>por<br>Jornada<br>Laboral|
|---|---|---|---|---|---|---|
|**PTAS**|Caseta PTAS|Fugitiva|Funcionamiento|328706|6307686|24|
|**PTAS**|Estanque<br>PTAS|Puntual|Funcionamiento y<br>exposición al<br>ambiente|328704|6307673|24|
|**PTAS**|Estanque<br>Agua Tratada|Superficial<br>Pasiva|Exposición al<br>ambiente|328699|6307676|24|
|**Producción**|Filtro de<br>Manga|Puntual|Elaboración de<br>Productos|328667|6307658|9|
|**Producción**|Filtro de<br>Carbón|Fugitiva|Elaboración de<br>Productos|328692|6307663|9|
|**Producción**|Planta de<br>Polvos 1|Puntual|Elaboración de<br>Productos|328658|6307582|9|
|**Producción**|Envasado P1 y<br>P2|Puntual|Envasado de<br>Productos|328659|6307587|9|
|**Producción**|Planta de<br>Polvos 2|Puntual|Elaboración de<br>Productos|328660|6307591|9|
|**Producción**|Nutrición<br>Vegetal|Puntual|Elaboración de<br>Productos|328650|6307734|9|
|**Producción**|Lavado IBC|Fugitiva|Lavado de<br>contenedores y<br>generación de<br>RILES de lavado|328679|6307587|9|
|**Almacenamiento**|Bodega 1000|Fugitiva|Almacenaje y<br>concentración de<br>productos|328656|6307576|12|

Las Instalaciones de la planta operan de lunes a viernes durante 24 horas diarias durante todo el año; sin

embargo, las labores de producción se concentran entre las 09:00 h y 17:00 h. Fuera de ese horario, se

Página **18** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

realizan labores de mantención, aseo, almacenaje, etc. Por esta razón, se presentan distintos tipos de

emisión dependiendo del proceso correspondiente a cada fuente.

**Figura 12** . Ubicación de las fuentes de emisión.

Las fuentes fueron seleccionadas mediante una visita a terreno por parte de panelistas expertos en

monitoreo de olores. Estas fuentes representan los principales puntos de emisión de olor para los

distintos procesos productivos que se llevan a cabo en esta Planta.

Para la presente modelación se utilizaron datos de tasas de emisión obtenidos a partir de una campaña
de medición de olfatometría Dinamica para el presente proyecto, ejecutada por ANAM S.A. por encargo
de ESS CONSULTORES. Las mediciones se realizaron en conformidad a la normativa correspondiente:

- La toma de muestra se realizó en función de la Guía Metodológica 3386:2015 y VDI
4285:2011 [6,7]

- El análisis de las muestras se realizó según NCh 3190:2010 [8]

__________________________________________________

6
Instituto Nacional de Normalización. Norma Chilena 3386:2015 “Muestreo estático para olfatometría”. Chile. 2015.

7 Verein Deutscher Ingenieure. VDI 4285:2011 Determination of diffusive emissions by measurements industrial halls and

livestock farming. Germany. 2011.

Página **19** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

8 Instituto Nacional de Normalización. Norma Chilena 3190:2010 “Calidad del aire - Determinación de la concentración de olor

por olfatometría dinámica”. Chile. 2010.

- La campaña de medición fue llevada a cabo durante los días 25 y 26 de junio de 2019.

Las normas mencionadas anteriormente dan cuenta de la metodología y procedimientos
adecuados para la toma de muestra y la determinación de su concentración.

Para el caso de la fuente denominada Nutrición Vegetal, que no se encontraba operativa al
momento de la medición, se homologó con el valor medido para la fuente Filtro de Mangas,
considerando las similitudes entre ambas unidades en cuanto a elaboración de productos y
materias primas utilizadas para tal acción.

Los valores de emisión utilizados se muestran en la Tabla 6, ordenados desde mayor a menor emisión, a

modo de ranking de emisiones.

**Tabla 6** . Tasas de emisión por unidad.

Página **20** de **30**

|Fuente de Olor|Tasa de Emisión Total<br>(Uo/s)|
|---|---|
|Bodega 1000|1090|
|Filtro de Carbón|223|
|Planta de Polvos 2|117|
|Planta de Polvos 1|93,9|
|Envasado P1 y P2|44,4|
|Filtro de Manga|28,3|
|Nutrición Vegetal|28,3|
|Lavado IBC|8,46|
|Caseta PTAS|1,24|
|Estanque Agua Tratada|0,99|
|Estanque PTAS|0,36|

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

La tasa de emisión total incorpora la concentración medida, el área de emisión y el flujo volumétrico para

cada una de las fuentes.

Respecto a los receptores definidos, se consideraron 7 receptores discretos alrededor del proyecto, tal

como lo muestra la Figura 13.

**Figura 13.** Receptores definidos dentro del dominio de modelación.

La

ubicación en detalle de los receptores definidos, se presenta en la Tabla 7.

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La ubicación en detalle de los receptores definidos, se presenta en la Tabla 7. -->

**Tabla 7: ** . Ubicación de los receptores discretos definidos dentro del dominio de la modelación.**

| Punto | Receptor | Coordenada<br>Este (m) | Coordenada<br>Norte (m) | Altitud<br>(m) | Altura<br>(m) | Distancia aproximada<br>al perímetro de la<br>Planta ANASAC Lampa<br>(km) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | R1 | 328643 | 6308753 | 478 | 2 | 1,5 |
| 2 | R2 | 327253 | 6309968 | 482 | 2 | 1,4 |

<!-- Estadísticas: 2 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Página **21** de **30** Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa -->
<!-- FIN TABLA 7 -->


**Tabla 7** . Ubicación de los receptores discretos definidos dentro del dominio de la modelación.

|Punto|Receptor|Coordenada<br>Este (m)|Coordenada<br>Norte (m)|Altitud<br>(m)|Altura<br>(m)|Distancia aproximada<br>al perímetro de la<br>Planta ANASAC Lampa<br>(km)|
|---|---|---|---|---|---|---|
|1|R1|328643|6308753|478|2|1,5|
|2|R2|327253|6309968|482|2|1,4|

Página **21** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

|3|R3|331186|6309492|479|2|1,9|
|---|---|---|---|---|---|---|
|4|R4|333577|6307462|479|2|0,7|
|5|R5|332568|6305473|476|2|2,6|
|6|R6|328372|6306596|475|2|1,2|
|7|R7|325743|6305170|488|2|2,5|

Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas cercanas al

proyecto, ya que principalmente en estas se concentra la población susceptible de ser afectada por

potenciales emisiones de malos olores. También se consideró la existencia de “población flotante”

asociada a las distintas labores industriales existentes en la zona.

## 6. RESULTADOS DE LA DISPERSIÓN E IMPACTO POR OLORES

A continuación, se presentan los resultados obtenidos para la modelación de olores correspondiente al

proyecto en evaluación.

Las Figura 14. Unidades de olor, P98.

4 y 15 muestran una vista general de todo el dominio considerado, para el percentil 98 y 99,5 de los

promedios horarios para el periodo modelado, respectivamente.

Página **22** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Figura 14.** Unidades de olor, P98.

**Figura 125** . Unidades de olor, P99,5.

Página **23** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

Se puede observar que solamente utilizando el criterio de percentil 99,5 para el promedio de los valores
horarios se supera el valor de 1 Uo/m [3], siendo 1,25 Uo/m [3] el valor de impacto máximo. En el caso del
percentil 98, este valor máximo no supera la unidad (0,92 Uo/m [3] ). Valores por debajo de 1 Unidad de

Olor son considerados prácticamente imperceptibles por el ser humano.

En la siguiente imagen se presenta en forma detallada el área comprendida por la isodora 1 Uo/m [3] para

el percentil 99,5 de los valores horarios promedio. Como se mencionó anteriormente, se utilizó este
criterio para determinar el área de influencia del proyecto [9], debido a los bajos resultados de inmisión

obtenidos para el percentil 98.

____________________________________________________

9 Guía para la predicción y evaluación de impactos por olor en el SEIA, Servicio de Evaluación Ambiental (SEA), 2017.

**Figura 16** . Área de influencia del proyecto para el percentil 99,5.

Página **24** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

Se puede apreciar que el área de influencia queda bastante confinada a las cercanías de la Planta

ANASAC Lampa, alcanzando principalmente terrenos de uso agrícola y parte de sectores industriales

vecinos.

Página **25** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

En la Tabla 8 se presenta un detalle de los máximos valores horarios del día calculados para cada

receptor discreto definido, junto a los valores calculados para el Punto de Máximo Impacto.

**Tabla 8** . Valores de UO calculados para cada uno de los receptores discretos definidos.

|Receptor|P98 (Uo/m^3)|P99,5 (Uo/m^3)|
|---|---|---|
|R1|0,07|0,08|
|R2|0,02|0,02|
|R3|0,00|0,01|
|R4|0,00|0,00|
|R5|0,00|0,00|
|R6|0,05|0,11|
|R7|0,00|0,01|
|PMI (328322E, 6307410N)|0,92|1,25|

Se desprende de los resultados entregados en la tabla anterior que ninguno de los receptores se ven

afectados por emisiones de olor, puesto que los valores de concentración arrojados por la modelación

son en la práctica imperceptibles por el ser humano, y están muy por debajo del valor considerado como

umbral (1 Uo/m^3).

Página **26** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

## 6. CONCLUSIONES

Los resultados permiten cuantificar las molestias causadas por las emisones de olores. La escala de
percepciones y concentración de olores generalmente aceptada a nivel internacional se resumen en la
siguente estructura :

**Tabla 9.** Concentración y percepción.

|Concentracion|Percepcion|
|---|---|
|1 Uo/m3|50% de la población puede comenzar a percibir un olor|
|3 Uo/m3|50% de la población puede reconocer o comenzar a reconocer un olor|
|5 Uo/m3|El olor es calificable y puede comenzar a recibirse quejas (puede ser<br>identificado)|
|10 Uo/m3|Los olores son reconocibles y se pueden recibir reclamos|

Es importante matizar el limite que se debe alcanzar para que exista una queja, ya que estas dependen
tambien de la intensidad de los olores percibidos, de su agresividad, de su apreciación (positiva o
negativa) y de su frecuencia. En consecuencia, la sensibilidad individual hacia los olores tiene una
influencia importante en la presentacion de quejas. Varias jurisdicciones alrededor del mundo han
implementado con éxito programas de gestión de olores, que proponen criterios de percepción de olor
que oscilan entre 1 y 10 u.o./m [3] .

Como referencia, se cita la Guía Técnica Preliminar “Horizontal Guidance for Odour Part 1 - Regulation
and Permitting” [10] de la Integrated Pollution Prevention and Control (IPPC), mecanismo regulatorio
medioambiental de la Unión Europea. En este documento se proponen los siguientes criterios de
inmisión según el tipo de actividad.

____________________________________________________

10 Horizontal Guidance for Odour Part 1 - Regulation and Permitting. Scotish Environment Prevention Agency/Environment

 - and Heritage Service/UK Environmet Agency. 2002. https://olores.mma.gob.cl/wp content/uploads/2019/03/Integrated

Pollution-Prevention-and-Control-part1.pdf

Página **27** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**Tabla 10.** Valores de inmisión según actividad, IPPC.

|Ofensividad<br>Relativa del<br>Olor|Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales)|Tipo de Actividad Relacionada|
|---|---|---|
|ALTA|1,5 Uo/m3|Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales|
|MEDIA|3 Uo/m3|Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva|
|BAJA|6 Uo/m3|Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías|

Esta guía recomienda valores de concentración según el nivel de ofensividad (alta, media o baja) para

cada olor molesto asociado a cada tipo de faena, indicando algunos ejemplos de ellas. Esta guía

considera el percentil 98 de los valores horarios promedio para un año.

Considerando los resultados obtenidos para el presente proyecto, con un criterio más exigente (percentil

99,5), se aprecia que incluso en el caso más restrictivo, de alta ofensividad, los valores de se encuentran

por debajo de lo recomendado en este cuerpo normativo.

En base a la Modelación de olores, se puede concluir que el impacto odorante del proyecto evaluado

“Planta ANASAC Lampa” es marginal, de acuerdo al estándar internacional vigente y aceptado en cuanto

a emanaciones, percepción y molestia por olores.

Página **28** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

§ Según los resultados de la modelación, el mayor impacto por olores provenientes del proyecto se

recibe a 300 metros aproximadamente, al suroeste desde el proyecto, con un valor de 1,25
Uo/m [3], para el percetil 99,5 de los valores horarios promedio en un año.

§ El área de influencia del proyecto tiene una dimensión de 11, 1 hectáreas, y se encuentra

inmediatamente cercana a la planta, impactando principalmente en zonas de uso agrícola e

industrial.

§ Según los resultados entregados en la Tabla 8, los valores de inmisión en los posibles receptores

son muy bajos, cercanos a cero en la mayoría de los casos. El valor más relevante alcanzó el
máximo de 0,11 Uo/m [3] para el receptor 6, situado a 1,2 km aproximadamente, al sur-suroeste del
proyecto. Este valor está muy por debajo de 1 Uo/m [3] y es prácticamente imperceptible por el

sistema olfatorio humano.

§ Considerando que las personas son susceptibles de ser afectadas por la emisión de malos olores,

es importante considerar que la zona de emplazamiento del proyecto presenta una baja densidad

poblacional, lo que ayuda a disminuir el número de individuos que pudiesen ser afectados.

§ Los resultados se encuentran por debajo de lo recomendado por la legislación internacional

aceptada para la evaluación de olores.

En conclusión, los resultados permiten afirmar que el presente proyecto no genera impactos

significativos para el medio ambiente ni las personas en relación a emisión de olores molestos, ya que sus

niveles de emisión se encuentran por debajo de lo detectable por un panel experto y muy por debajo en

comparación con normativa internacional vigente relacionada.

Página **29** de **30**

Modelación de Dispersión e Impacto por Olores Planta ANASAC Lampa

**www.essconsultores.cl**

**La Capitanía 80, Oficina 108, Las Condes**
**Santiago, Chile**

**+562 23034022**

**+569 82234583**

Página **30** de **30**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Coordenadas punto representativo del proyecto (Datum WGS 84).**

| Coordenadas UTM Planta ANASAC Lampa. | Col2 |
| --- | --- |
| Coordenada Este (m) | Coordenada Norte<br>(m) |
| 328596 | 6307668 |

**Tabla 2.: ** Configuración física del modelo WRF 3.9.1, dominio más pequeño.**

| Centro Latitud | -33.356631 |
| --- | --- |
| Centro Longitud <br> | -70.842430 <br> |
| Condiciones de entrada <br> | FNL DS083.2 2017 <br> |
| Proyección cartográfica <br> | Mercator <br> |
| Puntos en X <br> | 60 <br> |
| Puntos en Y <br> | 60 <br> |
| Topografía <br> | SRTM3 (Aproximadamente 100 metros) <br> |
| Uso de suelo <br> | USGS (Aproximadamente 1 Kilómetro) <br> |
| Resolución horizontal (Km) <br> | 0,5 <br> |
| Resolución vertical (niveles) | 27 niveles hasta 10 hPa |
| Microfísica | “WRF Single-Moment 8-class scheme”.<br>Esquema microfísico de 8 clases, que<br>incorpora además de líquidos, hielo y nieve.<br>Parametrización ideal para simulaciones a<br>alta resolución. |
| Radiación (Onda larga y Corta) | “RRTMG”. Esquema radiativo simple y<br>eficiente, capaz de simular los fenómenos<br>radiativos de onda larga a través del<br>solapamiento de capas nubosas. |
| Modelo de suelo | “ETA Similarity”. Esquema fenómenos suelo-<br>atmósfera ampliamente utilizado por otros<br>modelos numéricos además de WRF, basado<br>en Monin-Obukhov (esquema requerido por<br>el modelo de dispersión) que incorpora la<br>longitud de rugosidad térmica Zilitinkevich y<br>funciones de similitud estándar desde tablas<br>predefinidas. |
| Interacción suelo atmósfera | “Noah Land Surface Model”. Esquema<br>utilizado por NCEP/NCAR/AFWA que<br>incorpora temperatura y humedad del suelo<br>en cuatro capas. |
| Capa planetaria | “Mellor-Yamada- Janjic”. Ampliamente<br>utilizado operacionalmente por otros<br>modelos además de WRF. Basado en un<br>régimen turbulento unidimensional de<br>energía cinética vertical local. |

**Tabla 3.: ** Información de la estación Pudahuel Santiago.**

| Estación | Latitud (°) | Longitud (°) | Altitud (m) |
| --- | --- | --- | --- |
| Pudahuel Santiago | -33.391944 | -70.794444 | 482 |

**Tabla 4.: ** Configuración del dominio del modelo CALPUFF.**

| Ítem | Valor |
| --- | --- |
| Centro UTM E (m) | 328571.8 |
| Centro UTM N (m) | 6307659.9 |
| Resolución espacial (m) | 500 |
| Puntos en X | 60 |
| Puntos en Y | 60 |
| Topografía | SRTM3 (Aproximadamente 90 metros de resolución) |
| Uso de suelo | GLCC (USGS30 aproximadamente a 1 Kilómetro e<br>resolución) |

**Tabla 5: ** . Fuentes de olor consideradas para la modelación.**

| Zona o Proceso | Fuente de<br>Olor | Tipo de Fuente | Principales<br>factores<br>operacionales que<br>influyen en la<br>emisión de olor | Coordenada<br>geográfica<br>Este (m) | Coordenada<br>geográfica<br>Norte (m) | Horas de<br>Emisión<br>por<br>Jornada<br>Laboral |
| --- | --- | --- | --- | --- | --- | --- |
| **PTAS** | Caseta PTAS | Fugitiva | Funcionamiento | 328706 | 6307686 | 24 |
| **PTAS** | Estanque<br>PTAS | Puntual | Funcionamiento y<br>exposición al<br>ambiente | 328704 | 6307673 | 24 |
| **PTAS** | Estanque<br>Agua Tratada | Superficial<br>Pasiva | Exposición al<br>ambiente | 328699 | 6307676 | 24 |
| **Producción** | Filtro de<br>Manga | Puntual | Elaboración de<br>Productos | 328667 | 6307658 | 9 |
| **Producción** | Filtro de<br>Carbón | Fugitiva | Elaboración de<br>Productos | 328692 | 6307663 | 9 |
| **Producción** | Planta de<br>Polvos 1 | Puntual | Elaboración de<br>Productos | 328658 | 6307582 | 9 |
| **Producción** | Envasado P1 y<br>P2 | Puntual | Envasado de<br>Productos | 328659 | 6307587 | 9 |
| **Producción** | Planta de<br>Polvos 2 | Puntual | Elaboración de<br>Productos | 328660 | 6307591 | 9 |
| **Producción** | Nutrición<br>Vegetal | Puntual | Elaboración de<br>Productos | 328650 | 6307734 | 9 |
| **Producción** | Lavado IBC | Fugitiva | Lavado de<br>contenedores y<br>generación de<br>RILES de lavado | 328679 | 6307587 | 9 |
| **Almacenamiento** | Bodega 1000 | Fugitiva | Almacenaje y<br>concentración de<br>productos | 328656 | 6307576 | 12 |

**Tabla 6: ** . Tasas de emisión por unidad.**

| Fuente de Olor | Tasa de Emisión Total<br>(Uo/s) |
| --- | --- |
| Bodega 1000 | 1090 |
| Filtro de Carbón | 223 |
| Planta de Polvos 2 | 117 |
| Planta de Polvos 1 | 93,9 |
| Envasado P1 y P2 | 44,4 |
| Filtro de Manga | 28,3 |
| Nutrición Vegetal | 28,3 |
| Lavado IBC | 8,46 |
| Caseta PTAS | 1,24 |
| Estanque Agua Tratada | 0,99 |
| Estanque PTAS | 0,36 |

**Tabla 8: ** . Valores de UO calculados para cada uno de los receptores discretos definidos.**

| Receptor | P98 (Uo/m^3) | P99,5 (Uo/m^3) |
| --- | --- | --- |
| R1 | 0,07 | 0,08 |
| R2 | 0,02 | 0,02 |
| R3 | 0,00 | 0,01 |
| R4 | 0,00 | 0,00 |
| R5 | 0,00 | 0,00 |
| R6 | 0,05 | 0,11 |
| R7 | 0,00 | 0,01 |
| PMI (328322E, 6307410N) | 0,92 | 1,25 |

**Tabla 9.: ** Concentración y percepción.**

| Concentracion | Percepcion |
| --- | --- |
| 1 Uo/m3 | 50% de la población puede comenzar a percibir un olor |
| 3 Uo/m3 | 50% de la población puede reconocer o comenzar a reconocer un olor |
| 5 Uo/m3 | El olor es calificable y puede comenzar a recibirse quejas (puede ser<br>identificado) |
| 10 Uo/m3 | Los olores son reconocibles y se pueden recibir reclamos |

**Tabla 10.: ** Valores de inmisión según actividad, IPPC.**

| Ofensividad<br>Relativa del<br>Olor | Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales) | Tipo de Actividad Relacionada |
| --- | --- | --- |
| ALTA | 1,5 Uo/m3 | Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales |
| MEDIA | 3 Uo/m3 | Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva |
| BAJA | 6 Uo/m3 | Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías |
