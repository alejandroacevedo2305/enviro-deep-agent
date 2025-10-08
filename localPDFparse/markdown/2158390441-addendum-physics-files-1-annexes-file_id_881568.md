---
title: Sin título
author: pc
date: D:20230820235316-04'00'
language: es
type: general
pages: 2
has_toc: True
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - APÉNDICE B: MÉTODO DE ELEMENTOS FINITOS O MÉTODO VARIACIONAL
  - Figura 1. Subdivisión de una región en triángulos
  - 2.1 Procedimiento
  - 2
-->

Apéndice D - Método de Elementos Finitos / Estudio CEM

ADENDA Proyecto “ Nueva Subestación Seccionadora

Loica y Nueva Línea 2x220 Kv Loica - Portezuelo”

# APÉNDICE B: MÉTODO DE ELEMENTOS FINITOS O MÉTODO VARIACIONAL

El problema matemático a resolver en un problema de campos consiste en determinar un
potencial eléctrico o magnético y el campo en el interior de un dominio tridimensional, donde el
potencial satisface la ecuación de Laplace, o más general, la ecuación de Poisson, cuando existe
carga eléctrica o corriente y materiales con diferentes propiedades dieléctricas, conductivas y
magnéticas. Las condiciones de borde que debe cumplir el potencial corresponden a condiciones de
tipo valor de la función conocido, valor de la derivada conocida, o mixtas. La función potencial
solución de este problema minimiza la funcional de energía total del campo dentro del dominio.
Gracias a esta propiedad de la solución, la esencia del método consiste en buscar directamente la
función que minimiza la funcional, en vez de intentar resolver la ecuación diferencial.

La habilitación del método requiere en primer lugar subdividir la región en estudio en un
cierto número de sub-regiones (usualmente poliedros en problemas tridimensionales o polígonos
en dos dimensiones) tal como lo muestra la figura.

# Figura 1. Subdivisión de una región en triángulos

Las aristas de estos elementos definen una malla, y sus vértices corresponden a los nudos
de la malla. Los elementos son de forma y tamaño arbitrarios, con la condición de que sus lados se
ajusten a las superficies de separación internas y al contorno del dominio. Las características
eléctricas se suponen constantes en cada elemento, aun cuando pueden variar de uno a otro.

La minimización de la funcional conduce a una expresión del tipo:

[ C 2K V 2K + C 3K V 3K ]

− ∑ C 2K V 2K +
= Ω 1

− ∑ C 2K V 2K + C 3K V

V 1 = Ω 1
∑ C

2K 2K 3K 3K

1

∑ C

1K
1 1

1

Apéndice D - Método de Elementos Finitos / Estudio CEM

ADENDA Proyecto “ Nueva Subestación Seccionadora

Loica y Nueva Línea 2x220 Kv Loica - Portezuelo”

para cada vértice “i”, donde los V k representan los potenciales y los C k son coeficientes conocidos,
que dependen de las coordenadas de los vértices y de las características físicas de los materiales.
Repitiendo la condición de minimización para todos los vértices, se forma un sistema de ecuaciones

lineales:

A V = U

Donde:

A es la matriz de coeficientes del sistema, dependiente de las características de los elementos
en que se subdivide la región y de las coordenadas de sus vértices
V es el vector de incógnitas, los potenciales Vi desconocidos
U es el vector dato, obtenido de las condiciones a borde

De la formulación anterior, se derivan las expresiones correspondientes a cada componente
del vector campo en el interior de un elemento; en la formulación básica, la intensidad de campo
resulta constante en el interior del elemento por lo que presenta discontinuidades en las fronteras
de los triángulos.

# 2.1 Procedimiento

El procedimiento de cálculo de campos por el método de elementos finitos puede
esquematizarse en el siguiente proceso:
_1.- Generación de la malla:_ Definido un dominio y una configuración de materiales (dieléctricos,
conductores, magnéticos), se procede a la subdivisión de dicho dominio o generación de la malla,
con libertad de forma, orientación y tamaño de los elementos. Existen generadores de mallas
computacionales, facilitando esta parte del modelamiento.
_2.- Caracterización de elementos:_ Se definen las características dieléctricas, conductivas o
magnéticas de todos los elementos, las cuales se suponen constantes en el interior de cada uno de
ellos, y los restantes parámetros por elemento.
_3.- Cálculo de coeficientes de ecuaciones de potencial:_ Se generan los coeficientes C ik asociados a

cada nudo de la malla.

_4.- Formación del sistema de ecuaciones:_ Se estructura el sistema de ecuaciones, luego de haber
calculado todos los coeficientes en la etapa anterior.
_5.- Solución del sistema:_ Se resuelve el sistema, utilizando métodos directos o iterativos,
dependiendo del grado de densidad de la matriz de coeficientes.
_6.- Cálculo de campo y otras cantidades:_ Se aplican las ecuaciones de campo para evaluar el campo
en zonas de interés y otros parámetros derivados.

_7.- Visualización de resultados._

El método de elementos finitos mejora su precisión en la medida que se modela con triángulos
de menor tamaño, por eso se reduce el tamaño de los triángulos en la zona cercana a la línea y

tierra.

# 2