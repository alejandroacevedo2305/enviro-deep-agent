---
title: Sin título
author: Users-Pre-Installed
date: D:20250213161955-03'00'
language: es
type: report
pages: 52
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME
-->

# INFORME

## Evaluación de la dispersión de emisiones de olores

### Piscicultura San Pablo

Desarrollos Acuícolas San Pablo

**Diciembre del 2024**

**Inf01E01.O-24-133.**

Anexo F Estimación y Modelación de Olores 1 de 52

#### Datos del Proyecto

**Empresa** : Desarrollos Acuícolas San Pablo.

**Planta** : Piscicultura San Pablo.

**Coordinador** : Pamela Valenzuela.

**Gerente de Ing. en olores** : Miguel Gatica Rivera (MGR).

**Jefe de Proyectos** : Felipe Sánchez Mella (FSM).

**Fecha** : 18 de diciembre del 2024.

|Emisión|Datos|Preparó|Revisó|Aprobó|
|---|---|---|---|---|
|Rev A. Para<br>Revisión<br>cliente.|Nombre|FSM|MGR|MGR|
|Rev A. Para<br>Revisión<br>cliente.|Fecha|25-10-2024|25-10-2024|25-10-2024|

Anexo F Estimación y Modelación de Olores 2 de 52

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

4.3.4 Evaluación de los resultados .......................................................................................... 16

4.3.5 Área de Influencia y receptores de interés. .................................................................... 17

Evaluación del desempeño del archivo de pronóstico utilizado ................................... 17
**5** **Resultados ....................................................................................................................... 18**

Caracterización de las fuentes de emisión .................................................................. 18

Ubicación de fuentes .................................................................................................. 19

Factores de emisión utilizados .................................................................................... 20

Emisiones de olores ................................................................................................... 22

Evaluación de la dispersión de olores ......................................................................... 24

5.5.1 Dispersión de emisiones de olor. ................................................................................... 24

5.5.2 Punto Máxima concentración de olor ............................................................................. 25

5.5.3 Área de Influencia........................................................................................................... 26

Análisis del desempeño del archivo de pronóstico utilizado ........................................ 32
**6** **Conclusiones ................................................................................................................... 33**

**7** **Anexos ............................................................................................................................. 34**

Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación ............ 34
Anexo No2. Análisis de receptores .............................................................................. 35
Anexo No3: Descripción meteorológica y geofísica de la zona (EM La Unión) ............ 36

7.3.1 Cantidad de Datos .......................................................................................................... 36

7.3.2 Gráficos Ciclo diario ....................................................................................................... 38

7.3.3 Gráficos Distribución de Vientos .................................................................................... 40

7.3.4 Rosa de los Vientos........................................................................................................ 41

7.3.5 Ciclo estacional .............................................................................................................. 43

7.3.6 Elevación de Terreno ..................................................................................................... 44

Anexo No4. Análisis de incertidumbre. Comparación entre la meteorología de pronóstico
y los datos observados en la estación meteorológica (EM La Unión). ............................... 46

Anexo F Estimación y Modelación de Olores 3 de 52

7.4.1 Ciclos diarios promedios ................................................................................................ 46

7.4.2 Promedio Mensual.......................................................................................................... 48

7.4.3 Rosas de los vientos ...................................................................................................... 51

7.4.4 Análisis Cuantitativo ....................................................................................................... 52

**Índice de Tabla**

**Tabla No 1.** Factores de emisión a utilizar en proyecto en cuestión. ........................................................... 6
**Tabla No 2** . Emisión asociada a cada fuente. ............................................................................................... 7
**Tabla No 3** . Concentración receptores. Percentil 98. ................................................................................... 9
**Tabla No 4.** Variables de entrada consideradas en la modelación ............................................................. 13
**Tabla No 5** . Configuración de grilla. ............................................................................................................ 14
**Tabla No 6.** Características del archivo meteorológico WRF. .................................................................... 15
**Tabla No 7** . Descripción fuentes y procesos asociados. ............................................................................ 18
**Tabla No 8.** Coordenadas de fuentes de emisión odorantes. ..................................................................... 19

**Tabla No 9.** Factores de emisión Guía Holandesa. .................................................................................... 20
**Tabla No 10.** Factores de emisión para proyectos aprobados de Pisciculturas. ........................................ 20
**Tabla No 11.** Factores de emisión a utilizar en proyecto en cuestión. ....................................................... 21
**Tabla No 12** . Justificación de áreas efectivas de emisión. ......................................................................... 22
**Tabla No 13** . Factores de emisión y emisión asociada a cada fuente. ....................................................... 23
**Tabla No 14.** Punto máximo impacto para percentil 98. Coordenadas UTM 18S. ..................................... 25
**Tabla No 15** . Receptores discretos considerados en la modelación. ......................................................... 27
**Tabla No 16** . Concentración receptores. Escenario Actual, percentil 98. .................................................. 29
**Tabla No 17** . Protocolo FIDOL. ................................................................................................................... 31
**Tabla No 18** . Estaciones meteorológicas. ................................................................................................... 36
**Tabla No 19.** Datos válidos estación meteorológica La Unión. .................................................................. 37
**Tabla No 20.** Análisis cuantitativo. .............................................................................................................. 52

**Índice de Figura**

**Figura No 1** . Mapa de concentración de olor generado por las fuentes de emisión de la planta (Percentil
98). ................................................................................................................................................................ 8
**Figura No 2** . Mapa ubicación del proyecto. ................................................................................................ 10
**Figura No 3** . Esquema resumen de las metodologías para estimar las emisiones de olor. ...................... 12
**Figura No 4** . Visualización de distribución de grillas de modelación. ......................................................... 14
**Figura No 5** . Ubicación espacial de las fuentes generadoras de olor del proyecto. .................................. 19
**Figura No 6** . Distribución porcentual de Emisiones. ................................................................................... 23
**Figura No 7** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio horario,
percentil 98. ................................................................................................................................................. 25
**Figura No 8.** Mapa del Área de Influencia (AI), definida por 1 OU E /m [3] . ..................................................... 26
**Figura No 9** . Receptores discretos considerados en la modelación. ......................................................... 28
**Figura No 10** . Mapa de horas sobre 3,0 OU E /m3 generado por las fuentes de emisión de la Piscicultura
San Pablo, promedio horario (percentil 98). ............................................................................................... 30
**Figura No 11** . Estaciones Meteorológicas utilizada en el Análisis de Incertidumbre. ................................ 32
**Figura No 12** . Esquema funcionamiento CALPUFF. .................................................................................. 34
**Figura No 13** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No4. .......................... 35
**Figura No 14** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No16. ........................ 35
**Figura No 15** . Serie de tiempo velocidad de viento - datos observados estación La Unión - Año 2022. . 36
**Figura No 16** . Serie de tiempo dirección de viento - datos observados estación La Unión - Año 2022. .. 37

Anexo F Estimación y Modelación de Olores 4 de 52

**Figura No 17** . Serie de tiempo temperatura - datos observados estación La Unión - Año 2022. ............ 37
**Figura No 18** . Ciclo diario velocidad viento - datos observados estación La Unión - Año 2022. ............. 38
**Figura No 19** . Ciclo diario dirección viento - datos observados estación La Unión - Año 2022. .............. 39
**Figura No 20** . Ciclo diario temperatura - datos observados estación La Unión - Año 2022. .................... 39
**Figura No 21** . Distribución de vientos - datos observados estación La Unión - Año 2022. ...................... 40
**Figura No 22** . Rosa de los vientos - datos observados estación La Unión - Año 2022............................ 41
**Figura No 23** . Rosa de los vientos por estación del año. ........................................................................... 42
**Figura No 24** . Ciclos estacionales - datos observados estación La Unión - Año 2022. ........................... 44
**Figura No 25** . Elevación de terreno archivo WRF. ..................................................................................... 45
**Figura No 26** . Comparación ciclo diario de velocidad de viento entre los datos observados y proyectados
para la estación La Unión. .......................................................................................................................... 47
**Figura No 27** . Ciclo diario de dirección de viento datos observados para la estación La Unión. .............. 47
**Figura No 28.** Comparación ciclo diario de temperatura entre los datos observados y proyectados para la
estación La Unión. ...................................................................................................................................... 48
**Figura No 29.** Comparación ciclo mensual de velocidad de viento entre los datos observados y
proyectados para la estación La Unión. ...................................................................................................... 49
**Figura No 30.** Comparación ciclo mensual de dirección de viento entre los datos observados y
proyectados para la estación La Unión. ...................................................................................................... 50
**Figura No 31.** Comparación ciclo mensual de temperatura entre los datos observados y proyectados para
la estación La Unión. ................................................................................................................................... 51
**Figura No 32.** Comparación rosa de los vientos entre los datos observados y proyectados para la
estación La Unión. ...................................................................................................................................... 51

Anexo F Estimación y Modelación de Olores 5 de 52

**1** **Resumen**

Desarrollos acuícolas San Pablo, en base al proyecto centro de cultivo “Piscicultura San Pablo”,
solicitó los servicios de Proterm S.A. con el objetivo de evaluar la futura dispersión de olores
provenientes de las principales fuentes. Tales fuentes consideradas corresponden Sistema de
Tratamiento del Efluente (específicamente en el Sistema de rotofiltros y Manejo de lodos), Silo
de mortalidad y PTAS (planta de tratamiento de aguas servidas).

El objetivo del presente informe es evaluar el comportamiento y efecto de las emisiones de olor
del proyecto sobre la salud de la población cercana, sistema de vida y costumbres, población
protegida, y turismo. Lo anterior acorde al artículo 11 de la Ley N°19.300 y la Guía para la
predicción y evaluación de impactos por olor en el SEIA.

Con respecto a la metodología y bajo el contexto de que hoy en día no contamos con factores
de emisión provenientes de fuentes medidas con características similares a las presentes en el
proyecto en cuestión, se decide utilizar aquellos factores de emisión de proyectos aprobados,
con los valores más altos, con el objetivo de evaluar el peor escenario, tal como establece la
“Guía para la predicción y evaluación de impactos por olor en el SEIA”, para proyectos que aún
no se encuentran en ejecución. A continuación, tabla resumen de factores de emisión utilizados
para las fuentes a evaluar en proyecto en cuestión.

**Tabla No 1.** Factores de emisión a utilizar en proyecto en cuestión.

|Fuente|Col2|Factor de Emisión<br>(OU /m2s)<br>E|Referencia|
|---|---|---|---|
|Sistema de<br>Tratamiento del<br>Efluente|Sistema de<br>Rotofiltros|**7,5**|Modernización y Aumento de<br>Producción en Piscicultura Quillaico<br>(2021)|
|Sistema de<br>Tratamiento del<br>Efluente|Manejo de<br>Lodos|**8,0**|**8,0**|
|Silo de Mortalidad|Silo de Mortalidad|**26,3**|Modificación Proyecto Técnico y<br>Mejoramiento Piscicultura Trafún<br>(2020)|
|PTAS|PTAS|**1,75**|Piscicultura de Recirculación Los<br>Arrayanes - Componente Olores<br>(2018)|

De acuerdo con la aplicación de los factores de emisión, provenientes principalmente de
proyectos aprobados ingresados en él SEA, se obtuvo que la mayor fuente de emisión de olor
corresponde al Sistema de rotofiltros con 3.990 OU E /s, seguido por el Silo de mortalidad con 434
OU E /s, tal como muestra la siguiente tabla.

Anexo F Estimación y Modelación de Olores 6 de 52

**Tabla No 2** . Emisión asociada a cada fuente.

|Fuente|Col2|Dimensiones|Col4|Col5|Factor de<br>emisión<br>(OU /m2s)<br>E|Emisión<br>de olor<br>(OU /s)1<br>E|
|---|---|---|---|---|---|---|
|**Fuente**|**Fuente**|**Área Efectiva**<br>**de emisión**<br>**(m2) **|**Cantidad**|**Área Total**<br>**Efectiva**<br>**(m2)**|**Área Total**<br>**Efectiva**<br>**(m2)**|**Área Total**<br>**Efectiva**<br>**(m2)**|
|Sistema<br>de<br>Tratamiento<br>del Efluente|Sistema de<br>Rotofiltros|266|22|**532**|**7,5**|**3.990**|
|Sistema<br>de<br>Tratamiento<br>del Efluente|Manejo de<br>Lodos|0,64|4|**2,6**|**8,0**|**21**|
|Silo de Mortalidad|Silo de Mortalidad|9,363|1|**9,36**|**26,3**|**246**|
|PTAS|PTAS|3,0|1|**3,0**|**1,75**|**5,3**|

Una vez obtenidas las emisiones de olor de cada fuente, se ingresaron al modelo de dispersión
atmosférica calpuff, el cual permitió conocer la concentración y dispersión de los olores, tanto en
el área de estudio como en los receptores discretos cercanos al proyecto, los cuales
corresponden principalmente a viviendas cercanas a la piscicultura y fundos.

Debido a que en Chile no existe normativa que regule la emisión ni la inmisión de olores por parte
de una planta de estas características, se utiliza como referencia, normativas internacionales. Es
por esto que las concentraciones de olor (OU E /m [3] ) resultantes del modelo, para cada receptor
discreto, fueron comparados con el límite de inmisión establecido en la normativa de Colombia.
En esta normativa establece un límite de inmisión de 3,0 OU E /m [3] para percentil 98, que aplica a
la contaminación de olor generada en el procesamiento y conservación de carne, pescado,
crustáceos y moluscos. Se señala que este valor límite se ha utilizado en diferentes proyectos
del rubro pesquero evaluados en el SEA.

La dispersión de las emisiones de olor de la piscicultura indica que el área de influencia cubre un
área total de 122 ha, con una longitud aproximada de 1,47 km en dirección noreste y suroeste.
El área de influencia corresponde a la superficie circunscrita por 1 OU E /m [3], establecida en la
“Guía para la predicción y evaluación de impactos por olor en SEIA” del año 2017, concentración
que indica que el 50% de la población puede comenzar a detectar un olor.

Las isodoras pueden alcanzar valores entre 1,0 a 22,5 OU E /m [3] alcanzando su mayor
concentración en el sistema de tratamiento de efluentes, específicamente al costado Este de los
rotofiltros. Fuera de los límites de la planta las isodoras trazan valores entre 1,0 a 3,0 OU E /m [3],
abarcando un área total de 122 ha para la isodora de 1,0 OU E /m [3] .

1 Las emisiones de olores de las fuentes consideradas en la modelación, se incorporaron asumiendo un periodo de
funcionamiento anual constante, representando de esta manera, el escenario más desfavorable que se pudiese

generar.
2 Se consideran 2, ya que se contemplan las 2 columnas en donde se emplazan los rotofiltros.
3 Corresponde a 6m 2 de las puertas de ingreso sumado a los 3,36 m 2 correspondiente al área total equivalente de
las 4 celosías.

Anexo F Estimación y Modelación de Olores 7 de 52

**Figura No 1** . Mapa de concentración de olor generado por las fuentes de emisión de la planta

(Percentil 98).

En base a lo mencionado anteriormente, en la siguiente Tabla, se presenta en forma detallada
las concentraciones de inmisión de olor en los receptores, donde se puede observar que ninguno
supera el límite de molestia de 3 OU E /m [3 ] (Percentil 98), descrito por la norma de referencia
colombiana.

Anexo F Estimación y Modelación de Olores 8 de 52

**Tabla No 3** . Concentración receptores. Percentil 98.

|No|ID|Descripción|Concentración<br>de inmisión<br>(OU /m3)<br>E|Límite inmisión<br>(Norma<br>colombiana)|Horas sobre<br>3,0 OU /m3<br>E|
|---|---|---|---|---|---|
|1|R1|Vivienda 1|**1,68**|**3,0**<br>**OUE/m3 **<br>**(percentil 98)**|59<br>(0,67%)|
|2|R2|Vivienda 2|**1,28**|**1,28**|24<br>(0,27%)|
|3|R3|Vivienda 3|**0,18**|**0,18**|0 <br>(0,00%)|
|4|R4|Vivienda 4|**2,06**|**2,06**|48<br>(0,55%)|
|5|R5|Vivienda 5|**0,79**|**0,79**|15<br>(0,17%)|
|6|R6|Vivienda 6|**0,78**|**0,78**|15<br>(0,17%)|
|7|R7|Vivienda 7|**0,50**|**0,50**|4 <br>(0,05%)|
|8|R8|Vivienda 8|**0,22**|**0,22**|0 <br>(0,00%)|
|9|R9|Vivienda 9|**0,13**|**0,13**|0 <br>(0,00%)|
|10|R10|Vivienda 10|**0,12**|**0,12**|0 <br>(0,00%)|
|11|R11|Vivienda 11|**0,06**|**0,06**|0 <br>(0,00%)|
|12|R12|Vivienda 12|**0,04**|**0,04**|0 <br>(0,00%)|
|13|R13|Vivienda 13|**0,04**|**0,04**|0 <br>(0,00%)|
|14|R14|Fundo los Castaños|**2,00**|**2,00**|52<br>(0,59%)|
|15|R15|Fundo Pilmaiquén|**1,67**|**1,67**|38<br>(0,43%)|
|16|R16|Fundo Pilmaiquén|**2,78**|**2,78**|156<br>(1,78%)|
|17|R17|Vivero Pilmaiquén|**0,22**|**0,22**|0 <br>(0,00%)|
|18|R18|Fundo Cuyaima|**0,06**|**0,06**|0 <br>(0,00%)|
|19|R19|Agrícola Pilmaiquén|**0,76**|**0,76**|9 <br>(0,10%)|

Se evaluó el efecto generado en diecinueve receptores discretos, la evaluación de los resultados,
demostró que en ninguno de los 19 recetores discretos superó el límite de referencia de 3
OU E /m [3], siendo los más altos el receptor N°4 y 16 (Vivienda 4 y Fundo Pilmaiquén,
respectivamente) con una concentración de inmisión de 2,06 y 2,78 OU E /m [3], respectivamente, lo
cual indica que las emisiones de la planta no implican una potencial afectación sobre la salud de
la población cercana, sistema de vida y costumbres, población protegida, y turismo.

Anexo F Estimación y Modelación de Olores 9 de 52

**2** **Introducción**

En el marco de la evaluación ambiental del proyecto centro de cultivo “Piscicultura San Pablo”,
se solicitó los servicios de Proterm S.A. con el objetivo de evaluar la futura dispersión de olores
provenientes de las principales fuentes. Tales fuentes consideradas corresponden Sistema de
Tratamiento del Efluente (específicamente en el Sistema de rotofiltros y Manejo de lodos), Silo
de mortalidad y PTAS (planta de tratamiento de aguas servidas).

El proyecto consiste en la construcción y operación de un centro de cultivo (Piscicultura) de flujo
abierto para una producción máxima anual de 2.622 ton/año de salmónidos a cosecha. El
Proyecto considera la implementación de 108 estanques de 350 m [3] cada uno, con una capacidad
instalada de 37.800 m [3], para la crianza de salmónidos desde 3 hasta 250 gramos de peso
promedio, con una proyección de generación anual de biomasa de 3.614 ton/año (850 Ton stock
+ 2.622 ton/año de biomasa a cosecha + 142 ton/año mortalidad proyectada). El centro de cultivo,
de flujo abierto, requiere de 10 m3/s (en periodo peak) para mantener los procesos de cultivo.
Dicho proyecto considera el abastecimiento de agua dulce desde un derecho de
aprovechamiento de aguas de carácter no consecutivo desde el Río Pilmaiquén otorgado por
Res DGA 196/08 por 10.000 lt/seg. Por otro lado, el área donde se emplazará el centro de cultivo
corresponde a una plantación de especies exóticas (Eucaliptus nitens) que está en edad de
cosecha, localizado en territorio privado al interior del Fundo conocido como Pilmaiquén II,
ubicada en la comuna de San Pablo, Provincia de Osorno, Región de Los Lagos.

A continuación, en la Figura N°2, se detalla la ubicación geográfica del proyecto, el
emplazamiento del archivo WRF y la zona modelada.

**Figura No 2** . Mapa ubicación del proyecto.

Anexo F Estimación y Modelación de Olores 10 de 52

**3** **Objetivos General**

Evaluar el efecto de las emisiones de olor del proyecto Piscicultura San Pablo, sobre la salud de
la población cercana, sistema de vida, costumbres, población protegida y turismo.

**Objetivos específicos**

Determinar las emisiones de olor generadas por el futuro proyecto “Piscicultura San Pablo”.

Evaluar el efecto de la dispersión de olores en diecinueve receptores discretos de interés
cercanos al proyecto.

Analizar y evaluar las variables meteorológicas consideradas en la modelación respecto a las
estaciones más cercanas al proyecto.

**4** **Metodología**

A continuación, se presenta la metodología que permitió evaluar las emisiones odorantes del
proyecto Piscicultura San Pablo.

**Caracterización de las fuentes**

Para poder evaluar los objetivos propuestos, se plantea el siguiente escenario:

Modelación de olor de las fuentes del futuro proyecto, evaluando la dispersión de la pluma
con respecto a los receptores discretos considerados.

Por otro lado, para poder caracterizar las fuentes generadoras de olor, se utilizaron las siguientes
metodologías.

- Detección satelital: Mediante Google Earth Pro, se identificaron las superficies de las fuentes
generadoras de emisión y la distancia con respecto a los sectores poblados.

- Solicitud de información: Se solicitó información al consultor del proyecto “Piscicultura San

Pablo”.

Revisión bibliográfica: Se consultaron diferentes plataformas para obtener información sobre
la ubicación, procesos, producción y tipos de fuentes de emisión de olor relacionadas con el
tipo de tecnología utilizada. Asimismo, se utiliza como base para identificación de las fuentes,
el estudio: Antecedentes para la regulación de olores en Chile, y la Estrategia para la gestión
de olores en Chile, aprobada a través la Resolución Exenta N°947 el 7 de noviembre de 2013
del Ministerio de Medio Ambiente, en donde se menciona que la industria pesquera y el
procesamiento de productos del mar potencialmente generan malos olores. De igual forma
es utilizada la base de datos del SEA, específicamente proyectos aprobados con factores de
emisión aplicables al proyecto en cuestión.

Anexo F Estimación y Modelación de Olores 11 de 52

**Estimación de emisiones**

Para conocer las emisiones del “Proyecto” se utilizaron Factores de Emisión de olor.

**Factores de emisión de olor (OEF)** : son análogos a los factores de emisión desarrollados por
la US EPA para otros contaminantes. Se utiliza la siguiente ecuación:

OER= A∗OEF

Donde OER es la tasa de emisión de olor en (OU E /s), A es el nivel de actividad, OEF es el factor
de emisión.

**Figura No 3** . Esquema resumen de las metodologías para estimar las emisiones de olor.

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
trayectoria por “Puff”, lo que hace su cálculo mucho más rápido [4] .

4 Guía para el uso de modelos de calidad del aire, 2023.

Anexo F Estimación y Modelación de Olores 12 de 52

Para la modelación se utilizó el software Calpuff versión 7.2.1 junto a los módulos CALPOST
7.1.0. y CALRANK 7.0.0. Además, para efectos de la interacción gráfica de los módulos, se usó
el software interactivo CALPUFF View 8.5.0.

En Anexo No1 se presenta un esquema de funcionamiento del software Calpuff.

**4.3.2 Recopilación de Antecedentes Para la Modelación**

Para conocer la dispersión que tendrán los contaminantes en un área determinada es preciso
incorporar al modelo seleccionado distintos parámetros de manera que la simulación sea lo más
parecida a las condiciones reales. Las variables o entradas que requirió el modelo se muestran
en la tabla a continuación:

**Tabla No 4.** Variables de entrada consideradas en la modelación

|Variable|Parámetros|Fuente|
|---|---|---|
|Meteorológicas|Dirección de Viento|Tal como lo establece la guía el modelo<br>numérico recomendado para la generación de<br>datos meteorológicos es el Weather Research<br>and Forecasting Model (WRF)5. WRF es uno<br>de los modelos meteorológicos de pronóstico<br>más avanzados y completos y es mantenido<br>por NCAR9/NOAA10 de Estados Unidos.|
|Meteorológicas|Velocidad de Viento|Velocidad de Viento|
|Meteorológicas|Temperatura|Temperatura|
|Meteorológicas|Presión|Presión|
|Meteorológicas|Precipitación|Precipitación|
|Geofísicas|Elevación del Terreno|Elevación del Terreno|
|Geofísicas|Uso de Suelo|Uso de Suelo|
|Características de la<br>fuente|Fuentes de emisión|Información proporcionada por el mandante<br>del proyecto.|
|Características de la<br>fuente|Superficies de fuentes de<br>emisión|Superficies de fuentes de<br>emisión|
|Receptores Discretos|Coordenadas de los<br>receptores|Se definieron los poblados cercanos a la<br>piscicultura, y los ubicados en el interior de la<br>superficie del área de influencia. Cabe<br>destacar<br>que<br>los<br>receptores<br>fueron<br>proporcionados por el titular.|

**4.3.3 Variables meteorológicas y geofísicas**

La Guía Para el Uso de Modelos de Calidad del Aire publicada en el año 2012 y actualizada en
febrero de 2023, señala que en el modelo de calidad del aire se debe configurar una grilla de
receptores en forma adicional a los receptores discretos. Para asegurar un mejor desempeño del
modelo, se recomienda definir cinco grillas como lo indica la siguiente tabla:

5 Se consideró un WRF del año 2022 debido a que dicho año presentó datos meteorológicos más estables, por ende
corresponde al escenario más desfavorable considerando 3 años de evaluación según la Guía para Uso de Modelos
de Calidad del aire, actualizada en febrero del 2023.

Anexo F Estimación y Modelación de Olores 13 de 52

**Tabla No 5** . Configuración de grilla.

|ID|Espaciado<br>(m)|Distancia<br>(m)|Observación|Altura de grilla de<br>receptores|
|---|---|---|---|---|
|Grilla 1|20|-|La grilla se define dentro del perímetro<br>de la instalación|1,5 m|
|Grilla 2|50|500|Desde la fuente y sobre el terreno<br>elevado|Desde la fuente y sobre el terreno<br>elevado|
|Grilla 3|250|2.000|Desde la fuente|Desde la fuente|
|Grilla 4|500|5.000|Desde la fuente|Desde la fuente|
|Grilla 5|1.000|Más de<br>5000|Desde la fuente|Desde la fuente|

|WRF|Sampling Grid|
|---|---|
|<br>Nested Grid|<br>Nested Grid y Receptores Discretos.|

**Figura No 4** . Visualización de distribución de grillas de modelación.

(WRF, Sampling grid, Nested Grid y Discrete Receptors)

Anexo F Estimación y Modelación de Olores 14 de 52

Tal como se mencionó en el punto 4.3.1, se utilizó la meteorología de pronóstico WRF 2022 en
formato calmet.dat, de esta forma se incorporó el archivo directamente al programa. El archivo
meteorológico tiene su centro en la comuna de San Pablo. Para la ejecución del modelo se
modeló una zona más pequeña en comparación al WRF, es importante destacar que la zona
modelada tiene una dimensión de grilla de 250 metros. En la tabla N°3 se presentan las
características del archivo meteorológico y en la figura N°2 los límites indicados (figura en
apartado “introducción”).

**Tabla No 6.** Características del archivo meteorológico WRF 2022.

|Datos|Col2|Archivo Meteorológico|
|---|---|---|
|Comuna|Comuna|San Pablo|
|Dimensión grilla|Dimensión grilla|71x71 km|
|Espaciado grilla|Espaciado grilla|1 km|
|Fecha-Hora inicio|Fecha-Hora inicio|**01-01-2022** 00:00|
|Fecha-Hora fin|Fecha-Hora fin|**31-12-2022** 23:00|
|Coordenadas NO6|Este|706.705|
|Coordenadas NO6|Norte|5.562.187|
|Coordenada NE7|Este|635.568|
|Coordenada NE7|Norte|5.563.484|
|Coordenada SO8|Este|633.830|
|Coordenada SO8|Norte|5.492.594|
|Coordenadas SE9|Este|704.955|
|Coordenadas SE9|Norte|5.491.193|

**Cabe señalar que el archivo meteorológico WRF 2022 utilizado en la modelación de olores**
**fue el mismo archivo utilizado en la modelación atmosférica del Proyecto. Por lo tanto,**
**este archivo ya fue cargado en el expediente del Proyecto como archivo de gran tamaño**
**en el marco del Anexo E “Modelación de Emisiones Atmosféricas” la adenda anterior, con**
**el nombre de Calmet 2022. En el Apéndice 3 del presente Anexo F, se adjunta el**
**comprobante de la carga de este archivo en la adenda anterior.**

6 Coordenadas WGS-84 Huso 18 S
7 Coordenadas WGS-84 Huso 18 S
8 Coordenadas WGS-84 Huso 18 S
9 Coordenadas WGS-84 Huso 18 S

Anexo F Estimación y Modelación de Olores 15 de 52

**4.3.4 Evaluación de los resultados**

Los resultados de las concentraciones de olor (OU E /m [3] ) arrojadas por el modelo de dispersión,
fueron comparados con el límite de referencia propuesto por Colombia, según la resolución
vigente N°1.541 del Ministerio de Ambiente y Desarrollo Sostenible. La norma señala 3 OU E /m [3 ]

como nivel permisible de calidad del aire para el procesamiento y conservación de carne,
pescado, crustáceos y moluscos. Es importante mencionar, que este límite se ha indicado en
otros proyectos referentes a elaboración y procesamiento de productos del mar en el país. Se
define dicho límite, debido a que en Chile no existe normativa de calidad o norma de emisión
específica para este tipo de proyectos.

Para evaluar las concentraciones de olor, generadas por Piscicultura San Pablo, se utilizó como
valor límite 3 OU E /m [3] dado por la similitud que dicho valor regula las concentraciones que
involucran la actividad pesquera y el procesamiento de productos del mar. Se señala que este
valor límite se ha utilizado en diferentes proyectos del rubro pesquero evaluados en el marco del
Sistema de Evaluación de Impacto Ambiental (SEIA).

Junto a los resultados de concentración de olor, se identificará el área de influencia de la
operación de la planta. Tal como lo indica la guía, el área de Influencia se debe circunscribir en
el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de detección del
olor compuesto.

Anexo F Estimación y Modelación de Olores 16 de 52

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
variables de viento respecto a los registros de las estaciones públicas Osorno desde el sistema
SINCA.

Anexo F Estimación y Modelación de Olores 17 de 52

**5** **Resultados**

A continuación, se presentan los resultados que permitirán evaluar el efecto de las emisiones de
olor del Proyecto en estudio.

**Caracterización de las fuentes de emisión**

A continuación, se describen las fuentes generadoras de olor para el escenario a modelar. En la
siguiente tabla se detallan las fuentes consideradas en la modelación, mientras que en la
cartografía se presenta su ubicación espacial. Lo anterior de acuerdo con lo señalado en el punto
3.3 de guía para la predicción y evaluación de olores.

**Tabla No 7** . Descripción fuentes y procesos asociados [10] .

|Fuente|Col2|Descripción de referencia|
|---|---|---|
|Sistema de<br>Tratamiento<br>del Efluente|Sistema<br>de<br>Rotofiltros|El efluente del sistema de piscicultura será tratado por medio de rotofiltros,<br>destinados a la filtración de líquidos, a través de una separación continua<br>del sólido - líquido. El rotofiltro es un dispositivo de funcionamiento auto<br>limpiante, capaz de operar durante largos períodos sin necesidad de<br>atención|
|Sistema de<br>Tratamiento<br>del Efluente|Manejo de<br>Lodos|Posteriormente, los sólidos resultantes del retrolavado del sistema de<br>tratamiento del efluente, serán dispuestos en un estanque de concreto<br>armado, con hormigón H25, con adición de aditivo impermeabilizante.|
|Silo de Mortalidad|Silo de Mortalidad|Para el manejo de la mortalidad originada en proceso productivo, se<br>instalará un Sistema de Ensilaje compuesto de los siguientes componentes:<br>picador, bomba moledora, bomba dosificadora, entre otros.<br>Para evitar riesgo de escurrimiento producto de la operación del sistema de<br>ensilaje o sus componentes se habilitará una losa de concreto con un pretil.|
|PTAS|PTAS|El Proyecto considera como solución sanitaria sistemas de tratamiento de<br>aguas servidas, conformado por dos plantas de tratamiento de aguas<br>servidas (en adelante PTAS), diseñadas para recibir la descarga de agua<br>residual proveniente de las instalaciones sanitarias del centro de<br>piscicultura. La disposición final del efluente tratado será a través de drenes<br>de infiltración.|

10 Información proveída por el titular .

Anexo F Estimación y Modelación de Olores 18 de 52

**Ubicación de fuentes**

A continuación, se presenta la ubicación de las fuentes evaluadas, mientras que en la imagen se
muestra la ubicación espacial de cada una de ellas.

**Tabla No 8.** Coordenadas de fuentes de emisión odorantes.

|Fuente|Coordenadas WGS-84 Huso 18S|Col3|
|---|---|---|
|**Fuente**|**Este (m)**|**Norte (m)**|
|Sistema de Rotofiltros|670.075|5.527.438|
|Manejo de Lodos|670.047|5.527.454|
|Silo de Mortalidad|670.244|5.527.325|
|PTAS|670.028|5.527.410|

En la siguiente figura se presenta la ubicación espacial de las fuentes de emisiones considerados
en la modelación.

**Figura No 5** . Ubicación espacial de las fuentes generadoras de olor del proyecto.

Anexo F Estimación y Modelación de Olores 19 de 52

**Factores de emisión utilizados**

En cuanto a los factores de emisión a utilizar, se realiza una búsqueda en donde se contempla
como una buena fuente de factores de emisión, la “Guía de Emisiones para Holanda” (Abreviada
NeR) (INFOMIL 2004), sumado a los estándares de calidad del aire con respecto a olores del
Ministerio de Medio Ambiente VROM, sin embargo, para el proyecto en evaluación solo
continente factores par obras de tratamiento de residuos líquidos (domésticos). Se determinan
las siguientes fuentes y sus factores de emisión para el tratamiento de aguas residuales
aplicables al proyecto (sección G3).

**Tabla No 9.** Factores de emisión Guía Holandesa.

|Fuente|Factor de Emisión (OU /m2s)<br>E|
|---|---|
|Rejas|7|
|Clarificador primario|7,5|
|Estanque de lodos|3,95|

Por otro lado, ante la carencia de factores de emisión para este tipo de industria, se realizó una
búsqueda en el SEIA con el objetivo de encontrar emisiones de referencia para proyectos y/o
actividades similares. La búsqueda se enfoca principalmente en proyectos ingresados desde el
2018 hasta la fecha, en donde ya se encontraba vigente la Guía para la Predicción y Evaluación
de Impactos por Olor en el SEIA. Se encontraron los siguientes proyectos con potencial de
homologación de factores:

**Tabla No 10.** Factores de emisión para proyectos aprobados de Pisciculturas.

|Proyecto|Fuente|Factor de emisión<br>(OU /m2s)<br>E|
|---|---|---|
|Piscicultura de Recirculación<br>Los Arrayanes -<br>Componente Olores<br>(2018)|Filtros rotatorios|7|
|Piscicultura de Recirculación<br>Los Arrayanes -<br>Componente Olores<br>(2018)|Estanques buffer de lodos|3,95|
|Piscicultura de Recirculación<br>Los Arrayanes -<br>Componente Olores<br>(2018)|Espesamiento y deshidratación|1,75|
|Piscicultura de Recirculación<br>Los Arrayanes -<br>Componente Olores<br>(2018)|Acopio de lodo deshidratado|1,75|
|Piscicultura de Recirculación<br>Los Arrayanes -<br>Componente Olores<br>(2018)|Estanque de mortalidad|26,3|
|Modificación Proyecto<br>Técnico y Mejoramiento<br>Piscicultura Trafún<br>(2020)|Filtros rotatorios Planta de Tratamiento N°1|7|
|Modificación Proyecto<br>Técnico y Mejoramiento<br>Piscicultura Trafún<br>(2020)|Filtros rotatorios Planta de tratamiento N°2|7|
|Modificación Proyecto<br>Técnico y Mejoramiento<br>Piscicultura Trafún<br>(2020)|Estanque acopio de lodos|3,95|
|Modificación Proyecto<br>Técnico y Mejoramiento<br>Piscicultura Trafún<br>(2020)|Estanque de almacenamiento de mortalidad|26,3|
|Modernización y Aumento de<br>Producción en Piscicultura<br>Quillaico<br>(2021)|Filtros rotatorios|7,5|
|Modernización y Aumento de<br>Producción en Piscicultura<br>Quillaico<br>(2021)|Estanque de lodos|8|
|Modernización y Aumento de<br>Producción en Piscicultura<br>Quillaico<br>(2021)|Filtro de lodos / Deshidratación de lodos|4,35|
|Modernización y Aumento de<br>Producción en Piscicultura<br>Quillaico<br>(2021)|Biofiltración|0,16|
|Modernización y Aumento de<br>Producción en Piscicultura<br>Quillaico<br>(2021)|Estanque de mortalidad|3|

Anexo F Estimación y Modelación de Olores 20 de 52

Bajo el contexto de que hoy en día no contamos con factores de emisión provenientes de fuentes medidas con características similares
a las presentes en el proyecto en cuestión, se decide utilizar aquellos factores de emisión de proyectos aprobados, con los valores
más altos, con el objetivo de evaluar el peor escenario, tal como establece la “Guía para la predicción y evaluación de impactos por
olor en el SEIA”, para proyectos que aún no se encuentran en ejecución. A continuación, tabla resumen de factores de emisión
utilizados para las fuentes a evaluar en proyecto en cuestión.

**Tabla No 11.** Factores de emisión a utilizar en proyecto en cuestión.

|Fuente|Col2|Factor de<br>Emisión<br>(OU /m2s)<br>E|Referencia|Justificación técnica de utilización de estos factores|
|---|---|---|---|---|
|Sistema de<br>Tratamiento<br>del Efluente|Sistema<br>de<br>Rotofiltros|**7,5**|Modernización y<br>Aumento de<br>Producción en<br>Piscicultura<br>Quillaico<br>(2021)|Para ambos casos los factores de emisión provienen originalmente de plantas de<br>tratamiento de aguas servidas, esto debido a que no existen estudios de impacto odorante<br>para este tipo de proyectos y así poder contar con emisiones de referencia. Es por esto que<br>se optó por la utilización de factores en donde su origen proviene del Informe BS<br>Consultores (2015) para factores de emisión de Tratamiento de RILes y Aguas Servidas,<br>obtenidas de la regulación de emisiones del Reino de los Países Bajos, siendo la fuente<br>original INFOMIL (2004). De este modo, se concluye que el uso de dichos factores de<br>emisión comprende una evaluación muy conservadora, ya que el potencial odorífico de una<br>planta de tratamiento de aguas servidas es evidentemente mucho más elevado que el de<br>una piscicultura.|
|Sistema de<br>Tratamiento<br>del Efluente|Manejo<br>de Lodos|**8,0**|**8,0**|**8,0**|
|Silo de Mortalidad|Silo de Mortalidad|**26,3**|Modificación<br>Proyecto Técnico<br>y Mejoramiento<br>Piscicultura<br>Trafún<br>(2020)|Para el caso del presente factor, este presenta su origen en un Estudio de Impacto<br>Odorante de Planta Orizon Coronel Sur, por lo tanto, la utilización de dicho factor resulta<br>ser un escenario extremadamente conservador, debido a que el potencial odorífico de una<br>planta de Harina y Aceite son muchos mayores a la de una Piscicultura, por lo tanto, se<br>está evaluando una sobreestimación de las emisiones, lo cual representaría el escenario<br>más desfavorable|
|PTAS|PTAS|**1,75**|Piscicultura de<br>Recirculación Los<br>Arrayanes -<br>Componente<br>Olores<br>(2018)|En cuanto al Factor utilizado para PTAS, se opta por un factor que presenta su origen en el<br>Informe BS Consultores (2015) para factores de emisión de Tratamiento de RILes y Aguas<br>Servidas, obtenidas de la regulación de emisiones del Reino de los Países Bajos, siendo la<br>fuente original INFOMIL (2004). Esto efectivamente evalúa una sobreestimación, debido al<br>potencial odorífico de las Plantas de tratamiento de aguas servidas es evidentemente de<br>índole mayor en comparación con las Pisciculturas.|

Anexo F Estimación y Modelación de Olores 21 de 52

Es importante mencionar que la ausencia de factores de emisión y emisiones de referencia para esta tipología de proyectos, es un
indicador de que el potencial de generación de malos olores es más bien bajo. En base a esto y cómo antecedente adicional, es que
tampoco se ha encontrado en la literatura internacional emisiones de referencia o factores de emisión para la actividad de acuícultura
esto muy probablemente porque se trata de una tipología de proyectos que genera muy pocos olores, ya que “peces vivos en agua
no huelen” (cita original “Land based aquaculture facilities typically create very little odour as live fish in water don't smell.” VFA, 2005).

Resuelta la obtención de factores de emisión, se procede a evaluar las emisiones que serán incorporadas al modelo. Mayor detalle
en el siguiente apartado.

**Emisiones de olores**

En primera instancia, se presenta la justificación de las áreas efectivas de emisión, basadas en el emplazamiento y características
constructivas de cada fuente evaluada:

**Tabla No 12** . Justificación de áreas efectivas de emisión. [11]

|Fuente|Col2|Dimensiones|Col4|Col5|Justificación|
|---|---|---|---|---|---|
|**Fuente**|**Fuente**|**Área efectiva**<br>**de emisión**<br>**(m2) **|**Cantidad**|**Área Total**<br>**Efectiva (m2) **|**Área Total**<br>**Efectiva (m2) **|
|Sistema de<br>Tratamiento<br>del Efluente|Sistema de<br>Rotofiltros|266|2|**532**|Corresponde al área efectiva de los rotofiltros, considerando la ubicación de<br>estos en dos columnas, es por esto que se detalla “2” como cantidad.|
|Sistema de<br>Tratamiento<br>del Efluente|Manejo de<br>Lodos|0,64|4|**2,6**|Si bien la cámara de lodos presenta una superficie total por diseño de 112 m2,<br>el área efectiva de emisión corresponde 4 compuertas de 0,64 m2, la cual<br>presenta un área total efectiva de 2,6 m2.|
|Silo de Mortalidad|Silo de Mortalidad|9,36|1|**9,36**|Para el caso del silo de mortalidad, este considera un área de 9,36 m2, lo cual<br>representa el área efectiva correspondiente a la puerta de acceso del galpón<br>donde se encuentra el silo y el área equivalente total de las celosías.|
|PTAS|PTAS|3,0|1|**3,0**|En cuanto a PTAS, si bien la superficie de diseño del emplazado de la PTAS,<br>comprende 14,64 m2, el área efectivamente expuesta, corresponde a la<br>abertura de ingreso del portón con 3,0 m2. Importante considerar, que el<br>sistema más bien cerrado, por lo que se estaría considerando en su peor<br>escenario. Se considera solo 1 correspondiente a la obra permanente en la<br>etapa de operación (PTAS en construcción es solo temporal).|

11 De manera complementaria y para mayor comprensión, revisar Figura N°4 de ubicación de fuente.

Anexo F Estimación y Modelación de Olores 22 de 52

A continuación, se presentan las emisiones de olores obtenidas por la revisión bibliográfica de factores de emisión de olor (OEF),
expresadas en tasa de emisiones de olor (OU E /s), esto en base a la “Guía para la predicción y evaluación de impacto por olor en el
SEIA”.

**Tabla No 13** . Factores de emisión y emisión asociada a cada fuente.

|Fuente|Col2|Dimensiones|Col4|Col5|Factor de emisión<br>(OU /m2/s)<br>E|Emisión de<br>olor (OU /s)12<br>E|
|---|---|---|---|---|---|---|
|**Fuente**|**Fuente**|**Área efectiva**<br>**de emisión (m2) **|**Cantidad**|**Área Total Efectiva**<br>**(m2) **|**Área Total Efectiva**<br>**(m2) **|**Área Total Efectiva**<br>**(m2) **|
|Sistema de Tratamiento<br>del Efluente|Sistema de Rotofiltros|266|213|**532**|**7,5**|**3.990**|
|Sistema de Tratamiento<br>del Efluente|Manejo de Lodos|0,64|4|**2,6**|**8,0**|**21**|
|Silo de Mortalidad|Silo de Mortalidad|9,3614|1|**9,36**|**26,3**|**246**|
|PTAS|PTAS|3,0|1|**3,0**|**1,75**|**5,3**|

En la tabla anterior, se puede observar que las mayores emisiones provienen del sistema de rotofiltros con 3.990 OU E /s, seguida del
silo de mortalidad, manejo de lodo y PTAS. En la siguiente figura, es posible observar la distribución porcentual de las emisiones:

**Figura No 6** . Distribución porcentual de Emisiones.

12 Las emisiones de olores de las fuentes consideradas en la modelación, se incorporaron asumiendo un periodo de funcionamiento anual constante,
representando de esta manera, el escenario más desfavorable que se pudiese generar.
13 Se consideran 2, ya que se contemplan las 2 columnas en donde se emplazan los rotofiltros.
14 Corresponde a 6m 2 de las puertas de ingreso sumado a los 3,36 m 2 correspondiente al área total equivalente de las 4 celosías.

Anexo F Estimación y Modelación de Olores 23 de 52

**Evaluación de la dispersión de olores**

A continuación, se presentan los resultados de dispersión y concentración de olores en el área
de estudio y en los receptores discretos considerados (diecinueve), para el escenario evaluado.

Escenario evaluado: Modelación de las emisiones de olor de las potenciales fuentes de emisión
de olor tales como Sistema de Tratamiento del Efluente (específicamente en el Sistema de
rotofiltros y Manejo de lodos), Silo de mortalidad y PTAS de la Piscicultura San Pablo, ubicada
en la comuna de San Pablo, Provincia de Osorno, Región de Los Lagos.

Se presenta un mapa de dispersión de olor, el cual registra el percentil 98 de las
concentraciones horarias, con el objetivo de poder comparar los resultados con el límite de
referencia propuesto por Colombia, según la resolución vigente N°1.541 del Ministerio de
Ambiente y Desarrollo Sostenible.

Considerando que los criterios de máximo impacto horario, o condición más desfavorable, no
son representativos de una condición de exposición permanente sintetizada en un año, debido
a la variación del estado meteorológico estacional de un determinado lugar, se recomienda el
uso del criterio de percentil 98 el cual permite visualizar los porcentajes de horas en que se
supera el valor definido para las 8.760 horas del año [15] .

**5.5.1 Dispersión de emisiones de olor.**

En la figura a continuación se muestra la dispersión de odorantes desde la Piscicultura San
Pablo. La imagen presenta las máximas concentraciones de olor en las zonas aledañas a la
piscicultura, considerando una excedencia de un 2%, lo que es comparado con las normas de
referencia. El análisis presente indica que durante el 98% de las horas del año se presentarán
concentraciones igual o menor al valor indicado en la cartografía.

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se acentúa
en sentido noreste y suroeste con una longitud aproximada de 1,47 km. Las curvas de isoconcentración pueden alcanzar valores entre 1,0 a 22,5 OU E /m [3] alcanzando su mayor
concentración al costado Este del sistema de Rotofiltros. Fuera de los límites de la planta las
isodoras trazan valores entre 1,0 a 3,0 OU E /m [3], abarcando un área total de 122 ha para la
isodora de 1,0 OU E /m [3] .

15
Según la Guía para la predicción y evaluación de impactos por olor en el SEIA, 2017.

Anexo F Estimación y Modelación de Olores 24 de 52

**Figura No 7** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio

horario, percentil 98. [ 16]

**5.5.2 Punto Máxima concentración de olor**

El punto de máxima concentración se posiciona a 3,1 metros del sistema de Rotofiltros y a 71
metros de la unidad de cultivo más cercana, alcanzando una concentración de 22,5 OU E /m [3] .

En función de la dispersión de olor, se determina el punto de máxima concentración, el cual se
detalla a continuación:

**Tabla No 14.** Punto máximo impacto para percentil 98. Coordenadas UTM 18S.

|Concentración<br>(OU /m3)<br>E|Coordenada Este (m)|Coordenada Norte (m)|
|---|---|---|
|22,5|670.082|5.527.424|

16 PMC: Punto de máxima concentración.

Anexo F Estimación y Modelación de Olores 25 de 52

**5.5.3 Área de Influencia**

Con base en la dispersión de emisiones del escenario evaluado, se determinó un área de
influencia definida según la “Guía para la predicción y evaluación de impactos por olor en el
SEIA” [17], como el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de
detección del olor compuesto, es decir, es la concentración en donde el 50% de la población
puede percibir un olor.

A continuación, se observa el mapa con el emplazamiento de área de influencia circunscrita por
el límite de isoconcentración de 1 OU E /m [3] .

**Figura No 8.** Mapa del Área de Influencia (AI), definida por 1 OU E /m [3] .

La isodora de 1 OU E /m3, valor que indica la concentración desde el cual el 50% de la población
puede percibir un olor, cubre una superficie de 122 ha. La distribución de la pluma se acentúa
en sentido noreste y suroeste con una longitud aproximada de 1,47 km.

17 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Anexo F Estimación y Modelación de Olores 26 de 52

Como se mencionó anteriormente, el área de influencia, determinada por la curva de isoconcentración de 1 OU E /m3, se circunscribe hacia el este de la Piscicultura San Pablo,
cubriendo un área forestal y viviendas cercanas. El área de influencia circunscribe cinco
receptores (R1, R2, R4, R14, R15 y R16).

**5.5.3.1 Receptores discretos considerados en la modelación**

A continuación, se presentan los receptores discretos considerados en la modelación descritos
en la siguiente tabla:

**Tabla No 15** . Receptores discretos considerados en la modelación.

|No|ID|Distancia a la fuente<br>más cercana (km)|Coordenadas UTM WGS-84<br>Zona 18 S|Col5|Uso de Suelo|
|---|---|---|---|---|---|
|**No**|**ID**|**Distancia a la fuente**<br>**más cercana (km)**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R1|Vivienda 1|0,47|670.120|5.527.909|Agrícola|
|R2|Vivienda 2|0,45|669.778|5.527.781|Agrícola|
|R3|Vivienda 3|0,85|669.273|5.527.718|Forestal|
|R4|Vivienda 4|0,25|669.905|5.527.622|Agrícola|
|R5|Vivienda 5|0,69|669.821|5.526.794|Agropecuario|
|R6|Vivienda 6|0,67|669.965|5.526.780|Agropecuario|
|R7|Vivienda 7|0,79|669.878|5.526.676|Agropecuario|
|R8|Vivienda 8|0,99|669.766|5.526.500|Agrícola|
|R9|Vivienda 9|1,14|669.803|5.526.335|Agropecuario|
|R10|Vivienda 10|1,15|669.863|5.526.312|Agropecuario|
|R11|Vivienda 11|1,46|669.588|5.526.060|Agrícola|
|R12|Vivienda 12|1,62|669.633|5.525.883|Agropecuario|
|R13|Vivienda 13|1,71|669.640|5.525.789|Agropecuario|
|R14|Fundo los Castaños|0,11|670.271|5.527.236|Agropecuario|
|R15|Fundo Pilmaiquén|0,35|669.736|5.527.350|Agrícola|
|R16|Fundo Pilmaiquén|0,43|670.422|5.527.681|Agrícola|
|R17|Vivero Pilmaiquén|0,84|669.313|5.527.788|Forestal|
|R18|Fundo Cuyaima|1,34|670.068|5.526.097|Agropecuario|
|R19|Agrícola Pilmaiquén|0,61|669.779|5.527.975|Agrícola|

Anexo F Estimación y Modelación de Olores 27 de 52

**Figura No 9** . Receptores discretos considerados en la modelación.

En la siguiente tabla, se presenta el resultado del Percentil 98, de las concentraciones horarias
para cada receptor discreto considerado en la modelación. Tal como se puede apreciar en la
tabla, la futura operación de la Piscicultura produciría concentraciones de inmisión que se
encuentran bajo el límite de referencia establecido en la normativa colombiana (3,0 OU E /m [3] ).
Las concentraciones mayores se observan en los receptores R4 y R16 (Vivienda 4 y Fundo
Pilmaiquén, respectivamente) que alcanzan 2,06 y 2,78 OU E /m [3] respectivamente,
concentraciones que se encuentran bajo el límite de inmisión establecido en la normativa de
referencia.

Anexo F Estimación y Modelación de Olores 28 de 52

**Tabla No 16** . Concentración receptores. Escenario Actual, percentil 98 .

|No|ID|Descripción|Concentración<br>de inmisión<br>(OU /m3)<br>E|Límite inmisión<br>(Norma<br>colombiana)|Horas sobre<br>3,0 OU /m3<br>E|
|---|---|---|---|---|---|
|1|R1|Vivienda 1|**1,68**|**3,0**<br>**OUE/m3 **<br>**(percentil 98)**|59<br>(0,67%)|
|2|R2|Vivienda 2|**1,28**|**1,28**|24<br>(0,27%)|
|3|R3|Vivienda 3|**0,18**|**0,18**|0 <br>(0,00%)|
|4|R4|Vivienda 4|**2,06**|**2,06**|48<br>(0,55%)|
|5|R5|Vivienda 5|**0,79**|**0,79**|15<br>(0,17%)|
|6|R6|Vivienda 6|**0,78**|**0,78**|15<br>(0,17%)|
|7|R7|Vivienda 7|**0,50**|**0,50**|4 <br>(0,05%)|
|8|R8|Vivienda 8|**0,22**|**0,22**|0 <br>(0,00%)|
|9|R9|Vivienda 9|**0,13**|**0,13**|0 <br>(0,00%)|
|10|R10|Vivienda 10|**0,12**|**0,12**|0 <br>(0,00%)|
|11|R11|Vivienda 11|**0,06**|**0,06**|0 <br>(0,00%)|
|12|R12|Vivienda 12|**0,04**|**0,04**|0 <br>(0,00%)|
|13|R13|Vivienda 13|**0,04**|**0,04**|0 <br>(0,00%)|
|14|R14|Fundo los Castaños|**2,00**|**2,00**|52<br>(0,59%)|
|15|R15|Fundo Pilmaiquén|**1,67**|**1,67**|38<br>(0,43%)|
|16|R16|Fundo Pilmaiquén|**2,78**|**2,78**|156<br>(1,78%)|
|17|R17|Vivero Pilmaiquén|**0,22**|**0,22**|0 <br>(0,00%)|
|18|R18|Fundo Cuyaima|**0,06**|**0,06**|0 <br>(0,00%)|
|19|R19|Agrícola Pilmaiquén|**0,76**|**0,76**|9 <br>(0,10%)|

En el Anexo N°2 se presenta el análisis de la variación horaria de olor, en los receptores
discretos que presentaron la mayor concentración de olor.

.

Anexo F Estimación y Modelación de Olores 29 de 52

**5.5.3.1.1 Frecuencia Percepción Olor**

**Figura No 10** . Mapa de horas sobre 3,0 OU E /m3 generado por las fuentes de emisión de la

Piscicultura San Pablo, promedio horario (percentil 98).

En la figura anterior se puede observar las horas al año sobre las 3 OUE/m3. Dicha figura indica
que los lugares sobre un 2% de frecuencia (175 horas), se encuentran superior a la excedencia
entregada por el percentil 98. Las zonas al interior de esta curva corresponden a sectores al
interior la Piscicultura San Pablo, territorio que no se encuentra habitado. Todas las viviendas
cercanas (indicadas por un punto amarillo, receptores) se encuentran bajo las 175 horas sobre
3 OU E /m3, lo que indica que ninguna zona usada como residencia supera el 2% de horas por
sobre el umbral de molestia.

Anexo F Estimación y Modelación de Olores 30 de 52

**5.5.3.1.2 Protocolo FIDOL**

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

**Tabla No 17** . Protocolo FIDOL.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia<br>>3 OUe/m3|La Piscicultura San Pablo operará durante todos los días del año. Sin embargo, durante<br>el 98% de las horas del año no se prevé superación de las 3 OUE/m3, lo anterior porque<br>en los receptores R4 y R16, alcanzan valores de 2,02 y 2,78 OUE/m3 respectivamente<br>(máximo durante el 98% del tiempo). Por lo tanto, las horas sobre 3 OUE/m3, son menores<br>al 2% del año, siendo 0,55% y 1,78%, los mayores porcentajes, en dichos receptores<br>respectivamente.|
|Intensidad|Ningún receptor se encuentra sobre las 3 OUE/m3 en el percentil 98, de la normativa de<br>referencia (concentración que representa el umbral de molestia). Dado que los resultados<br>en los receptores son menores a 3 OUE/m3, no se prevé afectación en términos de<br>intensidad en los 19 receptores considerados en la modelación.|
|Duración|En cuanto a la duración, pese a que la proyecto contempla una operación constante, las<br>horas sobre e límite no superan el 1% de las horas totales anuales, considerando los<br>receptores más cercanos. Dado lo anterior se considera que solo pudiese haber<br>superación solo en eventos intermitentes, menor al 1% de las horas anuales.|
|Ofensividad|Considerando que las concentraciones en receptores no superan el límite del umbral de<br>molestia de 3 OUE/m3, se puede concluir que, la combinación entre frecuencia, intensidad<br>y duración no representan ofensividad, considerando los 19 receptores discretos<br>definidos.|
|Localización|El proyecto se emplaza al interior de un predio localizado en Fundo Pilmaiquén II, de<br>propiedad del titular, y que colinda con el Río Pilmaiquén. El uso de suelo al que<br>pertenece corresponde a suelos de Clase III y IV dentro del área del predio.|

Anexo F Estimación y Modelación de Olores 31 de 52

**Análisis del desempeño del archivo de pronóstico utilizado**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para ello
se utilizan los datos disponibles de las estaciones de monitoreo ubicadas en la zona de interés
para el estudio.

La estación utilizada corresponde a La Unión del sistema SINCA, ubicada a 12,8 km
respectivamente de la Piscicultura San Pablo. Esta estación presentan datos de temperatura,
dirección y velocidad de viento, las cuales serán utilizadas para validar el modelo meteorológico
de pronóstico WRF, no siendo usadas como entradas al modelo.

En el Anexo N°3 se presentan las variables meteorológicas y geofísicas del emplazamiento del
proyecto y en el Anexo No4 se presenta una comparación cualitativa y cuantitativa entre la
meteorología de pronóstico y los datos observados en la estación meteorológica La Unión. De
igual manera se presentan estos resultados en los Anexos N°5 y N°6.

De acuerdo con las comparaciones realizadas en forma cualitativa de ciclo diario, promedio
mensual rosa de los vientos y ciclos estacionales, para los parámetros temperatura, velocidad y
dirección de viento para la estación de La Unión se puede indicar que tanto el modelo WRF y los
datos observados presentan valores y patrones similares, que permiten indicar que los datos
WRF se ajustan a la realidad y pueden ser utilizados en la modelación.

**Figura No 11** . Estaciones Meteorológicas utilizada en el Análisis de Incertidumbre.

Anexo F Estimación y Modelación de Olores 32 de 52

**6** **Conclusiones**

De acuerdo al estudio de estimación y evaluación de la dispersión de las fuentes de olores, se
concluye lo siguiente:

1. La mayor emisión se presenta en el sistema de rotofiltros alcanzando un valor de 3.990

OU E /s, mientras que el silo de mortalidad, manejo de lodo y PTAS obtuvieron emisiones
de 246 OU E /s, 21 OU E /s y 5,3 OU E /s, respectivamente.

2. Las curvas de isoconcentración del percentil 98, indican que las concentraciones de olor

pueden alcanzar valores entre 1,0 a 22,5 OU E /m [3], presentándose la máxima
concentración, al costado Este del sistema de rotofiltros. Fuera de los límites del predio
las concentraciones alcanzan valores entre 1,0 a 3,0 OU E /m [3], abarcando un área total de
122 ha para la isodora de 1,0 OU E /m [3] .

3. El área de influencia correspondiente a la curva de 1 OU E /m [3] bajo percentil 98,

circunscribe a cinco de los diecinueve receptores considerados en la modelación,
alcanzando valores de hasta 2,78 OU E /m [3] . Es importante señalar, que dichos receptores
corresponden a viviendas y fundos.

4. En el escenario evaluado no se presenta superación del límite de 3 OU E /m [3] (percentil 98),

en ninguno de los receptores identificados. El receptor que presenta la concentración más
alta (R16) fue identificado como Fundo Pilmaiquén, ubicado al noreste de la piscicultura
con una concentración de 2,78 OU E /m [3] .

5. De acuerdo a las comparaciones realizadas al ciclo diario, al promedio mensual de los

vientos y ciclos estacionales, y estadística para los parámetros temperatura, velocidad y
dirección de viento para la estación La Unión, se puede indicar que, tanto el modelo WRF
como los datos reales observados, presentan valores y patrones similares. Lo anterior
permite concluir que los datos WRF se ajustan a la realidad y, en consecuencia, al ser
utilizados en la modelación arrojan resultados técnicamente válidos.

6. Todos los resultados presentes en este informe son válidos sólo para las condiciones y

consideraciones estipuladas en el presente informe.

Anexo F Estimación y Modelación de Olores 33 de 52

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

**Figura No 12** . Esquema funcionamiento CALPUFF.

Anexo F Estimación y Modelación de Olores 34 de 52

**Anexo No2. Análisis de receptores**

A continuación, se presentan los gráficos ciclo diario de las concentraciones de olor, para los dos
receptores que presentaron la concentración más alta (R4 y R16). Estos gráficos permiten
detectar las horas en donde ocurren las mayores concentraciones durante el día, respecto al
90% observado del tiempo (variación entre el percentil 5 y percentil 95). Los resultados de la
modelación y el análisis en los dos receptores indican que ninguno de ellos está por sobre el
límite de inmisión de 3 OU E /m [3] .

**Figura No 13** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No4.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor
durante el día. Se puede observar que los mayores valores se presentan durante la
madrugada, entre las 00:00 a 05:00 hrs. con valores de hasta 2,0 OU E /m3 en el rango del

90% observado .

**Figura No 14** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No16.

En el gráfico anterior se puede apreciar que entre las 00:00-05:00 hrs se registran las mayores
concentraciones de olor alcanzando un valor 3,2 OU E /m3 en el rango del 90% observado. Las
horas con menor concentración de olor se registran en horarios con mayor velocidad de viento
(07:00-16:00 hrs).

Anexo F Estimación y Modelación de Olores 35 de 52

**Anexo No3: Descripción meteorológica y geofísica de la zona (EM La Unión)**
En el siguiente anexo se presenta el análisis meteorológico de la zona modelada. Los datos
expresados a continuación fueron extraídos de la plataforma SINCA, correspondientes a la
estación de monitoreo La Unión.

**Tabla No 18** . Estaciones meteorológicas.

|Nombre de la Estación|Col2|EM La Unión|
|---|---|---|
|Coordenada UTM 18S,<br>Datum WGS 84|Este (m)|663.446 m E|
|Coordenada UTM 18S,<br>Datum WGS 84|Norte (m)|5.538.659 m S|
|Distancia desde el proyecto|Distancia desde el proyecto|12,8 km|
|"Periodo del registro (desde DD/MM/AA - hasta<br>DD/MM/AA)"|"Periodo del registro (desde DD/MM/AA - hasta<br>DD/MM/AA)"|01/01/2022 - 31/12/2022|
|Meteorología|Meteorología|Velocidad Viento (VV)<br>Dirección Viento (DV)<br>Temperatura (T)|

**7.3.1** **Cantidad de Datos**

Para realizar el análisis meteorológico y el análisis de incertidumbre es necesario verificar la
cantidad de datos presente en las mediciones ambientales de la estación. A continuación, se
muestran los datos de la estación en la serie de tiempo para comprobar que no existen periodos
extensos sin datos durante el año de análisis.

**Figura No 15** . Serie de tiempo velocidad de viento - datos observados estación La Unión - Año

2022.

Anexo F Estimación y Modelación de Olores 36 de 52

**Figura No 16** . Serie de tiempo dirección de viento - datos observados estación La Unión - Año

2022.

**Figura No 17** . Serie de tiempo temperatura - datos observados estación La Unión - Año 2022.

**Tabla No 19.** Datos válidos estación meteorológica La Unión.

|Porcentaje de datos meteorológicos disponibles - EM La Unión|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Pará/mes|E|F|M|A|M|J|J|A|S|O|N|D|**Total**|
|VV|100%|100%|100%|100%|100%|98%|98%|100%|100%|98%|100%|100%|99%|
|DV|100%|100%|100%|100%|100%|98%|98%|100%|100%|98%|100%|100%|99%|
|T|100%|100%|100%|100%|100%|100%|100%|100%|100%|98%|100%|100%|100%|

A partir de las gráficas de serie de tiempo de los parámetros temperatura, velocidad y dirección
de viento de la estación La Unión se evidencia que existen periodos sin datos durante los meses
de junio, julio y octubre, sin embargo estos períodos no superan el 2% del tiempo, se pueden

Anexo F Estimación y Modelación de Olores 37 de 52

observar periodos de datos del 100 % para la variable Temperatura y de 99% para las variables
velocidad y dirección de viento, valores que se encuentran sobre el límite de 75% indicado en la
Guía para modelos de calidad del aire del SEA. Por lo tanto, esta estación se puede considerar
en el análisis.

**7.3.2** **Gráficos Ciclo diario**

7.3.2.1 Velocidad de viento

En los siguientes gráficos se presenta los ciclos diarios promedios de temperatura, velocidad y
dirección del viento; junto con su variabilidad entre el percentil 5% a 95% (Rango 90%
observado).

**Figura No 18** . Ciclo diario velocidad viento - datos observados estación La Unión - Año 2022.

En relación con el ciclo diario promedio de la velocidad de viento se observa una velocidad
promedio mínima de 0,7 m/s entre las 00:00 y 06:00 horas, y una velocidad máxima promedio de
2,2 m/s entre las 15:00 y 16:00 horas. Durante el año, la velocidad del viento puede variar entre
vientos calmos y 4,99 m/s de acuerdo con el 90% observado. La velocidad de viento en dicha
zona, favorece la dispersión de emisiones.

Anexo F Estimación y Modelación de Olores 38 de 52

7.3.2.2 Dirección de viento

**Figura No 19** . Ciclo diario dirección viento - datos observados estación La Unión - Año 2022.

En relación con el ciclo diario de la dirección de viento, se observan vientos predominantes
provenientes del Sur y Suroeste entre la mañana e inicios de la tarde, con frecuencias hasta de
un 20%, principalmente entre las 08:00 y 16:00 horas. Durante la noche se observan vientos
desde el Norte y Noroeste, con frecuencias de hasta un 20% entre las 00:00 y las 03:00 horas.

7.3.2.3 Temperatura

**Figura No 20** . Ciclo diario temperatura - datos observados estación La Unión - Año 2022.

Respecto al ciclo diario de la temperatura, se observa una temperatura promedio variable entre
6°C a 16°C. La temperatura máxima ocurre entre las 14:00 a 15:00 horas, mientras que la mínima
sucede a las 05:00 horas. Durante el año la temperatura puede alcanzar máximas de 26 °C y
mínimas de -2°C, respecto al 90% observado.

Anexo F Estimación y Modelación de Olores 39 de 52

**7.3.3** **Gráficos Distribución de Vientos**

La siguiente figura muestra la distribución de vientos en la estación La Unión. De la figura se
puede concluir que los vientos de mayores velocidades ocurren en el rango de 0,5 a 2 m/s con
un 45% de la frecuencia de los vientos, seguidos de vientos calmos con un 31%. Por otro lado,
los vientos entre 2,0 y 4,0 m/s representan un 21% mientras que los vientos entre 4,0 y 6,0 m/s
representan un 4%.

**Figura No 21** . Distribución de vientos - datos observados estación La Unión - Año 2022.

Anexo F Estimación y Modelación de Olores 40 de 52

**7.3.4** **Rosa de los Vientos**

7.3.4.1 Anual

**Figura No 22** . Rosa de los vientos - datos observados estación La Unión - Año 2022.

De la rosa de los vientos se puede concluir que predominan los vientos calmos, cuya frecuencia
alcanza el 31%. Por otro lado, los vientos varían principalmente desde el Suroeste (SO) y el
Sureste, llegando a velocidades sobre los 6 m/s con frecuencias entre un 5% y un 7%. También
se observan, en menor medida, vientos desde el Norte (N) y Estenoreste (ENE), con velocidades
de hasta 4 m/s y frecuencias cercanas al 6% para ambos vientos.

Anexo F Estimación y Modelación de Olores 41 de 52

Por estación

|(a) Otoño - EM La Unión 2022|(b) Invierno - EM La Unión 2022|
|---|---|
|<br>(c) Primavera - EM La Unión 2022|<br>(d) Verano - EM La Unión 2022|

**Figura No 23** . Rosa de los vientos por estación del año.

De acuerdo con las rosas de los vientos anteriores, se puede indicar lo siguiente:

- En otoño los vientos predominantes son desde el Estenoreste (ENE), con velocidades de
hasta 4 m/s y frecuencias de un 11%. También se observan vientos desde el Suroeste (SO)
y Sursuroeste con velocidades de hasta 6 m/s y frecuencias entre un 5% y un 10%.

Anexo F Estimación y Modelación de Olores 42 de 52

En invierno los vientos predominantes varían entre vientos provenientes desde el Norte (N) y
el Este (E), con vientos de hasta 6 m/s, y frecuencias por sobre un 6%. A su vez, se pueden
observar vientos desde el Nornoreste (NNE) con velocidades de hasta 6 m/s y frecuencias

de hasta un 6%.

Para la estación de primavera los vientos predominantes son principalmente desde el Sureste
(SE) y Sursureste (SSE), alcanzado los 6 m/s y frecuencias de un 17% y un 13%
respectivamente. En menor medida, se observan vientos desde el Oeste noroeste (ONO),
con velocidades de 4 m/s y una frecuencia de un 7%.

En la estación de verano, se observan vientos predominantes desde el Sursuroeste (SSO) y
Suroeste (SO) mayoritariamente, con velocidades de hasta 8 m/s con frecuencias de un 17%
para vientos SSO y velocidades de hasta 6 m/s y frecuencias cercanas al 15% para los
vientos provenientes desde el SO. En menor medida se observan vientos desde el SE, con
velocidades de hasta 8 m/s y frecuencias de un 6%.

**7.3.5** **Ciclo estacional**

En la figura a continuación se observa la variación estacional de los ciclos de velocidad y
dirección de viento. Para los datos observados, en relación a la dirección de viento en los meses
de primavera, se mantiene el ciclo diario con vientos desde el sur y sureste durante la mañana y
la tarde, variando desde el Suroeste principalmente por la noche. Durante el verano, los vientos
predominan desde el Suroeste durante la mañana y la tarde, variando desde el norte y noroeste
por la noche.

Por otro lado, durante los meses otoño los vientos varían entre el sur y norte debido a los
periodos de inestabilidad. Lo anterior indica que la dispersión de contaminantes varía entre el sur
y norte en los meses de invierno.

Respecto a la velocidad del viento, durante las horas del día en primavera y verano ocurren las
mayores velocidades, entre 2,0 a 4,0 m/s mientras que en la noche desciende a vientos calmos
y de hasta 2 m/s. En los meses de invierno las velocidades también varían durante el día
alcanzando un máximo de 2 m/s en las horas de la tarde para luego disminuir a 0,5 m/s durante
la noche y la mañana.

Anexo F Estimación y Modelación de Olores 43 de 52

**Figura No 24** . Ciclos estacionales - datos observados estación La Unión - Año 2022.

**7.3.6** **Elevación de Terreno**

La zona modelada corresponde a un sector ubicado en el territorio de Chile correspondiente a la
zona sur, comuna de San Pablo, Provincia de Osorno, Región de los Lagos. El Proyecto se
emplazará en un terreno privado al interior del Fundo conocido como Pilmaiquén II. La ubicación
de la planta se encuentra a niveles donde se observan elevaciones de terreno que van de 0 a 30
metros, no obstante, el sector está rodeado de relieve con alturas desde los 100 a 342 msnm.

Anexo F Estimación y Modelación de Olores 44 de 52

**Figura No 25** . Elevación de terreno archivo WRF.

Anexo F Estimación y Modelación de Olores 45 de 52

**Anexo No4. Análisis de incertidumbre. Comparación entre la meteorología de**

**pronóstico y los datos observados en la estación meteorológica (EM La Unión).**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 6” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para ello
se utilizan los datos disponibles en las estaciones de monitoreo ubicadas en la zona de interés
para el estudio.

La estación de monitoreo más cercanas al proyecto se encuentra a 12,8 km en la ciudad de La
Unión (hacia el noroeste de la piscicultura) y pertenece al sistema SINCA. Los parámetros
monitoreados por dicha estación corresponden a velocidad, dirección de viento y temperatura.
Para la evaluación del desempeño se realiza una comparación entre las variables temperatura,
velocidad y dirección de viento, ya que éstas son las variables de mayor interés.

Con el fin de evaluar el desempeño, se realiza un análisis cualitativo de los parámetros de interés.
El análisis cualitativo se desarrolla mediante la comparación entre los ciclos diarios promedios,
mensuales, ciclos estacionales y rosa de los vientos.

Definiciones:

Datos observados: Se refiere a los datos provenientes desde una estación de monitoreo durante
un periodo de interés.

Datos modelados: Se refiere a los datos meteorológicos provenientes desde un modelo de
pronóstico como WRF o MM5.

Rango 90% observado: Se refiere a la variación de los datos entre el percentil 5 y percentil 95 de
éstos

**7.4.1** **Ciclos diarios promedios**

7.4.1.1 Velocidad de Viento

Del siguiente gráfico se puede concluir que el ciclo diario promedio de velocidad de viento entre
los datos modelados y los observados presentan una diferencia promedio de ± 0,9 m/s. La mayor
diferencia se observa a las en la noche, entre las 23:00 horas y las 03:00 horas con 1,1 m/s. La
variación diaria de velocidad posee el mismo patrón entre el modelo de pronóstico y el observado,
con una leve sobreestimación por parte de los datos modelados.

Anexo F Estimación y Modelación de Olores 46 de 52

**Figura No 26** . Comparación ciclo diario de velocidad de viento entre los datos observados y

proyectados para la estación La Unión.

7.4.1.2 Dirección de Viento

En los siguientes gráficos se presenta el ciclo diario de dirección de viento, para la estación La
Unión, aquí se puede apreciar que los datos observados y los datos modelados presentan
valores con leves variaciones en las frecuencias. Se pueden observar que en ambos casos los
vientos desde el Sur con variantes entre Sureste y Suroeste predominan durante el día,
alcanzado frecuencias de hasta un 40% en los datos modelados y 30% en los observados. En
los datos modelados se pueden observar vientos desde el Sur durante todo el día, mientras que,
en los datos observados los vientos Norte se aprecian mayoritariamente en la noche y
madrugada.

**Figura No 27** . Ciclo diario de dirección de viento datos observados para la estación La Unión.

Anexo F Estimación y Modelación de Olores 47 de 52

7.4.1.3 Temperatura

De la siguiente figura, se puede concluir que los ciclos diarios promedios de temperatura entre
los datos observados y los datos modelados presentan valores similares con una diferencia
promedio de ± 0,8°C, la mayor diferencia se observa entre las 17:00 y las 18:00 horas con 1,9°C.
Además, la variación diaria de temperatura posee el mismo patrón del modelo de pronóstico y el
observado. Dado estas circunstancias, respecto al ciclo diario promedio de temperatura, el
modelo es adecuado.

**Figura No 28.** Comparación ciclo diario de temperatura entre los datos observados y

proyectados para la estación La Unión.

**7.4.2** **Promedio Mensual**

7.4.2.1 Velocidad de Viento

De la figura a continuación, se puede concluir que el promedio mensual de velocidad de viento
entre los datos observados y los datos modelados presenta valores similares con una diferencia
promedio de ± 0,9 m/s, con una diferencia máxima de 1,7 m/s el mes de julio. La variación
mensual de velocidad posee un patrón similar entre el modelo de pronóstico y el observado.
Dado estas circunstancias, respecto al promedio mensual de velocidad, el modelo es adecuado.

Anexo F Estimación y Modelación de Olores 48 de 52

**Figura No 29.** Comparación ciclo mensual de velocidad de viento entre los datos observados y

proyectados para la estación La Unión.

7.4.2.2 Dirección de Viento

De la siguiente figura, se puede concluir que el promedio mensual de dirección de viento entre
los datos observados y los modelados presenta valores similares con diferencias puntuales. Se
observa que en los datos modelados los vientos Sur (S) se mantienen durante todo el año,
alcanzado frecuencias de hasta un 50% en febrero, en el caso de los datos observados, los
vientos predominantes provienen desde el Suroeste (SO), se observan mayormente en la
estacion de verano, alcanzado frecuencias de un 50% en febrero. También se observa que los
datos observados poseen variaciones de vientos durante el invierno, con un comportamiento
similar a los datos modelados, donde existe una variación entre vientos provenientes desde el
Norte y el Sur.

Anexo F Estimación y Modelación de Olores 49 de 52

**Figura No 30.** Comparación ciclo mensual de dirección de viento entre los datos observados y

proyectados para la estación La Unión.

7.4.2.3 Temperatura

De la siguiente figura se puede concluir que los promedios mensuales de temperatura entre los
datos observados y los datos modelados presentan valores similares para la estación La Unión,
la diferencia promedio es de ±1,0°C, alcanzando la mayor diferencia el mes de noviembre con
2,5°C. La variación entre los datos modelados y observados presenta un patrón similar,
aumentando las temperaturas en primavera y verano, y disminuyendo en otoño e invierno.

Anexo F Estimación y Modelación de Olores 50 de 52

**Figura No 31.** Comparación ciclo mensual de temperatura entre los datos observados y

proyectados para la estación La Unión.

**7.4.3** **Rosas de los vientos**

De la rosa de los vientos mostrada, se puede observar que los vientos con velocidades superiores
a 6 m/s predominan desde el Norte tanto en los datos observados como en los datos modelados.
Por otro lado, para los datos modelados se puede ver una alta frecuencia de vientos provenientes
desde el Sur, superando el 15% de los datos, a diferencia de los datos observados, que poseen
frecuencias cercanas al 5%. Dada la similitud cualitativa de las rosas de los vientos, se considera

el modelo adecuado.

**Figura No 32.** Comparación rosa de los vientos entre los datos observados y proyectados para

la estación La Unión.

Anexo F Estimación y Modelación de Olores 51 de 52

**7.4.4** **Análisis Cuantitativo**

De acuerdo con lo solicitado por la Guía para uso de modelos de calidad del aire en el SEIA, se
presenta el análisis cuantitativo de las variables meteorológicas involucradas en la modelación.

**Tabla No 20.** Análisis cuantitativo.

|Parámetro|Métrica|EM La Unión|Col4|Condición|
|---|---|---|---|---|
|**Parámetro**|**Métrica**|**Horario**|**Diario**|**Diario**|
|**Velocidad**|**BIAS**|0,9|0,94|[-2,5;2,5] m/s|
|**Velocidad**|**MAE**|1,26|1,02|<=3 m/s|
|**Velocidad**|**RMSE**|1,76|1,41|<= 3,5 m/s|
|**Temperatura**|**BIAS**|-0,84|-0,84|[-4;4] °C|
|**Temperatura**|**MAE**|1,77|1,26|<= 4 °C|
|**Temperatura**|**RMSE**|2,35|1,70|<= 4,5 °C|

**Conclusión**

Se puede concluir a partir del análisis cualitativo (ciclo diario, promedio mensual, rosa de los
vientos y ciclos estacionales) y cuantitativo que los datos de pronóstico WRF y datos observados
presentan valores similares para las direcciones frecuentes, velocidades de vientos y
temperatura ambiente. De acuerdo con lo presentado en el análisis de la estación La Unión, el
modelo WRF utilizado en la dispersión atmosférica es adecuado y concuerda con las condiciones
de la realidad.

**Cabe señalar que el archivo meteorológico WRF 2022 y los archivos del modelo fueron**
**cargados mediante link de archivos de gran tamaño. El comprobante de la carga es**
**adjuntado en el Apéndice 2 del presente documento.**

Anexo F Estimación y Modelación de Olores 52 de 52