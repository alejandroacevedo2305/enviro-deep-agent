---
title: Sin título
author: Laptop
date: D:20250425121425-04'00'
language: es
type: report
pages: 63
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - APÉNDICE 6.1.3 CARACTERIZACIÓN METEOROLÓGICA Y ANÁLISIS DE INCERTIDUMBRE
-->

# APÉNDICE 6.1.3 CARACTERIZACIÓN METEOROLÓGICA Y ANÁLISIS DE INCERTIDUMBRE

Mewlen Asesoría

Especialistas en Calidad de Aire

[contacto@mewlenasesoria.cl](mailto:contacto@mewlenasesoria.cl)

Febrero 2025

**ÍNDICE DE CONTENIDOS**

1 Introducción ............................................................................................................................................ 6

2 Objetivos ................................................................................................................................................. 7

2.1 Objetivo Principal .............................................................................................................................. 7

2.2 Objetivos Secundarios ...................................................................................................................... 7

3 Caracterización de Variables Meteorológicas ........................................................................................ 8

3.1 Cantidad de Datos ............................................................................................................................. 8

3.2 Gráficos ciclos diarios .....................................................................................................................14

3.3 Evolución del componente sin la ejecución del Proyecto, y considerando cambio climático .........33

4 Parámetros y Variables De Modelación ...............................................................................................39

4.1 Topografía .......................................................................................................................................39

4.2 Uso de Suelo ...................................................................................................................................40

4.3 Contenido de Agua del Suelo..........................................................................................................41

4.4 Rugosidad Superficial .....................................................................................................................42

4.5 Índice de Área Foliar .......................................................................................................................43

5 Descripción Meteorológica (Observación y Pronóstico) ......................................................................44

5.1 Series de Tiempo ............................................................................................................................46

5.1.1. Temperatura .........................................................................................................................46

5.1.2. Velocidad del Viento .............................................................................................................48

5.1.3. Dirección del Viento ..............................................................................................................50

5.2 Altura De Capa De Mezcla ..............................................................................................................54

5.3 Campos de Viento ...........................................................................................................................55

6. Análisis De Incertidumbre ....................................................................................................................59

6.1. Análisis Cualitativo .......................................................................................................................59

2

6.2. Análisis Cuantitativo .....................................................................................................................60

7. Comentarios .........................................................................................................................................62

8. Conclusiones ........................................................................................................................................63

**ÍNDICE DE TABLAS**

Tabla 3-1:Datos válidos estación meteorológica Aeródromo La Independencia (2023), Rancagua ...........10

Tabla 3-2:Datos válidos estación meteorológica San Francisco de Mostazal (2017) .................................12

Tabla 3-3:Datos válidos estación meteorológica Codegua (2017) ..............................................................14

Tabla 5-1: _Coordenadas de ubicación y variables meteorológicas estación Aeródromo La_

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- el período enero de 2023 a diciembre de 2023, cuyo detalle es posible observar en la **¡Error! No se** **encuentra el origen de la referencia.** . -->

**Tabla 5-1: _Coordenadas de ubicación y variables meteorológicas estación Aeródromo La Independencia._**

| Estación | Coordenadas UTM WGS 84<br>Huso 19 S | Col3 | Variables meteorológicas | Período |
| --- | --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Aeródromo<br>La<br>Independen<br>cia | 336.861 | 6.217.579 | Dirección y Velocidad del Viento<br>y Temperatura | Enero 2023 a<br>diciembre 2023 |

<!-- Estadísticas: 2 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Mewlen, 2024._ La elección del año 2023 para realizar la modelación consideró lo señalado en la “Guía para el uso de -->
<!-- FIN TABLA 5-1 -->

_Independencia._ .............................................................................................................................................44

Tabla 5-2: _Valores promedio de velocidad del viento y temperatura en estación Pudahuel._ ......................44

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- comparación de valores promedio, como se presenta en la **¡Error! No se encuentra el origen de la** **referencia.** -->

**Tabla 5-2: _Valores promedio de velocidad del viento y temperatura en estación Pudahuel._**

| Año | Cantidad de datos | Promedio<br>velocidad del<br>viento [m/s] | Promedio<br>Temperatura [°C] |
| --- | --- | --- | --- |
| 2021 | 8.609 | 2,38 | 14,72 |
| 2022 | 7.927 | 2,39 | 14,88 |
| 2023 | 8.635 | 2,29 | 15,16 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Mewlen, 2024._ 44 -->
<!-- FIN TABLA 5-2 -->


Tabla 5-3 _: Resumen de información altura de capa de mezcla modelada._ .................................................54

Tabla 6-1 _: Métricas estadísticas para la evaluación de la incertidumbre del Modelo de Dispersión._ .........61

**ÍNDICE DE FIGURAS**

Figura 3-1: Serie de tiempo velocidad de viento- datos observados estación Aeródromo La Independencia,

2023. ............................................................................................................................................................... 8

Figura 3-2 _: Serie de tiempo dirección de viento- datos observados estación Aeródromo La Independencia,_

_2023_ ................................................................................................................................................................ 9

Figura 3-3 _: Serie de tiempo temperatura- datos observados estación Aeródromo La Independencia,_

_2023_ ................................................................................................................................................................ 9

Figura 3-4 _: Serie de tiempo velocidad del viento- datos observados estación San Francisco de Mostazal,_

_2017_ ..............................................................................................................................................................10

Figura 3-5 _: Serie de tiempo dirección del viento- datos observados estación San Francisco de Mostazal,_

_2017_ ..............................................................................................................................................................11

Figura 3-6 _: Serie de tiempo temperatura - datos observados estación San Francisco de Mostazal, 2017_ 11

Figura 3-7 _: Serie de tiempo velocidad del viento - datos observados estación Codegua, 2017_ .................12

Figura 3-8 _: Serie de tiempo dirección del viento - datos observados estación Codegua, 2017_ ..................13

Figura 3-9 _: Serie de tiempo temperatura - datos observados estación Codegua, 2017_ .............................13

3

Figura 3-10 _: Ciclo diario velocidad del viento - datos observados estación Aeródromo La Independencia,_

_año 2023_ .......................................................................................................................................................15

Figura 3-11 _: Ciclo diario velocidad del viento - datos observados estación San Francisco de Mostazal, año_

_2017_ ..............................................................................................................................................................16

Figura 3-12 _: Ciclo diario velocidad del viento - datos observados estación Codegua, año 2017_ ...............17

Figura 3-13 _: Ciclo diario dirección del viento - datos observados estación Aeródromo La Independencia,_

_año 2023_ .......................................................................................................................................................18

Figura 3-14 _: Ciclo diario dirección del viento - datos observados estación San Francisco de Mostazal, año_

_2017_ ..............................................................................................................................................................19

Figura 3-15 _: Ciclo diario dirección del viento - datos observados estación Codegua, año 2017_ ................20

Figura 3-16 _: Ciclo diario temperatura - datos observados estación Aeródromo La Independencia, año 2023_

......................................................................................................................................................................21

Figura 3-17 _: Ciclo diario temperatura - datos observados estación San Francisco de Mostazal, año_

_2017_ ..............................................................................................................................................................22

Figura 3-18 _: Ciclo diario temperatura - datos observados estación Codegua, año 2017_ ............................23

Figura 3-19 _: Rosa de vientos anual - datos observados estación Aeródromo La Independencia, año_

_2023_ ..............................................................................................................................................................24

Figura 3-20 _: Rosa de vientos comportamiento diario - datos observados estación Aeródromo La_
_Independencia, año 2023_ .............................................................................................................................25

Figura 3-21 _: Rosa de vientos anual - datos observados estación San Francisco de Mostazal, año 2017_ .26

Figura 3-22 _: Rosa de vientos comportamiento estacional - datos observados estación San Francisco de_

_Mostazal, año 2017_ ......................................................................................................................................27

Figura 3-23 _: Rosa de vientos anual - datos observados estación Codegua, año 2017_ ..............................28

Figura 3-24 _: Rosa de vientos comportamiento estacional - datos observados estación Codegua, año 2017_

......................................................................................................................................................................29

Figura 3-25 _: Ciclo estacional - datos observados estación Aeródromo La Independencia, año 2023_ ........30

Figura 3-26 _: Ciclo estacional - datos observados estación San Francisco de Mostazal, año 2017_ ............31

Figura 3-27 _: Ciclo estacional - datos observados estación Codegua, año 2017_ .........................................32

Figura 3-28 _:_ _Evolución viento medio - comuna de Mostazal_ .......................................................................34

Figura 3-29 _: Evolución temperatura media - comuna de Mostazal_ .............................................................35

Figura 3-30: _Evolución precipitación acumulada - comuna de Mostazal_ .....................................................36

Figura 3-31: _Evolución Presión Atmosférica Media- Comuna de Mostazal_ .................................................37

4

Figura 3-32 _: Evolución Humedad Relativa Media Diaria- Comuna de Mostazal_ .........................................38

Figura 4-1 _: Topografía área de modelación._ ................................................................................................39

Figura 4-2 _: Uso de suelo área de modelación._ ............................................................................................40

Figura 4-3 _: Contenido de agua del suelo área de modelación._ ...................................................................41

Figura 4-4: _Rugosidad superficial área de modelación._ ...............................................................................42

Figura 4-5 _:_ _Índice de área foliar área de modelación._ .................................................................................43

Figura 5-1 _:_ _Comportamiento horario de temperatura (°C) en periodo 2021 al 2023_ ...................................45

Figura 5-2 _: Comportamiento horario de velocidad del viento (m/s) en periodo 2021 a 2023_ ......................46

Figura 5-3 _: Comparación entre ciclos diarios de temperatura observada v/s modelada._ ............................47

Figura 5-4: _Comparación entre series de tiempo de temperatura observada v/s modelada._ ......................48

Figura 5-5 _: Comparación entre ciclos diarios de velocidad del viento observada v/s modelada._ ...............49

Figura 5-6 _:_ _Comparación entre series de tiempo de velocidad del viento observada v/s modelada._ .........50

Figura 5-7: _Comparación entre ciclos diarios de dirección del viento observada v/s modelada._ ................51

Figura 5-8 _: Comparación entre series de tiempo de velocidad del viento observada v/s modelada._ .........51

Figura 5-9 _: Comparación entre rosas de viento observada v/s modelada._ .................................................52

Figura 5-10 _: Comparación entre ciclos estacionales de dirección y velocidad del viento observada v/s_

_modelada._ .....................................................................................................................................................53

Figura 5-11 _: Campos de viento área de modelación - Verano 12:00 pm._ ..................................................55

Figura 5-12 _: Campos de viento área de modelación - Verano 00:00 am._ ..................................................56

Figura 5-13 _: Campos de viento área de modelación - Invierno 12:00 pm._ .................................................57

Figura 5-14 _:_ _Campos de viento área de modelación - Invierno 00:00 am._ .................................................58

Figura 6-1 _: Comparación entre ciclos diarios de temperatura observada v/s modelada._ ............................59

Figura 6-2 _: Comparación entre ciclos diarios de velocidad del viento observada v/s modelada._ ...............60

5

## 1 I NTRODUCCIÓN

En la actualidad Chilemink utiliza agua para procesar subproductos cárnicos con el propósito de generar

ingredientes, harina y sebo, para la elaboración de alimentos de consumo animal y humano. A partir de

dicho proceso se genera una tasa máxima de efluentes de 150 m3/día para su tratamiento y posterior

descarga al alcantarillado.

Chilemink implemento un Sistema de Tratamiento de RILes, aprobada mediante RCA N° 14/2010, de la

extinta Comisión Regional del Medio Ambiente de la Región del General Libertador Bernardo O’Higgins (en

adelante, Región de O’Higgins), la que califico favorablemente el proyecto “Sistema de Neutralización y

Depuración de Residuos Industriales Líquidos de Criaderos Chilemink Ltda.”, la que fue modificada por el

Proyecto “Aumento de Producción Planta Elaboradora de Ingredientes para Consumo Animal Chilemink”

calificado ambientalmente favorable mediante RCA N°22/2014, del Servicio de Evaluación de Impacto

Ambiental (SEIA) de la región de O’Higgins.

El presente Proyecto contempla una modificación únicamente al Sistema de Tratamiento de RILes, sin

modificación en la tasa de descarga de efluentes, considerando mejoras tecnológicas que permiten el uso

de estas descargas para el riego de un sector aledaño de aproximadamente 3 ha. En esta área de riego se

realizará el cultivo de vegetación para forraje, la cual se busca entregar a precio costo a algún beneficiario

de la zona y que este pueda utilizarlo como alimento de animales. Las mejoras consideradas corresponden
a la implementación de un homogeneizador; un DAF; un Filtro de Membranas y un Estanque de
Acumulación de Efluentes. Adicionalmente, la eliminación del sistema de lombrifiltros (sistema TOHÁ), en

cuenta que se incorpora un sistema de filtrado más eficiente.

Estas regularizaciones requieren ponderar los potenciales efectos ambientales que pudieran generarse en
el entorno del proyecto, siendo de particular interés el referido a las emisiones odorantes.

En el presente informe, se presenta la caracterización de la línea de base de meteorología, utilizando para

ello información proporcionada por la estación de monitoreo C, Rancagua.

Adicionalmente, se desarrolla un análisis de los ciclos diarios y estacionales de las variables meteorológicas

velocidad y dirección de viento, temperatura y altura de capa de mezcla, los cuales permiten describir los
procesos de transporte y dispersión de contaminantes en el área del Proyecto.

Finalmente se realiza el análisis de incertidumbre el cual evidencia el potencial impacto de la modelación

meteorológica sobre las concentraciones estimadas.

6

## 2 O BJETIVOS

**2.1** **O** **BJETIVO** **P** **RINCIPAL**

El presente informe tiene por objetivo realizar un análisis de la meteorología del área donde se encuentra

emplazado el Proyecto.

**2.2** **O** **BJETIVOS** **S** **ECUNDARIOS**

a) Desarrollar una caracterización meteorológica del área de localización del Proyecto en función de

las variables que intervienen primariamente en el proceso de transporte y dispersión de

contaminantes.

b) Analizar el comportamiento de las variables meteorológicas de interés que permitan interpretar si

los resultados de la modelación de emisiones odorantes, evaluando datos obtenidos en la estación

meteorológica Aeródromo La Independencia versus el modelo meteorológico WRF.

7

## 3 C ARACTERIZACIÓN DE V ARIABLES M ETEOROLÓGICAS

Para efectos de la caracterización meteorológica del Área de Influencia (AI), se utilizará la información
registrada por estaciones locales cercanas a la ubicación de la Planta Chilemink. Las más próximas

corresponden a las estaciones San Francisco de Mostazal y Codegua cuyos datos de años completo

corresponden al 2017, extraídos de la plataforma SINCA (Sistema de Información Nacional de Calidad del

Aire), las cuales se ubican linealmente entre los 2,2 km y 7,9 km respectivamente en relación con el

Proyecto. De forma complementaría y con la finalidad de representar datos más actuales, se utilizó los
registros del año 2023 de la estación Aeródromo La Independencia, ubicada aproximadamente a 23 km

lineales en relación con el Proyecto, extraídos de la plataforma de agrometeorología (Red

Agrometeorología INIA). Se hace presente que, las condiciones meteorológicas que intervienen en los

procesos de transporte y dispersión de contaminantes en general siguen un patrón climatológico recurrente
en ciclo anual de tal manera que es posible establecer una descripción cualitativa del AI a partir de la

información de un año precedente.

**3.1** **C** **ANTIDAD DE** **D** **ATOS**

Para realizar el análisis meteorológico y el análisis de incertidumbre es necesario verificar la cantidad de
datos presentes en las mediciones ambientales de las estaciones. A continuación, se muestran los datos
de las estaciones en la serie de tiempo para comprobar que no existen periodos extensos sin datos
durante el año de análisis.

Estación Aeródromo La Independencia

_Figura 3-1_ : _Serie de tiempo velocidad de viento- datos observados estación Aeródromo La Independencia,_

_2023._

_Fuente: Mewlen, 2024._

Figura 3-2 _: Serie de tiempo dirección de viento- datos observados estación Aeródromo La Independencia, 2023_

_Fuente: Mewlen, 2024._

Figura 3-3 _: Serie de tiempo temperatura- datos observados estación Aeródromo La Independencia, 2023_

_Fuente: Mewlen, 2024._

9

_Tabla 3-1:Datos válidos estación meteorológica Aeródromo La Independencia (2023), Rancagua_

|Porcentaje de datos meteorológicos disponibles- EM Aeródromo La Independencia, Rancagua|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Parámetro**<br>**/mes**|**E **|**F **|**M **|**A **|**M **|**J **|**J **|**A **|**S **|**O **|**N **|**D **|
|Velocidad<br>viento|100|100|100|100|100|97,8|93,6|92|100|100|100|100|
|Dirección<br>viento|100|100|100|100|100|97,8|93,6|92|100|100|100|100|
|Temperatu<br>ra|100|100|100|100|100|97,8|93,6|92|100|100|100|100|

_Fuente: Mewlen, 2023._

Estación San Francisco de Mostazal

Figura 3-4 _: Serie de tiempo velocidad del viento- datos observados estación San Francisco de Mostazal,_

_2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

10

Figura 3-5 _: Serie de tiempo dirección del viento- datos observados estación San Francisco de Mostazal,_

_2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

Figura 3-6 _: Serie de tiempo temperatura - datos observados estación San Francisco de Mostazal, 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

11

_Tabla 3-2:Datos válidos estación meteorológica San Francisco de Mostazal (2017)_

|Porcentaje de datos meteorológicos disponibles- EM San Francisco de Mostazal|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Parámetro**<br>**/mes**|**E **|**F **|**M **|**A **|**M **|**J **|**J **|**A **|**S **|**O **|**N **|**D **|
|Velocidad<br>viento|100|100|100|100|99|100|100|100|100|100|100|100|
|Dirección<br>viento|100|100|100|100|99|100|100|100|100|100|100|100|
|Temperatu<br>ra|100|100|100|100|99|100|100|100|100|100|100|100|

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

Estación Codegua

Figura 3-7 _: Serie de tiempo velocidad del viento - datos observados estación Codegua, 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

12

Figura 3-8 _: Serie de tiempo dirección del viento - datos observados estación Codegua, 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

Figura 3-9 _: Serie de tiempo temperatura - datos observados estación Codegua, 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

13

_Tabla 3-3:Datos válidos estación meteorológica Codegua (2017)_

|Porcentaje de datos meteorológicos disponibles- EM Codegua|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Parámetro**<br>**/mes**|**E **|**F **|**M **|**A **|**M **|**J **|**J **|**A **|**S **|**O **|**N **|**D **|
|Velocidad<br>viento|100|100|100|100|99|100|100|100|100|100|100|63|
|Dirección<br>viento|100|100|100|100|99|100|100|100|100|100|99|63|
|Temperatu<br>ra|100|100|100|100|99|100|100|100|100|100|99|63|

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

A partir de las gráficas de serie de tiempo de los parámetros velocidad del viento, dirección del viento y

temperatura de la estación meteorológica Aeródromo La Independencia, Rancagua se evidencia que los

periodos con falta de información son acotados por lo que la representación de información es la necesaria

para el análisis.

**3.2** **G** **RÁFICOS CICLOS DIARIOS**

En los siguientes gráficos se presenta los ciclos diarios promedio de velocidad del viento, dirección del

viento y temperatura; junto con su variabilidad entre el percentil 5% a 95% (Rango 90% observado).

**Velocidad del viento**

**Estación Aeródromo La Independencia**

La Figura 3-10 muestra el ciclo diario de velocidad del viento en la Estación Aeródromo La Independencia

durante el año 2023. La gráfica muestra que la velocidad del viento es más bien baja durante las primeras

horas de la madrugada con valores cercanos a 2 m/s entre las 0:00 y las 8:00 horas. A partir de la mañana

la velocidad del viento comienza a aumentar gradualmente, alcanzando su punto máximo en el periodo de

la tarde, entre las 13:00 y las 17:00 horas, con velocidades aproximadas a 4 m/s. posteriormente, la

velocidad disminuye progresivamente hacia la noche, descendiendo nuevamente a sus niveles mas bajos

alrededor de las 23:00.

El área sombreada del gráfico representa el rango del 90% de las observaciones, destacando que la

variabilidad es más pronunciada durante las horas de la tarde y menor durante la madrugada y la noche.

14

Figura 3-10 _: Ciclo diario velocidad del viento - datos observados estación Aeródromo La Independencia, año 2023_

_Fuente: Mewlen, 2024._

**Estación San Francisco de Mostazal**

La Figura 3-11 muestra el ciclo diario de velocidad del viento en la Estación San Francisco de Mostazal

durante el año 2017. La gráfica muestra que la velocidad del viento es más bien baja durante las primeras

horas de la madrugada con valores cercanos a 1 m/s entre las 0:00 y las 8:00 horas. A partir de la mañana
la velocidad del viento comienza a aumentar gradualmente, alcanzando su punto máximo en el periodo de

la tarde, entre las 15:00 y las 18:00 horas, con velocidades aproximadas a 2,4 m/s. posteriormente, la

velocidad disminuye progresivamente hacia la noche, descendiendo nuevamente a sus niveles más bajos

alrededor de las 23:00.

El área sombreada del gráfico representa el rango del 90% de las observaciones, destacando que la
variabilidad es más pronunciada durante las horas de la tarde y menor durante la madrugada y la noche.

15

Figura 3-11 _: Ciclo diario velocidad del viento - datos observados estación San Francisco de Mostazal, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

**Estación Codegua**

La Figura 3-12 muestra el ciclo diario de velocidad del viento en la Estación San Francisco de Mostazal

durante el año 2017. La gráfica muestra que la velocidad del viento es más bien baja durante las primeras

horas de la madrugada con valores cercanos a 1 m/s entre las 0:00 y las 10:00 horas. A partir de la mañana

la velocidad del viento comienza a aumentar gradualmente, alcanzando su punto máximo en el periodo de

la tarde, entre las 13:00 y las 18:00 horas, con velocidades aproximadas a 2 m/s. posteriormente, la

velocidad disminuye progresivamente hacia la noche, descendiendo nuevamente a sus niveles más bajos

alrededor de las 23:00.

El área sombreada del gráfico representa el rango del 90% de las observaciones, destacando que la

variabilidad es más pronunciada durante las horas de la tarde y menor durante la madrugada y la noche

16

Figura 3-12 _: Ciclo diario velocidad del viento - datos observados estación Codegua, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

**Dirección del viento**

**Estación Aeródromo La Independencia**

La Figura 3-13 muestra un mapa de calor que representa la frecuencia de las direcciones del viento en

función de la hora local en la estación de estudio para el año 2023. En el eje horizontal se presentan las

horas del día, de 0 a 23, y en el eje vertical se indican las direcciones del viento en grados de 0° a 360°.

Los colores del mapa van desde el celeste al rojo, donde el rojo señala frecuencias más altas y el azul

frecuencias más bajas.

El grafico revela que, a lo largo del día, el viento tiende a provenir principalmente de la dirección entre 100°

y 200° evidenciado por el área en tonos rojos, lo que indica una alta frecuencia de estas direcciones. En

menor medida se evidencia que durante las horas de la mañana (de 4:00 a 8:00) presenta la menor

frecuencia en las direcciones de viento provenientes de 0° a 100°

El comportamiento indica que el viento en la Estación Aeródromo La Independencia tiene patrones

direccionales claros a lo largo del día.

17

Figura 3-13 _: Ciclo diario dirección del viento - datos observados estación Aeródromo La Independencia, año 2023_

_Fuente: Mewlen, 2024._

**Estación San Francisco de Mostazal**

La Figura 3-14 muestra un mapa de calor que representa la frecuencia de las direcciones del viento en

función de la hora local en la estación de estudio para el año 2017. En el eje horizontal se presentan las
horas del día, de 0 a 23, y en el eje vertical se indican las direcciones del viento en grados de 0° a 360°.

Los colores del mapa van desde el celeste al rojo, donde el rojo señala frecuencias más altas y el azul

frecuencias más bajas.

El grafico revela que, a lo largo del día, el viento tiende a provenir principalmente de la dirección entre 180°

y 200° evidenciado por el área verde, amarilla y en tonos rojos, siendo este último el que representa una

alta frecuencia de estas direcciones. En menor medida se evidencia que durante las horas de la mañana

(de 4:00 a 8:00) presenta la menor frecuencia en las direcciones de viento provenientes de 0° a 100°

El comportamiento indica que el viento en la Estación San Francisco de Mostazal tiene patrones

direccionales claros a lo largo del día.

18

Figura 3-14 _: Ciclo diario dirección del viento - datos observados estación San Francisco de Mostazal, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

**Estación Codegua**

La Figura 3-14 muestra un mapa de calor que representa la frecuencia de las direcciones del viento en

función de la hora local en la estación de estudio para el año 2017. En el eje horizontal se presentan las

horas del día, de 0 a 23, y en el eje vertical se indican las direcciones del viento en grados de 0° a 360°.

Los colores del mapa van desde el celeste al rojo, donde el rojo señala frecuencias más altas y el azul
frecuencias más bajas.

El grafico revela que, a lo largo del día, el viento tiende a provenir principalmente de la dirección entre 200°

y 270° evidenciado por el área amarilla, naranja y en tonos rojos, siendo este último el que representa una

alta frecuencia de estas direcciones. En menor medida se evidencia que durante las horas de la mañana

(de 8:00 a 19:00) presenta la menor frecuencia en las direcciones de viento provenientes de 0° a 150°

El comportamiento indica que el viento en la Estación Codegua tiene patrones direccionales claros a lo

largo del día.

19

Figura 3-15 _: Ciclo diario dirección del viento - datos observados estación Codegua, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

**Temperatura**

**Estación Aeródromo La Independencia**

La Figura 3-16 ilustra el ciclo diario de temperatura. A lo largo del día sigue un patrón bien definido. En las

primeras horas de la madrugada (de 00:00 a 6:00), las temperaturas se mantienen relativamente bajas,

con un promedio cercano a 10°C. Conforme avanza mañana, la temperatura comienza a aumentar

gradualmente, alcanzando su punto máximo de las 14:00 a 16:00 horas, con valores promedio cercanos
a 20°C. Este aumento refleja el calentamiento diurno típico, influenciado por la radiación solar y la

disminución de la humedad relativa.

Después de alcanzar su máximo en la tarde, la temperatura empieza a descender progresivamente. En

las últimas horas de la tarde y primeras horas de la noche (de 17:00 a 21:00 horas), la temperatura se
estabiliza a medida que se pierde el calor acumulado durante el día, volviendo a promedios cercanos a

15°C. Al final del día, cerca de las 22:00 horas, la temperatura se estabiliza nuevamente en rangos más

bajos, cerrando el ciclo diario.

El área sombreada en el gráfico revela la variabilidad de la temperatura a lo largo del día. Es más ancha

durante las horas de la tarde, indicando una mayor dispersión en los valores de temperatura debido a
factores como la radiación solar y las variaciones en la cobertura de nubes. Por la noche y la madrugada,

el área sombreada es más estrecha, lo que sugiere menor variabilidad y condiciones más estables.

20

Figura 3-16 _: Ciclo diario temperatura - datos observados estación Aeródromo La Independencia, año 2023_

_Fuente: Mewlen, 2024._

**Estación San Francisco de Mostazal**

La Figura 3-17 ilustra el ciclo diario de temperatura. A lo largo del día sigue un patrón bien definido. En las

primeras horas de la madrugada (de 00:00 a 6:00), las temperaturas se mantienen relativamente bajas,

con un promedio cercano a 10°C. Conforme avanza mañana, la temperatura comienza a aumentar

gradualmente, alcanzando su punto máximo de las 15:00 a 18:00 horas, con valores promedio cercanos

a 20°C. Este aumento refleja el calentamiento diurno típico, influenciado por la radiación solar y la

disminución de la humedad relativa.

Después de alcanzar su máximo en la tarde, la temperatura empieza a descender progresivamente. En

las últimas horas de la tarde y primeras horas de la noche (de 19:00 a 23:00 horas), la temperatura se

estabiliza a medida que se pierde el calor acumulado durante el día, volviendo a promedios cercanos a

15°C. Al final del día, cerca de las 24:00 horas, la temperatura se estabiliza nuevamente en rangos más

bajos, cerrando el ciclo diario.

El área sombreada en el gráfico revela la variabilidad de la temperatura a lo largo del día. Es más ancha

durante las horas de la tarde, indicando una mayor dispersión en los valores de temperatura debido a

factores como la radiación solar y las variaciones en la cobertura de nubes. Por la noche y la madrugada,

el área sombreada es más estrecha, lo que sugiere menor variabilidad y condiciones más estables.

21

Figura 3-17 _: Ciclo diario temperatura - datos observados estación San Francisco de Mostazal, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

**Estación Codegua**

La Figura 3-18 ilustra el ciclo diario de temperatura. A lo largo del día sigue un patrón bien definido. En las

primeras horas de la madrugada (de 02:00 a 8:00), las temperaturas se mantienen relativamente bajas,

con un promedio cercano a 10°C. Conforme avanza mañana, la temperatura comienza a aumentar
gradualmente, alcanzando su punto máximo entre las 15:00 a 18:00 horas, con valores promedio cercanos

a 27°C. Este aumento refleja el calentamiento diurno típico, influenciado por la radiación solar y la

disminución de la humedad relativa.

Después de alcanzar su máximo en la tarde, la temperatura empieza a descender progresivamente. En

las últimas horas de la tarde y primeras horas de la noche (de 19:00 a 23:00 horas), la temperatura se
estabiliza a medida que se pierde el calor acumulado durante el día, volviendo a promedios cercanos a

15°C. Al final del día, cerca de las 24:00 horas, la temperatura se estabiliza nuevamente en rangos más

bajos, cerrando el ciclo diario.

El área sombreada en el gráfico revela la variabilidad de la temperatura a lo largo del día. Es más ancha

durante las horas de la tarde, indicando una mayor dispersión en los valores de temperatura debido a
factores como la radiación solar y las variaciones en la cobertura de nubes. Por la noche y la madrugada,

el área sombreada es más estrecha, lo que sugiere menor variabilidad y condiciones más estables.

22

Figura 3-18 _: Ciclo diario temperatura - datos observados estación Codegua, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

**Rosa de vientos**

**Estación Aeródromo La Independencia**

La Figura 3-19 presenta un diagrama de rosa de vientos, que muestra la distribución de la velocidad del

viento en relación a las direcciones cardinales. Se observa que el viento más frecuente proviene del Sur,
representando un 30,8% del tiempo, seguido por el Sursureste (21,5%). Las mayores velocidades del

viento, indicadas por los colores rojo y amarillo, se presentan predominantemente en las direcciones Sur

y Sursureste.

23

Figura 3-19 _: Rosa de vientos anual - datos observados estación Aeródromo La Independencia, año 2023_

_Fuente: Mewlen, 2024._

En cuanto al comportamiento diario de la dirección del viento y corroborando que las direcciones del viento

predominantes son desde el Sur y Sursureste, cuyo periodo de mayor velocidad del ciento se presenta

durante la tarde con velocidades máximas de 5,7 m/s.

24

Figura 3-20 _: Rosa de vientos comportamiento diario - datos observados estación Aeródromo La Independencia, año_

_2023_

|Entre 00:00 a las 5:59 hrs.|Entre 6:00 a las 11:59 hrs.|
|---|---|
|<br>Entre 12:00 a las 17:59 hrs.|<br>Entre 18:00 a las 23:59 hrs.|

**Estación San Francisco de Mostazal**

_Fuente: Mewlen, 2024._

La Figura 3-21 presenta un diagrama de rosa de vientos, que muestra la distribución de la velocidad del

viento en relación a las direcciones cardinales. Se observa que el viento más frecuente proviene del Sur,

representando un 40% del tiempo. Las mayores velocidades del viento, indicadas por los colores rojo y

amarillo, se presentan predominantemente en la direccione Sur.

25

Figura 3-21 _: Rosa de vientos anual - datos observados estación San Francisco de Mostazal, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

26

Figura 3-22 _: Rosa de vientos comportamiento estacional - datos observados estación San Francisco de Mostazal,_

_año 2017_

|Otoño|Invierno|
|---|---|
|<br>Primavera|<br>Verano|

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

27

**Estación Codegua**

La Figura 3-23 presenta un diagrama de rosa de vientos, que muestra la distribución de la velocidad del

viento en relación a las direcciones cardinales. Se observa que el viento más frecuente proviene del Sur,

representando un 20% del tiempo, luego Suroeste y Sureste. Las mayores velocidades del viento,

indicadas por el color amarillo, se presentan predominantemente en la direccione Sur.

Figura 3-23 _: Rosa de vientos anual - datos observados estación Codegua, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

28

Figura 3-24 _: Rosa de vientos comportamiento estacional - datos observados estación Codegua, año 2017_

|Otoño|Invierno|
|---|---|
|<br>Primavera|<br>Verano|

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

29

**Gráficos Ciclo Estacional**

**Estación Aeródromo La Independencia**

En la Figura 3-25 se observa la variación estacional de los ciclos de velocidad y dirección del viento. En

relación a la dirección del viento en los meses de primavera y verano, se mantiene el ciclo diario con
vientos desde el sur durante todo el día. Durante los meses de mayo a agosto los vientos varían entre el

sur, sursureste y norte debido a los periodos de inestabilidad. Lo anterior indica que la dispersión de

contaminantes se dirige hacia el norte.

Respecto a la velocidad del viento, durante las horas del día en primavera y verano ocurren las mayores
velocidades, siendo las máximas de 5,2 m/s promedio, mientras que en la noche descienden a menos de

1 m/s.

Figura 3-25 _: Ciclo estacional - datos observados estación Aeródromo La Independencia, año 2023_

_Fuente: Mewlen, 2024._

30

**Estación San Francisco de Mostazal**

En la Figura 3-26 se observa la variación estacional de los ciclos de velocidad y dirección del viento. En

relación a la dirección del viento en los meses de primavera y verano, se mantiene el ciclo diario con

vientos desde el sur durante todo el día. Durante los meses de mayo a agosto los vientos varían entre el

sur, suroeste debido a los periodos de inestabilidad. Lo anterior indica que la dispersión de contaminantes

se dirige hacia el norte.

Respecto a la velocidad del viento, durante las horas del día en primavera y verano ocurren las mayores

velocidades, siendo las máximas de 4 m/s promedio, mientras que en la noche descienden a menos de 1

m/s.

Figura 3-26 _: Ciclo estacional - datos observados estación San Francisco de Mostazal, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

31

**Estación Codegua**

En la Figura 3-27 se observa la variación estacional de los ciclos de velocidad y dirección del viento. En

relación a la dirección del viento en los meses de primavera y verano, se mantiene el ciclo diario con

vientos desde el sur durante todo el día. Durante los meses de mayo a agosto los vientos varían entre el

sur, suroeste debido a los periodos de inestabilidad. Lo anterior indica que la dispersión de contaminantes

se dirige hacia el norte.

Respecto a la velocidad del viento, durante las horas del día en primavera y verano ocurren las mayores

velocidades, siendo las máximas de 2,5 m/s promedio, mientras que en la noche descienden a menos de

1 m/s.

Figura 3-27 _: Ciclo estacional - datos observados estación Codegua, año 2017_

_Fuente: Anexo 2.2 Modelación de Dispersión de Emisiones Atmosféricas Adenda DIA “Mejora de Eficiencia y Aumento de_

_Producción Maquina N°3”_

32

**3.3** **E** **VOLUCIÓN DEL COMPONENTE SIN LA EJECUCIÓN DEL** **P** **ROYECTO** **,** **Y CONSIDERANDO CAMBIO**

**CLIMÁTICO**

En esta sección se presenta a evolución de los parámetros climáticos y meteorológicos analizados en la

línea de base, en el contexto de los efectos del cambio climático. La información se basa en el “Explorador

de Amenazas Climáticas 1 ” del Ministerio del Medio Ambiente, que compara los valores históricos con los

valores proyectados para un escenario de emisiones RCP8.5 para el período 2035-2065.

Este análisis distingue entre escenarios históricos y futuros para los siguientes parámetros en la comuna
de Mostazal:

 - Viento medio

 - Temperatura media

 - Precipitación acumulada

 - Presión atmosférica media

 - Insolación solar diaria

 - Humedad relativa media diaria

A continuación, se desarrolla el análisis para cada una de estas variables:

**Viento medio**

El análisis de los gráficos presentados a continuación compara la velocidad media del viento entre datos

históricos y proyecciones futuras para la comuna de Mostazal. El primer gráfico (izquierda) muestra la

velocidad media del viento a lo largo de un año completo, utilizando una escala de colores que va del azul

(indicando 1 m/s) al rojo (indicando 5 m/s). En este gráfico se observa que, para la situación actual, la

velocidad media del viento en Mostazal es de aproximadamente 3,78 m/s, mientras que la proyección

futura indica un leve descenso a 3,76 m/s.

El segundo gráfico (derecha) representa la variación porcentual proyectada en la velocidad media del

viento, con una escala que va desde una disminución de -2% (en azul) hasta un incremento de +0,5% (en

rojo). Este mapa muestra que la comuna de Mostazal experimentará una disminución porcentual de la

velocidad media del viento del -0,57%.

1 https://arclim.mma.gob.cl/amenazas/

33

Figura 3-28 _: Evolución viento medio - comuna de Mostazal_

_Fuente: https://arclim.mma.gob.cl/amenazas/_

**Temperatura Media**

Los gráficos presentados a continuación comparan la temperatura media anual entre datos históricos y

proyecciones futuras para la comuna de Mostazal. El primer gráfico (izquierda) muestra la temperatura

media anual, con una escala de colores que varía del azul (indicando temperaturas más bajas, alrededor

de 6 °C) al rojo (indicando temperaturas más altas, hasta 16 °C). En este gráfico se observa que la
temperatura media anual actual en Mostazal es de aproximadamente 11,9 °C, mientras que se proyecta

un aumento a 13,3 °C.

El segundo gráfico (derecha) ilustra el cambio proyectado en la temperatura media anual, con una escala

de colores que muestra variaciones desde -1 °C (en azul) hasta +1,8 °C (en rojo). Este mapa indica que la

comuna de Mostazal experimentará un aumento de la temperatura media anual de 1,37 °C.

34

Figura 3-29 _: Evolución temperatura media - comuna de Mostazal_

_Fuente: https://arclim.mma.gob.cl/amenazas/_

**Precipitación Acumulada**

A continuación, se presentan los gráficos de precipitación acumulada que comparan datos históricos y

proyecciones futuras, así como el cambio proyectado en la precipitación para la comuna de Mostazal. El

primer gráfico (izquierda) muestra la precipitación acumulada a lo largo de un año completo, utilizando una
escala de colores que va del morado oscuro (indicando una precipitación mínima de 0 mm) al rojo oscuro

(indicando una precipitación máxima de 2000 mm). En este gráfico, se observa que la precipitación

acumulada actual en Mostazal es de aproximadamente 844,7 mm, mientras que la proyección futura indica

una disminución a 702,0 mm.

El segundo gráfico (derecha) ilustra la variación porcentual proyectada en la precipitación acumulada
anual, con una escala de colores que varía desde -20% (en azul, indicando una disminución) hasta +5%

(en rojo, indicando un aumento). Este mapa revela que se proyecta una disminución porcentual de la

precipitación en la comuna de Mostazal del 16,9%.

35

Figura 3-30: _Evolución precipitación acumulada - comuna de Mostazal_

_Fuente: https://arclim.mma.gob.cl/amenazas/_

**Presión Atmosférica Media**

El análisis de los gráficos de presión atmosférica media presentados a continuación muestran una

comparación entre datos históricos y futuros, así como los cambios proyectados en la presión atmosférica
media en la comuna de Mostazal. El primer gráfico (izquierda), representa la presión atmosférica media

anual, con una escala de colores que varía desde el verde (indicando presiones más bajas de 750 hPa)

hasta el rojo (indicando presiones más altas de 1000 hPa). En este gráfico se observa que, para la situación

actual, la presión atmosférica media en Mostazal es de aproximadamente 861,9 hPa, mientras que la

proyección futura indica un leve aumento a 862 hPa.

El segundo gráfico (derecha), muestra el cambio proyectado en la presión atmosférica media anual,

utilizando una escala de colores que va desde 0,1 hPa (en azul claro) hasta 0,6 hPa (en rojo oscuro). Este

mapa indica que se proyecta un aumento de la presión atmosférica media en la comuna de Mostazal del

0,07 hPa.

36

Figura 3-31: _Evolución Presión Atmosférica Media- Comuna de Mostazal_

_Fuente: https://arclim.mma.gob.cl/amenazas/_

**Humedad Relativa Media Diaria**

A continuación, se presentan los gráficos de humedad relativa media diaria que comparan datos históricos

y proyecciones futuras, y analizan los cambios proyectados en la humedad relativa para la comuna de
Mostazal. El primer gráfico (izquierda) muestra la humedad relativa media diaria, utilizando una escala de

colores que varía del naranja (indicando menores valores, alrededor del 50%) al azul oscuro (indicando

mayores valores, hasta el 75%). En este gráfico se observa que la humedad relativa media diaria actual

en Mostazal es de aproximadamente 61,7%, mientras que se proyecta una disminución 60,9%.

El segundo gráfico (derecha) ilustra el cambio proyectado en la humedad relativa media diaria, con una
escala de colores que oscila entre -2% (en azul, indicando una disminución) y +4% (en rojo, indicando un

aumento). Este mapa indica que la comuna de Mostazal experimentará una disminución del 1,24% en la

humedad relativa media diaria del aire.

37

Figura 3-32 _: Evolución Humedad Relativa Media Diaria- Comuna de Mostazal_

_Fuente: https://arclim.mma.gob.cl/amenazas/_

38

## 4 P ARÁMETROS Y V ARIABLES D E M ODELACIÓN

**4.1** **T** **OPOGRAFÍA**

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1, cuya resolución es
aproximadamente 90 m. El archivo SRTM1 ha sido incorporado al modelo con el objetivo de proporcionar

la altura de los puntos de interés.

Cabe señalar que la planta se encuentra localizada en un uso de suelo industrial en un entorno urbano,

dónde además se verifica una ausencia de topografía compleja.

En la siguiente figura se presenta una imagen de la información utilizada.

Figura 4-1 _: Topografía área de modelación._

_Fuente: Mewlen, 2024._

39

**4.2** **U** **SO DE** **S** **UELO**

La información relacionada con el uso de suelo, de igual manera que la elevación de terreno es utilizada

directamente del modelo WRF, la cual corresponde a información de Global Land Cover Characteristicas

(GLCC) con resolución de 1 km.

La caracterización de uso de suelo para cada celda del dominio de WRF se puede observar en la Figura

3-2.

Figura 4-2 _: Uso de suelo área de modelación._

_Fuente: Mewlen, 2024._

40

**4.3** **C** **ONTENIDO DE** **A** **GUA DEL** **S** **UELO**

Otra de las características de la superficie del dominio de la modelación es conocer el contenido de agua

del suelo, el cual se puede observar en la siguiente figura para el área de modelación:

Figura 4-3 _: Contenido de agua del suelo área de modelación._

_Fuente: Mewlen, 2024._

41

**4.4** **R** **UGOSIDAD** **S** **UPERFICIAL**

La rugosidad del suelo se estima como un espesor o altura, este es un parámetro que influye en el perfil

vertical de la velocidad del viento y por lo tanto en la dispersión. A continuación, la siguiente figura presenta

la rugosidad superficial para el área de modelación.

Figura 4-4: _Rugosidad superficial área de modelación._

_Fuente: Mewlen, 2024._

42

**4.5** **Í** **NDICE DE** **Á** **REA** **F** **OLIAR**

El índice de área foliar varía tanto en tiempo como en espacio. Las variaciones en este índice pueden

deberse a una variedad de factores, entre los que se incluyen cambios generados por el desarrollo del

rodal, el crecimiento de las especies, su genética y su arquitectura, las condiciones climáticas, las

propiedades del suelo, los contaminantes aéreos y gases, y la herbivoría, entre otros (Pokorný et al., 2008;

Jonckheere et al., 2004).

Figura 4-5 _: Índice de área foliar área de modelación._

_Fuente: Mewlen, 2024._

43

## 5 D ESCRIPCIÓN M ETEOROLÓGICA (O BSERVACIÓN Y P RONÓSTICO )

El análisis de las variables de meteorología del entorno del proyecto se basó en la descripción del

comportamiento de las siguientes variables:

 - Velocidad y Dirección del viento

 - Temperatura

Para lo anterior, se utilizaron los registros provenientes de la estación Aeródromo La Independencia, para

el período enero de 2023 a diciembre de 2023, cuyo detalle es posible observar en la **¡Error! No se**

**encuentra el origen de la referencia.** .

Tabla 5-1: _Coordenadas de ubicación y variables meteorológicas estación Aeródromo La Independencia._

|Estación|Coordenadas UTM WGS 84<br>Huso 19 S|Col3|Variables meteorológicas|Período|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Aeródromo<br>La<br>Independen<br>cia|336.861|6.217.579|Dirección y Velocidad del Viento<br>y Temperatura|Enero 2023 a<br>diciembre 2023|

_Fuente: Mewlen, 2024._

La elección del año 2023 para realizar la modelación consideró lo señalado en la “Guía para el uso de

modelos de calidad del aire en el SEIA”, (febrero 2023), en la cual se indica que _“para la elección del año_

_para la simulación se recomienda que se analicen al menos tres años anteriores de datos observados en_

_el dominio de modelación y que se escoja el escenario (año) de peor condición para la dispersión de_

_contaminantes”_ . Por lo anterior se evaluó la condición meteorológica asociada a la velocidad del viento y

temperatura para la estación Aeródromo La Independencia entre los años 2021 y 2023, realizando

comparación de valores promedio, como se presenta en la **¡Error! No se encuentra el origen de la**

**referencia.**

Tabla 5-2: _Valores promedio de velocidad del viento y temperatura en estación Pudahuel._

|Año|Cantidad de datos|Promedio<br>velocidad del<br>viento [m/s]|Promedio<br>Temperatura [°C]|
|---|---|---|---|
|2021|8.609|2,38|14,72|
|2022|7.927|2,39|14,88|
|2023|8.635|2,29|15,16|

_Fuente: Mewlen, 2024._

44

De los valores expuestos en la tabla precedente, no se obtienen comportamientos muy disímiles a la hora

de poder escoger un año sobre el cuál realizar la modelación de la dispersión de contaminantes. Lo anterior

se valida al observar el comportamiento horario de las variables en estudio cómo es posible apreciar en

los siguientes gráficos:

Figura 5-1 _: Comportamiento horario de temperatura (°C) en periodo 2021 al 2023_

_Fuente: Mewlen, 2024._

45

Figura 5-2 _:_ _Comportamiento horario de velocidad del viento (m/s) en periodo 2021 a 2023_

_Fuente: Mewlen, 2024._

Por lo anterior se determinó el utilizar el año 2023 para realizar la modelación de la dispersión de

contaminantes, considerando que los promedios de velocidad del viento y temperatura calculados para los

tres años de análisis son similares, y por tanto tienen la misma proyección respecto de la evaluación del

impacto de olores del Proyecto.

Por otra parte, a partir de la información meteorológica de pronóstico simulada bajo plataforma WRF, se

desagregó información espacial homóloga a la presentada para los registros meteorológicos observados

obtenido de la estación de monitoreo.

La información presentada en las siguientes secciones corresponde a la misma localización de la estación

de monitoreo de superficie de la estación Aeródromo La Independencia, de tal manera que posteriormente
se puedan realizar estimaciones cualitativas y cuantitativas de la certidumbre de la modelación numérica

WRF.

**5.1** **S** **ERIES DE** **T** **IEMPO**

5.1.1. T EMPERATURA

En la Figura 5-3 se observa el ciclo diario de temperatura para la situación observada y modelada por

WRF. Para ambos casos se identifica que las mayores temperaturas se encuentran dentro del ciclo diurno,
entre las 12:00 y 17:00 horas, próxima a los 20 °C.

46

Respecto a la temperatura máxima promedio de los registros observados, se tiene un valor de 22,12 °C a

las 14:00 horas, mientras que la mínima alcana los 8,54 °C a las 05:00 horas, y el promedio de temperatura

es de 15,16 °C.

En cuanto a la temperatura modelada, esta presenta una temperatura máxima promedio de 19,57 °C a las

15:00 horas, una mínima de 9,46 °C a las 06:00 horas, y un promedio de temperatura de 14,17 °C.

Figura 5-3 _: Comparación entre ciclos diarios de temperatura observada v/s modelada._

_Fuente: Mewlen, 2024._

La Figura 5-4 presenta la serie de tiempo para la variable temperatura de los registros observados y

modelados, donde se observa que la modelación logra reproducir correctamente la variabilidad estacional,

no obstante los valores de temperatura modelada son menores que la observada.

47

La temperatura ambiental influye en el desarrollo de la capa de mezcla, por lo tanto al haber una correlación

entre lo observado y lo modelado, se espera que las concentraciones modeladas no se encuentren

subestimadas.

Figura 5-4: _Comparación entre series de tiempo de temperatura observada v/s modelada._

_Fuente: Mewlen, 2024._

5.1.2. V ELOCIDAD DEL V IENTO

Al comparar el ciclo diario observado y de pronóstico ilustrado en la Figura 5-5, se evidencia que el modelo

WRF reproduce correctamente la trayectoria de la curva promedio de velocidad en el perfil diario con una

sobrestimación de la velocidad del viento parte del día. Tal situación, articula un escenario favorable

respecto de las condiciones de ventilación del área de interés, de manera que los valores que representan
el transporte de contaminantes a partir de lo desagregado del modelo de dispersión que utiliza como dato

de entrada la meteorología de pronóstico, podría subestimar el valor de las concentraciones.

48

Los promedios diarios de la velocidad de viento observada varían entre 1 m/s y 3,5 m/s, registrados a las

04:00 y 16:00 horas respectivamente, con un promedio anual de 2,29 m/s, mientras que en la situación

modelada la velocidad de viento promedio varía entre 1 m/s y próximo a 6 m/s, registrados a las 00:00 y

15:00 horas respectivamente, con un promedio anual de 1,43 m/s.

Figura 5-5 _: Comparación entre ciclos diarios de velocidad del viento observada v/s modelada._

_Fuente: Mewlen, 2024._

La Figura 5-6 presenta la serie de tiempo horaria de velocidad del viento para la situación observada y
modelada. Las series de tiempo permiten observar la completitud de la serie la que muestra claramente la
presencia de registros observados para todo el año en la estación Aeródromo La Independencia. Se
muestra en general una correlación entre las estaciones que experimentan mayor amplitud, sin que exista
equivalencia en la magnitud. Las mayores velocidades se presentan durante las temporadas de primavera
y verano, mientras que las menores se registran en invierno, específicamente en el mes de julio.

49

Figura 5-6 _: Comparación entre series de tiempo de velocidad del viento observada v/s modelada._

_Fuente: Mewlen, 2024._

5.1.3. D IRECCIÓN DEL V IENTO

La Figura 5-7 muestra el ciclo diario para la dirección del viento modelada y observada, donde se distinguen
direcciones de vientos similares asociadas a las componentes Sur (S) y Sur-suroeste (SSE). La serie de
datos pronosticados WRF presenta el mismo desarrollo con valores que se ubican en la dirección 200° en
promedio por lo que el comportamiento de la dirección de vientos no presenta sobre o subestimación en el
transporte desde el Proyecto hacia los receptores ubicados al norte del Proyecto.

50

Figura 5-7: _Comparación entre ciclos diarios de dirección del viento observada v/s modelada._

_Fuente: Mewlen, 2024._

La Figura 5-8 presenta la serie de tiempo horaria de velocidad del viento observada y modelada, donde es
posible distinguir que el modelo WRF reproduce las direcciones predominantes, concentrando una mayor
cantidad de registros en las direcciones 200° - 250 °, a diferencia de lo observado, que principalmente se
concentra entre los 150° y 200°.

Figura 5-8 _: Comparación entre series de tiempo de velocidad del viento observada v/s modelada._

51

_Fuente: Mewlen, 2024._

Por otra parte, en la Figura 5-9 se muestra la comparación entre las rosas del viento observada y modelada,
donde es posible sostener que existe una componente sur de los vientos, siento marcada la dirección Sur
y Sur sureste en los datos observados, mientras que en los datos modelados la dirección de vientos es
principalmente desde el Suroeste.

Figura 5-9 _: Comparación entre rosas de viento observada v/s modelada._

|Col1|Col2|
|---|---|
|**Rosa de Viento Observada**|**Rosa de Viento Modelada**|

_Fuente: Mewlen, 2024._

La Figura 5-10 muestra la comparación del ciclo estacional de la dirección y velocidad del viento observada
en la estación Aeródromo La Independencia y modelada por WRF para el año 2023. A partir de esta
comparación, es posible establecer que el modelo logra representar de buena manera los meses del año
y horas del día en que se presentan las mayores y menores intensidades de viento. En ambas gráficas se
aprecian mayores valores de velocidad del viento en el horario diurno entre los meses de septiembre a

52

abril. Por el contrario, se tienen menores velocidades de viento durante el periodo nocturno y de
madrugada, particularmente entre marzo y agosto.

En cuanto a la dirección del viento, el modelo pronostica de buena forma los vientos del periodo diurno con
dirección suroeste observados y los vientos del periodo nocturno con dirección sur observados.

Figura 5-10 _: Comparación entre ciclos estacionales de dirección y velocidad del viento observada v/s modelada._

53

_Fuente: Mewlen, 2024._

**5.2** **A** **LTURA** **D** **E** **C** **APA** **D** **E** **M** **EZCLA**

La altura de capa de mezcla es un parámetro obtenido del procesamiento de los resultados del modelo

meteorológico WRF, y corresponde a la altura medida desde la superficie en la que la inestabilidad

favorece la dispersión vertical de tal manera que puede interpretarse como el volumen de atmósfera
disponible para la dilución de contaminantes atmosféricos. En la Tabla 5-3 se presenta el resumen de

información para la variable meteorológica altura de mezcla.

Cabe señalar que no existen datos de meteorología de altura registrados dentro del dominio de modelación

para la estación Aeródromo La Independencia, razón por la cual no es posible desarrollar una comparación

entre la meteorología observada v/s modelada.

Tabla 5-3 _: Resumen de información altura de capa de mezcla modelada._

54

|Variable|Estadístico|Valor (m)|
|---|---|---|
|Altura de mezcla (m)|Promedio|781|

|Variable|Estadístico|Valor (m)|
|---|---|---|
||Máximo|3.500|
||Mínimo|108|
||Datos válidos (%)|100%|

_Fuente: Mewlen, 2024._

**5.3** **C** **AMPOS DE** **V** **IENTO**

De la Figura 4-11 a la Figura 4-14 se muestra el campo vectorial de vientos a 10 metros de altura modelados

por WRF durante el periodo diurno y nocturno para un día típico de verano e invierno. En estas figuras se

aprecia que durante el verano los campos vectoriales se dirigen hacia el Norte en ambos escenarios, siendo

el de las 00:00 horas levemente menores al de las 12:00 horas en cuanto a intensidad. Para el caso de la

estación de invierno, se puede apreciar en las gráficas que los campos vectoriales son mucho menores a

los reportados en verano, no mostrando además una tendencia clara de dirección del viento.

Figura 5-11 _: Campos de viento área de modelación - Verano 12:00 pm._

_Fuente: Mewlen, 2024._

55

Figura 5-12 _: Campos de viento área de modelación - Verano 00:00 am._

_Fuente: Mewlen, 2024._

56

Figura 5-13 _: Campos de viento área de modelación - Invierno 12:00 pm._

_Fuente: Mewlen, 2024._

57

Figura 5-14 _: Campos de viento área de modelación - Invierno 00:00 am._

_Fuente: Mewlen, 2024._

58

### 6. A NÁLISIS D E I NCERTIDUMBRE

**6.1.** **A** **NÁLISIS** **C** **UALITATIVO**

En relación a los elementos cualitativos que describen las diferencias entre parámetros meteorológicos

observados y pronosticados en Estación Aeródromo La Independencia para el año 2023, es posible indicar

lo siguiente:

- Para la variable temperatura, el modelo de pronóstico logra reproducir correctamente la variabilidad

estacional con tendencia a sobreestimar el registro observado en algunas horas del día, principalmente
en la tarde y en la noche, tal como se observa en el Gráfico 5-1. La temperatura ambiental influye en
el desarrollo de la capa de mezcla, por lo tanto, al haber una correlación entre lo observado y lo
modelado, se espera que las concentraciones modeladas no se encuentren subestimadas.

Figura 6-1 _: Comparación entre ciclos diarios de temperatura observada v/s modelada._

_Fuente: Mewlen, 2024._

- Por otra parte, al comparar el ciclo diario observado y de pronóstico, se evidencia que el modelo WRF

reproduce correctamente la trayectoria de la curva promedio de velocidad en el perfil diario con una
subestimación de la velocidad del viento parte del día, principalmente en las horas del día (09:00 a las
19:00). Tal situación, articula un escenario desfavorable respecto de las condiciones de ventilación del
área de interés, de manera que los valores que representan el transporte de contaminantes a partir de

59

lo desagregado del modelo de dispersión que utiliza como dato de entrada la meteorología de
pronóstico, podría sobrestimar el valor de las concentraciones.

Figura 6-2 _: Comparación entre ciclos diarios de velocidad del viento observada v/s modelada._

_Fuente: Mewlen, 2024._

- El ciclo diario para la dirección del viento distingue direcciones de vientos similares entre valor

observado y valor pronóstico, asociadas a las componentes Sur (S) y Sur-suroeste (SSO). La serie de
datos pronosticados WRF presenta el desarrollo de un componente SE que no se verifica en los vientos
observados por estación Aeródromo La Independencia, siendo un elemento singular de evaluación ya
que la presencia de estos vientos en el modelo de dispersión sobrestimaría el transporte desde la
Planta hacia los receptores ubicados al nor-poniente (NO) de la planta.

**6.2.** **A** **NÁLISIS** **C** **UANTITATIVO**

Considerando la información disponible registrada por estación Aeródromo la Independencia, Rancagua

para año 2023 y la obtenida para una estación virtual proveniente de la matriz de datos meteorológicos de

pronóstico WRF para el mismo año, se ha desarrollado una evaluación basada en la comparación de los

parámetros velocidad del viento y temperatura los cuales permiten establecer un factor de incertidumbre

de la capacidad predictiva del modelo de dispersión. El análisis considera la evaluación sobre los
estadígrafos: Error Medio (BIAS), Error Absoluto Medio (MAE); Error Cuadrático Medio (RMSE) y

Coeficiente de correlación (r), cuyas fórmulas de cálculo y resultados se presentan a continuación

60

n

BIAS= [1]

n [∑(S] [i] [−O] [i] [)]

i=1

n

MAE= [1]

n [∑|S] [i] [−O] [i] [|]

i=1

[1]

n

RMSE= √

n

n [∑(S] [i] [−O] [i] [)] [2]

i=1

Dónde:

_n_ _= Cantidad de datos_

_S_ _= Valores obtenidos del modelo_

_O_ _= Valores observados en estaciones meteorológicas_

Tabla 6-1 _: Métricas estadísticas para la evaluación de la incertidumbre del Modelo de Dispersión._

|Medida de Error|Velocidad del<br>Viento (m/s)|Temperatura<br>(°C)|
|---|---|---|
|BIAS|-0,8|-0,8|
|MAE|-0,8|-0,8|
|RMSE|1,5|2,6|
|r|0,6|1,0|

_Fuente: Mewlen, 2024._

En conformidad con lo valores de tolerancia para análisis sobre la capacidad predictiva del modelo indicado

en la Tabla 2 de la Sección 6.2.2 de la Guía para el Uso de modelos en el SEIA (segunda edición), se hace

presente que todos los estadísticos se ajustan a los umbrales de tolerancia de error.

61

### 7. C OMENTARIOS

De lo presentado para la caracterización meteorológica es posible señalar lo siguiente:

 - Se realiza el análisis comparativo entre las variables velocidad y dirección del viento y

temperatura registradas en la estación de monitoreo Aeródromo La Independencia en el año
2023, versus las variables generadas mediante el modelo meteorológico WRF en la misma

ubicación.

 - La temperatura de los registros observados y modelados, presentan un buen ajuste en cuanto

al comportamiento diario y serie de tiempo, no obstante, los valores modelados subestiman

levemente el valor de la temperatura. Cabe señalar que las temperaturas promedio para los
registros observados y modelados son 14,16 °C y 15,16°C respectivamente, lo que no

representa una desviación muy significativa.

 - Respecto a la velocidad del viento, los registros de la estación Aeródromo La Independencia

varían entre 1,25 m/s y 3,75 m/s, con un promedio anual de 2,28 m/s, mientras que en la

situación modelada la velocidad de viento promedio varía entre 0,92 m/s y 2,28 m/s, con un

promedio anual de 1,43 m/s.

 - En cuanto a la dirección del viento, se desprende que la componente predominante en la rosa

de vientos asociada a los datos observados corresponde a los provenientes desde el Sur (S)

y en menor proporción los vientos provenientes desde el Sursureste (SSE). En tanto la rosa

de vientos de los registros modelados (WRF) presenta vientos que predominan desde el

Suroeste (SO) y en menor proporción los vientos provenientes del Sursuroeste(SSO).

 - Respecto a la altura de capa de mezcla, no se cuenta con datos meteorológicos dentro del

dominio de modelación para la estación Aeródromo La Independencia, por lo tanto, no se

pudo realizar una comparación con los valores obtenidos del modelo meteorológico WRF. De
este último, se tiene que el modelo presenta una altura de capa de mezcla promedio de 781

m.

 - Los gráficos de campos de vientos modelados por WRF, se aprecia que durante el verano los

campos vectoriales presentan un dominio hegemónico indistinto si es ciclo diurno y nocturno.

En tanto en el invierno los campos vectoriales son mucho menores a los reportados en verano,

sin marcar una tendencia prevalente de dirección del viento.

 - Finalmente, en relación al análisis cuantitativo datos meteorológicos de pronóstico WRF, se

ha desarrollado una evaluación basada en la comparación de los parámetros velocidad del

viento y temperatura los cuales permiten establecer un factor de incertidumbre de la
capacidad predictiva del modelo de dispersión. En conformidad con lo valores de tolerancia

para análisis sobre la capacidad predictiva del modelo se hace presente que todos los

estadísticos se ajustan a los umbrales de tolerancia de error

62

### 8. C ONCLUSIONES

Para realizar el diagnóstico de las condiciones meteorológicas presentes en el área de localización del

proyecto, se realizó el análisis de los ciclos diarios de variables meteorológicas (temperatura, velocidad
del viento y dirección del viento), también nos entregan información importante para describir los procesos

de transporte y dispersión de contaminantes. Al observar estas gráficas se puede identificar aquellos

periodos del día en que potencialmente pueden desarrollarse las más altas concentraciones de

contaminantes que las masas de aire circulante contengan. Estos subciclos que pueden calificarse como
potencialmente críticos, corresponden a aquellos en que se dan condiciones de viento calmo y mínima

altura de capa de mezclado.

No obstante, considerando las condiciones topográficas del área del proyecto, dado que presenta una

ausencia de cordones montañosos o cerros islas, esto no permite confinamiento de las emisiones por tanto

igualmente existen buenas condiciones de ventilación, más aún en altura, donde se generan las emisiones

de planta.

En general, las desviaciones del modelo de pronóstico meteorológico utilizado como dato de entrada en

el modelo de dispersión son poco significativas dado que los valores obtenidos se encuentran dentro de

tolerancia recomendados para la evaluación. Si bien una subestimación de la velocidad del viento puede
inducir una sobrestimación de los impactos; la presencia de vientos modelados en la dirección SO

proyecta un transporte sobrestimado de los olores en receptores residenciales ubicados viento arriba del

Proyecto, no obstante, los vientos observados presentan un comportamiento de vientos provenientes

desde el Sur y con mayores velocidades que las modeladas. Por lo anterior, es posible señalar que la

modelación de dispersión presenta un escenario desfavorable de predicción confiable sobre las

concentraciones de olor en el área de influencia.

63

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 5-3: _: Resumen de información altura de capa de mezcla modelada._**

| Variable | Estadístico | Valor (m) |
| --- | --- | --- |
|  | Máximo | 3.500 |
|  | Mínimo | 108 |
|  | Datos válidos (%) | 100% |

**Tabla 6-1: _: Métricas estadísticas para la evaluación de la incertidumbre del Modelo de Dispersión._**

| Medida de Error | Velocidad del<br>Viento (m/s) | Temperatura<br>(°C) |
| --- | --- | --- |
| BIAS | -0,8 | -0,8 |
| MAE | -0,8 | -0,8 |
| RMSE | 1,5 | 2,6 |
| r | 0,6 | 1,0 |
