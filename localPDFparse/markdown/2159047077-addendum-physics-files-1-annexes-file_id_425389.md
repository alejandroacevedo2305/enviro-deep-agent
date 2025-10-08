---
title: Sin título
author: VEMAS
date: D:20240202205608-03'00'
language: es
type: report
pages: 18
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 22015-ID-HI-MC-00-B DISEÑO TRANQUE AGRÍCOLA ESTRELLA INFORME DE MODELACIÓN HIDRÁULICA
-->

# 22015-ID-HI-MC-00-B DISEÑO TRANQUE AGRÍCOLA ESTRELLA INFORME DE MODELACIÓN HIDRÁULICA

|Col1|Col2|Col3|
|---|---|---|
|APROBADO|||
|PARA APROBACIÓN|||
|PARA REVISIÓN CLIENTE|02-02-2024|B|
|**REVISIÓN**|**FECHA REVISIÓN**|**N° REVISIÓN**|
||||
|**PREPARÓ**|Pablo Salgado|Pablo Salgado|
|**REVISÓ**|Marcela Rojas|Marcela Rojas|
|**APROBÓ**|Rafael Valenzuela|Rafael Valenzuela|

**22015-ID-HI-MC-00-B**
**INFORME DE MODELACIÓN HIDRÁULICA**

1 Introducción ................................................................................................................................ 3

2 Antecedentes .............................................................................................................................. 3

2.1 Topografía ........................................................................................................................... 3

2.2 Caudales de diseño.............................................................................................................. 4

2.3 Antecedentes del Lecho ...................................................................................................... 5

2.4 Coeficientes de rugosidad ................................................................................................... 5

3 Modelo Hidráulico ....................................................................................................................... 7

3.1 Generación modelo de terreno ........................................................................................... 7

3.2 Mallado ............................................................................................................................... 8

3.3 Condiciones de borde.......................................................................................................... 9

3.3.1 Condiciones de borde sin proyecto ............................................................................. 9

3.3.2 Condiciones de borde con proyecto ........................................................................... 9

4 Resultados Modelación Hidráulica 2D ...................................................................................... 10

4.1 Escenario Base ................................................................................................................... 10

4.2 Escenario con proyecto ..................................................................................................... 15

4.3 Condiciones hidráulicas en la descarga disipador de energía ........................................... 16

4.4 Condiciones hidráulicas en la Captación ........................................................................... 17

22015-ID-HI-MC-00-B 2

**1** **Introducción**

Con el objetivo de evaluar y/o cuantificar el posible impacto de las obras en el escurrimiento de los
cauces, y de definir la ubicación de algunas de ellas, se ha realizado la modelación hidráulica de los
cauces que se encuentran en la zona del proyecto para determinar el eje hidráulico de la qubrada
sin nombre, Estero Cardo Verde y río Perquilauquen.

Los cauces naturales en el entorno del proyecto se encuentran conectados hidráulicamente, de tal
manera que la quebrada sin nombre es afluente al estero Cardo Verde y este a su vez confluye al río
Perquilauquen.

El eje hidráulico de la quebrada sin nombre permite definir la ubicación de la presa principal,
estableciendo que quede fuera del área de inundación de la crecida de 100 años de período de
retorno, y ubicar el disipador de energía, de tal manera que descargue las aguas en forma

controlada.

Por otra parte, la captación de las aguas desde el río Perquilauquen, se realiza mediante elevación
mecánica, utilizando un grupo de bombas que se ubican en diferentes niveles dependiendo de las
alturas de agua que experimenta el río en distintas épocas del año, es por ello que se calculó el eje
hidráulico en la captación, con la finalidad de determinar los caudales de operación para cada una
de las plataformas.

En la Figura 1.1 se presenta la ubicación general de las obras y los cauces ubicados en las cercanías
del proyecto.

Figura 1.1 Ubicación general de las obras.

**2** **Antecedentes**

**2.1** **Topografía**

La información topográfica disponible para el desarrollo del proyecto se detalla a continuación:

 Levantamiento topográfico con curvas de nivel cada 0,50 m, sobre el costado poniente del
Río Perquilauquén.

 Nube de puntos de elevaciones sobre el costado oriente del Río Perquilauquén, que cubre
el área donde se desarrolla el proyecto.

22015-ID-HI-MC-00-B 3

 Levantamiento topobatimétrico de perfiles transversales sobre los cauces en estudio. Estos
perfiles se dividen en 25 sobre el Río Perquilauquén, 20 sobre el estero Cardo Verde y 10 a
lo largo de la Quebrada S/N.

El detalle de los levantamientos topográficos y topobatimétricos se presentan el informe de
topografía (INFORME TOPOGRAFICO TRANQUE CAUQUENES_version 02_correccion).

En la Figura 2.1 se muestra la topografía levantada para el desarrollo del proyecto y la modelación

hidráulica de los cauces.

Figura 2.1 Información topográfica disponible.

**2.2** **Caudales de diseño**

El detalle de los criterios de cálculos y resultados de la determinación de los caudales para el diseño
de las obras se presentan en la hidrología del proyecto (22015-EB-HID-MC-01-B Hidrología).

Según las exigencias de la DGA el diseño de las obras sobre cauces naturales debe ser evaluado para
los caudales de crecida asociados a los períodos de retorno de 100 años de período de retorno y
verificados para los caudales de 200 años de período de retorno. En el Cuadro 2.1 se presentan los
caudales de crecida para los 3 cauces en estudios para los períodos de retorno de diseño.

Cuadro 2.1 Caudales de Crecida para T=100 años y T=200 años

|T<br>[años]|Quebrada Sin Nombre<br>[m3/s]|Estero Cardo Verde<br>[m3/s]|Río Perquilauquén<br>[m3/s]|
|---|---|---|---|
|100|1,23|90,54|4.455,1|
|200|1,34|103,27|5.007,8|

A partir de la simulación de estos caudales se calculan los ejes hidráulicos en crecida en la zona de
la descarga de la obra de seguridad y de la captación de las aguas en el río Perquilauquen.

22015-ID-HI-MC-00-B 4

En el caso de la zona de la descarga de la obra de seguridad, se considera un escenario sin y con
proyecto, sin embargo, para la captación, que es una verificación hidráulica de una obra existente,
se considera un único escenario con proyecto.

En el caso de la simulación del escenario con proyecto, se debe considerar que para el estero cardo
verde y río Perquilauquen, se utilizarán los caudales de crecida del Cuadro 2.1, mientras que, para
la quebrada sin nombre, el caudal de crecida corresponderá al caudal de diseño de la obra de
seguridad, el cual corresponde a 500 l/s.

En el caso de la captación que cuenta con plataformas en la que se instalan los equipos de bombeo
durante la época de riego, el análisis hidráulico se centra en la definición del rango de caudales de
operación de dichas obras menores. Se simuló un rango de caudales entre el caudal mínimo
determinado para la probabilidad de excedencia del 85% y el caudal de crecida asociado al período
de retorno de 100 años. El caudal mínimo es igual a 0,77 m [3] /s y el caudal máximo igual a 4.455,1
m [3] .

**2.3** **Antecedentes del Lecho**

Como parte del estudio geotécnico se realizaron varias exploraciones de terreno, detalle que se
encuentra en el documento 22015-EB-GEO-INF-01-B Informe Geológico-Geotécnico. En este caso
particular se busca caracterizar el lecho de la quebrada sin nombre.

Para ello se ha considerado la información recopilada de la calicata CE-2 que se encuentra muy
cercana al cauce. Los resultados de los ensayos realizados a la muestra de suelo indican que se trata
de una arena arcillo limosa. En el Cuadro 2.2 se presentan los diámetros característicos de las
partículas del lecho.

Cuadro 2.2 Diámetros característicos del lecho (mm)

**2.4** **Coeficientes de rugosidad**

|d<br>50|d<br>90|
|---|---|
|0,60|1,60|

La rugosidad en los cauces se define a partir del coeficiente Manning, para lo cual, ante la falta de
información de terreno, se utiliza el método de Cowan como metodología de estimación, el cual
considera que el coeficiente de Manning se puede aproximar de la siguiente forma:

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) ⋅m

Donde:

n 0 : valor básico del coeficiente de rugosidad para un tramo recto y uniforme.
n 1 : incremento por irregularidades de las secciones.
n 2 : incremento por variaciones de forma y dimensiones de las secciones.
n 3 : incremento por obstrucciones.
n 4 : incremento por vegetación en el cauce.
m : factor correctivo por curvas y meandros del río.

Los valores recomendados para los coeficientes de la ecuación de Cowan se pueden obtener de Ven
Te Chow (1959) y se presentan en el Cuadro 2.3.

22015-ID-HI-MC-00-B 5

Cuadro 2.3 Coeficientes recomendados para el cálculo de rugosidad mediante Cowan.

|Grado de los efectos por meandros|Menor|m|1,000|
|---|---|---|---|
|Grado de los efectos por meandros|Apreciable|Apreciable|1,150|
|Grado de los efectos por meandros|Severo|Severo|1,300|
|Material involucrado|Tierra|n0|0,020|
|Material involucrado|Corte en roca|Corte en roca|0,025|
|Material involucrado|Grava fina|Grava fina|0,024|
|Material involucrado|Grava gruesa|Grava gruesa|0,028|
|Grado de irregularidad|Suave|n1|0,000|
|Grado de irregularidad|Menor|Menor|0,005|
|Grado de irregularidad|Moderado|Moderado|0,010|
|Grado de irregularidad|Severo|Severo|0,020|
|Variaciones de la sección transversal|Gradual|n2|0,000|
|Variaciones de la sección transversal|Ocasionalmente alternante|Ocasionalmente alternante|0,005|
|Variaciones de la sección transversal|Frecuentemente alternante|Frecuentemente alternante|0,010 - 0,015|
|Efecto relativo de las obstrucciones|Insignificante|n3|0,000|
|Efecto relativo de las obstrucciones|Menor|Menor|0,010 - 0,015|
|Efecto relativo de las obstrucciones|Apreciable|Apreciable|0,020 - 0,030|
|Efecto relativo de las obstrucciones|Severo|Severo|0,040 - 0,060|
|Vegetación|Baja|n4|0,005 - 0,010|
|Vegetación|Media|Media|0,010 - 0,025|
|Vegetación|Alta|Alta|0,025 - 0,050|
|Vegetación|Muy alta|Muy alta|0,050 - 0,100|

Fuente: Ven Te Chow (1959).

Por otra parte, dentro del área de modelación existen diferentes coberturas de suelo, las cuales se
identificaron mediante la ortofoto, imágenes satelitales históricas de Google Earth y visitas al área
del proyecto.

Teniendo en consideraciones toda la información disponible con respecto a la rugosidad de los
cauces, a las cuales se asignaron diferentes coeficientes de Manning para las diferentes zonas del

proyecto.

En el Cuadro 2.4 se presentan los coeficientes de Manning adoptados para cada tipo de superficie.
Y En la Figura 2.2 se presenta la distribución espacial de los tipos de suelo identificados en el área
del proyecto.

Cuadro 2.4 Coeficientes de rugosidad de Manning adoptados.

|Tipo de suelo|n|
|---|---|
|Río Perquilauquén|0,025|
|Estero Cardo Verde|0,030|
|Quebrada Sin Nombre|0,035|
|Praderas|0,040|
|Terreno agrícola|0,040|

22015-ID-HI-MC-00-B 6

Figura 2.2 Tipos de suelo en el área de modelación.

**3** **Modelo Hidráulico**

Para modelar el escurrimiento en la zona de interés se utilizó el software Iber, el cual es un modelo
numérico de volúmenes finitos, que simula el flujo en lámina libre mediante la resolución de las
ecuaciones de Saint Venant bidimensionales. El mallado es no estructurado, lo que ayuda a la
representación de geometrías complejas.

Se desarrollaron escenarios de modelación hidráulica, asociados a los caudales de crecidas para los
periodos de retorno de 100 y 200 años, para los escenarios sin y con proyecto. Y una simulación que
aumenta constantemente el caudal de entrada para el río Perquilauquen desde el caudal mínimo
(caudal de sequía) y el caudal máximo (crecida de 100 años) en el río.

La bondad de los resultados se evaluó buscando que la modelación muestre resultados coherentes
con el levantamiento topográfico del cauce y sus características hidromorfológicas.

**3.1** **Generación modelo de terreno**

Con el objetivo obtener una buena representación del eje hidráulico de los cauces, se construyó un
modelo de terreno utilizando todos los levantamientos topográficos del proyecto, integrando la
topografía terrestre más la topo batimetría de los cauces. Para ello, la interpolación TIN de las curvas
de nivel disponibles sobre la ribera izquierda del río Perquilauquen más la nube de puntos levantada
en la ribera derecha. Los perfiles topobatimétrico fueron sometidos a un proceso de interpolación
a través de la herramienta RAS Mapper de HEC-RAS. Finalmente, mediante el programa QGIS, se
consolidan todos los levantamientos obteniendo un único modelo de terreno del área del proyecto.

En la Figura 3.1 se presenta el modelo de terreno generado para la modelación hidráulica en dos

dimensiones.

22015-ID-HI-MC-00-B 7

Figura 3.1 Modelo de terreno generado.

**3.2** **Mallado**

Se definieron 4 zonas de mallado distintas. La primera zona consiste en una malla fina, con celdas
de 2 m en aquellas áreas donde se espera flujo significativo, como los cauces y sus riberas. En las
zonas adyacentes a los cauces, se aplicó un mallado intermedio, con celdas de 4 m. Para aquellas
áreas presumiblemente fuera del alcance de flujo, se implementó un mallado un poco más grueso,
con celdas de 5 metros. Finalmente, al sur de la ribera izquierda del río Perquilauquen, donde el
terreno es relativamente plano, se utilizó un mallado de 10 m. En la Figura 3.2 se presenta la
superficie de modelación y las diferentes zonas de mallado.

Figura 3.2 Superficie de modelación.

22015-ID-HI-MC-00-B 8

**3.3** **Condiciones de borde**

**3.3.1** **Condiciones de borde sin proyecto**

Como condición de contorno, se ha definido tres puntos de entradas de caudal con descarga
constante, correspondientes a la Quebrada Sin Nombre, estero Cardo Verde y al río Perquilauquen.
Los caudales de entrada corresponden a los presentados en el capítulo 2.2 del presente informe.

Las secciones donde se imponen las condiciones de borde de entrada se han desplazado unos
metros hacia aguas abajo con el objetivo de asegurar que todo el perfil se encuentre dentro del MDT
y evitar la existencia de puntos sin elevación.

La condición de contorno de salida del modelo fue establecida en régimen supercrítico. En la Figura
3.3 se presenta la ubicación de las condiciones de borde de entrada y salida del modelo.

Figura 3.3 Condiciones de borde - escenario sin proyecto.

Estas mismas condiciones de borde fueron utilizadas para desarrollar una simulación con un caudal
variable en un rango desde 1 m [3] /s hasta 5.000 m [3] /s en el Río Perquilauquen, con el objetivo de
definir los rangos de operación de las plataformas.

**3.3.2** **Condiciones de borde con proyecto**

Para la simulación del escenario con proyecto, se modifica la Entrada N°1, ya que el agua se desviará
a través del tranque, y frente a una crecida podrá regular el agua caída, en consecuencia, se ha
ingresado una entrada puntual con un caudal constante igual 0,50 m [3] /s, el cual corresponde al
caudal de diseño de la obra de seguridad.

La ubicación de la entrada N°1 corresponde a la descarga del disipador de energía. En la Figura 3.4
se presentan las condiciones de borde para el escenario con proyecto.

22015-ID-HI-MC-00-B 9

Figura 3.4 Condiciones de borde - escenario con proyecto.

**4** **Resultados Modelación Hidráulica 2D**

Las simulaciones realizadas están directamente relacionadas con los requisitos técnicos para el
diseño de las estructuras y las condiciones hidráulicas exigidas por la DGA, para asegurar que en
caso de existir alguna influencia sobre el escurrimiento, esta sea controlada y no genere impactos a
terceros ni a la calidad de las aguas.

Se han llevado a cabo las simulaciones necesarias para respaldar el diseño de las nuevas estructuras
y verificar que las obras existentes no generen impactos.

**4.1** **Escenario Base**

Se realizó una modelación base que considera los caudales de diseño y verificación en crecida, con
el objetivo de determinar las áreas de inundación que produce una lluvia importante.

En el caso de las obras que se ubican en la quebrada sin nombre, esta modelación corresponde al
escenario sin proyecto, mientras que para la captación permitirá verificar que la plataforma que se
encuentra a una cota mayor que la crecida de 100 años.

De los resultados de esta simulación se evidencia que el río Perquilauquen controla el escurrimiento
en crecidas tanto en el estero Cardo Verde como en la sección baja de la quebrada sin nombre. Lo
cual es consecuencia de los altos caudales que conduce el río Perquilauquen en comparación a los
caudales de los otros cauces, y a las características topográficas de esa zona, que se caracteriza por
pendientes bajas, lo que se evidencia en la formación de meandros en río Perquilauquen.

En la Figura 4.1 se presentan fotografías, donde se puede apreciar las diferencias en las magnitudes
de los cauces que se encuentran en el proyecto, y la influencia del río Perquilauquen en el estero
Cardo Verde y a su vez en la quebrada sin nombre. También se evidencia la influencia del río
Perquilauquen, en que el nivel de agua se impone hacia aguas arriba.

22015-ID-HI-MC-00-B 10

Figura 4.1 Fotografías de los cauces del entorno al proyecto.

En Figura 4.2 muestra la profundidad del flujo para el periodo de retorno de 100 años, donde las
profundidades máximas se dan dentro del cauce activo recurrente del Río Perquilauquen,
superando los 10 metros de profundidad en algunas secciones.

En el caso del estero Cardo Verde se observa la fuerte influencia desde aguas abajo del río
Perquilauquen. Las profundidades máximas están en el rango entre 5, y 6 m de profundidad.

22015-ID-HI-MC-00-B 11

Mientras que la quebrada sin nombre experimenta profundidades máximas del orden de 3 m, en la
descarga al Cardo Verde. Donde también se encuentra influenciado por el río Perquilauquen.

La modelación indica que frente a una crecida importante del río Perquilauquen, este se desborda
inundando los terrenos contiguos al cauce principal, y recuperando vías de escurrimiento
eventuales, que han sido modificadas por las actividades económicas características de esta zona.

Figura 4.2 Profundidad del flujo para la crecida con 100 años de periodo de retorno.

En la Figura 4.3 se presenta la cota de agua obtenida en los cauces modelados. Se observa que las
cotas de agua en el sector donde se ubicará el disipador de energía es del orden de 131,2 msnm,
mientras que la cota en la captación es aproximadamente de 130,6 msnm.

Figura 4.3 Cota de agua para la crecida con 100 años de periodo de retorno.

22015-ID-HI-MC-00-B 12

Las velocidades experimentadas en crecida se muestran en la Figura 4.4. Al igual que con las
profundidades los mayores valores se evidencian en el Río Perquilauquen, en particular en el
extremo de más aguas abajo del modelo, en donde río cambia de régimen de subcrítico a super
crítico, debido a la existencia de un fondo rocoso que genera una sección de control (altura crítica).

En la sección del cauce donde se encuentra la descarga del disipador de energía, las velocidades
varían entre 0 m/s y 2 m/s como máximo.

Figura 4.4 Velocidad de flujo para la crecida de 100 años de periodo de retorno.

Como medio de verificación se realizó la simulación hidráulica para la crecida de 200 años. En las
Figuras 4.5, 4.6 y 4.7 se presentan los resultados obtenidos para la profundidad, cotas de inundación
y velocidad de escurrimiento.

22015-ID-HI-MC-00-B 13

Figura 4.5 Profundidad del flujo para la crecida con 200 años de periodo de retorno.

Figura 4.6 Cota de agua para la crecida con 200 años de periodo de retorno.

Figura 4.7 Velocidad de flujo para la crecida de 200 años de periodo de retorno.

Para la crecida con periodo de retorno de 200 años, los resultados son similares a los obtenidos para
la modelación del escurrimiento para la crecida de 100 años de período de retorno. Se observa un
leve aumento en la profundidad de algunos sectores, siendo en promedio de 40 cm en toda la
superficie inundada. Las velocidades del flujo presentan una variación mínima, que se hacen
evidentes principalmente dentro del río Perquilauquén, presentando un aumento de
aproximadamente 0,1 m/s.

22015-ID-HI-MC-00-B 14

**4.2** **Escenario con proyecto**

Como se ha mencionado, la modelación del escenario con proyecto es relevante para la revisión del
comportamiento hidráulico en la descarga del disipador de energía, e indirectamente en la zona en
que el pretil principal de la presa que se encuentra dentro de la quebrada sin nombre.

La diferencia con la modelación sin proyecto es que se consideró una entrada puntual de caudal,
ubicada en la salida de la obra de seguridad, donde se ingresa un caudal de 500 lt/s, correspondiente

al caudal de diseño de esta obra.

En las Figuras de la 4.8 a la 4.10, se presentan las profundidades, cotas de inundación y velocidades
para la situación con proyecto de la crecida de 100 años de período de retorno, donde se evidencia
que los resultados son prácticamente iguales a la situación sin proyecto, y que tanto el estero Cardo
Verde como la Quebrada Sin Nombre, se ven influenciados por el nivel de agua alcanzado por el río
Perquilauquén.

Figura 4.8 Profundidad del flujo para la crecida con 100 años de periodo de retorno.

22015-ID-HI-MC-00-B 15

Figura 4.9 Nivel de agua para la crecida con 100 años de periodo de retorno.

Figura 4.10 Velocidad del flujo para la crecida con 100 años de periodo de retorno.

**4.3** **Condiciones hidráulicas en la descarga disipador de energía**

Dados los requerimientos de diseño del disipador de energía de la obra de seguridad, se utilizaron
los resultados de la modelación hidráulica para posicionar las obras y establecer sus condiciones de

diseño.

La ubicación espacial en el terreno se definió de acuerdo con el área de inundación de la crecida de
100 años de período de retorno, que de acuerdo con la modelación hidráulica en la descarga del
disipador se encuentra en la cota 131,2 msnm. El empalme hidráulico considera que el nivel de agua

22015-ID-HI-MC-00-B 16

de aguas abajo sea capaz de contener el resalto y para ello, la cota de agua sobre la grada del
disipador debe ser al menos igual a la cota de agua de aguas abajo para la crecida de 100 años. La
velocidad en la descarga de las aguas hacia la quebrada sin nombre es aproximadamente de 0,3
m/s. En la Figura 4.11 se presenta el perfil transversal sobre la quebrada sin nombre donde se ubica
el disipador de energía.

Figura 4.11 Sección transversal en disipador de energía.

**4.4** **Condiciones hidráulicas en la Captación**

Con respecto a las plataformas donde se ubica la obra de captación, la modelación hidráulica
permitió establecer los caudales de operación de las plataformas que alojan a los equipos móviles
de la captación. Para ello realizó una simulación con caudal variable, donde se modelaron caudales
en un rango de 1 m [3] /s a 5.000 m [3] /s, para determinar el nivel de agua para distintos caudales.

En la Figura 4.12 se presenta la relación entre el nivel de agua y el caudal en la sección donde se
ubican las plataformas.

Figura 4.13 Variación del nivel de agua con respecto al caudal.

22015-ID-HI-MC-00-B 17

Como resultado de este análisis se establece que la Plataforma N°1 se destinará para caudales
menores a 610 m [3] /s, la Plataforma N°2 se empleará para caudales menores a 2.420 m [3] /s, y la
Plataforma N°3 se destinará a los caudales hasta 4.455 m [3] /s. En la Figura 4.13 se presenta
esquemáticamente los niveles de agua y caudales asociados a las cotas de elevación de cada
plataforma.

Figura 4.13 Sección transversal en plataformas de captación.

La evaluación de los niveles de agua para diferentes caudales también consideró el análisis de los
caudales mínimos. La simulación realizada se hizo para el caudal mínimo de probabilidad de
excedencia del 85 %, el cual tiene un valor de 0,77 m [3] /s. El resultado indica que la cota de agua de
este caudal es de 120 msnm, por lo tanto, el caudal de diseño podrá ser captado desde la plataforma
N°1. Es importante señalar, que los años en que hay caudales de sequía, no capta el caudal máximo
de derecho que corresponde a 200 l/s, a lo más se pueden captar 100 l/s, y esta experiencia es la
que justifica la construcción del tranque para las épocas deficitarias en el río Perquilauquen.

La verificación hidráulica de las plataformas indica que no generan un impacto en las aguas del río
Perquilauquen, desde el punto de vista del escurrimiento ni de la calidad de las aguas,
consecuentemente, no hay afectación a tercero por la instalación de estas pequeñas obras.

22015-ID-HI-MC-00-B 18

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1: Caudales de Crecida para T=100 años y T=200 años**

| T<br>[años] | Quebrada Sin Nombre<br>[m3/s] | Estero Cardo Verde<br>[m3/s] | Río Perquilauquén<br>[m3/s] |
| --- | --- | --- | --- |
| 100 | 1,23 | 90,54 | 4.455,1 |
| 200 | 1,34 | 103,27 | 5.007,8 |

**Tabla 2.2: Diámetros característicos del lecho (mm)**

| d<br>50 | d<br>90 |
| --- | --- |
| 0,60 | 1,60 |

**Tabla 2.3: Coeficientes recomendados para el cálculo de rugosidad mediante Cowan.**

| Grado de los efectos por meandros | Menor | m | 1,000 |
| --- | --- | --- | --- |
| Grado de los efectos por meandros | Apreciable | Apreciable | 1,150 |
| Grado de los efectos por meandros | Severo | Severo | 1,300 |
| Material involucrado | Tierra | n0 | 0,020 |
| Material involucrado | Corte en roca | Corte en roca | 0,025 |
| Material involucrado | Grava fina | Grava fina | 0,024 |
| Material involucrado | Grava gruesa | Grava gruesa | 0,028 |
| Grado de irregularidad | Suave | n1 | 0,000 |
| Grado de irregularidad | Menor | Menor | 0,005 |
| Grado de irregularidad | Moderado | Moderado | 0,010 |
| Grado de irregularidad | Severo | Severo | 0,020 |
| Variaciones de la sección transversal | Gradual | n2 | 0,000 |
| Variaciones de la sección transversal | Ocasionalmente alternante | Ocasionalmente alternante | 0,005 |
| Variaciones de la sección transversal | Frecuentemente alternante | Frecuentemente alternante | 0,010 - 0,015 |
| Efecto relativo de las obstrucciones | Insignificante | n3 | 0,000 |
| Efecto relativo de las obstrucciones | Menor | Menor | 0,010 - 0,015 |
| Efecto relativo de las obstrucciones | Apreciable | Apreciable | 0,020 - 0,030 |
| Efecto relativo de las obstrucciones | Severo | Severo | 0,040 - 0,060 |
| Vegetación | Baja | n4 | 0,005 - 0,010 |
| Vegetación | Media | Media | 0,010 - 0,025 |
| Vegetación | Alta | Alta | 0,025 - 0,050 |
| Vegetación | Muy alta | Muy alta | 0,050 - 0,100 |

**Tabla 2.4: Coeficientes de rugosidad de Manning adoptados.**

| Tipo de suelo | n |
| --- | --- |
| Río Perquilauquén | 0,025 |
| Estero Cardo Verde | 0,030 |
| Quebrada Sin Nombre | 0,035 |
| Praderas | 0,040 |
| Terreno agrícola | 0,040 |
