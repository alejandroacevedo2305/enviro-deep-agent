---
title: Sin título
author: Desconocido
date: D:20140303160603
language: es
type: report
pages: 58
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - N
-->

## INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS “PROYECTO DE EXTRACCIÓN DE ÁRIDOS E INSTALACIONES ASOCIADAS POZO EL MANZANO PARA MEJORAMIENTO Y CONSERVACIÓN DE RUTA 43 DE LA REGIÓN DE COQUIMBO”

COMUNA DE ANDACOLLO, REGIÓN DE COQUIMBO

(Revisión B)

Documento preparado por:

**F.R.B. Ingeniería Ltda.**

28 de Febrero de 2014

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

ÍNDICE GENERAL

1.0 INTRODUCCIÓN ....................................................................................... 2

2.0 ANTECEDENTES DEL PROYECTO................................................................. 3

2.1 Localización Geográfica ........................................................................ 3

2.2 Instalaciones del Proyecto .................................................................... 5

2.3 Características Operacionales de Instalaciones del Proyecto ...................... 7

3.0 NORMATIVA SOBRE CALIDAD DEL AIRE.....................................................10

4.0 CALIDAD DEL AIRE en la zona del proyecto ................................................13

4.1 Estaciones de Monitoreo Consideradas ..................................................13

4.2 Información de Calidad del Aire............................................................15

5.0 METEOROLOGÍA EN LA ZONA DEL PROYECTO.............................................20

5.1 Estación de Monitoreo Considerada.......................................................20

5.2 Información Meteorológica...................................................................20

6.0 EMISIONES DE LA PLANTA .......................................................................25

6.1 Fuentes Emisoras ...............................................................................25

6.2 Emisiones Atmosféricas.......................................................................26

7.0 MODELACIÓN DE CALIDAD DEL AIRE.........................................................30

7.1 Modelo de Dispersión Utilizado y Datos de Entrada .................................30

7.2 Área de Modelación.............................................................................32

7.3 Resultados Obtenidos..........................................................................34

8.0 CONCLUSIONES......................................................................................55

ANEXOS:

Anexo A: Datos meteorológicos MM5 adquiridos para la modelación.
Anexo B: Archivos de entrada (input) y salida (output) de la modelación.

Sacyr Chile S.A 1 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

1.0 INTRODUCCIÓN

La empresa Sacyr Chile S.A. (en adelante, Sacyr) contempla llevar a cabo el proyecto
denominado “Extracción de Áridos e Instalaciones Asociadas - Pozo El Manzano para Mejoramiento de la Ruta 43 de la Región de Coquimbo” (en adelante, el Proyecto
o el Pozo El Manzano), consistente en la extracción y preparación de los áridos requeridos
para la construcción de la nueva calzada y el mejoramiento de la Ruta 43 Tramo Ovalle - La
Serena, obra pública correspondiente a la Concesión para el Mejoramiento y Conservación
de la Ruta 43 de la Región de Coquimbo, adjudicado al Licitante Sacyr Concesiones S.A.

El Proyecto se localiza en la comuna de Andacollo, provincia del Elqui, Región de Coquimbo,
al interior de un terreno de 18.182 hectáreas correspondiente al bien privado denominado
Comunidad Agrícola Cuesta El Manzano, ubicado a la altura del km 58 de la Ruta 43, en el
cruce con la Ruta D-51, que lleva hacia la localidad de Andacollo. Desde este cruce se
ingresa hasta el km 3,7 aproximadamente para tomar la Ruta D-323. El área del Proyecto se
encuentra a la altura del km 1,4 de esta última vía.

Forman parte del Proyecto un pozo de extracción de áridos, una planta de chancado y una
planta de asfalto, incluyendo también algunas áreas de acopio de materiales y un camino de

acceso.

El presente informe contiene los resultados de la modelación de las emisiones atmosféricas
(material particulado y gases de combustión) generadas durante la etapa de operación del
Proyecto. Para tales efectos se consideraron las emisiones diarias estimadas también por
Eco Master, contenidas en el documento “Estimación de emisiones atmosféricas Proyecto
Extracción de Áridos e Instalaciones Asociadas Pozo El Manzano para Mejoramiento y
Conservación de la Ruta 43 de la Región de Coquimbo”, Revisión 2, de fecha 25/02/2014.

Como resultado de la modelación de emisiones, se obtuvieron las concentraciones máximas
horarias, diarias y/o promedios anuales, dependiendo de las normas de calidad del aire
aplicables a material particulado de tamaño respirable (MP10), material particulado fino
(MP2.5), material particulado o polvo sedimentable (MPS), monóxido de carbono (CO),
dióxido de azufre (SO 2 ) y dióxido de nitrógeno (NO 2 ).

Corresponde destacar que la modelación de emisiones, y su efecto o impacto en la calidad
del aire, depende fuertemente de las condiciones meteorológicas y características
topográficas del área geográfica específica donde se emplazan las fuentes emisoras.
Asimismo cabe recordar que la modelación de la calidad del aire no es más que una
estimación de la forma cómo se comportaría o manifestaría la dispersión de las emisiones
en la atmósfera, bajo una serie de supuestos, entre las cuales se incluyen tasas de emisión,
composición de los contaminantes modelados, comportamiento temporal y espacial de las
fuentes emisoras, condiciones topográficas y, lo más importante, el comportamiento de las
variables meteorológicas, tanto de superficie como de altura. De ninguna forma reemplazan
a las mediciones o monitoreos reales, por muy bien calibrados que estén los modelos y muy
buena información meteorológica con que se disponga.

Sacyr Chile S.A 2 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

2.0 ANTECEDENTES DEL PROYECTO

2.1 Localización Geográfica

Desde el punto de vista político administrativo, el Proyecto se emplaza en la comuna de la
Andacollo, provincia del Elqui, Región de Coquimbo.

Como se indica anteriormente, el Proyecto se localiza al interior de un terreno de 18.182
hectáreas correspondiente al bien privado denominado Comunidad Agrícola Cuesta El
Manzano, ubicado a la altura del km 58 de la Ruta 43, en el cruce con la Ruta D-51, que
lleva hacia la localidad de Andacollo. Desde este cruce se ingresa hasta el kilómetro 3.7
aproximadamente para tomar la Ruta D-323. El área del Proyecto se encuentra a la altura
del kilómetro 1.4 de esta última vía.

El Cuadro 1 indica las coordinadas UTM de los vértices del área del Proyecto.

Cuadro 1: Coordenadas UTM de los vértices del área del Proyecto.

|Vértice|Coordenadas UTM<br>(Datum WGS-84, Huso 19 S)|Col3|
|---|---|---|
|Vértice|Norte|Este|
|1|6.662.625,00|287.189,00|
|2|6.661.635,00|288.733,00|
|3|6.661.393,00|288.677,00|
|4|6.661.993,00|287.242,00|

Fuente: Sacyr Chile S.A.

La Figura 1 muestra la ubicación geográfica del Proyecto.

Sacyr Chile S.A 3 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 1: Localización geográfica del Proyecto.

|Ubicación del Proye<br>Pozo El Manzano|Col2|Col3|
|---|---|---|
|**Ubicación del Proye**<br>**Pozo El Manzano**|**Ubicación del Proye**<br>**Pozo El Manzano**|**cto**<br>|
|**Ubicación del Proye**<br>**Pozo El Manzano**|**Ubicación del Proye**<br>**Pozo El Manzano**||

Fuente: Sacyr Chile S.A.

Por su parte, la Figura 2 muestra la ubicación geográfica del Proyecto en Google Earth.

Sacyr Chile S.A 4 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 2: Localización geográfica del Proyecto en Google Earth.

# N

Fuente: Elaboración propia sobre base Google Earth.

2.2 Instalaciones del Proyecto

La superficie total del predio Comunidad Agrícola Cuesta El Manzano es de 18.182
hectáreas. De este total, 39,02 hectáreas serán empleadas en el Proyecto, entre las cuales
24,2 hectáreas corresponderán a la explotación de áridos, mientras que las instalaciones
asociadas (planta de chancado, áreas de acopio y planta de asfalto), ocuparán una superficie
de 14,8 hectáreas, emplazadas en el borde poniente del polígono del Proyecto. A estas
superficies se deben agregar 0,3 hectáreas correspondientes al camino de acceso.

La Figura 3 ilustra la ubicación del área del Proyecto dentro del referido predio.

Sacyr Chile S.A 5 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 3: Emplazamiento del Proyecto.

Fuente: Sacyr Chile S.A.

Las principales instalaciones asociadas a la etapa de operación del Proyecto son: un área o
pozo de extracción de áridos, desde donde se extraerá el material; una planta de chancado,
necesaria para la fabricación de base chancada y áridos de distintas granulometrías; y una
planta de asfalto para la producción del aglomerado necesario para la pavimentación de
vías.

La Figura 4 ilustra el emplazamiento de las principales instalaciones del Proyecto.

Sacyr Chile S.A 6 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 4: Ubicación de principales instalaciones del Proyecto.

Fuente: Sacyr Chile S.A.

2.3 Características Operacionales de Instalaciones del Proyecto

A continuación se entrega una descripción general de cada una de las instalaciones del
Proyecto, en términos de las variables de interés desde el punto de vista de las emisiones
atmosféricas asociadas a la etapa de operación de las mismas.

Pozo de áridos:

La explotación de áridos abarca una superficie de 24,2 hectáreas. El volumen de explotación
efectivo se estima en aproximadamente 600.000 m [3] (1.020.000 toneladas) de material, en
un período de 17 meses.

Antes de iniciar la explotación, se realizará el replanteo topográfico y estacado de las áreas
de explotación, a partir de una distancia de 10 metros desde el camino público y de la línea
eléctrica. Dependiendo del ancho del área a explotar, se replantearán las celdas paralelas al
eje del Proyecto, a fin de realizar una extracción en forma ordenada, conforme a los perfiles
transversales propuestos.

Sacyr Chile S.A 7 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Las franjas de explotación serán definidas con estacado, se explotarán en sentido
longitudinal, iniciándose el proceso desde la sección de aguas arriba de la zona de plantas de
producción, hacia aguas abajo, hasta el camino de acceso al predio, lugar donde el área de
extracción queda dividida. En estas franjas se retirará el material no apto para el proceso de
chancado, acopiándose en las riberas laterales, para luego realizar la extracción del material
utilizable. La potencia del estrato de materiales no aptos puede variar entre 1 a 2 m, el cual
será devuelto al área excava en el cierre de las operaciones, perfilándolo a fin de dejar una
sección ordenada y homogénea. El mismo proceso se realizará en el área ubicada aguas
abajo del camino de acceso al predio.

Para la obtención de 600.000 m [3] efectivos de material, será necesario excavar y remover un
volumen de aproximadamente 790.000 m [3] (1.343.000 toneladas) de material. La diferencia
(190.000 m [3] ó 323.000 ton) corresponde a material de rechazo que será devuelto al lecho
de la quebrada.

Desde el pozo de áridos se extraerá y transportará aproximadamente 80.000 m [3] (136.000
toneladas) de material integral para la construcción de los terraplenes de la Ruta 43. Así
también se podrá realizar una graduación de material in situ de una parte de los materiales,
aproximadamente 100.000 m [3] (170.000 toneladas) para obtener áridos bajo 4”, necesario
para conformar la coronación de terraplenes de la Ruta 43. Los materiales sobre 4” se
devuelven al área de extracción. Se estima que el material integral y bajo 4” a transportar
directamente hasta la Ruta 43 será de 100 viajes diarios durante un período de 5 meses
(considerando 24 días/mes y flota de 15 camiones de 15 m [3] ó 25,5 toneladas de capacidad).

De los 600.000 m [3] de material a extraer, 420.000 m [3] (714.000 toneladas) serán
transportados a la planta de chancado, lugar donde se procesarán áridos de distinta
granulometría. Se estima que el transporte de material a la planta de chancado generará
aproximadamente 69 viajes/día durante un período aproximado de 17 meses (considerando
24 días/mes y flota de 6 camiones de 15 m [3] ó 25,5 toneladas de capacidad).

La extracción, transporte y alimentación a la planta de chancado, se realizará con los
siguientes equipos:

 - Extracción y alimentación: 2 excavadoras de 30 toneladas y 15 camiones tolva de 15
m [3] .

 - Manejo y conformación de acopios: 4 cargadores frontales de 3,5 m [3] y 4 camiones
tolva de 15 m [3] .

Planta de chancado:

Corresponde a una planta marca Alquezar, modelo 500, con una capacidad máxima de
producción de 350 ton/hora de material procesado. Estará compuesta básicamente por un
buzón de entrada, molinos, harneros y cintas transportadoras. El acopio de los materiales
procesados se realizará mediante un cargador frontal que trasladará el material procesado
(proveniente de las cintas transportadoras) a la zona de acopio definitivo.
El proceso de chancado se resume a continuación.

- El procesamiento del material en la planta comienza en el buzón alimentador donde

el material es vaciado desde los camiones tolva.

Sacyr Chile S.A 8 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

- Desde el alimentador la roca pasa a un primer chancador o chancador primario para
ser transportada en dos cintas hasta las cribas que seleccionan el material en tres
granulometrías.

- Estas tres granulometrías a su vez son transportadas por tres cintas hacia los molinos
o chancadoras que realizan el procesamiento que deriva en la obtención de base
chancada, gravas y gravillas.

- Las gravas y gravillas caen de las cintas a las pilas de acopio, desde donde son
trasladadas a distintos patios de acopios incorporado al Proyecto que en total suman
una superficie cercana a 3 hectáreas.

El acopio de los áridos se realiza mediante cargador frontal desde la salida de las cintas
transportadoras a las áreas de acopio, pudiendo también utilizarse camiones tolva.

Las cintas transportadoras que salen de los molinos o chancadores se encuentran
encapsuladas y con aplicación de agua, ya que en esta etapa del proceso es donde se
genera la mayor parte de las emisiones de material fino a la atmósfera. Las cintas
encapsuladas son 10, de un total de 15. Las 5 restantes son las cintas que entran y salen de
la criba o seleccionadora principal que no se encuentran encapsuladas por cuanto el material
sólo se clasifica para pasar a los molinos o chancadores.

Los equipos de la planta contarán con malla raschel y aspersores de agua para el control de
las emisiones.

Para satisfacer sus requerimientos de energía, la planta contará con un grupo electrógeno de
620 kVA.

De la planta de chancado se obtendrán aproximadamente 300.000 m [3] (510.000 toneladas)
de base chancada y 120.000 m [3] (204.000 toneladas) áridos de asfalto. Este material será
trasladado a los patios de acopio donde se acumulará temporalmente para ser utilizado para
relleno estructural de Ruta 43 o en la fabricación de asfalto. El manejo interno del material
producido en la planta de chancado se realizará mediante 4 cargadores frontales de 3,5 m [3] y
4 camiones tolva de 15 m [3], durante los 17 meses.

Para transportar los 300.000 m [3] de base chancada hasta la Ruta 43 se realizará a través de
aproximadamente 69 viajes/día, durante un período de 12 meses (considerando 24
días/mes y camiones de 15 m [3] ó 25,5 toneladas de capacidad).

Planta de asfalto:

Consta de equipos propios para la fabricación de la mezcla asfáltica, a saber: unidad
alimentadora, unidad secadora de áridos, unidad dosificadora-mezcladora, equipo de
recuperación, depuración y dosificación de filler, filtro de mangas, equipo de
almacenamiento y calentamiento de asfalto (caldera de fluido térmico), estanque de fuel oil
No5 para el funcionamiento del secador de áridos (horno rotatorio) y estanque de fuel oil
No1 para el funcionamiento de la caldera y grupo electrógeno.

El funcionamiento de la planta de asfalto se realiza en caliente a una temperatura de 160oC.

Sacyr Chile S.A 9 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

El proceso se inicia con la colocación de los áridos en las tolvas en frío o alimentadores,
desde donde pasan a través de cintas transportadoras hacia el tambor de secado hasta
alcanzar la temperatura deseada. Desde allí son conducidos a la denominada criba
seleccionadora mediante un elevador de áridos.

Durante la selección o cribado del material, se realizará el aspirado del polvo fino o filler.
Este polvo será conducido a los filtros de mangas desde será recuperado e integrado
nuevamente al proceso. El polvo ingresa a la cámara y se adhiere a los filtros. Debido a la
condensación que se produce al interior de la cámara se genera vapor de agua que es
expelido a través de una chimenea. El polvo se desprende de los filtros de manga y es
reintegrado al proceso de fabricación de asfalto. Del filler de recuperación se generan
excedentes que son manejados en un patio especialmente diseñado para ello, a fin de evitar
la dispersión del polvo.

Los áridos para la fabricación de asfalto provienen de la planta de chancado y son de 3
granulometrías: 0-6 mm, 6-12 mm y 12-18 mm, los que serán acopiados en el predio para
su posterior uso en la fabricación de la mezcla.

Para satisfacer sus requerimientos de energía, la planta contará con un grupo electrógeno de
650 kVA.

La producción de asfalto no se realiza en forma continua durante el período de operación de
la planta, sino en períodos bien específicos de tiempo, de tal forma que la producción media
diaria es variable, entre 500 y 1.900 ton/día. Para efectos de la presente DIA del Proyecto y
las estimaciones de emisiones atmosféricas asociadas, se considerará una media de 1.200
ton/día durante los 10 meses de producción de asfalto.

El asfalto total que se dispondrá en obra alcanza a 214.200 toneladas, cifra proveniente de
la suma de 204.000 toneladas de áridos (120.000 m [3] ) y 10.200 toneladas de betún.

La distribución de asfalto a la obra se realizará por camino habilitado del Proyecto hasta la
Ruta 43 ingresando a la carretera en el km 53. Para transportar 214.200 toneladas de
asfalto, se estima una media de 30 viajes/día de camiones hacia la Ruta 43, durante los 10
meses de producción (considerando 24 días/mes y camiones de 15 m [3] ó 30 toneladas de
capacidad).

3.0 NORMATIVA SOBRE CALIDAD DEL AIRE

A nivel nacional, la normativa sobre calidad del aire, se encuentra contenida en los
siguientes cuerpos legales:

 - Decreto Supremo N°59/98 del Ministerio Secretaría General de la Presidencia [1], que
establece las normas de calidad del aire primarias para Material Particulado
Respirable (MP10).

 - Decreto Supremo N°12/11 del Ministerio del Medio Ambiente, que establece las
normas de calidad del aire primarias para Material Particulado Fino (MP2.5).

 - Decreto Supremo N°113/02 del Ministerio Secretaría General de la Presidencia, que
establece las normas de calidad del aire primarias para Dióxido de Azufre (SO 2 ).

1 Incluyendo las modificaciones introducidas por el Decreto Supremo N°45/01 del Ministerio Secretaría General de
la Presidencia.

Sacyr Chile S.A 10 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

 - Decreto Supremo N°114/02 del Ministerio Secretaría General de la Presidencia, que
establece las normas de calidad del aire primarias para Dióxido de Nitrógeno (NO 2 ).

 - Decreto Supremo N°115/02 del Ministerio Secretaría General de la Presidencia, que
establece las normas de calidad del aire primarias para Monóxido de Carbono (CO).

 - Decreto Supremo N°22/10 del Ministerio Secretaría General de la Presidencia, que
establece las normas de calidad del aire secundarias para SO 2 .

Corresponde indicar que las normas de calidad del aire, en este caso para SO 2, están
orientadas a proteger la salud de las personas, mientras que las normas secundarias tienen
por objeto la protección y conservación de los recursos naturales renovables del ámbito
silvoagropecuario y de vida silvestre, de los efectos agudos y crónicos generados por la
exposición a SO 2 en el aire.

El Cuadro indica las concentraciones o límites máximos permisibles que establece cada uno
de los cuerpos legales antes indicados.

Cuadro 2: Normas de calidad del aire vigentes a nivel nacional.

|Cuerpo Legal|Contaminante<br>Normado|Límite Máximo<br>Establecido|Período<br>Normado|Criterios de Superación de las<br>Normas|
|---|---|---|---|---|
|D.S. N°59/98<br>MINSEGPRES|MP10|150 ug/m3N(1)|Diario|Percentil 98 de los valores diarios<br>registrados en un año calendario,<br>supera el valor de la norma diaria;<br>o si en un año calendario se<br>supera en más de 7 ocasiones el<br>valor de la norma diaria.|
|D.S. N°59/98<br>MINSEGPRES|MP10|50 ug/m3N(1)|Anual|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos de promedios<br>anuales, es igual o superior al<br>valor de la norma anual.|
|D.S. N°12/11<br>MMA|MP2.5|50 ug/m3N(1)|Diario|Percentil 98 de los valores diarios<br>registrados en un año calendario,<br>es superior al valor de la norma<br>diaria.|
|D.S. N°12/11<br>MMA|MP2.5|20 ug/m3N(1)|Anual|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos de promedios<br>anuales, es superior al valor de la<br>norma anual.|
|D.S. N°113/02<br>MINSEGPRES|SO2|250 ug/m3N <br>(ó 96 ppbv)(1) <br>|Diaria|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99<br>de<br>los<br>valores<br>diarios<br>registrados en cada año, es igual o<br>superior al valor de la norma<br>diaria.|
|D.S. N°113/02<br>MINSEGPRES|SO2|80 ug/m3N <br>(ó 31 ppbv)(1)|Anual|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos de promedios<br>anuales, es igual o superior al<br>valor de la norma anual.|
|D.S. N°22/10<br>MINSEGPRES|SO2|700 ug/m3N <br>(ó 268 ppbv)(2)|Horario|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99,73 de las concentraciones de 1|

hora registradas en cada año, es
igual o superior al valor de la

Sacyr Chile S.A 11 norma horaria; o si el Percentil Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

|Cuerpo Legal|Contaminante<br>Normado|Límite Máximo<br>Establecido|Período<br>Normado|Criterios de Superación de las<br>Normas|
|---|---|---|---|---|
|||||99,73 de las concentraciones de 1<br>hora<br>registradas<br>en<br>un<br>año<br>calendario, es igual o superior al<br>valor de la norma horaria.|
|||260 ug/m3N <br>(ó 99 ppbv)(2)|Diaria|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99,7<br>de<br>los<br>valores<br>diarios<br>registrados es igual a superior al<br>valor de la norma diaria; o si el<br>Percentil<br>99,7<br>de<br>los<br>valores<br>diarios registrados en un año<br>calendario es igual o superior al<br>doble de la norma diaria.|
|||60 ug/m3N <br>(ó 23 ppbv)(2)|Anual|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos de promedios<br>anuales, es igual o superior a la<br>norma anual; o si el promedio de<br>un año calendario es igual o<br>superior al valor de la norma<br>anual.|
|D.S. N°114/02<br>MINSEGPRES|NO2|400 ug/m3N <br>(ó 213 ppbv)(1)|Horaria|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99 de los máximos diarios de 1<br>hora registrados en cada año, es<br>igual o superior al valor de la<br>norma horaria.|
|D.S. N°114/02<br>MINSEGPRES|NO2|100 ug/m3N <br>(ó 53 ppbv)(1)|Anual|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios<br>seguidos<br>de<br>los<br>promedios anuales, es igual o<br>superior al valor de la norma<br>anual.|
|D.S. N°115/02<br>MINSEGPRES|CO|30 mg/m3N <br>(ó 26 ppmv)(1)|Hora|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99 de los máximos diarios de<br>concentración<br>de<br>1 <br>hora<br>registrados en cada año, es igual o<br>superior al valor de la norma<br>horaria.|
|D.S. N°115/02<br>MINSEGPRES|CO|10 mg/m3N <br>(ó 9 ppmv)(1)|8 Horas|Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99 de los máximos diarios de 8<br>horas registrados en cada año, es<br>igual o superior al valor de la<br>norma de 8 horas.|

Notas:
(1) Norma primaria de calidad del aire.
(2) Norma secundaria de calidad del aire.
Fuente: Elaboración propia.

A nivel nacional no existe normativa aplicable a Material Particulado o Polvo Sedimentable
(MPS). Por esta razón se ha utilizado el valor de referencia propuesto por la Confederación
Suiza; 200 mg/m [2] /día como promedio anual.

Sacyr Chile S.A 12 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

4.0 CALIDAD DEL AIRE EN LA ZONA DEL PROYECTO

4.1 Estaciones de Monitoreo Consideradas

En la comuna de Andacollo, el Sistema Información Nacional de Calidad del Aire (SINCA,
http://sinca.mma.cl), cuenta con 5 estaciones de monitoreo de calidad del aire. Estas
estaciones son las siguientes:

- Estación Andacollo;

- Estación Chepiquilla;

- Estación El Sauce;

- Estación Hospital;

- Estación Urmeneta-Plaza Centenario.

El Cuadro 3 indica la ubicación geográfica de ambas estaciones, los contaminantes
monitoreados y los períodos para los cuales se dispone de información.

Cuadro 3: Antecedentes estaciones de monitoreo de calidad del aire en comuna de

Andacollo.

|Estación de<br>Monitoreo|Coordenadas UTM<br>(WGS-84, H 19S)|Col3|Contaminantes<br>Monitoreados|Período de Datos<br>Disponibles(1)|
|---|---|---|---|---|
|Estación de<br>Monitoreo|Este|Norte|Norte|Norte|
|Andacollo|299.239|6.654.143|MP10|17/07/2009-26/02/2014|
|Andacollo|299.239|6.654.143|MP2.5|Sin información disponible|
|Chepiquilla|299.429|6.651.104|MP10|02/01/2005-26/04/2010|
|El Sauce|298.643|6.653.356|MP10|01/06/2009-31/05/2010|
|Hospital|299.414|6.654.515|MP10|03/01/2010-31/05/2010|
|Urmeneta-<br>Plaza<br>Centenario|299.288|6.652.817|MP10|02/01/2005-20/04/2010|

(1) Información disponible al 26/02/2014.
(2) Coordenadas en WGS-84, Huso H 19S.
Fuente: Basado en datos disponibles en sitio web del Sistema de Información Nacional de Calidad del Aire, SINCA
(http://sinca.mma.cl).

Como se puede observar de la tabla anterior, las Estaciones Chepiquilla, El Sauce, Hospital y
Urmeneta-Plaza Centenario sólo disponen registros históricos de MP10 hasta Abril o Mayo
del año 2010. Sólo la Estación Andacollo dispone de información reciente para Material
Particulado Respirable (MP10). Ninguna de las estaciones considera el monitoreo de gases
contaminantes, tales como Dióxido de Azufre (SO 2 ), Monóxido de Carbono (CO) o Dióxido de
Nitrógeno (NO 2 ), ni tampoco Material Particulado Fino (MP2.5) [2] y Material Particulado
Sedimentable (MPS).

Con el objeto de subsanar la ausencia de datos sobre MP2.5 en la zona del Proyecto, se
consideró la información de este contaminante registrada en las Estaciones Coquimbo y La
Serena, ubicadas respectivamente en las comunas de los mismos nombres.

2 La Estación Andacollo aparentemente dispone de un monitor de MP2.5, pero no existe información de acceso
público sobre mediciones realizadas desde su implementación (14/02/2012).

Sacyr Chile S.A 13 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

El Cuadro 4 indica la ubicación geográfica de las Estaciones Coquimbo y La Serena, los
contaminantes monitoreados y los períodos para los cuales se dispone de información.

Cuadro 4: Antecedentes de estaciones de monitoreo de calidad del aire en
Coquimbo y La Serena.

|Estación de<br>Monitoreo|Coordenadas UTM<br>(WGS-84, H 19S)|Col3|Contaminantes<br>Monitoreados|Período de Datos<br>Disponibles(1)|
|---|---|---|---|---|
|Estación de<br>Monitoreo|Este|Norte|Norte|Norte|
|Coquimbo|274.603|6.682.159|MP2.5|26/01/2014-12/02/2014|
|La Serena|282.210|6.687.902|MP2.5|26/01/2014-10/02/2014|

(1) Información disponible al 26/02/2014.
(2) Coordenadas en WGS-84, Huso H 19S.
Fuente: Basado en datos disponibles en sitio web del Sistema de Información Nacional de Calidad del Aire, SINCA
(http://sinca.mma.cl).

Consistente con lo antes expuesto, para efectos del presente estudio, se consideraron las
mediciones de MP10 registradas en la Estación Andacollo y las concentraciones de MP2.5
medidas en las Estaciones Coquimbo y La Serena.

Para MPS, CO, SO 2 y NO 2, sin embargo, no se logró obtener información sobre eventuales
mediciones oficiales para estos contaminantes, que pudiesen haberse realizado en la zona
del Proyecto, en la comuna de Andacollo o en las comunas de Coquimbo y La Serena.

La Figura 5 ilustra la ubicación geográfica de las Estaciones Andacollo, Coquimbo y La
Serena.

Sacyr Chile S.A 14 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 5: Localización de las estaciones de monitoreo Andacollo, Coquimbo y La
Serena.

Fuente: Elaboración propia sobre mapa Google Earth.

4.2 Información de Calidad del Aire

Consistente con lo descrito en el punto anterior, para efectos de la definición de la línea base
de calidad del aire del área de influencia del Proyecto, se consideró lo siguiente:

Sacyr Chile S.A 15 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

- MP10: A partir de los resultados del monitoreo de este contaminante realizado en la
Estación Andacollo, durante el período Enero - Diciembre de 2013.

- MP2.5: A partir de los resultados de las mediciones puntuales de este contaminante
realizadas en las Estaciones Coquimbo y La Serena, en Enero y Febrero del año 2014.

- MPS: Ante la ausencia de información para este contaminante, se consideró de
manera meramente referencial, rango de concentraciones obtenidas de mediciones
realizadas en las zonas centro y norte del país.

- CO, SO 2 y NO 2 : Antes la ausencia de información para estos contaminantes, se
consideró como referencia la información disponible en el sitio web del SINCA para
otras ciudades del país.

A continuación se entrega los resultados de este análisis.

4.2.1 Material Particulado Respirable (MP10)

La Figura 6 muestra las series de tiempo de las concentraciones diarias de MP10 para el
período Enero - Diciembre de 2013, para la Estación Andacollo.

Figura 6: Series de tiempo de concentraciones diarias de MP10 en Estación
Andacollo; período Enero - Diciembre de 2013.

Fuente: Elaboración propia a partir del procesamiento de datos disponibles en sitio web del Sistema de Información
Nacional de Calidad del Aire, SINCA (http://sinca.mma.cl).

El Cuadro 5 resume los resultados del procesamiento de los datos diarios de MP10 en la
Estación Andacollo, para el período analizado.

Sacyr Chile S.A 16 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Cuadro 5: Resultados procesamiento de datos diarios de MP10 en Estación
Andacollo; período Enero - Diciembre de 2013.

|Parámetros|Estación de Monitoreo|
|---|---|
|Parámetros|Andacollo|
|Período de datos analizados|01/01/2013-31/12/2013|
|Número de datos diarios|259|
|Promedio anual (ug/m3N)|64,0|
|Norma anual (ug/m3N)|50,0|
|Percentil 98 de valores diarios (ug/m3N)|121,0|
|Máximo diario anual (ug/m3N)|172,9|
|Mínimo diario (ug/m3N)|7,0|
|Número de días sobre norma diaria|1|
|Número de días sobre 80% norma diaria (>120 ug/m3N)|5|
|Norma diaria (ug/m3N)|150,0|

Fuente: Elaboración propia a partir del procesamiento de datos disponibles en sitio web del Sistema de Información
Nacional de Calidad del Aire, SINCA (http://sinca.mma.cl).

Del cuadro anterior se deduce que, para el período analizado (Enero - Diciembre 2013), la
Estación Andacollo superó tanto la norma de calidad del aire diaria como la norma anual
para MP10. En efecto, el promedio anual de MP10 (64,0 ug/m [3] N) superó el valor establecido
por la respectiva norma (50 ug/m [3] N), y en una ocasión (172,9 ug/m [3] N ) se superó la norma
diaria (150 ug/m [3] N ). Sin embargo, el Percentil 98 [3] de los valores diarios de MP10 (121,0
ug/m [3] N) no superó la norma diaria (150 ug/m [3] N). Corresponde destacar que en 5 ocasiones
la concentración diaria de MP10 superó el 80% de la norma diaria (condición de latencia).

4.2.2 Material Particulado Fino (MP2.5)

La Figura 7 muestra las series de tiempo de las concentraciones diarias de MP2.5 para el
período Enero - Febrero de 2014, registrado en las Estaciones Coquimbo y La Serena [4] .

3 Percentil: Corresponde a la concentración del elemento de orden “k" calculada a partir de una lista establecida
de valores ordenada en forma creciente (X1<<X2<<X3...<<Xk...<<Xn-1<<Xn), donde “k” se calcula como k =
q * n, en que "q" = 0,98 para el Percentil 98 y "n" corresponde a un número de datos de la serie.
4 Basado en datos diarios de MP2.5 disponibles en el sitio web de SINCA (datos no validados), donde se eliminó
del presente análisis aquellos datos que se escapaban de las tendencias esperadas.

Sacyr Chile S.A 17 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 7: Series de tiempo de concentraciones diarias de MP2.5 en Estaciones
Coquimbo y La Serena; período Enero a Febrero de 2014.

Fuente: Elaboración propia a partir del procesamiento de datos disponibles en sitio web del Sistema de Información
Nacional de Calidad del Aire, SINCA (http://sinca.mma.cl).

El Cuadro 6 resume los resultados del procesamiento de los datos diarios de MP2.5 de
ambas estaciones, para el período analizado.

Sacyr Chile S.A 18 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Cuadro 6: Resultados procesamiento de datos diarios de MP2.5 en Estaciones
Coquimbo y La Serena; período Enero - Febrero de 2014.

|Parámetros|Estaciones de Monitoreo|Col3|
|---|---|---|
|Parámetros|Coquimbo|La Serena|
|Período de datos analizados|26/01/2014-10/02/2014|26/01/2014-09/02/2014|
|Número datos diarios|16|15|
|Promedio período (ug/m3N)|9,0|18,7|
|Norma anual (ug/m3N)|20,0|20,0|
|Percentil 98 de valores diarios (ug/m3N)|-|-|
|Máximo diario (ug/m3N)|12,5|22,4|
|Mínimo diario (ug/m3N)|6,2|14,0|
|Número de días sobre norma diaria|0|0|
|Número de días sobre 80% norma diaria<br>(>120 ug/m3N)|0|0|
|Norma diaria (ug/m3N)|50,0|50,0|

Fuente: Elaboración propia a partir del procesamiento de datos disponibles en sitio web del Sistema de Información
Nacional de Calidad del Aire, SINCA (http://sinca.mma.cl).

4.2.3 Material Particulado Sedimentable (MPS)

Sólo para efectos de evaluar el eventual impacto del Proyecto en el entorno rural de la
comuna de Andacollo, se ha considerado que la concentración anual de MPS podría alcanzar
valores similares a los registrados en otras localidades rurales de la zona norte del país.
Según antecedentes obtenidos, en localidades de las zonas central y norte del país, las
concentraciones anuales de MPS han fluctuado entre 40 y 80 mg/m [2] /día.

Del cuadro anterior se deduce que, para el período analizado (Enero - Febrero 2013), la
Estación Coquimbo no superó la norma de calidad del aire diaria ni tampoco anual para
MP2.5. En efecto, el promedio del período (9,0 ug/m [3] N) se encuentra muy por debajo del
valor establecido por la respectiva norma anual para MP2.5 (20 ug/m [3] N), al igual que el
valor máximo diario (12,5 ug/m [3] N) tampoco superó la norma diaria (50 ug/m [3] N).

En cuanto a la Estación La Serena, ésta también tampoco superó ninguna de las normas
para MP2.5. El promedio del período (18,7 ug/m [3] N) no superó la respectiva norma anual (20
ug/m [3] N), al igual que el valor máximo diario (22,5 ug /m [3] N) que está muy por debajo del
valor de la norma diaria (50 ug/m [3] N).

4.2.4 Monóxido de Carbono (CO)

También a partir de datos disponibles en sitio web del SINCA (http://sinca.mma.cl), el rango
de concentraciones de CO registradas en ciudades de la zona centro-sur del país, que
cuentan con monitoreo permanente de este contaminante, los valores horarios y los
promedios de 8 horas continuas, se encuentran en torno a 10-20 partes por millón (ppm) y
3-5 ppm, respectivamente. Estos valores están muy por debajo de las normas horarias y de
8 horas, esto es, 26 ppm y 9 ppm, respectivamente.

4.2.5 Dióxido de Azufre (SO 2 )

A partir de datos disponibles en sitio web del Sistema de Información Nacional de Calidad
del Aire, SINCA (http://sinca.mma.cl), el rango de concentraciones de SO 2 registradas en
ciudades de la zona centro-sur del país, que cuentan con monitoreo permanente de este

Sacyr Chile S.A 19 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

contaminante, los promedio anuales fluctúan en torno a 3-5 partes por billón (ppb), con
valores máximos diarios que normalmente no superan 20 ppb. Corresponde indicar que la
norma diaria (primaria) para SO 2 es 96 ppb, mientras la norma anual (primaria) alcanza a
31 ppb.

4.2.6 Dióxido de Nitrógeno (NO 2 )

También a partir de datos disponibles en sitio web del SINCA (http://sinca.mma.cl), el rango
de concentraciones de NO 2 registradas en ciudades de la zona centro-sur del país, que
cuentan con monitoreo permanente de este contaminante, los promedio anuales fluctúan en
torno a 5-20 ppb, con valores máximos horarios que no superan el rango 50-150 ppb.
Corresponde indicar que la norma anual para NO 2 es 53 ppb y la norma horaria alcanza a
213 ppb.

5.0 METEOROLOGÍA EN LA ZONA DEL PROYECTO

5.1 Estación de Monitoreo Considerada

De las estaciones del Sistema de Información Nacional de Calidad del Aire, SINCA
(http://sinca.mma.cl) existentes en la zona, la Estación Andacollo es la única que posee
registros históricos para algunas variables meteorológicas. Sin embargo, esta estación se
encuentra a más de 15 km en línea recta al área del Proyecto, en una zona geográfica y
topográficamente muy distinta a la del Proyecto, razón por la cual se optó por dar
preferencia a los datos de la Estación Las Cardas por ser más representativos de la zona de
emplazamiento del Proyecto.

La Estación Las Cardas se localiza en la comuna de Coquimbo, a aproximadamente 13 km al
sur del Proyecto, siguiendo la dirección de la Ruta 43. Esta estación pertenece a la Facultad
de Ciencias Agronómicas de la Universidad de Chile, depende del Centro de Estudios de
Zonas Áridas (CEZA) y tiene como objetivo principal realizar investigaciones en materias
relacionadas con sistemas productivos para zonas áridas y transferencia de los
conocimientos adquiridos a través de la docencia y extensión.

5.2 Información Meteorológica

Para efectos del presente estudio, se optó por utilizar los datos meteorológicos de la
Estación Las Cardas correspondientes al año calendario 2013 (01 de Enero al 31 de
Diciembre de 2013). Con esta información se definió las condiciones meteorológicas de
superficie de la zona del Proyecto.

En cuanto a datos meteorológicos de altura, en Chile, esta información es escasa o
inexistente, por lo que fue necesario encargarla a una empresa americana
(www.weblakes.com). En el punto 7.1 del presente informe se entregan más antecedentes
sobre esta materia.

A continuación se entrega el análisis de la información meteorológica obtenida de los
registros de la Estación Las Cardas.

Sacyr Chile S.A 20 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

5.2.1 Temperatura Ambiente

La Figura 8 muestra las series de tiempo de la temperatura ambiente horaria (°C) para el
período Enero - Diciembre de 2013, en la Estación Las Cardas.

Figura 8: Series de tiempo de temperatura ambiente horaria en la Estación Las
Cardas; período Enero - Diciembre de 2013.

Fuente: Basado en datos disponibles para la Estación Las Cardas.

5.2.3 Velocidad del Viento

La Figura 9 muestra las series de tiempo de la velocidad del viento horaria (m/s) para el
período Enero - Diciembre de 2013, en la Estación Las Cardas.

Sacyr Chile S.A 21 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 9: Series de tiempo de velocidad del viento horaria en la Estación Las
Cardas; período Enero - Diciembre de 2013.

Fuente: Basado en datos disponibles para la Estación Las Cardas.

5.2.4 Rosas de Viento

Las Figuras 10 y 11 muestran las rosas de viento anual y estacional para el período EneroDiciembre de 2013, respectivamente, en la Estación Las Cardas. Las imágenes fueron
generadas mediante el programa WRPLOT View (Wind Rose Plot for Meteorologica Data).

Sacyr Chile S.A 22 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 10: Rosa de viento anual en la Estación Las Cardas; período EneroDiciembre de 2013.

Fuente: Basado en datos disponibles para la Estación Las Cardas.

Sacyr Chile S.A 23 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Figura 11: Rosas de viento estacional en la Estación Las Cardas; período Enero Diciembre de 2013.

|Rosa de viento Verano|Rosa de viento Otoño|
|---|---|
|<br>**Rosa de viento Invierno**|<br>**Rosa de viento Primavera**|

Fuente: Basado en datos disponibles para la Estación Las Cardas.

Sacyr Chile S.A 24 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

La Figura 12 muestra las rosas de viento diurno y nocturno para el período en la Estación
Las Cardas. Estas imágenes fueron generadas mediante el programa WRPLOT View (Wind
Rose Plot for Meteorologica Data).

Figura 12: Rosas de viento diurna y nocturna en la Estación Las Cardas; período
Enero - Diciembre de 2013.

Fuente: Basado en datos disponibles para la Estación Las Cardas.

6.0 EMISIONES DE LA PLANTA

6.1 Fuentes Emisoras

Las principales fuentes de emisión de material particulado (y gases de combustión
(básicamente monóxido de carbono, óxidos de azufre y óxidos de nitrógeno), generadas por la
etapa de operación del Proyecto, están asociadas a la extracción y procesamiento y manejo de
áridos, al funcionamiento de camiones, maquinaria y equipos, y a la circulación de camiones y
maquinaria.

En efecto, la extracción y procesamiento de áridos generará emisiones principalmente de
material particulado producto de las actividades de escarpe y extracción de material,
extracción, selección, transporte, procesamiento, manejo, acopio y carguío de áridos, y
transporte de estos materiales (circulación de camiones por rutas no pavimentadas al interior
del área del Proyecto).

Sacyr Chile S.A 25 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Por su parte, el uso de camiones, maquinaria y ciertos equipos (grupos electrógenos), generará
emisiones tanto de material particulado como de gases de combustión interna provenientes de
sus motores (emisiones de escape de motores Diesel). Así también el uso de otros equipos
(caldera de fluido térmico y horno rotatorio) también generará emisiones de material
particulado y gases de combustión, en este caso derivadas de procesos de combustión externa.

El Cuadro 7 muestra las fuentes de emisión de contaminantes atmosféricos más importantes
identificadas para la etapa de operación del Proyecto .

Cuadro 7: Fuentes de emisiones atmosféricas etapa de operación del Proyecto.

|TIPO DE<br>EMISIONES|FUENTES DE EMISIÓN|CONTAMINANTES(*)|
|---|---|---|
|Fugitivas de<br>material<br>particulado|Escarpe del terreno (Pozo de Áridos)|Material particulado|
|Fugitivas de<br>material<br>particulado|Excavación del terreno - material no apto (Pozo de Áridos)|Material particulado|
|Fugitivas de<br>material<br>particulado|Extracción de áridos (Pozo de Áridos)|Material particulado|
|Fugitivas de<br>material<br>particulado|Selección de áridos bajo 4 “(Pozo de Áridos)|Material particulado|
|Fugitivas de<br>material<br>particulado|Carguío de áridos (Pozo de Áridos)||
|Fugitivas de<br>material<br>particulado|Transporte interno de áridos (Pozo de Áridos)|Material particulado|
|Fugitivas de<br>material<br>particulado|Transporte material integral y bajo 4” por camino interno<br>hasta Ruta 43 (Pozo de Áridos)|Material particulado|
|Fugitivas de<br>material<br>particulado|Procesamiento y manejo de áridos (Planta de Chancado)|Material particulado|
|Fugitivas de<br>material<br>particulado|Acopio de base chancada ( Planta de Chancado)|Material particulado|
|Fugitivas de<br>material<br>particulado|Carguío de base chancada (Planta de Chancado)|Material particulado|
|Fugitivas de<br>material<br>particulado|Transporte interno de base chancada (Planta de Chancado)|Material particulado|
|Fugitivas de<br>material<br>particulado|Transporte de base chancada por camino interno hasta<br>Ruta 43 (Planta de Chancado)|Material particulado|
|Fugitivas de<br>material<br>particulado|Descarga de áridos asfalto (Planta de Asfalto)|Material particulado|
|Fugitivas de<br>material<br>particulado|Transporte de asfalto por camino interno hasta Ruta 43<br>(Planta de Asfalto)|Material particulado|
|Combustión<br>interna|Uso / funcionamiento de camiones y maquinaria (Pozo de<br>Áridos, Planta de Chancado y Planta de Asfalto)|Material particulado y<br>gases de combustión|
|Combustión<br>interna|Uso / funcionamiento de grupos electrógenos (Planta de<br>Chancado y Planta de Asfalto)|Material particulado y<br>gases de combustión|
|Combustión<br>externa<br>|Uso / funcionamiento de caldera y horno rotatorio (Planta<br>de Asfalto)<br>|Material particulado y<br>gases de combustión|

(*) Contaminantes:
a) Material particulado: Partículas totales en suspensión (PTS); material particulado respirable
(MP10); material particulado fino (MP2.5).
b) Gases de combustión: monóxido de carbono (CO); óxidos de azufre (SOx); y óxidos de
nitrógeno (NOx).
Fuente: Elaboración propia.

6.2 Emisiones Atmosféricas

El Cuadro 8 resume las emisiones máximas diarias (kg/día) de material particulado (PTS,
MP10 y MP2.5) y gases de combustión (CO, SOx y NOx), estimadas para las fuentes
fugitivas y de combustión (interna y externa) de la etapa de operación del Proyecto.

Como se podrá observar en dicho cuadro, las emisiones más importantes (valores
absolutos), referidos al período de máxima actividad en la etapa de operación (cuando se
encuentren operando el pozo de extracción y las instalaciones en forma simultánea),
corresponden a NOx (377,70 kg/día), CO (337,43 kg/día) y PTS (228,21 kg/día). Las

Sacyr Chile S.A 26 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

menores emisiones corresponde a MP2.5 (26,80 kg/día), SOx (75,11 kg/día) y MP10 (80,76
kg/día).

En cuando a la importancia relativa de las fuentes emisoras, las emisiones PTS, MP10 y
MP2.5 tienen su origen principalmente en las fuentes fugitivas de polvo. En el caso de las
emisiones PTS, el aporte de estas fuentes es del 89,5% y para MP10 es del 75,5%. Las
fuentes de combustión (interna y externa) son responsables de la diferencia. Por su parte,
las fuentes de combustión constituyen la principal fuente de las emisiones de MP2.5
(64,4%).

Respecto a los gases de combustión, las fuentes de combustión interna son responsables de
la mayoría de las emisiones de NOx (78,1%), mientras las fuentes de combustión externa
son las principales emisoras de SOx (87,0%) y CO (80,5%).

Sacyr Chile S.A 27 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

Cuadro 8: Resumen de emisiones atmosféricas de la etapa de operación del Proyecto.

|TIPO DE<br>EMISIONES|FUENTES DE EMISIÓN|EMISIONES DIARIAS (kg/día)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|TIPO DE<br>EMISIONES|FUENTES DE EMISIÓN|PTS|MP10|MP2.5|CO|SOx|NOx|
|Fugitivas de<br>material<br>particulado|Escarpe del terreno (Pozo de Áridos)|4,54|2,27|1,13||||
|Fugitivas de<br>material<br>particulado|Excavación del terreno - retiro de material no apto<br>(Pozo de Áridos)|14,38|2,71|0,38||||
|Fugitivas de<br>material<br>particulado|Extracción de áridos (Pozo de Áridos)|67,01|13,40|0,30||||
|Fugitivas de<br>material<br>particulado|Selección de áridos bajo 4” (Pozo de Áridos)|4,17|1,43|0,72||||
|Fugitivas de<br>material<br>particulado|Carguío de áridos (Pozo de Áridos)|12,32|5,83|1,83||||
|Fugitivas de<br>material<br>particulado|Transporte interno de áridos hasta Planta de<br>Chancado (Pozo de Áridos)|33,46|9,79|0,51||||
|Fugitivas de<br>material<br>particulado|Transporte externo de material integral y bajo 4” por<br>camino interno del Proyecto|15,08|5,57|0,84||||
|Fugitivas de<br>material<br>particulado|Subtotal Parcial|150,96|41,00|5,71||||
|Fugitivas de<br>material<br>particulado|Procesamiento y manejo de áridos (Planta de<br>Chancado)|1,56|0,56|0,09||||
|Fugitivas de<br>material<br>particulado|Acopio de base chancada (Planta de Chancado)|0,08|0,04|0,02||||
|Fugitivas de<br>material<br>particulado|Carguío de base chancada (Planta de Chancado)|12,32|5,83|1,83||||
|Fugitivas de<br>material<br>particulado|Transporte interno de base chancada a acopios<br>(Planta de Chancado)|12,87|3,77|0,19||||
|Fugitivas de<br>material<br>particulado|Transporte interno de base chancada a Planta de<br>Asfalto (Planta de Chancado)|6,15|1,8|0,09||||
|Fugitivas de<br>material<br>particulado|Transporte externo de base chancada por camino<br>interno del Proyecto (Planta de Chancado)|10,40|3,84|0,58||||
|Fugitivas de<br>material<br>particulado|Subtotal Parcial|43,38|15,84|2,80||||
|Fugitivas de<br>material<br>particulado|Descarga de áridos (Planta de Asfalto)|5,28|2,50|0,78||||
|Fugitivas de<br>material<br>particulado|Transporte de asfalto por camino interno del<br>Proyecto (Planta de Asfalto)|4,52|1,67|0,25||||

Sacyr Chile S.A 28 Eco Master

Modelación de Emisiones Atmosféricas
Proyecto Extracción de Áridos e Instalaciones Asociadas
Pozo El Manzano
Para Mejoramiento y Conservación de la Ruta 43 de la Región de Coquimbo

|TIPO DE<br>EMISIONES|FUENTES DE EMISIÓN|EMISIONES DIARIAS (kg/día)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|TIPO DE<br>EMISIONES|FUENTES DE EMISIÓN|PTS|MP10|MP2.5|CO|SOx|NOx|
|TIPO DE<br>EMISIONES|Subtotal Parcial|9,80|4,17|1,03||||
|Subtotal|Subtotal|204,14|61,01|9,54||||
|Combustión<br>interna|Uso / funcionamiento de camiones, maquinaria y<br>equipos (Pozo de Áridos)|8,64|8,64|8,64|27,34|3,12|121,56|
|Combustión<br>interna|Uso / funcionamiento de camiones, maquinaria y<br>equipos (Planta de Chancado)|8,57|7,06|5,91|26,86|3,86|120,99|
|Combustión<br>interna|Uso / funcionamiento de camiones, maquinaria y<br>equipos (Planta de Asfalto)|3,68|1,92|0,58|11,56|2,80|52,28|
|Subtotal|Subtotal|20,89|17,62|15,13|65,76|9,78|294,82|
|Combustión<br>externa|Uso / funcionamiento de caldera y horno rotatorio<br>(Planta de Asfalto)|3,18|2,13|2,13|271,67|65,33|82,87|
|Subtotal|Subtotal|3,18|2,13|2,13|271,67|65,33|82,87|
|TOTAL EMISIONES PROYECTO|TOTAL EMISIONES PROYECTO|228,21|80,76|26,80|337,43|75,11|377,70|

Fuente: Elaboración propia.

Sacyr Chile S.A 29 Eco Master

La estimación de emisiones representada en el cuadro anterior se refiere al escenario
cuando operan simultáneamente el pozo de áridos, la planta de chancado, la planta de
asfalto, incluyendo el manejo de los acopios y transporte de materiales dentro área del
Proyecto. Consecuente con lo antes expuesto, el escenario de modelación seleccionado
corresponde a la peor condición desde el punto de las emisiones del Proyecto.

7.0 MODELACIÓN DE CALIDAD DEL AIRE

7.1 Modelo de Dispersión Utilizado y Datos de Entrada

El modelo utilizado para modelar las emisiones atmosféricas generadas por el Proyecto,
corresponde al denominado AERMOD, de tipo Gaussiano, desarrollado por la Agencia de
Protección Ambiental (EPA) de los E.E.U.U. para simular emisiones provenientes de
complejos industriales ubicados en terreno complejo. El modelo AERMOD es aplicable a
plumas de contaminantes industriales transportadas a través de distancias cortas (hasta 50
km).

AERMOD simula el transporte y la dispersión atmosférica de contaminantes emitidos desde
fuentes puntuales múltiples, de área o volumétricas. Se basa en la caracterización de la capa
límite atmosférica, utilizando para ello los datos medidos de algunas variables
meteorológicas convencionales. Las fuentes de emisión pueden estar ubicadas en áreas
rurales o urbanas, y los receptores pueden estar localizados en terreno simple o complejo. El
modelo AERMOD tiene en cuenta los efectos de la estela turbulenta en el aire originada por
los edificios (remoción en la pluma de contaminantes), utilizando los algoritmos incluidos en
el Plume Rise Model Enhancements (PRIME).

El modelo AERMOD utiliza datos meteorológicos horarios procesados secuencialmente con el
objetivo de calcular las concentraciones de contaminantes en aire para diferentes tiempos de
promedio desde una hora hasta un año.

El modelo está diseñado para operar con dos pre-procesadores:

- De datos meteorológicos (ARMET); y

- De información del terreno (AERMAP).

El pre-procesador AERMET requiere como entrada al menos 2 archivos de información
meteorológica y preferentemente de 3 archivos. Los primeros dos archivos corresponden a
información meteorológica de superficie y de altura. El tercer archivo corresponde a
información meteorológica local (site specific or on site). En este caso particular se contó
con información local proveniente de la estación meteorológica Las Cardas para el año 2013.
Es estación pertenece a la red de estaciones de red de estaciones CEAZA-Met, administradas
por el Centro de Estudios Avanzados en Zonas Áridas (CEAZA).

En Chile, la información de los datos para preparar los dos primeros archivos meteorológicos
(superficie y de altura) es muchas veces escasa o inexistente, por lo que es necesario
levantar esta información para seguir las recomendaciones de la Guía para el Uso de
Modelos de Calidad del Aire en el SEIA. Los dos primeros archivos meteorológicos, de
superficie y de altura se obtuvieron de los archivos de salida del modelo de meso-escala de
quinta generación MM5 con una resolución de 12x 12 km para el año 2013.

Sacyr Chile S.A 30 Eco Master

La meteorología utilizada en la modelación corresponde a la generada por el modelo
meteorológico MM5. Este modelo es recomendado por la EPA de los E.E.U.U. para generar la
meteorología requerida como entrada en modelos de dispersión tales como AERMOD y otros.
La información generada es referente al entorno del Proyecto y corresponde al período
comprendido entre el 01 de Enero y el 31 de Diciembre del año 2013 (se escogió este
período para mantener la consistencia temporal con la información meteorológica de
superficie obtenida de la Estación Las Cardas). En Anexo A se adjunta la información
meteorológica MM5 adquirida para la modelación.

El otro pre-procesador es el AERMAP, que genera un archivo de salida, el cual se copia en el
archivo principal de AERMOD y contiene las cotas de las fuentes como de los receptores que
se hayan definido en el modelo.

La información topográfica se obtuvo del archivo SRTM-V2 “S31W72.hgt” (The Shuttle Radar
Topography Mission) de la NASA que posee una resolución espacial aproximada de 90 x 90
metros. La definición de los receptores se fijó para este caso como una grilla polar con un
espaciamiento angular de 10 grados sexagesimales (36 datos por anillo) y con los siguientes
radios medidos desde el punto V1 (coordenadas UTM, según Datum WGS-84, Huso 19 S:
287.645,0 Este y 6.662.095,0 Norte): 100, 200, 300, 500, 750, 1.000, 1.500, 2.000, 2.500,
3.000, 3.500, 4.000, 4.500 y 5.000 metros, resultando un total de 504 receptores en torno
al área del Proyecto.

En el Anexo B se adjuntan los archivos de entrada (input) y salida (output) de la
modelación con AERMOD.

El modelo AERMOD posee las siguientes características:

- Cuenta con documentación completa sobre sus fundamentos conceptuales,
ecuaciones matemáticas, y los tipos de datos de entrada y de salida junto con sus
respectivos formatos;

- Se encuentra escrito en un lenguaje de programación común y con un código abierto;

- Es de acceso libre (es posible bajarlos directamente del sitio web de la EPA;
www.epa.gov.com);

- Dispone de documentación sobre su evaluación, en forma de informes técnicos,
publicaciones científicas, etc.;

- Cuenta con desarrollo y soporte técnico actualizado de parte de su comunidad de
usuarios o desarrolladores.

Para modelar las emisiones atmosféricas del Proyecto, los aspectos o factores considerados
en la selección del modelo AERMOD, fueron los siguientes:

- Terreno elevado; la zona donde se emplaza el Proyecto corresponde a un área
relativamente plana, elevada, con presencia de cerros al norte y al sur del área del
Proyecto (por esta razón se utilizó AERMOD con pre-procesamiento mediante el
modelo AERMAP con un modelo digital de terreno (DTM) compatible con el formato
DEM del USGS).

- Contaminantes a modelar; todos los contaminantes a modelar (PTS, MP10, MP2.5,
SO 2, NO 2 y CO), son considerados primarios.

- Meteorología homogénea; por su topografía, se esperaría que el área del Proyecto
posea una meteorología relativamente homogénea.

Sacyr Chile S.A 31 Eco Master

Corresponde indicar que los modelos Gaussianos corresponden a los modelos estacionarios
basados en la conocida “ecuación de Gauss”, representada de la siguiente manera:

Donde:

c : Concentración del contaminante modelado.
u : Velocidad del viento a la altura de la emisión.
Q : Emisión unitaria.
σy : Coeficiente de dispersión horizontal.
σz : Coeficiente de dispersión vertical.
H : Altura efectiva de la emisión.
y : Coordenada horizontal, en la dirección del viento.
z: Coordenada vertical.

Con respecto a la estabilidad atmosférica, corresponde indicar que el método de PasquillGuiford es el más utilizado para caracterizar este parámetro. Este método clasifica la
atmósfera en 6 clases, a saber:

- Clase A: Atmósfera muy inestable;

- Clase B: Atmósfera inestable;

- Clase C: Atmósfera ligeramente inestable;

- Clase D: Atmósfera neutra;

- Clase E: Atmósfera ligeramente estable;

- Clase F: Atmósfera estable.

7.2 Área de Modelación

Para modelar las emisiones atmosféricas del Proyecto, se definió un área de modelación
correspondiente a una superficie de aproximadamente 10 km x 10 km, en cuyo interior se
encuentra localizado el Proyecto, y que abarca la zona donde se encuentra el límite de las
comunas de Andacollo y Coquimbo.

El Cuadro 9 indica las coordenadas UTM aproximadas de los vértices del área de modelación
de las emisiones del Proyecto.

Cuadro 9: Área de modelación en las comunas de Andacollo y Coquimbo.

|Vértices|Coordenadas UTM (aproximadas)<br>(Datum WGS-84, Huso 19S)|Col3|
|---|---|---|
|Vértices|Este|Norte|
|Noroeste|292.645|6.667.095|
|Noreste|302.645|6.667.095|
|Sureste|302.645|6.657.095|
|Suroeste|292.645|6.657.095|

Fuente: Elaboración propia.

Sacyr Chile S.A 32 Eco Master

La Figura 12 ilustra el área de modelación de las emisiones del Proyecto, representada sobre
mapa topográfico que abarca parte de las comunas de Andacollo y Coquimbo.

Figura 12: Área de modelación del Proyecto.

Fuente: Elaboración propia sobre plano topográfico obtenido de The Shuttle Radar Topography Mission (archivo
SRTM-V2 “S31W72.hgt”), de la NASA de los E.E.U.U.

Por otra parte, la Figura 13 ilustra el área de modelación de las emisiones del Proyecto,
representada en Google Earth.

Sacyr Chile S.A 33 Eco Master

Figura 13: Área de modelación del Proyecto (en Google Earth).

Fuente: Elaboración propia sobre base Google Earth.

7.3 Resultados Obtenidos

7.3.1 Puntos de Máximo Impacto

Las salidas (output) del modelo AERMOD corresponden a concentraciones máximas horarias,
diarias y anuales de MP10, MP2.5, CO, SO 2 y NO 2, estimadas para los 365 días del año
modelado, expresadas en microgramos por metro cúbico de aire en condiciones normales
(μg/m [3] N). También entrega las concentraciones promedio anuales de MPS, en este caso,
expresadas como gramos por metro cuadrado al año (g/m [2] /año).

El Cuadro 10 indica las coordenadas UTM de los puntos de máximo impacto de las emisiones
del Proyecto.

Sacyr Chile S.A 34 Eco Master

Cuadro 10: Ubicación de puntos de máximo impacto del Proyecto.

|Contaminantes|Parámetros|Coordenadas UTM aproximadas<br>(Datum WGS-84, Huso 19S)|Col4|
|---|---|---|---|
|Contaminantes|Parámetros|Este|Norte|
|MP10|Concentración máxima diaria|287.904,8|6.661.945,0|
|MP10|Promedio máximo anual|287.662,4|6.661.996,5|
|MP2.5|Concentración máxima diaria|287.904,8|6.661.945,0|
|MP2.5|Promedio máximo anual|287.662,4|6.661.996,5|
|MPS|Promedio máximo anual|288.411,0|6.661.452,2|
|CO|Concentración máxima 1 hora|287.743,5|6.662.112,4|
|CO|Concentración máxima 8 hora|287.713,5|6.662.112,4|
|SO2|Concentración máxima 1 hora|287.679,2|6.662.189,0|
|SO2|Concentración máxima diaria|287.709,3|6.662.018,4|
|SO2|Promedio máximo anual|287.662,4|6.661.996,5|
|NO2|Concentración máxima 1 hora|287.743,5|6.662.112,4|
|NO2|Promedio máximo anual|287.662,4|6.661.996,5|

Fuente: Elaboración propia.

Por su parte, el Cuadro 11 indica el aporte del Proyecto en los puntos de máximo impacto
identificados anteriormente, y la comparación con las respectivas normas de calidad del aire
aplicables.

Cuadro 11: Aporte del Proyecto en los puntos de máximo impacto.

|Contaminantes|Parámetros|Aporte del<br>Proyecto|Valor de la<br>Norma Primaria<br>(Secundaria)|
|---|---|---|---|
|MP10|Concentración máxima diaria|105,8 ug/m3N|150 ug/m3N|
|MP10|Promedio máximo anual|11,8 ug/m3N|50 ug/m3N|
|MP2.5|Concentración máxima diaria|57,9 ug/m3N|50 ug/m3N|
|MP2.5|Promedio máximo anual|7,7 ug/m3N|20 ug/m3N|
|MPS|Promedio máximo anual|221,4 mg/m2/día|200 mg/m2/día|
|CO|Concentración máxima 1 hora|91.861 ug/m3N|30.000 ug/m3N|
|CO|Concentración máxima 8 hora|11.482 ug/m3N|10.000 ug/m3N|
|SO2|Concentración máxima 1 hora|15.417 ug/m3N|(700 ug/m3N)|
|SO2|Concentración máxima diaria|676,7 ug/m3N|250 ug/m3N <br>(260 ug/m3N)|
|SO2|Promedio máximo anual|152,6 ug/m3N|80 ug/m3N <br>(60 ug/m3N)|
|NO2|Concentración máxima 1 hora|46.213 ug/m3N|400 ug/m3N|
|NO2|Promedio máximo anual|301 ug/m3N|100 ug/m3N|

Fuente: Elaboración propia.

7.3.2 Curvas de Isoconcentraciones

Los resultados obtenidos de la modelación para cada contaminante fueron representados
gráficamente sobre el mapa topográfico antes presentado (Figura 12).

Sacyr Chile S.A 35 Eco Master

A continuación se entregan los resultados de la modelación (incluyendo los puntos de
máximo impacto analizados en el punto 7.3.1) y la comparación con las respectivas normas
o valores de referencia existentes para cada contaminante.

a) Concentraciones Diarias de MP10

La Figura 14 ilustra gráficamente las concentraciones máximas diarias de MP10 obtenidas de
la modelación.

En general, las concentraciones máximas diarias de MP10 se encuentran en el rango 10 - 20
μg/m [3] N en los alrededores del área del Proyecto. Todas las concentraciones son inferiores al
valor que señala la norma primaria diaria para MP10; 150 μg/m [3] N (Decreto Supremo
No59/98 del Ministerio de Salud), exceptuando en punto de máximo impacto (105,8
μg/m [3] N), pero éste se encuentra dentro del área del Proyecto.

Figura 14: Curvas Isoconcentraciones de MP10 - valores máximos diarios
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 36 Eco Master

b) Concentraciones Anuales de MP10

La Figura 15 ilustra gráficamente las concentraciones promedio anuales de MP10 obtenidas
de la modelación.

En general, las concentraciones anuales de MP10 se encuentran en el rango 0,5 - 1,5
μg/m [3] N en los alrededores del área del Proyecto. Todas las concentraciones son muy
inferiores al valor que señala la norma primaria anual para MP10; 50 μg/m [3] N (Decreto
Supremo No59/98 del Ministerio de Salud, incluyendo modificación introducida a través de
Decreto Supremo No45/01 del mismo ministerio), exceptuando en el punto de máximo
impacto (11,8 μg/m [3] N), pero éste se encuentra dentro del área del Proyecto.

Figura 15: Curvas Isoconcentraciones de MP10 - valores promedio anuales
(concentraciones en μg/m [3] N).

Fuente: Elaboración propia.

Sacyr Chile S.A 37 Eco Master

c) Concentraciones Diarias de MP2.5

La Figura 16 ilustra gráficamente las concentraciones máximas diarias de MP2.5 obtenidas
de la modelación.

En general, las concentraciones máximas diarias de MP2.5 se encuentran en el rango 2,5 - 5
μg/m [3] N en los alrededores del área del Proyecto. Todas concentraciones son inferiores al
valor que señala la norma primaria diaria para MP2.5; 50 μg/m [3] (Decreto Supremo No12/11
del Ministerio del Medio Ambiente), excepto en el punto de máximo impacto (57,9 μg/m [3] N),
pero éste se encuentra dentro del área del Proyecto.

Figura 16: Curvas Isoconcentraciones de MP2.5 - valores máximos diarios
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 38 Eco Master

d) Concentraciones Anuales de MP2.5

La Figura 17 ilustra gráficamente las concentraciones promedio anuales de MP2.5 obtenidas
de la modelación.

En general, las concentraciones anuales de MP2.5 se encuentran en el rango 0,5 - 1,5
μg/m [3] en los alrededores del área del Proyecto. Todas las concentraciones son muy
inferiores al valor que señala la norma primaria anual para MP2.5; 20 μg/m [3] (Decreto
Supremo No12/11 del Ministerio del Medio Ambiente), exceptuando en el punto de máximo
impacto (7,7 μg/m [3] N), pero éste se encuentra dentro del área del Proyecto.

Figura 17: Curvas Isoconcentraciones de MP2.5 - valores promedio anuales
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 39 Eco Master

e) Concentraciones Anuales de MPS

La Figura 18 ilustra gráficamente las concentraciones anuales de MPS obtenidas de la
modelación.

En general, las concentraciones (depositación acumulada) anuales de MPS se encuentran en
el rango 2,5 - 5 g/m [2] /año (equivalente a 6,8 - 13,7 mg/m [2] /día) en los alrededores del área
del Proyecto. Todas las concentraciones son inferiores al valor anual para MPS que establece
la Confederación Suiza [5] ; 200 mg/m [2] /día, excepto en el punto de máximo impacto (80,8
g/m [2] /año ó 221,4 mg/m [2] /día), pero éste se encuentra dentro del área del Proyecto.

Figura 18: Curvas Isoconcentraciones de MPS - valores promedio anuales
(concentraciones en g/m [2] /año)

Fuente: Elaboración propia.

5 Según el artículo 11 del Reglamento del SEIA (Decreto Supremo N°40/2012 del Ministerio del Medio Ambiente),
ante la ausencia de normas nacionales, se pueden utilizar las normas, entre otras, de la Confederación Suiza
como valores de referencia para efectos de evaluar efectos o riegos en calidad del aire.

Sacyr Chile S.A 40 Eco Master

f) Concentraciones Horarias de CO

La Figura 19 ilustra gráficamente las concentraciones máximas horarias de CO obtenidas de
la modelación.

En general, las concentraciones máximas horarias de CO se encuentran en el rango 2.50010.000 μg/m [3] N en los alrededores del área del Proyecto. Todas las concentraciones son
inferiores al valor establecido por la norma primaria horaria para CO; 30.000 μg/m [3] N ó 30
mg/m [3] N (Decreto Supremo No115/02 del Ministerio Secretaría General de la Presidencia),
excepto en el punto de máximo impacto (91.861 μg/m [3] N), pero éste se encuentra dentro del
área del Proyecto.

Figura 19: Curvas Isoconcentraciones de CO- valores máximos horarios
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 41 Eco Master

g) Concentraciones Promedio 8 horas de CO

La Figura 20 ilustra gráficamente las concentraciones máximas de CO para períodos de 8
horas, obtenidas de la modelación.

En general, las concentraciones máximas de 8 horas de CO se encuentran en el rango 2502.000 μg/m [3] N en los alrededores del área del Proyecto. Todas las concentraciones son
inferiores al que señala la norma primaria para 8 horas de CO; 10.000 μg/m [3] N ó 10 mg/m [3] N
(Decreto Supremo No115/02 del Ministerio Secretaría General de la Presidencia),
exceptuando en el punto de máximo impacto (11.482 μg/m [3] N), pero éste se encuentra
dentro del área del Proyecto.

Figura 20: Curvas Isoconcentraciones de CO- valores máximos 8 horas
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 42 Eco Master

h) Concentraciones Horarias de SO 2

La Figura 21 ilustra gráficamente las concentraciones máximas horarias de SO 2 obtenidas de
la modelación.

En general, las concentraciones máximas horarias de SO 2 se encuentran en el rango 100250 μg/m [3] N en los alrededores del área del Proyecto. Todas las concentraciones son muy
inferiores al valor que señala la norma secundaria horaria para SO 2 ; 700 μg/m [3] N (Decreto
Supremo No22/10 del Ministerio Secretaría General de la Presidencia), exceptuando en el
punto de máximo impacto (15,417 μg/m [3] N), pero éste se encuentra dentro del área del
Proyecto.

Figura 21: Curvas Isoconcentraciones de SO 2 - valores máximos horarios
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 43 Eco Master

i) Concentraciones Diarias de SO 2

La Figura 22 ilustra gráficamente las concentraciones máximas diarias de SO 2 obtenidas de
la modelación.

En general, las concentraciones máximas diarias de SO 2 se encuentran en el rango 10-25
μg/m [3] N en los alrededores del área del Proyecto. Todos los valores son muy inferiores al que
señalan las normas primaria y secundaria diarias para SO 2 ; 250 y 260 μg/m [3] N (Decretos
Supremo No113/02 y N°22/10 del Ministerio Secretaría General de la Presidencia,
respectivamente), exceptuando en el punto de máximo impacto (676,7 μg/m [3] N), pero éste
se encuentra dentro del área del Proyecto.

Figura 22: Curvas Isoconcentraciones de SO 2 - valores máximos diarios
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 44 Eco Master

j) Concentraciones Anuales de SO 2

La Figura 23 ilustra gráficamente las concentraciones máximas anuales de SO 2 obtenidas de
la modelación.

En general, las concentraciones anuales de SO 2 se encuentran en el rango 1 - 1,5 μg/m [3] N
en los alrededores del área del Proyecto. Todas las concentraciones son inferiores al valor
que señalan las normas primaria y secundaria anuales para SO 2 ; 80 y 60 μg/m [3] N (Decretos
Supremo No113/02 N°22/10 del Ministerio Secretaría General de la Presidencia,
respectivamente), exceptuando en el punto de máximo impacto (152,6 μg/m [3] N), pero éste
se encuentra en el área del Proyecto.

Figura 23: Curvas Isoconcentraciones de SO 2 - valores promedio anuales
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 45 Eco Master

k) Concentraciones Horarias de NO 2

La Figura 24 ilustra gráficamente las concentraciones máximas horarias de NO 2 obtenidas de
la modelación.

En general, las concentraciones máximas horarias de NO 2 se encuentran en el rango 1.500
Supremo No114/02 del Ministerio Secretaría General de la Presidencia).

Figura 24: Curvas Isoconcentraciones de NO 2 - valores máximos horarios
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 46 Eco Master

l) Concentraciones Anuales de NO 2

La Figura 25 ilustra gráficamente las concentraciones máximas anuales de NO 2 obtenidas de
la modelación.

En general, las concentraciones anuales de NO 2 se encuentran en el rango 1 - 2,5 μg/m [3] N
en los alrededores del área del Proyecto. Todas las concentraciones son muy inferiores al
valor que señala la norma primaria anual para NO 2 ; 100 μg/m [3] N (Decreto Supremo
No114/02 del Ministerio Secretaría General de la Presidencia), exceptuando en el punto de
máximo impacto (301 μg/m [3] N), pero éste se encuentra dentro del área del Proyecto.

Figura 25: Curvas Isoconcentraciones de NO 2 - valores promedio anuales
(concentraciones en μg/m [3] N)

Fuente: Elaboración propia.

Sacyr Chile S.A 47 Eco Master

7.3.3 Cumplimiento de la Normativa sobre Material Particulado

Como se indica anteriormente, en el área de emplazamiento del Proyecto, no existe registro
histórico de las concentraciones de MP10, MP2.5 y MPS. Por esta razón, y de manera
exclusivamente referencial, se ha considerado los datos de calidad del aire para MP10 y
MP2.5 registrados en las Estaciones Andacollo, Coquimbo y La Serena, todas pertenecientes
a la red de calidad del aire del SINCA, localizadas en las comunas de Andacollo, Coquimbo y
La Serena, respectivamente, como una línea base tentativa para el área del Proyecto.

A continuación se analiza el eventual cumplimiento de la normativa primaria sobre calidad
del aire, en este caso considerando la información de línea base obtenida de las referidas
estaciones de monitoreo. Para ello se han considerado las concentraciones diarias y anuales
de MP10 y MP2.5 indicadas anteriormente en el punto 7.3.1 (Cuadro 11) y los datos
referenciales de calidad del aire registrados en dichas estaciones y que son entregados en el
punto 4.2 del presente informe.

En el caso de MPS, se ha asumido que la concentración anual de MPS podría alcanzar
valores similares a los registrados en localidades localizadas en el centro y norte del país.

a) Material Particulado Respirable (MP10)

El Cuadro 12 evalúa tentativamente el cumplimiento de la normativa primaria diaria y anual
para MP10 en el punto de máximo impacto del Proyecto, considerando como referencia la
información de calidad del aire de la Estación Andacollo.

Cuadro 12: Evaluación del cumplimiento de normativa (primaria) sobre MP10 en
el punto de máximo impacto del Proyecto.

|Parámetros|Concentraciones MP10 (μg/m3N)|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 98<br>(valores diarios)|
|Línea base (supuesto)(1)|64,0|121,0|
|Aporte máximo del Proyecto(2)|11,8|105,8|
|Valores según normativa(3)|50,0|150,0|

Notas:
(1) Considerando rango de concentraciones registradas en la Estación Andacollo.
(2) Concentraciones estimadas en punto de máximo impacto (ver Cuadro 11 del presente informe).
(3) Decreto Supremo No59/98 del Ministerio de Salud (incluye modificación introducida por Decreto Supremo
No45/01 del mismo ministerio).
Fuente: Elaboración propia.

b) Material Particulado Fino (MP2.5)

El Cuadro 13 evalúa tentativamente el cumplimiento de la normativa primaria diaria y anual
para MP2.5 en el punto de máximo impacto del Proyecto, considerando como referencia la
información de calidad del aire de la Estaciones Coquimbo y La Serena.

Sacyr Chile S.A 48 Eco Master

Cuadro 13: Evaluación del cumplimiento de normativa (primaria) sobre MP2.5 en
el punto de máximo impacto del Proyecto.

|Parámetros|Concentraciones MP2.5 (μg/m3N)|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 98<br>(valores diarios)|
|Línea base (supuesto)(1)|13,9|17,5|
|Aporte máximo del Proyecto(2)|7,7|221,4|
|Valores según normativa(3)|20,0|50,0|

Notas:
(1) Considerando rango de concentraciones registradas en las Estaciones Coquimbo y La Serena.
(2) Concentraciones estimadas en punto de máximo impacto (ver Cuadro 11 del presente informe).
(3) Decreto Supremo N°12/11 del Ministerio del Medio Ambiente.
Fuente: Elaboración propia.

c) Material Particulado o Polvo Sedimentable (MPS)

Según antecedentes obtenidos, las concentraciones anuales de MPS podrían encontrarse en
el rango entre 40 y 80 mg/m [2] /día.

En cuanto a normativa, en Chile no existe normativa para MPS. Por esta razón, se puede
considerar como referencia la norma anual establecida por la Confederación Suiza; 200
mg/m [2] /día.

El Cuadro 14 evalúa el cumplimiento del valor de referencia anual para MPS, en el punto de
máximo impacto del Proyecto.

Cuadro 14: Evaluación del cumplimiento de normativa sobre MPS en el punto de
máximo impacto del Proyecto.

|Parámetros|Concentraciones MP10<br>(mg/m2/día)|
|---|---|
|Parámetros|Promedio Anual|
|Línea base (supuesto)(1)|40,0 - 80,0|
|Aporte máximo del Proyecto(2)|221,4|
|Valores según normativa(3)|200,0|

Notas:
(1) Considerando rango de concentraciones registradas en zonas centro y norte del país.
(2) Concentraciones estimadas en punto de máximo impacto (ver Cuadro 11 del presente informe).
(3) Valor de referencia propuesto por la Confederación Suiza.
Fuente: Elaboración propia.

7.3.4 Cumplimiento de la Normativa sobre Gases

Como se indica anteriormente, en comuna de Andacollo y específicamente en el área de
emplazamiento del Proyecto, no existe monitoreo o registro histórico de CO, SO 2 y NO 2 . Por
esta razón, y de manera exclusivamente referencial, se han considerado los datos de calidad
del aire para estos gases registrados en las estaciones de la red SINCA en la zona centro-sur
del país, como una línea base tentativa para CO, SO ~~2~~ y NO ~~2~~, respectivamente, en el área del
Proyecto.

A continuación se analiza el eventual cumplimiento de la normativa primaria sobre calidad
del aire en el punto de máximo impacto del Proyecto, en este caso considerando las
concentraciones máximas de CO, SO 2 y NO 2, indicadas anteriormente en el punto 7.3.1

Sacyr Chile S.A 49 Eco Master

(Cuadro 11) y los datos referenciales de calidad del aire registrados en dichas estaciones y
que son entregados en el punto 4.2 del presente informe.

a) Monóxido de Carbono (CO)

El Cuadro 15 evalúa tentativamente el cumplimiento de la normativa primaria de 1 hora y 9
horas para CO en el punto de máximo impacto del Proyecto, considerando como referencia
la información disponible en el sitio web del SINCA para otras ciudades del país.

Cuadro 15: Evaluación del cumplimiento de normativa (primaria) sobre CO en el
punto de máximo impacto del Proyecto.

|Parámetros|Concentraciones CO (μg/m3N)|Col3|
|---|---|---|
|Parámetros|Percentil 99<br>(datos 1 hora)|Percentil 99<br>(datos 8 horas)|
|Línea base (supuesto)(1)|11.540-23.080 (10-20 ppm)|3.333-5.555 (3-5 ppm)|
|Aporte máximo del Proyecto(2)|91.861|11.482|
|Valores según normativa(3)|30.000 (26 ppm)|10.000 (9 ppm)|

Notas:
(1) Considerando información disponible en el sitio web del SINCA para otras ciudades del país.
(2) Concentraciones estimadas en punto de máximo impacto (ver Cuadro 11 del presente informe).
(3) Decretos Supremo N°115/02 del Ministerio Secretaría General de la Presidencia.
Fuente: Elaboración propia.

b) Dióxido de Azufre (SO 2 )

El Cuadro 16 evalúa tentativamente el cumplimiento de la normativa primaria diaria y anual
para SO 2 en el punto de máximo impacto del Proyecto, considerando como referencia la
información disponible en el sitio web del SINCA para otras ciudades del país.

Cuadro 16: Evaluación del cumplimiento de normativa (primaria) sobre SO 2 en el
punto de máximo impacto del Proyecto.

|Parámetros|Concentraciones SO (μg/m3N)<br>2|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 99<br>(valores diarios)|
|Línea base (supuesto)(1)|3,0 - 5,0|20,0|
|Aporte máximo del Proyecto(2)|152,6|676,7|
|Valores según normativa(3)|80,0 (31 ppb)|250,0 (96 ppb)|

Notas:
(1) Considerando información disponible en el sitio web del SINCA para otras ciudades del país.
(2) Concentraciones estimadas en punto de máximo impacto (ver Cuadro 11 del presente informe).
(3) Decretos Supremo N°113/02 del Ministerio Secretaría General de la Presidencia.
Fuente: Elaboración propia.

c) Dióxido de Nitrógeno (NO 2 )

El Cuadro 17 evalúa tentativamente el cumplimiento de la normativa primaria horaria y
anual para NO 2 en el punto de máximo impacto del Proyecto, considerando como referencia
la información disponible en el sitio web del SINCA para otras ciudades del país.

Sacyr Chile S.A 50 Eco Master

Cuadro 17: Evaluación del cumplimiento de normativa (primaria) sobre NO 2 en el
punto de máximo impacto del Proyecto.

|Parámetros|Concentraciones NO (μg/m3N)<br>2|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 99<br> <br> (valores diarios)|
|Línea base (supuesto)(1)|9,4 - 37,7 (5-20 ppb)|94 - 282 (50-150 ppb)|
|Aporte máximo del Proyecto(2)|301,0|46.213|
|Valores según normativa(3)|100,0 (53 ppb)|400,0 (213 ppb)|

Notas:
(1) Considerando información disponible en el sitio web del SINCA para otras ciudades del país.
(2) Concentraciones estimadas en punto de máximo impacto (ver Cuadro 11 del presente informe).
(3) Decretos Supremo N°114/02 del Ministerio Secretaría General de la Presidencia.
Fuente: Elaboración propia.

7.3.5 Impacto Sobre Receptores Más Cercanos

Dentro del área de influencia del proyecto, se identificó las viviendas más cercanas que
pudieran ser afectadas por las emisiones del Proyecto.

El Cuadro 18 identifica estas viviendas y entrega las coordenadas UTM de cada una de ellas.

Cuadro 18: Localización de viviendas más próximas al área del Proyecto.

|Punto|Descripción|Coordenadas UTM<br>(Datum WGS 84, Huso H 19S)|Col4|
|---|---|---|---|
|Punto|Descripción|Este|Norte|
|A1|Vivienda ubicada al oriente del Proyecto y<br>al norte de la Ruta D-51.|287.961|6.662.565|
|B1|Vivienda ubicada al norponiente del<br>Proyecto.|286.925|6.662.367|
|C1|Vivienda ubicada al oriente del Proyecto y<br>al sur de la Ruta D-51|289.324|6.662.176|
|A2|Vivienda ubicada al suroriente del Proyecto<br>y al poniente de la Ruta D-323.|288.877|6.661.247|
|B2|Vivienda ubicada norte del Proyecto.|288.462|6.661.204|

Fuente: Basado en estudio de ruido del Proyecto.

Por su parte, la Figura 26 ilustra la ubicación geográfica de las viviendas anteriores, dentro
del área de influencia del Proyecto.

Sacyr Chile S.A 51 Eco Master

Figura 26: Localización de viviendas más próximas al área del Proyecto.

Fuente: Basado en estudio de ruido del Proyecto.

A continuación se evalúa el cumplimiento de la normativa en cada uno de los receptores sensibles antes indicados
(A1, B1, C1, A2 y B2).

a) Material Particulado Respirable (MP10)

El Cuadro 19 evalúa tentativamente el cumplimiento de la normativa primaria diaria y anual
para MP10 en los receptores sensibles antes indicados (Cuadro 17), considerando como
referencia la información de calidad del aire de la Estación Andacollo.

Cuadro 19: Evaluación del cumplimiento de normativa (primaria) sobre MP10 en
los Receptores Sensibles del Proyecto.

|Parámetros|Concentraciones MP10 (μg/m3N)|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 98<br>(valores diarios)|
|Línea base (supuesto)(1)|64,0|121,0|
|Aporte en Receptor A1(2)|0,1|2,4|
|Aporte en Receptor B1(2)|0,3|1,8|
|Aporte en Receptor C1(2)|0,04|0,8|
|Aporte en Receptor A2(2)|2,5|8,5|
|Aporte en Receptor B2(2)|4,5|16,5|
|Valores según normativa(3)|50,0|150,0|

Notas:
(4) Considerando rango de concentraciones registradas en la Estación Andacollo.
(5) Concentraciones estimadas (ver Cuadro 18 del presente informe).
(6) Decreto Supremo No59/98 del Ministerio de Salud (incluye modificación introducida por Decreto Supremo
No45/01 del mismo ministerio).
Fuente: Elaboración propia.

Sacyr Chile S.A 52 Eco Master

b) Material Particulado Fino (MP2.5)

El Cuadro 20 evalúa tentativamente el cumplimiento de la normativa primaria diaria y anual
para MP2.5 en los receptores sensibles antes indicados (Cuadro 17), considerando como
referencia la información de calidad del aire de la Estaciones Coquimbo y La Serena.

Cuadro 20: Evaluación del cumplimiento de normativa (primaria) sobre MP2.5 en
los Receptores Sensibles del Proyecto.

|Parámetros|Concentraciones MP2.5 (μg/m3N)|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 98<br>(valores diarios)|
|Línea base (supuesto)(1)|13,9|17,5|
|Aporte en Receptor A1(2)|0,12|2,32|
|Aporte en Receptor B1(2)|0,12|0,98|
|Aporte en Receptor C1(2)|0,02|0,39|
|Aporte en Receptor A2(2)|0,91|3,28|
|Aporte en Receptor B2(2)|1,75|7,25|
|Valores según normativa(3)|20,0|50,0|

Notas:
(4) Considerando rango de concentraciones registradas en las Estaciones Coquimbo y La Serena.
(5) Concentraciones estimadas (ver Cuadro 18 del presente informe).
(6) Decreto Supremo N°12/11 del Ministerio del Medio Ambiente.
Fuente: Elaboración propia.

c) Material Particulado o Polvo Sedimentable (MPS)

El Cuadro 21 evalúa el cumplimiento del valor de referencia anual para MPS, en el Receptor
C1 del Proyecto.

Cuadro 21: Evaluación del cumplimiento de normativa sobre MPS en los
Receptores Sensibles del Proyecto.

|Parámetros|Concentraciones MP10<br>(mg/m2/día)|
|---|---|
|Parámetros|Promedio Anual|
|Línea base (supuesto)(1)|40,0 - 80,0|
|Aporte en Receptor A1(2)|0,52|
|Aporte en Receptor B1(2)|4,1|
|Aporte en Receptor C1(2)|0,4|
|Aporte en Receptor A2(2)|73,0|
|Aporte en Receptor B2(2)|102,4|
|Valores según normativa(3)|200,0|

Notas:
(1) Considerando rango de concentraciones registradas en zonas centro y norte del país.
(2) Concentraciones estimadas (ver Cuadro 18 del presente informe).
(3) Valor de referencia propuesto por la Confederación Suiza.
Fuente: Elaboración propia.

d) Monóxido de Carbono (CO)

El Cuadro 22 evalúa tentativamente el cumplimiento de la normativa primaria de 1 hora y 9
horas para CO en los receptores sensibles antes indicados (Cuadro 17), considerando como
referencia la información disponible en el sitio web del SINCA para otras ciudades del país.

Sacyr Chile S.A 53 Eco Master

Cuadro 22: Evaluación del cumplimiento de normativa (primaria) sobre CO en los
Receptores Sensibles del Proyecto.

|Parámetros|Concentraciones CO (μg/m3N)|Col3|
|---|---|---|
|Parámetros|Percentil 99<br>(datos 1 hora)|Percentil 99<br>(datos 8 horas)|
|Línea base (supuesto)(1)|11.540-23.080 (10-20 ppm)|3.333-5.555 (3-5 ppm)|
|Aporte en Receptor A1(2)|2.141|289|
|Aporte en Receptor B1(2)|146|18|
|Aporte en Receptor C1(2)|162|21|
|Aporte en Receptor A2(2)|452|59|
|Aporte en Receptor B2(2)|667|95|
|Valores según normativa(3)|30.000 (26 ppm)|10.000 (9 ppm)|

Notas:
(1) Considerando información disponible en el sitio web del SINCA para otras ciudades del país.
(2) Concentraciones estimadas (ver Cuadro 18 del presente informe).
(3) Decretos Supremo N°115/02 del Ministerio Secretaría General de la Presidencia.
Fuente: Elaboración propia.

b) Dióxido de Azufre (SO 2 )

El Cuadro 23 evalúa tentativamente el cumplimiento de la normativa primaria diaria y anual
para SO 2 en los receptores sensibles antes indicados (Cuadro 17), considerando como
referencia la información disponible en el sitio web del SINCA para otras ciudades del país.

Cuadro 23: Evaluación del cumplimiento de normativa (primaria) sobre SO 2 en los
Receptores Sensibles del Proyecto.

|Parámetros|Concentraciones SO (μg/m3N)<br>2|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 99<br>(valores diarios)|
|Línea base (supuesto)(1)|3,0 - 5,0|20,0|
|Aporte en Receptor A1(2)|0,58|7,6|
|Aporte en Receptor B1(2)|0,11|0,9|
|Aporte en Receptor C1(2)|0,04|0,7|
|Aporte en Receptor A2(2)|0,32|2,9|
|Aporte en Receptor B2(2)|0,60|3,8|
|Valores según normativa(3)|80,0 (31 ppb)|250,0 (96 ppb)|

Notas:
(1) Considerando información disponible en el sitio web del SINCA para otras ciudades del país.
(2) Concentraciones estimadas (ver Cuadro 18 del presente informe).
(3) Decretos Supremo N°113/02 del Ministerio Secretaría General de la Presidencia.
Fuente: Elaboración propia.

c) Dióxido de Nitrógeno (NO 2 )

El Cuadro 24 evalúa tentativamente el cumplimiento de la normativa primaria horaria y
anual para NO 2 en los receptores sensibles antes indicados (Cuadro 17), considerando como
referencia la información disponible en el sitio web del SINCA para otras ciudades del país.

Sacyr Chile S.A 54 Eco Master

Cuadro 24: Evaluación del cumplimiento de normativa (primaria) sobre NO 2 en los
Receptores Sensibles del Proyecto.

|Parámetros|Concentraciones NO (μg/m3N)<br>2|Col3|
|---|---|---|
|Parámetros|Promedio Anual|Percentil 99<br> <br> (valores horarios)|
|Línea base (supuesto)(1)|9,4 - 37,7 (5-20 ppb)|94 - 282 (50-150 ppb)|
|Aporte en Receptor A1(2)|2,3|4.452,9|
|Aporte en Receptor B1(2)|0,8|275,5|
|Aporte en Receptor C1(2)|0,2|125,4|
|Aporte en Receptor A2(2)|8,3|773,2|
|Aporte en Receptor B2(2)|16,2|1.591,4|
|Valores según normativa(3)|100,0 (53 ppb)|400,0 (213 ppb)|

Notas:
(1) Considerando información disponible en el sitio web del SINCA para otras ciudades del país.
(2) Concentraciones estimadas (ver Cuadro 18 del presente informe).
(3) Decretos Supremo N°114/02 del Ministerio Secretaría General de la Presidencia.
Fuente: Elaboración propia.

8.0 CONCLUSIONES

De acuerdo a los resultados de la modelación, se concluye que las emisiones de MP10,
MP2.5, MPS, CO, SO 2 y NO 2, provenientes del Proyecto, en general no superan por si solas
las respectivas normas o valores de referencia sobre calidad del aire vigentes en Chile, en
los alrededores del área del Proyecto, incluyendo los receptores sensibles identificados.
Constituye una excepción la superación de la norma horaria de NOx en el Receptor A1. Los
puntos de máximo impacto de todos los contaminantes se localizan al interior del área del
Proyecto, donde aplicaría la normativa sobre lugares de trabajo.

La evaluación de las concentraciones anticipadas para cada uno de los contaminantes
analizados, fuera de los límites del área del Proyecto, es la siguiente:

- Material particulado respirable (MP10): Las concentraciones máximas diarias y
anuales de MP10 se encuentran en los rangos 10-20 μg/m [3] N y 0,5-1,5 μg/m [3] N,
respectivamente, y se manifiestan en los alrededores inmediatos del área del
Proyecto. Todas las concentraciones son inferiores a los valores que señalan las
normas primarias diaria y anual para MP10; 150 μg/m [3] N y 50 μg/m [3] N,
respectivamente (Decreto Supremo No59/98 del Ministerio de Salud).

- Material particulado fino (MP2.5): Las concentraciones máximas diarias y anuales
de MP2.5 se encuentran en los rangos 2,5-5 μg/m [3] N y 0,5-1,5 μg/m [3] N,
respectivamente, y se manifiestan en los alrededores inmediatos del área del
Proyecto. Todas las concentraciones son inferiores a los valores que señalan las
normas primarias diaria y anual para MP2.5; 50 μg/m [3 ] y 20 μg/m [3], respectivamente
(Decreto Supremo No12/11 del Ministerio del Medio Ambiente).

- Material particulado sedimentable (MPS): Las concentraciones máximas anuales
de MPS se encuentran en el rango 2,5 - 5 g/m [2] /año (equivalente a 6,8-13,7
mg/m [2] /día) y se manifiestan en los alrededores inmediatos del área del Proyecto.
Todas las concentraciones son inferiores al valor de referencia anual para MPS que
establece la Confederación Suiza; 200 mg/m [2] /día.

Sacyr Chile S.A 55 Eco Master

- Monóxido de carbono (CO): Las concentraciones máximas horarias y de 8 horas de
CO se encuentran en los rangos 2.500-10.000 μg/m [3] N y 250-2.000 μg/m [3] N, y se
manifiestan en los alrededores inmediatos del área del Proyecto. Todas las
concentraciones son muy inferiores a los valores establecidos por las normas
primarias de 1 y 8 horas para CO; 30.000 μg/m [3] N y 10.000 μg/m [3] N, respectivamente
(Decreto Supremo No115/02 del Ministerio Secretaría General de la Presidencia).

- Dióxido de azufre (SO 2 ): Las concentraciones máximas diarias y anuales de SO 2 se
encuentran en los rangos de 100-250 μg/m [3] N, 10-25 μg/m [3] N y 1-1,5 μg/m [3] N,
respectivamente. Todas las concentraciones son muy inferiores a los valores que
señalan las normas primarias diaria y anual para SO 2 ; 250 μg/m [3] N y 80 μg/m [3] N,
respectivamente (Decreto Supremo No113/02 del Ministerio Secretaría General de la
Presidencia). También cumplen las normas secundarias horaria, diaria y anual para
SO 2 ; 700 μg/m [3] N, 260 μg/m [3] N y 60 μg/m [3] N, respectivamente (Decreto Supremo
No22/10 del Ministerio Secretaría General de la Presidencia).

- Dióxido de nitrógeno (NO 2 ): Las concentraciones máximas horarias y diarias de
NO 2 se encuentran en los rangos 1.500-2.000 μg/m [3] N y 1-2,5 μg/m [3] N, y se
manifiestan en los alrededores inmediatos del área del Proyecto. Las concentraciones
anuales son inferiores a los valores que señalan la norma primaria para NO 2 ; 400

Secretaría General de la Presidencia).

Sacyr Chile S.A 56 Eco Master

NOTA FINAL

Este documento ha sido elaborado por Eco Master en respuesta a una solicitud expresa y
en base a la información y antecedentes proporcionados por Sacyr Chile S.A.

Los datos de la empresa Eco Master son los siguientes:

- Razón social: F.R.B. Ingeniería Ltda.

- Nombre de fantasía: Eco Master

- R.U.T.: 77.581.630-3

- Dirección comercial: Loreley 1337, La Reina, Santiago

- Fono: (2) 2371 7002

- Email: frb@entelchile.net

Santiago, 28 de Febrero de 2014

Sacyr Chile S.A 57 Eco Master

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Coordenadas UTM de los vértices del área del Proyecto.**

| Vértice | Coordenadas UTM<br>(Datum WGS-84, Huso 19 S) | Col3 |
| --- | --- | --- |
| Vértice | Norte | Este |
| 1 | 6.662.625,00 | 287.189,00 |
| 2 | 6.661.635,00 | 288.733,00 |
| 3 | 6.661.393,00 | 288.677,00 |
| 4 | 6.661.993,00 | 287.242,00 |

**Tabla 2: Normas de calidad del aire vigentes a nivel nacional.**

| Cuerpo Legal | Contaminante<br>Normado | Límite Máximo<br>Establecido | Período<br>Normado | Criterios de Superación de las<br>Normas |
| --- | --- | --- | --- | --- |
| D.S. N°59/98<br>MINSEGPRES | MP10 | 150 ug/m3N(1) | Diario | Percentil 98 de los valores diarios<br>registrados en un año calendario,<br>supera el valor de la norma diaria;<br>o si en un año calendario se<br>supera en más de 7 ocasiones el<br>valor de la norma diaria. |
| D.S. N°59/98<br>MINSEGPRES | MP10 | 50 ug/m3N(1) | Anual | Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos de promedios<br>anuales, es igual o superior al<br>valor de la norma anual. |
| D.S. N°12/11<br>MMA | MP2.5 | 50 ug/m3N(1) | Diario | Percentil 98 de los valores diarios<br>registrados en un año calendario,<br>es superior al valor de la norma<br>diaria. |
| D.S. N°12/11<br>MMA | MP2.5 | 20 ug/m3N(1) | Anual | Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos de promedios<br>anuales, es superior al valor de la<br>norma anual. |
| D.S. N°113/02<br>MINSEGPRES | SO2 | 250 ug/m3N <br>(ó 96 ppbv)(1) <br> | Diaria | Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99<br>de<br>los<br>valores<br>diarios<br>registrados en cada año, es igual o<br>superior al valor de la norma<br>diaria. |
| D.S. N°113/02<br>MINSEGPRES | SO2 | 80 ug/m3N <br>(ó 31 ppbv)(1) | Anual | Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos de promedios<br>anuales, es igual o superior al<br>valor de la norma anual. |
| D.S. N°22/10<br>MINSEGPRES | SO2 | 700 ug/m3N <br>(ó 268 ppbv)(2) | Horario | Media<br>aritmética<br>de<br>3 <br>años<br>calendarios seguidos del Percentil<br>99,73 de las concentraciones de 1 |

**Tabla 3: Antecedentes estaciones de monitoreo de calidad del aire en comuna de**

| Estación de<br>Monitoreo | Coordenadas UTM<br>(WGS-84, H 19S) | Col3 | Contaminantes<br>Monitoreados | Período de Datos<br>Disponibles(1) |
| --- | --- | --- | --- | --- |
| Estación de<br>Monitoreo | Este | Norte | Norte | Norte |
| Andacollo | 299.239 | 6.654.143 | MP10 | 17/07/2009-26/02/2014 |
| Andacollo | 299.239 | 6.654.143 | MP2.5 | Sin información disponible |
| Chepiquilla | 299.429 | 6.651.104 | MP10 | 02/01/2005-26/04/2010 |
| El Sauce | 298.643 | 6.653.356 | MP10 | 01/06/2009-31/05/2010 |
| Hospital | 299.414 | 6.654.515 | MP10 | 03/01/2010-31/05/2010 |
| Urmeneta-<br>Plaza<br>Centenario | 299.288 | 6.652.817 | MP10 | 02/01/2005-20/04/2010 |

**Tabla 4: Antecedentes de estaciones de monitoreo de calidad del aire en**

| Estación de<br>Monitoreo | Coordenadas UTM<br>(WGS-84, H 19S) | Col3 | Contaminantes<br>Monitoreados | Período de Datos<br>Disponibles(1) |
| --- | --- | --- | --- | --- |
| Estación de<br>Monitoreo | Este | Norte | Norte | Norte |
| Coquimbo | 274.603 | 6.682.159 | MP2.5 | 26/01/2014-12/02/2014 |
| La Serena | 282.210 | 6.687.902 | MP2.5 | 26/01/2014-10/02/2014 |

**Tabla 5: Resultados procesamiento de datos diarios de MP10 en Estación**

| Parámetros | Estación de Monitoreo |
| --- | --- |
| Parámetros | Andacollo |
| Período de datos analizados | 01/01/2013-31/12/2013 |
| Número de datos diarios | 259 |
| Promedio anual (ug/m3N) | 64,0 |
| Norma anual (ug/m3N) | 50,0 |
| Percentil 98 de valores diarios (ug/m3N) | 121,0 |
| Máximo diario anual (ug/m3N) | 172,9 |
| Mínimo diario (ug/m3N) | 7,0 |
| Número de días sobre norma diaria | 1 |
| Número de días sobre 80% norma diaria (>120 ug/m3N) | 5 |
| Norma diaria (ug/m3N) | 150,0 |

**Tabla 6: Resultados procesamiento de datos diarios de MP2.5 en Estaciones**

| Parámetros | Estaciones de Monitoreo | Col3 |
| --- | --- | --- |
| Parámetros | Coquimbo | La Serena |
| Período de datos analizados | 26/01/2014-10/02/2014 | 26/01/2014-09/02/2014 |
| Número datos diarios | 16 | 15 |
| Promedio período (ug/m3N) | 9,0 | 18,7 |
| Norma anual (ug/m3N) | 20,0 | 20,0 |
| Percentil 98 de valores diarios (ug/m3N) | - | - |
| Máximo diario (ug/m3N) | 12,5 | 22,4 |
| Mínimo diario (ug/m3N) | 6,2 | 14,0 |
| Número de días sobre norma diaria | 0 | 0 |
| Número de días sobre 80% norma diaria<br>(>120 ug/m3N) | 0 | 0 |
| Norma diaria (ug/m3N) | 50,0 | 50,0 |

**Tabla 7: Fuentes de emisiones atmosféricas etapa de operación del Proyecto.**

| TIPO DE<br>EMISIONES | FUENTES DE EMISIÓN | CONTAMINANTES(*) |
| --- | --- | --- |
| Fugitivas de<br>material<br>particulado | Escarpe del terreno (Pozo de Áridos) | Material particulado |
| Fugitivas de<br>material<br>particulado | Excavación del terreno - material no apto (Pozo de Áridos) | Material particulado |
| Fugitivas de<br>material<br>particulado | Extracción de áridos (Pozo de Áridos) | Material particulado |
| Fugitivas de<br>material<br>particulado | Selección de áridos bajo 4 “(Pozo de Áridos) | Material particulado |
| Fugitivas de<br>material<br>particulado | Carguío de áridos (Pozo de Áridos) |  |
| Fugitivas de<br>material<br>particulado | Transporte interno de áridos (Pozo de Áridos) | Material particulado |
| Fugitivas de<br>material<br>particulado | Transporte material integral y bajo 4” por camino interno<br>hasta Ruta 43 (Pozo de Áridos) | Material particulado |
| Fugitivas de<br>material<br>particulado | Procesamiento y manejo de áridos (Planta de Chancado) | Material particulado |
| Fugitivas de<br>material<br>particulado | Acopio de base chancada ( Planta de Chancado) | Material particulado |
| Fugitivas de<br>material<br>particulado | Carguío de base chancada (Planta de Chancado) | Material particulado |
| Fugitivas de<br>material<br>particulado | Transporte interno de base chancada (Planta de Chancado) | Material particulado |
| Fugitivas de<br>material<br>particulado | Transporte de base chancada por camino interno hasta<br>Ruta 43 (Planta de Chancado) | Material particulado |
| Fugitivas de<br>material<br>particulado | Descarga de áridos asfalto (Planta de Asfalto) | Material particulado |
| Fugitivas de<br>material<br>particulado | Transporte de asfalto por camino interno hasta Ruta 43<br>(Planta de Asfalto) | Material particulado |
| Combustión<br>interna | Uso / funcionamiento de camiones y maquinaria (Pozo de<br>Áridos, Planta de Chancado y Planta de Asfalto) | Material particulado y<br>gases de combustión |
| Combustión<br>interna | Uso / funcionamiento de grupos electrógenos (Planta de<br>Chancado y Planta de Asfalto) | Material particulado y<br>gases de combustión |
| Combustión<br>externa<br> | Uso / funcionamiento de caldera y horno rotatorio (Planta<br>de Asfalto)<br> | Material particulado y<br>gases de combustión |

**Tabla 8: Resumen de emisiones atmosféricas de la etapa de operación del Proyecto.**

| TIPO DE<br>EMISIONES | FUENTES DE EMISIÓN | EMISIONES DIARIAS (kg/día) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TIPO DE<br>EMISIONES | FUENTES DE EMISIÓN | PTS | MP10 | MP2.5 | CO | SOx | NOx |
| Fugitivas de<br>material<br>particulado | Escarpe del terreno (Pozo de Áridos) | 4,54 | 2,27 | 1,13 |  |  |  |
| Fugitivas de<br>material<br>particulado | Excavación del terreno - retiro de material no apto<br>(Pozo de Áridos) | 14,38 | 2,71 | 0,38 |  |  |  |
| Fugitivas de<br>material<br>particulado | Extracción de áridos (Pozo de Áridos) | 67,01 | 13,40 | 0,30 |  |  |  |
| Fugitivas de<br>material<br>particulado | Selección de áridos bajo 4” (Pozo de Áridos) | 4,17 | 1,43 | 0,72 |  |  |  |
| Fugitivas de<br>material<br>particulado | Carguío de áridos (Pozo de Áridos) | 12,32 | 5,83 | 1,83 |  |  |  |
| Fugitivas de<br>material<br>particulado | Transporte interno de áridos hasta Planta de<br>Chancado (Pozo de Áridos) | 33,46 | 9,79 | 0,51 |  |  |  |
| Fugitivas de<br>material<br>particulado | Transporte externo de material integral y bajo 4” por<br>camino interno del Proyecto | 15,08 | 5,57 | 0,84 |  |  |  |
| Fugitivas de<br>material<br>particulado | Subtotal Parcial | 150,96 | 41,00 | 5,71 |  |  |  |
| Fugitivas de<br>material<br>particulado | Procesamiento y manejo de áridos (Planta de<br>Chancado) | 1,56 | 0,56 | 0,09 |  |  |  |
| Fugitivas de<br>material<br>particulado | Acopio de base chancada (Planta de Chancado) | 0,08 | 0,04 | 0,02 |  |  |  |
| Fugitivas de<br>material<br>particulado | Carguío de base chancada (Planta de Chancado) | 12,32 | 5,83 | 1,83 |  |  |  |
| Fugitivas de<br>material<br>particulado | Transporte interno de base chancada a acopios<br>(Planta de Chancado) | 12,87 | 3,77 | 0,19 |  |  |  |
| Fugitivas de<br>material<br>particulado | Transporte interno de base chancada a Planta de<br>Asfalto (Planta de Chancado) | 6,15 | 1,8 | 0,09 |  |  |  |
| Fugitivas de<br>material<br>particulado | Transporte externo de base chancada por camino<br>interno del Proyecto (Planta de Chancado) | 10,40 | 3,84 | 0,58 |  |  |  |
| Fugitivas de<br>material<br>particulado | Subtotal Parcial | 43,38 | 15,84 | 2,80 |  |  |  |
| Fugitivas de<br>material<br>particulado | Descarga de áridos (Planta de Asfalto) | 5,28 | 2,50 | 0,78 |  |  |  |
| Fugitivas de<br>material<br>particulado | Transporte de asfalto por camino interno del<br>Proyecto (Planta de Asfalto) | 4,52 | 1,67 | 0,25 |  |  |  |

**Tabla 9: Área de modelación en las comunas de Andacollo y Coquimbo.**

| Vértices | Coordenadas UTM (aproximadas)<br>(Datum WGS-84, Huso 19S) | Col3 |
| --- | --- | --- |
| Vértices | Este | Norte |
| Noroeste | 292.645 | 6.667.095 |
| Noreste | 302.645 | 6.667.095 |
| Sureste | 302.645 | 6.657.095 |
| Suroeste | 292.645 | 6.657.095 |

**Tabla 10: Ubicación de puntos de máximo impacto del Proyecto.**

| Contaminantes | Parámetros | Coordenadas UTM aproximadas<br>(Datum WGS-84, Huso 19S) | Col4 |
| --- | --- | --- | --- |
| Contaminantes | Parámetros | Este | Norte |
| MP10 | Concentración máxima diaria | 287.904,8 | 6.661.945,0 |
| MP10 | Promedio máximo anual | 287.662,4 | 6.661.996,5 |
| MP2.5 | Concentración máxima diaria | 287.904,8 | 6.661.945,0 |
| MP2.5 | Promedio máximo anual | 287.662,4 | 6.661.996,5 |
| MPS | Promedio máximo anual | 288.411,0 | 6.661.452,2 |
| CO | Concentración máxima 1 hora | 287.743,5 | 6.662.112,4 |
| CO | Concentración máxima 8 hora | 287.713,5 | 6.662.112,4 |
| SO2 | Concentración máxima 1 hora | 287.679,2 | 6.662.189,0 |
| SO2 | Concentración máxima diaria | 287.709,3 | 6.662.018,4 |
| SO2 | Promedio máximo anual | 287.662,4 | 6.661.996,5 |
| NO2 | Concentración máxima 1 hora | 287.743,5 | 6.662.112,4 |
| NO2 | Promedio máximo anual | 287.662,4 | 6.661.996,5 |

**Tabla 11: Aporte del Proyecto en los puntos de máximo impacto.**

| Contaminantes | Parámetros | Aporte del<br>Proyecto | Valor de la<br>Norma Primaria<br>(Secundaria) |
| --- | --- | --- | --- |
| MP10 | Concentración máxima diaria | 105,8 ug/m3N | 150 ug/m3N |
| MP10 | Promedio máximo anual | 11,8 ug/m3N | 50 ug/m3N |
| MP2.5 | Concentración máxima diaria | 57,9 ug/m3N | 50 ug/m3N |
| MP2.5 | Promedio máximo anual | 7,7 ug/m3N | 20 ug/m3N |
| MPS | Promedio máximo anual | 221,4 mg/m2/día | 200 mg/m2/día |
| CO | Concentración máxima 1 hora | 91.861 ug/m3N | 30.000 ug/m3N |
| CO | Concentración máxima 8 hora | 11.482 ug/m3N | 10.000 ug/m3N |
| SO2 | Concentración máxima 1 hora | 15.417 ug/m3N | (700 ug/m3N) |
| SO2 | Concentración máxima diaria | 676,7 ug/m3N | 250 ug/m3N <br>(260 ug/m3N) |
| SO2 | Promedio máximo anual | 152,6 ug/m3N | 80 ug/m3N <br>(60 ug/m3N) |
| NO2 | Concentración máxima 1 hora | 46.213 ug/m3N | 400 ug/m3N |
| NO2 | Promedio máximo anual | 301 ug/m3N | 100 ug/m3N |

**Tabla 12: Evaluación del cumplimiento de normativa (primaria) sobre MP10 en**

| Parámetros | Concentraciones MP10 (μg/m3N) | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 98<br>(valores diarios) |
| Línea base (supuesto)(1) | 64,0 | 121,0 |
| Aporte máximo del Proyecto(2) | 11,8 | 105,8 |
| Valores según normativa(3) | 50,0 | 150,0 |

**Tabla 13: Evaluación del cumplimiento de normativa (primaria) sobre MP2.5 en**

| Parámetros | Concentraciones MP2.5 (μg/m3N) | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 98<br>(valores diarios) |
| Línea base (supuesto)(1) | 13,9 | 17,5 |
| Aporte máximo del Proyecto(2) | 7,7 | 221,4 |
| Valores según normativa(3) | 20,0 | 50,0 |

**Tabla 14: Evaluación del cumplimiento de normativa sobre MPS en el punto de**

| Parámetros | Concentraciones MP10<br>(mg/m2/día) |
| --- | --- |
| Parámetros | Promedio Anual |
| Línea base (supuesto)(1) | 40,0 - 80,0 |
| Aporte máximo del Proyecto(2) | 221,4 |
| Valores según normativa(3) | 200,0 |

**Tabla 15: Evaluación del cumplimiento de normativa (primaria) sobre CO en el**

| Parámetros | Concentraciones CO (μg/m3N) | Col3 |
| --- | --- | --- |
| Parámetros | Percentil 99<br>(datos 1 hora) | Percentil 99<br>(datos 8 horas) |
| Línea base (supuesto)(1) | 11.540-23.080 (10-20 ppm) | 3.333-5.555 (3-5 ppm) |
| Aporte máximo del Proyecto(2) | 91.861 | 11.482 |
| Valores según normativa(3) | 30.000 (26 ppm) | 10.000 (9 ppm) |

**Tabla 16: Evaluación del cumplimiento de normativa (primaria) sobre SO 2 en el**

| Parámetros | Concentraciones SO (μg/m3N)<br>2 | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 99<br>(valores diarios) |
| Línea base (supuesto)(1) | 3,0 - 5,0 | 20,0 |
| Aporte máximo del Proyecto(2) | 152,6 | 676,7 |
| Valores según normativa(3) | 80,0 (31 ppb) | 250,0 (96 ppb) |

**Tabla 17: Evaluación del cumplimiento de normativa (primaria) sobre NO 2 en el**

| Parámetros | Concentraciones NO (μg/m3N)<br>2 | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 99<br> <br> (valores diarios) |
| Línea base (supuesto)(1) | 9,4 - 37,7 (5-20 ppb) | 94 - 282 (50-150 ppb) |
| Aporte máximo del Proyecto(2) | 301,0 | 46.213 |
| Valores según normativa(3) | 100,0 (53 ppb) | 400,0 (213 ppb) |

**Tabla 18: Localización de viviendas más próximas al área del Proyecto.**

| Punto | Descripción | Coordenadas UTM<br>(Datum WGS 84, Huso H 19S) | Col4 |
| --- | --- | --- | --- |
| Punto | Descripción | Este | Norte |
| A1 | Vivienda ubicada al oriente del Proyecto y<br>al norte de la Ruta D-51. | 287.961 | 6.662.565 |
| B1 | Vivienda ubicada al norponiente del<br>Proyecto. | 286.925 | 6.662.367 |
| C1 | Vivienda ubicada al oriente del Proyecto y<br>al sur de la Ruta D-51 | 289.324 | 6.662.176 |
| A2 | Vivienda ubicada al suroriente del Proyecto<br>y al poniente de la Ruta D-323. | 288.877 | 6.661.247 |
| B2 | Vivienda ubicada norte del Proyecto. | 288.462 | 6.661.204 |

**Tabla 19: Evaluación del cumplimiento de normativa (primaria) sobre MP10 en**

| Parámetros | Concentraciones MP10 (μg/m3N) | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 98<br>(valores diarios) |
| Línea base (supuesto)(1) | 64,0 | 121,0 |
| Aporte en Receptor A1(2) | 0,1 | 2,4 |
| Aporte en Receptor B1(2) | 0,3 | 1,8 |
| Aporte en Receptor C1(2) | 0,04 | 0,8 |
| Aporte en Receptor A2(2) | 2,5 | 8,5 |
| Aporte en Receptor B2(2) | 4,5 | 16,5 |
| Valores según normativa(3) | 50,0 | 150,0 |

**Tabla 20: Evaluación del cumplimiento de normativa (primaria) sobre MP2.5 en**

| Parámetros | Concentraciones MP2.5 (μg/m3N) | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 98<br>(valores diarios) |
| Línea base (supuesto)(1) | 13,9 | 17,5 |
| Aporte en Receptor A1(2) | 0,12 | 2,32 |
| Aporte en Receptor B1(2) | 0,12 | 0,98 |
| Aporte en Receptor C1(2) | 0,02 | 0,39 |
| Aporte en Receptor A2(2) | 0,91 | 3,28 |
| Aporte en Receptor B2(2) | 1,75 | 7,25 |
| Valores según normativa(3) | 20,0 | 50,0 |

**Tabla 21: Evaluación del cumplimiento de normativa sobre MPS en los**

| Parámetros | Concentraciones MP10<br>(mg/m2/día) |
| --- | --- |
| Parámetros | Promedio Anual |
| Línea base (supuesto)(1) | 40,0 - 80,0 |
| Aporte en Receptor A1(2) | 0,52 |
| Aporte en Receptor B1(2) | 4,1 |
| Aporte en Receptor C1(2) | 0,4 |
| Aporte en Receptor A2(2) | 73,0 |
| Aporte en Receptor B2(2) | 102,4 |
| Valores según normativa(3) | 200,0 |

**Tabla 22: Evaluación del cumplimiento de normativa (primaria) sobre CO en los**

| Parámetros | Concentraciones CO (μg/m3N) | Col3 |
| --- | --- | --- |
| Parámetros | Percentil 99<br>(datos 1 hora) | Percentil 99<br>(datos 8 horas) |
| Línea base (supuesto)(1) | 11.540-23.080 (10-20 ppm) | 3.333-5.555 (3-5 ppm) |
| Aporte en Receptor A1(2) | 2.141 | 289 |
| Aporte en Receptor B1(2) | 146 | 18 |
| Aporte en Receptor C1(2) | 162 | 21 |
| Aporte en Receptor A2(2) | 452 | 59 |
| Aporte en Receptor B2(2) | 667 | 95 |
| Valores según normativa(3) | 30.000 (26 ppm) | 10.000 (9 ppm) |

**Tabla 23: Evaluación del cumplimiento de normativa (primaria) sobre SO 2 en los**

| Parámetros | Concentraciones SO (μg/m3N)<br>2 | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 99<br>(valores diarios) |
| Línea base (supuesto)(1) | 3,0 - 5,0 | 20,0 |
| Aporte en Receptor A1(2) | 0,58 | 7,6 |
| Aporte en Receptor B1(2) | 0,11 | 0,9 |
| Aporte en Receptor C1(2) | 0,04 | 0,7 |
| Aporte en Receptor A2(2) | 0,32 | 2,9 |
| Aporte en Receptor B2(2) | 0,60 | 3,8 |
| Valores según normativa(3) | 80,0 (31 ppb) | 250,0 (96 ppb) |

**Tabla 24: Evaluación del cumplimiento de normativa (primaria) sobre NO 2 en los**

| Parámetros | Concentraciones NO (μg/m3N)<br>2 | Col3 |
| --- | --- | --- |
| Parámetros | Promedio Anual | Percentil 99<br> <br> (valores horarios) |
| Línea base (supuesto)(1) | 9,4 - 37,7 (5-20 ppb) | 94 - 282 (50-150 ppb) |
| Aporte en Receptor A1(2) | 2,3 | 4.452,9 |
| Aporte en Receptor B1(2) | 0,8 | 275,5 |
| Aporte en Receptor C1(2) | 0,2 | 125,4 |
| Aporte en Receptor A2(2) | 8,3 | 773,2 |
| Aporte en Receptor B2(2) | 16,2 | 1.591,4 |
| Valores según normativa(3) | 100,0 (53 ppb) | 400,0 (213 ppb) |
