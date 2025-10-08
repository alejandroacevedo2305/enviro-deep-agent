---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 74
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1 Introducción
  - 2 Meteorología
  - 3 Emisiones
  - 4 Simulación de dispersión
  - 5 Conclusiones
-->

|Col1|Col2|
|---|---|
|<br>||
|<br>|DECLARACIÓN DE IMPACTO<br>AMBIENTAL<br> <br>ADENDA 1<br> <br>ANEXO 6<br> <br>MODELACIÓN DE DISPERSION DE<br>CONTAMINANTES|
|||
|||

Informe de Modelación de Dispersión

“Lixiviación de Ripios y Recursos Artificiales”

Codelco División Chuquicamata

Preparado por:

Ingenería y Geofísica Limitada.

Junio, 2016

Contenidos

1 Introducción 2

1.1 Modelos de dispersión atmosféricos disponibles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

1.1.1 Modelos Gaussianos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

1.1.2 Modelos Lagrangeanos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

1.1.3 Modelos tipo “puff” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

1.2 Sistema de Modelación WRF - CALPUFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

2 Meteorología 8

2.1 Diagnóstico en base a observaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.2 Comparación de resultados WRF con observaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

2.3 Caracterización de los vientos segun WRF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

3 Emisiones 16

4 Simulación de dispersión 17

4.1 Aportes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

4.1.1 Comparación con la Norma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

4.2 Isolíneas de concentración . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

4.2.1 Escenario de Operación Actual. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

4.2.2 Escenario de Construccion. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

4.2.3 Escenario de Operación Proyectada. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

4.2.4 Escenario de Cierre. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

4.2.5 Escenario de Operación Proyectada - Operación Actual. . . . . . . . . . . . . . . . . . . . 67

4.3 Análisis de Incertidumbre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

5 Conclusiones 72

1 INTRODUCCIÓN

# 1 Introducción

Según el Anexo 1 “Fundamentos de la Contaminación Atmosférica” de la “Guía para el uso de modelos de

calidad del aire en el SEIA” del Servicio de Impacto Ambiental (SEA), los modelos de dispersión atmosférica son

frecuentemente utilizados para estimar concentraciones ambientales de contaminantes producto de la emisión a

la atmósfera desde fuentes fijas, móviles o difusas, bajo condiciones desfavorables.

Los modelos de dispersión de contaminantes en la atmósfera son herramientas útiles para estimar el impacto

sobre el recurso natural aire de un proyecto o actividad, así como el impacto sobre otros recursos naturales

renovables y el riesgo a la salud de la población, producto de las emisiones atmosféricas. Dichas estimaciones son

contrastadas con la línea de base de calidad del aire levantada en el área de influencia con el objeto de evaluar

si dicho impacto constituye o no una alteración significativa del recurso. Asimismo, se utilizan como criterio

los valores de las concentraciones máximas establecidas por las normas de calidad primarias o secundarias,

nacionales o de los Estados que señala el Reglamento del SEIA en su artículo 11, así como información

toxicológica disponible, para determinar la significancia de dicho impacto. De esta manera, los modelos de

dispersión atmosféricos resultan útiles para estimar la magnitud del área de influencia y la distribución de las

concentraciones en ésta, como asimismo para determinar la ubicación óptima de estaciones de monitoreo de

calidad del aire.

## 1.1 Modelos de dispersión atmosféricos disponibles

Los modelos existentes se pueden clasificar como Gaussianos, Eulerianos, Langrangeanos y tipo “puff” cuyos

conceptos se describen a continuación.

### 1.1.1 Modelos Gaussianos

Los modelos Gaussianos describen la distribución tridimensional de una pluma bajo condiciones meteorológ

icas y de emisiones estacionarias. Las concentraciones se estiman en base a una distribución Gaussiana cuyos

parámetros dependen de las condiciones meteorológicas. Aunque existen modelos Gaussianos que tratan de

incluir el efecto del terreno complejo en la distribución espacial de concentraciones, sus conceptos matemáticos

son fundamentalmente iguales a aquellos modelos que no lo hacen.

Modelos existentes: AERMOD

### 1.1.2 Modelos Lagrangeanos

El concepto detrás de un modelo Lagrangeano es seguir matemáticamente el movimiento de una parcela de

aire o de una partícula en la atmósfera. Es decir, si en la posición inicial de una partícula se conoce tanto la

velocidad como la dirección del viento fácilmente se puede calcular a dónde va esa partícula en un intervalo

de tiempo finito dado (integración en el tiempo). Después de esa integración la partícula tiene una posición

nueva en el espacio donde el viento puede ser distinto que en la posición inicial. Ocupando esta información del

viento, nuevamente se puede integrar en el tiempo moviendo la partícula a otra posición y así sucesivamente se

sigue la integración. El camino que se describe a través de esta integración se llama trayectoria. Con el fin de

obtener una estimación de las concentraciones en un modelo de trayectorias se requiere el cálculo de muchas

2

## 1.2 Sistema de Modelación WRF - CALPUFF 1 INTRODUCCIÓN

trayectorias (del orden de un millón para la dispersión de un contaminante desde una fuente). Aparte de los

procesos de transporte por el viento, también se pueden incorporar los procesos turbulentos de la atmósfera. Al

contrario de los modelos Eulerianos, los modelos Lagrangeanos tienen una capacidad muy limitada de incorpo

rar procesos químicos. No hay mucha experiencia en el uso de modelos Langrangeanos en Chile y, además, a

nivel internacional se usan en muy pocos países con fines regulatorios (por ejemplo Alemania). Mientras no se

descarte su uso en el futuro también en Chile con estos fines, no existen antecedentes suficientes para que este

tipo de modelo sea recomendado.

Modelo existente: AUSTAL

### 1.1.3 Modelos tipo “puff”

Los modelos tipo puff son una combinación entre los modelos Gaussianos y los modelos Lagrangeanos en el

sentido que esencialmente calculan la dispersión de una emisión instantánea, llamada “puff”, a lo largo de una

trayectoria. Su aproximación matemática es estimar la dispersión en forma Gaussiana en cada punto de una

trayectoria; es decir, a diferencia de los modelos Langrangeanos que necesitan el cálculo de un gran número

de trayectorias para una fuente, en el caso de los modelos tipo “puff” sólo se requiere una trayectoria por “puff”

lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se simulan las trayectorias y

la dispersión Gaussiana de muchos “puffs”. Además, estos modelos son capaces de simular muchas fuentes y

fuentes de distinto tipo al mismo tiempo.

Modelos existentes: CALPUFF

Fuente: Anexo 1 “Fundamentos de la Contaminación Atmosférica” de la “Guía para el uso de modelos de calidad del aire en el SEIA” del Servicio de Impacto Ambiental (SEA).

## 1.2 Sistema de Modelación WRF - CALPUFF

El modelo utilizado para determinar el efecto que tendrán las emisiones de material particulado y gases

provenientes de la operación del Proyecto, corresponde al sistema de modelación “WRF-CALPUFF” tal como se

recomienda en el Anexo 1 “Fundamentos de la Contaminación Atmosférica” de la “Guía para el uso de modelos

de calidad del aire en el SEIA” del Servicio de Impacto Ambiental (SEA).

En términos simples, WRF es un modelo de pronóstico meteorológico que simula campos de viento y tem

peratura en un dominio de modelación engrillado y tridimensional, WRF también produce campos en dos

dimensiones como altura de mezcla, características de superficie y propiedades de dispersión. Por otra parte

CALPUFF es un modelo que trata las emisiones como “puffs”, que se van desplazando a través de un campo

meteorológico tridimensional. El sistema de modelación CALPUFF incluye dos componentes principales: WRF

y CALPUFF, además de una larga selección de preprocesadores diseñados para incluir en el modelo datos

meteorológicos y geofísicos, con el objetivo de modelar el transporte y dispersión de contaminantes emitidos por

las fuentes emisoras ("puffs"). La salida primaria de este modelo contiene concentraciones y/o flujos de deposición.

A continuación las figuras 1 a la 4 muestran el área de estudio, los receptores en que se evaluarán las

concentraciones y la ubicación de las fuentes de emisión.

3

1.2 Sistema de Modelación WRF - CALPUFF 1 INTRODUCCIÓN

4

1.2 Sistema de Modelación WRF - CALPUFF 1 INTRODUCCIÓN

5

1.2 Sistema de Modelación WRF - CALPUFF 1 INTRODUCCIÓN

6

1.2 Sistema de Modelación WRF - CALPUFF 1 INTRODUCCIÓN

7

2 METEOROLOGÍA

# 2 Meteorología

## 2.1 Diagnóstico en base a observaciones

Tal como se indica en la Guía el fundamento para la modelación de la dispersión de los contaminantes atmos

féricos es la meteorología. En este capítulo se describen las características más importantes de la meteorología

junto con una evaluación de desempeño del modelo WRF.

La zona cuenta con una red de estaciones meteorológicas muy densa. La figura 5 indica las ubicaciones de

aquellas que se han usado en la evaluación.

Figura 5: Ubicación de las estaciones meteorológicas en la zona de interés.

Un rasgo muy importante de la meteorología en la zona son los ciclos diarios. La figura 6 muestra a modo

del ejemplo de la estación Calama norte estos ciclos de la velocidad y la dirección del viento; el panel superior

entrega el ciclo diario promedio (línea azul) y el rango de 90% de los datos (sombra celeste) y en el panel

inferior, se muestran las frecuencias de las direcciones de viento a nivel horario.

8

2.1 Diagnóstico en base a observaciones 2 METEOROLOGÍA

Figura 6: Ciclo diario del viento en estación Calama Norte. El panel superior el ciclo diario promedio (líneaazul)

y el rango de 90% de los datos (sombra celeste). En el panel inferior, se muestran las frecuencias de las

direcciones de viento a nivel horario.

En primer lugar, la figura demuestra de manera muy clara la presencia del ciclo diario en ambas variables.

Durante la noche, la velocidad de viento es baja con valores mínimos de aproximadamente 5 m/s. Durante el

día el viento es más fuerte, generalmente dos a tres veces más intenso que durante la noche. En este caso, se

alcanzan velocidades de aproximadamente 8 m/s. También en términos de la dirección del viento, se observa un

ciclo diario muy marcado. Tal como se describe más adelante, la variabilidad espacial de esta variable es muy

alta. En el caso de la estación Calama Norte, se observa un viento desde el este durante la noche y desde el

sur-oeste durante el día. Considerando Calama como el punto más crítico en términos de impacto, generalmente

no se observa un flujo de aire con un origen directamente de la faenas de CODELCO.

Mientras la figura 6 se usó a modo de ejemplo, las figuras 7 y 8 ponen en contexto los ciclos diarios de

viento de todas las estaciones a través de los campos de viento a las 17:00 y 05:00 hrs, respectivamente. Las

flechas indican hacia donde sopla el viento y los puntos amarillos la ubicación de la estación.

Es evidente la diferencia entre los patrones de viento durante el día y la noche. Los vientos son mucho más

fuertes durante el día y, además no existen direcciones de viento que apuntan a Calama. Generalmente, los

vientos dirección suroeste-oeste durante este periodo. Durante la noche, los vientos son mucho más débiles y el

patrón de viento es más complejo. En este caso sí existen estaciones que muestran direcciones de viento hacia

Calama como por ejemplo Quetena 1 y Pique 2. No obstante, se puede ver muy bien en la figura, que tanto

en Quetena 2 y Calama Norte, las direcciones indican que los flujos no llegan a la ciudad sino son desviadas

9

2.1 Diagnóstico en base a observaciones 2 METEOROLOGÍA

antes por parte de un flujo desde el este.

Figura 7: Patrón de viento día a las 17:00 hrs según las observaciones. Las flechas indican hacia donde sopla

el viento y los puntos amarillos la ubicación de la estación.

10

## 2.2 Comparación de resultados WRF con observaciones 2 METEOROLOGÍA

Figura 8: Patrón de viento día a las 05:00 hrs según las observaciones. Las flechas indican hacia donde sopla

el viento y los puntos amarillos la ubicación de la estación

## 2.2 Comparación de resultados WRF con observaciones

Mientras las figuras 6-8 se basan en la información más objetiva que son las observaciones, no pueden entregar

una información con una cobertura espacial completa. Con fines de lograr esta cobertura, se usan los modelos

numéricos, en este caso el modelo WRF. Con respecto a estos datos, se debe, en primer lugar, compararlos con

los datos observacionales.

Nuevamente, se usa la estación Calama Norte a modo de ejemplo para esta comparación. La figura 9

compara el ciclo diario de la velocidad del viento observado con el de WRF (simulado) para esta estación. Se

puede observar que WRF sobre-estima la velocidad máxima durante el día. No obstante, durante la noche que

representa el periodo más crítico de transporte de contaminantes hacia la ciudad de Calama, el desempeño del

modelo es muy bueno.

La figura 10 compara los ciclos diarios de la dirección del viento observados con los de WRF (simulados)

11

2.2 Comparación de resultados WRF con observaciones 2 METEOROLOGÍA

también para la estación Calama Norte. También en este caso, se puede observar que WRF reproduce muy bien

el ciclo.

Las características indicadas para la estación Calama Norte en términos del desempeño de WRF son muy

representativas para todas las otras estaciones evaluadas.

Figura 9: Ciclo diario de la velocidad del viento en estación Calama Norte. El panel superior se muestra el

ciclo diario observado, en el panel inferior el simulado por WRF. El ciclo diario promedio se indica a través de

la línea azul y el rango de 90% a través de la sombra celeste.

12

## 2.3 Caracterización de los vientos segun WRF 2 METEOROLOGÍA

Figura 10: Ciclo diario de la dirección del viento según las observaciones (panel superior) y WRF (panel

inferior). Se muestran las frecuencias de las direcciones de viento a nivel horario.

## 2.3 Caracterización de los vientos segun WRF

Finalmente, se usan los datos de WRF para indicar los patrones de viento más importante en la zona. Las figuras

11 y 12 muestran los patrones de viento según el modelo WRF a las 05:00 y las 17:00 hrs que se consideran

horas representativas de los patrones durante la noche y el día, respectivamente. Tal como en el caso de las

observaciones, se puede observar también en este caso que los vientos durante el día son más fuertes y muestran

direcciones dominantes desde el oeste y suroeste. A contrario a este patrón, los vientos durante la noche son

más débiles y el patrón es más complejo. Esta complejidad se debe a la presencia de vientos catabáticos que

siguen principalmente los rasgos de la topografía. Es así también que se explican los vientos del este en la

zona dentro de Calama y hacia el sur este, que actúan como un “escudo” para la ciudad en un sentido que

previenen que los flujos desde el norte y, por lo tanto, desde el Distrito Norte (que transportan contaminantes

de esta zona hacia Calama) no entren a la ciudad.

13

2.3 Caracterización de los vientos segun WRF 2 METEOROLOGÍA

Figura 11: Patrón de viento según WRF a las 05:00 hrs. Se observan vientos débiles y las direcciones de viento

en función de la pendiente hacia abajo local.

14

2.3 Caracterización de los vientos segun WRF 2 METEOROLOGÍA

Figura 12: Patrón de viento según WRF a las 17:00 hrs. Los vientos son más fuertes que durante la noche y se

muestran direcciones dominantes desde el oeste y suroeste

15

3 EMISIONES

# 3 Emisiones

A continuación se presenta un resumen de las emisiones asociadas a las distintas actividades del proyecto en

sus fases de Operación Actual, Construcción, Operación (Proyectada) y Cierre.

|Fuentes|Operación Actual [Ton/año]|Col3|
|---|---|---|
|Fuentes|MP10|MP2,5|
|Fase 11|708,221|30,103|
|Fase 11 a CHENMS|131,869|13,187|
|Fase 11 a Botadero 2480|53,938|5,394|
|Fase 11 a Stock 4|91,643|9,164|
|Stock 4 a CHENMS|23,513|2,351|
|Botadero 2480|10,173|1,540|
|Stock 4|8,614|1,304|
|Chancador Primario|1,880|0,932|
|Acopio Gruesos|1,596|14,169|
|Chancador Secundario|0,572|0,572|
|Chancador Terciario|1,259|1,259|
|Acopio Finos|0,181|0,027|
|Ruta 1|2,000|0,300|
|Ruta 2|0,108|0,081|
|Botadero Ripios|2,049|2,049|
|Total|1037,616|82,434|

Tabla 1: Emisiones Escenario Operación Actual

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Ruta 1|2,000|0,300| |Ruta 2|0,108|0,081| |Botadero Ripios|2,049|2,049| |Total|1037,616|82,434| -->

**Tabla 1: Emisiones Escenario Operación Actual**

| Fuentes | Construcción [Ton/año] | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Fuentes | CO | HC | MP10 | MP2,5 | MPS | NO2 |
| Área de Mezcla | 1,2965 | 0,5882 | 6,0043 | 1,0543 | 30,8942 | 5,3679 |
| Camino No Pavimentado Camionetas Extracción A Mezclado | 0,0021 | 0,0006 | 0,3111 | 0,0314 | 1,2651 | 0,0068 |
| Camino CAEX Zona Extracción A Zona Mezcla | 2,0711 | 0,9244 | 26,7552 | 3,9639 | 84,1948 | 8,6932 |
| Etapa C Botadero | 3,2864 | 1,4909 | 9,0938 | 5,0756 | 39,2914 | 13,6062 |
| Ruta Camionetas Etapa C Botadero | 0,0069 | 0,0019 | 1,2384 | 0,1248 | 4,8166 | 0,0221 |
| Total | 6,6631 | 3,0059 | 43,4029 | 10,2500 | 160,4621 | 27,6961 |

<!-- Estadísticas: 7 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 2: Emisiones Escenario de Construcción 16 -->
<!-- FIN TABLA 1 -->


|Fuentes|Construcción [Ton/año]|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Fuentes|CO|HC|MP10|MP2,5|MPS|NO2|
|Área de Mezcla|1,2965|0,5882|6,0043|1,0543|30,8942|5,3679|
|Camino No Pavimentado Camionetas Extracción A Mezclado|0,0021|0,0006|0,3111|0,0314|1,2651|0,0068|
|Camino CAEX Zona Extracción A Zona Mezcla|2,0711|0,9244|26,7552|3,9639|84,1948|8,6932|
|Etapa C Botadero|3,2864|1,4909|9,0938|5,0756|39,2914|13,6062|
|Ruta Camionetas Etapa C Botadero|0,0069|0,0019|1,2384|0,1248|4,8166|0,0221|
|Total|6,6631|3,0059|43,4029|10,2500|160,4621|27,6961|

Tabla 2: Emisiones Escenario de Construcción

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Camino CAEX Zona Extracción A Zona Mezcla|2,0711|0,9244|26,7552|3,9639|84,1948|8,6932| |Etapa C Botadero|3,2864|1,4909|9,0938|5,0756|39,2914|13,6062| |Ruta Camionetas Etapa C Botadero|0,0069|0,0019|1,2384|0,1248|4,8166|0,0221| |Total|6,6631|3,0059|43,4029|10,2500|160,4621|27,6961| -->

**Tabla 2: Emisiones Escenario de Construcción**

| Fuentes | Operación [Ton/año] | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Fuentes | CO | HC | MP10 | MP2,5 | MPS | NO2 |
| Área Extracción de Ripios | 0,0000 | 0,0000 | 7,0741 | 1,0712 | 14,9566 | 0,0000 |
| Camino CAEX Zona Extracción A Zona Mezcla | 1,6585 | 0,5531 | 202,6826 | 20,5914 | 823,6919 | 8,4210 |
| Camino No Pavimentado Camionetas Extracción A Mezclado | 0,0103 | 0,0028 | 1,5048 | 0,1519 | 6,1188 | 0,0329 |
| Área de Mezcla | 37,9877 | 17,0945 | 28,0770 | 16,0713 | 43,8420 | 181,8346 |
| Camino No Pavimentado Camión Zona Mezclado A Chancado | 0,1924 | 0,0642 | 28,7312 | 2,9106 | 111,6947 | 0,9768 |
| Chancado | 0,0000 | 0,0000 | 7,0741 | 1,0712 | 14,9566 | 0,0000 |
| Zona Lixiviación | 0,0000 | 0,0000 | 1,7206 | 0,2606 | 3,6379 | 0,0000 |
| Camino No Pavimentado Camión A Botadero | 1,1941 | 0,3983 | 178,3314 | 18,0658 | 693,2772 | 6,0631 |
| Camino No Pavimentado Camionetas A Botadero | 0,0073 | 0,0020 | 1,3096 | 0,1320 | 5,0935 | 0,0234 |
| Zona Botadero Total | 18,9939 | 8,5472 | 8,6851 | 7,2250 | 10,6023 | 90,9173 |
| Zona Carga de Marinas | 0,0000 | 0,0000 | 1,1448 | 0,1734 | 2,4205 | 0,0000 |
| Ruta Traslado Marinas 1 | 0,0075 | 0,0025 | 4,2307 | 0,4245 | 16,4601 | 0,0382 |
| Ruta Traslado Marinas 2 | 0,0128 | 0,0043 | 7,2036 | 0,7229 | 28,0267 | 0,0651 |
| Rampa 1A | 3,7467 | 1,6860 | 1,7554 | 1,4316 | 2,1806 | 17,9344 |
| Rampa 1B | 3,7467 | 1,6860 | 1,7554 | 1,4316 | 2,1806 | 17,9344 |
| Rampa 2 | 3,7467 | 1,6860 | 1,7554 | 1,4316 | 2,1806 | 17,9344 |
| Camino No Pavimentado Camionetas Traslado De Marinas | 0,0014 | 0,0004 | 0,2457 | 0,0248 | 0,9556 | 0,0044 |
| Total | 71,3062 | 31,7273 | 483,2813 | 73,1911 | 1782,2763 | 342,1800 |

<!-- Estadísticas: 19 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 3: Emisiones Escenario de Operación |Fuentes|Cierre [Ton/año]|Col3|Col4|Col5|Col6|Col7| |---|---|---|---|---|---|---| -->
<!-- FIN TABLA 2 -->


16

4 SIMULACIÓN DE DISPERSIÓN

|Fuentes|Operación [Ton/año]|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Fuentes|CO|HC|MP10|MP2,5|MPS|NO2|
|Área Extracción de Ripios|0,0000|0,0000|7,0741|1,0712|14,9566|0,0000|
|Camino CAEX Zona Extracción A Zona Mezcla|1,6585|0,5531|202,6826|20,5914|823,6919|8,4210|
|Camino No Pavimentado Camionetas Extracción A Mezclado|0,0103|0,0028|1,5048|0,1519|6,1188|0,0329|
|Área de Mezcla|37,9877|17,0945|28,0770|16,0713|43,8420|181,8346|
|Camino No Pavimentado Camión Zona Mezclado A Chancado|0,1924|0,0642|28,7312|2,9106|111,6947|0,9768|
|Chancado|0,0000|0,0000|7,0741|1,0712|14,9566|0,0000|
|Zona Lixiviación|0,0000|0,0000|1,7206|0,2606|3,6379|0,0000|
|Camino No Pavimentado Camión A Botadero|1,1941|0,3983|178,3314|18,0658|693,2772|6,0631|
|Camino No Pavimentado Camionetas A Botadero|0,0073|0,0020|1,3096|0,1320|5,0935|0,0234|
|Zona Botadero Total|18,9939|8,5472|8,6851|7,2250|10,6023|90,9173|
|Zona Carga de Marinas|0,0000|0,0000|1,1448|0,1734|2,4205|0,0000|
|Ruta Traslado Marinas 1|0,0075|0,0025|4,2307|0,4245|16,4601|0,0382|
|Ruta Traslado Marinas 2|0,0128|0,0043|7,2036|0,7229|28,0267|0,0651|
|Rampa 1A|3,7467|1,6860|1,7554|1,4316|2,1806|17,9344|
|Rampa 1B|3,7467|1,6860|1,7554|1,4316|2,1806|17,9344|
|Rampa 2|3,7467|1,6860|1,7554|1,4316|2,1806|17,9344|
|Camino No Pavimentado Camionetas Traslado De Marinas|0,0014|0,0004|0,2457|0,0248|0,9556|0,0044|
|Total|71,3062|31,7273|483,2813|73,1911|1782,2763|342,1800|

Tabla 3: Emisiones Escenario de Operación

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Rampa 1B|3,7467|1,6860|1,7554|1,4316|2,1806|17,9344| |Rampa 2|3,7467|1,6860|1,7554|1,4316|2,1806|17,9344| |Camino No Pavimentado Camionetas Traslado De Marinas|0,0014|0,0004|0,2457|0,0248|0,9556|0,0044| |Total|71,3062|31,7273|483,2813|73,1911|1782,2763|342,1800| -->

**Tabla 3: Emisiones Escenario de Operación**

| Fuentes | Cierre [Ton/año] | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Fuentes | CO | HC | MP10 | MP2,5 | MPS | NO2 |
| Ruta Camionetas | 0,0003 | 0,0001 | 0,0509 | 0,0051 | 0,1979 | 0,0009 |
| Área Extracción De Ripios | 0,0950 | 0,0428 | 0,0348 | 0,0348 | 0,0348 | 0,4549 |
| Total | 0,0953 | 0,0428 | 0,0857 | 0,0400 | 0,2328 | 0,4558 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 4: Emisiones Escenario de Cierre # 4 Simulación de dispersión -->
<!-- FIN TABLA 3 -->


|Fuentes|Cierre [Ton/año]|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Fuentes|CO|HC|MP10|MP2,5|MPS|NO2|
|Ruta Camionetas|0,0003|0,0001|0,0509|0,0051|0,1979|0,0009|
|Área Extracción De Ripios|0,0950|0,0428|0,0348|0,0348|0,0348|0,4549|
|Total|0,0953|0,0428|0,0857|0,0400|0,2328|0,4558|

Tabla 4: Emisiones Escenario de Cierre

# 4 Simulación de dispersión

El presente documento da cuenta de los resultados obtenidos al modelar la dispersión atmosférica de las

concentraciones de MP10, MP2 _,_ 5, MPS y gases (CO, HC y NO 2 ) para el Proyecto "Lixiviación de Ripios y

Recursos Artificiales" de Chuquicamata CODELCO Chile, Región de Antofagasta, Chile.

Dado que para la Operación de este Proyecto se detendrán operaciones de la Mina Sur y Chancado

Harneado de la PTMP, también se modela la dispersión atmosférica de las concentraciones de MP10 y MP2 _,_ 5

para la Operación Actual, obteniendo la diferencia entre ambos escenarios con el fin de demostrar que las

emisiones del Proyecto futuro serán menores que la Operación Actual.

Los detalles del inventario de emisiones se encuentran en el documento "Inventario de Emisiones", anexo al

Proyecto.

El área de modelación corresponde a una grilla de 72 x 72 km [2], con un espaciamiento de 1 km., en cuyo

interior se encuentra ubicado el sitio de emplazamiento del Proyecto y puntos de interés. Las figuras 1 a la 4

presentan la zona de estudio.

17

## 4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

La simulación de las concentraciones de material particulado asociadas al Proyecto, fueron modeladas según

requerimiento de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA, 2012” Servicio de Evaluación

Ambiental, mediante la aplicación del sistema de modelación atmosférica “WRF - CALPUFF” definido por la

agencia EPA como sistema de referencia para simular la dispersión de contaminantes provenientes de complejos

industriales ubicados en terreno complejo.

La meteorología utilizada en la modelación, corresponde a la obtenida por medio del modelo meteorológico

de pronóstico Weather Research and Forecasting Model (WRF), la cual será utilizada como entrada para el

modelo de dispersión CALPUFF. Dicha información es referente al entorno del proyecto y corresponde al periodo

comprendido entre el 1 de enero y el 31 de diciembre del año 2012.

Cabe destacar que las emisiones de NO _x_ fueron consideradas como NO 2 en su totalidad, lo que constituye

el escenario más conservador.

## 4.1 Aportes

Mediante la aplicación del modelo CALPUFF fue posible obtener las concentraciones de material particu

lado, basándose en los campos de vientos generados por la modelación meteorológica realizada con WRF.

Cabe destacar que cuando entre en funcionamiento el presente proyecto, algunas fuentes preexistentes

dejarán de estar en vigencia. Por ende, para evaluar el real impacto se debe hacer la diferencia entre la

operación proyectada y la operación actual (caso base).

Las tablas 7, 9, 11, 13 y 15 presentan el resumen de las concentraciones resultantes de la modelación en

los puntos de interés. Las coordenadas del punto de máximo impacto (PMI) se muestran en la tabla 5.

Al observar la diferencia entre la Operación Actual del Proyecto y la Operación Proyectada, los aportes

para MP10 y MP2 _,_ 5 son nulos, esto dado que las emisiones en la Operación Actual son mayores a las emi

siones que se presentarán en la Operación proyectada. En cuanto a los gases los aportes son los mismos que

para Operación Proyectada, debido a que la Operación Actual sólo presenta emisiones de MP10 y MP2 _,_ 5, sin

embargo estos aportes son bajos (practicamente nulos), con respecto a la norma, Las mayores concentraciones

se observan en el NO 2 alcanzando 0,89 _μ_ g/m [3] N como promedio anual y 10,22 _μ_ g/m [3] N para el percentil 99

horario, todo esto en la estación PVK.

En cuanto al escenario de Construcción, este presenta concentraciones inferiores a 0,91 _μ_ g/m [3] N en todos

contaminantes y estadísticos evaluados. En cuanto a los aportes (a la línea de base de la zona) estos alcanzan

un 0,2% y 0,1% para promedio anual y P98 diario respectivamente en MP10 en la estación PVK. Respecto al

escenario de Cierre, los aportes a la línea de base de la zona son nulos para todos los contaminantes.

18

4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

|Contaminante|Estadístico|Esc. Operación Actual|Col4|Esc. Construcción|Col6|Esc. Operación Proyectada|Col8|Esc. Cierre|Col10|
|---|---|---|---|---|---|---|---|---|---|
|Contaminante|Estadístico|Lon|Lat|Lon|Lat|Lon|Lat|Lon|Lat|
|CO|P99 8hr|-|-|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3291|
|CO|P99 hr|-|-|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3291|
|HC|~~_x_ ~~Anual|-|-|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3201|
|HC|P98 diario|-|-|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3291|
|MP10|~~_x_ ~~Anual|-68,9124|-22,3291|-68,9124|-22,3111|-68,8831|-22,3741|-68,9221|-22,3201|
|MP10|P98 diario|-68,9124|-22,3201|-68,9124|-22,3111|-68,8831|-22,3741|-68,9221|-22,3291|
|MP2,5|~~_x_ ~~Anual|-68,8831|-22,3471|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3201|
|MP2,5|P98 diario|-68,8831|-22,3471|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3291|
|MPS|~~_x_ ~~Anual|-|-|-68,9124|-22,3111|-68,9124|-22,3111|-68,9026|-22,3111|
|MPS|~~_x_ ~~Mensual|-|-|-68,9124|-22,3111|-68,9124|-22,3111|-68,9026|-22,3111|
|NO2|~~_x_ ~~Anual|-|-|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3201|
|NO2|P99 hr|-|-|-68,8734|-22,3651|-68,9026|-22,3291|-68,9221|-22,3291|

Tabla 5: Coordenadas del punto de máximo impacto (PMI).

### 4.1.1 Comparación con la Norma

Las normas chilenas de calidad ambiental, cada una dictada por medio de un Decreto Supremo, establecen los

valores de las concentraciones y períodos, máximos o mínimos permisibles de los contaminantes. La tabla 6

muestra las concentraciones máximas permitidas según la normativa Chilena vigente, el tipo de norma a la cual

corresponde y el decreto que establece estos límites. Cabe destacar que una norma de tipo primaria es aquella

que establece los valores de las concentraciones y períodos, máximos y mínimos permisibles cuya presencia

en el ambiente pueda constituir un riesgo para la vida o la salud de la población. Analogamente las de tipo

secundaria norman aquellos contaminantes cuya presencia en el ambiente pueda constituir un riesgo para la

protección o conservación del medio ambiente, o la preservación de la naturaleza. (Fuente: Ley 19.300 de Bases

del Medio Ambiente)

19

4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

|Contaminante|Tipo de Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|MPS|Secundaria|Promedio del Periodo|100 mg/m2-día|D.S. 04/92 MINAGRI|
|MPS|Secundaria|Promedio Mensual|150 mg/m2-día|D.S. 04/92 MINAGRI|
|MP10|Primaria|Promedio del Periodo|50_ μ_g/m3N|D.S. 45/02 MINSEGPRES|
|MP10|Primaria|Percentil 98 diario|150_ μ_g/m3N|D.S. 20/13 MMA|
|MP2_._5|Primaria|Promedio del Periodo|20_ μ_g/m3N|D.S. 12/11 MMA|
|MP2_._5|Primaria|Percentil 98 diario|50_ μ_g/m3N|D.S. 12/11 MMA|
|SO2|Primaria|Promedio del Periodo|80_ μ_g/m3N|D.S. 113/02 MINSEGPRES|
|SO2|Primaria|Percentil 99 diario|250_ μ_g/m3N|D.S. 113/02 MINSEGPRES|
|SO2|Secundaria|Promedio del Periodo|80_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 diario|365_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,73 horario|1.000_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|NO2|Primaria|Promedio del Periodo|100_ μ_g/m3N|D.S. 114/02 MINSEGPRES|
|NO2|Primaria|Percentil 99 horario|400_ μ_g/m3N|D.S. 114/02 MINSEGPRES|
|CO|Primaria|Percentil 99 8 horas|10.000_ μ_g/m3N|D.S. 115/02 MINSEGPRES|
|CO|Primaria|Percentil 99 horario|30.000_ μ_g/m3N|D.S. 115/02 MINSEGPRES|
|O3|Primaria|Percentil 99 8 horas|120_ μ_g/m3N|D.S. 112/02 MINSEGPRES|

Tabla 6: Valores límites de referencia según la normativa vigente para cada contaminante.

A continuación, en las tablas 8, 10, 12, 14 y 16 se presenta una comparación porcentual entre los límites

establecidos por la normativa vigente y los aportes obtenidos en la modelación de contaminantes atmosféricos

del presente proyecto.

20

4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

|[μg/m3N] NO2|P99 hr|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0.4 %|0.1 %|0.5 %|0.5 %|1.0 %|0.6 %|32.4 %|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0.3 %|0 %|0.3 %|0.4 %|1.0 %|0.6 %|39.4 %|
|MP10 [_μ_g/m3N]|P98 diario|1.6 %|0.3 %|1.8 %|2.0 %|3.9 %|2.2 %|197.7 %|
|MP10 [_μ_g/m3N]|_x_ Anual|1.4 %|0.1 %|1.3 %|2.0 %|4.5 %|2.5 %|213.7 %|
|HC [_μ_g/m3N]|P98 diario|-|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_ Anual|-|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99 hr|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|CO [_μ_g/m3N]|P99 8hr|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

21

|[μg/m3N] NO2|P99 hr|-|-|-|-|-|-|-|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|-|-|-|-|-|-|-|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0.2003|0.0324|0.2305|0.2480|0.5128|0.2782|16.1883|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0.0606|0.0052|0.0594|0.0874|0.2091|0.1113|7.8876|
|MP10 [_μ_g/m3N]|P98 diario|2.4678|0.3871|2.6749|3.0092|5.8423|3.3401|296.5260|
|MP10 [_μ_g/m3N]|_x_ Anual|0.6910|0.0578|0.6707|0.9776|2.2503|1.2358|106.8394|
|HC [_μ_g/m3N]|P98 diario|-|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_ Anual|-|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99 hr|-|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99 8hr|-|-|-|-|-|-|-|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

|[μg/m3N] NO2|P99 hr|0.1 %|0 %|0.1 %|0.1 %|0.2 %|0.1 %|4.3 %|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|0 %|0 %|0 %|0 %|0.1 %|0 %|3.2 %|
|MPS [mg/m2-día]|_x_ Mensual|0 %|0 %|0 %|0 %|0 %|0 %|22.5 %|
|MPS [mg/m2-día]|_x_ Anual|0 %|0 %|0 %|0 %|0 %|0 %|30.5 %|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0.1 %|0 %|0.1 %|0.1 %|0.1 %|0.1 %|3.8 %|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0 %|0 %|0 %|0.1 %|0.1 %|0.1 %|5.9 %|
|MP10 [_μ_g/m3N]|P98 diario|0.1 %|0 %|0.1 %|0.1 %|0.1 %|0.1 %|3.8 %|
|MP10 [_μ_g/m3N]|_x_ Anual|0.1 %|0 %|0.1 %|0.1 %|0.2 %|0.1 %|6.4 %|
|HC [_μ_g/m3N]|P98 diario|-|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_ Anual|-|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99 hr|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|CO [_μ_g/m3N]|P99 8hr|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

22

|[μg/m3N] NO2|P99 hr|0.3416|0.0309|0.3688|0.4677|0.9099|0.5425|17.2234|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|0.0209|0.0021|0.0201|0.0309|0.0751|0.0400|3.1723|
|MPS [mg/m2-día]|_x_ Mensual|0.0029|0.0005|0.0031|0.0038|0.0104|0.0048|33.7750|
|MPS [mg/m2-día]|_x_ Anual|0.0063|0.0051|0.0064|0.0096|0.0287|0.0120|30.5003|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0.0251|0.0037|0.0266|0.0310|0.0640|0.0365|1.8931|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0.0077|0.0008|0.0075|0.0114|0.0278|0.0148|1.1826|
|MP10 [_μ_g/m3N]|P98 diario|0.0907|0.0153|0.1023|0.1142|0.2159|0.1288|5.6891|
|MP10 [_μ_g/m3N]|_x_ Anual|0.0280|0.0027|0.0268|0.0398|0.0907|0.0506|3.1832|
|HC [_μ_g/m3N]|P98 diario|0.0074|0.0011|0.0079|0.0092|0.0190|0.0108|0.5564|
|HC [_μ_g/m3N]|_x_ Anual|0.0023|0.0002|0.0022|0.0034|0.0082|0.0044|0.3475|
|CO [_μ_g/m3N]|P99 hr|0.0824|0.0074|0.0889|0.1128|0.2196|0.1309|4.1598|
|CO [_μ_g/m3N]|P99 8hr|0.0345|0.0054|0.0396|0.0463|0.0971|0.0541|2.2472|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

|[μg/m3N] NO2|P99 hr|1.0 %|0.1 %|1.1 %|1.3 %|2.6 %|1.5 %|78.3 %|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|0.3 %|0 %|0.2 %|0.4 %|0.9 %|0.5 %|42.0 %|
|MPS [mg/m2-día]|_x_ Mensual|0 %|0 %|0 %|0 %|0.1 %|0 %|214.9 %|
|MPS [mg/m2-día]|_x_ Anual|0.1 %|0.1 %|0.1 %|0.1 %|0.4 %|0.2 %|290.9 %|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0.3 %|0.1 %|0.4 %|0.4 %|0.9 %|0.5 %|18.8 %|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0.3 %|0 %|0.2 %|0.4 %|0.9 %|0.5 %|26.0 %|
|MP10 [_μ_g/m3N]|P98 diario|0.7 %|0.1 %|0.8 %|0.9 %|2.0 %|1.1 %|35.8 %|
|MP10 [_μ_g/m3N]|_x_ Anual|0.7 %|0.1 %|0.6 %|1.0 %|2.4 %|1.3 %|48.6 %|
|HC [_μ_g/m3N]|P98 diario|-|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_ Anual|-|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99 hr|0 %|0 %|0 %|0 %|0 %|0 %|0.2 %|
|CO [_μ_g/m3N]|P99 8hr|0 %|0 %|0 %|0 %|0 %|0 %|0.4 %|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

23

|[μg/m3N] NO2|P99 hr|4.0781|0.3867|4.3868|5.3911|10.2224|6.1753|313.2188|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|0.2558|0.0248|0.2498|0.3726|0.8920|0.4790|41.9832|
|MPS [mg/m2-día]|_x_ Mensual|0.0325|0.0057|0.0353|0.0433|0.1501|0.0588|322.3154|
|MPS [mg/m2-día]|_x_ Anual|0.0759|0.0585|0.0782|0.1197|0.4119|0.1554|290.9380|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0.1682|0.0268|0.1935|0.2127|0.4475|0.2485|9.4108|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0.0521|0.0052|0.0493|0.0760|0.1860|0.0990|5.2086|
|MP10 [_μ_g/m3N]|P98 diario|1.0984|0.1703|1.2525|1.3791|2.9597|1.5962|53.6279|
|MP10 [_μ_g/m3N]|_x_ Anual|0.3364|0.0336|0.3133|0.4924|1.2200|0.6460|24.2856|
|HC [_μ_g/m3N]|P98 diario|0.0770|0.0122|0.0860|0.0966|0.1964|0.1105|7.5072|
|HC [_μ_g/m3N]|_x_ Anual|0.0237|0.0023|0.0232|0.0346|0.0828|0.0445|3.9309|
|CO [_μ_g/m3N]|P99 hr|0.8499|0.0806|0.9141|1.1235|2.1305|1.2868|65.3850|
|CO [_μ_g/m3N]|P99 8hr|0.3917|0.0575|0.4208|0.4743|0.9513|0.5379|37.5308|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

|[μg/m3N] NO2|P99 hr|0 %|0 %|0 %|0 %|0 %|0 %|0.1 %|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|0 %|0 %|0 %|0 %|0 %|0 %|0.1 %|
|MPS [mg/m2-día]|_x_ Mensual|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|MPS [mg/m2-día]|_x_ Anual|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|MP10 [_μ_g/m3N]|P98 diario|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|MP10 [_μ_g/m3N]|_x_ Anual|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|HC [_μ_g/m3N]|P98 diario|-|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_ Anual|-|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99 hr|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|CO [_μ_g/m3N]|P99 8hr|0 %|0 %|0 %|0 %|0 %|0 %|0 %|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

24

|[μg/m3N] NO2|P99 hr|0.0040|0.0004|0.0041|0.0054|0.0120|0.0065|0.3493|
|---|---|---|---|---|---|---|---|---|
|NO2 [_μ_g/m3N]|_x_ Anual|0.0003|0.0000|0.0003|0.0004|0.0008|0.0005|0.0572|
|MPS [mg/m2-día]|_x_ Mensual|0.0000|0.0000|0.0000|0.0000|0.0000|0.0000|0.0385|
|MPS [mg/m2-día]|_x_ Anual|0.0000|0.0000|0.0000|0.0000|0.0000|0.0000|0.0342|
|MP2_,_ 5 [_μ_g/m3N]|P98 diario|0.0001|0.0000|0.0001|0.0001|0.0002|0.0001|0.0081|
|MP2_,_ 5 [_μ_g/m3N]|_x_ Anual|0.0000|0.0000|0.0000|0.0000|0.0001|0.0000|0.0045|
|MP10 [_μ_g/m3N]|P98 diario|0.0002|0.0000|0.0002|0.0002|0.0004|0.0003|0.0092|
|MP10 [_μ_g/m3N]|_x_ Anual|0.0001|0.0000|0.0001|0.0001|0.0002|0.0001|0.0053|
|HC [_μ_g/m3N]|P98 diario|0.0001|0.0000|0.0001|0.0001|0.0002|0.0001|0.0099|
|HC [_μ_g/m3N]|_x_ Anual|0.0000|0.0000|0.0000|0.0000|0.0001|0.0000|0.0054|
|CO [_μ_g/m3N]|P99 hr|0.0008|0.0001|0.0009|0.0011|0.0025|0.0014|0.0730|
|CO [_μ_g/m3N]|P99 8hr|0.0005|0.0001|0.0005|0.0005|0.0010|0.0006|0.0452|
|Receptor|Receptor|Centro|Chiu Chiu|Hospital del Cobre|Marzo 23|PVK|SML|PMI|

4.1 Aportes 4 SIMULACIÓN DE DISPERSIÓN

|Receptor|MP10 [μg/m3N]|Col3|MP2, 5 [μg/m3N]|Col5|
|---|---|---|---|---|
|Receptor|~~_x_ ~~Anual|P98 diario|~~_x_ ~~Anual|P98 diario|
|Centro|-0.2857|-1.2294|-0.0020|-0.0192|
|Chiu Chiu|-0.0238|-0.2196|0.0000|-0.0055|
|Hospital del Cobre|-0.2657|-1.2196|-0.0010|-0.0152|
|Marzo 23|-0.3860|-1.5079|-0.0019|-0.0188|
|PVK|-0.7871|-2.3810|-0.0004|-0.0322|
|SML|-0.4794|-1.6117|-0.0020|-0.0175|
|PMI|-82.8022|-242.5695|-2.6391|-6.7550|

Tabla 15: Aportes del proyecto en los puntos receptores para el escenario de Operación Proyectada - Operación

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Marzo 23|-0.3860|-1.5079|-0.0019|-0.0188| |PVK|-0.7871|-2.3810|-0.0004|-0.0322| |SML|-0.4794|-1.6117|-0.0020|-0.0175| |PMI|-82.8022|-242.5695|-2.6391|-6.7550| -->

**Tabla 15: Aportes del proyecto en los puntos receptores para el escenario de Operación Proyectada - Operación**

| Receptor | MP10 [μg/m3N] | Col3 | MP2, 5 [μg/m3N] | Col5 |
| --- | --- | --- | --- | --- |
| Receptor | ~~_x_ ~~Anual | P98 diario | ~~_x_ ~~Anual | P98 diario |
| Centro | -0.6 % | -0.8 % | 0 % | 0 % |
| Chiu Chiu | 0 % | -0.1 % | 0 % | 0 % |
| Hospital del Cobre | -0.5 % | -0.8 % | 0 % | 0 % |
| Marzo 23 | -0.8 % | -1.0 % | 0 % | 0 % |
| PVK | -1.6 % | -1.6 % | 0 % | -0.1 % |
| SML | -1.0 % | -1.1 % | 0 % | 0 % |
| PMI | -165.6 % | -161.7 % | -13.2 % | -13.5 % |

<!-- Estadísticas: 8 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 16: Relación porcentual entre los aportes y la normativa vigente para el escenario de Operación Proyectada - Operación Actual. -->
<!-- FIN TABLA 15 -->

Actual.

|Receptor|MP10 [μg/m3N]|Col3|MP2, 5 [μg/m3N]|Col5|
|---|---|---|---|---|
|Receptor|~~_x_ ~~Anual|P98 diario|~~_x_ ~~Anual|P98 diario|
|Centro|-0.6 %|-0.8 %|0 %|0 %|
|Chiu Chiu|0 %|-0.1 %|0 %|0 %|
|Hospital del Cobre|-0.5 %|-0.8 %|0 %|0 %|
|Marzo 23|-0.8 %|-1.0 %|0 %|0 %|
|PVK|-1.6 %|-1.6 %|0 %|-0.1 %|
|SML|-1.0 %|-1.1 %|0 %|0 %|
|PMI|-165.6 %|-161.7 %|-13.2 %|-13.5 %|

Tabla 16: Relación porcentual entre los aportes y la normativa vigente para el escenario de Operación Proyectada

- Operación Actual.

25

## 4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN 4.2 Isolíneas de concentración

A continuación se presentan las isoconcentraciones obtenidas en la modelación para MP10, MP2 _,_ 5 y gases.

Se observa que la pluma es mayormente desviada hacia el oeste de la comuna de Calama debido a que los

vientos predominantes forman una especie de escudo en este sector, imposibilitando que los contaminantes

lleguen directamente.

26

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

27

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

28

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

29

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

30

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

31

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

32

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

33

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

34

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

35

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

36

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

37

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

38

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

39

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

40

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

41

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

42

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

43

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

44

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

45

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

46

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

47

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

48

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

49

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

50

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

51

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

52

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

53

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

54

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

55

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

56

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

57

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

58

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

59

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

60

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

61

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

62

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

63

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

64

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

65

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

66

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

67

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

68

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

69

4.2 Isolíneas de concentración 4 SIMULACIÓN DE DISPERSIÓN

70

## 4.3 Análisis de Incertidumbre 4 SIMULACIÓN DE DISPERSIÓN 4.3 Análisis de Incertidumbre

El objetivo de un análisis de incertidumbre es poner en contexto los resultados de las simulaciones de dispersión

con los errores del modelo meteorológico. De esta manera, se apunta a evaluar posibles sobre o subestimaciones

del modelo de dispersión. En este sentido se observa que el modelo WRF representa muy bien la meteorología

predominante del sector, ya sea para velocidad o dirección de viento. Debido a lo anterior, se concluye que no

existen antecedentes necesarios para considerar incertidumbres significativas en las concentraciones presentadas

anteriormente, ya sea en las magnitudes o en la dirección de la pluma.

71

5 CONCLUSIONES

# 5 Conclusiones

El presente informe tiene por finalidad evaluar las concentraciones de MP10, MP2 _,_ 5, MPS y gases (CO,

HC, NO 2 ), en los puntos receptores ubicados en la comuna de Calama en la región de Antofagasta.

Cabe destacar que cuando entre en funcionamiento el presente proyecto, algunas fuentes preexistentes de

jarán de estar en vigencia. Por ende, para evaluar el real impacto se debe hacer la diferencia entre la operación

proyectada y la operación actual (caso base).

Escenario de Construcción

El escenario de Construcción presenta concentraciones inferiores a 0,91 _μ_ g/m [3] N en todos contaminantes y

estadísticos evaluados. En cuanto a los aportes (a la línea de base de la zona) estos alcanzan un 0,2% y 0,1%

para promedio anual y P98 diario respectivamente en MP10 en la estación PVK.

Escenario de Operación Actual y Proyectada

Al observar la diferencia entre la Operación Actual del Proyecto y la Operación Proyectada, los aportes

para MP10 y MP2 _,_ 5 son nulos, esto dado que las emisiones en la Operación Actual son mayores a las emi

siones que se presentarán en la Operación proyectada. En cuanto a los gases los aportes son los mismos que

para Operación Proyectada, debido a que la Operación Actual sólo presenta emisiones de MP10 y MP2 _,_ 5, sin

embargo estos aportes son bajos (practicamente nulos), con respecto a la norma, Las mayores concentraciones

se observan en el NO 2 alcanzando 0,89 _μ_ g/m [3] N como promedio anual y 10,22 _μ_ g/m [3] N para el percentil 99

horario, todo esto en la estación PVK.

Escenario de Cierre

El escenario de cierre no modifican la línea de base existente en la zona ya que el porcentaje de la norma

es 0% para todos los contaminantes y estadísticos evaluados.

72