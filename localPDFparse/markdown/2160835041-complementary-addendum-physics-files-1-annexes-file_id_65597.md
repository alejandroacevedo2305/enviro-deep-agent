---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA COMPLEMENTARIA DECLARACIÓN DE IMPACTO AMBIENTAL “SUBESTACIÓN QUEPE 220/66 KV”
-->

# ADENDA COMPLEMENTARIA DECLARACIÓN DE IMPACTO AMBIENTAL “SUBESTACIÓN QUEPE 220/66 KV”

## ANEXO 1.6: MODELACIÓN HIDRÁULICA

Elaborado para:

Región de La Araucanía

Marzo, 2025

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

### CONTENIDO

1 INTRODUCCIÓN ..................................................................................................................................... 3

1.1 OBJETIVO ....................................................................................................................................... 3

2 REFERENCIAS ......................................................................................................................................... 3
3 DESCRIPCIÓN GENERAL Y BASES DE CÁLCULO ...................................................................................... 4

3.1 Definiciones ................................................................................................................................... 4

3.2 Datos .............................................................................................................................................. 4

3.2.1 Coordenadas del sitio de interés y límite predial .................................................................. 4

3.2.2 Caudales máximos instantáneos ........................................................................................... 4

3.2.3 Condición natural del cauce para el análisis de la condición sin proyecto ........................... 4
3.2.4 Topografía del sector ............................................................................................................. 5

3.3 Criterios de evaluación .................................................................................................................. 6

3.4 Supuestos ...................................................................................................................................... 6
4 METODOLOGÍA ...................................................................................................................................... 6

4.1 Generalidades ................................................................................................................................ 6

4.2 Descripción del modelo HEC-RAS .................................................................................................. 7
4.3 Coeficiente de rugosidad ............................................................................................................... 7

4.4 Condiciones de borde .................................................................................................................... 9

5 RESULTADOS ....................................................................................................................................... 10

6 CONCLUSIONES ................................................................................................................................... 12
ANEXO 1: POLÍGONO DE SERVIDUMBRE SUBESTACIÓN QUEPE ................................................................. 13
ANEXO 2: REGISTRO FOTOGRÁFICO ............................................................................................................ 16
APÉNDICE A: RESULTADOS EJES HIDRÁULICOS ........................................................................................... 21
APÉNDICE B: ARCHIVO “KMZ” POLÍGONOS DE INUNDACIÓN .................................................................... 28
APÉNDICE C: ARCHIVOS DE ENTRADA HEC-RAS .......................................................................................... 29

## TABLAS

Tabla 3-1: Definiciones y Abreviaciones ........................................................................................................ 4

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Las unidades por utilizar en el presente documento serán del Sistema Internacional de Unidades (SI). Se utilizará punto (.) como separador de miles y coma (,) como separador de decimales. Las definiciones o abreviaturas consideradas son: -->

**Tabla 3-1: Definiciones y Abreviaciones****

| Término Definición | Col2 |
| --- | --- |
| msnm<br>Metros sobre el nivel del mar | msnm<br>Metros sobre el nivel del mar |
| SI<br>Sistema Internacional de Unidades | SI<br>Sistema Internacional de Unidades |
| T <br>Período de Retorno (años) | T <br>Período de Retorno (años) |
| USACE<br>United States Army Corps of Engineers (Cuerpo de Ingenieros del Ejército de los Estados<br>Unidos) | USACE<br>United States Army Corps of Engineers (Cuerpo de Ingenieros del Ejército de los Estados<br>Unidos) |
| Cauce natural<br> | Según ARTICULO 30° de la Ref. [1] “Álveo o cauce natural de una corriente de uso público es<br>el suelo que el agua ocupa y desocupa alternativamente en sus creces y bajas periódicas.” |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Con relación a la definición cauce natural resulta necesario realizar una evaluación de los márgenes del cauce sobre la base de información histórica, dadas las características hidráulicas del cauce (régimen subcrítico), y la morfología del sector. -->
<!-- FIN TABLA 3-1 -->


Tabla 3-2: Caudales máximos instantáneos - Estero Pelales en sitio de interés .......................................... 4

Tabla 3-3: Sección inferida Estero Pelales en condición natural ................................................................... 5

Tabla 4-1: Coeficientes de Manning para fórmula de Cowan (Tabla 3.707.104.B, Ref.[9]) .......................... 8
Tabla 4-2: Estimación de coeficiente de rugosidad de Manning .................................................................. 8
Tabla 4-3: Condiciones de borde modelación hidráulica - Cruce 1, Estero El Sauce .................................... 9

<!-- INICIO TABLA 4-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 4-3 se presentan las condiciones de borde consideradas en las simulaciones hidráulicas. Al estar sustentado en un supuesto (ver punto 3.4) los resultados en las cercanías de los bordes son sólo referenciales. -->

**Tabla 4-3: Condiciones de borde modelación hidráulica - Cruce 1, Estero El Sauce****

| Aguas arriba Aguas abajo | Col2 |
| --- | --- |
| Altura normal<br>S=0,17% | Altura normal<br>S=0,17% |

<!-- Estadísticas: 1 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 240923-000-HI-MDC-001_R0.docx 9 de 29 MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO -->
<!-- FIN TABLA 4-3 -->

Tabla 6-1: Resumen de resultados, Estero Pelales en sitio Subestación Quepe ......................................... 12

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 2) En la siguiente tabla se resumen los resultados más relevantes de la modelación en HEC-RAS en torno al sitio de la subestación (PK 500 a 1200): -->

**Tabla 6-1: Resumen de resultados, Estero Pelales en sitio Subestación Quepe****

| Variable Unidad T=10 T=100<br>Años años | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9 | Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9 | Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9 | Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9 |
| Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6 | Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6 | Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6 | Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6 |
| Ancho superficial prom. - Cond. Natural sin proy. | [m] | 25,8 | 59,7 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 3) Del análisis expuesto queda demostrado que el emplazamiento del proyecto de subestación Quepe, queda fuera del cauce natural. -->
<!-- FIN TABLA 6-1 -->


## FIGURAS

Figura 3-1: Perfil longitudinal del cauce en condición natural ...................................................................... 5
Figura 4-1: Planta perfiles transversales modelo hidráulico -Estero Pelales en sitio de interés .................. 7
Figura 5-1: Área de inundación - Condición natural sin proyecto, Estero Pelales en sitio de interés ........ 10
Figura 5-2: Perfil longitudinal - Condición natural sin proyecto, Estero Pelales en sitio de interés ........... 11
Figura 5-3: Velocidades medias - Condición natural sin proyecto, Estero Pelales en sitio de interés [ 1] ...... 11

240923-000-HI-MDC-001_R0.docx 2 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### 1 INTRODUCCIÓN

El presente trabajo, desarrollado por solicitud de Besalco Energía Renovable (BSER), contempla un estudio
hidrológico e hidráulico complementario para la estimación de escorrentía superficial del Estero Pelales y
su interacción con el sitio del proyecto de la Subestación Eléctrica Quepe, la que se proyecta al sur de la
localidad del mismo nombre, Región de La Araucanía.

Este estudio viene a complementar el ya presentado por BSER en la Adenda de la DIA del proyecto con la
finalidad de corregir información sobre la base de antecedentes disponibles y que no fueron presentados

en dicha Adenda.

El propósito central de este estudio complementario es obtener los márgenes de crecida para la situación
con y sin proyecto para los caudales máximos instantáneos asociados a eventos de periodo de retorno
T=2, 10, 20, 50 y 100 años, con la finalidad de que sea utilizado por BSER para asegurar que las estructuras
proyectadas no se vean afectadas y se encuentren fuera del área de crecida, dando así respuesta a las
observaciones de la autoridad pertinente al respecto.

**1.1** **OBJETIVO**

1) El objetivo de esta memoria es realizar una modelación hidráulica del Estero Pelales a la altura del

proyecto de la Subestación Quepe para la condición natural para caudales de crecidas asociados a
la ocurrencia de períodos de retorno de 2, 10, 20, 50 y 100 años.

#### 2 REFERENCIAS

**[1]** DFL No. 1122/1981 “Código de Aguas”, versión vigente modificada mayo 2024.
https://www.bcn.cl/leychile/navegar?idNorma=5605&idVersion=2024-05-30&idParte=

**[2]** Plano S/N No. “Levantamiento Lidar Fotogramétrico/Topobatimétrico”, Rev.2, DroneLidar,

enero 2025. Enlace:

https://drive.google.com/file/d/18cRUYPQzmRQm5Jc40H7hE7QiUuyQOObW/view?usp=sha
ring

**[3]** Plano No. NSQUEPE-PES-01, Lámina 1 de 4, septiembre 2024 (incluido en el Anexo 1).

**[4]** Plano No. 6141-2017 -01, agregado en fojas 3227 No. 2919 del 2015, 2do CBR de Temuco,
marzo 2024 (incluido en el Anexo 1).

**[5]** Documento No. 240923-000-HD-INF-001 “Informe técnico - Análisis hidrológico
complementario - Proyecto Subestación Quepe”, EVYS, 2025.

**[6]** Plano No. 240923-000-HD-PLA-001_R0 “Análisis de crecidas Estero Pelales - Región de La
Araucanía”, EVYS, marzo 2025.

**[7]** Documento “Informe Final - Estudio hidráulico e hidrológico del Estero Pelales, comuna de
freire, Región de La Araucanía - Capítulo IV Diagnóstico”, Prisma Ingeniería Limitada, DOH,
agosto 2012. Enlace:

 - =
https://drive.google.com/file/d/1k8dJrbIRY yvzJVBQD79WtxZt9XWCRZk/view?usp sharing

**[8]** “HEC-RAS River Analysis System - Hydraulic Reference Manual”, Version 5.0., February 2016.

**[9]** Manual de carreteras Volumen 3 “Instrucciones y criterios de diseño”, Ministerio de obras
públicas de Chile, 2016.

240923-000-HI-MDC-001_R0.docx 3 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### 3 DESCRIPCIÓN GENERAL Y BASES DE CÁLCULO

**3.1** **Definiciones**

Las unidades por utilizar en el presente documento serán del Sistema Internacional de Unidades (SI). Se
utilizará punto (.) como separador de miles y coma (,) como separador de decimales. Las definiciones o

abreviaturas consideradas son:

**Tabla 3-1: Definiciones y Abreviaciones**

|Término Definición|Col2|
|---|---|
|msnm<br>Metros sobre el nivel del mar|msnm<br>Metros sobre el nivel del mar|
|SI<br>Sistema Internacional de Unidades|SI<br>Sistema Internacional de Unidades|
|T <br>Período de Retorno (años)|T <br>Período de Retorno (años)|
|USACE<br>United States Army Corps of Engineers (Cuerpo de Ingenieros del Ejército de los Estados<br>Unidos)|USACE<br>United States Army Corps of Engineers (Cuerpo de Ingenieros del Ejército de los Estados<br>Unidos)|
|Cauce natural<br>|Según ARTICULO 30° de la Ref. [1] “Álveo o cauce natural de una corriente de uso público es<br>el suelo que el agua ocupa y desocupa alternativamente en sus creces y bajas periódicas.”|

Con relación a la definición cauce natural resulta necesario realizar una evaluación de los márgenes del
cauce sobre la base de información histórica, dadas las características hidráulicas del cauce (régimen
subcrítico), y la morfología del sector.

**3.2** **Datos**

**3.2.1** **Coordenadas del sitio de interés y límite predial**

El sitio del proyecto de la Subestación Quepe se encuentra emplazado en una servidumbre dentro del
predio ROL Predial No. 310-409, Lote B-1, Fundo San Carlos, comuna de Freire. Las coordenadas del
polígono de servidumbre de la Subestación y el límite predial con relación al Bien Nacional de Uso Público
(BNUP) se informan en la Ref. [3] y Ref. [4].

**3.2.2** **Caudales máximos instantáneos**

Los caudales máximos instantáneos (QMI) utilizados en la modelación se encuentran respaldados en la
Ref. [5] y se resumen en la siguiente tabla:

**Tabla 3-2: Caudales máximos instantáneos - Estero Pelales en sitio de interés**

**3.2.3** **Condición natural del cauce para el análisis de la condición sin proyecto**

 - Del levantamiento satelital ASTER v3 incluido en la Ref. [6], se desprende que el Estero Pelales
tiene una pendiente promedio de 0,17% en un largo de 4 km centrado en torno al punto de interés,
como se aprecia en la siguiente figura:

240923-000-HI-MDC-001_R0.docx 4 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**Figura 3-1: Perfil longitudinal del cauce en condición natural**

 - De acuerdo con el registro de imágenes satelitales disponibles en Google Earth del año 2003
(imagen 1, Figura 3 2) se observa que en condición natural el cauce del estero Pelales tiene un
ancho promedio en torno a 15m y un ancho en crecidas en torno a 60m (guiado por la marca de
la vegetación arbustiva y arbórea que crece en sus márgenes).

Los resultados presentados en la siguiente tabla son referenciales y se presentan únicamente para
mostrar la razonabilidad de los valores planteados.

**Tabla 3-3: Sección inferida Estero Pelales en condición natural**

**Descripción** **Símbolo** **Unidad** **T=2** **T=10** **T=50** **T=100** **Referencia**

Talud Derecho _t1_ [H:V] 6,000 6,000 6,000 6,000

Talud Izquierdo _t2_ [H:V] 6,000 6,000 6,000 6,000

_**Condición en régimen**_

Altura normal _hn_ [m] 2,288 3,115 3,764 4,070
Área Hidráulica _An_ [m [2] ] 65,729 104,944 141,471 160,430

Radio Hidráulico _Rh_ [m] 1,534 1,984 2,327 2,487

Velocidad Media _vn_ [m/s] 0,3 0,3 0,4 0,4 _vn=Q/An_

No. Froude _Fr_ - 0,07 0,08 0,08 0,08
Energía específica _Bn_ [m] 2,292 3,121 3,772 4,078 _Bn=hn+vn_ _[2]_ _/(2_ - _g)_

**Ancho superficial** _**L**_ **[m]** **42** **52** **60** **64** _**L=W+2hnt**_

**3.2.4** **Topografía del sector**

Para la modelación de la condición natural sin proyecto se utiliza un levantamiento digital obtenido de
Global Mapper, a partir del cual se procesó una topografía a lo largo de un tramo de aproximadamente 3

km del Estero Pelales centrado en el sitio de interés.

.

240923-000-HI-MDC-001_R0.docx 5 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**3.3** **Criterios de evaluación**

Los criterios utilizados para la modelación de crecidas del cauce en estudio son:

 - La modelación se realizará en estado estacionario (caudal constante).

 - Se considerará el caudal máximo instantáneo, asociado a la crecida de 2, 10, 20, 50 y 100 años.

 - Entre perfiles transversales sucesivos se aplican valores para los coeficientes de contracción y
expansión de 0,1 y 0,3, respectivamente.

**3.4** **Supuestos**

1. Se supondrá altura normal aguas abajo asociada a la pendiente del cauce en su condición natural.

Por lo tanto, en las cercanías de dicho borde los resultados serán sólo referenciales.

2. Para la condición natural se asumirán las consideraciones indicadas en el punto 3.2.3, que respaldan

los límites prediales inscritos en el CBR.

#### 4 METODOLOGÍA

La metodología explicada en los siguientes puntos será aplicada para modelar la condición natural.

**4.1** **Generalidades**

El estudio hidráulico tiene por objetivo principal determinar el comportamiento del fluido y el área de
inundación generada por el aumento de los caudales máximos instantáneos frente a algún evento
meteorológico extraordinario.

Para estudiar el eje hidráulico de un cauce se requiere del desarrollo de un modelo geométrico, sobre el
cual posteriormente se desarrolle el análisis hidráulico respectivo. En el presente estudio, el análisis
hidráulico del cauce se realiza utilizando el software HEC-RAS 6.3.1, específicamente para los caudales de
periodo de retorno T=2, 10, 20, 50 y 100 años, señalado en Tabla 3-2.

El modelo geométrico georreferenciado del cauce se elabora a partir de un DEM ( _Digital Elevation Model_,
típicamente de extensión geotiff) que se obtiene a partir de una exportación del levantamiento
topográfico. Con el módulo RAS Mapper incorporado dentro de la versión HEC-RAS señalada se traza el
cauce y se generan los perfiles transversales georreferenciados que serán manejados en la modelación.

Los perfiles georreferenciados son importados como información geométrica dentro de HEC-RAS, donde
las características del modelo deben ser editadas según corresponda (rugosidades, singularidades, áreas
inefectivas, etc.) para posteriormente imponer las condiciones de borde y caudales a considerar para llevar

a cabo las simulaciones.

Como metodología de cálculo, HEC-RAS utiliza el balance de energía (o _momenta_, según elección) entre
dos (2) secciones transversales sucesivas usando el método del paso estándar y la ecuación de Manning
como modelo de estimación de pérdidas friccionales. Con el software pueden obtenerse, entre otros, los
siguientes resultados para cada sección transversal: niveles de agua, velocidad media del flujo, alturas
máximas, radio hidráulico, número de Froude, alturas críticas, etc.

Utilizando los resultados obtenidos en la modelación con HEC RAS, se evalúa el comportamiento del cauce,
tanto en las alturas de escurrimiento como las velocidades que se alcanza.

240923-000-HI-MDC-001_R0.docx 6 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**4.2** **Descripción del modelo HEC-RAS**

El modelo hidráulico del Estero Pelales a la altura del sitio del proyecto tiene una longitud de 1470 m de
cauce en total, con perfiles transversales distanciados cada 10 metros. Para la situación natural sin
proyecto estos perfiles tienen una longitud de 500 metros.

En la Figura 4-1 se presenta una planta esquemática con la distribución de los perfiles principales en ambos
casos y el sitio de la Subestación. Se considera que el caudal ingresa por completo al en el extremo aguas

arriba de la modelación.

**Figura 4-1: Planta perfiles transversales modelo hidráulico -Estero Pelales en sitio de interés**

**4.3** **Coeficiente de rugosidad**

Para la estimación de la pérdida friccional entre tramos consecutivos del cauce, el software utiliza la
ecuación de Manning, la cual depende del parámetro empírico de rugosidad conocido como “n” de
Manning. Este parámetro engloba las asperezas del lecho y las pérdidas por irregularidades de la sección
(e.g., depósitos, socavaciones, vegetación, etc.).

Para determinar su valor se considera la fórmula propuesta por Cowan (1956, Ref. [9]) que propone que
el valor de “n” puede estimarse según la siguiente relación:

240923-000-HI-MDC-001_R0.docx 7 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

n= m∙(n ଴ + n ଵ + n ଶ + n ଷ + n ସ )

Donde:

_n_ : Coeficiente de rugosidad de Manning [m/s [1/3] ].
_m_ : Factor de corrección por la presencia de meandros.
_n_ 0 : Valor básico de n, para un canal recto, uniforme y liso en materiales naturales.
n 1 : Valor dependiente de las irregularidades de la superficie.
n 2 : Valor dependiente de las variaciones en la sección transversal.
n 3 : Valor dependiente de las obstrucciones en el cauce.
n 4 : Valor dependiente del efecto de la vegetación.

Los coeficientes anteriores se encuentran tabulados en la Tabla 4-1:

**Tabla 4-1: Coeficientes de Manning** **para fórmula de Cowan (Tabla 3.707.104.B, Ref.[9])**

De acuerdo con esta metodología, y en atención a las características del cauce (Anexo 2), se estimó el valor
del coeficiente de rugosidad de Manning presentado en Tabla 4-2, el cual está acorde a valores típicos de
cursos de baja pendiente, con bancos de sedimentos, pendientes irregulares y tramos con árboles y
arbustos (Tabla 3.707.104.A de Ref.[9]).

**Tabla 4-2: Estimación de coeficiente de rugosidad de Manning**

(*) Las variaciones de la sección transversal no se consideran en el cálculo con la ecuación de Cowan

debido a que están incluidas en el software HEC RAS y se estaría incorporando dos veces el mismo
efecto. Los coeficientes de contracción / expansión utilizados son 0,1 y 0,3 respectivamente.

240923-000-HI-MDC-001_R0.docx 8 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**4.4** **Condiciones de borde**

El cauce en estudio presenta pendiente longitudinal baja lo que a priori indica la predominancia de
régimen subcrítico.

Sin embargo, debido a la irregularidad del lecho y a la presencia de sectores en contrapendiente que
pudiesen generar resaltos hidráulicos, el análisis hidráulico se realiza en régimen mixto, ya que una
simulación en régimen subcrítico limitaría a priori las alturas de escurrimiento a valores mayores o iguales
a la altura crítica, lo cual no necesariamente a priori sería correcto. Dado lo anterior, se requiere establecer
una condición de borde para el extremo de aguas arriba y otra para el extremo de aguas abajo.

En la Tabla 4-3 se presentan las condiciones de borde consideradas en las simulaciones hidráulicas. Al estar
sustentado en un supuesto (ver punto 3.4) los resultados en las cercanías de los bordes son sólo

referenciales.

**Tabla 4-3: Condiciones de borde modelación hidráulica - Cruce 1, Estero El Sauce**

|Aguas arriba Aguas abajo|Col2|
|---|---|
|Altura normal<br>S=0,17%|Altura normal<br>S=0,17%|

240923-000-HI-MDC-001_R0.docx 9 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### 5 RESULTADOS

A continuación, se presenta la determinación de eje hidráulico para T=2, 10, 20, 50 y 100 años para el

Cauce en estudio.

En las siguientes figuras se presenta el área de inundación, altura de escurrimiento y velocidad de
escurrimiento a lo largo del cauce, para el caudal máximo instantáneo (QMI) asociado a los períodos de
retorno de 2, 10, 20, 50 y 100 años para la condición natural sin proyecto.

**Figura 5-1: Área de inundación - Condición natural sin proyecto, Estero Pelales en sitio de interés**

**T=2**

**T=10**

**T=50**

**T=100**

240923-000-HI-MDC-001_R0.docx 10 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**Figura 5-2: Perfil longitudinal - Condición natural sin proyecto, Estero Pelales en sitio de interés** **[ 1]**

|Col1|Col2|Legend|
|---|---|---|
|||WS T=100|
|||WS T=050|
|||WS T=010<br>|
||||
|||Crit T=100<br>WS T=002|
|||Crit T=050<br>|
|||Crit T=010|
|||Crit T=002|
|||Ground|
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||

**Figura 5-3: Velocidades medias - Condición natural sin proyecto, Estero Pelales en sitio de interés** **[ 1]**

|Col1|Col2|Legend|
|---|---|---|
|||Vel Chnl T=100<br>Vel Chnl T=050<br>Vel Chnl T=010<br>Vel Chnl T=002|
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||

Los resultados detallados se encuentran en el Apéndice A. En Apéndice B se adjunta archivo “kmz” del

área de inundación del cauce para los periodos de retorno en estudio. En Apéndice C se adjuntan los

archivos entrada del modelo HEC-RAS.

1 Los resultados que se obtienen a menos de 5 metros de los extremos de la modelación se consideran no
representativos pues están influenciados por la condición de borde supuesta.

240923-000-HI-MDC-001_R0.docx 11 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### 6 CONCLUSIONES

1) Según se desprende de la Figura 5-1, que muestra los márgenes de la crecida del Estero Pelales en

condición natural, el sitio de la Subestación proyectada se encuentra fuera del cauce.

2) En la siguiente tabla se resumen los resultados más relevantes de la modelación en HEC-RAS en

torno al sitio de la subestación (PK 500 a 1200):

**Tabla 6-1: Resumen de resultados, Estero Pelales en sitio Subestación Quepe**

|Variable Unidad T=10 T=100<br>Años años|Col2|Col3|Col4|
|---|---|---|---|
|Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9|Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9|Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9|Alt. de escurrimiento máx- Cond. Natural sin proy.<br>[m]<br>1,3<br>1,9|
|Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6|Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6|Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6|Vel. Máx. - Cond. Natural sin proy.<br>[m/s]<br>1,2<br>1,6|
|Ancho superficial prom. - Cond. Natural sin proy.|[m]|25,8|59,7|

3) Del análisis expuesto queda demostrado que el emplazamiento del proyecto de subestación Quepe,

queda fuera del cauce natural.

240923-000-HI-MDC-001_R0.docx 12 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### ANEXO 1: POLÍGONO DE SERVIDUMBRE SUBESTACIÓN QUEPE

240923-000-HI-MDC-001_R0.docx 13 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**Figura An.1-1: Plano de polígono de servidumbre**

240923-000-HI-MDC-001_R0.docx 14 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**Figura An.1-2: Plano límite predial, ROL No. 310-409**

240923-000-HI-MDC-001_R0.docx 15 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### ANEXO 2: REGISTRO FOTOGRÁFICO

240923-000-HI-MDC-001_R0.docx 16 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

Con la visita a terreno se elaboró un set fotográfico georreferenciado, donde se visualiza el emplazamiento
del Proyecto con relación a la hidrología propia del sector.

En la Figura An.2-1 se indica espacialmente el registro fotográfico obtenido en terreno y en la Tabla An.21 se muestran las fotografías obtenidas.

**Figura An.2-1: Distribución espacial de fotografías de visita a terreno**

240923-000-HI-MDC-001_R0.docx 17 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**Tabla An.2-1: Fotografías del área de Proyecto**

|F-1: Fotografía desde el lado Este de la zona del Proyecto (desde Ruta 5). F-2: Fotografía desde el lado Sureste de la zona del Proyecto (desde Ruta 5).|Col2|
|---|---|
|F-3: Fotografía desde el lado Suroeste de la zona del Proyecto.<br>F-4: Fotografía desde el lado Oeste de la zona del Proyecto<br>(desde Ruta Camino al Aeropuerto).|F-3: Fotografía desde el lado Suroeste de la zona del Proyecto.<br>F-4: Fotografía desde el lado Oeste de la zona del Proyecto<br>(desde Ruta Camino al Aeropuerto).|
|F-5: Fotografía general del área de Proyecto, desde el lado<br>Oeste de la zona (desde Ruta Camino al Aeropuerto).|F-6: Fotografía general del área de Proyecto, desde el lado<br>Oeste de la zona (desde Ruta Camino al Aeropuerto).|

240923-000-HI-MDC-001_R0.docx 18 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**Tabla An.2-1: Fotografías del área de Proyecto**

|F-7: Fotografía del Estero Pelales al lado Este de la zona del Proyecto (desde Ruta 5). F-8: Fotografía del Estero Pelales al lado Este de la zona del Proyecto (desde Ruta 5).|Col2|
|---|---|
|F-9: Fotografía del Estero Pelales al lado Este de la zona del<br>Proyecto (desde Ruta 5).<br>F-10: Fotografía del Estero Pelales al lado Este de la zona del<br>Proyecto (desde Ruta 5).|F-9: Fotografía del Estero Pelales al lado Este de la zona del<br>Proyecto (desde Ruta 5).<br>F-10: Fotografía del Estero Pelales al lado Este de la zona del<br>Proyecto (desde Ruta 5).|
|F-11: Fotografía del Estero Pelales en el lado Este de la zona<br>del Proyecto.|F-12: Fotografía del Estero Pelales en el lado Este de la zona<br>del Proyecto.|

240923-000-HI-MDC-001_R0.docx 19 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

**Tabla An.2-1: Fotografías del área de Proyecto**

|F-13: Fotografía del Estero Pelales en el lado Este de la zona del Proyecto. F-14: Fotografía del Estero Pelales en el lado Noroeste de la zona del Proyecto.|Col2|
|---|---|
|F-15: Fotografía del Estero Pelales en el lado Noroeste de la<br>zona del Proyecto.<br>F-16: Fotografía del Estero Pelales en el lado Oeste de la zona<br>del Proyecto.|F-15: Fotografía del Estero Pelales en el lado Noroeste de la<br>zona del Proyecto.<br>F-16: Fotografía del Estero Pelales en el lado Oeste de la zona<br>del Proyecto.|
|F-17: Fotografía del Estero Pelales en el lado Oeste de la zona<br>del Proyecto.|F-18: Fotografía del Estero Pelales en el lado Oeste de la zona<br>del Proyecto.|

240923-000-HI-MDC-001_R0.docx 20 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### APÉNDICE A: RESULTADOS EJES HIDRÁULICOS

240923-000-HI-MDC-001_R0.docx 21 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

En la Tabla Ap.A.1 del presente apéndice se muestra el detalle del resultado del eje hidráulico para la
condición natural. Se muestran los resultados para T= 10 y 100 años, en torno al sitio de interés (estaciones
500 a 1200)

Los resultados se presentan en orden correlativo desde aguas arriba hacia aguas abajo.

La nomenclatura de resultados se resume a continuación:

**Tabla Ap.A-1: Nomenclatura de resultados ejes hidráulicos**

**Tabla Ap.A-1: Resultados**

240923-000-HI-MDC-001_R0.docx 22 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

240923-000-HI-MDC-001_R0.docx 23 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

240923-000-HI-MDC-001_R0.docx 24 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

240923-000-HI-MDC-001_R0.docx 25 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

240923-000-HI-MDC-001_R0.docx 26 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

|River Sta Profile Q Total Min Ch El Hydr Depth C Vel Chnl Area Channel Top Width Froude # Chl|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|**(m3/s)**<br>**(m)**<br>**(m)**<br>**(m/s)**<br>**(m2)**<br>**(m)**|
|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|80<br>T=010<br>36<br>89.82<br>1.26<br>1.19<br>30.3<br>25.75<br>0.34|
|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|80<br>T=100<br>64<br>89.82<br>1.76<br>1.48<br>42.14<br>45.48<br>0.36|
|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|70<br>T=010<br>36<br>89.8<br>1.27<br>1.19<br>30.38<br>25.87<br>0.34|
|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|70<br>T=100<br>64<br>89.8<br>1.76<br>1.48<br>42.22<br>45.61<br>0.36|
|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|60<br>T=010<br>36<br>89.79<br>1.26<br>1.19<br>30.18<br>25.55<br>0.34|
|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|59.99999<br>T=100<br>64<br>89.79<br>1.75<br>1.48<br>42.02<br>45.28<br>0.36|
|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|50<br>T=010<br>36<br>89.77<br>1.26<br>1.19<br>30.25<br>25.68<br>0.34|
|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|50<br>T=100<br>64<br>89.77<br>1.75<br>1.48<br>42.09<br>45.41<br>0.36|
|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|39.99999<br>T=010<br>36<br>89.75<br>1.26<br>1.19<br>30.33<br>25.8<br>0.34|
|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|40<br>T=100<br>64<br>89.75<br>1.76<br>1.48<br>42.17<br>45.53<br>0.36|
|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|30<br>T=010<br>36<br>89.73<br>1.27<br>1.18<br>30.41<br>25.93<br>0.34|
|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|30<br>T=100<br>64<br>89.73<br>1.76<br>1.48<br>42.25<br>45.66<br>0.36|
|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|20<br>T=010<br>36<br>89.72<br>1.26<br>1.19<br>30.22<br>25.62<br>0.34|
|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|20<br>T=100<br>64<br>89.72<br>1.75<br>1.48<br>42.05<br>45.34<br>0.36|
|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|10<br>T=010<br>36<br>89.7<br>1.26<br>1.19<br>30.3<br>25.74<br>0.34|
|10|T=100|64|89.7|1.76|1.48|42.13|45.46|0.36|

240923-000-HI-MDC-001_R0.docx 27 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### APÉNDICE B: ARCHIVO “KMZ” POLÍGONOS DE INUNDACIÓN

240923-000-HI-MDC-001 - Ap.B.zip

240923-000-HI-MDC-001_R0.docx 28 de 29

MODELACIÓN HIDRÁULICA ESTERO PELALES EN SITIO DEL PROYECTO

PROYECTO SUBESTACIÓN QUEPE

#### APÉNDICE C: ARCHIVOS DE ENTRADA HEC-RAS

240923-000-HI-MDC-001 - Ap.C.zip

240923-000-HI-MDC-001_R0.docx 29 de 29