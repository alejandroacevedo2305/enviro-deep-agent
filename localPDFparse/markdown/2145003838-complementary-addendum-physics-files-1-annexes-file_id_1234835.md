---
title: Sin título
author: Alarcon Gonzalez Richard (Codelco-DMH)
date: D:20200811120123-04'00'
language: es
type: general
pages: 26
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CORPORACIÓN NACIONAL DEL COBRE DE CHILE DIVISIÓN MINISTRO HALES
-->

# CORPORACIÓN NACIONAL DEL COBRE DE CHILE DIVISIÓN MINISTRO HALES

### GERENCIA DE RECURSOS MINEROS Y DESARROLLO RESULTADOS SIMULACIÓN CAÍDA DE BLOQUES DISEÑO DE BOTADERO DMH RAJO MINISTRO HALES 2020 SUPERINTENDENCIA DE GEOTECNIA

|Nombre|Cargo|Fecha|Firma|
|---|---|---|---|
|Rodrigo Álvarez de Araya A.|Ingeniero Geotécnico<br>Corto Plazo|Mayo 2020||
|Rodrigo Aguirre M.|Superintendente<br>Geotecnia (S)|Mayo 2020||

**Mayo 2020**

## ÍNDICE

**1** **INTRODUCCIÓN ............................................................................................... 3**

**2** **ESTIMACIÓN DE PARÁMETROS DE MATERIALES ............................................... 3**

**3** **SIMULACIONES DE CAÍDA DE BLOQUES SIN VELOCIDAD INICIAL ....................... 5**

**4** **SIMULACIONES DE CAÍDA DE BLOQUES CON VELOCIDAD INICIAL ..................... 5**

**5** **RESULTADOS GENERALES ................................................................................. 8**

**6** **CONCLUSIONES ................................................................................................ 8**

**ANEXO A.** **RESULTADOS SIMULACIONES DE CAÍDA DE BLOQUES SIN VELOCIDAD**

**INICIAL** **......................................................................................................... 9**

**ANEXO B.** **RESULTADOS SIMULACIONES DE CAÍDA DE BLOQUES CON VELOCIDAD**

**INICIAL** **....................................................................................................... 15**

2

## 1 INTRODUCCIÓN

En el marco de la tramitación de la DIA del proyecto “Aumento Movimientos Mina”, para la
aprobación del diseño del Botadero de Estéril, se realizaron simulaciones de caída de bloques y la
condición de riesgo que estos presentarían. Para lo cual se seleccionaron dos (2) perfiles que
representan las alturas máximas de botadero y la interacción con las rampas, las cuales
corresponden a las secciones P-Bot-02 y P-Bot-03 del análisis de estabilidad, destacados con
contorno rojo en Figura 1. Se utilizó la herramienta computacional RocFall V5.0 (Rocscience 2014).

#### P-Bot-01 P-Bot-04

Figura 1. Ubicación de los perfiles considerados en la simulación de caída de bloques.

## 2 ESTIMACIÓN DE PARÁMETROS DE MATERIALES

Para realizar la simulación de la caída de bloques, es relevante definir los parámetros que
condicionarán la respuesta de los bloques al interactuar con la superficie del talud. Para ello se
definen cuatro (parámetros): Restitución Normal; Restitución Tangencial; Fricción Dinámica; y
Resistencia al Rodado. Todos ellos controlarán la altura del rebote, la velocidad de desplazamiento,
entre otros, los que finalmente determinan la posición final del bloque.

La metodología utilizada para ajustar los valores de los parámetros antes mencionados (calibración),
consiste en utilizar las posiciones conocidas de los bloques alrededor del perfil P-Bot-03-Topo,
donde es conocida la posición final de los bloques y la geometría del talud. A continuación se
observan distintas combinaciones de valores, disponibles en la biblioteca de materiales del
programa RocFall, así como otros materiales utilizados en análisis anteriores de DMH. La siguiente

figura (ver Figura 2), muestra los distintos casos analizados, a partir de los cuales se revisa la
condición de bloques que se identifican en la pata del sector SW, asociado a la posición del perfil PBot-03-Topo. Los valores de los parámetros utilizados en los análisis se presentan en la siguiente
Tabla 1, de los cuales los seleccionados corresponden al material DMH02.

**P-Bot-03-Topo-70t-”Bedrock”**

**P-Bot-03-Topo-70t-”DMH01”**

**R** **N** **: 0,35**
**R** **T** **: 0,85**
 **D** **: 0,5**
**RR: 0,15**

**R** **N** **: 0,35**
**R** **T** **: 0,75**
 **D** **: 0,55**
**RR: 0,5**

**R** **N** **: 0,32**
**R** **T** **: 0,8**
 **D** **: 0,5**
**RR: 0,3**

**R** **N** **: 0,3**
**R** **T** **: 0,4**
 **D** **: 0,65**
**RR: 0,4**

**P-Bot-03-Topo-70t-”Talus”**

**P-Bot-03-Topo-70t-”DMH02”**

Figura 2. Resultados Calibración de Parámetros del Material para Simulación de Caída de Bloques.

Tabla 1. Parámetros Utilizados en Proceso de Calibración.

|Col1|“Bedrock”|“Talus”|DMH01|DMH02|
|---|---|---|---|---|
|Restitución<br>Normal (RN)|0,35|0,32|0,35|0,3|
|Restitución<br>Tangencial (RT)|0,85|0,8|0,75|0,4|
|Fricción<br>Direccional (D)|0,5|0,5|0,55|0,65|
|Resistencia<br>al<br>Rodado (RR)|0,15|0,3|0,5|0,4|

A continuación se entrega una breve descripción de los coeficientes utilizados en la configuración

de los análisis:

**Restitución Normal (R** **N** **):** Explica la relación entre las velocidades normales a la ladera antes y
después del impacto. Viene determinado por la rigidez de la superficie de la ladera, cuanto más
desfavorable sea el material, menor será su coeficiente de restitución normal.
**Restitución Tangencial (R** **T** **):** Explica la relación entre las velocidades paralelas a la ladera antes y
después del impacto. La vegetación y en menor grado, el material de la ladera, influyen en el
coeficiente tangencial.
**Fricción Dinámica (**  **D** **):** Depende del ángulo de fricción del material:  D =tan()
**Resistencia a la Rodadura (RR):** Este coeficiente representa la pérdida de energía, por otros factores

además de la fricción dinámica, como la deformación plástica, la histéresis y deslizamiento de la
superficie de contacto.

## 3 SIMULACIONES DE CAÍDA DE BLOQUES SIN VELOCIDAD INICIAL

Para evaluar los requerimientos de contención en el entorno del Botadero para el cierre de la
Operación se realiza la simulación de caída de bloques de tamaños de 1,5x1,5x1,5m [3], 2x2x2m [3], y
3x3x3m [3], lo que corresponde a pesos de 10t, 20t y 70t, respectivamente, el último corresponde al
tamaño máximo que podría ser cargado por los equipos disponibles en DMH.

La posición de los orígenes de los bloques simulados corresponden a los bordes de cada uno de los
pisos del botadero, de manera de identificar el riesgo de proyección de bloques hasta la base del
botadero y por otro lado, de ser necesario se debe identificar que la configuración del pretil
perimetral capaz de contener los bloques, el cual se considera con una configuración de 2m de altura
a 10m desde la pata.

En la siguiente figura se presentan los resultados de las simulaciones del perfil P-Bot-02 y P-Bot-03,
para los bloques de 70t (ver Figura 3), la totalidad de las simulaciones se entregan en Anexo A.

**P-Bot-02-70t** **P-Bot-03-70t**

Figura 3. Resultados Simulación de Caída de Bloques para Bloques de 70t. Las cruces representan los puntos

de inicio de la caída de los bloques y las líneas representan las trayectorias simuladas.

Los resultados obtenidos muestran que cada berma de 20m de ancho es capaz de contener el 100%
de los bloques proveniente de los pisos inmediatamente superiores, y para el piso inferior, la
proyección máxima de los bloques alcanza los 10m desde la pata del botadero, por lo que el pretil
podrá contener los bloques proyectados.

## 4 SIMULACIONES DE CAÍDA DE BLOQUES CON VELOCIDAD INICIAL

Para las simulaciones de caída de bloques en las dos secciones mencionadas en el capítulo anterior,
se consideran tres (3) tamaños de bloque, que van desde 1,5x1,5x1,5m [3] a 3x3x3m [3], este último
corresponde al tamaño máximo que podría ser cargado por los equipos disponibles en DMH.

Con el fin de representar la condición de vaciado se considera una velocidad inicial distinta de cero
en cada punto de origen de caída. Para estimar cuál es la velocidad del bloque al momento de salir

de la tolva del camión, se consideran las dimensiones 3 y 8, y el ángulo de vaciado, del CAEX
Caterpillar797F, ver Figura 4.

3Longitud Interior de la tolva: 9,976m
8Espacio Libre de Descarga: 2,017m
Ángulo de Elevación de tolva: 45°

Figura 4. Dimensiones Consideradas de CAEX Cat 797F. (Catálogo Camión Minero 797F).

Para estimar la velocidad inicial del bloque, al salir de la tolva del camión, se considera que el bloque
recorre toda la longitud interior de la tolva (~10m), con la inclinación de 45° que alcanza la tolva al
ser levantada, no se considera la interacción con el resto del material. A partir de las consideraciones
anteriores, utilizando las ecuaciones de movimiento a través de un plano inclinado se logra calcular
que el bloque deja el camión a ~21,8m/s; con esta velocidad, y considerando el ángulo de 45°, se
determina que las componentes verticales y horizontales son iguales, a saber velocidad horizontal
V H =15,4m/s y velocidad vertical V V =-15,4m/s. Esta condición es conservadora, ya que se asume la
máxima trayectoria dentro de la tolva, y se desprecia la interacción con el resto del material, lo que
reduciría la velocidad del bloque.

Además de la velocidad horizontal y vertical, el programa RocFall permite definir la velocidad
rotacional del bloque, expresada en grados por segundo (°/s), la que dado el comportamiento del
material no debería ser muy alta. Para estimar este valor, se considera que el bloque logra dar un
giro completo en unos 5s, por lo que se utiliza inicialmente una velocidad rotacional de 75°/s.

El origen de los bloques cayendo directamente desde el camión a la ladera del talud del botadero,
es la situación más conservadora para el vaciado, condición representada en las simulaciones como
caída desde el **borde** . Por otro lado, considerando que en todo el perímetro del botadero existe un
pretil de contorno de al menos 2m de altura, que al tener ángulo de reposo por ambos lados, se
obtiene que el pretil tendría al menos 5,3m de ancho en su base, se simula otra condición de vaciado
denominada **interior**, en la que el bloque cae a 1,5m desde la cresta hacia la plataforma. Los
resultados de las simulaciones para los perfiles considerados se presentan en el Anexo B, y a
continuación, en Figura 5, se muestran los resultados del perfil P-Bot-02, para el caso de caída desde

el borde:

Op-P-Bot-02-70t-borde Op-P-Bot-02-20t-borde

Op-P-Bot-02-10t-borde

Figura 5. Resultados Simulación de caída de bloques perfil P-Bot-02. Las cruces representan los

puntos de inicio de la caída de los bloques y las líneas representan las trayectorias simuladas.

Para evaluar el efecto de esta componente de velocidad se realizan simulaciones de caída de
bloques considerando velocidades de 0°/s, 75°/s, 180°/s, y 360°/s, los cuales se muestran a
continuación, en Figura 6.

**Op-P-Bot-02-70t-borde-**
**0m/s**

**Op-P-Bot-02-70t-borde-**
**180m/s**

**Op-P-Bot-02-70t-borde-**
**75m/s**

**Op-P-Bot-02-70t-borde-**
**360m/s**

Figura 6. Resultados Simulación de caída de bloques a distintas velocidades rotacionales. Perfil P
Bot-02. Las cruces representan los puntos de inicio de la caída de los bloques y las líneas

representan las trayectorias simuladas.

Los resultados de las simulaciones presentadas en Figura 6, muestran que la velocidad rotacional no
afecta la trayectoria, por lo que los valores de velocidad más relevantes están en la componente
vertical y horizontal. Sin embargo, al considerar una velocidad inicial del bloque, las bermas
contienen el 100% de los bloques simulados, por lo que al nivel inferior sólo se proyectan los bloques
desprendidos desde la primera plataforma.

## 5 RESULTADOS GENERALES

Para los distintos casos analizados, entregados en Anexo B, la distancia máxima de proyección en el
nivel inferior alcanza aproximadamente 23m, en los casos sin pretil de contención. Al incluir el pretil
inferior (Anexos A.2; A.4; B.2; B.4; B.6; y B.8), con 2m de altura y ubicado a 10m de la pata del
botadero, se logran contener el 100% de los bloques simulados en la condición de velocidad inicial
0m/s. Por otro lado, para el caso de velocidad inicial distinta de 0m/s, se contienen ~1.199 de los
1.2000 bloques simulados, ya que sólo 1 bloque, para el caso de 20t, sobrepasó el pretil del perfil PBot-03-20t-borde-pretil, por lo que la contención bordearía el 99,9% de los bloques simulados.

## 6 CONCLUSIONES

Se observa que tanto en las simulaciones sin velocidad inicial como en los caso con velocidad inicial,
las bermas, de 20m de ancho, consideradas en la configuración propuesta para el Botadero,
permiten contener el 100% de los bloques simulados, para los distintos tamaños.

La configuración propuesta del pretil en el perímetro del botadero permite contener al menos el
99% de los bloques que caen en ese nivel, siendo esta una excepción para el caso de bloques de 20t,
que caen desde el borde con velocidad inicial. Todos los otros casos para este tamaño de bloques y
para los demás tamaños (70t y 10t), la contención alcanza el 100%.

Sobre la base de los resultados se puede concluir que durante la operación, la condición crítica se
presenta al momento de vaciar sobre los pisos superiores, por lo que se debe mantener de forma
estricta la restricción definida en los procedimientos internos, de no realizar trabajos simultáneos
en dos niveles en una misma línea vertical.

## ANEXO A. RESULTADOS SIMULACIONES DE CAÍDA DE BLOQUES SIN VELOCIDAD INICIAL

**A.1** **SIMULACIONES PERFIL P-Bot-02**

**P-Bot-02-70t**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**P-Bot-02-20t**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**P-Bot-02-10t**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**A.2** **SIMULACIONES PERFIL P-Bot-02 CON PRETIL INFERIOR**

**P-Bot-02-70t-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**P-Bot-02-20t-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**P-Bot-02-10t-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**A.3** **SIMULACIONES PERFIL P-Bot-03**

**P-Bot-03-70t**

**P-Bot-03-20t**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**P-Bot-03-10t**

**A.4** **SIMULACIONES PERFIL P-Bot-03 CON PRETIL INFERIOR**

**P-Bot-03-70t-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**P-Bot-03-20t-pretil**

**P-Bot-03-10t-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

## ANEXO B. RESULTADOS SIMULACIONES DE CAÍDA DE BLOQUES CON VELOCIDAD INICIAL

**B.1** **SIMULACIONES PERFIL P-Bot-02 CAÍDA DESDE BORDE**

**Op-P-Bot-02-70t-borde**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-20t-borde**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-10t-borde**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**B.2** **SIMULACIONES PERFIL P-Bot-02 CAÍDA DESDE BORDE, CON PRETIL INFERIOR**

**Op-P-Bot-02-70t-borde-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-20t-borde-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-10t-borde-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**B.3** **SIMULACIONES PERFIL P-Bot-03 CAÍDA DESDE BORDE**

**Op-P-Bot-03-70t-borde**

**Op-P-Bot-03-20t-borde**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-03-10t-borde**

**B.4** **SIMULACIONES PERFIL P-Bot-03 CAÍDA DESDE BORDE, CON PRETIL INFERIOR**

**Op-P-Bot-03-70t-borde-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-03-20t-borde-pretil**

**Op-P-Bot-03-10t-borde-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**B.5** **SIMULACIONES PERFIL P-Bot-02 CAÍDA DESDE INTERIOR**

**Op-P-Bot-02-70t-int**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-20t-int**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-10t-int**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**B.6** **SIMULACIONES PERFIL P-Bot-02 CAÍDA DESDE INTERIOR, CON PRETIL INFERIOR**

**Op-P-Bot-02-70t-int-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-20t-int-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-02-10t-int-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**B.7** **SIMULACIONES PERFIL P-Bot-03 CAÍDA DESDE INTERIOR**

**Op-P-Bot-03-70t-int**

**Op-P-Bot-03-20t-int**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-03-10t-int**

**B.8** **SIMULACIONES PERFIL P-Bot-03 CAÍDA DESDE INTERIOR, CON PRETIL INFERIOR**

**Op-P-Bot-03-70t-int-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

**Op-P-Bot-03-20t-int-pretil**

**Op-P-Bot-03-10t-int-pretil**

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

P-Bot-01

P-Bot-04

P-Bot-02

P-Bot-03

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Parámetros Utilizados en Proceso de Calibración.**

| Col1 | “Bedrock” | “Talus” | DMH01 | DMH02 |
| --- | --- | --- | --- | --- |
| Restitución<br>Normal (RN) | 0,35 | 0,32 | 0,35 | 0,3 |
| Restitución<br>Tangencial (RT) | 0,85 | 0,8 | 0,75 | 0,4 |
| Fricción<br>Direccional (D) | 0,5 | 0,5 | 0,55 | 0,65 |
| Resistencia<br>al<br>Rodado (RR) | 0,15 | 0,3 | 0,5 | 0,4 |
