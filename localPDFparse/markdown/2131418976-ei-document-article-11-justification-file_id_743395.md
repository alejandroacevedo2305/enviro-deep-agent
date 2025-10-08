---
title: ESTUDIO DE IMPACTO AMBIENTAL PROYECTO INFRAESTRUCTURA COMPLEMENTARIA
author: Desconocido
date: D:20160516120801-04'00'
language: es
type: report
pages: 31
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO C2-4 MODELACIÓN DEL COMPORTAMIENTO DE LA PLUMA SALINA DE LA PLANTA DESALINIZADORA DEL PROYECTO AMPLIACIÓN PLANTA MEJILLONES, BAHÍA MEJILLONES, MEJILLONES, REGIÓN DE ANTOFAGASTA
-->

# ANEXO C2-4 MODELACIÓN DEL COMPORTAMIENTO DE LA PLUMA SALINA DE LA PLANTA DESALINIZADORA DEL PROYECTO AMPLIACIÓN PLANTA MEJILLONES, BAHÍA MEJILLONES, MEJILLONES, REGIÓN DE ANTOFAGASTA

**ANEXO C2-4**

**MODELACIÓN DEL COMPORTAMIENTO DE LA PLUMA SALINA DE LA PLANTA**
**DESALINIZADORA** **DEL PROYECTO AMPLIACI** ~~**Ó**~~ **N PLANTA MEJILLONES, BAH** ~~**Í**~~ **A**

**MEJILLONES, MEJILLONES, REGI** ~~**Ó**~~ **N DE ANTOFAGASTA**

**ÍNDICE**

**1.** **INTRODUCCIÓN..................................................................................................................1**

**2.** **OBJETIVO............................................................................................................................3**

2.1. Objetivos Específicos....................................................................................................3

**3.** **METODOLOGÍA ..................................................................................................................3**

3.1. Área de Estudio.............................................................................................................3

3.2. Modelación de Campo Cercano ...................................................................................6

3.3. Modelación de Campo Lejano ......................................................................................8

3.4. Batimetría, condiciones iniciales, condiciones de borde y forzantes.........................12

3.4.1 Batimetría.............................................................................................................12

3.4.2 Meteorología ........................................................................................................14

3.4.3 Marea ...................................................................................................................14

3.4.4 Temperatura y Salinidad .....................................................................................14

3.5. Simulaciones ...............................................................................................................14

**4.** **RESULTADOS ...................................................................................................................15**

4.1. Malla Flexible ..............................................................................................................15

4.2. Modelo Campo Cercano .............................................................................................17

4.3. Modelo Campo Lejano................................................................................................21

4.3.1 Verano..................................................................................................................21

4.3.2 Invierno ................................................................................................................24

**5.** **CONCLUSIONES...............................................................................................................27**

**6.** **REFERENCIAS ..................................................................................................................28**

**TABLAS**

Tabla C2-1: Información y fuente de esta y periodos utilizados para inicializar y forzar el
modelo hidrodinámico ...................................................................................10

Tabla C2-2 : Características de la grilla utilizada ..............................................................15

Tabla C2-3 : Características de la descarga de Salmuera y diseño del difusor ...............18

Tabla C2-4 : Coordenadas de Emisario (UTM, H19S, WGS-84) ......................................18

Anexo C2-4

**FIGURAS:**

Figura C2-1: Área de Estudio, Sector de ubicación Planta Molycop y ................................4

Figura C2-2: Dominio de modelación ...................................................................................5

Figura C2-3: Características de una descarga de salmuera. (Niepelt, 2007) .....................7

Figura C2-4: Diagrama de flujo de metodología a emplear...............................................11

Figura C2-5: Carta náutica SHOA No1331 edición 2004 ...................................................12

Figura C2-6: Batimetría de área de modelación. Se incluye sector costero considerando
información provista por Molycop .................................................................13

Figura C2-7: Malla flexible implementada en el dominio de modelación y batimetría
interpolada. El recuadro indica un acercamiento del área de interés de la
modelación ....................................................................................................16

Figura C2-8: Diseño del extremo del emisario...................................................................17

Figura C2-9: Perfil batimétrico obtenido en la línea de trazado del ducto de descarga de
salmuera. (Derecha: Intersección ducto con línea borde costero, Izquierda:
Extremo del emisario). Información extraída desde grilla de modelación ...18

Figura C2-10: Resultados modelación de campo cercano para los períodos modelados .19

Figura C2-11: Reducción de la salinidad .............................................................................20

Figura C2-12: Salinidad de fondo en verano con situación de menor transporte
(Condición 1) .................................................................................................22

Figura C2-13: Corte transversal de la pluma de dispersión, dirección paralelo a la costa
(a) y dirección ................................................................................................23

Figura C2-14: Salinidad de fondo en invierno con situación de máxima ............................25

Figura C2-15: Cortes verticales de la pluma de dispersión, dirección paralela a la costa (a)
y transversal a la costa (b) ............................................................................26

Anexo C2-4

**ANEXO C2-4**

**MODELACIÓN DEL COMPORTAMIENTO DE LA PLUMA SALINA DE LA PLANTA**
**DESALINIZADORA DEL PROYECTO AMPLIACIÓN PLANTA MEJILLONES, BAHÍA**

**MEJILLONES, MEJILLONES, REGIÓN DE ANTOFAGASTA**

**1.** **INTRODUCCIÓN**

El presente estudio, tiene como finalidad la realización de diversos análisis dirigidos a
modelar el comportamiento de una pluma de salmuera, proveniente desde el emisario
proyectado por Molycop como parte de su planta ubicada en la Bahía de Mejillones del Sur,
diseñado para disponer del agua de rechazo de la planta de Osmosis Inversa, el cual forma
parte del actual proyecto. Dicho emisario ha sido diseñado para maximizar la dilución de la
pluma hipersalina, minimizando de esta forma los efectos sobre el medioambiente,
especialmente aquellos relacionados con el bentos cercano a la ubicación del extremo
terminal del emisario.

Químicamente, la descarga de salmuera está conformada por agua de mar con una salinidad
mayor a la del medio circundante, condición generada por la extracción de agua desde el
flujo obtenido en la captación y el rechazo simultáneo de las sales disueltas, las cuales al
encontrarse en un volumen menor, tienen como efecto el aumento de la densidad del flujo de
descarga, el cual se convierte en un flujo hipersalino o salmuera que contiene las mismas
especies químicas que el agua de mar. El efecto de este tipo de flujos sobre los organismos
del medio ambiente se observa en la modificación de los equilibrios osmóticos y, por ende, la
introducción de mayores niveles de estrés, así como un aumento en el gasto energético
asociado a la regulación del equilibrio homeostático de las células. Si bien existe una
capacidad de adaptación a los cambios de salinidad del medio, esta se limita a umbrales de
variación específicos de cada especie. La superación de dichos umbrales en periodos cortos
de tiempo generará daños en los organismos cercanos, especialmente en aquellos que
poseen una capacidad de desplazamiento reducida desde las zonas afectadas.

Físicamente, las condiciones de aumento de la salinidad así como una variación menor en la
temperatura de la descarga, determina el aumento de la densidad de la pluma, que es
forzada a fluir de acuerdo a las características de la batimetría del fondo marino en las
proximidades del difusor o descarga. En el momento de la descarga a través de las portas
del difusor, el diseño de las mismas introduce modificaciones físicas en el flujo, aumentando
la velocidad y turbulencia de la pluma, propiciando su rápida dilución. Estas modificaciones
dependen en gran medida del diseño del difusor, el cual es expuesto en el presente informe
y utilizado en la implementación de los modelos usados como parte de la metodología del
presente estudio.

En relación al marco teórico expuesto resumidamente en los párrafos anteriores, la Autoridad
Marítima ha establecido un conjunto de procedimientos y metodologías que deben ser
seguidos para el desarrollo de estudios de tendientes a modelar el comportamiento de
plumas hipersalinas. Al respecto, la Autoridad Marítima define en su documento “Directrices
para la evaluación ambiental de proyectos industriales de desalación en jurisdicción de la
Autoridad Marítima” (DIRINMAR, 2015), la metodología a ser implementada para estos
estudios. En dicho documento, se establecen los límites en los cuales deben ser aplicadas
las diferentes metodologías necesarias en la elaboración de los estudios de plumas
hipersalinas. Es relevante en este punto la definición de los ambientes en los que cada

Anexo C2-4 - 

modelo debe ser aplicado, estableciendo definiciones operativas de campo cercano y lejano
proporcionadas por la autoridad.

Dichas definiciones se transcriben a continuación:

Campo Cercano: Gobernado por la diferencia de Temperatura y Salinidad (densidades)

y la difusión.

Campo Lejano: Gobernado por las condiciones ambientales: corrientes marinas, vientos.”

Como se desprende de dichas definiciones, el campo cercano se encontrará ubicado a corta
distancia del difusor, mientras que el campo lejano poseerá, a lo menos la escala de Bahía
Mejillones. Se especifica en dicha normativa la necesidad de realizar una modelación de
campo cercano a fin de describir el comportamiento de la pluma en las cercanías del difusor,
información que será utilizada como dato de entrada al modelo de campo lejano
seleccionado, en el cual el comportamiento de la pluma salina es modelado bajo el efecto de
forzantes tales como el viento superficial, la marea, las corrientes marinas y la estructura
termohalina de la columna de agua. Cabe agregar que el modelo de campo lejano también
es utilizado para transferir la información oceánica de estos forzantes, normalmente
disponible a gran escala, hacia el interior de la bahía, la cual es afectada por la dinámica
oceánica costera.

Considerando las recomendaciones técnicas de la Autoridad, se utiliza en el presente
estudio, en la etapa de modelación de campo cercano, la utilidad Visual Plumes v1.0, creada
por el U.S. _Environmental Protection Agency_ . Debido a que el presente estudio se centra en
la dinámica que domina la dilución de la descarga de salmuera para un difusor con múltiples
portas, se utilizará el modelo el UM3, disponible en el software Visual Plumes. Dichos
modelos serán descritos brevemente en las próximas secciones. Para la modelación de
campo lejano, se utiliza en el presente proyecto, el software MIKE, desarrollado por el
_Danish Hidraulic Institute._ Dicho software posee diversos modelos capaces de simular
fenómenos tales como la propagación del oleaje hacia la costa, el forzamiento generado por
el viento y la marea y la interacción de dichos forzantes con la batimetría costera. Este
software es el fruto de desarrollos en modelación hidrodinámica que se extienden por casi 30
años, siendo a la fecha uno de los software de modelación de mayor confiabilidad en el
mundo. Una de las características que proporcionan a los modelos MIKE una mayor
capacidad por sobre otros disponibles en el mercado, se desprende de la capacidad de
trabajar con mallas no estructuradas, las cuales permiten que las grillas generadas por el
modelo se ajusten con mayor precisión al borde costero y la batimetría, sin comprometer la
capacidad del modelo en la obtención de resultados confiables y precisos en el borde
costero. En las siguientes secciones se describen en mayor profundidad los fundamentos
teóricos de los modelos utilizados.

En resumen, el presente estudio contempla el levantamiento de información oceánica de
gran escala, la cual junto a la batimetría disponible para el área será utilizada en la
implementación de un modelo de circulación en Bahía de Mejillones, durante los meses de
Enero y Julio de 2015, correspondientes a los periodos estacionales de verano e invierno.

Anexo C2-4 - 

**2.** **OBJETIVO**

Determinar la zona de dispersión de la descarga salina proveniente de la planta
desalinizadora, evaluando su dispersión en escenarios de verano e invierno.

Para ello se establecieron los siguientes objetivos específicos:

**2.1.** **Objetivos Específicos**

Determinar el patrón de circulación en la bahía en verano e invierno.

Determinar la dilución inicial de la pluma salina e acuerdo al caudal seleccionado de
descarga en verano e invierno.

Evaluar el comportamiento de la pluma salina descargada en los escenarios
seleccionados.

**3.** **METODOLOGÍA**

**3.1.** **Área de Estudio**

MOLYCOP posee una planta Elaboradora de Bolas de Acero, la cual se encuentra ubicada
en el sector central de Bahía de Mejillones, una de las bahías de mayor desarrollo en el
ámbito industrial a lo largo de la costa de Chile (Figura C2-1). Esta bahía se caracteriza por
ser una bahía protegida a las direcciones S y SW, encontrándose totalmente expuesta a las
direcciones N a NW (4° Cuadrante). La batimetría de la bahía es relativamente suave,
existiendo un gradiente batimétrico que determina bajas profundidades a gran distancia de la
costa.

La Figura C2-2 muestra la ubicación general de Bahía Mejillones y el área general utilizada
para implementar el modelo de campo lejano. Como puede apreciarse, se ha considerado un
amplia área oceánica con el fin de posibilitar la consideración de forzantes existentes en
océano abierto, tales como el viento oceánico, las corrientes sobre la plataforma y la
existencia permanente de ondas de marea.

Anexo C2-4 - 

**Figura C2-1: Área de Estudio, Sector de ubicación Planta Molycop y**

**Emisario de Planta Desaladora.**

Leyenda

Límite de batimetría de

prospección MOLYCOP.

Trazado del Emisario.

Anexo C2-4 - 

**Figura C2-2: Dominio de modelación**

Anexo C2-4 - 

**3.2.** **Modelación de Campo Cercano**

En la Figura C2-3 se esquematizan las características de una descarga de salmuera en el
ambiente costero, pudiendo apreciarse la diferencia entre flujos de boyantez positivos y
negativos. En el caso de la presente modelación, se utilizarán los conceptos asociados a un
flujo de descarga de boyantez negativa, por cuanto el proceso de desalinización genera una
descarga de temperatura cercana a la ambiental con una alta salinidad. La conformación de
este tipo de flujo determina la presencia de un campo cercano, en donde el flujo de salmuera
describe un arco desde la salida de la porta de descarga, cayendo al fondo marino a corta
distancia.

Para determinar el aumento de salinidad que se produce al momento de que el agua
descargada se incorpora al mar, considerándose una descarga a través de un difusor, se
utilizó el programa Visual Plumes v1.0, creado por la U.S. Environmental Protection Agency
(EPA), que incluye el modelo UM3 (three-dimensional Update Merge) de tipo lagrangiano, el
ucal posee la capacidad de simular una descarga mediante una puerta simple o varias
puertas sumergidas en función de las características de la descarga y del medio ambiente
(Frick _et al_ ., 2003). Este modelo se basa en la hipótesis del área proyectada de la descarga,
en la cual se incorpora fluido hacia el interior de la pluma (Rawn _et al_ ., 1960), proceso en el
que se cuantifica la tasa en que la masa de la pluma es incorporada al medio, asumiendo
que la pluma se encuentra en un estado estacionario. Desde el punto de vista de la
implementación del modelo, su formulación lagrangiana implica que, desde el punto de
inyección en la boca de la porta, los elementos o parcelas de agua siguen la misma
trayectoria, las cuales son determinadas por las líneas de flujo estimadas (Frick _et al_ ., 1994).
Es necesario considerar en este punto que el supuesto de estado estacionario de la pluma
solo es válido si las condiciones de descarga (dependientes del diseño del difusor) así como
las condiciones ambientales se, mantienen constantes. Sin embargo, es claro que las
condiciones ambientales cambian en el tiempo, motivo por el cual se llevó a cabo un análisis
de las condiciones extremas en que se alcanza la fase final de la dilución inicial, usualmente
el punto de máximo del proceso, estableciéndose que estas condiciones se presentan
durante los meses de verano e invierno, considerándose en dicho caso las características
de la columna de agua observadas mediante los Planes Vigilancia Ambiental realizados por
MOLYCOP.

Junto a la información ambiental antes referida, el modelo de campo cercano requiere como
información de entrada las características del difusor y la descarga, correspondientes al
número de portas, ángulos vertical y horizontal de cada porta (este último respecto al norte
geográfico), diámetro de la porta, distancia al fondo y a la superficie de la porta. El efluente
es parametrizado mediante la inclusión del caudal, la temperatura y salinidad de la descarga.

Anexo C2-4 - 

**Figura C2-3: Características de una descarga de salmuera. (Niepelt, 2007)**

Como resultados de la aplicación del programa Visual Plumes en el campo cercano, se
generan los valores de un conjunto de parámetros entre los que se considera como más
relevante la distancia desde el emisario y la salinidad de la pluma. Junto a esta información,
es posible obtener una salida compuesta por 4 gráficos de los parámetros más importantes
que se desprenden de la modelación. En el presente documento se ha optado por presentar
los resultados gráficos directamente obtenidos del modelo, sin introducir ningún tipo de
modificaciones, con el fin de permitir a la autoridad la comparación directa de las corridas de
verificación con los resultados aquí presentados. Los gráficos proporcionados por Visual
Plumes para el campo cercano son los siguientes:

 Elevación de la Pluma (Plume Elevation)

Este grafico se logra mediante la generación de una vista en sentido horizontal de la pluma,
consiguiendo de esta forma la descripción del comportamiento de la pluma en la vertical. Un
punto importante que debe ser considerado en el análisis del gráfico, es la identificación del
punto en el cual la pluma toca el fondo, punto final admitido como resultado confiable del
modelo.

 Propiedades Ambientales (Ambient Properties)

Este grafico presenta la densidad del agua de mar como función de la profundidad. Los
datos presentados corresponden al parámetro sigma-t. Este grafico no tiene asociada una
dimensión espacial, sino que muestra los resultados de densidad de la pluma a lo largo de
su desarrollo.

 Vista en planta (Plan View)

En este grafico se presenta una vista en planta que muestra el comportamiento de una
pluma individual en el campo cercano, correspondiente a una representación del total de las
portas que conforman el difusor antes que se inicie la interacción entre ellas.

 Predicción de la dilución de la pluma (Plumes Dilution Prediction)

Muestra la variación de la dilución media a lo largo de la línea central de la pluma, tomando
como referencia la distancia medida desde la descarga proyectada sobre la trayectoria de la
pluma.

Anexo C2-4 - 

Los resultados obtenidos por las diferentes modelaciones realizadas deben ser comparados
con respecto a normas establecidas para este fin. En la actualidad, no existe en la
reglamentación nacional una norma para la aceptabilidad de valores de salinidad en el medio
marino, utilizándose por este motivo como referencia, la norma aplicada en Australia y Nueva
Zelandia hasta el año 2000. Dicha norma establece que las descargas salinas no podrán
exceder al 5% de la salinidad del medio (ANZECC, 1992). Si bien esta norma data de 1992,
no introdujo cambios sustanciales en las posteriores revisiones, citándose el mismo valor
antes indicado, vigente hasta la fecha (ANZECC, 2000). Sin perjuicio de lo anterior, se indica
que el valor a ser utilizado dependerá también del tipo de ecosistema, del nivel de protección
deseado, de la disponibilidad de referencias bibliográficas y de datos adecuados del lugar de
estudio.

De acuerdo a esto, se calcularon las distancias descritas por la pluma hasta lograr una
salinidad equivalente al 5% de exceso sobre la salinidad ambiental utilizada como referencia
en las modelaciones presentadas.

**3.3.** **Modelación de Campo Lejano**

Para modelar el comportamiento de la pluma salina generada por la descarga de la planta
desalinizadora proyectada, se utilizó el modelo hidrodinámico MIKE 3 en su versión de malla
flexible. Este tipo de malla permite obtener una mejor representación del área de estudio,
especialmente de la morfología de la costa y de los cambios batimétricos existentes en el
lugar, además que permite una resolución más fina en el área del proyecto.

Este modelo se basa en la solución de las ecuaciones tridimensionales incompresibles de
Navier-Stokes, a través de los flujos promedio de Reynolds, invocando la aproximación de
Boussinesq y presión hidrostática.

La ecuación de continuidad local es escrita de la forma:

∂u

∂x [+]

∂v ∂w

∂y [+] ∂z [=S ]

y las ecuaciones horizontales de _momentum_ para las componentes x e y respectivamente

son:

∂vu

∂y [+]

∂v [2]

∂y [+]

∂z∂ [(] [ν] [t]

∂u

∂t [+]

∂v

∂t [+]

∂u [2]

∂x [+]

∂uv

∂x [+]

∂wu

∂z [=fv - g]

∂wv

∂z [=-fu - g]

∂η 1

∂x [-] ρ 0

∂η 1

∂y [-] ρ 0

∂p a

∂x [-]

∂p a

∂y [-]

η

ρ 0 ∫ z [∂][ρ]

∂y

g

1

∂S
xy

∂y [)] [+F] [u] [+]

∂S
xy

∂x [+]

η

ρ 0 ∫ z [∂][ρ]

η
z dz

1

ρ 0 h [(] [∂S] ∂x [xx]

∂x

∂z∂ [(] [ν] [t]

∂u

∂z [+u] [s] [S] [)]

∂v

∂z [+v] [s] [S] [)]

∂S
y x

g

1

∂S
yy

∂y [)] [+F] [v] [+]

∂S
yy

η
z dz

1

ρ 0 h ~~[(]~~

∂x [+]

donde t es el tiempo; x, y, z son las coordenadas cartesianas; η es la elevación de la
superficie; h es la profundidad total; _d = h-η_ ; _u_, _v_ y _w_ son las componentes de la velocidad en
las direcciones x, y, z; f= 2Ωsinφ es el parámetro de Coriolis ( _Ω_ es la velocidad angular de
rotación de la Tierra, y φ es la latitud); _g_ es la aceleración de gravedad; ρ es la densidad del
agua; _S_ _xx_ _, S_ _xy_ _, S_ _yx_, y _S_ _yy_ son las componentes del tensor de estrés; _ν_ _t_ es la viscosidad
turbulenta vertical; _p_ a es la presión atmosférica; ρ 0 es la densidad de referencia del agua; _S_
es la magnitud de la descarga de los emisarios y _u_ _s_ _, v_ _s_ es la velocidad del agua descargada;
_F_ _u_ y _F_ _v_ son los términos de estrés horizontal.

Anexo C2-4 - 

El transporte y difusión de temperatura (T) y salinidad (S) está dado por las ecuaciones:

∂T∂z [)] [+H] [̂] [+T] [s] [S ]

∂T

∂T∂t [+∂uT] ∂x

∂x [+∂vT]

∂y [+ ∂wT] ∂z

[∂]
∂z [=F] [T] [+]

∂z [∂] [(] [D] [v]

∂s

∂s∂t [+∂us] ∂x

∂x [+ ∂vs]

∂y [+∂ws] ∂z

[∂]
∂z [=F] [s] [+]

∂z [∂] [(] [D] [v]

∂s
∂z ~~[)]~~ [+s] [s] [S ]

donde D v es el coeficiente vertical de difusión turbulenta, H [̂] es el intercambio de calor con la
atmósfera, T s y S s son la temperatura y salinidad de las descargas. _F_ _t_ y _F_ _s_ son los términos
de difusión turbulenta de temperatura y salinidad. La turbulencia es modelada utilizando un
esquema de clausura, y la viscosidad vertical es calculada por la expresión:

ν t =U τ h c 1
(

)

z+d

h [+c] [2] ~~[(]~~ [z+d] h

h [)]

2

donde U τ = max⁡(U τs,U bs )⁡ ; U τs,U bs son las velocidades de fricción asociadas con el estrés de
superficie y fondo, c 1 y c 2 son dos constantes que dan él perfil parabólico. La viscosidad
turbulenta horizontal en muchas aplicaciones puede ser considerada constante, o se puede
usar una viscosidad turbulenta relacionada a la longitud de escala característica
(Smagorinsky, 1963).

La viscosidad turbulenta de escala de sub grilla está dada por la siguiente fórmula,

A=c s [2] l [2] 2S ij S ij
~~√~~

donde _c_ _s_ es una constante, l es la longitud característica y S ij es la tasa de deformación.

Estas ecuaciones son resueltas usando la transformación sigma en la vertical σ=
(

z-z b

Estas ecuaciones son resueltas usando la transformación sigma en la vertical σ=
( h [)] [, que ]

varía entre 0 y 1 entre fondo y superficie, respectivamente.

La discretización de las ecuaciones primitivas es realizada usando el método de volumen
finito centrado en la celda, es decir, por la subdivisión del espacio en elementos que no se
sobreponen. En el plano horizontal se usa una malla no estructurada, y en la vertical una
estructurada, los elementos pueden ser prismas o cubos cuyas caras horizontales son
triángulos o cuadriláteros. La información utilizada tanto para inicializar el modelo como
forzarlo fue obtenida de las siguientes fuentes para los períodos indicados en la Tabla C2-1.

z-z b

Anexo C2-4 - 

**Tabla C2-1: Información y fuente de esta y periodos utilizados para inicializar y forzar**

**el modelo hidrodinámico**

|Información|Fuente de Datos|Período|
|---|---|---|
|Batimetría|Carta náutica SHOA N°1331, Edición<br>2004.<br>Global Bathymetry and Elevation Data<br>at<br>30<br>Arc<br>Seconds<br>Resolution:<br>SRTM30_PLUS<br>Batimetría<br>de<br>Prospección<br>proporcionada por MOLYCOP|2016|
|Meteorología (Viento, Presión<br>Atmosférica, Humedad Relativa,<br>Temperatura del Aire)|Modelo WRF, datos cada 1 hora|01/01/2015 -<br>01/12/2015|
|Marea|Modelo Global provisto por DHI|01/01/2015 -<br>01/12/2015|
|Temperatura, Salinidad,<br>Componentes u y v de la<br>corriente|Modelo regional MERCATOR|01/01/2015 -<br>01/12/2015|

En la Figura C2-4 se presenta un resumen de la metodología utilizada para simular la
descarga de salmuera, diferenciándose como puntos principales la utilización del modelo
Visual Plumes para campo cercano y la utilización del modelo hidrodinámico MIKE 3D FM
para la modelación del campo lejano. En dicha metodología es clave la representación del
diseño del difusor y las características y diseño del mismo.

Anexo C2-4 - 

**Figura C2-4: Diagrama de flujo de metodología a emplear**

Anexo C2-4 - 

**3.4.** **Batimetría, condiciones iniciales, condiciones de borde y forzantes**

**3.4.1** **Batimetría**

La información batimétrica para caracterizar el dominio de modelación fue obtenida desde 3
fuentes principales, estas corresponden a la carta náutica N°1331 del Servicio Hidrográfico y
Oceanográfico de la Armada SHOA (Figura C2-5), batimetrías de prospección realizadas en
el área de estudio por MOLYCOP y finalmente una base de datos proveniente de datos
grillados extraídos desde Global _Bathymetry and Elevation Data at 30 Arc Seconds_
_Resolution_ : SRTM30_PLUS. Las batimetrías obtenidas por el proyecto por MOLYCOP
cuentan con la autorización SHOA, siguiendo por este motivo los requerimientos
establecidos por la norma SHOA N°3201.

Se utilizó un área extensa y se incluyó la línea de costa como dato de sonda igual a cero
para evitar hacer extrapolaciones que generen inestabilidades numéricas por un lado y
cambios batimétricos irreales en las zonas con poca información (Figura C2-6).

**Figura C2-5: Carta náutica SHOA No1331 edición 2004**

Anexo C2-4 - 

**Figura C2-6: Batimetría de área de modelación. Se incluye sector costero**

**considerando información provista por Molycop**

Anexo C2-4 - 

**3.4.2** **Meteorología**

Para forzar el modelo se utilizó la información meteorológica extraída desde el modelo WRF
adquirido para el desarrollo de los estudios de calidad de aire considerados en el presente
proyecto, el cual tiene una resolución de 1 km e información cada 1 hora de dirección y
velocidad del viento superficial. Con esta información se cubre la variabilidad espacio
temporal de la zona de estudio que incluye las condiciones meteorológicas en el océano
costero y las condiciones sobre tierra incluyendo los efectos de la diferencias en las
ganancias y pérdidas de calor del mar y de la tierra.

**3.4.3** **Marea**

Del modelo global de marea provisto por DHI se obtuvo la variación espacio temporal del
nivel del mar para el dominio de estudio. Dicha marea tiene un rango máximo de un metro o,
que es la variación típica de la zona con un comportamiento que corresponde a una marea
semidiurna mixta con una marcada desigualdad diaria entre las pleamares y las bajamares.
Esta información se utilizó para generar los campos iniciales de nivel del mar en verano e
invierno, así como las condiciones forzantes del nivel del mar en cada una de las fronteras
abiertas del dominio de modelación. Por las características de la propagación de la onda de
marea y su descomposición en las componentes armónicas se calcula la variación del nivel
del mar para cada hora del periodo de simulación. Este modelo forma parte de las utilidades
internas del software MIKE, y fue desarrollado por el doctor M.G.G. Foreman y por el Institute
of Ocean Sciences (IOS).

**3.4.4** **Temperatura,Salinidad y Corrientes.**

Los campos tridimensionales de temperatura, salinidad y las componentes u y v de la
corriente para iniciar y forzar el dominio de modelación en verano e invierno se obtuvieron
del modelo global MERCATOR de resolución de 1/12 de grado. Estas salidas corresponden
a promedios diarios de cada una variable en 40 niveles de profundidad, las cuales fueron
llevadas mediante interpolación en la vertical a profundidades igualmente espaciadas en el
dominio y después a una grilla en la vertical uniforme mediante el método de kriging.

**3.5.** **Simulaciones**

El estudio se realizó para las dos condiciones extremas de un ciclo anual, considerándose
para tal fin un período de 30 días en verano e invierno. Los primeros 5 días se utilizaron para
la estabilización de la simulación y los 25 días siguientes son los que se consideraron para el
análisis de la dinámica del sector de estudio.

Las simulaciones realizadas fueron:

 - _Base:_ simulación en verano e invierno sin descargas.

 - _Emisario_ : simulación en verano e invierno con la descarga propuesta.

Anexo C2-4 - 

**4.** **RESULTADOS**

En esta sección se presentan los resultados del proceso de modelación en campo cercano y
campo lejano, para la etapa de operación de la planta desalinizadora que forma parte del
actual Proyecto.

**4.1.** **Malla Flexible**

La implementación del modelo incorpora en una de sus primeras etapas, la generación de
una grilla de elementos finitos la cual, como se ha indicado anteriormente, utiliza elementos
triangulares que permiten un mejor ajuste a la línea de costa digitalizada, representando con
una mayor precisión los detalles de ésta. La Tabla C2-2 presenta los resultados de la
generación de la grilla. Puede observarse que esta tiene un tamaño aproximado de 54 x 50
km, superando a las dimensiones de bahía Mejillones y la zona de interés propiamente tal.
La principal ventaja de esta configuración es que elimina la posible propagación de errores
numéricos desde los bordes de la grilla hacia el interior de esta. Como puede también
observarse en la Tabla C2-2, la grilla abarca desde profundidades superiores a los 2.000 m,
llegando hasta las cercanías de la línea de costa de más baja marea.

**Tabla C2-2 : Características de la grilla utilizada**

|Parámetro|Col2|Valor|
|---|---|---|
|Cantidad de elementos|Cantidad de elementos|2653|
|Límites (m)|Oeste|316170.160|
|Límites (m)|Este|367884.878|
|Límites (m)|Sur|7424577.51,8|
|Límites (m)|Norte|7479223.80,9|
|Profundidad<br>(m)<br>|Mínima|1|
|Profundidad<br>(m)<br>|Máxima|3098.1,4|

Anexo C2-4 - 

**Figura C2-7: Malla flexible implementada en el dominio de modelación y batimetría**
**interpolada. El recuadro indica un acercamiento del área de interés de la modelación**

Anexo C2-4 - 

**4.2.** **Modelo Campo Cercano**

Utilizando la información de los perfiles de temperatura, salinidad, y corrientes y la
información del diseño del difusor se realizó la simulación de la dilución inicial de la descarga
salina del proyecto en la condición de invierno y verano. Como se indicó en la metodología,
el modelo UM3 (incorporado en el programa Visual Plumes) requiere las características del
emisario como del medio ambiente, en este caso se consideró la descarga propuesta
mediante el difusor diseñado, considerando el caudal seleccionado para esta descarga. En la
Tabla C2-3, adjunta a continuación, se resumen las características relevantes para la
descarga de salmuera propuesta. En la Tabla C2-4 se presenta la ubicación de los puntos
notables asociados al difusor, correspondientes al extremo del difusor y al punto en el cual el
ducto se intersecta con la línea de costa. La Figura C2-9 presenta el perfil batimétrico
observado a lo largo de la extensión del emisario. Al respecto, es conveniente recordar que
el emisario se encuentra enterrado en gran parte de su longitud, descubriéndose solamente
en los puntos de mayor profundidad. La Figura C2-8 presenta el diseño del extremo del
emisario, el cual presenta una disminución en su extremo a fin de aumentar la turbulencia y
por ende la difusión de la salmuera. de la descarga.

**Figura C2-8: Diseño del extremo del emisario**

Fuente: Plano MOLYCOP 115-010-02

Anexo C2-4 - 

**Tabla C2-3 : Características de la descarga de Salmuera y diseño del difusor**

|ITEM|Valores|Unidades|
|---|---|---|
|Salinidad|47,000|PSU|
|Temperatura|23|°C|
|**Rechazo Salmuera**|**0,016435**|**m3/s**|
|**Rechazo Salmuera en cada porta**|0,016435|**m3/s**|
|Número de Portas|1|-|
|Longitud difusor.|No incluye<br>difusor|m|
|Diámetro de emisario.|250|mm|
|Diseño de la porta.|Sección transversal circular|Sección transversal circular|
|Diámetro de la porta.|125|mm|
|Altura de la porta sobre el piso marino o respecto al nivel de<br>referencia utilizado en el proyecto.|75|mm|
|Angulo del emisario con respecto al norte geográfico.|330|°|
|Angulo de las portas con respecto al plano vertical.|0|°|

**Tabla C2-4 : Coordenadas de Emisario (UTM, H19S, WGS-84)**

|Punto Notable del Emisario|Coordenada<br>Norte (m)|Coordenada<br>Este (m)|
|---|---|---|
|Extremo del Emisario|7446812.31|355950.85|
|Punto de intersección del emisario con la línea de costa.|7446696.47|356170.31|

**Figura C2-9: Perfil batimétrico obtenido en la línea de trazado del ducto de descarga de**

**salmuera. (Derecha: Intersección ducto con línea borde costero, Izquierda: Extremo**

**del emisario). Información extraída desde grilla de modelación**

Con esta información se realizó la simulación de la dilución inicial de la descarga salina del
proyecto en verano e invierno para los caudales considerados. Los resultados de este
análisis se presentan en la Figura C2-10, en donde puede apreciarse la rápida dilución de la
descarga salina. Los resultados de Visual Plumes muestran un rápido decaimiento,
evidenciándose solamente los efectos de la corriente de fondo sobre la descarga de
salmuera. Al observar el decaimiento estimado por este método para ambas estaciones, se

Anexo C2-4 - 

aprecia en la Figura C2-11 (a) y (b) la fuerte similitud entre los resultados para verano e
invierno, tanto para casos evaluados en marea vaciante como llenante, en los cuales se
aprecia una distancia máxima menor a 2 m entre el difusor y el punto en donde la pluma
alcanza el punto de cumplimiento de la norma ANZEC (2000), equivalente al exceso del 5%
de la salinidad del medioambiente, considerada esta salinidad como el promedio de la
salinidad de las capas de fondo en las cuales se realiza la liberación de la pluma de
salmuera.

**Figura C2-10: Resultados modelación de campo cercano para los períodos modelados**

Anexo C2-4 - 

**Figura C2-11: Reducción de la salinidad**

(a)

Anexo C2-4 - 

**4.3.** **Modelo Campo Lejano**

**4.3.1** **Verano**

Utilizando como base la información generada desde las diferentes corridas de Visual
Plumes, se introdujo la salinidad obtenida por dicho modelo en un punto de descarga
estimado, correspondiente al elemento de la grilla numérica más cercano al punto de
contacto de la descarga con el fondo marino. Desde dicho punto, la pluma de descarga
hipersalina se incorpora al modelo de campo lejano, en donde es sometida a la circulación y
forzamiento del modelo hidrodinámico obtenido para la Bahía de Mejillones y las áreas
aledañas. En las Figuras C2-12 a la C2-13 se muestran los resultados de transporte de la
pluma salina para el periodo de verano, durante el cual se identificó uno de los eventos de
mayor transporte en el total de los eventos estudiados

Los resultados que se presentan corresponden a aquella de mayor alcance de la pluma, la
cual se mantiene en el área de la descarga con una expansión de un diámetro no superior a
los 180 m, tomando en consideración aquellas zonas en las cuales la magnitud de la
salinidad alcanza valores levemente superiores a los ambientales (Figura C2-12). Un sector
de alta concentración de sal se mantiene en el centro de la pluma de dispersión,
correspondiente al punto de descarga, desde el cual se aprecia un fuerte gradiente de
salinidad relativo, a aproximadamente algunas decenas de metros desde la ubicación del
difusor. Posterior a este punto, la salinidad se aproxima a aquella del medio ambiente.

La observación de la variabilidad temporal de la pluma de descarga muestra una débil
asociación con la corriente de marea, la cual se traduce en una mayor dilución durante los
periodos de llenante o vaciante, disminuyendo hacia los momentos de cambio de fase de la
marea (estoa). El efecto de la corriente de marea, presente en las mediciones y en la
modelación que se llevó a cabo, funciona como un modulador cíclico de las condiciones de
descarga, ya que se mantiene siempre presente en forma independiente de las condiciones
de viento superficial, el cual es el forzante de mayor importancia en la bahía.

Con el fin de establecer el comportamiento en tres dimensiones de la pluma de descarga, se
procedió a efectuar 2 cortes transversales ortogonales, centrados en el punto de mayor
salinidad modelada para la capa de fondo (Figura C2-12). En ambas transectas se
generaron perfiles verticales de la salinidad incluyendo toda la columna de agua. El perfil
paralelo a la costa (Figura C2-13 (a)), muestra la estructura vertical y horizontal a lo largo de
la columna de agua en el sentido paralelo a la costa. En el caso de perfil oeste-este (Figura
C2-13 (b)), presenta la distribución vertical de la salinidad en el sentido de mayor gradiente
batimétrico, observándose un mayor efecto sobre el movimiento de la descarga.

Sin perjuicio del comportamiento antes descrito, se observa que la pluma de descarga del
difusor sufre una rápida dilución, estableciendo un rápido gradiente de salinidad entre la
descarga y el sector circundante.

Anexo C2-4 - 

|Figura C2-12: Salinidad de fondo en verano con situación de máxima excursión de la pluma|Col2|
|---|---|
|||
|<br>|<br>|
||Transectas para obtención de perfiles verticales.|

Anexo C2-4 - 

**Figura C2-13: Corte transversal de la pluma de dispersión, dirección paralelo a la costa (a) y dirección**

**transversa a la costa (b)**

Anexo C2-4 - 

**4.3.2** **Invierno**

En forma similar al análisis presentado para el período de verano, durante el periodo invernal
se identificó el evento de máxima excursión de la pluma de salmuera, condición que fue
analizada en forma similar al caso de verano. Como puede apreciarse en la Figura C2-14, el
evento de máxima excursión se presentó a inicios de julio, ocasión en la cual los procesos de
dispersión de la descarga de salmuera posibilitan una mayor permanencia en el tiempo de la
pluma. Los cortes paralelo a la costa y transversal a la costa presentan el comportamiento
típico de la pluma, la cual se mueve sobre el fondo marino sin llegar a superficie (Figura C215).

Es necesario apreciar que aun cuando la dispersión de la pluma es baja, esta alcanza una
extensión de 180 m en dirección paralela a la costa en dirección predominante NE. No
obstante, es importante señalar que la salinidad obtenida como resultado en las
modelaciones se mantiene en el rango de los valores ambientales detectados para esta
área, cercanos a 34,1 y 34,6 PSU (Periodo de Invierno).

Uno de los aspectos más llamativos de la condición observada durante el evento de mayor
extensión en invierno, corresponde al comparativamente alto valor de salinidad ambiental
previsto por el modelo para esta época. Esto se aprecia en toda el área de modelación,
condición que tiende a minimizar naturalmente el efecto de la descarga para este evento,
correspondiendo probablemente a la intrusión de aguas oceánicas de mayor salinidad.

Anexo C2-4 - 

|Figura C2-14: Salinidad de fondo en invierno con situación de máxima excursión de la pluma.|Col2|
|---|---|
|||
|||
|<br>|Transectas para obtención de perfiles verticales.|

Anexo C2-4 - 

**Figura C2-15: Cortes verticales de la pluma de dispersión, dirección paralela a la costa (a) y transversal a la costa (b)**

Anexo EI14 - 

**5.** **CONCLUSIONES**

De los resultados del estudio realizado se puede concluir lo siguiente:

1. La simulación realizada mediante el modelo de campo cercano dan cuenta de una

rápida disminución en la salinidad de la descarga, la cual llega a valores ambientales
en el rango de 1 a 3 m desde el punto de ubicación de la porta, observándose una
fuerte disminución de la salinidad a distancias inferiores a 2 m desde la porta. Esto
determina que el impacto de la pluma en el medio, ya en el campo lejano, sea de baja
magnitud.

2. Los resultados de las simulaciones en verano e invierno realizadas para el caudal de

0,0164 m [3] /s, muestran que la pluma de descarga es rápidamente diluida en el medio
circundante, manteniéndose una máxima extensión en direcciones paralelas a la
costa con una mínima extensión en sentido transversal. Sin perjuicio de lo anterior se
observa que debido al bajo flujo de descarga, la dilución de la pluma es
suficientemente rápida para que su salinidad se asimile a la ambiental descrita para
cada estación.

Anexo C2-4 - 

**6.** **REFERENCIAS**

Australia Department of the Environment. 2000. “Australian and New Zealand Guidelines for
Fresh and Marine Water Quality”, Volumen 1.

Becker, J.J., D.T. Sandwell, W.H.F. Smith, J. Braud, B. Binder, J. Depner, D. Fabre, J.
Factor, S. Ingalls, S-H. Kim, R. Ladner, K. Marks, S. Nelson, A. Pharaoh, R. Trimmer, J. Von
Rosenberg, G. Wallace & P. Weatherall. 2009. Global Bathymetry and Elevation Data at 30
Arc Seconds Resolution: SRTM30_PLUS, Mar. Geodesy, 32:4, 355-371.
http://topex.ucsd.edu/cgi-bin/get_srtm30.cgi; revisado en septiembre de 2014.

Dirección General del Territorio Marítimo y de Marina Mercante, Armada de Chile. 2015.
“Guía Metodológica sobre procedimientos y consideraciones ambientales básicas para la
descarga de aguas residuales mediante emisarios submarinos”.

Egbert, G.D., A.F. Bennett & M.G.G. Foreman. 1994. TOPEX/POSEIDON tides estimated
using a global inverse model. J. Geoph. Res. Ocean., 99(C12): 24821-24852.

Egbert, G.D. & S.Y. Erofeeva. 2002. Efficient inverse modeling of barotropic ocean tides. J.
Atm. Ocea. Tech., 19: 183-204.

Frick W.E., D.J. Baumgartner & C.G. Fox. 1994. Improved prediction of bending plumes,
Journal of Hydraulic Research 32(6): 935-950.

Frick, W.E., P.J.W. Roberts, L.R. Davis, J. Keyes, D.J. Baumgartner & K.P. George. 2003.
Dilution models for effluent discharges. 4 [th] Edition (Visual Plumes). Ecosystems Research
Division, NERL, ORD. US Environmental Protection Agency. 960 College Station Road,
Athens Georgia 30605-2700.

Niepelt, A.2007.Development of interfaces for the coupling of hydrodynamic models for brine
discharges from desalination plants. Diploma Thesis, UNIVERSITY OF KARLSRUHE
Institute for Hydromechanics. Alemania 100: pag. 5.

Rawn, A.M., F.R. Bowerman & N.H. Brooks. 1960. Diffusers for disposal of sewage in sea
water. Proceedings of the American Society of Civil Engineers, J.San. Eng. Div., 86: 65-105.

Smagorinsky, J. 1963. General circulation experimental with primitive equations. Mon. Wea.
Rev., 91(3): 99-164.

Anexo C2-4 - 