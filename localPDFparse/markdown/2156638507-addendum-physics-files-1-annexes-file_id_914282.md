---
title: Sin título
author: Jasmine
date: D:20221028152753-03'00'
language: es
type: report
pages: 45
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - E S T U D I O D E D I S P E R S I Ó N D E C O N T A M I N A N T E S A T M O S F É R I C O S
-->

# E S T U D I O D E D I S P E R S I Ó N D E C O N T A M I N A N T E S A T M O S F É R I C O S

## DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO LOTEO PINTOR PEDRO LUNA, SAN PEDRO DE LA PAZ

INFORME TÉCNICO ELABORADO PARA:

.

315-IEP-22

Estudio de Dispersión de Contaminantes Atmosféricos

Proyecto Loteo Pintor Pedro Luna

Comuna de San Pedro de la Paz, Provincia de Concepción, Región del Biobio.

**© SICAM Ingeniería**

Estudios Técnicos en Medio Ambiente

Casa matriz: Prieto Sur 965, Temuco. Chile.

Teléfono (045) 2 668119

[Página web: www.sicam,cl](http://www.sicam,cl/)

[Contacto: cvarela@sicam.cl](mailto:cvarela@sicam.cl)

Temuco, Septiembre 2022

**Equipo Técnico**

**MSc. Cristian Varela Bruce**

Ingeniero Ambiental
Jefe Modelación

Elaboración de informe.

**Ing. Carmen Aravena**
Ingeniero Civil Ambiental
Análisis meteorológico.

**Ing. Jasmine Bastidas Muñoz**
Ingeniero Ambiental
Análisis de calidad del aire.

Elaboración de informe.

|Versión|Fecha|Elaborado por|Revisado por|Aprobado por|
|---|---|---|---|---|
|V.1|27-07-2022|Jasmine Bastidas M.|Cristian Varela B.|Cristian Varela B.|
|V.2|26-10-2022|Cristian Varela B|||

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 2

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**ÍNDICE**

1 ANTECEDENTES GENERALES DEL ESTUDIO ........................................................................................................ 6

1.1 Identificación de la empresa consultora .......................................................................................................... 6

1.2 Objetivos de la consultoría.................................................................................................................................... 6

2 DESCRIPCIÓN GENERAL DEL PROYECTO ............................................................................................................. 7

3 MARCO NORMATIVO................................................................................................................................................... 8

4 METODOLOGÍA DE MODELACIÓN ......................................................................................................................... 9

4.1 Modelo Meteorológico ........................................................................................................................................ 10

4.2 Características del Dominio de Modelación y su Entorno ..................................................................... 10

4.2.1 Dominio de Modelación ................................................................................................................................ 11

4.2.2 Topografía y Uso de Suelo ............................................................................................................................ 12

5 CARACTERIZACIÓN METEOROLÓGICA .............................................................................................................. 13

5.1 Información Meteorológica ............................................................................................................................... 13

5.2 Rosas de Los Vientos ............................................................................................................................................ 13

5.2.1 Series de Tiempo ............................................................................................................................................... 15

5.2.2 Ciclos Estacionales ............................................................................................................................................ 16

5.2.3 Ciclos estacionales de datos en altura ...................................................................................................... 18

6 CARACTERIZACIÓN DE CALIDAD DEL AIRE ...................................................................................................... 20

7 CARACTERIZACIÓN DE LA FUENTE Y SUS EMISIONES ................................................................................ 24

7.1 Identificación de las fuentes emisoras ........................................................................................................... 24

7.2 Perfil Temporal ........................................................................................................................................................ 24

8 RESULTADOS DE LA MODELACIÓN .................................................................................................................... 26

8.1 Validación Meteorológica ................................................................................................................................... 26

8.2 Resultados de la Modelación Meteorológica ............................................................................................. 27

8.3 Resultados de la Modelación de Dispersión de Contaminantes ........................................................ 32

8.3.1 Determinación de concentración en el punto de Máximo Impacto Etapa Construcción y

Operación. ................................................................................................................................................................................ 32

8.3.2 Mapas de Isoconcentraciones Construcción ......................................................................................... 32

8.3.3 Mapas de Isoconcentraciones Operación ............................................................................................... 36

8.3.4 Determinación de receptores y concentración de inmisión ............................................................ 41

9 CONCLUSIONES .......................................................................................................................................................... 44

10 REFERENCIAS ........................................................................................................................................................... 45

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 3

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**ÍNDICE DE FIGURAS**

Figura 1. Emplazamiento del proyecto. ............................................................................... 7
Figura 2. Protocolo de Modelación ..................................................................................... 9
Figura 3. Esquema general de funcionamiento de WRF-ARW ........................................... 10
Figura 4. Dominio de modelación WRF/CALPUFF ............................................................. 11
Figura 5. Topografía del área de modelación 3D .............................................................. 12
Figura 6. Rosas de los vientos estacionales (A: verano, B: otoño, C: Invierno, D: Primavera) 14
Figura 7. Series de tiempo horaria de variables meteorológicas año 2021 ........................ 16
Figura 8. Variación estacional del ciclo diario de la velocidad del viento ........................... 16
Figura 9. Variación estacional del ciclo diario de la Temperatura ...................................... 17
Figura 10. Variación estacional del ciclo diario de la Humedad Relativa ............................ 17
Figura 11. Variación estacional del perfil vertical de temperatura ..................................... 18
Figura 12. Variación estacional del perfil vertical de velocidad de viento .......................... 19
Figura 13. Evaluación de Norma diaria para MP10 ............................................................ 21
Figura 14. Evaluación de Norma Anual para MP10 ........................................................... 21
Figura 15. Evaluación de Norma diaria para MP2,5 ........................................................... 23
Figura 16. Evaluación de Norma anual para MP2,5 ........................................................... 23
Figura 17. Perfil temporal emisiones calefacción ............................................................... 25
Figura 18. velocidad del viento modelada v/s modelada serie anual ................................. 26
Figura 19. Correlación Velocidad del viento observada v/s modelada serie anual ............. 26
Figura 20. Campos de viento estación: Verano-periodo nocturno ..................................... 27
Figura 21. Campos de viento estación: Verano-periodo diurno ........................................ 28
Figura 22. Campos de viento estación: Otoño-periodo nocturno ...................................... 28
Figura 23. Campos de viento estación: Otoño-periodo diurno .......................................... 29
Figura 24. Campos de viento estación: Invierno-periodo nocturno ................................... 29
Figura 25. Campos de viento estación: Invierno-periodo diurno ....................................... 30
Figura 26. Campos de viento estación: Primavera-periodo nocturno ................................ 30
Figura 27. Campos de viento estación: Primavera-periodo diurno .................................... 31
Figura 28. Modelación de Dispersión de MP10 P98 promedio 24 hrs. Fase Construcción. . 33
Figura 29. Modelación de Dispersión de MP2.5 P98 promedio 24 hrs. Fase Construcción. 33
Figura 30. Modelación de Dispersión de CO promedio 1 hora Fase Construcción. ............ 34
Figura 31. Modelación de Dispersión de SO 2 P99 promedio 24 hora Fase Construcción ... 34
Figura 32. Modelación de Dispersión de NOx máximo horario Fase Construcción. ........... 35
Figura 32.Modelación de Dispersión de MP10 P98 promedio 24 hrs Fase Operación. ....... 36
Figura 33. Modelación de Dispersión de MP2.5 P98 promedio 24 hrs Fase de Operación. 37
Figura 34. Modelación de Dispersión de SO 2 P99 promedio 24 hora Fase de Operación .. 38
Figura 35. Modelación de Dispersión de NOx máximo horario Fase Operación. ................ 39
Figura 36. Modelación de Dispersión de CO promedio 1 hora Fase de Operación. ........... 40
Figura 38. Receptores evaluados en el proyecto ............................................................... 41

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 4

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**ÍNDICE DE TABLAS**

Tabla 1. Norma de calidad del aire para Material Particulado. .............................................................................. 8
Tabla 2. Coordenadas vértices del área de modelación del proyecto (Huso 18 - WGS84) ..................... 11
Tabla 3. Estaciones meteorológicas y calidad del aire para datos en superficie cercanas al proyecto

...................................................................................................................................................................................................... 13

Tabla 4. Ubicación Estación de Radiosondeo para datos de altura .................................................................. 13

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La información meteorológica utilizada proviene de estaciones de superficie cercanas al área del proyecto y en altura de una estación de radio sondeo. A continuación, en la Tabla 3 y -->

**Tabla 4: se detallan las fuentes de información y sus características, para datos de calidad del**

| Nombre<br>Estación | Coordenadas UTM (18 H) | Col3 | Calidad del Aire | Col5 | Variables<br>meteorológicas | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nombre<br>Estación | UTM-E | UTM-S | MP2.5 | MP10 | HR | TA | DV | VV | RG |
| Bocatoma | 667680 | 5925321 | X | X | - | - | - | - | - |
| Masisa | 665704 | 5918379 | - | - | X | X | X | X | X |

<!-- Estadísticas: 3 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- HR: humedad relativa; TA: Temperatura ambiente; P: Presión atmosférica; DV: dirección del viento; VV: velocidad del viento, PP: precipitaciones; RG: Radiación global -->
<!-- FIN TABLA 4 -->

Tabla 5. Parámetros de cumplimiento de norma de MP10 años 2019-2021 ................................................ 20
Tabla 6. Parámetros de cumplimiento de norma de MP2,5 años 2019-2021 ............................................... 22
Tabla 7. Fuentes de emisiones atmosféricas, durante etapa de construcción del Proyecto. .................. 24
Tabla 8. Días de funcionamiento de la fuente ........................................................................................................... 25

Tabla 9. Resultados de la modelación de calidad del aire (máximo impacto). ............................................. 32
Tabla 10. Identificación de los receptores discretos ............................................................................................... 41
Tabla 11. Resultados de la modelación de calidad del aire (MP10) Construcción ...................................... 42
Tabla 12. Resultados de la modelación de calidad del aire (MP2.5) Construcción ..................................... 42
Tabla 13. Resultados de la modelación de calidad del aire (MP10) operación ............................................ 42
Tabla 14. Resultados de la modelación de calidad del aire (MP2.5) operación ........................................... 43

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 5

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**1** **ANTECEDENTES GENERALES DEL ESTUDIO**

**1.1** **Identificación de la empresa consultora**

|Nombre|: SICAM INGENIERÍA|
|---|---|
|RUT|: 76.244.668-5|
|Dirección|: PRIETO SUR 965|
|Comuna|: TEMUCO|
|Región|: ARAUCANÍA|
|Email|: servicios@sicam.cl|
|Teléfono|: 61575998|
|WEB|: www.sicam.cl|

**1.2** **Objetivos de la consultoría**

Determinar, mediante modelación WRF/CALPUFF, la dispersión de los contaminantes

atmosféricos generados por las actividades asociadas a la etapa de construcción y operación

del proyecto Loteo Pintor Pedro Luna, en el marco de la declaración de impacto ambiental.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 6

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**2** **DESCRIPCIÓN GENERAL DEL PROYECTO**

El proyecto “Loteo Pintor Pedro Luna” se encuentra emplazado en el sector sur poniente de

la comuna de San Pedro de la Paz, Provincia de Concepción, Región del Bio-Bio. En una

superficie total Neta de 7.2 Ha. Entre las calles Avenida 4 norte con Avenida Costanera.

El proyecto consiste en la construcción y habilitación de 334 viviendas., se presenta a

continuación en la figura 1.

Figura 1. Emplazamiento del proyecto.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 7

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**3** **MARCO NORMATIVO**

Según la ley de bases del medio ambiente, las normas de calidad primaria son instrumentos

de gestión ambiental que establecen los límites para proteger la salud de las personas. En

la Tabla 1 se puede verificar los valores establecidos en las normas chilenas de

contaminantes criterio y sus formas de verificación. En el presente informe, las

concentraciones modeladas se compararon con los valores entregados por la normativa, en

relación a los contaminantes aplicables al proyecto.

Tabla 1. Norma de calidad del aire para Material Particulado.

|Contaminante|Valor|Periodo de<br>Evaluación|Forma de Verificación|Fuente<br>Normativa|
|---|---|---|---|---|
|~~Material~~<br>particulado<br>respirable<br>(MP10)|~~130 μg~~<br>/m3N|~~Promedio aritmético~~<br>de 24 hrs.|~~Percentil 98 de valores de un~~<br>año o más de 7 días en un año.|~~D.S. N° 12/2022~~<br>del MMA que<br>deroga<br>D.S.<br>N°59/98<br>MINSEGPRES|
|~~Material~~<br>particulado<br>respirable<br>(MP10)|50 μg /m3N|Promedio aritmético<br>anual|Promedio aritmético de 3 años<br>consecutivos.|Promedio aritmético de 3 años<br>consecutivos.|
|Material<br>particulado fino<br>(MP2.5)|50 μg /m3|Promedio aritmético<br>de 24 hrs.|Percentil 98 de valores de 1<br>año.|D.S. N° 12/2011<br>del<br>Ministerio<br>del<br>medio<br>Ambiente|
|Material<br>particulado fino<br>(MP2.5)|20 μg /m3|Promedio aritmético<br>anual.|Promedio aritmético de 3 años<br>consecutivos.|Promedio aritmético de 3 años<br>consecutivos.|
|Dióxido de<br>azufre (SO2)|80 μg /m3N|Media aritmética<br>anual|Promedio de tres años del<br>percentil 99 de las<br>concentraciones de 24 horas.|D.S.<br>No113/2002<br>del<br>MINSEGPRES|
|Dióxido de<br>azufre (SO2)|250 μg<br>/m3N|Media aritmética<br>diaria|Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|
|Monóxido de<br>Carbono<br>(CO)|30 mg/<br>m3N|Media aritmética<br>horaria|Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora.|D.S.<br>No115/2002<br>del<br>MINSEGPRES|
|Monóxido de<br>Carbono<br>(CO)|10 mg/<br>m3N|Promedio móvil de 8<br>hrs.|Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas.|
|Dióxido de<br>nitrógeno (NO2)|100 μg<br>/m3N|Media aritmética<br>anual|Promedio aritmético de 3 años<br>consecutivos.|D.S.<br>No114/2002<br>del<br>MINSEGPRES|
|Dióxido de<br>nitrógeno (NO2)|400 μg<br>/m3N|Concentración de 1<br>hora|Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora|Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora|

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 8

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**4** **METODOLOGÍA DE MODELACIÓN**

El sistema de modelación propuesto considera el protocolo, WRF/CALPUFF, los cuales han

sido adaptados a las condiciones del área de estudio.

Se aplicó el modelo meteorológico WRF ( _Weather Research and Forecasting_ ), para lo cual se

elaboraron escenarios de campos de vientos que sirven de base para el entendimiento de la

meteorología del área de estudio. Por otra parte, se realizó un procesamiento espacial de

inventarios de emisiones para ser utilizado en el modelo de dispersión de contaminantes.

CALPUFF es un modelo dinámico tipo _puff_, concordante con las recomendaciones

entregadas en la Guía para el Uso de Modelos de Calidad del Aire del SEIA **[1]** (en adelante,

Guía de Modelación del SEIA), que asume que de una sola fuente sale una bocanada ( _puff_ ),

la cual va sufriendo alteraciones a medida que se dispersa y transporta, a través de

mecanismos de advección, difusión, recirculación y transformaciones químicas.

La Figura 2 muestra el protocolo de modelación utilizado en el presente estudio.

Figura 2. Protocolo de Modelación

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 9

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**4.1** **Modelo Meteorológico**

La modelación meteorológica se realizó utilizando WRF ( _Weather Research and Forecasting_

_Model_, por sus siglas en inglés) en base a los criterios y recomendaciones establecidos por

la US EPA ( _Guidance on the Use of Models and Other Analyses for Demonstrating Attainment_

_of Air Quality Goals for Ozone, PM2.5, and Regional Haze, 2007_ ) y según se indica en la Guía

de Modelación del SEIA.

En términos esenciales, el modelo WRF consta de tres módulos principales, WPS, WRF-Var y

ARW-WRF, tal como se aprecia en el esquema presentado en la Figura 3.

Figura 3. Esquema general de funcionamiento de WRF-ARW

Fuente: Elaboración propia en base a información del Manual del Usuario de WRF

**4.2** **Características del Dominio de Modelación y su Entorno**

De acuerdo a los requerimientos metodológicos, el consultor recopiló, procesó y seleccionó

los datos de entrada, necesarios para alimentar el modelo meteorológico y de dispersión,

ajustando al formato correspondiente. A continuación, se presenta la data utilizada,

haciendo referencia de los criterios de selección empleados, y describiendo aquellos

elementos que tienen incidencia en los procesos de transporte y dispersión de

contaminantes.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 10

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**4.2.1** **Dominio de Modelación**

Para efecto de evaluar el impacto en la calidad del aire provocado por el proyecto, se ha

seleccionado un dominio de modelación en función de la disponibilidad de información

meteorológica y cercanía a receptores de interés. Posee una dimensión de 50 x 50 km, con

un tamaño de celda de 1 x 1 km. La Tabla 2 muestra las coordenadas de los vértices del

dominio de modelación.

Figura 4. Dominio de modelación WRF/CALPUFF

Fuente: Elaboración propia

Tabla 2. Coordenadas vértices del área de modelación del proyecto (Huso 18 - WGS84)

|Identificación|Coordenada E (m)|Coordenada S (m)|
|---|---|---|
|~~NO~~|~~641803~~|~~5942965~~|
|NE|689335|5942068|
|SO|640955|5895828|
|SE|688368|5894950|

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 11

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**4.2.2** **Topografía y Uso de Suelo**

La topografía del dominio fue obtenida de las bases satelitales topográfica SRTM1 que

poseen una cobertura global con aproximadamente 90 m de resolución y las bases de uso

de suelo GLCC con 1 km de resolución. La representación en tres dimensiones en la Figura

5 da cuenta de los principales accidentes topográficos de la zona de estudio, en particular,

se aprecia la zona costera de la comuna de San Pedro de La Paz y desembocadura del río

Bíobio, la zona cordillera de la costa.

Figura 5. Topografía del área de modelación 3D

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 12

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**5** **CARACTERIZACIÓN METEOROLÓGICA**

**5.1** **Información Meteorológica**

La información meteorológica utilizada proviene de estaciones de superficie cercanas al área

del proyecto y en altura de una estación de radio sondeo. A continuación, en la Tabla 3 y

Tabla 4 se detallan las fuentes de información y sus características, para datos de calidad del

aire y variables meteorológicas de superficie y altura, respectivamente, para el año base

2020.

Tabla 3. Estaciones meteorológicas y calidad del aire para datos en superficie cercanas al proyecto

|Nombre<br>Estación|Coordenadas UTM (18 H)|Col3|Calidad del Aire|Col5|Variables<br>meteorológicas|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|Nombre<br>Estación|UTM-E|UTM-S|MP2.5|MP10|HR|TA|DV|VV|RG|
|Bocatoma|667680|5925321|X|X|-|-|-|-|-|
|Masisa|665704|5918379|-|-|X|X|X|X|X|

HR: humedad relativa; TA: Temperatura ambiente; P: Presión atmosférica; DV: dirección del viento; VV: velocidad del viento,

PP: precipitaciones; RG: Radiación global

Tabla 4. Ubicación Estación de Radiosondeo para datos de altura

|Nombre Estación|Coordenadas UTM (19 H)|Col3|
|---|---|---|
|Nombre Estación|UTM-E|UTM-N|
|Santo Domingo|257969|6273039|

**5.2** **Rosas de Los Vientos**

De los datos meteorológicos utilizados por el modelo, los más relevantes son la velocidad y

dirección del viento preponderante de la zona. A continuación, en los gráficos siguientes se

presenta la rosa de los vientos en un análisis estacional (verano, otoño, primavera, verano),

Los datos analizados corresponden a lo registrado por la Estación Masisa, de la comuna de

San Pedro de la Paz, en el año 2021, perteneciente a la red de monitoreo meteorológico y

de calidad del aire del Ministerio de Medio Ambiente (SINCA), la cual corresponde a la

estación más cercana a la fuente, que presenta registro de datos horarios. Por otra parte, es

importante mencionar que para la elaboración de las rosas de los vientos se empleó la

opción de “ _blowing from_ ”, es decir que el vector sopla desde el origen hacia la estación.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 13

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

|A|B|
|---|---|
|<br>**C **|<br>**D **|

Figura 6. Rosas de los vientos estacionales (A: verano, B: otoño, C: Invierno, D: Primavera)

Fuente: En base a datos meteorológicos año 2021, Estación Masisa.

De las rosas de los vientos estacionales se puede observar una notoria variabilidad en la

velocidad y dirección del viento entre las estaciones frías y cálidas del año. Las rosas

muestran predominancia de los vientos que soplan desde sur en la estación de verano. Para

las estaciones de otoño e invierno la dirección del viento tiene su origen en el norte soplando

hacia el sur.

Respecto a la velocidad registrada en la estación, se observa que en todas las estaciones

predominan los vientos en el rango de 3,6 a 5,7 m/s y distribuidos de forma uniforme en

ambos periodos para épocas frías y cálidas.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 14

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**5.2.1** **Series de Tiempo**

A continuación, se presentan los gráficos de series de tiempo de las variables meteorológicas

temperatura, velocidad del viento, humedad relativa, presión atmosférica en términos de

valores horarios, para el año 2021.

De la serie de tiempo de temperatura, se observa poca variación estacional estacionalidad,

apreciándose los valores mínimos entre los meses de junio a septiembre, encontrándose

que los valores horarios fluctúan entre -1 y 20 °C en este periodo. Se observa que para el

mes de julio la data presenta algún tipo de error ya que las temperaturas se escapan del

rango esperado para el periodo del año.

Para la variable velocidad del viento, se puede apreciar que se encuentran los mayores

valores máximos horarios se encuentran cercanos a los 7 m/s. En general, los valores

observados dan cuenta de que los vientos en el área de estudio presentan alta variación a

lo largo de todas las estaciones.

En relación a la humedad relativa es posible observar una marcada estacionalidad,

presentándose los mayores valores durante los meses fríos del año.

En general, en análisis de las variables meteorológicas que caracterizan el área de estudio

indica poca variación estacional, apreciándose diferencias bajas a través de los meses.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 15

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 7. Series de tiempo horaria de variables meteorológicas año 2021

Fuente: Elaboración propia a partir de la data de estación meteorológica Masisa

**5.2.2** **Ciclos Estacionales**

A continuación, se presenta la variación estacional de los ciclos diarios de las variables

velocidad, temperatura y dirección del viento.

El gráfico de la variación estacional del ciclo diario de la velocidad del viento, presentado en

la Figura 8, demuestra la diferencia tanto mensual como a lo largo del día, en el área de

estudio. Encontrándose durante el periodo nocturno menores velocidades que durante el

día, con los valores máximos entre las 15:00 y las 19:00 en los meses entre noviembre y

diciembre. Mientras que durante los meses fríos (abril a agosto) se encuentran velocidades

menores, lo que propicia condiciones para generar episodios de contaminación, asociado a

la mala ventilación del ambiente.

Figura 8. Variación estacional del ciclo diario de la velocidad del viento

Fuente: Elaboración propia en base a datos meteorológicos año 2021, Estación Masisa

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 16

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

La variación estacional del ciclo diario de la temperatura muestra una marcada variación

mensual y horaria. Encontrándose las mayores temperaturas entre los meses de noviembre

a marzo, entre las 13:00 y las 17:00 horas. Situación que se observa también con la variable

humedad relativa, pero en relación inversa a la temperatura.

Figura 9. Variación estacional del ciclo diario de la Temperatura
Fuente: Elaboración propia en base a datos meteorológicos año 2021, Estación Masisa

Figura 10. Variación estacional del ciclo diario de la Humedad Relativa

Fuente: Elaboración propia en base a datos meteorológicos año 2021, Estación Masisa

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 17

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**5.2.3** **Ciclos estacionales de datos en altura**

A continuación, se presenta el ciclo estacional del perfil vertical de las variables temperatura

y velocidad del viento.

La variación estacional de los datos de altura de la variable temperatura, presentada en la

Figura 11, da cuenta de una tendencia homogénea, a lo largo de cada nivel de altura, durante

el año, alcanzándose en general, los 15°C hasta los 2000 m de altura. Mientras que los 0° se

alcanzan a la altura cercana a los 5000 m.

Figura 11. Variación estacional del perfil vertical de temperatura
Fuente: Elaboración propia en base a datos meteorológicos año 2021 radiosonda Santo Domingo

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 18

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

La variación estacional de los datos de altura de la velocidad de viento, presentada en la

Figura 12, da cuenta de una variación en los distintos meses en estudio. En general, hasta

los 4.000 m de altura, las velocidades del viento se consideran con poca variación entre los

distintos meses de monitoreo. Mientras que, sobre los 7.000 m de altura, la velocidad del

viento varía, de acuerdo al periodo del año en que se mida. De esta manera, entre diciembre

y marzo, se aprecian menores velocidades que entre los meses de abril y noviembre,

alcanzándose velocidades tan altas como 50 m/s, durante los meses de junio a agosto, en

altura sobre los 10.000 m.

Figura 12. Variación estacional del perfil vertical de velocidad de viento
Fuente: Elaboración propia en base a datos meteorológicos año 2021 radiosonda Santo Domingo

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 19

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**6** **CARACTERIZACIÓN DE CALIDAD DEL AIRE**

Para la caracterización de la calidad del aire se consideró la información entregada por la

estación de monitoreo “Bocatoma”, de propiedad de ENAP, con información disponible en

la plataforma SINCA del Ministerio del Medio Ambiente, la cual corresponde a la estación

con datos validados, más cercana a la ubicación del proyecto. Para la caracterización se

emplearon los datos de concentración de material particulado MP10 y MP2,5, para el

periodo 2019-2021.

**Material Particulado MP10**

El D.S. N°12/22 del MMA [2], establece la norma primaria de calidad ambiental material

particulado respirable MP10 y deroga el D.S. N° 59/98 de MINSEGPRES. La norma primaria

como concentración diaria se considera sobrepasada cuando en un año calendario, el valor

correspondiente al percentil 98 de las concentraciones de 24 horas registradas, sea mayor o

igual a 130 μg/m [3] N o, si antes que concluya un año calendario, el número de días con

mediciones sobre el valor de 130 μg/m [3] N, sea mayor que siete.

Asimismo, la norma establece el límite de 50 μg/m [3] N, como concentración anual,

considerándose sobrepasada cuando el promedio trianual [1] de las concentraciones anuales

sea mayor al valor indicado, en cualquier estación monitora calificada como EMRP.

La información respecto a la evaluación de la norma de calidad primaria de MP10, en la

Estación Bocatoma, se presenta en la Tabla 5.

Tabla 5. Parámetros de cumplimiento de norma de MP10 años 2019-2021

|Parámetro|2019|2020|2021|
|---|---|---|---|
|Norma anual|Norma anual|Norma anual|Norma anual|
|Promedio Anual (μg/m3 N)|21||24|
|No datos validados|360|30|279|
|% datos validados|99%|8%|76%|
|Promedio Trianual (μg/m3 N)*|23|23|23|
|Norma|50|50|50|
|% norma|45%|45%|45%|
|Norma diaria|Norma diaria|Norma diaria|Norma diaria|
|Percentil 98|53||49|
|Norma|150|150|130|
|% norma|35%||38%|

*Promedio trianual referencial (se considera solo 2019-2021.
Fuente: Elaboración propia en base a la data de calidad del aire de la Estación Bocatoma, [www.sinca.cl](http://www.sinca.cl/)

1 Promedio trianual corresponde al promedio aritmético de tres años calendario consecutivos de la concentración anual, en
cualquier estación monitora.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 20

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

La data de calidad del aire disponible presenta información para los años 2019 y 2021. Para

el año 2020 presenta solo 30 días de medición, por lo que se descarta como año válido para

el análisis. Para el caso del año 2021, se cuenta con 3 meses con una cantidad de datos

menor al 75%, por lo tanto, se completan estos meses con el mes de mayor concentración

para poder evaluar la data.

Según el análisis de la data de calidad del aire disponible, la norma diaria y anual no se vería

sobrepasada, ya que el resultado anual indica que las concentraciones de MP10 están en el

45% de cumplimiento de norma anual, y entre el 35 y 38% de norma diaria. El análisis de

entrega de manera referencial ya que para el año 2020 no se cuenta con data suficiente para

establecer el cumplimiento de norma anual (evaluación trianual).

Figura 13. Evaluación de Norma diaria para MP10
Fuente: Elaboración propia en base a la data de calidad del aire de la estación Bocatoma, www.sinca.cl

Figura 14. Evaluación de Norma Anual para MP10
Fuente: Elaboración propia en base a la data de calidad del aire de la estación Bocatoma, www.sinca.cl

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 21

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**Material Particulado MP2,5**

El D.S. N°12/11 [2], establece que la norma primaria de calidad del aire para el contaminante

Material Particulado Fino MP2,5, es 50 μg/m [3] N como concentración de 24 horas,

considerándose sobrepasada cuando el percentil 98 de las concentraciones de 24 horas

registradas durante un período anual en cualquier estación monitora calificada EMRP, sea

mayor a 50 μg/m [3] .

Asimismo, la norma establece el límite de 20 μg/m [3] N, como concentración anual,

considerándose sobrepasada cuando el promedio trianual [2] de las concentraciones anuales

sea mayor a 20 μg/m [3], en cualquier estación monitora calificada como EMRP.

La información respecto a la evaluación de la norma de calidad primaria de MP2,5, de

acuerdo a los datos registrados en la estación de monitoreo Bocatoma se presenta en la

Tabla 6.

Tabla 6. Parámetros de cumplimiento de norma de MP2,5 años 2019-2021

|Parámetro|2019|2020|2021|
|---|---|---|---|
|Norma anual|Norma anual|Norma anual|Norma anual|
|Promedio Anual (μg/m3 N)|15|N.V.|17|
|No datos validados|361|30|279|
|% datos validados|99%|8%|76%|
|Promedio Trianual (μg/m3 N)*|16|16|16|
|Norma|20|20|20|
|% norma|84%|84%|84%|
|Norma diaria|Norma diaria|Norma diaria|Norma diaria|
|Percentil 98|43||42|
|Norma|50||50|
|% norma|86%||84%|

*Promedio trianual referencial (se considera solo 2019-2021.
Fuente: Elaboración propia en base a la data de calidad del aire de la Estación Bocatoma, [www.sinca.cl](http://www.sinca.cl/)

La data de calidad del aire disponible presenta información para los años 2019 y 2021. Para

el año 2020 presenta solo 30 días de medición, por lo que se descarta como año válido para

el análisis. Para el caso del año 2021, se cuenta con 3 meses con una cantidad de datos

menor al 75%, por lo tanto, se completan estos meses con el mes de mayor concentración

para poder evaluar la data.

Según el análisis de la data de calidad del aire disponible, la norma diaria y anual no se vería

sobrepasada, sin embargo, se observa la condición de latencia, ya que el resultado anual

indica que las concentraciones de MP2,5 están en el 84% de cumplimiento de norma anual,

2 Promedio trianual corresponde al promedio aritmético de tres años calendario consecutivos de la concentración anual, en
cualquier estación monitora.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 22

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

y entre el 86 y 84% de norma diaria. El análisis de entrega de manera referencial ya que para

el año 2020 no se cuenta con data suficiente para establecer el cumplimiento de norma

anual (evaluación trianual).

Figura 15. Evaluación de Norma diaria para MP2,5
Fuente: Elaboración propia en base a la data de calidad del aire de la estación Bocatoma, www.sinca.cl

Figura 16. Evaluación de Norma anual para MP2,5
Fuente: Elaboración propia en base a la data de calidad del aire de la estación Bocatoma, www.sinca.cl

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 23

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**7** **CARACTERIZACIÓN DE LA FUENTE Y SUS EMISIONES**

**7.1** **Identificación de las fuentes emisoras**

Las fuentes de emisión identificadas para el Proyecto se presentan a continuación en la siguiente

tabla.

Tabla 7. Fuentes de emisiones atmosféricas, durante etapa de construcción del Proyecto.

|Tipo de<br>Emisión|Actividad|Tipo de contaminante|Etapa|
|---|---|---|---|
|Emisiones<br>directas|Demolición|MP10, MP2,5|<br> <br> <br> <br> <br>Construcción|
|Emisiones<br>directas|Escarpe, Compactación y Nivelación|MP10, MP2,5|MP10, MP2,5|
|Emisiones<br>directas|Excavaciones|MP10, MP2,5|MP10, MP2,5|
|Emisiones<br>directas|Carguío de camiones y transferencia de material|MP10, MP2,5|MP10, MP2,5|
|Emisiones<br>directas|Erosión del material en pila|MP10, MP2,5|MP10, MP2,5|
|Emisiones<br>directas|Tránsito por caminos no pavimentados al interior del sitio<br>donde se emplaza el proyecto (vehículos pesados)|MP10, MP2,5 y gases de<br>combustión|MP10, MP2,5 y gases de<br>combustión|
|Emisiones<br>directas|Emisiones de gases de combustión de maquinaria y vehículos|MP10, MP2,5 y gases de<br>combustión|MP10, MP2,5 y gases de<br>combustión|
|Emisiones<br>indirectas|Tránsito por caminos pavimentados fuera del sitio donde se<br>emplaza el proyecto (vehículos pesados y livianos)|MP10, MP2,5 y gases de<br>combustión|Construcción /operación|
|Emisiones<br>indirectas|Emisiones de gases de combustión de maquinaria y vehículos|MP10, MP2,5 y gases de<br>combustión|Construcción /operación|
|Emisiones<br>indirectas|Emisiones de combustión residencial|MP10, MP2,5 y gases de<br>combustión|operación|

Fuente: Elaboración propia en base a Estudio de Estimación de Emisiones Atmosféricas.

Las emisiones de material particulado y gases de combustión para la **fase de operación**

están dadas por el tránsito de vehículos livianos de propiedad de los residentes y la

calefacción domiciliaria, cuyas emisiones son presentadas en el Anexo “Estimación de

Emisiones Atmosféricas Proyecto Loteo Pintor Pedro Luna”.

**7.2** **Perfil Temporal**

El perfil temporal correspondiente a la fase de construcción fue determinado de acuerdo

con la información entregada por la empresa, definiéndose un funcionamiento con 10 horas

de trabajos, según se presenta en la Tabla 8. Respecto a las emisiones mensuales, éstas se

basan directamente en el cronograma presente en el anexo “Estimación de Emisiones

Atmosféricas Proyecto Pintor Pedro Luna”. La Figura 17, muestra por otra parte el perfil

temporal para la fase de operación del proyecto en su componente calefacción residencial.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 24

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Tabla 8. Días de funcionamiento de la fuente

|Horario|SEMANA|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|<br>**Horario**|Lun|Mar.|Mie.|Jue.|Vie.|Sab.|Dom.|
|8-9|X|X|X|X|X|||
|9-10|X|X|X|X|X|||
|10-11|X|X|X|X|X|||
|11-12|X|X|X|X|X|||
|12-13|X|X|X|X|X|||
|13-14|X|X|X|X|X|||
|14-15|X|X|X|X|X|||
|15-16|X|X|X|X|X|||
|16-17|X|X|X|X|X|||
|17-18|X|X|X|X|X|||

Fuente: Elaboración propia

Figura 17. Perfil temporal emisiones calefacción

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 25

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8** **RESULTADOS DE LA MODELACIÓN**

**8.1** **Validación Meteorológica**

Se presenta a continuación, la validación de la velocidad del viento en base a la serie de

tiempo anual de la estación Escuadrón ENESA, la que presenta mayor cantidad de datos

válidos que la estación Masisa, se puede apreciar que el modelo es capaz de captar las

tendencias estacionales, existiendo únicamente algunas sobrestimaciones menores en

agosto y septiembre. Para esta variable el coeficiente de correlación es de 0,45 lo que da

cuenta de un desempeño aceptable del modelo para la variable velocidad del viento.

Figura 18. velocidad del viento modelada v/s modelada serie anual

Fuente: Elaboración propia

Figura 19. Correlación Velocidad del viento observada v/s modelada serie anual

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 26

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8.2** **Resultados de la Modelación Meteorológica**

A continuación, se presentan los resultados obtenidos con el modelo WRF aplicado para el

año base 2021, considerando 365 días de procesamiento. Las siguientes figuras representan

los campos de viento estacionales y horarios entregados por la simulación. Es posible

observar que el modelo estima de manera adecuada el comportamiento de las variables

meteorológicas ejemplificadas en los campos de viento, puesto que se mantiene la

tendencia observada en las rosas de los vientos y los gráficos de variación estacional de los

ciclos diarios. De manera general, es posible apreciar que las condiciones de estabilidad se

ven favorecidas principalmente en el periodo de invierno, generando peores condiciones de

ventilación, lo que incide en la generación de episodios de contaminación como queda de

manifiesto en el análisis de calidad del aire. En contraposición, los meses más cálidos

presentan condiciones que favorecen la dispersión de contaminantes. Se evidencia además

un comportamiento del vector del viento dependiente de las masas de agua presentes en la

zona, dónde en verano/primavera el vector tiene dirección norte en periodo diurno y

nocturno, y en dirección sur en otoño/invierno.

Los campos de vientos permitirán determinar posteriormente la dispersión de los

contaminantes, por medio de la aplicación del modelo CALPUFF.

Figura 20. Campos de viento estación: Verano-periodo nocturno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 27

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 21. Campos de viento estación: Verano-periodo diurno

Fuente: Elaboración propia

Figura 22. Campos de viento estación: Otoño-periodo nocturno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 28

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 23. Campos de viento estación: Otoño-periodo diurno

Fuente: Elaboración propia

Figura 24. Campos de viento estación: Invierno-periodo nocturno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 29

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 25. Campos de viento estación: Invierno-periodo diurno

Fuente: Elaboración propia

Figura 26. Campos de viento estación: Primavera-periodo nocturno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 30

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 27. Campos de viento estación: Primavera-periodo diurno

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 31

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8.3** **Resultados de la Modelación de Dispersión de Contaminantes**

**8.3.1** **Determinación de concentración en el punto de Máximo Impacto Etapa**

**Construcción y Operación.**

En respuesta al objetivo de la consultoría, a continuación, se presentan los valores

modelados para los contaminantes con mayor relevancia para el área de estudio,

determinado en el punto de máximo impacto, contrastando respecto a los límites de las

Normas Primarias de Calidad del Aire. Se presentan los resultados para MP10 y MP2,5 como

percentil 98 de las concentraciones anuales del promedio de 24 horas.

Los resultados para MP10 y MP2.5 como concentraciones anuales se presentan más adelante

en el informe.

Tabla 9. Resultados de la modelación de calidad del aire (máximo impacto).

|Contaminante|Construcción|Col3|Operación|Col5|
|---|---|---|---|---|
|Contaminante|Máx. (μg/m3)|% r/Norma|Máx. (μg/m3)|% r/Norma|
|MP10 (24h.)|0,49|0,38|2,70|2,10|
|MP2.5 (24h.)<br>|0,12<br>|0,24|1,80|3,60|

Fuente: Elaboración propia

**8.3.2** **Mapas de Isoconcentraciones Construcción**

En los gráficos siguientes, se muestran las concentraciones de contaminante modelados

según las normativas de referencia. En ellas se observa cómo se dispersa la pluma

contaminante desde su fuente generadora (principalmente Resuspensión de MP en sus

fracciones normadas), hasta llegar a sectores colindantes, donde, es posible apreciar un bajo

impacto al contrastar con la normativa nacional para cada contaminante y/o con los índices

considerados inseguros para la salud de la población. También se observa que el impacto

de la fuente solo está presente en la zona inmediatamente adyacente a la zona de

construcción y transporte de materiales, sin evidenciarse concentraciones relevantes en las

rutas modeladas (bajo 0,5 g/m [3] para MP10) A continuación, se presentan los mapas de

Isoconcentraciones que dan cuenta las concentraciones del proyecto y permite

contextualizar el impacto de las fuentes en función de los distintos contaminantes

normados.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 32

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 28. Modelación de Dispersión de MP10 P98 promedio 24 hrs. Fase Construcción.

Fuente: Elaboración propia

Figura 29. Modelación de Dispersión de MP2.5 P98 promedio 24 hrs. Fase Construcción.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 33

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 30. Modelación de Dispersión de CO promedio 1 hora Fase Construcción.

Fuente: Elaboración propia

Figura 31. Modelación de Dispersión de SO 2 P99 promedio 24 hora Fase Construcción

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 34

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 32. Modelación de Dispersión de NOx máximo horario Fase Construcción.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 35

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8.3.3** **Mapas de Isoconcentraciones Operación**

Al evaluar en conjunto la dispersión de los contaminantes, queda de manifiesto el bajo

impacto de las emisiones de las fuentes modeladas, viéndose que el área de mayores

impactos corresponde exclusivamente al sector colindante con el proyecto, Es importante

destacar además que al evaluar el impacto de la fuente sobre receptores discretos no se

registran concentraciones que pudieran considerarse nocivas para la salud (ver anexo).

Figura 33.Modelación de Dispersión de MP10 P98 promedio 24 hrs Fase Operación.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 36

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 34. Modelación de Dispersión de MP2.5 P98 promedio 24 hrs Fase de Operación.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 37

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 35. Modelación de Dispersión de SO 2 P99 promedio 24 hora Fase de Operación

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 38

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 36. Modelación de Dispersión de NOx máximo horario Fase Operación.

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 39

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Figura 37. Modelación de Dispersión de CO promedio 1 hora Fase de Operación.

Fuente: Elaboración propia

Al evaluar en conjunto la dispersión de los contaminantes, queda de manifiesto el bajo

impacto de las emisiones de las fuentes modeladas, viéndose que el área de mayores

impactos corresponde exclusivamente al sector colindante con el proyecto, Es importante

destacar además que al evaluar el impacto de la fuente sobre receptores discretos no se

registran concentraciones que pudieran considerarse nocivas para la salud de la población

(ver anexo).

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 40

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**8.3.4** **Determinación de receptores y concentración de inmisión**

Considerando todo el dominio de modelación, se determinaron los receptores que pudieran

determinar una zona de impacto del proyecto en función de su exposición. Así se definieron

5 lugares donde existen viviendas y/o lugares de alojamiento que representan los principales

centros poblados aledaños al proyecto y rutas en evaluación.

Figura 38. Receptores evaluados en el proyecto

Fuente: Elaboración propia

Tabla 10. Identificación de los receptores discretos

|Col1|Receptor|Col3|Col4|Col5|
|---|---|---|---|---|
|ID|Tipo|Distancia (m)|Coordenada UTM E|Coordenada UTM S|
|R1|Viviendas|40|665132|5919130|
|R2|Viviendas|80|665284|5919289|
|R3|Viviendas|47|665148|5919479|
|R4|Piscina y<br>departamentos|85|664931|5919329|
|R5|departamentos|280|665017|5919733|

Fuente: Elaboración propia

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 41

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Tabla 11. Resultados de la modelación de calidad del aire (MP10) Construcción

|Receptor|Concentración (g/m3)|
|---|---|
|MP10 (p 98 promedio 24 hrs)|MP10 (p 98 promedio 24 hrs)|
|R1|2,3448E-04|
|R2|1,1576E-04|
|R3|2,2113E-04|
|R4|3,7454E-05|
|R5|1,2545E-05|
|MP10 (promedio anual)|MP10 (promedio anual)|
|R1|3,2105E-05|
|R2|4,3000E-05|
|R3|2,7994E-05|
|R4|5,5030E-06|
|R5|1,5977E-06|

Fuente: Elaboración propia

Tabla 12. Resultados de la modelación de calidad del aire (MP2.5) Construcción

|Receptor|Concentración (g/m3)|
|---|---|
|MP2,5 (p 98 promedio 24 hrs)|MP2,5 (p 98 promedio 24 hrs)|
|R1|5,0969E-05|
|R2|2,6390E-05|
|R3|4,8538E-05|
|R4|8,9804E-06|
|R5|2,9753E-06|
|MP2,5 (promedio anual)|MP2,5 (promedio anual)|
|R1|7,7007E-06|
|R2|1,0365E-05|
|R3|7,2067E-06|
|R4|1,4732E-06|
|R5|5,3696E-07|

Fuente: Elaboración propia

Tabla 13. Resultados de la modelación de calidad del aire (MP10) operación

|Receptor|Concentración (g/m3)|
|---|---|
|MP10 (p 98 promedio 24 hrs)|MP10 (p 98 promedio 24 hrs)|
|R1|1,5829|
|R2|1,2445|
|R3|2,6587|
|R4|1,1913|
|R5|0,8546|
|MP10 (promedio anual)|MP10 (promedio anual)|
|R1|2,6645E-01|
|R2|2,6320E-01|
|R3|5,4472E-01|
|R4|1,4935E-01|
|R5|8,5950E-02|

Fuente: Elaboración propia.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 42

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

Tabla 14. Resultados de la modelación de calidad del aire (MP2.5) operación

|Receptor|Concentración (g/m3)|
|---|---|
|MP2.5 (p 98 promedio 24 hrs)|MP2.5 (p 98 promedio 24 hrs)|
|R1|1,0508|
|R2|0,8261|
|R3|1,0765|
|R4|0,7909|
|R5|0,5673|
|MP2,5 (promedio anual)|MP2,5 (promedio anual)|
|R1|1,7689E-01|
|R2|1,7472E-01|
|R3|3,6166E-01|
|R4|9,9155E-02|
|R5|5,7066E-02|

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 43

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**9** **CONCLUSIONES**

Con los resultados obtenidos mediante la modelación es posible concluir que las emisiones

provenientes del proyecto Loteo Pintor Pedro Luna, no provocarán un aporte significativo

sobre las concentraciones de contaminantes criterio en la zona de San Pedro de La Paz y

comunas colindantes, para las etapas de construcción y operación, dado que, en su

operación, donde las emisiones representan el peor escenario asociado al uso de leña para

calefacción, no provocaría un riesgo significativo para la salud de la población, debido a las

bajas concentraciones de MP10 y MP2.5 .

Lo anterior se sustenta, en que el punto de mayor impacto de MP10 y MP2,5 se encuentra

inmediatamente alrededor de la zona de viviendas, alcanzando ahí 2,7 μg/m [3] para MP10 y

1,8 μg/m [3] para MP2,5 como máxima concentración percentil 98 del promedio 24h para el

año evaluado con información meteorológica 2021.

Para los contaminantes SO 2, CO y NO 2, de acuerdo con los resultados obtenidos, se puede

concluir que las concentraciones generadas por las fuentes no influyen de manera

significativa sobre la calidad del aire de la comuna en estudio, por cuanto, los puntos de

máximo impacto están muy por debajo de los límites normativos, siendo las concentraciones

en dicha ubicación de 4,8x10 [-1 ] μg/m [3], 1,1x10 [-1] mg/m [3] y 14,2 g/m [3], respectivamente.

Con todo lo anterior, se puede concluir que el proyecto no provocará efectos adversos

significativos sobre la salud de la población ubicada tanto en el área circundante al proyecto

como en los receptores evaluados y para los periodos de construcción y operación.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 44

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

**10** **REFERENCIAS**

[1] SEIA, «Guía para el Uso de Modelos de Calidad del Aire en el SEIA,» Servicio de

Evaluación Ambiental, Chile, 2012.

[2] MMA, «D,S,N° 12/11 Establece Norma Primaria de Calidad del Aire para Material

Particulado Fino MP2,5,,» 2011.

[3] MMA, «D,S, N° 12/2022 Establece Norma de Calidad Primara para Material Particulado

Respirable MP10.

SERVICIOS INTEGRALES DE CALIDAD AMBIENTAL LTDA. - SICAM INGENIERÍA 45

Prieto Sur 965, Temuco - Chile

[Email: cvarela@sicam.cl - Teléfono: (045) 2668119 - Web: www.sicam.cl](http://www.sicam.cl/)

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Norma de calidad del aire para Material Particulado.**

| Contaminante | Valor | Periodo de<br>Evaluación | Forma de Verificación | Fuente<br>Normativa |
| --- | --- | --- | --- | --- |
| ~~Material~~<br>particulado<br>respirable<br>(MP10) | ~~130 μg~~<br>/m3N | ~~Promedio aritmético~~<br>de 24 hrs. | ~~Percentil 98 de valores de un~~<br>año o más de 7 días en un año. | ~~D.S. N° 12/2022~~<br>del MMA que<br>deroga<br>D.S.<br>N°59/98<br>MINSEGPRES |
| ~~Material~~<br>particulado<br>respirable<br>(MP10) | 50 μg /m3N | Promedio aritmético<br>anual | Promedio aritmético de 3 años<br>consecutivos. | Promedio aritmético de 3 años<br>consecutivos. |
| Material<br>particulado fino<br>(MP2.5) | 50 μg /m3 | Promedio aritmético<br>de 24 hrs. | Percentil 98 de valores de 1<br>año. | D.S. N° 12/2011<br>del<br>Ministerio<br>del<br>medio<br>Ambiente |
| Material<br>particulado fino<br>(MP2.5) | 20 μg /m3 | Promedio aritmético<br>anual. | Promedio aritmético de 3 años<br>consecutivos. | Promedio aritmético de 3 años<br>consecutivos. |
| Dióxido de<br>azufre (SO2) | 80 μg /m3N | Media aritmética<br>anual | Promedio de tres años del<br>percentil 99 de las<br>concentraciones de 24 horas. | D.S.<br>No113/2002<br>del<br>MINSEGPRES |
| Dióxido de<br>azufre (SO2) | 250 μg<br>/m3N | Media aritmética<br>diaria | Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. | Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. |
| Monóxido de<br>Carbono<br>(CO) | 30 mg/<br>m3N | Media aritmética<br>horaria | Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora. | D.S.<br>No115/2002<br>del<br>MINSEGPRES |
| Monóxido de<br>Carbono<br>(CO) | 10 mg/<br>m3N | Promedio móvil de 8<br>hrs. | Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. | Promedios de tres años del<br>percentil 99 de los máximos<br>diarios promedios de 8 horas. |
| Dióxido de<br>nitrógeno (NO2) | 100 μg<br>/m3N | Media aritmética<br>anual | Promedio aritmético de 3 años<br>consecutivos. | D.S.<br>No114/2002<br>del<br>MINSEGPRES |
| Dióxido de<br>nitrógeno (NO2) | 400 μg<br>/m3N | Concentración de 1<br>hora | Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora | Promedio de tres años del<br>percentil 99 de los máximos<br>diarios de 1 hora |

**Tabla 2.: Coordenadas vértices del área de modelación del proyecto (Huso 18 - WGS84)**

| Identificación | Coordenada E (m) | Coordenada S (m) |
| --- | --- | --- |
| ~~NO~~ | ~~641803~~ | ~~5942965~~ |
| NE | 689335 | 5942068 |
| SO | 640955 | 5895828 |
| SE | 688368 | 5894950 |

**Tabla 4.: Ubicación Estación de Radiosondeo para datos de altura**

| Nombre Estación | Coordenadas UTM (19 H) | Col3 |
| --- | --- | --- |
| Nombre Estación | UTM-E | UTM-N |
| Santo Domingo | 257969 | 6273039 |

**Tabla 5.: Parámetros de cumplimiento de norma de MP10 años 2019-2021**

| Parámetro | 2019 | 2020 | 2021 |
| --- | --- | --- | --- |
| Norma anual | Norma anual | Norma anual | Norma anual |
| Promedio Anual (μg/m3 N) | 21 |  | 24 |
| No datos validados | 360 | 30 | 279 |
| % datos validados | 99% | 8% | 76% |
| Promedio Trianual (μg/m3 N)* | 23 | 23 | 23 |
| Norma | 50 | 50 | 50 |
| % norma | 45% | 45% | 45% |
| Norma diaria | Norma diaria | Norma diaria | Norma diaria |
| Percentil 98 | 53 |  | 49 |
| Norma | 150 | 150 | 130 |
| % norma | 35% |  | 38% |

**Tabla 6.**

| Parámetro | 2019 | 2020 | 2021 |
| --- | --- | --- | --- |
| Norma anual | Norma anual | Norma anual | Norma anual |
| Promedio Anual (μg/m3 N) | 15 | N.V. | 17 |
| No datos validados | 361 | 30 | 279 |
| % datos validados | 99% | 8% | 76% |
| Promedio Trianual (μg/m3 N)* | 16 | 16 | 16 |
| Norma | 20 | 20 | 20 |
| % norma | 84% | 84% | 84% |
| Norma diaria | Norma diaria | Norma diaria | Norma diaria |
| Percentil 98 | 43 |  | 42 |
| Norma | 50 |  | 50 |
| % norma | 86% |  | 84% |

**Tabla 7.: Fuentes de emisiones atmosféricas, durante etapa de construcción del Proyecto.**

| Tipo de<br>Emisión | Actividad | Tipo de contaminante | Etapa |
| --- | --- | --- | --- |
| Emisiones<br>directas | Demolición | MP10, MP2,5 | <br> <br> <br> <br> <br>Construcción |
| Emisiones<br>directas | Escarpe, Compactación y Nivelación | MP10, MP2,5 | MP10, MP2,5 |
| Emisiones<br>directas | Excavaciones | MP10, MP2,5 | MP10, MP2,5 |
| Emisiones<br>directas | Carguío de camiones y transferencia de material | MP10, MP2,5 | MP10, MP2,5 |
| Emisiones<br>directas | Erosión del material en pila | MP10, MP2,5 | MP10, MP2,5 |
| Emisiones<br>directas | Tránsito por caminos no pavimentados al interior del sitio<br>donde se emplaza el proyecto (vehículos pesados) | MP10, MP2,5 y gases de<br>combustión | MP10, MP2,5 y gases de<br>combustión |
| Emisiones<br>directas | Emisiones de gases de combustión de maquinaria y vehículos | MP10, MP2,5 y gases de<br>combustión | MP10, MP2,5 y gases de<br>combustión |
| Emisiones<br>indirectas | Tránsito por caminos pavimentados fuera del sitio donde se<br>emplaza el proyecto (vehículos pesados y livianos) | MP10, MP2,5 y gases de<br>combustión | Construcción /operación |
| Emisiones<br>indirectas | Emisiones de gases de combustión de maquinaria y vehículos | MP10, MP2,5 y gases de<br>combustión | Construcción /operación |
| Emisiones<br>indirectas | Emisiones de combustión residencial | MP10, MP2,5 y gases de<br>combustión | operación |

**Tabla 8.: Días de funcionamiento de la fuente**

| Horario | SEMANA | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <br>**Horario** | Lun | Mar. | Mie. | Jue. | Vie. | Sab. | Dom. |
| 8-9 | X | X | X | X | X |  |  |
| 9-10 | X | X | X | X | X |  |  |
| 10-11 | X | X | X | X | X |  |  |
| 11-12 | X | X | X | X | X |  |  |
| 12-13 | X | X | X | X | X |  |  |
| 13-14 | X | X | X | X | X |  |  |
| 14-15 | X | X | X | X | X |  |  |
| 15-16 | X | X | X | X | X |  |  |
| 16-17 | X | X | X | X | X |  |  |
| 17-18 | X | X | X | X | X |  |  |

**Tabla 9.: Resultados de la modelación de calidad del aire (máximo impacto).**

| Contaminante | Construcción | Col3 | Operación | Col5 |
| --- | --- | --- | --- | --- |
| Contaminante | Máx. (μg/m3) | % r/Norma | Máx. (μg/m3) | % r/Norma |
| MP10 (24h.) | 0,49 | 0,38 | 2,70 | 2,10 |
| MP2.5 (24h.)<br> | 0,12<br> | 0,24 | 1,80 | 3,60 |

**Tabla 10.: Identificación de los receptores discretos**

| Col1 | Receptor | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| ID | Tipo | Distancia (m) | Coordenada UTM E | Coordenada UTM S |
| R1 | Viviendas | 40 | 665132 | 5919130 |
| R2 | Viviendas | 80 | 665284 | 5919289 |
| R3 | Viviendas | 47 | 665148 | 5919479 |
| R4 | Piscina y<br>departamentos | 85 | 664931 | 5919329 |
| R5 | departamentos | 280 | 665017 | 5919733 |

**Tabla 11.: Resultados de la modelación de calidad del aire (MP10) Construcción**

| Receptor | Concentración (g/m3) |
| --- | --- |
| MP10 (p 98 promedio 24 hrs) | MP10 (p 98 promedio 24 hrs) |
| R1 | 2,3448E-04 |
| R2 | 1,1576E-04 |
| R3 | 2,2113E-04 |
| R4 | 3,7454E-05 |
| R5 | 1,2545E-05 |
| MP10 (promedio anual) | MP10 (promedio anual) |
| R1 | 3,2105E-05 |
| R2 | 4,3000E-05 |
| R3 | 2,7994E-05 |
| R4 | 5,5030E-06 |
| R5 | 1,5977E-06 |

**Tabla 12.: Resultados de la modelación de calidad del aire (MP2.5) Construcción**

| Receptor | Concentración (g/m3) |
| --- | --- |
| MP2,5 (p 98 promedio 24 hrs) | MP2,5 (p 98 promedio 24 hrs) |
| R1 | 5,0969E-05 |
| R2 | 2,6390E-05 |
| R3 | 4,8538E-05 |
| R4 | 8,9804E-06 |
| R5 | 2,9753E-06 |
| MP2,5 (promedio anual) | MP2,5 (promedio anual) |
| R1 | 7,7007E-06 |
| R2 | 1,0365E-05 |
| R3 | 7,2067E-06 |
| R4 | 1,4732E-06 |
| R5 | 5,3696E-07 |

**Tabla 13.: Resultados de la modelación de calidad del aire (MP10) operación**

| Receptor | Concentración (g/m3) |
| --- | --- |
| MP10 (p 98 promedio 24 hrs) | MP10 (p 98 promedio 24 hrs) |
| R1 | 1,5829 |
| R2 | 1,2445 |
| R3 | 2,6587 |
| R4 | 1,1913 |
| R5 | 0,8546 |
| MP10 (promedio anual) | MP10 (promedio anual) |
| R1 | 2,6645E-01 |
| R2 | 2,6320E-01 |
| R3 | 5,4472E-01 |
| R4 | 1,4935E-01 |
| R5 | 8,5950E-02 |

**Tabla 14.: Resultados de la modelación de calidad del aire (MP2.5) operación**

| Receptor | Concentración (g/m3) |
| --- | --- |
| MP2.5 (p 98 promedio 24 hrs) | MP2.5 (p 98 promedio 24 hrs) |
| R1 | 1,0508 |
| R2 | 0,8261 |
| R3 | 1,0765 |
| R4 | 0,7909 |
| R5 | 0,5673 |
| MP2,5 (promedio anual) | MP2,5 (promedio anual) |
| R1 | 1,7689E-01 |
| R2 | 1,7472E-01 |
| R3 | 3,6166E-01 |
| R4 | 9,9155E-02 |
| R5 | 5,7066E-02 |
