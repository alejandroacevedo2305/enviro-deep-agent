---
title: Depomod Reñihue 2015
author: KarenGonzález
date: D:20150429192135-03'00'
language: es
type: report
pages: 11
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME TÉCNICO
-->

# INFORME TÉCNICO

**Modelación Capacidad de Carga mediando DEPOMOD**

**Elaborado por:**

**DEPARTAMENTO MEDIOAMBIENTE**

**ABRIL 2015**

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

**TABLA DE CONTENIDO**

**1- INTRODUCCIÓN** **............................................................................................................................. 3**

**2- METODOLOGÍA** **............................................................................................................................. 4**

**2.1.** **A** **NTECEDENTES** **P** **RODUCTIVOS** **....................................................................................................... 4**

**2.2.** **A** **NTECENDENTES MEDIOAMBIENTALES** **............................................................................................. 4**

**2.3.** **A** **NTECENDENTES MODELO** **............................................................................................................. 5**

**3- RESULTADOS** **................................................................................................................................... 7**

**4.- DISCUSIÓN Y CONCLUSIÓN** **...................................................................................................... 10**

**5.- REFERENCIAS BIBLIOGRÁFICAS** **................................................................................................. 11**

2

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

Los sedimentos tienen una importante función reguladora en el ecosistema acuatíco
debido a la gran capacidad de almacenaje de materia orgánica y, por lo tanto, de
nutrientes. Ellos afectan el balance de oxígeno de las aguas de fondo y permiten la
renovación o liberación de nutrientres nuevos hacia la columna de agua, lo que
finalmente también afecta a la producción de fitoplancton (Jorgensen, 1996). Por otra
parte, se debe tener presente, que en los sedimentos existe una alta tasa de metabolismo
microbial, el que dependiendo de la cantidad de materia orgánica acumulada y de la
tasa de ventilación puede provocar condiciones de hipoxia o anoxia en los sedimentos y
en los estratos suprayacentes de la columna de agua (Libes, 1992; Silva, 1999).

La legislación Chilena, reglamenta a través del decreto supremo n° 320 del 14 de
Diciembre de 2001, en su artículo N°3 que “ _Para los efectos del presente reglamento,_
_constituyen instrumentos para la conservación y evaluación de las capacidades de los_
_cuerpos de agua, los requisitos de operación previstos en las normas generales y_
_especiales del mismo, así como la Caracterización Preliminar de Sitio y la información_
_ambiental en los casos en que resulten procedentes._
_Asimismo, para los efectos del presente reglamento, se entenderá que se supera la_
_capacidad de un cuerpo de agua cuando el área de sedimentación presente_
_condiciones anaeróbicas_ ”. Es así como la normativa permite evaluar si el sitio está
operando conforme a su capacidad de carga y con un alto nivel de certeza.

Por otra parte, hay que tener presente que la acuicultura constituye una de las
actividades económicas que ha experimentado el mayor crecimiento durante los últimos
años . Sin embargo, uno de los problemas importantes que la industria genera, es el de los
fondos marinos impactados bajo los centros de cultivos(Troncoso, 2006; Brooks, 2001)

En repuesta al problema planteado anteriormente y en base a los requerimientos del
Reglamento Ambiental para la Acuicultura (D.S. N° 32 de 2001y sus modificaciones), el
cual señala en su artículo 18 “ _Los proyectos en sectores de agua y fondo que deban_
_someterse al Sistema de Evaluación de Impacto Ambiental, sólo obtendrán el permiso_
_Ambiental Sectorial cuando se determine que la futura área de Sedimentación o el decil_
_más profundo de la columna de agua, según corresponda, presenta condiciones_
_aeróbicas. Asimismo se señala, es responsabilidad del titular que su centro opere en_
_niveles compatibles con las capacidades de los cuerpos de aguas lacustres, fluviales y/o_
_marítimos, para lo cual deberá mantener siempre condiciones aeróbicas_ ”.

Es por esto que el objetivo principal de este informe es describir el proceso de dispersión
de las partículas desechadas y /o no consumidas, es decir, carbono orgánico total
proveniente de las balsas jaulas mediante el programa de modelación DEPOMOD v2.4.1.
y de esta manera conocer el área de dispersión y sedimentación que alcanza el proceso
productivo en el fondo marino, para así, evaluar la capacidad de carga del sector y
comparar estos resultados con los parámetros de Findlay y Watling (1997). Para así cumplir
con lo reglamentado.

3

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

**2.1. ANTECEDENTES PRODUCTIVOS**

El centro Reñihue se encuentra en el estero Reñihue al sureste de Punta Puquetey, en la
comuna de Chaitén, Décima región de los Lagos.
Se proyecta ampliar la producción máxima a 5.500 toneladas de salmónidos al final del
ciclo, el cual, dependiendo de la especie a cultivar será de 12 a 18 meses. Sin embargo,
el modelo de sedimentación se realizó considerando un input de alimento en un ciclo de
18 meses. En la tabla 1 se presentan los valores productivos para el programa DEPOMOD
v2.4.1.

Tabla 1: Datos productivos con los cuales se alimenta el programa de modelación.

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ciclo, el cual, dependiendo de la especie a cultivar será de 12 a 18 meses. Sin embargo, el modelo de sedimentación se realizó considerando un input de alimento en un ciclo de 18 meses. En la tabla 1 se presentan los valores productivos para el programa DEPOMOD v2.4.1. -->

**Tabla 1: Datos productivos con los cuales se alimenta el programa de modelación.**

| ITEM | VALOR | UNIDAD |
| --- | --- | --- |
| **Número de Jaulas** | 24 | Unidad |
| **Dimensiones de Jaulas** | 30x30x20 | M3 |
| **Tipo de jaulas** | Rectangular | - |
| **Ciclo Productivo** | 18 | Meses |
| **Producción** | 5500 | Toneladas |
| **Factor de Conversión** | 1.2 | - |
| **Total Alimento Suministrado** | 6471 | Toneladas |
| **Tasa de Alimentación** | 492 | Kg/Jaula/Día |
| **Profundidad del sector** | 279 | metros |
| **Velocidad prom. Capa superior** | 18 | cm/s |
| **Velocidad prom. Capas medias** | 7.1-5.8-5.6 | cm/s |
| **Velocidad prom. Capa fondo** | 5.2 | cm/s |

<!-- Estadísticas: 12 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **2.2. ANTECENDENTES MEDIOAMBIENTALES** - _Batimetría_ : La medición de la profundidad se realizó el 24 de Febrero del presente año, mediante un Ecosonda marca Garmin, modelo527 xs (profundidad máxima -->
<!-- FIN TABLA 1 -->


|ITEM|VALOR|UNIDAD|
|---|---|---|
|**Número de Jaulas**|24|Unidad|
|**Dimensiones de Jaulas**|30x30x20|M3|
|**Tipo de jaulas**|Rectangular|-|
|**Ciclo Productivo**|18|Meses|
|**Producción**|5500|Toneladas|
|**Factor de Conversión**|1.2|-|
|**Total Alimento Suministrado**|6471|Toneladas|
|**Tasa de Alimentación**|492|Kg/Jaula/Día|
|**Profundidad del sector**|279|metros|
|**Velocidad prom. Capa superior**|18|cm/s|
|**Velocidad prom. Capas medias**|7.1-5.8-5.6|cm/s|
|**Velocidad prom. Capa fondo**|5.2|cm/s|

**2.2. ANTECENDENTES MEDIOAMBIENTALES**

 - _Batimetría_ : La medición de la profundidad se realizó el 24 de Febrero del presente
año, mediante un Ecosonda marca Garmin, modelo527 xs (profundidad máxima
alcanzable 609 mts de profundidad), observando una profundidad máxima de 280
metros y una profundidad mínima de 1 metro.
El sondaje de profundidad fue referido al datum WGS-84, la navegación se realizó
con una velocidad constante y con una línea de navegación lo mas cercanas
posibles, abarcando un área 200 metros más allá del área de la concesión.

 - _Correntometría_ : La medición de corriente se realizó mediante un correntómetro

perfilador acústico doppler (ADCP) marca Nortek modelo Aquadopp Profiler de
0.4 MHz de frecuencia, los días 12 y 13 de Marzo del presente año, realizando una
medición de 24 horas contemplando así el periodo de cuadratura.
El equipo se programó para medir la magnitud y dirección de las corrientes cada
10 minutos, considerando 30 celdas de 2 metros de espesor en la columna de
agua. En la tabla 2 se presentan los datos correspondientes a la correntometría.

4

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

Para la modelación fue considerado una velocidad de sedimentación de las fecas
de 0.032 m/s y un tamaño promedio de 1 μm de diámetro (Cromey, 2002).

Tabla 2. Información correntometría utilzada en la modelación.

|ITEM VALOR|Col2|
|---|---|
|**N° perfiles**|145|
|**Profundidad amarre correntómetro**|60|
|**Fase Lunar**|Cuadratura|
|**Intervalo perfil**|600|
|**N° estratos**|30|
|**Tamaño estratos**|2|
|**Capa superior (m)**|2|
|**Capas medias (m)**|14-26-38|
|**Capa fondo (m)**|54|

**2.3. ANTECENDENTES MODELO**

La modelación realizada con el programa DEPOMOD v2.4.1., tiene como base la
consideración de supuestos, los cuales son presentados en la siguiente tabla.

Tabla 3. Suspuestos del modelo Depomod según Cromey, 2002.

La relación entre la oferta de oxígeno y la demanda de oxígeno fue examinada por
Findlay R.H. & L. Watling (1997), como un predictor de la propuesta bentónica al
enriquecimiento orgánico causado por el cultivo de salmónidos. En su estudio ellos
encuentran una robusta correlación lineal entre la tasa de sedimentación de carbón
medida y la tasa de metabolismo bentónico. Esta relación permite una estimación de la
demanda de oxígeno con la ofertada por las corrientes y la ley de difusión de Fick.

El presente análisis reproduce la propuesta de estos autores a las condiciones presentes
en la concesión y calcula el índice de impacto que permite determinar si existe impacto o
no. Este índice entrega el balance entre la demanda de oxígeno y el oxígeno disponible.

5

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

a) Oferta de oxígeno en el bentos, usando primera ley de Fick:

J= D(C∞− C0)/Z ∂

Donde,
D = Coeficiente de difusión molecular del soluto en el ambiente (m [2] h [-1] )
C ∞ = Concentración del soluto en el cuerpo de agua (mmol m [-3] )
C 0 = Concentración del soluto en la interfase (mmol m [-3] )
Z∂ = Espesor de la capa límite de difusión (m)

b) De la ecuación anterior, y adecuándola a las mediciones de campo obtenidas

por los autores, se presenta la siguiente ecuación no lineal que relaciona la
velocidad de la corriente con la oferta de oxígeno:

Y= −32.6 + 1.1X ; r [2] = 0.965

Donde,

X = Flujo de Carbono (mmol m [-2] d [-1] )
Y = Consumo de Oxígeno (mmol m [-2] d [-1] )

c) El cálculo del índice de impacto se realiza según la siguiente ecuación de Findlay

& Watling (1997):

Aporte de oxígeno

I= [736.3 + 672.6 ∗log(X)] ó I=

−32.6 + 1.1 ∗Y Demanda de oxígeno

Donde,

X = Velocidad de las corrientes a 1 metro del fondo
Y = Concentración de Carbono en mmol/m [2] /día

Finalmente el índice establece lo siguiente:

1. Si la disponibilidad es mayor que la demanda, el índice tendrá un valor mayor a 1,

lo que implica que los impactos serían mínimos ( **I>1** ).
2. Por otro lado si la disponibilidad y la demanda son equivalentes, el índice sería

cercano a 1, lo que se traduce en que los impactos serían moderados ( **I=1** ).
3. Finalmente, si la disponibilidad es menor a la demanda, los valores del índice serán

menores a 1 y por lo tanto, los impactos serán altos ( **I<1** ).

6

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

En la figura 1 se observa la batimetría del sector, posicionamiento de la concesión y de
las balsas jaulas, las cuales se econtrarán en el sector más profundo de la concesión,
mejorando la capacidad de dilusión y transporte de todo material proveniente de las
fecas y alimento no consumido. Se observa, además, la costa, la cual se ubica al sur-oeste
de la concesión.

Figura 1: Posición de batimetría, concesión, jaulas y línea de costa.

La modelación con DEPOMOD v2.4.1. predice una tasa máxima depositada de 4.8
KgC/m [2] /año bajo la coordenada 691706,5289288, lo cual equivale al 0.004% del total del
área impactada; y una sedimentación promedio de 0.365 KgC/m [2] /año en las zonas que
reciben aporte (Figura 2).

Por otra parte, podemos indicar, mediante los resultados obtenidos en la modelación un
área total de dispersión de 8.4 hectáreas, tomando en cuenta que esta área contempla
las distintas capas o niveles de concentración de carbono medido en kg/m [2] /año,
podemos decir que, el área que tiene una mayor cobertura (2.26 há), la cual representa
el 26.8% del total de influencia, tiene una tasa de sedimentación de 0.5 kg/m [2] /año;
mientras que la mayor tasa de sedimentación correspondiente a 4.8 kg/m [2] /año

7

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

correspondiente sólo al 0.004% del total, tiniendo un área de cobertura de 0.00036
hectáreas.

Cabe destacar que existe un área de la concesión libre de perturbación, la cual
corresponde a 0.7 hectáreas, siendo el 12% del total de la concesión.

En la tabla 4 se logra observar con más detalle lo anteriormente mencionado y los distintos
niveles de tasas de sedimentación, mientras que en la figura 2 se observa de manera
gráfica.

Tabla 4. Tasa de sedimentación de Carbono modelada en DEPOMOD.

|KgC/m2/año|Dimensión del<br>área de<br>cobertura (Há.)|Influencia<br>Carbono (%)|
|---|---|---|
|4.8|0.00036|0.004|
|4.0|0.014|0.2|
|3.5|0.27|3.2|
|3.0|0.93|11.0|
|2.5|0.96|11.3|
|2.0|1.30|15.4|
|1.5|1.30|15.4|
|1.0|1.41|16.7|
|0.5|2.26|26.8|

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

8

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

Figura 2: Concentración de carbono medido en Kg/m [2] /año, mediante modelación

DEPOMOD.

Finalmente, junto a los resultados obtenidos en la modelación, es decir la concentración
máxima de carbono (4.8 kg/m [2] /año), más los datos de corrientes (mínima velocidad
promedio de la capa más profunda 4.06 cm/s) y oxígeno se logró estimar el índice de
impacto, el cual obtuvo un valor de 1.0.

Esto quiere decir, según los establecido por Findlay y Watling en el ’97, que el impacto
sería moderado. Sin embargo, hay que tomar en cuenta que este valor proviene de un
registro realizado en cuadratura, por lo tanto, se traduce en que se proyecta en periodos
de baja intensidad de corrientes y por ende una mayor perturbación en el bentos. Por
otro lado, es importante señalar, que al mes los periodos de cuadratura son dos, mientras
que el resto del tiempo, las corrientes tienden a ser mayores, obteniendo valores máximos
en los periodos de sicigia. Esto implica que en escenarios de mayor energía, el índice
tenderá a sobrepasar el valor de 1.0, lo que se traduce en una mejora en la calidad del
bentos.

9

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

Si bien la modelación es una aproximación matemática de los resultados que pudieran
obtenerse, los resultado entregados en el presente informe nos permiten obtener una idea
bastante cercana del comportamiento real de la depositación bajo un escenario típico
de un ciclo productivo de salmónidos, tomando en cuenta, además, que la modelación
realizada por el software DEPOMOD tiene una certeza de ± 23.1% (Cromey _et al._, 2002 en:
Corner et al., 2006).

Los valores del proyecto indican un valor máximo de depositación de 4.8 kg/m [2] /año, y al
ser comparados con estudios realizados para el hemisferio norte, como el realizado por
Pérez et al. 2002 que obtuvo valores máximos de 12 kg/m [2] /año bajo las balsas jaulas en
mar o por Corner en el 2006, el cual reporta valores de 37 kg/m [2] /año, el valor máximo
encontrado en éste trabajo es claramente menor.

Por otra parte, es necesario mencionar que los cálculos de sedimentación realizados bajo
las balsas jaulas son muy variables, dependiendo de la metodología ocupada por los
autores. Así tenemos valores que van de 4.9 kg/m [2] /año (Cross,1990) a 110 kg/m [2] /año
(Weston and Gowen, 1988).

En Chile, de acuerdo a González (op. Cit, 1997) la tasa de sedimentación fluctúa de 26.09
g/m [2] /día (9.5 kg/m [2] /año) a 67.62 g/m [2] /día (24.68 kg/m [2] /año) dependiendo si la balsa
jaula contiene smolts o individuos adultos respetivamente.

En la mayoría de los sitios de cultivo de salmónidos alrededor del mundo, los reportes de
corrientes oscilan alrededor de 0 a 10 cm/s, esto sugiere que estos sitios pueden
experimentar significativos períodos de tiempo con poco o nada de flujo y que ellos
podrían estar limitando la oferta de oxígeno. Findlay y Watling (1997) reportan que
velocidades menores a 0.3 cm/s, representan un valor límite, donde se pueden observar
sedimentos acompañados de manchas blancas características de algunas bacterias
filamentosas anaeróbicas como _Beggiatoa_ sp., indicativos de condiciones con baja
concentración de oxígeno. En el presente estudio se obtuvo una velocidad promedio de
corrientes en la capa profunda de 5.2 cm/s en cuadratura.

Por lo tanto, en base a las comparaciones con los diferentes autores, los cuales
mencionan valores superiores de carbono en el medio ambiente a los obtenidos en el
presente estudio y a las velocidades de corrientes mencionadas por Findlay y Watling en
el ’97, las cuales también, presentan un valor bastante inferior para la ocurrencia de
microorganismos; la presente modelación tendría un impacto mínimo en el medio
ambiente, el cual debería mejorar bajo condiciones normales y/o sicigia.

10

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

_MODELACIÓN CAPACIDAD DE CARGA_

SALMONES HUMBOLDT LTDA.
Centro Reñihue

Corner, R. A., A. J. Brooker, T. C. Telfer, L. G. Ross. 2006. A fully integrated GIS-based model
of particulate waste distribution from marine fish-cage sites. Aquaculture 258, 299-311.

Cross SF. 1990. Benthic impact of salmon farming in british Columbia. Vol. 1: Summary
report. Aquametrix, Sydney, british Columbia. 150pp.

Cromey, C. J.; T. D. Nickell, K. D. Black. 2002. DEPOMOD- modelling the deposition and
biological effect of waste solids from marine cage farms. Aquaculture 214. 211-239.

Findlay R.H. & L. Watling. 1997. Prediction of benthic impact for salmon Net-Pens based on
the balance of benthic oxygen supply and demand. Marine ecology progress series. Vol.
155: 147-157.

Jorgensen, B.B. & K. Richardson. 1996. Eutrophication in coastal marine ecosystems.
American geophysical union, coastal and estuarine Studies 52, Washington, D.C. ISBN o87590-266-9. 273p.

Libes, S. 1992. An introduction to marine biogeochemistry, 289 p. Jonhn Wiley & Sons, Inc.

Perez O. M.; T. C. Telfer, M. C. M. Beveridge and L. G. Ross. 2002. Geographical information
systems (GIS) as a simple tool to aid modelling of particulate waste ndistribution al marine
fish cage sites. Estuarine, coastal and shelf science. 54, 761-768.

Silva, C., Olivari, R. y G. Yani. 1999. Determinación de distritos de aptitud acuícola
mediante la aplicación de sistemas de información geográfica. Invest. Mar., Valparaiso,
27: 93-99.

Troncoso, J.M., Rojas, X., Millán N., y G. Schroeder. 2006. Recuperación de fondos marinos
anaeróbicos, bajo balsas de cultivo de salmones, por medio del tratamiento con hidróxido
de magnesio. Salmociencia, 67,71.

Weston DP, Gowen RJ. 1998. Assessment and prediction of the effects of salmon net-pen
culture on the benthic environment. 62 pp. in: Proceedings of the first annual meetings on
Puget sound research.

11

_[E-mail.: medioambiente@aquagestion.cl](mailto:medioambiente@aquagestion.cl)_

_Fono : (56) (65) 2576337_

_Puerto Montt_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.: Información correntometría utilzada en la modelación.**

| ITEM VALOR | Col2 |
| --- | --- |
| **N° perfiles** | 145 |
| **Profundidad amarre correntómetro** | 60 |
| **Fase Lunar** | Cuadratura |
| **Intervalo perfil** | 600 |
| **N° estratos** | 30 |
| **Tamaño estratos** | 2 |
| **Capa superior (m)** | 2 |
| **Capas medias (m)** | 14-26-38 |
| **Capa fondo (m)** | 54 |

**Tabla 4.: Tasa de sedimentación de Carbono modelada en DEPOMOD.**

| KgC/m2/año | Dimensión del<br>área de<br>cobertura (Há.) | Influencia<br>Carbono (%) |
| --- | --- | --- |
| 4.8 | 0.00036 | 0.004 |
| 4.0 | 0.014 | 0.2 |
| 3.5 | 0.27 | 3.2 |
| 3.0 | 0.93 | 11.0 |
| 2.5 | 0.96 | 11.3 |
| 2.0 | 1.30 | 15.4 |
| 1.5 | 1.30 | 15.4 |
| 1.0 | 1.41 | 16.7 |
| 0.5 | 2.26 | 26.8 |
