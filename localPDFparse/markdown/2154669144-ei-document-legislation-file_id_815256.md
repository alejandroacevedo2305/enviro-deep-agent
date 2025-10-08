---
title: Sin título
author: Desconocido
date: D:20210104132153-03'00'
language: es
type: report
pages: 31
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo A
-->

```
3 7 1 03 7 1 2 -

```

```
 3 7 1 03 7 1 2 -

```

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

**Tabla de Contenidos**

**1.** **Introducción .......................................................................................................................................... 3**

**2.** **Objetivo ................................................................................................................................................. 3**

**3.** **Alcances (incluidos y excluidos) ........................................................................................................ 4**

**4.** **Límite de batería ................................................................................................................................... 4**

**5.** **Antecedentes ........................................................................................................................................ 4**

**6.** **Criterios de diseño específicos .......................................................................................................... 5**

**7.** **Bases de cálculo................................................................................................................................... 6**

**8.** **Descripción del Sistema ...................................................................................................................... 6**

**9.** **Análisis Hidráulico ............................................................................................................................... 8**

9.1 Perfiles Hidráulicos ........................................................................................................................ 9
9.2 Verificación de colapso de cañerías ............................................................................................ 11

**10.** **Conclusiones ...................................................................................................................................... 12**

_**Lista de Tablas**_

Tabla 1: Listado de Antecedentes ................................................................................................................ 4

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ## 5. Antecedentes Los antecedentes utilizados son: -->

**Tabla 1: Listado de Antecedentes****

| Col1 | N° Documento | Título |
| --- | --- | --- |
| [Ref.1] | 4400241113-3713-MDCCA-0000400003 | Memoria de Cálculo<br>Cajón RT a PEAD |
| [Ref.2] | 4400241113-0000-CRTPR-00001 | Criterio de Diseño de Procesos<br>Etapa 2 |
| [Ref.3] | 4400241113-0000-CRTCA-00001 | Adenda Criterio de Diseño de<br>Cañerías |
| [Ref.4] | N14CC22-F1-SNCLAV-44200-MDCCA02-<br>3370-004 | Simulación Transiente<br>Tubería de Relave- RT |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- H362274-3712-250-202-0004 Pág. 4 de 12 Memoria de Cálculo -->
<!-- FIN TABLA 1 -->

Tabla 2: Balance de Materiales .................................................................................................................... 6

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- El balance de materiales, así como las características del relaves, considerado para el presente documento es la siguiente: -->

**Tabla 2: Balance de Materiales****

| Parámetro | Unidad | Valores | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| Tonelaje Nominal | [tpd] | 177.300 | 197.000 | 197.000 | 254.194 |
| Tonelaje seco Instantáneo | [tph] | 7.388 | 8.826 | 8.826 | 11.389 |
| Gravedad Específica | [-] | 2,66 | 2,66 | 2,66 | 2,66 |
| Densidad del agua | [kg/m3] | 1,01 | 1,01 | 1,01 | 1,01 |
| Concentración en peso, Cp | [%] | 57 | 55 | 50 | 50 |
| Flujo de Relaves | [m3/s] | 2,30 | 2,91 | 3,35 | 4,32 |
| Flujo de Relaves | [m3/h] | 8.295 | 10.468 | 12.057 | 15.557 |
| Densidad de Relaves | [kg/m3] | 1.562 | 1.533 | 1.464 | 1.464 |
| Viscosidad | [Pa·s] | 0,0162 | 0,0114 | 0,0073 | 0,0073 |
| Tensión de fluencia | [Pa] | 14 | 9 | 2 | 2 |

<!-- Estadísticas: 10 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- ## 8. Descripción del Sistema El transporte de relaves desde la División Radomiro Tomic (RT) se inicia en la descarga de -->
<!-- FIN TABLA 2 -->

Tabla 3: Ubicación estaciones principales. ................................................................................................... 7

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En Tabla 3 se presenta la elevación del Cajón RT y PEAD, mientras que en Figura 2 se presenta el trazado proyectado. -->

**Tabla 3: Ubicación estaciones principales.****

| Estación | Unidad | Valor |
| --- | --- | --- |
| CENTER LÍNEA DESCARGA CAJON RT | [msnm] | 2.601,4 |
| DESCARGA PEAD | [msnm] | 2.559,4 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 2: Trazado Líneas Gravitacionales Cajón RT-PEAD.** H362274-3712-250-202-0004 Pág. 7 de 12 -->
<!-- FIN TABLA 3 -->

Tabla 4: Resumen Escenario Simulado. ....................................................................................................... 8

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- tonelaje solicitado por el diseño por cada línea según [Ref. 1], lo cual corresponde al máximo porteo por dos líneas, lo cual se detalla en Tabla 4. -->

**Tabla 4: Resumen Escenario Simulado.****

| Escenario | Unidad | Valores |
| --- | --- | --- |
| Tonelaje total | [ktpd] | 197 |
| Líneas en operación | [-] | 2 |
| Concentración en peso, Cp | [%] | 50 |
| Flujo por línea | [m3/h] | 5.463 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- El evento transiente analizado corresponde al cierre de válvulas de descarga hacia PEAD durante la operación del relaveducto las cuales se ubican a 5,365 Km aguas abajo del Cajón -->
<!-- FIN TABLA 4 -->

Tabla 5: Celeridades de Onda. ..................................................................................................................... 8

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- RT. Respecto al tiempo de cierre de la válvula de descarga hacia PEAD se consideró 60s. Respecto a las celeridades de la onda, los valores utilizados son presentados en Tabla 5. -->

**Tabla 5: Celeridades de Onda.****

| Escenario | Unidad | Valores | Col4 |
| --- | --- | --- | --- |
| Material | - | HDPE | Acero |
| Diámetro de la Línea | [mm] | 900 | 864 |
| Espesor | [mm] | 53,3 | 22,23 |
| Celeridad | [m/s] | 240 | 1.156 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- H362274-3712-250-202-0004 Pág. 8 de 12 Q -->
<!-- FIN TABLA 5 -->

Tabla 6: Verificación ante presión de colapso. Cañería de Ø900mm y Ø34’’ ............................................ 11

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- externa corresponde a la presión atmosférica. El resumen de dicha comparación se muestra en Tabla 6. -->

**Tabla 6: Verificación ante presión de colapso. Cañería de Ø900m** **m y Ø34’’****

| Parámetro | Unidad | Valores | Col4 |
| --- | --- | --- | --- |
| Diámetro nominal | [in] | 36" | 34" |
| Diámetro exterior | [mm] | 900 | 864 |
| Módulo de Young / Tfluencia | [PSI] | 113.786 | 35.000 |
| Espesor Remanente | [mm] | 33,63 | 12,85 |
| Presión Crítica | [PSI] | 28,38 | 29,73 |
| Presión Atmósférica | [PSI] | 10,7 | 10,7 |
| Factor de Seguridad (F.S.>1,2) | [-] | 2 | 6,0 |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- H362274-3712-250-202-0004 Pág. 11 de 12 Memoria de Cálculo -->
<!-- FIN TABLA 6 -->


_**Lista de Figuras**_

Figura 1: Vista en planta Cajón de Carga ..................................................................................................... 7
Figura 2: Trazado Líneas Gravitacionales Cajón RT-PEAD. ........................................................................ 7
Figura 3: Gradiente Hidráulico Evento Transiente Línea Descarga Cajón RT - PEAD. ............................... 9
Figura 4: Presiones Máximas y Admisibles a lo Largo de Líneas Proyectadas. ........................................ 10

_**Lista de Anexos**_

**Anexo A**

Cálculos Detallados

H362274-3712-250-202-0004
Pág. 2 de 13

Q

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

## 1. Introducción

La Corporación Nacional del Cobre de Chile, CODELCO, a través de la Gerencia de Proyectos

Relaves de la Vicepresidencia de Proyectos (Codelco-VP), ha adjudicado a HATCH el servicio
de “Ingeniería Básica, Sistema de Transporte, Espesamiento y Depositación de Relaves,

Estudio Actualización de F actibilidad” del proyecto Relaves Espesados Talabre (PRET).

El proyecto se localiza en la División Chuquicamata, Región de Antofagasta, provincia de El

Loa, comuna de Calama, a 250 km al Noreste de la ciudad de Antofagasta. El tranque de

relaves Talabre recibe actualmente la totalidad de los relaves generados por las plantas

concentradoras de División Chuquicamata (DCH) y División Ministro Hales (DMH), y en un

futuro de la División Radomiro Tomic (DRT).

En la actualidad el tranque Talabre opera de manera convencional y su vida útil se ha

extendido en el tiempo mediante el peraltamiento de sus muros perimetrales y variadas obras

anexas que le permiten operar los sistemas de relave y agua del distrito norte (DN). Los

análisis realizados durante la prefactibilidad del proyecto permitieron concluir que la solución

técnico económica óptima que resuelve el manejo de los relaves del DN es implementar un

Proyecto de Relaves Espesados en Talabre posterior a la operación de la IX Etapa

convencional.

De acuerdo a los niveles productivos indicados en el PND2020 y a la capacidad de

almacenamiento de la VIII y IX etapa, durante el primer semestre del año 2027 se requiere

iniciar la operación en régimen del Proyecto Relaves Espesados Talabre (PRET) que

representa la solución a largo plazo para la disposición de los relaves del Distrito Norte de

Codelco.

El PRET se encuentra amparado por la Resolución de Calificación Ambiental del año 2016

(RCA 022/2016) en la cual se aprobó la depositación de relaves espesados en Talabre y

variadas obras anexas.

## 2. Objetivo

El objetivo del presente documento es verificar el correcto funcionamiento del sistema de

transporte de relaves convencionales desde Cajón RT hacia PEAD en régimen transiente.

Esta verificación se efectúa para validar la distribución de espesores determinados en análisis

de régimen permanente presentados en el documento 4400241113-3712-MDCCA-00003

correspondiente a la Memoria de Cálculo de líneas gravitacionales desde Cajón RT hacia

PEAD.

Las simulaciones contemplan el cierre de válvula aguas abajo del relaveducto.

H362274-3712-250-202-0004
Pág. 3 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

## 3. Alcances (incluidos y excluidos)

Dentro de los alcances de este documento, se encuentran:

 - Verificación de los espesores remanente de las cañerías;

 - Verificación del Piping Class de líneas gravitacionales desde Cajón RT a PEAD.

Por otro lado, las exclusiones corresponden a:

 - Transito de interfases y/o lavado de línea con agua.

 - Cualquiera no indicado dentro de los alcances del presente documento.

## 4. Límite de batería

El lìmite de batería del presente documento corresponde a:

 - **Aguas Arriba:** Descarga Cajón RT.

 - **Aguas Abajo:** Descarga en Cajón de alimentación de relaves convencionales de la

PEAD.

## 5. Antecedentes

Los antecedentes utilizados son:

**Tabla 1: Listado de Antecedentes**

|Col1|N° Documento|Título|
|---|---|---|
|[Ref.1]|4400241113-3713-MDCCA-0000400003|Memoria de Cálculo<br>Cajón RT a PEAD|
|[Ref.2]|4400241113-0000-CRTPR-00001|Criterio de Diseño de Procesos<br>Etapa 2|
|[Ref.3]|4400241113-0000-CRTCA-00001|Adenda Criterio de Diseño de<br>Cañerías|
|[Ref.4]|N14CC22-F1-SNCLAV-44200-MDCCA02-<br>3370-004|Simulación Transiente<br>Tubería de Relave- RT|

H362274-3712-250-202-0004
Pág. 4 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

## 6. Criterios de diseño específicos

Los códigos de diseño considerados son los siguientes:

 - Acero ASME B31.4-2016. Pipeline Transportation Systems for Liquids and Slurries.

 - HDPE ISO 4427-2:2019 Plastics piping systems - Polyethylene (PE) - Part 2: Pipes.

Para el diseño del sistema de bombeo, se han considerado los siguientes criterios de diseño

hidráulicos:

 - Las características del relave, son aquellas presentadas en el documento - Criterio de

Diseño de Procesos Etapa 2 (Ver [Ref. 2])

 - La celeridad de onda en las cañerías de acero y HDPE fueron determinadas según el

modelo masa virtual Bechteler y Vogel (1982), según lo presentado en Adenda

4400241113-0000-CRTCA- 00001 “Adenda Criterio de Diseño de Cañerías”, aprobada por

Codelco.

 - El escenario evaluado en la presente memoria corresponde al cierre de válvulas a la

llegada en PEAD. Dicha derivación ha sido proyectada para permitir la descarga de

relaves hacia la cola del depósito, a través de una conducción gravitacional, fuera del

alcance de la presente memoria.

 - Para el análisis y estudio de los eventos transientes del sistema, se utilizó el software

Bentley Hammer V8i.

H362274-3712-250-202-0004
Pág. 5 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

## 7. Bases de cálculo

El balance de materiales, así como las características del relaves, considerado para el

presente documento es la siguiente:

**Tabla 2: Balance de Materiales**

|Parámetro|Unidad|Valores|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Tonelaje Nominal|[tpd]|177.300|197.000|197.000|254.194|
|Tonelaje seco Instantáneo|[tph]|7.388|8.826|8.826|11.389|
|Gravedad Específica|[-]|2,66|2,66|2,66|2,66|
|Densidad del agua|[kg/m3]|1,01|1,01|1,01|1,01|
|Concentración en peso, Cp|[%]|57|55|50|50|
|Flujo de Relaves|[m3/s]|2,30|2,91|3,35|4,32|
|Flujo de Relaves|[m3/h]|8.295|10.468|12.057|15.557|
|Densidad de Relaves|[kg/m3]|1.562|1.533|1.464|1.464|
|Viscosidad|[Pa·s]|0,0162|0,0114|0,0073|0,0073|
|Tensión de fluencia|[Pa]|14|9|2|2|

## 8. Descripción del Sistema

El transporte de relaves desde la División Radomiro Tomic (RT) se inicia en la descarga de

relaves, a través una canaleta de hormigón, proyectada por terceros, hacia el Cajón Relave

Convencional RT (3712-CAJ-2001). Desde dicho cajón, se proyecta transportar el relave

convencional hacia PEAD por tres (3) líneas operando en paralelo, la cuales transportan el

relave de forma gravitacional.

Las líneas asociadas a la descarga hacia PEAD constan de tres líneas de un primer tramo de

2,00 km en HDPE PN10 de 900mm de diámetro y un segundo tramo de 3,365 km en acero de
Ø34” hasta la llegada a la PEAD.

En Figura 1 se presenta la distribución de las líneas proyectadas.

H362274-3712-250-202-0004
Pág. 6 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

**Figura 1: Vista en planta Cajón de Carga**

En Tabla 3 se presenta la elevación del Cajón RT y PEAD, mientras que en Figura 2 se

presenta el trazado proyectado.

**Tabla 3: Ubicación estaciones principales.**

|Estación|Unidad|Valor|
|---|---|---|
|CENTER LÍNEA DESCARGA CAJON RT|[msnm]|2.601,4|
|DESCARGA PEAD|[msnm]|2.559,4|

**Figura 2: Trazado Líneas Gravitacionales Cajón RT-PEAD.**

H362274-3712-250-202-0004
Pág. 7 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

## 9. Análisis Hidráulico

Los cálculos fueron realizados tomando en consideración el caso de transporte de mayor

tonelaje solicitado por el diseño por cada línea según [Ref. 1], lo cual corresponde al máximo

porteo por dos líneas, lo cual se detalla en Tabla 4.

**Tabla 4: Resumen Escenario Simulado.**

|Escenario|Unidad|Valores|
|---|---|---|
|Tonelaje total|[ktpd]|197|
|Líneas en operación|[-]|2|
|Concentración en peso, Cp|[%]|50|
|Flujo por línea|[m3/h]|5.463|

El evento transiente analizado corresponde al cierre de válvulas de descarga hacia PEAD

durante la operación del relaveducto las cuales se ubican a 5,365 Km aguas abajo del Cajón

RT. Respecto al tiempo de cierre de la válvula de descarga hacia PEAD se consideró 60s.

Respecto a las celeridades de la onda, los valores utilizados son presentados en Tabla 5.

**Tabla 5: Celeridades de Onda.**

|Escenario|Unidad|Valores|Col4|
|---|---|---|---|
|Material|-|HDPE|Acero|
|Diámetro de la Línea|[mm]|900|864|
|Espesor|[mm]|53,3|22,23|
|Celeridad|[m/s]|240|1.156|

H362274-3712-250-202-0004
Pág. 8 de 12

Q

Q

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

**9.1** **Perfiles Hidráulicos**

En la Figura 3 se presenta el gradiente hidráulico asociado al evento transiente analizado,

mientras que en Figura 4 se presentan las presiones máximas a lo largo de la línea proyectada.

**Figura 3: Gradiente Hidráulico Evento Transiente Línea Descarga Cajón RT - PEAD.**

H362274-3712-250-202-0004
Pág. 9 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

**Figura 4: Presiones Máximas y Admisibles a lo Largo de Líneas Proyectadas.**

A partir de lo obtenido en Figura 2, se observa que la envolvente de presiones máximas es

menor a la presión admisible al año 20 de operación. Por otro lado, no existen subpresiones

producto del evento transiente a lo largo del trazado. Respecto a lo presentado en Figura 3,

se verifica que el sistema opera bajo la clase ASME #150.

H362274-3712-250-202-0004
Pág. 10 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

**9.2** **Verificación de colapso de cañerías**

Ante un eventual corte de columna en la cañéria producto de un transiente, o como parte de

las maniobras de drenaje, se verificó la resistencia de la cañería antes presiones externas.

Considerando que éstas cañerías serán instaladas en superficie, con camellones, la presión

externa corresponde a la presión atmosférica. El resumen de dicha comparación se muestra

en Tabla 6.

**Tabla 6: Verificación ante presión de colapso. Cañería de Ø900m** **m y Ø34’’**

|Parámetro|Unidad|Valores|Col4|
|---|---|---|---|
|Diámetro nominal|[in]|36"|34"|
|Diámetro exterior|[mm]|900|864|
|Módulo de Young / Tfluencia|[PSI]|113.786|35.000|
|Espesor Remanente|[mm]|33,63|12,85|
|Presión Crítica|[PSI]|28,38|29,73|
|Presión Atmósférica|[PSI]|10,7|10,7|
|Factor de Seguridad (F.S.>1,2)|[-]|2|6,0|

H362274-3712-250-202-0004
Pág. 11 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES
/ CANALETAS - TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

## 10. Conclusiones

Los resultados del presente documento son:

 - En función del análisis desarrollado, se validan los espesores de las líneas

proyectadas, así como la clase de los flanges de acuerdo a la Memoria de Cálculo de

Líneas Gravitacionales Cajón RT a PEAD [Ref. 1].

 - En particular, el transporte de los relaves convencionales desde Cajón RT desde las

líneas proyectadas, se considera el uso de tres líneas paralelas que constan de un

primer tramo en HDPE PN10 de 900mm (2,00 km) y otro de acero carbono API 5L
grado B de Ø34” de diámetro nominal, con un espesor de 22,23mm sin revestimiento

(3,365 km).

 - Se valida la clase ASME 150 para el sistema gravitacional desde el inicio del trazado

hasta la llegada a PEAD.

H362274-3712-250-202-0004
Pág. 12 de 12

Memoria de Cálculo

Contrato N°4400241113
3710 - EMBALSES / TRANQUES - 3712 - SISTEMA DE CAPTACIÓN DE RELAVES / CANALETAS
TRANSIENTES EN LÍNEAS GRAVITACIONALES CAJÓN RT-PEAD

4400241113-3712-MDCCA-00004, Rev. Q
17-12-2020

# Anexo A

## Cálculos Detallados

(18 páginas)

H362274-3712-250-202-0004

Transient Calculation Summary: Base

Transient Calculation Summary

Time Step 0,050000 sec Specific Gravity 1,533
Number of Time Steps 10000 Wave Speed (Global) (N/A) m/s
Total Simulated Time 500,0 sec Vapor Pressure -76,96 m H2O
Number of Nodes 274 Number of Report Paths 1
Number of Pipes 273

**Transient Initial Conditions Summary**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 1 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base
**Transient Initial Conditions Summary**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 2 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base
**Transient Initial Conditions Summary**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 3 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base
**Transient Initial Conditions Summary**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 4 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base
**Transient Initial Conditions Summary**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 5 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base
**Transient Initial Conditions Summary**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 6 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base
**Transient Initial Conditions Summary**

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 7 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 8 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 9 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 10 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 11 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 12 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 13 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 14 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 15 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 16 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 17 of 18
Watertown, CT 06795 USA +1-203-755-1666

Transient Calculation Summary: Base

**Extreme Pressures and Heads**

Bentley HAMMER V8i (SELECTseries 6)

Bentley Systems, Inc. Haestad Methods Solution Bentley HAMMER V8i (SELECTseries 6)

Center [08.11.06.113]

RT2.wtg Center

17-11-2020 27 Siemon Company Drive Suite 200 W Page 18 of 18
Watertown, CT 06795 USA +1-203-755-1666