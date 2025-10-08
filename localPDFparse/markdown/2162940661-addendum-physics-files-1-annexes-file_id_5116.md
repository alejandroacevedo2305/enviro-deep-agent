---
title: Sin título
author: mesenia atenas
date: D:20250316052914-03'00'
language: es
type: report
pages: 42
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe Técnico
-->

# Informe Técnico

## Actualización Modelo Hidrogeológico SHAC Punitaqui. DIA Proyecto Los Mantos

#### INFORME Rev. B

PREPARADO PARA

**Marzo de 2025**

### Informe Técnico Actualización Modelo Hidrogeológico SHAC Punitaqui. DIA Proyecto Los Mantos

Código de Proyecto: [2024-329-DIALM]

#### HIDROGEOLOGIA y MEDIO AMBIENTE SUSTENTABLE LTDA

Suecia 211, Oficina 701-A, Providencia - Santiago Chile
[e-mail: contacto@hidromas.cl](mailto:contacto@hidromas.cl)

website: www.hidromas.cl

Tel: +(56-2) 232027540

|REV.|Elaborado por:|Revisado por:|Aprobado por:|DESCRIPCIÓN|
|---|---|---|---|---|
|Rev.B|Rodrigo Zamorano|René Figueroa|Carlos Espinoza||
|Rev.B|[06.03.2025]|[07.03.2025]|[17.03.2025]|[17.03.2025]|

____________________________________________________________________________

**HIDROMAS** Hidrogeología y Medio Ambiente Sustentable | Av. Suecia 211 Of 701-A, Providencia | www.hidromas.cl

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

**TABLA DE CONTENIDOS**

**1** **INTRODUCCIÓN ................................................................................................................................. 1**

1.1 Antecedentes Generales .................................................................................................................. 1

1.2 Zona de Estudio ............................................................................................................................... 1

1.3 Objetivos ........................................................................................................................................... 2

1.3.1 Objetivo General ........................................................................................................................ 2

1.3.2 Objetivos Específicos ................................................................................................................. 2

**2** **CONSTRUCCIÓN MODELO NUMÉRICO .......................................................................................... 1**

2.1 Aspectos Generales ......................................................................................................................... 1

2.2 Dominio y Geometría ........................................................................................................................ 1

2.3 Representación Temporal en Modelo Hidrogeológico ..................................................................... 5

2.4 Definición de la Grilla de Modelación ............................................................................................... 5

**3** **ESTIMACIÓN DE LA RECARGA ....................................................................................................... 7**

3.1 Aspectos Generales ......................................................................................................................... 7

3.2 Actualización de la Recarga ............................................................................................................. 8

3.2.1 Relleno de información pluviométrica estación Punitaqui ......................................................... 8

3.2.2 Correlación recarga - precipitación ........................................................................................... 9

3.2.3 Distribución espacial de la recarga .......................................................................................... 11

**4** **POZOS DE EXTRACCIÓN Y PROPIEDADES HIDROGEOLÓGICAS ........................................... 13**

4.1 Información sobre Pozos de Bombeo ............................................................................................ 13

4.2 Unidades Hidrogeológicas y Propiedades Hidráulicas .................................................................. 14

**5** **PROCESO DE CALIBRACIÓN Y AJUSTE ...................................................................................... 17**

5.1 Ajuste de niveles ............................................................................................................................ 17

5.2 Hidrogramas de Niveles ................................................................................................................. 20

5.2.1 Pozos DGA .............................................................................................................................. 20

5.2.2 Pozos Monitoreado BMR ......................................................................................................... 20

5.3 Equipotenciales y Direcciones de Flujo .......................................................................................... 27

5.4 Balance Hídrico .............................................................................................................................. 31

**6** **CONCLUSIONES .............................................................................................................................. 32**

**7** **REFERENCIAS ................................................................................................................................. 33**

**APÉNDICES**

Apéndice A Datos de Precipitación

_____________________________________________________________________________________
i

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

**LISTADO DE FIGURAS**

Figura 1-1: Ubicación Referencial Proyecto y Sectores de Bombeo ............................................................ 3

Figura 1-2: Ubicación Referencial Sectores de Interés desde el punto de vista de Recursos Hídricos ....... 4

Figura 2-1: Dominio y elevaciones de modelo numérico .............................................................................. 2

Figura 2-2: Perfil L1 Los Mantos ................................................................................................................... 3

Figura 2-3: Perfil C3 sector El Ciénago ......................................................................................................... 3

Figura 2-4: Perfil N-S sector El Ciénago ....................................................................................................... 4

Figura 2-5: Espesor del Acuífero ................................................................................................................... 5

Figura 2-6: Grilla de Modelación y Acercamiento en Zona de Interés con refinamiento _Quadtree_ .............. 6

Figura 3-1: Zonas de Recarga del Modelo PEGH ........................................................................................ 7

Figura 3-2: Ubicación Estaciones Meteorológicas de la DGA ...................................................................... 8

Figura 3-3: Serie Precipitación Anual Estación Punitaqui ............................................................................. 9

Figura 3-4: Correlación entre Recarga Modelo PEGH y Precipitación Anual Punitaqui ............................. 10

Figura 3-5: Serie de Recarga Anual rellenada en Dominio de Modelación ................................................ 10

Figura 3-6: Zonas de Recarga Directa y Lateral ......................................................................................... 11

Figura 3-7: Serie de Caudal de Recarga Distribuida en Zonas .................................................................. 12

Figura 4-1: Ubicación Espacial de Pozos de Extracción Dentro del Dominio ............................................. 13

Figura 4-2: Serie de Caudal de Extracción de Pozos de Bombeo .............................................................. 14

Figura 4-3: Representación de Unidades Hidrogeológicas en Modelo Numérico ...................................... 16

Figura 5-1: Ubicación Pozos de Observación para Calibración de Modelo Numérico ............................... 17

Figura 5-2: Niveles Observados versus Niveles Calculados por el Modelo Numérico ............................... 18

Figura 5-3: Histograma de Residuales ........................................................................................................ 19

Figura 5-4: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA AP Punitaqui ............ 21

Figura 5-5: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Graneros ............ 21

Figura 5-6: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Nogales ............. 22

Figura 5-7: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Campo Lindo ..... 22

Figura 5-8: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. U. Campesina .... 23

Figura 5-9: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Nueva Aurora .... 23

_____________________________________________________________________________________
ii

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

Figura 5-10: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Rancho 1 ........................ 24

Figura 5-11: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Rancho 3 ........................ 24

Figura 5-12: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Rancho 5 ........................ 25

Figura 5-13: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Nuevo 1 .......................... 25

Figura 5-14: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Nuevo 2 .......................... 26

Figura 5-15: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Los Mantos ..................... 26

Figura 5-16: Mapa de Equipotenciales para Enero del Año 2000 .............................................................. 28

Figura 5-17: Mapa de Equipotenciales para Junio del Año 2024 ............................................................... 29

Figura 5-18: Mapa de Equipotenciales Sector El Ciénago ......................................................................... 30

Figura 5-19: Serie Temporal de las Componentes del Balance Hídrico del Sistema ................................. 31

**LISTADO DE TABLAS**

Tabla 3-1: Información de las Estaciones Relevantes para el Estudio ......................................................... 8

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- utilizadas en el presente análisis y en Figura 3-2 se ilustra la distribución espacial de las estaciones DGA. La información pluviométrica considerada se presenta en el Apéndice A de este informe. -->

**Tabla 3-1: Información de las Estaciones Relevantes para el Estudio****

| Estación | Código BNA | Coordenada Este (m) | Coordenada Norte<br>(m) | Período con<br>información |
| --- | --- | --- | --- | --- |
| Punitaqui | 4555001 | 284.077 | 6.586.719 | 1990 - 2020 |
| La Placilla | 4554003 | 278.631 | 6.579.522 | 1990 - 2020 |
| Ovalle DGA | 4551005 | 288.294 | 6.612.196 | 1990 - 2024 |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia._ **Figura 3-2: Ubicación Estaciones Meteorológicas de la DGA** -->
<!-- FIN TABLA 3-1 -->


Tabla 4-1: Resumen Definición Unidades Hidrogeológicas ........................................................................ 15

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Esta unidad tiene una baja a nula capacidad de almacenar y transmitir el agua subterránea por lo que se le considera los límites laterales y en profundidad de las unidades acuíferas. Presenta los mayores valores de resistividad, siendo mayores a 150 Ohm-m (Tabla 4-1). -->

**Tabla 4-1: Resumen Definición Unidades Hidrogeológicas****

| Nombre | Col2 | Geología<br>Superficial | Litología de<br>Pozos | Unidad de<br>Resistividad<br>(Ohm-m) | Transmisividad<br>Representativa (m2/d) |
| --- | --- | --- | --- | --- | --- |
| UH1 | Aluvial y fluvial actual | Hf | Gravas y arenas<br>con bajo contenido<br>de limo o arcilla<br>(<15%) | 1 a 42 | 5,0 - 514,9 |
| UH1 | Aluvial y fluvial Antiguo | PlHf, PlHa, Pla,<br>MPc | Gravas y arenas<br>con predominio de<br>contenido de<br>arcilla | Gravas y arenas<br>con predominio de<br>contenido de<br>arcilla | Gravas y arenas<br>con predominio de<br>contenido de<br>arcilla |
| UH1 | Coluviales | PlHc | S/I | S/I | S/I |
| UH2: Roca Fracturada | UH2: Roca Fracturada | JKas, JsKip,<br>Kim, Kiqm Ksh,<br>Kip, Kia | Roca Alterada o<br>Fracturada | 27 a 150 | 13,0 - 26,3 |
| UH3: Basamento Impermeable | UH3: Basamento Impermeable | UH3: Basamento Impermeable | Roca Sana | > 150 | No Aplica |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia a partir de CPH (2014) y análisis presentado en acápite 4.4.2._ _______________________________________________________________________________________ Rev. B / 17.03.2025 15 -->
<!-- FIN TABLA 4-1 -->


_____________________________________________________________________________________
iii

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

**1** **INTRODUCCIÓN**

**1.1** **Antecedentes Generales**

Minera BMR SpA (en adelante BMR) solicitó a HIDROMAS una asesoría referida a recursos hídricos
subterráneos para el desarrollo de una Declaración de Impacto Ambiental (DIA) que considera la incorporación
de un Depósito de Relaves Filtrados y la extensión de la vida útil de la Planta Los Mantos.

En este contexto HIDROMAS (2024) realizó una caracterización geológica e hidrogeológica general para el
Sector Hidrogeológico de Aprovechamiento Común (SHAC) de Punitaqui y una caracterización hidrogeológica
más específica para los sectores de interés para el presente Proyecto: Los Mantos y El Ciénago, la cual fue
presentada en el Anexo 2.9 de la DIA (HIDROMAS, 2024). Dicha caracterización se basa tanto en información
histórica generada por el Proyecto, así como en nueva data generada en el marco de la DIA.

Esta caracterización fue considerada para actualizar el modelo hidrogeológico que sustenta la zona de estudio,
de manera de incorporar todas las propiedades levantadas en el Anexo 2.9 de la DIA. La actualización del
modelo de aguas subterráneas consiste en una restructuración geométrica total del modelo PEGH (DGAHídrica Consultores, 2020), utilizando información generada en la zona de estudio, además de una mejor
representación de las condiciones de borde y resolución del modelo, para finalmente realizar un ajuste de
niveles de agua subterránea para representar adecuadamente la dinámica del sistema.

De esta forma, la presente actualización del modelo hidrogeológico da respuesta a lo observado en la Adenda
en el punto 4.2.6.7. que señala que:

“ _Respecto a la utilización del modelo PEGH se solicita al Titular describir detalladamente la incorporación de_
_las propiedades hidrogeológicas que fueron levantadas en el estudio de caracterización presentado en el_
_Anexo 2.9 de la DIA. De no haber sido consideradas, el Titular deberá actualizar el modelo numérico_

_incorporando las propiedades definidas en la caracterización hidrogeológica.”_

**1.2** **Zona de Estudio**

Desde el punto de vista administrativo la Planta Los Mantos se encuentra en la comuna de Punitaqui, provincia
de Limarí, región de Coquimbo. Se localiza a unos 114 km al sur de la ciudad de La Serena y a unos 30 km al
suroeste de Ovalle, en la quebrada Los Mantos. Desde el punto de vista de los recursos hídricos los sectores
de interés del Proyecto se encuentran ubicados dentro de la cuenca del río Limarí y del SHAC de Punitaqui.

Las fuentes de abastecimiento consideradas para el proyecto se ubicarán en dos sectores:

 - El primer sector se ubica en la parte alta de la quebrada Los Mantos, donde el Proyecto cuenta con
dos pozos con derechos de agua. Estos pozos se ubican a aproximadamente 700 a 1.000 m hacia el

Este desde la ubicación de la Planta.

 - La segunda fuente corresponde a los derechos de un tercero (SAGA) que cuenta con dos pozos de
bombeo denominados SAGA N°1 y SAGA N°2, que se ubican dentro de la denominada “Parcela
N°45”, la que se ubica en el sector de El Ciénago, aproximadamente a uno 8,3 km desde el sector de

la Planta Los Mantos.

Es importante indicar que para efectos de la DIA se presentó que la extracción se desarrollaría desde el
denominado pozo “Parcela N°45”, dentro de la parcela homónima, pero en la actualidad los pozos que el titular
del derecho está operando son los indicados SAGA N°1 (expediente ND-0402-800265) y SAGA N°2 (VPC

_______________________________________________________________________________________
Rev. B / 17.03.2025 1

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

0402-105). Lo anterior no implica un mayor cambio en términos del análisis de efectos, ya que dichos tres
pozos están bastante cercanos uno del otro (del orden de 350 m).

En la Figura 1-1 se muestra de forma referencial la ubicación del Proyecto en un contexto regional y luego a
una escala más local. Luego, en la Figura 1-2 se muestra la ubicación de ambos sectores dentro de la cuenca
del río Limarí, compuesto para efectos de agua subterránea por 14 Sectores Hidrogeológicos de
Aprovechamiento Común (SHAC), entre los que se destaca el SHAC Punitaqui en el cual se encuentra el
proyecto en evaluación.

**1.3** **Objetivos**

1.3.1 Objetivo General

Actualizar el modelo hidrogeológico del SHAC Punitaqui de manera de incorporar la caracterización
hidrogeológica presentada en el Anexo 2.9 de la DIA del Proyecto.

1.3.2 Objetivos Específicos

Para la consecución del objetivo general se contempla el cumplimiento de los siguientes objetivos específicos:

 - Restructurar geometría y dominio del modelo PEGH de manera de representar adecuadamente estas
propiedades en el modelo numérico.

 - Implementación de Unidades Hidrogeológicas (UH) en modelo numérico.

 - Actualizar modelo a la fecha de estudio, marzo del año 2025.

 - Ajustar niveles de aguas subterráneas para representación histórica de información.

_______________________________________________________________________________________
Rev. B / 17.03.2025 2

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 1-1: Ubicación Referencial Proyecto y Sectores de Bombeo**

_Fuente: Modificado de BMR (2023)._

_______________________________________________________________________________________
Rev. B / 17.03.2025 3

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 1-2: Ubicación Referencial Sectores de Interés desde el punto de vista de Recursos Hídricos**

Sector El Ciénago
(Extracción de Aguas)

Sector Los Mantos
(Planta y Extracción

de Aguas)

_Fuente: Modificado de DGA - Hídrica Consultores (2020)._

_______________________________________________________________________________________
Rev. B / 17.03.2025 4

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**2** **CONSTRUCCIÓN MODELO NUMÉRICO**

**2.1** **Aspectos Generales**

Para el desarrollo del modelo numérico del SHAC de Punitaqui, se ha seleccionado el software _Groundwater_
_Vistas versión 8.30 Build 76_, debido a que presenta ventajas comparativas y flexibilidad para la elaboración
de modelos conceptuales, que permiten construir modelos numéricos en tres dimensiones de manera simple
y eficiente. Este software se encuentra recomendado en la “Guía para el uso de modelos de aguas
subterráneas en el SEIA” (SEA, 2012) para realizar modelos hidrogeológicos aplicados a la mayoría de los
problemas presentes en Chile.

Para resolver el problema de flujo y representar las complejidades hidrogeológicas del SHAC de Punitaqui, se
ha seleccionado el motor de cálculo MODFLOW USG, debido a que permite trabajar con grillas no
estructuradas. La flexibilidad en el tamaño de la grilla permite enfocar la resolución del problema en representar
adecuadamente los pozos de bombeo, de monitoreo y poner énfasis en zonas de interés, como la quebrada
Los Mantos o el sector El Ciénago.

MODFLOW USG, es basado en el método numérico de volúmenes finitos y además usa opcionalmente
Newton Raphson, basado en MODFLOW NWT, para mejorar la convergencia de la solución, resolviendo el
problema de secado y re-humedecimiento de las celdas. También se incorpora el solver SMS (Sparse Matrix
Solver Package), que provee varios métodos para resolver las no-linealidades de la matriz proveniente de las
expresiones de flujo y de la formulación de Newton Raphson.

El modelo numérico actualizado posee como base la información de la caracterización hidrogeológica
presentada en el Anexo 2.9 de la DIA, así como las series de recarga junto con las de bombeo de pozos de

extracción del modelo PEGH hasta el año 2019.

Debido a los cambios incluidos en el modelo, este fue recalibrado, ajustando los parámetros hidrogeológicos
de manera de cumplir con los criterios establecidos en la guía para uso de modelos hidrogeológicos en el SEIA
(SEA, 2012).

**2.2** **Dominio y Geometría**

El dominio del modelo numérico fue definido a partir de la delimitación del Sector Hidrogeológico de
Aprovechamiento Común (SHAC) Punitaqui que se presenta en la Figura 1-2.

El techo o superficie del sistema hidrogeológico a modelar corresponde al nivel de terreno, el cual se obtuvo
desde un modelo de elevación digital _Alos Palsar_ Región de Coquimbo. En la Figura 2-1 se presenta el dominio
y mapa de elevaciones del modelo numérico.

_______________________________________________________________________________________
Rev. B / 17.03.2025 1

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 2-1: Dominio y elevaciones de modelo numérico**

_Fuente: Elaboración propia._

La discretización en vertical considera tres (3) capas, de manera de representar las unidades hidrogeológicas
del acuífero cuando se requiera, es decir, una capa para representar principalmente a los depósitos no
consolidados, las arcillas o finos que definen el acuitardo y la roca fracturada. Los espesores de cada una de
estas capas se obtuvieron a partir de perfiles geológicos, información de la estratigrafía de pozos del sector y
de la interpretación de perfiles geofísicos según se presentó en el Anexo 2.9 de la caracterización
hidrogeológica (HIDROMAS, 2024).

En la Figura 2-2 se presenta el perfil L1 en la quebrada Los Mantos, cuyos espesores varían entre 40 y 70 m,
y donde se destaca la presencia de la unidad de roca fracturada en la zona inferior, representada en la capa

3 del modelo numérico.

Del mismo modo, en la Figura 2-3 se presenta el perfil C3 en el sector El Ciénago, en esta zona se identifica
la UH1b del acuitardo detrítico, representado en la capa 1 del modelo numérico, por debajo de esta unidad se
encuentra el acuífero principal localizado en la capa 2 y finalmente la roca fracturada de la capa 3. Los
espesores son variables, pero la capa 1 que representa el acuitardo tiene un espesor medio de 50 m
aproximadamente.

Finalmente, para efectos de la presente actualización se desarrolló un perfil adicional denominado N-S que
cruza el sector Norte del SHAC desde el río Limarí hasta el sector de El Ciénago, atravesando el estero
Punitaqui. En este perfil se observa que la capa del acuitardo sigue presente, abarcando gran parte del SHAC

_______________________________________________________________________________________
Rev. B / 17.03.2025 2

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

Punitaqui, con excepción del lecho del estero Punitaqui. En esta sección se mantiene en la capa 1 del modelo
la unidad asociada al acuitardo, la capa 2 el acuífero y la capa 3 la roca fracturada.

**Figura 2-2: Perfil L1 Los Mantos**

_Fuente: Elaboración propia._

**Figura 2-3: Perfil C3 sector El Ciénago**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 3

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 2-4: Perfil N-S sector El Ciénago**

_Fuente: Elaboración propia._

Adicionalmente, para caracterizar la profundidad del basamento en sectores del SHAC sin información, se
utilizó el estudio del SERNAGEOMIN (2019) donde se realizó una estimación de la profundidad del basamento
en el contexto regional, de manera de cuantificar el espesor del relleno. Esta información fue considerada
como referencial en sectores sin información, mientras que en sectores con datos levantados fue considerada
como una segunda prioridad. En la Figura 2-5 se presenta la profundidad del basamento estimada para el

modelo numérico.

Se observa de la figura que, en la quebrada Los Mantos los espesores del relleno varían entre 50 y 100 m
aproximadamente, siendo consistentes con la información levantada a partir de campañas geofísicas. Del
mismo modo, en El Ciénago existen sectores con mayor potencia, alcanzando valores que superan los 300
m, condición que se observa en el sector norte del estero Punitaqui, con espesores que superan los 200 m.

Esta definición de la potencia del acuífero permite estimar con menor incertidumbre las componentes
geométricas del sistema, ya sean secciones pasantes o volumen almacenado, de manera de que la
herramienta numérica es capaz de representar adecuadamente la dinámica del sistema hidrogeológico.

_______________________________________________________________________________________
Rev. B / 17.03.2025 4

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 2-5: Espesor del Acuífero**

_Fuente: Elaboración propia._

**2.3** **Representación Temporal en Modelo Hidrogeológico**

El modelo numérico del SHAC Punitaqui, considera un régimen transiente a escala mensual, desde abril de
1990 hasta junio del 2025, con un total de 423 períodos de simulación. La condición inicial fue generada a
partir de datos del nivel estático en distintos pozos con expedientes que datan la información de construcción.

**2.4** **Definición de la Grilla de Modelación**

Para la construcción del modelo numérico, se ha definido una grilla de tipo no estructurada, basada en el
método _Quadtree_, que permite generar grillas muy refinadas en sectores de interés o que requieran un mayor
detalle en la solución del problema numérico como en los pozos de monitoreo de nivel de aguas subterráneas,
unidad hidrogeológica del relleno sedimentario y en las zonas de relevantes del proyecto como en la quebrada
Los Mantos y El Ciénago.

La discretización adoptada en el modelo numérico se describe a continuación:

 - 300 m x 300 m: Se define como el máximo tamaño de celda de la grilla definida. Este tipo de elementos
se encuentran en sectores más alejados de las zonas de interés. Equivale al tamaño de la grilla del

modelo PEGH.

 - 150 m x 150 m: Relleno sedimentario cercano a zonas de interés.

_______________________________________________________________________________________
Rev. B / 17.03.2025 5

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

 - 75 m x 75 m: Corresponde al menor tamaño de celda, en donde la grilla posee su mayor refinamiento.
Este tipo de elemento se encuentra en los pozos monitoreo y en los sectores de Los Mantos y El
Ciénago.

La Figura 2-6 muestra la grilla utilizada en el modelo numérico, en donde se presenta una vista general de
todo el dominio de modelación, además de un acercamiento a la zona de interés, de manera de mostrar el

refinamiento de la grilla en estos sectores.

**Figura 2-6: Grilla de Modelación y Acercamiento en Zona de Interés con refinamiento** _**Quadtree**_

_Fuente: Elaboración propia desde Groundwater Vistas._

_______________________________________________________________________________________
Rev. B / 17.03.2025 6

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**3** **ESTIMACIÓN DE LA RECARGA**

**3.1** **Aspectos Generales**

La principal entrada al sistema hidrogeológico corresponde a la recarga. Esta componente fue estimada en el
modelo PEGH (DGA-Hídrica Consultores, 2020) mediante la herramienta de modelación superficial WEAP,
generando una serie de recarga mensual por SHAC hasta el año 2019. En la actualización hecha en el del
modelo base GCF (2015), en el marco del desarrollo del modelo PEGH, se modificaron las zonas de recarga
asociándolas a los SHACs de la cuenca, con el objetivo de que los flujos fueran integrados directamente desde
WEAP a Groundwater Vistas. Las zonas de recarga asociadas a los SHACs de la cuenca se presentan en la
Figura 3-1.

En la presente actualización se considera la serie de recarga mensual hasta el año 2019 del SHAC Punitaqui
determinada por el modelo PEGH, la cual se consideró como una magnitud por año hidrológico, para
representar de mejor manera la variación que se observa en los niveles de agua subterránea del acuífero.

**Figura 3-1: Zonas de Recarga del Modelo PEGH**

_Fuente: Elaboración propia a partir de modelo PEGH (DGA - Hídrica Consultores, 2020)._

_______________________________________________________________________________________
Rev. B / 17.03.2025 7

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**3.2** **Actualización de la Recarga**

Para actualizar la serie de recarga desde el año 2019 hasta 2025, se correlacionó la información de esta
variable con la precipitación anual registrada en la estación pluviométrica Punitaqui de la red
hidrometeorológica de la Dirección General (“DGA”).

3.2.1 Relleno de información pluviométrica estación Punitaqui

Para obtener la serie completa de precipitación de la estación Punitaqui se realizó un relleno de datos a partir
de correlación con estaciones cercanas. En la Tabla 3-1 se presenta la información relevante de las estaciones
utilizadas en el presente análisis y en

Figura 3-2 se ilustra la distribución espacial de las estaciones DGA. La información pluviométrica considerada
se presenta en el Apéndice A de este informe.

**Tabla 3-1: Información de las Estaciones Relevantes para el Estudio**

|Estación|Código BNA|Coordenada Este (m)|Coordenada Norte<br>(m)|Período con<br>información|
|---|---|---|---|---|
|Punitaqui|4555001|284.077|6.586.719|1990 - 2020|
|La Placilla|4554003|278.631|6.579.522|1990 - 2020|
|Ovalle DGA|4551005|288.294|6.612.196|1990 - 2024|

_Fuente: Elaboración propia._

**Figura 3-2: Ubicación Estaciones Meteorológicas de la DGA**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 8

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

La serie de precipitación de la estación Punitaqui fue rellenada hasta julio del 2020 a partir de la estación base
de La Placilla, estableciendo entre ambas una correlación con coeficiente R2 de 0,91. Desde julio del 2020 a

diciembre del 2024 se utilizó la información de la estación Ovalle DGA con una correlación directa con

Punitaqui con coeficiente R2 de 0,89, la cual se reporta en los Boletines Hidrológicos (DGA, 2025).

De esta forma se genera la serie de precipitación anual de la estación Punitaqui, la cual se presenta Figura
3-3. De la figura se observa que, la precipitación varía entre 12 mm y 510 mm, siendo este último valor
alcanzado durante el año 1997. De la serie se calculó un valor promedio de 138 mm.

**Figura 3-3: Serie Precipitación Anual Estación Punitaqui**

_Fuente: Elaboración propia._

3.2.2 Correlación recarga - precipitación

Con la serie de precipitación completa desde el año 1990 a 2024 de la estación Punitaqui, se verifica el nivel
de correlación con la serie de recarga obtenida desde el modelo PEGH (DGA - Hídrica, 2020) desde 1990 a
2019. En la Figura 3-4 se presenta el gráfico de correlación de ambas series, de la cual se observa que poseen
una correlación directa con coeficiente R2 de 0,85, indicando un buen ajuste entre las variables.

A partir de esta relación, se extendió la recarga desde 2019 a 2024 a partir de la precipitación anual de
Punitaqui, generando la serie presentada en la Figura 3-5 que varía entre 12 mm/año y 284 mm/año, con un
promedio de 116 mm/año. Los valores más altos responden a años hidrológicos de mayor precipitación, y
viceversa, en donde los años secos poseen los menores valores de recarga. Esta serie anual es la que se
ingresa al modelo numérico mediante el paquete RECH de MODFLOW.

_______________________________________________________________________________________
Rev. B / 17.03.2025 9

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 3-4: Correlación entre Recarga Modelo PEGH y Precipitación Anual Punitaqui**

600

550

500

450

400

350

300

250

200

150

100

50

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||y = 0.<br>R|50x +<br>2 = 0.|47.15<br>85||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||

0 50 100 150 200 250 300 350 400 450 500 550 600

Precipitación anual Punitaqui (mm)

_Fuente: Elaboración propia._

**Figura 3-5: Serie de Recarga Anual rellenada en Dominio de Modelación**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 10

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

3.2.3 Distribución espacial de la recarga

Para la distribución de la recarga dentro del dominio de modelación que corresponde al SHAC de Punitaqui,
se utilizó la metodología de la DGA según el estudio SDT 276/2009. En este documento se establece que la
recarga producto de la precipitación, se obtiene como la suma de: (1) una recarga lateral (o de piedemonte)
que se produce por la precipitación que cae sobre la roca impermeable o semipermeable (“RL”) y (2) una
recarga directa dada por la precipitación que cae sobre los depósitos sedimentarios (“RD”).

En la Figura 3-6 se presenta la distribución espacial de las zonas de recarga directa y recarga lateral, las
cuales fueron determinadas en función de la distribución de las unidades hidrogeológicas UH1 depósitos
fluviales o aluviales y la UH3 basamento impermeable.

Debido a las características de recibir y transmitir la recarga, la mayor parte de la recarga se distribuye en los
depósitos aluviales o fluviales que representan la zona de Recarga Directa, mientras que el menor porcentaje
se recibe como una Recarga lateral. En la Figura 3-7 se presenta la serie de caudal de recarga distribuido por

zonas.

**Figura 3-6: Zonas de Recarga Directa y Lateral**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 11

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 3-7: Serie de Caudal de Recarga Distribuida en Zonas**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 12

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**4** **POZOS DE EXTRACCIÓN Y PROPIEDADES HIDROGEOLÓGICAS**

**4.1** **Información sobre Pozos de Bombeo**

Dentro del SHAC Punitaqui el modelo PEGH (DGA-Hídrica, 2020) determinó un total de 1552 pozos de
extracción, los cuales poseen serie de bombeo a escala mensual hasta diciembre del año 2018. La distribución
espacial de estos pozos se presenta en la Figura 4-1. Adicionalmente, en la Figura 4-2 se presenta la serie
mensual de caudales de extracción, en donde desde 2019 a 2024 se replicó el último año generado desde el

modelo PEGH.

**Figura 4-1: Ubicación Espacial de Pozos de Extracción Dentro del Dominio**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 13

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 4-2: Serie de Caudal de Extracción de Pozos de Bombeo**

_Fuente: Elaboración propia._

**4.2** **Unidades Hidrogeológicas y Propiedades Hidráulicas**

En el área de estudio se han definido las siguientes unidades hidrogeológicas:

- **UH1: Unidades sedimentarias**

Esta unidad corresponde a la principal formación acuífera del área de interés. Se encuentra normalmente
sobre niveles de roca fracturada (UH2) o directamente sobre el basamento impermeable (UH3), presentando
resistividades en zonas saturadas entre 1 y 42 Ohm-m (Tabla 4-1). Tiene un espesor variable, entre 10 y 50
m en la Quebrada Los Mantos; y entre 100 m y 220 m en el sector El Ciénago. De acuerdo con las unidades
geológicas del área de estudio, se puede dividir en tres subcategorías, las cuales se describen a continuación:

`o` UH1A Depósitos aluviales y fluviales actuales

Litológicamente está conformada por gravas monomícticas gruesas sin estratificación, abundantes arenas
bien estratificadas y limos. Sus clastos presentan buen redondeamiento y esfericidad regular y están
formados por fragmentos de rocas intrusivas, volcánicas y sedimentarias. Presenta una baja compactación
y cementación. Se extiende en superficie sobre casi toda el área de estudio. Estos depósitos conforman
el principal acuífero del valle de la quebrada Los Mantos en la zona de estudio y el relleno superficial del
sector El Ciénago. Esta formación acuífera presenta características freáticas y condiciones
granulométricas que presumen conductividades hidráulicas moderadas.

`o` UH1B Depósitos Aluviales Antiguos

En la quebrada Los Mantos se reconoce principalmente en la zona de tributación al estero Punitaqui.
Corresponde a una unidad sedimentaria medianamente consolidada, de origen continental. Se encuentra
asociada con las unidades geológicas aluviales y fluviales antiguas, miocenas a pleistocenas. Presenta
un grado de compactación elevado y en algunos sectores muestran una cementación incipiente. Sub
superficialmente, estos rellenos se proyectan por debajo de los depósitos aluviales recientes, y se
presentan saturados.

_______________________________________________________________________________________
Rev. B / 17.03.2025 14

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

Localmente, en el sector El Ciénago estos depósitos podrían estar relacionados con capas continuas de
sedimentos finos UH1B(f) junto con unidades acuíferas subyacentes confinadas, esta distinción no es
observada en la quebrada Los Mantos.

Como se observa en la Figura 2-4 los sedimentos finos se han observado en la estratigrafía de diversos
pozos y en estudios geo-eléctricos realizados cercanos al pozo Parcela N°45 en el sector Ciénago, con
un espesor de hasta 60 m. Esta capa de arcilla se extiende hacia el noreste, siendo observada
extensamente también en el perfil TEM L24 realizado por GCF (2015), y es registrada a su vez en la
estratigrafía de otros pozos situados hacia el norte (expedientes ND-0402-178 y ND-0402-182).

`o` UH1C Depósitos Coluviales

Los depósitos coluviales son de origen gravitacional que se encuentran adosados en laderas de cerros
(PlHc). Esta unidad es permeable, y tiene baja potencia (inferior a 20 m) por lo que, si bien capta el agua
proveniente de precipitaciones, su alta pendiente ayuda a transmitir el agua captada hacia otras unidades
acuíferas con mayor capacidad de almacenar el agua subterránea debido a su mayor espesor relativo y
menor gradiente hidráulico (unidades fluviales y aluviales). Normalmente, estas unidades se encuentran

secas.

- **UH2: Roca Fracturada**

Esta unidad se observa en sub-superficie en las secciones hidrogeológicas a partir de la información litológica
y geofísica, normalmente bajo los niveles de la UH1. Presenta valores de resistividad entre 25 y 150 Ohm-m
(Tabla 4-1). Presenta un espesor entre 10 m y 50 m en la quebrada Los Mantos, mientras que en el sector El
Ciénago se estiman espesores de hasta 150 m. Esta unidad se observa con una continuidad acotada, a veces
en contacto lateral con áreas del Basamento Impermeable (UH3).

- **UH3: Basamento Impermeable**

Esta unidad tiene una baja a nula capacidad de almacenar y transmitir el agua subterránea por lo que se le
considera los límites laterales y en profundidad de las unidades acuíferas. Presenta los mayores valores de
resistividad, siendo mayores a 150 Ohm-m (Tabla 4-1).

**Tabla 4-1: Resumen Definición Unidades Hidrogeológicas**

|Nombre|Col2|Geología<br>Superficial|Litología de<br>Pozos|Unidad de<br>Resistividad<br>(Ohm-m)|Transmisividad<br>Representativa (m2/d)|
|---|---|---|---|---|---|
|UH1|Aluvial y fluvial actual|Hf|Gravas y arenas<br>con bajo contenido<br>de limo o arcilla<br>(<15%)|1 a 42|5,0 - 514,9|
|UH1|Aluvial y fluvial Antiguo|PlHf, PlHa, Pla,<br>MPc|Gravas y arenas<br>con predominio de<br>contenido de<br>arcilla|Gravas y arenas<br>con predominio de<br>contenido de<br>arcilla|Gravas y arenas<br>con predominio de<br>contenido de<br>arcilla|
|UH1|Coluviales|PlHc|S/I|S/I|S/I|
|UH2: Roca Fracturada|UH2: Roca Fracturada|JKas, JsKip,<br>Kim, Kiqm Ksh,<br>Kip, Kia|Roca Alterada o<br>Fracturada|27 a 150|13,0 - 26,3|
|UH3: Basamento Impermeable|UH3: Basamento Impermeable|UH3: Basamento Impermeable|Roca Sana|> 150|No Aplica|

_Fuente: Elaboración propia a partir de CPH (2014) y análisis presentado en acápite 4.4.2._

_______________________________________________________________________________________
Rev. B / 17.03.2025 15

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

En la Figura 4-3 se presenta la representación de las UH en el modelo numérico en la capa 1 donde se observa
que la UH3 representa la mayoría de la superficie expuesta, siendo predominante hacia los sectores sur y

sureste.

Por otro lado, en la Tabla 4-1 se presenta la relación de las unidades hidrogeológicas con la geología
superficial, las unidades geo-eléctricas a partir de las secciones NanoTEM, la litología de pozos y los valores
de transmisividad estimados en las distintas pruebas de bombeo.

Es importante mencionar que los rangos de transmisividad asociados a las unidades UH1 y UH2 (Tabla 4-1)
se basan en la información recopilada a nivel más específico cercano a los sectores de interés del Proyecto,
por lo que son más bien representativas de dichos sectores y no necesariamente del SHAC completo.

**Figura 4-3: Representación de Unidades Hidrogeológicas en Modelo Numérico**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 16

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**5** **PROCESO DE CALIBRACIÓN Y AJUSTE**

**5.1** **Ajuste de niveles**

Este proceso tiene como objetivo ajustar los parámetros hidrogeológicos del sistema, de manera de
representar los niveles de aguas subterráneas medidos en las unidades acuíferas, como también ajustar de

manera adecuada el balance hídrico del sistema.

Para lograr el ajuste en régimen transitorio, se utilizó la metodología de zonificación para los parámetros de
conductividad hidráulica, y coeficiente de almacenamiento en base a los rangos definidos conceptualmente
según la UH y condición del acuífero respectivo.

En total se cuenta con 12 pozos de observación, con registros de niveles de aguas subterránea, con distinta
extensión temporal de datos, entre 1990 y 2024. La distribución espacial se muestra en la Figura 5-1.

**Figura 5-1: Ubicación Pozos de Observación para Calibración de Modelo Numérico**

_Fuente: Elaboración propia._

De los 12 pozos considerados, se cuenta con 1563 datos de nivel de aguas subterráneas, y con los niveles
simulados por el modelo numérico, se calculó un error medio absoluto (“MAE” por sus siglas en inglés) de 3,4
m y un error cuadrático medio de 4,9 m, que, al normalizarlos según el rango de niveles observados, se obtiene
un NMAE de 3,3% y un NRMS 4,7%. Estos niveles de ajuste obtenidos se encuentran por debajo del 5%
recomendado por la Guía Para el Uso de Modelos de Aguas Subterráneas en el SEIA (SEA, 2012).

_______________________________________________________________________________________
Rev. B / 17.03.2025 17

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

El ajuste de niveles observados y calculados se presenta la Figura 5-2 en conjunto con los estadísticos de
ajuste obtenidos del proceso de calibración. Adicionalmente, en la Figura 5-3 se presenta el histograma de
residuales, donde se observa que, los residuales están contenidos -20 m y 20 m, donde cerca del 70% se
encuentra dentro -5 m y 5 m, mostrando el buen ajuste del modelo numérico.

**Figura 5-2: Niveles Observados versus Niveles Calculados por el Modelo Numérico**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 18

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-3: Histograma de Residuales**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 19

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**5.2** **Hidrogramas de Niveles**

5.2.1 Pozos DGA

Como parte de los resultados del modelo numérico, se presentan los hidrogramas de niveles de agua
subterránea de los pozos de observación presentes en el SHAC, que se presentaron en la Figura 5-1.

En la Figura 5-4 se presenta el hidrograma del pozo AP Punitaqui, ubicado en el relleno fluvial del estero
Punitaqui, aguas abajo de la confluencia con la quebrada Los Mantos. Este pozo muestra niveles relativamente
estables con una leve tendencia al descenso en el tiempo. Comportamiento similar se observa en el pozo
Asentamiento Graneros, ubicado aguas abajo del centro urbano de Punitaqui, siguiendo el relleno fluvial del
estero, tal como se presenta en la Figura 5-5.

En el sector al norte del estero Punitaqui, el pozo Asentamiento Nogales registró mediciones fuertemente
influenciadas por los bombeos cercanos, con un fuerte descenso a partir del año 2012. Debido a la
incertidumbre en las extracciones de los pozos de bombeo, el modelo no refleja estos efectos dinámicos, sin
embargo, el orden de magnitud del nivel se ajusta adecuadamente, como se presenta en la Figura 5-6.

En la Figura 5-7 se presenta el pozo Asentamiento Campo Lindo el cual muestra un comportamiento estable
en el tiempo. Finalmente, en la Figura 5-8 y Figura 5-9 se presentan la serie de los pozos Asentamiento Unión
Campesina y Asentamiento Nueva Aurora respectivamente. Ambos se ven fuertemente influenciados por los
bombeos cercanos y debido a la incertidumbre en la estimación de esta componente, el modelo numérico
representa parcialmente las tendencias.

5.2.2 Pozos Monitoreado BMR

Además de los pozos de monitoreo de la red DGA, se cuenta con 6 pozos en la quebrada Los Mantos que son
monitoreados por BMR. Si bien, se dispone de datos solamente desde el año 2024, esta información fue
utilizada para ajustar los niveles actuales del acuífero.

Desde la Figura 5-10 a la Figura 5-15 se presentan las series de niveles de aguas subterráneas simuladas a
lo largo de la quebrada los Mantos. Se observa que la tendencia general es de un descenso sostenido en el
tiempo, empalmando en el año 2024 en el orden de magnitud de los valores medidos en cada uno de los
pozos monitoreados.

_______________________________________________________________________________________
Rev. B / 17.03.2025 20

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-4: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA AP Punitaqui**

_Fuente: Elaboración propia._

**Figura 5-5: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Graneros**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 21

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-6: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Nogales**

_Fuente: Elaboración propia_

**Figura 5-7: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Campo Lindo**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 22

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-8: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. U. Campesina**

_Fuente: Elaboración propia._

**Figura 5-9: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo DGA As. Nueva Aurora**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 23

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-10: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Rancho 1**

_Fuente: Elaboración propia._

**Figura 5-11: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Rancho 3**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 24

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-12: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Rancho 5**

_Fuente: Elaboración propia._

**Figura 5-13: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Nuevo 1**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 25

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-14: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Nuevo 2**

_Fuente: Elaboración propia._

**Figura 5-15: Serie temporal de Nivel Piezométrico Simulado y Medidos, Pozo Los Mantos**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 26

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**5.3** **Equipotenciales y Direcciones de Flujo**

Como resultado del modelo numérico, se obtiene la distribución de niveles piezométricos en todo el dominio
de estudio. Con esta información se determinan direcciones de flujo, gradientes hidráulicos y su evolución en
el tiempo.

En la Figura 5-16 se presenta el mapa de equipotenciales calculado por el modelo numérico para enero del
año 2000, se agrega en la figura las equipotenciales estimadas conceptualmente para el mismo año y
presentadas en el Anexo 2.9 de la DIA (HIDROMAS, 2024). De la figura se observa que existe una dirección
principal de flujo que sigue el sentido del estero Punitaqui y de las quebradas y esteros aportantes a este.

En la Figura 5-17 se presentan las equipotenciales para el año 2024 (las del modelo numérico y las
conceptuales), de manera de ver la variación en el tiempo con respecto a la condición del año 2000. De la
figura mencionada se observa que, existe un efecto de expansión del cono de descenso alrededor de los
pozos de bombeo, ya que se pasó de promedio de 100 L/s en el año 2000 a casi 500 L/s de extracción
promedio en 2024.

Para mayor detalle y analizar la evolución en el tiempo de las direcciones de flujo, se realizó un acercamiento
de las equipotenciales (del modelo numérico) en el sector de El Ciénago, como se muestra en la Figura 5-18.
De ésta, se observa que, en el año 2000 cuando los bombeos eran muy bajos, la dirección de flujo era desde
el sur hacia el nor-oeste. Mientras que, en el año 2024, se generó un cono de depresión del nivel piezométrico,
producto de las extracciones continuas en el sector, generando que la dirección de flujo se modificara, hacia
la ubicación de los pozos de bombeo.

De esta forma, se observa que, debido al bombeo histórico del sector, la dinámica de flujo ha sido modificada,
cambiando patrones de flujo, de manera de que los flujos pasantes han modificado su dirección en función de
suplir la extracción desde los pozos de bombeo.

_______________________________________________________________________________________
Rev. B / 17.03.2025 27

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-16: Mapa de Equipotenciales para Enero del Año 2000**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 28

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.DIA

PROYECTO LOS MANTOS

**Figura 5-17: Mapa de Equipotenciales para Junio del Año 2024**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 29

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

**Figura 5-18: Mapa de Equipotenciales Sector El Ciénago**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 30

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

**5.4** **Balance Hídrico**

Con respecto al balance hídrico del SHAC Punitaqui, se identifica como principal entrada la recarga, la cual
varía entre 40 L/s y 964 L/s. Las salidas corresponden a afloramientos en los esteros y quebradas, además
de los pozos de extracción, que varían entre 407 y 1.429 L/s. La serie temporal de cada una de estas
componentes se presenta en la Figura 5-19.

De la figura se observa que, en términos generales, las salidas del sistema superan a las entradas en
prácticamente todo el período de análisis, con excepción de los años hidrológicos más lluviosos, como lo
fueron 1997 y 2002. De esta forma, para el cierre del balance hídrico, y poder suplir las salidas por
afloramientos y extracciones, se consume parte del volumen almacenado en el acuífero.

**Figura 5-19: Serie Temporal de las Componentes del Balance Hídrico del Sistema**

_Fuente: Elaboración propia._

_______________________________________________________________________________________
Rev. B / 17.03.2025 31

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

**6** **CONCLUSIONES**

Según lo descrito en todos los acápites anteriores, se puede comentar lo siguiente:

- Se desarrolló un modelo numérico que incorpora la caracterización hidrogeológica específica para los dos

sectores de interés del Proyecto: Los Mantos y El Ciénago realizada en el marco de la DIA del proyecto.

- En particular se construyó la geometría del modelo numérico de manera de representar adecuadamente la

potencia de las unidades hidrogeológicas presentes en el SHAC en función de información de campañas
geofísicas y de estratigrafía de pozos. Se puso énfasis en representar con mayor nivel de detalle los
sectores de Los Mantos y El Ciénago.

- El modelo numérico cumple con los ajustes recomendados en la “Guía para uso de modelos de aguas

subterráneas en el SEIA” (SEA, 2012), con un error medio absoluto normalizado (NMAE) de 3,3%, menor
al 5% recomendado en dicha guía. Además, se observa que se representan las tendencias históricas de
los pozos y los niveles piezométricos simulados se ajustan a los valores medidos. Sin embargo, es
importante señalar que, debido a la incertidumbre de las extracciones de terceros, los efectos dinámicos
observados en algunos pozos de observación dificultan un ajuste mayor.

- Con respecto al balance hídrico del sistema, la principal recarga del sistema proviene de la precipitación

en sectores altos, la cual no es suficiente para cumplir con la demanda de derechos de agua, de esta forma
existe una parte del consumo que es proveniente del volumen almacenado.

- El modelo numérico se considera como una herramienta válida y adecuada para su uso en evaluación de

posibles efectos relacionados al proyecto.

_______________________________________________________________________________________
Rev. B / 17.03.2025 32

INFORME TÉCNICO
ACTUALIZACIÓN MODELO HIDROGEOLÓGICO SHAC PUNITAQUI.

DIA PROYECTO LOS MANTOS

**7** **REFERENCIAS**

- ASTM D5447-17, 2018. Standard Guide for Application of a Numerical Groundwater Flow Model to a SiteSpecific Problem.

- Bureau of Mining Regulation and Reclamation, 2020. Guidance for Hydrogeologic Groundwater Flow
Modeling at Mine Sites.

- British Columbia, 2012. Guidelines for Groundwater Modelling to Assess Impacts of Proposed Natural
Resource Development Activities.

- Panday, Sorab, Langevin, C.D., Niswonger, R.G., Ibaraki, Motomu, and Hughes, J.D., 2017, MODFLOWUSG version 1.4.00: An unstructured grid version of MODFLOW for simulating groundwater flow and tightly
coupled processes using a control volume finite-difference formulation: U.S. Geological Survey Software
Release, 27 October 2017, https://dx.doi.org/10.5066/F7R20ZFJ

- Sea, 2012. Guía para el uso de modelos de aguas subterráneas en el SEIA.

- SERNAGEOMIN, 2019. Geometría de la cuenca del río Limarí región de Coquimbo.

- DGA - Hídrica Consultores (2020). Plan Estratégico De Gestión Hídrica En La Cuenca De Limarí.

- Ilustre Municipalidad de Punitaqui - PAC Consultores Ltda. (2011). Caracterización y Diagnóstico Comunal
Plan de Desarrollo Comunal 2011-2016. Etapa I. Tomo I.

- Ilustre Municipalidad de Punitaqui (2018). Actualización PLADECO 2018-2023.

- Hidromas, 2024. Caracterización Hidrogeológica SHAC Punitaqui DIA Proyecto Los Mantos.

_______________________________________________________________________________________
Rev. B / 17.03.2025 33