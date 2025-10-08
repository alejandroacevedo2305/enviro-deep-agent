---
title: Sin título
author: Leslie Lira Azcarategui
date: D:20250417114814-04'00'
language: es
type: report
pages: 61
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO ENERGÉTICA SOLAR MEMBRILLO
-->

**ANEXO N°2.3**
**MODELACIÓN DE EMISIONES ATMOSFÉRICAS**

**DIA ENERGÉTICA SOLAR MEMBRILLO**

# ADENDA DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO ENERGÉTICA SOLAR MEMBRILLO

## ANEXO N°2.3 MODELACIÓN DE EMISIONES ATMOSFÉRICAS

ELABORADO PARA

## ENERGÉTICA SOLAR MEMBRILLO SpA

Av. Andrés Bello 2233, Piso 3, Providencia · Santiago · Chile · Fono (+56 ) 2 2963 8560 · www.inerco.com

**Marzo 2025**

ENERGETICA SOLAR MEMBRILLO

**INDICE GENERAL**

**1** **Introducción ........................................................................................................................ 4**

**2** **Modelación de Calidad del Aire ............................................................................................ 5**

2.1 Descripción del modelo utilizado ........................................................................................ 5

2.2 Dominio de modelación meteorológica .............................................................................. 5

2.3 Topografía ........................................................................................................................... 6

2.4 Uso de Suelo ........................................................................................................................ 8

2.5 Selección del año de modelación ........................................................................................ 9

2.6 Antecedentes meteorológicos para Análisis de Incertidumbre .......................................... 9

2.6.1 Meteorología observada ............................................................................................. 9

2.6.2 Meteorología modelada WRF ................................................................................... 15

2.6.3 Análisis cualitativo y cuantitativo de modelación meteorológica v/s meteorología

observada .................................................................................................................................. 21

2.7 Receptores de interés y ubicación .................................................................................... 28

2.7.1 Receptores humanos ................................................................................................. 28

2.7.2 Normativa .................................................................................................................. 30

2.7.3 Escenario de modelación .......................................................................................... 31

2.7.4 Entradas al modelo .................................................................................................... 31

2.8 Resultados en punto de mayor concentración ................................................................. 33

2.9 Comparación con norma de calidad ................................................................................. 35

2.9.1 Comparación con norma de calidad escenario Año 1 ............................................... 35

2.10 Evaluación del impacto de las emisiones atmosféricas de material particulado respirable

MP 10 y MP 2,5 en Zonas Saturadas. ................................................................................................. 36

2.11 Mapas de isoconcentraciones e isodepositaciones (MPS)............................................ 37

2.11.1 Año 1: Mapas de Isoconcentración e isodepositación .............................................. 37
**3** **Área de Influencia .............................................................................................................. 53**

**4** **Escenario Sinérgico ............................................................................................................ 55**

4.1 Consideraciones ................................................................................................................ 55

**5** **Evaluación de Riesgo a la Salud de la Población por emisiones atmosféricas ...................... 55**

5.1 Criterios para Evaluar la Generación o Presencia del Efecto, Característica o Circunstancia

de la Letra a) del Artículo 11 de la Ley N° 19.300 ......................................................................... 55

**6** **Conclusiones ...................................................................................................................... 58**

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

i

ENERGETICA SOLAR MEMBRILLO

**INDICE DE TABLAS**

Tabla 2-1. Registro de velocidad del viento Estación ................................................................... 9

Tabla 2-2. Coordenadas de ubicación referencial de estación .................................................... 9

Tabla 2-3. Métricas estadísticas recomendables en el análisis de incertidumbre para las

variables 27

Tabla 2-4. Métricas estadísticas calculadas ............................................................................... 27

Tabla 2-5. Receptores humanos y coordenadas de ubicación referencial ................................ 28

Tabla 2-6. Receptores Fauna y coordenadas de ubicación referencial...................................... 28

Tabla 2-7. Normativa primaria y secundaria de calidad del aire utilizada ................................. 30

Tabla 2-8. Resumen de emisiones atmosféricas por año cronológico del proyecto. ................ 31

Tabla 2-9. Tasas de emisión de fase de construcción del Proyecto ........................................... 32

Tabla 2-10. Resultados punto de mayor concentración y depositación Año 1 ....................... 33

Tabla 2-11. Aporte en receptores humanos - Año 1 ............................................................... 35

Tabla 2-12 Relación porcentual del aporte respecto a normativa en receptores humanos Año

1 35

Tabla 2-13. Aporte de MPS y SO 2 en receptores discretos Año 1 ............................................ 36

Tabla 2-14. Relación porcentual del aporte de MPS y SO 2 en receptores discretos Año 1 ..... 36

Tabla 2-15 Comparación de los resultados de la modelación en receptores humanos y valores de

significancia de la Tabla 2 de la Guía, para la fase de construcción. ................................................. 37

Tabla 5-1 Criterios para evaluación la generación o presencia de los efectos características o

circunstancia de la Letra a) del Art. 11 Ley 19.300 ........................................................................... 56

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

ii

ENERGETICA SOLAR MEMBRILLO

**INDICE DE FIGURAS**

Figura 2-1. Dominio de modelación .............................................................................................. 6

Figura 2-2 Mapa topográfico 2D .................................................................................................. 7

Figura 2-3 Uso de Suelo ................................................................................................................ 8

Figura 2-4 Serie de tiempo velocidad del viento, m/s ................................................................ 10

Figura 2-5 Serie de tiempo dirección del viento promedio ........................................................ 11

Figura 2-6 Rosa de los vientos, promedio horario ..................................................................... 11

Figura 2-7 Gráficos de series de tiempo, temperatura .............................................................. 14

Figura 2-8 Ciclo estacional velocidad del viento ........................................................................ 15

Figura 2-9 Serie de tiempo diaria velocidad promedio del viento modelada ............................ 16

Figura 2-10 Serie de tiempo dirección del viento modelada .................................................. 16

Figura 2-11 Rosa de los vientos - modelada ........................................................................... 17

Figura 2-12 Serie de tiempo temperatura modelada ............................................................... 20

Figura 2-13 Ciclo estacional velocidad del viento ................................................................... 21

Figura 2-14 Ciclo diario de velocidad del viento observado v/s modelado ............................. 22

Figura 2-15 Comparación Rosa de los Vientos observada y modelada .................................... 23

Figura 2-16 Comparación ciclo diario de dirección del viento observado y modelado ........... 24

Figura 2-17 Ciclo diario de temperatura observado y modelado ............................................ 25

Figura 2-18 Distribución espacial de los receptores................................................................. 29

Figura 2-19 Punto de mayor concentración y depositación Año 1 .......................................... 34

Figura 2-20 Mapa de Dispersión MP10 24 horas P98 .............................................................. 38

Figura 2-21 Mapa de Dispersión MP10 Anual .......................................................................... 39

Figura 2-22 Mapa de Dispersión MP2,5 24 horas P98 ............................................................. 40

Figura 2-23 Mapa de Dispersión MP2,5 Anual ......................................................................... 41

Figura 2-24 Mapa de Dispersión SO2 1 hora P98,5 .................................................................. 42

Figura 2-25 Mapa de Dispersión SO2 24 horas P99 ................................................................. 43

Figura 2-26 Mapa de Dispersión SO2 Anual ............................................................................. 44

Figura 2-27 Mapa de Dispersión SO2 24 horas P99,7 .............................................................. 45

Figura 2-28 Mapa de Dispersión SO2 1 hora P99,73 ................................................................ 46

Figura 2-29 Mapa de Dispersión NO2 Anual ............................................................................ 47

Figura 2-30 Mapa de Dispersión NO2 1 hora P99 .................................................................... 48

Figura 2-31 Mapa de Dispersión NO2 24 hora P99 .................................................................. 49

Figura 2-32 Mapa de Dispersión CO 1 hora P99 ....................................................................... 50

Figura 2-33 Mapa de Dispersión CO 8 hora P99 ....................................................................... 51

Figura 2-34 Mapa de Dispersión MPS Anual ............................................................................ 52
Figura 3-1 Área de Influencia NO2 1 hr P99 y NO2 24 hrs P99 .................................................. 54

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

iii

ENERGETICA SOLAR MEMBRILLO

**1** **INTRODUCCIÓN**

El Proyecto Energética Solar Membrillo estará ubicado en la comuna de San Pedro,
provincia de Melipilla, Región Metropolitana y corresponde a una nueva Central Solar
Fotovoltaica (CSF) que estará constituida por paneles de silicio monocristalino y considera
la construcción de una línea de tendido eléctrico de media tensión, la cual se conectará al
alimentador “El Membrillo”. En relación con lo anterior, las fuentes de emisión provendrán
principalmente de la fase de construcción del Proyecto, correspondiente a: tránsito de
caminos pavimentados y no pavimentados, combustión de motor de vehículos y maquinaria
fuera de ruta, movimientos de tierra y grupos electrógenos.

Para la fase de operación se estiman emisiones atmosféricas del tránsito vehicular asociado
a las actividades de mantenimiento del parque. Finalmente, para la fase de cierre, las
emisiones estarán asociadas a la generación de material particulado producto de las
actividades de desmantelamiento y limpieza, tránsito de vehículos por caminos
pavimentados y no pavimentados, además de gases contaminantes debido a la combustión
interna de motores de vehículos, combustión interna de motores de maquinarias y
utilización de grupos electrógenos.

El presente informe contiene los resultados de la modelación de emisiones del Proyecto,
considerando material particulado y gases.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

4

ENERGETICA SOLAR MEMBRILLO

**2** **MODELACIÓN DE CALIDAD DEL AIRE**

En este Apartado, se desarrolla la modelación de dispersión de material particulado (MPS,
MP10, MP2,5) y gases contaminantes (SO2, NO2, CO) asociado a las fuentes y actividades
del Proyecto, con base en los resultados de inventario de emisiones atmosféricas del año
de mayor emisión correspondiendo al año 1, compuesto por 6 meses de Fase de
Construcción y 6 meses de Fase de Operación.

La modelación se efectuó mediante el Software Calpuff, utilizando como input la
meteorología generada por el modelo WRF.

De acuerdo con los requerimientos metodológicos, se efectuó la recopilación,
procesamiento y selección de datos de entrada necesarios para alimentar el modelo de
dispersión.

A continuación, se presenta la data utilizada, haciendo referencia de los criterios de
selección empleados, y describiendo aquellos elementos que tengan incidencia en los
procesos de transporte y dispersión de material particulado y gases.

**2.1 Descripción del modelo utilizado**

El sistema utilizado para la modelación de dispersión de contaminantes corresponde al
Software Calpuff, el cual ha sido recomendado por la Environmental Protection Agency (US
EPA) para topografía compleja, es un modelo tipo puff de estado no-estacionario, multicapa
y multi-especies, que puede simular los efectos de varias condiciones meteorológicas sobre
el transporte, transformación, difusión, y remoción de contaminantes en la atmósfera. Las
salidas de CALPUFF consisten en concentraciones en cada punto receptor o en formato
grillado, para cada hora de modelación. Los resultados de las modelaciones, en especial,
con las isolíneas de concentraciones de contaminantes permiten definir el área de influencia
de las emisiones de las fuentes modeladas.

El módulo de transporte y dispersión de contaminantes, denominado CALPUFF entrega
como resultados las concentraciones de contaminantes. El módulo CALPOST es el

encargado del procesamiento de los archivos de salida. El WRF es un modelo
meteorológico de meso-escala, que genera los campos meteorológicos 3D que alimenta a
CALPUFF.

El sistema WRF es un modelo de mesoescala de quinta generación, corresponde a una
versión no hidrostática y compresible de un modelo desarrollado por el National Center for
Atmospheric Research (NCAR) de Estados Unidos.

**2.2 Dominio de modelación meteorológica**

En la Figura 2-1 se muestra el dominio de modelación meteorológica WRF que corresponde

a un tamaño de 55x55 km.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

5

ENERGETICA SOLAR MEMBRILLO

**Figura 2-1.** **Dominio de modelación**

**2.3 Topografía**

En la Figura 2-2, se muestra el mapa topográfico correspondiente al Proyecto y sus
alrededores.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

6

ENERGETICA SOLAR MEMBRILLO

**Figura 2-2** **Mapa topográfico 2D**

Fuente: Elaboración Propia

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

7

ENERGETICA SOLAR MEMBRILLO

**2.4 Uso de Suelo**

En la Figura 2-3, se muestra el mapa de uso de suelo asociado al Proyecto y sus
alrededores.

**Figura 2-3** **Uso de Suelo**

Fuente: Elaboración Propia

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

8

ENERGETICA SOLAR MEMBRILLO

**2.5 Selección del año de modelación**

Para la selección del año de modelación, debido a la ausencia de estaciones de calidad del
aire cercana con data actualizada disponible, se utilizaron los antecedentes registrados
promedios anuales de velocidad del viento de la estación meteorológica San Pedro de
Melipilla, ubicada en la localidad de San Pedro, distancia de 19 km del proyecto. La data
está disponible en https://agrometeorologia.cl/#

**Tabla 2-1.** **Registro de velocidad del viento Estación**

|Período|Velocidad del viento, m/s|
|---|---|
|2021|0,5|
|2022|0,5|
|2023|0,47|

_Fuente: Elaboración Propia._

De los datos expuestos en el cuadro anterior, se observa que el año 2023 presenta el menor
promedio de velocidad del viento. Al respecto, debido a que a menor velocidad del viento
la dispersión de contaminante disminuye, se selecciona este año para la modelación
meteorológica como condición desfavorable.

**2.6 Antecedentes meteorológicos para Análisis de Incertidumbre**

Para el desarrollo del análisis de incertidumbre del modelo meteorológico WRF, se utiliza
la información de la estación meteorológica, donde en la primera sección expone los
resultados estadísticos y gráficos asociado a la meteorología observada y meteorología
modelada, seguido de ello, se desarrolla un análisis comparativo tanto cualitativo como

cuantitativo.

**2.6.1 Meteorología observada**

La estación San Pedro de Melipilla está situada dentro del dominio meteorológico
modelado. El periodo considerado corresponde de enero a diciembre 2023. En la Tabla 22 se presentan las coordenadas de ubicación de la estación.

**Tabla 2-2.** **Coordenadas de ubicación referencial de estación**

|Nombre de la estación|Coordenada UTM WGS 84 H 19s (m)|Col3|
|---|---|---|
|San Pedro de Melipilla|273.194|6.246.438|

_Fuente: Elaboración Propia._

La estación posee registros cada una hora, obteniendo 8.747 datos, lo que representa un
99% de completitud.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

9

ENERGETICA SOLAR MEMBRILLO

**2.6.1.1 Velocidad del viento**

De acuerdo con la información recopilada, el promedio horario de velocidad del viento en el
periodo 2023 fue de 0,47 m/s (24 horas), mientras que la velocidad máxima fue de 4,2 m/s
registrada en agosto.

El gráfico de serie de tiempo de la variable meteorológica velocidad del viento, se
representa en la Figura 2-4.

**Figura 2-4** **Serie de tiempo velocidad del viento, m/s**

_Fuente: Elaboración Propia._

**2.6.1.2 Dirección del viento**

En Figura 2-5 se presenta la serie de tiempo de la dirección del viento, donde es posible
observar una tendencia desde Oeste y Noroeste.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

10

ENERGETICA SOLAR MEMBRILLO

**Figura 2-5** **Serie de tiempo dirección del viento promedio**

_Fuente: Elaboración Propia._

**Figura 2-6** **Rosa de los vientos,** **promedio horario**

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

11

ENERGETICA SOLAR MEMBRILLO

|Verano|Para el verano, la dirección predominante<br>corresponde a Oeste y Noroeste principalmente.<br>A continuación, se presenta la distribución de<br>frecuencia de velocidad del viento, siendo el mayor<br>porcentaje con un 53,9% las calmas, seguido de un<br>43,6% entre 0,5 - 2,1 m/s.|
|---|---|
|**Otoño**<br>|Para el otoño, la dirección predominante corresponde<br>a Suroeste y Noroeste.<br> <br>A continuación, se presenta la distribución de<br>frecuencia de velocidad del viento, siendo el mayor<br>porcentaje con un 72,8% las calmas, seguido de un<br>26,2% entre 0,5 - 2,1 m/s.<br> <br>|

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

12

ENERGETICA SOLAR MEMBRILLO

|Invierno|Para el invierno, la dirección predominante<br>corresponde a Suroeste y oeste..<br>A continuación, se presenta la distribución de<br>frecuencia de velocidad del viento, siendo el mayor<br>porcentaje con un 71,1% las calmas, seguido de un<br>26,5% entre 0,5 - 2,1 m/s.|
|---|---|
|**Primavera**<br> <br>|Para la primavera, la dirección predominante<br>corresponde a Oeste y Noroeste principalmente.<br> <br>A continuación, se presenta la distribución de<br>frecuencia de velocidad del viento, siendo el mayor<br>porcentaje con un 60,% las calmas, seguido de un<br>39% entre 0,5 - 2,1 m/s.<br> <br> <br>|

_Fuente: Elaboración Propia_

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

13

ENERGETICA SOLAR MEMBRILLO

**2.6.1.3 Temperatura**

En el gráfico de la Figura 2-7, se presenta la serie de tiempo de la temperatura registrada
de promedio horario. La media anual fue de 14 °C, mostrando menores temperaturas en
invierno, con una mínima de -3,4 °C en junio, y la máxima de 35,1 °C en marzo.

**Figura 2-7** **Gráficos de series de tiempo, temperatura**

_Fuente: Elaboración Propia._

**2.6.1.4 Ciclo estacional velocidad del viento**

Para la estación de monitoreo en superficie, se presenta la variación estacional de sus ciclos
diarios.

La Figura 2-8, muestra el ciclo diario-estacional de la velocidad del viento observada en la
estación meteorológica, donde se puede apreciar que las mayores velocidades se
presentan en primavera y verano desde las 10:00 a 20:00 hrs.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

14

ENERGETICA SOLAR MEMBRILLO

**Figura 2-8** **Ciclo estacional velocidad del viento**

_Fuente: Elaboración Propia._

**2.6.2 Meteorología modelada WRF**

Los campos meteorológicos 3D que alimenta a Calpuff, se desarrollaron a partir de
meteorología de pronóstico WRF (Weather Research and Forecasting), con dominio de
55x55 km y resolución horizontal de 1 km, para el periodo desde el 01-01-2023 al 31-12
2023.

En el presente apartado, se entregan los gráficos y análisis de series de tiempo, ciclos
diarios y estacionales y rosa de los vientos de la meteorología modelada, en la ubicación
donde se emplaza la estación de monitoreo, así como los mapas de vientos de la
meteorología modelada en el contexto del dominio.

**2.6.2.1 Velocidad del viento**

La Figura 2-9 presenta la serie de tiempo de la velocidad del viento modelada.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

15

ENERGETICA SOLAR MEMBRILLO

**Figura 2-9** **Serie de tiempo diaria velocidad promedio del viento modelada**

_Fuente: Elaboración Propia._

De la figura precedente se observa, en términos generales, que las mayores velocidades
se presentan en los meses de verano, invierno y primavera. El promedio anual es de 2,5
m/s. La máxima velocidad promedio horario modelada corresponde a 10,6 m/s y se
presenta en agosto.

**2.6.2.2 Dirección del viento**

La Figura 2-10 presenta la serie de tiempo, promedio horario anual, de la dirección del
viento modelada, la cual tiene componentes principales de Noreste (NO).

**Figura 2-10** **Serie de tiempo dirección del viento modelada**

_Fuente: Elaboración Propia._

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

16

ENERGETICA SOLAR MEMBRILLO

A continuación, se presenta a continuación en la Figura 2-11, se presenta la rosa de los
vientos de la meteorología modelada.

**Figura 2-11** **Rosa de los vientos - modelada**

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

17

ENERGETICA SOLAR MEMBRILLO

|Verano|Para el verano, la dirección predominante<br>corresponde Oeste, con inclinación norte.<br>Se presenta la distribución de frecuencia de velocidad<br>del viento, siendo el mayor porcentaje entre 0,5 - 2,1<br>m/s.|
|---|---|
|**Otoño**<br>|Para el otoño, la dirección la dirección predominante<br>corresponde a Noroeste y Sureste.<br> <br>A continuación, se presenta la distribución de<br>frecuencia de velocidad del viento, siendo el mayor<br>porcentaje entre 0,5 - 2,1 m/s.<br> <br>|

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

18

ENERGETICA SOLAR MEMBRILLO

|Invierno|Para el invierno, la dirección la dirección promedio<br>predominante corresponde a Suroeste.<br>A continuación, se presenta la distribución de<br>frecuencia de velocidad del viento, siendo el mayor<br>porcentaje entre 0,5 - 2,1 m/s.|
|---|---|
|**Primavera**<br>|Para el año completo, la dirección predominante<br>corresponde Oeste, con inclinación norte.<br> <br>Se presenta la distribución de frecuencia de<br>velocidad del viento, siendo el mayor porcentaje<br>entre 0,5 - 2,1 m/s.<br> <br> <br>|

_Fuente: Elaboración Propia._

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

19

ENERGETICA SOLAR MEMBRILLO

**2.6.2.3 Temperatura**

En Figura 2-12 se presenta la serie de tiempo promedio horario anual, de la temperatura
modelada.

**Figura 2-12** **Serie de tiempo temperatura modelada**

_Fuente: Elaboración Propia._

En la figura anterior, se muestra en promedio temperaturas bajas en invierno y mayores en
verano, la máxima de 33,8 °C registrada en febrero y la mínima de 4,3°C en junio. La
temperatura promedio modelada en el periodo corresponde a 15,1°C.

**2.6.2.4 Ciclo estacional**

Para la meteorología modelada, se presenta la variación estacional de sus ciclos diarios.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

20

ENERGETICA SOLAR MEMBRILLO

**Figura 2-13** **Ciclo estacional velocidad del viento**

_uente: Elaboración Propia._

La Figura 2-13 muestra el ciclo diario-estacional de la velocidad del viento modelada, donde
se aprecia que las mayores velocidades se presentan en meses verano entre las 10:00 y

20 horas.

**2.6.3 Análisis cualitativo y cuantitativo de modelación meteorológica v/s**

**meteorología observada**

Se generó la modelación meteorológica utilizando el modelo WRF para el periodo anual 0101-2023 al 31-12-2023. Los resultados de la modelación meteorológica WRF, fueron
contrastados con los datos medidos en la estación de monitoreo, con el fin de analizar y
evaluar su desempeño, entendido éste como la similitud entre los valores observados y los
modelados.

**2.6.3.1 Análisis cualitativo**

En el entendido sobre la importancia que tiene la meteorología de superficie en la incidencia
en la dispersión de contaminantes, en este apartado se desarrolla el análisis cualitativo,
que busca comparar la meteorología observada y modelada, respecto a series de tiempo,
ciclos diarios y estacionales, así como la rosa de los vientos por estación del año para las
variables velocidad del viento, dirección del viento y temperatura en el periodo enero
diciembre 2023.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

21

ENERGETICA SOLAR MEMBRILLO

**2.6.3.2 Velocidad y dirección del viento**

En la Figura 2-14 se compara los gráficos de ciclos diarios de velocidad del viento
observada y modelada.

**Figura 2-14** **Ciclo diario de velocidad del viento observado v/s modelado**

_Fuente: Elaboración Propia._

De la figura anterior se observa que el promedio de la velocidad del viento, en el grafico
observado es menor a la temperatura observada, sin embargo, presentan una curva similar
durante el día, con temperaturas bajas durante la noche que se incrementan durante el día.

La

Figura 2-15 presenta la comparación de la rosa de los vientos del periodo anual entre
meteorología observada y modelada, donde es posible apreciar que la meteorología

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

22

ENERGETICA SOLAR MEMBRILLO

modelada presenta las mayores intensidades de viento con componentes principalmente
Noroeste, similares a la meteorología observada.

|Figura 2-15 Comparación Rosa de|los Vientos observada y modelada|
|---|---|
|Rosa del viento anual observada|Rosa del viento anual modelada|
|<br>|<br>|

_Fuente: Elaboración Propia._

En la

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

23

ENERGETICA SOLAR MEMBRILLO

Figura 2-16 se presenta la comparación de ciclo diario de dirección del viento observado y
modelado, donde es posible observar similitudes horario diurno y nocturno.

**Figura 2-16** **Comparación ciclo diario de dirección del viento observado y modelado**

Ciclo diario dirección del viento observado

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

24

ENERGETICA SOLAR MEMBRILLO

|Col1|Col2|Col3|
|---|---|---|
||||
|Ciclo diario dirección del viento modelado|Ciclo diario dirección del viento modelado|Ciclo diario dirección del viento modelado|
|Ciclo diario dirección del viento modelado|||
|Ciclo diario dirección del viento modelado|||

_Fuente: Elaboración Propia._

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

25

ENERGETICA SOLAR MEMBRILLO

**2.6.3.3 Temperatura**

En la Figura 2-17 se compara los gráficos de ciclos diarios de temperatura observada y
modelada.

**Figura 2-17** **Ciclo diario de temperatura observado y modelado**

_Fuente: Elaboración Propia._

De la Figura 2-17 se observa que, tanto la temperatura modelada como la observada,
presentan valores similares durante el transcurso del día.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

26

ENERGETICA SOLAR MEMBRILLO

**2.6.3.4 Análisis cuantitativo**

Para el análisis de incertidumbre, tal como lo expone la Guía de Uso de Modelos de Calidad
del Aire en el SEIA, 2023, el análisis cuantitativo se debe realizar calculando como mínimo
las métricas estadísticas del sesgo (error medio o BIAS), error absoluto medio (MAE) y la
raíz del error cuadrático medio (RMSE), cuyas ecuaciones se presentan a continuación.

**Ecuación 2-1**

Donde:

n: Cantidad de datos

S: Valores obtenidos del modelo

0: Valores observados en estaciones meteorológicas

Tanto BIAS como MAE son estimadores de la diferencia entre el valor modelado y
observado de un mismo fenómeno, en este caso meteorológico. De igual forma, RMSE es
un estimador de la frecuencia de las diferencias entre los valores observados y modelados,
siendo especialmente sensible a los valores atípicos, por lo tanto, a mayor diferencia entre
estos valores menor será el grado de ajuste de este estadístico. A su vez, a las métricas
señaladas se recomienda incorporar el coeficiente de correlación (r), que corresponde a
una medida de la correlación lineal entre dos conjuntos de variables, siendo para este caso,
los valores modelados y observados.

Las métricas estadísticas recomendadas por la mencionada Guía son los siguientes:

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

27

ENERGETICA SOLAR MEMBRILLO

**Tabla 2-3.** **Métricas estadísticas recomendables en el análisis de incertidumbre para las**

**variables**

|Estadístico|Velocidad del viento, m/s- (10 m)|Temperatura, °C (2 metros)|
|---|---|---|
|**BIAS**|[-2,5;2,5] (m/s)|[-4;4] (°C)|
|**MAE**|<= 3 (m/s)|<=4 (°C)|
|**RMSE**|<= 3,5 (m/s)|<=4,5(°C)|
|**r **|>0,6|>0,8|

Fuente: Tabla 2 Guía de Uso de Modelos de Calidad del Aire en el SEIA, 2023.

Con ello, los valores obtenidos de las métricas estadísticas corresponden a los siguientes:

**Tabla 2-4.** **Métricas estadísticas calculadas**

|Estadístico|Velocidad del viento, m/s|Temperatura, °C|
|---|---|---|
|**BIAS**|2,07|2,16|
|**MAE**|2,08|2,68|
|**RMSE**|2,45|3,47|
|**r **|0,67|0,91|

_Fuente: Elaboración Propia._

Conforme a los resultados presentados, todos los estadísticos evaluados se encuentran
dentro de los rangos recomendados en la Guía de Uso de Modelos de Calidad del Aire en
el SEIA, 2023. Por lo tanto, podemos señalar que el modelo representa de forma correcta
la meteorología del área del proyecto.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

28

ENERGETICA SOLAR MEMBRILLO

**2.7 Receptores de interés y ubicación**

A continuación, se presenta emplazamiento de receptores considerados para la evaluación.

**2.7.1 Receptores humanos**

Los receptores de interés considerados en el modelo de dispersión de contaminante, para
evaluar la calidad del aire primaria se exponen en la Tabla 2-5 con su respectiva
coordenada de ubicación referencial y en la Figura 2-18 se muestra la distribución espacial
de estos receptores.

**Tabla 2-5.** **Receptores humanos y coordenadas de ubicación referencial**

|Receptor|Coordenadas UTM WGS 84 H 19s|Col3|
|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|
|R01|288.625|6.235.514|
|R02|288.788|6.235.549|
|R03|289.147|6.235.530|
|R04|289.324|6.235.404|
|R05|289.548|6.235.588|
|R06|288.887|6.234.962|
|R07|288.485|6.235.269|
|R08|288.446|6.235.404|

_Fuente: Elaboración Propia._

**Tabla 2-6.** **Receptores Fauna y coordenadas de ubicación referencial**

|Receptor|Coordenadas UTM WGS 84 H 19s|Col3|
|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|
|F1|288.995|6.235.228|
|F2|289.354|6.235.575|

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

29

ENERGETICA SOLAR MEMBRILLO

**Figura 2-18** **Distribución espacial de los receptores**

_Fuente: Elaboración Propia._

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

30

ENERGETICA SOLAR MEMBRILLO

**2.7.2 Normativa**

La normativa de calidad del aire utilizada como referencia para comparar la concentración
de material particulado y gases generados por el Proyecto, se presenta en el Tabla 2-7.

**Tabla 2-7.** **Normativa primaria y secundaria de calidad del aire utilizada**

|Parámetro|Estadístico|Valor Normado|Normativa|
|---|---|---|---|
|MP10|Anual|50 μg/m3|D.S. N° 12/2022 MMA|
|MP10|Percentil 98 24 horas|130 μg/m3|130 μg/m3|
|MP2,5|Anual|20 μg/m3|D.S. N° 12/2010 MMA|
|MP2,5|Percentil 98 24 horas|50 μg/m3|50 μg/m3|
|NO2|Anual|40 μg/m3|D.S. N° 40/2024 MMA|
|NO2|Percentil 99 1 hora|200 μg/m3|200 μg/m3|
|NO2|Percentil 98 24 horas|100 μg/m3|100 μg/m3|
|CO|Percentil 99 8 horas|10.000 μg/m3|D.S. N°115/02 MINSEGPRES|
|CO|Percentil 99 1 hora|30.000 μg/m3|30.000 μg/m3|
|SO2|Percentil 98,5 1 hora|350 μg/m3|D.S. N°104/18 MMA|
|SO2|Anual|60 μg/m3|60 μg/m3|
|SO2|Percentil 99 24 horas|150 μg/m3|150 μg/m3|
|SO2 (secundario)|Anual|80 μg/m3|D.S. N°22/2010 MINSEGPRES|
|SO2 (secundario)|Percentil 99,7 24 horas|365 μg/m3|365 μg/m3|
|SO2 (secundario)|Percentil 99,73 1 hora|1000 μg/m3|1000 μg/m3|
|MPS*|Anual|200 mg/m2_dia|Norma de Confederación Suiza|

_Fuente: Elaboración Propia._

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

31

ENERGETICA SOLAR MEMBRILLO

**2.7.3 Escenario de modelación**

El escenario de modelación corresponde al año de mayor emisión del Proyecto
correspondiendo al año 1, compuesto por 6 meses de Fase de Construcción y 6 meses de
Fas de Operación.

**Tabla 2-8.** **Resumen de emisiones atmosféricas por año cronológico del proyecto.**

|FASE DE CONSTRUCCIÓN + OPERACIÓN (6 MESES)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**EMISIONES (t/fase)**|**EMISIONES (t/fase)**|**EMISIONES (t/fase)**|**EMISIONES (t/fase)**|**EMISIONES (t/fase)**|**EMISIONES (t/fase)**|
|**ACTIVIDAD**|**MP**2,5|**MP**10|**MPS**|**NOx**|**SOx**|**CO**|
|Excavación|0,0144|0,0278|0,1371||||
|Nivelación|0,0348|0,3288|1,1234||||
|Compactación|0,0128|0,0247|0,1217||||
|Transferencia de material|0,0014|0,0090|0,0189||||
|Tránsito de vehículos por caminos pavimentados|0,0650|0,2689|1,4007||||
|Tránsito de vehículos por caminos no pavimentados|0,0486|0,4859|1,7007||||
|Combustión interna de motores de vehículos por caminos pavimentados|0,0020|0,0020|0,0020|0,1723|0,0005|0,0090|
|Combustión interna de motores de vehículos por caminos no pavimentados|0,0000|0,0000|0,0000|0,0014|0,0000|0,0001|
|Combustión de motores de maquinarias|0,1247|0,1247|0,1247|2,2788|0,0028|0,8071|
|Grupo electrógeno|0,0407|0,0407|0,0407|0,5778|0,0380|0,1244|
|**TOTAL**|**0,3445**|**1,3126**|**4,6699**|**3,0302**|**0,0414**|**0,9406**|

_Fuente: Elaboración Propia._

**2.7.4 Entradas al modelo**

Las tasas de emisión ingresadas al modelo se basan en los siguientes criterios:

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

32

ENERGETICA SOLAR MEMBRILLO

**Tabla 2-9.** **Tasas de emisión de fase de construcción del Proyecto**

|Tipo|ID|Descripción|Valor<br>(m2, m)|Tiempo, seg|MP2,5|MP10|MPS|NO2|SO2|CO|
|---|---|---|---|---|---|---|---|---|---|---|
|AREA_POLY|SRC_1|Movimiento de<br>Tierra|158.135|1728000|2,32016E-07|1,4283E-06|5,1274E-06|-|-|-|
|ROAD|SRC_2|Camino<br>pavimentado|30000|5184000|4,31321E-07|1,7419E-06|9,0195E-06|1,1077E-06|3,3128E-09|5,8026E-08|
|LINE_AREA|SRC_3|Camino no<br>pavimentado|9200|5184000|1,01931E-06|1,0189E-05|3,5659E-05|2,8742E-08|8,3127E-11|1,4196E-09|
|AREA_POLY|SRC_4|Maquinaria|158.135|5184000|1,52163E-07|1,5216E-07|1,5216E-07|2,7798E-06|3,4722E-09|9,8458E-07|
|POINT|SRC_5|GE01|-|9504000|0,00143|0,00143|0,00143|0,02027|0,00133|0,00436|
|POINT|SRC_6|GE02|GE02|GE02|0,00143|0,00143|0,00143|0,02027|0,00133|0,00436|
|POINT|SRC_7|GE03|GE03|GE03|0,00143|0,00143|0,00143|0,02027|0,00133|0,00436|

_Fuente: Elaboración Propia._

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

33

ENERGETICA SOLAR MEMBRILLO

**2.8 Resultados en punto de mayor concentración**

A continuación, en Tabla 2-10 y Figura 2-19 se presenta el valor más la ubicación de los
puntos de máxima concentración del Proyecto por cada contaminante.

**Tabla 2-10.** **Resultados punto de mayor concentración y depositación Año 1**

|Parámetro|Estadístico|Unidad|Valor<br>modelado|Coordenada UTM,<br>WGS 84, Huso 19|Col6|Coordenadas LCC|Col8|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Unidad**|**Valor**<br>**modelado**|**Este (m) **|**Norte (m) **|**X, m**|**Y, m**|
|MP10|Anual|μg/m3|0,82|288.995|6.235.228|1407|-264,1|
|MP10|24 horas<br>P98|μg/m3|2,36|288.995|6.235.228|1407|-264,1|
|MP2,5|Anual|μg/m3|0,2|288.995|6.235.228|1407|-264,1|
|MP2,5|24 horas<br>P98|μg/m3|0,63|288.995|6.235.228|1407|-264,1|
|SO2|1 hora<br>Percentil<br>98,5|μg/m3|0,22|288.995|6.235.228|1407|-264,1|
|SO2|Anual|μg/m3|0,01|288.995|6.235.228|1407|-264,1|
|SO2|24 horas<br>Percentil 99|μg/m3|0,05|288.995|6.235.228|1407|-264,1|
|SO2 <br>(secundario)|Anual|μg/m3|0,01|288.995|6.235.228|1407|-264,1|
|SO2 <br>(secundario)|Percentil<br>99,7; 24<br>horas|μg/m3|0,06|288.788|6.235.549|1207|67.0|
|SO2 <br>(secundario)|Percentil<br>99,73; 1<br>hora|μg/m3|0,34|288.995|6.235.228|1407|-264,1|
|CO|1 hora<br>Percentil 99|μg/m3|9,92|288.995|6.235.228|1407|-264,1|
|CO|8 hora<br>Percentil 99|μg/m3|5,34|289.548|6.235.588|1563|38,0|
|NO2|1 hora<br>Percentil 99|μg/m3|28,3|288.995|6.235.228|1407|-264,1|
|NO2|24 horas<br>Percentil 99|μg/m3|9,35|288.995|6.235.228|1407|-264,1|
|NO2|Anual|μg/m3|1,99|288.995|6.235.228|1407|-264,1|
|MPS|Anual|mg/m2_dia|11,2|288.995|6.235.228|1407|-264,1|

_Fuente: Elaboración Propia._

A continuación, en la figura a continuación se representa el punto de mayor concentración
y depositación obtenido de la modelación.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

34

ENERGETICA SOLAR MEMBRILLO

**Figura 2-19** **Punto de mayor concentración y depositación Año 1**

_Fuente: Elaboración Propia._

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

35

ENERGETICA SOLAR MEMBRILLO

De acuerdo a los resultados obtenidos, los puntos de mayor concentración y depositación,
se encuentran ubicados cercanos a las fuentes de emisión.

**2.9 Comparación con norma de calidad**

**2.9.1 Comparación con norma de calidad escenario Año 1**

A continuación, en las tablas siguientes, se presentan los valores de los resultados
obtenidos de la modelación de calidad del aire en los receptores, presentando además la
relación porcentual del aporte del Proyecto con respecto a la normativa de referencia
utilizada.

**Tabla 2-11.** **Aporte en receptores humanos - Año 1**

|Receptores|MP10|Col3|MP2,5|Col5|NO2|Col7|Col8|CO|Col10|SO2|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptores**|**24 horas**<br>**P98**|**Anual**|**24**<br>**horas**<br>**P98**|**Anual**|**1 **<br>**hora**<br>**P99**|**24**<br>**hrs**<br>**P99**|**Anual**|**1 **<br>**hora**<br>**P99**|**8 **<br>**horas**<br>**P99**|**24**<br>**horas**<br>**P99**|**Anual**|**1 hora**<br>**Percentil**<br>**98,5**|
|R_1|0,73|0,12|0,21|0,04|9,72|4,04|0,39|3,47|2,37|0,01|0,00|0,02|
|R_2|1,44|0,26|0,40|0,06|16,73|6,12|0,68|5,70|3,58|0,05|0,00|0,06|
|R_3|1,40|0,24|0,56|0,08|18,63|9,01|0,90|6,50|5,34|0,02|0,00|0,07|
|R_4|1,19|0,23|0,46|0,07|11,10|7,76|0,85|3,91|3,48|0,02|0,00|0,04|
|R_5|0,59|0,10|0,21|0,03|4,28|3,56|0,29|1,48|1,73|0,01|0,00|0,01|
|R_6|0,95|0,14|0,28|0,04|8,80|6,23|0,48|3,17|3,15|0,02|0,00|0,04|
|R_7|0,94|0,09|0,36|0,03|1,70|5,39|0,30|0,59|3,64|0,01|0,00|0,00|
|R_8|0,56|0,07|0,16|0,02|1,74|2,97|0,20|0,61|1,75|0,01|0,00|0,00|
|Normativa,<br>μg/m3|130|50|50|20|200|100|40|30000|10000|150|60|350|

_Fuente: Elaboración Propia._

**Tabla 2-12** **Relación porcentual del aporte respecto a normativa en receptores humanos**

**Año 1**

|Receptores|MP10|Col3|MP2,5|Col5|NO2|Col7|Col8|CO|Col10|SO2|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptores**|**24 horas**<br>**P98**|**Anual**|**24**<br>**horas**<br>**P98**|**Anual**|**1 **<br>**hora**<br>**P99**|**24**<br>**hrs**<br>**P99**|**Anual**|**1 **<br>**hora**<br>**P99**|**8 **<br>**horas**<br>**P99**|**24**<br>**horas**<br>**P99**|**Anual**|**1 hora**<br>**Percentil**<br>**98,5**|
|R_1|0,56%|0,24%|0,43%|0,18%|4,86%|4,04%|0,98%|0,01%|0,02%|0,01%|0,00%|0,01%|
|R_2|1,11%|0,52%|0,79%|0,32%|8,37%|6,12%|1,70%|0,02%|0,04%|0,03%|0,01%|0,02%|
|R_3|1,08%|0,49%|1,11%|0,38%|9,31%|9,01%|2,24%|0,02%|0,05%|0,02%|0,00%|0,02%|
|R_4|0,92%|0,46%|0,91%|0,37%|5,55%|7,76%|2,12%|0,01%|0,03%|0,01%|0,00%|0,01%|
|R_5|0,45%|0,20%|0,43%|0,15%|2,14%|3,56%|0,72%|0,00%|0,02%|0,01%|0,00%|0,00%|
|R_6|0,73%|0,27%|0,56%|0,21%|4,40%|6,23%|1,21%|0,01%|0,03%|0,01%|0,00%|0,01%|
|R_7|0,72%|0,17%|0,72%|0,13%|0,85%|5,39%|0,76%|0,00%|0,04%|0,01%|0,00%|0,00%|
|R_8|0,43%|0,14%|0,32%|0,09%|0,87%|2,97%|0,49%|0,00%|0,02%|0,00%|0,00%|0,00%|

_Fuente: Elaboración Propia._

De acuerdo con los resultados presentados en los cuadros precedentes, el aporte de MP 10,
MP 2,5, CO, SO 2 y NO 2 en los receptores humanos considerados, no supera las normas de
calidad del aire, presentadas en la Tabla 2-7.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

36

ENERGETICA SOLAR MEMBRILLO

A continuación, en las tablas siguientes, se presentan los resultados asociados a la de la
depositación de material particulado sedimentable (MPS) y SO 2 en los receptores discretos
considerados.

**Tabla 2-13.** **Aporte de MPS y SO** **2** **en receptores discretos Año 1**

|Receptores|SO2, μg/m3|Col3|Col4|MPS, mg/m2 día|
|---|---|---|---|---|
|**Receptores**|**1 hr horas P99,73**|**Anual**|**24 hora Percentil 99,7**|**Anual**|
|F01|0,34|0,01|0,05|11,20|
|F02|0,104|0,001|0,014|1,301|
|**Normativa**|**1000**|**80**|**365**|**200**|

_Fuente: Elaboración Propia._

**Tabla 2-14.** **Relación porcentual del aporte de MPS y SO** **2** **en receptores discretos Año 1**

|Receptores|SO<br>2|Col3|Col4|MPS|
|---|---|---|---|---|
|**Receptores**|**1 hr horas P99,73**|**Anual**|**24 hora Percentil 99,7**|**Anual**|
|F01|0,03%|0,02%|0,01%|5,60%|
|F02|0,01%|0,00%|0,00%|0,65%|

_Fuente: Elaboración Propia._
De los resultados expuestos en los cuadros precedentes, los valores obtenidos de MPS en
receptores discretos Fauna, no son significativos respecto de los umbrales establecidos la
Norma de Confederación Suiza.

Del mismo modo, los valores obtenidos de SO 2 secundario en receptores discretos (flora y
vegetación), no son significativos respecto a los umbrales establecidos en el D.S.
N°22/2010 MINSEGPRES, Norma de Calidad Secundaria de Aire para Anhídrido Sulfuroso
(SO 2 ).

**2.10 Evaluación del impacto de las emisiones atmosféricas de material**

**particulado respirable MP** **10** **y MP** **2,5** **en Zonas Saturadas.**

La Guía “Criterio de evaluación en el SEIA: Impacto de emisiones en zonas saturadas por
material particulado respirable MP10 y material particulado fino respirable MP2,5” en
adelante la “Guía”, establece los criterios para definir el concepto de “aumento o
disminución significativos”, concepto contenido en el literal a) del artículo 5° del Reglamento
del SEIA, para la evaluación del riesgo para la salud y el uso de normas primarias de calidad
ambiental vigentes.

Debido a que el Proyecto se ubica en la Región Metropolitana, zona que se encuentra
declarada saturada por Material Particulado Respirable MP10 en el DS N° 131/1996 del
MINSEGPRES y por MP2,5 en el DS N° 67/2014 del MMA, se evalúa el impacto de las
emisiones atmosféricas de material particulado respirable de acuerdo con la Guía
mencionada en el párrafo anterior.

El escenario más desfavorable en cuanto a la generación de emisiones atmosféricas
corresponde al año correspondiente a la Fase de Operación más Construcción, para lo cual,
corresponde evaluar la significancia con la Tabla-1 de la Guía.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

37

ENERGETICA SOLAR MEMBRILLO

**Tabla 2-15** **Comparación de los resultados de la modelación en receptores humanos y valores de**

**significancia de la Tabla 2 de la Guía, para la fase de construcción.**

|Receptores|MP (ug/m3)<br>10|Col3|MP (ug/m3)<br>2,5|Col5|
|---|---|---|---|---|
|**Receptores**|**24 horas P98**|**Anual**|**24 horas P98**|**Anual**|
|R1|0,73|0,12|0,21|0,04|
|R2|1,44|0,26|0,40|0,06|
|R3|1,40|0,24|0,56|0,08|
|R4|1,19|0,23|0,46|0,07|
|R5|0,59|0,10|0,21|0,03|
|R6|0,95|0,14|0,28|0,04|
|R7|0,94|0,09|0,36|0,03|
|R8|0,56|0,07|0,16|0,02|
|**Valor Significancia**<br>**(Tabla-2, 12 meses)**|**5,00**|**1,00**|**1,71**|**0,33**|

_Fuente: Elaboración Propia_

De acuerdo con la Tabla 2-15, la concentración de material particulado MP10 y MP2,5 en
los receptores humanos, se encuentra por debajo de los valores de significancia
establecidos para en la Tabla 1, (Año 1: fase de construcción más operación 6 meses).

Considerando las evaluaciones realizadas, lo anterior se hace extensivo para la fase de
operación y cierre del proyecto, al presentar una menor generación de emisiones que el
escenario construcción más operación.

**2.11 Mapas de isoconcentraciones e isodepositaciones (MPS)**

En esta sección, se presentan los mapas de isoconcentraciones de MP 10, MP 2,5, SO 2, CO,
NO 2, e isodepositaciones de MPS. En estos mapas es posible observar el bajo aporte de
las emisiones mediante su dispersión, no representando un aporte significativo en los
receptores considerados.

**2.11.1 Año 1: Mapas de Isoconcentración e isodepositación**

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

38

ENERGETICA SOLAR MEMBRILLO

**Figura 2-20** **Mapa de Dispersión MP10 24 horas P98**

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

39

ENERGETICA SOLAR MEMBRILLO

**Figura 2-21** **Mapa de Dispersión MP10 Anual**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

40

ENERGETICA SOLAR MEMBRILLO

**Figura 2-22** **Mapa de Dispersión MP2,5 24 horas P98**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

41

ENERGETICA SOLAR MEMBRILLO

**Figura 2-23** **Mapa de Dispersión MP2,5 Anual**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

42

ENERGETICA SOLAR MEMBRILLO

**Figura 2-24** **Mapa de Dispersión SO2 1 hora P98,5**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

43

ENERGETICA SOLAR MEMBRILLO

**Figura 2-25** **Mapa de Dispersión SO2 24 horas P99**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

44

ENERGETICA SOLAR MEMBRILLO

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

**Figura 2-26** **Mapa de Dispersión SO2 Anual**

45

ENERGETICA SOLAR MEMBRILLO

**Figura 2-27** **Mapa de Dispersión SO2 24 horas P99,7**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

46

ENERGETICA SOLAR MEMBRILLO

**Figura 2-28** **Mapa de Dispersión SO2 1 hora P99,73**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

47

ENERGETICA SOLAR MEMBRILLO

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

**Figura 2-29** **Mapa de Dispersión NO2 Anual**

48

ENERGETICA SOLAR MEMBRILLO

**Figura 2-30** **Mapa de Dispersión NO2 1 hora P99**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

49

ENERGETICA SOLAR MEMBRILLO

**Figura 2-31** **Mapa de Dispersión NO2 24 hora P99**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

50

ENERGETICA SOLAR MEMBRILLO

**Figura 2-32** **Mapa de Dispersión CO 1 hora P99**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

51

ENERGETICA SOLAR MEMBRILLO

**Figura 2-33** **Mapa de Dispersión CO 8 hora P99**

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

52

ENERGETICA SOLAR MEMBRILLO

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

**Figura 2-34** **Mapa de Dispersión MPS Anual**

53

ENERGETICA SOLAR MEMBRILLO

**3** **ÁREA DE INFLUENCIA**

El área de influencia corresponde al espacio geográfico cuyos atributos, elementos naturales o
socioculturales deben ser considerados con la finalidad de definir si el proyecto o actividad genera
o presenta alguno de los efectos, características o circunstancias del artículo 11 de la Ley N°
19.300, o bien para justificar su inexistencia. (Ref. letra a) del artículo 2 del Reglamento del SEIA).
Dada esta definición, se efectuó una delimitación del área de influencia considerando los
siguientes factores:

Distancia de dispersión material particulado y gases, cuyos antecedentes fueron
obtenidos de la modelación de calidad del aire.

Distancia de receptores de interés humano cercanos al proyecto.

Isolínea de mayor extensión que representa el 1%, correspondiente a NO2 1 hr P99 y
NO2 24 hrs P99. Este criterio se basa en documento consultado como referencia

“Significance in air quality November 20091” del Institute of Air Quality Management, UK,
se indica, un cambio de magnitud inferior al 1% del umbral, es considerado como
imperceptible

Cabe destacar que concentraciones modeladas de MP 10, MP 2,5, MPS, NO 2, SO 2 y CO no son
significativas respecto a las normas de calidad del aire usadas como referencia.

Por lo expuesto anteriormente, es posible inferir con los resultados de la modelación que el
Proyecto no presenta alguno de los efectos, características o circunstancias del artículo 11 de la
Ley N°19.300.

Con todo lo anterior, se definió el área de influencia para la componente calidad del aire,
representada geográficamente en la Figura 3-1, es de aproximadamente 988 ha.

1 [https://www.iaqm.co.uk/text/guidance/iaqm_significance_nov09.pdf](https://www.iaqm.co.uk/text/guidance/iaqm_significance_nov09.pdf)

Anexo N° 2.3 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

54

ENERGETICA SOLAR MEMBRILLO

**Figura 3-1** **Área de Influencia NO2 1 hr P99 y NO2 24 hrs P99**

_Fuente: Elaboración Propia_

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

55

ENERGETICA SOLAR MEMBRILLO

**4** **ESCENARIO SINÉRGICO**

**4.1 Consideraciones**

Para el desarrollo del escenario sinérgico se han considerado los siguientes criterios:

−
Identificación de proyectos aprobados en el SEIA de hasta 5 años atrás, que se
intercepten con el área de influencia del Proyecto Energética Solar Membrillo.

−
Revisión del estado e información de proyectos disponibles en el sitio web del Sistema
Nacional de Información de Fiscalización Ambiental de la Superintendencia del Medio
Ambiente.

−
Análisis de la información, basado en antecedentes disponibles entregados por los
titulares de los proyectos aprobados. Esto incluye revisión en la página web del
Sistema de Evaluación Ambiental.

−
Se considera en el análisis sinérgico aquellos proyectos que han presentado
modelación de calidad del aire.

Conforme al listado mencionado anteriormente, no se identifica Proyectos que cuenten con los
criterios indicados. Al respecto, no se identifica la generación de un escenario sinérgico.

**5** **EVALUACIÓN DE RIESGO A LA SALUD DE LA POBLACIÓN POR EMISIONES**
**ATMOSFÉRICAS**

La Evaluación de Riesgo a la Salud de Población por las emisiones atmosféricas generadas por
el Proyecto, se realiza en base a la Guía de Riesgo a la Salud Riesgo a la Salud, del SEA [2] .

**5.1** **Criterios para Evaluar la Generación o Presencia del Efecto, Característica o**
**Circunstancia de la Letra a) del Artículo 11 de la Ley N° 19.300**

En el punto 3.2 de la Guía mencionada, se establecen los criterios para evaluar la generación o
presencia de los efectos, características o circunstancias de la Letra a) del Art. 11 de la Ley
N°19.300. A continuación, se exponen los criterios indicados en dicho punto de la Guía, que
deben verificarse, para cada contaminante o mezcla de contaminantes, para evaluar la
generación o presencia de riesgo para la salud, en el orden planteado:

2 [https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/03/08/Guia.pdf](https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/03/08/Guia.pdf)

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

56

ENERGETICA SOLAR MEMBRILLO

**Tabla 5-1** **Criterios para evaluación la generación o presencia de los efectos**
**características o circunstancia de la Letra a) del Art. 11 Ley 19.300**

|Criterio|Análisis|
|---|---|
|a) Superación de valores de concentración y<br>períodos establecidos en normas primarias<br>de calidad ambiental nacional.|De acuerdo a los resultados de máxima<br>concentración obtenidos de la modelación de<br>calidad del Aire, presentados en la Tabla<br>2-10, Tabla 2-11 y Tabla 2-12 el aporte del<br>Proyecto no supera los valores establecidos<br>en las normas primarias de calidad del aire.<br>Se debe tener en consideración que la RM se<br>encuentra saturada por MP10 y MP2,5por lo<br>tano existe un riesgo pre-existente el cual<br>será analizado en la letra c) de esta tabla.|
|b) Superación de valores de concentración y<br>períodos establecidos en normas primarias<br>de calidad ambiental de los Estados que<br>señala el Reglamento del SEIA|Se utilizó norma primaria de calidad de aire<br>Nacional.|
|c) Aumento del riesgo pre-existente|El área que se emplaza el Proyecto está<br>declarada como saturada.<br>De acuerdo a los resultados de máxima<br>concentración obtenidos de la modelación de<br>calidad del Aire, presentados en la Tabla<br>2-10, Tabla 2-11 y Tabla 2-12 y respecto a los<br>umbrales establecidos en las Tabla 1 y Tabla<br>2 del documento “_Criterio de Evaluación en el_<br>_SEIA: Impacto de emisiones en zonas_<br>_saturadas por material particulado respirable_<br>_MP10 y material particulado fino respirable_<br>_MP2,5_” el aporte del Proyecto en todas sus<br>Fases no supera valores establecidos en el<br>año de mayor emisión, por lo tanto,<br>corresponden a valores no significativos para<br>la evaluación de impacto en un escenario de<br>riesgo preexistente, con ello se concluye que<br>las emisiones atmosféricas generadas por el<br>Proyecto, no afectan a la salud de la<br>población.. .|
|d) Superación de los valores establecidos en<br>las normas de emisión.|Las<br>emisiones<br>del<br>Proyecto<br>son<br>principalmente<br>polvo<br>resuspendido<br>por<br>tránsito vehicular,|

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

57

ENERGETICA SOLAR MEMBRILLO

|Criterio|Análisis|
|---|---|
||Cabe<br>destacar<br>que<br>no<br>se<br>presenta<br>superación de normas de calidad del aire.|

Es importante indicar que las mayores emisiones del Proyecto se generan durante la Fase de
Operación más Fase de Construcción, cuya magnitud de las concentraciones para todos los
contaminantes analizados se encuentran bajo los límites normados y de las normativas de
referencia utilizadas, y que la extensión de dichas emisiones se limita al área circundante del
proyecto, tal como se expone en los mapas de isoconcentraciones de la Sección 13.12 del
presente documento.

Por lo tanto, es posible concluir que las emisiones asociadas al Proyecto no presentan alguno de
los efectos, características o circunstancias del artículo 11 de la Ley N°19.300.

Por lo tanto, con todo lo expuesto es posible señalar que el Proyecto no genera un riesgo a la
salud de la población.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

58

ENERGETICA SOLAR MEMBRILLO

**6** **CONCLUSIONES**

Respecto de la modelación de dispersión de contaminantes se puede señalar que, de
acuerdo con los resultados obtenidos, los aportes de material particulado sedimentable
(MPS), material particulado fracción respirable (MP 10 y MP 2,5 ) y gases (NO 2, SO 2 y CO) en
los receptores considerados, se encuentran bajo los umbrales establecidos en las normas
de calidad del aire primarias y secundarias.

Es importante indicar que las mayores emisiones del Proyecto se presentan en el año 1
compuesto por fase de construcción y 6 meses de operación las cuales están asociadas a
la resuspensión de polvo por tránsito vehicular por camino no pavimentado y movimiento
de tierra en las fases de construcción y cierre y que la extensión de dichas emisiones se
limita al área circundante del proyecto, tal como se expone en los mapas de
isoconcentraciones de la Sección 2.11 del presente documento.

Por lo tanto, es posible concluir que las emisiones asociadas al Proyecto no presentan
alguno de los efectos, características o circunstancias del artículo 11 de la Ley N°19.300.

Anexo N° 2 Modelación de Emisiones Atmosféricas

Adenda DIA Proyecto Energética Solar Membrillo

59

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1.: ** **Registro de velocidad del viento Estación****

| Período | Velocidad del viento, m/s |
| --- | --- |
| 2021 | 0,5 |
| 2022 | 0,5 |
| 2023 | 0,47 |

**Tabla 2-2.: ** **Coordenadas de ubicación referencial de estación****

| Nombre de la estación | Coordenada UTM WGS 84 H 19s (m) | Col3 |
| --- | --- | --- |
| San Pedro de Melipilla | 273.194 | 6.246.438 |

**Tabla 2-3.: ** **Métricas estadísticas recomendables en el análisis de incertidumbre para las****

| Estadístico | Velocidad del viento, m/s- (10 m) | Temperatura, °C (2 metros) |
| --- | --- | --- |
| **BIAS** | [-2,5;2,5] (m/s) | [-4;4] (°C) |
| **MAE** | <= 3 (m/s) | <=4 (°C) |
| **RMSE** | <= 3,5 (m/s) | <=4,5(°C) |
| **r ** | >0,6 | >0,8 |

**Tabla 2-4.: ** **Métricas estadísticas calculadas****

| Estadístico | Velocidad del viento, m/s | Temperatura, °C |
| --- | --- | --- |
| **BIAS** | 2,07 | 2,16 |
| **MAE** | 2,08 | 2,68 |
| **RMSE** | 2,45 | 3,47 |
| **r ** | 0,67 | 0,91 |

**Tabla 2-5.: ** **Receptores humanos y coordenadas de ubicación referencial****

| Receptor | Coordenadas UTM WGS 84 H 19s | Col3 |
| --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** |
| R01 | 288.625 | 6.235.514 |
| R02 | 288.788 | 6.235.549 |
| R03 | 289.147 | 6.235.530 |
| R04 | 289.324 | 6.235.404 |
| R05 | 289.548 | 6.235.588 |
| R06 | 288.887 | 6.234.962 |
| R07 | 288.485 | 6.235.269 |
| R08 | 288.446 | 6.235.404 |

**Tabla 2-6.: ** **Receptores Fauna y coordenadas de ubicación referencial****

| Receptor | Coordenadas UTM WGS 84 H 19s | Col3 |
| --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** |
| F1 | 288.995 | 6.235.228 |
| F2 | 289.354 | 6.235.575 |

**Tabla 2-7.: ** **Normativa primaria y secundaria de calidad del aire utilizada****

| Parámetro | Estadístico | Valor Normado | Normativa |
| --- | --- | --- | --- |
| MP10 | Anual | 50 μg/m3 | D.S. N° 12/2022 MMA |
| MP10 | Percentil 98 24 horas | 130 μg/m3 | 130 μg/m3 |
| MP2,5 | Anual | 20 μg/m3 | D.S. N° 12/2010 MMA |
| MP2,5 | Percentil 98 24 horas | 50 μg/m3 | 50 μg/m3 |
| NO2 | Anual | 40 μg/m3 | D.S. N° 40/2024 MMA |
| NO2 | Percentil 99 1 hora | 200 μg/m3 | 200 μg/m3 |
| NO2 | Percentil 98 24 horas | 100 μg/m3 | 100 μg/m3 |
| CO | Percentil 99 8 horas | 10.000 μg/m3 | D.S. N°115/02 MINSEGPRES |
| CO | Percentil 99 1 hora | 30.000 μg/m3 | 30.000 μg/m3 |
| SO2 | Percentil 98,5 1 hora | 350 μg/m3 | D.S. N°104/18 MMA |
| SO2 | Anual | 60 μg/m3 | 60 μg/m3 |
| SO2 | Percentil 99 24 horas | 150 μg/m3 | 150 μg/m3 |
| SO2 (secundario) | Anual | 80 μg/m3 | D.S. N°22/2010 MINSEGPRES |
| SO2 (secundario) | Percentil 99,7 24 horas | 365 μg/m3 | 365 μg/m3 |
| SO2 (secundario) | Percentil 99,73 1 hora | 1000 μg/m3 | 1000 μg/m3 |
| MPS* | Anual | 200 mg/m2_dia | Norma de Confederación Suiza |

**Tabla 2-8.: ** **Resumen de emisiones atmosféricas por año cronológico del proyecto.****

| FASE DE CONSTRUCCIÓN + OPERACIÓN (6 MESES) | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **EMISIONES (t/fase)** | **EMISIONES (t/fase)** | **EMISIONES (t/fase)** | **EMISIONES (t/fase)** | **EMISIONES (t/fase)** | **EMISIONES (t/fase)** |
| **ACTIVIDAD** | **MP**2,5 | **MP**10 | **MPS** | **NOx** | **SOx** | **CO** |
| Excavación | 0,0144 | 0,0278 | 0,1371 |  |  |  |
| Nivelación | 0,0348 | 0,3288 | 1,1234 |  |  |  |
| Compactación | 0,0128 | 0,0247 | 0,1217 |  |  |  |
| Transferencia de material | 0,0014 | 0,0090 | 0,0189 |  |  |  |
| Tránsito de vehículos por caminos pavimentados | 0,0650 | 0,2689 | 1,4007 |  |  |  |
| Tránsito de vehículos por caminos no pavimentados | 0,0486 | 0,4859 | 1,7007 |  |  |  |
| Combustión interna de motores de vehículos por caminos pavimentados | 0,0020 | 0,0020 | 0,0020 | 0,1723 | 0,0005 | 0,0090 |
| Combustión interna de motores de vehículos por caminos no pavimentados | 0,0000 | 0,0000 | 0,0000 | 0,0014 | 0,0000 | 0,0001 |
| Combustión de motores de maquinarias | 0,1247 | 0,1247 | 0,1247 | 2,2788 | 0,0028 | 0,8071 |
| Grupo electrógeno | 0,0407 | 0,0407 | 0,0407 | 0,5778 | 0,0380 | 0,1244 |
| **TOTAL** | **0,3445** | **1,3126** | **4,6699** | **3,0302** | **0,0414** | **0,9406** |

**Tabla 2-9.: ** **Tasas de emisión de fase de construcción del Proyecto****

| Tipo | ID | Descripción | Valor<br>(m2, m) | Tiempo, seg | MP2,5 | MP10 | MPS | NO2 | SO2 | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AREA_POLY | SRC_1 | Movimiento de<br>Tierra | 158.135 | 1728000 | 2,32016E-07 | 1,4283E-06 | 5,1274E-06 | - | - | - |
| ROAD | SRC_2 | Camino<br>pavimentado | 30000 | 5184000 | 4,31321E-07 | 1,7419E-06 | 9,0195E-06 | 1,1077E-06 | 3,3128E-09 | 5,8026E-08 |
| LINE_AREA | SRC_3 | Camino no<br>pavimentado | 9200 | 5184000 | 1,01931E-06 | 1,0189E-05 | 3,5659E-05 | 2,8742E-08 | 8,3127E-11 | 1,4196E-09 |
| AREA_POLY | SRC_4 | Maquinaria | 158.135 | 5184000 | 1,52163E-07 | 1,5216E-07 | 1,5216E-07 | 2,7798E-06 | 3,4722E-09 | 9,8458E-07 |
| POINT | SRC_5 | GE01 | - | 9504000 | 0,00143 | 0,00143 | 0,00143 | 0,02027 | 0,00133 | 0,00436 |
| POINT | SRC_6 | GE02 | GE02 | GE02 | 0,00143 | 0,00143 | 0,00143 | 0,02027 | 0,00133 | 0,00436 |
| POINT | SRC_7 | GE03 | GE03 | GE03 | 0,00143 | 0,00143 | 0,00143 | 0,02027 | 0,00133 | 0,00436 |

**Tabla 2-10.: ** **Resultados punto de mayor concentración y depositación Año 1****

| Parámetro | Estadístico | Unidad | Valor<br>modelado | Coordenada UTM,<br>WGS 84, Huso 19 | Col6 | Coordenadas LCC | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Unidad** | **Valor**<br>**modelado** | **Este (m) ** | **Norte (m) ** | **X, m** | **Y, m** |
| MP10 | Anual | μg/m3 | 0,82 | 288.995 | 6.235.228 | 1407 | -264,1 |
| MP10 | 24 horas<br>P98 | μg/m3 | 2,36 | 288.995 | 6.235.228 | 1407 | -264,1 |
| MP2,5 | Anual | μg/m3 | 0,2 | 288.995 | 6.235.228 | 1407 | -264,1 |
| MP2,5 | 24 horas<br>P98 | μg/m3 | 0,63 | 288.995 | 6.235.228 | 1407 | -264,1 |
| SO2 | 1 hora<br>Percentil<br>98,5 | μg/m3 | 0,22 | 288.995 | 6.235.228 | 1407 | -264,1 |
| SO2 | Anual | μg/m3 | 0,01 | 288.995 | 6.235.228 | 1407 | -264,1 |
| SO2 | 24 horas<br>Percentil 99 | μg/m3 | 0,05 | 288.995 | 6.235.228 | 1407 | -264,1 |
| SO2 <br>(secundario) | Anual | μg/m3 | 0,01 | 288.995 | 6.235.228 | 1407 | -264,1 |
| SO2 <br>(secundario) | Percentil<br>99,7; 24<br>horas | μg/m3 | 0,06 | 288.788 | 6.235.549 | 1207 | 67.0 |
| SO2 <br>(secundario) | Percentil<br>99,73; 1<br>hora | μg/m3 | 0,34 | 288.995 | 6.235.228 | 1407 | -264,1 |
| CO | 1 hora<br>Percentil 99 | μg/m3 | 9,92 | 288.995 | 6.235.228 | 1407 | -264,1 |
| CO | 8 hora<br>Percentil 99 | μg/m3 | 5,34 | 289.548 | 6.235.588 | 1563 | 38,0 |
| NO2 | 1 hora<br>Percentil 99 | μg/m3 | 28,3 | 288.995 | 6.235.228 | 1407 | -264,1 |
| NO2 | 24 horas<br>Percentil 99 | μg/m3 | 9,35 | 288.995 | 6.235.228 | 1407 | -264,1 |
| NO2 | Anual | μg/m3 | 1,99 | 288.995 | 6.235.228 | 1407 | -264,1 |
| MPS | Anual | mg/m2_dia | 11,2 | 288.995 | 6.235.228 | 1407 | -264,1 |

**Tabla 2-11.: ** **Aporte en receptores humanos - Año 1****

| Receptores | MP10 | Col3 | MP2,5 | Col5 | NO2 | Col7 | Col8 | CO | Col10 | SO2 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **24 horas**<br>**P98** | **Anual** | **24**<br>**horas**<br>**P98** | **Anual** | **1 **<br>**hora**<br>**P99** | **24**<br>**hrs**<br>**P99** | **Anual** | **1 **<br>**hora**<br>**P99** | **8 **<br>**horas**<br>**P99** | **24**<br>**horas**<br>**P99** | **Anual** | **1 hora**<br>**Percentil**<br>**98,5** |
| R_1 | 0,73 | 0,12 | 0,21 | 0,04 | 9,72 | 4,04 | 0,39 | 3,47 | 2,37 | 0,01 | 0,00 | 0,02 |
| R_2 | 1,44 | 0,26 | 0,40 | 0,06 | 16,73 | 6,12 | 0,68 | 5,70 | 3,58 | 0,05 | 0,00 | 0,06 |
| R_3 | 1,40 | 0,24 | 0,56 | 0,08 | 18,63 | 9,01 | 0,90 | 6,50 | 5,34 | 0,02 | 0,00 | 0,07 |
| R_4 | 1,19 | 0,23 | 0,46 | 0,07 | 11,10 | 7,76 | 0,85 | 3,91 | 3,48 | 0,02 | 0,00 | 0,04 |
| R_5 | 0,59 | 0,10 | 0,21 | 0,03 | 4,28 | 3,56 | 0,29 | 1,48 | 1,73 | 0,01 | 0,00 | 0,01 |
| R_6 | 0,95 | 0,14 | 0,28 | 0,04 | 8,80 | 6,23 | 0,48 | 3,17 | 3,15 | 0,02 | 0,00 | 0,04 |
| R_7 | 0,94 | 0,09 | 0,36 | 0,03 | 1,70 | 5,39 | 0,30 | 0,59 | 3,64 | 0,01 | 0,00 | 0,00 |
| R_8 | 0,56 | 0,07 | 0,16 | 0,02 | 1,74 | 2,97 | 0,20 | 0,61 | 1,75 | 0,01 | 0,00 | 0,00 |
| Normativa,<br>μg/m3 | 130 | 50 | 50 | 20 | 200 | 100 | 40 | 30000 | 10000 | 150 | 60 | 350 |

**Tabla 2-12: ** **Relación porcentual del aporte respecto a normativa en receptores humanos****

| Receptores | MP10 | Col3 | MP2,5 | Col5 | NO2 | Col7 | Col8 | CO | Col10 | SO2 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **24 horas**<br>**P98** | **Anual** | **24**<br>**horas**<br>**P98** | **Anual** | **1 **<br>**hora**<br>**P99** | **24**<br>**hrs**<br>**P99** | **Anual** | **1 **<br>**hora**<br>**P99** | **8 **<br>**horas**<br>**P99** | **24**<br>**horas**<br>**P99** | **Anual** | **1 hora**<br>**Percentil**<br>**98,5** |
| R_1 | 0,56% | 0,24% | 0,43% | 0,18% | 4,86% | 4,04% | 0,98% | 0,01% | 0,02% | 0,01% | 0,00% | 0,01% |
| R_2 | 1,11% | 0,52% | 0,79% | 0,32% | 8,37% | 6,12% | 1,70% | 0,02% | 0,04% | 0,03% | 0,01% | 0,02% |
| R_3 | 1,08% | 0,49% | 1,11% | 0,38% | 9,31% | 9,01% | 2,24% | 0,02% | 0,05% | 0,02% | 0,00% | 0,02% |
| R_4 | 0,92% | 0,46% | 0,91% | 0,37% | 5,55% | 7,76% | 2,12% | 0,01% | 0,03% | 0,01% | 0,00% | 0,01% |
| R_5 | 0,45% | 0,20% | 0,43% | 0,15% | 2,14% | 3,56% | 0,72% | 0,00% | 0,02% | 0,01% | 0,00% | 0,00% |
| R_6 | 0,73% | 0,27% | 0,56% | 0,21% | 4,40% | 6,23% | 1,21% | 0,01% | 0,03% | 0,01% | 0,00% | 0,01% |
| R_7 | 0,72% | 0,17% | 0,72% | 0,13% | 0,85% | 5,39% | 0,76% | 0,00% | 0,04% | 0,01% | 0,00% | 0,00% |
| R_8 | 0,43% | 0,14% | 0,32% | 0,09% | 0,87% | 2,97% | 0,49% | 0,00% | 0,02% | 0,00% | 0,00% | 0,00% |

**Tabla 2-13.: ** **Aporte de MPS y SO** **2** **en receptores discretos Año 1****

| Receptores | SO2, μg/m3 | Col3 | Col4 | MPS, mg/m2 día |
| --- | --- | --- | --- | --- |
| **Receptores** | **1 hr horas P99,73** | **Anual** | **24 hora Percentil 99,7** | **Anual** |
| F01 | 0,34 | 0,01 | 0,05 | 11,20 |
| F02 | 0,104 | 0,001 | 0,014 | 1,301 |
| **Normativa** | **1000** | **80** | **365** | **200** |

**Tabla 2-14.: ** **Relación porcentual del aporte de MPS y SO** **2** **en receptores discretos Año 1****

| Receptores | SO<br>2 | Col3 | Col4 | MPS |
| --- | --- | --- | --- | --- |
| **Receptores** | **1 hr horas P99,73** | **Anual** | **24 hora Percentil 99,7** | **Anual** |
| F01 | 0,03% | 0,02% | 0,01% | 5,60% |
| F02 | 0,01% | 0,00% | 0,00% | 0,65% |

**Tabla 2-15: ** **Comparación de los resultados de la modelación en receptores humanos y valores de****

| Receptores | MP (ug/m3)<br>10 | Col3 | MP (ug/m3)<br>2,5 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptores** | **24 horas P98** | **Anual** | **24 horas P98** | **Anual** |
| R1 | 0,73 | 0,12 | 0,21 | 0,04 |
| R2 | 1,44 | 0,26 | 0,40 | 0,06 |
| R3 | 1,40 | 0,24 | 0,56 | 0,08 |
| R4 | 1,19 | 0,23 | 0,46 | 0,07 |
| R5 | 0,59 | 0,10 | 0,21 | 0,03 |
| R6 | 0,95 | 0,14 | 0,28 | 0,04 |
| R7 | 0,94 | 0,09 | 0,36 | 0,03 |
| R8 | 0,56 | 0,07 | 0,16 | 0,02 |
| **Valor Significancia**<br>**(Tabla-2, 12 meses)** | **5,00** | **1,00** | **1,71** | **0,33** |

**Tabla 5-1: ** **Criterios para evaluación la generación o presencia de los efectos****

| Criterio | Análisis |
| --- | --- |
| a) Superación de valores de concentración y<br>períodos establecidos en normas primarias<br>de calidad ambiental nacional. | De acuerdo a los resultados de máxima<br>concentración obtenidos de la modelación de<br>calidad del Aire, presentados en la Tabla<br>2-10, Tabla 2-11 y Tabla 2-12 el aporte del<br>Proyecto no supera los valores establecidos<br>en las normas primarias de calidad del aire.<br>Se debe tener en consideración que la RM se<br>encuentra saturada por MP10 y MP2,5por lo<br>tano existe un riesgo pre-existente el cual<br>será analizado en la letra c) de esta tabla. |
| b) Superación de valores de concentración y<br>períodos establecidos en normas primarias<br>de calidad ambiental de los Estados que<br>señala el Reglamento del SEIA | Se utilizó norma primaria de calidad de aire<br>Nacional. |
| c) Aumento del riesgo pre-existente | El área que se emplaza el Proyecto está<br>declarada como saturada.<br>De acuerdo a los resultados de máxima<br>concentración obtenidos de la modelación de<br>calidad del Aire, presentados en la Tabla<br>2-10, Tabla 2-11 y Tabla 2-12 y respecto a los<br>umbrales establecidos en las Tabla 1 y Tabla<br>2 del documento “_Criterio de Evaluación en el_<br>_SEIA: Impacto de emisiones en zonas_<br>_saturadas por material particulado respirable_<br>_MP10 y material particulado fino respirable_<br>_MP2,5_” el aporte del Proyecto en todas sus<br>Fases no supera valores establecidos en el<br>año de mayor emisión, por lo tanto,<br>corresponden a valores no significativos para<br>la evaluación de impacto en un escenario de<br>riesgo preexistente, con ello se concluye que<br>las emisiones atmosféricas generadas por el<br>Proyecto, no afectan a la salud de la<br>población.. . |
| d) Superación de los valores establecidos en<br>las normas de emisión. | Las<br>emisiones<br>del<br>Proyecto<br>son<br>principalmente<br>polvo<br>resuspendido<br>por<br>tránsito vehicular, |
