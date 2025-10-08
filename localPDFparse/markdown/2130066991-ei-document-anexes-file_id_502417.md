---
title: (Microsoft Word - Informe Modelaci\363n Transito SW)
author: Daniela Gomez
date: D:20141204100219+03'00'
language: es
type: report
pages: 13
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTIMACIÓN DEL ÁREA DE DISPERSIÓN A TRAVES DE UN MODELO DE TRAYECTORIA DE PARTICULAS
-->

# ESTIMACIÓN DEL ÁREA DE DISPERSIÓN A TRAVES DE UN MODELO DE TRAYECTORIA DE PARTICULAS

**PROYECTO**

“MODIFICACIÓN CENTRO DE ENGORDA DE SALMONES CANAL MORALEDA, AL NORESTE DE ISLA

TRÁNSITO SW, CÓDIGO CENTRO No 110762 (ISLA TRÁNSITO SW)”

**PARA:**

## EXPORTADORA LOS FIORDOS LTDA.

**NOVIEMBRE, 2014**

Santiago: Renato Sánchez 3838, Las Condes; Fono (56-02) 2070154; Fax (56-02) 2634766; e-mail: ambiental@poch.cl

Puerto Montt: Av. Juan Soler Manfredini No 41 of. 1401; Fono (56-65) 2773000; Fax (56-65) 2363247; e-mail: pmontt@poch.cl

Coyhaique: José de Moraleda No 412, Fono (56-67) 573188; Fax (56-67) 573184

**ARGENTINA**

Buenos Aires: Montevideo 765 Piso 3o; Fono/Fax (054-11) 4813 5133; e-mail: pochcdiar@fibertel.com.ar

**COLOMBIA**

Bogotá: Carrera 12 No 96 -81 oficina 203; Fono 057 (1) 691 22 81 - 057 (1) 616 78 09; e-mail: marcos.bravo@poch.cl

**PERÚ**

Lima: Av. Camino Real 1225, Piso 7, San Isidro; Fono (51-1) 421 8700; Fax: (51-1) 421 7959; e-mail: fiorella.balbi@poch.com.pe

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**Contenido**

## 1. INTRODUCCIÓN ......................................................................................................... 3 2. OBJETIVOS .................................................................................................................... 3 3. MATERIAL Y MÉTODOS .......................................................................................... 4

3.1. Modelación Depomod y Área de Dispersión ..................................................................................... 4
3.2. Cálculo del Índice de Impacto .............................................................................................................. 7

## 4. RESULTADOS Y DISCUSIÓN................................................................................... 8

4.1. Modelación Depomod y Área de Dispersión ..................................................................................... 8
4.2. Cálculo del Índice de Impacto ........................................................................................................... 11

## 5. CONCLUSIÓN ............................................................................................................. 13

LF - 1256 2

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**1.** **INTRODUCCIÓN**

Según lo establecido en el Articulo 17 del D.S. 320/01 y sus modificaciones (RAMA) se indica que

“Es responsabilidad del titular que su centro opere en niveles compatibles con las capacidades de los

cuerpos de agua lacustres, fluviales y/o marítimos, para lo cual deberá mantener siempre condiciones

aeróbicas. Por otro lado, según el Literal j) del artículo 6 del D.S. N° 95/2001, el proyecto debe

establecer que no afectara la capacidad de dilución, dispersión, autodepuración, asimilación y

regeneración de los recursos naturales renovables presentes en el área de influencia del proyecto. Por

lo tanto, se opta por realizar una estimación del área de dispersión de sólidos del centro de cultivo a

través de un modelo de trayectoria de partículas.

Existen diversos modelos en el mercado en distinto grado de complejidad y alcance de resultados

que intentan predecir la concentración de carbono orgánico bajo balsas jaulas, sin embargo, hay

escasos estudios que evalúen cuánto está afectando el carbono orgánico a la disponibilidad de

oxígeno en el fondo marino (Findlay, 1997; Gargiulo, 2007 [1] ).

Por ello, se han desarrollado herramientas que permiten evaluar el contenido de carbono orgánico

en el sedimento depositado producto de la actividad acuícola y la demanda de oxígeno disuelto en el

fondo, relacionado a su vez con las características oceanográficas y de producción de un centro de

engorda. Una de estas herramientas se ambienta bajo la aplicación de Software DEPOMOD y una

plataforma para modelar basado en dinámica de sistemas y modelos publicados en la prensa

especializada.

**2.** **OBJETIVOS**

Evaluar si el proyecto se desarrollará en niveles compatibles con la capacidad del cuerpo de agua

receptor, presentando condiciones aeróbicas al final del ciclo productivo.

De esta manera, de desprenden los siguientes objetivos específicos:

 - Estimar mediante un modelo matemático el área de dispersión de fecas y alimento no

consumido del proyecto y cantidad de residuos sólidos (carbono) que eventualmente generará

el centro de cultivo con una ampliación de biomasa.

 - Evaluar la potencial generación de condiciones de anaerobiosis y efectos negativos sobre los

recursos renovables al final del ciclo productivo del proyecto.

1 Gargiulo, M. E. 2007. Evaluación de la Capacidad de Carga en Centros de Cultivo mediante la Combinación de un Modelo de
Dispersión (DEPOMOD) con un Modelo Basado en el Balance de Oxígeno en Sedimento (Findlay & Watling). Salmociencia. 83-87.

LF - 1256 3

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**3.** **MATERIAL Y MÉTODOS**

**3.1.** **Modelación Depomod y Área de Dispersión**

El modelo DEPOMOD versión 2.2 predice la depositación de sólidos en el fondo marino alrededor

de las balsas jaulas de cultivo de peces, asociando los cambios bentónicos provocados por los aportes

de materia orgánica total en el medio. Para ello, combina las condiciones geográficas e hidrográficas

locales con los volúmenes de compuestos orgánicos totales liberados (material fecal y alimento no

consumido), trazando un mapa de acumulación o flujos de sedimentación de residuos en la grilla de

fondo marino. El modelo está estructurado básicamente en cuatro componentes o módulos que se

acoplan para estimar las concentraciones de Carbono Orgánico Total (COT) en el fondo. Estos

módulos se definen como generación de grilla, rastreo de partículas, resuspensión y módulo de

respuesta bentónica (ver esquema). Cromey (2002) menciona que la cuantificación de la dispersión de

los residuos liberados por los centros de cultivo pueden ser estimados conectando los tres primeros

módulos propuestos (Fig. 1).

Los módulos mencionados anteriormente se denominan:

 - **Grid Generation:** Módulo generador de la grilla, el cual permite detallar la batimetría,

posición de jaulas, estaciones de muestreo y ajustar el área de interés que se desea estudiar.

 - **Particle Tracking:** Módulo rastreo de partículas, este módulo que permite dar solución al

proceso de advección de partículas a través de la columna de agua

 - **Resuspension:** Módulo de resuspensión que calcula los sólidos, carbón u otro compuesto

en términos de flujos de deposición del compuesto con o sin resuspensión

 - **Benthic response:** Módulo que predice la respuesta bentónica para ciertos niveles de

acumulación de sólidos en el fondo.

LF - 1256 4

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión

a través de un modelo de trayectoria de partículas - C **E**

**Figura 1.-** Esquema de **i**

modelo DEPOMOD.

**Fuente:** Adaptado por P **O**

no ha sido incluido en el presente estudio, mie

para obtener los valores de salida de Carbono, ientes en cuadratura, según el análisis de corre **n**

e Sitio, y sin resuspensión. La tabla 1 resume l **a**

El último de estos módulos

CH 2013 2 de Cromey et al., 2002 3 .

ntras que el módulo de

resuspensión sólo se ocupó

condición, es decir, con cor **r**

Caracterización Preliminar **d**

del modelo.

a través de un modelo de trayectoria de partículas - C **E**

modelo DEPOMOD.

**Fuente:** Adaptado por P **O** CH 2013 2 de Cromey et al., 2002 3 .

no ha sido incluido en el presente estudio, mie ntras que el módulo de

para obtener los valores de salida de Carbono, ientes en cuadratura, según el análisis de corre **n**
e Sitio, y sin resuspensión. La tabla 1 resume l **a** considerando así la peor tometría establecido en la información de entrada

Depomod a centros de cultivo de peces en la X° Región de l **o**

esca.
lack. 2002. DEPOMOD- Modelling the Deposition and Biol **o** s Lagos (Primera parte). Licitación gical Effects of Waste Solids from
. 211-239. [S Isla Transito SW]

5

Los contenidos que soporta el presente docu **m**

[ntegración de los módulos de utilizados por el ] Queda prohibido su reproducción, total o parcial, por cualqu **i** ento constituyen Propiedad Intelectual. er medio, en forma íntegra o extractada.

**Fuente:** Adaptado por P **O**

no ha sido incluido en el presente estudio, mie

para obtener los valores de salida de Carbono, ientes en cuadratura, según el análisis de corre **n**

e Sitio, y sin resuspensión. La tabla 1 resume l **a**

Depomod a centros de cultivo de peces en la X° Región de l **o**

esca.

lack. 2002. DEPOMOD- Modelling the Deposition and Biol **o**
. 211-239.

Los contenidos que soporta el presente docu **m**

[ntegración de los módulos de utilizados por el ] Queda prohibido su reproducción, total o parcial, por cualqu **i**

2 Poch 2013. Aplicación del programa
N° 4728-62-LE12. Subsecretaria de **P**
3 Cromey, C. J.; T. D. Nickell, K. D. **B**
Marine Cage Farms. Aquaculture 214

considerando así la peor tometría establecido en la información de entrada

s Lagos (Primera parte). Licitación gical Effects of Waste Solids from

LF - 1256

5

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**Tabla 1.** Información de entrada del modelo Depomod.

|Módulo Depomod|Variable|Observaciones|
|---|---|---|
|**Grid Generation **|Batimetría|Extraída del plano batimétrico|
|**Grid Generation **|Ubicación Módulos|Extraída del plano batimétrico|
|**Particle Tracking **|Corrientes4 5|CPS, analizando 5 capas de la columna.|
|**Particle Tracking **|Velocidad Fecas|0,032 m/s, según Gowen and Bradbury (1987)|
|**Particle Tracking **|Velocidad ANC|0,128 m/s para un tamaño de pellet de 9200um|
|**Particle Tracking **|Agua en el pellet|9%|
|**Particle Tracking **|Digestibilidad del pellet|85%|
|**Particle Tracking **|Perdida de alimento|5%|
|**Particle Tracking **|Carbono en el Pellet|46%|
|**Particle Tracking **|Carbono en las Fecas|30%|
|**Particle Tracking **|Numero de estructuras|Proyecto Técnico|
|**Particle Tracking **|Dimensiones estructuras|Proyecto Técnico|
|**Particle Tracking **|Alimento por jaula|Factor de conversión de 1,2|
|**Resuspensión **|No se aplicó|Sólo utilizada para obtener los resultados de Carbono<br>(g/m2/día)|

Los datos obtenidos fueron ploteados en el plano de la concesión para evidenciar el área de

dispersión del carbono producto del alimento no consumido y de las Fecas del proyecto. Se utilizó

un valor de referencia de 500 g C/m [2] /año para definir el limite menor del área señalada, ya que

Cromey _et al_ . [6] (1998), señalan que valores por sobre esta concentración podrían causar condiciones

de degradación anaeróbica en el fondo. Sin embargo, este valor es sólo referencial para definir el

polígono de influencia de los sólidos.

Para determinar si el presente proyecto generará una condición anaeróbica bajo las jaulas, se calculó

el siguiente Índice de Impacto.

4 Información extraída de la correntometria de 24 horas y en periodo de cuadratura.
5 El modelo DEPOMOD asume internamente el efecto de las estructuras (jaulas y pecera) sobre el transporte de
partículas.
6 Cromey CJ, Black KD, Edwars A and Jack IA. 1998. Modeling the deposition and biological effects of organic carbón from marine
sewage discharges. Estuarine, Coastal and shelf science 47: 295 - 308.

LF - 1256 6

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**3.2.** **Cálculo del Índice de Impacto**

Una vez conocido el aporte de carbono total del centro al área de sedimentación definida, se

procedió a la determinación del Índice de Impacto, el cual fue establecido en base a las ecuaciones de

Findlay y Watling (1997) [7,] quienes estimaron el estado del sedimento en base al aporte de oxígeno y

la demanda de oxígeno.

஺௣௢௥௧௘ ௗ௘ ை௫௜௚௘௡௢ ଻ଷ଺,ଷା଺଻ଶ,ହכ ௅௢௚ [భబ] ሺ௏ሻ

[ܫൌ]
஽௘௠௔௡ௗ௔ ௗ௘ ை௫௜௚௘௡௢ ଵ,଴଻כ ௑ିଷଶ,଺

஺௣௢௥௧௘ ௗ௘ ை௫௜௚௘௡௢
ܫൌ

ଵ,଴଻כ ௑ିଷଶ,଺

Dónde:

v: _velocidad promedio de corriente_ a 1 m del fondo [8] .

x _: aporte de carbono total al sedimento_ (mmol/m [2] /d).

Este modelo contiene ecuaciones que permitieron evaluar el estado del sedimento con los aportes

totales de Carbono bajo un escenario de peor condición, es decir, en período de corrientes en

cuadratura, tal como lo contempla la Resolución Exenta No 3612/2009. El modelo predice que en la

medida que el valor del índice I se incrementa a valores mayores a 1, la perturbación sobre el

sedimento disminuye; mientras que por el contrario, en la medida que desciende del valor 1, la

perturbación sobre el sedimento se verá incrementada.

Debido a la alta dispersión de los datos entregados por el modelo, se procedió a calcular el índice de

impacto con el valor máximo encontrado y el promedio de todos ellos, para establecer la peor

condición de carbono en el medio.

7 Findlay, R.H., Watling, L., 1997. Prediction of benthic impact for salmon net-pens based on the balance of benthic oxygen supply and
demand.Mar. Ecol.: Prog. Ser. 155, 147-157.
8 Extraído de la CPS 2014.

LF - 1256 7

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**4.** **RESULTADOS Y DISCUSIÓN**

**4.1.** **Modelación Depomod y Área de Dispersión**

La Figura 2 entrega el plano batimétrico del sector donde se emplazará el proyecto. El sector donde

se desea instalar los módulos posee una profundidad promedio de 40 m aproximadamente. Las

profundidades en general tienden a aumentar hacia el centro de la concesión, en dirección hacia el

vértice B.

La Figura 3 entrega el área de dispersión de acuerdo a la modelación realizada, entregando el

escenario más desfavorable en cuanto a corrientes y alimentación proyectada. El modelo indica que

la mayor concentración de carbono en el lugar estará bajo el modulo del lado oeste. La superficie

total del área de dispersión será de aproximadamente **79.917 m** **[2]**, según los resultados del modelo

Depomod.

LF - 1256 8

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**Figura 2.** Ubicación de los módulos de cultivo y batimetría de la concesión.

**Fuente:** elaboración propia.

LF - 1256 9

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**Figura 3.** Ubicación de los módulos de cultivo en relación a la concesión, incorporando el área de dispersión del proyecto.
**Fuente:** elaboración propia.

LF - 1256 10

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**4.2.** **Cálculo del Índice de Impacto**

La Figura 4 entrega el gráfico de cajas con los datos obtenidos según el modelo y un análisis de

frecuencias. Se puede observar que los valores obtenidos por el modelo, tienden agruparse en su

mayoría en alrededor de 800 g C/m [2] /año, con frecuencias mucho menores en concentraciones mas

altas.

**Figura 4.-** A) Gráfico de cajas y B) Gráfica de frecuencias para los datos de salida del Modelo.

**Fuente:** elaboración propia.

LF - 1256 11

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

De esta manera la Tabla 2 entrega el resumen de los cálculos realizados con los datos entregados por

el modelo Depomod, aplicando la ecuación de Findlay y Watling (1997). Considerando el valor

máximo promedio de carbono depositado, el índice de impacto da como resultado **6,4**, por lo que la

demanda de oxígeno en el fondo no superará las oferta del medio, en relación a la producción

planteada. En este sentido, un factor primordial en el equilibrio del sistema, son las altas magnitudes

de corrientes presentes a 1 m del fondo, las cuales alcanzan en cuadratura una velocidad de 5,8 cm/s.

**Tabla 2.-** Resultados según el modelo.

|Variable|Valor|Unidades|
|---|---|---|
|**Índice de Impacto Promedio depositación **|**5,8 **|-|
|**Demanda Promedio Oxígeno **|**215,8 **|**mmol x m2 x día **|
|Oferta de Oxígeno del medio|1248,2|mmol x m2 x día|
|**Depositación Promedio de COT **|**1524,1 **|**g C x m2 x año **|

Los resultados expuestos en el informe consideran una condición hipotéticamente extrema,

asumiendo que el comportamiento de las corrientes en cuadratura se mantiene a lo largo de todo el

ciclo productivo, al igual que la cantidad de alimento suministrado a las jaulas (cantidad de alimento

considerando la máxima biomasa). Por lo tanto, al considerar una mayor magnitud de las corrientes,

es decir, con un ciclo lunar completo (sicigia y cuadratura), el área de sedimentación aumenta y por

consiguiente, la concentración de carbono debería disminuir, mejorando la degradación natural de

este material orgánico en el fondo, según lo expresado por Hevia _et al._ [9] (1996).

9 Hevia M., H. Rosenthal & R.J. Gowen.1996.Modelling Benthic Deposition under Fish Cages.Journal Appl. Ichthyol.
12:71-74.

LF - 1256 12

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

Estimación del área de dispersión a través de un modelo de trayectoria de partículas - CES Isla Transito SW

**5.** **CONCLUSIÓN**

Considerando los antecedentes expuestos, tomando en cuenta los datos del proyecto técnico y la

información levantada en la CPS, las predicciones del modelo permiten concluir que el proyecto no

generará efectos ambientales y ecológicos significativos sobre los recursos naturales presentes en el

área de dispersión de fecas y alimento no consumido, debido a que el sedimento mantendrá las

condiciones aeróbicas al culminar su ciclo productivo.

Lo cual se sustenta en:

 - El área de dispersión calculada del proyecto junto con el resto de la información que se

presenta al Sistema de Evaluación Ambiental, está circunscrita a un área localizada

mayoritariamente bajo la concesión, en condición de corrientes medidas en cuadratura

(menores magnitudes).

 - De acuerdo a los balances expuestos: cantidad de alimento suministrado, correntometría (en

cuadratura) y ubicación de jaulas, la capacidad de carga de la demanda de oxígeno del lugar,

no se verá sobrepasada, en cuanto a la demanda de oxigeno del lugar.

LF - 1256 13

Los contenidos que soporta el presente documento constituyen Propiedad Intelectual.
Queda prohibido su reproducción, total o parcial, por cualquier medio, en forma íntegra o extractada.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Información de entrada del modelo Depomod.**

| Módulo Depomod | Variable | Observaciones |
| --- | --- | --- |
| **Grid Generation ** | Batimetría | Extraída del plano batimétrico |
| **Grid Generation ** | Ubicación Módulos | Extraída del plano batimétrico |
| **Particle Tracking ** | Corrientes4 5 | CPS, analizando 5 capas de la columna. |
| **Particle Tracking ** | Velocidad Fecas | 0,032 m/s, según Gowen and Bradbury (1987) |
| **Particle Tracking ** | Velocidad ANC | 0,128 m/s para un tamaño de pellet de 9200um |
| **Particle Tracking ** | Agua en el pellet | 9% |
| **Particle Tracking ** | Digestibilidad del pellet | 85% |
| **Particle Tracking ** | Perdida de alimento | 5% |
| **Particle Tracking ** | Carbono en el Pellet | 46% |
| **Particle Tracking ** | Carbono en las Fecas | 30% |
| **Particle Tracking ** | Numero de estructuras | Proyecto Técnico |
| **Particle Tracking ** | Dimensiones estructuras | Proyecto Técnico |
| **Particle Tracking ** | Alimento por jaula | Factor de conversión de 1,2 |
| **Resuspensión ** | No se aplicó | Sólo utilizada para obtener los resultados de Carbono<br>(g/m2/día) |

**Tabla 2.-: ** Resultados según el modelo.**

| Variable | Valor | Unidades |
| --- | --- | --- |
| **Índice de Impacto Promedio depositación ** | **5,8 ** | - |
| **Demanda Promedio Oxígeno ** | **215,8 ** | **mmol x m2 x día ** |
| Oferta de Oxígeno del medio | 1248,2 | mmol x m2 x día |
| **Depositación Promedio de COT ** | **1524,1 ** | **g C x m2 x año ** |
