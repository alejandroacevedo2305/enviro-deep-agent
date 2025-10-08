---
title: Informe técnico modelación Hidrodinámica
author: Jhon
date: D:20200804104448-04'00'
language: es
type: report
pages: 47
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - _ESTUDIO DE MODELACIÓN_ _HIDRODINÁMICA DE PLUMA_ _TÉRMICA Y CALIDAD DE AGUA_ _PLANTA DE ELABORACIÓN DE_ _QUESOS Y_ _PLANTA DE TRATAMIENTO DE_ _RILES_ _LACSUR_
-->

# _ESTUDIO DE MODELACIÓN_ _HIDRODINÁMICA DE PLUMA_ _TÉRMICA Y CALIDAD DE AGUA_ _PLANTA DE ELABORACIÓN DE_ _QUESOS Y_ _PLANTA DE TRATAMIENTO DE_ _RILES_ _LACSUR_

## Simulaciones: Invierno-Primavera, 2019 Preparado para: LACSUR

1

ÍNDICE DE CONTENIDOS

**1.1.** **OBJETIVO GENERAL ............................................................................................. 4**

**1.2.** **OBJETIVOS ESPECÍFICOS ....................................................................................... 4**

**1.3.** **ANTECEDENTES DEL ÁREA DE ESTUDIO ................................................................ 4**

1.4. **DETERMINACIÓN DEL ÁREA DE INFLUENCIA PARA EFECTOS DE EVALAUCIÓN**

**AMBIENTAL** .......................................................................................................................... 5

**2.** **METODOLOGÍA ..................................................................................................... 5**

**2.1.** **DESCRIPCIÓN DE LOS MODELOS NUMÉRICOS ....................................................... 7**

**2.2.** **MODELO DE CAMPO CERCANO ............................................................................ 7**

**2.3.** **MODELO DE CAMPO LEJANO ............................................................................... 8**

**2.4.** **CÁLCULO DEL TIEMPO DE RESIDENCIA DEL AGUA ESTERO HUILMA. ................... 11**

**2.5.** **VALIDACIÓN Y CALIBRACIÓN ............................................................................. 13**

**2.6.** **CONDICIONES INICIALES DE MODELO DE CAMPO CERCANO ............................... 14**

**2.7.** **CARACTERIZACIÓN DE LA DESCARFA DEL RIL. ..................................................... 16**

**2.8.** **CAUDALES Y FLUJOS DE DESCARGA UTILIZADOS PARA LAS SIMUACIONES .......... 16**

**2.9.** **MODELO DE CAMPO CERCANO .......................................................................... 17**

**2.10.** **DOMINIO DE MODELACIÓN CAMPO LEJANO ...................................................... 17**

**2.11.** **FORZANTES ....................................................................................................... 22**

**3.** **RESULTADOS ...................................................................................................... 22**

**3.1.** **MODELACIÓN EN CAMPO CERCANO: VISUAL PLUMES: ....................................... 22**

**3.2.** **MODELACIÓN DE CAMPO LEJANO: MIKE3 HD FM ............................................... 26**

**3.3.** **SIMULACION DE PLUMA TERMICA EN CAMPO LEJANO MIKE3 HD FM ................. 28**

**4.** **TIEMPO DE RESIDENCIA ...................................................................................... 32**

**5.** **DBO** **5** **.................................................................................................................. 34**

**6.** **CONCENRACION DE NITRATO ............................................................................. 37**

2

**7.** **CONCENTRACION DE FOSFATO ........................................................................... 40**

**8.** **ACEITES Y GRASAS (APROXIMACIÓN LAGRANGIANA) .......................................... 43**

**9.** **CONCLUSIÓN ...................................................................................................... 46**

**10.** **REFERENCIAS BIBLIOGRÁFICAS............................................................................ 47**

3

1.0 INTRODUCCIÓN

La empresa LACSUR ha solicitado a AMVC SPA evaluar el alcance y extensión de la pluma térmica y
calidad de agua (DBO5, Temperatura, STS, Nitrógeno Total, Fósforo Total) para su proyecto Planta de
Elaboración de Quesos y Planta de Tratamiento de Riles LACSUR (en adelante “proyecto”) mediante
modelación numérica con la información base proporcionada por el titular del proyecto.

En este contexto, para el presente proyecto se analizó el impacto térmico de la descarga, con la
implementación de los modelos en campo cercano “VISUAL PLUMES” y campo lejano MIKE3 FM
(modelo hidrodinámico del Instituto de Hidráulica Danés, DHI) para simular la pluma térmica.
Además, se modelo la calidad del agua acoplando al modelo hidrodinámico un modelo de calidad de
agua del mismo instituto Danés llamado (MIKE21/3 WQ con nutrientes en ECOLAB) para explicar la
distribución y dispersión de elementos tales como DBO5, Temperatura, STS, Nitrógeno Total, Fósforo

Total.

1.1. **OBJETIVO** **GENERAL**

Describir los elementos vertidos en la pluma de descarga del emisario tendientes a determinar el
áreas de influencia del proyecto (descarga), y con ello proveer los antecedentes necesarios que
permitan evaluar sus potenciales impactos sobre el medio ambiente del Estero Huilma.

1.2. **OBJETIVOS** **ESPECÍFICOS**

Implementar un modelo hidrodinámico que caracterice la hidrodinámica del río en condiciones

estacionales asociados al caudal del EsteroHuilma.

Acoplar al modelo hidrodinámico un modelo de calidad de agua que considere DBO5, Temperatura,
SST, Nitrógeno Total, Fósforo Total.

1.3. **ANTECEDENTES** **DEL** **ÁREA** **DE** **ESTUDIO**

El proyecto, se ubica en la Comuna de Río Negro, Provincia de Osorno, Región de Los Lagos, cuya
ubicación geográfica será en torno al punto 40°43'7.92"S latitud Sur y 73°15'12.86"O longitud Oeste.
Que se ubicada aproximadamente a 38 km al sur de Osorno y 6 km de la Ruta 5 Sur.

El proyecto pretende la construcción y operación de una planta de elaboración de quesos, junto con
su planta de tratamiento de Riles. Los Riles a tratar serán los producidos en el proceso productivo de
LACSUR, empresa que se dedica a la fabricación exclusiva de quesos, los efluentes tratados serán
descargados al estero Huilma ( **Figura 2-1** ) durante los meses de lluvias (cuando el estero posea caudal
suficiente para la dilución), en los meses de verano serán utilizados para riego. Adicionalmente se
simulan las condiciones de caudal solicitados por los servicios (para los caudales de 112, 180 y 580
L/s). El presente documento considera además un caudal de 112 L/s (correspondiente al mes de
mayo) como el caudal más desfavorable dentro del periodo de descarga considerado por el proyecto.

4

En la planta se tratarán riles con carga orgánica, mediante la tecnología BIDA®, en la cual se realiza
el tratamiento de los riles mediante filtros biológicos dinámicos aerobios.

En el presente informe se entrega una descripción de los aspectos más relevantes del estudio de

modelación realizado. Las modelaciones desarrolladas con un criterio ambiental precautorio en las

condiciones de mayor y menor impacto empleando los datos obtenidos en la línea de base como

agentes forzantes de la circulación del río (e.g. magnitud y dirección de viento, precipitación y caudal

del rìo) levantados en el área de interés por el titular del proyecto

1.4. **DETERMINACIÓN** **DEL** **ÁREA** **DE** **INFLUENCIA** **PARA** **EFECTOS** **DE** **EVALAUCIÓN** **AMBIENTAL**

Para la determinación de las áreas de influencia de descargas de efluentes térmicos y descarga de la

Planta de Tratamiento de Riles existen varias normas y criterios aplicables.

En el presente estudio para el caso de la temperatura, se adoptó el criterio utilizado por la Comunidad

Económica Europea (EU-FFH) que dicta las directrices para la regulación de estudios ambientales que

tengan relación con la evaluación de impacto por el calentamiento o enfriamiento de las aguas del

medio ambiente. En esta se define una zona de mezcla ( ∆T< 3 _°_ C ), la cual no puede superar un radio

de 500 m de área de influencia [(http://eur-lex.europa.eu/legal-](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32009L0031))

[content/EN/TXT/?uri=celex:32009L0031). Se tiene además una referencia similar en la norma](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32009L0031))

Chilena NCH 1333 que establece que para aguas destinadas para vida acuática, no debe aumentar el

valor natural en más de 3°C, la misma norma establece que para aguas de uso recreacional las

descargas no deben superar los 30°C, siendo en este caso como máximo una temperatura de

descarga de 20oC.

Para el caso de los riles se aplica la norma Chilena NCh 1333 que establece que para aguas de uso

recreacional, o de regadío la conductividad especifica no debería superar los 750 μhoms/cm

equivalente a **750 S/cm** . Y además que los sólidos disueltos totales no deberían superar los **500 ppm**

La misma norma establece que para el caso del pH esta debe estar dentro del rango entre 6,5 y 8,3

unidades de pH. Condiciones que se cumplen debido a que los parámetros de calidad de la descarga

estarán pode debajo de los valores establecidos en las normas de referencia.

**2.** **METODOLOGÍA**

El área de estudio donde se emplazará el proyecto se ubicará aproximadamente a 8,8 km de la
confluencia entre el Estero Huilma y el Río Negro en la región de los Lagos ( **Figura 2-1**, **Tabla 2-1** ).
Este proyecto considera la descarga de un ril de agua a una temperatura ambiente la cual como
criterio precautorio se ha definido en torno a los 20oC y considera una descarga de 90 m [3] /día en su
fase de operación.

5

**Tabla 2-1. Coordenadas UTM (Datum WGS 84, zona 18G)**

|Sectores Coordenada Este (m) Coordenada Norte (m)|Col2|Col3|
|---|---|---|
|**Planta Producción**|647802|5491097|
|**Planta Riles**|647811|5491185|
|**Descarga Planta de Riles**|647506|5490949|

**Figura 2-1: Ubicación geográfica del proyecto, identificando en círculo rojo el sector de descarga.**

Para forzar el modelo de calidad de agua (ECOLAB) se utilizaron los valores de referencia promedio
para cada periodo, debido a que las diferencias entre el valor máximo y mínimo son no significativos,
lo cual es indicativo que no existe una variabilidad estacional de la calidad del agua entre primavera

e invierno del 2019.

6

2.1. **DESCRIPCIÓN** **DE** **LOS** **MODELOS** **NUMÉRICOS**

Con la información de calidad del agua (temperatura), corrientes del río (campañas de invierno y

primavera 2019) y los flujos de descarga proporcionados por LACSUR S.A., se simuló el

comportamiento de la pluma térmica en campo cercano, utilizando el modelo VISUAL PLUMES,

modulo llamado UM3 (Uddated Merge), y en campo lejano utilizando el modelo hidrodinámico 3D

que resuelve las ecuaciones de movimiento para un fluido incompresible como el software de origen

Danés llamado MIKE3. En este último caso se analizaron los escenarios más favorables y

desfavorables en términos limnológicos, dentro del periodo de descarga considerado por el proyecto,

los que corresponden a los periodos de mayo y agosto de 2019 respectivamente. Los datos que

alimentaron el modelo fueron los obtenidos durante las campañas (invierno-primavera), en los que

se midieron los parámetros de calidad de agua tales como temperatura, conductividad, pH, DBO 5,

Nutrientes (Fosfato y Nitrato), concentración de oxígeno disuelto y sólidos disueltos totales.

En virtud a que no existen otros proyectos a una distancia que pudieran tener algún efecto, no se

realiza un análisis sinérgico considerando otros aportes.

2.2. **MODELO** **DE** **CAMPO** **CERCANO**

Para calcular la dilución inicial se utilizó el modelo paramétrico de dilución y dispersión Visual Plumes

v 1.0, recomendado por la Agencia de Protección Ambiental de EE.UU (EPA), que ha sido utilizado en

numerosos estudios de este tipo a nivel mundial. Este modelo simula el comportamiento de una

pluma descargada a través de un emisario el cual puede o no contar con difusor, y cómo evoluciona

por acción de las condiciones físico químicas (temperatura, conductividad y corrientes del río) de la

columna de agua en el sector de la descarga. El modelo incluye los tres procesos dinámicos que

definen el comportamiento de una descarga submarina:

 - Dilución inicial de la pluma en el área de vertido, lo que ocurre durante los primeros minutos

después de ser descargada el agua del río,

 - Dispersión horizontal y advección de la pluma por la acción de las corrientes del río,

 - En el caso de las descargas térmicas, considera la forma en que el agua descargada interactúa

con el agua del medio. Para este caso (pluma térmica), se consideró la mezcla turbulenta en

la zona de contacto de ambas cuerpos de aguas (medio receptor y pluma térmica).

Para las presentes simulaciones se utilizó el módulo UM3 de VISUAL PLUMES, que simula una pluma

para distintos tipos de descargas simples o múltiples. Este modelo es de libre uso, disponible en la

página web de la US Enviromental Protection Agency Interface Visual Plumes (VP) (Frick _et al.,_ 2004).

Este modelo ha sido ampliamente usado tanto a nivel nacional como internacional, por lo que ha

sido evaluado y probado en varios escenarios y con distintas descargas para predecir la dilución y

decaimiento térmico de una forma más precisa (Roberts & TIan, 2004) que otros modelos de campo

cercano (RSB o CORMIX).

7

2.3. **MODELO** **DE** **CAMPO** **LEJANO**

Para simular la hidrodinámica del río y conocer la dinámica de la pluma térmica en el campo lejano

se utilizó el modelo numérico hidrodinámico Mike3 HD FM (DHI, 2016), desarrollado por el Instituto

de Hidráulica Danés (DHI). Modelo formulado en elementos finitos (malla flexible), capaz de simular

las fluctuaciones de nivel del río, variaciones de temperatura y su conductividad (flujo baroclínico) y

los flujos asociados a forzantes como son principalmente el viento.

El sistema se basa en la solución numérica de las ecuaciones hidrodinámicas incompresibles de

Navier-Stokes, utilizando el enfoque de Reynolds, los supuestos de Boussinesq y de presión

hidrostática. Además, utiliza las ecuaciones de conservación de masa y momentum considerando las

variaciones de temperatura, salinidad (agua dulce salinidad es cercana a cero) y densidad, con un

esquema turbulento de cierre.

La ecuación de continuidad local es escrita de la forma:

∂u
∂x [+ ∂v]

∂y [+ ∂w] ∂z

∂z [= S]

Y las dos ecuaciones horizontales de momentum para las componentes x e y, respectivamente son:

∂u

∂t [+ ∂u] ∂x [2]

∂y [+ ∂wu] ∂z

∂u

∂x [+ ∂vu]

∂z

= fv-- g [∂η]

ρ 0

[∂η]

∂x [−1]

∂p a

a g

∂x [−] η

∂x [+]

− [1]

∂S xy

∂y [) + F] [u]

η

ρ 0 ∫ [∂][ρ]

η [ρ] dz
z ∂x

[1]

ρ 0 h [(∂S] ∂x [xx]

∂x

+ [∂]

∂z [(ν] [t]

∂u

∂z [+ u] [s] [S)]

∂z

∂v

∂v

∂t [+ ∂uv] ∂x

∂x [+ ∂v] [2]

∂y [+ ∂wv] ∂z

∂S
yy

∂y [) + F] [v]

= −fu-- g [∂η]

ρ 0

[∂η]

∂y [−1] ρ 0

∂p a

∂S yx

a g

∂y [−] η

η

ρ 0 ∫ [∂][ρ]

η [ρ] dz
z

− [1]

ρ 0 h [(]

[1]

ρ 0 h [(]

∂S yx

∂x [+]

∂y

+ [∂]

∂z [(ν] [t]

∂v
∂z [+ v] [s] [S)]

Donde t es el tiempo; **x, y, z** son las coordenadas cartesianas; η es la elevación de la superficie; h es

la profundidad total; **d = h-η; u, v y w** son las componentes de la velocidad en las direcciones **x, y, z** ;

f= 2Ωsinφ es el parámetro de Corioles ( **Ω** es la velocidad angular de rotación de la Tierra, y φ es

la latitud); g es la aceleración de gravedad; ρ es la densidad del agua; **S** **xx** **, S** **xy** **, S** **yx** **, y S** **yy** son las

componentes del tensor de estrés; **ν** **t** es la viscosidad turbulenta vertical; **p** **a** es la presión atmosférica;

8

ρ 0 es la densidad de referencia del agua; **S** es la magnitud de la descarga de los emisarios y **u** **s** **, v** **s** es

la velocidad del agua descargada; **F** **u** **y F** **v** son los términos de estrés horizontal.

El transporte y difusión de temperatura ( **T** ) y salinidad (s) está dado por las ecuaciones:

∂T

∂T

∂t [+ ∂uT] ∂x

∂x [+ ∂vT]

∂y [+ ∂wT] ∂z

[∂]
∂z [= F] [T] [+]

∂z [(D] [v]

∂T

∂z ~~[)]~~ [ + Ĥ + T] [s] [S]

∂s
∂t [+ ∂us] ∂x

∂x [+ ∂vs]

∂y [+ ∂ws] ∂z

[∂]
∂z [= F] [s] [+]

∂z [(D] [v]

∂s
∂z ~~[)]~~ [ + s] [s] [S]

Donde **D** **v** es el coeficiente vertical de difusión turbulenta, H [̂] es el intercambio de calor con la

atmósfera (en el caso de la presente evaluación no se incorpora información relativa a radiación

solar, humedad del aire, entre otras, razón por la cual no se consideró estas variables en la

modelación debido a que es un flujo turbulento), **T** **s** **y S** **s** son la temperatura y salinidad de las

descargas. **F** **t** **y F** **s** son los términos de difusión turbulenta de temperatura y salinidad (se consideró

pese a que la conductividad llevada a unidades de salinidad es aproximadamente cero).

La turbulencia es modelada utilizando un esquema de clausura, y la viscosidad vertical es calculada

por la expresión:

)

ν t = U τ 1
h(c

z+ d

h + c 2 ~~(~~ [z+ d] h

h ~~)~~

2

Donde U τ = max⁡(U τs, U bs )⁡ ; U τs, U bs son las velocidades de fricción asociadas con el estrés de

superficie y fondo. **c** **1** y **c** **2** son dos constantes que da el perfil parabólico. Mayores antecedentes

pueden ser revisados en el manual de usuario (DHI, 2016).

Un vez que se implementó el modelo hidrodinámico, se incorporaron las ecuaciones de advección y

transporte acoplando al modelo hidrodinámico, el modelo de calidad de agua, utilizando el modelo

MIKE 21/3 WQ con nutrientes utilizando las herramientas de ECOLAB ( Figura 2-2 ) .

9

**Figura 2-2. Resumen metodológico para generar los diferentes escenarios simulados**
**utilizando el modelo comercial MIKE3, acoplado a modelo de calidad de agua MIKE21/3**

**con nutrientes implementado en ECOLAB.**

10

2.4. **CÁLCULO** **DEL** **TIEMPO** **DE** **RESIDENCIA** **DEL** **AGUA** **ESTERO** **HUILMA.**

En términos matemáticos, el tiempo de residencia se puede calcular utilizando el modelo
hidrodinámico implementado, el cual es capaz de simular el transporte de un trazador conservativo
en la región de interés. Donde las parcelas de agua presentes en el tiempo **t** **0**, en el subdominio **Ω** **i**,
pueden ser representadas como un trazador conservativo virtual, con una condición inicial **C** **i** igual a
1, y 0 en otro lugar del subdominio (Gourgue _et al.,_ 2007), de esta forma esto se puede resumir como
un modelo 2D representado por la siguiente ecuación diferencial :

[∂]

∂t [(HC] [i] [) + ∇⁡(HuC] [i] [) = ∇(Hk∇C] [i] [)]

{

C i (t 0,X⁡⁡∈⁡⁡ Ω i )⁡⁡⁡⁡⁡= 1

C i (t 0,X⁡⁡∈⁡⁡ Ω\Ω i ) = 0

Donde:

“ **H** ” es la profundidad promedio de la celda **i** .

“ **C** ” la variación de la concentración del elemento conservativo,

" **t** " el tiempo, y donde “ **K** ” es el tensor de difusividad y “ **u** ” la velocidad de la corriente.

De esta forma al integrar en función del tiempo, sobre el dominio ( **Ω** ) se puede obtener el tiempo de

residencia Θ i⁡ **:** Θ i⁡⁡(t 0 ) =

∫ t **∞** 0 ∫H(t,X)C Ω i(t,X)dX⁡dt

∫H(t Ω 0,X)C i(t0,X)dX⁡

Nota: “ **Ω** ” en este caso representa el subdominio del modelo sobre el cual se integra en cada paso
de tiempo.

Este modelo pude ser acoplado al modelo hidrodinámico utilizando las herramientas de ECOLAB
donde se incluyen las variables de estado de cualquier trazador conservativo, por ejemplo, Sólidos
totales suspendidos (STS).

11

**Figura 2-3. Resumen metodológico para calcular el tiempo de residencia de un trazador**

**pasivo, integrando sobre el dominio del modelo acoplando a MIKE3**

12

2.5. **VALIDACIÓN** **Y** **CALIBRACIÓN**

El proceso de validación se realizó utilizando los valores puntuales de medición durante las campañas

de agosto (20/21 de Agosto) y diciembre (18/20 de Diciembre) del 2019 (invierno y primavera

respectivamente), donde se midió la corriente en el río en 5 estaciones de manera de asegurar que

el balance de agua sea el correcto a partir de la malla de discretización del modelo.

Se comparó la magnitud de la corriente, medida instrumentalmente en el lecho del río en 5

estaciones diferentes (E1, a E5) con los valores predichos por la simulación del modelo

hidrodinámico, estimando algunos índices de calidad para el modelo (Dingman & Bedford, 1986). Por

ejemplo, se calculó el error definido como la diferencia entre el valor predicho por el modelo “ **mo** **i** ”

menos el valor observado “ **me** **i** ”, por lo tanto, el error estimado o residual tendrá la siguiente forma:

Donde se define la media muestral como:

Además, se estimó el error medio BIAS definido como:

Calculando además la raíz del error cuadrático medio RMS y el coeficiente de determinación,

respectivamente, definidos como:

Estos índices permiten tener una medida objetiva de la calibración del modelo. Los resultados de

estos índices fueron presentados en formato de Figuras utilizando el diagrama de Taylor (Taylor,

2001), el cual fue programado en SCILAB (Software de uso libre).

13

2.6. **CONDICIONES** **INICIALES** **DE** **MODELO** **DE** **CAMPO** **CERCANO**

**CONDICIÓN** **LIMNOLOGICA** **ESTERO** **HUILMA,** **REGIÓN** **DE** **LOS** **LAGOS**

Para determinar los valores típicos de temperatura (oC), conductividad (μS/cm), pH, SDT (ppm),

concentración de oxígeno nutrientes y DBO5 se utilizó la información de 5 estaciones en el área de

interés, proporcionadas por el titular del proyecto, las cuales fueron obtenidas del muestreo insitu y

midiendo con una soda multiparámetros HANNA modelo HI98194 debidamente calibrada. Esta

información es parte del estudio de línea base.

En la Tabla 2-2, se entregan las coordenadas de las distintas posiciones geográficas de las estaciones

consideradas para el presente informe, representadas en la Figura 2-4.

En la de las mediciones de los distintos parámetros muestreados como parte de las mediciones de

línea de base realizadas en 5 estaciones de muestreo empleado.

**Tabla 2-2. Posición geografía de las estaciones de muestreo campañas invierno y primavera**

**2019.**

Fuente: Informe de línea de base “Caracterización de fauna íctica y zona de mezcla de pluma de dilución, Estero Huilma,

Comuna de Río Negro, XIV Región de los Lagos.

14

**Figura 2-4: Ubicación geográfica de las estaciones donde se midió la corriente del Estero Huilma y**

**variables de calidad del agua durante invierno y primavera del 2019.**

Fuente: : Informe de línea de base “Caracterización de fauna íctica y zona de mezcla de pluma de dilución, Estero Huilma,
Comuna de Río Negro, XIV Región de los Lagos.

15

2.7. **CARACTERIZACIÓN** **DE** **LA** **DESCARFA** **DEL** **RIL.**

Para cumplir con el DS90, la descarga del ril en términos de su calidad deberá tener los siguientes
valores y concentraciones resumidos en la siguiente Tabla 2-3., valores que fueron asumidos como
constantes en el tiempo de la descarga con un caudal operacional de 90 m [3] /día de la planta durante
los meses de lluvias (cuando el estero Huilma, posea caudal de dilución suficiente) vale decir entre
mayo y septiembre, mientras que en los meses de verano será utilizado para riego.

Tabla 2-3. Parámetros de calidad de la descarga del ril considerados para las distintas

simulaciones.

|PARAMETRO Unidades Con dilución|Col2|Col3|
|---|---|---|
|**DBO5**|mg O2/l|300|
|**Oxígeno Disuelto**|mg/l|7,5|
|**NITRATOS**|mg/l|<75|
|**FOSFATOS**|mg/l|<15|
|**pH**|-|6,0-8,5|
|**ACEITES Y GRASAS**|mg/l|50|

2.8. **CAUDALES** **Y** **FLUJOS** **DE** **DESCARGA** **UTILIZADOS** **PARA** **LAS** **SIMUACIONES**

Para efectos de modelación, se consideraron la mínima y la máxima velocidad de la corriente del río
medida instrumentalmente (0,3 y 0,6 m/s, condiciones precautoria y más favorable a la dilución
respectivamente), considerando los distintos caudales del río (Tabla 2-4), según los datos informados

<!-- INICIO TABLA 2-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- este sentido se considera un espesor de la capa de mezcla superficial estándar, de 0,5m, ya que las capas de desratización de los modelos es discreta. 16 -->

**Tabla 2-4: Resumen de las variables utilizadas en las distintas simulaciones (caudal del río y punto****

| Simulaciones | Temperatura(oC)<br>Descarga | Caudal de<br>descarga<br>Ril<br>(m3/día) | Punto de descarga<br>(Datum WGS84, UTM<br>Zona 18G) | Col5 | Espesor de<br>la capa de<br>mezcla<br>Superficial<br>(m) | Velocidad<br>de la<br>corriente<br>(m/s) |
| --- | --- | --- | --- | --- | --- | --- |
| **Caso 1:** | 20 | 90 | 647506E | 5490949N | 0,5 | 0,3 |
| **Caso 2:** | 20 | 90 | 647506E | 5490949N | 0,5 | 0,4 |
| **Caso 3:** | 20 | 90 | 647506E | 5490949N | 0,5 | 0,5 |
| **Caso 4:** | 20 | 90 | 647506E | 5490949N | 0,5 | 0,6 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- 2.9. **MODELO** **DE** **CAMPO** **CERCANO** Los parámetros ambientales utilizados para el modelo de campo cercano se detallan en la **Tabla 2-3**, junto a los valores de las distintas variables utilizadas como condición inicial para el modelo VISUAL -->
<!-- FIN TABLA 2-4 -->

por la Dirección General de Aguas, en su Informe Técnico No000162, expediente QD-1002-61 de
fecha 7 de mayo de 2020, acogiendo la observación de los servicios e incorporando un análisis del
efecto de los caudales (112 L/s, 180 L/s y 580 L/s) considerado los datos del informe técnico de DGA.

En la Tabla 2-4, se muestran los valores de las distintas variables de corrientes y caudales del río y de
la descarga del proyecto, junto a su posición geográfica considerando una descarga superficial, en
este sentido se considera un espesor de la capa de mezcla superficial estándar, de 0,5m, ya que las
capas de desratización de los modelos es discreta.

16

**Tabla 2-4: Resumen de las variables utilizadas en las distintas simulaciones (caudal del río y punto**
**de descarga del agua de Ril y velocidad de la corriente del Estero Huilma, para las simulaciones en**

**campo cercano.**

|Simulaciones|Temperatura(oC)<br>Descarga|Caudal de<br>descarga<br>Ril<br>(m3/día)|Punto de descarga<br>(Datum WGS84, UTM<br>Zona 18G)|Col5|Espesor de<br>la capa de<br>mezcla<br>Superficial<br>(m)|Velocidad<br>de la<br>corriente<br>(m/s)|
|---|---|---|---|---|---|---|
|**Caso 1:**|20|90|647506E|5490949N|0,5|0,3|
|**Caso 2:**|20|90|647506E|5490949N|0,5|0,4|
|**Caso 3:**|20|90|647506E|5490949N|0,5|0,5|
|**Caso 4:**|20|90|647506E|5490949N|0,5|0,6|

2.9. **MODELO** **DE** **CAMPO** **CERCANO**

Los parámetros ambientales utilizados para el modelo de campo cercano se detallan en la **Tabla 2-3**,
junto a los valores de las distintas variables utilizadas como condición inicial para el modelo VISUAL
PLUMES, simulando las condiciones promedio en términos de la variación de la temperatura, mínima
y máxima magnitud de la corriente, considerando distintos escenarios para campo cercano, para las
campañas de invierno y primavera de 2019, y de los meses mayo, junio y octubre del mismo año,
asumiendo la misma calidad de agua para las distintas simulaciones, pero diferente velocidad del río
(0,3 y 0,6 m/s).

2.10. **DOMINIO** **DE** **MODELACIÓN** **CAMPO** **LEJANO**

Esta etapa corresponde al momento en que el efluente es influenciado por los factores del medio

(corrientes, vientos, temperatura, otros tributarios), una vez que termina la influencia de la propia

descarga. El modelo hidrodinámico tridimensional implementado permite predecir y visualizar la ruta

y la mezcla de la pluma después de la zona de mezcla, calculando la difusividad térmica en la ruta.

La batimetría utilizada en la implementación del modelo fue generada a partir de las secciones
generadas por el titula que son parte del Estudio hidrológico, hidráulico y mecánica fluvial. Los
datos fueron georreferenciados en coordenadas geográficas, utilizando el Datum WGS-1984.

17

**Figura 2-5. Datos batimétricos utilizados para el dominio del modelo Hidrodinámico, sobre Estero**

**Huilma, Región de Los Lagos**

18

Por razones de estabilidad numérica y de representación de los principales procesos limnológicos,

así como de las características topográficas del sector, se seleccionó un dominio que cubre un área

mayor a la zona de influencia del proyecto ( **Figura 2-6** ). Esto permite que las simulaciones

representen de manera adecuada las influencias topográficas sobre el patrón local de corriente en

cada tramo del río, y que el “ruido” o distorsión que se genera al inicio en las fronteras se reduzca, y

no se intensifique en los bordes. El dominio cubrió una distancia lineal del orden de 9,42 km.

El área de estudio se discretizó mediante una malla de elementos triangulares variables en el espacio,

aumentando la resolución de la malla en las zonas donde se necesita mayor precisión de cálculo (zona

de descarga o vertimiento y zona de desarrollo de la pluma). El dominio del modelo se discretizó

empleado un total de 2156 elementos triangulares, con 2146 nodos ( **Figura 2-6** ). Verticalmente, el

dominio se discretizó mediante 2 capas equidistantes en profundidad y el espesor de las capas varía

en el tiempo en función del nivel de agua, ya que se utilizó coordenadas sigma en la vertical ( **Figura**

**2-7** ). A esta malla flexible se le acoplo la interpolación de información batimétrica, obteniéndose,

después de los ajustes necesarios para la estabilidad numérica, la batimetría que se muestra en la

**Figura 2-6** .

19

**Figura 2-6. Malla en elementos finitos que discretiza el dominio del modelo sobre Estero Huilma, región de Los Lagos.**

20

**Figura 2-7. Discretización en la vertical utilizando coordenadas sigma.**

21

2.11. **FORZANTES**

Para forzar el modelo en las fronteras abiertas, se utilizó el caudal del río aportados por la Dirección

General de Aguas, en su Informe Técnico No000162, expediente QD-1002-61 de fecha 7 de mayo de

2020, generando el flujo de corriente a partir de los nodos en los bordes abiertos del dominio del

modelo para las estaciones invierno y primavera 2019 (20/21 de Agosto y 18/20 de Diciembre

respectivamente).

En todo el dominio evaluado, se impuso un viento variable en el tiempo y constante en el espacio,

empleando registros de vientos medidos como parte del Informe de Modelación Atmosférica

Emisiones Odorantes “Proyecto Planta de Elaboración de Quesos y Planta de Tratamiento de Riles

LACSUR.” Estudio realizado por “AMBIENTE SOCIAL, ASESORIA Y CONSULTORIA”.

**3.** **RESULTADOS**

3.1. **MODELACIÓN** **EN** **CAMPO** **CERCANO:** **VISUAL** **PLUMES:**

La evaluación de campo cercano se realizó con los parámetros de diseño descritos anteriormente,
con una temperatura promedio en torno Estero Huilma en invierno de 8,27°C que considera la
información obtenida de 5 estaciones (parte del Estudio de Ictiofauna y Pluma de Dilución, Anexo 7
de la DIA, Tabla 3-1) y, con temperatura promedio de 11,13 para la primavera ( Tabla 3-1 y Tabla

3-2 ). Los valores de velocidad considerados son las magnitudes observadas instrumentalmente,
considerando las velocidades entre el rango de 0,3 m/s y 0,6 m/s, para todos los casos.

**Tabla 3-1. Resumen de calidad del agua de los puntos de monitoreo, para cada parámetro**
**in situ, para ambos periodos del año analizados (invierno y primavera 2019).**

|PARÁMETROS COLUMNA DE AGUA|INVIERNO 2019|Col3|Col4|Col5|Col6|PRIMAVERA 2019|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|ESTACIONES DE MONITOREO|E1|E2|E3|E4|E5|E1|E2|E3|E4|E5|
|pH|7.57|7.51|7.48|7.48|7.45|7.41|7.43|7.39|7.42|7.42|
|Temperatura (°C)|8.27|8.27|8.29|8.29|8.31|11.13|11.18|11.16|11.20|11.20|
|Conductividad (μS/cm)|65|66|66|65|66|85|91|86|78|80|
|Flujo Corriente (m/s)|0.3|0.5|0.4|0.6|0.4|0.3|0.5|0.5|0.6|0.3|
|Oxigeno Disuelto (mg/L)|9.35|9.38|9.36|9.39|9.36|8.44|8.36|8.41|8.39|8.35|
|Potencial Oxido Reducción<br>(mV/Ag/AgCl)|233.9|228.5|216.7|245.5|231.1|189.5|203.4|197.6|201.1|179.8|
|Solidos Disueltos Totales (ppm)|32|36|18|35|41|67|74|49|55|73|

Fuente: Estudio de Ictiofauna y Pluma de Dilución, Anexo 7 de la DIA, preparado por EEA. E.I.R.L

22

**Tabla 3-2. Estadística básica de los parámetros de calidad de agua para cada parámetro in**

**situ, para ambos periodos del año analizados (invierno y primavera 2019).**

|PARÁMETROS COLUMNA DE AGUA|AGOSTO, 2019|Col3|Col4|DICIEMBRE. 2019|Col6|Col7|
|---|---|---|---|---|---|---|
||PROMEDIO|MAXIMO|MINIMO|PROMEDIO|MAXIMO|MINIMO|
|pH|7.50|7.57|7.45|7.41|7.43|7.39|
|Temperatura (°C)|8.29|8.31|8.27|11.17|11.20|11.13|
|Conductividad (μS/cm)|65.60|66.00|65.00|84.00|91.00|78.00|
|Flujo Corriente (m/s)|0.44|0.60|0.30|0.44|0.60|0.30|
|Oxigeno Disuelto (mg/L)|9.37|9.39|9.35|8.39|8.44|8.35|
|Potencial Oxido Reducción<br>(mV/Ag/AgCl)|231.14|245.50|216.70|194.28|203.40|179.80|
|Solidos Disueltos Totales (ppm)|32.40|41.00|18.00|63.60|74.00|49.00|

Fuente: Estudio de Ictiofauna y Pluma de Dilución, Anexo 7 de la DIA, preparado por EEA. E.I.R.L

3.1.1. **DECAIMIENTO DE PLUMA TÉRMICA**

**A)** **INVIERNO**

En la Figura 3-1, en durante el invierno se muestra el comportamiento de la pluma térmica

(decaimiento de la temperatura) en función de su distancia radial desde la fuente de descarga, para

distintas velocidades de corriente simuladas (0,3; 0,4; 0,5 y 0,6 m/s). Los resultados obtenidos con

diferentes valores de magnitud de la corriente del río para la condición inicial, mostraron un

decaimiento de la pluma en la medida que se aleja de la fuente de descarga, de forma similar para

las diferentes velocidades de la corriente.

Con respecto a la variación de temperatura de la pluma, se consideró como condición inicial de
temperatura de descarga (20°C) como criterio precautorio, asumiendo que esta temperatura
ambiental sería la más desfavorable en términos dinámicos de la descarga sobre el lecho del río en
torno al Estero Huilma. E n invierno se presentó una temperatura promedio de 8,29°C como
condición natural, donde se observó que con una velocidad de corriente del río de 0,3 m/s, a partir
de una distancia en torno a los 7,4 m desde la fuente de descarga el diferencial de temperatura es
entorno a 0,26°C con respecto a la condición natural. Al aumentar la velocidad a 0,4 m/s, a una
distancia de 8,7 m desde la fuente de descarga del ril el diferencial de temperatura es del orden de
0,26°C. Si la descarga se realiza sobre una corriente de 0,5 m/s, a una distancia de 10,1 m se
presentaría un diferencial térmico de 0,24°C y si la corriente del Estero Huilma es de 0,6 m/s a una
distancia de 11,6 m el diferencial térmico sería de 0,22°C. Por lo tanto, la temperatura de la descarga
del ril disminuye rápidamente hasta alcanzar una temperatura cercana a la natural a una distancia
muy local y menor a 12 m ( **Figura 3-1** ).

23

**Figura 3-1. Variación de la temperatura de la pluma a partir del valor inicial de descarga del**
**efluente de 90 m** **[3]** **/día condición válida para invierno 2019, resultado de simulación en campo**

**cercano utilizando modelo VISUAL PLUMES considerando distintas velocidades de corrientes del**

**río (azul magnitud mínima (caso 1: 0,3 m/s), magenta magnitud (caso2: 0,4 m/s), en negro**
**magnitud (caso 3: 0,5 m/s), en azul oscuro magnitud (caso 4: 0,6 m/s). La línea roja segmentada**
**delimita el valor de temperatura considerado como temperatura de descarga (20°C) y la línea de**

**color verde segmentada se presenta la temperatura promedio observada (8,29°C)**

**B)** **PRIMAVERA**

En la Figura 3-2, se muestra el comportamiento de la pluma térmica (decaimiento de la
temperatura) en función de su distancia radial desde la fuente de descarga para la primavera de
2019, para distintas velocidades de corriente (0,3; 0,4; 0,5 y 0,6 m/s). Los resultados obtenidos,
mostraron un decaimiento térmico local de la pluma en la medida que se aleja de la fuente de
descarga, de forma similar para las diferentes velocidades de la corriente (Figura 3-2).

Con respecto a la variación de temperatura de la pluma, se consideró como condición inicial de
temperatura de descarga (20°C) como criterio precautorio, asumiendo que esta temperatura
ambiental sería la más desfavorable en términos dinámicos de la descarga sobre el lecho del río
en torno al Estero Huilma. En primavera se presentó una temperatura promedio de 11,17°C como
condición natural, donde se observó que con una velocidad de corriente de 0,3 m/s, a partir de

24

una distancia en torno a los 7,5 m desde la fuente de descarga, el diferencial de temperatura es
entorno a 0,19°C con respecto a la condición natural. Al aumentar la velocidad a 0,4 m/s, a una
distancia de 9,2 m desde la fuente de descarga del ril, el diferencial de temperatura es del orden
de 0,18°C. Si la descarga se realiza sobre una corriente de 0,5 m/s, a una distancia de 11,0 m se
presentaría un diferencial térmico de 0,16°C y si la corriente del río en torno a Estero Hulme es
de 0,6 m/s a una distancia de 13,0 m el diferencial térmico sería de 0,15°C.

Por lo tanto, la temperatura de la descarga del ril disminuye rápidamente hasta alcanzar una
temperatura cercana a la natural a una distancia local y menor a 13 m (Figura 3-2).

**Figura 3-2. Variación de la temperatura de la pluma a partir del valor inicial de descarga del**
**efluente de 90 m** **[3]** **/día condición válida para primavera 2019, resultado de simulación en campo**

**cercano utilizando modelo VISUAL PLUMES considerando distintas velocidades de corrientes del**

**río (azul magnitud mínima (0,3 m/s), magenta magnitud (0,4 m/s), en negro magnitud (0,5 m/s),**

**en azul oscuro magnitud (0,6 m/s). La línea roja segmentada delimita el valor de temperatura**

**considerado como temperatura de descarga (20°C) y la línea de color verde segmentada se**

**presenta la temperatura promedio observada (11,17°C)**

A partir de las condiciones simuladas y descritas en los párrafos precedentes, la magnitud de las

corrientes del río, permiten que la temperatura de la descarga del ril disminuya rápidamente en un

25

tramo muy local, disminuyendo de manera progresiva la temperatura llegando a los niveles naturales

a una distancia menor a los 13 m aproximadamente, en todos los casos analizados.

Por lo tanto, la zona de impacto primario en campo cercano, tanto en la condición de invierno como

primavera se verifica en las proximidades de la descarga térmica con diferencias en temperatura

inferiores o iguales a 0,3°C respecto de la condición natural existente en el cuerpo receptor.

3.2. **MODELACIÓN** **DE** **CAMPO** **LEJANO:** **MIKE3** **HD** **FM**

Antes de conocer el comportamiento de la pluma salina en el campo lejano, fue necesario validar las

condiciones limnológicas existentes entono a Estero Huilma. La validación del modelo hidrodinámico

consistió en verificar la reproducción de los valores de corrientes observados instrumentalmente

durante el invierno y primavera 2019 (20/21 de Agosto y 18/20 de Diciembre respectivamente).

En las **Figura 3-3** y **Figura 3-4** se presenta la validación de la corriente de 5 mediciones de puntuales

durante las campañas de invierno y primavera del 2019. En primavera se observó que el modelo

representó adecuadamente las variaciones de la corrientes en cada tramo del río, estimando un error

promedio de 0,44 y BIAS -0,02, con un error cuadrático medio de su sigla en inglés RMS en torno a

0,08 y con un coeficiente de correlación en torno a 0,78 con un N=5 datos. En condición de invierno

se observó una situación similar, respecto a la corriente medida instrumentalmente y el modelado,

obteniendo un RMS en torno a 0,1 y un coeficiente de correlación en torno al 0,67, con un N=5 datos.

Los resultados fueron presentados en formato de Figura a través del diagrama de Taylor (Taylor,

2001). Esto permite representar en una sola figura los índices estadísticos más relevantes de la

validación de los datos observados con respecto a lo simulado para invierno y primavera

respectivamente ( **Figura 3-3** y **Figura 3-4** ).

26

**Figura 3-3. Diagrama de Taylor (Taylor, 2001) con la comparación de las corrientes observados (A)**

**y simuladas (B) en el lecho del río en tono a Estero Huilma durante el 20/21 de Agosto de 2019.**

0 0.1 0.2

0.99

1

0.99

1

3.3. **SIMULACION** **DE** **PLUMA** **TERMICA** **EN** **CAMPO** **LEJANO** **MIKE3** **HD** **FM**

3.3.1. **COMPORTAMIENTO DE PLUMA TÉRMICA INVIERNO**

Como parte de los resultados se muestra el comportamiento de la pluma térmica ( **Figura 3-5** ) para

mayo, asociado a un caudal de 112 L/s de forma complementaria para el periodo de invierno, debido

a que durante este mes se considera la condición más desfavorable tomando como criterio el caudal.

Para un caudal de 112L/s, las simulaciones mostraron que no se sobrepasa la norma de referencia,

ya que las diferencias térmicas simuladas no superan los 0,19oC, presentándose temperaturas

cercanas a la natural con un diferencial térmico entre 0,89 a 1,09°C ( **Figura 3-5** ), con una distancia

menor a 10 m.

En octubre ( **Figura 3-6** ), asociado a un caudal de 180L/s, al igual que el caso anterior, la pluma

térmica mostró diferencias por debajo del límite autoimpuesto ( ∆T°C < 3° en 500m de radio, sobre

el valor de base). Se observó que las diferencias térmicas no superarían los 0,19°C, considerando que

el valor de referencia como condición natural fue de 8,29°C.

Y para un caudal mayor de 580 L/s, la pluma térmica tendió a extenderse levente más hacia el sur

( **Figura 3-7** ). En este caso, fue posible observar diferencias térmicas inferiores a 0,19°C en torno a la

descarga del proyecto, con un área de influencia muy local asociado al foco de descarga e inferior al

límite autoimpuesto ( ∆T°C < 3° en 500m de radio, sobre el valor de base), observando diferencias

térmicas entre el agua vertida y la natural incluso menores a 0,19°C (Figura 3-7). En general, se

observó un rápido decaimiento de la temperatura en torno al área del proyecto ( **Figura 3-5**, **Figura**

**3-6** y **Figura 3-7** ). Condiciones muy similares a lo establecido en campo cercano debido al bajo caudal

de descarga del ril.

28

**Figura 3-5. Simulación de Pluma térmica en campo lejano, durante mayo (112L/s) tomando como referencia temperatura basal igual a**

**8,29°C como condición natural.**

29

**Figura 3-6. Simulación de Pluma térmica en campo lejano, durante octubre (180L/s) condición más desfavorable tomando como**

**referencia temperatura basal igual a 8,29°C como condición natural.**

30

**Figura 3-7. Simulación de Pluma térmica en campo lejano, con un caudal de 580L/s (Junio a septiembre) tomando como referencia**

**temperatura basal igual a 8,29°C como condición natural.**

31

De acuerdo a lo anterior, los resultados obtenidos son inferiores a la norma de la Comunidad

Económica Europea ( ∆T < 3 ° en⁡un⁡radio⁡de⁡500m⁡ ), que se consideró como referencia,

fundamentalmente por su mayor exigencia impuesta a este tipo de estudios y a la validación

científica de la misma (Hart _et al_ ., 1990, 1991).

**4.** **TIEMPO DE RESIDENCIA**

Los resultados de las simulaciones para calcular el tiempo de residencia se muestran en la **Figura 4-1**,

donde la escala de colores de la gráfica muestra la fracción de tiempo en el dominio del modelo.

Diferenciándose tres zonas, la zona inicial que incluye el área de la descarga en el estero Huilma, la

velocidad del río es lo suficiente para renovar el sistema como máximo en 2 horas, una zona

intermedia más sinuosa que tardaría en renovarse del orden de 4 horas como máximo, y una tramo

final del río, que debido a la extensión y a lo sinuoso del tramo tardaría más en renovarse (máximo 6

horas, **Figura 4-1** )

Los mayores tiempos de residencia (o permanecía) se asocian en términos ecológicos a zonas con

mayor retención de las aguas, y sus distintos componentes en la columna de agua (eg., Materia

orgánica, sedimentos, entre otros). En términos prácticos el tiempo de residencia permite identificar

las áreas o sectores con menor recambio de las aguas, lo que repercute en el empobrecimiento de la

concentración de oxígeno en la columna de agua. Destacándose en este caso que el sector donde se

ubica la descarga presenta una condición favorable debido a su rápida tasa de recambio.

32

**Figura 4-1. Estimación del tiempo de residencia en el área de estudio, considerando los meses en que se realizara la descarga del ril en**

**torno al Estero Huilma.**

33

### 5. DBO 5

Se simuló además el comportamiento del valor DBO 5 que en términos prácticos es la
cantidad de oxígeno que las bacterias y microorganismos consumen durante 5 días a una
temperatura de 20°C en una muestra de agua. Lo cual, es relevante en caso de las descargas
de riles que requerían una mayor degradación aeróbica de la composición del ril que serán

vertidas en torno al estero Huilma.

Para simular la concentración de DBO5 se consideraron los valores de calidad del agua de la

Tabla 5-1.

**Tabla 5-1. Calidad del agua muestreada en el estero Huilma.**

|MUESTREO PUNTUAL EN ESTERO<br>HUILMA. LABORATORIO DICTUC<br>PARÁMETROS COLUMNA DE AGUA|17-03-2020<br>CONCENTRACIÓN UNIDADES|Col3|
|---|---|---|
|Aceites y Grasas|<2|(mg/L)|
|DBO5<br>Fósforo|7<br>0.06|(mg O2/L)<br>(mg/L)|
|Nitrógeno total Kjeldahl|0.51|(mg/L)|
|Sólidos Suspendidos|<10|(mg/L)|

Fuente: Titular del proyecto.

Para un caudal del orden de 112L/s (mayo), condición más desfavorable, el DBO5 (Figura 5-1)
se mantienen muy cercanas a las condiciones naturales del sistema, con concentraciones
entre 6,8 a 7 mg/l en torno al proyecto, manteniéndose la calidad similar a las condiciones
naturales a partir de una distancia menor a 20 m desde la fuente de descarga (Figura 5-1).

Al simular el comportamiento del DBO5 con el máximo caudal o condición más favorable (de

junio a agosto) se pudo observar que las condiciones de calidad respecto a la concentración

de DBO5 se mantienen muy cercanas a las condiciones naturales del sistema, con

concentraciones entre 6,0 mg/l a 8 mg/L (Figura 5-2). Por esta razón cabe destacar la

relevancia del DBO5 ya que es una medida indirecta de la suma de todas las sustancias

orgánicas biodegradables presentes en agua del río que tiene relación con la concentración de

oxígeno disponible para actuar en la degradación biológica de las sustancias orgánicas.

34

**Figura 5-1. Variación de BDO5 asociado a un caudal más desfavorable para el periodo considerado para las descargas (112 L/s).**

35

**Figura 5-2. Variación de BDO5 asociado a un caudal máximo (580L/s).**

36

### 6. CONCENRACION DE NITRATO

Para simular la variación de la concentración de nitratos, con la interacción con la descarga

del ril, se trabajo bajo el supuesto de que todo el nitrógeno como nitrato aportado por la

descarga es menor a 75 mg/l( **Tabla 2-3** ), asumiendo que el caudal más desfavorable para el

periodo de vertimiento es 112L/s, se pudo observar que la concentración podría variar entre

0,48 mg/l y 0,56 mg/l, en torno a la descarga, no superar los 0,56 mg/l ( **Figura 6-1** ).

A diferencia de una condición de máximo caudal (580 L/s) donde la concentración podría

llegar a valores de entorno a la descarga del proyecto (entre 0,2 y 0,3 mg/l, **Figura 6-1** ),

Las bajas concentraciones muestran que existe una capacidad de bajo consumo nitratos

probablemente asociado al bajo tiempo de residencia de las aguas en torno a la descarga

debido al flujo turbulento del río debido al caudal ( **Figura 6-1** **y** **Figura 6-2** ).

37

**Figura 6-1. Variación máxima estimada de la concentración de nitratos con un caudal más desfavorable para el periodo considerado**

**para las descargas (112 L/s).**

38

**Figura 6-2. Variación máxima estimada de la concentración de nitratos con un caudal máximo (580 L/s)**

39

### 7. CONCENTRACION DE FOSFATO

Para simular la variación de la concentración de fosfatos, con la interacción con la descarga

del ril, se trabajo bajo el supuesto de que todo el fosforo que es aportado por la descarga es

menor a 15 mg/l ( **Tabla 2-3** ), y la calidad del agua presenta una concentración de 0,06 mg/L.

Cuando el caudal del río es en torno a 112L/s, asumida como la condición más desfavorable

para el periodo de descarga del ril considerada por el proyecto (asociado al mes de mayo),

el tramo del río de mayor intensidad de la corriente, que presenta a su vez el menor tiempo

de residencia, podrían presentarse concentraciones entre 0,06 a 0,08 mg/l como máximo

( **Figura 7-1** ). Si el caudal es mucho mayor, como el que se podría presentar de junio a

septiembre (580L/s), se extiende el área de menor concentración, y en torno al área de

descarga se podrían presentar concentraciones menores a 0,08 mg/l ( **Figura 7-2** ).

40

**Figura 7-1. Variación máxima estimada de la concentración de fosfato con un caudal más desfavorable para el periodo considerado para**

**las descargas (112 L/s).**

41

**Figura 7-2. Variación máxima estimada de la concentración de fosfato con un máximo (580 L/s).**

42

### 8. ACEITES Y GRASAS (APROXIMACIÓN LAGRANGIANA)

Para simular el comportamiento de los aceites y grasas se utilizó una aproximación
Lagrangiana, debido a la naturaleza de estas, ya que poseen boyantes, y tienden a
dispersarce sobre la capa superficial, y en la medida que viajan por el río van sufriendo
procesos oxidativos que los disgregan y dispersan pudiendo distribuirse en una menor o
mayor área dependiendo del caudal del río y su velocidad.

Las partículas lagrangianas tiendes a permaneces agregadas en su viaje hacia el sur del área
del proyecto, observando una distribución de las partículas que se extiende de forma casi
continua con una baja disgregación de las partículas cuando el caudal es del orden de 112
L/s ( **Figura 8-1** ). Y con un caudal máximo (580L/s), se observa una mayor segregación espacial
y una mayor dispersión sobre el lecho del río ( **Figura 8-2** ), de las partículas que simular como
trazador conservativo las partículas de aceite y grasa.

43

**Figura 8-1. Aproximación Lagrangiana para simular la distribución espacial de aceite y grasas con un caudal más desfavorable para el**

**periodo considerado para las descargas (112 L/s)**

44

**Figura 8-2 Aproximación Lagrangiana para simular la distribución espacial de aceite y grasas con un caudal máximo (580L/s)**

45

**9.** **CONCLUSIÓN**

A partir de los resultados obtenidos con el modelo Visual Plumes para la evaluación en campo

cercano, es posible establecer que a partir de las descarga propuesta, y en virtud a que las

simulaciones no mostraron excesos térmicos significativos que sobrepasen el diferencial térmico

auto-impuesto según norma de la Comunidad Económica Europea ( ∆T< 3 _°_ C, en 500 m de distancia

radial), se estimó un área de influencia (AI) en base a una diferencia térmica más estricta, ya que se
consideró un ∆T= 0,5 ° C . Estimando un “AI” para invierno y primavera 0,00023km [2 ] en base a las

distancias radiales equivalentes a 0,023ha. Cabe destacar, que el área de influencia estimada es

reducida y se acota al área en torno al proyecto.

Los resultados de campo lejano, mostraron que las variaciones de temperatura debido a la descarga

de del ril durante la operación del proyecto, no generaría diferencias de temperaturas excesivas que

pudieran tener un impacto significativo, y dado que además las descargas se realizaran solo en los

periodos de mayor caudal (entre mayo a octubre) ya que en los escenarios simulados las diferencias

térmicas estarían por debajo de los 1,5°C en un radio de 500 m, no observándose grandes variaciones

en términos de los diferenciales térmicos entre invierno y primavera.

Se debe destacar que los efectos térmicos son temporales debido a la corriente del río y al bajo

tiempo de residencia, lo que implica que en un tiempo muy reducido se recambia toda el agua del

área de influencia, lo cual es un elemento muy favorable en términos dinámicos debido a que

favorecen la dispersión y advección de las aguas y a la disminución del efecto térmico, y

concentración de los distintos elementos del ril. Lo cual es válido para los caudales simulados de

mayo (112L/s), de junio a septiembre (580L/s), ya que las simulaciones consideran un criterio

precautorio, al incluir la peor condición y optima condición de caudal sobre la cual se descargara el

ril.

En conclusión y conforme a estos resultados de campo cercano y lejano, la descarga térmica del ril

sobre el cuerpo receptor Estero Huilma, durante la operación del proyecto, no generaría variaciones

térmicas significativas, lo cual no superaría la norma de referencia consultada (Normativa de la

Comunidad Económica Europea (EU-FFH), que define una zona de mezcla ( ∆T< 3 _°_ C ), la cual no

[puede superar un radio de 500 m de área de influencia (http://eur-lex.europa.eu/legal-](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32009L0031))

[content/EN/TXT/?uri=celex:32009L0031). Similar situación ocurriría con la calidad del agua en](http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32009L0031))

términos al contenido de oxígeno dado que las concentraciones de DBO5 se mantendrías cercanas a

las concentraciones naturales.

En el caso de los nutrientes, en virtud a que no existe una norma específica, se adopta el criterio de

calidad de agua de las normas secundarias que establecen que la concentración para nitrato debe

ser menor a 50mg/l, y a partir de las simulaciones se está varios órdenes de magnitud bajo esa

concentración. Similar situación ocurre con el fosfato, donde las bajas concentraciones en las

distintas simulaciones permiten definir un impacto no significativo.

46

Para los aceites y grasa dado que el supuesto del modelo lagrangiano asume que es un elemento con

boyantes positiva, se presentó como resultado la dispersión y distribución en el dominio del modelo

asociado a la diferencia de caudal del río para el mes de mayo asumiendo un caudal de 112 L/s como

condición precautoria más desfavorable mostrando una dispersión y distribución más agregada que

con un caudal mayor (580 L/s) donde la dispersión es mayor y los aceites y grasas se ven más

disgregados en el dominio con una distribución mucho más discreta. Por lo tanto, el mayor caudal

favorece la dispersión y disgregación de las partículas en el dominio; sin embrago las bajas

concentraciones en las distintas simulaciones permiten definir un impacto no significativo.

**10.** **REFERENCIAS BIBLIOGRÁFICAS**

 - DHI (2016). MIKE 3D Model FM, User Guide, Danish Hydraulics Software.

 - Dingman, J.S., and BedfordK.W.1986.Skill test sand parametric statistics for model
evaluation,J. Hydraulic Engineering 112:124-141.

 - Frick., W.E. 2004. Visual Plumes mixing zone modeling software. Environmental Modelling &
Software 19 (2004) 645-654.

 - Gourgue, Olivier ; Deleersnijder, Eric ; White, Laurent. Toward a generic method for studying
water renewal,with application to the epilimnion of Lake Tanganyika. In: Estuarine, Coastal
and Shelf Science, Vol. 74, no.4, p. 628-640 (2007) http://hdl.handle.net/2078.1/37339 -- DOI
: 10.1016/j.ecss.2007.05.009

 - Taylor, K.E. 2001. Summarizing multiple aspects of model performance in a single diagram.
J. Geophys. Res., 106, 7183-7192, (http://wwwpcmdi.llnl.gov/publications/ab55.html)

47

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1.: Coordenadas UTM (Datum WGS 84, zona 18G)****

| Sectores Coordenada Este (m) Coordenada Norte (m) | Col2 | Col3 |
| --- | --- | --- |
| **Planta Producción** | 647802 | 5491097 |
| **Planta Riles** | 647811 | 5491185 |
| **Descarga Planta de Riles** | 647506 | 5490949 |

**Tabla 2-3.: Parámetros de calidad de la descarga del ril considerados para las distintas**

| PARAMETRO Unidades Con dilución | Col2 | Col3 |
| --- | --- | --- |
| **DBO5** | mg O2/l | 300 |
| **Oxígeno Disuelto** | mg/l | 7,5 |
| **NITRATOS** | mg/l | <75 |
| **FOSFATOS** | mg/l | <15 |
| **pH** | - | 6,0-8,5 |
| **ACEITES Y GRASAS** | mg/l | 50 |

**Tabla 3-1.: Resumen de calidad del agua de los puntos de monitoreo, para cada parámetro****

| PARÁMETROS COLUMNA DE AGUA | INVIERNO 2019 | Col3 | Col4 | Col5 | Col6 | PRIMAVERA 2019 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ESTACIONES DE MONITOREO | E1 | E2 | E3 | E4 | E5 | E1 | E2 | E3 | E4 | E5 |
| pH | 7.57 | 7.51 | 7.48 | 7.48 | 7.45 | 7.41 | 7.43 | 7.39 | 7.42 | 7.42 |
| Temperatura (°C) | 8.27 | 8.27 | 8.29 | 8.29 | 8.31 | 11.13 | 11.18 | 11.16 | 11.20 | 11.20 |
| Conductividad (μS/cm) | 65 | 66 | 66 | 65 | 66 | 85 | 91 | 86 | 78 | 80 |
| Flujo Corriente (m/s) | 0.3 | 0.5 | 0.4 | 0.6 | 0.4 | 0.3 | 0.5 | 0.5 | 0.6 | 0.3 |
| Oxigeno Disuelto (mg/L) | 9.35 | 9.38 | 9.36 | 9.39 | 9.36 | 8.44 | 8.36 | 8.41 | 8.39 | 8.35 |
| Potencial Oxido Reducción<br>(mV/Ag/AgCl) | 233.9 | 228.5 | 216.7 | 245.5 | 231.1 | 189.5 | 203.4 | 197.6 | 201.1 | 179.8 |
| Solidos Disueltos Totales (ppm) | 32 | 36 | 18 | 35 | 41 | 67 | 74 | 49 | 55 | 73 |

**Tabla 3-2.: Estadística básica de los parámetros de calidad de agua para cada parámetro in****

| PARÁMETROS COLUMNA DE AGUA | AGOSTO, 2019 | Col3 | Col4 | DICIEMBRE. 2019 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
|  | PROMEDIO | MAXIMO | MINIMO | PROMEDIO | MAXIMO | MINIMO |
| pH | 7.50 | 7.57 | 7.45 | 7.41 | 7.43 | 7.39 |
| Temperatura (°C) | 8.29 | 8.31 | 8.27 | 11.17 | 11.20 | 11.13 |
| Conductividad (μS/cm) | 65.60 | 66.00 | 65.00 | 84.00 | 91.00 | 78.00 |
| Flujo Corriente (m/s) | 0.44 | 0.60 | 0.30 | 0.44 | 0.60 | 0.30 |
| Oxigeno Disuelto (mg/L) | 9.37 | 9.39 | 9.35 | 8.39 | 8.44 | 8.35 |
| Potencial Oxido Reducción<br>(mV/Ag/AgCl) | 231.14 | 245.50 | 216.70 | 194.28 | 203.40 | 179.80 |
| Solidos Disueltos Totales (ppm) | 32.40 | 41.00 | 18.00 | 63.60 | 74.00 | 49.00 |

**Tabla 5-1.**

| MUESTREO PUNTUAL EN ESTERO<br>HUILMA. LABORATORIO DICTUC<br>PARÁMETROS COLUMNA DE AGUA | 17-03-2020<br>CONCENTRACIÓN UNIDADES | Col3 |
| --- | --- | --- |
| Aceites y Grasas | <2 | (mg/L) |
| DBO5<br>Fósforo | 7<br>0.06 | (mg O2/L)<br>(mg/L) |
| Nitrógeno total Kjeldahl | 0.51 | (mg/L) |
| Sólidos Suspendidos | <10 | (mg/L) |
