---
title: Sin título
author: fernando fernandez
date: D:20230516184444-04'00'
language: es
type: report
pages: 191
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MINERA ALTOS DE PUNITAQUI
-->

## INFORME TÉCNICO DE ESTUDIO DE ESTABILIDAD FÍSICA BOTADERO DALMACIA MAYO 2023 MINERA BMR SPA - MINA DALMACIA

**INFORME FFGEO-BMR-007-2023**

**FF GEOMECHANICS ING. LTDA.**

**PREPARADO POR:** **PARA:**

**VALPARAÍSO, CHILE, 16/05/2023**

## INFORME TÉCNICO DE ESTUDIO DE ESTABILIDAD FÍSICA BOTADERO DALMACIA MAYO 2023 MINERA BMR SPA - MINA DALMACIA

|PREPARADO<br>POR|Fernando Fernández|Col3|Ingeniero Geomecánico Principal<br>FF GEOMECHANICS|Orig. Firmado|Rev. 0|
|---|---|---|---|---|---|
|**PREPARADO**<br>**POR**|Guillermo Sotomayor||Ingeniero Geomecánico<br>FF GEOMECHANICS|**Orig. Firmado**|Rev. 0|
|**REVISADO**<br>**POR**|Fernando Fernández||Ingeniero Geomecánico Principal<br>FF GEOMECHANICS|**Orig. Firmado**|Rev. 0|
|**REVISADO**<br>**POR**|René Rojas||Jefe de Geomecánica<br>Minera BMR SPA|**Orig. Firmado**|Rev. 0|
|**APROBADO**<br>**POR**|Fernando Fernández||Ingeniero Geomecánico Principal<br>FF GEOMECHANICS|**Orig. Firmado**|Rev. 0|
|**APROBADO**<br>**POR**|Antonio Pereira||Ingeniero Planificación Senior<br>Minera BMR SPA|**Orig. Firmado**|Rev. 0|
|**APROBADO**<br>**POR**|Néstor Concha||Gerente General<br>Minera BMR SPA|**Orig. Firmado**|Rev. 0|

**INFORME FFGEO-BMR-007-2023**

**FF GEOMECHANICS ING. LTDA.**

**VALPARAÍSO, CHILE, 16/05/2023**

**ÍNDICE DE CONTENIDOS**

1. INTRODUCCIÓN ........................................................................................... 2

2. OBJETIVOS Y ALCANCES ........................................................................... 2

3. ANTECEDENTES Y FUENTES DE INFORMACIÓN .................................... 3

4. UBICACIÓN DEL PROYECTO ...................................................................... 4

5. AMBIENTE DE EMPLAZAMIENTO DEL BOTADERO .................................. 6

5.1. Hidrología ..................................................................................................... 7

5.2. Hidrología Local ............................................................................................ 7

5.3. Hidrogeología ............................................................................................... 8

6. PARAMETRIZACIÓN Y COEFICIENTES SÍSMICOS ................................. 12

6.1. Caracterización de Suelos .......................................................................... 12

6.2. Propiedades Constitutivas del Enrocado .................................................... 16

6.3. Coeficientes Sísmicos................................................................................. 18

7. CRITERIOS DE ACEPTABILIDAD .............................................................. 19

7.1. Definición de Variabilidad de Parámetros ................................................... 22

8. ANÁLISIS DE ESTABILIDAD DE BOTADERO ........................................... 24

8.1. Resultados de Análisis de Estabilidad ........................................................ 30

9. MODELAMIENTO NUMÉRICO ................................................................... 32

10. CONCLUSIONES ........................................................................................ 37

11. REFERENCIAS BIBLIOGRÁFICAS ............................................................ 39

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **1** de **41**

**1.** **INTRODUCCIÓN**

El presente informe se enmarca dentro de los trabajos de ingeniera desarrollados
por parte de la consultora FF GeoMechanics a Minera BMR SPA, que corresponde
a los análisis de estabilidad física del Botadero Dalmacia, para dar respuesta a las
observaciones realizadas en el documento ICSARA, asociado al Proyecto Minero
Dalmacia 60.000 tons/m.

Para tales efectos, se considera el Informe de estabilidad física de Botadero
Dalmacia elaborado por BMR, la caracterización geotécnica de materiales
constituyentes del depósito, mecánica de suelos y rocas del sector, así como la
condición sísmica presente en el distrito.

**2.** **OBJETIVOS Y ALCANCES**

_Los objetivos del presente estudio son los siguientes:_

Entregar un análisis y evaluación de estabilidad física del diseño de Botadero
Dalmacia.

_Los alcances del presente estudio son los siguientes:_

El análisis de estabilidad se realiza en base a métodos de equilibrio límite
utilizando el software Slide ( _www.rocscience.com_ ).

Se considera la condición hipotética de generación de grietas de tracción en
la parte superior más elevada (o “cresta”) del Botadero Dalmacia, al ser
afectado por un potencial problema de estabilidad.

Se realizan análisis estáticos y pseudo-estático (sísmicos). Estos últimos
caracterizados por coeficientes sísmicos horizontales de 0.21 y 0.17, para los
casos de sismo máximo probable y sismo de operación, respectivamente.

- Para el análisis de estabilidad del Botadero Dalmacia se utiliza el método
GLE (“General Limit Equilibrium”), el cual permite obtener resultados más
completos, debido a que consideran el equilibrio de fuerzas y momentos
actuantes.

La estabilidad del Botadero se evalúa en base al factor de seguridad y
probabilidad de falla. Para tales efectos se utilizan las rutinas del software
Slide2 v.9.019, para definición de variabilidad de parámetros de entrada, y
simulación de probabilidad mediante técnica del “Hipercubo Latino”, con
5000 iteraciones (considerando la convergencia de los modelos analizados),
50 Slices y 50 iteraciones máximas.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **2** de **41**

La variabilidad de los parámetros de entrada se define según los criterios de
**Duncan (2000)**, de tal forma que los Coeficientes de Variación (COV) para
la Fricción y Cohesión, corresponden a 15%, y 25%, respectivamente.

Respecto a las propiedades geotécnicas utilizadas en los materiales que
constituyen el botadero, es posible indicar que para todos los efectos de
análisis se utiliza una condición conservadora, con cohesión nula (cero), y
con propiedades de ángulo de fricción interna bajo la curva promedio, del
criterio tipo Leps ( **Indraratna, 1993)**, en función de los resultados de ensayos
triaxiales de los materiales del botadero.

Los criterios de aceptabilidad para la evaluación de estabilidad, se definen
en función de la literatura más reciente referente a instalaciones mineras
remanentes, extraídas del libro “Guidelines for Mine Waste Dump and
Stockpile Design”, de los autores **M.** **Hawley** y **J. Cunning (2017)**, para
Factores de Seguridad (FS), Probabilidad de Falla (PF), y deformaciones.

- Las deformaciones en el botadero se analizan a través de modelamiento
numérico de elementos finitos con el software RS2 ( _www.rocscience.com_ ).

**3.** **ANTECEDENTES Y FUENTES DE INFORMACIÓN**

Los principales antecedentes utilizados en el desarrollo de este estudio
corresponden a los siguientes:

Informe P-IDR- 168-85-12-2-0, Estudio de Estabilidad de Botadero, Proyecto
Dalmacia y Anexos, elaborado por Ingeroc, el año 2014.

Informe de Mecánica de Suelos Botadero de Proyecto Dalmacia, elaborado
por Rodriguez y Goldsack, el año 2014, incluido en el Anexo del Informe PIDR- 168-85-12-2-0 de Ingeroc.

Estudio de Riesgo Sísmico, elaborado por S y S Ingenieros Consultores
Ltda., febrero 2019.

Ensayos triaxiales de mecánica de suelos para el material del Botadero,
elaborados por Fugro durante marzo y abril de 2023.

Ensayos de Laboratorio de Mecánica de suelos para los materiales de
fundación del Botadero, elaborados por IDIEM el año 2014.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **3** de **41**

**4.** **UBICACIÓN DEL PROYECTO**

Mina Dalmacia se emplaza en la comuna de Punitaqui a 8 km hacía el sur-oeste de
dicha localidad, en la cuarta Región de Coquimbo, ubicada en la Formación
Arqueros y estratos El Reloj, con una secuencia de rocas volcánicas y
sedimentarias, tal como se observa en la **Figura 4.1.**

El Botadero Dalmacia se encuentra ubicado en Quebrada El Peral, afluente del
Estero Punitaqui a aproximadamente 300 m.s.n.m., y a 900 metros en línea recta al
Suroeste del portal de acceso a la mina.

**Figura 4.1.** Ubicación de la zona de estudio a nivel regional.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **4** de **41**

Asimismo, una vista en planta del Botadero de Mina Dalmacia se muestra en la
**Figura 4.2** .

**Figura 4.2.** Vista en planta con coordenadas de emplazamiento del Botadero Mina

Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **5** de **41**

**5.** **AMBIENTE DE EMPLAZAMIENTO DEL BOTADERO**

El Botadero de Mina Dalmacia estará conformado por terrazas en donde la primera
está en contacto con el terreno natural y tiene 4.3 metros de altura, las demás tienen
alturas uniformes de 8 m, mientras que las nuevas terrazas a construir tendrán una
altura aproximada de 9.6 m con taludes con ángulos comprendidos entre 36° y 38°.
El diseño geométrico generado para la readecuación y crecimiento de los depósitos
de material fue proyectado a partir de la información topográfica actualizada, tal
como se muestra en la **Figura 5.1** .





**Figura 5.1.** Geometría Botadero Mina Dalmacia.

La zona donde se emplaza el depósito corresponde a sectores de quebradas,
ubicadas al suroeste del acceso de Mina Dalmacia.

Para la ejecución del proyecto se requiere la construcción de dos (2) bancos
adicionales en el Botadero existente, los cuales tendrán una capacidad asociada de
195,441 m [3] de material estéril.

Para la realización del diseño del banco proyectado se ha considerado la siguiente
información:

Reglamentación vigente para este tipo de depósito.

Características del material a depositar.

Características del suelo de emplazamiento.

Superficie basal y rasgos morfológicos del sitio de emplazamiento.

Ubicación de instalaciones, caminos e infraestructura.

- En la **Tabla 5.1** se resumen los parámetros de diseño.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **6** de **41**

**Tabla 5.1.** Parámetros de diseño del Botadero Mina Dalmacia.

|Tipo de Banco|Simple|
|---|---|
|Ángulo de Cara Banco ()|36o a 38°|
|Altura de Banco|9.6 m|
|Ángulo Final Talud Global|23o|
|Ancho de Berma Botadero|12 m|
|Ancho de Rampa Botadero|5 m|
|Gradiente Máxima Rampa Botadero|10%|
|Ancho Pretil Rampa Botadero|2 m|
|Altura Pretil Rampa Botadero|0.75 m|
|Ancho de Berma Caminos Botadero|14 m|
|Ancho de Caminos Botadero|10 m|
|Gradiente Máximo de Camino Botadero|10%|
|Ancho Pretil Camino Botadero|2 m|
|Altura Pretil Camino Botadero|0.75|

**5.1.** **Hidrología**

Entre los 27°y 33°S se presentan cuencas hidrográficas exorreicas, en donde la red
hídrica está marcada por angostos valles transversales, los más importantes de
ellos, de alcance cordillerano, con ríos en torrente de régimen mixto, aunque
fundamentalmente nival, y caudales crecientes, de 2 hasta 30 m [3] /s. En esta zona
se ha construido numerosos embalses para regularizar y aprovechar los
escurrimientos superficiales (DGA, 1986).

**5.2.** **Hidrología Local**

La zona de estudio se encuentra dentro de la cuenca hidrográfica del río Limarí, y
para la caracterización de régimen de precipitaciones, se consideraron los análisis
hechos por el Departamento de Administración de Recursos Hídricos. A partir de la
**Figura 5.2**, es posible estimar que la zona presenta una precipitación media anual
entre 150 - 200 mm. Por otro lado, el estudio hecho por **Godoy (2012)**, se diseña el
Botadero para una precipitación de 20,0 mm/h.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **7** de **41**

**Figura 5.2.** Mapa de isoyetas de la Región de Coquimbo.

**5.3.** **Hidrogeología**

En la región de Coquimbo se reconocen 6 sistemas de acuíferos principales: Los
Choros, Elqui, Culebrón-Lagunillas, Limarí, Choapa y Quilimarí. En particular, la
zona de estudio se ubica dentro de la zona del acuífero Limarí, como se observa en
la **Figura 5.3** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **8** de **41**

**Figura 5.3.** Mapa de acuíferos de la Región de Coquimbo.

En la cuenca hidrográfica del río Limarí se destacan tres escurrimientos
subterráneos, el primero en dirección sur-oeste que fluye paralelo al río Hurtado,
con profundidades freáticas de 2.0 - 3.6 m hasta las cercanías de Ovalle. En
dirección norte-oeste escurre un acuífero paralelo al río Grande, hasta la confluencia
con río Hurtado en Ovalle. Por último, en dirección norte-sur se encuentra el último
acuífero que fluye paralelo al río Combarbalá, hasta el Embalse La Paloma,
constituido de rocas sedimento-volcánicas con profundidades freáticas de 3.0 a 1.5
m, por tanto, la zona de estudio la podemos asociar a este acuífero.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **9** de **41**

Cabe mencionar que en la parte alta destaca la existencia de permeabilidad muy
baja, debido a la existencia de rocas plutónicas e hipabisales de muy baja
permeabilidad hidráulica. En la sección media se presentan rocas volcanosedimentarias de muy baja permeabilidad. Las características de impermeabilidad
de las rocas originan que el acuífero escurra paralelo a los cursos de agua.

**5.3.1. Hidrogeología Local**

Según la distribución administrativa que realiza la DGA, la zona de estudio estaría
contenida en la cuenca Limarí, en el acuífero Punitaqui siendo un afluente del Estero
Punitaqui, el cual tiene una extensión aproximada de 1.282 km [2] según **CPH y**
**Asociados S.A (2019).**

De los estudios hechos por **Godoy (2012)**, mediante cuatro (4) calicatas de 3 metros
de profundidad, no se detectó la napa freática, todos los antecedentes indican que
no existe napa hasta varias decenas de metros de profundidad, sin embargo, se
debe considerar el aporte de aguas lluvia de las cuencas mejores a la quebrada
principal y las aguas lluvia que escurrirán sobre el área de emplazamiento del
Botadero.

**5.3.2. Estimación de Las Constantes Elásticas (T y S)**

Los parámetros hidráulicos nos permiten estimar el potencial hidrogeológico de las
unidades acuíferas, dichos parámetros son la transmisividad (T) y el coeficiente de
almacenamiento (S). Donde T es la capacidad de un medio para trasmitir el agua, y
resulta del producto de la permeabilidad por el espesor saturado del acuífero.
Mientras que S es la capacidad del acuífero para almacenar o liberar el agua. De
los estudios realizados por **CPH y Asociados S.A (2019)**, se determinaron
transmisividades del orden de 7 a 60 m [2] /d, por otro lado, se estimó un coeficiente
de almacenamiento de entre 0.1 a 0.2.

Estas constantes se determinaron a partir de pozos hidráulicos ubicados entre
Ovalle - Punitaqui, cercanos a mina Cinabrio en materiales igualmente
pertenecientes a estratos de El Reloj.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **10** de **41**

**Figura 5.4.** Acuífero y pozos hidráulicos cercanos a mina Cinabrio.

Finalmente, desde el punto de vista hidrogeológico estas unidades, próximas a
mina, Dalmacia presentan nula importancia. La vulnerabilidad de la zona de estudio
se ha calculado como baja y con un tiempo de residencia aproximado en el subsuelo
sobre el acuífero mayor a 25 años, de acuerdo a **CPH y Asociados S.A (2019)** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **11** de **41**

**6.** **PARAMETRIZACIÓN Y COEFICIENTES SÍSMICOS**

Los antecedentes geotécnicos que permiten caracterizar los diversos materiales
presentes en el sitio del proyecto, se obtuvieron mediante la ejecución de ensayos
de laboratorio sobre una serie de muestras recolectadas el 2014 de las distintas
litologías de mina Dalmacia. Además, para la caracterización del suelo de
fundación, se consideraron las calicatas realizadas en el sector de emplazamiento
del Botadero, detalladas en el Informe de Mecánica de Suelos Botadero de Proyecto
Dalmacia, elaborado por **Rodríguez y Goldsack**, el año 2014.

Asimismo, las propiedades del material del Botadero fueron obtenidas a partir de
Informes de Ensayos de Laboratorio de Mecánica de Suelos, realizados entre marzo
y abril de 2023, por la empresa **Fugro** (Adjunto en el **Anexo A** ).

**6.1.** **Caracterización de Suelos**

A partir de las calicatas y cortes de caminos existentes en el sector de
emplazamiento del Botadero Dalmacia, se evidencia una cobertura superficial de
suelo fino residual, de color café, de consistencia y plasticidad medias, con un
contenido de humedad menor al límite plástico.

La estructura del suelo es heterogénea, de compresibilidad media a baja, y con
materia orgánica en los primeros 30 cm. Se presentan bloques aislados, de canto
angular, con tamaño máximo de 6”. El espesor medio de toda la capa de suelo
superficial, varía entre 0 y 1.5 m de profundidad.

Bajo la cubierta de suelo superficial, se presenta una unidad constituida por regolito
(o roca muy meteorizada), emplazada a una profundidad media variable entre 1.5
m y 3.5 m, aproximadamente.

La roca basal corresponde principalmente a Andesitas y Ocoítas, que subyace a las
unidades anteriores en las áreas con mayor presencia de materiales de arrastre, en
las zonas de quebradas y depresiones. En zonas elevadas es posible observar los
afloramientos de este tipo de rocas, las cuales presentan en general, buenas
calidades geotécnicas.

En las fotos de las **Figuras 6.1** a **6.3**, se observa de manera descriptiva, la
constitución de los suelos presentes en el sector de emplazamiento del Botadero
Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **12** de **41**

**Figura 6.1.** Corte de camino en el sector de emplazamiento del Botadero
Dalmacia, en el cual se observan las unidades características que conforman el

material de fundación de éste. Tomado de Informe de **Rodríguez y Goldsack**

**(2014)** .

**Figura 6.2.** Corte de camino en el sector de emplazamiento del Botadero
Dalmacia, en el cual se observan las unidades características que conforman el

material de fundación de éste. Tomado de Informe de **Rodríguez y Goldsack**

**(2014)** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **13** de **41**

**Figura 6.3.** Calicata en el sector de emplazamiento del Botadero Dalmacia, en el

cual se observan las unidades características que conforman el material de

fundación de éste. Tomado de Informe de **Rodríguez y Goldsack (2014)** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **14** de **41**

A partir de los Informes de **Rodríguez y Goldsack (2014)** y de **Ingeroc (2014)**, es
posible inferir los parámetros mostrados en la **Tabla 6.1**, para los materiales de
fundación presentes en el sector de emplazamiento del Botadero Dalmacia.

**Tabla 6.1.** Propiedades de los materiales de fundación, en el sector de

emplazamiento de Botadero Dalmacia.

|Descripción|Col2|Peso Unitario<br>Natural|Ángulo de<br>Fricción|Cohesión|
|---|---|---|---|---|
|**Descripción**|**Descripción**|**[ton/m3] **|**[o]**|**[kPa]**|
|Suelo residual|Corresponde al<br>estrato superficial a<br>nivel de terreno|1.90|30|20|
|Roca altamente<br>meteorizada y<br>fracturada (Regolito)|Corresponde al<br>segundo estrato en<br>profundidad|2.10|33|100|
|Roca volcánica<br>Andesítica / Ocoíta|Corresponde a la roca<br>basal, bajo las<br>unidades anteriores.|28.2|60|4,110|

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **15** de **41**

**6.2.** **Propiedades Constitutivas del Enrocado**

**T.M. Leps (1970)**, desarrolló una cantidad importante de ensayos triaxiales en
botaderos, que permitieron construir correlaciones empíricas entre el esfuerzo
normal actuante y el ángulo de fricción interna, para distintas calidades de material.

Posteriormente, en el transcurso de los años, se han realizado numerosas
publicaciones, cuyos autores han citado, modificado y/o actualizado los criterios
originales de **Leps (1970)** . Entre estos autores es posible citar: **Indraratna et al.**
**(1993)**, **M. Hawley et al (2016, 2017), N. Barton (2008), S. Linero et al (2007)** .

En la **Figura 6.4** se entrega la representación gráfica de Leps citada por **M. Hawley**
**y J. Cunning (2017)** .

**Figura 6.4.** Gráfico de relación entre ángulo de fricción interna máximo y esfuerzo

normal actuante en botaderos. Tomado de **M. Hawley y J. Cunning (2017)** .

En el caso del Botadero Dalmacia, los niveles de confinamiento o presiones al
interior de éstos, definirán los valores de resistencia al corte.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **16** de **41**

De esta forma, en la **Figura 6.5** se muestra un ejemplo correspondiente a la
representación de presiones de confinamiento del Botadero Dalmacia, según la
profundidad, obtenida a partir de modelamiento numérico, utilizando el software
Examine 2D ( _[www.rocscience.com](http://www.rocscience.com/)_ ).

_**Representación de Esfuerzo Principal Menor (**_  _**3**_ _**)**_

**Figura 6.5.** Representación de resultados de esfuerzos principales menores ( 3 ), o

presiones de confinamiento, en el perfil característico del Botadero Dalmacia.

Los resultados de los ensayos de laboratorio del material del Botadero Dalmacia,
definen una envolvente de ruptura que es mayor a la curva tipo Leps promedio,
según lo que se muestra en la **Figura 6.6.**

**Figura 6.6.** representación gráfica de las envolventes de falla de los parámetros

 respecto a  n, según **Leps (1970)** e **Indraratna (1993)** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **17** de **41**

Sin embargo, a efecto de realizar un análisis conservador, se contempla el uso de
los valores de confinamiento para la estimación de la resistencia al corte, a través
del uso de la curva Inferior ( **Indraratna et al., 1993** ) **,** mostrada en la **Figura 6.4** .

Los valores obtenidos según la curva de **Indraratna (1993)**, son ingresados
directamente en el programa de análisis (a través del método de equilibrio límite),
para la determinación de la estabilidad del Botadero Dalmacia, como se indica a
continuación:

Para efectos de caracterización de este material de relleno, se considera,
de manera conservadora, que presenta Cohesión = 0.

Asimismo, el material del enrocado queda definido por distintos ángulos de
fricción en función de su confinamiento, según la curva tipo Leps Inferior, de
**Indraratna (1993)**, utilizada.

En consecuencia, para el análisis de estabilidad se ingresa la curva
completa, en el software SLIDE (www.rocscience.com).

**6.3.** **Coeficientes Sísmicos**

Los coeficientes o cargas sísmicas a ser utilizados en el análisis de estabilidad del
Botadero, se han obtenido del “Estudio de Riesgo Sísmico” ( **S y S Ingenieros**
**Consultores Ltda., 2019** ), y se muestran en la **Tabla 6.2** .

**Tabla 6.2.** Coeficientes sísmicos utilizados para el análisis.

|Sismo|Aceleración máxima|Coeficiente sísmico|
|---|---|---|
|**_Operación_**|_0.50 g = 4.90 (m/s2) _|_0.17_|
|**_Máximo Probable_**|_0.95 g = 9.29 (m/s2) _|_0.21_|

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **18** de **41**

**7.** **CRITERIOS DE ACEPTABILIDAD**

Los criterios de aceptabilidad geotécnica de estabilidad de botaderos generalmente
se definen en función de valores mínimos de Factor de Seguridad (FS) y
Probabilidad de Falla (PF), para condiciones estáticas y sísmicas (o “pseudoestáticas”).

**Karzulovic (2006)**, en su “Curso de Master en Geomecánica”, Curso 03: Factor de
Seguridad vs Probabilidad de Falla, entrega una revisión de los criterios de
aceptabilidad de taludes. Se incluye una mención de algunos criterios de
aceptabilidad basados en FS para botaderos, los cuales se muestran en la **Tabla**
**7.1** .

**Tabla 7.1** . Factores de seguridad mínimos requeridos en Proyecto de

Escombreras (Botaderos). Fuente: **Ayala et al (1986)** .

**Karzulovic (2006)**, también menciona algunos criterios de aceptabilidad específicos
desarrollados en Botaderos de Minera Andina de Codelco, los cuales se resumen
en la **Tabla 7.2** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **19** de **41**

**Tabla 7.2** . Criterios de Aceptabilidad geotécnica para el diseño de Botaderos.

Fuente: **Karzulovic (2006)** .

|Referencia|Condición|Criterios de<br>Aceptabilidad|Comentarios|
|---|---|---|---|
|**Karzulovic (2006)**|Botaderos de Mina<br>Andina, algunos de<br>los cuales se<br>encuentran<br>ubicados sobre<br>morrenas<br>glaciares.|FS> 1.20 y PF< 10%|Condición Estática|
|**Karzulovic (2006)**|Botaderos de Mina<br>Andina, algunos de<br>los cuales se<br>encuentran<br>ubicados sobre<br>morrenas<br>glaciares.|FS> 1.10 y PF< 25%|Condición Sísmica<br>(Sismo Operacional)|
|**Karzulovic (2006)**|Botaderos de Mina<br>Andina, algunos de<br>los cuales se<br>encuentran<br>ubicados sobre<br>morrenas<br>glaciares.|FS> 1.00 y PF< 50%|Condición Sísmica<br>(Terremoto Máximo Probable)|

Algunos estudios más recientes, desarrollados por **M. Hawley y J. Cunning (2017)**,
citados en el libro: “Guidelines for Mine Waste Dump and Stockpile Design”,
entregan Matrices para la definición de Criterios de Aceptabilidad Geotécnica para
Botaderos de Lastre y Stocks de Mineral en función del nivel de confianza del diseño
y posible magnitud de consecuencias asociadas a las inestabilidades. Los criterios
son definidos para condición estática y pseudo-estática (o sísmica), de acuerdo con
las matrices de la **Figura 7.1** .

**STATIC ANALYSIS** **PSEUDO-STATIC ANALYSIS**

**LOW** **MODERATE** **HIGH**

**CONFIDENCE**

**LOW** **MODERATE** **HIGH**

**CONFIDENCE**

**Figura 7.1** . Matrices para la definición de Criterios de Aceptabilidad Geotécnica en
Botaderos y Stocks de Mineral en función del nivel de confianza del diseño y
consecuencias de inestabilidades. Fuente: **M. Hawley y J. Cunning (2017)** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **20** de **41**

Respecto a la definición de criterios de aceptabilidad de análisis de estabilidad
geotécnica a ser utilizado en el Botadero, es posible entregar los siguientes
comentarios:

_**Debido al uso de parámetros conservadores en la configuración**_ _y_
_análisis de estabilidad, se considera un Alto Nivel de Confianza del Diseño._

_Las consecuencias de posibles inestabilidades asociadas al Botadero, son_
_Bajas._

_**Sin embargo, y de manera conservadora**_ _, se exige el cumplimiento de_
_Criterios de Aceptabilidad asociados a Consecuencias y Confianza_
_Moderadas._

De acuerdo con la definición de las condiciones de diseño y posibles consecuencias
(anteriormente citadas), se entregan los Criterios de Aceptabilidad para el diseño
del Botadero, según los autores **M. Hawley y J. Cunning (2017)** . Ver detalles en
**Tabla 7.3** .

**Tabla 7.3** . Criterios de Aceptabilidad geotécnica para el diseño del Botadero.

Fuente: **M. Hawley y J. Cunning (2017)**

|Referencia|Condición|Criterios de<br>Aceptabilidad|Comentarios|
|---|---|---|---|
|**M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**|Condición establecida<br>de acuerdo con<br>Consecuencias y<br>Confianza Moderadas<br>en los diseños.|FS> 1.30 y PF< 15%|Condición Estática|
|**M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**|Condición establecida<br>de acuerdo con<br>Consecuencias y<br>Confianza Moderadas<br>en los diseños.|FS> 1.10|Condición Sísmica<br>(Sismo Operacional)|
|**M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**|Condición establecida<br>de acuerdo con<br>Consecuencias y<br>Confianza Moderadas<br>en los diseños.|FS> 1.05|Condición Sísmica<br>(Terremoto Máximo Probable)|

Los criterios de aceptabilidad de **M. Hawley y J. Cunning (2017)**, a diferencia de
los definidos por **Karzulovic (2006)**, no establecen valores máximos admisibles
para las probabilidades de falla en condiciones sísmicas (o pseudo-estáticas).

Para poder subsanar esta condición, se realiza una combinación de ambos criterios
de Aceptabilidad Geotécnica, los que deberán ser cumplidos como requerimientos
mínimos de diseño, en función de los análisis de estabilidad, ver **Tabla 7.4** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **21** de **41**

**Tabla 7.4** . Criterios de Aceptabilidad geotécnica definidos para el diseño del

Botadero.

|Referencia|Condición|Criterios de<br>Aceptabilidad|Comentarios|
|---|---|---|---|
|**M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**<br> <br>**Karzulovic (2006)**|Condición establecida<br>de<br>acuerdo<br>con<br>Consecuencias<br>y <br>Confianza Moderadas<br>en los diseños.|FS> 1.30 y PF< 10%|Condición Estática|
|**M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**<br> <br>**Karzulovic (2006)**|Condición establecida<br>de<br>acuerdo<br>con<br>Consecuencias<br>y <br>Confianza Moderadas<br>en los diseños.|FS> 1.10 y PF< 25%|Condición Sísmica<br>(Sismo Operacional)|
|**M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**<br> <br>**Karzulovic (2006)**|Condición establecida<br>de<br>acuerdo<br>con<br>Consecuencias<br>y <br>Confianza Moderadas<br>en los diseños.|FS> 1.05 y PF< 45%|Condición Sísmica<br>(Terremoto Máximo Probable)|

Es importante indicar que los criterios establecidos de Factores de Seguridad y
Probabilidades de Falla, de la **Tabla 7.4**, corresponden a los estándares mínimos
de cumplimiento en términos de estabilidad crítica a condición de talud global, que
pudiesen afectar la seguridad y/o continuidad de las operaciones.

**7.1.** **Definición de Variabilidad de Parámetros**

Con propósitos de definición de variabilidad de los parámetros geotécnicos
utilizados en los análisis de estabilidad, se realiza una revisión de los criterios
publicados en la literatura especializada. Los resultados de la revisión indican que
los criterios más completos corresponden a los entregados por **J. M. Duncan (1999-**
**2000)**, que se resumen en la **Tabla 7.5** .

**Tabla 7.5** . Valores de coeficientes de variación de propiedades geotécnicas y

ensayos “In-Situ”. Fuente: **J. M. Duncan (2000)** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **22** de **41**

De acuerdo con los valores de **Duncan (2000)**, mostrados en la **Tabla 7.5**, es
posible entregar los siguientes comentarios relativos a la variabilidad de los
parámetros de entrada: Ángulo de Fricción, Cohesión y Densidad, que determinan
la probabilidad de falla asociada al análisis de estabilidad.

- _Para_ _**Ángulo de Fricción (**_  _**):**_ _**Duncan**_ _define un Coeficiente de Variación_
_que fluctúa entre 2% y 13%. Para efectos de los análisis de estabilidad,_ _**se**_
_**considera una Variabilidad Alta de 15%.**_

- _Para_ _**Cohesión (c):**_ _**Duncan**_ _NO define la variabilidad de este parámetro._
_Para efectos de los análisis de estabilidad del_ _**Botadero**_ _, y en función de los_
_estándares definidos en el_ _**Taller Inter-divisional de Codelco (1997):**_
_**“Estándares para la Caracterización Geotécnica de Rocas, Estructuras**_
_**y Macizos Rocosos”, se define una Alta Variabilidad para la Cohesión,**_
_**correspondiente a 25%.**_

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **23** de **41**

**8.** **ANÁLISIS DE ESTABILIDAD DE BOTADERO**

Para el desarrollo del análisis de estabilidad se contemplaron una serie de
supuestos y consideraciones de diseño, los cuales se citan a continuación:

Para el análisis a nivel global de Botadero Dalmacia, se considera el perfil
más crítico, que se muestra en la vista en planta de la **Figura 8.1**, y
corresponde a la Sección A’-A, de la **Figura 8.2** .

**Figura 8.1.** Vista en planta con la ubicación de la Sección A-A’, considerada para

el análisis del Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **24** de **41**

**Figura 8.2.** Talud Global analizado, de Botadero Dalmacia.

De forma complementaria, se realizan análisis locales de estabilidad,
asociados a cada uno de los taludes individuales que conforman la Sección
A-A’ crítica del botadero, y que se identifican de acuerdo a la **Figura 8.3** .

**Figura 8.3.** Taludes individuales analizados, de Botadero Dalmacia.

Se consideran las propiedades geotécnicas del suelo de fundación y cuerpo
del Botadero, definidas en el **Capítulo 6** del presente informe.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **25** de **41**

Se considera la condición hipotética de generación de grietas de tracción,
ubicadas en la parte superior (de mayor altura), o “cresta” del botadero, con
una saturación de agua correspondiente a un 33% de la profundidad de las
grietas, y que se asocia a las condiciones geográficas y niveles de lluvias
máximos esperados, del sector de emplazamiento.

Se realizan análisis estáticos y pseudo-estático (sísmicos). Estos últimos
caracterizados por coeficientes sísmicos horizontales de 0.21 y 0.17, para los
casos de sismo máximo probable y sismo de operación, respectivamente.

- Para el análisis de estabilidad del Botadero se utiliza el método **GLE**
(“General Limit Equilibrium”), según los autores Morgenstern-Price, el cual
permite obtener resultados más completos, debido a que consideran el
equilibrio de fuerzas y momentos actuantes.

La estabilidad del Botadero se evalúa en base al factor de seguridad y
probabilidad de falla. Para tales efectos se utilizan las rutinas del software
Slide2 v.9.019, para definición de variabilidad de parámetros de entrada, y
simulación de probabilidad mediante técnica del “Hipercubo Latino”, con 5000
iteraciones (considerando la convergencia de los modelos analizados), 50
Slices y 50 iteraciones máximas.

La variabilidad de los parámetros de entrada se define según los criterios de
**Duncan (2000)**, de tal forma que los Coeficientes de Variación (COV) para la
Fricción y Cohesión, corresponden a 15% y 25%, respectivamente.

Respecto a las propiedades geotécnicas utilizadas, que constituyen los
botaderos, es posible indicar que para todos los efectos de análisis se utiliza
una condición conservadora, con cohesión nula (cero), y con propiedades de
ángulo de fricción interna bajo la curva promedio, del criterio tipo Leps
( **Indraratna, 1993)**, en función de los resultados de ensayos triaxiales de los
materiales del Botadero, tal como se muestra en la **Figura 8.4** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **26** de **41**

**Figura 8.4.** representación gráfica de las envolventes de falla de los parámetros

 respecto a  n, según **Leps (1970)** e **Indraratna (1993)** .

Los criterios de aceptabilidad para la evaluación de estabilidad, se definen
en función de la literatura más reciente referente a instalaciones mineras
remanentes, extraídas del libro “Guidelines for Mine Waste Dump and
Stockpile Design”, de los autores **M.** **Hawley** y **J. Cunning (2017)**, para
Factores de Seguridad (FS), Probabilidad de Falla (PF), y deformaciones.

- Las deformaciones en el botadero se analizan a través de modelamiento
numérico de elementos finitos con el software RS2 ( _www.rocscience.com_ ).

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **27** de **41**

Respecto a la metodología de análisis, es importante mencionar que el método de
las “tajadas” o “dovelas” que utiliza el software Slide no considera esfuerzos o
fuerzas laterales (“entrantes” en el plano).

En consecuencia, es posible inferir que los análisis de estabilidad, desarrollados a
través de equilibrio límite utilizando el método de las “dovelas”, son conservadores,
ya que no consideran los efectos de confinamiento en el material constituyente del
mismo.

A continuación, se entrega una breve descripción de la metodología, y uso de
ecuaciones asociadas al método de las “dovelas” o “tajadas” utilizado en el software
Slide:

a) Se divide la zona de análisis en “tajadas” o “dovelas” verticales, de tal forma
que se evalúa el Factor de Seguridad, comparando la razón entre las
fuerzas resistentes y las fuerzas de movimiento, asociadas a cada dovela
( **Figura 8.5** ).

b) Las fuerzas actuantes en una dovela típica corresponden al Peso de la
dovela (W), las fuerzas Normal (N) y Tangencial (T) que actúan en el borde
inferior de cada dovela, así como las fuerzas laterales X y E actuantes en el
plano. Ver **Figura 8.5** .

c) El análisis de dovelas es bi-dimensional, de tal forma que no se consideran
fuerzas laterales, que “entren” en el plano.

**Figura 8.5** . Esquema de fuerzas actuantes en método ordinario de dovelas.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **28** de **41**

d) Una forma análoga de descripción del análisis de dovelas, se expresa en
relación a los esfuerzos resistentes y esfuerzos actuantes (o de
movimiento), de acuerdo con el esquema de la **Figura 8.6** .

**Figura 8.6** . Esquema típico de fuerzas actuantes y esfuerzos considerados en

Métodos de Dovelas, según **Hoek y Bray (2004)** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **29** de **41**

**8.1.** **Resultados de Análisis de Estabilidad**

Los resultados correspondientes al análisis de Estabilidad Física del Botadero Dalmacia, indicando valores de Factor de
Seguridad (FS) y Probabilidad de Falla (PF), para cada una de las metodologías y condiciones simuladas (estáticas y
pseudo-estáticas), se presentan en la **Tabla 8.1** .

**Tabla 8.1.** Resultados de análisis de estabilidad de Botadero Dalmacia.

<!-- INICIO TABLA 8.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _En el_ _**Anexo B**_ _se muestran los resultados de las simulaciones realizadas con el software Slide del Botadero Dalmacia._ Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **30** de **41** -->

**Tabla 8.1: (continuación).** Resultados de análisis de estabilidad de Botadero Dalmacia.**

| ANÁLISIS | SECCIÓN | CONDICIÓN DE ANÁLISIS | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **_ANÁLISIS_** | **_SECCIÓN_** | **_ESTÁTICO_**<br>**_(kh=0)_** | **_SISMO OPERACIONAL_**<br>**_(kh=0.17)_** | **_SISMO MAX. CREÍBLE_**<br>**_(kh=0.21)_** |
| **_ANÁLISIS_** | **_SECCIÓN_** | **_GLE_** | **_GLE_** | **_GLE_** |
| **_Local_** | Talud 4 (T-4) | _FS (det.) = 1.74_<br>_FS (mean) = 1.78_<br>_PF = 0.1%_ | _FS (det.) = 1.29_<br>_FS (mean) = 1.32_<br>_PF = 10.2%_ | _FS (det.) = 1.21_<br>_FS (mean) = 1.24_<br>_PF = 16.1%_ |
| **_Local_** | Talud 5 (T-5) | _FS (det.) = 1.72_<br>_FS (mean) = 1.76_<br>_PF = 0.2%_ | _FS (det.) = 1.27_<br>_FS (mean) = 1.30_<br>_PF = 11.4%_ | _FS (det.) = 1.19_<br>_FS (mean) = 1.22_<br>_PF = 18.3%_ |
| **_Local_** | Talud 6 (T-6) | _FS (det.) = 1.68_<br>_FS (mean) = 1.72_<br>_PF = 0.5%_ | _FS (det.) = 1.24_<br>_FS (mean) = 1.27_<br>_PF = 14.2%_ | _FS (det.) = 1.16_<br>_FS (mean) = 1.19_<br>_PF = 22.7%_ |
| **_Local_** | Talud 7 (T-7) | _FS (det.) = 1.78_<br>_FS (mean) = 1.83_<br>_PF = 0.1%_ | _FS (det.) = 1.32_<br>_FS (mean) = 1.35_<br>_PF = 7.5%_ | _FS (det.) = 1.24_<br>_FS (mean) = 1.27_<br>_PF = 14.1%_ |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- _En el_ _**Anexo B**_ _se muestran los resultados de las simulaciones realizadas con el software Slide del Botadero Dalmacia._ Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **31** de **41** -->
<!-- FIN TABLA 8.1 -->


|ANÁLISIS|SECCIÓN|CONDICIÓN DE ANÁLISIS|Col4|Col5|
|---|---|---|---|---|
|**_ANÁLISIS_**|**_SECCIÓN_**|**_ESTÁTICO_**<br>**_(kh=0)_**|**_SISMO OPERACIONAL_**<br>**_(kh=0.17)_**|**_SISMO MAX. CREÍBLE_**<br>**_(kh=0.21)_**|
|**_ANÁLISIS_**|**_SECCIÓN_**|**_GLE_**|**_GLE_**|**_GLE_**|
|**_Global_**|A-A'|_FS (det.) = 2.04_<br>_FS (mean) = 2.06_<br>_PF = 0.0%_|_FS (det.) = 1.34_<br>_FS (mean) = 1.36_<br>_PF = 0.6%_|_FS (det.) = 1.23_<br>_FS (mean) = 1.25_<br>_PF = 2.9%_|
|**_Local_**|Talud 1 (T-1)|_FS (det.) = 2.20_<br>_FS (mean) = 2.25_<br>_PF = 0.0%_|_FS (det.) = 1.60_<br>_FS (mean) = 1.64_<br>_PF = 1.2%_|_FS (det.) = 1.50_<br>_FS (mean) = 1.53_<br>_PF = 1.9%_|
|**_Local_**|Talud 2 (T-2)|_FS (det.) = 1.80_<br>_FS (mean) = 1.85_<br>_PF = 0.1%_|_FS (det.) = 1.34_<br>_FS (mean) = 1.38_<br>_PF = 6.2%_|_FS (det.) = 1.26_<br>_FS (mean) = 1.29_<br>_PF = 12.0%_|
|**_Local_**|Talud 3 (T-3)|_FS (det.) = 1.76_<br>_FS (mean) = 1.81_<br>_PF = 0.1%_|_FS (det.) = 1.30_<br>_FS (mean) = 1.34_<br>_PF = 9.1%_|_FS (det.) = 1.22_<br>_FS (mean) = 1.25_<br>_PF = 15.1%_|

_En el_ _**Anexo B**_ _se muestran los resultados de las simulaciones realizadas con el software Slide del Botadero Dalmacia._

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **30** de **41**

**Tabla 8.1 (continuación).** Resultados de análisis de estabilidad de Botadero Dalmacia.

|ANÁLISIS|SECCIÓN|CONDICIÓN DE ANÁLISIS|Col4|Col5|
|---|---|---|---|---|
|**_ANÁLISIS_**|**_SECCIÓN_**|**_ESTÁTICO_**<br>**_(kh=0)_**|**_SISMO OPERACIONAL_**<br>**_(kh=0.17)_**|**_SISMO MAX. CREÍBLE_**<br>**_(kh=0.21)_**|
|**_ANÁLISIS_**|**_SECCIÓN_**|**_GLE_**|**_GLE_**|**_GLE_**|
|**_Local_**|Talud 4 (T-4)|_FS (det.) = 1.74_<br>_FS (mean) = 1.78_<br>_PF = 0.1%_|_FS (det.) = 1.29_<br>_FS (mean) = 1.32_<br>_PF = 10.2%_|_FS (det.) = 1.21_<br>_FS (mean) = 1.24_<br>_PF = 16.1%_|
|**_Local_**|Talud 5 (T-5)|_FS (det.) = 1.72_<br>_FS (mean) = 1.76_<br>_PF = 0.2%_|_FS (det.) = 1.27_<br>_FS (mean) = 1.30_<br>_PF = 11.4%_|_FS (det.) = 1.19_<br>_FS (mean) = 1.22_<br>_PF = 18.3%_|
|**_Local_**|Talud 6 (T-6)|_FS (det.) = 1.68_<br>_FS (mean) = 1.72_<br>_PF = 0.5%_|_FS (det.) = 1.24_<br>_FS (mean) = 1.27_<br>_PF = 14.2%_|_FS (det.) = 1.16_<br>_FS (mean) = 1.19_<br>_PF = 22.7%_|
|**_Local_**|Talud 7 (T-7)|_FS (det.) = 1.78_<br>_FS (mean) = 1.83_<br>_PF = 0.1%_|_FS (det.) = 1.32_<br>_FS (mean) = 1.35_<br>_PF = 7.5%_|_FS (det.) = 1.24_<br>_FS (mean) = 1.27_<br>_PF = 14.1%_|

_En el_ _**Anexo B**_ _se muestran los resultados de las simulaciones realizadas con el software Slide del Botadero Dalmacia._

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **31** de **41**

**9.** **MODELAMIENTO NUMÉRICO**

Con el propósito de poder evaluar las posibles deformaciones generadas en el
sector de la sección crítica del Botadero de Mina Dalmacia, se realizan los
modelamientos numéricos a través del software RS2 (Phases 2D).

El esfuerzo vertical ( v ) actuante en el Botadero corresponde al incremento
producido por el peso propio del material. Para tales efectos, se utiliza la opción
“gravity” del comando “Field Stress Properties” del software RS2 (Phases 2D).

Las condiciones de borde corresponden a apoyos deslizantes (o “rollers”) en ambos
costados del modelo, con apoyos fijos en la parte inferior del mismo.

La malla de modelamiento es uniforme, conformada por triángulos de 6 nodos, tal
como se muestra en la **Figura 9.1** .

**Figura 9.1** . Condiciones de borde y enmallado utilizados en Modelo Numérico.

El criterio de aceptabilidad considerado en el Modelamiento Numérico se establece
en función de las máximas deformaciones esperadas, según la publicación:
_“Guidelines for Waste Dump and Sockpile Design”_, de **M. Hawley & J. Cunning**
**(2017)** .

De acuerdo con los citados autores, el criterio de aceptabilidad se establece de
manera matricial, en función de las máximas deformaciones esperadas, de acuerdo
con el esquema mostrado en la **Figura 9.2** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **32** de **41**

**Figura 9.2** . Matriz de criterio de aceptabilidad geotécnica basado en análisis de

deformación, de acuerdo con **M. Hawley & J. Cunning (2016, 2017)** .

De manera razonable, es posible estimar un nivel bajo a moderado de consecuencia
de inestabilidad, con un nivel moderado a alto de confianza en la estimación de los
parámetros de diseño del Botadero Dalmacia.

De esta forma, se establece que el valor de deformación máxima no puede ser
mayor a 1% para condición de Análisis Estático, y no puede sobrepasar una
deformación de 1.5%, para condición de Análisis Pseudo-estático (sísmico).

Con el propósito de mostrar las deformaciones generadas en el Botadero Dalmacia,
se realizan la interpretación del modelo numérico a través de la opción “Volumetric
Strain”, que corresponde a la siguiente expresión (www.rocscience.com):

Volumetric Strain= ε x + ε y + ε z

En condiciones de estado plano de deformaciones, el valor de  z es igual a 0, por lo

que:

Volumetric Strain= ε x + ε y

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **33** de **41**

Los análisis de modelamiento numérico, correspondientes a las deformaciones
generadas (“Volumetric Strain”), para condición estática, sismo de operación, y
sismo (terremoto) máximo probable (condición de abandono), se representan en las
**Figuras 9.3** a **9.5**, respectivamente.

**Figura 9.3** . Deformaciones generadas en el Botadero Dalmacia, para sección

crítica de análisis, condición Estática (Kh = 0.0).

**Figura 9.4** . Deformaciones generadas en el Botadero Dalmacia, para sección

crítica de análisis, condición de Sismo Operacional (Kh = 0.17).

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **34** de **41**

**Figura 9.5** . Deformaciones generadas en el Botadero Dalmacia, para sección
crítica de análisis, condición de Sismo Máximo Probable o Abandono (Kh = 0.21).

De acuerdo con los resultados de deformación máxima obtenidos a través de
modelamiento numérico ( **Figuras 9.3** a **9.5** ), es posible entregar los siguientes
comentarios:

Los valores de SRF (Strength Reduction Factor) para condición estática,
sismo operacional (Kh = 0.17), y sismo máximo probable (Kh = 0.21),
corresponden a 2.03, 1.31 y 1.21, respectivamente. Estos valores son
concordantes con los Factores de Seguridad (FS) obtenidos a través de
equilibrio límite con el software SLIDE.

Las deformaciones máximas para condición estática, sismo operacional (Kh
= 0.17), y sismo máximo probable (Kh = 0.21), corresponden a 0.5%, 0.8%
y 1.0%, respectivamente.

Los valores de deformaciones en el Botadero Dalmacia cumplen con los
criterios de aceptabilidad geotécnica de **Hawley y Cunning (2017)** .

El resumen de los resultados obtenidos y su aceptabilidad geotécnica, se resumen
en la **Tabla 9.1** .

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **35** de **41**

**Tabla 9.1** . Resultados de análisis de estabilidad de Botadero Dalmacia. Método de

Modelamiento Numérico utilizando software RS2 (Phases 2D).

|Condición de Análisis|Col2|Carga<br>Sísmica|Estabilidad|Col5|Deformación<br>Máxima|Criterio<br>Aceptabilidad|
|---|---|---|---|---|---|---|
|**Condición de Análisis**|**Condición de Análisis**|**Carga**<br>**Sísmica**|**FS**<br>**(análisis**<br>**SLIDE)**|**SRF**<br>**(Modelo**<br>**Numérico)**|**SRF**<br>**(Modelo**<br>**Numérico)**|**SRF**<br>**(Modelo**<br>**Numérico)**|
|**Botadero**<br>**Dalmacia**|**Estático**|0.0|2.04|2.03|0.5%|Cumple|
|**Botadero**<br>**Dalmacia**|**Sismo Op.**|0.17|1.34|1.31|0.8%|Cumple|
|**Botadero**<br>**Dalmacia**|**Sismo Máx.**|0.21|1.23|1.21|1.0%|Cumple|

Es importante indicar que en la **Tabla 9.1** se incluyen los valores de F.S. obtenidos
a partir de Análisis de Equilibrio Límite (Slide), ya que éstos sirven de referencia
para el Modelamiento Numérico.

En consecuencia, el análisis es válido, siempre y cuando exista coherencia y
convergencia entre los valores de F.S. y SRF, obtenidos a través de ambas
metodologías (equilibrio límite y modelamiento numérico).

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **36** de **41**

**10.** **CONCLUSIONES**

_**A partir de los resultados del análisis de estabilidad del botadero, mediante el**_
_**Análisis de Equilibrio Límite (Slide), es posible señalar lo siguiente:**_

- _**Condición Análisis Estático:**_ _todos los Factores de Seguridad (F.S.)_
_obtenidos, mediante la aplicación del método utilizado, para todas las_
_condiciones (global y local), son superiores a 1.3, cumpliendo con los_
_criterios de aceptabilidad definidos. La probabilidad de falla (P.F.)_
_corresponde al criterio de estabilidad determinado para este tipo de estudio_
_(≤ 10%), por lo tanto, cumplen en su condición estática._

- _**Condición Análisis Operacional (Pseudo-Estático):**_ _con una solicitación_
_equivalente a un coeficiente sísmico de Kh =0.17, las condiciones_
_evaluadas, evidencian Factores de Seguridad (F.S.) superiores a 1.1 y_
_Probabilidades de Falla (P.F.) ≤ 25%, cumpliendo con los criterios de_
_aceptabilidad definidos para este estudio. Por lo tanto, ante este tipo de_
_solicitación sísmica, todos los escenarios evaluados, son estables._

- _**Condición Análisis Abandono (Pseudo-Estático):**_ _con una solicitación_
_sísmica máxima probable, bajo una condición de abandono (Kh= 0.21), las_
_condiciones evaluadas, evidencian Factores de Seguridad (F.S.) superiores_
_a 1.05 y Probabilidades de Falla (P.F.) ≤ 45%, cumpliendo con los criterios_
_de aceptabilidad definidos para este estudio. Por lo tanto, ante este tipo de_
_solicitación sísmica, todos los escenarios evaluados, son estables._

_**A partir de los resultados del análisis de estabilidad del botadero, mediante**_
_**Modelamiento Numérico de sección crítica, es posible señalar lo siguiente:**_

_Los valores de SRF (Strength Reduction Factor) para condición estática,_
_sismo operacional (Kh = 0.17), y sismo máximo probable (Kh = 0.21),_
_corresponden a 2.03, 1.31 y 1.21, respectivamente. Estos valores son_
_concordantes con los Factores de Seguridad (FS) obtenidos a través de_
_equilibrio límite con el software SLIDE._

_Las deformaciones máximas para condición estática, sismo operacional (Kh_
_= 0.17), y sismo máximo probable (Kh = 0.21), corresponden a 0.5%, 0.8%_
_y 1.0%, respectivamente._

_Los valores de deformaciones en el Botadero Dalmacia cumplen con los_
_criterios de aceptabilidad geotécnica de_ _**Hawley y Cunning (2017)**_ _._

_El resumen de los resultados obtenidos y su aceptabilidad geotécnica, se_
_resumen en la siguiente_ _**Tabla**_ _._

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **37** de **41**

_**Tabla**_ _. Resultados de análisis de estabilidad de Botadero Dalmacia. Método de_

_Modelamiento Numérico utilizando software RS2 (Phases 2D)._

|Condición de Análisis|Col2|Carga<br>Sísmica|Estabilidad|Col5|Deformación<br>Máxima|Criterio<br>Aceptabilidad|
|---|---|---|---|---|---|---|
|**Condición de Análisis**|**Condición de Análisis**|**Carga**<br>**Sísmica**|**FS**<br>**(análisis**<br>**SLIDE)**|**SRF**<br>**(Modelo**<br>**Numérico)**|**SRF**<br>**(Modelo**<br>**Numérico)**|**SRF**<br>**(Modelo**<br>**Numérico)**|
|**Botadero**<br>**Dalmacia**|**Estático**|0.0|2.04|2.03|0.5%|Cumple|
|**Botadero**<br>**Dalmacia**|**Sismo Op.**|0.17|1.34|1.31|0.8%|Cumple|
|**Botadero**<br>**Dalmacia**|**Sismo Máx.**|0.21|1.23|1.21|1.0%|Cumple|

- _Es importante indicar que en la_ _**Tabla**_ _anterior_ _se incluyen los valores de F.S._
_obtenidos a partir de Análisis de Equilibrio Límite (Slide), ya que éstos sirven_
_de referencia para el Modelamiento Numérico._

_En consecuencia, el análisis es válido, siempre y cuando exista coherencia y_
_convergencia entre los valores de F.S. y SRF, obtenidos a través de ambas_
_metodologías (equilibrio límite y modelamiento numérico)._

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **38** de **41**

**11.** **REFERENCIAS BIBLIOGRÁFICAS**

_**Barrientos S.**_ _“Seismic regionalization of Chile. (1980)”. Magister Thesis,_
_Department of Geophysics, University of Chile, Santiago, Chile, 1980 (In Spanish)._

_**Barton, N.R. (2008).**_ _Shear strength of rockfill, interfaces and rock joints and their_
_points of contact in rock dump design; in A. Fourie, ed., Rock Dumps 2008:_
_Australian Centre for Geomechanics, Perth, p. 3-17._

_**Blight, G., Steffen, D. (1979).**_ _Geotechnics of gold mine waste disposal. Current_
_geotechnical practice in mine waste disposal. ASCE, 1-52._

_**Chung, A.I, Neighbors, C., Belmonte, A., Miller, M., Sepúlveda, H.H.,**_
_**Christensen, C., Jakka, R.S., Cochran, E. S, Lawrence, J.F. (2011).**_ _The Quake-_
_Catcher Network Rapid Aftershock Mobilization Program Following the 2010 M 8.8_
_Maule, Chile Earthquake. Seismological Research Letters 82 526, 532._

_**Duncan, J.M. (2000).**_ _Factors of safety and reliability in geotechnical engineering._
_Journal of Geotechnical Engineering and Environmental Engineering._

_**Henríquez, C. (2012).**_ _Estimación del efecto de sitio en zonas afectadas por el_
_terremoto (Mw = 8.8) del 27/02/10 a la luz de las leyes de atenuación existentes._
_Tesis para optar al título profesional de geofísico. Universidad de Concepción,_
_Departamento de Geofísica._

_**Hoek, E & Bray, J. (1981)**_ _: Rock slope Engineering, I.M.M., London._

_**Hoek, E, Carranza-Torres, C. and Corkum, B. (2002).**_ _Hoek- Brown Failure_
_Criterion-2002 Edition, 5th North American Rock Mechanics Symposium and 17th_
_Tunneling Association of Canada Conference: NARMS-TAC, 2002._

_**Hoek E, Karzulovic A. (2000).**_ _Rock mass properties for surface mines. In: Hustrulid_
_WA, McCarter MK, van Zyl DJA, eds. Slope stability in surface mining. Littleton, CO:_
_Society for Mining, Metallurgy, and Exploration, Inc., pp. 59-70._

_**Hynes-Griffin M.E., Franklin A.G. (1984).**_ _Rationalizing the Seismic Coefficient_
_Method, Miscellaneous Paper GL-84-13. Department of the Army, Waterways_
_Experiment Station, Vicksburg, MS._

_**Karzulovic, A., Aguirre, A., Araya, R. (1989).**_ _Definición del sismo operacional y_
_terremoto máximo probable para el análisis de estabilidad sísmica de depósitos de_
_relaves. Anales VI Simposium de Ingeniería de Minas, Universidad de Santiago de_
_Chile._

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **39** de **41**

_**Karzulovic, A. (2007).**_ _Programa de Magister en Geomecánica Aplicada a la_
_Minería, Universidad de Los Andes. Curso 03: Geomecánica en la minería a rajo_
_abierto._

_**Leps, T.M. (1970).**_ _Review of Shearing Strength of rockfill: Journal of Soil Mechanics_
_and Foundation Engineering Division, v. 96(SM4), p. 1159-1170._

_**Linero, S., Palma, C., and Apablaza, R. (2007).**_ _Geotechnical characterization of_
_waste material in very high dumps with large scale triaxial testing, Proceedings of_
_International Symposium on Rock Slope Stability in Open Pit Mining and Civil_
_Engineering, 12-14 September 2007, Perth, Australia, p. 59-75._

_**Marcuson WF, Franklin AG. (1983).**_ _“Seismic Design, Analysis, and Remedial_
_Measures to Improve the Stability of Existing Earth Dams - Corps of Engineers_
_Approach”, in Seismic Design of Embankments and Caverns, T.R. Howard, Ed.,_
_New York, ASCE._

_**Marsal, R.J. (1965).**_ _Discussion: Proceedings, 6th International Conference on Soil_
_Mechanics and Foundation Engineering, v. 3, p. 310-316._

_**Marsal, R.J. (1973).**_ _Mechanical properties of rockfill. Embankment-Dam_
_Engineering, Casagrande Volume, eds. Hirschfeld and Poulos, J. Wiley and Sons,_
_New York, pp. 109-200._

_**Marsal, R.J. and Resendiz, D.R. (1975).**_ _Presas de Tierra y Enrocamiento. Mexico._
_Ed Limusa, México, pp. 237-239._

_**Martin, A. (1990).**_ _Hacia una nueva regionalización y cálculo del peligro sísmico en_
_Chile. Memoria para optar al título de ingeniero civil. Universidad de Chile._

_**Murphy, J. R. and L. J. O'Brien (1977).**_ _The correlation of peak ground acceleration_
_amplitude with seismic intensity and other physical parameters, Bull. Seism. Soc._
_Am. 67, 877-915._

_**Noda, S., Uwabe, T. & Chiba, T. (1975).**_ _“Relation between seismic coefficient and_
_ground acceleration for gravity quay wall”, Report of Port and Harbour Research_
_Institute; 14(4): 67 -111._

_**Rajapakse, R. (2008).**_ _Geotechnical Engineering Calculations and Rules of Thumb._
_Elsevier, Oxford UK._

_**Read, J & Stacey, P (2009):**_ _Guidelines for open pit slopes design, CSIRO_
_Publishing._

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **40** de **41**

_**Ruiz, S. (2002).**_ _Fórmulas de atenuación para la subducción de Chile considerando_
_los dos mecanismos principales de sismogénesis y los efectos del suelo y las_
_asperezas. Memoria para optar al título profesional de ingeniero civil. Universidad_
_de Chile._

_**Ruiz, S., Saragoni, G.R. (2005).**_ _Fórmulas de atenuación para la subducción de_
_Chile considerando los dos mecanismos de sismogénesis y los efectos del suelo._

_**S y S Ingenieros Consultores Ltda. (2019)**_ _. Estudio de Riesgo Sísmico, realizado_
_en el Sector de emplazamiento del Proyecto._

_**Saragoni G R, Crempien J, Araya R. (1982).**_ _“Experimental measurement of Chile_
_seismic strong motion” Revista del I.D.I.E.M, University of Chile, Chile, 1982; 21: 67-_
_87. (In Spanish)._

_**Saragoni, R. (1993).**_ _Análisis de riesgo sísmico para la reconstrucción del Puerto_
_de Valparaíso. 6tas Jornadas Chilenas de Sismología e Ingeniería Antisísmica,_
_Santiago, Vol 2, 165-178._

_**Seed, H. B. (1979).**_ _"Soil Liquefaction and Cyclic Mobility Evaluation for Level_
_Ground During Earthquakes," Journal of the Geotechnical Engineering Division,_
_ASCE, Vol. 105, No. GT2._

_**Seed HB. (1980).**_ _“Considerations in the earthquake-resistant design of earth and_
_rockfill dams.” Géotechnique, 1979, Vol. 29, No. 3, pp. 215-263._

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com Página **41** de **41**

## ANEXO A RESULTADOS DE ENSAYOS DE MECÁNICA DE SUELOS (FUGRO)

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

.

.

.

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~05-04-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>2,65<br>~~150,00~~<br>300,00<br>65,17<br>0,24<br>2,14<br>2,27<br>5,81<br>-|

. **Nota:**

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D4767 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D4767 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D4767 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D4767 Sección 8.4~~|
|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Data Triaxial CIU - B - FCL1114-7-9.xl~~<br>|
|~~Ejecutado por~~<br>Fecha<br>|05-04-2023<br>~~PR~~|
|~~Procesado por~~<br>Fecha<br>|10-04-2023<br>~~MA~~|
|~~Aprobado por~~<br>Fecha|10-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>FCL1114sm9<br>~~-~~|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>510,00<br>500,10<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>~~650,00~~<br>499,90<br>500,50<br>-<br>149,50<br>100<br>-<br>8,36<br>2,35<br>2,17<br>0,22<br>149,50<br>0,00<br>1,12<br>0,53|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>FCL1114sm9<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|ETAPA DE CORTE|Col2|
|---|---|
|~~Presión radial efectiva inicial~~<br>~~[kPa]~~<br>Presión axial efectiva inicial<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|~~149,70~~<br>149,70<br>3,33|
|~~**Al peak del esfuerzo desviador**~~<br>Esfuerzo desviador corregido<br>[kPa]<br>Corrección de membrana aplicada<br>[kPa]<br>Corrección de dren aplicada<br>[kPa]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación radial local<br>[%]<br>Exceso PWP en base<br>[kPa]<br>Exceso PWP en altura-media<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|1,70<br>-<br>148,00<br>469,90<br>1,24<br>0,00<br>14,68<br>-<br>-<br>617,90<br>4,18<br>0,36<br>66145,46|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|-<br>-<br>382,77<br>0,16<br>0,00<br>1,52<br>58,40<br>-<br>91,30<br>474,07<br>5,19|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|138,90<br>462,77<br>601,67<br>4,33<br>0,92<br>0,00<br>9,97<br>-<br>-<br>10,80<br>-|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>~~-~~<br>FCL1114sm9|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>FCL1114sm9<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

0

0,2

0,4

0,6

0,8

1

1,2

0

0,2

0,4

0,6

0,8

1

1,2

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 2 4 6 8 10 12 14

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|s1|
|---|---|---|---|---|---|---|---|
|||||||Serie|s1|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
||||Serie|s1||||||||||||||||||||||||
|||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~11,00~~<br>11,00<br>149,50<br>149,50|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm9<br>-<br>CIUc03|

**FASE DE CONSOLIDACIÓN ISOTRÓPICA**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~149,70~~<br>149,70<br>469,90<br>14,68|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm9<br>-<br>CIUc03|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

.

.

.

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~04-04-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>-<br>2,65<br>~~150,00~~<br>300,00<br>54,02<br>0,22<br>2,17<br>2,27<br>4,50|

. **Nota:**

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D4767 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D4767 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D4767 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D4767 Sección 8.4~~|
|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Data Triaxial CIU - B - FCL1114-7-9.xl~~<br>|
|~~Ejecutado por~~<br>Fecha<br>|04-04-2023<br>~~PR~~|
|~~Procesado por~~<br>Fecha<br>|10-04-2023<br>~~MA~~|
|~~Aprobado por~~<br>Fecha|10-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|-<br>FCL1114sm8<br>~~-~~<br>CIUc02|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>510,00<br>503,70<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>7,47<br>2,38<br>2,21<br>0,20<br>298,00<br>0,00<br>1,86<br>-0,01<br>100<br>-<br>~~800,00~~<br>500,00<br>502,00<br>-<br>298,00|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc02<br>-<br>FCL1114sm8<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|ETAPA DE CORTE|Col2|
|---|---|
|~~Presión radial efectiva inicial~~<br>~~[kPa]~~<br>Presión axial efectiva inicial<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|298,00<br>3,29<br>~~298,00~~|
|~~**Al peak del esfuerzo desviador**~~<br>Esfuerzo desviador corregido<br>[kPa]<br>Corrección de membrana aplicada<br>[kPa]<br>Corrección de dren aplicada<br>[kPa]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación radial local<br>[%]<br>Exceso PWP en base<br>[kPa]<br>Exceso PWP en altura-media<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|737,68<br>4,27<br>0,30<br>94672,75<br>564,98<br>1,36<br>0,00<br>16,67<br>-<br>-<br>125,30<br>-<br>172,70|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|162,70<br>-<br>135,30<br>626,19<br>4,63<br>-<br>-<br>490,89<br>0,49<br>0,00<br>4,78|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|535,47<br>687,97<br>4,51<br>0,93<br>0,00<br>9,96<br>-<br>-<br>145,50<br>-<br>152,50|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm8<br>CIUc02<br>-|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc02<br>-<br>FCL1114sm8<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

0

0,2

0,4

0,6

0,8

1

1,2

1,4

1,6

1,8

2

0

0,2

0,4

0,6

0,8

1

1,2

1,4

1,6

1,8

2

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 5 10 15 20 25

|Col1|Col2|Col3|Col4|Col5|Series1|
|---|---|---|---|---|---|
||||||Series1|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
||||Serie|s1||||||||||||||||||||||||
|||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~6,10~~<br>6,10<br>298,00<br>298,00|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm8<br>-<br>CIUc02|

**FASE DE CONSOLIDACIÓN ISOTRÓPICA**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~298,00~~<br>298,00<br>564,98<br>16,67|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm8<br>-<br>CIUc02|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

.

.

.

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~03-04-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>-<br>2,65<br>~~150,00~~<br>300,00<br>62,61<br>0,23<br>2,15<br>2,27<br>5,49|

. **Nota:**

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D4767 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D4767 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D4767 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D4767 Sección 8.4~~|
|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Data Triaxial CIU - B - FCL1114-7-9.xl~~<br>|
|~~Ejecutado por~~<br>Fecha<br>|03-04-2023<br>~~PR~~|
|~~Procesado por~~<br>Fecha<br>|10-04-2023<br>~~MA~~|
|~~Aprobado por~~<br>Fecha|10-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|-<br>FCL1114sm7<br>~~-~~<br>CIUc03|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>509,00<br>500,00<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>7,31<br>2,38<br>2,22<br>0,19<br>500,00<br>0,00<br>3,07<br>0,44<br>100<br>-<br>~~1000,00~~<br>500,10<br>500,00<br>-<br>500,00|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>FCL1114sm7<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|ETAPA DE CORTE|Col2|
|---|---|
|~~Presión radial efectiva inicial~~<br>~~[kPa]~~<br>Presión axial efectiva inicial<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|500,00<br>3,30<br>~~500,00~~|
|~~**Al peak del esfuerzo desviador**~~<br>Esfuerzo desviador corregido<br>[kPa]<br>Corrección de membrana aplicada<br>[kPa]<br>Corrección de dren aplicada<br>[kPa]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación radial local<br>[%]<br>Exceso PWP en base<br>[kPa]<br>Exceso PWP en altura-media<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|1242,64<br>4,06<br>0,42<br>112698,27<br>936,54<br>1,53<br>0,00<br>20,23<br>-<br>-<br>193,90<br>-<br>306,10|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|303,00<br>-<br>197,00<br>913,75<br>4,64<br>-<br>-<br>716,75<br>0,30<br>0,00<br>2,85|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|873,47<br>1131,77<br>4,38<br>0,93<br>0,00<br>9,91<br>-<br>-<br>241,70<br>-<br>258,30|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm7<br>CIUc03<br>-|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>FCL1114sm7<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

0

0,5

1

1,5

2

2,5

3

3,5

0

0,5

1

1,5

2

2,5

3

3,5

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 5 10 15 20 25 30

|Col1|Col2|Col3|Col4|Se|ries1|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
||||Serie|s1||||||||||||||||||||||||
|||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~10,10~~<br>10,10<br>500,00<br>500,00|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm7<br>-<br>CIUc03|

**FASE DE CONSOLIDACIÓN ISOTRÓPICA**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~500,00~~<br>500,00<br>936,54<br>20,23|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm7<br>-<br>CIUc03|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

|Según ASTM D4767 (Set con 3 espécimenes) San Miguel, Santiago, Chile|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|
|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|
|**CONDICIONES INICIALES**|Espécimen 1|Espécimen 2|Espécimen 3|Espécimen 4|
|**Muestra número**|1|2|3|-|
|**Profundidad de la muestra (m)**|-|-|-|-|
|**Altura (mm)**|300,0|300,0|300,0|-|
|**Diámetro (mm)**|150,0|150,0|150,0|-|
|**Densidad seca (g/cm3)**|2,142|2,144|2,140|-|
|**Razón de vacíos**|0,237|0,236|0,238|-|
|**Contenido humedad (recortes) (%)**|5,49|4,50|5,81|-|
|**Grado de saturación**|61,4|50,5|64,6|-|
||||||
|**SATURACIÓN**|**SATURACIÓN**|**SATURACIÓN**|**SATURACIÓN**|**SATURACIÓN**|
|**Método de saturación**|Método húmedo|Método húmedo|Método húmedo|Método húmedo|
|**Contrapresión final (kPa)**|500|500|500|-|
|**Valor-B final**|0,96|0,95|0,96|-|
||||||
|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|
|**Esfuerzo de consolidación efectivo (kPa)**|500|300|150|-|
|**Tiempo 50% consolidación primaria (mins)**||||-|
|**Densidad seca final (g/cm3)**|2,210|2,184|2,164|-|
|**Razón de vacios final**|0,199|0,213|0,224|-|
|**Contenido de humedad final (%)**|7,48|8,03|8,43|-|
|**Grado de saturación final**|100|100|100|-|
|**Área final (mm2)**|17128,31|17343,08|17473,07|-|
|**Método de deformación de área**|Método A|Método A|Método A|-|
|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>10-04-2023<br>**Fecha Reporte:**<br>10-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>10-04-2023<br>**Fecha Reporte:**<br>10-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>10-04-2023<br>**Fecha Reporte:**<br>10-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>10-04-2023<br>**Fecha Reporte:**<br>10-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>10-04-2023<br>**Fecha Reporte:**<br>10-04-2023|

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 1 de 4

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

**Según ASTM D4767 (Set con 3 espécimenes)** San Miguel, Santiago, Chile

|CORTE|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Razón de deformación (%/min)**|0,056|0,056|0,056|-|
|**Condición a la falla**|**Condición a la falla**|**Condición a la falla**|**Condición a la falla**|**Condición a la falla**|
|**Criterio de falla**|Esfuerzo Desviador Máximo|Esfuerzo Desviador Máximo|Esfuerzo Desviador Máximo|Esfuerzo Desviador Máximo|
|**Esfuerzo desviador (kPa)**|939|569|471|-|
|**Deformación axial (%)**|20,1|16,7|14,6|-|
|**Esfuerzo principal mayor (kPa)**|1245|739|618|-|
|**Esfuerzo principal menor (kPa)**|306|171|147|-|
|**Obliquedad del esfuerzo efectivo (kPa)**|4,07|4,34|4,19|-|
|**Corrección de la membrana aplicada (kPa)**|4,58|3,77|3,29|-|
|**Corrección de los filtros aplicado (kPa)**|0,00|0,00|0,00|-|
|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>42 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>42 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>42 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>42 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>42 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 2 de 4

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

|Espé|Col2|cimen 1|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Espé|Espé|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|
||Espé|cimen 2|||||||||||
||Espé|cimen 3|||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||

|Según ASTM D4767 (Set con 3 espécimenes) San Miguel, Santiago, Chile|Col2|Col3|
|---|---|---|
|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestr**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información de la Muestra**<br>**Información del Proyecto**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestr**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información de la Muestra**<br>**Información del Proyecto**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm7-9<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestr**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información de la Muestra**<br>**Información del Proyecto**|
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>700<br>800<br>900<br>1000<br>0,00<br>2,00<br>4,00<br>6,00<br>8,00<br>10,00<br>12,00<br>14,00<br>16,00<br>18,00<br>20,00<br>**Esfuerzo desviador (kPa)**<br>**Deformación axial (%)**<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3<br>-50<br>0<br>50<br>100<br>150<br>200<br>250<br>300<br>350<br>0,00<br>2,00<br>4,00<br>6,00<br>8,00<br>10,00<br>12,00<br>14,00<br>16,00<br>18,00<br>20,00<br>**PWP inducido (kPa)**<br>**Deformación axial (%)**<br>Espécimen<br>1<br>Espécimen<br>2<br>Espécimen<br>3|0<br>100<br>200<br>300<br>400<br>500<br>600<br>700<br>800<br>900<br>1000<br>0,00<br>2,00<br>4,00<br>6,00<br>8,00<br>10,00<br>12,00<br>14,00<br>16,00<br>18,00<br>**Esfuerzo desviador (kPa)**<br>**Deformación axial (%)**<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|20,00|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|en|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||Espécim<br>1|en|en|
|||||||||||Espécim<br>2<br>|en<br>||
|||||||||||spéci<br>3|en|en|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
|00<br>2,|00<br>4,|00<br>6,|00<br>8,|00<br>10|,00<br>12|,00<br>14|,00<br>16|,00<br>18|,00<br>18|,00|20|20|

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 3 de 4

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

**Según ASTM D4767 (Set con 3 espécimenes)** San Miguel, Santiago, Chile

|Col1|Col2|Col3|Col4|Col5|Col6|Efectiv<br>Total 1|Col8|o 1|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||Efectiv<br>Total 1<br>|Efectiv<br>Total 1<br>|o 1<br>|o 1<br>|
||||||||Efectiv<br>Total 2<br>Efectiv|2<br>o 3||
|||||||Total 3<br>Envolve|Total 3<br>Envolve|nte de Falla|nte de Falla|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
||||**Esfuerz**|**o normal (kPa**|**)**|||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|
|||Specimen 2<br>Specimen 3|||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 4 de 4

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

.

.

.

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~27-03-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>-<br>2,65<br>~~150,00~~<br>300,00<br>67,95<br>0,24<br>2,14<br>2,27<br>6,16|

. **Nota:**

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D4767 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D4767 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D4767 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D4767 Sección 8.4~~|
|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Triaxial CIU - B - 200 kPa - FCL1114s~~<br>|
|~~Ejecutado por~~<br>Fecha<br>|27-03-2023<br>~~PR~~|
|~~Procesado por~~<br>Fecha<br>|04-04-2023<br>~~MA~~|
|~~Aprobado por~~<br>Fecha|04-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|-<br>FCL1114sm3<br>~~-~~<br>CIUc03|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>510,00<br>501,10<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>8,15<br>2,35<br>2,18<br>0,22<br>199,20<br>0,00<br>1,78<br>0,00<br>99<br>-<br>~~700,00~~<br>500,00<br>500,80<br>-<br>199,20|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>FCL1114sm3<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|ETAPA DE CORTE|Col2|
|---|---|
|~~Presión radial efectiva inicial~~<br>~~[kPa]~~<br>Presión axial efectiva inicial<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|199,40<br>3,27<br>~~199,40~~|
|~~**Al peak del esfuerzo desviador**~~<br>Esfuerzo desviador corregido<br>[kPa]<br>Corrección de membrana aplicada<br>[kPa]<br>Corrección de dren aplicada<br>[kPa]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación radial local<br>[%]<br>Exceso PWP en base<br>[kPa]<br>Exceso PWP en altura-media<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|812,00<br>4,22<br>0,50<br>61940,20<br>619,40<br>1,48<br>0,00<br>19,23<br>-<br>-<br>6,80<br>-<br>192,60|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|90,70<br>-<br>108,70<br>575,68<br>5,30<br>-<br>-<br>466,98<br>0,15<br>0,00<br>1,42|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|605,18<br>776,78<br>4,53<br>0,92<br>0,00<br>9,93<br>-<br>-<br>27,80<br>-<br>171,60|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm3<br>CIUc03<br>-|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc03<br>-<br>FCL1114sm3<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

0

0,2

0,4

0,6

0,8

1

1,2

1,4

1,6

1,8

2

0

0,2

0,4

0,6

0,8

1

1,2

1,4

1,6

1,8

2

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 5 10 15 20 25

|Col1|Col2|Col3|Col4|Col5|Series1|
|---|---|---|---|---|---|
||||||Series1|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
||||Serie|s1||||||||||||||||||||||||
|||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~9,10~~<br>9,10<br>199,20<br>199,20|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm3<br>-<br>CIUc03|

**FASE DE CONSOLIDACIÓN ISOTRÓPICA**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~199,40~~<br>199,40<br>619,40<br>19,23|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm3<br>-<br>CIUc03|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

.

.

.

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~27-03-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>2,65<br>~~150,00~~<br>300,00<br>62,83<br>0,23<br>2,15<br>2,27<br>5,52<br>-|

. **Nota:**

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D4767 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D4767 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D4767 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D4767 Sección 8.4~~|
|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Triaxial CIU - B - 400 kPa - FCL1114s~~<br>|
|~~Ejecutado por~~<br>Fecha<br>|27-03-2023<br>~~PR~~|
|~~Procesado por~~<br>Fecha<br>|04-04-2023<br>~~MA~~|
|~~Aprobado por~~<br>Fecha|04-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc02<br>-<br>FCL1114sm2<br>~~-~~|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>510,00<br>502,50<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>~~900,00~~<br>500,00<br>502,60<br>-<br>397,40<br>100<br>-<br>7,63<br>2,37<br>2,20<br>0,20<br>397,40<br>0,00<br>2,44<br>0,00|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc02<br>-<br>FCL1114sm2<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|ETAPA DE CORTE|Col2|
|---|---|
|~~Presión radial efectiva inicial~~<br>~~[kPa]~~<br>Presión axial efectiva inicial<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|~~397,80~~<br>397,80<br>3,28|
|~~**Al peak del esfuerzo desviador**~~<br>Esfuerzo desviador corregido<br>[kPa]<br>Corrección de membrana aplicada<br>[kPa]<br>Corrección de dren aplicada<br>[kPa]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación radial local<br>[%]<br>Exceso PWP en base<br>[kPa]<br>Exceso PWP en altura-media<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|176,60<br>-<br>222,20<br>764,21<br>1,50<br>0,00<br>19,71<br>-<br>-<br>986,41<br>4,44<br>0,39<br>97076,63|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|-<br>-<br>614,10<br>0,37<br>0,00<br>3,51<br>233,80<br>-<br>164,00<br>778,10<br>4,74|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|185,10<br>674,77<br>859,87<br>4,65<br>0,93<br>0,00<br>9,97<br>-<br>-<br>212,70<br>-|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc02<br>-<br>~~-~~<br>FCL1114sm2|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc02<br>-<br>FCL1114sm2<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

0

0,5

1

1,5

2

2,5

3

0

0,5

1

1,5

2

2,5

3

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 2 4 6 8 10 12 14 16

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||Series1||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
||||Serie|s1||||||||||||||||||||||||
|||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~7,30~~<br>7,30<br>397,40<br>397,40|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm2<br>-<br>CIUc02|

**FASE DE CONSOLIDACIÓN ISOTRÓPICA**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~397,80~~<br>397,80<br>764,21<br>19,71|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm2<br>-<br>CIUc02|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

.

.

.

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~24-03-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>2,65<br>~~150,00~~<br>300,00<br>70,08<br>0,24<br>2,13<br>2,27<br>6,44<br>-|

. **Nota:**

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D4767 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D4767 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D4767 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D4767 Sección 8.4~~|
|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|~~**Nota:**~~<br>Los procedimientos de prueba de Fugro están disponibles bajo petición|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Triaxial CIU - B - 600 kPa - FCL1114s~~<br>|
|~~Ejecutado por~~<br>Fecha<br>|24-03-2023<br>~~PR~~|
|~~Procesado por~~<br>Fecha<br>|04-04-2023<br>~~MA~~|
|~~Aprobado por~~<br>Fecha|04-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc01<br>-<br>FCL1114sm1<br>~~-~~|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>509,00<br>500,30<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>~~1100,00~~<br>500,10<br>499,20<br>-<br>600,80<br>99<br>-<br>7,40<br>2,37<br>2,21<br>0,20<br>600,80<br>0,00<br>3,60<br>-0,02|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc01<br>-<br>FCL1114sm1<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|ETAPA DE CORTE|Col2|
|---|---|
|~~Presión radial efectiva inicial~~<br>~~[kPa]~~<br>Presión axial efectiva inicial<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|~~600,00~~<br>600,00<br>3,25|
|~~**Al peak del esfuerzo desviador**~~<br>Esfuerzo desviador corregido<br>[kPa]<br>Corrección de membrana aplicada<br>[kPa]<br>Corrección de dren aplicada<br>[kPa]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación radial local<br>[%]<br>Exceso PWP en base<br>[kPa]<br>Exceso PWP en altura-media<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|262,80<br>-<br>338,20<br>1190,94<br>1,50<br>0,00<br>19,38<br>-<br>-<br>1529,14<br>4,52<br>0,66<br>90748,28|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|-<br>-<br>926,00<br>0,57<br>0,00<br>5,58<br>359,00<br>-<br>241,00<br>1167,00<br>4,84|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Excess base PWP<br>[kPa]<br>Excess mid height PWP<br>[kPa]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|281,10<br>1052,34<br>1333,44<br>4,74<br>0,93<br>0,00<br>9,91<br>-<br>-<br>318,90<br>-|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc01<br>-<br>~~-~~<br>FCL1114sm1|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIUc01<br>-<br>FCL1114sm1<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

0

0,5

1

1,5

2

2,5

3

3,5

4

0

0,5

1

1,5

2

2,5

3

3,5

4

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 5 10 15 20 25 30

|Col1|Col2|Col3|Col4|Se|Col6|ries1|
|---|---|---|---|---|---|---|
|||||Se|Se|ries1|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
||||Serie|s1||||||||||||||||||||||||
|||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~8,80~~<br>8,80<br>600,80<br>600,80|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm1<br>-<br>CIUc01|

**FASE DE CONSOLIDACIÓN ISOTRÓPICA**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**
Triaxial Consolidado Isotrópicamente No Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~600,00~~<br>600,00<br>1190,94<br>19,38|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm1<br>-<br>CIUc01|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-015 | Formato Informe Triaxial Consolidado Isotrópicamente No Drenado | Edición [00] Rev [00]

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

|Según ASTM D4767 (Set con 3 espécimenes) San Miguel, Santiago, Chile|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestreo:**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información del Proyecto**<br>**Información de la Muestra**|
|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|**Preparación**<br>**Gravedad específica**<br>2,65 (Asumido)<br>**Resultados**<br>Compactada|
|**CONDICIONES INICIALES**|Espécimen 1|Espécimen 2|Espécimen 3|Espécimen 4|
|**Muestra número**|1|2|3|-|
|**Profundidad de la muestra (m)**|-|-|-|-|
|**Altura (mm)**|300,0|300,0|300,0|-|
|**Diámetro (mm)**|150,0|150,0|150,0|-|
|**Densidad seca (g/cm3)**|2,141|2,141|2,141|-|
|**Razón de vacíos**|0,238|0,238|0,238|-|
|**Contenido humedad (recortes) (%)**|5,95|6,00|6,04|-|
|**Grado de saturación**|66,4|66,9|67,4|-|
||||||
|**SATURACIÓN**|**SATURACIÓN**|**SATURACIÓN**|**SATURACIÓN**|**SATURACIÓN**|
|**Método de saturación**|Método húmedo|Método húmedo|Método húmedo|Método húmedo|
|**Contrapresión final (kPa)**|500|500|500|-|
|**Valor-B final**|0,96|0,95|0,96|-|
||||||
|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|**CONSOLIDACIÓN**|
|**Esfuerzo de consolidación efectivo (kPa)**|600|400|200|-|
|**Tiempo 50% consolidación primaria (mins)**||||-|
|**Densidad seca final (g/cm3)**|2,221|2,195|2,180|-|
|**Razón de vacios final**|0,193|0,207|0,216|-|
|**Contenido de humedad final (%)**|7,28|7,80|8,12|-|
|**Grado de saturación final**|100|100|100|-|
|**Área final (mm2)**|17034,82|17240,77|17356,76|-|
|**Método de deformación de área**|Método A|Método A|Método A|-|
|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>05-04-2023<br>**Fecha Reporte:**<br>05-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>05-04-2023<br>**Fecha Reporte:**<br>05-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>05-04-2023<br>**Fecha Reporte:**<br>05-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>05-04-2023<br>**Fecha Reporte:**<br>05-04-2023|Observaciones:<br>**Solicitante**Byron Zambrano<br>**Empresa:** Minera BMR SpA<br>**Revisión:**<br>00<br>**Fecha Autorización:**<br>**Autorizado por:** ACH<br>Los resultados son aplicables solo a la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados.<br>A menos que se haya indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida.<br>**Información del Reporte**<br>05-04-2023<br>**Fecha Reporte:**<br>05-04-2023|

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 1 de 4

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

**Según ASTM D4767 (Set con 3 espécimenes)** San Miguel, Santiago, Chile

|CORTE|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Razón de deformación (%/min)**|0,056|0,056|0,056|-|
|**Condición a la falla**|**Condición a la falla**|**Condición a la falla**|**Condición a la falla**|**Condición a la falla**|
|**Criterio de falla**|Esfuerzo Desviador Máximo|Esfuerzo Desviador Máximo|Esfuerzo Desviador Máximo|Esfuerzo Desviador Máximo|
|**Esfuerzo desviador (kPa)**|1188|761|617|-|
|**Deformación axial (%)**|19,4|19,7|19,2|-|
|**Esfuerzo principal mayor (kPa)**|1525|980|809|-|
|**Esfuerzo principal menor (kPa)**|337|219|192|-|
|**Obliquedad del esfuerzo efectivo (kPa)**|4,52|4,48|4,21|-|
|**Corrección de la membrana aplicada (kPa)**|4,42|4,47|4,35|-|
|**Corrección de los filtros aplicado (kPa)**|0,00|0,00|0,00|-|
|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>41 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>41 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>41 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>41 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|Observaciones:<br>Cálculos realizados automáticamente por el software.<br>c' =<br>00 kPa<br>f' =<br>41 °<br>DIBUJOS DE LAS FALLAS<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 2 de 4

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

|Espé|Col2|cimen 1|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Espé|Espé|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|cimen 1|
||Espé<br>Espé|cimen 2<br>cimen 3|||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|en|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||Espécim<br>1|en|en|
|||||||||||Espécim<br>2|en||
|||||||||||Espécim<br>3|en||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||

|Según ASTM D4767 (Set con 3 espécimenes) San Miguel, Santiago, Chile|Col2|Col3|
|---|---|---|
|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestr**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información de la Muestra**<br>**Información del Proyecto**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestr**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información de la Muestra**<br>**Información del Proyecto**|**Nombre del Proyecto**<br>Caracterización de material estéril del botadero Dalmacia<br>**Ubicación del proyecto**<br>-<br>**Código Proyecto:**<br>232641<br>**Número de Muestra:**<br>FCL1114sm1-3<br>**Profundidad (m):**<br>-<br>**Número del Pozo:**<br>-<br>**Tipo de Muestra:**<br>B<br>**Ubicación del Muestr**<br>-<br>**Muestreado Por:**<br>Cliente<br>**Fecha del Muestreo:**<br>-<br>**Descripción Visual:**<br>Grava con arenas y limos<br>**Información de la Muestra**<br>**Información del Proyecto**|
|0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>0,00<br>2,00<br>4,00<br>6,00<br>8,00<br>10,00<br>12,00<br>14,00<br>16,00<br>18,00<br>20,00<br>**Esfuerzo desviador (kPa)**<br>**Deformación axial (%)**<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3<br>0<br>50<br>100<br>150<br>200<br>250<br>300<br>350<br>400<br>450<br>0,00<br>2,00<br>4,00<br>6,00<br>8,00<br>10,00<br>12,00<br>14,00<br>16,00<br>18,00<br>20,00<br>**PWP inducido (kPa)**<br>**Deformación axial (%)**<br>Espécimen<br>1<br>Espécimen<br>2<br>Espécimen<br>3|0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>0,00<br>2,00<br>4,00<br>6,00<br>8,00<br>10,00<br>12,00<br>14,00<br>16,00<br>18,00<br>**Esfuerzo desviador (kPa)**<br>**Deformación axial (%)**<br>Espécimen 1<br>Espécimen 2<br>Espécimen 3|20,00|

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 3 de 4

**INFORME DE RESULTADOS DE ENSAYOS** **FUGRO**

**COMPRESIÓN TRIAXIAL CONSOLIDADO NO DRENADO** Av. Departamental 1292

**Según ASTM D4767 (Set con 3 espécimenes)** San Miguel, Santiago, Chile

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||Efectivo 1<br>Total 1<br>|||
|||||||||||||
||||||||||Efectivo 2<br>Total 2<br>Efectivo 3<br>|||
|||||||||||||
||||||||||Total 3<br>Envolvente|de Falla|de Falla|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||**Esfuerz**|**o normal (k**|**Pa)**||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|Specimen 1<br>|
|||Specimen 2<br>Specimen 3|||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||

Fugro Chile S.A. | With operating companies throughout the world

**D** +2 2371 0698 | **W** fugro.com

Página 4 de 4

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~29-03-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>-<br>2,65<br>~~150,0~~<br>300,0<br>67<br>0,239<br>2,14<br>2,27<br>6,0|

.

.

.

. **Nota:**

.

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D7181 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D7181 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D7181 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D7181 Sección 8.4~~|
|~~**Nota:**~~|~~**Nota:**~~|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Triaxial CID - LB - 200 kPa - FCL111~~<br>|
|~~Procesado por~~<br>Fecha<br>|29-03-2023<br>~~MA~~|
|~~Chequeado por~~<br>Fecha<br>|05-04-2023<br>~~ACH~~|
|~~Aprovado por~~<br>Fecha|05-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|-<br>FCL1114sm6<br>~~-~~<br>CIDc03|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>510,00<br>503,40<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>8,14<br>2,35<br>2,18<br>0,22<br>199,60<br>0,00<br>1,73<br>0,01<br>99<br>-<br>~~700,00~~<br>500,10<br>500,40<br>-<br>199,60|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc03<br>-<br>FCL1114sm6<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|ETAPA DE CORTE (DRENADO)|Col2|
|---|---|
|~~Initial effective radial pressure~~<br>~~[kPa]~~<br>Initial effective axial pressure<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|199,60<br>1,44<br>~~199,60~~|
|~~**At peak deviator stress**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|815,13<br>4,08<br>0,88<br>34834,67<br>615,23<br>1,00<br>0,00<br>10,97<br>-<br>-<br>1,78<br>-<br>199,90|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|1,77<br>-<br>199,30<br>814,13<br>4,08<br>-<br>-<br>614,83<br>1,03<br>0,00<br>11,42|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|612,44<br>812,24<br>4,07<br>0,93<br>0,00<br>9,99<br>-<br>-<br>1,79<br>-<br>199,80|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm6<br>CIDc03<br>-|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc03<br>-<br>FCL1114sm6<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

0

0,2

0,4

0,6

0,8

1

1,2

1,4

1,6

1,8

2

0

0,2

0,4

0,6

0,8

1

1,2

1,4

1,6

1,8

2

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 2 4 6 8 10 12 14

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|olumétrica|
|---|---|---|---|---|---|---|---|
|||||||Deformación V|lumétrica|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|a|Col26|Col27|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||Def|ormaci|ón V|lu|ét|ric|a|a|a|
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~6,50~~<br>6,50<br>199,60<br>199,60|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm6<br>-<br>CIDc03|

**FASE DE CONSOLIDACIÓN ISOTROPICA**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|700<br>600<br>500<br>[kPa]<br>400<br>s') r<br>-<br>300 (s' a<br>q,<br>200<br>100<br>0<br>0 2 4 6 8 10 12 14 16 18 20<br>DEFORMACIÓN AXIAL [%]|Col2|
|---|---|
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>700<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>**q, (s'a - s'r) [kPa]**<br>**DEFORMACIÓN AXIAL [%]**||
||0<br>0,2<br>0,4<br>0,6<br>0,8<br>1<br>1,2<br>1,4<br>1,6<br>1,8<br>2<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>**DEFORMACIÓN VOLUMÉTRICA [%]**<br>**DEFORMACIÓN AXIAL [%]**|

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~199,60~~<br>199,60<br>615,23<br>10,97|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm6<br>-<br>CIDc03|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~29-03-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>2,65<br>~~150,0~~<br>300,0<br>68<br>0,241<br>2,14<br>2,27<br>6,2<br>-|

.

.

.

. **Nota:**

.

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D7181 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D7181 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D7181 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D7181 Sección 8.4~~|
|~~**Nota:**~~|~~**Nota:**~~|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Triaxial CID - LB - 400 kPa - FCL111~~<br>|
|~~Procesado por~~<br>Fecha<br>|29-03-2023<br>~~MA~~|
|~~Chequeado por~~<br>Fecha<br>|05-04-2023<br>~~ACH~~|
|~~Aprovado por~~<br>Fecha|05-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc02<br>-<br>FCL1114sm4<br>~~-~~|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>510,00<br>499,90<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>~~900,00~~<br>500,00<br>499,20<br>-<br>400,80<br>100<br>-<br>8,06<br>2,38<br>2,20<br>0,21<br>400,80<br>0,00<br>2,88<br>-0,02|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc02<br>-<br>FCL1114sm4<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|ETAPA DE CORTE (DRENADO)|Col2|
|---|---|
|~~Initial effective radial pressure~~<br>~~[kPa]~~<br>Initial effective axial pressure<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|~~400,20~~<br>400,20<br>2,80|
|~~**At peak deviator stress**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|1,87<br>-<br>399,60<br>1368,27<br>1,09<br>0,00<br>12,12<br>-<br>-<br>1767,87<br>4,42<br>0,97<br>70326,02|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|-<br>-<br>1367,81<br>1,07<br>0,00<br>11,92<br>1,87<br>-<br>398,60<br>1766,41<br>4,43|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|399,60<br>1353,86<br>1753,46<br>4,39<br>0,93<br>0,00<br>9,91<br>-<br>-<br>1,89<br>-|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc02<br>-<br>~~-~~<br>FCL1114sm4|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc02<br>-<br>FCL1114sm4<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

0

0,5

1

1,5

2

2,5

3

3,5

0

0,5

1

1,5

2

2,5

3

3,5

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 5 10 15 20 25 30

|Col1|Col2|Col3|Col4|Col5|ies1|
|---|---|---|---|---|---|
|||||Ser|ies1|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||S|eries|1||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~10,10~~<br>10,10<br>400,80<br>400,80|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm4<br>-<br>CIDc02|

**FASE DE CONSOLIDACIÓN ISOTROPICA**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|1600<br>1400<br>1200<br>1000 [kPa]<br>800 s') r<br>-<br>(s' a<br>600 q,<br>400<br>200<br>0<br>0 2 4 6 8 10 12 14 16 18 20<br>DEFORMACIÓN AXIAL [%]|Col2|
|---|---|
|0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>1600<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>**q, (s'a - s'r) [kPa]**<br>**DEFORMACIÓN AXIAL [%]**||
||0<br>0,2<br>0,4<br>0,6<br>0,8<br>1<br>1,2<br>1,4<br>1,6<br>1,8<br>2<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>**DEFORMACIÓN VOLUMÉTRICA [%]**<br>**DEFORMACIÓN AXIAL [%]**|

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~400,20~~<br>400,20<br>1368,27<br>12,12|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm4<br>-<br>CIDc02|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

.

.

.

.

.

.

.

.

.

|GENERAL|Col2|
|---|---|
|~~Fecha de inicio de ensayo~~<br>Tipo de muestra<br>Tipos de drenes instalados|One end only<br>Re-compacted<br>~~29-03-2023~~|

|INICIAL|Col2|
|---|---|
|~~Diámetro~~<br>~~[mm]~~<br>Longitud<br>[mm]<br>Contenido de humedad<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]<br>Densidad de partículas asumida<br>[Mg/m3]<br>Corte Torvane<br>[kPa]<br>Penetrómetro de bolsillo<br>[kPa]|-<br>2,65<br>~~150,0~~<br>300,0<br>67<br>0,239<br>2,14<br>2,27<br>6,0<br>-|

.

.

.

. **Nota:**

.

.

.

|PROCEDIMIENTOS UTILIZADOS EN EL ENSAYO|Col2|
|---|---|
|~~Set-up del espécimen~~<br>|~~ASTM D7181 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~ASTM D7181 Sección 8.2~~<br>|
|~~Consolidación - Isotrópica~~<br>Consolidación - Anisotrópica<br>|~~ASTM D7181 Sección 8.3~~<br>|
|~~Corte~~<br>|~~ASTM D7181 Sección 8.4~~|
|~~**Nota:**~~|~~**Nota:**~~|

|ASEGURAMIENTO DE CALIDAD|Col2|
|---|---|
|~~Edición de plantilla~~<br>|~~1,9~~<br>|
|~~Nombre de archivo~~<br>|~~232641 \ 232641 - Triaxial CID - LB - 600 kPa - FCL111~~<br>|
|~~Procesado por~~<br>Fecha<br>|29-03-2023<br>~~MA~~|
|~~Chequeado por~~<br>Fecha<br>|05-04-2023<br>~~ACH~~|
|~~Aprovado por~~<br>Fecha|05-04-2023<br>~~ACH~~|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc01<br>-<br>FCL1114sm4<br>~~-~~|

.

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|SATURACIÓN|Col2|
|---|---|
|~~Incrementos de presión aplicados~~<br>~~[kPa]~~<br>Presión diferencial utilizada<br>[kPa]<br>Presión de celda<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Valor B alcanzado<br>[-]|1,00<br>~~Como instruido por ensayo~~<br>N/A<br>500,00<br>490,60<br>-|

|CONSOLIDACIÓN: ISOTROPICA|Col2|
|---|---|
|~~Presión de celda~~<br>~~[kPa]~~<br>Contrapresión<br>[kPa]<br>PWP base<br>[kPa]<br>PWP a media-altura<br>[kPa]<br>Presión radial efectiva<br>[kPa]<br>Presión axial efectiva<br>[kPa]<br>Esfuerzo desviador<br>[kPa]<br>Deformación volumétrica<br>[%]<br>Deformación axial externa<br>[%]<br>Deformación axial local<br>[%]<br>Deformación local radial<br>[%]<br>Contenido húmedo<br>[%]<br>Densidad húmeda<br>[Mg/m3]<br>Densidad seca<br>[Mg/m3]<br>Índice de vacíos<br>[-]<br>Grado de saturación<br>[%]|-<br>~~1140,00~~<br>540,10<br>542,90<br>-<br>597,10<br>100<br>-<br>7,81<br>2,38<br>2,21<br>0,20<br>597,10<br>0,00<br>3,20<br>-0,01|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc01<br>-<br>FCL1114sm4<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|ETAPA DE CORTE (DRENADO)|Col2|
|---|---|
|~~Initial effective radial pressure~~<br>~~[kPa]~~<br>Initial effective axial pressure<br>[kPa]<br>Rate of strain<br>[%/hour]<br>|~~597,10~~<br>597,10<br>2,75|
|~~**At peak deviator stress**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>e50<br>[%]<br>Secant modulus (E50) ate50<br>[kPa]<br>|1,93<br>-<br>598,60<br>1997,30<br>0,90<br>0,00<br>9,54<br>-<br>-<br>2595,90<br>4,34<br>1,23<br>81092,59|
|~~**At peak principal effective stress ratio**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]<br>|-<br>-<br>1996,03<br>0,91<br>0,00<br>9,74<br>1,93<br>-<br>597,10<br>2593,13<br>4,34|
|~~**At 10% external axial strain**~~<br>Corrected deviator stress<br>[kPa]<br>Membrane correction applied<br>[kPa]<br>Drain correction applied<br>[kPa]<br>External axial strain<br>[%]<br>Local axial strain<br>[%]<br>Local radial strain<br>[%]<br>Volumetric strain<br>[%]<br>Local volumetric strain<br>[%]<br>Effective radial pressure<br>[kPa]<br>Effective axial pressure<br>[kPa]<br>Principal effective stress ratio<br>[-]|598,90<br>1994,69<br>2593,59<br>4,33<br>0,93<br>0,00<br>9,93<br>-<br>-<br>1,93<br>-|

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc01<br>-<br>~~-~~<br>FCL1114sm4|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|IDENTIFICACIÓN DE ENSAYO|Col2|
|---|---|
|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|CIDc01<br>-<br>FCL1114sm4<br>~~-~~|

**RESUMEN ENSAYO TRIAXIAL CONSOLIDADO ISOTROPICAMENTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

0

0,5

1

1,5

2

2,5

3

3,5

0

0,5

1

1,5

2

2,5

3

3,5

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

**RAIZ CUADRADA DE TIEMPO [Minutos** **[0,5]** **]**

0 5 10 15 20 25

|Col1|Col2|Col3|Col4|Col5|Series1|
|---|---|---|---|---|---|
||||||Series1|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

**ESFUERZO AXIAL EFECTIVO [kPa]**

1 10 100 1000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||S|eries|1||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>σ'r final<br>σ'a final|~~kPa~~<br>kPa<br>kPa<br>kPa<br>~~8,50~~<br>8,50<br>597,10<br>597,10|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm4<br>-<br>CIDc01|

**FASE DE CONSOLIDACIÓN ISOTROPICA**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

**Informe de Ensayo de Laboratorio**

Triaxial Consolidado Isotrópicamente Drenado

|2500<br>2000<br>[kPa]<br>1500<br>s') r<br>-<br>(s' a<br>1000<br>q,<br>500<br>0<br>0 2 4 6 8 10 12 14 16 18 20<br>DEFORMACIÓN AXIAL [%]|Col2|
|---|---|
|0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>**q, (s'a - s'r) [kPa]**<br>**DEFORMACIÓN AXIAL [%]**||
||0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>**DEFORMACIÓN VOLUMÉTRICA [%]**<br>**DEFORMACIÓN AXIAL [%]**|

|IDENTIFICACIÓN DE ENSAYO|Col2|Col3|Col4|
|---|---|---|---|
|σ'r inicial<br>σ'a inicial<br>qpeak<br>Defor. en qpeak|~~kPa~~<br>kPa<br>kPa<br>%<br>~~597,10~~<br>597,10<br>1997,30<br>9,54|~~ID Pozo~~<br>ID Muestra<br>Profundidad [m]<br>Número de ensayo|~~-~~<br>FCL1114sm4<br>-<br>CIDc01|

**FASE DE CORTE**

FCSA-LAN-LAB-FO-I-016 | Formato Informe Triaxial Consolidado Isotrópicamente Drenado | Edición [00] Rev [00]

|pción de la Muestra: ID Laboratorio: Resultados General Grava con arena y limos FCL1114sm4-6|Col2|Col3|Col4|
|---|---|---|---|
|~~General~~<br><br><br><br>|~~General~~<br><br><br><br>|~~General~~<br><br><br><br>|~~General~~<br><br><br><br>|
|~~N° Probeta~~|~~Probeta 1~~|~~Probeta 2~~|~~Probeta 3~~|
|~~Fecha Inicio Ensayo~~<br>|~~29-03-2023~~<br>|~~29-03-2023~~<br>|~~31-03-2023~~<br>|
|~~Tipo de Muestra~~|~~Recompacted~~|~~Recompacted~~|~~Recompacted~~|
|~~Orientación de la Muestra~~<br>|~~Vertical~~<br>|~~Vertical~~<br>|~~Vertical~~<br>|
|~~Tipo de Drenaje~~|~~One end~~|~~One end~~|~~One end~~|

|Condiciones Iniciales|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Diámetro~~|mm|~~150,0~~|~~150,0~~|~~150,0~~|
|~~Alto~~<br>|mm|~~300,0~~<br>|~~300,0~~<br>|~~300,0~~<br>|
|~~Contenido de Humedad~~|%<br>|~~6,0~~|~~6,2~~|~~4,9~~|
|~~Densidad Húmeda~~<br>|~~g/cm~~3<br>|~~2,268~~<br>|~~2,268~~<br>|~~2,268~~<br>|
|~~Densidad Seca~~|~~g/cm~~3|~~2,139~~|~~2,136~~|~~2,163~~|
|~~índice de Vacíos~~<br>|~~índice de Vacíos~~<br>|~~0,239~~<br>|~~0,241~~<br>|~~0,225~~<br>|
|~~Grado de Saturación~~|%|~~67,0~~|~~68,4~~|~~57,4~~|

|Saturación|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Incrementos de Presión Aplicados~~<br>|kPa<br>|~~50~~<br>|~~50~~<br>|~~50~~<br>|
|~~Diferencia de Presiones Usada~~<br>|~~kPa~~|~~10~~<br>|~~10~~<br>|~~10~~<br>|
|~~Presión de Poros al Completar~~<br>|kPa|~~491~~<br>|~~500~~<br>|~~503~~<br>|
|~~Presión de Celda al Completar~~<br>|kPa|~~500~~<br>|~~510~~<br>|~~510~~<br>|
|~~Valor B Alcanzado~~|~~Valor B Alcanzado~~|~~0,95~~|~~0,98~~|~~0,96~~|

|Consolidación: Isotropica|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Presión de Celda~~|kPa|~~1140,00~~|~~890,00~~|~~690,00~~|
|~~Contrapresión~~<br>|kPa|~~540,00~~<br>|~~590,00~~<br>|~~590,00~~<br>|
|~~Presión de Celda Efectiva~~|kPa<br>|~~600,00~~|~~300,00~~|~~100,00~~|
|~~Presión de Poros al Completar~~|~~kPa~~|~~540,70~~|~~499,20~~|~~504,60~~|
|~~Disipación de la Presión de Poros~~<br>|%|~~53,33~~<br>|~~-0,78~~<br>|~~1,27~~<br>|
|~~Contenido de Humedad~~|%<br>|~~7,52~~|~~7,74~~|~~7,70~~|
|~~Densidad Húmeda~~<br>|~~g/cm~~3<br>|~~2,38~~<br>|~~2,37~~<br>|~~2,37~~<br>|
|~~Densidad Seca~~|~~g/cm~~3|~~2,21~~|~~2,20~~|~~2,20~~|
|~~índice de Vacíos~~<br>|~~índice de Vacíos~~<br>|~~0,20~~<br>|~~0,21~~<br>|~~0,20~~<br>|
|~~Grado de Saturación~~|%|~~100~~|~~100~~|~~100~~|
|~~Deformación Volumétrica~~|%|~~3,20~~|~~2,88~~|~~1,73~~|

|Procedimientos del Ensayo|Col2|Col3|
|---|---|---|
|~~Montaje de las Probetas~~<br>|~~Montaje de las Probetas~~<br>|~~ASTM D7181 Sección 6-7~~<br>|
|~~Saturación~~<br>|~~Saturación~~<br>|~~ASTM D7181 Sección 8.2~~<br>|
|~~Consolidación Isotropica~~<br>|~~Consolidación Isotropica~~<br>|~~ASTM D7181 Sección 8.6~~<br>|
|~~Corte~~|~~Corte~~|~~ASTM D7181 Sección 8.4~~|
|~~Notas:~~|~~Los procedimientos de prueba de Fugro están disponibles bajo petición~~|~~Los procedimientos de prueba de Fugro están disponibles bajo petición~~|

|INFORME DE ENSAYO DE LABORATORIO<br>Triaxial Consolidado Isotropicamente Drenado<br>Según: ASTM D7181-20|Col2|Col3|Col4|
|---|---|---|---|
|**Nombre Proyecto:**|Caracterización de material estéril del botadero Dalmacia<br>|**Código del Proyecto:**|232641|
|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|
|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|
|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|
|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|
|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|
|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|
|mm<br>mm<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>kPa<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>kPa<br>kPa<br>~~kPa~~<br>%<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>%<br>~~General~~<br>~~Fecha Inicio Ensayo~~<br>~~29-03-2023~~<br>~~29-03-2023~~<br>~~31-03-2023~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Orientación de la Muestra~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Tipo de Muestra~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Tipo de Drenaje~~<br>~~One end~~<br>~~One end~~<br>~~One end~~<br>~~Condiciones Iniciales~~<br>~~Alto~~<br>~~300,0~~<br>~~300,0~~<br>~~300,0~~<br>~~Diámetro~~<br>~~150,0~~<br>~~150,0~~<br>~~150,0~~<br>~~Densidad Húmeda~~<br>~~2,268~~<br>~~2,268~~<br>~~2,268~~<br>~~Contenido de Humedad~~<br>~~6,0~~<br>~~6,2~~<br>~~4,9~~<br>~~índice de Vacíos~~<br>~~0,239~~<br>~~0,241~~<br>~~0,225~~<br>~~Densidad Seca~~<br>~~2,139~~<br>~~2,136~~<br>~~2,163~~<br>~~Grado de Saturación~~<br>~~67,0~~<br>~~68,4~~<br>~~57,4~~<br>~~Saturación~~<br>~~Incrementos de Presión Aplicados~~<br>~~50~~<br>~~50~~<br>~~50~~<br>~~Diferencia de Presiones Usada~~<br>~~10~~<br>~~10~~<br>~~10~~<br>~~Presión de Poros al Completar~~<br>~~491~~<br>~~500~~<br>~~503~~<br>~~Presión de Celda al Completar~~<br>~~500~~<br>~~510~~<br>~~510~~<br>~~Valor B Alcanzado~~<br>~~0,95~~<br>~~0,98~~<br>~~0,96~~<br>~~Consolidación: Isotropica~~<br>~~Contrapresión~~<br>~~540,00~~<br>~~590,00~~<br>~~590,00~~<br>~~Presión de Celda~~<br>~~1140,00~~<br>~~890,00~~<br>~~690,00~~<br>~~Disipación de la Presión de Poros~~<br>~~53,33~~<br>~~-0,78~~<br>~~1,27~~<br>~~Presión de Poros al Completar~~<br>~~540,70~~<br>~~499,20~~<br>~~504,60~~<br>~~Presión de Celda Efectiva~~<br>~~600,00~~<br>~~300,00~~<br>~~100,00~~<br>~~Densidad Húmeda~~<br>~~2,38~~<br>~~2,37~~<br>~~2,37~~<br>~~Contenido de Humedad~~<br>~~7,52~~<br>~~7,74~~<br>~~7,70~~<br>~~índice de Vacíos~~<br>~~0,20~~<br>~~0,21~~<br>~~0,20~~<br>~~Densidad Seca~~<br>~~2,21~~<br>~~2,20~~<br>~~2,20~~<br>~~Deformación Volumétrica~~<br>~~3,20~~<br>~~2,88~~<br>~~1,73~~<br>~~Grado de Saturación~~<br>~~100~~<br>~~100~~<br>~~100~~<br>~~Procedimientos del Ensayo~~<br>~~Montaje de las Probetas~~<br>~~ASTM D7181 Sección 6-7~~<br>~~Saturación~~<br>~~ASTM D7181 Sección 8.2~~<br>~~Consolidación Isotropica~~<br>~~ASTM D7181 Sección 8.6~~<br>~~Notas:~~<br>~~Los procedimientos de prueba de Fugro están disponibles bajo petición~~<br>~~Corte~~<br>~~ASTM D7181 Sección 8.4~~<br>|mm<br>mm<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>kPa<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>kPa<br>kPa<br>~~kPa~~<br>%<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>%<br>~~General~~<br>~~Fecha Inicio Ensayo~~<br>~~29-03-2023~~<br>~~29-03-2023~~<br>~~31-03-2023~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Orientación de la Muestra~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Tipo de Muestra~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Tipo de Drenaje~~<br>~~One end~~<br>~~One end~~<br>~~One end~~<br>~~Condiciones Iniciales~~<br>~~Alto~~<br>~~300,0~~<br>~~300,0~~<br>~~300,0~~<br>~~Diámetro~~<br>~~150,0~~<br>~~150,0~~<br>~~150,0~~<br>~~Densidad Húmeda~~<br>~~2,268~~<br>~~2,268~~<br>~~2,268~~<br>~~Contenido de Humedad~~<br>~~6,0~~<br>~~6,2~~<br>~~4,9~~<br>~~índice de Vacíos~~<br>~~0,239~~<br>~~0,241~~<br>~~0,225~~<br>~~Densidad Seca~~<br>~~2,139~~<br>~~2,136~~<br>~~2,163~~<br>~~Grado de Saturación~~<br>~~67,0~~<br>~~68,4~~<br>~~57,4~~<br>~~Saturación~~<br>~~Incrementos de Presión Aplicados~~<br>~~50~~<br>~~50~~<br>~~50~~<br>~~Diferencia de Presiones Usada~~<br>~~10~~<br>~~10~~<br>~~10~~<br>~~Presión de Poros al Completar~~<br>~~491~~<br>~~500~~<br>~~503~~<br>~~Presión de Celda al Completar~~<br>~~500~~<br>~~510~~<br>~~510~~<br>~~Valor B Alcanzado~~<br>~~0,95~~<br>~~0,98~~<br>~~0,96~~<br>~~Consolidación: Isotropica~~<br>~~Contrapresión~~<br>~~540,00~~<br>~~590,00~~<br>~~590,00~~<br>~~Presión de Celda~~<br>~~1140,00~~<br>~~890,00~~<br>~~690,00~~<br>~~Disipación de la Presión de Poros~~<br>~~53,33~~<br>~~-0,78~~<br>~~1,27~~<br>~~Presión de Poros al Completar~~<br>~~540,70~~<br>~~499,20~~<br>~~504,60~~<br>~~Presión de Celda Efectiva~~<br>~~600,00~~<br>~~300,00~~<br>~~100,00~~<br>~~Densidad Húmeda~~<br>~~2,38~~<br>~~2,37~~<br>~~2,37~~<br>~~Contenido de Humedad~~<br>~~7,52~~<br>~~7,74~~<br>~~7,70~~<br>~~índice de Vacíos~~<br>~~0,20~~<br>~~0,21~~<br>~~0,20~~<br>~~Densidad Seca~~<br>~~2,21~~<br>~~2,20~~<br>~~2,20~~<br>~~Deformación Volumétrica~~<br>~~3,20~~<br>~~2,88~~<br>~~1,73~~<br>~~Grado de Saturación~~<br>~~100~~<br>~~100~~<br>~~100~~<br>~~Procedimientos del Ensayo~~<br>~~Montaje de las Probetas~~<br>~~ASTM D7181 Sección 6-7~~<br>~~Saturación~~<br>~~ASTM D7181 Sección 8.2~~<br>~~Consolidación Isotropica~~<br>~~ASTM D7181 Sección 8.6~~<br>~~Notas:~~<br>~~Los procedimientos de prueba de Fugro están disponibles bajo petición~~<br>~~Corte~~<br>~~ASTM D7181 Sección 8.4~~<br>|mm<br>mm<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>kPa<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>kPa<br>kPa<br>~~kPa~~<br>%<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>%<br>~~General~~<br>~~Fecha Inicio Ensayo~~<br>~~29-03-2023~~<br>~~29-03-2023~~<br>~~31-03-2023~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Orientación de la Muestra~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Tipo de Muestra~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Tipo de Drenaje~~<br>~~One end~~<br>~~One end~~<br>~~One end~~<br>~~Condiciones Iniciales~~<br>~~Alto~~<br>~~300,0~~<br>~~300,0~~<br>~~300,0~~<br>~~Diámetro~~<br>~~150,0~~<br>~~150,0~~<br>~~150,0~~<br>~~Densidad Húmeda~~<br>~~2,268~~<br>~~2,268~~<br>~~2,268~~<br>~~Contenido de Humedad~~<br>~~6,0~~<br>~~6,2~~<br>~~4,9~~<br>~~índice de Vacíos~~<br>~~0,239~~<br>~~0,241~~<br>~~0,225~~<br>~~Densidad Seca~~<br>~~2,139~~<br>~~2,136~~<br>~~2,163~~<br>~~Grado de Saturación~~<br>~~67,0~~<br>~~68,4~~<br>~~57,4~~<br>~~Saturación~~<br>~~Incrementos de Presión Aplicados~~<br>~~50~~<br>~~50~~<br>~~50~~<br>~~Diferencia de Presiones Usada~~<br>~~10~~<br>~~10~~<br>~~10~~<br>~~Presión de Poros al Completar~~<br>~~491~~<br>~~500~~<br>~~503~~<br>~~Presión de Celda al Completar~~<br>~~500~~<br>~~510~~<br>~~510~~<br>~~Valor B Alcanzado~~<br>~~0,95~~<br>~~0,98~~<br>~~0,96~~<br>~~Consolidación: Isotropica~~<br>~~Contrapresión~~<br>~~540,00~~<br>~~590,00~~<br>~~590,00~~<br>~~Presión de Celda~~<br>~~1140,00~~<br>~~890,00~~<br>~~690,00~~<br>~~Disipación de la Presión de Poros~~<br>~~53,33~~<br>~~-0,78~~<br>~~1,27~~<br>~~Presión de Poros al Completar~~<br>~~540,70~~<br>~~499,20~~<br>~~504,60~~<br>~~Presión de Celda Efectiva~~<br>~~600,00~~<br>~~300,00~~<br>~~100,00~~<br>~~Densidad Húmeda~~<br>~~2,38~~<br>~~2,37~~<br>~~2,37~~<br>~~Contenido de Humedad~~<br>~~7,52~~<br>~~7,74~~<br>~~7,70~~<br>~~índice de Vacíos~~<br>~~0,20~~<br>~~0,21~~<br>~~0,20~~<br>~~Densidad Seca~~<br>~~2,21~~<br>~~2,20~~<br>~~2,20~~<br>~~Deformación Volumétrica~~<br>~~3,20~~<br>~~2,88~~<br>~~1,73~~<br>~~Grado de Saturación~~<br>~~100~~<br>~~100~~<br>~~100~~<br>~~Procedimientos del Ensayo~~<br>~~Montaje de las Probetas~~<br>~~ASTM D7181 Sección 6-7~~<br>~~Saturación~~<br>~~ASTM D7181 Sección 8.2~~<br>~~Consolidación Isotropica~~<br>~~ASTM D7181 Sección 8.6~~<br>~~Notas:~~<br>~~Los procedimientos de prueba de Fugro están disponibles bajo petición~~<br>~~Corte~~<br>~~ASTM D7181 Sección 8.4~~<br>|mm<br>mm<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>kPa<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>kPa<br>kPa<br>~~kPa~~<br>%<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>%<br>%<br>~~General~~<br>~~Fecha Inicio Ensayo~~<br>~~29-03-2023~~<br>~~29-03-2023~~<br>~~31-03-2023~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Orientación de la Muestra~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Vertical~~<br>~~Tipo de Muestra~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Recompacted~~<br>~~Tipo de Drenaje~~<br>~~One end~~<br>~~One end~~<br>~~One end~~<br>~~Condiciones Iniciales~~<br>~~Alto~~<br>~~300,0~~<br>~~300,0~~<br>~~300,0~~<br>~~Diámetro~~<br>~~150,0~~<br>~~150,0~~<br>~~150,0~~<br>~~Densidad Húmeda~~<br>~~2,268~~<br>~~2,268~~<br>~~2,268~~<br>~~Contenido de Humedad~~<br>~~6,0~~<br>~~6,2~~<br>~~4,9~~<br>~~índice de Vacíos~~<br>~~0,239~~<br>~~0,241~~<br>~~0,225~~<br>~~Densidad Seca~~<br>~~2,139~~<br>~~2,136~~<br>~~2,163~~<br>~~Grado de Saturación~~<br>~~67,0~~<br>~~68,4~~<br>~~57,4~~<br>~~Saturación~~<br>~~Incrementos de Presión Aplicados~~<br>~~50~~<br>~~50~~<br>~~50~~<br>~~Diferencia de Presiones Usada~~<br>~~10~~<br>~~10~~<br>~~10~~<br>~~Presión de Poros al Completar~~<br>~~491~~<br>~~500~~<br>~~503~~<br>~~Presión de Celda al Completar~~<br>~~500~~<br>~~510~~<br>~~510~~<br>~~Valor B Alcanzado~~<br>~~0,95~~<br>~~0,98~~<br>~~0,96~~<br>~~Consolidación: Isotropica~~<br>~~Contrapresión~~<br>~~540,00~~<br>~~590,00~~<br>~~590,00~~<br>~~Presión de Celda~~<br>~~1140,00~~<br>~~890,00~~<br>~~690,00~~<br>~~Disipación de la Presión de Poros~~<br>~~53,33~~<br>~~-0,78~~<br>~~1,27~~<br>~~Presión de Poros al Completar~~<br>~~540,70~~<br>~~499,20~~<br>~~504,60~~<br>~~Presión de Celda Efectiva~~<br>~~600,00~~<br>~~300,00~~<br>~~100,00~~<br>~~Densidad Húmeda~~<br>~~2,38~~<br>~~2,37~~<br>~~2,37~~<br>~~Contenido de Humedad~~<br>~~7,52~~<br>~~7,74~~<br>~~7,70~~<br>~~índice de Vacíos~~<br>~~0,20~~<br>~~0,21~~<br>~~0,20~~<br>~~Densidad Seca~~<br>~~2,21~~<br>~~2,20~~<br>~~2,20~~<br>~~Deformación Volumétrica~~<br>~~3,20~~<br>~~2,88~~<br>~~1,73~~<br>~~Grado de Saturación~~<br>~~100~~<br>~~100~~<br>~~100~~<br>~~Procedimientos del Ensayo~~<br>~~Montaje de las Probetas~~<br>~~ASTM D7181 Sección 6-7~~<br>~~Saturación~~<br>~~ASTM D7181 Sección 8.2~~<br>~~Consolidación Isotropica~~<br>~~ASTM D7181 Sección 8.6~~<br>~~Notas:~~<br>~~Los procedimientos de prueba de Fugro están disponibles bajo petición~~<br>~~Corte~~<br>~~ASTM D7181 Sección 8.4~~<br>|
|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|
|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|
|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|
|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|
|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|
|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>||
|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|
|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 1 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 1 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 1 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 1 de 6|

|pción de la Muestra: ID Laboratorio: Resultados Corte Grava con arena y limos FCL1114sm4-6|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Corte~~<br><br><br><br>|~~Corte~~<br><br><br><br>|~~Corte~~<br><br><br><br>|~~Corte~~<br><br><br><br>|~~Corte~~<br><br><br><br>|
|~~N° Probeta~~|~~N° Probeta~~|~~Probeta 1~~|~~Probeta 2~~<br>|~~Probeta 3~~<br>|
|~~Presión de Poros Inicial~~<br>|kPa|~~542,90~~<br>|~~499,80~~<br>|~~500,40~~<br>|
|~~Presión Efectiva de Celda Inicial~~|kPa|~~597,10~~|~~390,20~~<br>|~~189,60~~<br>|
|~~Razón de Deformación~~|%/hr|~~0,08~~|~~0,08~~|~~0,08~~|

|Al Peak del Esfuerzo Desviador|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Esfuerzo Desviador Corregido~~<br>|~~kPa~~|~~1968,54~~<br>|~~1330,83~~<br>|~~599,44~~<br>|
|~~Corrección de Membranas Aplicada~~|kPa|~~0,91~~|~~0,90~~<br>|~~0,85~~<br>|
|~~Corrección de Drenajes Aplicado~~<br>|kPa|~~0~~<br>|~~0~~<br>|~~0~~<br>|
|~~Deformación Axial~~|%<br>|~~9,84~~|~~9,80~~<br>|~~9,06~~<br>|
|~~Deformación Volumétrica~~<br>|~~%~~<br>|~~1,94~~<br>|~~1,89~~<br>|~~1,79~~<br>|
|~~Esfuerzo Desviador Principal Mayor~~|~~kPa~~|~~2565,64~~|~~1721,03~~<br>|~~789,04~~<br>|
|~~Esfuerzo Desviador Principal Menor~~<br>|kPa|~~597,10~~<br>|~~390,20~~<br>|~~189,60~~<br>|
|~~Razón de Esfuerzo Desviador Principal~~|-|~~4,30~~|~~4,41~~<br>|~~4,16~~<br>|
|~~Epsilon 50 (e50)~~<br>|%<br>|~~1,49~~<br>|~~1,09~~<br>|~~1,09~~<br>|
|~~Módulo Secante (E50) al e50~~|~~kPa~~|~~66146,05~~|~~61099,26~~|~~27397,84~~|

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Esfuerzo Desviador Corregido~~<br>|kPa|~~1968,54~~<br>|~~1330,83~~<br>|~~599,44~~<br>|
|~~Corrección de Membranas Aplicada~~<br>|kPa|~~0,91~~<br>|~~0,90~~<br>|~~0,85~~<br>|
|~~Corrección de Drenajes Aplicado~~<br>|kPa|~~0~~<br>|~~0~~<br>|~~0~~<br>|
|~~Deformación Axial~~<br>|%<br>|~~9,84~~<br>|~~9,80~~<br>|~~9,06~~<br>|
|~~Deformación Volumétrica~~<br>|~~%~~|~~1,94~~<br>|~~1,89~~<br>|~~1,79~~<br>|
|~~Esfuerzo Desviador Principal Mayor~~|kPa|~~2565,64~~|~~1721,03~~<br>|~~789,04~~<br>|
|~~Esfuerzo Desviador Principal Menor~~<br>|kPa|~~597,10~~<br>|~~390,20~~<br>|~~189,60~~<br>|
|~~Razón de Esfuerzo Efectivo Principal~~|-|~~4,30~~|~~4,41~~|~~4,16~~|

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Esfuerzo Desviador Corregido~~|kPa<br>|~~1967,55~~|~~1333,82~~<br>|~~612,69~~<br>|
|~~Corrección de Membranas Aplicada~~<br>|~~kPa~~<br>|~~0,92~~<br>|~~0,92~~<br>|~~0,92~~<br>|
|~~Corrección de Drenajes Aplicado~~|~~kPa~~<br>|~~0,00~~|~~0,00~~<br>|~~0,00~~<br>|
|~~Deformación Axial~~<br>|~~%~~<br>|~~10,00~~<br>|~~10,00~~<br>|~~10,00~~<br>|
|~~Deformación Volumétrica~~|~~%~~<br>|~~1,93~~|~~1,89~~<br>|~~1,80~~<br>|
|~~Esfuerzo Desviador Principal Mayor~~<br>|~~kPa~~<br>|~~2565,28~~<br>|~~1720,88~~<br>|~~804,39~~<br>|
|~~Esfuerzo Desviador Principal Menor~~<br>|~~kPa~~<br>|~~597,73~~<br>|~~387,06~~<br>|~~191,69~~<br>|
|~~Razón de Esfuerzo Efectivo Princiapl~~|~~-~~|~~4,29~~|~~4,45~~|~~4,20~~|

|Condiciones Finales|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~Contenido de Humedad~~<br>|%<br>|~~2,44~~<br>|~~2,39~~<br>|~~2,37~~<br>|
|~~Densidad Húmeda~~|~~g/cm~~3<br>|~~2,44~~|~~2,39~~|~~2,37~~|
|~~Densidad Seca~~|~~g/cm~~3|~~2,38~~|~~2,34~~|~~2,32~~|

|INFORME DE ENSAYO DE LABORATORIO<br>Triaxial Consolidado Isotropicamente Drenado<br>Según: ASTM D7181-20|Col2|Col3|Col4|
|---|---|---|---|
|**Nombre Proyecto:**|Caracterización de material estéril del botadero Dalmacia<br>|**Código del Proyecto:**|232641|
|~~**Información de la Muestra**~~<br><br>|~~**Información de la Muestra**~~<br><br>|~~**Información de la Muestra**~~<br><br>|~~**Información de la Muestra**~~<br><br>|
|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br><br><br>~~-~~<br>~~-~~|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br><br><br>~~-~~<br>~~-~~|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br><br><br>~~-~~<br>~~-~~|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~**Identificación del pozo:**~~<br>~~-~~<br><br><br>~~-~~<br>~~-~~|
|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|
|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~|
|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|
|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|
|kPa<br>kPa<br>%/hr<br>~~kPa~~<br>kPa<br>kPa<br>%<br>~~%~~<br>~~kPa~~<br>kPa<br>-<br>%<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>%<br>~~%~~<br>kPa<br>kPa<br>-<br>kPa<br>~~kPa~~<br>~~kPa~~<br>~~%~~<br>~~%~~<br>~~kPa~~<br>~~kPa~~<br>~~-~~<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>~~Corte~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Presión de Poros Inicial~~<br>~~542,90~~<br>~~499,80~~<br>~~500,40~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~390,20~~<br>~~189,60~~<br>~~Razón de Deformación~~<br>~~0,08~~<br>~~0,08~~<br>~~0,08~~<br>~~Presión Efectiva de Celda Inicial~~<br>~~597,10~~<br>~~Al Peak del Esfuerzo Desviador~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Epsilon 50 (e50)~~<br>~~1,49~~<br>~~1,09~~<br>~~1,09~~<br>~~Razón de Esfuerzo Desviador Principal~~<br>~~4,30~~<br>~~Módulo Secante (E50) al e50~~<br>~~66146,05~~<br>~~61099,26~~<br>~~27397,84~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Razón de Esfuerzo Efectivo Principal~~<br>~~4,30~~<br>~~1333,82~~<br>~~612,69~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,92~~<br>~~0,92~~<br>~~0,92~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1967,55~~<br>~~0,00~~<br>~~0,00~~<br>~~Deformación Axial~~<br>~~10,00~~<br>~~10,00~~<br>~~10,00~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0,00~~<br>~~1,89~~<br>~~1,80~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,28~~<br>~~1720,88~~<br>~~804,39~~<br>~~Deformación Volumétrica~~<br>~~1,93~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,73~~<br>~~387,06~~<br>~~191,69~~<br>~~Razón de Esfuerzo Efectivo Princiapl~~<br>~~4,29~~<br>~~4,45~~<br>~~4,20~~<br>~~Condiciones Finales~~<br>~~Contenido de Humedad~~<br>~~2,44~~<br>~~2,39~~<br>~~Densidad Seca~~<br>~~2,38~~<br>~~2,34~~<br>~~2,32~~<br>~~2,37~~<br>~~Densidad Húmeda~~<br>~~2,44~~<br>~~2,39~~<br>~~2,37~~<br>|kPa<br>kPa<br>%/hr<br>~~kPa~~<br>kPa<br>kPa<br>%<br>~~%~~<br>~~kPa~~<br>kPa<br>-<br>%<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>%<br>~~%~~<br>kPa<br>kPa<br>-<br>kPa<br>~~kPa~~<br>~~kPa~~<br>~~%~~<br>~~%~~<br>~~kPa~~<br>~~kPa~~<br>~~-~~<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>~~Corte~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Presión de Poros Inicial~~<br>~~542,90~~<br>~~499,80~~<br>~~500,40~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~390,20~~<br>~~189,60~~<br>~~Razón de Deformación~~<br>~~0,08~~<br>~~0,08~~<br>~~0,08~~<br>~~Presión Efectiva de Celda Inicial~~<br>~~597,10~~<br>~~Al Peak del Esfuerzo Desviador~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Epsilon 50 (e50)~~<br>~~1,49~~<br>~~1,09~~<br>~~1,09~~<br>~~Razón de Esfuerzo Desviador Principal~~<br>~~4,30~~<br>~~Módulo Secante (E50) al e50~~<br>~~66146,05~~<br>~~61099,26~~<br>~~27397,84~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Razón de Esfuerzo Efectivo Principal~~<br>~~4,30~~<br>~~1333,82~~<br>~~612,69~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,92~~<br>~~0,92~~<br>~~0,92~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1967,55~~<br>~~0,00~~<br>~~0,00~~<br>~~Deformación Axial~~<br>~~10,00~~<br>~~10,00~~<br>~~10,00~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0,00~~<br>~~1,89~~<br>~~1,80~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,28~~<br>~~1720,88~~<br>~~804,39~~<br>~~Deformación Volumétrica~~<br>~~1,93~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,73~~<br>~~387,06~~<br>~~191,69~~<br>~~Razón de Esfuerzo Efectivo Princiapl~~<br>~~4,29~~<br>~~4,45~~<br>~~4,20~~<br>~~Condiciones Finales~~<br>~~Contenido de Humedad~~<br>~~2,44~~<br>~~2,39~~<br>~~Densidad Seca~~<br>~~2,38~~<br>~~2,34~~<br>~~2,32~~<br>~~2,37~~<br>~~Densidad Húmeda~~<br>~~2,44~~<br>~~2,39~~<br>~~2,37~~<br>|kPa<br>kPa<br>%/hr<br>~~kPa~~<br>kPa<br>kPa<br>%<br>~~%~~<br>~~kPa~~<br>kPa<br>-<br>%<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>%<br>~~%~~<br>kPa<br>kPa<br>-<br>kPa<br>~~kPa~~<br>~~kPa~~<br>~~%~~<br>~~%~~<br>~~kPa~~<br>~~kPa~~<br>~~-~~<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>~~Corte~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Presión de Poros Inicial~~<br>~~542,90~~<br>~~499,80~~<br>~~500,40~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~390,20~~<br>~~189,60~~<br>~~Razón de Deformación~~<br>~~0,08~~<br>~~0,08~~<br>~~0,08~~<br>~~Presión Efectiva de Celda Inicial~~<br>~~597,10~~<br>~~Al Peak del Esfuerzo Desviador~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Epsilon 50 (e50)~~<br>~~1,49~~<br>~~1,09~~<br>~~1,09~~<br>~~Razón de Esfuerzo Desviador Principal~~<br>~~4,30~~<br>~~Módulo Secante (E50) al e50~~<br>~~66146,05~~<br>~~61099,26~~<br>~~27397,84~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Razón de Esfuerzo Efectivo Principal~~<br>~~4,30~~<br>~~1333,82~~<br>~~612,69~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,92~~<br>~~0,92~~<br>~~0,92~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1967,55~~<br>~~0,00~~<br>~~0,00~~<br>~~Deformación Axial~~<br>~~10,00~~<br>~~10,00~~<br>~~10,00~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0,00~~<br>~~1,89~~<br>~~1,80~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,28~~<br>~~1720,88~~<br>~~804,39~~<br>~~Deformación Volumétrica~~<br>~~1,93~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,73~~<br>~~387,06~~<br>~~191,69~~<br>~~Razón de Esfuerzo Efectivo Princiapl~~<br>~~4,29~~<br>~~4,45~~<br>~~4,20~~<br>~~Condiciones Finales~~<br>~~Contenido de Humedad~~<br>~~2,44~~<br>~~2,39~~<br>~~Densidad Seca~~<br>~~2,38~~<br>~~2,34~~<br>~~2,32~~<br>~~2,37~~<br>~~Densidad Húmeda~~<br>~~2,44~~<br>~~2,39~~<br>~~2,37~~<br>|kPa<br>kPa<br>%/hr<br>~~kPa~~<br>kPa<br>kPa<br>%<br>~~%~~<br>~~kPa~~<br>kPa<br>-<br>%<br>~~kPa~~<br>kPa<br>kPa<br>kPa<br>%<br>~~%~~<br>kPa<br>kPa<br>-<br>kPa<br>~~kPa~~<br>~~kPa~~<br>~~%~~<br>~~%~~<br>~~kPa~~<br>~~kPa~~<br>~~-~~<br>%<br>~~g/cm~~3<br>~~g/cm~~3<br>~~Corte~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>~~Presión de Poros Inicial~~<br>~~542,90~~<br>~~499,80~~<br>~~500,40~~<br>~~N° Probeta~~<br>~~Probeta 1~~<br>~~390,20~~<br>~~189,60~~<br>~~Razón de Deformación~~<br>~~0,08~~<br>~~0,08~~<br>~~0,08~~<br>~~Presión Efectiva de Celda Inicial~~<br>~~597,10~~<br>~~Al Peak del Esfuerzo Desviador~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Epsilon 50 (e50)~~<br>~~1,49~~<br>~~1,09~~<br>~~1,09~~<br>~~Razón de Esfuerzo Desviador Principal~~<br>~~4,30~~<br>~~Módulo Secante (E50) al e50~~<br>~~66146,05~~<br>~~61099,26~~<br>~~27397,84~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1968,54~~<br>~~1330,83~~<br>~~599,44~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,91~~<br>~~0,90~~<br>~~0,85~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0~~<br>~~0~~<br>~~0~~<br>~~Deformación Axial~~<br>~~9,84~~<br>~~9,80~~<br>~~9,06~~<br>~~Deformación Volumétrica~~<br>~~1,94~~<br>~~1,89~~<br>~~1,79~~<br>~~1721,03~~<br>~~789,04~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,10~~<br>~~390,20~~<br>~~189,60~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,64~~<br>~~4,41~~<br>~~4,16~~<br>~~Razón de Esfuerzo Efectivo Principal~~<br>~~4,30~~<br>~~1333,82~~<br>~~612,69~~<br>~~Corrección de Membranas Aplicada~~<br>~~0,92~~<br>~~0,92~~<br>~~0,92~~<br>~~Esfuerzo Desviador Corregido~~<br>~~1967,55~~<br>~~0,00~~<br>~~0,00~~<br>~~Deformación Axial~~<br>~~10,00~~<br>~~10,00~~<br>~~10,00~~<br>~~Corrección de Drenajes Aplicado~~<br>~~0,00~~<br>~~1,89~~<br>~~1,80~~<br>~~Esfuerzo Desviador Principal Mayor~~<br>~~2565,28~~<br>~~1720,88~~<br>~~804,39~~<br>~~Deformación Volumétrica~~<br>~~1,93~~<br>~~Esfuerzo Desviador Principal Menor~~<br>~~597,73~~<br>~~387,06~~<br>~~191,69~~<br>~~Razón de Esfuerzo Efectivo Princiapl~~<br>~~4,29~~<br>~~4,45~~<br>~~4,20~~<br>~~Condiciones Finales~~<br>~~Contenido de Humedad~~<br>~~2,44~~<br>~~2,39~~<br>~~Densidad Seca~~<br>~~2,38~~<br>~~2,34~~<br>~~2,32~~<br>~~2,37~~<br>~~Densidad Húmeda~~<br>~~2,44~~<br>~~2,39~~<br>~~2,37~~<br>|
|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|
|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|
|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~|
|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|
|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|
|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>||
|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|
|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 2 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 2 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 2 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 2 de 6|

|INFORME DE ENSAYO DE LABORATORIO<br>Triaxial Consolidado Isotropicamente Drenado<br>Según: ASTM D7181-20|Col2|Col3|Col4|
|---|---|---|---|
|**Nombre Proyecto:**|Caracterización de material estéril del botadero Dalmacia<br>|**Código del Proyecto:**|232641|
|~~**Información de la Muestra**~~<br><br>|~~**Información de la Muestra**~~<br><br>|~~**Información de la Muestra**~~<br><br>|~~**Información de la Muestra**~~<br><br>|
|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~|~~**Profundidad de la Muestra [m]:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~|
|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br>~~**Identificación de la muestra:**~~<br>~~FCL1114sm4-6~~<br><br><br>|
|~~**Tipo de muestra:**~~<br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~<br><br>|~~**Tipo de muestra:**~~<br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~<br><br>|~~**Tipo de muestra:**~~<br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~<br><br>|~~**Tipo de muestra:**~~<br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~LB~~<br><br>|
|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br><br>~~Grava con arena y limos~~<br>~~FCL1114sm4-6~~|
|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|
|~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>|~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>|~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>|~~Probeta 1~~<br>~~Probeta 2~~<br>~~Probeta 3~~<br>|
|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|
|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|
|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~<br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~<br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~<br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br>~~14-03-2023~~<br>~~05-04-2023~~<br>~~03-04-2023~~<br>~~PR~~<br>|
|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~05-04-2023~~<br>~~05-04-2023~~<br>~~ACH~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~05-04-2023~~<br>~~05-04-2023~~<br>~~ACH~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~05-04-2023~~<br>~~05-04-2023~~<br>~~ACH~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br>~~05-04-2023~~<br>~~05-04-2023~~<br>~~ACH~~|
|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|
|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>||
|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a~~<br>la muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|
|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 3 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 3 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 3 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 3 de 6|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
|||||||Probeta 1|
|||||||Probeta 2<br>Probeta 3|
||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Probeta 1|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||Probeta 1<br>|Probeta 1<br>|
|||||||||Probeta 2<br>Probeta 3||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||

|INFORME DE ENSAYO DE LABORATORIO<br>Triaxial Consolidado Isotropicamente Drenado<br>Según: ASTM D7181-20|Col2|Col3|Col4|
|---|---|---|---|
|**Nombre Proyecto:**|Ensayos Triaxiales Botadero Dalmacia<br>|**Código del Proyecto:**|232641|
|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|
|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|
|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|
|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|
|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|
|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|
|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>3<br>3,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>Deformación Volumétrica (%)<br>Tiempo (Raiz Cuadrada)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>Presión de Poros (kPa)<br>Presión de Celda (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>**Consolidación**<br>**Saturación**|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>3<br>3,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>Deformación Volumétrica (%)<br>Tiempo (Raiz Cuadrada)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>Presión de Poros (kPa)<br>Presión de Celda (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>**Consolidación**<br>**Saturación**|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>3<br>3,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>Deformación Volumétrica (%)<br>Tiempo (Raiz Cuadrada)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>Presión de Poros (kPa)<br>Presión de Celda (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>**Consolidación**<br>**Saturación**|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>3<br>3,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>Deformación Volumétrica (%)<br>Tiempo (Raiz Cuadrada)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>Presión de Poros (kPa)<br>Presión de Celda (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>**Consolidación**<br>**Saturación**|
|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|
|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~Minera BMR SpA.~~<br>~~byron.zambrano@altospunita~~<br><br><br><br>|
|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|
|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|
|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|
|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>||
|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|
|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 4 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 4 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 4 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 4 de 6|

|Probeta 1<br>Probeta 2<br>Probeta 3|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|Probeta 1<br>Probeta 2<br>Probeta 3|
||||||||||
||||||||||
||||||||||
||||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|beta 1<br>beta 2|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||Pro<br>Pro<br>|beta 1<br>beta 2<br>|
||||||||||Pro|beta 3|
||||||||||||
||||||||||||
||||||||||||
||||||||||||

|INFORME DE ENSAYO DE LABORATORIO<br>Triaxial Consolidado Isotropicamente Drenado<br>Según: ASTM D7181-20|Col2|Col3|Col4|
|---|---|---|---|
|**Nombre Proyecto:**|Ensayos Triaxiales Botadero Dalmacia<br>|**Código del Proyecto:**|232641|
|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|~~**Información de la Muestra**~~|
|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|
|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|~~**Muestreado por:**~~<br>~~Cliente~~<br><br>~~**Identificación de la muestra:**~~<br>~~-~~<br><br><br>|
|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|
|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|
|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|
|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Deformación Volumétrica (%)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Esfuerzo Desviador (kPa)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Deformación Volumétrica (%)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Esfuerzo Desviador (kPa)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Deformación Volumétrica (%)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Esfuerzo Desviador (kPa)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3|0<br>0,5<br>1<br>1,5<br>2<br>2,5<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Deformación Volumétrica (%)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>Esfuerzo Desviador (kPa)<br>Deformación Axial (%)<br>Probeta 1<br>Probeta 2<br>Probeta 3|
|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|
|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~|
|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~<br><br><br>|
|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|
|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|~~**Observaciones:**~~<br>|
|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>||
|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|
|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 5 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 5 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 5 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 5 de 6|

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||Probeta 1<br>Probeta 2|
|||||||Probeta 3|
||||||||
||||||||
||||||||
||||||||
||||||||

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
||||||||Probeta 1|
||||||||Probeta 1|
||||||||Probeta 2<br>Probeta 3|

|INFORME DE ENSAYO DE LABORATORIO<br>Triaxial Consolidado Isotropicamente Drenado<br>Según: ASTM D7181-20|Col2|Col3|Col4|
|---|---|---|---|
|**Nombre Proyecto:**|Ensayos Triaxiales Botadero Dalmacia<br>|**Código del Proyecto:**|232641|
|~~**Información de la Muestra**~~<br><br><br><br>|~~**Información de la Muestra**~~<br><br><br><br>|~~**Información de la Muestra**~~<br><br><br><br>|~~**Información de la Muestra**~~<br><br><br><br>|
|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|**Profundidad de la Muestra [m]:**<br>-<br><br><br>~~**Identificación del pozo:**~~<br>~~-~~<br>~~-~~<br>~~-~~<br><br>|
|~~**Muestreado por:**~~<br>~~Cliente~~<br><br><br><br><br>~~**Identificación de la muestra:**~~<br>~~-~~|~~**Muestreado por:**~~<br>~~Cliente~~<br><br><br><br><br>~~**Identificación de la muestra:**~~<br>~~-~~|~~**Muestreado por:**~~<br>~~Cliente~~<br><br><br><br><br>~~**Identificación de la muestra:**~~<br>~~-~~|~~**Muestreado por:**~~<br>~~Cliente~~<br><br><br><br><br>~~**Identificación de la muestra:**~~<br>~~-~~|
|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|~~**Tipo de muestra:**~~<br><br><br>~~**Fecha del muestreo:**~~<br>~~-~~<br>~~B~~<br><br>|
|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|~~**Descripción de la Muestra:**~~<br>~~**ID Laboratorio:**~~<br>~~Gravas con arena y limos~~<br>~~FCL1114sm4-6~~<br>|
|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|~~**Resultados**~~|
|0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>3000<br>t,1⁄2(σv-σr) (kPa)<br>Esfuerzo Efectivo (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>q, (σv-σr) (kPa)<br>p', (σv' - 2σr')' / 3 (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3|0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>3000<br>t,1⁄2(σv-σr) (kPa)<br>Esfuerzo Efectivo (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>q, (σv-σr) (kPa)<br>p', (σv' - 2σr')' / 3 (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3|0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>3000<br>t,1⁄2(σv-σr) (kPa)<br>Esfuerzo Efectivo (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>q, (σv-σr) (kPa)<br>p', (σv' - 2σr')' / 3 (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3|0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>3000<br>t,1⁄2(σv-σr) (kPa)<br>Esfuerzo Efectivo (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>q, (σv-σr) (kPa)<br>p', (σv' - 2σr')' / 3 (kPa)<br>Probeta 1<br>Probeta 2<br>Probeta 3|
|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|~~**Información del Reporte**~~<br><br><br>|
|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|~~**Solicitante:**~~<br>~~-~~<br>~~**Empresa:**~~<br><br><br><br><br>~~Byron Zambrano~~<br>~~byron.zambrano@altospunitaqui.cl~~<br>~~Minera BMR SpA.~~<br><br><br><br>|
|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~|~~**Fecha Recepción:**~~<br>~~**Fecha Inicio Ensayo:**~~<br>~~**Fecha Término:**~~<br>~~**Realizado Por:**~~<br><br><br><br><br><br><br><br><br>~~14-03-2023~~<br>~~29-03-2023~~<br>~~03-04-2023~~<br>~~PR~~|
|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|~~**Autorizado Por:**~~<br>~~**Fecha Autorización:**~~<br>~~**Fecha Reporte:**~~<br>~~**Revisión:**~~<br>~~00~~<br><br>~~ACH~~<br>~~05-04-2023~~<br>~~05-04-2023~~|
|~~**Observaciones:**~~<br>c'= 00kPa<br>f'= 38°<br>|~~**Observaciones:**~~<br>c'= 00kPa<br>f'= 38°<br>|~~**Observaciones:**~~<br>c'= 00kPa<br>f'= 38°<br>|~~**Observaciones:**~~<br>c'= 00kPa<br>f'= 38°<br>|
|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>|~~Fugro Chile S.A., Avenida Departamental 1292, San Miguel, Santiago, Chile~~<br>||
|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|~~El ensayo fue realizado en el laboratorio de Fugro Chile S.A. en la dirección indicada arriba. Los resultados son aplicables solo a la~~<br>muestra ensayada. El laboratorio no emite opiniones o interpretaciones de los resultados indicados. A menos que se haya<br>indicado lo contrario, la muestra fue ensayada en la condición en la cual fue recibida por el laboratorio.|
|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 6 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 6 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 6 de 6|FCSA-LAN-LAB-FO-I-001 | Formato Reporte Triaxial CID | Edición [00] Rev [00]<br>Página 6 de 6|

## ANEXO B ANÁLISIS DE ESTABILIDAD REALIZADO MEDIANTE SOFTWARE SLIDE

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.1.** Condición Estática, Sección A-A’ Global, Botadero Dalmacia.

**Figura B.2.** Condición Sismo Operacional, Sección A-A’ Global, Botadero

Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.3.** Condición Sismo Máximo Creíble, Sección A-A’ Global, Botadero

Dalmacia.

**Figura B.4.** Condición Estática, Sección A-A’ Talud 1 (T-1), Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.5.** Condición Sismo Operacional, Sección A-A’ Talud 1 (T-1), Botadero

Dalmacia.

**Figura B.6.** Condición Sismo Máximo Creíble, Sección A-A’ Talud 1 (T-1),

Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.7.** Condición Estática, Sección A-A’ Talud 2 (T-2), Botadero Dalmacia.

**Figura B.8.** Condición Sismo Operacional, Sección A-A’ Talud 2 (T-2), Botadero

Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.9.** Condición Sismo Máximo Creíble, Sección A-A’ Talud 2 (T-2),

Botadero Dalmacia.

**Figura B.10.** Condición Estática, Sección A-A’ Talud 3 (T-3), Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.11.** Condición Sismo Operacional, Sección A-A’ Talud 3 (T-3), Botadero

Dalmacia.

**Figura B.12.** Condición Sismo Máximo Creíble, Sección A-A’ Talud 3 (T-3),

Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.13.** Condición Estática, Sección A-A’ Talud 4 (T-4), Botadero Dalmacia.

**Figura B.14.** Condición Sismo Operacional, Sección A-A’ Talud 4 (T-4), Botadero

Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.15.** Condición Sismo Máximo Creíble, Sección A-A’ Talud 4 (T-4),

Botadero Dalmacia.

**Figura B.16.** Condición Estática, Sección A-A’ Talud 5 (T-5), Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.17.** Condición Sismo Operacional, Sección A-A’ Talud 5 (T-5), Botadero

Dalmacia.

**Figura B.18.** Condición Sismo Máximo Creíble, Sección A-A’ Talud 5 (T-5),

Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.19.** Condición Estática, Sección A-A’ Talud 6 (T-6), Botadero Dalmacia.

**Figura B.20.** Condición Sismo Operacional, Sección A-A’ Talud 6 (T-6), Botadero

Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.21.** Condición Sismo Máximo Creíble, Sección A-A’ Talud 6 (T-6),

Botadero Dalmacia.

**Figura B.22.** Condición Estática, Sección A-A’ Talud 7 (T-7), Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

**Figura B.23.** Condición Sismo Operacional, Sección A-A’ Talud 7 (T-7), Botadero

Dalmacia.

**Figura B.24.** Condición Sismo Máximo Creíble, Sección A-A’ Talud 7 (T-7),

Botadero Dalmacia.

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

## ANEXO C INFORME DE MECÁNICA DE SUELOS Y ENSAYOS IDIEM

Plaza de La Justicia No 45, Oficinas 301-302 - Valparaíso, Chile
Teléfonos: (+56) (32) 2597809 - 2595116; www.ffgeomechanics.com

## ANEXO A Informe Mecánica de Suelos

# MINERA ALTOS DE PUNITAQUI

#### INFORME

**MECANICA DE SUELOS**

**BOTADERO PROYECTO DALMACIA**

Solicitado Por:

**INGEROC**
Ingeniería de Rocas Ltda.
Rosario Sur 91 Oficinas 802 - 803 - Las Condes

Fono : 2202 15 02 - 2201 45 04

e - mail : ingeroc@ingeroc.com

Preparado Por:

**RODRIGUEZ Y GOLDSACK**

Ingenieros Civiles Ltda.
Presidente Riesco 3074 Depto. 32 - Las Condes

Fono - Fax: 237 871 93
e - mail : rodygold@123.cl

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

**INDICE**

**INFORME**

**MECANICA DE SUELOS**

**BOTADERO PROYECTO DALMACIA**

**MINERA ALTOS DE PUNITAQUI**

1.-GENERALIDADES y OBJETIVOS ............................................................................. 1

2.-ANTECEDENTES ........................................................................................................ 2

2.1 Ubicación del sitio................................................................................................ 2

2.2 Topografía............................................................................................................ 2

2.3 Geología............................................................................................................... 3

2.4 Exploración .......................................................................................................... 3

2.5 Napa Freática ....................................................................................................... 7

2.6 Fotografías ........................................................................................................... 8

2.7 Ensayos de Laboratorio ........................................................................................ 8

2.8 Características del botadero .................................................................................. 9

2.9 Precipitaciones en el sector ................................................................................... 9

3.-CONCLUSIONES Y RECOMENDACIONES............................................................ 10

3.1 Características geomorfológicas del área ............................................................ 10

3.2 Características geomecánicas de los suelos existentes en los sitios donde se

implantarán los botaderos ................................................................................... 10

3.3 Clasificación de los suelos existentes en los sitio según la norma NCh 2369 of.

2003 ................................................................................................................... 13

3.4 Profundidad de la napa freática........................................................................... 13

3.5 Tratamiento del suelo existente a nivel de sello de fundación del botadero ......... 13

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

3.6 Recomendaciones para el Relleno del Botadero .................................................. 14

3.7 Caudal de agua a controlar en el botadero ........................................................... 15

3.8 Saneamiento hidráulico a considerar en el botadero ............................................ 15

3.9 Exploración complementaria .............................................................................. 17

4.-ARCHIVO DIGITAL .................................................................................................. 17

ANEXO No 1 Figuras

ANEXO N° 2 Plano Topografía

ANEXO No 3 Fotografías

ANEXO No 4 Ensayos de Laboratorio

ANEXO No 5 Archivo Digital

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

1 de 17

**INFORME**

**MECANICA DE SUELOS**

**BOTADERO PROYECTO DALMACIA**

**MINERA ALTOS DE PUNITAQUI**

**1.-** **GENERALIDADES y OBJETIVOS**

Ingeroc Ingeniería de Rocas Ltda, a través de su ingeniero señor Juan Alvarado K.

ha solicitado a Rodríguez y Goldsack Ingenieros Civiles Ltda., el informe de

Mecánica de Suelos necesario para desarrollar el proyecto de ingeniería básica de

un botadero para el Proyecto Dalmacia de propiedad de la minera Altos de

Punitaqui.

El objetivo de este informe es entregar los siguientes antecedentes geotécnicos para

cumplir con lo solicitado.

 Características geomorfológicas del área.

 Características geomecánicas de los suelos existentes en el sitio donde se

implantará el botadero.

 Clasificación de los suelos existentes en el sitio según la norma NCh 2369

of. 2003

 Profundidad de la napa freática.

 - Tratamiento del suelo existente a nivel de sello de fundación del botadero.

 Recomendaciones para el relleno del botadero.

 Caudales de agua a controlar en el botadero.

 - Saneamiento hidráulico a considerar en el botadero.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

2 de 17

**2.-** **ANTECEDENTES**

Los antecedentes, en los cuales se basan las conclusiones y recomendaciones

geotécnicas que se entregan, son los que siguen:

**2.1** **Ubicación del sitio**

El sitio está ubicado a ~35,00 km al Sur de la ciudad de Ovalle, en la IV

Región, ~500 m al Poniente de la ruta N° D-673 y a ~8,00 km al Sur

Poniente de la localidad de Punitaqui.

En el Anexo No 1 se adjunta la Figura No 1 en la que se muestra la ubicación

del Botadero Dalmacia a nivel Regional.

**2.2** **Topografía**

Para el desarrollo de este informe se ha dispuesto de la Plancheta del

Instituto Geográfico Militar escala 1:50.000 que muestra la geomorfología

general del área donde se ubica el botadero y de un levantamiento

topográfico a escala 1:1.000 con curvas de nivel cada 1,00 m del área del

botadero.

En el Anexo N° 1 se adjunta la Figura No 2 que muestra el citado

levantamiento en escala 1:50.000 y el Anexo N° 2 se adjunta el citado

levantamiento topográfico.

En el Anexo N° 1 se adjunta las Figuras N° 3 a N° 6 que muestran la

ubicación y la morfología del área donde se implantará el botadero en

estudio, en fotografías aéreas a diferentes escalas tomadas de Google Earth.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

3 de 17

En el Anexo N° 1 se adjunta la Figura N° 7 y N° 8 que muestran los

principales cauces de las quebradas existentes en el área de implantación del

botadero.

El sitio en donde se implantará el botadero corresponde a cuatro quebradas

que confluyen primero en dos quebradas y después en una quebrada de

mayor tamaño en el tercio inferior respecto del área de implantación del

botadero, éstas quebradas se ubican en la ladera Norte del cordón montañoso

formado por el cerro Guayacán y por el cerro El Peñón, el botadero está

confinado por el Norte por la quebrada El Peral.

La pendiente general de las quebradas afluentes es de un 20% y de la

quebrada de mayor tamaño aguas abajo es de un 15% y las laderas que las

confinan tiene una pendiente promedio de ~40% y con pendientes máximas

de hasta 45%.

**2.3** **Geología**

En el Anexo No 1 se adjunta la Figura No 9 que muestra la geología del

sector, desarrollada por el Sernageomín, a escala 1:100.000.

Como se puede observar, el sitio se implanta en laderas formadas por roca

intrusiva diorítica compuesta por monzodioritas cuarcíferas de anfíbola

piroxeno y de piroxeno biotita.

**2.4** **Exploración**

Con el objeto de precisar las características de los suelos existentes en el

sitio donde se implantará el botadero, se hizo una exploración a base de 4

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

4 de 17

calicatas, las que fueron registradas por el ingeniero Andrés Alvarado P. el

día 19 de Febrero de 2014.

En la Figura No 5 y N° 6 adjunta en Anexo No 1 se muestra la ubicación de

las citadas calicatas.

Los antecedentes entregados por las calicatas son los que siguen:

**-** **Estratigrafía**

 - **Calicata No 1**

**N: 6.578.939;** **E: 283.588** **WGS84**

**N: 6.579.279;** **E: 283.770 PSAD56**

Profundidad

(m)

0,00 ÷ 0,50

Estrato 1

0,50 ÷ 1,10

Estrato 2

Descripción

Suelo fino residual con color café, de consistencia

media, de plasticidad media, con un contenido de

humedad menor al límite plástico, con bloques de

canto angular aislados de tamaño máximo 6 ”, de

estructura heterogénea, de compresibilidad media a

baja y con materia orgánica en los primeros 30 cm.

Fragmentos dispersos de roca fracturada a

meteorizada inmersa en una matriz de suelo fino

residual con color café, de consistencia firme, de

plasticidad media a alta, con un contenido de

humedad menor al límite plástico, de estructura

heterogénea, de compresibilidad baja y libre de

materia orgánica.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

1,10 ÷ 2,70

Estrato 3

5 de 17

Roca altamente fracturada y meteorizada, en

bloques de canto angular de tamaño máximo 10 ” y

en una matriz de suelo fino residual.

- **Calicata No 2**

**N: 6.578.844;** **E: 283.606** **WGS84**

**N: 6.579.185;** **E: 283.786 PSAD56**

Profundidad

(m)

0,00 ÷ 0,80

Estrato 1

0,80 ÷ 1,40

Estrato 2

1,40 ÷ 3,50

Estrato 3

Descripción

Suelo fino residual con color café, de consistencia

media, de plasticidad media, con un contenido de

humedad menor al límite plástico, con bloques de

canto angular aislados de tamaño máximo 6 ”, de

estructura heterogénea, de compresibilidad media a

baja y con materia orgánica en los primeros 30 cm.

Fragmentos dispersos de roca fracturada a

meteorizada inmersa en una matriz de suelo fino

residual con color café, de consistencia firme, de

plasticidad media a alta, con un contenido de

humedad menor al límite plástico, de estructura

heterogénea, de compresibilidad baja y libre de

materia orgánica.

Roca altamente fracturada y meteorizada, en

bloques de canto angular de tamaño máximo 10 ” y

en una matriz de suelo fino residual.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

6 de 17

- **Calicata No 3**

**N: 6.578.786;** **E: 283.616** **WGS84**

**N: 6.579.126;** **E: 283.795 PSAD56**

Profundidad

(m)

0,00 ÷ 1,10

Estrato 1

1,10 ÷ 1,60

Estrato 2

1,60 ÷ 3,30

Estrato 3

Descripción

Suelo fino residual con color café, de consistencia

media, de plasticidad media, con un contenido de

humedad menor al límite plástico, con bloques de

canto angular aislados de tamaño máximo 6 ”, de

estructura heterogénea, de compresibilidad media a

baja y con materia orgánica en los primeros 30 cm.

Fragmentos dispersos de roca fracturada a

meteorizada inmersa en una matriz de suelo fino

residual con color café, de consistencia firme, de

plasticidad media a alta, con un contenido de

humedad menor al límite plástico, de estructura

heterogénea, de compresibilidad baja y libre de

materia orgánica.

Roca altamente fracturada y meteorizada, en

bloques de canto angular de tamaño máximo 10 ” y

en una matriz de suelo fino residual.

 - **Calicata No 4**

**N: 6.578.743;** **E: 283.617** **WGS84**

**N: 6.579.083;** **E: 283.797 PSAD56**

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

Profundidad

(m)

0,00 ÷ 0,50

Estrato 1

0,50 ÷ 1,50

Estrato 2

1,50 ÷ 3,00

Estrato 3

**2.5** **Napa Freática**

7 de 17

Descripción

Suelo fino residual con color café, de consistencia

media, de plasticidad media, con un contenido de

humedad menor al límite plástico, con bloques de

canto angular aislados de tamaño máximo 6 ”, de

estructura heterogénea, de compresibilidad media a

baja y con materia orgánica en los primeros 30 cm.

Fragmentos dispersos de roca fracturada a

meteorizada inmersa en una matriz de suelo fino

residual con color café, de consistencia firme, de

plasticidad media a alta, con un contenido de

humedad menor al límite plástico, de estructura

heterogénea, de compresibilidad baja y libre de

materia orgánica.

Roca altamente fracturada y meteorizada, en

bloques de canto angular de tamaño máximo 10 ” y

en una matriz de suelo fino residual.

No se detectó la napa durante el registro de las calicatas el día 19 de Febrero

de 2014.

Todos los antecedentes indican que no existe napa hasta varías decenas de

metros de profundidad, sin embargo se debe considerar el aporte de aguas

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

8 de 17

lluvia de las cuencas menores a la quebrada principal y las aguas lluvias que

escurrirán sobre el área de implantación del botadero.

**2.6** **Fotografías**

En el Anexo No 3 se adjunta un conjunto de fotografías que muestra las

características del sitio y las de los suelos existentes en él.

**2.7** **Ensayos de Laboratorio**

De las Calicatas No 1, N° 2, N° 3 y N° 4 se tomaron muestras perturbadas de

los suelos y se llevaron a IDIEM para que se le hiciera ensayos de

clasificación completa.

Los resultados de los ensayos hechos a las muestras obtenidas se entregan en

el Informe de Ensayo No 888.707-A emitido por Idiem el 19 de Marzo de

2014, copia del cual se adjunta en el Anexo N° 4.

Los resultados de los ensayos se pueden resumir como sigue:

|Granulometría|Col2|C - 1<br>0,50|C - 2<br>0,80|C - 3<br>1,60 m|C - 4<br>0,50 m|
|---|---|---|---|---|---|
|Tamaño de<br>la partícula<br>(mm)|Malla|% de<br>Peso que<br>Pasa|% de<br>Peso que<br>Pasa|% de<br>Peso que<br>Pasa|% de<br>Peso que<br>Pasa|
|63,50|2 1⁄2”|-|-|100,0|-|
|50,80|2”|100,0|-|96,3|-|
|38,10|1 1⁄2”|98,6|100,0|96,3|100,0|
|25,40|1”|95,3|99,8|95,9|99,2|
|19,00|3/4”|93,1|99,0|95,4|98,2|
|9,52|3/8”|89,4|97,5|94,3|96,6|

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

9 de 17

|4,760|# 4|84,6|93,8|93,3|93,5|
|---|---|---|---|---|---|
|2,000|# 10|78,0|88,6|91,4|90,4|
|0,840|# 20|72,5|83,7|89,4|86,5|
|0,420|# 40|66,1|80,3|86,7|83,1|
|0,250|# 60|60,8|77,0|83,8|79,9|
|0,106|#140|52,4|71,3|78,2|73,4|
|0,074|#200|49,1|69,2|75,9|70,5|
|||||||
|Límites de<br>Atterberg|LL|24|40|45|39|
|Límites de<br>Atterberg|LP|17|21|25|13|
|Límites de<br>Atterberg|IP|7|19|20|26|
|Peso<br>Específico|Gs|2,82|2,80|2,78|2,83|
|Clasificación USCS|Clasificación USCS|SC-SM|CL|CL|CL|

**2.8** **Características del botadero**

El botadero se formará llenando las quebradas existentes en el área por lo

que quedará confinado por las laderas adyacentes a éstas, dejando sin

confinamiento sólo la cara hacia aguas abajo de la quebrada.

La cuenca de la quebrada que aporta agua al botadero tendrá un área de

~1,10 km [2] .

**2.9** **Precipitaciones en el sector**

De acuerdo a antecedentes de precipitaciones anteriores en la zona para esta

etapa del proyecto se diseña para una precipitación de 20,00 mm/h. Este

valor debe ser confirmado o modificado por algún estudio especial en una

etapa posterior de este proyecto.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

10 de 17

**3.-** **CONCLUSIONES Y RECOMENDACIONES**

El análisis de los antecedentes antes expuestos permite concluir y recomendar lo que

sigue:

**3.1** **Características geomorfológicas del área**

El sitio en donde se implantará el botadero corresponde a cuatro quebradas

que confluyen primero en dos quebradas y después en una quebrada de

mayor tamaño en el tercio inferior respecto del área de implantación del

botadero, éstas quebradas se ubican en la ladera Norte del cordón montañoso

formado por el cerro Guayacán y por el cerro El Peñón, el botadero está

confinado por el Norte por la quebrada El Peral.

La pendiente general de las quebradas afluentes es de un 20% y de la

quebrada de mayor tamaño aguas abajo es de un 15% y las laderas que las

confinan tiene una pendiente promedio de ~40% y con pendientes máximas

de hasta 45%.

En este sector existe roca intrusiva diorítica compuesta por monzodioritas

cuarcíferas de anfíbola-piroxeno y de piroxeno biotita.

**3.2** **Características geomecánicas de los suelos existentes en los sitios donde**

**se implantarán los botaderos**

En el sitio donde se construirá el botadero se distinguen principalmente los

siguientes estratos:

**-** **Suelo Residual**

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

11 de 17

Suelo fino residual con color café, de consistencia media, de plasticidad

media, con un contenido de humedad menor al límite plástico, con

bloques de canto angular aislados de tamaño máximo 6 ”, de estructura

heterogénea, de compresibilidad media a baja y con materia orgánica en

los primeros 30 cm.

El espesor de este estrato se puede considerar entre 0,50 m y 1,50 m.

Este suelo se puede caracterizar asignando a sus parámetros

geomecánicos los siguientes valores:

φ : Angulo de fricción interna : 30°

c : Cohesión : 2,00 ton/m2

γ : Peso unitario Natural : 1,90 ton/m3

E e : Modulo de Elasticidad Estático : 250,00 kg/cm2

E d : Modulo de Elasticidad Dinámico : 750,00 kg/cm2

μ : Modulo de Poisson : 0,30

En general los suelos residuales ocupan la mayor parte del área de las

laderas.

**-** **Roca altamente meteorizada**

Fragmentos dispersos de roca fracturada a meteorizada inmersa en una

matriz de suelo fino residual con color café, de consistencia firme, de

plasticidad media a alta, con un contenido de humedad menor al límite

plástico, de estructura heterogénea, de compresibilidad baja y libre de

materia orgánica.

El espesor de este estrato se puede considerar entre 1,00 m y 2,00 m

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

12 de 17

Este suelo se puede caracterizar asignando a sus parámetros

geomecánicos los siguientes valores:

φ : Angulo de fricción interna : 35o

c : Cohesión : 10,00 ton/m2

γ : Peso unitario Natural : 2,00 ton/m3

E e : Modulo de Elasticidad Estático : 700,00 kg/cm2

E d : Modulo de Elasticidad Dinámico : 2.100,00 kg/cm2

μ : Modulo de Poisson : 0,30

En general la roca altamente meteorizada se ubica en los sectores altos

de las quebradas en donde la pendiente de las laderas es mayor.

**-** **Depósitos coluviales y aluviales**

Suelo formado por gravas arenosas o arenas gravosas con algo o escasos

finos con bolones de hasta 40 ” de tamaño máximo de color café,

pobremente graduada, partículas de cantos angulares a subredondeados,

compacidad media y densa, estructura homogénea y compresibilidad

media.

El espesor de este estrato se puede considerar entre 0,50 m y 3,00 m

El suelo que forma este depósito se puede caracterizar asignando a sus

parámetros geomecánicos los siguientes valores:

φ : Angulo de fricción interna : 33o

c : Cohesión : 0,00 ton/m2

γ : Peso unitario Natural : 2,10 ton/m3

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

13 de 17

E e : Modulo de Elasticidad Estático : 350,00 kg/cm2

E d : Modulo de Elasticidad Dinámico : 1.050,00 kg/cm2

μ : Modulo de Poisson : 0,30

En general los depósitos coluviales rellenan los puntos bajos de las

quebradas.

**3.3** **Clasificación de los suelos existentes en los sitio según la norma NCh**

**2369 of. 2003**

El suelo existente en el sitio donde se construirán los botaderos se puede

clasificar según la norma NCh 2369 Of. 2003 como Tipo I.

**3.4** **Profundidad de la napa freática**

Para todos los efectos de proyecto y de construcción se puede considerar que

no existe la napa freática, pero se debe considerar el aporte de agua de las

cuencas que se deben controlar con contrafosos que eviten el ingreso del

agua desde las laderas al botadero y evacuen las aguas lluvia que caiga sobre

la superficie del botadero.

**3.5** **Tratamiento del suelo existente a nivel de sello de fundación del**

**botadero**

Previo a la colocación del material de relleno del botadero, se debe adecuar

tanto el área donde se colocarán como los suelos sobre los que se apoyarán,

procediendo como sigue:

 Hacer un escarpe que retire todo el suelo suelto y/o contaminado con

materia orgánica y dejar una superficie lo más uniforme posible.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

14 de 17

Se recomienda que el material del escarpe sea acumulado para poder

usarlo en la capa superior a colocar en la parte superior del botadero,

sobre los taludes y sobre las banquetas.

 En los sectores donde la pendiente sea mayor igual a ~15%, o de ~9°

con respecto a la horizontal, se debe hacer escalones de 5 m de ancho

mínimo y para subir al escalón siguiente se debe dejar un talud con

inclinación 1,50/1,00 (H/V).

 El sello de excavación de escarpe debe ser recibido por el ingeniero

geotécnico a cargo del proyecto.

Se hace notar que es fundamental para asegurar la estabilidad del

relleno del botadero que éste se apoye sobre un suelo de calidad

geomecánica buena, lo cual corresponde a los suelos residuales, roca

altamente meteorizada o depósitos coluviales definido para el

botadero.

 Una vez recibido el sello de fundación por el ingeniero geotécnico y

hechas las sobrexcavaciones que pudieran ser necesarias se

comenzará a formar el botadero colocando en los 50 cm inferiores

material grueso de 10 ” de tamaño mínimo.

**3.6** **Recomendaciones para el Relleno del Botadero**

El botadero deberá construirse por etapas, partiendo desde el sector inferior

de la etapa superior hasta llegar al coronamiento de esa etapa, después

continuar desde el sector inferior de la segunda etapa superior hasta llegar al

coronamiento de esa etapa y seguir así sucesivamente.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

15 de 17

Una vez que se han colocado 50 cm de material grueso en el fondo del

botadero se deberá continuar con el relleno del botadero.

Cuando se alcance la superficie definitiva del botadero se deberá colocar una

capa de material impermeable que permita que el agua escurra y sea

controlada por contrafosos.

**3.7** **Caudal de agua a controlar en el botadero**

De acuerdo al método racional del Manual de Carreteras el caudal de agua

que se debe manejar en el botadero es el que sigue:

C ⋅ i ⋅ A

=
Q

3,6

En que:

Q = Caudal en m [3] /s.

C = Coeficiente de la cuenca.

i = Intensidad de la lluvia en mm/h.

A = Area de la cuenca en Km [2] .

Para una precipitación de 20 mm/h

C = 1,25· (0,35 + 0,16 + 0,16 + 0,12) = 0,99

0,99 ⋅ 20,00 ⋅1,10 3
Q = = 6,05 m /s

3,6

**3.8** **Saneamiento hidráulico a considerar en el botadero**

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

16 de 17

Para evitar problemas con el agua que escurrirá por las quebradas que son

rellenadas con el botadero se recomienda proceder como sigue:

 Se debe hacer un contrafoso que circunscriba el área del botadero y

capte toda el agua proveniente de las laderas y de la superficie del

botadero y la lleve en forma controlada a un punto a definir en el

proyecto.

 Los contrafosos deberán tener las siguientes características:

 - En los sectores donde se implantará el contrafoso se deberá hacer

el mismo escarpe que en los sectores donde se apoyaran los

botaderos.

 - El contrafoso deberá estar revestido con una capa de hormigón

proyectado de 5 cm de espesor mínimo.

 - Eventualmente los taludes del contrafoso se deberán sostener con

barras de anclaje.

 - Para los taludes se recomienda considerar inclinaciones de 1/1

(H/V).

 - El contrafoso deberá tener una pendiente del orden del 2% en el

sentido longitudinal hacia ambos lados del eje del botadero.

 Las banquetas deben tener una pendiente de ~3% hacia el interior,

para poder captar las aguas y llevarlas en forma controlada a puntos a

determinar en el proyecto de los botaderos.

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

17 de 17

 Una vez terminado el relleno, a la superficie superior se le debe dar

pendiente transversal hacia el contrafoso que la circunscribe y se

recomienda colocar sobre ella material impermeable proveniente del

escarpe de ~30 cm de espesor mínimo.

 En el desarrollo del proyecto de detalle del botadero se recomienda

considerar que los contrafosos deben controlar un caudal de 12,00

m [3] /s.

En la Figura N° 10 adjunta en el Anexo N° 1 se muestra el corte

típico del contrafoso para el botadero, si se considera que se reviste

con hormigón proyectado y que tienen una pendiente longitudinal del

2%.

**3.9** **Exploración complementaria**

Se recomienda considerar una exploración complementaria a base de

calicatas distribuidas en el sitio en análisis para poder desarrollar

debidamente el diseño del botadero en su etapa de detalle.

**4.-** **ARCHIVO DIGITAL**

En el Anexo No 5 se adjunta el Archivo Digital de este informe.

**ANDRES ALVARADO PAVEZ** **ARTURO GOLDSACK JARPA**

Ingeniero Civil Ingeniero Civil

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

ANEXO No 1

FIGURAS

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

FIGURA No 1

**Ubicación del lugar de interés**
**Botadero Proyecto Dalmacia**

**Botadero Proyecto Dalmacia**

FIGURA No 2

**Mapa Instituto Geográfico Militar 1:50.000**
**Botadero Proyecto Dalmacia**

**Botadero Proyecto Dalmacia**

FIGURA No 3

**Fotografía aérea de la ubicación**
**Botadero Proyecto Dalmacia**

FIGURA No 4

**Fotografía aérea de la ubicación**
**Botadero Proyecto Dalmacia**

FIGURA No 5

**Fotografía aérea de la ubicación**
**Botadero Proyecto Dalmacia**

FIGURA No 6

**Fotografía aérea de la ubicación**
**Botadero Proyecto Dalmacia**

FIGURA No 7

**Fotografía aérea de la ubicación**
**Botadero Proyecto Dalmacia**

FIGURA No 8

**Fotografía aérea de la ubicación**
**Botadero Proyecto Dalmacia**

FIGURA No 9

**Mapa geológico Sernageomin 1:100.000**
**Botadero Proyecto Dalmacia**

**Botadero Proyecto Dalmacia**

ANEXO No 2

PLANO TOPOGRAFIA

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|**LEYENDA**|**LEYENDA**|||
|**LEYENDA**|**LEYENDA**|||

ANEXO No 3

FOTOGRAFIAS

C:\AAP\ RyG \2570 Botadero Proyecto Dalmacia Rev.A 21/03/2014

FOTO N° 1

Vista general del área de implantación del botadero desde el Sur.

La línea roja muestra aproximadamente el límite del botadero.

FOTO N° 2

Vista del fondo de la quebrada ubicada en el tercio inferior respecto del área de implantación del botadero.

Se observan depósitos coluviales y aluviales.

FOTO N° 3

Vista general del área de implantación del botadero desde el Poniente.

Se muestra el área inferior del botadero.

FOTO N° 4

Vista general de la quebrada afluente en el extremo Oriente del botadero.

FOTO N° 5

Vista desde la confluencia de las quebradas Oriente y Poniente, hacia la quebrada Poniente.

Se observan depósitos aluviales y coluviales en el fondo de la quebrada.

FOTO N° 6

Vista desde la confluencia de las quebradas Oriente y Poniente, hacia la quebrada Oriente.

Se observan depósitos aluviales y coluviales en el fondo de la quebrada.

FOTO N° 7

Vista desde la confluencia de las quebradas Oriente y Poniente, hacia aguas abajo.

Se observan depósitos aluviales y coluviales en el fondo de la quebrada

FOTO N° 8

Vista corte en el camino en el área donde se implantará el botadero.

Se muestra un estrato superior de suelo fino residual, un estrato intermedio formado por

fragmentos dispersos de roca fracturada a meteorizada inmersa en una matriz de suelo fino

residual y un estrato inferior formado por roca altamente fracturada y meteorizada, en

bloques de canto angular de tamaño máximo 10 ” y en una matriz de suelo fino residual.

FOTO N° 9

Detalle Foto N° 8.

FOTO N° 10

Vista corte en el camino en el área donde se implantará el botadero.

Se muestra un estrato superior de suelo fino residual, un estrato inferior formado por

fragmentos dispersos de roca fracturada a meteorizada inmersa en una matriz de suelo fino

residual (a la izquierda) y un estrato inferior formado por roca altamente fracturada y

meteorizada, en bloques de canto angular de tamaño máximo 10 ” y en una matriz de suelo

fino residual (a la derecha).

Profundidad

(m)

0,00 ÷ 0,50

Estrato 1

FOTO N° 11

Calicata 1.

Estratigrafía.

Descripción

: Suelo fino residual con color café, de consistencia media, de

plasticidad media, con un contenido de humedad menor al límite

plástico, con bloques de canto angular aislados de tamaño

0,50 ÷ 1,10

Estrato 2

1,10 ÷ 2,70

Estrato 3

máximo 6 ”, de estructura heterogénea, de compresibilidad media

a baja y con materia orgánica en los primeros 30 cm.

: Fragmentos dispersos de roca fracturada a meteorizada inmersa

en una matriz de suelo fino residual con color café, de

consistencia firme, de plasticidad media a alta, con un contenido

de humedad menor al límite plástico, de estructura heterogénea,

de compresibilidad baja y libre de materia orgánica.

: Roca altamente fracturada y meteorizada, en bloques de canto

angular de tamaño máximo 10 ” y en una matriz de suelo fino

residual.

FOTO N° 12

Calicata 1.

Detalle Pared Calicata.

FOTO N° 13

Calicata 1.

Detalle Pared Norte Calicata.

Profundidad

(m)

0,00 ÷ 0,80

Estrato 1

FOTO N° 14

Calicata 2.

Estratigrafía.

Descripción

: Suelo fino residual con color café, de consistencia media, de

plasticidad media, con un contenido de humedad menor al límite

0,80 ÷ 1,40

Estrato 2

1,40 ÷ 3,50

Estrato 3

plástico, con bloques de canto angular aislados de tamaño

máximo 6 ”, de estructura heterogénea, de compresibilidad media

a baja y con materia orgánica en los primeros 30 cm.

: Fragmentos dispersos de roca fracturada a meteorizada inmersa

en una matriz de suelo fino residual con color café, de

consistencia firme, de plasticidad media a alta, con un contenido

de humedad menor al límite plástico, de estructura heterogénea,

de compresibilidad baja y libre de materia orgánica.

: Roca altamente fracturada y meteorizada, en bloques de canto

angular de tamaño máximo 10 ” y en una matriz de suelo fino

residual.

FOTO N° 15

Calicata 2.

Detalle pared Calicata.

Profundidad

(m)

0,00 ÷ 1,10

Estrato 1

FOTO N° 16

Calicata 3.

Estratigrafía.

Descripción

: Suelo fino residual con color café, de consistencia media, de

plasticidad media, con un contenido de humedad menor al límite

plástico, con bloques de canto angular aislados de tamaño

1,10 ÷ 1,60

Estrato 2

1,60 ÷ 3,30

Estrato 3

máximo 6 ”, de estructura heterogénea, de compresibilidad media

a baja y con materia orgánica en los primeros 30 cm.

: Fragmentos dispersos de roca fracturada a meteorizada inmersa

en una matriz de suelo fino residual con color café, de

consistencia firme, de plasticidad media a alta, con un contenido

de humedad menor al límite plástico, de estructura heterogénea,

de compresibilidad baja y libre de materia orgánica.

: Roca altamente fracturada y meteorizada, en bloques de canto

angular de tamaño máximo 10 ” y en una matriz de suelo fino

residual.

FOTO N° 17

Calicata 3.

Detalle pared Calicata.

FOTO N° 18

Calicata 3.

Vista superior de la Calicata.

Profundidad

(m)

0,00 ÷ 0,50

Estrato 1

FOTO N° 19

Calicata 3.

Estratigrafía.

Descripción

: Suelo fino residual con color café, de consistencia media, de

plasticidad media, con un contenido de humedad menor al límite

plástico, con bloques de canto angular aislados de tamaño

0,50 ÷ 1,50

Estrato 2

1,50 ÷ 3,00

Estrato 3

máximo 6 ”, de estructura heterogénea, de compresibilidad media

a baja y con materia orgánica en los primeros 30 cm.

: Fragmentos dispersos de roca fracturada a meteorizada inmersa

en una matriz de suelo fino residual con color café, de

consistencia firme, de plasticidad media a alta, con un contenido

de humedad menor al límite plástico, de estructura heterogénea,

de compresibilidad baja y libre de materia orgánica.

: Roca altamente fracturada y meteorizada, en bloques de canto

angular de tamaño máximo 10 ” y en una matriz de suelo fino

residual.

FOTO N° 20

Calicata 4.

Vista superior de la Calicata.

## ANEXO B Ensayos de Laboratorio

**INFORME DE ENSAYO No** **888.707-A**
MECÁNICA DE SUELOS

### PROYECTO DALMACIA

OT No 28-0000014-14-00

|SECCIÓN LABORATORIO DE GEOTECNIA|Col2|REF.: SLG.PRE.AC 085|EJEMPLAR N°: 1|N° DE PÁGINAS: 5|
|---|---|---|---|---|
|**ELABORADO POR:**<br>Gaspar Besio H.|**REVISADO POR:** <br>Gaspar Besio H.|**APROBADO POR:** <br>Alejandra Sánchez T.|**CLIENTE: LUIS MERINO INGENIERÍA DE**<br>**ROCAS LTDA.**|**CLIENTE: LUIS MERINO INGENIERÍA DE**<br>**ROCAS LTDA.**|
|**ELABORADO POR:**<br>Gaspar Besio H.|**REVISADO POR:** <br>Gaspar Besio H.|**APROBADO POR:** <br>Alejandra Sánchez T.|**Dirección:** Rosario Sur 91, of. 802,<br> Las Condes|**Dirección:** Rosario Sur 91, of. 802,<br> Las Condes|
|**ELABORADO POR:**<br>Gaspar Besio H.|**REVISADO POR:** <br>Gaspar Besio H.|**APROBADO POR:** <br>Alejandra Sánchez T.|**DESTINATARIO:**Daniela Jerez|**DESTINATARIO:**Daniela Jerez|
|**FECHA DE MUESTREO**: ---|**FECHA DE MUESTREO**: ---|**LUGAR DE MUESTREO:** (Realizado por el Cliente)|**LUGAR DE MUESTREO:** (Realizado por el Cliente)|**LUGAR DE MUESTREO:** (Realizado por el Cliente)|
|**FECHA DE RECEPCIÓN**<br>**DE MUESTRAS**: <br>07 / 03 / 2014|**FECHA DE INICIO DE**<br>**LOS TRABAJOS:**<br>10 / 03 / 2014|** FECHA DE TÉRMINO DE**<br>**LOS ENSAYOS:**<br> 17 / 03 / 2014|**FECHA DE EMISIÓN :**19 / 03 / 2014|**FECHA DE EMISIÓN :**19 / 03 / 2014|

Nota:
La reproducción parcial del presente informe debe ser hecha con la autorización de la Sección Laboratorio de Geotecnia de IDIEM.
Los resultados son aplicables sólo a las muestras ensayadas.
Plaza Ercilla No883 / Arturo Prat No1171, Santiago.

Informe No 888 . 707-A PROYECTO DALMACIA

Página 1 de 5

SLG FOR 153 Versión: 10

**1. Antecedentes**

Informe de ensayos realizados según los siguientes documentos recibidos por la Sección
Laboratorio de Geotecnia

 Aceptación de presupuesto SLG.PRE.AC 85/14

De acuerdo a esto, se ejecutaron los siguientes ensayos:

 SLG-PP-06 Granulometría ASTM D422-60 (2007)

 - SLG-PP-08 IP ASTM D4318-10

 SLG-PP-09 Peso especifico bajo tamiz N° 4 ASTM D 854-10

 - SLG-PP-13 Clasificación USCS ASTM D2487-06

Nota:
La reproducción parcial del presente informe debe ser hecha con la autorización de la Sección Laboratorio de Geotecnia de IDIEM.
Los resultados son aplicables sólo a las muestras ensayadas.
Plaza Ercilla No883 / Arturo Prat No1171, Santiago.

Informe No 888 . 707-A PROYECTO DALMACIA

Página 2 de 5

SLG FOR 153 Versión: 10

**2. Identificación de muestras recepcionadas y ensayadas.**

Las muestras recepcionadas y ensayadas corresponden al detalle indicado en la tabla No1.

Tabla No1.- Muestras recepcionadas y ensayadas

|Identificación de Muestra|Calicata<br>[No]|Cotas<br>[m]|Tipo|Recibida|Ensayada|
|---|---|---|---|---|---|
|CALICATA #1|---|0,00-0,50|P|X|X|
|CALICATA #2|---|0,00-0,80|P|X|X|
|CALICATA #3|---|1,10-1,60|P|X|X|
|CALICATA #4|---|---|P|X|X|

La definición del tipo de muestras corresponde a:

P: muestra perturbada

NP: muestra no perturbada en bloque inalterado

SH: muestra tubo Shelby
- CN: muestra cuchara normal

- CD: muestra corona diamantina

C: colpa

Las muestras son almacenadas por IDIEM hasta 15 días luego de emitido este informe.
Posterior a este tiempo serán eliminadas, a menos que exista una solicitud escrita del cliente
para su resguardo y la ejecución de ensayos adicionales por un tiempo determinado.

**Gaspar Besio H.** **Alejandra Sánchez T.**

**Jefe Unidad Geotecnia Ensayos Especiales**

**Laboratorio Geotecnia**

**Jefe División Geotecnia Laboratorios**

**Geotecnia IDIEM** **Geotecnia IDIEM**

GBH/jao

Nota:
La reproducción parcial del presente informe debe ser hecha con la autorización de la Sección Laboratorio de Geotecnia de IDIEM.
Los resultados son aplicables sólo a las muestras ensayadas.
Plaza Ercilla No883 / Arturo Prat No1171, Santiago.

Informe No 888 . 707-A PROYECTO DALMACIA

Página 3 de 5

SLG FOR 153 Versión: 10

**INFORME ENSAYOS DE CLASIFICACIÓN DE MUESTRAS DE SUELO**

|Proyecto|PROYECTO DALMACIA|
|---|---|
|**Inf. Ensaye**|N° 888.707-A|
|**Orden de Trabajo**|28-0000060-14-00|
|**Fecha Inicio**|10-03-2014|
|**Fecha Término**|17-03-2014|

**IDENTIFICACIÓN**

|CALICATA #1|CALICATA #2|CALICATA #3|CALICATA #4|
|---|---|---|---|
|(0,00-0,50)|(0,00-0,80)|(1,10-1,60)|-|

Partículas sobre 3" [%] 0,0 0,0 0,0 0,0

**GRANULOMETRÍA**

|Tamaño de<br>Partícula, mm|Designación<br>Malla o Criba|
|---|---|
|63,50|2 1/2"|
|50,80|2"|
|38,10|1 1/2"|
|25,40|1"|
|19,00|3/4"|
|9,52|3/8"|
|4,76|No 4|
|2,00|No 10|
|0,84|No 20|
|0,42|No 40|
|0,25|No 60|
|0,11|No 140|
|0,07|No 200|

|% en peso que pasa|Col2|Col3|Col4|
|---|---|---|---|
|100,0|100,0|100,0|100,0|
|100,0|100,0|96,3|100,0|
|98,6|100,0|96,3|100,0|
|95,3|99,8|95,9|99,2|
|93,1|99,0|95,4|98,2|
|89,4|97,5|94,3|96,6|
|84,6|93,8|93,3|93,5|
|78,0|88,6|91,4|90,4|
|72,5|83,7|89,4|86,5|
|66,1|80,3|86,7|83,1|
|60,8|77,0|83,8|79,9|
|52,4|71,3|78,2|73,4|
|49,1|69,2|75,9|70,5|

|24|40|45|39|
|---|---|---|---|
|17|21|25|13|
|7|19|20|26|

**Clasificación USCS** SC-SM CL CL CL

**Referencias**

1. SLG-PP-06 Granulometría ASTM D422-63 (2007).

2. Límite Líquido, Límite Plástico e Indice de Plasticidad según SLG-PP-08 basado en ASTM D4318-10.

3. Límite Líquido realizado por método mecánico.

4. Clasificación USCS en base a SLG-PP-13 basado en ASTM D2487-06.

**Observaciones**

a. Límites Líquidos y Plásticos realizados con material preparado en seco.

b. Granulometría realizada por método seco.

Nota:
La reproducción parcial del presente informe debe ser hecha con la autorización de la Sección Laboratorio de Geotecnia de IDIEM.
Los resultados son aplicables sólo a las muestras ensayadas.
Plaza Ercilla No883 / Arturo Prat No1171, Santiago.

Informe No 888 . 707-A PROYECTO DALMACIA

Página 4 de 5

SLG FOR 153 Versión: 10

**INFORME DETERMINACION DE PESO ESPECIFICO BAJO TAMIZ No 4**

|Proyecto|PROYECTO DALMACIA|
|---|---|
|**Inf. Ensaye**|N° 888.707-A|
|**Orden de Trabajo**|28-0000060-14-00|
|**Fecha Inicio**|10-03-2014|
|**Fecha Término**|13-03-2014|

**RESULTADOS DE ENSAYO**

|Muestra|Cota<br>[m]|Gs|
|---|---|---|
|CALICATA #1|(0,00-0,50)|2,82 *|
|CALICATA #2|(0,00-0,80)|2,80 *|
|CALICATA #3|(1,10-1,60)|2,78|
|CALICATA #4|-|2,83 *|
|||<br>|
|||<br>|
|||<br>|
|||<br>|
|||<br>|
|||<br>|

**Referencias**

1. Determinación de Peso Específico bajo tamiz No 4 según SLG-PP-09, basado en ASTM D854-10

2. Se utilizó el método seco para determinar el peso específico

3. El porcentaje de material que pasa el tamiz No 4 es el indicado en el formulario de Clasificación

USCS

**Observaciones**

1. Peso específico informado a la temperatura de 20 oC

2. Se utilizó agua destilada en la ejecución del ensayo.

(*) La muestra presenta metales

Nota:
La reproducción parcial del presente informe debe ser hecha con la autorización de la Sección Laboratorio de Geotecnia de IDIEM.
Los resultados son aplicables sólo a las muestras ensayadas.
Plaza Ercilla No883 / Arturo Prat No1171, Santiago.

Informe No 888 . 707-A PROYECTO DALMACIA

Página 5 de 5

SLG FOR 153 Versión: 10

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 5.1.: ** Parámetros de diseño del Botadero Mina Dalmacia.**

| Tipo de Banco | Simple |
| --- | --- |
| Ángulo de Cara Banco () | 36o a 38° |
| Altura de Banco | 9.6 m |
| Ángulo Final Talud Global | 23o |
| Ancho de Berma Botadero | 12 m |
| Ancho de Rampa Botadero | 5 m |
| Gradiente Máxima Rampa Botadero | 10% |
| Ancho Pretil Rampa Botadero | 2 m |
| Altura Pretil Rampa Botadero | 0.75 m |
| Ancho de Berma Caminos Botadero | 14 m |
| Ancho de Caminos Botadero | 10 m |
| Gradiente Máximo de Camino Botadero | 10% |
| Ancho Pretil Camino Botadero | 2 m |
| Altura Pretil Camino Botadero | 0.75 |

**Tabla 6.1.: ** Propiedades de los materiales de fundación, en el sector de**

| Descripción | Col2 | Peso Unitario<br>Natural | Ángulo de<br>Fricción | Cohesión |
| --- | --- | --- | --- | --- |
| **Descripción** | **Descripción** | **[ton/m3] ** | **[o]** | **[kPa]** |
| Suelo residual | Corresponde al<br>estrato superficial a<br>nivel de terreno | 1.90 | 30 | 20 |
| Roca altamente<br>meteorizada y<br>fracturada (Regolito) | Corresponde al<br>segundo estrato en<br>profundidad | 2.10 | 33 | 100 |
| Roca volcánica<br>Andesítica / Ocoíta | Corresponde a la roca<br>basal, bajo las<br>unidades anteriores. | 28.2 | 60 | 4,110 |

**Tabla 6.2.: ** Coeficientes sísmicos utilizados para el análisis.**

| Sismo | Aceleración máxima | Coeficiente sísmico |
| --- | --- | --- |
| **_Operación_** | _0.50 g = 4.90 (m/s2) _ | _0.17_ |
| **_Máximo Probable_** | _0.95 g = 9.29 (m/s2) _ | _0.21_ |

**Tabla 7.2: ** . Criterios de Aceptabilidad geotécnica para el diseño de Botaderos.**

| Referencia | Condición | Criterios de<br>Aceptabilidad | Comentarios |
| --- | --- | --- | --- |
| **Karzulovic (2006)** | Botaderos de Mina<br>Andina, algunos de<br>los cuales se<br>encuentran<br>ubicados sobre<br>morrenas<br>glaciares. | FS> 1.20 y PF< 10% | Condición Estática |
| **Karzulovic (2006)** | Botaderos de Mina<br>Andina, algunos de<br>los cuales se<br>encuentran<br>ubicados sobre<br>morrenas<br>glaciares. | FS> 1.10 y PF< 25% | Condición Sísmica<br>(Sismo Operacional) |
| **Karzulovic (2006)** | Botaderos de Mina<br>Andina, algunos de<br>los cuales se<br>encuentran<br>ubicados sobre<br>morrenas<br>glaciares. | FS> 1.00 y PF< 50% | Condición Sísmica<br>(Terremoto Máximo Probable) |

**Tabla 7.3: ** .**

| Referencia | Condición | Criterios de<br>Aceptabilidad | Comentarios |
| --- | --- | --- | --- |
| **M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)** | Condición establecida<br>de acuerdo con<br>Consecuencias y<br>Confianza Moderadas<br>en los diseños. | FS> 1.30 y PF< 15% | Condición Estática |
| **M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)** | Condición establecida<br>de acuerdo con<br>Consecuencias y<br>Confianza Moderadas<br>en los diseños. | FS> 1.10 | Condición Sísmica<br>(Sismo Operacional) |
| **M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)** | Condición establecida<br>de acuerdo con<br>Consecuencias y<br>Confianza Moderadas<br>en los diseños. | FS> 1.05 | Condición Sísmica<br>(Terremoto Máximo Probable) |

**Tabla 7.4: ** . Criterios de Aceptabilidad geotécnica definidos para el diseño del**

| Referencia | Condición | Criterios de<br>Aceptabilidad | Comentarios |
| --- | --- | --- | --- |
| **M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**<br> <br>**Karzulovic (2006)** | Condición establecida<br>de<br>acuerdo<br>con<br>Consecuencias<br>y <br>Confianza Moderadas<br>en los diseños. | FS> 1.30 y PF< 10% | Condición Estática |
| **M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**<br> <br>**Karzulovic (2006)** | Condición establecida<br>de<br>acuerdo<br>con<br>Consecuencias<br>y <br>Confianza Moderadas<br>en los diseños. | FS> 1.10 y PF< 25% | Condición Sísmica<br>(Sismo Operacional) |
| **M. Hawley y J.**<br>**Cunning**<br>**(2016-2017)**<br> <br>**Karzulovic (2006)** | Condición establecida<br>de<br>acuerdo<br>con<br>Consecuencias<br>y <br>Confianza Moderadas<br>en los diseños. | FS> 1.05 y PF< 45% | Condición Sísmica<br>(Terremoto Máximo Probable) |

**Tabla 8.1.: ** Resultados de análisis de estabilidad de Botadero Dalmacia.**

| ANÁLISIS | SECCIÓN | CONDICIÓN DE ANÁLISIS | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **_ANÁLISIS_** | **_SECCIÓN_** | **_ESTÁTICO_**<br>**_(kh=0)_** | **_SISMO OPERACIONAL_**<br>**_(kh=0.17)_** | **_SISMO MAX. CREÍBLE_**<br>**_(kh=0.21)_** |
| **_ANÁLISIS_** | **_SECCIÓN_** | **_GLE_** | **_GLE_** | **_GLE_** |
| **_Global_** | A-A' | _FS (det.) = 2.04_<br>_FS (mean) = 2.06_<br>_PF = 0.0%_ | _FS (det.) = 1.34_<br>_FS (mean) = 1.36_<br>_PF = 0.6%_ | _FS (det.) = 1.23_<br>_FS (mean) = 1.25_<br>_PF = 2.9%_ |
| **_Local_** | Talud 1 (T-1) | _FS (det.) = 2.20_<br>_FS (mean) = 2.25_<br>_PF = 0.0%_ | _FS (det.) = 1.60_<br>_FS (mean) = 1.64_<br>_PF = 1.2%_ | _FS (det.) = 1.50_<br>_FS (mean) = 1.53_<br>_PF = 1.9%_ |
| **_Local_** | Talud 2 (T-2) | _FS (det.) = 1.80_<br>_FS (mean) = 1.85_<br>_PF = 0.1%_ | _FS (det.) = 1.34_<br>_FS (mean) = 1.38_<br>_PF = 6.2%_ | _FS (det.) = 1.26_<br>_FS (mean) = 1.29_<br>_PF = 12.0%_ |
| **_Local_** | Talud 3 (T-3) | _FS (det.) = 1.76_<br>_FS (mean) = 1.81_<br>_PF = 0.1%_ | _FS (det.) = 1.30_<br>_FS (mean) = 1.34_<br>_PF = 9.1%_ | _FS (det.) = 1.22_<br>_FS (mean) = 1.25_<br>_PF = 15.1%_ |

**Tabla 9.1: ** . Resultados de análisis de estabilidad de Botadero Dalmacia. Método de**

| Condición de Análisis | Col2 | Carga<br>Sísmica | Estabilidad | Col5 | Deformación<br>Máxima | Criterio<br>Aceptabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Condición de Análisis** | **Condición de Análisis** | **Carga**<br>**Sísmica** | **FS**<br>**(análisis**<br>**SLIDE)** | **SRF**<br>**(Modelo**<br>**Numérico)** | **SRF**<br>**(Modelo**<br>**Numérico)** | **SRF**<br>**(Modelo**<br>**Numérico)** |
| **Botadero**<br>**Dalmacia** | **Estático** | 0.0 | 2.04 | 2.03 | 0.5% | Cumple |
| **Botadero**<br>**Dalmacia** | **Sismo Op.** | 0.17 | 1.34 | 1.31 | 0.8% | Cumple |
| **Botadero**<br>**Dalmacia** | **Sismo Máx.** | 0.21 | 1.23 | 1.21 | 1.0% | Cumple |
