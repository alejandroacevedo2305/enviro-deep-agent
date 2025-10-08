---
title: Microsoft Word - Memoria PEAS (CAMARA - POZO)
author: Desconocido
date: D:20240612124412-04'00'
language: es
type: general
pages: 7
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MEMORIA ESTRUCTURAS
-->

# MEMORIA ESTRUCTURAS

## PROYECTO PLANTA ELEVADORA DE AGUAS SERVIDAS E IMPULSIÓN

_**LOTEO DOÑA AGUSTINAS IV**_

_**COMUNA: LINARES**_

**1.** **Diseño Estructural Planta Elevadora.**

**1.1 Introducción**

El objetivo de esta memoria de cálculo es diseñar la estructura de un pozo de una
planta elevadora de aguas servidas con una profundidad de 8.54 metros y un diámetro
interior de 1,80 metros. Se considerará el tipo de suelo granular con fi=31°, y se
diseñará con un empuje de reposo del suelo granular y un empuje hidrostático. La
estructura se modelará en SAP2000 y se verificará su estabilidad y resistencia.

Normativa y bases para el diseño

Para el diseño estructural del pozo se seguirán las normas y recomendaciones del
Código ACI 318-19 para el diseño de concreto armado, Nch 3171 Disposiciones
generales y combinaciones de carga

Se considerará el suelo granular con un ángulo de fricción interna de 31°. Se diseñará
con un empuje de reposo del suelo granular y un empuje hidrostático.

**1.2** **Normativa aplicada**

El diseño de la estructura se realiza según las indicaciones de las siguientes normas:

NCh 430 - 2008 Hormigón Armado - Requisitos de Diseño y Cálculo
NCh 433 - 2008 Diseño Sísmicos de Estructuras
D.S.60 Hormigón Armado - Requisitos de Diseño y Cálculo
NCh1537 - 2009 Cargas permanentes y cargas de uso
ACI 318-19 Requisitos de reglamento para concreto estructural
NCH 3171 Disposiciones generales y combinaciones de carga

**2** **Materiales y calidades**

Los distintos elementos estructurales se realizan con los siguientes materiales y
propiedades.
Para la construcción del pozo se utilizará concreto armado con una resistencia a la
compresión de 250 kg/cm2 y acero de refuerzo A44-28

**2.1** **Hormigón**

Se utiliza hormigón en las fundaciones, muros.
Se consideran las siguientes especificaciones:

Para Fundaciones
Hormigón G12
Resistencia cilíndrica f ́c 120 [MPa]
Módulo de Elasticidad: 16281 [MPa]

Para sobrecimientos, muros y losa
Hormigón G17
Resistencia f ́c 17 [MPa]
Módulo de Elasticidad: 196880 [kg/cm2]
Se considera el módulo de elasticidad 15100√fc [kg/cm2] indicado en ACI318

**2.2** **Acero**

Se utilizar acero para conformar hormigón armado en fundaciones, muros, vigas y
losa.
Se consideran las siguientes especificaciones:

Acero A500-560
Tensión de Fluencia fy: 5000 [kg/cm2]
Tensión de Ruptura fu 5600 [kg/cm2

**2.3** **Cargas y sobrecargas**

Para el diseño de la estructura se ha considerado las siguientes cargas

**a.** **Cargas Peso Propio y Permanentes (dl)**

Se consideran los siguientes pesos específicos de los materiales utilizados
Hormigón Armado 2500 [kg/m3]
Acero 7850 [kg/m3]

**b.** **Sobrecargas de Uso (ll)**

De acuerdo a la NCh1537 se ha considerado las siguientes sobrecargas
Sobrecarga de piso 150 [kg/m2]
Sobrecargas de techo 30 [kg/m2]

**c.** **Carga hidrostática**

Se considera el siguiente peso específico para el agua

Agua 1000 [kg/m2]

_PROYECTO PEAS DOÑA AGUSTINAS IV, COMUNA DE LINARES._ 2

**3.- Estudio De Suelos**

De acuerdo con la Mecánica de Suelos, el terreno donde se emplazará la PEAS se
compone de dos estratos. El primer estrato E-1 corresponde a un suelo fino que varía
entre arcilla y arena, con un espesor de 0,60 metros de color café oscuro térreo. El
segundo estrato E-2, es un suelo granular mal graduado con arena con bloques
ubicado desde los 0,60 hasta los 8,5 [m], de color gris térreo. Este último, se
considera muy aceptable para efectos de sello de fundación. Por lo tanto, Se debe
fundar en este estrato (E-2) por especificaciones espaciales de la PEAS.

_PROYECTO PEAS DOÑA AGUSTINAS IV, COMUNA DE LINARES._ 3

**4.- Presiones laterales del suelo**

Las presiones laterales del suelo se determinarán mediante el método de Rankine,
considerando el empuje de reposo del suelo granular y el empuje hidrostático.

Carga Hidrostática

Empuje pasivo del suelo

_PROYECTO PEAS DOÑA AGUSTINAS IV, COMUNA DE LINARES._ 4

**5.- Verificación estructural**

La estructura se modelará en SAP2000 para obtener las tensiones en el hormigón de
forma gráfica. Se verificará la estabilidad y la resistencia de la estructura mediante los
siguientes cálculos:

Espesor de pared: se calculará el espesor de pared necesario para resistir las cargas
consideradas.
Armado de pared: se calculará el armado de la pared mediante la distribución de las
cargas entre las barras de acero.

**5.1.- Pozo bombas**

Para la construcción del pozo se utilizará concreto armado con una resistencia a la
compresión de 250 kg/cm2 y acero de refuerzo A44-28

Solicitaciones consideradas

Empuje de reposo del suelo granular:
Ko= 1-sen(31°,)= 0.485
Y suelo= 2.52 tonf/m3 (Se estandariza a un solo estrato)

Combinación de carga considerada:
Se considera la combinación:

C1. 1.2 carga muerta + 1.6 empuje lateral del suelo

Resultados obtenidos, momento máximo en C1: 1.2 Carga muerta + 1.6 empuje
lateral.

El momento ultimo obtenido es: Mu= 0.46 tonf*m
Datos geométricos de la sección de hormigón armado en la pared de la PEAS.

F’c= 250 kgf/cm2

_PROYECTO PEAS DOÑA AGUSTINAS IV, COMUNA DE LINARES._ 5

Fy= 2855 kgf/cm2
Espesor: 20 cm
As (fi10@20) = 3.92 cm2
Mn= 1.98 tonf*m

fi*Mn= 0.9*1.98=1.78 tonf*m
ratio:0.47/1.78*100=26.40%

La tensión solicitante por momento flector solicitante en la sección en las paredes del
pozo húmedo es del orden del 26.40% de su capacidad nominal, por lo cual la
estructuración propuesta es cumple con la resistencia.

**5.2.- Cámara de Rejas**

De igual forma, se presenta a continuación la verificación del diseño estructural de la
cámara de rejas.

Para la construcción del pozo se utilizará concreto armado con una resistencia a la
compresión de 250 kg/cm2 y acero de refuerzo A44-28

Solicitaciones consideradas

Empuje de reposo del suelo granular:
Ko= 1-sen(31°,)= 0.485
Y suelo= 2.52 tonf/m3 (Se estandariza a un solo estrato)

*Nota: Dada su profundidad, no se encuentra influenciada por la presencia de la napa
freática

Combinación de carga considerada:

_PROYECTO PEAS DOÑA AGUSTINAS IV, COMUNA DE LINARES._ 6

Se considera la combinación:

C1. 1.2 carga muerta + 1.6 empuje lateral del suelo

Resultados obtenidos, momento máximo en C1: 1.2 Carga muerta + 1.6 empuje
lateral.

El momento ultimo obtenido es: Mu= 0.08 tonf*m
Datos geométricos de la sección de hormigón armado en la pared de la Cámara de
Rejas.

F’c= 250 kgf/cm2
Fy= 2855 kgf/cm2
Espesor: 15 cm
As (fi10@20) = 3.92 cm2
Mn= 1.45 tonf*m

fi*Mn= 0.9*1.45=1.305 tonf*m
ratio:0.11/1.305*100=8,6%

La tensión solicitante por momento flector solicitante en la sección en las paredes de la
cámara de rejas es del orden del 8,6 % de su capacidad nominal, por lo cual la
estructuración propuesta es cumple con la resistencia.

**DENIS OJEDA CARO**

**INGENIERO CIVIL**
Talca, Junio de 2024

_PROYECTO PEAS DOÑA AGUSTINAS IV, COMUNA DE LINARES._ 7