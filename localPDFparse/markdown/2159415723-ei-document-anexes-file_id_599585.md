---
title: Sin título
author: Andrés Burboa Lizama
date: D:20230308131349-03'00'
language: es
type: manual
pages: 11
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 2.04 MODELO HIDRÁULICO C_04 ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO LLANOS DE RUNGUE
  - Contenidos
  - Figuras
  - Tablas
  - 1. Introducción
  - 2. Parámetros de entrada
  - n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)
  - n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales
  - 3. Resultados
  - 4. Referencias
-->

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.04 MODELO HIDRÁULICO C_04 ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

para UKA CHILE y PLAN 8

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|B|-|08/03/2023|Cliente|DMM|BGP|ABL|
|A|-|20/01/2023|Cliente|DMM|CJS|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comuna de Illapel<br>Región de Coquimbo|Col3|
|---|---|---|
|<br>|UKA-B22032-EHID-DOC-02.04|**Rev. B**|

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# Contenidos

**1.** **Introducción .................................................................................................................... 3**

**2.** **Parámetros de entrada ................................................................................................... 3**

2.1. Coeficiente de rugosidad .................................................................................................................... 3
2.2. Condiciones de borde e iniciales ....................................................................................................... 5

2.3. Otras consideraciones.......................................................................................................................... 7

**3.** **Resultados ....................................................................................................................... 7**

**4.** **Referencias .................................................................................................................... 10**

# Figuras

Figura 2-1: IMG_20221222_134025 ................................................................................................................................. 4

Figura 2-2. Ubicación condiciones de borde ................................................................................................................. 6

Figura 2-3. Hidrogramas de entrada ............................................................................................................................. 7

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 8

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 9

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente .............................................. 10

# Tablas

Tabla 2-1: Información de imágenes de visita a terreno ............................................................................................ 4

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PARQUE FOTOVOLTAICO LLANOS DE RUNGUE Figura 2-1: IMG_20221222_134025 -->

**Tabla 2-1: Información de imágenes de visita a terreno**

| Figura | Nombre archivo | Este [m] | Norte [m] | CRS (*) |
| --- | --- | --- | --- | --- |
| Figura 2-1 | IMG_20221222_135232 | 275 650.0 | 6 499 627.5 | UTM WGS84 H19 S |

<!-- Estadísticas: 1 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- (*) Coordinate reference system La Tabla 2-2 muestra la condición del cauce según los criterios del método: -->
<!-- FIN TABLA 2-1 -->


Tabla 2-2. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ...................... 4

Tabla 2-3. Condiciones de borde e iniciales. ................................................................................................................. 5

ii
BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# 1. Introducción

Se construyó el modelo hidráulico denominado C_04, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2020):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La figura presentada a continuación fue registrada durante la visita a terreno realizada el día 22/12/2022 y

sus coordenadas se encuentran en la siguiente tabla:

3
BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 2-1: IMG_20221222_134025

Tabla 2-1: Información de imágenes de visita a terreno

|Figura|Nombre archivo|Este [m]|Norte [m]|CRS (*)|
|---|---|---|---|---|
|Figura 2-1|IMG_20221222_135232|275 650.0|6 499 627.5|UTM WGS84 H19 S|

(*) Coordinate reference system

La Tabla 2-2 muestra la condición del cauce según los criterios del método:

Tabla 2-2. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

4

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.012|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|

BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|Condición del cauce|Símbolo|Valor|
|---|---|---|
|**Coeficiente de rugosidad**|n|**0.052**|

## 2.2. Condiciones de borde e iniciales

Se definieron tres tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) intermedia y (iii) final o

aguas abajo. La CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Por

otro lado, parte del modelo posee una longitud de cauce significativa y sus caudales pueden variar bastante

entre su inicio y final, ya que el área drenante de su cuenca aumenta a medida que se avanza hacia aguas

abajo. En estos casos se agrega una CB intermedia, cuyo objetivo es añadir un incremento de caudal al

modelo para representar el aumento del caudal a lo largo del cauce. Por último, se incluye la CB aguas abajo

para permitir la salida del flujo.

En resumen, las CB aguas arriba e intermedias incluyen parámetros de caudal en función de su ubicación a

lo largo del cauce. Además, las tres CB poseen condición de borde de altura normal, definiendo el parámetro

de pendiente normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-3 y Figura 2-2:

Tabla 2-3. Condiciones de borde e iniciales.

5

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00||✅||0.32|0.170|
|US_01|✅|||4.72|0.029|
|DS|||✅|--|0.280|

BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 2-2. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

6
BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-3. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 2 x 2 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas 20 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

7
BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

8
BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

9
BAQUA Ingeniería

www.baqua.cl

ANEXO 2.04 MODELO HIDRÁULICO C_04
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

10
BAQUA Ingeniería

www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-2.: Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.**

| Condición del cauce | Col2 | Símbolo | Valor |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad del perímetro mojado | Leve | n1 | 0.005 |
| Variación de las secciones transversales | Gradual | n2 | 0.000 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.015 |
| Densidad de vegetación | Media | n4 | 0.012 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |

**Tabla 2-3.: Condiciones de borde e iniciales.**

| Nombre CB | CB aguas<br>arriba | CB<br>interm. | CB aguas<br>abajo | Caudal<br>[m3/s] | Pendiente<br>[m/m] |
| --- | --- | --- | --- | --- | --- |
| US_00 |  | ✅ |  | 0.32 | 0.170 |
| US_01 | ✅ |  |  | 4.72 | 0.029 |
| DS |  |  | ✅ | -- | 0.280 |
