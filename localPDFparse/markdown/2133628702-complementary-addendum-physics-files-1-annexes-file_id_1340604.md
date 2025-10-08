---
title: Análisis Demográfico Área de Influencia Medio Humano, DIA Proyecto Los Toros
author: Héctor Vera Bórquez
date: D:20180516164141-04'00'
language: es
type: manual
pages: 26
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Análisis Demográfico Área de Influencia Medio Humano, DIA Proyecto Los Toros
-->

# Análisis Demográfico Área de Influencia Medio Humano, DIA Proyecto Los Toros

**Preparada para:**

|Col1|Col2|Marzo, 2018|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|~~D ~~<br>|<br>|~~Revisión Cliente~~<br>|<br>|<br>|<br>|<br>|
|~~C ~~<br>|<br>|~~Revisión Cliente~~<br>|<br>|<br>|<br>|<br>|
|~~B ~~<br>|<br>|~~Revisión Cliente~~<br>|<br>|<br>|<br>|<br>|
|~~A ~~||~~Coordinación Interna~~|~~GA~~|~~PLS~~|~~POB~~||
|**REV**||**EMITIDO PARA**|**POR**|**REV.**|**APR.**||
||||**EMPRESA CONSULTORA**<br>**GISOC**|**EMPRESA CONSULTORA**<br>**GISOC**|**EMPRESA CONSULTORA**<br>**GISOC**||

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

**TABLA DE CONTENIDOS**

1 Consideraciones técnicas .......................................................................................................................... 3

1.1 Preparación de los datos: .................................................................................................................. 3

1.2 Diferencias en la división del territorio ............................................................................................... 5

2 Análisis de los datos................................................................................................................................... 7

2.1 Censo 1992 ....................................................................................................................................... 7

2.1.1 Resultados por zona Área de Influencia ....................................................................................... 8

2.2 Censo 2002 ..................................................................................................................................... 16

2.2.1 Resultados por Zona Área de Influencia ..................................................................................... 17

2.3 Proyección de escenario actual ....................................................................................................... 24

**TABLAS**

Tabla 1. Conteo de personas y viviendas, 1992. ................................................................................................ 7
Tabla 2. Conteo de personas y viviendas, 2002. .............................................................................................. 16

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

**1** **CONSIDERACIONES TÉCNICAS**

**1.1** **PREPARACIÓN DE LOS DATOS:**
Para la realización del análisis se utilizaron las bases de datos de los censos de 1992 y 2002 en formato
Redatam. Además de las cobertura en formato shape de ambos censos a nivel de manzanas censales.
Una primera situación técnica a enfrentar fue la inexistencia del campo “manzent” en la cobertura del censo
de 1992. En primera instancia se procedió a llamar al Instituto Nacional de Estadísticas para realizar consultas
respecto de la existencia del archivo con la tabla de atributos completa (cuestión que sí existe en la cobertura
del Censo de 2002). Tras una serie de cinco llamados en espacio de poco más de una semana, se informó
que la persona encargada del tema se encontraba de vacaciones, pero al llamar sucesivamente los días 05 y
06 de marzo se informó que ella aun no volvía. Finalmente se tomó contacto con ésta pero no se obtuvo
resultados positivos con la premura requerida.

Se apreciaron diversos inconvenientes respecto a la calidad de la cobertura correspondiente al censo de
1992:

 - Ausencia del código que identifica las manzanas censales.

 - Errores en la visualización de algunos códigos contenidos en la tabla de atributos del archivo
“manz.shp”. La revisión de la tabla de atributos en el software gvSIG mostró una anomalía en la
visualización de la columna COD92 que en Arcgis se visualizaba diferente:

_Ilustración 1. Visualización en ArcGis_

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

_Ilustración 2 Visualización en gvSIG_

Esto dio pie para realizar una revisión del archivo .dbf asociado al archivo “manz.shp”. A raíz de esto se
agregaron columnas que contenían los códigos de comuna, distrito y zona censal. Los que finalmente se
fusionaron para dar con el “manzent” de cada manzana.

El resultado se obtuvo mediante la identificación del distrito, zona y manzana en los mapas en pdf de 1992.
Por medio de este procedimiento, se introdujo manualmente en el archivo shape, el código que se denomina
“manzent”, mediante el cual se integran todos los niveles de división del territorio en un sólo código que
identifica la manzana en la que se efectuó la recolección del dato.

Finalmente se depuró la base de datos y se obtuvo la visualización de este dato de manera concordante con
el “manzent” que arroja el análisis con Redatam de la base de datos del censo de 1992.

_Ilustración 3. Tabla de atributos definitiva del Censo de 1992_

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

**1.2** **DIFERENCIAS EN LA DIVISIÓN DEL TERRITORIO**

Un segundo aspecto a considerar previo a la realización de los análisis es la diferencia que se aprecia en la
subdivisión del territorio entre ambos censos, lo cual se comprende por el proceso de crecimiento urbano
desarrollado en la comuna en el periodo intercensal.

A continuación se muestran las diferencias en el polígono que corresponde a las zonas 5 y 7 del análisis.

_Ilustración 4. Zonas 5 y 7 (1992)_

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

_Ilustración 5. Zonas 5 y 7 (2002)_

En el caso de 1992 se decidió dejar por completo en la zona 5 al polígono ubicado entre las calles Portezuelo
de Colina por el norte, por el poniente antes calle Nueva posterior Reñaca en 2002, por el oriente, Nonato
Coo y por el sur Psje 12/Psje Parque Cousiño.
Un segundo elemento a considerar es que la división y codificación del territorio hecha en el censo de 1992 y
el de 2002 es diferente para la misma comuna. Por un lado, el código de la comuna en 1992 fue 133645,
mientras que en el censo de 2002 la comuna se codificó como 13201.

Por otro lado para el Censo de 1992 la zona analizada corresponde a un fragmento del Distrito Censal No2,
de este una parte corresponde a la Zona Censal 1 completa y el resto a una parte de la Zona Censal 4.

En el caso del censo de 2002 el polígono a analizar considera manzanas de las zonas censales 1,2 y 3 del
distrito censal 11 (Zona Censal 4 del Distrito 2 en censo de 1992), y las zonas censales 1 y 4 del distrito
censal 12 (Zona 1 del Distrito Censal 2 en censo de 1992).

Este aspecto dificulta la comparación al nivel de manzana entre censos, dado que estas no poseen la misma
codificación. La estandarización del dato implica un trabajo que sobrepasa los plazos definidos para el
presente análisis. De todos modos se incluyen los datos a nivel de manzana censal por cada uno de los

censos.

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

**2** **ANÁLISIS DE LOS DATOS**

**2.1** **CENSO 1992**
En 1992 la comuna de Puente Alto contaba con 64.331 viviendas y 254.673 habitantes. Respecto del censo
de 1982 el crecimiento intercensal corresponde a un aumento del 130,7% de su población, de acuerdo al sitio
web del municipio, esto se explica por dos razones la primera: “políticas gubernamentales llevadas a cabo
principalmente en el periodo 1980 - 1987, y que tienen relación con las políticas de erradicaciones de
campamentos y poblaciones marginales de la época” [ 1] . Y la segunda causa de este crecimiento se debería a
“La Segunda, y muy asociada a la anterior premisa, se refiere a políticas de planificación gubernamental que
están focalizando a Puente Alto como receptor de viviendas sociales, y por otro lado a un fenómeno propio
del mercado inmobiliario que trata de responder a los gustos y preferencias de los demandantes.” [2]
Respecto del polígono conformado por las 9 zonas identificadas en el estudio este contaba con 5.668
viviendas (8,8% del total de viviendas de la comuna) y 20.497 habitantes, los cuales corresponde el 8% de la
población de Puente Alto.

En cuanto a cada zona analizada se muestra la siguiente tabla resumen con la información respecto al
número de personas y viviendas que habitaban en cada una de estos.

_Tabla 1. Conteo de personas y viviendas, 1992._

|CENSO 1992|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|ZONA|~~CONTEO~~<br>VIVIENDAS|% DEL SECTOR|CONTEO PERSONAS|% PERS DEL SECTOR|
|Z1|476|8,4%|1841|9,0%|
|Z2|549|9,7%|2168|10,6%|
|Z3|536|9,5%|2102|10,3%|
|Z4|765|13,5%|2969|14,5%|
|Z5|600|10,6%|1590|7,8%|
|Z6|643|11,3%|1984|9,7%|
|Z7|485|8,6%|1258|6,1%|
|Z8|353|6,2%|1361|6,6%|
|Z9|1261<br>|22,2%<br>|5224<br>|25,5%<br>|

Fuente: Elaboración propia en base a XVI Censo Nacional de Población y V de Vivienda

Como se aprecia en la tabla precedente la Zona 9 es la que concentra la mayor cantidad de viviendas y
personas del sector, con un 22,2% de las viviendas y un 25,5% del total de los habitantes de esta zona de la

comuna.

1 http://www.mpuentealto.cl/localizate/?page_id=5811. Visitada el 05 de marzo de 2018.
2 Idem

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

**2.1.1** **Resultados por zona Área de Influencia**

 - Zona 1

|MANZENT|CONTEO<br>VIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021001001|28|122|
|133645021001003|36|152|
|133645021001004|36|135|
|133645021001005|32|133|
|133645021001006|32|131|
|133645021001007|24|107|
|133645021001008|24|95|
|133645021001009|20|60|
|133645021001010|27|88|
|133645021001011|61|211|
|133645021001012|12|37|
|133645021001013|12|37|
|133645021001014|12|47|
|133645021001015|12|51|
|133645021001016|8|29|
|133645021001017|12|50|
|133645021001018|12|32|
|133645021001019|12|54|
|133645021001020|12|52|
|133645021001021|12|49|
|133645021001024|12|51|
|133645021001106|28|118|
|TOTAL|476|1841|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

- ZONA 2

- ZONA 3

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021001022|20|75|
|133645021001024|12|51|
|133645021001025|50|207|
|133645021001026|20|73|
|133645021001027|28|121|
|133645021001028|28|118|
|133645021001029|28|115|
|133645021001030|28|102|
|133645021001031|20|78|
|133645021001032|20|86|
|133645021001033|20|78|
|133645021001034|48|181|
|133645021001035|48|193|
|133645021001036|44|148|
|133645021001037|43|161|
|133645021001038|44|176|
|133645021001107|24|91|
|133645021001108|24|114|
|TOTAL|549|2168|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021001055|20|72|
|133645021001056|16|54|
|133645021001057|20|81|
|133645021001059|15|62|
|133645021001060|16|67|
|133645021001061|20|83|
|133645021001063|20|94|
|133645021001064|12|51|
|133645021001065|12|44|
|133645021001066|22|91|
|133645021001068|24|85|
|133645021001069|12|57|
|133645021001070|11|34|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

- ZONA 4

|133645021001072|44|166|
|---|---|---|
|133645021001073|12|50|
|133645021001074|12|48|
|133645021001075|12|48|
|133645021001076|20|81|
|133645021001077|20|68|
|133645021001078|20|73|
|133645021001079|64|247|
|133645021001080|24|99|
|133645021001081|16|67|
|133645021001082|24|91|
|133645021001083|24|93|
|133645021001084|24|96|
|TOTAL|536|2102|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021001039|28|117|
|133645021001040|14|49|
|133645021001041|24|99|
|133645021001042|16|67|
|133645021001043|28|114|
|133645021001045|16|74|
|133645021001046|16|70|
|133645021001047|16|61|
|133645021001048|28|113|
|133645021001049|16|58|
|133645021001051|20|83|
|133645021001052|16|71|
|133645021001053|12|40|
|133645021001054|4|14|
|133645021001085|49|186|
|133645021001086|16|47|
|133645021001087|16|65|
|133645021001088|16|62|
|133645021001089|16|61|
|133645021001090|16|61|
|133645021001091|16|56|
|133645021001092|28|104|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

- ZONA 5

|133645021001093|20|59|
|---|---|---|
|133645021001094|20|73|
|133645021001095|16|58|
|133645021001096|16|65|
|133645021001097|16|60|
|133645021001097|16|60|
|133645021001098|20|74|
|133645021001099|12|48|
|133645021001100|20|67|
|133645021001101|19|68|
|133645021001102|11|52|
|133645021001103|136|550|
|133645021001104|16|63|
|TOTAL|765|2969|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021004228|65|150|
|133645021004229|26|92|
|133645021004230|24|63|
|133645021004231|19|71|
|133645021004232|24|62|
|133645021004233|24|60|
|133645021004234|18|49|
|133645021004235|24|67|
|133645021004236|22|61|
|133645021004237|18|43|
|133645021004238|46|61|
|133645021004239|37|131|
|133645021004240|48|178|
|133645021004241|28|98|
|133645021004242|22|83|
|133645021004243|26|99|
|133645021004244|26|78|
|133645021004245|20|64|
|133645021004246|83|80|
|TOTAL|600|1590|

- ZONA 6

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021004267|10|30|
|133645021004268|11|26|
|133645021004269|12|36|
|133645021004270|14|31|
|133645021004271|20|67|
|133645021004272|20|57|
|133645021004273|22|70|
|133645021004274|24|78|
|133645021004275|24|100|
|133645021004276|24|83|
|133645021004277|24|81|
|133645021004279|6|22|
|133645021004280|23|92|
|133645021004281|36|130|
|133645021004282|36|63|
|133645021004283|33|0|
|133645021004284|30|33|
|133645021004285|16|41|
|133645021004286|117|430|
|133645021004288|122|442|
|133645021004289|19|72|
|TOTAL|643|1984|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

- ZONA 7

- ZONA 8

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021004249|8|0|
|133645021004250|8|0|
|133645021004251|24|40|
|133645021004252|24|38|
|133645021004253|22|37|
|133645021004254|24|33|
|133645021004255|38|141|
|133645021004256|38|124|
|133645021004257|40|128|
|133645021004258|70|269|
|133645021004259|18|57|
|133645021004260|43|158|
|133645021004261|16|39|
|133645021004262|16|41|
|133645021004263|20|47|
|133645021004264|20|26|
|133645021004265|20|0|
|133645021004266|36|80|
|TOTAL|485|1258|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021004002|40|162|
|133645021004003|20|85|
|133645021004004|20|74|
|133645021004005|20|84|
|133645021004006|20|81|
|133645021004007|20|86|
|133645021004009|65|250|
|133645021004010|36|135|
|133645021004011|35|148|
|133645021004012|40|138|
|133645021004013|37|118|
|TOTAL|353|1361|

- ZONA 9

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|133645021004014|94|427|
|133645021004015|16|62|
|133645021004016|18|68|
|133645021004017|19|66|
|133645021004018|18|71|
|133645021004019|16|70|
|133645021004020|20|118|
|133645021004021|27|104|
|133645021004022|23|127|
|133645021004023|19|82|
|133645021004024|17|93|
|133645021004026|44|186|
|133645021004027|42|158|
|133645021004028|43|184|
|133645021004029|44|193|
|133645021004030|41|168|
|133645021004031|39|165|
|133645021004032|44|202|
|133645021004033|39|159|
|133645021004034|39|170|
|133645021004035|43|179|
|133645021004036|123|530|
|133645021004037|199|808|
|133645021004038|16|61|
|133645021004039|4|13|
|133645021004040|14|39|
|133645021004041|22|69|
|133645021004042|18|59|
|133645021004043|23|94|
|133645021004044|23|87|
|133645021004045|23|89|
|133645021004046|24|90|
|133645021004047|18|58|
|133645021004048|24|80|
|133645021004049|25|95|
|TOTAL|1261|5224|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

_Ilustración 6. Zonas analizadas Puente Alto 1992_

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

**2.2** **CENSO 2002**

Tras este censo, la comuna contaba con un total de 130.819 viviendas, lo cual constituye un aumento del
112,4%. Mientras que su población fue de 491.915 personas. Lo cual corresponde a una variación intercensal
del 93,5%.

En cuanto a la zona analizada esta muestra un aumento del 9,1% de viviendas pasando de 5.668 a 6.183.
Mientras que la cantidad de habitantes de este sector aumentó en un 15,1%, pasando de 20.497 a 23.676.

El sector muestra un aumento de la población mucho menor al de la comuna en general, esto debido
principalmente a que se trata de un sector residencial consolidado desde mediados de la década de 1980 [3] .
Ahora bien al analizar zona por zona, tendencia de cada una de estas es dispar, existiendo zonas que incluso
muestran leves disminuciones de, y otras que tienen un importante crecimiento.

_Tabla 2. Conteo de personas y viviendas, 2002._

|CENSO 2002|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|ZONA|~~CONTEO~~<br>VIVIENDAS|% VIV|~~Variación~~<br>Intercensal|~~CONTEO~~<br>PERSONAS|% PERS|Variación Intercensal|
|Z1|499|8,1%|4,8%|1872|7,9%|1,68%|
|Z2|549|8,9%|0,0%|2026|8,6%|-6,55%|
|Z3|526|8,5%|-1,9%|2069|8,7%|-1,57%|
|Z4|746|12,1%|-2,5%|2870|12,1%|-3,33%|
|Z5|876|14,2%|46,0%|3342|14,1%|110,19%|
|Z6|684|11,1%|6,4%|2455|10,4%|23,74%|
|Z7|699|11,3%|44,1%|2589|10,9%|105,80%|
|Z8|345|5,6%|-2,3%|1415|6,0%|3,97%|
|Z9|1259<br>|20,4%<br>|-0,2%<br>|5038<br>|21,3%<br>|-3,56%<br>|

Fuente: Elaboración propia en base a resultados de XVII Censo Nacional de Población y VI de Vivienda

Llama la atención el aumento en el número de viviendas y personas experimentado en las zonas 5 y 7, las
cuales muestran un incremento considerable. Es importante agregar que en la división del territorio que se
aprecia en el censo de 1992 hay un polígono que no cuenta con viviendas ni habitantes, mientras que en el
2002 ese mismo polígono aparece completamente urbanizado y se reparte entre las zonas 5 y 7.

Sin embargo la zona 9 sigue siendo la mayormente poblada de todo este polígono pese a que muestra un
descenso del 3,56% en su población. Más sigue representando a poco más de 1/5 de la población de esta
zona de la comuna de Puente Alto.

Dentro de las zonas que perdieron población en el periodo intercensal se cuentan la 2, 3, 4 y la 9. De estas, la
zona 2 es la que disminuyó en mayor porcentaje su población.

A continuación se presentan las tablas con los resultados por manzana de cada zona definida para este
análisis.

3 Mapa de Crecimiento histórico de Puente Alto, disponible en http://www.mpuentealto.cl/localizate/?page_id=5811

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

**2.2.1** **Resultados por Zona Área de Influencia**

 - ZONA 1

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201121001001|26|98|
|13201121001002|32|135|
|13201121001003|32|125|
|13201121001004|35|125|
|13201121001005|37|137|
|13201121001006|22|78|
|13201121001007|20|71|
|13201121001008|23|96|
|13201121001009|24|96|
|13201121001010|28|118|
|13201121001011|12|33|
|13201121001012|12|46|
|13201121001013|12|36|
|13201121001014|12|43|
|13201121001015|12|47|
|13201121001016|8|31|
|13201121001017|12|41|
|13201121001018|11|26|
|13201121001019|12|45|
|13201121001020|10|36|
|13201121001021|59|227|
|13201121001035|48|182|
|TOTAL|499|1872|

- ZONA 2

- ZONA 3

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201121004001|26|109|
|13201121004002|20|64|
|13201121004004|12|44|
|13201121004005|20|76|
|13201121004006|28|115|
|13201121004007|28|101|
|13201121004008|28|103|
|13201121004009|28|114|
|13201121004010|20|88|
|13201121004011|24|91|
|13201121004012|19|57|
|13201121004013|20|70|
|13201121004014|47|177|
|13201121004015|48|169|
|13201121004016|44|140|
|13201121004017|43|150|
|13201121004018|44|169|
|13201121004032|50|189|
|TOTAL|549|2026|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201121001022|18|69|
|13201121001023|16|57|
|13201121001025|19|84|
|13201121001026|15|56|
|13201121001027|16|68|
|13201121001028|20|64|
|13201121001030|20|104|
|13201121001031|12|56|
|13201121001032|13|51|
|13201121001034|22|81|
|13201121001036|12|45|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

- ZONA 4

|13201121001037|10|38|
|---|---|---|
|13201121001039|24|82|
|13201121001040|40|157|
|13201121001041|12|48|
|13201121001042|12|55|
|13201121001043|12|43|
|13201121001044|20|69|
|13201121001045|20|86|
|13201121001046|20|76|
|13201121001047|16|74|
|13201121001048|24|103|
|13201121001049|63|214|
|13201121001050|22|101|
|13201121001051|24|99|
|13201121001052|24|89|
|TOTAL|526|2069|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201121004019|16|63|
|13201121004020|16|71|
|13201121004022|30|125|
|13201121004023|14|57|
|13201121004024|22|101|
|13201121004025|16|72|
|13201121004026|28|113|
|13201121004027|28|107|
|13201121004028|16|60|
|13201121004029|16|46|
|13201121004031|21|87|
|13201121004033|4|16|
|13201121004034|15|48|
|13201121004035|16|50|
|13201121004036|49|186|
|13201121004037|17|52|
|13201121004038|16|67|
|13201121004039|16|65|
|13201121004040|17|70|
|13201121004041|16|57|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

- ZONA 5

|13201121004042|17|53|
|---|---|---|
|13201121004043|27|108|
|13201121004044|20|72|
|13201121004045|18|69|
|13201121004046|16|63|
|13201121004047|16|65|
|13201121004048|16|64|
|13201121004049|21|77|
|13201121004050|20|76|
|13201121004051|12|47|
|13201121004052|13|46|
|13201121004053|20|62|
|13201121004054|125|486|
|13201121004056|16|69|
|TOTAL|746|2870|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201111002001|48|189|
|13201111002002|38|153|
|13201111002003|46|170|
|13201111002004|16|54|
|13201111002006|24|87|
|13201111002007|18|76|
|13201111002008|24|91|
|13201111002009|24|75|
|13201111002010|20|81|
|13201111002011|24|90|
|13201111002012|26|97|
|13201111002013|20|65|
|13201111002014|26|73|
|13201111002015|26|95|
|13201111002016|22|78|
|13201111002017|30|109|
|13201111002018|84|303|
|13201111002019|110|443|
|13201111002021|12|48|
|13201111002022|14|61|
|13201111002023|18|85|

|13201111002024|25|105|
|---|---|---|
|13201111002025|29|126|
|13201111002026|23|95|
|13201111002027|1|3|
|13201111002028|10|41|
|13201111002029|10|48|
|13201111002030|31|133|
|13201111002031|31|98|
|13201111002056|24|98|
|13201111002063|22|72|
|TOTAL|876|3342|

- ZONA 6

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201111001002|16|57|
|13201111001004|123|438|
|13201111001005|14|56|
|13201111001006|12|44|
|13201111001007|11|33|
|13201111001008|10|40|
|13201111001009|135|508|
|13201111001010|23|72|
|13201111001011|25|94|
|13201111001012|24|75|
|13201111001013|20|80|
|13201111001014|19|54|
|13201111001015|24|97|
|13201111001016|24|81|
|13201111001017|17|52|
|13201111001018|24|87|
|13201111001019|36|135|
|13201111001020|35|121|
|13201111001021|33|117|
|13201111001022|30|102|
|13201111001023|29|112|
|TOTAL|684|2455|

- ZONA 7

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201111002032|23|71|
|13201111002033|20|67|
|13201111002034|8|21|
|13201111002035|8|18|
|13201111002036|24|81|
|13201111002037|24|89|
|13201111002038|8|16|
|13201111002040|24|96|
|13201111002041|24|97|
|13201111002043|20|68|
|13201111002044|20|80|
|13201111002045|20|72|
|13201111002046|36|149|
|13201111002047|16|65|
|13201111002048|16|63|
|13201111002049|18|85|
|13201111002050|44|166|
|13201111002051|103|394|
|13201111002052|40|141|
|13201111002053|38|143|
|13201111002054|39|153|
|13201111002055|27|98|
|13201111002057|10|34|
|13201111002058|10|38|
|13201111002059|12|40|
|13201111002060|13|43|
|13201111002061|28|108|
|13201111002062|26|93|
|TOTAL|699|2589|

- ZONA 8

- ZONA 9

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201111001024|39|164|
|13201111001025|20|89|
|13201111001026|20|94|
|13201111001027|19|83|
|13201111001028|20|80|
|13201111001029|17|62|
|13201111001030|1|4|
|13201111001031|64|262|
|13201111001032|36|136|
|13201111001033|34|139|
|13201111001034|39|149|
|13201111001035|36|153|
|TOTAL|345|1415|

|MANZENT|CONTEO<br>VIVIENDA|CONTEO<br>PERSONA|
|---|---|---|
|13201111003001|89|362|
|13201111003002|16|63|
|13201111003003|40|165|
|13201111003004|40|153|
|13201111003005|16|74|
|13201111003006|19|69|
|13201111003007|40|151|
|13201111003008|45|177|
|13201111003009|18|80|
|13201111003010|18|68|
|13201111003011|41|181|
|13201111003012|40|173|
|13201111003013|23|98|
|13201111003014|20|97|
|13201111003015|46|174|
|13201111003016|42|166|
|13201111003017|22|94|
|13201111003018|20|86|
|13201111003019|42|160|

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

|13201111003020|16|81|
|---|---|---|
|13201111003021|1|3|
|13201111003022|46|184|
|13201111003023|124|514|
|13201111003024|202|825|
|13201111003025|16|50|
|13201111003026|4|20|
|13201111003027|14|52|
|13201111003028|23|69|
|13201111003029|18|71|
|13201111003030|23|96|
|13201111003031|23|79|
|13201111003032|24|97|
|13201111003033|22|84|
|13201111003034|18|62|
|13201111003035|24|78|
|13201111003036|24|82|
|TOTAL|1259|5038|

**2.3** **PROYECCIÓN DE ESCENARIO ACTUAL**

A la fecha de realización de este análisis aún no se cuenta con información actualizada que permita hacer un
análisis a nivel de manzana censal. Sin embargo la tendencia que muestra el periodo intercensal 1992 y 2002
permite prefigurar un escenario para el sector analizado en el presente texto.

Los resultados a nivel comunal para el año 2017 arrojan que la comuna cuenta con un total de 568.106
habitantes. Lo cual muestra un importante descenso en los ritmos de crecimiento mostrados en el periodo de
1982 a 2002.

Considerando la historia del crecimiento urbano de la comuna de Puente Alto se concluye que el polígono
analizado se trata de un sector residencial consolidado desde mediados de los noventa. Tal como lo muestra

el mapa de crecimiento histórico de la comuna.

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

Fuente: Municipalidad de Puente Alto [4]

De lo anterior se desprende que las zonas 5 y 7 hayan visto disminuido su explosivo crecimiento del periodo
intercensal 1992-2002. Y tomen un comportamiento como el visto por las demás zonas analizadas las cuales
mostraban bajas tasas de crecimiento o incluso decrecimiento poblacional.

Para refrendar este posible escenario se consultó el Plan Regulador de la comuna. En el cual las zonas
analizadas están catalogadas dentro de dos tipos: (i) Zona H1 [5] y (ii) Zona HE (m) 2. [6]

De esto se concluye que aquellos sectores catalogados dentro de las Zonas H1 se desarrollen procesos de
crecimiento o pérdida de población y viviendas tal como se observó en el periodo 1992-2002.

En la otra categorización se encuentra un sector reducido de la zona de análisis, correspondiente a la franja
entorno al eje Concha y Toro, (toma parte de las zonas 1,3 y 6). Estas están consideradas como zonas de
densificación residencial, lo cual podría provocar un aumento de la población en esta franja. Esta

4 http://www.mpuentealto.cl/localizate/?page_id=5811. Visitada el 05 de marzo de 2018.
5 Forma parte de Zonas Residenciales y de Equipamiento. Los usos permitidos en este tipo de zonas son: Residencial y
equipamiento de salud, educación, culto y cultura, social, seguridad, comercio y servicios. Además de infraestructura de
vialidad y aguas lluvia. Considera una densidad poblacional de 250 hab/ha (Reformulación Plan Regular Comunal,
Ordenanza Local, Municipalidad Puente Alto, 2002)
6 Corresponde a la franja en torno al eje Concha y Toro. Se trata de una zona de equipamiento y densificación
residencial, considera una densidad de 450 hab/ha. Esto se entiende, en parte, por la línea 4 del metro.

Proyecto DIA “Los Toros”
Análisis Demográfico, Área de Influencia Medio Humano

consideración proviene de la extensión de la Línea 4 del Metro, parte de la zona analizada se encuentra
dentro del área de influencia de la Estación Elisa Correa.

Sin embargo un estudio realizado por el Centro de Desarrollo Urbano Sostenible (CEDEUS) publicado en
2015, en el cual se analizó los procesos de densificación residencial e integración social en torno a estaciones
de transporte masivo, elaboró una tipología de 5 categorías de estaciones de metro, ubicando a la estación
mencionada (y todas las demás de la comuna) dentro de la categoría de ‘estaciones periféricas vivienda
social’. Al respecto señala que se trata de “17 estaciones en las comunas del poniente y sur de la ciudad.
Presentan las superficies construidas más bajas de toda la red y las densidades más elevadas del sistema
(sobre 300 hab/ha en algunos casos). Concentran la mayor cantidad de personas de bajos recursos, llegan a
agrupar a más de 70% de personas de estratos D y E en algunas estaciones del sur de Santiago (Santa Rosa
y San Ramón). El predio promedio es el más bajo de todas las tipologías de estaciones, es inferior a 200 m2
en casos específicos como la estación Grecia.” [7]

De las cinco categorías de zonas cuatro muestran alguna dinámica de inversión inmobiliaria, sin embargo la
quinta categoría (estaciones periféricas vivienda social) “no exhiben inversión, reciente o histórica y sus
territorios se componen, casi exclusivamente, de operaciones estatales desarrolladas entre los años 1960 y
2000.” [8]

En conclusión, de no mediar intervenciones mayores en el área analizada resulta altamente improbable que
exista un crecimiento explosivo de la población o del número de viviendas. Por lo que se espera que los
resultados del censo 2017 reflejen esta tendencia.

*****Proyección censal sin confirmación de INE:**

Se hizo el cálculo "manual" (sin la confirmación del INE para saber si está correcto), y éste confirma la misma
hipótesis inicial: se observa un casi estancamiento en el crecimiento de la población del sector analizado.

En el 92 en la zona analizada vivía el 8% de la población de la comuna, en 2002 la población correspondía al
4,8% del total comunal y se espera que en los resultados del censo 2017, la proporción de la población será
cercana al 4%. A su vez esto equivale a decir que la población en el polígono aumentaría un 0,5% por ende el
número de habitantes rondaría los 23.794, es decir la población de esta área tendería a estancarse.

7 “Densificación residencial e integración social en torno a estaciones de transporte masivo”, 2015, En: Propuestas para
Chile. Pontificia Universidad Católica de Chile. Disponible en:
https://www.researchgate.net/profile/Natan_Waintrub/publication/308892209_Densificacion_residencial_e_integracion_so
cial_en_torno_a_las_estaciones_de_transporte_masivo/links/580a61fc08ae2cb3a5d301a5/Densificacion-residencial-eintegracion-social-en-torno-a-las-estaciones-de-transporte-masivo.pdf
8 Ibid