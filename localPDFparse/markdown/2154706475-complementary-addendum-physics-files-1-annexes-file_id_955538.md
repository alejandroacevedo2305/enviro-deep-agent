---
title: Sin título
author: Argis
date: D:20240605151207-04'00'
language: es
type: report
pages: 57
has_toc: True
has_tables: True
extraction_quality: high
---

________________________________________________________________________________

**ADENDA COMPLEMENTARIA**

**ANEXO OBS. 071a**

**MODELACIÓN CALIDAD DEL AIRE**

**METALES PESADOS**

**PARTE 2**

Declaración de Impacto Ambiental
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo
Adenda Complementaria

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**ANEXO**

**Modelación de Calidad de Aire**

**Metales Pesados**

**Proyecto Redes Primarias y Planta de**
**Tratamiento de Aguas Servidas Localidad**

**de Maitencillo**

**Proyecto : 0126**
**Cliente: ESVAL S.A.**
**Dirigido a : Mario Figueroa**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 1 de 56

CONTROL INTERNO **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 2 de 56

**CONTROL INTERNO**

Proyecto Redes Primarias y Planta de Tratamiento de
Proyecto
Aguas Servidas Localidad de Maitencillo

ID Proyecto MC-0126

Servicio Modelación de Calidad del Aire - Metales pesados

Solicitado por : ESVAL S.A.

Mario Figueroa
Contacto:

Jefe Depto. Calidad y Medio Ambiente

Preparado por: Are Project SpA.

Aprobado por: Gerardo González - Gerente General

Fecha: Abril de 2024

|Versión del documento|Descripción|Fecha|
|---|---|---|
|V0.1|Reporte borrador|16-abr-2024|

|Elaboración|Col2|Aprobación|Col4|
|---|---|---|---|
|Nombre|Oscar<br>Santamaría|Nombre|Gerardo<br>González|
|Cargo|Ingeniero<br>de<br>Proyectos|Cargo|Gerente<br>General|
|Fecha|15-abr-2024|Fecha|16-abr-2024|
|Firma||Firma||

CONTROL INTERNO **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 3 de 56

**ÍNDICE**

CONTROL INTERNO .......................................................................................................................... 2
ÍNDICE ................................................................................................................................................ 3
1 MODELACIÓN DE METALES PESADOS .................................................................................... 6
1.1 ESCENARIO DE MODELACIÓN .......................................................................................... 6
1.2 EMISIONES ATMOSFÉRICAS ............................................................................................. 7
1.2.1 IDENTIFICACIÓN DE FUENTES DE EMISIÓN ................................................................ 7
1.2.2 TASAS DE EMISIÓN ........................................................................................................ 7

1.3 RECEPTORES DISCRETOS ............................................................................................... 8
1.4 RESULTADOS DE MODELACIÓN ESCENARIO 1 .............................................................. 9

1.5 CONCENTRACIONES DE METALES PESADO EN RECEPTORES ................................. 10
2 ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL ............................................. 11

2.1 CONCLUSIONES ............................................................................................................... 13
2.2 ISOLÍNEAS DE CONCENTRACIÓN .................................................................................. 14
3 ANEXO 1 - FUENTES DE EMISIÓN ........................................................................................... 19
4 ANEXO 2 - JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO ................................................. 42
4.1 JUSTIFICACIÓN DEL MODELO ........................................................................................ 42
4.2 DESCRIPCIÓN DEL MODELO .......................................................................................... 44
4.3 PROCESO DE MODELACIÓN ........................................................................................... 44
5 ANEXO 3 - RESPUESTAS ORGANISMOS AMBIENTALES (SMA, MMA) ................................ 46
5.1 RESPUESTA MINISTERIO DEL MEDIO AMBIENTE ......................................................... 46

5.2 RESPUESTA SUPERINTENDENCIA DEL MEDIO AMBIENTE ......................................... 48
6 CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN ........................................................... 50
6.1 DOMINIO DE MODELACIÓN ............................................................................................. 50
6.2 BASE METEOROLÓGICA ................................................................................................. 52
6.2.1 PERIODO DE MODELACIÓN ........................................................................................ 52
6.2.2 FUENTE DE DATOS METEOROLÓGICOS ................................................................... 52
6.2.3 DATOS TOPOGRÁFICOS Y DE USO DE SUELO ......................................................... 52
6.2.4 CONFIGURACIÓN DEL MODELO ................................................................................. 54
6.2.5 PARAMETRIZACIÓN RECEPTORES ............................................................................ 55
7 BIBLIOGRAFÍA ........................................................................................................................... 56

ÍNDICE **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 4 de 56

**ÍNDICE DE TABLAS**

Tabla 1. Concentración representativa de metales pesados en el suelo del área del Proyecto. ........... 6
Tabla 2. Receptores discretos.............................................................................................................. 8
Tabla 3. Límite normativo por contaminante ........................................................................................ 9
Tabla 4. Concentraciones de metales pesados en receptores sensibles - parte 1 ............................. 10
Tabla 5. Concentraciones de metales pesados en receptores sensibles - parte 2 ............................. 10
Tabla 6 Línea base estación de calidad del aire Puchuncaví año 2022 ............................................. 12

Tabla 7 Aumento de las concentraciones basales en EMRP Puchuncaví .......................................... 12
Tabla 8. Escenario 1 - Descripción de las fuentes de emisión de área parte 1 .................................. 19
Tabla 9. Escenario 1 - Descripción de las fuentes de emisión de área parte 2 .................................. 20
Tabla 10. Escenario 1 - Descripción de las fuentes de emisión de área parte 3 ................................ 21
Tabla 11. Escenario 1 - Descripción de las fuentes de emisión de área parte 4 ................................ 22
Tabla 12. Escenario 1 - Descripción de las fuentes de emisión de área parte 5 ................................ 23
Tabla 13. Escenario 1 - Descripción de las fuentes de emisión de área parte 6 ................................ 24
Tabla 14. Escenario 1 - Descripción de las fuentes de emisión de área parte 7 ................................ 25
Tabla 15. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 8 .......................... 26
Tabla 16. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 9 .......................... 27
Tabla 17. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 10 ........................ 28
Tabla 18. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 11 ........................ 29
Tabla 19. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 12 ........................ 30
Tabla 20. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 13 ........................ 31
Tabla 21. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 14 ........................ 32
Tabla 22. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 15 ........................ 33
Tabla 23. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 16 ........................ 34
Tabla 24. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 17 ........................ 35
Tabla 25. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 18 ........................ 36
Tabla 26. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 19 ........................ 37
Tabla 27. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 20 ........................ 38
Tabla 28. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 21 ........................ 39
Tabla 29. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 22 ........................ 40
Tabla 30. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 23 ........................ 41
Tabla 31. Análisis porcentual de vientos calmos - Estación Puchuncaví ........................................... 50
Tabla 32. Parametrización grilla 1 receptores .................................................................................... 55
Tabla 33. Parametrización grilla 2 receptores .................................................................................... 55
Tabla 34. Parametrización grilla 3 receptores .................................................................................... 55
Tabla 35. Parametrización grilla 4 receptores .................................................................................... 55
Tabla 36. Parametrización grilla 5 receptores .................................................................................... 55

ÍNDICE **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 5 de 56

**ÍNDICE DE FIGURAS**

Figura 1. E1 Isolíneas Arsénico Concentración Anual ........................................................................ 14
Figura 2. E1 Isolíneas Cadmio Concentración Anual .......................................................................... 15
Figura 3. E1 Isolíneas Cromo Concentración Anual ........................................................................... 16
Figura 4. E1 Isolíneas Níquel Concentración Anual ........................................................................... 17
Figura 5. E1 Isolíneas Plomo Concentración Anual ........................................................................... 18
Figura 6. Modelación de calidad de aire ............................................................................................. 45
Figura 7. Dominio de modelación ....................................................................................................... 51
Figura 8. Elevación de terreno del dominio ........................................................................................ 53
Figura 9. Uso de suelo del dominio .................................................................................................... 54

ÍNDICE **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 6 de 56

**1** **MODELACIÓN DE METALES PESADOS**

**1.1** **ESCENARIO DE MODELACIÓN**

A continuación, se presenta la evaluación de la dispersión de las emisiones de metales
pesados con respecto al material particulado MP10 del peor escenario de modelación
correspondiente al Escenario 1 del proyecto contemplando la construcción simultanea de la
Planta de Tratamiento de Aguas Servidas, de acuerdo con lo estipulado en cronograma de
actividades. Esta evaluación se fundamenta en la magnitud de las emisiones, que se
consideran las más conservadoras según lo estipulado en el inventario de emisiones llevado
a cabo por los consultores de GSI. Este análisis responde a la solicitud de la autoridad
ambiental contenida en el documento ICSARA N°20230510381 (en adelante, ICSARA), que
requiere la evaluación del transporte de material particulado 10 (PM10) en su fracción de
metales pesados hacia los receptores sensibles

Se evaluaron los contaminantes Arsénico (As), Cadmio (Cd), Níquel (Ni), Cromo (Cr) y Plomo
(Pb), de acuerdo con las exigencias de la autoridad ambiental, que solicitó la evaluación de la
normativa de referencia establecida en el Real Decreto 102/2011 del Reino de España, como
se detalla en el documento ICSARA N°20230510381, específicamente en relación con la
concentración de metales pesados.

Es relevante destacar que las normas de referencia utilizadas en este análisis se ajustan a las
directrices proporcionadas por la autoridad ambiental en el mencionado ICSARA, además de
tener en cuenta las que están disponibles en el documento "Normas de Calidad y Valores de
Referencia" para el Sistema de Evaluación de Impacto Ambiental (SEIA), considerando
exclusivamente sólo los valores límites disponibles y establecidos en dicho documento."

Para el cálculo de las tasas de emisión de los contaminantes denominados como metales
pesados, se consideró la concentración de metales pesados en el suelo representativa del
área del proyecto (sector PTAS y sector Redes) [1] . A continuación, se presenta la concentración
de metales pesados en el suelo que se considera representativa del área del Proyecto para
los contaminantes sujetos a evaluación:

Tabla 1. Concentración representativa de metales pesados en el suelo del área del Proyecto.

|Contaminantes|Concentración en el suelo<br>mg/Kg|Col3|
|---|---|---|
|Contaminantes|Sector PTAS|Sector Redes|
|Arsénico|15,19|14,29|
|Cadmio|0,55|1,11|
|Cromo|22,68|27,29|
|Níquel|10,68|11,83|
|Plomo|21,85|26,94|

1 DIA. (2022). “Proyecto redes primarias y planta de Tratamiento de aguas servidas localidad de Maitencillo”. Adenda. Obs.
151. Estudio de metales pesados - suelo

MODELACIÓN DE METALES PESADOS **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 7 de 56

**1.2** **EMISIONES ATMOSFÉRICAS**

**1.2.1** **IDENTIFICACIÓN DE FUENTES DE EMISIÓN**

Las fuentes de emisión identificadas corresponden a las actividades consideradas en el
inventario de emisiones elaborado por consultores de GSI.

Las fuentes se han caracterizado en su totalidad a fuentes de área. Estas se han incorporado
en el modelo de dispersión CALPUFF para llevar a cabo la correspondiente modelación
atmosférica. Con respecto a la asignación de las tasas de emisión en el modelo, se ha utilizado
el estudio de la concentración de metales pesados en las muestras de suelo del proyecto como
un factor multiplicativo para las tasas de emisión de partículas PM10 asociadas con las
operaciones de resuspensión y de movimientos de tierra asociados a excavaciones de las
emisiones de PM10.

**1.2.2** **TASAS DE EMISIÓN**

Las tasas de emisión empleadas en la modelación correspondiente al Escenario 1 se
encuentran detalladas al final de este informe.

MODELACIÓN DE METALES PESADOS **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 8 de 56

**1.3** **RECEPTORES DISCRETOS**

Para evaluar el cumplimiento de las normas primarias relacionadas con los contaminantes
Arsénico (As), Cadmio (Cd), Cromo (Cr), Níquel (Ni) y Plomo (Pb), se han identificado un total
de 26 receptores ubicados en las proximidades del proyecto. La selección de estos receptores
se basó en los estudios de ruido y olores, los cuales fueron determinados por el titular del
proyecto en función de su proximidad a las obras que se llevarán a cabo.

Tabla 2. Receptores discretos

|ID|Coordenadas UTM [m]<br>(WGS84-H19S)|Col3|Descripción|
|---|---|---|---|
|ID|X:Este|Y: Sur|Y: Sur|
|R1|273.467|6.387.304|Receptor ruido 1|
|R2|273.165|6.386.964|Receptor ruido 2|
|R3|272.667|6.386.718|Receptor ruido 3|
|R4|272.686|6.386.266|Receptor ruido 4|
|R5|272.095|6.386.403|Receptor ruido 5|
|R6|272.061|6.386.029|Receptor ruido 6|
|R7|272.062|6.385.336|Receptor ruido 7|
|R8|272.550|6.385.155|Receptor ruido 8|
|R9|272.361|6.384.963|Receptor ruido 9|
|R10|272.633|6.384.083|Receptor ruido 10|
|R11|271.742|6.385.511|Receptor ruido 12|
|R12|271.303|6.385.031|Receptor ruido 13|
|R13|270.870|6.384.346|Receptor ruido 14|
|R14|271.064|6.383.040|Receptor ruido 15|
|R15|271.195|6.382.539|Receptor ruido 16|
|R16|273.437|6.383.498|Receptor fauna|
|R17|272.900|6.384.175|Receptor olor 1|
|R18|273.262|6.384.342|Receptor olor 2|
|R19|273.332|6.384.523|Receptor olor 3|
|R20|273.201|6.382.149|Receptor olor 4|
|R21|274.626|6.383.665|Receptor olor 5|
|R22|275.043|6.382.044|Receptor olor 6|
|R23|272.529|6.383.695|Receptor olor 7|
|R24|272.543|6.383.117|Receptor olor 8|
|R25|272.512|6.382.513|Receptor olor 9|
|R26|274.379|6.377.371|Estación Puchuncaví|

MODELACIÓN DE METALES PESADOS **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 9 de 56

**1.4** **RESULTADOS DE MODELACIÓN ESCENARIO 1**

A continuación, se presentan los resultados obtenidos de la modelación de calidad del aire
para el Escenario 1 del proyecto.

Los resultados muestran las concentraciones en receptores discretos y la comparación con el
límite de la normativa de calidad del aire aplicable para el Escenario 1, conformado en función
del cronograma de Obras Fase Construcción:

Tabla 3. Límite normativo por contaminante

|Escenario de<br>modelación|Contaminante|Normativa de referencia|Tipo de Norma|Unidad|Tipo|Límite|
|---|---|---|---|---|---|---|
|E1: Escenario 1|Arsénico (As)|Real Decreto 102/20112|Primaria|[ng/m3]|Anual|6|
|E1: Escenario 1|Cadmio (Cd)|Real Decreto 102/2011|Primaria|[ng/m3]|Anual|5|
|E1: Escenario 1|Cadmio (Cd)|OMS3|Primaria|[ng/m3]|Anual|5|
|E1: Escenario 1|Níquel (Ni)|Real Decreto 102/2011|Primaria|[ng/m3]|Anual|20|
|E1: Escenario 1|Plomo (Pb)|D.S. N°136/20004|Primaria|[ng/m3]|Anual|500|
|E1: Escenario 1|Plomo (Pb)|Real Decreto 102/2011|Primaria|[ng/m3]|Anual|500|
|E1: Escenario 1|Plomo (Pb)|OMS|Primaria|[ng/m3]|Anual|500|
|E1: Escenario 1|Cromo (Cr)|Nueva Zelandia AAQG5|Primaria|[ng/m3]|Anual|110|

2 Real Decreto 102/2011, de 28 de enero, relativo a la mejora de la calidad del aire. España.
https://www.boe.es/eli/es/rd/2011/01/28/102/con.
3 WHO (2000) - Air Quality Guidelines for Europe. Regional Office for Europe Copenhagen.
4 [D.S. 136/2000. Establece Norma De Calidad Primaria Para Plomo En El Aire. Chile. https://bcn.cl/2ldka](https://bcn.cl/2ldka)
5 WHO (2000) - Air Quality Guidelines for Europe. Regional Office for Europe Copenhagen.

MODELACIÓN DE METALES PESADOS **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**1.5** **CONCENTRACIONES DE METALES PESADO EN RECEPTORES**

-
Tabla 4. Concentraciones de metales pesados en receptores sensibles parte 1

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 10 de 56

|Contaminante|Tipo de Norma|Unidad|Tipo|Límite|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Arsénico (As)|Primaria|[ng/m3]|Anual|6|0,0003|0,0004|0,0023|0,0004|0,0004|0,0004|0,0044|0,0008|0,0021|0,0023|0,0143|0,0021|
|Cadmio (Cd)|Primaria|[ng/m3]|Anual|5|0,0000|0,0000|0,0002|0,0000|0,0000|0,0000|0,0003|0,0001|0,0002|0,0002|0,0011|0,0002|
|Níquel (Ni)|Primaria|[ng/m3]|Anual|20|0,0003|0,0003|0,0019|0,0003|0,0003|0,0003|0,0037|0,0006|0,0017|0,0019|0,0118|0,0018|
|Plomo (Pb)|Primaria|[ng/m3]|Anual|500|0,0006|0,0006|0,0043|0,0007|0,0007|0,0007|0,0083|0,0014|0,0038|0,0042|0,0269|0,0040|
|Plomo (Pb)*|Primaria|[ng/m3]|Anual|500|0,0006|0,0006|0,0042|0,0007|0,0007|0,0007|0,0083|0,0014|0,0038|0,0042|0,0267|0,0040|
|Cromo (Cr)|Primaria|[ng/m3]|Anual|110|0,0006|0,0006|0,0043|0,0007|0,0007|0,0008|0,0084|0,0014|0,0038|0,0043|0,0273|0,0041|

*Calculado según D.S. N°136/2000 [6]

-
Tabla 5. Concentraciones de metales pesados en receptores sensibles parte 2

|Contaminante|Tipo de Norma|Unidad|Tipo|Límite|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Arsénico (As)|Primaria|[ng/m3]|Anual|6|0,0123|0,0004|0,0002|0,0129|0,0018|0,0022|0,0019|0,0017|0,0058|0,0025|0,0016|0,0009|0,0006|
|Cadmio (Cd)|Primaria|[ng/m3]|Anual|5|0,0010|0,0000|0,0000|0,0006|0,0001|0,0001|0,0001|0,0001|0,0002|0,0001|0,0001|0,0001|0,0000|
|Níquel (Ni)|Primaria|[ng/m3]|Anual|20|0,0102|0,0003|0,0001|0,0095|0,0014|0,0016|0,0014|0,0012|0,0042|0,0018|0,0013|0,0007|0,0004|
|Plomo (Pb)|Primaria|[ng/m3]|Anual|500|0,0232|0,0007|0,0003|0,0201|0,0030|0,0035|0,0030|0,0026|0,0086|0,0037|0,0028|0,0016|0,0009|
|Plomo (Pb)*|Primaria|[ng/m3]|Anual|500|0,0231|0,0007|0,0003|0,0201|0,0030|0,0035|0,0030|0,0026|0,0086|0,0037|0,0028|0,0016|0,0009|
|Cromo (Cr)|Primaria|[ng/m3]|Anual|110|0,0235|0,0007|0,0003|0,0207|0,0031|0,0036|0,0031|0,0027|0,0089|0,0039|0,0029|0,0017|0,0010|

*Calculado según D.S. N°136/2000 [7]

6 [D.S. 136/2000. Establece Norma De Calidad Primaria Para Plomo En El Aire. Chile. https://bcn.cl/2ldka](https://bcn.cl/2ldka)
7 Ibíd.

MODELACIÓN DE METALES PESADOS **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 11 de 56

**2** **ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL**

Para el análisis de contribución del proyecto a la condición basal de los respectivos
contaminantes, se utilizó información obtenida del proyecto “Desarrollo Urbano Habitacional
Maratué de Puchuncaví” de los registros provenientes de la especiación química realizados a
través del monitoreo discreto a los filtros de MP10 de las estaciones monitoras de calidad de
aire para los metales pesados de interés, de acuerdo con los indicado en el Anexo III.2 “Línea
de Base de Clima, Meteorología y calidad del Aire”, en Adenda Complementaria.

A pesar de que en el ICSARA se requería: “Presentar la especiación química de las emisiones
de MP10 de los metales pesados de interés que permita determinar del resultado de la
modelación el incremento de las concentraciones de MP10 el aporte de metales pesados. _Esta_
_información se puede obtener mediante solicitud de transparencia al Ministerio del Medio_
_Ambiente”_ .

Se realizó la solicitud correspondiente. Sin embargo, la autoridad ambiental indicó que no
disponía de dicha información.

**Respuesta SMA** **[8]** **.**
En razón de lo expuesto precedentemente, indicamos que este servicio no posee la
información requerida, por lo que de acuerdo a lo señalado en el artículo 13 de la ley N°20.285,
su solicitud será derivada al Ministerio del Medio Ambiente y a la Secretaría Regional
Ministerial de Salud de la región de Valparaíso, para que entreguen respuesta dentro del marco
de sus respectivas competencias.

**Respuesta MMA** **[9]** **.**
Al respecto, Informamos a usted que el Ministerio del Medio Ambiente no cuenta con la
información solicitada, toda vez que es la Superintendencia del Medio Ambiente (SMA) la
entidad pública que competente en el ámbito.

Pese a lo anterior, se recopiló la información desde los informes en Adenda complementaria
del proyecto mencionado para el periodo 2022 específicamente la estación de calidad del aire
Puchuncaví, esto debido a su cercanía con las fuentes de emisión y periodo anual utilizado en
la modelación de calidad del aire. Los contaminantes utilizados correspondieron a los
disponibles por dicha estación, los cuales fueron: Arsénico (As), Cadmio (Cd), Cromo (Cr),
Níquel (Ni) y Plomo (Pb).

A modo de actualización, se requirió nuevamente la solicitud al MMA, cuya institución declaró
no tener la información indicada derivándonos con la Superintendencia de Medio Ambiente,
cuyo requerimiento está en curso y a la espera de obtener una respuesta (Ver Anexo). Debido
a lo anterior, se obtuvieron las concentraciones de metales desde la adenda complementaria
del proyecto “Desarrollo Urbano Habitacional Maratué de Puchuncaví” tomando el año 2022.

8 ORD N° 913 SMA 2023. Superintendencia del Medio Ambiente. Solicitud N° AW003T0007308. 23 de mayo de
2023.
9 Carta DJ N° 231957. Ministerio del Medio Ambiente. Respuesta a Folio N° AW002T0009656. 23 de mayo de
2023.

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 12 de 56

A continuación, se presentan los resultados de concentración de Arsénico (As), Cadmio (Cd),
Cromo (Cr), Níquel (Ni) y Plomo (Pb) simuladas en la Estación Puchuncaví (EMRP) y la
comparación con las concentraciones basales de calidad del aire.

Tabla 6 Línea base estación de calidad del aire Puchuncaví año 2022

|Contaminante|Promedio<br>Anual (ng/m3)|N° registros<br>para el<br>periodo anual|N° datos<br>válidos|Porcentaje de<br>completitud de<br>datos válidos|
|---|---|---|---|---|
|Arsénico (As)|7,31000|122|121|99.2%|
|Cadmio (Cd)|1,00000|122|121|99.2%|
|Níquel (Ni)|12,18000|122|121|99.2%|
|Plomo (Pb)|5,51000|122|121|99.2%|
|Cromo (Cr)|13,08000|122|121|99.2%|

Tabla 7 Aumento de las concentraciones basales en EMRP Puchuncaví

|Contaminante|Tipo de Norma|Estadístico|Medido EMRP<br>Puchuncaví<br>[ng/m3]|Modelado<br>EMRP<br>Puchuncaví<br>[ng/m3]|Total Aporte<br>proyecto +<br>línea base<br>[ng/m3]|Límite Norma|
|---|---|---|---|---|---|---|
|Arsénico (As)|Primaria|Promedio<br>Anual|7,31000|0,00025|7,31025|6|
|Cadmio (Cd)|Primaria|Promedio<br>Anual|1,00000|0,00001|1,00001|5|
|Níquel (Ni)|Primaria|Promedio<br>Anual|12,18000|0,00019|12,18019|20|
|Plomo (Pb)|Primaria|Promedio<br>Anual|5,51000|0,00041|5,51041|500|
|Cromo (Cr)|Primaria|Promedio<br>Anual|13,08000|0,00042|13,08042|110|

De los resultados obtenidos para el escenario evaluado, se concluye que los aportes del
proyecto a las concentraciones basales medidas en la estación de Puchuncaví para el periodo
2022 tienen una baja significancia, ya que no llegan ni al 1% de contribución.

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 13 de 56

**2.1** **CONCLUSIONES**

Las conclusiones con respecto a la modelación de metales originados por las actividades de
resuspensión de material particulado en la zona del proyecto son las siguientes:

 En lo que concierne al contaminante arsénico, los resultados de la modelación de

metales generados por las actividades de construcción del proyecto no exceden el límite
anual establecido en el Decreto 102/2011 del Reino de España en ninguno de los
receptores.

 Respecto al contaminante cadmio, los resultados de la modelación de metales

derivados de las actividades de construcción del proyecto no sobrepasan el límite anual
establecido en el Decreto 102/2011 del Reino de España y la OMS (2000) en ninguno
de los receptores.

 En cuanto al contaminante níquel, los resultados de la modelación de metales

procedentes de las actividades de construcción del proyecto no superan el límite anual
del Decreto 102/2011 del Reino de España en ninguno de los receptores.

 Respecto al contaminante plomo, los resultados de la modelación de metales

provenientes de las actividades de construcción del proyecto no exceden el límite anual
establecido en el Decreto 102/2011 del Reino de España, el D.S. N°136/2000 y la OMS
(2000) en ninguno de los receptores.

 En lo que respecta al contaminante cromo, los resultados de la modelación de metales

derivados de las actividades de construcción del proyecto no superan el límite anual
establecido en la normativa de la OMS (2000) en ninguno de los receptores.

Se concluye que el riesgo de exceder las normativas y su impacto en la salud de las personas
debido a la emisión de metales es prácticamente nulo, ya que las concentraciones se
encuentran muy por debajo de los estándares establecidos en las normativas mencionadas en
este estudio.

En cuanto a la evaluación del cumplimiento de la normativa aplicable utilizando la estación de
monitoreo más cercana (Estación EMRP Puchuncaví), el proyecto no altera la condición inicial
de la línea base para las concentraciones de Arsénico (As), Cadmio (Cd), Cromo (Cr), Níquel
(Ni) y Plomo (Pb).

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 14 de 56

**2.2** **ISOLÍNEAS DE CONCENTRACIÓN**

En el siguiente apartado se presentan las isolíneas de concentración de Arsénico (As), Cadmio (Cd), Cromo (Cr), Níquel (Ni) y
Plomo (Pb) para la fracción de metales pesados contenidas en el PM10.

Figura 1. E1 Isolíneas Arsénico Concentración Anual

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 2. E1 Isolíneas Cadmio Concentración Anual

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 15 de 56

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 3. E1 Isolíneas Cromo Concentración Anual

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 16 de 56

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 4. E1 Isolíneas Níquel Concentración Anual

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 17 de 56

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 5. E1 Isolíneas Plomo Concentración Anual

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 18 de 56

ANÁLISIS APORTE DEL PROYECTO A LA CONDICIÓN BASAL **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**3** **ANEXO 1 - FUENTES DE EMISIÓN**

Tabla 8. Escenario 1 - Descripción de las fuentes de emisión de área parte 1

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 19 de 56

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_1|Peas_1|270.862|6.384.348|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_2|Peas_2|271.312|6.385.052|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_3|Peas_3|272.644|6.386.732|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_4|Peas_5.1|271.757|6.385.539|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_5|Peas_5.2|272.602|6.384.124|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_6|Colec_1.1|270.894|6.383.950|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_7|Colec_1.2|270.876|6.384.052|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_8|Colec_1.3|270.873|6.384.151|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_9|Colec_1.4|270.873|6.384.253|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_10|Col_1_2.1|270.931|6.384.850|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_11|Col_1_2.2|271.016|6.384.942|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_12|Col_1_2.3|271.106|6.384.990|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_13|Col_1_2.4|271.203|6.385.001|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_14|Colec_2.1|271.534|6.385.454|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_15|Colec_2.2|271.640|6.385.468|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_16|Colec_2.3|271.734|6.385.512|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_17|Colec_5.1.1|271.798|6.385.551|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_18|Colec_5.1.2|271.860|6.385.633|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_19|Colec_5.1.3|271.915|6.385.715|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_20|Colec_5.1.4|271.973|6.385.798|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_21|Colec_5.1.5|272.032|6.385.882|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_22|Colec_5.1.6|272.063|6.385.983|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_23|Colec_5.1.7|272.071|6.386.082|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_24|Colec_5.1.8|272.080|6.386.180|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_25|Colec_5.1.9|272.092|6.386.283|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_26|Colec_5.1.10|272.101|6.386.381|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_27|Colec_5.1.11|272.112|6.386.484|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_28|Colec_5.1.12|272.122|6.386.584|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_29|Colec_5.1.13|272.132|6.386.683|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_30|Colec_5.1.14|272.171|6.386.767|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 9. Escenario 1 - Descripción de las fuentes de emisión de área parte 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 20 de 56

|Tipo<br>AREA|ID<br>SRC_31|Descripción<br>Colec_5.1.15|X1|Y1|Ciclo<br>operación<br>1 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_31|Descripción<br>Colec_5.1.15|[m]<br>272.225|[m]<br>6.386.788|[m]<br>6.386.788|[m2]<br>4|[g/m2s]<br>3,323E-08|[g/m2s]<br>2,5812E-09|[g/m2s]<br>6,346E-08|[g/m2s]<br>2,7509E-08|[g/m2s]<br>6,2646E-08|
|AREA|SRC_32|Imp_1.1|270.869|6.384.373|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_33|Imp_1.2|270.883|6.384.472|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_34|Imp_1.3|270.915|6.384.567|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_35|Imp_1.4|270.907|6.384.662|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_36|Imp_1.5|270.863|6.384.741|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_37|Imp_2.1|271.310|6.385.050|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_38|Imp_2.2|271.349|6.385.137|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_39|Imp_2.3|271.379|6.385.235|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_40|Imp_2.4|271.425|6.385.313|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_41|Imp_2.5|271.473|6.385.362|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_42|Imp_3.1|272.362|6.386.742|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_43|Imp_3.2|272.478|6.386.683|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_44|Imp_3.3|272.646|6.386.701|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_45|Imp_5.1.1|271.781|6.385.537|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_46|Imp_5.1.2|271.876|6.385.511|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_47|Imp_5.1.3|271.846|6.385.422|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_48|Imp_5.1.4|271.858|6.385.339|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_49|Imp_5.1.5|271.954|6.385.328|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_50|Imp_5.1.6|272.056|6.385.329|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_51|Imp_5.1.7|272.156|6.385.329|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_52|Imp_5.1.8|272.220|6.385.336|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_53|Imp_5.1.9|272.311|6.385.344|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_54|Imp_5.1.10|272.285|6.385.236|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_55|Imp_5.1.11|272.304|6.385.134|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_56|Imp_5.1.12|272.336|6.385.038|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_57|Imp_5.1.13|272.407|6.384.841|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_58|Imp_5.1.14|272.372|6.384.937|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_59|Imp_5.1.15|272.450|6.384.738|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_60|Imp_5.1.16|272.488|6.384.641|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 10. Escenario 1 - Descripción de las fuentes de emisión de área parte 3

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 21 de 56

|Tipo<br>AREA|ID<br>SRC_61|Descripción<br>Imp_5.1.17|X1|Y1|Ciclo<br>operación<br>1 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_61|Descripción<br>Imp_5.1.17|[m]<br>272.524|[m]<br>6.384.542|[m]<br>6.384.542|[m2]<br>4|[g/m2s]<br>3,323E-08|[g/m2s]<br>2,5812E-09|[g/m2s]<br>6,346E-08|[g/m2s]<br>2,7509E-08|[g/m2s]<br>6,2646E-08|
|AREA|SRC_62|Imp_5.1.18|272.555|6.384.455|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_63|Imp_5.1.19|272.599|6.384.360|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_64|Imp_5.1.20|272.630|6.384.265|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_65|Imp_5.2.1|272.632|6.384.030|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_66|Imp_5.2.2|272.629|6.383.932|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_67|Imp_5.2.3|272.630|6.383.829|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_68|Imp_5.2.4|272.630|6.383.727|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_69|Imp_5.2.5|272.640|6.383.641|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_70|Imp_5.2.6|272.746|6.383.639|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_71|Imp_5.2.7|272.851|6.383.632|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_72|Imp_5.2.8|272.942|6.383.633|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_73|Imp_5.2.9|273.063|6.383.633|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_74|Imp_5.2.10|273.174|6.383.643|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_75|Imp_5.2.11|273.241|6.383.541|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_76|Imp_5.2.12|273.289|6.383.443|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_77|Imp_5.2.13|273.365|6.383.370|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_78|Imp_5.2.14|273.435|6.383.287|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_79|Imp_5.2.15|273.517|6.383.233|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_80|Imp_5.2.16|273.550|6.383.131|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_81|IF_1_Redes|272.317|6.384.978|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_82|IF_2_PTAS|273.520|6.383.274|10 meses|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_83|Tub_1.1|272.633|6.383.633|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_84|Tub_1.2|272.635|6.383.539|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_85|Tub_1.3|272.525|6.383.555|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_86|Tub_1.4|272.458|6.383.630|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_87|Tub_1.5|272.378|6.383.683|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_88|Tub_1.6|272.300|6.383.735|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_89|Tub_1.7|272.197|6.383.722|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_90|Tub_1.8|272.122|6.383.755|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 11. Escenario 1 - Descripción de las fuentes de emisión de área parte 4

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 22 de 56

|Tipo<br>AREA|ID<br>SRC_91|Descripción<br>Tub_1.9|X1|Y1|Ciclo<br>operación<br>1 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_91|Descripción<br>Tub_1.9|[m]<br>272.060|[m]<br>6.383.844|[m]<br>6.383.844|[m2]<br>4|[g/m2s]<br>3,323E-08|[g/m2s]<br>2,5812E-09|[g/m2s]<br>6,346E-08|[g/m2s]<br>2,7509E-08|[g/m2s]<br>6,2646E-08|
|AREA|SRC_92|Tub_1.10|271.961|6.383.846|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_93|Tub_1.11|271.862|6.383.794|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_94|Tub_1.12|271.766|6.383.745|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_95|Tub_1.13|271.669|6.383.720|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_96|Tub_1.14|271.564|6.383.688|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_97|Tub_1.15|271.501|6.383.601|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_98|Tub_1.16|271.424|6.383.524|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_99|Tub_1.17|271.369|6.383.436|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_100|Tub_1.18|271.340|6.383.353|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_101|Tub_1.19|271.274|6.383.286|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_102|Tub_1.20|271.248|6.383.193|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_103|Tub_1.21|271.205|6.383.096|1 mes|4|3,323E-08|2,5812E-09|6,346E-08|2,7509E-08|6,2646E-08|
|AREA|SRC_537|PTAS|273.586|6.383.219|10 meses|4|3,4547E-07|1,2509E-08|5,1581E-07|2,429E-07|4,9694E-07|
|AREA|SRC_209|Cam_Cat_1-PEAS e Imp|273.043|6.387.323|3 mes|383|1,2384E-12|9,6195E-14|2,365E-12|1,0252E-12|2,3347E-12|
|AREA|SRC_210|Cam_Cat_2-PEAS e Imp|273.206|6.387.558|3 mes|1.145|4,1458E-13|3,2203E-14|7,9174E-13|3,4321E-13|7,8159E-13|
|AREA|SRC_211|Cam_Cat_3-PEAS e Imp|273.308|6.387.612|3 mes|456|1,041E-12|8,0864E-14|1,9881E-12|8,6182E-13|1,9626E-12|
|AREA|SRC_212|Cam_Cat_4-PEAS e Imp|273.511|6.387.668|3 mes|844|5,6274E-13|4,3711E-14|1,0747E-12|4,6586E-13|1,0609E-12|
|AREA|SRC_213|Cam_Cat_5-PEAS e Imp|273.721|6.387.707|3 mes|853|5,5631E-13|4,3212E-14|1,0624E-12|4,6054E-13|1,0488E-12|
|AREA|SRC_214|Cam_Cat_6-PEAS e Imp|273.880|6.387.880|3 mes|945|5,022E-13|3,9009E-14|9,5907E-13|4,1575E-13|9,4677E-13|
|AREA|SRC_215|Cam_Cat_7-PEAS e Imp|273.982|6.387.934|3 mes|458|1,0376E-12|8,0595E-14|1,9815E-12|8,5896E-13|1,9561E-12|
|AREA|SRC_216|Cam_Cat_8-PEAS e Imp|274.178|6.387.916|3 mes|782|6,0689E-13|4,7141E-14|1,159E-12|5,0242E-13|1,1441E-12|
|AREA|SRC_217|Cam_Cat_9-PEAS e Imp|274.216|6.387.945|3 mes|195|2,4284E-12|1,8863E-13|4,6377E-12|2,0104E-12|4,5782E-12|
|AREA|SRC_218|Cam_Cat_10-PEAS e Imp|274.213|6.388.017|3 mes|296|1,6059E-12|1,2474E-13|3,0668E-12|1,3294E-12|3,0275E-12|
|AREA|SRC_219|Cam_Cat_11-PEAS e Imp|274.177|6.388.250|3 mes|942|5,0419E-13|3,9164E-14|9,6287E-13|4,174E-13|9,5052E-13|
|AREA|SRC_220|Cam_Cat_12-PEAS e Imp|274.185|6.388.365|3 mes|458|1,0357E-12|8,0451E-14|1,9779E-12|8,5742E-13|1,9526E-12|
|AREA|SRC_221|Cam_Cat_13-PEAS e Imp|274.352|6.388.558|3 mes|1.017|4,6681E-13|3,626E-14|8,9148E-13|3,8645E-13|8,8005E-13|
|AREA|SRC_222|Cam_Cat_14-PEAS e Imp|274.654|6.388.846|3 mes|1.667|2,8477E-13|2,212E-14|5,4383E-13|2,3575E-13|5,3686E-13|
|AREA|SRC_223|Cam_Cat_15-PEAS e Imp|274.745|6.388.895|3 mes|410|1,1584E-12|8,9979E-14|2,2122E-12|9,5896E-13|2,1838E-12|
|AREA|SRC_224|Cam_Cat_16-PEAS e Imp|274.834|6.388.862|3 mes|371|1,2791E-12|9,9359E-14|2,4428E-12|1,0589E-12|2,4115E-12|
|AREA|SRC_225|Cam_Cat_17-PEAS e Imp|274.882|6.388.794|3 mes|331|1,4329E-12|1,113E-13|2,7365E-12|1,1862E-12|2,7014E-12|
|AREA|SRC_226|Cam_Cat_18-PEAS e Imp|274.979|6.388.768|3 mes|407|1,1674E-12|9,0681E-14|2,2294E-12|9,6644E-13|2,2008E-12|
|AREA|SRC_227|Cam_Cat_19-PEAS e Imp|275.069|6.388.799|3 mes|384|1,2357E-12|9,5985E-14|2,3599E-12|1,023E-12|2,3296E-12|
|AREA|SRC_228|Cam_Cat_20-PEAS e Imp|275.059|6.388.911|3 mes|460|1,0331E-12|8,0245E-14|1,9729E-12|8,5522E-13|1,9476E-12|
|AREA|SRC_229|Cam_Cat_21-PEAS e Imp|275.040|6.389.003|3 mes|374|1,2691E-12|9,858E-14|2,4236E-12|1,0506E-12|2,3926E-12|
|AREA|SRC_230|Cam_Cat_22-PEAS e Imp|274.958|6.389.092|3 mes|489|9,7057E-13|7,5391E-14|1,8535E-12|8,0349E-13|1,8297E-12|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 12. Escenario 1 - Descripción de las fuentes de emisión de área parte 5

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 23 de 56

|Tipo<br>AREA|ID<br>SRC_231|Descripción<br>Cam_Cat_23-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_231|Descripción<br>Cam_Cat_23-PEAS e Imp|[m]<br>274.915|[m]<br>6.389.184|[m]<br>6.389.184|[m2]<br>402|[g/m2s]<br>1,1803E-12|[g/m2s]<br>9,168E-14|[g/m2s]<br>2,254E-12|[g/m2s]<br>9,771E-13|[g/m2s]<br>2,2251E-12|
|AREA|SRC_232|Cam_Cat_24-PEAS e Imp|274.946|6.389.307|3 mes|503|9,4416E-13|7,3339E-14|1,8031E-12|7,8162E-13|1,78E-12|
|AREA|SRC_233|Cam_Cat_25-PEAS e Imp|275.049|6.389.374|3 mes|485|9,7867E-13|7,602E-14|1,869E-12|8,1019E-13|1,845E-12|
|AREA|SRC_234|Cam_Cat_26-PEAS e Imp|275.181|6.389.406|3 mes|541|8,7688E-13|6,8113E-14|1,6746E-12|7,2592E-13|1,6531E-12|
|AREA|SRC_235|Cam_Cat_27-PEAS e Imp|275.286|6.389.385|3 mes|424|1,1187E-12|8,6896E-14|2,1364E-12|9,2611E-13|2,109E-12|
|AREA|SRC_236|Cam_Cat_28-PEAS e Imp|275.372|6.389.387|3 mes|345|1,3757E-12|1,0686E-13|2,6273E-12|1,1389E-12|2,5936E-12|
|AREA|SRC_237|Cam_Cat_29-PEAS e Imp|275.519|6.389.442|3 mes|633|7,4963E-13|5,8229E-14|1,4316E-12|6,2058E-13|1,4132E-12|
|AREA|SRC_238|Cam_Cat_30-PEAS e Imp|275.575|6.389.512|3 mes|360|1,3173E-12|1,0232E-13|2,5157E-12|1,0905E-12|2,4835E-12|
|AREA|SRC_239|Cam_Cat_31-PEAS e Imp|275.579|6.389.623|3 mes|447|1,0613E-12|8,2435E-14|2,0267E-12|8,7856E-13|2,0007E-12|
|AREA|SRC_240|Cam_Cat_32-PEAS e Imp|275.473|6.389.738|3 mes|630|7,5399E-13|5,8568E-14|1,4399E-12|6,242E-13|1,4215E-12|
|AREA|SRC_241|Cam_Cat_33-PEAS e Imp|275.397|6.389.809|3 mes|419|1,1325E-12|8,7967E-14|2,1627E-12|9,3752E-13|2,135E-12|
|AREA|SRC_242|Cam_Cat_34-PEAS e Imp|275.382|6.389.918|3 mes|433|1,0969E-12|8,5202E-14|2,0947E-12|9,0805E-13|2,0679E-12|
|AREA|SRC_243|Cam_Cat_35-PEAS e Imp|275.487|6.390.018|3 mes|577|8,2322E-13|6,3945E-14|1,5721E-12|6,815E-13|1,552E-12|
|AREA|SRC_244|Cam_Cat_36-PEAS e Imp|275.630|6.390.045|3 mes|576|8,2366E-13|6,3979E-14|1,573E-12|6,8187E-13|1,5528E-12|
|AREA|SRC_245|Cam_Cat_37-PEAS e Imp|275.763|6.390.025|3 mes|533|8,9073E-13|6,9189E-14|1,7011E-12|7,3739E-13|1,6792E-12|
|AREA|SRC_246|Cam_Cat_38-PEAS e Imp|275.861|6.389.993|3 mes|412|1,153E-12|8,9562E-14|2,2019E-12|9,5452E-13|2,1737E-12|
|AREA|SRC_247|Cam_Cat_39-PEAS e Imp|276.044|6.389.963|3 mes|743|6,3902E-13|4,9637E-14|1,2204E-12|5,2901E-13|1,2047E-12|
|AREA|SRC_248|Cam_Cat_40-PEAS e Imp|276.114|6.389.925|3 mes|317|1,4977E-12|1,1634E-13|2,8602E-12|1,2399E-12|2,8235E-12|
|AREA|SRC_249|Cam_Cat_41-PEAS e Imp|276.133|6.389.885|3 mes|173|2,745E-12|2,1323E-13|5,2423E-12|2,2725E-12|5,1751E-12|
|AREA|SRC_250|Cam_Cat_42-PEAS e Imp|276.158|6.389.818|3 mes|287|1,6549E-12|1,2855E-13|3,1605E-12|1,37E-12|3,12E-12|
|AREA|SRC_251|Cam_Cat_43-PEAS e Imp|276.157|6.389.659|3 mes|633|7,5012E-13|5,8267E-14|1,4325E-12|6,2099E-13|1,4142E-12|
|AREA|SRC_252|Cam_Cat_44-PEAS e Imp|276.172|6.389.529|3 mes|521|9,1098E-13|7,0762E-14|1,7397E-12|7,5416E-13|1,7174E-12|
|AREA|SRC_253|Cam_Cat_45-PEAS e Imp|276.275|6.389.477|3 mes|468|1,0136E-12|7,8736E-14|1,9358E-12|8,3914E-13|1,911E-12|
|AREA|SRC_254|Cam_Cat_46-PEAS e Imp|276.411|6.389.458|3 mes|553|8,5785E-13|6,6635E-14|1,6383E-12|7,1017E-13|1,6173E-12|
|AREA|SRC_255|Cam_Cat_47-PEAS e Imp|276.501|6.389.471|3 mes|366|1,2962E-12|1,0068E-13|2,4753E-12|1,073E-12|2,4436E-12|
|AREA|SRC_256|Cam_Cat_48-PEAS e Imp|276.706|6.389.673|3 mes|1.151|4,1227E-13|3,2024E-14|7,8732E-13|3,413E-13|7,7722E-13|
|AREA|SRC_257|Cam_Cat_49-PEAS e Imp|277.353|6.390.498|3 mes|4.195|1,1315E-13|8,7891E-15|2,1609E-13|9,3671E-14|2,1331E-13|
|AREA|SRC_258|Cam_Cat_50-PEAS e Imp|277.494|6.390.575|3 mes|640|7,4169E-13|5,7612E-14|1,4164E-12|6,1401E-13|1,3983E-12|
|AREA|SRC_259|Cam_Cat_51-PEAS e Imp|279.440|6.391.244|3 mes|8.224|5,7725E-14|4,4839E-15|1,1024E-13|4,7788E-14|1,0882E-13|
|AREA|SRC_260|Cam_Cat_52-PEAS e Imp|283.346|6.393.239|3 mes|17.541|2,7063E-14|2,1022E-15|5,1683E-14|2,2404E-14|5,102E-14|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 13. Escenario 1 - Descripción de las fuentes de emisión de área parte 6

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 24 de 56

|Tipo<br>AREA|ID<br>SRC_261|Descripción<br>Cam_Cat_53-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_261|Descripción<br>Cam_Cat_53-PEAS e Imp|[m]<br>287.745|[m]<br>6.394.661|[m]<br>6.394.661|[m2]<br>18.483|[g/m2s]<br>2,5683E-14|[g/m2s]<br>1,995E-15|[g/m2s]<br>4,9048E-14|[g/m2s]<br>2,1262E-14|[g/m2s]<br>4,8419E-14|
|AREA|SRC_262|Cam_Pta_1-PEAS e Imp|273.147|6.383.634|3 mes|1.866|2,7036E-13|9,7892E-15|4,0367E-13|1,9009E-13|3,889E-13|
|AREA|SRC_263|Cam_Pta_2-PEAS e Imp|273.165|6.383.642|3 mes|81|6,2414E-12|2,2599E-13|9,319E-12|4,3883E-12|8,978E-12|
|AREA|SRC_264|Cam_Pta_3-PEAS e Imp|273.189|6.383.637|3 mes|94|5,3601E-12|1,9408E-13|8,003E-12|3,7686E-12|7,7102E-12|
|AREA|SRC_265|Cam_Pta_4-PEAS e Imp|273.241|6.383.562|3 mes|360|1,4019E-12|5,0759E-14|2,0931E-12|9,8564E-13|2,0165E-12|
|AREA|SRC_266|Cam_Pta_5-PEAS e Imp|273.289|6.383.445|3 mes|506|9,981E-13|3,6139E-14|1,4902E-12|7,0176E-13|1,4357E-12|
|AREA|SRC_267|Cam_Pta_6-PEAS e Imp|273.304|6.383.402|3 mes|180|2,8093E-12|1,0172E-13|4,1945E-12|1,9752E-12|4,041E-12|
|AREA|SRC_268|Cam_Pta_7-PEAS e Imp|273.331|6.383.382|3 mes|138|3,6448E-12|1,3197E-13|5,442E-12|2,5627E-12|5,2429E-12|
|AREA|SRC_269|Cam_Pta_8-PEAS e Imp|273.361|6.383.362|3 mes|146|3,4666E-12|1,2552E-13|5,176E-12|2,4374E-12|4,9865E-12|
|AREA|SRC_270|Cam_Pta_9-PEAS e Imp|273.393|6.383.346|3 mes|144|3,5045E-12|1,2689E-13|5,2325E-12|2,464E-12|5,041E-12|
|AREA|SRC_271|Cam_Pta_10-PEAS e Imp|273.413|6.383.324|3 mes|116|4,3382E-12|1,5708E-13|6,4774E-12|3,0502E-12|6,2403E-12|
|AREA|SRC_272|Cam_Pta_11-PEAS e Imp|273.447|6.383.229|3 mes|400|1,2614E-12|4,5673E-14|1,8834E-12|8,8689E-13|1,8145E-12|
|AREA|SRC_273|Cam_Pta_12-PEAS e Imp|273.463|6.383.220|3 mes|80|6,2976E-12|2,2802E-13|9,4029E-12|4,4278E-12|9,0588E-12|
|AREA|SRC_274|Cam_Pta_13-PEAS e Imp|273.473|6.383.218|3 mes|45|1,1183E-11|4,049E-13|1,6697E-11|7,8625E-12|1,6086E-11|
|AREA|SRC_275|Cam_Pta_14-PEAS e Imp|273.519|6.383.228|3 mes|189|2,6766E-12|9,6913E-14|3,9963E-12|1,8819E-12|3,8501E-12|
|AREA|SRC_276|Cam_Valpo_1-PEAS e Imp|267.407|6.370.003|3 mes|9.182|5,1701E-14|4,0159E-15|9,8734E-14|4,2801E-14|9,7468E-14|
|AREA|SRC_277|Cam_Valpo_2-PEAS e Imp|267.402|6.370.088|3 mes|338|1,4033E-12|1,09E-13|2,6799E-12|1,1617E-12|2,6455E-12|
|AREA|SRC_278|Cam_Valpo_3-PEAS e Imp|267.699|6.371.506|3 mes|5.789|8,2003E-14|6,3697E-15|1,566E-13|6,7886E-14|1,5459E-13|
|AREA|SRC_279|Cam_Valpo_4-PEAS e Imp|267.700|6.371.619|3 mes|452|1,0502E-12|8,158E-14|2,0057E-12|8,6945E-13|1,98E-12|
|AREA|SRC_280|Cam_Valpo_5-PEAS e Imp|267.517|6.371.917|3 mes|1.401|3,3873E-13|2,6311E-14|6,4688E-13|2,8042E-13|6,3859E-13|
|AREA|SRC_281|Cam_Valpo_6-PEAS e Imp|267.499|6.371.980|3 mes|261|1,8181E-12|1,4123E-13|3,4721E-12|1,5051E-12|3,4276E-12|
|AREA|SRC_282|Cam_Valpo_7-PEAS e Imp|267.496|6.372.042|3 mes|247|1,9217E-12|1,4927E-13|3,6699E-12|1,5909E-12|3,6228E-12|
|AREA|SRC_283|Cam_Valpo_8-PEAS e Imp|267.518|6.372.113|3 mes|294|1,6121E-12|1,2522E-13|3,0787E-12|1,3346E-12|3,0392E-12|
|AREA|SRC_284|Cam_Valpo_9-PEAS e Imp|267.547|6.372.151|3 mes|187|2,5327E-12|1,9673E-13|4,8368E-12|2,0967E-12|4,7747E-12|
|AREA|SRC_285|Cam_Valpo_10-PEAS e Imp|267.569|6.372.177|3 mes|137|3,4645E-12|2,6911E-13|6,6163E-12|2,8681E-12|6,5314E-12|
|AREA|SRC_286|Cam_Valpo_11-PEAS e Imp|267.738|6.372.319|3 mes|880|5,3955E-13|4,191E-14|1,0304E-12|4,4667E-13|1,0172E-12|
|AREA|SRC_287|Cam_Valpo_12-PEAS e Imp|267.762|6.372.358|3 mes|187|2,5444E-12|1,9764E-13|4,8592E-12|2,1064E-12|4,7969E-12|
|AREA|SRC_288|Cam_Valpo_13-PEAS e Imp|267.783|6.372.410|3 mes|225|2,1144E-12|1,6424E-13|4,0379E-12|1,7504E-12|3,9861E-12|
|AREA|SRC_289|Cam_Valpo_14-PEAS e Imp|267.855|6.372.669|3 mes|1.076|4,4134E-13|3,4282E-14|8,4284E-13|3,6537E-13|8,3203E-13|
|AREA|SRC_290|Cam_Valpo_15-PEAS e Imp|267.848|6.372.720|3 mes|208|2,2847E-12|1,7746E-13|4,3631E-12|1,8914E-12|4,3071E-12|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 14. Escenario 1 - Descripción de las fuentes de emisión de área parte 7

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 25 de 56

|Tipo<br>AREA|ID<br>SRC_291|Descripción<br>Cam_Valpo_16-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_291|Descripción<br>Cam_Valpo_16-PEAS e Imp|[m]<br>267.715|[m]<br>6.373.066|[m]<br>6.373.066|[m2]<br>1.484|[g/m2s]<br>3,1987E-13|[g/m2s]<br>2,4846E-14|[g/m2s]<br>6,1086E-13|[g/m2s]<br>2,648E-13|[g/m2s]<br>6,0303E-13|
|AREA|SRC_292|Cam_Valpo_17-PEAS e Imp|267.705|6.373.122|3 mes|225|2,1058E-12|1,6357E-13|4,0215E-12|1,7433E-12|3,9699E-12|
|AREA|SRC_293|Cam_Valpo_18-PEAS e Imp|267.701|6.373.182|3 mes|241|1,9679E-12|1,5286E-13|3,7582E-12|1,6291E-12|3,71E-12|
|AREA|SRC_294|Cam_Valpo_19-PEAS e Imp|267.704|6.373.237|3 mes|218|2,1779E-12|1,6917E-13|4,1592E-12|1,803E-12|4,1059E-12|
|AREA|SRC_295|Cam_Valpo_20-PEAS e Imp|267.713|6.373.309|3 mes|291|1,6298E-12|1,266E-13|3,1126E-12|1,3493E-12|3,0726E-12|
|AREA|SRC_296|Cam_Valpo_21-PEAS e Imp|267.741|6.373.522|3 mes|860|5,5188E-13|4,2869E-14|1,0539E-12|4,5688E-13|1,0404E-12|
|AREA|SRC_297|Cam_Valpo_22-PEAS e Imp|267.757|6.373.574|3 mes|214|2,2198E-12|1,7243E-13|4,2392E-12|1,8377E-12|4,1848E-12|
|AREA|SRC_298|Cam_Valpo_23-PEAS e Imp|267.777|6.373.617|3 mes|187|2,5342E-12|1,9685E-13|4,8397E-12|2,098E-12|4,7776E-12|
|AREA|SRC_299|Cam_Valpo_24-PEAS e Imp|267.817|6.373.719|3 mes|441|1,0761E-12|8,3587E-14|2,055E-12|8,9085E-13|2,0287E-12|
|AREA|SRC_300|Cam_Valpo_25-PEAS e Imp|267.843|6.373.782|3 mes|273|1,7415E-12|1,3528E-13|3,3258E-12|1,4417E-12|3,2832E-12|
|AREA|SRC_301|Cam_Valpo_26-PEAS e Imp|267.877|6.373.831|3 mes|236|2,0112E-12|1,5623E-13|3,8409E-12|1,665E-12|3,7916E-12|
|AREA|SRC_302|Cam_Valpo_27-PEAS e Imp|267.910|6.373.883|3 mes|246|1,9288E-12|1,4982E-13|3,6834E-12|1,5967E-12|3,6362E-12|
|AREA|SRC_303|Cam_Valpo_28-PEAS e Imp|268.105|6.374.174|3 mes|1.400|3,3919E-13|2,6347E-14|6,4777E-13|2,808E-13|6,3946E-13|
|AREA|SRC_304|Cam_Valpo_29-PEAS e Imp|268.274|6.374.430|3 mes|1.228|3,8655E-13|3,0026E-14|7,382E-13|3,2E-13|7,2873E-13|
|AREA|SRC_305|Cam_Valpo_30-PEAS e Imp|268.317|6.374.478|3 mes|254|1,8663E-12|1,4497E-13|3,5642E-12|1,545E-12|3,5185E-12|
|AREA|SRC_306|Cam_Valpo_31-PEAS e Imp|268.347|6.374.502|3 mes|154|3,0734E-12|2,3874E-13|5,8694E-12|2,5444E-12|5,7942E-12|
|AREA|SRC_307|Cam_Valpo_32-PEAS e Imp|269.602|6.375.295|3 mes|5.936|7,9977E-14|6,2124E-15|1,5273E-13|6,6209E-14|1,5078E-13|
|AREA|SRC_308|Cam_Valpo_33-PEAS e Imp|270.646|6.375.956|3 mes|4.938|9,6128E-14|7,4669E-15|1,8358E-13|7,9579E-14|1,8122E-13|
|AREA|SRC_309|Cam_Valpo_34-PEAS e Imp|270.700|6.375.970|3 mes|221|2,1505E-12|1,6705E-13|4,1069E-12|1,7803E-12|4,0542E-12|
|AREA|SRC_310|Cam_Valpo_35-PEAS e Imp|270.759|6.375.972|3 mes|232|2,0459E-12|1,5892E-13|3,9071E-12|1,6937E-12|3,857E-12|
|AREA|SRC_311|Cam_Valpo_36-PEAS e Imp|270.817|6.375.960|3 mes|238|1,996E-12|1,5504E-13|3,8118E-12|1,6524E-12|3,7629E-12|
|AREA|SRC_312|Cam_Valpo_37-PEAS e Imp|271.210|6.375.788|3 mes|1.711|2,7745E-13|2,1552E-14|5,2986E-13|2,2969E-13|5,2307E-13|
|AREA|SRC_313|Cam_Valpo_38-PEAS e Imp|271.299|6.375.786|3 mes|362|1,3111E-12|1,0185E-13|2,5039E-12|1,0854E-12|2,4718E-12|
|AREA|SRC_314|Cam_Valpo_39-PEAS e Imp|271.410|6.375.784|3 mes|444|1,069E-12|8,3033E-14|2,0414E-12|8,8494E-13|2,0152E-12|
|AREA|SRC_315|Cam_Valpo_40-PEAS e Imp|271.537|6.375.829|3 mes|540|8,7918E-13|6,8292E-14|1,679E-12|7,2783E-13|1,6575E-12|
|AREA|SRC_316|Cam_Valpo_41-PEAS e Imp|271.698|6.375.908|3 mes|718|6,6149E-13|5,1382E-14|1,2633E-12|5,4762E-13|1,2471E-12|
|AREA|SRC_317|Cam_Valpo_42-PEAS e Imp|271.943|6.376.040|3 mes|1.111|4,2712E-13|3,3177E-14|8,1569E-13|3,5359E-13|8,0523E-13|
|AREA|SRC_318|Cam_Valpo_43-PEAS e Imp|272.216|6.376.245|3 mes|1.366|3,4756E-13|2,6998E-14|6,6375E-13|2,8773E-13|6,5524E-13|
|AREA|SRC_319|Cam_Valpo_44-PEAS e Imp|272.308|6.376.283|3 mes|397|1,1963E-12|9,2926E-14|2,2846E-12|9,9037E-13|2,2553E-12|
|AREA|SRC_320|Cam_Valpo_45-PEAS e Imp|272.828|6.376.412|3 mes|2.140|2,2188E-13|1,7235E-14|4,2373E-13|1,8368E-13|4,1829E-13|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 15. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 8

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 26 de 56

|Tipo<br>AREA|ID<br>SRC_321|Descripción<br>Cam_Valpo_46-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_321|Descripción<br>Cam_Valpo_46-PEAS e Imp|[m]<br>272.961|[m]<br>6.376.463|[m]<br>6.376.463|[m2]<br>573|[g/m2s]<br>8,2861E-13|[g/m2s]<br>6,4364E-14|[g/m2s]<br>1,5824E-12|[g/m2s]<br>6,8596E-13|[g/m2s]<br>1,5621E-12|
|AREA|SRC_322|Cam_Valpo_47-PEAS e Imp|273.101|6.376.548|3 mes|656|7,2317E-13|5,6174E-14|1,3811E-12|5,9868E-13|1,3633E-12|
|AREA|SRC_323|Cam_Valpo_48-PEAS e Imp|273.683|6.376.890|3 mes|2.700|1,7582E-13|1,3657E-14|3,3577E-13|1,4555E-13|3,3146E-13|
|AREA|SRC_324|Cam_Valpo_49-PEAS e Imp|273.729|6.376.911|3 mes|199|2,3895E-12|1,8561E-13|4,5634E-12|1,9782E-12|4,5049E-12|
|AREA|SRC_325|Cam_Valpo_50-PEAS e Imp|273.841|6.376.934|3 mes|455|1,0422E-12|8,0953E-14|1,9903E-12|8,6277E-13|1,9648E-12|
|AREA|SRC_326|Cam_Valpo_51-PEAS e Imp|273.918|6.376.948|3 mes|315|1,5078E-12|1,1712E-13|2,8794E-12|1,2482E-12|2,8425E-12|
|AREA|SRC_327|Cam_Valpo_52-PEAS e Imp|273.963|6.376.959|3 mes|182|2,6042E-12|2,0228E-13|4,9733E-12|2,1559E-12|4,9095E-12|
|AREA|SRC_328|Cam_Valpo_53-PEAS e Imp|274.013|6.376.981|3 mes|220|2,1556E-12|1,6744E-13|4,1166E-12|1,7845E-12|4,0638E-12|
|AREA|SRC_329|Cam_Valpo_54-PEAS e Imp|274.045|6.377.010|3 mes|176|2,7012E-12|2,0982E-13|5,1586E-12|2,2362E-12|5,0924E-12|
|AREA|SRC_330|Cam_Valpo_55-PEAS e Imp|274.402|6.377.569|3 mes|2.655|1,788E-13|1,3889E-14|3,4146E-13|1,4802E-13|3,3708E-13|
|AREA|SRC_331|Cam_Valpo_56-PEAS e Imp|274.508|6.377.712|3 mes|712|6,6654E-13|5,1775E-14|1,2729E-12|5,518E-13|1,2566E-12|
|AREA|SRC_332|Cam_Valpo_57-PEAS e Imp|274.515|6.377.737|3 mes|106|4,4978E-12|3,4937E-13|8,5895E-12|3,7235E-12|8,4794E-12|
|AREA|SRC_333|Cam_Valpo_58-PEAS e Imp|274.530|6.377.783|3 mes|191|2,4874E-12|1,9321E-13|4,7502E-12|2,0592E-12|4,6893E-12|
|AREA|SRC_334|Cam_Valpo_59-PEAS e Imp|274.571|6.378.190|3 mes|1.641|2,8936E-13|2,2477E-14|5,526E-13|2,3955E-13|5,4552E-13|
|AREA|SRC_335|Cam_Valpo_60-PEAS e Imp|274.512|6.378.662|3 mes|1.902|2,4955E-13|1,9384E-14|4,7658E-13|2,0659E-13|4,7047E-13|
|AREA|SRC_336|Cam_Valpo_61-PEAS e Imp|274.484|6.378.742|3 mes|339|1,3988E-12|1,0866E-13|2,6714E-12|1,158E-12|2,6372E-12|
|AREA|SRC_337|Cam_Valpo_62-PEAS e Imp|274.397|6.378.959|3 mes|935|5,0778E-13|3,9442E-14|9,6971E-13|4,2036E-13|9,5728E-13|
|AREA|SRC_338|Cam_Valpo_63-PEAS e Imp|274.391|6.379.006|3 mes|190|2,504E-12|1,945E-13|4,782E-12|2,0729E-12|4,7206E-12|
|AREA|SRC_339|Cam_Valpo_64-PEAS e Imp|274.392|6.379.034|3 mes|109|4,3358E-12|3,3679E-13|8,2801E-12|3,5894E-12|8,1739E-12|
|AREA|SRC_340|Cam_Valpo_65-PEAS e Imp|274.513|6.379.469|3 mes|1.806|2,6291E-13|2,0422E-14|5,0209E-13|2,1765E-13|4,9565E-13|
|AREA|SRC_341|Cam_Valpo_66-PEAS e Imp|274.514|6.379.510|3 mes|163|2,906E-12|2,2573E-13|5,5497E-12|2,4057E-12|5,4785E-12|
|AREA|SRC_342|Cam_Valpo_67-PEAS e Imp|274.503|6.379.560|3 mes|209|2,2743E-12|1,7666E-13|4,3432E-12|1,8828E-12|4,2875E-12|
|AREA|SRC_343|Cam_Valpo_68-PEAS e Imp|274.488|6.379.623|3 mes|255|1,8584E-12|1,4436E-13|3,5491E-12|1,5385E-12|3,5035E-12|
|AREA|SRC_344|Cam_Valpo_69-PEAS e Imp|274.426|6.379.798|3 mes|746|6,3671E-13|4,9458E-14|1,2159E-12|5,271E-13|1,2004E-12|
|AREA|SRC_345|Cam_Valpo_70-PEAS e Imp|274.386|6.379.897|3 mes|429|1,1078E-12|8,6047E-14|2,1155E-12|9,1705E-13|2,0884E-12|
|AREA|SRC_346|Cam_Valpo_71-PEAS e Imp|274.352|6.379.981|3 mes|360|1,3178E-12|1,0236E-13|2,5166E-12|1,0909E-12|2,4844E-12|
|AREA|SRC_347|Cam_Valpo_72-PEAS e Imp|274.336|6.380.041|3 mes|249|1,9028E-12|1,478E-13|3,6337E-12|1,5752E-12|3,5871E-12|
|AREA|SRC_348|Cam_Valpo_73-PEAS e Imp|274.333|6.380.099|3 mes|228|2,0839E-12|1,6187E-13|3,9797E-12|1,7252E-12|3,9287E-12|
|AREA|SRC_349|Cam_Valpo_74-PEAS e Imp|274.332|6.380.163|3 mes|257|1,8452E-12|1,4333E-13|3,5238E-12|1,5275E-12|3,4786E-12|
|AREA|SRC_350|Cam_Valpo_75-PEAS e Imp|274.329|6.380.546|3 mes|1.530|3,1018E-13|2,4094E-14|5,9236E-13|2,5678E-13|5,8476E-13|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 16. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 9

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 27 de 56

|Tipo<br>AREA|ID<br>SRC_351|Descripción<br>Cam_Valpo_76-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_351|Descripción<br>Cam_Valpo_76-PEAS e Imp|[m]<br>274.323|[m]<br>6.380.578|[m]<br>6.380.578|[m2]<br>131|[g/m2s]<br>3,6364E-12|[g/m2s]<br>2,8246E-13|[g/m2s]<br>6,9445E-12|[g/m2s]<br>3,0104E-12|[g/m2s]<br>6,8554E-12|
|AREA|SRC_352|Cam_Valpo_77-PEAS e Imp|274.308|6.380.608|3 mes|138|3,4356E-12|2,6687E-13|6,5611E-12|2,8442E-12|6,4769E-12|
|AREA|SRC_353|Cam_Valpo_78-PEAS e Imp|274.078|6.381.086|3 mes|2.121|2,2387E-13|1,7389E-14|4,2752E-13|1,8533E-13|4,2204E-13|
|AREA|SRC_354|Cam_Valpo_79-PEAS e Imp|274.036|6.381.146|3 mes|293|1,6204E-12|1,2587E-13|3,0945E-12|1,3415E-12|3,0549E-12|
|AREA|SRC_355|Cam_Valpo_80-PEAS e Imp|273.997|6.381.192|3 mes|243|1,9559E-12|1,5193E-13|3,7353E-12|1,6192E-12|3,6874E-12|
|AREA|SRC_356|Cam_Valpo_81-PEAS e Imp|273.945|6.381.212|3 mes|225|2,1075E-12|1,637E-13|4,0248E-12|1,7447E-12|3,9732E-12|
|AREA|SRC_357|Cam_Valpo_82-PEAS e Imp|273.863|6.381.235|3 mes|341|1,3938E-12|1,0826E-13|2,6617E-12|1,1538E-12|2,6276E-12|
|AREA|SRC_358|Cam_Valpo_83-PEAS e Imp|273.527|6.381.309|3 mes|1.377|3,4483E-13|2,6785E-14|6,5852E-13|2,8546E-13|6,5008E-13|
|AREA|SRC_359|Cam_Valpo_84-PEAS e Imp|273.488|6.381.317|3 mes|159|2,9888E-12|2,3216E-13|5,7078E-12|2,4743E-12|5,6346E-12|
|AREA|SRC_360|Cam_Valpo_85-PEAS e Imp|273.437|6.381.311|3 mes|211|2,254E-12|1,7508E-13|4,3045E-12|1,866E-12|4,2493E-12|
|AREA|SRC_361|Cam_Valpo_86-PEAS e Imp|273.400|6.381.306|3 mes|149|3,1913E-12|2,4789E-13|6,0946E-12|2,6419E-12|6,0164E-12|
|AREA|SRC_362|Cam_Valpo_87-PEAS e Imp|273.330|6.381.278|3 mes|302|1,5718E-12|1,2209E-13|3,0017E-12|1,3012E-12|2,9632E-12|
|AREA|SRC_363|Cam_Valpo_88-PEAS e Imp|273.269|6.381.275|3 mes|240|1,9753E-12|1,5344E-13|3,7723E-12|1,6353E-12|3,7239E-12|
|AREA|SRC_364|Cam_Valpo_89-PEAS e Imp|273.210|6.381.284|3 mes|239|1,9888E-12|1,5448E-13|3,7981E-12|1,6464E-12|3,7494E-12|
|AREA|SRC_365|Cam_Valpo_90-PEAS e Imp|273.140|6.381.307|3 mes|292|1,6263E-12|1,2633E-13|3,1058E-12|1,3464E-12|3,066E-12|
|AREA|SRC_366|Cam_Valpo_91-PEAS e Imp|273.026|6.381.364|3 mes|511|9,2969E-13|7,2215E-14|1,7754E-12|7,6964E-13|1,7527E-12|
|AREA|SRC_367|Cam_Valpo_92-PEAS e Imp|272.787|6.381.471|3 mes|1.046|4,5363E-13|3,5237E-14|8,6631E-13|3,7554E-13|8,552E-13|
|AREA|SRC_368|Cam_Valpo_93-PEAS e Imp|272.625|6.381.553|3 mes|727|6,5314E-13|5,0734E-14|1,2473E-12|5,407E-13|1,2313E-12|
|AREA|SRC_369|Cam_Valpo_94-PEAS e Imp|272.586|6.381.587|3 mes|206|2,3059E-12|1,7911E-13|4,4036E-12|1,9089E-12|4,3471E-12|
|AREA|SRC_370|Cam_Valpo_95-PEAS e Imp|272.567|6.381.621|3 mes|150|3,1594E-12|2,4541E-13|6,0336E-12|2,6155E-12|5,9563E-12|
|AREA|SRC_371|Cam_Valpo_96-PEAS e Imp|272.558|6.381.659|3 mes|155|3,0708E-12|2,3853E-13|5,8644E-12|2,5422E-12|5,7892E-12|
|AREA|SRC_372|Cam_Valpo_97-PEAS e Imp|272.513|6.381.931|3 mes|1.103|4,303E-13|3,3425E-14|8,2176E-13|3,5623E-13|8,1122E-13|
|AREA|SRC_373|Cam_Valpo_98-PEAS e Imp|272.500|6.382.030|3 mes|398|1,1916E-12|9,2562E-14|2,2757E-12|9,8649E-13|2,2465E-12|
|AREA|SRC_374|Cam_Valpo_99-PEAS e Imp|272.492|6.382.086|3 mes|224|2,1204E-12|1,6471E-13|4,0494E-12|1,7554E-12|3,9975E-12|
|AREA|SRC_375|Cam_Valpo_100-PEAS e Imp|272.491|6.382.127|3 mes|164|2,889E-12|2,2441E-13|5,5172E-12|2,3917E-12|5,4465E-12|
|AREA|SRC_376|Cam_Valpo_101-PEAS e Imp|272.506|6.382.188|3 mes|247|1,9193E-12|1,4909E-13|3,6654E-12|1,5889E-12|3,6184E-12|
|AREA|SRC_377|Cam_Valpo_102-PEAS e Imp|272.660|6.383.439|3 mes|5.043|9,4127E-14|7,3114E-15|1,7976E-13|7,7923E-14|1,7745E-13|
|AREA|SRC_378|Cam_Valpo_103-PEAS e Imp|272.630|6.384.559|3 mes|4.479|1,0599E-13|8,2328E-15|2,0241E-13|8,7742E-14|1,9981E-13|
|AREA|SRC_379|Cam_Valpo_104-PEAS e Imp|272.626|6.385.227|3 mes|2.671|1,7772E-13|1,3805E-14|3,394E-13|1,4713E-13|3,3505E-13|
|AREA|SRC_380|Cam_Valpo_105-PEAS e Imp|272.602|6.386.454|3 mes|4.906|9,6765E-14|7,5164E-15|1,8479E-13|8,0107E-14|1,8242E-13|
|AREA|SRC_381|Cam_Valpo_106-PEAS e Imp|272.609|6.386.527|3 mes|293|1,6228E-12|1,2605E-13|3,0991E-12|1,3434E-12|3,0593E-12|
|AREA|SRC_382|Cam_Valpo_107-PEAS e Imp|272.650|6.386.615|3 mes|385|1,234E-12|9,5853E-14|2,3566E-12|1,0216E-12|2,3264E-12|
|AREA|SRC_383|Cam_Valpo_108-PEAS e Imp|272.755|6.386.705|3 mes|550|8,6311E-13|6,7043E-14|1,6483E-12|7,1453E-13|1,6272E-12|
|AREA|SRC_384|Cam_Valpo_109-PEAS e Imp|272.846|6.386.776|3 mes|461|1,0301E-12|8,0013E-14|1,9672E-12|8,5275E-13|1,9419E-12|
|AREA|SRC_385|Cam_Valpo_110-PEAS e Imp|272.918|6.386.821|3 mes|339|1,4012E-12|1,0884E-13|2,6759E-12|1,16E-12|2,6416E-12|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 17. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 10

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 28 de 56

|Tipo<br>AREA|ID<br>SRC_386|Descripción<br>Cam_Valpo_111-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_386|Descripción<br>Cam_Valpo_111-PEAS e Imp|[m]<br>272.959|[m]<br>6.386.856|[m]<br>6.386.856|[m2]<br>216|[g/m2s]<br>2,2007E-12|[g/m2s]<br>1,7095E-13|[g/m2s]<br>4,2028E-12|[g/m2s]<br>1,8219E-12|[g/m2s]<br>4,1489E-12|
|AREA|SRC_387|Cam_Valpo_112-PEAS e Imp|272.979|6.386.909|3 mes|229|2,07E-12|1,6079E-13|3,9532E-12|1,7137E-12|3,9025E-12|
|AREA|SRC_388|Cam_Valpo_113-PEAS e Imp|272.982|6.386.950|3 mes|168|2,8224E-12|2,1923E-13|5,39E-12|2,3365E-12|5,3208E-12|
|AREA|SRC_389|Cam_Valpo_114-PEAS e Imp|272.974|6.387.033|3 mes|335|1,4189E-12|1,1022E-13|2,7097E-12|1,1746E-12|2,675E-12|
|AREA|SRC_390|Cam_Valpo_115-PEAS e Imp|272.969|6.387.289|3 mes|1.021|4,6483E-13|3,6106E-14|8,8769E-13|3,8481E-13|8,7631E-13|
|AREA|SRC_391|Cam_Valpo_116-PEAS e Imp|272.950|6.387.316|3 mes|136|3,4941E-12|2,7141E-13|6,6728E-12|2,8926E-12|6,5873E-12|
|AREA|SRC_392|Cam_Valpo_117-PEAS e Imp|272.918|6.387.332|3 mes|151|3,1517E-12|2,4482E-13|6,0189E-12|2,6092E-12|5,9417E-12|
|AREA|SRC_393|Cam_Valpo_118-PEAS e Imp|272.871|6.387.328|3 mes|193|2,4582E-12|1,9095E-13|4,6945E-12|2,035E-12|4,6343E-12|
|AREA|SRC_394|Cam_Valpo_119-PEAS e Imp|272.818|6.387.319|3 mes|215|2,2098E-12|1,7165E-13|4,2201E-12|1,8294E-12|4,166E-12|
|AREA|SRC_395|Cam_Valpo_120-PEAS e Imp|272.669|6.387.324|3 mes|594|7,9983E-13|6,2128E-14|1,5275E-12|6,6214E-13|1,5079E-12|
|AREA|SRC_396|Cam_Valpo_121-PEAS e Imp|272.536|6.387.380|3 mes|574|8,2686E-13|6,4228E-14|1,5791E-12|6,8452E-13|1,5588E-12|
|AREA|SRC_397|Cam_Valpo_122-PEAS e Imp|272.406|6.387.475|3 mes|643|7,3845E-13|5,736E-14|1,4102E-12|6,1133E-13|1,3921E-12|
|AREA|SRC_398|Cam_Valpo_123-PEAS e Imp|272.321|6.387.544|3 mes|439|1,0817E-12|8,4022E-14|2,0657E-12|8,9548E-13|2,0392E-12|
|AREA|SRC_399|Cam_Valpo_124-PEAS e Imp|272.252|6.387.605|3 mes|366|1,297E-12|1,0074E-13|2,4769E-12|1,0737E-12|2,4451E-12|
|AREA|SRC_400|Cam_Valpo_125-PEAS e Imp|272.138|6.387.749|3 mes|734|6,4677E-13|5,0239E-14|1,2352E-12|5,3543E-13|1,2193E-12|
|AREA|SRC_401|Cam_Valpo_126-PEAS e Imp|272.059|6.387.890|3 mes|646|7,3518E-13|5,7107E-14|1,404E-12|6,0862E-13|1,386E-12|
|AREA|SRC_402|Cam_Valpo_127-PEAS e Imp|272.019|6.388.008|3 mes|494|9,6039E-13|7,46E-14|1,8341E-12|7,9506E-13|1,8106E-12|
|AREA|SRC_403|Cam_Valpo_128-PEAS e Imp|272.005|6.388.086|3 mes|318|1,492E-12|1,1589E-13|2,8493E-12|1,2352E-12|2,8128E-12|
|AREA|SRC_404|Cam_Valpo_129-PEAS e Imp|272.005|6.388.171|3 mes|338|1,4028E-12|1,0897E-13|2,679E-12|1,1613E-12|2,6447E-12|
|AREA|SRC_405|Cam_Valpo_130-PEAS e Imp|272.018|6.388.207|3 mes|149|3,1774E-12|2,4681E-13|6,068E-12|2,6304E-12|5,9902E-12|
|AREA|SRC_406|Cam_Valpo_131-PEAS e Imp|272.053|6.388.222|3 mes|145|3,2836E-12|2,5506E-13|6,2708E-12|2,7184E-12|6,1904E-12|
|AREA|SRC_407|Cam_Valpo_132-PEAS e Imp|272.113|6.388.260|3 mes|286|1,6587E-12|1,2884E-13|3,1677E-12|1,3732E-12|3,1271E-12|
|AREA|SRC_408|Cam_Valpo_133-PEAS e Imp|272.165|6.388.289|3 mes|237|2,0072E-12|1,5591E-13|3,8332E-12|1,6617E-12|3,7841E-12|
|AREA|SRC_409|Cam_Valpo_134-PEAS e Imp|272.170|6.388.313|3 mes|103|4,6072E-12|3,5787E-13|8,7985E-12|3,8141E-12|8,6856E-12|
|AREA|SRC_410|Cam_Valpo_135-PEAS e Imp|272.160|6.388.355|3 mes|179|2,6569E-12|2,0638E-13|5,0739E-12|2,1995E-12|5,0088E-12|
|AREA|SRC_411|Cam_Valpo_136-PEAS e Imp|272.116|6.388.384|3 mes|213|2,2269E-12|1,7298E-13|4,2528E-12|1,8436E-12|4,1983E-12|
|AREA|SRC_412|Cam_Valpo_137-PEAS e Imp|271.990|6.388.473|3 mes|618|7,6782E-13|5,9642E-14|1,4663E-12|6,3564E-13|1,4475E-12|
|AREA|SRC_413|Cam_Valpo_138-PEAS e Imp|271.909|6.388.570|3 mes|502|9,4518E-13|7,3418E-14|1,805E-12|7,8247E-13|1,7819E-12|
|AREA|SRC_414|Cam_Valpo_139-PEAS e Imp|271.887|6.388.631|3 mes|258|1,8423E-12|1,431E-13|3,5183E-12|1,5252E-12|3,4732E-12|
|AREA|SRC_415|Cam_Valpo_140-PEAS e Imp|271.869|6.388.710|3 mes|325|1,4626E-12|1,1361E-13|2,7932E-12|1,2108E-12|2,7573E-12|
|AREA|SRC_416|Cam_Valpo_141-PEAS e Imp|271.879|6.388.778|3 mes|271|1,7535E-12|1,3621E-13|3,3487E-12|1,4516E-12|3,3058E-12|
|AREA|SRC_417|Cam_Valpo_142-PEAS e Imp|271.889|6.388.831|3 mes|216|2,1997E-12|1,7086E-13|4,2008E-12|1,821E-12|4,1469E-12|
|AREA|SRC_418|Cam_Valpo_143-PEAS e Imp|271.888|6.388.910|3 mes|318|1,4949E-12|1,1612E-13|2,8549E-12|1,2376E-12|2,8183E-12|
|AREA|SRC_419|Cam_Valpo_144-PEAS e Imp|271.765|6.389.249|3 mes|1.444|3,2878E-13|2,5539E-14|6,2789E-13|2,7218E-13|6,1984E-13|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 18. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 11

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 29 de 56

|Tipo<br>AREA|ID<br>SRC_420|Descripción<br>Cam_Valpo_145-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_420|Descripción<br>Cam_Valpo_145-PEAS e Imp|[m]<br>271.745|[m]<br>6.389.323|[m]<br>6.389.323|[m2]<br>309|[g/m2s]<br>1,5379E-12|[g/m2s]<br>1,1946E-13|[g/m2s]<br>2,9369E-12|[g/m2s]<br>1,2731E-12|[g/m2s]<br>2,8993E-12|
|AREA|SRC_421|Cam_Valpo_146-PEAS e Imp|271.746|6.389.404|3 mes|321|1,4783E-12|1,1483E-13|2,8231E-12|1,2238E-12|2,7869E-12|
|AREA|SRC_422|Cam_Valpo_147-PEAS e Imp|271.745|6.389.713|3 mes|1.235|3,8428E-13|2,9849E-14|7,3386E-13|3,1812E-13|7,2445E-13|
|AREA|SRC_423|Cam_Valpo_148-PEAS e Imp|271.729|6.389.779|3 mes|275|1,7279E-12|1,3421E-13|3,2997E-12|1,4304E-12|3,2574E-12|
|AREA|SRC_424|Cam_Valpo_149-PEAS e Imp|271.405|6.390.771|3 mes|4.170|1,1385E-13|8,8433E-15|2,1742E-13|9,4249E-14|2,1463E-13|
|AREA|SRC_425|Cam_Valpo_150-PEAS e Imp|271.408|6.390.852|3 mes|324|1,4648E-12|1,1378E-13|2,7974E-12|1,2127E-12|2,7616E-12|
|AREA|SRC_426|Cam_Valpo_151-PEAS e Imp|271.425|6.390.918|3 mes|270|1,7598E-12|1,3669E-13|3,3607E-12|1,4568E-12|3,3176E-12|
|AREA|SRC_427|Cam_Valpo_152-PEAS e Imp|271.595|6.391.444|3 mes|2.210|2,1478E-13|1,6684E-14|4,1017E-13|1,7781E-13|4,0491E-13|
|AREA|SRC_428|Cam_Valpo_153-PEAS e Imp|271.601|6.391.518|3 mes|297|1,598E-12|1,2413E-13|3,0517E-12|1,3229E-12|3,0126E-12|
|AREA|SRC_429|Cam_Valpo_154-PEAS e Imp|271.583|6.391.599|3 mes|335|1,4189E-12|1,1022E-13|2,7098E-12|1,1747E-12|2,675E-12|
|AREA|SRC_430|Cam_Valpo_155-PEAS e Imp|271.490|6.391.665|3 mes|462|1,0269E-12|7,9764E-14|1,961E-12|8,501E-13|1,9359E-12|
|AREA|SRC_431|Cam_Valpo_156-PEAS e Imp|271.388|6.391.779|3 mes|610|7,7759E-13|6,0401E-14|1,485E-12|6,4373E-13|1,4659E-12|
|AREA|SRC_432|Cam_Valpo_157-PEAS e Imp|271.303|6.391.969|3 mes|830|5,7197E-13|4,4429E-14|1,0923E-12|4,7351E-13|1,0783E-12|
|AREA|SRC_433|Cam_Valpo_158-PEAS e Imp|271.249|6.392.048|3 mes|385|1,2315E-12|9,5658E-14|2,3518E-12|1,0195E-12|2,3217E-12|
|AREA|SRC_434|Cam_Valpo_159-PEAS e Imp|271.095|6.392.199|3 mes|863|5,5E-13|4,2722E-14|1,0503E-12|4,5532E-13|1,0369E-12|
|AREA|SRC_435|Cam_Valpo_160-PEAS e Imp|271.003|6.392.357|3 mes|727|6,526E-13|5,0692E-14|1,2463E-12|5,4026E-13|1,2303E-12|
|AREA|SRC_436|Cam_Valpo_161-PEAS e Imp|270.864|6.392.618|3 mes|1.182|4,0173E-13|3,1205E-14|7,6719E-13|3,3257E-13|7,5735E-13|
|AREA|SRC_437|Cam_Valpo_162-PEAS e Imp|270.665|6.392.901|3 mes|1.387|3,4234E-13|2,6592E-14|6,5377E-13|2,834E-13|6,4539E-13|
|AREA|SRC_438|Cam_Valpo_163-PEAS e Imp|270.570|6.393.060|3 mes|740|6,4167E-13|4,9843E-14|1,2254E-12|5,3121E-13|1,2097E-12|
|AREA|SRC_439|Cam_Valpo_164-PEAS e Imp|270.535|6.393.162|3 mes|428|1,1093E-12|8,6166E-14|2,1185E-12|9,1833E-13|2,0913E-12|
|AREA|SRC_440|Cam_Valpo_165-PEAS e Imp|270.408|6.393.157|3 mes|516|9,197E-13|7,1439E-14|1,7564E-12|7,6137E-13|1,7338E-12|
|AREA|SRC_441|Cam_Valpo_166-PEAS e Imp|270.322|6.393.156|3 mes|344|1,3795E-12|1,0716E-13|2,6345E-12|1,142E-12|2,6007E-12|
|AREA|SRC_442|Cam_Valpo_167-PEAS e Imp|270.198|6.393.225|3 mes|562|8,4464E-13|6,5608E-14|1,613E-12|6,9923E-13|1,5923E-12|
|AREA|SRC_443|Cam_Valpo_168-PEAS e Imp|270.084|6.393.222|3 mes|462|1,0285E-12|7,9887E-14|1,9641E-12|8,5141E-13|1,9389E-12|
|AREA|SRC_444|Cam_Valpo_169-PEAS e Imp|270.014|6.393.114|3 mes|520|9,1282E-13|7,0905E-14|1,7432E-12|7,5568E-13|1,7209E-12|
|AREA|SRC_445|Cam_Valpo_170-PEAS e Imp|269.944|6.393.026|3 mes|448|1,0592E-12|8,2273E-14|2,0227E-12|8,7684E-13|1,9968E-12|
|AREA|SRC_446|Cam_Valpo_171-PEAS e Imp|269.831|6.392.981|3 mes|484|9,8009E-13|7,613E-14|1,8717E-12|8,1137E-13|1,8477E-12|
|AREA|SRC_447|Cam_Valpo_172-PEAS e Imp|269.702|6.392.966|3 mes|517|9,1822E-13|7,1324E-14|1,7535E-12|7,6015E-13|1,7311E-12|
|AREA|SRC_448|Cam_Valpo_173-PEAS e Imp|269.506|6.393.084|3 mes|907|5,2354E-13|4,0667E-14|9,9982E-13|4,3341E-13|9,87E-13|
|AREA|SRC_449|Cam_Valpo_174-PEAS e Imp|269.407|6.393.106|3 mes|411|1,1561E-12|8,9802E-14|2,2078E-12|9,5707E-13|2,1795E-12|
|AREA|SRC_450|Cam_Valpo_175-PEAS e Imp|269.355|6.393.219|3 mes|493|9,6265E-13|7,4776E-14|1,8384E-12|7,9693E-13|1,8148E-12|
|AREA|SRC_451|Cam_Valpo_176-PEAS e Imp|269.450|6.393.436|3 mes|940|5,0524E-13|3,9245E-14|9,6487E-13|4,1826E-13|9,525E-13|
|AREA|SRC_452|Cam_Valpo_177-PEAS e Imp|269.537|6.393.768|3 mes|1.375|3,4512E-13|2,6808E-14|6,5908E-13|2,8571E-13|6,5063E-13|
|AREA|SRC_453|Cam_Valpo_178-PEAS e Imp|269.541|6.393.876|3 mes|433|1,0959E-12|8,5128E-14|2,0929E-12|9,0726E-13|2,0661E-12|
|AREA|SRC_454|Cam_Valpo_179-PEAS e Imp|269.514|6.393.952|3 mes|327|1,4495E-12|1,1259E-13|2,7682E-12|1,2E-12|2,7327E-12|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 19. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 30 de 56

|Tipo<br>AREA|ID<br>SRC_455|Descripción<br>Cam_Valpo_180-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_455|Descripción<br>Cam_Valpo_180-PEAS e Imp|[m]<br>269.461|[m]<br>6.394.006|[m]<br>6.394.006|[m2]<br>302|[g/m2s]<br>1,5718E-12|[g/m2s]<br>1,2209E-13|[g/m2s]<br>3,0016E-12|[g/m2s]<br>1,3012E-12|[g/m2s]<br>2,9631E-12|
|AREA|SRC_456|Cam_Valpo_181-PEAS e Imp|269.456|6.394.087|3 mes|318|1,495E-12|1,1613E-13|2,855E-12|1,2376E-12|2,8184E-12|
|AREA|SRC_457|Cam_Valpo_182-PEAS e Imp|269.494|6.394.169|3 mes|359|1,3225E-12|1,0273E-13|2,5257E-12|1,0949E-12|2,4933E-12|
|AREA|SRC_458|Cam_Valpo_183-PEAS e Imp|269.580|6.394.296|3 mes|612|7,7568E-13|6,0253E-14|1,4813E-12|6,4215E-13|1,4623E-12|
|AREA|SRC_459|Cam_Valpo_184-PEAS e Imp|269.614|6.394.394|3 mes|417|1,1395E-12|8,851E-14|2,1761E-12|9,4331E-13|2,1482E-12|
|AREA|SRC_460|Cam_Valpo_185-PEAS e Imp|269.617|6.394.492|3 mes|397|1,1971E-12|9,2983E-14|2,286E-12|9,9098E-13|2,2567E-12|
|AREA|SRC_461|Cam_Valpo_186-PEAS e Imp|269.532|6.394.634|3 mes|664|7,1473E-13|5,5518E-14|1,3649E-12|5,9169E-13|1,3474E-12|
|AREA|SRC_462|Cam_Valpo_187-PEAS e Imp|269.478|6.394.752|3 mes|518|9,1608E-13|7,1158E-14|1,7495E-12|7,5838E-13|1,727E-12|
|AREA|SRC_463|Cam_Valpo_188-PEAS e Imp|269.437|6.394.881|3 mes|541|8,7758E-13|6,8167E-14|1,6759E-12|7,265E-13|1,6544E-12|
|AREA|SRC_464|Cam_Valpo_189-PEAS e Imp|269.448|6.395.002|3 mes|483|9,8191E-13|7,6271E-14|1,8752E-12|8,1287E-13|1,8511E-12|
|AREA|SRC_465|Cam_Valpo_190-PEAS e Imp|269.465|6.395.049|3 mes|198|2,3997E-12|1,864E-13|4,5828E-12|1,9866E-12|4,524E-12|
|AREA|SRC_466|Cam_Valpo_191-PEAS e Imp|269.701|6.395.188|3 mes|1.089|4,3605E-13|3,3871E-14|8,3274E-13|3,6098E-13|8,2206E-13|
|AREA|SRC_467|Cam_Valpo_192-PEAS e Imp|269.737|6.395.244|3 mes|269|1,7623E-12|1,3689E-13|3,3654E-12|1,4589E-12|3,3223E-12|
|AREA|SRC_468|Cam_Valpo_193-PEAS e Imp|269.748|6.395.318|3 mes|302|1,5725E-12|1,2215E-13|3,003E-12|1,3018E-12|2,9645E-12|
|AREA|SRC_469|Cam_Valpo_194-PEAS e Imp|269.734|6.395.473|3 mes|624|7,6073E-13|5,9091E-14|1,4528E-12|6,2978E-13|1,4342E-12|
|AREA|SRC_470|Cam_Valpo_195-PEAS e Imp|269.791|6.395.575|3 mes|463|1,0255E-12|7,9657E-14|1,9584E-12|8,4896E-13|1,9333E-12|
|AREA|SRC_471|Cam_Valpo_196-PEAS e Imp|269.918|6.395.634|3 mes|558|8,5139E-13|6,6133E-14|1,6259E-12|7,0482E-13|1,6051E-12|
|AREA|SRC_472|Cam_Valpo_197-PEAS e Imp|269.951|6.395.703|3 mes|312|1,5232E-12|1,1831E-13|2,9088E-12|1,261E-12|2,8715E-12|
|AREA|SRC_473|Cam_Valpo_198-PEAS e Imp|269.926|6.395.767|3 mes|278|1,7084E-12|1,327E-13|3,2625E-12|1,4143E-12|3,2207E-12|
|AREA|SRC_474|Cam_Valpo_199-PEAS e Imp|269.853|6.395.812|3 mes|348|1,363E-12|1,0587E-13|2,603E-12|1,1284E-12|2,5696E-12|
|AREA|SRC_475|Cam_Valpo_200-PEAS e Imp|269.732|6.395.847|3 mes|505|9,4063E-13|7,3065E-14|1,7964E-12|7,787E-13|1,7733E-12|
|AREA|SRC_476|Cam_Valpo_201-PEAS e Imp|269.688|6.395.928|3 mes|365|1,2989E-12|1,009E-13|2,4806E-12|1,0753E-12|2,4488E-12|
|AREA|SRC_477|Cam_Valpo_202-PEAS e Imp|269.717|6.396.047|3 mes|485|9,7943E-13|7,6079E-14|1,8704E-12|8,1082E-13|1,8465E-12|
|AREA|SRC_478|Cam_Valpo_203-PEAS e Imp|269.712|6.396.106|3 mes|237|1,9989E-12|1,5527E-13|3,8173E-12|1,6548E-12|3,7683E-12|
|AREA|SRC_479|Cam_Valpo_204-PEAS e Imp|269.657|6.396.143|3 mes|271|1,7486E-12|1,3583E-13|3,3394E-12|1,4476E-12|3,2965E-12|
|AREA|SRC_480|Cam_Valpo_205-PEAS e Imp|269.580|6.396.120|3 mes|326|1,4541E-12|1,1295E-13|2,7769E-12|1,2038E-12|2,7413E-12|
|AREA|SRC_481|Cam_Valpo_206-PEAS e Imp|269.501|6.396.070|3 mes|376|1,2619E-12|9,8018E-14|2,4098E-12|1,0446E-12|2,3789E-12|
|AREA|SRC_482|Cam_Valpo_207-PEAS e Imp|269.359|6.396.026|3 mes|594|7,998E-13|6,2126E-14|1,5274E-12|6,6211E-13|1,5078E-12|
|AREA|SRC_483|Cam_Valpo_208-PEAS e Imp|269.272|6.396.023|3 mes|343|1,3821E-12|1,0735E-13|2,6393E-12|1,1441E-12|2,6055E-12|
|AREA|SRC_484|Cam_Valpo_209-PEAS e Imp|269.222|6.396.073|3 mes|276|1,7212E-12|1,337E-13|3,287E-12|1,4249E-12|3,2448E-12|
|AREA|SRC_485|Cam_Valpo_210-PEAS e Imp|269.210|6.396.185|3 mes|446|1,0638E-12|8,2631E-14|2,0315E-12|8,8065E-13|2,0055E-12|
|AREA|SRC_486|Cam_Valpo_211-PEAS e Imp|269.167|6.396.232|3 mes|255|1,8583E-12|1,4434E-13|3,5488E-12|1,5384E-12|3,5033E-12|
|AREA|SRC_487|Cam_Valpo_212-PEAS e Imp|269.082|6.396.226|3 mes|350|1,3579E-12|1,0548E-13|2,5933E-12|1,1242E-12|2,56E-12|
|AREA|SRC_488|Cam_Valpo_213-PEAS e Imp|268.998|6.396.240|3 mes|336|1,4148E-12|1,0989E-13|2,7018E-12|1,1712E-12|2,6672E-12|
|AREA|SRC_489|Cam_Valpo_214-PEAS e Imp|268.894|6.396.300|3 mes|480|9,888E-13|7,6806E-14|1,8883E-12|8,1858E-13|1,8641E-12|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 20. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 13

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 31 de 56

|Tipo<br>AREA|ID<br>SRC_490|Descripción<br>Cam_Valpo_215-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_490|Descripción<br>Cam_Valpo_215-PEAS e Imp|[m]<br>268.805|[m]<br>6.396.381|[m]<br>6.396.381|[m2]<br>477|[g/m2s]<br>9,9419E-13|[g/m2s]<br>7,7225E-14|[g/m2s]<br>1,8986E-12|[g/m2s]<br>8,2304E-13|[g/m2s]<br>1,8743E-12|
|AREA|SRC_491|Cam_Valpo_216-PEAS e Imp|268.734|6.396.481|3 mes|489|9,7011E-13|7,5355E-14|1,8526E-12|8,0311E-13|1,8289E-12|
|AREA|SRC_492|Cam_Valpo_217-PEAS e Imp|268.692|6.396.569|3 mes|388|1,2225E-12|9,4958E-14|2,3346E-12|1,012E-12|2,3046E-12|
|AREA|SRC_493|Cam_Valpo_218-PEAS e Imp|268.614|6.396.686|3 mes|564|8,4216E-13|6,5416E-14|1,6083E-12|6,9718E-13|1,5877E-12|
|AREA|SRC_494|Cam_Valpo_219-PEAS e Imp|268.551|6.396.751|3 mes|365|1,3001E-12|1,0099E-13|2,4829E-12|1,0763E-12|2,451E-12|
|AREA|SRC_495|Cam_Valpo_220-PEAS e Imp|268.525|6.396.834|3 mes|343|1,385E-12|1,0758E-13|2,645E-12|1,1466E-12|2,6111E-12|
|AREA|SRC_496|Cam_Valpo_221-PEAS e Imp|268.521|6.396.918|3 mes|335|1,4162E-12|1,1001E-13|2,7046E-12|1,1724E-12|2,6699E-12|
|AREA|SRC_497|Cam_Valpo_222-PEAS e Imp|268.510|6.396.996|3 mes|312|1,5207E-12|1,1812E-13|2,9041E-12|1,2589E-12|2,8668E-12|
|AREA|SRC_498|Cam_Valpo_223-PEAS e Imp|268.441|6.397.095|3 mes|487|9,752E-13|7,575E-14|1,8624E-12|8,0732E-13|1,8385E-12|
|AREA|SRC_499|Cam_Valpo_224-PEAS e Imp|268.352|6.397.195|3 mes|538|8,8267E-13|6,8563E-14|1,6857E-12|7,3072E-13|1,664E-12|
|AREA|SRC_500|Cam_Valpo_225-PEAS e Imp|268.295|6.397.296|3 mes|460|1,0311E-12|8,009E-14|1,9691E-12|8,5357E-13|1,9438E-12|
|AREA|SRC_501|Cam_Valpo_226-PEAS e Imp|268.265|6.397.370|3 mes|319|1,4881E-12|1,1559E-13|2,8419E-12|1,2319E-12|2,8054E-12|
|AREA|SRC_502|Cam_Valpo_227-PEAS e Imp|268.236|6.397.470|3 mes|415|1,1452E-12|8,8957E-14|2,1871E-12|9,4807E-13|2,159E-12|
|AREA|SRC_503|Cam_Valpo_228-PEAS e Imp|268.225|6.397.539|3 mes|278|1,7075E-12|1,3263E-13|3,2608E-12|1,4135E-12|3,219E-12|
|AREA|SRC_504|Cam_Valpo_229-PEAS e Imp|268.212|6.397.650|3 mes|446|1,0633E-12|8,259E-14|2,0305E-12|8,8022E-13|2,0045E-12|
|AREA|SRC_505|Cam_Valpo_230-PEAS e Imp|268.292|6.397.691|3 mes|353|1,3452E-12|1,0449E-13|2,5689E-12|1,1136E-12|2,5359E-12|
|AREA|SRC_506|Cam_Valpo_231-PEAS e Imp|268.324|6.397.741|3 mes|244|1,9448E-12|1,5106E-13|3,714E-12|1,61E-12|3,6664E-12|
|AREA|SRC_507|Cam_Valpo_232-PEAS e Imp|268.344|6.397.809|3 mes|285|1,6685E-12|1,296E-13|3,1863E-12|1,3812E-12|3,1454E-12|
|AREA|SRC_508|Cam_Valpo_233-PEAS e Imp|268.317|6.397.871|3 mes|277|1,7113E-12|1,3293E-13|3,268E-12|1,4167E-12|3,2261E-12|
|AREA|SRC_509|Cam_Valpo_234-PEAS e Imp|268.289|6.397.931|3 mes|263|1,8019E-12|1,3997E-13|3,4412E-12|1,4917E-12|3,3971E-12|
|AREA|SRC_510|Cam_Valpo_235-PEAS e Imp|268.281|6.397.993|3 mes|246|1,9281E-12|1,4977E-13|3,6821E-12|1,5962E-12|3,6349E-12|
|AREA|SRC_511|Cam_Valpo_236-PEAS e Imp|268.325|6.398.057|3 mes|307|1,5457E-12|1,2007E-13|2,9519E-12|1,2796E-12|2,914E-12|
|AREA|SRC_512|Cam_Valpo_237-PEAS e Imp|268.339|6.398.092|3 mes|154|3,0802E-12|2,3926E-13|5,8824E-12|2,55E-12|5,807E-12|
|AREA|SRC_513|Cam_Valpo_238-PEAS e Imp|268.362|6.398.151|3 mes|252|1,8871E-12|1,4658E-13|3,6038E-12|1,5622E-12|3,5576E-12|
|AREA|SRC_514|Cam_Valpo_239-PEAS e Imp|268.383|6.398.192|3 mes|185|2,5634E-12|1,9912E-13|4,8954E-12|2,1221E-12|4,8326E-12|
|AREA|SRC_515|Cam_Valpo_240-PEAS e Imp|268.355|6.398.247|3 mes|250|1,8975E-12|1,4739E-13|3,6237E-12|1,5709E-12|3,5773E-12|
|AREA|SRC_516|Cam_Valpo_241-PEAS e Imp|268.227|6.398.303|3 mes|567|8,3746E-13|6,5051E-14|1,5993E-12|6,9329E-13|1,5788E-12|
|AREA|SRC_517|Cam_Valpo_242-PEAS e Imp|268.140|6.398.362|3 mes|419|1,1334E-12|8,804E-14|2,1645E-12|9,383E-13|2,1367E-12|
|AREA|SRC_518|Cam_Valpo_243-PEAS e Imp|268.089|6.398.427|3 mes|325|1,4587E-12|1,1331E-13|2,7858E-12|1,2076E-12|2,75E-12|
|AREA|SRC_519|Cam_Valpo_244-PEAS e Imp|268.005|6.398.483|3 mes|406|1,1688E-12|9,0788E-14|2,2321E-12|9,6759E-13|2,2035E-12|
|AREA|SRC_520|Cam_Valpo_245-PEAS e Imp|267.956|6.398.553|3 mes|338|1,4034E-12|1,0901E-13|2,6801E-12|1,1618E-12|2,6457E-12|
|AREA|SRC_521|Cam_Valpo_246-PEAS e Imp|267.920|6.398.673|3 mes|499|9,5141E-13|7,3902E-14|1,8169E-12|7,8762E-13|1,7936E-12|
|AREA|SRC_522|Cam_Valpo_247-PEAS e Imp|267.908|6.398.749|3 mes|308|1,5394E-12|1,1958E-13|2,9399E-12|1,2744E-12|2,9022E-12|
|AREA|SRC_523|Cam_Valpo_248-PEAS e Imp|267.894|6.398.771|3 mes|107|4,4196E-12|3,433E-13|8,4403E-12|3,6588E-12|8,3321E-12|
|AREA|SRC_524|Cam_Valpo_249-PEAS e Imp|267.791|6.398.823|3 mes|467|1,0175E-12|7,9034E-14|1,9431E-12|8,4232E-13|1,9182E-12|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 21. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 14

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 32 de 56

|Tipo<br>AREA|ID<br>SRC_525|Descripción<br>Cam_Valpo_250-PEAS e Imp|X1|Y1|Ciclo<br>operación<br>3 mes|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_525|Descripción<br>Cam_Valpo_250-PEAS e Imp|[m]<br>267.747|[m]<br>6.398.849|[m]<br>6.398.849|[m2]<br>204|[g/m2s]<br>2,327E-12|[g/m2s]<br>1,8075E-13|[g/m2s]<br>4,4439E-12|[g/m2s]<br>1,9264E-12|[g/m2s]<br>4,3869E-12|
|AREA|SRC_526|Cam_Valpo_251-PEAS e Imp|267.699|6.398.875|3 mes|217|2,1861E-12|1,6981E-13|4,1749E-12|1,8098E-12|4,1213E-12|
|AREA|SRC_527|Cam_Valpo_252-PEAS e Imp|267.673|6.398.943|3 mes|286|1,6603E-12|1,2897E-13|3,1708E-12|1,3745E-12|3,1301E-12|
|AREA|SRC_528|Cam_Valpo_253-PEAS e Imp|267.740|6.399.152|3 mes|872|5,444E-13|4,2287E-14|1,0397E-12|4,5068E-13|1,0263E-12|
|AREA|SRC_529|Cam_Valpo_254-PEAS e Imp|267.754|6.399.259|3 mes|434|1,0929E-12|8,489E-14|2,0871E-12|9,0473E-13|2,0603E-12|
|AREA|SRC_530|Cam_Valpo_255-PEAS e Imp|267.756|6.399.372|3 mes|453|1,0481E-12|8,1411E-14|2,0015E-12|8,6765E-13|1,9759E-12|
|AREA|SRC_531|Cam_Valpo_256-PEAS e Imp|267.702|6.399.478|3 mes|480|9,8891E-13|7,6815E-14|1,8885E-12|8,1867E-13|1,8643E-12|
|AREA|SRC_532|Cam_Valpo_257-PEAS e Imp|267.740|6.399.547|3 mes|307|1,5452E-12|1,2003E-13|2,9509E-12|1,2792E-12|2,9131E-12|
|AREA|SRC_533|Cam_Valpo_258-PEAS e Imp|267.742|6.399.624|3 mes|312|1,5237E-12|1,1835E-13|2,9098E-12|1,2614E-12|2,8725E-12|
|AREA|SRC_534|Cam_Valpo_259-PEAS e Imp|267.731|6.399.695|3 mes|288|1,6507E-12|1,2822E-13|3,1524E-12|1,3665E-12|3,1119E-12|
|AREA|SRC_535|Cam_Valpo_260-PEAS e Imp|267.682|6.399.788|3 mes|426|1,1151E-12|8,662E-14|2,1296E-12|9,2317E-13|2,1023E-12|
|AREA|SRC_536|Cam_Valpo_261-PEAS e Imp|267.661|6.399.830|3 mes|187|2,5381E-12|1,9715E-13|4,847E-12|2,1011E-12|4,7848E-12|
|AREA|SRC_540|Cam_Cat_1-PTAS|273.043|6.387.323|10 meses|383|3,328E-14|2,5851E-15|6,3555E-14|2,7551E-14|6,274E-14|
|AREA|SRC_541|Cam_Cat_2-PTAS|273.206|6.387.558|10 meses|1.145|1,1141E-14|8,6541E-16|2,1277E-14|9,2232E-15|2,1004E-14|
|AREA|SRC_542|Cam_Cat_3-PTAS|273.308|6.387.612|10 meses|456|2,7976E-14|2,1731E-15|5,3426E-14|2,316E-14|5,2741E-14|
|AREA|SRC_543|Cam_Cat_4-PTAS|273.511|6.387.668|10 meses|844|1,5122E-14|1,1747E-15|2,888E-14|1,2519E-14|2,8509E-14|
|AREA|SRC_544|Cam_Cat_5-PTAS|273.721|6.387.707|10 meses|853|1,495E-14|1,1612E-15|2,855E-14|1,2376E-14|2,8184E-14|
|AREA|SRC_545|Cam_Cat_6-PTAS|273.880|6.387.880|10 meses|945|1,3496E-14|1,0483E-15|2,5773E-14|1,1172E-14|2,5443E-14|
|AREA|SRC_546|Cam_Cat_7-PTAS|273.982|6.387.934|10 meses|458|2,7883E-14|2,1658E-15|5,3248E-14|2,3083E-14|5,2566E-14|
|AREA|SRC_547|Cam_Cat_8-PTAS|274.178|6.387.916|10 meses|782|1,6309E-14|1,2668E-15|3,1146E-14|1,3502E-14|3,0747E-14|
|AREA|SRC_548|Cam_Cat_9-PTAS|274.216|6.387.945|10 meses|195|6,526E-14|5,0692E-15|1,2463E-13|5,4025E-14|1,2303E-13|
|AREA|SRC_549|Cam_Cat_10-PTAS|274.213|6.388.017|10 meses|296|4,3155E-14|3,3522E-15|8,2415E-14|3,5726E-14|8,1358E-14|
|AREA|SRC_550|Cam_Cat_11-PTAS|274.177|6.388.250|10 meses|942|1,3549E-14|1,0525E-15|2,5875E-14|1,1217E-14|2,5543E-14|
|AREA|SRC_551|Cam_Cat_12-PTAS|274.185|6.388.365|10 meses|458|2,7833E-14|2,162E-15|5,3153E-14|2,3042E-14|5,2472E-14|
|AREA|SRC_552|Cam_Cat_13-PTAS|274.352|6.388.558|10 meses|1.017|1,2545E-14|9,7442E-16|2,3957E-14|1,0385E-14|2,365E-14|
|AREA|SRC_553|Cam_Cat_14-PTAS|274.654|6.388.846|10 meses|1.667|7,6526E-15|5,9443E-16|1,4614E-14|6,3353E-15|1,4427E-14|
|AREA|SRC_554|Cam_Cat_15-PTAS|274.745|6.388.895|10 meses|410|3,1129E-14|2,418E-15|5,9448E-14|2,577E-14|5,8686E-14|
|AREA|SRC_555|Cam_Cat_16-PTAS|274.834|6.388.862|10 meses|371|3,4375E-14|2,6701E-15|6,5646E-14|2,8457E-14|6,4804E-14|
|AREA|SRC_556|Cam_Cat_17-PTAS|274.882|6.388.794|10 meses|331|3,8507E-14|2,9911E-15|7,3538E-14|3,1878E-14|7,2594E-14|
|AREA|SRC_557|Cam_Cat_18-PTAS|274.979|6.388.768|10 meses|407|3,1372E-14|2,4369E-15|5,9912E-14|2,5971E-14|5,9144E-14|
|AREA|SRC_558|Cam_Cat_19-PTAS|275.069|6.388.799|10 meses|384|3,3207E-14|2,5794E-15|6,3417E-14|2,7491E-14|6,2603E-14|
|AREA|SRC_559|Cam_Cat_20-PTAS|275.059|6.388.911|10 meses|460|2,7762E-14|2,1564E-15|5,3017E-14|2,2983E-14|5,2337E-14|
|AREA|SRC_560|Cam_Cat_21-PTAS|275.040|6.389.003|10 meses|374|3,4105E-14|2,6492E-15|6,5131E-14|2,8234E-14|6,4296E-14|
|AREA|SRC_561|Cam_Cat_22-PTAS|274.958|6.389.092|10 meses|489|2,6082E-14|2,026E-15|4,981E-14|2,1592E-14|4,9171E-14|
|AREA|SRC_562|Cam_Cat_23-PTAS|274.915|6.389.184|10 meses|402|3,1718E-14|2,4637E-15|6,0572E-14|2,6258E-14|5,9795E-14|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 22. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 15

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 33 de 56

|Tipo<br>AREA|ID<br>SRC_563|Descripción<br>Cam_Cat_24-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_563|Descripción<br>Cam_Cat_24-PTAS|[m]<br>274.946|[m]<br>6.389.307|[m]<br>6.389.307|[m2]<br>503|[g/m2s]<br>2,5372E-14|[g/m2s]<br>1,9708E-15|[g/m2s]<br>4,8454E-14|[g/m2s]<br>2,1005E-14|[g/m2s]<br>4,7833E-14|
|AREA|SRC_564|Cam_Cat_25-PTAS|275.049|6.389.374|10 meses|485|2,63E-14|2,0429E-15|5,0226E-14|2,1772E-14|4,9581E-14|
|AREA|SRC_565|Cam_Cat_26-PTAS|275.181|6.389.406|10 meses|541|2,3564E-14|1,8304E-15|4,5002E-14|1,9508E-14|4,4424E-14|
|AREA|SRC_566|Cam_Cat_27-PTAS|275.286|6.389.385|10 meses|424|3,0063E-14|2,3352E-15|5,7412E-14|2,4887E-14|5,6675E-14|
|AREA|SRC_567|Cam_Cat_28-PTAS|275.372|6.389.387|10 meses|345|3,697E-14|2,8717E-15|7,0603E-14|3,0606E-14|6,9697E-14|
|AREA|SRC_568|Cam_Cat_29-PTAS|275.519|6.389.442|10 meses|633|2,0145E-14|1,5648E-15|3,8471E-14|1,6677E-14|3,7978E-14|
|AREA|SRC_569|Cam_Cat_30-PTAS|275.575|6.389.512|10 meses|360|3,54E-14|2,7498E-15|6,7605E-14|2,9306E-14|6,6738E-14|
|AREA|SRC_570|Cam_Cat_31-PTAS|275.579|6.389.623|10 meses|447|2,8519E-14|2,2153E-15|5,4464E-14|2,361E-14|5,3766E-14|
|AREA|SRC_571|Cam_Cat_32-PTAS|275.473|6.389.738|10 meses|630|2,0262E-14|1,5739E-15|3,8695E-14|1,6774E-14|3,8199E-14|
|AREA|SRC_572|Cam_Cat_33-PTAS|275.397|6.389.809|10 meses|419|3,0433E-14|2,3639E-15|5,8119E-14|2,5194E-14|5,7374E-14|
|AREA|SRC_573|Cam_Cat_34-PTAS|275.382|6.389.918|10 meses|433|2,9477E-14|2,2896E-15|5,6292E-14|2,4402E-14|5,557E-14|
|AREA|SRC_574|Cam_Cat_35-PTAS|275.487|6.390.018|10 meses|577|2,2122E-14|1,7184E-15|4,2248E-14|1,8314E-14|4,1706E-14|
|AREA|SRC_575|Cam_Cat_36-PTAS|275.630|6.390.045|10 meses|576|2,2134E-14|1,7193E-15|4,227E-14|1,8324E-14|4,1728E-14|
|AREA|SRC_576|Cam_Cat_37-PTAS|275.763|6.390.025|10 meses|533|2,3937E-14|1,8593E-15|4,5713E-14|1,9816E-14|4,5126E-14|
|AREA|SRC_577|Cam_Cat_38-PTAS|275.861|6.389.993|10 meses|412|3,0985E-14|2,4068E-15|5,9173E-14|2,5651E-14|5,8414E-14|
|AREA|SRC_578|Cam_Cat_39-PTAS|276.044|6.389.963|10 meses|743|1,7172E-14|1,3339E-15|3,2795E-14|1,4216E-14|3,2374E-14|
|AREA|SRC_579|Cam_Cat_40-PTAS|276.114|6.389.925|10 meses|317|4,0248E-14|3,1263E-15|7,6863E-14|3,3319E-14|7,5877E-14|
|AREA|SRC_580|Cam_Cat_41-PTAS|276.133|6.389.885|10 meses|173|7,3768E-14|5,7301E-15|1,4088E-13|6,1069E-14|1,3907E-13|
|AREA|SRC_581|Cam_Cat_42-PTAS|276.158|6.389.818|10 meses|287|4,4473E-14|3,4545E-15|8,4932E-14|3,6817E-14|8,3843E-14|
|AREA|SRC_582|Cam_Cat_43-PTAS|276.157|6.389.659|10 meses|633|2,0158E-14|1,5658E-15|3,8496E-14|1,6688E-14|3,8003E-14|
|AREA|SRC_583|Cam_Cat_44-PTAS|276.172|6.389.529|10 meses|521|2,4481E-14|1,9016E-15|4,6752E-14|2,0267E-14|4,6152E-14|
|AREA|SRC_584|Cam_Cat_45-PTAS|276.275|6.389.477|10 meses|468|2,724E-14|2,1159E-15|5,202E-14|2,255E-14|5,1353E-14|
|AREA|SRC_585|Cam_Cat_46-PTAS|276.411|6.389.458|10 meses|553|2,3053E-14|1,7907E-15|4,4025E-14|1,9085E-14|4,3461E-14|
|AREA|SRC_586|Cam_Cat_47-PTAS|276.501|6.389.471|10 meses|366|3,4832E-14|2,7056E-15|6,652E-14|2,8836E-14|6,5667E-14|
|AREA|SRC_587|Cam_Cat_48-PTAS|276.706|6.389.673|10 meses|1.151|1,1079E-14|8,6058E-16|2,1158E-14|9,1717E-15|2,0886E-14|
|AREA|SRC_588|Cam_Cat_49-PTAS|277.353|6.390.498|10 meses|4.195|3,0407E-15|2,3619E-16|5,8069E-15|2,5172E-15|5,7324E-15|
|AREA|SRC_589|Cam_Cat_50-PTAS|277.494|6.390.575|10 meses|640|1,9932E-14|1,5482E-15|3,8064E-14|1,65E-14|3,7576E-14|
|AREA|SRC_590|Cam_Cat_51-PTAS|279.440|6.391.244|10 meses|8.224|1,5512E-15|1,205E-16|2,9625E-15|1,2842E-15|2,9245E-15|
|AREA|SRC_591|Cam_Cat_52-PTAS|283.346|6.393.239|10 meses|17.541|7,2727E-16|5,6492E-17|1,3889E-15|6,0207E-16|1,3711E-15|
|AREA|SRC_592|Cam_Cat_53-PTAS|287.745|6.394.661|10 meses|18.483|6,9019E-16|5,3612E-17|1,3181E-15|5,7138E-16|1,3012E-15|
|AREA|SRC_593|Cam_Pta_1-PTAS|273.147|6.383.634|10 meses|1.866|7,2654E-15|2,6307E-16|1,0848E-14|5,1083E-15|1,0451E-14|
|AREA|SRC_594|Cam_Pta_2-PTAS|273.165|6.383.642|10 meses|81|1,6773E-13|6,0731E-15|2,5043E-13|1,1793E-13|2,4127E-13|
|AREA|SRC_595|Cam_Pta_3-PTAS|273.189|6.383.637|10 meses|94|1,4404E-13|5,2155E-15|2,1507E-13|1,0127E-13|2,072E-13|
|AREA|SRC_596|Cam_Pta_4-PTAS|273.241|6.383.562|10 meses|360|3,7673E-14|1,364E-15|5,6248E-14|2,6487E-14|5,419E-14|
|AREA|SRC_597|Cam_Pta_5-PTAS|273.289|6.383.445|10 meses|506|2,6822E-14|9,7117E-16|4,0048E-14|1,8858E-14|3,8582E-14|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 23. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 16

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 34 de 56

|Tipo<br>AREA|ID<br>SRC_598|Descripción<br>Cam_Pta_6-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_598|Descripción<br>Cam_Pta_6-PTAS|[m]<br>273.304|[m]<br>6.383.402|[m]<br>6.383.402|[m2]<br>180|[g/m2s]<br>7,5494E-14|[g/m2s]<br>2,7335E-15|[g/m2s]<br>1,1272E-13|[g/m2s]<br>5,3079E-14|[g/m2s]<br>1,0859E-13|
|AREA|SRC_599|Cam_Pta_7-PTAS|273.331|6.383.382|10 meses|138|9,7948E-14|3,5465E-15|1,4624E-13|6,8866E-14|1,4089E-13|
|AREA|SRC_600|Cam_Pta_8-PTAS|273.361|6.383.362|10 meses|146|9,3159E-14|3,3731E-15|1,3909E-13|6,5499E-14|1,34E-13|
|AREA|SRC_601|Cam_Pta_9-PTAS|273.393|6.383.346|10 meses|144|9,4177E-14|3,41E-15|1,4061E-13|6,6215E-14|1,3547E-13|
|AREA|SRC_602|Cam_Pta_10-PTAS|273.413|6.383.324|10 meses|116|1,1658E-13|4,2212E-15|1,7407E-13|8,1968E-14|1,677E-13|
|AREA|SRC_603|Cam_Pta_11-PTAS|273.447|6.383.229|10 meses|400|3,3898E-14|1,2274E-15|5,0613E-14|2,3834E-14|4,8761E-14|
|AREA|SRC_604|Cam_Pta_12-PTAS|273.463|6.383.220|10 meses|80|1,6924E-13|6,1277E-15|2,5268E-13|1,1899E-13|2,4344E-13|
|AREA|SRC_605|Cam_Pta_13-PTAS|273.473|6.383.218|10 meses|45|3,0051E-13|1,0881E-14|4,4869E-13|2,1129E-13|4,3227E-13|
|AREA|SRC_606|Cam_Pta_14-PTAS|273.519|6.383.228|10 meses|189|7,1927E-14|2,6043E-15|1,0739E-13|5,0572E-14|1,0346E-13|
|AREA|SRC_607|Cam_Valpo_1-PTAS|267.407|6.370.003|10 meses|9.182|1,3894E-15|1,0792E-16|2,6533E-15|1,1502E-15|2,6193E-15|
|AREA|SRC_608|Cam_Valpo_2-PTAS|267.402|6.370.088|10 meses|338|3,771E-14|2,9292E-15|7,2016E-14|3,1218E-14|7,1092E-14|
|AREA|SRC_609|Cam_Valpo_3-PTAS|267.699|6.371.506|10 meses|5.789|2,2037E-15|1,7117E-16|4,2084E-15|1,8243E-15|4,1544E-15|
|AREA|SRC_610|Cam_Valpo_4-PTAS|267.700|6.371.619|10 meses|452|2,8223E-14|2,1923E-15|5,3899E-14|2,3365E-14|5,3208E-14|
|AREA|SRC_611|Cam_Valpo_5-PTAS|267.517|6.371.917|10 meses|1.401|9,1027E-15|7,0707E-16|1,7384E-14|7,5357E-15|1,7161E-14|
|AREA|SRC_612|Cam_Valpo_6-PTAS|267.499|6.371.980|10 meses|261|4,8859E-14|3,7952E-15|9,3307E-14|4,0448E-14|9,2111E-14|
|AREA|SRC_613|Cam_Valpo_7-PTAS|267.496|6.372.042|10 meses|247|5,1642E-14|4,0114E-15|9,8622E-14|4,2752E-14|9,7357E-14|
|AREA|SRC_614|Cam_Valpo_8-PTAS|267.518|6.372.113|10 meses|294|4,3322E-14|3,3651E-15|8,2734E-14|3,5865E-14|8,1673E-14|
|AREA|SRC_615|Cam_Valpo_9-PTAS|267.547|6.372.151|10 meses|187|6,8062E-14|5,2868E-15|1,2998E-13|5,6345E-14|1,2831E-13|
|AREA|SRC_616|Cam_Valpo_10-PTAS|267.569|6.372.177|10 meses|137|9,3103E-14|7,2319E-15|1,778E-13|7,7075E-14|1,7552E-13|
|AREA|SRC_617|Cam_Valpo_11-PTAS|267.738|6.372.319|10 meses|880|1,4499E-14|1,1263E-15|2,769E-14|1,2003E-14|2,7335E-14|
|AREA|SRC_618|Cam_Valpo_12-PTAS|267.762|6.372.358|10 meses|187|6,8377E-14|5,3113E-15|1,3058E-13|5,6606E-14|1,2891E-13|
|AREA|SRC_619|Cam_Valpo_13-PTAS|267.783|6.372.410|10 meses|225|5,682E-14|4,4136E-15|1,0851E-13|4,7039E-14|1,0712E-13|
|AREA|SRC_620|Cam_Valpo_14-PTAS|267.855|6.372.669|10 meses|1.076|1,186E-14|9,2126E-16|2,265E-14|9,8185E-15|2,2359E-14|
|AREA|SRC_621|Cam_Valpo_15-PTAS|267.848|6.372.720|10 meses|208|6,1396E-14|4,769E-15|1,1725E-13|5,0827E-14|1,1575E-13|
|AREA|SRC_622|Cam_Valpo_16-PTAS|267.715|6.373.066|10 meses|1.484|8,5959E-15|6,677E-16|1,6416E-14|7,1161E-15|1,6205E-14|
|AREA|SRC_623|Cam_Valpo_17-PTAS|267.705|6.373.122|10 meses|225|5,6589E-14|4,3957E-15|1,0807E-13|4,6847E-14|1,0668E-13|
|AREA|SRC_624|Cam_Valpo_18-PTAS|267.701|6.373.182|10 meses|241|5,2884E-14|4,1079E-15|1,0099E-13|4,378E-14|9,9699E-14|
|AREA|SRC_625|Cam_Valpo_19-PTAS|267.704|6.373.237|10 meses|218|5,8528E-14|4,5462E-15|1,1177E-13|4,8452E-14|1,1034E-13|
|AREA|SRC_626|Cam_Valpo_20-PTAS|267.713|6.373.309|10 meses|291|4,3799E-14|3,4022E-15|8,3644E-14|3,6259E-14|8,2572E-14|
|AREA|SRC_627|Cam_Valpo_21-PTAS|267.741|6.373.522|10 meses|860|1,4831E-14|1,152E-15|2,8323E-14|1,2278E-14|2,796E-14|
|AREA|SRC_628|Cam_Valpo_22-PTAS|267.757|6.373.574|10 meses|214|5,9653E-14|4,6336E-15|1,1392E-13|4,9384E-14|1,1246E-13|
|AREA|SRC_629|Cam_Valpo_23-PTAS|267.777|6.373.617|10 meses|187|6,8103E-14|5,29E-15|1,3006E-13|5,6379E-14|1,2839E-13|
|AREA|SRC_630|Cam_Valpo_24-PTAS|267.817|6.373.719|10 meses|441|2,8918E-14|2,2463E-15|5,5225E-14|2,394E-14|5,4517E-14|
|AREA|SRC_631|Cam_Valpo_25-PTAS|267.843|6.373.782|10 meses|273|4,68E-14|3,6353E-15|8,9376E-14|3,8744E-14|8,823E-14|
|AREA|SRC_632|Cam_Valpo_26-PTAS|267.877|6.373.831|10 meses|236|5,4048E-14|4,1983E-15|1,0322E-13|4,4744E-14|1,0189E-13|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 24. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 17

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 35 de 56

|Tipo<br>AREA|ID<br>SRC_633|Descripción<br>Cam_Valpo_27-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_633|Descripción<br>Cam_Valpo_27-PTAS|[m]<br>267.910|[m]<br>6.373.883|[m]<br>6.373.883|[m2]<br>246|[g/m2s]<br>5,1832E-14|[g/m2s]<br>4,0261E-15|[g/m2s]<br>9,8984E-14|[g/m2s]<br>4,2909E-14|[g/m2s]<br>9,7715E-14|
|AREA|SRC_634|Cam_Valpo_28-PTAS|268.105|6.374.174|10 meses|1.400|9,1152E-15|7,0804E-16|1,7407E-14|7,546E-15|1,7184E-14|
|AREA|SRC_635|Cam_Valpo_29-PTAS|268.274|6.374.430|10 meses|1.228|1,0388E-14|8,0689E-16|1,9838E-14|8,5995E-15|1,9583E-14|
|AREA|SRC_636|Cam_Valpo_30-PTAS|268.317|6.374.478|10 meses|254|5,0154E-14|3,8958E-15|9,5781E-14|4,152E-14|9,4552E-14|
|AREA|SRC_637|Cam_Valpo_31-PTAS|268.347|6.374.502|10 meses|154|8,2593E-14|6,4156E-15|1,5773E-13|6,8375E-14|1,5571E-13|
|AREA|SRC_638|Cam_Valpo_32-PTAS|269.602|6.375.295|10 meses|5.936|2,1492E-15|1,6695E-16|4,1045E-15|1,7792E-15|4,0518E-15|
|AREA|SRC_639|Cam_Valpo_33-PTAS|270.646|6.375.956|10 meses|4.938|2,5832E-15|2,0066E-16|4,9333E-15|2,1385E-15|4,87E-15|
|AREA|SRC_640|Cam_Valpo_34-PTAS|270.700|6.375.970|10 meses|221|5,7791E-14|4,489E-15|1,1037E-13|4,7842E-14|1,0895E-13|
|AREA|SRC_641|Cam_Valpo_35-PTAS|270.759|6.375.972|10 meses|232|5,498E-14|4,2707E-15|1,05E-13|4,5515E-14|1,0365E-13|
|AREA|SRC_642|Cam_Valpo_36-PTAS|270.817|6.375.960|10 meses|238|5,3638E-14|4,1664E-15|1,0243E-13|4,4404E-14|1,0112E-13|
|AREA|SRC_643|Cam_Valpo_37-PTAS|271.210|6.375.788|10 meses|1.711|7,4561E-15|5,7916E-16|1,4239E-14|6,1725E-15|1,4056E-14|
|AREA|SRC_644|Cam_Valpo_38-PTAS|271.299|6.375.786|10 meses|362|3,5235E-14|2,7369E-15|6,7289E-14|2,9169E-14|6,6426E-14|
|AREA|SRC_645|Cam_Valpo_39-PTAS|271.410|6.375.784|10 meses|444|2,8726E-14|2,2314E-15|5,4859E-14|2,3781E-14|5,4156E-14|
|AREA|SRC_646|Cam_Valpo_40-PTAS|271.537|6.375.829|10 meses|540|2,3626E-14|1,8352E-15|4,512E-14|1,9559E-14|4,4541E-14|
|AREA|SRC_647|Cam_Valpo_41-PTAS|271.698|6.375.908|10 meses|718|1,7776E-14|1,3808E-15|3,3948E-14|1,4716E-14|3,3513E-14|
|AREA|SRC_648|Cam_Valpo_42-PTAS|271.943|6.376.040|10 meses|1.111|1,1478E-14|8,9158E-16|2,192E-14|9,5022E-15|2,1639E-14|
|AREA|SRC_649|Cam_Valpo_43-PTAS|272.216|6.376.245|10 meses|1.366|9,3401E-15|7,2551E-16|1,7837E-14|7,7323E-15|1,7608E-14|
|AREA|SRC_650|Cam_Valpo_44-PTAS|272.308|6.376.283|10 meses|397|3,2149E-14|2,4972E-15|6,1395E-14|2,6614E-14|6,0608E-14|
|AREA|SRC_651|Cam_Valpo_45-PTAS|272.828|6.376.412|10 meses|2.140|5,9625E-15|4,6315E-16|1,1387E-14|4,9361E-15|1,1241E-14|
|AREA|SRC_652|Cam_Valpo_46-PTAS|272.961|6.376.463|10 meses|573|2,2267E-14|1,7296E-15|4,2524E-14|1,8434E-14|4,1979E-14|
|AREA|SRC_653|Cam_Valpo_47-PTAS|273.101|6.376.548|10 meses|656|1,9434E-14|1,5096E-15|3,7113E-14|1,6088E-14|3,6637E-14|
|AREA|SRC_654|Cam_Valpo_48-PTAS|273.683|6.376.890|10 meses|2.700|4,7248E-15|3,6701E-16|9,0231E-15|3,9114E-15|8,9074E-15|
|AREA|SRC_655|Cam_Valpo_49-PTAS|273.729|6.376.911|10 meses|199|6,4215E-14|4,988E-15|1,2263E-13|5,316E-14|1,2106E-13|
|AREA|SRC_656|Cam_Valpo_50-PTAS|273.841|6.376.934|10 meses|455|2,8007E-14|2,1755E-15|5,3485E-14|2,3185E-14|5,2799E-14|
|AREA|SRC_657|Cam_Valpo_51-PTAS|273.918|6.376.948|10 meses|315|4,0519E-14|3,1473E-15|7,7379E-14|3,3543E-14|7,6387E-14|
|AREA|SRC_658|Cam_Valpo_52-PTAS|273.963|6.376.959|10 meses|182|6,9982E-14|5,436E-15|1,3365E-13|5,7935E-14|1,3193E-13|
|AREA|SRC_659|Cam_Valpo_53-PTAS|274.013|6.376.981|10 meses|220|5,7928E-14|4,4997E-15|1,1063E-13|4,7956E-14|1,0921E-13|
|AREA|SRC_660|Cam_Valpo_54-PTAS|274.045|6.377.010|10 meses|176|7,259E-14|5,6385E-15|1,3863E-13|6,0094E-14|1,3685E-13|
|AREA|SRC_661|Cam_Valpo_55-PTAS|274.402|6.377.569|10 meses|2.655|4,8049E-15|3,7323E-16|9,1761E-15|3,9778E-15|9,0584E-15|
|AREA|SRC_662|Cam_Valpo_56-PTAS|274.508|6.377.712|10 meses|712|1,7912E-14|1,3913E-15|3,4207E-14|1,4828E-14|3,3768E-14|
|AREA|SRC_663|Cam_Valpo_57-PTAS|274.515|6.377.737|10 meses|106|1,2087E-13|9,3887E-15|2,3083E-13|1,0006E-13|2,2787E-13|
|AREA|SRC_664|Cam_Valpo_58-PTAS|274.530|6.377.783|10 meses|191|6,6844E-14|5,1922E-15|1,2765E-13|5,5337E-14|1,2602E-13|
|AREA|SRC_665|Cam_Valpo_59-PTAS|274.571|6.378.190|10 meses|1.641|7,7761E-15|6,0402E-16|1,485E-14|6,4374E-15|1,466E-14|
|AREA|SRC_666|Cam_Valpo_60-PTAS|274.512|6.378.662|10 meses|1.902|6,7063E-15|5,2092E-16|1,2807E-14|5,5518E-15|1,2643E-14|
|AREA|SRC_667|Cam_Valpo_61-PTAS|274.484|6.378.742|10 meses|339|3,7591E-14|2,92E-15|7,1789E-14|3,112E-14|7,0869E-14|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 25. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 18

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 36 de 56

|Tipo<br>AREA|ID<br>SRC_668|Descripción<br>Cam_Valpo_62-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_668|Descripción<br>Cam_Valpo_62-PTAS|[m]<br>274.397|[m]<br>6.378.959|[m]<br>6.378.959|[m2]<br>935|[g/m2s]<br>1,3646E-14|[g/m2s]<br>1,0599E-15|[g/m2s]<br>2,6059E-14|[g/m2s]<br>1,1296E-14|[g/m2s]<br>2,5725E-14|
|AREA|SRC_669|Cam_Valpo_63-PTAS|274.391|6.379.006|10 meses|190|6,729E-14|5,2269E-15|1,2851E-13|5,5707E-14|1,2686E-13|
|AREA|SRC_670|Cam_Valpo_64-PTAS|274.392|6.379.034|10 meses|109|1,1652E-13|9,0505E-15|2,2251E-13|9,6458E-14|2,1966E-13|
|AREA|SRC_671|Cam_Valpo_65-PTAS|274.513|6.379.469|10 meses|1.806|7,0653E-15|5,4881E-16|1,3493E-14|5,849E-15|1,332E-14|
|AREA|SRC_672|Cam_Valpo_66-PTAS|274.514|6.379.510|10 meses|163|7,8093E-14|6,066E-15|1,4914E-13|6,465E-14|1,4722E-13|
|AREA|SRC_673|Cam_Valpo_67-PTAS|274.503|6.379.560|10 meses|209|6,1117E-14|4,7474E-15|1,1672E-13|5,0596E-14|1,1522E-13|
|AREA|SRC_674|Cam_Valpo_68-PTAS|274.488|6.379.623|10 meses|255|4,9941E-14|3,8793E-15|9,5374E-14|4,1344E-14|9,4151E-14|
|AREA|SRC_675|Cam_Valpo_69-PTAS|274.426|6.379.798|10 meses|746|1,711E-14|1,3291E-15|3,2676E-14|1,4165E-14|3,2257E-14|
|AREA|SRC_676|Cam_Valpo_70-PTAS|274.386|6.379.897|10 meses|429|2,9769E-14|2,3123E-15|5,685E-14|2,4644E-14|5,6121E-14|
|AREA|SRC_677|Cam_Valpo_71-PTAS|274.352|6.379.981|10 meses|360|3,5413E-14|2,7508E-15|6,763E-14|2,9317E-14|6,6763E-14|
|AREA|SRC_678|Cam_Valpo_72-PTAS|274.336|6.380.041|10 meses|249|5,1133E-14|3,9718E-15|9,765E-14|4,233E-14|9,6397E-14|
|AREA|SRC_679|Cam_Valpo_73-PTAS|274.333|6.380.099|10 meses|228|5,6001E-14|4,35E-15|1,0695E-13|4,6361E-14|1,0558E-13|
|AREA|SRC_680|Cam_Valpo_74-PTAS|274.332|6.380.163|10 meses|257|4,9586E-14|3,8516E-15|9,4695E-14|4,1049E-14|9,348E-14|
|AREA|SRC_681|Cam_Valpo_75-PTAS|274.329|6.380.546|10 meses|1.530|8,3355E-15|6,4747E-16|1,5919E-14|6,9005E-15|1,5714E-14|
|AREA|SRC_682|Cam_Valpo_76-PTAS|274.323|6.380.578|10 meses|131|9,7721E-14|7,5906E-15|1,8662E-13|8,0898E-14|1,8423E-13|
|AREA|SRC_683|Cam_Valpo_77-PTAS|274.308|6.380.608|10 meses|138|9,2326E-14|7,1716E-15|1,7632E-13|7,6432E-14|1,7406E-13|
|AREA|SRC_684|Cam_Valpo_78-PTAS|274.078|6.381.086|10 meses|2.121|6,016E-15|4,673E-16|1,1489E-14|4,9804E-15|1,1342E-14|
|AREA|SRC_685|Cam_Valpo_79-PTAS|274.036|6.381.146|10 meses|293|4,3546E-14|3,3825E-15|8,316E-14|3,6049E-14|8,2094E-14|
|AREA|SRC_686|Cam_Valpo_80-PTAS|273.997|6.381.192|10 meses|243|5,2561E-14|4,0828E-15|1,0038E-13|4,3513E-14|9,9091E-14|
|AREA|SRC_687|Cam_Valpo_81-PTAS|273.945|6.381.212|10 meses|225|5,6636E-14|4,3993E-15|1,0816E-13|4,6886E-14|1,0677E-13|
|AREA|SRC_688|Cam_Valpo_82-PTAS|273.863|6.381.235|10 meses|341|3,7455E-14|2,9094E-15|7,1529E-14|3,1007E-14|7,0612E-14|
|AREA|SRC_689|Cam_Valpo_83-PTAS|273.527|6.381.309|10 meses|1.377|9,2665E-15|7,1979E-16|1,7697E-14|7,6713E-15|1,747E-14|
|AREA|SRC_690|Cam_Valpo_84-PTAS|273.488|6.381.317|10 meses|159|8,0319E-14|6,2389E-15|1,5339E-13|6,6492E-14|1,5142E-13|
|AREA|SRC_691|Cam_Valpo_85-PTAS|273.437|6.381.311|10 meses|211|6,0572E-14|4,705E-15|1,1568E-13|5,0145E-14|1,1419E-13|
|AREA|SRC_692|Cam_Valpo_86-PTAS|273.400|6.381.306|10 meses|149|8,5761E-14|6,6616E-15|1,6378E-13|7,0997E-14|1,6168E-13|
|AREA|SRC_693|Cam_Valpo_87-PTAS|273.330|6.381.278|10 meses|302|4,2239E-14|3,281E-15|8,0665E-14|3,4968E-14|7,9631E-14|
|AREA|SRC_694|Cam_Valpo_88-PTAS|273.269|6.381.275|10 meses|240|5,3083E-14|4,1233E-15|1,0137E-13|4,3945E-14|1,0007E-13|
|AREA|SRC_695|Cam_Valpo_89-PTAS|273.210|6.381.284|10 meses|239|5,3446E-14|4,1515E-15|1,0207E-13|4,4245E-14|1,0076E-13|
|AREA|SRC_696|Cam_Valpo_90-PTAS|273.140|6.381.307|10 meses|292|4,3705E-14|3,3948E-15|8,3464E-14|3,6181E-14|8,2393E-14|
|AREA|SRC_697|Cam_Valpo_91-PTAS|273.026|6.381.364|10 meses|511|2,4984E-14|1,9406E-15|4,7712E-14|2,0683E-14|4,71E-14|
|AREA|SRC_698|Cam_Valpo_92-PTAS|272.787|6.381.471|10 meses|1.046|1,219E-14|9,4692E-16|2,3281E-14|1,0092E-14|2,2982E-14|
|AREA|SRC_699|Cam_Valpo_93-PTAS|272.625|6.381.553|10 meses|727|1,7552E-14|1,3634E-15|3,3519E-14|1,453E-14|3,3089E-14|
|AREA|SRC_700|Cam_Valpo_94-PTAS|272.586|6.381.587|10 meses|206|6,1966E-14|4,8133E-15|1,1834E-13|5,1298E-14|1,1682E-13|
|AREA|SRC_701|Cam_Valpo_95-PTAS|272.567|6.381.621|10 meses|150|8,4904E-14|6,595E-15|1,6214E-13|7,0288E-14|1,6006E-13|
|AREA|SRC_702|Cam_Valpo_96-PTAS|272.558|6.381.659|10 meses|155|8,2522E-14|6,41E-15|1,5759E-13|6,8316E-14|1,5557E-13|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 26. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 19

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 37 de 56

|Tipo<br>AREA|ID<br>SRC_703|Descripción<br>Cam_Valpo_97-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_703|Descripción<br>Cam_Valpo_97-PTAS|[m]<br>272.513|[m]<br>6.381.931|[m]<br>6.381.931|[m2]<br>1.103|[g/m2s]<br>1,1564E-14|[g/m2s]<br>8,9822E-16|[g/m2s]<br>2,2083E-14|[g/m2s]<br>9,573E-15|[g/m2s]<br>2,18E-14|
|AREA|SRC_704|Cam_Valpo_98-PTAS|272.500|6.382.030|10 meses|398|3,2023E-14|2,4874E-15|6,1155E-14|2,651E-14|6,037E-14|
|AREA|SRC_705|Cam_Valpo_99-PTAS|272.492|6.382.086|10 meses|224|5,6983E-14|4,4262E-15|1,0882E-13|4,7173E-14|1,0743E-13|
|AREA|SRC_706|Cam_Valpo_100-PTAS|272.491|6.382.127|10 meses|164|7,7637E-14|6,0306E-15|1,4826E-13|6,4272E-14|1,4636E-13|
|AREA|SRC_707|Cam_Valpo_101-PTAS|272.506|6.382.188|10 meses|247|5,1579E-14|4,0065E-15|9,8501E-14|4,2699E-14|9,7238E-14|
|AREA|SRC_708|Cam_Valpo_102-PTAS|272.660|6.383.439|10 meses|5.043|2,5295E-15|1,9648E-16|4,8306E-15|2,094E-15|4,7687E-15|
|AREA|SRC_709|Cam_Valpo_103-PTAS|272.630|6.384.559|10 meses|4.479|2,8482E-15|2,2124E-16|5,4393E-15|2,3579E-15|5,3696E-15|
|AREA|SRC_710|Cam_Valpo_104-PTAS|272.626|6.385.227|10 meses|2.671|4,7759E-15|3,7098E-16|9,1207E-15|3,9538E-15|9,0038E-15|
|AREA|SRC_711|Cam_Valpo_105-PTAS|272.602|6.386.454|10 meses|4.906|2,6004E-15|2,0199E-16|4,966E-15|2,1527E-15|4,9023E-15|
|AREA|SRC_712|Cam_Valpo_106-PTAS|272.609|6.386.527|10 meses|293|4,3609E-14|3,3874E-15|8,3282E-14|3,6102E-14|8,2214E-14|
|AREA|SRC_713|Cam_Valpo_107-PTAS|272.650|6.386.615|10 meses|385|3,3161E-14|2,5759E-15|6,3329E-14|2,7453E-14|6,2517E-14|
|AREA|SRC_714|Cam_Valpo_108-PTAS|272.755|6.386.705|10 meses|550|2,3194E-14|1,8017E-15|4,4295E-14|1,9202E-14|4,3727E-14|
|AREA|SRC_715|Cam_Valpo_109-PTAS|272.846|6.386.776|10 meses|461|2,7681E-14|2,1502E-15|5,2864E-14|2,2916E-14|5,2186E-14|
|AREA|SRC_716|Cam_Valpo_110-PTAS|272.918|6.386.821|10 meses|339|3,7654E-14|2,9248E-15|7,1909E-14|3,1172E-14|7,0987E-14|
|AREA|SRC_717|Cam_Valpo_111-PTAS|272.959|6.386.856|10 meses|216|5,9141E-14|4,5938E-15|1,1294E-13|4,896E-14|1,1149E-13|
|AREA|SRC_718|Cam_Valpo_112-PTAS|272.979|6.386.909|10 meses|229|5,5629E-14|4,321E-15|1,0624E-13|4,6052E-14|1,0487E-13|
|AREA|SRC_719|Cam_Valpo_113-PTAS|272.982|6.386.950|10 meses|168|7,5846E-14|5,8915E-15|1,4485E-13|6,2789E-14|1,4299E-13|
|AREA|SRC_720|Cam_Valpo_114-PTAS|272.974|6.387.033|10 meses|335|3,813E-14|2,9618E-15|7,2818E-14|3,1566E-14|7,1884E-14|
|AREA|SRC_721|Cam_Valpo_115-PTAS|272.969|6.387.289|10 meses|1.021|1,2491E-14|9,7029E-16|2,3855E-14|1,0341E-14|2,3549E-14|
|AREA|SRC_722|Cam_Valpo_116-PTAS|272.950|6.387.316|10 meses|136|9,3898E-14|7,2937E-15|1,7932E-13|7,7734E-14|1,7702E-13|
|AREA|SRC_723|Cam_Valpo_117-PTAS|272.918|6.387.332|10 meses|151|8,4697E-14|6,579E-15|1,6175E-13|7,0116E-14|1,5967E-13|
|AREA|SRC_724|Cam_Valpo_118-PTAS|272.871|6.387.328|10 meses|193|6,606E-14|5,1313E-15|1,2616E-13|5,4688E-14|1,2454E-13|
|AREA|SRC_725|Cam_Valpo_119-PTAS|272.818|6.387.319|10 meses|215|5,9384E-14|4,6128E-15|1,1341E-13|4,9161E-14|1,1195E-13|
|AREA|SRC_726|Cam_Valpo_120-PTAS|272.669|6.387.324|10 meses|594|2,1494E-14|1,6696E-15|4,1048E-14|1,7794E-14|4,0521E-14|
|AREA|SRC_727|Cam_Valpo_121-PTAS|272.536|6.387.380|10 meses|574|2,222E-14|1,726E-15|4,2435E-14|1,8395E-14|4,1891E-14|
|AREA|SRC_728|Cam_Valpo_122-PTAS|272.406|6.387.475|10 meses|643|1,9844E-14|1,5414E-15|3,7897E-14|1,6428E-14|3,7411E-14|
|AREA|SRC_729|Cam_Valpo_123-PTAS|272.321|6.387.544|10 meses|439|2,9068E-14|2,2579E-15|5,5513E-14|2,4064E-14|5,4801E-14|
|AREA|SRC_730|Cam_Valpo_124-PTAS|272.252|6.387.605|10 meses|366|3,4854E-14|2,7073E-15|6,6561E-14|2,8854E-14|6,5707E-14|
|AREA|SRC_731|Cam_Valpo_125-PTAS|272.138|6.387.749|10 meses|734|1,7381E-14|1,3501E-15|3,3192E-14|1,4389E-14|3,2767E-14|
|AREA|SRC_732|Cam_Valpo_126-PTAS|272.059|6.387.890|10 meses|646|1,9757E-14|1,5346E-15|3,773E-14|1,6356E-14|3,7246E-14|
|AREA|SRC_733|Cam_Valpo_127-PTAS|272.019|6.388.008|10 meses|494|2,5809E-14|2,0047E-15|4,9288E-14|2,1366E-14|4,8655E-14|
|AREA|SRC_734|Cam_Valpo_128-PTAS|272.005|6.388.086|10 meses|318|4,0095E-14|3,1145E-15|7,6571E-14|3,3193E-14|7,5589E-14|
|AREA|SRC_735|Cam_Valpo_129-PTAS|272.005|6.388.171|10 meses|338|3,7698E-14|2,9283E-15|7,1994E-14|3,1209E-14|7,107E-14|
|AREA|SRC_736|Cam_Valpo_130-PTAS|272.018|6.388.207|10 meses|149|8,5388E-14|6,6326E-15|1,6307E-13|7,0688E-14|1,6098E-13|
|AREA|SRC_737|Cam_Valpo_131-PTAS|272.053|6.388.222|10 meses|145|8,8241E-14|6,8543E-15|1,6852E-13|7,3051E-14|1,6636E-13|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 27. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 20

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 38 de 56

|Tipo<br>AREA|ID<br>SRC_738|Descripción<br>Cam_Valpo_132-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_738|Descripción<br>Cam_Valpo_132-PTAS|[m]<br>272.113|[m]<br>6.388.260|[m]<br>6.388.260|[m2]<br>286|[g/m2s]<br>4,4575E-14|[g/m2s]<br>3,4624E-15|[g/m2s]<br>8,5126E-14|[g/m2s]<br>3,6901E-14|[g/m2s]<br>8,4034E-14|
|AREA|SRC_739|Cam_Valpo_133-PTAS|272.165|6.388.289|10 meses|237|5,394E-14|4,1899E-15|1,0301E-13|4,4654E-14|1,0169E-13|
|AREA|SRC_740|Cam_Valpo_134-PTAS|272.170|6.388.313|10 meses|103|1,2381E-13|9,6171E-15|2,3644E-13|1,025E-13|2,3341E-13|
|AREA|SRC_741|Cam_Valpo_135-PTAS|272.160|6.388.355|10 meses|179|7,1399E-14|5,546E-15|1,3635E-13|5,9107E-14|1,346E-13|
|AREA|SRC_742|Cam_Valpo_136-PTAS|272.116|6.388.384|10 meses|213|5,9844E-14|4,6485E-15|1,1429E-13|4,9542E-14|1,1282E-13|
|AREA|SRC_743|Cam_Valpo_137-PTAS|271.990|6.388.473|10 meses|618|2,0634E-14|1,6028E-15|3,9405E-14|1,7082E-14|3,8899E-14|
|AREA|SRC_744|Cam_Valpo_138-PTAS|271.909|6.388.570|10 meses|502|2,54E-14|1,973E-15|4,8507E-14|2,1027E-14|4,7885E-14|
|AREA|SRC_745|Cam_Valpo_139-PTAS|271.887|6.388.631|10 meses|258|4,9509E-14|3,8457E-15|9,4548E-14|4,0986E-14|9,3335E-14|
|AREA|SRC_746|Cam_Valpo_140-PTAS|271.869|6.388.710|10 meses|325|3,9305E-14|3,053E-15|7,5061E-14|3,2538E-14|7,4098E-14|
|AREA|SRC_747|Cam_Valpo_141-PTAS|271.879|6.388.778|10 meses|271|4,7122E-14|3,6603E-15|8,9991E-14|3,901E-14|8,8837E-14|
|AREA|SRC_748|Cam_Valpo_142-PTAS|271.889|6.388.831|10 meses|216|5,9112E-14|4,5916E-15|1,1289E-13|4,8936E-14|1,1144E-13|
|AREA|SRC_749|Cam_Valpo_143-PTAS|271.888|6.388.910|10 meses|318|4,0174E-14|3,1206E-15|7,6721E-14|3,3258E-14|7,5737E-14|
|AREA|SRC_750|Cam_Valpo_144-PTAS|271.765|6.389.249|10 meses|1.444|8,8355E-15|6,8631E-16|1,6873E-14|7,3145E-15|1,6657E-14|
|AREA|SRC_751|Cam_Valpo_145-PTAS|271.745|6.389.323|10 meses|309|4,1328E-14|3,2102E-15|7,8925E-14|3,4213E-14|7,7913E-14|
|AREA|SRC_752|Cam_Valpo_146-PTAS|271.746|6.389.404|10 meses|321|3,9725E-14|3,0857E-15|7,5864E-14|3,2887E-14|7,4891E-14|
|AREA|SRC_753|Cam_Valpo_147-PTAS|271.745|6.389.713|10 meses|1.235|1,0327E-14|8,0215E-16|1,9721E-14|8,549E-15|1,9468E-14|
|AREA|SRC_754|Cam_Valpo_148-PTAS|271.729|6.389.779|10 meses|275|4,6433E-14|3,6068E-15|8,8674E-14|3,844E-14|8,7537E-14|
|AREA|SRC_755|Cam_Valpo_149-PTAS|271.405|6.390.771|10 meses|4.170|3,0594E-15|2,3765E-16|5,8427E-15|2,5328E-15|5,7678E-15|
|AREA|SRC_756|Cam_Valpo_150-PTAS|271.408|6.390.852|10 meses|324|3,9365E-14|3,0577E-15|7,5176E-14|3,2588E-14|7,4212E-14|
|AREA|SRC_757|Cam_Valpo_151-PTAS|271.425|6.390.918|10 meses|270|4,7291E-14|3,6734E-15|9,0313E-14|3,915E-14|8,9154E-14|
|AREA|SRC_758|Cam_Valpo_152-PTAS|271.595|6.391.444|10 meses|2.210|5,7719E-15|4,4834E-16|1,1023E-14|4,7782E-15|1,0881E-14|
|AREA|SRC_759|Cam_Valpo_153-PTAS|271.601|6.391.518|10 meses|297|4,2943E-14|3,3357E-15|8,201E-14|3,5551E-14|8,0958E-14|
|AREA|SRC_760|Cam_Valpo_154-PTAS|271.583|6.391.599|10 meses|335|3,8131E-14|2,9619E-15|7,282E-14|3,1567E-14|7,1886E-14|
|AREA|SRC_761|Cam_Valpo_155-PTAS|271.490|6.391.665|10 meses|462|2,7595E-14|2,1435E-15|5,27E-14|2,2845E-14|5,2024E-14|
|AREA|SRC_762|Cam_Valpo_156-PTAS|271.388|6.391.779|10 meses|610|2,0896E-14|1,6232E-15|3,9906E-14|1,7299E-14|3,9395E-14|
|AREA|SRC_763|Cam_Valpo_157-PTAS|271.303|6.391.969|10 meses|830|1,5371E-14|1,1939E-15|2,9354E-14|1,2725E-14|2,8977E-14|
|AREA|SRC_764|Cam_Valpo_158-PTAS|271.249|6.392.048|10 meses|385|3,3094E-14|2,5706E-15|6,3201E-14|2,7397E-14|6,239E-14|
|AREA|SRC_765|Cam_Valpo_159-PTAS|271.095|6.392.199|10 meses|863|1,478E-14|1,1481E-15|2,8226E-14|1,2236E-14|2,7864E-14|
|AREA|SRC_766|Cam_Valpo_160-PTAS|271.003|6.392.357|10 meses|727|1,7537E-14|1,3622E-15|3,3492E-14|1,4518E-14|3,3062E-14|
|AREA|SRC_767|Cam_Valpo_161-PTAS|270.864|6.392.618|10 meses|1.182|1,0796E-14|8,3857E-16|2,0617E-14|8,9372E-15|2,0352E-14|
|AREA|SRC_768|Cam_Valpo_162-PTAS|270.665|6.392.901|10 meses|1.387|9,1997E-15|7,146E-16|1,7569E-14|7,616E-15|1,7344E-14|
|AREA|SRC_769|Cam_Valpo_163-PTAS|270.570|6.393.060|10 meses|740|1,7244E-14|1,3394E-15|3,2931E-14|1,4275E-14|3,2508E-14|
|AREA|SRC_770|Cam_Valpo_164-PTAS|270.535|6.393.162|10 meses|428|2,981E-14|2,3156E-15|5,6929E-14|2,4678E-14|5,6199E-14|
|AREA|SRC_771|Cam_Valpo_165-PTAS|270.408|6.393.157|10 meses|516|2,4715E-14|1,9198E-15|4,7199E-14|2,046E-14|4,6594E-14|
|AREA|SRC_772|Cam_Valpo_166-PTAS|270.322|6.393.156|10 meses|344|3,7072E-14|2,8796E-15|7,0797E-14|3,069E-14|6,9889E-14|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 28. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 21

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 39 de 56

|Tipo<br>AREA|ID<br>SRC_773|Descripción<br>Cam_Valpo_167-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_773|Descripción<br>Cam_Valpo_167-PTAS|[m]<br>270.198|[m]<br>6.393.225|[m]<br>6.393.225|[m2]<br>562|[g/m2s]<br>2,2698E-14|[g/m2s]<br>1,7631E-15|[g/m2s]<br>4,3347E-14|[g/m2s]<br>1,8791E-14|[g/m2s]<br>4,2791E-14|
|AREA|SRC_774|Cam_Valpo_168-PTAS|270.084|6.393.222|10 meses|462|2,7638E-14|2,1468E-15|5,2781E-14|2,288E-14|5,2104E-14|
|AREA|SRC_775|Cam_Valpo_169-PTAS|270.014|6.393.114|10 meses|520|2,453E-14|1,9054E-15|4,6846E-14|2,0307E-14|4,6245E-14|
|AREA|SRC_776|Cam_Valpo_170-PTAS|269.944|6.393.026|10 meses|448|2,8463E-14|2,2109E-15|5,4357E-14|2,3563E-14|5,366E-14|
|AREA|SRC_777|Cam_Valpo_171-PTAS|269.831|6.392.981|10 meses|484|2,6338E-14|2,0459E-15|5,0299E-14|2,1804E-14|4,9654E-14|
|AREA|SRC_778|Cam_Valpo_172-PTAS|269.702|6.392.966|10 meses|517|2,4675E-14|1,9167E-15|4,7123E-14|2,0428E-14|4,6519E-14|
|AREA|SRC_779|Cam_Valpo_173-PTAS|269.506|6.393.084|10 meses|907|1,4069E-14|1,0928E-15|2,6868E-14|1,1647E-14|2,6524E-14|
|AREA|SRC_780|Cam_Valpo_174-PTAS|269.407|6.393.106|10 meses|411|3,1068E-14|2,4132E-15|5,9331E-14|2,572E-14|5,857E-14|
|AREA|SRC_781|Cam_Valpo_175-PTAS|269.355|6.393.219|10 meses|493|2,587E-14|2,0095E-15|4,9404E-14|2,1416E-14|4,877E-14|
|AREA|SRC_782|Cam_Valpo_176-PTAS|269.450|6.393.436|10 meses|940|1,3577E-14|1,0546E-15|2,5929E-14|1,124E-14|2,5597E-14|
|AREA|SRC_783|Cam_Valpo_177-PTAS|269.537|6.393.768|10 meses|1.375|9,2744E-15|7,2041E-16|1,7712E-14|7,6779E-15|1,7484E-14|
|AREA|SRC_784|Cam_Valpo_178-PTAS|269.541|6.393.876|10 meses|433|2,9451E-14|2,2876E-15|5,6243E-14|2,4381E-14|5,5522E-14|
|AREA|SRC_785|Cam_Valpo_179-PTAS|269.514|6.393.952|10 meses|327|3,8953E-14|3,0258E-15|7,439E-14|3,2248E-14|7,3436E-14|
|AREA|SRC_786|Cam_Valpo_180-PTAS|269.461|6.394.006|10 meses|302|4,2238E-14|3,2809E-15|8,0663E-14|3,4967E-14|7,9628E-14|
|AREA|SRC_787|Cam_Valpo_181-PTAS|269.456|6.394.087|10 meses|318|4,0175E-14|3,1206E-15|7,6723E-14|3,3259E-14|7,5739E-14|
|AREA|SRC_788|Cam_Valpo_182-PTAS|269.494|6.394.169|10 meses|359|3,5541E-14|2,7607E-15|6,7873E-14|2,9422E-14|6,7002E-14|
|AREA|SRC_789|Cam_Valpo_183-PTAS|269.580|6.394.296|10 meses|612|2,0845E-14|1,6192E-15|3,9808E-14|1,7257E-14|3,9298E-14|
|AREA|SRC_790|Cam_Valpo_184-PTAS|269.614|6.394.394|10 meses|417|3,0621E-14|2,3786E-15|5,8478E-14|2,535E-14|5,7728E-14|
|AREA|SRC_791|Cam_Valpo_185-PTAS|269.617|6.394.492|10 meses|397|3,2169E-14|2,4987E-15|6,1433E-14|2,6631E-14|6,0645E-14|
|AREA|SRC_792|Cam_Valpo_186-PTAS|269.532|6.394.634|10 meses|664|1,9207E-14|1,4919E-15|3,668E-14|1,5901E-14|3,621E-14|
|AREA|SRC_793|Cam_Valpo_187-PTAS|269.478|6.394.752|10 meses|518|2,4618E-14|1,9122E-15|4,7013E-14|2,038E-14|4,6411E-14|
|AREA|SRC_794|Cam_Valpo_188-PTAS|269.437|6.394.881|10 meses|541|2,3583E-14|1,8319E-15|4,5038E-14|1,9523E-14|4,446E-14|
|AREA|SRC_795|Cam_Valpo_189-PTAS|269.448|6.395.002|10 meses|483|2,6387E-14|2,0496E-15|5,0392E-14|2,1844E-14|4,9745E-14|
|AREA|SRC_796|Cam_Valpo_190-PTAS|269.465|6.395.049|10 meses|198|6,4487E-14|5,0092E-15|1,2315E-13|5,3386E-14|1,2157E-13|
|AREA|SRC_797|Cam_Valpo_191-PTAS|269.701|6.395.188|10 meses|1.089|1,1718E-14|9,1022E-16|2,2378E-14|9,7008E-15|2,2091E-14|
|AREA|SRC_798|Cam_Valpo_192-PTAS|269.737|6.395.244|10 meses|269|4,7357E-14|3,6785E-15|9,0439E-14|3,9205E-14|8,9279E-14|
|AREA|SRC_799|Cam_Valpo_193-PTAS|269.748|6.395.318|10 meses|302|4,2258E-14|3,2824E-15|8,0701E-14|3,4983E-14|7,9666E-14|
|AREA|SRC_800|Cam_Valpo_194-PTAS|269.734|6.395.473|10 meses|624|2,0443E-14|1,588E-15|3,9041E-14|1,6924E-14|3,854E-14|
|AREA|SRC_801|Cam_Valpo_195-PTAS|269.791|6.395.575|10 meses|463|2,7558E-14|2,1406E-15|5,2629E-14|2,2814E-14|5,1954E-14|
|AREA|SRC_802|Cam_Valpo_196-PTAS|269.918|6.395.634|10 meses|558|2,288E-14|1,7772E-15|4,3694E-14|1,8941E-14|4,3133E-14|
|AREA|SRC_803|Cam_Valpo_197-PTAS|269.951|6.395.703|10 meses|312|4,0932E-14|3,1795E-15|7,817E-14|3,3886E-14|7,7167E-14|
|AREA|SRC_804|Cam_Valpo_198-PTAS|269.926|6.395.767|10 meses|278|4,5909E-14|3,5661E-15|8,7674E-14|3,8006E-14|8,655E-14|
|AREA|SRC_805|Cam_Valpo_199-PTAS|269.853|6.395.812|10 meses|348|3,6628E-14|2,8451E-15|6,995E-14|3,0323E-14|6,9052E-14|
|AREA|SRC_806|Cam_Valpo_200-PTAS|269.732|6.395.847|10 meses|505|2,5278E-14|1,9635E-15|4,8274E-14|2,0926E-14|4,7654E-14|
|AREA|SRC_807|Cam_Valpo_201-PTAS|269.688|6.395.928|10 meses|365|3,4907E-14|2,7114E-15|6,6662E-14|2,8898E-14|6,5807E-14|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 29. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 22

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 40 de 56

|Tipo<br>AREA|ID<br>SRC_808|Descripción<br>Cam_Valpo_202-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_808|Descripción<br>Cam_Valpo_202-PTAS|[m]<br>269.717|[m]<br>6.396.047|[m]<br>6.396.047|[m2]<br>485|[g/m2s]<br>2,632E-14|[g/m2s]<br>2,0445E-15|[g/m2s]<br>5,0265E-14|[g/m2s]<br>2,1789E-14|[g/m2s]<br>4,962E-14|
|AREA|SRC_809|Cam_Valpo_203-PTAS|269.712|6.396.106|10 meses|237|5,3716E-14|4,1725E-15|1,0258E-13|4,4469E-14|1,0127E-13|
|AREA|SRC_810|Cam_Valpo_204-PTAS|269.657|6.396.143|10 meses|271|4,699E-14|3,6501E-15|8,9739E-14|3,8901E-14|8,8588E-14|
|AREA|SRC_811|Cam_Valpo_205-PTAS|269.580|6.396.120|10 meses|326|3,9076E-14|3,0353E-15|7,4625E-14|3,2349E-14|7,3668E-14|
|AREA|SRC_812|Cam_Valpo_206-PTAS|269.501|6.396.070|10 meses|376|3,391E-14|2,634E-15|6,4759E-14|2,8073E-14|6,3929E-14|
|AREA|SRC_813|Cam_Valpo_207-PTAS|269.359|6.396.026|10 meses|594|2,1493E-14|1,6695E-15|4,1046E-14|1,7793E-14|4,0519E-14|
|AREA|SRC_814|Cam_Valpo_208-PTAS|269.272|6.396.023|10 meses|343|3,714E-14|2,8849E-15|7,0928E-14|3,0747E-14|7,0018E-14|
|AREA|SRC_815|Cam_Valpo_209-PTAS|269.222|6.396.073|10 meses|276|4,6253E-14|3,5928E-15|8,8331E-14|3,8291E-14|8,7199E-14|
|AREA|SRC_816|Cam_Valpo_210-PTAS|269.210|6.396.185|10 meses|446|2,8587E-14|2,2205E-15|5,4593E-14|2,3666E-14|5,3893E-14|
|AREA|SRC_817|Cam_Valpo_211-PTAS|269.167|6.396.232|10 meses|255|4,9937E-14|3,879E-15|9,5367E-14|4,1341E-14|9,4143E-14|
|AREA|SRC_818|Cam_Valpo_212-PTAS|269.082|6.396.226|10 meses|350|3,6492E-14|2,8346E-15|6,969E-14|3,021E-14|6,8796E-14|
|AREA|SRC_819|Cam_Valpo_213-PTAS|268.998|6.396.240|10 meses|336|3,8019E-14|2,9532E-15|7,2606E-14|3,1474E-14|7,1675E-14|
|AREA|SRC_820|Cam_Valpo_214-PTAS|268.894|6.396.300|10 meses|480|2,6572E-14|2,064E-15|5,0745E-14|2,1998E-14|5,0094E-14|
|AREA|SRC_821|Cam_Valpo_215-PTAS|268.805|6.396.381|10 meses|477|2,6717E-14|2,0753E-15|5,1022E-14|2,2118E-14|5,0368E-14|
|AREA|SRC_822|Cam_Valpo_216-PTAS|268.734|6.396.481|10 meses|489|2,607E-14|2,025E-15|4,9786E-14|2,1582E-14|4,9148E-14|
|AREA|SRC_823|Cam_Valpo_217-PTAS|268.692|6.396.569|10 meses|388|3,2852E-14|2,5518E-15|6,2738E-14|2,7196E-14|6,1933E-14|
|AREA|SRC_824|Cam_Valpo_218-PTAS|268.614|6.396.686|10 meses|564|2,2631E-14|1,7579E-15|4,322E-14|1,8735E-14|4,2666E-14|
|AREA|SRC_825|Cam_Valpo_219-PTAS|268.551|6.396.751|10 meses|365|3,4938E-14|2,7139E-15|6,6723E-14|2,8924E-14|6,5867E-14|
|AREA|SRC_826|Cam_Valpo_220-PTAS|268.525|6.396.834|10 meses|343|3,7219E-14|2,8911E-15|7,1079E-14|3,0812E-14|7,0167E-14|
|AREA|SRC_827|Cam_Valpo_221-PTAS|268.521|6.396.918|10 meses|335|3,8058E-14|2,9562E-15|7,2681E-14|3,1507E-14|7,1749E-14|
|AREA|SRC_828|Cam_Valpo_222-PTAS|268.510|6.396.996|10 meses|312|4,0865E-14|3,1743E-15|7,8041E-14|3,383E-14|7,704E-14|
|AREA|SRC_829|Cam_Valpo_223-PTAS|268.441|6.397.095|10 meses|487|2,6207E-14|2,0356E-15|5,0048E-14|2,1695E-14|4,9406E-14|
|AREA|SRC_830|Cam_Valpo_224-PTAS|268.352|6.397.195|10 meses|538|2,372E-14|1,8425E-15|4,5299E-14|1,9637E-14|4,4718E-14|
|AREA|SRC_831|Cam_Valpo_225-PTAS|268.295|6.397.296|10 meses|460|2,7708E-14|2,1523E-15|5,2915E-14|2,2938E-14|5,2236E-14|
|AREA|SRC_832|Cam_Valpo_226-PTAS|268.265|6.397.370|10 meses|319|3,999E-14|3,1063E-15|7,637E-14|3,3106E-14|7,539E-14|
|AREA|SRC_833|Cam_Valpo_227-PTAS|268.236|6.397.470|10 meses|415|3,0776E-14|2,3906E-15|5,8773E-14|2,5478E-14|5,8019E-14|
|AREA|SRC_834|Cam_Valpo_228-PTAS|268.225|6.397.539|10 meses|278|4,5886E-14|3,5642E-15|8,7629E-14|3,7986E-14|8,6505E-14|
|AREA|SRC_835|Cam_Valpo_229-PTAS|268.212|6.397.650|10 meses|446|2,8573E-14|2,2195E-15|5,4567E-14|2,3654E-14|5,3867E-14|
|AREA|SRC_836|Cam_Valpo_230-PTAS|268.292|6.397.691|10 meses|353|3,6149E-14|2,8079E-15|6,9034E-14|2,9926E-14|6,8149E-14|
|AREA|SRC_837|Cam_Valpo_231-PTAS|268.324|6.397.741|10 meses|244|5,2262E-14|4,0596E-15|9,9807E-14|4,3265E-14|9,8527E-14|
|AREA|SRC_838|Cam_Valpo_232-PTAS|268.344|6.397.809|10 meses|285|4,4837E-14|3,4828E-15|8,5626E-14|3,7118E-14|8,4527E-14|
|AREA|SRC_839|Cam_Valpo_233-PTAS|268.317|6.397.871|10 meses|277|4,5987E-14|3,5721E-15|8,7823E-14|3,807E-14|8,6696E-14|
|AREA|SRC_840|Cam_Valpo_234-PTAS|268.289|6.397.931|10 meses|263|4,8424E-14|3,7614E-15|9,2476E-14|4,0088E-14|9,129E-14|
|AREA|SRC_841|Cam_Valpo_235-PTAS|268.281|6.397.993|10 meses|246|5,1813E-14|4,0247E-15|9,8949E-14|4,2894E-14|9,768E-14|
|AREA|SRC_842|Cam_Valpo_236-PTAS|268.325|6.398.057|10 meses|307|4,1538E-14|3,2266E-15|7,9327E-14|3,4388E-14|7,831E-14|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 30. Escenario 1 - Descripción de las fuentes de emisión de volumen parte 23

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 41 de 56

|Tipo<br>AREA|ID<br>SRC_843|Descripción<br>Cam_Valpo_237-PTAS|X1|Y1|Ciclo<br>operación<br>10 meses|Área|PM10-As|PM10-Cd|PM10-Cr|PM10-Ni|PM10-Pb|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo<br>AREA|ID<br>SRC_843|Descripción<br>Cam_Valpo_237-PTAS|[m]<br>268.339|[m]<br>6.398.092|[m]<br>6.398.092|[m2]<br>154|[g/m2s]<br>8,2775E-14|[g/m2s]<br>6,4297E-15|[g/m2s]<br>1,5808E-13|[g/m2s]<br>6,8526E-14|[g/m2s]<br>1,5605E-13|
|AREA|SRC_844|Cam_Valpo_238-PTAS|268.362|6.398.151|10 meses|252|5,0712E-14|3,9391E-15|9,6846E-14|4,1982E-14|9,5604E-14|
|AREA|SRC_845|Cam_Valpo_239-PTAS|268.383|6.398.192|10 meses|185|6,8886E-14|5,3509E-15|1,3155E-13|5,7028E-14|1,2987E-13|
|AREA|SRC_846|Cam_Valpo_240-PTAS|268.355|6.398.247|10 meses|250|5,0992E-14|3,9609E-15|9,7381E-14|4,2214E-14|9,6132E-14|
|AREA|SRC_847|Cam_Valpo_241-PTAS|268.227|6.398.303|10 meses|567|2,2505E-14|1,7481E-15|4,2979E-14|1,8631E-14|4,2428E-14|
|AREA|SRC_848|Cam_Valpo_242-PTAS|268.140|6.398.362|10 meses|419|3,0458E-14|2,3659E-15|5,8167E-14|2,5215E-14|5,7421E-14|
|AREA|SRC_849|Cam_Valpo_243-PTAS|268.089|6.398.427|10 meses|325|3,92E-14|3,045E-15|7,4862E-14|3,2452E-14|7,3902E-14|
|AREA|SRC_850|Cam_Valpo_244-PTAS|268.005|6.398.483|10 meses|406|3,1409E-14|2,4398E-15|5,9983E-14|2,6002E-14|5,9214E-14|
|AREA|SRC_851|Cam_Valpo_245-PTAS|267.956|6.398.553|10 meses|338|3,7713E-14|2,9295E-15|7,2022E-14|3,1221E-14|7,1099E-14|
|AREA|SRC_852|Cam_Valpo_246-PTAS|267.920|6.398.673|10 meses|499|2,5567E-14|1,986E-15|4,8826E-14|2,1166E-14|4,82E-14|
|AREA|SRC_853|Cam_Valpo_247-PTAS|267.908|6.398.749|10 meses|308|4,1369E-14|3,2134E-15|7,9004E-14|3,4248E-14|7,7991E-14|
|AREA|SRC_854|Cam_Valpo_248-PTAS|267.894|6.398.771|10 meses|107|1,1877E-13|9,2256E-15|2,2682E-13|9,8324E-14|2,2391E-13|
|AREA|SRC_855|Cam_Valpo_249-PTAS|267.791|6.398.823|10 meses|467|2,7343E-14|2,1239E-15|5,2217E-14|2,2636E-14|5,1548E-14|
|AREA|SRC_856|Cam_Valpo_250-PTAS|267.747|6.398.849|10 meses|204|6,2534E-14|4,8574E-15|1,1942E-13|5,1769E-14|1,1789E-13|
|AREA|SRC_857|Cam_Valpo_251-PTAS|267.699|6.398.875|10 meses|217|5,8747E-14|4,5633E-15|1,1219E-13|4,8634E-14|1,1075E-13|
|AREA|SRC_858|Cam_Valpo_252-PTAS|267.673|6.398.943|10 meses|286|4,4618E-14|3,4658E-15|8,5209E-14|3,6937E-14|8,4116E-14|
|AREA|SRC_859|Cam_Valpo_253-PTAS|267.740|6.399.152|10 meses|872|1,463E-14|1,1364E-15|2,7939E-14|1,2111E-14|2,758E-14|
|AREA|SRC_860|Cam_Valpo_254-PTAS|267.754|6.399.259|10 meses|434|2,9369E-14|2,2813E-15|5,6086E-14|2,4313E-14|5,5367E-14|
|AREA|SRC_861|Cam_Valpo_255-PTAS|267.756|6.399.372|10 meses|453|2,8165E-14|2,1878E-15|5,3788E-14|2,3317E-14|5,3098E-14|
|AREA|SRC_862|Cam_Valpo_256-PTAS|267.702|6.399.478|10 meses|480|2,6575E-14|2,0643E-15|5,0751E-14|2,2E-14|5,01E-14|
|AREA|SRC_863|Cam_Valpo_257-PTAS|267.740|6.399.547|10 meses|307|4,1525E-14|3,2255E-15|7,9301E-14|3,4376E-14|7,8284E-14|
|AREA|SRC_864|Cam_Valpo_258-PTAS|267.742|6.399.624|10 meses|312|4,0946E-14|3,1805E-15|7,8195E-14|3,3897E-14|7,7193E-14|
|AREA|SRC_865|Cam_Valpo_259-PTAS|267.731|6.399.695|10 meses|288|4,4359E-14|3,4457E-15|8,4714E-14|3,6723E-14|8,3627E-14|
|AREA|SRC_866|Cam_Valpo_260-PTAS|267.682|6.399.788|10 meses|426|2,9967E-14|2,3278E-15|5,7229E-14|2,4808E-14|5,6495E-14|
|AREA|SRC_867|Cam_Valpo_261-PTAS|267.661|6.399.830|10 meses|187|6,8206E-14|5,298E-15|1,3025E-13|5,6464E-14|1,2858E-13|

ANEXO 1 - FUENTES DE EMISIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 42 de 56

**4** **ANEXO 2 - JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO**

**4.1** **JUSTIFICACIÓN DEL MODELO**

Para asegurar la calidad de la modelación tanto en los datos utilizados como en los resultados
obtenidos, se aplicaron criterios de buenas prácticas para modelos de calidad del aire. De
manera que toda la información de entrada como datos topográficos, datos observados y
configuraciones del modelo, permitan la reproducción de los resultados relevantes para la
evaluación por parte de la autoridad ambiental.

En concordancia con lo descrito en la Guía para el Uso de Modelos de Calidad del Aire en el
SEIA, los criterios de selección del modelo se basaron en el tipo de terreno en el cual se inserta
el proyecto en evaluación (plano o complejo) y el tipo de contaminante emitido al ambiente en
las distintas fases del proyecto.

El primer criterio asociado al tipo de terreno permite representar el impacto de las emisiones
del proyecto a partir de las condiciones meteorológicas locales del dominio de modelación
definido. Debido a que estas condiciones están vinculadas a las características topográficas
como orografía, uso de suelo, rugosidad superficial, presencia de cuerpos de agua, zona
costera, valle interior, entre otros. Por lo tanto, mientras más heterogéneas son las
características del área de interés, más complejo es el terreno y, en consecuencia, dado el
impacto en la meteorología local, más heterogénea (horizontal y verticalmente) es la
meteorología.

Tal como señala la Guía del SEA, a diferencia de otros países que cuentan en muchas partes
con terreno plano (con características homogéneas), las características de gran parte del
territorio chileno se debieran considerar complejas (heterogéneas). Por esta razón, se deben
considerar modelos capaces de representar esa heterogeneidad de la mejor manera posible.
En complemento a este criterio, señala que en el caso que se requiera estimar el impacto en
la calidad del aire a distancias mayores a 5 [km], lo más adecuado es utilizar un modelo que
permita simular meteorología heterogénea. Los modelos capaces de esto son los de tipo “puff”
o Eulerianos. El modelo tipo “puff” recomendado es el modelo CALPUFF.

Los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos
Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes
provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su
aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada punto
de una trayectoria; es decir, a diferencia de los modelos Langrangeanos que necesitan el
cálculo de un gran número de trayectorias para una fuente, los modelos tipo “puff” sólo
requieren una trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En el caso de
emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana de muchos “puffs”.

Debido a las características costeras de la región en donde se emplaza el proyecto en estudio,
cobra relevancia la capacidad del modelo de representar el comportamiento del viento sobre
las masas de agua y su interacción en la relación mar/tierra (Barclay, 2011), puesto que, podría
incrementar el potencial de impacto en receptores situados próximos a la instalación. Estas
condiciones de dispersión son abordadas con un modelo de tipo “puff” como CALPUFF.

ANEXO 2 - JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 43 de 56

Dado que este modelo no presenta limitaciones respecto a bajas velocidades de viento,
permitiendo al “puff” crecer y difundirse sin un efecto de advección. Tal característica permite
representar eventos de estancamiento en periodos con condición de calma donde los “puff” se
acumularían en función del tiempo. Por otro lado, es importante tener en consideración, que el
modelo CALPUFF permite una representación más realista de la dinámica de vientos en la
zona interés, al utilizar campos de vientos tridimensionales, propiedad ausente en un modelo
de tipo Gaussiano. A su vez, los modelos Gaussianos carecen de efecto memoria de los
contaminantes emitidos en horas previas, esta característica es de importancia en dominios
donde se presenten condiciones de vientos de baja velocidad o de calma (Barclay, 2011).

El segundo criterio para la selección del modelo es el tipo de contaminante a modelar. Debido
a que los contaminantes emitidos a la atmósfera en las distintas fases del proyecto
corresponden mayormente a contaminantes primarios, se justifica la aplicación de un modelo
como CALPUFF.

Con relación al modelo meteorológico utilizado, se consideró como criterio de selección las
características geográficas del área entorno al proyecto las que la definen como terreno
complejo de meteorología heterogénea. Debido principalmente a la presencia de masas de
aguas oceánicas, zona costera y condiciones topográficas que afectan la linealidad de las
emisiones generadas por el proyecto. Por lo anterior, se utilizó el campo meteorológico
tridimensional horario del año 2023. El cual fue generado utilizando el modelo meteorológico
WRF (v4.0) y procesado con MMIF (v3.3) para su uso directo en el modelo de calidad de aire
CALPUFF. Esto debido a que MMIF procesa los datos obtenidos de la simulación WRF a
formato requeridos para el ingreso directo al modelo de dispersión CALPUFF, como una
alternativa a CALMET (Brashers, 2014).

Adicionalmente, el procesamiento de la meteorología de pronóstico WRF usando CALMET no
es recomendable y genera un deterioro en el desempeño de la base meteorológica (Fox,
Clarification on EPA-FLM Recommended Settings for CALMET. U.S. Environmental Protection
Agency, 2009).

En estudios realizados por la EPA, se ha verificado que el desempeño del modelo
CALPUFF/MMIF y CALPUFF/CALMET es similar. Sin embargo, las variaciones del modelo de
predicción de CALPUFF usando MMIF son menores que las registradas usando CALMET
(Fox, Supplemental Information for EPA's 2009 Draft Report regarding Reassessment of IW
AQM Phase 2 Recommendations. U.S. Environmental Protection Agency, 2015).

ANEXO 2 - JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 44 de 56

**4.2** **DESCRIPCIÓN DEL MODELO**

Para la estimación del área de influencia y la cuantificación de impactos por olor, se aplicó el
software de modelación atmosférica Calpuff en su versión aprobada por la EPA 5.8.5, el cual
es señalado por la U.S. Environmental Protection Agency como modelo alternativo para la
evaluación de calidad del aire con propósitos regulatorios. El software se complementó con los
módulos de análisis numérico Calpost (7.2.1).

Para la simulación de campos de viento, temperaturas y otras variables meteorológicas, en un
dominio de modelación tridimensional, la Guía para el Uso de Modelos de Calidad del Aire en
el SEIA se señala que en el caso de utilizar Calpuff, se recomienda usar la información del
modelo de pronóstico directamente, sin usar el preprocesador Calmet. Por lo tanto, en
concordancia a lo anterior se utilizó el preprocesador meteorológico el modelo MMIF
(Mesoscale Model Interface Program) aprobado por U.S. EPA, en la generación de los campos
tridimensionales necesarios para la dispersión de emisiones en el modelo.

El módulo Calpuff es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario, que
permite representar la dispersión de una emisión continua como un número discreto de
paquetes de material de o los contaminantes modelados. De esta forma el modelo describe la
contribución de un “puff” en la concentración atmosférica de un receptor en un instante
determinado. Donde la concentración total en un receptor estará dada por la sumatoria de las
contribuciones de todos los “puff” (Scire, 2000).

**4.3** **PROCESO DE MODELACIÓN**

La primera etapa del proceso de modelación de calidad del aire corresponde al modelo
numérico meteorológico WRF, cuyo sistema de preprocesamiento (WPS) integra un conjunto
de programas para la preparación de los datos de entrada para el modelo meteorológico WRF.
Mediante Geogrid se preparan los datos geográficos, tales como uso de suelo y elevaciones
de terreno. Ungrib extrae campos meteorológicos globales de archivos con formato GRIB; y
Metgrid interpola horizontalmente los campos meteorológicos extraídos por Ungrib a las
cuadrículas del modelo definidas por Geogrid. El trabajo de interpolación vertical de campos
meteorológicos de WRF se realiza dentro del programa Real.

Posteriormente se aplica el programa WRF para el pronóstico de la meteorología en el dominio
caracterizado. Una vez terminada la simulación meteorológica, se aplica el procesador MMIF
para convertir los datos de salida WRF (WRF.OUT) al formato CALMET.DAT. Este archivo de
salida contiene la meteorología tridimensional utilizada por el modelo de dispersión CALPUFF,
para el cálculo de dispersión y transporte de contaminantes. En una grilla de cálculo, se
obtienen las concentraciones (CONC.DAT) provenientes de las fuentes de emisión y sus
respectivas tasas de emisión ingresadas.
Los resultados son obtenidos con el procesador CALPOST, para la interpolación de las
isolíneas de concentración en conjunto con las concentraciones en receptores discretos
definidos, basado en los criterios normativos aplicables.

ANEXO 2 - JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 6. Modelación de calidad de aire

Fuente: Are Project.

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 45 de 56

ANEXO 2 - JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 46 de 56

**5** **ANEXO 3 - RESPUESTAS ORGANISMOS AMBIENTALES (SMA, MMA)**

**5.1** **RESPUESTA MINISTERIO DEL MEDIO AMBIENTE**

ANEXO 3 - RESPUESTAS ORGANISMOS AMBIENTALES (SMA, MMA) **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 47 de 56

ANEXO 3 - RESPUESTAS ORGANISMOS AMBIENTALES (SMA, MMA) **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**5.2** **RESPUESTA SUPERINTENDENCIA DEL MEDIO AMBIENTE**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 48 de 56

ANEXO 3 - RESPUESTAS ORGANISMOS AMBIENTALES (SMA, MMA) **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 49 de 56

ANEXO 3 - RESPUESTAS ORGANISMOS AMBIENTALES (SMA, MMA) **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**6** **CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 50 de 56

**6.1** **DOMINIO DE MODELACIÓN**

La extensión del área de modelación, o dominio espacial, fue definida en función de la
magnitud del proyecto y de las emisiones identificadas en las 3 etapas del proyecto.
Considerando la presencia de receptores susceptibles de ser afectados en el área de
emplazamiento del proyecto.

El dominio definido corresponde a 62 x 62 [km], con un tamaño de celda de 1 [km], en
concordancia a lo solicitado por el Servicio de Evaluación Ambiental.

La justificación de la selección del año meteorológico según lo indicado en la Guía para el Uso
de Modelos de Calidad del Aire en el SEIA se basa en la elección del escenario que representa
las condiciones más desfavorables para la dispersión de los contaminantes. Esta elección se
fundamenta en el análisis de los datos observados de la estación meteorológica Puchuncaví,
seleccionada debido a su proximidad al proyecto en cuestión. Se enfocó principalmente en las
condiciones de calma, identificadas a través de la variable velocidad del viento, ya que estas
condiciones representan una dispersión menos efectiva de los contaminantes.

El resultado del análisis de las condiciones meteorológicas se presenta en la tabla adjunta.

Tabla 31. Análisis porcentual de vientos calmos - Estación Puchuncaví

|Año|% de vientos<br>calmos|% datos<br>válidos|
|---|---|---|
|2021|21,24|92,71%|
|2022|22,21|93,31%|
|2023|25,37|92,98%|

Con base en este análisis, se optó por utilizar los datos meteorológicos pronosticados para el
año 2023, debido que presentó mayor porcentaje de vientos de calma.

Los datos fueron obtenidos a partir del modelo WRF y preprocesados por MMIF. Estos datos
cubren un periodo anual y consideran 11 niveles verticales a partir del nivel superficial de 0
metros.

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 7. Dominio de modelación

Fuente: Elaborado por Are Project, basado en Google Earth 2024.

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 51 de 56

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 52 de 56

**6.2** **BASE METEOROLÓGICA**

**6.2.1** **PERIODO DE MODELACIÓN**

Basado en lo recomendado por la Guía del SEA, la simulación del modelo de dispersión
consideró un periodo anual 2023 completo, para representar la variabilidad climática relevante
de la zona de interés. Esto abarcando los rangos de variaciones horarias y estacionales para
asegurar la inclusión de las condiciones meteorológicas más desfavorables.

**6.2.2** **FUENTE DE DATOS METEOROLÓGICOS**

Existen dos tipos de datos meteorológicos: datos observados y datos generados por un modelo
numérico. En todos los tipos de modelaciones se requiere de ambos. A su vez, los datos
meteorológicos se dividen en datos en superficie y datos en altura. En Chile, la información de
ambos tipos es muchas veces escasa o inexistente.

Se recomienda que el porcentaje de datos válidos de las series de tiempo sea siempre superior
al 75% en un año y que los datos en superficie y altura cubran exactamente el mismo período.
Respecto a la información en altura, el nivel mínimo debiera cubrir los 200 [m]
aproximadamente, medidos desde la superficie.

Debido a que el dominio meteorológico definido no se dispone de suficiente información
superficial observada, para la caracterización adecuada de los campos de vientos locales, se
consideró la utilización de información generada por el modelo pronóstico WRF a partir de
datos FNL del último año disponible, correspondiente al año 2023. Por lo tanto, las estaciones
observadas validadas dentro del dominio fueron utilizadas como referencia para la evaluación
del modelo meteorológico en concordancia a lo señalado por la Guía del SEA (2012). La
comparación de las observaciones con las simulaciones del modelo de pronóstico en el punto
de medición permite evaluar la incertidumbre de los datos meteorológicos tridimensionales
generados y de los resultados del modelo de calidad del aire, siempre que estos datos
observados no sean usados como información de entrada del modelo de pronóstico.

**6.2.3** **DATOS TOPOGRÁFICOS Y DE USO DE SUELO**

La escasez de información meteorológica en altura representativa es una limitante a la hora
de evaluar cualquier modelo. El modelo numérico recomendado para la generación de datos
meteorológicos es el Weather Research and Forecasting Model (WRF). WRF es uno de los
modelos meteorológicos de pronóstico más avanzados y completos y es mantenido por el
National Center for Atmospheric Research (NCAR) y National Oceanic and Atmospheric
Administration (NOAA) de Estados Unidos. Además, como señala la Guía del SEA (2023), este
tipo de modelo se ha ocupado en la mayoría de los proyectos relacionados con modelación
atmosférica encargados por organismos estatales, respaldando su aplicación al contexto de
evaluación ambiental, siempre que la resolución horizontal de WRF sea de 1 [km].

De acuerdo a Schmitz et al. (2011), en el caso de los modelos tipo “puff” y Eulerianos, si bien
son capaces de representar meteorología heterogénea en el dominio de modelación, no tienen
un desempeño muy superior a los modelos Gaussianos si se utilizan con información
meteorológica de sólo una estación y un radiosondeo como información de entrada. Es por ello

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 53 de 56

que estos modelos debieran usarse únicamente con datos provenientes de un modelo
meteorológico de pronóstico. En el caso de CALPUFF, se recomienda usar la información del
modelo de pronóstico directa mente, sin usar el preprocesador CALMET.

La fuente de información topográfica del dominio de modelación considerado en CALPUFF
corresponde a cartas topográficas digitales adquiridos desde la base de “U.S. Geological
Survey (USGS) - Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010)” con
curvas de nivel de resolución 30 [arc-second], equivalente a 920 [m] aproximadamente.
Con relación al uso de suelo, el modelo meteorológico utilizó información satelital de la base
de datos “Moderate Resolution Imaging Spectroradiometer (MODIS)” para Sudamérica con
una resolución 15 [arc-second], equivalente a 465 [m] aproximadamente.

Figura 8. Elevación de terreno del dominio

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 9. Uso de suelo del dominio

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 54 de 56

**6.2.4** **CONFIGURACIÓN DEL MODELO**

Todos los modelos requieren ser configurados para su aplicación en cada caso específico.
Estas configuraciones determinan características como el periodo y dominio geográfico de la
simulación, resolución espacial horizontal y vertical, parametrizaciones físicas, formato de
resultados, entre otros. Dado que la distribución temporal y espacial de las concentraciones de
contaminantes depende en gran medida de la meteorología, las parametrizaciones de los
modelos meteorológicos (o pre-procesadores meteorológicos) requieren una atención
especial.

En concordancia a lo descrito en la Guía del SEA, se consideró la configuración por defecto
del modelo Calpuff, considerando además la misma resolución horizontal que la obtenida por
el modelo meteorológico WRF.

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**6.2.5** **PARAMETRIZACIÓN RECEPTORES**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 55 de 56

Tal como lo señala la Guía de Calidad del Aire: En el modelo se debe configurar una
cuadrícula o grilla de receptores, diferente de los receptores discretos. Al definir la grilla de
receptores más adecuada para el proyecto, se debe asegurar que el tamaño de esta sea lo
suficientemente grande para garantizar la cuantificación de la concentración máxima a nivel
del suelo (Servicio de Evaluación Ambiental, 2023).

Dado lo anterior, se utilizó la grilla anidada de receptores, cuya parametrización es la
siguiente, según lo que establece la Guía:

Tabla 32. Parametrización grilla 1 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.495|6.386.450|1,5|
|1.000|250|250|250|250|

Tabla 33. Parametrización grilla 2 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.306|6.385.136|1,5|
|1.000|250|250|250|250|

Tabla 34. Parametrización grilla 3 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.956|6.384.019|1,5|
|1.000|250|250|250|250|

Tabla 35. Parametrización grilla 4 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.714|6.382.885|1,5|
|1.000|250|250|250|250|

Tabla 36. Parametrización grilla 5 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|20.000|1.000|272.829|6.385.151|1,5|

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 56 de 56

**7** **BIBLIOGRAFÍA**

Barclay, J. S. (2011). _Generic Guidance and Optimum Model Settings for the CALPUFF_

_Modeling System for Inclusion into the Approved Methods for the Modeling and_
_Assessments of Air Pollutants in NSW, Australia. TRC Environmental Corporation._
Brashers, B. E. (2014). _Draft User’s Manual:The Mesoscale Model Interface Program (MMIF),_

_Version 3.1. U.S. Environmental Protection Agency._
Emery, C., Tai, E., & Yarwood, G. (2001). _Enhanced Meteorological Modeling and_

_Performance Evaluation for Two Texas Ozone Episodes, prepared for the Texas Natural_
_Resource Conservation Commission, prepared by ENVIRON International Corporation,_
_Novato, CA._
Environment Agency. (2002). _Integrated Pollution Prevention and Control (IPPC): Horizontal_

_Guidance for Odour - Part 2 - Assessment and control. Commissioning Organisation_
_Environment Agency._
Environment Agency. (2009). _Horizontal Guidance: Technical Guidance Note - H4 Odour_

_Management. Environment Agency._
ESVAL S.A. (2019). _Declaración de Impacto Ambiental: Proyecto Redes Primarias y Planta de_

_Tratamiento de Aguas Servidas Localidad de Maitencillo. GSI Ingeniería Ltda._ Chile.
Fox, T. (2009). _Clarification on EPA-FLM Recommended Settings for CALMET. U.S._

_Environmental Protection Agency._
Fox, T. (2015). _Supplemental Information for EPA's 2009 Draft Report regarding Reassessment_

_of IW AQM Phase 2 Recommendations. U.S. Environmental Protection Agency._
Gobierno Regional de Valparaíso. (2005). _Gobierno Regional de Valparaíso. 2005._

_Modificación Plan Intercomunal de Valparaíso. Comunas de Puchuncaví, Zapallar,_
_Papudo, La ligua - Satélite Borde Costero Norte. Secretaría Regional Ministerial de_
_Vivienda y Urbanismo V Región de Valparaíso._ Chile.
Municipalidad de Puchuncaví. (2011). _Decreto 1576: Aprueba Proyecto “Actualización Plan_

_Regulador, Comuna de Puchuncaví”. Comisión Regional de Medio Ambiente._ Chile.
Pielke, R. (1984). _Mesoscale Metereological Modeling. Academic Pess._ Orlando.
Pielke, R. (1984). _Mesoscale Metereological Modeling. Academic Pess._ Orlando.
Scire, J. S. (2000). _A User's Guide for the Calpuff Dispersión Model. Earth Tech, Inc._
Servicio de Evaluación Ambiental. (2012). _Guía par el Uso de Modelos de Calidad del Aire en_

_el SEIA. Ministerio del Medio Ambiente._ Chile.
Servicio de Evaluación Ambiental. (2012). _Guía para el uso de modelos de calidad del aire en_

_el SEIA._ Chile.
Servicio de Evaluación Ambiental. (2023). Guía para la evaluación ambiental de riesgo para la
salud de la población. _Ministerio del Medio Ambiente._ Chile.
Stauffer, D., & Seaman, N. (1990). _Use of Four - Dimensional Data assimilation in a limited -_

_Area Mesoscale Model. Part I: Experiments with Synoptic - scale Data._
Stauffer, D., & Seaman, N. (1990). _Use of Four - Dimensional Data assimilation in a limited -_

_Area Mesoscale Model. Part I: Experiments with Synoptic - scale Data._

BIBLIOGRAFÍA **www.arechile.com**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Concentración representativa de metales pesados en el suelo del área del Proyecto.**

| Contaminantes | Concentración en el suelo<br>mg/Kg | Col3 |
| --- | --- | --- |
| Contaminantes | Sector PTAS | Sector Redes |
| Arsénico | 15,19 | 14,29 |
| Cadmio | 0,55 | 1,11 |
| Cromo | 22,68 | 27,29 |
| Níquel | 10,68 | 11,83 |
| Plomo | 21,85 | 26,94 |

**Tabla 2.: Receptores discretos**

| ID | Coordenadas UTM [m]<br>(WGS84-H19S) | Col3 | Descripción |
| --- | --- | --- | --- |
| ID | X:Este | Y: Sur | Y: Sur |
| R1 | 273.467 | 6.387.304 | Receptor ruido 1 |
| R2 | 273.165 | 6.386.964 | Receptor ruido 2 |
| R3 | 272.667 | 6.386.718 | Receptor ruido 3 |
| R4 | 272.686 | 6.386.266 | Receptor ruido 4 |
| R5 | 272.095 | 6.386.403 | Receptor ruido 5 |
| R6 | 272.061 | 6.386.029 | Receptor ruido 6 |
| R7 | 272.062 | 6.385.336 | Receptor ruido 7 |
| R8 | 272.550 | 6.385.155 | Receptor ruido 8 |
| R9 | 272.361 | 6.384.963 | Receptor ruido 9 |
| R10 | 272.633 | 6.384.083 | Receptor ruido 10 |
| R11 | 271.742 | 6.385.511 | Receptor ruido 12 |
| R12 | 271.303 | 6.385.031 | Receptor ruido 13 |
| R13 | 270.870 | 6.384.346 | Receptor ruido 14 |
| R14 | 271.064 | 6.383.040 | Receptor ruido 15 |
| R15 | 271.195 | 6.382.539 | Receptor ruido 16 |
| R16 | 273.437 | 6.383.498 | Receptor fauna |
| R17 | 272.900 | 6.384.175 | Receptor olor 1 |
| R18 | 273.262 | 6.384.342 | Receptor olor 2 |
| R19 | 273.332 | 6.384.523 | Receptor olor 3 |
| R20 | 273.201 | 6.382.149 | Receptor olor 4 |
| R21 | 274.626 | 6.383.665 | Receptor olor 5 |
| R22 | 275.043 | 6.382.044 | Receptor olor 6 |
| R23 | 272.529 | 6.383.695 | Receptor olor 7 |
| R24 | 272.543 | 6.383.117 | Receptor olor 8 |
| R25 | 272.512 | 6.382.513 | Receptor olor 9 |
| R26 | 274.379 | 6.377.371 | Estación Puchuncaví |

**Tabla 3.: Límite normativo por contaminante**

| Escenario de<br>modelación | Contaminante | Normativa de referencia | Tipo de Norma | Unidad | Tipo | Límite |
| --- | --- | --- | --- | --- | --- | --- |
| E1: Escenario 1 | Arsénico (As) | Real Decreto 102/20112 | Primaria | [ng/m3] | Anual | 6 |
| E1: Escenario 1 | Cadmio (Cd) | Real Decreto 102/2011 | Primaria | [ng/m3] | Anual | 5 |
| E1: Escenario 1 | Cadmio (Cd) | OMS3 | Primaria | [ng/m3] | Anual | 5 |
| E1: Escenario 1 | Níquel (Ni) | Real Decreto 102/2011 | Primaria | [ng/m3] | Anual | 20 |
| E1: Escenario 1 | Plomo (Pb) | D.S. N°136/20004 | Primaria | [ng/m3] | Anual | 500 |
| E1: Escenario 1 | Plomo (Pb) | Real Decreto 102/2011 | Primaria | [ng/m3] | Anual | 500 |
| E1: Escenario 1 | Plomo (Pb) | OMS | Primaria | [ng/m3] | Anual | 500 |
| E1: Escenario 1 | Cromo (Cr) | Nueva Zelandia AAQG5 | Primaria | [ng/m3] | Anual | 110 |

**Tabla 4.: Concentraciones de metales pesados en receptores sensibles parte 1**

| Contaminante | Tipo de Norma | Unidad | Tipo | Límite | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Arsénico (As) | Primaria | [ng/m3] | Anual | 6 | 0,0003 | 0,0004 | 0,0023 | 0,0004 | 0,0004 | 0,0004 | 0,0044 | 0,0008 | 0,0021 | 0,0023 | 0,0143 | 0,0021 |
| Cadmio (Cd) | Primaria | [ng/m3] | Anual | 5 | 0,0000 | 0,0000 | 0,0002 | 0,0000 | 0,0000 | 0,0000 | 0,0003 | 0,0001 | 0,0002 | 0,0002 | 0,0011 | 0,0002 |
| Níquel (Ni) | Primaria | [ng/m3] | Anual | 20 | 0,0003 | 0,0003 | 0,0019 | 0,0003 | 0,0003 | 0,0003 | 0,0037 | 0,0006 | 0,0017 | 0,0019 | 0,0118 | 0,0018 |
| Plomo (Pb) | Primaria | [ng/m3] | Anual | 500 | 0,0006 | 0,0006 | 0,0043 | 0,0007 | 0,0007 | 0,0007 | 0,0083 | 0,0014 | 0,0038 | 0,0042 | 0,0269 | 0,0040 |
| Plomo (Pb)* | Primaria | [ng/m3] | Anual | 500 | 0,0006 | 0,0006 | 0,0042 | 0,0007 | 0,0007 | 0,0007 | 0,0083 | 0,0014 | 0,0038 | 0,0042 | 0,0267 | 0,0040 |
| Cromo (Cr) | Primaria | [ng/m3] | Anual | 110 | 0,0006 | 0,0006 | 0,0043 | 0,0007 | 0,0007 | 0,0008 | 0,0084 | 0,0014 | 0,0038 | 0,0043 | 0,0273 | 0,0041 |

**Tabla 5.: Concentraciones de metales pesados en receptores sensibles parte 2**

| Contaminante | Tipo de Norma | Unidad | Tipo | Límite | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Arsénico (As) | Primaria | [ng/m3] | Anual | 6 | 0,0123 | 0,0004 | 0,0002 | 0,0129 | 0,0018 | 0,0022 | 0,0019 | 0,0017 | 0,0058 | 0,0025 | 0,0016 | 0,0009 | 0,0006 |
| Cadmio (Cd) | Primaria | [ng/m3] | Anual | 5 | 0,0010 | 0,0000 | 0,0000 | 0,0006 | 0,0001 | 0,0001 | 0,0001 | 0,0001 | 0,0002 | 0,0001 | 0,0001 | 0,0001 | 0,0000 |
| Níquel (Ni) | Primaria | [ng/m3] | Anual | 20 | 0,0102 | 0,0003 | 0,0001 | 0,0095 | 0,0014 | 0,0016 | 0,0014 | 0,0012 | 0,0042 | 0,0018 | 0,0013 | 0,0007 | 0,0004 |
| Plomo (Pb) | Primaria | [ng/m3] | Anual | 500 | 0,0232 | 0,0007 | 0,0003 | 0,0201 | 0,0030 | 0,0035 | 0,0030 | 0,0026 | 0,0086 | 0,0037 | 0,0028 | 0,0016 | 0,0009 |
| Plomo (Pb)* | Primaria | [ng/m3] | Anual | 500 | 0,0231 | 0,0007 | 0,0003 | 0,0201 | 0,0030 | 0,0035 | 0,0030 | 0,0026 | 0,0086 | 0,0037 | 0,0028 | 0,0016 | 0,0009 |
| Cromo (Cr) | Primaria | [ng/m3] | Anual | 110 | 0,0235 | 0,0007 | 0,0003 | 0,0207 | 0,0031 | 0,0036 | 0,0031 | 0,0027 | 0,0089 | 0,0039 | 0,0029 | 0,0017 | 0,0010 |

**Tabla 6: Línea base estación de calidad del aire Puchuncaví año 2022**

| Contaminante | Promedio<br>Anual (ng/m3) | N° registros<br>para el<br>periodo anual | N° datos<br>válidos | Porcentaje de<br>completitud de<br>datos válidos |
| --- | --- | --- | --- | --- |
| Arsénico (As) | 7,31000 | 122 | 121 | 99.2% |
| Cadmio (Cd) | 1,00000 | 122 | 121 | 99.2% |
| Níquel (Ni) | 12,18000 | 122 | 121 | 99.2% |
| Plomo (Pb) | 5,51000 | 122 | 121 | 99.2% |
| Cromo (Cr) | 13,08000 | 122 | 121 | 99.2% |

**Tabla 7: Aumento de las concentraciones basales en EMRP Puchuncaví**

| Contaminante | Tipo de Norma | Estadístico | Medido EMRP<br>Puchuncaví<br>[ng/m3] | Modelado<br>EMRP<br>Puchuncaví<br>[ng/m3] | Total Aporte<br>proyecto +<br>línea base<br>[ng/m3] | Límite Norma |
| --- | --- | --- | --- | --- | --- | --- |
| Arsénico (As) | Primaria | Promedio<br>Anual | 7,31000 | 0,00025 | 7,31025 | 6 |
| Cadmio (Cd) | Primaria | Promedio<br>Anual | 1,00000 | 0,00001 | 1,00001 | 5 |
| Níquel (Ni) | Primaria | Promedio<br>Anual | 12,18000 | 0,00019 | 12,18019 | 20 |
| Plomo (Pb) | Primaria | Promedio<br>Anual | 5,51000 | 0,00041 | 5,51041 | 500 |
| Cromo (Cr) | Primaria | Promedio<br>Anual | 13,08000 | 0,00042 | 13,08042 | 110 |

**Tabla 8.: Escenario 1 - Descripción de las fuentes de emisión de área parte 1**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_1 | Peas_1 | 270.862 | 6.384.348 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_2 | Peas_2 | 271.312 | 6.385.052 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_3 | Peas_3 | 272.644 | 6.386.732 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_4 | Peas_5.1 | 271.757 | 6.385.539 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_5 | Peas_5.2 | 272.602 | 6.384.124 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_6 | Colec_1.1 | 270.894 | 6.383.950 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_7 | Colec_1.2 | 270.876 | 6.384.052 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_8 | Colec_1.3 | 270.873 | 6.384.151 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_9 | Colec_1.4 | 270.873 | 6.384.253 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_10 | Col_1_2.1 | 270.931 | 6.384.850 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_11 | Col_1_2.2 | 271.016 | 6.384.942 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_12 | Col_1_2.3 | 271.106 | 6.384.990 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_13 | Col_1_2.4 | 271.203 | 6.385.001 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_14 | Colec_2.1 | 271.534 | 6.385.454 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_15 | Colec_2.2 | 271.640 | 6.385.468 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_16 | Colec_2.3 | 271.734 | 6.385.512 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_17 | Colec_5.1.1 | 271.798 | 6.385.551 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_18 | Colec_5.1.2 | 271.860 | 6.385.633 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_19 | Colec_5.1.3 | 271.915 | 6.385.715 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_20 | Colec_5.1.4 | 271.973 | 6.385.798 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_21 | Colec_5.1.5 | 272.032 | 6.385.882 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_22 | Colec_5.1.6 | 272.063 | 6.385.983 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_23 | Colec_5.1.7 | 272.071 | 6.386.082 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_24 | Colec_5.1.8 | 272.080 | 6.386.180 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_25 | Colec_5.1.9 | 272.092 | 6.386.283 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_26 | Colec_5.1.10 | 272.101 | 6.386.381 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_27 | Colec_5.1.11 | 272.112 | 6.386.484 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_28 | Colec_5.1.12 | 272.122 | 6.386.584 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_29 | Colec_5.1.13 | 272.132 | 6.386.683 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_30 | Colec_5.1.14 | 272.171 | 6.386.767 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |

**Tabla 9.: Escenario 1 - Descripción de las fuentes de emisión de área parte 2**

| Tipo<br>AREA | ID<br>SRC_31 | Descripción<br>Colec_5.1.15 | X1 | Y1 | Ciclo<br>operación<br>1 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_31 | Descripción<br>Colec_5.1.15 | [m]<br>272.225 | [m]<br>6.386.788 | [m]<br>6.386.788 | [m2]<br>4 | [g/m2s]<br>3,323E-08 | [g/m2s]<br>2,5812E-09 | [g/m2s]<br>6,346E-08 | [g/m2s]<br>2,7509E-08 | [g/m2s]<br>6,2646E-08 |
| AREA | SRC_32 | Imp_1.1 | 270.869 | 6.384.373 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_33 | Imp_1.2 | 270.883 | 6.384.472 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_34 | Imp_1.3 | 270.915 | 6.384.567 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_35 | Imp_1.4 | 270.907 | 6.384.662 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_36 | Imp_1.5 | 270.863 | 6.384.741 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_37 | Imp_2.1 | 271.310 | 6.385.050 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_38 | Imp_2.2 | 271.349 | 6.385.137 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_39 | Imp_2.3 | 271.379 | 6.385.235 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_40 | Imp_2.4 | 271.425 | 6.385.313 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_41 | Imp_2.5 | 271.473 | 6.385.362 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_42 | Imp_3.1 | 272.362 | 6.386.742 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_43 | Imp_3.2 | 272.478 | 6.386.683 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_44 | Imp_3.3 | 272.646 | 6.386.701 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_45 | Imp_5.1.1 | 271.781 | 6.385.537 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_46 | Imp_5.1.2 | 271.876 | 6.385.511 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_47 | Imp_5.1.3 | 271.846 | 6.385.422 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_48 | Imp_5.1.4 | 271.858 | 6.385.339 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_49 | Imp_5.1.5 | 271.954 | 6.385.328 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_50 | Imp_5.1.6 | 272.056 | 6.385.329 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_51 | Imp_5.1.7 | 272.156 | 6.385.329 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_52 | Imp_5.1.8 | 272.220 | 6.385.336 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_53 | Imp_5.1.9 | 272.311 | 6.385.344 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_54 | Imp_5.1.10 | 272.285 | 6.385.236 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_55 | Imp_5.1.11 | 272.304 | 6.385.134 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_56 | Imp_5.1.12 | 272.336 | 6.385.038 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_57 | Imp_5.1.13 | 272.407 | 6.384.841 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_58 | Imp_5.1.14 | 272.372 | 6.384.937 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_59 | Imp_5.1.15 | 272.450 | 6.384.738 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_60 | Imp_5.1.16 | 272.488 | 6.384.641 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |

**Tabla 10.: Escenario 1 - Descripción de las fuentes de emisión de área parte 3**

| Tipo<br>AREA | ID<br>SRC_61 | Descripción<br>Imp_5.1.17 | X1 | Y1 | Ciclo<br>operación<br>1 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_61 | Descripción<br>Imp_5.1.17 | [m]<br>272.524 | [m]<br>6.384.542 | [m]<br>6.384.542 | [m2]<br>4 | [g/m2s]<br>3,323E-08 | [g/m2s]<br>2,5812E-09 | [g/m2s]<br>6,346E-08 | [g/m2s]<br>2,7509E-08 | [g/m2s]<br>6,2646E-08 |
| AREA | SRC_62 | Imp_5.1.18 | 272.555 | 6.384.455 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_63 | Imp_5.1.19 | 272.599 | 6.384.360 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_64 | Imp_5.1.20 | 272.630 | 6.384.265 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_65 | Imp_5.2.1 | 272.632 | 6.384.030 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_66 | Imp_5.2.2 | 272.629 | 6.383.932 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_67 | Imp_5.2.3 | 272.630 | 6.383.829 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_68 | Imp_5.2.4 | 272.630 | 6.383.727 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_69 | Imp_5.2.5 | 272.640 | 6.383.641 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_70 | Imp_5.2.6 | 272.746 | 6.383.639 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_71 | Imp_5.2.7 | 272.851 | 6.383.632 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_72 | Imp_5.2.8 | 272.942 | 6.383.633 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_73 | Imp_5.2.9 | 273.063 | 6.383.633 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_74 | Imp_5.2.10 | 273.174 | 6.383.643 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_75 | Imp_5.2.11 | 273.241 | 6.383.541 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_76 | Imp_5.2.12 | 273.289 | 6.383.443 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_77 | Imp_5.2.13 | 273.365 | 6.383.370 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_78 | Imp_5.2.14 | 273.435 | 6.383.287 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_79 | Imp_5.2.15 | 273.517 | 6.383.233 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_80 | Imp_5.2.16 | 273.550 | 6.383.131 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_81 | IF_1_Redes | 272.317 | 6.384.978 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_82 | IF_2_PTAS | 273.520 | 6.383.274 | 10 meses | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_83 | Tub_1.1 | 272.633 | 6.383.633 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_84 | Tub_1.2 | 272.635 | 6.383.539 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_85 | Tub_1.3 | 272.525 | 6.383.555 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_86 | Tub_1.4 | 272.458 | 6.383.630 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_87 | Tub_1.5 | 272.378 | 6.383.683 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_88 | Tub_1.6 | 272.300 | 6.383.735 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_89 | Tub_1.7 | 272.197 | 6.383.722 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_90 | Tub_1.8 | 272.122 | 6.383.755 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |

**Tabla 11.: Escenario 1 - Descripción de las fuentes de emisión de área parte 4**

| Tipo<br>AREA | ID<br>SRC_91 | Descripción<br>Tub_1.9 | X1 | Y1 | Ciclo<br>operación<br>1 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_91 | Descripción<br>Tub_1.9 | [m]<br>272.060 | [m]<br>6.383.844 | [m]<br>6.383.844 | [m2]<br>4 | [g/m2s]<br>3,323E-08 | [g/m2s]<br>2,5812E-09 | [g/m2s]<br>6,346E-08 | [g/m2s]<br>2,7509E-08 | [g/m2s]<br>6,2646E-08 |
| AREA | SRC_92 | Tub_1.10 | 271.961 | 6.383.846 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_93 | Tub_1.11 | 271.862 | 6.383.794 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_94 | Tub_1.12 | 271.766 | 6.383.745 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_95 | Tub_1.13 | 271.669 | 6.383.720 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_96 | Tub_1.14 | 271.564 | 6.383.688 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_97 | Tub_1.15 | 271.501 | 6.383.601 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_98 | Tub_1.16 | 271.424 | 6.383.524 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_99 | Tub_1.17 | 271.369 | 6.383.436 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_100 | Tub_1.18 | 271.340 | 6.383.353 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_101 | Tub_1.19 | 271.274 | 6.383.286 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_102 | Tub_1.20 | 271.248 | 6.383.193 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_103 | Tub_1.21 | 271.205 | 6.383.096 | 1 mes | 4 | 3,323E-08 | 2,5812E-09 | 6,346E-08 | 2,7509E-08 | 6,2646E-08 |
| AREA | SRC_537 | PTAS | 273.586 | 6.383.219 | 10 meses | 4 | 3,4547E-07 | 1,2509E-08 | 5,1581E-07 | 2,429E-07 | 4,9694E-07 |
| AREA | SRC_209 | Cam_Cat_1-PEAS e Imp | 273.043 | 6.387.323 | 3 mes | 383 | 1,2384E-12 | 9,6195E-14 | 2,365E-12 | 1,0252E-12 | 2,3347E-12 |
| AREA | SRC_210 | Cam_Cat_2-PEAS e Imp | 273.206 | 6.387.558 | 3 mes | 1.145 | 4,1458E-13 | 3,2203E-14 | 7,9174E-13 | 3,4321E-13 | 7,8159E-13 |
| AREA | SRC_211 | Cam_Cat_3-PEAS e Imp | 273.308 | 6.387.612 | 3 mes | 456 | 1,041E-12 | 8,0864E-14 | 1,9881E-12 | 8,6182E-13 | 1,9626E-12 |
| AREA | SRC_212 | Cam_Cat_4-PEAS e Imp | 273.511 | 6.387.668 | 3 mes | 844 | 5,6274E-13 | 4,3711E-14 | 1,0747E-12 | 4,6586E-13 | 1,0609E-12 |
| AREA | SRC_213 | Cam_Cat_5-PEAS e Imp | 273.721 | 6.387.707 | 3 mes | 853 | 5,5631E-13 | 4,3212E-14 | 1,0624E-12 | 4,6054E-13 | 1,0488E-12 |
| AREA | SRC_214 | Cam_Cat_6-PEAS e Imp | 273.880 | 6.387.880 | 3 mes | 945 | 5,022E-13 | 3,9009E-14 | 9,5907E-13 | 4,1575E-13 | 9,4677E-13 |
| AREA | SRC_215 | Cam_Cat_7-PEAS e Imp | 273.982 | 6.387.934 | 3 mes | 458 | 1,0376E-12 | 8,0595E-14 | 1,9815E-12 | 8,5896E-13 | 1,9561E-12 |
| AREA | SRC_216 | Cam_Cat_8-PEAS e Imp | 274.178 | 6.387.916 | 3 mes | 782 | 6,0689E-13 | 4,7141E-14 | 1,159E-12 | 5,0242E-13 | 1,1441E-12 |
| AREA | SRC_217 | Cam_Cat_9-PEAS e Imp | 274.216 | 6.387.945 | 3 mes | 195 | 2,4284E-12 | 1,8863E-13 | 4,6377E-12 | 2,0104E-12 | 4,5782E-12 |
| AREA | SRC_218 | Cam_Cat_10-PEAS e Imp | 274.213 | 6.388.017 | 3 mes | 296 | 1,6059E-12 | 1,2474E-13 | 3,0668E-12 | 1,3294E-12 | 3,0275E-12 |
| AREA | SRC_219 | Cam_Cat_11-PEAS e Imp | 274.177 | 6.388.250 | 3 mes | 942 | 5,0419E-13 | 3,9164E-14 | 9,6287E-13 | 4,174E-13 | 9,5052E-13 |
| AREA | SRC_220 | Cam_Cat_12-PEAS e Imp | 274.185 | 6.388.365 | 3 mes | 458 | 1,0357E-12 | 8,0451E-14 | 1,9779E-12 | 8,5742E-13 | 1,9526E-12 |
| AREA | SRC_221 | Cam_Cat_13-PEAS e Imp | 274.352 | 6.388.558 | 3 mes | 1.017 | 4,6681E-13 | 3,626E-14 | 8,9148E-13 | 3,8645E-13 | 8,8005E-13 |
| AREA | SRC_222 | Cam_Cat_14-PEAS e Imp | 274.654 | 6.388.846 | 3 mes | 1.667 | 2,8477E-13 | 2,212E-14 | 5,4383E-13 | 2,3575E-13 | 5,3686E-13 |
| AREA | SRC_223 | Cam_Cat_15-PEAS e Imp | 274.745 | 6.388.895 | 3 mes | 410 | 1,1584E-12 | 8,9979E-14 | 2,2122E-12 | 9,5896E-13 | 2,1838E-12 |
| AREA | SRC_224 | Cam_Cat_16-PEAS e Imp | 274.834 | 6.388.862 | 3 mes | 371 | 1,2791E-12 | 9,9359E-14 | 2,4428E-12 | 1,0589E-12 | 2,4115E-12 |
| AREA | SRC_225 | Cam_Cat_17-PEAS e Imp | 274.882 | 6.388.794 | 3 mes | 331 | 1,4329E-12 | 1,113E-13 | 2,7365E-12 | 1,1862E-12 | 2,7014E-12 |
| AREA | SRC_226 | Cam_Cat_18-PEAS e Imp | 274.979 | 6.388.768 | 3 mes | 407 | 1,1674E-12 | 9,0681E-14 | 2,2294E-12 | 9,6644E-13 | 2,2008E-12 |
| AREA | SRC_227 | Cam_Cat_19-PEAS e Imp | 275.069 | 6.388.799 | 3 mes | 384 | 1,2357E-12 | 9,5985E-14 | 2,3599E-12 | 1,023E-12 | 2,3296E-12 |
| AREA | SRC_228 | Cam_Cat_20-PEAS e Imp | 275.059 | 6.388.911 | 3 mes | 460 | 1,0331E-12 | 8,0245E-14 | 1,9729E-12 | 8,5522E-13 | 1,9476E-12 |
| AREA | SRC_229 | Cam_Cat_21-PEAS e Imp | 275.040 | 6.389.003 | 3 mes | 374 | 1,2691E-12 | 9,858E-14 | 2,4236E-12 | 1,0506E-12 | 2,3926E-12 |
| AREA | SRC_230 | Cam_Cat_22-PEAS e Imp | 274.958 | 6.389.092 | 3 mes | 489 | 9,7057E-13 | 7,5391E-14 | 1,8535E-12 | 8,0349E-13 | 1,8297E-12 |

**Tabla 12.: Escenario 1 - Descripción de las fuentes de emisión de área parte 5**

| Tipo<br>AREA | ID<br>SRC_231 | Descripción<br>Cam_Cat_23-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_231 | Descripción<br>Cam_Cat_23-PEAS e Imp | [m]<br>274.915 | [m]<br>6.389.184 | [m]<br>6.389.184 | [m2]<br>402 | [g/m2s]<br>1,1803E-12 | [g/m2s]<br>9,168E-14 | [g/m2s]<br>2,254E-12 | [g/m2s]<br>9,771E-13 | [g/m2s]<br>2,2251E-12 |
| AREA | SRC_232 | Cam_Cat_24-PEAS e Imp | 274.946 | 6.389.307 | 3 mes | 503 | 9,4416E-13 | 7,3339E-14 | 1,8031E-12 | 7,8162E-13 | 1,78E-12 |
| AREA | SRC_233 | Cam_Cat_25-PEAS e Imp | 275.049 | 6.389.374 | 3 mes | 485 | 9,7867E-13 | 7,602E-14 | 1,869E-12 | 8,1019E-13 | 1,845E-12 |
| AREA | SRC_234 | Cam_Cat_26-PEAS e Imp | 275.181 | 6.389.406 | 3 mes | 541 | 8,7688E-13 | 6,8113E-14 | 1,6746E-12 | 7,2592E-13 | 1,6531E-12 |
| AREA | SRC_235 | Cam_Cat_27-PEAS e Imp | 275.286 | 6.389.385 | 3 mes | 424 | 1,1187E-12 | 8,6896E-14 | 2,1364E-12 | 9,2611E-13 | 2,109E-12 |
| AREA | SRC_236 | Cam_Cat_28-PEAS e Imp | 275.372 | 6.389.387 | 3 mes | 345 | 1,3757E-12 | 1,0686E-13 | 2,6273E-12 | 1,1389E-12 | 2,5936E-12 |
| AREA | SRC_237 | Cam_Cat_29-PEAS e Imp | 275.519 | 6.389.442 | 3 mes | 633 | 7,4963E-13 | 5,8229E-14 | 1,4316E-12 | 6,2058E-13 | 1,4132E-12 |
| AREA | SRC_238 | Cam_Cat_30-PEAS e Imp | 275.575 | 6.389.512 | 3 mes | 360 | 1,3173E-12 | 1,0232E-13 | 2,5157E-12 | 1,0905E-12 | 2,4835E-12 |
| AREA | SRC_239 | Cam_Cat_31-PEAS e Imp | 275.579 | 6.389.623 | 3 mes | 447 | 1,0613E-12 | 8,2435E-14 | 2,0267E-12 | 8,7856E-13 | 2,0007E-12 |
| AREA | SRC_240 | Cam_Cat_32-PEAS e Imp | 275.473 | 6.389.738 | 3 mes | 630 | 7,5399E-13 | 5,8568E-14 | 1,4399E-12 | 6,242E-13 | 1,4215E-12 |
| AREA | SRC_241 | Cam_Cat_33-PEAS e Imp | 275.397 | 6.389.809 | 3 mes | 419 | 1,1325E-12 | 8,7967E-14 | 2,1627E-12 | 9,3752E-13 | 2,135E-12 |
| AREA | SRC_242 | Cam_Cat_34-PEAS e Imp | 275.382 | 6.389.918 | 3 mes | 433 | 1,0969E-12 | 8,5202E-14 | 2,0947E-12 | 9,0805E-13 | 2,0679E-12 |
| AREA | SRC_243 | Cam_Cat_35-PEAS e Imp | 275.487 | 6.390.018 | 3 mes | 577 | 8,2322E-13 | 6,3945E-14 | 1,5721E-12 | 6,815E-13 | 1,552E-12 |
| AREA | SRC_244 | Cam_Cat_36-PEAS e Imp | 275.630 | 6.390.045 | 3 mes | 576 | 8,2366E-13 | 6,3979E-14 | 1,573E-12 | 6,8187E-13 | 1,5528E-12 |
| AREA | SRC_245 | Cam_Cat_37-PEAS e Imp | 275.763 | 6.390.025 | 3 mes | 533 | 8,9073E-13 | 6,9189E-14 | 1,7011E-12 | 7,3739E-13 | 1,6792E-12 |
| AREA | SRC_246 | Cam_Cat_38-PEAS e Imp | 275.861 | 6.389.993 | 3 mes | 412 | 1,153E-12 | 8,9562E-14 | 2,2019E-12 | 9,5452E-13 | 2,1737E-12 |
| AREA | SRC_247 | Cam_Cat_39-PEAS e Imp | 276.044 | 6.389.963 | 3 mes | 743 | 6,3902E-13 | 4,9637E-14 | 1,2204E-12 | 5,2901E-13 | 1,2047E-12 |
| AREA | SRC_248 | Cam_Cat_40-PEAS e Imp | 276.114 | 6.389.925 | 3 mes | 317 | 1,4977E-12 | 1,1634E-13 | 2,8602E-12 | 1,2399E-12 | 2,8235E-12 |
| AREA | SRC_249 | Cam_Cat_41-PEAS e Imp | 276.133 | 6.389.885 | 3 mes | 173 | 2,745E-12 | 2,1323E-13 | 5,2423E-12 | 2,2725E-12 | 5,1751E-12 |
| AREA | SRC_250 | Cam_Cat_42-PEAS e Imp | 276.158 | 6.389.818 | 3 mes | 287 | 1,6549E-12 | 1,2855E-13 | 3,1605E-12 | 1,37E-12 | 3,12E-12 |
| AREA | SRC_251 | Cam_Cat_43-PEAS e Imp | 276.157 | 6.389.659 | 3 mes | 633 | 7,5012E-13 | 5,8267E-14 | 1,4325E-12 | 6,2099E-13 | 1,4142E-12 |
| AREA | SRC_252 | Cam_Cat_44-PEAS e Imp | 276.172 | 6.389.529 | 3 mes | 521 | 9,1098E-13 | 7,0762E-14 | 1,7397E-12 | 7,5416E-13 | 1,7174E-12 |
| AREA | SRC_253 | Cam_Cat_45-PEAS e Imp | 276.275 | 6.389.477 | 3 mes | 468 | 1,0136E-12 | 7,8736E-14 | 1,9358E-12 | 8,3914E-13 | 1,911E-12 |
| AREA | SRC_254 | Cam_Cat_46-PEAS e Imp | 276.411 | 6.389.458 | 3 mes | 553 | 8,5785E-13 | 6,6635E-14 | 1,6383E-12 | 7,1017E-13 | 1,6173E-12 |
| AREA | SRC_255 | Cam_Cat_47-PEAS e Imp | 276.501 | 6.389.471 | 3 mes | 366 | 1,2962E-12 | 1,0068E-13 | 2,4753E-12 | 1,073E-12 | 2,4436E-12 |
| AREA | SRC_256 | Cam_Cat_48-PEAS e Imp | 276.706 | 6.389.673 | 3 mes | 1.151 | 4,1227E-13 | 3,2024E-14 | 7,8732E-13 | 3,413E-13 | 7,7722E-13 |
| AREA | SRC_257 | Cam_Cat_49-PEAS e Imp | 277.353 | 6.390.498 | 3 mes | 4.195 | 1,1315E-13 | 8,7891E-15 | 2,1609E-13 | 9,3671E-14 | 2,1331E-13 |
| AREA | SRC_258 | Cam_Cat_50-PEAS e Imp | 277.494 | 6.390.575 | 3 mes | 640 | 7,4169E-13 | 5,7612E-14 | 1,4164E-12 | 6,1401E-13 | 1,3983E-12 |
| AREA | SRC_259 | Cam_Cat_51-PEAS e Imp | 279.440 | 6.391.244 | 3 mes | 8.224 | 5,7725E-14 | 4,4839E-15 | 1,1024E-13 | 4,7788E-14 | 1,0882E-13 |
| AREA | SRC_260 | Cam_Cat_52-PEAS e Imp | 283.346 | 6.393.239 | 3 mes | 17.541 | 2,7063E-14 | 2,1022E-15 | 5,1683E-14 | 2,2404E-14 | 5,102E-14 |

**Tabla 13.: Escenario 1 - Descripción de las fuentes de emisión de área parte 6**

| Tipo<br>AREA | ID<br>SRC_261 | Descripción<br>Cam_Cat_53-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_261 | Descripción<br>Cam_Cat_53-PEAS e Imp | [m]<br>287.745 | [m]<br>6.394.661 | [m]<br>6.394.661 | [m2]<br>18.483 | [g/m2s]<br>2,5683E-14 | [g/m2s]<br>1,995E-15 | [g/m2s]<br>4,9048E-14 | [g/m2s]<br>2,1262E-14 | [g/m2s]<br>4,8419E-14 |
| AREA | SRC_262 | Cam_Pta_1-PEAS e Imp | 273.147 | 6.383.634 | 3 mes | 1.866 | 2,7036E-13 | 9,7892E-15 | 4,0367E-13 | 1,9009E-13 | 3,889E-13 |
| AREA | SRC_263 | Cam_Pta_2-PEAS e Imp | 273.165 | 6.383.642 | 3 mes | 81 | 6,2414E-12 | 2,2599E-13 | 9,319E-12 | 4,3883E-12 | 8,978E-12 |
| AREA | SRC_264 | Cam_Pta_3-PEAS e Imp | 273.189 | 6.383.637 | 3 mes | 94 | 5,3601E-12 | 1,9408E-13 | 8,003E-12 | 3,7686E-12 | 7,7102E-12 |
| AREA | SRC_265 | Cam_Pta_4-PEAS e Imp | 273.241 | 6.383.562 | 3 mes | 360 | 1,4019E-12 | 5,0759E-14 | 2,0931E-12 | 9,8564E-13 | 2,0165E-12 |
| AREA | SRC_266 | Cam_Pta_5-PEAS e Imp | 273.289 | 6.383.445 | 3 mes | 506 | 9,981E-13 | 3,6139E-14 | 1,4902E-12 | 7,0176E-13 | 1,4357E-12 |
| AREA | SRC_267 | Cam_Pta_6-PEAS e Imp | 273.304 | 6.383.402 | 3 mes | 180 | 2,8093E-12 | 1,0172E-13 | 4,1945E-12 | 1,9752E-12 | 4,041E-12 |
| AREA | SRC_268 | Cam_Pta_7-PEAS e Imp | 273.331 | 6.383.382 | 3 mes | 138 | 3,6448E-12 | 1,3197E-13 | 5,442E-12 | 2,5627E-12 | 5,2429E-12 |
| AREA | SRC_269 | Cam_Pta_8-PEAS e Imp | 273.361 | 6.383.362 | 3 mes | 146 | 3,4666E-12 | 1,2552E-13 | 5,176E-12 | 2,4374E-12 | 4,9865E-12 |
| AREA | SRC_270 | Cam_Pta_9-PEAS e Imp | 273.393 | 6.383.346 | 3 mes | 144 | 3,5045E-12 | 1,2689E-13 | 5,2325E-12 | 2,464E-12 | 5,041E-12 |
| AREA | SRC_271 | Cam_Pta_10-PEAS e Imp | 273.413 | 6.383.324 | 3 mes | 116 | 4,3382E-12 | 1,5708E-13 | 6,4774E-12 | 3,0502E-12 | 6,2403E-12 |
| AREA | SRC_272 | Cam_Pta_11-PEAS e Imp | 273.447 | 6.383.229 | 3 mes | 400 | 1,2614E-12 | 4,5673E-14 | 1,8834E-12 | 8,8689E-13 | 1,8145E-12 |
| AREA | SRC_273 | Cam_Pta_12-PEAS e Imp | 273.463 | 6.383.220 | 3 mes | 80 | 6,2976E-12 | 2,2802E-13 | 9,4029E-12 | 4,4278E-12 | 9,0588E-12 |
| AREA | SRC_274 | Cam_Pta_13-PEAS e Imp | 273.473 | 6.383.218 | 3 mes | 45 | 1,1183E-11 | 4,049E-13 | 1,6697E-11 | 7,8625E-12 | 1,6086E-11 |
| AREA | SRC_275 | Cam_Pta_14-PEAS e Imp | 273.519 | 6.383.228 | 3 mes | 189 | 2,6766E-12 | 9,6913E-14 | 3,9963E-12 | 1,8819E-12 | 3,8501E-12 |
| AREA | SRC_276 | Cam_Valpo_1-PEAS e Imp | 267.407 | 6.370.003 | 3 mes | 9.182 | 5,1701E-14 | 4,0159E-15 | 9,8734E-14 | 4,2801E-14 | 9,7468E-14 |
| AREA | SRC_277 | Cam_Valpo_2-PEAS e Imp | 267.402 | 6.370.088 | 3 mes | 338 | 1,4033E-12 | 1,09E-13 | 2,6799E-12 | 1,1617E-12 | 2,6455E-12 |
| AREA | SRC_278 | Cam_Valpo_3-PEAS e Imp | 267.699 | 6.371.506 | 3 mes | 5.789 | 8,2003E-14 | 6,3697E-15 | 1,566E-13 | 6,7886E-14 | 1,5459E-13 |
| AREA | SRC_279 | Cam_Valpo_4-PEAS e Imp | 267.700 | 6.371.619 | 3 mes | 452 | 1,0502E-12 | 8,158E-14 | 2,0057E-12 | 8,6945E-13 | 1,98E-12 |
| AREA | SRC_280 | Cam_Valpo_5-PEAS e Imp | 267.517 | 6.371.917 | 3 mes | 1.401 | 3,3873E-13 | 2,6311E-14 | 6,4688E-13 | 2,8042E-13 | 6,3859E-13 |
| AREA | SRC_281 | Cam_Valpo_6-PEAS e Imp | 267.499 | 6.371.980 | 3 mes | 261 | 1,8181E-12 | 1,4123E-13 | 3,4721E-12 | 1,5051E-12 | 3,4276E-12 |
| AREA | SRC_282 | Cam_Valpo_7-PEAS e Imp | 267.496 | 6.372.042 | 3 mes | 247 | 1,9217E-12 | 1,4927E-13 | 3,6699E-12 | 1,5909E-12 | 3,6228E-12 |
| AREA | SRC_283 | Cam_Valpo_8-PEAS e Imp | 267.518 | 6.372.113 | 3 mes | 294 | 1,6121E-12 | 1,2522E-13 | 3,0787E-12 | 1,3346E-12 | 3,0392E-12 |
| AREA | SRC_284 | Cam_Valpo_9-PEAS e Imp | 267.547 | 6.372.151 | 3 mes | 187 | 2,5327E-12 | 1,9673E-13 | 4,8368E-12 | 2,0967E-12 | 4,7747E-12 |
| AREA | SRC_285 | Cam_Valpo_10-PEAS e Imp | 267.569 | 6.372.177 | 3 mes | 137 | 3,4645E-12 | 2,6911E-13 | 6,6163E-12 | 2,8681E-12 | 6,5314E-12 |
| AREA | SRC_286 | Cam_Valpo_11-PEAS e Imp | 267.738 | 6.372.319 | 3 mes | 880 | 5,3955E-13 | 4,191E-14 | 1,0304E-12 | 4,4667E-13 | 1,0172E-12 |
| AREA | SRC_287 | Cam_Valpo_12-PEAS e Imp | 267.762 | 6.372.358 | 3 mes | 187 | 2,5444E-12 | 1,9764E-13 | 4,8592E-12 | 2,1064E-12 | 4,7969E-12 |
| AREA | SRC_288 | Cam_Valpo_13-PEAS e Imp | 267.783 | 6.372.410 | 3 mes | 225 | 2,1144E-12 | 1,6424E-13 | 4,0379E-12 | 1,7504E-12 | 3,9861E-12 |
| AREA | SRC_289 | Cam_Valpo_14-PEAS e Imp | 267.855 | 6.372.669 | 3 mes | 1.076 | 4,4134E-13 | 3,4282E-14 | 8,4284E-13 | 3,6537E-13 | 8,3203E-13 |
| AREA | SRC_290 | Cam_Valpo_15-PEAS e Imp | 267.848 | 6.372.720 | 3 mes | 208 | 2,2847E-12 | 1,7746E-13 | 4,3631E-12 | 1,8914E-12 | 4,3071E-12 |

**Tabla 14.: Escenario 1 - Descripción de las fuentes de emisión de área parte 7**

| Tipo<br>AREA | ID<br>SRC_291 | Descripción<br>Cam_Valpo_16-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_291 | Descripción<br>Cam_Valpo_16-PEAS e Imp | [m]<br>267.715 | [m]<br>6.373.066 | [m]<br>6.373.066 | [m2]<br>1.484 | [g/m2s]<br>3,1987E-13 | [g/m2s]<br>2,4846E-14 | [g/m2s]<br>6,1086E-13 | [g/m2s]<br>2,648E-13 | [g/m2s]<br>6,0303E-13 |
| AREA | SRC_292 | Cam_Valpo_17-PEAS e Imp | 267.705 | 6.373.122 | 3 mes | 225 | 2,1058E-12 | 1,6357E-13 | 4,0215E-12 | 1,7433E-12 | 3,9699E-12 |
| AREA | SRC_293 | Cam_Valpo_18-PEAS e Imp | 267.701 | 6.373.182 | 3 mes | 241 | 1,9679E-12 | 1,5286E-13 | 3,7582E-12 | 1,6291E-12 | 3,71E-12 |
| AREA | SRC_294 | Cam_Valpo_19-PEAS e Imp | 267.704 | 6.373.237 | 3 mes | 218 | 2,1779E-12 | 1,6917E-13 | 4,1592E-12 | 1,803E-12 | 4,1059E-12 |
| AREA | SRC_295 | Cam_Valpo_20-PEAS e Imp | 267.713 | 6.373.309 | 3 mes | 291 | 1,6298E-12 | 1,266E-13 | 3,1126E-12 | 1,3493E-12 | 3,0726E-12 |
| AREA | SRC_296 | Cam_Valpo_21-PEAS e Imp | 267.741 | 6.373.522 | 3 mes | 860 | 5,5188E-13 | 4,2869E-14 | 1,0539E-12 | 4,5688E-13 | 1,0404E-12 |
| AREA | SRC_297 | Cam_Valpo_22-PEAS e Imp | 267.757 | 6.373.574 | 3 mes | 214 | 2,2198E-12 | 1,7243E-13 | 4,2392E-12 | 1,8377E-12 | 4,1848E-12 |
| AREA | SRC_298 | Cam_Valpo_23-PEAS e Imp | 267.777 | 6.373.617 | 3 mes | 187 | 2,5342E-12 | 1,9685E-13 | 4,8397E-12 | 2,098E-12 | 4,7776E-12 |
| AREA | SRC_299 | Cam_Valpo_24-PEAS e Imp | 267.817 | 6.373.719 | 3 mes | 441 | 1,0761E-12 | 8,3587E-14 | 2,055E-12 | 8,9085E-13 | 2,0287E-12 |
| AREA | SRC_300 | Cam_Valpo_25-PEAS e Imp | 267.843 | 6.373.782 | 3 mes | 273 | 1,7415E-12 | 1,3528E-13 | 3,3258E-12 | 1,4417E-12 | 3,2832E-12 |
| AREA | SRC_301 | Cam_Valpo_26-PEAS e Imp | 267.877 | 6.373.831 | 3 mes | 236 | 2,0112E-12 | 1,5623E-13 | 3,8409E-12 | 1,665E-12 | 3,7916E-12 |
| AREA | SRC_302 | Cam_Valpo_27-PEAS e Imp | 267.910 | 6.373.883 | 3 mes | 246 | 1,9288E-12 | 1,4982E-13 | 3,6834E-12 | 1,5967E-12 | 3,6362E-12 |
| AREA | SRC_303 | Cam_Valpo_28-PEAS e Imp | 268.105 | 6.374.174 | 3 mes | 1.400 | 3,3919E-13 | 2,6347E-14 | 6,4777E-13 | 2,808E-13 | 6,3946E-13 |
| AREA | SRC_304 | Cam_Valpo_29-PEAS e Imp | 268.274 | 6.374.430 | 3 mes | 1.228 | 3,8655E-13 | 3,0026E-14 | 7,382E-13 | 3,2E-13 | 7,2873E-13 |
| AREA | SRC_305 | Cam_Valpo_30-PEAS e Imp | 268.317 | 6.374.478 | 3 mes | 254 | 1,8663E-12 | 1,4497E-13 | 3,5642E-12 | 1,545E-12 | 3,5185E-12 |
| AREA | SRC_306 | Cam_Valpo_31-PEAS e Imp | 268.347 | 6.374.502 | 3 mes | 154 | 3,0734E-12 | 2,3874E-13 | 5,8694E-12 | 2,5444E-12 | 5,7942E-12 |
| AREA | SRC_307 | Cam_Valpo_32-PEAS e Imp | 269.602 | 6.375.295 | 3 mes | 5.936 | 7,9977E-14 | 6,2124E-15 | 1,5273E-13 | 6,6209E-14 | 1,5078E-13 |
| AREA | SRC_308 | Cam_Valpo_33-PEAS e Imp | 270.646 | 6.375.956 | 3 mes | 4.938 | 9,6128E-14 | 7,4669E-15 | 1,8358E-13 | 7,9579E-14 | 1,8122E-13 |
| AREA | SRC_309 | Cam_Valpo_34-PEAS e Imp | 270.700 | 6.375.970 | 3 mes | 221 | 2,1505E-12 | 1,6705E-13 | 4,1069E-12 | 1,7803E-12 | 4,0542E-12 |
| AREA | SRC_310 | Cam_Valpo_35-PEAS e Imp | 270.759 | 6.375.972 | 3 mes | 232 | 2,0459E-12 | 1,5892E-13 | 3,9071E-12 | 1,6937E-12 | 3,857E-12 |
| AREA | SRC_311 | Cam_Valpo_36-PEAS e Imp | 270.817 | 6.375.960 | 3 mes | 238 | 1,996E-12 | 1,5504E-13 | 3,8118E-12 | 1,6524E-12 | 3,7629E-12 |
| AREA | SRC_312 | Cam_Valpo_37-PEAS e Imp | 271.210 | 6.375.788 | 3 mes | 1.711 | 2,7745E-13 | 2,1552E-14 | 5,2986E-13 | 2,2969E-13 | 5,2307E-13 |
| AREA | SRC_313 | Cam_Valpo_38-PEAS e Imp | 271.299 | 6.375.786 | 3 mes | 362 | 1,3111E-12 | 1,0185E-13 | 2,5039E-12 | 1,0854E-12 | 2,4718E-12 |
| AREA | SRC_314 | Cam_Valpo_39-PEAS e Imp | 271.410 | 6.375.784 | 3 mes | 444 | 1,069E-12 | 8,3033E-14 | 2,0414E-12 | 8,8494E-13 | 2,0152E-12 |
| AREA | SRC_315 | Cam_Valpo_40-PEAS e Imp | 271.537 | 6.375.829 | 3 mes | 540 | 8,7918E-13 | 6,8292E-14 | 1,679E-12 | 7,2783E-13 | 1,6575E-12 |
| AREA | SRC_316 | Cam_Valpo_41-PEAS e Imp | 271.698 | 6.375.908 | 3 mes | 718 | 6,6149E-13 | 5,1382E-14 | 1,2633E-12 | 5,4762E-13 | 1,2471E-12 |
| AREA | SRC_317 | Cam_Valpo_42-PEAS e Imp | 271.943 | 6.376.040 | 3 mes | 1.111 | 4,2712E-13 | 3,3177E-14 | 8,1569E-13 | 3,5359E-13 | 8,0523E-13 |
| AREA | SRC_318 | Cam_Valpo_43-PEAS e Imp | 272.216 | 6.376.245 | 3 mes | 1.366 | 3,4756E-13 | 2,6998E-14 | 6,6375E-13 | 2,8773E-13 | 6,5524E-13 |
| AREA | SRC_319 | Cam_Valpo_44-PEAS e Imp | 272.308 | 6.376.283 | 3 mes | 397 | 1,1963E-12 | 9,2926E-14 | 2,2846E-12 | 9,9037E-13 | 2,2553E-12 |
| AREA | SRC_320 | Cam_Valpo_45-PEAS e Imp | 272.828 | 6.376.412 | 3 mes | 2.140 | 2,2188E-13 | 1,7235E-14 | 4,2373E-13 | 1,8368E-13 | 4,1829E-13 |

**Tabla 15.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 8**

| Tipo<br>AREA | ID<br>SRC_321 | Descripción<br>Cam_Valpo_46-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_321 | Descripción<br>Cam_Valpo_46-PEAS e Imp | [m]<br>272.961 | [m]<br>6.376.463 | [m]<br>6.376.463 | [m2]<br>573 | [g/m2s]<br>8,2861E-13 | [g/m2s]<br>6,4364E-14 | [g/m2s]<br>1,5824E-12 | [g/m2s]<br>6,8596E-13 | [g/m2s]<br>1,5621E-12 |
| AREA | SRC_322 | Cam_Valpo_47-PEAS e Imp | 273.101 | 6.376.548 | 3 mes | 656 | 7,2317E-13 | 5,6174E-14 | 1,3811E-12 | 5,9868E-13 | 1,3633E-12 |
| AREA | SRC_323 | Cam_Valpo_48-PEAS e Imp | 273.683 | 6.376.890 | 3 mes | 2.700 | 1,7582E-13 | 1,3657E-14 | 3,3577E-13 | 1,4555E-13 | 3,3146E-13 |
| AREA | SRC_324 | Cam_Valpo_49-PEAS e Imp | 273.729 | 6.376.911 | 3 mes | 199 | 2,3895E-12 | 1,8561E-13 | 4,5634E-12 | 1,9782E-12 | 4,5049E-12 |
| AREA | SRC_325 | Cam_Valpo_50-PEAS e Imp | 273.841 | 6.376.934 | 3 mes | 455 | 1,0422E-12 | 8,0953E-14 | 1,9903E-12 | 8,6277E-13 | 1,9648E-12 |
| AREA | SRC_326 | Cam_Valpo_51-PEAS e Imp | 273.918 | 6.376.948 | 3 mes | 315 | 1,5078E-12 | 1,1712E-13 | 2,8794E-12 | 1,2482E-12 | 2,8425E-12 |
| AREA | SRC_327 | Cam_Valpo_52-PEAS e Imp | 273.963 | 6.376.959 | 3 mes | 182 | 2,6042E-12 | 2,0228E-13 | 4,9733E-12 | 2,1559E-12 | 4,9095E-12 |
| AREA | SRC_328 | Cam_Valpo_53-PEAS e Imp | 274.013 | 6.376.981 | 3 mes | 220 | 2,1556E-12 | 1,6744E-13 | 4,1166E-12 | 1,7845E-12 | 4,0638E-12 |
| AREA | SRC_329 | Cam_Valpo_54-PEAS e Imp | 274.045 | 6.377.010 | 3 mes | 176 | 2,7012E-12 | 2,0982E-13 | 5,1586E-12 | 2,2362E-12 | 5,0924E-12 |
| AREA | SRC_330 | Cam_Valpo_55-PEAS e Imp | 274.402 | 6.377.569 | 3 mes | 2.655 | 1,788E-13 | 1,3889E-14 | 3,4146E-13 | 1,4802E-13 | 3,3708E-13 |
| AREA | SRC_331 | Cam_Valpo_56-PEAS e Imp | 274.508 | 6.377.712 | 3 mes | 712 | 6,6654E-13 | 5,1775E-14 | 1,2729E-12 | 5,518E-13 | 1,2566E-12 |
| AREA | SRC_332 | Cam_Valpo_57-PEAS e Imp | 274.515 | 6.377.737 | 3 mes | 106 | 4,4978E-12 | 3,4937E-13 | 8,5895E-12 | 3,7235E-12 | 8,4794E-12 |
| AREA | SRC_333 | Cam_Valpo_58-PEAS e Imp | 274.530 | 6.377.783 | 3 mes | 191 | 2,4874E-12 | 1,9321E-13 | 4,7502E-12 | 2,0592E-12 | 4,6893E-12 |
| AREA | SRC_334 | Cam_Valpo_59-PEAS e Imp | 274.571 | 6.378.190 | 3 mes | 1.641 | 2,8936E-13 | 2,2477E-14 | 5,526E-13 | 2,3955E-13 | 5,4552E-13 |
| AREA | SRC_335 | Cam_Valpo_60-PEAS e Imp | 274.512 | 6.378.662 | 3 mes | 1.902 | 2,4955E-13 | 1,9384E-14 | 4,7658E-13 | 2,0659E-13 | 4,7047E-13 |
| AREA | SRC_336 | Cam_Valpo_61-PEAS e Imp | 274.484 | 6.378.742 | 3 mes | 339 | 1,3988E-12 | 1,0866E-13 | 2,6714E-12 | 1,158E-12 | 2,6372E-12 |
| AREA | SRC_337 | Cam_Valpo_62-PEAS e Imp | 274.397 | 6.378.959 | 3 mes | 935 | 5,0778E-13 | 3,9442E-14 | 9,6971E-13 | 4,2036E-13 | 9,5728E-13 |
| AREA | SRC_338 | Cam_Valpo_63-PEAS e Imp | 274.391 | 6.379.006 | 3 mes | 190 | 2,504E-12 | 1,945E-13 | 4,782E-12 | 2,0729E-12 | 4,7206E-12 |
| AREA | SRC_339 | Cam_Valpo_64-PEAS e Imp | 274.392 | 6.379.034 | 3 mes | 109 | 4,3358E-12 | 3,3679E-13 | 8,2801E-12 | 3,5894E-12 | 8,1739E-12 |
| AREA | SRC_340 | Cam_Valpo_65-PEAS e Imp | 274.513 | 6.379.469 | 3 mes | 1.806 | 2,6291E-13 | 2,0422E-14 | 5,0209E-13 | 2,1765E-13 | 4,9565E-13 |
| AREA | SRC_341 | Cam_Valpo_66-PEAS e Imp | 274.514 | 6.379.510 | 3 mes | 163 | 2,906E-12 | 2,2573E-13 | 5,5497E-12 | 2,4057E-12 | 5,4785E-12 |
| AREA | SRC_342 | Cam_Valpo_67-PEAS e Imp | 274.503 | 6.379.560 | 3 mes | 209 | 2,2743E-12 | 1,7666E-13 | 4,3432E-12 | 1,8828E-12 | 4,2875E-12 |
| AREA | SRC_343 | Cam_Valpo_68-PEAS e Imp | 274.488 | 6.379.623 | 3 mes | 255 | 1,8584E-12 | 1,4436E-13 | 3,5491E-12 | 1,5385E-12 | 3,5035E-12 |
| AREA | SRC_344 | Cam_Valpo_69-PEAS e Imp | 274.426 | 6.379.798 | 3 mes | 746 | 6,3671E-13 | 4,9458E-14 | 1,2159E-12 | 5,271E-13 | 1,2004E-12 |
| AREA | SRC_345 | Cam_Valpo_70-PEAS e Imp | 274.386 | 6.379.897 | 3 mes | 429 | 1,1078E-12 | 8,6047E-14 | 2,1155E-12 | 9,1705E-13 | 2,0884E-12 |
| AREA | SRC_346 | Cam_Valpo_71-PEAS e Imp | 274.352 | 6.379.981 | 3 mes | 360 | 1,3178E-12 | 1,0236E-13 | 2,5166E-12 | 1,0909E-12 | 2,4844E-12 |
| AREA | SRC_347 | Cam_Valpo_72-PEAS e Imp | 274.336 | 6.380.041 | 3 mes | 249 | 1,9028E-12 | 1,478E-13 | 3,6337E-12 | 1,5752E-12 | 3,5871E-12 |
| AREA | SRC_348 | Cam_Valpo_73-PEAS e Imp | 274.333 | 6.380.099 | 3 mes | 228 | 2,0839E-12 | 1,6187E-13 | 3,9797E-12 | 1,7252E-12 | 3,9287E-12 |
| AREA | SRC_349 | Cam_Valpo_74-PEAS e Imp | 274.332 | 6.380.163 | 3 mes | 257 | 1,8452E-12 | 1,4333E-13 | 3,5238E-12 | 1,5275E-12 | 3,4786E-12 |
| AREA | SRC_350 | Cam_Valpo_75-PEAS e Imp | 274.329 | 6.380.546 | 3 mes | 1.530 | 3,1018E-13 | 2,4094E-14 | 5,9236E-13 | 2,5678E-13 | 5,8476E-13 |

**Tabla 16.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 9**

| Tipo<br>AREA | ID<br>SRC_351 | Descripción<br>Cam_Valpo_76-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_351 | Descripción<br>Cam_Valpo_76-PEAS e Imp | [m]<br>274.323 | [m]<br>6.380.578 | [m]<br>6.380.578 | [m2]<br>131 | [g/m2s]<br>3,6364E-12 | [g/m2s]<br>2,8246E-13 | [g/m2s]<br>6,9445E-12 | [g/m2s]<br>3,0104E-12 | [g/m2s]<br>6,8554E-12 |
| AREA | SRC_352 | Cam_Valpo_77-PEAS e Imp | 274.308 | 6.380.608 | 3 mes | 138 | 3,4356E-12 | 2,6687E-13 | 6,5611E-12 | 2,8442E-12 | 6,4769E-12 |
| AREA | SRC_353 | Cam_Valpo_78-PEAS e Imp | 274.078 | 6.381.086 | 3 mes | 2.121 | 2,2387E-13 | 1,7389E-14 | 4,2752E-13 | 1,8533E-13 | 4,2204E-13 |
| AREA | SRC_354 | Cam_Valpo_79-PEAS e Imp | 274.036 | 6.381.146 | 3 mes | 293 | 1,6204E-12 | 1,2587E-13 | 3,0945E-12 | 1,3415E-12 | 3,0549E-12 |
| AREA | SRC_355 | Cam_Valpo_80-PEAS e Imp | 273.997 | 6.381.192 | 3 mes | 243 | 1,9559E-12 | 1,5193E-13 | 3,7353E-12 | 1,6192E-12 | 3,6874E-12 |
| AREA | SRC_356 | Cam_Valpo_81-PEAS e Imp | 273.945 | 6.381.212 | 3 mes | 225 | 2,1075E-12 | 1,637E-13 | 4,0248E-12 | 1,7447E-12 | 3,9732E-12 |
| AREA | SRC_357 | Cam_Valpo_82-PEAS e Imp | 273.863 | 6.381.235 | 3 mes | 341 | 1,3938E-12 | 1,0826E-13 | 2,6617E-12 | 1,1538E-12 | 2,6276E-12 |
| AREA | SRC_358 | Cam_Valpo_83-PEAS e Imp | 273.527 | 6.381.309 | 3 mes | 1.377 | 3,4483E-13 | 2,6785E-14 | 6,5852E-13 | 2,8546E-13 | 6,5008E-13 |
| AREA | SRC_359 | Cam_Valpo_84-PEAS e Imp | 273.488 | 6.381.317 | 3 mes | 159 | 2,9888E-12 | 2,3216E-13 | 5,7078E-12 | 2,4743E-12 | 5,6346E-12 |
| AREA | SRC_360 | Cam_Valpo_85-PEAS e Imp | 273.437 | 6.381.311 | 3 mes | 211 | 2,254E-12 | 1,7508E-13 | 4,3045E-12 | 1,866E-12 | 4,2493E-12 |
| AREA | SRC_361 | Cam_Valpo_86-PEAS e Imp | 273.400 | 6.381.306 | 3 mes | 149 | 3,1913E-12 | 2,4789E-13 | 6,0946E-12 | 2,6419E-12 | 6,0164E-12 |
| AREA | SRC_362 | Cam_Valpo_87-PEAS e Imp | 273.330 | 6.381.278 | 3 mes | 302 | 1,5718E-12 | 1,2209E-13 | 3,0017E-12 | 1,3012E-12 | 2,9632E-12 |
| AREA | SRC_363 | Cam_Valpo_88-PEAS e Imp | 273.269 | 6.381.275 | 3 mes | 240 | 1,9753E-12 | 1,5344E-13 | 3,7723E-12 | 1,6353E-12 | 3,7239E-12 |
| AREA | SRC_364 | Cam_Valpo_89-PEAS e Imp | 273.210 | 6.381.284 | 3 mes | 239 | 1,9888E-12 | 1,5448E-13 | 3,7981E-12 | 1,6464E-12 | 3,7494E-12 |
| AREA | SRC_365 | Cam_Valpo_90-PEAS e Imp | 273.140 | 6.381.307 | 3 mes | 292 | 1,6263E-12 | 1,2633E-13 | 3,1058E-12 | 1,3464E-12 | 3,066E-12 |
| AREA | SRC_366 | Cam_Valpo_91-PEAS e Imp | 273.026 | 6.381.364 | 3 mes | 511 | 9,2969E-13 | 7,2215E-14 | 1,7754E-12 | 7,6964E-13 | 1,7527E-12 |
| AREA | SRC_367 | Cam_Valpo_92-PEAS e Imp | 272.787 | 6.381.471 | 3 mes | 1.046 | 4,5363E-13 | 3,5237E-14 | 8,6631E-13 | 3,7554E-13 | 8,552E-13 |
| AREA | SRC_368 | Cam_Valpo_93-PEAS e Imp | 272.625 | 6.381.553 | 3 mes | 727 | 6,5314E-13 | 5,0734E-14 | 1,2473E-12 | 5,407E-13 | 1,2313E-12 |
| AREA | SRC_369 | Cam_Valpo_94-PEAS e Imp | 272.586 | 6.381.587 | 3 mes | 206 | 2,3059E-12 | 1,7911E-13 | 4,4036E-12 | 1,9089E-12 | 4,3471E-12 |
| AREA | SRC_370 | Cam_Valpo_95-PEAS e Imp | 272.567 | 6.381.621 | 3 mes | 150 | 3,1594E-12 | 2,4541E-13 | 6,0336E-12 | 2,6155E-12 | 5,9563E-12 |
| AREA | SRC_371 | Cam_Valpo_96-PEAS e Imp | 272.558 | 6.381.659 | 3 mes | 155 | 3,0708E-12 | 2,3853E-13 | 5,8644E-12 | 2,5422E-12 | 5,7892E-12 |
| AREA | SRC_372 | Cam_Valpo_97-PEAS e Imp | 272.513 | 6.381.931 | 3 mes | 1.103 | 4,303E-13 | 3,3425E-14 | 8,2176E-13 | 3,5623E-13 | 8,1122E-13 |
| AREA | SRC_373 | Cam_Valpo_98-PEAS e Imp | 272.500 | 6.382.030 | 3 mes | 398 | 1,1916E-12 | 9,2562E-14 | 2,2757E-12 | 9,8649E-13 | 2,2465E-12 |
| AREA | SRC_374 | Cam_Valpo_99-PEAS e Imp | 272.492 | 6.382.086 | 3 mes | 224 | 2,1204E-12 | 1,6471E-13 | 4,0494E-12 | 1,7554E-12 | 3,9975E-12 |
| AREA | SRC_375 | Cam_Valpo_100-PEAS e Imp | 272.491 | 6.382.127 | 3 mes | 164 | 2,889E-12 | 2,2441E-13 | 5,5172E-12 | 2,3917E-12 | 5,4465E-12 |
| AREA | SRC_376 | Cam_Valpo_101-PEAS e Imp | 272.506 | 6.382.188 | 3 mes | 247 | 1,9193E-12 | 1,4909E-13 | 3,6654E-12 | 1,5889E-12 | 3,6184E-12 |
| AREA | SRC_377 | Cam_Valpo_102-PEAS e Imp | 272.660 | 6.383.439 | 3 mes | 5.043 | 9,4127E-14 | 7,3114E-15 | 1,7976E-13 | 7,7923E-14 | 1,7745E-13 |
| AREA | SRC_378 | Cam_Valpo_103-PEAS e Imp | 272.630 | 6.384.559 | 3 mes | 4.479 | 1,0599E-13 | 8,2328E-15 | 2,0241E-13 | 8,7742E-14 | 1,9981E-13 |
| AREA | SRC_379 | Cam_Valpo_104-PEAS e Imp | 272.626 | 6.385.227 | 3 mes | 2.671 | 1,7772E-13 | 1,3805E-14 | 3,394E-13 | 1,4713E-13 | 3,3505E-13 |
| AREA | SRC_380 | Cam_Valpo_105-PEAS e Imp | 272.602 | 6.386.454 | 3 mes | 4.906 | 9,6765E-14 | 7,5164E-15 | 1,8479E-13 | 8,0107E-14 | 1,8242E-13 |
| AREA | SRC_381 | Cam_Valpo_106-PEAS e Imp | 272.609 | 6.386.527 | 3 mes | 293 | 1,6228E-12 | 1,2605E-13 | 3,0991E-12 | 1,3434E-12 | 3,0593E-12 |
| AREA | SRC_382 | Cam_Valpo_107-PEAS e Imp | 272.650 | 6.386.615 | 3 mes | 385 | 1,234E-12 | 9,5853E-14 | 2,3566E-12 | 1,0216E-12 | 2,3264E-12 |
| AREA | SRC_383 | Cam_Valpo_108-PEAS e Imp | 272.755 | 6.386.705 | 3 mes | 550 | 8,6311E-13 | 6,7043E-14 | 1,6483E-12 | 7,1453E-13 | 1,6272E-12 |
| AREA | SRC_384 | Cam_Valpo_109-PEAS e Imp | 272.846 | 6.386.776 | 3 mes | 461 | 1,0301E-12 | 8,0013E-14 | 1,9672E-12 | 8,5275E-13 | 1,9419E-12 |
| AREA | SRC_385 | Cam_Valpo_110-PEAS e Imp | 272.918 | 6.386.821 | 3 mes | 339 | 1,4012E-12 | 1,0884E-13 | 2,6759E-12 | 1,16E-12 | 2,6416E-12 |

**Tabla 17.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 10**

| Tipo<br>AREA | ID<br>SRC_386 | Descripción<br>Cam_Valpo_111-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_386 | Descripción<br>Cam_Valpo_111-PEAS e Imp | [m]<br>272.959 | [m]<br>6.386.856 | [m]<br>6.386.856 | [m2]<br>216 | [g/m2s]<br>2,2007E-12 | [g/m2s]<br>1,7095E-13 | [g/m2s]<br>4,2028E-12 | [g/m2s]<br>1,8219E-12 | [g/m2s]<br>4,1489E-12 |
| AREA | SRC_387 | Cam_Valpo_112-PEAS e Imp | 272.979 | 6.386.909 | 3 mes | 229 | 2,07E-12 | 1,6079E-13 | 3,9532E-12 | 1,7137E-12 | 3,9025E-12 |
| AREA | SRC_388 | Cam_Valpo_113-PEAS e Imp | 272.982 | 6.386.950 | 3 mes | 168 | 2,8224E-12 | 2,1923E-13 | 5,39E-12 | 2,3365E-12 | 5,3208E-12 |
| AREA | SRC_389 | Cam_Valpo_114-PEAS e Imp | 272.974 | 6.387.033 | 3 mes | 335 | 1,4189E-12 | 1,1022E-13 | 2,7097E-12 | 1,1746E-12 | 2,675E-12 |
| AREA | SRC_390 | Cam_Valpo_115-PEAS e Imp | 272.969 | 6.387.289 | 3 mes | 1.021 | 4,6483E-13 | 3,6106E-14 | 8,8769E-13 | 3,8481E-13 | 8,7631E-13 |
| AREA | SRC_391 | Cam_Valpo_116-PEAS e Imp | 272.950 | 6.387.316 | 3 mes | 136 | 3,4941E-12 | 2,7141E-13 | 6,6728E-12 | 2,8926E-12 | 6,5873E-12 |
| AREA | SRC_392 | Cam_Valpo_117-PEAS e Imp | 272.918 | 6.387.332 | 3 mes | 151 | 3,1517E-12 | 2,4482E-13 | 6,0189E-12 | 2,6092E-12 | 5,9417E-12 |
| AREA | SRC_393 | Cam_Valpo_118-PEAS e Imp | 272.871 | 6.387.328 | 3 mes | 193 | 2,4582E-12 | 1,9095E-13 | 4,6945E-12 | 2,035E-12 | 4,6343E-12 |
| AREA | SRC_394 | Cam_Valpo_119-PEAS e Imp | 272.818 | 6.387.319 | 3 mes | 215 | 2,2098E-12 | 1,7165E-13 | 4,2201E-12 | 1,8294E-12 | 4,166E-12 |
| AREA | SRC_395 | Cam_Valpo_120-PEAS e Imp | 272.669 | 6.387.324 | 3 mes | 594 | 7,9983E-13 | 6,2128E-14 | 1,5275E-12 | 6,6214E-13 | 1,5079E-12 |
| AREA | SRC_396 | Cam_Valpo_121-PEAS e Imp | 272.536 | 6.387.380 | 3 mes | 574 | 8,2686E-13 | 6,4228E-14 | 1,5791E-12 | 6,8452E-13 | 1,5588E-12 |
| AREA | SRC_397 | Cam_Valpo_122-PEAS e Imp | 272.406 | 6.387.475 | 3 mes | 643 | 7,3845E-13 | 5,736E-14 | 1,4102E-12 | 6,1133E-13 | 1,3921E-12 |
| AREA | SRC_398 | Cam_Valpo_123-PEAS e Imp | 272.321 | 6.387.544 | 3 mes | 439 | 1,0817E-12 | 8,4022E-14 | 2,0657E-12 | 8,9548E-13 | 2,0392E-12 |
| AREA | SRC_399 | Cam_Valpo_124-PEAS e Imp | 272.252 | 6.387.605 | 3 mes | 366 | 1,297E-12 | 1,0074E-13 | 2,4769E-12 | 1,0737E-12 | 2,4451E-12 |
| AREA | SRC_400 | Cam_Valpo_125-PEAS e Imp | 272.138 | 6.387.749 | 3 mes | 734 | 6,4677E-13 | 5,0239E-14 | 1,2352E-12 | 5,3543E-13 | 1,2193E-12 |
| AREA | SRC_401 | Cam_Valpo_126-PEAS e Imp | 272.059 | 6.387.890 | 3 mes | 646 | 7,3518E-13 | 5,7107E-14 | 1,404E-12 | 6,0862E-13 | 1,386E-12 |
| AREA | SRC_402 | Cam_Valpo_127-PEAS e Imp | 272.019 | 6.388.008 | 3 mes | 494 | 9,6039E-13 | 7,46E-14 | 1,8341E-12 | 7,9506E-13 | 1,8106E-12 |
| AREA | SRC_403 | Cam_Valpo_128-PEAS e Imp | 272.005 | 6.388.086 | 3 mes | 318 | 1,492E-12 | 1,1589E-13 | 2,8493E-12 | 1,2352E-12 | 2,8128E-12 |
| AREA | SRC_404 | Cam_Valpo_129-PEAS e Imp | 272.005 | 6.388.171 | 3 mes | 338 | 1,4028E-12 | 1,0897E-13 | 2,679E-12 | 1,1613E-12 | 2,6447E-12 |
| AREA | SRC_405 | Cam_Valpo_130-PEAS e Imp | 272.018 | 6.388.207 | 3 mes | 149 | 3,1774E-12 | 2,4681E-13 | 6,068E-12 | 2,6304E-12 | 5,9902E-12 |
| AREA | SRC_406 | Cam_Valpo_131-PEAS e Imp | 272.053 | 6.388.222 | 3 mes | 145 | 3,2836E-12 | 2,5506E-13 | 6,2708E-12 | 2,7184E-12 | 6,1904E-12 |
| AREA | SRC_407 | Cam_Valpo_132-PEAS e Imp | 272.113 | 6.388.260 | 3 mes | 286 | 1,6587E-12 | 1,2884E-13 | 3,1677E-12 | 1,3732E-12 | 3,1271E-12 |
| AREA | SRC_408 | Cam_Valpo_133-PEAS e Imp | 272.165 | 6.388.289 | 3 mes | 237 | 2,0072E-12 | 1,5591E-13 | 3,8332E-12 | 1,6617E-12 | 3,7841E-12 |
| AREA | SRC_409 | Cam_Valpo_134-PEAS e Imp | 272.170 | 6.388.313 | 3 mes | 103 | 4,6072E-12 | 3,5787E-13 | 8,7985E-12 | 3,8141E-12 | 8,6856E-12 |
| AREA | SRC_410 | Cam_Valpo_135-PEAS e Imp | 272.160 | 6.388.355 | 3 mes | 179 | 2,6569E-12 | 2,0638E-13 | 5,0739E-12 | 2,1995E-12 | 5,0088E-12 |
| AREA | SRC_411 | Cam_Valpo_136-PEAS e Imp | 272.116 | 6.388.384 | 3 mes | 213 | 2,2269E-12 | 1,7298E-13 | 4,2528E-12 | 1,8436E-12 | 4,1983E-12 |
| AREA | SRC_412 | Cam_Valpo_137-PEAS e Imp | 271.990 | 6.388.473 | 3 mes | 618 | 7,6782E-13 | 5,9642E-14 | 1,4663E-12 | 6,3564E-13 | 1,4475E-12 |
| AREA | SRC_413 | Cam_Valpo_138-PEAS e Imp | 271.909 | 6.388.570 | 3 mes | 502 | 9,4518E-13 | 7,3418E-14 | 1,805E-12 | 7,8247E-13 | 1,7819E-12 |
| AREA | SRC_414 | Cam_Valpo_139-PEAS e Imp | 271.887 | 6.388.631 | 3 mes | 258 | 1,8423E-12 | 1,431E-13 | 3,5183E-12 | 1,5252E-12 | 3,4732E-12 |
| AREA | SRC_415 | Cam_Valpo_140-PEAS e Imp | 271.869 | 6.388.710 | 3 mes | 325 | 1,4626E-12 | 1,1361E-13 | 2,7932E-12 | 1,2108E-12 | 2,7573E-12 |
| AREA | SRC_416 | Cam_Valpo_141-PEAS e Imp | 271.879 | 6.388.778 | 3 mes | 271 | 1,7535E-12 | 1,3621E-13 | 3,3487E-12 | 1,4516E-12 | 3,3058E-12 |
| AREA | SRC_417 | Cam_Valpo_142-PEAS e Imp | 271.889 | 6.388.831 | 3 mes | 216 | 2,1997E-12 | 1,7086E-13 | 4,2008E-12 | 1,821E-12 | 4,1469E-12 |
| AREA | SRC_418 | Cam_Valpo_143-PEAS e Imp | 271.888 | 6.388.910 | 3 mes | 318 | 1,4949E-12 | 1,1612E-13 | 2,8549E-12 | 1,2376E-12 | 2,8183E-12 |
| AREA | SRC_419 | Cam_Valpo_144-PEAS e Imp | 271.765 | 6.389.249 | 3 mes | 1.444 | 3,2878E-13 | 2,5539E-14 | 6,2789E-13 | 2,7218E-13 | 6,1984E-13 |

**Tabla 18.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 11**

| Tipo<br>AREA | ID<br>SRC_420 | Descripción<br>Cam_Valpo_145-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_420 | Descripción<br>Cam_Valpo_145-PEAS e Imp | [m]<br>271.745 | [m]<br>6.389.323 | [m]<br>6.389.323 | [m2]<br>309 | [g/m2s]<br>1,5379E-12 | [g/m2s]<br>1,1946E-13 | [g/m2s]<br>2,9369E-12 | [g/m2s]<br>1,2731E-12 | [g/m2s]<br>2,8993E-12 |
| AREA | SRC_421 | Cam_Valpo_146-PEAS e Imp | 271.746 | 6.389.404 | 3 mes | 321 | 1,4783E-12 | 1,1483E-13 | 2,8231E-12 | 1,2238E-12 | 2,7869E-12 |
| AREA | SRC_422 | Cam_Valpo_147-PEAS e Imp | 271.745 | 6.389.713 | 3 mes | 1.235 | 3,8428E-13 | 2,9849E-14 | 7,3386E-13 | 3,1812E-13 | 7,2445E-13 |
| AREA | SRC_423 | Cam_Valpo_148-PEAS e Imp | 271.729 | 6.389.779 | 3 mes | 275 | 1,7279E-12 | 1,3421E-13 | 3,2997E-12 | 1,4304E-12 | 3,2574E-12 |
| AREA | SRC_424 | Cam_Valpo_149-PEAS e Imp | 271.405 | 6.390.771 | 3 mes | 4.170 | 1,1385E-13 | 8,8433E-15 | 2,1742E-13 | 9,4249E-14 | 2,1463E-13 |
| AREA | SRC_425 | Cam_Valpo_150-PEAS e Imp | 271.408 | 6.390.852 | 3 mes | 324 | 1,4648E-12 | 1,1378E-13 | 2,7974E-12 | 1,2127E-12 | 2,7616E-12 |
| AREA | SRC_426 | Cam_Valpo_151-PEAS e Imp | 271.425 | 6.390.918 | 3 mes | 270 | 1,7598E-12 | 1,3669E-13 | 3,3607E-12 | 1,4568E-12 | 3,3176E-12 |
| AREA | SRC_427 | Cam_Valpo_152-PEAS e Imp | 271.595 | 6.391.444 | 3 mes | 2.210 | 2,1478E-13 | 1,6684E-14 | 4,1017E-13 | 1,7781E-13 | 4,0491E-13 |
| AREA | SRC_428 | Cam_Valpo_153-PEAS e Imp | 271.601 | 6.391.518 | 3 mes | 297 | 1,598E-12 | 1,2413E-13 | 3,0517E-12 | 1,3229E-12 | 3,0126E-12 |
| AREA | SRC_429 | Cam_Valpo_154-PEAS e Imp | 271.583 | 6.391.599 | 3 mes | 335 | 1,4189E-12 | 1,1022E-13 | 2,7098E-12 | 1,1747E-12 | 2,675E-12 |
| AREA | SRC_430 | Cam_Valpo_155-PEAS e Imp | 271.490 | 6.391.665 | 3 mes | 462 | 1,0269E-12 | 7,9764E-14 | 1,961E-12 | 8,501E-13 | 1,9359E-12 |
| AREA | SRC_431 | Cam_Valpo_156-PEAS e Imp | 271.388 | 6.391.779 | 3 mes | 610 | 7,7759E-13 | 6,0401E-14 | 1,485E-12 | 6,4373E-13 | 1,4659E-12 |
| AREA | SRC_432 | Cam_Valpo_157-PEAS e Imp | 271.303 | 6.391.969 | 3 mes | 830 | 5,7197E-13 | 4,4429E-14 | 1,0923E-12 | 4,7351E-13 | 1,0783E-12 |
| AREA | SRC_433 | Cam_Valpo_158-PEAS e Imp | 271.249 | 6.392.048 | 3 mes | 385 | 1,2315E-12 | 9,5658E-14 | 2,3518E-12 | 1,0195E-12 | 2,3217E-12 |
| AREA | SRC_434 | Cam_Valpo_159-PEAS e Imp | 271.095 | 6.392.199 | 3 mes | 863 | 5,5E-13 | 4,2722E-14 | 1,0503E-12 | 4,5532E-13 | 1,0369E-12 |
| AREA | SRC_435 | Cam_Valpo_160-PEAS e Imp | 271.003 | 6.392.357 | 3 mes | 727 | 6,526E-13 | 5,0692E-14 | 1,2463E-12 | 5,4026E-13 | 1,2303E-12 |
| AREA | SRC_436 | Cam_Valpo_161-PEAS e Imp | 270.864 | 6.392.618 | 3 mes | 1.182 | 4,0173E-13 | 3,1205E-14 | 7,6719E-13 | 3,3257E-13 | 7,5735E-13 |
| AREA | SRC_437 | Cam_Valpo_162-PEAS e Imp | 270.665 | 6.392.901 | 3 mes | 1.387 | 3,4234E-13 | 2,6592E-14 | 6,5377E-13 | 2,834E-13 | 6,4539E-13 |
| AREA | SRC_438 | Cam_Valpo_163-PEAS e Imp | 270.570 | 6.393.060 | 3 mes | 740 | 6,4167E-13 | 4,9843E-14 | 1,2254E-12 | 5,3121E-13 | 1,2097E-12 |
| AREA | SRC_439 | Cam_Valpo_164-PEAS e Imp | 270.535 | 6.393.162 | 3 mes | 428 | 1,1093E-12 | 8,6166E-14 | 2,1185E-12 | 9,1833E-13 | 2,0913E-12 |
| AREA | SRC_440 | Cam_Valpo_165-PEAS e Imp | 270.408 | 6.393.157 | 3 mes | 516 | 9,197E-13 | 7,1439E-14 | 1,7564E-12 | 7,6137E-13 | 1,7338E-12 |
| AREA | SRC_441 | Cam_Valpo_166-PEAS e Imp | 270.322 | 6.393.156 | 3 mes | 344 | 1,3795E-12 | 1,0716E-13 | 2,6345E-12 | 1,142E-12 | 2,6007E-12 |
| AREA | SRC_442 | Cam_Valpo_167-PEAS e Imp | 270.198 | 6.393.225 | 3 mes | 562 | 8,4464E-13 | 6,5608E-14 | 1,613E-12 | 6,9923E-13 | 1,5923E-12 |
| AREA | SRC_443 | Cam_Valpo_168-PEAS e Imp | 270.084 | 6.393.222 | 3 mes | 462 | 1,0285E-12 | 7,9887E-14 | 1,9641E-12 | 8,5141E-13 | 1,9389E-12 |
| AREA | SRC_444 | Cam_Valpo_169-PEAS e Imp | 270.014 | 6.393.114 | 3 mes | 520 | 9,1282E-13 | 7,0905E-14 | 1,7432E-12 | 7,5568E-13 | 1,7209E-12 |
| AREA | SRC_445 | Cam_Valpo_170-PEAS e Imp | 269.944 | 6.393.026 | 3 mes | 448 | 1,0592E-12 | 8,2273E-14 | 2,0227E-12 | 8,7684E-13 | 1,9968E-12 |
| AREA | SRC_446 | Cam_Valpo_171-PEAS e Imp | 269.831 | 6.392.981 | 3 mes | 484 | 9,8009E-13 | 7,613E-14 | 1,8717E-12 | 8,1137E-13 | 1,8477E-12 |
| AREA | SRC_447 | Cam_Valpo_172-PEAS e Imp | 269.702 | 6.392.966 | 3 mes | 517 | 9,1822E-13 | 7,1324E-14 | 1,7535E-12 | 7,6015E-13 | 1,7311E-12 |
| AREA | SRC_448 | Cam_Valpo_173-PEAS e Imp | 269.506 | 6.393.084 | 3 mes | 907 | 5,2354E-13 | 4,0667E-14 | 9,9982E-13 | 4,3341E-13 | 9,87E-13 |
| AREA | SRC_449 | Cam_Valpo_174-PEAS e Imp | 269.407 | 6.393.106 | 3 mes | 411 | 1,1561E-12 | 8,9802E-14 | 2,2078E-12 | 9,5707E-13 | 2,1795E-12 |
| AREA | SRC_450 | Cam_Valpo_175-PEAS e Imp | 269.355 | 6.393.219 | 3 mes | 493 | 9,6265E-13 | 7,4776E-14 | 1,8384E-12 | 7,9693E-13 | 1,8148E-12 |
| AREA | SRC_451 | Cam_Valpo_176-PEAS e Imp | 269.450 | 6.393.436 | 3 mes | 940 | 5,0524E-13 | 3,9245E-14 | 9,6487E-13 | 4,1826E-13 | 9,525E-13 |
| AREA | SRC_452 | Cam_Valpo_177-PEAS e Imp | 269.537 | 6.393.768 | 3 mes | 1.375 | 3,4512E-13 | 2,6808E-14 | 6,5908E-13 | 2,8571E-13 | 6,5063E-13 |
| AREA | SRC_453 | Cam_Valpo_178-PEAS e Imp | 269.541 | 6.393.876 | 3 mes | 433 | 1,0959E-12 | 8,5128E-14 | 2,0929E-12 | 9,0726E-13 | 2,0661E-12 |
| AREA | SRC_454 | Cam_Valpo_179-PEAS e Imp | 269.514 | 6.393.952 | 3 mes | 327 | 1,4495E-12 | 1,1259E-13 | 2,7682E-12 | 1,2E-12 | 2,7327E-12 |

**Tabla 19.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 12**

| Tipo<br>AREA | ID<br>SRC_455 | Descripción<br>Cam_Valpo_180-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_455 | Descripción<br>Cam_Valpo_180-PEAS e Imp | [m]<br>269.461 | [m]<br>6.394.006 | [m]<br>6.394.006 | [m2]<br>302 | [g/m2s]<br>1,5718E-12 | [g/m2s]<br>1,2209E-13 | [g/m2s]<br>3,0016E-12 | [g/m2s]<br>1,3012E-12 | [g/m2s]<br>2,9631E-12 |
| AREA | SRC_456 | Cam_Valpo_181-PEAS e Imp | 269.456 | 6.394.087 | 3 mes | 318 | 1,495E-12 | 1,1613E-13 | 2,855E-12 | 1,2376E-12 | 2,8184E-12 |
| AREA | SRC_457 | Cam_Valpo_182-PEAS e Imp | 269.494 | 6.394.169 | 3 mes | 359 | 1,3225E-12 | 1,0273E-13 | 2,5257E-12 | 1,0949E-12 | 2,4933E-12 |
| AREA | SRC_458 | Cam_Valpo_183-PEAS e Imp | 269.580 | 6.394.296 | 3 mes | 612 | 7,7568E-13 | 6,0253E-14 | 1,4813E-12 | 6,4215E-13 | 1,4623E-12 |
| AREA | SRC_459 | Cam_Valpo_184-PEAS e Imp | 269.614 | 6.394.394 | 3 mes | 417 | 1,1395E-12 | 8,851E-14 | 2,1761E-12 | 9,4331E-13 | 2,1482E-12 |
| AREA | SRC_460 | Cam_Valpo_185-PEAS e Imp | 269.617 | 6.394.492 | 3 mes | 397 | 1,1971E-12 | 9,2983E-14 | 2,286E-12 | 9,9098E-13 | 2,2567E-12 |
| AREA | SRC_461 | Cam_Valpo_186-PEAS e Imp | 269.532 | 6.394.634 | 3 mes | 664 | 7,1473E-13 | 5,5518E-14 | 1,3649E-12 | 5,9169E-13 | 1,3474E-12 |
| AREA | SRC_462 | Cam_Valpo_187-PEAS e Imp | 269.478 | 6.394.752 | 3 mes | 518 | 9,1608E-13 | 7,1158E-14 | 1,7495E-12 | 7,5838E-13 | 1,727E-12 |
| AREA | SRC_463 | Cam_Valpo_188-PEAS e Imp | 269.437 | 6.394.881 | 3 mes | 541 | 8,7758E-13 | 6,8167E-14 | 1,6759E-12 | 7,265E-13 | 1,6544E-12 |
| AREA | SRC_464 | Cam_Valpo_189-PEAS e Imp | 269.448 | 6.395.002 | 3 mes | 483 | 9,8191E-13 | 7,6271E-14 | 1,8752E-12 | 8,1287E-13 | 1,8511E-12 |
| AREA | SRC_465 | Cam_Valpo_190-PEAS e Imp | 269.465 | 6.395.049 | 3 mes | 198 | 2,3997E-12 | 1,864E-13 | 4,5828E-12 | 1,9866E-12 | 4,524E-12 |
| AREA | SRC_466 | Cam_Valpo_191-PEAS e Imp | 269.701 | 6.395.188 | 3 mes | 1.089 | 4,3605E-13 | 3,3871E-14 | 8,3274E-13 | 3,6098E-13 | 8,2206E-13 |
| AREA | SRC_467 | Cam_Valpo_192-PEAS e Imp | 269.737 | 6.395.244 | 3 mes | 269 | 1,7623E-12 | 1,3689E-13 | 3,3654E-12 | 1,4589E-12 | 3,3223E-12 |
| AREA | SRC_468 | Cam_Valpo_193-PEAS e Imp | 269.748 | 6.395.318 | 3 mes | 302 | 1,5725E-12 | 1,2215E-13 | 3,003E-12 | 1,3018E-12 | 2,9645E-12 |
| AREA | SRC_469 | Cam_Valpo_194-PEAS e Imp | 269.734 | 6.395.473 | 3 mes | 624 | 7,6073E-13 | 5,9091E-14 | 1,4528E-12 | 6,2978E-13 | 1,4342E-12 |
| AREA | SRC_470 | Cam_Valpo_195-PEAS e Imp | 269.791 | 6.395.575 | 3 mes | 463 | 1,0255E-12 | 7,9657E-14 | 1,9584E-12 | 8,4896E-13 | 1,9333E-12 |
| AREA | SRC_471 | Cam_Valpo_196-PEAS e Imp | 269.918 | 6.395.634 | 3 mes | 558 | 8,5139E-13 | 6,6133E-14 | 1,6259E-12 | 7,0482E-13 | 1,6051E-12 |
| AREA | SRC_472 | Cam_Valpo_197-PEAS e Imp | 269.951 | 6.395.703 | 3 mes | 312 | 1,5232E-12 | 1,1831E-13 | 2,9088E-12 | 1,261E-12 | 2,8715E-12 |
| AREA | SRC_473 | Cam_Valpo_198-PEAS e Imp | 269.926 | 6.395.767 | 3 mes | 278 | 1,7084E-12 | 1,327E-13 | 3,2625E-12 | 1,4143E-12 | 3,2207E-12 |
| AREA | SRC_474 | Cam_Valpo_199-PEAS e Imp | 269.853 | 6.395.812 | 3 mes | 348 | 1,363E-12 | 1,0587E-13 | 2,603E-12 | 1,1284E-12 | 2,5696E-12 |
| AREA | SRC_475 | Cam_Valpo_200-PEAS e Imp | 269.732 | 6.395.847 | 3 mes | 505 | 9,4063E-13 | 7,3065E-14 | 1,7964E-12 | 7,787E-13 | 1,7733E-12 |
| AREA | SRC_476 | Cam_Valpo_201-PEAS e Imp | 269.688 | 6.395.928 | 3 mes | 365 | 1,2989E-12 | 1,009E-13 | 2,4806E-12 | 1,0753E-12 | 2,4488E-12 |
| AREA | SRC_477 | Cam_Valpo_202-PEAS e Imp | 269.717 | 6.396.047 | 3 mes | 485 | 9,7943E-13 | 7,6079E-14 | 1,8704E-12 | 8,1082E-13 | 1,8465E-12 |
| AREA | SRC_478 | Cam_Valpo_203-PEAS e Imp | 269.712 | 6.396.106 | 3 mes | 237 | 1,9989E-12 | 1,5527E-13 | 3,8173E-12 | 1,6548E-12 | 3,7683E-12 |
| AREA | SRC_479 | Cam_Valpo_204-PEAS e Imp | 269.657 | 6.396.143 | 3 mes | 271 | 1,7486E-12 | 1,3583E-13 | 3,3394E-12 | 1,4476E-12 | 3,2965E-12 |
| AREA | SRC_480 | Cam_Valpo_205-PEAS e Imp | 269.580 | 6.396.120 | 3 mes | 326 | 1,4541E-12 | 1,1295E-13 | 2,7769E-12 | 1,2038E-12 | 2,7413E-12 |
| AREA | SRC_481 | Cam_Valpo_206-PEAS e Imp | 269.501 | 6.396.070 | 3 mes | 376 | 1,2619E-12 | 9,8018E-14 | 2,4098E-12 | 1,0446E-12 | 2,3789E-12 |
| AREA | SRC_482 | Cam_Valpo_207-PEAS e Imp | 269.359 | 6.396.026 | 3 mes | 594 | 7,998E-13 | 6,2126E-14 | 1,5274E-12 | 6,6211E-13 | 1,5078E-12 |
| AREA | SRC_483 | Cam_Valpo_208-PEAS e Imp | 269.272 | 6.396.023 | 3 mes | 343 | 1,3821E-12 | 1,0735E-13 | 2,6393E-12 | 1,1441E-12 | 2,6055E-12 |
| AREA | SRC_484 | Cam_Valpo_209-PEAS e Imp | 269.222 | 6.396.073 | 3 mes | 276 | 1,7212E-12 | 1,337E-13 | 3,287E-12 | 1,4249E-12 | 3,2448E-12 |
| AREA | SRC_485 | Cam_Valpo_210-PEAS e Imp | 269.210 | 6.396.185 | 3 mes | 446 | 1,0638E-12 | 8,2631E-14 | 2,0315E-12 | 8,8065E-13 | 2,0055E-12 |
| AREA | SRC_486 | Cam_Valpo_211-PEAS e Imp | 269.167 | 6.396.232 | 3 mes | 255 | 1,8583E-12 | 1,4434E-13 | 3,5488E-12 | 1,5384E-12 | 3,5033E-12 |
| AREA | SRC_487 | Cam_Valpo_212-PEAS e Imp | 269.082 | 6.396.226 | 3 mes | 350 | 1,3579E-12 | 1,0548E-13 | 2,5933E-12 | 1,1242E-12 | 2,56E-12 |
| AREA | SRC_488 | Cam_Valpo_213-PEAS e Imp | 268.998 | 6.396.240 | 3 mes | 336 | 1,4148E-12 | 1,0989E-13 | 2,7018E-12 | 1,1712E-12 | 2,6672E-12 |
| AREA | SRC_489 | Cam_Valpo_214-PEAS e Imp | 268.894 | 6.396.300 | 3 mes | 480 | 9,888E-13 | 7,6806E-14 | 1,8883E-12 | 8,1858E-13 | 1,8641E-12 |

**Tabla 20.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 13**

| Tipo<br>AREA | ID<br>SRC_490 | Descripción<br>Cam_Valpo_215-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_490 | Descripción<br>Cam_Valpo_215-PEAS e Imp | [m]<br>268.805 | [m]<br>6.396.381 | [m]<br>6.396.381 | [m2]<br>477 | [g/m2s]<br>9,9419E-13 | [g/m2s]<br>7,7225E-14 | [g/m2s]<br>1,8986E-12 | [g/m2s]<br>8,2304E-13 | [g/m2s]<br>1,8743E-12 |
| AREA | SRC_491 | Cam_Valpo_216-PEAS e Imp | 268.734 | 6.396.481 | 3 mes | 489 | 9,7011E-13 | 7,5355E-14 | 1,8526E-12 | 8,0311E-13 | 1,8289E-12 |
| AREA | SRC_492 | Cam_Valpo_217-PEAS e Imp | 268.692 | 6.396.569 | 3 mes | 388 | 1,2225E-12 | 9,4958E-14 | 2,3346E-12 | 1,012E-12 | 2,3046E-12 |
| AREA | SRC_493 | Cam_Valpo_218-PEAS e Imp | 268.614 | 6.396.686 | 3 mes | 564 | 8,4216E-13 | 6,5416E-14 | 1,6083E-12 | 6,9718E-13 | 1,5877E-12 |
| AREA | SRC_494 | Cam_Valpo_219-PEAS e Imp | 268.551 | 6.396.751 | 3 mes | 365 | 1,3001E-12 | 1,0099E-13 | 2,4829E-12 | 1,0763E-12 | 2,451E-12 |
| AREA | SRC_495 | Cam_Valpo_220-PEAS e Imp | 268.525 | 6.396.834 | 3 mes | 343 | 1,385E-12 | 1,0758E-13 | 2,645E-12 | 1,1466E-12 | 2,6111E-12 |
| AREA | SRC_496 | Cam_Valpo_221-PEAS e Imp | 268.521 | 6.396.918 | 3 mes | 335 | 1,4162E-12 | 1,1001E-13 | 2,7046E-12 | 1,1724E-12 | 2,6699E-12 |
| AREA | SRC_497 | Cam_Valpo_222-PEAS e Imp | 268.510 | 6.396.996 | 3 mes | 312 | 1,5207E-12 | 1,1812E-13 | 2,9041E-12 | 1,2589E-12 | 2,8668E-12 |
| AREA | SRC_498 | Cam_Valpo_223-PEAS e Imp | 268.441 | 6.397.095 | 3 mes | 487 | 9,752E-13 | 7,575E-14 | 1,8624E-12 | 8,0732E-13 | 1,8385E-12 |
| AREA | SRC_499 | Cam_Valpo_224-PEAS e Imp | 268.352 | 6.397.195 | 3 mes | 538 | 8,8267E-13 | 6,8563E-14 | 1,6857E-12 | 7,3072E-13 | 1,664E-12 |
| AREA | SRC_500 | Cam_Valpo_225-PEAS e Imp | 268.295 | 6.397.296 | 3 mes | 460 | 1,0311E-12 | 8,009E-14 | 1,9691E-12 | 8,5357E-13 | 1,9438E-12 |
| AREA | SRC_501 | Cam_Valpo_226-PEAS e Imp | 268.265 | 6.397.370 | 3 mes | 319 | 1,4881E-12 | 1,1559E-13 | 2,8419E-12 | 1,2319E-12 | 2,8054E-12 |
| AREA | SRC_502 | Cam_Valpo_227-PEAS e Imp | 268.236 | 6.397.470 | 3 mes | 415 | 1,1452E-12 | 8,8957E-14 | 2,1871E-12 | 9,4807E-13 | 2,159E-12 |
| AREA | SRC_503 | Cam_Valpo_228-PEAS e Imp | 268.225 | 6.397.539 | 3 mes | 278 | 1,7075E-12 | 1,3263E-13 | 3,2608E-12 | 1,4135E-12 | 3,219E-12 |
| AREA | SRC_504 | Cam_Valpo_229-PEAS e Imp | 268.212 | 6.397.650 | 3 mes | 446 | 1,0633E-12 | 8,259E-14 | 2,0305E-12 | 8,8022E-13 | 2,0045E-12 |
| AREA | SRC_505 | Cam_Valpo_230-PEAS e Imp | 268.292 | 6.397.691 | 3 mes | 353 | 1,3452E-12 | 1,0449E-13 | 2,5689E-12 | 1,1136E-12 | 2,5359E-12 |
| AREA | SRC_506 | Cam_Valpo_231-PEAS e Imp | 268.324 | 6.397.741 | 3 mes | 244 | 1,9448E-12 | 1,5106E-13 | 3,714E-12 | 1,61E-12 | 3,6664E-12 |
| AREA | SRC_507 | Cam_Valpo_232-PEAS e Imp | 268.344 | 6.397.809 | 3 mes | 285 | 1,6685E-12 | 1,296E-13 | 3,1863E-12 | 1,3812E-12 | 3,1454E-12 |
| AREA | SRC_508 | Cam_Valpo_233-PEAS e Imp | 268.317 | 6.397.871 | 3 mes | 277 | 1,7113E-12 | 1,3293E-13 | 3,268E-12 | 1,4167E-12 | 3,2261E-12 |
| AREA | SRC_509 | Cam_Valpo_234-PEAS e Imp | 268.289 | 6.397.931 | 3 mes | 263 | 1,8019E-12 | 1,3997E-13 | 3,4412E-12 | 1,4917E-12 | 3,3971E-12 |
| AREA | SRC_510 | Cam_Valpo_235-PEAS e Imp | 268.281 | 6.397.993 | 3 mes | 246 | 1,9281E-12 | 1,4977E-13 | 3,6821E-12 | 1,5962E-12 | 3,6349E-12 |
| AREA | SRC_511 | Cam_Valpo_236-PEAS e Imp | 268.325 | 6.398.057 | 3 mes | 307 | 1,5457E-12 | 1,2007E-13 | 2,9519E-12 | 1,2796E-12 | 2,914E-12 |
| AREA | SRC_512 | Cam_Valpo_237-PEAS e Imp | 268.339 | 6.398.092 | 3 mes | 154 | 3,0802E-12 | 2,3926E-13 | 5,8824E-12 | 2,55E-12 | 5,807E-12 |
| AREA | SRC_513 | Cam_Valpo_238-PEAS e Imp | 268.362 | 6.398.151 | 3 mes | 252 | 1,8871E-12 | 1,4658E-13 | 3,6038E-12 | 1,5622E-12 | 3,5576E-12 |
| AREA | SRC_514 | Cam_Valpo_239-PEAS e Imp | 268.383 | 6.398.192 | 3 mes | 185 | 2,5634E-12 | 1,9912E-13 | 4,8954E-12 | 2,1221E-12 | 4,8326E-12 |
| AREA | SRC_515 | Cam_Valpo_240-PEAS e Imp | 268.355 | 6.398.247 | 3 mes | 250 | 1,8975E-12 | 1,4739E-13 | 3,6237E-12 | 1,5709E-12 | 3,5773E-12 |
| AREA | SRC_516 | Cam_Valpo_241-PEAS e Imp | 268.227 | 6.398.303 | 3 mes | 567 | 8,3746E-13 | 6,5051E-14 | 1,5993E-12 | 6,9329E-13 | 1,5788E-12 |
| AREA | SRC_517 | Cam_Valpo_242-PEAS e Imp | 268.140 | 6.398.362 | 3 mes | 419 | 1,1334E-12 | 8,804E-14 | 2,1645E-12 | 9,383E-13 | 2,1367E-12 |
| AREA | SRC_518 | Cam_Valpo_243-PEAS e Imp | 268.089 | 6.398.427 | 3 mes | 325 | 1,4587E-12 | 1,1331E-13 | 2,7858E-12 | 1,2076E-12 | 2,75E-12 |
| AREA | SRC_519 | Cam_Valpo_244-PEAS e Imp | 268.005 | 6.398.483 | 3 mes | 406 | 1,1688E-12 | 9,0788E-14 | 2,2321E-12 | 9,6759E-13 | 2,2035E-12 |
| AREA | SRC_520 | Cam_Valpo_245-PEAS e Imp | 267.956 | 6.398.553 | 3 mes | 338 | 1,4034E-12 | 1,0901E-13 | 2,6801E-12 | 1,1618E-12 | 2,6457E-12 |
| AREA | SRC_521 | Cam_Valpo_246-PEAS e Imp | 267.920 | 6.398.673 | 3 mes | 499 | 9,5141E-13 | 7,3902E-14 | 1,8169E-12 | 7,8762E-13 | 1,7936E-12 |
| AREA | SRC_522 | Cam_Valpo_247-PEAS e Imp | 267.908 | 6.398.749 | 3 mes | 308 | 1,5394E-12 | 1,1958E-13 | 2,9399E-12 | 1,2744E-12 | 2,9022E-12 |
| AREA | SRC_523 | Cam_Valpo_248-PEAS e Imp | 267.894 | 6.398.771 | 3 mes | 107 | 4,4196E-12 | 3,433E-13 | 8,4403E-12 | 3,6588E-12 | 8,3321E-12 |
| AREA | SRC_524 | Cam_Valpo_249-PEAS e Imp | 267.791 | 6.398.823 | 3 mes | 467 | 1,0175E-12 | 7,9034E-14 | 1,9431E-12 | 8,4232E-13 | 1,9182E-12 |

**Tabla 21.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 14**

| Tipo<br>AREA | ID<br>SRC_525 | Descripción<br>Cam_Valpo_250-PEAS e Imp | X1 | Y1 | Ciclo<br>operación<br>3 mes | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_525 | Descripción<br>Cam_Valpo_250-PEAS e Imp | [m]<br>267.747 | [m]<br>6.398.849 | [m]<br>6.398.849 | [m2]<br>204 | [g/m2s]<br>2,327E-12 | [g/m2s]<br>1,8075E-13 | [g/m2s]<br>4,4439E-12 | [g/m2s]<br>1,9264E-12 | [g/m2s]<br>4,3869E-12 |
| AREA | SRC_526 | Cam_Valpo_251-PEAS e Imp | 267.699 | 6.398.875 | 3 mes | 217 | 2,1861E-12 | 1,6981E-13 | 4,1749E-12 | 1,8098E-12 | 4,1213E-12 |
| AREA | SRC_527 | Cam_Valpo_252-PEAS e Imp | 267.673 | 6.398.943 | 3 mes | 286 | 1,6603E-12 | 1,2897E-13 | 3,1708E-12 | 1,3745E-12 | 3,1301E-12 |
| AREA | SRC_528 | Cam_Valpo_253-PEAS e Imp | 267.740 | 6.399.152 | 3 mes | 872 | 5,444E-13 | 4,2287E-14 | 1,0397E-12 | 4,5068E-13 | 1,0263E-12 |
| AREA | SRC_529 | Cam_Valpo_254-PEAS e Imp | 267.754 | 6.399.259 | 3 mes | 434 | 1,0929E-12 | 8,489E-14 | 2,0871E-12 | 9,0473E-13 | 2,0603E-12 |
| AREA | SRC_530 | Cam_Valpo_255-PEAS e Imp | 267.756 | 6.399.372 | 3 mes | 453 | 1,0481E-12 | 8,1411E-14 | 2,0015E-12 | 8,6765E-13 | 1,9759E-12 |
| AREA | SRC_531 | Cam_Valpo_256-PEAS e Imp | 267.702 | 6.399.478 | 3 mes | 480 | 9,8891E-13 | 7,6815E-14 | 1,8885E-12 | 8,1867E-13 | 1,8643E-12 |
| AREA | SRC_532 | Cam_Valpo_257-PEAS e Imp | 267.740 | 6.399.547 | 3 mes | 307 | 1,5452E-12 | 1,2003E-13 | 2,9509E-12 | 1,2792E-12 | 2,9131E-12 |
| AREA | SRC_533 | Cam_Valpo_258-PEAS e Imp | 267.742 | 6.399.624 | 3 mes | 312 | 1,5237E-12 | 1,1835E-13 | 2,9098E-12 | 1,2614E-12 | 2,8725E-12 |
| AREA | SRC_534 | Cam_Valpo_259-PEAS e Imp | 267.731 | 6.399.695 | 3 mes | 288 | 1,6507E-12 | 1,2822E-13 | 3,1524E-12 | 1,3665E-12 | 3,1119E-12 |
| AREA | SRC_535 | Cam_Valpo_260-PEAS e Imp | 267.682 | 6.399.788 | 3 mes | 426 | 1,1151E-12 | 8,662E-14 | 2,1296E-12 | 9,2317E-13 | 2,1023E-12 |
| AREA | SRC_536 | Cam_Valpo_261-PEAS e Imp | 267.661 | 6.399.830 | 3 mes | 187 | 2,5381E-12 | 1,9715E-13 | 4,847E-12 | 2,1011E-12 | 4,7848E-12 |
| AREA | SRC_540 | Cam_Cat_1-PTAS | 273.043 | 6.387.323 | 10 meses | 383 | 3,328E-14 | 2,5851E-15 | 6,3555E-14 | 2,7551E-14 | 6,274E-14 |
| AREA | SRC_541 | Cam_Cat_2-PTAS | 273.206 | 6.387.558 | 10 meses | 1.145 | 1,1141E-14 | 8,6541E-16 | 2,1277E-14 | 9,2232E-15 | 2,1004E-14 |
| AREA | SRC_542 | Cam_Cat_3-PTAS | 273.308 | 6.387.612 | 10 meses | 456 | 2,7976E-14 | 2,1731E-15 | 5,3426E-14 | 2,316E-14 | 5,2741E-14 |
| AREA | SRC_543 | Cam_Cat_4-PTAS | 273.511 | 6.387.668 | 10 meses | 844 | 1,5122E-14 | 1,1747E-15 | 2,888E-14 | 1,2519E-14 | 2,8509E-14 |
| AREA | SRC_544 | Cam_Cat_5-PTAS | 273.721 | 6.387.707 | 10 meses | 853 | 1,495E-14 | 1,1612E-15 | 2,855E-14 | 1,2376E-14 | 2,8184E-14 |
| AREA | SRC_545 | Cam_Cat_6-PTAS | 273.880 | 6.387.880 | 10 meses | 945 | 1,3496E-14 | 1,0483E-15 | 2,5773E-14 | 1,1172E-14 | 2,5443E-14 |
| AREA | SRC_546 | Cam_Cat_7-PTAS | 273.982 | 6.387.934 | 10 meses | 458 | 2,7883E-14 | 2,1658E-15 | 5,3248E-14 | 2,3083E-14 | 5,2566E-14 |
| AREA | SRC_547 | Cam_Cat_8-PTAS | 274.178 | 6.387.916 | 10 meses | 782 | 1,6309E-14 | 1,2668E-15 | 3,1146E-14 | 1,3502E-14 | 3,0747E-14 |
| AREA | SRC_548 | Cam_Cat_9-PTAS | 274.216 | 6.387.945 | 10 meses | 195 | 6,526E-14 | 5,0692E-15 | 1,2463E-13 | 5,4025E-14 | 1,2303E-13 |
| AREA | SRC_549 | Cam_Cat_10-PTAS | 274.213 | 6.388.017 | 10 meses | 296 | 4,3155E-14 | 3,3522E-15 | 8,2415E-14 | 3,5726E-14 | 8,1358E-14 |
| AREA | SRC_550 | Cam_Cat_11-PTAS | 274.177 | 6.388.250 | 10 meses | 942 | 1,3549E-14 | 1,0525E-15 | 2,5875E-14 | 1,1217E-14 | 2,5543E-14 |
| AREA | SRC_551 | Cam_Cat_12-PTAS | 274.185 | 6.388.365 | 10 meses | 458 | 2,7833E-14 | 2,162E-15 | 5,3153E-14 | 2,3042E-14 | 5,2472E-14 |
| AREA | SRC_552 | Cam_Cat_13-PTAS | 274.352 | 6.388.558 | 10 meses | 1.017 | 1,2545E-14 | 9,7442E-16 | 2,3957E-14 | 1,0385E-14 | 2,365E-14 |
| AREA | SRC_553 | Cam_Cat_14-PTAS | 274.654 | 6.388.846 | 10 meses | 1.667 | 7,6526E-15 | 5,9443E-16 | 1,4614E-14 | 6,3353E-15 | 1,4427E-14 |
| AREA | SRC_554 | Cam_Cat_15-PTAS | 274.745 | 6.388.895 | 10 meses | 410 | 3,1129E-14 | 2,418E-15 | 5,9448E-14 | 2,577E-14 | 5,8686E-14 |
| AREA | SRC_555 | Cam_Cat_16-PTAS | 274.834 | 6.388.862 | 10 meses | 371 | 3,4375E-14 | 2,6701E-15 | 6,5646E-14 | 2,8457E-14 | 6,4804E-14 |
| AREA | SRC_556 | Cam_Cat_17-PTAS | 274.882 | 6.388.794 | 10 meses | 331 | 3,8507E-14 | 2,9911E-15 | 7,3538E-14 | 3,1878E-14 | 7,2594E-14 |
| AREA | SRC_557 | Cam_Cat_18-PTAS | 274.979 | 6.388.768 | 10 meses | 407 | 3,1372E-14 | 2,4369E-15 | 5,9912E-14 | 2,5971E-14 | 5,9144E-14 |
| AREA | SRC_558 | Cam_Cat_19-PTAS | 275.069 | 6.388.799 | 10 meses | 384 | 3,3207E-14 | 2,5794E-15 | 6,3417E-14 | 2,7491E-14 | 6,2603E-14 |
| AREA | SRC_559 | Cam_Cat_20-PTAS | 275.059 | 6.388.911 | 10 meses | 460 | 2,7762E-14 | 2,1564E-15 | 5,3017E-14 | 2,2983E-14 | 5,2337E-14 |
| AREA | SRC_560 | Cam_Cat_21-PTAS | 275.040 | 6.389.003 | 10 meses | 374 | 3,4105E-14 | 2,6492E-15 | 6,5131E-14 | 2,8234E-14 | 6,4296E-14 |
| AREA | SRC_561 | Cam_Cat_22-PTAS | 274.958 | 6.389.092 | 10 meses | 489 | 2,6082E-14 | 2,026E-15 | 4,981E-14 | 2,1592E-14 | 4,9171E-14 |
| AREA | SRC_562 | Cam_Cat_23-PTAS | 274.915 | 6.389.184 | 10 meses | 402 | 3,1718E-14 | 2,4637E-15 | 6,0572E-14 | 2,6258E-14 | 5,9795E-14 |

**Tabla 22.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 15**

| Tipo<br>AREA | ID<br>SRC_563 | Descripción<br>Cam_Cat_24-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_563 | Descripción<br>Cam_Cat_24-PTAS | [m]<br>274.946 | [m]<br>6.389.307 | [m]<br>6.389.307 | [m2]<br>503 | [g/m2s]<br>2,5372E-14 | [g/m2s]<br>1,9708E-15 | [g/m2s]<br>4,8454E-14 | [g/m2s]<br>2,1005E-14 | [g/m2s]<br>4,7833E-14 |
| AREA | SRC_564 | Cam_Cat_25-PTAS | 275.049 | 6.389.374 | 10 meses | 485 | 2,63E-14 | 2,0429E-15 | 5,0226E-14 | 2,1772E-14 | 4,9581E-14 |
| AREA | SRC_565 | Cam_Cat_26-PTAS | 275.181 | 6.389.406 | 10 meses | 541 | 2,3564E-14 | 1,8304E-15 | 4,5002E-14 | 1,9508E-14 | 4,4424E-14 |
| AREA | SRC_566 | Cam_Cat_27-PTAS | 275.286 | 6.389.385 | 10 meses | 424 | 3,0063E-14 | 2,3352E-15 | 5,7412E-14 | 2,4887E-14 | 5,6675E-14 |
| AREA | SRC_567 | Cam_Cat_28-PTAS | 275.372 | 6.389.387 | 10 meses | 345 | 3,697E-14 | 2,8717E-15 | 7,0603E-14 | 3,0606E-14 | 6,9697E-14 |
| AREA | SRC_568 | Cam_Cat_29-PTAS | 275.519 | 6.389.442 | 10 meses | 633 | 2,0145E-14 | 1,5648E-15 | 3,8471E-14 | 1,6677E-14 | 3,7978E-14 |
| AREA | SRC_569 | Cam_Cat_30-PTAS | 275.575 | 6.389.512 | 10 meses | 360 | 3,54E-14 | 2,7498E-15 | 6,7605E-14 | 2,9306E-14 | 6,6738E-14 |
| AREA | SRC_570 | Cam_Cat_31-PTAS | 275.579 | 6.389.623 | 10 meses | 447 | 2,8519E-14 | 2,2153E-15 | 5,4464E-14 | 2,361E-14 | 5,3766E-14 |
| AREA | SRC_571 | Cam_Cat_32-PTAS | 275.473 | 6.389.738 | 10 meses | 630 | 2,0262E-14 | 1,5739E-15 | 3,8695E-14 | 1,6774E-14 | 3,8199E-14 |
| AREA | SRC_572 | Cam_Cat_33-PTAS | 275.397 | 6.389.809 | 10 meses | 419 | 3,0433E-14 | 2,3639E-15 | 5,8119E-14 | 2,5194E-14 | 5,7374E-14 |
| AREA | SRC_573 | Cam_Cat_34-PTAS | 275.382 | 6.389.918 | 10 meses | 433 | 2,9477E-14 | 2,2896E-15 | 5,6292E-14 | 2,4402E-14 | 5,557E-14 |
| AREA | SRC_574 | Cam_Cat_35-PTAS | 275.487 | 6.390.018 | 10 meses | 577 | 2,2122E-14 | 1,7184E-15 | 4,2248E-14 | 1,8314E-14 | 4,1706E-14 |
| AREA | SRC_575 | Cam_Cat_36-PTAS | 275.630 | 6.390.045 | 10 meses | 576 | 2,2134E-14 | 1,7193E-15 | 4,227E-14 | 1,8324E-14 | 4,1728E-14 |
| AREA | SRC_576 | Cam_Cat_37-PTAS | 275.763 | 6.390.025 | 10 meses | 533 | 2,3937E-14 | 1,8593E-15 | 4,5713E-14 | 1,9816E-14 | 4,5126E-14 |
| AREA | SRC_577 | Cam_Cat_38-PTAS | 275.861 | 6.389.993 | 10 meses | 412 | 3,0985E-14 | 2,4068E-15 | 5,9173E-14 | 2,5651E-14 | 5,8414E-14 |
| AREA | SRC_578 | Cam_Cat_39-PTAS | 276.044 | 6.389.963 | 10 meses | 743 | 1,7172E-14 | 1,3339E-15 | 3,2795E-14 | 1,4216E-14 | 3,2374E-14 |
| AREA | SRC_579 | Cam_Cat_40-PTAS | 276.114 | 6.389.925 | 10 meses | 317 | 4,0248E-14 | 3,1263E-15 | 7,6863E-14 | 3,3319E-14 | 7,5877E-14 |
| AREA | SRC_580 | Cam_Cat_41-PTAS | 276.133 | 6.389.885 | 10 meses | 173 | 7,3768E-14 | 5,7301E-15 | 1,4088E-13 | 6,1069E-14 | 1,3907E-13 |
| AREA | SRC_581 | Cam_Cat_42-PTAS | 276.158 | 6.389.818 | 10 meses | 287 | 4,4473E-14 | 3,4545E-15 | 8,4932E-14 | 3,6817E-14 | 8,3843E-14 |
| AREA | SRC_582 | Cam_Cat_43-PTAS | 276.157 | 6.389.659 | 10 meses | 633 | 2,0158E-14 | 1,5658E-15 | 3,8496E-14 | 1,6688E-14 | 3,8003E-14 |
| AREA | SRC_583 | Cam_Cat_44-PTAS | 276.172 | 6.389.529 | 10 meses | 521 | 2,4481E-14 | 1,9016E-15 | 4,6752E-14 | 2,0267E-14 | 4,6152E-14 |
| AREA | SRC_584 | Cam_Cat_45-PTAS | 276.275 | 6.389.477 | 10 meses | 468 | 2,724E-14 | 2,1159E-15 | 5,202E-14 | 2,255E-14 | 5,1353E-14 |
| AREA | SRC_585 | Cam_Cat_46-PTAS | 276.411 | 6.389.458 | 10 meses | 553 | 2,3053E-14 | 1,7907E-15 | 4,4025E-14 | 1,9085E-14 | 4,3461E-14 |
| AREA | SRC_586 | Cam_Cat_47-PTAS | 276.501 | 6.389.471 | 10 meses | 366 | 3,4832E-14 | 2,7056E-15 | 6,652E-14 | 2,8836E-14 | 6,5667E-14 |
| AREA | SRC_587 | Cam_Cat_48-PTAS | 276.706 | 6.389.673 | 10 meses | 1.151 | 1,1079E-14 | 8,6058E-16 | 2,1158E-14 | 9,1717E-15 | 2,0886E-14 |
| AREA | SRC_588 | Cam_Cat_49-PTAS | 277.353 | 6.390.498 | 10 meses | 4.195 | 3,0407E-15 | 2,3619E-16 | 5,8069E-15 | 2,5172E-15 | 5,7324E-15 |
| AREA | SRC_589 | Cam_Cat_50-PTAS | 277.494 | 6.390.575 | 10 meses | 640 | 1,9932E-14 | 1,5482E-15 | 3,8064E-14 | 1,65E-14 | 3,7576E-14 |
| AREA | SRC_590 | Cam_Cat_51-PTAS | 279.440 | 6.391.244 | 10 meses | 8.224 | 1,5512E-15 | 1,205E-16 | 2,9625E-15 | 1,2842E-15 | 2,9245E-15 |
| AREA | SRC_591 | Cam_Cat_52-PTAS | 283.346 | 6.393.239 | 10 meses | 17.541 | 7,2727E-16 | 5,6492E-17 | 1,3889E-15 | 6,0207E-16 | 1,3711E-15 |
| AREA | SRC_592 | Cam_Cat_53-PTAS | 287.745 | 6.394.661 | 10 meses | 18.483 | 6,9019E-16 | 5,3612E-17 | 1,3181E-15 | 5,7138E-16 | 1,3012E-15 |
| AREA | SRC_593 | Cam_Pta_1-PTAS | 273.147 | 6.383.634 | 10 meses | 1.866 | 7,2654E-15 | 2,6307E-16 | 1,0848E-14 | 5,1083E-15 | 1,0451E-14 |
| AREA | SRC_594 | Cam_Pta_2-PTAS | 273.165 | 6.383.642 | 10 meses | 81 | 1,6773E-13 | 6,0731E-15 | 2,5043E-13 | 1,1793E-13 | 2,4127E-13 |
| AREA | SRC_595 | Cam_Pta_3-PTAS | 273.189 | 6.383.637 | 10 meses | 94 | 1,4404E-13 | 5,2155E-15 | 2,1507E-13 | 1,0127E-13 | 2,072E-13 |
| AREA | SRC_596 | Cam_Pta_4-PTAS | 273.241 | 6.383.562 | 10 meses | 360 | 3,7673E-14 | 1,364E-15 | 5,6248E-14 | 2,6487E-14 | 5,419E-14 |
| AREA | SRC_597 | Cam_Pta_5-PTAS | 273.289 | 6.383.445 | 10 meses | 506 | 2,6822E-14 | 9,7117E-16 | 4,0048E-14 | 1,8858E-14 | 3,8582E-14 |

**Tabla 23.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 16**

| Tipo<br>AREA | ID<br>SRC_598 | Descripción<br>Cam_Pta_6-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_598 | Descripción<br>Cam_Pta_6-PTAS | [m]<br>273.304 | [m]<br>6.383.402 | [m]<br>6.383.402 | [m2]<br>180 | [g/m2s]<br>7,5494E-14 | [g/m2s]<br>2,7335E-15 | [g/m2s]<br>1,1272E-13 | [g/m2s]<br>5,3079E-14 | [g/m2s]<br>1,0859E-13 |
| AREA | SRC_599 | Cam_Pta_7-PTAS | 273.331 | 6.383.382 | 10 meses | 138 | 9,7948E-14 | 3,5465E-15 | 1,4624E-13 | 6,8866E-14 | 1,4089E-13 |
| AREA | SRC_600 | Cam_Pta_8-PTAS | 273.361 | 6.383.362 | 10 meses | 146 | 9,3159E-14 | 3,3731E-15 | 1,3909E-13 | 6,5499E-14 | 1,34E-13 |
| AREA | SRC_601 | Cam_Pta_9-PTAS | 273.393 | 6.383.346 | 10 meses | 144 | 9,4177E-14 | 3,41E-15 | 1,4061E-13 | 6,6215E-14 | 1,3547E-13 |
| AREA | SRC_602 | Cam_Pta_10-PTAS | 273.413 | 6.383.324 | 10 meses | 116 | 1,1658E-13 | 4,2212E-15 | 1,7407E-13 | 8,1968E-14 | 1,677E-13 |
| AREA | SRC_603 | Cam_Pta_11-PTAS | 273.447 | 6.383.229 | 10 meses | 400 | 3,3898E-14 | 1,2274E-15 | 5,0613E-14 | 2,3834E-14 | 4,8761E-14 |
| AREA | SRC_604 | Cam_Pta_12-PTAS | 273.463 | 6.383.220 | 10 meses | 80 | 1,6924E-13 | 6,1277E-15 | 2,5268E-13 | 1,1899E-13 | 2,4344E-13 |
| AREA | SRC_605 | Cam_Pta_13-PTAS | 273.473 | 6.383.218 | 10 meses | 45 | 3,0051E-13 | 1,0881E-14 | 4,4869E-13 | 2,1129E-13 | 4,3227E-13 |
| AREA | SRC_606 | Cam_Pta_14-PTAS | 273.519 | 6.383.228 | 10 meses | 189 | 7,1927E-14 | 2,6043E-15 | 1,0739E-13 | 5,0572E-14 | 1,0346E-13 |
| AREA | SRC_607 | Cam_Valpo_1-PTAS | 267.407 | 6.370.003 | 10 meses | 9.182 | 1,3894E-15 | 1,0792E-16 | 2,6533E-15 | 1,1502E-15 | 2,6193E-15 |
| AREA | SRC_608 | Cam_Valpo_2-PTAS | 267.402 | 6.370.088 | 10 meses | 338 | 3,771E-14 | 2,9292E-15 | 7,2016E-14 | 3,1218E-14 | 7,1092E-14 |
| AREA | SRC_609 | Cam_Valpo_3-PTAS | 267.699 | 6.371.506 | 10 meses | 5.789 | 2,2037E-15 | 1,7117E-16 | 4,2084E-15 | 1,8243E-15 | 4,1544E-15 |
| AREA | SRC_610 | Cam_Valpo_4-PTAS | 267.700 | 6.371.619 | 10 meses | 452 | 2,8223E-14 | 2,1923E-15 | 5,3899E-14 | 2,3365E-14 | 5,3208E-14 |
| AREA | SRC_611 | Cam_Valpo_5-PTAS | 267.517 | 6.371.917 | 10 meses | 1.401 | 9,1027E-15 | 7,0707E-16 | 1,7384E-14 | 7,5357E-15 | 1,7161E-14 |
| AREA | SRC_612 | Cam_Valpo_6-PTAS | 267.499 | 6.371.980 | 10 meses | 261 | 4,8859E-14 | 3,7952E-15 | 9,3307E-14 | 4,0448E-14 | 9,2111E-14 |
| AREA | SRC_613 | Cam_Valpo_7-PTAS | 267.496 | 6.372.042 | 10 meses | 247 | 5,1642E-14 | 4,0114E-15 | 9,8622E-14 | 4,2752E-14 | 9,7357E-14 |
| AREA | SRC_614 | Cam_Valpo_8-PTAS | 267.518 | 6.372.113 | 10 meses | 294 | 4,3322E-14 | 3,3651E-15 | 8,2734E-14 | 3,5865E-14 | 8,1673E-14 |
| AREA | SRC_615 | Cam_Valpo_9-PTAS | 267.547 | 6.372.151 | 10 meses | 187 | 6,8062E-14 | 5,2868E-15 | 1,2998E-13 | 5,6345E-14 | 1,2831E-13 |
| AREA | SRC_616 | Cam_Valpo_10-PTAS | 267.569 | 6.372.177 | 10 meses | 137 | 9,3103E-14 | 7,2319E-15 | 1,778E-13 | 7,7075E-14 | 1,7552E-13 |
| AREA | SRC_617 | Cam_Valpo_11-PTAS | 267.738 | 6.372.319 | 10 meses | 880 | 1,4499E-14 | 1,1263E-15 | 2,769E-14 | 1,2003E-14 | 2,7335E-14 |
| AREA | SRC_618 | Cam_Valpo_12-PTAS | 267.762 | 6.372.358 | 10 meses | 187 | 6,8377E-14 | 5,3113E-15 | 1,3058E-13 | 5,6606E-14 | 1,2891E-13 |
| AREA | SRC_619 | Cam_Valpo_13-PTAS | 267.783 | 6.372.410 | 10 meses | 225 | 5,682E-14 | 4,4136E-15 | 1,0851E-13 | 4,7039E-14 | 1,0712E-13 |
| AREA | SRC_620 | Cam_Valpo_14-PTAS | 267.855 | 6.372.669 | 10 meses | 1.076 | 1,186E-14 | 9,2126E-16 | 2,265E-14 | 9,8185E-15 | 2,2359E-14 |
| AREA | SRC_621 | Cam_Valpo_15-PTAS | 267.848 | 6.372.720 | 10 meses | 208 | 6,1396E-14 | 4,769E-15 | 1,1725E-13 | 5,0827E-14 | 1,1575E-13 |
| AREA | SRC_622 | Cam_Valpo_16-PTAS | 267.715 | 6.373.066 | 10 meses | 1.484 | 8,5959E-15 | 6,677E-16 | 1,6416E-14 | 7,1161E-15 | 1,6205E-14 |
| AREA | SRC_623 | Cam_Valpo_17-PTAS | 267.705 | 6.373.122 | 10 meses | 225 | 5,6589E-14 | 4,3957E-15 | 1,0807E-13 | 4,6847E-14 | 1,0668E-13 |
| AREA | SRC_624 | Cam_Valpo_18-PTAS | 267.701 | 6.373.182 | 10 meses | 241 | 5,2884E-14 | 4,1079E-15 | 1,0099E-13 | 4,378E-14 | 9,9699E-14 |
| AREA | SRC_625 | Cam_Valpo_19-PTAS | 267.704 | 6.373.237 | 10 meses | 218 | 5,8528E-14 | 4,5462E-15 | 1,1177E-13 | 4,8452E-14 | 1,1034E-13 |
| AREA | SRC_626 | Cam_Valpo_20-PTAS | 267.713 | 6.373.309 | 10 meses | 291 | 4,3799E-14 | 3,4022E-15 | 8,3644E-14 | 3,6259E-14 | 8,2572E-14 |
| AREA | SRC_627 | Cam_Valpo_21-PTAS | 267.741 | 6.373.522 | 10 meses | 860 | 1,4831E-14 | 1,152E-15 | 2,8323E-14 | 1,2278E-14 | 2,796E-14 |
| AREA | SRC_628 | Cam_Valpo_22-PTAS | 267.757 | 6.373.574 | 10 meses | 214 | 5,9653E-14 | 4,6336E-15 | 1,1392E-13 | 4,9384E-14 | 1,1246E-13 |
| AREA | SRC_629 | Cam_Valpo_23-PTAS | 267.777 | 6.373.617 | 10 meses | 187 | 6,8103E-14 | 5,29E-15 | 1,3006E-13 | 5,6379E-14 | 1,2839E-13 |
| AREA | SRC_630 | Cam_Valpo_24-PTAS | 267.817 | 6.373.719 | 10 meses | 441 | 2,8918E-14 | 2,2463E-15 | 5,5225E-14 | 2,394E-14 | 5,4517E-14 |
| AREA | SRC_631 | Cam_Valpo_25-PTAS | 267.843 | 6.373.782 | 10 meses | 273 | 4,68E-14 | 3,6353E-15 | 8,9376E-14 | 3,8744E-14 | 8,823E-14 |
| AREA | SRC_632 | Cam_Valpo_26-PTAS | 267.877 | 6.373.831 | 10 meses | 236 | 5,4048E-14 | 4,1983E-15 | 1,0322E-13 | 4,4744E-14 | 1,0189E-13 |

**Tabla 24.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 17**

| Tipo<br>AREA | ID<br>SRC_633 | Descripción<br>Cam_Valpo_27-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_633 | Descripción<br>Cam_Valpo_27-PTAS | [m]<br>267.910 | [m]<br>6.373.883 | [m]<br>6.373.883 | [m2]<br>246 | [g/m2s]<br>5,1832E-14 | [g/m2s]<br>4,0261E-15 | [g/m2s]<br>9,8984E-14 | [g/m2s]<br>4,2909E-14 | [g/m2s]<br>9,7715E-14 |
| AREA | SRC_634 | Cam_Valpo_28-PTAS | 268.105 | 6.374.174 | 10 meses | 1.400 | 9,1152E-15 | 7,0804E-16 | 1,7407E-14 | 7,546E-15 | 1,7184E-14 |
| AREA | SRC_635 | Cam_Valpo_29-PTAS | 268.274 | 6.374.430 | 10 meses | 1.228 | 1,0388E-14 | 8,0689E-16 | 1,9838E-14 | 8,5995E-15 | 1,9583E-14 |
| AREA | SRC_636 | Cam_Valpo_30-PTAS | 268.317 | 6.374.478 | 10 meses | 254 | 5,0154E-14 | 3,8958E-15 | 9,5781E-14 | 4,152E-14 | 9,4552E-14 |
| AREA | SRC_637 | Cam_Valpo_31-PTAS | 268.347 | 6.374.502 | 10 meses | 154 | 8,2593E-14 | 6,4156E-15 | 1,5773E-13 | 6,8375E-14 | 1,5571E-13 |
| AREA | SRC_638 | Cam_Valpo_32-PTAS | 269.602 | 6.375.295 | 10 meses | 5.936 | 2,1492E-15 | 1,6695E-16 | 4,1045E-15 | 1,7792E-15 | 4,0518E-15 |
| AREA | SRC_639 | Cam_Valpo_33-PTAS | 270.646 | 6.375.956 | 10 meses | 4.938 | 2,5832E-15 | 2,0066E-16 | 4,9333E-15 | 2,1385E-15 | 4,87E-15 |
| AREA | SRC_640 | Cam_Valpo_34-PTAS | 270.700 | 6.375.970 | 10 meses | 221 | 5,7791E-14 | 4,489E-15 | 1,1037E-13 | 4,7842E-14 | 1,0895E-13 |
| AREA | SRC_641 | Cam_Valpo_35-PTAS | 270.759 | 6.375.972 | 10 meses | 232 | 5,498E-14 | 4,2707E-15 | 1,05E-13 | 4,5515E-14 | 1,0365E-13 |
| AREA | SRC_642 | Cam_Valpo_36-PTAS | 270.817 | 6.375.960 | 10 meses | 238 | 5,3638E-14 | 4,1664E-15 | 1,0243E-13 | 4,4404E-14 | 1,0112E-13 |
| AREA | SRC_643 | Cam_Valpo_37-PTAS | 271.210 | 6.375.788 | 10 meses | 1.711 | 7,4561E-15 | 5,7916E-16 | 1,4239E-14 | 6,1725E-15 | 1,4056E-14 |
| AREA | SRC_644 | Cam_Valpo_38-PTAS | 271.299 | 6.375.786 | 10 meses | 362 | 3,5235E-14 | 2,7369E-15 | 6,7289E-14 | 2,9169E-14 | 6,6426E-14 |
| AREA | SRC_645 | Cam_Valpo_39-PTAS | 271.410 | 6.375.784 | 10 meses | 444 | 2,8726E-14 | 2,2314E-15 | 5,4859E-14 | 2,3781E-14 | 5,4156E-14 |
| AREA | SRC_646 | Cam_Valpo_40-PTAS | 271.537 | 6.375.829 | 10 meses | 540 | 2,3626E-14 | 1,8352E-15 | 4,512E-14 | 1,9559E-14 | 4,4541E-14 |
| AREA | SRC_647 | Cam_Valpo_41-PTAS | 271.698 | 6.375.908 | 10 meses | 718 | 1,7776E-14 | 1,3808E-15 | 3,3948E-14 | 1,4716E-14 | 3,3513E-14 |
| AREA | SRC_648 | Cam_Valpo_42-PTAS | 271.943 | 6.376.040 | 10 meses | 1.111 | 1,1478E-14 | 8,9158E-16 | 2,192E-14 | 9,5022E-15 | 2,1639E-14 |
| AREA | SRC_649 | Cam_Valpo_43-PTAS | 272.216 | 6.376.245 | 10 meses | 1.366 | 9,3401E-15 | 7,2551E-16 | 1,7837E-14 | 7,7323E-15 | 1,7608E-14 |
| AREA | SRC_650 | Cam_Valpo_44-PTAS | 272.308 | 6.376.283 | 10 meses | 397 | 3,2149E-14 | 2,4972E-15 | 6,1395E-14 | 2,6614E-14 | 6,0608E-14 |
| AREA | SRC_651 | Cam_Valpo_45-PTAS | 272.828 | 6.376.412 | 10 meses | 2.140 | 5,9625E-15 | 4,6315E-16 | 1,1387E-14 | 4,9361E-15 | 1,1241E-14 |
| AREA | SRC_652 | Cam_Valpo_46-PTAS | 272.961 | 6.376.463 | 10 meses | 573 | 2,2267E-14 | 1,7296E-15 | 4,2524E-14 | 1,8434E-14 | 4,1979E-14 |
| AREA | SRC_653 | Cam_Valpo_47-PTAS | 273.101 | 6.376.548 | 10 meses | 656 | 1,9434E-14 | 1,5096E-15 | 3,7113E-14 | 1,6088E-14 | 3,6637E-14 |
| AREA | SRC_654 | Cam_Valpo_48-PTAS | 273.683 | 6.376.890 | 10 meses | 2.700 | 4,7248E-15 | 3,6701E-16 | 9,0231E-15 | 3,9114E-15 | 8,9074E-15 |
| AREA | SRC_655 | Cam_Valpo_49-PTAS | 273.729 | 6.376.911 | 10 meses | 199 | 6,4215E-14 | 4,988E-15 | 1,2263E-13 | 5,316E-14 | 1,2106E-13 |
| AREA | SRC_656 | Cam_Valpo_50-PTAS | 273.841 | 6.376.934 | 10 meses | 455 | 2,8007E-14 | 2,1755E-15 | 5,3485E-14 | 2,3185E-14 | 5,2799E-14 |
| AREA | SRC_657 | Cam_Valpo_51-PTAS | 273.918 | 6.376.948 | 10 meses | 315 | 4,0519E-14 | 3,1473E-15 | 7,7379E-14 | 3,3543E-14 | 7,6387E-14 |
| AREA | SRC_658 | Cam_Valpo_52-PTAS | 273.963 | 6.376.959 | 10 meses | 182 | 6,9982E-14 | 5,436E-15 | 1,3365E-13 | 5,7935E-14 | 1,3193E-13 |
| AREA | SRC_659 | Cam_Valpo_53-PTAS | 274.013 | 6.376.981 | 10 meses | 220 | 5,7928E-14 | 4,4997E-15 | 1,1063E-13 | 4,7956E-14 | 1,0921E-13 |
| AREA | SRC_660 | Cam_Valpo_54-PTAS | 274.045 | 6.377.010 | 10 meses | 176 | 7,259E-14 | 5,6385E-15 | 1,3863E-13 | 6,0094E-14 | 1,3685E-13 |
| AREA | SRC_661 | Cam_Valpo_55-PTAS | 274.402 | 6.377.569 | 10 meses | 2.655 | 4,8049E-15 | 3,7323E-16 | 9,1761E-15 | 3,9778E-15 | 9,0584E-15 |
| AREA | SRC_662 | Cam_Valpo_56-PTAS | 274.508 | 6.377.712 | 10 meses | 712 | 1,7912E-14 | 1,3913E-15 | 3,4207E-14 | 1,4828E-14 | 3,3768E-14 |
| AREA | SRC_663 | Cam_Valpo_57-PTAS | 274.515 | 6.377.737 | 10 meses | 106 | 1,2087E-13 | 9,3887E-15 | 2,3083E-13 | 1,0006E-13 | 2,2787E-13 |
| AREA | SRC_664 | Cam_Valpo_58-PTAS | 274.530 | 6.377.783 | 10 meses | 191 | 6,6844E-14 | 5,1922E-15 | 1,2765E-13 | 5,5337E-14 | 1,2602E-13 |
| AREA | SRC_665 | Cam_Valpo_59-PTAS | 274.571 | 6.378.190 | 10 meses | 1.641 | 7,7761E-15 | 6,0402E-16 | 1,485E-14 | 6,4374E-15 | 1,466E-14 |
| AREA | SRC_666 | Cam_Valpo_60-PTAS | 274.512 | 6.378.662 | 10 meses | 1.902 | 6,7063E-15 | 5,2092E-16 | 1,2807E-14 | 5,5518E-15 | 1,2643E-14 |
| AREA | SRC_667 | Cam_Valpo_61-PTAS | 274.484 | 6.378.742 | 10 meses | 339 | 3,7591E-14 | 2,92E-15 | 7,1789E-14 | 3,112E-14 | 7,0869E-14 |

**Tabla 25.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 18**

| Tipo<br>AREA | ID<br>SRC_668 | Descripción<br>Cam_Valpo_62-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_668 | Descripción<br>Cam_Valpo_62-PTAS | [m]<br>274.397 | [m]<br>6.378.959 | [m]<br>6.378.959 | [m2]<br>935 | [g/m2s]<br>1,3646E-14 | [g/m2s]<br>1,0599E-15 | [g/m2s]<br>2,6059E-14 | [g/m2s]<br>1,1296E-14 | [g/m2s]<br>2,5725E-14 |
| AREA | SRC_669 | Cam_Valpo_63-PTAS | 274.391 | 6.379.006 | 10 meses | 190 | 6,729E-14 | 5,2269E-15 | 1,2851E-13 | 5,5707E-14 | 1,2686E-13 |
| AREA | SRC_670 | Cam_Valpo_64-PTAS | 274.392 | 6.379.034 | 10 meses | 109 | 1,1652E-13 | 9,0505E-15 | 2,2251E-13 | 9,6458E-14 | 2,1966E-13 |
| AREA | SRC_671 | Cam_Valpo_65-PTAS | 274.513 | 6.379.469 | 10 meses | 1.806 | 7,0653E-15 | 5,4881E-16 | 1,3493E-14 | 5,849E-15 | 1,332E-14 |
| AREA | SRC_672 | Cam_Valpo_66-PTAS | 274.514 | 6.379.510 | 10 meses | 163 | 7,8093E-14 | 6,066E-15 | 1,4914E-13 | 6,465E-14 | 1,4722E-13 |
| AREA | SRC_673 | Cam_Valpo_67-PTAS | 274.503 | 6.379.560 | 10 meses | 209 | 6,1117E-14 | 4,7474E-15 | 1,1672E-13 | 5,0596E-14 | 1,1522E-13 |
| AREA | SRC_674 | Cam_Valpo_68-PTAS | 274.488 | 6.379.623 | 10 meses | 255 | 4,9941E-14 | 3,8793E-15 | 9,5374E-14 | 4,1344E-14 | 9,4151E-14 |
| AREA | SRC_675 | Cam_Valpo_69-PTAS | 274.426 | 6.379.798 | 10 meses | 746 | 1,711E-14 | 1,3291E-15 | 3,2676E-14 | 1,4165E-14 | 3,2257E-14 |
| AREA | SRC_676 | Cam_Valpo_70-PTAS | 274.386 | 6.379.897 | 10 meses | 429 | 2,9769E-14 | 2,3123E-15 | 5,685E-14 | 2,4644E-14 | 5,6121E-14 |
| AREA | SRC_677 | Cam_Valpo_71-PTAS | 274.352 | 6.379.981 | 10 meses | 360 | 3,5413E-14 | 2,7508E-15 | 6,763E-14 | 2,9317E-14 | 6,6763E-14 |
| AREA | SRC_678 | Cam_Valpo_72-PTAS | 274.336 | 6.380.041 | 10 meses | 249 | 5,1133E-14 | 3,9718E-15 | 9,765E-14 | 4,233E-14 | 9,6397E-14 |
| AREA | SRC_679 | Cam_Valpo_73-PTAS | 274.333 | 6.380.099 | 10 meses | 228 | 5,6001E-14 | 4,35E-15 | 1,0695E-13 | 4,6361E-14 | 1,0558E-13 |
| AREA | SRC_680 | Cam_Valpo_74-PTAS | 274.332 | 6.380.163 | 10 meses | 257 | 4,9586E-14 | 3,8516E-15 | 9,4695E-14 | 4,1049E-14 | 9,348E-14 |
| AREA | SRC_681 | Cam_Valpo_75-PTAS | 274.329 | 6.380.546 | 10 meses | 1.530 | 8,3355E-15 | 6,4747E-16 | 1,5919E-14 | 6,9005E-15 | 1,5714E-14 |
| AREA | SRC_682 | Cam_Valpo_76-PTAS | 274.323 | 6.380.578 | 10 meses | 131 | 9,7721E-14 | 7,5906E-15 | 1,8662E-13 | 8,0898E-14 | 1,8423E-13 |
| AREA | SRC_683 | Cam_Valpo_77-PTAS | 274.308 | 6.380.608 | 10 meses | 138 | 9,2326E-14 | 7,1716E-15 | 1,7632E-13 | 7,6432E-14 | 1,7406E-13 |
| AREA | SRC_684 | Cam_Valpo_78-PTAS | 274.078 | 6.381.086 | 10 meses | 2.121 | 6,016E-15 | 4,673E-16 | 1,1489E-14 | 4,9804E-15 | 1,1342E-14 |
| AREA | SRC_685 | Cam_Valpo_79-PTAS | 274.036 | 6.381.146 | 10 meses | 293 | 4,3546E-14 | 3,3825E-15 | 8,316E-14 | 3,6049E-14 | 8,2094E-14 |
| AREA | SRC_686 | Cam_Valpo_80-PTAS | 273.997 | 6.381.192 | 10 meses | 243 | 5,2561E-14 | 4,0828E-15 | 1,0038E-13 | 4,3513E-14 | 9,9091E-14 |
| AREA | SRC_687 | Cam_Valpo_81-PTAS | 273.945 | 6.381.212 | 10 meses | 225 | 5,6636E-14 | 4,3993E-15 | 1,0816E-13 | 4,6886E-14 | 1,0677E-13 |
| AREA | SRC_688 | Cam_Valpo_82-PTAS | 273.863 | 6.381.235 | 10 meses | 341 | 3,7455E-14 | 2,9094E-15 | 7,1529E-14 | 3,1007E-14 | 7,0612E-14 |
| AREA | SRC_689 | Cam_Valpo_83-PTAS | 273.527 | 6.381.309 | 10 meses | 1.377 | 9,2665E-15 | 7,1979E-16 | 1,7697E-14 | 7,6713E-15 | 1,747E-14 |
| AREA | SRC_690 | Cam_Valpo_84-PTAS | 273.488 | 6.381.317 | 10 meses | 159 | 8,0319E-14 | 6,2389E-15 | 1,5339E-13 | 6,6492E-14 | 1,5142E-13 |
| AREA | SRC_691 | Cam_Valpo_85-PTAS | 273.437 | 6.381.311 | 10 meses | 211 | 6,0572E-14 | 4,705E-15 | 1,1568E-13 | 5,0145E-14 | 1,1419E-13 |
| AREA | SRC_692 | Cam_Valpo_86-PTAS | 273.400 | 6.381.306 | 10 meses | 149 | 8,5761E-14 | 6,6616E-15 | 1,6378E-13 | 7,0997E-14 | 1,6168E-13 |
| AREA | SRC_693 | Cam_Valpo_87-PTAS | 273.330 | 6.381.278 | 10 meses | 302 | 4,2239E-14 | 3,281E-15 | 8,0665E-14 | 3,4968E-14 | 7,9631E-14 |
| AREA | SRC_694 | Cam_Valpo_88-PTAS | 273.269 | 6.381.275 | 10 meses | 240 | 5,3083E-14 | 4,1233E-15 | 1,0137E-13 | 4,3945E-14 | 1,0007E-13 |
| AREA | SRC_695 | Cam_Valpo_89-PTAS | 273.210 | 6.381.284 | 10 meses | 239 | 5,3446E-14 | 4,1515E-15 | 1,0207E-13 | 4,4245E-14 | 1,0076E-13 |
| AREA | SRC_696 | Cam_Valpo_90-PTAS | 273.140 | 6.381.307 | 10 meses | 292 | 4,3705E-14 | 3,3948E-15 | 8,3464E-14 | 3,6181E-14 | 8,2393E-14 |
| AREA | SRC_697 | Cam_Valpo_91-PTAS | 273.026 | 6.381.364 | 10 meses | 511 | 2,4984E-14 | 1,9406E-15 | 4,7712E-14 | 2,0683E-14 | 4,71E-14 |
| AREA | SRC_698 | Cam_Valpo_92-PTAS | 272.787 | 6.381.471 | 10 meses | 1.046 | 1,219E-14 | 9,4692E-16 | 2,3281E-14 | 1,0092E-14 | 2,2982E-14 |
| AREA | SRC_699 | Cam_Valpo_93-PTAS | 272.625 | 6.381.553 | 10 meses | 727 | 1,7552E-14 | 1,3634E-15 | 3,3519E-14 | 1,453E-14 | 3,3089E-14 |
| AREA | SRC_700 | Cam_Valpo_94-PTAS | 272.586 | 6.381.587 | 10 meses | 206 | 6,1966E-14 | 4,8133E-15 | 1,1834E-13 | 5,1298E-14 | 1,1682E-13 |
| AREA | SRC_701 | Cam_Valpo_95-PTAS | 272.567 | 6.381.621 | 10 meses | 150 | 8,4904E-14 | 6,595E-15 | 1,6214E-13 | 7,0288E-14 | 1,6006E-13 |
| AREA | SRC_702 | Cam_Valpo_96-PTAS | 272.558 | 6.381.659 | 10 meses | 155 | 8,2522E-14 | 6,41E-15 | 1,5759E-13 | 6,8316E-14 | 1,5557E-13 |

**Tabla 26.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 19**

| Tipo<br>AREA | ID<br>SRC_703 | Descripción<br>Cam_Valpo_97-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_703 | Descripción<br>Cam_Valpo_97-PTAS | [m]<br>272.513 | [m]<br>6.381.931 | [m]<br>6.381.931 | [m2]<br>1.103 | [g/m2s]<br>1,1564E-14 | [g/m2s]<br>8,9822E-16 | [g/m2s]<br>2,2083E-14 | [g/m2s]<br>9,573E-15 | [g/m2s]<br>2,18E-14 |
| AREA | SRC_704 | Cam_Valpo_98-PTAS | 272.500 | 6.382.030 | 10 meses | 398 | 3,2023E-14 | 2,4874E-15 | 6,1155E-14 | 2,651E-14 | 6,037E-14 |
| AREA | SRC_705 | Cam_Valpo_99-PTAS | 272.492 | 6.382.086 | 10 meses | 224 | 5,6983E-14 | 4,4262E-15 | 1,0882E-13 | 4,7173E-14 | 1,0743E-13 |
| AREA | SRC_706 | Cam_Valpo_100-PTAS | 272.491 | 6.382.127 | 10 meses | 164 | 7,7637E-14 | 6,0306E-15 | 1,4826E-13 | 6,4272E-14 | 1,4636E-13 |
| AREA | SRC_707 | Cam_Valpo_101-PTAS | 272.506 | 6.382.188 | 10 meses | 247 | 5,1579E-14 | 4,0065E-15 | 9,8501E-14 | 4,2699E-14 | 9,7238E-14 |
| AREA | SRC_708 | Cam_Valpo_102-PTAS | 272.660 | 6.383.439 | 10 meses | 5.043 | 2,5295E-15 | 1,9648E-16 | 4,8306E-15 | 2,094E-15 | 4,7687E-15 |
| AREA | SRC_709 | Cam_Valpo_103-PTAS | 272.630 | 6.384.559 | 10 meses | 4.479 | 2,8482E-15 | 2,2124E-16 | 5,4393E-15 | 2,3579E-15 | 5,3696E-15 |
| AREA | SRC_710 | Cam_Valpo_104-PTAS | 272.626 | 6.385.227 | 10 meses | 2.671 | 4,7759E-15 | 3,7098E-16 | 9,1207E-15 | 3,9538E-15 | 9,0038E-15 |
| AREA | SRC_711 | Cam_Valpo_105-PTAS | 272.602 | 6.386.454 | 10 meses | 4.906 | 2,6004E-15 | 2,0199E-16 | 4,966E-15 | 2,1527E-15 | 4,9023E-15 |
| AREA | SRC_712 | Cam_Valpo_106-PTAS | 272.609 | 6.386.527 | 10 meses | 293 | 4,3609E-14 | 3,3874E-15 | 8,3282E-14 | 3,6102E-14 | 8,2214E-14 |
| AREA | SRC_713 | Cam_Valpo_107-PTAS | 272.650 | 6.386.615 | 10 meses | 385 | 3,3161E-14 | 2,5759E-15 | 6,3329E-14 | 2,7453E-14 | 6,2517E-14 |
| AREA | SRC_714 | Cam_Valpo_108-PTAS | 272.755 | 6.386.705 | 10 meses | 550 | 2,3194E-14 | 1,8017E-15 | 4,4295E-14 | 1,9202E-14 | 4,3727E-14 |
| AREA | SRC_715 | Cam_Valpo_109-PTAS | 272.846 | 6.386.776 | 10 meses | 461 | 2,7681E-14 | 2,1502E-15 | 5,2864E-14 | 2,2916E-14 | 5,2186E-14 |
| AREA | SRC_716 | Cam_Valpo_110-PTAS | 272.918 | 6.386.821 | 10 meses | 339 | 3,7654E-14 | 2,9248E-15 | 7,1909E-14 | 3,1172E-14 | 7,0987E-14 |
| AREA | SRC_717 | Cam_Valpo_111-PTAS | 272.959 | 6.386.856 | 10 meses | 216 | 5,9141E-14 | 4,5938E-15 | 1,1294E-13 | 4,896E-14 | 1,1149E-13 |
| AREA | SRC_718 | Cam_Valpo_112-PTAS | 272.979 | 6.386.909 | 10 meses | 229 | 5,5629E-14 | 4,321E-15 | 1,0624E-13 | 4,6052E-14 | 1,0487E-13 |
| AREA | SRC_719 | Cam_Valpo_113-PTAS | 272.982 | 6.386.950 | 10 meses | 168 | 7,5846E-14 | 5,8915E-15 | 1,4485E-13 | 6,2789E-14 | 1,4299E-13 |
| AREA | SRC_720 | Cam_Valpo_114-PTAS | 272.974 | 6.387.033 | 10 meses | 335 | 3,813E-14 | 2,9618E-15 | 7,2818E-14 | 3,1566E-14 | 7,1884E-14 |
| AREA | SRC_721 | Cam_Valpo_115-PTAS | 272.969 | 6.387.289 | 10 meses | 1.021 | 1,2491E-14 | 9,7029E-16 | 2,3855E-14 | 1,0341E-14 | 2,3549E-14 |
| AREA | SRC_722 | Cam_Valpo_116-PTAS | 272.950 | 6.387.316 | 10 meses | 136 | 9,3898E-14 | 7,2937E-15 | 1,7932E-13 | 7,7734E-14 | 1,7702E-13 |
| AREA | SRC_723 | Cam_Valpo_117-PTAS | 272.918 | 6.387.332 | 10 meses | 151 | 8,4697E-14 | 6,579E-15 | 1,6175E-13 | 7,0116E-14 | 1,5967E-13 |
| AREA | SRC_724 | Cam_Valpo_118-PTAS | 272.871 | 6.387.328 | 10 meses | 193 | 6,606E-14 | 5,1313E-15 | 1,2616E-13 | 5,4688E-14 | 1,2454E-13 |
| AREA | SRC_725 | Cam_Valpo_119-PTAS | 272.818 | 6.387.319 | 10 meses | 215 | 5,9384E-14 | 4,6128E-15 | 1,1341E-13 | 4,9161E-14 | 1,1195E-13 |
| AREA | SRC_726 | Cam_Valpo_120-PTAS | 272.669 | 6.387.324 | 10 meses | 594 | 2,1494E-14 | 1,6696E-15 | 4,1048E-14 | 1,7794E-14 | 4,0521E-14 |
| AREA | SRC_727 | Cam_Valpo_121-PTAS | 272.536 | 6.387.380 | 10 meses | 574 | 2,222E-14 | 1,726E-15 | 4,2435E-14 | 1,8395E-14 | 4,1891E-14 |
| AREA | SRC_728 | Cam_Valpo_122-PTAS | 272.406 | 6.387.475 | 10 meses | 643 | 1,9844E-14 | 1,5414E-15 | 3,7897E-14 | 1,6428E-14 | 3,7411E-14 |
| AREA | SRC_729 | Cam_Valpo_123-PTAS | 272.321 | 6.387.544 | 10 meses | 439 | 2,9068E-14 | 2,2579E-15 | 5,5513E-14 | 2,4064E-14 | 5,4801E-14 |
| AREA | SRC_730 | Cam_Valpo_124-PTAS | 272.252 | 6.387.605 | 10 meses | 366 | 3,4854E-14 | 2,7073E-15 | 6,6561E-14 | 2,8854E-14 | 6,5707E-14 |
| AREA | SRC_731 | Cam_Valpo_125-PTAS | 272.138 | 6.387.749 | 10 meses | 734 | 1,7381E-14 | 1,3501E-15 | 3,3192E-14 | 1,4389E-14 | 3,2767E-14 |
| AREA | SRC_732 | Cam_Valpo_126-PTAS | 272.059 | 6.387.890 | 10 meses | 646 | 1,9757E-14 | 1,5346E-15 | 3,773E-14 | 1,6356E-14 | 3,7246E-14 |
| AREA | SRC_733 | Cam_Valpo_127-PTAS | 272.019 | 6.388.008 | 10 meses | 494 | 2,5809E-14 | 2,0047E-15 | 4,9288E-14 | 2,1366E-14 | 4,8655E-14 |
| AREA | SRC_734 | Cam_Valpo_128-PTAS | 272.005 | 6.388.086 | 10 meses | 318 | 4,0095E-14 | 3,1145E-15 | 7,6571E-14 | 3,3193E-14 | 7,5589E-14 |
| AREA | SRC_735 | Cam_Valpo_129-PTAS | 272.005 | 6.388.171 | 10 meses | 338 | 3,7698E-14 | 2,9283E-15 | 7,1994E-14 | 3,1209E-14 | 7,107E-14 |
| AREA | SRC_736 | Cam_Valpo_130-PTAS | 272.018 | 6.388.207 | 10 meses | 149 | 8,5388E-14 | 6,6326E-15 | 1,6307E-13 | 7,0688E-14 | 1,6098E-13 |
| AREA | SRC_737 | Cam_Valpo_131-PTAS | 272.053 | 6.388.222 | 10 meses | 145 | 8,8241E-14 | 6,8543E-15 | 1,6852E-13 | 7,3051E-14 | 1,6636E-13 |

**Tabla 27.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 20**

| Tipo<br>AREA | ID<br>SRC_738 | Descripción<br>Cam_Valpo_132-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_738 | Descripción<br>Cam_Valpo_132-PTAS | [m]<br>272.113 | [m]<br>6.388.260 | [m]<br>6.388.260 | [m2]<br>286 | [g/m2s]<br>4,4575E-14 | [g/m2s]<br>3,4624E-15 | [g/m2s]<br>8,5126E-14 | [g/m2s]<br>3,6901E-14 | [g/m2s]<br>8,4034E-14 |
| AREA | SRC_739 | Cam_Valpo_133-PTAS | 272.165 | 6.388.289 | 10 meses | 237 | 5,394E-14 | 4,1899E-15 | 1,0301E-13 | 4,4654E-14 | 1,0169E-13 |
| AREA | SRC_740 | Cam_Valpo_134-PTAS | 272.170 | 6.388.313 | 10 meses | 103 | 1,2381E-13 | 9,6171E-15 | 2,3644E-13 | 1,025E-13 | 2,3341E-13 |
| AREA | SRC_741 | Cam_Valpo_135-PTAS | 272.160 | 6.388.355 | 10 meses | 179 | 7,1399E-14 | 5,546E-15 | 1,3635E-13 | 5,9107E-14 | 1,346E-13 |
| AREA | SRC_742 | Cam_Valpo_136-PTAS | 272.116 | 6.388.384 | 10 meses | 213 | 5,9844E-14 | 4,6485E-15 | 1,1429E-13 | 4,9542E-14 | 1,1282E-13 |
| AREA | SRC_743 | Cam_Valpo_137-PTAS | 271.990 | 6.388.473 | 10 meses | 618 | 2,0634E-14 | 1,6028E-15 | 3,9405E-14 | 1,7082E-14 | 3,8899E-14 |
| AREA | SRC_744 | Cam_Valpo_138-PTAS | 271.909 | 6.388.570 | 10 meses | 502 | 2,54E-14 | 1,973E-15 | 4,8507E-14 | 2,1027E-14 | 4,7885E-14 |
| AREA | SRC_745 | Cam_Valpo_139-PTAS | 271.887 | 6.388.631 | 10 meses | 258 | 4,9509E-14 | 3,8457E-15 | 9,4548E-14 | 4,0986E-14 | 9,3335E-14 |
| AREA | SRC_746 | Cam_Valpo_140-PTAS | 271.869 | 6.388.710 | 10 meses | 325 | 3,9305E-14 | 3,053E-15 | 7,5061E-14 | 3,2538E-14 | 7,4098E-14 |
| AREA | SRC_747 | Cam_Valpo_141-PTAS | 271.879 | 6.388.778 | 10 meses | 271 | 4,7122E-14 | 3,6603E-15 | 8,9991E-14 | 3,901E-14 | 8,8837E-14 |
| AREA | SRC_748 | Cam_Valpo_142-PTAS | 271.889 | 6.388.831 | 10 meses | 216 | 5,9112E-14 | 4,5916E-15 | 1,1289E-13 | 4,8936E-14 | 1,1144E-13 |
| AREA | SRC_749 | Cam_Valpo_143-PTAS | 271.888 | 6.388.910 | 10 meses | 318 | 4,0174E-14 | 3,1206E-15 | 7,6721E-14 | 3,3258E-14 | 7,5737E-14 |
| AREA | SRC_750 | Cam_Valpo_144-PTAS | 271.765 | 6.389.249 | 10 meses | 1.444 | 8,8355E-15 | 6,8631E-16 | 1,6873E-14 | 7,3145E-15 | 1,6657E-14 |
| AREA | SRC_751 | Cam_Valpo_145-PTAS | 271.745 | 6.389.323 | 10 meses | 309 | 4,1328E-14 | 3,2102E-15 | 7,8925E-14 | 3,4213E-14 | 7,7913E-14 |
| AREA | SRC_752 | Cam_Valpo_146-PTAS | 271.746 | 6.389.404 | 10 meses | 321 | 3,9725E-14 | 3,0857E-15 | 7,5864E-14 | 3,2887E-14 | 7,4891E-14 |
| AREA | SRC_753 | Cam_Valpo_147-PTAS | 271.745 | 6.389.713 | 10 meses | 1.235 | 1,0327E-14 | 8,0215E-16 | 1,9721E-14 | 8,549E-15 | 1,9468E-14 |
| AREA | SRC_754 | Cam_Valpo_148-PTAS | 271.729 | 6.389.779 | 10 meses | 275 | 4,6433E-14 | 3,6068E-15 | 8,8674E-14 | 3,844E-14 | 8,7537E-14 |
| AREA | SRC_755 | Cam_Valpo_149-PTAS | 271.405 | 6.390.771 | 10 meses | 4.170 | 3,0594E-15 | 2,3765E-16 | 5,8427E-15 | 2,5328E-15 | 5,7678E-15 |
| AREA | SRC_756 | Cam_Valpo_150-PTAS | 271.408 | 6.390.852 | 10 meses | 324 | 3,9365E-14 | 3,0577E-15 | 7,5176E-14 | 3,2588E-14 | 7,4212E-14 |
| AREA | SRC_757 | Cam_Valpo_151-PTAS | 271.425 | 6.390.918 | 10 meses | 270 | 4,7291E-14 | 3,6734E-15 | 9,0313E-14 | 3,915E-14 | 8,9154E-14 |
| AREA | SRC_758 | Cam_Valpo_152-PTAS | 271.595 | 6.391.444 | 10 meses | 2.210 | 5,7719E-15 | 4,4834E-16 | 1,1023E-14 | 4,7782E-15 | 1,0881E-14 |
| AREA | SRC_759 | Cam_Valpo_153-PTAS | 271.601 | 6.391.518 | 10 meses | 297 | 4,2943E-14 | 3,3357E-15 | 8,201E-14 | 3,5551E-14 | 8,0958E-14 |
| AREA | SRC_760 | Cam_Valpo_154-PTAS | 271.583 | 6.391.599 | 10 meses | 335 | 3,8131E-14 | 2,9619E-15 | 7,282E-14 | 3,1567E-14 | 7,1886E-14 |
| AREA | SRC_761 | Cam_Valpo_155-PTAS | 271.490 | 6.391.665 | 10 meses | 462 | 2,7595E-14 | 2,1435E-15 | 5,27E-14 | 2,2845E-14 | 5,2024E-14 |
| AREA | SRC_762 | Cam_Valpo_156-PTAS | 271.388 | 6.391.779 | 10 meses | 610 | 2,0896E-14 | 1,6232E-15 | 3,9906E-14 | 1,7299E-14 | 3,9395E-14 |
| AREA | SRC_763 | Cam_Valpo_157-PTAS | 271.303 | 6.391.969 | 10 meses | 830 | 1,5371E-14 | 1,1939E-15 | 2,9354E-14 | 1,2725E-14 | 2,8977E-14 |
| AREA | SRC_764 | Cam_Valpo_158-PTAS | 271.249 | 6.392.048 | 10 meses | 385 | 3,3094E-14 | 2,5706E-15 | 6,3201E-14 | 2,7397E-14 | 6,239E-14 |
| AREA | SRC_765 | Cam_Valpo_159-PTAS | 271.095 | 6.392.199 | 10 meses | 863 | 1,478E-14 | 1,1481E-15 | 2,8226E-14 | 1,2236E-14 | 2,7864E-14 |
| AREA | SRC_766 | Cam_Valpo_160-PTAS | 271.003 | 6.392.357 | 10 meses | 727 | 1,7537E-14 | 1,3622E-15 | 3,3492E-14 | 1,4518E-14 | 3,3062E-14 |
| AREA | SRC_767 | Cam_Valpo_161-PTAS | 270.864 | 6.392.618 | 10 meses | 1.182 | 1,0796E-14 | 8,3857E-16 | 2,0617E-14 | 8,9372E-15 | 2,0352E-14 |
| AREA | SRC_768 | Cam_Valpo_162-PTAS | 270.665 | 6.392.901 | 10 meses | 1.387 | 9,1997E-15 | 7,146E-16 | 1,7569E-14 | 7,616E-15 | 1,7344E-14 |
| AREA | SRC_769 | Cam_Valpo_163-PTAS | 270.570 | 6.393.060 | 10 meses | 740 | 1,7244E-14 | 1,3394E-15 | 3,2931E-14 | 1,4275E-14 | 3,2508E-14 |
| AREA | SRC_770 | Cam_Valpo_164-PTAS | 270.535 | 6.393.162 | 10 meses | 428 | 2,981E-14 | 2,3156E-15 | 5,6929E-14 | 2,4678E-14 | 5,6199E-14 |
| AREA | SRC_771 | Cam_Valpo_165-PTAS | 270.408 | 6.393.157 | 10 meses | 516 | 2,4715E-14 | 1,9198E-15 | 4,7199E-14 | 2,046E-14 | 4,6594E-14 |
| AREA | SRC_772 | Cam_Valpo_166-PTAS | 270.322 | 6.393.156 | 10 meses | 344 | 3,7072E-14 | 2,8796E-15 | 7,0797E-14 | 3,069E-14 | 6,9889E-14 |

**Tabla 28.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 21**

| Tipo<br>AREA | ID<br>SRC_773 | Descripción<br>Cam_Valpo_167-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_773 | Descripción<br>Cam_Valpo_167-PTAS | [m]<br>270.198 | [m]<br>6.393.225 | [m]<br>6.393.225 | [m2]<br>562 | [g/m2s]<br>2,2698E-14 | [g/m2s]<br>1,7631E-15 | [g/m2s]<br>4,3347E-14 | [g/m2s]<br>1,8791E-14 | [g/m2s]<br>4,2791E-14 |
| AREA | SRC_774 | Cam_Valpo_168-PTAS | 270.084 | 6.393.222 | 10 meses | 462 | 2,7638E-14 | 2,1468E-15 | 5,2781E-14 | 2,288E-14 | 5,2104E-14 |
| AREA | SRC_775 | Cam_Valpo_169-PTAS | 270.014 | 6.393.114 | 10 meses | 520 | 2,453E-14 | 1,9054E-15 | 4,6846E-14 | 2,0307E-14 | 4,6245E-14 |
| AREA | SRC_776 | Cam_Valpo_170-PTAS | 269.944 | 6.393.026 | 10 meses | 448 | 2,8463E-14 | 2,2109E-15 | 5,4357E-14 | 2,3563E-14 | 5,366E-14 |
| AREA | SRC_777 | Cam_Valpo_171-PTAS | 269.831 | 6.392.981 | 10 meses | 484 | 2,6338E-14 | 2,0459E-15 | 5,0299E-14 | 2,1804E-14 | 4,9654E-14 |
| AREA | SRC_778 | Cam_Valpo_172-PTAS | 269.702 | 6.392.966 | 10 meses | 517 | 2,4675E-14 | 1,9167E-15 | 4,7123E-14 | 2,0428E-14 | 4,6519E-14 |
| AREA | SRC_779 | Cam_Valpo_173-PTAS | 269.506 | 6.393.084 | 10 meses | 907 | 1,4069E-14 | 1,0928E-15 | 2,6868E-14 | 1,1647E-14 | 2,6524E-14 |
| AREA | SRC_780 | Cam_Valpo_174-PTAS | 269.407 | 6.393.106 | 10 meses | 411 | 3,1068E-14 | 2,4132E-15 | 5,9331E-14 | 2,572E-14 | 5,857E-14 |
| AREA | SRC_781 | Cam_Valpo_175-PTAS | 269.355 | 6.393.219 | 10 meses | 493 | 2,587E-14 | 2,0095E-15 | 4,9404E-14 | 2,1416E-14 | 4,877E-14 |
| AREA | SRC_782 | Cam_Valpo_176-PTAS | 269.450 | 6.393.436 | 10 meses | 940 | 1,3577E-14 | 1,0546E-15 | 2,5929E-14 | 1,124E-14 | 2,5597E-14 |
| AREA | SRC_783 | Cam_Valpo_177-PTAS | 269.537 | 6.393.768 | 10 meses | 1.375 | 9,2744E-15 | 7,2041E-16 | 1,7712E-14 | 7,6779E-15 | 1,7484E-14 |
| AREA | SRC_784 | Cam_Valpo_178-PTAS | 269.541 | 6.393.876 | 10 meses | 433 | 2,9451E-14 | 2,2876E-15 | 5,6243E-14 | 2,4381E-14 | 5,5522E-14 |
| AREA | SRC_785 | Cam_Valpo_179-PTAS | 269.514 | 6.393.952 | 10 meses | 327 | 3,8953E-14 | 3,0258E-15 | 7,439E-14 | 3,2248E-14 | 7,3436E-14 |
| AREA | SRC_786 | Cam_Valpo_180-PTAS | 269.461 | 6.394.006 | 10 meses | 302 | 4,2238E-14 | 3,2809E-15 | 8,0663E-14 | 3,4967E-14 | 7,9628E-14 |
| AREA | SRC_787 | Cam_Valpo_181-PTAS | 269.456 | 6.394.087 | 10 meses | 318 | 4,0175E-14 | 3,1206E-15 | 7,6723E-14 | 3,3259E-14 | 7,5739E-14 |
| AREA | SRC_788 | Cam_Valpo_182-PTAS | 269.494 | 6.394.169 | 10 meses | 359 | 3,5541E-14 | 2,7607E-15 | 6,7873E-14 | 2,9422E-14 | 6,7002E-14 |
| AREA | SRC_789 | Cam_Valpo_183-PTAS | 269.580 | 6.394.296 | 10 meses | 612 | 2,0845E-14 | 1,6192E-15 | 3,9808E-14 | 1,7257E-14 | 3,9298E-14 |
| AREA | SRC_790 | Cam_Valpo_184-PTAS | 269.614 | 6.394.394 | 10 meses | 417 | 3,0621E-14 | 2,3786E-15 | 5,8478E-14 | 2,535E-14 | 5,7728E-14 |
| AREA | SRC_791 | Cam_Valpo_185-PTAS | 269.617 | 6.394.492 | 10 meses | 397 | 3,2169E-14 | 2,4987E-15 | 6,1433E-14 | 2,6631E-14 | 6,0645E-14 |
| AREA | SRC_792 | Cam_Valpo_186-PTAS | 269.532 | 6.394.634 | 10 meses | 664 | 1,9207E-14 | 1,4919E-15 | 3,668E-14 | 1,5901E-14 | 3,621E-14 |
| AREA | SRC_793 | Cam_Valpo_187-PTAS | 269.478 | 6.394.752 | 10 meses | 518 | 2,4618E-14 | 1,9122E-15 | 4,7013E-14 | 2,038E-14 | 4,6411E-14 |
| AREA | SRC_794 | Cam_Valpo_188-PTAS | 269.437 | 6.394.881 | 10 meses | 541 | 2,3583E-14 | 1,8319E-15 | 4,5038E-14 | 1,9523E-14 | 4,446E-14 |
| AREA | SRC_795 | Cam_Valpo_189-PTAS | 269.448 | 6.395.002 | 10 meses | 483 | 2,6387E-14 | 2,0496E-15 | 5,0392E-14 | 2,1844E-14 | 4,9745E-14 |
| AREA | SRC_796 | Cam_Valpo_190-PTAS | 269.465 | 6.395.049 | 10 meses | 198 | 6,4487E-14 | 5,0092E-15 | 1,2315E-13 | 5,3386E-14 | 1,2157E-13 |
| AREA | SRC_797 | Cam_Valpo_191-PTAS | 269.701 | 6.395.188 | 10 meses | 1.089 | 1,1718E-14 | 9,1022E-16 | 2,2378E-14 | 9,7008E-15 | 2,2091E-14 |
| AREA | SRC_798 | Cam_Valpo_192-PTAS | 269.737 | 6.395.244 | 10 meses | 269 | 4,7357E-14 | 3,6785E-15 | 9,0439E-14 | 3,9205E-14 | 8,9279E-14 |
| AREA | SRC_799 | Cam_Valpo_193-PTAS | 269.748 | 6.395.318 | 10 meses | 302 | 4,2258E-14 | 3,2824E-15 | 8,0701E-14 | 3,4983E-14 | 7,9666E-14 |
| AREA | SRC_800 | Cam_Valpo_194-PTAS | 269.734 | 6.395.473 | 10 meses | 624 | 2,0443E-14 | 1,588E-15 | 3,9041E-14 | 1,6924E-14 | 3,854E-14 |
| AREA | SRC_801 | Cam_Valpo_195-PTAS | 269.791 | 6.395.575 | 10 meses | 463 | 2,7558E-14 | 2,1406E-15 | 5,2629E-14 | 2,2814E-14 | 5,1954E-14 |
| AREA | SRC_802 | Cam_Valpo_196-PTAS | 269.918 | 6.395.634 | 10 meses | 558 | 2,288E-14 | 1,7772E-15 | 4,3694E-14 | 1,8941E-14 | 4,3133E-14 |
| AREA | SRC_803 | Cam_Valpo_197-PTAS | 269.951 | 6.395.703 | 10 meses | 312 | 4,0932E-14 | 3,1795E-15 | 7,817E-14 | 3,3886E-14 | 7,7167E-14 |
| AREA | SRC_804 | Cam_Valpo_198-PTAS | 269.926 | 6.395.767 | 10 meses | 278 | 4,5909E-14 | 3,5661E-15 | 8,7674E-14 | 3,8006E-14 | 8,655E-14 |
| AREA | SRC_805 | Cam_Valpo_199-PTAS | 269.853 | 6.395.812 | 10 meses | 348 | 3,6628E-14 | 2,8451E-15 | 6,995E-14 | 3,0323E-14 | 6,9052E-14 |
| AREA | SRC_806 | Cam_Valpo_200-PTAS | 269.732 | 6.395.847 | 10 meses | 505 | 2,5278E-14 | 1,9635E-15 | 4,8274E-14 | 2,0926E-14 | 4,7654E-14 |
| AREA | SRC_807 | Cam_Valpo_201-PTAS | 269.688 | 6.395.928 | 10 meses | 365 | 3,4907E-14 | 2,7114E-15 | 6,6662E-14 | 2,8898E-14 | 6,5807E-14 |

**Tabla 29.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 22**

| Tipo<br>AREA | ID<br>SRC_808 | Descripción<br>Cam_Valpo_202-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_808 | Descripción<br>Cam_Valpo_202-PTAS | [m]<br>269.717 | [m]<br>6.396.047 | [m]<br>6.396.047 | [m2]<br>485 | [g/m2s]<br>2,632E-14 | [g/m2s]<br>2,0445E-15 | [g/m2s]<br>5,0265E-14 | [g/m2s]<br>2,1789E-14 | [g/m2s]<br>4,962E-14 |
| AREA | SRC_809 | Cam_Valpo_203-PTAS | 269.712 | 6.396.106 | 10 meses | 237 | 5,3716E-14 | 4,1725E-15 | 1,0258E-13 | 4,4469E-14 | 1,0127E-13 |
| AREA | SRC_810 | Cam_Valpo_204-PTAS | 269.657 | 6.396.143 | 10 meses | 271 | 4,699E-14 | 3,6501E-15 | 8,9739E-14 | 3,8901E-14 | 8,8588E-14 |
| AREA | SRC_811 | Cam_Valpo_205-PTAS | 269.580 | 6.396.120 | 10 meses | 326 | 3,9076E-14 | 3,0353E-15 | 7,4625E-14 | 3,2349E-14 | 7,3668E-14 |
| AREA | SRC_812 | Cam_Valpo_206-PTAS | 269.501 | 6.396.070 | 10 meses | 376 | 3,391E-14 | 2,634E-15 | 6,4759E-14 | 2,8073E-14 | 6,3929E-14 |
| AREA | SRC_813 | Cam_Valpo_207-PTAS | 269.359 | 6.396.026 | 10 meses | 594 | 2,1493E-14 | 1,6695E-15 | 4,1046E-14 | 1,7793E-14 | 4,0519E-14 |
| AREA | SRC_814 | Cam_Valpo_208-PTAS | 269.272 | 6.396.023 | 10 meses | 343 | 3,714E-14 | 2,8849E-15 | 7,0928E-14 | 3,0747E-14 | 7,0018E-14 |
| AREA | SRC_815 | Cam_Valpo_209-PTAS | 269.222 | 6.396.073 | 10 meses | 276 | 4,6253E-14 | 3,5928E-15 | 8,8331E-14 | 3,8291E-14 | 8,7199E-14 |
| AREA | SRC_816 | Cam_Valpo_210-PTAS | 269.210 | 6.396.185 | 10 meses | 446 | 2,8587E-14 | 2,2205E-15 | 5,4593E-14 | 2,3666E-14 | 5,3893E-14 |
| AREA | SRC_817 | Cam_Valpo_211-PTAS | 269.167 | 6.396.232 | 10 meses | 255 | 4,9937E-14 | 3,879E-15 | 9,5367E-14 | 4,1341E-14 | 9,4143E-14 |
| AREA | SRC_818 | Cam_Valpo_212-PTAS | 269.082 | 6.396.226 | 10 meses | 350 | 3,6492E-14 | 2,8346E-15 | 6,969E-14 | 3,021E-14 | 6,8796E-14 |
| AREA | SRC_819 | Cam_Valpo_213-PTAS | 268.998 | 6.396.240 | 10 meses | 336 | 3,8019E-14 | 2,9532E-15 | 7,2606E-14 | 3,1474E-14 | 7,1675E-14 |
| AREA | SRC_820 | Cam_Valpo_214-PTAS | 268.894 | 6.396.300 | 10 meses | 480 | 2,6572E-14 | 2,064E-15 | 5,0745E-14 | 2,1998E-14 | 5,0094E-14 |
| AREA | SRC_821 | Cam_Valpo_215-PTAS | 268.805 | 6.396.381 | 10 meses | 477 | 2,6717E-14 | 2,0753E-15 | 5,1022E-14 | 2,2118E-14 | 5,0368E-14 |
| AREA | SRC_822 | Cam_Valpo_216-PTAS | 268.734 | 6.396.481 | 10 meses | 489 | 2,607E-14 | 2,025E-15 | 4,9786E-14 | 2,1582E-14 | 4,9148E-14 |
| AREA | SRC_823 | Cam_Valpo_217-PTAS | 268.692 | 6.396.569 | 10 meses | 388 | 3,2852E-14 | 2,5518E-15 | 6,2738E-14 | 2,7196E-14 | 6,1933E-14 |
| AREA | SRC_824 | Cam_Valpo_218-PTAS | 268.614 | 6.396.686 | 10 meses | 564 | 2,2631E-14 | 1,7579E-15 | 4,322E-14 | 1,8735E-14 | 4,2666E-14 |
| AREA | SRC_825 | Cam_Valpo_219-PTAS | 268.551 | 6.396.751 | 10 meses | 365 | 3,4938E-14 | 2,7139E-15 | 6,6723E-14 | 2,8924E-14 | 6,5867E-14 |
| AREA | SRC_826 | Cam_Valpo_220-PTAS | 268.525 | 6.396.834 | 10 meses | 343 | 3,7219E-14 | 2,8911E-15 | 7,1079E-14 | 3,0812E-14 | 7,0167E-14 |
| AREA | SRC_827 | Cam_Valpo_221-PTAS | 268.521 | 6.396.918 | 10 meses | 335 | 3,8058E-14 | 2,9562E-15 | 7,2681E-14 | 3,1507E-14 | 7,1749E-14 |
| AREA | SRC_828 | Cam_Valpo_222-PTAS | 268.510 | 6.396.996 | 10 meses | 312 | 4,0865E-14 | 3,1743E-15 | 7,8041E-14 | 3,383E-14 | 7,704E-14 |
| AREA | SRC_829 | Cam_Valpo_223-PTAS | 268.441 | 6.397.095 | 10 meses | 487 | 2,6207E-14 | 2,0356E-15 | 5,0048E-14 | 2,1695E-14 | 4,9406E-14 |
| AREA | SRC_830 | Cam_Valpo_224-PTAS | 268.352 | 6.397.195 | 10 meses | 538 | 2,372E-14 | 1,8425E-15 | 4,5299E-14 | 1,9637E-14 | 4,4718E-14 |
| AREA | SRC_831 | Cam_Valpo_225-PTAS | 268.295 | 6.397.296 | 10 meses | 460 | 2,7708E-14 | 2,1523E-15 | 5,2915E-14 | 2,2938E-14 | 5,2236E-14 |
| AREA | SRC_832 | Cam_Valpo_226-PTAS | 268.265 | 6.397.370 | 10 meses | 319 | 3,999E-14 | 3,1063E-15 | 7,637E-14 | 3,3106E-14 | 7,539E-14 |
| AREA | SRC_833 | Cam_Valpo_227-PTAS | 268.236 | 6.397.470 | 10 meses | 415 | 3,0776E-14 | 2,3906E-15 | 5,8773E-14 | 2,5478E-14 | 5,8019E-14 |
| AREA | SRC_834 | Cam_Valpo_228-PTAS | 268.225 | 6.397.539 | 10 meses | 278 | 4,5886E-14 | 3,5642E-15 | 8,7629E-14 | 3,7986E-14 | 8,6505E-14 |
| AREA | SRC_835 | Cam_Valpo_229-PTAS | 268.212 | 6.397.650 | 10 meses | 446 | 2,8573E-14 | 2,2195E-15 | 5,4567E-14 | 2,3654E-14 | 5,3867E-14 |
| AREA | SRC_836 | Cam_Valpo_230-PTAS | 268.292 | 6.397.691 | 10 meses | 353 | 3,6149E-14 | 2,8079E-15 | 6,9034E-14 | 2,9926E-14 | 6,8149E-14 |
| AREA | SRC_837 | Cam_Valpo_231-PTAS | 268.324 | 6.397.741 | 10 meses | 244 | 5,2262E-14 | 4,0596E-15 | 9,9807E-14 | 4,3265E-14 | 9,8527E-14 |
| AREA | SRC_838 | Cam_Valpo_232-PTAS | 268.344 | 6.397.809 | 10 meses | 285 | 4,4837E-14 | 3,4828E-15 | 8,5626E-14 | 3,7118E-14 | 8,4527E-14 |
| AREA | SRC_839 | Cam_Valpo_233-PTAS | 268.317 | 6.397.871 | 10 meses | 277 | 4,5987E-14 | 3,5721E-15 | 8,7823E-14 | 3,807E-14 | 8,6696E-14 |
| AREA | SRC_840 | Cam_Valpo_234-PTAS | 268.289 | 6.397.931 | 10 meses | 263 | 4,8424E-14 | 3,7614E-15 | 9,2476E-14 | 4,0088E-14 | 9,129E-14 |
| AREA | SRC_841 | Cam_Valpo_235-PTAS | 268.281 | 6.397.993 | 10 meses | 246 | 5,1813E-14 | 4,0247E-15 | 9,8949E-14 | 4,2894E-14 | 9,768E-14 |
| AREA | SRC_842 | Cam_Valpo_236-PTAS | 268.325 | 6.398.057 | 10 meses | 307 | 4,1538E-14 | 3,2266E-15 | 7,9327E-14 | 3,4388E-14 | 7,831E-14 |

**Tabla 30.: Escenario 1 - Descripción de las fuentes de emisión de volumen parte 23**

| Tipo<br>AREA | ID<br>SRC_843 | Descripción<br>Cam_Valpo_237-PTAS | X1 | Y1 | Ciclo<br>operación<br>10 meses | Área | PM10-As | PM10-Cd | PM10-Cr | PM10-Ni | PM10-Pb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo<br>AREA | ID<br>SRC_843 | Descripción<br>Cam_Valpo_237-PTAS | [m]<br>268.339 | [m]<br>6.398.092 | [m]<br>6.398.092 | [m2]<br>154 | [g/m2s]<br>8,2775E-14 | [g/m2s]<br>6,4297E-15 | [g/m2s]<br>1,5808E-13 | [g/m2s]<br>6,8526E-14 | [g/m2s]<br>1,5605E-13 |
| AREA | SRC_844 | Cam_Valpo_238-PTAS | 268.362 | 6.398.151 | 10 meses | 252 | 5,0712E-14 | 3,9391E-15 | 9,6846E-14 | 4,1982E-14 | 9,5604E-14 |
| AREA | SRC_845 | Cam_Valpo_239-PTAS | 268.383 | 6.398.192 | 10 meses | 185 | 6,8886E-14 | 5,3509E-15 | 1,3155E-13 | 5,7028E-14 | 1,2987E-13 |
| AREA | SRC_846 | Cam_Valpo_240-PTAS | 268.355 | 6.398.247 | 10 meses | 250 | 5,0992E-14 | 3,9609E-15 | 9,7381E-14 | 4,2214E-14 | 9,6132E-14 |
| AREA | SRC_847 | Cam_Valpo_241-PTAS | 268.227 | 6.398.303 | 10 meses | 567 | 2,2505E-14 | 1,7481E-15 | 4,2979E-14 | 1,8631E-14 | 4,2428E-14 |
| AREA | SRC_848 | Cam_Valpo_242-PTAS | 268.140 | 6.398.362 | 10 meses | 419 | 3,0458E-14 | 2,3659E-15 | 5,8167E-14 | 2,5215E-14 | 5,7421E-14 |
| AREA | SRC_849 | Cam_Valpo_243-PTAS | 268.089 | 6.398.427 | 10 meses | 325 | 3,92E-14 | 3,045E-15 | 7,4862E-14 | 3,2452E-14 | 7,3902E-14 |
| AREA | SRC_850 | Cam_Valpo_244-PTAS | 268.005 | 6.398.483 | 10 meses | 406 | 3,1409E-14 | 2,4398E-15 | 5,9983E-14 | 2,6002E-14 | 5,9214E-14 |
| AREA | SRC_851 | Cam_Valpo_245-PTAS | 267.956 | 6.398.553 | 10 meses | 338 | 3,7713E-14 | 2,9295E-15 | 7,2022E-14 | 3,1221E-14 | 7,1099E-14 |
| AREA | SRC_852 | Cam_Valpo_246-PTAS | 267.920 | 6.398.673 | 10 meses | 499 | 2,5567E-14 | 1,986E-15 | 4,8826E-14 | 2,1166E-14 | 4,82E-14 |
| AREA | SRC_853 | Cam_Valpo_247-PTAS | 267.908 | 6.398.749 | 10 meses | 308 | 4,1369E-14 | 3,2134E-15 | 7,9004E-14 | 3,4248E-14 | 7,7991E-14 |
| AREA | SRC_854 | Cam_Valpo_248-PTAS | 267.894 | 6.398.771 | 10 meses | 107 | 1,1877E-13 | 9,2256E-15 | 2,2682E-13 | 9,8324E-14 | 2,2391E-13 |
| AREA | SRC_855 | Cam_Valpo_249-PTAS | 267.791 | 6.398.823 | 10 meses | 467 | 2,7343E-14 | 2,1239E-15 | 5,2217E-14 | 2,2636E-14 | 5,1548E-14 |
| AREA | SRC_856 | Cam_Valpo_250-PTAS | 267.747 | 6.398.849 | 10 meses | 204 | 6,2534E-14 | 4,8574E-15 | 1,1942E-13 | 5,1769E-14 | 1,1789E-13 |
| AREA | SRC_857 | Cam_Valpo_251-PTAS | 267.699 | 6.398.875 | 10 meses | 217 | 5,8747E-14 | 4,5633E-15 | 1,1219E-13 | 4,8634E-14 | 1,1075E-13 |
| AREA | SRC_858 | Cam_Valpo_252-PTAS | 267.673 | 6.398.943 | 10 meses | 286 | 4,4618E-14 | 3,4658E-15 | 8,5209E-14 | 3,6937E-14 | 8,4116E-14 |
| AREA | SRC_859 | Cam_Valpo_253-PTAS | 267.740 | 6.399.152 | 10 meses | 872 | 1,463E-14 | 1,1364E-15 | 2,7939E-14 | 1,2111E-14 | 2,758E-14 |
| AREA | SRC_860 | Cam_Valpo_254-PTAS | 267.754 | 6.399.259 | 10 meses | 434 | 2,9369E-14 | 2,2813E-15 | 5,6086E-14 | 2,4313E-14 | 5,5367E-14 |
| AREA | SRC_861 | Cam_Valpo_255-PTAS | 267.756 | 6.399.372 | 10 meses | 453 | 2,8165E-14 | 2,1878E-15 | 5,3788E-14 | 2,3317E-14 | 5,3098E-14 |
| AREA | SRC_862 | Cam_Valpo_256-PTAS | 267.702 | 6.399.478 | 10 meses | 480 | 2,6575E-14 | 2,0643E-15 | 5,0751E-14 | 2,2E-14 | 5,01E-14 |
| AREA | SRC_863 | Cam_Valpo_257-PTAS | 267.740 | 6.399.547 | 10 meses | 307 | 4,1525E-14 | 3,2255E-15 | 7,9301E-14 | 3,4376E-14 | 7,8284E-14 |
| AREA | SRC_864 | Cam_Valpo_258-PTAS | 267.742 | 6.399.624 | 10 meses | 312 | 4,0946E-14 | 3,1805E-15 | 7,8195E-14 | 3,3897E-14 | 7,7193E-14 |
| AREA | SRC_865 | Cam_Valpo_259-PTAS | 267.731 | 6.399.695 | 10 meses | 288 | 4,4359E-14 | 3,4457E-15 | 8,4714E-14 | 3,6723E-14 | 8,3627E-14 |
| AREA | SRC_866 | Cam_Valpo_260-PTAS | 267.682 | 6.399.788 | 10 meses | 426 | 2,9967E-14 | 2,3278E-15 | 5,7229E-14 | 2,4808E-14 | 5,6495E-14 |
| AREA | SRC_867 | Cam_Valpo_261-PTAS | 267.661 | 6.399.830 | 10 meses | 187 | 6,8206E-14 | 5,298E-15 | 1,3025E-13 | 5,6464E-14 | 1,2858E-13 |

**Tabla 31.: Análisis porcentual de vientos calmos - Estación Puchuncaví**

| Año | % de vientos<br>calmos | % datos<br>válidos |
| --- | --- | --- |
| 2021 | 21,24 | 92,71% |
| 2022 | 22,21 | 93,31% |
| 2023 | 25,37 | 92,98% |

**Tabla 32.: Parametrización grilla 1 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.495 | 6.386.450 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 33.: Parametrización grilla 2 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.306 | 6.385.136 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 34.: Parametrización grilla 3 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.956 | 6.384.019 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 35.: Parametrización grilla 4 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.714 | 6.382.885 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 36.: Parametrización grilla 5 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 20.000 | 1.000 | 272.829 | 6.385.151 | 1,5 |
