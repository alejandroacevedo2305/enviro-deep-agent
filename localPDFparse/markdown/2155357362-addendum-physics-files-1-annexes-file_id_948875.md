---
title: Sin título
author: Anexo 1.5 Estudio de emisiones atmosféricas, DIA “Data Center Chile 2”
date: D:20220526163333-04'00'
language: es
type: report
pages: 86
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Adenda del proyecto “SCALA Data Center Curauma”
-->

# Adenda del proyecto “SCALA Data Center Curauma”

## Informe de modelación de emisiones atmosféricas

Elaborado por:

GIZA Ingeniería SpA
[https://gizaingenieria.com/](https://gizaingenieria.com/)

Región Metropolitana, mayo de 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_1_
_Curauma”_

**ÍNDICE**

**1. INTRODUCCIÓN............................................................................................................................................... 4**
**2. DESCRIPCIÓN GENERAL DEL PROYECTO .......................................................................................................... 4**

**2.1.** **D** **ESCRIPCIÓN BREVE DEL PROYECTO** **.** .................................................................................................................. 4

**3. LOCALIZACIÓN ................................................................................................................................................ 7**

**4. EMISIONES A MODELAR ................................................................................................................................ 10**
**5. MODELACIÓN DE EMISIONES ATMOSFÉRICAS .............................................................................................. 12**

**5.1.** **M** **ARCO LEGAL** ............................................................................................................................................ 12

**5.2.** **E** **CUACIÓN GENERAL PARA EL CÁLCULO DE EMISIONES** .......................................................................................... 13

**5.3.** **R** **ESULTADOS Y** **A** **NÁLISIS** ............................................................................................................................... 14

**5.4** **D** **ESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO** ....................................................................................................... 15

**5.5** **F** **UENTES DE EMISIÓN** .................................................................................................................................... 15

**5.6** **R** **ESULTADOS DE LA MODELACIÓN** .................................................................................................................... 17

_5.6.1 Fase de construcción ......................................................................................................................... 17_

_5.6.2 Fase de operación. Etapa propuesta.................................................................................................. 27_
_5.6.3 Fase de operación. Proyecto total ..................................................................................................... 37_

**6. CONCLUSIÓN................................................................................................................................................. 48**

**7. REFERENCIAS ................................................................................................................................................ 49**
**APÉNDICE 1: MEMORIA DE CÁLCULO DE LA MODELACIÓN ............................................................................... 50**

**ÍNDICE DE TABLAS**

Tabla 1. Resumen de emisiones por actividad, Fase de Construcción - Escenario 1............................................. 11
Tabla 2. Resumen de emisiones por actividad, Fase de Operación Etapa Propuesta - Escenario 2 ...................... 11

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- material particulado MPS, MP 10 y MP 2,5 presentes en las emisiones por resuspensión y combustión, así como los Gases, CO, NO X y SO X, producto de la combustión en las fuentes estacionarias y móviles, asociadas a las actividades del proyecto por cada escenario. Además, se consideraron las emisiones anuales asociadas a las fuentes emisoras de contaminantes del Proyecto (ver -->

**Tabla 2: , Tabla 2 y Tabla 3), producidas en toda la superficie del sitio del proyecto. El resultado de las emisiones**

| Emisiones | CO | SO<br>x | NO<br>X | MP<br>2,5 Total | MP<br>10 Total | MPS<br>l |
| --- | --- | --- | --- | --- | --- | --- |
| ton/año | 0,1312 | 0,0007 | 0,1202 | 0,0705 | 0,0922 | 0,4112 |
| g/m2-s | **0,0000004475** | **0,0000000024** | **0,0000004097** | **0,0000002402** | **0,0000003144** | **0,0000014019** |

<!-- Estadísticas: 2 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia, 2022 Tabla 8. Tasas de emisiones del Proyecto, Fase operación Etapa propuesta - Escenario 2 -->
<!-- FIN TABLA 2 -->

Tabla 3. Resumen de emisiones por actividad, Fase de Operación Proyecto Total - Escenario 3 ......................... 11

Tabla 4. Normas de Calidad del Aire consideradas en el estudio ......................................................................... 12

Tabla 5. Contaminante que constituye la Línea de base de Calidad de aire y ubicación de la Estación de monitoreo

................................................................................................................................................................. 13
Tabla 6. Resumen de concentraciones (μg/m [3] N) ................................................................................................ 14
Tabla 7. Tasas de emisiones del Proyecto, Fase construcción - Escenario 1 ........................................................ 15
Tabla 8. Tasas de emisiones del Proyecto, Fase operación Etapa propuesta - Escenario 2 .................................. 15
Tabla 9. Tasas de emisiones del Proyecto, Fase operación Proyecto total - Escenario 3 ...................................... 15
Tabla 10. Coordenadas de los receptores del Proyecto ....................................................................................... 16

Tabla 11. Datos de entrada del modelo .............................................................................................................. 17

Tabla 12. Resultados del modelo, Fase de construcción - Escenario 1 ................................................................ 17

Tabla 13. Máximas concentraciones horarias obtenidas del modelo ................................................................... 18

Tabla 14. Factores de conversión para promedios máximos de concentración.................................................... 18
Tabla 15. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Construcción - Escenario 1

................................................................................................................................................................. 19

Tabla 16. Concentraciones por distancia de los contaminantes analizados, Fase de Construcción - Escenario 1 .. 20

Tabla 17. Datos de entrada del modelo .............................................................................................................. 27

Tabla 18. Resultados del modelo, Fase de operación Etapa propuesta - Escenario 2 .......................................... 27
Tabla 19. Máximas concentraciones horarias obtenidas del modelo. Fase operación, Etapa propuesta - Escenario

2 ............................................................................................................................................................... 28

Tabla 20. Factores de conversión para promedios máximos de concentración.................................................... 28
Tabla 21. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Operación Etapa

Propuesta - Escenario 2 ............................................................................................................................ 29

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_2_
_Curauma”_

Tabla 22. Concentraciones por distancia de los contaminantes analizados, Fase de Operación Etapa PropuestaEscenario 2 ............................................................................................................................................... 30

Tabla 23. Datos de entrada del modelo .............................................................................................................. 37

Tabla 24. Resultados del modelo, Fase de operación Proyecto total - Escenario 3 .............................................. 37
Tabla 25. Máximas concentraciones horarias obtenidas del modelo. Fase operación, Proyecto total - Escenario 3

................................................................................................................................................................. 38

Tabla 26. Factores de conversión para promedios máximos de concentración.................................................... 38
Tabla 27. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Operación Proyecto totalEscenario 3 ............................................................................................................................................... 39

Tabla 28. Concentraciones por distancia de los contaminantes analizados, Fase de Operación Proyecto totalEscenario 3 ............................................................................................................................................... 40

**ÍNDICE DE FIGURAS**

Figura 1. Cuadro de superficies Proyecto completo .............................................................................................. 4
Figura 2. Cuadro de superficies etapa propuesta .................................................................................................. 6
Figura 3. Localización del Proyecto....................................................................................................................... 8
Figura 4. Ubicación del Proyecto respecto a la aplicación del D.S. N°10/2015 y PPDA de Concón, Quintero y

Puchuncaví ............................................................................................................................................... 10

Figura 5. Ubicación de la Estación de monitoreo de Calidad de aire .................................................................... 14
Figura 6. Ubicación de los potenciales receptores de norma primaria y secundaria ............................................ 16
Figura 7. Área de influencia del Proyecto, Fase de Construcción - Escenario 1 .................................................... 21
Figura 8. Área de influencia del Proyecto, Fase de Operación, Etapa propuesta - Escenario 2 ............................. 31
Figura 9. Área de influencia del Proyecto, Fase de Operación, Proyecto total- Escenario 3 ................................. 41
Figura 10. Distancia respecto al Lago Peñuelas ................................................................................................... 47

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_3_
_Curauma”_

**1. INTRODUCCIÓN**

E l presente informe contiene la modelación de emisiones atmosféricas de los contaminantes material particulado
respirable (MP10), Material particulado respirable fino (MP2,5) y gases (NOx, SOx y CO), producto de la
construcción y operación del proyecto “SCALA Data Center Curauma” ubicado en la comuna y región de Valparaíso.

**2. DESCRIPCIÓN GENERAL DEL PROYECTO**

**2.1. Descripción breve del proyecto.**

El proyecto denominado “SCALA Data Center Curauma”, consiste en la construcción y habilitación de data centers
por etapas, diseñados con una infraestructura acorde para almacenar aplicaciones y datos críticos a gran escala de
diversas empresas. Estará conformado por un total de 4 edificios con un consumo de energía 30 MW y que contará
con un total de 38 grupos electrógenos de emergencia (34 equipos de 3.437 KVA/2.750 kW para respaldo de salada
datos y 4 equipos de 400 kW/500 KVA para respaldo de áreas comunes), 30 equipos de enfriamientos tipo Chillers
de 1.557 kW, 168 equipos de aire acondicionado tipo Crah (ventiladores - computer room air handler), 34 áreas
de transformadores, 30 áreas de baterías, bodegas de mantenimiento y almacenamientos para distintos usos
(placas, fibras ópticas, partes equipos útiles de aseo y artículos de oficina), oficinas del cliente, salas de descanso,
salas de conferencia, una salas de basura, 2 estaciones de bombeo de agua potable para el control de incendios,
oficinas Scala, salas de seguridad, controles de acceso, áreas de carga y descarga, 84 estacionamientos vehiculares
(incluye 13 estacionamientos de 30 m2 para camiones) y 66 estacionamientos para bicicletas. El terreno donde se
localizará el Proyecto cuenta con una superficie de terreno de 82.448,54 m2 y tendrá una superficie construida
total de 26.525,50 m2. Las superficies de ocupación del Proyecto completo corresponden a 65.345,70 m2
correspondientes a los polígonos de los 4 edificio de data center, las 2 estación de bombeo, sala de basura,
portería, calle, estacionamientos, veredas, áreas verdes y sala de pre-carguío graficado en el plano “CUR01-E-BAUDC01-AR00-A0-4001-R-0A” adjunto en el Anexo A-02 de la Adenda.

Figura 1. Cuadro de superficies Proyecto completo

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_4_
_Curauma”_

El Proyecto **se realizará en 4 etapas, la primera de ella cierta y determinada, consistente en el edificio 1 y obras**
**anexas, y las siguientes eventuales y sujetas condiciones comerciales, conforme a lo estipulado en el artículo**

**°**
**14 del D.S. N** **40/2012 MMA** . “Los proponentes no podrán, a sabiendas, fraccionar sus proyectos o actividades
con el objeto de variar el instrumento de evaluación o de eludir el ingreso al Sistema de Evaluación de Impacto
Ambiental. Corresponderá a la Superintendencia determinar la infracción a esta obligación y requerir al
proponente el ingreso adecuado, previo informe del Servicio. No aplicará lo señalado en el inciso anterior cuando
el proponente acredite que el proyecto o actividad corresponde a uno cuya ejecución se realizará por etapas,
aplicándose en todo caso lo establecido en el artículo 11 ter de la Ley. Los Estudios y Declaraciones de Impacto
Ambiental deberán indicar expresamente si sus proyectos o actividades se desarrollarán por etapas. En tal caso,
deberá incluirse una descripción somera de tales etapas, indicando para cada una de ellas el objetivo y las razones
o circunstancias de que dependen, así como las obras o acciones asociadas y su duración estimada.” La primera
etapa contempla la construcción de 1 edificio, estacionamientos, urbanización (áreas verdes, veredas, solución de
aguas lluvias, conexión de agua potable y alcantarillado etc.), vialidad interna de las etapas 1 y 4 y además portería,
sala de seguridad y sala de basura. La segunda etapa del Proyecto consta de 1 edificio, estacionamientos y vialidad
interna de las etapas 3 y 4, mientras que la tercera y cuarta etapa constan sólo de 1 edificio cada una.

**Etapa 1: construcción y operación del edificio 1**

**La etapa sometida a evaluación ambiental (“Edificio 1”)** consiste en la construcción y habilitación de un edificio
de consumo de energía de 5 MW y contará con un total de 7 grupos electrógenos de emergencia, de los cuales 5
grupos electrógenos de emergencia son para el respaldo de las salas de datos y 1 grupo electrógeno es utilizado
para mantenciones y/o falla de éstos equipos, todos de 3.437 KVA/2.750 kW y, además 1 grupo electrógeno de
emergencia de 500 KVA/400 kW para respaldo de áreas comunes, estos contarán con estanque (subbase) de
almacenamiento de petróleo diésel para autonomía de 48 horas a plena carga, 2 salas de datos, 28 unidades de
ventiladores tipo Crah (en el interior de las salas de datos), 5 equipos de enfriamiento tipo Chillers de 1.557 kW,
además de 6 áreas de transformadores, 5 áreas de baterías, bodegas de mantenimiento y almacenamientos para
distintos usos (placas, fibras ópticas, partes equipos útiles de aseo y artículos de oficina), oficina del cliente, sala
de descanso, sala de conferencia, una sala de basura, una estación de bombeo de agua potable para el control de
incendios, oficina Scala, sala de seguridad, control de acceso, portería, área de carga y descarga, 19
estacionamientos vehiculares (incluye 3 estacionamientos de 30 m2 para camiones) y 22 estacionamientos para

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_5_
_Curauma”_

bicicletas. El terreno donde se localizará el Proyecto cuenta con una superficie de terreno de 82.448,54 m2 y
tendrá una superficie construida total de 4.665,80 m2. Las superficies de ocupación de la etapa 1 corresponde a
20.768,70 m2 correspondientes a los polígonos del edificio 1 data center, estación de bombeo, sala de basura,
portería, calle, estacionamientos, veredas, áreas verdes y sala de pre-carguío graficado en el plano “CUR01-E-BAUDC01-AR00-A0-3002-R-0A” adjunto en el Anexo A-02 de la Adenda.

Figura 2. Cuadro de superficies etapa propuesta

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_6_
_Curauma”_

A continuación, (i) se describen someramente las futuras etapas eventuales (edificios data center 2, 3 y 4) que se
someterán a evaluación en su debido momento, de acuerdo a los artículos 11 bis y 11 ter de la Ley 19.300, (ii) las
razones o circunstancias que dependen de ello, (iii) las partes, obras y acciones asociadas a cada etapa y (iv) la
duración estimada de cada etapa.

**i.** **Descripción somera de las futuras etapas eventuales**

**Edificio 2 data center**

Construcción y operación de un edificio data center con un consumo de 10 MW que contará con un total de 12
grupos electrógenos de emergencia, de los cuales 10 grupos electrógenos de emergencia que serán de respaldo
para las salas de datos y 1 grupos electrógeno emergencia serán utilizados para mantenciones y/o fallas en los
equipos, todos de 3.437 KVA/2.750 kW y, además de 1 grupos electrógenos de emergencia de 500 KVA/400 kW
para cargas no esenciales, todos estos contarán con estanque (subbase) de almacenamiento de petróleo diésel
para autonomía de 48 horas a plena carga, 4 salas de datos, 56 unidades de ventiladores tipo Crah (en el interior
de las salas de datos), 10 equipos de enfriamiento tipo Chillers de 1.550 kW, 11 áreas de transformadores y 10

áreas de baterías.

**Edificio 3 data center**

Construcción y operación de un edificio data center con un consumo de 10 MW que contará con un total de 12
grupos electrógenos de emergencia, de los cuales 10 grupos electrógenos de emergencia que serán de respaldo
para las salas de datos y 1 grupos electrógeno emergencia serán utilizados para mantenciones y/o fallas en los
equipos, todos de 3.437 KVA/2.750 kW y, además de 1 grupos electrógenos de emergencia de 500 KVA/400 kW
para cargas no esenciales, todos estos contarán con estanque (subbase) de almacenamiento de petróleo diésel
para autonomía de 48 horas a plena carga, 4 salas de datos, 56 unidades de ventiladores tipo Crah (en el interior
de las salas de datos), 10 equipos de enfriamiento tipo Chillers de 1.550 kW, 11 áreas de transformadores y 10

áreas de baterías

**Edificio 4 data center**

Construcción y habilitación de un edificio data center de consumo de energía de 5 MW y contará con un total de
7 grupos electrógenos de emergencia, de los cuales 5 grupos electrógenos de emergencia son para el respaldo de
las salas de datos y 1 grupo electrógeno es utilizado para mantenciones y/o falla de éstos equipos, todos de 3.437
KVA/2.750 kW y, además 1 grupo electrógeno de emergencia de 500 KVA/400 kW para respaldo de áreas
comunes, estos contarán con estanque (subbase) de almacenamiento de petróleo diésel para autonomía de 48
horas a plena carga, 2 salas de datos, 28 unidades de ventiladores tipo Crah (en el interior de las salas de datos),
5 equipos de enfriamiento tipo Chillers de 1.557 kW, además de 6 áreas de transformadores, 5 áreas de baterías

Se estima que construcción de la 1° etapa tenga una duración de 6 meses, la fase de operación se extenderá por
25 años, y su fase de cierre tendrá una duración de 3 meses.

**3. LOCALIZACIÓN**

El Proyecto se ubica en la Av. Tupungato N°3291, N°3321 N°3371, comuna y provincia de Valparaíso,
específicamente (ROL S.I.I. N°9540-72, N°9540-73 y N°9540-74) correspondiente a correspondiente a la
habilitación de un Data Center, Región de Valparaíso.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_7_
_Curauma”_

Figura 3. Localización del Proyecto

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_8_
_Curauma”_

Fuente: Elaboración propia, 2022

Como se puede observar en la figura siguiente, el Proyecto se ubica fuera del área de aplicación del Plan de
Prevención y Descontaminación de las comunas de Concón, Quintero y Puchuncaví y del D.S. N°10/2015 donde se
declaró como zona saturada por material particulado fino respirable MP2,5, como concentración anual y, zona
latente por material particulado respirable MP10, como concentración anual a las comunas antes nombradas. En
la siguiente figura se puede ver la ubicación del Proyecto respecto del plan.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_9_
_Curauma”_

Figura 4. Ubicación del Proyecto respecto a la aplicación del D.S. N°10/2015 y PPDA de Concón, Quintero y

Puchuncaví

Fuente: Elaboración propia, 2022

**4. EMISIONES A MODELAR**

La estimación de emisiones del Proyecto se realizó aplicando los factores de emisión y fórmulas propuestas por la
Agencia de Protección Ambiental de los EE.UU. en el documento “AP-42 5th Edición”, complementando esta
información con la indicada por SEREMI de Medio Ambiente Región Metropolitana en el documento “Guía para la
Estimación de Emisiones Atmosféricas en la Región Metropolitana” (junio 2020), el que ha sido utilizado como una
referencia técnica para el cálculo de las emisiones.

A continuación, en la Tabla 2 se muestra el resumen de las emisiones de material particulado sedimentable (MPS),
material particulado respirable (MP10), material particulado fino respirable (MP2,5), en el modelo como óxidos de
nitrógeno (NOx), monóxido de carbono (CO) y óxidos de azufre (SOx). Es importante señalar que para evaluar el
impacto de las emisiones se han considerado 3 escenarios:

1. Emisiones generadas en el año 1 correspondiente a la fase de construcción,
2. Emisiones generadas desde 2 al 25 correspondiente a la fase de operación de la etapa propuesta y,

finalmente

3. Las emisiones generadas cuando el Proyecto se encuentre operando totalmente, es decir, con la etapa

propuesta y las tres etapas futuras funcionando simultáneamente.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_10_
_Curauma”_

Es importante destacar que, las emisiones que se modelaron son las emisiones que se generan al interior del área de Proyecto. Estas se muestran a continuación.

Tabla 1. Resumen de emisiones por actividad, Fase de Construcción - Escenario 1

|Fase|Actividades|Emisiones Atmosféricas del Proyecto<br>(ton/año)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Fase|Actividades|CO|SOX|NOX|MP2,5 comb|MP10 comb|MP2,5 resus|MP10 resus|MP2,5 total|MP10 total|MPS|
|Construcción|Compactación|0,0000|0,0000|0,0000|0,0000|0,0000|0,0017|0,0034|0,0017|0,0034|0,0164|
|Construcción|Excavación|0,0000|0,0000|0,0000|0,0000|0,0000|0,0394|0,0768|0,0394|0,0768|0,3756|
|Construcción|Transferencia de material|0,0000|0,0000|0,0000|0,0000|0,0000|0,0013|0,0086|0,0013|0,0086|0,0183|
|Construcción|Erosión de material en acopio|0,0000|0,0000|0,0000|0,0000|0,0000|0,0001|0,0004|0,0001|0,0004|0,0009|
|Construcción|Circulación de vehículos en caminos pavimentado interior|0,0000|0,0000|0,0000|0,0000|0,0000|0,0012|0,0052|0,0012|0,0052|0,0250|
|Construcción|Combustión vehículos|0,0054|0,0001|0,0531|0,0007|0,0007|0,0000|0,0000|0,0022|0,0007|0,0000|
|Construcción|Combustión maquinaria fuera de ruta|0,1258|0,0006|0,0671|0,0022|0,0022|0,0000|0,0000|0,0022|0,0022|0,0000|
|Construcción|**Emisión total (ton/año)**|**0,1312**|**0,0007**|**0,1202**|**0,0029**|**0,0029**|**0,0437**|**0,0944**|**0,0705**|**0,0922**|**0,4112**|

Fuente: Elaboración propia, 2022

Tabla 2. Resumen de emisiones por actividad, Fase de Operación Etapa Propuesta - Escenario 2

|Fase|Actividades|Emisiones Atmosféricas del Proyecto<br>(ton/año)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Fase|Actividades|CO|SOX|NOX|MP2,5 comb|MP10 comb|MP2,5 resus|MP10 resus|MP2,5 total|MP10 total|MPS|
|Operación<br>Etapa 1|Circulación de vehículos en caminos pavimentado|0,0000|0,0000|0,0000|0,0000|0,0000|0,0056|0,0251|0,0056|0,0251|0,1206|
|Operación<br>Etapa 1|Combustión vehículos|0,0066|0,0002|0,0282|0,0002|0,0002|0,0000|0,0000|0,0002|0,0002|0,0000|
|Operación<br>Etapa 1|Grupo Electrógeno|0,0129|0,0000|2,0991|0,0224|0,0224|0,0000|0,0000|0,0224|0,0224|0,0000|
|Operación<br>Etapa 1|**Emisión total (ton/año)**|**0,0195**|**0,0002**|**2,1273**|**0,0226**|**0,0226**|**0,0056**|**0,0251**|**0,0282**|**0,0477**|**0,1206**|

Fuente: Elaboración propia, 2022

Tabla 3. Resumen de emisiones por actividad, Fase de Operación Proyecto Total - Escenario 3

|Fase|Actividades|Emisiones Atmosféricas del Proyecto<br>(ton/año)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Fase|Actividades|CO|SOX|NOX|MP2,5 comb|MP10 comb|MP2,5 resus|MP10 resus|MP2,5 total|MP10 total|MPS|
|Operación<br>Proyecto<br>Total|Circulación de vehículos en caminos pavimentado|0,0000|0,0000|0,0000|0,0000|0,0000|0,0336|0,1506|0,0336|0,1506|0,7236|
|Operación<br>Proyecto<br>Total|Combustión vehículos|0,0396|0,0011|0,1692|0,0012|0,0012|0,0000|0,0000|0,0012|0,0012|0,0000|
|Operación<br>Proyecto<br>Total|Grupo Electrógeno|0,0774|0,0000|12,5946|0,1344|0,1344|0,0000|0,0000|0,1344|0,1344|0,0000|
|Operación<br>Proyecto<br>Total|**Emisión total (ton/año)**|**0,1172**|**0,0011**|**12,7641**|**0,1356**|**0,1356**|**0,0336**|**0,1506**|**0,1694**|**0,2865**|**0,7238**|

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_11_
_Curauma”_

**5. MODELACIÓN DE EMISIONES ATMOSFÉRICAS**

**5.1. Marco legal**

La siguiente modelación determinará el efecto en las cercanías del Proyecto, producto de las emisiones de Material Particulado Respirable (MP10), Fino (MP2,5) y los gases
generados por las actividades asociadas a la fase de Operación del Proyecto.

En el contexto legal, existen normas primarias y secundarias asociadas a los contaminantes de las emisiones atmosféricas generadas en el Proyecto. Los estadísticos a evaluar
se presentan en la Tabla 4:

Tabla 4. Normas de Calidad del Aire consideradas en el estudio

|Parámetro|Norma|Estadístico|Limite según Norma|Unidad|Referencia|
|---|---|---|---|---|---|
|MP10|Primaria|Promedio Anual1|50|(~~~~g/m3)|D.S. N° 59 / 1998 MINSEGPRES|
|MP10|Primaria|Percentil 98 promedio diario|150|(g/m3)|(g/m3)|
|MP2,5|Primaria|Promedio Anual|20|(g/m3)|D.S. N° 12/2011 del MMA|
|MP2,5|Primaria|Percentil 98 promedio diario|50|(g/m3)|(g/m3)|
|NO2|Primaria|Promedio Anual|100|(g/m3)|D.S. N° 114/ 2002 MINSEGPRES|
|NO2|Primaria|Percentil 99 máx. 1 hora|400|(g/m3)|(g/m3)|
|CO|Primaria|Percentil 99 1 hora|30|(mg/m3)|D.S. N° 115/2002 del MINSEGPRES|
|CO|Primaria|Percentil 99 8 hora|10|(mg/m3) <br>|(mg/m3) <br>|
|SO2|Primaria|Promedio Anual|60|(~~~~g/m3)|D.S. N° 104/ 2018 MMA|
|SO2|Primaria|Percentil 99 24 horas|150|(g/m3)|(g/m3)|
|SO2|Primaria|Percentil 98,5 1 hora|350|(g/m3)|(g/m3)|
|SO2 (**)|Secundaria|Promedio Anual2|365|(g/m3)|D.S. N°22/2010 MINSEGPRES|
|SO2 (**)|Secundaria|Percentil 98 promedio diario|80|(g/m3)|(g/m3)|
|MPS (*)|Secundaria|Promedio Anual3|200|(g/m3)|Norma Suiza|

(*) Norma Secundaria de Calidad del Aire del Ambiente de la Confederación Suiza.

(**) Norma Secundario de Calidad del Aire para Anhídrido Sulfuroso. Valores de la zona norte del país

Fuente: Elaboración propia, 2022

1 Aplicable al promedio anual de tres años consecutivos.
2 Aplicable al promedio anual de tres años consecutivos.
3 Aplicable al promedio anual de tres años consecutivos.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_12_
_Curauma”_

**5.2. Ecuación general para el cálculo de emisiones**

Para establecer la línea de base de calidad del aire del Proyecto, se realizó una recopilación de la información pública
para lo cual y de acuerdo a la ubicación del Proyecto y lo disponible en el Sistema de Información Nacional de Calidad
del Aire (SINCA), se considerará lo presentado en la estación Valparaíso (Ministerio de Medio Ambiente), siendo la
estación más cercana al Proyecto.

La caracterización de la calidad del aire se realizó sobre el contaminante, MP2,5, y su análisis se llevó a cabo mediante
la comparación de los registros recopilados con las normas de calidad del aire establecidas por la legislación vigente
y normas de referencia cuando corresponde. Es importante señalar que en la estación Valparaíso no se encuentran
disponibles los datos de MP 10, SO 2, NO 2 y CO.

En la Tabla 5 se presentan las coordenadas de ubicación de la estación y los parámetros que se miden en ella.

Tabla 5. Contaminante que constituye la Línea de base de Calidad de aire y ubicación de la Estación de monitoreo

|Estación|Coordenadas UTM WGS84 (Huso 19)|Col3|Contaminante|Periodo|Administrada por|
|---|---|---|---|---|---|
|Estación|Este (m)|Norte (m)|Norte (m)|Norte (m)|Norte (m)|
|Valparaíso|255.891|6.340.183|MP2,5|2019-2021|MMA|

Fuente: Elaboración propia, 2022

La Figura 5 presenta la ubicación de la estación de monitoreo de calidad del aire considerada en la presente línea de
base.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_13_
_Curauma”_

Figura 5. Ubicación de la Estación de monitoreo de Calidad de aire

Fuente: Elaboración propia, 2022

**5.3. Resultados y Análisis**

Para caracterizar la línea de base de calidad del aire en el Área de Influencia del Proyecto, se consideraron las
mediciones de MP2,5 monitoreadas en la estación de calidad del aire anteriormente mencionada. A continuación,
en la Tabla 6, se presenta el resumen estadístico de los registros de Calidad del Aire disponibles en el entorno del
Proyecto.

Tabla 6. Resumen de concentraciones (μg/m [3] N)

|Contaminante|Estadístico|Estación Valparaíso|Limite según Norma|% de la Norma|
|---|---|---|---|---|
|MP2,5|Promedio Anual1|14|20|68,2|
|MP2,5|Percentil 98 promedio diario|35|50|70,2|

Fuente: Elaboración propia, 2022

Como se observa en la tabla anterior, las concentraciones de MP2,5 no alcanzan el nivel de saturación ni latencia
para la norma diaria y anual.

Se reitera que los contaminantes MP10 y gases (CO, NO2 y SO2), no están disponibles para análisis en la plataforma

del SINCA.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_14_
_Curauma”_

**5.4 Descripción y justificación del modelo**

El modelo utilizado para este análisis es el SCREEN 3 de la United States Environmental Protection Agency (USEPA).
Este modelo nos permite determinar el aporte de las emisiones provenientes de fuentes emisoras, en localidades y
sectores aledaños a las instalaciones del Proyecto, permitiendo de este modo asignar las cuotas de responsabilidad
en los niveles de calidad del aire proyectados en su entorno.

El modelo SCREEN 3, se desarrolló como una herramienta para realizar estimaciones de concentraciones de
contaminantes, tomando como base el documento de procedimientos de proyección de la USEPA, utilizando un
modelo de dispersión Gaussiano que incorpora factores relacionados a la fuente emisora y factores meteorológicos
para estimar concentraciones de contaminantes de fuentes continuas. Se asume que el contaminante no sufre
reacciones químicas y que la pluma no es afectada por procesos de remoción, como deposición seca o húmeda,
durante su transporte desde la fuente. Las variables de entrada introducidas al modelo, incluyen características de
la fuente y la tasa de emisión correspondiente a cada contaminante a evaluar.

Cabe destacar que el modelo SCREEN 3 siempre entrega como resultado concentraciones ambientales
sobreestimadas, debido a que genera internamente la condición meteorológica más desfavorable, es decir, aquella
con la que se obtiene la concentración ambiental más alta, considerando además que el diseño del modelo ubica al
receptor recibiendo el viento directo de las fuentes y no considerando factores atenuadores como la topografía. Por
lo anterior, la estimación con SCREEN 3, establece un techo o valor máximo, que en la práctica nunca ocurre, por lo
que las concentraciones reales en un punto determinado son siempre menores a las estimadas por este modelo.

**5.5 Fuentes de emisión**

La modelación de las emisiones producto de la construcción (Escenario 1), operación de la etapa propuesta
(Escenario 2) y operación del Proyecto total (Escenario 3) en estudio, se realizó considerando la dispersión del
material particulado MPS, MP 10 y MP 2,5 presentes en las emisiones por resuspensión y combustión, así como los
Gases, CO, NO X y SO X, producto de la combustión en las fuentes estacionarias y móviles, asociadas a las actividades
del proyecto por cada escenario.

Además, se consideraron las emisiones anuales asociadas a las fuentes emisoras de contaminantes del Proyecto (ver
Tabla 2, Tabla 2 y Tabla 3), producidas en toda la superficie del sitio del proyecto. El resultado de las emisiones
generadas espacial y temporalmente, se presenta en la tabla que se muestra a continuación.

Tabla 7. Tasas de emisiones del Proyecto, Fase construcción - Escenario 1

|Emisiones|CO|SO<br>x|NO<br>X|MP<br>2,5 Total|MP<br>10 Total|MPS<br>l|
|---|---|---|---|---|---|---|
|ton/año|0,1312|0,0007|0,1202|0,0705|0,0922|0,4112|
|g/m2-s|**0,0000004475**|**0,0000000024**|**0,0000004097**|**0,0000002402**|**0,0000003144**|**0,0000014019**|

Fuente: Elaboración propia, 2022

Tabla 8. Tasas de emisiones del Proyecto, Fase operación Etapa propuesta - Escenario 2

|Emisiones|CO|SO<br>x|NO<br>X|MP<br>2,5 Total|MP<br>10 Total|MPS<br>l|
|---|---|---|---|---|---|---|
|ton/año|0,0195|0,0002|2,1273|0,0282|0,0477|0,1206|
|g/m2-s|**0,0000000666**|**0,0000000006**|**0,0000072535**|**0,0000000963**|**0,0000001628**|0,0000004113|

Fuente: Elaboración propia, 2022

Tabla 9. Tasas de emisiones del Proyecto, Fase operación Proyecto total - Escenario 3

|Emisiones|CO|SO<br>x|NO<br>X|MP<br>2,5 Total|MP<br>10 Total|MPS<br>l|
|---|---|---|---|---|---|---|
|ton/año|0,1172|0,0011|12,7641|0,1694|0,2865|0,7238|
|g/m2-s|**0,0000000743**|**0,0000000007**|**0,0000080949**|**0,0000001075**|**0,0000001817**|**0,0000004591**|

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_15_
_Curauma”_

Cabe destacar, que las tasas de emisión presentadas en la tabla anterior, corresponde al total de las emisiones
generadas por el proyecto, por lo que se está considerando que todas las actividades se realizan al mismo tiempo,
por lo tanto, los valores entregados representan el escenario de emisión más desfavorable para las fuentes descritas.

A su vez, para efectos de la modelación, en el sector más cercano al área del proyecto se identificaron potenciales
receptores humanos y recursos naturales (Ver Figura 6). Estos potenciales receptores son los puntos de actividades
productivas más cercanos los cuales correspondes a Galpón Chilexpress, Galpón Sitrans, Galpón Audiopro, Galpón
Centro Comercial y Reserva Lago Peñuelas. Sin embargo, se considerará la distancia del Punto de Máxima
Concentración (PMC) proyectada desde la fuente de emisión, para realizar el análisis de cumplimiento de las normas

de referencia de calidad del aire.

En la siguiente tabla y figura se presentan las coordenadas de los receptores considerados en el análisis de la

modelación.

Tabla 10. Coordenadas de los receptores del Proyecto

|Nombre|Tipo de receptor|Coordenadas UTM WGS84 (Huso 19)|Col4|Distancia aproximada al área<br>del Proyecto|
|---|---|---|---|---|
|Nombre|Tipo de receptor|Este (m)|Norte (m)|Norte (m)|
|Receptor 1|Humano|261.403|6.330.734|52|
|Receptor 2|Humano|261.468|6.330.465|83|
|Receptor 3|Humano|261.092|6.330.389|0|
|Receptor 4|Humano|261.142|6.330.595|0|
|Receptor 5|Recurso natural (Reserva Lago Peñuelas)|<br>261222|6330175|120|

Fuente: Elaboración propia, 2022

Figura 6. Ubicación de los potenciales receptores de norma primaria y secundaria

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_16_
_Curauma”_

Fuente: Elaboración propia, 2022

**5.6 Resultados de la modelación**

5.6.1 Fase de construcción

La modelación de la dispersión de las emisiones de los distintos contaminantes, fue considerada como fuentes de
área, y se realizó estableciendo como datos de entrada las siguientes opciones que permite el modelo.

Tabla 11. Datos de entrada del modelo

|Parámetro|Datos de entrada|Unidad|
|---|---|---|
|Tipo de fuente|Área|-|
|Altura de liberación|1,0|m|
|Longitud de lado largo|97|m|
|Longitud de lado corto|96|m|
|Altura del receptor|1,5|m|
|Terreno Urbano/Rural|Urbano|-|
|Altura de la mezcla|30|m|
|Altura anemométrica|5|m|
|Clase de estabilidad|3|“Semi Inestable”|
|Velocidad eólica|1,0|m/s|

Fuente: Elaboración propia, 2022

La tabla siguiente, muestra los resultados de la modelación del proyecto, con el cual se obtuvo la dispersión de las
concentraciones de los distintos contaminantes, a distancias entre 30 y 1.500 m del proyecto, con lo que se
determinó el aporte de contaminantes (concentración) sobre los potenciales receptores de interés.

Tabla 12. Resultados del modelo, Fase de construcción - Escenario 1

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Distancia (m)|CO|SOx|NOX|MP2,5 Total|MP10 Total|MPS|
|30|4,951|0,02655|4,533|2,657|3,478|15,51|
|40|5,126|0,02749|4,693|2,751|3,601|16,06|
|50|5,288|0,02836|4,841|2,838|3,72|16,57|
|60|5,439|0,02917|4,98|2,92|3,82|17,04|
|70|5,369|0,02879|4,915|2,882|3,77|16,82|
|80|3,753|0,02013|3,436|2,014|2,64|11,76|
|90|2,908|0,01559|2,662|1,561|2,04|9,109|
|100|2,395|0,01284|2,193|1,285|1,683|7,503|
|150|1,39|0,007453|1,272|0,7459|0,9764|4,354|
|200|1,103|0,005918|1,01|0,5923|0,7753|3,457|
|250|0,9385|0,005033|0,8592|0,5037|0,6593|2,94|
|300|0,8149|0,00437|0,746|0,4374|0,5725|2,553|
|350|0,7193|0,003857|0,6585|0,3861|0,5053|2,253|
|400|0,6437|0,003452|0,5893|0,3455|0,4522|2,016|
|450|0,5828|0,003125|0,5335|0,3128|0,4094|2,826|
|500|0,5328|0,002858|0,4878|0,286|0,3743|1,669|
|600|0,4557|0,002444|0,4173|0,2446|0,3202|1,428|
|700|0,3991|0,002141|0,3654|0,2142|0,2804|1,25|
|800|0,3561|0,00191|0,326|0,1911|0,2502|1,116|
|900|0,3221|0,001728|0,2949|0,1729|0,2263|1,009|
|1000|0,2948|0,001581|0,2699|0,1582|0,2071|0,9234|
|1500|0,2112|0,001133|0,1933|0,1133|0,1484|0,6615|

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_17_
_Curauma”_

Fuente: Elaboración propia, 2022

El resultado de las máximas concentraciones horarias (μg/m3) arrojadas por el modelo, se presentan en la Tabla 13
que se muestra a continuación.

Tabla 13. Máximas concentraciones horarias obtenidas del modelo

|Lugar|Distancia máx,<br>concentración (m)|Concentración horaria (g/m3)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Lugar<br>|Distancia máx,<br>concentración (m)|<br>CO|SOx|NOX|MP2,5 Total|MP10 Tota|MPS|
|Proyecto|60|5,439|0,02917|4,98|2,92|3,82|17,04|

Fuente: Elaboración propia, 2022

Es necesario destacar que el modelo entrega concentraciones a nivel horario, las que son convertidas a
concentraciones de 3 h, 8 h, 24 h o anuales, de acuerdo a los factores de conversión establecidos por la EPA [4] y que
se presentan en la siguiente tabla.

Tabla 14. Factores de conversión para promedios máximos de concentración

|Tiempo promedio|Factor conversión|
|---|---|
|3 horas|0,9|
|8 horas|0,7|
|24 horas|0,4|
|Anual|0,08|

Fuente: Screening Procedures for Estimating the Air Quality Impact of Stationary Sources (USEPA 1992).

Para evaluar el nivel de cumplimiento de la normativa ambiental con respecto al material particulado, se ha
considerado como referencia el D.S. N° 59/98, del Ministerio del Ministerio Secretaría General de la Presidencia, que
establece la Norma de Calidad Primaria para Material Particulado Respirable MP10, en especial los valores que
definen situaciones de emergencia, la cual se comparó con la concentración máxima aportada por el proyecto.

Para los gases NOX se ha considerado como referencia el D.S. N° 114 del Ministerio Secretaría General de la
Presidencia, que establece la Norma de Calidad Primaria de Aire para Dióxido de Nitrógeno (NO2), A su vez, para el
contaminante SOX se ha considerado como referencia el D.S. N°104 del Ministerio de Medio Ambiente, que establece
la Norma de Calidad Primaria de Aire para Dióxido de Azufre (SO2). Finalmente, para el contaminante CO se ha
utilizado el D.S. N°115 de Ministerio Secretaría General de la Presidencia, que establece la Norma de Calidad Primaria
de Aire para Monóxido de Carbono (CO).

Respecto a las Normas Secundarias de Calidad del Aire se consideró la norma para Anhídrido Sulfuroso (valores de la
zona norte del país) y la norma de la Confederación Suiza.

A continuación, se presenta el análisis de cumplimiento de las normas de referencia de calidad del aire, respecto de
la concentración máxima para los contaminantes indicados anteriormente en la Tabla 13, la cual se presentará a una
distancia de 60 m del Proyecto.

4 Screening Procedures for Estimating the Air Quality Impact of Stationary Sources. U.S. Environmental Protection Agency (USEPA). Octubre de

1992. Pp 39.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_18_
_Curauma”_

Tabla 15. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Construcción - Escenario 1

|Parámetro|Estadístico|Máxima del<br>proyecto<br>(g/m3N)|Limite según<br>Norma<br>(g/m3)|Porcentaje<br>respecto de la<br>Norma (%)|Referencia|
|---|---|---|---|---|---|
|MP10|Concentración 24 horas|1,53|150|1,0|D.S. N° 59 / 1998 MINSEGPRES|
|MP10|Concentración anual|0,31|50|0,6|0,6|
|MP2,5|Concentración 24 horas|1,17|50|2,3|D.S. N° 12/2011 del MMA|
|MP2,5|Concentración anual|0,23|20|1,2|1,2|
|NOx|Concentración 1 hora|4,98|400|1,2|D.S. N° 114/ 2002 MINSEGPRES|
|NOx|Concentración anual|0,40|100|0,4|0,4|
|SO2|Concentración 1 hora|0,03|350|0,008|D.S. N° 104/ 2018 MMA|
|SO2|Concentración 24 horas|0,012|150|0,008|0,008|
|SO2|Concentración anual|0,002|60|0,004|0,004|
|CO|Concentración 1 hora|5,44|30.000|0,018|~~D~~.S. N° 115/2002 del MINSEGPRES|
|CO|Concentración 8 horas|3,81|10.000|0,038|0,038|
|MPS (*)|Concentración anual|1,36|200|0,7|Norma Suiza|
|SO2 (**)|Concentración 24 horas|0,012|365|0,003|D.S. N°22/2010 MINSEGPRES|
|SO2 (**)|Concentración anual|0,002|80|0,003|0,003|

(*) Norma Secundaria de Calidad del Aire del Ambiente de la Confederación Suiza.

(**) Norma Secundario de Calidad del Aire para Anhídrido Sulfuroso. Valores de la zona norte del país

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_19_
_Curauma”_

Al respecto, las concentraciones máximas en el área del proyecto se encontrarán muy por debajo de los límites de concentración establecidos por sus correspondientes
normas de referencia, por lo que el aporte de emisiones a los potenciales receptores será igualmente bajo, aun considerando el efecto sinérgico por la operación simultánea
de todas las actividades del proyecto durante su fase de construcción en el año 1.

Tabla 16. Concentraciones por distancia de los contaminantes analizados, Fase de Construcción - Escenario 1

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Distancia (m)|CO <br>(1 hora)|CO <br>(8 horas)|SOx <br>(1 hora)|SOx <br>(24 horas)|SOx <br>(Anual)|NOX <br>(1 hora)|NOx <br>(Anual)|MP2,5 Total<br>(24 horas)|MP2,5 Total<br>(Anual)|MP10 Total<br>(24 horas)|MP10 Total<br>(Anual)|MPS <br>(Anual)|
|30|4,951|3,466|0,027|0,011|0,002|4,533|0,363|1,063|0,213|1,391|0,278|1,241|
|40|5,126|3,588|0,027|0,011|0,002|4,693|0,375|1,100|0,220|1,440|0,288|1,285|
|50|5,288|3,702|0,028|0,011|0,002|4,841|0,387|1,135|0,227|1,486|0,297|1,326|
|60*|5,439|3,807|0,029|0,012|0,002|4,980|0,398|1,168|0,234|1,529|0,306|1,363|
|70|5,369|3,758|0,029|0,012|0,002|4,915|0,393|1,153|0,231|1,509|0,302|1,346|
|80|3,753|2,627|0,020|0,008|0,002|3,436|0,275|0,806|0,161|1,055|0,211|0,941|
|90|2,908|2,036|0,016|0,006|0,001|2,662|0,213|0,624|0,125|0,817|0,163|0,729|
|100|2,395|1,677|0,013|0,005|0,001|2,193|0,175|0,514|0,103|0,673|0,135|0,600|
|150|1,39|0,973|0,007|0,003|0,001|1,272|0,102|0,298|0,060|0,391|0,078|0,348|
|200|1,103|0,772|0,006|0,002|0,000|1,010|0,081|0,237|0,047|0,310|0,062|0,277|
|250|0,9385|0,657|0,005|0,002|0,000|0,859|0,069|0,201|0,040|0,264|0,053|0,235|
|300|0,8149|0,570|0,004|0,002|0,000|0,746|0,060|0,175|0,035|0,229|0,046|0,204|
|350|0,7193|0,504|0,004|0,002|0,000|0,659|0,053|0,154|0,031|0,202|0,040|0,180|
|400|0,6437|0,451|0,003|0,001|0,000|0,589|0,047|0,138|0,028|0,181|0,036|0,161|
|450|0,5828|0,408|0,003|0,001|0,000|0,534|0,043|0,125|0,025|0,164|0,033|0,226|
|500|0,5328|0,373|0,003|0,001|0,000|0,488|0,039|0,114|0,023|0,150|0,030|0,134|
|600|0,4557|0,319|0,002|0,001|0,000|0,417|0,033|0,098|0,020|0,128|0,026|0,114|
|700|0,3991|0,279|0,002|0,001|0,000|0,365|0,029|0,086|0,017|0,112|0,022|0,100|
|800|0,3561|0,249|0,002|0,001|0,000|0,326|0,026|0,076|0,015|0,100|0,020|0,089|
|900|0,3221|0,225|0,002|0,001|0,000|0,295|0,024|0,069|0,014|0,091|0,018|0,081|
|1000|0,2948|0,206|0,002|0,001|0,000|0,270|0,022|0,063|0,013|0,083|0,017|0,074|
|1500|0,2112|0,148|0,001|0,000|0,000|0,193|0,015|0,045|0,009|0,059|0,012|0,053|

- Distancia en la que se presentará la concentración máxima de contaminantes.

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_20_
_Curauma”_

A partir de los resultados obtenidos y del análisis normativo realizado se determinó el área de influencia (AI) del
proyecto, el cual se muestra en la figura siguiente.

Figura 7. Área de influencia del Proyecto, Fase de Construcción - Escenario 1

 - CO

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_21_
_Curauma”_

 - SO2

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_22_
_Curauma”_

 - NO2

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_23_
_Curauma”_

 - MP2,5

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_24_
_Curauma”_

 - MP10

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_25_
_Curauma”_

 - MPS

Fuente: Elaboración propia, 2022

Comparando los resultados de Tabla 16 con las distancias a los receptores considerados en la Tabla 10, es posible
afirmar que todos los receptores se encuentran fuera del área de influencia del Proyecto y punto de máximo impacto
de este. Adicionalmente a lo anterior tal como se mencionó, las concentraciones de contaminantes en el aire que se
producen por causa de las emisiones del proyecto durante la fase de construcción, no son significativas, por cuanto
se encuentran muy por debajo del límite establecido por las normativas de referencia, tal como se presentó en la
Tabla 15, y no generan un impacto negativo sobre la calidad del aire.

En consecuencia, no se requeriría utilizar un modelo más complejo y los resultados son concluyentes, por cuanto
indican que las emisiones del Proyecto no producirán efectos adversos significativos en la calidad del aire, aun
considerando las peores condiciones de emisión y meteorológicas.

Cabe destacar, que el modelo SCREEN 3 no entrega la opción de ingresar datos meteorológicos que sean
representativos de un sector específico. En lugar de eso, lo que hace es examinar respecto de rangos de estabilidad
y velocidades del viento, que sí pueden ser ingresados, para identificar el peor caso de condiciones meteorológicas,
es decir, la combinación de la velocidad del viento y estabilidad que resulta más desfavorable,

En el Apéndice I, del presente informe se entregan los reportes de salida del modelo utilizado, con los cuales es
posible verificar los resultados presentados en la Tabla 16 y los datos de entradas de la Tabla 11.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_26_
_Curauma”_

5.6.2 Fase de operación. Etapa propuesta

La modelación de la dispersión de las emisiones de los distintos contaminantes, fue considerada como fuentes de
área, y se realizó estableciendo como datos de entrada las siguientes opciones que permite el modelo.

Tabla 17. Datos de entrada del modelo

|Parámetro|Datos de entrada|Unidad|
|---|---|---|
|Tipo de fuente|Área|-|
|Altura de liberación|1,0|m|
|Longitud de lado largo|97|m|
|Longitud de lado corto|96|m|
|Altura del receptor|1,5|m|
|Terreno Urbano/Rural|Urbano|-|
|Altura de la mezcla|30|m|
|Altura anemométrica|5|m|
|Clase de estabilidad|3|“Semi Inestable”|
|Velocidad eólica|1,0|m/s|

Fuente: Elaboración propia, 2022

La tabla siguiente, muestra los resultados de la modelación del proyecto, con el cual se obtuvo la dispersión de las
concentraciones de los distintos contaminantes, a distancias entre 30 y 1.500 m del proyecto, con lo que se
determinó el aporte de contaminantes (concentración) sobre los potenciales receptores de interés.

Tabla 18. Resultados del modelo, Fase de operación Etapa propuesta - Escenario 2

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Distancia (m)|CO|SOx|NOX|MP2,5 Total|MP10 Total|MPS|
|30|0,7368|0,006638|80,25|1,065|1,801|4,55|
|40|0,7629|0,006873|83,09|1,103|1,865|4,711|
|50|0,787|0,00709|85,71|1,138|1,924|4,86|
|60|0,8095|0,007293|88,17|1,171|1,979|4,999|
|70|0,799|0,007198|87,02|1,155|1,95|4,935|
|80|0,5585|0,005032|60,83|0,8076|1,37|3,449|
|90|0,4328|0,003899|47,13|0,6257|1,06|2,673|
|100|0,3564|0,003211|38,82|0,5154|0,8713|2,201|
|150|0,2068|0,001863|22,53|0,2991|0,5056|1,277|
|200|0,1642|0,00148|17,89|0,2375|0,4014|1,014|
|250|0,1397|0,001258|15,21|0,202|0,3414|0,8626|
|300|0,1213|0,001093|13,21|0,1754|0,2965|0,749|
|350|0,107|0,0009644|11,66|0,1548|0,2617|0,6611|
|400|0,09579|0,000863|10,43|0,1385|0,2342|0,5916|
|450|0,08673|0,0007814|9,446|0,1254|0,212|0,5356|
|500|0,0793|0,0007144|8,636|0,1147|0,1938|0,4897|
|600|0,06783|0,0006111|7,387|0,09808|0,1658|0,4189|
|700|0,0594|0,0005352|6,47|0,08589|0,1452|0,3669|
|800|0,05299|0,0004774|5,772|0,07663|0,1295|0,3273|
|900|0,04794|0,0004319|5,221|0,06932|0,1172|0,2961|
|1000|0,04387|0,0003952|4,778|0,06343|0,1072|0,2709|
|1500|0,03143|0,0002831|3,423|0,04544|0,07682|0,1941|

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_27_
_Curauma”_

El resultado de las máximas concentraciones horarias (μg/m3) arrojadas por el modelo, se presentan en la Tabla 13
que se muestra a continuación.

Tabla 19. Máximas concentraciones horarias obtenidas del modelo. Fase operación, Etapa propuesta - Escenario 2

|Lugar|Distancia máx,<br>concentración (m)|Concentración horaria (g/m3)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Lugar<br>|Distancia máx,<br>concentración (m)|<br>CO|SOx|NOX|MP2,5 Total|MP10 Tota|MPS|
|Proyecto|60|0,8095|0,007293|88,17|1,171|1,979|4,999|

Fuente: Elaboración propia, 2022

Como se mencionó anteriormente, es necesario destacar que el modelo entrega concentraciones a nivel horario, las
que son convertidas a concentraciones de 3 h, 8 h, 24 h o anuales, de acuerdo a los factores de conversión
establecidos por la EPA [5] y que se presentan en la siguiente tabla.

Tabla 20. Factores de conversión para promedios máximos de concentración

|Tiempo promedio|Factor conversión|
|---|---|
|3 horas|0,9|
|8 horas|0,7|
|24 horas|0,4|
|Anual|0,08|

Fuente: Screening Procedures for Estimating the Air Quality Impact of Stationary Sources (USEPA 1992).

Para evaluar el nivel de cumplimiento de la normativa ambiental con respecto al material particulado, se ha
considerado como referencia el D.S. N° 59/98, del Ministerio del Ministerio Secretaría General de la Presidencia, que
establece la Norma de Calidad Primaria para Material Particulado Respirable MP10, en especial los valores que
definen situaciones de emergencia, la cual se comparó con la concentración máxima aportada por el proyecto.

Para los gases NOX se ha considerado como referencia el D.S. N° 114 del Ministerio Secretaría General de la
Presidencia, que establece la Norma de Calidad Primaria de Aire para Dióxido de Nitrógeno (NO2), A su vez, para el
contaminante SOX se ha considerado como referencia el D.S. N°104 del Ministerio de Medio Ambiente, que establece
la Norma de Calidad Primaria de Aire para Dióxido de Azufre (SO2). Finalmente, para el contaminante CO se ha
utilizado el D.S. N°115 de Ministerio Secretaría General de la Presidencia, que establece la Norma de Calidad Primaria
de Aire para Monóxido de Carbono (CO).

Respecto a las Normas Secundarias de Calidad del Aire se consideró la norma para Anhídrido Sulfuroso (valores de la
zona norte del país) y la norma de la Confederación Suiza.

A continuación, se presenta el análisis de cumplimiento de las normas de referencia de calidad del aire, respecto de
la concentración máxima para los contaminantes indicados anteriormente en la Tabla 13, la cual se presentará a una
distancia de 60 m del Proyecto.

5 Screening Procedures for Estimating the Air Quality Impact of Stationary Sources. U.S. Environmental Protection Agency (USEPA). Octubre de

1992. Pp 39.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_28_
_Curauma”_

Tabla 21. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Operación Etapa PropuestaEscenario 2

|Parámetro|Estadístico|Máxima del<br>proyecto<br>(g/m3N)|Limite según<br>Norma<br>(g/m3)|Porcentaje<br>respecto de la<br>Norma (%)|Referencia|
|---|---|---|---|---|---|
|MP10|Concentración 24 horas|0,8|150|0,5|D.S. N° 59 / 1998 MINSEGPRES|
|MP10|Concentración anual|0,2|50|0,3|0,3|
|MP2,5|Concentración 24 horas|0,5|50|0,9|D.S. N° 12/2011 del MMA|
|MP2,5|Concentración anual|0,1|20|0,5|0,5|
|NOx|Concentración 1 hora|88,2|400|22,0|D.S. N° 114/ 2002 MINSEGPRES|
|NOx|Concentración anual|7,1|100|7,1|7,1|
|SO2|Concentración 1 hora|0,01|350|0,002|D.S. N° 104/ 2018 MMA|
|SO2|Concentración 24 horas|0,003|150|0,002|0,002|
|SO2|Concentración anual|0,001|60|0,001|0,001|
|CO|Concentración 1 hora|0,8|30.000|0,003|~~D~~.S. N° 115/2002 del MINSEGPRES|
|CO|Concentración 8 horas|0,6|10.000|0,006|0,006|
|MPS (*)|Concentración anual|0,6|200|0,284|Norma Suiza|
|SO2 (**)|Concentración 24 horas|0,003|365|0,001|D.S. N°22/2010 MINSEGPRES|
|SO2 (**)|Concentración anual|0,001|80|0,001|0,001|

(*) Norma Secundaria de Calidad del Aire del Ambiente de la Confederación Suiza.

(**) Norma Secundario de Calidad del Aire para Anhídrido Sulfuroso. Valores de la zona norte del país

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_29_
_Curauma”_

Al respecto, las concentraciones máximas en el área del proyecto se encontrarán muy por debajo de los límites de concentración establecidos por sus correspondientes
normas de referencia, por lo que el aporte de emisiones a los potenciales receptores será igualmente bajo, aun considerando el efecto sinérgico por la operación simultánea
de todas las actividades del proyecto durante su fase de operación desde el año 2 al año 25.

Tabla 22. Concentraciones por distancia de los contaminantes analizados, Fase de Operación Etapa Propuesta - Escenario 2

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Distancia (m)|CO <br>(1 hora)|CO <br>(8 horas)|SOx <br>(1 hora)|SOx <br>(24 horas)|SOx <br>(Anual)|NOX <br>(1 hora)|NOx <br>(Anual)|MP2,5 Total<br>(24 horas)|MP2,5 Total<br>(Anual)|MP10 Total<br>(24 horas)|MP10 Total<br>(Anual)|MPSl <br>(Anual)|
|30|0,7368|0,516|0,007|0,003|0,001|80,250|6,420|0,426|0,085|0,720|0,144|0,364|
|40|0,7629|0,534|0,007|0,003|0,001|83,090|6,647|0,441|0,088|0,746|0,149|0,377|
|50|0,787|0,551|0,007|0,003|0,001|85,710|6,857|0,455|0,091|0,770|0,154|0,389|
|60*|0,8095|0,567|0,007|0,003|0,001|88,170|7,054|0,468|0,094|0,792|0,158|0,400|
|70|0,799|0,559|0,007|0,003|0,001|87,020|6,962|0,462|0,092|0,781|0,156|0,395|
|80|0,5585|0,391|0,005|0,002|0,000|60,830|4,866|0,323|0,065|0,546|0,109|0,276|
|90|0,4328|0,303|0,004|0,002|0,000|47,130|3,770|0,250|0,050|0,423|0,085|0,214|
|100|0,3564|0,249|0,003|0,001|0,000|38,820|3,106|0,206|0,041|0,349|0,070|0,176|
|150|0,2068|0,145|0,002|0,001|0,000|22,530|1,802|0,120|0,024|0,202|0,040|0,102|
|200|0,1642|0,115|0,001|0,001|0,000|17,890|1,431|0,095|0,019|0,161|0,032|0,081|
|250|0,1397|0,098|0,001|0,001|0,000|15,210|1,217|0,081|0,016|0,137|0,027|0,069|
|300|0,1213|0,085|0,001|0,000|0,000|13,210|1,057|0,070|0,014|0,119|0,024|0,060|
|350|0,107|0,075|0,001|0,000|0,000|11,660|0,933|0,062|0,012|0,105|0,021|0,053|
|400|0,09579|0,067|0,001|0,000|0,000|10,430|0,834|0,055|0,011|0,094|0,019|0,047|
|450|0,08673|0,061|0,001|0,000|0,000|9,446|0,756|0,050|0,010|0,085|0,017|0,043|
|500|0,0793|0,056|0,001|0,000|0,000|8,636|0,691|0,046|0,009|0,078|0,016|0,039|
|600|0,06783|0,047|0,001|0,000|0,000|7,387|0,591|0,039|0,008|0,066|0,013|0,034|
|700|0,0594|0,042|0,001|0,000|0,000|6,470|0,518|0,034|0,007|0,058|0,012|0,029|
|800|0,05299|0,037|0,000|0,000|0,000|5,772|0,462|0,031|0,006|0,052|0,010|0,026|
|900|0,04794|0,034|0,000|0,000|0,000|5,221|0,418|0,028|0,006|0,047|0,009|0,024|
|1000|0,04387|0,031|0,000|0,000|0,000|4,778|0,382|0,025|0,005|0,043|0,009|0,022|
|1500|0,03143|0,022|0,000|0,000|0,000|3,423|0,274|0,018|0,004|0,031|0,006|0,016|

- Distancia en la que se presentará la concentración máxima de contaminantes.

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_30_
_Curauma”_

A partir de los resultados obtenidos y del análisis normativo realizado se determinó el área de influencia (AI) del
proyecto, el cual se muestra en la figura siguiente.

Figura 8. Área de influencia del Proyecto, Fase de Operación, Etapa propuesta - Escenario 2

 - CO

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_31_
_Curauma”_

 - SO2

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_32_
_Curauma”_

 - NO2

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_33_
_Curauma”_

 - MP2,5

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_34_
_Curauma”_

 - MP10

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_35_
_Curauma”_

 - MPS

Fuente: Elaboración propia, 2022

Comparando los resultados de Tabla 16 con las distancias a los receptores considerados en la Tabla 10, es posible
afirmar que todos los receptores se encuentran fuera del área de influencia del Proyecto y punto de máximo impacto
de este. Adicionalmente a lo anterior tal como se mencionó, las concentraciones de contaminantes en el aire que se
producen por causa de las emisiones del proyecto durante la fase de construcción, no son significativas, por cuanto
se encuentran muy por debajo del límite establecido por las normativas de referencia, tal como se presentó en la
Tabla 15, y no generan un impacto negativo sobre la calidad del aire.

En consecuencia, no se requeriría utilizar un modelo más complejo y los resultados son concluyentes, por cuanto
indican que las emisiones del Proyecto no producirán efectos adversos significativos en la calidad del aire, aun
considerando las peores condiciones de emisión y meteorológicas.

Cabe destacar, que el modelo SCREEN 3 no entrega la opción de ingresar datos meteorológicos que sean
representativos de un sector específico. En lugar de eso, lo que hace es examinar respecto de rangos de estabilidad
y velocidades del viento, que sí pueden ser ingresados, para identificar el peor caso de condiciones meteorológicas,
es decir, la combinación de la velocidad del viento y estabilidad que resulta más desfavorable,

En el Apéndice I, del presente informe se entregan los reportes de salida del modelo utilizado, con los cuales es
posible verificar los resultados presentados en la Tabla 16 y los datos de entradas de la Tabla 11.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_36_
_Curauma”_

5.6.3 Fase de operación. Proyecto total

La modelación de la dispersión de las emisiones de los distintos contaminantes, fue considerada como fuentes de
área, y se realizó estableciendo como datos de entrada las siguientes opciones que permite el modelo.

Tabla 23. Datos de entrada del modelo

|Parámetro|Datos de entrada|Unidad|
|---|---|---|
|Tipo de fuente|Área|-|
|Altura de liberación|1,0|m|
|Longitud de lado largo|240|m|
|Longitud de lado corto|210|m|
|Altura del receptor|1,5|m|
|Terreno Urbano/Rural|Urbano|-|
|Altura de la mezcla|30|m|
|Altura anemométrica|5|m|
|Clase de estabilidad|3|“Semi Inestable”|
|Velocidad eólica|1,0|m/s|

Fuente: Elaboración propia, 2022

La tabla siguiente, muestra los resultados de la modelación del proyecto, con el cual se obtuvo la dispersión de las
concentraciones de los distintos contaminantes, a distancias entre 50 y 1.500 m del proyecto, con lo que se
determinó el aporte de contaminantes (concentración) sobre los potenciales receptores de interés.

Tabla 24. Resultados del modelo, Fase de operación Proyecto total - Escenario 3

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Distancia (m)|CO|SOx|NOX|MP2,5 Total|MP10 Total|MPS|
|50|1,084|0,01022|118,2|1,569|2,652|6,701|
|60|1,106|0,01042|120,5|1,6|2,704|6,833|
|70|1,127|0,01062|122,8|1,631|2,756|6,964|
|80|1,15|0,01083|125,3|1,664|2,812|7,106|
|90|1,172|0,01104|127,7|1,695|2,865|7,24|
|100|1,193|0,01124|130|1,727|2,918|7,374|
|110|1,215|0,01145|132,4|1,758|2,971|7,507|
|120|1,237|0,01165|134,7|1,789|3,025|7,642|
|130|1,259|0,01186|137,1|1,821|3,078|7,776|
|140|1,28|0,01206|139,5|1,852|3,131|7,911|
|150|1,301|0,01226|141,7|1,882|3,182|8,039|
|160|1,324|0,01248|144,3|1,916|3,239|8,184|
|170|1,042|0,009819|113,5|1,508|2,549|6,44|
|180|0,8899|0,008384|96,95|1,288|2,176|5,499|
|190|0,7992|0,007529|87,07|1,156|1,954|4,938|
|200|0,7395|0,006967|80,57|1,07|1,808|4,569|
|250|0,6086|0,005734|66,3|0,8805|1,488|3,76|
|300|0,5583|0,00526|60,83|0,8078|1,365|3,45|
|350|0,5187|0,004887|56,51|0,7504|1,268|3,205|
|400|0,4827|0,004548|52,59|0,6985|1,181|2,983|
|450|0,4505|0,004244|49,08|0,6517|1,102|2,783|
|500|0,4216|0,003972|45,94|0,6101|1,031|2,605|
|1000|0,2549|0,002402|27,77|0,3688|0,6234|1,575|
|1500|0,1861|0,001753|20,28|0,2693|0,4552|1,15|

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_37_
_Curauma”_

El resultado de las máximas concentraciones horarias (μg/m3) arrojadas por el modelo, se presentan en la Tabla 13
que se muestra a continuación.

Tabla 25. Máximas concentraciones horarias obtenidas del modelo. Fase operación, Proyecto total - Escenario 3

|Lugar|Distancia máx,<br>concentración (m)|Concentración horaria (g/m3)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Lugar<br>|Distancia máx,<br>concentración (m)|<br>CO|SOx|NOX|MP2,5 Total|MP10 Tota|MPS|
|Proyecto|160|1,324|0,01248|144,3|1,916|3,239|8,184|

Fuente: Elaboración propia, 2022

Como se mencionó anteriormente, es necesario destacar que el modelo entrega concentraciones a nivel horario, las
que son convertidas a concentraciones de 3 h, 8 h, 24 h o anuales, de acuerdo a los factores de conversión
establecidos por la EPA [6] y que se presentan en la siguiente tabla.

Tabla 26. Factores de conversión para promedios máximos de concentración

|Tiempo promedio|Factor conversión|
|---|---|
|3 horas|0,9|
|8 horas|0,7|
|24 horas|0,4|
|Anual|0,08|

Fuente: Screening Procedures for Estimating the Air Quality Impact of Stationary Sources (USEPA 1992).

Para evaluar el nivel de cumplimiento de la normativa ambiental con respecto al material particulado, se ha
considerado como referencia el D.S. N° 59/98, del Ministerio del Ministerio Secretaría General de la Presidencia, que
establece la Norma de Calidad Primaria para Material Particulado Respirable MP10, en especial los valores que
definen situaciones de emergencia, la cual se comparó con la concentración máxima aportada por el proyecto.

Para los gases NOX se ha considerado como referencia el D.S. N° 114 del Ministerio Secretaría General de la
Presidencia, que establece la Norma de Calidad Primaria de Aire para Dióxido de Nitrógeno (NO2), A su vez, para el
contaminante SOX se ha considerado como referencia el D.S. N°104 del Ministerio de Medio Ambiente, que establece
la Norma de Calidad Primaria de Aire para Dióxido de Azufre (SO2). Finalmente, para el contaminante CO se ha
utilizado el D.S. N°115 de Ministerio Secretaría General de la Presidencia, que establece la Norma de Calidad Primaria
de Aire para Monóxido de Carbono (CO).

Respecto a las Normas Secundarias de Calidad del Aire se consideró la norma para Anhídrido Sulfuroso (valores de la
zona norte del país) y la norma de la Confederación Suiza.

A continuación, se presenta el análisis de cumplimiento de las normas de referencia de calidad del aire, respecto de
la concentración máxima para los contaminantes indicados anteriormente en la Tabla 13, la cual se presentará a una
distancia de 160 m del Proyecto.

6 Screening Procedures for Estimating the Air Quality Impact of Stationary Sources. U.S. Environmental Protection Agency (USEPA). Octubre de

1992. Pp 39.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_38_
_Curauma”_

Tabla 27. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Operación Proyecto totalEscenario 3

|Parámetro|Estadístico|Máxima del<br>proyecto<br>(g/m3N)|Limite según<br>Norma<br>(g/m3)|Porcentaje<br>respecto de la<br>Norma (%)|Referencia|
|---|---|---|---|---|---|
|MP10|Concentración 24 horas|1,30|150|0,9|D.S. N° 59 / 1998 MINSEGPRES|
|MP10|Concentración anual|0,26|50|0,5|0,5|
|MP2,5|Concentración 24 horas|0,77|50|1,5|D.S. N° 12/2011 del MMA|
|MP2,5|Concentración anual|0,15|20|0,8|0,8|
|NOx|Concentración 1 hora|144,30|400|36,1|D.S. N° 114/ 2002 MINSEGPRES|
|NOx|Concentración anual|11,54|100|11,5|11,5|
|SO2|Concentración 1 hora|0,01|350|0,004|D.S. N° 104/ 2018 MMA|
|SO2|Concentración 24 horas|0,005|150|0,003|0,003|
|SO2|Concentración anual|0,001|60|0,002|0,002|
|CO|Concentración 1 hora|1,32|30.000|0,004|~~D~~.S. N° 115/2002 del MINSEGPRES|
|CO|Concentración 8 horas|0,93|10.000|0,009|0,009|
|MPS (*)|Concentración anual|0,65|200|0,3|Norma Suiza|
|SO2 (**)|Concentración 24 horas|0,005|365|0,001|D.S. N°22/2010 MINSEGPRES|
|SO2 (**)|Concentración anual|0,001|80|0,001|0,001|

(*) Norma Secundaria de Calidad del Aire del Ambiente de la Confederación Suiza.

(**) Norma Secundario de Calidad del Aire para Anhídrido Sulfuroso. Valores de la zona norte del país

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_39_
_Curauma”_

Al respecto, las concentraciones máximas en el área del proyecto se encontrarán muy por debajo de los límites de concentración establecidos por sus correspondientes
normas de referencia, por lo que el aporte de emisiones a los potenciales receptores será igualmente bajo, aun considerando el efecto sinérgico por la operación simultánea
de todas las actividades del proyecto durante su fase de operación total.

Tabla 28. Concentraciones por distancia de los contaminantes analizados, Fase de Operación Proyecto total - Escenario 3

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Distancia (m)|CO <br>(1 hora)|CO <br>(8 horas)|SOx <br>(1 hora)|SOx <br>(24 horas)|SOx <br>(Anual)|NOX <br>(1 hora)|NOx <br>(Anual)|MP2,5 Total<br>(24 horas)|MP2,5 Total<br>(Anual)|MP10 Total<br>(24 horas)|MP10 Total<br>(Anual)|MPSl <br>(Anual)|
|50|1,084|0,759|0,010|0,004|0,001|118,20|9,456|0,628|0,126|1,061|0,212|0,536|
|60|1,106|0,774|0,010|0,004|0,001|120,50|9,640|0,640|0,128|1,082|0,216|0,547|
|70|1,127|0,789|0,011|0,004|0,001|122,80|9,824|0,652|0,130|1,102|0,220|0,557|
|80|1,15|0,805|0,011|0,004|0,001|125,30|10,024|0,666|0,133|1,125|0,225|0,568|
|90|1,172|0,820|0,011|0,004|0,001|127,70|10,216|0,678|0,136|1,146|0,229|0,579|
|100|1,193|0,835|0,011|0,004|0,001|130,00|10,400|0,691|0,138|1,167|0,233|0,590|
|110|1,215|0,851|0,011|0,005|0,001|132,40|10,592|0,703|0,141|1,188|0,238|0,601|
|120|1,237|0,866|0,012|0,005|0,001|134,70|10,776|0,716|0,143|1,210|0,242|0,611|
|130|1,259|0,881|0,012|0,005|0,001|137,10|10,968|0,728|0,146|1,231|0,246|0,622|
|140|1,28|0,896|0,012|0,005|0,001|139,50|11,160|0,741|0,148|1,252|0,250|0,633|
|150|1,301|0,911|0,012|0,005|0,001|141,70|11,336|0,753|0,151|1,273|0,255|0,643|
|160|1,324|0,927|0,012|0,005|0,001|144,30|11,544|0,766|0,153|1,296|0,259|0,655|
|170|1,042|0,729|0,010|0,004|0,001|113,50|9,080|0,603|0,121|1,020|0,204|0,515|
|180|0,8899|0,623|0,008|0,003|0,001|96,95|7,756|0,515|0,103|0,870|0,174|0,440|
|190|0,7992|0,559|0,008|0,003|0,001|87,07|6,966|0,462|0,092|0,782|0,156|0,395|
|200|0,7395|0,518|0,007|0,003|0,001|80,57|6,446|0,428|0,086|0,723|0,145|0,366|
|250|0,6086|0,426|0,006|0,002|0,000|66,30|5,304|0,352|0,070|0,595|0,119|0,301|
|300|0,5583|0,391|0,005|0,002|0,000|60,83|4,866|0,323|0,065|0,546|0,109|0,276|
|350|0,5187|0,363|0,005|0,002|0,000|56,51|4,521|0,300|0,060|0,507|0,101|0,256|
|400|0,4827|0,338|0,005|0,002|0,000|52,59|4,207|0,279|0,056|0,472|0,094|0,239|
|450|0,4505|0,315|0,004|0,002|0,000|49,080|3,926|0,261|0,052|0,441|0,088|0,223|
|500|0,4216|0,295|0,004|0,002|0,000|45,940|3,675|0,244|0,049|0,412|0,082|0,208|
|1000|0,2549|0,178|0,002|0,001|0,000|27,770|2,222|0,148|0,030|0,249|0,050|0,126|
|1500|0,1861|0,130|0,002|0,001|0,000|20,280|1,622|0,108|0,022|0,182|0,036|0,092|

- Distancia en la que se presentará la concentración máxima de contaminantes.

Fuente: Elaboración propia, 2022

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_40_
_Curauma”_

A partir de los resultados obtenidos y del análisis normativo realizado se determinó el área de influencia (AI) del
proyecto, el cual se muestra en la figura siguiente.

Figura 9. Área de influencia del Proyecto, Fase de Operación, Proyecto total- Escenario 3

 - CO

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_41_
_Curauma”_

 - SO2

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_42_
_Curauma”_

 - NO2

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_43_
_Curauma”_

 - MP2,5

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_44_
_Curauma”_

 - MP10

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_45_
_Curauma”_

 - MPS

Fuente: Elaboración propia, 2022

Comparando los resultados de Tabla 16 con las distancias a los receptores considerados en la Tabla 10, es posible
afirmar que los receptores humanos R1, R2, R3 y R4 se encuentran dentro del área de influencia del Proyecto y
punto de máximo impacto de este, sin embargo tal como se mencionó, las concentraciones de contaminantes en
el aire que se producen por causa de las emisiones del proyecto durante la fase de operación, considerando el
funcionamiento del Proyecto total, no son significativas, por cuanto se encuentran muy por debajo del límite
establecido por las normativas de referencia, tal como se presentó en la Tabla 15, y no generan un impacto
negativo sobre la calidad del aire.

Por otro lado, el receptor de recurso natural, Reserva Lago Peñuelas, se encuentra fuera del área de influencia, por
lo que se descarta cualquier afectación a este y a sus recursos. En la siguiente figura se muestra que la distancia
desde la obra más cercana del Proyecto hasta la Reserva es de 190 m, quedando esta fuera del AI.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_46_
_Curauma”_

Figura 10. Distancia respecto al Lago Peñuelas

Fuente: Elaboración propia, 2022

En consecuencia, no se requeriría utilizar un modelo más complejo y los resultados son concluyentes, por cuanto
indican que las emisiones del Proyecto no producirán efectos adversos significativos en la calidad del aire, aun
considerando las peores condiciones de emisión y meteorológicas.

Cabe destacar, que el modelo SCREEN 3 no entrega la opción de ingresar datos meteorológicos que sean
representativos de un sector específico. En lugar de eso, lo que hace es examinar respecto de rangos de estabilidad
y velocidades del viento, que sí pueden ser ingresados, para identificar el peor caso de condiciones meteorológicas,
es decir, la combinación de la velocidad del viento y estabilidad que resulta más desfavorable,

En el Apéndice I, del presente informe se entregan los reportes de salida del modelo utilizado, con los cuales es
posible verificar los resultados presentados en la Tabla 16 y los datos de entradas de la Tabla 11.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_47_
_Curauma”_

**6. CONCLUSIÓN**

En la Tabla 7 se observan los valores alcanzados por las emisiones anuales asociadas a cada una de las fuentes
emisoras de contaminantes, además de las emisiones totales, considerando que todas las actividades operarán al
mismo tiempo movimiento de tierra, maquinaria y traslado, para de esta forma obtener la situación más
desfavorable asociada a los 3 escenarios analizados (construcción, operación de la etapa propuesta y operación
del Proyecto total).

En tanto que en la Tabla 16, Tabla 22 y Tabla 28, se pueden observar los valores de las concentraciones de
dispersión de los contaminantes, modelados mediante SCREEN 3, en el cual se consideró el funcionamiento de
todas las actividades a la vez, en el área de Proyecto y por el mismo periodo de tiempo para cada escenario. Al
respecto se aprecia que los puntos de máxima concentración aportadas por el proyecto, se presentarán a una
distancia de 60 m alrededor de las fuentes emisoras para los escenarios 1 (fase de construcción) y 2 (fase de
operación de la etapa propuesta), mientras que para el escenario 3 (operación del Proyecto total) la máxima
concentración se encontrará a los 160 m. En tanto, que en la Tabla 15, Tabla 21 y Tabla 27 se estableció que
ninguno de estos contaminantes sobrepasará el umbral de sus correspondientes normas, por lo que su aporte de
emisiones a la atmósfera no afectará de forma significativa a la calidad del aire del sector para ninguno de los

escenarios analizados.

Finalmente, y de acuerdo a los resultados aquí descritos, se puede concluir que las emisiones asociadas al proyecto
en todos sus escenarios son bajas y en ningún caso producirán efectos adversos significativos en la calidad del aire,
que afecten a la salud de las personas o la calidad de los recursos naturales del sector, aun considerando las peores
condiciones de emisión y meteorológicas. Así mismo, y por esta misma razón no se requerirá en este análisis, la
utilización de otro modelo más complejo.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_48_
_Curauma”_

**7. REFERENCIAS**

`o` Guía de estimación de emisiones atmosféricas. Seremi de Medio Ambiente. Junio 2020.

`o` Compilation of Air Pollutant Emission Factors, AP 42, Actualizada por EPA en su sitio Web en diciembre

2011.

`o` Guía Metodológica Inventario de Emisiones Atmosféricas, M11 Metodología SINCA 2011 Ambiosis S,A,,

octubre 2011.
`o` Industria del Árido en Chile, Tomo I, Sistematización de Antecedentes Técnicos y Ambientales,
Corporación de Desarrollo Tecnológico, Comisión Nacional del Árido, Santiago, diciembre de 2001.
`o` Informe Final, “Servicio de Recopilación y Sistematización de Factores de Emisión al Aire para el Servicio
de Evaluación Ambiental”, de mayo 2015.
`o` Reconciling Urban Fugitive Dust Emissions Inventory and Ambient Source Contribution Estimates:
Summary of Current Knowledge and Needed Research, del Desert Research Institute (2000), publicado
por la Universidad University and Community College System of Nevada.

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_49_
_Curauma”_

### APÉNDICE 1: MEMORIA DE CÁLCULO DE LA MODELACIÓN

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_50_
_Curauma”_

```
05/12/22

20:11:57

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Construcción CO

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.447500E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 4.951 3 1.0 1.0 30.0 1.00 44.

40. 5.126 3 1.0 1.0 30.0 1.00 44.

50. 5.288 3 1.0 1.0 30.0 1.00 43.

60. 5.439 3 1.0 1.0 30.0 1.00 41.

70. 5.369 3 1.0 1.0 30.0 1.00 45.

80. 3.753 3 1.0 1.0 30.0 1.00 45.

90. 2.908 3 1.0 1.0 30.0 1.00 45.

100. 2.395 3 1.0 1.0 30.0 1.00 45.

150. 1.390 3 1.0 1.0 30.0 1.00 44.

200. 1.103 3 1.0 1.0 30.0 1.00 44.

250. 0.9385 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_51_
_Curauma”_

```
300. 0.8149 3 1.0 1.0 30.0 1.00 41.

350. 0.7193 3 1.0 1.0 30.0 1.00 36.

400. 0.6437 3 1.0 1.0 30.0 1.00 39.

450. 0.5828 3 1.0 1.0 30.0 1.00 33.

500. 0.5328 3 1.0 1.0 30.0 1.00 36.

600. 0.4557 3 1.0 1.0 30.0 1.00 3.

700. 0.3991 3 1.0 1.0 30.0 1.00 24.

800. 0.3561 3 1.0 1.0 30.0 1.00 33.

900. 0.3221 3 1.0 1.0 30.0 1.00 0.

1000. 0.2948 3 1.0 1.0 30.0 1.00 17.

1500. 0.2112 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 5.439 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_52_
_Curauma”_

```
05/12/22

20:15:19

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Construcción SOx

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.240000E-08

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 0.2655E-01 3 1.0 1.0 30.0 1.00 44.

40. 0.2749E-01 3 1.0 1.0 30.0 1.00 44.

50. 0.2836E-01 3 1.0 1.0 30.0 1.00 43.

60. 0.2917E-01 3 1.0 1.0 30.0 1.00 41.

70. 0.2879E-01 3 1.0 1.0 30.0 1.00 45.

80. 0.2013E-01 3 1.0 1.0 30.0 1.00 45.

90. 0.1559E-01 3 1.0 1.0 30.0 1.00 45.

100. 0.1284E-01 3 1.0 1.0 30.0 1.00 45.

150. 0.7453E-02 3 1.0 1.0 30.0 1.00 44.

200. 0.5918E-02 3 1.0 1.0 30.0 1.00 44.

250. 0.5033E-02 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_53_
_Curauma”_

```
300. 0.4370E-02 3 1.0 1.0 30.0 1.00 41.

350. 0.3857E-02 3 1.0 1.0 30.0 1.00 36.

400. 0.3452E-02 3 1.0 1.0 30.0 1.00 39.

450. 0.3125E-02 3 1.0 1.0 30.0 1.00 33.

500. 0.2858E-02 3 1.0 1.0 30.0 1.00 36.

600. 0.2444E-02 3 1.0 1.0 30.0 1.00 3.

700. 0.2141E-02 3 1.0 1.0 30.0 1.00 24.

800. 0.1910E-02 3 1.0 1.0 30.0 1.00 33.

900. 0.1728E-02 3 1.0 1.0 30.0 1.00 0.

1000. 0.1581E-02 3 1.0 1.0 30.0 1.00 17.

1500. 0.1133E-02 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 0.2917E-01 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_54_
_Curauma”_

```
05/12/22

20:18:14

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Construcción NOx

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.409700E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 4.533 3 1.0 1.0 30.0 1.00 44.

40. 4.693 3 1.0 1.0 30.0 1.00 44.

50. 4.841 3 1.0 1.0 30.0 1.00 43.

60. 4.980 3 1.0 1.0 30.0 1.00 41.

70. 4.915 3 1.0 1.0 30.0 1.00 45.

80. 3.436 3 1.0 1.0 30.0 1.00 45.

90. 2.662 3 1.0 1.0 30.0 1.00 45.

100. 2.193 3 1.0 1.0 30.0 1.00 45.

150. 1.272 3 1.0 1.0 30.0 1.00 44.

200. 1.010 3 1.0 1.0 30.0 1.00 44.

250. 0.8592 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_55_
_Curauma”_

```
300. 0.7460 3 1.0 1.0 30.0 1.00 41.

350. 0.6585 3 1.0 1.0 30.0 1.00 36.

400. 0.5893 3 1.0 1.0 30.0 1.00 39.

450. 0.5335 3 1.0 1.0 30.0 1.00 33.

500. 0.4878 3 1.0 1.0 30.0 1.00 36.

600. 0.4173 3 1.0 1.0 30.0 1.00 3.

700. 0.3654 3 1.0 1.0 30.0 1.00 24.

800. 0.3260 3 1.0 1.0 30.0 1.00 33.

900. 0.2949 3 1.0 1.0 30.0 1.00 0.

1000. 0.2699 3 1.0 1.0 30.0 1.00 17.

1500. 0.1933 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 4.980 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_56_
_Curauma”_

```
05/12/22

20:20:17

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Construcción MP2,5

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.240200E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 2.657 3 1.0 1.0 30.0 1.00 44.

40. 2.751 3 1.0 1.0 30.0 1.00 44.

50. 2.838 3 1.0 1.0 30.0 1.00 43.

60. 2.920 3 1.0 1.0 30.0 1.00 41.

70. 2.882 3 1.0 1.0 30.0 1.00 45.

80. 2.014 3 1.0 1.0 30.0 1.00 45.

90. 1.561 3 1.0 1.0 30.0 1.00 45.

100. 1.285 3 1.0 1.0 30.0 1.00 45.

150. 0.7459 3 1.0 1.0 30.0 1.00 44.

200. 0.5923 3 1.0 1.0 30.0 1.00 44.

250. 0.5037 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_57_
_Curauma”_

```
300. 0.4374 3 1.0 1.0 30.0 1.00 41.

350. 0.3861 3 1.0 1.0 30.0 1.00 36.

400. 0.3455 3 1.0 1.0 30.0 1.00 39.

450. 0.3128 3 1.0 1.0 30.0 1.00 33.

500. 0.2860 3 1.0 1.0 30.0 1.00 36.

600. 0.2446 3 1.0 1.0 30.0 1.00 3.

700. 0.2142 3 1.0 1.0 30.0 1.00 24.

800. 0.1911 3 1.0 1.0 30.0 1.00 33.

900. 0.1729 3 1.0 1.0 30.0 1.00 0.

1000. 0.1582 3 1.0 1.0 30.0 1.00 17.

1500. 0.1133 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 2.920 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_58_
_Curauma”_

```
05/12/22

20:22:10

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Construcción MP10

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.314400E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 3.478 3 1.0 1.0 30.0 1.00 44.

40. 3.601 3 1.0 1.0 30.0 1.00 44.

50. 3.715 3 1.0 1.0 30.0 1.00 43.

60. 3.822 3 1.0 1.0 30.0 1.00 41.

70. 3.772 3 1.0 1.0 30.0 1.00 45.

80. 2.637 3 1.0 1.0 30.0 1.00 45.

90. 2.043 3 1.0 1.0 30.0 1.00 45.

100. 1.683 3 1.0 1.0 30.0 1.00 45.

150. 0.9764 3 1.0 1.0 30.0 1.00 44.

200. 0.7753 3 1.0 1.0 30.0 1.00 44.

250. 0.6593 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_59_
_Curauma”_

```
300. 0.5725 3 1.0 1.0 30.0 1.00 41.

350. 0.5053 3 1.0 1.0 30.0 1.00 36.

400. 0.4522 3 1.0 1.0 30.0 1.00 39.

450. 0.4094 3 1.0 1.0 30.0 1.00 33.

500. 0.3743 3 1.0 1.0 30.0 1.00 36.

600. 0.3202 3 1.0 1.0 30.0 1.00 3.

700. 0.2804 3 1.0 1.0 30.0 1.00 24.

800. 0.2502 3 1.0 1.0 30.0 1.00 33.

900. 0.2263 3 1.0 1.0 30.0 1.00 0.

1000. 0.2071 3 1.0 1.0 30.0 1.00 17.

1500. 0.1484 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 3.822 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_60_
_Curauma”_

```
05/12/22

20:23:46

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Construcción MPS

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.140190E-05

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 15.51 3 1.0 1.0 30.0 1.00 44.

40. 16.06 3 1.0 1.0 30.0 1.00 44.

50. 16.57 3 1.0 1.0 30.0 1.00 43.

60. 17.04 3 1.0 1.0 30.0 1.00 41.

70. 16.82 3 1.0 1.0 30.0 1.00 45.

80. 11.76 3 1.0 1.0 30.0 1.00 45.

90. 9.109 3 1.0 1.0 30.0 1.00 45.

100. 7.503 3 1.0 1.0 30.0 1.00 45.

150. 4.354 3 1.0 1.0 30.0 1.00 44.

200. 3.457 3 1.0 1.0 30.0 1.00 44.

250. 2.940 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_61_
_Curauma”_

```
300. 2.553 3 1.0 1.0 30.0 1.00 41.

350. 2.253 3 1.0 1.0 30.0 1.00 36.

400. 2.016 3 1.0 1.0 30.0 1.00 39.

450. 1.826 3 1.0 1.0 30.0 1.00 33.

500. 1.669 3 1.0 1.0 30.0 1.00 36.

600. 1.428 3 1.0 1.0 30.0 1.00 3.

700. 1.250 3 1.0 1.0 30.0 1.00 24.

800. 1.116 3 1.0 1.0 30.0 1.00 33.

900. 1.009 3 1.0 1.0 30.0 1.00 0.

1000. 0.9234 3 1.0 1.0 30.0 1.00 17.

1500. 0.6615 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 17.04 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_62_
_Curauma”_

 - **Fase operación, etapa propuesta**

```
05/12/22

20:27:09

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Operación CO

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.666000E-07
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 0.7368 3 1.0 1.0 30.0 1.00 44.

40. 0.7629 3 1.0 1.0 30.0 1.00 44.

50. 0.7870 3 1.0 1.0 30.0 1.00 43.

60. 0.8095 3 1.0 1.0 30.0 1.00 41.

70. 0.7990 3 1.0 1.0 30.0 1.00 45.

80. 0.5585 3 1.0 1.0 30.0 1.00 45.

90. 0.4328 3 1.0 1.0 30.0 1.00 45.

100. 0.3564 3 1.0 1.0 30.0 1.00 45.

150. 0.2068 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_63_
_Curauma”_

```
200. 0.1642 3 1.0 1.0 30.0 1.00 44.

250. 0.1397 3 1.0 1.0 30.0 1.00 44.

300. 0.1213 3 1.0 1.0 30.0 1.00 41.

350. 0.1070 3 1.0 1.0 30.0 1.00 36.

400. 0.9579E-01 3 1.0 1.0 30.0 1.00 39.

450. 0.8673E-01 3 1.0 1.0 30.0 1.00 33.

500. 0.7930E-01 3 1.0 1.0 30.0 1.00 36.

600. 0.6783E-01 3 1.0 1.0 30.0 1.00 3.

700. 0.5940E-01 3 1.0 1.0 30.0 1.00 24.

800. 0.5299E-01 3 1.0 1.0 30.0 1.00 33.

900. 0.4794E-01 3 1.0 1.0 30.0 1.00 0.

1000. 0.4387E-01 3 1.0 1.0 30.0 1.00 17.

1500. 0.3143E-01 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 0.8095 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_64_
_Curauma”_

```
05/12/22

20:29:15

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Operación SOx

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.600000E-09

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 0.6638E-02 3 1.0 1.0 30.0 1.00 44.

40. 0.6873E-02 3 1.0 1.0 30.0 1.00 44.

50. 0.7090E-02 3 1.0 1.0 30.0 1.00 43.

60. 0.7293E-02 3 1.0 1.0 30.0 1.00 41.

70. 0.7198E-02 3 1.0 1.0 30.0 1.00 45.

80. 0.5032E-02 3 1.0 1.0 30.0 1.00 45.

90. 0.3899E-02 3 1.0 1.0 30.0 1.00 45.

100. 0.3211E-02 3 1.0 1.0 30.0 1.00 45.

150. 0.1863E-02 3 1.0 1.0 30.0 1.00 44.

200. 0.1480E-02 3 1.0 1.0 30.0 1.00 44.

250. 0.1258E-02 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_65_
_Curauma”_

```
300. 0.1093E-02 3 1.0 1.0 30.0 1.00 41.

350. 0.9644E-03 3 1.0 1.0 30.0 1.00 36.

400. 0.8630E-03 3 1.0 1.0 30.0 1.00 39.

450. 0.7814E-03 3 1.0 1.0 30.0 1.00 33.

500. 0.7144E-03 3 1.0 1.0 30.0 1.00 36.

600. 0.6111E-03 3 1.0 1.0 30.0 1.00 3.

700. 0.5352E-03 3 1.0 1.0 30.0 1.00 24.

800. 0.4774E-03 3 1.0 1.0 30.0 1.00 33.

900. 0.4319E-03 3 1.0 1.0 30.0 1.00 0.

1000. 0.3952E-03 3 1.0 1.0 30.0 1.00 17.

1500. 0.2831E-03 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 0.7293E-02 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_66_
_Curauma”_

```
05/12/22

20:31:08

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Operación NOx

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.725350E-05

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 80.25 3 1.0 1.0 30.0 1.00 44.

40. 83.09 3 1.0 1.0 30.0 1.00 44.

50. 85.71 3 1.0 1.0 30.0 1.00 43.

60. 88.17 3 1.0 1.0 30.0 1.00 41.

70. 87.02 3 1.0 1.0 30.0 1.00 45.

80. 60.83 3 1.0 1.0 30.0 1.00 45.

90. 47.13 3 1.0 1.0 30.0 1.00 45.

100. 38.82 3 1.0 1.0 30.0 1.00 45.

150. 22.53 3 1.0 1.0 30.0 1.00 44.

200. 17.89 3 1.0 1.0 30.0 1.00 44.

250. 15.21 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_67_
_Curauma”_

```
300. 13.21 3 1.0 1.0 30.0 1.00 41.

350. 11.66 3 1.0 1.0 30.0 1.00 36.

400. 10.43 3 1.0 1.0 30.0 1.00 39.

450. 9.446 3 1.0 1.0 30.0 1.00 33.

500. 8.636 3 1.0 1.0 30.0 1.00 36.

600. 7.387 3 1.0 1.0 30.0 1.00 3.

700. 6.470 3 1.0 1.0 30.0 1.00 24.

800. 5.772 3 1.0 1.0 30.0 1.00 33.

900. 5.221 3 1.0 1.0 30.0 1.00 0.

1000. 4.778 3 1.0 1.0 30.0 1.00 17.

1500. 3.423 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 88.17 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_68_
_Curauma”_

```
05/12/22

20:33:00

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Operación MP2,5

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.963000E-07

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 1.065 3 1.0 1.0 30.0 1.00 44.

40. 1.103 3 1.0 1.0 30.0 1.00 44.

50. 1.138 3 1.0 1.0 30.0 1.00 43.

60. 1.171 3 1.0 1.0 30.0 1.00 41.

70. 1.155 3 1.0 1.0 30.0 1.00 45.

80. 0.8076 3 1.0 1.0 30.0 1.00 45.

90. 0.6257 3 1.0 1.0 30.0 1.00 45.

100. 0.5154 3 1.0 1.0 30.0 1.00 45.

150. 0.2991 3 1.0 1.0 30.0 1.00 44.

200. 0.2375 3 1.0 1.0 30.0 1.00 44.

250. 0.2020 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_69_
_Curauma”_

```
300. 0.1754 3 1.0 1.0 30.0 1.00 41.

350. 0.1548 3 1.0 1.0 30.0 1.00 36.

400. 0.1385 3 1.0 1.0 30.0 1.00 39.

450. 0.1254 3 1.0 1.0 30.0 1.00 33.

500. 0.1147 3 1.0 1.0 30.0 1.00 36.

600. 0.9808E-01 3 1.0 1.0 30.0 1.00 3.

700. 0.8589E-01 3 1.0 1.0 30.0 1.00 24.

800. 0.7663E-01 3 1.0 1.0 30.0 1.00 33.

900. 0.6932E-01 3 1.0 1.0 30.0 1.00 0.

1000. 0.6343E-01 3 1.0 1.0 30.0 1.00 17.

1500. 0.4544E-01 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 1.171 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_70_
_Curauma”_

```
05/12/22

20:35:00

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Operación MP10

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.162800E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 1.801 3 1.0 1.0 30.0 1.00 44.

40. 1.865 3 1.0 1.0 30.0 1.00 44.

50. 1.924 3 1.0 1.0 30.0 1.00 43.

60. 1.979 3 1.0 1.0 30.0 1.00 41.

70. 1.953 3 1.0 1.0 30.0 1.00 45.

80. 1.365 3 1.0 1.0 30.0 1.00 45.

90. 1.058 3 1.0 1.0 30.0 1.00 45.

100. 0.8713 3 1.0 1.0 30.0 1.00 45.

150. 0.5056 3 1.0 1.0 30.0 1.00 44.

200. 0.4014 3 1.0 1.0 30.0 1.00 44.

250. 0.3414 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_71_
_Curauma”_

```
300. 0.2965 3 1.0 1.0 30.0 1.00 41.

350. 0.2617 3 1.0 1.0 30.0 1.00 36.

400. 0.2342 3 1.0 1.0 30.0 1.00 39.

450. 0.2120 3 1.0 1.0 30.0 1.00 33.

500. 0.1938 3 1.0 1.0 30.0 1.00 36.

600. 0.1658 3 1.0 1.0 30.0 1.00 3.

700. 0.1452 3 1.0 1.0 30.0 1.00 24.

800. 0.1295 3 1.0 1.0 30.0 1.00 33.

900. 0.1172 3 1.0 1.0 30.0 1.00 0.

1000. 0.1072 3 1.0 1.0 30.0 1.00 17.

1500. 0.7682E-01 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 1.979 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_72_
_Curauma”_

```
05/12/22

20:36:45

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Fase Operación MPS

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.411300E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 97.0000
LENGTH OF SMALLER SIDE (M) = 96.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
30. 4.550 3 1.0 1.0 30.0 1.00 44.

40. 4.711 3 1.0 1.0 30.0 1.00 44.

50. 4.860 3 1.0 1.0 30.0 1.00 43.

60. 4.999 3 1.0 1.0 30.0 1.00 41.

70. 4.935 3 1.0 1.0 30.0 1.00 45.

80. 3.449 3 1.0 1.0 30.0 1.00 45.

90. 2.673 3 1.0 1.0 30.0 1.00 45.

100. 2.201 3 1.0 1.0 30.0 1.00 45.

150. 1.277 3 1.0 1.0 30.0 1.00 44.

200. 1.014 3 1.0 1.0 30.0 1.00 44.

250. 0.8626 3 1.0 1.0 30.0 1.00 44.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_73_
_Curauma”_

```
300. 0.7490 3 1.0 1.0 30.0 1.00 41.

350. 0.6611 3 1.0 1.0 30.0 1.00 36.

400. 0.5916 3 1.0 1.0 30.0 1.00 39.

450. 0.5356 3 1.0 1.0 30.0 1.00 33.

500. 0.4897 3 1.0 1.0 30.0 1.00 36.

600. 0.4189 3 1.0 1.0 30.0 1.00 3.

700. 0.3669 3 1.0 1.0 30.0 1.00 24.

800. 0.3273 3 1.0 1.0 30.0 1.00 33.

900. 0.2961 3 1.0 1.0 30.0 1.00 0.

1000. 0.2709 3 1.0 1.0 30.0 1.00 17.

1500. 0.1941 3 1.0 1.0 30.0 1.00 15.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 4.999 60. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_74_
_Curauma”_

 - **Fase de operación, Proyecto total**

```
05/13/22

14:44:20

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Proyecto completo - Fase Operación CO

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.743000E-07
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 240.0000
LENGTH OF SMALLER SIDE (M) = 210.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
50. 1.084 3 1.0 1.0 30.0 1.00 37.

60. 1.106 3 1.0 1.0 30.0 1.00 36.

70. 1.127 3 1.0 1.0 30.0 1.00 36.

80. 1.150 3 1.0 1.0 30.0 1.00 35.

90. 1.172 3 1.0 1.0 30.0 1.00 35.

100. 1.193 3 1.0 1.0 30.0 1.00 34.

110. 1.215 3 1.0 1.0 30.0 1.00 32.

120. 1.237 3 1.0 1.0 30.0 1.00 33.

130. 1.259 3 1.0 1.0 30.0 1.00 32.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_75_
_Curauma”_

```
140. 1.280 3 1.0 1.0 30.0 1.00 31.

150. 1.301 3 1.0 1.0 30.0 1.00 37.

160. 1.324 3 1.0 1.0 30.0 1.00 41.

170. 1.042 3 1.0 1.0 30.0 1.00 41.

180. 0.8899 3 1.0 1.0 30.0 1.00 41.

190. 0.7992 3 1.0 1.0 30.0 1.00 41.

200. 0.7395 3 1.0 1.0 30.0 1.00 40.

250. 0.6086 3 1.0 1.0 30.0 1.00 38.

300. 0.5583 3 1.0 1.0 30.0 1.00 36.

350. 0.5187 3 1.0 1.0 30.0 1.00 34.

400. 0.4827 3 1.0 1.0 30.0 1.00 32.

450. 0.4505 3 1.0 1.0 30.0 1.00 29.

500. 0.4216 3 1.0 1.0 30.0 1.00 23.

1000. 0.2549 3 1.0 1.0 30.0 1.00 1.

1500. 0.1861 3 1.0 1.0 30.0 1.00 2.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 1.324 160. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_76_
_Curauma”_

```
05/13/22

14:38:29

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Proyecto completo - Fase Operación SOx

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.700000E-09

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 240.0000
LENGTH OF SMALLER SIDE (M) = 210.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
50. 0.1022E-01 3 1.0 1.0 30.0 1.00 37.

60. 0.1042E-01 3 1.0 1.0 30.0 1.00 36.

70. 0.1062E-01 3 1.0 1.0 30.0 1.00 36.

80. 0.1083E-01 3 1.0 1.0 30.0 1.00 35.

90. 0.1104E-01 3 1.0 1.0 30.0 1.00 35.

100. 0.1124E-01 3 1.0 1.0 30.0 1.00 34.

110. 0.1145E-01 3 1.0 1.0 30.0 1.00 32.

120. 0.1165E-01 3 1.0 1.0 30.0 1.00 33.

130. 0.1186E-01 3 1.0 1.0 30.0 1.00 32.

140. 0.1206E-01 3 1.0 1.0 30.0 1.00 31.

150. 0.1226E-01 3 1.0 1.0 30.0 1.00 37.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_77_
_Curauma”_

```
160. 0.1248E-01 3 1.0 1.0 30.0 1.00 41.

170. 0.9819E-02 3 1.0 1.0 30.0 1.00 41.

180. 0.8384E-02 3 1.0 1.0 30.0 1.00 41.

190. 0.7529E-02 3 1.0 1.0 30.0 1.00 41.

200. 0.6967E-02 3 1.0 1.0 30.0 1.00 40.

250. 0.5734E-02 3 1.0 1.0 30.0 1.00 38.

300. 0.5260E-02 3 1.0 1.0 30.0 1.00 36.

350. 0.4887E-02 3 1.0 1.0 30.0 1.00 34.

400. 0.4548E-02 3 1.0 1.0 30.0 1.00 32.

450. 0.4244E-02 3 1.0 1.0 30.0 1.00 29.

500. 0.3972E-02 3 1.0 1.0 30.0 1.00 23.

1000. 0.2402E-02 3 1.0 1.0 30.0 1.00 1.

1500. 0.1753E-02 3 1.0 1.0 30.0 1.00 2.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 0.1248E-01 160. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_78_
_Curauma”_

```
05/13/22

14:18:24

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Proyecto completo - Fase Operación NOx

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.809490E-05

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 240.0000
LENGTH OF SMALLER SIDE (M) = 210.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
50. 118.2 3 1.0 1.0 30.0 1.00 37.

60. 120.5 3 1.0 1.0 30.0 1.00 36.

70. 122.8 3 1.0 1.0 30.0 1.00 36.

80. 125.3 3 1.0 1.0 30.0 1.00 35.

90. 127.7 3 1.0 1.0 30.0 1.00 35.

100. 130.0 3 1.0 1.0 30.0 1.00 34.

110. 132.4 3 1.0 1.0 30.0 1.00 32.

120. 134.7 3 1.0 1.0 30.0 1.00 33.

130. 137.1 3 1.0 1.0 30.0 1.00 32.

140. 139.5 3 1.0 1.0 30.0 1.00 31.

150. 141.7 3 1.0 1.0 30.0 1.00 37.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_79_
_Curauma”_

```
160. 144.3 3 1.0 1.0 30.0 1.00 41.

170. 113.5 3 1.0 1.0 30.0 1.00 41.

180. 96.95 3 1.0 1.0 30.0 1.00 41.

190. 87.07 3 1.0 1.0 30.0 1.00 41.

200. 80.57 3 1.0 1.0 30.0 1.00 40.

250. 66.30 3 1.0 1.0 30.0 1.00 38.

300. 60.83 3 1.0 1.0 30.0 1.00 36.

350. 56.51 3 1.0 1.0 30.0 1.00 34.

400. 52.59 3 1.0 1.0 30.0 1.00 32.

450. 49.08 3 1.0 1.0 30.0 1.00 29.

500. 45.94 3 1.0 1.0 30.0 1.00 23.

1000. 27.77 3 1.0 1.0 30.0 1.00 1.

1500. 20.28 3 1.0 1.0 30.0 1.00 2.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 144.3 160. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_80_
_Curauma”_

```
05/13/22

14:33:49

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Proyecto completo - Fase Operación MP2,5

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.107500E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 240.0000
LENGTH OF SMALLER SIDE (M) = 210.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
50. 1.569 3 1.0 1.0 30.0 1.00 37.

60. 1.600 3 1.0 1.0 30.0 1.00 36.

70. 1.631 3 1.0 1.0 30.0 1.00 36.

80. 1.664 3 1.0 1.0 30.0 1.00 35.

90. 1.695 3 1.0 1.0 30.0 1.00 35.

100. 1.727 3 1.0 1.0 30.0 1.00 34.

110. 1.758 3 1.0 1.0 30.0 1.00 32.

120. 1.789 3 1.0 1.0 30.0 1.00 33.

130. 1.821 3 1.0 1.0 30.0 1.00 32.

140. 1.852 3 1.0 1.0 30.0 1.00 31.

150. 1.882 3 1.0 1.0 30.0 1.00 37.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_81_
_Curauma”_

```
160. 1.916 3 1.0 1.0 30.0 1.00 41.

170. 1.508 3 1.0 1.0 30.0 1.00 41.

180. 1.288 3 1.0 1.0 30.0 1.00 41.

190. 1.156 3 1.0 1.0 30.0 1.00 41.

200. 1.070 3 1.0 1.0 30.0 1.00 40.

250. 0.8805 3 1.0 1.0 30.0 1.00 38.

300. 0.8078 3 1.0 1.0 30.0 1.00 36.

350. 0.7504 3 1.0 1.0 30.0 1.00 34.

400. 0.6985 3 1.0 1.0 30.0 1.00 32.

450. 0.6517 3 1.0 1.0 30.0 1.00 29.

500. 0.6101 3 1.0 1.0 30.0 1.00 23.

1000. 0.3688 3 1.0 1.0 30.0 1.00 1.

1500. 0.2693 3 1.0 1.0 30.0 1.00 2.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 1.916 160. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_82_
_Curauma”_

```
05/13/22

14:30:00

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Proyecto completo - Fase Operación MP10

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.181700E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 240.0000
LENGTH OF SMALLER SIDE (M) = 210.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
50. 2.652 3 1.0 1.0 30.0 1.00 37.

60. 2.704 3 1.0 1.0 30.0 1.00 36.

70. 2.756 3 1.0 1.0 30.0 1.00 36.

80. 2.812 3 1.0 1.0 30.0 1.00 35.

90. 2.865 3 1.0 1.0 30.0 1.00 35.

100. 2.918 3 1.0 1.0 30.0 1.00 34.

110. 2.971 3 1.0 1.0 30.0 1.00 32.

120. 3.025 3 1.0 1.0 30.0 1.00 33.

130. 3.078 3 1.0 1.0 30.0 1.00 32.

140. 3.131 3 1.0 1.0 30.0 1.00 31.

150. 3.182 3 1.0 1.0 30.0 1.00 37.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_83_
_Curauma”_

```
160. 3.239 3 1.0 1.0 30.0 1.00 41.

170. 2.549 3 1.0 1.0 30.0 1.00 41.

180. 2.176 3 1.0 1.0 30.0 1.00 41.

190. 1.954 3 1.0 1.0 30.0 1.00 41.

200. 1.808 3 1.0 1.0 30.0 1.00 40.

250. 1.488 3 1.0 1.0 30.0 1.00 38.

300. 1.365 3 1.0 1.0 30.0 1.00 36.

350. 1.268 3 1.0 1.0 30.0 1.00 34.

400. 1.181 3 1.0 1.0 30.0 1.00 32.

450. 1.102 3 1.0 1.0 30.0 1.00 29.

500. 1.031 3 1.0 1.0 30.0 1.00 23.

1000. 0.6234 3 1.0 1.0 30.0 1.00 1.

1500. 0.4552 3 1.0 1.0 30.0 1.00 2.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 3.239 160. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_84_
_Curauma”_

```
05/13/22

14:25:31

*** SCREEN3 MODEL RUN ***

*** VERSION DATED 13043 ***

Proyecto completo - Fase Operación MPS

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.459100E-06

SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 240.0000
LENGTH OF SMALLER SIDE (M) = 210.0000
RECEPTOR HEIGHT (M) = 1.5000
URBAN/RURAL OPTION = URBAN

THE NON-REGULATORY BUT CONSERVATIVE BRODE 2 MIXING HEIGHT OPTION WAS

SELECTED.

A NON-REGULATORY ANEMOMETER HEIGHT (HANE) OF 5.0 METERS WAS

ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** STABILITY CLASS 3 ONLY ***

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING

DISTANCES ***

DIST CONC UHANE USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
50. 6.701 3 1.0 1.0 30.0 1.00 37.

60. 6.833 3 1.0 1.0 30.0 1.00 36.

70. 6.964 3 1.0 1.0 30.0 1.00 36.

80. 7.106 3 1.0 1.0 30.0 1.00 35.

90. 7.240 3 1.0 1.0 30.0 1.00 35.

100. 7.374 3 1.0 1.0 30.0 1.00 34.

110. 7.507 3 1.0 1.0 30.0 1.00 32.

120. 7.642 3 1.0 1.0 30.0 1.00 33.

130. 7.776 3 1.0 1.0 30.0 1.00 32.

140. 7.911 3 1.0 1.0 30.0 1.00 31.

150. 8.039 3 1.0 1.0 30.0 1.00 37.

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_85_
_Curauma”_

```
160. 8.184 3 1.0 1.0 30.0 1.00 41.

170. 6.440 3 1.0 1.0 30.0 1.00 41.

180. 5.499 3 1.0 1.0 30.0 1.00 41.

190. 4.938 3 1.0 1.0 30.0 1.00 41.

200. 4.569 3 1.0 1.0 30.0 1.00 40.

250. 3.760 3 1.0 1.0 30.0 1.00 38.

300. 3.450 3 1.0 1.0 30.0 1.00 36.

350. 3.205 3 1.0 1.0 30.0 1.00 34.

400. 2.983 3 1.0 1.0 30.0 1.00 32.

450. 2.783 3 1.0 1.0 30.0 1.00 29.

500. 2.605 3 1.0 1.0 30.0 1.00 23.

1000. 1.575 3 1.0 1.0 30.0 1.00 1.

1500. 1.150 3 1.0 1.0 30.0 1.00 2.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 8.184 160. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

```

_Informe de modelación de emisiones atmosféricas, Adenda DIA “SCALA Data Center_
_86_
_Curauma”_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Resumen de emisiones por actividad, Fase de Construcción - Escenario 1**

| Fase | Actividades | Emisiones Atmosféricas del Proyecto<br>(ton/año) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase | Actividades | CO | SOX | NOX | MP2,5 comb | MP10 comb | MP2,5 resus | MP10 resus | MP2,5 total | MP10 total | MPS |
| Construcción | Compactación | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0017 | 0,0034 | 0,0017 | 0,0034 | 0,0164 |
| Construcción | Excavación | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0394 | 0,0768 | 0,0394 | 0,0768 | 0,3756 |
| Construcción | Transferencia de material | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0013 | 0,0086 | 0,0013 | 0,0086 | 0,0183 |
| Construcción | Erosión de material en acopio | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0001 | 0,0004 | 0,0001 | 0,0004 | 0,0009 |
| Construcción | Circulación de vehículos en caminos pavimentado interior | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0012 | 0,0052 | 0,0012 | 0,0052 | 0,0250 |
| Construcción | Combustión vehículos | 0,0054 | 0,0001 | 0,0531 | 0,0007 | 0,0007 | 0,0000 | 0,0000 | 0,0022 | 0,0007 | 0,0000 |
| Construcción | Combustión maquinaria fuera de ruta | 0,1258 | 0,0006 | 0,0671 | 0,0022 | 0,0022 | 0,0000 | 0,0000 | 0,0022 | 0,0022 | 0,0000 |
| Construcción | **Emisión total (ton/año)** | **0,1312** | **0,0007** | **0,1202** | **0,0029** | **0,0029** | **0,0437** | **0,0944** | **0,0705** | **0,0922** | **0,4112** |

**Tabla 2.: Resumen de emisiones por actividad, Fase de Operación Etapa Propuesta - Escenario 2**

| Fase | Actividades | Emisiones Atmosféricas del Proyecto<br>(ton/año) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase | Actividades | CO | SOX | NOX | MP2,5 comb | MP10 comb | MP2,5 resus | MP10 resus | MP2,5 total | MP10 total | MPS |
| Operación<br>Etapa 1 | Circulación de vehículos en caminos pavimentado | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0056 | 0,0251 | 0,0056 | 0,0251 | 0,1206 |
| Operación<br>Etapa 1 | Combustión vehículos | 0,0066 | 0,0002 | 0,0282 | 0,0002 | 0,0002 | 0,0000 | 0,0000 | 0,0002 | 0,0002 | 0,0000 |
| Operación<br>Etapa 1 | Grupo Electrógeno | 0,0129 | 0,0000 | 2,0991 | 0,0224 | 0,0224 | 0,0000 | 0,0000 | 0,0224 | 0,0224 | 0,0000 |
| Operación<br>Etapa 1 | **Emisión total (ton/año)** | **0,0195** | **0,0002** | **2,1273** | **0,0226** | **0,0226** | **0,0056** | **0,0251** | **0,0282** | **0,0477** | **0,1206** |

**Tabla 3.: Resumen de emisiones por actividad, Fase de Operación Proyecto Total - Escenario 3**

| Fase | Actividades | Emisiones Atmosféricas del Proyecto<br>(ton/año) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fase | Actividades | CO | SOX | NOX | MP2,5 comb | MP10 comb | MP2,5 resus | MP10 resus | MP2,5 total | MP10 total | MPS |
| Operación<br>Proyecto<br>Total | Circulación de vehículos en caminos pavimentado | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0336 | 0,1506 | 0,0336 | 0,1506 | 0,7236 |
| Operación<br>Proyecto<br>Total | Combustión vehículos | 0,0396 | 0,0011 | 0,1692 | 0,0012 | 0,0012 | 0,0000 | 0,0000 | 0,0012 | 0,0012 | 0,0000 |
| Operación<br>Proyecto<br>Total | Grupo Electrógeno | 0,0774 | 0,0000 | 12,5946 | 0,1344 | 0,1344 | 0,0000 | 0,0000 | 0,1344 | 0,1344 | 0,0000 |
| Operación<br>Proyecto<br>Total | **Emisión total (ton/año)** | **0,1172** | **0,0011** | **12,7641** | **0,1356** | **0,1356** | **0,0336** | **0,1506** | **0,1694** | **0,2865** | **0,7238** |

**Tabla 4.: Normas de Calidad del Aire consideradas en el estudio**

| Parámetro | Norma | Estadístico | Limite según Norma | Unidad | Referencia |
| --- | --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio Anual1 | 50 | (~~~~g/m3) | D.S. N° 59 / 1998 MINSEGPRES |
| MP10 | Primaria | Percentil 98 promedio diario | 150 | (g/m3) | (g/m3) |
| MP2,5 | Primaria | Promedio Anual | 20 | (g/m3) | D.S. N° 12/2011 del MMA |
| MP2,5 | Primaria | Percentil 98 promedio diario | 50 | (g/m3) | (g/m3) |
| NO2 | Primaria | Promedio Anual | 100 | (g/m3) | D.S. N° 114/ 2002 MINSEGPRES |
| NO2 | Primaria | Percentil 99 máx. 1 hora | 400 | (g/m3) | (g/m3) |
| CO | Primaria | Percentil 99 1 hora | 30 | (mg/m3) | D.S. N° 115/2002 del MINSEGPRES |
| CO | Primaria | Percentil 99 8 hora | 10 | (mg/m3) <br> | (mg/m3) <br> |
| SO2 | Primaria | Promedio Anual | 60 | (~~~~g/m3) | D.S. N° 104/ 2018 MMA |
| SO2 | Primaria | Percentil 99 24 horas | 150 | (g/m3) | (g/m3) |
| SO2 | Primaria | Percentil 98,5 1 hora | 350 | (g/m3) | (g/m3) |
| SO2 (**) | Secundaria | Promedio Anual2 | 365 | (g/m3) | D.S. N°22/2010 MINSEGPRES |
| SO2 (**) | Secundaria | Percentil 98 promedio diario | 80 | (g/m3) | (g/m3) |
| MPS (*) | Secundaria | Promedio Anual3 | 200 | (g/m3) | Norma Suiza |

**Tabla 5.: Contaminante que constituye la Línea de base de Calidad de aire y ubicación de la Estación de monitoreo**

| Estación | Coordenadas UTM WGS84 (Huso 19) | Col3 | Contaminante | Periodo | Administrada por |
| --- | --- | --- | --- | --- | --- |
| Estación | Este (m) | Norte (m) | Norte (m) | Norte (m) | Norte (m) |
| Valparaíso | 255.891 | 6.340.183 | MP2,5 | 2019-2021 | MMA |

**Tabla 6.: Resumen de concentraciones (μg/m [3] N)**

| Contaminante | Estadístico | Estación Valparaíso | Limite según Norma | % de la Norma |
| --- | --- | --- | --- | --- |
| MP2,5 | Promedio Anual1 | 14 | 20 | 68,2 |
| MP2,5 | Percentil 98 promedio diario | 35 | 50 | 70,2 |

**Tabla 8.: Tasas de emisiones del Proyecto, Fase operación Etapa propuesta - Escenario 2**

| Emisiones | CO | SO<br>x | NO<br>X | MP<br>2,5 Total | MP<br>10 Total | MPS<br>l |
| --- | --- | --- | --- | --- | --- | --- |
| ton/año | 0,0195 | 0,0002 | 2,1273 | 0,0282 | 0,0477 | 0,1206 |
| g/m2-s | **0,0000000666** | **0,0000000006** | **0,0000072535** | **0,0000000963** | **0,0000001628** | 0,0000004113 |

**Tabla 9.: Tasas de emisiones del Proyecto, Fase operación Proyecto total - Escenario 3**

| Emisiones | CO | SO<br>x | NO<br>X | MP<br>2,5 Total | MP<br>10 Total | MPS<br>l |
| --- | --- | --- | --- | --- | --- | --- |
| ton/año | 0,1172 | 0,0011 | 12,7641 | 0,1694 | 0,2865 | 0,7238 |
| g/m2-s | **0,0000000743** | **0,0000000007** | **0,0000080949** | **0,0000001075** | **0,0000001817** | **0,0000004591** |

**Tabla 10.: Coordenadas de los receptores del Proyecto**

| Nombre | Tipo de receptor | Coordenadas UTM WGS84 (Huso 19) | Col4 | Distancia aproximada al área<br>del Proyecto |
| --- | --- | --- | --- | --- |
| Nombre | Tipo de receptor | Este (m) | Norte (m) | Norte (m) |
| Receptor 1 | Humano | 261.403 | 6.330.734 | 52 |
| Receptor 2 | Humano | 261.468 | 6.330.465 | 83 |
| Receptor 3 | Humano | 261.092 | 6.330.389 | 0 |
| Receptor 4 | Humano | 261.142 | 6.330.595 | 0 |
| Receptor 5 | Recurso natural (Reserva Lago Peñuelas) | <br>261222 | 6330175 | 120 |

**Tabla 11.: Datos de entrada del modelo**

| Parámetro | Datos de entrada | Unidad |
| --- | --- | --- |
| Tipo de fuente | Área | - |
| Altura de liberación | 1,0 | m |
| Longitud de lado largo | 97 | m |
| Longitud de lado corto | 96 | m |
| Altura del receptor | 1,5 | m |
| Terreno Urbano/Rural | Urbano | - |
| Altura de la mezcla | 30 | m |
| Altura anemométrica | 5 | m |
| Clase de estabilidad | 3 | “Semi Inestable” |
| Velocidad eólica | 1,0 | m/s |

**Tabla 12.: Resultados del modelo, Fase de construcción - Escenario 1**

| Distancia (m) | Concentración horaria (g/m3) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO | SOx | NOX | MP2,5 Total | MP10 Total | MPS |
| 30 | 4,951 | 0,02655 | 4,533 | 2,657 | 3,478 | 15,51 |
| 40 | 5,126 | 0,02749 | 4,693 | 2,751 | 3,601 | 16,06 |
| 50 | 5,288 | 0,02836 | 4,841 | 2,838 | 3,72 | 16,57 |
| 60 | 5,439 | 0,02917 | 4,98 | 2,92 | 3,82 | 17,04 |
| 70 | 5,369 | 0,02879 | 4,915 | 2,882 | 3,77 | 16,82 |
| 80 | 3,753 | 0,02013 | 3,436 | 2,014 | 2,64 | 11,76 |
| 90 | 2,908 | 0,01559 | 2,662 | 1,561 | 2,04 | 9,109 |
| 100 | 2,395 | 0,01284 | 2,193 | 1,285 | 1,683 | 7,503 |
| 150 | 1,39 | 0,007453 | 1,272 | 0,7459 | 0,9764 | 4,354 |
| 200 | 1,103 | 0,005918 | 1,01 | 0,5923 | 0,7753 | 3,457 |
| 250 | 0,9385 | 0,005033 | 0,8592 | 0,5037 | 0,6593 | 2,94 |
| 300 | 0,8149 | 0,00437 | 0,746 | 0,4374 | 0,5725 | 2,553 |
| 350 | 0,7193 | 0,003857 | 0,6585 | 0,3861 | 0,5053 | 2,253 |
| 400 | 0,6437 | 0,003452 | 0,5893 | 0,3455 | 0,4522 | 2,016 |
| 450 | 0,5828 | 0,003125 | 0,5335 | 0,3128 | 0,4094 | 2,826 |
| 500 | 0,5328 | 0,002858 | 0,4878 | 0,286 | 0,3743 | 1,669 |
| 600 | 0,4557 | 0,002444 | 0,4173 | 0,2446 | 0,3202 | 1,428 |
| 700 | 0,3991 | 0,002141 | 0,3654 | 0,2142 | 0,2804 | 1,25 |
| 800 | 0,3561 | 0,00191 | 0,326 | 0,1911 | 0,2502 | 1,116 |
| 900 | 0,3221 | 0,001728 | 0,2949 | 0,1729 | 0,2263 | 1,009 |
| 1000 | 0,2948 | 0,001581 | 0,2699 | 0,1582 | 0,2071 | 0,9234 |
| 1500 | 0,2112 | 0,001133 | 0,1933 | 0,1133 | 0,1484 | 0,6615 |

**Tabla 13.: Máximas concentraciones horarias obtenidas del modelo**

| Lugar | Distancia máx,<br>concentración (m) | Concentración horaria (g/m3) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lugar<br> | Distancia máx,<br>concentración (m) | <br>CO | SOx | NOX | MP2,5 Total | MP10 Tota | MPS |
| Proyecto | 60 | 5,439 | 0,02917 | 4,98 | 2,92 | 3,82 | 17,04 |

**Tabla 14.: Factores de conversión para promedios máximos de concentración**

| Tiempo promedio | Factor conversión |
| --- | --- |
| 3 horas | 0,9 |
| 8 horas | 0,7 |
| 24 horas | 0,4 |
| Anual | 0,08 |

**Tabla 15.: Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Construcción - Escenario 1**

| Parámetro | Estadístico | Máxima del<br>proyecto<br>(g/m3N) | Limite según<br>Norma<br>(g/m3) | Porcentaje<br>respecto de la<br>Norma (%) | Referencia |
| --- | --- | --- | --- | --- | --- |
| MP10 | Concentración 24 horas | 1,53 | 150 | 1,0 | D.S. N° 59 / 1998 MINSEGPRES |
| MP10 | Concentración anual | 0,31 | 50 | 0,6 | 0,6 |
| MP2,5 | Concentración 24 horas | 1,17 | 50 | 2,3 | D.S. N° 12/2011 del MMA |
| MP2,5 | Concentración anual | 0,23 | 20 | 1,2 | 1,2 |
| NOx | Concentración 1 hora | 4,98 | 400 | 1,2 | D.S. N° 114/ 2002 MINSEGPRES |
| NOx | Concentración anual | 0,40 | 100 | 0,4 | 0,4 |
| SO2 | Concentración 1 hora | 0,03 | 350 | 0,008 | D.S. N° 104/ 2018 MMA |
| SO2 | Concentración 24 horas | 0,012 | 150 | 0,008 | 0,008 |
| SO2 | Concentración anual | 0,002 | 60 | 0,004 | 0,004 |
| CO | Concentración 1 hora | 5,44 | 30.000 | 0,018 | ~~D~~.S. N° 115/2002 del MINSEGPRES |
| CO | Concentración 8 horas | 3,81 | 10.000 | 0,038 | 0,038 |
| MPS (*) | Concentración anual | 1,36 | 200 | 0,7 | Norma Suiza |
| SO2 (**) | Concentración 24 horas | 0,012 | 365 | 0,003 | D.S. N°22/2010 MINSEGPRES |
| SO2 (**) | Concentración anual | 0,002 | 80 | 0,003 | 0,003 |

**Tabla 16.: Concentraciones por distancia de los contaminantes analizados, Fase de Construcción - Escenario 1**

| Distancia (m) | Concentración horaria (g/m3) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO <br>(1 hora) | CO <br>(8 horas) | SOx <br>(1 hora) | SOx <br>(24 horas) | SOx <br>(Anual) | NOX <br>(1 hora) | NOx <br>(Anual) | MP2,5 Total<br>(24 horas) | MP2,5 Total<br>(Anual) | MP10 Total<br>(24 horas) | MP10 Total<br>(Anual) | MPS <br>(Anual) |
| 30 | 4,951 | 3,466 | 0,027 | 0,011 | 0,002 | 4,533 | 0,363 | 1,063 | 0,213 | 1,391 | 0,278 | 1,241 |
| 40 | 5,126 | 3,588 | 0,027 | 0,011 | 0,002 | 4,693 | 0,375 | 1,100 | 0,220 | 1,440 | 0,288 | 1,285 |
| 50 | 5,288 | 3,702 | 0,028 | 0,011 | 0,002 | 4,841 | 0,387 | 1,135 | 0,227 | 1,486 | 0,297 | 1,326 |
| 60* | 5,439 | 3,807 | 0,029 | 0,012 | 0,002 | 4,980 | 0,398 | 1,168 | 0,234 | 1,529 | 0,306 | 1,363 |
| 70 | 5,369 | 3,758 | 0,029 | 0,012 | 0,002 | 4,915 | 0,393 | 1,153 | 0,231 | 1,509 | 0,302 | 1,346 |
| 80 | 3,753 | 2,627 | 0,020 | 0,008 | 0,002 | 3,436 | 0,275 | 0,806 | 0,161 | 1,055 | 0,211 | 0,941 |
| 90 | 2,908 | 2,036 | 0,016 | 0,006 | 0,001 | 2,662 | 0,213 | 0,624 | 0,125 | 0,817 | 0,163 | 0,729 |
| 100 | 2,395 | 1,677 | 0,013 | 0,005 | 0,001 | 2,193 | 0,175 | 0,514 | 0,103 | 0,673 | 0,135 | 0,600 |
| 150 | 1,39 | 0,973 | 0,007 | 0,003 | 0,001 | 1,272 | 0,102 | 0,298 | 0,060 | 0,391 | 0,078 | 0,348 |
| 200 | 1,103 | 0,772 | 0,006 | 0,002 | 0,000 | 1,010 | 0,081 | 0,237 | 0,047 | 0,310 | 0,062 | 0,277 |
| 250 | 0,9385 | 0,657 | 0,005 | 0,002 | 0,000 | 0,859 | 0,069 | 0,201 | 0,040 | 0,264 | 0,053 | 0,235 |
| 300 | 0,8149 | 0,570 | 0,004 | 0,002 | 0,000 | 0,746 | 0,060 | 0,175 | 0,035 | 0,229 | 0,046 | 0,204 |
| 350 | 0,7193 | 0,504 | 0,004 | 0,002 | 0,000 | 0,659 | 0,053 | 0,154 | 0,031 | 0,202 | 0,040 | 0,180 |
| 400 | 0,6437 | 0,451 | 0,003 | 0,001 | 0,000 | 0,589 | 0,047 | 0,138 | 0,028 | 0,181 | 0,036 | 0,161 |
| 450 | 0,5828 | 0,408 | 0,003 | 0,001 | 0,000 | 0,534 | 0,043 | 0,125 | 0,025 | 0,164 | 0,033 | 0,226 |
| 500 | 0,5328 | 0,373 | 0,003 | 0,001 | 0,000 | 0,488 | 0,039 | 0,114 | 0,023 | 0,150 | 0,030 | 0,134 |
| 600 | 0,4557 | 0,319 | 0,002 | 0,001 | 0,000 | 0,417 | 0,033 | 0,098 | 0,020 | 0,128 | 0,026 | 0,114 |
| 700 | 0,3991 | 0,279 | 0,002 | 0,001 | 0,000 | 0,365 | 0,029 | 0,086 | 0,017 | 0,112 | 0,022 | 0,100 |
| 800 | 0,3561 | 0,249 | 0,002 | 0,001 | 0,000 | 0,326 | 0,026 | 0,076 | 0,015 | 0,100 | 0,020 | 0,089 |
| 900 | 0,3221 | 0,225 | 0,002 | 0,001 | 0,000 | 0,295 | 0,024 | 0,069 | 0,014 | 0,091 | 0,018 | 0,081 |
| 1000 | 0,2948 | 0,206 | 0,002 | 0,001 | 0,000 | 0,270 | 0,022 | 0,063 | 0,013 | 0,083 | 0,017 | 0,074 |
| 1500 | 0,2112 | 0,148 | 0,001 | 0,000 | 0,000 | 0,193 | 0,015 | 0,045 | 0,009 | 0,059 | 0,012 | 0,053 |

**Tabla 17.: Datos de entrada del modelo**

| Parámetro | Datos de entrada | Unidad |
| --- | --- | --- |
| Tipo de fuente | Área | - |
| Altura de liberación | 1,0 | m |
| Longitud de lado largo | 97 | m |
| Longitud de lado corto | 96 | m |
| Altura del receptor | 1,5 | m |
| Terreno Urbano/Rural | Urbano | - |
| Altura de la mezcla | 30 | m |
| Altura anemométrica | 5 | m |
| Clase de estabilidad | 3 | “Semi Inestable” |
| Velocidad eólica | 1,0 | m/s |

**Tabla 18.: Resultados del modelo, Fase de operación Etapa propuesta - Escenario 2**

| Distancia (m) | Concentración horaria (g/m3) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO | SOx | NOX | MP2,5 Total | MP10 Total | MPS |
| 30 | 0,7368 | 0,006638 | 80,25 | 1,065 | 1,801 | 4,55 |
| 40 | 0,7629 | 0,006873 | 83,09 | 1,103 | 1,865 | 4,711 |
| 50 | 0,787 | 0,00709 | 85,71 | 1,138 | 1,924 | 4,86 |
| 60 | 0,8095 | 0,007293 | 88,17 | 1,171 | 1,979 | 4,999 |
| 70 | 0,799 | 0,007198 | 87,02 | 1,155 | 1,95 | 4,935 |
| 80 | 0,5585 | 0,005032 | 60,83 | 0,8076 | 1,37 | 3,449 |
| 90 | 0,4328 | 0,003899 | 47,13 | 0,6257 | 1,06 | 2,673 |
| 100 | 0,3564 | 0,003211 | 38,82 | 0,5154 | 0,8713 | 2,201 |
| 150 | 0,2068 | 0,001863 | 22,53 | 0,2991 | 0,5056 | 1,277 |
| 200 | 0,1642 | 0,00148 | 17,89 | 0,2375 | 0,4014 | 1,014 |
| 250 | 0,1397 | 0,001258 | 15,21 | 0,202 | 0,3414 | 0,8626 |
| 300 | 0,1213 | 0,001093 | 13,21 | 0,1754 | 0,2965 | 0,749 |
| 350 | 0,107 | 0,0009644 | 11,66 | 0,1548 | 0,2617 | 0,6611 |
| 400 | 0,09579 | 0,000863 | 10,43 | 0,1385 | 0,2342 | 0,5916 |
| 450 | 0,08673 | 0,0007814 | 9,446 | 0,1254 | 0,212 | 0,5356 |
| 500 | 0,0793 | 0,0007144 | 8,636 | 0,1147 | 0,1938 | 0,4897 |
| 600 | 0,06783 | 0,0006111 | 7,387 | 0,09808 | 0,1658 | 0,4189 |
| 700 | 0,0594 | 0,0005352 | 6,47 | 0,08589 | 0,1452 | 0,3669 |
| 800 | 0,05299 | 0,0004774 | 5,772 | 0,07663 | 0,1295 | 0,3273 |
| 900 | 0,04794 | 0,0004319 | 5,221 | 0,06932 | 0,1172 | 0,2961 |
| 1000 | 0,04387 | 0,0003952 | 4,778 | 0,06343 | 0,1072 | 0,2709 |
| 1500 | 0,03143 | 0,0002831 | 3,423 | 0,04544 | 0,07682 | 0,1941 |

**Tabla 19.: Máximas concentraciones horarias obtenidas del modelo. Fase operación, Etapa propuesta - Escenario 2**

| Lugar | Distancia máx,<br>concentración (m) | Concentración horaria (g/m3) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lugar<br> | Distancia máx,<br>concentración (m) | <br>CO | SOx | NOX | MP2,5 Total | MP10 Tota | MPS |
| Proyecto | 60 | 0,8095 | 0,007293 | 88,17 | 1,171 | 1,979 | 4,999 |

**Tabla 20.: Factores de conversión para promedios máximos de concentración**

| Tiempo promedio | Factor conversión |
| --- | --- |
| 3 horas | 0,9 |
| 8 horas | 0,7 |
| 24 horas | 0,4 |
| Anual | 0,08 |

**Tabla 21.: Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Operación Etapa PropuestaEscenario 2**

| Parámetro | Estadístico | Máxima del<br>proyecto<br>(g/m3N) | Limite según<br>Norma<br>(g/m3) | Porcentaje<br>respecto de la<br>Norma (%) | Referencia |
| --- | --- | --- | --- | --- | --- |
| MP10 | Concentración 24 horas | 0,8 | 150 | 0,5 | D.S. N° 59 / 1998 MINSEGPRES |
| MP10 | Concentración anual | 0,2 | 50 | 0,3 | 0,3 |
| MP2,5 | Concentración 24 horas | 0,5 | 50 | 0,9 | D.S. N° 12/2011 del MMA |
| MP2,5 | Concentración anual | 0,1 | 20 | 0,5 | 0,5 |
| NOx | Concentración 1 hora | 88,2 | 400 | 22,0 | D.S. N° 114/ 2002 MINSEGPRES |
| NOx | Concentración anual | 7,1 | 100 | 7,1 | 7,1 |
| SO2 | Concentración 1 hora | 0,01 | 350 | 0,002 | D.S. N° 104/ 2018 MMA |
| SO2 | Concentración 24 horas | 0,003 | 150 | 0,002 | 0,002 |
| SO2 | Concentración anual | 0,001 | 60 | 0,001 | 0,001 |
| CO | Concentración 1 hora | 0,8 | 30.000 | 0,003 | ~~D~~.S. N° 115/2002 del MINSEGPRES |
| CO | Concentración 8 horas | 0,6 | 10.000 | 0,006 | 0,006 |
| MPS (*) | Concentración anual | 0,6 | 200 | 0,284 | Norma Suiza |
| SO2 (**) | Concentración 24 horas | 0,003 | 365 | 0,001 | D.S. N°22/2010 MINSEGPRES |
| SO2 (**) | Concentración anual | 0,001 | 80 | 0,001 | 0,001 |

**Tabla 22.: Concentraciones por distancia de los contaminantes analizados, Fase de Operación Etapa Propuesta - Escenario 2**

| Distancia (m) | Concentración horaria (g/m3) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO <br>(1 hora) | CO <br>(8 horas) | SOx <br>(1 hora) | SOx <br>(24 horas) | SOx <br>(Anual) | NOX <br>(1 hora) | NOx <br>(Anual) | MP2,5 Total<br>(24 horas) | MP2,5 Total<br>(Anual) | MP10 Total<br>(24 horas) | MP10 Total<br>(Anual) | MPSl <br>(Anual) |
| 30 | 0,7368 | 0,516 | 0,007 | 0,003 | 0,001 | 80,250 | 6,420 | 0,426 | 0,085 | 0,720 | 0,144 | 0,364 |
| 40 | 0,7629 | 0,534 | 0,007 | 0,003 | 0,001 | 83,090 | 6,647 | 0,441 | 0,088 | 0,746 | 0,149 | 0,377 |
| 50 | 0,787 | 0,551 | 0,007 | 0,003 | 0,001 | 85,710 | 6,857 | 0,455 | 0,091 | 0,770 | 0,154 | 0,389 |
| 60* | 0,8095 | 0,567 | 0,007 | 0,003 | 0,001 | 88,170 | 7,054 | 0,468 | 0,094 | 0,792 | 0,158 | 0,400 |
| 70 | 0,799 | 0,559 | 0,007 | 0,003 | 0,001 | 87,020 | 6,962 | 0,462 | 0,092 | 0,781 | 0,156 | 0,395 |
| 80 | 0,5585 | 0,391 | 0,005 | 0,002 | 0,000 | 60,830 | 4,866 | 0,323 | 0,065 | 0,546 | 0,109 | 0,276 |
| 90 | 0,4328 | 0,303 | 0,004 | 0,002 | 0,000 | 47,130 | 3,770 | 0,250 | 0,050 | 0,423 | 0,085 | 0,214 |
| 100 | 0,3564 | 0,249 | 0,003 | 0,001 | 0,000 | 38,820 | 3,106 | 0,206 | 0,041 | 0,349 | 0,070 | 0,176 |
| 150 | 0,2068 | 0,145 | 0,002 | 0,001 | 0,000 | 22,530 | 1,802 | 0,120 | 0,024 | 0,202 | 0,040 | 0,102 |
| 200 | 0,1642 | 0,115 | 0,001 | 0,001 | 0,000 | 17,890 | 1,431 | 0,095 | 0,019 | 0,161 | 0,032 | 0,081 |
| 250 | 0,1397 | 0,098 | 0,001 | 0,001 | 0,000 | 15,210 | 1,217 | 0,081 | 0,016 | 0,137 | 0,027 | 0,069 |
| 300 | 0,1213 | 0,085 | 0,001 | 0,000 | 0,000 | 13,210 | 1,057 | 0,070 | 0,014 | 0,119 | 0,024 | 0,060 |
| 350 | 0,107 | 0,075 | 0,001 | 0,000 | 0,000 | 11,660 | 0,933 | 0,062 | 0,012 | 0,105 | 0,021 | 0,053 |
| 400 | 0,09579 | 0,067 | 0,001 | 0,000 | 0,000 | 10,430 | 0,834 | 0,055 | 0,011 | 0,094 | 0,019 | 0,047 |
| 450 | 0,08673 | 0,061 | 0,001 | 0,000 | 0,000 | 9,446 | 0,756 | 0,050 | 0,010 | 0,085 | 0,017 | 0,043 |
| 500 | 0,0793 | 0,056 | 0,001 | 0,000 | 0,000 | 8,636 | 0,691 | 0,046 | 0,009 | 0,078 | 0,016 | 0,039 |
| 600 | 0,06783 | 0,047 | 0,001 | 0,000 | 0,000 | 7,387 | 0,591 | 0,039 | 0,008 | 0,066 | 0,013 | 0,034 |
| 700 | 0,0594 | 0,042 | 0,001 | 0,000 | 0,000 | 6,470 | 0,518 | 0,034 | 0,007 | 0,058 | 0,012 | 0,029 |
| 800 | 0,05299 | 0,037 | 0,000 | 0,000 | 0,000 | 5,772 | 0,462 | 0,031 | 0,006 | 0,052 | 0,010 | 0,026 |
| 900 | 0,04794 | 0,034 | 0,000 | 0,000 | 0,000 | 5,221 | 0,418 | 0,028 | 0,006 | 0,047 | 0,009 | 0,024 |
| 1000 | 0,04387 | 0,031 | 0,000 | 0,000 | 0,000 | 4,778 | 0,382 | 0,025 | 0,005 | 0,043 | 0,009 | 0,022 |
| 1500 | 0,03143 | 0,022 | 0,000 | 0,000 | 0,000 | 3,423 | 0,274 | 0,018 | 0,004 | 0,031 | 0,006 | 0,016 |

**Tabla 23.: Datos de entrada del modelo**

| Parámetro | Datos de entrada | Unidad |
| --- | --- | --- |
| Tipo de fuente | Área | - |
| Altura de liberación | 1,0 | m |
| Longitud de lado largo | 240 | m |
| Longitud de lado corto | 210 | m |
| Altura del receptor | 1,5 | m |
| Terreno Urbano/Rural | Urbano | - |
| Altura de la mezcla | 30 | m |
| Altura anemométrica | 5 | m |
| Clase de estabilidad | 3 | “Semi Inestable” |
| Velocidad eólica | 1,0 | m/s |

**Tabla 24.: Resultados del modelo, Fase de operación Proyecto total - Escenario 3**

| Distancia (m) | Concentración horaria (g/m3) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO | SOx | NOX | MP2,5 Total | MP10 Total | MPS |
| 50 | 1,084 | 0,01022 | 118,2 | 1,569 | 2,652 | 6,701 |
| 60 | 1,106 | 0,01042 | 120,5 | 1,6 | 2,704 | 6,833 |
| 70 | 1,127 | 0,01062 | 122,8 | 1,631 | 2,756 | 6,964 |
| 80 | 1,15 | 0,01083 | 125,3 | 1,664 | 2,812 | 7,106 |
| 90 | 1,172 | 0,01104 | 127,7 | 1,695 | 2,865 | 7,24 |
| 100 | 1,193 | 0,01124 | 130 | 1,727 | 2,918 | 7,374 |
| 110 | 1,215 | 0,01145 | 132,4 | 1,758 | 2,971 | 7,507 |
| 120 | 1,237 | 0,01165 | 134,7 | 1,789 | 3,025 | 7,642 |
| 130 | 1,259 | 0,01186 | 137,1 | 1,821 | 3,078 | 7,776 |
| 140 | 1,28 | 0,01206 | 139,5 | 1,852 | 3,131 | 7,911 |
| 150 | 1,301 | 0,01226 | 141,7 | 1,882 | 3,182 | 8,039 |
| 160 | 1,324 | 0,01248 | 144,3 | 1,916 | 3,239 | 8,184 |
| 170 | 1,042 | 0,009819 | 113,5 | 1,508 | 2,549 | 6,44 |
| 180 | 0,8899 | 0,008384 | 96,95 | 1,288 | 2,176 | 5,499 |
| 190 | 0,7992 | 0,007529 | 87,07 | 1,156 | 1,954 | 4,938 |
| 200 | 0,7395 | 0,006967 | 80,57 | 1,07 | 1,808 | 4,569 |
| 250 | 0,6086 | 0,005734 | 66,3 | 0,8805 | 1,488 | 3,76 |
| 300 | 0,5583 | 0,00526 | 60,83 | 0,8078 | 1,365 | 3,45 |
| 350 | 0,5187 | 0,004887 | 56,51 | 0,7504 | 1,268 | 3,205 |
| 400 | 0,4827 | 0,004548 | 52,59 | 0,6985 | 1,181 | 2,983 |
| 450 | 0,4505 | 0,004244 | 49,08 | 0,6517 | 1,102 | 2,783 |
| 500 | 0,4216 | 0,003972 | 45,94 | 0,6101 | 1,031 | 2,605 |
| 1000 | 0,2549 | 0,002402 | 27,77 | 0,3688 | 0,6234 | 1,575 |
| 1500 | 0,1861 | 0,001753 | 20,28 | 0,2693 | 0,4552 | 1,15 |

**Tabla 25.: Máximas concentraciones horarias obtenidas del modelo. Fase operación, Proyecto total - Escenario 3**

| Lugar | Distancia máx,<br>concentración (m) | Concentración horaria (g/m3) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lugar<br> | Distancia máx,<br>concentración (m) | <br>CO | SOx | NOX | MP2,5 Total | MP10 Tota | MPS |
| Proyecto | 160 | 1,324 | 0,01248 | 144,3 | 1,916 | 3,239 | 8,184 |

**Tabla 26.: Factores de conversión para promedios máximos de concentración**

| Tiempo promedio | Factor conversión |
| --- | --- |
| 3 horas | 0,9 |
| 8 horas | 0,7 |
| 24 horas | 0,4 |
| Anual | 0,08 |

**Tabla 27.: Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase Operación Proyecto totalEscenario 3**

| Parámetro | Estadístico | Máxima del<br>proyecto<br>(g/m3N) | Limite según<br>Norma<br>(g/m3) | Porcentaje<br>respecto de la<br>Norma (%) | Referencia |
| --- | --- | --- | --- | --- | --- |
| MP10 | Concentración 24 horas | 1,30 | 150 | 0,9 | D.S. N° 59 / 1998 MINSEGPRES |
| MP10 | Concentración anual | 0,26 | 50 | 0,5 | 0,5 |
| MP2,5 | Concentración 24 horas | 0,77 | 50 | 1,5 | D.S. N° 12/2011 del MMA |
| MP2,5 | Concentración anual | 0,15 | 20 | 0,8 | 0,8 |
| NOx | Concentración 1 hora | 144,30 | 400 | 36,1 | D.S. N° 114/ 2002 MINSEGPRES |
| NOx | Concentración anual | 11,54 | 100 | 11,5 | 11,5 |
| SO2 | Concentración 1 hora | 0,01 | 350 | 0,004 | D.S. N° 104/ 2018 MMA |
| SO2 | Concentración 24 horas | 0,005 | 150 | 0,003 | 0,003 |
| SO2 | Concentración anual | 0,001 | 60 | 0,002 | 0,002 |
| CO | Concentración 1 hora | 1,32 | 30.000 | 0,004 | ~~D~~.S. N° 115/2002 del MINSEGPRES |
| CO | Concentración 8 horas | 0,93 | 10.000 | 0,009 | 0,009 |
| MPS (*) | Concentración anual | 0,65 | 200 | 0,3 | Norma Suiza |
| SO2 (**) | Concentración 24 horas | 0,005 | 365 | 0,001 | D.S. N°22/2010 MINSEGPRES |
| SO2 (**) | Concentración anual | 0,001 | 80 | 0,001 | 0,001 |

**Tabla 28.: Concentraciones por distancia de los contaminantes analizados, Fase de Operación Proyecto total - Escenario 3**

| Distancia (m) | Concentración horaria (g/m3) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO <br>(1 hora) | CO <br>(8 horas) | SOx <br>(1 hora) | SOx <br>(24 horas) | SOx <br>(Anual) | NOX <br>(1 hora) | NOx <br>(Anual) | MP2,5 Total<br>(24 horas) | MP2,5 Total<br>(Anual) | MP10 Total<br>(24 horas) | MP10 Total<br>(Anual) | MPSl <br>(Anual) |
| 50 | 1,084 | 0,759 | 0,010 | 0,004 | 0,001 | 118,20 | 9,456 | 0,628 | 0,126 | 1,061 | 0,212 | 0,536 |
| 60 | 1,106 | 0,774 | 0,010 | 0,004 | 0,001 | 120,50 | 9,640 | 0,640 | 0,128 | 1,082 | 0,216 | 0,547 |
| 70 | 1,127 | 0,789 | 0,011 | 0,004 | 0,001 | 122,80 | 9,824 | 0,652 | 0,130 | 1,102 | 0,220 | 0,557 |
| 80 | 1,15 | 0,805 | 0,011 | 0,004 | 0,001 | 125,30 | 10,024 | 0,666 | 0,133 | 1,125 | 0,225 | 0,568 |
| 90 | 1,172 | 0,820 | 0,011 | 0,004 | 0,001 | 127,70 | 10,216 | 0,678 | 0,136 | 1,146 | 0,229 | 0,579 |
| 100 | 1,193 | 0,835 | 0,011 | 0,004 | 0,001 | 130,00 | 10,400 | 0,691 | 0,138 | 1,167 | 0,233 | 0,590 |
| 110 | 1,215 | 0,851 | 0,011 | 0,005 | 0,001 | 132,40 | 10,592 | 0,703 | 0,141 | 1,188 | 0,238 | 0,601 |
| 120 | 1,237 | 0,866 | 0,012 | 0,005 | 0,001 | 134,70 | 10,776 | 0,716 | 0,143 | 1,210 | 0,242 | 0,611 |
| 130 | 1,259 | 0,881 | 0,012 | 0,005 | 0,001 | 137,10 | 10,968 | 0,728 | 0,146 | 1,231 | 0,246 | 0,622 |
| 140 | 1,28 | 0,896 | 0,012 | 0,005 | 0,001 | 139,50 | 11,160 | 0,741 | 0,148 | 1,252 | 0,250 | 0,633 |
| 150 | 1,301 | 0,911 | 0,012 | 0,005 | 0,001 | 141,70 | 11,336 | 0,753 | 0,151 | 1,273 | 0,255 | 0,643 |
| 160 | 1,324 | 0,927 | 0,012 | 0,005 | 0,001 | 144,30 | 11,544 | 0,766 | 0,153 | 1,296 | 0,259 | 0,655 |
| 170 | 1,042 | 0,729 | 0,010 | 0,004 | 0,001 | 113,50 | 9,080 | 0,603 | 0,121 | 1,020 | 0,204 | 0,515 |
| 180 | 0,8899 | 0,623 | 0,008 | 0,003 | 0,001 | 96,95 | 7,756 | 0,515 | 0,103 | 0,870 | 0,174 | 0,440 |
| 190 | 0,7992 | 0,559 | 0,008 | 0,003 | 0,001 | 87,07 | 6,966 | 0,462 | 0,092 | 0,782 | 0,156 | 0,395 |
| 200 | 0,7395 | 0,518 | 0,007 | 0,003 | 0,001 | 80,57 | 6,446 | 0,428 | 0,086 | 0,723 | 0,145 | 0,366 |
| 250 | 0,6086 | 0,426 | 0,006 | 0,002 | 0,000 | 66,30 | 5,304 | 0,352 | 0,070 | 0,595 | 0,119 | 0,301 |
| 300 | 0,5583 | 0,391 | 0,005 | 0,002 | 0,000 | 60,83 | 4,866 | 0,323 | 0,065 | 0,546 | 0,109 | 0,276 |
| 350 | 0,5187 | 0,363 | 0,005 | 0,002 | 0,000 | 56,51 | 4,521 | 0,300 | 0,060 | 0,507 | 0,101 | 0,256 |
| 400 | 0,4827 | 0,338 | 0,005 | 0,002 | 0,000 | 52,59 | 4,207 | 0,279 | 0,056 | 0,472 | 0,094 | 0,239 |
| 450 | 0,4505 | 0,315 | 0,004 | 0,002 | 0,000 | 49,080 | 3,926 | 0,261 | 0,052 | 0,441 | 0,088 | 0,223 |
| 500 | 0,4216 | 0,295 | 0,004 | 0,002 | 0,000 | 45,940 | 3,675 | 0,244 | 0,049 | 0,412 | 0,082 | 0,208 |
| 1000 | 0,2549 | 0,178 | 0,002 | 0,001 | 0,000 | 27,770 | 2,222 | 0,148 | 0,030 | 0,249 | 0,050 | 0,126 |
| 1500 | 0,1861 | 0,130 | 0,002 | 0,001 | 0,000 | 20,280 | 1,622 | 0,108 | 0,022 | 0,182 | 0,036 | 0,092 |
