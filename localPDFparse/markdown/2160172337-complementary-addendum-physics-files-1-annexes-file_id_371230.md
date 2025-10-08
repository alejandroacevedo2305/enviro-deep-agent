---
title: Sin título
author: Valeria Mundaca
date: D:20250211094658-03'00'
language: es
type: report
pages: 93
has_toc: False
has_tables: True
extraction_quality: high
---

**ANEXO 2.4.1: MODELACIÓN DE ODORANTES**

**DECLARACIÓN DE IMPACTO AMBIENTAL**

**“PLANTA DE TRATAMIENTO DE RILES AQUALIF”**

**FEBRERO 2025**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**INDICE**



1 Introducción ........................................................................................................ 8

2 Objetivos ........................................................................................................... 11

3 Antecedentes ..................................................................................................... 11

3.1 Geografía y topografía ................................................................................. 11

3.2 Meteorología .............................................................................................. 12

3.2.1 Temperatura ........................................................................................... 13

3.2.2 Precipitación ........................................................................................... 16

3.2.3 Velocidad y dirección del viento ................................................................ 18

4 Marco regulatorio de olores ................................................................................. 21

4.1 Justificación normativa de comparación ........................................................ 22

5 Modelos utilizados .............................................................................................. 24

5.1 Modelo CALPUFF ......................................................................................... 25

5.2 Modelo Weather Research and Forecast (WRF) ............................................. 27

6 Metodología ....................................................................................................... 28

6.1 Subgrilla .................................................................................................... 29

6.2 Escenario de modelación ............................................................................. 31

6.2.1 Abatimiento ............................................................................................ 36

6.3 Factores de emisión .................................................................................... 36

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



6.4 Receptores ................................................................................................. 42

7 Estimación de emisiones de olor .......................................................................... 45

8 Modelación meteorológica ................................................................................... 49

8.1 Análisis de incertidumbre ............................................................................. 50

8.1.1 Análisis cuantitativo ................................................................................. 53

8.1.2 Análisis cualitativo ................................................................................... 54

8.2 Caracterizaciones variables meteorológicas ................................................... 63

8.2.1 Viento .................................................................................................... 63

8.2.2 Temperatura del aire ............................................................................... 70

8.2.1 Capa límite atmosférica ............................................................................ 74

8.2.1 Precipitación ........................................................................................... 80

9 Modelación de olor ............................................................................................. 81

9.1 Resultados de la dispersión de olor y análisis normativo ................................. 82

9.2 Percepción de olor ...................................................................................... 88

10 Conclusión ..................................................................................................... 91

11 Bibliografía..................................................................................................... 93

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

ÍNDICE DE TABLAS



Tabla 1. Ubicación punto central del proyecto ............................................................... 9

Tabla 2. Norma de olores de referencia ....................................................................... 23

Tabla 3. Límite normativo .......................................................................................... 23

Tabla 4. Fuentes de olor modeladas del proyecto ......................................................... 33

Tabla 5. Valores del parámetro P (% del flujo que llega por gravedad) para los diferentes

procesos de la planta................................................................................................. 37

Tabla 6. Parámetros para la selección de los factores de emisión .................................. 38

Tabla 7. Factores de emisión para cada una de las fuentes modeladas y su respectiva

justificación .............................................................................................................. 39

Tabla 8. Receptores cercanos al proyecto .................................................................... 42

Tabla 9. Estimación de emisiones odorantes ................................................................ 46

Tabla 10. Ranking de las unidades generadoras de olor ................................................ 48

Tabla 11. Coordenadas del centroide del modelo WRF .................................................. 49

Tabla 12. Resultados estadísticos obtenidos por la modelación respecto a las estaciones

emplazadas dentro del dominio de modelación aledañas al proyecto ............................. 53

Tabla 13. Temperatura modelada y observada en estación Pudahuel ............................. 54

Tabla 14. Velocidad del viento modelada y observada en estación Pudahuel .................. 57

Tabla 15. Dirección del viento modelada y observada en estación Pudahuel ................... 60

Tabla 16. Rosa y distribución de la velocidad del viento ................................................ 68

Tabla 17. Características de la pluma de dispersión ...................................................... 83

Tabla 18. Análisis del cumplimiento normativo en los receptores ................................... 86

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



Tabla 19. Descriptores de efectos de olor propuestos para impactos predichos por

modelación ............................................................................................................... 88

Tabla 20. Percepción del olor en los receptores cercanos al proyecto ............................. 89

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

ÍNDICE DE FIGURAS



Figura 1. Ubicación del proyecto .................................................................................. 9

Figura 2. Punto representativo del centro del proyecto ................................................. 10

Figura 3. Elevación de terreno para la Región de Los Lagos .......................................... 12

Figura 4. Ubicación del proyecto y estación Pudahuel ................................................... 13

Figura 5. Serie de tiempo para la variable temperatura medida en la estación Pudahuel .. 14

Figura 6. Ciclo diario de la variable temperatura medida en la estación Pudahuel ............ 15

Figura 7. Ciclo estacionar de la variable temperatura medida en la estación Pudahuel ..... 16

Figura 8. Serie de tiempo para la variable Precipitación medida en la estación Pudahuel . 17

Figura 9. Precipitación acumulada mensual medida en la estación Pudahuel ................... 18

Figura 10. Series de tiempo de las variables velocidad y rapidez del viento medidas en la

estación Alerce ......................................................................................................... 19

Figura 11. Ciclos diarios para las variables de velocidad y dirección del viento medidas en la

estación Pudahuel ..................................................................................................... 20

Figura 12. Subgrilla utilizada para la pluma de dispersión ............................................. 30

Figura 13. Ubicación fuentes de olor ........................................................................... 31

Figura 14. Ubicación de los receptores discretos cercanos al proyecto ........................... 44

Figura 15. Centroide y extensión del modelo WRF ........................................................ 50

Figura 16. Serie de tiempo de la velocidad del viento modelada para el año 2022 ........... 64

Figura 17. Ciclo diario del viento construido con modelo WRF 2022 ............................... 65

Figura 18. Ciclo diario del viento con un rango del 90% de lo modelado por el WRF 2022

............................................................................................................................... 66

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



Figura 19. Ciclo mensual del viento construido con modelo WRF 2022 ........................... 67

Figura 20. Serie de tiempo de la temperatura modelada por el modelo WRF, para el año

2022 ........................................................................................................................ 71

Figura 21. Ciclo diario de temperatura construido con modelo WRF 2022 ....................... 72

Figura 22. Ciclo diario de temperatura con un rango del 90% de lo modelado por el WRF

2022 ........................................................................................................................ 73

Figura 23. Ciclo mensual para la temperatura construido con modelo WRF 2022 ............ 74

Figura 24. Serie de tiempo de la altura de la capa límite modelada por WRF, para el año

2022 ........................................................................................................................ 76

Figura 25. Ciclo diario altura de capa límite construido con modelo WRF 2022 ................ 77

Figura 26. Ciclo diario altura de capa límite con un rango del 90% de lo modelado por el

WRF 2022 ................................................................................................................ 78

Figura 27. Ciclo diario de altura de la capa límite construida con modelo WRF 2022 ........ 79

Figura 28. Precipitación mensual construida con modelo WRF 2022 ............................... 81

Figura 29. Pluma de dispersión de odorantes e isodoras ............................................... 83

Figura 30. Área de influencia del proyecto ................................................................... 85

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**1** **Introducción**

El presente informe exhibe los resultados obtenidos en la modelación de dispersión e

impacto de compuestos odorantes asociados a la "Planta de Tratamiento de RILes

AQUALIF".

El proyecto "Planta de Tratamiento de RILes AQUALIF", se ubica en la comuna de Lampa,

Región de Metropolitana de Santiago, dentro del Parque Industrial Miraflores, como muestra

la **Figura 1**, el punto central del área del proyecto se presenta en la **Tabla 1.** El proyecto

consiste en construcción y posterior operación de una planta de tratamiento de RILes de

nombre AQUALIF. El proyecto está diseñado para recibir un volumen máximo de 100 m3 de

RILes desde camiones por día. Como resultado del proceso, se obtiene agua limpia y lodos

deshidratados. Del volumen tratado, se recupera aproximadamente 60 m3 diarios

destinados a la venta para su uso como agua industrial, la cual se encontrará en

cumplimiento con la Tabla N°1 del DS N°90/00. Esta agua será almacenada en ocho

estanques con una capacidad de 30 m3 cada uno. En función de esto, se espera un flujo de

tres camiones diarios para el retiro del efluente tratado.

En cuanto a los lodos deshidratados, con un contenido de 25% de materia seca, se generará

una cantidad máxima de 1.449 kg/h, lo que equivale a 34,7 toneladas diarias. Estos lodos

serán almacenados en un contenedor estanco con capacidad para 9 toneladas, por lo que

se prevé un total de cuatro viajes diarios para su retiro, realizando el cambio de contenedor

cada seis horas.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Figura 1. Ubicación del proyecto**



En este informe, se presenta una estimación de las emisiones de odorantes del proyecto, y

los efectos que dichas emisiones producen en el aire. Su elaboración, se basó en las

recomendaciones de la “Guía para la predicción y evaluación de impactos por olor en el

SEIA”, (SEA, 2017), con esto se busca conocer y/o descartar posibles impactos a la población

cercana al emplazamiento del proyecto. El punto representativo central del proyecto es

presentado en la **Tabla 1** y su representación geográfica se detalla en la **Figura 2**

**Tabla 1. Ubicación punto central del proyecto**

|Coordenadas del proyecto (UTM 19 WGS 84)|Col2|
|---|---|
|**Coordenada Este (m)**|**Coordenada Norte (m)**|
|329.545|6.308.789|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Figura 2. Punto representativo del centro del proyecto**



Además, es preciso indicar que, a la fecha en Chile no existe una norma que regule la

inmisión en los receptores cercanos a una planta de tratamiento de riles, sin embargo, en

el contexto de la evaluación ambiental, los resultados serán analizados con los estándares

internacionales. La norma de referencia utilizada para la presente evaluación corresponde a

la Ordenanza Municipal de Calidad Odorífera del Aire NPE: A-240415-5055 de Alcantarilla,

Murcia, España [1], la que posee límites específicos para plantas de tratamientos,

estableciendo límites de inmisión de 1,5 uo/m [3] .

Por último, de acuerdo con lo solicitado en la observación 4.2.1.4 del ICSARA, se utiliza el

año 2022, para realizar la modelación meteorológica WRF, el cual corresponde al año previo

al ingreso del Proyecto al SEIA.

1 NPE: A-240415-5055, 2015. Recuperado desde https://www.borm.es/eli/es-mu-01300050/odnz/2015/4/24/(1)/dof/spa/html

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**2** **Objetivos**

El presente informe tiene como objetivo general cuantificar y evaluar el impacto atmosférico

de las emisiones de olor generadas por el proyecto, así como determinar sus

concentraciones y área de influencia.

Para lo anterior se plantean los siguientes objetivos específicos:

 Determinar la normativa internacional aplicable a las características del proyecto.

 Estimar las cantidades esperadas de emisiones odoríficas del proyecto, considerando

factores de emisión o emisiones de referencia, según corresponda, para cada una

de las fuentes identificadas.

 - Evaluar las concentraciones de las emisiones de odorantes emitidas a la atmósfera

por el proyecto, en su condición más desfavorable.

 Definir el área de influencia del proyecto en términos del impacto de las

concentraciones de olor modelados.

 Determinar la concentración de olores en diversos puntos receptores representativos

de las zonas cercanas del proyecto.

 Realizar un análisis comparativo entre los resultados obtenidos en cuanto a

concentración de olores y la normativa internacional aplicable.

**3** **Antecedentes**

**3.1** **Geografía y topografía**

La Región Metropolitana se ubica entre los 32o55' y los 34o19' de latitud sur, y entre los

69°47’ y 71°43’ longitud oeste. El relieve que presenta esta región corresponde a tres

unidades que son de oriente a poniente, la Cordillera de los Andes, la Cuenca de Santiago

y la Cordillera de la Costa.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Figura 3. Elevación de terreno para la Región Metropolitana**



En la **Figura 3** se muestra la elevación de terreno para la Región Metropolitana, se observa

que la comuna de Lampa presenta elevaciones entre 1 y 500 m s.n.m y el proyecto se ubica

aproximadamente a 470 m s.n.m.

**3.2** **Meteorología**

El Proyecto se desarrollará en la Región Metropolitana, las principales características

climáticas que presenta la región corresponden a un clima tipo “mediterráneo” de estación

seca larga y con un invierno lluvioso. La temperatura media anual es de 13,9°C, en tanto

que el mes más cálido corresponde al mes de enero, alcanzando una temperatura de 22,1°C,

y el mes más frío corresponde al mes de julio con 7,7°C.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



En cuanto a la meteorología, para el análisis de variables meteorológicas, se hizo el análisis

de la estación Pudahuel, la cual se ilustra en la **Figura 4.** Esta estación se ubica a 12,6 km

del proyecto.

**Figura 4. Ubicación del proyecto y estación Pudahuel**

Para este análisis se utilizó la estación Pudahuel, pertenece a la Dirección Meteorológica de

Chile (DMC) y sus datos puedes se obtenidos a partir de la página web [2] del Instituto de

Investigaciones Agropecuarias (INIA).

**3.2.1** **Temperatura**

La **Figura 5** presenta la serie de tiempo para la variable temperatura para el año 2022. Este

gráfico facilita el análisis cualitativo de los datos, de manera de examinar la continuidad de

la serie, identificando periodos con datos faltantes, valores fuera de rango, problemas de

2 https://agrometeorologia.cl/

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



equipo (datos constantes y tendencias), y peaks relativos generados durante el periodo de

registro.

**Figura 5. Serie de tiempo para la variable temperatura medida en la estación**

**Pudahuel**

En la **Figura 5** se pueden observar las variaciones horarias para la temperatura, a su vez

se ve un marcado ciclo estacional, con aumentos en los meses estivales y disminuciones en

los meses de invierno. En promedio, la temperatura registrada es de 15,12°C.

En la **Figura 6** se presenta el ciclo diario de la temperatura. Se puede observar cómo la

temperatura varía a lo largo del día, alcanzando sus valores mínimos durante las primeras

horas de la mañana entre las 04:00 y 06:00 y aumentando gradualmente hasta alcanzar su

máximo en las horas de la tarde, cercano a las 14:00. Posteriormente, la temperatura

desciende nuevamente durante la noche.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 6. Ciclo diario de la variable temperatura medida en la estación Pudahuel**

El promedio en esta estación varía entre los 10°C y 22°C. Además, se muestra el rango del

90% de los datos, representando la variabilidad de la temperatura a lo largo del día. Este

rango proporciona una indicación de la dispersión de los valores, con la mayoría de los datos

concentrados dentro de este intervalo.

En la **Figura 7** se presenta el ciclo estacional de la temperatura, en el eje x se presenta las

horas del día y en el eje y los meses del año, los colores indican la variación de la

temperatura, lo que permite identificar los patrones estacionales y diurnos.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 7. Ciclo estacionar de la variable temperatura medida en la estación**

**Pudahuel**

Se puede observar un aumento de la temperatura durante los meses estivales,

especialmente entre las 10:00 y 19:00 horas, y una disminución durante los meses

invernales, con las temperaturas más bajas registradas durante la madrugada. Los valores

mínimos para invierno se presentan entre los 4°C y 10°C y las máximas rondan los 15°C,

mientras que para verano las mínimas rondan los 15°C y las máximas son cercanas a los

27°C. Este patrón estacional refleja la influencia del ciclo solar anual en la temperatura

diaria.

**3.2.2** **Precipitación**

La **Figura 8** presenta la serie de tiempo de la variable temperatura medida en la estación

Pudahuel. La precipitación acumulada anual es de 121,7 mm.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 8. Serie de tiempo para la variable Precipitación medida en la estación**

**Pudahuel**

En la serie temporal se observa que hay meses con precipitaciones casi nulas,

principalmente durante el período de primavera-verano. Además, se destaca que la mayor

parte de las precipitaciones se concentra entre junio y agosto, coincidiendo con la

temporada de invierno. También se identifican eventos puntuales de precipitaciones horarias

que pueden alcanzar hasta 5,5 mm, correspondientes al mes de abril.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 9. Precipitación acumulada mensual medida en la estación Pudahuel**

En cuanto a la distribución mensual, presentada en la **Figura 9**, se muestra que en las

cercanías del proyecto hay una precipitación concentrada entre los meses de junio y agosto.

La temporada estival registra los niveles más bajos de precipitación. Es importante destacar

que en julio se alcanza el máximo de precipitación, superando la suma total de la

precipitación acumulada en los demás meses.

**3.2.3** **Velocidad y dirección del viento**

La **Figura 10** presenta la serie de tiempo para las variables velocidad y dirección del viento.

El valor promedio de la velocidad del viento para el año 2022 es de 2,52 m/s, con máximos

alrededor de 10 m/s

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 10. Series de tiempo de las variables velocidad y rapidez del viento**

**medidas en la estación Alerce**

En esta misma figura se muestra también la serie de tiempo de dirección de viento, esta

forma de presentar la información es útil para identificar la cantidad de datos faltantes en

la información. Que en este caso permite observar la falta de mediciones durante los meses

de enero y febrero del año 2022.

El ciclo diario de la velocidad del viento se presenta en la **Figura 11** mostrando tanto el

promedio como el rango observado del 90% de los datos. Generalmente, la velocidad del

viento comienza a aumentar a las 10:00 horas, alcanzando su máximo a las 16:00 horas

con una velocidad de 4,5 m/s, y luego empieza a descender hasta las 02:00, momento en

el cual se estabiliza en 1,8 m/s.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 11. Ciclos diarios para las variables de velocidad y dirección del viento**

**medidas en la estación Pudahuel**

En la misma figura se muestra el porcentaje de tiempo que se tiene cada dirección del

viento. Durante la mayor parte de día se tienen direcciones cercanas a los 150°-200°, que

corresponde a sur. Esto se intensifica, con una mayor cantidad de viento de esta dirección

entre las 16:00 y 20:00 horas.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**4** **Marco regulatorio de olores**



Las emisiones odorantes son elementos perturbadores para la salud humana, entendida

ésta última en el sentido amplio del “completo bienestar físico, mental y social, y no

solamente la ausencia de afecciones o enfermedades” (OMS, 2005). El olor es un vector

ambiental que puede causar molestia y, al mismo tiempo afectar negativamente a la salud

y calidad de vida cuando la exposición es frecuente y repetida. Este vector se denomina

factores de estrés ambiental (Cohen, Evans, Stokols, & Krantz, 1986), ya que, a diferencia

de otros contaminantes, el olor puede causar efectos en la salud por debajo del nivel de un

daño físico real, pero su exposición constante causa un malestar agobiante, dando lugar a

efectos fisiológicos.

Los límites de inmisión y los factores de emisión son conceptos clave en la gestión de la

calidad del aire, pero tienen diferencias fundamentales. Los límites de inmisión se refieren

a las concentraciones máximas permitidas de un contaminante en el aire ambiente en un

área específica, establecidas para proteger la salud humana y el medio ambiente. Estos

límites son utilizados para evaluar la calidad del aire y asegurar que no se excedan niveles

perjudiciales de contaminación. Por otro lado, los factores de emisión son valores que

indican la cantidad de contaminante liberado a la atmósfera por una fuente específica, como

una fábrica o planta de tratamiento, por alguna actividad o producción. Estos factores se

utilizan para estimar las emisiones de contaminantes a partir de distintas fuentes, ayudando

a modelar y prever los impactos ambientales potenciales. Mientras que los límites de

inmisión se enfocan en la calidad del aire que respiran las personas, los factores de emisión

se centran en cuantificar las fuentes de contaminación.

A partir de los efectos en la salud y medio ambiente que pueden causar las emisiones

odorantes, se elabora la “Estrategia para la Gestión de Olores en Chile 2014-2017” por el

Ministerio del Medio Ambiente (2013, actualizada el 2017), que busca fortalecer el marco

regulatorio de olores, ya que en la actualidad no se cuenta con una normativa ambiental

aplicable a éstos. Uno de los puntos que destaca para mencionar la inexistencia de esta

normativa es la falta de antecedentes disponibles en el tema.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



En este contexto es que los últimos años el Ministerio del Medio Ambiente (MMA) ha

levantado información para fortalecer el marco regulatorio, dentro de la cual en el estudio

**“Antecedentes para la Regulación de Olores en Chile” de ECOTEC (2013)**, se

presentan más de 2.000 establecimientos que contienen actividades con el potencial de

generar olores.

Las normas de odorantes vigentes en otros países establecen límites máximos de

concentración de olores promedio horaria en unidad de olor, concepto que se define como

la cantidad de sustancia odorífera que, cuando se evapora en un metro cúbico de un gas

neutro en condiciones normales, originan una respuesta fisiológica de un panel equivalente

a la que origina una Masa de Olor de Referencia Europea (MORE) evaporada en un metro

cúbico de un gas neutro en condiciones normales.

**4.1** **Justificación normativa de comparación**

La regulación de emisiones de olores busca establecer límites específicos para emisiones

provenientes de industrias, empresas y hogares, con el fin de proteger la salud humana y

el medio ambiente. Estas normativas no solo fijan límites de emisión, sino que también

especifican métodos de medición y monitoreo de olores y sanciones para quienes incumplan

las regulaciones. Tener normas claras sobre olores es esencial para la evaluación de olores

que pueden generar molestias y reclamos. En resumen, una adecuada regulación de olores

es clave para la protección de la salud pública y el medio ambiente, así como para fomentar

una convivencia positiva y mejorar la calidad de vida.

En el caso de Chile, actualmente no existen normativas específicas para el control de olores;

sin embargo, las empresas y los ciudadanos deben cumplir con las regulaciones ambientales

generales que limitan las emisiones de contaminantes atmosféricos. Hasta la fecha, Chile

solo ha definido normas específicas de emisión de olores para la industria de crianza

intensiva de animales, en particular la industria porcina. Esta normativa, siendo la única de

su tipo a nivel nacional, no resulta directamente aplicable a todos los sectores, por lo que

es necesario revisar criterios internacionales para evaluar la calidad del aire en actividades

como las plantas de tratamiento de RILes. De hecho, el Artículo 11 de la Ley N° 19.300 en

Chile establece que, para evaluar si un proyecto implica riesgos para la salud, se deben

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



considerar las normas de calidad ambiental vigentes, tomando como referencia las

regulaciones de otros países, conforme a lo indicado en el Reglamento del SEIA.

La norma de referencia utilizada para la presente evaluación corresponde a la Ordenanza

Municipal de Calidad Odorífera del Aire NPE: A-240415-5055 de Alcantarilla, Murcia, España.

Esta norma consiste en definir los niveles de acuerdo con qué tan ofensivo es el olor, esto

significa que, a mayor ofensividad del olor, el umbral de sensibilidad es menor.

A continuación, en la **Tabla 2,** se presentan los límites asociados a diferentes actividades

generadoras de olor.

**Tabla 2. Norma de olores de referencia**

|Norma|Nivel de<br>ofensividad|Valor<br>[uo/m3]|Ejemplo|
|---|---|---|---|
|Percentil 98 del<br>promedio horario|Alta|1,5|Depuración tratamiento de aguas<br>residuales industriales, procesamiento de<br>grasas y aceites, aprovechamiento de<br>subproductos de origen animal, etc|
|Percentil 98 del<br>promedio horario|Media|3|Producción y fabricación de alimentos,<br>frituras, etc|
|Percentil 98 del<br>promedio horario|Baja|6|Cerveceras, fabricación industrial de pan,<br>pastelería, dulces y golosinas, etc|

De los valores propuestos por la norma española, se consideró adecuado elegir el grado de

ofensividad alta (1,5 uo/m [3] ) con el motivo de realizar una evaluación conservadora de la

norma. Para contextualizar, el valor en uo con respecto a la sensibilidad al olor, cabe

destacar que 1 uo/m [3] corresponde al nivel en que recién se comienza a percibir el olor, a

las 5 uo/m [3] el olor es suave y a las 10 uo/m [3] el olor ya es distintivo.

El límite de inmisión que define la norma española son 1,5 uo/m [3] . Finalmente, se entrega,

en el Anexo 2.4.2 de la presente adenda complementaria, un ejemplar de la norma de

referencia.

**Tabla 3. Límite normativo**



DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

|Estado|Límite de<br>inmisión<br>(uo/m3)|Forma de cálculo|Fuente|
|---|---|---|---|
|España|1,5|Como el percentil 98 de las<br>concentraciones horarias de un<br>año calendario.|Anexo<br>4 <br>de<br>la<br>Ordenanza<br>Municipal de Calidad Odorífera<br>del Aire NPE: A-240415-5055 de<br>Alcantarilla, Murcia, España|

Es importante destacar que esta norma de referencia resguarda el mismo objeto de

protección, en este caso, la salud de la población, tal como se analiza en este informe.

Además, regula los mismos contaminantes, específicamente el olor, y está diseñada para

actividades relacionadas con plantas de tratamiento, alineándose con las actividades del

presente proyecto. En comparación con otras normativas, esta norma de referencia

establece los umbrales de inmisión necesarios para determinar la condición más

desfavorable a la que podría estar expuesto el objeto de protección, asegurando así una

evaluación rigurosa y acorde a los estándares necesarios para proteger la salud de la

población.

**5** **Modelos utilizados**

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (2023) hace una serie de recomendaciones para la modelación de contaminantes

primarios [3] y secundarios en el aire. En la actualidad, esta guía es el único documento

existente como parámetro para la modelación de calidad del aire y tiene como objetivo

uniformar los criterios, exigencias técnicas y antecedentes para la evaluación de los impactos

asociados a este componente de proyectos que ingresen al Servicio de Evaluación

Ambiental. Dentro de las recomendaciones de la guía está el uso del modelo de dispersión

CALPUFF y sugiere utilizar el modelo meteorológico WRF, los cuales fueron utilizados en la

modelación de odorantes del proyecto.

A continuación, se presenta los modelos utilizados al modelar las emisiones del proyecto.

3 Los contaminantes primarios son los producidos directamente por la actividad humana o la naturaleza a la
atmósfera, dentro de los cuales caben las emisiones odorantes.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**5.1** **Modelo CALPUFF**

La modelación de dispersión atmosférica de olores provenientes del proyecto se realizó con

un modelo tipo “Puff”, específicamente el modelo CALPUFF. Tal como lo define la guía, los

modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos

Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes

provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su

aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada

punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria

por “puff”, lo que hace su cálculo mucho más rápido.

En el caso de emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana de

muchos “puffs”, como es en el caso de las emisiones de olor generadas por el proyecto.

Así mismo, el modelo CALPUFF es un modelo completo que incorpora herramientas para

procesar datos meteorológicos y geofísicos, modelos de dispersión y post procesamiento.

Dicho modelo es recomendado por la Agencia de Protección Ambiental de los Estados Unidos

(EPA) para modelar transporte a larga distancia de contaminantes.

CALPUFF se compone de tres módulos:

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento

y temperatura en una grilla de tres dimensiones. También asocia campos en dos

dimensiones de altura y usos de suelo. Este modelo fue reemplazado por el

WRF, tal como lo recomienda la guía antes citada.

 CALPUFF: Es un modelo de transporte y dispersión de partículas y gases

emitidos desde fuentes modeladas, simulando procesos de dispersión y

transformación. CALPUFF utiliza los datos generados por CALMET. Los archivos

de salida de CALPUFF contienen las concentraciones horarias o deposición por

hora de flujos evaluados en receptores seleccionados.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



 CALPOST: Es usado para procesar aquellos archivos generados por CALMET y

CALPUFF, produciendo tabulaciones que resumen los resultados de la

simulación. Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

**Ecuación 5.1**

[−d] 2σ y [2][a2] ~~[]]~~

Q
C=
2πσ x σ y

∗g∗exp

~~[~~ [−d] 2σ x [2][a2]

[−d] 2σ x [2][a2] [] ∗exp] ~~[[]~~ [−d] 2σ y [2][a2]

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Ecuación 5.2**

Dónde:

∞

2
g=

1
2 σ z

∑exp ~~[~~ [−(H] [e] 2σ [+ 2nh)] z [2] [2]

(2π ~~)~~

n=∞

[+ 2nh)] [2]

2σ z [2] ]

C, es concentración a nivel del suelo (g/m [3] )

Q, es masa de contaminantes (g) en la nube.

σ x, es desviación estándar de la distribución de Gauss en el viento a lo largo de la dirección.

σ y, es desviación estándar de la distribución de Gauss en el viento de costado

σ z, es desviación estándar de la distribución de Gauss en la dirección vertical.

d a, es distancia del centro de la nube al receptor en la dirección del viento a lo largo.

d c, es distancia del centro de la nube al receptor en la dirección de viento cruzado.

g, es el término vertical de la ecuación Gaussiana.

H, es la altura afectiva desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

El terreno en el cual se realizará la modelación de las emisiones odorantes se considera

heterogéneo, debido a las distintas unidades geomorfológicas. Por esta razón y en

consistencia con las recomendaciones del Servicio de Evaluación ambiental (SEA), para la

modelación en sus guías, se consideró utilizar el modelo CALPUFF para simular la dispersión

y concentración de la emisión de odorantes generadas por el proyecto.

**5.2** **Modelo Weather Research and Forecast (WRF)**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico de cuatro

dimensiones, recomendado para la generación de datos meteorológicos y es uno de los

modelos de pronóstico meteorológicos más avanzados. Debido a la falta de una red robusta

de estaciones meteorológicas, la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA” recomienda emplear WRF por sobre el uso del CALMET. Además, el mismo

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



documento, sugiere el uso del WRF para la modelación de dispersión de contaminantes con

CALPUFF.

**6** **Metodología**

De acuerdo con la “Guía para la predicción y evaluación de impactos por olor en el SEIA”,

(SEA, 2017), se puede realizar una estimación de las emisiones de odorantes de un proyecto

mediante dos metodologías, utilizando factores de emisión o emisiones de referencia. Si

bien, en dicha guía, establece que se debe priorizar la utilización de emisiones de referencia

por sobre los factores de emisión, también señala que podrán usarse factores de emisión o

valores de referencia, justificando la pertinencia y aplicabilidad al proyecto o actividad,

cuando se trate de un proyecto inexistente (ver sección 4.3 de la guía).

Es importante recordar que los límites de inmisión son las concentraciones máximas

permitidas de contaminantes en el aire para proteger la salud y el medio ambiente, mientras

que los factores de emisión cuantifican la cantidad de contaminantes liberados por una

fuente específica, como una fábrica, ayudando a estimar y modelar las emisiones.

Debido a que el proyecto presentado es un proyecto nuevo, y no es posible realizar una

olfatometría dinámica para saber el olor real emitido, es necesario usar factores de emisión.

Aunque, como se mencionó en el acápite 4.1, la normativa Española se emplea como

referencia para establecer los límites de inmisión debido a su relevancia en los estándares

ambientales locales, esta no proporciona factores de emisión específicos para procesos de

tratamiento de RILes. Por esta razón, se ha optado por utilizar los factores de emisión del

documento **“Netherlands Emission Guidelines for Air, Chapter 3.3 Special**

**Regulations for Specific Processes, Section G.3 "Sewage Treatment Installations,**

**abril 2003" (páginas 117 a 122)”** del cual se adjunta una copia en el Anexo 2.4.3.

Un factor de emisión es una relación entre la cantidad de contaminante emitido a la

atmósfera y una unidad de actividad. La unidad de actividad puede consistir en datos de

producción, horas de operación de la fuente, área superficial involucrada; o en datos como

número de empleados u otros (Radian Corporation, 1996). El uso de factores de emisión es

aconsejable solo en proyectos nuevos, y siempre que no se cuente con emisiones de

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



referencia, en este caso se deben utilizar preferentemente factores publicados por agencias

estatales de protección del medio ambiente, normas o guías técnicas relacionadas.

La ecuación general para la estimación de emisiones utilizando factores de emisión

corresponde a

**Ecuación 6.1**

E= A× EF

Donde E corresponde a las emisiones, A al nivel de actividad y EF al factor de emisión.

**6.1** **Subgrilla**

El modelo de dispersión CALPUFF por defecto crea una grilla de modelación partir del modelo

meteorológico, la cual tiene una resolución espacial de 1 km, con una dimensión de 57 km

x 57 km. Este modelo proporciona el valor promedio de concentración en la primera capa

de modelación, que abarca entre 0 y 20 metros sobre el nivel del suelo. Aunque esta grilla

inicial ofrece resultados generales, puede carecer de precisión en ciertos análisis. Por ello,

el modelo permite definir grillas de modelación personalizadas, especificando tanto la altura

(eje vertical) como el tamaño de las cuadrículas. Este enfoque es recomendado por la “GUÍA

PARA EL USO DE MODELOS DE CALIDAD DEL AIRE EN EL SEIA” (2023), que señala: “al

definir la subgrilla más adecuada para el proyecto, se debe asegurar que el tamaño de esta

sea lo suficientemente grande para garantizar la cuantificación de la concentración máxima

a nivel de suelo. El tamaño de la grilla requerida será específico del proyecto y variará según

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



las características de las fuentes, los factores geofísicos y las condiciones meteorológicas.”

**Figura 12. Subgrilla utilizada para la pluma de dispersión**

En este sentido, para la modelación de dispersión de partículas del proyecto, se adoptaron

las recomendaciones de la guía. Estas incluyen:

a. Definir una altura de 1,6 m, correspondiente a la altura a la que se evalúan las

concentraciones en los receptores discretos.

b. Generar una cuadrícula o grilla de modelación refinada, denominada subgrilla, con

el siguiente espaciado:

 **Subgrilla 1** : Con una resolución de 20 m, que se encuentra en la zona de

emplazamiento del proyecto y fue representado por los puntos amarillos en la

**Figura 12**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



 **Subgrilla 2** : Tiene una resolución de 50 m, se extiende por 500 m desde el centro

del proyecto y es representada por los puntos rosados en la **Figura 12.**

 **Subgrilla 3** : Tiene una resolución de 250 m, se extiende por 2.000 metros desde el

centro del proyecto y corresponde a los puntos celestes en la **Figura 12** .

**6.2** **Escenario de modelación**

Para el presente proyecto, se han considerado las fuentes de emisión descritas en la **Tabla**

**4** y mostradas en la **Figura 13**, detallando las características de cada fuente y su emisión

de olor.

**Figura 13. Ubicación fuentes de olor**

Dado que se trata de una planta nueva, no es posible realizar mediciones directas para

establecer los niveles de olor, por lo que, para esta modelación, se han utilizado valores de

factores de emisión basados en la literatura (documento **Netherlands Emission**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”,**

**sección G.3, “Sewage Treatment Installations”** ), es importante mencionar que estos

valores suponen un peor escenario. En la **Tabla 4** se presentan las ubicaciones y tipos de

fuentes las unidades del proyecto, específicamente seleccionados para plantas de

tratamiento residuos industriales líquidos.

El proceso de tratamiento de Residuos Industriales Líquidos (RILes) en la planta "AQUALIF"

se divide en varias etapas principales, diseñadas para asegurar la eficiencia en la remoción

de contaminantes y la producción de agua tratada de alta calidad. A continuación, se

describen las etapas clave de manera general:

1. **Recepción del RIL** : Los RILes son recibidos desde camiones cisterna. Se filtran los

sólidos gruesos y finos antes de almacenar el RIL en estanques acumuladores.

2. **Deshidratación** : El RIL se mezcla con lodo generado en el proceso y se somete a

neutralización y deshidratación. Se produce lodo deshidratado con un 25% de sólidos

y agua residual (cola).

3. **Tratamiento primario** : El agua residual es tratada para remover sólidos, aceites y

grasas mediante un desengrasador y un sistema de flotación por aire disuelto (DAF).

Esto permite una reducción significativa de los contaminantes sólidos y grasos.

4. **Tratamiento secundario** : Consiste en un tratamiento biológico con un Reactor de

Membrana (MBR), que utiliza filtración por membranas para remover la DBO 5 y otros

contaminantes orgánicos, obteniendo agua de alta calidad.

5. **Almacenamiento** : El agua tratada se almacena en estanques y se somete a un

proceso de desinfección con hipoclorito antes de su venta. La planta dispone de un

sistema de carga de camiones para la distribución del agua tratada.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Tabla 4. Fuentes de olor modeladas del proyecto**



|ID|Fuente|Coordenadas centrales UTM<br>(WGS-84 19S)|Col4|Tipo de<br>Fuente|Descripción de la fuente|Régimen de<br>funcionamiento|
|---|---|---|---|---|---|---|
|**ID**|**Fuente**|**Este (m)**|**Norte(m)**|**Norte(m)**|**Norte(m)**|**Norte(m)**|
|1|Cámara de elevación PTAS|329.523,38|6.308.821,39|Difusa|Recolección<br>de<br>aguas<br>residuales mediante una red<br>subterránea de alcantarillado.<br>Esta red descargará las aguas<br>a <br>un<br>estanque<br>de<br>acumulación, desde donde se<br>alimentará una planta de<br>tratamiento de aguas servidas<br>(PTAS), del tipo lodo activado.<br>Esta cuenta con una cámara<br>de elevación y dos tuberías<br>por las cuales podría emitirse<br>olor.|Todo el año|
|2|PTAS (tubería 1)|329.521,02|6.308.819,67|Difusa|Difusa|Todo el año|
|3|PTAS (tubería 1)|329.521,81|6.308.820,11|Difusa|Difusa|Todo el año|
|4|Filtrado sólidos gruesos|329.552,57|6.308.789,86|Difusa|Remover sólidos asimilables a<br>domiciliarios mediante una<br>rejilla gruesa|Todo el año|
|5|Fosa receptora (compuerta 1)|329.546,97|6.308.789,45|Difusa|Recibir todos los RILes crudos<br>posteriores<br>al<br>filtrado<br>de<br>solidos<br>gruesos<br>para<br>posteriormente ser tratados<br>por la planta de tratamiento.<br>La fosa receptora posee dos<br>aperturas, que se modelan<br>abiertas para considerar un<br>escenario conservador.|Todo el año|
|6|Fosa receptora (compuerta 2)|329.549,95|6.308.790,51|Difusa|Difusa|Todo el año|
|7|Estanque acumulador de RILes|329.547,08|6.308.803,25|Difusa|Almacenar los RILES, estos<br>estanques,<br>fabricados<br>en<br>polietileno lineal LLDPE, son|Todo el año|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|ID|Fuente|Coordenadas centrales UTM<br>(WGS-84 19S)|Col4|Tipo de<br>Fuente|Descripción de la fuente<br>cerrados. Para considerar un<br>escenario desfavorable, se<br>contempla la posible emisión<br>de olores a través de la tapa<br>superior de los estanques|Régimen de<br>funcionamiento|
|---|---|---|---|---|---|---|
|**ID**|**Fuente**|**Este (m)**|**Norte(m)**|**Norte(m)**|**Norte(m)**|**Norte(m)**|
|8|Estanque acumulador de RILes|329.542,26|6.308.801,52|Difusa|Difusa|Todo el año|
|9|Estanque acumulador de RILes|329.546,35|6.308.805,16|Difusa|Difusa|Todo el año|
|10|Ecualizadores de RILes|329.548,63|6.308.795,91|Difusa|Sistema<br>diseñado<br>para<br>mezclar y homogeneizar el<br>lodo antes de su tratamiento.|Todo el año|
|11|Ecualizadores de RILes|329.546,33|6.308.795,05|Difusa|Difusa|Todo el año|
|12|Deshidratador|329.530,59|6.308.792,48|Difusa|Extraer agua presente en el<br>RIL,<br>funciona<br>ejerciendo<br>trabajo mecánico, similar a un<br>estruje,<br>generando<br>una<br>compresión del lodo y por lo<br>tanto desaguando el agua|Todo el año|
|13|Desengrasador|329.534,08|6.308.793,46|Difusa|Este<br>a <br>través<br>de<br>la<br>incorporación de aire logra<br>que las partículas de grasas y<br>otras sean arrastradas hasta la<br>superficie|Todo el año|
|14|Flotación de aire disuelto (DAF)|329.531,79|6.308.796,36|Difusa|Sistema de flotación para el<br>tratamiento del RIL, realiza<br>actividades<br>como:<br>coagulación, ajuste de pH y<br>floculación.|Todo el año|
|15|Contenedor de lodos|329.528,23|6.308.789,63|Difusa||Todo el año|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|ID|Fuente|Coordenadas centrales UTM<br>(WGS-84 19S)|Col4|Tipo de<br>Fuente|Descripción de la fuente<br>Tolvas en las cuales se<br>almacena el lodo proveniente<br>del deshidratador.|Régimen de<br>funcionamiento|
|---|---|---|---|---|---|---|
|**ID**|**Fuente**|**Este (m)**|**Norte(m)**|**Norte(m)**|**Norte(m)**|**Norte(m)**|
|16|Contenedor de lodos|329.525,35|6.308.788,58|Difusa|Difusa|Todo el año|
|17|Cámara de agua cola|329.529,49|6.308.797,33|Difusa|“Agua cola” (fase líquida)<br>obtenida desde el proceso de<br>deshidratación.|Todo el año|
|18|Estanque de lodos|329.554,21|6.308.783,23|Difusa|Acumulación<br>de<br>lodos<br>extraídos.|Todo el año|
|19|Ecualizador secundario|329.550,04|6.308.781,68|Difusa|Sistema<br>diseñado<br>para<br>mezclar y homogeneizar el<br>lodo antes de su tratamiento.|Todo el año|
|20|Reactor biológico|329.544,41|6.308.768,38|Difusa|Se realiza el proceso de<br>tratamiento<br>biológico<br>mediante un Reactor Biológico<br>de Membrana (MBR). Para el<br>estanque de las membranas,<br>existirá<br>una<br>aireación<br>de<br>burbuja gruesa definida por el<br>proveedor de las membranas.|Todo el año|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**6.2.1** **Abatimiento**

Aunque la mayoría de las fuentes son unidades completamente cerradas, como se detalla

en los planos de detalle (Anexo 1.2 de la Adenda complementaria), ninguna de estas

unidades cuenta con un sistema activo de abatimiento de olores, como biofiltros, filtros de

carbón activado, scrubbers u otros. Las unidades abiertas, como los deshidratadores y el

sistema DAF, se encuentran dentro del edificio de producción, lo que ayuda a mitigar los

olores. Sin embargo, este estudio no consideró este factor para evaluar un escenario más

desfavorable, por lo que la percepción real de olores debería ser menor a la calculada.

**6.3** **Factores de emisión**

Como se señaló anteriormente, dado que este es un proyecto nuevo, se emplearán factores

de emisión para estimar las emisiones y evaluar la cantidad liberada a la atmósfera. Los

factores seleccionados están alineados con las actividades del proceso, y su justificación se

presenta en la **Tabla 7** .

Como se mencionó en el acápite 4.1, si bien, la normativa Española se emplea como

referencia para establecer los límites de inmisión debido a su relevancia en los estándares

ambientales locales, esta no proporciona factores de emisión específicos para procesos de

tratamiento de aguas residuales. En este caso, se utiliza como referencia el documento

**Netherlands Emission Guidelines for Air, capítulo 3.3, “Special Regulations for**

**Specific Processes”, sección G.3, “Sewage Treatment Installations”** (abril 2003,

páginas 117 a 122). Estos valores luego serán aplicados a un modelo de dispersión de olor

para evaluar esta variable en los receptores.

Para utilizar los valores propuestos en este documento correctamente, es necesario definir

dos parámetros clave para la adecuada selección de los factores de emisión. El primer

parámetro es el porcentaje del flujo que ingresa a la planta por gravedad (P), y el segundo

es el contenido de limo del afluente (S). Este último se define como la cantidad de materia

orgánica (por ejemplo, Demanda Biológica de Oxígeno - DBO) por kilogramo de sólidos

secos presentes en el agua residual, expresado en kg DBO/kg de sólidos secos por día.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



ara esta planta, se consideran dos valores de P: el primero corresponde al Sistema de

tratamiento particular de alcantarillado y el segundo al tratamiento de los RILes. En la **Tabla**

**5** se detallan los valores para cada situación junto con su justificación.

**Tabla 5. Valores del parámetro P (% del flujo que llega por gravedad) para los**

**diferentes procesos de la planta**

|Procesos|Parámetro P|Justificación|
|---|---|---|
|Sistema de<br>tratamiento particular<br>de alcantarillado|0|La recolección de las aguas residuales se realiza<br>mediante una red subterránea de alcantarillado, la<br>cual descarga en un estaque de acumulación, luego<br>una planta de elevación lleva estas aguas residuales<br>a la planta de tratamiento de aguas servidas del tipo<br>de lo activado. Por lo tanto, el agua es impulsada por<br>esta planta de elevación.|
|Tratamiento de RILes|100|El RIL es traído por camiones cisterna, los cuales<br>realizan sus descargas en un área específica de la<br>planta, adaptada para esta actividad, en donde el<br>flujo de descarga del RIL se realiza mediante<br>gravedad.|

El contenido de limo del afluente se calcula de la siguiente manera:

kg DBO por día
S=
kg de sólido secos por día

Se estima que la planta procesará una carga orgánica de 809 kg de DBO por día. Para

calcular los sólidos secos totales, se determina la masa horaria de los lodos deshidratados,

que es de 362 kg/h. Este valor se multiplica por 24 horas, obteniendo un total diario de

8.688 kg/día.

S=

809 [k][g][ DBO]

día

8.688 [k][g][ SST]

día

S= 0,09 [kg DBO]

kg SST día

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Tabla 6. Parámetros para la selección de los factores de emisión**



|Parámetro|Descripción|Valor|
|---|---|---|
|P|Porcentaje del flujo total que llega a planta por gravedad (%)|100|
|S|Contenido de limo del afluente|0,09|

A partir de los factores definidos en la **Tabla 6**, se establecieron los Factores de Emisión

(FE) que se presentan en la **Tabla 7** . Estos FE fueron determinados en función de los

criterios previamente descritos y servirán como referencia para el análisis de emisiones en

el sistema de tratamiento de la planta.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Tabla 7. Factores de emisión para cada una de las fuentes modeladas y su respectiva justificación**



|ID<br>modelo<br>4|Nombre fuente<br>emisora|Tipo<br>de<br>fuent<br>e|Tipo de<br>emisión|Factor de<br>Emisión<br>(uo /s m2)<br>e|Justificación|
|---|---|---|---|---|---|
|SRC_1|Cámara de<br>elevación|Área|Pasiva|65|Con la presente reformulación del proyecto, el sistema de alcantarillado, originalmente compuesto<br>por una fosa séptica, será sustituido por una planta de tratamiento de aguas servidas (PTAS). Para<br>más detalles, se puede consultar el Anexo 3.1 de la Adenda complementaria. Esta PTAS recibirá el<br>agua servida a través de una red subterránea, la cual pasará posteriormente por una cámara de<br>elevación.<br>El factor de emisión aplicado se ha basado en los valores especificados en la tabla 2 del documento<br>Netherlands Emission Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”,<br>sección G.3, “Sewage Treatment Installations”, aplicable a procesos de pretratamiento.<br>Considerando que todo el flujo llega mediante impulsión, se ha determinado como adecuado el uso<br>de un factor de emisión de 65, correspondiente al acceso y pretratamiento para esta condición<br>(100% impulsión)|
|SRC_2|PTAS (tubería 1)|Área|Pasiva|65|65|
|SRC_3|PTAS (tubería 2)|Área|Pasiva|65|65|
|SRC_4|Filtrado sólidos<br>gruesos|Área|Pasiva|9,5|Esta fuente de emisión corresponde a la recepción de los RILes, donde el 100% del afluente a<br>tratar llega por gravedad, descargado directamente desde camiones transporte de RIL. El factor de<br>emisión aplicado se refiere al agua pretratada, en la que solo se han filtrado los sólidos gruesos<br>presentes en el agua residual, antes de ser trasladada a la fosa receptora. El factor de emisión<br>utilizado se basa en los valores especificados en la tabla 2 del documento Netherlands Emission<br>Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”, sección G.3, “Sewage<br>Treatment Installations”. Este factor es aplicable a sistemas de pretratamiento, específicamente<br>para la remoción de material retenido en la rejilla de ingreso, considerando un flujo que llega por<br>gravedad al 100%.|
|SRC_5|Fosa receptora|Área|Activa|9,5|9,5|
|SRC_6|Fosa receptora|Área|Activa|9,5|9,5|
|SRC_7|Estanque<br>acumulador de<br>RILes|Área|Activa|9,5|Cabe destacar que, en este punto, las unidades aún no han pasado por el sistema de tratamiento<br>biológico. Por lo tanto, se utiliza el mismo factor de emisión aplicado al pretratamiento, ya que los|

4 ID modelo hace referencia al número asignado a la fuente en el modelo CALPUFF.



DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

|ID<br>modelo<br>4|Nombre fuente<br>emisora|Tipo<br>de<br>fuent<br>e|Tipo de<br>emisión|Factor de<br>Emisión<br>(uo /s m2)<br>e|Justificación|
|---|---|---|---|---|---|
|SRC_8|Estanque<br>acumulador de<br>RILes|Área|Activa|9,5|estanques acumuladores sirven para almacenar los RILes, mientras que los ecualizadores se<br>encargan de generar un lodo ecualizado. El factor de emisión utilizado se basa en los valores<br>especificados en la tabla 2 del documento Netherlands Emission Guidelines for Air, capítulo 3.3,<br>“Special Regulations for Specific Processes”, sección G.3, “Sewage Treatment Installations”. Este<br>factor es aplicable a sistemas de pretratamiento.|
|SRC_9|Estanque<br>acumulador de<br>RILes|Área|Pasiva|9,5|9,5|
|SRC_10|Ecualizadores de<br>RILes|Área|Pasiva|9,5|9,5|
|SRC_11|Ecualizadores de<br>RILes|Área|Pasiva|9,5|9,5|
|SRC_12|Deshidratador|Área|Pasiva|8,0|El factor de emisión utilizado se basa en los valores especificados en la tabla 4 del documento<br>Netherlands Emission Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”,<br>sección G.3, “Sewage Treatment Installations”, aplicable a la línea de lodos, correspondiente al<br>sistema de pre-deshidratación, para lodos mezclados, este valor es el mayor de su categoría para<br>garantizar la evaluación de un peor escenario.|
|SRC_13|Desengrasador|Área|Pasiva|5,5|El sistema de desengrasadores emplea un factor de emisión basado en los valores especificados<br>en la tabla 2 del documento Netherlands Emission Guidelines for Air, capítulo 3.3, “Special<br>Regulations for Specific Processes”, sección G.3, “Sewage Treatment Installations”. Este factor es<br>aplicable al separador de partículas, ya que esta unidad, mediante la incorporación de aire, facilita<br>el arrastre de las partículas de grasa y otras sustancias hacia la superficie.|
|SRC_14|Flotación de aire<br>disuelto (DAF)|Área|Pasiva|0,55|El sistema de flotación para el tratamiento de los RILes utiliza un factor de emisión basado en los<br>valores especificados en la tabla 3 del documento Netherlands Emission Guidelines for Air, capítulo<br>3.3, “Special Regulations for Specific Processes”, sección G.3, “Sewage Treatment Installations”.<br>Este factor es aplicable a la línea de agua, específicamente para emisiones de olores en estanques<br>de aireación abiertos con aireación sin cobertura, en una zona aeróbica.|
|SRC_15|Contenedor de<br>lodos|Área|Pasiva|4,35|Los contenedores de lodos reciben el lodo extraído del proceso de deshidratación. Por este motivo,<br>se utiliza el factor de emisión especificado en la tabla 4 del documento Netherlands Emission<br>Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”, sección G.3, “Sewage<br>Treatment Installations”. Este factor corresponde a la línea de lodo, específicamente para la laguna<br>de deshidratación y almacenamiento de lodo.|
|SRC_16|Contenedor de<br>lodos|Área|Pasiva|4,35|4,35|



DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

|ID<br>modelo<br>4|Nombre fuente<br>emisora|Tipo<br>de<br>fuent<br>e|Tipo de<br>emisión|Factor de<br>Emisión<br>(uo /s m2)<br>e|Justificación|
|---|---|---|---|---|---|
|SRC_17|Cámara de agua<br>cola|Área|Pasiva|1,1|Agua obtenida del proceso de deshidratación y recolectada gravitacionalmente hacia una cámara<br>de elevación. El factor de emisión utilizado está especificado en la tabla 3 del documento<br>Netherlands Emission Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”,<br>sección G.3, “Sewage Treatment Installations”. Se emplea el factor de emisión relacionado con la<br>línea de agua, específicamente para la estación de bombeo.|
|SRC_18|Estanque de<br>lodos|Área|Pasiva|4,35|Los contenedores de lodos reciben el lodo extraído del proceso de deshidratación. Por este motivo,<br>se utiliza el factor de emisión especificado en la tabla 4 del documento Netherlands Emission<br>Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”, sección G.3, “Sewage<br>Treatment Installations”. Este factor corresponde a la línea de lodo, específicamente para la laguna<br>de deshidratación y almacenamiento de lodo.|
|SRC_19|Ecualizador<br>secundario|Área|Pasiva|1,1|El estanque que recibe el agua impulsada por la cámara de agua cola utiliza el mismo factor de<br>emisión que dicha fuente, ya que no ha habido cambios en la naturaleza del afluente a tratar. El<br>factor de emisión aplicado está especificado en la tabla 3 del documento Netherlands Emission<br>Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”, sección G.3, “Sewage<br>Treatment Installations”. Este factor corresponde a la línea de agua, específicamente para la<br>estación de bombeo.|
|SRC_20|Reactor biológico|Área|Pasiva|0,55|Combina procesos biológicos con filtración por membranas, lo que permite una alta eficiencia en la<br>eliminación de contaminantes orgánicos y sólidos suspendidos. Los reactores contarán con un<br>sistema de aireación de burbuja fina. Dado que el reactor es una unidad abierta, se aplica el factor<br>de emisión relacionado con la línea de agua y la aireación en punto único sin cobertura, tal como<br>se especifica en la tabla 3 del documento Netherlands Emission Guidelines for Air, capítulo 3.3,<br>“Special Regulations for Specific Processes”, sección G.3, “Sewage Treatment Installations”.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**6.4** **Receptores**

Se consideraron 32 puntos discretos cercanos al proyecto. A continuación, se presenta en

la **Tabla 8** las coordenadas, y en la **Figura 14** la distribución espacial de los receptores

discretos.

**Tabla 8. Receptores cercanos al proyecto**

|Receptor|Coordenada UTM HUSO<br>19 S (m)|Col3|Distancia al<br>centro<br>del proyecto<br>(m)|Descripción|
|---|---|---|---|---|
|**Receptor**|**Este**|**Norte**|**Norte**|**Norte**|
|Est_1|339.594|6.308.625|10.048|Estación Quilicura (SINCA)|
|R_1|329.847|6.308.901|322|Vivenda Chorillo 2|
|R_2|329.797|6.308.956|304|Vivenda Chorillo 2|
|R_3|329.798|6.309.035|354|Parcela Chorrillo 2|
|R_4|329.901|6.309.227|569|Parcela El Descanso|
|R_5|330.120|6.308.520|631|Parcela Chorrillo 2|
|R_6|329.848|6.308.231|629|Parcela Chorrillo 1|
|R_7|328.789|6.308.470|820|Vivienda El Noviciado|
|R_8|328.756|6.308.676|800|Vivienda El Noviciado|
|R_9|328.721|6.308.764|826|Vivienda El Noviciado|
|R_10|328.511|6.308.854|1.037|Vivienda El Noviciado|
|R_11|328.799|6.309.102|813|Vivienda El Noviciado|
|R_12|328.708|6.309.242|956|Vivienda El Noviciado|
|R_13|328.789|6.309.241|885|Vivienda El Noviciado|
|R_14|328.815|6.309.391|951|Vivienda El Noviciado|
|R_15|329.125|6.309.462|800|Parcela El Noviciado|
|R_16|330.357|6.309.052|853|Parcela Chorrillo 3|
|R_17|330.223|6.309.088|743|Parcela Chorrillo 3|
|R_18|328.810|6.309.334|919|Vivienda El Noviciado|
|R_19|329.830|6.309.144|462|Parcela Chorrillo 2|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Receptor|Coordenada UTM HUSO<br>19 S (m)|Col3|Distancia al<br>centro<br>del proyecto<br>(m)|Descripción|
|---|---|---|---|---|
|**Receptor**|**Este**|**Norte**|**Norte**|**Norte**|
|R_20|328.568|6.309.072|1.019|Parcela El Noviciado|
|R_21|330.569|6.308.277|1.140|Vivenda Chorillo 3|
|R_22|330.695|6.308.910|1.154|Vivenda Chorillo 3|
|R_23|330.401|6.309.495|1.109|Parcela Chorrillo 3|
|R_24|330.144|6.309.841|1.215|Parcela Chorrillo 2|
|R_25|328.838|6.310.065|1.465|Vivienda El Noviciado|
|R_26|328.433|6.310.030|1.672|Vivienda Agrícola|
|R_27|329.037|6.310.208|1.514|Parcela El Noviciado|
|R_28|328.613|6.310.254|1.747|Condominio Miraflores de Lipangue|
|R_29|328.744|6.309.510|1.086|Vivienda El Noviciado|
|R_30|326.940|6.310.150|2.934|Vivienda Lipangue|
|R_31|330.780|6.309.632|1.495|Vivienda Parecelación Miraflores|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 14. Ubicación de los receptores discretos cercanos al proyecto**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**7** **Estimación de emisiones de olor**



La estimación de emisiones de odorantes se realizó en base a la información presentada en

el acápite 5.1, en donde se consideraron factores de emisión obtenidos de la Tabla 2, 3 y 4

del documento **Netherlands Emission Guidelines for Air, capítulo 3.3, “Special**

**Regulations** **for** **Specific Processes”,** **sección G.3,** **“Sewage** **Treatment**

**Installations”**, que fueron resumidos en la Tabla 9 del presente informe.

La Tasa de Emisión Total de Olor (TEO) (uo/s) para las fuentes superficiales, presentada en

la Tabla 9, se calcula multiplicando la Tasa de Emisión por Área (uo/m2·s) por el área

transversal de la fuente (m2). Se adjunta el Anexo 2.4.4 Unidades y Factores de emisión,

que muestra la memoria de cálculo para dicha tasa de emisión

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Tabla 9. Estimación de emisiones odorantes**



|ID|Nombre fuente emisora|Tipo<br>de<br>Fuente|Tipo de<br>emisión|Factor de emisión e (uo /m2)|Área<br>(m2)|TEO<br>(uo /s)<br>e|Referencia|País de<br>proceden<br>cia|
|---|---|---|---|---|---|---|---|---|
|SRC_1|Cámara de elevación|Área|Pasiva|65,00|2,25|146,25|Netherlands<br>Emission<br>Guidelines for Air,<br>Chapter 3.3<br>Special<br>Regulations for<br>Specific<br>Processes,<br>Section G.3<br>"Sewage<br>Treatment<br>Installations, Abril<br>2003" (páginas<br>117 a 122)|Países<br>Bajos|
|SRC_2|PTAS (tuberia 1)|Área|Pasiva|65,00|0,01|0,62|0,62|0,62|
|SRC_3|PTAS (tuberia 1)|Área|Pasiva|65,00|0,01|0,62|0,62|0,62|
|SRC_4|Filtrado sólidos gruesos|Área|Pasiva|9,50|3,00|28,50|28,50|28,50|
|SRC_5|Fosa receptora|Área|Pasiva|9,50|1,04|9,88|9,88|9,88|
|SRC_6|Fosa receptora|Área|Pasiva|9,50|0,64|6,08|6,08|6,08|
|SRC_7|Estanque acumulador de RILes|Área|Pasiva|9,50|0,29|2,77|2,77|2,77|
|SRC_8|Estanque acumulador de RILes|Área|Pasiva|9,50|0,29|2,77|2,77|2,77|
|SRC_9|Estanque acumulador de RILes|Área|Pasiva|9,50|0,29|2,77|2,77|2,77|
|SRC_10|Ecualizadores de RILes|Área|Pasiva|9,50|0,29|2,77|2,77|2,77|
|SRC_11|Ecualizadores de RILes|Área|Pasiva|9,50|0,29|2,77|2,77|2,77|
|SRC_12|Deshidratador|Área|Pasiva|8,00|1,92|15,37|15,37|15,37|
|SRC_13|Desengrasador|Área|Pasiva|5,50|7,07|38,86|38,86|38,86|
|SRC_14|Flotación de aire disuelto (DAF)|Área|Pasiva|0,55|2,44|1,34|1,34|1,34|
|SRC_15|Contenedor de lodos|Área|Pasiva|4,35|5,08|22,11|22,11|22,11|
|SRC_16|Contenedor de lodos|Área|Pasiva|4,35|5,08|22,11|22,11|22,11|
|SRC_17|Cámara de agua cola|Área|Pasiva|1,10|13,00|14,30|14,30|14,30|
|SRC_18|Estanque de lodos|Área|Pasiva|4,35|0,29|1,27|1,27|1,27|
|SRC_19|Ecualizador secundario|Área|Pasiva|1,10|0,29|0,32|0,32|0,32|
|SRC_20|Reactor biológico|Área|Pasiva|0,55|132,00|72,60|||

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|ID|Nombre fuente emisora|Tipo<br>de<br>Fuente|Tipo de<br>emisión|Factor de emisión e (uo /m2)|Área<br>(m2)|TEO<br>(uo /s)<br>e|Referencia|País de<br>proceden<br>cia|
|---|---|---|---|---|---|---|---|---|
|**TOTAL EMISIONES**|**TOTAL EMISIONES**|**TOTAL EMISIONES**|**TOTAL EMISIONES**|**TOTAL EMISIONES**|**TOTAL EMISIONES**|**394,10**|||

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



En los resultados presentados en la **Tabla 9 y Tabla** **10**, se observa que las mayores

emisiones corresponden a la cámara de elevación de la PTAS y al reactor biológico, este

último es una sección clave en la planta de tratamiento de RILes donde se realiza el proceso

de tratamiento biológico, permitiendo una alta eficiencia en la remoción de contaminantes

orgánicos y sólidos suspendidos. Ambas unidades mencionadas configuran el 55,5% de las

emisiones de olor.

**Tabla 10. Ranking de las unidades generadoras de olor**

|Nombre unidad|TEO (uo/s)|% TEO|
|---|---|---|
|Cámara de elevación PTAS|146,25|37,11|
|Reactor biológico|72,60|18,42|
|Desengrasador|38,86|9,86|
|Filtrado sólidos gruesos|28,50|7,23|
|Contenedor de lodos|22,11|5,61|
|Contenedor de lodos|22,11|5,61|
|Deshidratador|15,37|3,90|
|Cámara de agua cola|14,30|3,63|
|Fosa receptora|9,88|2,51|
|Fosa receptora|6,08|1,54|
|Estanque acumulador de RILes|2,77|0,70|
|Estanque acumulador de RILes|2,77|0,70|
|Estanque acumulador de RILes|2,77|0,70|
|Ecualizadores de RILes|2,77|0,70|
|Ecualizadores de RILes|2,77|0,70|
|Flotación de aire disuelto (DAF)|1,34|0,34|
|Estanque de lodos|1,27|0,32|
|PTAS (tuberia 1)|0,62|0,16|
|PTAS (tuberia 1)|0,62|0,16|
|Ecualizador secundario|0,32|0,08|
|**TOTAL**|**394,10**|**394,10**|

Finalmente, se hace hincapié en que, al considerar factores de emisión teóricos, los que en

la práctica han resultado mayores que los factores de emisión de referencia, que derivan de

mediciones in-situ, se está sobreestimado las emisiones a la atmósfera y por lo tanto

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

considerando un escenario desfavorable.

**8** **Modelación meteorológica**



Existen dos tipos de datos meteorológicos: datos observados y datos generados por un

modelo numérico. En todos los tipos de modelaciones de calidad del aire se requiere de al

menos uno de estos datos.

Por otro lado, el modelo numérico recomendado para la generación de datos meteorológicos

es WRF (Weather Research and Forecasting Model, por sus siglas en inglés). Este modelo

es uno de los simuladores meteorológicos de pronóstico más avanzados, completos y en

constante mejora, mantenido por NCAR/NOAA de Estados Unidos. Además, ha sido utilizado

en la mayoría de los proyectos relacionados con el comportamiento atmosférico encargados

por la Comisión Nacional de Energía, Ministerio del Medio Ambiente, entre otros

El modelo WRF abarca un área de aproximada de 3.248 km [2], y presenta una grilla de 1 km

de resolución. El centroide se presenta en la **Tabla 11** y se encuentra a una distancia de

8,3 km del centro del proyecto. En la **Figura 15** se presenta la ubicación espacial del

centroide del modelo WRF y la ubicación del proyecto.

A su vez, de acuerdo con lo solicitado en la observación 4.2.1.4 del ICSARA, se utiliza el año

2022, para realizar la modelación meteorológica WRF, el cual corresponde al año previo al

ingreso del Proyecto al SEIA.

**Tabla 11. Coordenadas del centroide del modelo WRF**

|WSG 84 - 19 S|Col2|
|---|---|
|**UTM E (m)**|**UTM N (m)**|
|330.217|6.316.965|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Figura 15. Centroide y extensión del modelo WRF**

**8.1** **Análisis de incertidumbre**



Tal como se plantea en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2023) de manera textual “cualquier modelo (meteorológico o de calidad del aire) representa

una aproximación a la realidad y, en consecuencia, sus resultados tienen incertidumbres

asociadas”. Ante lo cual, para cuantificar esta incertidumbre, se realiza un análisis entre los

valores entregados por el modelo WRF (valores meteorológicos) y valores observados. En

este caso los datos son extraídos de la **Estación Pudahuel** de la Red Agrometeorológica

del INIA, correspondiente a la estación meteorológica más cercana al proyecto y con datos

disponibles superiores al 75% para el año 2022, mismo año de modelación del modelo WRF.

El modelo WRF simuló las condiciones meteorológicas dentro de un rango de 57 x 57 km

celdas de una dimensión de 1 x 1 km. Para efectos del análisis del ajuste de los datos

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



meteorológicos modelados se seleccionó una celda en donde se ubica la estación a analizar,

de donde se extrajeron los datos y se compararon con los valores observados.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados, método

en el que existen dos parámetros principales: el coeficiente de correlación lineal de Pearson

(r) y el coeficiente de determinación ( R [2] ).

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos variables

y se usa para medir el grado de relación entre ellas. El rango de valores va desde el -1 al 1

y está representado por la siguiente ecuación.

r = [σ] [x][y]
xy

σ x . σ y

Donde,

 - σ xy, es la covarianza entre x e y;

 - σx, es la desviación estándar de x;

 σy, es la desviación estándar de y.

El coeficiente de determinación se utiliza como medida de eficiencia de la cobertura de datos

midiendo el porcentaje de variación entre las variables observadas y modeladas, es decir,

testea la capacidad predictiva del modelo e indica la proporción de la varianza de los

resultados que puede ser explicado por el modelo. Los valores del coeficiente de

determinación varían de 0 a 1, siendo este último el valor óptimo y está determinada por la

siguiente relación.

R [2] = r 2
xy
= (

Donde,

 - - σ xy, es la covarianza entre x e y;

 - - σ x, es la desviación estándar de x;

 - - σ y, es la desviación estándar de y.

σ xy

σ x . σ y

) 2

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



Se presenta el análisis de tendencia de los valores modelados a estar sobredimensionados

o subdimensionados respecto de los observados, a través del BIAS, el valor óptimo es 0 y

su cálculo se realiza según la siguiente ecuación.

n

BIAS = [1]

n [∑(S] [i] [−O] [i] [)]

i=1

Donde,

 - S i, es el valor modelado;

 - O i, es el valor observado;

 - n, es el número de mediciones, en este caso el número de horas en un año, es decir,

8.760 horas.

Se presenta el Mean Absolute Error (MAE), el cual es una medida del error promedio

absoluto del modelo con respecto a las observaciones. Este estadístico se calcula mediante

a la siguiente formula.

n

MAE = [1]

n [∑|S] [i] [−O] [i] [|]

i=1

Donde,

 - S i, es el valor modelado;

 - O i, es el valor observado;

 - n, es el número de mediciones, en este caso el número de horas en un año, es decir,

8.760 horas.

El Root Mean Squeare Error (RMSE) es una medida del desempeño promedio del modelo,

el cual, según él SEA, es un “estimador de la frecuencia de las diferencias entre los valores

observados y modelados, siendo especialmente sensible a los valores atípicos, por lo tanto,

a mayor diferencia entre estos valores menor será el grado de ajuste de este estadístico”.

Esta estadística toma valores de 0 al infinito, donde 0 es el valor de una modelación sin

errores y va creciendo a medida que decrece la capacidad del modelo de representar la

realidad.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



n

RMSE = √ [1]

n

n [∑(S] [i] [−O] [i] [)] [2]

i=1

**8.1.1** **Análisis cuantitativo**

Como parte del análisis de incertidumbre se analizaron los datos observados de la estación

Pudahuel, centrados principalmente en la velocidad del viento y la temperatura. En la Tabla

12 se observa que, en relación con la temperatura, se ve claramente como el modelo cumple

con todas las condiciones “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2023) en todas las estaciones analizadas.

Con respecto a la velocidad del viento, la estación Pudahuel cumplen con todos los criterios

establecidos en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (2023),

salvo la correlación, que es ligeramente menor. Esto nos indica que el margen de error con

respecto a la intensidad de la velocidad del viento y la capacidad con que el modelo

representa la variabilidad observada se encuentra dentro de los parámetros esperados.

**Tabla 12. Resultados estadísticos obtenidos por la modelación respecto a las**
**estaciones emplazadas dentro del dominio de modelación aledañas al proyecto**

|Estadístico|Criterio guía modelación<br>SEA|Estación Pudahuel|
|---|---|---|
|**Temperatura (°C)**|**Temperatura (°C)**|**Temperatura (°C)**|
|Correlación lineal (r)|**>0,8**|0,95|
|Coeficiente de determinación (r2)|**- **|0,90|
|BIAS|**[-4, 4]**|0,62|
|MAE|**≤ 4**|1,88|
|RMSE|**≤ 4,5**|2,48|
|**Velocidad del viento (m/s)**|**Velocidad del viento (m/s)**|**Velocidad del viento (m/s)**|
|Correlación lineal (r)|**>0,6**|0,49|
|Coeficiente de determinación (r2)|**- **|0,24|
|BIAS|**[-2,5, 2,5]**|0,2|
|MAE|**≤ 3**|1,57|
|RMSE|**≤3,5**|2,31|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**8.1.2** **Análisis cualitativo**

**8.1.2.1** **Caracterización de la temperatura modelada y observada**

En la Tabla 13 se presenta la caracterización entre la temperatura horaria observada en la

estación Pudahuel y las modeladas por el modelo WRF del año 2022.

**Tabla 13. Temperatura modelada y observada en estación Pudahuel**

|Col1|Temperatura modelada y observada|Características|
|---|---|---|
|**Serie de tiempo**||-En<br>la<br>figura<br>se<br>presenta<br>la<br>temperatura<br>observada<br>en<br>la<br>estación Pudahuel (superior) y la<br>modelada en el punto de grilla donde<br>se ubica la estación (inferior). La<br>cantidad<br>de<br>disponibles<br>de<br>la<br>estación corresponde a 99,98% lo<br>que queda en evidencia de acuerdo<br>con lo observado.<br>-Se observa que el modelo logra<br>representar de manera robusta el<br>comportamiento observado en la<br>estación Pudahuel.|
|**Correlación**||-La temperatura modelada tiene una<br>correlación<br>significativa<br>con<br>los<br>valores observados en la estación<br>Pudahuel, cuyo valor es de 0,95.<br>-A<br>su<br>vez,<br>el<br>coeficiente<br>de<br>determinación sugiere que el modelo<br>es capaz de representar el 90% de la<br>variabilidad observada (R2 = 0,90).|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Temperatura modelada y observada|Características|
|---|---|---|
|**Frecuencia**||- Se observa que en general el<br>modelo tiene pocas diferencias con<br>las<br>observaciones,<br>siendo<br>las<br>temperaturas en rango de 0 a 10°C<br>y 10 a 20°C las más modeladas, con<br>diferencia -6,4% y +6,3% con<br>respecto<br>a <br>las<br>observaciones,<br>respectivamente.<br>-El valor del BIAS nos indica que la<br>temperatura promedio modelada es<br>0,62°C mayor a la observada.|
|**Ciclo promedio diario**||-La figura nos presenta el ciclo<br>promedio diario de la temperatura en<br>todo el periodo analizado, para los<br>datos simulados (línea azul) como la<br>data observada (línea roja).<br>-En términos generales, el modelo<br>logra una sólida representación de la<br>variabilidad diaria, evidenciada por<br>una correlación de 1,0.<br>-Se observa como la temperatura<br>diaria observada es menor entre las<br>0 horas y las 10 horas y entre las 19<br>horas hasta completar el ciclo a las 0<br>horas.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Temperatura modelada y observada|Características|
|---|---|---|
|**Ciclo promedio diario y mensual**||-La figura presenta el ciclo diario<br>mensual<br>de<br>la<br>temperatura<br>observada (superior) y modelada en<br>WRF (inferior), para el año 2022.<br>-Se puede observar que el modelo<br>reproduce de manera sólida el ciclo<br>diario de las temperaturas y su<br>variabilidad mensual.<br>-Es evidente que el modelo refleja<br>adecuadamente la variación mensual<br>del ciclo diario observado. Además,<br>se aprecia que las temperaturas<br>tienden a ser más altas durante las<br>primeras horas de la mañana en el<br>modelo.|

**8.1.2.2** **Caracterización de la velocidad del viento modelada y observada**

En **Tabla 14** se presenta la caracterización entre la velocidad del viento horaria observada

en la estación **Pudahuel** y las modelada por el modelo WRF del año **2022** .

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Tabla 14. Velocidad del viento modelada y observada en estación Pudahuel**

|Col1|Velocidad del viento modelada y observada|Características|
|---|---|---|
|**Series de tiempo**||-En la figura se presenta la velocidad<br>del viento observada en la estación<br>Pudahuel (superior) y la modelada<br>en el punto de grilla donde se ubica<br>la estación (inferior). Contemplando<br>la estación una disponibilidad de<br>datos del 99,98%.<br>-Se observa que el modelo logra<br>representar de manera robusta la<br>variabilidad estación.<br>-Aunque no se observa una pérdida<br>significativa de datos, se evidencia<br>que, durante los meses de enero y<br>febrero,<br>la<br>estación<br>simula<br>exclusivamente velocidades calmas<br>de 0 m/s. Es importante señalar que<br>estos<br>valores<br>de<br>0 <br>m/s<br>probablemente<br>corresponden<br>a <br>errores en la estación y deberían<br>considerarse como datos faltantes.<br>Sin embargo, no se realizó este<br>ajuste debido a la falta de certeza,<br>lo que afecta los estadísticos y<br>puede ser una de las razones por las<br>que la correlación no cumple con el<br>criterio.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Velocidad del viento modelada y observada|Col3|Características|
|---|---|---|---|
|**Correlación**|||-De la figura se observa que existe<br>una correlación positiva entre la<br>velocidad del viento observada y la<br>modelada, siendo el valor del<br>coeficiente de correlación lineal de<br>0,5.<br>-Por otro lado, el coeficiente de<br>determinación<br>sugiere<br>que<br>el<br>modelo es capaz de representar el<br>20% del comportamiento observado<br>(R2 = 0,2).|
|**Frecuencia**|||-De la frecuencia de magnitudes de<br>velocidad del viento en distintas<br>categorías, se identifica claramente<br>como el modelo representa de<br>forma muy sólida la magnitud de la<br>velocidad del viento observada.<br>-El valor del BIAS nos indica que la<br>velocidad del viento modelada es<br>0,2 m/s superior a la observada.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Velocidad del viento modelada y observada|Características|
|---|---|---|
|**Ciclo promedio diario**||-La figura nos presenta el ciclo<br>promedio diario de la rapidez del<br>viento en todo el periodo analizado,<br>para los datos simulados (línea azul)<br>como la data observada (línea roja).<br>-En términos generales, el modelo<br>logra una sólida representación de la<br>variabilidad diaria, evidenciada por<br>una correlación de 1,0.<br>-Se aprecia que la velocidad del<br>viento modelada es menor a la<br>observada antes de las 13 horas,<br>luego<br>la<br>velocidad<br>del<br>viento<br>modelada es mayor hasta completar<br>el ciclo|
|**Ciclo promedio diario y mensual**||-La figura presenta el ciclo diario<br>mensual de la velocidad del viento<br>observada (superior) y modelada en<br>WRF (inferior), para el año 2022.<br>-Se destaca, nuevamente que la<br>estación Pudahuel cuenta con datos<br>0 para enero y febrero pueden<br>afectar el análisis.<br>-Se observa que el ciclo diario<br>observado y modelado están en fase<br>durante todo el periodo, provocando<br>que los máximos y mínimos se den<br>la hora correspondiente.<br>-Por<br>otra<br>parte,<br>los<br>patrones<br>mensuales son representados de<br>buena manera.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**8.1.2.3** **Caracterización de la dirección del viento modelada y observada**



En Tabla 15 se presenta la caracterización entre la rapidez del viento horaria observada en

la estación Pudahuel y las modelada por el modelo WRF del año 2022.

**Tabla 15. Dirección del viento modelada y observada en estación Pudahuel**

|Col1|Dirección del viento modelada y observada|Características|
|---|---|---|
|**Series de tiempo**||-En la figura se presenta la rapidez<br>del viento observada en la estación<br>Pudahuel (superior) y la modelada<br>en el punto de grilla donde se ubica<br>la estación (inferior). Existiendo en<br>la estación un 99,98% de los datos<br>anuales.<br>-Se<br>evidencia<br>que,<br>como<br>fue<br>mencionado con la velocidad del<br>viento,<br>no<br>hay<br>una<br>perdida<br>significativa de datos en la estación<br>de monitoreo, pero se observa como<br>los datos del mes de enero y parte<br>de febrero son 0° constantemente.<br>- Es importante señalar que estos<br>valores<br>de<br>0°<br>probablemente<br>corresponden a errores en la<br>estación y deberían considerarse<br>como datos faltantes. Sin embargo,<br>no se realizó este ajuste debido a la<br>falta de certeza, lo que afecta los<br>estadísticos y puede ser una de las<br>razones por las que la correlación no<br>cumple con el criterio.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Dirección del viento modelada y observada|Características|
|---|---|---|
|**Correlación**||-El modelo reproduce de manera<br>moderada la dirección del viento.<br>-Las mayores discrepancias entre las<br>observaciones y la modelación se<br>dan antes de las 7:00 horas.<br>-El<br>resto<br>del<br>día<br>el<br>modelo<br>representa de manera sólida las<br>observaciones.|
|**Frecuencia**||-Se observa que el comportamiento<br>observado<br>en<br>el<br>ciclo<br>diario<br>promedio es consistente a lo medido<br>en la estación durante todo el año,<br>salvo en los meses de enero y<br>febrero.<br>-En<br>general,<br>vemos<br>una<br>predominancia de viento del norte<br>en las mañanas, mientras que en<br>horas de la tarde la componente<br>predominante es sur.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Dirección del viento modelada y observada|Características|
|---|---|---|
|**Ciclo promedio diario**||-La figura nos presenta la rosa del<br>viento<br>observado<br>(derecha)<br>y <br>modelada (izquierda)<br>-Se aprecia que el modelo logra una<br>representación<br>sólida<br>de<br>las<br>principales direcciones del viento<br>observadas, excepto en la dirección<br>norte, que está subestimada. Esto<br>se debe principalmente a que,<br>durante los meses de enero y<br>febrero,<br>se<br>registraron<br>datos<br>constantes de 0° (norte), en todas<br>las horas. Esta anomalía podría<br>deberse a un error de medición en<br>la estación.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**8.2** **Caracterizaciones variables meteorológicas**



A continuación, se presentan los resultados de la modelación meteorológica para el año

2022, extraídos del punto de grilla más cercano a la ubicación del proyecto. Aunque

previamente se mostraron los datos obtenidos en la estación Pudahuel, en este apartado se

detallan los resultados del modelo WRF, con el fin de proporcionar información

meteorológica específica para la ubicación del proyecto.

**8.2.1** **Viento**

Los campos de viento se caracterizan por la velocidad y las componentes vectoriales de

dirección, las cuales resultan del comportamiento dinámico de las masas de aire. La

interacción entre estas componentes define las características del viento y, en consecuencia,

su capacidad para influir en la dispersión de contaminantes en el área de estudio. En

términos de calidad del aire, el viento juega un papel crucial, ya que su velocidad y dirección

determinan la extensión y dirección de la propagación de los contaminantes, así como su

dilución o concentración en la atmósfera. Estos factores son esenciales para predecir la

dispersión de emisiones y evaluar el impacto ambiental en los puntos receptores.

**8.2.1.1** **Serie de tiempo de la velocidad del viento**

La **Figura 16** muestra la serie temporal de la velocidad del viento modelada mediante el

modelo WRF para el año 2022. A lo largo del periodo analizado, se evidencia una variabilidad

significativa en los valores registrados, destacando picos pronunciados hacia mediados de

año, particularmente entre los meses de junio y julio, cuando se alcanzaron máximos de

hasta 15,00 m/s.

El percentil 95, ubicado en aproximadamente 5,76 m/s, resalta los valores más altos dentro

del conjunto de datos, mientras que el percentil 5, cercano a 0,09 m/s, representa las

condiciones de viento más bajas. Por otro lado, el valor promedio de 2,34 m/s refleja una

tendencia general hacia magnitudes bajas a moderadas durante el año evaluado.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 16. Serie de tiempo de la velocidad del viento modelada para el año**

**2022**

**8.2.1.2** **Caracterización del ciclo diario del viento**

La **Figura 17** presenta el perfil horario promedio de la velocidad del viento modelada con

WRF, tanto para el promedio anual como para cada estación del año 2022; mientras que en

la **Figura 18** se presenta la velocidad promedio horaria junto a los percentiles 5 y 90 que

permiten evidenciar el comportamiento modelado en un rango del 90% de los datos.

A lo largo del año, se observa que la velocidad del viento anual tiende a ser inferior a 2,00

m/s entre las 00:00 y las 10:00 horas, aumentando progresivamente hasta alcanzar un

máximo cercano a 4,50 m/s alrededor de las 16:00 horas. Posteriormente, disminuye

gradualmente hasta completar el ciclo diario. Este patrón general se mantiene en todas las

estaciones del año, aunque con ligeras variaciones.

En verano, la velocidad del viento muestra un aumento significativo entre las 9:00 y las

23:00 horas, marcando un comportamiento distintivo. En contraste, durante el invierno, las

velocidades son notablemente inferiores al promedio anual durante el mismo intervalo

horario. Por su parte, otoño y primavera presentan patrones similares al promedio anual,

sin diferencias significativas en las variaciones horarias.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



Respecto al 90% de los datos modelados se observa que en el horario comprendido entre

las 0:00 a 7:00 horas se simulan velocidades de 0 en el percentil 5 de los datos la cual va

en aumento llegando a ser superior a 1,00 m/s alrededor de las 4 de la tarde, hora en la

cual comienza a disminuir siguiendo el ciclo, lo que es concordante con lo evidenciado en

todas las estaciones de acuerdo con la Figura 17. Respecto a lo evidenciado en el percentil

95, se observa que las velocidades del viento varían en el rango de 2,50 a 6,50 m/s,

presentando varias fluctuaciones en el transcurso del ciclo diario.

**Figura 17. Ciclo diario del viento construido con modelo WRF 2022**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 18. Ciclo diario del viento con un rango del 90% de lo modelado por el**

**WRF 2022**

**8.2.1.3** **Caracterización del ciclo mensual del viento**

En la Figura 19 muestra el ciclo mensual promedio de la velocidad del viento modelada con

WRF para cada estación del año 2022.

El análisis revela un marcado ciclo estacional en la velocidad del viento. Durante los meses

del verano, se registra un aumento significativo en la intensidad entre las 14:00 y las 18:00

horas, alcanzando velocidades superiores a 5 m/s. En contraste, los meses de invierno se

caracterizan por velocidades predominantemente bajas, con valores inferiores a 2 m/s

durante la mayor parte del día.

Independientemente del mes analizado, las horas de la madrugada y las primeras horas de

la mañana presentan las velocidades más bajas del año. Por su parte, los meses de

primavera y otoño exhiben un comportamiento intermedio, con velocidades moderadas y

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



un aumento ligero en horas de la tarde, aunque menos pronunciado que en los meses de

verano.

Este patrón refleja una clara estacionalidad en la distribución y magnitud de la velocidad del

viento.

**Figura 19. Ciclo mensual del viento construido con modelo WRF 2022**

**8.2.1.4** **Caracterización de la velocidad y dirección del viento anual y estacional**

A continuación, se presentan la rosa de los vientos y las distribuciones de frecuencia de la

velocidad del viento, elaboradas a partir de los datos obtenidos del modelo meteorológico

2022 utilizado.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Tabla 16. Rosa y distribución de la velocidad del viento**

|Col1|Rosa y distribución de la velocidad del viento|Características|
|---|---|---|
|**Anual**||-La dirección del viento modelada<br>predominante corresponde a sur<br>(S), representando el 28,1% del<br>total seguida de la dirección sur<br>sureste (SSE) con un 18,5%.<br>-La distribución de la velocidad del<br>viento muestra que la clase<br>predominante corresponde a los<br>vientos entre 0,5-2,1 m/s, con un<br>26,4%, seguido por los vientos<br>calmos, con un 24,9%.<br>-La velocidad del viento promedio<br>es de 2,33 m/s.|
|**Verano**||<br>-La dirección del viento modelada<br>predominante corresponde al sur<br>(S), representando el 36,8% del<br>total seguida de la dirección sur<br>suroeste (SSE) con un 22,7%.<br>-La distribución de la velocidad del<br>viento muestra que la clase<br>predominante corresponde a los<br>vientos entre 3,6-5,7 m/s, con un<br>31,5%, seguido por los vientos<br>entre 2,1 - 3,6 m/s, con un 23,9.<br>-La velocidad del viento promedio<br>es 3,05 m/s.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Rosa y distribución de la velocidad del viento|Características|
|---|---|---|
|**Otoño**||<br>-La dirección del viento modelada<br>predominante corresponde al sur<br>(S), representando el 29,00% del<br>total seguida de la dirección sur<br>suroeste (SSO) con un 18,3%.<br>-La distribución de la velocidad del<br>viento muestra la frecuencia más<br>alta registrada son los vientos<br>calmos con un 28,1% seguido por<br>los vientos entre 0,5 a 2,1 m/s,<br>alcanzando un 26,4%.<br>-La velocidad del viento promedio<br>es 2,14 m/s.|
|**Invierno**||<br>-La dirección del viento modelada<br>predominante corresponde al sur<br>(S), representando el 18,1 % del<br>total seguida de la dirección nor<br>noreste (NNE) con un 13,8%.<br>-Se observa un claro aumento de<br>los vientos calmos y vientos con<br>componente norte, derivando esto<br>último en el aumento se sistemas<br>frontales que ocurre en esta<br>época.<br>-La distribución de la velocidad del<br>viento muestra la frecuencia más<br>alta registrada son las calmas,<br>alcanzando un 38,2%.<br>- La velocidad del viento promedio<br>es de 1,69 m/s.|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Col1|Rosa y distribución de la velocidad del viento|Características|
|---|---|---|
|**Primavera**||-La dirección del viento modelada<br>predominante corresponde al sur<br>(S), representando el 28,7 % del<br>total seguida de la dirección sur<br>sureste (SSE) con un 21,9%.<br>-La distribución de la velocidad del<br>viento muestra la frecuencia más<br>alta registrada es el rango de 3,6 a<br>5,7 m/s y 0,5 a 2,1m/s, alcanzando<br>un<br>29,4%<br>y <br>27,2%<br>respectivamente.<br>-La velocidad del viento promedio<br>es 3,87 m/s.|

**8.2.2** **Temperatura del aire**

La temperatura del aire es un factor clave tanto en la calidad del aire como en los modelos

meteorológicos, ya que influye directamente en los procesos atmosféricos que determinan

la dispersión y transformación de los contaminantes. Su variación impacta la estabilidad

atmosférica, la dinámica de la capa límite, la velocidad de las reacciones químicas y la

capacidad de mezcla vertical, elementos fundamentales para comprender cómo los

contaminantes se distribuyen y se transforman en la atmósfera.

**8.2.2.1** **Serie de tiempo de la temperatura del aire**

La Figura 20 muestra la evolución de la temperatura durante el año 2022, evidenciando una

clara variabilidad estacional. Las temperaturas son más altas en los primeros meses del año

(enero-marzo) y hacia finales de este (noviembre-diciembre), mientras que alcanzan sus

valores más bajos durante el invierno (junio-agosto).

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



El percentil 95, ubicado en 28,29 °C, representa los valores más altos registrados en el

periodo, mientras que el percentil 5, cercano a 5,77 °C, refleja las temperaturas más bajas.

La línea de la media, situada en 15,78 °C, indica que la mayoría de las temperaturas se

mantuvieron en un rango moderado.

Este patrón sigue un comportamiento estacional típico, con variaciones alineadas a las

estaciones climáticas del hemisferio correspondiente. El análisis de estos datos puede ser

útil para identificar períodos críticos de calor o frío que podrían afectar las actividades del

proyecto o las condiciones del entorno.

**Figura 20. Serie de tiempo de la temperatura modelada por el modelo WRF,**

**para el año 2022**

**8.2.2.2** **Caracterización del ciclo diario de la temperatura**

En la Figura 21 muestra el ciclo diario estacional de la temperatura modelada con WRF,

tanto para el promedio anual como para cada estación del año 2022; mientras que en la

Figura 22 se presenta la temperatura promedio horaria junto a los percentiles 5 y 90 que

permiten evidenciar el comportamiento modelado en un rango del 90% de los datos

Se observa que tanto la temperatura anual como la de cada estación siguen una tendencia

similar: a partir de la medianoche, la temperatura disminuye hasta alcanzar su mínimo

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



alrededor de las 6:00 horas. A partir de este momento, con la salida del sol, la temperatura

comienza a aumentar, alcanzando su máximo simulado alrededor de las 15:00 horas.

Durante el verano, la temperatura máxima alcanza aproximadamente los 28°C, mientras

que el promedio anual se sitúa en torno a los 22,5°C. En invierno, la temperatura máxima

simulada es de aproximadamente 15,0°C.

Respecto al 90% de los datos modelados se observa que este sigue plenamente el ciclo

promedio horario de las temperaturas simuladas presentando las mínimas alrededor de las

6:00 y las máximas cercano a 15:00 como percentil 5 y 95.

**Figura 21. Ciclo diario de temperatura construido con modelo WRF 2022**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 22. Ciclo diario de temperatura con un rango del 90% de lo modelado**

**por el WRF 2022**

**8.2.2.3** **Caracterización del ciclo mensual de la temperatura**

En la Figura 23 presenta el perfil horario con el promedio mensual de la temperatura

modelada con WRF para el año 2022. En ella se pueden identificar dos ciclos claramente

definidos. El primero es el ciclo diario, en el cual la temperatura aumenta de manera gradual

desde las 08:00 hasta las 17:00 horas, para luego comenzar a descender. El segundo ciclo

es el estacional, que modifica el ciclo diario a medida que transcurren los meses, pasando

del verano al otoño e invierno. Este ciclo estacional se caracteriza por temperaturas más

bajas y una reducción en la cantidad de horas durante las cuales se alcanzan las

temperaturas máximas.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 23. Ciclo mensual para la temperatura construido con modelo WRF 2022**

**8.2.1** **Capa límite atmosférica**

La capa límite atmosférica es una región de la atmósfera situada cerca de la superficie

terrestre, desempeñando un papel crucial en la dispersión de contaminantes y en el

comportamiento general de la calidad del aire. Su altura varía entre unos pocos cientos de

metros y varios kilómetros, dependiendo de las condiciones meteorológicas.

Esta capa está directamente influenciada por los procesos de intercambio de energía,

momentum y materiales (como calor, humedad y contaminantes) entre la superficie

terrestre y la atmósfera. Dichos intercambios son principalmente controlados por la radiación

solar durante el día y por la radiación térmica nocturna.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**8.2.1.1** **Serie de tiempo de la altura de capa límite atmosférica**



La Figura 24 muestra la evolución anual de la altura de la capa límite atmosférica modelada

para el año 2022. Se observa un comportamiento estacional claramente definido, con

valores más altos durante los meses de verano y primavera, y valores mínimos en invierno.

En promedio, la capa límite alcanza una altura de 336,16 m, mientras que los valores

extremos son reflejados por el percentil 95, ubicado en 1.384,28 m, y el percentil 5, cercano

a 27,58 m.

Durante los meses de verano, se registran las mayores alturas, superando los 2.000 m, lo

que indica una mayor inestabilidad atmosférica y una intensa convección térmica. Esta

mayor altura de la capa límite favorece una mayor mezcla de los contaminantes en la

atmósfera, lo que facilita su dispersión y dilución en la capa de mezcla. En contraste, durante

el invierno, la capa límite se mantiene a alturas notablemente más bajas, generalmente por

debajo de los 500 m. Este comportamiento está asociado a condiciones de estabilidad

atmosférica y la posible presencia de inversiones térmicas, donde las temperaturas en las

capas superiores de la atmósfera son más altas que en la superficie, lo que limita la

verticalidad del aire y, por lo tanto, la dispersión de contaminantes. En estos períodos, los

contaminantes tienden a concentrarse cerca de la superficie, lo que puede generar niveles

elevados de contaminación del aire.

Hacia finales del año, en los meses de primavera y principios de verano, la capa límite

comienza a elevarse nuevamente, lo que contribuye a una mayor capacidad de mezcla y

dispersión de los contaminantes. Este comportamiento estacional de la capa límite

atmosférica es fundamental para entender la dinámica de dispersión y concentración de los

contaminantes. Las variaciones en la altura de la capa límite tienen un impacto directo en

la capacidad de los contaminantes para diluirse o acumularse en la atmósfera, afectando así

la calidad del aire y su distribución espacial a lo largo del año.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 24. Serie de tiempo de la altura de la capa límite modelada por WRF,**

**para el año 2022**

**Caracterización del ciclo diario de la altura de capa límite atmosférica**

En la Figura 25 muestra el ciclo diario estacional de la altura de capa límite atmosférica

modelada con WRF, tanto para el promedio anual como para cada estación del año 2022;

mientras que en la Figura 26 se presenta la altura de capa límite atmosférica promedio

horario junto a los percentiles 5 y 90 que permiten evidenciar el comportamiento modelado

en un rango del 90% de los datos

Se observa que tanto la altura de capa límite atmosférica anual como la de cada estación

siguen una tendencia similar: siendo cercana a 100 metros en horario nocturno comprendido

entre las 00:00 a 7:00 y las 19:00 a 23:00, e incrementando con la salida del sol, llegando

a ser superior a los 1.000 metros como promedio anual alrededor de las 15:00. Durante el

verano, los máximos valores siendo cercana 1.600 metros. En contraste con el invierno,

donde la altura de capa límite atmosférica promedio máximo simulada es de

aproximadamente 450 metros.

Respecto al 90% de los datos modelados se observa que este sigue plenamente el ciclo

promedio horario de la altura de capa límite atmosférica simulada presentando las mínimas

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

en horario nocturno y las máximas cercano a 15:00 como percentil 5 y 95.



**Figura 25. Ciclo diario altura de capa límite construido con modelo WRF 2022**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 26. Ciclo diario altura de capa límite con un rango del 90% de lo**

**modelado por el WRF 2022**

**8.2.1.2** **Caracterización del ciclo mensual de la altura de capa límite atmosférica**

La Figura 27 presenta el ciclo promedio de la altura de la capa límite modelada en la zona

de emplazamiento del proyecto, con un promedio mensual.

Se observa un ciclo diario claro en tres de las cuatro estaciones del año. Las menores alturas

de la capa límite se alcanzan entre las 00:00 y las 07:00 horas, y nuevamente entre las

18:00 y las 23:00 horas. En contraste, entre las 10:00 y las 18:00 horas, la altura de la capa

límite aumenta gradualmente hasta alcanzar su valor máximo alrededor de las 16:00 horas,

para luego comenzar a disminuir. Este patrón se mantiene durante la mayor parte del año,

con excepción de la temporada invernal, cuando las alturas de la capa límite permanecen

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

entre 0 y 750 metros durante todo el día.



Durante los meses de invierno (de mayo a agosto), se observan menores alturas de la capa

de mezcla y condiciones atmosféricas más estables, lo que favorece la acumulación de

contaminantes cerca de la superficie, ya que la capacidad de mezcla vertical es limitada.

Esta estabilidad atmosférica restringe la dispersión de los contaminantes, lo que puede

generar concentraciones más altas de estos en la superficie.

**Figura 27. Ciclo diario de altura de la capa límite construida con modelo WRF**

**2022**

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**8.2.1** **Precipitación**

La precipitación es un fenómeno meteorológico que consiste en la caída de agua desde la

atmósfera hacia la superficie terrestre. Su formación está relacionada con los procesos de

condensación y enfriamiento del vapor de agua en la atmósfera, que, al alcanzar un tamaño

crítico, cae debido a la gravedad.

Este proceso desempeña un papel fundamental en la dinámica atmosférica, actuando como

un mecanismo natural de limpieza de la atmósfera. Durante las precipitaciones, los

contaminantes atmosféricos, como partículas en suspensión y gases, son eliminados de la

columna atmosférica mediante procesos de "lavado" o "remoción húmeda". Como resultado,

se reduce temporalmente la concentración de contaminantes en el aire, mejorando así la

calidad del aire en las áreas afectadas.

En la Figura 28 podemos observar la precipitación mensual modelada por WRF. Se estima

que la precipitación anual es de 158,74 milímetros.

En cuanto a la distribución mensual, se observa claramente que en la zona de

emplazamiento del proyecto existe una temporada húmeda que se extiende durante junio

y julio, durante la cual se concentra el 71,75% de la precipitación anual. Por otro lado, la

temporada seca abarca desde septiembre hasta mayo. Además, durante abril y agosto se

modelaron 21 mm y 16 mm, aproximadamente.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**Figura 28. Precipitación mensual construida con modelo WRF 2022**

**9** **Modelación de olor**

A continuación, se entrega la información acerca de la dispersión de la pluma de olores

dentro del área de estudio. Esto ocurre mediante la interpolación de los valores obtenidos

del percentil 98 de la modelación horaria de la concentración del olor. Esto quiere decir que

el 98% los datos horarios de concentración de olor están por debajo del valor del percentil

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



98, mientras que solo el 2% restante (alrededor de 176 horas al año) superan este nivel.

Los resultados que se presentan a continuación se construyeron usando la subgrilla descrita

en el acápite 6.1, que considera las concentraciones modeladas a una altura 1,6 m, misma

a la cual se evalúan los receptores discretos. Esto evita discrepancias entre la pluma de

dispersión y las concentraciones evaluadas en los receptores discretos. La utilización de esta

metodología es mencionada en la “GUÍA PARA EL USO DE MODELOS DE CALIDAD DEL AIRE

EN EL SEIA” (2023).

**9.1** **Resultados de la dispersión de olor y análisis normativo**

En la **Figura 29** se presenta la pluma de dispersión de odorantes del proyecto con

concentraciones que van desde 1,0 uo/m [3] hasta 4,0 uo/m [3] en la zona de máximo impacto.

El área con concentraciones de olor entre 3 y 4 uo/m3 abarca una superficie de 0,03

hectáreas, la cual se divide en dos zonas distintas, separadas espacialmente, pero con una

forma compacta. Esto indica la presencia de dos focos principales de emisión dentro del

área analizada. La distribución de la pluma de olor está influenciada por la dirección e

intensidad del viento. Como se observa en la **Tabla 16**, el viento proviene

predominantemente del sur, lo que provoca que los contaminantes se desplacen hacia el

norte. Este comportamiento se debe a que, al soplar desde el sur, el viento empuja la pluma

en dirección norte. Además, la intensidad del viento es alta, lo que refuerza este

desplazamiento. Es relevante destacar que los puntos de máxima emisión presentan un

corrimiento hacia el norte con respecto a las fuentes que generan estos puntos, como la

cámara elevadora de la PTAS y el reactor biológico. Este corrimiento hacia el norte es un

reflejo de la dinámica del viento y su interacción con las fuentes de emisión.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Figura 29. Pluma de dispersión de odorantes e isodoras**



No se presentan receptores dentro del área de influencia de la pluma de olores. En la **Tabla**

**17** se presenta un resumen de las características de la pluma de dispersión de odorantes

del proyecto. Entre las características presentadas se encuentran la superficie del área de

máxima emisión, la superficie del área de influencia, el desplazamiento de la pluma medido

desde el área de máxima emisión.

**Tabla 17. Características de la pluma de dispersión**

|Situación<br>de la planta|Superficie<br>del área de<br>máxima<br>emisión (ha)|Superficie<br>del área de<br>influencia<br>(ha)|Desplazamiento (m)|Col5|Receptores<br>en el área de<br>influencia del<br>proyecto|
|---|---|---|---|---|---|
|Situación<br>proyectada|0,03|1,01|**Norte**|88,05|0|
|Situación<br>proyectada|0,03|1,01|**Sur**|116,87|116,87|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Situación<br>de la planta|Superficie<br>del área de<br>máxima<br>emisión (ha)|Superficie<br>del área de<br>influencia<br>(ha)|Desplazamiento (m)|Col5|Receptores<br>en el área de<br>influencia del<br>proyecto|
|---|---|---|---|---|---|
||||**Este**|34,38||
||||**Oeste**|23,50|23,50|

El área de influencia se define como el área o espacio geográfico cuyos atributos, elementos

naturales o socioculturales deben ser considerados con la finalidad de definir si el proyecto

o actividad genera o presenta alguno de los efectos, características o circunstancias del

artículo 11 de la Ley, o bien para justificar la inexistencia de dichos efectos, características

o circunstancias. En este caso, la Guía para la Predicción y Evaluación de Impactos por Olor

en el SEIA establece que el área de influencia se encuentra limitada al espacio contenido

dentro de la isodora de 1 uo/m [3] .

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”

**Figura 30. Área de influencia del proyecto**



La **Figura 30** muestra el área de influencia correspondiente, que abarca una superficie de

1,01 hectáreas y se extiende hacia el norte del área del proyecto. Dentro de esta área, no

se identifican receptores.

La pluma de dispersión tiene un alcance local, presentando las máximas emisiones dentro

del emplazamiento del proyecto y en sus cercanías, lo cual es congruente con el tipo de

actividad y las fuentes generadoras de olor. El área de máxima emisión se definió como el

espacio contenido por la isodora mayor o igual a 3 uo/m [3] . Podemos observar que el área es

de 0,03 ha y esta se divide claramente en dos zonas distintas (ver **Figura 29** ). Estas zonas

están separadas espacialmente y mantienen una forma compacta, indicando la presencia

de dos focos principales de emisión dentro del área analizada. Cada foco está rodeado por

áreas de menor intensidad de emisión, como se observa en los gradientes de color hacia el

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



verde, azul y morado.

El Anexo 2.4.5 kmz, contiene los archivos del área de influencia, Receptores y superficies

modeladas (la superficie de máxima emisión y curvas de nivel).

A continuación, se presentan los resultados de la concentración de los odorantes en los

puntos discretos de interés. Es necesario mencionar, que estos fueron evaluados a una

**altura de 1,6 m respecto del nivel del suelo**, tal como se especifica en el apartado

4.5.2 de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (2023) entregando

una idea de la percepción del olor a la altura de una persona de estatura promedio.

Los resultados obtenidos de la modelación de las emisiones de odorantes de la planta fueron

comparados con el límite normativo de referencia correspondiente a la norma española. En

la **Tabla 18** se presentan los 32 receptores discretos evaluados, junto con el límite

normativo aplicable y las concentraciones modeladas. Se observa que todos los receptores

cumplen con la normativa, siendo el receptor R3 y R3 el que presenta la mayor

concentración, con un valor de 0,23 uo/m [3], lo cual está por debajo del límite de referencia.

**Tabla 18. Análisis del cumplimiento normativo en los receptores**

|Receptor|Límite normativo de<br>inmisión (uo/m3)|Concentración de olor<br>modelado P98 (uo/m3)|Cumplimiento de la<br>norma Percentil 98|
|---|---|---|---|
|EST_1|1,5|0,001|Si|
|R2|1,5|0,22|Si|
|R3|1,5|0,23|Si|
|R4|1,5|0,23|Si|
|R5|1,5|0,20|Si|
|R6|1,5|0,12|Si|
|R7|1,5|0,14|Si|
|R8|1,5|0,08|Si|
|R9|1,5|0,09|Si|
|R10|1,5|0,08|Si|
|R11|1,5|0,04|Si|
|R12|1,5|0,09|Si|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Receptor|Límite normativo de<br>inmisión (uo/m3)|Concentración de olor<br>modelado P98 (uo/m3)|Cumplimiento de la<br>norma Percentil 98|
|---|---|---|---|
|R13|1,5|0,06|Si|
|R14|1,5|0,08|Si|
|R15|1,5|0,07|Si|
|R16|1,5|0,14|Si|
|R17|1,5|0,07|Si|
|R18|1,5|0,10|Si|
|R19|1,5|0,08|Si|
|R20|1,5|0,22|Si|
|R21|1,5|0,05|Si|
|R22|1,5|0,02|Si|
|R23|1,5|0,03|Si|
|R24|1,5|0,04|Si|
|R25|1,5|0,04|Si|
|R26|1,5|0,03|Si|
|R27|1,5|0,02|Si|
|R28|1,5|0,03|Si|
|R29|1,5|0,02|Si|
|R30|1,5|0,05|Si|
|R31|1,5|0,01|Si|
|R32|1,5|0,02|Si|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**9.2** **Percepción de olor**

Si bien el proyecto cumple con todos los límites normativos y no existe impacto significativo,

se realiza el análisis a las concentraciones de acuerdo con la percepción al olfato humano

en los receptores identificados. Para esto, y de acuerdo con la guía, se utilizan dos criterios

de concentración.

Percentil 98: Indica la concentración a la que el 98% de las horas del año las

concentraciones serían iguales o inferiores a las que se indican, por el contrario, sólo el

2% de las horas del año podrían tener concentraciones superiores, lo que equivale a

7,3 días en el año.

Percentil 99,5: Indica las concentraciones en el que el 99,5% del tiempo las

concentraciones son iguales a inferiores a la magnitud indicada, esperando que el 0,5%

de las horas del año pudieran tener concentraciones de mayores magnitudes, es decir,

1,8 día.

La concentración modelada para estos valores será interpretada de acuerdo con la Guía de

Evaluación de Olores para Planificación (IAQM, 2014), la que se basa en la experiencia en

el manejo de olores en Europa, quienes han establecido criterios de sensibilidad para los

receptores de acuerdo con los niveles de exposición.

**Tabla 19. Descriptores de efectos de olor propuestos para impactos predichos**

**por modelación**

|Nivel de exposición<br>al olor|Sensibilidad del receptor|Col3|Col4|
|---|---|---|---|
|**Nivel de exposición**<br>**al olor**|**Baja**|**Media **|**Alta**|
|≥10|Moderada|Sustancial|Sustancial|
|5 <10|Moderada|Moderada|Sustancial|
|3 <5|Leve|Moderada|Moderada|
|1,5 <3|Insignificante|Leve|Moderada|
|0,5<1,5|Insignificante|Insignificante|Leve|
|<0,5|Insignificante|Insignificante|Insignificante|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



En la **Tabla 20** se presentan los resultados de la modelación proyectada para los receptores,

interpretando la percepción del olor de acuerdo con los parámetros identificados en la tabla

anterior, utilizando una sensibilidad alta.

**Tabla 20. Percepción del olor en los receptores cercanos al proyecto**

|Receptor|Concentración modelada<br>(uo/m3)|Col3|Percepción del olor modelada<br>(sensibilidad alta)|Col5|
|---|---|---|---|---|
|**Receptor**|**P98**|**P99,5**|**P98**|**P99,5**|
|R1|0,001|0,001|Insignificante|Insignificante|
|R2|0,22|0,31|Insignificante|Insignificante|
|R3|0,23|0,31|Insignificante|Insignificante|
|R4|0,23|0,31|Insignificante|Insignificante|
|R5|0,20|0,25|Insignificante|Insignificante|
|R6|0,12|0,18|Insignificante|Insignificante|
|R7|0,14|0,18|Insignificante|Insignificante|
|R8|0,08|0,13|Insignificante|Insignificante|
|R9|0,09|0,14|Insignificante|Insignificante|
|R10|0,08|0,13|Insignificante|Insignificante|
|R11|0,04|0,07|Insignificante|Insignificante|
|R12|0,09|0,15|Insignificante|Insignificante|
|R13|0,06|0,11|Insignificante|Insignificante|
|R14|0,08|0,13|Insignificante|Insignificante|
|R15|0,07|0,13|Insignificante|Insignificante|
|R16|0,14|0,19|Insignificante|Insignificante|
|R17|0,07|0,11|Insignificante|Insignificante|
|R18|0,10|0,16|Insignificante|Insignificante|
|R19|0,08|0,13|Insignificante|Insignificante|
|R20|0,22|0,29|Insignificante|Insignificante|
|R21|0,05|0,09|Insignificante|Insignificante|
|R22|0,02|0,04|Insignificante|Insignificante|
|R23|0,03|0,04|Insignificante|Insignificante|
|R24|0,04|0,07|Insignificante|Insignificante|
|R25|0,04|0,07|Insignificante|Insignificante|
|R26|0,03|0,05|Insignificante|Insignificante|

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



|Receptor|Concentración modelada<br>(uo/m3)|Col3|Percepción del olor modelada<br>(sensibilidad alta)|Col5|
|---|---|---|---|---|
|**Receptor**|**P98**|**P99,5**|**P98**|**P99,5**|
|R27|0,02|0,03|Insignificante|Insignificante|
|R28|0,03|0,05|Insignificante|Insignificante|
|R29|0,02|0,03|Insignificante|Insignificante|
|R30|0,05|0,09|Insignificante|Insignificante|
|R31|0,01|0,01|Insignificante|Insignificante|
|R32|0,02|0,03|Insignificante|Insignificante|

Finalmente, en la **Tabla 20** se muestra que, para el percentil 98 de las concentraciones

modeladas de olor, los 32 receptores presentan una percepción insignificante, lo mismo

ocurre al analizar el percentil 99,5. Los receptores con las concentraciones más altas

corresponden a R3 y R4, con valores de 0,23 para el percentil 98 y de 0,31 para el percentil

99,5 en ambos casos.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**10** **Conclusión**

Las concentraciones de odorantes del proyecto “Planta de Tratamiento de RILes AQUALIF”

están influenciada por una serie de factores, que incluyen la tasa de emisión de las fuentes,

así como las características topográficas y meteorológicas de la región en cuestión. En este

contexto, comprender y caracterizar estas variables es crucial para seleccionar los modelos

meteorológicos adecuados que simulen la dispersión y concentración de contaminantes.

Para este estudio, se siguieron las directrices del Servicio de Evaluación Ambiental (SEA)

establecidas en su "Guía para el Uso de Modelos de Calidad del Aire en el SEIA", la cual

recomienda el uso del modelo WRF para la modelación y dispersión de contaminantes, el

cual fue utilizado en el estudio.

En relación con la emisión de odorantes del proyecto, se espera que éstas asciendan a

**394,10** uo/s. El cálculo se basa en la estimación de un factor de emisión determinado de

forma teórica. Cabe señalar que se privilegia el uso de factores de emisión teóricos debido

a que el proyecto en evaluación es un proyecto nuevo, considerando que la metodología

descrita dentro de la “Guía para la predicción y evaluación de impactos por olor del SEIA”,

señala que “podrán usarse factores de emisión o valores de referencia, justificando la

pertinencia y aplicabilidad al proyecto o actividad, cuando se trate de un proyecto

inexistente”

En la estimación de emisiones odorantes, se identificó que las principales fuentes de olor

son la cámara elevadora asociada a la PTAS y el reactor biológico, este último encargado

de recibir el efluente a tratar. El nivel de emisión del reactor biológico está relacionado con

el tamaño de la unidad odorante, ya que cuenta con una superficie de 132 m2.

El área de influencia del proyecto definido como el entorno comprendido dentro de la isodora

de 1 uo/m3, abarca una extensión total de 1,01 hectáreas. Esta área se extiende

predominantemente hacia el norte del proyecto, con una menor proyección hacia el sur.

Dentro de esta zona no se encuentra ningún receptor, sin embargo, el receptor más cercano

al área de influencia es el receptor R2 que se encuentra a 264 metros del límite de la pluma.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



Las máximas emisiones se distribuyen en dos sectores, uno dentro del área del proyecto y

otro al norte, fuera de ella, abarcando una superficie de 0,03 hectáreas. Este patrón sugiere

la presencia de dos focos principales de emisión, relacionados a la cámara de elevación de

la PTAS y el reactor biológico. El desplazamiento de las emisiones hacia el norte se debe a

la dirección predominante del viento del sur, reforzado por su alta intensidad, lo que indica

una clara influencia de la dinámica del viento en la distribución de la pluma de olor.

Desde la perspectiva del análisis de cumplimiento normativo, se concluye que el proyecto

se ajusta a los límites establecidos por la normativa española para la inmisión de odorantes

provenientes de actividades de tratamiento de aguas industriales residuales, en donde en

ningún receptor se supera el límite de 1,5 uo/m [3] .

Con base en lo anterior, y considerando que las emisiones evaluadas corresponden a un

escenario desfavorable, se ha asumido que las unidades abiertas, como los deshidratadores,

el desengrasador y el sistema DAF, se evalúan como si estuvieran fuera del edificio de

producción (a pesar de que su ubicación original sea dentro de este). Esto permite analizar

un escenario más adverso y desfavorable, por lo que la percepción real de los olores debería

ser menor a la calculada en este informe. Por lo anterior, se puede afirmar que el proyecto

no generará un perjuicio a la calidad de vida de las personas debido a la generación de

odorantes que derivan de la fase de operación del proyecto.

Asimismo, se concluye que la salud de la población vecina no se verá comprometida, dado

que las concentraciones modeladas en cada punto receptor se encuentran por debajo de

los límites de inmisión establecidos por la normativa de referencia utilizada.

DECLARACION IMPACTO AMBIENTAL
INFORME MODELACIÓN ODORANTES

“Planta De Tratamiento De RILes AQUALIF”



**11** **Bibliografía**

Netherlands Emission Guidelines for Air, Chapter 3.3 Special Regulations for Specific

Processes, Section G.3 "Sewage Treatment Installations, abril 2003" (páginas 117 a 122)”.

Normativa de Inmisión, Anexo 4 de la Ordenanza Municipal de Calidad Odorífera del Aire

NPE: A-240415-5055 de Alcantarilla, Murcia, España

Servicio de Evaluación Ambiental (2017). Guía para la Predicción y Evaluación de Impactos

por Olor en el SEIA.

Cohen, S., Evans, G., Stokols, D., & Krantz, D. (1986). Behavior, health and environmental

stress. New York.

Servicio de Evaluación Ambiental. (2015). Informe final: Servicio de recopilación y

sistematización de factores de emisión al aire para el Servicio de Evaluación Ambiental.

 - - - - - Recuperado de [https://www.sea.gob.cl/noticias/sea](https://www.sea.gob.cl/noticias/sea-publica-guia-para-prediccion-y-evaluacion-de-impactos-por-olor-en-el-seia) publica guia para prediccion y

[evaluacion-de-impactos-por-olor-en-el-seia.Infraestructura de Datos Geospaciales - IDE](https://www.sea.gob.cl/noticias/sea-publica-guia-para-prediccion-y-evaluacion-de-impactos-por-olor-en-el-seia)

Chile. (8 de enero de 2018). www.ide.cl.

Martínez Rodríguez, E. (2005). Errores Frecuentes en la interpretación del coeficiente de

determinación lineal. Anuario Jurídico y Económico Escuarialense, 315-322.

OMS. (2005). Guías de calidad del aire de la OMS relativas al material particulado, el ozono,

el dióxido de nitrógeno y el dióxido de azufre.

Sarricolea, P., Herrera-Ossandon, M., & Meseguer-Ruiz, O. (2016). Climatic regionalisation

of continental Chile.

Servicio de Evaluación Ambiental (2023). Guía para el Uso de Modelos de Calidad del Aire

en el SEIA.

ECOTEC (2013). ESTUDIO: ANTECEDENTES PARA LA REGULACIÓN DE OLORES EN CHILE

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Ubicación punto central del proyecto****

| Coordenadas del proyecto (UTM 19 WGS 84) | Col2 |
| --- | --- |
| **Coordenada Este (m)** | **Coordenada Norte (m)** |
| 329.545 | 6.308.789 |

**Tabla 2.: Norma de olores de referencia****

| Norma | Nivel de<br>ofensividad | Valor<br>[uo/m3] | Ejemplo |
| --- | --- | --- | --- |
| Percentil 98 del<br>promedio horario | Alta | 1,5 | Depuración tratamiento de aguas<br>residuales industriales, procesamiento de<br>grasas y aceites, aprovechamiento de<br>subproductos de origen animal, etc |
| Percentil 98 del<br>promedio horario | Media | 3 | Producción y fabricación de alimentos,<br>frituras, etc |
| Percentil 98 del<br>promedio horario | Baja | 6 | Cerveceras, fabricación industrial de pan,<br>pastelería, dulces y golosinas, etc |

**Tabla 3.: Límite normativo****

| Estado | Límite de<br>inmisión<br>(uo/m3) | Forma de cálculo | Fuente |
| --- | --- | --- | --- |
| España | 1,5 | Como el percentil 98 de las<br>concentraciones horarias de un<br>año calendario. | Anexo<br>4 <br>de<br>la<br>Ordenanza<br>Municipal de Calidad Odorífera<br>del Aire NPE: A-240415-5055 de<br>Alcantarilla, Murcia, España |

**Tabla 4.: Fuentes de olor modeladas del proyecto****

| ID | Fuente | Coordenadas centrales UTM<br>(WGS-84 19S) | Col4 | Tipo de<br>Fuente | Descripción de la fuente | Régimen de<br>funcionamiento |
| --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Fuente** | **Este (m)** | **Norte(m)** | **Norte(m)** | **Norte(m)** | **Norte(m)** |
| 1 | Cámara de elevación PTAS | 329.523,38 | 6.308.821,39 | Difusa | Recolección<br>de<br>aguas<br>residuales mediante una red<br>subterránea de alcantarillado.<br>Esta red descargará las aguas<br>a <br>un<br>estanque<br>de<br>acumulación, desde donde se<br>alimentará una planta de<br>tratamiento de aguas servidas<br>(PTAS), del tipo lodo activado.<br>Esta cuenta con una cámara<br>de elevación y dos tuberías<br>por las cuales podría emitirse<br>olor. | Todo el año |
| 2 | PTAS (tubería 1) | 329.521,02 | 6.308.819,67 | Difusa | Difusa | Todo el año |
| 3 | PTAS (tubería 1) | 329.521,81 | 6.308.820,11 | Difusa | Difusa | Todo el año |
| 4 | Filtrado sólidos gruesos | 329.552,57 | 6.308.789,86 | Difusa | Remover sólidos asimilables a<br>domiciliarios mediante una<br>rejilla gruesa | Todo el año |
| 5 | Fosa receptora (compuerta 1) | 329.546,97 | 6.308.789,45 | Difusa | Recibir todos los RILes crudos<br>posteriores<br>al<br>filtrado<br>de<br>solidos<br>gruesos<br>para<br>posteriormente ser tratados<br>por la planta de tratamiento.<br>La fosa receptora posee dos<br>aperturas, que se modelan<br>abiertas para considerar un<br>escenario conservador. | Todo el año |
| 6 | Fosa receptora (compuerta 2) | 329.549,95 | 6.308.790,51 | Difusa | Difusa | Todo el año |
| 7 | Estanque acumulador de RILes | 329.547,08 | 6.308.803,25 | Difusa | Almacenar los RILES, estos<br>estanques,<br>fabricados<br>en<br>polietileno lineal LLDPE, son | Todo el año |

**Tabla 5.: Valores del parámetro P (% del flujo que llega por gravedad) para los****

| Procesos | Parámetro P | Justificación |
| --- | --- | --- |
| Sistema de<br>tratamiento particular<br>de alcantarillado | 0 | La recolección de las aguas residuales se realiza<br>mediante una red subterránea de alcantarillado, la<br>cual descarga en un estaque de acumulación, luego<br>una planta de elevación lleva estas aguas residuales<br>a la planta de tratamiento de aguas servidas del tipo<br>de lo activado. Por lo tanto, el agua es impulsada por<br>esta planta de elevación. |
| Tratamiento de RILes | 100 | El RIL es traído por camiones cisterna, los cuales<br>realizan sus descargas en un área específica de la<br>planta, adaptada para esta actividad, en donde el<br>flujo de descarga del RIL se realiza mediante<br>gravedad. |

**Tabla 6.: Parámetros para la selección de los factores de emisión****

| Parámetro | Descripción | Valor |
| --- | --- | --- |
| P | Porcentaje del flujo total que llega a planta por gravedad (%) | 100 |
| S | Contenido de limo del afluente | 0,09 |

**Tabla 7.: Factores de emisión para cada una de las fuentes modeladas y su respectiva justificación****

| ID<br>modelo<br>4 | Nombre fuente<br>emisora | Tipo<br>de<br>fuent<br>e | Tipo de<br>emisión | Factor de<br>Emisión<br>(uo /s m2)<br>e | Justificación |
| --- | --- | --- | --- | --- | --- |
| SRC_1 | Cámara de<br>elevación | Área | Pasiva | 65 | Con la presente reformulación del proyecto, el sistema de alcantarillado, originalmente compuesto<br>por una fosa séptica, será sustituido por una planta de tratamiento de aguas servidas (PTAS). Para<br>más detalles, se puede consultar el Anexo 3.1 de la Adenda complementaria. Esta PTAS recibirá el<br>agua servida a través de una red subterránea, la cual pasará posteriormente por una cámara de<br>elevación.<br>El factor de emisión aplicado se ha basado en los valores especificados en la tabla 2 del documento<br>Netherlands Emission Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”,<br>sección G.3, “Sewage Treatment Installations”, aplicable a procesos de pretratamiento.<br>Considerando que todo el flujo llega mediante impulsión, se ha determinado como adecuado el uso<br>de un factor de emisión de 65, correspondiente al acceso y pretratamiento para esta condición<br>(100% impulsión) |
| SRC_2 | PTAS (tubería 1) | Área | Pasiva | 65 | 65 |
| SRC_3 | PTAS (tubería 2) | Área | Pasiva | 65 | 65 |
| SRC_4 | Filtrado sólidos<br>gruesos | Área | Pasiva | 9,5 | Esta fuente de emisión corresponde a la recepción de los RILes, donde el 100% del afluente a<br>tratar llega por gravedad, descargado directamente desde camiones transporte de RIL. El factor de<br>emisión aplicado se refiere al agua pretratada, en la que solo se han filtrado los sólidos gruesos<br>presentes en el agua residual, antes de ser trasladada a la fosa receptora. El factor de emisión<br>utilizado se basa en los valores especificados en la tabla 2 del documento Netherlands Emission<br>Guidelines for Air, capítulo 3.3, “Special Regulations for Specific Processes”, sección G.3, “Sewage<br>Treatment Installations”. Este factor es aplicable a sistemas de pretratamiento, específicamente<br>para la remoción de material retenido en la rejilla de ingreso, considerando un flujo que llega por<br>gravedad al 100%. |
| SRC_5 | Fosa receptora | Área | Activa | 9,5 | 9,5 |
| SRC_6 | Fosa receptora | Área | Activa | 9,5 | 9,5 |
| SRC_7 | Estanque<br>acumulador de<br>RILes | Área | Activa | 9,5 | Cabe destacar que, en este punto, las unidades aún no han pasado por el sistema de tratamiento<br>biológico. Por lo tanto, se utiliza el mismo factor de emisión aplicado al pretratamiento, ya que los |

**Tabla 8.: Receptores cercanos al proyecto****

| Receptor | Coordenada UTM HUSO<br>19 S (m) | Col3 | Distancia al<br>centro<br>del proyecto<br>(m) | Descripción |
| --- | --- | --- | --- | --- |
| **Receptor** | **Este** | **Norte** | **Norte** | **Norte** |
| Est_1 | 339.594 | 6.308.625 | 10.048 | Estación Quilicura (SINCA) |
| R_1 | 329.847 | 6.308.901 | 322 | Vivenda Chorillo 2 |
| R_2 | 329.797 | 6.308.956 | 304 | Vivenda Chorillo 2 |
| R_3 | 329.798 | 6.309.035 | 354 | Parcela Chorrillo 2 |
| R_4 | 329.901 | 6.309.227 | 569 | Parcela El Descanso |
| R_5 | 330.120 | 6.308.520 | 631 | Parcela Chorrillo 2 |
| R_6 | 329.848 | 6.308.231 | 629 | Parcela Chorrillo 1 |
| R_7 | 328.789 | 6.308.470 | 820 | Vivienda El Noviciado |
| R_8 | 328.756 | 6.308.676 | 800 | Vivienda El Noviciado |
| R_9 | 328.721 | 6.308.764 | 826 | Vivienda El Noviciado |
| R_10 | 328.511 | 6.308.854 | 1.037 | Vivienda El Noviciado |
| R_11 | 328.799 | 6.309.102 | 813 | Vivienda El Noviciado |
| R_12 | 328.708 | 6.309.242 | 956 | Vivienda El Noviciado |
| R_13 | 328.789 | 6.309.241 | 885 | Vivienda El Noviciado |
| R_14 | 328.815 | 6.309.391 | 951 | Vivienda El Noviciado |
| R_15 | 329.125 | 6.309.462 | 800 | Parcela El Noviciado |
| R_16 | 330.357 | 6.309.052 | 853 | Parcela Chorrillo 3 |
| R_17 | 330.223 | 6.309.088 | 743 | Parcela Chorrillo 3 |
| R_18 | 328.810 | 6.309.334 | 919 | Vivienda El Noviciado |
| R_19 | 329.830 | 6.309.144 | 462 | Parcela Chorrillo 2 |

**Tabla 9.: Estimación de emisiones odorantes****

| ID | Nombre fuente emisora | Tipo<br>de<br>Fuente | Tipo de<br>emisión | Factor de emisión e (uo /m2) | Área<br>(m2) | TEO<br>(uo /s)<br>e | Referencia | País de<br>proceden<br>cia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC_1 | Cámara de elevación | Área | Pasiva | 65,00 | 2,25 | 146,25 | Netherlands<br>Emission<br>Guidelines for Air,<br>Chapter 3.3<br>Special<br>Regulations for<br>Specific<br>Processes,<br>Section G.3<br>"Sewage<br>Treatment<br>Installations, Abril<br>2003" (páginas<br>117 a 122) | Países<br>Bajos |
| SRC_2 | PTAS (tuberia 1) | Área | Pasiva | 65,00 | 0,01 | 0,62 | 0,62 | 0,62 |
| SRC_3 | PTAS (tuberia 1) | Área | Pasiva | 65,00 | 0,01 | 0,62 | 0,62 | 0,62 |
| SRC_4 | Filtrado sólidos gruesos | Área | Pasiva | 9,50 | 3,00 | 28,50 | 28,50 | 28,50 |
| SRC_5 | Fosa receptora | Área | Pasiva | 9,50 | 1,04 | 9,88 | 9,88 | 9,88 |
| SRC_6 | Fosa receptora | Área | Pasiva | 9,50 | 0,64 | 6,08 | 6,08 | 6,08 |
| SRC_7 | Estanque acumulador de RILes | Área | Pasiva | 9,50 | 0,29 | 2,77 | 2,77 | 2,77 |
| SRC_8 | Estanque acumulador de RILes | Área | Pasiva | 9,50 | 0,29 | 2,77 | 2,77 | 2,77 |
| SRC_9 | Estanque acumulador de RILes | Área | Pasiva | 9,50 | 0,29 | 2,77 | 2,77 | 2,77 |
| SRC_10 | Ecualizadores de RILes | Área | Pasiva | 9,50 | 0,29 | 2,77 | 2,77 | 2,77 |
| SRC_11 | Ecualizadores de RILes | Área | Pasiva | 9,50 | 0,29 | 2,77 | 2,77 | 2,77 |
| SRC_12 | Deshidratador | Área | Pasiva | 8,00 | 1,92 | 15,37 | 15,37 | 15,37 |
| SRC_13 | Desengrasador | Área | Pasiva | 5,50 | 7,07 | 38,86 | 38,86 | 38,86 |
| SRC_14 | Flotación de aire disuelto (DAF) | Área | Pasiva | 0,55 | 2,44 | 1,34 | 1,34 | 1,34 |
| SRC_15 | Contenedor de lodos | Área | Pasiva | 4,35 | 5,08 | 22,11 | 22,11 | 22,11 |
| SRC_16 | Contenedor de lodos | Área | Pasiva | 4,35 | 5,08 | 22,11 | 22,11 | 22,11 |
| SRC_17 | Cámara de agua cola | Área | Pasiva | 1,10 | 13,00 | 14,30 | 14,30 | 14,30 |
| SRC_18 | Estanque de lodos | Área | Pasiva | 4,35 | 0,29 | 1,27 | 1,27 | 1,27 |
| SRC_19 | Ecualizador secundario | Área | Pasiva | 1,10 | 0,29 | 0,32 | 0,32 | 0,32 |
| SRC_20 | Reactor biológico | Área | Pasiva | 0,55 | 132,00 | 72,60 |  |  |

**Tabla 10.: Ranking de las unidades generadoras de olor****

| Nombre unidad | TEO (uo/s) | % TEO |
| --- | --- | --- |
| Cámara de elevación PTAS | 146,25 | 37,11 |
| Reactor biológico | 72,60 | 18,42 |
| Desengrasador | 38,86 | 9,86 |
| Filtrado sólidos gruesos | 28,50 | 7,23 |
| Contenedor de lodos | 22,11 | 5,61 |
| Contenedor de lodos | 22,11 | 5,61 |
| Deshidratador | 15,37 | 3,90 |
| Cámara de agua cola | 14,30 | 3,63 |
| Fosa receptora | 9,88 | 2,51 |
| Fosa receptora | 6,08 | 1,54 |
| Estanque acumulador de RILes | 2,77 | 0,70 |
| Estanque acumulador de RILes | 2,77 | 0,70 |
| Estanque acumulador de RILes | 2,77 | 0,70 |
| Ecualizadores de RILes | 2,77 | 0,70 |
| Ecualizadores de RILes | 2,77 | 0,70 |
| Flotación de aire disuelto (DAF) | 1,34 | 0,34 |
| Estanque de lodos | 1,27 | 0,32 |
| PTAS (tuberia 1) | 0,62 | 0,16 |
| PTAS (tuberia 1) | 0,62 | 0,16 |
| Ecualizador secundario | 0,32 | 0,08 |
| **TOTAL** | **394,10** | **394,10** |

**Tabla 11.: Coordenadas del centroide del modelo WRF****

| WSG 84 - 19 S | Col2 |
| --- | --- |
| **UTM E (m)** | **UTM N (m)** |
| 330.217 | 6.316.965 |

**Tabla 12.: Resultados estadísticos obtenidos por la modelación respecto a las****

| Estadístico | Criterio guía modelación<br>SEA | Estación Pudahuel |
| --- | --- | --- |
| **Temperatura (°C)** | **Temperatura (°C)** | **Temperatura (°C)** |
| Correlación lineal (r) | **>0,8** | 0,95 |
| Coeficiente de determinación (r2) | **- ** | 0,90 |
| BIAS | **[-4, 4]** | 0,62 |
| MAE | **≤ 4** | 1,88 |
| RMSE | **≤ 4,5** | 2,48 |
| **Velocidad del viento (m/s)** | **Velocidad del viento (m/s)** | **Velocidad del viento (m/s)** |
| Correlación lineal (r) | **>0,6** | 0,49 |
| Coeficiente de determinación (r2) | **- ** | 0,24 |
| BIAS | **[-2,5, 2,5]** | 0,2 |
| MAE | **≤ 3** | 1,57 |
| RMSE | **≤3,5** | 2,31 |

**Tabla 13.: Temperatura modelada y observada en estación Pudahuel****

| Col1 | Temperatura modelada y observada | Características |
| --- | --- | --- |
| **Serie de tiempo** |  | -En<br>la<br>figura<br>se<br>presenta<br>la<br>temperatura<br>observada<br>en<br>la<br>estación Pudahuel (superior) y la<br>modelada en el punto de grilla donde<br>se ubica la estación (inferior). La<br>cantidad<br>de<br>disponibles<br>de<br>la<br>estación corresponde a 99,98% lo<br>que queda en evidencia de acuerdo<br>con lo observado.<br>-Se observa que el modelo logra<br>representar de manera robusta el<br>comportamiento observado en la<br>estación Pudahuel. |
| **Correlación** |  | -La temperatura modelada tiene una<br>correlación<br>significativa<br>con<br>los<br>valores observados en la estación<br>Pudahuel, cuyo valor es de 0,95.<br>-A<br>su<br>vez,<br>el<br>coeficiente<br>de<br>determinación sugiere que el modelo<br>es capaz de representar el 90% de la<br>variabilidad observada (R2 = 0,90). |

**Tabla 14.: Velocidad del viento modelada y observada en estación Pudahuel****

| Col1 | Velocidad del viento modelada y observada | Características |
| --- | --- | --- |
| **Series de tiempo** |  | -En la figura se presenta la velocidad<br>del viento observada en la estación<br>Pudahuel (superior) y la modelada<br>en el punto de grilla donde se ubica<br>la estación (inferior). Contemplando<br>la estación una disponibilidad de<br>datos del 99,98%.<br>-Se observa que el modelo logra<br>representar de manera robusta la<br>variabilidad estación.<br>-Aunque no se observa una pérdida<br>significativa de datos, se evidencia<br>que, durante los meses de enero y<br>febrero,<br>la<br>estación<br>simula<br>exclusivamente velocidades calmas<br>de 0 m/s. Es importante señalar que<br>estos<br>valores<br>de<br>0 <br>m/s<br>probablemente<br>corresponden<br>a <br>errores en la estación y deberían<br>considerarse como datos faltantes.<br>Sin embargo, no se realizó este<br>ajuste debido a la falta de certeza,<br>lo que afecta los estadísticos y<br>puede ser una de las razones por las<br>que la correlación no cumple con el<br>criterio. |

**Tabla 15.: Dirección del viento modelada y observada en estación Pudahuel****

| Col1 | Dirección del viento modelada y observada | Características |
| --- | --- | --- |
| **Series de tiempo** |  | -En la figura se presenta la rapidez<br>del viento observada en la estación<br>Pudahuel (superior) y la modelada<br>en el punto de grilla donde se ubica<br>la estación (inferior). Existiendo en<br>la estación un 99,98% de los datos<br>anuales.<br>-Se<br>evidencia<br>que,<br>como<br>fue<br>mencionado con la velocidad del<br>viento,<br>no<br>hay<br>una<br>perdida<br>significativa de datos en la estación<br>de monitoreo, pero se observa como<br>los datos del mes de enero y parte<br>de febrero son 0° constantemente.<br>- Es importante señalar que estos<br>valores<br>de<br>0°<br>probablemente<br>corresponden a errores en la<br>estación y deberían considerarse<br>como datos faltantes. Sin embargo,<br>no se realizó este ajuste debido a la<br>falta de certeza, lo que afecta los<br>estadísticos y puede ser una de las<br>razones por las que la correlación no<br>cumple con el criterio. |

**Tabla 16.: Rosa y distribución de la velocidad del viento****

| Col1 | Rosa y distribución de la velocidad del viento | Características |
| --- | --- | --- |
| **Anual** |  | -La dirección del viento modelada<br>predominante corresponde a sur<br>(S), representando el 28,1% del<br>total seguida de la dirección sur<br>sureste (SSE) con un 18,5%.<br>-La distribución de la velocidad del<br>viento muestra que la clase<br>predominante corresponde a los<br>vientos entre 0,5-2,1 m/s, con un<br>26,4%, seguido por los vientos<br>calmos, con un 24,9%.<br>-La velocidad del viento promedio<br>es de 2,33 m/s. |
| **Verano** |  | <br>-La dirección del viento modelada<br>predominante corresponde al sur<br>(S), representando el 36,8% del<br>total seguida de la dirección sur<br>suroeste (SSE) con un 22,7%.<br>-La distribución de la velocidad del<br>viento muestra que la clase<br>predominante corresponde a los<br>vientos entre 3,6-5,7 m/s, con un<br>31,5%, seguido por los vientos<br>entre 2,1 - 3,6 m/s, con un 23,9.<br>-La velocidad del viento promedio<br>es 3,05 m/s. |

**Tabla 17.: Características de la pluma de dispersión****

| Situación<br>de la planta | Superficie<br>del área de<br>máxima<br>emisión (ha) | Superficie<br>del área de<br>influencia<br>(ha) | Desplazamiento (m) | Col5 | Receptores<br>en el área de<br>influencia del<br>proyecto |
| --- | --- | --- | --- | --- | --- |
| Situación<br>proyectada | 0,03 | 1,01 | **Norte** | 88,05 | 0 |
| Situación<br>proyectada | 0,03 | 1,01 | **Sur** | 116,87 | 116,87 |

**Tabla 18.: Análisis del cumplimiento normativo en los receptores****

| Receptor | Límite normativo de<br>inmisión (uo/m3) | Concentración de olor<br>modelado P98 (uo/m3) | Cumplimiento de la<br>norma Percentil 98 |
| --- | --- | --- | --- |
| EST_1 | 1,5 | 0,001 | Si |
| R2 | 1,5 | 0,22 | Si |
| R3 | 1,5 | 0,23 | Si |
| R4 | 1,5 | 0,23 | Si |
| R5 | 1,5 | 0,20 | Si |
| R6 | 1,5 | 0,12 | Si |
| R7 | 1,5 | 0,14 | Si |
| R8 | 1,5 | 0,08 | Si |
| R9 | 1,5 | 0,09 | Si |
| R10 | 1,5 | 0,08 | Si |
| R11 | 1,5 | 0,04 | Si |
| R12 | 1,5 | 0,09 | Si |

**Tabla 19.: Descriptores de efectos de olor propuestos para impactos predichos****

| Nivel de exposición<br>al olor | Sensibilidad del receptor | Col3 | Col4 |
| --- | --- | --- | --- |
| **Nivel de exposición**<br>**al olor** | **Baja** | **Media ** | **Alta** |
| ≥10 | Moderada | Sustancial | Sustancial |
| 5 <10 | Moderada | Moderada | Sustancial |
| 3 <5 | Leve | Moderada | Moderada |
| 1,5 <3 | Insignificante | Leve | Moderada |
| 0,5<1,5 | Insignificante | Insignificante | Leve |
| <0,5 | Insignificante | Insignificante | Insignificante |

**Tabla 20.: Percepción del olor en los receptores cercanos al proyecto****

| Receptor | Concentración modelada<br>(uo/m3) | Col3 | Percepción del olor modelada<br>(sensibilidad alta) | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **P98** | **P99,5** | **P98** | **P99,5** |
| R1 | 0,001 | 0,001 | Insignificante | Insignificante |
| R2 | 0,22 | 0,31 | Insignificante | Insignificante |
| R3 | 0,23 | 0,31 | Insignificante | Insignificante |
| R4 | 0,23 | 0,31 | Insignificante | Insignificante |
| R5 | 0,20 | 0,25 | Insignificante | Insignificante |
| R6 | 0,12 | 0,18 | Insignificante | Insignificante |
| R7 | 0,14 | 0,18 | Insignificante | Insignificante |
| R8 | 0,08 | 0,13 | Insignificante | Insignificante |
| R9 | 0,09 | 0,14 | Insignificante | Insignificante |
| R10 | 0,08 | 0,13 | Insignificante | Insignificante |
| R11 | 0,04 | 0,07 | Insignificante | Insignificante |
| R12 | 0,09 | 0,15 | Insignificante | Insignificante |
| R13 | 0,06 | 0,11 | Insignificante | Insignificante |
| R14 | 0,08 | 0,13 | Insignificante | Insignificante |
| R15 | 0,07 | 0,13 | Insignificante | Insignificante |
| R16 | 0,14 | 0,19 | Insignificante | Insignificante |
| R17 | 0,07 | 0,11 | Insignificante | Insignificante |
| R18 | 0,10 | 0,16 | Insignificante | Insignificante |
| R19 | 0,08 | 0,13 | Insignificante | Insignificante |
| R20 | 0,22 | 0,29 | Insignificante | Insignificante |
| R21 | 0,05 | 0,09 | Insignificante | Insignificante |
| R22 | 0,02 | 0,04 | Insignificante | Insignificante |
| R23 | 0,03 | 0,04 | Insignificante | Insignificante |
| R24 | 0,04 | 0,07 | Insignificante | Insignificante |
| R25 | 0,04 | 0,07 | Insignificante | Insignificante |
| R26 | 0,03 | 0,05 | Insignificante | Insignificante |
