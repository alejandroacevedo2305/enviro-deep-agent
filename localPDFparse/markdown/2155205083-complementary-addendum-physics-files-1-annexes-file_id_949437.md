---
title: Sin título
author: SGA
date: D:20231013081455-03'00'
language: es
type: report
pages: 72
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 4 ACTUALIZACIÓN MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA
-->

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

# ANEXO 4 ACTUALIZACIÓN MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA

**Rosario Norte 100 Piso 14, Las Condes, Santiago, Chile. Fono: 562-2580 6500;**

**[e-mail: contacto@sgasa.cl;](mailto:contacto@sgasa.cl)** **[www.sgasa.cl](http://www.sgasa.cl/)**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**ÍNDICE**

**1** **INTRODUCCIÓN ...................................................................................................................... 1**
**2** **RESUMEN DE ESTIMACIÓN DE EMISIONES .............................................................................. 3**
**3** **MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES ............................................................... 3**

3.1 MARCO LEGAL ......................................................................................................................... 3
3.2 LÍNEA DE BASE ......................................................................................................................... 4
3.3 BASE TEÓRICA DEL MODELO UTILIZADO ................................................................................. 6

3.4 ESCENARIO DE EMISIONES ...................................................................................................... 8
3.5 RECEPTORES DE INTERÉS ...................................................................................................... 10
3.6 DOMINIO DE MODELACIÓN .................................................................................................. 12
3.7 TOPOGRAFÍA ......................................................................................................................... 14

3.8 USO DE SUELOS ..................................................................................................................... 15
3.9 ANÁLISIS DE INCERTIDUMBRE ............................................................................................... 16
3.10 RESULTADOS DE LA IMPLEMENTACIÓN DEL MODELO ......................................................... 16

3.10.1 Aportes del proyecto ........................................................................................................... 16
3.10.2 Puntos de Máximo Impacto ................................................................................................. 25
3.10.3 Isolíneas de Concentración y Depositación ......................................................................... 25
3.10.4 Aporte otros proyectos con RCA aprobada ......................................................................... 40
3.10.5 Calidad de Aire Proyectada .................................................................................................. 44

**4** **CONCLUSIONES .................................................................................................................... 67**

**ÍNDICE DE TABLAS**

Tabla 1.Resumen Estimación de Emisiones ............................................................................................. 3

Tabla 2. Normas de Calidad del Aire Consideradas en el Estudio. ........................................................... 4

Tabla 3. Línea de Base de Calidad del Aire y ubicación de Estaciones de monitoreo dentro del Dominio.

............................................................................................................................................... 5

Tabla 4. Línea de Base Estación Pozo Almonte (g/m [3] N). ....................................................................... 5
Tabla 5. Línea de Base Estación Alto Hospicio (g/m [3] N). ........................................................................ 6
Tabla 6. Tasa de Emisión Consideradas Año Fase de Operación. ............................................................ 9
Tabla 7. Coordenadas de los receptores ................................................................................................ 10

Tabla 8 Detalle Archivo WRF .................................................................................................................. 12
Tabla 9. Aporte del Proyecto Material Particulado Respirable MP10 y MP2,5 (μg/m [3] N) - Año Fase de

Operación ............................................................................................................................ 17
Tabla 10. Aporte del Proyecto Material Particulado Sedimentable MPS (mg/m [2] -día) Norma Secundaria

- Año Fase de Operación .................................................................................................... 18
Tabla 11. Aporte del Proyecto Dióxido de Nitrógeno NO 2 (μg/m [3] N) - Año Fase de Operación ............ 19
Tabla 12. Aporte del Proyecto Monóxido de Carbono CO (μg/m [3] N) - Año Fase de Operación ............ 21
Tabla 13. Aporte del Proyecto Dióxido de Azufre (SO 2 ) Norma Primaria (μg/m [3] N) - Año Fase de

Operación ............................................................................................................................ 22
Tabla 14. Aporte del Proyecto Dióxido de Azufre (SO 2 ) Norma Secundaria (μg/m [3] N) - Año Fase de

Operación ............................................................................................................................ 23
Tabla 15. Coordenadas del Punto de Máximo Impacto (PMI) ............................................................... 25

Actualización Modelación dispersión atmosférica **i**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

Tabla 16. Lista de otros Proyectos con RCA evaluados .......................................................................... 41
**Tabla 17. Aporte de otros Proyectos con RCA evaluados (ug/m3N)** ................................................... 42

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- asimilables a los considerados en el presente proyecto De esta forma, para los proyectos mencionados en la Tabla 16, existen antecedentes de concentraciones seleccionables, estimando sus aportes en distintos receptores de interés, entre los cuales se incluyen al menos una vez alguno de los receptores considerados en este Proyecto. Así, en la -->

**Tabla 17: se resumen los aportes cuantificados en dichas evaluaciones ambientales para los eceptores**

| Col1 | DECLARACIÓN DE IMPACTO AMBIENTAL | Col3 |
| --- | --- | --- |
|  | PLANTA DE BENEFICIO DE SALES DE NITRATOS | PLANTA DE BENEFICIO DE SALES DE NITRATOS |

<!-- Estadísticas: 1 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 16. Lista de otros Proyectos con RCA evaluados** |ID|Nombre Proyecto|Receptor en que estima aportes| |---|---|---| -->
<!-- FIN TABLA 17 -->

**Tabla 18. Concentraciones Proyectadas de MP10** ............................................................................... 44
**Tabla 19. Concentraciones Proyectadas de MP2,5** .............................................................................. 47
**Tabla 20. Concentraciones Proyectadas de NO2** .................................................................................. 50
**Tabla 21. Concentraciones Proyectadas de CO** .................................................................................... 53
**Tabla 22. Concentraciones Proyectadas de SO2 Norma Primaria** ....................................................... 56
**Tabla 23. Concentraciones Proyectadas de SO2 Norma Secundaria** ................................................... 61
**Tabla 24. Tasas de Depositación Proyectadas de MPS** ........................................................................ 65

**ÍNDICE DE FIGURAS**

Figura 1. Ubicación del Proyecto a nivel regional. ................................................................................... 2
Figura 2. Representación Gráfica del Modelo Tipo Puff y de Pluma........................................................ 7
Figura 3. Ubicación de Receptores de Interés........................................................................................ 11
Figura 4. Dominio de Modelación .......................................................................................................... 13
Figura 5. Topografías de la Zona. ........................................................................................................... 14
Figura 6. Usos de suelo en el área de modelación ................................................................................. 15
Figura 7. Isoconcentración Aportes MP10 Promedio Anual - Fase de Operación ................................ 26
Figura 8. Isoconcentración Aportes MP10 Percentil 98 Diario - Fase de Operación............................. 27
Figura 9. Isoconcentración Aportes MP2,5 Promedio Anual - Fase de Operación ............................... 28
Figura 10. Isoconcentración Aportes MP2,5 Percentil 98 Diario - Fase de Operación ......................... 29
Figura 11. Isoconcentración Aportes NO 2 Promedio Anual - Fase de Operación ................................. 30
Figura 12. Isoconcentración Aportes NO 2 Percentil 99 Horario - Fase de Operación ........................... 31
Figura 13. Isoconcentración Aportes CO Percentil 99 Horario - Fase de Operación ............................. 32
Figura 14. Isoconcentración Aportes CO Percentil 99 8 Horas - Fase de Operación............................. 33
Figura 15. Isoconcentración Aportes SO 2 Promedio Anual - Fase de Operación .................................. 34
Figura 16. Isoconcentración Aportes SO 2 Percentil 99 Diario - Fase de Operación .............................. 35
Figura 17. Isoconcentración Aportes SO 2 Percentil 98,5 Horario - Fase de Operación ......................... 36
Figura 18. Isoconcentración Aportes SO 2 Percentil 99,7 Diario - Fase de Operación ........................... 37
Figura 19. Isoconcentración Aportes SO 2 Percentil 99,73 Horario - Fase de Operación ....................... 38
Figura 20. Isodepositación Aportes de MPS Promedio Anual - Fase de Operación .............................. 39

**APÉNDICES**

Apéndice 1: Actualización Archivos Digitales de Modelación

Apéndice 2: Archivos kmz Isolíneas, Receptores y Obras del Proyecto

Actualización Modelación dispersión atmosférica **ii**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**1** **INTRODUCCIÓN**

En este anexo se presenta la actualización de la modelación de emisiones atmosféricas de los
contaminantes: material particulado (MP10, MP2,5 y MPS) y gases de combustión (CO, NO x y SO 2 ) del
Proyecto “Planta de Beneficio de Sales de Nitrato”, en adelante “el Proyecto”.

El Proyecto consiste en la operación de una Planta de Beneficio de Sales de Nitrato por un periodo de
20 años, para la producción de 200.000 t/año de Nitrato de Potasio y 120.000 t/año de Nitrato de Sodio.
Para lo anterior, se considera utilizar las instalaciones existentes en el sector de producción de Nitrato
de la faena Cala-Cala, conformado por el Área de Evaporación Solar y la Planta de Beneficio, junto a la
construcción de nuevas obras dentro del mismo sector. Cabe señalar que la ejecución del Proyecto no
modificará ni intervendrá la operación del Área Mina de la faena Cala-Cala, Planta Química ni Planta

Refinadora.

En relación a las nuevas obras, el Proyecto considera la construcción de 14 piscinas de evaporación
solar, además de una bodega de RESPEL para el almacenamiento temporal de residuos y la ampliación
del patio de salvataje. Adicionalmente, se considera la habilitación de huellas de acceso a las nuevas
piscinas de evaporación y la construcción de una fosa séptica con sus respectivas instalaciones

sanitarias.

La Planta de Beneficio de Sales de Nitrato, posee una Planta de Cristalizado y una Planta de Prilado con
las cuales se produce Nitrato de Sodio y Nitrato de Potasio a partir de Sales Ricas en Nitratos (sales con
un contenido medio de Nitratos de 30% - 40%) obtenidas en el Área de Evaporación Solar de Faena

Cala-Cala.

Dicho esto, en La Figura 1 muestra la ubicación del Proyecto a nivel regional

Actualización Modelación dispersión atmosférica **1**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 1. Ubicación del Proyecto a nivel regional.**

Fuente: Elaborado por MYMA.

Actualización Modelación dispersión atmosférica **2**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**2** **RESUMEN DE ESTIMACIÓN DE EMISIONES**

La estimación de emisiones del Proyecto se realizó aplicando los factores de emisión y fórmulas
propuestas por la Agencia de Protección Ambiental de los EE.UU. en el documento “AP-42 5th
Edición”, complementando esta información con informe final de B&S Consultores (2015)
denominado “Servicio de Recopilación y sistematización de factores de emisión al aire para el
Servicio de Evaluación Ambiental” y, a modo referencial, la “Guía para la Estimación de Emisiones
Atmosféricas en la Región Metropolitana” (2020). El detalle de este cálculo se presenta en el Anexo
de “Actualización de Estimación de Emisiones” de esta Adenda Complementaria.

Para efectos de modelación atmosférica fue elegida un año normal de la fase de operación, ya que
en esta fase el proyecto alcanza las mayores emisiones atmosféricas anuales.

Sobre la Fase de Operación evaluada, resulta importante señalar que, las emisiones de operación
estimadas corresponden a la operación futura, las cuales son equivalentes en magnitud a la
operación actual, debido a que las modificaciones presentadas en este proyecto no alteran la
capacidad productiva autorizada de la planta, ya que, más bien están asociadas a mejoras en la

infraestructura de la misma.

A continuación, en la Tabla 1 se muestra el resumen de las emisiones de material particulado
respirable (MP10), fino (MP2,5), sedimentable(MPS), óxidos de nitrógeno (NOx), monóxido de
carbono (CO) y dióxido de azufre (SO 2 ), correspondiente a cada período y escenario descrito

anteriormente.

**Tabla 1.Resumen Estimación de Emisiones**

|Fase|Emisiones (t/año)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Fase**|**MP10**|**MP2,5**|**MPS**|**NOx**|**CO**|**SO2 **|
|Construcción|18,5426|2,9018|67,6981|4,6763|2,3694|0,0102|
|Operación|122,1264|28,3002|535,0672|89,5855|28,4720|0,3615|
|Cierre|18,5426|2,9018|67,6981|4,6763|2,3694|0,0102|

Fuente: Elaboración propia

**3** **MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES**

**3.1** **Marco Legal**

La siguiente modelación determinará el efecto en las cercanías del Proyecto, producto de las
emisiones de Material Particulado Respirable (MP10), Fino (MP2,5), sedimentable (MPS), además
de los gases generados por las actividades asociadas a la fase de operación durante el escenario de

modelación indicado anteriormente.

En el contexto legal, existen normas primarias y secundarias asociadas a los contaminantes de las
emisiones atmosféricas generadas en el Proyecto. Los estadísticos a evaluar se presentan en la Tabla

2:

Actualización Modelación dispersión atmosférica **3**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 2. Normas de Calidad del Aire Consideradas en el Estudio.**

|Parámetro|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|
|MP10|Primaria|Promedio Anual1|50g/m3N|D.S. N° 12/2022 del MMA|
|MP10|Primaria|Percentil 98 promedio diario|130g/m3N|130g/m3N|
|MP2,5|Primaria|Promedio Anual1|20g/m3N|D.S. N° 12/2011 del MMA|
|MP2,5|Primaria|Percentil 98 promedio diario|50g/m3N|50g/m3N|
|NO2|Primaria|Promedio Anual1|100g/m3N|D.S. N° 114/2002 del<br>MINSEGPRES|
|NO2|Primaria|Percentil 99 máx. 1 hora1|400g/m3N|400g/m3N|
|CO|Primaria|Percentil 99 1 hora1|30 mg/m3N|D.S. N° 115/2002 del<br>MINSEGPRES|
|CO|Primaria|Percentil 99 8 hora1|10 mg/m3N|10 mg/m3N|
|SO2|Primaria|Promedio Anual1|60 μg/m3N|D.S. N° 104/2018 del MMA|
|SO2|Primaria|Percentil 99 24 horas1|150 μg/m3N|150 μg/m3N|
|SO2|Primaria|Percentil 98,5 1 hora1|350 μg/m3N|350 μg/m3N|
|SO2|Secundaria|Promedio Anual1|80 μg/m3N|D.S. N° 22/2010 del<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 24 horas1|365 μg/m3N|365 μg/m3N|
|SO2|Secundaria|Percentil 99,73 1 hora1|1000 μg/m3N|1000 μg/m3N|
|MPS|Secundaria|Promedio Anual|200 mg/m2-día|Ordenanza Suiza|

Fuente: Elaboración propia

**3.2** **Línea de Base**

Para establecer la línea de base de calidad del aire del Proyecto, se realizó una recopilación y
actualización de la información de la estación Pozo Almonte, pertenecientes a COSAYACH, además
de la estación Alto Hospicio, de propiedad del Ministerio del Medio Ambiente y disponible en el
Sistema de Información Nacional de Calidad del Aire (SINCA), ambas incluidas dentro del dominio

de modelación.

La caracterización de la calidad del aire se realiza analizando las concentraciones de MP10, MP2,5 y
SO 2, según la información disponible, durante el periodo comprendido entre los años 2018 y 2020.
El detalle de este análisis se presenta en el anexo de Línea de base de calidad de aire de esta DIA.
En la Tabla 3 se presentan las coordenadas de ubicación de cada estación y los parámetros que se

miden en ella.

1 Aplicable al promedio anual de tres años consecutivos.

Actualización Modelación dispersión atmosférica **4**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 3. Línea de Base de Calidad del Aire y ubicación de Estaciones de monitoreo dentro del**

**Dominio.**

|Estación|Coordenada UTM WGS84 (Huso 19)|Col3|Parámetros<br>calidad del aire|Periodo|Administrada por|
|---|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Pozo Almonte|417.709|7.760.617|MP10, MP2,5, SO2|2018 - 2020|COSAYACH|
|Alto Hospicio|385.118|7.755.989|MP2,5|2018 - 2020|MMA|

Fuente: Elaboración propia

A continuación, se presentan los valores de Línea de Base medido en las 2 estaciones. En la Tabla 4
se presentan los estadísticos del monitoreo de MP10, MP2,5 y SO 2 para los tres periodos analizados

en la estación Pozo Almonte.

**Tabla 4. Línea de Base Estación Pozo Almonte (**  **g/m** **[3]** **N).**

|Contaminante|Estadístico|Año|Col4|Col5|Valor|Valor Norma|% de la Norma|
|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadístico**|**2018**|**2019**|**2020**|**2020**|**2020**|**2020**|
|MP10|Promedio Anual|34,5|36,4|31,3|34,1|50|68%|
|MP10|Percentil 98 24 horas|66,0|68,0|62,9|65,6|130|50%|
|MP2,5|Promedio Anual|8,7|8,0|10,7|9,1|20|46%|
|MP2,5|Percentil 98 24 horas|7,0|17,0|28,8|17,6|50|35%|
|SO2 (Primaria)|Promedio Anual|1,6|1,7|4,6|2,6|60|4%|
|SO2 (Primaria)|Percentil 99 24 horas|3,8|4,3|9,3|5,8|150|4%|
|SO2 (Primaria)|Percentil 98,5 1 hora|5,3|6,2|12,8|8,1|350|2%|
|SO2 <br>(Secundaria)|Promedio Anual|1,6|1,7|4,6|2,6|80|3%|
|SO2 <br>(Secundaria)|Percentil 99,7 24 horas|4,0|4,6|13,7|7,4|365|2%|
|SO2 <br>(Secundaria)|Percentil 99,73 1 hora|7,9|11,5|27,5|15,6|1000|2%|

Fuente: Elaboración propia

En la Tabla anterior se observa que la media trianual y las normas diarias de MP10 y MP2,5 no
sobrepasan los límites establecidos por el D.S. 12/2022 y D.S. 12/2011, ni tampoco se encuentran
en rango de latencia. En el caso del SO 2, tanto para la norma primaria como secundaria, no se
sobrepasan los límites de latencia y saturación respectivos.

En la Tabla 5 se presentan los estadísticos del monitoreo de MP2,5 para los tres periodos analizados
en la estación Alto Hospicio.

Actualización Modelación dispersión atmosférica **5**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 5. Línea de Base Estación Alto Hospicio (**  **g/m** **[3]** **N).**

|Contaminante|Estadístico|Año|Col4|Col5|Valor|Valor Norma|% de la Norma|
|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadístico**|**2018**|**2019**|**2020**|**2020**|**2020**|**2020**|
|MP2,5|Promedio Anual|11,2|11,1|10,3|10,9|20|54%|
|MP2,5|Percentil 98 24 horas|21,6|19,0|18,7|19,8|50|40%|

Fuente: Elaboración propia

En la Tabla anterior se observa que tanto para la media trianual como para el percentil 98 diario, no
se sobrepasan los límites de saturación y latencia establecidos para MP2,5 mediante el D.S. 12/2011.

En vista de los resultados expuestos de línea de base de calidad de aire, se puede descartar la
condición de riesgo preexistente para la evaluación de cumplimiento, dado que todos los registros
estadísticos informados están bajo los límites normativos.

**3.3** **Base Teórica del Modelo Utilizado**

El modelo utilizado para determinar el efecto que tendrán las emisiones de Material Particulado
Respirable (MP-10), Fino (MP-2,5), sedimentable (MPS) y los gases (NO x, SO x y CO) generadas en el
escenario representado por un año de fase de operación del Proyecto, corresponde al sistema de

modelación “WRF-CALPUFF”.

El sistema de modelación incluye tres componentes principales: WRF, CALPUFF y CALPOST, además
de una larga selección de preprocesadores diseñados para incluir en el modelo datos
meteorológicos y geofísicos.

WRF es un sistema de predicción numérico de mesoescala no hidrostático (considera los
movimientos verticales), usado con fines de pronóstico operacional y en investigación de la
atmósfera. Los principales componentes de este modelo son las fuentes externas de datos, como
son los datos de entrada y la información geográfica, el sistema de pre-procesamiento, el modelo
WRF-ARW y los sistemas de post-procesamiento.

CALPUFF es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario capaz de modelar el
transporte y dispersión de contaminantes sobre la base entregada por el Servicio Evaluación
Ambiental (SEA). Los modelos tipo “puff” representan una pluma de contaminantes continuo como
un número discreto de paquetes de material contaminante. El modelo evalúa la contribución de un
“puff” en la concentración atmosférica de un receptor en un instante determinado, para luego
permitir que el puff se mueva, evolucione en tamaño, fuerza, etc., hasta la próxima iteración. Luego,
la concentración total en un receptor resultará de la sumatoria de las contribuciones de todos los
“puff”. La ecuación básica del modelo se muestra a continuación:

Actualización Modelación dispersión atmosférica **6**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

Donde:

C: Concentración (g/m [3] )

Q: Masa del contaminante en el “puff” (g)

σx: Coeficiente de dispersión en dirección del viento (m)

σy: Coeficiente de dispersión en dirección perpendicular al viento (m)

σz: Coeficiente de dispersión vertical (m)

da: Distancia desde el centro del “puff” hacia el receptor en el eje de la dirección del viento
(m)

dc: Distancia desde el centro del “puff” hacia el receptor en el eje perpendicular a la
dirección del viento (m)

g: Altura de la ecuación gaussiana (m)

H: Altura efectiva del “puff” (m)

h: Altura de la capa de mezcla (m)

A diferencia de un modelo de pluma, los modelos de tipo “puff” consideran las emisiones (de los
puff) independientes de su fuente de emisión permitiendo que los “puff” respondan a la
meteorología en la que se encuentra inmerso en cada instante. Lo anterior se representa
esquemáticamente en la siguiente Figura 2.

**Figura 2. Representación Gráfica del Modelo Tipo Puff y de Pluma.**

Fuente: Lakes Environmental.

Actualización Modelación dispersión atmosférica **7**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

Finalmente, CALPOST procesa las salidas de CALPUFF creando los archivos con las tabulaciones
necesarias para la evaluación de los resultados según los estadísticos establecidos en las normas de

calidad del aire.

**3.4** **Escenario de Emisiones**

Se ha considerado para la modelación de dispersión de contaminantes un año de emisiones para la
fase de operación, ya que durante un año de esta fase el proyecto alcanza las mayores emisiones
atmosféricas, tal como se menciona en la sección 2.2.

Sobre la Fase de Operación evaluada, se reitera que, las emisiones de operación estimadas
corresponden a la operación futura, las cuales son equivalentes en magnitud a la operación actual,
debido a que las modificaciones presentadas en este proyecto no alteran la capacidad productiva
autorizada de la planta, ya que, más bien están asociadas a mejoras en la infraestructura de la

misma .

La tasa de emisión y características de cada una de las fuentes consideradas del Proyecto, se han
estimado a partir de los resultados del cálculo de emisiones indicado en la Tabla 1.

El detalle de los datos ingresados al modelo se encuentra en los archivos de entrada en el Apéndice
1 adjuntados como respaldo digital al presente documento. En cuanto al detalle de las isolíneas de
concentración y depositación resultantes, la ubicación de los receptores de interés y las obras del
proyecto asociadas a la modelación Calpuff, estas se presentan en formato kmz en el Apéndice 2 de

este documento.

A continuación, en la Tabla 6 se resumen las tasas de emisión asociado al escenario de modelación
representado por un año de la fase de operación del Proyecto.

Actualización Modelación dispersión atmosférica **8**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 6. Tasa de Emisión Consideradas Año Fase de Operación.**

|ID<br>Fuente|Fase Emisión|Fuente|Tipo|Largo|Ancho|Área (m2)|Tasas de emisión|Col9|Col10|Col11|Col12|Col13|Unidad<br>Tasas de<br>Emisión|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Fuente**|**Fase Emisión**|**Fuente**|**Tipo**|**Largo**|**Ancho**|**Área (m2)**|**MPS**|**MP10**|**MP2,5**|**NOx**|**SO2**|**CO**|**CO**|
|SRC_1|Operación|Caldera|Puntual|--|--|--|2,32E+00|2,32E+00|2,32E+00|3,94E+01|1,70E-01|3,58E+00|t/año|
|SRC_2|Operación|Tramo 1|Areal|2,41|5|12.050|6,00E-03|1,62E-03|1,62E-04|2,65E-05|7,54E-08|1,24E-06|t/m2-año|
|SRC_3|Operación|Tramo 2|Areal|2,46|5|12.300|6,58E-04|1,26E-04|3,08E-05|2,67E-05|7,60E-08|1,24E-06|t/m2-año|
|SRC_4|Operación|Tramo 3|Areal|38,40|5|192.000|6,58E-04|1,26E-04|3,08E-05|2,67E-05|7,60E-08|1,24E-06|t/m2-año|
|SRC_5|Operación|Tramo 4|Areal|10,20|5|51.000|5,00E-04|9,62E-05|2,34E-05|2,03E-05|5,78E-08|9,44E-07|t/m2-año|
|SRC_6|Operación|Tramo 5|Areal|3,26|5|16.300|4,63E-04|8,90E-05|2,17E-05|1,88E-05|5,35E-08|8,74E-07|t/m2-año|
|SRC_7|Operación|Tramo 6|Areal|364,00|5|1.820.000|1,20E-04|2,31E-05|5,62E-06|4,88E-06|1,39E-08|2,27E-07|t/m2-año|
|SRC_8|Operación|Tramo 8|Areal|0,93|5|4.650|1,67E-03|4,50E-04|4,51E-05|7,14E-06|2,03E-08|3,34E-07|t/m2-año|
|SRC_9|Operación|Tramo 9|Areal|1,16|5|5.800|3,34E-03|9,00E-04|9,01E-05|1,43E-05|4,06E-08|6,67E-07|t/m2-año|
|SRC_10|Operación|Tramo 10|Areal|1,00|5|5.000|5,00E-04|1,35E-04|1,35E-05|2,14E-06|6,09E-09|1,00E-07|t/m2-año|
|SRC_11|Operación|Tramo 11|Areal|1,00|5|5.000|3,34E-03|9,00E-04|9,01E-05|1,43E-05|4,06E-08|6,67E-07|t/m2-año|
|SRC_12|Operación|Tramo 12|Areal|2,24|5|11.200|7,38E-04|1,99E-04|1,99E-05|3,16E-06|8,98E-09|1,48E-07|t/m2-año|
|SRC_13|Operación|Procesos|Areal|--|--|1.748|3,39E-03|2,27E-03|9,63E-04|0,00E+00|0,00E+00|0,00E+00|t/m2-año|
|SRC_14|Operación|Carga de Material|Areal|--|--|199.820|2,22E-05|1,30E-05|6,07E-06|8,16E-05|3,63E-07|5,95E-05|t/m2-año|
|SRC_15|Operación|Descarga de Material|Areal|--|--|72.858|6,08E-05|3,58E-05|1,67E-05|2,24E-04|9,95E-07|1,63E-04|t/m2-año|
|SRC_16|Operación|Grupo electrógeno|Puntual|--|--|--|2,27E-02|2,27E-02|1,90E-02|1,27E+00|6,01E-04|3,37E-01|t/año|
|SRC_17|Operación|Botadero Sales Pobres|Areal|--|--|378.000|6,23E-06|3,12E-06|4,68E-07|0,00E+00|0,00E+00|0,00E+00|t/m2-año|
|SRC_18|Operación|ETSR Evaporación solar|Areal|--|--|71.973|2,08E-05|1,04E-05|1,56E-06|0,00E+00|0,00E+00|0,00E+00|t/m2-año|

Elaboración propia

Actualización Modelación dispersión atmosférica **9**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.5** **Receptores de interés**

Los receptores considerados en la Tabla 7 corresponden las 2 estaciones de monitoreo, además de 29
receptores identificados por el consultor para ser evaluados.

**Tabla 7. Coordenadas de los receptores**

|ID|Nombre|Coordenadas UTM<br>(Huso 19. Datum WGS84)|Col4|
|---|---|---|---|
|**ID**|**Nombre**|**Este (m)**|**Norte (m)**|
|R_1|Estación Pozo Almonte|417.707|7.760.616|
|R_2|Estación Alto Hospicio|385.117|7.755.989|
|R_3|Hospital Regional de Iquique|381.076|7.764.412|
|R_4|AI Campesina Pampa del Tamarugal - Transhumancia|418.775|7.762.574|
|R_5|AI Campesina Pampa del Tamarugal - Río Aroma|419.265|7.762.630|
|R_6|AI Campesina Pampa del Tamarugal - Casa Blanca|423.608|7.764.423|
|R_7|AI Campesina Pampa del Tamarugal - Cerro Sagrado Corazón|418.530|7.756.929|
|R_8|AI Campesina Pampa del Tamarugal - Majada|431.513|7.772.518|
|R_9|AI Campesina Pampa del Tamarugal - Pampa Verde|421.670|7.754.345|
|R_10|AI Campesina Pampa del Tamarugal - Rodal|427.683|7.744.681|
|R_11|AI Campesina Pampa del Tamarugal - Transhumancia|421.915|7.762.474|
|R_12|CI Patrimonial Pampa del Tamarugal - Apacheta|417.786|7.762.400|
|R_13|CI Patrimonial Pampa del Tamarugal - Apacheta|415.079|7.764.234|
|R_14|CI Patrimonial Pampa del Tamarugal - Apacheta|429.542|7.760.068|
|R_15|CI Patrimonial Pampa del Tamarugal - Curuña/Diana|418.585|7.745.639|
|R_16|CI Patrimonial Pampa del Tamarugal - La Huayca|441.613|7.740.671|
|R_17|Familia Choque - Transhumancia|420.654|7.762.188|
|R_18|Familia Choque - Ruta en Vehículo|420.219|7.762.600|
|R_19|Familia Choque - Casa Blanca|425.141|7.763.825|
|R_20|Familia Choque - Santa Emilia|429.773|7.753.580|
|R_21|Familia Choque - Dupliza|429.104|7.772.955|
|R_22|Familia Choque - San Felipe|426.209|7.743.158|
|R_23|GHPPI Sol Naciente - Transhumancia|418.754|7.763.757|
|R_24|GHPPI Sol Naciente - Predio Agrícola|419.604|7.760.585|
|R_25|GHPPI Sol Naciente - Mesa Ceremonial|420.168|7.760.481|
|R_26|GHPPI Sol Naciente - Poblado Andino|418.677|7.760.184|
|R_27|GHPPI Sol Naciente - Quebrada Salar de Pintados|420.436|7.761.737|
|R_28|GHPPI Sol Naciente - Pampa Yura|428.832|7.771.921|
|R_29|GHPPI Sol Naciente - Dupliza|435.558|7.766.532|
|R_30|GHPPI Sol Naciente - Rodales|427.296|7.744.773|
|R_31|GHPPI Sol Naciente - Rodal El Refresco|429.840|7.730.575|

Fuente: Elaboración propia

Actualización Modelación dispersión atmosférica **10**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

Además, para generar los mapas de isoconcentraciones se estableció una grilla de receptores que
abarca un área de 101 x 101 km, equiespaciados cada 1 km en donde se encuentra contenida el área
del Proyecto, el área de influencia directa del mismo y toda la información de interés. La Figura 3
presenta la ubicación de los receptores mencionados.

**Figura 3. Ubicación de Receptores de Interés**

Fuente: Elaboración propia

Actualización Modelación dispersión atmosférica **11**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.6** **Dominio de Modelación**

El escenario meteorológico se construyó a partir de la información meteorológica generada por el
modelo WRF para el año 2020. La Tabla 8 muestra la configuración utilizada por el modelo
meteorológico. El dominio del área corresponde a una grilla de 101 km x 101 km, teniendo origen en
las coordenadas presentadas en dicha tabla.

**Tabla 8 Detalle Archivo WRF**

|Proyección Cartográfica|Cónica conforme de Lambert (LCC)|
|---|---|
|Período|1 Enero al 31 de Diciembre 2020|
|Proyección Cartográfica|LCC-NWS 84|
|Latitud de Origen de la Proyección|20,181 S|
|Longitud de Origen de la Proyección|69,770 W|
|Paralelo Estándar 1|19,871 S|
|Paralelo Estándar 2|20,491 S|
|Resolución de Grilla (1 km)|1 km|
|Área del Dominio (km2)|101 x 101|

Fuente: Elaboración propia

La Figura 4 muestra el dominio de modelación para el año de la fase de operación del Proyecto.

Actualización Modelación dispersión atmosférica **12**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 4. Dominio de Modelación**

Fuente: Elaboración propia

Actualización Modelación dispersión atmosférica **13**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.7** **Topografía**

La topografía de la zona se obtuvo de datos de elevación recopilados por satélite con una resolución
de tres arcos-segundo, lo que significa 1/1.200ava parte de un grado de latitud/longitud o bien 90
metros. A continuación, la Figura 5 presenta gráficamente la topografía del área.

**Figura 5. Topografías de la Zona.**

Fuente: Elaboración propia

Actualización Modelación dispersión atmosférica **14**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.8** **U** **SO DE SUELOS**

La información relacionada con el uso de suelo de la zona se obtiene a través de los archivos Global

Land Cover Characterization (GLCC) publicados por el U.S.Geological Survey (USGS). La Figura 6 muestra
el uso de suelos dentro del dominio de modelación. En ella se puede apreciar que el Proyecto se
encuentra mayoritariamente dentro de los usos de suelo de pastizales y tierra estéril.

**Figura 6. Usos de suelo en el área de modelación**

Land Use Code: 10 = Urbano; 30 = Pastizal; 51= Cuerpo de Agua; 70 = Tierra estéril; 80 = Tundra.

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **15**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.9** **Análisis de Incertidumbre**

La modelación de la dispersión de las emisiones del Proyecto se realizó teniendo como base la
modelación meteorológica WRF en un dominio de modelación alrededor del Proyecto de 101 x 101 km,
para el Año 2020. En relación con la modelación meteorológica, la “Guía Para el Uso de Modelos de
Calidad de Aire en el SEIA” (Febrero 2023), señala que existen limitaciones e incertidumbre inherentes
a cada tipo de modelo, así como también incertidumbre asociada a los datos utilizados como
información de entrada. La guía señala que sólo se pueden estimar los errores entre modelación y
observaciones en el caso de la meteorología de superficie y en altura (ni para las emisiones ni para los
impactos futuros existen observaciones).

En esta sección se consideraron los resultados del análisis de incertidumbre presentados en el capítulo
4.2 del Anexo 2.3 de la de Declaración de Impacto Ambiental de este Proyecto, en el cual se estima un
valor de corrección de aportes de 1,08, tomando un promedio entre las estaciones evaluadas
correspondiente a Alto Hospicio y Pozo Almonte.

**3.10** **Resultados de la Implementación del Modelo**

A continuación, se presentan los resultados de la implementación del modelo WRF-CALPUFF, cuyo
detalle es presentado en los archivos digitales de modelación del Apéndice 1 de este documento.

**3.10.1** **Aportes del proyecto**

Utilizando el modelo de dispersión WRF-CALPUFF, se modelaron las emisiones de MP10, MP2,5, MPS
y los gases SO 2, NO 2 y CO, sobre el dominio de modelación establecido por la extensión en superficie
del archivo WRF. La resolución con tamaño de grilla de los receptores fue de 1.000 x 1.000 metros.

Para la aplicación de este modelo se consideró la meteorología WRF para el período entre el 1 de enero
del 2020 al 31 de diciembre de 2020. Luego, se obtuvieron las concentraciones de los contaminantes
anteriormente mencionados y estimadas para cada una de las horas del periodo.

Finalmente se aplicó el módulo CALPOST para obtener los estadísticos establecidos en las normas de
calidad del aire presentadas en este documento.

A partir de la Tabla 9 hasta la Tabla 14, se presentan los resultados del aporte del Proyecto en material
particulado y gases en los receptores evaluados, para el escenario de modelación representado por el
Año de fase de Operación del Proyecto, los cuales ya se encuentran corregidos según los resultados del

análisis de incertidumbre.

De acuerdo con estos resultados, para el año de fase de operación, los mayores aportes del Proyecto
para material particulado se presentan en el receptor R_12, correspondiente a “CI Patrimonial Pampa
del Tamarugal - Apacheta”, alcanzando el 10% de la norma primaria anual de MP10. Para gases los
aportes más altos se producen en el mismo receptor llegando al 14,7% de la norma primaria horaria de

NO2.

Respecto a las normas secundarias, los resultados de la modelación arrojan que los aportes tanto a las
tasas de depositación de material particulado sedimentable (MPS) como a las concentraciones de SO 2
alcanzan como máximo apenas un 0,1% de la norma anual Suiza de MPS en el receptor R_12
“Apacheta” mencionado anteriormente.

Actualización Modelación dispersión atmosférica **16**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 9. Aporte del Proyecto Material Particulado Respirable MP10 y MP2,5 (μg/m** **[3]** **N) - Año Fase de Operación**

|Receptor|MP10|Col3|Col4|Col5|Col6|Col7|MP2,5|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor**<br>**Norma**<br>**Anual**<br>**D.S. No**<br>**12/2022**|**% de la**<br>**Norma**|**P98 24**<br>**hrs**|**Valor**<br>**Norma**<br>**Diaria**<br>**D.S. No**<br>**12/2022**|**% de la**<br>**Norma**|**Anual**|**Valor**<br>**Anual**<br>**Norma**<br>**D.S. No**<br>**12/2012**|**% de la**<br>**Norma**|**P98 24**<br>**hrs**|**Valor**<br>**Norma**<br>**Diaria**<br>**D.S. No**<br>**12/2012**|**% de la**<br>**Norma**|
|R_1|0,380|50|0,8%|1,093|130|0,8%|0,071|20|0,4%|0,224|50|0,4%|
|R_2|0,923|0,923|1,8%|1,781|1,781|1,4%|0,225|0,225|1,1%|0,435|0,435|0,9%|
|R_3|0,687|0,687|1,4%|1,693|1,693|1,3%|0,168|0,168|0,8%|0,414|0,414|0,8%|
|R_4|1,295|1,295|2,6%|3,270|3,270|2,5%|0,253|0,253|1,3%|0,701|0,701|1,4%|
|R_5|0,954|0,954|1,9%|2,336|2,336|1,8%|0,194|0,194|1,0%|0,475|0,475|1,0%|
|R_6|0,157|0,157|0,3%|0,408|0,408|0,3%|0,035|0,035|0,2%|0,099|0,099|0,2%|
|R_7|0,068|0,068|0,1%|0,181|0,181|0,1%|0,014|0,014|0,1%|0,039|0,039|0,1%|
|R_8|0,018|0,018|0,0%|0,053|0,053|0,0%|0,004|0,004|0,0%|0,012|0,012|0,0%|
|R_9|0,048|0,048|0,1%|0,122|0,122|0,1%|0,011|0,011|0,1%|0,026|0,026|0,1%|
|R_10|0,022|0,022|0,0%|0,046|0,046|0,0%|0,005|0,005|0,0%|0,010|0,010|0,0%|
|R_11|0,343|0,343|0,7%|0,782|0,782|0,6%|0,072|0,072|0,4%|0,175|0,175|0,3%|
|R_12|4,998|4,998|10,0%|9,764|9,764|7,5%|0,719|0,719|3,6%|1,651|1,651|3,3%|
|R_13|3,381|3,381|6,8%|8,176|8,176|6,3%|0,790|0,790|3,9%|1,719|1,719|3,4%|
|R_14|0,059|0,059|0,1%|0,160|0,160|0,1%|0,013|0,013|0,1%|0,035|0,035|0,1%|
|R_15|0,018|0,018|0,0%|0,038|0,038|0,0%|0,004|0,004|0,0%|0,009|0,009|0,0%|
|R_16|0,012|0,012|0,0%|0,030|0,030|0,0%|0,003|0,003|0,0%|0,007|0,007|0,0%|
|R_17|0,480|0,480|1,0%|1,038|1,038|0,8%|0,095|0,095|0,5%|0,219|0,219|0,4%|
|R_18|0,627|0,627|1,3%|1,322|1,322|1,0%|0,129|0,129|0,6%|0,285|0,285|0,6%|
|R_19|0,124|0,124|0,2%|0,304|0,304|0,2%|0,027|0,027|0,1%|0,071|0,071|0,1%|
|R_20|0,040|0,040|0,1%|0,094|0,094|0,1%|0,009|0,009|0,0%|0,020|0,020|0,0%|
|R_21|0,019|0,019|0,0%|0,058|0,058|0,0%|0,004|0,004|0,0%|0,013|0,013|0,0%|
|R_22|0,020|0,020|0,0%|0,040|0,040|0,0%|0,004|0,004|0,0%|0,009|0,009|0,0%|
|R_23|1,666|1,666|3,3%|3,913|3,913|3,0%|0,384|0,384|1,9%|0,961|0,961|1,9%|
|R_24|0,228|0,228|0,5%|0,614|0,614|0,5%|0,047|0,047|0,2%|0,125|0,125|0,3%|
|R_25|0,204|0,204|0,4%|0,499|0,499|0,4%|0,042|0,042|0,2%|0,105|0,105|0,2%|
|R_26|0,214|0,214|0,4%|0,601|0,601|0,5%|0,043|0,043|0,2%|0,120|0,120|0,2%|
|R_27|0,403|0,403|0,8%|0,970|0,970|0,7%|0,079|0,079|0,4%|0,202|0,202|0,4%|

Actualización Modelación dispersión atmosférica **17**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|MP10|Col3|Col4|Col5|Col6|Col7|MP2,5|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor**<br>**Norma**<br>**Anual**<br>**D.S. No**<br>**12/2022**|**% de la**<br>**Norma**|**P98 24**<br>**hrs**|**Valor**<br>**Norma**<br>**Diaria**<br>**D.S. No**<br>**12/2022**|**% de la**<br>**Norma**|**Anual**|**Valor**<br>**Anual**<br>**Norma**<br>**D.S. No**<br>**12/2012**|**% de la**<br>**Norma**|**P98 24**<br>**hrs**|**Valor**<br>**Norma**<br>**Diaria**<br>**D.S. No**<br>**12/2012**|**% de la**<br>**Norma**|
|R_28|0,022||0,0%|0,068||0,1%|0,005||0,0%|0,015||0,0%|
|R_29|0,021|0,021|0,0%|0,063|0,063|0,0%|0,005|0,005|0,0%|0,014|0,014|0,0%|
|R_30|0,022|0,022|0,0%|0,046|0,046|0,0%|0,005|0,005|0,0%|0,010|0,010|0,0%|
|R_31|0,011|0,011|0,0%|0,023|0,023|0,0%|0,002|0,002|0,0%|0,005|0,005|0,0%|

Fuente: Elaboración propia

**Tabla 10. Aporte del Proyecto Material Particulado Sedimentable MPS (mg/m** **[2]** **-día) Norma Secundaria - Año Fase de Operación**

|Receptores|MPS|Col3|Col4|
|---|---|---|---|
|**Receptores**|**Promedio Anual**|**Valor Norma Anual**<br>**Ordenanza Suiza**|**% de la Norma**|
|R_1|0,006|200|0,0%|
|R_2|0,017|0,017|0,0%|
|R_3|0,015|0,015|0,0%|
|R_4|0,030|0,030|0,0%|
|R_5|0,023|0,023|0,0%|
|R_6|0,004|0,004|0,0%|
|R_7|0,002|0,002|0,0%|
|R_8|0,001|0,001|0,0%|
|R_9|0,002|0,002|0,0%|
|R_10|0,001|0,001|0,0%|
|R_11|0,009|0,009|0,0%|
|R_12|0,107|0,107|0,1%|
|R_13|0,052|0,052|0,0%|
|R_14|0,002|0,002|0,0%|
|R_15|0,001|0,001|0,0%|
|R_16|0,002|0,002|0,0%|
|R_17|0,012|0,012|0,0%|
|R_18|0,015|0,015|0,0%|

Actualización Modelación dispersión atmosférica **18**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptores|MPS|Col3|Col4|
|---|---|---|---|
|**Receptores**|**Promedio Anual**|**Valor Norma Anual**<br>**Ordenanza Suiza**|**% de la Norma**|
|R_19|0,004||0,0%|
|R_20|0,002|0,002|0,0%|
|R_21|0,001|0,001|0,0%|
|R_22|0,001|0,001|0,0%|
|R_23|0,030|0,030|0,0%|
|R_24|0,007|0,007|0,0%|
|R_25|0,006|0,006|0,0%|
|R_26|0,005|0,005|0,0%|
|R_27|0,011|0,011|0,0%|
|R_28|0,001|0,001|0,0%|
|R_29|0,002|0,002|0,0%|
|R_30|0,001|0,001|0,0%|
|R_31|0,001|0,001|0,0%|

Fuente: Elaboración propia

**Tabla 11. Aporte del Proyecto Dióxido de Nitrógeno NO** **2** **(μg/m** **[3]** **N) - Año Fase de Operación**

|Receptor|NO<br>2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma**<br>**Anual D.S. No**<br>**114/2002**|**% de la Norma**|**P99 1 hora**|**Valor Norma**<br>**Horaria D.S.**<br>**No 114/2002**|**% de la Norma**|
|R_1|0,219|100|0,2%|7,975|400|2,0%|
|R_2|0,145|0,145|0,1%|1,651|1,651|0,4%|
|R_3|0,103|0,103|0,1%|1,307|1,307|0,3%|
|R_4|0,899|0,899|0,9%|29,389|29,389|7,3%|
|R_5|0,767|0,767|0,8%|16,143|16,143|4,0%|
|R_6|0,156|0,156|0,2%|4,693|4,693|1,2%|
|R_7|0,055|0,055|0,1%|1,963|1,963|0,5%|
|R_8|0,015|0,015|0,0%|0,271|0,271|0,1%|
|R_9|0,044|0,044|0,0%|1,157|1,157|0,3%|
|R_10|0,020|0,020|0,0%|0,273|0,273|0,1%|

Actualización Modelación dispersión atmosférica **19**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|NO<br>2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma**<br>**Anual D.S. No**<br>**114/2002**|**% de la Norma**|**P99 1 hora**|**Valor Norma**<br>**Horaria D.S.**<br>**No 114/2002**|**% de la Norma**|
|R_11|0,329||0,3%|5,599||1,4%|
|R_12|1,608|1,608|1,6%|58,893|58,893|14,7%|
|R_13|2,015|2,015|2,0%|57,373|57,373|14,3%|
|R_14|0,056|0,056|0,1%|1,109|1,109|0,3%|
|R_15|0,013|0,013|0,0%|0,190|0,190|0,0%|
|R_16|0,010|0,010|0,0%|0,106|0,106|0,0%|
|R_17|0,397|0,397|0,4%|7,791|7,791|1,9%|
|R_18|0,558|0,558|0,6%|9,749|9,749|2,4%|
|R_19|0,123|0,123|0,1%|2,883|2,883|0,7%|
|R_20|0,036|0,036|0,0%|0,503|0,503|0,1%|
|R_21|0,016|0,016|0,0%|0,332|0,332|0,1%|
|R_22|0,017|0,017|0,0%|0,217|0,217|0,1%|
|R_23|1,582|1,582|1,6%|31,075|31,075|7,8%|
|R_24|0,181|0,181|0,2%|6,196|6,196|1,5%|
|R_25|0,168|0,168|0,2%|5,226|5,226|1,3%|
|R_26|0,160|0,160|0,2%|6,706|6,706|1,7%|
|R_27|0,316|0,316|0,3%|8,111|8,111|2,0%|
|R_28|0,018|0,018|0,0%|0,439|0,439|0,1%|
|R_29|0,019|0,019|0,0%|0,302|0,302|0,1%|
|R_30|0,020|0,020|0,0%|0,269|0,269|0,1%|
|R_31|0,009|0,009|0,0%|0,091|0,091|0,0%|

Fuente: Elaboración propia

Actualización Modelación dispersión atmosférica **20**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 12. Aporte del Proyecto Monóxido de Carbono CO (μg/m** **[3]** **N) - Año Fase de Operación**

|Receptor|CO|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**P99 1 hora**|**Valor Norma**<br>**1 hr D.S. No**<br>**115/2002**|**% de la Norma**|**P99 8 horas**|**Valor Norma**<br>**8 hrs D.S. No**<br>**115/2002**|**% de la Norma**|
|R_1|5,272|30.000|0,0%|2,127|10.000|0,0%|
|R_2|0,106|0,106|0,0%|0,043|0,043|0,0%|
|R_3|0,087|0,087|0,0%|0,037|0,037|0,0%|
|R_4|30,862|30,862|0,1%|6,993|6,993|0,1%|
|R_5|15,767|15,767|0,1%|4,045|4,045|0,0%|
|R_6|1,834|1,834|0,0%|0,638|0,638|0,0%|
|R_7|0,884|0,884|0,0%|0,251|0,251|0,0%|
|R_8|0,153|0,153|0,0%|0,049|0,049|0,0%|
|R_9|0,645|0,645|0,0%|0,166|0,166|0,0%|
|R_10|0,123|0,123|0,0%|0,047|0,047|0,0%|
|R_11|2,881|2,881|0,0%|1,074|1,074|0,0%|
|R_12|60,439|60,439|0,2%|15,189|15,189|0,2%|
|R_13|59,548|59,548|0,2%|12,857|12,857|0,1%|
|R_14|0,549|0,549|0,0%|0,214|0,214|0,0%|
|R_15|0,100|0,100|0,0%|0,035|0,035|0,0%|
|R_16|0,056|0,056|0,0%|0,026|0,026|0,0%|
|R_17|4,354|4,354|0,0%|1,350|1,350|0,0%|
|R_18|5,984|5,984|0,0%|1,971|1,971|0,0%|
|R_19|1,488|1,488|0,0%|0,447|0,447|0,0%|
|R_20|0,253|0,253|0,0%|0,104|0,104|0,0%|
|R_21|0,190|0,190|0,0%|0,056|0,056|0,0%|
|R_22|0,105|0,105|0,0%|0,040|0,040|0,0%|
|R_23|35,217|35,217|0,1%|9,144|9,144|0,1%|
|R_24|3,209|3,209|0,0%|0,907|0,907|0,0%|
|R_25|2,257|2,257|0,0%|0,670|0,670|0,0%|
|R_26|2,934|2,934|0,0%|0,909|0,909|0,0%|
|R_27|4,341|4,341|0,0%|1,360|1,360|0,0%|
|R_28|0,246|0,246|0,0%|0,068|0,068|0,0%|

Actualización Modelación dispersión atmosférica **21**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|CO|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**P99 1 hora**|**Valor Norma**<br>**1 hr D.S. No**<br>**115/2002**|**% de la Norma**|**P99 8 horas**|**Valor Norma**<br>**8 hrs D.S. No**<br>**115/2002**|**% de la Norma**|
|R_29|0,143||0,0%|0,065||0,0%|
|R_30|0,122|0,122|0,0%|0,047|0,047|0,0%|
|R_31|0,043|0,043|0,0%|0,021|0,021|0,0%|

Fuente: Elaboración propia

**Tabla 13. Aporte del Proyecto Dióxido de Azufre (SO** **2** **) Norma Primaria (μg/m** **[3]** **N) - Año Fase de Operación**

|Receptor|SO - Norma primaria<br>2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma**<br>**D.S. No**<br>**104/2018**|**% de la Norma**|**P99 24 hrs**|**Valor Norma**<br>**D.S. No**<br>**104/2018**|**% de la norma**|**P98,5 1 hr**|**Valor**<br>**Norma D.S.**<br>**No**<br>**104/2018**|**% de la Norma**|
|R_1|0,001|60|0,0%|0,005|150|0,0%|0,014|350|0,0%|
|R_2|0,001|0,001|0,0%|0,001|0,001|0,0%|0,003|0,003|0,0%|
|R_3|3,7E-04|3,7E-04|0,0%|0,001|0,001|0,0%|0,003|0,003|0,0%|
|R_4|0,005|0,005|0,0%|0,017|0,017|0,0%|0,047|0,047|0,0%|
|R_5|0,004|0,004|0,0%|0,012|0,012|0,0%|0,035|0,035|0,0%|
|R_6|0,001|0,001|0,0%|0,003|0,003|0,0%|0,008|0,008|0,0%|
|R_7|2,9E-04|2,9E-04|0,0%|0,001|0,001|0,0%|0,003|0,003|0,0%|
|R_8|7,7E-05|7,7E-05|0,0%|2,9E-04|2,9E-04|0,0%|0,001|0,001|0,0%|
|R_9|2,3E-04|2,3E-04|0,0%|0,001|0,001|0,0%|0,002|0,002|0,0%|
|R_10|1,0E-04|1,0E-04|0,0%|2,5E-04|2,5E-04|0,0%|0,001|0,001|0,0%|
|R_11|0,002|0,002|0,0%|0,005|0,005|0,0%|0,015|0,015|0,0%|
|R_12|0,009|0,009|0,0%|0,031|0,031|0,0%|0,112|0,112|0,0%|
|R_13|0,010|0,010|0,0%|0,031|0,031|0,0%|0,113|0,113|0,0%|
|R_14|3,0E-04|3,0E-04|0,0%|0,001|0,001|0,0%|0,003|0,003|0,0%|
|R_15|6,9E-05|6,9E-05|0,0%|1,8E-04|1,8E-04|0,0%|4,3E-04|4,3E-04|0,0%|
|R_16|5,5E-05|5,5E-05|0,0%|1,5E-04|1,5E-04|0,0%|3,0E-04|3,0E-04|0,0%|
|R_17|0,002|0,002|0,0%|0,006|0,006|0,0%|0,018|0,018|0,0%|

Actualización Modelación dispersión atmosférica **22**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|SO - Norma primaria<br>2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma**<br>**D.S. No**<br>**104/2018**|**% de la Norma**|**P99 24 hrs**|**Valor Norma**<br>**D.S. No**<br>**104/2018**|**% de la norma**|**P98,5 1 hr**|**Valor**<br>**Norma D.S.**<br>**No**<br>**104/2018**|**% de la Norma**|
|R_18|0,003||0,0%|0,008||0,0%|0,023||0,0%|
|R_19|0,001|0,001|0,0%|0,002|0,002|0,0%|0,006|0,006|0,0%|
|R_20|1,9E-04|1,9E-04|0,0%|0,001|0,001|0,0%|0,001|0,001|0,0%|
|R_21|8,4E-05|8,4E-05|0,0%|3,1E-04|3,1E-04|0,0%|0,001|0,001|0,0%|
|R_22|9,1E-05|9,1E-05|0,0%|2,2E-04|2,2E-04|0,0%|0,001|0,001|0,0%|
|R_23|0,009|0,009|0,0%|0,021|0,021|0,0%|0,063|0,063|0,0%|
|R_24|0,001|0,001|0,0%|0,003|0,003|0,0%|0,010|0,010|0,0%|
|R_25|0,001|0,001|0,0%|0,003|0,003|0,0%|0,009|0,009|0,0%|
|R_26|0,001|0,001|0,0%|0,003|0,003|0,0%|0,009|0,009|0,0%|
|R_27|0,002|0,002|0,0%|0,005|0,005|0,0%|0,015|0,015|0,0%|
|R_28|9,5E-05|9,5E-05|0,0%|3,6E-04|3,6E-04|0,0%|0,001|0,001|0,0%|
|R_29|9,8E-05|9,8E-05|0,0%|3,2E-04|3,2E-04|0,0%|0,001|0,001|0,0%|
|R_30|1,0E-04|1,0E-04|0,0%|2,5E-04|2,5E-04|0,0%|0,001|0,001|0,0%|
|R_31|4,5E-05|4,5E-05|0,0%|1,1E-04|1,1E-04|0,0%|2,5E-04|2,5E-04|0,0%|

Fuente: Elaboración propia

**Tabla 14. Aporte del Proyecto Dióxido de Azufre (SO** **2** **) Norma Secundaria (μg/m** **[3]** **N) - Año Fase de Operación**

|Receptor|SO - Norma Secundaria<br>2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma D.S.**<br>**No 22/2010**|**% de la Norma**|**P99,7 24 hrs**|**Valor Norma D.S.**<br>**No 22/2010**|**% de la Norma**|**P99,73 1 hr**|**Valor Norma D.S.**<br>**No 22/2010**|**% de la Norma**|
|R_1|0,001|80|0,0%|0,006|365|0,0%|0,027|1.000|0,0%|
|R_2|0,001|0,001|0,0%|0,001|0,001|0,0%|0,005|0,005|0,0%|
|R_3|3,7E-04|3,7E-04|0,0%|0,001|0,001|0,0%|0,004|0,004|0,0%|
|R_4|0,005|0,005|0,0%|0,021|0,021|0,0%|0,085|0,085|0,0%|
|R_5|0,004|0,004|0,0%|0,015|0,015|0,0%|0,057|0,057|0,0%|
|R_6|0,001|0,001|0,0%|0,003|0,003|0,0%|0,015|0,015|0,0%|

Actualización Modelación dispersión atmosférica **23**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|SO - Norma Secundaria<br>2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma D.S.**<br>**No 22/2010**|**% de la Norma**|**P99,7 24 hrs**|**Valor Norma D.S.**<br>**No 22/2010**|**% de la Norma**|**P99,73 1 hr**|**Valor Norma D.S.**<br>**No 22/2010**|**% de la Norma**|
|R_7|2,9E-04||0,0%|0,001||0,0%|0,006||0,0%|
|R_8|7,7E-05|7,7E-05|0,0%|3,7E-04|3,7E-04|0,0%|0,001|0,001|0,0%|
|R_9|2,3E-04|2,3E-04|0,0%|0,001|0,001|0,0%|0,005|0,005|0,0%|
|R_10|1,0E-04|1,0E-04|0,0%|2,6E-04|2,6E-04|0,0%|0,001|0,001|0,0%|
|R_11|0,002|0,002|0,0%|0,006|0,006|0,0%|0,022|0,022|0,0%|
|R_12|0,009|0,009|0,0%|0,036|0,036|0,0%|0,227|0,227|0,0%|
|R_13|0,010|0,010|0,0%|0,038|0,038|0,0%|0,192|0,192|0,0%|
|R_14|3,0E-04|3,0E-04|0,0%|0,001|0,001|0,0%|0,005|0,005|0,0%|
|R_15|6,9E-05|6,9E-05|0,0%|2,4E-04|2,4E-04|0,0%|0,001|0,001|0,0%|
|R_16|5,5E-05|5,5E-05|0,0%|1,5E-04|1,5E-04|0,0%|4,7E-04|4,7E-04|0,0%|
|R_17|0,002|0,002|0,0%|0,007|0,007|0,0%|0,029|0,029|0,0%|
|R_18|0,003|0,003|0,0%|0,009|0,009|0,0%|0,037|0,037|0,0%|
|R_19|0,001|0,001|0,0%|0,002|0,002|0,0%|0,011|0,011|0,0%|
|R_20|1,9E-04|1,9E-04|0,0%|0,001|0,001|0,0%|0,002|0,002|0,0%|
|R_21|8,4E-05|8,4E-05|0,0%|3,3E-04|3,3E-04|0,0%|0,001|0,001|0,0%|
|R_22|9,1E-05|9,1E-05|0,0%|2,3E-04|2,3E-04|0,0%|0,001|0,001|0,0%|
|R_23|0,009|0,009|0,0%|0,028|0,028|0,0%|0,121|0,121|0,0%|
|R_24|0,001|0,001|0,0%|0,004|0,004|0,0%|0,020|0,020|0,0%|
|R_25|0,001|0,001|0,0%|0,003|0,003|0,0%|0,017|0,017|0,0%|
|R_26|0,001|0,001|0,0%|0,004|0,004|0,0%|0,018|0,018|0,0%|
|R_27|0,002|0,002|0,0%|0,007|0,007|0,0%|0,028|0,028|0,0%|
|R_28|9,5E-05|9,5E-05|0,0%|3,8E-04|3,8E-04|0,0%|0,001|0,001|0,0%|
|R_29|9,8E-05|9,8E-05|0,0%|4,4E-04|4,4E-04|0,0%|0,001|0,001|0,0%|
|R_30|1,0E-04|1,0E-04|0,0%|2,7E-04|2,7E-04|0,0%|0,001|0,001|0,0%|
|R_31|4,5E-05|4,5E-05|0,0%|1,2E-04|1,2E-04|0,0%|3,7E-04|3,7E-04|0,0%|

Actualización Modelación dispersión atmosférica **24**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.10.2** **Puntos de Máximo Impacto**

En la Tabla 15 presenta los máximos aportes del Proyecto en el Año de Fase de Operación dentro del
dominio de modelación, para el material particulado (MP10, MP2,5 y MPS) y gases (NO2, CO y SO2).
Estos aportes se presentan a través del punto de máximo impacto (PMI), el cual viene acompañado de
la coordenada en la que se produce la máxima concentración o depositación, según cada contaminante

o estadístico.

Cabe indicar, que para este caso los puntos de máximo impacto del Proyecto (PMI) se encuentran al
interior del proyecto, alejados de los receptores de interés poblacional o vegetacionales, lo que implica
que en específico no le aplicaría el análisis de cumplimiento normativo, puesto que en esos puntos no
existen objetos de protección, por lo que estos aportes no generan efectos adversos significativos en
la salud de la población ni en la vegetación.

**Tabla 15. Coordenadas del Punto de Máximo Impacto (PMI)**

|Contaminante|Estadígrafo|Coordenadas PMI<br>(UTM WGS84 - H19S)|Col4|Aporte|Unidad|
|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Este**|**Norte**|**Norte**|**Norte**|
|MP10|Media Anual|416.564|7.763.311|56,854|ug/m3|
|MP10|Percentil 98 en 24 horas|416.564|7.763.311|113,760|ug/m3|
|MP2,5|Media Anual|416.564|7.763.311|10,550|ug/m3|
|MP2,5|Percentil 98 en 24 horas|416.564|7.763.311|21,149|ug/m3|
|NO2|Media Anual|416.564|7.763.311|25,300|ug/m3|
|NO2|Percentil 99 en 1 Hora|416.559|7.764.307|417,990|ug/m3|
|CO|Percentil 99 en 1 hora|416.559|7.764.307|409,470|ug/m3|
|CO|Percentil 99 8 Horas|416.559|7.764.307|139,870|ug/m3|
|SO2|Media Anual|416.564|7.763.311|0,137|ug/m3|
|SO2|Percentil 99 en 24 horas|416.564|7.763.311|0,301|ug/m3|
|SO2|Percentil 98,5 en 1 hora|416.559|7.764.307|1.355|ug/m3|
|SO2|Percentil 99,7 en 24 horas|416.564|7.763.311|0,400|ug/m3|
|SO2|Percentil 99,73 en 1 hora|416.559|7.764.307|2,067|ug/m3|
|MPS|Media Anual|416.564|7.763.311|0,709|mg/m2-día|

_Fuente: Elaboración propia._

**3.10.3** **Isolíneas de Concentración y Depositación**

Como producto de la modelación Calpuff se generan isolíneas que pueden dar una idea de la trayectoria
de la pluma contaminante y como se relaciona su dispersión con el entorno, en función de la ubicación
de sus fuentes emisoras (en color rojo). En dichas isolíneas presentadas entre la Figura 7 y Figura
20 **¡Error! No se encuentra el origen de la referencia.** se observa que, en general, los mayores aportes
del Proyecto a las concentraciones y tasas de depositación de los distintos contaminantes se mantienen

fundamentalmente en el entorno inmediato de sus obras.

Actualización Modelación dispersión atmosférica **25**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 7. Isoconcentración Aportes MP10 Promedio Anual - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **26**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 8. Isoconcentración Aportes MP10 Percentil 98 Diario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **27**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 9. Isoconcentración Aportes MP2,5 Promedio Anual - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **28**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 10. Isoconcentración Aportes MP2,5 Percentil 98 Diario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **29**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 11. Isoconcentración Aportes NO** **2** **Promedio Anual - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **30**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 12. Isoconcentración Aportes NO** **2** **Percentil 99 Horario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **31**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 13. Isoconcentración Aportes CO Percentil 99 Horario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **32**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 14. Isoconcentración Aportes CO Percentil 99 8 Horas - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **33**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 15. Isoconcentración Aportes SO** **2** **Promedio Anual - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **34**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 16. Isoconcentración Aportes SO** **2** **Percentil 99 Diario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **35**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 17. Isoconcentración Aportes SO** **2** **Percentil 98,5 Horario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **36**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 18. Isoconcentración Aportes SO** **2** **Percentil 99,7 Diario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **37**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 19. Isoconcentración Aportes SO** **2** **Percentil 99,73 Horario - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **38**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Figura 20. Isodepositación Aportes de MPS Promedio Anual - Fase de Operación**

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **39**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.10.4** **Aporte otros proyectos con RCA aprobada**

A continuación, se analizan las concentraciones y tasas de depositación, estimadas por otros proyectos
con RCA aprobada que no han sido ejecutados, identificados en el entorno próximo del proyecto. Para
asegurar la correspondencia del análisis acumulativo, se tomaron como referencia aquellos aportes
que se evaluaron en alguno de los receptores presentados en la sección 3.5 de este Anexo.

Sin perjuicio de lo anterior, es importante señalar que el proyecto genera aportes no significativos en
los receptores poblacionales y vegetacionales, pero considerando la recomendación metodológica de
la Guía Para el Uso de Modelos de Calidad de Aire en el SEIA (Febrero 2023), se contempló como criterio
conservador, realizar una revisión en el Sistema de Evaluación Ambiental (SEA) de los proyectos
cercanos al proyecto que pueden ser relevantes en términos de aportes a las concentraciones de
contaminantes en los receptores de interés seleccionados para la evaluación del Proyecto.

De acuerdo con esta revisión, según muestra la Tabla 16, se identifican 5 proyectos aprobados sin
ejecutar, todos los cuales incluyeron modelación refinada evaluando sus aportes en los receptores
asimilables a los considerados en el presente proyecto

De esta forma, para los proyectos mencionados en la Tabla 16, existen antecedentes de
concentraciones seleccionables, estimando sus aportes en distintos receptores de interés, entre los
cuales se incluyen al menos una vez alguno de los receptores considerados en este Proyecto. Así, en la
Tabla 17 se resumen los aportes cuantificados en dichas evaluaciones ambientales para los eceptores
según corresponda.

Actualización Modelación dispersión atmosférica **40**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 16. Lista de otros Proyectos con RCA evaluados**

|ID|Nombre Proyecto|Receptor en que estima aportes|
|---|---|---|
|P1|Parque Solar Fotovoltaico Negreiros|Pozo Almonte y Alto Hospicio|
|P2|Parque Fotovoltaico Victor Jara|Pozo Almonte|
|P3|Centro de Distribución CBB Tarapacá|Pozo Almonte|
|P4|Planta Fotovoltaica Jardín Solar|Pozo Almonte|
|P5|Centro de Distribución CDD Pozo Almonte|Pozo Almonte|

_Fuente: Elaboración propia._

Actualización Modelación dispersión atmosférica **41**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 17. Aporte de otros Proyectos con RCA evaluados (ug/m3N)**

|ID Proyecto|Estación|MP10|Col4|MP2,5|Col6|NO2|Col8|CO|Col10|SO2|Col12|Col13|Col14|Col15|MPS (mg/m2-<br>día)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID Proyecto**|**Estación**|**Media**<br>**Anual**|**P98 24 hrs**|**Media**<br>**Anual**|**P98 24**<br>**hrs**|**Media**<br>**Anual**|**P99 1 hora**|**P99 1 hora**|**P99 8**<br>**horas**|**Media**<br>**Anual**|**P99 24**<br>**hrs**|**P98,5 1**<br>**hr**|**P99,7**<br>**24 hrs**|**P99,73 1**<br>**hr**|**Media anual**|
|P1|Pozo Almonte|0,003|0,007|0,001|0,001|--|0,011|0,002|0,005|0,0001|0,0001|0,0003|0,0001|0,0004|0,009|
|P1|Alto Hospicio|0,009|0,024|0,002|0,006|--|0,074|0,001|0,003|0,0001|0,0001|0,0001|0,0001|0,0001|0,012|
|P2|Pozo Almonte|0,085|0,249|0,021|0,050|0,079|1,404|0,154|0,379|0,001|0,003|0,008|0,004|0,015|0,002|
|P2|Alto Hospicio|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|P3|Pozo Almonte|0,220|0,700|0,052|0,170|0,017|1,110|0,510|2,700|0,002|0,027|0,014|0,040|0,180|--|
|P3|Alto Hospicio|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|P4|Pozo Almonte|0,000|0,000|0,000|0,000|0,000|0,200|0,000|0,000|0,000|0,000|0,000|--|--|--|
|P4|Alto Hospicio|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

Actualización Modelación dispersión atmosférica **42**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|ID Proyecto|Estación|MP10|Col4|MP2,5|Col6|NO2|Col8|CO|Col10|SO2|Col12|Col13|Col14|Col15|MPS (mg/m2-<br>día)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID Proyecto**|**Estación**|**Media**<br>**Anual**|**P98 24 hrs**|**Media**<br>**Anual**|**P98 24**<br>**hrs**|**Media**<br>**Anual**|**P99 1 hora**|**P99 1 hora**|**P99 8**<br>**horas**|**Media**<br>**Anual**|**P99 24**<br>**hrs**|**P98,5 1**<br>**hr**|**P99,7**<br>**24 hrs**|**P99,73 1**<br>**hr**|**Media anual**|
|P5|Pozo Almonte|0,040|0,310|0,030|0,190|0,160|5,260|0,720|1,260|0,000|0,040|0,080|--|--|--|
|P5|Alto Hospicio|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|**Aporte Total**<br>**Otros**<br>**Proyectos**|**Pozo Almonte**|**0,349**|**1,266**|**0,103**|**0,412**|**0,256**|**7,985**|**1,386**|**4,343**|**0,003**|**0,070**|**0,103**|**0,044**|**0,196**|**0,011**|
|**Aporte Total**<br>**Otros**<br>**Proyectos**|**Alto Hospicio**|**0,009**|**0,024**|**0,002**|**0,006**|**0,000**|**0,074**|**0,001**|**0,003**|**0,000**|**0,000**|**0,000**|**0,000**|**0,000**|**0,012**|

Fuente: Elaboración propia.

Actualización Modelación dispersión atmosférica **43**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**3.10.5** **Calidad de Aire Proyectada**

De esta forma, desde la Tabla 18 a la Tabla 24 se presentan las concentraciones y depositaciones totales
de los distintos contaminantes durante el Año de fase de operación del proyecto, en virtud de lo
solicitado, la cual resulta de la suma de la línea de base, el aporte corregido del Proyecto y de los otros
proyectos con RCA aprobada sin ejecutar, en cada uno de los receptores de interés evaluados, para
luego ser comparados con la norma de calidad de aire respectiva.

En cuanto, a los receptores que no cuentan con línea de base de MP10, MP2,5 y SO 2, se decidió
asignarles los valores de la estación Pozo Almonte (Receptor R_1), con excepción de la estación Alto
Hospicio (R_2) y Hospital Regional de Iquique (R_3), ya que todos ellos cumplen con características de
representatividad tanto por cercanía como por estar en un entorno similar topográfico y meteorológico
a la estación Pozo Almonte. Para el caso de la estación Alto Hospicio, esta solo mide línea de base de
MP2,5, valor que también le fue asignado al receptor Hospital Regional (R_3), por ser el receptor más
cercano a esta. Cabe indicar que, que a estos 2 receptores no se les asignó la línea de base de MP10 y
SO2 medida en estación Pozo Almonte, dado que, por su lejanía y características meteorológicas y
topográficas, no cumplen con los lineamientos de representatividad de los registros de dicha estación.

Respecto a la línea de base de gases (NO2 y CO) y MPS, no existen registros cercanos para establecer
una línea base representativa de los receptores.

**Tabla 18. Concentraciones Proyectadas de MP10**

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-1|Media Anual|34,1|0,380|0,349|34,829|50|69,7%|
|R-1|P98 24 hrs|65,6|1,093|1,266|67,959|130|52,3%|
|R-2|Media Anual|--|0,923|0,009|0,932|50|1,9%|
|R-2|P98 24 hrs|--|1,781|0,024|1,805|130|1,4%|
|R-3|Media Anual|--|0,687|--|0,687|50|1,4%|
|R-3|P98 24 hrs|--|1,693|--|1,693|130|1,3%|
|R-4|Media Anual|34,1|1,295|--|35,395|50|70,8%|
|R-4|P98 24 hrs|65,6|3,270|--|68,870|130|53,0%|
|R-5|Media Anual|34,1|0,954|--|35,054|50|70,1%|
|R-5|P98 24 hrs|65,6|2,336|--|67,936|130|52,3%|
|R-6|Media Anual|34,1|0,157|--|34,257|50|68,5%|

Actualización Modelación dispersión atmosférica **44**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P98 24 hrs|65,6|0,408|--|66,008|130|50,8%|
|R-7|Media Anual|34,1|0,068|--|34,168|50|68,3%|
|R-7|P98 24 hrs|65,6|0,181|--|65,781|130|50,6%|
|R-8|Media Anual|34,1|0,018|--|34,118|50|68,2%|
|R-8|P98 24 hrs|65,6|0,053|--|65,653|130|50,5%|
|R-9|Media Anual|34,1|0,048|--|34,148|50|68,3%|
|R-9|P98 24 hrs|65,6|0,122|--|65,722|130|50,6%|
|R-10|Media Anual|34,1|0,022|--|34,122|50|68,2%|
|R-10|P98 24 hrs|65,6|0,046|--|65,646|130|50,5%|
|R-11|Media Anual|34,1|0,343|--|34,443|50|68,9%|
|R-11|P98 24 hrs|65,6|0,782|--|66,382|130|51,1%|
|R-12|Media Anual|34,1|4,998|--|39,098|50|78,2%|
|R-12|P98 24 hrs|65,6|9,764|--|75,364|130|58,0%|
|R-13|Media Anual|34,1|3,381|--|37,481|50|75,0%|
|R-13|P98 24 hrs|65,6|8,176|--|73,776|130|56,8%|
|R-14|Media Anual|34,1|0,059|--|34,159|50|68,3%|
|R-14|P98 24 hrs|65,6|0,160|--|65,760|130|50,6%|
|R-15|Media Anual|34,1|0,018|--|34,118|50|68,2%|
|R-15|P98 24 hrs|65,6|0,038|--|65,638|130|50,5%|
|R-16|Media Anual|34,1|0,012|--|34,112|50|68,2%|
|R-16|P98 24 hrs|65,6|0,030|--|65,630|130|50,5%|
|R-17|Media Anual|34,1|0,480|--|34,580|50|69,2%|

Actualización Modelación dispersión atmosférica **45**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P98 24 hrs|65,6|1,038|--|66,638|130|51,3%|
|R-18|Media Anual|34,1|0,627|--|34,727|50|69,5%|
|R-18|P98 24 hrs|65,6|1,322|--|66,922|130|51,5%|
|R-19|Media Anual|34,1|0,124|--|34,224|50|68,4%|
|R-19|P98 24 hrs|65,6|0,304|--|65,904|130|50,7%|
|R-20|Media Anual|34,1|0,040|--|34,140|50|68,3%|
|R-20|P98 24 hrs|65,6|0,094|--|65,694|130|50,5%|
|R-21|Media Anual|34,1|0,019|--|34,119|50|68,2%|
|R-21|P98 24 hrs|65,6|0,058|--|65,658|130|50,5%|
|R-22|Media Anual|34,1|0,020|--|34,120|50|68,2%|
|R-22|P98 24 hrs|65,6|0,040|--|65,640|130|50,5%|
|R-23|Media Anual|34,1|1,666|--|35,766|50|71,5%|
|R-23|P98 24 hrs|65,6|3,913|--|69,513|130|53,5%|
|R-24|Media Anual|34,1|0,228|--|34,328|50|68,7%|
|R-24|P98 24 hrs|65,6|0,614|--|66,214|130|50,9%|
|R-25|Media Anual|34,1|0,204|--|34,304|50|68,6%|
|R-25|P98 24 hrs|65,6|0,499|--|66,099|130|50,8%|
|R-26|Media Anual|34,1|0,214|--|34,314|50|68,6%|
|R-26|P98 24 hrs|65,6|0,601|--|66,201|130|50,9%|
|R-27|Media Anual|34,1|0,403|--|34,503|50|69,0%|
|R-27|P98 24 hrs|65,6|0,970|--|66,570|130|51,2%|
|R-28|Media Anual|34,1|0,022|--|34,122|50|68,2%|

Actualización Modelación dispersión atmosférica **46**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P98 24 hrs|65,6|0,068|--|65,668|130|50,5%|
|R-29|Media Anual|34,1|0,021|--|34,121|50|68,2%|
|R-29|P98 24 hrs|65,6|0,063|--|65,663|130|50,5%|
|R-30|Media Anual|34,1|0,022|--|34,122|50|68,2%|
|R-30|P98 24 hrs|65,6|0,046|--|65,646|130|50,5%|
|R-31|Media Anual|34,1|0,011|--|34,111|50|68,2%|
|R-31|P98 24 hrs|65,6|0,023|--|65,623|130|50,5%|

Fuente: Elaboración propia.

**Tabla 19. Concentraciones Proyectadas de MP2,5**

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-1|Media Anual|9,1|0,071|0,103|9,274|20|46,4%|
|R-1|P98 24 hrs|17,6|0,224|0,412|18,236|50|36,5%|
|R-2|Media Anual|10,9|0,225|0,002|11,127|20|55,6%|
|R-2|P98 24 hrs|19,8|0,435|0,006|20,241|50|40,5%|
|R-3|Media Anual|10,9|0,168|--|11,068|20|55,3%|
|R-3|P98 24 hrs|19,8|0,414|--|20,214|50|40,4%|
|R-4|Media Anual|9,1|0,253|--|9,353|20|46,8%|
|R-4|P98 24 hrs|17,6|0,701|--|18,301|50|36,6%|
|R-5|Media Anual|9,1|0,194|--|9,294|20|46,5%|
|R-5|P98 24 hrs|17,6|0,475|--|18,075|50|36,2%|

Actualización Modelación dispersión atmosférica **47**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-6|Media Anual|9,1|0,035|--|9,135|20|45,7%|
|R-6|P98 24 hrs|17,6|0,099|--|17,699|50|35,4%|
|R-7|Media Anual|9,1|0,014|--|9,114|20|45,6%|
|R-7|P98 24 hrs|17,6|0,039|--|17,639|50|35,3%|
|R-8|Media Anual|9,1|0,004|--|9,104|20|45,5%|
|R-8|P98 24 hrs|17,6|0,012|--|17,612|50|35,2%|
|R-9|Media Anual|9,1|0,011|--|9,111|20|45,6%|
|R-9|P98 24 hrs|17,6|0,026|--|17,626|50|35,3%|
|R-10|Media Anual|9,1|0,005|--|9,105|20|45,5%|
|R-10|P98 24 hrs|17,6|0,010|--|17,610|50|35,2%|
|R-11|Media Anual|9,1|0,072|--|9,172|20|45,9%|
|R-11|P98 24 hrs|17,6|0,175|--|17,775|50|35,5%|
|R-12|Media Anual|9,1|0,719|--|9,819|20|49,1%|
|R-12|P98 24 hrs|17,6|1,651|--|19,251|50|38,5%|
|R-13|Media Anual|9,1|0,790|--|9,890|20|49,4%|
|R-13|P98 24 hrs|17,6|1,719|--|19,319|50|38,6%|
|R-14|Media Anual|9,1|0,013|--|9,113|20|45,6%|
|R-14|P98 24 hrs|17,6|0,035|--|17,635|50|35,3%|
|R-15|Media Anual|9,1|0,004|--|9,104|20|45,5%|
|R-15|P98 24 hrs|17,6|0,009|--|17,609|50|35,2%|
|R-16|Media Anual|9,1|0,003|--|9,103|20|45,5%|
|R-16|P98 24 hrs|17,6|0,007|--|17,607|50|35,2%|

Actualización Modelación dispersión atmosférica **48**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-17|Media Anual|9,1|0,095|--|9,195|20|46,0%|
|R-17|P98 24 hrs|17,6|0,219|--|17,819|50|35,6%|
|R-18|Media Anual|9,1|0,129|--|9,229|20|46,1%|
|R-18|P98 24 hrs|17,6|0,285|--|17,885|50|35,8%|
|R-19|Media Anual|9,1|0,027|--|9,127|20|45,6%|
|R-19|P98 24 hrs|17,6|0,071|--|17,671|50|35,3%|
|R-20|Media Anual|9,1|0,009|--|9,109|20|45,5%|
|R-20|P98 24 hrs|17,6|0,020|--|17,620|50|35,2%|
|R-21|Media Anual|9,1|0,004|--|9,104|20|45,5%|
|R-21|P98 24 hrs|17,6|0,013|--|17,613|50|35,2%|
|R-22|Media Anual|9,1|0,004|--|9,104|20|45,5%|
|R-22|P98 24 hrs|17,6|0,009|--|17,609|50|35,2%|
|R-23|Media Anual|9,1|0,384|--|9,484|20|47,4%|
|R-23|P98 24 hrs|17,6|0,961|--|18,561|50|37,1%|
|R-24|Media Anual|9,1|0,047|--|9,147|20|45,7%|
|R-24|P98 24 hrs|17,6|0,125|--|17,725|50|35,5%|
|R-25|Media Anual|9,1|0,042|--|9,142|20|45,7%|
|R-25|P98 24 hrs|17,6|0,105|--|17,705|50|35,4%|
|R-26|Media Anual|9,1|0,043|--|9,143|20|45,7%|
|R-26|P98 24 hrs|17,6|0,120|--|17,720|50|35,4%|
|R-27|Media Anual|9,1|0,079|--|9,179|20|45,9%|
|R-27|P98 24 hrs|17,6|0,202|--|17,802|50|35,6%|

Actualización Modelación dispersión atmosférica **49**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-28|Media Anual|9,1|0,005|--|9,105|20|45,5%|
|R-28|P98 24 hrs|17,6|0,015|--|17,615|50|35,2%|
|R-29|Media Anual|9,1|0,005|--|9,105|20|45,5%|
|R-29|P98 24 hrs|17,6|0,014|--|17,614|50|35,2%|
|R-30|Media Anual|9,1|0,005|--|9,105|20|45,5%|
|R-30|P98 24 hrs|17,6|0,010|--|17,610|50|35,2%|
|R-31|Media Anual|9,1|0,002|--|9,102|20|45,5%|
|R-31|P98 24 hrs|17,6|0,005|--|17,605|50|35,2%|

Fuente: Elaboración propia.

**Tabla 20. Concentraciones Proyectadas de NO2**

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-1|Media Anual|--|0,219|0,256|0,475|100|0,5%|
|R-1|P99 1 hr|--|7,975|7,985|15,960|400|4,0%|
|R-2|Media Anual|--|0,145|0,000|0,145|100|0,1%|
|R-2|P99 1 hr|--|1,651|0,074|1,725|400|0,4%|
|R-3|Media Anual|--|0,103|--|0,103|100|0,1%|
|R-3|P99 1 hr|--|1,307|--|1,307|400|0,3%|
|R-4|Media Anual|--|0,899|--|0,899|100|0,9%|
|R-4|P99 1 hr|--|29,389|--|29,389|400|7,3%|
|R-5|Media Anual|--|0,767|--|0,767|100|0,8%|

Actualización Modelación dispersión atmosférica **50**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P99 1 hr|--|16,143|--|16,143|400|4,0%|
|R-6|Media Anual|--|0,156|--|0,156|100|0,2%|
|R-6|P99 1 hr|--|4,693|--|4,693|400|1,2%|
|R-7|Media Anual|--|0,055|--|0,055|100|0,1%|
|R-7|P99 1 hr|--|1,963|--|1,963|400|0,5%|
|R-8|Media Anual|--|0,015|--|0,015|100|0,0%|
|R-8|P99 1 hr|--|0,271|--|0,271|400|0,1%|
|R-9|Media Anual|--|0,044|--|0,044|100|0,0%|
|R-9|P99 1 hr|--|1,157|--|1,157|400|0,3%|
|R-10|Media Anual|--|0,020|--|0,020|100|0,0%|
|R-10|P99 1 hr|--|0,273|--|0,273|400|0,1%|
|R-11|Media Anual|--|0,329|--|0,329|100|0,3%|
|R-11|P99 1 hr|--|5,599|--|5,599|400|1,4%|
|R-12|Media Anual|--|1,608|--|1,608|100|1,6%|
|R-12|P99 1 hr|--|58,893|--|58,893|400|14,7%|
|R-13|Media Anual|--|2,015|--|2,015|100|2,0%|
|R-13|P99 1 hr|--|57,373|--|57,373|400|14,3%|
|R-14|Media Anual|--|0,056|--|0,056|100|0,1%|
|R-14|P99 1 hr|--|1,109|--|1,109|400|0,3%|
|R-15|Media Anual|--|0,013|--|0,013|100|0,0%|
|R-15|P99 1 hr|--|0,190|--|0,190|400|0,0%|
|R-16|Media Anual|--|0,010|--|0,010|100|0,0%|

Actualización Modelación dispersión atmosférica **51**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P99 1 hr|--|0,106|--|0,106|400|0,0%|
|R-17|Media Anual|--|0,397|--|0,397|100|0,4%|
|R-17|P99 1 hr|--|7,791|--|7,791|400|1,9%|
|R-18|Media Anual|--|0,558|--|0,558|100|0,6%|
|R-18|P99 1 hr|--|9,749|--|9,749|400|2,4%|
|R-19|Media Anual|--|0,123|--|0,123|100|0,1%|
|R-19|P99 1 hr|--|2,883|--|2,883|400|0,7%|
|R-20|Media Anual|--|0,036|--|0,036|100|0,0%|
|R-20|P99 1 hr|--|0,503|--|0,503|400|0,1%|
|R-21|Media Anual|--|0,016|--|0,016|100|0,0%|
|R-21|P99 1 hr|--|0,332|--|0,332|400|0,1%|
|R-22|Media Anual|--|0,017|--|0,017|100|0,0%|
|R-22|P99 1 hr|--|0,217|--|0,217|400|0,1%|
|R-23|Media Anual|--|1,582|--|1,582|100|1,6%|
|R-23|P99 1 hr|--|31,075|--|31,075|400|7,8%|
|R-24|Media Anual|--|0,181|--|0,181|100|0,2%|
|R-24|P99 1 hr|--|6,196|--|6,196|400|1,5%|
|R-25|Media Anual|--|0,168|--|0,168|100|0,2%|
|R-25|P99 1 hr|--|5,226|--|5,226|400|1,3%|
|R-26|Media Anual|--|0,160|--|0,160|100|0,2%|
|R-26|P99 1 hr|--|6,706|--|6,706|400|1,7%|
|R-27|Media Anual|--|0,316|--|0,316|100|0,3%|

Actualización Modelación dispersión atmosférica **52**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P99 1 hr|--|8,111|--|8,111|400|2,0%|
|R-28|Media Anual|--|0,018|--|0,018|100|0,0%|
|R-28|P99 1 hr|--|0,439|--|0,439|400|0,1%|
|R-29|Media Anual|--|0,019|--|0,019|100|0,0%|
|R-29|P99 1 hr|--|0,302|--|0,302|400|0,1%|
|R-30|Media Anual|--|0,020|--|0,020|100|0,0%|
|R-30|P99 1 hr|--|0,269|--|0,269|400|0,1%|
|R-31|Media Anual|--|0,009|--|0,009|100|0,0%|
|R-31|P99 1 hr|--|0,091|--|0,091|400|0,0%|

Fuente: Elaboración propia.

**Tabla 21. Concentraciones Proyectadas de CO**

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-1|P99 8 hrs|--|2,127|1,386|3,513|10000|0,0%|
|R-1|P99 1 hr|--|5,272|4,343|9,615|30000|0,0%|
|R-2|P99 8 hrs|--|0,043|0,001|0,044|10000|0,0%|
|R-2|P99 1 hr|--|0,106|0,003|0,109|30000|0,0%|
|R-3|P99 8 hrs|--|0,037|--|0,037|10000|0,0%|
|R-3|P99 1 hr|--|0,087|--|0,087|30000|0,0%|
|R-4|P99 8 hrs|--|6,993|--|6,993|10000|0,1%|
|R-4|P99 1 hr|--|30,862|--|30,862|30000|0,1%|

Actualización Modelación dispersión atmosférica **53**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-5|P99 8 hrs|--|4,045|--|4,045|10000|0,0%|
|R-5|P99 1 hr|--|15,767|--|15,767|30000|0,1%|
|R-6|P99 8 hrs|--|0,638|--|0,638|10000|0,0%|
|R-6|P99 1 hr|--|1,834|--|1,834|30000|0,0%|
|R-7|P99 8 hrs|--|0,251|--|0,251|10000|0,0%|
|R-7|P99 1 hr|--|0,884|--|0,884|30000|0,0%|
|R-8|P99 8 hrs|--|0,049|--|0,049|10000|0,0%|
|R-8|P99 1 hr|--|0,153|--|0,153|30000|0,0%|
|R-9|P99 8 hrs|--|0,166|--|0,166|10000|0,0%|
|R-9|P99 1 hr|--|0,645|--|0,645|30000|0,0%|
|R-10|P99 8 hrs|--|0,047|--|0,047|10000|0,0%|
|R-10|P99 1 hr|--|0,123|--|0,123|30000|0,0%|
|R-11|P99 8 hrs|--|1,074|--|1,074|10000|0,0%|
|R-11|P99 1 hr|--|2,881|--|2,881|30000|0,0%|
|R-12|P99 8 hrs|--|15,189|--|15,189|10000|0,2%|
|R-12|P99 1 hr|--|60,439|--|60,439|30000|0,2%|
|R-13|P99 8 hrs|--|12,857|--|12,857|10000|0,1%|
|R-13|P99 1 hr|--|59,548|--|59,548|30000|0,2%|
|R-14|P99 8 hrs|--|0,214|--|0,214|10000|0,0%|
|R-14|P99 1 hr|--|0,549|--|0,549|30000|0,0%|
|R-15|P99 8 hrs|--|0,035|--|0,035|10000|0,0%|
|R-15|P99 1 hr|--|0,100|--|0,100|30000|0,0%|

Actualización Modelación dispersión atmosférica **54**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-16|P99 8 hrs|--|0,026|--|0,026|10000|0,0%|
|R-16|P99 1 hr|--|0,056|--|0,056|30000|0,0%|
|R-17|P99 8 hrs|--|1,350|--|1,350|10000|0,0%|
|R-17|P99 1 hr|--|4,354|--|4,354|30000|0,0%|
|R-18|P99 8 hrs|--|1,971|--|1,971|10000|0,0%|
|R-18|P99 1 hr|--|5,984|--|5,984|30000|0,0%|
|R-19|P99 8 hrs|--|0,447|--|0,447|10000|0,0%|
|R-19|P99 1 hr|--|1,488|--|1,488|30000|0,0%|
|R-20|P99 8 hrs|--|0,104|--|0,104|10000|0,0%|
|R-20|P99 1 hr|--|0,253|--|0,253|30000|0,0%|
|R-21|P99 8 hrs|--|0,056|--|0,056|10000|0,0%|
|R-21|P99 1 hr|--|0,190|--|0,190|30000|0,0%|
|R-22|P99 8 hrs|--|0,040|--|0,040|10000|0,0%|
|R-22|P99 1 hr|--|0,105|--|0,105|30000|0,0%|
|R-23|P99 8 hrs|--|9,144|--|9,144|10000|0,1%|
|R-23|P99 1 hr|--|35,217|--|35,217|30000|0,1%|
|R-24|P99 8 hrs|--|0,907|--|0,907|10000|0,0%|
|R-24|P99 1 hr|--|3,209|--|3,209|30000|0,0%|
|R-25|P99 8 hrs|--|0,670|--|0,670|10000|0,0%|
|R-25|P99 1 hr|--|2,257|--|2,257|30000|0,0%|
|R-26|P99 8 hrs|--|0,909|--|0,909|10000|0,0%|
|R-26|P99 1 hr|--|2,934|--|2,934|30000|0,0%|

Actualización Modelación dispersión atmosférica **55**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R-27|P99 8 hrs|--|1,360|--|1,360|10000|0,0%|
|R-27|P99 1 hr|--|4,341|--|4,341|30000|0,0%|
|R-28|P99 8 hrs|--|0,068|--|0,068|10000|0,0%|
|R-28|P99 1 hr|--|0,246|--|0,246|30000|0,0%|
|R-29|P99 8 hrs|--|0,065|--|0,065|10000|0,0%|
|R-29|P99 1 hr|--|0,143|--|0,143|30000|0,0%|
|R-30|P99 8 hrs|--|0,047|--|0,047|10000|0,0%|
|R-30|P99 1 hr|--|0,122|--|0,122|30000|0,0%|
|R-31|P99 8 hrs|--|0,021|--|0,021|10000|0,0%|
|R-31|P99 1 hr|--|0,043|--|0,043|30000|0,0%|

Fuente: Elaboración propia.

**Tabla 22. Concentraciones Proyectadas de SO2 Norma Primaria**

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R_1|Media Anual|2,6|0,001|0,003|2,604|60|4,3%|
|R_1|P99 24 hrs|5,8|0,005|0,07|5,875|150|3,9%|
|R_1|P98,5 1 hr|8,1|0,014|0,103|8,217|350|2,3%|
|R_2|Media Anual|--|0,001|0,000|0,001|60|0,0%|
|R_2|P99 24 hrs|--|0,001|0,000|0,001|150|0,0%|
|R_2|P98,5 1 hr|--|0,003|0,000|0,003|350|0,0%|
|R_3|Media Anual|--|3,7E-04|--|0,000|60|0,0%|

Actualización Modelación dispersión atmosférica **56**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P99 24 hrs|--|0,001|--|0,001|150|0,0%|
|**Receptor**|P98,5 1 hr|--|0,003|--|0,003|350|0,0%|
|R_4|Media Anual|2,6|0,005|--|2,605|60|4,3%|
|R_4|P99 24 hrs|5,8|0,017|--|5,817|150|3,9%|
|R_4|P98,5 1 hr|8,1|0,047|--|8,147|350|2,3%|
|R_5|Media Anual|2,6|0,004|--|2,604|60|4,3%|
|R_5|P99 24 hrs|5,8|0,012|--|5,812|150|3,9%|
|R_5|P98,5 1 hr|8,1|0,035|--|8,135|350|2,3%|
|R_6|Media Anual|2,6|0,001|--|2,601|60|4,3%|
|R_6|P99 24 hrs|5,8|0,003|--|5,803|150|3,9%|
|R_6|P98,5 1 hr|8,1|0,008|--|8,108|350|2,3%|
|R_7|Media Anual|2,6|2,9E-04|--|2,600|60|4,3%|
|R_7|P99 24 hrs|5,8|0,001|--|5,801|150|3,9%|
|R_7|P98,5 1 hr|8,1|0,003|--|8,103|350|2,3%|
|R_8|Media Anual|2,6|7,7E-05|--|2,600|60|4,3%|
|R_8|P99 24 hrs|5,8|2,9E-04|--|5,800|150|3,9%|
|R_8|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_9|Media Anual|2,6|2,3E-04|--|2,600|60|4,3%|
|R_9|P99 24 hrs|5,8|0,001|--|5,801|150|3,9%|
|R_9|P98,5 1 hr|8,1|0,002|--|8,102|350|2,3%|
|R_10|Media Anual|2,6|1,0E-04|--|2,600|60|4,3%|
|R_10|P99 24 hrs|5,8|2,5E-04|--|5,800|150|3,9%|

Actualización Modelación dispersión atmosférica **57**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_11|Media Anual|2,6|0,002|--|2,602|60|4,3%|
|R_11|P99 24 hrs|5,8|0,005|--|5,805|150|3,9%|
|R_11|P98,5 1 hr|8,1|0,015|--|8,115|350|2,3%|
|R_12|Media Anual|2,6|0,009|--|2,609|60|4,3%|
|R_12|P99 24 hrs|5,8|0,031|--|5,831|150|3,9%|
|R_12|P98,5 1 hr|8,1|0,112|--|8,212|350|2,3%|
|R_13|Media Anual|2,6|0,010|--|2,610|60|4,4%|
|R_13|P99 24 hrs|5,8|0,031|--|5,831|150|3,9%|
|R_13|P98,5 1 hr|8,1|0,113|--|8,213|350|2,3%|
|R_14|Media Anual|2,6|3,0E-04|--|2,600|60|4,3%|
|R_14|P99 24 hrs|5,8|0,001|--|5,801|150|3,9%|
|R_14|P98,5 1 hr|8,1|0,003|--|8,103|350|2,3%|
|R_15|Media Anual|2,6|6,9E-05|--|2,600|60|4,3%|
|R_15|P99 24 hrs|5,8|1,8E-04|--|5,800|150|3,9%|
|R_15|P98,5 1 hr|8,1|4,3E-04|--|8,100|350|2,3%|
|R_16|Media Anual|2,6|5,5E-05|--|2,600|60|4,3%|
|R_16|P99 24 hrs|5,8|1,5E-04|--|5,800|150|3,9%|
|R_16|P98,5 1 hr|8,1|3,0E-04|--|8,100|350|2,3%|
|R_17|Media Anual|2,6|0,002|--|2,602|60|4,3%|
|R_17|P99 24 hrs|5,8|0,006|--|5,806|150|3,9%|
|R_17|P98,5 1 hr|8,1|0,018|--|8,118|350|2,3%|

Actualización Modelación dispersión atmosférica **58**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R_18|Media Anual|2,6|0,003|--|2,603|60|4,3%|
|R_18|P99 24 hrs|5,8|0,008|--|5,808|150|3,9%|
|R_18|P98,5 1 hr|8,1|0,023|--|8,123|350|2,3%|
|R_19|Media Anual|2,6|0,001|--|2,601|60|4,3%|
|R_19|P99 24 hrs|5,8|0,002|--|5,802|150|3,9%|
|R_19|P98,5 1 hr|8,1|0,006|--|8,106|350|2,3%|
|R_20|Media Anual|2,6|1,9E-04|--|2,600|60|4,3%|
|R_20|P99 24 hrs|5,8|0,001|--|5,801|150|3,9%|
|R_20|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_21|Media Anual|2,6|8,4E-05|--|2,600|60|4,3%|
|R_21|P99 24 hrs|5,8|3,1E-04|--|5,800|150|3,9%|
|R_21|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_22|Media Anual|2,6|9,1E-05|--|2,600|60|4,3%|
|R_22|P99 24 hrs|5,8|2,2E-04|--|5,800|150|3,9%|
|R_22|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_23|Media Anual|2,6|0,009|--|2,609|60|4,3%|
|R_23|P99 24 hrs|5,8|0,021|--|5,821|150|3,9%|
|R_23|P98,5 1 hr|8,1|0,063|--|8,163|350|2,3%|
|R_24|Media Anual|2,6|0,001|--|2,601|60|4,3%|
|R_24|P99 24 hrs|5,8|0,003|--|5,803|150|3,9%|
|R_24|P98,5 1 hr|8,1|0,010|--|8,110|350|2,3%|
|R_25|Media Anual|2,6|0,001|--|2,601|60|4,3%|

Actualización Modelación dispersión atmosférica **59**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P99 24 hrs|5,8|0,003|--|5,803|150|3,9%|
|**Receptor**|P98,5 1 hr|8,1|0,009|--|8,109|350|2,3%|
|R_26|Media Anual|2,6|0,001|--|2,601|60|4,3%|
|R_26|P99 24 hrs|5,8|0,003|--|5,803|150|3,9%|
|R_26|P98,5 1 hr|8,1|0,009|--|8,109|350|2,3%|
|R_27|Media Anual|2,6|0,002|--|2,602|60|4,3%|
|R_27|P99 24 hrs|5,8|0,005|--|5,805|150|3,9%|
|R_27|P98,5 1 hr|8,1|0,015|--|8,115|350|2,3%|
|R_28|Media Anual|2,6|9,5E-05|--|2,600|60|4,3%|
|R_28|P99 24 hrs|5,8|3,6E-04|--|5,800|150|3,9%|
|R_28|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_29|Media Anual|2,6|9,8E-05|--|2,600|60|4,3%|
|R_29|P99 24 hrs|5,8|3,2E-04|--|5,800|150|3,9%|
|R_29|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_30|Media Anual|2,6|1,0E-04|--|2,600|60|4,3%|
|R_30|P99 24 hrs|5,8|2,5E-04|--|5,800|150|3,9%|
|R_30|P98,5 1 hr|8,1|0,001|--|8,101|350|2,3%|
|R_31|Media Anual|2,6|4,5E-05|--|2,600|60|4,3%|
|R_31|P99 24 hrs|5,8|1,1E-04|--|5,800|150|3,9%|
|R_31|P98,5 1 hr|8,1|2,5E-04|--|8,100|350|2,3%|

Fuente: Elaboración propia.

Actualización Modelación dispersión atmosférica **60**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**Tabla 23. Concentraciones Proyectadas de SO2 Norma Secundaria**

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R_1|Media Anual|2,6|0,001|0,003|2,604|80|3,3%|
|R_1|P99,7 24 hrs|7,4|0,006|0,044|7,450|365|2,0%|
|R_1|P99,73 1 hr|15,6|0,027|0,196|15,823|1.000|1,6%|
|R_2|Media Anual|--|0,001|0,000|0,001|80|0,0%|
|R_2|P99,7 24 hrs|--|0,001|0,000|0,001|365|0,0%|
|R_2|P99,73 1 hr|--|0,005|0,000|0,005|1.000|0,0%|
|R_3|Media Anual|--|3,7E-04|--|0,000|80|0,0%|
|R_3|P99,7 24 hrs|--|0,001|--|0,001|365|0,0%|
|R_3|P99,73 1 hr|--|0,004|--|0,004|1.000|0,0%|
|R_4|Media Anual|2,6|0,005|--|2,605|80|3,3%|
|R_4|P99,7 24 hrs|7,4|0,021|--|7,421|365|2,0%|
|R_4|P99,73 1 hr|15,6|0,085|--|15,685|1.000|1,6%|
|R_5|Media Anual|2,6|0,004|--|2,604|80|3,3%|
|R_5|P99,7 24 hrs|7,4|0,015|--|7,415|365|2,0%|
|R_5|P99,73 1 hr|15,6|0,057|--|15,657|1.000|1,6%|
|R_6|Media Anual|2,6|0,001|--|2,601|80|3,3%|
|R_6|P99,7 24 hrs|7,4|0,003|--|7,403|365|2,0%|
|R_6|P99,73 1 hr|15,6|0,015|--|15,615|1.000|1,6%|
|R_7|Media Anual|2,6|2,9E-04|--|2,600|80|3,3%|
|R_7|P99,7 24 hrs|7,4|0,001|--|7,401|365|2,0%|
|R_7|P99,73 1 hr|15,6|0,006|--|15,606|1.000|1,6%|

Actualización Modelación dispersión atmosférica **61**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R_8|Media Anual|2,6|7,7E-05|--|2,600|80|3,3%|
|R_8|P99,7 24 hrs|7,4|3,7E-04|--|7,400|365|2,0%|
|R_8|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|
|R_9|Media Anual|2,6|2,3E-04|--|2,600|80|3,3%|
|R_9|P99,7 24 hrs|7,4|0,001|--|7,401|365|2,0%|
|R_9|P99,73 1 hr|15,6|0,005|--|15,605|1.000|1,6%|
|R_10|Media Anual|2,6|1,0E-04|--|2,600|80|3,3%|
|R_10|P99,7 24 hrs|7,4|2,6E-04|--|7,400|365|2,0%|
|R_10|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|
|R_11|Media Anual|2,6|0,002|--|2,602|80|3,3%|
|R_11|P99,7 24 hrs|7,4|0,006|--|7,406|365|2,0%|
|R_11|P99,73 1 hr|15,6|0,022|--|15,622|1.000|1,6%|
|R_12|Media Anual|2,6|0,009|--|2,609|80|3,3%|
|R_12|P99,7 24 hrs|7,4|0,036|--|7,436|365|2,0%|
|R_12|P99,73 1 hr|15,6|0,227|--|15,827|1.000|1,6%|
|R_13|Media Anual|2,6|0,010|--|2,610|80|3,3%|
|R_13|P99,7 24 hrs|7,4|0,038|--|7,438|365|2,0%|
|R_13|P99,73 1 hr|15,6|0,192|--|15,792|1.000|1,6%|
|R_14|Media Anual|2,6|3,0E-04|--|2,600|80|3,3%|
|R_14|P99,7 24 hrs|7,4|0,001|--|7,401|365|2,0%|
|R_14|P99,73 1 hr|15,6|0,005|--|15,605|1.000|1,6%|
|R_15|Media Anual|2,6|6,9E-05|--|2,600|80|3,3%|

Actualización Modelación dispersión atmosférica **62**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P99,7 24 hrs|7,4|2,4E-04|--|7,400|365|2,0%|
|**Receptor**|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|
|R_16|Media Anual|2,6|5,5E-05|--|2,600|80|3,3%|
|R_16|P99,7 24 hrs|7,4|1,5E-04|--|7,400|365|2,0%|
|R_16|P99,73 1 hr|15,6|4,7E-04|--|15,600|1.000|1,6%|
|R_17|Media Anual|2,6|0,002|--|2,602|80|3,3%|
|R_17|P99,7 24 hrs|7,4|0,007|--|7,407|365|2,0%|
|R_17|P99,73 1 hr|15,6|0,029|--|15,629|1.000|1,6%|
|R_18|Media Anual|2,6|0,003|--|2,603|80|3,3%|
|R_18|P99,7 24 hrs|7,4|0,009|--|7,409|365|2,0%|
|R_18|P99,73 1 hr|15,6|0,037|--|15,637|1.000|1,6%|
|R_19|Media Anual|2,6|0,001|--|2,601|80|3,3%|
|R_19|P99,7 24 hrs|7,4|0,002|--|7,402|365|2,0%|
|R_19|P99,73 1 hr|15,6|0,011|--|15,611|1.000|1,6%|
|R_20|Media Anual|2,6|1,9E-04|--|2,600|80|3,3%|
|R_20|P99,7 24 hrs|7,4|0,001|--|7,401|365|2,0%|
|R_20|P99,73 1 hr|15,6|0,002|--|15,602|1.000|1,6%|
|R_21|Media Anual|2,6|8,4E-05|--|2,600|80|3,3%|
|R_21|P99,7 24 hrs|7,4|3,3E-04|--|7,400|365|2,0%|
|R_21|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|
|R_22|Media Anual|2,6|9,1E-05|--|2,600|80|3,3%|
|R_22|P99,7 24 hrs|7,4|2,3E-04|--|7,400|365|2,0%|

Actualización Modelación dispersión atmosférica **63**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|**Receptor**|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|
|R_23|Media Anual|2,6|0,009|--|2,609|80|3,3%|
|R_23|P99,7 24 hrs|7,4|0,028|--|7,428|365|2,0%|
|R_23|P99,73 1 hr|15,6|0,121|--|15,721|1.000|1,6%|
|R_24|Media Anual|2,6|0,001|--|2,601|80|3,3%|
|R_24|P99,7 24 hrs|7,4|0,004|--|7,404|365|2,0%|
|R_24|P99,73 1 hr|15,6|0,020|--|15,620|1.000|1,6%|
|R_25|Media Anual|2,6|0,001|--|2,601|80|3,3%|
|R_25|P99,7 24 hrs|7,4|0,003|--|7,403|365|2,0%|
|R_25|P99,73 1 hr|15,6|0,017|--|15,617|1.000|1,6%|
|R_26|Media Anual|2,6|0,001|--|2,601|80|3,3%|
|R_26|P99,7 24 hrs|7,4|0,004|--|7,404|365|2,0%|
|R_26|P99,73 1 hr|15,6|0,018|--|15,618|1.000|1,6%|
|R_27|Media Anual|2,6|0,002|--|2,602|80|3,3%|
|R_27|P99,7 24 hrs|7,4|0,007|--|7,407|365|2,0%|
|R_27|P99,73 1 hr|15,6|0,028|--|15,628|1.000|1,6%|
|R_28|Media Anual|2,6|9,5E-05|--|2,600|80|3,3%|
|R_28|P99,7 24 hrs|7,4|3,8E-04|--|7,400|365|2,0%|
|R_28|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|
|R_29|Media Anual|2,6|9,8E-05|--|2,600|80|3,3%|
|R_29|P99,7 24 hrs|7,4|4,4E-04|--|7,400|365|2,0%|
|R_29|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|

Actualización Modelación dispersión atmosférica **64**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Concentraciones (μg/m3N)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Concentración**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R_30|Media Anual|2,6|1,0E-04|--|2,600|80|3,3%|
|R_30|P99,7 24 hrs|7,4|2,7E-04|--|7,400|365|2,0%|
|R_30|P99,73 1 hr|15,6|0,001|--|15,601|1.000|1,6%|
|R_31|Media Anual|2,6|4,5E-05|--|2,600|80|3,3%|
|R_31|P99,7 24 hrs|7,4|1,2E-04|--|7,400|365|2,0%|
|R_31|P99,73 1 hr|15,6|3,7E-04|--|15,600|1.000|1,6%|

Fuente: Elaboración propia.

**Tabla 24. Tasas de Depositación Proyectadas de MPS**

|Receptor|Estadístico|Tasa de Depositación (mg/m2-día)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Depositación**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R_1|Media Anual|--|0,006|0,011|0,017|200|0,0%|
|R_2|Media Anual|--|0,017|0,012|0,029|200|0,0%|
|R_3|Media Anual|--|0,015|--|0,015|200|0,0%|
|R_4|Media Anual|--|0,030|--|0,030|200|0,0%|
|R_5|Media Anual|--|0,023|--|0,023|200|0,0%|
|R_6|Media Anual|--|0,004|--|0,004|200|0,0%|
|R_7|Media Anual|--|0,002|--|0,002|200|0,0%|
|R_8|Media Anual|--|0,001|--|0,001|200|0,0%|
|R_9|Media Anual|--|0,002|--|0,002|200|0,0%|
|R_10|Media Anual|--|0,001|--|0,001|200|0,0%|
|R_11|Media Anual|--|0,009|--|0,009|200|0,0%|
|R_12|Media Anual|--|0,107|--|0,107|200|0,1%|
|R_13|Media Anual|--|0,052|--|0,052|200|0,0%|
|R_14|Media Anual|--|0,002|--|0,002|200|0,0%|
|R_15|Media Anual|--|0,001|--|0,001|200|0,0%|
|R_16|Media Anual|--|0,002|--|0,002|200|0,0%|
|R_17|Media Anual|--|0,012|--|0,012|200|0,0%|

Actualización Modelación dispersión atmosférica **65**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

|Receptor|Estadístico|Tasa de Depositación (mg/m2-día)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadístico**|**Línea de**<br>**Base**|**Aporte**<br>**del**<br>**Proyecto**|**Aporte**<br>**Otros**<br>**Proyectos**|**Depositación**<br>**Final**|**Norma**|**% de la**<br>**Norma**|
|R_18|Media Anual|--|0,015|--|0,015|200|0,0%|
|R_19|Media Anual|--|0,004|--|0,004|200|0,0%|
|R_20|Media Anual|--|0,002|--|0,002|200|0,0%|
|R_21|Media Anual|--|0,001|--|0,001|200|0,0%|
|R_22|Media Anual|--|0,001|--|0,001|200|0,0%|
|R_23|Media Anual|--|0,030|--|0,030|200|0,0%|
|R_24|Media Anual|--|0,007|--|0,007|200|0,0%|
|R_25|Media Anual|--|0,006|--|0,006|200|0,0%|
|R_26|Media Anual|--|0,005|--|0,005|200|0,0%|
|R_27|Media Anual|--|0,011|--|0,011|200|0,0%|
|R_28|Media Anual|--|0,001|--|0,001|200|0,0%|
|R_29|Media Anual|--|0,002|--|0,002|200|0,0%|
|R_30|Media Anual|--|0,001|--|0,001|200|0,0%|
|R_31|Media Anual|--|0,001|--|0,001|200|0,0%|

Fuente: Elaboración propia.

Considerando que el emplazamiento y los receptores del proyecto no se encuentran dentro de una
zona de riesgo preexistente y en función de los resultados expuestos, se puede apreciar que todas las
concentraciones y tasas de depositación proyectadas en los receptores de interés más cercanos al
mismo, están en situación de cumplimiento normativo, siendo no significativos, ya que se encuentran
bajo la norma y rangos de latencia en todos sus contaminantes y estadísticos, llegando a lo sumo a los
78,2% de la concentración proyectada para la media anual de MP10 en norma primaria en el receptor
R_12 (CI Patrimonial Pampa de Tamarugal -Apacheta).

Respecto a los receptores de norma secundaria de SO2, los aportes del proyecto no son significativos,
ya que la situación de calidad de aire con proyecto llega apenas a los 3,3% de la norma anual. Por otra
parte, si bien no hay mediciones basales de MPS, los aportes del proyecto llegan como máximo al 0,1%
de la norma anual en el receptor R_12, por lo que se puede descartar cualquier efecto en el entorno.

Actualización Modelación dispersión atmosférica **66**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATOS|PLANTA DE BENEFICIO DE SALES DE NITRATOS|

**4** **CONCLUSIONES**

Respecto a los resultados obtenidos de la modelación, se puede concluir que el Proyecto no genera
aportes significativos y no provoca efectos adversos significativos en los receptores analizados toda vez

que:

 - Las emisiones atmosféricas de un año de operación normal de la fase de operación del Proyecto

corresponden al escenario más adverso, durante los cuales se presentan las mayores emisiones.

 - Dado que el proyecto y sus receptores no se enmarcan dentro de una zona declarada legalmente

como saturada y según los resultados expuestos de línea de base de calidad de aire, se puede
descartar la condición de riesgo preexistente para la evaluación de cumplimiento, dado que
todos los registros estadísticos informados están bajo los límites normativos, llegando como

máximo a un 68% de la norma anual de MP10 en la estación Pozo Almonte.

 - Considerando que el emplazamiento y los receptores del proyecto no se encuentran dentro de

una zona de riesgo preexistente y en función de los resultados expuestos, se puede apreciar que
todas las concentraciones y tasas de depositación proyectadas en los receptores de interés más
cercanos al mismo, derivadas de la suma entre la línea de base, aportes corregidos del proyecto
y de otros proyectos aprobados sin ejecutar, están en situación de cumplimiento normativo,
siendo no significativos, ya que se encuentran bajo la norma y rangos de latencia en todos sus
contaminantes y estadísticos, llegando a lo sumo a los 78,2% de la concentración proyectada
para la media anual de MP10 en norma primaria en el receptor R_12 (CI Patrimonial Pampa de
Tamarugal -Apacheta).

 - Respecto a los receptores de norma secundaria de SO2, los aportes del proyecto no son

significativos, ya que la situación de calidad de aire con proyecto llega apenas a los 3,3% de la
norma anual. Por otra parte, si bien no hay mediciones basales de MPS, los aportes del proyecto
llegan como máximo al 0,1% de la norma anual en el receptor R_12, por lo que se puede
descartar cualquier efecto en el entorno.

 - Por último, resulta importante mencionar que, al ser las emisiones de la operación actual, previo

al ingreso al SEIA, similares en magnitud a las de Operación Futura presentadas para este
proyecto, lo evaluado en este documento se encuentra dentro de la condición basal medida en
las estaciones de monitoreo de calidad de aire, lo que da cuenta que la evaluación de
cumplimiento normativo para esta componente se realiza bajo un escenario conservador,
tomando en cuenta que en el análisis de concentraciones proyectadas de la sección 3.10.5 se le
sumó la línea de base completa a los aportes.

Actualización Modelación dispersión atmosférica **67**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATO|PLANTA DE BENEFICIO DE SALES DE NITRATO|

## APÉNDICE 1 ACTUALIZACIÓN ARCHIVOS DIGITALES DE MODELACIÓN

Actualización Modelación dispersión atmosférica **68**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PLANTA DE BENEFICIO DE SALES DE NITRATO|PLANTA DE BENEFICIO DE SALES DE NITRATO|

## APÉNDICE 2 ARCHIVOS KMZ ISOLÍNEAS, RECEPTORES Y OBRAS DEL PROYECTO

Actualización Modelación dispersión atmosférica **69**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 14.: Aporte del Proyecto Dióxido de Azufre (SO** **2** **) Norma Secundaria (μg/m** **[3]** **N) - Año Fase de Operación****

| Receptor | SO - Norma Secundaria<br>2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor Norma D.S.**<br>**No 22/2010** | **% de la Norma** | **P99,7 24 hrs** | **Valor Norma D.S.**<br>**No 22/2010** | **% de la Norma** | **P99,73 1 hr** | **Valor Norma D.S.**<br>**No 22/2010** | **% de la Norma** |
| R_1 | 0,001 | 80 | 0,0% | 0,006 | 365 | 0,0% | 0,027 | 1.000 | 0,0% |
| R_2 | 0,001 | 0,001 | 0,0% | 0,001 | 0,001 | 0,0% | 0,005 | 0,005 | 0,0% |
| R_3 | 3,7E-04 | 3,7E-04 | 0,0% | 0,001 | 0,001 | 0,0% | 0,004 | 0,004 | 0,0% |
| R_4 | 0,005 | 0,005 | 0,0% | 0,021 | 0,021 | 0,0% | 0,085 | 0,085 | 0,0% |
| R_5 | 0,004 | 0,004 | 0,0% | 0,015 | 0,015 | 0,0% | 0,057 | 0,057 | 0,0% |
| R_6 | 0,001 | 0,001 | 0,0% | 0,003 | 0,003 | 0,0% | 0,015 | 0,015 | 0,0% |

**Tabla 1.: Resumen Estimación de Emisiones****

| Fase | Emisiones (t/año) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **MP10** | **MP2,5** | **MPS** | **NOx** | **CO** | **SO2 ** |
| Construcción | 18,5426 | 2,9018 | 67,6981 | 4,6763 | 2,3694 | 0,0102 |
| Operación | 122,1264 | 28,3002 | 535,0672 | 89,5855 | 28,4720 | 0,3615 |
| Cierre | 18,5426 | 2,9018 | 67,6981 | 4,6763 | 2,3694 | 0,0102 |

**Tabla 2.: Normas de Calidad del Aire Consideradas en el Estudio.****

| Parámetro | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio Anual1 | 50g/m3N | D.S. N° 12/2022 del MMA |
| MP10 | Primaria | Percentil 98 promedio diario | 130g/m3N | 130g/m3N |
| MP2,5 | Primaria | Promedio Anual1 | 20g/m3N | D.S. N° 12/2011 del MMA |
| MP2,5 | Primaria | Percentil 98 promedio diario | 50g/m3N | 50g/m3N |
| NO2 | Primaria | Promedio Anual1 | 100g/m3N | D.S. N° 114/2002 del<br>MINSEGPRES |
| NO2 | Primaria | Percentil 99 máx. 1 hora1 | 400g/m3N | 400g/m3N |
| CO | Primaria | Percentil 99 1 hora1 | 30 mg/m3N | D.S. N° 115/2002 del<br>MINSEGPRES |
| CO | Primaria | Percentil 99 8 hora1 | 10 mg/m3N | 10 mg/m3N |
| SO2 | Primaria | Promedio Anual1 | 60 μg/m3N | D.S. N° 104/2018 del MMA |
| SO2 | Primaria | Percentil 99 24 horas1 | 150 μg/m3N | 150 μg/m3N |
| SO2 | Primaria | Percentil 98,5 1 hora1 | 350 μg/m3N | 350 μg/m3N |
| SO2 | Secundaria | Promedio Anual1 | 80 μg/m3N | D.S. N° 22/2010 del<br>MINSEGPRES |
| SO2 | Secundaria | Percentil 99,7 24 horas1 | 365 μg/m3N | 365 μg/m3N |
| SO2 | Secundaria | Percentil 99,73 1 hora1 | 1000 μg/m3N | 1000 μg/m3N |
| MPS | Secundaria | Promedio Anual | 200 mg/m2-día | Ordenanza Suiza |

**Tabla 3.: Línea de Base de Calidad del Aire y ubicación de Estaciones de monitoreo dentro del****

| Estación | Coordenada UTM WGS84 (Huso 19) | Col3 | Parámetros<br>calidad del aire | Periodo | Administrada por |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Pozo Almonte | 417.709 | 7.760.617 | MP10, MP2,5, SO2 | 2018 - 2020 | COSAYACH |
| Alto Hospicio | 385.118 | 7.755.989 | MP2,5 | 2018 - 2020 | MMA |

**Tabla 4.: Línea de Base Estación Pozo Almonte (**  **g/m** **[3]** **N).****

| Contaminante | Estadístico | Año | Col4 | Col5 | Valor | Valor Norma | % de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadístico** | **2018** | **2019** | **2020** | **2020** | **2020** | **2020** |
| MP10 | Promedio Anual | 34,5 | 36,4 | 31,3 | 34,1 | 50 | 68% |
| MP10 | Percentil 98 24 horas | 66,0 | 68,0 | 62,9 | 65,6 | 130 | 50% |
| MP2,5 | Promedio Anual | 8,7 | 8,0 | 10,7 | 9,1 | 20 | 46% |
| MP2,5 | Percentil 98 24 horas | 7,0 | 17,0 | 28,8 | 17,6 | 50 | 35% |
| SO2 (Primaria) | Promedio Anual | 1,6 | 1,7 | 4,6 | 2,6 | 60 | 4% |
| SO2 (Primaria) | Percentil 99 24 horas | 3,8 | 4,3 | 9,3 | 5,8 | 150 | 4% |
| SO2 (Primaria) | Percentil 98,5 1 hora | 5,3 | 6,2 | 12,8 | 8,1 | 350 | 2% |
| SO2 <br>(Secundaria) | Promedio Anual | 1,6 | 1,7 | 4,6 | 2,6 | 80 | 3% |
| SO2 <br>(Secundaria) | Percentil 99,7 24 horas | 4,0 | 4,6 | 13,7 | 7,4 | 365 | 2% |
| SO2 <br>(Secundaria) | Percentil 99,73 1 hora | 7,9 | 11,5 | 27,5 | 15,6 | 1000 | 2% |

**Tabla 5.: Línea de Base Estación Alto Hospicio (**  **g/m** **[3]** **N).****

| Contaminante | Estadístico | Año | Col4 | Col5 | Valor | Valor Norma | % de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadístico** | **2018** | **2019** | **2020** | **2020** | **2020** | **2020** |
| MP2,5 | Promedio Anual | 11,2 | 11,1 | 10,3 | 10,9 | 20 | 54% |
| MP2,5 | Percentil 98 24 horas | 21,6 | 19,0 | 18,7 | 19,8 | 50 | 40% |

**Tabla 6.: Tasa de Emisión Consideradas Año Fase de Operación.****

| ID<br>Fuente | Fase Emisión | Fuente | Tipo | Largo | Ancho | Área (m2) | Tasas de emisión | Col9 | Col10 | Col11 | Col12 | Col13 | Unidad<br>Tasas de<br>Emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Fuente** | **Fase Emisión** | **Fuente** | **Tipo** | **Largo** | **Ancho** | **Área (m2)** | **MPS** | **MP10** | **MP2,5** | **NOx** | **SO2** | **CO** | **CO** |
| SRC_1 | Operación | Caldera | Puntual | -- | -- | -- | 2,32E+00 | 2,32E+00 | 2,32E+00 | 3,94E+01 | 1,70E-01 | 3,58E+00 | t/año |
| SRC_2 | Operación | Tramo 1 | Areal | 2,41 | 5 | 12.050 | 6,00E-03 | 1,62E-03 | 1,62E-04 | 2,65E-05 | 7,54E-08 | 1,24E-06 | t/m2-año |
| SRC_3 | Operación | Tramo 2 | Areal | 2,46 | 5 | 12.300 | 6,58E-04 | 1,26E-04 | 3,08E-05 | 2,67E-05 | 7,60E-08 | 1,24E-06 | t/m2-año |
| SRC_4 | Operación | Tramo 3 | Areal | 38,40 | 5 | 192.000 | 6,58E-04 | 1,26E-04 | 3,08E-05 | 2,67E-05 | 7,60E-08 | 1,24E-06 | t/m2-año |
| SRC_5 | Operación | Tramo 4 | Areal | 10,20 | 5 | 51.000 | 5,00E-04 | 9,62E-05 | 2,34E-05 | 2,03E-05 | 5,78E-08 | 9,44E-07 | t/m2-año |
| SRC_6 | Operación | Tramo 5 | Areal | 3,26 | 5 | 16.300 | 4,63E-04 | 8,90E-05 | 2,17E-05 | 1,88E-05 | 5,35E-08 | 8,74E-07 | t/m2-año |
| SRC_7 | Operación | Tramo 6 | Areal | 364,00 | 5 | 1.820.000 | 1,20E-04 | 2,31E-05 | 5,62E-06 | 4,88E-06 | 1,39E-08 | 2,27E-07 | t/m2-año |
| SRC_8 | Operación | Tramo 8 | Areal | 0,93 | 5 | 4.650 | 1,67E-03 | 4,50E-04 | 4,51E-05 | 7,14E-06 | 2,03E-08 | 3,34E-07 | t/m2-año |
| SRC_9 | Operación | Tramo 9 | Areal | 1,16 | 5 | 5.800 | 3,34E-03 | 9,00E-04 | 9,01E-05 | 1,43E-05 | 4,06E-08 | 6,67E-07 | t/m2-año |
| SRC_10 | Operación | Tramo 10 | Areal | 1,00 | 5 | 5.000 | 5,00E-04 | 1,35E-04 | 1,35E-05 | 2,14E-06 | 6,09E-09 | 1,00E-07 | t/m2-año |
| SRC_11 | Operación | Tramo 11 | Areal | 1,00 | 5 | 5.000 | 3,34E-03 | 9,00E-04 | 9,01E-05 | 1,43E-05 | 4,06E-08 | 6,67E-07 | t/m2-año |
| SRC_12 | Operación | Tramo 12 | Areal | 2,24 | 5 | 11.200 | 7,38E-04 | 1,99E-04 | 1,99E-05 | 3,16E-06 | 8,98E-09 | 1,48E-07 | t/m2-año |
| SRC_13 | Operación | Procesos | Areal | -- | -- | 1.748 | 3,39E-03 | 2,27E-03 | 9,63E-04 | 0,00E+00 | 0,00E+00 | 0,00E+00 | t/m2-año |
| SRC_14 | Operación | Carga de Material | Areal | -- | -- | 199.820 | 2,22E-05 | 1,30E-05 | 6,07E-06 | 8,16E-05 | 3,63E-07 | 5,95E-05 | t/m2-año |
| SRC_15 | Operación | Descarga de Material | Areal | -- | -- | 72.858 | 6,08E-05 | 3,58E-05 | 1,67E-05 | 2,24E-04 | 9,95E-07 | 1,63E-04 | t/m2-año |
| SRC_16 | Operación | Grupo electrógeno | Puntual | -- | -- | -- | 2,27E-02 | 2,27E-02 | 1,90E-02 | 1,27E+00 | 6,01E-04 | 3,37E-01 | t/año |
| SRC_17 | Operación | Botadero Sales Pobres | Areal | -- | -- | 378.000 | 6,23E-06 | 3,12E-06 | 4,68E-07 | 0,00E+00 | 0,00E+00 | 0,00E+00 | t/m2-año |
| SRC_18 | Operación | ETSR Evaporación solar | Areal | -- | -- | 71.973 | 2,08E-05 | 1,04E-05 | 1,56E-06 | 0,00E+00 | 0,00E+00 | 0,00E+00 | t/m2-año |

**Tabla 7.: Coordenadas de los receptores****

| ID | Nombre | Coordenadas UTM<br>(Huso 19. Datum WGS84) | Col4 |
| --- | --- | --- | --- |
| **ID** | **Nombre** | **Este (m)** | **Norte (m)** |
| R_1 | Estación Pozo Almonte | 417.707 | 7.760.616 |
| R_2 | Estación Alto Hospicio | 385.117 | 7.755.989 |
| R_3 | Hospital Regional de Iquique | 381.076 | 7.764.412 |
| R_4 | AI Campesina Pampa del Tamarugal - Transhumancia | 418.775 | 7.762.574 |
| R_5 | AI Campesina Pampa del Tamarugal - Río Aroma | 419.265 | 7.762.630 |
| R_6 | AI Campesina Pampa del Tamarugal - Casa Blanca | 423.608 | 7.764.423 |
| R_7 | AI Campesina Pampa del Tamarugal - Cerro Sagrado Corazón | 418.530 | 7.756.929 |
| R_8 | AI Campesina Pampa del Tamarugal - Majada | 431.513 | 7.772.518 |
| R_9 | AI Campesina Pampa del Tamarugal - Pampa Verde | 421.670 | 7.754.345 |
| R_10 | AI Campesina Pampa del Tamarugal - Rodal | 427.683 | 7.744.681 |
| R_11 | AI Campesina Pampa del Tamarugal - Transhumancia | 421.915 | 7.762.474 |
| R_12 | CI Patrimonial Pampa del Tamarugal - Apacheta | 417.786 | 7.762.400 |
| R_13 | CI Patrimonial Pampa del Tamarugal - Apacheta | 415.079 | 7.764.234 |
| R_14 | CI Patrimonial Pampa del Tamarugal - Apacheta | 429.542 | 7.760.068 |
| R_15 | CI Patrimonial Pampa del Tamarugal - Curuña/Diana | 418.585 | 7.745.639 |
| R_16 | CI Patrimonial Pampa del Tamarugal - La Huayca | 441.613 | 7.740.671 |
| R_17 | Familia Choque - Transhumancia | 420.654 | 7.762.188 |
| R_18 | Familia Choque - Ruta en Vehículo | 420.219 | 7.762.600 |
| R_19 | Familia Choque - Casa Blanca | 425.141 | 7.763.825 |
| R_20 | Familia Choque - Santa Emilia | 429.773 | 7.753.580 |
| R_21 | Familia Choque - Dupliza | 429.104 | 7.772.955 |
| R_22 | Familia Choque - San Felipe | 426.209 | 7.743.158 |
| R_23 | GHPPI Sol Naciente - Transhumancia | 418.754 | 7.763.757 |
| R_24 | GHPPI Sol Naciente - Predio Agrícola | 419.604 | 7.760.585 |
| R_25 | GHPPI Sol Naciente - Mesa Ceremonial | 420.168 | 7.760.481 |
| R_26 | GHPPI Sol Naciente - Poblado Andino | 418.677 | 7.760.184 |
| R_27 | GHPPI Sol Naciente - Quebrada Salar de Pintados | 420.436 | 7.761.737 |
| R_28 | GHPPI Sol Naciente - Pampa Yura | 428.832 | 7.771.921 |
| R_29 | GHPPI Sol Naciente - Dupliza | 435.558 | 7.766.532 |
| R_30 | GHPPI Sol Naciente - Rodales | 427.296 | 7.744.773 |
| R_31 | GHPPI Sol Naciente - Rodal El Refresco | 429.840 | 7.730.575 |

**Tabla 8: Detalle Archivo WRF****

| Proyección Cartográfica | Cónica conforme de Lambert (LCC) |
| --- | --- |
| Período | 1 Enero al 31 de Diciembre 2020 |
| Proyección Cartográfica | LCC-NWS 84 |
| Latitud de Origen de la Proyección | 20,181 S |
| Longitud de Origen de la Proyección | 69,770 W |
| Paralelo Estándar 1 | 19,871 S |
| Paralelo Estándar 2 | 20,491 S |
| Resolución de Grilla (1 km) | 1 km |
| Área del Dominio (km2) | 101 x 101 |

**Tabla 9.: Aporte del Proyecto Material Particulado Respirable MP10 y MP2,5 (μg/m** **[3]** **N) - Año Fase de Operación****

| Receptor | MP10 | Col3 | Col4 | Col5 | Col6 | Col7 | MP2,5 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor**<br>**Norma**<br>**Anual**<br>**D.S. No**<br>**12/2022** | **% de la**<br>**Norma** | **P98 24**<br>**hrs** | **Valor**<br>**Norma**<br>**Diaria**<br>**D.S. No**<br>**12/2022** | **% de la**<br>**Norma** | **Anual** | **Valor**<br>**Anual**<br>**Norma**<br>**D.S. No**<br>**12/2012** | **% de la**<br>**Norma** | **P98 24**<br>**hrs** | **Valor**<br>**Norma**<br>**Diaria**<br>**D.S. No**<br>**12/2012** | **% de la**<br>**Norma** |
| R_1 | 0,380 | 50 | 0,8% | 1,093 | 130 | 0,8% | 0,071 | 20 | 0,4% | 0,224 | 50 | 0,4% |
| R_2 | 0,923 | 0,923 | 1,8% | 1,781 | 1,781 | 1,4% | 0,225 | 0,225 | 1,1% | 0,435 | 0,435 | 0,9% |
| R_3 | 0,687 | 0,687 | 1,4% | 1,693 | 1,693 | 1,3% | 0,168 | 0,168 | 0,8% | 0,414 | 0,414 | 0,8% |
| R_4 | 1,295 | 1,295 | 2,6% | 3,270 | 3,270 | 2,5% | 0,253 | 0,253 | 1,3% | 0,701 | 0,701 | 1,4% |
| R_5 | 0,954 | 0,954 | 1,9% | 2,336 | 2,336 | 1,8% | 0,194 | 0,194 | 1,0% | 0,475 | 0,475 | 1,0% |
| R_6 | 0,157 | 0,157 | 0,3% | 0,408 | 0,408 | 0,3% | 0,035 | 0,035 | 0,2% | 0,099 | 0,099 | 0,2% |
| R_7 | 0,068 | 0,068 | 0,1% | 0,181 | 0,181 | 0,1% | 0,014 | 0,014 | 0,1% | 0,039 | 0,039 | 0,1% |
| R_8 | 0,018 | 0,018 | 0,0% | 0,053 | 0,053 | 0,0% | 0,004 | 0,004 | 0,0% | 0,012 | 0,012 | 0,0% |
| R_9 | 0,048 | 0,048 | 0,1% | 0,122 | 0,122 | 0,1% | 0,011 | 0,011 | 0,1% | 0,026 | 0,026 | 0,1% |
| R_10 | 0,022 | 0,022 | 0,0% | 0,046 | 0,046 | 0,0% | 0,005 | 0,005 | 0,0% | 0,010 | 0,010 | 0,0% |
| R_11 | 0,343 | 0,343 | 0,7% | 0,782 | 0,782 | 0,6% | 0,072 | 0,072 | 0,4% | 0,175 | 0,175 | 0,3% |
| R_12 | 4,998 | 4,998 | 10,0% | 9,764 | 9,764 | 7,5% | 0,719 | 0,719 | 3,6% | 1,651 | 1,651 | 3,3% |
| R_13 | 3,381 | 3,381 | 6,8% | 8,176 | 8,176 | 6,3% | 0,790 | 0,790 | 3,9% | 1,719 | 1,719 | 3,4% |
| R_14 | 0,059 | 0,059 | 0,1% | 0,160 | 0,160 | 0,1% | 0,013 | 0,013 | 0,1% | 0,035 | 0,035 | 0,1% |
| R_15 | 0,018 | 0,018 | 0,0% | 0,038 | 0,038 | 0,0% | 0,004 | 0,004 | 0,0% | 0,009 | 0,009 | 0,0% |
| R_16 | 0,012 | 0,012 | 0,0% | 0,030 | 0,030 | 0,0% | 0,003 | 0,003 | 0,0% | 0,007 | 0,007 | 0,0% |
| R_17 | 0,480 | 0,480 | 1,0% | 1,038 | 1,038 | 0,8% | 0,095 | 0,095 | 0,5% | 0,219 | 0,219 | 0,4% |
| R_18 | 0,627 | 0,627 | 1,3% | 1,322 | 1,322 | 1,0% | 0,129 | 0,129 | 0,6% | 0,285 | 0,285 | 0,6% |
| R_19 | 0,124 | 0,124 | 0,2% | 0,304 | 0,304 | 0,2% | 0,027 | 0,027 | 0,1% | 0,071 | 0,071 | 0,1% |
| R_20 | 0,040 | 0,040 | 0,1% | 0,094 | 0,094 | 0,1% | 0,009 | 0,009 | 0,0% | 0,020 | 0,020 | 0,0% |
| R_21 | 0,019 | 0,019 | 0,0% | 0,058 | 0,058 | 0,0% | 0,004 | 0,004 | 0,0% | 0,013 | 0,013 | 0,0% |
| R_22 | 0,020 | 0,020 | 0,0% | 0,040 | 0,040 | 0,0% | 0,004 | 0,004 | 0,0% | 0,009 | 0,009 | 0,0% |
| R_23 | 1,666 | 1,666 | 3,3% | 3,913 | 3,913 | 3,0% | 0,384 | 0,384 | 1,9% | 0,961 | 0,961 | 1,9% |
| R_24 | 0,228 | 0,228 | 0,5% | 0,614 | 0,614 | 0,5% | 0,047 | 0,047 | 0,2% | 0,125 | 0,125 | 0,3% |
| R_25 | 0,204 | 0,204 | 0,4% | 0,499 | 0,499 | 0,4% | 0,042 | 0,042 | 0,2% | 0,105 | 0,105 | 0,2% |
| R_26 | 0,214 | 0,214 | 0,4% | 0,601 | 0,601 | 0,5% | 0,043 | 0,043 | 0,2% | 0,120 | 0,120 | 0,2% |
| R_27 | 0,403 | 0,403 | 0,8% | 0,970 | 0,970 | 0,7% | 0,079 | 0,079 | 0,4% | 0,202 | 0,202 | 0,4% |

**Tabla 10.: Aporte del Proyecto Material Particulado Sedimentable MPS (mg/m** **[2]** **-día) Norma Secundaria - Año Fase de Operación****

| Receptores | MPS | Col3 | Col4 |
| --- | --- | --- | --- |
| **Receptores** | **Promedio Anual** | **Valor Norma Anual**<br>**Ordenanza Suiza** | **% de la Norma** |
| R_1 | 0,006 | 200 | 0,0% |
| R_2 | 0,017 | 0,017 | 0,0% |
| R_3 | 0,015 | 0,015 | 0,0% |
| R_4 | 0,030 | 0,030 | 0,0% |
| R_5 | 0,023 | 0,023 | 0,0% |
| R_6 | 0,004 | 0,004 | 0,0% |
| R_7 | 0,002 | 0,002 | 0,0% |
| R_8 | 0,001 | 0,001 | 0,0% |
| R_9 | 0,002 | 0,002 | 0,0% |
| R_10 | 0,001 | 0,001 | 0,0% |
| R_11 | 0,009 | 0,009 | 0,0% |
| R_12 | 0,107 | 0,107 | 0,1% |
| R_13 | 0,052 | 0,052 | 0,0% |
| R_14 | 0,002 | 0,002 | 0,0% |
| R_15 | 0,001 | 0,001 | 0,0% |
| R_16 | 0,002 | 0,002 | 0,0% |
| R_17 | 0,012 | 0,012 | 0,0% |
| R_18 | 0,015 | 0,015 | 0,0% |

**Tabla 11.: Aporte del Proyecto Dióxido de Nitrógeno NO** **2** **(μg/m** **[3]** **N) - Año Fase de Operación****

| Receptor | NO<br>2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor Norma**<br>**Anual D.S. No**<br>**114/2002** | **% de la Norma** | **P99 1 hora** | **Valor Norma**<br>**Horaria D.S.**<br>**No 114/2002** | **% de la Norma** |
| R_1 | 0,219 | 100 | 0,2% | 7,975 | 400 | 2,0% |
| R_2 | 0,145 | 0,145 | 0,1% | 1,651 | 1,651 | 0,4% |
| R_3 | 0,103 | 0,103 | 0,1% | 1,307 | 1,307 | 0,3% |
| R_4 | 0,899 | 0,899 | 0,9% | 29,389 | 29,389 | 7,3% |
| R_5 | 0,767 | 0,767 | 0,8% | 16,143 | 16,143 | 4,0% |
| R_6 | 0,156 | 0,156 | 0,2% | 4,693 | 4,693 | 1,2% |
| R_7 | 0,055 | 0,055 | 0,1% | 1,963 | 1,963 | 0,5% |
| R_8 | 0,015 | 0,015 | 0,0% | 0,271 | 0,271 | 0,1% |
| R_9 | 0,044 | 0,044 | 0,0% | 1,157 | 1,157 | 0,3% |
| R_10 | 0,020 | 0,020 | 0,0% | 0,273 | 0,273 | 0,1% |

**Tabla 12.: Aporte del Proyecto Monóxido de Carbono CO (μg/m** **[3]** **N) - Año Fase de Operación****

| Receptor | CO | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **P99 1 hora** | **Valor Norma**<br>**1 hr D.S. No**<br>**115/2002** | **% de la Norma** | **P99 8 horas** | **Valor Norma**<br>**8 hrs D.S. No**<br>**115/2002** | **% de la Norma** |
| R_1 | 5,272 | 30.000 | 0,0% | 2,127 | 10.000 | 0,0% |
| R_2 | 0,106 | 0,106 | 0,0% | 0,043 | 0,043 | 0,0% |
| R_3 | 0,087 | 0,087 | 0,0% | 0,037 | 0,037 | 0,0% |
| R_4 | 30,862 | 30,862 | 0,1% | 6,993 | 6,993 | 0,1% |
| R_5 | 15,767 | 15,767 | 0,1% | 4,045 | 4,045 | 0,0% |
| R_6 | 1,834 | 1,834 | 0,0% | 0,638 | 0,638 | 0,0% |
| R_7 | 0,884 | 0,884 | 0,0% | 0,251 | 0,251 | 0,0% |
| R_8 | 0,153 | 0,153 | 0,0% | 0,049 | 0,049 | 0,0% |
| R_9 | 0,645 | 0,645 | 0,0% | 0,166 | 0,166 | 0,0% |
| R_10 | 0,123 | 0,123 | 0,0% | 0,047 | 0,047 | 0,0% |
| R_11 | 2,881 | 2,881 | 0,0% | 1,074 | 1,074 | 0,0% |
| R_12 | 60,439 | 60,439 | 0,2% | 15,189 | 15,189 | 0,2% |
| R_13 | 59,548 | 59,548 | 0,2% | 12,857 | 12,857 | 0,1% |
| R_14 | 0,549 | 0,549 | 0,0% | 0,214 | 0,214 | 0,0% |
| R_15 | 0,100 | 0,100 | 0,0% | 0,035 | 0,035 | 0,0% |
| R_16 | 0,056 | 0,056 | 0,0% | 0,026 | 0,026 | 0,0% |
| R_17 | 4,354 | 4,354 | 0,0% | 1,350 | 1,350 | 0,0% |
| R_18 | 5,984 | 5,984 | 0,0% | 1,971 | 1,971 | 0,0% |
| R_19 | 1,488 | 1,488 | 0,0% | 0,447 | 0,447 | 0,0% |
| R_20 | 0,253 | 0,253 | 0,0% | 0,104 | 0,104 | 0,0% |
| R_21 | 0,190 | 0,190 | 0,0% | 0,056 | 0,056 | 0,0% |
| R_22 | 0,105 | 0,105 | 0,0% | 0,040 | 0,040 | 0,0% |
| R_23 | 35,217 | 35,217 | 0,1% | 9,144 | 9,144 | 0,1% |
| R_24 | 3,209 | 3,209 | 0,0% | 0,907 | 0,907 | 0,0% |
| R_25 | 2,257 | 2,257 | 0,0% | 0,670 | 0,670 | 0,0% |
| R_26 | 2,934 | 2,934 | 0,0% | 0,909 | 0,909 | 0,0% |
| R_27 | 4,341 | 4,341 | 0,0% | 1,360 | 1,360 | 0,0% |
| R_28 | 0,246 | 0,246 | 0,0% | 0,068 | 0,068 | 0,0% |

**Tabla 13.: Aporte del Proyecto Dióxido de Azufre (SO** **2** **) Norma Primaria (μg/m** **[3]** **N) - Año Fase de Operación****

| Receptor | SO - Norma primaria<br>2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor Norma**<br>**D.S. No**<br>**104/2018** | **% de la Norma** | **P99 24 hrs** | **Valor Norma**<br>**D.S. No**<br>**104/2018** | **% de la norma** | **P98,5 1 hr** | **Valor**<br>**Norma D.S.**<br>**No**<br>**104/2018** | **% de la Norma** |
| R_1 | 0,001 | 60 | 0,0% | 0,005 | 150 | 0,0% | 0,014 | 350 | 0,0% |
| R_2 | 0,001 | 0,001 | 0,0% | 0,001 | 0,001 | 0,0% | 0,003 | 0,003 | 0,0% |
| R_3 | 3,7E-04 | 3,7E-04 | 0,0% | 0,001 | 0,001 | 0,0% | 0,003 | 0,003 | 0,0% |
| R_4 | 0,005 | 0,005 | 0,0% | 0,017 | 0,017 | 0,0% | 0,047 | 0,047 | 0,0% |
| R_5 | 0,004 | 0,004 | 0,0% | 0,012 | 0,012 | 0,0% | 0,035 | 0,035 | 0,0% |
| R_6 | 0,001 | 0,001 | 0,0% | 0,003 | 0,003 | 0,0% | 0,008 | 0,008 | 0,0% |
| R_7 | 2,9E-04 | 2,9E-04 | 0,0% | 0,001 | 0,001 | 0,0% | 0,003 | 0,003 | 0,0% |
| R_8 | 7,7E-05 | 7,7E-05 | 0,0% | 2,9E-04 | 2,9E-04 | 0,0% | 0,001 | 0,001 | 0,0% |
| R_9 | 2,3E-04 | 2,3E-04 | 0,0% | 0,001 | 0,001 | 0,0% | 0,002 | 0,002 | 0,0% |
| R_10 | 1,0E-04 | 1,0E-04 | 0,0% | 2,5E-04 | 2,5E-04 | 0,0% | 0,001 | 0,001 | 0,0% |
| R_11 | 0,002 | 0,002 | 0,0% | 0,005 | 0,005 | 0,0% | 0,015 | 0,015 | 0,0% |
| R_12 | 0,009 | 0,009 | 0,0% | 0,031 | 0,031 | 0,0% | 0,112 | 0,112 | 0,0% |
| R_13 | 0,010 | 0,010 | 0,0% | 0,031 | 0,031 | 0,0% | 0,113 | 0,113 | 0,0% |
| R_14 | 3,0E-04 | 3,0E-04 | 0,0% | 0,001 | 0,001 | 0,0% | 0,003 | 0,003 | 0,0% |
| R_15 | 6,9E-05 | 6,9E-05 | 0,0% | 1,8E-04 | 1,8E-04 | 0,0% | 4,3E-04 | 4,3E-04 | 0,0% |
| R_16 | 5,5E-05 | 5,5E-05 | 0,0% | 1,5E-04 | 1,5E-04 | 0,0% | 3,0E-04 | 3,0E-04 | 0,0% |
| R_17 | 0,002 | 0,002 | 0,0% | 0,006 | 0,006 | 0,0% | 0,018 | 0,018 | 0,0% |

**Tabla 15.: Coordenadas del Punto de Máximo Impacto (PMI)****

| Contaminante | Estadígrafo | Coordenadas PMI<br>(UTM WGS84 - H19S) | Col4 | Aporte | Unidad |
| --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Este** | **Norte** | **Norte** | **Norte** |
| MP10 | Media Anual | 416.564 | 7.763.311 | 56,854 | ug/m3 |
| MP10 | Percentil 98 en 24 horas | 416.564 | 7.763.311 | 113,760 | ug/m3 |
| MP2,5 | Media Anual | 416.564 | 7.763.311 | 10,550 | ug/m3 |
| MP2,5 | Percentil 98 en 24 horas | 416.564 | 7.763.311 | 21,149 | ug/m3 |
| NO2 | Media Anual | 416.564 | 7.763.311 | 25,300 | ug/m3 |
| NO2 | Percentil 99 en 1 Hora | 416.559 | 7.764.307 | 417,990 | ug/m3 |
| CO | Percentil 99 en 1 hora | 416.559 | 7.764.307 | 409,470 | ug/m3 |
| CO | Percentil 99 8 Horas | 416.559 | 7.764.307 | 139,870 | ug/m3 |
| SO2 | Media Anual | 416.564 | 7.763.311 | 0,137 | ug/m3 |
| SO2 | Percentil 99 en 24 horas | 416.564 | 7.763.311 | 0,301 | ug/m3 |
| SO2 | Percentil 98,5 en 1 hora | 416.559 | 7.764.307 | 1.355 | ug/m3 |
| SO2 | Percentil 99,7 en 24 horas | 416.564 | 7.763.311 | 0,400 | ug/m3 |
| SO2 | Percentil 99,73 en 1 hora | 416.559 | 7.764.307 | 2,067 | ug/m3 |
| MPS | Media Anual | 416.564 | 7.763.311 | 0,709 | mg/m2-día |

**Tabla 16.: Lista de otros Proyectos con RCA evaluados****

| ID | Nombre Proyecto | Receptor en que estima aportes |
| --- | --- | --- |
| P1 | Parque Solar Fotovoltaico Negreiros | Pozo Almonte y Alto Hospicio |
| P2 | Parque Fotovoltaico Victor Jara | Pozo Almonte |
| P3 | Centro de Distribución CBB Tarapacá | Pozo Almonte |
| P4 | Planta Fotovoltaica Jardín Solar | Pozo Almonte |
| P5 | Centro de Distribución CDD Pozo Almonte | Pozo Almonte |

**Tabla 17.: Aporte de otros Proyectos con RCA evaluados (ug/m3N)****

| ID Proyecto | Estación | MP10 | Col4 | MP2,5 | Col6 | NO2 | Col8 | CO | Col10 | SO2 | Col12 | Col13 | Col14 | Col15 | MPS (mg/m2-<br>día) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID Proyecto** | **Estación** | **Media**<br>**Anual** | **P98 24 hrs** | **Media**<br>**Anual** | **P98 24**<br>**hrs** | **Media**<br>**Anual** | **P99 1 hora** | **P99 1 hora** | **P99 8**<br>**horas** | **Media**<br>**Anual** | **P99 24**<br>**hrs** | **P98,5 1**<br>**hr** | **P99,7**<br>**24 hrs** | **P99,73 1**<br>**hr** | **Media anual** |
| P1 | Pozo Almonte | 0,003 | 0,007 | 0,001 | 0,001 | -- | 0,011 | 0,002 | 0,005 | 0,0001 | 0,0001 | 0,0003 | 0,0001 | 0,0004 | 0,009 |
| P1 | Alto Hospicio | 0,009 | 0,024 | 0,002 | 0,006 | -- | 0,074 | 0,001 | 0,003 | 0,0001 | 0,0001 | 0,0001 | 0,0001 | 0,0001 | 0,012 |
| P2 | Pozo Almonte | 0,085 | 0,249 | 0,021 | 0,050 | 0,079 | 1,404 | 0,154 | 0,379 | 0,001 | 0,003 | 0,008 | 0,004 | 0,015 | 0,002 |
| P2 | Alto Hospicio | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| P3 | Pozo Almonte | 0,220 | 0,700 | 0,052 | 0,170 | 0,017 | 1,110 | 0,510 | 2,700 | 0,002 | 0,027 | 0,014 | 0,040 | 0,180 | -- |
| P3 | Alto Hospicio | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| P4 | Pozo Almonte | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,200 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | -- | -- | -- |
| P4 | Alto Hospicio | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |

**Tabla 18.: Concentraciones Proyectadas de MP10****

| Receptor | Estadístico | Concentraciones (μg/m3N) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadístico** | **Línea de**<br>**Base** | **Aporte**<br>**del**<br>**Proyecto** | **Aporte**<br>**Otros**<br>**Proyectos** | **Concentración**<br>**Final** | **Norma** | **% de la**<br>**Norma** |
| R-1 | Media Anual | 34,1 | 0,380 | 0,349 | 34,829 | 50 | 69,7% |
| R-1 | P98 24 hrs | 65,6 | 1,093 | 1,266 | 67,959 | 130 | 52,3% |
| R-2 | Media Anual | -- | 0,923 | 0,009 | 0,932 | 50 | 1,9% |
| R-2 | P98 24 hrs | -- | 1,781 | 0,024 | 1,805 | 130 | 1,4% |
| R-3 | Media Anual | -- | 0,687 | -- | 0,687 | 50 | 1,4% |
| R-3 | P98 24 hrs | -- | 1,693 | -- | 1,693 | 130 | 1,3% |
| R-4 | Media Anual | 34,1 | 1,295 | -- | 35,395 | 50 | 70,8% |
| R-4 | P98 24 hrs | 65,6 | 3,270 | -- | 68,870 | 130 | 53,0% |
| R-5 | Media Anual | 34,1 | 0,954 | -- | 35,054 | 50 | 70,1% |
| R-5 | P98 24 hrs | 65,6 | 2,336 | -- | 67,936 | 130 | 52,3% |
| R-6 | Media Anual | 34,1 | 0,157 | -- | 34,257 | 50 | 68,5% |

**Tabla 19.: Concentraciones Proyectadas de MP2,5****

| Receptor | Estadístico | Concentraciones (μg/m3N) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadístico** | **Línea de**<br>**Base** | **Aporte**<br>**del**<br>**Proyecto** | **Aporte**<br>**Otros**<br>**Proyectos** | **Concentración**<br>**Final** | **Norma** | **% de la**<br>**Norma** |
| R-1 | Media Anual | 9,1 | 0,071 | 0,103 | 9,274 | 20 | 46,4% |
| R-1 | P98 24 hrs | 17,6 | 0,224 | 0,412 | 18,236 | 50 | 36,5% |
| R-2 | Media Anual | 10,9 | 0,225 | 0,002 | 11,127 | 20 | 55,6% |
| R-2 | P98 24 hrs | 19,8 | 0,435 | 0,006 | 20,241 | 50 | 40,5% |
| R-3 | Media Anual | 10,9 | 0,168 | -- | 11,068 | 20 | 55,3% |
| R-3 | P98 24 hrs | 19,8 | 0,414 | -- | 20,214 | 50 | 40,4% |
| R-4 | Media Anual | 9,1 | 0,253 | -- | 9,353 | 20 | 46,8% |
| R-4 | P98 24 hrs | 17,6 | 0,701 | -- | 18,301 | 50 | 36,6% |
| R-5 | Media Anual | 9,1 | 0,194 | -- | 9,294 | 20 | 46,5% |
| R-5 | P98 24 hrs | 17,6 | 0,475 | -- | 18,075 | 50 | 36,2% |

**Tabla 20.: Concentraciones Proyectadas de NO2****

| Receptor | Estadístico | Concentraciones (μg/m3N) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadístico** | **Línea de**<br>**Base** | **Aporte**<br>**del**<br>**Proyecto** | **Aporte**<br>**Otros**<br>**Proyectos** | **Concentración**<br>**Final** | **Norma** | **% de la**<br>**Norma** |
| R-1 | Media Anual | -- | 0,219 | 0,256 | 0,475 | 100 | 0,5% |
| R-1 | P99 1 hr | -- | 7,975 | 7,985 | 15,960 | 400 | 4,0% |
| R-2 | Media Anual | -- | 0,145 | 0,000 | 0,145 | 100 | 0,1% |
| R-2 | P99 1 hr | -- | 1,651 | 0,074 | 1,725 | 400 | 0,4% |
| R-3 | Media Anual | -- | 0,103 | -- | 0,103 | 100 | 0,1% |
| R-3 | P99 1 hr | -- | 1,307 | -- | 1,307 | 400 | 0,3% |
| R-4 | Media Anual | -- | 0,899 | -- | 0,899 | 100 | 0,9% |
| R-4 | P99 1 hr | -- | 29,389 | -- | 29,389 | 400 | 7,3% |
| R-5 | Media Anual | -- | 0,767 | -- | 0,767 | 100 | 0,8% |

**Tabla 21.: Concentraciones Proyectadas de CO****

| Receptor | Estadístico | Concentraciones (μg/m3N) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadístico** | **Línea de**<br>**Base** | **Aporte**<br>**del**<br>**Proyecto** | **Aporte**<br>**Otros**<br>**Proyectos** | **Concentración**<br>**Final** | **Norma** | **% de la**<br>**Norma** |
| R-1 | P99 8 hrs | -- | 2,127 | 1,386 | 3,513 | 10000 | 0,0% |
| R-1 | P99 1 hr | -- | 5,272 | 4,343 | 9,615 | 30000 | 0,0% |
| R-2 | P99 8 hrs | -- | 0,043 | 0,001 | 0,044 | 10000 | 0,0% |
| R-2 | P99 1 hr | -- | 0,106 | 0,003 | 0,109 | 30000 | 0,0% |
| R-3 | P99 8 hrs | -- | 0,037 | -- | 0,037 | 10000 | 0,0% |
| R-3 | P99 1 hr | -- | 0,087 | -- | 0,087 | 30000 | 0,0% |
| R-4 | P99 8 hrs | -- | 6,993 | -- | 6,993 | 10000 | 0,1% |
| R-4 | P99 1 hr | -- | 30,862 | -- | 30,862 | 30000 | 0,1% |

**Tabla 22.: Concentraciones Proyectadas de SO2 Norma Primaria****

| Receptor | Estadístico | Concentraciones (μg/m3N) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadístico** | **Línea de**<br>**Base** | **Aporte**<br>**del**<br>**Proyecto** | **Aporte**<br>**Otros**<br>**Proyectos** | **Concentración**<br>**Final** | **Norma** | **% de la**<br>**Norma** |
| R_1 | Media Anual | 2,6 | 0,001 | 0,003 | 2,604 | 60 | 4,3% |
| R_1 | P99 24 hrs | 5,8 | 0,005 | 0,07 | 5,875 | 150 | 3,9% |
| R_1 | P98,5 1 hr | 8,1 | 0,014 | 0,103 | 8,217 | 350 | 2,3% |
| R_2 | Media Anual | -- | 0,001 | 0,000 | 0,001 | 60 | 0,0% |
| R_2 | P99 24 hrs | -- | 0,001 | 0,000 | 0,001 | 150 | 0,0% |
| R_2 | P98,5 1 hr | -- | 0,003 | 0,000 | 0,003 | 350 | 0,0% |
| R_3 | Media Anual | -- | 3,7E-04 | -- | 0,000 | 60 | 0,0% |

**Tabla 23.: Concentraciones Proyectadas de SO2 Norma Secundaria****

| Receptor | Estadístico | Concentraciones (μg/m3N) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadístico** | **Línea de**<br>**Base** | **Aporte**<br>**del**<br>**Proyecto** | **Aporte**<br>**Otros**<br>**Proyectos** | **Concentración**<br>**Final** | **Norma** | **% de la**<br>**Norma** |
| R_1 | Media Anual | 2,6 | 0,001 | 0,003 | 2,604 | 80 | 3,3% |
| R_1 | P99,7 24 hrs | 7,4 | 0,006 | 0,044 | 7,450 | 365 | 2,0% |
| R_1 | P99,73 1 hr | 15,6 | 0,027 | 0,196 | 15,823 | 1.000 | 1,6% |
| R_2 | Media Anual | -- | 0,001 | 0,000 | 0,001 | 80 | 0,0% |
| R_2 | P99,7 24 hrs | -- | 0,001 | 0,000 | 0,001 | 365 | 0,0% |
| R_2 | P99,73 1 hr | -- | 0,005 | 0,000 | 0,005 | 1.000 | 0,0% |
| R_3 | Media Anual | -- | 3,7E-04 | -- | 0,000 | 80 | 0,0% |
| R_3 | P99,7 24 hrs | -- | 0,001 | -- | 0,001 | 365 | 0,0% |
| R_3 | P99,73 1 hr | -- | 0,004 | -- | 0,004 | 1.000 | 0,0% |
| R_4 | Media Anual | 2,6 | 0,005 | -- | 2,605 | 80 | 3,3% |
| R_4 | P99,7 24 hrs | 7,4 | 0,021 | -- | 7,421 | 365 | 2,0% |
| R_4 | P99,73 1 hr | 15,6 | 0,085 | -- | 15,685 | 1.000 | 1,6% |
| R_5 | Media Anual | 2,6 | 0,004 | -- | 2,604 | 80 | 3,3% |
| R_5 | P99,7 24 hrs | 7,4 | 0,015 | -- | 7,415 | 365 | 2,0% |
| R_5 | P99,73 1 hr | 15,6 | 0,057 | -- | 15,657 | 1.000 | 1,6% |
| R_6 | Media Anual | 2,6 | 0,001 | -- | 2,601 | 80 | 3,3% |
| R_6 | P99,7 24 hrs | 7,4 | 0,003 | -- | 7,403 | 365 | 2,0% |
| R_6 | P99,73 1 hr | 15,6 | 0,015 | -- | 15,615 | 1.000 | 1,6% |
| R_7 | Media Anual | 2,6 | 2,9E-04 | -- | 2,600 | 80 | 3,3% |
| R_7 | P99,7 24 hrs | 7,4 | 0,001 | -- | 7,401 | 365 | 2,0% |
| R_7 | P99,73 1 hr | 15,6 | 0,006 | -- | 15,606 | 1.000 | 1,6% |

**Tabla 24.: Tasas de Depositación Proyectadas de MPS****

| Receptor | Estadístico | Tasa de Depositación (mg/m2-día) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadístico** | **Línea de**<br>**Base** | **Aporte**<br>**del**<br>**Proyecto** | **Aporte**<br>**Otros**<br>**Proyectos** | **Depositación**<br>**Final** | **Norma** | **% de la**<br>**Norma** |
| R_1 | Media Anual | -- | 0,006 | 0,011 | 0,017 | 200 | 0,0% |
| R_2 | Media Anual | -- | 0,017 | 0,012 | 0,029 | 200 | 0,0% |
| R_3 | Media Anual | -- | 0,015 | -- | 0,015 | 200 | 0,0% |
| R_4 | Media Anual | -- | 0,030 | -- | 0,030 | 200 | 0,0% |
| R_5 | Media Anual | -- | 0,023 | -- | 0,023 | 200 | 0,0% |
| R_6 | Media Anual | -- | 0,004 | -- | 0,004 | 200 | 0,0% |
| R_7 | Media Anual | -- | 0,002 | -- | 0,002 | 200 | 0,0% |
| R_8 | Media Anual | -- | 0,001 | -- | 0,001 | 200 | 0,0% |
| R_9 | Media Anual | -- | 0,002 | -- | 0,002 | 200 | 0,0% |
| R_10 | Media Anual | -- | 0,001 | -- | 0,001 | 200 | 0,0% |
| R_11 | Media Anual | -- | 0,009 | -- | 0,009 | 200 | 0,0% |
| R_12 | Media Anual | -- | 0,107 | -- | 0,107 | 200 | 0,1% |
| R_13 | Media Anual | -- | 0,052 | -- | 0,052 | 200 | 0,0% |
| R_14 | Media Anual | -- | 0,002 | -- | 0,002 | 200 | 0,0% |
| R_15 | Media Anual | -- | 0,001 | -- | 0,001 | 200 | 0,0% |
| R_16 | Media Anual | -- | 0,002 | -- | 0,002 | 200 | 0,0% |
| R_17 | Media Anual | -- | 0,012 | -- | 0,012 | 200 | 0,0% |
