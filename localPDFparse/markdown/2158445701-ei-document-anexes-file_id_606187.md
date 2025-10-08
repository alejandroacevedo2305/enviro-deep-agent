---
title: Microsoft Word - Estudio de Modelación  de Olor_Proyecto BCC Lampa v01022023.docx
author: Desconocido
date: D:20230202162411Z00'00'
language: es
type: report
pages: 37
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - BCC S.A.
-->

|Col1|BCC S.A.|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Febrero 2023|V-3|V-3||1 de 37|

## ESTUDIO DE MODELACIÓN DE DISPERSIÓN DE OLOR, PROYECTO « PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS ETAPAS 3»

Preparado para

# BCC S.A.

**Febrero de 2023**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||ii de 37|

TABLA DE CONTENIDO

LISTA DE TABLAS _______________________________________________________ 2

LISTA DE FIGURAS ______________________________________________________ 3

1. GLOSARIO, SIGLAS Y UNIDADES ______________________________________ 4

2. CONTEXTO ________________________________________________________ 6

3. METODOLOGÍA ____________________________________________________ 7

4. MODELO DE DISPERSIÓN DEL OLOR ___________________________________ 7

5. TOPOGRAFÍA ______________________________________________________ 7

6. METEOROLOGÍA __________________________________________________ 10

7. CONFIGURACIÓN DE LA MALLA DE RECEPTORES _______________________ 14

8. RECEPTORES DISCRETOS ____________________________________________ 14

9. MÉTODO DE EVALUACIÓN DEL IMPACTO DE OLOR _____________________ 17

10. DESCRIPCIÓN DE LAS FUENTES Y ESCENARIOS DE MODELACIÓN __________ 19

11. RESULTADOS DE LA MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA _________ 26

12. CONCLUSIONES ___________________________________________________ 29

13. BIBLIOGRAFÍA _____________________________________________________ 30

## LISTA DE TABLAS

**Tabla 1 Detalle de proyección cartográfica y coordenadas Archivos WRF ............ 10**

**Tabla 2 Sesgo, Error Cuadrático Medio y Coeficiente de Correlación - Información**

**Estación El Oasis vs Información Modelo WRF .......................................... 13**

**Tabla 3: Características de los receptores discretos ................................................ 15**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---| ||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**| |**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**| |BCC_2022|Diciembre 2022|V-3|V-3||15 de<br>37| -->

**Tabla 3: Características de los receptores discretos****

| Recept<br>or | Localización<br>UTM<br>WGS84, 19H | Col3 | Altura<br>m.s.n.<br>m | Distancia<br>al límite de<br>la<br>propiedad* | Descripción |
| --- | --- | --- | --- | --- | --- |
| <br> <br>**Recept**<br>**or** | **X [m]** | **Y [m]** | **H **<br>**[m]** | **L [m]** | **L [m]** |
| 1 | 333 337 | 6 311 513 | 482 | 1 820 | Primer Vecino norte (N) |
| 2 | 337082 | 6 312 251 | 482 | 2 350 | Primer Vecino noreste (NE) |
| 3 | 335 217 | 6 310 105 | 482 | 2 180 | Primer Vecino este-noreste (ENE) |
| 4 | 335 881 | 6 309 492 | 482 | 2 780 | Primer Vecino este-sureste (ESE) |
| 5 | 335 029 | 6 308 332 | 481 | 2 280 | Primer Vecino sur (S) |
| 6 | 333 858 | 6 309 370 | 480 | 270 | Primer Vecino sur-suroeste (SSO) |
| 7 | 332 358 | 6 310 188 | 480 | 800 | Primer Vecino noroeste (NO) |
| 8 | 333 350 | 6 309 551 | 480 | 250 | Primer Vecino Proyectado este<br>(E) |
| 9 | 333 356 | 6 309 895 | 480 | 320 | Primer Vecino Proyectado<br>noreste (NE) |
| 10 | 333 181 | 6 310 474 | 480 | 760 | Primer Vecino Proyectado Norte<br>(N) |

<!-- Estadísticas: 11 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- En la siguiente Figura se muestra el receptor discreto incluido en el estudio. |Col1|BCC S.A|Col3|Col4|Col5|Col6| |---|---|---|---|---|---| -->
<!-- FIN TABLA 3 -->


**Tabla 4: Criterios de Calidad de Olor a Nivel Internacional .................................... 18**

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- impacto de olor generado por Plantas de Tratamiento de Aguas Servidas, indica criterios de calidad que varían entre 5 y 10 u.o/m3. Estos valores se especifican en la Tabla 4. -->

**Tabla 4: Criterios de Calidad de Olor a Nivel Internacional****

| ESTADO Ó<br>CIUDAD-PAÍS | LÍMITE | TIEMPO | FRECUENCIA<br>% | USO DE<br>SUELO | TIPO DE<br>FUENTE | REFERENCIA |
| --- | --- | --- | --- | --- | --- | --- |
| <br>UK<br> | 5 OU/m3<br> | <br>- <br> | <br>98%<br> | <br>- <br> | <br>PTAS<br> | <br>Mahin (2001)<br> |

<!-- Estadísticas: 1 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: ECOTEC (2013), “Antecedentes para la Regulación de Olores en Chile”, realizado para la_ _Subsecretaría del Medio Ambiente, Santiago de Chile, agosto._ De esta forma se mantiene la norma de referencia bajo la cual fue extendida la -->
<!-- FIN TABLA 4 -->


|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||3 de 37|

**Tabla 5: Fuentes consideradas en Proyecto .............................................................. 19**

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 5 se especifican las condiciones de funcionamiento de cada fuente en el escenario de modelación propuesto, indicando si las mismas son generadora de gases odoríficos para ser consideradas en la modelación. -->

**Tabla 5: Fuentes consideradas en Proyecto****

| Escen<br>ario | No | Fuente | Descripción | Incluida en<br>la<br>modelación | Comentario |
| --- | --- | --- | --- | --- | --- |
| Actual | 1 | Sedimentador I | Unidad abierta | Si |  |
| Actual | 2 | Cámara de distribución<br>I | Unidad abierta | Si |  |
| Actual | 3 | Digestor I | Unidad abierta | Si | Esta unidad no<br>operará en el<br>Escenario<br>Proyectado |
| Actual | 4 | Espesador de lodos I | Unidad abierta | Si |  |
| Actual | 5 | Reactores (2) I | Unidades<br>abiertas | Si |  |
| Actual | 6 | Contenedor de lodos<br>I | Unidad abierta | Si | Esta unidad no<br>operará en el<br>Escenario<br>Proyectado |
| Actual | 7 | Ventana (Galpón de<br>deshidratado de<br>lodo<br>I) | Abertura en el<br>edificio | Si | Esta unidad no<br>operará en el<br>Escenario<br>Proyectado |
| Actual | 8 | Reactor biológico<br>II | Unidad abierta | Si |  |
| Actual | 9 | Sedimentadores (2) II | Unidades<br>abiertas | Si |  |
| Actual | 10 | Cámara repartidora de flujo<br>#1 II | Unidad abierta | Si |  |
| Actual | 11 | Cámara de<br>contacto II | Unidad abierta | Si |  |
| Actual | 12 | Cámara medición de<br>caudal efluente y<br>repartidora de caudal #3<br>II | Unidad abierta | <br>Si |  |

<!-- Estadísticas: 12 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- |Col1|BCC S.A|Col3|Col4|Col5|Col6| |---|---|---|---|---|---| ||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**| |**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**| -->
<!-- FIN TABLA 5 -->


**Tabla 6 : Características de las fuentes a modelar ................................................... 22**

_**Tabla 7: Resultados de concentración de olor y frecuencia de exceso en los**_

_**receptores discretos - Escenario Actual.**_ **.................................................... 27**

_**Tabla 8: Resultados de concentración de olor y frecuencia de exceso en los**_

_**receptores discretos - Escenario Proyectado.**_ **........................................... 28**

## LISTA DE FIGURAS

Figura 1: Topografía del área a modelar ..................................................................... 9

Figura 2 Rosa de Vientos periodo de modelación. .................................................. 11

Figura 3: Límite de propiedad y receptores discretos .............................................. 16

Figura 4: Fuentes - Escenario Actual .......................................................................... 24

Figura 5: Fuentes - Escenario Proyectado ................................................................. 25

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||4 de 37|

## 1. GLOSARIO, SIGLAS Y UNIDADES

Análisis Olfatométrico Técnica de cuantificación de olor o medida de

concentración de olor.

ASTM _American Society for Testing and Materials_ / Sociedad
Americana para la prueba de Materiales.

CEN _Comité_ _européen_ _de_ _normalisation_ /European
Committee for Standardization / Comité Europeo de
Normalización.

Concentración de

Olor

Condiciones

Normales

Número de unidades de olor en 1 m [3] de gas, o número
de diluciones (con aire) necesarias para obtener por
parte del panel de los jurados, la situación en que el 50%
de ellos percibe (u.o./m [3] ).

Condiciones normales de temperatura y presión:
P=101,3 kPa (1 atm, 14,696 psi) and T=293°K (20°C).

C P98 Las concentraciones calculadas en este punto son
inferiores al valor determinado por la modelación y 2%
de los valores de concentración calculados son
superiores (175 horas/ acumuladas en un año).

EN _European Standard_ / Norma Europea.

Fuente [1] puntual Fuente estacionaria discreta, de emisión de gases a la
atmósfera a través de conductos, de dimensión y
caudal de aire definidos. (Por ejemplo: chimeneas,
venteos, otros).

Fuentes difusas Fuentes con dimensiones definidas (mayoritariamente
fuentes superficiales) que no tienen flujo de gas residual
definido.

Fuentes difusas

activas

Fuentes difusas
pasivas

Fuentes difusas con aireación forzada. (Por ejemplo:
biofiltros, piscina de aireación extendida, otros).

Fuentes difusas sin aireación forzada. (Por ejemplo: pilas
de lodos, estanques de sedimentación, otros).

Fuentes fugitivas Fuentes esquivas o de difícil identificación que liberan
cantidades indefinidas de sustancias olorosas. (Por

1 Definiciones de Fuentes puntuales, difusas, difusas activas, difusas pasivas y fuentes fugitivas han sido de
acuerdo a lo descrito en la NCh 3190.Of 2010.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||5 de 37|

ejemplo: fugas de válvulas y juntas, aperturas de
ventilación pasiva, otros).

H Hora.

Molestia Efecto acumulativo de episodios de olor, los cuales
superan el nivel de tolerancia de las personas
expuestas. Son cuatro los elementos que deben ser
considerados durante el análisis para determinar la
molestia a causa de un olor: concentración de olor,
frecuencia, duración y tono hedónico.

Nm [3] Volumen en un m [3] a temperatura y presión normalizada
(P=101,3 kPa and T=293K).

SEA Servicio de Evaluación Ambiental

SEIA Sistema de Evaluación Impacto Ambiental

Situación

conservadora

Estimación del impacto de olores con las tasas de
emisión máximas.

u.o./m [3] Unidades de olor por metro cúbico de aire. Unidad de
Medida. 1 u.o./m [3] corresponde al nivel en que el 50% de
la población es capaz de comenzar a detectar un olor,
en un ambiente libre de olor.

u.o./m [2] /s Unidad de olor por metro cuadrado por segundo. Tasa
de emisión de olor por unidad de superficie. (Aplica
para fuentes superficiales).

Área de influencia

por olores

Con relación a la determinación del Área de Influencia,
esta se define a partir de la dispersión de la pluma
odorante ( sección 4.4 Guía para la predicción y
evaluación de impactos por olor en el SEIA).

Es usual circunscribir el AI al espacio contenido por la
isodora de 1 OUE, que corresponde al umbral de
detección del olor compuesto. En el caso de un olor
simple el umbral de detección se asocia a una
determinada concentración de la sustancia olorosa en
la que se percibe el olor de dicha sustancia (μg/m3,
ppm o ppb) (ver sección 2.3 de Guía para la predicción
y evaluación de impactos por olor en el SEIA).

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||6 de 37|

## 2. CONTEXTO

Desarrollar un estudio de la dispersión de los olores de las fuentes odoríficas de las
Instalaciones del Proyecto “ Planta de Tratamiento de Aguas Servidas Etapas 3”
de BCC S.A., en adelante PTAS, ubicada en la comuna de Lampa, Provincia de
Chacabuco, Región Metropolitana.

Este informe presenta los parámetros de modelación de la dispersión de los olores
de las Instalaciones de la PTAS para el Escenario Actual y Proyectado de
Modelación, en la que se consideraran los siguientes procesos:

 - Escenario Actual

`o` Planta de Tratamiento I

`o` Planta de Tratamiento II

`o` Tratamiento Preliminar Existente

`o` Sala de Deshidratado de Lodos

`o` Cámara de Contacto

 Escenario Proyectado

`o` Planta de Tratamiento III

§
Cámara de Reja Mecánica

§ Planta Elevadora Cabecera

§ Tratamiento Preliminar

§ Reactor

§ PE RAS-WAS

§ Espesador Lodos

§ Digestor Lodos

§
Galpón Deshidratado

§
Galpón Acopio

Las fuentes anteriormente señaladas serán caracterizadas a partir de los
resultados de la campaña de muestreo y análisis Olfatométrico realizado en las
actuales unidades de la PTAS realizada en el mes de Agosto de 2022, en caso
que sea necesario se utilizarán factores de emisión, utilizando como fuente
principal para la recopilación de estos el Informe Final Servicio de Recopilación y

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||7 de 37|

Sistematización de Factores de Emisión al Aire para el SEA, complementando
dicha información con documentos relacionados que serán citados
particularmente en cada caso (como por ejemplo procesos de evaluación
ambiental anteriores para la misma PTAS).

El presente informe presenta los datos de configuración y resultados del modelo
de dispersión de olor para la evaluación de la influencia de olores del Proyecto.

## 3. METODOLOGÍA

En las siguientes secciones de este informe se describen los elementos principales
utilizados para realizar el presente Estudio de modelación de dispersión de olor,
cabe señalar que para el desarrollo del presente estudio se han considerado los
criterios principales establecidos en la Guía para el uso de modelos de calidad
del aire en el SEIA y la Guía para la predicción y evaluación de impactos por olor

en el SEIA.

## 4. MODELO DE DISPERSIÓN DEL OLOR

Para el presente estudio, la dispersión de olores fue modelada con CALPUFF-View
(versión actualizada de _Lakes Environmental_ 8.5 y versión 5.8.5 aprobada de la
US-EPA). Calpuff es un modelo utilizado para la modelación de dispersión
atmosférica, el cual fue desarrollado por la Agencia Estadounidense de
Protección Ambiental (US-EPA) para predecir los impactos atmosféricos.
Adicionalmente, es uno de los modelos recomendado por la Guía para el uso de
modelos de calidad del aire en el SEIA (SEA, 2012), siendo una combinación del
modelo Gaussiano y el modelo Lagrangeano, en el sentido de que
esencialmente calculan la dispersión de contaminantes provenientes de una
emisión instantánea, llamada “puff”, a lo largo de una trayectoria.

## 5. TOPOGRAFÍA

El Estudio de Modelación de Dispersión de olor se realizará en un área 10 km x 10
km teniendo como centro la Planta de Tratamiento de Aguas Servidas. Las
coordenadas geográficas centrales son X 333.050 km, Y 6.309.650 km (UTM WGS84, zona 19S). La Figura 1 presenta el dominio de la información meteorológica

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||8 de 37|

(un área de 50 km x 50 km) cubierta con una grilla meteorológica (la resolución
de la grilla es de 1 km x 1 km). El lugar de emplazamiento de la PTAS es
identificado con un punto rojo en la misma figura.

Las elevaciones del terreno del área a modelar pueden presentar un alto
impacto en la dispersión de olores, cuando existen desnivelaciones de más de 10
m se estima el terreno como accidentado y las desnivelaciones serán tomadas
en consideración para la modelación. En el presente estudio, la elevación del
terreno varía entre 174 y 2.392 metros sobre el nivel del mar, en particular el área

en donde se emplaza el Proyecto se encuentra entre alrededor de los 400 y 500

metros sobre el nivel del mar, en consecuencia, se tuvieron en cuenta las

elevaciones del terreno para la modelación. La información de topografía
utilizada será obtenida a través de la interfaz de _Lakes Environmental_ y se basa
en los datos de la misión de topografía _Shuttle Radar Topography Mission_ (SRTM1).
Estos datos son utilizados por TERREL para calcular la altura del terreno de cada
una de las fuentes de emisión y de los receptores para su uso en el modelo.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||9 de 37|

**Figura 1: Topografía del área a modelar**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||10 de<br>37|

## 6. METEOROLOGÍA

El Estudio de modelación de dispersión de olores, se realizó en base a un (01) año
de data meteorológica (periodo del 01/01/2021 al 01/01/2022) representativa del
área de estudio dentro de una grilla de modelación de 50 x 50 km. Esta data fue
obtenida a partir del modelo de pronóstico meteorológico WRF [2] . En la siguiente
tabla se presenta un resumen de los principales parámetros de la configuración

del modelo WRF.

**Tabla 1 Detalle de proyección cartográfica y coordenadas Archivos WRF**

|Proyección Cartográfica|Cónica Conforme de Lambert (LCC)|
|---|---|
|Período|1 Ene 2021 00:00 - 1 Ene 2022 00:00|
|Origen|RLAT0 = 33.340S<br>RLAN0 = 70.794W|
|DATUM|NWS-84 6370 km Radius, Global Sphere|
|Grilla|50 x 50 km|
|Resolución Espacial|1 x 1 km|
|Celdas verticals|10|

Para evaluar el comportamiento del modelo meteorológico de pronóstico se ha
considerado el uso de información pública, en este caso de la estación El Oasis
que se encuentra ubicada en la comuna de Lampa a 6,5 km al noroeste de la
ubicación del Proyecto, y que cuenta con información disponible en el sitio de
AGROMET, dependiente del Ministerio de Agricultura.

Para realizar el análisis cualitativo se han considerado los registros horarios para el
año 2021 en ambas fuentes de información, cabe señalar que el modelo de
pronóstico cuenta con un 100% de registros para el periodo mientras que para la
estación observada se cuenta con sobre un 98% de los registros, siendo la perdida
de información poco significativa.

2 El modelo numérico recomendado para la generación de datos meteorológicos es el _Weather Research_
_Forecasting Model_ (WRF). WRF es uno de los modelos meteorológicos de pronóstico más avanzados y
completos, y mantenido por NCAR/NOAA ( _National Center for Atmospheric Research/National Oceanic and_
_Atmospheric Administration_ ) de Estados Unidos (SEA, 2012). Este modelo de pronóstico numérico es utilizado
a nivel global y se encuentra en continuo desarrollo. Una de las ventajas más significativas se manifiesta en la
parametrización física configurada para el territorio Chileno, que entre otras cosas permite otorgar una
resolución horizontal de la grilla meteorológica de 1km.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||11 de<br>37|

En la siguiente figura se puede ver la comparación de las rosas de viento, en
donde se aprecia que la dirección de viento se encuentra bien representada, y
de acuerdo con las intensidades se ve que el modelo de pronóstico sobreestima
levemente las intensidades de los campos de viento.

|Modelo de Pronostico<br>Año 2021|Datos Observados<br>Año 2021|
|---|---|
|||

**Figura 2 Rosa de Vientos periodo de modelación.**

Para la realización del análisis cuantitativo se han considerado las siguientes
medidas de error estadístico, a saber:

Sesgo: que representa la tendencia del modelo de pronóstico WRF a sobreestimar
o subestimar las condiciones reales. Los resultados a obtener se comparan con
respecto a si son negativos o positivos, en el primer caso se interpreta como que
el modelo subestima el valor de las variables modeladas y viceversa. La fórmula
para el cálculo del sesgo es la siguiente:

"

Sesgo= [1]

N [*(M] [!] [ −O] [!] [)]

!#$

Donde:

N: Tamaño de la muestra

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||12 de<br>37|

M: Valor del Modelo de Pronostico

O: Valor Observado en la Estación de Superficie

Error Cuadrático Medio (ECM): este valor entrega la diferencia promedio entre
los valores promedios del modelo de pronóstico y observados en la estación
superficial. La fórmula para el cálculo del error cuadrático medio es la siguiente:

"

ECM=

!#$

~~2~~

"

(M ! −O ! ) [%]

N

!#$

Donde:

N: Tamaño de la muestra

M: Valor del Modelo de Pronostico

O: Valor Observado en la Estación de Superficie

Coeficiente de Correlación (r): a partir de este coeficiente se mide la relación
lineal entre la variable generada por el modelo de pronóstico y la variable
observada en la estación de superficie. El resultado de este coeficiente se
encuentra en el intervalo [-1, 1]. El resultado ideal es 1, considerando este como
la mejor capacidad del modelo para representar las condiciones generadas. La
fórmula para el cálculo del coeficiente de correlación es la siguiente:

"

r= [1]

N [ *]

!#$

(M ! −M [4] )(O ! −O [5] )

σ & σ '

Donde:

N: Tamaño de la muestra

M: Valor del Modelo de Pronostico

O: Valor Observado en la Estación de Superficie

σ: Desviación Estándar

En base a la fórmula para cada estadístico presentado anteriormente, en la
siguiente tabla se presentan los valores obtenidos para la comparación entre los
datos del modelo de pronóstico WRF y los datos observados en la estación el

Oasis.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||13 de<br>37|

**Tabla 2 Sesgo, Error Cuadrático Medio y Coeficiente de Correlación - Información**

**Estación El Oasis vs Información Modelo WRF**

|Información|Estación|Sesgo|Error<br>Cuadrático<br>Medio|Coeficiente<br>de Correlación|
|---|---|---|---|---|
|Observada|El Oasis|0,42|1,89|-0,01|
|Modelo<br>Pronóstico|Archivo<br>WRF|Archivo<br>WRF|Archivo<br>WRF|Archivo<br>WRF|

Con respecto al análisis de los estadísticos de error analizados, es posible señalar
en primer lugar, que este complementa la información presentada en la Tabla 2,

es decir se manifiesta una leve sobreestimación del modelo sobre las velocidades

de viento en el área de modelación de acuerdo con los resultados del cálculo

del sesgo. Asociado a lo anterior el Error Cuadrático Medio complementa dicha
información y de acuerdo con lo que es posible apreciar del cálculo de
velocidad promedio de ambas fuentes de información es posible señalar que el
modelo aumenta levemente las velocidades promedio de los datos observados.

Considerando todo lo anterior se establece, que a pesar de la sobrestimación
presente en los campos de viento, toda vez que existen barreras naturales que
no son posible incluir en la modelación, se establece que no es necesario el uso
de factores de corrección, ya que la evaluación se ha realizado en el peor
escenario posible.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||14 de<br>37|

## 7. CONFIGURACIÓN DE LA MALLA DE RECEPTORES

Un receptor es un punto en el cual el modelo calcula las concentraciones de olor.
Una malla de receptores es un grupo de receptores configurados a diferentes
distancias de la fuente de olores. La malla de receptores se ha configurado
dentro de un radio de 15 km alrededor del Proyecto, de esta forma es posible
abarcar el entorno directo de la misma y otros sectores en la comuna de Lampa
y alrededores, presentando distancias variables entre cada receptor (cuando su
posición es más alejada de la fuente, la distancia entre receptores aumenta).
Para el presente estudio la distancia entre los receptores de la malla variará entre
20 y 500 m, mientras que la distancia entre el receptor discreto y el Proyecto se
sitúan entre 270 y 2780 m, siendo la Población más cercana al Proyecto. Todos los
receptores se fijaron a una altura de 1,5 m, que corresponde a la altura media de

la nariz humana

## 8. RECEPTORES DISCRETOS

Para reflejar más eficientemente los posibles impactos provocados por los olores,
se han agregado receptores discretos a la malla de receptores. Estos receptores
se encuentran ubicados en las primeras residencias del sector poblado más
próximo al sitio.

Al igual que los receptores de la malla, los receptores discretos se fijaron a una
altura de 1,5 m del suelo. En total, diez (10) receptores discretos situado entre 270
a 2 780 de los límites del terreno de la PTAS Santo Tomás han sido agregados para
el presente estudio. Cabe señalar que, de los 10 receptores discretos, los
identificados del 1 al 7 corresponden a receptores actualmente existentes en el
entorno del proyecto, mientras que los receptores identificados del 7 al 10 se
presentan receptores correspondientes a áreas proyectadas de acuerdo con la
zonificación planificada para el entorno de la PTAS Santo Tomás.

La Tabla 3 presentan los receptores discretos definidos para el actual estudio. En
la Figura 3, los receptores están representados con una cruz.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||15 de<br>37|

**Tabla 3: Características de los receptores discretos**

|Recept<br>or|Localización<br>UTM<br>WGS84, 19H|Col3|Altura<br>m.s.n.<br>m|Distancia<br>al límite de<br>la<br>propiedad*|Descripción|
|---|---|---|---|---|---|
|<br> <br>**Recept**<br>**or**|**X [m]**|**Y [m]**|**H **<br>**[m]**|**L [m]**|**L [m]**|
|1|333 337|6 311 513|482|1 820|Primer Vecino norte (N)|
|2|337082|6 312 251|482|2 350|Primer Vecino noreste (NE)|
|3|335 217|6 310 105|482|2 180|Primer Vecino este-noreste (ENE)|
|4|335 881|6 309 492|482|2 780|Primer Vecino este-sureste (ESE)|
|5|335 029|6 308 332|481|2 280|Primer Vecino sur (S)|
|6|333 858|6 309 370|480|270|Primer Vecino sur-suroeste (SSO)|
|7|332 358|6 310 188|480|800|Primer Vecino noroeste (NO)|
|8|333 350|6 309 551|480|250|Primer Vecino Proyectado este<br>(E)|
|9|333 356|6 309 895|480|320|Primer Vecino Proyectado<br>noreste (NE)|
|10|333 181|6 310 474|480|760|Primer Vecino Proyectado Norte<br>(N)|

En la siguiente Figura se muestra el receptor discreto incluido en el estudio.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||16 de<br>37|

PTAS Santo Tomas

**Figura 3: Límite de propiedad y receptores discretos**

( _zoom_ del dominio de modelación)

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||17 de<br>37|

## 9. MÉTODO DE EVALUACIÓN DEL IMPACTO DE OLOR

Los resultados de la modelación de dispersión de olores permiten cuantificar las
molestias causadas por los olores. La escala de percepción y concentración de
olores generalmente aceptada se resume de la siguiente forma:

50% de la población puede comenzar a percibir un
1 u.o./m [3] :
olor

50% de la población puede reconocer o comenzar a
2-3 u.o./m [3 ] :
reconocer un olor

El olor es calificable y puede comenzar a recibirse
5 u.o./m [3 ] :
quejas (puede ser identificado)

Los olores son reconocibles y se pueden recibir
10 u.o./m [3] :
reclamos.

Es importante matizar el límite que se debe alcanzar para que exista una queja,
ya que éstas dependen también de la intensidad de los olores percibidos, de su
agresividad, de su apreciación y de su frecuencia. En consecuencia, la
sensibilidad individual hacia los olores tiene una influencia importante en la
presentación de quejas.

Varias jurisdicciones alrededor del mundo han implementado con éxito
programas de gestión de olores. Por ejemplo: en Alemania, en la región sur de
Australia, en los Países Bajos y en el estado de California de EE.UU; entre muchos
otros. Estos programas proponen criterios de percepción de olor que oscilan entre
1 y 10 u.o./m3 (RWDI, 2005).

En el marco del presente estudio, la concentración del percentil 98 será utilizado
para evaluar el nivel de olor de las zonas de ocupación humana de los bordes

del terreno del sitio sobre el cual se realiza el estudio. Por definición, la

concentración del percentil 98 en un punto receptor, es el valor de
concentración tal que 98 % de las concentraciones calculadas en este punto son
inferiores al valor determinado por la modelación y 2 % de los valores de
concentración calculados son superiores (175 horas/ acumuladas en un año). La
evaluación con la concentración de percentil 98 es aceptada y aplicada en
países que cuentan con legislación sobre olores, las cuales se identifican en la

Tabla 4.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||18 de<br>37|

Según el estudio de ECOTEC (2013), las normas de referencia, para evaluar el
impacto de olor generado por Plantas de Tratamiento de Aguas Servidas, indica
criterios de calidad que varían entre 5 y 10 u.o/m3. Estos valores se especifican

en la Tabla 4.

**Tabla 4: Criterios de Calidad de Olor a Nivel Internacional**

|ESTADO Ó<br>CIUDAD-PAÍS|LÍMITE|TIEMPO|FRECUENCIA<br>%|USO DE<br>SUELO|TIPO DE<br>FUENTE|REFERENCIA|
|---|---|---|---|---|---|---|
|<br>UK<br>|5 OU/m3<br>|<br>- <br>|<br>98%<br>|<br>- <br>|<br>PTAS<br>|<br>Mahin (2001)<br>|

_Fuente: ECOTEC (2013), “Antecedentes para la Regulación de Olores en Chile”, realizado para la_
_Subsecretaría del Medio Ambiente, Santiago de Chile, agosto._

De esta forma se mantiene la norma de referencia bajo la cual fue extendida la
Resolución de Calificación Ambiental Favorable N° 320/2017 que aprobó la
ampliación anterior de la PTAS.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||19 de<br>37|

## 10. DESCRIPCIÓN DE LAS FUENTES Y ESCENARIOS DE MODELACIÓN

En la Tabla 5 se especifican las condiciones de funcionamiento de cada fuente
en el escenario de modelación propuesto, indicando si las mismas son
generadora de gases odoríficos para ser consideradas en la modelación.

**Tabla 5: Fuentes consideradas en Proyecto**

|Escen<br>ario|No|Fuente|Descripción|Incluida en<br>la<br>modelación|Comentario|
|---|---|---|---|---|---|
|Actual|1|Sedimentador I|Unidad abierta|Si||
|Actual|2|Cámara de distribución<br>I|Unidad abierta|Si||
|Actual|3|Digestor I|Unidad abierta|Si|Esta unidad no<br>operará en el<br>Escenario<br>Proyectado|
|Actual|4|Espesador de lodos I|Unidad abierta|Si||
|Actual|5|Reactores (2) I|Unidades<br>abiertas|Si||
|Actual|6|Contenedor de lodos<br>I|Unidad abierta|Si|Esta unidad no<br>operará en el<br>Escenario<br>Proyectado|
|Actual|7|Ventana (Galpón de<br>deshidratado de<br>lodo<br>I)|Abertura en el<br>edificio|Si|Esta unidad no<br>operará en el<br>Escenario<br>Proyectado|
|Actual|8|Reactor biológico<br>II|Unidad abierta|Si||
|Actual|9|Sedimentadores (2) II|Unidades<br>abiertas|Si||
|Actual|10|Cámara repartidora de flujo<br>#1 II|Unidad abierta|Si||
|Actual|11|Cámara de<br>contacto II|Unidad abierta|Si||
|Actual|12|Cámara medición de<br>caudal efluente y<br>repartidora de caudal #3<br>II|Unidad abierta|<br>Si||

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||20 de<br>37|

|Escen<br>ario|No|Fuente|Descripción|Incluida en<br>la<br>modelación|Comentario|
|---|---|---|---|---|---|
|Actual|13|Pre-tratamiento II tipo Huber|Unidad cerrada, sin<br>embargo, para la<br>modelación se<br>considerará que la<br>emisión de olor es<br>directa, para realizar<br>la evaluación en el<br>peor escenario, toda<br>vez que no se tiene<br>información respecto<br>a la ventilación del<br>edificio donde se<br>ubicará el Huber|<br>Si||
|Actual|14|Contenedor de lodos<br>II|Unidad abierta|Si||
|Actual|15|Espesador de lodos II|Unidad abierta|Si||
|Actual|16|Ventana (Galpón de<br>deshidratado de<br>lodo II)|Abertura en el<br>edificio|Si|Esta unidad no<br>operará en el<br>Escenario<br>Proyectado|
|Actual|17|Cancha de Secado|Unidad Abierta|Si|Esta unidad no<br>operará en el<br>Escenario<br>Proyectado|
|Proyectado|18|Cámara de Reja<br>Mecánica|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|
|Proyectado|19|Planta Elevadora<br>Cabecera|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|
|Proyectado|20|Tratamiento Preliminar|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|
|Proyectado|21|Reactor|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|
|Proyectado|22|PE RAS-WAS|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|
|Proyectado|23|Espesador Lodos|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|
|Proyectado|24|Digestor Lodos|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|
|Proyectado|25|Galpón Deshidratado|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||21 de<br>37|

|Escen<br>ario|No|Fuente|Descripción|Incluida en<br>la<br>modelación|Comentario|
|---|---|---|---|---|---|
|Proye<br>ctado|26|Galpón Acopio|Unidad<br>Cerrada|Si|Unidad Encapsulada,<br>no genera emisiones|

De acuerdo con la Tabla 5, para el escenario actual se han identificado diecisiete
(17) fuentes generadoras de olor, mientras que para el escenario proyectado se
han identificado veintiun (21) fuentes generadoras de olor.

Se utilizó la tasa de emisión fija para cada fuente en la modelación. Estos datos
fueron obtenidos partir de los resultados de la campaña de muestreo y análisis

Olfatométrico realizado en las actuales unidades de la PTAS Santo Tomás

realizada en el mes de Agosto, en caso que sea necesario se utilizarán factores
de emisión, utilizando como fuente principal para la recopilación de estos el
Informe Final Servicio de Recopilación y Sistematización de Factores de Emisión al
Aire para el SEA, complementando dicha información con documentos
relacionados que serán citados particularmente en cada caso (como por
ejemplo procesos de evaluación ambiental anteriores para la misma PTAS).

Las fuentes de olor están representadas en las Figura **4** y Figura 5 y la Tabla 6

describe sus características.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||22 de<br>37|

**Tabla 6 : Características de las fuentes a modelar**

|(1) Fuente|ID|Tipo|Numero de<br>fuentes<br>idénticas|Altura de<br>emisión desde<br>el|Concent-<br>ración de olor|Tasa de<br>Emisión|Área|Flujo|Flujo de Olor<br>total|
|---|---|---|---|---|---|---|---|---|---|
|**(1)Fuente**|**ID**|**Tipo**|**Numero de**<br>**fuentes**<br>**idénticas**|**suelo**|**suelo**|**suelo**|**suelo**|**suelo**|**suelo**|
|**(1)Fuente**|**ID**|**Tipo**|**Numero de**<br>**fuentes**<br>**idénticas**|**m **|**u.o./m3**|**u.o./s/m2**|**m2**|**m3/s**|**u.o./s**|
|Sedimentador I|SEDIM|Superficie|1|3,5|591|2,000|260|-|520|
|Cámara de distribución I|CAM_DIS|Superficie|1|3,5|-|5,900|27|_- _|159|
|Digestor I|DIGESTOR|Superficie|1|3,5|173|0,750|156|-|117|
|Espesador de lodos I|ES_LODOS|Superficie|1|3,5|-|2,000|19|-|38|
|Reactores I|REACTOR1 y 2|Superficie|2|3,5|305|1,500|226|-|339|
|Contenedor de lodos I|CON_LODO|Superficie|1|1|1092|9,051|10|-|91|
|Ventana (Galpón de deshidratado de<br>lodo I)|VENTANA (11)|Volumétrica|1|1|2137|-|-|0,7|436|
|Reactor biológico II|REACTORP|Superficie|1|3,5|-|1,500|750|-|1125|
|Sedimentadores (2) II|SEDIM_P1 y 2|Superficie|2|3,5|-|2,000|154|-|308|
|Cámara repartidora de flujo #1 II|CAM_R_P|Superficie|1|3,5|-|1,208|9|-|11|
|Cámara de contacto II|CAM_C_P|Superficie|1|3|145|1,208|82|-|99|
|Cámara medición de caudal efluente y<br>repartidora de caudal #3 II|CAM_MC_P|Superficie|1|3|-|1,208|12|-|14|
|Pre-tratamiento II|PRET_P|Superficie|1|6,4|-|5,900|21|-|124|
|Contenedor de lodos II|CON_LO_P|Superficie|1|1|-|9,051|10|-|91|
|Espesador de lodos II|ES_LOD_P|Superficie|1|2|-||27|-|133|
|Ventana (Galpón de deshidratado de<br>lodo II)|VENTA_P (12)|Volumétrica|1|1|2137 (5)|-|-|0,3 (10)|640|
|Cancha de Secado|CDS_P|Superficie|1|0|-|29,7|35|-|1040|
|Cámara de Reja Mecánica|CRM|Superficie|1|0,2|-|5,900|55|-|325|
|Planta Elevadora Cabecera|PEC|Superficie|1|0,2|-|5,900|15|-|89|

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||23 de<br>37|

|(1) Fuente|ID|Tipo|Numero de<br>fuentes<br>idénticas|Altura de<br>emisión desde<br>el|Concent-<br>ración de olor|Tasa de<br>Emisión|Área|Flujo|Flujo de Olor<br>total|
|---|---|---|---|---|---|---|---|---|---|
|**(1)Fuente**|**ID**|**Tipo**|**Numero de**<br>**fuentes**<br>**idénticas**|**suelo**|**suelo**|**suelo**|**suelo**|**suelo**|**suelo**|
|**(1)Fuente**|**ID**|**Tipo**|**Numero de**<br>**fuentes**<br>**idénticas**|**m **|**u.o./m3**|**u.o./s/m2**|**m2**|**m3/s**|**u.o./s**|
|Tratamiento Preliminar|TP|Superficie|1|7,8|-|5,900|88|-|519|
|Reactor|REAN|Superficie|1|4,8|-|4,039|590|-|2383|
|PE RAS-WAS|RAS|Superficie|1|3,6|-|4,039|16|-|65|
|Espesador Lodos|EL|Superficie|1|5,7|-|4,922|30|-|148|
|Digestor Lodos|DL|Superficie|1|4,3|-|1,503|690|-|1037|
|Galpón Deshidratado|GD|Volumétrica|1|0|2137|-|-|0,3|640|
|Galpón Acopio|GA|Volumétrica|1|0|2137|-|-|0,3|640|
|||||||Flujo de Olor Total Escenario Actual|Flujo de Olor Total Escenario Actual|Flujo de Olor Total Escenario Actual|6216|
|||||||Flujo de Olor Total Escenario Proyectado|Flujo de Olor Total Escenario Proyectado|Flujo de Olor Total Escenario Proyectado|8806|

NOTA: Toda la información aquí presentada corresponde a asimilación de tasas de emisión obtenidos en las fuentes muestreadas que siguen el
proceso del tratamiento del agua. Además se señala que las superficies y alturas de emisión han sido obtenidas a partir de la información
presentada por el Titular del proyecto.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||24 de<br>37|

PTAS Santo Tomas

**Figura 4: Fuentes - Escenario Actual**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||25 de<br>37|

PTAS Santo Tomas

**Figura 5: Fuentes - Escenario Proyectado**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||26 de<br>37|

## 11. RESULTADOS DE LA MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA

El modelo atmosférico predice como los olores se van a dispersar en los

alrededores del Proyecto.

Para los propósitos de este estudio, se calculó el percentil 98 (CP98) y la
frecuencia de exceso del límite de 5 u.o./m3 en porcentaje y hora por año.

Los resultados de percentil 98 son el valor de la concentración tal que el 98 % de
las concentraciones calculadas en este punto son inferiores al valor determinado
por la modelación y 2 % de los valores de concentración calculados son
superiores (175 horas/ acumuladas en un año).

Las frecuencias de exceso del límite de 5 u.o./m3 en porcentaje y hora por año
permite saber cuánto tiempo los receptores discretos son expuestos a niveles
donde El olor es calificable y puede comenzar a recibirse quejas (puede ser
identificado). Los resultados para cada escenario se presentan en forma gráfica

en el ANEXO A.

**Escenario Actual de Evaluación**

Para el escenario actual de evaluación la concentración del percentil 98 más
alta calculada en los receptores discretos evaluados es de 4,3 u.o./m [3], para el
receptor R6, los demás receptores varían entre 0,0 y 1,2 u.o./m [3.]

El resultado máximo de la frecuencia de exceso del límite de 5 u.o./m [3], que indica
el nivel donde el olor es calificable y puede comenzar a recibirse quejas (puede
ser identificado), alcanza 1,2% o 113 horas/año, para el receptor R6, para los
demás receptores el valor es de 0,0% o 0 h/año.

Los resultados en los receptores discretos de la concentración del percentil 98 y
las frecuencias de exceso del límite de 5 u.o./m [3 ] en porcentaje y horas/año están
resumidos en la Tabla 7. Las isopletas de concentración se muestran en el ANEXO

A.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||27 de<br>37|

_**Tabla 7: Resultados de concentración de olor y frecuencia de exceso en los**_
_**receptores discretos - Escenario Actual.**_

|Receptores Discretos|Percentil 98|Frecuencia de Exceso del Límite de|
|---|---|---|
|**Receptores Discretos**|**Percentil 98**|**5 u.o./m3 **|
|**Receptores Discretos**|**[u.o./ m3] **|**% (# horas/año)**|
|R1|0,0|0,0 % (0 h/a)|
|R2|0,0|0,0 % (0 h/a)|
|R3|0,0|0,0 % (0 h/a)|
|R4|0,0|0,0 % (0 h/a)|
|R5|0,0|0,0 % (0 h/a)|
|R6|4,3|1,2 % (113 h/a)|
|R7|0,1|0,0 % (0 h/a)|
|R8|1,2|0,0% (0 h/a)|
|R9|1,2|0,0% (0 h/a)|
|R10|0,2|0,0 % (0 h/a)|

**Escenario Proyectado de Evaluación**

Para el escenario actual de evaluación la concentración del percentil 98 más
alta calculada en los receptores discretos evaluados es de 2,8 u.o./m [3], para el
receptor R6, los demás receptores varían entre 0,0 y 0,8 u.o./m [3.]

El resultado máximo de la frecuencia de exceso del límite de 5 u.o./m [3], que indica
el nivel donde el olor es calificable y puede comenzar a recibirse quejas (puede

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||28 de<br>37|

ser identificado), alcanza 0,4% o 39 horas/año, para el receptor R6, para los
demás receptores se presentan valores de 0,0% o 0 h/año.

Los resultados en los receptores discretos de la concentración del percentil 98 y
las frecuencias de exceso del límite de 5 u.o./m [3 ] en porcentaje y horas/año están
resumidos en la Tabla 8. Las isopletas de concentración se muestran en el ANEXO

A.

_**Tabla 8: Resultados de concentración de olor y frecuencia de exceso en los**_
_**receptores discretos - Escenario Proyectado.**_

|Receptores Discretos|Percentil 98|Frecuencia de Exceso del Límite de|
|---|---|---|
|**Receptores Discretos**|**Percentil 98**|**5 u.o./m3 **|
|**Receptores Discretos**|**[u.o./ m3] **|**% (# horas/año)**|
|R1|0,0|0,0 % (0 h/a)|
|R2|0,0|0,0 % (0 h/a)|
|R3|0,0|0,0 % (0 h/a)|
|R4|0,0|0,0 % (0 h/a)|
|R5|0,0|0,0 % (0 h/a)|
|R6|2,8|0,4 % (39 h/a)|
|R7|0,1|0,0 % (0 h/a)|
|R8|0,8|0,0 % (0 h/a)|
|R9|0,8|0,0 % (0 h/a)|
|R10|0,1|0,0 % (0 h/a)|

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||29 de<br>37|

## 12. CONCLUSIONES

Para las instalaciones de la “ Planta de Tratamiento de Aguas Servidas (PTAS Santo
Tomás) Santo Tomás”, ubicado en la comuna de Lampa, Región Metropolitana,
se realizó la modelación de la dispersión atmosférica a través del modelo Calpuff
, para evaluar el impacto de olor en un escenario actual y proyectado de
operación del proceso de tratamiento de aguas servidas, midiendo este impacto
sobre la población aledaña.

De los resultados obtenidos por la modelación para ambos escenarios de
modelación, actual, se tiene que:

 De acuerdo a la configuración de ambos escenarios de evaluación, los
resultados obtenidos indican que el valor del percentil 98 de las
concentraciones en 1 hora en los receptores discretos considerados NO se
supera el valor límite de 5u.o./m [3], es decir, las emisiones NO generan una
superación de los límites normativos analizados.

 - El resultado máximo de la frecuencia de exceso del límite de 5 u.o./m3,

que indica el nivel donde el olor es calificable y puede comenzar a
recibirse quejas (puede ser identificado), para ambos escenarios en
evaluación alcanza un máximo de 1,2% o 113 horas/año en el receptor
discreto R6, mientras que en el resto de los receptores discretos evaluados
es de menos de un 2%. Se señala que para el escenario Proyectado no se
superan las 39 h/año en el receptor discreto R6

 Al respecto en la Figura A-1 y A-3 se puede apreciar que el área de
influencia de la componente de olor, identificada como la inscrita al
interior de la línea de isoconcentración de olor con valor de 1 u.o./m [3],

correspondiente a 240 ha en el escenario actual y una disminución a 165
ha en el escenario proyectado.

De acuerdo a los resultados obtenidos en ambos escenarios de evaluación, se

señala que NO existiría superación de la normativa de referencia, para ninguno
de los escenarios de operación de la PTAS.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||30 de<br>37|

## 13. BIBLIOGRAFÍA

 ECOTEC (2013), Estudio: Antecedentes para la Regulación de Olores en
Chile, realizado para la Subsecretaría del Medio Ambiente, Santiago de
Chile, Agosto.

 SEA (Sistema de Evaluación Ambiental) (2012), “Guía para el uso de

modelos de Calidad del Aire en el SEIA”, Ministerio del Medio Ambiente de

Chile.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||31 de<br>37|

## ANEXO A: RESULTADOS GRÁFICOS DE MODELACIÓN

Los resultados se presentan en forma gráfica ilustran mediante iso-contornos de
los valores de concentración, calculados en percentil 98, mostrando la siguiente

información:

 Isopleta de concentración de olor (líneas que unen los diferentes puntos
con similares valores o rangos de valor), las cuales se encuentran
superpuestas en el mapa sobre el área de modelación. Cada color
representa un rango diferente. Una escala UTM se encuentra situada en el
lado inferior e izquierdo.

 Una leyenda en la que se presentan los distintos rangos y colores asociados
a las concentraciones de olor, se expresan en unidades de olor por metros
cúbicos (u.o./m3), para las concentraciones máximas y el percentil.

 Los receptores discretos están representados con una circulo azul.

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||32 de<br>37|

**Figura A - 1 Percentil 98 - Escenario Actual**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||33 de<br>37|

**Figura A - 2 Frecuencia de Exceso del Límite de 5 u.o./m** **[3]** **- Escenario Actual**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||34 de<br>37|

**Figura A - 3 Percentil 98 - Escenario Proyectado**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||35 de<br>37|

PTAS Santo Tomas

**Figura A - 4 Frecuencia de Exceso del Límite de 5 u.o./m** **[3]** **- Escenario Proyectado**

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||36 de<br>37|

|Col1|BCC S.A|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|**REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR**|
|**IDENTIFICACIÓN**|**FECHA DE REVISIÓN**|**VERSIÓN**|**VERSIÓN**|**RESPONSABLES**|**PAGINA**|
|BCC_2022|Diciembre 2022|V-3|V-3||37 de<br>37|

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2: Sesgo, Error Cuadrático Medio y Coeficiente de Correlación - Información****

| Información | Estación | Sesgo | Error<br>Cuadrático<br>Medio | Coeficiente<br>de Correlación |
| --- | --- | --- | --- | --- |
| Observada | El Oasis | 0,42 | 1,89 | -0,01 |
| Modelo<br>Pronóstico | Archivo<br>WRF | Archivo<br>WRF | Archivo<br>WRF | Archivo<br>WRF |

**Tabla 1: Detalle de proyección cartográfica y coordenadas Archivos WRF****

| Proyección Cartográfica | Cónica Conforme de Lambert (LCC) |
| --- | --- |
| Período | 1 Ene 2021 00:00 - 1 Ene 2022 00:00 |
| Origen | RLAT0 = 33.340S<br>RLAN0 = 70.794W |
| DATUM | NWS-84 6370 km Radius, Global Sphere |
| Grilla | 50 x 50 km |
| Resolución Espacial | 1 x 1 km |
| Celdas verticals | 10 |

**Tabla 4.**

| Col1 | BCC S.A | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
|  | **REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR** | **REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR** | **REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR** | **REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR** | **REPORTE DE MODELACIÓN DE DISPERSIÓN DE OLOR** |
| **IDENTIFICACIÓN** | **FECHA DE REVISIÓN** | **VERSIÓN** | **VERSIÓN** | **RESPONSABLES** | **PAGINA** |
| BCC_2022 | Diciembre 2022 | V-3 | V-3 |  | 18 de<br>37 |

**Tabla 6: : Características de las fuentes a modelar****

| (1) Fuente | ID | Tipo | Numero de<br>fuentes<br>idénticas | Altura de<br>emisión desde<br>el | Concent-<br>ración de olor | Tasa de<br>Emisión | Área | Flujo | Flujo de Olor<br>total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **(1)Fuente** | **ID** | **Tipo** | **Numero de**<br>**fuentes**<br>**idénticas** | **suelo** | **suelo** | **suelo** | **suelo** | **suelo** | **suelo** |
| **(1)Fuente** | **ID** | **Tipo** | **Numero de**<br>**fuentes**<br>**idénticas** | **m ** | **u.o./m3** | **u.o./s/m2** | **m2** | **m3/s** | **u.o./s** |
| Sedimentador I | SEDIM | Superficie | 1 | 3,5 | 591 | 2,000 | 260 | - | 520 |
| Cámara de distribución I | CAM_DIS | Superficie | 1 | 3,5 | - | 5,900 | 27 | _- _ | 159 |
| Digestor I | DIGESTOR | Superficie | 1 | 3,5 | 173 | 0,750 | 156 | - | 117 |
| Espesador de lodos I | ES_LODOS | Superficie | 1 | 3,5 | - | 2,000 | 19 | - | 38 |
| Reactores I | REACTOR1 y 2 | Superficie | 2 | 3,5 | 305 | 1,500 | 226 | - | 339 |
| Contenedor de lodos I | CON_LODO | Superficie | 1 | 1 | 1092 | 9,051 | 10 | - | 91 |
| Ventana (Galpón de deshidratado de<br>lodo I) | VENTANA (11) | Volumétrica | 1 | 1 | 2137 | - | - | 0,7 | 436 |
| Reactor biológico II | REACTORP | Superficie | 1 | 3,5 | - | 1,500 | 750 | - | 1125 |
| Sedimentadores (2) II | SEDIM_P1 y 2 | Superficie | 2 | 3,5 | - | 2,000 | 154 | - | 308 |
| Cámara repartidora de flujo #1 II | CAM_R_P | Superficie | 1 | 3,5 | - | 1,208 | 9 | - | 11 |
| Cámara de contacto II | CAM_C_P | Superficie | 1 | 3 | 145 | 1,208 | 82 | - | 99 |
| Cámara medición de caudal efluente y<br>repartidora de caudal #3 II | CAM_MC_P | Superficie | 1 | 3 | - | 1,208 | 12 | - | 14 |
| Pre-tratamiento II | PRET_P | Superficie | 1 | 6,4 | - | 5,900 | 21 | - | 124 |
| Contenedor de lodos II | CON_LO_P | Superficie | 1 | 1 | - | 9,051 | 10 | - | 91 |
| Espesador de lodos II | ES_LOD_P | Superficie | 1 | 2 | - |  | 27 | - | 133 |
| Ventana (Galpón de deshidratado de<br>lodo II) | VENTA_P (12) | Volumétrica | 1 | 1 | 2137 (5) | - | - | 0,3 (10) | 640 |
| Cancha de Secado | CDS_P | Superficie | 1 | 0 | - | 29,7 | 35 | - | 1040 |
| Cámara de Reja Mecánica | CRM | Superficie | 1 | 0,2 | - | 5,900 | 55 | - | 325 |
| Planta Elevadora Cabecera | PEC | Superficie | 1 | 0,2 | - | 5,900 | 15 | - | 89 |
