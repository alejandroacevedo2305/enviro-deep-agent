---
title: Sin título
author: Anexo 1.5 Estudio de emisiones atmosféricas, DIA “Data Center Chile 2”
date: D:20240325161100-03'00'
language: es
type: report
pages: 44
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Adenda a la DIA del proyecto “Condominios Fuentes de Porvenir”
-->

# Adenda a la DIA del proyecto “Condominios Fuentes de Porvenir”

## Informe de modelación de dispersión de contaminantes versión corregida

Elaborado por:
GIZA Ingeniería SpA
[https://gizaingenieria.com/](https://gizaingenieria.com/)

Región del Biobío, marzo de 2024

Informe de modelación de dispersión de contaminantes versión corregida,
1
Adenda “Condominios Fuentes de Porvenir”

**ÍNDICE**

**1. INTRODUCCIÓN ............................................................................................................. 3**
**2. DESCRIPCIÓN GENERAL DEL PROYECTO .................................................................... 3**

**2.1.** **D** **ESCRIPCIÓN BREVE DEL PROYECTO** **.** ................................................................................................ 3

**3. LOCALIZACIÓN .............................................................................................................. 4**
**4. EMISIONES A MODELAR ............................................................................................... 5**
**5. MODELACIÓN DE EMISIONES ATMOSFÉRICAS .......................................................... 7**

**5.1.** **M** **ARCO LEGAL** ....................................................................................................................................... 7
**5.2.** **E** **CUACIÓN GENERAL PARA EL CÁLCULO DE EMISIONES** ................................................................... 8
**5.3.** **R** **ESULTADOS Y** **A** **NÁLISIS** **L** **ÍNEA DE** **B** **ASE** ......................................................................................... 9

_5.3.1 Material Particulado (MP_ _10_ _) .......................................................................................................... 9_
_5.3.2 Material Particulado Fino (MP_ _2,5_ _) ............................................................................................... 11_
_5.3.3 Dióxido de Nitrógeno (NO_ _2_ _) ......................................................................................................... 13_
_5.3.4 Dióxido de Azufre (SO_ _2_ _) ................................................................................................................ 14_
**5.4** **D** **ESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO** ..................................................................................17
**5.5** **F** **UENTES DE EMISIÓN** ..........................................................................................................................17
**5.6** **R** **ESULTADOS DE LA MODELACIÓN** ..................................................................................................... 19

_5.6.1 Superposición de la fase de construcción y operación ............................................................... 19_

**6. ANÁLISIS IMPACTO DE EMISIONES EN ZONAS SATURADAS POR MATERIAL**
**PARTICULADO MP** **10** **Y MATERIAL PARTICULADO FINO RESPIRABLE MP** **2,5** **............... 29**
**7. CONCLUSIÓN ............................................................................................................... 30**
**8. REFERENCIAS ............................................................................................................. 31**
**APÉNDICE 1: MEMORIA DE CÁLCULO DE LA MODELACIÓN ........................................ 32**

**ÍNDICE DE TABLAS**

Tabla 1. Resumen de emisiones por actividad, Fase de Construcción - año 1 .............................................. 6
Tabla 2. Resumen de emisiones por actividad, Fase de Operación - año 1 .................................................. 6
Tabla 3. Resumen de emisiones- año 1 ........................................................................................................... 6
Tabla 4. Normas de Calidad del Aire consideradas en el estudio .................................................................. 7
Tabla 5. Contaminante que constituye la Línea de base de Calidad de aire y ubicación de la Estación de

monitoreo ................................................................................................................................................. 8
Tabla 6. Percentil 98 concentraciones de 24 horas y Promedio anual de concentración de MP 10, periodo

2020 - 2022, Estación Punteras ........................................................................................................... 10
Tabla 7. Resumen de concentraciones de MP 10 (μg/m [3] N) ............................................................................ 11
Tabla 8. Percentil 98 concentraciones de 24 horas y Promedio anual de concentración de MP 2,5, periodo

2020 - 2022, Estación Punteras ............................................................................................................ 11
Tabla 9. Resumen de concentraciones de MP 2,5 (μg/m [3] N) .......................................................................... 13

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de modelación de dispersión de contaminantes versión corregida, _12_ Adenda “Condominios Fuentes de Porvenir” -->

**Tabla 9: , se presenta el resumen estadístico de los registros de Calidad del Aire disponibles en el entorno del**

| Contaminante | Norma | Estadístico | Estación<br>Punteras | Limite según Norma | Unidad | % de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | Primaria | Promedio Anual1 | 17 | 20 | (g/m3) | 83,3 |
| MP2,5 | Primaria | Percentil 98 promedio diario - 2020 | 51 | 50 | (g/m3) | 101,6 |
| MP2,5 | Primaria | Percentil 98 promedio diario - 2021 | 57 | 50 | (g/m3) | 113,9 |
| MP2,5 | Primaria | Percentil 98 promedio diario - 2022 | <br>53 | 50 | (g/m3) | 106,4 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia, 2024 Como se observa en la tabla anterior, la concentración anual de MP2,5, alcanza el nivel de latencia para la norma anual. Mientras que la norma diaria supera los niveles de saturación para los tres años en estudio. -->
<!-- FIN TABLA 9 -->

Tabla 10. Percentil 99 concentración de 1 hora y Promedio anual de concentración de NO 2, periodo 2020

- 2022, Estación Punteras ..................................................................................................................... 13
Tabla 11. Resumen de concentraciones de NO 2 (μg/m [3] N) ........................................................................... 14
Tabla 12. Percentil 99 concentración de 1 hora, Percentil 99 concentraciones de 24 hora y Promedio

anual de concentración de SO 2, periodo 2020 - 2022, Estación Punteras ........................................ 15
Tabla 13. Resumen de concentraciones de SO 2 (μg/m [3] N) ............................................................................17
Tabla 14. Tasas de emisiones del Proyecto, Fase construcción y operación ............................................... 18
Tabla 15. Datos de entrada del modelo .......................................................................................................... 19
Tabla 16. Resultados del modelo, Fase de la superposición de la fase de construcción y operación ......... 19
Tabla 17. Máximas concentraciones horarias obtenidas del modelo ........................................................... 20

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |5000|0,544|0,008348|0,7069|9734|0,3323| Fuente: Elaboración propia, 2024 El resultado de las máximas concentraciones horarias (μg/m3) arrojadas por el modelo, se presentan en la -->

**Tabla 17: que se muestra a continuación.**

| Lugar | Distancia máx,<br>concentración<br>(m) | Concentración horaria (g/m3) | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Lugar | Distancia máx,<br>concentración<br>(m) | CO | SO2 | NO2 | MP2,5 Total | MP10 Tota |
| Proyecto | 100 | 20,75 | 0,3185 | 26,97 | 3,714 | 12,680 |

<!-- Estadísticas: 2 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia, 2024 Es necesario destacar que el modelo entrega concentraciones a nivel horario, las que son convertidas a concentraciones de 3 h, 8 h, 24 h o anuales, de acuerdo a los factores de conversión establecidos por la EPA [3] -->
<!-- FIN TABLA 17 -->

Tabla 18. Factores de conversión para promedios máximos de concentración .......................................... 20
Tabla 19. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase construcción y

operación ................................................................................................................................................ 21

Informe de modelación de dispersión de contaminantes versión corregida,
_2_
Adenda “Condominios Fuentes de Porvenir”

Tabla 20. Concentraciones por distancia de los contaminantes analizados, Fase de construcción y

operación ................................................................................................................................................ 22
Tabla 21. Evaluación de Significancia ........................................................................................................... 29

**ÍNDICE DE FIGURAS**
Figura 1. Localización del Proyecto ................................................................................................................. 5
Figura 2. Ubicación de la Estación de monitoreo de Calidad de aire ............................................................ 9
Figura 3. Percentil 98 concentraciones 24 horas de MP 10, periodo 2020 - 2022, Estación Punteras ...... 10
Figura 4. Promedio anual de MP 10, periodo 2020 - 2022, Estación Punteras ........................................... 10
Figura 5. Percentil 98 concentraciones 24 horas de MP 2,5, periodo 2020 - 2022, Estación Punteras ..... 12
Figura 6. Promedio anual de MP 2,5, periodo 2020 - 2022, Estación Punteras .......................................... 12
Figura 7. Percentil 99 de concentración de 1 hora de NO 2, periodo 2020 - 2022, Estación Punteras ..... 13
Figura 8. Promedio anual de NO 2, periodo 2020 - 2022, Estación Punteras ............................................ 14
Figura 9. Percentil 99 de concentración de 1 hora de SO 2, periodo 2020 - 2022, Estación Punteras ...... 15
Figura 10. Percentil 99 de concentración de 24 horas de SO 2, periodo 2020 - 2022, Estación Punteras 16
Figura 11. Promedio anual de SO 2, periodo 2020 - 2022, Estación Punteras ............................................ 16
Figura 12. Ubicación de los potenciales receptores ...................................................................................... 18
Figura 13. Área de influencia del Proyecto .................................................................................................... 24

**1. INTRODUCCIÓN**

E l presente informe contiene la modelación de emisiones atmosféricas de los contaminantes material
particulado respirable (MP10), Material particulado respirable fino (MP2,5) y gases (NOx, SOx y CO),
producto de la construcción y operación del proyecto “Condominio Fuentes de Porvenir” ubicado en la
comuna de Chiguayante y Región del Biobío.

**2. DESCRIPCIÓN GENERAL DEL PROYECTO**

**2.1. Descripción breve del proyecto.**

El proyecto denominado “Condominios Fuentes de Porvenir” (en adelante e indistintamente el
“Proyecto”), perteneciente a Inmobiliaria Fuentes de Porvenir S.p.A. (en adelante el “Titular”) y que estará
emplazado en la ciudad de Chiguayante ubicada en la Provincia de Concepción de la Región del Biobío.

El proyecto consiste en la construcción de un conjunto habitacional acogido a la Ley Copropiedad
Inmobiliaria. N°19.537 en 2 lotes denominaos Lote A1 y Lote A-2, dentro de una Zona Mixta ZU 5 y ZU1A, con un total de 347 viviendas (296 estacionamientos vehiculares, 165 bicicleteros, 4 salas múltiples y 2
porterías, que se desarrolla en 2 fases de desarrollo.

La primera fase corresponde a las etapas I-A del Lote A-I, la cual se encuentran ejecutada y recibida de
acuerdo a la Dirección de Obras Municipales de Chiguayante (proyecto existente).

La etapa ejecutada y recibida constan de un total de 175 viviendas, 138 estacionamientos, 114 bicicleteros,1
sala múltiple y 1 portería. Con una superficie total construida de 12.650,91 m2 sobre en una superficie
bruta total de terreno de 10.833,98 m2.

El segundo desarrollo inmobiliario corresponde a la construcción y operación de la etapa II-A en el Lote
A-2 que vienen a sumar 172 viviendas, 158 estacionamientos, 51 bicicleteros, 2 locales comerciales,3
bodegas y 1 portería. a la etapa ejecutada y recepcionada. Con una superficie total construida de 11.707,93
m2 sobre en una superficie bruta total de terreno de 8.512,11 m2.

La fase de construcción de las etapas del Lote A-2 tendrá una duración de 18 meses.

Informe de modelación de dispersión de contaminantes versión corregida,
_3_
Adenda “Condominios Fuentes de Porvenir”

A continuación, se describen las etapas del Proyecto:

Lote A-1 (Etapa A ejecutada y recibida por la DOM de Chiguayante):

Proyecto existente

Denominado “Condominios Fuentes de Porvenir Lote A-I”: (ROL SII 3109-4)

Etapa I-A: Se encuentra ejecutada de acuerdo al permiso de edificación N° 1 de fecha 23 de noviembre del
2020 y con recepción final de la Dirección de Obras Municipales de Chiguayante No02 de Fecha de enero
del 2023, adjunto en el Anexo 1.2 de la DIA. Esta etapa ejecutada consiste 10 torres de departamentos
(Torres de la A hasta la l correspondientes a 5 pisos, y Torre J de 4 pisos) (1 tipo 1, 3 tipo 2, 2 tipo 3, 2 tipo
4, 1 tipo 5 y 1 tipo 6), considera 175 departamentos, 1 sala de uso múltiple, 1 portería bodega, 138
estacionamientos vehiculares (98 unidades asignados y 40 unidades en el nivel subterráneo) y 114
estacionamientos de bicicletas, con una superficie construida de 12.650,99 m2 sobre en una superficie
bruta total de terreno de 10.833,98 m2.

Lote A-2 (Etapas por construir):
Denominado “Condominios Fuentes de Porvenir Lote A-II”: (ROL SII 3109-8)

Etapa II-A: Contempla la construcción de172 viviendas, 158 estacionamientos, 51 bicicleteros, 2 locales
comerciales, 3 bodegas y 1 portería. a la etapa ejecutada y recepcionada. Con una superficie total
construida de 11.707,93 m2 sobre en una superficie bruta total de terreno de 8.512,11 m2.

El Proyecto se encuentra ubicado en Av. Manuel Rodríguez No2725, Comuna de Chiguayante, Provincia
de Concepción, Región del Bio Bío.

La superficie de terreno bruta total del Proyecto es de 19.346,09 m2.
La superficie construida total del Proyecto es de 24.358,92 m2.

**3. LOCALIZACIÓN**

El Proyecto se encuentra ubicado en Av. Manuel Rodríguez No2725, Comuna de Chiguayante, Provincia
de Concepción, Región del Bio Bío

Informe de modelación de dispersión de contaminantes versión corregida,
_4_
Adenda “Condominios Fuentes de Porvenir”

Figura 1. Localización del Proyecto

Fuente: Elaboración propia, 2024

**4. EMISIONES A MODELAR**

La estimación de emisiones del Proyecto se realizó aplicando los factores de emisión y fórmulas
propuestas por la Agencia de Protección Ambiental de los EE.UU. en el documento “AP-42 5th Edición”,
complementando esta información con la indicada por SEREMI de Medio Ambiente Región
Metropolitana en el documento “Guía para la Estimación de Emisiones Atmosféricas en la Región
Metropolitana” (octubre 2020), el que ha sido utilizado como una referencia técnica para el cálculo de las
emisiones.

A continuación, en la Tabla 1 se muestra el resumen de las emisiones directas de material particulado
respirable (MP10), material particulado fino respirable (MP2,5), en el modelo como óxidos de nitrógeno
(NOx), monóxido de carbono (CO) y óxidos de azufre (SOx). Es importante señalar que para evaluar el
impacto de las emisiones se consideró el año con mayores emisiones correspondiente al año 1 con la
superposición de la fase de construcción y operación del Proyecto:

Informe de modelación de dispersión de contaminantes versión corregida,
_5_
Adenda “Condominios Fuentes de Porvenir”

Es importante destacar que, las emisiones que se modelaron son las emisiones directas que se generan al interior del área de Proyecto. Estas se muestran a
continuación.

Tabla 1. Resumen de emisiones por actividad, Fase de Construcción - año 1

|Actividades|CO (ton/año)|COV (ton/año)|SOX (ton/año)|NOX (ton/año)|NH3 (ton/año)|MP2,5 Comb<br>(ton/año)|MP10 Comb<br>(ton/año)|MP2,5 Resus<br>(ton/año)|MP10 Resus<br>(ton/año)|MP2,5 Total<br>(ton/año)|MP10 Total<br>(ton/año)|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Compactación|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0028|0,0054|0,0028|0,0054|
|Nivelación|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0005|0,0043|0,0005|0,0043|
|Escarpe|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0026|0,0173|0,0026|0,0173|
|Excavación|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0153|0,0298|0,0153|0,0298|
|Transferencia de material|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0011|0,0075|0,0011|0,0075|
|Erosión de material en acopio|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0001|0,0004|0,0001|0,0004|
|Circulación de vehículos en<br>caminos pavimentado<br>(interior)|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,00933|0,04161|0,00933|0,04161|
|Combustión vehículos|0,0090|0,0013|0,0019|0,1592|0,0003|0,0014|0,0014|0,0000|0,0000|0,0014|0,0014|
|Combustión maquinaria fuera<br>de ruta|0,2740|0,0256|0,0012|0,1918|0,0000|0,0027|0,0027|0,0000|0,0000|0,0027|0,0027|
|Grupos electrógenos|0,0045|0,0000|0,0014|0,0208|0,0000|0,0015|0,0015|0,0000|0,0000|0,0015|0,0015|
|**Emisión total (ton/año)**|**0,2875**|**0,0269**|**0,0045**|**0,3718**|**0,0003**|**0,0056**|**0,0056**|**0,03173**|**0,10631**|**0,03733**|**0,11191**|

Tabla 2. Resumen de emisiones por actividad, Fase de Operación - año 1

|Actividades|CO (ton/año)|COV (ton/año)|SOX (ton/año)|NOX (ton/año)|NH3 (ton/año)|MP2,5 Comb<br>(ton/año)|MP10 Comb<br>(ton/año)|MP2,5 Resus<br>(ton/año)|MP10 Resus<br>(ton/año)|MP2,5 Total<br>(ton/año)|MP10 Total<br>(ton/año)|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Circulación de vehículos en<br>caminos pavimentado|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,0000|0,01867|0,08327|0,01867|0,08327|
|Combustión vehículos|0,00081|0,00020|0,00002|0,00343|0,00004|0,00003|0,00003|0,0000|0,0000|0,00003|0,00003|
|**Emisión total (ton/año)**|**0,00081**|**0,00020**|**0,00002**|**0,00343**|**0,00004**|**0,00003**|**0,00003**|**0,01867**|**0,08327**|**0,01870**|**0,08330**|

Fuente: Elaboración propia, 2024

Tabla 3. Resumen de emisiones- año 1

|Año|Fase|CO<br>(ton/año)|COV<br>(ton/año)|SOX<br>(ton/año)|NOX<br>(ton/año)|NH3<br>(ton/año)|MP2,5 Comb<br>(ton/año)|MP10 Comb<br>(ton/año)|MP2,5 Resus<br>(ton/año)|MP10 Resus<br>(ton/año)|MP2,5 Total<br>(ton/año)|MP10 Total<br>(ton/año)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|Construcción|0,2875|0,0269|0,0045|0,3718|0,0003|0,0056|0,0056|0,03173|0,10631|0,03733|0,11191|
|1|Operación Etapa A-I|0,00081|0,00020|0,00002|0,00343|0,00004|0,00003|0,00003|0,01867|0,08327|0,01870|0,08330|
|1|**Total**|**0,28831**|**0,0271**|**0,00452**|**0,37523**|**0,00034**|**0,00563**|**0,00563**|**0,0504**|**0,18958**|**0,05603**|**0,19521**|

Fuente: Elaboración propia, 2024

Informe de modelación de dispersión de contaminantes versión corregida,
6
Adenda “Condominios Fuentes de Porvenir”

**5. MODELACIÓN DE EMISIONES ATMOSFÉRICAS**

**5.1. Marco legal**

La siguiente modelación determinará el efecto en las cercanías del Proyecto, producto de las emisiones de Material
Particulado Respirable (MP10), Fino (MP2,5) y los gases generados por las actividades asociadas a la superposición
de las fases de construcción y operación del Proyecto.

En el contexto legal, existen normas primarias y secundarias asociadas a la concentración de los contaminantes de
los contaminantes generados en el Proyecto. Los estadísticos a evaluar se presentan en la Tabla 4:

Tabla 4. Normas de Calidad del Aire consideradas en el estudio

|Parámetro|Norma|Estadístico|Limite<br>según<br>Norma|Unidad|Referencia|
|---|---|---|---|---|---|
|MP10|Primaria|Promedio Anual1|50|(g/m3)|D.S. N°12/2022 del MMA<br>|
|MP10|Primaria|Percentil 98 promedio diario|130|(g/m3)|(g/m3)|
|MP2,5|Primaria|Promedio Anual|20|(g/m3)|D.S. N°12/2011 del MMA<br>|
|MP2,5|Primaria|Percentil 98 promedio diario|50|(g/m3)|(g/m3)|
|NO2|Primaria|Promedio Anual|100|(g/m3)|D.S. N°114/ 2002 MINSEGPRES<br>|
|NO2|Primaria|Percentil 99 máx. 1 hora|400|(g/m3)|(g/m3)|
|CO|Primaria|Percentil 99 1 hora|30|(mg/m3)|D.S. N°115/2002 del MINSEGPRES<br>|
|CO|Primaria|Percentil 99 8 hora|10|(mg/m3)|(mg/m3)|
|SO2|Primaria|Promedio Anual|60|(g/m3)|D.S. N°104/ 2018 MMA<br><br>|
|SO2|Primaria|Percentil 99 24 horas|150|(g/m3)|(g/m3)|
|SO2|Primaria|Percentil 99 1 hora|350|(g/m3)|(g/m3)|
|SO2 (*)|Secundaria|Promedio Anual2|260|(g/m3)|D.S. N°22/2010 MINSEGPRES<br>|
|SO2 (*)|Secundaria|Percentil 98 promedio diario|60|(g/m3)|(g/m3)|

(*) Norma Secundario de Calidad del Aire para Anhídrido Sulfuroso. Valores de la zona sur del país

Fuente: Elaboración propia, 2024

1 Aplicable al promedio anual de tres años consecutivos.
2 Aplicable al promedio anual de tres años consecutivos.

Informe de modelación de dispersión de contaminantes versión corregida,
7
Adenda “Condominios Fuentes de Porvenir”

**5.2. Ecuación general para el cálculo de emisiones**

Para establecer la línea de base de calidad del aire del Proyecto, se realizó una recopilación de la información
pública para lo cual y de acuerdo a la ubicación del Proyecto y lo disponible en el Sistema de Información
Nacional de Calidad del Aire (SINCA), se considerará lo presentado en la Estación Punteras (Ministerio de
Medio Ambiente), siendo la estación más cercana al Proyecto.

La caracterización de la calidad del aire se realizó sobre los contaminantes MP 10, MP 2,5, NO 2 y SO 2 y su
análisis se llevó a cabo, mediante la comparación de los registros recopilados con las normas de calidad del
aire establecidas por la legislación vigente y normas de referencia cuando corresponde. No se realizó este
análisis para CO por no contar con información disponible.

En la Tabla 5 se presentan las coordenadas de ubicación de la estación y los parámetros que se miden en
ella.

Tabla 5. Contaminante que constituye la Línea de base de Calidad de aire y ubicación de la Estación de

monitoreo

|Estación|Coordenadas UTM WGS84 (Huso 19)|Col3|Contaminante|Periodo|Administrada por|
|---|---|---|---|---|---|
|Estación|Este (m)|Norte (m)|Norte (m)|Norte (m)|Norte (m)|
|Punteras|674.923|5.911.833<br>|MP10 - MP2,5- NO2 - SO2|2020-2022|MMA|

Fuente: Elaboración propia, 2024

La Figura 2 presenta la ubicación de la estación de monitoreo de calidad del aire considerada en la presente
línea de base.

Informe de modelación de dispersión de contaminantes versión corregida,
_8_
Adenda “Condominios Fuentes de Porvenir”

Figura 2. Ubicación de la Estación de monitoreo de Calidad de aire

Fuente: Elaboración propia, 2024

**5.3. Resultados y Análisis Línea de Base**

Para caracterizar la línea de base de calidad del aire en el Área de Influencia del Proyecto, se consideraron
las mediciones de MP 10, MP 2,5, NO 2 y SO 2, monitoreadas en la estación de calidad del aire anteriormente
mencionada.

5.3.1 Material Particulado (MP 10 )

A continuación, se presenta una tabla con los valores de las concentraciones de MP 10 por año, aplicando el
criterio Percentil 98 de los promedios de 24 horas y el Promedio anual en los períodos registrados según los
años que se indican en la estación en estudio:

Informe de modelación de dispersión de contaminantes versión corregida,
_9_
Adenda “Condominios Fuentes de Porvenir”

Tabla 6. Percentil 98 concentraciones de 24 horas y Promedio anual de concentración de MP 10, periodo

2020 - 2022, Estación Punteras

|Estación|Año|Percentil 98<br>(μg/m3N)|Norma (μg/m3N)|Promedio<br>anual<br>(μg/m3N)|Norma<br>(μg/m3N)|
|---|---|---|---|---|---|
|Punteras|2020|58|130|26|50|
|Punteras|2021|70|130|31|50|
|Punteras|2022|64|130|30|50|
|Punteras|Promedio Trianual*|Promedio Trianual*|Promedio Trianual*|29|50|

*Corresponde al promedio trianual (2020 - 2021 - 2022) de concentración.

Fuente: Elaboración propia, 2024

Además, se presentan las gráficas asociadas a estas concentraciones para los períodos indicados.

Figura 3. Percentil 98 concentraciones 24 horas de MP 10, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Figura 4. Promedio anual de MP 10, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Informe de modelación de dispersión de contaminantes versión corregida,
_10_
Adenda “Condominios Fuentes de Porvenir”

Como se puede observar, los valores de los Percentiles 98 de las concentraciones de 24 horas de MP 10, de
los tres años en estudio, todos se encuentran bajo el límite establecido en el D.S. N°12/2022 del Ministerio
de Medio Ambiente de 120 μg/m [3] N.
Respecto de los valores de Concentración promedio anual para el periodo en estudio, estos tampoco
sobrepasan la norma, no superando el promedio trianual el límite establecido de 20 μg/m [3] N. El promedio
trianual fue 29 μg/m [3] N siendo inferior en un 42% respecto de la norma.

A continuación, en la Tabla 7, se presenta el resumen estadístico de los registros de Calidad del Aire
disponibles en el entorno del Proyecto.

Tabla 7. Resumen de concentraciones de MP 10 (μg/m [3] N)

|Contaminante|Norma|Estadístico|Estación<br>Punteras|Limite según Norma|Unidad|% de la Norma|
|---|---|---|---|---|---|---|
|MP10|Primaria|Promedio Anual1|29|50|(g/m3)|58,4|
|MP10|Primaria|Percentil 98 promedio diario - 2020|58|130|(g/m3)|44,6|
|MP10|Primaria|Percentil 98 promedio diario - 2021|<br>70|130|(g/m3)|53,5|
|MP10|Primaria|Percentil 98 promedio diario - 2022|<br>64|130|(g/m3)|49,2|

Fuente: Elaboración propia, 2024

Como se observa en la tabla anterior, la concentración de MP10, no supera el nivel de latencia para la norma
diaria y anual.

5.3.2 Material Particulado Fino (MP 2,5 )

A continuación, se presenta una tabla con los valores de las concentraciones de MP 2,5 por año, aplicando el
criterio Percentil 98 de los promedios de 24 horas y el Promedio anual en los períodos registrados según los
años que se indican por estación en estudio:

Tabla 8. Percentil 98 concentraciones de 24 horas y Promedio anual de concentración de MP 2,5, periodo

2020 - 2022, Estación Punteras

|Estación|Año|Percentil 98<br>(μg/m3N)|Norma (μg/m3N)|Promedio<br>anual<br>(μg/m3N)|Norma<br>(μg/m3N)|
|---|---|---|---|---|---|
|Punteras|2020|51|50|17|20|
|Punteras|2021|57|50|17|20|
|Punteras|2022|53|50|16|20|
|Punteras|Promedio Trianual*|Promedio Trianual*|Promedio Trianual*|17|20|

*Corresponde al promedio trianual (2020 - 2021 - 2022) de concentración.

Fuente: Elaboración propia, 2024

Además, se presentan las gráficas asociadas a estas concentraciones para los períodos indicados.

Informe de modelación de dispersión de contaminantes versión corregida,
_11_
Adenda “Condominios Fuentes de Porvenir”

Figura 5. Percentil 98 concentraciones 24 horas de MP 2,5, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Figura 6. Promedio anual de MP 2,5, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Como se puede observar, los valores de los Percentiles 98 de las concentraciones de 24 horas de MP 10, de
los tres años en estudio, todos se encuentran sobre el límite establecido en el D.S. N°12/2010 del Ministerio
de Medio Ambiente de 50 μg/m [3] N.
Respecto de los valores de Concentración promedio anual para el periodo en estudio, estos no sobrepasan
la norma, no superando el promedio trianual el límite establecido de 20 μg/m [3] N. El promedio trianual fue
17 μg/m [3] N siendo inferior en un 16% respecto de la norma.

A continuación, en la

Informe de modelación de dispersión de contaminantes versión corregida,
_12_
Adenda “Condominios Fuentes de Porvenir”

Tabla 9, se presenta el resumen estadístico de los registros de Calidad del Aire disponibles en el entorno del
Proyecto.

Informe de modelación de dispersión de contaminantes versión corregida,
_13_
Adenda “Condominios Fuentes de Porvenir”

Tabla 9. Resumen de concentraciones de MP 2,5 (μg/m [3] N)

|Contaminante|Norma|Estadístico|Estación<br>Punteras|Limite según Norma|Unidad|% de la Norma|
|---|---|---|---|---|---|---|
|MP2,5|Primaria|Promedio Anual1|17|20|(g/m3)|83,3|
|MP2,5|Primaria|Percentil 98 promedio diario - 2020|51|50|(g/m3)|101,6|
|MP2,5|Primaria|Percentil 98 promedio diario - 2021|57|50|(g/m3)|113,9|
|MP2,5|Primaria|Percentil 98 promedio diario - 2022|<br>53|50|(g/m3)|106,4|

Fuente: Elaboración propia, 2024

Como se observa en la tabla anterior, la concentración anual de MP2,5, alcanza el nivel de latencia para la
norma anual. Mientras que la norma diaria supera los niveles de saturación para los tres años en estudio.

5.3.3 Dióxido de Nitrógeno (NO 2 )

A continuación, se presenta una tabla con los valores de las concentraciones de MP 2,5 por año, aplicando el
criterio Percentil 99 de los máximos diarios de concentración de 1 hora y el Promedio anual en los períodos
registrados según los años que se indican por estación en estudio:

Tabla 10. Percentil 99 concentración de 1 hora y Promedio anual de concentración de NO 2, periodo 20202022, Estación Punteras

|Estación|Año|Percentil 99<br>(μg/m3N)|Norma (μg/m3N)|Promedio<br>anual<br>(μg/m3N)|Norma<br>(μg/m3N)|
|---|---|---|---|---|---|
|Punteras|2020|52,4|400|8,0|100|
|Punteras|2021|50,3|400|9,1|100|
|Punteras|2022|105,8|400|9,7|100|
|Punteras|Promedio<br>Trianual*|69,5|400|8,9|100|

*Corresponde al promedio trianual (2020 - 2021 - 2022) de concentración.

Fuente: Elaboración propia, 2024

Además, se presentan las gráficas asociadas a estas concentraciones para los períodos indicados.

Figura 7. Percentil 99 de concentración de 1 hora de NO 2, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Informe de modelación de dispersión de contaminantes versión corregida,
_14_
Adenda “Condominios Fuentes de Porvenir”

Figura 8. Promedio anual de NO 2, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Como se puede observar, el promedio trianual de los valores de los Percentiles 99 de las concentraciones de
1 hora de NO 2, de los tres años en estudio, todos se encuentran bajo el límite establecido en el D.S.
N°114/2002 del Ministerio de Secretaría General de la Presidencia de 400 μg/m [3] N. El promedio trianual
fue 69,5 μg/m [3] N siendo inferior en un 82% respecto de la norma.
Respecto de los valores de Concentración promedio anual para el periodo en estudio, estos no sobrepasan
la norma, no superando el promedio trianual el límite establecido de 100 μg/m [3] N. El promedio trianual fue
8,9 μg/m [3] N siendo inferior en un 91% respecto de la norma.

A continuación, en la Tabla 11, se presenta el resumen estadístico de los registros de Calidad del Aire
disponibles en el entorno del Proyecto.

Tabla 11. Resumen de concentraciones de NO 2 (μg/m [3] N)

|Contaminante|Norma|Estadístico|Estación<br>Punteras|Limite según<br>Norma|Unidad|% de la<br>Norma|
|---|---|---|---|---|---|---|
|NO2|Primaria|Promedio Anual1|8,9|100|(g/m3)|<br>8,9|
|NO2|Primaria|Percentil 99 promedio diario trianual|69,5|400|(g/m3)|<br>17,4|

Fuente: Elaboración propia, 2024

Como se observa en la tabla anterior, tanto el percentil 99 de 1 hora como la concentración anual de NO 2,
no alcanzan el nivel de latencia.

5.3.4 Dióxido de Azufre (SO 2 )

A continuación, se presenta una tabla con los valores de las concentraciones de SO 2 por año, aplicando el
criterio Percentil 99 de concentración de 1 hora, Percentil 99 de concentraciones de 24 horas y el Promedio
anual en los períodos registrados según los años que se indican por estación para el periodo en estudio:

Informe de modelación de dispersión de contaminantes versión corregida,
_15_
Adenda “Condominios Fuentes de Porvenir”

Tabla 12. Percentil 99 concentración de 1 hora, Percentil 99 concentraciones de 24 hora y Promedio anual

de concentración de SO 2, periodo 2020 - 2022, Estación Punteras

|Estación|Año|Percentil<br>99 1 hora<br>(μg/m3N)|Norma<br>(μg/m3N)|Percentil 99<br>24 horas<br>(μg/m3N)|Norma<br>(μg/m3N)|Promedio<br>anual<br>(μg/m3N)|Norma<br>(μg/m3N)|
|---|---|---|---|---|---|---|---|
|Punteras|2020|11,6|400|3,7|150|2,0|60|
|Punteras|2021|8,7|400|2,9|150|2,0|60|
|Punteras|2022|12,2|400|3,4|150|2,0|60|
|Punteras|Promedio<br>Trianual*|10,8|400|3,3|150|2,0|60|

*Corresponde al promedio trianual (2020 - 2021 - 2022) de concentración.

Fuente: Elaboración propia, 2024

Además, se presentan las gráficas asociadas a estas concentraciones para los períodos indicados.

Figura 9. Percentil 99 de concentración de 1 hora de SO 2, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Informe de modelación de dispersión de contaminantes versión corregida,
_16_
Adenda “Condominios Fuentes de Porvenir”

Figura 10. Percentil 99 de concentración de 24 horas de SO 2, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Figura 11. Promedio anual de SO 2, periodo 2020 - 2022, Estación Punteras

Fuente: Elaboración propia, 2024

Como se puede observar, el promedio trianual de los valores de los Percentiles 99 de las concentraciones de
1 hora de SO 2, de los tres años en estudio, todos se encuentran bajo el límite establecido en el D.S.
N°114/2002 del Ministerio de Secretaría General de la Presidencia de 400 μg/m [3] N. El promedio trianual
fue 10,8 μg/m [3] N siendo inferior en un 96,9% respecto de la norma.
En cuanto al promedio trianual de los valores de Percentiles 99 para las concentraciones de 24 horas de SO 2,
de los tres años en estudio, todos se encuentran bajo el límite establecido de 150 μg/m [3] N. El promedio
trianual fue 3,3 μg/m [3] N siendo inferior en un 97,8% respecto de la norma.
Respecto de los valores de Concentración promedio anual para el periodo en estudio, estos tampoco
sobrepasan la norma, no superando el promedio trianual el límite establecido de 60 μg/m [3] N. El promedio
trianual fue 2,0 μg/m [3] N siendo inferior en un 96,7% respecto de la norma.

A continuación, en la Tabla 13, se presenta el resumen estadístico de los registros de Calidad del Aire
disponibles en el entorno del Proyecto.

Informe de modelación de dispersión de contaminantes versión corregida,
_17_
Adenda “Condominios Fuentes de Porvenir”

Tabla 13. Resumen de concentraciones de SO 2 (μg/m [3] N)

|Contaminante|Norma|Estadístico|Estación<br>Punteras|Limite según<br>Norma|Unidad|% de la<br>Norma|
|---|---|---|---|---|---|---|
|SO2|Primaria|Percentil 99 promedio horario trianual|10,8|350|(g/m3)|<br>3,1|
|SO2|Primaria|Percentil 99 promedio diario trianual|3,3|150|(g/m3)|<br>2,2|
|SO2|Primaria|Promedio Anual1|2,0|60|(g/m3)|<br>3,3|

Fuente: Elaboración propia, 2024

Como se observa en la tabla anterior, tanto el percentil 99 de 1 hora, percentil 99 de 24 horas como la
concentración anual de SO 2, no alcanzan el nivel de latencia.

**5.4 Descripción y justificación del modelo**

El modelo utilizado para este análisis es el SCREEN 3 de la United States Environmental Protection Agency
(USEPA). Este modelo nos permite determinar el aporte de las emisiones provenientes de fuentes emisoras,
en localidades y sectores aledaños a las instalaciones del Proyecto, permitiendo de este modo asignar las
cuotas de responsabilidad en los niveles de calidad del aire proyectados en su entorno.

El modelo SCREEN 3, se desarrolló como una herramienta para realizar estimaciones de concentraciones
de contaminantes, tomando como base el documento de procedimientos de proyección de la USEPA,
utilizando un modelo de dispersión Gaussiano que incorpora factores relacionados a la fuente emisora y
factores meteorológicos para estimar concentraciones de contaminantes de fuentes continuas. Se asume que
el contaminante no sufre reacciones químicas y que la pluma no es afectada por procesos de remoción, como
deposición seca o húmeda, durante su transporte desde la fuente. Las variables de entrada introducidas al
modelo, incluyen características de la fuente y la tasa de emisión correspondiente a cada contaminante a
evaluar.

Cabe destacar que el modelo SCREEN 3 siempre entrega como resultado concentraciones ambientales
sobreestimadas, debido a que genera internamente la condición meteorológica más desfavorable, es decir,
aquella con la que se obtiene la concentración ambiental más alta, considerando además que el diseño del
modelo ubica al receptor recibiendo el viento directo de las fuentes y no considerando factores atenuadores
como la topografía. Por lo anterior, la estimación con SCREEN 3, establece un techo o valor máximo, que
en la práctica nunca ocurre, por lo que las concentraciones reales en un punto determinado son siempre
menores a las estimadas por este modelo.

**5.5 Fuentes de emisión**

La modelación de las emisiones producto de la superposición de la fase de construcción y operación del
Proyecto (año 1) en estudio, se realizó considerando la dispersión del material particulado MP 10 y MP 2,5
presentes en las emisiones por resuspensión y combustión, así como los gases, CO, NO X y SO X, producto de
la combustión en las fuentes estacionarias y móviles, asociadas a las actividades del Proyecto.

Además, se consideraron las emisiones anuales asociadas a las fuentes emisoras de contaminantes del
Proyecto (ver Tabla 1), producidas en toda la superficie del sitio del Proyecto. El resultado de las emisiones
generadas espacial y temporalmente, se presenta en la tabla que se muestra a continuación.

Informe de modelación de dispersión de contaminantes versión corregida,
_18_
Adenda “Condominios Fuentes de Porvenir”

Tabla 14. Tasas de emisiones del Proyecto, Fase construcción y operación

|Emisiones|CO|SO<br>x|NO<br>X|MP<br>2,5 Total|MP<br>10 Total|
|---|---|---|---|---|---|
|ton/año|0,2877|0,0044|0,3687|0,0515|0,1759|
|g/m2-s|**0,0000014186**|**0,0000000215**|**0,0000018177**|**0,0000002539**|**0,0000008675**|

Fuente: Elaboración propia, 2024

Cabe destacar, que las tasas de emisión presentadas en la tabla anterior, corresponde al total de las
emisiones generadas por al interior del Proyecto, por lo que se está considerando que todas las actividades
se realizan al mismo tiempo, por lo tanto, los valores entregados representan el escenario de emisión más
desfavorable para las fuentes descritas.

Los receptores considerados corresponden a casas y edificio cercanos, además de una bodega.
Adicionalmente, se consideró a los edificios de la Etapa A-I, como receptor interno del Proyecto.

Figura 12. Ubicación de los potenciales receptores

Fuente: Elaboración propia, 2024

Sin embargo, se considerará la distancia del Punto de Máxima Concentración (PMC) proyectada desde la
fuente de emisión, para realizar el análisis de cumplimiento de las normas de referencia de calidad del aire.

Informe de modelación de dispersión de contaminantes versión corregida,
_19_
Adenda “Condominios Fuentes de Porvenir”

**5.6 Resultados de la modelación**

5.6.1 Superposición de la fase de construcción y operación

La modelación de la dispersión de las emisiones de los distintos contaminantes, fue considerada como
fuentes de área, y se realizó estableciendo como datos de entrada las siguientes opciones que permite el
modelo.

Tabla 15. Datos de entrada del modelo

|Parámetro|Datos de entrada|Unidad|
|---|---|---|
|Tipo de fuente|Área|-|
|Altura de liberación|1,0|m|
|Longitud de lado largo|195|m|
|Longitud de lado corto|94|m|
|Altura del receptor|1,5|m|
|Terreno Urbano/Rural|Urbano|-|
|Altura de la mezcla|30|m|
|Altura anemométrica|5|m|
|Clase de estabilidad|3|“Inestable”|
|Velocidad eólica|1,0|m/s|

Fuente: Elaboración propia, 2024

La tabla siguiente, muestra los resultados de la modelación del Proyecto, con el cual se obtuvo la dispersión
de las concentraciones de los distintos contaminantes, a distancias entre 10 y 5.000 m del Proyecto, con lo
que se determinó el aporte de contaminantes (concentración) sobre los potenciales receptores de interés.

Tabla 16. Resultados del modelo, Fase de la superposición de la fase de construcción y operación

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Distancia (m)|CO|SO2|NO2|MP2,5 Total|MP10 Total|
|10|17,07|0,262|22,19|3,055|10,43|
|20|17,58|0,2698|22,84|3,146|10,74|
|30|18,05|0,277|23,45|3,23|11,030|
|40|18,49|0,2838|24,03|3,309|11,300|
|50|18,92|0,2903|24,58|3,385|11,560|
|60|19,33|0,2966|25,11|3,458|11,810|
|70|19,72|0,3026|25,62|3,529|12,050|
|80|20,1|0,3084|26,12|3,597|12,280|
|90|20,47|0,3141|26,6|3,663|12,500|
|100|20,75|0,3185|26,97|3,714|12,680|
|110|20,05|0,3077|26,06|3,588|12,250|
|120|14,89|0,2285|19,34|2,664|9,0,94|
|130|12,23|0,1878|15,9|2,189|7,474|
|140|10,62|0,163|13,8|1,9|6,487|
|150|9,528|0,1462|12,38|1,705|5,821|
|200|7,035|0,108|9,141|1,259|4,297|
|250|5,946|0,09124|7,726|1,064|3,632|
|300|5,168|0,07931|6,716|0,9248|3,157|
|350|4,556|0,06992|5,92|0,8153|2,783|
|400|4,07|0,06246|5,289|0,7284|2,486|
|450|3,678|0,05645|4,78|0,6582|2,247|
|500|3,357|0,05152|4,363|0,6008|2,051|
|600|2,865|0,04397|3,723|0,5127|1,750|

Informe de modelación de dispersión de contaminantes versión corregida,
_20_
Adenda “Condominios Fuentes de Porvenir”

|Distancia (m)|Concentración horaria (g/m3)|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Distancia (m)|CO|SO2|NO2|MP2,5 Total|MP10 Total|
|700|2,506|0,03845|3,256|0,4484|1,531|
|800|2,233|0,03427|2,902|0,3996|1,364|
|900|2,019|0,03098|2,623|0,3612|1,233|
|1000|1,845|0,02832|2,398|0,3303|1,1270|
|1500|1,321|0,02027|1,717|0,2364|0,8071|
|2000|1,052|0,01614|1,366|0,1882|0,6424|
|2500|0,8874|0,01362|1,153|0,1588|0,5421|
|3000|0,7761|0,1191|1,009|0,1389|0,4741|
|3500|0,695|0,1067|0,9032|0,1244|0,4246|
|4000|0,633|0,009715|0,8226|0,1133|0,3867|
|5000|0,544|0,008348|0,7069|9734|0,3323|

Fuente: Elaboración propia, 2024

El resultado de las máximas concentraciones horarias (μg/m3) arrojadas por el modelo, se presentan en la
Tabla 17 que se muestra a continuación.

Tabla 17. Máximas concentraciones horarias obtenidas del modelo

|Lugar|Distancia máx,<br>concentración<br>(m)|Concentración horaria (g/m3)|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Lugar|Distancia máx,<br>concentración<br>(m)|CO|SO2|NO2|MP2,5 Total|MP10 Tota|
|Proyecto|100|20,75|0,3185|26,97|3,714|12,680|

Fuente: Elaboración propia, 2024

Es necesario destacar que el modelo entrega concentraciones a nivel horario, las que son convertidas a
concentraciones de 3 h, 8 h, 24 h o anuales, de acuerdo a los factores de conversión establecidos por la EPA [3]
y que se presentan en la siguiente tabla.

Tabla 18. Factores de conversión para promedios máximos de concentración

|Tiempo promedio|Factor conversión|
|---|---|
|3 horas|0,9|
|8 horas|0,7|
|24 horas|0,4|
|Anual|0,08|

Fuente: Screening Procedures for Estimating the Air Quality Impact of Stationary Sources (USEPA 1992).

Para evaluar el nivel de cumplimiento de la normativa ambiental con respecto al material particulado, se
han considerado como referencia el D.S. N°12/10, del Ministerio de Medio Ambiente, que establece la
Norma de Calidad Primaria para Material Particulado Fino Respirable MP2,5 y el D.S. N°12/22 para
Material Particulado MP10, en especial los valores que definen situaciones de emergencia, la cual se
comparó con la concentración máxima aportada por el proyecto.

Para los gases NO 2 se ha considerado como referencia el D.S. N°114 del Ministerio Secretaría General de la
Presidencia, que establece la Norma de Calidad Primaria de Aire para Dióxido de Nitrógeno (NO 2 ), A su vez,
para el contaminante SO 2 se ha considerado como referencia el D.S. N°104 del Ministerio de Medio
Ambiente, que establece la Norma de Calidad Primaria de Aire para Dióxido de Azufre (SO 2 ). Finalmente,
para el contaminante CO se ha utilizado el D.S. N°115 de Ministerio Secretaría General de la Presidencia,
que establece la Norma de Calidad Primaria de Aire para Monóxido de Carbono (CO).

3 Screening Procedures for Estimating the Air Quality Impact of Stationary Sources. U.S. Environmental Protection Agency (USEPA). Octubre de

1992. Pp 39.

Informe de modelación de dispersión de contaminantes versión corregida,
_21_
Adenda “Condominios Fuentes de Porvenir”

A continuación, se presenta el análisis de cumplimiento de las normas de referencia de calidad del aire,
respecto de la concentración máxima para los contaminantes indicados anteriormente en la Tabla 17, la cual
se presentará a una distancia de 100 m del Proyecto.

Tabla 19. Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase construcción y

operación

|Parámetro|Estadístico|Máxima del<br>proyecto<br>(g/m3N)|Limite según<br>Norma<br>(g/m3)|Porcentaje<br>respecto de la<br>Norma (%)|Referencia|
|---|---|---|---|---|---|
|MP10 <br>|Concentración 24 horas|5,1|130|3,9|D.S. N°12 / 2022 MMA|
|MP10 <br>|Concentración anual|1,0|50|2,0|2,0|
|MP2,5 <br>|Concentración 24 horas|1,5|50|3,0|D.S. N°12/2010 del MMA|
|MP2,5 <br>|Concentración anual|0,3|20|1,5|1,5|
|NO2|Concentración 1 hora|27,0|400|6,7|D.S. N°114/ 2002 MINSEGPRES|
|NO2|Concentración anual|2,2|100|2,2|2,2|
|SO2 <br>|Concentración 1 hora|0,32|350|0,091|D.S. N°104/ 2018 MMA|
|SO2 <br>|Concentración 24 horas|0,127|150|0,085|0,085|
|SO2 <br>|Concentración anual|0,025|60|0,042|0,042|
|CO|Concentración 1 hora|20,8|30.000|0,069|~~D~~.S. N°115/2002 del MINSEGPRES|
|CO|Concentración 8 horas|14,5|10.000|0,145|0,145|

Fuente: Elaboración propia, 2024

Informe de modelación de dispersión de contaminantes versión corregida,
_22_
Adenda “Condominios Fuentes de Porvenir”

Al respecto, las concentraciones máximas en el área del Proyecto se encontrarán muy por debajo de los límites de concentración establecidos por sus
correspondientes normas de referencia, por lo que el aporte de emisiones a los potenciales receptores será igualmente bajo, aun considerando el efecto sinérgico
por la operación simultánea de todas las actividades del proyecto durante su fase de construcción y operación en el año 1.

Tabla 20. Concentraciones por distancia de los contaminantes analizados, Fase de construcción y operación

|Distancia<br>(m)|Concentración (g/m3)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Distancia<br>(m)|CO <br>(1 hora)|CO <br>(8 horas)|SO2 <br>(1 hora)|SO2 <br>(24 horas)|SO2 <br>(Anual)|NO2 <br>(1 hora)|NO2 <br>(Anual)|MP2,5 Total<br>(24 horas)|MP2,5 Total<br>(Anual)|MP10 Total<br>(24 horas)|MP10 Total<br>(Anual)|
|10|17,07|11,949|0,262|0,105|0,021|22,190|1,775|1,222|0,244|4,172|0,834|
|20|17,58|12,306|0,270|0,108|0,022|22,840|1,827|1,258|0,252|4,296|0,859|
|30|18,05|12,635|0,277|0,111|0,022|23,450|1,876|1,292|0,258|4,412|0,882|
|40|18,49|12,943|0,284|0,114|0,023|24,030|1,922|1,324|0,265|4,520|0,904|
|50|18,92|13,244|0,290|0,116|0,023|24,580|1,966|1,354|0,271|4,624|0,925|
|60|19,33|13,531|0,297|0,119|0,024|25,110|2,009|1,383|0,277|4,724|0,945|
|70|19,72|13,804|0,303|0,121|0,024|25,620|2,050|1,412|0,282|4,820|0,964|
|80|20,1|14,070|0,308|0,123|0,025|26,120|2,090|1,439|0,288|4,912|0,982|
|90|20,47|14,329|0,314|0,126|0,025|26,600|2,128|1,465|0,293|5,000|1,000|
|100*|20,75|14,525|0,319|0,127|0,025|26,970|2,158|1,486|0,297|5,072|1,014|
|110|20,05|14,035|0,308|0,123|0,025|26,060|2,085|1,435|0,287|4,900|0,980|
|120|14,89|10,423|0,229|0,091|0,018|19,340|1,547|1,066|0,213|3,638|0,728|
|130|12,23|8,561|0,188|0,075|0,015|15,900|1,272|0,876|0,175|2,990|0,598|
|140|10,62|7,434|0,163|0,065|0,013|13,800|1,104|0,760|0,152|2,595|0,519|
|150|9,528|6,670|0,146|0,058|0,012|12,380|0,990|0,682|0,136|2,328|0,466|
|200|7,035|4,925|0,108|0,043|0,009|9,141|0,731|0,504|0,101|1,719|0,344|
|250|5,946|4,162|0,091|0,036|0,007|7,726|0,618|0,426|0,085|1,453|0,291|
|300|5,168|3,618|0,079|0,032|0,006|6,716|0,537|0,370|0,074|1,263|0,253|
|350|4,556|3,189|0,070|0,028|0,006|5,920|0,474|0,326|0,065|1,113|0,223|
|400|4,07|2,849|0,062|0,025|0,005|5,289|0,423|0,291|0,058|0,994|0,199|
|450|3,678|2,575|0,056|0,023|0,005|4,780|0,382|0,263|0,053|0,899|0,180|
|500|3,357|2,350|0,052|0,021|0,004|4,363|0,349|0,240|0,048|0,820|0,164|
|600|2,865|2,006|0,044|0,018|0,004|3,723|0,298|0,205|0,041|0,700|0,140|
|700|2,506|1,754|0,038|0,015|0,003|3,256|0,260|0,179|0,036|0,612|0,122|
|800|2,233|1,563|0,034|0,014|0,003|2,902|0,232|0,160|0,032|0,546|0,109|
|900|2,019|1,413|0,031|0,012|0,002|2,623|0,210|0,144|0,029|0,493|0,099|
|1000|1,845|1,292|0,028|0,011|0,002|2,398|0,192|0,132|0,026|0,451|0,090|
|1500|1,321|0,925|0,020|0,008|0,002|1,717|0,137|0,095|0,019|0,323|0,065|
|2000|1,052|0,736|0,016|0,006|0,001|1,366|0,109|0,075|0,015|0,257|0,051|
|2500|0,8874|0,621|0,014|0,005|0,001|1,153|0,092|0,064|0,013|0,217|0,043|

Informe de modelación de dispersión de contaminantes versión corregida,
23
Adenda “Condominios Fuentes de Porvenir”

|Distancia<br>(m)|Concentración (g/m3)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Distancia<br>(m)|CO <br>(1 hora)|CO <br>(8 horas)|SO2 <br>(1 hora)|SO2 <br>(24 horas)|SO2 <br>(Anual)|NO2 <br>(1 hora)|NO2 <br>(Anual)|MP2,5 Total<br>(24 horas)|MP2,5 Total<br>(Anual)|MP10 Total<br>(24 horas)|MP10 Total<br>(Anual)|
|3000|0,7761|0,543|0,119|0,048|0,0095|1,009|0,081|0,056|0,011|0,190|0,038|
|3500|0,695|0,487|0,107|0,043|0,0085|0,903|0,072|0,050|0,010|0,170|0,034|
|4000|0,633|0,443|0,010|0,004|0,0008|0,823|0,066|0,045|0,009|0,155|0,031|
|5000<br>|0,544<br>|0,381<br>|0,008<br>|0,003<br>|0,0007|0,707|0,057|0,039|0,008|0,133|0,027|

- Distancia en la que se presentará la concentración máxima de contaminantes.

Fuente: Elaboración propia, 2024

Informe de modelación de dispersión de contaminantes versión corregida,
_24_
Adenda “Condominios Fuentes de Porvenir”

A partir de los resultados obtenidos y del análisis normativo realizado se determinó el área de influencia
(AI) del proyecto, el cual se muestra en la figura siguiente.

Figura 13. Área de influencia del Proyecto

 - MP10

Informe de modelación de dispersión de contaminantes versión corregida,
25
Adenda “Condominios Fuentes de Porvenir”

 - MP2,5

Informe de modelación de dispersión de contaminantes versión corregida,
_26_
Adenda “Condominios Fuentes de Porvenir”

 - NO2

Informe de modelación de dispersión de contaminantes versión corregida,
_27_
Adenda “Condominios Fuentes de Porvenir”

 - SO2

Informe de modelación de dispersión de contaminantes versión corregida,
_28_
Adenda “Condominios Fuentes de Porvenir”

 - CO

Fuente: Elaboración propia, 2024

Comparando los resultados de Tabla 20 con las distancias a los receptores considerados en la Figura 12,
es posible afirmar que todos los receptores se encuentran dentro del área de influencia del Proyecto y del
punto de máximo impacto de este. **Sin embargo, es importante señalar que, las concentraciones**
**de contaminantes en el aire que se producen por causa de las emisiones del Proyecto**
**durante la superposición de la fase de construcción y operación durante el año 1, no son**
**significativas, por cuanto se encuentran muy por debajo del límite establecido por las**
**normativas de referencia, tal como se presentó en la Tabla 17, y no generan un impacto**
**negativo sobre la calidad del aire.**

En consecuencia, no se requeriría utilizar un modelo más complejo y los resultados son concluyentes, por
cuanto indican que las emisiones del Proyecto no producirán efectos adversos significativos en la calidad
del aire, aun considerando las peores condiciones de emisión y meteorológicas.

Informe de modelación de dispersión de contaminantes versión corregida,
_29_
Adenda “Condominios Fuentes de Porvenir”

Cabe destacar, que el modelo SCREEN 3 no entrega la opción de ingresar datos meteorológicos que sean
representativos de un sector específico. En lugar de eso, lo que hace es examinar respecto de rangos de
estabilidad y velocidades del viento, que sí pueden ser ingresados, para identificar el peor caso de
condiciones meteorológicas, es decir, la combinación de la velocidad del viento y estabilidad que resulta
más desfavorable,

**6. ANÁLISIS IMPACTO DE EMISIONES EN ZONAS SATURADAS POR MATERIAL**
**PARTICULADO MP** **10** **Y MATERIAL PARTICULADO FINO RESPIRABLE MP** **2,5**

En la siguiente tabla se presentan los valores de significancia obtenidos de la modelación.

Tabla 21. Evaluación de Significancia

|Col1|Proyecto|Col3|Valores de<br>Significancia<br>Tabla 2|Col5|Proyecto|Col7|Valores de<br>Significancia<br>Tabla 2|Col9|¿CUMPLE?|
|---|---|---|---|---|---|---|---|---|---|
||MP10 Total|MP10 Total|MP10 Total|MP10 Total|MP2,5 Total|MP2,5 Total|MP2,5 Total|MP2,5 Total|MP2,5 Total|
||24<br>horas|Anual|24<br>horas|Anual|24<br>horas|Anual|24<br>horas|Anual|Anual|
|Concentración<br>(μg/m3)|5,072|1,014|10,00|3,00|1,486|0,297|5,13|0,99|SÍ|

Fuente: Elaboración propia, 2024

En base a los resultados obtenidos y considerando el análisis de la guía “Criterio de evaluación en el SEIA:
Impacto de emisiones en zonas saturadas por material particulado respirable MP10 y material particulado
fino respirable MP2,5” (SEA, 2023), se obtuvo que al evaluar el impacto de dichos contaminantes
provenientes del estudio de estimación de emisiones atmosféricas, al aplicar los valores de la Tabla 2 de
la guía, por tener mayor emisiones solamente durante el año 1 durante la spersopiscino de la fase de
construcción y operación del lote ya construido (duración menor a 3 años), se obtuvieron valores de
concentración en su punto de máximo impacto, menores a los de la Tabla 2 de la guía, tanto para el periodo
de 24 horas como para la métrica anual. **De esta manera, se puede concluir que el Proyecto**
**durante la superposición de su fase de construcción y operación, y no generará impactos**
**significativos en la salud de la población cercana al Proyecto** .

Informe de modelación de dispersión de contaminantes versión corregida,
_30_
Adenda “Condominios Fuentes de Porvenir”

**7. CONCLUSIÓN**

En la

Informe de modelación de dispersión de contaminantes versión corregida,
_31_
Adenda “Condominios Fuentes de Porvenir”

Tabla 14 se observan los valores alcanzados por las emisiones anuales asociadas a cada una de las fuentes
emisoras de contaminantes, además de las emisiones totales, considerando que todas las actividades
operarán al mismo tiempo movimiento de tierra, maquinaria y traslado, para de esta forma obtener la
situación más desfavorable de la superposición de la fase de construcción y operación durante el año 1.

En tanto que, en la Tabla 20 se pueden observar los valores de las concentraciones de dispersión de los
contaminantes modelados mediante SCREEN 3, en el cual se consideró el funcionamiento de todas las
actividades a la vez en el área de Proyecto y por el mismo periodo de tiempo. Al respecto, se aprecia que
los puntos de máxima concentración aportadas por el Proyecto, se presentarán a una distancia de 100 m
alrededor de las fuentes emisoras. En tanto que, en la Tabla 17 se estableció que ninguno de estos
contaminantes sobrepasará el umbral de sus correspondientes normas, mientras que en la Tabla 21 se
estableció que los valores de concentración en el punto de máximo impacto son menores a la Tabla 2 de
la Guía de Impacto de Material Particulado en Zonas Saturadas (2023), por lo que su aporte de emisiones
a la atmósfera no afectará de forma significativa a la calidad del aire del sector.

Finalmente, y de acuerdo a los resultados aquí descritos, se puede concluir que las emisiones asociadas al
Proyecto son bajas y en ningún caso producirán efectos adversos significativos en la calidad del aire, que
afecten a la salud de las personas o la calidad de los recursos naturales del sector, aun considerando las
peores condiciones de emisión y meteorológicas. Así mismo, y por esta misma razón no se requerirá en
este análisis, la utilización de otro modelo más complejo.

Informe de modelación de dispersión de contaminantes versión corregida,
_32_
Adenda “Condominios Fuentes de Porvenir”

**8. REFERENCIAS**

`o` Guía de estimación de emisiones atmosféricas. Seremi de Medio Ambiente. Junio 2020.
`o` Compilation of Air Pollutant Emission Factors, AP 42, Actualizada por EPA en su sitio Web en
diciembre 2011.
`o` Guía Metodológica Inventario de Emisiones Atmosféricas, M11 Metodología SINCA 2011
Ambiosis S,A, octubre 2011.
`o` Industria del Árido en Chile, Tomo I, Sistematización de Antecedentes Técnicos y Ambientales,
Corporación de Desarrollo Tecnológico, Comisión Nacional del Árido, Santiago, diciembre de

2001.
`o` Informe Final, “Servicio de Recopilación y Sistematización de Factores de Emisión al Aire para el
Servicio de Evaluación Ambiental”, de mayo 2015.
`o` Reconciling Urban Fugitive Dust Emissions Inventory and Ambient Source Contribution
Estimates: Summary of Current Knowledge and Needed Research, del Desert Research Institute
(2000), publicado por la Universidad University and Community College System of Nevada.

Informe de modelación de dispersión de contaminantes versión corregida,
_33_
Adenda “Condominios Fuentes de Porvenir”

### APÉNDICE 1: MEMORIA DE CÁLCULO DE LA MODELACIÓN

Informe de modelación de dispersión de contaminantes versión corregida,
_34_
Adenda “Condominios Fuentes de Porvenir”

03/15/24
13:10:06
*** SCREEN3 MODEL RUN ***
*** VERSION DATED 13043 ***

D:\GIZA Ingenieria\DIAs\CFP_Condominio Fuentes de Porvenir\Emisiones\ADENDA\Mod

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA
EMISSION RATE (G/(S-M**2)) = 0.867800E-06
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 195.0000
LENGTH OF SMALLER SIDE (M) = 94.0000
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
10. 10.43 3 1.0 1.0 30.0 1.00 1.

20. 10.74 3 1.0 1.0 30.0 1.00 0.

30. 11.03 3 1.0 1.0 30.0 1.00 0.

40. 11.30 3 1.0 1.0 30.0 1.00 0.
50. 11.56 3 1.0 1.0 30.0 1.00 0.
60. 11.81 3 1.0 1.0 30.0 1.00 0.

70. 12.05 3 1.0 1.0 30.0 1.00 0.
80. 12.28 3 1.0 1.0 30.0 1.00 0.

90. 12.50 3 1.0 1.0 30.0 1.00 0.
100. 12.68 3 1.0 1.0 30.0 1.00 10.

110. 12.25 3 1.0 1.0 30.0 1.00 25.

120. 9.094 3 1.0 1.0 30.0 1.00 24.

130. 7.474 3 1.0 1.0 30.0 1.00 22.

Informe de modelación de dispersión de contaminantes versión corregida,
_35_
Adenda “Condominios Fuentes de Porvenir”

140. 6.487 3 1.0 1.0 30.0 1.00 19.
150. 5.821 3 1.0 1.0 30.0 1.00 17.

200. 4.297 3 1.0 1.0 30.0 1.00 0.
250. 3.632 3 1.0 1.0 30.0 1.00 0.

300. 3.157 3 1.0 1.0 30.0 1.00 0.
350. 2.783 3 1.0 1.0 30.0 1.00 0.
400. 2.486 3 1.0 1.0 30.0 1.00 0.

450. 2.247 3 1.0 1.0 30.0 1.00 0.

500. 2.051 3 1.0 1.0 30.0 1.00 0.
600. 1.750 3 1.0 1.0 30.0 1.00 2.

700. 1.531 3 1.0 1.0 30.0 1.00 0.
800. 1.364 3 1.0 1.0 30.0 1.00 0.

900. 1.233 3 1.0 1.0 30.0 1.00 0.

1000. 1.127 3 1.0 1.0 30.0 1.00 3.
1500. 0.8071 3 1.0 1.0 30.0 1.00 0.
2000. 0.6424 3 1.0 1.0 30.0 1.00 8.

2500. 0.5421 3 1.0 1.0 30.0 1.00 5.

3000. 0.4741 3 1.0 1.0 30.0 1.00 4.
3500. 0.4246 3 1.0 1.0 30.0 1.00 4.
4000. 0.3867 3 1.0 1.0 30.0 1.00 4.

5000. 0.3323 3 1.0 1.0 30.0 1.00 4.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN
PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 12.68 100. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

Informe de modelación de dispersión de contaminantes versión corregida,
_36_
Adenda “Condominios Fuentes de Porvenir”

03/15/24
13:18:00
*** SCREEN3 MODEL RUN ***
*** VERSION DATED 13043 ***

D:\GIZA Ingenieria\DIAs\CFP_Condominio Fuentes de Porvenir\Emisiones\ADENDA\Mod

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA
EMISSION RATE (G/(S-M**2)) = 0.254200E-06
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 195.0000
LENGTH OF SMALLER SIDE (M) = 94.0000
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
10. 3.055 3 1.0 1.0 30.0 1.00 1.
20. 3.146 3 1.0 1.0 30.0 1.00 0.

30. 3.230 3 1.0 1.0 30.0 1.00 0.

40. 3.309 3 1.0 1.0 30.0 1.00 0.
50. 3.385 3 1.0 1.0 30.0 1.00 0.
60. 3.458 3 1.0 1.0 30.0 1.00 0.

70. 3.529 3 1.0 1.0 30.0 1.00 0.
80. 3.597 3 1.0 1.0 30.0 1.00 0.
90. 3.663 3 1.0 1.0 30.0 1.00 0.

100. 3.714 3 1.0 1.0 30.0 1.00 10.
110. 3.588 3 1.0 1.0 30.0 1.00 25.
120. 2.664 3 1.0 1.0 30.0 1.00 24.
130. 2.189 3 1.0 1.0 30.0 1.00 22.

Informe de modelación de dispersión de contaminantes versión corregida,
_37_
Adenda “Condominios Fuentes de Porvenir”

140. 1.900 3 1.0 1.0 30.0 1.00 19.

150. 1.705 3 1.0 1.0 30.0 1.00 17.

200. 1.259 3 1.0 1.0 30.0 1.00 0.
250. 1.064 3 1.0 1.0 30.0 1.00 0.
300. 0.9248 3 1.0 1.0 30.0 1.00 0.
350. 0.8153 3 1.0 1.0 30.0 1.00 0.
400. 0.7284 3 1.0 1.0 30.0 1.00 0.
450. 0.6582 3 1.0 1.0 30.0 1.00 0.
500. 0.6008 3 1.0 1.0 30.0 1.00 0.
600. 0.5127 3 1.0 1.0 30.0 1.00 2.
700. 0.4484 3 1.0 1.0 30.0 1.00 0.
800. 0.3996 3 1.0 1.0 30.0 1.00 0.
900. 0.3612 3 1.0 1.0 30.0 1.00 0.

1000. 0.3303 3 1.0 1.0 30.0 1.00 3.
1500. 0.2364 3 1.0 1.0 30.0 1.00 0.
2000. 0.1882 3 1.0 1.0 30.0 1.00 8.
2500. 0.1588 3 1.0 1.0 30.0 1.00 5.
3000. 0.1389 3 1.0 1.0 30.0 1.00 4.

3500. 0.1244 3 1.0 1.0 30.0 1.00 4.

4000. 0.1133 3 1.0 1.0 30.0 1.00 4.
5000. 0.9734E-01 3 1.0 1.0 30.0 1.00 4.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN
PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------SIMPLE TERRAIN 3.714 100. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

Informe de modelación de dispersión de contaminantes versión corregida,
_38_
Adenda “Condominios Fuentes de Porvenir”

03/15/24
13:29:08
*** SCREEN3 MODEL RUN ***
*** VERSION DATED 13043 ***

D:\GIZA Ingenieria\DIAs\CFP_Condominio Fuentes de Porvenir\Emisiones\ADENDA\Mod

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA
EMISSION RATE (G/(S-M**2)) = 0.184590E-05
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 195.0000
LENGTH OF SMALLER SIDE (M) = 94.0000
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
10. 22.19 3 1.0 1.0 30.0 1.00 1.
20. 22.84 3 1.0 1.0 30.0 1.00 0.

30. 23.45 3 1.0 1.0 30.0 1.00 0.

40. 24.03 3 1.0 1.0 30.0 1.00 0.
50. 24.58 3 1.0 1.0 30.0 1.00 0.
60. 25.11 3 1.0 1.0 30.0 1.00 0.
70. 25.62 3 1.0 1.0 30.0 1.00 0.
80. 26.12 3 1.0 1.0 30.0 1.00 0.
90. 26.60 3 1.0 1.0 30.0 1.00 0.
100. 26.97 3 1.0 1.0 30.0 1.00 10.
110. 26.06 3 1.0 1.0 30.0 1.00 25.

120. 19.34 3 1.0 1.0 30.0 1.00 24.

130. 15.90 3 1.0 1.0 30.0 1.00 22.

Informe de modelación de dispersión de contaminantes versión corregida,
_39_
Adenda “Condominios Fuentes de Porvenir”

140. 13.80 3 1.0 1.0 30.0 1.00 19.
150. 12.38 3 1.0 1.0 30.0 1.00 17.

200. 9.141 3 1.0 1.0 30.0 1.00 0.
250. 7.726 3 1.0 1.0 30.0 1.00 0.
300. 6.716 3 1.0 1.0 30.0 1.00 0.

350. 5.920 3 1.0 1.0 30.0 1.00 0.
400. 5.289 3 1.0 1.0 30.0 1.00 0.
450. 4.780 3 1.0 1.0 30.0 1.00 0.
500. 4.363 3 1.0 1.0 30.0 1.00 0.
600. 3.723 3 1.0 1.0 30.0 1.00 2.
700. 3.256 3 1.0 1.0 30.0 1.00 0.
800. 2.902 3 1.0 1.0 30.0 1.00 0.
900. 2.623 3 1.0 1.0 30.0 1.00 0.
1000. 2.398 3 1.0 1.0 30.0 1.00 3.

1500. 1.717 3 1.0 1.0 30.0 1.00 0.
2000. 1.366 3 1.0 1.0 30.0 1.00 8.

2500. 1.153 3 1.0 1.0 30.0 1.00 5.

3000. 1.009 3 1.0 1.0 30.0 1.00 4.

3500. 0.9032 3 1.0 1.0 30.0 1.00 4.
4000. 0.8226 3 1.0 1.0 30.0 1.00 4.
5000. 0.7069 3 1.0 1.0 30.0 1.00 4.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN
PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------SIMPLE TERRAIN 26.97 100. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

Informe de modelación de dispersión de contaminantes versión corregida,
_40_
Adenda “Condominios Fuentes de Porvenir”

03/15/24

13:33:51
*** SCREEN3 MODEL RUN ***
*** VERSION DATED 13043 ***

D:\GIZA Ingenieria\DIAs\CFP_Condominio Fuentes de Porvenir\Emisiones\ADENDA\Mod

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA
EMISSION RATE (G/(S-M**2)) = 0.218000E-07
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 195.0000
LENGTH OF SMALLER SIDE (M) = 94.0000
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

------- ---------- ---- ----- ----- ------ ------ ------10. 0.2620 3 1.0 1.0 30.0 1.00 1.
20. 0.2698 3 1.0 1.0 30.0 1.00 0.

30. 0.2770 3 1.0 1.0 30.0 1.00 0.
40. 0.2838 3 1.0 1.0 30.0 1.00 0.

50. 0.2903 3 1.0 1.0 30.0 1.00 0.
60. 0.2966 3 1.0 1.0 30.0 1.00 0.
70. 0.3026 3 1.0 1.0 30.0 1.00 0.
80. 0.3084 3 1.0 1.0 30.0 1.00 0.

90. 0.3141 3 1.0 1.0 30.0 1.00 0.
100. 0.3185 3 1.0 1.0 30.0 1.00 10.

110. 0.3077 3 1.0 1.0 30.0 1.00 25.
120. 0.2285 3 1.0 1.0 30.0 1.00 24.
130. 0.1878 3 1.0 1.0 30.0 1.00 22.

Informe de modelación de dispersión de contaminantes versión corregida,
_41_
Adenda “Condominios Fuentes de Porvenir”

140. 0.1630 3 1.0 1.0 30.0 1.00 19.
150. 0.1462 3 1.0 1.0 30.0 1.00 17.
200. 0.1080 3 1.0 1.0 30.0 1.00 0.
250. 0.9124E-01 3 1.0 1.0 30.0 1.00 0.
300. 0.7931E-01 3 1.0 1.0 30.0 1.00 0.
350. 0.6992E-01 3 1.0 1.0 30.0 1.00 0.
400. 0.6246E-01 3 1.0 1.0 30.0 1.00 0.
450. 0.5645E-01 3 1.0 1.0 30.0 1.00 0.
500. 0.5152E-01 3 1.0 1.0 30.0 1.00 0.
600. 0.4397E-01 3 1.0 1.0 30.0 1.00 2.
700. 0.3845E-01 3 1.0 1.0 30.0 1.00 0.
800. 0.3427E-01 3 1.0 1.0 30.0 1.00 0.
900. 0.3098E-01 3 1.0 1.0 30.0 1.00 0.
1000. 0.2832E-01 3 1.0 1.0 30.0 1.00 3.
1500. 0.2027E-01 3 1.0 1.0 30.0 1.00 0.
2000. 0.1614E-01 3 1.0 1.0 30.0 1.00 8.
2500. 0.1362E-01 3 1.0 1.0 30.0 1.00 5.
3000. 0.1191E-01 3 1.0 1.0 30.0 1.00 4.
3500. 0.1067E-01 3 1.0 1.0 30.0 1.00 4.
4000. 0.9715E-02 3 1.0 1.0 30.0 1.00 4.
5000. 0.8348E-02 3 1.0 1.0 30.0 1.00 4.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN
PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------SIMPLE TERRAIN 0.3185 100. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

Informe de modelación de dispersión de contaminantes versión corregida,
_42_
Adenda “Condominios Fuentes de Porvenir”

03/15/24

13:43:44
*** SCREEN3 MODEL RUN ***
*** VERSION DATED 13043 ***

D:\GIZA Ingenieria\DIAs\CFP_Condominio Fuentes de Porvenir\Emisiones\ADENDA\Mod

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA
EMISSION RATE (G/(S-M**2)) = 0.142050E-05
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 195.0000
LENGTH OF SMALLER SIDE (M) = 94.0000
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
10. 17.07 3 1.0 1.0 30.0 1.00 1.
20. 17.58 3 1.0 1.0 30.0 1.00 0.
30. 18.05 3 1.0 1.0 30.0 1.00 0.
40. 18.49 3 1.0 1.0 30.0 1.00 0.
50. 18.92 3 1.0 1.0 30.0 1.00 0.
60. 19.33 3 1.0 1.0 30.0 1.00 0.

70. 19.72 3 1.0 1.0 30.0 1.00 0.
80. 20.10 3 1.0 1.0 30.0 1.00 0.

90. 20.47 3 1.0 1.0 30.0 1.00 0.

100. 20.75 3 1.0 1.0 30.0 1.00 10.

110. 20.05 3 1.0 1.0 30.0 1.00 25.
120. 14.89 3 1.0 1.0 30.0 1.00 24.

130. 12.23 3 1.0 1.0 30.0 1.00 22.

Informe de modelación de dispersión de contaminantes versión corregida,
_43_
Adenda “Condominios Fuentes de Porvenir”

140. 10.62 3 1.0 1.0 30.0 1.00 19.
150. 9.528 3 1.0 1.0 30.0 1.00 17.

200. 7.035 3 1.0 1.0 30.0 1.00 0.
250. 5.946 3 1.0 1.0 30.0 1.00 0.
300. 5.168 3 1.0 1.0 30.0 1.00 0.
350. 4.556 3 1.0 1.0 30.0 1.00 0.

400. 4.070 3 1.0 1.0 30.0 1.00 0.
450. 3.678 3 1.0 1.0 30.0 1.00 0.

500. 3.357 3 1.0 1.0 30.0 1.00 0.
600. 2.865 3 1.0 1.0 30.0 1.00 2.
700. 2.506 3 1.0 1.0 30.0 1.00 0.
800. 2.233 3 1.0 1.0 30.0 1.00 0.

900. 2.019 3 1.0 1.0 30.0 1.00 0.
1000. 1.845 3 1.0 1.0 30.0 1.00 3.

1500. 1.321 3 1.0 1.0 30.0 1.00 0.
2000. 1.052 3 1.0 1.0 30.0 1.00 8.
2500. 0.8874 3 1.0 1.0 30.0 1.00 5.
3000. 0.7761 3 1.0 1.0 30.0 1.00 4.
3500. 0.6950 3 1.0 1.0 30.0 1.00 4.
4000. 0.6330 3 1.0 1.0 30.0 1.00 4.

5000. 0.5440 3 1.0 1.0 30.0 1.00 4.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN
PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------SIMPLE TERRAIN 20.75 100. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

Informe de modelación de dispersión de contaminantes versión corregida,
_44_
Adenda “Condominios Fuentes de Porvenir”

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Resumen de emisiones por actividad, Fase de Construcción - año 1**

| Actividades | CO (ton/año) | COV (ton/año) | SOX (ton/año) | NOX (ton/año) | NH3 (ton/año) | MP2,5 Comb<br>(ton/año) | MP10 Comb<br>(ton/año) | MP2,5 Resus<br>(ton/año) | MP10 Resus<br>(ton/año) | MP2,5 Total<br>(ton/año) | MP10 Total<br>(ton/año) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Compactación | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0028 | 0,0054 | 0,0028 | 0,0054 |
| Nivelación | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0005 | 0,0043 | 0,0005 | 0,0043 |
| Escarpe | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0026 | 0,0173 | 0,0026 | 0,0173 |
| Excavación | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0153 | 0,0298 | 0,0153 | 0,0298 |
| Transferencia de material | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0011 | 0,0075 | 0,0011 | 0,0075 |
| Erosión de material en acopio | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0001 | 0,0004 | 0,0001 | 0,0004 |
| Circulación de vehículos en<br>caminos pavimentado<br>(interior) | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,00933 | 0,04161 | 0,00933 | 0,04161 |
| Combustión vehículos | 0,0090 | 0,0013 | 0,0019 | 0,1592 | 0,0003 | 0,0014 | 0,0014 | 0,0000 | 0,0000 | 0,0014 | 0,0014 |
| Combustión maquinaria fuera<br>de ruta | 0,2740 | 0,0256 | 0,0012 | 0,1918 | 0,0000 | 0,0027 | 0,0027 | 0,0000 | 0,0000 | 0,0027 | 0,0027 |
| Grupos electrógenos | 0,0045 | 0,0000 | 0,0014 | 0,0208 | 0,0000 | 0,0015 | 0,0015 | 0,0000 | 0,0000 | 0,0015 | 0,0015 |
| **Emisión total (ton/año)** | **0,2875** | **0,0269** | **0,0045** | **0,3718** | **0,0003** | **0,0056** | **0,0056** | **0,03173** | **0,10631** | **0,03733** | **0,11191** |

**Tabla 2.: Resumen de emisiones por actividad, Fase de Operación - año 1**

| Actividades | CO (ton/año) | COV (ton/año) | SOX (ton/año) | NOX (ton/año) | NH3 (ton/año) | MP2,5 Comb<br>(ton/año) | MP10 Comb<br>(ton/año) | MP2,5 Resus<br>(ton/año) | MP10 Resus<br>(ton/año) | MP2,5 Total<br>(ton/año) | MP10 Total<br>(ton/año) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Circulación de vehículos en<br>caminos pavimentado | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,0000 | 0,01867 | 0,08327 | 0,01867 | 0,08327 |
| Combustión vehículos | 0,00081 | 0,00020 | 0,00002 | 0,00343 | 0,00004 | 0,00003 | 0,00003 | 0,0000 | 0,0000 | 0,00003 | 0,00003 |
| **Emisión total (ton/año)** | **0,00081** | **0,00020** | **0,00002** | **0,00343** | **0,00004** | **0,00003** | **0,00003** | **0,01867** | **0,08327** | **0,01870** | **0,08330** |

**Tabla 3.: Resumen de emisiones- año 1**

| Año | Fase | CO<br>(ton/año) | COV<br>(ton/año) | SOX<br>(ton/año) | NOX<br>(ton/año) | NH3<br>(ton/año) | MP2,5 Comb<br>(ton/año) | MP10 Comb<br>(ton/año) | MP2,5 Resus<br>(ton/año) | MP10 Resus<br>(ton/año) | MP2,5 Total<br>(ton/año) | MP10 Total<br>(ton/año) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Construcción | 0,2875 | 0,0269 | 0,0045 | 0,3718 | 0,0003 | 0,0056 | 0,0056 | 0,03173 | 0,10631 | 0,03733 | 0,11191 |
| 1 | Operación Etapa A-I | 0,00081 | 0,00020 | 0,00002 | 0,00343 | 0,00004 | 0,00003 | 0,00003 | 0,01867 | 0,08327 | 0,01870 | 0,08330 |
| 1 | **Total** | **0,28831** | **0,0271** | **0,00452** | **0,37523** | **0,00034** | **0,00563** | **0,00563** | **0,0504** | **0,18958** | **0,05603** | **0,19521** |

**Tabla 4.: Normas de Calidad del Aire consideradas en el estudio**

| Parámetro | Norma | Estadístico | Limite<br>según<br>Norma | Unidad | Referencia |
| --- | --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio Anual1 | 50 | (g/m3) | D.S. N°12/2022 del MMA<br> |
| MP10 | Primaria | Percentil 98 promedio diario | 130 | (g/m3) | (g/m3) |
| MP2,5 | Primaria | Promedio Anual | 20 | (g/m3) | D.S. N°12/2011 del MMA<br> |
| MP2,5 | Primaria | Percentil 98 promedio diario | 50 | (g/m3) | (g/m3) |
| NO2 | Primaria | Promedio Anual | 100 | (g/m3) | D.S. N°114/ 2002 MINSEGPRES<br> |
| NO2 | Primaria | Percentil 99 máx. 1 hora | 400 | (g/m3) | (g/m3) |
| CO | Primaria | Percentil 99 1 hora | 30 | (mg/m3) | D.S. N°115/2002 del MINSEGPRES<br> |
| CO | Primaria | Percentil 99 8 hora | 10 | (mg/m3) | (mg/m3) |
| SO2 | Primaria | Promedio Anual | 60 | (g/m3) | D.S. N°104/ 2018 MMA<br><br> |
| SO2 | Primaria | Percentil 99 24 horas | 150 | (g/m3) | (g/m3) |
| SO2 | Primaria | Percentil 99 1 hora | 350 | (g/m3) | (g/m3) |
| SO2 (*) | Secundaria | Promedio Anual2 | 260 | (g/m3) | D.S. N°22/2010 MINSEGPRES<br> |
| SO2 (*) | Secundaria | Percentil 98 promedio diario | 60 | (g/m3) | (g/m3) |

**Tabla 5.: Contaminante que constituye la Línea de base de Calidad de aire y ubicación de la Estación de**

| Estación | Coordenadas UTM WGS84 (Huso 19) | Col3 | Contaminante | Periodo | Administrada por |
| --- | --- | --- | --- | --- | --- |
| Estación | Este (m) | Norte (m) | Norte (m) | Norte (m) | Norte (m) |
| Punteras | 674.923 | 5.911.833<br> | MP10 - MP2,5- NO2 - SO2 | 2020-2022 | MMA |

**Tabla 6.: Percentil 98 concentraciones de 24 horas y Promedio anual de concentración de MP 10, periodo**

| Estación | Año | Percentil 98<br>(μg/m3N) | Norma (μg/m3N) | Promedio<br>anual<br>(μg/m3N) | Norma<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Punteras | 2020 | 58 | 130 | 26 | 50 |
| Punteras | 2021 | 70 | 130 | 31 | 50 |
| Punteras | 2022 | 64 | 130 | 30 | 50 |
| Punteras | Promedio Trianual* | Promedio Trianual* | Promedio Trianual* | 29 | 50 |

**Tabla 7.: Resumen de concentraciones de MP 10 (μg/m [3] N)**

| Contaminante | Norma | Estadístico | Estación<br>Punteras | Limite según Norma | Unidad | % de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio Anual1 | 29 | 50 | (g/m3) | 58,4 |
| MP10 | Primaria | Percentil 98 promedio diario - 2020 | 58 | 130 | (g/m3) | 44,6 |
| MP10 | Primaria | Percentil 98 promedio diario - 2021 | <br>70 | 130 | (g/m3) | 53,5 |
| MP10 | Primaria | Percentil 98 promedio diario - 2022 | <br>64 | 130 | (g/m3) | 49,2 |

**Tabla 8.: Percentil 98 concentraciones de 24 horas y Promedio anual de concentración de MP 2,5, periodo**

| Estación | Año | Percentil 98<br>(μg/m3N) | Norma (μg/m3N) | Promedio<br>anual<br>(μg/m3N) | Norma<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Punteras | 2020 | 51 | 50 | 17 | 20 |
| Punteras | 2021 | 57 | 50 | 17 | 20 |
| Punteras | 2022 | 53 | 50 | 16 | 20 |
| Punteras | Promedio Trianual* | Promedio Trianual* | Promedio Trianual* | 17 | 20 |

**Tabla 10.: Percentil 99 concentración de 1 hora y Promedio anual de concentración de NO 2, periodo 20202022, Estación Punteras**

| Estación | Año | Percentil 99<br>(μg/m3N) | Norma (μg/m3N) | Promedio<br>anual<br>(μg/m3N) | Norma<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Punteras | 2020 | 52,4 | 400 | 8,0 | 100 |
| Punteras | 2021 | 50,3 | 400 | 9,1 | 100 |
| Punteras | 2022 | 105,8 | 400 | 9,7 | 100 |
| Punteras | Promedio<br>Trianual* | 69,5 | 400 | 8,9 | 100 |

**Tabla 11.: Resumen de concentraciones de NO 2 (μg/m [3] N)**

| Contaminante | Norma | Estadístico | Estación<br>Punteras | Limite según<br>Norma | Unidad | % de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | Primaria | Promedio Anual1 | 8,9 | 100 | (g/m3) | <br>8,9 |
| NO2 | Primaria | Percentil 99 promedio diario trianual | 69,5 | 400 | (g/m3) | <br>17,4 |

**Tabla 12.: Percentil 99 concentración de 1 hora, Percentil 99 concentraciones de 24 hora y Promedio anual**

| Estación | Año | Percentil<br>99 1 hora<br>(μg/m3N) | Norma<br>(μg/m3N) | Percentil 99<br>24 horas<br>(μg/m3N) | Norma<br>(μg/m3N) | Promedio<br>anual<br>(μg/m3N) | Norma<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Punteras | 2020 | 11,6 | 400 | 3,7 | 150 | 2,0 | 60 |
| Punteras | 2021 | 8,7 | 400 | 2,9 | 150 | 2,0 | 60 |
| Punteras | 2022 | 12,2 | 400 | 3,4 | 150 | 2,0 | 60 |
| Punteras | Promedio<br>Trianual* | 10,8 | 400 | 3,3 | 150 | 2,0 | 60 |

**Tabla 13.: Resumen de concentraciones de SO 2 (μg/m [3] N)**

| Contaminante | Norma | Estadístico | Estación<br>Punteras | Limite según<br>Norma | Unidad | % de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | Primaria | Percentil 99 promedio horario trianual | 10,8 | 350 | (g/m3) | <br>3,1 |
| SO2 | Primaria | Percentil 99 promedio diario trianual | 3,3 | 150 | (g/m3) | <br>2,2 |
| SO2 | Primaria | Promedio Anual1 | 2,0 | 60 | (g/m3) | <br>3,3 |

**Tabla 14.: Tasas de emisiones del Proyecto, Fase construcción y operación**

| Emisiones | CO | SO<br>x | NO<br>X | MP<br>2,5 Total | MP<br>10 Total |
| --- | --- | --- | --- | --- | --- |
| ton/año | 0,2877 | 0,0044 | 0,3687 | 0,0515 | 0,1759 |
| g/m2-s | **0,0000014186** | **0,0000000215** | **0,0000018177** | **0,0000002539** | **0,0000008675** |

**Tabla 15.: Datos de entrada del modelo**

| Parámetro | Datos de entrada | Unidad |
| --- | --- | --- |
| Tipo de fuente | Área | - |
| Altura de liberación | 1,0 | m |
| Longitud de lado largo | 195 | m |
| Longitud de lado corto | 94 | m |
| Altura del receptor | 1,5 | m |
| Terreno Urbano/Rural | Urbano | - |
| Altura de la mezcla | 30 | m |
| Altura anemométrica | 5 | m |
| Clase de estabilidad | 3 | “Inestable” |
| Velocidad eólica | 1,0 | m/s |

**Tabla 16.: Resultados del modelo, Fase de la superposición de la fase de construcción y operación**

| Distancia (m) | Concentración horaria (g/m3) | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO | SO2 | NO2 | MP2,5 Total | MP10 Total |
| 10 | 17,07 | 0,262 | 22,19 | 3,055 | 10,43 |
| 20 | 17,58 | 0,2698 | 22,84 | 3,146 | 10,74 |
| 30 | 18,05 | 0,277 | 23,45 | 3,23 | 11,030 |
| 40 | 18,49 | 0,2838 | 24,03 | 3,309 | 11,300 |
| 50 | 18,92 | 0,2903 | 24,58 | 3,385 | 11,560 |
| 60 | 19,33 | 0,2966 | 25,11 | 3,458 | 11,810 |
| 70 | 19,72 | 0,3026 | 25,62 | 3,529 | 12,050 |
| 80 | 20,1 | 0,3084 | 26,12 | 3,597 | 12,280 |
| 90 | 20,47 | 0,3141 | 26,6 | 3,663 | 12,500 |
| 100 | 20,75 | 0,3185 | 26,97 | 3,714 | 12,680 |
| 110 | 20,05 | 0,3077 | 26,06 | 3,588 | 12,250 |
| 120 | 14,89 | 0,2285 | 19,34 | 2,664 | 9,0,94 |
| 130 | 12,23 | 0,1878 | 15,9 | 2,189 | 7,474 |
| 140 | 10,62 | 0,163 | 13,8 | 1,9 | 6,487 |
| 150 | 9,528 | 0,1462 | 12,38 | 1,705 | 5,821 |
| 200 | 7,035 | 0,108 | 9,141 | 1,259 | 4,297 |
| 250 | 5,946 | 0,09124 | 7,726 | 1,064 | 3,632 |
| 300 | 5,168 | 0,07931 | 6,716 | 0,9248 | 3,157 |
| 350 | 4,556 | 0,06992 | 5,92 | 0,8153 | 2,783 |
| 400 | 4,07 | 0,06246 | 5,289 | 0,7284 | 2,486 |
| 450 | 3,678 | 0,05645 | 4,78 | 0,6582 | 2,247 |
| 500 | 3,357 | 0,05152 | 4,363 | 0,6008 | 2,051 |
| 600 | 2,865 | 0,04397 | 3,723 | 0,5127 | 1,750 |

**Tabla 18.: Factores de conversión para promedios máximos de concentración**

| Tiempo promedio | Factor conversión |
| --- | --- |
| 3 horas | 0,9 |
| 8 horas | 0,7 |
| 24 horas | 0,4 |
| Anual | 0,08 |

**Tabla 19.: Análisis del cumplimiento de la norma de referencia de Calidad de aire, Fase construcción y**

| Parámetro | Estadístico | Máxima del<br>proyecto<br>(g/m3N) | Limite según<br>Norma<br>(g/m3) | Porcentaje<br>respecto de la<br>Norma (%) | Referencia |
| --- | --- | --- | --- | --- | --- |
| MP10 <br> | Concentración 24 horas | 5,1 | 130 | 3,9 | D.S. N°12 / 2022 MMA |
| MP10 <br> | Concentración anual | 1,0 | 50 | 2,0 | 2,0 |
| MP2,5 <br> | Concentración 24 horas | 1,5 | 50 | 3,0 | D.S. N°12/2010 del MMA |
| MP2,5 <br> | Concentración anual | 0,3 | 20 | 1,5 | 1,5 |
| NO2 | Concentración 1 hora | 27,0 | 400 | 6,7 | D.S. N°114/ 2002 MINSEGPRES |
| NO2 | Concentración anual | 2,2 | 100 | 2,2 | 2,2 |
| SO2 <br> | Concentración 1 hora | 0,32 | 350 | 0,091 | D.S. N°104/ 2018 MMA |
| SO2 <br> | Concentración 24 horas | 0,127 | 150 | 0,085 | 0,085 |
| SO2 <br> | Concentración anual | 0,025 | 60 | 0,042 | 0,042 |
| CO | Concentración 1 hora | 20,8 | 30.000 | 0,069 | ~~D~~.S. N°115/2002 del MINSEGPRES |
| CO | Concentración 8 horas | 14,5 | 10.000 | 0,145 | 0,145 |

**Tabla 20.: Concentraciones por distancia de los contaminantes analizados, Fase de construcción y operación**

| Distancia<br>(m) | Concentración (g/m3) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distancia<br>(m) | CO <br>(1 hora) | CO <br>(8 horas) | SO2 <br>(1 hora) | SO2 <br>(24 horas) | SO2 <br>(Anual) | NO2 <br>(1 hora) | NO2 <br>(Anual) | MP2,5 Total<br>(24 horas) | MP2,5 Total<br>(Anual) | MP10 Total<br>(24 horas) | MP10 Total<br>(Anual) |
| 10 | 17,07 | 11,949 | 0,262 | 0,105 | 0,021 | 22,190 | 1,775 | 1,222 | 0,244 | 4,172 | 0,834 |
| 20 | 17,58 | 12,306 | 0,270 | 0,108 | 0,022 | 22,840 | 1,827 | 1,258 | 0,252 | 4,296 | 0,859 |
| 30 | 18,05 | 12,635 | 0,277 | 0,111 | 0,022 | 23,450 | 1,876 | 1,292 | 0,258 | 4,412 | 0,882 |
| 40 | 18,49 | 12,943 | 0,284 | 0,114 | 0,023 | 24,030 | 1,922 | 1,324 | 0,265 | 4,520 | 0,904 |
| 50 | 18,92 | 13,244 | 0,290 | 0,116 | 0,023 | 24,580 | 1,966 | 1,354 | 0,271 | 4,624 | 0,925 |
| 60 | 19,33 | 13,531 | 0,297 | 0,119 | 0,024 | 25,110 | 2,009 | 1,383 | 0,277 | 4,724 | 0,945 |
| 70 | 19,72 | 13,804 | 0,303 | 0,121 | 0,024 | 25,620 | 2,050 | 1,412 | 0,282 | 4,820 | 0,964 |
| 80 | 20,1 | 14,070 | 0,308 | 0,123 | 0,025 | 26,120 | 2,090 | 1,439 | 0,288 | 4,912 | 0,982 |
| 90 | 20,47 | 14,329 | 0,314 | 0,126 | 0,025 | 26,600 | 2,128 | 1,465 | 0,293 | 5,000 | 1,000 |
| 100* | 20,75 | 14,525 | 0,319 | 0,127 | 0,025 | 26,970 | 2,158 | 1,486 | 0,297 | 5,072 | 1,014 |
| 110 | 20,05 | 14,035 | 0,308 | 0,123 | 0,025 | 26,060 | 2,085 | 1,435 | 0,287 | 4,900 | 0,980 |
| 120 | 14,89 | 10,423 | 0,229 | 0,091 | 0,018 | 19,340 | 1,547 | 1,066 | 0,213 | 3,638 | 0,728 |
| 130 | 12,23 | 8,561 | 0,188 | 0,075 | 0,015 | 15,900 | 1,272 | 0,876 | 0,175 | 2,990 | 0,598 |
| 140 | 10,62 | 7,434 | 0,163 | 0,065 | 0,013 | 13,800 | 1,104 | 0,760 | 0,152 | 2,595 | 0,519 |
| 150 | 9,528 | 6,670 | 0,146 | 0,058 | 0,012 | 12,380 | 0,990 | 0,682 | 0,136 | 2,328 | 0,466 |
| 200 | 7,035 | 4,925 | 0,108 | 0,043 | 0,009 | 9,141 | 0,731 | 0,504 | 0,101 | 1,719 | 0,344 |
| 250 | 5,946 | 4,162 | 0,091 | 0,036 | 0,007 | 7,726 | 0,618 | 0,426 | 0,085 | 1,453 | 0,291 |
| 300 | 5,168 | 3,618 | 0,079 | 0,032 | 0,006 | 6,716 | 0,537 | 0,370 | 0,074 | 1,263 | 0,253 |
| 350 | 4,556 | 3,189 | 0,070 | 0,028 | 0,006 | 5,920 | 0,474 | 0,326 | 0,065 | 1,113 | 0,223 |
| 400 | 4,07 | 2,849 | 0,062 | 0,025 | 0,005 | 5,289 | 0,423 | 0,291 | 0,058 | 0,994 | 0,199 |
| 450 | 3,678 | 2,575 | 0,056 | 0,023 | 0,005 | 4,780 | 0,382 | 0,263 | 0,053 | 0,899 | 0,180 |
| 500 | 3,357 | 2,350 | 0,052 | 0,021 | 0,004 | 4,363 | 0,349 | 0,240 | 0,048 | 0,820 | 0,164 |
| 600 | 2,865 | 2,006 | 0,044 | 0,018 | 0,004 | 3,723 | 0,298 | 0,205 | 0,041 | 0,700 | 0,140 |
| 700 | 2,506 | 1,754 | 0,038 | 0,015 | 0,003 | 3,256 | 0,260 | 0,179 | 0,036 | 0,612 | 0,122 |
| 800 | 2,233 | 1,563 | 0,034 | 0,014 | 0,003 | 2,902 | 0,232 | 0,160 | 0,032 | 0,546 | 0,109 |
| 900 | 2,019 | 1,413 | 0,031 | 0,012 | 0,002 | 2,623 | 0,210 | 0,144 | 0,029 | 0,493 | 0,099 |
| 1000 | 1,845 | 1,292 | 0,028 | 0,011 | 0,002 | 2,398 | 0,192 | 0,132 | 0,026 | 0,451 | 0,090 |
| 1500 | 1,321 | 0,925 | 0,020 | 0,008 | 0,002 | 1,717 | 0,137 | 0,095 | 0,019 | 0,323 | 0,065 |
| 2000 | 1,052 | 0,736 | 0,016 | 0,006 | 0,001 | 1,366 | 0,109 | 0,075 | 0,015 | 0,257 | 0,051 |
| 2500 | 0,8874 | 0,621 | 0,014 | 0,005 | 0,001 | 1,153 | 0,092 | 0,064 | 0,013 | 0,217 | 0,043 |

**Tabla 21.: Evaluación de Significancia**

| Col1 | Proyecto | Col3 | Valores de<br>Significancia<br>Tabla 2 | Col5 | Proyecto | Col7 | Valores de<br>Significancia<br>Tabla 2 | Col9 | ¿CUMPLE? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | MP10 Total | MP10 Total | MP10 Total | MP10 Total | MP2,5 Total | MP2,5 Total | MP2,5 Total | MP2,5 Total | MP2,5 Total |
|  | 24<br>horas | Anual | 24<br>horas | Anual | 24<br>horas | Anual | 24<br>horas | Anual | Anual |
| Concentración<br>(μg/m3) | 5,072 | 1,014 | 10,00 | 3,00 | 1,486 | 0,297 | 5,13 | 0,99 | SÍ |
