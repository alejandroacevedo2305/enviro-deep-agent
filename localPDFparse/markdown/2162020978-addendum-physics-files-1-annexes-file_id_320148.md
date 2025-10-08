---
title: Sin título
author: Andrés Burboa Lizama
date: D:20230707123304-04'00'
language: es
type: manual
pages: 10
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO ZALDÍVAR
  - Contenidos
  - Figuras
  - Tablas
  - 1. Introducción
  - 2. Descripción del modelo
  - 3. Parámetros de entrada
  - n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)
  - n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales 3 Baqua Ingeniería
  - 4. Resultados
  ... y 1 secciones más
-->

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
# ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO ZALDÍVAR

para ZAPALERI SPA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|07/07/2023|Revisión cliente|RPF|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comuna de Antofagasta<br>Región de Antofagasta|Col3|
|---|---|---|
||FPG-B22028(3)-EHID2-DOC-02.02.14|Rev. A|

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

# Contenidos

1. Introducción ............................................................................................................................................. 3

2. Descripción del modelo.......................................................................................................................... 3

3. Parámetros de entrada ......................................................................................................................... 3

3.1. Coeficiente de rugosidad .................................................................................................................... 3
3.2. Condiciones de borde e iniciales ...................................................................................................... 4

3.3. Otras Consideraciones ........................................................................................................................ 6

4. Resultados ............................................................................................................................................... 7

4.1. Tormenta periodo de retorno 100 años .......................................................................................... 7

5. Referencias .............................................................................................................................................. 9

# Figuras

Figura 3-1. Ubicación condiciones de borde ................................................................................................................. 5

Figura 3-2. Hidrograma de crecida cuenca LAT_14_00 ............................................................................................. 6

# Tablas

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método de Cowan .................. 4

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 4

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

# 1. Introducción

A continuación, se detallan los antecedentes y metodología empleada para la construcción del modelo

hidráulico LAT_14, que forma parte del estudio de inundación del Área de Generación (AG) y la Línea de Alta

Tensión (LAT) del proyecto Parque Fotovoltaico Zaldívar.

El modelo se basa en la topografía de detalle del proyecto, la cual fue representada mediante un Modelo

Digital de Terreno (MDT), que fue obtenido a partir de un vuelo fotogramétrico.

Se tomaron en cuenta los resultados del análisis hidrológico (Anexo 1), donde se consideró una tormenta de

duración de 6 horas y periodo de retorno de 100 años.

Los resultados obtenidos permiten conocer las características del eje hidráulico y las áreas de inundación. A

continuación, se presentan las consideraciones para elaborar el modelo y los principales resultados

obtenidos.

# 2. Descripción del modelo

Se construyó el modelo hidráulico de la cuenca LAT_14_00 empleando el software HEC-RAS (HEC, 2022),

representando la condición actual de los cauces y utilizando para su cálculo un flujo bidimensional.

Se realizaron ingresos de caudal mediante el hidrograma de crecida de la cuenca antes mencionada,

considerando una malla de cálculo con celdas de 1.0 x 1.0 m en toda su extensión.

# 3. Parámetros de entrada

## 3.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2020)

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho
# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales 3 Baqua Ingeniería

[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método:

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método de Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Alternándose<br>Frecuentemente|n2|0.010|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.000|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

## 3.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB), aguas arriba y aguas abajo. La CB aguas arriba

incorpora el hidrograma de crecida de la cuenca al cauce en el inicio del área de interés, mientras que la CB

aguas abajo permite la salida del flujo.

La condición de borde aguas arriba incluye el hidrograma de crecida de la cuenca LAT_14_00 para el periodo

de retorno 100 años. Además, ambas CB poseen condición de borde de altura normal, definiendo el

parámetro de pendiente normal a partir de la topografía del modelo. La pendiente y el caudal peak del

periodo de retorno se presenta a continuación:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|Tipo de CB|Caudal peak<br>[m3 /s]<br>1.96|Pendiente<br>[mm]<br>0.06|
|---|---|---|---|
|US_ LAT_14_00|Aguas arriba|Aguas arriba|Aguas arriba|
|DS_00|Aguas abajo|-|0.05|

Por otro lado, la ubicación de las condiciones de borde y los hidrogramas de crecida se presentan en las

siguientes Figuras:

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-1. Ubicación condiciones de borde

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 3-2. Hidrograma de crecida cuenca LAT_14_00

## 3.3. Otras Consideraciones

En el modelo hidráulico LAT_14, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant

(opción SWE-ELM en HEC-RAS). El área de flujo se discretizó en celdas de 1.0 x 1.0 m.

Se utilizo un paso de tiempo de 1 segundo ajustado en función de los numero de Courant del modelo, donde

se empleó un máximo de 0.4 y un mínimo de 0.15.

El tiempo de modelación se consideró en función del tiempo del hidrograma de crecida, en particular el

modelo LAT_14 tiene un tiempo de modelación de 10 horas.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

# 4. Resultados

## 4.1. Tormenta periodo de retorno 100 años

Figura 4-1. Profundidad máxima periodo de retorno 100 años. Línea de alta tensión (negro)

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 4-2. Velocidad máxima periodo de retorno 100 años. Línea de alta tensión (negro)

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02.14 MODELO HIDRAULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE FOTOVOLTAICO ZALDÍVAR

Figura 4-3. Hidrograma de salida periodo de retorno de 100 años

# 5. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. HEC-RAS. Versión 6.2. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Condición del cauce para el cálculo del coeficiente de Manning con método de Cowan**

| Condición del cauce | Col2 | Símbolo | Valor |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad del perímetro mojado | Leve | n1 | 0.005 |
| Variación de las secciones transversales | Alternándose<br>Frecuentemente | n2 | 0.010 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.010 |
| Densidad de vegetación | Baja | n4 | 0.000 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| Coeficiente de rugosidad | Coeficiente de rugosidad | n | 0.045 |

**Tabla 3-2.: Condiciones de borde e iniciales**

| Nombre CB | Tipo de CB | Caudal peak<br>[m3 /s]<br>1.96 | Pendiente<br>[mm]<br>0.06 |
| --- | --- | --- | --- |
| US_ LAT_14_00 | Aguas arriba | Aguas arriba | Aguas arriba |
| DS_00 | Aguas abajo | - | 0.05 |
