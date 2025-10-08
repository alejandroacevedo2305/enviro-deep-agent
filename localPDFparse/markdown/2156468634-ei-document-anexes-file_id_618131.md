---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: manual
pages: 351
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 2.01.01 MODELO HIDRÁULICO PE_01 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO
  - Contenidos
  - Figuras
  - Tablas
  - 1. Introducción
  - 2. Parámetros de entrada
  - n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)
  - n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales
  - 1 BAQUA Ingeniería
  - 3. Resultados
  ... y 353 secciones más
-->

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 02. MODELOS HIDRÁULICOS

ESTUDIO DE INUNDACIÓN

PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.01 MODELO HIDRÁULICO PE_01 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ASP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.01|**Rev. A**|

ANEXO 2.01.01 MODELO HIDRÁULICO PE_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ........................................................................................................ 2

2.3. Otras consideraciones ......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde ......................................................................................................................3

Figura 2-2. Hidrogramas de entrada .................................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ................................................5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años ....................................................5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................. 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ...................................................................................................................... 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.01 MODELO HIDRÁULICO PE_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_01, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.01 MODELO HIDRÁULICO PE_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||1.17|0.0519|
|US_01|✅|||0.75|0.0188|
|US_02||✅||0.57|0.0073|
|US_03||✅||1.02|0.0708|
|US_04||✅||1.99|0.0093|
|US_05||✅||0.61|0.0260|
|US_06||✅||0.06|0.1017|
|DS|||✅|--|0.0001|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.01 MODELO HIDRÁULICO PE_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.01 MODELO HIDRÁULICO PE_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.01 MODELO HIDRÁULICO PE_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.01 MODELO HIDRÁULICO PE_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.02 MODELO HIDRÁULICO PE_02 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BJG|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.02|**Rev. A**|

ANEXO 2.01.02 MODELO HIDRÁULICO PE_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.02 MODELO HIDRÁULICO PE_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_02, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.02 MODELO HIDRÁULICO PE_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron tres tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) intermedia y (iii) final o

aguas abajo. Las CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Por

otro lado, parte del modelo posee una longitud de cauce significativa y sus caudales pueden variar bastante

entre su inicio y final, ya que el área drenante de su cuenca aumenta a medida que se avanza hacia aguas

abajo. En estos casos se agregan dos CB intermedia, cuyo objetivo es añadir un incremento de caudal al

modelo para representar el aumento del caudal a lo largo del cauce. Por último, se incluye la CB aguas abajo

para permitir la salida del flujo.

En resumen, las CB aguas arriba e intermedias incluyen parámetros de caudal en función de su ubicación a

lo largo del cauce. Además, las tres CB poseen condición de borde de altura normal, definiendo el parámetro

de pendiente normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00||✅||0.68|0.008|
|US_01|✅|||1.84|0.04|
|US_02||✅||0.18|0.1|
|US_03|✅|||0.47|0.1|
|US_04|✅|||0.46|0.08|
|DS|||✅|--|0.2|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.02 MODELO HIDRÁULICO PE_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.02 MODELO HIDRÁULICO PE_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas y 50 min para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.02 MODELO HIDRÁULICO PE_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.02 MODELO HIDRÁULICO PE_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.03. MODELO HIDRÁULICO PE_03 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|EPC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.03|**Rev. A**|

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 3-2. Ubicación condiciones de borde ................................................................................................................. 3

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 4

Figura 4-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 4-2. Velocidad máxima para la crecida con periodo de retorno 100 años ................................................. 6

Figura 4-2. Hidrograma a la salida del modelo mostrando régimen permanente .............................................. 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_03, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.02|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0|
|Variación de las secciones transversales|Graduales|n2|0|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.02|
|Sinuosidad y frecuencia de meandros|Leve|m|1|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|DS|||✅|--|0.1|
|US_00||✅||0.16|0.08|
|US_01||✅||0.17|0.08|
|US_02|✅|||0.36|0.1|
|US_03|✅|||0.36|0.1|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por un periodo de 2 horas más, sumando en total 3 horas de simulación.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 4 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.03. MODELO HIDRÁULICO PE_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.04 MODELO HIDRÁULICO PE_04 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|EPC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.04|**Rev. A**|

ANEXO 2.01.04 MODELO HIDRÁULICO PE_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 3-2. Ubicación condiciones de borde ................................................................................................................. 2

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 3

Figura 4-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 4-2. Velocidad máxima para la crecida con periodo de retorno 100 años ................................................. 4

Figura 4-2. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 5

# Tablas

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ....................... 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.04 MODELO HIDRÁULICO PE_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_04, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.02|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0|
|Variación de las secciones transversales|Graduales|n2|0|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.02|
|Sinuosidad y frecuencia de meandros|Leve|m|1|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.04 MODELO HIDRÁULICO PE_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|DS|||✅|--|0.06|
|US_00||✅||0.08|0.06|
|US_01|✅|||1.88|0.055|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.04 MODELO HIDRÁULICO PE_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por un periodo de 2 horas más, sumando en total 3 horas de simulación.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.04 MODELO HIDRÁULICO PE_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.04 MODELO HIDRÁULICO PE_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.05 MODELO HIDRÁULICO PE_05 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BAS|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.05|**Rev. A**|

ANEXO 2.01.05 MODELO HIDRÁULICO PE_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 3-2. Ubicación condiciones de borde ................................................................................................................. 2

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 3

Figura 4-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 4-2. Velocidad máxima para la crecida con periodo de retorno 100 años ................................................. 4

Figura 4-2. Hidrograma a la salida del modelo mostrando régimen permanente .............................................. 5

# Tablas

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ....................... 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.05 MODELO HIDRÁULICO PE_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_05, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.05 MODELO HIDRÁULICO PE_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_02|✅|||1.29|0.08|
|US_01||✅||0.70|0.07|
|US_00||✅||0.36|0.11|
|DS|||✅|-|0.14|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.05 MODELO HIDRÁULICO PE_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora 50 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.05 MODELO HIDRÁULICO PE_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.05 MODELO HIDRÁULICO PE_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06

ESTUDIO DE INUNDACIÓN

PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|JCP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.06|**Rev. A**|

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**Contenidos**

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

**Figuras**

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 6

**Tablas**

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**1.** **Introducción**

Se construyó el modelo hidráulico denominado PE_06, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

**2.** **Parámetros de entrada**

**2.1.** **Coeficiente de rugosidad**

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Despreciable|n3|0.000|
|Densidad de vegetación|Media|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

1 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**2.2.** **Condiciones de borde e iniciales**

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.37|0.058|
|DS||✅|-|0.022|

2 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

**2.3.** **Otras consideraciones**

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

**3.** **Resultados**

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.06. MODELO HIDRÁULICO PE_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**4.** **Referencias**

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.07 MODELO HIDRÁULICO PE_07 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ASP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.07|**Rev. A**|

ANEXO 2.01.07 MODELO HIDRÁULICO PE_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ........................................................................................................ 2

2.3. Otras consideraciones ......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde ......................................................................................................................3

Figura 2-2. Hidrogramas de entrada .................................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ................................................5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años ....................................................5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................. 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ...................................................................................................................... 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.07 MODELO HIDRÁULICO PE_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_07, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.07 MODELO HIDRÁULICO PE_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||0.50|0.0967|
|US_01||✅||0.22|0.0814|
|US_02||✅||0.14|0.5090|
|DS|||✅|--|0.0540|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.07 MODELO HIDRÁULICO PE_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.07 MODELO HIDRÁULICO PE_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas y 50 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.07 MODELO HIDRÁULICO PE_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.07 MODELO HIDRÁULICO PE_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.08 MODELO HIDRÁULICO PE_08 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DPP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.08|**Rev. A**|

ANEXO 2.01.08 MODELO HIDRÁULICO PE_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 3-2. Ubicación condiciones de borde ................................................................................................................. 2

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 3

Figura 4-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 4-2. Velocidad máxima para la crecida con periodo de retorno 100 años ................................................. 4

Figura 4-2. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 4

# Tablas

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ....................... 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.08 MODELO HIDRÁULICO PE_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_08, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Grava fina|n0|0.024|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.011|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.08 MODELO HIDRÁULICO PE_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00||✅||0.31|0.05|
|US_01||✅||0.32|0.08|
|US_02|✅|||0.36|0.09|
|US_03|✅|||1.46|0.06|
|DS|||✅|-|0.08|

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.08 MODELO HIDRÁULICO PE_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes, a lo más, por un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas 30 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.08 MODELO HIDRÁULICO PE_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.08 MODELO HIDRÁULICO PE_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09

ESTUDIO DE INUNDACIÓN

PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|JCP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.09|**Rev. A**|

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**Contenidos**

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

**Figuras**

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 7

**Tablas**

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**1.** **Introducción**

Se construyó el modelo hidráulico denominado PE_09, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

**2.** **Parámetros de entrada**

**2.1.** **Coeficiente de rugosidad**

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alterándose ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.045**|

1 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**2.2.** **Condiciones de borde e iniciales**

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US|✅||0.9|0.05|
|DS||✅||0.01|

2 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

**2.3.** **Otras consideraciones**

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora 50 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

**3.** **Resultados**

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.09. MODELO HIDRÁULICO PE_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

**4.** **Referencias**

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.10. MODELO HIDRÁULICO PE_10 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BAS|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.10|**Rev. A**|

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_10, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Despreciable|n3|0.005|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||0.53|0.07|
|US_01|✅|||0.11|0.38|
|DS|||✅|-|0.10|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.10. MODELO HIDRÁULICO PE_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11

ESTUDIO DE INUNDACIÓN

PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|JCP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.11|**Rev. A**|

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**Contenidos**

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

**Figuras**

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

**Tablas**

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**1.** **Introducción**

Se construyó el modelo hidráulico denominado PE_11, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

**2.** **Parámetros de entrada**

**2.1.** **Coeficiente de rugosidad**

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

1 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**2.2.** **Condiciones de borde e iniciales**

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y final o aguas abajo. La CB de

aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.18|0.31|
|DS||✅|-|0.16|

2 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

**2.3.** **Otras consideraciones**

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

**3.** **Resultados**

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.11. MODELO HIDRÁULICO PE_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**4.** **Referencias**

HEC. (2022). HEC-RAS. Versión 6.2. Hydrologic Engineering Center. Obtenido de
https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.12 MODELO HIDRÁULICO PE_12 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ENC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.12|**Rev. A**|

ANEXO 2.01.12 MODELO HIDRÁULICO PE_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 4

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.12 MODELO HIDRÁULICO PE_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_12, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.12 MODELO HIDRÁULICO PE_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las tres CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.28|0.30|
|DS||✅|-|0.35|

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.12 MODELO HIDRÁULICO PE_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.12 MODELO HIDRÁULICO PE_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.12 MODELO HIDRÁULICO PE_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.13 MODELO HIDRÁULICO PE_13 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DPP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.13|**Rev. A**|

ANEXO 2.01.13 MODELO HIDRÁULICO PE_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 4

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.13 MODELO HIDRÁULICO PE_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_13, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Grava gruesa|n0|0.028|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.058**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.13 MODELO HIDRÁULICO PE_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||3.94|0.05|
|US_01|✅|||18.46|0.04|
|US_02||✅||0.21|0.10|
|US_03|✅|||0.61|0.29|
|DS|||✅|-|0.02|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.13 MODELO HIDRÁULICO PE_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.13 MODELO HIDRÁULICO PE_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.13 MODELO HIDRÁULICO PE_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.14 MODELO HIDRÁULICO PE_14 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BJG|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.14|**Rev. A**|

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_14, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00||✅||0.06|0.28|
|US_01|✅|||0.27|0.31|
|US_02|✅|||0.1|0.38|
|DS|||✅|--|0.24|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas y 15 min para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.14 MODELO HIDRÁULICO PE_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.15 MODELO HIDRÁULICO PE_15 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DMM|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.15|**Rev. A**|

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 7

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_15, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Roca cortada|n0|0.025|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

En resumen, las CB aguas arriba incluyen parámetros de caudal en función de su ubicación a lo largo del

cauce. Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.51|0.124|
|US_01|✅||0.14|0.331|
|DS||✅|-|0.098|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por un periodo de 2 horas más.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.15 MODELO HIDRÁULICO PE_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.16 MODELO HIDRÁULICO PE_16 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|CJS|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.16|**Rev. A**|

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 5**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ....................... 2

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_16, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose<br>Ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.46|0.242|
|US_01|✅||0.28|0.238|
|DS||✅|--|0.065|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.16 MODELO HIDRÁULICO PE_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.17 MODELO HIDRÁULICO PE_17 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ASP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.17|**Rev. A**|

ANEXO 2.01.17 MODELO HIDRÁULICO PE_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ........................................................................................................ 2

2.3. Otras consideraciones .......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 2-1. Ubicación condiciones de borde ...................................................................................................................... 2

Figura 2-2. Hidrogramas de entrada ...................................................................................................................................3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................... 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años ................................................... 4

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ..................................................5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ...................................................................................................................... 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.17 MODELO HIDRÁULICO PE_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_17, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.005|
|Densidad de vegetación|Media|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.17 MODELO HIDRÁULICO PE_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||1.18|0.06|
|DS||✅|--|0.08|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.17 MODELO HIDRÁULICO PE_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 11 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.17 MODELO HIDRÁULICO PE_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.17 MODELO HIDRÁULICO PE_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18

# ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BAS|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.18|**Rev. A**|

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 7

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_18, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Despreciable|n3|0.000|
|Densidad de vegetación|Media|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) y final o aguas abajo. La

CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés, y se incluye la CB

aguas abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US|✅||0.26|0.25|
|DS||✅|-|0.21|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.18. MODELO HIDRÁULICO PE_18
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.19 MODELO HIDRÁULICO PE_19 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ENC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.19|**Rev. A**|

ANEXO 2.01.19 MODELO HIDRÁULICO PE_19
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.19 MODELO HIDRÁULICO PE_19
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_19, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.19 MODELO HIDRÁULICO PE_19
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las tres CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.41|0.07|
|DS||✅|-|0.08|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.19 MODELO HIDRÁULICO PE_19
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.19 MODELO HIDRÁULICO PE_19
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.19 MODELO HIDRÁULICO PE_19
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.19 MODELO HIDRÁULICO PE_19
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.20 MODELO HIDRÁULICO PE_20 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BJG|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.20|**Rev. A**|

ANEXO 2.01.20 MODELO HIDRÁULICO PE_20
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrograma de entrada ............................................................................................................................... 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 4

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.20 MODELO HIDRÁULICO PE_20
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_20, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.20 MODELO HIDRÁULICO PE_20
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.86|0.008|
|DS||✅|--|0.2|

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.20 MODELO HIDRÁULICO PE_20
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrograma de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.20 MODELO HIDRÁULICO PE_20
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.20 MODELO HIDRÁULICO PE_20
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.01.21 MODELO HIDRÁULICO PE_21 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DPP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.01.21|**Rev. A**|

ANEXO 2.01.21 MODELO HIDRÁULICO PE_21
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.21 MODELO HIDRÁULICO PE_21
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado PE_21, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.21 MODELO HIDRÁULICO PE_21
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||2.66|0.08|
|DS||✅|-|0.04|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.21 MODELO HIDRÁULICO PE_21
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora 40 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.01.21 MODELO HIDRÁULICO PE_21
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.21 MODELO HIDRÁULICO PE_21
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.01.21 MODELO HIDRÁULICO PE_21
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ENC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.01|**Rev. A**|

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_01, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Grava fina|n0|0.024|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.054**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||2.99|0.04|
|US_01|✅||2.39|0.07|
|DS||✅|-|0.03|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por un periodo de a lo más 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 50 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.01 MODELO HIDRÁULICO LAT_01
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ENC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.02|**Rev. A**|

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_02, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Grava fina|n0|0.024|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.054**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||10.51|0.03|
|US_01|✅||0.21|0.30|
|DS||✅|-|0.10|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por un periodo de a lo más 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.02 MODELO HIDRÁULICO LAT_02
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ENC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.03|**Rev. A**|

ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_03, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.055**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00||✅||0.025|0.1|
|US_01||✅||0.304|0.3|
|US_02||✅||0.067|0.15|
|US_03A|✅|||0.069|0.3|
|US_03B|✅|||0.111|0.3|
|US_04|✅|||1.688|0.05|
|US_05|✅|||0.121|0.4|
|US_06|✅|||0.109|0.4|
|DS|||✅|-|0.2|

Nótese que las CB US_03A y US_03B pertenecen a una única cuenca del Anexo 01.02.03 delimitada bajo la

confluencia de las dos quebradas, pero, para efectos del modelo, el caudal resultante se subdividió de forma

proporcional respecto al área de cada subcuenca.

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por un periodo de a lo más 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.03 MODELO HIDRÁULICO LAT_03
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|ENC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.04|**Rev. A**|

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 7

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_04, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose Ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.054**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||0.18|0.30|
|US_01|✅||0.14|0.06|
|DS||✅|-|0.20|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por un periodo de a lo más 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.04 MODELO HIDRÁULICO LAT_04
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05

ESTUDIO DE INUNDACIÓN

PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|JCP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.05|**Rev. A**|

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**Contenidos**

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

**Figuras**

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 6

**Tablas**

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**1.** **Introducción**

Se construyó el modelo hidráulico denominado LAT_05, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

**2.** **Parámetros de entrada**

**2.1.** **Coeficiente de rugosidad**

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

1 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**2.2.** **Condiciones de borde e iniciales**

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_01|✅|||38.78|0.18|
|US_02|✅|||3.16|0.12|
|US_03||✅||0.19|0.076|
|US_00||✅||1.15|0.008|
|DS|||✅|-|0.013|

2 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

**2.3.** **Otras consideraciones**

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas 50 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

**3.** **Resultados**

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.05. MODELO HIDRÁULICO LAT_05
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**4.** **Referencias**

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.02.06 MODELO HIDRÁULICO LAT_06

ESTUDIO DE INUNDACIÓN

PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|EPC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.06|**Rev. A**|

ANEXO 2.02.06 MODELO HIDRÁULICO LAT_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**Contenidos**

2.1. Coeficiente de rugosidad ......................................................................................................................................... 1
2.2. Condiciones de borde e iniciales ............................................................................................................................ 2

2.3. Otras consideraciones ............................................................................................................................................. 3

**Figuras**

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 4

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 5

**Tablas**

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.06 MODELO HIDRÁULICO LAT_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**1.** **Introducción**

Se construyó el modelo hidráulico denominado LAT_06, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

**2.** **Parámetros de entrada**

**2.1.** **Coeficiente de rugosidad**

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.02|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.003|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.01|
|Densidad de vegetación|Media|n4|0.02|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.053**|

1 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.06 MODELO HIDRÁULICO LAT_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**2.2.** **Condiciones de borde e iniciales**

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||13.33|0.053|
|US_01|✅|||2.19|0.052|
|DS|||✅|--|0.053|

Figura 2-1. Ubicación condiciones de borde

2 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.06 MODELO HIDRÁULICO LAT_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

**2.3.** **Otras consideraciones**

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

**3.** **Resultados**

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.06 MODELO HIDRÁULICO LAT_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.06 MODELO HIDRÁULICO LAT_06
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

**4.** **Referencias**

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07

ESTUDIO DE INUNDACIÓN

PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|EPC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.07|**Rev. A**|

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**Contenidos**

2.1. Coeficiente de rugosidad ......................................................................................................................................... 1
2.2. Condiciones de borde e iniciales ............................................................................................................................ 2

2.3. Otras consideraciones ............................................................................................................................................. 3

**Figuras**

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 5

**Tablas**

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**1.** **Introducción**

Se construyó el modelo hidráulico denominado LAT_07, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

**2.** **Parámetros de entrada**

**2.1.** **Coeficiente de rugosidad**

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.002|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.052**|

1 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**2.2.** **Condiciones de borde e iniciales**

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||38.94|0.052|
|DS|||✅|--|0.052|

Figura 2-1. Ubicación condiciones de borde

2 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

**2.3.** **Otras consideraciones**

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

**3.** **Resultados**

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.07 MODELO HIDRÁULICO LAT_07
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

**4.** **Referencias**

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BAS|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.08|**Rev. A**|

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_08, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US|✅||1.79|0.35|
|DS||✅|-|0.17|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.08. MODELO HIDRÁULICO LAT_08
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DPP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.09|**Rev. A**|

ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_09, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00||✅||0.38|0.13|
|US_01|✅|||5.33|0.05|
|DS|||✅|-|0.04|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas 30 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.09 MODELO HIDRÁULICO LAT_09
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DPP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.10|**Rev. A**|

ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_10, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.045**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||6.06|0.06|
|DS||✅|-|0.03|

Figura 2-1. Ubicación condiciones de borde
## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora 40 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.10 MODELO HIDRÁULICO LAT_10
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.11 MODELO HIDRÁULICO LAT_11 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DPP|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.11|**Rev. A**|

ANEXO 2.02.11 MODELO HIDRÁULICO LAT_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones.......................................................................................................................... 3

**3.** **Resultados ....................................................................................................................... 3**

**4.** **Referencias ...................................................................................................................... 5**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 4

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.11 MODELO HIDRÁULICO LAT_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_11, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Grava fina|n0|0.024|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.020|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.054**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.11 MODELO HIDRÁULICO LAT_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||193.68|0.015|
|DS||✅|-|0.010|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.11 MODELO HIDRÁULICO LAT_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora 40 minutos para que el flujo entrara en

régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.11 MODELO HIDRÁULICO LAT_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.11 MODELO HIDRÁULICO LAT_11
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

5 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12

# ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|BAS|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.12|**Rev. A**|

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 7

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_12, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.015|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.050**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) y final o aguas abajo. La

CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés, y se incluye la CB

aguas abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_RIGHT|✅||2.84|0.19|
|US_LEFT|✅||1.89|0.29|
|DS||✅|-|0.06|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.12. MODELO HIDRÁULICO LAT_12
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|EPC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.13|**Rev. A**|

ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

2.1. Coeficiente de rugosidad ......................................................................................................................................... 1
2.2. Condiciones de borde e iniciales ............................................................................................................................ 2

2.3. Otras consideraciones ............................................................................................................................................. 3

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_13, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.014|
|Densidad de vegetación|Media|n4|0.014|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.048**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||1.46|0.048|
|DS|||✅|--|0.048|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.13 MODELO HIDRÁULICO LAT_13
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|EPC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.14|**Rev. A**|

ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

2.1. Coeficiente de rugosidad .................................................................................................................................. 1

2.2. Condiciones de borde e iniciales ...................................................................................................................... 2

2.3. Otras consideraciones ...................................................................................................................................... 3

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 2

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 3

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 4

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ............................................... 5

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_14, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.013|
|Densidad de vegetación|Media|n4|0.014|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.047**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅|||1.04|0.047|
|DS|||✅|--|0.047|

Figura 2-1. Ubicación condiciones de borde

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

# 3 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.14 MODELO HIDRÁULICO LAT_14
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|DMM|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.15|**Rev. A**|

ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 6**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrograma de entrada ............................................................................................................................... 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 5

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_15, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.013|
|Densidad de vegetación|Media|n4|0.014|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.047**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las dos CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente

normal a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100

años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US|✅||0.23|0.020|
|DS||✅|-|0.066|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrograma de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.15 MODELO HIDRÁULICO LAT_15
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

6 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|CJS|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.16|**Rev. A**|

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 5**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ....................... 2

Tabla 2-2. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_16, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Alternándose<br>Ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.012|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.052**|

## 2.2. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales corresponden al periodo de retorno de 100 años. Un

resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||1.91|0.126|
|DS||✅|--|0.037|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.16 MODELO HIDRÁULICO LAT_16
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. Obtenido de https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Ministerio de Obras Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17 ESTUDIO DE INUNDACIÓN PARQUE EÓLICO EL GUANACO

para FREEPOWER GROUP

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|13/07/2022|Cliente|IDC|BGP|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comunas de Constitución, Empedrado y San Javier<br>Región del Maule|Col3|
|---|---|---|
||FPG-B21048-EHID2-DOC-02.02.17|**Rev. A**|

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# Contenidos

**1.** **Introducción ..................................................................................................................... 1**

**2.** **Parámetros de entrada .................................................................................................... 1**

2.1. Coeficiente de rugosidad .................................................................................................................... 1
2.2. Condiciones de borde e iniciales ....................................................................................................... 2

2.3. Otras consideraciones......................................................................................................................... 4

**3.** **Resultados ....................................................................................................................... 4**

**4.** **Referencias ...................................................................................................................... 7**

# Figuras

Figura 2-1. Ubicación condiciones de borde.................................................................................................................. 3

Figura 2-2. Hidrogramas de entrada ............................................................................................................................. 4

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años ............................................. 5

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años.................................................. 6

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente ................................................ 6

# Tablas

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan. ........................ 1

Tabla 2-3. Condiciones de borde e iniciales. ................................................................................................................. 2

ii BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 1. Introducción

Se construyó el modelo hidráulico denominado LAT_17, empleando para ello el software HEC-RAS (HEC,

2022). El objetivo del modelo es representar la condición actual de cada cauce mediante el cálculo de flujo

bidimensional.

Los resultados entregados por el software permiten conocer las características del eje hidráulico y las áreas

de inundación. A continuación, se presentan las consideraciones para elaborar los modelos y los principales

resultados obtenidos.

# 2. Parámetros de entrada

## 2.1. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método Cowan (MOP, 2022):

# n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

# n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado n 2 : Coeficiente asociado a la variación de las secciones transversales

n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 2-1 muestra la condición del cauce según los criterios del método:

Tabla 2-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Gradual|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.018|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|**Coeficiente de rugosidad**|**Coeficiente de rugosidad**|n|**0.053**|

# 1 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

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

retorno de 100 años. Un resumen de las CB y su ubicación se presenta en la Tabla 2-2 y Figura 2-1:

Tabla 2-2. Condiciones de borde e iniciales.

|Nombre CB|CB aguas<br>arriba|CB<br>interm.|CB aguas<br>abajo|Caudal<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00||✅||0.21|0.15|
|US_01|✅|||0.21|0.20|
|US_02|✅|||0.08|0.13|
|DS|||✅|-|0.13|

## 2 BAQUA Ingeniería

www.baqua.cl

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-1. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora, y

permanecen constantes por, a lo más, un periodo de 2 horas.

La forma de los hidrogramas de entrada utilizados para los modelos se muestra a continuación:

3 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 2-2. Hidrogramas de entrada

## 2.3. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.2). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

# 3. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

4 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-1. Profundidad máxima para la crecida con periodo de retorno 100 años

5 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

Figura 3-2. Velocidad máxima para la crecida con periodo de retorno 100 años

Figura 3-3. Hidrograma a la salida del modelo mostrando régimen permanente

6 BAQUA Ingeniería
www.baqua.cl

ANEXO 2.02.17 MODELO HIDRÁULICO LAT_17
ESTUDIO DE INUNDACIÓN
PARQUE EÓLICO EL GUANACO

# 4. Referencias

HEC. (2022). HEC-RAS. Versión 6.2. HEC-RAS. Versión 6.2. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2022). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

7 BAQUA Ingeniería
www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1.: Condición del cauce para el cálculo del coeficiente de Manning con método Cowan.**

| Condición del cauce | Col2 | Símbolo | Valor |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad del perímetro mojado | Leve | n1 | 0.005 |
| Variación de las secciones transversales | Gradual | n2 | 0.000 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.010 |
| Densidad de vegetación | Media | n4 | 0.018 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| **Coeficiente de rugosidad** | **Coeficiente de rugosidad** | n | **0.053** |

**Tabla 2-2.: Condiciones de borde e iniciales.**

| Nombre CB | CB aguas<br>arriba | CB<br>interm. | CB aguas<br>abajo | Caudal<br>[m3/s] | Pendiente<br>[m/m] |
| --- | --- | --- | --- | --- | --- |
| US_00 |  | ✅ |  | 0.21 | 0.15 |
| US_01 | ✅ |  |  | 0.21 | 0.20 |
| US_02 | ✅ |  |  | 0.08 | 0.13 |
| DS |  |  | ✅ | - | 0.13 |
