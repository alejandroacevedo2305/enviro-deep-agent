---
title: Sin título
author: valentina carné
date: D:20230328152024-03'00'
language: es
type: report
pages: 84
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 16. Modelación de Estimación Atmosféricas
-->

### DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO SANTA GRACIELA SOLAR ANEXO 16 MODELACION ATMOSFERICA MARZO 2023

ANEXO 16. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

# Anexo 16. Modelación de Estimación Atmosféricas

## Declaración de Impacto Ambiental Proyecto “Santa Graciela Solar”

#### Doña Graciela Solar SpA Elaborado por: Geografía, Territorio y Medio Ambiente SpA.

Marzo 2023, Santiago de Chile

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**ÍNDICE**

1 INTRODUCCIÓN ................................................................................................................. 5

2 ANTECEDENTES GENERALES DEL PROYECTO ........................................................... 7

2.1 Breve descripción del Proyecto ........................................................................................... 7

2.2 Localización ......................................................................................................................... 7

2.3 Cronograma ....................................................................................................................... 10

3 CARACTERIZACIÓN ZONA DE ESTUDIO ...................................................................... 11

3.1 Clima .................................................................................................................................. 11

3.2 Meteorología ...................................................................................................................... 13

3.2.1 Dirección y velocidad del viento ................................................................................ 13

3.2.2 Temperatura .............................................................................................................. 16

3.3 Calidad del aire .................................................................................................................. 18

3.3.1 Material Particulado MP 10 .......................................................................................... 19

3.3.2 Material Particulado MP 2.5 ......................................................................................... 20

4 DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO Y LOS CONTAMINANTES

CONSIDERADOS ............................................................................................................................. 21

4.1 Justificación del modelo seleccionado ............................................................................... 21

4.2 Justificación de los contaminantes por modelar ................................................................ 24

4.3 Norma de calidad del aire .................................................................................................. 26

4.4 Análisis de incertidumbre ................................................................................................... 27

4.4.1 Análisis cualitativo ..................................................................................................... 29

4.4.2 Análisis cuantitativo ................................................................................................... 32

5 CONFIGURACIÓN DEL MODELO .................................................................................... 36

5.1 Dominio de modelación ..................................................................................................... 36

5.2 Configuración del modelo .................................................................................................. 38

5.3 Meteorología ...................................................................................................................... 39

5.4 Topografía .......................................................................................................................... 40

6 DATOS DE ENTRADA DEL MODELO .............................................................................. 42

6.1 Fuentes de Emisión ........................................................................................................... 42

6.2 Receptores ......................................................................................................................... 46

7 RESULTADOS DE LA MODELACIÓN ATMOSFÉRICA ................................................... 49

7.1 Isoconcentraciones ............................................................................................................ 49

7.2 Puntos de máxima concentración (PMC) .......................................................................... 65

7.3 Aportes en receptores de interés ....................................................................................... 67

7.4 Escenario Proyectado ........................................................................................................ 72

8 DEFINICIÓN DEL ÁREA DE INFLUENCIA ....................................................................... 75

ii

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

9 ANÁLISIS DE RESULTADOS Y CONCLUSIONES .......................................................... 75

**ÍNDICE DE TABLA**

Tabla 1. Cronograma del Proyecto. .................................................................................................. 10

Tabla 2. Coordenadas estaciones meteorológicas. .......................................................................... 13

Tabla 3. Resumen general de las variables meteorológicas consideradas. ..................................... 13

Tabla 4. Coordenadas y porcentaje de data válida - Estación Puren. ............................................. 19

Tabla 5. Caracterización ambiental de la calidad del aire - Material Particulado MP 10 . .................. 19

Tabla 6. Caracterización ambiental de la calidad del aire - Material Particulado MP 2.5 . .................. 20

Tabla 7. Norma primaria de calidad del aire. .................................................................................... 26

Tabla 8. Norma secundaria de calidad del aire para el SO 2 y norma de referencia para el MPS. ... 27

Tabla 9. Parámetros meteorológicos utilizados en el análisis de incertidumbre. ............................. 28

Tabla 10. Referencias de aceptabilidad para los estadígrafos de cada una de variables

meteorológicas. ................................................................................................................................. 35

Tabla 11. Análisis cuantitativo de la comparación de la data observada y modelada...................... 35

Tabla 12: Descripción del archivo *.INP. ........................................................................................... 38

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- permite ver las características o configuraciones de la modelación realizada. El archivo se estructura de acuerdo con lo que se presenta en la siguiente tabla: -->

**Tabla 12: ** Descripción del archivo *.INP.**

| ID | Descripción |
| --- | --- |
| * | Nombre de la modelación realizada. |
| 0 | Nombre de archivos de entrada y salida de la modelación. |
| 1 | Parámetros de control generales de la corrida: Fecha y hora de inicio, duración de la ejecución,<br>frecuencia temporal. Número de contaminantes. Configuración de reinicio para realizar una serie<br>de ejecuciones de continuación. Formato de datos meteorológicos y ajuste de tiempo promedio. |
| 2 | Opciones Técnicas. Variables de control que determinan los métodos para el tratamiento de la<br>química, deposición húmeda, depositación seca, dispersión, aumento de pluma, terreno. |
| 3 a,b | Listado de especies. Nombres de especies, especies habilitadas, emitidas y depositadas en<br>seco. |
| 4 | Parámetros de control de cuadrícula. Especificación de cuadrículas meteorológicas,<br>computacionales y de muestreo, número de celdas, capas verticales y coordenadas de<br>referencia. |
| 5 | Opciones de salida. Variables de control de impresión, variables de control de salida del disco. |
| 6a, b,<br>c | Configuración del terreno complejo a escala de subcuadrícula (CTSG). Información que describe<br>la ubicación, la forma y la altura de la colina a escala de subcuadrícula. Ubicaciones y altitud de<br>receptores. |
| 7 | Parámetros de deposición seca- Gases. Difusividad de contaminantes, constante de disociación,<br>reactividad, resistencia al mesófilo, coeficiente de la ley de Henry. |
| 8 | Parámetros de deposición seca - Partículas. Diámetro medio de masa geométrica. |
| 9 | Parámetros misceláneos de deposición seca. Resistencias de la cutícula y del suelo de<br>referencia, reactividad del contaminante de referencia, estado de la vegetación. |
| 10 | Parámetros de deposición húmeda. Coeficientes de barrido para cada contaminante y tipo de<br>precipitación (precipitación líquida y congelada). |
| 11 | Parámetros Químicos. Variables de control para la entrada de datos de ozono, concentraciones<br>de fondo de ozono y amoníaco, tasas de transformación nocturna. |
| 12 | Varios parámetros de dispersión y parámetros computacionales. Constantes de dispersión<br>vertical, tasa de dispersión por encima de la capa límite, distancia de cruce a coeficientes de<br>dispersión dependientes del tiempo, uso del suelo asociado con la dispersión urbana, controles<br>de división de bocanadas, coeficientes de trayectoria de la pluma, ley de potencia de la velocidad<br>del viento, gradientes de temperatura y otros. |

<!-- Estadísticas: 14 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 40 ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS -->
<!-- FIN TABLA 12 -->


Tabla 13: Detalle de modelo meteorológico WRF. ........................................................................... 39

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- el desarrollo de un modelo meteorológico de retrospectiva WRF. Los datos de salida, como su localización, fecha, resolución, entre otras, se presentan a continuación: -->

**Tabla 13: ** Detalle de modelo meteorológico WRF.**

| Proyección Cartográfica | Cónica conforme de Lambert (LCC) |
| --- | --- |
| Período | 30 Dic 2021 00:00 - 03 Ene 2023 00:00 |
| Origen | R L AT 01 = 36.760S<br>RLAN0 = 72.069W<br>XLAT1= 37.000S<br>XLAT2 = 36.520S |
| Proyección | Lambert Conic Conformal |
| Datum | NWS-84 6370 km Radius, Global Sphere |
| Grilla | 50 x 50 km |
| Resolución | 1 x 1 km2 |
| Celdas verticales | 10 |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Las variables meteorológicas que contiene el modelo para toda el área de estudio corresponden a -->
<!-- FIN TABLA 13 -->


Tabla 14. Caminos acceso al Proyecto. ............................................................................................ 43

Tabla 15. Receptores de interés. ...................................................................................................... 46

Tabla 16. Puntos de máxima concentración (PMC). ......................................................................... 65

Tabla 17. Aportes del Proyecto en receptores primarios. ................................................................. 68

Tabla 18. Aportes del Proyecto en receptores secundarios. ............................................................ 69

Tabla 19. Relación del aporte del Proyecto con la normativa primaria vigente. ............................... 70

Tabla 20. Relación del aporte del Proyecto con la normativa secundaria vigente. .......................... 71

Tabla 21. Escenario Proyectado - Material Particulado MP 10 . ......................................................... 73

Tabla 22. Escenario Proyectado - Material Particulado MP 2.5 . ........................................................ 74

Tabla 23. Límites normativos considerados en definición del AI - Receptores primarios. ............... 75

iii

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**ÍNDICE DE FIGURA**

Figura 1. Ubicación del del Proyecto. ........................................................................................................... 8
Figura 2. Obras y partes del Proyecto. ......................................................................................................... 9
Figura 3. Clasificación de Köppen para el área de estudio. .................................................................... 12
Figura 4. Serie de tiempo horaria - Velocidad del viento [m/s]. ............................................................. 14
Figura 5. Ciclo diario de la velocidad del viento. ....................................................................................... 14
Figura 6. Ciclo mensual de la velocidad del viento. ................................................................................. 15
Figura 7. Rosa de los vientos - Estación Purén. ...................................................................................... 16
Figura 8. Serie de tiempo horaria - Temperatura [°C]. ............................................................................ 17
Figura 9. Ciclo diario de la temperatura. .................................................................................................... 17
Figura 10. Ciclo mensual de la temperatura. ............................................................................................. 18
Figura 11. Serie de tiempo diaria MP 10 [ug/m3] - Estación Puren. ........................................................ 19
Figura 12. Serie de tiempo diaria MP 2.5 [ug/m3] - Estación Puren. ........................................................ 20
Figura 13. Representación gráfica del modelo tipo Puff y de Pluma. .................................................... 22
Figura 14. Dispersión de la pluma a diferentes horas. ............................................................................ 24
Figura 15. Ciclos de formación de ozono. ................................................................................................. 25
Figura 16. Esquema de oxidación SO x y NO x . .......................................................................................... 25
Figura 17. Ciclo diario de la temperatura observada y modelada. ......................................................... 29
Figura 18. Ciclo mensual de la temperatura observada y modelada. ................................................... 29
Figura 19. Ciclo diario de la velocidad del viento observada y modelada. ........................................... 30
Figura 20. Ciclo mensual de la velocidad del viento observada y modelada. ...................................... 31
Figura 21. Rosa de los vientos observada y modelada. .......................................................................... 31
Figura 22. Dominio de modelación. ............................................................................................................ 37
Figura 23. Topografía del área de estudio. ................................................................................................ 41
Figura 24. Fuentes de emisión en el modelo ............................................................................................ 45
Figura 25. Receptores del modelo - Área del Proyecto .......................................................................... 47
Figura 26. Receptores del modelo - Chillán ............................................................................................. 48
Figura 27. Curva isoconcentración - MP 10 - Norma promedio anual. .................................................. 50
Figura 28. Curva isoconcentración - MP 10 - Norma diaria (P98). ......................................................... 51
Figura 29. Curva isoconcentración - MP 2,5 - Norma promedio anual. ................................................. 52
Figura 30. Curva isoconcentración - MP 2,5 - Norma diaria (P98). ........................................................ 53
Figura 31. Curva isodepositación - MPS - Norma promedio anual. ..................................................... 54
Figura 32. Curva isodepositación - MPS - Norma promedio mensual ................................................. 55
Figura 33. Curva isoconcentración - SO 2 - Norma promedio anual. .................................................... 56
Figura 34. Curva isoconcentración - SO 2 - Norma diaria (P99). ........................................................... 57
Figura 35. Curva isoconcentración - SO 2 - Norma horaria (P98,5). ..................................................... 58
Figura 36. Curva isoconcentración - SO 2 - Norma diaria secundaria (P99,7). ................................... 59
Figura 37. Curva isoconcentración - SO 2 - Norma horaria secundaria (P99,73). .............................. 60
Figura 38. Curva isoconcentración - NO 2 - Norma anual. ..................................................................... 61
Figura 39. Curva isoconcentración - NO 2 - Norma horaria (P99). ........................................................ 62
Figura 40. Curva isoconcentración - CO - Norma horaria (P99). ......................................................... 63
Figura 41. Curva isoconcentración - CO - Norma 8 horas (P99). ........................................................ 64
Figura 42. Localización puntos de máxima concentración (PMC). ........................................................ 66
Figura 43. Área de Influencia primario del Proyecto. ............................................................................... 76
Figura 44. Área de Influencia secundario del Proyecto. .......................................................................... 77

iv

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**1** **INTRODUCCIÓN**

En el presenta anexo corresponde a la modelación de las emisiones atmosféricas asociadas al

desarrollo del proyecto de “Santa Graciela Solar” (en adelante el “Proyecto”) del Titular Doña Graciela

Solar Sp, el cual se localizará en la comuna de San Ignacio, provincia de Diguillín, región de Ñuble.

El Proyecto corresponde la construcción y operación de un nuevo Parque Solar Fotovoltaico (PSF),

destinado a la generación de energía eléctrica a partir de tecnología solar por medio del uso de

módulos fotovoltaicos, montados sobre una estructura con un eje móvil siguiendo la trayectoria del

sol, el presente Proyecto se enmarca dentro de las Energías Renovables No Convencionales

(ERNC) contribuyendo a la diversificación de la matriz energética renovable de la región.

Se contempla que el parque fotovoltaico se emplace al interior de tres (3) terrenos los que serán

denominados Área A, Área B y Área C, con una superficie de 109,17 hectáreas aproximadas, con

una potencia nominal de 80 MWac. En cada una de las Áreas mencionados se emplazarán las obras

temporales y permanentes del Proyecto.

Debido a la tipología del Proyecto, las emisiones atmosféricas y por ende las concentraciones

resultantes generadas se concentran en la fase de construcción del Proyecto, dado que se producen

los principales movimientos de tierra, las circulaciones más intensivas de vehículos y la combustión

de maquinaria que permite implementar la infraestructura necesaria para el desarrollo del proyecto,

por lo que se considera este como el escenario a modelar más desfavorable.

Los contaminantes considerados en la modelación de emisiones corresponden al material

particulado en sus distintas fracciones (MPS, MP 10 y MP 2,5 ) y los gases: dióxidos de nitrógeno (NO 2 ),

dióxidos de azufre (SO 2 ), monóxido de carbono (CO), amoniaco (NH 3 ) y compuestos orgánicos

volátiles (COV) o hidrocarburos (HC), dependiendo del factor de emisión con el que se cuente.

La modelación se realizará en consideración de los requerimientos o recomendaciones de la “Guía

para el Uso de Modelos de Calidad del Aire en el SEIA, 2023” desarrollada por el Servicio de

Evaluación Ambiental. Respecto a esto, el sistema de modelación atmosférica utilizado corresponde

al “WRF - CALPUFF”, definido por la agencia EPA como sistema de referencia para simular la

dispersión de contaminantes provenientes de instalaciones industriales ubicadas en terreno

complejo.

En cuanto a la meteorología base utilizada en la modelación, dado el sistema de seleccionado,

corresponde al modelo de retrospectiva WRF, el cual proveerá, entre otras variables, de los campos

de viento para el modelo de dispersión CALPUFF. Esta data fue validada mediante un análisis de

incertidumbre con datos meteorológicos observados en el área de estudio.

5

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

El informe se estructura de acuerdo con lo siguiente:

 - Primero, se presenta los antecedentes generales del Proyecto, que incluye una

descripción general, la localización, un cronograma de ejecución de cada una de las

fases consideradas y las emisiones resultantes estimadas en el inventario de emisiones;

 - Segundo, se presenta una caracterización del clima y la meteorología del área de

estudio, que es necesaria para la contextualización del entorno;

 - Tercero, se presenta una caracterización basas de las condiciones de la calidad del aire

del sector;

 - Cuarto, se presenta un capítulo de Modelación de Emisiones Atmosféricas, en donde:

se describe y justifica el modelo de emisiones considerado; se presentan las normas de

calidad del aire y la caracterización de la calidad del aire en el área de estudio; se detalla

la configuración del modelo y su análisis de incertidumbre; se describen los datos de

entrada al modelo, correspondiente a las fuentes de emisión, las emisiones a incorporar

en el modelo y los receptores de interés puntuales y sensibles, y; se presentan los

resultados y la evaluación de las concentraciones y depositaciones atmosféricas;

 - Quinto, se presenta un capítulo de Definición del Área de Influencia, en base a las

isocurvas de concentración y depositación, tanto para los receptores primarios como

secundarios generados por las distintas fases de ejecución proyecto, y;

 - Finalmente se presentan las conclusiones de la modelación de emisiones atmosféricas.

6

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**2** **ANTECEDENTES GENERALES DEL PROYECTO**

**2.1** Breve descripción del Proyecto

El proyecto denominado “Santa Graciela Solar” (en adelante “Proyecto”), se localiza en la comuna

de San Ignacio, provincia de Diguillín, perteneciente a la región de Ñuble.

Corresponde a un proyecto nuevo de tecnología fotovoltaica perteneciente a la categoría de Central

Solar Fotovoltaica (CSF), la cual, a través de módulos solares con celdas de Silicio Monocristalino

de 670 Wp de potencia, permitirá la captación de radiación solar para una posterior conversión en

energía eléctrica. Estos módulos se instalan sobre soportes, los cuales se emplazan sobre perfiles

de acero galvanizado, los que a su vez van fijados en el suelo, sin necesidad de contar con

fundaciones de hormigón.

El Proyecto considera un parque fotovoltaico de una potencia nominal de 80 MWac y una potencia

instalada de 93,41MWp aproximadamente, en una superficie de 109,17 ha y una Línea de

Transmisión Eléctrica de Alta Tensión (LAT) de 66 kV para inyectar el aporte energético al Sistema

Eléctrico Nacional (SEN), cuya longitud será de aproximadamente de 2,99 km, donde la LAT se

conecta desde la Subestación Eléctrica (SE) Elevadora del Proyecto de 23kV/66kV hasta la SE

Seccionadora Montenegro1.

La vida útil del Proyecto corresponde a 30 años, sin embargo, si por razones técnicas y económicas

se determina su continuidad, ésta podría extenderse mediante actividades de mantención y/o

mejoras tecnológicas, situación que será debidamente informada a los organismos sectoriales

pertinentes y cumplirá con la normativa ambiental vigente.

**2.2** **Localización**

El proyecto se encuentra emplazado aproximadamente 4 km al norte-oste del centro de la comuna

de San Ignacio y 15 km aproximadamente al sur de Chillán, provincia de Diguillín, región de Ñuble,

tal como se muestra en la siguiente figura:

7

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 1.** Ubicación del del Proyecto.

Fuente: Elaboración propia.

Mientras que, en la siguiente figura se presentan las Obras y Partes Temporales y Permanentes del

Proyecto .

8

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 2.** Obras y partes del Proyecto.

Fuente: Elaboración propia.

9

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**2.3** **Cronograma**

El Proyecto consta tres 3 fases; la fase de construcción tendrá una duración de 12 meses, la fase de

operación estimada es de 30 años y la fase de cierre durará 6 meses, tal como lo muestra la Tabla

1:

**Tabla 1.** Cronograma del Proyecto.

|Fase|Meses - Año 1|Col3|Col4|Col5|Col6|Col7|Años|Col9|Col10|Meses - Año 32|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**1 **|**2 **|**3 **|**4 **|**- **|**12**|**2-31**|**2-31**|**2-31**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|
|Construcción||||||||||||||||
|Operación||||||||||||||||
|Cierre||||||||||||||||

Fuente: Elaboración propia,2023.

10

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**3** **CARACTERIZACIÓN ZONA DE ESTUDIO**

En el presente apartado se describe el componente clima y meteorología para el área general de

emplazamiento del Proyecto, conforme a lo establecido por la Ley N°19.300, y el artículo 19 literal

e.7) del Reglamento del Sistema de Evaluación de Impacto Ambiental (D.S. N°40/2012 del Ministerio

del Medio Ambiente).

Es importante señalar que las componentes clima y meteorología son elementos del medio ambiente

que no pueden ser afectados por el Proyecto, sin embargo, su caracterización es necesaria para la

contextualización del entorno, siendo variables relevantes para realizar la evaluación del impacto

ambiental en relación con la calidad del aire.

**3.1** **Clima**

El análisis del clima se llevó a cabo mediante la revisión bibliográfica de las condiciones de la región

según la clasificación de Köppen y, adicionalmente, se clasificó el clima regional de acuerdo con la

información del documento “Climatología Regional” de la Dirección Meteorológica de Chile (2001) y

del documento “Bioclimatología de Chile” de Di Castri y Hajek (1976).

Respecto de la clasificación climática de Köppen, es posible indicar que, esta clasificación busca

otorgar una caracterización climática a nivel mundial, identificando cada tipo de clima mediante una

codificación que los distingue entre sí. Esta codificación corresponde a una clasificación empírica y

considera umbrales que establecen la distribución del clima que incide directamente en el tipo de

vegetación. La metodología de la codificación toma como referencia letras mayúsculas y minúsculas,

que denotan las principales características del clima.

Respecto de la localización del proyecto, es posible indicar que se desarrolla en la Región de ñuble,

provincia de Diguillín, comuna de San Ignacio. En esta localización, según la clasificación de Köppen

(ver Figura 3), se observa un Clima Mediterráneo de Lluvia Invernal (Csb), el cual que considera

como principal característica los inviernos fríos o templados y veranos secos y frescos. La mayor

parte de las lluvias caen en invierno o en las estaciones intermedias, alcanzando precipitaciones de

1.500 [mm/año] (según isoyeta, línea azul de la Figura 3).

La temperatura media anual es de 13,1 - 13,6oC. La mínima durante el mes de julio es de 3,03,9oC y la máxima de enero es de 27,8 - 29oC. [1], esto se puede corroborar con la isoterma (línea

roja) de la Figura 3:

1 https://www.sitrural.cl/wp-content/uploads/2020/03/SanIgnacio_rec_nat.pdf

11

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 3.** Clasificación de Köppen para el área de estudio.

Fuente: Elaboración propia.

12

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**3.2** **Meteorología**

En este apartado se presenta la caracterización de la meteorología observada para el sector de

emplazamiento del Proyecto. Esta se basó en la descripción de las variables temperatura, presión y

dirección y velocidad del viento, a partir de los registros de la estación Purén de Chillán. A

continuación, en la Tabla 2 se presenta las coordenadas de las estaciones meteorológicas, distancia

con respecto al área de proyecto más cercana y las variables monitoreadas.

**Tabla 2.** Coordenadas estaciones meteorológicas.

|Estación|Distancia con respecto al<br>área de Proyecto [km]|Coordenadas (UTM WGS84 H18)|Col4|Variables<br>meteorológicas|
|---|---|---|---|---|
|**Estación**|**Distancia con respecto al**<br>**área de Proyecto [km]**|**Este [m]**|**Norte [m]**|**Norte [m]**|
|Purén<br>(Chillán)|16|759.972|5.943.765|Velocidad del viento|
|Purén<br>(Chillán)|16|759.972|5.943.765|Dirección del viento|
|Purén<br>(Chillán)|16|759.972|5.943.765|Temperatura ambiente|

Fuente: Sistema de Información Nacional de Calidad del Aire (SINCA), 2023.

A continuación, en la Tabla 3 se presenta un resumen general de la data considerada, en la que se

presenta el porcentaje de data validada, los valores, máximos, promedio y mínimos, para el año

2022, de cada una de las variables en estudio.

**Tabla 3.** Resumen general de las variables meteorológicas consideradas.

|Variable|Año|Porcentaje data<br>válida [%]|Máximo|Promedio|Mínimo|
|---|---|---|---|---|---|
|Velocidad del viento [m/s]|2022|100%|7,74|1,87|0,01|
|Dirección del viento [°]|Dirección del viento [°]|100%|359,95|177,35|0,11|
|Temperatura [°C]|Temperatura [°C]|100%|39,41|14,27|-3,85|

Fuente: Elaboración propia, 2023.

**3.2.1** **Dirección y velocidad del viento**

La variable meteorológica viento se representa por medio de la descripción de sus componentes

vectoriales, por lo que primero se caracteriza su magnitud (velocidad) y dirección. Estos parámetros

meteorológicos tienen una influencia directa en el transporte mecánico y la concentración de los

contaminantes del aire, y su conocimiento nos permite entender la evolución diaria y anual de la

concentración media de partículas en la atmósfera.

Para la caracterización de la velocidad del viento, primero se presentan en la Figura 4,

correspondiente a una serie de tiempo horarias que permiten visualizar la distribución de la

información registrada en los años considerados, tal como se muestra a continuación:

13

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 4.** Serie de tiempo horaria - Velocidad del viento [m/s].

Fuente: Elaboración propia, 2023.

De la figura anterior, se puede indicar que el periodo de la data completa comprende desde enero

hasta diciembre del 2022. Lo anterior es posible complementarlo con la información presentada en

la Tabla 3, en donde se observa un 100% de información válida.

El análisis de esta variable es posible complementarlo con los ciclos diarios y mensuales de la

velocidad del viento, los cuales se presentan en detalle en la Figura 5 y Figura 6.

**Figura 5.** Ciclo diario de la velocidad del viento.

Fuente: Elaboración propia, 2023.

14

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 6.** Ciclo mensual de la velocidad del viento.

Fuente: Elaboración propia, 2023.

En la Figura 5 se puede observar que las velocidades del viento mayores se presentan en las horas

de la tarde, en las cuales los vientos alcanzan un promedio máximo de 2,3 [m/s] aproximadamente.

Respecto al ciclo mensual de la velocidad del viento, que se presenta en la Figura 6, se aprecia un

ciclo anual estable a través de los meses del año, en donde los vientos disminuyen ligeramente (1

[m/s]) en los meses de otoño.

Por otra parte, para caracterizar las direcciones de los vientos, a continuación, se presenta la rosa

de los vientos anuales registrado en la Estación Purén.

15

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 7.** Rosa de los vientos - Estación Purén.

Fuente: Elaboración propia, 2023.

Para la estación se observa una marcada predominancia en las direcciones Suroeste y Oeste

Suroeste, datos que abarcan un 52% del total de los registros monitoreados. Desde estas direcciones

el 5% del porcentaje de tiempo (total de la data) presentan una intensidad que va entre los 3 a los

7,74 [m/s], mientras que el 47% restante presenta velocidades inferiores a 3 [m/s]. Además, se puede

apreciar vientos desde Noreste, registrando un 10% del total de los vientos con velocidad alta.

El resto de los registros, correspondientes a los vientos de velocidades moderadas, entre 0 y 2 [m/s],

los que se distribuyen en todas las direcciones de la roza de los vientos.

**3.2.2** **Temperatura**

La temperatura es un índice indicativo del calentamiento o enfriamiento del aire que resulta del

intercambio de calor entre la atmósfera y la tierra. Para describir la temperatura generalmente

interesan los valores promedio y sus oscilaciones, es decir, por un lado, se determina cual es la

temperatura media de una zona durante un margen de tiempo determinado (diario, mensual,

16

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

estacional, anual, etc.) y por otro, el margen de temperaturas entre las que oscila, esto es, la

diferencia entre las temperaturas máximas y mínimas, llamada amplitud térmica.

En la Figura 8 se presenta una gráfica de series de tiempo horarias que permiten entender la

distribución de la data horaria en el tiempo monitoreado.

**Figura 8.** Serie de tiempo horaria - Temperatura [°C].

Fuente: Elaboración propia, 2023.

De la figura anterior, se puede indicar que el periodo de la data completa comprende desde enero

hasta diciembre del 2022. Lo anterior es posible complementarlo con la información presentada en

la Tabla 3, en donde se observa un 100% de información válida.

El análisis de esta variable es posible complementarlo con los ciclos diarios y mensuales de la

temperatura, los cuales se presentan en detalle en la Figura 9 y Figura 10.

**Figura 9.** Ciclo diario de la temperatura.

Fuente: Elaboración propia, 2023.

17

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 10.** Ciclo mensual de la temperatura.

Fuente: Elaboración propia, 2023.

Respecto de las figuras presentadas anteriormente, es posible indicar que, los meses más cálidos

corresponden a los meses de verano, mientras que las temperaturas más altas se presentan en las

horas de la tarde, alcanzando el _peak_ cerca de las 16 horas, donde se presenta una mayor incidencia

del sol.

**3.3** **Calidad del aire**

La caracterización de la Calidad del Aire se desarrolla con la finalidad de analizar y describir los

niveles basales de concentración de contaminantes en los receptores de interés asociados a las

partes, acciones y obras físicas del Proyecto.

Para elaborar esta caracterización, se consideraron los principales parámetros o contaminantes

vinculados a las fuentes de emisión de este tipo de proyectos, en los cuales se generan emisiones

de material particulado acotadas al proceso de construcción y operación, particularmente debido al

movimiento de material y al tránsito por caminos no pavimentados. Dado esto se consideró

desarrollar una caracterización ambiental de la calidad de los contaminantes MP 10 y MP 2,5 .

La estación utilizada corresponde a Purén, cuya data fue extraída en el Sistema de Información

Nacional de Calidad del Aire (SINCA). En la siguiente tabla se muestra las coordenadas y porcentaje

de data válida con el que contó el periodo de monitoreo año 2022.

18

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Tabla 4.** Coordenadas y porcentaje de data válida - Estación Purén.

|Estación|Contaminante|Data valida|Coordenadas (UTM - Datum WGS84 - H18)|Col5|
|---|---|---|---|---|
|**Estación**|**Contaminante**|**Data valida**|**Este [m]**|**Norte [m]**|
|Purén|MP10|99%|759.972|5.943.765|
|Purén|MP2,5|99%|99%|99%|

Fuente: Sistema de Información Nacional de Calidad del Aire (SINCA), 2023.

**3.3.1** **Material Particulado MP** **10**

A continuación, se presentan la serie de tiempo diaria del MP 10 con su respectiva normativa asociada:

**Figura 11.** Serie de tiempo diaria MP 10 [ug/m3] - Estación Purén.

Fuente: Elaboración propia, 2023.

De la figura anterior, se puede indicar que el periodo de la data comprende desde enero hasta

diciembre del 2022, con un 99% de información valida, tal como se muestra en la Tabla 4.

<!-- INICIO TABLA 4. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PROYECTO “SANTA GRACIELA SOLAR” DOÑA GRACIELA SOLAR SPA” -->

**Tabla 4.: ** Coordenadas y porcentaje de data válida - Estación Purén.**

| Estación | Contaminante | Data valida | Coordenadas (UTM - Datum WGS84 - H18) | Col5 |
| --- | --- | --- | --- | --- |
| **Estación** | **Contaminante** | **Data valida** | **Este [m]** | **Norte [m]** |
| Purén | MP10 | 99% | 759.972 | 5.943.765 |
| Purén | MP2,5 | 99% | 99% | 99% |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Sistema de Información Nacional de Calidad del Aire (SINCA), 2023. **3.3.1** **Material Particulado MP** **10** -->
<!-- FIN TABLA 4. -->


En la Tabla 5 se entrega la caracterización de este contaminante respecto de la normativa de calidad

primaria.

**Tabla 5.** Caracterización ambiental de la calidad del aire - Material Particulado MP 10 .

|Contaminante|Estadístico|Concentración<br>[ug/m3]|Evaluación normativa|Col5|
|---|---|---|---|---|
|**Contaminante**|**Estadístico**|**Concentración**<br>**[ug/m3]**|**Norma**|**% de la norma**|
|MP10|Promedio Anual|39|50|78%|
|MP10|Percentil 98 - Diario|121|130|93%|

Fuente: Elaboración propia, 2023.

Considerando los antecedentes expuestos en la tabla anterior, que detalla la calidad del aire basal

de sector, es posible indicar que para el material particulado MP 10 percentil 98 diario se encuentra

en situación de latencia (sobre el 80%).

19

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**3.3.2** **Material Particulado MP** **2.5**

A continuación, se presentan la serie de tiempo diaria del MP 2.5 con su respectiva normativa
asociada:

**Figura 12.** Serie de tiempo diaria MP 2.5 [ug/m3] - Estación Purén.

Fuente: Elaboración propia, 2023.

De la figura anterior, se puede indicar que el periodo de la data comprende desde enero hasta

diciembre del 2022, con un 99% de información valida, tal como se muestra en la Tabla 4.

En la Tabla 6 se entrega la caracterización de este contaminante respecto de la normativa de calidad

primaria.

**Tabla 6.** Caracterización ambiental de la calidad del aire - Material Particulado MP 2.5 .

|Contaminante|Estadístico|Concentración<br>[ug/m3]|Evaluación normativa|Col5|
|---|---|---|---|---|
|**Contaminante**|**Estadístico**|**Concentración**<br>**[ug/m3]**|**Norma**|**% de la norma**|
|MP2,5|Promedio Anual|2|20|11%|
|MP2,5|Percentil 98 - Diario|12|50|24%|

Fuente: Elaboración propia, 2023.

Con respecto a la tabla anterior, se puede observar que los registros monitoreados están por debajo

del valor normado, no superando la normativa y tampoco alcanzando valores de latencia.

20

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**4** **DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO Y LOS CONTAMINANTES**

**CONSIDERADOS**

En este apartado se presenta la modelación atmosférica de emisiones del Proyecto “Santa Graciela

Solar”, con la cual se busca determinar el impacto atmosférico asociado a la ejecución del Proyecto,

por medio de la cuantificación de las concentraciones/depositaciones resultantes en el área de

estudio y los receptores de interés.

La presente modelación es representativa para todas las fases de la ejecución Proyecto, tanto como

para la construcción, operación, y cierre, dado que se considera la modelación del escenario más

desfavorable de generación de emisiones atmosféricas, en donde se integra la fase de construcción

y la fase de operación, año 1 del Proyecto.

Dada las características intrínsecas del proyecto, asociadas a la construcción, operación y cierre de

un Parque Fotovoltaico, los contaminantes considerados en esta modelación de emisiones

corresponden al material particulado en sus distintas fracciones (MPS, MP10 y MP2,5) y los

siguientes gases: dióxido de nitrógeno (NO2), dióxido de azufre (SO2) y monóxido de carbono (CO),

todos los que fueron estimados en base a los niveles de actividad del Proyecto, presentados en el

Anexo 2.1: Estimación de emisiones atmosféricas adjunto a la DIA.

Cabe destacar que, la modelación es realizada en consideración de los requerimientos o

recomendaciones de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA, 2023”

desarrollada por el Servicio de Evaluación Ambiental. Dado lo anterior, el sistema de modelación

utilizado corresponde a la integración “WRF - CALPUFF”, definido por la agencia EPA como un

sistema de referencia para simular la dispersión de contaminantes provenientes de instalaciones

industriales ubicadas en terreno complejo.

**4.1** **Justificación del modelo seleccionado**

La metodología utilizada para evaluar el impacto de las emisiones en el área de estudio corresponde

al sistema integrado “WRF-CALPUFF”. La elección de este tipo de sistema se basa en las

recomendaciones dadas en el punto 4.2 de la “Guía para el uso de modelos de calidad del aire en el

SEIA” (2012), dado que las emisiones a considerar corresponden a emisiones de tipo primarias,

provenientes desde una fuente de emisión, en una superficie, o dominio de modelación, de más de

5 kilómetros, entre fuentes y receptores.

El sistema de modelación, tal como su nombre lo indica, incluye dos componentes principales: WRF

y CALPUFF, además de una larga selección de preprocesadores, diseñados para incluir en el

modelo datos geofísicos y de usos de suelos, y postprocesadores como por ejemplo CALPOST, que

21

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

permiten convertir los resultados a los estadísticos considerados por las normas primarias y

secundarias de calidad del aire.

En cuanto a la meteorología base utilizada en la modelación, se desarrolló un modelo de

retrospectiva (Hindcast) **WRF** (Weather Research and Forecasting, por sus siglas en ingles), el cual

provee los datos de entrada que simulan la meteorología de un año pasado y permiten modelar la

dispersión de las emisiones en la atmosfera mediante el software CALPUFF. En cuanto a esto, cabe

destacar que, el modelo cumple con las recomendaciones de configuración definidas por el Servicio

de Evaluación Ambiental, particularmente respecto de los documentos “Configuración WRF” y

“Namelist.input”.

El WRF es el modelo meteorológico recomendado por él Servicio de evaluación Ambiental de Chile,

para la generación de meteorología para estudios de calidad del aire. Lo anterior dado que, además

de sus avanzadas características, se ha ocupado en la mayoría de los Proyectos relacionados con

modelación atmosférica en cargados por organismos estatales de Chile, por lo que existe una vasta

experiencia de su aplicación en el País.

Por otra parte, **CALPUFF** es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario capaz de

modelar el transporte y dispersión de contaminantes. Los modelos tipo “puff” representan una pluma

de contaminantes continua como un número discreto de paquetes de material contaminante, tal

como se muestra la siguiente figura:

**Figura 13.** Representación gráfica del modelo tipo Puff y de Pluma.

Fuente: Elaboración Propia.

22

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

El modelo evalúa la contribución de un “puff” en la concentración atmosférica de un punto de la grilla

en un instante determinado, para luego permitir que el “puff” se mueva, evolucione en tamaño, fuerza,

etc., hasta la próxima iteración, en el próximo punto de la grilla, respondiendo a la meteorología del

sector en la que se encuentre inmerso el “puff” en cada instante. Luego, la concentración total en un

receptor resultará de la sumatoria de las contribuciones de todos los “puff”. La ecuación básica del

modelo se muestra a continuación:

Q
C=
2πσ x σ y

2 )]

a2 /(2σ x

2

c /(2σ y

2

g exp[−d a

2
)] exp[−d c

2
g=
(2π) [1/2] σ z

∞

e + 2nh) [2] /(2σ z2 )]
∑exp[−(H

n=−∞

Dónde:

 - C: Concentración [g/m3];

 - Q: Masa del contaminante en el “puff” [g];

 - σx: Coeficiente de dispersión en dirección del viento [m];

 - σy: Coeficiente de dispersión en dirección perpendicular al viento [m];

 - σz: Coeficiente de dispersión vertical [m];

 - da: Distancia desde el centro del “puff” hacia el receptor en el eje de la dirección del viento

[m];

 - dc: Distancia desde el centro del “puff” hacia el receptor en el eje perpendicular a la dirección

del viento [m];

 - g: Altura de la ecuación gaussiana [m];

 - H: Altura efectiva del “puff” [m], y;

 - h: Altura de la capa de mezcla [m].

Para casos que involucran un alto grado de variabilidad espacial del flujo dentro de la capa límite,

tales como flujos ascendentes o descendentes o flujos a lo largo de un valle fluvial sinuoso, la

suposición de estado estacionario en línea recta puede ser poco válida incluso a algunos kilómetros

de la fuente, por lo que un modelo de puff puede ser el más apropiado.

Un modelo de tipo “puff” libera emisiones independientes de la fuente, a diferencia del modelo de

pluma, permitiendo que la bocanada responda a la meteorología que la rodea. Esto también permite

rastreos a través de múltiples períodos de muestreo hasta que se haya diluido completamente o se

haya rastreado en todo el dominio de modelado, tal como se observa en Figura 14:

23

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 14.** Dispersión de la pluma a diferentes horas.

Fuente: Elaboración Propia.

**4.2** **Justificación de los contaminantes por modelar**

Tal como está detallado en el inventario de emisiones, el Proyecto generará emisiones primarias,

directas desde sus fuentes, de los contaminantes SO 2, NH 3, NO 2, CO, HC/COVs, MPS, MP 10 y MP 2,5,

propias de las actividades correspondientes al proyecto, asociadas principalmente a movimientos de

tierra, a la combustión en los motores de las maquinarias y a las generadas por el tránsito de

vehículos, dada la resuspención y la combustión.

Por otra parte, se encuentran los contaminantes secundarios, que corresponden a los contaminantes

que no se emite directamente de las fuentes emisoras, sino que, se produce por la reacción de

contaminantes primarios (emitidos directamente por la fuente emisora) con contaminantes

precursores que se encuentran en la atmósfera.

Uno de los principales contaminantes secundarios corresponde al Ozono (O 3 ), el cual necesita como

precursores NO X (NO + NO 2 ) y Compuestos Orgánicos Volátiles (COV) para su formación. En la

siguiente figura se presenta un esquema resumido de las reacciones involucradas en la conversión

de NO a NO 2 y formación de Ozono (O 3 ). El ciclo A, corresponde al ciclo NO-NO 2 -O 3 en ausencia de

COV, mientras que en el ciclo B se presenta el ciclo A con presencia de COV, siendo hv la radiación

solar necesaria para llevar a cabo la reacción. Las reacciones para la formación de ozono como

contaminante secundario son analizadas en detalle en el Anexo 2 de la “Guía para el uso de modelos

de calidad del aire en el SEIA”.

24

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 15.** Ciclos de formación de ozono.

Fuente: Elaboración Propia.

Así también, otros contaminantes atmosféricos que poseen origen secundario son los nitratos y

sulfatos que corresponden partículas sólidas (material particulado) cuyos precursores son los óxidos

de nitrógeno (NO X ) y óxidos de azufre (SO X ). En la siguiente figura se presenta el esquema de

oxidación para la formación de material particulado secundario (sulfatos y nitratos).

**Figura 16.** Esquema de oxidación SO x y NO x .

Fuente: Elaboración propia.

Respecto de los contaminantes secundarios como el Ozono, de acuerdo con lo indicado en el punto

4.2.c de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, para su modelación se

25

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

requiere de la aplicación de complejos modelos fotoquímicos del tipo WRFChem, CAMx o CMAQ

cuyo uso debe analizarse caso a caso, considerando la magnitud del Proyecto y sus impactos

ambientales potenciales.

En base a lo presentado en los párrafos anteriores:

1) En virtud de la magnitud de las emisiones de óxidos de nitrógeno (NO X ) y compuestos

orgánicos volátiles (COV) que genera el Proyecto, la condición de NO saturación del

contaminante Ozono en la zona de estudio, según lo indicado en la “Guía para el Uso

de Modelos de Calidad del Aire en el SEIA”, el presente Proyecto no cumple con las

características para generar un potencial impacto por formación de Ozono, por lo que no

requiere de una modelación de este contaminante secundario;

2) Se considera una modelación tipo PUFF de contaminantes primarios con una

transformación RIVAD, que permite considerar la formación de material particulado

desde los nitratos y sulfatos;

3) Por lo que, los contaminantes considerados para la modelación, en base a las

características del Proyecto, corresponden a SO 2, NO 2, CO, MPS, MP 10 (primarios y

secundarios por nitratos y sulfatos) y MP 2,5 (primarios y secundarios por nitratos y

sulfatos).

En base a lo anterior, en el siguiente apartado se detalla la norma de calidad del aire de los

contaminantes considerados.

**4.3** **Norma de calidad del aire**

Para realizar la evaluación de los aportes de concentraciones sobre la calidad del aire monitoreado

en la zona se ha considerado la normativa ambiental primaria de calidad de aire vigente para, MP 10,

MP 2,5, NO 2, SO 2 y CO, presentada en la Tabla 7 y norma secundaria presentada en la Tabla 8:

**Tabla 7.** Norma primaria de calidad del aire.

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**MP10 **|D.S. N°12/2021<br>del MMS|Promedio aritmético de tres años calendario consecutivos.|50 μg/m3|
|**MP10 **|D.S. N°12/2021<br>del MMS|Percentil 98 de las concentraciones de 24 horas registradas<br>durante un período anual.|130<br>μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Promedio trianual de las concentraciones anuales.|20 μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Percentil 98 de los promedios diarios registrados durante un<br>año.|50 μg/m3|
|**NO2 **||Promedio aritmético de los valores de concentración anual<br>de tres años calendarios sucesivos.|100<br>μg/m3|

26

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
||D.S. N°<br>114/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99<br>de los máximos diarios de concentración de 1 hora<br>registrados durante un año calendario.|400<br>μg/m3|
|**SO2 **|D.S. N°<br>104/2019 del<br>MMA|Promedio aritmético de tres años sucesivos del percentil 99<br>de las concentraciones de 24 horas registradas durante un<br>año calendario.|150<br>μg/m3|
|**SO2 **|D.S. N°<br>104/2019 del<br>MMA|Promedio aritmético de los valores de concentración anual<br>tres años calendario sucesivos.|60 μg/m3|
|**SO2 **|D.S. N°<br>104/2019 del<br>MMA|Promedio aritmético de tres años sucesivos del percentil<br>98,5 de las concentraciones horarias registradas durante un<br>año calendario.|350<br>μg/m3|
|**CO**|D.S. N°<br>115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99<br>de los máximos diarios de concentración de 1 hora<br>registrados durante un año calendario.|30<br>mg/m3|
|**CO**|D.S. N°<br>115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99<br>de los máximos diarios de concentración de 8 horas<br>(promedio móvil) registrados durante un año calendario.|10<br>mg/m3|

Fuente: Elaboración propia.

**Tabla 8.** Norma secundaria de calidad del aire para el SO 2 y norma de referencia para el MPS.

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**SO2 **|D.S. N°185/92<br>del MIN. DE<br>MINERÍA,<br>modificado por<br>D.S N° 22/09 del<br>MINSEGPRES|Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,73 de la concentración máxima de horaria.|700<br>μg/m3|
|**SO2 **|D.S. N°185/92<br>del MIN. DE<br>MINERÍA,<br>modificado por<br>D.S N° 22/09 del<br>MINSEGPRES|Promedio aritmético anual.|60 μg/m3|
|**SO2 **|D.S. N°185/92<br>del MIN. DE<br>MINERÍA,<br>modificado por<br>D.S N° 22/09 del<br>MINSEGPRES|Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,7 de las concentraciones diarias.|260<br>μg/m3|
|**MPS**|Norma de<br>Referencia<br>Cuenca del Río<br>Huasco|Promedio aritmético mensual.|150<br>mg/m2día|
|**MPS**|Norma de<br>Referencia<br>Cuenca del Río<br>Huasco|Promedio aritmético anual.|100<br>mg/m2día|

Fuente: Elaboración propia.

**4.4** **Análisis de incertidumbre**

La modelación de la atmósfera está basada en uno de los mejores modelos meteorológicos

disponibles en la actualidad, correspondiente al WRF, el cual cuenta con un gran número de

parametrizaciones, las cuales, si son adecuadamente seleccionadas e implementadas, simulan de

muy buena manera gran parte de los procesos meteorológicos de meso-escala.

Cabe señalar que, independiente de las bondades del modelo utilizado, todo resultado obtenido

desde un modelo atmosférico requiere ser sometido a un proceso de validación, el que debe

desarrollarse para la condición meteorológica y de terreno descrita para el área a modelar. Este

proceso permite la detección de posibles inexactitudes en los datos modelados a partir de la

información meteorológica obtenida, dado que una mala implementación de alguna parametrización

puede llevar a errores significativos en la estimación de los vientos en superficie y, con esto, de las

27

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

trayectorias de los contaminantes atmosféricos por modelar, siendo así, de esta manera

subestimadas o sobreestimadas las concentraciones de los contaminantes modelados.

Para realizar el análisis de incertidumbre se consideran las recomendaciones establecidas en la Guía

de modelación, donde, en su acápite 7, se menciona que cualquier modelo representa una

aproximación a la realidad y sus resultados tienen incertidumbres asociadas, las cuales se expresan

a través de diferencias entre lo estimado y lo observado.

El proceso consiste en evaluar las variables meteorológicas de mayor incidencia en el transporte de

contaminantes, mediante métodos cualitativos, cuantitativos y mediante técnicas estadísticas. En

base a lo anterior, a continuación, se presenta el análisis de incertidumbre en donde:

 - Primero, se realiza un análisis cualitativo en base a las figuras de series de tiempo, ciclos

diarios y ciclos anuales, de las variables dirección, velocidad del viento y temperatura, para

los datos observados y modelados;

 - Segundo, se presenta un análisis cuantitativo estadístico, y finalmente;

 - Tercero, se presenta conclusiones respecto de los datos observados y del análisis de

incertidumbre.

La estación considerada para el análisis corresponde a la que se presenta en la Tabla 9, en donde

se indican los parámetros monitoreados y se detallan las coordenadas geográficas de sus

localizaciones. Cabe destacar que la data modelada (modelo meteorológico WRF), utilizada para el

análisis de incertidumbre, se obtuvo de estos mismos puntos monitoreados.

**Tabla 9.** Parámetros meteorológicos utilizados en el análisis de incertidumbre.

|Estación|Coordenadas (UTM - Datum WGS84 - H18)|Col3|Variables meteorológicas|
|---|---|---|---|
|**Estación**|**Este [m]**|**Norte [m]**|**Norte [m]**|
|Puren|759.972|5.943.765|Velocidad y dirección del viento|
|Puren|759.972|5.943.765|Temperatura ambiente|

Fuente: Sistema de Información Nacional de Calidad del Aire (SINCA), 2023.

Adicionalmente, cabe destacar que, de acuerdo con los requerimientos del Servicio de Evaluación

Ambiental (SEA) en su “Guía para el uso de modelos de calidad del aire en el SEIA” (2012), las

estaciones de monitoreo cumplen con el porcentaje mínimo de datos válidos de las variables

meteorológicas, correspondiente a un mínimo de 75% de los registros.

Respecto a los datos meteorológicos obtenidos del modelo WRF, es importante destacar que, estos

también corresponden a datos del año 2022.

28

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**4.4.1** **Análisis cualitativo**

A continuación, se detalla una comparación cualitativa de las variables dirección del viento, velocidad

del viento y temperatura, en sus ciclos diarios y mensuales, entre los registros de las estaciones de

monitoreo (datos observados) y los registros pronosticados por el modelo meteorológico WRF (datos

modelados), para la misma localización, con el fin de evaluar la capacidad predictiva del modelo.

**4.4.1.1** **Temperatura**
A continuación, para la variable meteorológica temperatura en la Figura 17 y Figura 18 se presenta

el ciclo diario y el ciclo mensual, en donde se agregan áreas que representan el 90% de la muestra,

es decir los datos que se encuentran entre los percentiles 5 y 95.

**Figura 17.** Ciclo diario de la temperatura observada y modelada.

Fuente: Elaboración propia, 2023.

**Figura 18.** Ciclo mensual de la temperatura observada y modelada.

Fuente: Elaboración propia, 2023.

29

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

En relación con el ciclo diario y mensual de la temperatura observada y modelada, presentadas en

las figuras anteriores, es posible indicar que el modelo se adapta de muy buena forma a la realidad,

ya que además de reproducir la variación promedio a través de las horas del día, también reproduce

de buena manera el 90% de la data. Ahora bien, también es posible observar que, los valores

modelados están ligeramente subdimensionados, dado que los valores son más bajos que los

valores observados.

**4.4.1.2** **Velocidad del viento**

A continuación, para la variable meteorológica temperatura en la Figura 19 y

30

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

Figura 20 se presenta el ciclo diario y el ciclo mensual, en donde se agregan áreas que representan

el 90% de la muestra, es decir los datos que se encuentran entre los percentiles 5 y 95.

**Figura 19.** Ciclo diario de la velocidad del viento observada y modelada.

Fuente: Elaboración propia, 2023.

31

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 20.** Ciclo mensual de la velocidad del viento observada y modelada.

Fuente: Elaboración propia, 2023.

En relación con la figura anterior, respecto del ciclo diario de la velocidad del viento observada y

modelada, es posible indicar que el modelo se adapta de buena forma a la realidad, ya que logra

reproducir la variación a través de las horas del día. Ahora bien, también es posible observar que,

los valores modelados están ligeramente subdimensionados, dado que los valores son más bajos

que los valores observados.

4.4.1.3 **Dirección del viento**

A continuación, en la Figura 21 se presenta la rosa de los vientos anuales observadas y modeladas

para la estación Purén.

**Figura 21.** Rosa de los vientos observada y modelada.

32

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

Fuente: Elaboración propia, 2023.

De la figura anterior se observa que, el modelo simula claramente las tendencias de las direcciones

de los vientos en su variación anual.

**4.4.2** **Análisis cuantitativo**

A continuación, tal como lo recomienda la “Guía para el uso de modelos de Calidad del Aire en el

SEIA” (2023), se realiza el análisis cuantitativo de la incertidumbre del modelo en base los

estadígrafos Sesgo (BIAS), el Índice de Ajuste (IOA), el Error Bruto Medio (MGE), el Coeficiente de

Correlación (r) y el Error Medio Cuadrático (RMSE).

A continuación, se presenta la metodología considerada para el análisis cuantitativo. La metodología

de Análisis Cuantitativo de la incertidumbre de los datos meteorológicos modelados frente a los

observados se desarrolla por medio de la comparación de diversos parámetros estadísticos

estimados, que surgen de la comparación de la data observada con la modelada, frente a rangos de

aceptabilidad. Complementariamente, en caso de que estos rangos de aceptabilidad sean superados

se establece un factor de corrección (FC), el cual permite suplir, en cierta medida, la inexactitud del

modelo meteorológico.

 - **Sesgo (BIAS)**

Proporciona información sobre la tendencia del modelo WRF a sobreestimar o subestimar las

condiciones reales de una variable, cuantificando el error sistemático del modelo. Los resultados a

obtener se comparan con respecto a si son negativos o positivos, en el primer caso se interpreta

como que el modelo subestima el valor de las variables modeladas y viceversa. La fórmula para el

cálculo del sesgo es la siguiente:

33

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

N

BIAS= ∑ [(Mi−Oi)] N

i=1

Dónde:

`o` BIAS: Sesgo (unidad de la variable evaluada);

`o` N: Tamaño de la Muestra;

`o` M: Valor Modelado, y;

`o` O: Valor Observado.

 **Índice de Ajuste (IOA)**

Aporta información sobre el comportamiento del modelo al comparar estadísticamente los valores

observados, con los valores modelados. Este corresponde a un estadístico robusto, ya que

integra los errores cuadráticos medios y absolutos:

EOA= 1 −

∑ Ni=1 (M i −O i ) [2]
∑ Ni=1 (|M i −O mean | + |O i −O mean |) [2]

Dónde:

`o` IOA: Índice de ajuste (adimensional);

`o` N: Número de datos;

`o` Mi: Valor modelado;

`o` Oi: Valor observado, y;

`o` Omean: Valor observado promedio.

 - **Error bruto medio (MGE)**

El error bruto medio proporciona una buena estimación del error medio, independientemente de

si es una sobrestimación o una subestimación de los datos modelados frente a los datos

observados. El error bruto medio está en las mismas unidades que las cantidades consideradas:

N

MGE= [1]

N [ ∑|Mi−Oi|]

i=1

Dónde:

`o` MGE: Error bruto medio;

`o` N: Tamaño de la Muestra;

34

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

`o` M: Valor Modelado, y;

`o` O: Valor Observado.

 - **Coeficiente de Correlación (r)**

A partir de este coeficiente se mide la relación lineal entre la variable modelada y la variable

observada. El resultado de este coeficiente se encuentra en el intervalo [-1, 1]. El resultado ideal

es 1, considerando este como la mejor capacidad del modelo para representar las condiciones

generadas. La fórmula para el cálculo del error cuadrático medio es la siguiente:

N

[1] ̅̅̅̅(Oi−Oi̅̅̅)

N [ ∑(Mi−M)] σ M σ O

r= [1]

i=1

Dónde:

`o` r: Coeficiente de Correlación;

`o` N: Tamaño de la Muestra;

`o` M: Valor Modelado;

`o` O: Valor Observado, y;

`o` σ: Desviación Estándar.

 - **Error Cuadrático Medio**

Este valor entre la diferencia promedio entre los valores promedios modelados y observados. La

fórmula para el cálculo del error cuadrático medio es la siguiente:

N

N

i=1

RMSE= √∑ [(Mi−Oi)] [2]

N

N

i=1

Dónde:

`o` RMSE: Error Cuadrático Medio;

`o` N: Tamaño de la Muestra;

`o` M: Valor Modelado;

`o` O: Valor Observado.

35

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

Estos parámetros estadísticos son comparados con algunos rangos de aceptabilidad establecidos

referencialmente por la EPA. Al respecto, cabe destacar que, técnicamente no existen criterios

desempeño o rangos de aceptabilidad de las variables estadísticas para el análisis de incertidumbre

de los modelos meteorológicos de pronóstico, pero la EPA, en sus estudios, ha intentado formular

un conjunto de puntos de referencia de evaluación de modelos de mesoescala basados en la

literatura de evaluación de desempeño de MM5 [2] . En el documento (nota al pie) establece que el

propósito de estos puntos de referencia (o rangos de aceptabilidad) no es asignar una calificación

de aprobado o reprobado a una aplicación de modelo meteorológico en particular, sino más bien

poner sus resultados en un contexto útil. Por lo tanto, la idoneidad y adecuación de los puntos de

referencia deben considerarse cuidadosamente en función de los resultados de la aplicación

específica del modelo meteorológico que se esté examinando.

Los puntos de referencia o rangos de aceptabilidad, de cada uno de los estadígrafos considerados,

para el análisis de las variables meteorológicas modeladas frente a las observadas corresponden a

las siguientes:

**Tabla 10.** Referencias de aceptabilidad para los estadígrafos de cada una de variables

meteorológicas.

|Estación|BIAS|IOA|MGE|RMSE|r|
|---|---|---|---|---|---|
|Velocidad del Viento|≤ ±0,5 [m/s]|≥ 0,60|-|≤ 2 [m/s]|1|
|Dirección del Viento|≤ ±10 [°]|≥ 0,60|≤ 30 [°]|-|1|
|Temperatura|≤ ±0,5 [°]|≥ 0,80|≤ 2 [°]|-|1|

Fuente: Elaboración propia en base a documento [2] .

En base a lo presentado anteriormente, en la Tabla 11 se presentan los resultados de los parámetros

estadísticos utilizados para comparar los datos modelados con los datos observados del modelo

WRF para el área de estudio, para las variables de viento y temperatura en la estación analizada.

En ella se destaca con color verde los parámetros estadísticos que se cumplen a cabalidad los

parámetros estadísticos y se dejan con rojo los parámetros estadísticos que superan la referencia

de aceptabilidad óptima, independiente de su magnitud de superación:

**Tabla 11.** Análisis cuantitativo de la comparación de la data observada y modelada [3] .

|Variable|BIAS|IOA|MGE|RMSE|r|
|---|---|---|---|---|---|
|Velocidad del viento|0,16|0,57|0,77|1,02|0,75|

2 Operational Evaluation Of The MM5 Meteorological Model Over The Continental United States. Prepared for:
Mr. Pat Dolwick, Office of Air Quality Planning and Standards, U.S. Environmental Protection Agency.

3 La aceptabilidad de los resultados de los parámetros se presenta según su coloración. Verde: aceptabilidad
óptima; Amarillo: aceptabilidad media; Rojo: no cumplen y Negro: no tienen valor de referencia para comparar.

36

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

|Variable|BIAS|IOA|MGE|RMSE|r|
|---|---|---|---|---|---|
|Dirección del viento|6,36|0,69|47,43|88,04|0,53|
|Temperatura|-2,47|0,75|2,92|3,68|0,95|

Fuente: Elaboración propia, 2023.

En base a estos parámetros obtenidos, es posible indicar que el modelo se adapta de mejor manera

para las variables velocidad del viento y temperatura, pero presenta una menor precisión en la

componente meteorológica dirección del viento.

**5** **CONFIGURACIÓN DEL MODELO**

En esta sección se presenta las principales definiciones que permiten configuración el modelo, las

cuales permiten obtener los resultados de concentraciones y depositaciones en el área de estudio,

así también se caracteriza el domino seleccionado, por lo que, a continuación, se presenta:

 - Una caracterización del dominio de modelación

 - Un detalle de la configuración Calpuff

 - Un detalle de las características del modelo WRF

**5.1** **Dominio de modelación**

El dominio de modelación se compone de dos tipos de dominios, el meteorológico y el

computacional: El dominio meteorológico comprende un área de 50 km x 50 km, correspondiente a

la grilla del WRF ocupado, mientras que; la grilla de modelación ( _sampling grid_ ) comprende un área

de 31 km x 41km, que correspondiente a un área seleccionada para modelar, donde se ubican las

partes, obras y acciones del Proyecto, tal como se muestra en la

37

Figura 22 .

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

38

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 22.** Dominio de modelación.

Fuente: Elaboración Propia.

39

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**5.2** **Configuración del modelo**

El detalle de la configuración del modelo de dispersión de contaminantes se encuentra disponible en

el archivo denominado CALPUFF.INP (Apéndice), el cual corresponde a un archivo de texto que

permite ver las características o configuraciones de la modelación realizada. El archivo se estructura

de acuerdo con lo que se presenta en la siguiente tabla:

**Tabla 12:** Descripción del archivo *.INP.

|ID|Descripción|
|---|---|
|*|Nombre de la modelación realizada.|
|0|Nombre de archivos de entrada y salida de la modelación.|
|1|Parámetros de control generales de la corrida: Fecha y hora de inicio, duración de la ejecución,<br>frecuencia temporal. Número de contaminantes. Configuración de reinicio para realizar una serie<br>de ejecuciones de continuación. Formato de datos meteorológicos y ajuste de tiempo promedio.|
|2|Opciones Técnicas. Variables de control que determinan los métodos para el tratamiento de la<br>química, deposición húmeda, depositación seca, dispersión, aumento de pluma, terreno.|
|3 a,b|Listado de especies. Nombres de especies, especies habilitadas, emitidas y depositadas en<br>seco.|
|4|Parámetros de control de cuadrícula. Especificación de cuadrículas meteorológicas,<br>computacionales y de muestreo, número de celdas, capas verticales y coordenadas de<br>referencia.|
|5|Opciones de salida. Variables de control de impresión, variables de control de salida del disco.|
|6a, b,<br>c|Configuración del terreno complejo a escala de subcuadrícula (CTSG). Información que describe<br>la ubicación, la forma y la altura de la colina a escala de subcuadrícula. Ubicaciones y altitud de<br>receptores.|
|7|Parámetros de deposición seca- Gases. Difusividad de contaminantes, constante de disociación,<br>reactividad, resistencia al mesófilo, coeficiente de la ley de Henry.|
|8|Parámetros de deposición seca - Partículas. Diámetro medio de masa geométrica.|
|9|Parámetros misceláneos de deposición seca. Resistencias de la cutícula y del suelo de<br>referencia, reactividad del contaminante de referencia, estado de la vegetación.|
|10|Parámetros de deposición húmeda. Coeficientes de barrido para cada contaminante y tipo de<br>precipitación (precipitación líquida y congelada).|
|11|Parámetros Químicos. Variables de control para la entrada de datos de ozono, concentraciones<br>de fondo de ozono y amoníaco, tasas de transformación nocturna.|
|12|Varios parámetros de dispersión y parámetros computacionales. Constantes de dispersión<br>vertical, tasa de dispersión por encima de la capa límite, distancia de cruce a coeficientes de<br>dispersión dependientes del tiempo, uso del suelo asociado con la dispersión urbana, controles<br>de división de bocanadas, coeficientes de trayectoria de la pluma, ley de potencia de la velocidad<br>del viento, gradientes de temperatura y otros.|

40

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

|ID|Descripción|
|---|---|
|13a,b,<br>c|Parámetros de fuente puntual. Datos de fuentes puntuales, incluida la ubicación de la fuente, la<br>elevación, los parámetros de la chimenea, las emisiones, las unidades, las dimensiones del<br>edificio, el ciclo de emisiones.|
|14a,b,<br>c|Parámetros de fuente de área. Datos de la fuente del área, incluida la ubicación de la fuente, la<br>altura efectiva, la elevación, las sigmas iniciales, las emisiones, las unidades, el ciclo de<br>emisiones variables.|
|15a,b,<br>c|Parámetros de fuente lineal. Datos de la fuente como la ubicación de la fuente, la elevación, la<br>longitud de la línea, los parámetros de flotabilidad, la altura de liberación, las emisiones, las<br>unidades, el ciclo de emisiones.|
|16a,b,<br>c|Parámetros de fuente de volumen. Datos de la fuente de volumen, incluida la ubicación de la<br>fuente, la elevación, la altura efectiva, los datos de tamaño inicial, las emisiones, las unidades, el<br>ciclo de emisiones.|
|17a,b,|Información del receptor sin cuadrícula (discreta). Coordenadas del receptor y elevación del<br>suelo.|

Fuente: Elaboración Propia.

**5.3** **Meteorología**

Tal como se indica previamente, la meteorología del sector se incorpora al modelo Calpuff mediante

el desarrollo de un modelo meteorológico de retrospectiva WRF. Los datos de salida, como su

localización, fecha, resolución, entre otras, se presentan a continuación:

**Tabla 13:** Detalle de modelo meteorológico WRF.

|Proyección Cartográfica|Cónica conforme de Lambert (LCC)|
|---|---|
|Período|30 Dic 2021 00:00 - 03 Ene 2023 00:00|
|Origen|R L AT 01 = 36.760S<br>RLAN0 = 72.069W<br>XLAT1= 37.000S<br>XLAT2 = 36.520S|
|Proyección|Lambert Conic Conformal|
|Datum|NWS-84 6370 km Radius, Global Sphere|
|Grilla|50 x 50 km|
|Resolución|1 x 1 km2|
|Celdas verticales|10|

Fuente: Elaboración propia.

Las variables meteorológicas que contiene el modelo para toda el área de estudio corresponden a

las siguientes:

 - Campos de viento (dirección y velocidad del viento)

 - Temperatura del aire [°K]

 - Clases de Estabilidad

 - Velocidad de fricción en la superficie [m/s]

41

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

 - Altura de Capa de Mezcla [m]

 - Longitud de Monin-Obukhov [m]

 - Escala de velocidad convectiva [m/s]

 - Rango de precipitación [mm/hr]

 - Temperatura de superficie [K]

 - Densidad del aire [kg/m3]

 - Radiación solar [W/m2]

 - Humedad relativa [%]

 - Uso de suelo

 - Índice de cobertura foliar

 - Rugosidad superficial

**5.4** **Topografía**

La topografía del área de estudio se ha extraído de Shuttle Radar Topography Mission, más conocido

como SRTM1, cuya resolución es aproximadamente 30 [m] x 30 [m]. El archivo SRTM1 ha sido

incorporado al modelo con el objetivo de proporcionar la altura de los puntos de interés,

correspondientes tanto a las fuentes como los receptores.

En la siguiente figura se presenta una imagen de la información utilizada:

42

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 23.** Topografía del área de estudio.

Fuente: Elaboración propia.

43

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**6** **DATOS DE ENTRADA DEL MODELO**

A continuación, se presentan los datos de entrada utilizados para la modelación de la dispersión de

contaminantes, correspondientes a fuentes de emisión y receptores de interés.

**6.1** **Fuentes de Emisión**

Las fuentes de emisión del Proyecto corresponderán principalmente a fuentes del tipo Areal lineal y

Areal, y se encuentran asociadas a las fuentes consideradas en el inventario de emisiones.

Para evaluar el escenario de emisiones más desfavorable, en el modelo se consideró las emisiones

de la fase de construcción año 1 del Proyecto, cuyas tasas de emisión, descripción, largo o área,

son presentadas en las siguientes tablas.

Las tasas de emisión fueron estimadas de acuerdo con el inventario de emisiones y determinadas

para la modelación siguiendo la siguiente fórmula:

Emisión [t]
Tasa de Emisión =
Duración [año] ∗Dimensión [m [2] ]

A continuación, se presentan las emisiones consideradas por área modelada y posteriormente se

presenta la distribución fuentes en el territorio. Además, en la Figura 24 se presentan la ubicación

de las fuentes del modelo.

44

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA””

**Tabla 14.** Caminos acceso al Proyecto.

|Tipo de fuente|ID|Descripción|Elevación<br>[m]|Superficie|Col6|Col7|Tasa de emisión [t/año-m2]|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de fuente**|**ID**|**Descripción**|**Elevación**<br>**[m]**|**Largo [m]**|**Ancho [m]**|**Área [m2]**|**MP10 **|**MP2,5 **|**MPS**|**NOx**|**CO**|**SO2 **|
|Lineal areal|SRC_1|Tramo 01|-|5195,9|5|25.980|1,82E-06|4,63E-07|1,82E-06|1,35E-06|3,22E-07|1,38E-09|
|Lineal areal|SRC_2|Tramo 02|-|3690,9|5|18.455|1,89E-06|4,80E-07|1,89E-06|1,41E-06|3,37E-07|1,44E-09|
|Lineal areal|SRC_3|Tramo 03|-|5246,8|5|26.234|2,83E-06|7,20E-07|2,83E-06|2,10E-06|5,01E-07|2,14E-09|
|Lineal areal|SRC_4|Tramo 04|-|5.215|5|26.074|2,33E-06|5,93E-07|2,33E-06|1,73E-06|4,12E-07|1,76E-09|
|Lineal areal|SRC_5|Tramo 05|-|1.378|5|6.892|2,06E-06|5,23E-07|2,06E-06|1,53E-06|3,64E-07|1,56E-09|
|Lineal areal|SRC_6|Tramo 06|-|1.557|5|7.787|1,61E-06|4,10E-07|1,61E-06|1,20E-06|2,85E-07|1,22E-09|
|Lineal areal|SRC_7|Tramo 07|-|1.198|5|5.990|3,11E-07|7,91E-08|3,11E-07|2,31E-07|5,50E-08|2,35E-10|
|Lineal areal|SRC_8|Tramo 08|- <br>|675|5|3.375|1,29E-06|3,29E-07|1,29E-06|9,59E-07|2,29E-07|9,78E-10|
|Lineal areal|SRC_9|Tramo 09|<br>|410|5|2.051|1,31E-06|3,34E-07|1,31E-06|9,74E-07|2,32E-07|9,93E-10|
|Lineal areal|SRC_10|Tramo 10|<br>|1.070|5|5.350|9,57E-07|2,44E-07|9,57E-07|7,11E-07|1,70E-07|7,24E-10|
|Lineal areal|SRC_11|Tramo 11|<br>|6.229|5|31.145|9,87E-07|2,51E-07|9,87E-07|7,33E-07|1,75E-07|7,47E-10|
|Lineal areal|SRC_12|Tramo 12|<br>|3.873|5|19.364|2,69E-07|6,85E-08|2,69E-07|2,00E-07|4,77E-08|2,04E-10|
|Lineal areal|SRC_13|Tramo 13|<br>|11.406|5|57.029|2,38E-06|6,06E-07|2,38E-06|1,77E-06|4,22E-07|1,80E-09|
|Lineal areal|SRC_14|Tramo 14|<br>|1.490|5|7.450|4,37E-07|1,11E-07|4,37E-07|3,25E-07|7,75E-08|3,31E-10|
|Lineal areal|SRC_15|Tramo 15|<br>|175|5|873|5,25E-08|1,34E-08|5,25E-08|3,90E-08|9,30E-09|3,98E-11|
|Lineal areal|SRC_16|Tramo 16|<br>|4.641|5|23.207|2,94E-07|7,49E-08|2,94E-07|2,18E-07|5,21E-08|2,23E-10|
|Lineal areal|SRC_17|Tramo 17|<br>|3.527|5|17.635|3,17E-07|8,06E-08|3,17E-07|2,35E-07|5,61E-08|2,40E-10|
|Lineal areal|SRC_18|Tramo 18|<br>|4.433|5|22.164|4,44E-05|4,45E-06|4,44E-05|1,50E-06|3,59E-07|1,53E-09|
|Lineal areal|SRC_19|Tramo 19|<br>|1.787|5|8.933|4,19E-06|4,27E-07|4,19E-06|3,93E-07|9,38E-08|4,01E-10|
|Lineal areal|SRC_20|Tramo 20|<br>|206|5|1.031|2,43E-06|2,47E-07|2,43E-06|2,28E-07|5,43E-08|2,32E-10|
|Lineal areal|SRC_21|Tramo 21|<br>|223|5|1.113|2,50E-06|2,55E-07|2,50E-06|2,35E-07|5,60E-08|2,39E-10|
|Lineal areal|SRC_22|Tramo 22|<br>|285|5|1.426|3,22E-06|3,28E-07|3,22E-06|3,05E-07|7,28E-08|3,11E-10|
|Lineal areal|SRC_23|Tramo 23|<br>|2.721|5|13.604|3,08E-08|2,23E-08|3,08E-08|8,73E-07|2,08E-07|8,90E-10|
|Lineal areal|SRC_24|Tramo 24|<br>|657|5|3.283|5,37E-06|5,47E-07|5,37E-06|5,06E-07|1,21E-07|5,16E-10|
|Lineal areal|SRC_25|Tramo 25||7.001|5|35.007|2,08E-05|2,09E-06|2,08E-05|6,89E-07|1,64E-07|7,03E-10|

45

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

|Tipo de fuente|ID|Descripción|Elevación<br>[m]|Superficie|Col6|Col7|Tasa de emisión [t/año-m2]|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de fuente**|**ID**|**Descripción**|**Elevación**<br>**[m]**<br>|**Largo [m]**|**Ancho [m]**|**Área [m2]**|**MP10 **|**MP2,5 **|**MPS**|**NOx**|**CO**|**SO2 **|
|**Tipo de fuente**|SRC_26|Tramo 26|<br>|1.175|5|5.875|3,77E-06|3,84E-07|3,77E-06|3,48E-07|8,30E-08|3,55E-10|
|**Tipo de fuente**|SRC_27|Tramo 27|<br>|2.252|5|11.259|2,73E-08|1,96E-08|2,73E-08|7,66E-07|1,83E-07|7,82E-10|
|**Tipo de fuente**|SRC_28|Tramo 28||1.018|5|5.091|1,53E-06|3,88E-07|1,53E-06|1,12E-06|2,66E-07|1,14E-09|
|Areal Poligonal|SRC_29|Área A|190,9|-|-|639.315|8,06E-07|6,77E-07|8,06E-07|8,05E-06|3,27E-06|9,23E-08|
|Areal Poligonal|SRC_30|Área B|186,3|-|-|54.847|8,06E-07|6,77E-07|8,06E-07|8,05E-06|3,27E-06|9,23E-08|
|Areal Poligonal|SRC_31|Área C|188,2|-|-|466.779|8,06E-07|6,77E-07|8,06E-07|8,05E-06|3,27E-06|9,23E-08|
|Total|Total|Total|Total|Total|Total|Total|1,12E-04|1,66E-05|1,12E-04|4,68E-05|1,52E-05|3,00E-07|

Fuente: Elaboración propia.

46

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 24.** Fuentes de emisión en el modelo

Fuente: Elaboración propia.

47

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**6.2** **Receptores**

La ubicación, descripción e ID de los receptores discretos a considerar se presenta a continuación

en la siguiente tabla, y posteriormente se presenta una figura, en donde se puede observar su

ubicación respecto de las fuentes del proyecto:

**Tabla 15.** Receptores de interés.

|ID|Descripción|Tipo de<br>receptor|Coordenadas de Ubicación|Col5|
|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de**<br>**receptor**|**(Datum WGS84 - H18)**|**(Datum WGS84 - H18)**|
|**ID**|**Descripción**|**Tipo de**<br>**receptor**|**Este [m]**|**Norte [m]**|
|R_1|Estación Purén (Chillán) - Medio<br>Humano|Primario|759.972|5.943.765|
|R_2|Mongetun Mapu (Plaza San Ignación) -<br>Medio Humano|Mongetun Mapu (Plaza San Ignación) -<br>Medio Humano|764.975|5.923.193|
|R_3|Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano|Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano|762.393|5.927.377|
|R_4|Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano|Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano|759.628|5.943.886|
|R_5|Integrante Indigena más cercano -<br>Medio Humano|Integrante Indigena más cercano -<br>Medio Humano|762.103|5.925.398|
|R_6|Producción y venta de carbón - Medio<br>Humano|Producción y venta de carbón - Medio<br>Humano|756.034|5.930.111|
|R_7|Producción y venta de carbón - Medio<br>Humano|Producción y venta de carbón - Medio<br>Humano|762.378|5.925.748|
|R_8|Producción y venta de carbón - Medio<br>Humano|Producción y venta de carbón - Medio<br>Humano|762.742|5.926.307|
|R_9|Producción y venta de carbón - Medio<br>Humano|Producción y venta de carbón - Medio<br>Humano|756.395|5.930.475|
|R_10|Producción y venta de carbón - Medio<br>Humano|Producción y venta de carbón - Medio<br>Humano|762.829|5.926.378|
|R_11|R1 (Ruido)|R1 (Ruido)|762.406|5.927.352|
|R_12|R2 (Ruido)|R2 (Ruido)|761.064|5.925.708|
|R_13|R3 (Ruido)|R3 (Ruido)|760.585|5.925.397|
|R_14|R4 (Ruido)|R4 (Ruido)|761.531|5.928.526|
|R_15|RF (Ruido)|RF (Ruido)|759.175|5.927.299|
|R_16|Frutillas|Secundario|762.469|5.931.046|
|R_17|Frutillas|Frutillas|762.458|5.931.133|
|R_18|Frutillas|Frutillas|759.842|5.924.188|
|R_19|Frutillas|Frutillas|760.204|5.924.171|
|R_20|Frutillas|Frutillas|763.309|5.926.117|
|R_21|Frutillas|Frutillas|763.393|5.926.354|
|R_22|Frutillas|Frutillas|762.883|5.927.197|
|R_23|Frutillas|Frutillas|763.081|5.927.717|
|R_24|Frutillas|Frutillas|762.823|5.929.150|
|R_25|Frutillas|Frutillas|762.854|5.929.330|
|R_26|Frutillas|Frutillas|762.449|5.929.371|
|R_27|Frutillas|Frutillas|762.504|5.929.422|
|R_28|Frutillas|Frutillas|762.708|5.929.416|

48

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

|ID|Descripción|Tipo de<br>receptor|Coordenadas de Ubicación|Col5|
|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de**<br>**receptor**<br>|**(Datum WGS84 - H18)**|**(Datum WGS84 - H18)**|
|**ID**|**Descripción**|**Tipo de**<br>**receptor**<br>|**Este [m]**|**Norte [m]**|
|R_29|Frutillas|Frutillas|762.409|5.929.622|
|R_30|Frutillas|Frutillas|762.480|5.929.680|
|R_31|Frutillas<br>|Frutillas<br>|762.554<br>|5.929.858|

Fuente: Elaboración propia.

En la Figura 25 se presenta los receptores considerados en el modelo.

**Figura 25.** Receptores del modelo - Área del Proyecto

Fuente: Elaboración propia.

49

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 26.** Receptores del modelo - Chillán

Fuente: Elaboración propia.

50

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**7** **RESULTADOS DE LA MODELACIÓN ATMOSFÉRICA**

Los resultados de la modelación atmosférica se presentan en: a) isocurvas para cada uno de los

estadísticos considerados en las normativas de calidad del aire aplicables al presente estudio; b) en

cartografías con Puntos de Máxima Concentración, y; c) finalmente se presenta un análisis respecto

a la concentración esperada en los receptores sensibles del Proyecto.

**7.1** **Isoconcentraciones**

En las siguientes figuras se muestran las distintas curvas de isoconcentración obtenidas como

resultado del modelo de dispersión CALPUFF-WRF para Material Particulado Respirable (MP 10 ),

Material Particulado Fino Respirable (MP 2,5 ), Material Particulado Sedimentado (MPS), Dióxido de

Azufre (SO 2 ) y Dióxido de Nitrógeno (NO 2 ). Cabe mencionar que estos resultados fueron adjuntados

como archivos originales en el Anexo 15,16 y 17 de Modelaciones.

51

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 27.** Curva isoconcentración - MP 10 - Norma promedio anual.

Fuente: Elaboración propia.

52

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 28.** Curva isoconcentración - MP 10 - Norma diaria (P98).

Fuente: Elaboración propia.

53

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 29.** Curva isoconcentración - MP 2,5 - Norma promedio anual.

Fuente: Elaboración propia.

54

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 30.** Curva isoconcentración - MP 2,5 - Norma diaria (P98).

Fuente: Elaboración propia.

55

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 31.** Curva isodepositación - MPS - Norma promedio anual.

Fuente: Elaboración propia.

56

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 32.** Curva isodepositación - MPS - Norma promedio mensual

Fuente: Elaboración propia.

57

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 33.** Curva isoconcentración - SO 2 - Norma promedio anual.

Fuente: Elaboración propia.

58

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 34.** Curva isoconcentración - SO 2 - Norma diaria (P99).

Fuente: Elaboración propia.

59

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 35.** Curva isoconcentración - SO 2 - Norma horaria (P98,5).

Fuente: Elaboración propia.

60

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 36.** Curva isoconcentración - SO 2 - Norma diaria secundaria (P99,7).

Fuente: Elaboración propia.

61

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 37.** Curva isoconcentración - SO 2 - Norma horaria secundaria (P99,73).

Fuente: Elaboración propia.

62

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 38.** Curva isoconcentración - NO 2 - Norma anual.

Fuente: Elaboración propia.

63

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 39.** Curva isoconcentración - NO 2 - Norma horaria (P99).

Fuente: Elaboración propia.

64

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 40.** Curva isoconcentración - CO - Norma horaria (P99).

Fuente: Elaboración propia.

65

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 41.** Curva isoconcentración - CO - Norma 8 horas (P99).

Fuente: Elaboración propia.

66

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**7.2** **Puntos de máxima concentración (PMC)**

A continuación, en la siguiente tabla, se detallan los Puntos de Máxima Concentración (PMC) del

escenario modelado, detallando el contaminante y su aporte, por estadístico. Además, se muestra

las coordenadas de cada PMC.

**Tabla 16.** Puntos de máxima concentración (PMC).

|ID|Cont.|Tipo de<br>Norma|Estadístico|PMC<br>[ug/m<br>3]|Norma<br>[ug/m3]|Unidad|%<br>Norma|Coordenadas UTM -<br>WGS84|Col10|Coordenadas<br>LCC - NWS84|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Cont.**|**Tipo de**<br>**Norma**|**Estadístico**|**PMC**<br>**[ug/m**<br>**3]**|**Norma**<br>**[ug/m3]**|**Unidad**|**% **<br>**Norma**|**Este [m]**|**Norte [m]**|**X [km]**|**Y [km]**|
|PMC1|MPS|Secundaria|Promedio del<br>Periodo|1,7|100|mg/m2-<br>día|1,67%|757.204|5.930.377|-4,50|2,50|
|PMC1|MPS|Secundaria|Promedio<br>mensual|2,7|150|150|1,83%|757.204|5.930.377|-4,50|2,50|
|PMC2|MP10|Primaria|Promedio del<br>Periodo|1,29|50|ug/m3|2,59%|762124|5927229|0,50|-0,50|
|PMC2|MP10|Primaria|Percentil 98<br>Diario|2,78|130|130|2,14%|762124|5927229|0,50|-0,50|
|PMC2|MP2,5|Primaria|Promedio del<br>Periodo|1,02|20|20|5,10%|762124|5927229|0,50|-0,50|
|PMC2|MP2,5|Primaria|Percentil 98<br>Diario|2,19|50|50|4,37%|762124|5927229|0,50|-0,50|
|PMC2|SO2|Primaria|Promedio del<br>Periodo|0,12|60|60|0,19%|762124|5927229|0,50|-0,50|
|PMC2|SO2|Primaria|Percentil 99<br>Diario|0,24|150|150|0,16%|762124|5927229|0,50|-0,50|
|PMC2|SO2|Primaria|Percentil 98,5<br>Horario|0,60|350|350|0,17%|762124|5927229|0,50|-0,50|
|PMC2|SO2|Secundaria|Promedio del<br>Periodo|0,12|60|60|0,19%|762124|5927229|0,50|-0,50|
|PMC2|SO2|Secundaria|Percentil 99,7<br>Diario|0,27|260|260|0,10%|762124|5927229|0,50|-0,50|
|PMC2|SO2|Secundaria|Percentil 99,73<br>Horario|0,80|700|700|0,11%|762124|5927229|0,50|-0,50|
|PMC2|NO2|Primaria|Promedio del<br>Periodo|10,08|100|100|10,08%|762124|5927229|0,50|-0,50|
|PMC2|NO2|Primaria|Percentil 99<br>Horario|79,40|400|400|19,85%|762124|5927229|0,50|-0,50|
|PMC2|CO|Primaria|Percentil 99 8<br>Horas|18,36|10.000|10.000|0,18%|762124|5927229|0,50|-0,50|
|PMC2|CO|Primaria|Percentil 99<br>Horario|37,19|30.000|30.000|0,12%|762124|5927229|0,50|-0,50|

Fuente: Elaboración propia.

En la siguiente Figura se presenta la ubicación de los PMC. Al respecto, se encuentran ubicados en

el Sector del Proyecto y los alrededores, zona altamente intervenida, tanto para material particulado

como gases, durante todas las fases del Proyecto.

67

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 42.** Localización puntos de máxima concentración (PMC).

Fuente: Elaboración propia.

68

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**7.3** **Aportes en receptores de interés**

A continuación, se presenta el análisis de la concentración esperada en los receptores de interés

identificados. Para ello, en la Tabla 17 y Tabla 18 se presenta los resultados obtenidos de la

modelación y en la

69

Tabla 19 y

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

70

Tabla 20 su relación con las normas señaladas.

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

71

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Tabla 17.** Aportes del Proyecto en receptores primarios.

|ID|Descripción|MP [ug/m3]<br>10|Col4|MP [ug/m3]<br>2.5|Col6|SO [ug/m3]<br>2|Col8|Col9|NO [ug/m3]<br>2|Col11|CO [ug/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|R_1|Estación Purén (Chillán) - Medio<br>Humano|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,13|0,02|0,07|
|R_2|Mongetun Mapu (Plaza San Ignación)<br>- Medio Humano|0,01|0,05|<0,01|0,02|<0,01|<0,01|<0,01|0,02|0,89|0,11|0,42|
|R_3|Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano|0,43|1,34|0,32|1,05|0,03|0,10|0,31|2,71|52,77|9,03|25,35|
|R_4|Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,00|0,14|0,02|0,07|
|R_5|Integrante indígena más cercano -<br>Medio Humano|0,05|0,25|0,03|0,17|<0,01|0,01|0,03|0,21|8,73|1,36|4,15|
|R_6|Producción y venta de carbón - Medio<br>Humano|0,07|0,26|0,01|0,04|<0,01|<0,01|<0,01|0,02|0,99|0,12|0,47|
|R_7|Producción y venta de carbón - Medio<br>Humano|0,06|0,26|0,04|0,17|<0,01|0,01|0,04|0,23|7,08|1,33|3,67|
|R_8|Producción y venta de carbón - Medio<br>Humano|0,09|0,32|0,05|0,20|<0,01|0,01|0,04|0,27|11,41|1,61|5,52|
|R_9|Producción y venta de carbón - Medio<br>Humano|0,29|0,66|0,03|0,08|<0,01|<0,01|<0,01|0,02|1,17|0,14|0,60|
|R_10|Producción y venta de carbón - Medio<br>Humano|0,09|0,32|0,05|0,20|<0,01|0,01|0,04|0,26|10,09|1,54|5,26|
|R_11|R1 (Ruido)|0,41|1,32|0,30|1,01|0,03|0,09|0,30|2,49|52,33|8,81|25,29|
|R_12|R2 (Ruido)|0,59|1,72|0,46|1,29|0,05|0,13|0,36|4,30|50,46|10,22|23,77|
|R_13|R3 (Ruido)|0,27|1,00|0,19|0,75|0,02|0,07|0,24|1,61|45,83|6,71|22,34|
|R_14|R4 (Ruido)|0,20|0,61|0,08|0,24|0,01|0,02|0,06|0,57|10,55|2,00|5,41|
|R_15|RF (Ruido)|0,12|0,37|0,02|0,11|0,00|0,01|0,02|0,09|4,90|1,03|2,41|

Fuente: Elaboración propia.

72

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Tabla 18.** Aportes del Proyecto en receptores secundarios.

|ID Modelo|Receptor|MPS [mg/m2d]|Col4|SO [ug/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID Modelo**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|R_16|Frutillas|0,01|0,02|<0,01|<0,01|0,01|
|R_17|Frutillas|0,01|0,02|<0,01|<0,01|0,01|
|R_18|Frutillas|0,29|0,37|<0,01|0,01|0,04|
|R_19|Frutillas|<0,01|<0,01|<0,01|0,01|0,04|
|R_20|Frutillas|0,01|0,01|<0,01|0,01|0,04|
|R_21|Frutillas|0,10|0,17|<0,01|0,01|0,05|
|R_22|Frutillas|0,01|0,02|0,01|0,03|0,19|
|R_23|Frutillas|0,11|0,14|<0,01|0,02|0,10|
|R_24|Frutillas|0,51|0,76|<0,01|0,01|0,04|
|R_25|Frutillas|0,11|0,15|<0,01|0,01|0,03|
|R_26|Frutillas|0,27|0,35|<0,01|0,01|0,04|
|R_27|Frutillas|0,53|0,65|<0,01|0,01|0,03|
|R_28|Frutillas|0,12|0,25|<0,01|0,01|0,03|
|R_29|Frutillas|0,12|0,13|<0,01|0,01|0,03|
|R_30|Frutillas|0,07|0,09|<0,01|0,01|0,03|
|R_31|Frutillas|0,01|0,02|<0,01|0,01|0,03|

Fuente: Elaboración propia.

73

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Tabla 19.** Relación del aporte del Proyecto con la normativa primaria vigente.

|ID|Receptor/Norma|MP [ug/m3]<br>10|Col4|MP [ug/m3]<br>2.5|Col6|SO [ug/m3]<br>2|Col8|Col9|NO [ug/m3]<br>2|Col11|CO [ug/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor/Norma**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horari**<br>**o **|
|**ID**|**Receptor/Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_1|Estación Purén (Chillán) - Medio<br>Humano|<0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|
|R_2|Mongetun Mapu (Plaza San Ignación) -<br>Medio Humano|0,02%|0,04%|0,02%|0,04%|<0,01%|<0,01%|<0,01%|0,02%|0,22%|<0,01%|<0,01%|
|R_3|Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano|0,86%|1,03%|1,59%|2,10%|0,05%|0,06%|0,09%|2,71%|13,19%|0,09%|0,08%|
|R_4|Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano|<0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,04%|<0,01%|<0,01%|
|R_5|Integrante indígena más cercano -<br>Medio Humano|0,11%|0,19%|0,17%|0,33%|<0,01%|0,01%|0,01%|0,21%|2,18%|0,01%|0,01%|
|R_6|Producción y venta de carbón - Medio<br>Humano|0,15%|0,20%|0,06%|0,08%|<0,01%|<0,01%|<0,01%|0,02%|0,25%|<0,01%|<0,01%|
|R_7|Producción y venta de carbón - Medio<br>Humano|0,12%|0,20%|0,19%|0,34%|<0,01%|0,01%|0,01%|0,23%|1,77%|0,01%|0,01%|
|R_8|Producción y venta de carbón - Medio<br>Humano|0,18%|0,25%|0,25%|0,40%|<0,01%|0,01%|0,01%|0,27%|2,85%|0,02%|0,02%|
|R_9|Producción y venta de carbón - Medio<br>Humano|0,58%|0,51%|0,16%|0,15%|<0,01%|<0,01%|<0,01%|0,02%|0,29%|<0,01%|<0,01%|
|R_10|Producción y venta de carbón - Medio<br>Humano|0,17%|0,24%|0,24%|0,40%|<0,01%|0,01%|0,01%|0,26%|2,52%|0,02%|0,02%|
|R_11|R1 (Ruido)|0,82%|1,02%|1,49%|2,03%|0,05%|0,06%|0,09%|2,49%|13,08%|0,09%|0,08%|
|R_12|R2 (Ruido)|1,17%|1,32%|2,29%|Y e|0,08%|0,09%|0,10%|4,30%|12,61%|0,10%|0,08%|
|R_13|R3 (Ruido)|0,54%|0,77%|0,97%|1,50%|0,03%|0,05%|0,07%|1,61%|11,46%|0,07%|0,07%|
|R_14|R4 (Ruido)|0,40%|0,47%|0,40%|0,48%|0,01%|0,02%|0,02%|0,57%|2,64%|0,02%|0,02%|
|R_15|RF (Ruido)|0,24%|0,28%|0,11%|0,22%|<0,01%|0,01%|0,01%|0,09%|1,22%|0,01%|0,01%|

Fuente: Elaboración propia.

74

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Tabla 20.** Relación del aporte del Proyecto con la normativa secundaria vigente.

|ID Modelo|Receptor/Norma|MPS [mg/m2d]|Col4|SO [ug/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID Modelo**|**Receptor/Norma**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**ID Modelo**|**Receptor/Norma**|**100**|**150**|**60**|**260**|**700**|
|R_16|Frutillas|0,01%|0,01%|<0,01%|<0,01%|<0,01%|
|R_17|Frutillas|0,01%|0,01%|<0,01%|<0,01%|<0,01%|
|R_18|Frutillas|0,01%|0,02%|<0,01%|<0,01%|0,01%|
|R_19|Frutillas|0,01%|0,01%|<0,01%|<0,01%|0,01%|
|R_20|Frutillas|0,09%|0,07%|<0,01%|<0,01%|0,01%|
|R_21|Frutillas|0,04%|0,04%|<0,01%|<0,01%|0,01%|
|R_22|Frutillas|0,04%|0,05%|0,01%|0,01%|0,03%|
|R_23|Frutillas|0,02%|0,02%|0,01%|0,01%|0,01%|
|R_24|Frutillas|0,02%|0,02%|<0,01%|<0,01%|0,01%|
|R_25|Frutillas|0,02%|0,02%|<0,01%|<0,01%|<0,01%|
|R_26|Frutillas|0,03%|0,03%|<0,01%|<0,01%|0,01%|
|R_27|Frutillas|0,03%|0,03%|<0,01%|<0,01%|<0,01%|
|R_28|Frutillas|0,02%|0,02%|<0,01%|<0,01%|<0,01%|
|R_29|Frutillas|0,03%|0,02%|<0,01%|<0,01%|<0,01%|
|R_30|Frutillas|0,02%|0,02%|<0,01%|<0,01%|<0,01%|
|R_31|Frutillas|0,02%|0,02%|<0,01%|<0,01%|<0,01%|

Fuente: Elaboración propia.

75

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**7.4** **Escenario Proyectado**

En la siguiente sección se presenta el escenario proyectado, el que contempla el aporte del Proyecto.

Además de los valores de Línea de Base de Calidad del aire presentado en el capítulo 3.3. Por lo

tanto y debido a que en la estación Purén sólo se monitorea MP 10, MP 2,5, el análisis se realiza para

dichos contaminantes utilizando de manera referencial los valores monitoreados para cada receptor

primario en estudio.

76

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Tabla 21.** Escenario Proyectado - Material Particulado MP 10 .

|ID|Receptor|MP Promedio anual [ug/m3]<br>10|Col4|Col5|Norma<br>[ug/m3]|%Norma|MP P98 Diario [ug/m3]<br>10|Col9|Col10|Norma<br>[ug/m3]|% Norma|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**AP**|**LB**|**AP+LB**|**AP+LB**|**AP+LB**|**AP**|**LB**|**AP+LB**|**AP+LB**|**AP+LB**|
|R_1|Estación Purén (Chillán) -<br>Medio Humano|<0,1|39,2|39,2|50|78%|<0,1|121,3|121,3|130|93%|
|R_2|Mongetun Mapu (Plaza San<br>Ignación) - Medio Humano|<0,1|<0,1|39,2|39,2|78%|0,1|0,1|121,4|121,4|93%|
|R_3|Junta de Vecinos San Bernardo<br>(ex-escuela) - Medio Humano|0,4|0,4|39,6|39,6|79%|1,3|1,3|122,7|122,7|94%|
|R_4|Comunidad Familiar Indígena<br>Flor del Canelo - Medio<br>Humano|<0,1|<0,1|39,2|39,2|78%|<0,1|<0,1|121,3|121,3|93%|
|R_5|Integrante indígena más<br>cercano - Medio Humano|0,1|0,1|39,3|39,3|79%|0,2|0,2|121,6|121,6|94%|
|R_6|Producción y venta de carbón -<br>Medio Humano|0,1|0,1|39,3|39,3|79%|0,3|0,3|121,6|121,6|94%|
|R_7|Producción y venta de carbón -<br>Medio Humano|0,1|0,1|39,3|39,3|79%|0,3|0,3|121,6|121,6|94%|
|R_8|Producción y venta de carbón -<br>Medio Humano|0,1|0,1|39,3|39,3|79%|0,3|0,3|121,7|121,7|94%|
|R_9|Producción y venta de carbón -<br>Medio Humano|0,3|0,3|39,5|39,5|79%|0,7|0,7|122,0|122,0|94%|
|R_10|Producción y venta de carbón -<br>Medio Humano|0,1|0,1|39,3|39,3|79%|0,3|0,3|121,7|121,7|94%|
|R_11|R1 (Ruido)|0,4|0,4|39,6|39,6|79%|1,3|1,3|122,7|122,7|94%|
|R_12|R2 (Ruido)|0,6|0,6|39,8|39,8|80%|1,7|1,7|123,1|123,1|95%|
|R_13|R3 (Ruido)|0,3|0,3|39,5|39,5|79%|1,0|1,0|122,3|122,3|94%|
|R_14|R4 (Ruido)|0,2|0,2|39,4|39,4|79%|0,6|0,6|121,9|121,9|94%|
|R_15|RF (Ruido)|0,1|0,1|39,3|39,3|79%|0,4|0,4|121,7|121,7|94%|

Fuente: Elaboración propia.

77

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Tabla 22.** Escenario Proyectado - Material Particulado MP 2.5 .

|ID|Descripción|MP2.5 Promedio anual [ug/m3]|Col4|Col5|Norma<br>[ug/m3]|%Norm<br>a|MP2.5 P98 Diario [ug/m3]|Col9|Col10|Norma<br>[ug/m3]|%<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**AP**|**LB**|**AP+LB**|**AP+LB**|**AP+LB**|**AP**|**LB**|**AP+LB**|**AP+LB**|**AP+LB**|
|R_1|Estación Purén (Chillán) - Medio<br>Humano|0,0|2,1|2,1|20|11%|0,0|12,0|12,0|50|24%|
|R_2|Mongetun Mapu (Plaza San<br>Ignación) - Medio Humano|0,0|0,0|2,1|2,1|11%|0,0|0,0|12,0|12,0|24%|
|R_3|Junta de Vecinos San Bernardo<br>(ex-escuela) - Medio Humano|0,3|0,3|2,4|2,4|12%|1,1|1,1|13,1|13,1|26%|
|R_4|Comunidad Familiar Indígena Flor<br>del Canelo - Medio Humano|0,0|0,0|2,1|2,1|11%|0,0|0,0|12,0|12,0|24%|
|R_5|Integrante indígena más cercano -<br>Medio Humano|0,0|0,0|2,1|2,1|11%|0,2|0,2|12,2|12,2|24%|
|R_6|Producción y venta de carbón -<br>Medio Humano|0,0|0,0|2,1|2,1|11%|0,0|0,0|12,0|12,0|24%|
|R_7|Producción y venta de carbón -<br>Medio Humano|0,0|0,0|2,1|2,1|11%|0,2|0,2|12,2|12,2|24%|
|R_8|Producción y venta de carbón -<br>Medio Humano|0,0|0,0|2,2|2,2|11%|0,2|0,2|12,2|12,2|24%|
|R_9|Producción y venta de carbón -<br>Medio Humano|0,0|0,0|2,1|2,1|11%|0,1|0,1|12,1|12,1|24%|
|R_10|Producción y venta de carbón -<br>Medio Humano|0,0|0,0|2,2|2,2|11%|0,2|0,2|12,2|12,2|24%|
|R_11|R1 (Ruido)|0,3|0,3|2,4|2,4|12%|1,0|1,0|13,0|13,0|26%|
|R_12|R2 (Ruido)|0,5|0,5|2,6|2,6|13%|1,3|1,3|13,3|13,3|27%|
|R_13|R3 (Ruido)|0,2|0,2|2,3|2,3|12%|0,7|0,7|12,7|12,7|25%|
|R_14|R4 (Ruido)|0,1|0,1|2,2|2,2|11%|0,2|0,2|12,2|12,2|24%|
|R_15|RF (Ruido)|0,0|0,0|2,1|2,1|11%|0,1|0,1|12,1|12,1|24%|

Fuente: Elaboración propia.

78

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA””

**8** **DEFINICIÓN DEL ÁREA DE INFLUENCIA**

De acuerdo con el Reglamento del Sistema de Evaluación de Impacto Ambiental, el área de

influencia _es “El área o espacio geográfico, cuyos atributos, elementos naturales o socioculturales_

_deben ser considerados con la finalidad de definir si el proyecto genera o presenta algunos de los_

_efectos, características o circunstancias del artículo 11 de la Ley, o bien para justificar la inexistencia_

_de dichos efectos características o circunstancias”._ En el contexto de esta definición, para delimitar

el área de influencia se considera como insumo principal los resultados de la Modelación de la

Calidad del Aire, correspondiente a las isoconcentraciones de los contaminantes modelados, los que

permiten asegurar que el Área de Influencia abarque aquellas zonas donde se presentan aportes de

contaminantes generados por el proyecto.

De base a lo anterior se define un polígono conformado por todas las isolíneas de concentración

resultantes de la modelación de los contaminantes y estadísticos considerados, de modo de definir

a través de ellas un área que englobe la zona donde se presentan los aportes principales para los

receptores del proyecto.

En particular, para definir el Área de Influencia de los receptores primarios las curvas consideradas

de isoconcentraciones por cada contaminante, y su estadístico normativo, se establecen de acuerdo

con lo propuesto por el documento SILs [4], del Departamento de Salud y Medio Ambiente de Kansas,

en donde, los niveles de concentración establecidos corresponden a los que se presentan en la

siguiente tabla:

**Tabla 23.** Límites normativos considerados en definición del AI - Receptores primarios.

|Parámetro|Periodo evaluado|SILs [ug/m3]|Norma Chilena<br>[ug/m3]|% de la Norma<br>Chilena|
|---|---|---|---|---|
|NO2|1 hora|10|400|2,5%|
|NO2|Promedio Anual|1|100|1%|
|MP10|24 horas|5|130|4%|
|MP10|Promedio Anual|1|50|2%|
|MP2,5|24 horas|1,2|50|2%|
|MP2,5|Promedio Anual|0,3|20|2%|

Fuente: Elaboración propia.

Por otra parte, para los receptores secundarios se define un área de influencia en base al Material

Particulado Sedimentable (MPS). El SO 2, dado lo imperceptible de sus aportes, no genera un área

4 Significant Impact Levels (SILs), National Ambient Air Quality Standards (NAAQS), PSD Class II Increments, and Significant Monitoring
Concentrations for Criteria Pollutants Kansas Department of Health and Environment, Bureau of Air-Modeling Group.
[https://www.kdheks.gov/bar/modeling/Table_of_NAAQS_SILs_SMCs.pdf](https://www.kdheks.gov/bar/modeling/Table_of_NAAQS_SILs_SMCs.pdf)

79

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

de influencia particular. Respecto del MPS, la curva de isodepositación considerada representa el

1% de la norma referencial utilizada (Cuenca del Río Huasco).

En base a lo definido anteriormente, en la Figura 43 se presenta el área de influencia primario y en

la Figura 44 el área de influencia secundario del proyecto:

**Figura 43.** Área de Influencia primario del Proyecto.

Fuente: Elaboración propia.

80

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**Figura 44.** Área de Influencia secundario del Proyecto.

Fuente: Elaboración propia.

81

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

**9** **ANÁLISIS DE RESULTADOS Y CONCLUSIONES**

Según lo expuesto en el documento, se concluye que:

**Respecto a la descripción y justificación del modelo utilizado y los contaminantes modelados:**

El sistema de modelación utilizado corresponde al denominado “WRF-CALPUFF”, que considera un

modelo tipo “puff” Lagrangiano Gaussiano no estacionario y un modelo meteorológico de predicción

numérica a mesoescala no hidrostático. Este modelo sirve para representar la dispersión de

contaminantes en dominios de modelación cuyas fuentes de emisión se ubican a más de 5 km de

los receptores sensibles a analizar.

En base a las características intrínsecas del Proyecto, y a lo justificado en apartados anterior, los

contaminantes modelados corresponden a MPS, MP 10, MP 2,5 NO 2, SO 2 y CO.

**Respecto a la incertidumbre:**

Se realizó un análisis de incertidumbre del modelo meteorológico de tipo cualitativo y uno

cuantitativo. En el análisis cualitativo se observó que el modelo se acerca bastante a la realidad para

las variables analizadas, correspondientes a dirección del viento, velocidad del viento y temperatura.

De estas tres variables, la temperatura es la variable modelada que mejor se comporta, dado que

los valores promedio presentan un muy buen rendimiento.

Respecto de la velocidad, el análisis cualitativo, se observó en un comportamiento que

subdimensiona los valores altos y bajos, por lo que, respecto de la modelación de contaminantes, se

configura un escenario más desfavorable, en el sentido de que las calmas y la estabilidad atmosférica

(representada por la velocidad) contribuyen a aumentar las concentraciones en los sectores

aledaños a las zonas del Proyecto. En cuanto a las direcciones, en ambas datas se observa una

tendencia muy similar.

**Respecto de la implementación del modelo y el análisis normativo:**

En cuanto a los aportes del Proyecto se indica que:

- En los receptores de interés, para el material particulado MP 10, MP 2,5 y MPS, se generan aportes

que resultan ser valores muy reducidos con respecto a la norma, siendo el receptor R_12 “R2

ruido” más cercano al Proyecto, el que presenta mayor aporte, específicamente sobre el

contaminante MP 2,5, alcanzando una concentración igual 2,58% de la norma. El resto los aportes

en porcentajes respecto de la norma, para MP 10 y MPS, son inferiores a este valor.

- Los aportes para todos los receptores de interés en los gases SO 2 y CO resultan valores muy

reducidos con respecto a la norma, con un aporte menor al 0,1% de la norma en todos sus

estadísticos, lo que se asocia a un aporte igual a 0% de la norma. Para el caso del NO 2 los

82

ANEXO 15. MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO “SANTA GRACIELA SOLAR”

DOÑA GRACIELA SOLAR SPA”

valores resultan bajo la norma, siendo el receptor R_3 “Junta de Vecinos San Bernardo (ex

escuela) - Medio Humano” el que presenta un valor mayor, con un aporte menor al 13,19% de

la norma en todos sus estadísticos.

Finalmente, respecto de los aportes del proyecto, cabe destacar que la calidad del aire basal se

encuentra en estado de latencia para el contaminante MP 10 en un 93% al comparar el percentil 98

de las concentraciones diarias con la norma respectiva. Por otra parte, el aporte máximo del proyecto

en este contaminantes y estadístico es de un 1,3% (1,7 [ug/m2]). Este valor es clasificado como NO

SIGNIFICATIVO en la tabla “Criterios recomendados de incremento significativo en la concentración

de contaminantes atmosféricos en zonas saturadas” (Tabla 0-8) del estudio “Evaluación Significancia

del Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas en el Marco del SEIA

(ID Licitación: 1588-16-LE21)”. En base a lo anterior, es posible indicar que el proyecto no genera

una alteración significativa del área de estudio, el área de influencia y los receptores cercanos.

83

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Cronograma del Proyecto.**

| Fase | Meses - Año 1 | Col3 | Col4 | Col5 | Col6 | Col7 | Años | Col9 | Col10 | Meses - Año 32 | Col12 | Col13 | Col14 | Col15 | Col16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **1 ** | **2 ** | **3 ** | **4 ** | **- ** | **12** | **2-31** | **2-31** | **2-31** | **1 ** | **2 ** | **3 ** | **4 ** | **5 ** | **6 ** |
| Construcción |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Operación |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Cierre |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Tabla 2.: ** Coordenadas estaciones meteorológicas.**

| Estación | Distancia con respecto al<br>área de Proyecto [km] | Coordenadas (UTM WGS84 H18) | Col4 | Variables<br>meteorológicas |
| --- | --- | --- | --- | --- |
| **Estación** | **Distancia con respecto al**<br>**área de Proyecto [km]** | **Este [m]** | **Norte [m]** | **Norte [m]** |
| Purén<br>(Chillán) | 16 | 759.972 | 5.943.765 | Velocidad del viento |
| Purén<br>(Chillán) | 16 | 759.972 | 5.943.765 | Dirección del viento |
| Purén<br>(Chillán) | 16 | 759.972 | 5.943.765 | Temperatura ambiente |

**Tabla 3.: ** Resumen general de las variables meteorológicas consideradas.**

| Variable | Año | Porcentaje data<br>válida [%] | Máximo | Promedio | Mínimo |
| --- | --- | --- | --- | --- | --- |
| Velocidad del viento [m/s] | 2022 | 100% | 7,74 | 1,87 | 0,01 |
| Dirección del viento [°] | Dirección del viento [°] | 100% | 359,95 | 177,35 | 0,11 |
| Temperatura [°C] | Temperatura [°C] | 100% | 39,41 | 14,27 | -3,85 |

**Tabla 5.: ** Caracterización ambiental de la calidad del aire - Material Particulado MP 10 .**

| Contaminante | Estadístico | Concentración<br>[ug/m3] | Evaluación normativa | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Estadístico** | **Concentración**<br>**[ug/m3]** | **Norma** | **% de la norma** |
| MP10 | Promedio Anual | 39 | 50 | 78% |
| MP10 | Percentil 98 - Diario | 121 | 130 | 93% |

**Tabla 6.: ** Caracterización ambiental de la calidad del aire - Material Particulado MP 2.5 .**

| Contaminante | Estadístico | Concentración<br>[ug/m3] | Evaluación normativa | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Estadístico** | **Concentración**<br>**[ug/m3]** | **Norma** | **% de la norma** |
| MP2,5 | Promedio Anual | 2 | 20 | 11% |
| MP2,5 | Percentil 98 - Diario | 12 | 50 | 24% |

**Tabla 7.: ** Norma primaria de calidad del aire.**

| Parámetro | Cuerpo Legal | Estadístico | Valor |
| --- | --- | --- | --- |
| **MP10 ** | D.S. N°12/2021<br>del MMS | Promedio aritmético de tres años calendario consecutivos. | 50 μg/m3 |
| **MP10 ** | D.S. N°12/2021<br>del MMS | Percentil 98 de las concentraciones de 24 horas registradas<br>durante un período anual. | 130<br>μg/m3 |
| **MP2,5 ** | D.S. N°12/11 del<br>MMA | Promedio trianual de las concentraciones anuales. | 20 μg/m3 |
| **MP2,5 ** | D.S. N°12/11 del<br>MMA | Percentil 98 de los promedios diarios registrados durante un<br>año. | 50 μg/m3 |
| **NO2 ** |  | Promedio aritmético de los valores de concentración anual<br>de tres años calendarios sucesivos. | 100<br>μg/m3 |

**Tabla 8.: ** Norma secundaria de calidad del aire para el SO 2 y norma de referencia para el MPS.**

| Parámetro | Cuerpo Legal | Estadístico | Valor |
| --- | --- | --- | --- |
| **SO2 ** | D.S. N°185/92<br>del MIN. DE<br>MINERÍA,<br>modificado por<br>D.S N° 22/09 del<br>MINSEGPRES | Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,73 de la concentración máxima de horaria. | 700<br>μg/m3 |
| **SO2 ** | D.S. N°185/92<br>del MIN. DE<br>MINERÍA,<br>modificado por<br>D.S N° 22/09 del<br>MINSEGPRES | Promedio aritmético anual. | 60 μg/m3 |
| **SO2 ** | D.S. N°185/92<br>del MIN. DE<br>MINERÍA,<br>modificado por<br>D.S N° 22/09 del<br>MINSEGPRES | Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,7 de las concentraciones diarias. | 260<br>μg/m3 |
| **MPS** | Norma de<br>Referencia<br>Cuenca del Río<br>Huasco | Promedio aritmético mensual. | 150<br>mg/m2día |
| **MPS** | Norma de<br>Referencia<br>Cuenca del Río<br>Huasco | Promedio aritmético anual. | 100<br>mg/m2día |

**Tabla 9.: ** Parámetros meteorológicos utilizados en el análisis de incertidumbre.**

| Estación | Coordenadas (UTM - Datum WGS84 - H18) | Col3 | Variables meteorológicas |
| --- | --- | --- | --- |
| **Estación** | **Este [m]** | **Norte [m]** | **Norte [m]** |
| Puren | 759.972 | 5.943.765 | Velocidad y dirección del viento |
| Puren | 759.972 | 5.943.765 | Temperatura ambiente |

**Tabla 10.: ** Referencias de aceptabilidad para los estadígrafos de cada una de variables**

| Estación | BIAS | IOA | MGE | RMSE | r |
| --- | --- | --- | --- | --- | --- |
| Velocidad del Viento | ≤ ±0,5 [m/s] | ≥ 0,60 | - | ≤ 2 [m/s] | 1 |
| Dirección del Viento | ≤ ±10 [°] | ≥ 0,60 | ≤ 30 [°] | - | 1 |
| Temperatura | ≤ ±0,5 [°] | ≥ 0,80 | ≤ 2 [°] | - | 1 |

**Tabla 11.: ** Análisis cuantitativo de la comparación de la data observada y modelada [3] .**

| Variable | BIAS | IOA | MGE | RMSE | r |
| --- | --- | --- | --- | --- | --- |
| Velocidad del viento | 0,16 | 0,57 | 0,77 | 1,02 | 0,75 |

**Tabla 14.: ** Caminos acceso al Proyecto.**

| Tipo de fuente | ID | Descripción | Elevación<br>[m] | Superficie | Col6 | Col7 | Tasa de emisión [t/año-m2] | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de fuente** | **ID** | **Descripción** | **Elevación**<br>**[m]** | **Largo [m]** | **Ancho [m]** | **Área [m2]** | **MP10 ** | **MP2,5 ** | **MPS** | **NOx** | **CO** | **SO2 ** |
| Lineal areal | SRC_1 | Tramo 01 | - | 5195,9 | 5 | 25.980 | 1,82E-06 | 4,63E-07 | 1,82E-06 | 1,35E-06 | 3,22E-07 | 1,38E-09 |
| Lineal areal | SRC_2 | Tramo 02 | - | 3690,9 | 5 | 18.455 | 1,89E-06 | 4,80E-07 | 1,89E-06 | 1,41E-06 | 3,37E-07 | 1,44E-09 |
| Lineal areal | SRC_3 | Tramo 03 | - | 5246,8 | 5 | 26.234 | 2,83E-06 | 7,20E-07 | 2,83E-06 | 2,10E-06 | 5,01E-07 | 2,14E-09 |
| Lineal areal | SRC_4 | Tramo 04 | - | 5.215 | 5 | 26.074 | 2,33E-06 | 5,93E-07 | 2,33E-06 | 1,73E-06 | 4,12E-07 | 1,76E-09 |
| Lineal areal | SRC_5 | Tramo 05 | - | 1.378 | 5 | 6.892 | 2,06E-06 | 5,23E-07 | 2,06E-06 | 1,53E-06 | 3,64E-07 | 1,56E-09 |
| Lineal areal | SRC_6 | Tramo 06 | - | 1.557 | 5 | 7.787 | 1,61E-06 | 4,10E-07 | 1,61E-06 | 1,20E-06 | 2,85E-07 | 1,22E-09 |
| Lineal areal | SRC_7 | Tramo 07 | - | 1.198 | 5 | 5.990 | 3,11E-07 | 7,91E-08 | 3,11E-07 | 2,31E-07 | 5,50E-08 | 2,35E-10 |
| Lineal areal | SRC_8 | Tramo 08 | - <br> | 675 | 5 | 3.375 | 1,29E-06 | 3,29E-07 | 1,29E-06 | 9,59E-07 | 2,29E-07 | 9,78E-10 |
| Lineal areal | SRC_9 | Tramo 09 | <br> | 410 | 5 | 2.051 | 1,31E-06 | 3,34E-07 | 1,31E-06 | 9,74E-07 | 2,32E-07 | 9,93E-10 |
| Lineal areal | SRC_10 | Tramo 10 | <br> | 1.070 | 5 | 5.350 | 9,57E-07 | 2,44E-07 | 9,57E-07 | 7,11E-07 | 1,70E-07 | 7,24E-10 |
| Lineal areal | SRC_11 | Tramo 11 | <br> | 6.229 | 5 | 31.145 | 9,87E-07 | 2,51E-07 | 9,87E-07 | 7,33E-07 | 1,75E-07 | 7,47E-10 |
| Lineal areal | SRC_12 | Tramo 12 | <br> | 3.873 | 5 | 19.364 | 2,69E-07 | 6,85E-08 | 2,69E-07 | 2,00E-07 | 4,77E-08 | 2,04E-10 |
| Lineal areal | SRC_13 | Tramo 13 | <br> | 11.406 | 5 | 57.029 | 2,38E-06 | 6,06E-07 | 2,38E-06 | 1,77E-06 | 4,22E-07 | 1,80E-09 |
| Lineal areal | SRC_14 | Tramo 14 | <br> | 1.490 | 5 | 7.450 | 4,37E-07 | 1,11E-07 | 4,37E-07 | 3,25E-07 | 7,75E-08 | 3,31E-10 |
| Lineal areal | SRC_15 | Tramo 15 | <br> | 175 | 5 | 873 | 5,25E-08 | 1,34E-08 | 5,25E-08 | 3,90E-08 | 9,30E-09 | 3,98E-11 |
| Lineal areal | SRC_16 | Tramo 16 | <br> | 4.641 | 5 | 23.207 | 2,94E-07 | 7,49E-08 | 2,94E-07 | 2,18E-07 | 5,21E-08 | 2,23E-10 |
| Lineal areal | SRC_17 | Tramo 17 | <br> | 3.527 | 5 | 17.635 | 3,17E-07 | 8,06E-08 | 3,17E-07 | 2,35E-07 | 5,61E-08 | 2,40E-10 |
| Lineal areal | SRC_18 | Tramo 18 | <br> | 4.433 | 5 | 22.164 | 4,44E-05 | 4,45E-06 | 4,44E-05 | 1,50E-06 | 3,59E-07 | 1,53E-09 |
| Lineal areal | SRC_19 | Tramo 19 | <br> | 1.787 | 5 | 8.933 | 4,19E-06 | 4,27E-07 | 4,19E-06 | 3,93E-07 | 9,38E-08 | 4,01E-10 |
| Lineal areal | SRC_20 | Tramo 20 | <br> | 206 | 5 | 1.031 | 2,43E-06 | 2,47E-07 | 2,43E-06 | 2,28E-07 | 5,43E-08 | 2,32E-10 |
| Lineal areal | SRC_21 | Tramo 21 | <br> | 223 | 5 | 1.113 | 2,50E-06 | 2,55E-07 | 2,50E-06 | 2,35E-07 | 5,60E-08 | 2,39E-10 |
| Lineal areal | SRC_22 | Tramo 22 | <br> | 285 | 5 | 1.426 | 3,22E-06 | 3,28E-07 | 3,22E-06 | 3,05E-07 | 7,28E-08 | 3,11E-10 |
| Lineal areal | SRC_23 | Tramo 23 | <br> | 2.721 | 5 | 13.604 | 3,08E-08 | 2,23E-08 | 3,08E-08 | 8,73E-07 | 2,08E-07 | 8,90E-10 |
| Lineal areal | SRC_24 | Tramo 24 | <br> | 657 | 5 | 3.283 | 5,37E-06 | 5,47E-07 | 5,37E-06 | 5,06E-07 | 1,21E-07 | 5,16E-10 |
| Lineal areal | SRC_25 | Tramo 25 |  | 7.001 | 5 | 35.007 | 2,08E-05 | 2,09E-06 | 2,08E-05 | 6,89E-07 | 1,64E-07 | 7,03E-10 |

**Tabla 15.: ** Receptores de interés.**

| ID | Descripción | Tipo de<br>receptor | Coordenadas de Ubicación | Col5 |
| --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Tipo de**<br>**receptor** | **(Datum WGS84 - H18)** | **(Datum WGS84 - H18)** |
| **ID** | **Descripción** | **Tipo de**<br>**receptor** | **Este [m]** | **Norte [m]** |
| R_1 | Estación Purén (Chillán) - Medio<br>Humano | Primario | 759.972 | 5.943.765 |
| R_2 | Mongetun Mapu (Plaza San Ignación) -<br>Medio Humano | Mongetun Mapu (Plaza San Ignación) -<br>Medio Humano | 764.975 | 5.923.193 |
| R_3 | Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano | Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano | 762.393 | 5.927.377 |
| R_4 | Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano | Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano | 759.628 | 5.943.886 |
| R_5 | Integrante Indigena más cercano -<br>Medio Humano | Integrante Indigena más cercano -<br>Medio Humano | 762.103 | 5.925.398 |
| R_6 | Producción y venta de carbón - Medio<br>Humano | Producción y venta de carbón - Medio<br>Humano | 756.034 | 5.930.111 |
| R_7 | Producción y venta de carbón - Medio<br>Humano | Producción y venta de carbón - Medio<br>Humano | 762.378 | 5.925.748 |
| R_8 | Producción y venta de carbón - Medio<br>Humano | Producción y venta de carbón - Medio<br>Humano | 762.742 | 5.926.307 |
| R_9 | Producción y venta de carbón - Medio<br>Humano | Producción y venta de carbón - Medio<br>Humano | 756.395 | 5.930.475 |
| R_10 | Producción y venta de carbón - Medio<br>Humano | Producción y venta de carbón - Medio<br>Humano | 762.829 | 5.926.378 |
| R_11 | R1 (Ruido) | R1 (Ruido) | 762.406 | 5.927.352 |
| R_12 | R2 (Ruido) | R2 (Ruido) | 761.064 | 5.925.708 |
| R_13 | R3 (Ruido) | R3 (Ruido) | 760.585 | 5.925.397 |
| R_14 | R4 (Ruido) | R4 (Ruido) | 761.531 | 5.928.526 |
| R_15 | RF (Ruido) | RF (Ruido) | 759.175 | 5.927.299 |
| R_16 | Frutillas | Secundario | 762.469 | 5.931.046 |
| R_17 | Frutillas | Frutillas | 762.458 | 5.931.133 |
| R_18 | Frutillas | Frutillas | 759.842 | 5.924.188 |
| R_19 | Frutillas | Frutillas | 760.204 | 5.924.171 |
| R_20 | Frutillas | Frutillas | 763.309 | 5.926.117 |
| R_21 | Frutillas | Frutillas | 763.393 | 5.926.354 |
| R_22 | Frutillas | Frutillas | 762.883 | 5.927.197 |
| R_23 | Frutillas | Frutillas | 763.081 | 5.927.717 |
| R_24 | Frutillas | Frutillas | 762.823 | 5.929.150 |
| R_25 | Frutillas | Frutillas | 762.854 | 5.929.330 |
| R_26 | Frutillas | Frutillas | 762.449 | 5.929.371 |
| R_27 | Frutillas | Frutillas | 762.504 | 5.929.422 |
| R_28 | Frutillas | Frutillas | 762.708 | 5.929.416 |

**Tabla 16.: ** Puntos de máxima concentración (PMC).**

| ID | Cont. | Tipo de<br>Norma | Estadístico | PMC<br>[ug/m<br>3] | Norma<br>[ug/m3] | Unidad | %<br>Norma | Coordenadas UTM -<br>WGS84 | Col10 | Coordenadas<br>LCC - NWS84 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Cont.** | **Tipo de**<br>**Norma** | **Estadístico** | **PMC**<br>**[ug/m**<br>**3]** | **Norma**<br>**[ug/m3]** | **Unidad** | **% **<br>**Norma** | **Este [m]** | **Norte [m]** | **X [km]** | **Y [km]** |
| PMC1 | MPS | Secundaria | Promedio del<br>Periodo | 1,7 | 100 | mg/m2-<br>día | 1,67% | 757.204 | 5.930.377 | -4,50 | 2,50 |
| PMC1 | MPS | Secundaria | Promedio<br>mensual | 2,7 | 150 | 150 | 1,83% | 757.204 | 5.930.377 | -4,50 | 2,50 |
| PMC2 | MP10 | Primaria | Promedio del<br>Periodo | 1,29 | 50 | ug/m3 | 2,59% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | MP10 | Primaria | Percentil 98<br>Diario | 2,78 | 130 | 130 | 2,14% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | MP2,5 | Primaria | Promedio del<br>Periodo | 1,02 | 20 | 20 | 5,10% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | MP2,5 | Primaria | Percentil 98<br>Diario | 2,19 | 50 | 50 | 4,37% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | SO2 | Primaria | Promedio del<br>Periodo | 0,12 | 60 | 60 | 0,19% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | SO2 | Primaria | Percentil 99<br>Diario | 0,24 | 150 | 150 | 0,16% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | SO2 | Primaria | Percentil 98,5<br>Horario | 0,60 | 350 | 350 | 0,17% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | SO2 | Secundaria | Promedio del<br>Periodo | 0,12 | 60 | 60 | 0,19% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | SO2 | Secundaria | Percentil 99,7<br>Diario | 0,27 | 260 | 260 | 0,10% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | SO2 | Secundaria | Percentil 99,73<br>Horario | 0,80 | 700 | 700 | 0,11% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | NO2 | Primaria | Promedio del<br>Periodo | 10,08 | 100 | 100 | 10,08% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | NO2 | Primaria | Percentil 99<br>Horario | 79,40 | 400 | 400 | 19,85% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | CO | Primaria | Percentil 99 8<br>Horas | 18,36 | 10.000 | 10.000 | 0,18% | 762124 | 5927229 | 0,50 | -0,50 |
| PMC2 | CO | Primaria | Percentil 99<br>Horario | 37,19 | 30.000 | 30.000 | 0,12% | 762124 | 5927229 | 0,50 | -0,50 |

**Tabla 17.: ** Aportes del Proyecto en receptores primarios.**

| ID | Descripción | MP [ug/m3]<br>10 | Col4 | MP [ug/m3]<br>2.5 | Col6 | SO [ug/m3]<br>2 | Col8 | Col9 | NO [ug/m3]<br>2 | Col11 | CO [ug/m3] | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Media**<br>**Anual** | **P98**<br>**Diario** | **Media**<br>**Anual** | **P98**<br>**Diario** | **Media**<br>**Anual** | **P99**<br>**Diario** | **P98.5**<br>**Horario** | **Media**<br>**Anual** | **P99**<br>**Horario** | **P99 8**<br>**hrs.** | **P99**<br>**Horario** |
| R_1 | Estación Purén (Chillán) - Medio<br>Humano | <0,01 | 0,01 | <0,01 | <0,01 | <0,01 | <0,01 | <0,01 | <0,01 | 0,13 | 0,02 | 0,07 |
| R_2 | Mongetun Mapu (Plaza San Ignación)<br>- Medio Humano | 0,01 | 0,05 | <0,01 | 0,02 | <0,01 | <0,01 | <0,01 | 0,02 | 0,89 | 0,11 | 0,42 |
| R_3 | Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano | 0,43 | 1,34 | 0,32 | 1,05 | 0,03 | 0,10 | 0,31 | 2,71 | 52,77 | 9,03 | 25,35 |
| R_4 | Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano | <0,01 | 0,01 | <0,01 | <0,01 | <0,01 | <0,01 | <0,01 | 0,00 | 0,14 | 0,02 | 0,07 |
| R_5 | Integrante indígena más cercano -<br>Medio Humano | 0,05 | 0,25 | 0,03 | 0,17 | <0,01 | 0,01 | 0,03 | 0,21 | 8,73 | 1,36 | 4,15 |
| R_6 | Producción y venta de carbón - Medio<br>Humano | 0,07 | 0,26 | 0,01 | 0,04 | <0,01 | <0,01 | <0,01 | 0,02 | 0,99 | 0,12 | 0,47 |
| R_7 | Producción y venta de carbón - Medio<br>Humano | 0,06 | 0,26 | 0,04 | 0,17 | <0,01 | 0,01 | 0,04 | 0,23 | 7,08 | 1,33 | 3,67 |
| R_8 | Producción y venta de carbón - Medio<br>Humano | 0,09 | 0,32 | 0,05 | 0,20 | <0,01 | 0,01 | 0,04 | 0,27 | 11,41 | 1,61 | 5,52 |
| R_9 | Producción y venta de carbón - Medio<br>Humano | 0,29 | 0,66 | 0,03 | 0,08 | <0,01 | <0,01 | <0,01 | 0,02 | 1,17 | 0,14 | 0,60 |
| R_10 | Producción y venta de carbón - Medio<br>Humano | 0,09 | 0,32 | 0,05 | 0,20 | <0,01 | 0,01 | 0,04 | 0,26 | 10,09 | 1,54 | 5,26 |
| R_11 | R1 (Ruido) | 0,41 | 1,32 | 0,30 | 1,01 | 0,03 | 0,09 | 0,30 | 2,49 | 52,33 | 8,81 | 25,29 |
| R_12 | R2 (Ruido) | 0,59 | 1,72 | 0,46 | 1,29 | 0,05 | 0,13 | 0,36 | 4,30 | 50,46 | 10,22 | 23,77 |
| R_13 | R3 (Ruido) | 0,27 | 1,00 | 0,19 | 0,75 | 0,02 | 0,07 | 0,24 | 1,61 | 45,83 | 6,71 | 22,34 |
| R_14 | R4 (Ruido) | 0,20 | 0,61 | 0,08 | 0,24 | 0,01 | 0,02 | 0,06 | 0,57 | 10,55 | 2,00 | 5,41 |
| R_15 | RF (Ruido) | 0,12 | 0,37 | 0,02 | 0,11 | 0,00 | 0,01 | 0,02 | 0,09 | 4,90 | 1,03 | 2,41 |

**Tabla 18.: ** Aportes del Proyecto en receptores secundarios.**

| ID Modelo | Receptor | MPS [mg/m2d] | Col4 | SO [ug/m3]<br>2 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID Modelo** | **Receptor** | **Media Anual** | **Media Mensual** | **Media Anual** | **P99.7 Diario** | **P99.73 Horario** |
| R_16 | Frutillas | 0,01 | 0,02 | <0,01 | <0,01 | 0,01 |
| R_17 | Frutillas | 0,01 | 0,02 | <0,01 | <0,01 | 0,01 |
| R_18 | Frutillas | 0,29 | 0,37 | <0,01 | 0,01 | 0,04 |
| R_19 | Frutillas | <0,01 | <0,01 | <0,01 | 0,01 | 0,04 |
| R_20 | Frutillas | 0,01 | 0,01 | <0,01 | 0,01 | 0,04 |
| R_21 | Frutillas | 0,10 | 0,17 | <0,01 | 0,01 | 0,05 |
| R_22 | Frutillas | 0,01 | 0,02 | 0,01 | 0,03 | 0,19 |
| R_23 | Frutillas | 0,11 | 0,14 | <0,01 | 0,02 | 0,10 |
| R_24 | Frutillas | 0,51 | 0,76 | <0,01 | 0,01 | 0,04 |
| R_25 | Frutillas | 0,11 | 0,15 | <0,01 | 0,01 | 0,03 |
| R_26 | Frutillas | 0,27 | 0,35 | <0,01 | 0,01 | 0,04 |
| R_27 | Frutillas | 0,53 | 0,65 | <0,01 | 0,01 | 0,03 |
| R_28 | Frutillas | 0,12 | 0,25 | <0,01 | 0,01 | 0,03 |
| R_29 | Frutillas | 0,12 | 0,13 | <0,01 | 0,01 | 0,03 |
| R_30 | Frutillas | 0,07 | 0,09 | <0,01 | 0,01 | 0,03 |
| R_31 | Frutillas | 0,01 | 0,02 | <0,01 | 0,01 | 0,03 |

**Tabla 19.: ** Relación del aporte del Proyecto con la normativa primaria vigente.**

| ID | Receptor/Norma | MP [ug/m3]<br>10 | Col4 | MP [ug/m3]<br>2.5 | Col6 | SO [ug/m3]<br>2 | Col8 | Col9 | NO [ug/m3]<br>2 | Col11 | CO [ug/m3] | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Receptor/Norma** | **Media**<br>**Anual** | **P98**<br>**Diario** | **Media**<br>**Anual** | **P98**<br>**Diario** | **Media**<br>**Anual** | **P99**<br>**Diario** | **P98.5**<br>**Horario** | **Media**<br>**Anual** | **P99**<br>**Horario** | **P99 8**<br>**hrs.** | **P99**<br>**Horari**<br>**o ** |
| **ID** | **Receptor/Norma** | **50** | **130** | **20** | **50** | **60** | **150** | **350** | **100** | **400** | **10.000** | **30.000** |
| R_1 | Estación Purén (Chillán) - Medio<br>Humano | <0,01% | 0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | 0,03% | <0,01% | <0,01% |
| R_2 | Mongetun Mapu (Plaza San Ignación) -<br>Medio Humano | 0,02% | 0,04% | 0,02% | 0,04% | <0,01% | <0,01% | <0,01% | 0,02% | 0,22% | <0,01% | <0,01% |
| R_3 | Junta de Vecinos San Bernardo (ex-<br>escuela) - Medio Humano | 0,86% | 1,03% | 1,59% | 2,10% | 0,05% | 0,06% | 0,09% | 2,71% | 13,19% | 0,09% | 0,08% |
| R_4 | Comunidad Familiar Indígena Flor del<br>Canelo - Medio Humano | <0,01% | 0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | 0,04% | <0,01% | <0,01% |
| R_5 | Integrante indígena más cercano -<br>Medio Humano | 0,11% | 0,19% | 0,17% | 0,33% | <0,01% | 0,01% | 0,01% | 0,21% | 2,18% | 0,01% | 0,01% |
| R_6 | Producción y venta de carbón - Medio<br>Humano | 0,15% | 0,20% | 0,06% | 0,08% | <0,01% | <0,01% | <0,01% | 0,02% | 0,25% | <0,01% | <0,01% |
| R_7 | Producción y venta de carbón - Medio<br>Humano | 0,12% | 0,20% | 0,19% | 0,34% | <0,01% | 0,01% | 0,01% | 0,23% | 1,77% | 0,01% | 0,01% |
| R_8 | Producción y venta de carbón - Medio<br>Humano | 0,18% | 0,25% | 0,25% | 0,40% | <0,01% | 0,01% | 0,01% | 0,27% | 2,85% | 0,02% | 0,02% |
| R_9 | Producción y venta de carbón - Medio<br>Humano | 0,58% | 0,51% | 0,16% | 0,15% | <0,01% | <0,01% | <0,01% | 0,02% | 0,29% | <0,01% | <0,01% |
| R_10 | Producción y venta de carbón - Medio<br>Humano | 0,17% | 0,24% | 0,24% | 0,40% | <0,01% | 0,01% | 0,01% | 0,26% | 2,52% | 0,02% | 0,02% |
| R_11 | R1 (Ruido) | 0,82% | 1,02% | 1,49% | 2,03% | 0,05% | 0,06% | 0,09% | 2,49% | 13,08% | 0,09% | 0,08% |
| R_12 | R2 (Ruido) | 1,17% | 1,32% | 2,29% | Y e | 0,08% | 0,09% | 0,10% | 4,30% | 12,61% | 0,10% | 0,08% |
| R_13 | R3 (Ruido) | 0,54% | 0,77% | 0,97% | 1,50% | 0,03% | 0,05% | 0,07% | 1,61% | 11,46% | 0,07% | 0,07% |
| R_14 | R4 (Ruido) | 0,40% | 0,47% | 0,40% | 0,48% | 0,01% | 0,02% | 0,02% | 0,57% | 2,64% | 0,02% | 0,02% |
| R_15 | RF (Ruido) | 0,24% | 0,28% | 0,11% | 0,22% | <0,01% | 0,01% | 0,01% | 0,09% | 1,22% | 0,01% | 0,01% |

**Tabla 20.: ** Relación del aporte del Proyecto con la normativa secundaria vigente.**

| ID Modelo | Receptor/Norma | MPS [mg/m2d] | Col4 | SO [ug/m3]<br>2 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ID Modelo** | **Receptor/Norma** | **Media Anual** | **Media Mensual** | **Media Anual** | **P99.7 Diario** | **P99.73 Horario** |
| **ID Modelo** | **Receptor/Norma** | **100** | **150** | **60** | **260** | **700** |
| R_16 | Frutillas | 0,01% | 0,01% | <0,01% | <0,01% | <0,01% |
| R_17 | Frutillas | 0,01% | 0,01% | <0,01% | <0,01% | <0,01% |
| R_18 | Frutillas | 0,01% | 0,02% | <0,01% | <0,01% | 0,01% |
| R_19 | Frutillas | 0,01% | 0,01% | <0,01% | <0,01% | 0,01% |
| R_20 | Frutillas | 0,09% | 0,07% | <0,01% | <0,01% | 0,01% |
| R_21 | Frutillas | 0,04% | 0,04% | <0,01% | <0,01% | 0,01% |
| R_22 | Frutillas | 0,04% | 0,05% | 0,01% | 0,01% | 0,03% |
| R_23 | Frutillas | 0,02% | 0,02% | 0,01% | 0,01% | 0,01% |
| R_24 | Frutillas | 0,02% | 0,02% | <0,01% | <0,01% | 0,01% |
| R_25 | Frutillas | 0,02% | 0,02% | <0,01% | <0,01% | <0,01% |
| R_26 | Frutillas | 0,03% | 0,03% | <0,01% | <0,01% | 0,01% |
| R_27 | Frutillas | 0,03% | 0,03% | <0,01% | <0,01% | <0,01% |
| R_28 | Frutillas | 0,02% | 0,02% | <0,01% | <0,01% | <0,01% |
| R_29 | Frutillas | 0,03% | 0,02% | <0,01% | <0,01% | <0,01% |
| R_30 | Frutillas | 0,02% | 0,02% | <0,01% | <0,01% | <0,01% |
| R_31 | Frutillas | 0,02% | 0,02% | <0,01% | <0,01% | <0,01% |

**Tabla 21.: ** Escenario Proyectado - Material Particulado MP 10 .**

| ID | Receptor | MP Promedio anual [ug/m3]<br>10 | Col4 | Col5 | Norma<br>[ug/m3] | %Norma | MP P98 Diario [ug/m3]<br>10 | Col9 | Col10 | Norma<br>[ug/m3] | % Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Receptor** | **AP** | **LB** | **AP+LB** | **AP+LB** | **AP+LB** | **AP** | **LB** | **AP+LB** | **AP+LB** | **AP+LB** |
| R_1 | Estación Purén (Chillán) -<br>Medio Humano | <0,1 | 39,2 | 39,2 | 50 | 78% | <0,1 | 121,3 | 121,3 | 130 | 93% |
| R_2 | Mongetun Mapu (Plaza San<br>Ignación) - Medio Humano | <0,1 | <0,1 | 39,2 | 39,2 | 78% | 0,1 | 0,1 | 121,4 | 121,4 | 93% |
| R_3 | Junta de Vecinos San Bernardo<br>(ex-escuela) - Medio Humano | 0,4 | 0,4 | 39,6 | 39,6 | 79% | 1,3 | 1,3 | 122,7 | 122,7 | 94% |
| R_4 | Comunidad Familiar Indígena<br>Flor del Canelo - Medio<br>Humano | <0,1 | <0,1 | 39,2 | 39,2 | 78% | <0,1 | <0,1 | 121,3 | 121,3 | 93% |
| R_5 | Integrante indígena más<br>cercano - Medio Humano | 0,1 | 0,1 | 39,3 | 39,3 | 79% | 0,2 | 0,2 | 121,6 | 121,6 | 94% |
| R_6 | Producción y venta de carbón -<br>Medio Humano | 0,1 | 0,1 | 39,3 | 39,3 | 79% | 0,3 | 0,3 | 121,6 | 121,6 | 94% |
| R_7 | Producción y venta de carbón -<br>Medio Humano | 0,1 | 0,1 | 39,3 | 39,3 | 79% | 0,3 | 0,3 | 121,6 | 121,6 | 94% |
| R_8 | Producción y venta de carbón -<br>Medio Humano | 0,1 | 0,1 | 39,3 | 39,3 | 79% | 0,3 | 0,3 | 121,7 | 121,7 | 94% |
| R_9 | Producción y venta de carbón -<br>Medio Humano | 0,3 | 0,3 | 39,5 | 39,5 | 79% | 0,7 | 0,7 | 122,0 | 122,0 | 94% |
| R_10 | Producción y venta de carbón -<br>Medio Humano | 0,1 | 0,1 | 39,3 | 39,3 | 79% | 0,3 | 0,3 | 121,7 | 121,7 | 94% |
| R_11 | R1 (Ruido) | 0,4 | 0,4 | 39,6 | 39,6 | 79% | 1,3 | 1,3 | 122,7 | 122,7 | 94% |
| R_12 | R2 (Ruido) | 0,6 | 0,6 | 39,8 | 39,8 | 80% | 1,7 | 1,7 | 123,1 | 123,1 | 95% |
| R_13 | R3 (Ruido) | 0,3 | 0,3 | 39,5 | 39,5 | 79% | 1,0 | 1,0 | 122,3 | 122,3 | 94% |
| R_14 | R4 (Ruido) | 0,2 | 0,2 | 39,4 | 39,4 | 79% | 0,6 | 0,6 | 121,9 | 121,9 | 94% |
| R_15 | RF (Ruido) | 0,1 | 0,1 | 39,3 | 39,3 | 79% | 0,4 | 0,4 | 121,7 | 121,7 | 94% |

**Tabla 22.: ** Escenario Proyectado - Material Particulado MP 2.5 .**

| ID | Descripción | MP2.5 Promedio anual [ug/m3] | Col4 | Col5 | Norma<br>[ug/m3] | %Norm<br>a | MP2.5 P98 Diario [ug/m3] | Col9 | Col10 | Norma<br>[ug/m3] | %<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **AP** | **LB** | **AP+LB** | **AP+LB** | **AP+LB** | **AP** | **LB** | **AP+LB** | **AP+LB** | **AP+LB** |
| R_1 | Estación Purén (Chillán) - Medio<br>Humano | 0,0 | 2,1 | 2,1 | 20 | 11% | 0,0 | 12,0 | 12,0 | 50 | 24% |
| R_2 | Mongetun Mapu (Plaza San<br>Ignación) - Medio Humano | 0,0 | 0,0 | 2,1 | 2,1 | 11% | 0,0 | 0,0 | 12,0 | 12,0 | 24% |
| R_3 | Junta de Vecinos San Bernardo<br>(ex-escuela) - Medio Humano | 0,3 | 0,3 | 2,4 | 2,4 | 12% | 1,1 | 1,1 | 13,1 | 13,1 | 26% |
| R_4 | Comunidad Familiar Indígena Flor<br>del Canelo - Medio Humano | 0,0 | 0,0 | 2,1 | 2,1 | 11% | 0,0 | 0,0 | 12,0 | 12,0 | 24% |
| R_5 | Integrante indígena más cercano -<br>Medio Humano | 0,0 | 0,0 | 2,1 | 2,1 | 11% | 0,2 | 0,2 | 12,2 | 12,2 | 24% |
| R_6 | Producción y venta de carbón -<br>Medio Humano | 0,0 | 0,0 | 2,1 | 2,1 | 11% | 0,0 | 0,0 | 12,0 | 12,0 | 24% |
| R_7 | Producción y venta de carbón -<br>Medio Humano | 0,0 | 0,0 | 2,1 | 2,1 | 11% | 0,2 | 0,2 | 12,2 | 12,2 | 24% |
| R_8 | Producción y venta de carbón -<br>Medio Humano | 0,0 | 0,0 | 2,2 | 2,2 | 11% | 0,2 | 0,2 | 12,2 | 12,2 | 24% |
| R_9 | Producción y venta de carbón -<br>Medio Humano | 0,0 | 0,0 | 2,1 | 2,1 | 11% | 0,1 | 0,1 | 12,1 | 12,1 | 24% |
| R_10 | Producción y venta de carbón -<br>Medio Humano | 0,0 | 0,0 | 2,2 | 2,2 | 11% | 0,2 | 0,2 | 12,2 | 12,2 | 24% |
| R_11 | R1 (Ruido) | 0,3 | 0,3 | 2,4 | 2,4 | 12% | 1,0 | 1,0 | 13,0 | 13,0 | 26% |
| R_12 | R2 (Ruido) | 0,5 | 0,5 | 2,6 | 2,6 | 13% | 1,3 | 1,3 | 13,3 | 13,3 | 27% |
| R_13 | R3 (Ruido) | 0,2 | 0,2 | 2,3 | 2,3 | 12% | 0,7 | 0,7 | 12,7 | 12,7 | 25% |
| R_14 | R4 (Ruido) | 0,1 | 0,1 | 2,2 | 2,2 | 11% | 0,2 | 0,2 | 12,2 | 12,2 | 24% |
| R_15 | RF (Ruido) | 0,0 | 0,0 | 2,1 | 2,1 | 11% | 0,1 | 0,1 | 12,1 | 12,1 | 24% |

**Tabla 23.: ** Límites normativos considerados en definición del AI - Receptores primarios.**

| Parámetro | Periodo evaluado | SILs [ug/m3] | Norma Chilena<br>[ug/m3] | % de la Norma<br>Chilena |
| --- | --- | --- | --- | --- |
| NO2 | 1 hora | 10 | 400 | 2,5% |
| NO2 | Promedio Anual | 1 | 100 | 1% |
| MP10 | 24 horas | 5 | 130 | 4% |
| MP10 | Promedio Anual | 1 | 50 | 2% |
| MP2,5 | 24 horas | 1,2 | 50 | 2% |
| MP2,5 | Promedio Anual | 0,3 | 20 | 2% |
