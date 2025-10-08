---
title: PDF-XChange 4.0 Examples
author: Tracker Software
date: D:20101210023537-05'00'
language: es
type: report
pages: 67
has_toc: False
has_tables: True
extraction_quality: high
keywords: [PDF-XChange; Examples; 4.0; Delphi]
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 1
-->

|REVISION|CAMBIOS EFECTUADOS|FECHA|
|---|---|---|
|0|Informe elaborado con:<br>. <br> Informe de Resultados N°118537-19-00 (Incluye medición de<br>Vs30, estratigrafías calicatas y sondaje, ensayos in-situ y de<br>laboratorio) EMPRO Ltda., diciembre de 2019.|Diciembre<br>de 2019|
|1|Se modifica:<br> <br> Aumento en un nivel de subterráneos.<br>|Enero de<br>2020|
|2|Se modifica:<br> <br> Edificio pasa de 13 pisos a 15 pisos.<br>|Enero de<br>2020|

**ÍNDICE**

Página

ANTECEDENTES UTILIZADOS ............................................................................................ 4

INTRODUCCIÓN ..................................................................................................................... 5

PROPIEDADES DEL SUELO DE FUNDACIÓN ................................................................... 6

Antecedentes geológicos ..................................................................................................... 6

Estratigrafía ......................................................................................................................... 6

Ubicación del nivel freático ................................................................................................ 8

Propiedades mecánicas del suelo de fundación .................................................................. 8

DIMENSIONAMIENTO DE FUNDACIONES ....................................................................... 8

Tipo de fundaciones ............................................................................................................ 9

Dimensiones mínimas de fundaciones ................................................................................ 9

Capacidad de soporte admisible ........................................................................................ 10

ASENTAMIENTO DE FUNDACIONES ............................................................................... 12

Tipos de asentamientos ..................................................................................................... 12

E.1.1 Asentamiento para cargas permanentes ..................................................................... 12

E.1.3 Asentamiento para cargas dinámicas ......................................................................... 15

Asentamiento total admisible ............................................................................................ 15

Constantes de balasto de fundaciones ............................................................................... 16

Giros de fundaciones ......................................................................................................... 17

EMPUJES DE SUELO SOBRE MUROS ............................................................................... 18

Empuje de suelo sobre muros de subterráneos ................................................................. 18

F.1.1 Caso estático .............................................................................................................. 19

F.1.2 Caso sísmico .............................................................................................................. 20

Empuje de suelo sobre muros de contención .................................................................... 21

F.2.1 Caso estático .............................................................................................................. 21

F.2.2 Caso sísmico .............................................................................................................. 22

F.2.3 Empuje pasivo ............................................................................................................ 23

F.2.4 Factores de seguridad de muros de contención .......................................................... 24

F.2.5 Condiciones de drenaje de muro de contención......................................................... 24

ESPECIFICACIONES PARA RELLENOS ............................................................................ 25

Rellenos estructurales........................................................................................................ 25

Rellenos comunes.............................................................................................................. 26

CBR DE LA SUBRASANTE .................................................................................................. 27

CAPACIDAD DE INFILTRACIÓN DEL SUELO ................................................................ 28

CLASIFICACIÓN SEGÚN NORMA SÍSMICA .................................................................... 29

RECOMENDACIONES DE CONSTRUCCIÓN .................................................................... 30

Figuras N°1 a N°4

ANEXO 1: Informe de Resultados N°118537-19-00 (Incluye medición de Vs30, estratigrafías

calicatas y sondaje, ensayos in-situ y de laboratorio) EMPRO Ltda., diciembre de

2019.

**ANTECEDENTES UTILIZADOS**

Informe de Resultados N°118537-19-00 (Incluye medición de Vs30, estratigrafías calicatas

y sondaje, ensayos in-situ y de laboratorio) EMPRO Ltda., diciembre de 2019.

J.E. Bowles, "Foundation Analysis and Design". Ed. Mc. Graw-Hill, 1977.

Geografía de Chile, Instituto Geográfico Militar. Tomo II Geomorfología.

Mapa Geológico de Chile, Servicio Nacional de Geología y Minería, 1982.

Norma NCh 433 Of. 96 Mod. 2009, Diseño Sísmico de Edificios, Instituto Nacional de

Normalización, modificada por el Decreto Supremo No61 de 13 de Diciembre de 2011.

4

**INTRODUCCIÓN**

Con motivo de la construcción de un edificio de 15 pisos con 2 subterráneos, ubicado en

Cristóbal Colon N°8543, comuna de Hualpén, Región del Bío Bío, GRUPO INMOBILIARIO

PACAL, a través del Sr. Ángel Fernández, solicitó a HORACIO MUSANTE E INGENIEROS SPA,

el estudio de mecánica de suelos para dicha obra. El propósito del estudio es dar recomendaciones de

diseño y de construcción relativas a las fundaciones de las obras proyectadas.

El estudio comenzó con el análisis de antecedentes geológicos disponibles del sector, en

especial de la exploración del suelo de fundación realizada mediante 3 pozos de 2.0 m de

profundidad y un sondaje de 30.0 m de profundidad, ubicados en el terreno en estudio según se

muestra en la figura No1. El plan consideraba realizar 2 pozos de 3.5 m de profundidad y 1 pozo de

1.5 m, pero al detectarse napa freática no se pudo alcanzar la profundidad deseada. De los pozos y de

las muestras del sondaje se obtuvo la estratigrafía del suelo y muestras de suelo para ensayar en el

laboratorio. Además, se realizó un ensayo geofísico mediante el método ReMi para determinar la

velocidad de propagación de las ondas de corte en los primeros 30.0 m de profundidad.

Los resultados de la exploración de terreno, ensayes de laboratorio e in situ, se presentan en

los capítulos correspondientes debidamente interpretados y procesados.

Como resultado del trabajo realizado, han surgido el modelo estratigráfico y el de

propiedades mecánicas del suelo de fundación, utilizados en los cálculos para determinar

preliminarmente la capacidad de soporte, asentamientos, constantes de balasto de fundaciones,

empujes de suelo sobre muros, especificaciones para rellenos, agotamiento de la napa, potencial

de licuación, CBR de la subrasante, capacidad de infiltración, clasificación sísmica según Decreto

Supremo No61 de 13 de Diciembre de 2011 que modifica la Norma NCh 433 Of. 96 Mod. 2009

"Diseño sísmico de edificios" y, finalmente, para dar recomendaciones de construcción de las

fundaciones y radieres.

5

**PROPIEDADES DEL SUELO DE FUNDACIÓN**

**Antecedentes geológicos**

El área en que se emplaza el proyecto está situada en la unidad denominada planicie costera

marina, en donde ha tenido una fuerte influencia el río Bío-Bío en su modelación y constitución.

Se encuentran en el sector arenas grises negruzcas provenientes del sistema Antuco y

ocasionalmente arenas claras originadas por los sedimentos cuarzosos de rocas graníticas que son

erosionadas por algún curso de agua y que llegan hasta el océano.

Por debajo de los sedimentos cuaternarios existen rocas sedimentarias marinas y

continentales, entre las que se cuentan las pizarras arcillosas y arenosas, areniscas gruesas y finas,

lutitas y mantos de carbón. Las rocas sedimentarias se asignan a la era mesozoica y al período

Eoceno del Cenozoico, con una edad variable entre 60 y 280 millones de años.

**Estratigrafía**

En el Anexo 1, se adjunta el Informe N°118537-19-00, EMPRO Ltda, en donde se

presentan los resultados de un ensayo geofísico ejecutado mediante el método ReMi para obtener

la velocidad de propagación de las ondas de corte en los primeros 30 m de profundidad cuyo

resultado se utilizara en clasificación sísmica indicada en el capítulo J.

En el mismo informe se muestra la descripción estratigráfica de 3 pozos de exploración de

2.0 m de profundidad. El plan de exploración consideraba extraer muestras profundas para realizar

ensayos de densidad y resistencia al corte, pero la presencia de napa freática impidió su obtención.

No obstante, las muestras superficiales para el diseño de pavimentos sí pudieron obtenerse los que

se presentan en el capítulo H, mientras que en el capítulo I se indican los resultados de los ensayos

de infiltración descritos en el anexo. En la Figura N°2 a la N°3 se presenta la descripción

estratigráfica de los pozos.

6

Asimismo, se incluye la descripción estratigráfica de un sondaje de 30.00 m de

profundidad. El suelo de fundación detectado corresponde a una arena fina muy limosa de

compacidad media con índices de penetración estándar superiores a los 20 golpes por pie.

El mismo anexo contiene además los resultados de 31 clasificaciones USCS completas

(incluyen: granulometrías, límites de Atterberg, humedad natural y densidad de partículas sólidas).

Las muestras cercanas al sello de fundación clasificaron principalmente como arena fina algo

limosa (SM), con contenido de finos bajo malla 0.08 mm entre un 5 y un 33%. En la Figura N°4

se presenta la descripción estratigráfica del sondaje.

De acuerdo con los resultados de exploraciones realizadas en las cercanías del sitio y las

del sitio en estudio, se distinguen principalmente 4 estratos de suelo, que para fines de diseño

pueden describirse de la siguiente manera:

**TABLA I**

**MODELO ESTRATIGRÁFICO**

|Horizonte|Profundidad (m)|Descripción|
|---|---|---|
|H-1|0.00 - 0.65|Relleno, arena fina limosa con algunas gravas dispersas y<br>maderas, humedad media, compacidad suelta.|
|H-2|0.65 - 7.50|Arena muy fina limosa, color café grisáceo, humedad alta,<br>compacidad suelta|
|H-3|7.50 - 9.20|Limo arenoso, color gris claro, humedad alta, consistencia media<br>a dura.|
|H-4|9.20 - 30.00|Arena fina limosa con conchuelas marinas, color gris oscuro,<br>humedad alta, compacidad muy compacta|

7

**Ubicación del nivel freático**

Durante la fecha de la exploración (28 y 29 de octubre de 2019), se detectó lo siguiente:

**TABLA II**

|PROFUNDIDAD|NAPA DE AGUA|
|---|---|
|Exploración|Profundidad detectada [m]|
|Pozo 1|1.90|
|Pozo 2|1.85|
|Pozo 3|<br> 1.65|

Es importante mencionar que lo anterior corresponde específicamente a la situación

registrada durante las fechas de exploración, y no considera eventuales variaciones de la

profundidad del nivel freático debido a cambios estacionales u otros motivos, ya que lo anterior

no forma parte de los alcances del estudio solicitado.

**Propiedades mecánicas del suelo de fundación**

De los resultados obtenidos de los ensayos de laboratorio y de propiedades medidas en

suelos de similares características granulométricas, propiedades índices y origen geológico, se han

adoptado conservadoramente las siguientes propiedades mecánicas para el suelo de fundación:

**Limo Arenoso (Estrato H-3)**


 = 27, ángulo de fricción interna.

c = 0.50 t/m [2], cohesión.

γ = 1.70 t/m [3], peso unitario natural.

γ b = 1.00 t/m [3], peso unitario boyante.

E = 400 + 400 _z_ t/m [2], módulo de Young si z es la profundidad en metros.

E d = 2.5 E, módulo de Young para cargas cíclicas.

μ = 0.30, razón de Poisson

8

**DIMENSIONAMIENTO DE FUNDACIONES**

**Tipo de fundaciones**

La alternativa de fundación más adecuada desde un punto de vista de mecánica de suelos,

consiste en una losa de fundación que sea capaz de resistir una subpresión determinada con la napa a

1.5 metros de profundidad con respecto a la superficie actual de terreno.

**Dimensiones mínimas de fundaciones**

Todas las fundaciones del edificio quedarán apoyadas en suelo natural y tendrán una

profundidad mínima de enterramiento de 0.8 m, medida desde la superficie del sello del radier del

subterráneo. En el caso de detectar rellenos artificiales a nivel de sello de fundación, estos se extraerán

totalmente hasta alcanzar el suelo natural. El ancho mínimo de las fundaciones será de 0.50 m para

cimientos continuos y 0.8 m para zapatas aisladas, **cuando el sello de fundación no alcance la napa** .

**Cuando el sello de fundación alcance la napa se utilizara una losa de fundación**, ésta

deberá cubrir a lo menos, un área igual a la de la planta del edificio y deberá tener un espesor

definido por cálculo. La losa deberá ser de hormigón armado, se deberá apoyar sobre suelo natural

no removido y se calculará siempre considerando el caso boyante.

Para excavaciones cercanas a fundaciones (ejemplo: drenes, estanques, etc.) se adoptará

el criterio que un plano inclinado a 45  que baja desde la esquina inferior de la fundación, debe

cortar siempre suelo natural no removido y no la excavación adyacente. Si no se cumple lo anterior,

entonces se debe profundizar el sello de fundación, hasta que dicho criterio se cumpla.

Cualquier sobreexcavación que se produzca a nivel del sello de fundación producto del

retiro de rellenos artificiales u otras causas, deberá ser rellenada con hormigón pobre de 85 kg (2

sacos) de cemento por metro cúbico de mezcla, según se indica en el acápite K.4

9

**Capacidad de soporte admisible**

La presión de contacto estática de las fundaciones, a nivel de sello de fundación, no deberá

ser superior a la presión máxima admisible determinada a partir de las siguientes expresiones:

Para D ≤ B:

_B_ _D_ _B_ _D_ _B_
_q_ _ad_  _4.0(1 0.55_  _L_ _)(1 0.40_  _B_ _) 7.5D(1_   _0.51_ _L_ _)(1 0.30_  _B_ _)_  _2.6B(1-0.40_ _L_ _)_

Para D > B:

_B_ _D_ _B_ _D_ _B_
_q_ _ad_  _4.0(1 0.55_  _L_ _)(1 0.40arctg[_  _B_ _]) 7.5D(1_   _0.51_ _L_ _)(1 0.30arctg[_  _B_ _])_  _2.6B(1-0.40_ _L_ _)_

_q_ _ad_  _28 t/m_ _2_

_Dónde:_

_q_ _ad_ _=_ _presión de contacto admisible por rotura del suelo, en t/m_ _[2]_ _._

_B_ _=_ _ancho de la fundación (lado menor), en m._

_L_ _=_ _largo de la fundación, en m._

_D_ _=_ _profundidad de fundación, en m, medida desde el nivel de sello de radier._

_Arctg =_ _función arcotangente, con el argumento en radianes._

El valor determinado de la expresión anterior es válido para cargas permanentes. Para los

efectos de combinación de carga estática permanente más eventual (sísmica) el valor de _q_ _ad_ podrá

aumentarse en un 50%.

Además de verificar que la presión de contacto de la fundación no sea mayor que _q_ _ad_, se deberá

verificar también el asentamiento máximo admisible según lo expuesto en el capítulo E.2.

10

_Ejemplos de cálculo de capacidad de soporte:_

_Cimiento corrido_

_B_ _=_ _0.40 m_

_L_ _=_ _10.00 m_

_D_ _=_ _0.80 m_

_Entonces, resulta q_ _ad_ _= 15 t/m_ _[2]_ _< 28 t/m_ _[2 ]_  _Se adopta q_ _ad_ _= 15 t/m_ _[2 ]_ _(Verificar asentamientos)_

_Zapata aislada_

_B_ _=_ _1.00 m_

_L_ _=_ _1.00 m_

_D_ _=_ _1.00 m_

_Entonces, resulta q_ _ad_ _= 25 t/m_ _[2]_ _< 28 t/m_ _[2 ]_  _Se adopta q_ _ad_ _= 25 t/m_ _[2 ]_ _(Verificar asentamientos)_

_Losa de fundación_

_B_ _=_ _25.00 m_

_L_ _=_ _55.00 m_

_D_ _=_ _1.20 m_

_Entonces, resulta q_ _ad_ _= 70.34 t/m_ _[2]_ _> 28 t/m_ _[2 ]_  _Se adopta q_ _ad_ _= 28 t/m_ _[2 ]_ _(Verificar asentamientos)_

11

**ASENTAMIENTO DE FUNDACIONES**

**Tipos de asentamientos**

Puesto que el suelo de apoyo de fundaciones corresponde a un suelo granular, los

asentamientos de las fundaciones debido a las cargas permanentes se producirán en forma inmediata.

El asentamiento instantáneo elástico debido a cargas permanentes se obtendrá de la fórmula

basada en la teoría de elasticidad tal como se detalla en el acápite E.1.1.

Para el caso de cargas dinámicas (sismo) se producirá adicionalmente una componente de

asentamiento elástico, pero con un suelo que actúa en forma más rígida que en el caso estático. Este

asentamiento se calculará de acuerdo a E.1.2.

**E.1.1** **Asentamiento para cargas permanentes**

El asentamiento elástico o inmediato de las fundaciones para el caso de cargas permanentes

se obtendrá de las siguientes expresiones:

_S_ _i_  _40091_  _q400 P B I F_ ( _0_  _3_ _B_

 _0_ _3_

_i_

(  _B_ )

, para zapatas aisladas y corridas

_q_
_S_ _i_  _k_, para losa de fundación

12

_Dónde:_

_S_ _i_ _=_ _asentamiento elástico o inmediato, en cm._

_q_ _=_ _presión de contacto promedio fundación-suelo, en t/m_ _[2]_ _._

_B_ _=_ _ancho de fundación (lado menor), en m._

_P_ _=_ _profundidad del sello de fundación, en m, medida desde el nivel de superficie de terreno._

_I_ _0_ _=_ _factor de forma según Tabla III._

_F_ _3_ _=_ _factor de enterramiento según Tabla IV._

_k_ _=_ _constante de balasto caso estático, obtenida de Tabla V, en kg/cm_ _[3]_ _._

**TABLA III**

**TABLA IV**

**FACTORES DE ENTERRAMIENTO**

|FACTORES|DE FORMA|
|---|---|
|L/B|I0|
|1.0<br>1.5<br>2.0<br>5.0<br>> 10.0|0.82<br>1.06<br>1.20<br>1.70<br>2.10|

L = Largo de fundación

|D/B|F<br>3|
|---|---|
|0.0<br>0.5<br>1.0<br>2.0<br>3.0<br>4.0<br>5.0<br>10.0|1.00<br>0.87<br>0.78<br>0.68<br>0.62<br>0.58<br>0.55<br>0.52|

D= Profundidad de fundación medida desde

el nivel de sello de radier de subterráneo

13

_Ejemplos de cálculo de asentamientos:_

_Cimiento corrido_

_B_ _=_ _0.40 m_ _I_ _0_ _=_ _2.10 (de Tabla III)_

_L_ _=_ _10.00 m_ _F_ _3_ _=_ _0.68 (de Tabla IV)_

_D_ _=_ _0.80 m_ _q_ _=_ _15 t/m_ _[2 ]_ _(supuesto)_

_P_ _=_ _7.50 m_

_Entonces, resulta S_ _i_ _= 0.22 cm_  _1.0 cm_  _O.K._

_Zapata aislada_

_B_ _=_ _1.00 m_ _I_ _0_ _=_ _0.82 (de Tabla III)_

_L_ _=_ _1.00 m_ _F_ _3_ _=_ _0.78 (de Tabla IV)_

_D_ _=_ _1.00 m_ _q_ _=_ _25 t/m_ _[2 ]_ _(supuesto)_

_P_ _=_ _7.50 m_

_Entonces, resulta S_ _i_ _= 0.38 cm_  _1.0 cm_  _O.K._

_Losa de fundación_

_B_ _= 25.00 m_

_L_ _= 55.00 m_

_q_ _=_ _20 t/m_ _[2]_ _=_ _2.0 kg/cm_ _[2]_ _(supuesto)_

_k_ _=_ _0,674 kg/cm_ _[3]_ _(de Tabla V, para un espesor de losa de 1.2 m)_

###### Entonces, resulta S i = 2.09 cm  5.0 cm  O.K.

14

**E.1.3** **Asentamiento para cargas dinámicas**

El asentamiento adicional producido por cargas dinámicas (sísmicas) verticales, se podrá

calcular, en caso de ser necesario, de las expresiones:

_S_  _36 4_ . _q_ _d_ _B I F_ _0_ _3_

_d_

_400_  _400 P_ (  _B_

_d_  . _d_ _0_ _3_

.

(  _B_ )

, para zapatas aisladas y corridas

_S_ _d_  _qk_ _d_, para losa de fundación

_d_  _d_

_d_

Donde los términos son idénticos a los de la expresión para asentamientos elásticos de cargas

estáticas, pero _S_ _d_ y _q_ _d_ son respectivamente la componente dinámica del asentamiento y la componente

dinámica de la presión.

**Asentamiento total admisible**

El asentamiento estático máximo total admisible de cada fundación (continua y/o aislada)

individual, se recomienda que no sea superior a 1/400 de la distancia entre ejes paralelos

transversales de muros y/o pilares. Este asentamiento así calculado garantiza una distorsión

angular de muros en su plano vertical inferior a 1/600, si se supone que el asentamiento máximo

diferencial es igual a 2/3 del máximo total.

**En todo caso, ninguna fundación, cimiento corrido o zapata aislada, deberá tener un**

**asentamiento total calculado superior a 1.0 cm, mientras que para losa no deberá ser superior**

**a 5.0 cm.**

15

**Constantes de balasto de fundaciones**

Las constantes de balasto para el modo de deformación por asentamientos verticales de las

fundaciones aisladas o corridas se podrán calcular de las expresiones dadas para los asentamientos,

distinguiéndose las mismas circunstancias de velocidad de aplicación de las cargas.

En general las constantes de balasto se podrán calcular de las siguientes expresiones:

_q_
_k =_ _, para cargas permanentes_
_S_ _i_

_q_ _d_
_k_ _d_ _=_ _, para cargas sísmicas_
_S_ _d_

_d_
_d_ _=_

_d_

Para losa de fundación se usarán las siguientes constantes de balasto:

**TABLA V**

**CONSTANTES DE BALASTO VERTICAL PARA LOSA DE FUNDACIÓN**

|Espesor de<br>losa (m)|Constante de balasto<br>(permanente) [kg/cm3]|Constante de balasto<br>(sísmica) [kg/cm3]|
|---|---|---|
|0.80|0.731|1.828|
|0.90|0.712|1.780|
|1.00|0.697|1.602|
|1.10|0.684|1.505|
|1.20|0.674|1.685|

(Nota: En el cálculo de las constantes de balasto se deberá utilizar unidades consistentes para obtener

valores en t/m [3] o kg/cm [3] ).

16

**Giros de fundaciones**

Para el cálculo de giros de fundaciones se podrá utilizar el concepto de la constante de balasto.

Los giros se calcularán de la expresión:

_M_
 _=_ _, radianes_
_k I_

_g_

_Dónde:_

_θ_ _=_ _Giro de la fundación, en radianes._

_k_ _g_ _=_ _Constante de balasto al giro igual a 2 veces la constante de balasto al descenso_

_vertical según E.3._

_M_ _=_ _Momento volcante a nivel del sello de fundación._

_I_ _=_ _Momento de inercia del área del sello de fundación según el eje que pasa por el centro_

_de gravedad de dicha área y en la dirección del momento considerado según la_

_convención vectorial._

17

**EMPUJES DE SUELO SOBRE MUROS**

Para los efectos de calcular los empujes de suelo sobre muros, se considerarán los

siguientes casos:

**Empuje de suelo sobre muros de subterráneos**

Para los efectos de calcular empuje de suelo sobre muros del subterráneo, se ha supuesto

que el hormigonado del muro se realizará contra terreno natural no removido considerando los

siguientes parámetros de resistencia:

- ángulo de fricción interna (  ) = 30 

- cohesión (c) = 0

- peso unitario natural (γ) = 1.80 t/m [3]

- peso unitario boyante ( [] _b_ [) = 1.00 t/m] [3]

- ángulo de fricción entre el suelo y el hormigón del muro (  ) = 0 [o]

Los valores anteriores conducen a los siguientes coeficientes de empujes:

K a = 0.33 coeficiente de empuje activo

K 0 = 0.50 coeficiente de empuje en reposo (giro nulo)

K ae = 0.47 coeficiente de empuje total sísmico para un coeficiente sísmico horizontal

de 0.20

18

**F.1.1** **Caso estático**

Para el caso estático y considerando giro nulo del muro, el empuje total se calculará

utilizando las siguientes relaciones:

Sobre la napa:

 _h_ _0.90 z_  _0.50 q_ _S_

Bajo la napa:

 _h_ _0.90h_ _w_  _0.50 ( z'_  _q )_ _S_  _z'_

_Dónde:_

_σ_ _h_ _=_ _presión horizontal sobre el muro de subterráneo, en t/m_ _[2]_ _._

_q_ _s_ _=_ _sobrecarga permanente que pudiera existir en la superficie del terreno, en t/m_ _[2]_ _._

_h_ _w_ _=_ _profundidad de la napa (considerar h_ _w_ _= 4.8 m)._

_z, z’ =_ _profundidad a la cual se desea determinar_  _h_ _, medido desde la superficie y desde el_

_nivel de la napa, respectivamente, en m._

19

**F.1.2** **Caso sísmico**

En la eventualidad de la ocurrencia de un sismo, se deberá considerar la presión estática

permanente del caso activo y un aumento sísmico de acuerdo con lo indicado en la Norma

NCh 433, el empuje total del caso sísmico (presión activa más sísmica) queda dado por la

expresión:

Sobre la napa:

_A_
 _hsis_  _0.90 z_  _0.30 C H_ _R_  _0_  _0.47 q_ _S_
_g_

Bajo la napa:

_A_
 _hsis_  _0.90h_ _w_  _0.33z' 0.30 C H_  _R_  _0_  _0.47 q_ _S_  _( z' 1)_ 
_g_

_Dónde:_

_σ_ _hsis_ _=_ _presión horizontal total debido al sismo, en t/m_ _[2]_ _._

_z, z’ =_ _profundidad a la cual se desea determinar_  _hsis_ _, medido desde la superficie y desde la_

_napa, respectivamente, en m._

_C_ _R_ _=_ _Usar 0.45._

γ _=_ _peso unitario húmedo del suelo o del relleno colocado contra el muro, en t/m_ _[3]_ _._

_H_ _=_ _altura total del muro, en m._

_q_ _s_ _=_ _sobrecarga permanente en caso sísmico, en t/m_ _[2]_ _._

_A_ _0_ _=_ _aceleración efectiva máxima del suelo, usar 0.40 g._

_g_ _=_ _aceleración de gravedad, en m/s_ _[2]_ _._

20

**Empuje de suelo sobre muros de contención**

Para los efectos de calcular el empuje de suelos sobre muros de contención que permiten

el giro, se ha supuesto que el relleno compactado trasdós es una **arena limosa con un contenido**

**de finos bajo malla 0.08 mm inferior a 15%**, con los parámetros de resistencia siguientes:

- ángulo de fricción interna (  ) = 30 

- cohesión (c) = 0

- peso unitario natural (γ) = 1.60 t/m [3]

- ángulo de fricción entre el suelo y el hormigón del muro (  ) = 0 [o]

Los valores anteriores conducen a los siguientes coeficientes de empujes:

K a = 0.33 coeficiente de empuje activo

K ae = 0.47 coeficiente de empuje total sísmico para un coeficiente sísmico horizontal

de 0.20

K p = 3.00 coeficiente de empuje pasivo

**F.2.1** **Caso estático**

El empuje de suelo sobre el muro de contención se puede expresar, para el caso estático, a

través de la siguiente relación:

 _h_ _0.528 z_  _0.33 q_ _S_

_Dónde:_

_σ_ _h_ _=_ _presión horizontal sobre el muro de contención, en t/m_ _[2]_ _._

_z_ _=_ _profundidad a la cual se desea determinar_  _h_ _, medido desde la superficie, en m._

_q_ _s_ _=_ _sobrecarga permanente que pudiera existir en la superficie del terreno, en t/m_ _[2]_ _. Para_

_h_ 

_rellenos inclinados usar sobrecarga_ _q_ _s_   []  

 _2_ 

_con h en m (ver figura siguiente)._

21

**F.2.2** **Caso sísmico**

En la eventualidad de la ocurrencia de un sismo, se deberá considerar la presión estática

permanente del caso activo y un aumento sísmico de acuerdo a una ley de triángulo invertido, la

presión total del caso sísmico (presión activa más sísmica) queda dado por la expresión:

 _hsis_  _0.528 z_  _0.16 ( H_  _z ) 0.47 q_  _S_

_Dónde:_

_σ_ _hsis_ _=_ _presión horizontal total debido al sismo, en t/m_ _[2]_ _._

_H_ _=_ _altura total del muro, en m._

_z_ _=_ _profundidad a la cual se desea determinar_  _hsis_ _, medido desde la superficie, en m._

22

**F.2.3** **Empuje pasivo**

Para el cálculo de empujes pasivos se podrá utilizar la siguiente expresión:

 _3.0 z_
_p_ _p_

_Dónde:_

_σ_ _p_ _=_ _presión pasiva horizontal sobre el muro, en t/m_ _[2]_ _._

_z_ _p_ _=_ _profundidad a la cual se desea determinar σ_ _p_ _, en m, medida desde la superficie frente_

_al extremo inferior del muro._

Para que la expresión de empuje pasivo tenga validez, la fundación deberá contar con una

superficie horizontal frente al extremo inferior del muro de una longitud igual o superior a la dada

por la expresión siguiente:

 
 

_[L D tg 45 ]_ _2_  

 _2_ 

_Dónde:_

_L_ _2_ _=_ _distancia entre extremo inferior del muro y término de la zona horizontal de suelo, en m._

_D_ _=_ _altura enterrada del muro, en m._

 _=_ _30 o, ángulo de fricción interna del suelo superficial._

23

**F.2.4** **Factores de seguridad de muros de contención**

Para el diseño en condiciones estáticas de los muros de contención se utilizará un factor de

seguridad mínimo de 1.5 al deslizamiento y vuelco si se desprecia el empuje pasivo al pie del muro

o un factor de seguridad mínimo de 2.0 al deslizamiento y vuelco si se considera el empuje pasivo

al pie del muro generado en la altura de enterramiento.

Para el caso sísmico, considerando la acción simultánea del empuje estático más la com

ponente sísmica, se aceptará un factor de seguridad mínimo de 1.3 si se desprecia el empuje pasivo

al pie del muro y de 1.5 se toma en cuenta el empuje pasivo.

**F.2.5** **Condiciones de drenaje de muro de contención**

De modo de garantizar que el muro posea suficientes condiciones de drenaje, a fin de evitar

que reciba solicitaciones adicionales por presiones de agua, deberán colocarse previo al

hormigonado, barbacanas de PVC (pasadas) a través del muro de 2” de diámetro, en un reticulado

de 2x2 m, envuelta en geotextil de 200 g/m [2] o similar en su extremo no visible.

Alternativamente se recomienda usar geosintético para dren similar al TERRAM 1C1,

entre el muro y el relleno de suelo conectado a una tubería perforada basal que tenga salida al

exterior con pendientes adecuadas (se podrá utilizar pendiente del 1%). La tubería podrá ser de

PVC 110 perforado, o similar.

24

**ESPECIFICACIONES PARA RELLENOS**

**Rellenos estructurales**

En el caso que sea necesario apoyar fundaciones de estructuras menores (no del edificio)

sobre rellenos compactados controlados, se seguirán las siguientes indicaciones:

Se deberá realizar el retiro de la capa vegetal existente y de los rellenos artificiales en caso

de existir y se compactará el sello obtenido mediante 6 pasadas de rodillo vibratorio de peso

estático mínimo 6 ton.

El material de relleno deberá estar libre de basuras y desechos. Se podrá utilizar arena limosa

o una grava arenosa, con contenido de finos bajo 0.080 mm no superior a un 15% y tamaño máximo

4”. Este relleno se colocará con un sobreancho de 2.0 m con respecto a las estructuras y se compactará

en capas mediante un rodillo vibratorio de peso estático mínimo 6 ton, con 6 pasadas por cada punto

y por cada capa. El espesor máximo de capa será 30 cm en estado suelto. La humedad durante la

colocación será cercana a la óptima (  2 puntos porcentuales).

La colocación del relleno se controlará con densidades in situ, 1 por cada 250 m [2] por cada

capa, y deberá quedar con una densidad seca equivalente al 95% de la densidad seca máxima dada

por el ensaye Proctor Modificado (NCh 1534-II) o superior. La densidad de comparación se obtendrá

como el promedio simple de la densidad máxima seca obtenida en 3 ensayes Proctor Modificado

realizado en 3 muestras representativas del material de relleno.

Si bajo pavimentos de calles fuera necesaria la ejecución de un mejoramiento de suelos, se

podrá utilizar el relleno estructural anteriormente descrito, cumpliendo además con la ejecución

de un control in situ cada 50 m lineales de calle, el que deberá cumplir las mismas condiciones

anteriores.

25

**Rellenos comunes**

Para las zonas donde no se apoyen ni estructuras ni pavimentos, se utilizará un relleno

común de material granular, de tamaño máximo 4”, y con una cantidad de finos bajo malla 0.08

mm no superior a 15%, compactado con 4 pasadas de placa vibradora por cada punto, en capas de

espesor medido en estado suelto no superior a 30 cm. Se controlará visualmente las pasadas del

equipo compactador.

26

**CBR DE LA SUBRASANTE**

En el Anexo 2, se incluye también los resultados de un ensaye CBR (NCh 1534-II), que se

realizó en una muestra de suelo recompactada al 80% de la densidad relativa. Los valores obtenidos

son indicados en la Tabla VI.

**TABLA VI**

**VALORES DE CBR PARA 0.2” DE PENETRACIÓN**

|Pozo|Profundidad<br>[m]|Valor de<br>CBR [%]|Clasificación USCS<br>de la muestra|
|---|---|---|---|
|N°1|0.00 - 2.00|25|SM|
|N°2|0.00 - 1.00|36|SM|
|N°2|1.00 - 2.00|40|SM|
|N°3|0.35 - 2.00|29|SM|

De acuerdo con lo anterior, bajo pavimentos, se retirará la capa vegetal y rellenos

artificiales no controlados existentes y se compactará el sello de excavación mediante 6 pasadas

por cada punto de rodillo vibratorio de peso estático mínimo 5 toneladas, antes de ejecutar los

rellenos compactados controlados considerados en el diseño de pavimentos.

En caso de ser necesario por cota, para alcanzar el nivel de subrasante se podrá utilizar un

relleno granular de tamaño máximo 4" y no más de 15% de finos bajo 0.08 mm (malla #200). Debe

estar limpio de vegetales, escombros y basuras. Se colocará en capas de 30 cm de espesor medido

en estado suelto, con excepción de la primera capa sobre el sello de escarpe cuyo espesor será

15 cm. Se compactará cada capa con rodillo vibratorio de peso estático mínimo 5 toneladas

mediante 6 pasadas por cada punto. Cada capa del relleno se controlará con densidades in situ y

deberá quedar con una densidad seca equivalente al 95% de la densidad máxima compactada seca

(D.M.C.S.) dada por el ensaye Proctor Modificado (NCh 1534-II) u 80% de la densidad relativa.

Se hará como mínimo 1 control de densidad por cada capa por cada 100 m lineales de calle. La

densidad de comparación se obtendrá como el promedio simple de la D.M.C.S. obtenida en 3

ensayes Proctor Modificado, realizadas en 3 muestras representativas del material de relleno.

27

**CAPACIDAD DE INFILTRACIÓN DEL SUELO**

En Anexo 1 se presenta el detalle de un ensaye de infiltración según el método Porchet.

Los resultados obtenidos se exponen en la Tabla VII siguiente:

**TABLA VII**

**RESULTADOS DE ENSAYOS DE INFILTRACIÓN MÉTODO PORCHET**

|Pozo|Profundidad [m]|Capacidad de<br>infiltración [mm/hora]|Tipo de suelo|
|---|---|---|---|
|N°2|1.00|13|Arena limosa|
|N°3|1.00|8|Arena limosa|

Considerando las características de las gravas arenosas y los resultados del ensaye de

infiltración efectuado, se recomienda utilizar una capacidad de infiltración de 20 mm/hora para

drenes con sello ubicado en grava areno limosa.

28

**CLASIFICACIÓN SEGÚN NORMA SÍSMICA**

Para los fines de la utilización de la norma sísmica se considerará un suelo con los valores

de parámetros correspondientes al de tipo D.

La clasificación del suelo se realizó según Decreto Supremo No61 de 13 de Diciembre de

2011 que modifica la Norma NCh 433 Of. 96 Mod. 2009 "Diseño sísmico de edificios", en

consideración de los resultados de la exploración, que indican que el suelo de fundación

corresponde arenas algo limosas de compacidad densa con una velocidad de onda de corte de los

primeros 30 m de suelo igual a 208 m/s, según se muestra en el anexo 1 en donde además se

encuentra el sondaje.

29

**RECOMENDACIONES DE CONSTRUCCIÓN**

La construcción de las fundaciones se atendrá a las recomendaciones indicadas en los párrafos

siguientes:

K.1. Antes de iniciar las excavaciones, se debe realizar la extracción de todos los rellenos

artificiales, donde sea necesario.

K.2. Las excavaciones para fundaciones podrán ser realizadas a máquina o manualmente con

taludes verticales hasta 1.2 m de profundidad. Los últimos 0.10 m antes de llegar al sello de

excavación, deberán ser realizados manualmente con el propósito de obtener un sello libre de

material suelto, removido o perturbado.

K.3. Si existieran localmente rellenos artificiales en los sellos de fundaciones, éstos deberán

extraerse totalmente. El exceso de excavación producida por la extracción de rellenos

artificiales o por otros motivos, deberá ser rellenado con hormigón pobre.

K.4. El hormigón pobre se preparará en betonera con la cantidad mínima de agua suficiente para

darle una trabajabilidad compatible con la colocación. En su confección se utilizará una dosis

mínima de cemento de 75 kg (3 sacos) por metro cúbico de mezcla. La mezcla se compactará,

una vez colocada, con vibrador de inmersión.

K.5. Los sellos de fundaciones serán recibidos conformes por ingenieros de Horacio Musante e

Ingenieros SpA, para verificar que el tipo de suelo de fundación es de una resistencia y rigidez

igual o superior al supuesto en el presente informe.

K.6. La losa de fundación se hormigonará directamente contra terreno natural, cuando ello sea

posible.

30

K.7. Si es necesario elevar la cota de sello de radieres, se utilizará un relleno de material granular

de procedencia local, limpio de basuras y escombros y finos bajo malla 0.08 mm no superior

a 15%, compactado con 6 pasadas de placa vibradora por cada punto, en capas de espesor

medido en estado suelto no superior a 25 cm.

K.8. Bajo losa se colocará una capa de material granular limpio. Dicho material tendrá un

tamaño máximo de 1 1⁄2", y con un contenido de finos bajo 0.08 mm no mayor al 5%, y se

compactará con un mínimo de 6 pasadas de placa vibradora por un mismo punto, quedando

con un espesor no inferior a 10 cm.

K.9. La pendiente de los patios será tal que durante la construcción y en el futuro, las aguas lluvias

no se acumulen en el perímetro del edificio.

K.10. Las excavaciones masivas se realizaran con taludes temporales de inclinación no superior

a 35° con respecto a la horizontal. Taludes de mayor inclinación deberán reforzarse y/o

entibarse. Las paredes de estos deberán ser humectadas de manera regular con el objetivo de

generar una cohesión aparente, que mejore la condición de estabilidad del terreno.

K.11. Las paredes de taludes temporales deberá ser regada con abundante lechada agua cemento con

una dosis A/C=1/1.

K.12. El relleno tras los muros de contención será una arena de tamaño máximo 4 " de origen local,

que se compactará por capas de espesor medido suelto no superior a 25 cm, mediante 6

pasadas de placa vibradora por cada punto de cada capa. Sobre este relleno no se apoyará

ninguna estructura.

K.13. Para efectos del cálculo de la subpresión, se deberá considerar que eventualmente la napa

podría ubicarse a 1.5 m de profundidad.

K.14. Las pasadas de ductos deberán sellarse para quedar estancas.

31

Cualquier situación no prevista en el presente informe o cualquier modificación que se desee

realizar a su contenido, deberá ser consultada y aprobada por quien suscribe.

SANTIAGO, noviembre de 2020.

Horacio M. Musante H.

**Ingeniero Civil**

_**T:\1 PROYECTOS\1 HMUSANTE E ING\2019\Proyecto 6452 - MS - Hualpen - FRAN\2 Area Técnica\Informes\Rev. 2\6452 - MS - Cristobal Colon**_

_**- Hualpen - Rev2_FRANdocx**_

32

# Anexo 1

#### Informe de Resultados N°118537-19-00

Proyecto N° 6452

Ejecutado por: EMPRO Ltda.

Fecha: Diciembre, de 2019.

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**INFORME DE RESULTADOS**

**N° 118537 - 19 - 00**

### ENSAYOS DE TERRENO Y LABORATORIO AVENIDA CRISTOBAL COLON No8543 HUALPEN

Solicitado por: Francisca Lezana

**DICIEMBRE 2019**

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**INFORME DE MECANICA DE SUELOS**

**N° 118537 - 19 - 00**

**TABLA DE C O N T E N I D O**

**1.- INTRODUCCIÓN .............................................................................................................................. 3**

**2.- NORMATIVA Y REFERENCIAS UTILIZADAS ...................................................................................... 3**

**3.- ENSAYOS ........................................................................................................................................ 4**

3.1.- ENSAYOS DE TERRENO **.................................................................................................................** 4

3.2.- ENSAYOS DE LABORATORIO **.........................................................................................................** 5

**A N E X O 1: ENSAYO REMI ................................................................................................................... 6**

**A N E X O 2: FOTOGRAFÍAS ................................................................................................................. 12**

**A N E X O 3: RESULTADOS DE ENSAYES DE TERRENO ......................................................................... 15**

**A N E X O 4: RESULTADOS DE ENSAYES DE LABORATORIO ................................................................. 24**

2

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**1.- Introducción**

El presente informe de resultados fue solicitado a EMPRO Ltda. por la señora Francisca

Lezana en representación de la empresa de ingeniería Musante e ingenieros. El informe tiene

por objeto entregar los resultados de los ensayos de terreno y laboratorio realizados en terrenos

de Transelec, en la comuna de Talcahuano, región del Bio Bio.

En el Anexo 1 se presenta un set fotográfico de los trabajos de terreno y laboratorio

realizados.

**2.- Normativa y referencias utilizadas**

Se incluye la documentación técnica y normativa mas relevante utilizada tanto en el

desarrollo del informe de mecánica de suelos como de los ensayos realizados en laboratorio y

terreno.

 NCh 1515. Of. 1979: Mecánica de Suelos - Determinación de la humedad. Chile, 1979.

 NCh 1532. Of. 1980: Mecánica de Suelos - Determinación de la densidad de partículas

sólidas. Chile, 1980.

 - NCh 1517. Of. 1979: Mecánica de Suelos - Límites de consistencia.

 - Ministerio de Obras Públicas. Manual de Carreteras Volumen N° 08. En su: Sección N°

8.102.1: Suelos: método para determinar la granulometría (LNV 105). Santiago 2003.

 NCh 1852. Of. 1981: Mecánica de Suelos - Determinación de la razón de soporte de

suelos compactados en laboratorio.

3

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**3.- Ensayos**

**3.1.- Ensayos de terreno**

De acuerdo a lo solicitado por el mandante se realizo sondajes geotécnicos, calicatas y

ensayos geofísicos ReMi.

 1 sondaje geotécnico de 30.00m de profundidad.

 3 calicatas de 2.00m de profundidad.

 2 ensayos de infiltración a través del método Porchet

 2 tendidos ReMi de 24 geófonos dispuestos a una separación de 3.50m entre ellos.

En el sondaje se determinó la estratigrafía del subsuelo, se midió la profundidad del nivel

freático, el índice de penetración normal por cada metro de avance en suelos y se extrajeron un

total de 31 muestras alteradas de los estratos de suelo mediante cuchara normal. Los resultados

de los ensayes de terreno se presentan en el Anexo 3.

En las calicatas se determinó la estratigrafía del subsuelo, se verifico la profundidad del

nivel freático, se realizaron ensayos de infiltración y se extrajeron un total de 4 muestras

alteradas de los estratos de suelo para ser sometidas a ensayos en el laboratorio.

A través del método ReMi se realizó un análisis espectral de las ondas superficiales

Rayleigh para la obtención del perfil de velocidades de onda de corte hasta una profundidad de

30m.

Los gráficos de profundidad vs velocidad de ondas de corte para ambos arreglos, los

gráficos de las curvas de dispersión, así como los gráficos de dispersión frecuencia vs lentitud se

presentan en el Anexo 2.

4

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**3.2.- Ensayos de laboratorio**

A muestras seleccionadas por el mandante de suelo obtenidas del sondaje y calicatas se

le efectuaron ensayos conducentes a la clasificación USCS (límites de Atterberg y

granulometría), humedad natural, peso específico y CBR.

Los resultados de los ensayes de laboratorio se presentan en el Anexo 4.

**Ignacio Ebensperger Berckemeyer**
**Ingeniero Civil en Obras Civiles**
**MSc & DIC Soil Mechanics and Engineering Seismology**
**EMPRO Ltda.**

Concepción, 5 de diciembre de 2019

5

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

###### A N E X O 1: Ensayo ReMi

6

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**1.- Metodología de trabajo Ensayo REMI**

Para obtener el registro de ondas superficiales tipo Rayleigh se utilizo un equipo

DAQlink III, es un sistema de adquisición y transferencia múltiple de datos análogos a digitales,

además de chequear previamente el terreno y asegurar que no existe accidentes geográficos ni

posibles fuentes externas que alteren a las mediciones efectuadas.

Las mediciones se realizaron mediante dos arreglos lineales con 24 geófonos de 4.5 Hz

cada uno. Estos se dispusieron en forma perpendicular. El espaciamiento entre geófonos fue de

4.00 y 3.50m por arreglo.

Para el registro de alta frecuencia se utilizo una fuente activa la cual corresponde a golpes

de un mazo de 8 Kg sobre una placa metálica. Para ambos arreglos, la placa fue posicionada en

el eje de estos a una distancia de 6m de los extremos.

**2.- Resultados**

En Tabla No7 se presenta la disposición de los perfiles realizados.

**Tabla N°7:** Geometría Arreglos Perfiles

|Perfil|N° geófonos|Distancia<br>entre<br>geófonos (m)|Longitud<br>arreglo (m)|
|---|---|---|---|
|**T1**|24|4.00|96|
|**T2**|24|3.50|84|

Para el cálculo de las velocidades de onda de corte Vs30 se entregan como resultado su

valor, los gráficos de profundidad vs velocidad de ondas de corte para las mediciones registradas

en los arreglos T1 y T2, los graficos de velocidad vs periodo y los gráficos de frecuencia vs

lentitud.

7

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**Figura N°4:** Localización Arreglos T1 y T2

**Figura N°5:** Gráfico Dispersión Frecuencia vs Lentitud geófonos 1 - 24 arreglo T1

8

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**Figura N°6:** Curva Dispersión Periodo vs Velocidad de Onda de Corte Arreglo T1

**Figura N°7:** Velocidad Ondas de Corte Vs Profundidad Arreglo T1

9

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**Figura N°8:** Gráfico Dispersión Frecuencia vs Lentitud geófonos 1 -24 arreglo T2.

**Figura N°9:** Curva Dispersión Periodo vs Velocidad de Onda de Corte Arreglo T2

10

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**Figura N°10:** Velocidad Ondas Corte Vs Profundidad Arreglo T2

Para el cálculo de Vs30 se utilizo la expresión

donde: hi: Espesor del estrato i (m)

Vsi: Velocidad de onda de corte del estrato i (m/s)

Para los ensayos realizados se obtuvo una velocidad de ondas de corte de Vs(30) = **208**

**(m/s)** con un error de ±4 (m/s)

11

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

###### A N E X O 2: Fotografías

12

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**Figura N°11:** ReMi Tendido 1

**Figura N°12:** ReMi Tendido 2

13

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

**Figura N°13:** Sondaje S-1

14

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

###### A N E X O 3: Resultados de ensayes de terreno

15

**EMPRO LTDA.**

**Ensaye de Materiales y Prospecciones** **Suelos - Hormigones -Asfaltos**
**Paicaví N°3001** **Fono: (041)2741727** **Fax: (041)2741757** **e-mail: empro@entelchile.net** **Concepción**

**RESULTADOS DE EXPLORACIÓN DEL SUBSUELO**

**Sondaje S-1**

Norma NCh 3364 of 2014

**Informe N° 118537-19-00**

**O.T. N° 73122**

Obra: Cumbres de Hualpén
Ciudad: Concepción Equipo de perforación:

Solicitado por: Francisca Lezana Fecha de inicio 24/10/2019 Tipo de martillo:

Propietario: Musante e ingenieros Fecha término 04/11/2019 Tipo de revestimiento:

Método de avance:

Ubicación: Este: 670720 Cota de inicio: 0,00m Mantenimiento de la perforación:
Norte: 5926302 Cota de término: 30,00m Longitud de revestimiento:

Concepción Equipo de perforación: Percusión

Solicitado por: Francisca Lezana Fecha de inicio 24/10/2019 Tipo de martillo: Tambor - Soga

Musante e ingenieros Fecha término 04/11/2019 Tipo de revestimiento: HQ

Método de avance: Percusión

670720 Cota de inicio: 0,00m Mantenimiento de la perforación: Revestimiento

5926302 Cota de término: 30,00m Longitud de revestimiento: 29,50m

|PROFUNDIDAD|Col2|DESCRIPCIÓN VISUAL<br>DEL SUBSUELO|Col4|Col5|MUESTRA|Col7|COTAS|Col9|ENSAYO DE PENETRACIÓN ESTANDAR|Col11|Col12|Col13|L<br>(m)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|DE|A|A|A|A|No|TIPO|DE|A|N1|N2|N3|N|N|
|0,00<br>0,65<br>0,65<br>2,50<br>2,50<br>6,30<br>6,30<br>7,50<br>7,50<br>9,20<br>9,20<br>26,20|0,00<br>0,65<br>0,65<br>2,50<br>2,50<br>6,30<br>6,30<br>7,50<br>7,50<br>9,20<br>9,20<br>26,20|Relleno, arena fina limosa con algunas gravas dispersas y maderas, humedad media,<br>compacidad suelta.<br>Arena fina limosa, color girs oscuro, humedad alta, compacidad muy compacta.<br>Arena muy fina limosa, color gris cafesoso oscuro, humedad alta, compacidad suelta a<br>media.<br>Arena muy fina, color gris socuro, humedad alta, compacidad media a compacta.<br>Arena fina limosa, color gris claro, humedad alta, compacidad suelta.<br>Limo arenoso, color gris claro, humedad alta, consistencia media a dura.|Relleno, arena fina limosa con algunas gravas dispersas y maderas, humedad media,<br>compacidad suelta.<br>Arena fina limosa, color girs oscuro, humedad alta, compacidad muy compacta.<br>Arena muy fina limosa, color gris cafesoso oscuro, humedad alta, compacidad suelta a<br>media.<br>Arena muy fina, color gris socuro, humedad alta, compacidad media a compacta.<br>Arena fina limosa, color gris claro, humedad alta, compacidad suelta.<br>Limo arenoso, color gris claro, humedad alta, consistencia media a dura.|Relleno, arena fina limosa con algunas gravas dispersas y maderas, humedad media,<br>compacidad suelta.<br>Arena fina limosa, color girs oscuro, humedad alta, compacidad muy compacta.<br>Arena muy fina limosa, color gris cafesoso oscuro, humedad alta, compacidad suelta a<br>media.<br>Arena muy fina, color gris socuro, humedad alta, compacidad media a compacta.<br>Arena fina limosa, color gris claro, humedad alta, compacidad suelta.<br>Limo arenoso, color gris claro, humedad alta, consistencia media a dura.|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14|CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>SH<br>CN<br>CN<br>CN<br>CN<br>CN|0,65<br>1,55<br>2,57<br>3,55<br>4,60<br>5,60<br>6,55<br>7,58<br>8,30<br>8,75<br>9,62<br>10,55<br>11,60<br>12,57|1,10<br>2,00<br>3,02<br>4,00<br>5,05<br>6,05<br>7,00<br>8,03<br>8,70<br>9,20<br>10,07<br>11,00<br>12,03<br>12,97|2<br>11<br>13<br>17<br>11<br>8<br>3<br>3<br>7<br>11<br>15<br>12<br>16|3<br>10<br>3<br>20<br>17<br>15<br>3<br>3<br>12<br>15<br>40<br>37<br>38|4<br>14<br>15<br>32<br>28<br>26<br>4<br>4<br>14<br>18<br>50/14<br>4<br>50/10|7<br>24<br>18<br>52<br>45<br>41<br>7<br>7<br>26<br>33<br>R<br>R<br>R|0,40<br>0,42<br>0,40<br>0,40<br>0,40<br>0,40<br>0,42<br>0,45<br>0,40<br>0,38<br>0,40<br>0,35<br>0,40<br>0,30|
|CONTROL NAPA DE AGUA|CONTROL NAPA DE AGUA|CONTROL NAPA DE AGUA|MUESTREADOR TIPO|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|SIMBOLOGÍA DE MUESTRA|SIMBOLOGÍA DE MUESTRA|SIMBOLOGÍA DE MUESTRA|SIMBOLOGÍA DE MUESTRA|
|Fecha|Hora|Profundidad (m)|CN:<br>Cuchara Normal<br>SH:<br>Tubo Shelby<br>NQ3:<br>Barril testigo 45mm<br>HQ3:<br>Barril testigo 63mm|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|
|24-10-19|18:20|2,65|2,65|2,65|2,65|2,65|2,65|2,65|2,65|2,65|2,65|2,65|2,65|
|25-10-19|09:10|2,48|2,48|2,48|2,48|2,48|2,48|2,48|2,48|2,48|2,48|2,48|2,48|
|28-10-19|09:15|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|
|29-10-19|09:10|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|2,55|

**EMPRO LTDA.**

**Ensaye de Materiales y Prospecciones** **Suelos - Hormigones -Asfaltos**
**Paicaví N°3001** **Fono: (041)2741727** **Fax: (041)2741757** **e-mail: empro@entelchile.net** **Concepción**

**RESULTADOS DE EXPLORACIÓN DEL SUBSUELO**

**Sondaje S-1**

Norma NCh 3364 of 2014

**Informe N° 118537-19-00**

**O.T. N° 73122**

|PROFUNDIDAD|Col2|DESCRIPCIÓN VISUAL<br>DEL SUBSUELO|Col4|Col5|MUESTRA|Col7|COTAS|Col9|ENSAYO DE PENETRACIÓN ESTANDAR|Col11|Col12|Col13|L<br>(m)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|DE|A|A|A|A|No|TIPO|DE|A|N1|N2|N3|N|N|
|26,20<br>29,30<br>29,30<br>30,00|26,20<br>29,30<br>29,30<br>30,00|Arena fina limosa con conchuelas marinas, color girs oscuro, humedad alta, compacidad<br>muy compacta.<br>Arena fina limosa con conchuelas marinas, color girs claro, humedad alta, compacidad muy<br>compacta.|Arena fina limosa con conchuelas marinas, color girs oscuro, humedad alta, compacidad<br>muy compacta.<br>Arena fina limosa con conchuelas marinas, color girs claro, humedad alta, compacidad muy<br>compacta.|Arena fina limosa con conchuelas marinas, color girs oscuro, humedad alta, compacidad<br>muy compacta.<br>Arena fina limosa con conchuelas marinas, color girs claro, humedad alta, compacidad muy<br>compacta.|15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>|CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN<br>CN|13,60<br>14,62<br>15,60<br>16,55<br>17,55<br>18,59<br>19,55<br>20,58<br>21,57<br>22,60<br>23,55<br>24,58<br>25,60<br>26,55<br>27,57<br>28,55<br>29,60|13,98<br>14,99<br>15,83<br>16,67<br>17,68<br>18,73<br>19,67<br>20,71<br>21,69<br>22,72<br>23,85<br>24,87<br>25,85<br>26,80<br>27,81<br>28,69<br>29,89|20<br>17<br>25<br>50/12<br>50/13<br>50/14<br>50/12<br>50/13<br>50/12<br>50/12<br>35<br>36<br>38<br>24<br>30<br>50/14<br>35|42<br>43<br>50/8<br>50<br>50/14<br>50/10<br>50/10<br>50/9<br>50/14|50/8<br>50/7|R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R<br>R|0,32<br>0,29<br>0,30<br>0,15<br>0,15<br>0,18<br>0,20<br>0,20<br>0,15<br>0,16<br>0,30<br>0,30<br>0,30<br>0,30<br>0,20<br>0,22<br>0,30|
|CONTROL NAPA DE AGUA|CONTROL NAPA DE AGUA|CONTROL NAPA DE AGUA|MUESTREADOR TIPO|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|ENSAYO SPT|SIMBOLOGÍA DE MUESTRA|SIMBOLOGÍA DE MUESTRA|SIMBOLOGÍA DE MUESTRA|SIMBOLOGÍA DE MUESTRA|
|Fecha|Hora|Profundidad (m)|CN:<br>Cuchara Normal<br>SH:<br>Tubo Shelby<br>NQ3:<br>Barril testigo 45mm<br>HQ3:<br>Barril testigo 63mm|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|N1:<br>Número de golpes para penetrar los primeros 15cm<br>N2:<br>Número de golpes para penetrar los segundos 15cm<br>N3:<br>Número de golpes para penetrar los terceros 15cm<br>N:<br>N2 + N3|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|S/M:<br>Sin muestra recuperada<br>L:<br>Longitud de muestra<br>R:<br>Rechazo<br>r:<br>Recuperación|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||

**EMPRO LTDA.**

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos

Paicaví N°3001 Fono: (041)2741727 Fax: (041)2741757 E-mail: empro@entelchile.net Concepción

**Informe No 118537-19-00**

**O.T. No 73122**

**ESTRATIGRAFIA OBSERVADA**

**CALICATA C-1**

**OBRA:** Cumbres de Hualpén

**UBICACIÓN:** Este: 670748 Norte: 5926282

**FECHA:** 28-10-19

**COTA NAPA:** 1,90m

|Horizonte|Entre cotas|Espesor (m)|Descripción del material|
|---|---|---|---|
|H-1|0,00 - 2,00|Indef.|Arena fina limosa con restos de escombros, humedad media, color gris claro,<br>compacidad baja.|
|||||
|||||
|||||
|||||

**EMPRO LTDA.**

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos

Paicaví N°3001 Fono: (041)2741727 Fax: (041)2741757 E-mail: empro@entelchile.net Concepción

**Informe No 118537-19-00**

**O.T. No 73122**

**ESTRATIGRAFIA OBSERVADA**

**CALICATA C-2**

**OBRA:** Cumbres de Hualpén

**UBICACIÓN:** Este: 670720 Norte: 5926306

**FECHA:** 28-10-19

**COTA NAPA:** 1,85m

|Horizonte|Entre cotas|Espesor (m)|Descripción del material|
|---|---|---|---|
|H-1|0,00 - 1,00|1,00|Arena fina con gravillas, gravas y bolones TM 4", color gris claro, humedad media,<br>compacidad suelta.|
|H-2|1,00 - 2,00|Indef.|Arena limosa, color gris claro, humedad alta, compacidad suelta.|
|||||
|||||
|||||

**EMPRO LTDA.**

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos

Paicaví N°3001 Fono: (041)2741727 Fax: (041)2741757 E-mail: empro@entelchile.net Concepción

**Informe No 118537-19-00**

**O.T. No 73122**

**ESTRATIGRAFIA OBSERVADA**

**CALICATA C-3**

**OBRA:** Cumbres de Hualpén

**UBICACIÓN:** Este: 670819 Norte: 5926325

**FECHA:** 28-10-19

**COTA NAPA:** 1,65m

|Horizonte|Entre cotas|Espesor (m)|Descripción del material|
|---|---|---|---|
|H-1|0,00 - 0,35|0,35|Arena fina a media con restos de escombros, color gris claro, humedad media,<br>compacidad media.|
|H-2|0,35 - 2,00|Indef.|Arena fina limosa, color gris verdosa, poco orgánico, humedad alta, compacidad media.|
|||||
|||||
|||||

**EMPRO LTDA.**

Ensaye de Materiales y Prospecciones Suelos - Hormigones -Asfaltos

Paicaví N°3001 Fono: (041)2741727 Fax: (041)2741757 E-mail: empro@entelchile.net Concepción

**Informe No 118537-19-00**

**O.T. N° 73122**

Ubicación

Cota ensaye

Diámetro

Profundidad

Fecha

**RESULTADO ENSAYE PORCHET**

C-1

1,00 m

0,20 m

0,20 m

29-10-19

**ENSAYE DE INFILTRACIÓN**

|Nivel (mm)|Tiempo segundos|Tiempo Hrs.|Coeficiente de Infiltración<br>mm/hrs.|
|---|---|---|---|
|200|0|0,0000|45|
|190|162|0,0450|60|
|180|290|0,0806|46|
|170|465|0,1292|30|
|160|745|0,2069|14|
|150|1376|0,3822|13|
|140|2104|0,5844|17|
|130|2665|0,7403||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
||||**32**|

**Coeficiente de infiltración medio F = 32 mm/hr**

**EMPRO LTDA.**

Ensaye de Materiales y Prospecciones Suelos - Hormigones -Asfaltos

Paicaví N°3001 Fono: (041)2741727 Fax: (041)2741757 E-mail: empro@entelchile.net Concepción

**Informe No 118537-19-00**

**O.T. N° 73122**

Ubicación

Cota ensaye

Diámetro

Profundidad

Fecha

**RESULTADO ENSAYE PORCHET**

C-2

1,00 m

0,20 m

0,20 m

29-10-19

**ENSAYE DE INFILTRACIÓN**

|Nivel (mm)|Tiempo segundos|Tiempo Hrs.|Coeficiente de Infiltración<br>mm/hrs.|
|---|---|---|---|
|200|0|0,0000|21|
|190|350|0,0972|22|
|180|695|0,1931|10|
|170|1485|0,4125|11|
|160|2252|0,6256|12|
|150|3015|0,8375|9|
|140|3995|1,1097|11|
|130|4865|1,3514|12|
|120|5742|1,5950|13|
|110|6576|1,8267||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
||||**13**|

**Coeficiente de infiltración medio F = 13 mm/hr**

**EMPRO LTDA.**

Ensaye de Materiales y Prospecciones Suelos - Hormigones -Asfaltos

Paicaví N°3001 Fono: (041)2741727 Fax: (041)2741757 E-mail: empro@entelchile.net Concepción

**Informe No 118537-19-00**

**O.T. N° 73122**

Ubicación

Cota ensaye

Diámetro

Profundidad

Fecha

**RESULTADO ENSAYE PORCHET**

C-3

1,00 m

0,20 m

0,20 m

29-10-19

**ENSAYE DE INFILTRACIÓN**

|Nivel (mm)|Tiempo segundos|Tiempo Hrs.|Coeficiente de Infiltración<br>mm/hrs.|
|---|---|---|---|
|200|0|0,0000|11|
|190|641|0,1781|10|
|180|1434|0,3983|6|
|170|2715|0,7542|6|
|160|4219|1,1719||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
||||**8**|

**Coeficiente de infiltración medio F = 8 mm/hr**

**EMPRO Ltda** .

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos
Paicaví 3001 Fono 41-741727 Fax 41-741757 Email empro@entelchile.net Casilla 695 Concepción

###### A N E X O 4: Resultados de ensayes de Laboratorio

24

**EMPRO LTDA.**

**Ensaye de Materiales y Prospecciones** **Suelos - Hormigones -Asfaltos**

**Paicaví N°3001** **Fono: (041)2741727** **Fax: (041)2741757** **e-mail: empro@entelchile.net** **Casilla 695** **Concepción**

**RESULTADOS ENSAYOS DE CLASIFICACIÓN Y PROPIEDADES ÍNDICE** **Informe N° 118537-19-00**

**CUMBRES DE HUALPEN**

**SONDAJE S-1**

**O.T. N° 73122**

Peso Específico 2,832 2,865 2,783 2,798 2,827 2,845 2,792 2,653 2,791 2,688 2,888 1,789

Humedad Natural (%) 25,3 24,8 28,0 25,3 25,5 14,4 37,9 47,1 52,5 28,0 25,4 18,7

Clasificación USCS SM, SP-SM SM SM SM SP-SM ML ML ML SM SM SP-SM

Observación:

**EMPRO LTDA.**

**Ensaye de Materiales y Prospecciones** **Suelos - Hormigones -Asfaltos**

**Paicaví N°3001** **Fono: (041)2741727** **Fax: (041)2741757** **e-mail: empro@entelchile.net** **Casilla 695** **Concepción**

**RESULTADOS ENSAYOS DE CLASIFICACIÓN Y PROPIEDADES ÍNDICE** **Informe N° 118537-19-00**

**CUMBRES DE HUALPEN**

**SONDAJE S-1**

**O.T. N° 73122**

Peso Específico 2,859 2,782 2,811 2,777 2,724 2,833 2,744 2,854 2,888 2,859 2,816 2,854

Humedad Natural (%) 20,3 21,6 22,8 9,2 25,2 25,1 22,9 21,6 21,0 20,3 22,2 22,1

Clasificación USCS SP SP-SM SP-SM SP SP SP-SM SP SP-SM SP SP-SM SP SP

Observación:

**EMPRO LTDA.**

**Ensaye de Materiales y Prospecciones** **Suelos - Hormigones -Asfaltos**

**Paicaví N°3001** **Fono: (041)2741727** **Fax: (041)2741757** **e-mail: empro@entelchile.net** **Casilla 695** **Concepción**

**RESULTADOS ENSAYOS DE CLASIFICACIÓN Y PROPIEDADES ÍNDICE** **Informe N° 118537-19-00**

**CUMBRES DE HUALPEN**

**SONDAJE S-1**

Peso Específico 2,878 2,839 2,833 2,711 2,783 2,777 2,848

Humedad Natural (%) 22,0 21,7 22,0 20,1 23,1 23,1 24,3

Clasificación USCS SP-SM SP-SM SP-SM SM SP SP-SM SP-SM

Observación:

**O.T. N° 73122**

**EMPRO LTDA.**

Ensaye de Materiales y Prospecciones Suelos - Hormigones - Asfaltos

Paicaví N°3001 Fono: (041)2741727 Fax: (041)2741757 E-mail: empro@entelchile.net Concepción

**Informe No 118537-19-00**

**O.T. No 73122**

**ENSAYE DE CLASIFICACION**

|IDENTIFICACION|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Muestra No|1|2|3|4|||
|Ubicación|C-1|C-2|C-2|C-3|||
|Horizonte|H-1|H-1|H-2|H-2|||
|Cota(m)|0,00-2,00|0,00-1,00|1,00-2,00|0,35-2,00|||

**Granulometría según especificación Man. Carret. Vol.8 Sección 8.102.1 (LNV105)**

|Malla o Criba Tamaño (mm)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|6"<br>4"<br>3”<br>2 1/2"<br>2"<br>1 1/2"<br>1"<br>3/4"<br>3/8"<br>No 4<br>No 10<br>No 20<br>No 40<br>No 60<br>No 200|127,000<br>101,600<br>76,200<br>63.500<br>50.800<br>38.100<br>24.400<br>19.000<br>9.520<br>4.760<br>2.000<br>0.840<br>0.420<br>0.250<br>0.074|100<br>98<br>92<br>77<br>66<br>54<br>24|100<br>99<br>97<br>92<br>75<br>43<br>30<br>15|100<br>97<br>96<br>93<br>88<br>79<br>66<br>54<br>36|100<br>98<br>90<br>95<br>55<br>40|||

**LIMITES DE CONSISTENCIA Según NCh 1517/1 NCh 1517/2**

|Límite Líquido %|--|--|25,0|40,0|Col6|Col7|
|---|---|---|---|---|---|---|
|Límite Plástico %|--|--|21,9|29,1|||
|Indice Plástico %|NP|NP|3,1|10,9|||

**DENSIDAD DE PARTICULAS SOLIDAS Según NCh 1532**

|Peso Específico|2,742|2,800|2,718|2,689|Col6|Col7|
|---|---|---|---|---|---|---|
|Humedad natural (%)|13,8|11,5|23,1|39,4|||

Clasificación USCS SM SM SM SM

**Según NCh 1852**

CBR (%) para 0,2" de penetración

25,9 36,6 40,0 29,6