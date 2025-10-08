---
title: Sin título
author: Paolo Urrutia
date: D:20250321115554-03'00'
language: es
type: report
pages: 50
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - =  
  -   3 P i * n i 5.1 
  - 1   P i * n i 5.1 
  - n c =  P i * n i
-->

PROYECTO No 2410485

|REV.|FECHA|RVIA|Col4|Col5|DESCRIPCIÓN|
|---|---|---|---|---|---|
|**REV.**|**FECHA**|**PREP.**|**REV.**|**APR.**|**APR.**|
|A|23-12-2024|FMF|FGA/PUS|RVV|REVISIÓN INTERNA|
|B|10-01-2025|FMF|FGA|RVV|REVISIÓN DEL CLIENTE|
|||||||

**CONTENIDO**

**1** GENERAL .................................................................................................................. 4

1.1 INTRODUCCIÓN ..................................................................................................... 4

1.2 OBJETIVOS ............................................................................................................. 5

1.3 ALCANCES .............................................................................................................. 6

1.4 EXCLUSIONES ........................................................................................................ 6

1.5 REFERENCIAS ........................................................................................................ 6

2 DESCRIPCION GENERAL ......................................................................................... 8

3 Criterios de diseño .................................................................................................... 11

3.1 CAUDALES DE DISEÑO........................................................................................ 11

3.2 Velocidad mínima y máxima ................................................................................... 13

3.3 Condiciones de escurrimiento ................................................................................ 13

3.4 Revancha ............................................................................................................... 14

3.5 COEFICIENTE DE RUGOSIDAD ........................................................................... 14

3.6 condiciones de borde ............................................................................................. 16

4 CANALES DE CONTORNO ..................................................................................... 16

4.1 Separación en Subsecciones ................................................................................. 18

4.2 Consideraciones del Modelo. ................................................................................. 18

4.3 resultados de la MODELACIÓN HIDRÁULICA ....................................................... 18
4.3.1 Análisis escenario CON proyecto ......................................................................... 19
4.3.2 Resultados modelacion tramo 1 ........................................................................... 21

4.3.3 Resultados modelacion tramo 2 ........................................................................... 30

4.3.4 Resultados modelacion tramo 3 ........................................................................... 35

5 GRADAS ESCALONADAS ....................................................................................... 42

5.1 DISEÑO GEOMETRICO ........................................................................................ 42

5.2 VERIFICACION DE LA OBRA DE DESCARGA DE CANAL 1 ............................... 44

5.3 VERIFICACION DE LA OBRA DE DESCARGA DE CANAL 1 ............................... 47

6 CONCLUSIONES ..................................................................................................... 50

**FIGURAS**

Figura 1-1 Ubicación General del Proyecto ......................... **¡Error! Marcador no definido.**

Figura 2-1 Canal de Contorno Proyectado ......................................................................... 8

Figura 2-2 Obras Proyectadas ......................................................................................... 10

Figura 4-1 Sección Canal Proyectado .............................................................................. 19

2410485-00-HID-INF-002 Rev_B Página 2 de 50

Figura 4-2 Distribución Espacial de Tramos de Canal de Contorno Proyectado. ............. 20

Figura 4-3 Modelación Canal de Contorno - Tramo 1, Esquema Isométrico. .................. 21

Figura 4-4 Modelación Canal de Contorno - Tramo 1, Eje Hidráulico. ............................. 22

Figura 4-5 Modelación Canal de Contorno - Tramo 2, Esquema Isométrico. .................. 33

Figura 4-6 Modelación Canal de Contorno - Tramo 2, Eje Hidráulico. ............................. 34

Figura 4-7 Modelación Canal de Contorno - Tramo 3, Eje Hidráulico. ............................. 40

Figura 4-8 Modelación Canal de Contorno - Tramo 3, Esquema Isométrico. ........... **¡Error!**
**Marcador no definido.**

Figura 5-1 Altura de Escurrimiento - Aguas abajo de Grada de Bajada........................... 42

Figura 5-2 Longitud de Torrente - Aguas abajo de Grada de Bajada .............................. 43

Figura 5-3 Grada Escalonadas N°1 ................................................................................. 45

Figura 5-4 Grada Escalonadas N°2 ................................................................................. 48

**TABLAS**

Tabla 2-1. Canal de Contorno - Tramos y Obras Proyectadas .................................... 11

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 2410485-00-HID-INF-002 Rev_B Página 10 de 50 En la Tabla 2-1 se resume el inicio y fin de cada obra ejecutada. -->

**Tabla 2-1: Canal de Contorno - Tramos y Obras Proyectadas****

| TRAZADO | Col2 | SECCION TIPO |
| --- | --- | --- |
| **INICIO (m)** | **FIN (m)** | **FIN (m)** |
| 0,00 | 209,67 | CANAL TRAPECIAL |
| 209,67 | 230,00 | ALCANTARILLA |
| 230,00 | 1.107,03 | CANAL TRAPECIAL |
| 1.107,03 | 1.111,03 | TRANSICION |
| 1.111,03 | 1.135,54 | CANAL RECTANGULAR |
| 1.135,54 | 1.179,55 | GRADA ESCALONADA N°1 |
| 1.179,55 | 1.187,41 | CANAL RECTANGULAR |
| 1.187,41 | 1.191,41 | TRANSICION |
| 1.191,41 | 1614,39 | CANAL TRAPECIAL |
| 1614,39 | 1.618,39 | TRANSICION |
| 1.618,39 | 1.629,04 | CANAL RECTANGULAR |
| 1.629,04 | 1.690,18 | GRADA ESCALONADA N° 2 |
| 1.690,18 | 1.698,55 | CANAL RECTANGULAR |
| 1.698,55 | 1.702,55 | TRANSICION |
| 1.702,55 | 2.107,52 | CANAL TRAPECIAL |
| 2.107,52 | 2.115,30 | DISIPADOR DE ENERGIA |

<!-- Estadísticas: 17 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: RVIA, 2025. **3** **CRITERIOS DE DISEÑO** -->
<!-- FIN TABLA 2-1 -->


Tabla 3-1. Distribución Espacial de Caudales, Caudales de Diseño. ........................... 12

Tabla 3-2. Distribución Espacial de Caudales, Caudales de Verificación. .................... 12

Tabla 3-3. Valores límite del número de Froude .......................................................... 14

Tabla 3-4 Coeficiente de Rugosidad, Canales Revestidos o Artificiales ........................... 15

Tabla 3-5 Coeficiente de Rugosidad, Canales Excavados y Uniformes ........................... 15

Tabla 4-1 Modelación Canal de Contorno - Tramo 1, Resultados T=100 ........................ 23

Tabla 4-2 Modelación Canal de Contorno - Tramo 2, Resultados T=100 ........................ 30

Tabla 4-3 Modelación Canal de Contorno - Tramo 3, Resultados T=100 ........................ 35

Tabla 5-1 Verificación hidráulica de grada escalonada N°1 ............................................. 46

Tabla 5-2 Verificación hidráulica de grada escalonada N°2 ............................................. 49

2410485-00-HID-INF-002 Rev_B Página 3 de 50

**1** **GENERAL**
**1.1** **INTRODUCCIÓN**

En el marco de la DIA “Modificación Proyecto Planta Los Mantos: Implementación depósito
de relaves de filtrados y extensión de vida útil” [1] Batery Mineral Resources (en adelante
“BMR”) ha solicitado a RVIA la elaboración de los siguientes permisos sectoriales de la
Dirección General de Aguas (en adelante e indistintamente “DGA”) para el Canal de
Contorno y su Obra de Descarga en el Estero Los Mantos:

 - Permiso Sectorial DGA de “Modificación de Cauce” [2] acogido en los artículos 41 y 171
del Código de Aguas

 - Permiso Sectorial DGA de “Obra Hidráulica” [3] acogido a los artículos 294 y siguientes,
también del Código de Aguas.

De acuerdo con lo precisado en el artículo 2° del D.S N°50/2015 del Ministerio de Obras
Públicas (en adelante e indistintamente, “MOP”) y en la “Guía para solicitudes de Aprobación
de Proyectos de Construcción de Ciertas Obras Hidráulicas establecidas en el artículo 294
del Código de Aguas”, se ha definido solicitar en única presentación la aprobación de ambos
permisos sectoriales para las obras asociadas al canal de contorno:

_“[...] Esta reglamentación se aplicará a todas las obras nuevas que se proyecten y_
_que cumplan con alguna característica de las descritas en el artículo 294 del Código_
_de Aguas, y a la reconstrucción de este tipo de obras, aun cuando a las obras_
_originales no se les hayan aplicado estas disposiciones. Cuando algún proyecto de_
_estas obras hidráulicas contenga dentro de sus elementos algunas de las obras a_
_que se refieren los artículos 41, 151 y 171 del Código de Aguas, el Titular podrá_
_solicitar en una misma presentación la aprobación de dichas obras. En este caso, las_
_obras a que se refieren los artículos 41, 151 y 171 del Código de Aguas se evaluarán_
_en conjunto con las obras del mencionado artículo 294 y se aprobarán en una misma_
_resolución si cumplen con los requisitos técnicos y legales correspondientes [...]”_

En este contexto regulatorio y de acuerdo con lo indicado en las guías metodológicas
dispuestas por la DGA para los permisos sectoriales de “Modificación de Cauce” y de “Obra
hidráulica”, RVIA ha diseño el canal de contorno obteniendo los siguientes resultados:

 - Caudal de diseño para un periodo de retorno de 50 años (Q T=50 años ): 4,14 m [3] /s.

 - Caudal de verificación para un periodo de retorno de 100 años (Q T=100 años ): 4,80
m [3] /s.

1 [https://seia.sea.gob.cl/expediente/ficha/fichaPrincipal.php?modo=normal&id_expediente=2162940661](https://seia.sea.gob.cl/expediente/ficha/fichaPrincipal.php?modo=normal&id_expediente=2162940661)
2 [https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia](https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia%20de%20Presentacion%20y%20Aprobacion%20de%20Proyectos%20de%20Modificacion%20de%20Cauces%20DIC%202016.pdf)

[%20de%20Presentacion%20y%20Aprobacion%20de%20Proyectos%20de%20Modificacion%20de%20Ca](https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia%20de%20Presentacion%20y%20Aprobacion%20de%20Proyectos%20de%20Modificacion%20de%20Cauces%20DIC%202016.pdf)
[uces%20DIC%202016.pdf](https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia%20de%20Presentacion%20y%20Aprobacion%20de%20Proyectos%20de%20Modificacion%20de%20Cauces%20DIC%202016.pdf)
3 [https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia](https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia%20Solicitud%20VC%20Aprobacion%20Construccion%20Obras%20Art%20294%20ver%20abril%202022.pdf)

[%20Solicitud%20VC%20Aprobacion%20Construccion%20Obras%20Art%20294%20ver%20abril%202022](https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia%20Solicitud%20VC%20Aprobacion%20Construccion%20Obras%20Art%20294%20ver%20abril%202022.pdf)
.pdf

2410485-00-HID-INF-002 Rev_B Página 4 de 50

En consideración de lo anterior, el presente informe contiene la “Memoria de Cálculo

Hidráulica” del canal de contorno.

En la Figura 1-1 se presenta la ubicación general del Proyecto, el cual se emplaza en Planta
Los Mantos de BMR, Comuna de Punitaqui, IV Región de Coquimbo.

**Figura 1-1 Ubicación General del Proyecto.**

Fuente: DIA “Modificación Proyecto Planta Los Mantos: Implementación depósito de

relaves de filtrados y extensión de vida útil”, 2024.

**1.2** **OBJETIVOS**

El objetivo general de este documento es presentar un respaldo técnico que permita
garantizar la seguridad de la estructura proyectada, con capacidad de porteo asociada a un
periodo de retorno de 50 años y verificada para un caudal asociado a un periodo de retorno
de 100 años.

2410485-00-HID-INF-002 Rev_B Página 5 de 50

**1.3** **ALCANCES**

En este documento se presenta el estudio hidráulico, que abarca:

 - Definición del trazado del canal de contorno.

 Determinación del eje hidráulico del canal de contorno para periodos de retorno de
diseño de 50 años (T diseño =50 años).

 Verificación del eje hidráulico del canal de contorno para periodos de retorno de 100
años (T verificación =100 años).

 - Diseño de las alcantarillas requeridas para permitir el cruce del camino.

 Obras de disipación de energía necesarias para salvar grandes caídas en el trazado
del canal de contorno.

 Diseño de obras de disipación de energía.

**1.4** **EXCLUSIONES**

Se excluyen de este informe:

 - Determinación de caudales.

 Verificación estructural del canal y sus obras asociadas.

 Estimación de socavación general y local.

**1.5** **REFERENCIAS**

Los siguientes antecedentes son utilizados en el desarrollo del presente documento:

Ref. 1: Decreto Supremo N°50 del Ministerio de Obras Públicas.

Ref. 2: Guías Metodológica para Proyectos de Modificación de Cauces, DGAdiciembre 2016

Ref. 3: Topografía proporcionada por el cliente (1:1000, curvas c/1 m).

Ref. 4: Manual de Carreteras, MOP-2012. Capitulo No 3.700 "Hidrología y Drenaje".

Ref. 5: Hidrología Aplicada. McGraw-Hill. Chow V. T., Maidment D., Mays L. 1994.

Ref. 6: Estadísticas pluviométricas de precipitaciones de la Dirección General de
Aguas, Departamento de Hidrología.

Ref. 7: Precipitaciones Máximas para 10 años de Período de Retorno en 1, 2 y 3 días.
Dirección General de Aguas, 1994.

Ref. 8: Manual de cálculo de crecidas y caudales mínimos en cuencas sin
información pluviométrica. Dirección General de Aguas, 1995.

Ref. 9: Guía de Permisos Ambientales Sectoriales PAS 155, Permisos para la
Construcción de Ciertas Obras Hidráulicas, Servicio de Evaluación Ambiental,
2019

Ref. 10: Guía de Permisos Ambientales Sectoriales PAS 156, Modificación de Cauces,

2410485-00-HID-INF-002 Rev_B Página 6 de 50

Servicio de Evaluación Ambiental, 2019.

Ref. 11: Guía de Permisos Ambientales Sectoriales PAS 157, Permiso Obras de

Regularización o Defensa de Cauces Naturales, Servicio de Evaluación
Ambiental, 2019.

Ref. 12: VP812656-0000-40ER-0002, “Informe Final”, Ingeniería Conceptual diseño

de depósito de relaves MAP, SNC-Lavalin, 2012.

Ref. 13: Precipitaciones máximas diarias en Chile. Stowhas Ludwig B. Sociedad

Chilena de Ingeniería Hidráulica, VI Congreso Nacional. 1983.

Ref. 14: VP913680-0000-4HEB-0001, "Estudio hidrológico depósito de relaves MAP",

SNC-Lavalin, 2014.

Ref. 15: Sistema Hidrométrico en Línea, Dirección General de Aguas.

Ref. 16: 2410485-00-HID-INF-001, memoria de cálculo hidráulica, RVIA, 2024.

2410485-00-HID-INF-002 Rev_B Página 7 de 50

**2** **DESCRIPCION GENERAL**

Con motivo de cumplir con establecido en los artículos 41, 171, 130 y siguientes, y demás
pertinentes del Código de Aguas y lo establecido en el Manual de Normas y Procedimientos
para la Administración de Recursos Hídricos, se considera el diseño de un canal de contorno
destinado a interceptar los flujos superficiales de aguas no contactadas que drenan hacia
los depósitos de relave que administra actualmente Compañía Minera BMR.

El Decreto Supremo N°50 ( Ref. 1: ) del Ministerio de Obras Publicas indica en su artículo
35, letra b) que el canal de contorno deberá presentar una capacidad de conducción
asociada a un periodo de retorno de 50 años y verificado para un periodo de retorno de 100
años, de manera de garantizar la seguridad de terceros.

El trazado del canal de contorno proyectado ha sido definido de forma de adaptarse al relieve
del sector, tratando de copiar la ruta de caminos existentes.

Se considera además la implementación de dos alcantarillas para salvar la interferencia con
caminos de servicio existentes.

Se considera que el canal de contorno descargara en la quebrada Los Mantos, previo paso
por un tramo de riprap (enrocado destinado a la disipación de energía).

En la Figura 2-1 se presenta una **planta general con el trazado del canal de contorno** con
su punto de descarga propuesto en el cauce de la quebrada Los Mantos.

**Figura 2-1 Canal de Contorno Proyectado.**

2410485-00-HID-INF-002 Rev_B Página 8 de 50

En la Figura 2-2 se ilustra la ubicación referencial de las estructuras que forman parte del

canal de contorno.

2410485-00-HID-INF-002 Rev_B Página 9 de 50

**Figura 2-2 Obras Proyectadas**

Fuente: RVIA, 2025.

2410485-00-HID-INF-002 Rev_B Página 10 de 50

En la Tabla 2-1 se resume el inicio y fin de cada obra ejecutada.

**Tabla 2-1: Canal de Contorno - Tramos y Obras Proyectadas**

|TRAZADO|Col2|SECCION TIPO|
|---|---|---|
|**INICIO (m)**|**FIN (m)**|**FIN (m)**|
|0,00|209,67|CANAL TRAPECIAL|
|209,67|230,00|ALCANTARILLA|
|230,00|1.107,03|CANAL TRAPECIAL|
|1.107,03|1.111,03|TRANSICION|
|1.111,03|1.135,54|CANAL RECTANGULAR|
|1.135,54|1.179,55|GRADA ESCALONADA N°1|
|1.179,55|1.187,41|CANAL RECTANGULAR|
|1.187,41|1.191,41|TRANSICION|
|1.191,41|1614,39|CANAL TRAPECIAL|
|1614,39|1.618,39|TRANSICION|
|1.618,39|1.629,04|CANAL RECTANGULAR|
|1.629,04|1.690,18|GRADA ESCALONADA N° 2|
|1.690,18|1.698,55|CANAL RECTANGULAR|
|1.698,55|1.702,55|TRANSICION|
|1.702,55|2.107,52|CANAL TRAPECIAL|
|2.107,52|2.115,30|DISIPADOR DE ENERGIA|

Fuente: RVIA, 2025.

**3** **CRITERIOS DE DISEÑO**

A continuación, se indican los criterios de diseño y verificación utilizados en los diseños de
las obras hidráulicas.

**3.1** **CAUDALES DE DISEÑO**

De acuerdo con la memoria de cálculo de hidrología desarrollado por RVIA ( Ref. 16: ) que
complementa este documento, se ha estimado un caudal máximo de diseño para un periodo
de retorno de 50 años con valor de 4,14 m [3] /s y un caudal máximo de verificación para un
periodo de retorno de 100 años con un valor de 4,80 m [3] /s.

Los caudales determinados han sido distribuidos espacialmente según el punto de
descarga de las cuencas determinadas en la memoria de cálculo de hidrología Ref. 16: .

En la Tabla 3-1 se resume la distribución espacial de caudales de diseño con el tramo de
canal en el que se aplica.

Análogamente, en la Tabla 3-2, se resume la distribución espacial de caudales de diseño
con el tramo de canal en el que se aplica.

2410485-00-HID-INF-002 Rev_B

**Tabla 3-1.Distribución Espacial de Caudales, Caudales de Diseño.**

|Tramo Canal|Col2|Caudal Aportado por Cuenca|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Caudal<br>Total|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Inicio**|**Termino**|**C-1**|**C-2**|**IC-1**|**C-3**|**IC-2**|**C-4**|**IC-3**|**C-5**|**C-6**|**C-6**|
|**0,00**|**235,30**|0,98|||||||||0,98|
|**251,30**|**251,30**|0,98|0,67||||||||1,65|
|**251,30**|**453,30**|0,98|0,67|0,05|||||||1,71|
|**453,30**|**691,30**|0,98|0,67|0,05|0,77||||||2,48|
|**691,30**|**691,30**|0,98|0,67|0,05|0,77|0,05|||||2,53|
|**691,30**|**915,30**|0,98|0,67|0,05|0,77|0,05|0,69||||3,22|
|**915,30**|**915,30**|0,98|0,67|0,05|0,77|0,05|0,69|0,06|||3,28|
|**915,30**|**1179,55**|0,98|0,67|0,05|0,77|0,05|0,69|0,06|0,72||4,00|
|**1179,55**|**2.115,30**|0,98|0,67|0,05|0,77|0,05|0,69|0,06|0,72|0,13|4,14|

Fuente: RVIA, 2025.

**Tabla 3-2.** **Distribución Espacial de Caudales, Caudales de Verificación.**

|Tramo Canal|Col2|Caudal Aportado por Cuenca|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Caudal<br>Total|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Inicio**|**Termino**|**C-1**|**C-2**|**IC-1**|**C-3**|**IC-2**|**C-4**|**IC-3**|**C-5**|**C-6**|**C-6**|
|**0,00**|**235,30**|1,14|||||||||1,14|
|**251,30**|**251,30**|1,14|0,78||||||||1,92|
|**251,30**|**453,30**|1,14|0,78|0,06|||||||1,98|
|**453,30**|**691,30**|1,14|0,78|0,06|0,90||||||2,88|
|**691,30**|**691,30**|1,14|0,78|0,06|0,90|0,06|||||2,94|
|**691,30**|**915,30**|1,14|0,78|0,06|0,90|0,06|0,80||||3,74|
|**915,30**|**915,30**|1,14|0,78|0,06|0,90|0,06|0,80|0,06|||3,81|
|**915,30**|**1179,55**|1,14|0,78|0,06|0,90|0,06|0,80|0,06|0,84||4,65|
|**1179,55**|**2.115,30**|1,14|0,78|0,06|0,90|0,06|0,80|0,06|0,84|0,16|4,80|

Fuente: RVIA, 2025.

2410485-00-HID-INF-002 Rev_B

**3.2** **VELOCIDAD MÍNIMA Y MÁXIMA**

Las obras hidráulicas proyectadas consideran limitaciones de velocidad a fin de garantizar
la estabilidad y seguridad de la obra:

 - Se consideran secciones sin revestir en aquellos casos en que la velocidad media

del flujo resulte menor a 1,0 m/s.

 - En caso de que la velocidad media resulte mayor a 1,0 m/s y menor a 2,5 m/s, se

considera un revestimiento sin armadura.

 - Cuando la velocidad media del flujo resulte mayor a 2,5 m/s, se recomienda utilizar

revestimientos con armadura para evitar el levantamiento por sub-presión.

 - Se considera una velocidad mínima aceptable dentro del orden de 0,7 a 1,0 m/s a

fin de evitar la depositación de materiales en suspensión.

**3.3** **CONDICIONES DE ESCURRIMIENTO**

El comportamiento del flujo de agua está gobernado por la viscosidad, la gravedad y las
fuerzas inerciales del flujo. De acuerdo con la relación entre fuerzas inerciales y fuerzas
gravitacionales, el flujo puede ser clasificado como:

 Escurrimiento subcrítico: La influencia de la gravedad es mayor que las fuerzas
inerciales, por lo que la velocidad del flujo es lenta y el cauce es descrito como quieto
y lento.

 Escurrimiento supercrítico: La influencia de las fuerzas inerciales es mayor que la
gravedad, por lo que la velocidad del flujo es alta y el cauce es descrito como
torrencial y rápido.

 Escurrimiento crítico: Corresponde a la condición de mínima energía con que puede
escurrir cierto caudal, también se describe como el máximo caudal que puede
escurrir dado cierto nivel de energía. Es la condición límite entre escurrimiento
subcrítico y supercrítico.

Para representar la relación entre gravedad y la inercia se utiliza el Número de Froude, que
se expresa mediante la siguiente expresión:

Donde:

v : velocidad de escurrimiento [m/s].

g : aceleración de gravedad [m/s [2] ].

B : ancho superficial [m].

A : área de la sección transversal [m [2] ].

2410485-00-HID-INF-002 Rev_B

Las condiciones de escurrimiento se definen de acuerdo con el Número de Froude, según
las condiciones mostradas en la Tabla 3-3.

**Tabla 3-3.** **Valores límite del número de Froude**

|RÉGIMEN|FROUDE|
|---|---|
|**Subcrítico**|_FR_ < 1|
|**Crítico**|_FR_ = 1|
|**Supercrítico**|_FR_ > 1|

Fuente: RVIA, 2025.

**3.4** **REVANCHA**

Se considera que la crecida con periodo de retorno de 100 años quede contenida dentro de
la sección de canal, evitando sobre vertidos laterales.

En general, la revancha varía entre un 5% y un 30% de la altura de escurrimiento,
recomendándose en general un valor mínimo de 0,20 m.

Pare asegurar la contención del caudal se considera una revancha entre el borde del canal
y el eje hidráulico se adoptan las recomendaciones del U.S.B.R.

Para un caudal de diseño asociado a un periodo de retorno de 50 años y con valor igual a
4,14 m [3] /s se ha considerado conservadoramente una revancha mínima de 0,30 m (mayor
a la mínima recomendada), la que presenta capacidad suficiente para contener la crecida
centenaria correspondiente al caudal de verificación con periodo de retorno de 100 años.

**3.5** **COEFICIENTE DE RUGOSIDAD**

El grado de rugosidad entre el fluido y las paredes de la estructura de conducción queda
definido por el coeficiente propuesto por Manning y se selecciona de acuerdo con la
naturaleza de la estructura analizada, valores que han sido adoptado desde las tablas de
valores propuestos por Ven T Chow, obtenidos desde pruebas en laboratorio.

a) Revestimiento de hormigón o shotcrete

Se considera que las paredes del rápido de descarga sean recubiertas en hormigón
proyectado (shotcrete), clasificado como Gunita de acuerdo con la Tabla 3-4.

2410485-00-HID-INF-002 Rev_B

**Tabla 3-4 Coeficiente de Rugosidad, Canales Revestidos o Artificiales**

b) Secciones excavadas en roca

El canal de contorno se considera excavado en roca, con un nivel de irregularidad
equivalente a un coeficiente de Manning de 0,035, de acuerdo con la Tabla 3-5.

**Tabla 3-5 Coeficiente de Rugosidad, Canales Excavados y Uniformes**

2410485-00-HID-INF-002 Rev_B

c) Coeficiente de rugosidad adoptado

Para todos los efectos, se ha considerado que el canal y sus obras anexas como las gradas
escalonadas presentaran una superficie asimilable a hormigón platachado, por lo que se le
asignara el coeficiente de escurrimiento más alto posible indicado en la Tabla 3-4, es decir
un **n=0,015.**

**3.6** **CONDICIONES DE BORDE**

La modelación hidráulica del cauce en estudio requiere definir las condiciones de borde con
que se ejecutara la simulación, condiciones que dependerán del tipo de régimen de
escurrimiento, supercrítico o subcrítico.

El régimen subcrítico (o de rio), se impone cuando la pendiente longitudinal del fondo del
cauce es menor a la pendiente critica asociada al flujo, siendo necesario definir las
condiciones de borde existentes aguas abajo del tramo en análisis.

En el caso de régimen supercrítico (o de torrente), se impone en aquellos casos en que la
pendiente longitudinal del fondo del cauce es mayor (más fuerte) que la pendiente critica
asociada al flujo, siendo necesario definir las condiciones de borde existentes aguas arriba
del tramo en análisis.

Para el caso de cauces naturales, en que la sección transversal no es constante, es
complejo estimar la pendiente critica, por lo que, la práctica recomienda asumir el tipo de
régimen de escurrimiento de acuerdo con el siguiente criterio.

Régimen subcrítico, para pendientes longitudinales promedios con valor menor a
0,001 m/m

Régimen mixto, para pendientes longitudinales promedio entre 0,001 y 0,01 m/m y
cauces naturales.

Régimen supercrítico, para pendientes longitudinales promedios con valores
mayores a 0,01 m/m.

Para el caso en análisis, el canal presenta una pendiente longitudinal mínima de 0,5%
(0,005 m/m), por lo que, se asume un régimen de escurrimiento tipo supercrítico.

**4** **CANALES DE CONTORNO**

El cálculo de la cota de aguas máximas en el canal de contorno se determina mediante la
utilización del software HEC-RAS versión 4.0.; U.S. Army Corps of Engineers Hydrologic
Engineering Center, mayo de 2005

El cálculo se lleva a cabo por el método de factores de conducción hidráulica asumiendo
condiciones de escurrimiento gradualmente variada para cada una de las secciones de
cálculo.

El proceso se lleva a cabo mecánicamente empleando un software computacional cuyos
datos de entrada son la topografía del cauce, considerando perfiles transversales cada 50
m aproximadamente, lo que se complementa con los antecedentes de hidrología
representados por caudales de crecida y las condiciones hidráulicas que definen la
rugosidad.

2410485-00-HID-INF-002 Rev_B

El resultado está constituido por los parámetros hidráulicos del escurrimiento; niveles de
escurrimiento crítico y altura eje hidráulico, “coeficientes de conducción hidráulica”, etc.

Las rugosidades se determinan a través del Método de Cowan (V.T. Cowan, 1959), que,
haciendo uso de los datos de terreno, incorpora las características morfológicas del cauce
y el efecto relativo de las obstrucciones como componentes de la resistencia al
escurrimiento.

Para el análisis del funcionamiento hidráulico del sector se utiliza el software de aplicación
específica del Hydrologic Center - U.S. Army Corps of Engineers, HEC-RAS Water Surface
Profiles, Abril 1997.

Los fundamentos teóricos aplicados por el Hydrologic Center - U.S. Army Corps of
Engineers, en el modelo HEC-RAS Water Surface Profiles son los convencionales, y
corresponden al método de etapas fijas.

Conocida la geometría del cauce en términos de perfiles transversales y de planta del
sector, su caracterización rugosa (coeficiente de rugosidad), el caudal y la altura de
escurrimiento en una sección inicial 1, se determina por iteraciones de la altura en una
sección 2, ubicada a una distancia fija conocida, mediante el balance de Bernoulli o energía
específica.

2
2 +  2 - _v_ 2 = _h_ 1 + 

2
1 +  1 - _v_ 1

_h_ 2 +  2 - 2 _v_ 2 _g_ = _h_ 1 +  1 - 2 _v_ 1 _g_ + _H_ _e_

En que:

2
= _L_ - ~~_S_~~ + _C_ -  2 - _v_ 2 − 

2

 - _v_ 1

1

_H_ _e_ = _L_ - ~~_S_~~ _f_ + _C_ -  2 - _v_ 2 −  1 - _v_ 1
2 _g_ 2 _g_

h1, h2 = Cota superficial en secciones transversales 1 y 2.

V1, V2 = Velocidades media en secciones 1 y 2.

1, 2 = Coeficientes que afectan las alturas de velocidad, para compensar la

incerteza de suponer una distribución uniforme de la velocidad media a su
correspondiente sección.

He = Pérdida total de energía entre secciones.

L = Distancia entre las secciones; HEC-RAS calcula una longitud equivalente,

diferenciando las distancias entre perfiles transversales según se mida por
la planicie de inundación ubicada a la izquierda del cauce preferencial, por
la planicie ubicada a la derecha y la medida por el cauce propiamente tal,
ponderando la gravitación que cada una de estas distancias tenga en el
valor de L, de acuerdo a como se reparte el caudal entre estas áreas por
separado.

Sf = Pendiente de la línea de energía entre secciones; HEC-RAS presenta

diversas ecuaciones para estimar este valor. En este caso, lo
recomendable para un régimen fluvial es la ecuación que promedia la
pendiente evaluada en cada sección por separado, suponiendo flujo

2410485-00-HID-INF-002 Rev_B

normal en cada una de ellas. (Otras alternativas son la media geométrica,
la media armónica y la de conductancia promedio).

C = Coeficiente de expansión o contracción del flujo. Se considera valores de

0,3 y 0,1 respectivamente, para cambios de sección natural, que son
detectados por el programa según la variación de la velocidad media de
una sección a otra, y valores de 0,5 y 0,3 para expansión y contracción
asociados a la presencia de la Obra de Arte.

**4.1** **SEPARACIÓN EN SUBSECCIONES**

HEC-RAS permite la separación de los cauces activos de las planicies adyacentes de
inundación, lo que permite además adjudicar los coeficientes de rugosidad que
correspondan a cada subsección. Con lo anterior, obtiene un valor ponderado de coeficiente
de rugosidad para el lecho, mediante la expresión:

2 / 3
3

1  3
# =  

#   3 P i * n i 5.1 

 _i_ = 1 

# 1   P i * n i 5.1 

_P_  _i_ = 1 

# n c =  P i * n i

_P_

1

_i_ =

En esta expresión “ni” es el coeficiente de la subsección i, “P” es el perímetro mojado de la
sección completa y Pi es el perímetro mojado de la subsección i, que varía según la altura
del eje hidráulico.

La modelación del canal de contorno implica determinar la topografía necesaria, tal que los
resultados obtenidos sean representativos del régimen de escurrimiento del río en el sector
del emplazamiento de este.

**4.2** **CONSIDERACIONES DEL MODELO.**

Para la realización del modelo hidráulico se ha tenido en consideración que se trata de un
cauce uniforme, de un ancho definido, con nula presencia de embanque y escurrimiento
marcadamente supercrítico (torrente).

Se han incluido en el modelo todas las singularidades hidráulicas del cauce, de modo de
obtener resultados precisos sobre el comportamiento del escurrimiento.

**4.3** **RESULTADOS DE LA MODELACIÓN HIDRÁULICA**

El cálculo de la cota de aguas máximas en el perfil batimétrico se determina mediante la
utilización del software HEC-RAS; U.S. Army Corps of Engineers Hydrologic Engineering
Center, 1997.

El cálculo se lleva a cabo por el método de factores de conducción hidráulica asumiendo
condiciones de escurrimiento gradualmente variado para cada una de las secciones de
cálculo.

El proceso se lleva a cabo mecánicamente empleando un software computacional cuyos
datos de entrada son la topografía del cauce, considerando perfiles transversales cada 50
m aproximadamente, lo que se complementa con los antecedentes de hidrología
representados por caudales de crecida y las condiciones hidráulicas que definen la
rugosidad.

2410485-00-HID-INF-002 Rev_B

El resultado está constituido por los parámetros hidráulicos del escurrimiento; niveles de
escurrimiento crítico, altura del eje hidráulico, “coeficientes de conducción hidráulica”, y
otros similares.

**4.3.1 ANÁLISIS ESCENARIO CON PROYECTO**

La simulación de la situación con proyecto considera un canal de contorno con sección
trapecial revestida con shotcrete y armadura mínima (malla tipo ACMA) para resistir la
retracción, con una longitud total del canal existente alcanza un valor de 2144 metros
aproximadamente.

El canal de contorno proyectado considera una sección trapecial revestida con ancho basal
de 1,30 m, altura libre de 1,10 m y talud del canal y terreno H/V = 1/1 ( **Figura 4-1** ).

**Figura 4-1 Sección Canal Proyectado.**
Fuente: Plano 2410485-00-HOD-PLA-001, Anexo C.

La modelación del canal de contorno ha sido separada en tres tramos, separados por las
obras de disipación definidas como gradas de escalera, por lo que los resultados obtenidos
de la simulación se presentan separados según kilometraje para un mejor entendimiento.

2410485-00-HID-INF-002 Rev_B

**Figura 4-2 Distribución Espacial de Tramos de Canal de Contorno Proyectado.**

Fuente: Anexo C.

2410485-00-HID-INF-002 Rev_B Página 20 de 50

**4.3.2 RESULTADOS MODELACION TRAMO 1**

**Figura 4-3 Modelación Canal de Contorno - Tramo 1, Esquema Isométrico.**

2410485-00-HID-INF-002 Rev_B Página 21 de 50

**Figura 4-4 Modelación Canal de Contorno - Tramo 1, Eje Hidráulico.**

2410485-00-HID-INF-002 Rev_B Página 22 de 50

**Tabla 4-1 Modelación Canal de Contorno - Tramo 1, Resultados T=100**

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**0.00 **|2115.30|1.14|376.65|377.05|377.05|377.21|0.0028|1.90|0.68|2.10|0.96|
|**15.30 **|2100.00|1.14|376.42|376.68|376.82|377.11|0.0118|2.99|0.42|1.83|1.85|
|**31.30 **|2084.00|1.14|376.13|376.38|376.53|376.88|0.0156|3.26|0.38|1.79|2.10|
|**33.30 **|2082.00|1.14|376.08|376.48|376.48|376.65|0.0029|1.92|0.67|2.09|0.97|
|**35.30 **|2080.00|1.14|376.04|376.44|376.44|376.60|0.0028|1.91|0.68|2.10|0.97|
|**53.30 **|2062.00|1.14|375.62|375.85|376.02|376.45|0.0205|3.55|0.35|1.75|2.38|
|**55.30 **|2060.00|1.14|375.58|375.80|375.98|376.41|0.0207|3.56|0.35|1.75|2.39|
|**57.30 **|2058.00|1.14|375.53|375.76|375.93|376.37|0.0209|3.57|0.34|1.75|2.40|
|**67.30 **|2048.00|1.14|375.30|375.53|375.70|376.15|0.0219|3.62|0.34|1.75|2.45|
|**69.30 **|2046.00|1.14|375.26|375.48|375.65|376.11|0.0220|3.63|0.34|1.75|2.45|
|**75.30 **|2040.00|1.14|375.12|375.34|375.52|375.98|0.0222|3.64|0.34|1.74|2.47|
|**95.30 **|2020.00|1.14|374.66|374.88|375.06|375.52|0.0227|3.67|0.34|1.74|2.49|
|**111.30 **|2004.00|1.14|374.28|374.50|374.68|375.15|0.0232|3.69|0.33|1.74|2.51|
|**113.30 **|2002.00|1.14|374.22|374.44|374.62|375.10|0.0237|3.71|0.33|1.74|2.54|
|**115.30 **|2000.00|1.14|374.16|374.56|374.56|374.73|0.0029|1.92|0.67|2.09|0.97|
|**117.30 **|1998.00|1.14|374.11|374.50|374.50|374.67|0.0028|1.91|0.67|2.10|0.97|
|**119.30 **|1996.00|1.14|374.05|374.44|374.44|374.61|0.0028|1.91|0.68|2.10|0.97|
|**121.30 **|1994.00|1.14|373.99|374.30|374.39|374.59|0.0064|2.47|0.51|1.93|1.40|
|**123.30 **|1992.00|1.14|373.93|374.22|374.33|374.57|0.0087|2.72|0.46|1.88|1.62|
|**125.30 **|1990.00|1.14|373.87|374.14|374.27|374.54|0.0108|2.91|0.43|1.85|1.78|
|**127.30 **|1988.00|1.14|373.81|374.07|374.21|374.52|0.0127|3.06|0.41|1.82|1.91|
|**129.30 **|1986.00|1.14|373.75|374.00|374.15|374.49|0.0143|3.18|0.39|1.80|2.02|
|**135.30 **|1980.00|1.14|373.58|373.81|373.98|374.38|0.0188|3.46|0.36|1.77|2.29|
|**155.30 **|1960.00|1.14|372.99|373.39|373.39|373.55|0.0028|1.91|0.68|2.10|0.96|
|**165.30 **|1950.00|1.14|372.70|372.94|373.09|373.46|0.0165|3.32|0.37|1.78|2.15|
|**167.30 **|1948.00|1.14|372.64|372.87|373.03|373.43|0.0178|3.40|0.36|1.77|2.23|
|**175.30 **|1940.00|1.14|372.40|372.62|372.80|373.26|0.0223|3.64|0.34|1.74|2.47|
|**195.30 **|1920.00|1.14|371.85|372.06|372.25|372.77|0.0263|3.84|0.32|1.72|2.66|
|**203.30 **|1912.00|1.14|371.67|371.89|372.07|372.56|0.0240|3.73|0.33|1.73|2.55|
|**205.30 **|1910.00|1.14|371.63|371.84|372.02|372.51|0.0237|3.71|0.33|1.74|2.54|
|**209.67 **|1905.63|1.14|371.53|371.75|371.93|372.40|0.0230|3.68|0.33|1.74|2.51|
|**215.30 **|1900.00|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m|
|**230.00 **|1885.30|1.14|371.07|371.45|371.47|371.64|0.0033|2.02|0.64|2.06|1.05|
|**235.30 **|1880.00|1.14|370.52|370.72|370.92|371.53|0.0331|4.12|0.30|1.70|2.95|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**251.30 **|1864.00|1.98|368.85|369.09|369.41|370.74|0.0533|5.89|0.36|1.77|3.86|
|**253.30 **|1862.00|1.98|368.64|368.87|369.20|370.62|0.0581|6.05|0.35|1.76|4.01|
|**255.30 **|1860.00|1.98|368.43|368.66|368.99|370.50|0.0626|6.19|0.35|1.75|4.15|
|**257.30 **|1858.00|1.98|368.23|368.45|368.78|370.36|0.0668|6.31|0.34|1.74|4.28|
|**275.30 **|1840.00|1.98|366.64|366.85|367.20|369.01|0.0808|6.70|0.32|1.72|4.67|
|**295.30 **|1820.00|1.98|365.70|365.94|366.26|367.57|0.0521|5.85|0.37|1.78|3.82|
|**303.30 **|1812.00|1.98|365.59|365.86|366.15|367.12|0.0351|5.17|0.42|1.83|3.20|
|**305.30 **|1810.00|1.98|365.56|365.83|366.12|367.04|0.0323|5.04|0.43|1.85|3.08|
|**307.30 **|1808.00|1.98|365.53|365.81|366.09|366.96|0.0299|4.92|0.44|1.86|2.97|
|**309.30 **|1806.00|1.98|365.50|365.79|366.06|366.88|0.0277|4.81|0.45|1.87|2.87|
|**311.30 **|1804.00|1.98|365.48|365.77|366.03|366.81|0.0258|4.70|0.46|1.88|2.78|
|**313.30 **|1802.00|1.98|365.45|365.75|366.01|366.75|0.0243|4.61|0.47|1.89|2.70|
|**315.30 **|1800.00|1.98|365.42|365.72|365.98|366.69|0.0231|4.54|0.48|1.90|2.64|
|**317.30 **|1798.00|1.98|365.39|365.70|365.95|366.64|0.0219|4.47|0.49|1.91|2.58|
|**323.30 **|1792.00|1.98|365.31|365.62|365.86|366.49|0.0194|4.30|0.51|1.93|2.44|
|**325.30 **|1790.00|1.98|365.28|365.60|365.84|366.45|0.0187|4.25|0.52|1.94|2.40|
|**327.30 **|1788.00|1.98|365.25|365.57|365.81|366.41|0.0183|4.22|0.52|1.94|2.38|
|**335.30 **|1780.00|1.98|365.14|365.47|365.70|366.26|0.0166|4.10|0.54|1.96|2.28|
|**337.30 **|1778.00|1.98|365.11|365.45|365.67|366.22|0.0163|4.08|0.54|1.96|2.26|
|**339.30 **|1776.00|1.98|365.09|365.42|365.64|366.19|0.0161|4.06|0.54|1.97|2.25|
|**341.30 **|1774.00|1.98|365.06|365.39|365.61|366.15|0.0159|4.04|0.55|1.97|2.23|
|**343.30 **|1772.00|1.98|365.03|365.37|365.58|366.12|0.0157|4.02|0.55|1.97|2.22|
|**345.30 **|1770.00|1.98|365.00|365.34|365.56|366.09|0.0155|4.01|0.55|1.97|2.21|
|**347.30 **|1768.00|1.98|364.97|365.31|365.53|366.05|0.0153|4.00|0.55|1.97|2.20|
|**349.30 **|1766.00|1.98|364.95|365.28|365.50|366.02|0.0152|3.99|0.55|1.98|2.19|
|**355.30 **|1760.00|1.98|364.86|365.20|365.42|365.93|0.0148|3.95|0.56|1.98|2.16|
|**361.30 **|1754.00|1.98|364.78|365.12|365.33|365.84|0.0145|3.93|0.56|1.98|2.14|
|**375.30 **|1740.00|1.98|364.58|364.93|365.14|365.64|0.0143|3.91|0.57|1.99|2.13|
|**383.30 **|1732.00|1.98|364.47|364.82|365.03|365.53|0.0143|3.91|0.57|1.99|2.13|
|**395.30 **|1720.00|1.98|364.30|364.65|364.86|365.36|0.0142|3.91|0.57|1.99|2.13|
|**415.30 **|1700.00|1.98|364.03|364.37|364.58|365.07|0.0140|3.89|0.57|1.99|2.11|
|**425.30 **|1690.00|1.98|363.89|364.23|364.44|364.93|0.0140|3.89|0.57|1.99|2.11|
|**427.30 **|1688.00|1.98|363.86|364.20|364.42|364.91|0.0140|3.89|0.57|1.99|2.11|
|**429.30 **|1686.00|1.98|363.83|364.18|364.39|364.88|0.0140|3.89|0.57|1.99|2.11|
|**435.30 **|1680.00|1.98|363.50|363.80|364.05|364.75|0.0222|4.49|0.49|1.91|2.60|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**453.30 **|1662.00|2.88|362.58|362.94|363.27|364.28|0.0252|5.37|0.60|2.02|2.85|
|**455.30 **|1660.00|2.88|362.57|362.94|363.27|364.21|0.0233|5.25|0.62|2.04|2.75|
|**475.30 **|1640.00|2.88|362.46|362.90|363.15|363.75|0.0127|4.34|0.76|2.17|2.09|
|**479.30 **|1636.00|2.88|362.44|362.89|363.13|363.69|0.0116|4.20|0.79|2.20|2.00|
|**481.30 **|1634.00|2.88|362.42|362.88|363.12|363.66|0.0111|4.15|0.80|2.21|1.97|
|**483.30 **|1632.00|2.88|362.41|362.87|363.11|363.64|0.0108|4.11|0.81|2.22|1.94|
|**485.30 **|1630.00|2.88|362.40|362.87|363.10|363.61|0.0104|4.06|0.82|2.23|1.90|
|**487.30 **|1628.00|2.88|362.39|362.86|363.08|363.59|0.0100|4.02|0.83|2.23|1.88|
|**489.30 **|1626.00|2.88|362.38|362.85|363.07|363.56|0.0097|3.97|0.84|2.24|1.85|
|**491.30 **|1624.00|2.88|362.37|362.85|363.07|363.54|0.0094|3.93|0.85|2.25|1.82|
|**493.30 **|1622.00|2.88|362.36|362.84|363.06|363.52|0.0091|3.90|0.85|2.26|1.80|
|**495.30 **|1620.00|2.88|362.35|362.83|363.04|363.50|0.0089|3.87|0.86|2.26|1.78|
|**507.30 **|1608.00|2.88|362.15|362.61|362.85|363.38|0.0108|4.12|0.80|2.22|1.94|
|**515.30 **|1600.00|2.88|361.97|362.40|362.67|363.27|0.0130|4.37|0.75|2.17|2.11|
|**535.30 **|1580.00|2.88|361.51|361.91|362.21|362.95|0.0173|4.77|0.68|2.10|2.40|
|**545.30 **|1570.00|2.88|361.27|361.66|361.96|362.77|0.0190|4.92|0.66|2.08|2.51|
|**547.30 **|1568.00|2.88|361.22|361.60|361.91|362.73|0.0194|4.94|0.66|2.08|2.53|
|**549.30 **|1566.00|2.88|361.17|361.55|361.86|362.69|0.0197|4.97|0.65|2.08|2.55|
|**551.30 **|1564.00|2.88|361.11|361.50|361.81|362.65|0.0200|4.99|0.65|2.07|2.56|
|**553.30 **|1562.00|2.88|361.06|361.45|361.76|362.61|0.0203|5.02|0.65|2.07|2.58|
|**555.30 **|1560.00|2.88|361.01|361.40|361.71|362.57|0.0206|5.04|0.64|2.07|2.60|
|**563.30 **|1552.00|2.88|360.81|361.19|361.51|362.40|0.0216|5.11|0.63|2.06|2.65|
|**565.30 **|1550.00|2.88|360.76|361.14|361.46|362.35|0.0218|5.13|0.63|2.05|2.67|
|**567.30 **|1548.00|2.88|360.71|361.09|361.41|362.31|0.0219|5.14|0.63|2.05|2.67|
|**569.30 **|1546.00|2.88|360.66|361.04|361.36|362.26|0.0220|5.15|0.63|2.05|2.68|
|**575.30 **|1540.00|2.88|360.51|360.89|361.21|362.13|0.0225|5.18|0.63|2.05|2.71|
|**595.30 **|1520.00|2.88|360.01|360.38|360.71|361.66|0.0237|5.26|0.61|2.04|2.77|
|**597.30 **|1518.00|2.88|359.96|360.33|360.66|361.61|0.0238|5.27|0.61|2.04|2.77|
|**599.30 **|1516.00|2.88|359.91|360.28|360.60|361.56|0.0239|5.28|0.61|2.04|2.78|
|**601.30 **|1514.00|2.88|359.86|360.23|360.56|361.52|0.0239|5.28|0.61|2.03|2.78|
|**603.30 **|1512.00|2.88|359.81|360.18|360.50|361.47|0.0240|5.29|0.61|2.03|2.79|
|**605.30 **|1510.00|2.88|359.76|360.13|360.46|361.42|0.0241|5.29|0.61|2.03|2.79|
|**607.30 **|1508.00|2.88|359.71|360.08|360.41|361.37|0.0242|5.30|0.61|2.03|2.80|
|**609.30 **|1506.00|2.88|359.66|360.03|360.35|361.33|0.0242|5.30|0.61|2.03|2.80|
|**615.30 **|1500.00|2.88|359.51|359.87|360.19|361.18|0.0244|5.32|0.61|2.03|2.81|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**617.30 **|1498.00|2.88|359.46|359.82|360.16|361.13|0.0245|5.32|0.61|2.03|2.81|
|**619.30 **|1496.00|2.88|359.41|359.77|360.10|361.08|0.0246|5.33|0.61|2.03|2.82|
|**621.30 **|1494.00|2.88|359.36|359.72|360.06|361.04|0.0246|5.33|0.61|2.03|2.82|
|**623.30 **|1492.00|2.88|359.31|359.67|360.00|360.99|0.0247|5.33|0.61|2.03|2.82|
|**625.30 **|1490.00|2.88|359.26|359.62|359.95|360.94|0.0247|5.34|0.61|2.03|2.82|
|**635.30 **|1480.00|2.88|359.01|359.37|359.71|360.69|0.0248|5.35|0.60|2.03|2.83|
|**637.30 **|1478.00|2.88|358.96|359.32|359.65|360.64|0.0249|5.35|0.60|2.03|2.83|
|**639.30 **|1476.00|2.88|358.91|359.27|359.61|360.59|0.0247|5.34|0.61|2.03|2.82|
|**641.30 **|1474.00|2.88|358.89|359.26|359.59|360.53|0.0233|5.24|0.62|2.04|2.75|
|**643.30 **|1472.00|2.88|358.87|359.25|359.57|360.46|0.0219|5.14|0.63|2.05|2.67|
|**645.30 **|1470.00|2.88|358.85|359.24|359.55|360.41|0.0207|5.05|0.64|2.07|2.60|
|**647.30 **|1468.00|2.88|358.83|359.22|359.53|360.35|0.0196|4.96|0.66|2.08|2.54|
|**655.30 **|1460.00|2.88|358.76|359.17|359.46|360.17|0.0163|4.68|0.70|2.12|2.34|
|**669.30 **|1446.00|2.88|358.63|359.07|359.32|359.93|0.0130|4.35|0.76|2.17|2.11|
|**671.30 **|1444.00|2.88|358.61|359.05|359.31|359.90|0.0126|4.32|0.76|2.18|2.08|
|**673.30 **|1442.00|2.88|358.59|359.03|359.29|359.87|0.0125|4.30|0.77|2.18|2.07|
|**675.30 **|1440.00|2.88|358.58|359.02|359.27|359.85|0.0123|4.28|0.77|2.18|2.06|
|**677.30 **|1438.00|2.88|358.56|359.00|359.25|359.83|0.0121|4.27|0.77|2.19|2.05|
|**679.30 **|1436.00|2.88|358.54|358.98|359.24|359.80|0.0120|4.25|0.78|2.19|2.03|
|**681.30 **|1434.00|2.88|358.52|358.97|359.22|359.78|0.0119|4.24|0.78|2.19|2.02|
|**683.30 **|1432.00|2.88|358.50|358.95|359.19|359.76|0.0117|4.22|0.78|2.19|2.01|
|**685.30 **|1430.00|2.88|358.48|358.93|359.18|359.73|0.0116|4.21|0.78|2.20|2.00|
|**687.30 **|1428.00|2.88|358.46|358.91|359.16|359.71|0.0115|4.19|0.79|2.20|1.99|
|**689.30 **|1426.00|2.88|358.45|358.90|359.14|359.69|0.0114|4.18|0.79|2.20|1.99|
|**691.30 **|1424.00|3.74|358.43|359.18|359.24|359.55|0.0029|2.95|1.55|2.81|1.08|
|**693.30 **|1422.00|3.74|358.41|359.14|359.22|359.54|0.0033|3.08|1.48|2.76|1.15|
|**695.30 **|1420.00|3.74|358.39|359.10|359.20|359.53|0.0036|3.17|1.43|2.72|1.20|
|**697.30 **|1418.00|3.74|358.37|359.07|359.18|359.52|0.0038|3.25|1.39|2.70|1.24|
|**699.30 **|1416.00|3.74|358.35|359.04|359.16|359.51|0.0041|3.32|1.36|2.67|1.28|
|**701.30 **|1414.00|3.74|358.33|359.01|359.15|359.50|0.0044|3.39|1.33|2.65|1.32|
|**703.30 **|1412.00|3.74|358.32|358.98|359.13|359.49|0.0046|3.45|1.30|2.63|1.35|
|**705.30 **|1410.00|3.74|358.30|358.95|359.11|359.48|0.0049|3.50|1.28|2.61|1.38|
|**707.30 **|1408.00|3.74|358.28|358.93|359.09|359.47|0.0050|3.53|1.27|2.60|1.40|
|**709.30 **|1406.00|3.74|358.26|358.91|359.07|359.46|0.0051|3.57|1.26|2.59|1.42|
|**711.30 **|1404.00|3.74|358.24|358.88|359.05|359.44|0.0053|3.60|1.24|2.58|1.43|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**713.30 **|1402.00|3.74|358.22|358.86|359.04|359.43|0.0054|3.63|1.23|2.57|1.45|
|**715.30 **|1400.00|3.74|358.20|358.84|359.02|359.42|0.0056|3.66|1.22|2.56|1.47|
|**717.30 **|1398.00|3.74|358.19|358.81|359.00|359.41|0.0057|3.69|1.21|2.56|1.48|
|**719.30 **|1396.00|3.74|358.17|358.79|358.98|359.39|0.0058|3.71|1.20|2.55|1.50|
|**721.30 **|1394.00|3.74|358.15|358.77|358.96|359.38|0.0059|3.74|1.19|2.54|1.51|
|**723.30 **|1392.00|3.74|358.13|358.75|358.94|359.37|0.0061|3.77|1.18|2.54|1.53|
|**725.30 **|1390.00|3.74|358.11|358.73|358.92|359.35|0.0062|3.79|1.18|2.53|1.54|
|**727.30 **|1388.00|3.74|358.09|358.70|358.90|359.34|0.0063|3.81|1.17|2.52|1.56|
|**729.30 **|1386.00|3.74|358.08|358.68|358.89|359.33|0.0064|3.83|1.16|2.52|1.57|
|**735.30 **|1380.00|3.74|358.02|358.62|358.83|359.29|0.0068|3.90|1.14|2.50|1.61|
|**741.30 **|1374.00|3.74|357.96|358.56|358.78|359.24|0.0071|3.96|1.12|2.48|1.65|
|**743.30 **|1372.00|3.74|357.94|358.54|358.76|359.23|0.0072|3.98|1.11|2.48|1.65|
|**745.30 **|1370.00|3.74|357.93|358.51|358.74|359.21|0.0073|3.99|1.11|2.48|1.66|
|**755.30 **|1360.00|3.74|357.83|358.41|358.65|359.14|0.0077|4.06|1.09|2.46|1.70|
|**775.30 **|1340.00|3.74|357.65|358.22|358.46|358.97|0.0082|4.14|1.07|2.44|1.75|
|**777.30 **|1338.00|3.74|357.63|358.20|358.44|358.96|0.0082|4.15|1.06|2.44|1.76|
|**779.30 **|1336.00|3.74|357.61|358.18|358.42|358.94|0.0083|4.17|1.06|2.43|1.77|
|**781.30 **|1334.00|3.74|357.59|358.16|358.40|358.93|0.0084|4.18|1.06|2.43|1.77|
|**795.30 **|1320.00|3.74|357.46|358.03|358.28|358.81|0.0086|4.21|1.05|2.42|1.79|
|**801.30 **|1314.00|3.74|357.41|357.97|358.22|358.76|0.0087|4.22|1.04|2.42|1.80|
|**803.30 **|1312.00|3.74|357.39|357.95|358.20|358.73|0.0086|4.21|1.05|2.42|1.79|
|**805.30 **|1310.00|3.74|357.37|357.93|358.18|358.72|0.0086|4.22|1.04|2.42|1.80|
|**807.30 **|1308.00|3.74|357.35|357.91|358.17|358.70|0.0087|4.22|1.04|2.42|1.80|
|**809.30 **|1306.00|3.74|357.33|357.89|358.15|358.68|0.0087|4.23|1.04|2.42|1.81|
|**811.30 **|1304.00|3.74|357.32|357.88|358.13|358.67|0.0087|4.23|1.04|2.42|1.80|
|**813.30 **|1302.00|3.74|357.30|357.86|358.11|358.65|0.0088|4.24|1.04|2.42|1.81|
|**815.30 **|1300.00|3.74|357.28|357.84|358.09|358.63|0.0087|4.23|1.04|2.42|1.81|
|**831.30 **|1284.00|3.74|357.13|357.69|357.94|358.49|0.0089|4.25|1.03|2.41|1.82|
|**833.30 **|1282.00|3.74|357.11|357.67|357.92|358.47|0.0089|4.26|1.03|2.41|1.82|
|**835.30 **|1280.00|3.74|357.09|357.65|357.91|358.45|0.0089|4.26|1.03|2.41|1.82|
|**837.30 **|1278.00|3.74|357.08|357.63|357.89|358.43|0.0089|4.25|1.04|2.41|1.82|
|**855.30 **|1260.00|3.74|356.91|357.46|357.72|358.27|0.0090|4.27|1.03|2.41|1.83|
|**859.30 **|1256.00|3.74|356.87|357.43|357.68|358.23|0.0089|4.26|1.03|2.41|1.82|
|**861.30 **|1254.00|3.74|356.85|357.41|357.66|358.21|0.0089|4.26|1.03|2.41|1.82|
|**875.30 **|1240.00|3.74|356.72|357.28|357.53|358.08|0.0090|4.27|1.03|2.41|1.83|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**893.30 **|1222.00|3.74|356.56|357.11|357.37|357.92|0.0091|4.28|1.03|2.41|1.84|
|**895.30 **|1220.00|3.74|356.54|357.09|357.35|357.90|0.0090|4.27|1.03|2.41|1.83|
|**915.30 **|1200.00|4.65|356.37|357.11|357.29|357.72|0.0049|3.80|1.49|2.77|1.41|
|**921.30 **|1194.00|4.65|356.33|357.06|357.25|357.69|0.0051|3.84|1.48|2.76|1.44|
|**923.30 **|1192.00|4.65|356.32|357.05|357.24|357.68|0.0051|3.85|1.47|2.75|1.44|
|**925.30 **|1190.00|4.65|356.31|357.03|357.23|357.67|0.0051|3.85|1.47|2.75|1.44|
|**935.30 **|1180.00|4.65|356.24|356.96|357.16|357.61|0.0053|3.89|1.45|2.74|1.47|
|**943.30 **|1172.00|4.65|356.19|356.91|357.11|357.56|0.0054|3.92|1.44|2.73|1.48|
|**945.30 **|1170.00|4.65|356.18|356.89|357.10|357.55|0.0055|3.93|1.44|2.73|1.49|
|**947.30 **|1168.00|4.65|356.17|356.88|357.09|357.54|0.0054|3.92|1.44|2.73|1.48|
|**949.30 **|1166.00|4.65|356.15|356.87|357.07|357.53|0.0055|3.93|1.44|2.73|1.48|
|**951.30 **|1164.00|4.65|356.14|356.86|357.06|357.51|0.0054|3.92|1.44|2.73|1.48|
|**953.30 **|1162.00|4.65|356.13|356.84|357.05|357.50|0.0054|3.93|1.44|2.73|1.48|
|**955.30 **|1160.00|4.65|356.12|356.83|357.03|357.49|0.0054|3.92|1.44|2.73|1.48|
|**957.30 **|1158.00|4.65|356.10|356.82|357.02|357.48|0.0054|3.92|1.44|2.73|1.48|
|**959.30 **|1156.00|4.65|356.09|356.80|357.01|357.46|0.0055|3.93|1.44|2.73|1.48|
|**961.30 **|1154.00|4.65|356.08|356.79|356.99|357.45|0.0055|3.94|1.43|2.72|1.49|
|**963.30 **|1152.00|4.65|356.06|356.78|356.98|357.44|0.0054|3.93|1.44|2.73|1.48|
|**975.30 **|1140.00|4.65|355.99|356.70|356.91|357.37|0.0056|3.97|1.42|2.72|1.50|
|**981.30 **|1134.00|4.65|355.95|356.66|356.87|357.33|0.0057|3.98|1.42|2.71|1.51|
|**983.30 **|1132.00|4.65|355.94|356.64|356.86|357.32|0.0056|3.97|1.42|2.71|1.51|
|**985.30 **|1130.00|4.65|355.92|356.63|356.84|357.31|0.0056|3.97|1.42|2.72|1.50|
|**989.30 **|1126.00|4.65|355.89|356.59|356.81|357.28|0.0059|4.03|1.40|2.70|1.54|
|**995.30 **|1120.00|4.65|355.57|356.17|356.49|357.20|0.0105|4.86|1.14|2.50|2.01|
|**1009.30 **|1106.00|4.65|354.83|355.32|355.75|356.94|0.0206|6.01|0.90|2.30|2.72|
|**1011.30 **|1104.00|4.65|354.72|355.21|355.64|356.90|0.0219|6.13|0.88|2.28|2.80|
|**1013.30 **|1102.00|4.65|354.61|355.10|355.53|356.85|0.0231|6.24|0.86|2.27|2.86|
|**1015.30 **|1100.00|4.65|354.50|354.98|355.42|356.79|0.0243|6.34|0.85|2.25|2.93|
|**1035.30 **|1080.00|4.65|353.44|353.87|354.36|356.17|0.0348|7.10|0.75|2.16|3.45|
|**1055.30 **|1060.00|4.65|352.37|352.78|353.29|355.38|0.0418|7.53|0.70|2.12|3.75|
|**1075.30 **|1040.00|4.65|351.31|351.71|352.22|354.48|0.0463|7.77|0.68|2.10|3.93|
|**1095.30 **|1020.00|4.65|350.24|350.63|351.16|353.52|0.0491|7.92|0.66|2.08|4.04|
|**1107.03 **|1008.27|4.65|349.72|350.10|350.58|352.78|0.0680|7.25|0.64|2.06|4.15|
|**1111.03 **|1004.27|4.65|349.65|350.18|350.99|352.53|0.0245|6.80|0.69|1.31|2.99|
|**1113.30 **|1002.00|4.65|349.61|350.15|350.87|352.45|0.0372|6.73|0.70|1.31|2.94|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**1115.30 **|1000.00|4.65|349.58|350.12|350.77|352.36|0.0356|6.62|0.71|1.31|2.88|
|**1117.30 **|998.00|4.65|349.55|350.09|350.70|352.27|0.0341|6.53|0.72|1.31|2.82|
|**1119.30 **|996.00|4.65|349.51|350.07|350.61|352.18|0.0320|6.44|0.73|1.31|2.76|
|**1121.30 **|994.00|4.65|349.48|350.04|350.58|352.10|0.0307|6.36|0.74|1.31|2.71|
|**1123.30 **|992.00|4.65|349.44|350.01|350.54|352.02|0.0301|6.28|0.74|1.31|2.66|
|**1125.30 **|990.00|4.65|349.41|349.99|350.51|351.95|0.0283|6.21|0.75|1.31|2.61|
|**1127.30 **|988.00|4.65|349.38|349.96|350.48|351.88|0.0274|6.15|0.76|1.31|2.57|
|**1129.54 **|985.76|4.65|349.34|349.92|350.44|351.83|0.0176|6.12|0.76|1.31|2.56|
|**1135.54 **|979.76|4.65|348.22|348.69|349.34|351.59|0.0347|7.55|0.62|1.31|3.50|
|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|**Inicio Grada Escalonada N°1**|

Donde:

**Km.-** = kilometraje en sentido de avance del agua (utilizado en los planos de mov. de tierra)
**PT.-** = Nombre Perfil Transversal Modelado en HEC-RAS
**Q** = Caudal (L/s) **J** = Pendiente media de la línea de energía (m/m)
**Z1** = Cota de fondo m.s.m.m. **V** = Velocidad media de la sección (m/s)
**Z2** = Cota eje hidráulico m.s.m.m. **A** = Área de la sección (m2)

**Z3** = Cota de línea de energía m.s.m.m. **L** = Ancho de la superficie libre (m)

**Z4** = Cota de altura critica m.s.m.m. **F** = Valor de Froude

2410485-00-HID-INF-002 Rev_B

**4.3.3 RESULTADOS MODELACION TRAMO 2**

**Tabla 4-2 Modelación Canal de Contorno - Tramo 2, Resultados T=100**

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|**Fin Grada Escalonada N°1**|
|**1179.55 **|935.75|4.80|330.34|331.46|331.46|332.01|0.0021|3.28|1.48|1.66|0.99|
|**1181.30 **|934.00|4.80|330.31|331.39|331.47|332.00|0.0055|3.47|1.41|1.32|1.07|
|**1183.30 **|932.00|4.80|330.28|331.27|331.40|331.98|0.0052|3.73|1.30|1.32|1.20|
|**1185.30 **|930.00|4.80|330.24|331.23|331.42|331.96|0.0070|3.79|1.29|1.31|1.22|
|**1187.41 **|927.89|4.80|330.21|331.14|331.59|331.94|0.0039|3.97|1.22|1.32|1.31|
|**1191.41 **|923.89|4.80|330.15|330.73|331.08|331.88|0.0119|5.11|1.11|2.48|2.13|
|**1195.30 **|920.00|4.80|330.08|330.67|331.02|331.83|0.0122|5.15|1.10|2.47|2.15|
|**1203.30 **|912.00|4.80|329.95|330.53|330.89|331.73|0.0127|5.22|1.09|2.46|2.19|
|**1205.30 **|910.00|4.80|329.92|330.50|330.86|331.70|0.0129|5.23|1.08|2.45|2.20|
|**1207.30 **|908.00|4.80|329.89|330.46|330.82|331.68|0.0130|5.25|1.08|2.45|2.21|
|**1209.30 **|906.00|4.80|329.86|330.43|330.78|331.65|0.0131|5.26|1.08|2.45|2.22|
|**1211.30 **|904.00|4.80|329.82|330.40|330.76|331.62|0.0132|5.28|1.07|2.45|2.22|
|**1215.30 **|900.00|4.80|329.76|330.33|330.69|331.57|0.0133|5.30|1.07|2.44|2.24|
|**1225.30 **|890.00|4.80|329.60|330.16|330.53|331.43|0.0137|5.35|1.06|2.43|2.27|
|**1227.30 **|888.00|4.80|329.56|330.13|330.50|331.40|0.0139|5.36|1.05|2.43|2.28|
|**1229.30 **|886.00|4.80|329.53|330.10|330.47|331.37|0.0139|5.37|1.05|2.43|2.28|
|**1231.30 **|884.00|4.80|329.50|330.06|330.43|331.34|0.0140|5.38|1.05|2.43|2.29|
|**1235.30 **|880.00|4.80|329.43|330.00|330.37|331.28|0.0141|5.40|1.05|2.42|2.30|
|**1245.30 **|870.00|4.80|329.27|329.83|330.21|331.14|0.0145|5.44|1.04|2.42|2.32|
|**1255.30 **|860.00|4.80|329.11|329.67|330.05|330.99|0.0147|5.47|1.03|2.41|2.34|
|**1263.30 **|852.00|4.80|328.98|329.53|329.92|330.87|0.0150|5.50|1.03|2.41|2.36|
|**1265.30 **|850.00|4.80|328.95|329.50|329.88|330.84|0.0150|5.50|1.03|2.41|2.36|
|**1267.30 **|848.00|4.80|328.91|329.47|329.85|330.81|0.0151|5.51|1.02|2.40|2.36|
|**1269.30 **|846.00|4.80|328.88|329.43|329.82|330.78|0.0152|5.52|1.02|2.40|2.37|
|**1275.30 **|840.00|4.80|328.79|329.34|329.72|330.69|0.0152|5.53|1.02|2.40|2.38|
|**1283.30 **|832.00|4.80|328.66|329.21|329.59|330.57|0.0154|5.54|1.02|2.40|2.38|
|**1285.30 **|830.00|4.80|328.62|329.17|329.56|330.54|0.0154|5.55|1.02|2.40|2.39|
|**1287.30 **|828.00|4.80|328.59|329.14|329.53|330.51|0.0155|5.56|1.01|2.40|2.39|
|**1295.30 **|820.00|4.80|328.46|329.01|329.40|330.38|0.0156|5.57|1.01|2.40|2.40|
|**1299.30 **|816.00|4.80|328.40|328.94|329.33|330.32|0.0157|5.57|1.01|2.39|2.41|
|**1301.30 **|814.00|4.80|328.36|328.91|329.29|330.29|0.0157|5.58|1.01|2.39|2.41|
|**1303.30 **|812.00|4.80|328.33|328.88|329.27|330.26|0.0157|5.58|1.01|2.39|2.41|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**1305.30 **|810.00|4.80|328.30|328.85|329.24|330.23|0.0158|5.59|1.01|2.39|2.41|
|**1307.30 **|808.00|4.80|328.27|328.81|329.20|330.20|0.0158|5.59|1.01|2.39|2.42|
|**1315.30 **|800.00|4.80|328.14|328.68|329.07|330.07|0.0158|5.60|1.01|2.39|2.42|
|**1319.30 **|796.00|4.80|328.07|328.62|329.00|330.01|0.0159|5.60|1.01|2.39|2.42|
|**1321.30 **|794.00|4.80|328.04|328.58|328.98|329.98|0.0160|5.60|1.00|2.39|2.42|
|**1323.30 **|792.00|4.80|328.01|328.55|328.94|329.94|0.0159|5.60|1.01|2.39|2.42|
|**1325.30 **|790.00|4.80|327.97|328.52|328.91|329.91|0.0159|5.60|1.01|2.39|2.42|
|**1327.30 **|788.00|4.80|327.94|328.49|328.87|329.88|0.0159|5.60|1.00|2.39|2.42|
|**1329.30 **|786.00|4.80|327.91|328.46|328.84|329.84|0.0158|5.60|1.01|2.39|2.42|
|**1333.30 **|782.00|4.80|327.85|328.39|328.78|329.78|0.0159|5.60|1.01|2.39|2.42|
|**1335.30 **|780.00|4.80|327.81|328.36|328.75|329.75|0.0159|5.61|1.00|2.39|2.42|
|**1355.30 **|760.00|4.80|327.49|328.03|328.42|329.43|0.0160|5.62|1.00|2.39|2.43|
|**1373.30 **|742.00|4.80|326.25|326.69|327.18|328.95|0.0328|7.05|0.78|2.19|3.37|
|**1375.30 **|740.00|4.80|325.99|326.42|326.92|328.86|0.0369|7.32|0.75|2.16|3.55|
|**1395.30 **|720.00|4.80|323.38|323.73|324.32|327.68|0.0769|9.22|0.58|2.00|4.96|
|**1405.30 **|710.00|4.80|322.08|322.41|323.01|326.80|0.0905|9.71|0.55|1.97|5.34|
|**1415.30 **|700.00|4.80|320.77|321.10|321.71|325.81|0.1011|10.05|0.53|1.95|5.61|
|**1417.30 **|698.00|4.80|320.51|320.84|321.45|325.60|0.1030|10.10|0.53|1.95|5.66|
|**1435.30 **|680.00|4.80|318.16|318.48|319.10|323.61|0.1152|10.47|0.51|1.93|5.96|
|**1443.30 **|672.00|4.80|317.12|317.43|318.06|322.66|0.1189|10.56|0.50|1.92|6.04|
|**1445.30 **|670.00|4.80|316.86|317.17|317.79|322.42|0.1196|10.58|0.50|1.92|6.05|
|**1451.30 **|664.00|4.80|316.08|316.39|317.01|321.69|0.1213|10.64|0.50|1.92|6.09|
|**1455.30 **|660.00|4.80|315.56|315.87|316.49|321.20|0.1224|10.67|0.50|1.92|6.12|
|**1475.30 **|640.00|4.80|312.95|313.26|313.89|318.70|0.1264|10.77|0.49|1.91|6.21|
|**1493.30 **|622.00|4.80|310.60|310.91|311.54|316.41|0.1283|10.82|0.49|1.91|6.25|
|**1495.30 **|620.00|4.80|310.34|310.65|311.28|316.15|0.1284|10.83|0.49|1.91|6.26|
|**1503.30 **|612.00|4.80|309.30|309.61|310.24|315.12|0.1290|10.84|0.49|1.91|6.27|
|**1505.30 **|610.00|4.80|309.04|309.34|309.97|314.86|0.1290|10.84|0.49|1.91|6.27|
|**1507.30 **|608.00|4.80|308.78|309.08|309.71|314.60|0.1290|10.84|0.49|1.91|6.27|
|**1509.30 **|606.00|4.80|308.52|308.82|309.45|314.34|0.1290|10.85|0.49|1.91|6.27|
|**1511.30 **|604.00|4.80|308.26|308.56|309.19|314.09|0.1292|10.85|0.49|1.91|6.27|
|**1513.30 **|602.00|4.80|308.00|308.30|308.93|313.83|0.1293|10.85|0.49|1.91|6.28|
|**1515.30 **|600.00|4.80|307.74|308.04|308.67|313.57|0.1294|10.85|0.49|1.91|6.28|
|**1535.30 **|580.00|4.80|305.13|305.43|306.07|310.98|0.1298|10.87|0.49|1.91|6.29|
|**1555.30 **|560.00|4.80|302.52|302.83|303.45|308.38|0.1301|10.87|0.49|1.91|6.29|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**1575.30 **|540.00|4.80|299.92|300.22|300.85|305.77|0.1303|10.88|0.49|1.91|6.30|
|**1583.30 **|532.00|4.80|298.87|299.18|299.80|304.73|0.1305|10.88|0.49|1.91|6.30|
|**1585.30 **|530.00|4.80|298.61|298.91|299.54|304.47|0.1305|10.88|0.49|1.91|6.30|
|**1587.30 **|528.00|4.80|298.35|298.65|299.29|304.21|0.1305|10.88|0.49|1.91|6.30|
|**1589.30 **|526.00|4.80|298.09|298.39|299.02|303.95|0.1302|10.88|0.49|1.91|6.30|
|**1591.30 **|524.00|4.80|297.83|298.13|298.76|303.69|0.1307|10.88|0.49|1.91|6.30|
|**1595.30 **|520.00|4.80|297.31|297.61|298.24|303.17|0.1303|10.88|0.49|1.91|6.30|
|**1614.38 **|500.92|4.80|294.82|295.12|295.75|300.68|0.1303|10.88|0.49|1.91|6.30|
|**1615.30 **|500.00|4.80|294.82|295.17|295.85|300.52|0.0954|10.30|0.49|1.67|5.53|
|**1618.38 **|496.92|4.80|294.80|295.18|295.90|300.13|0.0810|9.86|0.49|1.31|5.14|
|**1619.30 **|496.00|4.80|294.80|295.18|295.95|300.00|0.1086|9.73|0.50|1.31|5.03|
|**1621.30 **|494.00|4.80|294.79|295.19|295.94|299.70|0.0985|9.42|0.51|1.31|4.80|
|**1623.30 **|492.00|4.80|294.78|295.19|295.92|299.43|0.0897|9.13|0.53|1.31|4.58|
|**1625.30 **|490.00|4.80|294.78|295.19|295.82|299.19|0.0817|8.86|0.55|1.31|4.37|
|**1627.30 **|488.00|4.80|294.77|295.20|295.25|298.96|0.0748|8.60|0.56|1.31|4.18|
|**1629.04 **|486.26|4.80|294.47|294.94|294.94|294.96|0.0001|0.40|8.45|9.56|0.19|
|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|

Donde:

**Km.-** = kilometraje en sentido de avance del agua (utilizado en los planos de mov. de tierra)
**PT.-** = Nombre Perfil Transversal Modelado en HEC-RAS
**Q** = Caudal (L/s) **J** = Pendiente media de la línea de energía (m/m)
**Z1** = Cota de fondo m.s.m.m. **V** = Velocidad media de la sección (m/s)
**Z2** = Cota eje hidráulico m.s.m.m. **A** = Área de la sección (m2)

**Z3** = Cota de línea de energía m.s.m.m. **L** = Ancho de la superficie libre (m)

**Z4** = Cota de altura critica m.s.m.m. **F** = Valor de Froude

2410485-00-HID-INF-002 Rev_B

**Figura 4-5 Modelación Canal de Contorno - Tramo 2, Esquema Isométrico.**

2410485-00-HID-INF-002 Rev_B Página 33 de 50

**Figura 4-6 Modelación Canal de Contorno - Tramo 2, Eje Hidráulico.**

2410485-00-HID-INF-002 Rev_B Página 34 de 50

**4.3.4 RESULTADOS MODELACION TRAMO 3**

**Tabla 4-3 Modelación Canal de Contorno - Tramo 3, Resultados T=100**

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|**Inicio Grada Escalonada N°2**|
|**1690.53 **|424.77|4.80|276.49|277.60|277.60|278.16|0.0081|3.32|1.45|1.30|1.00|
|**1691.30 **|424.00|4.80|276.45|277.45|277.57|278.14|0.0106|3.69|1.30|1.30|1.18|
|**1693.30 **|422.00|4.80|276.35|277.25|277.46|278.10|0.0137|4.08|1.18|1.30|1.37|
|**1695.30 **|420.00|4.80|276.25|277.10|277.37|278.06|0.0161|4.35|1.10|1.30|1.51|
|**1697.30 **|418.00|4.80|276.15|276.96|277.25|278.02|0.0182|4.55|1.05|1.30|1.61|
|**1698.55 **|416.75|4.80|276.09|276.88|277.34|277.99|0.0192|4.66|1.03|1.30|1.67|
|**1702.55 **|412.75|4.80|275.88|276.28|276.68|277.85|0.0272|5.98|0.90|2.52|3.01|
|**1709.63 **|405.67|4.80|275.53|276.04|276.47|277.68|0.0202|6.05|0.92|2.32|2.70|
|**1715.30 **|400.00|4.80|275.24|275.73|276.17|277.54|0.0234|6.34|0.88|2.28|2.89|
|**1735.30 **|380.00|4.80|274.23|274.67|275.16|276.94|0.0329|7.06|0.78|2.19|3.38|
|**1739.30 **|376.00|4.80|274.02|274.46|274.95|276.79|0.0344|7.16|0.77|2.18|3.44|
|**1741.30 **|374.00|4.80|273.92|274.36|274.85|276.72|0.0351|7.21|0.76|2.18|3.47|
|**1743.30 **|372.00|4.80|273.82|274.26|274.76|276.65|0.0358|7.25|0.76|2.17|3.50|
|**1745.30 **|370.00|4.80|273.72|274.15|274.66|276.57|0.0364|7.29|0.75|2.17|3.53|
|**1747.30 **|368.00|4.80|273.62|274.05|274.55|276.50|0.0371|7.33|0.75|2.16|3.56|
|**1749.30 **|366.00|4.80|273.52|273.95|274.45|276.42|0.0377|7.37|0.74|2.16|3.59|
|**1751.30 **|364.00|4.80|273.42|273.84|274.35|276.34|0.0382|7.40|0.74|2.16|3.61|
|**1753.30 **|362.00|4.80|273.32|273.74|274.25|276.26|0.0387|7.44|0.74|2.15|3.63|
|**1755.30 **|360.00|4.80|273.21|273.64|274.15|276.18|0.0393|7.47|0.73|2.15|3.66|
|**1757.30 **|358.00|4.80|273.11|273.54|274.05|276.10|0.0399|7.50|0.73|2.15|3.68|
|**1759.30 **|356.00|4.80|273.01|273.43|273.95|276.02|0.0404|7.53|0.73|2.14|3.70|
|**1761.30 **|354.00|4.80|272.91|273.33|273.85|275.94|0.0408|7.56|0.72|2.14|3.72|
|**1763.30 **|352.00|4.80|272.81|273.23|273.74|275.85|0.0413|7.58|0.72|2.14|3.74|
|**1765.30 **|350.00|4.80|272.71|273.13|273.64|275.77|0.0417|7.61|0.72|2.14|3.76|
|**1767.30 **|348.00|4.80|272.61|273.02|273.54|275.68|0.0421|7.63|0.72|2.13|3.77|
|**1769.30**|346.00|4.80|272.50|272.92|273.44|275.60|0.0425|7.65|0.71|2.13|3.79|
|**1771.30**|344.00|4.80|272.40|272.82|273.34|275.51|0.0428|7.67|0.71|2.13|3.80|
|**1773.30**|342.00|4.80|272.30|272.72|273.24|275.42|0.0432|7.69|0.71|2.13|3.82|
|**1775.30**|340.00|4.80|272.20|272.61|273.13|275.33|0.0435|7.71|0.71|2.13|3.83|
|**1777.30**|338.00|4.80|272.10|272.51|273.04|275.24|0.0438|7.73|0.71|2.12|3.84|
|**1779.30**|336.00|4.80|272.00|272.41|272.93|275.15|0.0441|7.74|0.70|2.12|3.85|
|**1781.30**|334.00|4.80|271.90|272.31|272.83|275.06|0.0443|7.76|0.70|2.12|3.86|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**1783.30**|332.00|4.80|271.80|272.21|272.73|274.97|0.0446|7.77|0.70|2.12|3.87|
|**1785.30**|330.00|4.80|271.70|272.10|272.63|274.88|0.0449|7.79|0.70|2.12|3.88|
|**1787.30**|328.00|4.80|271.59|272.00|272.53|274.79|0.0451|7.80|0.70|2.12|3.89|
|**1789.30**|326.00|4.80|271.49|271.90|272.43|274.69|0.0453|7.81|0.70|2.12|3.90|
|**1791.30**|324.00|4.80|271.39|271.80|272.33|274.60|0.0455|7.82|0.70|2.12|3.91|
|**1793.30**|322.00|4.80|271.29|271.70|272.22|274.51|0.0457|7.84|0.70|2.11|3.92|
|**1795.30**|320.00|4.80|271.19|271.60|272.12|274.41|0.0460|7.85|0.69|2.11|3.93|
|**1797.30**|318.00|4.80|271.09|271.49|272.02|274.32|0.0462|7.86|0.69|2.11|3.93|
|**1815.30**|300.00|4.80|270.18|270.58|271.11|273.47|0.0478|7.94|0.69|2.10|4.00|
|**1821.30**|294.00|4.80|269.87|270.27|270.81|273.18|0.0481|7.96|0.68|2.10|4.01|
|**1823.30**|292.00|4.80|269.77|270.17|270.71|273.08|0.0482|7.97|0.68|2.10|4.01|
|**1825.30**|290.00|4.80|269.67|270.07|270.61|272.99|0.0484|7.97|0.68|2.10|4.02|
|**1827.30**|288.00|4.80|269.57|269.97|270.51|272.89|0.0485|7.98|0.68|2.10|4.02|
|**1829.30**|286.00|4.80|269.47|269.87|270.41|272.79|0.0486|7.98|0.68|2.10|4.03|
|**1831.30**|284.00|4.80|269.39|269.79|270.33|272.69|0.0480|7.95|0.68|2.10|4.00|
|**1833.30**|282.00|4.80|269.32|269.72|270.25|272.59|0.0470|7.90|0.69|2.11|3.97|
|**1835.30**|280.00|4.80|269.25|269.65|270.18|272.48|0.0462|7.86|0.69|2.11|3.94|
|**1837.30**|278.00|4.80|269.18|269.58|270.11|272.38|0.0455|7.82|0.70|2.12|3.91|
|**1839.30**|276.00|4.80|269.10|269.51|270.04|272.28|0.0447|7.78|0.70|2.12|3.88|
|**1841.30**|274.00|4.80|269.03|269.44|269.97|272.18|0.0441|7.74|0.70|2.12|3.85|
|**1843.30**|272.00|4.80|268.96|269.37|269.90|272.09|0.0435|7.71|0.71|2.13|3.83|
|**1845.30**|270.00|4.80|268.89|269.30|269.82|272.00|0.0430|7.68|0.71|2.13|3.81|
|**1847.30**|268.00|4.80|268.82|269.23|269.75|271.90|0.0424|7.65|0.71|2.13|3.79|
|**1849.30**|266.00|4.80|268.74|269.16|269.68|271.81|0.0419|7.62|0.72|2.13|3.77|
|**1851.30**|264.00|4.80|268.67|269.09|269.61|271.72|0.0415|7.60|0.72|2.14|3.75|
|**1853.30**|262.00|4.80|268.60|269.02|269.54|271.64|0.0412|7.58|0.72|2.14|3.74|
|**1855.30**|260.00|4.80|268.53|268.95|269.46|271.55|0.0408|7.56|0.72|2.14|3.72|
|**1857.30**|258.00|4.80|268.46|268.88|269.39|271.47|0.0405|7.54|0.73|2.14|3.71|
|**1859.30**|256.00|4.80|268.38|268.81|269.32|271.38|0.0401|7.51|0.73|2.15|3.69|
|**1861.30**|254.00|4.80|268.34|268.76|269.27|271.29|0.0389|7.44|0.74|2.15|3.64|
|**1863.30**|252.00|4.80|268.30|268.73|269.23|271.19|0.0375|7.36|0.74|2.16|3.58|
|**1865.30**|250.00|4.80|268.26|268.69|269.19|271.10|0.0363|7.28|0.75|2.17|3.53|
|**1867.30**|248.00|4.80|268.22|268.66|269.15|271.01|0.0351|7.21|0.76|2.18|3.47|
|**1869.30**|246.00|4.80|268.18|268.62|269.11|270.93|0.0340|7.14|0.77|2.18|3.43|
|**1871.30**|244.00|4.80|268.14|268.58|269.07|270.85|0.0331|7.07|0.78|2.19|3.38|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**1873.30**|242.00|4.80|268.10|268.55|269.03|270.77|0.0322|7.01|0.79|2.20|3.34|
|**1875.30**|240.00|4.80|268.06|268.51|268.99|270.70|0.0313|6.95|0.79|2.20|3.30|
|**1877.30**|238.00|4.80|268.02|268.47|268.95|270.62|0.0305|6.89|0.80|2.21|3.26|
|**1879.30**|236.00|4.80|267.98|268.43|268.91|270.55|0.0298|6.84|0.81|2.22|3.22|
|**1885.30**|230.00|4.80|267.85|268.32|268.79|270.35|0.0280|6.71|0.82|2.23|3.13|
|**1887.30**|228.00|4.80|267.82|268.28|268.75|270.29|0.0274|6.67|0.83|2.24|3.11|
|**1889.30**|226.00|4.80|267.78|268.25|268.71|270.23|0.0270|6.63|0.84|2.24|3.08|
|**1891.30**|224.00|4.80|267.74|268.21|268.67|270.17|0.0265|6.59|0.84|2.25|3.06|
|**1893.30**|222.00|4.80|267.69|268.17|268.63|270.11|0.0260|6.56|0.85|2.25|3.03|
|**1895.30**|220.00|4.80|267.65|268.13|268.59|270.05|0.0256|6.52|0.85|2.26|3.01|
|**1897.30**|218.00|4.80|267.62|268.09|268.55|269.99|0.0253|6.49|0.85|2.26|2.99|
|**1899.30**|216.00|4.80|267.57|268.06|268.51|269.94|0.0249|6.47|0.86|2.26|2.97|
|**1901.30**|214.00|4.80|267.53|268.02|268.47|269.89|0.0247|6.45|0.86|2.27|2.96|
|**1903.30**|212.00|4.80|267.49|267.98|268.43|269.84|0.0245|6.43|0.86|2.27|2.95|
|**1905.30**|210.00|4.80|267.45|267.94|268.39|269.79|0.0243|6.41|0.87|2.27|2.94|
|**1907.30**|208.00|4.80|267.41|267.90|268.35|269.74|0.0241|6.40|0.87|2.27|2.93|
|**1909.30**|206.00|4.80|267.37|267.86|268.31|269.69|0.0239|6.38|0.87|2.27|2.92|
|**1911.30**|204.00|4.80|267.33|267.82|268.27|269.64|0.0237|6.37|0.87|2.28|2.91|
|**1913.30**|202.00|4.80|267.29|267.78|268.23|269.59|0.0235|6.35|0.88|2.28|2.90|
|**1915.30**|200.00|4.80|267.25|267.74|268.19|269.55|0.0234|6.34|0.88|2.28|2.89|
|**1935.30**|180.00|4.80|266.85|267.35|267.79|269.07|0.0217|6.19|0.90|2.30|2.80|
|**1955.30**|160.00|4.80|266.45|266.96|267.38|268.63|0.0209|6.11|0.91|2.31|2.74|
|**1975.30**|140.00|4.80|266.05|266.56|266.98|268.21|0.0205|6.08|0.92|2.32|2.72|
|**1977.30**|138.00|4.80|266.01|266.52|266.94|268.17|0.0205|6.08|0.92|2.32|2.72|
|**1979.30**|136.00|4.80|265.97|266.48|266.90|268.13|0.0205|6.08|0.92|2.32|2.72|
|**1981.30**|134.00|4.80|265.93|266.44|266.86|268.09|0.0205|6.08|0.92|2.32|2.72|
|**1983.30**|132.00|4.80|265.89|266.40|266.83|268.05|0.0205|6.08|0.92|2.32|2.72|
|**1985.30**|130.00|4.80|265.85|266.36|266.78|268.01|0.0205|6.08|0.92|2.32|2.72|
|**1987.30**|128.00|4.80|265.81|266.32|266.75|267.97|0.0205|6.07|0.92|2.32|2.72|
|**1989.30**|126.00|4.80|265.77|266.28|266.71|267.93|0.0205|6.08|0.92|2.32|2.72|
|**1991.30**|124.00|4.80|265.73|266.24|266.66|267.89|0.0205|6.07|0.92|2.32|2.72|
|**1993.30**|122.00|4.80|265.69|266.20|266.62|267.85|0.0204|6.07|0.92|2.32|2.72|
|**1995.30**|120.00|4.80|265.65|266.16|266.59|267.81|0.0205|6.07|0.92|2.32|2.72|
|**1997.30**|118.00|4.80|265.61|266.12|266.54|267.77|0.0205|6.07|0.92|2.32|2.72|
|**1999.30**|116.00|4.80|265.57|266.08|266.50|267.73|0.0205|6.07|0.92|2.32|2.72|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**2001.30**|114.00|4.80|265.53|266.04|266.46|267.69|0.0205|6.07|0.92|2.32|2.72|
|**2003.30**|112.00|4.80|265.49|266.00|266.42|267.64|0.0204|6.07|0.92|2.32|2.72|
|**2005.30**|110.00|4.80|265.45|265.96|266.38|267.60|0.0204|6.07|0.92|2.32|2.72|
|**2007.30**|108.00|4.80|265.41|265.92|266.34|267.56|0.0204|6.07|0.92|2.32|2.72|
|**2009.30**|106.00|4.80|265.36|265.87|266.30|267.52|0.0205|6.08|0.92|2.32|2.72|
|**2011.30**|104.00|4.80|265.27|265.77|266.21|267.48|0.0214|6.17|0.90|2.30|2.78|
|**2013.30**|102.00|4.80|265.17|265.66|266.10|267.43|0.0227|6.28|0.89|2.29|2.85|
|**2015.30**|100.00|4.80|265.06|265.55|265.99|267.37|0.0239|6.38|0.87|2.28|2.92|
|**2017.30**|98.00|4.80|264.95|265.43|265.89|267.32|0.0250|6.47|0.86|2.26|2.98|
|**2019.30**|96.00|4.80|264.84|265.32|265.78|267.26|0.0261|6.57|0.84|2.25|3.04|
|**2021.30**|94.00|4.80|264.74|265.21|265.67|267.20|0.0272|6.65|0.83|2.24|3.09|
|**2023.30**|92.00|4.80|264.63|265.10|265.56|267.14|0.0282|6.73|0.82|2.23|3.15|
|**2025.30**|90.00|4.80|264.52|264.98|265.46|267.07|0.0292|6.80|0.81|2.22|3.19|
|**2027.30**|88.00|4.80|264.41|264.87|265.35|267.01|0.0302|6.87|0.80|2.21|3.24|
|**2029.30**|86.00|4.80|264.31|264.76|265.24|266.94|0.0311|6.94|0.79|2.21|3.29|
|**2031.30**|84.00|4.80|264.20|264.65|265.13|266.87|0.0320|7.00|0.79|2.20|3.33|
|**2033.30**|82.00|4.80|264.09|264.54|265.03|266.80|0.0329|7.06|0.78|2.19|3.37|
|**2035.30**|80.00|4.80|263.99|264.43|264.92|266.73|0.0338|7.12|0.77|2.19|3.41|
|**2037.30**|78.00|4.80|263.88|264.32|264.81|266.66|0.0346|7.18|0.77|2.18|3.45|
|**2039.30**|76.00|4.80|263.77|264.21|264.71|266.59|0.0354|7.23|0.76|2.17|3.49|
|**2041.30**|74.00|4.80|263.67|264.10|264.60|266.51|0.0362|7.28|0.75|2.17|3.52|
|**2043.30**|72.00|4.80|263.56|263.99|264.49|266.43|0.0370|7.33|0.75|2.16|3.56|
|**2045.30**|70.00|4.80|263.45|263.88|264.39|266.36|0.0377|7.37|0.74|2.16|3.59|
|**2047.30**|68.00|4.80|263.35|263.77|264.28|266.28|0.0384|7.41|0.74|2.16|3.62|
|**2049.30**|66.00|4.80|263.24|263.66|264.18|266.20|0.0391|7.45|0.73|2.15|3.65|
|**2051.30**|64.00|4.80|263.15|263.57|264.08|266.12|0.0393|7.47|0.73|2.15|3.66|
|**2053.30**|62.00|4.80|263.07|263.49|264.00|266.04|0.0394|7.47|0.73|2.15|3.66|
|**2055.30**|60.00|4.80|262.99|263.41|263.92|265.96|0.0394|7.48|0.73|2.15|3.66|
|**2057.30**|58.00|4.80|262.90|263.33|263.84|265.88|0.0395|7.48|0.73|2.15|3.67|
|**2059.30**|56.00|4.80|262.82|263.25|263.76|265.80|0.0395|7.48|0.73|2.15|3.67|
|**2061.30**|54.00|4.80|262.74|263.17|263.68|265.72|0.0396|7.49|0.73|2.15|3.67|
|**2063.30**|52.00|4.80|262.66|263.09|263.60|265.65|0.0397|7.49|0.73|2.15|3.67|
|**2067.30**|48.00|4.80|262.58|263.01|263.51|265.46|0.0372|7.34|0.75|2.16|3.56|
|**2069.30**|46.00|4.80|262.57|263.00|263.50|265.35|0.0348|7.19|0.76|2.18|3.46|
|**2071.30**|44.00|4.80|262.56|263.00|263.49|265.25|0.0327|7.05|0.78|2.19|3.36|

2410485-00-HID-INF-002 Rev_B

|Km|PT|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Km**|**PT**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|**2073.30**|42.00|4.80|262.55|263.00|263.48|265.16|0.0308|6.91|0.80|2.21|3.27|
|**2075.30**|40.00|4.80|262.53|263.00|263.47|265.08|0.0291|6.79|0.81|2.22|3.19|
|**2077.30**|38.00|4.80|262.52|262.99|263.46|265.00|0.0274|6.66|0.83|2.24|3.10|
|**2079.30**|36.00|4.80|262.52|262.99|263.45|264.92|0.0259|6.54|0.85|2.25|3.02|
|**2081.30**|34.00|4.80|262.51|262.99|263.44|264.85|0.0245|6.43|0.86|2.27|2.95|
|**2091.30**|24.00|4.80|262.46|262.97|263.39|264.54|0.0191|5.94|0.94|2.34|2.63|
|**2093.30**|22.00|4.80|262.45|262.97|263.38|264.49|0.0182|5.84|0.96|2.35|2.57|
|**2095.30**|20.00|4.80|262.43|262.97|263.37|264.44|0.0173|5.76|0.98|2.36|2.52|
|**2097.30**|18.00|4.80|262.42|262.96|263.36|264.39|0.0166|5.67|0.99|2.38|2.47|
|**2099.30**|16.00|4.80|262.42|262.96|263.35|264.35|0.0158|5.59|1.01|2.39|2.42|
|**2101.30**|14.00|4.80|262.41|262.96|263.34|264.30|0.0152|5.52|1.02|2.40|2.37|
|**2103.30**|12.00|4.80|262.40|262.95|263.33|264.26|0.0145|5.44|1.04|2.42|2.32|
|**2115.30**|0.00|4.80|262.34|262.93|263.27|264.06|0.0116|5.07|1.12|2.48|2.10|
|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|**Descarga a Cauce Natural**|

Donde:

**Km.-** = kilometraje en sentido de avance del agua (utilizado en los planos de mov. de tierra)
**PT.-** = Nombre Perfil Transversal Modelado en HEC-RAS

**Q** = Caudal (L/s) **J** = Pendiente media de la línea de energía (m/m)
**Z1** = Cota de fondo m.s.m.m. **V** = Velocidad media de la sección (m/s)
**Z2** = Cota eje hidráulico m.s.m.m. **A** = Área de la sección (m2)

**Z3** = Cota de línea de energía m.s.m.m. **L** = Ancho de la superficie libre (m)

**Z4** = Cota de altura critica m.s.m.m. **F** = Valor de Froude

2410485-00-HID-INF-002 Rev_B

**Figura 4-7 Modelación Canal de Contorno - Tramo 3, Eje Hidráulico.**

2410485-00-HID-INF-002 Rev_B Página 40 de 50

**Figura 4-8 Modelación Canal de Contorno - Tramo 3, Esquema Isométrico.**

2410485-00-HID-INF-002 Rev_B Página 41 de 50

**5** **GRADAS ESCALONADAS**

El proyecto de canal de contorno considera la implementación de 2 dispositivos de disipación
de energía constituidos por gradas escalonadas, destinadas a salvar la diferencia de cota
entre dos tramos de canal.

Para lo anterior, se ha adoptado como solución la ejecución de una estructura formada por
una **rápida escalonada sin vertedero** con dimensiones tal que garanticen la formación de
resalto completo.

El diseño de la estructura se basa en el procedimiento indicado en el libro Hidráulica de
Francisco Javier Domínguez, en que conocido una altura de grada se bajada, es posible
determinar la altura de escurrimiento del flujo aguas abajo y la longitud a la que ocurre esta.

**5.1** **DISEÑO GEOMETRICO**

La estructura de la rápida escalonada se proyecta con sección transversal rectangular de
ancho basal 1,30 metros y altura libre de 1,10 metros, con altura de grada igual a 2,0 metros,
de manera de asegurar que el valor k sea mayor a 1,5 (ver Figura 5-1)

**Figura 5-1 Altura de Escurrimiento - Aguas abajo de Grada de Bajada**

2410485-00-HID-INF-002 Rev_B

La longitud de grada quedara definida de acuerdo con la aplicación de los 2 criterios
siguientes.

 Longitud mínima: Sera tal que garantice la formación perfecta del flujo supercrítico que
sigue a cada grada, de acuerdo con lo indica por Francisco Javier Domínguez (Figura
5-2).

**Figura 5-2 Longitud de Torrente - Aguas abajo de Grada de Bajada**

 Longitud máxima: Se adoptará la longitud que mejor se ajuste a la pendiente del
terreno natural, reduciendo el movimiento de tierra.

2410485-00-HID-INF-002 Rev_B

**5.2** **VERIFICACION DE LA OBRA DE DESCARGA - GRADA ESCALONADA N° 2**

Tomando en cuenta la envergadura del proyecto y la falta de espacio para proyectar un
disipador de energía tipo USBR, se considera la materialización de una grada escalonada
entre los kilómetros 1.135,54 y 1.179,55 (Figura 5-3).

2410485-00-HID-INF-002 Rev_B

**Figura 5-3 Grada Escalonadas N°1.**

Fuente: Anexo C.

2410485-00-HID-INF-002 Rev_B Página 45 de 50

Se ha estimado que un total de 10 gradas con altura de 1,9 metros cada una, permite cumplir
con los criterios de diseño de longitud máxima y mínima.

La verificación hidráulica de la grada se resume en la Tabla 5-1.

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Se ha estimado que un total de 10 gradas con altura de 1,9 metros cada una, permite cumplir con los criterios de diseño de longitud máxima y mínima. La verificación hidráulica de la grada se resume en la Tabla 5-1. -->

**Tabla 5-1: Verificación hidráulica de grada escalonada N°1****

| Col1 | Col2 | Col3 | Col4 | Col5 | Col6 | Parámetros | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GRADA** | **Km,-** | **Km,-** | **Largo** | **Cota** | **Cota** | **a ** | **K ** | **ho** | **Xo** | **h1/h0** | **h1** | **d/ho** | **d ** |
| **N°** | **Inicio** | **Fin** | **(metros)** | **(msnm)** | **(msnm)** | **(m)** | **(--)** | **(m)** | **(--)** | **(--)** | **(m)** | **(--)** | **(m)** |
|  | N/A | 1335,54 | N/A | N/A | 349,24 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **1 ** | 1335,54 | 1339,94 | 4,40 | 349,24 | 347,34 | 1,90 | 1,70 | 1,12 | 1,00 | 0,45 | 0,50 | 3,40 | 3,79 |
| **2 ** | 1339,94 | 1344,34 | 4,40 | 347,34 | 345,44 | 1,90 | 1,70 | 0,50 | 0,45 | 0,90 | 0,45 | 5,20 | 2,61 |
| **3 ** | 1344,34 | 1348,74 | 4,40 | 345,44 | 343,54 | 1,90 | 1,70 | 0,45 | 0,41 | 1,10 | 0,50 | 5,20 | 2,35 |
| **4 ** | 1348,74 | 1353,14 | 4,40 | 343,54 | 341,64 | 1,90 | 1,70 | 0,50 | 0,45 | 0,90 | 0,45 | 5,20 | 2,58 |
| **5 ** | 1353,14 | 1357,54 | 4,40 | 341,64 | 339,74 | 1,90 | 1,70 | 0,45 | 0,40 | 1,00 | 0,45 | 5,20 | 2,33 |
| **6 ** | 1357,54 | 1361,94 | 4,40 | 339,74 | 337,84 | 1,90 | 1,70 | 0,45 | 0,40 | 1,00 | 0,45 | 5,20 | 2,33 |
| **7 ** | 1361,94 | 1366,34 | 4,40 | 337,84 | 335,94 | 1,90 | 1,70 | 0,45 | 0,40 | 1,00 | 0,45 | 5,20 | 2,33 |
| **8 ** | 1366,34 | 1370,74 | 4,40 | 335,94 | 334,04 | 1,90 | 1,70 | 0,45 | 0,40 | 1,00 | 0,45 | 5,20 | 2,33 |
| **9 ** | 1370,74 | 1375,14 | 4,40 | 334,04 | 332,14 | 1,90 | 1,70 | 0,45 | 0,40 | 1,00 | 0,45 | 5,20 | 2,33 |
| **10** | 1375,14 | 1379,54 | 4,40 | 332,14 | 330,24 | 1,90 | 1,70 | 0,45 | 0,40 |  |  |  |  |

<!-- Estadísticas: 13 filas, 14 columnas -->
<!-- Contexto posterior: -->
<!-- Donde: L = Longitud de la grada (corresponde a la longitud máxima adoptada), en metros -->
<!-- FIN TABLA 5-1 -->


**Tabla 5-1 Verificación hidráulica de grada escalonada N°1**

|Col1|Col2|Col3|Col4|Col5|Col6|Parámetros|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**GRADA**|**Km,-**|**Km,-**|**Largo**|**Cota**|**Cota**|**a **|**K **|**ho**|**Xo**|**h1/h0**|**h1**|**d/ho**|**d **|
|**N°**|**Inicio**|**Fin**|**(metros)**|**(msnm)**|**(msnm)**|**(m)**|**(--)**|**(m)**|**(--)**|**(--)**|**(m)**|**(--)**|**(m)**|
||N/A|1335,54|N/A|N/A|349,24|N/A|N/A|N/A|N/A|N/A|N/A|N/A|N/A|
|**1 **|1335,54|1339,94|4,40|349,24|347,34|1,90|1,70|1,12|1,00|0,45|0,50|3,40|3,79|
|**2 **|1339,94|1344,34|4,40|347,34|345,44|1,90|1,70|0,50|0,45|0,90|0,45|5,20|2,61|
|**3 **|1344,34|1348,74|4,40|345,44|343,54|1,90|1,70|0,45|0,41|1,10|0,50|5,20|2,35|
|**4 **|1348,74|1353,14|4,40|343,54|341,64|1,90|1,70|0,50|0,45|0,90|0,45|5,20|2,58|
|**5 **|1353,14|1357,54|4,40|341,64|339,74|1,90|1,70|0,45|0,40|1,00|0,45|5,20|2,33|
|**6 **|1357,54|1361,94|4,40|339,74|337,84|1,90|1,70|0,45|0,40|1,00|0,45|5,20|2,33|
|**7 **|1361,94|1366,34|4,40|337,84|335,94|1,90|1,70|0,45|0,40|1,00|0,45|5,20|2,33|
|**8 **|1366,34|1370,74|4,40|335,94|334,04|1,90|1,70|0,45|0,40|1,00|0,45|5,20|2,33|
|**9 **|1370,74|1375,14|4,40|334,04|332,14|1,90|1,70|0,45|0,40|1,00|0,45|5,20|2,33|
|**10**|1375,14|1379,54|4,40|332,14|330,24|1,90|1,70|0,45|0,40|||||

Donde:

L = Longitud de la grada (corresponde a la longitud máxima adoptada), en metros

a = Altura de grada, en metros

K = Relación entre la altura de grada y la altura critica, aguas arriba de la grada (K=a/hc).

ho = Altura de escurrimiento inmediatamente aguas arriba de la grada, en metros.

Xo = Relación ho/hc, adimensional

h1/ho = Relación entra la altura de escurrimiento aguas debajo de la grada y la altura critica.

h1 = Altura de escurrimiento aguas abajo de la grada.

d/ho = Relación entre la longitud mínima de la grada y la altura aguas arriba de la grada.

d = Longitud mínima de la grada, para que el torrente sea contenido por la grada.

Los resultados de la Tabla 5-1 permite afirmar que la longitud adoptada para cada grada
resulta mayor a la grada mínima requerida de aplicar los criterios de Francisco Javier
Domínguez, por lo que, el torrente queda contenido dentro de la grada, lográndose el efecto
disipador buscado.

2410485-00-HID-INF-002 Rev_B

**5.3** **VERIFICACION DE LA OBRA DE DESCARGA - GRADA ESCALONADA N° 2**

Tomando en cuenta la envergadura del proyecto y la falta de espacio para proyectar un
disipador de energía tipo USBR, se considera la materialización de una grada escalonada
entre los kilómetros 1.629,04 y 1.671,34 (Figura 5-4) salvado una diferencia de cotas de 42,3
metros.

2410485-00-HID-INF-002 Rev_B

**Figura 5-4 Grada Escalonadas N°2**

2410485-00-HID-INF-002 Rev_B Página 48 de 50

Se ha estimado que un total de 9 gradas con altura de 1,7 metros cada una, permite cumplir
con los criterios de diseño de longitud máxima y mínima.

La verificación hidráulica de la grada se resume en la Tabla 5-2

**Tabla 5-2 Verificación hidráulica de grada escalonada N°2**

|Col1|Col2|Col3|Col4|Col5|Col6|Parámetros|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**GRADA**|**Km**|**Km**|**Largo**|**Cota**|**Cota**|**a **|**K **|**ho**|**Xo**|**h1/h0**|**h1**|**d/ho**|**d **|
|**N°**|**Inicio**|**Fin**|**(metros)**|**(msnm)**|**(msnm)**|**(m)**|**(--)**|**(m)**|**(--)**|**(--)**|**(m)**|**(--)**|**(m)**|
|||1629,04|N/A||294,76|||||||||
|**1 **|1629,04|1633,74|4,70|294,76|293,06|1,70|1,44|1,18|1,00|0,45|0,53|3,50|4,12|
|**2 **|1633,74|1638,44|4,70|293,06|291,36|1,70|1,44|0,53|0,45|0,90|0,48|4,75|2,52|
|**3 **|1638,44|1643,14|4,70|291,36|289,66|1,70|1,44|0,48|0,41|1,00|0,48|5,00|2,38|
|**4 **|1643,14|1647,84|4,70|289,66|287,96|1,70|1,44|0,48|0,41|1,00|0,48|5,00|2,38|
|**5 **|1647,84|1652,54|4,70|287,96|286,26|1,70|1,44|0,48|0,41|1,00|0,48|5,00|2,38|
|**6 **|1652,54|1657,24|4,70|286,26|284,56|1,70|1,44|0,48|0,41|1,00|0,48|5,00|2,38|
|**7 **|1657,24|1661,94|4,70|284,56|282,86|1,70|1,44|0,48|0,41|1,00|0,48|5,00|2,38|
|**8 **|1661,94|1666,64|4,70|282,86|281,16|1,70|1,44|0,48|0,41|1,00|0,48|5,00|2,38|
|**9 **|1666,64|1671,34|4,70|281,16|279,46|1,70|1,44|0,48|0,41|||||

Donde:

L = Longitud de la grada (corresponde a la longitud máxima adoptada), en metros

a = Altura de grada, en metros

K = Relación entre la altura de grada y la altura critica, aguas arriba de la grada (K=a/hc).

ho = Altura de escurrimiento inmediatamente aguas arriba de la grada, en metros.

Xo = Relación ho/hc, adimensional

h1/ho = Relación entra la altura de escurrimiento aguas debajo de la grada y la altura critica.

h1 = Altura de escurrimiento aguas abajo de la grada.

d/ho = Relación entre la longitud mínima de la grada y la altura aguas arriba de la grada.

d = Longitud mínima de la grada, para que el torrente sea contenido por la grada.

Los resultados de la Tabla 5-2 permite afirmar que la longitud adoptada para cada grada
resulta mayor a la grada mínima requerida de aplicar los criterios de Francisco Javier
Domínguez, por lo que, el torrente queda contenido dentro de la grada, lográndose el efecto
disipador buscado.

2410485-00-HID-INF-002 Rev_B Página 49 de 50

**6** **CONCLUSIONES**

El canal de contorno proyectado como parte del sistema de manejo de aguas no contactadas
permite interceptar todos los flujos superficiales producto de la escorrentía directa para un
periodo de retorno de 50 años, de acuerdo con lo indicado en el D.S. N°50 del MOP.

La sección proyectada, presenta, además, capacidad suficiente para contener el caudal
asociado al periodo de retorno de 100 años.

El terreno donde se proyecta la ejecución del canal de contorno ha sido clasificado
mayormente como maicillo (granito descompuesto), por lo que se ha considerado un
revestimiento en shotcrete con armadura mínima de retracción formada por malla tipo ACMA,
a fin de evitar la formación de cárcavas y arrastre de material.

La definición del trazado del canal de contorno proyectado genera la interferencia con dos
caminos de servicio existentes, por lo que se proyecta la ejecución de dos alcantarillas
formadas por ductos de HDPE estructurado (tipo ADS-12) con diámetro mínimo de 1,20

metros.

El material de relleno sobre la clave del ducto corresponderá a la definida por el fabricante,
con un espesor mínimo que permita asegurar el paso de camiones tipo ASSHTO HS-20-44
+20% con coeficiente de impacto incluido.

El perfil del trazado del canal de contorno proyectado ha identificado la necesidad de salvar
dos caídas de cota, las que se han solucionado mediante la proyección de dos gradas
escalonadas en hormigón armado con sección rectangular de ancho basal 1,20 metros y altura
libre de 1,20 metros.

2410485-00-HID-INF-002 Rev_B Página 50 de 50

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Distribución Espacial de Caudales, Caudales de Diseño.****

| Tramo Canal | Col2 | Caudal Aportado por Cuenca | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Caudal<br>Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Inicio** | **Termino** | **C-1** | **C-2** | **IC-1** | **C-3** | **IC-2** | **C-4** | **IC-3** | **C-5** | **C-6** | **C-6** |
| **0,00** | **235,30** | 0,98 |  |  |  |  |  |  |  |  | 0,98 |
| **251,30** | **251,30** | 0,98 | 0,67 |  |  |  |  |  |  |  | 1,65 |
| **251,30** | **453,30** | 0,98 | 0,67 | 0,05 |  |  |  |  |  |  | 1,71 |
| **453,30** | **691,30** | 0,98 | 0,67 | 0,05 | 0,77 |  |  |  |  |  | 2,48 |
| **691,30** | **691,30** | 0,98 | 0,67 | 0,05 | 0,77 | 0,05 |  |  |  |  | 2,53 |
| **691,30** | **915,30** | 0,98 | 0,67 | 0,05 | 0,77 | 0,05 | 0,69 |  |  |  | 3,22 |
| **915,30** | **915,30** | 0,98 | 0,67 | 0,05 | 0,77 | 0,05 | 0,69 | 0,06 |  |  | 3,28 |
| **915,30** | **1179,55** | 0,98 | 0,67 | 0,05 | 0,77 | 0,05 | 0,69 | 0,06 | 0,72 |  | 4,00 |
| **1179,55** | **2.115,30** | 0,98 | 0,67 | 0,05 | 0,77 | 0,05 | 0,69 | 0,06 | 0,72 | 0,13 | 4,14 |

**Tabla 3-2.: ** **Distribución Espacial de Caudales, Caudales de Verificación.****

| Tramo Canal | Col2 | Caudal Aportado por Cuenca | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Caudal<br>Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Inicio** | **Termino** | **C-1** | **C-2** | **IC-1** | **C-3** | **IC-2** | **C-4** | **IC-3** | **C-5** | **C-6** | **C-6** |
| **0,00** | **235,30** | 1,14 |  |  |  |  |  |  |  |  | 1,14 |
| **251,30** | **251,30** | 1,14 | 0,78 |  |  |  |  |  |  |  | 1,92 |
| **251,30** | **453,30** | 1,14 | 0,78 | 0,06 |  |  |  |  |  |  | 1,98 |
| **453,30** | **691,30** | 1,14 | 0,78 | 0,06 | 0,90 |  |  |  |  |  | 2,88 |
| **691,30** | **691,30** | 1,14 | 0,78 | 0,06 | 0,90 | 0,06 |  |  |  |  | 2,94 |
| **691,30** | **915,30** | 1,14 | 0,78 | 0,06 | 0,90 | 0,06 | 0,80 |  |  |  | 3,74 |
| **915,30** | **915,30** | 1,14 | 0,78 | 0,06 | 0,90 | 0,06 | 0,80 | 0,06 |  |  | 3,81 |
| **915,30** | **1179,55** | 1,14 | 0,78 | 0,06 | 0,90 | 0,06 | 0,80 | 0,06 | 0,84 |  | 4,65 |
| **1179,55** | **2.115,30** | 1,14 | 0,78 | 0,06 | 0,90 | 0,06 | 0,80 | 0,06 | 0,84 | 0,16 | 4,80 |

**Tabla 3-3.: ** **Valores límite del número de Froude****

| RÉGIMEN | FROUDE |
| --- | --- |
| **Subcrítico** | _FR_ < 1 |
| **Crítico** | _FR_ = 1 |
| **Supercrítico** | _FR_ > 1 |

**Tabla 4-1: Modelación Canal de Contorno - Tramo 1, Resultados T=100****

| Km | PT | Q | Z1 | Z2 | Z3 | Z4 | J | V | A | L | F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Km** | **PT** | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| **0.00 ** | 2115.30 | 1.14 | 376.65 | 377.05 | 377.05 | 377.21 | 0.0028 | 1.90 | 0.68 | 2.10 | 0.96 |
| **15.30 ** | 2100.00 | 1.14 | 376.42 | 376.68 | 376.82 | 377.11 | 0.0118 | 2.99 | 0.42 | 1.83 | 1.85 |
| **31.30 ** | 2084.00 | 1.14 | 376.13 | 376.38 | 376.53 | 376.88 | 0.0156 | 3.26 | 0.38 | 1.79 | 2.10 |
| **33.30 ** | 2082.00 | 1.14 | 376.08 | 376.48 | 376.48 | 376.65 | 0.0029 | 1.92 | 0.67 | 2.09 | 0.97 |
| **35.30 ** | 2080.00 | 1.14 | 376.04 | 376.44 | 376.44 | 376.60 | 0.0028 | 1.91 | 0.68 | 2.10 | 0.97 |
| **53.30 ** | 2062.00 | 1.14 | 375.62 | 375.85 | 376.02 | 376.45 | 0.0205 | 3.55 | 0.35 | 1.75 | 2.38 |
| **55.30 ** | 2060.00 | 1.14 | 375.58 | 375.80 | 375.98 | 376.41 | 0.0207 | 3.56 | 0.35 | 1.75 | 2.39 |
| **57.30 ** | 2058.00 | 1.14 | 375.53 | 375.76 | 375.93 | 376.37 | 0.0209 | 3.57 | 0.34 | 1.75 | 2.40 |
| **67.30 ** | 2048.00 | 1.14 | 375.30 | 375.53 | 375.70 | 376.15 | 0.0219 | 3.62 | 0.34 | 1.75 | 2.45 |
| **69.30 ** | 2046.00 | 1.14 | 375.26 | 375.48 | 375.65 | 376.11 | 0.0220 | 3.63 | 0.34 | 1.75 | 2.45 |
| **75.30 ** | 2040.00 | 1.14 | 375.12 | 375.34 | 375.52 | 375.98 | 0.0222 | 3.64 | 0.34 | 1.74 | 2.47 |
| **95.30 ** | 2020.00 | 1.14 | 374.66 | 374.88 | 375.06 | 375.52 | 0.0227 | 3.67 | 0.34 | 1.74 | 2.49 |
| **111.30 ** | 2004.00 | 1.14 | 374.28 | 374.50 | 374.68 | 375.15 | 0.0232 | 3.69 | 0.33 | 1.74 | 2.51 |
| **113.30 ** | 2002.00 | 1.14 | 374.22 | 374.44 | 374.62 | 375.10 | 0.0237 | 3.71 | 0.33 | 1.74 | 2.54 |
| **115.30 ** | 2000.00 | 1.14 | 374.16 | 374.56 | 374.56 | 374.73 | 0.0029 | 1.92 | 0.67 | 2.09 | 0.97 |
| **117.30 ** | 1998.00 | 1.14 | 374.11 | 374.50 | 374.50 | 374.67 | 0.0028 | 1.91 | 0.67 | 2.10 | 0.97 |
| **119.30 ** | 1996.00 | 1.14 | 374.05 | 374.44 | 374.44 | 374.61 | 0.0028 | 1.91 | 0.68 | 2.10 | 0.97 |
| **121.30 ** | 1994.00 | 1.14 | 373.99 | 374.30 | 374.39 | 374.59 | 0.0064 | 2.47 | 0.51 | 1.93 | 1.40 |
| **123.30 ** | 1992.00 | 1.14 | 373.93 | 374.22 | 374.33 | 374.57 | 0.0087 | 2.72 | 0.46 | 1.88 | 1.62 |
| **125.30 ** | 1990.00 | 1.14 | 373.87 | 374.14 | 374.27 | 374.54 | 0.0108 | 2.91 | 0.43 | 1.85 | 1.78 |
| **127.30 ** | 1988.00 | 1.14 | 373.81 | 374.07 | 374.21 | 374.52 | 0.0127 | 3.06 | 0.41 | 1.82 | 1.91 |
| **129.30 ** | 1986.00 | 1.14 | 373.75 | 374.00 | 374.15 | 374.49 | 0.0143 | 3.18 | 0.39 | 1.80 | 2.02 |
| **135.30 ** | 1980.00 | 1.14 | 373.58 | 373.81 | 373.98 | 374.38 | 0.0188 | 3.46 | 0.36 | 1.77 | 2.29 |
| **155.30 ** | 1960.00 | 1.14 | 372.99 | 373.39 | 373.39 | 373.55 | 0.0028 | 1.91 | 0.68 | 2.10 | 0.96 |
| **165.30 ** | 1950.00 | 1.14 | 372.70 | 372.94 | 373.09 | 373.46 | 0.0165 | 3.32 | 0.37 | 1.78 | 2.15 |
| **167.30 ** | 1948.00 | 1.14 | 372.64 | 372.87 | 373.03 | 373.43 | 0.0178 | 3.40 | 0.36 | 1.77 | 2.23 |
| **175.30 ** | 1940.00 | 1.14 | 372.40 | 372.62 | 372.80 | 373.26 | 0.0223 | 3.64 | 0.34 | 1.74 | 2.47 |
| **195.30 ** | 1920.00 | 1.14 | 371.85 | 372.06 | 372.25 | 372.77 | 0.0263 | 3.84 | 0.32 | 1.72 | 2.66 |
| **203.30 ** | 1912.00 | 1.14 | 371.67 | 371.89 | 372.07 | 372.56 | 0.0240 | 3.73 | 0.33 | 1.73 | 2.55 |
| **205.30 ** | 1910.00 | 1.14 | 371.63 | 371.84 | 372.02 | 372.51 | 0.0237 | 3.71 | 0.33 | 1.74 | 2.54 |
| **209.67 ** | 1905.63 | 1.14 | 371.53 | 371.75 | 371.93 | 372.40 | 0.0230 | 3.68 | 0.33 | 1.74 | 2.51 |
| **215.30 ** | 1900.00 | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m | Alcantarilla HDPE ADS-12 DN1200 mm L=21.33 m |
| **230.00 ** | 1885.30 | 1.14 | 371.07 | 371.45 | 371.47 | 371.64 | 0.0033 | 2.02 | 0.64 | 2.06 | 1.05 |
| **235.30 ** | 1880.00 | 1.14 | 370.52 | 370.72 | 370.92 | 371.53 | 0.0331 | 4.12 | 0.30 | 1.70 | 2.95 |

**Tabla 4-2: Modelación Canal de Contorno - Tramo 2, Resultados T=100****

| Km | PT | Q | Z1 | Z2 | Z3 | Z4 | J | V | A | L | F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Km** | **PT** | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** | **Fin Grada Escalonada N°1** |
| **1179.55 ** | 935.75 | 4.80 | 330.34 | 331.46 | 331.46 | 332.01 | 0.0021 | 3.28 | 1.48 | 1.66 | 0.99 |
| **1181.30 ** | 934.00 | 4.80 | 330.31 | 331.39 | 331.47 | 332.00 | 0.0055 | 3.47 | 1.41 | 1.32 | 1.07 |
| **1183.30 ** | 932.00 | 4.80 | 330.28 | 331.27 | 331.40 | 331.98 | 0.0052 | 3.73 | 1.30 | 1.32 | 1.20 |
| **1185.30 ** | 930.00 | 4.80 | 330.24 | 331.23 | 331.42 | 331.96 | 0.0070 | 3.79 | 1.29 | 1.31 | 1.22 |
| **1187.41 ** | 927.89 | 4.80 | 330.21 | 331.14 | 331.59 | 331.94 | 0.0039 | 3.97 | 1.22 | 1.32 | 1.31 |
| **1191.41 ** | 923.89 | 4.80 | 330.15 | 330.73 | 331.08 | 331.88 | 0.0119 | 5.11 | 1.11 | 2.48 | 2.13 |
| **1195.30 ** | 920.00 | 4.80 | 330.08 | 330.67 | 331.02 | 331.83 | 0.0122 | 5.15 | 1.10 | 2.47 | 2.15 |
| **1203.30 ** | 912.00 | 4.80 | 329.95 | 330.53 | 330.89 | 331.73 | 0.0127 | 5.22 | 1.09 | 2.46 | 2.19 |
| **1205.30 ** | 910.00 | 4.80 | 329.92 | 330.50 | 330.86 | 331.70 | 0.0129 | 5.23 | 1.08 | 2.45 | 2.20 |
| **1207.30 ** | 908.00 | 4.80 | 329.89 | 330.46 | 330.82 | 331.68 | 0.0130 | 5.25 | 1.08 | 2.45 | 2.21 |
| **1209.30 ** | 906.00 | 4.80 | 329.86 | 330.43 | 330.78 | 331.65 | 0.0131 | 5.26 | 1.08 | 2.45 | 2.22 |
| **1211.30 ** | 904.00 | 4.80 | 329.82 | 330.40 | 330.76 | 331.62 | 0.0132 | 5.28 | 1.07 | 2.45 | 2.22 |
| **1215.30 ** | 900.00 | 4.80 | 329.76 | 330.33 | 330.69 | 331.57 | 0.0133 | 5.30 | 1.07 | 2.44 | 2.24 |
| **1225.30 ** | 890.00 | 4.80 | 329.60 | 330.16 | 330.53 | 331.43 | 0.0137 | 5.35 | 1.06 | 2.43 | 2.27 |
| **1227.30 ** | 888.00 | 4.80 | 329.56 | 330.13 | 330.50 | 331.40 | 0.0139 | 5.36 | 1.05 | 2.43 | 2.28 |
| **1229.30 ** | 886.00 | 4.80 | 329.53 | 330.10 | 330.47 | 331.37 | 0.0139 | 5.37 | 1.05 | 2.43 | 2.28 |
| **1231.30 ** | 884.00 | 4.80 | 329.50 | 330.06 | 330.43 | 331.34 | 0.0140 | 5.38 | 1.05 | 2.43 | 2.29 |
| **1235.30 ** | 880.00 | 4.80 | 329.43 | 330.00 | 330.37 | 331.28 | 0.0141 | 5.40 | 1.05 | 2.42 | 2.30 |
| **1245.30 ** | 870.00 | 4.80 | 329.27 | 329.83 | 330.21 | 331.14 | 0.0145 | 5.44 | 1.04 | 2.42 | 2.32 |
| **1255.30 ** | 860.00 | 4.80 | 329.11 | 329.67 | 330.05 | 330.99 | 0.0147 | 5.47 | 1.03 | 2.41 | 2.34 |
| **1263.30 ** | 852.00 | 4.80 | 328.98 | 329.53 | 329.92 | 330.87 | 0.0150 | 5.50 | 1.03 | 2.41 | 2.36 |
| **1265.30 ** | 850.00 | 4.80 | 328.95 | 329.50 | 329.88 | 330.84 | 0.0150 | 5.50 | 1.03 | 2.41 | 2.36 |
| **1267.30 ** | 848.00 | 4.80 | 328.91 | 329.47 | 329.85 | 330.81 | 0.0151 | 5.51 | 1.02 | 2.40 | 2.36 |
| **1269.30 ** | 846.00 | 4.80 | 328.88 | 329.43 | 329.82 | 330.78 | 0.0152 | 5.52 | 1.02 | 2.40 | 2.37 |
| **1275.30 ** | 840.00 | 4.80 | 328.79 | 329.34 | 329.72 | 330.69 | 0.0152 | 5.53 | 1.02 | 2.40 | 2.38 |
| **1283.30 ** | 832.00 | 4.80 | 328.66 | 329.21 | 329.59 | 330.57 | 0.0154 | 5.54 | 1.02 | 2.40 | 2.38 |
| **1285.30 ** | 830.00 | 4.80 | 328.62 | 329.17 | 329.56 | 330.54 | 0.0154 | 5.55 | 1.02 | 2.40 | 2.39 |
| **1287.30 ** | 828.00 | 4.80 | 328.59 | 329.14 | 329.53 | 330.51 | 0.0155 | 5.56 | 1.01 | 2.40 | 2.39 |
| **1295.30 ** | 820.00 | 4.80 | 328.46 | 329.01 | 329.40 | 330.38 | 0.0156 | 5.57 | 1.01 | 2.40 | 2.40 |
| **1299.30 ** | 816.00 | 4.80 | 328.40 | 328.94 | 329.33 | 330.32 | 0.0157 | 5.57 | 1.01 | 2.39 | 2.41 |
| **1301.30 ** | 814.00 | 4.80 | 328.36 | 328.91 | 329.29 | 330.29 | 0.0157 | 5.58 | 1.01 | 2.39 | 2.41 |
| **1303.30 ** | 812.00 | 4.80 | 328.33 | 328.88 | 329.27 | 330.26 | 0.0157 | 5.58 | 1.01 | 2.39 | 2.41 |

**Tabla 4-3: Modelación Canal de Contorno - Tramo 3, Resultados T=100****

| Km | PT | Q | Z1 | Z2 | Z3 | Z4 | J | V | A | L | F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Km** | **PT** | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** | **Inicio Grada Escalonada N°2** |
| **1690.53 ** | 424.77 | 4.80 | 276.49 | 277.60 | 277.60 | 278.16 | 0.0081 | 3.32 | 1.45 | 1.30 | 1.00 |
| **1691.30 ** | 424.00 | 4.80 | 276.45 | 277.45 | 277.57 | 278.14 | 0.0106 | 3.69 | 1.30 | 1.30 | 1.18 |
| **1693.30 ** | 422.00 | 4.80 | 276.35 | 277.25 | 277.46 | 278.10 | 0.0137 | 4.08 | 1.18 | 1.30 | 1.37 |
| **1695.30 ** | 420.00 | 4.80 | 276.25 | 277.10 | 277.37 | 278.06 | 0.0161 | 4.35 | 1.10 | 1.30 | 1.51 |
| **1697.30 ** | 418.00 | 4.80 | 276.15 | 276.96 | 277.25 | 278.02 | 0.0182 | 4.55 | 1.05 | 1.30 | 1.61 |
| **1698.55 ** | 416.75 | 4.80 | 276.09 | 276.88 | 277.34 | 277.99 | 0.0192 | 4.66 | 1.03 | 1.30 | 1.67 |
| **1702.55 ** | 412.75 | 4.80 | 275.88 | 276.28 | 276.68 | 277.85 | 0.0272 | 5.98 | 0.90 | 2.52 | 3.01 |
| **1709.63 ** | 405.67 | 4.80 | 275.53 | 276.04 | 276.47 | 277.68 | 0.0202 | 6.05 | 0.92 | 2.32 | 2.70 |
| **1715.30 ** | 400.00 | 4.80 | 275.24 | 275.73 | 276.17 | 277.54 | 0.0234 | 6.34 | 0.88 | 2.28 | 2.89 |
| **1735.30 ** | 380.00 | 4.80 | 274.23 | 274.67 | 275.16 | 276.94 | 0.0329 | 7.06 | 0.78 | 2.19 | 3.38 |
| **1739.30 ** | 376.00 | 4.80 | 274.02 | 274.46 | 274.95 | 276.79 | 0.0344 | 7.16 | 0.77 | 2.18 | 3.44 |
| **1741.30 ** | 374.00 | 4.80 | 273.92 | 274.36 | 274.85 | 276.72 | 0.0351 | 7.21 | 0.76 | 2.18 | 3.47 |
| **1743.30 ** | 372.00 | 4.80 | 273.82 | 274.26 | 274.76 | 276.65 | 0.0358 | 7.25 | 0.76 | 2.17 | 3.50 |
| **1745.30 ** | 370.00 | 4.80 | 273.72 | 274.15 | 274.66 | 276.57 | 0.0364 | 7.29 | 0.75 | 2.17 | 3.53 |
| **1747.30 ** | 368.00 | 4.80 | 273.62 | 274.05 | 274.55 | 276.50 | 0.0371 | 7.33 | 0.75 | 2.16 | 3.56 |
| **1749.30 ** | 366.00 | 4.80 | 273.52 | 273.95 | 274.45 | 276.42 | 0.0377 | 7.37 | 0.74 | 2.16 | 3.59 |
| **1751.30 ** | 364.00 | 4.80 | 273.42 | 273.84 | 274.35 | 276.34 | 0.0382 | 7.40 | 0.74 | 2.16 | 3.61 |
| **1753.30 ** | 362.00 | 4.80 | 273.32 | 273.74 | 274.25 | 276.26 | 0.0387 | 7.44 | 0.74 | 2.15 | 3.63 |
| **1755.30 ** | 360.00 | 4.80 | 273.21 | 273.64 | 274.15 | 276.18 | 0.0393 | 7.47 | 0.73 | 2.15 | 3.66 |
| **1757.30 ** | 358.00 | 4.80 | 273.11 | 273.54 | 274.05 | 276.10 | 0.0399 | 7.50 | 0.73 | 2.15 | 3.68 |
| **1759.30 ** | 356.00 | 4.80 | 273.01 | 273.43 | 273.95 | 276.02 | 0.0404 | 7.53 | 0.73 | 2.14 | 3.70 |
| **1761.30 ** | 354.00 | 4.80 | 272.91 | 273.33 | 273.85 | 275.94 | 0.0408 | 7.56 | 0.72 | 2.14 | 3.72 |
| **1763.30 ** | 352.00 | 4.80 | 272.81 | 273.23 | 273.74 | 275.85 | 0.0413 | 7.58 | 0.72 | 2.14 | 3.74 |
| **1765.30 ** | 350.00 | 4.80 | 272.71 | 273.13 | 273.64 | 275.77 | 0.0417 | 7.61 | 0.72 | 2.14 | 3.76 |
| **1767.30 ** | 348.00 | 4.80 | 272.61 | 273.02 | 273.54 | 275.68 | 0.0421 | 7.63 | 0.72 | 2.13 | 3.77 |
| **1769.30** | 346.00 | 4.80 | 272.50 | 272.92 | 273.44 | 275.60 | 0.0425 | 7.65 | 0.71 | 2.13 | 3.79 |
| **1771.30** | 344.00 | 4.80 | 272.40 | 272.82 | 273.34 | 275.51 | 0.0428 | 7.67 | 0.71 | 2.13 | 3.80 |
| **1773.30** | 342.00 | 4.80 | 272.30 | 272.72 | 273.24 | 275.42 | 0.0432 | 7.69 | 0.71 | 2.13 | 3.82 |
| **1775.30** | 340.00 | 4.80 | 272.20 | 272.61 | 273.13 | 275.33 | 0.0435 | 7.71 | 0.71 | 2.13 | 3.83 |
| **1777.30** | 338.00 | 4.80 | 272.10 | 272.51 | 273.04 | 275.24 | 0.0438 | 7.73 | 0.71 | 2.12 | 3.84 |
| **1779.30** | 336.00 | 4.80 | 272.00 | 272.41 | 272.93 | 275.15 | 0.0441 | 7.74 | 0.70 | 2.12 | 3.85 |
| **1781.30** | 334.00 | 4.80 | 271.90 | 272.31 | 272.83 | 275.06 | 0.0443 | 7.76 | 0.70 | 2.12 | 3.86 |

**Tabla 5-2: Verificación hidráulica de grada escalonada N°2****

| Col1 | Col2 | Col3 | Col4 | Col5 | Col6 | Parámetros | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GRADA** | **Km** | **Km** | **Largo** | **Cota** | **Cota** | **a ** | **K ** | **ho** | **Xo** | **h1/h0** | **h1** | **d/ho** | **d ** |
| **N°** | **Inicio** | **Fin** | **(metros)** | **(msnm)** | **(msnm)** | **(m)** | **(--)** | **(m)** | **(--)** | **(--)** | **(m)** | **(--)** | **(m)** |
|  |  | 1629,04 | N/A |  | 294,76 |  |  |  |  |  |  |  |  |
| **1 ** | 1629,04 | 1633,74 | 4,70 | 294,76 | 293,06 | 1,70 | 1,44 | 1,18 | 1,00 | 0,45 | 0,53 | 3,50 | 4,12 |
| **2 ** | 1633,74 | 1638,44 | 4,70 | 293,06 | 291,36 | 1,70 | 1,44 | 0,53 | 0,45 | 0,90 | 0,48 | 4,75 | 2,52 |
| **3 ** | 1638,44 | 1643,14 | 4,70 | 291,36 | 289,66 | 1,70 | 1,44 | 0,48 | 0,41 | 1,00 | 0,48 | 5,00 | 2,38 |
| **4 ** | 1643,14 | 1647,84 | 4,70 | 289,66 | 287,96 | 1,70 | 1,44 | 0,48 | 0,41 | 1,00 | 0,48 | 5,00 | 2,38 |
| **5 ** | 1647,84 | 1652,54 | 4,70 | 287,96 | 286,26 | 1,70 | 1,44 | 0,48 | 0,41 | 1,00 | 0,48 | 5,00 | 2,38 |
| **6 ** | 1652,54 | 1657,24 | 4,70 | 286,26 | 284,56 | 1,70 | 1,44 | 0,48 | 0,41 | 1,00 | 0,48 | 5,00 | 2,38 |
| **7 ** | 1657,24 | 1661,94 | 4,70 | 284,56 | 282,86 | 1,70 | 1,44 | 0,48 | 0,41 | 1,00 | 0,48 | 5,00 | 2,38 |
| **8 ** | 1661,94 | 1666,64 | 4,70 | 282,86 | 281,16 | 1,70 | 1,44 | 0,48 | 0,41 | 1,00 | 0,48 | 5,00 | 2,38 |
| **9 ** | 1666,64 | 1671,34 | 4,70 | 281,16 | 279,46 | 1,70 | 1,44 | 0,48 | 0,41 |  |  |  |  |
