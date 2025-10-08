---
title: Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa
author: Klaus Weber
date: D:20201130172042-03'00'
language: es
type: report
pages: 19
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo numérico Alcaparrosa
-->

# Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo numérico Alcaparrosa

VAIGS-IT-020-05279-IT_3 Rev_0

Lundin

Noviembre 2020

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo numérico,<br>Alcaparrosa|Col3|
|---|---|---|
||**VAIGS-IT-20-05279-IT_3 Rev_0**|**VAIGS-IT-20-05279-IT_3 Rev_0**|

|CONTROL ENTREGA|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Fecha|Versión|Revisor VAI|Revisor Cliente|Firma|
|21-oct-20|**Rev_0**|**Paul Mansfield**||<br> <br>|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
|||||Fecha de entrega: 21-oct-20|
|||||Version actual: Rev_0|
|||||N° de páginas: 19|

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo numérico,<br>Alcaparrosa|Col3|
|---|---|---|
||**VAIGS-IT-20-05279-IT_3 Rev_0**|**VAIGS-IT-20-05279-IT_3 Rev_0**|

## Tabla de Contenidos

### 1 Introducción ............................................................................................................ 5

**1.1** **Generalidades .............................................................................................................................5**

**1.2** **Objetivos y alcances ....................................................................................................................6**

**1.3** **Área de Estudio ...........................................................................................................................6**

### 2 Definición de Casos de simulación ........................................................................... 9

**2.1** **Caso Sensibilidad de Conductividad Hidráulica Vertical (Kz) ..........................................................9**

**2.2** **Caso Sensibilidad de Coeficiente de Almacenamiento (Sy) ............................................................9**

### 3 Implementación de escenarios en el Modelo Numérico ........................................ 10

**3.1** **Tiempo de simulación ............................................................................................................... 10**

**3.2** **Representación de Caserones y Galerías Futuras ........................................................................ 10**

**3.3** **Condiciones de Borde ................................................................................................................ 10**

**3.3.1** **Recargas ................................................................................................................................. 10**

**3.3.2** **Descargas ............................................................................................................................... 11**

### 4 Resultados............................................................................................................. 12

**4.1** **Niveles en el acuífero ................................................................................................................ 12**

**4.2** **Balance Hídrico ......................................................................................................................... 13**

**4.3** **Caudales aflorados .................................................................................................................... 15**

### 5 Conclusiones ......................................................................................................... 17 6 Referencias ........................................................................................................... 18

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo numérico,<br>Alcaparrosa|Col3|
|---|---|---|
||**VAIGS-IT-20-05279-IT_3 Rev_0**|**VAIGS-IT-20-05279-IT_3 Rev_0**|

## Índice de Tablas

Tabla 4.1 Valores medios de los flujos régimen transiente Caso 1
Tabla 4.2 Valores medios de los flujos régimen transiente Caso 2
Tabla 4.3 Caudales Promedio por año para cada simulación

## Índice de Figuras

Figura 1.1 Área de estudio, ubicación de la Mina Alcaparrosa
Figura 1.1 Área de estudio, ubicación de la Mina Alcaparrosa
Figura 1.2 Desarrollo futuro de la Mina Alcaparrosa
Figura 3.1 Condiciones de borde utilizadas en el modelo
Figura 4.1 Niveles Simulados Escenario de Proyecto y Análisis de Sensibilidad
Figura 1.2 Balance Hídrico Análisis de Sensibilidad (Disminución Kz)
Figura 1.3 Balance Hídrico Análisis de Sensibilidad (Disminución Sy)
Figura 1.4 Caudales simulados Escenario de Proyecto, Caso 1 y Caso 2

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo<br>numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

## Resumen ejecutivo

Compañía Contractual Minera Ojos del Salado (CCMO) se encuentra desarrollando la mina subterránea
Alcaparrosa, específicamente los sectores de Viviana Oeste, Viviana Este y Alcaparrosa Sur. La Mina está
ubicada en el valle de río Copiapó, de donde se han extraído recursos de agua subterránea para
agricultores, industria minera y el abastecimiento de agua.

Actualmente CCMO tiene contemplado la presentación de una Declaración de Impacto Ambiental (DIA)
que permita la continuidad operacional de la mina de corto plazo, hasta el año 2025. Como apoyo para la
DIA se ha realizado una actualización del modelo hidrogeológico conceptual de la Mina Alcaparrosa y el
desarrollo del modelo numérico para simular el efecto de la extensión de la vida operacional a 2025 sobre
el flujo de ingreso a la mina y el nivel freático del acuífero de la cuenca del río Copiapó.

En el presente anexo se presentan dos simulaciones correspondientes al análisis de sensibilidad realizado
en las propiedades hidráulicas del acuífero del río Copiapó. La primera consiste en una reducción de la
conductividad hidráulica vertical (Kz) del acuífero en un orden de magnitud, mientras que la segunda se

reduce el coeficiente de almacenamiento de 30% a 15%. Ambos modelos comienzan la simulación en

enero de 2020, tomando las propiedades y soluciones de carga hidráulica obtenidas para diciembre de
2019 en el modelo Escenario de Proyecto, presentando en el informe “020-05279_IT 1 Informe Modelo
Conceptual-Numérico DIA Alcaparrosa”.

Las simulaciones muestran una variación en las tasas de descensos para ambas simulaciones con respecto
al Escenario de Proyecto. El caso 1 (Kz) indica una reducción de la tasa de descenso de los niveles freáticos,
con un nivel final 1.5 m mayor que el caso base al final de la simulación. Por otra parte, en el Caso 2 (Sy)
la tasa de descenso aumenta entre el período de 2020 y 2023, pero obteniendo un nivel final similar que
el caso con proyecto durante el año 2025.

La modificación de los parámetros del acuífero no influye de manera significativa en los caudales de
infiltración hacia la mina, indicando valores similares para todas las simulaciones. Se observa caudales
levemente mayores en el Caso 1 y menores en el Caso 2, con diferencias máximas cercanas a 1 L/s. Este
cambio está relacionado a las variaciones de nivel ocurridas en el acuífero, las que modifican la carga
hidráulica sobre las estructuras que transportan el flujo hacia la mina.

Las estimaciones de caudal de infiltración son poco sensibles a los cambios impuestos en las propiedades
del acuífero del río Copiapó, debido a que las modificaciones en el nivel simulado no son lo
suficientemente grandes para generar desviaciones significativas en los caudales simulados en el plazo de
extensión de la continuidad operacional de este proyecto.

_**www.vaigs.cl**_ **4**

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo<br>numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

## 1 Introducción

### 1.1 Generalidades

Compañía Contractual Minera Ojos del Salado (CCMO) se encuentra desarrollando la mina subterránea
Alcaparrosa en el Valle del Río Copiapó, específicamente los sectores de Viviana Oeste, Viviana Este y
Alcaparrosa Sur.

Las instalaciones de CCMO se encuentran ubicadas en la comuna de Tierra Amarilla entre las latitudes

27°27’ y 27°28’ sur y las longitudes 70°16’ y 70°17’ oeste, provincia de Copiapó, Región de Atacama,
aproximadamente a 800 m al noroeste de la zona urbana de la localidad de Tierra Amarilla y
aproximadamente a 20 kilómetros al interior de la ciudad de Copiapó.

La mina Alcaparrosa ha sido explotada con el método subterráneo de Sub Level Stoping (con pilares)
partiendo en el nivel superior N-390. Las cavidades se encuentran abiertas y sin relleno. Para los caserones
futuros se proyecta una distancia mínima de 80 m entre la mina subterránea y el acuífero del Rio Copiapó
(contacto grava/roca).

Actualmente, la mina opera bajo la Resolución de Calificación Ambiental RCA N°158/2017, en la que se
autoriza una extracción de cobre hasta el año 2022. No obstante, CCMO tiene contemplado la
presentación de una Declaración de Impacto Ambiental (DIA) que permita la continuidad operacional de
corto plazo para la mina hasta el año 2025.

Durante 2018 VAI Groundwater Solutions (VAI) realizó una investigación de terreno y un modelo
hidrogeológico conceptual y, posteriormente, desarrolló un modelo numérico 3D de la mina Alcaparrosa,
con el fin de estimar volúmenes de agua que ingresaran en el futuro e identificar zonas de riesgo donde
el agua afecte las condiciones geotécnicas-geomecánicas de la mina.

En el presente anexo se presenta un análisis de sensibilidad con respecto a los parámetros hidrogeológicos
del acuífero del río Copiapó con respecto al caso con proyecto, cuyos parámetros a modificar se detallan

a continuación:

 - **Caso 1:** Disminución de la conductividad hidráulica vertical (Kz) del acuífero del río Copiapó en 1
orden de magnitud.

 - **Caso 2:** Reducción del coeficiente de almacenamiento (Sy) la porosidad drenable del acuífero del
río Copiapó de en un 50%.

Estas simulaciones tienen por objetivo dar respaldo a la incertidumbre relacionada con los parámetros
hidrogeológicos del acuífero del río Copiapó y cuáles son los posibles efectos en la estimación de los
caudales de infiltración a la mina Alcaparrosa.

_**www.vaigs.cl**_ **5**

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo<br>numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

### 1.2 Objetivos y alcances

El objetivo del estudio es realizar un análisis de sensibilidad de los parámetros hidráulicos del acuífero del
río Copiapó, según el Escenario de Proyecto presentando en el informe 020-05279-IT_1 (octubre de 2020)
y evaluar las posibles consecuencias en la estimación de los caudales de infiltración a la mina Alcaparrosa.

El alcance del trabajo incluye lo siguiente:

 - Simulación con conductividad hidráulica vertical (Kz) reducida del acuífero del río Copiapó en un
orden de magnitud.

 - Simulación con coeficiente de almacenamiento (Sy) reducido del acuífero del río Copiapó de un

30 a un 15%.

### 1.3 Área de Estudio

La mina subterránea de Alcaparrosa se encuentra ubicada en el valle del río Copiapó al costado oeste del
eje del valle en la comunidad de Tierra Amarilla ubicado a 15 Km de distancia hacia el SE de la cuidad de
Copiapó (Figura 1.1). Las obras de la mina subterránea (galerías, caserones) han sido desarrolladas
principalmente por la ladera oeste del valle, y considerando algunos sectores más cercanos al eje del valle
según lo autorizado en la RCA N°158/2017 (Figura 1.2).

_**www.vaigs.cl**_ **6**

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo<br>numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

Fuente: Elaboración propia

_**www.vaigs.cl**_ **7**

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa, modelo<br>numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

Fuente: Elaboración propia

_**www.vaigs.cl**_ **8**

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

## 2 Definición de Casos de simulación

### 2.1 Caso Sensibilidad de Conductividad Hidráulica Vertical (Kz)

Esta simulación supone la disminución de la conductividad hidráulica vertical del acuífero del río Copiapó
en un orden de magnitud, variando desde una situación inicialmente isótropa con un coeficiente de
permeabilidad de 50.37 m/día a una situación anisótropa donde la conductividad hidráulica vertical
corresponde a 5.037 m/día. La variación de esta propiedad se evalúa desde enero de 2020, tomando con
como condiciones iniciales los resultados de la simulación del Escenario de Proyecto de diciembre de 2019
evaluado en régimen transiente.

### 2.2 Caso Sensibilidad de Coeficiente de Almacenamiento (Sy)

El segundo caso de sensibilidad corresponde a la disminución del coeficiente de almacenamiento o
porosidad drenable de 30% a 15%, con el fin de evaluar los posibles impactos que puede tener este
parámetro en los caudales de infiltración a la mina. Como fue mencionado en el caso anterior, el cambio
en el almacenamiento se modela desde enero de 2020 a partir de los resultados de carga hidráulica de
diciembre de 2019 evaluado en régimen transiente.

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

## 3 Implementación de escenarios en el Modelo Numérico

### 3.1 Tiempo de simulación

El periodo considerado para la simulación de los escenarios en régimen transitorio se extiende desde
enero de 2020 hasta diciembre de 2025. Éste se ha discretizado en 72 periodos de estrés ( _stress periods_ ),
cada uno con un mes de duración. Las condiciones iniciales del modelo corresponden a los resultados de
carga hidráulica de diciembre de 2019 del Escenario de Proyecto.

### 3.2 Representación de Caserones y Galerías Futuras

La representación de las galerías y caserones proyectadas de la mina se realizó a través de la incorporación
de condiciones de borde tipo drain, cuya conductancia fue determinada en la etapa de calibración
transitoria. El nivel de cada dren fue determinado como el punto más bajo donde se encuentra la cavidad,
o el fondo de la celda si corresponde a un espacio completamente vacío.

Los nodos donde se utiliza esta condición de borde se activan al inicio de cada representación de la
topografía de la mina, manteniéndose activos hasta el fin de la etapa de operación de la mina. Se debe
tener en cuenta que el modelo no representa el avance progresivo de la mina a nivel mensual, sino que
considera la inclusión de todas las unidades de explotación proyectadas para el periodo inmediatamente

terminado el anterior.

### 3.3 Condiciones de Borde

En la presente sección se indican las condiciones de bordes utilizadas en el modelo para representar el
sistema subterráneo en las inmediaciones de la mina Alcaparrosa. En la Figura 3.1 se muestra la
distribución de las condiciones de borde, descritas en detalles a continuación.

3.3.1 Recargas

3.3.1.1 Río Copiapó

El Río Copiapó fue representado a través del River Package (RIV) de MODFLOW. En el caso particular de
este modelo, el Río Copiapó presenta un comportamiento influente por los niveles observados en los
pozos del área ubicados en el acuífero. Personal de VAI durante las visitas a terreno reconoció depósitos
no consolidados de finos en el lecho del río asociados a los aluviones de 2015, por esta razón en el modelo
se asignó una baja conexión entre el Río Copiapó y el acuífero.

3.3.1.2 Flujo Subterráneo

El principal flujo subterráneo en el área del modelo corresponde al proveniente desde aguas arriba a
través de las gravas del acuífero del Río Copiapó. Este flujo es representado a través de pozos de inyección
en el límite sur del modelo con el paquete de MODFLOW Connected Linear Network (CLN).

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

Fuente: VAI Groundwater Solutions (2020)

Un flujo menor, pero de importancia para la distribución piezométrica en la zona, corresponde al flujo
proveniente desde las divisorias de agua de la subcuenca donde inserta la mina. Este flujo fue
representado con el paquete Recharge (RCH) de MODFLOW, a través de la asignación de celdas de recarga
en los límites este y oeste del modelo.

3.3.2 Descargas

3.3.2.1 Descarga flujo subterráneo

Las salidas del sistema de agua subterráneo del modelo numérico están representadas por condiciones
de borde de tipo drain (DRN), la cual simula la salida de agua del modelo a través de un conducto
permeable. Para representar la descarga de aguas del acuífero en el límite norte del modelo, se utilizaron
drenes en la unidad de grava con alta conductancia, lo que permite una salida sin limitaciones para
mantener la continuidad del flujo desde los pozos de inyección.

El nivel de los drenes fue definido en función de la piezometría esperada en el sector y que pudiera
representar la distribución piezométrica deseada en los pozos de observación.

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

## 4 Resultados

### 4.1 Niveles en el acuífero

En la Figura 4.1 se encuentran graficados los niveles simulados por el modelo desde el año 2018 al año
2025 del pozo 12 para el Escenario de Proyecto y las simulaciones de sensibilidad, de manera
representativa del comportamiento del resto de los pozos en las simulaciones.

La reducción de la conductividad hidráulica vertical del acuífero genera una disminución en la tasa de
descenso observada con respecto al caso con proyecto, mostrándose un menor descenso en el acuífero
dentro de la simulación, con niveles aproximadamente 1.5 m superiores.

Por otra parte, la reducción del almacenamiento genera una mayor velocidad de respuesta a los cambios
en las condiciones ambientales impuestas en el modelo. Durante el inicio de 2020 se muestra un aumento
en la tasa de ascenso con respecto al caso con proyecto, mientras que desde marzo del mismo año la tasa
de descenso aumenta, exhibiendo niveles hasta 3.4 m más bajos. No obstante, estos dos últimos casos
muestran niveles similares al final de la simulación, lo que se debe a su conductividad hidráulica similar.

Fuente: Elaboración Propia

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

### 4.2 Balance Hídrico

En las Figuras 4.2 a 4.5 se muestran los principales componentes del balance hídrico para las simulaciones
de utilizadas en el análisis de sensibilidad de 2020 a 2025. El balance hídrico del Caso Proyecto, en el cual
se basa las simulaciones presentadas en este anexo se encuentra en el informe 020-05279-IT_1 (octubre
de 2020). Se observa que en todos los periodos para ambas simulaciones se observan errores bajos,

cercanos al 0%.

Los peaks observados en salidas y entradas del modelo se deben a los cambios de las condiciones de borde
de entrada y salida para representar los cambios de nivel en el acuífero, los que están relacionados
principalmente a cambios de almacenamiento.

Además, se presentan los valores medios de los componentes del balance hídrico para ambas
simulaciones en el período entre 2020 y 2030 (Tabla 4.1 y Tabla 4.2).

Fuente: Elaboración Propia

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

Fuente: Elaboración Propia

|Tabla 4.1 Valores medios de los flujos régimen transiente Caso 1|Col2|
|---|---|
|**Flujo**|**Valor medio Periodo 2020-2025 (L/s)**|
|Recarga Subterránea Límite Sur|218.80|
|Recarga Lateral|0.0001|
|Entrada desde almacenamiento|93.29|
|Recarga Río|0.004|
|Descarga por mina|29.19|
|Descarga Límite Norte|276.76|
|Salida al almacenamiento|6.14|
|Total Entradas|312.10|
|Total Salidas|312.10|
|Error (%)|0.00|

Fuente: Elaboración Propia

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

|Tabla 4.2 Valores medios de los flujos régimen transiente Caso Base 2|Col2|
|---|---|
|**Flujo**|**Valor medio Periodo 2020-2025 (L/s) **|
|Recarga Subterránea Límite Sur|218.80|
|Recarga Lateral|0.0001|
|Entrada por Almacenamiento|57.00|
|Recarga Río|0.004|
|Descarga por mina|28.04|
|Descarga Límite Norte|242.86|
|Salida por Almacenamiento|4.91|
|Total Entradas|275.81|
|Total Salidas|275.81|
|Error (%)|0 .00|

Fuente: Elaboración Propia

### 4.3 Caudales aflorados

En la Figura 4.4 se encuentra la estimación de los caudales de infiltración para el Escenario de Proyecto y
las simulaciones de sensibilidad. El gráfico indica que no existen diferencias notorias en los caudales
simulados entre los 3 modelos. Esto también se ilustra en la Tabla 4.3, donde se encuentran los promedios
anuales entre 2020 y 2025. En general el caso 1 muestra caudales de infiltración levemente mayores que
el caso base, mientras que el caso 2 estima caudales levemente menores.

Fuente: Elaboración Propia

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

|Tabla 4.3 Caudales promedio por año para cada simulación|Col2|Col3|Col4|
|---|---|---|---|
|**Año**|**Caudal Promedio Caso de**<br>**Proyecto (L/s)**|**Caudal Promedio Caso 1 - Kz**<br>**(L/s)**|**Caudal Promedio Caso 2 - Sy**<br>**(L/s)**|
|2020|26.2|26.4|26.0|
|2021|27.7|28.1|26.8|
|2022|27.0|27.9|25.8|
|2023|29.0|29.9|28.5|
|2024|30.6|31.2|30.3|
|2025|31.2|31.7|31.0|

Fuente: Elaboración Propia

Las mayores diferencias entre cada simulación de sensibilidad y el caso base se observan entre los años
2021 y 2023, las que son más altas en el Caso 2, con un máximo de 1.2 L/s. Estas diferencias no son
significativas dado el contexto de la modelación, y la incertidumbre asociada al desarrollo preciso de las

cavidades durante la extracción.

La diferencia positiva observada en el Caso 1 y negativa Caso 2 está relacionada principalmente al efecto
que tiene los cambios de propiedades hidráulicas en el nivel en el acuífero. Las mayores diferencias en la
estimación de caudal de infiltración ocurren durante los años donde los niveles están más alejados entre
sí, reduciéndose a medida que estos son más similares (Figura 4.1 y Figura 4.4). Esto está relacionado al
efecto que tiene la carga hidráulica sobre las estructuras que conducen el flujo hacia la mina, la que
cambia según los parámetros utilizados en la modelación.

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

## 5 Conclusiones

De los resultados de las simulaciones se concluye lo siguiente:

 - La reducción del coeficiente de permeabilidad vertical del acuífero reduce la tasa de descenso
observada en el caso base, e implica un aumento en los niveles del modelo del orden de 1.5 m
para el final de la modelación. Está diferencia se observa también los caudales de infiltración,
donde los caudales estimados son levemente mayores, pero donde éstas no superan 1 L/s.

 - El Caso 2 (reducción de almacenamiento) muestra una reacción más rápida de los niveles a
cambios ambientales en el régimen de flujo en el acuífero con respecto al caso base. Para el
período simulado se muestra una tasa de descenso mucho más rápida, pero con niveles similares

durante el año final de la modelación. Los caudales de infiltración estimados son levemente

menores que el caso base, con las mayores diferencias en los años 2021 a 2023 (no superando los
1.2 L/s), lo que coincide con las mayores diferencias en el nivel.

 - Las estimaciones de caudal de infiltración son poco sensibles a los cambios impuestos en las
propiedades del acuífero del río Copiapó, debido a que la modificación en el nivel simulado no
son lo suficientemente grandes para generar desviaciones significativas en los caudales

simulados.

_VAI Groundwater Solutions_ 

|Col1|Anexo 2: Análisis de Sensibilidad, modelo numérico Alcaparrosa|Col3|
|---|---|---|
||VAIGS-IT-020-05279-IT_3 Rev_0|VAIGS-IT-020-05279-IT_3 Rev_0|

## 6 Referencias

VAI GROUNDWATER SOLUTIONS. Diciembre de 2018. Informe 017-09202 IT1. “Modelo hidrogeológico
conceptual, mina subterránea, Alcaparrosa.”

VAI GROUNDWATER SOLUTIONS. Octubre de 2020. Informe 020-05279 IT1. “Informe de los resultados

del Modelo Hidrogeológico Conceptual y Modelo Numérico, Mina Alcaparrosa 2020”

_VAI Groundwater Solutions_ 