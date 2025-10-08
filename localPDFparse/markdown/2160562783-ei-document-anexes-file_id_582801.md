---
title: Sin título
author: Users-Pre-Installed
date: D:20231116025200-03'00'
language: es
type: report
pages: 50
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME
-->

# INFORME

## Evaluación de la Dispersión de Emisiones de Olor de Planta COMFRUT.

### COMFRUT CHILE SPA.

Curicó.

**16 de noviembre del 2023**

**Inf01E01.O-22-056.**

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx
1 de 50

#### Datos del Proyecto

**Empresa** : COMFRUT S.A.

**Planta** : Comercial Frutícola Curicó.

**Coordinador** : María Soledad Roa.

**Gerente de Ing. en olores** : Miguel Gatica Rivera (MGR).

**Jefe de Proyectos** : Felipe Sánchez Mella (FSM).

**Ingenieros de Proyecto** : Diana Moraga Arriagada (DMA).

**Fecha** : 16 de noviembre de 2023.

|Emisión|Datos|Preparó|Revisó|Aprobó|
|---|---|---|---|---|
|Rev A. Para<br>Revisión<br>cliente.|Nombre|DMA|FSM|FSM|
|Rev A. Para<br>Revisión<br>cliente.|Fecha|14-11-2023|15-11-2023|16-11-2023|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 2 de 50

**Índice General**

**1** **Resumen ............................................................................................................................ 6**

**2** **Introducción ..................................................................................................................... 10**

**3** **Objetivos General ............................................................................................................ 11**

Objetivos específicos .................................................................................................. 11
**4** **Metodología ..................................................................................................................... 11**

Caracterización de las fuentes .................................................................................... 11

Estimación de emisiones ............................................................................................ 12

Evaluación de la dispersión de las emisiones de olor ................................................. 12

4.3.1 Selección del Modelo ..................................................................................................... 12

4.3.2 Recopilación de Antecedentes Para la Modelación ....................................................... 13

4.3.3 Variables meteorológicas y geofísicas ........................................................................... 13

4.3.4 Evaluación de los resultados .......................................................................................... 15

4.3.5 Área de Influencia y receptores de interés. .................................................................... 16

Evaluación del desempeño del archivo de pronóstico utilizado ................................... 16

**5** **Resultados ....................................................................................................................... 17**

Caracterización de las fuentes de emisión .................................................................. 17

Régimen de emisión ................................................................................................... 18
Ubicación de fuentes .................................................................................................. 18

Factores de emisión utilizados .................................................................................... 20

Emisiones de olores ................................................................................................... 22

Evaluación de la dispersión de olores ......................................................................... 23

5.6.1 Dispersión de emisiones de olor. Escenario Actual. ...................................................... 23

5.6.2 Punto Máxima concentración de olor. Escenario Actual. ............................................... 24

5.6.3 Área de Influencia. Escenario Actual. ............................................................................ 25

5.6.4 Receptores discretos considerados en la modelación ................................................... 26

5.6.1 Concentración en Receptores. Escenario Actual. .......................................................... 27

5.6.2 Protocolo FIDOL. Escenario Actual. ............................................................................... 28

5.6.3 Dispersión de emisiones de olor. Escenario Futuro. ...................................................... 29

5.6.4 Punto Máxima concentración de olor. Escenario Futuro. .............................................. 29

5.6.5 Área de Influencia. Escenario Futuro. ............................................................................ 30

5.6.1 Concentración en Receptores. Escenario Futuro. ......................................................... 31

5.6.2 Protocolo FIDOL. Escenario Futuro. .............................................................................. 32

Análisis del desempeño del archivo de pronóstico utilizado ........................................ 33
**6** **Conclusiones ................................................................................................................... 34**

**7** **Anexos ............................................................................................................................. 35**

Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación ............ 35
Anexo No2. Análisis de receptores .............................................................................. 36

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 3 de 50

Anexo No3. Descripción meteorológica y geofísica de la zona .................................... 37

7.3.1 Cantidad de datos .......................................................................................................... 37

7.3.2 Gráficos Ciclo diario ....................................................................................................... 39

7.3.3 Gráfico Distribución de Viento ........................................................................................ 40

7.3.4 Rosa de los vientos ........................................................................................................ 41

7.3.5 Gráfico ciclo estacional .................................................................................................. 43

7.3.6 Elevación de Terreno ..................................................................................................... 44

Anexo No4. Análisis incertidumbre .............................................................................. 45

7.4.1 Ciclos Diarios promedios ................................................................................................ 46

7.4.2 Promedio Mensual.......................................................................................................... 48

7.4.3 Dirección de viento ......................................................................................................... 49

**Índice de Tabla**

**Tabla No 1.** Factores de emisión base para estudio en cuestión. ................................................................ 6
**Tabla No 2.** Factores de emisión asociados a las fuentes evaluadas en el presente estudio. .................... 6
**Tabla No 3** . Emisión asociada a cada fuente. ............................................................................................... 7
**Tabla No 4** . Concentración receptores. Percentil 98. ................................................................................... 9
**Tabla No 5.** Variables de entrada consideradas en la modelación ............................................................. 13
**Tabla No 6.** Características del archivo meteorológico WRF. .................................................................... 14
**Tabla No 7** . Límites de inmisión según la resolución vigente No1.541 del Ministerio de Ambiente y
Desarrollo Sostenible de Colombia, para el percentil 98. ........................................................................... 15
**Tabla No 7** . Descripción fuentes y procesos asociados. ............................................................................ 17
**Tabla No 8** . Régimen de emisión de fuentes. ............................................................................................. 18
**Tabla No 9.** Coordenadas de fuentes de emisión odorantes. Escenario Actual. ....................................... 18

**Tabla No 10.** Coordenadas de fuentes de emisión odorantes. Escenario Futuro. ..................................... 19
**Tabla No 11.** Factores de emisión base para estudio en cuestión. ............................................................ 20
**Tabla No 12.** Factores de emisión asociados a las fuentes evaluadas en el presente estudio. ................ 21
**Tabla No 13** . Factores de emisión y emisión asociada a cada fuente. ....................................................... 22
**Tabla No 14.** Punto máximo concentración para percentil 98. Coordenadas UTM 19S. Escenario Actual.
.................................................................................................................................................................... 24
**Tabla No 15** . Receptores discretos considerados en la modelación. ......................................................... 26
**Tabla No 16** . Concentración receptores, percentil 98. Escenario Actual. .................................................. 27
**Tabla No 17** . Protocolo FIDOL. Escenario Actual. ...................................................................................... 28
**Tabla No 18.** Punto máxima concentración para percentil 98. Coordenadas UTM 19S. Escenario Futuro.
.................................................................................................................................................................... 29
**Tabla No 19** . Concentración receptores, percentil 98. Escenario Futuro. .................................................. 31
**Tabla No 20** . Protocolo FIDOL. Escenario Futuro. ..................................................................................... 32
**Tabla No 21.** Datos estaciones meteorológicas consideradas. .................................................................. 37
**Tabla No 22.** Datos válidos estación meteorológica Curicó. ...................................................................... 38
**Tabla No 23.** Análisis cuantitativo. .............................................................................................................. 50

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 4 de 50

**Índice de Figura**

**Figura No 1** . Mapa de concentración de olor. Escenario Actual (Percentil 98). ........................................... 8
**Figura No 2** . Mapa de concentración de olor. Escenario Futuro (Percentil 98). .......................................... 8
**Figura No 3** . Mapa ubicación del proyecto evaluado.................................................................................. 10
**Figura No 4** . Esquema resumen de las metodologías para estimar las emisiones de olor. ...................... 12
**Figura No 5** . Ubicación espacial de las fuentes. Escenario Actual. ........................................................... 19
**Figura No 6** . Ubicación espacial de las fuentes. Escenario Futuro. ........................................................... 20
**Figura No 7** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio horario,
percentil 98. Escenario Actual..................................................................................................................... 24
**Figura No 8.** Mapa del Área de Influencia (AI), definida por 1 OU E /m [3] . Escenario Actual. ........................ 25
**Figura No 9** . Receptores discretos considerados en la modelación. ......................................................... 26
**Figura No 10** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio horario,
percentil 98. Escenario Futuro. ................................................................................................................... 29
**Figura No 11.** Mapa del Área de Influencia (AI), definida por 1 OU E /m [3] . Escenario Futuro. ..................... 30
**Figura No 12** . Estación Meteorológica utilizada en el Análisis de Incertidumbre. ...................................... 33
**Figura No 13** . Esquema funcionamiento CALPUFF. .................................................................................. 35
**Figura No 14** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No12. ........................ 36
**Figura No 15** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No12. ........................ 36
**Figura No 16.** Serie de tiempo velocidad de viento - datos observados estación Curicó- año 2021. ...... 37
**Figura No 17.** Serie de tiempo dirección de viento - datos observados estación Curicó - año 2021. ...... 38
**Figura No 18.** Serie de tiempo temperatura - datos observados estación Curicó - año 2021. ................. 38
**Figura No 19.** Ciclo diario para velocidad de viento Estación Curicó. ........................................................ 39
**Figura No 20.** Ciclo diario para temperatura estación Curicó. .................................................................... 39
**Figura No 21.** Ciclo diario para dirección de viento estación Curicó. ......................................................... 40
**Figura No 22.** Distribución velocidades de viento estación Curicó. ............................................................ 40
**Figura No 23.** Rosa de los vientos Anual. Datos observados Estación Curicó. ......................................... 41
**Figura No 24.** Rosa de los vientos por estación del año. ........................................................................... 42
**Figura No 25.** Ciclos estacionales - datos observados estación Curicó - Año 2021. ............................... 43
**Figura No 26.** Elevación de terreno archivo WRF. ..................................................................................... 44
**Figura No 27.** Comparación ciclo diario de velocidad de viento entre datos observados y proyectados
para la estación de Curicó. ......................................................................................................................... 46
**Figura No 28.** Comparación ciclo diario de dirección de viento entre datos observados y proyectados
para la estación de Curicó. ......................................................................................................................... 46
**Figura No 29.** Comparación ciclo diario de dirección de viento entre datos observados y proyectados
para la estación de Curicó. ......................................................................................................................... 47
**Figura No 30.** Comparación moda mensual de velocidad de viento entre datos observados y proyectados
para la estación de Curicó. ......................................................................................................................... 48
**Figura No 31.** Comparación moda mensual de dirección de viento entre datos observados y proyectados
para la estación de Curicó. ......................................................................................................................... 48
**Figura No 32.** Comparación moda mensual de dirección de viento entre datos observados y proyectados
para la estación de Curicó. ......................................................................................................................... 49
**Figura No 33.** Comparación Rosas de viento. ............................................................................................ 49

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 5 de 50

**1** **Resumen**

Comercial Frutícola, COMFRUT S.A., solicitó los servicios de Proterm S.A. con el objetivo de
evaluar la condición actual y futura de planta en cuanto al comportamiento de la dispersión de
olores de las principales fuentes con potencial de emisión. Tales fuentes consideradas
corresponden a 12, relacionadas con el sistema de tratamiento de RILes de planta.

El objetivo del presente informe es evaluar el comportamiento y efecto de las emisiones de olor
del proyecto sobre la salud de la población cercana, sistema de vida y costumbres, población
protegida, y turismo. Lo anterior acorde al artículo 11 de la Ley N°19.300 y la Guía para la
predicción y evaluación de impactos por olor en el SEIA.

Con respecto a la metodología, se decide utilizar factores de emisión de referencia de un proyecto
aprobado, con características similares al proyecto en cuestión, con el objetivo de evaluar un
escenario representativo en base a factores de emisión. A continuación, una tabla resumen de
factores de emisión utilizados para las fuentes del proyecto en cuestión. Dichos factores
provienen del proyecto aprobado “Regularización Proyecto Planta RILes FRUSUR San Carlos”.

**Tabla No 1.** Factores de emisión base para estudio en cuestión.

|Fuente Evaluada|Factor de Emisión<br>(OU /m2s)<br>E|Origen Factor de<br>emisión|
|---|---|---|
|**Contenedor de residuos**|0,0605|DIA Regularización<br>Proyecto Planta de RILes<br>FRUSUR San Carlos|
|**Sedimentador PTR**|0,0447|0,0447|
|**Reactor PTR**|0,0447|0,0447|
|**Reactor PTAS**|0,0449|0,0449|

Por otro lado, en la siguiente tabla, se presenta el detalle de las fuentes a evaluar, con su
respectivo factor de emisión, asociado a la fuente de referencia del cual se homologa el valor.

**Tabla No 2.** Factores de emisión asociados a las fuentes evaluadas en el presente estudio.

|Nro.|Fuente Evaluada|Factor de Emisión<br>(OU /m2s)<br>E|Fuente Referencial de<br>homologación|
|---|---|---|---|
|**1 **|**Cámara de recolección RIL**|0,0605|Reactor PTAS|
|**2 **|**Pretratamiento**|0,0447|Sedimentador PTR|
|**3 **|**Canal de sedimentación**|0,0447|Sedimentador PTR|
|**4 **|**Estanque aireado**|0,0449|Reactor PTR|
|**5 **|**Filtro lamelar**|0,0449|Reactor PTR|
|**6 **|**Cámara de lodos**|3,07|Contenedor de residuos|
|**7 **|**Estanques de paso**|0,0447|Sedimentador PTR|
|**8 **|**Cámara de contacto**|0,0447|Sedimentador PTR|
|**9 **|**Estanque acumulación RIL tratado**|0,0447|Sedimentador PTR|
|**10**|**Tranque de acumulación**|0,0447|Sedimentador PTR|
|**11**|**Área de riego**|0,0447|Sedimentador PTR|
|**12**|**Contenedor de residuos**|3,07|Contenedor de residuos|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 6 de 50

De acuerdo con la aplicación de los factores de emisión, proveniente del proyecto aprobado
ingresado al SEA “Regularización Proyecto Planta de RILes FRUSUR San Carlos”, se obtuvo
que la mayor fuente de emisión de olor corresponde al Área de Riego con 232 OU E /s en el
Escenario Actual y 219 OU E /s en el Escenario Futuro. A continuación, el detalle de emisiones
para cada fuente evaluada en ambos escenarios.

**Tabla No 3** . Emisión asociada a cada fuente.

|Nro.|Fuente Evaluada|Emisión (OU /s)<br>E|Col4|
|---|---|---|---|
|**Nro.**|**Fuente Evaluada**|**Escenario Actual**|**Escenario Futuro**|
|**1 **|**Cámara de recolección RIL**|0,14|0,14|
|**2 **|**Pretratamiento**|0,05|0,05|
|**3 **|**Canal de sedimentación**|0,61|0,61|
|**4 **|**Estanque aireado**|1,18|1,18|
|**5 **|**Filtro lamelar**|**0,18**|**0,36**|
|**6 **|**Cámara de lodos**|**8,84**|**17,68**|
|**7 **|**Estanques de paso**|0,12|0,12|
|**8 **|**Cámara de contacto**|0,45|0,45|
|**9 **|**Estanque acumulación RIL tratado**|0,24|0,24|
|**10**|**Tranque de acumulación**|**13,41**|**26,82**|
|**11**|**Área de riego**|**232**|**219**|
|**12**|**Contenedor de residuos**|76,76|76,76|

Una vez obtenidas las emisiones de olor de cada fuente, se ingresaron al modelo de dispersión
atmosférica calpuff, el cual permitió conocer la concentración y dispersión de los olores, tanto en
el área de estudio como en los receptores discretos cercanos al proyecto, los cuales
corresponden principalmente a viviendas cercanas a Planta COMFRUT.

Debido a que en Chile no existe normativa que regule la emisión ni la inmisión de olores por parte
de una planta de estas características, se utiliza como referencia, normativas internacionales. Es
por esto que las concentraciones de olor (OU E /m [3] ) resultantes del modelo, para cada receptor
discreto, fueron comparados con el límite de inmisión establecido en la normativa de Colombia.
En esta normativa establece un límite de inmisión de 3,0 OU E /m [3] para percentil 98, que aplica a
la contaminación de olor generada por el tratamiento de aguas residuales. Importante señalar
que este valor límite se ha utilizado en diferentes proyectos del mismo rubro en él SEA.

La dispersión de las emisiones de olor de la Planta COMFRUT indica que el área de influencia,
para el Escenario Actual, cubre un área total de 2.152 m [2], con una longitud aproximada de 68 m
en dirección norte-sur. Para el caso del Escenario Futuro, el área de influencia comprende un
área de 2.174 m [2], con igual longitud norte-sur de 68 m. El área de influencia corresponde a la
superficie circunscrita por 1 OU E /m [3], establecida en la “Guía para la predicción y evaluación de
impactos por olor en SEIA” del año 2017, la cual indica la concentración en donde el 50% de la
población puede comenzar a detectar un olor. Dicha concentración también es definida como el
límite de detección.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 7 de 50

Las isodoras visualizadas en la siguiente cartografía del Escenario Actual, presentan valores de
0,1 a 2,28 OU E /m [3] alcanzando su mayor concentración dentro de los deslindes de planta. Fuera
de los límites de la planta las isodoras trazan valores menores al límite de detección de 1,0
OU E /m [3], valor que también define el área de influencia (2.152 m [2] ), tal como se menciona en el
párrafo anterior.

**Figura No 1** . Mapa de concentración de olor. Escenario Actual (Percentil 98).

Para el caso del Escenario Futuro, se mantiene un comportamiento similar, en donde el valor de
2,28 OU E /m [3] sigue siendo el punto de máxima concentración, presente dentro de los deslindes
de planta. En este escenario se presenta un leve aumento en la dispersión de emisiones,
reflejado por ejemplo en su área de influencia, la cual comprende ahora 2.174 m [2] .

**Figura No 2** . Mapa de concentración de olor. Escenario Futuro (Percentil 98).

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 8 de 50

En base a lo mencionado anteriormente, en la siguiente Tabla, se presenta en forma detallada
las concentraciones de inmisión de olor en los receptores, donde se puede observar que ninguno
supera las 3 OU E /m [3 ] (Percentil 98).

**Tabla No 4** . Concentración receptores. Percentil 98.

|No|ID|Descripción|Concentración de inmisión<br>(OU /m3)<br>E|Col5|Límite inmisión<br>(Norma<br>colombiana)|
|---|---|---|---|---|---|
|**No**|**ID**|**Descripción**|**Escenario**<br>**Actual**|**Escenario**<br>**Futuro**|**Escenario**<br>**Futuro**|
|1|R1|Vivienda Lote 1|0,09|0,10|**3,0**<br>**OUE/m3 **<br>**(percentil 98)**|
|2|R2|Vivienda Lote 2|0,08|0,09|0,09|
|3|R3|Vivienda Lote 3|0,05|0,06|0,06|
|4|R4|Vivienda Lote 4|0,06|0,07|0,07|
|5|R5|Vivienda Lote 5|0,03|0,03|0,03|
|6|R6|Vivienda Lote 6|0,01|0,01|0,01|
|7|R7|Vivienda Lote 7|0,01|0,01|0,01|
|8|R8|Vivienda Lote 8|0,06|0,07|0,07|
|9|R9|Vivienda Lote 9|0,07|0,08|0,08|
|10|R10|Vivienda Lote 10|0,07|0,08|0,08|
|11|R11|Vivienda Lote 11|0,07|0,08|0,08|
|12|R12|Receptor Copeval|0,27|0,27|0,27|
|13|R13|Vivienda Lote 13|0,06|0,07|0,07|
|14|R14|Vivienda Lote 14|0,05|0,07|0,07|
|15|R15|Vivienda Lote 15|0,06|0,08|0,08|

Se evaluó el efecto generado en quince receptores discretos, en donde la evaluación de los
resultados, demostró que en ninguno de ellos superó el límite de referencia de 3 OU E /m [3], siendo
los más altos el receptor N°12 (Receptor Copeval) con una concentración de inmisión de 0,27
OU E /m [3], lo cual indica que las emisiones de la planta no implican una potencial afectación sobre
la salud de la población cercana, sistema de vida y costumbres, población protegida, y turismo.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 9 de 50

**2** **Introducción**

En el marco de la evaluación ambiental de planta COMFRUT S.A. Curicó, se solicitó los servicios
de Proterm S.A. con el objetivo de evaluar la actual y futura dispersión de olores provenientes de
las principales fuentes con potencial de emisión. Tales fuentes consideradas corresponden a 12,
principalmente referentes al Sistema de Tratamiento de RILes.

El proyecto contempla evaluar el proceso de tratamiento de RILes, iniciando en una Cámara de
recolección de RIL, para luego ir paso a paso por un Pretratamiento de retiro de sólidos, Canal
de sedimentación, Estanque aireado, Filtro lamelar, Cámara de lodos, Estanques de paso,
Cámara de contacto, Estanque de acumulación de RIL tratado, Tranque de acumulación, Área
de riego y Contenedor de residuos.

Planta COMFRUT se encuentra ubicada en la Región del Maule, comuna de Curicó, a unos 7
km del centro de la ciudad, en Zona Urbana Mixta según Plan Regulador Comunal. A
continuación, se detalla la ubicación geográfica de Planta, el emplazamiento del archivo WRF y
la zona modelada.

**Figura No 3** . Mapa ubicación del proyecto evaluado.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 10 de 50

**3** **Objetivos General**

Evaluar bajo un escenario actual y futuro, el efecto de las emisiones de olor de Planta COMFRUT
S.A. Curicó, sobre la salud de la población cercana, sistema de vida, costumbres, población
protegida y turismo.

**Objetivos específicos**

Determinar las emisiones de olor, actuales y futuras, generadas por COMFRUT S.A. Curicó.

Evaluar el efecto de la dispersión de olores en quince receptores discretos de interés
cercanos al proyecto.

Analizar y evaluar las variables meteorológicas consideradas en la modelación respecto a las
estaciones más cercanas al proyecto.

**4** **Metodología**

A continuación, se presenta la metodología que permitió evaluar las emisiones odorantes de
planta COMFRUT S.A. Curicó.

**Caracterización de las fuentes**

Para poder evaluar los objetivos propuestos, se plantea el siguiente escenario:

Modelación de olor de las fuentes actuales y futuras, evaluando la dispersión de la pluma con
respecto a los receptores discretos considerados.

Por otro lado, para poder caracterizar las fuentes generadoras de olor, se utilizaron las siguientes
metodologías.

- Detección satelital: Mediante Google Earth Pro, se identificaron las superficies de las fuentes
generadoras de emisión y la distancia con respecto a los sectores poblados.

- Solicitud de información: Se solicitó información tanto al consultor del proyecto como al
encargado del proyecto en planta.

Revisión bibliográfica: Se consultaron diferentes plataformas para obtener información sobre
la ubicación, procesos, producción y tipos de fuentes de emisión de olor relacionadas con el
tipo de fuente a evaluar. Asimismo, se utiliza como base para identificación de las fuentes, el
estudio: Antecedentes para la regulación de olores en Chile, y la Estrategia para la gestión
de olores en Chile, aprobada a través la Resolución Exenta N°947 el 7 de noviembre de 2013
del Ministerio de Medio Ambiente. De igual forma es utilizada la base de datos del SEA,
específicamente proyectos aprobados con factores de emisión aplicables al proyecto en
cuestión.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 11 de 50

**Estimación de emisiones**

Para conocer las emisiones del “Proyecto” se utilizaron Factores de Emisión, considerando un
proyecto aprobado, con un sistema productivo de la misma índole.

**Factores de emisión de olor (OEF)** : son análogos a los factores de emisión desarrollados por
la US EPA para otros contaminantes. Se utiliza la siguiente ecuación:

OER= A∗OEF

Donde OER es la tasa de emisión de olor en (OU E /s), A es el nivel de actividad, OEF es el factor
de emisión.

**Figura No 4** . Esquema resumen de las metodologías para estimar las emisiones de olor.

**Evaluación de la dispersión de las emisiones de olor**

A continuación, se presentan las etapas necesarias para realizar la modelación de dispersión de

olores:

**4.3.1 Selección del Modelo**

Para seleccionar el modelo se consideraron los lineamientos que establece la Guía para el uso
de modelos de calidad del aire en el SEIA, publicada por el Servicio de Evaluación Ambiental el

año 2012.

Se consideró un modelo tipo Puff, el cual es una combinación entre los modelos Gaussiano y
Lagrangiano, en el sentido que esencialmente calculan la dispersión de contaminantes
provenientes de una emisión instantánea, llamada “Puff”, a lo largo de una trayectoria. Su
aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada punto
de una trayectoria. Es decir, a diferencia de los modelos Langrangianos que necesitan el cálculo
de un gran número de trayectorias para una fuente, los modelos tipo “Puff” sólo requieren una
trayectoria por “Puff”, lo que hace su cálculo mucho más rápido [1] .

1 Guía para el uso de modelos de calidad del aire, 2023.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 12 de 50

Para la modelación se utilizó el software Calpuff versión 7.2.1 junto a los módulos CALPOST
7.1.0. y CALRANK 7.0.0. Además, para efectos de la interacción gráfica de los módulos, se usó
el software interactivo CALPUFF View 8.5.0.

En Anexo No1 se presenta un esquema de funcionamiento del software Calpuff.

**4.3.2 Recopilación de Antecedentes Para la Modelación**

Para conocer la dispersión que tendrán los contaminantes en un área determinada es preciso
incorporar al modelo seleccionado distintos parámetros de manera que la simulación sea lo más
parecida a las condiciones reales. Las variables o entradas que requirió el modelo se muestran
en la tabla a continuación:

**Tabla No 5.** Variables de entrada consideradas en la modelación

|Variable|Parámetros|Fuente|
|---|---|---|
|Meteorológicas|Dirección de Viento|Tal como lo establece la guía el modelo<br>numérico recomendado para la generación de<br>datos meteorológicos es el Weather Research<br>and Forecasting Model (WRF)2. WRF es uno<br>de los modelos meteorológicos de pronóstico<br>más avanzados y completos y es mantenido<br>por NCAR9/NOAA10 de Estados Unidos.|
|Meteorológicas|Velocidad de Viento|Velocidad de Viento|
|Meteorológicas|Temperatura|Temperatura|
|Meteorológicas|Presión|Presión|
|Meteorológicas|Precipitación|Precipitación|
|Geofísicas|Elevación del Terreno|Elevación del Terreno|
|Geofísicas|Uso de Suelo|Uso de Suelo|
|Características de la<br>fuente|Fuentes de emisión|Información proporcionada por el mandante<br>del proyecto.|
|Características de la<br>fuente|Superficies de fuentes de<br>emisión|Superficies de fuentes de<br>emisión|
|Receptores Discretos|Coordenadas de los<br>receptores|Se definieron los poblados cercanos a Planta,<br>definiendo viviendas e instalaciones como<br>receptores, lo cuales fueron proporcionados<br>por el consultor.|

**4.3.3 Variables meteorológicas y geofísicas**

Tal como se mencionó en el punto 4.3.1, se utilizó la meteorología de pronóstico WRF en formato
calmet.dat, de esta forma se incorporó el archivo directamente al programa. El archivo
meteorológico tiene su centro en la comuna de Teno, Provincia de Curicó. Para la ejecución del
modelo se modeló una zona más pequeña en comparación al WRF, es importante destacar que
la zona modelada tiene 5 dimensiones de grilla de 20, 50, 250, 500 y 1.000 metros. En la tabla
N°3 se presentan las características del archivo meteorológico y en la figura N°3 los límites
indicados (figura en apartado “introducción”).

2 Se consideró un WRF del año 2021, dicho año presentó datos meteorológicos estables.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 13 de 50

**Tabla No 6.** Características del archivo meteorológico WRF.

|Datos|Col2|Archivo Meteorológico|
|---|---|---|
|Comuna|Comuna|Teno|
|Dimensión grilla|Dimensión grilla|63x63 km|
|Espaciado grilla|Espaciado grilla|1 km|
|Fecha-Hora inicio|Fecha-Hora inicio|01-01-2021 00:00|
|Fecha-Hora fin|Fecha-Hora fin|31-12-2021 23:00|
|Datum|Datum|WGS-84 Huso 19 S|
|Coordenadas NO|Este|268.183|
|Coordenadas NO|Norte|6.171.196|
|Coordenada NE|Este|331.401|
|Coordenada NE|Norte|6.172.655|
|Coordenada SO|Este|269.611|
|Coordenada SO|Norte|6.108.235|
|Coordenadas SE|Este|332.766|
|Coordenadas SE|Norte|6.109.687|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 14 de 50

**4.3.4 Evaluación de los resultados**

En Chile hoy en día no existe normativa nacional aplicable, específica para este tipo de proyectos,
sin embargo, según el Reglamento del SEIA (Art. 11), en el caso de no existir normativa nacional
se debe acudir a normativas de referencia en donde se debe priorizar estados que posean
similitudes en sus componentes ambientales, con la situación nacional y/o local. De esta manera,
los resultados de las concentraciones de olor (OU E /m [3] ) arrojadas por el modelo de dispersión,
fueron comparados con:

(1) Límite establecido en la Resolución No1.541 - 2013, Colombia. [3]

A continuación, se presenta la tabla que resume los límite de inmisión establecidos por actividad.

**Tabla No 7** . Límites de inmisión según la resolución vigente No1.541 del Ministerio de Ambiente

y Desarrollo Sostenible de Colombia, para el percentil 98 [4] .

|Nivel Permisible<br>OU /m3<br>E|Actividad|
|---|---|
|3|**Procesamiento y conservación de carne, pescado, crustáceos y moluscos.**<br>Fabricación de productos de la refinación del petróleo.<br>Fabricación de pulpas (pastas) celulósicas; papel y cartón.<br>Curtido y recurtido de cueros; recurtido y teñido de pieles.<br>Tratamiento y disposición de desechos no peligrosos y estaciones de<br>transferencia.<br>Planta de tratamiento de aguas residuales.<br>Actividades que capten agua de cuerpos de agua receptores de vertimientos.<br>Fabricación de sustancias y productos químicos básicos.<br>Tratamiento térmico de subproductos de animales.|
|5|Unidad de producción pecuaria.<br>Elaboración de aceites y grasas de origen vegetal.|
|7|Descafeinado, tostión y molienda de café.<br>Otras actividades.|

La norma señala 3 OU E /m [3 ] como nivel permisible de calidad del aire para procesos que cuenten
con Planta de tratamiento de aguas residuales. Importante señalar que este valor límite se ha
utilizado en diferentes proyectos del mismo rubro evaluados en el marco del Sistema de
Evaluación de Impacto Ambiental (SEIA).

Por otro lado, junto a los resultados de concentración de olor, se identificará el área de influencia
de la operación de la planta. Tal como lo indica la guía, el área de Influencia se debe circunscribir
en el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de detección del
olor compuesto.

3 Ministerio de Ambiente y Desarrollo Sostenible (2013). Resolución N°1541-2013 Niveles permisibles de calidad del
aire o de inmisión y procedimiento para la evaluación de actividades que generan olores ofensivos, Colombia.

4 Importante mencionar, que este límite se ha indicado en otros proyectos referentes a elaboración y procesamiento
de productos del mar en la región.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 15 de 50

**4.3.5 Área de Influencia y receptores de interés.**

Una vez ejecutado el modelo de dispersión de olor, se realizó el análisis de post-proceso
obteniendo las curvas iso-concentración de la dispersión anual. Tal como lo indica la guía el Área
de Influencia se debe circunscribir en el espacio contenido por la isodora de 1 OU E /m [3], que
corresponde al umbral de detección del olor compuesto.

Una vez determinado el área de influencia, se realizó una descripción general y significativa del
Área de Influencia, para cada elemento del medio ambiente considerando los efectos,
características o circunstancias establecidos en el artículo 11 de la Ley N°19.300 como
población, población protegida, grupos humanos y visitantes o turistas.

De acuerdo a lo establecido en la Guía para la predicción y evaluación de impacto por olor en el
SEIA, señala que _“La evaluación de los impactos ambientales por olor debe realizarse según las_
_consideraciones y criterios establecidos en los artículos del 5 al 9 del Reglamento del SEIA,_
_según lo siguiente”:_

 _Población en cuanto a la salud de la población (letra a)._

 _Grupos humanos, en cuanto a los sistemas de vida y costumbres (letra c)._

 _Población protegida (letra d)._

 _Visitantes o turistas, en cuanto componente el valor turístico de una zona (letra e)._

**Evaluación del desempeño del archivo de pronóstico utilizado**

El modelo numérico recomendado para la generación de datos meteorológicos es el Weather
Research and Forecasting Model (WRF). WRF es uno de los modelos meteorológicos de
pronóstico más avanzados y completos, que es mantenido por NCAR/NOAA de Estados Unidos.

Todos los modelos tienen asociados errores e incertidumbre. Los resultados del modelo se

analizan en base a la comparación de los gráficos indicados en los puntos 6.6.3 y 6.7 de la “Guía
para uso de modelos de Calidad del aire en el SEIA”. En base a la comparación de los ciclos
diarios de las variables meteorológicas observadas y simuladas, en la misma, ubicación, se debe
caracterizar la capacidad del modelo de reproducir las observaciones tanto en magnitud como
en su variabilidad.

Para cumplir con lo indicado por la guía para uso de modelos de dispersión del SEA, se realizó
un análisis del desempeño de la meteorología de pronóstico WRF utilizada para la modelación.
Este análisis permite detectar posibles desviaciones en el modelo de pronóstico que podrían
causar efectos en los resultados del modelo de dispersión. Para este informe se contrastaron las
variables de viento respecto a los registros de la estación pública Curicó desde el sistema SINCA.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 16 de 50

**5** **Resultados**

A continuación, se presentan los resultados que permitirán evaluar el efecto de las emisiones de
olor del Proyecto en estudio.

**Caracterización de las fuentes de emisión**

A continuación, se describen las fuentes generadoras de olor para los escenarios actual y futuro
a modelar. En la siguiente tabla se detallan las fuentes consideradas en la modelación, mientras
que en la cartografía se presenta su ubicación espacial. Lo anterior de acuerdo con lo señalado
en el punto 3.3 de guía para la predicción y evaluación de olores.

**Tabla No 8** . Descripción fuentes y procesos asociados [5] .

|Fuente|Descripción de referencia|
|---|---|
|Cámara de recolección<br>RIL|Cámara que recibe los flujos de RIL del proceso, posee bomba que<br>impulsa hacia el sistema de pretratamiento.|
|Pretratamiento|Se compone de un filtro rotatorio con malla con un paso de 1 mm para<br>eliminar los sólidos. Estos solidos caen a un bin plástico para luego ser<br>llevado a la zona de residuos. Las medidas de la superficie expuesta<br>corresponden a las medidas del Bin|
|Canal de sedimentación|Canal con separaciones que permiten la sedimentación de los sólidos no<br>captados en el pretratamiento.|
|Estanque aireado|Estanque que presenta un sistema de aireación por agitación, para luego<br>mediante una bomba impulsar hacia el filtro lamelar.|
|Filtro lamelar|Filtro que posee distintos canales verticales de manera diagonal para<br>captar y separar los sólidos suspendidos en el tratamiento.|
|Cámara de lodos|Almacenamiento de lodos del proceso, posterior a la acción del filtro<br>lamelar.|
|Estanques de paso|Estanques de acumulación de RILes posteriores al proceso del filtro<br>lamelar.|
|Cámara de contacto|Cámara de estructura serpenteante, encargada de la adición y mezcla de<br>desinfectantes al RIL.|
|Estanque acumulación RIL<br>tratado|Encargado de la acumulación luego de terminado el proceso de<br>tratamiento, posterior el último paso en cámara de contacto.|
|Tranque de acumulación|Acumulación de RIL tratado, para luego disponer en áreas de riego<br>colindantes a dicho tranque.|
|Área de riego|Zona de aplicación de RIL tratado.|
|Contenedor de residuos|Contenedores de residuos generados en loza de residuos, lo cuales por<br>lo normal son dos.|

5 Información entregada por el titular .

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 17 de 50

**Régimen de emisión**

A continuación, se describe el régimen de emisión de las fuentes a evaluar en ambos escenarios:

**Tabla No 9** . Régimen de emisión de fuentes [6] .

|Fuente|Detalle del régimen de emisión|
|---|---|
|Cámara de recolección RIL|Operación de 10 meses al año, con un receso normalmente<br>en los meses de Julio y Agosto.<br>El área de riego no será utilizada en los meses de invierno<br>debido a las precipitaciones (junio, julio y agosto)<br>Se define un riego que opera aprox. 2 hrs. Diarias:<br>- 1 hr. En la mañana de 8 a 9hrs.<br>- 1 hrs. en la tarde de 20 a 21hrs.<br>Riego ejecutado de Diciembre a Marzo. El resto de los<br>meses solo 1hr. al día.|
|Pretratamiento|Pretratamiento|
|Canal de sedimentación|Canal de sedimentación|
|Estanque aireado|Estanque aireado|
|Filtro lamelar|Filtro lamelar|
|Cámara de lodos|Cámara de lodos|
|Estanques de paso|Estanques de paso|
|Cámara de contacto|Cámara de contacto|
|Estanque acumulación RIL tratado|Estanque acumulación RIL tratado|
|Tranque de acumulación|Tranque de acumulación|
|Área de riego|Área de riego|
|Contenedor de residuos|Contenedor de residuos|

**Ubicación de fuentes**

A continuación, se presentan las coordenadas de las fuentes evaluadas, y la cartografía
respectiva tanto para el Escenario Actual como Futuro.

**Tabla No 10.** Coordenadas de fuentes de emisión odorantes. Escenario Actual.

|Nro.|Fuente|Coordenadas WGS-84 Huso 19S|Col4|
|---|---|---|---|
|**Nro.**|**Fuente**|**Este (m)**|**Norte (m)**|
|**1 **|Cámara de recolección RIL|297.055|6.123.886|
|**2 **|Pretratamiento|297.042|6.123.880|
|**3 **|Canal de sedimentación|297.132|6.123.826|
|**4 **|Estanque aireado|296.822|6.123.796|
|**5 **|Filtro lamelar|296.811|6.123.757|
|**6 **|Cámara de lodos|297.060|6.123.876|
|**7 **|Estanques de paso|297.042|6.123.885|
|**8 **|Cámara de contacto|297.098|6.123.801|
|**9 **|Estanque acumulación RIL tratado|297.139|6.123.830|
|**10**|Tranque de acumulación|297.048|6.123.876|
|**11**|Área de riego|297.040|6.123.884|
|**12**|Contenedor de residuos 1|296.973|6.123.847|
|**13**|Contenedor de residuos 2|296.977|6.123.841|

6 Información entregada por el titular .

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 18 de 50

En la siguiente figura se presenta la ubicación espacial de las fuentes de emisión consideradas
en la modelación para el Escenario Actual.

**Figura No 5** . Ubicación espacial de las fuentes. Escenario Actual.

**Tabla No 11.** Coordenadas de fuentes de emisión odorantes. Escenario Futuro.

|Nro.|Fuente|Coordenadas WGS-84 Huso 19S|Col4|
|---|---|---|---|
|**Nro.**|**Fuente**|**Este (m)**|**Norte (m)**|
|**1 **|Cámara de recolección RIL|297.055|6.123.886|
|**2 **|Pretratamiento|297.042|6.123.880|
|**3 **|Canal de sedimentación|297.132|6.123.826|
|**4 **|Estanque aireado|296.822|6.123.796|
|**5 **|Filtro lamelar|296.811|6.123.757|
|**6 **|Cámara de lodos|297.060|6.123.876|
|**7 **|Estanques de paso|297.042|6.123.885|
|**8 **|Cámara de contacto|297.098|6.123.801|
|**9 **|Estanque acumulación RIL tratado|297.139|6.123.830|
|**10**|Tranque de acumulación|297.048|6.123.876|
|**11**|Área de riego|297.040|6.123.884|
|**12**|Contenedor de residuos 1|296.973|6.123.847|
|**13**|Contenedor de residuos 2|296.977|6.123.841|
|**14**|Filtro lamelar 2|297.043|6.123.881|
|**15**|Cámara de lodos 2|297.038|6.123.885|
|**16**|Tranque de acumulación 2|296.832|6.123.790|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 19 de 50

En la siguiente figura se presenta la ubicación espacial de las fuentes de emisión consideradas
en la modelación para el Escenario Actual.

**Figura No 6** . Ubicación espacial de las fuentes. Escenario Futuro.

**Factores de emisión utilizados**

Ante la carencia de factores de emisión para este tipo de industria, se realizó una búsqueda en
el SEIA con el objetivo de encontrar emisiones de referencia para proyectos y/o actividades
similares. La búsqueda se enfoca principalmente en proyectos recientemente ingresados, en
donde fue posible contar con el proyecto aprobado “DIA de Regularización Proyecto Planta Riles
Frusur, San Carlos”, con RCA del 13 de julio del 2022. Dicho proyecto contempla gran similitud
en el proceso productivo con respecto a la COMFRUT, por lo que se define como buena base de
referencia para contemplar en el presente proyecto. Los factores de emisión de referencia de
dicho estudio de presentan a continuación.

**Tabla No 12.** Factores de emisión base para estudio en cuestión.

|Fuente Evaluada|Factor de Emisión<br>(OU /m2s)<br>E|Origen Factor de<br>emisión|
|---|---|---|
|**Contenedor de residuos**|0,0605|DIA Regularización<br>Proyecto Planta de RILes<br>FRUSUR San Carlos|
|**Sedimentador PTR**|0,0447|0,0447|
|**Reactor PTR**|0,0447|0,0447|
|**Reactor PTAS**|0,0449|0,0449|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 20 de 50

Por otro lado, en la siguiente tabla, se presenta el detalle de las fuentes a evaluar, con su
respectivo factor de emisión, asociado a la fuente de referencia del cual se homologa el valor.

**Tabla No 13.** Factores de emisión asociados a las fuentes evaluadas en el presente estudio.

|Nro.|Fuente Evaluada|Factor de Emisión<br>(OU /m2s)<br>E|Fuente Referencial de<br>homologación|
|---|---|---|---|
|**1 **|**Cámara de recolección RIL**|0,0605|Reactor PTAS|
|**2 **|**Pretratamiento**|0,0447|Sedimentador PTR|
|**3 **|**Canal de sedimentación**|0,0447|Sedimentador PTR|
|**4 **|**Estanque aireado**|0,0449|Reactor PTR|
|**5 **|**Filtro lamelar**|0,0449|Reactor PTR|
|**6 **|**Cámara de lodos**|3,07|Contenedor de residuos|
|**7 **|**Estanques de paso**|0,0447|Sedimentador PTR|
|**8 **|**Cámara de contacto**|0,0447|Sedimentador PTR|
|**9 **|**Estanque acumulación RIL tratado**|0,0447|Sedimentador PTR|
|**10**|**Tranque de acumulación**|0,0447|Sedimentador PTR|
|**11**|**Área de riego**|0,0447|Sedimentador PTR|
|**12**|**Contenedor de residuos**|3,07|Contenedor de residuos|

Resuelta la obtención de factores de emisión, se procede a evaluar las emisiones que serán
incorporadas al modelo tanto para el escenario actual como futuro. Mayor detalle en el siguiente
apartado.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 21 de 50

**Emisiones de olores**

A continuación, se presentan las emisiones de olores obtenidas por la revisión bibliográfica de factores de emisión de olor (OEF),
expresadas en tasa de emisiones de olor (OU E /s), esto en base a la “Guía para la predicción y evaluación de impacto por olor en el
SEIA”, en donde cada factor de emisión es justificado debidamente a continuación como es solicitado.

**Tabla No 14** . Factores de emisión y emisión asociada a cada fuente.

|Nro.|Fuentes|Factor de<br>Emisión<br>(OUE/m2s)|ESCENARIO ACTUAL|Col5|Col6|Col7|ESCENARIO FUTURO|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Nro.**|**Fuentes**|**Factor de**<br>**Emisión**<br>**(OUE/m2s)**|**Área**<br>**(m2)**|**Emisión**<br>**(OUE/s)**|**Cantidad**|**Emisión**<br>**Total**<br>**(OUE/s)**|**Área**<br>**(m2)**|**Emisión**<br>**(OUE/s)**|**Cantidad**|**Emisión**<br>**Total**<br>**(OUE/s)**|
|1|Cámara de recolección<br>RIL|0,0605|2,30|0,14|1|0,14|2|0,14|1|0,14|
|2|Pretratamiento|0,0447|1,20|0,05|1|0,05|1|0,05|1|0,05|
|3|Canal de sedimentación|0,0447|13,71|0,61|1|0,61|14|0,61|1|0,61|
|4|Estanque aireado|0,0449|26,32|1,18|1|1,18|26|1,18|1|1,18|
|5|Filtro lamelar|0,0449|4,00|0,18|1|0,18|4|0,18|**2 **|0,36|
|6|Cámara de lodos|3,07|2,88|8,84|1|8,84|3|8,84|**2 **|17,68|
|7|Estanques de paso|0,0447|2,66|0,12|1|0,12|3|0,12|1|0,12|
|8|Cámara de contacto|0,0447|9,96|0,45|1|0,45|10|0,45|1|0,45|
|9|Estanque acumulación<br>RIL tratado|0,0447|5,31|0,24|1|0,24|5|0,24|1|0,24|
|10|Tranque de<br>acumulación|0,0447|300|13,41|1|13,41|300|13,41|**2 **|26,82|
|11|Área de riego|0,0447|5.200|232|1|232|4.890|219|1|219|
|12|Contenedor de residuos|3,07|12,50|38,38|2|76,76|13|38,38|2|76,76|

En la tabla anterior, se puede observar que las mayores emisiones provienen del área de riego con 232 OU E /s en el escenario actual
y 219 OU E /s en el escenario futuro, seguida del contenedor de residuos y el tranque de acumulación.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 22 de 50

**Evaluación de la dispersión de olores**

A continuación, se presentan los resultados de dispersión y concentración de olores en el área
de estudio y en los receptores discretos considerados (quince), tanto para el escenario actual
como futuro.

Escenario Actual: comprende 12 fuentes correspondientes al sistema de tratamiento de RILes,
en donde una de ellas, correspondiente a contenedor de residuos, presenta dos unidades.
Estas fuentes de COMFRUT S.A. Curicó, se presentan en la comuna de Curicó, Provincia de
Curicó, Región del Maule.

Escenario Futuro: comprende las mismas 12 fuentes base, del escenario actual, con algunas
modificaciones que apuntan a la adición de un Filtro lamelar, una segunda Cámara de lodos y
un segundo Tranque de acumulación. El resto de las fuentes se mantienen.

Para ambos escenarios, se presenta un mapa de dispersión de olor, el cual registra el percentil
98 de las concentraciones horarias, con el objetivo de poder comparar los resultados con el
límite de referencia propuesto por Colombia, según la resolución vigente N°1.541 del Ministerio
de Ambiente y Desarrollo Sostenible.

Considerando que los criterios de máximo impacto horario, o condición más desfavorable, no
son representativos de una condición de exposición permanente sintetizada en un año, debido
a la variación del estado meteorológico estacional de un determinado lugar, se recomienda el
uso del criterio de percentil 98 el cual permite visualizar los porcentajes de horas en que se
supera el valor definido para las 8.760 horas del año [7] .

**5.6.1 Dispersión de emisiones de olor. Escenario Actual.**

En la figura a continuación se muestra la dispersión de odorantes de Planta COMFRUT S.A.
Curicó. La imagen presenta las máximas concentraciones de olor en las zonas aledañas a la
planta, considerando una excedencia de un 2%, lo que es comparado con las normas de
referencia. El análisis presente indica que durante el 98% de las horas del año se presentarán
concentraciones igual o menor al valor indicado en la cartografía.

Tal como se puede apreciar en la siguiente cartografía, las isodoras visualizadas en la siguiente
cartografía del Escenario Actual, presentan valores de 0,1 a 2,28 OU E /m [3] alcanzando su mayor
concentración dentro de los deslindes de planta. Fuera de los límites de la planta las isodoras
trazan valores menores al límite de detección de 1,0 OU E /m [3], valor que también define el área
de influencia.

7 Según la Guía para la predicción y evaluación de impactos por olor en el SEIA, 2017.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 23 de 50

**Figura No 7** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio

horario, percentil 98. Escenario Actual.

**5.6.2 Punto Máxima concentración de olor. Escenario Actual.**

En función de la dispersión de olor, se determina el punto de máxima concentración, el cual se
se posiciona dentro del deslinde de planta, en la zona de losa de residuos, a un costado de los
contenedores de residuos, alcanzando una concentración de 2,28 OU E /m [3] . Detalle de
concentración y coordenadas a continuación.

**Tabla No 15.** Punto máximo concentración para percentil 98. Coordenadas UTM 19S.

Escenario Actual.

|Concentración<br>(OU /m3)<br>E|Coordenada Este (m)|Coordenada Norte (m)|
|---|---|---|
|2,28|296.980|6.123.841|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 24 de 50

**5.6.3 Área de Influencia. Escenario Actual.**

Con base en la dispersión de emisiones del escenario evaluado, se determinó un área de
influencia definida según la “Guía para la predicción y evaluación de impactos por olor en el
SEIA” [8], como el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de
detección del olor compuesto, es decir, es la concentración en donde el 50% de la población
puede percibir un olor.

A continuación, se observa el mapa con el emplazamiento de área de influencia circunscrita por
el límite de isoconcentración de 1 OU E /m [3] .

**Figura No 8.** Mapa del Área de Influencia (AI), definida por 1 OU E /m [3] . Escenario Actual.

La isodora de 1 OU E /m3, valor que indica la concentración desde el cual el 50% de la población
puede percibir un olor, cubre una superficie de **2.152 m** **[2]** . La distribución de la pluma se acentúa
en sentido norte-sur con una longitud aproximada de 68 metros. Dicha área de influencia no
circunscribe a ninguno de los 15 receptores discretos considerados en la evaluación.

8 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 25 de 50

**5.6.4 Receptores discretos considerados en la modelación**

A continuación, se detallan los receptores discretos considerados en la modelación,
coordenadas y distancia con respecto a planta.

**Tabla No 16** . Receptores discretos considerados en la modelación.

|No|ID|Distancia a planta (m)|Coordenadas UTM WGS-84 Zona 19 S|Col5|
|---|---|---|---|---|
|**No**|**ID**|**Distancia a planta (m)**|**Este (m)**|**Norte (m)**|
|R1|Vivienda Lote 1|75|296.991|6.123.743|
|R2|Vivienda Lote 2|163|297.156|6.123.794|
|R3|Vivienda Lote 3|415|297.067|6.123.409|
|R4|Vivienda Lote 4|393|297.313|6.123.587|
|R5|Vivienda Lote 5|632|297.451|6.123.381|
|R6|Vivienda Lote 6|890|297.620|6.123.184|
|R7|Vivienda Lote 7|979|297.783|6.123.238|
|R8|Vivienda Lote 8|435|297.412|6.123.695|
|R9|Vivienda Lote 9|265|297.228|6.123.943|
|R10|Vivienda Lote 10|309|297.074|6.124.116|
|R11|Vivienda Lote 11|344|296.959|6.124.160|
|R12|Receptor Copeval|152|296.976|6.123.969|
|R13|Vivienda Lote 13|244|296.759|6.123.881|
|R14|Vivienda Lote 14|312|296.684|6.123.787|
|R15|Vivienda Lote 15|254|296.881|6.123.590|

**Figura No 9** . Receptores discretos considerados en la modelación.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 26 de 50

**5.6.1 Concentración en Receptores. Escenario Actual.**

En la siguiente tabla, se presenta el resultado del Percentil 98, de las concentraciones horarias
para cada receptor discreto considerado en la modelación. Tal como se puede apreciar en la
tabla, la operación actual de planta produce concentraciones de inmisión que se encuentran
bajo el límite de referencia establecido en la normativa colombiana (3,0 OU E /m [3] ). La mayor
concentración se observa en el receptor 12 (Receptor Copeval) que alcanzan un valor de 0,27
OU E /m [3] respectivamente, concentración que se encuentran bajo el límite de detección (1,0
OU E /m [3] ) y de molestia (3,0 OU E /m [3] ) establecido en la normativa de referencia.

**Tabla No 17** . Concentración receptores, percentil 98 . Escenario Actual.

|ID|Descripción|Concentración de<br>inmisión (OU /m3)<br>E|Límite inmisión<br>(Norma colombiana)|
|---|---|---|---|
|R1|Vivienda Lote 1|0,09|**3,0**<br>**OUE/m3 **<br>**(percentil 98)**|
|R2|Vivienda Lote 2|0,08|0,08|
|R3|Vivienda Lote 3|0,05|0,05|
|R4|Vivienda Lote 4|0,06|0,06|
|R5|Vivienda Lote 5|0,03|0,03|
|R6|Vivienda Lote 6|0,01|0,01|
|R7|Vivienda Lote 7|0,01|0,01|
|R8|Vivienda Lote 8|0,06|0,06|
|R9|Vivienda Lote 9|0,07|0,07|
|R10|Vivienda Lote 10|0,07|0,07|
|R11|Vivienda Lote 11|0,07|0,07|
|R12|Receptor Copeval|0,27|0,27|
|R13|Vivienda Lote 13|0,06|0,06|
|R14|Vivienda Lote 14|0,05|0,05|
|R15|Vivienda Lote 15|0,06|0,06|

En el Anexo N°2 se presenta el análisis de la variación horaria de olor, en el receptor discreto
que presenta la mayor concentración de olor.

.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 27 de 50

**5.6.2 Protocolo FIDOL. Escenario Actual.**

Conforme a lo estipulado por la “Guía para la predicción y evaluación de impactos por olor en
el SEIA”, se evalúa la significancia de la inmisión de olor en los receptores establecidos
mediante el Protocolo FIDOL, que habla sobre:

 Frecuencia: referido a la frecuencia que la o las personas están expuestas al olor.

 Intensidad: referido a la percepción de la fuerza del olor.

 Duración: referido al tiempo de un episodio de olor.

 - Ofensividad: referido a la caracterización del olor.

 Localización: referido al tipo de uso del suelo y la naturaleza de las actividades aledañas
a una fuente de olor. Se puede considerar que el factor “localización” abarca las
características del receptor como su sensibilidad, vulnerabilidad y otros.

A continuación, se desglosan los puntos mencionados:

**Tabla No 18** . Protocolo FIDOL. Escenario Actual.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia<br>>3 OUe/m3|Planta COMFRUT 10 meses del año, con un receso en los meses de julio y agosto. Sin<br>embargo, durante el 98% de las horas del año no se prevé superación de 1 OUE/m3 <br>(umbral de detección) y 3 OUE/m3 (umbral de molestia). Por lo tanto, no se prevé<br>afectación en términos de frecuencia.|
|Intensidad|Ningún receptor se encuentra sobre las 3 OUE/m3 en el percentil 98, de la normativa de<br>referencia (concentración que representa el umbral de molestia). Dado que los<br>resultados en los receptores son menores a 3 OUE/m3, no se prevé afectación en<br>términos de intensidad en los 15 receptores considerados en la modelación.|
|Duración|En cuanto a la duración, pese a que la proyecto contempla una operación constante en<br>10 meses del año, con un receso en los meses de julio y agosto, las horas sobre e<br>límite no superan el 1% de las horas totales anuales, considerando los receptores más<br>cercanos. Dado lo anterior se considera que solo pudiese haber superación solo en<br>eventos intermitentes, menor al 1% de las horas anuales.|
|Ofensividad|Considerando que las concentraciones en receptores no superan el límite del umbral<br>de molestia de 3 OUE/m3, se puede concluir que, la combinación entre frecuencia,<br>intensidad y duración no representan ofensividad, considerando los 15 receptores<br>discretos definidos.|
|Localización|El proyecto se emplaza en la comuna de Curicó, región del Maule, a unos 7 km del<br>centro de la ciudad, en Zona Urbana Mixta según Plan Regulador Comunal.|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 28 de 50

**5.6.3 Dispersión de emisiones de olor. Escenario Futuro.**

Tal como se puede apreciar en la siguiente cartografía, las isodoras visualizadas en la siguiente
cartografía del Escenario Futuro, presentan valores de 0,1 a 2,28 OU E /m [3] alcanzando su mayor
concentración dentro de los deslindes de planta. Fuera de los límites de la planta las isodoras
trazan valores menores al límite de detección de 1,0 OU E /m [3], valor que también define el área
de influencia.

**Figura No 10** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio

horario, percentil 98. Escenario Futuro.

**5.6.4 Punto Máxima concentración de olor. Escenario Futuro.**

En función de la dispersión de olor, se determina el punto de máxima concentración, el cual, al
igual que el escenario actual, se posiciona dentro del deslinde de planta, en la zona de losa de
residuos, a un costado de los contenedores de residuos, alcanzando una concentración de 2,28
OU E /m [3] . Detalle de concentración y coordenadas a continuación.

**Tabla No 19.** Punto máxima concentración para percentil 98. Coordenadas UTM 19S.

Escenario Futuro.

|Concentración (OU /m3)<br>E|Coordenada Este (m)|Coordenada Norte (m)|
|---|---|---|
|2,28|296.980|6.123.841|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 29 de 50

**5.6.5 Área de Influencia. Escenario Futuro.**

Con base en la dispersión de emisiones del escenario evaluado, se determinó un área de
influencia definida según la “Guía para la predicción y evaluación de impactos por olor en el
SEIA” [9], como el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de
detección del olor compuesto, es decir, es la concentración en donde el 50% de la población
puede percibir un olor.

A continuación, se observa el mapa con el emplazamiento de área de influencia circunscrita por
el límite de isoconcentración de 1 OU E /m [3] .

**Figura No 11.** Mapa del Área de Influencia (AI), definida por 1 OU E /m [3] . Escenario Futuro.

La isodora de 1 OU E /m3, valor que indica la concentración desde el cual el 50% de la población
puede percibir un olor, cubre una superficie de **2.174 m** **[2]** . La distribución de la pluma se acentúa
en sentido norte-sur, manteniendo una longitud aproximada de 68 metros. Dicha área de
influencia no circunscribe a ninguno de los 15 receptores discretos considerados en la
evaluación.

9 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 30 de 50

**5.6.1 Concentración en Receptores. Escenario Futuro.**

En la siguiente tabla, se presenta el resultado del Percentil 98, de las concentraciones horarias
para cada receptor discreto considerado en la modelación. Tal como se puede apreciar en la
tabla, la operación actual de planta produce concentraciones de inmisión que se encuentran
bajo el límite de referencia establecido en la normativa colombiana (3,0 OU E /m [3] ). La mayor
concentración se observa en el receptor 12 (Receptor Copeval) que alcanza un valor de 0,27
OU E /m [3], concentración que se encuentran bajo el límite de detección (1,0 OU E /m [3] ) y de molestia
(3,0 OU E /m [3] ) establecido en la normativa de referencia.

**Tabla No 20** . Concentración receptores, percentil 98 . Escenario Futuro.

|ID|Descripción|Concentración de<br>inmisión (OU /m3)<br>E|Límite inmisión<br>(Norma colombiana)|
|---|---|---|---|
|R1|Vivienda Lote 1|0,10|**3,0**<br>**OUE/m3 **<br>**(percentil 98)**|
|R2|Vivienda Lote 2|0,09|0,09|
|R3|Vivienda Lote 3|0,06|0,06|
|R4|Vivienda Lote 4|0,07|0,07|
|R5|Vivienda Lote 5|0,03|0,03|
|R6|Vivienda Lote 6|0,01|0,01|
|R7|Vivienda Lote 7|0,01|0,01|
|R8|Vivienda Lote 8|0,07|0,07|
|R9|Vivienda Lote 9|0,08|0,08|
|R10|Vivienda Lote 10|0,08|0,08|
|R11|Vivienda Lote 11|0,08|0,08|
|R12|Receptor Copeval|0,27|0,27|
|R13|Vivienda Lote 13|0,07|0,07|
|R14|Vivienda Lote 14|0,07|0,07|
|R15|Vivienda Lote 15|0,08|0,08|

En el Anexo N°2 se presenta el análisis de la variación horaria de olor, en el receptor discreto
que presenta la mayor concentración de olor.

.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 31 de 50

**5.6.2 Protocolo FIDOL. Escenario Futuro.**

Conforme a lo estipulado por la “Guía para la predicción y evaluación de impactos por olor en el
SEIA”, se evalúa la significancia de la inmisión de olor en los receptores establecidos mediante
el Protocolo FIDOL, que habla sobre:

 Frecuencia: referido a la frecuencia que la o las personas están expuestas al olor.

 Intensidad: referido a la percepción de la fuerza del olor.

 Duración: referido al tiempo de un episodio de olor.

 - Ofensividad: referido a la caracterización del olor.

 Localización: referido al tipo de uso del suelo y la naturaleza de las actividades aledañas
a una fuente de olor. Se puede considerar que el factor “localización” abarca las
características del receptor como su sensibilidad, vulnerabilidad y otros.

A continuación, se desglosan los puntos mencionados:

**Tabla No 21** . Protocolo FIDOL. Escenario Futuro.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia<br>>3 OUe/m3|Planta COMFRUT 10 meses del año, con un receso en los meses de julio y agosto. Sin<br>embargo, durante el 98% de las horas del año no se prevé superación de 1 OUE/m3 <br>(umbral de detección) y 3 OUE/m3 (umbral de molestia). Por lo tanto, no se prevé<br>afectación en términos de frecuencia.|
|Intensidad|Ningún receptor se encuentra sobre las 3 OUE/m3 en el percentil 98, de la normativa de<br>referencia (concentración que representa el umbral de molestia). Dado que los resultados<br>en los receptores son menores a 3 OUE/m3, no se prevé afectación en términos de<br>intensidad en los 15 receptores considerados en la modelación.|
|Duración|En cuanto a la duración, pese a que la proyecto contempla una operación constante en<br>10 meses del año, con un receso en los meses de julio y agosto, las horas sobre e límite<br>no superan el 1% de las horas totales anuales, considerando los receptores más<br>cercanos. Dado lo anterior se considera que solo pudiese haber superación solo en<br>eventos intermitentes, menor al 1% de las horas anuales.|
|Ofensividad|Considerando que las concentraciones en receptores no superan el límite del umbral de<br>molestia de 3 OUE/m3, se puede concluir que, la combinación entre frecuencia, intensidad<br>y duración no representan ofensividad, considerando los 15 receptores discretos<br>definidos.|
|Localización|El proyecto se emplaza en la comuna de Curicó, región del Maule, a unos 7 km del centro<br>de la ciudad, en Zona Urbana Mixta según Plan Regulador Comunal.|

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 32 de 50

**Análisis del desempeño del archivo de pronóstico utilizado**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para ello
se utilizan los datos disponibles de las estaciones de monitoreo ubicadas en la zona de interés
para el estudio.

La estación utilizada corresponde a Curicó, del sistema SINCA, a 3,66 km de la Planta
COMFRUT. Esta estación presenta datos de temperatura, dirección y velocidad de viento, las
cuales serán utilizadas para validar el modelo meteorológico de pronóstico WRF, no siendo

usadas como entradas al modelo.

En el Anexo N°3 se presentan las variables meteorológicas y geofísicas del emplazamiento del
proyecto y en el Anexo No4 se presenta una comparación cualitativa y cuantitativa entre la
meteorología de pronóstico y los datos observados en la estación meteorológica Curicó.

De acuerdo con las comparaciones realizadas en forma cualitativa de ciclo diario, promedio
mensual rosa de los vientos y ciclos estacionales, para los parámetros temperatura, velocidad y
dirección de viento para la estación de Curicó se puede indicar que tanto el modelo WRF y los
datos observados presentan valores y patrones similares, que permiten indicar que los datos
WRF se ajustan a la realidad y pueden ser utilizados en la modelación.

**Figura No 12** . Estación Meteorológica utilizada en el Análisis de Incertidumbre.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 33 de 50

**6** **Conclusiones**

De acuerdo al estudio de estimación y evaluación de la dispersión de las fuentes de olores, se
concluye lo siguiente:

1. La mayor emisión se presenta en el Área de Riego con 232 OU E /s en el escenario Actual

y 232 OU E /s en el escenario Futuro. Esto debido a que en el escenario Futuro la dimensión
de la zona de riego disminuye debido a la incorporación de un tranque de acumulación
adicional.

2. Las curvas de isoconcentración del percentil 98, indican que las concentraciones de olor,

tanto para el escenario actual como futuro, presentan un punto de máxima concentración,
presente dentro de los deslindes de planta, con un valor de 2,28 OU E /m [3] .

3. En cuanto al Área de influencia, definida por el límite de 1,0 OU E /m [3], presenta una

superficie de 2.152 m [2] para el escenario Actual y 2.174 m [2] para el escenario Futuro.

4. Ambos escenarios evaluados no presentan superación del límite de 3 OU E /m [3] (percentil

98), en ninguno de los receptores identificados (15). El receptor que presenta la
concentración más alta (R12) fue identificado como Receptor Copeval, ubicado al norte
de planta con una concentración de 0,27 OU E /m [3], en ambos escenarios.

5. De acuerdo a las comparaciones realizadas al ciclo diario, al promedio mensual de los

vientos y ciclos estacionales, y estadística para los parámetros temperatura, velocidad y
dirección de viento para la estación Curicó, se puede indicar que, tanto el modelo WRF
como los datos reales observados, presentan valores y patrones similares. Lo anterior
permite concluir que los datos WRF se ajustan a la realidad y, en consecuencia, al ser
utilizados en la modelación arrojan resultados técnicamente válidos.

6. Todos los resultados presentes en este informe son válidos sólo para las condiciones y

consideraciones estipuladas en el presente informe.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 34 de 50

**7** **Anexos**

**Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación**

El siguiente Anexo presente el archivo magnético el cual contiene la información que se utilizó
para realizar la modelación atmosférica, dicha información corresponde a la los input y output
ingresados para la modelación de los módulos del modelo (CALPUFF, CALPOST y CALRANK)
y el archivo Meteorológico WRF.

Por lo tanto, en el caso de que se requiera replicar la modelación realizada, esta se podrá hacer
utilizando los archivos presentes en este Anexo.

- **NOTA. Los antecedentes serán entregados al titular en formato digital, debido al tamaño**
**de los archivos.**

**Figura No 13** . Esquema funcionamiento CALPUFF.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 35 de 50

**Anexo No2. Análisis de receptores**

A continuación, se presentan los gráficos ciclo diario de las concentraciones de olor, para el
receptor que presenta la concentración más alta (R12). Estos gráficos permiten detectar las horas
en donde ocurren las mayores concentraciones durante el día, respecto al 90% observado del
tiempo (variación entre el percentil 5 y percentil 95). Los resultados de la modelación y el análisis
en los dos receptores indican que ninguno de ellos está por sobre el límite de inmisión de 3
OU E /m [3] .

**Escenario Actual.**

**Figura No 14** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No12.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor
durante el día. Se puede observar que los mayores valores se presentan durante la
madrugada, entre las 00:00 a 05:00 hrs. con valores de hasta 0,34 OU E /m3 en el rango

del 90% observado .

**Escenario Futuro.**

**Figura No 15** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No12.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor
durante el día. Se puede observar que los mayores valores se presentan durante la
madrugada, entre las 00:00 a 05:00 hrs. con valores de hasta 0,34 OU E /m3 en el rango

del 90% observado .

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 36 de 50

**Anexo No3. Descripción meteorológica y geofísica de la zona**

En el siguiente anexo se presenta el análisis de la meteorología de la zona modelada. Los datos
expresados a continuación fueron extraídos por la plataforma SINCA (Sistema de información
nacional de calidad del aire), correspondiente a la estación de monitoreo Curicó.

**Tabla No 22.** Datos estaciones meteorológicas consideradas.

|Estación Meteorológica|Col2|EM Curicó|
|---|---|---|
|Coordenada UTM Datum WGS 84|Zona|19S|
|Coordenada UTM Datum WGS 84|Este (m)|296.068|
|Coordenada UTM Datum WGS 84|Norte (m)|6.127.456|
|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|01/01/2021 - hasta 31/12/2021|
|Distancia desde Planta (km)|Distancia desde Planta (km)|3,66|
|Meteorología|Meteorología|Velocidad Viento (VV)<br>Dirección de Viento (DV)<br>Temperatura (T)|

**7.3.1 Cantidad de datos**

Para realizar el análisis meteorológico y el análisis de incertidumbre es necesario verificar la
cantidad de datos presentes en las mediciones ambientales de las estaciones. A continuación,
se muestran los datos de las estaciones en la serie de tiempo para comprobar que no existen
periodos extensos sin datos durante el año de análisis.

**Estación Curicó.**

**Figura No 16.** Serie de tiempo velocidad de viento - datos observados estación Curicó- año

2021.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 37 de 50

**Figura No 17.** Serie de tiempo dirección de viento - datos observados estación Curicó - año

2021.

**Figura No 18.** Serie de tiempo temperatura - datos observados estación Curicó - año 2021.

**Tabla No 23.** Datos válidos estación meteorológica Curicó.

|Porcentaje de datos meteorológicos disponibles - EM Curicó|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Pará/mes|E|F|M|A|M|J|J|A|S|O|N|D|**Total**|
|VV|98%|100%|99%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|DV|98%|100%|99%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|T|98%|100%|99%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|

La estación Curicó posee una cantidad de datos mínima de un 98% para las variables
temperatura, dirección y velocidad del viento durante el mes de diciembre. El total de datos
anuales es de un 100%, lo que es superior al 75% sugerido por la Guía para modelos de calidad
del aire del SEA.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 38 de 50

**7.3.2 Gráficos Ciclo diario**

Velocidad de viento

En los siguientes gráficos se presenta los ciclos diarios promedios de temperatura, velocidad y
dirección del viento; junto con su variabilidad entre el percentil 5% a 95% (Rango 90%
observado).

**Figura No 19.** Ciclo diario para velocidad de viento Estación Curicó.

En relación al ciclo diario promedio de la velocidad de viento, de la estación Curicó, se observa
una velocidad promedio mínima de 1,0 m/s desde las 23:00 a las 02:00 hrs. Durante el año, la
velocidad del viento puede variar entre calmas y 3,61 m/s en el rango de 90% observado.

Temperatura

**Figura No 20.** Ciclo diario para temperatura estación Curicó.
Respecto a la temperatura, se alcanzan máximas promedio de 22°C a las 15:00 y 16:00 hrs. y
mínimas de 10°C entre las 04:00 y 06:00 hrs. El rango del 90% observado varía de los 2 a los
32°C con diferencias de hasta 23°C respecto al promedio.

Dirección de viento

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 39 de 50

**Figura No 21.** Ciclo diario para dirección de viento estación Curicó.

En relación al ciclo diario de la dirección de viento de la estación Curicó, se observa que durante
horarios de tarde predominan los vientos provenientes desde el sur y suroeste; dicha condición
indica que los gases se dispersan hacia el norte y noreste. En cuanto a horas de la noche,
madrugada y parte de la mañana la dirección del viento proviene del suroeste y en menor medida

del noreste.

**7.3.3 Gráfico Distribución de Viento**

La siguiente figura muestra la distribución de vientos en la estación: Curicó. De acá se puede
concluir que la mayor parte del tiempo, los vientos presentan una velocidad que va entre 0,5 y
2,1 m/s, lo que representa un 68,9% de la frecuencia, mientras que en menor proporción se
registran vientos con velocidades de 2,1 y 3,6 m/s, representando un 19,4%.

**Figura No 22.** Distribución velocidades de viento estación Curicó.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 40 de 50

**7.3.4 Rosa de los vientos**

De las rosas de los vientos anual realizada para la estación Curicó, se puede concluir que el
viento predominante proviene desde el sur y suroeste, alcanzando una frecuencia de un 31% en
los datos observados en la estación Curicó. Es importante señalar que, se alcanza una velocidad
que va de 0,5 a 5,7 m/s. Los vientos calmos (<0,5 m/s) representan el 10,11% de la frecuencia
total.

**Figura No 23.** Rosa de los vientos Anual. Datos observados Estación Curicó.

**Por estación**

En los gráficos siguientes se muestra una comparación de las rosas de los vientos para cada
estación del año.

En otoño e invierno los vientos en la Estación Curicó provienen principalmente desde el sur
y suroeste con velocidades entre los 0,5 y 3,6 m/s mientras que en menor proporción se
observan vientos provenientes desde el noreste, con velocidades de 0,5 a 3,6 m/s en otoño
y 0,5 a 5,7 m/s en invierno.

- En primavera los vientos provienen principalmente del suroeste, seguido del sur, con
velocidades de los 0,5 a 3,6 m/s y 0,5 a 5,7 m/s, respectivamente. En verano los vientos
provienen principalmente desde el sur, suroeste y oeste en frecuencias muy similares con
velocidades de los 0,5 a 5,7 m/s.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 41 de 50

En los siguientes gráficos se muestran las rosas de los vientos para cada estación del año.

|(a) Otoño - EM Curicó 2021.|(b) Invierno - EM Curicó 2021.|
|---|---|
|(c) Primavera - EM Curicó 2021.|(d) Verano - EM Curicó 2021.|

**Figura No 24.** Rosa de los vientos por estación del año.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 42 de 50

**7.3.5 Gráfico ciclo estacional**

En la siguiente figura, se observa la variación estacional de los ciclos de velocidad y dirección de
viento.

En relación a la dirección de viento en la estación Curicó el ciclo diario se mantiene con vientos

principalmente desde el sur y suroeste durante la mayor parte del año, a excepción de invierno
donde se observan vientos provenientes desde el este en horarios de noche, madrugada y parte
de la mañana. Lo anterior indica que, durante la mayor parte del año, la dispersión de gases se
dirige hacia el norte y noreste, mientras que en invierno se dirige hacia el noreste sólo en horarios
de tarde.

En cuanto a la velocidad del viento, horas de la tarde se presentan las mayores velocidades que
pueden llegar hasta los 3,0 a 3,5 m/s en verano y los 2,0 a 2,5 m/s en invierno.

Durante horarios de noche, madrugada y parte de la mañana, tanto en meses de otoño e invierno
y primavera y verano, los vientos alcanzan velocidades de hasta 1,5 m/s aproximadamente.

**Figura No 25.** Ciclos estacionales - datos observados estación Curicó - Año 2021. [10]

10 Las flechas indican hacia donde se dirige el viento.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 43 de 50

**7.3.6 Elevación de Terreno**

La zona modelada corresponde a un sector ubicado al sureste de la comuna de Curicó, provincia
de Curicó, región del Maule, en la zona central, la que se encuentra rodeada por un cordón de
cerros hacia el este, alcanzando elevaciones de hasta 1.500 m.s.n.m., sin embargo, la planta
COMFRUT Curicó se encuentra emplazada entre 200 y 300 m.s.n.m.

**Figura No 26.** Elevación de terreno archivo WRF.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 44 de 50

**Anexo No4. Análisis incertidumbre**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA” en su capítulo 7 requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para ello
se utilizan los datos disponibles en las estaciones de monitoreo ubicadas en la zona de interés
para el estudio.

La estación de monitoreo analizada corresponde a Curicó, ubicada a 3,66 km hacia el suroeste
de la planta. Los parámetros monitoreados por dicha estación corresponden a temperatura,
velocidad y dirección de viento. Para la evaluación del desempeño se realiza una comparación
entre dichas variables, por ser consideradas las variables de mayor interés.

Con el fin de evaluar el desempeño, se realiza un análisis cualitativo de los parámetros de interés,
el que se desarrolla mediante la comparación entre los ciclos diarios promedios, mensuales,
ciclos estacionales y rosas de los vientos.

Definiciones

**Datos observados:** Se refiere a los datos provenientes desde una estación de monitoreo
durante un periodo de interés.

**Datos modelados:** Se refiere a los datos meteorológicos provenientes desde un modelo de
pronóstico como WRF o MM5.

**Rango 90% observado:** Se refiere a la variación de los datos entre el percentil 5 y percentil 95
en una hora o mes específico.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 45 de 50

**7.4.1 Ciclos Diarios promedios**

Velocidad de viento

**Figura No 27.** Comparación ciclo diario de velocidad de viento entre datos observados y

proyectados para la estación de Curicó.

Para el gráfico de velocidad de viento del ciclo diario se observa que los datos modelados están
sobrestimados respecto a los observados. En horarios de tarde se observa una diferencia
máxima de 1,6 m/s a las 18:00 hrs. En horarios de mañana esta diferencia disminuye, llegando
a presentarse la misma temperatura para ambos datos a las 08:00 y 09:00 hrs.

Dirección de Viento

**Figura No 28.** Comparación ciclo diario de dirección de viento entre datos observados y

proyectados para la estación de Curicó.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 46 de 50

De la figura anterior se puede concluir que la moda diaria de dirección del viento entre los datos
observados y los datos modelados presentan valores y patrones similares observándose una
dirección de viento proveniente principalmente del sur en horarios de madrugada y mañana y del
suroeste en horarios de tarde.

**Figura No 29.** Comparación ciclo diario de dirección de viento entre datos observados y

proyectados para la estación de Curicó.

Respecto a la temperatura se puede observar que no existen grandes diferencias entre los datos
modelados y los datos observados. Los datos modelados están sobrestimados respecto a los
observados puntualmente en parte de la mañana y tarde.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 47 de 50

**7.4.2 Promedio Mensual**

Velocidad de viento

**Figura No 30.** Comparación moda mensual de velocidad de viento entre datos observados y

proyectados para la estación de Curicó.

De la figura anterior se puede concluir que el promedio mensual de velocidad de viento entre los
datos observados y los datos modelados presentan valores similares con una diferencia máxima
de ±1 m/s para la estación de Curicó en el mes de mayo, observándose una sobreestimación en
los datos modelados en comparación a los observados. La variación mensual de velocidad posee
el mismo patrón del modelo de pronóstico y el observado.

Dirección de Viento

**Figura No 31.** Comparación moda mensual de dirección de viento entre datos observados y

proyectados para la estación de Curicó.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 48 de 50

De la figura anterior se puede concluir que la moda mensual de dirección del viento entre los
datos observados y los datos modelados los mismos valores todo el año. En los meses de enero,
febrero, marzo y diciembre se observa una dirección de viento proveniente del suroeste, mientras
que el resto del año se mantiene principalmente en dirección oeste.

**Figura No 32.** Comparación moda mensual de dirección de viento entre datos observados y

proyectados para la estación de Curicó.

De la figura anterior se puede concluir que la moda mensual de temperatura entre los datos
observados y los datos modelados presentan una tendencia similar durante todo el año,
observándose una sobreestimación puntual más significativa de ±3°C en el mes de julio. Dadas
estas circunstancias, respecto a la moda mensual de dirección de viento, el modelo es adecuado.

**7.4.3 Dirección de viento**

Rosa de los vientos

**Figura No 33.** Comparación Rosas de viento.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 49 de 50

De las rosas de los vientos anual realizada para la estación Curicó, se puede concluir que el
viento predominante proviene desde el sur y suroeste, tanto para los datos observados como los
datos modelados. Sin embargo, los datos modelados presentan una frecuencia mucho mayor en
dirección suroeste, de aproximadamente un 38% vs. Una frecuencia de 20% en los datos
observados. Además, en los datos modelados se observan mayores frecuencias de velocidades
más altas, alcanzando 8,8 m/s, mientras que los datos observados alcanzan velocidades de 5,7
m/s.

**Análisis cuantitativo**

De acuerdo a lo solicitado por la Guía para uso de modelos de calidad del aire en el SEIA, se
presenta el análisis cuantitativo de las variables meteorológicas involucradas en la modelación.
En el análisis se incluye las variables temperatura, dirección y velocidad de viento, con las
métricas solicitadas: RMSE, BIAS e IOA.

**Tabla No 24.** Análisis cuantitativo.

|Parámetro|Métrica|Catemu|Col4|
|---|---|---|---|
|**Parámetro**|**Métrica**|**Horario**|**Diario**|
|**Velocidad del viento (m/s)**|** RMSE**|1,40|0,97|
|**Velocidad del viento (m/s)**|**BIAS**|0,80|0,80|
|**Temperatura (°C)**|**BIAS**|0,47|0,47|
|**Temperatura (°C)**|**RMSE**|2,96|2,28|

Los resultados anteriores son comunes en archivos meteorológicos WRF. Se puede concluir que
los datos del modelo de pronóstico se asemejan a los datos observados, y puede ser usado en
la modelación.

Inf01E01.O-22-056. Estimación y Modelación de olores - COMFRUT.docx 50 de 50