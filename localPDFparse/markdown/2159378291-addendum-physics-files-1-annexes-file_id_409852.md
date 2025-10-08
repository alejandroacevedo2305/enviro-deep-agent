---
title: Sin título
author: Aldo Hernández
date: D:20231212161411-03'00'
language: es
type: report
pages: 25
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE MODELACIÓN DE LA PLUMA DE DESCARGA
-->

# ESTUDIO DE MODELACIÓN DE LA PLUMA DE DESCARGA

### Proyecto “Ampliación de la planta elaboradora de productos congelados”, sector San José comuna de Calbuco, Región de Los Lagos

## Requirente: Salmones Camanchaca S.A.

Concepción, diciembre de 2023

**EQUIPO DE TRABAJO**

**Aldo Hernández** Jefe de Proyecto

Coordinación de proyecto
**Daniela Henríquez**

Modelación

Biólogo Marino
Dr. Manejo Recursos
Acuáticos Renovables

Bióloga Marina
MSc. en Oceanografía

_Análisis de corrientes_

_Revisión y edición informe_

_Modelación Visual Plumes_

_Elaboración de informe_

Holon SpA. 2023. Estudio de modelación de la pluma de descarga. Proyecto “Ampliación de la

planta elaboradora de productos congelados”, sector San José comuna de Calbuco, Región de

Los Lagos. Salmones Camanchaca S.A. 22 pp.

i

**TABLA DE CONTENIDO**

**1** **INTRODUCCIÓN ................................................................................................................... 1**

**2** **OBJETIVO ............................................................................................................................ 3**

**3** **MATERIALES Y MÉTODO ................................................................................................... 3**

3.1 Á REA DE ESTUDIO ........................................................................................................................... 3

3.2 I NFORMACIÓN DE CAMPO ................................................................................................................. 4

3.3 P ROCESAMIENTO DE LA INFORMACIÓN ............................................................................................. 4

3.4 M ODELACIÓN DE LA DESCARGA ........................................................................................................ 5

3.4.1 Data de entrada a la modelación ...................................................................................................... 5

3.4.2 Modelación mediante Visual Plumes ................................................................................................ 6

**4** **RESULTADOS ...................................................................................................................... 7**

4.1 M ODELACIÓN DE LA DESCARGA MEDIANTE V ISUAL P LUMES .............................................................. 7

4.2 A NÁLISIS DE DILUCIÓN DE LAS PLUMAS MODELADAS ........................................................................ 19

**5** **CONCLUSIONES ................................................................................................................ 21**

**6** **REFERENCIAS ................................................................................................................... 22**

ii

**1** **INTRODUCCIÓN**

La modelación de las descargas ambientales representa una clase de diseños orientados a

determinar el grado de dilución de un efluente, cerca del punto de descarga (Lee & Chu, 2003).

La densidad del efluente determina el comportamiento de la pluma, pudiendo ser ascendente

cuando la densidad del efluente es menor que la densidad de la columna de agua del medio

receptor, o descendente cuando la densidad de la descarga es mayor a la del medio (Inan, 2018).

La hidrodinámica de un efluente que se descarga continuamente en un cuerpo de agua receptor

puede conceptualizarse como un proceso de mezcla que ocurre en dos regiones separadas. En

la primera región, las características iniciales del chorro de flujo de momento, flujo de flotabilidad

y geometría de descarga influyen en la trayectoria y la mezcla del chorro. Esta región se denomina

"campo cercano" y abarca el flujo de chorro flotante y cualquier interacción de la superficie, el

fondo o la capa terminal. A medida que la pluma turbulenta se aleja más de la fuente, las

características de la descarga se vuelven menos importantes, haciendo que las condiciones

advectivas del entorno controlen la trayectoria y la dilución de la columna turbulenta, a través de

movimientos de propagación flotantes y difusión pasiva, o "campo lejano" (Dokener & Jirka,

2007).

Una comprensión integral de los procesos de mezcla inicial hidrodinámica, incluidas las

interacciones de borde de las aguas residuales, es un requisito relevante para controlar las

descargas de aguas residuales y minimizar el impacto en el medio ambiente acuático. Las

investigaciones orientadas mejorar la comprensión del comportamiento de mezcla inicial de las

descargas de efluentes a través de estudios experimentales, han conducido al desarrollo de

modelos matemáticos semiempíricos, tales como Visual Plumes (Frick et al. 2003) VISJET

(Cheung et al. 2000) y CORMIX (Jirka et al. 1996). Estos modelos (denominados modelos de

plumas) predicen las trayectorias de la columna de estado estable hasta la finalización de la

dilución inicial cerca de la profundidad de atrapamiento de la pluma o cuando la pluma llega a la

superficie, con base en la simplificación analítica de fenómenos de mezcla turbulentos complejos,

y no siempre pueden proporcionar detalles de la hidrodinámica tridimensional en la zona de

mezcla inicial (Tang et al. 2008).

1

Con base en estas consideraciones, para el caso de la modelación de la pluma de descarga del

emisario de Salmones Camanchaca S.A, se ha considerado el empleo del modelo UM3 de Visual

Plumes (Frick et al. 2005) para la modelación de la pluma de descarga del efluente.

Los resultados del estudio de modelación han sido desarrollados en el marco del Proyecto

“Ampliación de la planta elaboradora de productos congelados”, sector San José comuna de

Calbuco, Región de Los Lagos, cuyo titular es Salmones Camanchaca S.A.

El análisis que se entrega se encuentra orientado a la evaluación de la modelación de la pluma

de descarga, considerando los escenarios de fase lunar de sicigia y cuadratura en mareas

llenante y vaciante.

2

**2** **OBJETIVO**

Evaluar el comportamiento de la pluma de descarga del emisario de Salmones Camanchaca S.A.,

mediante la aplicación de herramientas numéricas e información secundaria, bajo escenarios de

fase lunar de sicigia y cuadratura en mareas llenante y vaciante.

**3** **MATERIALES Y MÉTODO**

3.1 Área de estudio

El área de estudio del proyecto se ubica en el sector de San José, ubicada a 5 km al weste de la

localidad de Calbuco, Región de Los Lagos. El emisario realiza su trazado perpendicular a línea

de costa hasta una profundidad de 29,1 m referido al nivel medio del mar ( **Figura 1** ).

**Figura 1.** Ubicación espacial de punto de descarga de emisario de Salmones Camanchaca S.A.
en sector Calbuco, Región de Los Lagos. Coordenadas en UTM. Datum WGS84, Huso 18G.

3

3.2 Información de campo

Con el objetivo de evaluar la pluma de descarga del emisario, se obtuvo información de campo

de la dinámica de corrientes euleriana, la cual fue extraída del “Estudio de Dinámica costera:

Correntometría lagrangiana y Euleriana” de SALMONES CAMANCHACA S.A., debido a que la

base de datos cubre toda la columna de agua. Para esto, se consideraron las mediciones

obtenidas con el anclaje ADCP fondeado en las cercanías del sistema de descarga.

Adicionalmente, para evaluar el efecto de las mareas sobre las corrientes dentro del área de

estudio, se obtuvo información secundaria de mareas, extraída desde la plataforma del SHOA,

considerando los días donde se observó condiciones de sicigia y cuadratura lunar (ver informe

de dinámica costera).

3.3 Procesamiento de la información

A partir de la evaluación integrada de los resultados del análisis estadístico de corrientes y

mareas, se determinaron escenarios contrastantes que representan la mayor variabilidad del

cuerpo de agua, los cuales fueron utilizados como datos de entrada para la modelación de la

pluma de descarga ( **Tabla 1** ). Estos escenarios fueron seleccionados considerando la situación

más desfavorable en términos oceanográficos, vale decir, donde se registra la máxima y mínima

variabilidad de la serie de tiempo mareal entregada en la información de campo (sensor de

presión de equipo ADCP) e información secundaria (altura de marea de plataforma del SHOA),

considerando lo indicado en las Instrucciones Oceanográficas No2 “Método Oficial para el Cálculo

de los valores Armónicos de la Marea” del del SHOA (SHOA,1999).

**Tabla 1.** Escenarios de modelación propuestos para la dinámica de corrientes en la zona de
estudio. Extraído de Estudio de dinámica costera de Salmones Camanchaca S.A.

**Cuadratura** **Sicigia**

**Vaciante** **Llenante** **Vaciante** **Llenante**

**Estrato** **Variable** **Unidad**

27-05-23 09:10 27-05-23 14:40 20-06-04 15:00 20-06-04 21:50

Superficie Dirección grados-N 301,36 32,47 273,79 211,08

4.8 m Velocidad cm/s 5,55 8,46 5,41 40,86

Medio Dirección grados-N 299,19 63,33 278,03 354,36

12.8 m Velocidad cm/s 6,65 1,58 0,7 3,81

Fondo Dirección grados-N 266,09 194,37 185,5 58,74

24.8 m Velocidad cm/s 5,32 0,91 6,81 9,95

4

3.4 Modelación de la descarga

_3.4.1 Data de entrada a la modelación_

Los datos de entrada a la modelación se resumen en las **Tablas 2** a **4** . En las cuales se entregan

las características del sistema de descarga ( **Tabla 2** ) y las características del efluente ( **Tabla 3** ),

considerando como parámetros clave los sólidos suspendidos totales (SST), demanda biológica

de oxígeno (DBO 5 ), nitrógeno total Kjendalh (NTK) y fósforo total (PT), utilizando como

concentración de descarga los valores establecidos en la Tabla 5 del DS90 y de resultados del

balance del sistema de descarga de SALMONES CAMANCHACA S.A., efectuado durante el mes

de octubre 2023. En la **Tabla 4** se entregan las características del cuerpo receptor, utilizando

como valores de referencia precautorios, los valores mínimos observados en la estación control

Programa de Vigilancia Ambiental “Planta de Procesos Primarios San José” de Salmones

Camanchaca S.A, para las campañas de muestreo correspondientes al primer semestre de 2021

y 2022.

Con estos antecedentes, se efectuó la estimación de la distancia en la cual la pluma de descarga

alcanza la concentración del medio receptor ( **Tabla 4** ), considerando como valores de descarga

las concentraciones de los contaminantes indicadas en la Tabla 5 del DS90 y de resultados del

Programa de Vigilancia Ambiental de Salmones Camanchaca S.A., campañas del primer

semestre de 2021 y 2022 (ver **Tabla 3** ). Adicionalmente, se estimó la distancia a la cual la

descarga alcanza las concentraciones indicadas en la Tabla 4 del DS90 (concentraciones dentro

de la Zona de Protección Litoral), a saber: 100 mg/l de SST, 60 mg/l para DBO5, 50 mg/l para

NTK y 5 mg/l para PT en áreas aptas para la acuicultura.

**Tabla 2.** Características del sistema de descarga del efluente utilizadas en la modelación.

**SISTEMA DE DESCARGA**

Número de portas 20
Diámetro externo difusor 355 mm

Grosor del tubo 13,6 mm

Caudal máximo 649 m3/hora

Profundidad emisario 29,1 m
Largo del difusor 15 m
Diámetro de la porta 0,1 m
Altura de la porta 0,1016 m
Espaciamiento entre portas 0,75 m

5

**Tabla 3.** Características del sistema de efluente utilizadas en la modelación. SST: Sólidos
Suspendidos Totales, DBO 5 : Demanda Biológica de Oxígeno; NTK: Nitrógeno Total Kjendahl; PT:
Fósforo Total. Concentraciones corresponden a los límites de las Tabla 5 del DS90 y resultados
PVA Campaña enero 2022.

**EFLUENTE**

Concentración de SST 300 mg/l
Concentración de DBO 5 138 mg/l
Concentración de NTK 13 mg/l
Concentración de PT 4 mg/l
Temperatura promedio 23 oC
Salinidad promedio 37 PSU
Densidad promedio 1.025 kg/m [3]

**Tabla 4.** Características del cuerpo de agua receptor utilizadas en la modelación. SST: Sólidos
Suspendidos Totales, DBO5: Demanda Biológica de Oxígeno; NTK: Nitrógeno Total Kjendahl;
PT: Fósforo Total.

**MEDIO RECEPTOR**

Concentración de SST 19,3 mg/l
Concentración de DBO 5 1 mg/l
Concentración de NTK 0,8 mg/l
Concentración de PT 0,1 mg/l
Temperatura promedio 13,2 oC
Salinidad promedio 33,2 PSU
Densidad promedio 1.025 kg/m [3 ]

_3.4.2 Modelación mediante Visual Plumes_

Para la modelación inicial de la pluma de descarga se utilizó el programa Visual Plumes (VP)

v1.0, desarrollado la Agencia de Protección Ambiental de Estados Unidos (USEPA). El software

incorpora modelos que tienen la capacidad de simular plumas sumergidas con descargas simples

y con múltiples difusores en un ambiente estratificado, además de descargas boyantes en

superficie, considerando las condiciones ambientales del medio receptor.

En el caso particular de la modelación que se presenta, se utilizó el módulo denominado UM3

(Three Dimensional Update Merge), el cual desarrolla una aproximación de tipo lagrangiana que

simula una descarga por medio de uno o más difusores, en función de las características de la

6

descarga y del medio ambiente, permitiendo describir el comportamiento de la pluma en términos

de profundidad y en el espacio (Frick et al., 2003).

El modelo UM3 se caracteriza de tres puntos importantes para resolver el comportamiento de la

descarga en el medio receptor:

 Hipótesis del área proyectada del PAE (Projected Area Entrainment), la cual cuantifica la

fuerza (Rawn et al., 1960).

 - Tasa en que la masa de la pluma es incorporada a la corriente, asumiendo que la pluma

se encuentra en estado estacionario y,

 Formulación lagrangiana, que implica que sucesivos elementos siguen la misma

trayectoria (Baumgartner et al., 1994).

**4** **RESULTADOS**

4.1 Modelación de la descarga mediante Visual Plumes

En las **Figuras 2**, **3** y **4** se entrega el resultado de la modelación en Visual Plumes (Modelo UM3)

para SST utilizando como datos de entrada los indicados en las **Tablas 2**, **3** y **4.**

En términos generales, la modelación de SST arroja plumas en dirección fuera de la costa en

todos los escenarios, destacando la modelación en escenario de cuadratura-llenante y sicigia

vaciante, donde las plumas toman una dirección S-SSW, mientras que, en los escenarios de

cuadratura-vaciante y sicigia-llenante, las direcciones de las plumas se orientan hacia el W y E,

respectivamente ( **Figura 2** ).

7

**Figura 2.** Vista superior (Plan View) resultado de la modelación VISUAL PLUMES UM3 para SST
en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d) Sicigiallenante.

La vista lateral de las plumas ( **Figura 3** ), permite observar con mayor claridad la longitud de éstas,

observándose, en la mayoría de los escenarios modelados longitudes similares, las que no

superan los 10 metros, excepto en sicigia-llenante, donde la pluma no supera los 5 metros de

longitud. En todos los casos, las plumas se mantienen en el fondo, hasta llegar a profundidades

entre 25 y 20 metros.

8

**Figura 3.** Vista lateral (Plume Elevation) resultado de la modelación VISUAL PLUMES UM3 para
SST en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d)
Sicigia-llenante.

El análisis de las diluciones ( **Figura 4** ) permite observar que, en todos los escenarios, la dilución

al cuerpo receptor (dilución 15.5: 300 mg/l en la descarga _vs_ 19,3 mg/l en el cuerpo receptor) se

alcanza al nivel máximo de la longitud de las plumas, que para SST corresponde a longitudes

que oscilaron entre 5 y 10 metros. La dilución de la Tabla 4 del DS90 (dilución 3: 300 mg/l en la

descarga _vs_ 100 mg/l en Tabla 4) se alcanza a una distancia inferior a 1 m desde la descarga en

todos los escenarios.

9

**Figura 4.** Predicción de la dilución (Plumes Dilution Prediction) resultado de la modelación
VISUAL PLUMES UM3 para SST en 4 escenarios. a) Cuadratura-vaciante; b) Cuadraturallenante; c) Sicigia-vaciante; d) Sicigia-llenante.

En las **Figuras 5**, **6** y **7** se entrega el resultado de la modelación en Visual Plumes (Modelo UM3)

para DBO 5, utilizando como datos de entrada los indicados en las **Tablas 2**, **3** y **4** .

En términos generales, la modelación de DBO 5 arroja plumas en dirección fuera de la costa para

todos los escenarios, mostrando diferencias en la orientación de las plumas, donde destaca el

escenario cuadratura-vaciante una dirección W ( **Figura 5a** ), escenario cuadratura-llenante una

dirección S-SE ( **Figura 5b** ), mientras que los escenarios de sicigia-vaciante ( **Figura 5c** ) y sicigia

llenante ( **Figura 5d** ) mostraron una dirección SSW y E, respectivamente.

10

**Figura 5.** Vista superior (Plan View) resultado de la modelación VISUAL PLUMES UM3 para
DBO 5 en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d)
Sicigia-llenante.

La vista lateral de las plumas ( **Figura 6** ), permite observar con mayor claridad la longitud de éstas,

observándose que las plumas modeladas, en la mayoría de los escenarios alcanzan una longitud

de 45 metros, excepto en el escenario de cuadratura-llenante ( **Figura 6b** ), donde alcanza una

longitud cercana a los 15 metros. En la mayoría de los casos las plumas cubren hasta los 15

metros de profundidad, excepto en el escenario de sicigia-llenante ( **Figura 5d** ), donde la pluma

se mantiene en el fondo.

11

**Figura 6.** Vista lateral (Plume Elevation) resultado de la modelación VISUAL PLUMES UM3 para
DBO 5 en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d)
Sicigia-llenante.

El análisis de las diluciones ( **Figura 7** ) permite observar que, en todos los escenarios, la dilución

al cuerpo receptor (dilución 138:138 mg/l en la descarga _vs_ 1 mg/l en el cuerpo receptor) se

alcanza, en la mayoría de los escenarios, al nivel máximo de la longitud de las plumas, que para

DBO 5 oscila entre 10 y 45 metros. La dilución a la Tabla 4 del DS90 (dilución 2,3: 138 mg/l en la

descarga _vs_ 60 mg/l en Tabla 4) se alcanza a una distancia cercana a 1 m desde la descarga en

todos los escenarios.

12

**Figura 7.** Predicción de la dilución (Plumes Dilution Prediction) resultado de la modelación
VISUAL PLUMES UM3 para DBO 5 en 4 escenarios. a) Sicigia-vaciante; b) Sicigia-llenante; c)
Cuadratura-vaciante; a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d)
Sicigia-llenante.

En las **Figuras 8**, **9** y **10** se entrega el resultado de la modelación en Visual Plumes (Modelo

UM3) para NTK utilizando como datos de entrada los indicados en las **Tablas 2**, **3** y **4** .

En términos generales, la modelación de NTK arroja plumas orientadas en dirección fuera de la

costa para todos los escenarios, destacando diferencias entre escenarios, con dirección W y S

SSW en condiciones de cuadratura-vaciante ( **Figura 8a** ) y cuadratura-llenante ( **Figura 8b** ),

respectivamente; mientras que en condiciones de sicigia-llenante ( **Figura 8c** ) y sicigia-vaciante

( **Figura 8d** ), las plumas se orientaron hacia el S y E, respectivamente.

13

**Figura 8.** Vista superior (Plan View) resultado de la modelación VISUAL PLUMES UM3 para NTK
en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d) Sicigiallenante.

La vista lateral de las plumas ( **Figura 9** ), permite observar con mayor claridad la longitud de éstas,
observándose que la mayoría de las plumas modeladas presentaron longitudes cercanas a los
10 metros, excepto en el escenario de sicigia-llenante ( **Figura 9d** ), donde alcanzó una longitud
de 5 metros. En todos los casos, las plumas se mantuvieron en el fondo de la columna de agua,
alcanzando profundidades entre 25 y 20 metros.

14

**Figura 9.** Vista lateral (Plume Elevation) resultado de la modelación VISUAL PLUMES UM3 para
NTK en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d)
Sicigia-llenante.

El análisis de las diluciones ( **Figura 10** ) permite observar que, en todos los escenarios, la dilución

al cuerpo receptor (dilución 16,9: 13 mg/l en la descarga _vs_ 0,77 mg/l en el cuerpo receptor) se

alcanza al nivel máximo de la longitud de las plumas, que para NTK oscila entre 5 y 10 metros.

La dilución a la Tabla 4 del DS90 (dilución 0,26: 13 mg/l en la descarga _vs_ 50 mg/l en Tabla 4) se

alcanza a una distancia inferior a 1 m desde la descarga en todos los escenarios.

15

**Figura 10.** Predicción de la dilución (Plumes Dilution Prediction) resultado de la modelación
VISUAL PLUMES UM3 para NTK en 4 escenarios. a) Cuadratura-vaciante; b) Cuadraturallenante; c) Sicigia-vaciante; d) Sicigia-llenante.

En las **Figuras 11**, **12** y **13** se entrega el resultado de la modelación en Visual Plumes (Modelo

UM3) para PT utilizando como datos de entrada los indicados en las **Tablas 2**, **3** y **4** .

En términos generales, la modelación de PT arroja plumas en dirección fuera de la costa para

todos los escenarios, registrando diferencias en todos los escenarios modelados, con dirección

W y S-SSE en condiciones de cuadratura-vaciante ( **Figura 11a** ) y cuadratura-llenante ( **Figura**

**11b** ), respectivamente; mientras que en condiciones de sicigia-llenante ( **Figura 11c** ) y sicigia

vaciante ( **Figura 11d** ), las plumas se orientaron hacia el S y E-NE, respectivamente.

16

**Figura 11.** Vista superior (Plan View) resultado de la modelación VISUAL PLUMES UM3 para PT
en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d) Sicigiallenante.

La vista lateral de las plumas ( **Figura 12** ), permite observar con mayor claridad la longitud de
éstas, observándose que las plumas modeladas en los escenarios de marea vaciante ( **Figuras**
**12a, 12c** ) presentaron longitudes cercanas a los 35 metros, y se mantuvieron en el fondo, hasta
llegar a profundidades de 20 metros, mientras que el escenario de sicigia-vaciante ( **Figura 12d** )
alcanzó longitudes levemente menores (30 metros), y se mantuvo totalmente en el fondo de la
columna de agua. Las plumas más cortas se alcanzaron en el escenario de sicigia-llenante
( **Figura 12b** ), con longitudes cercanas a 15 metros, elevándose hasta estratos medios, alrededor
de los 15 metros de profundidad.

17

**Figura 12.** Vista lateral (Plume Elavation) resultado de la modelación VISUAL PLUMES UM3 para
PT en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante; c) Sicigia-vaciante; d)
Sicigia-llenante.

El análisis de las diluciones ( **Figura 13** ) permite observar que, en todos los escenarios, la dilución

al cuerpo receptor (dilución 78,4: 4 mg/l en la descarga _vs_ 0,051 mg/l en el cuerpo receptor) se

alcanza al nivel máximo de la longitud de las plumas, que para PT oscila entre 12 y 35 metros.

La dilución a la Tabla 4 del DS90 (dilución 0,8: 4 mg/l en la descarga _vs_ 5 mg/l en Tabla 4) se

alcanza a una distancia inferior a 1 m desde la descarga en todos los escenarios.

18

**Figura 13.** Predicción de la dilución (Plumes Dilution Prediction) resultado de la modelación
VISUAL PLUMES UM3 para PT en 4 escenarios. a) Cuadratura-vaciante; b) Cuadratura-llenante;
c) Sicigia-vaciante; d) Sicigia-llenante.

4.2 Análisis de dilución de las plumas modeladas

En la **Figura 14** se entrega el análisis de la dilución de las plumas modeladas en un plano

bidimensional elaborado en ArcGIS Pro que incluye una estimación de la ZPL que, para el área

de estudio, corresponde a 30 desde la línea de bajamar. Para este resultado se han proyectado

las longitudes de las plumas modeladas en torno al sistema de difusores de la descarga (línea

roja). En naranjo se entrega la dilución para Sólidos Suspendidos Totales (SST), que fue estimada

en 5 m para alcanzar las concentraciones del cuerpo receptor, lo que representa la pluma

modelada de menor tamaño. En amarillo se entrega la dilución para DBO5, que fue estimada en

45 m para alcanzar las concentraciones del cuerpo receptor, que representa la pluma modelada

de mayor tamaño o escenario más desfavorable. En ambos casos, las diluciones para alcanzar

los niveles de la Tabla 4 del DS90 resultaron inferiores a 1 m.

19

**Figura 14.** Representación cartográfica de la extensión de las plumas modeladas para SST
(naranjo) y DBO5 (amarillo) con base en los datos de dinámica de corrientes de mayo de 2023.

20

**5** **CONCLUSIONES**

Los resultados de la modelación mediante Visual Plumes UM3 indicaron que, para el caso de

SST y en todos los escenarios modelados, la pluma tiende a mantenerse cerca del fondo (hasta

20 metros), alcanzando longitudes máximas de 10 metros, con diferencias en la orientación de

las plumas.

Para DBO 5 las plumas modeladas con Visual Plumes alcanzaron longitudes máximas de 45

metros, excepto en el escenario de cuadratura-llenante, donde alcanza una longitud cercana a

los 15 metros. En la mayoría de los casos las plumas cubren hasta los 15 metros de profundidad,

excepto en el escenario de sicigia-llenante, donde la pluma se mantiene en el fondo., y con

diferencias en la dirección de las plumas (cuadratura-vaciante una dirección W; cuadratura

llenante una dirección S-SE; sicigia-vaciante hacia el SSW; y sicigia-llenante hacia el E).

Para el NTK, las plumas modeladas con Visual Plumes alcanzaron longitudes cercanas a los 10

metros, manteniéndose en el fondo de la columna de agua, alcanzando profundidades entre 25

y 20 metros; y con diferencias en la orientación de las plumas (cuadratura-vaciante una dirección

W; cuadratura-llenante una dirección S-SW; sicigia-vaciante hacia el S; y sicigia-llenante hacia el

E).

Para fósforo total (PT) las plumas modeladas con Visual Plumes alcanzaron longitudes entre 15

y 35 metros, manteniéndose en estratos profundos de la columna de agua, excepto en el

escenario de sicigia donde alcanza estratos medios (15 metros), y con diferencias en la

orientación de las plumas (cuadratura-vaciante una dirección W; cuadratura-llenante una

dirección S-SE; sicigia-vaciante hacia el S; y sicigia-llenante hacia el E-NE).

El análisis de dilución de las plumas modeladas arrojó que la dilución al cuerpo receptor se estima

en 5 metros para SST, lo que representa la pluma de menor tamaño, y de 45 metros para DBO5,

lo que representa la pluma de mayor tamaño o escenario más desfavorable. En ambos casos,

las diluciones para alcanzar los niveles de la Tabla 4 del DS90 resultaron inferiores a 1 m.

21

**6** **REFERENCIAS**

**Cheung, S.K.B., D.Y.L. Leung, W. Wang, J.H.W. Lee & V. Cheung, V. 2000.** VISJET-a
computer ocean outfall modelling system. Proceedings Computer Graphics International 2000.
doi:10.1109/cgi.2000.852322

**Dokener, R.L. & G. Jirka. 2007.** CORMIX User Manual. A Hydrodynamic Mixing Zone Model and
Decision Support System for Pollutant Discharges into Surface Waters. U.S. Environmental
Protection Agency. 206 pp.

**Frick, W. E., Roberts, P. J. W., Davis, L. R., Keyes, J., Baumgartner, D. J., & George, K. P.**
**2003.** Dilution Models for Effluent Discharges,4th Edition (Visual Plumes). U.S. Environmental

Protection.

**Frick, W. E., D. Baumgartner, L. Davis, Z. Ge, K, George, P. Roberts. 2005.** Visual Plumes
2005. Model Update Documentation. U.S. Environmental Protection Agency. 90 pp.

**Inan, A. 2018.** Modeling of Hydrodynamics and Dilution in Coastal Waters. Water 2019, 11, 83;
doi:10.3390/w11010083.

**Jirka, G. H., R. L. Doneker & S.W. Hinton. 1996.** “MANUAL FOR CORMIX: A Hydrodynamic
Mixing Zone Model and Decision Support System for Pollutant Discharges into Surface Waters”.
U.S.EPA, Office of Science and Technology, Washington.

**Lee J. H. & V.H. Chu. 2003.** Turbulent Jets and Plumes: A Lagrangian Approach. Kluwer
Academic Publishers. Springer. U.S.A. 389 pp.

**SHOA. 1999.** Instrucciones Oceanográficas No2. Método oficial para el cálculo de los valores no
armónicos de las mareas. 2da. Edición. Armada de Chile. 26pp.

**Tang, H.S., J. Paik, F. Sotiropoulos & T. Khangaonkar. 2008.** Three-Dimensional Numerical
Modeling of Initial Mixing of Thermal Discharges at Real-Life Configurations. Journal of Hydraulic
Engineering, 134(9), 1210-1224. doi:10.1061/(asce)0733-9429(2008)134:9(1210)

22