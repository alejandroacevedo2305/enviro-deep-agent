---
title: Sin título
author: Users-Pre-Installed
date: D:20210422135917-04'00'
language: es
type: report
pages: 63
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME Estudio de Impacto Odorante de Planta de Tratamiento de Aguas Servidas, Curepto. 22 de abril de 2021 Inf02E05.O-20-010
-->

# INFORME Estudio de Impacto Odorante de Planta de Tratamiento de Aguas Servidas, Curepto. 22 de abril de 2021 Inf02E05.O-20-010

## Datos del Proyecto

**Empresa** **:** Nuevosur S.A.

**Planta** **:** Planta de Tratamiento de Aguas Servidas, Curepto.

**Coordinador** **:** Javier Cartes (Gestec).

**Jefe de Proyecto** **:** Claudio Burdiles Melgarejo (CBM).

**Ingenieros de Proyecto** **:** Carolina Freire Ávila (CFA).

**Fecha** **:** 22 de abril de 2021.

|Emisión|Datos|Preparó|Revisó|Aprobó|
|---|---|---|---|---|
|Rev0. Versión<br>Final|Nombre|CFA|CBM|CBM|
|Rev0. Versión<br>Final|Fecha|22-04-2021|22-04-2021|22-04-2021|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 2 de 63

**Índice General**

**1** **Resumen ............................................................................................................................. 6**

**2** **Introducción ..................................................................................................................... 10**

**3** **Objetivo General .............................................................................................................. 11**

Objetivos específicos .................................................................................................. 11
**4** **Metodología ...................................................................................................................... 11**

Caracterización de las fuentes de emisión de olor. ..................................................... 12

Estimación de concentración y emisiones de olor ....................................................... 12

4.2.1 Procedimiento. ................................................................................................. 12

Evaluación de la dispersión de las emisiones de olor. ................................................. 13

4.3.1 Selección del modelo ....................................................................................... 13

4.3.2 Recopilación de los antecedentes para la modelación ..................................... 14

4.3.3 Variables meteorológicas y geofísicas ............................................................. 14

4.3.4 Evaluación de los resultados ........................................................................... 15

4.3.5 Área de Influencia y receptores de interés. ...................................................... 16

Evaluación del desempeño del archivo de pronóstico utilizado ................................... 16
**5** **Resultados ....................................................................................................................... 18**

Caracterización de las fuentes de emisión .................................................................. 18

5.1.1 Escenario Actual .............................................................................................. 18

Ubicación de fuentes ................................................................................................... 19

5.2.1 Escenario Futuro ............................................................................................. 20

Ubicación de fuentes ................................................................................................... 21

Emisiones de olor. ....................................................................................................... 22

5.4.1 Emisiones Escenario Actual. ............................................................................ 22

5.4.2 Emisiones Escenario Futuro. ........................................................................... 24

5.4.3 Dispersión de emisiones .................................................................................. 28

**6** **Conclusiones ................................................................................................................... 41**

**7** **Anexos .............................................................................................................................. 42**

Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación ............ 42
Anexo No2. Análisis de receptores. ............................................................................. 43
Anexo No3. Descripción meteorológica y geofísica de la zona. ................................... 47

7.3.1 Cantidad de Datos ........................................................................................... 47

7.3.2 Gráficos Ciclo diario ......................................................................................... 49

7.3.3 Gráficos Distribución de Vientos ...................................................................... 50

7.3.4 Rosa de los Vientos ......................................................................................... 52

7.3.5 Ciclo estacional ................................................................................................ 54

7.3.6 Elevación de Terreno ....................................................................................... 55

Anexo No4. Análisis de incertidumbre. ......................................................................... 56

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 3 de 63

7.4.1 Ciclos diarios promedios .................................................................................. 56

7.4.2 Promedio Mensual ........................................................................................... 58

7.4.3 Rosas de los vientos ........................................................................................ 60

7.4.4 Gráficos Ciclos estacionales ............................................................................ 60

7.4.5 Análisis Cuantitativo......................................................................................... 62

**Índice de Tablas**

**Tabla No 1** . Emisión por fuente. ................................................................................................ 6
**Tabla No 2** . Concentración receptores. Percentil 98. ................................................................ 9
**Tabla No 3** . Variables de entrada consideradas en la modelación. ......................................... 14
**Tabla No 4.** Características del archivo meteorológico WRF. ................................................. 15
**Tabla No 5** . Límites de inmisión según la normativa colombiana, para el percentil 98. ........... 15
**Tabla No 6.** Descripción fuentes y procesos asociados. ......................................................... 18
**Tabla No 7.** Coordenadas de fuentes de emisión odorantes. .................................................. 19
**Tabla No 8.** Coordenadas de referencia de fuentes de emisión odorantes. ............................ 21
**Tabla No 9.** Emisión de olor, fuentes de área pasivas. ........................................................... 23
**Tabla No 10.** Emisión de olor de la fuente de volumen. .......................................................... 23

**Tabla No 11.** Emisión de olor de las fuentes consideradas en la modelación. ........................ 26
**Tabla No 12** . Máxima concentración. Escenario actual. .......................................................... 29
**Tabla No 13** . Receptores discretos considerados en la modelación. ...................................... 31
**Tabla No 14** . Concentración receptores. Escenario Actual, percentil 98. ................................ 32
**Tabla No 15** . Protocolo FIDOL, Escenario Actual. .................................................................. 33
**Tabla No 16** . Máxima concentración. Escenario futuro. .......................................................... 36
**Tabla No 17** . Receptores considerados en la modelación. ..................................................... 37
**Tabla No 18** . Concentración receptores. Escenario Futuro, Percentil 98. ............................... 38
**Tabla No 19** . Protocolo FIDOL, Escenario Futuro. .................................................................. 40
**Tabla No 20** . Estaciones meteorológicas. ............................................................................... 47
**Tabla No 21.** Datos válidos estación meteorológica Lien. ....................................................... 48
**Tabla No 22.** Análisis estadístico Estación Lien. ..................................................................... 62

**Índice de Figuras**

**Figura No 1** . Mapa de concentración de olor generado por las fuentes de emisión de la planta
(Percentil 98). Escenario Actual. ............................................................................................... 7
**Figura No 2** . Mapa de concentración de olor generado por las fuentes de emisión de la planta
(Percentil 98). Escenario Futuro. .............................................................................................. 8
**Figura No 3** . Área del estudio de impacto odorante. ............................................................... 11
**Figura No 4** . Diagrama metodología de caracterización de olor. ............................................ 13
**Figura No 5** . Diagrama de flujo, Planta de Tratamiento de Aguas Servidas, Curepto. Escenario
Actual. .................................................................................................................................... 19
**Figura No 6** . Fuentes consideradas en el escenario actual. .................................................... 20
**Figura No 7** . Diagrama de flujo, Planta de Tratamiento de Aguas Servidas, Curepto. Escenario
Futuro. .................................................................................................................................... 21
**Figura No 8** . Fuentes consideradas en el escenario futuro. .................................................... 22
**Figura No 9** . Distribución porcentual de las emisiones generadas actualmente en la PTAS
Curepto. ................................................................................................................................. 24
**Figura No 10** . Distribución porcentual de las futuras emisiones de la PTAS Curepto. ............ 27

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 4 de 63

**Figura No 11** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio
horario, percentil 98. Escenario actual. ................................................................................... 28
**Figura No 12** . Área de Influencia. Escenario actual. ............................................................... 30
**Figura No 13** . Receptores de interés considerados en la modelación. ................................... 31
**Figura No 14** . Mapa de horas sobre 3 OU E /m3 generado por las fuentes de emisión de la
PTAS Curepto, promedio horario. Escenario actual. ............................................................... 33
**Figura No 15** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio
horario (percentil 98), Escenario futuro. .................................................................................. 35
**Figura No 16** . Área de Influencia. Escenario futuro................................................................. 36
**Figura No 17** . Receptores de interés considerados en la modelación. ................................... 38
**Figura No 18** . Mapa de horas sobre 3 OU E /m3 generado por las fuentes de emisión de la
PTAS Curepto, promedio horario. Escenario futuro. ............................................................... 39
**Figura No 19** . Esquema funcionamiento CALPUFF. ............................................................... 42
**Figura No 20** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No4. ........ 43
**Figura No 21** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No5. ........ 43
**Figura No 22** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No6. ........ 44
**Figura No 23** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No4. ........ 45
**Figura No 24** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No5. ........ 45
**Figura No 25** . Concentraciones horarias (OUE/m [3] ), Distribución horaria. Receptor No6. ........ 46
**Figura No 26** . Serie de tiempo anual. Velocidad de viento. Estación Lien. ............................. 47
**Figura No 27** . Serie de tiempo anual. Dirección de viento. Estación Lien. .............................. 48
**Figura No 28** . Serie de tiempo anual. Temperatura. Estación Lien. ........................................ 48
**Figura No 29** . Ciclo diario para velocidad de viento. Estación Lien. ........................................ 49
**Figura No 30** . Ciclo diario para dirección de viento. Estación Lien. ......................................... 49
**Figura No 31** . Ciclo diario de temperatura. Estación Lien. ...................................................... 50
**Figura No 32** . Distribución velocidades de viento en la zona del proyecto. Estación Lien. ...... 51
**Figura No 33** . Rosa de los vientos anual. Estación Lien. ........................................................ 52
**Figura No 34** . Rosa de los vientos por estación Lien, año 2019. ............................................ 53
**Figura No 35** . Gráfico ciclo estacional, Estación Lien. ............................................................ 54
**Figura No 36** . Elevación de terreno archivo WRF. .................................................................. 55
**Figura No 37** . Comparación ciclo diario de velocidad del viento entre datos observados y
modelados para la estación Lien. ........................................................................................... 56
**Figura No 38** . Comparación ciclo diario de dirección de viento entre datos observados y
modelados para la estación Lien. ........................................................................................... 57
**Figura No 39** . Comparación ciclo diario de temperatura entre los datos observados y
modelados para la estación Lien. ........................................................................................... 58
**Figura No 40** . Comparación ciclo mensual de velocidad de viento entre los datos observados
y modelados para la estación Lien.......................................................................................... 58
**Figura No 41** . Comparación ciclo mensual de dirección de viento entre datos observados y
modelados para la estación Lien. ........................................................................................... 59
**Figura No 42** . Comparación ciclo mensual de temperatura entre datos observados y
modelados para la estación Lien. ........................................................................................... 59
**Figura No 43.** Rosa de los vientos Estación Lien. ................................................................... 60
**Figura No 44** . Variación estacional de velocidad y dirección de viento EM Lien. .................... 61
**Figura No 45** . Variación estacional de velocidad y dirección de viento WRF Lien. ................. 62

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 5 de 63

**1** **Resumen**

En el marco de la Declaración de Impacto Ambiental para conocer el potencial impacto odorante
de la Planta de Tratamiento de Aguas Servidas de la comuna de Curepto (en adelante la PTAS
Curepto), Nuevosur S.A, a través de Gestec, solicitó los servicios de Proterm S.A. para realizar
un Estudio de Impacto Odorante, en Adelante EIO. El presente estudio incorpora la modelación
de dispersión atmosférica de la situación actual y futura, con la finalidad de determinar y/o
descartar la posible afectación a la calidad de vida de las personas, producto de la operación
de la planta ubicada en la comuna de Curepto, provincia de Talca, región del Maule.

Los resultados son presentados en dos informes: (A) Toma de muestra y resultados de
concentración de olor mediante olfatometría dinámica en Planta de Tratamiento de Aguas
Servidas, Curepto. (Inf01E01 O-20-010.) y (B) Estudio de Impacto Odorante, cuyos resultados
se entregan en el presente informe.

El estudio de Impacto Odorante, en su escenario actual analiza la emisión de olor generada por
las siguientes fuentes: (a) reactor aeróbico, (b) sedimentador, (c) digestor aeróbico/espesador,
(d) cámara de contacto y (e) lechos de secado. Es importante señalar que durante este
escenario no se consideran las emisiones del pretratamiento porque sus dimensiones son
pequeñas y por ende, su emisión es despreciable. Por otro lado, para la ampliación de la planta,
al año 2034, se considera implementar (a) pretratamiento compacto, (b) ampliar el reactor
aeróbico, (c) transformación del actual sedimentador a digestor aeróbico de lodos, (d)
construcción de un nuevo sedimentador, (e) implementar un sistema de deshidratado, (f)
construcción de una cámara de contacto e (g) incorporación de un espesador dinámico. Es
importante señalar, que adicionalmente el escenario futuro considera la implementación de una
cámara de lodos y un espesador dinámico cuyas unidades se encontrarán cerradas, estas
unidades no se consideraron en el modelo ya que sus emisiones no saldrán a la atmósfera. A
partir de los escenarios evaluados, se obtuvieron las siguientes emisiones de olor:

**Tabla No 1** . Emisión por fuente.

|Identificación fuente de olor|Estado|Tipo de fuente|Emisión (OU /s)<br>E|Col5|
|---|---|---|---|---|
|**Identificación fuente de olor**|**Estado**|**Tipo de fuente**|**E. Actual**|**E. Futuro**|
|Reactor aeróbico|Existente|Difusa área pasiva|31|48|
|Sedimentador|Existente|Difusa área pasiva|4|10|
|Cámara de contacto|Existente|Difusa área pasiva|2|5|
|Digestor aeróbico1|Existente|Difusa área pasiva|24|50|
|Espesador|Existente|Difusa área pasiva|7|-|
|Lechos de secado|Existente|De volumen|390|-|
|Pretratamiento compacto|Proyectada|Difusa área pasiva|-|1|
|Tornillo deshidratado|Proyectada|De volumen|-|68|
|Contenedor de lodos|Proyectada|Difusa área pasiva|-|9|

1 Las emisiones generadas por el digestor aeróbico, en la modelación del escenario actual, considera las emisiones
generadas en forma discontinua (batch), por el digestor aeróbico que funciona 6 días a la semana y el espesador
que funciona 1 día. Lo anterior porque ambas procesos se llevan a cabo en la misma unidad.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 6 de 63

|Identificación fuente de olor|Estado|Tipo de fuente|Emisión (OU /s)<br>E|Col5|
|---|---|---|---|---|
|**Identificación fuente de olor**|**Estado**|**Tipo de fuente**|**E. Actual**|**E. Futuro**|
|**Total**|**Total**|**Total**|**458**|**191**|

Es importante señalar que, el espesador dinámico que se incorporará será una unidad cerrada,
por lo que en el escenario futuro no se generarían emisiones a la atmósfera.

Una vez obtenidas las emisiones de olor de cada fuente, se ingresaron al modelo de dispersión
atmosférica calpuff, el cual permitió conocer la concentración y dispersión de los olores, tanto
en el área de estudio como en los receptores discretos cercanos al proyecto, los cuales
corresponden principalmente a viviendas cercanas a la planta y a un galpón.

Debido a que en Chile no existe normativa que regule la emisión ni la inmisión de olores por
parte de una planta de estas características, se utiliza como referencia normativas
internacionales. Por lo que las concentraciones de olor (OU E /m [3] ), resultantes del modelo, para
cada receptor discreto, fueron comparados con el límite de inmisión establecido en la normativa
colombiana para plantas de tratamiento de aguas servidas. En esta normativa se establece un
límite de inmisión de 3 OU E /m [3], para percentil 98, que aplica a la contaminación de olor
generada por plantas de tratamiento de aguas servidas.

**Figura No 1** . Mapa de concentración de olor generado por las fuentes de emisión de la planta

(Percentil 98). Escenario Actual.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 7 de 63

**Figura No 2** . Mapa de concentración de olor generado por las fuentes de emisión de la planta

(Percentil 98). Escenario Futuro.

Para el escenario actual, la dispersión de las emisiones de olor de la PTAS Curepto indican que
en los alrededores de la planta se producen concentraciones que van entre los 0,4 y 3,0 OU E /m3
durante el 98% del año, distribuyéndose en forma radial, abarcando un área total de 1,26 ha
para la isodora de 1 OU E /m3. Por otro lado, se puede observar que en el escenario futuro, las
concentraciones alrededor de la planta alcanzan entre los 0,4 y 1,0 OU E /m3 durante el 98% del
año, manteniéndose la misma tendencia de distribución del olor, mientras que la isodora de 1
OU E /m3 abarca un área de 0,26 ha. Es importante señalar, que a pesar de presentar un aumento
de emisiones de olor en la mayoría de las fuentes, el cambio del sistema de tratamiento de
lodos de lecho de secado a un tornillo de deshidratado se observa una disminución de un 58%

en las emisiones.

A partir de lo anteriormente señalado, se puede concluir que en ninguno de los escenarios
evaluados se registraría superación del límite de inmisión establecido en la normativa
colombiana (3 OU E /m [3] ).

El área de influencia en la operación actual, de las fuentes generadoras de olor de la PTAS
Curepto, cubre un área total de 1,26 ha, mientras que en el escenario futuro, el área de
influencia cubriría un área total de 0,26 ha. Esta área circunscrita por 1 OU E /m [3], se establece
según la “Guía para la predicción y evaluación de impactos por olor en SEIA” del año 2017, la
cual indica la concentración en donde el 50% de la población puede comenzar a detectar un

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 8 de 63

olor.

A continuación, se presentan los resultados de concentración de olor en los receptores
considerados en ambos escenarios (actual y futuro):

**Tabla No 2** . Concentración receptores. Percentil 98.

|No|Descripción|Concentración de inmisión<br>(OU /m3)<br>E|Col4|Límite<br>inmisión2|Horas sobre 3 OU /m3<br>E|Col7|
|---|---|---|---|---|---|---|
|**No**|**Descripción**|**Escenario**<br>**Actual**|**Escenario**<br>**Futuro**|**Escenario**<br>**Futuro**|**Escenario**<br>**Actual**|**Escenario**<br>**Futuro**|
|R1|Vivienda|0,18|0,08|3 <br>OUE/m3 <br>(percentil 98)|0 (0,00%)|0 (0,00%)|
|R2|Vivienda|0,15|0,09|0,09|0 (0,00%)|0 (0,00%)|
|R3|Vivienda|0,24|0,13|0,13|0 (0,00%)|0 (0,00%)|
|R4|Vivienda|0,40|0,22|0,22|9 (0,10%)|0 (0,00%)|
|R5|Vivienda|0,48|0,25|0,25|13 (0,15%)|0 (0,00%)|
|R6|Galpón|0,43|0,22|0,22|14 (0,16%)|0 (0,00%)|
|R7|Vivienda|0,29|0,14|0,14|2 (0,02%)|0 (0,00%)|

2 Como normativa de referencia se utilizó el límite de inmisión propuesto en la normativa colombiana.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 9 de 63

**2** **Introducción**

La Planta de Tratamiento de Aguas Servidas Curepto, se encuentra ubicada al noroeste de la
comuna de Curepto, provincia de Talca, Región del Maule. Presenta, actualmente, un sistema
de tratamiento biológico de lodos activados que consta de un pretratamiento, tratamiento
secundario (compuesto por un reactor aeróbico y un sedimentador) y por un sistema de
desinfección del efluente para luego ser descargado al estero Lien. Por otro lado, cuenta con
un tratamiento de lodos el cual está conformado por un digestor aeróbico que funciona en
condiciones discontinuas como digestor y como espesador [3] y cuenta, además, con lechos de
secado donde se disminuye la humedad del lodo para disponerlo en un lugar autorizado.

Al año 2034, se proyecta la ampliación de la capacidad de tratamiento de la planta que contará
con un sistema de pretratamiento compacto, reactor biológico con sedimentación, digestión
aeróbica de lodos y un sistema de deshidratado del tipo tornillo. Es por lo anteriormente
señalado, que se proyectan las siguientes modificaciones: (a) implementación de un
pretratamiento compacto, (b) se ampliará el reactor biológico a través de la transformación del
espesador/digestor de lodos, (c) el sedimentador existente se transformará en digestor de
lodos, (d) construirá un nuevo sedimentador, (e) incorporación de un espesador dinámico, (f)
implementación de un tornillo de deshidratado, (g) construcción de una nueva cámara de
contacto, (h) nueva estructura para tableros eléctricos y (i) una PEAS retorno.

Nuevosur S.A, a través de Gestec, solicitó los servicios de Proterm S.A. para realizar un Estudio
de Impacto Odorante (EIO), con el objetivo de evaluar el efecto actual y futuro de las emisiones
de olor generadas por la PTAS Curepto.

La PTAS Curepto es un proyecto en operación, por lo que se procedió a determinar las
emisiones de referencia de la operación actual de la planta, tal como lo indica la “Guía para
predicción y evaluación de los impactos por olor en el SEIA”. Los escenarios evaluados
consideraron las emisiones de olor generadas en la operación actual de la PTAS Curepto y su
futura operación. Las emisiones consideradas fueron obtenidas mediante mediciones de olor
realizados bajo lo indicado en la NCh 3386.of.2015 “Muestreo estático para olfatometría”, NCh
N°3431 Of.2020 “Determinación de las emisiones difusas por mediciones” y NCh 3190:2010
“Calidad de aire - Determinación de la concentración de olor por olfatometría dinámica”.

A continuación, se detalla la ubicación espacial del área considerada en el Estudio de Impacto
Odorante de la PTAS Curepto.

3 La misma unidad funciona alternadamente entre digestor y espesador. En promedio, el ciclo de operación como
digestor es de 6 días a la semana y 1 día funciona como espesador

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 10 de 63

**Figura No 3** . Área del estudio de impacto odorante.

**3** **Objetivo General**

Evaluar el efecto de las emisiones de olor generadas por la Planta de Tratamiento de Aguas
Servidas de Curepto, sobre la salud de la población cercana, sistemas de vida, costumbres,
población protegida y turismo.

**Objetivos específicos**

 - Determinar la tasa de emisión de olor de las fuentes monitoreadas.

 Determinar la dispersión de las emisiones de olor del proyecto en evaluación.

 Comparar los valores de concentración de inmisión de olor con el límite establecido en
la normativa internacional.

**4** **Metodología**

A continuación, se presenta la metodología que permitió evaluar el efecto de las emisiones de
olor del proyecto.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 11 de 63

**Caracterización de las fuentes de emisión de olor.**

Para poder caracterizar las fuentes generadoras de olor actuales de la planta, se utilizó el
siguiente procedimiento:

 - Verificación en terreno: Se realizó una ronda de identificación de fuentes, con el objetivo
de verificar la ubicación de cada una de ellas, dicho recorrido lo realizó personal de
Proterm en conjunto con personal de planta.

 - Detección satelital: Mediante Google Earth Pro [4], se identificaron las superficies de las
fuentes generadoras de olor y la distancia de los receptores con respecto a la planta.

 - Solicitud de información al cliente: Información donde se especifican dimensiones y
emplazamiento de las fuentes actuales y las futuras modificaciones que se
implementaran.

**Estimación de concentración y emisiones de olor**

Luego de una caracterización del proceso y las fuentes de emisión, se procede a la realización
de las siguientes actividades para determinar la tasa de emisión de olor de la planta:

**4.2.1 Procedimiento.**

El siguiente esquema detalla el procedimiento realizado para medir las emisiones de planta.

4 Versión 7.1.5.1557 de Google Earth

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 12 de 63

**Figura No 4** . Diagrama metodología de caracterización de olor.

En las fuentes seleccionadas de la planta de tratamiento de aguas servidas, se realizó un
muestreo estático bajo la NCh N°3386 Of.2015 y NCh N°3431 Of.2020 para posteriormente
realizar un análisis olfatométrico bajo la NCh N°3190 Of.2010, el que se llevó a cabo en el
laboratorio móvil de Proterm, el 14 de mayo de 2020. Es importante señalar que los resultados
del análisis fueron entregados en el informe Inf01E01.O-20-010. “Toma de muestra y resultados
de concentración de olor mediante olfatometría dinámica en Planta de Tratamiento de Aguas
Servidas, Curepto”.

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
trayectoria. Es decir, a diferencia de los modelos Langrangianos que necesitan el cálculo de un

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 13 de 63

gran número de trayectorias para una fuente, los modelos tipo “Puff” sólo requieren una
trayectoria por “Puff”, lo que hace su cálculo mucho más rápido [5] .

Para la modelación se utilizó el software Calpuff versión 7.2.1 junto a los módulos CALPOST
7.1.0. y CALRANK 7.0.0. Además, para efectos de la interacción gráfica de los módulos, se usó
el software interactivo CALPUFF View 8.5.0.

En el Anexo N°1 se presenta el esquema del modelo utilizado y los elementos de la modelación.

**4.3.2 Recopilación de los antecedentes para la modelación**

Para conocer la dispersión que tendrán los gases en un área determinada es preciso incorporar
en el modelo seleccionando distintos parámetros de manera que la simulación sea lo más
parecida a las condiciones reales. Las variables o entradas que requirió el modelo fueron.

**Tabla No 3** . Variables de entrada consideradas en la modelación.

|Variable|Parámetros|Fuente|
|---|---|---|
|Meteorológicas|Dirección de Viento|Tal como lo establece la guía el modelo numérico<br>recomendado para la generación de datos<br>meteorológicos es el Weather Research and<br>Forecasting Model (WRF). WRF es uno de los<br>modelos meteorológicos de pronóstico más<br>avanzados y completos que es mantenido por<br>NCAR/NOAA de Estados Unidos.|
|Meteorológicas|Velocidad de Viento|Velocidad de Viento|
|Meteorológicas|Temperatura|Temperatura|
|Meteorológicas|Presión|Presión|
|Meteorológicas|Precipitación|Precipitación|
|Geofísicas|Elevación del Terreno|Elevación del Terreno|
|Geofísicas|Uso de Suelo|Uso de Suelo|
|Características<br>de la fuente|Ubicación de las fuentes|Información de fuentes consideradas en los<br>escenarios evaluados.|
|Características<br>de la fuente|Descripción del proceso|Descripción del proceso|
|Características<br>de la fuente|Periodo de operación|Periodo de operación|
|Características<br>de la fuente|Emisiones de olor|Emisiones de olor|
|Receptores<br>Discretos|Coordenadas de los receptores|A través del estudio de medio humando, se<br>definieron las viviendas cercanas a la planta.|

**4.3.3 Variables meteorológicas y geofísicas**

Tal como se mencionó en el punto 4.3.2, se utilizó la meteorología de pronóstico WRF en
formato calmet.dat, de esta forma se incorporó el archivo directamente al programa. El archivo
meteorológico tiene su centro en la comuna de Curepto. Para la ejecución del modelo se modeló
una zona más pequeña en comparación al WRF, es importante destacar que la zona modelada
tiene una dimensión de grilla de 250 metros. En la tabla N°4 se presentan las características
del archivo meteorológico y en la figura N°3 los límites indicados (figura en apartado
“introducción”).

5 Guía para el uso de modelos de calidad del aire, 2012

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 14 de 63

**Tabla No 4.** Características del archivo meteorológico WRF.

|Datos|Col2|Archivo Meteorológico|
|---|---|---|
|Comuna Central|Comuna Central|Curepto|
|Dimensión grilla|Dimensión grilla|16x16 km|
|Espaciado grilla|Espaciado grilla|1 km|
|Fecha-Hora inicio|Fecha-Hora inicio|01-01-2019 00:00|
|Fecha-Hora fin|Fecha-Hora fin|31-12-2019 23:00|
|Coordenadas NO6|Este|762.723|
|Coordenadas NO6|Norte|6.121.087|
|Coordenadas NE7|Este|231.147|
|Coordenadas NE7|Norte|6.121.414|
|Coordenadas SO8|Este|762.702|
|Coordenadas SO8|Norte|6.105.095|
|Coordenadas SE9|Este|232.198|
|Coordenadas SE9|Norte|6.105.483|

**4.3.4 Evaluación de los resultados**

Debido a que en Chile no existe normativa que regule la emisión ni la inmisión de olores por
parte de una planta de estas características, se utilizan como referencias normativas
internacionales. En la siguiente tabla se indican los límites de inmisión establecidos en la
normativa colombiana que corresponden a unidades de olor europeas expresadas como el
percentil 98 de las horas modeladas durante un año para diferentes actividades, donde se
incluyen las plantas de tratamiento de aguas servidas y se indica que las comparaciones se
deben realizar con el valor de inmisión de 3 OU E /m [3] y un factor de frecuencia d el percentil 98.

**Tabla No 5** . Límites de inmisión según la normativa colombiana, para el percentil 98 [10] .

|Nivel Permisible<br>OU /m3<br>E|Actividad|
|---|---|
|3|Procesamiento y conservación de carne, pescado, crustáceos y moluscos.<br>Fabricación de productos de la refinación del petróleo.<br>Fabricación de pulpas (pastas) celulósicas; papel y cartón.<br>Curtido y recurtido de cueros; recurtido y teñido de pieles.<br>Tratamiento y disposición de desechos no peligrosos y estaciones de<br>transferencia.<br>**Planta de tratamiento de aguas residuales.**<br>Actividades que capten agua de cuerpos de agua receptores de vertimientos.<br>Fabricación de sustancias y productos químicos básicos.<br>Tratamiento térmico de subproductos de animales.|

6 Coordenadas WGS-84 Huso 18
7 Coordenadas WGS-84 Huso 19
8 Coordenadas WGS-84 Huso 18
9 Coordenadas WGS-84 Huso 19
10 El percentil es una medida de tendencia central usada en estadística que indica el valor de la variable por debajo
[de un porcentaje dado de observaciones ordenados de menor a mayor. El Percentil 98 es el valor bajo el cual se](https://es.wikipedia.org/wiki/Porcentaje)
encuentra el 98 % de los datos horarios de olor registrados durante un año (8760 datos).

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 15 de 63

|Nivel Permisible<br>OU /m3<br>E|Actividad|
|---|---|
|5|Unidad de producción pecuaria.<br>Elaboración de aceites y grasas de origen vegetal.|
|7|Descafeinado, tostión y molienda de café.<br>Otras actividades.|

Es por lo anteriormente señalado, que las concentraciones de olor resultantes del modelo, para
cada receptor discreto, en OU E /m [3], fueron comparados con el límite de inmisión de 3 OU E /m [3],
propuesto en la normativa colombiana, donde se indica que como resultado de la contaminación
por olores de una planta de tratamiento de aguas servidas, no debe superar las 3 OU E /m [3] para
el percentil 98.

Junto a los resultados de concentración de olor, se identificará el área de influencia de la
operación de la planta. Tal como lo indica la guía, el área de Influencia se debe circunscribir en
el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de detección del
olor compuesto.

**4.3.5 Área de Influencia y receptores de interés.**

Una vez ejecutado el modelo de dispersión de olor, se realiza el análisis de post-proceso
obteniendo las curvas iso-concentración de la dispersión anual. Tal como lo indica la guía el
Área de Influencia se debe circunscribir en el espacio contenido por la isodora de 1 OU E /m [3],
que corresponde al umbral de detección del olor compuesto.

Una vez determinada el área de influencia, se realizará una descripción general y significativa
del área de influencia, para cada elemento del medio ambiente, considerando los efectos,
características o circunstancias establecidos en el artículo 11 de la Ley N°19.300 como
población, población protegida, grupos humanos y visitantes o turistas.

De acuerdo a lo establecido en la Guía para la predicción y evaluación de impacto por olor en
el SEIA, señala que _“La evaluación de los impactos ambientales por olor debe realizarse según_
_las consideraciones y criterios establecidos en los artículos del 5 al 9 del Reglamento del SEIA,_
_según lo siguiente”:_

 _Población en cuanto a la salud de la población (letra a)._

 _Grupos humanos, en cuanto a los sistemas de vida y costumbres (letra c)._

 _Población protegida (letra d)._

 _Visitantes o turistas, en cuanto componente el valor turístico de una zona (letra e)._

**Evaluación del desempeño del archivo de pronóstico utilizado**

El modelo numérico recomendado para la generación de datos meteorológicos es el Weather
Research and Forecasting Model (WRF). WRF es uno de los modelos meteorológicos de
pronóstico más avanzados y completos, que es mantenido por NCAR/NOAA de Estados
Unidos.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 16 de 63

Todos los modelos tienen asociados errores e incertidumbre. Los resultados del modelo se

analizan en base a la comparación de los gráficos indicados en los puntos 6.6.3 y 6.7 de la
“Guía para uso de modelos de Calidad del aire en el SEIA”. En base a la comparación de los
ciclos diarios de las variables meteorológicas observadas y simuladas, en la misma, ubicación,
se debe caracterizar la capacidad del modelo de reproducir las observaciones tanto en
magnitud como en su variabilidad.

Para cumplir con lo indicado por la guía para uso de modelos de dispersión del SEA, se realizó
un análisis del desempeño de la meteorología de pronóstico WRF utilizada para la modelación.
Este análisis permite detectar posibles desviaciones en el modelo de pronóstico que podrían
causar efectos en los resultados del modelo de dispersión.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 17 de 63

**5** **Resultados**

A continuación, se presentan los resultados que permitirán evaluar el efecto de las emisiones
de olor del proyecto actual y futuro de la Planta de Tratamiento de Aguas Servidas de la comuna
de Curepto.

**Caracterización de las fuentes de emisión**

A continuación, se describen las fuentes generadoras de olor para ambos escenarios de
modelación. Lo anterior, de acuerdo a lo señalado en el punto 3.3 de la guía para la predicción
y evaluación de olores.

**5.1.1 Escenario Actual**

Actualmente, la PTAS Curepto presenta un sistema de tratamiento biológico de lodos activados
que consta de un pretratamiento, un tratamiento secundario (compuesto por un reactor aeróbico
y un sedimentador) y por un sistema de desinfección del efluente para luego ser descargado al
estero Curepto. Por otro lado, cuenta con un tratamiento de lodos el cual está conformado por
un digestor aeróbico que funciona en condiciones discontinuas como digestor y como
espesador y cuenta, además, con un lecho de secado, donde se disminuye la humedad del
lodo para disponerlo en un lugar autorizado.

A continuación, se presenta una tabla descriptiva de los procesos correspondientes a cada
fuente considerada en el estudio.

**Tabla No 6.** Descripción fuentes y procesos asociados.

|Fuente|Descripción|
|---|---|
|Reactor aeróbico|El tratamiento secundario corresponde a un proceso biológico aeróbico<br>mediante lodos activados. Está emplazado en una unidad compacta metálica<br>que incluye además el digestor aeróbico.<br>El tratamiento secundario se realiza en una unidad metálica elevada con un<br>volumen de 175 m3, con dimensiones 3,36 m x 7,32 m, con inyección de aire<br>desde el fondo, por medio de un sistema de aireación de difusores y<br>sopladores.|
|Sedimentador|Es una unidad metálica independiente de 7 m de diámetro y de 2,8 m de<br>profundidad en la periferia.<br>Recibe el caudal proveniente desde el tratamiento biológico, lo anterior<br>porque cuenta con un sistema de remoción de espumas y flotantes de tipo<br>radial. Cabe señalar que presenta un puente barredor de accionamiento<br>periférico y cubre la totalidad del diámetro.|
|Cámara de contacto|Es un estanque metálico de dimensiones 3,5 m de alto; 3,51 m de profundidad<br>y 1,22 m de ancho con capacidad útil de 11,5 m3. <br>La cámara de contacto recibe por gravedad el agua clarificada proveniente<br>desde el sedimentador. Es importante señalar que esta estructura se<br>encuentra adosada al sedimentador.|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 18 de 63

|Fuente|Descripción|
|---|---|
|Digestor<br>aeróbico/espesador|Se encuentra en el mismo sector del reactor biológico, tiene una capacidad<br>de 78 m3 de volumen útil y funciona tanto como digestor como espesador.<br>El lodo proveniente desde el sedimentador es transportado por airlift (WAS)<br>hasta la parte superior del digestor (El WAS es retirado 1 a 1,5 veces al día).<br>El oxígeno requerido para la digestión es provisto por el mismo sistema de<br>sopladores del reactor y es distribuido por 6 líneas de difusores de tubo de<br>burbuja gruesa en el fondo del estanque.|
|Lechos de secado|La PTAS cuenta con lechos de secado para lograr la disminución de la<br>humedad del lodo requerida y ser dispuesto en sitio autorizado. Consiste en<br>un galpón metálico con 8 lechos de arena, de largo de 10 m con un ancho de<br>5 m, la altura de muro es 1,1 m. El fondo de cada lecho cuenta con una<br>pendiente que permite recolectar los líquidos percolados.|

A continuación, se presenta un diagrama de flujo del proceso actual.

**Figura No 5** . Diagrama de flujo, Planta de Tratamiento de Aguas Servidas, Curepto. Escenario

Actual.

**Ubicación de fuentes**

A continuación, se presenta la ubicación de las fuentes evaluadas en el escenario actual,
mientras que en la imagen se muestra la ubicación espacial de cada una de ellas.

**Tabla No 7.** Coordenadas de fuentes de emisión odorantes.

|Fuente|Tipo de Fuente11|Coordenadas WGS-84 Huso 18S|Col4|
|---|---|---|---|
|**Fuente**|**Tipo de Fuente11 **|**Este (m)**|**Norte (m)**|
|Reactor aeróbico.|Difusa de área pasiva|770.686|6.113.200|

11 De acuerdo a la Guía para la predicción y evaluación de impactos por olor en el SEIA, los tipos de fuentes se
describen como fuentes puntuales, difusas pasivas, difusas activas y fugitivas. No obstante, de acuerdo a la NCh
3386:2015 “Calidad de aire Muestreo estático para olfatometría”, describe la fuente pasiva como fuente con
dimensiones definidas (fuente de área, fuentes de volumen) que no tienen un flujo de aire de salida definida, tales
como depósitos de desechos, lagunas, campos después de esparcir estiércol, pilas de compost no aireados,
**edificaciones** . Junto a lo anterior en la sección 8.1.2. se detalla la toma de muestra en “Fuentes de Volumen”, la
cual fue aplicada para las edificaciones en este estudio.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 19 de 63

|Fuente|Tipo de Fuente11|Coordenadas WGS-84 Huso 18S|Col4|
|---|---|---|---|
|**Fuente**|**Tipo de Fuente11 **|**Este (m)**|**Norte (m)**|
|Sedimentador.|Difusa de área pasiva|770.691|6.113.209|
|Cámara de contacto.|Difusa de área pasiva|770.692|6.113.214|
|Digestor aeróbico/espesador|Difusa de área pasiva|770.683|6.113.195|
|Lechos de secado.|Difusa de volumen|770.704|6.113.225|

**Figura No 6** . Fuentes consideradas en el escenario actual.

**5.2.1 Escenario Futuro**

Al año 2034, se proyecta la ampliación de la capacidad de tratamiento de la planta, que contará
con un sistema de pretratamiento compacto, reactor aeróbico con sedimentador, espesado y
digestión aeróbica de lodos y un sistema de deshidratado del tipo tornillo. Es por lo
anteriormente señalado, que se proyectan las siguientes modificaciones: (a) incorporación de
un pretratamiento compacto, (b) el espesador/ digestor existente se transformará en reactor,
(c) el sedimentador existente se transformará en digestor de lodos, (d) se construirá un
sedimentador, (e) implementación de una cámara de lodos, (f) se incorporará un espesador

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 20 de 63

dinámico [12], (g) se implementará un tornillo de deshidratado, (h) se construirá una nueva cámara
de contacto, (i) nueva estructura para tableros eléctricos y (j) una PEAS retorno.

A continuación, se presenta un diagrama de flujo donde se incluyen las modificaciones
proyectadas para la PTAS Curepto:

**Figura No 7** . Diagrama de flujo, Planta de Tratamiento de Aguas Servidas, Curepto. Escenario

Futuro.

**Ubicación de fuentes**

A continuación, se presenta la ubicación de las fuentes que fueron evaluadas en el escenario
futuro, mientras que en la imagen se muestra la ubicación espacial de cada una de ellas.

**Tabla No 8.** Coordenadas de referencia de fuentes de emisión odorantes.

|Fuente|Tipo de Fuente13|Coordenadas WGS-84 Huso 18S|Col4|
|---|---|---|---|
|**Fuente**|**Tipo de Fuente13 **|**Este (m)**|**Norte (m)**|
|Pretratamiento compacto.|De área pasiva|770.680|6.113.201|
|Reactor aeróbico.|De área pasiva|770.686|6.113.200|
|Sedimentador.|De área pasiva|770.712|6.113.216|
|Cámara de contacto.|De área pasiva|770.705|6.113.215|
|Digestor aeróbico.|De área pasiva|770.690|6.113.208|
|Tornillo deshidratado.|De volumen|770.706|6.113.205|

12 Es importante señalar que la cámara de lodos, el espesador dinámico y la PEAS de retorno son unidades cerradas
por lo que no se consideran en la modelación, lo anterior porque no generan emisiones de olores a la atmósfera.
13 De acuerdo a la Guía para la predicción y evaluación de impactos por olor en el SEIA, los tipos de fuentes se
describen como fuentes puntuales, difusas pasivas, difusas activas y fugitivas. No obstante, de acuerdo a la NCh
3386:2015 “Calidad de aire Muestreo estático para olfatometría”, describe la fuente pasiva como fuente con
dimensiones definidas (fuente de área, fuentes de volumen) que no tienen un flujo de aire de salida definida, tales
como depósitos de desechos, lagunas, campos después de esparcir estiércol, pilas de compost no aireados,
**edificaciones** . Junto a lo anterior en la sección 8.1.2. se detalla la toma de muestra en “Fuentes de Volumen”, la
cual fue aplicada para las edificaciones en este estudio.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 21 de 63

|Fuente|Tipo de Fuente13|Coordenadas WGS-84 Huso 18S|Col4|
|---|---|---|---|
|**Fuente**|**Tipo de Fuente13 **|**Este (m)**|**Norte (m)**|
|Contenedor de lodos.|De área pasiva|770.707|6.113.207|

**Figura No 8** . Fuentes consideradas en el escenario futuro.

**Emisiones de olor.**

**5.4.1 Emisiones Escenario Actual.**

En la siguiente tabla, se presentan las emisiones de olor de las fuentes que fueron muestreadas
bajo la NCh N° 3386 Of.2015, NCh N°3431 Of.2020 y su posterior análisis olfatométrico acorde
a la NCh 3190 Of.2010, cabe destacar que el terreno se realizó el 14 de mayo del presente año.
Para mayor información, revisar el informe (A)Inf01E01.O-20-010.“Toma de muestra y
resultados de concentración de olor mediante olfatometría dinámica en Planta de Tratamiento

de Aguas Servidas, Curepto.”
Como se mencionó anteriormente, en la misma unidad donde se encuentra emplazado el
reactor aeróbico, se encuentra el digestor aeróbico que funciona en condiciones discontinuas
(batch) como digestor (6 días) y como espesador de lodos (1 día). Es importante señalar, que
el día en que se realizó la medición, esta unidad estaba funcionando como digestor, por lo que

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 22 de 63

fue necesario homologar la emisión del espesador con la medición realizada en la PTAS
Quirihue, [14] donde se indica que la emisión de dicha unidad es de 0,36 OU E /m [2] /s.

A continuación, se detallan las emisiones consideradas en el escenario actual:

**Tabla No 9.** Emisión de olor, fuentes de área pasivas.

|Fuente|Concentración de<br>olor (OU /m3)<br>E|Superficie<br>(m2)|Emisión por área<br>(OU /m2/s)<br>E|Emisión de olor<br>(OU /s)<br>E|
|---|---|---|---|---|
|Reactor aeróbico|78|48|0,65|31|
|Sedimentador|13|35|0,11|4|
|Cámara de contacto|44|5|0,37|2|
|Digestor aeróbico|155|19|1,29|24|
|Espesador|4415|19|0,3616|7|

**Tabla No 10.** Emisión de olor de la fuente de volumen.

|Fuente|Concentración<br>de olor<br>(OU /m3)<br>E|Superficie<br>abertura<br>(m2)|Velocidad<br>promedio<br>(m/s)|Flujo<br>(m3/s)|Emisión<br>por área<br>(OU /m2/s)<br>E|Emisión<br>de olor<br>(OU /s)<br>E|
|---|---|---|---|---|---|---|
|Lechos de secado|<12|89|0,4|32,98|<4,37|<39017|

Es importante señalar que el valor de concentración considerado en cada fuente, es el resultado
del promedio de las 3 muestras muestreadas y analizadas el 14 de mayo de 2020. Por otro
lado, el dato de flujo de la fuente de volumen fue calculado a partir de la velocidad medida en
las aberturas.

En las tablas anteriores, se puede observar que las mayores emisiones provienen desde los
lechos de secado con 390 OU E /s, lo que representa el 85% de las emisiones totales generadas
en la PTAS, mientras que el reactor y digestor aeróbico representan el 7% y el 5%
respectivamente. Por otro lado, podemos ver que las menores emisiones se presentan en el
sedimentador y en la cámara de contacto, los que representan un 1% y un 0,4%,
respectivamente.

A continuación, se presenta un gráfico con la distribución porcentual de las fuentes
consideradas en el escenario actual de la PTAS Curepto.

14 Información contenida en el Reporte de muestreo Planta de Tratamiento de Aguas Servidas Quirihue, realizado
por Odotech Chile SpA.
15 Concentración homologada del Reporte de muestreo Planta de Tratamiento de Aguas Servidas Quirihue, realizado
por Odotech Chile SpA.
16 Emisión homologada del Reporte de muestreo Planta de Tratamiento de Aguas Servidas Quirihue, realizado por
Odotech Chile SpA.
17 La concentración determinada para el lecho de secado es menor a 12 OU E /m 3, dado que algunos panelistas
alcanzaron el límite de detección del método. La tasa de emisión es menor a 390 OU E /s.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 23 de 63

**Figura No 9** . Distribución porcentual de las emisiones generadas actualmente en la PTAS

Curepto.

**5.4.2 Emisiones Escenario Futuro.**

Como se mencionó anteriormente, el escenario futuro contempla un aumento de capacidad de
la PTAS Curepto, por lo que se estima que el caudal medio a tratar será de 8,3 l/s. A
continuación, se detallan las consideraciones realizadas a las fuentes, en el escenario futuro:

1. Pretratamiento compacto (basura, arena y grasas).
2. Ampliación del reactor aeróbico, el que ocupará el lugar donde actualmente se

encuentra el digestor/espesador.
3. El sedimentador existente se transformará en digestor aeróbico.
4. Construcción de un nuevo sedimentador, que contempla una cámara de lodos y una

cámara de espumas que se encontrarán cerradas. Dichas unidades no se consideran
en el modelo porque están cerradas.
5. Espesador dinámico; esta unidad no se considera en la modelación porque se encuentra

cerrada.

6. Tornillo de deshidratado, cuya unidad fue homologada a la medición realizada el 29 de

abril de 2020 en la PTAS Retiro, Nuevosur S.A.

7. Construcción de una nueva cámara de contacto.

8. PEAS retorno; dicha unidad no se considera en la modelación porque se encontrará

cerrada.

A continuación, se detallan las consideraciones utilizadas para realizar el cálculo de emisiones:

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 24 de 63

Pretratamiento compacto.

La operación actual de la PTAS Curepto considera una unidad de pretratamiento que incluye la
separación de basura, sin embargo, esta unidad es pequeña y se encontraba cerrada el día en
que se realizó la medición por lo que no se consideró en el escenario actual, ya que las
emisiones que podría emitir a la atmósfera se consideran despreciables; es importante señalar
que a futuro se considera la implementación de un pretratamiento compacto que considera
basura, arena y grasas, cuya emisión fue homologada del estudio Medición de olores en PTAS
Requinoa, [18] el cual considera 0,29 OU E /m [2] /s para pretratamiento.

Tornillo de deshidratado.

Como el tornillo de deshidratado en la PTAS Curepto es una unidad nueva, se estima su
emisión mediante una emisión de referencia de la PTAS Retiro [19], la que equivalente a 87,23
OU E /s. Dado que la cantidad de caudal a tratar entre ambas es diferente se realiza una
proyección de olor para el escenario futuro de la PTAS Curepto, mediante la siguiente ecuación:

EF T = [EA] [T] CMA [∗CMF]

Donde:

EF T : Emisión futura de olor tornillo de deshidratado PTAS Curepto ( OU E /s)
EA T : Emisión actual de olor tornillo de deshidratado PTAS Retiro ( OU E /s)
CMF: Caudal medio anual futuro PTAS Curepto 8,3 l/s
CMA: Caudal medio anual actual PTAS Retiro 10,7 l/s

Por lo anteriormente señalado, se considera que la futura emisión del tornillo de deshidratado
en la PTAS Curepto es de 67,66 OU E /s.

Contenedor de lodos.

La operación futura de la PTAS Curepto considera implementar un contenedor de lodos, cuya
emisión fue homologada del estudio Medición de olores en PTAS Requinoa, [20] el cual considera
una tasa de emisión de 0,96 OU E /m [2] /s para el contenedor de lodos.

Fuentes de área difusa pasiva

Las fuentes de área pasiva como el reactor aeróbico, digestor aeróbico, el sedimentador y la
cámara de contacto consideran la reubicación y ampliación de la unidad en algunos casos, por
lo tanto se considera la misma emisión por área (OU E /m [2] /s) en el escenario futuro.

18 Estudio realizado por ANAM en febrero de 2018.
19 La emisión de referencia fue homologada a la medición que se realizó en el deshidratador en la PTAS Retiro el 29
de abril de 2020.
20 Estudio realizado por ANAM en febrero de 2018.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 25 de 63

A continuación, en la siguiente tabla, se presentan las emisiones de olor de las fuentes que
fueron consideradas en el escenario futuro.

**Tabla No 11.** Emisión de olor de las fuentes consideradas en la modelación.

|Fuente|Tipo de fuente|Medición/<br>Homologación|Superficie<br>(m2)|Emisión<br>por área<br>(OU /m2/s)<br>E|Emisión<br>de olor<br>(OU /s)<br>E|
|---|---|---|---|---|---|
|Pretratamiento<br>compacto|Difusa área<br>pasiva|Homologación<br>PTAS Requínoa|3|0,29|1|
|Reactor aeróbico|Difusa área<br>pasiva|Medición|74|0,65|48|
|Sedimentador|Difusa área<br>pasiva|Medición|95|0,11|10|
|Cámara de contacto|Difusa área<br>pasiva|Medición|15|0,37|5|
|Digestor aeróbico|Difusa área<br>pasiva|Medición|39|1,29|50|
|Tornillo deshidratado|De volumen|Homologación<br>PTAS Retiro|8|8,90|68|
|Contenedor de lodos|Difusa área<br>pasiva|Homologación<br>PTAS Requínoa|9|0,96|9|

En la tabla anterior, se puede observar que las principales emisiones provienen de la línea de
lodos, específicamente del tornillo deshidratado con 68 OU E /s y del digestor aeróbico con 50
OU E /s, lo que representa un 35% y un 26%, respectivamente de las emisiones totales de la
PTAS Curepto. Por otro lado, se puede observar que las menores emisiones se registraron en
pretratamiento compacto (1 OU E /s) y cámara de contacto (5 OU E /s).

A continuación, se presenta un gráfico con la distribución porcentual de las fuentes que fueron
consideradas en la modelación del escenario futuro.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 26 de 63

**Figura No 10** . Distribución porcentual de las futuras emisiones de la PTAS Curepto.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 27 de 63

**5.4.3 Dispersión de emisiones**

**5.4.3.1 Escenario Actual** **[21]**

**5.4.3.1.1 Curva de Isoconcentración.**

En la figura a continuación se muestra la dispersión de odorantes desde la Planta de
Tratamiento de Aguas Servidas Curepto. La imagen presenta las máximas concentraciones de
olor en las zonas aledañas a la planta, considerando una excedencia de un 2%, lo que es
comparado con las normas de referencia. El análisis presente indica que durante el 98% de las
horas del año se presentarán concentraciones igual o menor al valor indicado en la cartografía.

**Figura No 11** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio

horario, percentil 98. Escenario actual.

De la figura, se puede observar que las concentraciones fuera de la planta varían entre 0,4 y
3,0 OU E /m [3], con una distribución radial, abarcando un área total de 1,26 ha para la isodora de
1 OU E /m [3] . En la imagen podemos observar que fuera del límite predial no existe superación del
límite de inmisión de 3 OU E /m [3] ; establecido en la normativa colombiana.

21 El escenario actual, considera una emisión constante para todas las fuentes, a excepción del digestor aeróbico
que funciona en forma discontinua como digestor que opera 6 días y como espesador 1 día a la semana, cuya
condición fue ingresada a Calpuff.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 28 de 63

El límite de referencia presentado establece un valor de 3 OU E /m [3] para periodos horarios con
percentil 98, que aplica para la contaminación de olor generada por plantas de tratamiento de
aguas servidas.

El punto de máxima concentración se produce dentro del límite predial, específicamente en el
sector ubicado entre la cámara de contacto y los lechos de secado, alcanzando una
concentración de 5,07 OU E /m [3] .

**Tabla No 12** . Máxima concentración. Escenario actual.

|Ubicación|UTM 18H - WGS84|Col3|Concentración de<br>inmisión<br>(OU /m3)<br>E|
|---|---|---|---|
|**Ubicación**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Predio PTAS Curepto|770.691|6.113.217|5,07|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 29 de 63

**5.4.3.1.2 Área de Influencia**

Con base en la dispersión de emisiones del escenario actual, se determinó un área de influencia
definida según la “Guía para la predicción y evaluación de impactos por olor en el SEIA” [22], como
el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de detección del
olor compuesto, es decir, es la concentración en donde el 50% de la población puede percibir
un olor. Dicho límite cubre una superficie de 1,26 ha, con tendencia radial. Es importante señalar
que dicha zona no circunscribe a ninguno de los receptores considerados en la modelación.

**Figura No 12** . Área de Influencia. Escenario actual.

22 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 30 de 63

**5.4.3.1.3 Receptores evaluados**

A continuación, se presentan los receptores discretos considerados en la modelación:

**Tabla No 13** . Receptores discretos considerados en la modelación.

|No|ID|Descripción|Distancia con<br>respecto a la<br>planta (km)|Coordenadas UTM<br>Datum WGS84 Huso 18S|Col6|Uso de suelo|
|---|---|---|---|---|---|---|
|**No**|**ID**|**Descripción**|**Distancia con**<br>**respecto a la**<br>**planta (km)**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R1|MH42|Vivienda|0,1723|770.854|6.113.138|Zona de área verde|
|R2|MH43|Vivienda|0,1924|770.737|6.113.017|Zona urbana 2|
|R3|MH44|Vivienda|0,1225|770.732|6.113.086|De acuerdo al Plan<br>Regulador Comunal de<br>Curepto, los receptores se<br>emplazan en una<br>zonificación de área<br>urbana, en un uso de<br>suelo ZAP Zona Actividad<br>Productiva|
|R4|MH45|Vivienda|0,1126|770.572|6.113.201|6.113.201|
|R5|MH46|Vivienda|0,1127|770.585|6.113.241|6.113.241|
|R6|MH47|Galpón|0,1328|770.605|6.113.307|6.113.307|
|R7|MH48|Vivienda|0,1929|770.503|6.113.251|6.113.251|

**Figura No 13** . Receptores de interés considerados en la modelación.

23 La fuente más cercana corresponde a los lechos de secado.
24 La fuente más cercana corresponde al digestor aeróbico.
25 La fuente más cercana corresponde al digestor aeróbico.
26 La fuente más cercana corresponde al digestor aeróbico.
27 El receptor se encuentra a la misma distancia de cuatro fuentes: digestor aeróbico, reactor aeróbico, sedimentador
y cámara de contacto.
28 El receptor se encuentra a la misma distancia de cuatro fuentes: lechos de secado, cámara de contacto,
sedimentador y reactor aeróbico.
29 El receptor se encuentra a la misma distancia de cuatro fuentes: digestor aeróbico, reactor aeróbico, sedimentador
y cámara de contacto.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 31 de 63

En la siguiente tabla, se presenta el resultado del Percentil 98, de las concentraciones horarias
para cada receptor discreto considerado en la modelación. Tal como se puede apreciar en la
tabla, la operación actual de la planta produce concentraciones de inmisión que se encuentran
bajo el límite de referencia establecido en la normativa colombiana (3 OU E /m [3] ). La
concentración más alta se observa en el receptor R5 que alcanza 0,48 OU E /m [3], concentración
que se encuentra bajo el límite de inmisión establecido en la normativa de referencia.

**Tabla No 14** . Concentración receptores. Escenario Actual, percentil 98.

|No|ID|Descripción|Concentración<br>de inmisión<br>(OU /m3)<br>E|Límite inmisión<br>(Norma<br>Colombiana)|Horas sobre<br>3 OU /m3<br>E|
|---|---|---|---|---|---|
|R1|MH42|Vivienda|0,18|3 <br>OUE/m3 <br>(percentil 98)|0 (0,00%)|
|R2|MH43|Vivienda|0,15|0,15|0 (0,00%)|
|R3|MH44|Vivienda|0,24|0,24|0 (0,00%)|
|R4|MH45|Vivienda|0,40|0,40|9 (0,10%)|
|R5|MH46|Vivienda|0,48|0,48|13 (0,15%)|
|R6|MH47|Galpón|0,43|0,43|14 (0,16%)|
|R7|MH48|Vivienda|0,29|0,29|2 (0,02%)|

En el Anexo N°2 se presenta el análisis de la variación horaria de olor, en los receptores
discretos que presentaron la mayor concentración de olor.

Por otro lado, debido a la utilización de variables meteorológicas mediante un archivo WRF, en
los Anexos N°3 y N°4 se presentan la descripción meteorológica/geofísica de la zona, y el
análisis de incertidumbre, respectivamente.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 32 de 63

**5.4.3.1.4 Frecuencia Percepción Olor**

**Figura No 14** . Mapa de horas sobre 3 OU E /m3 generado por las fuentes de emisión de la

PTAS Curepto, promedio horario. Escenario actual.

En la figura anterior se pueden observar las horas del año, en que la concentración de olor
superó el límite de referencia, establecido como 3 OU E /m3. La figura indica que en los
alrededores de la planta se observa una superación del límite de referencia entre 40 y 400
horas al año; a pesar de esto, ninguno de los receptores supera el 2% de horas del año, lo que
corresponde a 175 horas.

**5.4.3.1.5 Protocolo FIDOL**

**Tabla No 15** . Protocolo FIDOL, Escenario Actual.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia|La PTAS opera durante todos los días del año. Sin embargo, durante el 98% de las<br>horas del año no se prevé superación de las 3 OUE/m3, lo anterior porque el receptor<br>que presenta la máxima concentración (R5), alcanza las 0,48 OUE/m3.|
|Intensidad|Ningún receptor se encuentra sobre las 3 OUE/m3, en el percentil 98, de la normativa<br>de referencia (concentración que representa el umbral de molestia). Dado que los<br>resultados en los receptores son menores a 3 OUE/m3 y menores que 1 OUE/m3, se|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 33 de 63

|Parámetro|Con respecto a receptores discretos.|
|---|---|
||puede concluir que el olor es casi imperceptible en los 7 receptores considerados en la<br>modelación.|
|Duración|En cuanto a la duración, no ocurren eventos durante el año de superación de 3 OUE/m3 <br>(concentración utilizada como referencia). Dado lo anterior, se podría señalar que las<br>concentraciones no afectan a la población debido a que no superan el umbral de 3<br>OUE/m3 bajo el percentil 98.|
|Ofensividad|Los olores de la planta se consideran desde ligeramente desagradable a desagradable,<br>mientras que la intensidad de percepción puede variar entre muy débil y fuerte.|
|Localización|De acuerdo al plan regulador de la comuna de Curepto, la planta de tratamiento de<br>aguas servidas se emplaza en un uso de suelo de Zona Actividad Productiva (ZAP).|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 34 de 63

**5.4.3.2 Escenario Futuro**

**5.4.3.2.1 Curva de Isoconcentración.**

En la siguiente figura se muestra la dispersión de odorantes del escenario futuro de la Planta
de Tratamiento de Aguas Servidas, Curepto. La figura presenta las máximas concentraciones
de olor en las zonas aledañas a la planta, considerando una excedencia de un 2%, lo que es
comparado con la norma de referencia. El análisis presente indica que durante el 98% de las
horas del año se presentarán concentraciones igual o menor al valor indicado en la cartografía.

**Figura No 15** . Mapa de concentración de olor generado por las fuentes de emisión. Promedio

horario (percentil 98), Escenario futuro.

De la figura, se puede observar que las concentraciones fuera de la planta varían entre 0,4 a
1,0 OU E /m [3], con una distribución radial, abarcando un área total de 0,26 ha para la isodora de
1 OU E /m [3] . En la imagen podemos observar que fuera del límite predial no existe superación del
límite de inmisión de 3 OU E /m [3] ; establecido en la normativa colombiana. El límite de referencia
presentado establece un valor de 3 OU E /m [3] para periodos horarios con percentil 98, que aplica
para la contaminación de olor generada por plantas de tratamiento de aguas servidas.

El punto de máxima concentración se produce al interior de la planta, específicamente al
noroeste del digestor aeróbico, alcanzando el valor de 1,69 OU E /m [3] .

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 35 de 63

**Tabla No 16** . Máxima concentración. Escenario futuro.

|Ubicación|UTM 18H - WGS84|Col3|Concentración de<br>inmisión<br>(OU /m3)<br>E|
|---|---|---|---|
|**Ubicación**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Predio PTAS Curepto|770.691|6.113.217|1,69|

**5.4.3.2.2 Área de Influencia**

Con base en la dispersión de emisiones del escenario evaluado, se determinó un área de
influencia definida según la “Guía para la predicción y evaluación de impactos por olor en el
SEIA” [30], como el espacio contenido por la isodora de 1 OU E /m [3], que corresponde al umbral de
detección del olor compuesto, es decir, es la concentración en donde el 50% de la población
puede percibir un olor. Dicho límite cubre una superficie de 0,26 ha, por lo que no circunscribe
a ningún receptor.

**Figura No 16** . Área de Influencia. Escenario futuro.

30 Publicada el 2017 por el Servicio de Evaluación Ambiental.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 36 de 63

**5.4.3.2.3 Receptores discretos**

A continuación, se presentan los receptores discretos considerados en la modelación:

**Tabla No 17** . Receptores considerados en la modelación.

|No|ID|Descripción|Distancia con<br>respecto a la<br>planta (km)|Coordenadas UTM<br>Datum WGS84 Huso 18S|Col6|Uso de suelo|
|---|---|---|---|---|---|---|
|**No**|**ID**|**Descripción**|**Distancia con**<br>**respecto a la**<br>**planta (km)**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R1|MH42|Vivienda|0,1731|770.854|6.113.138|Zona de área verde|
|R2|MH43|Vivienda|0,1932|770.737|6.113.017|Zona urbana 2|
|R3|MH44|Vivienda|0,1233|770.732|6.113.086|De acuerdo al Plan<br>Regulador Comunal de<br>Curepto, los receptores<br>se emplazan en una<br>zonificación de área<br>urbana, en un uso de<br>suelo ZAP Zona<br>Actividad Productiva|
|R4|MH45|Vivienda|0,1134|770.572|6.113.201|6.113.201|
|R5|MH46|Vivienda|0,1135|770.585|6.113.241|6.113.241|
|R6|MH47|Galpón|0,1336|770.605|6.113.307|6.113.307|
|R7|MH48|Vivienda|0,1937|770.503|6.113.251|6.113.251|

31 La fuente más cercana corresponde a los lechos de secado.
32 La fuente más cercana corresponde al digestor aeróbico.
33 La fuente más cercana corresponde al digestor aeróbico.
34 La fuente más cercana corresponde al digestor aeróbico.
35 El receptor se encuentra a la misma distancia de cuatro fuentes: digestor, reactor biológico, sedimentador y cámara
de contacto.
36 El receptor se encuentra a la misma distancia de cuatro fuentes: lechos de secado, cámara de contacto,
sedimentador y reactor biológico.
37 El receptor se encuentra a la misma distancia de cuatro fuentes: digestor, reactor biológico, sedimentador y cámara
de contacto.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 37 de 63

**Figura No 17** . Receptores de interés considerados en la modelación.

En la siguiente tabla, se presenta el resultado del Percentil 98 de las concentraciones horarias
para cada receptor discreto considerado en la modelación. Tal como se puede apreciar, la
operación futura de la planta produce concentraciones de inmisión que se encuentran bajo el
límite de referencia establecido en la normativa colombiana (3 OU E /m [3] ). La concentración más
alta se observa en el receptor R5 que alcanza 0,25 OU E /m [3], concentración que se encuentra
bajo el límite de inmisión establecido en la normativa de referencia.

**Tabla No 18** . Concentración receptores. Escenario Futuro, Percentil 98.

|No|ID|Descripción|Concentración<br>de inmisión<br>(OU /m3)<br>E|Límite inmisión<br>(Norma<br>Colombiana)|Horas sobre 3<br>OU /m3<br>E|
|---|---|---|---|---|---|
|R1|MH42|Vivienda|0,08|3 <br>OUE/m3 <br>(percentil 98)|0 (0,00%)|
|R2|MH43|Vivienda|0,09|0,09|0 (0,00%)|
|R3|MH44|Vivienda|0,13|0,13|0 (0,00%)|
|R4|MH45|Vivienda|0,22|0,22|0 (0,00%)|
|R5|MH46|Vivienda|0,25|0,25|0 (0,00%)|
|R6|MH47|Galpón|0,22|0,22|0 (0,00%)|
|R7|MH48|Vivienda|0,14|0,14|0 (0,00%)|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 38 de 63

En el Anexo N°2 se presenta el análisis de la variación horaria del olor en los receptores
discretos con mayor concentración considerado en la modelación.

Por otro lado, debido a la utilización de variables meteorológicas mediante un archivo WRF, en
los Anexos N°3 y N°4 se presentan la descripción meteorológica/geofísica de la zona, y el
análisis de incertidumbre, respectivamente.

**5.4.3.2.4 Frecuencia Percepción Olor**

**Figura No 18** . Mapa de horas sobre 3 OU E /m3 generado por las fuentes de emisión de la

PTAS Curepto, promedio horario. Escenario futuro.

En la figura anterior se pueden observar las horas del año, en que la concentración de olor
superó el límite de referencia, establecido como 3 OU E /m3. La figura indica que en los
alrededores de la planta se observa una superación del límite de referencia de 5 a 30 horas al
año; a pesar de o anteriormente señalado, ninguno de los receptores supera el 2% de horas
del año, lo que corresponde a 175 horas.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 39 de 63

**5.4.3.2.5 Protocolo FIDOL**

**Tabla No 19** . Protocolo FIDOL, Escenario Futuro.

|Parámetro|Con respecto a receptores discretos.|
|---|---|
|Frecuencia|La PTAS opera durante todos los días del año. Sin embargo, durante el 98% de las<br>horas del año no se prevé superación de las 3 OUE/m3.|
|Intensidad|Ningún receptor se encuentra sobre las 3 OUE/m3 en el percentil 98, de la normativa de<br>referencia (concentración que representa el umbral de molestia). Dado que los<br>resultados en los receptores son menores a 3 OUE/m3 se puede concluir que en los<br>receptores no se lograría percibir el olor proveniente de la PTAS, lo anterior porque los<br>resultados se encuentran bajo 1 OUE/m3.|
|Duración|En cuanto a la duración, durante el año no ocurrirían efectos de superación de 3 OUE/m3 <br>(concentración utilizada como referencia). Dado lo anterior se podría señalar que las<br>concentraciones no afectarían a la población debido a que no superan el umbral de 3<br>OUE/m3 bajo el percentil 98.|
|Ofensividad|Los olores de la planta se consideran desde ligeramente desagradable a desagradable<br>mientras que la intensidad de percepción puede variar entre muy débil y fuerte.|
|Localización|De acuerdo al plan regulador de la comuna de Curepto, la planta de tratamiento de<br>aguas servidas se emplaza en un uso de suelo de Zona Actividad Productiva (ZAP).|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 40 de 63

**6** **Conclusiones**

En relación a la modelación de dispersión de olores, para el escenario actual, se concluye lo
siguiente:

1. La mayor emisión se presenta en los lechos de secado alcanzando un valor de 390

OU E /s, lo que representa el 85% de las emisiones totales generadas durante el
escenario actual.

2. Las curvas de isoconcentración del percentil 98, indican que las concentraciones de olor

producidas por las fuentes de la PTAS Curepto, varían entre 0,4 y 3,0 OU E /m [3],
concentraciones que se dispersan en forma radial. Dicha dispersión abarca un área total
de 1,26 ha para la isodora de 1 OU E /m [3] . Las mayores concentraciones se presentan al
interior de la planta, específicamente entre la cámara de contacto y el lecho de secado.

3. El área de influencia correspondiente a la curva de 1 OU E /m [3] bajo percentil 98, no

circunscribe a ningún receptor ya que el receptor que presenta la mayor concentración
(R5) alcanza las 0,48 OU E /m [3] . Es importante señalar, que dichos receptores
corresponden a viviendas cercanas a la planta.

4. Finalmente, se puede concluir que ninguno de los receptores considerados en el

escenario actual, supera el límite de inmisión de 3 OU E /m [3], establecido en la normativa
colombiana.

En relación a la modelación de dispersión de olores, para el escenario futuro, se concluye
lo siguiente:

5. La mayor emisión se presenta en el tornillo de deshidratado con 68 OU E /s, lo que

representa un 35%, seguido por el digestor aeróbico con 50 OU E /s, representando un
26% de las emisiones totales de la PTAS Curepto.

6. Las curvas de isoconcentración del percentil 98, indican que las concentraciones de olor

producidas por las fuentes de la PTAS Curepto, varían de 0,4 a 1,0 OU E /m [3], con una
distribución radial. Dicha dispersión abarca un área total de 0,26 ha para la isodora de
1 OU E /m [3] . Las mayores concentraciones se presentan al interior de la planta.

7. El área de influencia correspondiente a la curva de 1 OU E /m [3] bajo percentil 98, abarca

un área de 0,26 ha, sin embargo, no circunscribe a ningún receptor.

8. Ninguno de los receptores, considerados en la modelación del escenario futuro, supera

el límite de inmisión de 3 OU E /m [3] establecido en la normativa colombiana.

9. Al comparar el escenario actual con el futuro, se puede observar una disminución de la

emisión de olor de 458 OU E /s a 191 OU E /s, respectivamente, lo que representa una
disminución de un 58%, lo anterior se debe principalmente al cambio de los lechos de

secado a tornillo de deshidratado.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 41 de 63

**7** **Anexos**

**Anexo No1. Esquema de funcionamiento Calpuff y elementos de modelación**

El presente Anexo contiene el archivo magnético el cual contiene la información que se utilizó
para realizar la modelación atmosférica, dicha información corresponde a la los input y output
ingresados para la modelación de los módulos del modelo (CALPUFF, CALPOST y CALRANK)
y el archivo Meteorológico WRF.

Por lo tanto, en el caso de que se requiera replicar la modelación realizada, esta se podrá hacer
utilizando los archivos presentes en este Anexo.

- **NOTA. Los antecedentes serán entregados al titular en formato digital, debido al tamaño**

**de los archivos.**

**Figura No 19** . Esquema funcionamiento CALPUFF.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 42 de 63

**Anexo No2. Análisis de receptores.**

A continuación, se presentan los gráficos ciclo diario de las concentraciones de olor, para los
receptores que presentaron mayores concentraciones en los escenarios actual y futuro. Estos
gráficos permiten detectar las horas en donde ocurren las mayores concentraciones durante el
día, respecto al 90% observado del tiempo (variación entre el percentil 5 y percentil 95).

**Escenario Actual**

Receptor 4

**Figura No 20** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No4.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Se puede observar que los mayores valores se presentan durante la noche y madrugada,
entre las 00:00 y 06:00 hrs. con valores de hasta 0,60 OU E /m3. Los resultados anteriores indican
que, durante el 90% del tiempo, en los alrededores, al oeste de la planta, el olor no se alcanza
a percibir por la población.

Receptor 5

**Figura No 21** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No5.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 43 de 63

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Se puede observar que los mayores valores se presentan durante la noche y mañana,
entre las 22:00 y 9:00 hrs. con valores de hasta 0,8 OU E /m3. Los resultados anteriores indican
que, durante el 90% del tiempo, en los alrededores, al noroeste de la planta, el olor no se
alcanza a percibir por la población.

Receptor 6

**Figura No 22** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No6.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Se puede observar que los mayores valores se presentan durante el día, entre las 00:00 y
08:00 hrs. con valores de hasta 0,80 OU E /m3 a las 04:00 hrs. Los resultados anteriores indican
que, durante el 90% del tiempo, en los alrededores, al norte de la planta, el olor no se alcanza
a percibir por la población.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 44 de 63

**Escenario Futuro**

Receptor 4

**Figura No 23** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No4.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Se puede observar que los mayores valores se presentan durante el día, entre las 22:00 y
7:00 hrs. con valores de hasta 0,23 OU E /m3. Los resultados anteriores indican que, durante el
90% del tiempo, en los alrededores, al oeste de la planta, el olor no se alcanza a percibir por la
población.

Receptor 5

**Figura No 24** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No5.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Se puede observar que los mayores valores se presentan durante la noche, entre las 03:00
y 06:00 hrs. con valores de hasta 0,50 OU E /m3. Los resultados anteriores indican que, durante
el 90% del tiempo, en los alrededores, al noroeste de la planta, el olor no se alcanza a percibir
por la población.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 45 de 63

Receptor 6

**Figura No 25** . Concentraciones horarias (OU E /m [3] ), Distribución horaria. Receptor No6.

En la figura anterior se muestra, el comportamiento de las concentraciones de olor durante el
día. Se puede observar que los mayores valores se presentan entre las 04:00 y 07:00 hrs. con
valores de hasta 0,30 OU E /m3. Los resultados anteriores indican que, durante el 90% del tiempo,
en los alrededores, al norte de la planta, el olor no se alcanza a percibir por la población.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 46 de 63

**Anexo No3. Descripción meteorológica y geofísica de la zona.**

En el siguiente anexo se presenta el análisis meteorológico de la zona modelada. Estos datos
fueron extraídos desde la estación Lien contenida en el sistema Agromet INIA.

**Tabla No 20** . Estaciones meteorológicas.

|Nombre de la Estación|Col2|Lien|
|---|---|---|
|Coordenada UTM 19H,<br>Datum WGS 84|Este (m)|229.287 m E|
|Coordenada UTM 19H,<br>Datum WGS 84|Norte (m)|6.111.925 m S|
|Distancia desde el proyecto|Distancia desde el proyecto|5,71 km|
|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|"Periodo del registro<br>(desde DD/MM/AA - hasta DD/MM/AA)"|01/01/2019 - 31/12/2019|
|Meteorología|Meteorología|Velocidad Viento (VV)<br>Dirección Viento (DV)<br>Temperatura (T)|

7.3.1 Cantidad de Datos

Para realizar el análisis meteorológico y de incertidumbre es necesario verificar la cantidad de
registros presentes en las mediciones meteorológicas de la estación Lien. A continuación, se
muestran los datos de la estación, con la finalidad de comprobar que no existen periodos
extensos sin información, durante el año en estudio.

**Figura No 26** . Serie de tiempo anual. Velocidad de viento. Estación Lien.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 47 de 63

**Figura No 27** . Serie de tiempo anual. Dirección de viento. Estación Lien.

**Figura No 28** . Serie de tiempo anual. Temperatura. Estación Lien.

A partir de las gráficas de serie de tiempo, de los parámetros temperatura, velocidad y dirección
del viento, se evidencia que existe un registro completo de los datos meteorológicos

mencionados.

**Tabla No 21.** Datos válidos estación meteorológica Lien.

|Porcentaje de datos meteorológicos disponibles - EM Lien.|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Parám**<br>**/mes**|**E **|**F **|**M **|**A **|**M **|**J **|**J **|**A **|**S **|**O **|**N **|**D **|**Total**|
|**VV**|95%|89%|97%|98%|**62%**|**62%**|75%|96%|96%|97%|97%|94%|88%|
|**DV**|95%|89%|97%|98%|**62%**|**62%**|75%|96%|96%|97%|97%|94%|88%|
|**T **|95%|89%|97%|98%|**62%**|**62%**|75%|96%|96%|97%|97%|94%|88%|

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 48 de 63

De acuerdo a la tabla anterior, se puede observar que en el mes de mayo y junio, la cantidad
de datos alcanza un 62%; a pesar de esto, la cantidad de registros en forma anual es de un
88% para cada una de las variables analizadas, valor que esta sobre el límite de 75% indicado
por la Guía para modelos de calidad del aire del SEA. Por lo tanto, esta estación se puede
considerar en el análisis.

7.3.2 Gráficos Ciclo diario

En los siguientes gráficos se presentan los ciclos diarios promedios de velocidad y dirección
del viento; junto con su variabilidad entre el percentil 5% a 95%.

**Figura No 29** . Ciclo diario para velocidad de viento. Estación Lien.

En relación al ciclo diario promedio de la velocidad de viento alcanza una velocidad promedio
de 2,1 m/s en las horas de la tarde y de 0,2 m/s en las horas de la madrugada. Durante el año,
la velocidad del viento puede variar entre calmas y 3,9 m/s en el rango del 90% observado. Lo
anterior indica un escenario favorable para la dispersión de emisiones de olor.

**Figura No 30** . Ciclo diario para dirección de viento. Estación Lien.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 49 de 63

En relación al ciclo diario promedio de la dirección de viento se observa que durante el día y la
noche predominan los vientos provenientes desde el norte alcanzando un 60% y 48%,
respectivamente. Es importante señalar que, adicionalmente durante la noche, en menor
proporción se presentan vientos provenientes desde el sur lo que corresponde a un 24%. En
general los vientos, registrados indicarían que las emisiones de olor se desplazarían
principalmente hacia el sureste, sur y norte.

**Figura No 31** . Ciclo diario de temperatura. Estación Lien.

Respecto al ciclo diario de temperatura, se observa una temperatura promedio que alcanza los
19°C entre las 15:00 y las 17:00 hrs, mientras que la mínima alcanza los 7°C entre las 02:00 y
las 07:00 hrs. Durante el año, la temperatura puede variar entre ± 10°C respecto al promedio,
alcanzando máximos de 31°C y mínimas de 0°C, respecto al 90% observado.

7.3.3 Gráficos Distribución de Vientos

Las siguientes figuras muestran la distribución de vientos en la zona de emplazamiento
del proyecto. De la figura se puede concluir, el 38,4% del tiempo se observan periodos
de calmas, mientras que el 32% del tiempo se observan velocidades que ocurren en el
rango de 0,5 a 2,1 m/s, el 16,3% del viento alcanza velocidades que van desde los 2,1
a 3,6 m/s y finalmente un 1,4% del viento alcanza velocidades que van entre los 3,6 y
los 5,7 m/s. A partir de lo anteriormente señalado, se puede concluir que las condiciones
meteorológicas en la zona no favorecen la dispersión de las emisiones atmosféricas.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 50 de 63

**Figura No 32** . Distribución velocidades de viento en la zona del proyecto. Estación Lien.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 51 de 63

7.3.4 Rosa de los Vientos

**Figura No 33** . Rosa de los vientos anual. Estación Lien.

En la rosa de los vientos se puede observar que existe una predominancia de los vientos
provenientes desde el noroeste con un 20% de frecuencia aproximadamente. Estas direcciones
corresponden a los vientos de estabilidad atmosférica que se mantienen durante todo el año.
Con menos frecuencia, en un 5%, se presentan los vientos desde el sureste los cuales
corresponden a los periodos de inestabilidad atmosférica en las estaciones de otoño e invierno.
De lo anterior se concluye que la dispersión de emisiones ocurrirá en distintas direcciones,
principalmente hacia el sureste y en menor proporción al noroeste.

En las siguientes figuras se puede observar la distribución estacional de los vientos en la zona
del proyecto.

(a) Otoño [38]

(b) Invierno

38 Se observa una menor frecuencia de los vientos, dada la ausencia de datos de velocidad entre los meses de mayo
a junio.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 52 de 63

(c) Primavera (d) Verano

**Figura No 34** . Rosa de los vientos por estación Lien, año 2019.

De las imágenes se puede concluir:

 - En otoño e invierno los vientos provienen principalmente desde noroeste y en menor
proporción desde el sureste. Estas condiciones se deben a los periodos de inestabilidad
atmosférica de dichas estaciones del año. Por otro lado, se observan velocidades que
van desde los 0,5 a 3,6 m/s. La dispersión de emisiones se desplaza principalmente
hacia el sureste y en menor proporción hacia el noroeste.

 En primavera y verano los vientos provienen desde el noroeste y en menor proporción
desde el sur. Estas condiciones se deben a los periodos de estabilidad atmosférica. Las
velocidades preponderantes van desde los 0,5 a 5,7 m/s. La dispersión de emisiones
se desplaza hacia el sureste en mayor proporción.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 53 de 63

7.3.5 Ciclo estacional

**Figura No 35** . Gráfico ciclo estacional, Estación Lien.

De acuerdo a la distribución de los vientos en la gráfica de ciclo estacional, se observa que
durante el año predominan velocidades que van entre 1,5 y 3,5 m/s durante el día,
descendiendo en las horas de la noche a 1,0 m/s e incluso se observan periodos de calma.

En la estación de otoño las velocidades de viento varían de periodos de baja velocidad de viento
aumentando en las horas del día a 2,5 m/s. Es importante señalar que las menores velocidades,
durante el día, ocurren durante el otoño, situación que es similar en invierno. Mientras que en
primavera y verano las velocidades del viento, durante el día, pueden alcanzar los 3,5 m/s,
siendo las velocidades más altas del año. El escenario anterior favorece la dispersión de las
emisiones, pero a la vez aumenta el alcance de éstas.

En relación a la dirección del viento, en las épocas de verano los vientos provienen
principalmente desde el noroeste en las horas del día, y con dirección norte en horas de la
noche. En el periodo de invierno, los vientos se mantienen principalmente desde el norte y
noreste por los periodos de inestabilidad atmosférica causados por la estación. De acuerdo a
las condiciones de los vientos se prevé que las emisiones se dispersen en primavera y verano
principalmente hacia el sureste, mientras que en otoño e invierno se desplacen principalmente
hacia el sur o suroeste.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 54 de 63

7.3.6 Elevación de Terreno

**Figura No 36** . Elevación de terreno archivo WRF.

La zona modelada está ubicada en la comuna de Curepto y se caracteriza por una elevación
de terreno aproximada de 10 a 20 m.s.n.m. Este sector pertenece a la cordillera de la costa, en
dondese puede observar variaciones de altura entre 10 a 500 m.s.n.m.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 55 de 63

**Anexo No4. Análisis de incertidumbre.**

La “Guía para el Uso de Modelos de Calidad de Aire en el SEIA en su capítulo 7” requiere que
se realice una comparación de los registros WRF con información meteorológica local. Para
evaluar el desempeño del archivo de pronóstico WRF, se utilizan los datos provenientes de la
estación meteorológica Lien, cuyos datos se encuentran en el sistema Agromet. Los parámetros
monitoreados por dicha estación corresponden a temperatura, velocidad y dirección del viento.
Para la evaluación del desempeño se realiza una comparación de dichas variables ya que estás
son de interés para el análisis dispersión de contaminantes atmosféricos.

Con el fin de evaluar el desempeño del archivo WRF, se realizan dos tipos de análisis,
cualitativo y cuantitativo. Para el análisis cualitativo se realiza una comparación entre los
gráficos de ciclos diarios, promedios mensuales, ciclos estacionales y rosa de los vientos.
Mientras que el análisis cuantitativo se realiza de acuerdo a análisis estadísticos de RMSE y
BIAS.

**Definiciones**

**Datos observados:** Se refiere a los datos provenientes desde una estación de monitoreo
durante un periodo de interés.

**Datos modelados:** Se refiere a los datos meteorológicos provenientes desde un modelo de
pronóstico como WRF o MM5.

**Rango 90% observado:** Se refiere a la variación de los datos entre el percentil 5 y percentil 95
en una hora o mes específico.

7.4.1 Ciclos diarios promedios

Velocidad de viento

**Figura No 37** . Comparación ciclo diario de velocidad del viento entre datos observados y

modelados para la estación Lien.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 56 de 63

De la figura anterior, se puede concluir que el ciclo diario promedio de velocidad del viento,
entre los datos observados y los datos modelados, presentan valores similares con una
diferencia de ± 2 m/s. Además, la variación diaria de velocidad posee el mismo patrón del
modelo de pronóstico y el observado, sin embargo, en el modelo WRF se presentan
velocidades de viento levemente sobreestimadas en comparación a los datos de la estación
meteorológica Lien. A pesar de lo anterior, respecto al ciclo diario promedio de velocidad, el
modelo es adecuado.

Dirección de viento

**Figura No 38** . Comparación ciclo diario de dirección de viento entre datos observados y

modelados para la estación Lien.

De la figura anterior, se puede concluir que el ciclo diario de dirección de viento, entre los datos
observados y los modelados, presentan una tendencia similar con diferencias de 43,8° en
promedio. Cabe destacar que durante el día los registros del modelo de pronóstico presentan
una subestimación de los datos en comparación a los datos observados correspondiente
principalmente a vientos del norte; mientras que esta situación se invierte durante la noche, lo
anterior porque se observa una sobreestimación de los datos, correspondientes a vientos
provenientes del sur. Para el caso de la zona representada por la estación Lien, el modelo es
adecuado.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 57 de 63

**Figura No 39** . Comparación ciclo diario de temperatura entre los datos observados y

modelados para la estación Lien.

De la figura anterior, se puede concluir que el ciclo diario de temperatura, entre los datos
observados y los modelados, presentan valores similares con diferencias máximas de ±1°C. Se
puede observar que durante la noche y parte de la mañana los valores modelados son
levemente sobreestimados en comparación a los datos observados mientras que esta situación
cambia entre las 11:00 y las 20:00 hrs, donde los datos modelados presentan una
subestimación de la realidad. Para el caso de la zona representada por la estación Lien, el
modelo es adecuado.

7.4.2 Promedio Mensual

Velocidad de viento

**Figura No 40** . Comparación ciclo mensual de velocidad de viento entre los datos observados

y modelados para la estación Lien.

De la figura anterior, se puede concluir que el promedio mensual de velocidad del viento, entre
los datos observados y los modelados, presentan valores similares con una diferencia de ±1,5
m/s. Como se puede observar los datos modelados presentan una sobreestimación de la
velocidad del viento en comparación a los datos observados, sin embargo, la variación mensual

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 58 de 63

de velocidad posee el mismo patrón del modelo de pronóstico y el observado. La diferencia de
velocidades se debe a la diferencia de altura sobre el suelo de las estaciones del portal
AGROMET, usualmente a 2 metros de altura, mientras que el archivo meteorológico WRF
establece una capa de 10 metros.

Dirección de viento

**Figura No 41** . Comparación ciclo mensual de dirección de viento entre datos observados y

modelados para la estación Lien.

De la figura anterior, se puede observar que la moda mensual de dirección del viento, entre los
datos observados y los modelados, para la estación Lien los vientos provenientes del norte se
encuentran subestimados en los datos del modelo de pronóstico, los que pueden alcanzar los
77,5° en promedio. Mientras que en el mes de agosto se aprecia una sobreestimación de los
vientos provenientes del sur.

**Figura No 42** . Comparación ciclo mensual de temperatura entre datos observados y

modelados para la estación Lien.

De la figura anterior, se puede concluir que la moda mensual de temperatura, entre los datos
observados y los modelados, para la estación Lien presenta valores similares con diferencias

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 59 de 63

que pueden alcanzar 1°C, entre febrero y septiembre, observándose una leve sobreestimación
de los datos contenidos en el modelo de pronóstico. Sin embargo, la variación mensual de
temperatura posee el mismo patrón del modelo de pronóstico y el observado.

7.4.3 Rosas de los vientos

De las rosas de los vientos mostradas, se puede observar que en la estación meteorológica
Lien predominan los vientos principalmente provenientes desde el noroeste y oeste. En forma
secundaria desde el sureste para los datos observados, mientras que para los datos modelados
predominan los vientos provenientes desde el sur. Respecto a las velocidades se observa la
presencia de vientos de 0,5 a 5,7 m/s en los datos observados mientras que en los modelados
se alcanza una velocidad de 8,8 m/s. Se observa que el modelo de pronóstico WRF sobreestima
vientos sur.

(a) EM - 2019 (b) WRF - 2019

**Figura No 43.** Rosa de los vientos Estación Lien.

7.4.4 Gráficos Ciclos estacionales

En las figuras siguientes se muestran las variaciones de la velocidad y dirección del viento, en
forma diaria y estacional. De los gráficos se puede concluir que el modelo de pronóstico WRF
presenta valores similares a los observados, dado el mismo patrón de velocidades en forma
horaria y mensual.

En referencia al patrón de las velocidades de viento, se observa que ambos modelos presentan
las mayores velocidades entre las 12 a 20 horas, siendo el periodo del día con vientos de más
velocidad. Respecto a la variación mensual se observa que en el periodo de verano se
presencian las mayores velocidades que están entre el rango de los 2,5 a los 3,5 m/s en los
datos observados mientras que en los datos modelados la velocidad del viento va de los 3,5 a
5 m/s. Se observa una sobreestimación de ±2 m/s.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 60 de 63

Respecto a la dirección del viento a lo largo del año se observan direcciones similares,
provenientes principalmente desde el sur y norte en las horas de la mañana, desde el noroeste
en la tarde; esto para las épocas de otoño, primavera y verano tanto en los datos de pronóstico
como los datos observados. En los meses de invierno los vientos presentan una dirección norte
tanto en los datos observados como modelados.

La diferencia entre los datos observados y modelados en la estación Lien se deben
principalmente a las velocidades de viento en donde el archivo WRF sobrestima los vientos
provenientes del sur en ± 2,5 m/s.

**Figura No 44** . Variación estacional de velocidad y dirección de viento EM Lien.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 61 de 63

**Figura No 45** . Variación estacional de velocidad y dirección de viento WRF Lien.

7.4.5 Análisis Cuantitativo

El análisis de los registros de dirección y velocidad de viento se realizó comparando el ciclo
diario, ciclos estacionales, gráficos de distribución y rosa de los vientos. Además, se realizó un
análisis numérico de los promedios diarios de acuerdo a las recomendaciones de la guía EPA
para el uso de modelos numéricos del tiempo en Calpuff [39], cuyos resultados se presentan en
la tabla a continuación. De los valores recomendados, el modelo WRF cumple con la mayoría,
exceptuando a algunos muy cercanos a la recomendación.

**Tabla No 22.** Análisis estadístico Estación Lien.

|Parámetro|Variable Estadística|Horario|Diario|
|---|---|---|---|
|Velocidad|RMSE|2,19|1,82|
|Velocidad|BIAS|1,65|1,65|
|Dirección|BIAS|-0,56|-12,99|
|Temperatura|BIAS|1,45|1,46|

39 PRELIMINARY Draft Users Manual, The MMIFstat Statistical Analysis Package. Sección 2.2.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 62 de 63

Conclusión

De acuerdo a las comparaciones realizadas en forma cualitativa (de ciclo diario, promedio
mensual rosa de los vientos y ciclos estacionales), y cuantitativa para los parámetros
temperatura, velocidad y dirección de viento para la estación Lien se puede indicar que el
modelo WRF sobreestima los vientos provenientes del sur. Sin embargo, los datos observados
presentan valores y patrones similares, que permiten indicar que los datos WRF se ajustan a la
realidad y pueden ser utilizados en la modelación.

Inf02E05.O-20-010. Informe PTAS Curepto (Modelación).cfa 63 de 63