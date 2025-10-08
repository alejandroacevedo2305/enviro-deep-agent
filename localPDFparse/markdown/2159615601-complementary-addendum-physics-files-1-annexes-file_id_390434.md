---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: general
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
-->

## Adenda Complementaria de Declaración de Impacto Ambiental “Adecuación Cronograma y Obras Collahuasi” Anexo 1.8 Actualización modelación de flujo no saturado salar de Coposa

### Elaborado por: Junio, 2024

### Actualización modelación de flujo no saturado salar de Coposa

# Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi

Preparado para: Geobiota
Cliente final: Compañía Minera Doña Inés de Collahuasi
Código de documento: HIDRO.GEOB806.INF004.REV0
mayo, 2024

Actualización modelación de flujo no saturado salar de

Coposa

|Rev.|Id|Ejecutor|Revisor|Aprueba|Descripción|
|---|---|---|---|---|---|
|A|Nombre|R. Ordoñez|F. Varas|G. Sepúlveda|Revisión interna|
|A|Fecha|28.05.2024|28.05.2024|28.05.2024|28.05.2024|
|B|Nombre|R. Ordoñez|F. Varas|G. Sepúlveda|Revisión cliente|
|B|Fecha|29.05.2024|29.05.2024|29.05.2024|29.05.2024|
|0|Nombre|R. Ordoñez|F. Varas|G. Sepúlveda|Aprobado cliente|
|0|Fecha|30.05.2024|30.05.2024|30.05.2024|30.05.2024|

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0

Actualización modelación de flujo no saturado salar de

Coposa

**Índice de Contenido**

1. Introducción .................................................................................................................................................... 1

2. Propiedades del suelo .................................................................................................................................... 3

3. Profundidad del nivel freático Salar de Coposa .............................................................................................. 8

4. Modelos de flujo no saturado ........................................................................................................................ 12

5. Conclusiones ................................................................................................................................................ 23

6. Referencias ................................................................................................................................................... 24

**Listado Tablas**

Tabla 2-1: Coeficientes ajustados curvas características ................................................................................... 5

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Actualización modelación de flujo no saturado salar de Coposa -->

**Tabla 2-1: Coeficientes ajustados curvas características****

| Calicata | Muestra | θ (%, V/V)<br>s | θ (%, V/V)<br>r | α (1/cm) | n (-) | K Saturada (cm/día) |
| --- | --- | --- | --- | --- | --- | --- |
| C3 | C3H1 | 40,0 | 4,9 | 0,0381 | 1,13 | 165,7 |
| C3 | C3H2 | 42,0 | 4,6 | 0,1610 | 1,11 | 122,6 |
| C3 | C3H3 | 47,0 | 4,1 | 0,1870 | 1,08 | 57,5 |
| C4 | C4H1 | 44,0 | 4,9 | 0,1646 | 1,07 | 105,9 |
| C4 | C4H2 | 47,0 | 4,0 | 0,0104 | 1,13 | 62,5 |
| C4 | C4H3 | 54,0 | 7,2 | 0,0019 | 1,46 | 45,8 |
| C4 | C4H4 | 79,0 | 10,8 | 0,0007 | 2,11 | 568,9 |
| C4 | C4H5 | 55,0 | 4,8 | 0,0057 | 1,47 | 200,4 |
| C5 | C5H2 | 53,0 | 4,7 | 0,0111 | 1,27 | 83,6 |
| C5 | C5H3 | 49,0 | 8,2 | 0,0024 | 1,46 | 36,9 |
| C5 | C5H4 | 64,0 | 11,3 | 0,0014 | 1,76 | 108,0 |
| C5 | C5H5 | 69,0 | 11,3 | 0,0020 | 1,65 | 193,4 |
| C5 | C5H6 | 70,0 | 10,7 | 0,0022 | 1,81 | 275,3 |
| C6 | C6H1 | 58,0 | 6,7 | 0,0029 | 1,33 | 224,2 |
| C6 | C6H2 | 66,0 | 10,9 | 0,0019 | 1,57 | 284,0 |
| C6 | C6H3 | 72,0 | 12,0 | 0,0011 | 1,92 | 393,9 |
| C6 | C6H4 | 73,0 | 11,6 | 0,0023 | 1,61 | 444,3 |
| C6 | C6H5 | 69,0 | 11,0 | 0,0026 | 1,58 | 389,1 |
| C7 | C7H1 | 36,0 | 5,2 | 0,0076 | 1,31 | 8,4 |
| C7 | C7H2 | 38,0 | 5,3 | 1,3700 | 1,17 | 23,8 |
| C7 | C7H3 | 42,0 | 7,3 | 0,0122 | 1,24 | 9,5 |
| C7 | C7H4 | 39,0 | 4,4 | 0,0364 | 1,15 | 22,2 |
| C8 | C8H1 | 49,0 | 4,4 | 0,0365 | 1,12 | 99,9 |
| C8 | C8H2 | 49,0 | 4,1 | 0,2501 | 1,08 | 59,6 |
| C8 | C8H3 | 53,0 | 6,4 | 0,0059 | 1,25 | 44,9 |
| C8 | C8H4 | 45,0 | 5,9 | 0,0288 | 1,19 | 46,8 |
| C8 | C8H5 | 65,0 | 5,6 | 0,0093 | 1,64 | 187,4 |
| C8 | C8H6 | 56,0 | 4,3 | 0,0031 | 1,66 | 92,4 |
| C9 | C9H1 | 39,0 | 4,7 | 0,0098 | 1,70 | 17,9 |
| C9 | C9H2 | 33,0 | 4,8 | 0,0116 | 1,35 | 4,4 |
| C9 | C9H3 | 37,0 | 6,5 | 0,0145 | 1,29 | 3,5 |
| C10 | C10H1 | 37,0 | 5,0 | 0,0646 | 1,26 | 17,5 |
| C10 | C10H2 | 36,0 | 4,4 | 0,0584 | 1,36 | 34,0 |
| C10 | C10H4 | 38,0 | 4,4 | 0,1258 | 1,52 | 127,5 |
| C10 | C10H5 | 41,0 | 4,9 | 0,3235 | 1,47 | 153,4 |
| C11 | C11H1 | 32,0 | 3,4 | 0,0125 | 1,28 | 9,3 |
| C11 | C11H2 | 35,0 | 5,4 | 0,0562 | 1,18 | 7,5 |
| C11 | C11H3 | 38,0 | 5,4 | 2,3203 | 1,22 | 54,6 |
| C11 | C11H4 | 37,0 | 5,0 | 3,0096 | 1,21 | 97,7 |
| CC12 | CC12H1 | 45,0 | 5,4 | 0,0032 | 1,49 | 20,3 |
| CC12 | CC12H2 | 47,0 | 8,0 | 0,0019 | 1,60 | 14,5 |
| CC12 | CC12H3 | 45,0 | 7,5 | 0,0030 | 1,30 | 12,8 |
| CC12 | CC12H4 | 50,0 | 7,6 | 0,0045 | 1,25 | 24,3 |
| CC12 | CC12H5 | 55,0 | 8,1 | 0,0035 | 1,45 | 52,2 |
| CC12 | CC12H6 | 35,0 | 4,9 | 0,0058 | 1,29 | 23,3 |
| CC12 | CC12H7 | 63,0 | 7,5 | 0,0046 | 1,83 | 151,1 |
| CC13 | CC13H1 | 32,0 | 4,2 | 0,0572 | 1,36 | 29,7 |
| CC13 | CC13H2 | 36,0 | 4,8 | 0,0544 | 1,31 | 27,4 |
| CC13 | CC13H3 | 33,0 | 4,4 | 0,0479 | 1,33 | 22,8 |
| CC13 | CC13H4 | 51,0 | 5,3 | 0,0773 | 1,41 | 132,5 |
| CC14 | CC14H1 | 43,0 | 9,8 | 0,0073 | 1,39 | 8,8 |
| CC14 | CC14H2 | 60,0 | 10,0 | 0,0013 | 1,95 | 79,6 |
| CC14 | CC14H3 | 69,0 | 5,0 | 0,0134 | 1,45 | 217,9 |

<!-- Estadísticas: 53 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi HIDRO.GEOB806.INF004.REV0 5 Actualización modelación de flujo no saturado salar de -->
<!-- FIN TABLA 2-1 -->


Tabla 3-1: Puntos modelados, puntos de observación y profundidades desde la superficie de terreno por

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Actualización modelación de flujo no saturado salar de Coposa -->

**Tabla 3-1: Puntos modelados, puntos de observación y profundidades desde la superficie de****

| Calicata | Punto de<br>Observación | Escenario 1 (cm) -<br>Caso Base | Escenario 2 (cm) -<br>DIA |
| --- | --- | --- | --- |
| C3 | CMW-12 | 158 | 151 |
| C4 | CMW-05B | 233 | 226 |
| C5 | CPS-26 | 172 | 172 |
| C7 | CMW-02 | 233 | 200 |
| C6 | CMA-16 | 255 | 246 |
| C8 | CPMA-02 | 225 | 225 |
| C9 | CPMA-02 | 225 | 225 |
| C10 | CPMA-02 | 225 | 225 |
| C11 | CPS-35 | 142 | 140 |
| C12 | CPMA-02 | 225 | 225 |
| C13 | CPMA-02 | 225 | 225 |
| C14 | CPMA-02 | 225 | 225 |
| C15 | CMA-16 | 255 | 246 |
| C16 | CPS-54 | 210 | 208 |
| C17 | CWE-17 | 140 | 138 |
| C18 | CMW-29B | 63 | 54 |
| C19 | CMW-12 | 158 | 151 |
| C20 | CWE-21 | 95 | 92 |
| C21 | CMW-03 | 186 | 181 |
| C22 | CMW-06 | 137 | 132 |
| C24 | CWE-21 | 95 | 92 |

<!-- Estadísticas: 21 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi HIDRO.GEOB806.INF004.REV0 11 -->
<!-- FIN TABLA 3-1 -->


escenario .......................................................................................................................................................... 11

**Listado de Figuras**

Figura 1-1: Área de estudio ................................................................................................................................ 2

Figura 2-1: Ubicación calicatas con información de ensayos de succión ........................................................... 4

Figura 2-2: Ejemplo ajuste curvas de succión .................................................................................................... 7
Figura 3-1: Ubicación de puntos de observación ................................................................................................ 9

Figura 3-2: Ejemplo configuración de escenarios ............................................................................................. 10

Figura 4-1: Perfil de succión y humedad simulada en el suelo en calicata C3 ................................................. 13

Figura 4-2: Perfil de succión y humedad simulada en el suelo en calicata C4 ................................................. 13

Figura 4-3: Perfil de succión y humedad simulada en el suelo en calicata C5 ................................................. 14
Figura 4-4: Perfil de succión y humedad simulada en el suelo en calicata C6 ................................................. 14

Figura 4-5: Perfil de succión y humedad simulada en el suelo en calicata C7 ................................................. 15

Figura 4-6: Perfil de succión y humedad simulada en el suelo en calicata C8 ................................................. 15

Figura 4-7: Perfil de succión y humedad simulada en el suelo en calicata C9 ................................................. 16

Figura 4-8: Perfil de succión y humedad simulada en el suelo en calicata C10 ............................................... 16

Figura 4-9: Perfil de succión y humedad simulada en el suelo en calicata C11 ............................................... 17
Figura 4-10: Perfil de succión y humedad simulada en el suelo en calicata CC12 ........................................... 17

Figura 4-11: Perfil de succión y humedad simulada en el suelo en calicata CC13 ........................................... 18

Figura 4-12: Perfil de succión y humedad simulada en el suelo en calicata CC14 ........................................... 18

Figura 4-13: Perfil de succión y humedad simulada en el suelo en calicata CC15 ........................................... 19

Figura 4-14: Perfil de succión y humedad simulada en el suelo en calicata CC16 ........................................... 19
Figura 4-15: Perfil de succión y humedad simulada en el suelo en calicata CC17 ........................................... 20

Figura 4-16: Perfil de succión y humedad simulada en el suelo en calicata CC18 ........................................... 20

Figura 4-17: Perfil de succión y humedad simulada en el suelo en calicata CC19 ........................................... 21

Figura 4-18: Perfil de succión y humedad simulada en el suelo en calicata CC20 ........................................... 21

Figura 4-19: Perfil de succión y humedad simulada en el suelo en calicata CC21 ........................................... 22
Figura 4-20: Perfil de succión y humedad simulada en el suelo en calicata CC22 ........................................... 22

Figura 4-21: Perfil de succión y humedad simulada en el suelo en calicata CC24 ........................................... 23

iii

**Listado de Apéndices**

Apéndice 1: Ajuste curvas de succión
Apéndice 2: Herramientas numéricas

Actualización modelación de flujo no saturado salar de

Coposa

iv

Actualización modelación de flujo no saturado salar de

Coposa

**1.** **INTRODUCCIÓN**

En el marco de la Declaración de Impacto Ambiental (DIA) del proyecto “Adecuación Cronograma y obras
Collahuasi”, en adelante el “Proyecto”, cuyo Titular es Compañía Minera Doña Inés de Collahuasi S.C.M., en
adelante “CMDIC”, Hidroestudios ha desarrollado trabajos de apoyo en la preparación de los antecedentes
relativos a recursos hídricos y su relación con otras componentes ambientales. En este contexto, se ha solicitado
a Hidroestudios evaluar la evolución del perfil de humedad del suelo ante variaciones en el nivel freático en el
salar de Coposa en consistencia con las nuevas simulaciones del modelo numérico integrado presentadas en
la Adenda Complementaria.

El objetivo de este estudio es proveer información para la evaluación de efectos de la variación del nivel freático
en el salar de Coposa sobre los objetos de protección ambiental. Para cumplir con dicho objetivo se realizó una
modelación del comportamiento de la humedad del suelo no saturado, ubicado entre la napa y la superficie del
suelo (zona no saturada). La Figura 1-1 presenta el área de estudio.

El estudio consistió principalmente en: i) el análisis de la profundidad del nivel freático histórico y su
recuperación, para lo cual se utilizó, además de los datos medidos, el resultado del modelo numérico
hidrogeológico presentado en el marco de la evaluación ambiental y que ha sido validado y utilizado para las
simulaciones de acuerdo a lo indicado en el Anexo 1.2 “Actualización del modelo hidrogeológico conceptual y
numérico a diciembre de 2023” de esta Adenda Complementaria, ii) ajuste de las propiedades hidráulicas del
suelo no saturado en el salar de Coposa a partir de las muestras presentadas en Anexo 2.5 Caracterización
Ambiental de Suelos de la presente DIA y actualizado en el Estudio de Raíces (Anexo 12 de la Adenda) y iii)
modelación de flujo no saturado a través de Hydrus1D.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 1

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 1-1: Área de estudio**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 2

Actualización modelación de flujo no saturado salar de

Coposa

**2.** **PROPIEDADES DEL SUELO**

El agua subterránea asciende por capilaridad desde la napa y la extensión de esta zona húmeda depende de
las características del suelo. Se considera que la presión de agua es mayor que 0, relativo a la presión
atmosférica, en la zona saturada e igual a 0 en el nivel freático donde se encuentra en equilibrio con la presión
atmosférica. En el caso de la zona no saturada la presión es menor que cero, esto refleja el hecho de que el
agua es mantenida en los poros debido a tensiones o fuerzas superficiales en el suelo. Tanto el contenido de
humedad como la conductividad hidráulica son funciones no lineales de esta presión negativa o succión y su
relación se expresa en la denominada curva de retención. Existen una gran variedad de ecuaciones que
describen la forma de la curva de retención o curva característica del suelo siendo una de las más ampliamente
utilizada el modelo de Van Genuchten - Mualem (1980).

θ(h) = θ r + (1 + |αh|θ s −θ r [n] ) [m] [ para h< 0 (1)]

2

)

1

m
)

K(h) = K s S e [l] e
(1 −(1 −S

m

(2)

[1] n> 1 (3) y S e = [θ−θ] [r]

n [,] θ −θ

Con m= 1 − [1]

θ s −θ r

(4)

Donde

θ s : Contenido de humedad volumétrica saturada

θ r : Contenido de humedad volumétrica residual

h: Succión (presión negativa)
K: conductividad hidráulica no saturada

K s : Conductividad hidráulica saturada

α, n y l: coeficientes empíricos
S e : Saturación efectiva

Con el fin de contar con curvas características del suelo se cuenta con información de ensayos de succión para
las muestras tomadas en distintos estratos en calicatas excavadas en el salar de Coposa, información que se
presenta de manera detallada en el Anexo 2.5 Caracterización Ambiental de Suelos de la presente DIA y Anexo
12 de la Adenda. La Figura 2-1 muestra la ubicación de las calicatas utilizadas para la modelación de flujo no
saturado. Los resultados de dichas pruebas fueron parametrizados a partir del software RetC (Van Genuchten
et al, 1991), el cual permite ajustar los parámetros de la curva de succión a los datos medidos. Adicionalmente,
RetC cuenta con una gran base de datos que permite estimar algunos de estos parámetros en base a la
información de granulometría y densidad aparente del suelo. De esta forma los valores de los parámetros fueron
ajustados siguiendo los siguientes criterios:

 - El valor del contenido de humedad saturado se asume igual a la porosidad de las muestras (dato de
laboratorio).

 - Los valores del contenido de humedad residual y la permeabilidad hidráulica saturada fueron
adoptados de la predicción de RetC en base a la granulometría de las muestras.

 - Los coeficientes _α_ y _n_, fueron ajustados con el software RetC a partir de la información de las curvas
de succión disponibles.

 - El valor del coeficiente empírico _l_ de la curva de conductividad fue fijado en 0,5, de acuerdo con las
recomendaciones del propio programa y literatura especializada (Mualem, 1976).

La Tabla 2-1 muestra los coeficientes considerados y ajustados para cada uno de los ensayos de succión
disponibles, el detalle de los parámetros ajustados y las curvas se encuentra en el Apéndice 1. A modo de
ejemplo la Figura 2-2 muestras los ajustes conseguidos para la curva de succión del primer estrato de cada
calicata.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 3

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 2-1: Ubicación calicatas con información de ensayos de succión**

Fuente: Elaboración propia

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 4

Actualización modelación de flujo no saturado salar de

Coposa

**Tabla 2-1: Coeficientes ajustados curvas características**

|Calicata|Muestra|θ (%, V/V)<br>s|θ (%, V/V)<br>r|α (1/cm)|n (-)|K Saturada (cm/día)|
|---|---|---|---|---|---|---|
|C3|C3H1|40,0|4,9|0,0381|1,13|165,7|
|C3|C3H2|42,0|4,6|0,1610|1,11|122,6|
|C3|C3H3|47,0|4,1|0,1870|1,08|57,5|
|C4|C4H1|44,0|4,9|0,1646|1,07|105,9|
|C4|C4H2|47,0|4,0|0,0104|1,13|62,5|
|C4|C4H3|54,0|7,2|0,0019|1,46|45,8|
|C4|C4H4|79,0|10,8|0,0007|2,11|568,9|
|C4|C4H5|55,0|4,8|0,0057|1,47|200,4|
|C5|C5H2|53,0|4,7|0,0111|1,27|83,6|
|C5|C5H3|49,0|8,2|0,0024|1,46|36,9|
|C5|C5H4|64,0|11,3|0,0014|1,76|108,0|
|C5|C5H5|69,0|11,3|0,0020|1,65|193,4|
|C5|C5H6|70,0|10,7|0,0022|1,81|275,3|
|C6|C6H1|58,0|6,7|0,0029|1,33|224,2|
|C6|C6H2|66,0|10,9|0,0019|1,57|284,0|
|C6|C6H3|72,0|12,0|0,0011|1,92|393,9|
|C6|C6H4|73,0|11,6|0,0023|1,61|444,3|
|C6|C6H5|69,0|11,0|0,0026|1,58|389,1|
|C7|C7H1|36,0|5,2|0,0076|1,31|8,4|
|C7|C7H2|38,0|5,3|1,3700|1,17|23,8|
|C7|C7H3|42,0|7,3|0,0122|1,24|9,5|
|C7|C7H4|39,0|4,4|0,0364|1,15|22,2|
|C8|C8H1|49,0|4,4|0,0365|1,12|99,9|
|C8|C8H2|49,0|4,1|0,2501|1,08|59,6|
|C8|C8H3|53,0|6,4|0,0059|1,25|44,9|
|C8|C8H4|45,0|5,9|0,0288|1,19|46,8|
|C8|C8H5|65,0|5,6|0,0093|1,64|187,4|
|C8|C8H6|56,0|4,3|0,0031|1,66|92,4|
|C9|C9H1|39,0|4,7|0,0098|1,70|17,9|
|C9|C9H2|33,0|4,8|0,0116|1,35|4,4|
|C9|C9H3|37,0|6,5|0,0145|1,29|3,5|
|C10|C10H1|37,0|5,0|0,0646|1,26|17,5|
|C10|C10H2|36,0|4,4|0,0584|1,36|34,0|
|C10|C10H4|38,0|4,4|0,1258|1,52|127,5|
|C10|C10H5|41,0|4,9|0,3235|1,47|153,4|
|C11|C11H1|32,0|3,4|0,0125|1,28|9,3|
|C11|C11H2|35,0|5,4|0,0562|1,18|7,5|
|C11|C11H3|38,0|5,4|2,3203|1,22|54,6|
|C11|C11H4|37,0|5,0|3,0096|1,21|97,7|
|CC12|CC12H1|45,0|5,4|0,0032|1,49|20,3|
|CC12|CC12H2|47,0|8,0|0,0019|1,60|14,5|
|CC12|CC12H3|45,0|7,5|0,0030|1,30|12,8|
|CC12|CC12H4|50,0|7,6|0,0045|1,25|24,3|
|CC12|CC12H5|55,0|8,1|0,0035|1,45|52,2|
|CC12|CC12H6|35,0|4,9|0,0058|1,29|23,3|
|CC12|CC12H7|63,0|7,5|0,0046|1,83|151,1|
|CC13|CC13H1|32,0|4,2|0,0572|1,36|29,7|
|CC13|CC13H2|36,0|4,8|0,0544|1,31|27,4|
|CC13|CC13H3|33,0|4,4|0,0479|1,33|22,8|
|CC13|CC13H4|51,0|5,3|0,0773|1,41|132,5|
|CC14|CC14H1|43,0|9,8|0,0073|1,39|8,8|
|CC14|CC14H2|60,0|10,0|0,0013|1,95|79,6|
|CC14|CC14H3|69,0|5,0|0,0134|1,45|217,9|

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 5

Actualización modelación de flujo no saturado salar de

Coposa

|Calicata|Muestra|θ (%, V/V)<br>s|θ (%, V/V)<br>r|α (1/cm)|n (-)|K Saturada (cm/día)|
|---|---|---|---|---|---|---|
||CC14H4|77,0|12,9|0,0018|1,84|515,7|
||CC14H5|77,0|10,8|0,0031|1,71|593,6|
|CC15|CC15H1|71,0|9,2|0,0031|1,67|378,6|
|CC15|CC15H2|66,0|10,1|0,0018|1,74|183,8|
|CC15|CC15H3|44,0|6,4|0,0016|1,47|15,6|
|CC16|CC16H1|50,0|6,4|0,0035|1,24|38,2|
|CC16|CC16H2|59,0|5,6|0,0086|1,26|130,4|
|CC16|CC16H3|56,0|5,2|0,0084|1,23|117,0|
|CC16|CC16H4|66,0|7,4|0,0116|1,26|220,6|
|CC17|CC17H1|42,0|5,1|0,0168|1,14|88,6|
|CC17|CC17H2|47,0|6,1|0,0039|1,22|27,9|
|CC17|CC17H3|48,0|6,9|0,0010|1,47|30,5|
|CC17|CC17H4|61,0|6,2|0,0251|1,24|191,2|
|CC17|CC17H5|36,0|4,7|0,1493|1,35|52,2|
|CC18|CC18H1|38,0|5,6|0,3148|1,09|275,9|
|CC18|CC18H2|43,0|5,0|0,7610|1,11|300,5|
|CC18|CC18H3|42,0|4,8|0,2118|1,11|238,1|
|CC18|CC18H4|42,0|5,6|0,1669|1,11|490,4|
|CC18|CC18H5|51,0|5,7|0,0031|1,28|88,1|
|CC18|CC18H6|46,0|4,2|0,0065|1,17|99,8|
|CC18|CC18H7|41,0|4,2|0,0120|1,15|134,5|
|CC19|CC19H1|40,0|5,1|0,4738|1,09|168,4|
|CC19|CC19H2|49,0|3,9|0,0039|1,27|65,2|
|CC19|CC19H3|36,0|5,0|0,2793|1,07|249,6|
|CC19|CC19H6|46,0|4,5|0,4785|1,18|203,7|
|CC19|CC19H7|43,0|4,4|0,0098|1,17|90,3|
|CC19|CC19H8|50,0|4,2|0,0072|1,22|79,3|
|CC20|CC20H1|46,0|5,1|0,0138|1,22|44,1|
|CC20|CC20H2|42,0|4,5|0,0018|1,53|24,0|
|CC20|CC20H3|42,0|6,6|0,0019|1,61|12,2|
|CC20|CC20H4|44,0|6,6|0,0008|1,70|12,8|
|CC20|CC20H5|51,0|7,7|0,0005|1,87|43,8|
|CC21|CC21H1|54,0|5,2|0,0102|1,20|133,1|
|CC21|CC21H2|59,0|4,9|0,0068|1,19|254,1|
|CC21|CC21H3|48,0|4,3|0,0048|1,15|88,0|
|CC21|CC21H4|47,0|4,8|0,0063|1,14|143,9|
|CC21|CC21H5|65,0|11,6|0,0017|1,29|169,8|
|CC21|CC21H6|75,0|10,2|0,0041|1,45|415,1|
|CC22|CC22H2|51,0|9,2|0,0081|1,34|26,1|
|CC22|CC22H3|52,0|9,8|0,0079|1,28|28,4|
|CC22|CC22H4|54,0|8,5|0,0021|1,31|30,5|
|CC22|CC22H7|60,0|9,5|0,0010|1,61|81,3|
|CC24|CC24H1|35,0|3,8|0,0215|1,61|42,1|
|CC24|CC24H2|38,0|3,7|0,1918|1,39|77,6|
|CC24|CC24H3|39,0|3,7|0,0856|1,44|171,4|
|CC24|CC24H4|38,0|4,3|0,0210|1,58|110,4|
|CC24|CC24H5|34,0|4,3|0,0721|1,53|123,3|
|CC24|CC24H6|61,0|4,6|0,0018|2,90|175,0|
|CC24|CC24H7|47,0|5,5|0,8217|1,26|262,7|
|CC24|CC24H8|51,0|4,5|0,0080|1,68|90,9|

Fuente: Elaboración Propia

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 6

Actualización modelación de flujo no saturado salar de Coposa

**Figura 2-2: Ejemplo ajuste curvas de succión**

Fuente: Elaboración Propia

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 7

Actualización modelación de flujo no saturado salar de

Coposa

**3.** **PROFUNDIDAD DEL NIVEL FREÁTICO SALAR DE COPOSA**

El salar de Coposa corresponde a una zona naturalmente con niveles freáticos someros, que cuenta con
información de niveles y profundidades para puntos de observación con el fin de hacer seguimiento a la
evolución del nivel piezométrico, los cuales se pueden observar en la Figura 3-1. A partir de la información
histórica y los resultados del modelo numérico (Anexo 1.2 “Actualización del modelo hidrogeológico conceptual
y numérico a diciembre de 2023” de la presente Adenda Complementaria), se ha estimado la evolución de la
profundidad del nivel freático en puntos de observación. Con este fin, se han ajustado los resultados del modelo
numérico a los datos observados en los distintos puntos.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 8

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 3-1: Ubicación de puntos de observación**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 9

Actualización modelación de flujo no saturado salar de

Coposa

En términos generales, de acuerdo con los resultados de las simulaciones del modelo hidrogeológico numérico
de flujo (Anexo 1.2 “Actualización del modelo hidrogeológico conceptual y numérico a diciembre de 2023” de la
presente Adenda Complementaria), la mayor parte de los puntos de observación de nivel somero ubicados en
el salar de Coposa ya tuvieron su nivel mínimo durante los años 2019-2020 y, adicionalmente, la simulación de
la presente DIA muestra niveles más altos en el salar de Coposa que la simulación EIA. Por otro lado, para el
inicio del actual proyecto (primer trimestre 2025) la totalidad de los puntos monitoreados tendrán un ascenso en
su nivel respecto de la situación actual, debido a la reducción paulatina del bombeo. Ambos escenarios de
simulación consideran el efecto del cambio climático en sus variables de entrada.

Los escenarios evaluados son los siguientes (ejemplo en Figura 3-2):

 - Escenario 1: corresponde a la mayor profundidad estimada en el Caso Base de la presente DIA,
escenario aprobado mediante RCA 20219900112.

 - Escenario 2: corresponde a la mayor profundidad estimada para el proyecto actual, que corresponde

a la máxima profundidad en el periodo del proyecto.

**Figura 3-2: Ejemplo configuración de escenarios**

Fuente: Elaboración propia

Finalmente, la Tabla 3-1 muestra los pozos seleccionados como punto de observación para el análisis de la
evolución de la profundidad, las calicatas consideradas en la modelación y las profundidades presentes para
cada caso a simular. Se observa que el escenario 2 corresponde al caso más favorable, lo cual es consistente
con la mayor recuperación de niveles debido a la disminución acumulada de las extracciones en el presente
proyecto (actual DIA).

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 10

Actualización modelación de flujo no saturado salar de

Coposa

**Tabla 3-1: Puntos modelados, puntos de observación y profundidades desde la superficie de**

**terreno por escenario**

|Calicata|Punto de<br>Observación|Escenario 1 (cm) -<br>Caso Base|Escenario 2 (cm) -<br>DIA|
|---|---|---|---|
|C3|CMW-12|158|151|
|C4|CMW-05B|233|226|
|C5|CPS-26|172|172|
|C7|CMW-02|233|200|
|C6|CMA-16|255|246|
|C8|CPMA-02|225|225|
|C9|CPMA-02|225|225|
|C10|CPMA-02|225|225|
|C11|CPS-35|142|140|
|C12|CPMA-02|225|225|
|C13|CPMA-02|225|225|
|C14|CPMA-02|225|225|
|C15|CMA-16|255|246|
|C16|CPS-54|210|208|
|C17|CWE-17|140|138|
|C18|CMW-29B|63|54|
|C19|CMW-12|158|151|
|C20|CWE-21|95|92|
|C21|CMW-03|186|181|
|C22|CMW-06|137|132|
|C24|CWE-21|95|92|

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 11

Actualización modelación de flujo no saturado salar de

Coposa

**4.** **MODELOS DE FLUJO NO SATURADO**

A partir de la interpretación de curvas de succión e información meteorológica se construyeron modelos de flujo
no saturado en el software Hydrus1D, el cual resuelve la ecuación de Richards de flujo no saturado y permite
obtener el perfil de humedad y succión en una columna de suelo. El modelo es ejecutado hasta que se alcanza
el régimen permanente en los casos descritos en la sección 3. El respaldo de las herramientas numéricas se
encuentra en el Apéndice 2. Se considera lo siguiente en su construcción:

 - Para la estratificación del perfil en profundidad se utilizan los horizontes definidos en la campaña de

muestreo de suelo (detalles se pueden revisar en Anexo 2.5 Caracterización Ambiental Suelos de la

presente DIA y Anexo 12 de la Adenda). El estrato más profundo se extrapola hasta llegar al nivel

freático para cada modelo.

 - En el límite inferior de la columna se utiliza succión nula, condición que corresponde al nivel freático.

 - En el límite superior de la columna se imponen las condiciones meteorológicas más desfavorables.
Para el caso de la precipitación se establece como nula, para la evaporación el valor es constante y
equivalente a la máxima evaporación potencial (6 mm/día, Línea de Base Hidrología del EIA, Arcadis
(2018)).

Desde la Figura 4-1 hasta la Figura 4-21 se muestran los perfiles de humedad y succión obtenidos para los
modelos de cada calicata, considerando los dos escenarios simulados (caso base y caso con proyecto (DIA)).
En cada gráfica además se incluye el límite y el número de muestra, como así también la ubicación del nivel
freático en el perfil. Los resultados muestran que los estratos de suelo más gruesos (arenas y arenosos)
muestran un rango de humedad desde 5% hasta un 50% aproximadamente, mientras q los estratos más finos
(arcillas y arcillosos) desde un 25% hasta un 70%, lo que se condice con la cualidad de retención de agua de
cada tipo de suelo.

Además, de forma general, se observan los quiebres en las curvas de humedad entre un estrato y otro, lo cual
se debe a la granulometría del tipo de suelo. Estos quiebres son más bruscos cuando el cambio es entre suelos
finos y gruesos, como se puede observar específicamente en C4 (Figura 4-2) entre el estrato 3 y 4. En términos
generales, la succión presenta un comportamiento más suave (con menos quiebres) y, a profundidades
mayores a 20cm, las calicatas muestran succiones menores al Punto de Marchitez Permanente (PMP), a
excepción de la calicata C11 (Figura 4-9) que presenta succiones menores a PMP bajo los 40 cm de
profundidad.

Por otro lado, las mayores diferencias de succión y humedad entre escenarios de simulación se observan a
mayor profundidad en los perfiles, es decir en la zona más cercana al nivel freático, y va disminuyendo medida
que se va evaluando a menor profundidad. Cabe notar, que el caso con proyecto (escenario 2) muestra
condiciones más favorables en relación con la succión y humedad disponibles con respecto al escenario base.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 12

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-1: Perfil de succión y humedad simulada en el suelo en calicata C3**

Fuente: Elaboración propia.

**Figura 4-2: Perfil de succión y humedad simulada en el suelo en calicata C4**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 13

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-3: Perfil de succión y humedad simulada en el suelo en calicata C5**

Fuente: Elaboración propia.

**Figura 4-4: Perfil de succión y humedad simulada en el suelo en calicata C6**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 14

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-5: Perfil de succión y humedad simulada en el suelo en calicata C7**

Fuente: Elaboración propia.
**Figura 4-6: Perfil de succión y humedad simulada en el suelo en calicata C8**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 15

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-7: Perfil de succión y humedad simulada en el suelo en calicata C9**

Fuente: Elaboración propia.

**Figura 4-8: Perfil de succión y humedad simulada en el suelo en calicata C10**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 16

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-9: Perfil de succión y humedad simulada en el suelo en calicata C11**

Fuente: Elaboración propia.
**Figura 4-10: Perfil de succión y humedad simulada en el suelo en calicata CC12**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 17

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-11: Perfil de succión y humedad simulada en el suelo en calicata CC13**

Fuente: Elaboración propia.

**Figura 4-12: Perfil de succión y humedad simulada en el suelo en calicata CC14**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 18

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-13: Perfil de succión y humedad simulada en el suelo en calicata CC15**

Fuente: Elaboración propia.
**Figura 4-14: Perfil de succión y humedad simulada en el suelo en calicata CC16**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 19

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-15: Perfil de succión y humedad simulada en el suelo en calicata CC17**

Fuente: Elaboración propia.

**Figura 4-16: Perfil de succión y humedad simulada en el suelo en calicata CC18**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 20

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-17: Perfil de succión y humedad simulada en el suelo en calicata CC19**

Fuente: Elaboración propia.

**Figura 4-18: Perfil de succión y humedad simulada en el suelo en calicata CC20**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 21

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-19: Perfil de succión y humedad simulada en el suelo en calicata CC21**

Fuente: Elaboración propia.

**Figura 4-20: Perfil de succión y humedad simulada en el suelo en calicata CC22**

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 22

Actualización modelación de flujo no saturado salar de

Coposa

**Figura 4-21: Perfil de succión y humedad simulada en el suelo en calicata CC24**

Fuente: Elaboración propia.

**5.** **CONCLUSIONES**

A partir de la modelación realizada se pueden extraer las siguientes conclusiones:

 - Se puede observar que, consistentemente con la recuperación del nivel freático, tanto el contenido de
humedad como la succión presentan condiciones más favorables para el escenario con proyecto
(escenario 2) con respecto a la situación base (escenario 1).

 - En general, a profundidades mayores a 20cm, todas las calicatas muestran succiones menores al
Punto de Marchitez Permanente en los 2 escenarios, excepto el punto de la C-11 se cumple con lo
anterior a profundidades mayores a 40cm.

 - Si bien las diferencias en los resultados de succión y humedad entre los distintos escenarios no son
significativas, el escenario de la presente DIA corresponde a una situación de menor profundidad del
nivel freático y, por ende, menor succión.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 23

Actualización modelación de flujo no saturado salar de

Coposa

**6.** **REFERENCIAS**

Mualem, Y. 1976. A new model predicting the hydraulic conductivity of unsaturated porous media.
Van Genuchten, M. Th., 1980. A close form equation for predicting the hydraulic conductivity of unsaturated
soils.

Van Genuchten et al, 1991. The RETC Code for Quantifying the Hydraulic Functions of Unsaturated Soils.

Declaración de Impacto Ambiental Adecuación Cronograma y Obras Collahuasi
HIDRO.GEOB806.INF004.REV0 24