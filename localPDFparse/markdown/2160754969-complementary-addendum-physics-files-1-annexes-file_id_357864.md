---
title: Sin título
author: Gerardo Cornejo Balharry
date: D:20240923190610-03'00'
language: es
type: report
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN HIDRÁULICA
-->

## ANEXO 8b Actualizado Versión Adenda Complementaria Informe Hidráulico

### PROYECTO GENERACIÓN ELÉCTRICA GENERSUR SPA

# MODELACIÓN HIDRÁULICA
### RÍO TIJERAL

#### ZONA ATRAVIESO LINEA ELÉCTRICA

**REV_D ADENDA COMPLEMENTARIA**
**Comuna de Osorno, Provincia Osorno, Región de Los Lagos**

|Revisión:|Preparó:|Aprobó:|Fecha:|Observaciones:|
|---|---|---|---|---|
|A|Afluente Chile SpA|Santiago Ugarte|01-07-2023|Emitido para Titular|
|B|Afluente Chile SpA|Santiago Ugarte|03-09-2023|Emitido para DGA|
|C|Afluente Chile SpA|Santiago Ugarte|02-04-2024|Adenda N°1|
|D|Afluente Chile SpA|Santiago Ugarte|12-09-2024|Adenda Complementaria|

1
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

#### TABLA DE CONTENIDOS

1. INTRODUCCIÓN .................................................................................................. 3

2. ALCANCES .......................................................................................................... 5

3. ANTECEDENTES GENERALES ................................................................................ 6

3.1 Antecedentes Disponibles .............................................................................. 6

3.2 Referencias Bibliográficas .............................................................................. 6

4. MODELACIÓN HIDRÁULICA .................................................................................. 7

4.1 Objetivos de la Modelación ............................................................................ 7

4.2 Enfoque y Metodología .................................................................................. 7

4.3 Variables y Condiciones de Borde Utilizados en la Simulación ............................ 8

4.3.1 Geometría del Cauce y Planicie de inundación ........................................... 8

4.3.2 Coeficiente de Manning ........................................................................... 9

4.3.3 Condiciones de Borde ............................................................................ 14

4.3.4 Determinación de Caudales .................................................................... 15

4.4 Modelación Línea Eléctrica ............................................................................ 16

4.5 Resultados Modelación ................................................................................. 16

4.6 Análisis Proyección Línea Eléctrica ................................................................. 24

5. CONCLUSIONES ................................................................................................. 28

6. ANEXO A: “Ensayo Granulométrico” ..................................................................... 29

2
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

#### 1. INTRODUCCIÓN

El presente informe trata del análisis del comportamiento hidráulico del río Tijeral en la zona

de influencia del proyecto de generación eléctrica de la empresa GENERSUR SpA, el que se

emplaza en las cercanías del río Tijeral, ubicado en la comuna de Puerto Montt, Región de

los Lagos. Si bien el proyecto de generación eléctrica no tiene relación directa con el cauce

del río, este proyecta una línea eléctrica para evacuar su electricidad al sistema

interconectado central (SIC), en donde el trazado de la línea pasa por sobre el cauce.

Para hacer este análisis se estudian los ejes hidráulicos del río para la situación actual, y así

se analiza la influencia de la estructura eléctrica proyectada sobre esta modelación base.

Hay que tener en consideración que la línea eléctrica se considera de media tensión (23 Kv),

la que se construye con postes de hormigón tipos de 18 metros de alto, los cuales 15 metros

están sobre el nivel del terreno, y el resto soterrado. Estas estructuras alcanzan vanos

promedios entre postes de entre 60 a 70 metros, pero con refuerzos adicionales, pueden

alcanzar vanos entre postes de hasta 300 metros, dependiendo del tipo de cable y

condiciones climáticas a la que está expuesta la línea proyectada.

Para el caso del proyecto en estudio, se proyecta un vano entre postes de 195 metros

aproximadamente, tramo suficiente para que ninguna estructura de la línea eléctrica afecte

el libre escurrimiento del agua que circula superficialmente por el río Tijeral.

La modelación hidráulica se realiza en el software HEC-RAS, el cual nos permite tener una

estimación del comportamiento del agua para la condición actual sin proyecto,

determinando así las zonas de inundación del cauce. En la Figura 1.1 se muestra una vista

en planta con el tramo de estudio del río Tijeral.

3
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 1.1 Zona de estudio en río Tijeral, zona Cruce Línea Eléctrica.**

**Fuente: Plano Topográfico.**

El objetivo de la memoria de la modelación hidráulica de río Tijeral es realizar un análisis

del escurrimiento del caudal porteado para las condiciones de crecidas del río, que en este

caso son los casos de interés, ya que lo que se busca principalmente es determinar las zonas

de inundación para estas ocasiones, de esta manera desestimar cualquier afectación de la

línea eléctrica sobre el cauce.

4
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

#### 2. ALCANCES

Esta memoria hidráulica tiene por objetivo modelar y analizar las condiciones de

escurrimiento del río Tijeral, en la zona de cruce de la línea eléctrica por sobre el cauce del

río Tijeral. Para esto se realizaron las siguientes etapas.

 - Generar un modelo de la zona de influencia hidráulica por donde se proyecta el cruce

de la línea eléctrica. El modelo se genera en el software HEC-RAS en base a datos

topográficos e hidrológicos.

 Obtener un perfil longitudinal del río Tijeral en la zona de influencia hidráulica, para

luego generar los perfiles transversales de éste.

 Obtener y analizar los parámetros hidráulicos del modelo en HEC-RAS para la

situación actual.

 Verificar si el emplazamiento de los postes de la línea eléctrica se encuentran fuera

del cauce del río Tijeral.

5
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

#### 3. ANTECEDENTES GENERALES

**3.1** **Antecedentes Disponibles**

Para la elaboración de la presente memoria, se dispone de los siguientes antecedentes.

 Estudio Hidrológico

 Levantamiento topográfico del sector

 - Visita a terreno

 Análisis granulométrico del río

**3.2** **Referencias Bibliográficas**

Para la elaboración de la siguiente memoria, se han consultado las siguientes referencias

bibliográficas:

[Ref.1]: Guía de Presentación y Aprobación de Proyectos de Modificación de Cauces.

[Ref.2]: Design of Small Canals, Bureau of Reclamation.

[Ref.3]: Hidráulica, F.J Domínguez.

[Ref.4]: Open Channel Hydraulics, Ven Te Chow.

[Ref.5]: Open Channel Hydraulics, Ven Te Chow.

[Ref.6]: Hidráulica Aplicada al Diseño de Obras, Horacio Mery.

6
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

#### 4. MODELACIÓN HIDRÁULICA

**4.1** **Objetivos de la Modelación**

De acuerdo con lo indicado en el instructivo de la Dirección General de Aguas se debe

realizar un análisis hidráulico del escurrimiento para diferentes condiciones de caudal,

determinando ejes hidráulicos para las crecidas, velocidades, régimen de escurrimiento y

definición de zonas de inundación.

El objetivo del análisis hidráulico es, a partir de las características morfológicas del cauce,

determinar los niveles de aguas máximas, ejes hidráulicos y las zonas de inundación para

poder visualizar el comportamiento de este y su capacidad máxima, específicamente en la

zona de cruce de la línea eléctrica por sobre el cauce, verificando que las estructuras de

apoyo de la línea no interfieren con el cauce bajo condiciones de crecida.

**4.2** **Enfoque y Metodología**

La altura de escurrimiento en una sección de un cauce puede ser determinada por la

medición directa en terreno o bien, puede ser estimada a través de las técnicas clásicas de

la hidráulica conociendo las condiciones físicas del entorno. Esta altura depende del caudal

y las formas y características del cauce.

La caracterización hidráulica del flujo se realiza a través de la modelación del funcionamiento

hidráulico del cauce con el programa HEC-RAS. Este es un programa de análisis hidráulico

desarrollado por el Hydrologic Engineering Center (del Cuerpo de Ingenieros del Ejército de

EE.UU.) que a partir de datos topográficos y de caudales permite simular el comportamiento

hidráulico del cauce. HEC-RAS es un programa que se utiliza frecuentemente para este tipo

de modelaciones y entrega resultados adecuados para este tipo de análisis.

7
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**4.3** **Variables y Condiciones de Borde Utilizados en la**

**Simulación**

El software HEC-RAS requiere para la simulación del cauce la caracterización de los perfiles

transversales, el coeficiente de rugosidad de Manning y los caudales a simular. HEC-RAS

permite la simulación del caudal en el cauce deseado entregando resultados tales como

velocidades, alturas de escurrimiento y número de Froude, entre otros.

**4.3.1** **Geometría del Cauce y Planicie de inundación**

Se realizó un levantamiento topo batimétrico mediante el uso de una estación total,

construyendo curvas de nivel cada 1 [m] que caracterizan la geografía de la zona de

proyecto. A partir de esta información, se trazó el eje longitudinal del río Tijeral en los

sectores adyacentes a la zona de atravieso de la línea eléctrica por sobre el eje del río.

El eje para analizar del río en la zona de influencia tiene una longitud de 560 [m], de esta

forma, se cumple con el tramo mínimo exigido de 100 [m] aguas arriba y aguas abajo de la

obra proyectada estipulado por la Dirección General de Aguas en la Referencia 1 mencionada

en el Capítulo 4. Finalmente, se trazaron perfiles transversales cada 20 [m] a lo largo del

eje de en estudio, abarcando 180 [m] de ancho en toda su extensión. Para la condición

base de la modelación, no hay presencia de alguna particularidad o singularidad especial en

el tramo de estudio.

En la Figura 4.1 se muestra la topografía utilizada y el alineamiento trazado para luego ser

utilizado en la modelación hidráulica.

8
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.1 Alineamiento utilizado en modelo hidráulico HEC-RAS.**

**Fuente: Modelo hidráulico de río Tijeral, HEC-RAS.**

Notar que el alineamiento trazado en la planta topográfica es la misma utilizada en la

modelación hidráulica, respetando la morfología del río Tijeral en la zona de estudio.

**4.3.2** **Coeficiente de Manning**

Si bien una de las hipótesis básicas en HEC-RAS es la unidimensionalidad del flujo, se

permite representar la sección caracterizándola según las planicies de inundación derecha

(right over bank) e izquierda (left over bank) separadas ambas por el cauce principal (main

channel). Así, cada una de dichas partes debe ser caracterizada con su valor del coeficiente

de Manning y su distancia a la sección inmediatamente aguas abajo. Tradicionalmente para

este tipo de estudios, la metodología utilizada es la recomendada en el libro “Hidráulica de

Canales Abiertos” de Ven Te Chow de acuerdo al método de Cowan. Según este método, el

coeficiente de rugosidad de Manning se obtiene a partir de la ecuación 4.1.

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) ∗m (4.1)

9
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

Donde n i y m son valores que dependen de las condiciones del cauce, las cuales se detallan

a continuación:

n 0 Valor base, relacionado al material del lecho.

n 1 Grado de Irregularidad

n 2 Variación de la Sección Transversal

n 3 Efecto Relativo de las Obstrucciones

n 4 Vegetación

m Grado de los Efectos por Meandros

El valor base n 0 se determina analíticamente a partir de la ecuación de Strickler (4.2),

suponiendo que el lecho no es macrorugoso:

S t = ~~[√]~~ [g∗n] [o] (4.2)

D [1/6]

Donde:

S t Número de Strickler (=0,12).

g Aceleración de gravedad (m/s2)

n o Coeficiente de rugosidad de Manning.

D Diámetro característico del sedimento, D 84 (m)

Para determinar el diámetro característico del sedimento, es necesario analizar la

granulometría obtenida del estudio del ensayo macro granulométrico realizado en el lecho

del río Tijeral, en la zona de interés del proyecto, el cual se puede ver en la copia del informe

de laboratorio (Anexo A del presente informe), y el gráfico de la figura 4.3.

10
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

100%

90%

80%

70%

60%

50%

40%

30%

20%

10%

0%

**Figura 4.2 Curva Granulométrica Río Tijeral, Zona Captación.**

**Fuente: Ensayo Macro granulométrico Labinco.**

#### Curva Granulométrica RÍO TIJERAL ZONA INFLUENCIA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|Col45|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||

1000 100 10 1 0,1 0,01

DIÁMETRO DE LA PARTÍCULA (mm)

**Figura 4.3 Curva Granulométrica Río Tijeral, Zona Captación.**

**Fuente: Ensayo Macro granulométrico.**

11
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

El lecho del río Tijeral en la zona de estudio presenta una granulometría poco rugosa, sin

tendencia al acorazamiento, razón por la que el diámetro característico del sedimento se

acerca al D84 [1], obteniendo un diámetro equivalente de 125 mm.

**Figura 4.4 Fotos In Situ, Zona Captación.**
**Fuente: Ensayo Macro granulométrico laboratorio Labinco EIRL.**

Dadas las características del río Tijeral, en el tramo de interés, y con base en valores

entregados por Ven Te Chow (1959) en el libro “Hidráulica de Canales Abiertos”, y de los

1 Página 779, Manual de Carreteras, Volumen 3, Edición 2019.

12
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

datos de la se determinaron los coeficientes ya mencionados tanto para el cauce principal

como para las planicies de inundación izquierda y derecha del cauce en análisis.

En la Tabla 4.1 se muestra los valores estimados para n i y m, tanto para riberas y cauce

principal.

**Tabla 4.1 Determinación del coeficiente de rugosidad de Manning por método de Cowan.**

|Descripción Coeficiente|Col2|Cauce|Col4|Ribera|Col6|
|---|---|---|---|---|---|
|**Descripción Coeficiente**|**Descripción Coeficiente**|**Justificación**|**Valor**|**Justificación**|**Valor**|
|n0|Fórmula de Strickler|D84=0,125 m|0.027|Tierra|0.028|
|n1|Grado de Irregularidad Perímetro<br>Mojado|leve|0.005|Moderado|0.005|
|n2|Variaciones de las Secciones|Graduales|0|Graduales|0|
|n3|Efecto Relativo de las Obstrucciones|leve|0.0065|Leve|0.005|
|n4|Densidad de Vegetación|Muy Alta|0.05|Alta|0.03|
|m|Sinuosidad y Frecuencia de Meandros|Leve|1|Leve|1|
|**n **|**Rugosidad de Manning**|**Manning **|**0.089**|**Manning **|**0.068**|

**Fuente: Elaboración propia.**

Se tiene para el cauce principal del río Tijeral:

n = 0.089 [s/m [1/3] ]

Y para las planicies de inundación izquierda y derecha:

n = 0.068 [s/m [1/3] ]

Los valores estimados están por sobre los criterios establecidos por Chow (1959), donde se

indica que para ríos de planicie menor el coeficiente de Manning varía entre 0.020 y 0.050

s/m [1/3] . El elevado valor del coeficiente de Manning en las planicies de inundación se debe a

la alta vegetación presente en todo el cauce, tanto en el mismo lecho como en las orillas de

éste. También se suma el criterio conservador para la modelación.

13
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**4.3.3** **Condiciones de Borde**

La morfología del río Tijeral, en la sección de captación de la planta, es similar a lo largo del

tramo de estudio, sin presentar grandes variaciones en cuanto a su pendiente, sinuosidad

y planicie de inundación. Esto sería suficiente como para considerar una condición de

contorno ajustada a la pendiente de fondo del cauce acorde a la pendiente media del tramo

de estudio, la cual se supone similar a la pendiente de escurrimiento. Por la razón anterior,

se utilizó como condición de borde aguas arriba y aguas abajo la pendiente media del tramo

del cauce en estudio.

➢ Cota Perfil PK 0+000.00: 86,397 (msnm)

➢ Cota Perfil PK 0+560.00: 85.156 (msnm)

Pendiente Media= [86,397 −85,156] = 0,0022 (m/m)

560

Por otra parte, el régimen de escurrimiento del tramo de estudio es predominantemente

subcrítico, sin excepción para ningún tramo, por lo que se utiliza el criterio de simular el río

Tijeral en el software HEC-RAS para este régimen. Esto último concuerda con lo observado

en terreno, en donde una leve pendiente del cauce y una excesiva vegetación no permiten

el desarrollo de grandes velocidades en el porte de agua.

En la Tabla 4.2 se resume las condiciones de contorno utilizadas en modelo hidráulico HEC

RAS.

14
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Tabla 4.2. Resumen de condiciones de contorno calibradas para la modelación hidráulica de río Tijeral, en la**

**Sección de Captación de la planta.**

|Variables|Descripción|
|---|---|
|Geometría|Levantamiento realizado en la zona de estudio.|
|Coeficiente de Rugosidad<br>de Manning|Cauce principal: n = 0.089<br>Planicies de inundación: n = 0.068|
|Tipo de Modelación|Flujo Permanente en Escurrimiento Subcrítico|
|Condición de Borde Aguas<br>Arriba y Abajo|Aguas Arriba: Pendiente Normal S=0,0022<br>Aguas Abajo: Pendiente Normal S=0,0022|

**Fuente: Elaboración propia.**

**4.3.4** **Determinación de Caudales**

Los caudales considerados para la modelación hidráulica fueron obtenidos del estudio

hidrológico para el río Tijeral en el sector del proyecto, cuyo análisis está hecho en esta

misma coordenada geográfica. Éste se realizó para la cuenca en estudio, determinando el

caudal de diseño (Q100) y de verificación (Q200).

Debido que el proyecto de la línea eléctrica no altera el libre escurrimiento del agua que

circula superficialmente por el río Tijeral, el único caso a analizar es para el caso actual sin

proyecto, en donde se modelan los caudales de crecidas y de verificación, es decir, no existe

el caso con proyecto propiamente tal ya que, una vez instalada la línea eléctrica, no existirá

cambio alguno.

La Tabla 4.3 resume los datos mencionados en la representación anterior.

15
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Tabla 4.3. Caudales utilizados en la modelación hidráulica de río Tijeral en zona de Cruce.**

**CASO MODELACIÓN** **Q100** **Q200**

**Fuente: Estudio Hidrológico río Tijeral.**

**4.4** **Modelación Línea Eléctrica**

Como se explica anteriormente, el objetivo de esta modelación es verificar si la

implementación de la estructura eléctrica relacionada a la línea eléctrica proveniente de la

central de generación eléctrica se encuentra fuera del cauce del río Tijeral. En el caso que

se la modelación indique que, si existe una alteración del libre escurrimiento del agua del

río Tijeral, se tendrá que generar una condición con proyecto, de manera de poder

dimensionar las posibles obras a realizar para que no exista una afectación al cauce y la

calidad del agua.

**4.5** **Resultados Modelación**

En la Figura 4.3 se muestra el modelo desarrollado en HEC-RAS para la condición sin

proyecto, que incluye las condiciones de borde mencionadas en inciso 4.3.

16
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.3 Vista 3D de modelo hidráulico de río Tijeral Zona de Influencia, situación actual.**

**Fuente: Modelo hidráulico río Tijeral, HEC-RAS.**

En la Figura 4.4 se muestra el eje hidráulico de los tramos de estudio del río Tijeral, para

los caudales de crecida con periodo de retorno de 100 y 200 años para la condición sin

proyecto. Es posible observar un leve aumento de cota del pelo de agua para el caudal de

verificación con respecto al de diseño, pero el aumento es insignificante. Esto se debe a que

la diferencia en la magnitud de caudal representa un aumento del 12,2% del caudal de

diseño.

17
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.4 Eje Hidráulico río Tijeral, situación actual para caudal medio anual, T = 100 y 200 años.**

**Fuente: Modelo hidráulico río Tijeral, HEC-RAS.**

Además, en las Tablas 4.4 y Tabla 4.5 se muestran los principales resultados de la simulación

hidráulica para el tramo en estudio del río Tijeral, para la situación actual. Se entregan los

valores del eje hidráulico, velocidad de escurrimiento, ancho superficial, y número de

Froude.

**Tabla 4.4. Resultados simulación hidráulica en situación actual de río Tijeral para para T=100 años.**

|Perfil|Cota Pelo Velocidad Área Ancho<br>Caudal Cota Fondo Número<br>de Agua Media Mojada Superficial<br>de Froude<br>[m3/s] [m.s.n.m.] [m.s.n.m.] [m/s] [m2] [m]|
|---|---|
|**km 0+000**<br>**km 0+020**<br>**km 0+040**<br>**km 0+060**<br>**km 0+080**<br>**km 0+100**|158.36<br>86.4<br>89.26<br>0.74<br>215.75<br>105.41<br>0.16<br>158.36<br>86.34<br>89.22<br>0.84<br>199.41<br>106.93<br>0.17<br>158.36<br>86.31<br>89.18<br>0.84<br>201.62<br>115.79<br>0.17<br>158.36<br>86.28<br>89.15<br>0.78<br>214.5<br>116.8<br>0.16<br>158.36<br>86.2<br>89.13<br>0.69<br>235.57<br>110.85<br>0.14<br>158.36<br>86.03<br>89.11<br>0.64<br>253.5<br>110.44<br>0.13|

18
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Fuente: Modelo hidráulico río Tijeral, HEC-RAS.**

**Tabla 4.5. Resultados simulación hidráulica en situación actual de río Tijeral para T=200 años.**

|Perfil|Cota Pelo Velocidad Área Ancho Número<br>Caudal Cota Fondo<br>de Agua Media Mojada Superficial de<br>[m3/s] [m.s.n.m.] [m.s.n.m.] [m/s] [m2] [m] Froude|
|---|---|
|**km 0+000**<br>**km 0+020**<br>**km 0+040**<br>**km 0+060**<br>**km 0+080**<br>**km 0+100**<br>**km 0+120**<br>**km 0+140**<br>**km 0+160**<br>**km 0+180**<br>**km 0+200**<br>**km 0+220**<br>**km 0+240**|177.68<br>86.4<br>89.4<br>0.78<br>230.98<br>106.87<br>0.16<br>177.68<br>86.34<br>89.36<br>0.88<br>214.79<br>108.26<br>0.17<br>177.68<br>86.31<br>89.33<br>0.87<br>218.32<br>117.16<br>0.17<br>177.68<br>86.28<br>89.3<br>0.81<br>231.35<br>118.38<br>0.16<br>177.68<br>86.2<br>89.27<br>0.73<br>251.51<br>112.34<br>0.14<br>177.68<br>86.03<br>89.25<br>0.68<br>269.33<br>112.18<br>0.13<br>177.68<br>85.95<br>89.24<br>0.66<br>277.17<br>119.71<br>0.13<br>177.68<br>85.9<br>89.22<br>0.68<br>270.33<br>124.19<br>0.13<br>177.68<br>85.84<br>89.2<br>0.69<br>272.56<br>125.95<br>0.13<br>177.68<br>85.78<br>89.17<br>0.76<br>254.24<br>130.3<br>0.14<br>177.68<br>85.94<br>89.13<br>0.87<br>226.26<br>128.02<br>0.17<br>177.68<br>85.94<br>89.1<br>0.88<br>215.28<br>122.37<br>0.18<br>177.68<br>85.92<br>89.06<br>0.87<br>218.91<br>124.26<br>0.18|

19
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Fuente: Modelo hidráulico río Tijeral, HEC-RAS.**

En la Figura 4.5 se muestra gráficamente un perfil longitudinal con los ejes hidráulicos del

Río Tijeral para los distintos escenarios modelados en la condición sin Proyecto. Como se

puede apreciar en el gráfico, no existen grandes variaciones a lo largo del trazado de

estudio.

20
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.5. Gráfico de ejes hidráulicos de escurrimiento en río Tijeral, para la condición sin proyecto, para**

**caudal de periodos de retorno 100 y 200 años.**

**Fuente: Elaboración propia.**

21
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.6. Imagen Zona de Influencia en Río Tijeral**

**Fuente: Elaboración propia.**

Como se puede ver en la fotografía de la Figura 4.6, el río Tijeral en la Zona de Influencia

escurre de manera similar a lo largo del área de influencia estudiada. Lo más relevante es

la baja pendiente y la vegetación en todo el lecho, la cual está considerada en el modelo

realizado en el software HEC-RAS.

En la Figura 4.7 se muestra los valores de velocidad media del flujo en el río Tijeral para

cada perfil. Tal como se explica en el párrafo anterior, no hay grandes variaciones a lo largo

de la zona de estudio, y las velocidades son bajas, considerando que se analizan caudales

de crecidas de 100 y 200 años.

22
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.7 Gráfico Velocidad de escurrimiento en río Tijeral, para la condición sin proyecto, para caudal de**

**periodos de retorno 100 y 200 años.**

**Fuente: Elaboración propia.**

En la Figura 4.8 se muestra los valores del número de Froude en el río Tijeral para cada

perfil. Tal como se observa y concluye con las variables observadas previamente, el río

Tijeral no tiene grandes variaciones en el tramo de estudio, y su comportamiento es por lo

general el de río, sin excepción, en donde el agua circula muy por debajo del límite de

régimen crítico. Lo anterior viene a reforzar lo observado en terreno y las conclusiones que

se han hecho hasta ahora, en donde una baja pendiente y una elevada vegetación no

permiten un escurrimiento eficiente de agua de manera superficial.

23
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.11 Gráfico número de Froude en río Tijeral, para la condición sin proyecto, para caudal de periodos**

**de retorno 100 y 200 años.**
**Fuente: Elaboración propia.**

**4.6** **Análisis Proyección Línea Eléctrica**

Luego de analizar los resultados para las situaciones “sin proyecto” obtenidas con ayuda del

modelo hidráulico en HEC-RAS, es posible determinar las zonas de inundación del río Tijeral

en la zona de influencia hidráulica. Con esto se puede determinar el impacto de la obra de

la línea eléctrica proyectada de una manera más gráfica, y por ende más fácil de comprender

y analizar si hay un cambio significativo o no.

24
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

Antes de mostrar los resultados es importante recordar que la modelación toma como caso

base el río Tijeral sin ninguna intervención en el río, y la entrada en operación de la línea

eléctrica no altera esta condición base.

La Figura 4.12 muestra la zona de inundación del río en el eje analizado, y muestra la

proyección de la línea eléctrica.

**Figura 4.12 Plano de Planta de Zonas de Inundación del río Tijeral, Situaciones sin para caudal de diseño T =**

**100 años.**

**Fuente: Modelo hidráulico río Tijeral, HEC-RAS.**

Como se puede observar, el trazado de la línea eléctrica se proyecta entre los perfiles

PK0+340.00 y PK0+380.00. Se realiza a continuación el análisis de la ubicación de los postes

de la línea eléctrica en función de las cotas de inundación definidas para Q100 y Q200.

25
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

En la tabla siguiente 4.6, se presenta un cuadro resumen de las cotas del eje hidráulico a lo

largo de los citados perfiles, y la revancha que existe entre estas y la base de los postes.

**Tabla 4.6. Revanchas de postes sobre río Tijerales, según resultados Perfiles PK 0+340 al perfil PK 0+380**

**simulación hidráulica río Tijerales.**

|Cota poste n°2 (LEMT) 94.2 msnm<br>Cota poste n°3 (LEMT) 90.4 msnm|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|<br> <br> <br> <br>|<br> <br> <br> <br>|<br> <br> <br> <br>|<br> <br> <br> <br>|<br> <br> <br> <br>|**Revancha Postes (m)**|**Revancha Postes (m)**|**Revancha Postes (m)**|**Revancha Postes (m)**|
|Perfil|Cota Fondo|Q100 - SP|Q200 - SP||Poste N°2<br>Poste N°3|Poste N°2<br>Poste N°3|Poste N°2<br>Poste N°3|Poste N°2<br>Poste N°3|
|Perfil|[m.s.n.m.]|[m.s.n.m.]|[m.s.n.m.]||Q100|Q200|Q100|Q200|
|km 0+340|85.26|88.78|88.92||5.42|5.28|1.62|1.48|
|km 0+360|85.28|88.75|88.89||5.45|5.31|1.65|1.51|
|km 0+380|85.28|88.72|88.86||5.48|5.34|1.68|1.54|

**Fuente: Modelo hidráulico río Tijeral, HEC-RAS.**

De la tabla 4.6 se puede comprobar que, para todos los perfiles transversales del río Tijerales

involucrados en el cruce del tendido eléctrico, los citados postes n°2 y n°3 se localizan a

una cota mayor a la cota de inundación. Cabe resaltar que ambos postes están más de un

metro por sobre la cota de crecida de diseño, cumpliendo con la revancha mínima de diseño

hidráulico.

Por tanto, se puede concluir que la implementación de estas obras no involucra una

modificación de cauce en el río.

Para ver de manera más gráfica esta situación, en la figura a continuación se muestra el

perfil de la línea eléctrica proyectada, y se toma como referencia las cotas de inundación

del perfil PK0+360.

26
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

**Figura 4.13 Plano Perfil Transversal línea eléctrica sobre río Tijeral. Situaciones de cota de inundación para**

**caudal de diseño T = 100 años y T=200 años en PK 0+360.**

**Fuente: Modelo hidráulico río Tijeral, HEC-RAS.**

Como se puede comprobar gráficamente, las obras proyectadas para la estructura de la

línea eléctrica están fuera de la definición del cauce del río Tijerales. El poste N°3 de la

LEMT se distancia en proyección horizontal 14,1 metros de la cota de inundación, y el poste

n°2 de la LEMT se sitúa a 52,4 metros de distancia en proyección horizontal de la cota de

inundación del río.

27
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

#### 5. CONCLUSIONES

A través de la modelación hidráulica del río Tijeral en la zona del proyecto, con ayuda de los

levantamientos topográficos en terreno y los datos de caudales de crecidas obtenidos en el

estudio hidrológico, se pudo obtener el comportamiento hidráulico del río Tijeral en la zona

de influencia.

Como se introdujo, para la implementación del proyecto de generación eléctrica, es

necesario la construcción de una línea eléctrica para evacuar su electricidad al sistema

interconectado central (SIC), en donde el trazado de la línea pasa por sobre el cauce del río

Tijeral. El principal objetivo del presente estudio fue verificar la interacción que podría existir

entre el río Tijeral y las obras relacionadas al cauce.

Para la modelación del río Tijeral en la zona de influencia, se utilizaron los datos de hidrología

más conservadores, de manera de hacer que el río Tijeral porte mayor cantidad de caudal,

y por ende con una caja de río más grande.

Como conclusión general se tiene que no hay una alteración de la línea eléctrica proyectada

sobre el río, ya que todas las estructuras eléctricas se encuentran fuera del cauce del río

Tijeral, definido para los casos de crecidas.

Como conclusión a lo descrito en el párrafo anterior, al no existir una alteración al cauce,

no es necesario presentar un Permiso Sectorial de Modificación de Cauce (PAS 156 o PAS

157), en el contexto de la evaluación ambiental y/o sectorial del proyecto.

28
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

#### 6. ANEXO A: “Ensayo Granulométrico”

29
Málaga 50 / Las Condes / Santiago / Chile Fono: (+56) 9 54071612

[E-mail: santiago.ugarte@afluentechile.cl www.afluentechile.cl](mailto:santiago.ugarte@afluentechile.cl)

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4.1: Determinación del coeficiente de rugosidad de Manning por método de Cowan.****

| Descripción Coeficiente | Col2 | Cauce | Col4 | Ribera | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Descripción Coeficiente** | **Descripción Coeficiente** | **Justificación** | **Valor** | **Justificación** | **Valor** |
| n0 | Fórmula de Strickler | D84=0,125 m | 0.027 | Tierra | 0.028 |
| n1 | Grado de Irregularidad Perímetro<br>Mojado | leve | 0.005 | Moderado | 0.005 |
| n2 | Variaciones de las Secciones | Graduales | 0 | Graduales | 0 |
| n3 | Efecto Relativo de las Obstrucciones | leve | 0.0065 | Leve | 0.005 |
| n4 | Densidad de Vegetación | Muy Alta | 0.05 | Alta | 0.03 |
| m | Sinuosidad y Frecuencia de Meandros | Leve | 1 | Leve | 1 |
| **n ** | **Rugosidad de Manning** | **Manning ** | **0.089** | **Manning ** | **0.068** |

**Tabla 4.2.: Resumen de condiciones de contorno calibradas para la modelación hidráulica de río Tijeral, en la****

| Variables | Descripción |
| --- | --- |
| Geometría | Levantamiento realizado en la zona de estudio. |
| Coeficiente de Rugosidad<br>de Manning | Cauce principal: n = 0.089<br>Planicies de inundación: n = 0.068 |
| Tipo de Modelación | Flujo Permanente en Escurrimiento Subcrítico |
| Condición de Borde Aguas<br>Arriba y Abajo | Aguas Arriba: Pendiente Normal S=0,0022<br>Aguas Abajo: Pendiente Normal S=0,0022 |

**Tabla 4.4.: Resultados simulación hidráulica en situación actual de río Tijeral para para T=100 años.****

| Perfil | Cota Pelo Velocidad Área Ancho<br>Caudal Cota Fondo Número<br>de Agua Media Mojada Superficial<br>de Froude<br>[m3/s] [m.s.n.m.] [m.s.n.m.] [m/s] [m2] [m] |
| --- | --- |
| **km 0+000**<br>**km 0+020**<br>**km 0+040**<br>**km 0+060**<br>**km 0+080**<br>**km 0+100** | 158.36<br>86.4<br>89.26<br>0.74<br>215.75<br>105.41<br>0.16<br>158.36<br>86.34<br>89.22<br>0.84<br>199.41<br>106.93<br>0.17<br>158.36<br>86.31<br>89.18<br>0.84<br>201.62<br>115.79<br>0.17<br>158.36<br>86.28<br>89.15<br>0.78<br>214.5<br>116.8<br>0.16<br>158.36<br>86.2<br>89.13<br>0.69<br>235.57<br>110.85<br>0.14<br>158.36<br>86.03<br>89.11<br>0.64<br>253.5<br>110.44<br>0.13 |

**Tabla 4.5.: Resultados simulación hidráulica en situación actual de río Tijeral para T=200 años.****

| Perfil | Cota Pelo Velocidad Área Ancho Número<br>Caudal Cota Fondo<br>de Agua Media Mojada Superficial de<br>[m3/s] [m.s.n.m.] [m.s.n.m.] [m/s] [m2] [m] Froude |
| --- | --- |
| **km 0+000**<br>**km 0+020**<br>**km 0+040**<br>**km 0+060**<br>**km 0+080**<br>**km 0+100**<br>**km 0+120**<br>**km 0+140**<br>**km 0+160**<br>**km 0+180**<br>**km 0+200**<br>**km 0+220**<br>**km 0+240** | 177.68<br>86.4<br>89.4<br>0.78<br>230.98<br>106.87<br>0.16<br>177.68<br>86.34<br>89.36<br>0.88<br>214.79<br>108.26<br>0.17<br>177.68<br>86.31<br>89.33<br>0.87<br>218.32<br>117.16<br>0.17<br>177.68<br>86.28<br>89.3<br>0.81<br>231.35<br>118.38<br>0.16<br>177.68<br>86.2<br>89.27<br>0.73<br>251.51<br>112.34<br>0.14<br>177.68<br>86.03<br>89.25<br>0.68<br>269.33<br>112.18<br>0.13<br>177.68<br>85.95<br>89.24<br>0.66<br>277.17<br>119.71<br>0.13<br>177.68<br>85.9<br>89.22<br>0.68<br>270.33<br>124.19<br>0.13<br>177.68<br>85.84<br>89.2<br>0.69<br>272.56<br>125.95<br>0.13<br>177.68<br>85.78<br>89.17<br>0.76<br>254.24<br>130.3<br>0.14<br>177.68<br>85.94<br>89.13<br>0.87<br>226.26<br>128.02<br>0.17<br>177.68<br>85.94<br>89.1<br>0.88<br>215.28<br>122.37<br>0.18<br>177.68<br>85.92<br>89.06<br>0.87<br>218.91<br>124.26<br>0.18 |

**Tabla 4.6.: Revanchas de postes sobre río Tijerales, según resultados Perfiles PK 0+340 al perfil PK 0+380****

| Cota poste n°2 (LEMT) 94.2 msnm<br>Cota poste n°3 (LEMT) 90.4 msnm | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br> <br> <br> <br> | <br> <br> <br> <br> | <br> <br> <br> <br> | <br> <br> <br> <br> | <br> <br> <br> <br> | **Revancha Postes (m)** | **Revancha Postes (m)** | **Revancha Postes (m)** | **Revancha Postes (m)** |
| Perfil | Cota Fondo | Q100 - SP | Q200 - SP |  | Poste N°2<br>Poste N°3 | Poste N°2<br>Poste N°3 | Poste N°2<br>Poste N°3 | Poste N°2<br>Poste N°3 |
| Perfil | [m.s.n.m.] | [m.s.n.m.] | [m.s.n.m.] |  | Q100 | Q200 | Q100 | Q200 |
| km 0+340 | 85.26 | 88.78 | 88.92 |  | 5.42 | 5.28 | 1.62 | 1.48 |
| km 0+360 | 85.28 | 88.75 | 88.89 |  | 5.45 | 5.31 | 1.65 | 1.51 |
| km 0+380 | 85.28 | 88.72 | 88.86 |  | 5.48 | 5.34 | 1.68 | 1.54 |
