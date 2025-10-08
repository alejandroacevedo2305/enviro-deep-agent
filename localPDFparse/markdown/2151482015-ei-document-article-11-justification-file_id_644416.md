---
title: Sin título
author: Lastenia Faundez
date: D:20210415192233-04'00'
language: es
type: report
pages: 9
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”
  - Índice
-->

# Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

### Apéndice 2.E-2 Minuta técnica análisis de vegetación con imagen de alta resolución espacial

Preparado por

Abril 2021

# Índice

1 Introducción 1

2 Metodología 2

3 Resultados 3

4 Conclusiones 6

5 Bibliografia 7

#### Índice de Tablas

Tabla 1 Estadística descriptiva de valores de NDVI 5

#### Índice de Figuras

Figura 1 Resultado del índice NDVI en el área del proyecto 3

Figura 2 Histogramas de valores de NDVI por tipo de área del proyecto 4

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | i

## 1 Introducción

El presente reporte corresponde al análisis de coberturas terrestres en el área del Proyecto denominado
“Optimización Planta Solar Sol del Loa", utilizando una imagen multiespectral con alta resolución espacial, con el
objetivo de corroborar la existencia de áreas con ausencia de vegetación. Para ello se utiliza un índice de vegetación
sensible a la detección de coberturas con material fotosintéticamente activo y se analizan los resultados con apoyo
de estadística descriptiva.

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | 1

## 2 Metodología

Se analizó una imagen de alta resolución espacial proveniente del sistema de satélites Pleiades, específicamente
provenientes del sensor Pleaides-1A con una resolución espacial de 50 cm (similar a GeoEye-1), compuesto de 5

bandas:

Pancromática: 480 - 830 nm

Azul: 430-550 nm

Verde: 490-610 nm

Rojo: 600-720 nm

Infrarrojo cercano: 750-950 nm

La ubicación de la escena corresponde al Path 613 y Raw 472 ( [1] ). Esta imagen fue capturada por el sensor el 9 de
diciembre del 2018 a las 14:51 h (UTC) El formato raster corresponde a GeoTTIF. La imagen fue procesada para su
corrección radiométrica y geométrica, posteriormente se construyó el índice para detectar vegetación, denominado
NDVI (Rouse _et al_ ., 1973), mediante la siguiente fórmula:

NDVI= [(][IR−R][)]

(IR+ R)

Siendo IR la banda correspondiente al Infrarrojo cercano (750-950 nm) y R la banda correspondiente al rojo (600720 nm).

El uso de NDVI (índice de vegetación de diferencia normalizada) es ampliamente utilizado para determinar la
presencia de vegetación, ya que es eficiente para el análisis y monitoreo de las condiciones vegetativas y su dinámica
en la cobertura terrestre. El resultado de estas operaciones permite obtener una nueva imagen o banda donde se
destacan determinados píxeles o zonas relacionados con parámetros de las coberturas vegetales, en este caso, de

su existencia en un ambiente desértico.

Para el procesamiento la imagen se utilizó el software QGIS, versión 3.10.1-A Coruña (QGIS.org, 2020) y para el
desarrollo de la estadística descriptiva se utilizó R Project, versión 3.6.3 (R Core Team, 2013)

1 La combinación de un número de Path y un número de Raw identifica de forma exclusiva un centro de escena nominal de la imagen

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | 2

## 3 Resultados

El resultado gráfico se observa en la Figura 1, donde se aplicó un pseudocolor de banda única (opción de simbología
de capa de colores graduados) con un espectro completo de colores que se pueden crear mezclando diferentes
cantidades desde el azul al rojo, donde el azul representa los valores más bajos de NDVI y el rojo los valores más
altos de NDVI. En la figura se observa la ubicación del proyecto y las áreas que cubre en el territorio, donde se puede
observar claramente que los tonos asociados a valores altos de NDVI, en este caso tendientes al rojo, solo se
observan en el cauce del río Loa, correspondiente a la formación ‘Matorral’, en tanto, la totalidad de la superficie
denominada ‘Sin vegetación’ presenta tonos azulados indicativo de valores bajos de NDVI y, consecuentemente,
con ausencia de indicios de presencia de vegetación o elementos fotosintéticamente activos.

Figura 1 Resultado del índice NDVI en el área del proyecto

Fuente: Elaboración propia en base al índice NDVI derivado de imagen Pleiades 1A

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | 3

Para cuantificar los datos que se observan en la Figura 1 se procedió a desarrollar cálculos de estadística descriptiva
de los valores de NDVI de la imagen en relación con las áreas donde el proyecto será desarrollado. Para ello, la
imagen con el índice NDVI fue recortada al área del proyecto y se atributó con los nombres de las formaciones
vegetacionales de la COT, que en este caso son dos: ‘Sin vegetación’ y ‘Matorral’. El resultado gráfico del histograma
de la cantidad de pixeles según su valor de NDVI por formación vegetacional se presenta en la Figura 2, con una
escala similar del eje x (valores de NDVI) para comparar las distribuciones de ambos tipos de superficies. En la figura
se aprecia la distribución del valor de NDVI para la formación clasificada como “Sin vegetación”, en la cual se observa
que la concentración de valores está en torno a un promedio de 0,086, es decir esta superficie presenta valores de
NDVI reducidos que indican la ausencia de actividad fotosintética, la frecuencia en rango de millones de pixel indica
la gran extensión de superficie analizada. En contraste, al cruzar el polígono de la formación ‘Matorral’ con los valores
de NDVI se observa presenta valores típicos de suelo desnudo y de vegetación fotosintéticamente activa, con un
promedio de 0,33, el reducido valor de la frecuencia indica la menor superficie de este polígono o formación, dado
que se acota a un sector del cauce del río Loa. Cabe destacar que el umbral de NDVI para detectar vegetación es,
aproximadamente, en valores mayores a 0,2 (Hashim _et al._,2019, Cheng _et al._,2008), valores menores a este umbral

indican otras coberturas, como, en este caso, suelo desnudo.

Figura 2 Histogramas de valores de NDVI por tipo de área del proyecto

Fuente: Elaboración propia en base al índice NDVI derivado de imagen Pleiades 1A

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | 4

La Tabla 1 presenta un resumen de estadísticas descriptivas del valor de NDVI por formación vegetacional, en ella
se puede observar que, para la formación ‘sin vegetación’ el valor promedio es 0,086 y el valor máximo es de 0,15,
tal que, si consideramos que la vegetación en general se detecta con valores de NDVI superiores a 0,2, se puede
concluir que este espacio o superficie no presenta evidencias de contener material fotosintéticamente activo. En
contraste la formación de ‘Matorral’ presenta un promedio de 0,333 y un máximo de 0,634 dado que gran parte de
este sector está cubierto con vegetación. El cuartil 1 (Q1) y el cuartil 3 (Q3) dan cuenta de la dispersión de valores,
dado que entre ellos se concentra el 50 % de los datos, siendo muy estrecho para la formación ‘sin vegetación’ (suelo
homogéneo) y más amplia para la formación ‘Matorral’ (suelo con diferentes tipos de cubiertas incluyendo
vegetación).

Tabla 1 Estadística descriptiva de valores de NDVI

|Parámetro|Formación|Col3|
|---|---|---|
|Parámetro|Sin vegetación|Matorral|
|N (n° de píxeles)|21.287.678|13.079|
|Mínimo|-0,435|-0,105|
|Q1|0,083|0,191|
|Media|0,086|0,333|
|Q3|0,089|0,479|
|Máximo|0,150|0,634|
|Desv. Est.|0,006|0,157|

Fuente: Elaboración propia en base al índice NDVI derivado de imagen Pleiades 1A.

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | 5

## 4 Conclusiones

El análisis de la cobertura terrestre del área del Proyecto con una imagen multiespectral de alta resolución espacial
(50 cm), indica que la clasificación utilizando el índice NDVI, que es sensible a la presencia de vegetación con
material fotosintéticamente activo, no detectó formaciones vegetacionales activas en el área del Proyecto
denominada ‘sin vegetación’. En contraste, el sector denominado Matorral, que corresponde a una porción del cauce
del río Loa, mostró claramente la detección de vegetación por medio del índice NDVI. La estadística descriptiva
desarrollada apoya esta conclusión con el análisis del conjunto total de píxeles de estos sectores y sus valores de
NDVI, al no detectar evidencia de presencia de vegetación en el área declarada como ‘sin vegetación’.

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | 6

## 5 Bibliografia

Cheng, W. C., Chang, J. C., Chang, C. P., Su, Y., & Tu, T. M. (2008). A Fixed-Threshold Approach to Generate HighResolution Vegetation Maps for IKONOS Imagery. Sensors (Basel, Switzerland), 8(7), 4308-4317.
https://doi.org/10.3390/s8074308

Hashim, H., Latif, Z. A., Adnan, N. A. (2019). ISPRS - International Archives of the Photogrammetry, Remote Sensing
and Spatial Information Sciences, 4216, 237

R Core Team (2013). R: A language and environment for statistical computing. R Foundation for Statistical
Computing, Vienna, Austria. URL http://www.R-project.org/.

Rouse, J.W., Haas, R.H., Schell, J.A. And Deering, D.W. (1973). Monitoring vegetation systems in the Great Plains
with ERTS. In 3rd ERTS Symposium, NASA SP-351 I, pp. 309-317.

QGIS.org (2020). QGIS Geographic Information System. Open Source Geospatial Foundation Project. [http://qgis.org](http://qgis.org/)

Declaración de Impacto Ambiental “Optimización Planta Solar Sol del Loa”

Apéndice 2.E-2 Minuta técnica análisis imagen de alta resolución | 7

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Estadística descriptiva de valores de NDVI**

| Parámetro | Formación | Col3 |
| --- | --- | --- |
| Parámetro | Sin vegetación | Matorral |
| N (n° de píxeles) | 21.287.678 | 13.079 |
| Mínimo | -0,435 | -0,105 |
| Q1 | 0,083 | 0,191 |
| Media | 0,086 | 0,333 |
| Q3 | 0,089 | 0,479 |
| Máximo | 0,150 | 0,634 |
| Desv. Est. | 0,006 | 0,157 |
