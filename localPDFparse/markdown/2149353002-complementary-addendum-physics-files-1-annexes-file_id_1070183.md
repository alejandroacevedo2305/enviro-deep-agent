---
title: Sin título
author: gburgos
date: D:20210525123225-04'00
language: es
type: report
pages: 63
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 1 de 62
-->

Anexo 3

Estudio de impacto odorante

Adenda Complementaria Equipos de

Satinado Cristalerías de Chile Llay-Llay

Región de Valparaíso

Mayo, 2021

Elaborado por:

**Gestión Ambiental Consultores S.A.**

General del Canto 421 Piso 6, Providencia

Fono: +56 2 2719 5600

www.gac.cl

**INFORME**

**Estudio de Impacto Odorante:**
**“Equipos de Satinado Cristalerías**

**de Chile Llay-Llay”.**

**24 de mayo del 2021**

**Inf01E01.O-21-024**

# Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 1 de 62

**Datos del Proyecto**

**Empresa** **:** Cristal Chile.

**Coordinador** **:** Camila Figueroa Aguilar (Cristal Chile).
Carla Carrasco Benavente (Cristal Chile).

**Subgerente Ing. En olores:** Miguel Gatica Rivera (MGR).

**Jefe de Proyecto** **:** Claudio Burdiles Melgarejo (CBM).

**Ingeniero de Proyecto** **:** Carolina Freire Ávila (CFA).

**Fecha** **:** 24 de mayo del 2021.

|Emisión|Datos|Preparó|Revisó|Aprobó|
|---|---|---|---|---|
|Rev.A. Para<br>Revisión Cliente|Nombre|CFA|CBM|CBM|
|Rev.A. Para<br>Revisión Cliente|Fecha|24-05-2021|24-05-2021|24-05-2021|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 2 de 62

**Índice General**

**1** **Resumen ............................................................................................................................. 6**

**2** **Introducción ..................................................................................................................... 13**

**3** **Objetivo General .............................................................................................................. 14**

Objetivos específicos .................................................................................................. 14
**4** **Metodología ...................................................................................................................... 15**

Caracterización de la fuente generadora de olor y amoniaco ...................................... 15
Estimación de las emisiones ....................................................................................... 15

Evaluación de la dispersión de las emisiones de olor. ................................................. 16

4.3.1 Selección del modelo ....................................................................................... 16

4.3.2 Recopilación de los antecedentes para la modelación ..................................... 17

4.3.3 Variables meteorológicas y geofísicas ............................................................. 17

4.3.4 Evaluación de los resultados ........................................................................... 18

4.3.5 Área de Influencia y receptores de interés. ...................................................... 20

Evaluación del desempeño del archivo de pronóstico utilizado ................................... 21
**5** **Resultados ....................................................................................................................... 21**

Caracterización de las fuentes de emisión .................................................................. 21

Emisiones ................................................................................................................... 26

5.2.1 Emisión de olor ................................................................................................ 26

5.2.2 Emisión de amoniaco ....................................................................................... 27

Evaluación de la dispersión de olor ............................................................................. 28
Evaluación de la dispersión de amoniaco .................................................................... 32

5.4.1 Resultados emisión de amoniaco .................................................................... 33

Análisis del desempeño del archivo de pronóstico utilizado ........................................ 40
**6** **Conclusiones ................................................................................................................... 42**

**7** **Anexos .............................................................................................................................. 44**

Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación ............ 44
Anexo No2. Descripción meteorológica y geofísica de la zona .................................... 45

7.2.1 Cantidad de datos ............................................................................................ 45

7.2.2 Gráficos Ciclo diario ......................................................................................... 47

7.2.3 Gráficos Distribución de Vientos ...................................................................... 50

7.2.4 Rosa de los vientos ......................................................................................... 51

7.2.5 Gráficos ciclo estacional .................................................................................. 53

7.2.6 Elevación de Terreno ....................................................................................... 55

Anexo No3. Análisis incertidumbre .............................................................................. 56

7.3.1 Ciclos Diarios promedios ................................................................................. 57

7.3.2 Promedio Mensuales ....................................................................................... 59

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 3 de 62

7.3.3 Dirección de viento .......................................................................................... 61

7.3.4 Análisis cuantitativo ......................................................................................... 62

**Índice de Tablas**

**Tabla No 1** . Emisiones del contenedor de lodos. ...................................................................... 7
**Tabla No 2** . Concentraciones en receptores. .......................................................................... 12
**Tabla No 3** . Variables de entrada consideradas en la modelación. ......................................... 17
**Tabla No 4.** Características del archivo meteorológico WRF. ................................................. 18
**Tabla No 5** . Límites de inmisión según Guía UK (Versión 1.1, 2018), para el percentil 98. ..... 19
**Tabla No 6** . Límites máximos para amoniaco. ........................................................................ 20
**Tabla No 7** . Estándares para amoniaco. ................................................................................. 20
**Tabla No 8** . Factores de emisión para olores/línea de lodo/sistema de pre-deshidratado. ...... 26
**Tabla No 9.** Emisión de olor contenedor de lodos. .................................................................. 26
**Tabla No 10.** Emisión de amoniaco contenedor de lodos. ...................................................... 28
**Tabla No 11** . Máxima concentración. ...................................................................................... 30
**Tabla No 12** . Receptores considerados en la modelación. ..................................................... 30
**Tabla No 13** . Concentración receptores. Percentil 98. ............................................................ 31
**Tabla No 14.** Protocolo FIDOL con base a receptores definidos. ............................................ 32
**Tabla No 15** . Máxima concentración. ...................................................................................... 34

**Tabla No 16** . Máxima concentración. ...................................................................................... 35
**Tabla No 17** . Máxima concentración. ...................................................................................... 37
**Tabla No 18** . Máxima concentración. ...................................................................................... 38
**Tabla No 19** . Concentración en receptores. ............................................................................ 39
**Tabla No 20** . Concentración en receptores. ............................................................................ 39
**Tabla No 21.** Datos estaciones meteorológicas consideradas. ............................................... 45
**Tabla No 22.** Datos válidos estación meteorológica Catemu. ................................................. 46
**Tabla No 23.** Datos válidos estación meteorológica Romeral. ................................................ 47
**Tabla No 24.** Análisis cuantitativo. .......................................................................................... 62

**Índice de Figuras**

**Figura No 1** . Mapa de concentración de olor (Percentil 98). ..................................................... 8
**Figura No 2** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (15 min). .................................................................................... 9
**Figura No 3** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (30 min). .................................................................................. 10
**Figura No 4** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (8 horas). ................................................................................. 11
**Figura No 5** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (24 horas). ............................................................................... 12
**Figura No 6** . Área del estudio de impacto odorante. ............................................................... 14
**Figura No 7** . Esquema resumen de las metodologías para estimar las emisiones de olor. ..... 16
**Figura No 8** . Diagrama de Proceso Satinado. ........................................................................ 22
**Figura No 9** . Diagrama de Procesos Planta de Tratamiento de RILes. ................................... 23
**Figura No 10** . Diagrama de Flujo generación de lodos. .......................................................... 24
**Figura No 11** . Fuentes consideradas para modelación. .......................................................... 25
**Figura No 12** . Mapa de concentración de olor generado por las fuentes de emisión de la
planta. Promedio horario (percentil 98). .................................................................................. 29

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 4 de 62

**Figura No 13** . Receptores de interés analizados. ................................................................... 31
**Figura No 14** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (15 min). .................................................................................. 34
**Figura No 15** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (30 min). .................................................................................. 35
**Figura No 16** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (8 horas). ................................................................................. 37
**Figura No 17** . Mapa de concentración de amoniaco generado por el contenedor de lodos.
Concentración máxima anual (24 horas). ............................................................................... 38
**Figura No 18** . Estaciones Meteorológicas utilizadas en el Análisis de Incertidumbre. ............. 41
**Figura No 19** . Esquema funcionamiento CALPUFF ................................................................ 44
**Figura No 20.** Serie de tiempo velocidad de viento - datos observados estación Catemu- año
2020. ...................................................................................................................................... 45
**Figura No 21.** Serie de tiempo dirección de viento - datos observados estación Catemu - año
2020. ...................................................................................................................................... 46
**Figura No 22.** Serie de tiempo velocidad de viento - datos observados estación Romeral- año
2020. ...................................................................................................................................... 46
**Figura No 23.** Serie de tiempo dirección de viento - datos observados estación Romeral - año
2020. ...................................................................................................................................... 47
**Figura No 24.** Ciclo diario para velocidad de viento Estación Catemu. ................................... 48
**Figura No 25.** Ciclo diario para velocidad de viento Estación Romeral. .................................. 48
**Figura No 26.** Ciclo diario para dirección de viento estación Catemu. .................................... 49
**Figura No 27.** Ciclo diario para dirección de viento estación Romeral. ................................... 49
**Figura No 28.** Distribución velocidades de viento estación Catemu. ....................................... 50
**Figura No 29.** Distribución velocidades de viento estación Romeral. ...................................... 50
**Figura No 30.** Rosa de los vientos Anual. Estación Catemu. .................................................. 51
**Figura No 31.** Rosa de los vientos Anual. Estación Romeral. ................................................. 51
**Figura No 32.** Rosa de los vientos por estación del año. ........................................................ 53
**Figura No 33.** Ciclos estacionales - datos observados estación Catemu - Año 2020. ........... 54
**Figura No 34.** Ciclos estacionales - datos observados estación Romeral - Año 2020. .......... 54
**Figura No 35.** Elevación de terreno archivo WRF. .................................................................. 55
**Figura No 36.** Comparación ciclo diario de velocidad de viento entre datos observados y
proyectados para la estación de Catemu. ............................................................................... 57
**Figura No 37.** Comparación ciclo diario de velocidad de viento entre datos observados y
proyectados para la estación de Romeral. .............................................................................. 57
**Figura No 38.** Comparación ciclo diario de dirección de viento entre datos observados y
proyectados para la estación de Catemu. ............................................................................... 58
**Figura No 39.** Comparación ciclo diario de dirección de viento entre datos observados y
proyectados para la estación de Romeral. .............................................................................. 58
**Figura No 40.** Comparación moda mensual de velocidad de viento entre datos observados y
proyectados para la estación de Catemu. ............................................................................... 59
**Figura No 41.** Comparación moda mensual de velocidad de viento entre datos observados y
proyectados para la estación de Romeral. .............................................................................. 59
**Figura No 42.** Comparación moda mensual de dirección de viento entre datos observados y
proyectados para la estación de Catemu. ............................................................................... 60
**Figura No 43.** Comparación moda mensual de dirección de viento entre datos observados y
proyectados para la estación de Romeral. .............................................................................. 60
**Figura No 44.** Comparación Rosas de viento. ........................................................................ 61

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 5 de 62

**1** **Resumen**

Cristal Chile, solicitó los servicios de Proterm S.A para llevar a cabo un Estudio de Impacto
Odorante en el marco de la presentación al servicio de evaluación ambiental de la DIA “Equipos
de Satinado Cristalerías de Chile Llay Llay”. El presente estudio tiene como objetivo determinar
y/o descartar posible afectación a la calidad de vida de las personas, producto de la operación
de los equipos de satinado en la planta Cristal Chile, ubicada en la comuna de Llay Llay, región
de Valparaíso.

El proyecto consiste en la instalación y operación de dos máquinas para el satinado de botellas,
que darán un acabado de tipo opaco a las botellas mediante la aplicación de soluciones en un
proceso de saponificación. Estas máquinas reciben una parte de las botellas fabricadas en
planta Llay Llay, sin alterar de forma alguna los procesos de fabricación. La capacidad de cada
máquina de satinado es de 3.500 botellas/hora. Los líquidos provenientes del proceso serán
neutralizados en un equipo de tratamiento de efluentes de satinado, descargando al
alcantarillado.

Para evaluar los efectos de las emisiones de la planta se realiza una modelación de dispersión
de olor y amoniaco. Para calcular las emisiones de olor del contenedor de lodos se utilizó el
factor de emisión propuesto en el Informe Final “Servicio de recopilación y sistematización de
factores de emisión al aire para el Servicio de Evaluación Ambiental” realizado en mayo de
2015. En este estudio se indican factores de emisión para olores/línea de lodos/sistema de predeshidratado para el manejo de aguas residuales la que incluye residuos industriales líquidos.
Es importante señalar que para efectos de la modelación se consideró el factor más
conservador, establecido para lodo mezclado (8 OU E /m [2] /s). Por otro lado, para calcular las
emisiones de amoniaco se realizó una simulación de la tasa de evaporación y generación de
amoniaco en el contenedor de lodos considerando un contenedor hermético de 15 m [3], humedad
del lodo de 30%, pH neutro, temperatura de 25°C, 5% de disolución de amonio en agua y se
asume apertura diaria del contenedor de lodos (15 m [3] ).

A continuación, se presenta la estimación de emisiones de olor y amoniaco del contenedor de
lodos:

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 6 de 62

**Tabla No 1** . Emisiones del contenedor de lodos.

|Fuente|Emisión<br>De olor<br>(OU /s)<br>E|Emisión de<br>NH<br>3<br>(g/s)|
|---|---|---|
|Contenedor de lodos|101,2|1,40E-06|

Una vez obtenidas las emisiones del contenedor de lodos, se ingresaron a un modelo de
dispersión atmosférica calpuff para obtener las concentraciones de inmisión. Los resultados de
las concentraciones de olor (OU E /m [3] ) arrojadas por el modelo de dispersión fueron comparadas
con el límite 1,5 OU E /m [3] establecido en la Guía UK, mientras que las concentraciones de
amoniaco fueron comparadas con el límite permisible temporal y ponderado establecido en el
DS N° 594 y los estándares de media hora y de 24 horas definidos en la norma Ontario de
Canadá.

En la Figura N°1, se puede observar que la distribución de la pluma de olor se acentúa hacia el
sureste con una longitud aproximada de 0,16 km en dirección noroeste-sureste. Las isodoras
graficadas pueden alcanzar valores entre 0,01 a 0,23 OU E /m [3], alcanzando su mayor
concentración al sureste del contenedor de lodos, alcanzando las 0,23 OU E /m [3] ; concentración
que se encuentra bajo el límite establecido en la Guía UK (1,5 OU E /m [3] ) y bajo 1 OU E /m [3], por lo
que no se genera un área de influencia. Es importante señalar que la pluma se desplaza dentro
del límite de Cristal Chile, por lo que los receptores no se verían afectados por la emisión de
olor.

Tal como se puede apreciar en la Figura N°2, la distribución de la pluma que presenta las
concentraciones máximas en periodos de 15 min, se distribuye en sentido noroeste y sureste
con una longitud aproximada de 0,34 km. Las isodoras graficadas pueden alcanzar valores
entre 0,003 y 0,053 μg /m [3], alcanzando su mayor concentración al suroeste del contenedor de
lodos, alcanzando 0,053 μg /m [3] . Es importante señalar que, las concentraciones de amoniaco
no superan el límite permisible temporal de 24.000 μg /m [3] establecido en el DS N°594.

En la Figura N°3, se presenta la distribución de la pluma con las concentraciones máximas en
periodos de 30 min, la que se distribuye en sentido noroeste y sureste con una longitud
aproximada de 0,22 km. Las isodoras graficadas pueden alcanzar valores entre 0,005 y 0,0436
μg /m [3], alcanzando su mayor concentración al suroeste del contenedor de lodos, alcanzando
0,0436 μg /m [3] . Es importante señalar que, las concentraciones de amoniaco no superan el
límite de 300 μg /m [3] establecido en la norma Ontario de Canadá.

Tal como se puede apreciar en la Figura N°4, la distribución de la pluma que presenta las
concentraciones máximas en periodos de 8 horas, la que se distribuye en sentido noroeste y
sureste con una longitud aproximada de 0,23 km. Las isodoras graficadas pueden alcanzar
valores entre 0,0005 y 0,0045 μg /m [3], alcanzando su mayor concentración al suroeste del
contenedor de lodos, alcanzando 0,0045 μg /m [3] . Es importante señalar que, las
concentraciones de amoniaco no superan el límite permisible ponderado de 15.000 μg /m [3]
establecido en el DS N°594.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 7 de 62

Finalmente, en la Figura N°5, se presenta la distribución de la pluma con las concentraciones
máximas en periodos de 24 horas, la que se distribuye en sentido noroeste y sureste con una
longitud aproximada de 0,31 km. Las isodoras graficadas pueden alcanzar valores entre 0,0001
y 0,0015 μg /m [3], alcanzando su mayor concentración al suroeste del contenedor de lodos,
alcanzando 0,0015 μg /m [3] . Es importante señalar que, las concentraciones de amoniaco no
superan el límite de 100 μg /m [3] establecido en la norma Ontario de Canadá.

Tal como se muestra en las siguientes cartografías, la pluma de dispersión del amoniaco se
desplaza dentro y fuera del límite predial, a pesar de lo anteriormente señalado, ninguno de los
receptores considerados en la modelación, se verá afectado por la emisión de olor y tampoco
de amoniaco.

**Figura No 1** . Mapa de concentración de olor (Percentil 98).

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 8 de 62

**Figura No 2** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (15 min).

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 9 de 62

**Figura No 3** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (30 min).

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 10 de 62

**Figura No 4** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (8 horas).

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 11 de 62

**Figura No 5** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (24 horas).

A continuación, se presentan las concentraciones de inmisión de olor y de amoniaco en cada
receptor:

**Tabla No 2** . Concentraciones en receptores.

|No|Concentración<br>de inmisión<br>(OU /m3)<br>E|Concentración de amoniaco|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**No**|**Concentración**<br>**de inmisión**<br>** (OUE/m3) **|**Periodo**<br>**15 min**<br>**(**μg/m3**) **|**Periodo**<br>** 30 min**<br>**(**μg/m3**) **|**Periodo**<br>** 8 horas**<br>**(**μg/m3**) **|**Periodo**<br>** 24 horas**<br>**(**μg/m3**) **|
|**No**|**Límite norma**<br>**1,5 OUE/m3 **|**Límite norma**<br>**15.000**μg/m3|**Límite norma**<br>**300**μg/m3|**Límite norma**<br>**24.000**μg/m3|**Límite norma**<br>**100**μg/m3|
|R1|1,32E-06|0,0017|0,0014|0,00015|0,000049|
|R2|1,41E-06|0,0010|0,0008|0,00009|0,000029|
|R3|1,47E-06|0,0016|0,0013|0,00014|0,000047|
|R4|1,36E-06|0,0017|0,0014|0,00015|0,000049|
|R5|1,33E-06|0,0017|0,0014|0,00015|0,000049|
|R6|1,35E-06|0,0017|0,0014|0,00015|0,000049|
|R7|1,40E-06|0,0017|0,0014|0,00014|0,000048|
|R8|1,42E-03|0,0014|0,0012|0,00012|0,000040|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 12 de 62

|No|Concentración<br>de inmisión<br>(OU /m3)<br>E|Concentración de amoniaco|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**No**|**Concentración**<br>**de inmisión**<br>** (OUE/m3) **|**Periodo**<br>**15 min**<br>**(**μg/m3**) **|**Periodo**<br>** 30 min**<br>**(**μg/m3**) **|**Periodo**<br>** 8 horas**<br>**(**μg/m3**) **|**Periodo**<br>** 24 horas**<br>**(**μg/m3**) **|
|**No**|**Límite norma**<br>**1,5 OUE/m3 **|**Límite norma**<br>**15.000**μg/m3|**Límite norma**<br>**300**μg/m3|**Límite norma**<br>**24.000**μg/m3|**Límite norma**<br>**100**μg/m3|
|R9|1,29E-03|0,0013|0,0011|0,00011|0,000037|
|R10|4,76E-04|0,0015|0,0012|0,00013|0,000043|
|R11|1,98E-04|0,0007|0,0006|0,00006|0,000021|
|R12|1,50E-06|0,0005|0,0004|0,00004|0,000014|
|R13|1,38E-06|0,0002|0,0002|0,00002|0,000005|
|R14|1,42E-06|0,0002|0,0001|0,00001|0,000005|
|R15|1,41E-06|0,0004|0,0003|0,00004|0,000012|

Los resultados entregados en el presente informe corresponden a los máximos valores
determinados en el modelo, por lo que el resto de las horas del año presentan valores inferiores
a los indicados.

**2** **Introducción**

Cristal Chile, solicitó los servicios de Proterm S.A para llevar a cabo un Estudio de Impacto
Odorante en el marco de la presentación al servicio de evaluación ambiental de la DIA “Equipos
de Satinado Cristalerías de Chile Llay Llay”. El presente estudio tiene como objetivo determinar
y/o descartar posible afectación a la calidad de vida de las personas, producto de la operación
de los equipos de satinado en la planta Cristal Chile, ubicada en la comuna de Llay Llay, región
de Valparaíso.

El proyecto consiste en la instalación y operación de dos máquinas para el satinado de botellas,
que darán un acabado de tipo opaco a las botellas mediante la aplicación de soluciones en un
proceso de saponificación. Estas máquinas reciben una parte de las botellas fabricadas en
planta Llay Llay, sin alterar de forma alguna los procesos de fabricación. La capacidad de cada
máquina de satinado es de 3.500 botellas/hora. Los líquidos provenientes del proceso serán
neutralizados en un equipo de tratamiento de efluentes de satinado, descargando al
alcantarillado.

A continuación, se detalla la ubicación espacial del área de estudio considerada para el estudio
de impacto odorante.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 13 de 62

**Figura No 6** . Área del estudio de impacto odorante.

El presente informe evalúa la dispersión de las emisiones de olor y de amoniaco generadas en

el contenedor de lodos.

**3** **Objetivo General**

Evaluar las emisiones de olor y de amoniaco generadas por el contenedor de lodos de Cristal
Chile, sobre la salud de la población cercana, sistema de vida, costumbres, población protegida
y turismo.

**Objetivos específicos**

 Estimar la tasa de emisión de olor y amoniaco generada por el contenedor de lodos de
Cristal Chile.

 Determinar la dispersión de las emisiones de olor y amoniaco generadas por el
contenedor de lodos de Cristal Chile.

 Comparar los valores de concentración de inmisión de olor, con normas de referencia
internacionales.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 14 de 62

**4** **Metodología**

A continuación, se presenta la metodología utilizada que permitió evaluar el efecto de las
emisiones de olor y de amoniaco generadas por el contenedor de lodos.

**Caracterización de la fuente generadora de olor y amoniaco**

Para poder caracterizar la fuente generadora de olor y amoniaco, se utilizó la siguiente
metodología:

 Revisión bibliográfica: Para poder caracterizar la fuente generadora de olor y amoniaco,
fue necesario revisar la Declaración de Impacto Ambiental “Equipos de Satinado
Cristalerías de Chile Llay Llay”, ingresada el 15 de diciembre de 2020. Específicamente
el Anexo 2 “Ingeniería básica planta de satinado” y el Anexo 9 “Plan de manejo de
lodos”, ambos presentados en la Adenda a la DIA Equipos de Satinado Cristalerías de
Chile Llay-Llay (abril, 2021).

°

 - DS N 594/2000: Aprueba Reglamento sobre las condiciones Sanitarias y
Ambientales básicas en los lugares de trabajo.

 - O.Reg 419/05: Contaminación del aire - Calidad del aire local.

 - Detección satelital: mediante Google Earth Pro [1], se identificó la superficie del
contenedor de lodos y la ubicación de los receptores.

 - Solicitud de información al cliente: donde se especificaban las horas en que se abriría
el contenedor de lodos; por otro lado se solicitaron los receptores que se consideraron
en la modelación.

**Estimación de las emisiones**

Para conocer las emisiones del “Proyecto” se utilizaron Factores de Emisión.

**Factores de emisión de olor (OEF)** : son análogos a los factores de emisión desarrollados por
la US EPA para otros contaminantes. Se utiliza la siguiente ecuación:

OER= A∗OEF

Donde OER es la tasa de emisión de olor en (OU E /s), A es el nivel de actividad, OEF es el factor
de emisión.

1 Versión 7.1.5.1557 de Google Earth.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 15 de 62

**Figura No 7** . Esquema resumen de las metodologías para estimar las emisiones de olor.

**Factores de emisión amoniaco:** Para calcular la emisión de amoniaco se utilizó la siguiente
ecuación:

E A = FE ∗F ∗A
**Dónde:**
E A : Emisión de amoniaco
FE: Factor de emisión
F: Flujo (30 m/h)
A: Área (m [2] )

**Evaluación de la dispersión de las emisiones de olor.**

Para evaluar la dispersión atmosférica de las emisiones de olor generadas por las fuentes, se
realizaron las siguientes actividades.

**4.3.1 Selección del modelo**

Para seleccionar el modelo se consideraron los lineamientos que establece la Guía para el uso
de modelos de calidad del aire en el SEIA, publicada por el Servicio de Evaluación Ambiental
el año 2012.

Se consideró un modelo tipo Puff, el cual es una combinación entre los modelos Gaussiano y
Lagrangiano, en el sentido que esencialmente calculan la dispersión de gases provenientes de
una emisión instantánea, llamada “Puff”, a lo largo de una trayectoria. Su aproximación
matemática consiste en estimar la dispersión en forma Gaussiana en cada punto de una
trayectoria. Es decir, a diferencia de los modelos Lagrangianos que necesitan el cálculo de un
gran número de trayectorias para una fuente, los modelos tipo “Puff” sólo requieren una
trayectoria por “Puff”, lo que hace su cálculo mucho más rápido [2] .

Para la modelación se utilizó el software Calpuff versión 7.2.1 junto a los módulos CALPOST
7.1.0. y CALRANK 7.0.0. Además, para efectos de la interacción gráfica de los módulos, se usó
el software interactivo CALPUFF View 8.5.0.

2 Guía para el uso de modelos de calidad del aire, 2012

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 16 de 62

En el Anexo N°1 se presenta el esquema del modelo utilizado y los elementos de la modelación.

**4.3.2** **Recopilación de los antecedentes para la modelación**

Para conocer la dispersión que tendrán los gases en un área determinada es preciso incorporar
en el modelo seleccionando distintos parámetros de manera que la simulación sea lo más
parecida a las condiciones reales. Las variables o entradas que requirió el modelo se detallan
a continuación.

**Tabla No 3** . Variables de entrada consideradas en la modelación.

|Variable|Parámetros|Fuente|
|---|---|---|
|Meteorológicas|Dirección de Viento|Tal como lo establece la guía, el modelo<br>numérico recomendado para la generación de<br>datos meteorológicos es el Weather Research<br>and Forecasting Model (WRF). WRF es uno de<br>los modelos meteorológicos de pronóstico más<br>avanzados y completos que es mantenido por<br>NCAR/NOAA de Estados Unidos.|
|Meteorológicas|Velocidad de Viento|Velocidad de Viento|
|Meteorológicas|Temperatura|Temperatura|
|Meteorológicas|Presión|Presión|
|Meteorológicas|Precipitación|Precipitación|
|Geofísicas|Elevación del Terreno|Elevación del Terreno|
|Geofísicas|Uso de Suelo|Uso de Suelo|
|Características<br>de la fuente|Descripción del proceso|Información de fuentes consideradas en el<br>escenario evaluado.|
|Características<br>de la fuente|Emisiones de olor|Emisiones de olor|
|Características<br>de la fuente|Periodo de operación|Periodo de operación|
|Características<br>de la fuente|Temperatura de los gases|Temperatura de los gases|
|Características<br>de la fuente|Ubicación de las fuentes|Ubicación de las fuentes|
|Características<br>de la fuente|Velocidad de salida de los<br>gases|Velocidad de salida de los<br>gases|
|Receptores<br>Discretos|Coordenadas de los receptores|Los receptores utilizados fueron proporcionados<br>por el titular del proyecto y a la vez fueron<br>complementados con aquellos que fueron<br>considerados en el estudio de ruidos del año<br>2018.|

**4.3.3 Variables meteorológicas y geofísicas**

Tal como se mencionó en el punto 4.3.2, se utilizó la meteorología de pronóstico WRF en
formato calmet.dat, de esta forma se incorporó el archivo directamente al programa. El archivo
meteorológico tiene su centro en la comuna de Llay Llay. Para la ejecución del modelo se
modeló una zona más pequeña en comparación al WRF, es importante destacar que la zona
modelada tiene una dimensión de grilla de 25 metros (500 m x 500 m). En la siguiente Tabla se
presentan las características del archivo meteorológico.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 17 de 62

**Tabla No 4.** Características del archivo meteorológico WRF.

|Datos|Col2|Archivo Meteorológico|
|---|---|---|
|Comuna Central|Comuna Central|Llay Llay|
|Dimensión grilla|Dimensión grilla|60 x 60 km|
|Espaciado grilla|Espaciado grilla|1 km|
|Fecha-Hora inicio|Fecha-Hora inicio|01-01-2020 00:00|
|Fecha-Hora fin|Fecha-Hora fin|31-12-2020 23:00|
|Coordenadas NO3|Este|300.393|
|Coordenadas NO3|Norte|6.382.269|
|Coordenadas NE4|Este|360.548|
|Coordenadas NE4|Norte|6.383.168|
|Coordenadas SO5|Este|301.450|
|Coordenadas SO5|Norte|6.322.312|
|Coordenadas SE6|Este|361.561|
|Coordenadas SE6|Norte|6.323.309|

**4.3.4 Evaluación de los resultados**

Debido a que en Chile no existe normativa que regule la emisión ni la inmisión de olores por
parte de una planta de estas características, se utiliza como referencias normativas
internacionales, con el objetivo de evaluar y/o descartar la afectación a la calidad de vida de las
personas, acorde a los proyectos evaluados en el país por el Servicio de Evaluación Ambiental.
Las concentraciones de olor resultantes del modelo, para cada receptor discreto en OU E /m [3],
fueron comparados con el límite de inmisión de 1,5 OU E /m [3] propuesto en la “Guía de evaluación
de olores para planificación” (Guía UK), elaborado por el Instituto de Manejo de Calidad del Aire
(IAQM), Londres. Este límite se establece principalmente por su clasificación, debido a que
apunta actividades de acuerdo a su ofensividad, representativo al tipo de procesos de Cristal
Chile.

A continuación, se presentan los límites de la Guía UK, el cuál estipula límites de referencia
según ofensividad y fuentes de emisión de olor. Esta guía define tres grupos dependiendo del
nivel de ofensividad.

3 Coordenadas WGS-84 Huso 19.
4 Coordenadas WGS-84 Huso 19.
5 Coordenadas WGS-84 Huso 19.
6 Coordenadas WGS-84 Huso 19.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 18 de 62

Criterios de impacto de olor.

**Tabla No 5** . Límites de inmisión según Guía UK (Versión 1.1, 2018), para el percentil 98 [7] .

|Límite de<br>inmisión<br>C (ou /m3)<br>P98 E|Ofensividad|Tipo de actividad|
|---|---|---|
|1,5|Muy ofensivo|Procesos que involucran animales en descomposición o restos<br>de pescados.**Procesos que involucran residuos sépticos o**<br>**lodo.** Olores de vertederos biológicos.|
|3,0|Moderadamente<br>ofensivo|Crianza intensiva de ganado. Fritura de grasas (Procesamiento<br>de comida). Procesamiento de remolacha, azucarera.<br>Compostaje de desperdicios verdes bien ventilados.|
|6,0|Menos ofensivo|Cervecería Repostería Cafetería|

La Guía UK (Versión 1.1,2018) considera tres límites de inmisión dependiendo del tipo de
actividad y de su ofensividad. Para efectos de este informe se consideraron límites regulados
bajo el percentil 98, debido a que este percentil tiene una relación directa con la molestia
producida por olor [8] .

A partir de lo anteriormente señalado, para evaluar las concentraciones de olor, generadas por
la Cristal Chile, se decidió utilizar como valor límite 1,5 OU E /m [3], dado que dicho valor regula las
concentraciones que involucran procesos muy ofensivos; se considera que el nivel de
ofensividad está relacionado con el tipo de actividad, por lo tanto, mientras más ofensivo sean
los olores de una actividad, más restrictivo será el límite.

Los límites anteriormente mencionados son evaluados en receptores sensibles al olor. De
acuerdo a lo establecido en la Guía para la predicción y evaluación de impacto por olor en el
SEIA, señala que _“La evaluación de los impactos ambientales por olor debe realizarse según_
_las consideraciones y criterios establecidos en los artículos 5 al 9 del Reglamento del SEIA”_

 _Población en cuanto a la salud de la población (letra a)._

 _Grupos humanos, en cuanto a los sistemas de vida y costumbres (letra c)._

 _Población protegida (letra d)._

 _Visitantes o turistas, en cuanto componente el valor turístico de una zona (letra e)._

Criterios de impacto de amoniaco

Actualmente en Chile existe el D.S N°594 (publicado el 29 de abril de 2000) que “Aprueba el
Reglamento sobre Condiciones sanitarias y Ambientales Básicas en los Lugares de Trabajo”,
el cual establece algunos límites para contaminantes químicos, entre los que encontramos:

7 [El percentil es una medida de tendencia central usada en estadística que indica el valor de la variable por debajo de un porcentaje](https://es.wikipedia.org/wiki/Porcentaje)
dado de observaciones ordenados de menor a mayor. El Percentil 98 es el valor bajo el cual se encuentra el 98 % de los datos
horarios de olor registrados durante un año. (8760 datos)
8 Según la Enviroment Agency (UK) en su estudio “Review of dispersion modelling for Odour of preditios, del año 2007.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 19 de 62

 - **Límite Permisible Temporal:** Valor máximo permitido para el promedio ponderado de
las concentraciones ambientales de contaminantes químicos en los lugares de trabajo,
medidas en un período de 15 minutos continuos dentro de la jornada de trabajo. Este
límite no podrá ser excedido en ningún momento de la jornada.

 - **Límite Permisible Ponderado:** Valor máximo permitido para el promedio ponderado
de las concentraciones ambientales de contaminantes químicos existente en los lugares
de trabajo durante la jornada normal de 8 horas diarias, con un total de 45 horas
semanales.

En la siguiente tabla, se indican los límites establecidos para el amoniaco en el DS N°594:

**Tabla No 6** . Límites máximos para amoniaco.

|Contaminante|Límite Permisible Temporal|Col3|Límite Permisible Ponderado|Col5|
|---|---|---|---|---|
|**Contaminante**|**ppm**|**mg/m3 **|**ppm**|**mg/m3 **|
|Amoniaco|35|24|22|15|

Fuente: DS N° 594/2000: Aprueba reglamento sobre condiciones básicas y ambientales en los logares de trabajo.

Por otro lado, las concentraciones de amoniaco fueron comparadas con los límites establecidos
en la norma de calidad del aire Ontario de Canadá, la que establece límites para periodos de
30 min y de 24 horas, tales como los que se indican en la siguiente tabla:

**Tabla No 7** . Estándares para amoniaco.

|Contaminante|Estándar de media hora<br>(μg/m3)|Estándar de 24 horas<br>(μg/m3)|
|---|---|---|
|Amoniaco|300|100|

Fuente: O.Reg. 419/05: Contaminación del aire - Calidad del aire local.

Como el DS N°594 establece un límite permisible temporal de 15 min y la norma de calidad del
aire Ontario, Canadá establece un límite para periodos de 30 min y dado que el modelo utilizado
entrega la concentraciones en un promedio mínimo de 1 hora, fue necesario convertir las
concentraciones promedios a un equivalente de 15 minutos y 30 minutos, de tal forma de poder
comparar los resultados con las normas indicadas previamente. Para esto se utilizó la siguiente
ecuación:

[μg] [x(] 60 min

m [3] 15 min o 30 min ~~[)]~~

[NH 3 ] [μg]

0,28

**4.3.5 Área de Influencia y receptores de interés.**

Una vez ejecutado el modelo de dispersión de olor, se realizó el análisis de post-proceso
obteniendo las curvas iso-concentración de la dispersión anual. Tal como lo indica la guía el
Área de Influencia se debe circunscribir en el espacio contenido por la isodora de 1 OU E /m [3],
que corresponde al umbral de detección del olor compuesto.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 20 de 62

Las concentraciones de olor no supera 1 OU E /m [3], por lo que no se pudo determinar el área de
influencia y tampoco se pudo realizar una descripción general y significativa del Área de
Influencia, para cada elemento del medio ambiente considerando los efectos, características o
circunstancias establecidos en el artículo 11 de la Ley N°19.300 como población, población
protegida, grupos humanos y visitantes o turistas.

Al igual que en el apartado anterior, el área de influencia se contrasta con lo establecido en la
Guía para la predicción y evaluación de impacto por olor en el SEIA, donde se señala que _“La_
_evaluación de los impactos ambientales por olor deben realizarse según las consideraciones y_
_criterios establecidos en los artículos 5 al 9 del Reglamento del SEIA, según lo siguiente”._

**Evaluación del desempeño del archivo de pronóstico utilizado**

El modelo numérico recomendado para la generación de datos meteorológicos es el Weather
Research and Forecasting Model (WRF). WRF es uno de los modelos meteorológicos de
pronóstico más avanzados y completos, el cual es mantenido por NCAR/NOAA de Estados

Unidos.

Todos los modelos tienen asociados errores e incertidumbre. Los resultados del modelo se

analizan con base a la comparación de los gráficos indicados en los puntos 6.6.3 y 6.7 de la
“Guía para uso de modelos de Calidad del aire en el SEIA”. Con base a la comparación de los
ciclos diarios de las variables meteorológicas observadas y simuladas, en la misma, ubicación,
se debe caracterizar la capacidad del modelo de reproducir las observaciones tanto en
magnitud como en su variabilidad.

Para cumplir con lo indicado por la guía para uso de modelos de dispersión del SEA, se realizó
un análisis del desempeño de la meteorología de pronóstico WRF utilizada para la modelación.
Este análisis permite detectar posibles desviaciones en el modelo de pronóstico que podrían
causar efectos en los resultados del modelo de dispersión. Para este informe se contrastaron
las variables de viento respecto a los registros de las estaciones públicas Catemu y Romeral,
ambas del SINCA.

**5** **Resultados**

A continuación, se presentan los resultados que permitieron evaluar el efecto de las emisiones
de olor y de amoniaco generadas por el contenedor de lodos.

**Caracterización de las fuentes de emisión**

Con la finalidad de dar cumplimiento al D.S 609/98 Descargas de Residuos Industriales
Líquidos a Sistemas de Alcantarillado, la planta de Satinado Llay Llay cuenta con una planta de
tratamiento que recibe 27 m [3] /día como afluente de las etapas de proceso: (a) Desengrasante,
(b) Lavado 1, (c) Lavado 2, (d) Lavado 3, (e) Lavado 4, (f) Lavado 5, (g) Lavado
Desmineralizado, (h) Scrubber. A continuación, se presenta un diagrama de proceso de la
planta de satinado:

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 21 de 62

**Figura No 8** . Diagrama de Proceso Satinado.

El RIL generado durante los procesos de lavado, se caracteriza por presentar un pH ácido con
valores que van entre 1 y 3 upH, por lo que deben ser neutralizados y precipitados con
fluorosilicatos mediante la adición de Hidróxido de Calcio, logrando una separación física con
la generación de lodos con alto contenido de Fluorito de Calcio. Tal como lo muestra el siguiente
diagrama:

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 22 de 62

**Figura No 9** . Diagrama de Procesos Planta de Tratamiento de RILes.

A continuación, se presenta en mayor detalle el diagrama de flujo de generación de lodos:

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 23 de 62

**Figura No 10** . Diagrama de Flujo generación de lodos.

La deshidratación de lodos proveniente del espesamiento gravitacional se efectúa mediante
filtro de placas, donde por acción de gravedad cae a un contenedor abierto de 2 m [3], donde es
acumulado durante el día para posteriormente ser trasladados a un contenedor hermético de
15 m [3] de capacidad. Para efectos de la modelación se consideró que el contenedor se iba abrir
1 hora al día de lunes a domingo (de 17:00 a 18:00 hrs).

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 24 de 62

**Figura No 11** . Fuentes consideradas para modelación.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 25 de 62

**Emisiones**

**5.2.1 Emisión de olor**

Para determinar las emisiones de olor generadas en el contenedor de lodos, se utilizaron los
factores de emisión propuestos en el Informe Final “Servicio de recopilación y sistematización
de factores de emisión al aire para el Servicio de Evaluación Ambiental” (mayo, 2015), donde
se indican factores de emisión para las emisiones atmosféricas asociadas al manejo de aguas
residuales.

En la siguiente tabla, se presentan los factores de emisión para olores/línea de lodo/sistema de
pre-deshidratado:

**Tabla No 8** . Factores de emisión para olores/línea de lodo/sistema de pre-deshidratado. [9]

|Descripción|Factor de emisión (OU /m2s)<br>E|
|---|---|
|Lodo fresco|8|
|Lodo anaeróbico|3,95|
|Lodo mezclado|8|

Para efectos de la modelación se consideró un escenario más conservador, por lo que las
emisiones de olor fueron calculadas a partir del factor de emisión propuesto para lodo
mezclado, el cual establece 8 OU E /m [2] s. Así, la emisión de olor generada en el contenedor de
lodos, queda definida por:

E olor (OU E /s) = S (m [2] ) x FE (OU E /m [2] s) Ecuación 1

Dónde:
E olor : Emisión de olor (OU E /s).
S: Superficie contenedor de lodos (m [2] ).
FE: Factor de emisión (OU E /m [2] s).

E olor = 12,65 m [2] x 8 OU E /m [2] s

E olor = 101,2 OU E /s

A continuación, se presentan las emisiones de olor generadas, por el contenedor de lodos en
Cristal Chile.

**Tabla No 9.** Emisión de olor contenedor de lodos.

|Fuente|Alto (m)|Ancho (m)|Largo (m)|Superficie<br>(m2)|Factor de<br>emisión<br>(OU /s*m2)<br>E|Emisión de<br>olor<br>(OU /s)<br>E|
|---|---|---|---|---|---|---|
|Contenedor de lodos|1,2|2,3|5,5|12,65|8|101,2|

9 Netherlands Emission Guidelines for Air, Chapter 3.3 Special Regulations for Specific Processes, Section G.3
“Sewage Treatment Installations, Abril 2003” (páginas 117 a 122).

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 26 de 62

Es importante señalar que, para ejecutar el modelo de olor se tomaron las siguientes
consideraciones:

 - Se modeló un contenedor de lodos de dimensiones 5,5 m x 2,3 m = 12,65 m [2] .

 - Se consideró un contenedor hermético, el cual se abriría 1 vez al día de 17:00 a 18:00
hrs de lunes a viernes, con la finalidad de trasvasijar el lodo contenido en el contenedor
abierto de 2 m [3] que almacena en forma diaria el lodo que cae el filtro prensa.

**5.2.2 Emisión de amoniaco**

Para calcular la emisión de amoniaco, el titular del proyecto realizó una simulación de la tasa
de evaporación y generación de amoniaco en el contenedor de lodos, donde se consideraron
los siguientes criterios:

- Contenedor de lodos hermético de 15 m [3], equivalente a 12 m [2 ] de superficie, se
contempla un flujo de aire despreciable.

- Humedad del lodo de 30%.

- pH neutro de los lodos.

- Temperatura 25°C

- 5% de disolución de amonio en agua.

- Se asume apertura diaria del contenedor de lodos (15 m [3] ).

- Se mezcla el Cloruro de Amonio con el total agua disponible.

- Simulación de tasa de evaporación inicial.

- Los gases de evaporación quedan contenidos en el contenedor hasta su apertura.

Por lo que se concluyó que la concentración inicial de amoniaco en el aire del contenedor era
de 13,4 mg/l.

A partir de lo anterior, se procedió a calcular la emisión de amoniaco en aire, considerando que
el contenedor de lodos es una fuente pasiva, las que según la NCh 3386/2015 (Calidad del aire

- Muestreo estático para olfatometría) se caracterizan por tener una velocidad de flujo igual a
30 m/h:

13,4 [m][g]

h [∗1 h∗12,65m] 3.600 s [2]

[NH 3 ] =

L [∗30 m]
1.000 L/m [3] h

3.600 s

0,00141 [m][g]

[NH 3 ] =

s
1.000 ~~[m][g]~~

s

~~[g]~~

[= 1,40 ∗10] [−6] [ g] s
g [∗12,65 m] [2]

s

Además, se calcula la tasa de emisión de amoniaco por superficie.

[g]

[NH 3 ] = 1,11 ∗10 [−7]

m [2] s

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 27 de 62

A continuación, se presentan las emisiones de amoniaco generadas, por el contenedor de lodos
en Cristal Chile.

**Tabla No 10.** Emisión de amoniaco contenedor de lodos.

|Fuente|Superficie<br>(m2)|Velocidad del<br>Flujo<br>(m/s)|Concentración de<br>amoniaco<br>(g/m3)|Emisión de<br>NH<br>3<br>(g/m2*s)|Emisión de<br>NH<br>3<br>(g/s)|
|---|---|---|---|---|---|
|Contenedor de lodos|12.65|8.33E-03|1.34E-05|1.11E-07|1.40E-06|

Es importante señalar que, para ejecutar el modelo de olor se tomaron las siguientes
consideraciones:

 - Se modeló un contenedor de lodos de dimensiones 5,5 m x 2,3 m = 12,65 m [2] .

 - Se consideró un contenedor hermético, el cual se abriría 1 vez al día de 17:00 a 18:00
hrs de lunes a viernes, con la finalidad de trasvasijar el lodo contenido en el contenedor
abierto de 2 m [3] que almacena en forma diaria el lodo que cae el filtro prensa.

**Evaluación de la dispersión de olor**

En el presente apartado se presenta la dispersión de las emisiones de olores generadas por el
contenedor de lodos de la planta Cristal Chile, según las fuentes mencionadas en el punto 5.1
del presente estudio. Los resultados muestran la pluma de dispersión de los olores dentro del
límite predial, las cuales, además de simular la dispersión de los gases, entregan las
concentraciones de olor (OU E /m [3] ) en el espacio.

Más adelante se presenta una cartografía de dispersión de olor, la que registra el percentil 98
de las concentraciones horarias, con el objetivo de poder comparar los resultados con el límite
de 1,5 OU E /m [3], establecido en la Guía UK.

A continuación, se presentan los resultados, de la evaluación del modelo de dispersión, del
contenedor de lodos.

**5.3.1.1 Dispersión de emisiones de olor**

El límite de referencia indicado en la Guía UK establece un valor de 1,5 OU E /m [3] para periodos
horarios con percentil 98.

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se acentúa
hacia el sureste con una longitud aproximada de 0,16 km en dirección noroeste-sureste. Las
isodoras graficadas varían entre 0,01 a 0,23 OU E /m [3], presentando su mayor concentración al
sureste del contenedor de lodos, donde alcanza las 0,23 OU E /m [3] . Es importante señalar que la
pluma se desplaza dentro del límite de cristal Chile, por lo que los receptores no se verían
afectados por la emisión de olor.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 28 de 62

La Guía UK define el umbral de molestia en 1,5 OU E /m3, sin embargo, las emisiones generadas
por el contenedor de lodos son tan pequeñas que no superan dicho límite.

A continuación, se presenta la cartografía que contiene las curvas de isoconcentración.

**Figura No 12** . Mapa de concentración de olor generado por las fuentes de emisión de la

planta. Promedio horario (percentil 98).

Según la “Guía para la predicción y evaluación de impactos por olor en el SEIA” [10], el área de
influencia está definida como el espacio contenido por la isodora de 1 OU E /m [3], que corresponde
al umbral de detección del olor compuesto. Sin embargo, las emisiones generadas por el
contenedor de lodos son tan pequeñas que no superan las 0,23 OU E /m [3], es por lo mismo que
tampoco se presentan las curvas de isofrecuencia que indican las horas de excedencia del
límite de inmisión.

La máxima concentración se produce al interior de la planta, al sureste del contenedor de lodos,
alcanzando una concentración de 0,23 OU E /m [3] .

10 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 29 de 62

**Tabla No 11** . Máxima concentración.

|Descripción|UTM 19H WGS84|Col3|Concentración de<br>inmisión<br>(OU /m3)<br>E|
|---|---|---|---|
|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Punto de máxima concentración|317.951|6.364.092|0,23|

**5.3.1.2 Receptores discretos considerados en la modelación de olor**

En la modelación se consideraron los receptores utilizados en el estudio de ruido del año 2018
realizado por Cristal Chile y en forma adicional, se consideraron algunos propuestos por el
titular. A continuación, se presentan las coordenadas de cada uno de ellos:

**Tabla No 12** . Receptores considerados en la modelación.

|No|Descripción|Proyección UTM Huso 19S<br>Datum WGS84|Col4|Distancia con respecto a la<br>fuente (km)|
|---|---|---|---|---|
|**No**|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R1|Vivienda más cercana|317.978|6.364.178|0,08|
|R2|Receptor estadio|317.735|6.363.979|0,23|
|R3|Vivienda|318.064|6.364.130|0,13|
|R4|Vivienda|318.016|6.364.157|0,09|
|R5|Receptor ruido R1|317.983|6.364.168|0,08|
|R6|Receptor ruido R2|318.012|6.364.152|0,09|
|R7|Receptor ruido R3|318.040|6.364.139|0,10|
|R8|Receptor ruido R4|318.235|6.364.031|0,30|
|R9|Receptor ruido R5|318.309|6.363.992|0,38|
|R10|Receptor ruido R6|318.110|6.364.092|0,17|
|R11|Receptor ruido R7|318.282|6.363.819|0,44|
|R12|Receptor ruido R8|318.128|6.363.526|0,60|
|R13|Receptor ruido R9|317.389|6.363.648|0,70|
|R14|Receptor ruido R10|317.293|6.363.744|0,73|
|R15|Receptor ruido R11|317.737|6.363.577|0,55|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 30 de 62

**Figura No 13** . Receptores de interés analizados.

En la siguiente tabla, se presenta el resultado del Percentil 98, de las concentraciones horarias,
para cada receptor identificado. Tal como se puede observar, los receptores considerados
presentan concentraciones que no superan el límite de inmisión durante todo el año (límite de
inmisión definido por la Guía UK como 1,5 OU E /m [3] ).

**Tabla No 13** . Concentración receptores. Percentil 98.

|No|Concentración de inmisión<br>(OU /m3)<br>E|Límite de inmisión<br>Guía UK|
|---|---|---|
|R1|1,32E-06|<br> <br> <br> <br> <br> <br> <br> <br> <br>1,5 OUE/m3|
|R2|1,41E-06|1,41E-06|
|R3|1,47E-06|1,47E-06|
|R4|1,36E-06|1,36E-06|
|R5|1,33E-06|1,33E-06|
|R6|1,35E-06|1,35E-06|
|R7|1,40E-06|1,40E-06|
|R8|1,42E-03|1,42E-03|
|R9|1,29E-03|1,29E-03|
|R10|4,76E-04|4,76E-04|
|R11|1,98E-04|1,98E-04|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 31 de 62

|No|Concentración de inmisión<br>(OU /m3)<br>E|Límite de inmisión<br>Guía UK|
|---|---|---|
|R12|1,50E-06||
|R13|1,38E-06|1,38E-06|
|R14|1,42E-06|1,42E-06|
|R15|1,41E-06|1,41E-06|

**5.3.1.3 Análisis FIDOL**

**Tabla No 14.** Protocolo FIDOL con base a receptores definidos.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia|La planta opera durante todo el año, sin embargo, la fuente modelada (contenedor de<br>lodos) es totalmente hermética, por lo que se abre una vez al día durante una hora para<br>vaciar el lodo. A partir de la modelación realizada, durante el 98% de las horas del año;<br>no existiría superación de las 1,5 OUE/m3 - percentil 98 en ninguno de los receptores.|
|Intensidad|No existe superación del umbral de molestia de 1,5 OUE/m3 en ninguno de los<br>receptores, por lo que no se prevé afectación por factor de intensidad.|
|Duración|No existe superación del umbral de molestia de 1,5 OUE/m3 en ninguno de los<br>receptores, por lo que no se prevé afectación por factor de duración.|
|Ofensividad|No existe superación del umbral de molestia de 1,5 OUE/m3 en ninguno de los<br>receptores, por lo que no se prevé afectación por factor de duración.|
|Localización|Según el Plan regulador de la comuna de Llay Llay, Cristal Chile se emplaza en un uso<br>de suelo clasificado como I1, el cual corresponde a uso industrial.|

**Evaluación de la dispersión de amoniaco**

En el presente apartado se presenta la dispersión de las emisiones de amoniaco, generadas
por el contenedor de lodos de la planta Cristal Chile, según las fuentes mencionadas en el punto
5.1 del presente estudio. Los resultados muestran la pluma de dispersión de amoniaco dentro
del límite predial, las cuales, además de simular la dispersión de los gases, entregan las
concentraciones de amoniaco ( μg /m [3] ) en el espacio.

Más adelante, se presentan cuatro cartografías que indican la concentración de amoniaco para
un periodo de 15 min, 30 min, 8 horas y 24 horas, en cada uno se indica el punto de máxima
concentración. Dichos resultados se comparan con los límites establecidos en el D.S N°594
donde se define el límite permisible temporal para periodos de 15 min (35 ppm - 24 mg/ m [3] -
24.000 μg /m [3] ) y el límite permisible ponderado para un periodo de 8 horas (22 ppm - 15 mg/
m [3] - 15.000 μg /m [3] ). En forma complementaria, se realizó una comparación de las
concentraciones de 30 min y de 24 horas con la norma Ontario de Canadá, la que establece un
límite de 300 μ g/m [3 ] y 100 μg /m [3 ] respectivamente.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 32 de 62

**5.4.1 Resultados emisión de amoniaco**

A continuación, se presentan los resultados de la emisión de olor generada por el contenedor
de lodos, considerando las concentraciones más desfavorables (el análisis se realizó con las
concentraciones máximas).

**5.4.1.1 Dispersión de emisiones de amoniaco**

**Dispersión Amoniaco - Concentración 15 min**

El D.S. N° 594 establece el límite permisible temporal, el cual define el valor máximo permitido
para el promedio ponderado de las concentraciones ambientales de contaminantes químicos
en los lugares de trabajo, para un periodo de 15 min; indicando que las concentraciones de
amoniaco no pueden superar los 35 ppm - 24 mg/ m [3] - 24.000 μg /m [3] . Es importante señalar
que los siguientes resultados se obtuvieron a partir de las máximas concentraciones obtenidas
en dicho periodo, lo que indica el peor escenario evaluado.

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se acentúa
en sentido noroeste y sureste con una longitud aproximada de 0,34 km. Las isodoras graficadas
varían entre 0,003 y 0,053 μg /m [3], presentando su mayor concentración al suroeste del
contenedor de lodos, donde alcanzan los 0,053 μg /m [3] . Es importante señalar que la pluma se
desplaza dentro y fuera del límite predial de Cristal Chile, a pesar de esto, ninguno de los
receptores considerados en la modelación se vería afectado por la emisión de amoniaco.

Como se mencionó anteriormente, el D.S N° 594 define el límite permisible temporal en 24.000
μg /m [3], sin embargo, las emisiones generadas por el contenedor de lodos no superan dicho
límite.

A continuación, se presenta la cartografía que representa la distribución de las emisiones de
amoniaco.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 33 de 62

**Figura No 14** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (15 min).

La máxima concentración se produce al interior de la planta, al suroeste del contenedor de
lodos, alcanzando una concentración de 0,053 μg /m [3] .

**Tabla No 15** . Máxima concentración.

|Descripción|UTM 19H WGS84|Col3|Concentración de<br>inmisión<br>(μ/m3)|
|---|---|---|---|
|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Punto de máxima concentración|317.926|6.364.092|0,053|

**Dispersión Amoniaco - Concentración 30 min**

El límite de referencia indicado en la norma Ontario de Canadá establece un valor de 300 μg /m [3]
para periodos promediados de media hora.

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se acentúa
en sentido noroeste y sureste con una longitud aproximada de 0,22 km. Las isodoras graficadas
varían entre 0,005 y 0,0436 μg /m [3], presentando su mayor concentración al suroeste del
contenedor de lodos, donde alcanzan los 0,0436 μg /m [3] . Es importante señalar que la pluma se

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 34 de 62

desplaza dentro y fuera del límite predial de Cristal Chile, a pesar de esto, ninguno de los
receptores considerados en la modelación se vería afectado por la emisión de amoniaco.

La norma Ontario de Canadá define el estándar de media hora en 300 μg /m [3], sin embargo, las
emisiones generadas por el contenedor de lodos no superan dicho límite.

A continuación, se presenta la cartografía que representa la distribución de las emisiones de
amoniaco.

**Figura No 15** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (30 min).

La máxima concentración se produce al interior de la planta, al suroeste del contenedor de
lodos, alcanzando una concentración de 0,0436 μ g/m [3] .

**Tabla No 16** . Máxima concentración.

|Descripción|UTM 19H WGS84|Col3|Concentración de<br>inmisión<br>(μg/m3)|
|---|---|---|---|
|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Punto de máxima concentración|317.926|6.364.092|0,0436|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 35 de 62

**Dispersión Amoniaco - Concentración 8 horas**

El D.S. N° 594 establece el límite permisible ponderado, el cual define el valor máximo permitido
para el promedio ponderado de las concentraciones ambientales de contaminantes químicos
en los lugares de trabajo, durante una jornada normal de 8 horas diarias, con un total de 45
horas semanales; indicando que las concentraciones de amoniaco no pueden superar los 22
ppm - 15 mg/ m [3] - 15.000 μg /m [3] . Es importante señalar que los siguientes resultados se
obtuvieron a partir de las máximas concentraciones obtenidas en dicho periodo, lo que indica
el peor escenario evaluado.

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se acentúa
en sentido noroeste y sureste con una longitud aproximada de 0,23 km. Las isodoras graficadas
varían entre 0,0005 y 0,0045 μg /m [3], presentando su mayor concentración al suroeste del
contenedor de lodos, donde alcanzan los 0,0045 μg /m [3] . Es importante señalar que la pluma se
desplaza dentro y fuera del límite predial de Cristal Chile, a pesar de esto, ninguno de los
receptores considerados en la modelación se vería afectado por la emisión de amoniaco.

Como se mencionó anteriormente, el D.S N° 594 define el límite permisible ponderado en
15.000 μg /m [3], sin embargo, las emisiones generadas por el contenedor de lodos no superan
dicho límite.

A continuación, se presenta la cartografía que representa la distribución de las emisiones de

amoniaco.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 36 de 62

**Figura No 16** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (8 horas).

La máxima concentración se produce al interior de la planta, al suroeste del contenedor de
lodos, alcanzando una concentración de 0,0045 μ g/m [3] .

**Tabla No 17** . Máxima concentración.

|Descripción|UTM 19H WGS84|Col3|Concentración de<br>inmisión<br>(μg/m3)|
|---|---|---|---|
|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Punto de máxima concentración|317.926|6.364.092|0,0045|

**Dispersión Amoniaco - Concentración 24 horas**

El límite de referencia indicado en la norma Ontario, Canadá establece un valor de 100 μg /m [3]
para periodos de 24 horas.

Tal como se puede apreciar en la siguiente cartografía, la distribución de la pluma se acentúa
en sentido noroeste y sureste con una longitud aproximada de 0,31 km. Las isodoras graficadas
varían entre 0,0001 y 0,0015 μg /m [3], presentando su mayor concentración al suroeste del
contenedor de lodos, donde alcanzan los 0,0015 μg /m [3] . Es importante señalar que la pluma se

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 37 de 62

desplaza dentro y fuera del límite predial de Cristal Chile, a pesar de esto, ninguno de los
receptores considerados en la modelación se vería afectado por la emisión de amoniaco.

La norma Ontario de Canadá define el umbral de molestia para 24 horas en 100 μg /m [3], sin
embargo, las emisiones generadas por el contenedor de lodos no superan dicho límite.

A continuación, se presenta la cartografía que representa la distribución de las emisiones de
amoniaco.

**Figura No 17** . Mapa de concentración de amoniaco generado por el contenedor de lodos.

Concentración máxima anual (24 horas).

La máxima concentración se produce al interior de la planta, al suroeste del contenedor de
lodos, alcanzando una concentración de 0,0015 μ g/m [3] .

**Tabla No 18** . Máxima concentración.

|Descripción|UTM 19H WGS84|Col3|Concentración de<br>inmisión<br>(μg/m3)|
|---|---|---|---|
|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Punto de máxima concentración|317.926|6.364.092|0,0015|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 38 de 62

**Comparación con el DS N° 594:**

En la siguiente tabla, se presenta el resultado de las concentraciones cada 15 minutos y cada
8 horas, de tal forma de poder compararlas con el límite permisible temporal (35 ppm - 24
mg/m [3], lo que equivale a 24.000 μ g/m [3] ) y con el límite permisible ponderado (22 ppm - 15
mg/m [3], lo que equivale a 15.000 μ g/m [3] ). Tal como se puede observar, los receptores
considerados presentan concentraciones que no superan el límite permisible temporal (15 min)
y tampoco el límite permisible ponderado (8 horas).

**Tabla No 19** . Concentración en receptores.

|No|Concentración de<br>inmisión<br>cada 15 min<br>(μg/m3)|Límite Permisible<br>Temporal|Concentración de<br>inmisión<br>cada 8 horas<br>(μg/m3)|Límite Permisible<br>Ponderado|
|---|---|---|---|---|
|R1|0,0017|<br> <br> <br>35 ppm<br>24 mg/m3 <br>24.000μg/m3 <br>|0,00015|<br> <br> <br> <br> <br> <br> <br> <br> <br>22 ppm<br>15 mg/m3 <br>15.000μg/m3|
|R2|0,0010|0,0010|0,00009|0,00009|
|R3|0,0016|0,0016|0,00014|0,00014|
|R4|0,0017|0,0017|0,00015|0,00015|
|R5|0,0017|0,0017|0,00015|0,00015|
|R6|0,0017|0,0017|0,00015|0,00015|
|R7|0,0017|0,0017|0,00014|0,00014|
|R8|0,0014|0,0014|0,00012|0,00012|
|R9|0,0013|0,0013|0,00011|0,00011|
|R10|0,0015|0,0015|0,00013|0,00013|
|R11|0,0007|0,0007|0,00006|0,00006|
|R12|0,0005|0,0005|0,00004|0,00004|
|R13|0,0002|0,0002|0,00002|0,00002|
|R14|0,0002|0,0002|0,00001|0,00001|
|R15|0,0004|0,0004|0,00004|0,00004|

**Comparación con los límites establecidos en la norma Ontario, Canadá**

En la siguiente tabla, se presenta el resultado de las concentraciones cada 30 minutos (300
μ g/m [3] ) y cada 24 horas (100 μ g/m [3] ), de tal forma de poder compararlas con los límites
establecidos en la norma Ontario, Canadá. Tal como se puede observar, los receptores
considerados presentan concentraciones que no superan el límite establecido para 30 min y
tampoco para 24 horas.

**Tabla No 20** . Concentración en receptores.

|No|Concentración de<br>inmisión<br>cada 30 min<br>(μg/m3)|Límite de inmisión<br>cada 30 min<br>(μg/m3)|Concentración de<br>inmisión<br>cada 8 horas<br>(μg/m3)|Límite de inmisión<br>cada 24 horas<br>(μg/m3)|
|---|---|---|---|---|
|R1|0,0014|<br> <br>|0,000049|<br> <br>|
|R2|0,0008|0,0008|0,000029|0,000029|
|R3|0,0013|0,0013|0,000047|0,000047|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 39 de 62

|No|Concentración de<br>inmisión<br>cada 30 min<br>(μg/m3)|Límite de inmisión<br>cada 30 min<br>(μg/m3)|Concentración de<br>inmisión<br>cada 8 horas<br>(μg/m3)|Límite de inmisión<br>cada 24 horas<br>(μg/m3)|
|---|---|---|---|---|
|R4|0,0014|<br> <br> <br>300<br>|0,000049|<br> <br> <br>100|
|R5|0,0014|0,0014|0,000049|0,000049|
|R6|0,0014|0,0014|0,000049|0,000049|
|R7|0,0014|0,0014|0,000048|0,000048|
|R8|0,0012|0,0012|0,000040|0,000040|
|R9|0,0011|0,0011|0,000037|0,000037|
|R10|0,0012|0,0012|0,000043|0,000043|
|R11|0,0006|0,0006|0,000021|0,000021|
|R12|0,0004|0,0004|0,000014|0,000014|
|R13|0,0002|0,0002|0,000005|0,000005|
|R14|0,0001|0,0001|0,000005|0,000005|
|R15|0,0003|0,0003|0,000012|0,000012|

**Análisis del desempeño del archivo de pronóstico utilizado**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para
ello se utilizan los datos disponibles de las estaciones de monitoreo ubicadas en la zona de
interés para el estudio.

Las estaciones provenientes del sistema de información nacional de calidad del aire (SINCA),
corresponden a Catemu y Romeral, ubicadas a 7,4 km y 6,0 km de la planta, respectivamente.
Estas estaciones presentan datos de dirección y velocidad de viento, las cuales serán utilizadas
para validar el modelo meteorológico de pronóstico WRF y no serán utilizadas como entradas
al modelo.

En el Anexo N°2 se presentan las variables meteorológicas y geofísicas del emplazamiento de
la planta y en el Anexo No3 se presenta una comparación cualitativa y cuantitativa entre la
meteorología de pronóstico y los datos observados en la estación meteorológica.

De acuerdo con las comparaciones realizadas en forma cualitativa de ciclo diario, promedio
mensual rosa de los vientos y ciclos estacionales, para los parámetros de velocidad y dirección
del viento para la estación Catemu y Romeral, se puede indicar que tanto el modelo WRF y los
datos observados presentan valores y patrones similares, que permiten indicar que los datos
WRF se ajustan a la realidad y pueden ser utilizados en la modelación.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 40 de 62

**Figura No 18** . Estaciones Meteorológicas utilizadas en el Análisis de Incertidumbre.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 41 de 62

**6** **Conclusiones**

Con respecto a la modelación del contenedor de lodos de Cristal Chile, se concluye lo siguiente:

Dispersión de olor

1. Las curvas de isoconcentración del percentil 98, indican que las concentraciones de olor

producidas por el contenedor de lodos, varían entre 0,01 y 0,23 OU E /m [3], presentándose la
máxima concentración dentro del límite predial, la que alcanza los 0,23 OU E /m [3] .

2. Bajo las condiciones modeladas, no se presenta superación del límite de 1,5 OU E /m [3]

(percentil 98) en ninguno de los receptores considerados en la modelación, en ninguna hora

del año.

3. Las concentraciones de olor generadas por el contenedor de lodos son menores a 1

OU E /m [3], por lo que no cumplen con los requisitos, establecidos en la Guía de olores del
SEIA, para definir el área de influencia.

Dispersión de amoniaco

4. Al evaluar las emisiones de amoniaco, para un periodo de 15 min, se tiene que las curvas

de isoconcentración, varían entre 0,003 y 0,053 μg /m [3], presentándose la máxima
concentración dentro del límite predial, la que alcanza los 0,053 μg /m [3] . Por lo que no se
supera el límite permisible temporal, establecido en el DS N° 594, en ninguna de las 8784
horas del año.

5. Al evaluar las emisiones de amoniaco, para un periodo de 30 min, se tiene que las curvas

de isoconcentración, varían entre 0,005 y 0,0436 μg /m [3], presentándose la máxima
concentración dentro del límite predial, la que alcanza los 0,0436 μg /m [3] . Por lo que no se
supera el estándar de 30 minutos de la norma Ontario, Canadá, en ninguna de las 8784
horas del año.

6. Al evaluar las emisiones de amoniaco, para un periodo de 8 horas, se tiene que las curvas

de isoconcentración, varían entre 0,0005 y 0,0045 μg /m [3], presentándose la máxima
concentración dentro del límite predial, la que alcanza los 0,0045 μg /m [3] . Por lo que no se
supera el límite permisible ponderado, establecido en el DS N° 594, en ninguna de las 8784
horas del año.

7. Al evaluar las emisiones de amoniaco, para un periodo de 24 horas, se tiene que las curvas

de isoconcentración, varían entre 0,0001 y 0,0015 μg /m [3], presentándose la máxima
concentración dentro del límite predial, la que alcanza los 0,0015 μg /m [3] . Por lo que no se
supera el estándar de 24 horas de la norma Ontario, Canadá, en ninguna de las 8784 horas
del año.

8. Bajo las condiciones modeladas, no se presenta superación de los límites establecidos en

el DS N° 594 y tampoco se superan los estándares establecidos en la norma Ontario de
Canadá.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 42 de 62

9. Los resultados entregados en el presente informe, corresponden a los máximos valores

determinados en el modelo, por lo que el resto de las horas del año presentan valores
inferiores a los indicados.

En relación con la validación meteorológica del modelo de pronóstico WRF:

10. Se puede concluir a partir del análisis cualitativo y cuantitativo, que el modelo de pronóstico

WRF presenta valores de dirección y velocidad de viento similares a los datos observados.
Al analizar las velocidades promedio y direcciones frecuentes del viento, los valores
modelados concuerdan con los datos observados. Por lo tanto, de acuerdo con lo
presentado en el análisis cuantitativo y cualitativo de la estación Catemu y Romeral, el
modelo WRF utilizado para el análisis de dispersión atmosférica es adecuado y concuerda
con las condiciones de la realidad.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 43 de 62

**7** **Anexos**

**Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación**

El presente Anexo contiene el archivo magnético el cual presenta la información que se utilizó
para realizar la modelación atmosférica, dicha información corresponde a los input y output
ingresados para la modelación de los módulos del modelo (CALPUFF, CALPOST y CALRANK)
y el archivo Meteorológico WRF.

Por lo tanto, en el caso de que se requiera replicar la modelación realizada, esta se podrá hacer

utilizando los archivos indicados en este Anexo.

**Figura No 19** . Esquema funcionamiento CALPUFF

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 44 de 62

**Anexo No2. Descripción meteorológica y geofísica de la zona**

En el siguiente anexo se presenta el análisis de la meteorología de la zona modelada. Los datos
expresados a continuación fueron extraídos por la plataforma SINCA (Sistema de información
nacional de calidad del aire), correspondientes a las estaciones de monitoreo de Catemu y

Romeral

**Tabla No 21.** Datos estaciones meteorológicas consideradas.

|Estación Meteorológica|Col2|EM Catemu|EM Romeral|
|---|---|---|---|
|Coordenada UTM Datum<br>WGS 84|Zona|19H|19H|
|Coordenada UTM Datum<br>WGS 84|Este (m)|316.512|312.181|
|Coordenada UTM Datum<br>WGS 84|Norte (m)|6.371.481|6.366.428|
|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|01/01/2020 - hasta<br>31/12/2020|01/01/2020 - hasta<br>31/12/2020|
|Distancia desde el Plantel (km)|Distancia desde el Plantel (km)|19|18|
|Meteorología|Meteorología|Velocidad Viento (VV)<br>Dirección Viento (DV)|Velocidad Viento (VV)<br>Dirección Viento (DV)|

**7.2.1 Cantidad de datos**

Para realizar el análisis meteorológico y el análisis de incertidumbre es necesario verificar la
cantidad de datos presentes en las mediciones ambientales de las estaciones. A continuación,
se muestran los datos de las estaciones en la serie de tiempo para comprobar que no existen
periodos extensos sin datos durante el año de análisis.

**Estación Catemu.**

**Figura No 20.** Serie de tiempo velocidad de viento - datos observados estación Catemu- año

2020.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 45 de 62

**Figura No 21.** Serie de tiempo dirección de viento - datos observados estación Catemu - año

2020.

**Tabla No 22.** Datos válidos estación meteorológica Catemu.

|Porcentaje de datos meteorológicos disponibles - EM Catemu|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Pará/mes|E|F|M|A|M|J|J|A|S|O|N|D|**Total**|
|VV|83%|90%|100%|98%|100%|100%|99%|95%|99%|100%|100%|99%|97%|
|DV|99%|100%|100%|100%|100%|100%|100%|99%|100%|100%|100%|99%|100%|

La estación Catemu posee una cantidad de datos mínima es de 83% para velocidad del viento
y dirección del viento, lo que es superior al 75% sugerido por la Guía para modelos de calidad
del aire del SEA.

**Estación Romeral:**

**Figura No 22.** Serie de tiempo velocidad de viento - datos observados estación Romeral- año

2020.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 46 de 62

**Figura No 23.** Serie de tiempo dirección de viento - datos observados estación Romeral - año

2020.

**Tabla No 23.** Datos válidos estación meteorológica Romeral.

|Porcentaje de datos meteorológicos disponibles - EM Romeral|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Pará/mes|E|F|M|A|M|J|J|A|S|O|N|D|**Total**|
|VV|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|DV|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|
|T|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|100%|

A partir de las gráficas de serie de tiempo de los parámetros velocidad y dirección de viento de
la estación Romeral, se evidencian una cantidad de datos mínima de un 100%, superior al 75%
sugerido por la Guía para modelos de calidad del aire del SEA.

**7.2.2 Gráficos Ciclo diario**

Velocidad de viento

En los siguientes gráficos se presenta los ciclos diarios promedios de temperatura, velocidad y
dirección del viento; junto con su variabilidad entre el percentil 5% a 95% (Rango 90%
observado).

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 47 de 62

**Figura No 24.** Ciclo diario para velocidad de viento Estación Catemu.

En relación al ciclo diario promedio de la velocidad de viento, de la estación Catemu, se observa
una velocidad promedio mínima de 0,3 m/s durante la madrugada y una velocidad máxima
promedio de 1,8 m/s en las horas de la tarde. Durante el año, la velocidad del viento puede
variar entre calmas y 3,0 m/s en el rango de 90% observado.

**Figura No 25.** Ciclo diario para velocidad de viento Estación Romeral.

En relación al ciclo diario promedio de la velocidad de viento, de la estación Romeral, se
observa una velocidad promedio mínima de 2,5 m/s durante la mañana y una velocidad máxima
promedio de 6,5 m/s en las horas de la tarde. Durante el año, la velocidad del viento puede
variar entre calmas y 10,0 m/s en el rango de 90% observado.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 48 de 62

Dirección de viento

**Figura No 26.** Ciclo diario para dirección de viento estación Catemu.

En relación al ciclo diario de la dirección de viento de la estación Catemu, se observa que
durante todo el día predominan los vientos provenientes desde el suroeste; dicha condición
indica que los gases se dispersan hacia el noreste. En cuanto a horas de la noche la dirección
del viento proviene del sureste.

**Figura No 27.** Ciclo diario para dirección de viento estación Romeral.

En relación al ciclo diario de la dirección de viento de la estación Romeral, se observa que
durante todo el día predominan los vientos provenientes desde el oeste; dicha condición indica
que los gases se dispersan hacia el este. Durante la noche dirección del viento proviene

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 49 de 62

principalmente del oeste, mientras que parte de la madrugada y mañana varía entre este y

oeste.

**7.2.3 Gráficos Distribución de Vientos**

Las siguientes figuras muestran la distribución de vientos en las estaciones: Catemu y Romeral.
De acá se puede concluir que la mayor parte del tiempo, los vientos son de calma, para el caso
de Catemu, Mientras que Romeral presenta menor proporción de calmas. La velocidad de los
vientos fluye a diferentes velocidades principalmente con una velocidad entre 0,5 y 2,0 m/s
correspondiendo a un 47,2% de la distribución total en Estación Catemu, mientras que Romeral
presenta el mayor porcentaje en vientos de 2,0 a 4,0 m/s con un 35%.

**Figura No 28.** Distribución velocidades de viento estación Catemu.

**Figura No 29.** Distribución velocidades de viento estación Romeral.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 50 de 62

**7.2.4 Rosa de los vientos**

De la rosa de los vientos anual realizada para cada estación, se puede concluir que el viento
predominante proviene desde el sur principalmente, alcanzando una frecuencia de un 20% en
la estación Catemu y aproximadamente un 40% en la estación Romeral con dirección oeste.
Cabe destacar que los vientos alcanzan una velocidad máxima en un rango desde 2,0 hasta
4,0 m/s en la estación Catemu, y 2,0 a 6,0 m/s en estación Romeral.

**Figura No 30.** Rosa de los vientos Anual.

Estación Catemu.

**Figura No 31.** Rosa de los vientos Anual.

Estación Romeral.

**Por estación**

En los gráficos siguientes se muestra una comparación de las rosas de los vientos para cada
estación del año.

En otoño e invierno los vientos en Estación Catemu presentan una dirección principalmente
sur, con variantes de dirección este en invierno, mientras que las velocidades se encuentran
entre 0,5 y 4,0 m/s. Por otro lado, romeral presenta direcciones predominantes con dirección
este, y sus velocidades están entre 0,5 y 6,0 m/s.

En primavera y verano los vientos en Estación Catemu presentan una dirección
principalmente sur, mientras que las velocidades se encuentran entre 0,5 y 4,0 m/s. Por otro
lado, Romeral presenta direcciones predominantes con dirección oeste, y sus velocidades
están entre 0,5 y 6,0 m/s.

En los gráficos siguientes se muestran las rosas de los vientos para cada estación del año.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 51 de 62

|(a) Otoño - EM Catemu 2020.|(b) Otoño - EM Romeral 2020.|
|---|---|
|<br>(c) Invierno - EM Catemu 2020.<br>|<br>(d) Invierno - EM Romeral 2020.|
|<br>(e) Primavera - EM Catemu 2020.|(f) Primavera - EM Romeral 2020.|

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 52 de 62

**Figura No 32.** Rosa de los vientos por estación del año.

**7.2.5 Gráficos ciclo estacional**

En las figuras a continuación, se observa la variación estacional de los ciclos de velocidad y
dirección de viento.

En relación a la dirección de viento a lo largo del año en la estación Catemu el ciclo diario se
mantiene con vientos principalmente desde el sur. Lo anterior indica que la dispersión de gases
se dirige hacia el norte.

En cuanto la velocidad del viento, durante las horas del día en primavera y verano ocurren las
mayores velocidades superando los 2,0 m/s, mientras que en horas de la noche presenta
velocidades del viento inferior a 1,0 m/s, predominando las calmas en las mañanas y noches.

En los meses de invierno y otoño las velocidades también varían durante el día alcanzando un
máximo de 1,5 m/s en las horas de la tarde para luego disminuir a valores menores a 1,0 m/s
durante la noche y la mañana.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 53 de 62

**Figura No 33.** Ciclos estacionales - datos observados estación Catemu - Año 2020. [11]

En cuanto a la Estación Romeral, el ciclo diario presenta variantes de dirección, con una leve
connotación de la dirección este. Lo anterior indica que la dispersión de gases se dirige hacia
el oeste.

En cuanto la velocidad del viento, durante las horas del día en primavera y verano ocurren las
mayores velocidades superando los 6,0 m/s, mientras que en horas de la noche presenta
velocidades del viento inferior a 3,0 m/s, predominando las calmas en las mañanas y noches.

En los meses de invierno y otoño las velocidades también varían durante el día alcanzando un
máximo de 4,0 m/s en las horas de la tarde para luego disminuir a valores menores a 2,0 m/s
durante la noche y la mañana.

**Figura No 34.** Ciclos estacionales - datos observados estación Romeral - Año 2020.

11 Las flechas indican hacia donde se dirige el viento.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 54 de 62

**7.2.6 Elevación de Terreno**

La zona modelada corresponde a un sector ubicado al norte de la región Metropolitana, en la
depresión intermedia, la que se encuentra rodeada por un cordón de cerros hacia el norte y
hacia el este, alcanzando elevaciones de hasta 2.000 m.s.n.m., sin embargo, la planta se
encuentra emplazada entre 336 y 400 m.s.n.m., en el límite norte de la comuna de Llay Llay.

**Figura No 35.** Elevación de terreno archivo WRF.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 55 de 62

**Anexo No3. Análisis incertidumbre**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para
ello se utilizan los datos disponibles en las estaciones de monitoreo ubicadas en la zona de
interés para el estudio.

Las estaciones de monitoreo analizadas Catemu y Romeral, se encuentran a 19 y 18 km
respectivamente del plantel de cerdos, hacia el noroeste. Los parámetros monitoreados por
dicha estación corresponden a velocidad y dirección de viento. Para la evaluación del
desempeño se realiza una comparación entre dichas variables, ya que éstas son las variables
de mayor interés.

Con el fin de evaluar el desempeño, se realiza un análisis cualitativo de los parámetros de
interés. El análisis cualitativo se desarrolla mediante la comparación entre los ciclos diarios
promedios, mensuales, ciclos estacionales y rosa de los vientos.

Definiciones

**Datos observados:** Se refiere a los datos provenientes desde una estación de monitoreo
durante un periodo de interés.

**Datos modelados:** Se refiere a los datos meteorológicos provenientes desde un modelo de
pronóstico como WRF o MM5.

**Rango 90% observado:** Se refiere a la variación de los datos entre el percentil 5 y percentil 95
en una hora o mes específico.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 56 de 62

**7.3.1 Ciclos Diarios promedios**

Velocidad de viento

**Figura No 36.** Comparación ciclo diario de velocidad de viento entre datos observados y

proyectados para la estación de Catemu.

**Figura No 37.** Comparación ciclo diario de velocidad de viento entre datos observados y

proyectados para la estación de Romeral.

De las figuras anteriores se puede concluir que el ciclo diario promedio de velocidad de viento
entre los datos observados y los datos modelados presenta valores sobrestimados entre ±1 m/s
y ±2 m/s en el WRF en comparación a la estación Catemu, observándose la mayor diferencia
en el horario diurno. Por otro lado, en la estación Romeral los valores se encuentran
sobrestimados de igual manera entre ±1 m/s y ±2 m/s en comparación al WRF.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 57 de 62

Dirección de Viento

**Figura No 38.** Comparación ciclo diario de dirección de viento entre datos observados y

proyectados para la estación de Catemu.

**Figura No 39.** Comparación ciclo diario de dirección de viento entre datos observados y

proyectados para la estación de Romeral.

De la figura anterior se puede concluir que la moda diaria de dirección del viento entre los datos
observados y los datos modelados presentan valores y patrones similares entre la estación de
Catemu y Romeral, existiendo diferencias puntuales, principalmente en horarios diurnos.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 58 de 62

**7.3.2 Promedio Mensuales**

Velocidad de viento

**Figura No 40.** Comparación moda mensual de velocidad de viento entre datos observados y

proyectados para la estación de Catemu.

**Figura No 41.** Comparación moda mensual de velocidad de viento entre datos observados y

proyectados para la estación de Romeral.

De las figuras anteriores se puede concluir que el promedio mensual de velocidad de viento
entre los datos observados y los datos modelados presentan valores similares con una
diferencia de ±2 m/s para la estación de Catemu, mientras que Romeral presenta una
considerable similitud en sus velocidades. La variación mensual de velocidad posee el mismo
patrón del modelo de pronóstico y el observado.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 59 de 62

Dirección de Viento

**Figura No 42.** Comparación moda mensual de dirección de viento entre datos observados y

proyectados para la estación de Catemu.

**Figura No 43.** Comparación moda mensual de dirección de viento entre datos observados y

proyectados para la estación de Romeral.

De las figuras anteriores se puede concluir que la moda mensual de dirección del viento entre
los datos observados y los datos modelados presentan valores similares la mayor parte del año,
variando principalmente 45°. Dado estas circunstancias, respecto a la moda mensual de
dirección de viento, el modelo es adecuado.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 60 de 62

**7.3.3 Dirección de viento**

Rosa de los vientos

|(a) EM Catemu - OBS|(b) EM Catemu - WRF|
|---|---|
|<br>(c) EM Catemu - OBS|<br>(d) EM Catemu - WRF|

**Figura No 44.** Comparación Rosas de viento.

De las rosas de los vientos mostradas, se puede observar que el modelo de pronóstico presenta
una considerable similitud con los datos observados. Se observan diferencias de velocidad

entre los datos observados sobreestimados para ambas estaciones en menos de 2 m/s. Se
considera esta diferencia aceptable.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 61 de 62

**7.3.4 Análisis cuantitativo**

De acuerdo a lo solicitado por la Guía para uso de modelos de calidad del aire en el SEIA, se
presenta el análisis cuantitativo de las variables meteorológicas involucradas en la modelación.
En el análisis se incluye las variables temperatura y velocidad de viento, con las métricas
solicitadas: Sesgo (error medio) y error medio cuadrático.

**Tabla No 24.** Análisis cuantitativo.

|Parámetro|Métrica|Catemu|Col4|Romeral|Col6|
|---|---|---|---|---|---|
|**Parámetro**|**Métrica**|**Horario**|**Diario**|**Horario**|**Diario**|
|**Velocidad**|** RMSE**|1,36 m/s|0,82 m/s|2,09 m/s|0,87m/s|
|**Velocidad**|**BIAS**|0,69 m/s|0,68 m/s|-0,27 m/s|-0,27 m/s|
|**Dirección**|**BIAS**|11,12 °|36,25 °|6,89 °|-5,84 °|

Los resultados anteriores son comunes en archivos meteorológicos WRF. Se puede concluir
que los datos del modelo de pronóstico se asemejan a los datos observados, y puede ser usado
en la modelación.

Inf01E02.O-21-024. EIO Cristal Chile (Modelación).cfa 62 de 62