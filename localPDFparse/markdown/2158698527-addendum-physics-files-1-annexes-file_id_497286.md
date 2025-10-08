---
title: Sin título
author: Luis Rojas Olivares
date: D:20211209113449-03'00'
language: es
type: report
pages: 23
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME TÉCNICO SERVICIO DE LEVANTAMIENTO AEROFOTOGRAMÉTRICO
-->

# INFORME TÉCNICO SERVICIO DE LEVANTAMIENTO AEROFOTOGRAMÉTRICO

## Mina Algarrobo INT-CMP-ALG-01-1

La Serena, 09 de diciembre de 2021.

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **1** de **23**

#### ÍNDICE

1 Introducción ................................................................................................................... 2

1.1 Objetivos .................................................................................................................. 2

1.2 Antecedentes del proyecto ...................................................................................... 2

2 Metodología de trabajo .................................................................................................. 3

2.1 Parámetros del Proyecto ......................................................................................... 3

2.2 Puntos de Referencia ............................................................................................... 4

2.2.1 Red Geodésica. ................................................................................................. 4

2.2.2 Vinculación Geodésica. ..................................................................................... 4

2.3 Levantamientos Aerofotogramétricos ..................................................................... 7

2.3.1 Parámetros de vuelo ........................................................................................ 7

2.3.2 Parámetros de autocontrol .............................................................................. 8

2.3.3 Ejecución en terreno ........................................................................................ 8

2.3.4 Materialización de puntos de control .............................................................. 9

2.3.5 Vinculación de autocontrol y puntos de control: ........................................... 10

2.3.6 Levantamiento aerofotogramétrico ............................................................... 10

2.3.7 Equipos RPAS .................................................................................................. 10

2.4 Procesamiento de la información .......................................................................... 11

2.4.1 Control de calidad (data-log y fotografías) ..................................................... 11

2.4.2 Restitución Aerofotogramétrica digital .......................................................... 12

2.4.3 Precisión observada ........................................................................................ 13

2.4.4 Generación del modelo digital de elevación (DEM) ....................................... 14

2.4.5 Filtrado del DEM y generación de modelo digital de terreno (DTM) ............. 14

2.4.6 Control de calidad ........................................................................................... 15

3 Productos fotogramétricos ........................................................................................... 19

3.1 Nube de puntos ..................................................................................................... 19

3.2 MDT ........................................................................................................................ 20

3.3 Mosaico .................................................................................................................. 21

3.4 Curvas de nivel ....................................................................................................... 22

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **2** de **23**

### 1 Introducción

El presente documento contiene los aspectos técnicos del servicio ejecutado para CMP,

denominado “ _**Servicio de Levantamiento Aerofotogramétricos Mina Algarrobo**_ ”. El área

de estudio se emplaza a 32 km al Sureste de la comuna de Vallenar, Región de Atacama,

Chile.

En los siguientes acápites se detallan los alcances generales, parámetros técnicos, marcos

de referencias, cálculos y resultados obtenidos en el desarrollo del presente servicio.

##### 1.1 Objetivos

El objetivo establecido con el cliente previo al desarrollo del servicio, es la ejecución y

aplicación de un levantamiento de **1.005 hectáreas** de mediciones indirectas

( _**Aerofotogrametría con Drone**_ ). La aplicación de dicha técnica, tiene como fin obtener

productos topográficos y cartográficos de precisión, con los que CMP procederá a elaborar

diversos estudios ingenieriles en el área de trabajo.

##### 1.2 Antecedentes del proyecto

El área de estudio es denominada “Mina Algarrobo” cuya superficie comprende un área

total de **1.005 hectáreas** .

|ID|Superficie (hectáreas)|
|---|---|
|Área de estudio|1.005 ha|

_Tabla 1, Superficie de áreas de estudios._

_Ilustración 1, Ubicación de área de estudio._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **3** de **23**

### 2 Metodología de trabajo

Servicios INTOSIM Ltda., establece como metodología de trabajo para la ejecución de

“ _Servicios_ _de_ _levantamientos_ _aerofotogramétricos_ ”, lineamientos transversales,

emplazados en un mapa de proceso cuya aplicación nos permite generar una adecuada

trazabilidad de las diversas etapas del servicio a desarrollar. En dicho proceso se establecen

**5 actividades** y **12 tareas**, las cuales son transversales y se aplican como base de ejecución

de cualquier servicio que desarrolle nuestra empresa en este tipo de prestaciones. De esta

forma, ejercemos controles reactivos y anticipados, evitando posibles desviaciones en los

diversos procesos desarrollados.

A continuación, exponemos el mapa de proceso utilizado para la ejecución del servicio:

_Ilustración 2, Mapa de proceso del servicio._

##### 2.1 Parámetros del Proyecto

En la siguiente tabla, se menciona los parámetros técnicos asignados al proyecto y definidos

por el cliente previa ejecución del servicio:

|Escala|1:1000|
|---|---|
|**Proyección Cartográfica**|UTM, Huso 19 Sur|
|**Referencia altimétrica**|Modelo Geoidal EGM 08|
|**Datum**|WGS84 ≈ SIRGAS Y LOCAL|

_Tabla 2, Parámetros del proyecto._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **4** de **23**

##### 2.2 Puntos de Referencia

**2.2.1** **Red Geodésica.**

Para el presente servicio, se define que los trabajos deben estar vinculados al sistema

geodésico establecido por el Instituto geográfico Militar (IGM). Por lo que la red interna, los

levantamientos de medición directa y los productos resultantes de dichas mediciones, son

vinculados al sistema geodésico SIRGAS época 2021, y Re-proyectados cartográficamente a

la proyección Universal Transversal de Mercator (UTM) huso 19 Sur. En lo que respecta a

las elevaciones estas se encuentran referidas al nivel medio del mar, mediante la utilización

del modelo Geoidal global denominado “ **EGM 2008** ” en el caso de SIRGAS.

En los siguientes apartados se detalla la metodología empleada y los resultados obtenidos

en dicha vinculación.

**2.2.2** **Vinculación Geodésica.**

Con la finalidad de obtener coordenadas de precisión, referidas a un marco de referencia

geodésico regional, se procede a ejecutar observaciones mediante la utilización de técnicas

GNSS, en modo “Estático Post Proceso”. La vinculación se realiza desde el punto “ **HSCO** ”

(Huasco) y “ **LLCH** ” (Llanos de Challe) estaciones activas perteneciente a la red geodésica

continental SIRGAS, junto con los vértices “ **ALG1** ” y “ **ALG2** ” los cuales se encuentran dentro

del área de estudio.

Las coordenadas informadas por el **IGM**, para las estaciones activas utilizadas corresponden

a las señaladas en las ilustraciones 3 y 4.

_Ilustración 3, Certificado estación Activa LLCH IGM._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **5** de **23**

_Ilustración 4, Certificado estación Activa HSCO IGM._

En la ilustración 5, se representa la disposición espacial de la Red Primaria planificada y

desarrollada para el servicio.

_Ilustración 5, Disposición espacial RED Primaria GNSS._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **6** de **23**

En la Ilustración 5, se puede observar que se utilizan como vértices de referencia geodésico

las estaciones activas ya señaladas. Dichas estaciones (vértices) se encuentran cercanas al

área de estudio, esto permite utilizarlas para formar figuras geométricas con el fin de

evaluar los errores de cierre y determinar ajustes que impliquen mayor precisión en la

obtención de coordenadas.

Las observaciones se desarrollan mediante la utilización de sistemas GNSS de la clase

geodésicos, aplicando el modo Estático Post-Proceso. Cada observación fue ejecutada al

menos en dos sesiones (Método multisesión) con un mínimo de 5 horas de observación. La

planificación de esta metodología de trabajo permite aumentar la redundancia en la

medición y así mitigar desviaciones en el procesamiento de las diversas líneas base.

A continuación, presentamos los resultados del procesamiento de líneas base generado en

el **Software TBC** :

_Tabla 3. líneas base Red geodésica Algarrobo._

Los resultados obtenidos del procesamiento de las líneas base, mediante el software de

postproceso de datos GNSS, son aceptables y están dentro de los parámetros esperados

para la RED Geodésica implementada. Sin embargo, con el objetivo de asegurar la calidad

interna de la red, se procede a realizar un análisis de cierre de figuras geométricas GNSS, el

cual arroja los siguientes resultados:

|ID del<br>punto de<br>origen|Al ID punto|ΔX (Metros)|ΔY (Metros)|ΔZ(Metros)|Distancia Elip.<br>(Metros)|
|---|---|---|---|---|---|
|ALG2|ALG1|-1328.3241|186.69|-1058.1371|1708.4942|
|LLCH|ALG2|-1188.8961|33364.3568|-60750.7089|69319.8558|
|HSCO|ALG1|15613.1368|24485.4002|-35456.3877|45830.7789|
|LLCH|HSCO|-18130.3566|9065.6395|-26352.4591|33246.7705|
|∑ <br>**-0.0004 **<br>**0.0071 **<br> <br> <br> <br> <br> <br> <br> <br>|∑ <br>**-0.0004 **<br>**0.0071 **<br> <br> <br> <br> <br> <br> <br> <br>|**-0.0004 **|**0.0071 **|**0.0008 **|**150105.8994 **|
|∑ <br>**-0.0004 **<br>**0.0071 **<br> <br> <br> <br> <br> <br> <br> <br>|∑ <br>**-0.0004 **<br>**0.0071 **<br> <br> <br> <br> <br> <br> <br> <br>|**-0.0004 **|**0.0071 **|**Error de Cierre**|**0.007**|
|∑ <br>**-0.0004 **<br>**0.0071 **<br> <br> <br> <br> <br> <br> <br> <br>|∑ <br>**-0.0004 **<br>**0.0071 **<br> <br> <br> <br> <br> <br> <br> <br>|**-0.0004 **|**0.0071 **|**PPM**|**0.048**|

_Tabla 4. Control de cierre de figuras sesión 1._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **7** de **23**

|ID del<br>punto de<br>origen|Al ID punto|ΔX (Metros)|ΔY (Metros)|ΔZ(Metros)|Distancia Elip.<br>(Metros)|
|---|---|---|---|---|---|
|ALG2|ALG1|-1328.3195|186.6816|-1058.1462|1708.4952|
|LLCH|ALG2|-1188.9058|33364.3658|-60750.6964|69319.8493|
|HSCO|ALG1|15613.1457|24485.39|-35456.3969|45830.7836|
|LLCH|HSCO|-18130.358|9065.6443|-26352.4552|33246.7695|
|∑ <br>**-0.0130**<br>**0.0131**<br> <br> <br> <br> <br> <br> <br> <br>|∑ <br>**-0.0130**<br>**0.0131**<br> <br> <br> <br> <br> <br> <br> <br>|**-0.0130**|**0.0131**|**0.0095**|**150105.8976**|
|∑ <br>**-0.0130**<br>**0.0131**<br> <br> <br> <br> <br> <br> <br> <br>|∑ <br>**-0.0130**<br>**0.0131**<br> <br> <br> <br> <br> <br> <br> <br>|**-0.0130**|**0.0131**|**Error de Cierre**|**0.021**|
|∑ <br>**-0.0130**<br>**0.0131**<br> <br> <br> <br> <br> <br> <br> <br>|∑ <br>**-0.0130**<br>**0.0131**<br> <br> <br> <br> <br> <br> <br> <br>|**-0.0130**|**0.0131**|**PPM**|**0.138**|

_Tabla 5. Control de cierre de figuras sesión 2._

Aceptado el procesamiento, y en función del análisis presentado respecto de su calidad

interna, se demuestra que los cierres de figuras geométricas cumplen con creces lo

establecido en el numeral **2.307.203-B** del Manual de Carreteras **Volumen 2**, en el cual se

indica como tolerancia de cierre lineal para el Orden Primario de **STC 1:40.000** (25 PPM). En

consecuencia, se considera validado el resultado del procesamiento, el cual es apto para el

ajuste final y cálculo de las coordenadas definitivas.

Las comprobaciones realizadas en los procesos anteriores son aceptables y están dentro de

los parámetros esperados, aun así, pueden ser mejoradas mediante la aplicación de

métodos de ajustes por mínimos cuadrados. El ajuste de la RED es posible de realizar,

debido a que las líneas base generadas tienen la particularidad de contar con redundancia

en sus observaciones, por lo que la red es susceptible al ajuste y, en consecuencia, se puede

distribuir el error de los vectores observados mediante la aplicación del método ChiCuadrado.

|Ajuste de coordenadas GNSS RED Primaria|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID Punto **|**Este **|**Este σ **|**Norte **|**Norte σ **|**Elevación **|**Elevación σ **|
|BN03|368260.887|0.001|6971934.800|0.001|386.555|0.003|
|HM-BAG|363636.559|0.001|6994074.420|0.001|1105.361|0.006|
|UDAT|366039.887|-|6973269.080|-|373.786|-|

_Tabla 6, Ajuste de coordenadas Red Primaria._

##### 2.3 Levantamientos Aerofotogramétricos

**2.3.1** **Parámetros de vuelo**

Previo al desarrollo de las actividades en terreno, se realiza una planificación con el plan de

vuelo a ejecutar, iniciando con la definición del sistema aéreo no tripulado (RPAS) a utilizar

en el proyecto. Se determina que la mejor opción para desarrollar la solicitud es utilizar la

plataforma **Wingtra One** ya que esta tiene la capacidad de obtener una optimización y

eficiencia abarcando una gran cobertura de terreno en tiempos acotados, dicha descripción

se adapta a las condiciones reales donde se desarrolla el levantamiento. Posteriormente se

definen las áreas o zonas de interés, analizando la información cartográfica disponible de

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **8** de **23**

las áreas de estudios. A partir de este análisis se definen los valores del GSD (Resolución

promedio) requerida como máximo para el proyecto y los traslapes pertinentes. Los valores

determinados para las áreas de estudio se exponen en la tabla 7.

|Área de estudio|Col2|
|---|---|
|**Resolución promedio (GSD)**|5 cm/píxel (Altura máximo de 120 m)|
|**Traslape Transversal**|70%|
|**Traslape longitudinal**|80%|

_Tabla 7, Parámetros de vuelos Generales._

**Nota:** Tanto para la planificación, como para la ejecución de los vuelos aerofotogramétricos,

se utilizó el software **Wingtra Hub** .

**2.3.2** **Parámetros de autocontrol**

INTOSIM, define como parte del proceso de ejecución de servicios aerofotogramétricos,

métodos de control que se orientan a la validación de datos mediante la comparación de

distintas técnicas, como lo es la aerofotogrametría (medición indirecta) y las observaciones

GNSS (Medición directa).

El método de control consta en establecer puntos foto identificables, los cuales son

distribuidos y materializados dentro del área de estudio. La materialización de dichos

puntos se realiza con la utilización de cal, dejando marcas que tienen dimensiones de 2 x 2

m. Una vez materializadas las marcas, se procede con el registro de sus coordenadas (X, Y,

Z) mediante instrumental GNSS en modalidad Cinemática Postproceso. Es importante

mencionar que el proceso aerofotogramétrico ejecutado en el presente estudio, se

desarrolla con instrumental de alta gama, como lo es el Wingtra One, el que cuenta con la

particularidad de integrar un sistema GNSS. Este punto es muy relevante ya que, al contar

con este tipo de sensores, no es necesario el desarrollo de puntos de apoyo fotogramétricos

y solo se requieren puntos de control, los que son utilizados como elementos que validan

el modelo generado a partir de la fotogrametría.

**2.3.3** **Ejecución en terreno**

La ejecución de los trabajos en terreno se desarrolla el **11 de noviembre de 2021**, conforme

a lo planificado. Los trabajos se ejecutan de manera normal, cumpliendo todos los

procedimientos y protocolos establecidos.

En los siguientes apartados se detallan las actividades realizadas en terreno y los resultados

del procesamiento de los productos.

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **9** de **23**

**2.3.4** **Materialización de puntos de control**

Se establecen puntos de control, los cuales se materializan en las diversas áreas de estudio.

En la ilustración 6, se grafica la distribución de los puntos de control acorde a lo antes

descrito.

_Ilustración 6, Distribución de puntos de control._

_Ilustración 7, Ejemplo de visualización de punto de control._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **10** de **23**

**2.3.5** **Vinculación de autocontrol y puntos de control:**

Tal como se ha indicado, la vinculación de los puntos de control y el levantamiento

aerofotogramétrico se realiza a partir de los HM mediante observaciones GNSS. Los puntos

de autocontrol se realizan utilizando el método estático Post Proceso.

**2.3.6** **Levantamiento aerofotogramétrico**

La actividad de levantamiento aerofotogramétrico fue ejecutada acorde a lo establecido en

la planificación de vuelo y a lo descrito en el punto 2.3 del presente informe. Los equipos

de operación se mantienen alerta a las condiciones del clima, además, previo a cada vuelo,

se realiza una revisión del correcto funcionamiento de todos los componentes de los

sistemas RPAS y de la cámara, asegurando en todo momento que la captura y el registro de

información sea óptimo.

**2.3.7** **Equipos RPAS**

En el siguiente apartado se describen las características técnicas de los equipos RPAS

utilizado en el desarrollo del servicio.

**Wingtra One RX1RII** es un vehículo aéreo no tripulado, diseñado principalmente para

mapeo y topografía, ya que permite levantamientos topográficos más rápidos a través de

la toma de imágenes aéreas. Con el se puede abarcar grandes áreas, su desempeño máximo
puede llegar a ser de 400 hectáreas a 3 cm/Píxel, lo que se traduce en 10 veces más que un

dron convencional.

Este equipo cuenta con un tiempo de vuelo de 55 minutos, un alcance de vuelo de hasta 50

km y un mecanismo eficiente que garantiza un vuelo inteligente. Su envergadura de ala es

de 125 cm y Pesa 3.7 kg (vacío). Incluye módulo y receptor PPK para una mejor precisión.

Wingtra One PPK establece el nuevo punto de referencia para los equipos de drones de
topografía. Gracias al receptor profesional PPK GNSS L1/L2 del dron y cámaras de la más

alta calidad, como la cámara Sony RX1RII de fotogramas completos de 42 MP, es posible

alcanzar una exactitud rigurosa de hasta 1 cm con un dron de fotografía aérea.

Este equipo posee la particularidad de realizar despegue y aterrizaje vertical (VTOL), lo que

permite que pueda despegar de manera vertical como un multirotor o helicóptero pero

luego realiza una transición de crucero hacia adelante para llevar a cabo el vuelo como un

avión o dron de ala fija, las ventajas de esta tecnología de aterrizaje vertical permite

estacionar el dron en áreas tan pequeñas como 2 metros x 2 metros, ya sea en barcos o

caminos estrechos donde desciende o aterriza de forma autónoma o manual.

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **11** de **23**

##### 2.4 Procesamiento de la información

Esta etapa se realiza por completo en gabinete con equipos computacionales de alto

desempeño, los cuales permiten procesar gran cantidad de información en tiempos más

acotados.

En los siguientes apartados se detallan las etapas correspondientes al procesamiento de

información.

**2.4.1** **Control de calidad (data-log y fotografías)**

Una etapa relevante del proceso es la validación de la información obtenida en terreno. Es

por ello, que los datos pasan por un proceso de vinculación y comprobación. Dicho proceso

es realizado en el software **WingtraHub** para el procesamiento de las fotografías obtenidas

por Wingtra One en donde se comprueba la integridad de los fotogramas y se verifica la

coincidencia con el archivo data-log (información de registro del vuelo ejecutado). Tanto las

fotografías como los archivos de data-Log son concordantes, y además el procesamiento de

vinculación entrega residuales menores a 4 cm, por lo que el levantamiento

aerofotogramétrico es validado al 100%.

_Ilustración 8: Sistema Wingtra One._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **12** de **23**

_Ilustración 9. Comprobación y validación del vuelo._

**2.4.2** **Restitución Aerofotogramétrica digital**

La restitución digital o etapa de Aero-triangulación tiene por objetivo resolver las incógnitas

de posicionamiento de la cámara al momento de la obtención del fotograma. El

procedimiento consiste en unir cada fotograma y determinar puntos de paso (puntos

comunes entre cada fotograma), los que permiten generar una verificación a la

georreferenciación del proceso aerofotogramétrico, y además obtener los ángulos de Pich

(Cabeceo) Roll (Alabeo) Yaw (Guiñado). Obtenidos estos valores, se resuelven las incógnitas

y se procede con la restitución digital. Cabe señalar que la cantidad de puntos de paso

determinados por el software de restitución depende directamente de la calidad de las

imágenes, que, para el presente caso, correspondiente al levantamiento de Algarrobo

estuvieron por debajo de los valores mínimos, obteniendo _715,665_ puntos de paso.

Un punto relevante en el procesamiento es el nivel de traslape longitudinal y transversal

obtenido, dado que de estos valores depende la calidad de los productos fotogramétricos.

A continuación, se grafican a modo de ejemplo los traslapes obtenidos para el área

denominada “ **Algarrobo** ”.

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **13** de **23**

_Ilustración 10, Ubicación de fotogramas capturados y traslapes obtenidos._

Como es posible observar en la Ilustración 10, la escala de colores indica el porcentaje de

traslape generado sobre el área de interés (Azul traslape eficiente, Rojo traslape deficiente),

lo que permite asegurar el cumplimiento de los parámetros establecidos en términos de

traslapes longitudinales de un 80% y transversales de 70%, por lo que el procesamiento es

apto y se ajusta a los valores esperados en cada uno de los levantamientos.

**2.4.3** **Precisión observada**

En la siguiente tabla, se presentan las precisiones observadas sobre los centros de

proyección de **3048** fotogramas de “ **Algarrobo** ”.

_Tabla 8, Precisión promedio observada sobre 3048 centros de proyección “Algarrobo”._

Actualmente no existe un marco de referencia específico que regule o valide los procesos

fotogramétricos en la industria minera. Aun así, en Chile existe el Manual de Carreteras Vol.

II, que regula y estructura muy rigurosamente todo lo relacionado a estudios topográficos

y geodésicos en el ámbito vial. En dicho documento se establece en el numeral 2.304.303.A,

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **14** de **23**

concerniente a servicios ejecutados con tecnologías aéreas no tripuladas, las tolerancias

admisibles para la aceptación de procesos aerofotogramétricos se muestra en la ilustración

11.

_Ilustración 11, Tolerancias Restituciones Aerofotogramétricas, Manual de Carreteras._

**Nota:** Es importante destacar que los valores obtenidos se encuentran muy por debajo de

lo establecido en el manual de carreteras. Esto nos permite asegurar productos confiables

y de alta exactitud y precisión.

**2.4.4** **Generación del modelo digital de elevación (DEM)**

Luego de finalizar la etapa de aerotringulación, se procede a generar la nube de puntos XYZ,

la cual, es desarrollada a través de estereoscopía digital. El procedimiento consiste en

reutilizar el resultado de la aerotringulación, que contiene los datos de orientación de las

imágenes y que permite trabajar con los estereopares. El módulo 3D del software permite,

utilizando los parámetros correctos obtenidos del análisis estereoscópico y gracias al gran

traslape que presentaron las imágenes, generar un modelo 3D. Los puntos XYZ se someten

a una etapa de selección, donde se procede a eliminar el “ruido” del modelo y controlar su

altura con respecto a los puntos de control.

Finalizada la etapa de modelamiento y construcción del DEM, se procede con la generación

del ortofoto definitivo y posterior mosaico. Para ello, cada imagen es ortorectificada píxel a

píxel utilizando el DEM como información base.

Luego que cada imagen por separado está ortorectificada, se elabora el mosaico en donde

se realiza un trabajo de unión de cada ortofoto, obteniendo como resultado un mosaico

homogéneo y completo de la zona de estudio.

**2.4.5** **Filtrado del DEM y generación de modelo digital de terreno (DTM)**

Una vez obtenido el DEM y la nube de puntos definitiva, comienza la etapa de generar el

Modelo Digital de Terreno (DTM), este elemento tiene la característica de mostrar el

modelamiento del terreno, clasificando las edificaciones, vegetación y otros objetos, las que

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **15** de **23**

son omitidas para facilitar la generación de las curvas de nivel. Para ello se utiliza el software

METASHAPE con la herramienta de trabajo “clasificación de puntos”, en donde la nube de

puntos es “refinada”, logrando definir el DTM.

_Ilustración 12, Clasificación de nube de puntos._

**2.4.6** **Control de calidad**

Una vez generados los productos, se realiza un control del modelo digital de terreno, con el

fin de corroborar que las elevaciones restituidas se encuentran dentro de las tolerancias

para la escala de precisión del proyecto. En este control, se utiliza información de puntos

tomados en terreno mediante sistema GNSS en modo Cinemático Postproceso (medición

directa) y se compara con el DEM resultante del proceso aerofotogramétrico (medición

indirecta).

Tal como se menciona anteriormente, se realiza un levantamiento de autocontrol en

terreno, el cual arroja los siguientes resultados:

|Autocontrol|Col2|
|---|---|
|**Desviación Estándar ± (m)**|0.09|
|**Promedio (m)**|0.01|
|**Tamaño de la muestra (N ° Puntos)**|52|
|**Residual Mínimo (m)**|-0.162|
|**Residual Máximo (m)**|0.179|
|**Varianza (m)**|0.009|
|**Porcentaje dentro de tolerancia 1:500**|100%|
|**Porcentaje fuera de tolerancia 1:500**|0%|

_Tabla 9, parámetros Autocontrol._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **16** de **23**

**-0.30** **-0.25** **-0.20** **-0.15** **-0.10** **-0.05** **0.00** **0.05** **0.10** **0.15** **0.20** **0.25** **0.30**

_Ilustración 13, Campana de Gauss._

_Ilustración 14, Distribución residual de los Puntos de Autocontrol._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **17** de **23**

0.50

0.30

0.10

-0.10

-0.30

-0.50

PA01 PA04 PA07 PA10 PA13 PA16 PA19 PA22 PA25 PA28 PA31 PA34 PA37 PA40 PA43 PA46 PA49 PA52

Puntos de control

_Ilustración 15, Valores de residuales observados en autocontrol._

El método de autocontrol realizado, valida la calidad del proceso fotogramétrico,

entregándonos como resultado una desviación por debajo de lo requerido por el manual de

carreteras (-25 a +25cm) de exactitud, el cual está dentro de los parámetros establecidos y

esperados para el proyecto.

INTOSIM establece métodos comparativos (mediciones directas e indirectas), con el

objetivo de acercar la exactitud y precisión de los productos generados, entendiendo y

teniendo como base las siguientes definiciones:

 - **Exactitud:** ¿Qué tan cercano está el valor medido respecto al valor verdadero?

 - **Precisión:** ¿Qué tan cercanos se ubican entre los valores calculados?

A continuación, se presenta un ejemplo que grafica la diferencia de las definiciones antes

expuestas:

_Ilustración 16, Ejemplo de precisión y exactitud._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **18** de **23**

_Ilustración 17, Representación de nivel de exactitud y presión de los modelos fotogramétricos controlados._

De la ilustración 17 presentada es posible concluir que, los productos resultantes de la

restitución Aerofotogramétrica (medición indirecta) se encuentran bastante cercanos al

valor real (medición directa) y cumple con lo estipulado para la escala comprometida para

el desarrollo del presente proyecto.

Con ello, se concluye que el levantamiento topográfico generado cumple las tolerancias

exigidas para levantamientos a escala 1:500, esto acorde a lo establecido en el Manual de

Carreteras tabla 2.304.303.A.

_Ilustración 18, Tolerancia admisibles._

Posterior a la comprobación del control de calidad, y luego de haber aprobado la nube de

puntos y modelo digital de terreno, se procede a la generación del resto de los productos

comprometidos para el presente servicio.

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **19** de **23**

### 3 Productos fotogramétricos

Para la generación de los productos, son considerados los siguientes parámetros técnicos:

 - Proyección Cartográfica, UTM 19 SUR.

 - Sistema Geodésico SIGAS 2000 ≈ WGS84 y PASAD 56.

 - Referencia de elevaciones, Nivel Medio del Mar EGM08.

##### 3.1 Nube de puntos

Se entrega un archivo en formato “LAS” correspondiente a la nube de puntos. Los archivos

que tienen formato LAS, además de poseer las coordenadas y cota de cada punto, incluyen

tres valores RGB los cuales permiten visualizar las elevaciones de terreno en términos

gráficos.

_Ilustración 19, Nube de puntos generada._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **20** de **23**

##### 3.2 MDT

Modelo digital de terreno (MDT): este modelo fue generado a partir de la nube de puntos

filtrada y utilizado para la generación de curvas de nivel.

_Ilustración 20, Modelo Digital de Terreno obtenido en función del proceso de restitución digital._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **21** de **23**

##### 3.3 Mosaico

El mosaico generado posee las siguientes características:

➢ Mosaico georreferenciado en formato GeoTiff de 24 bits.
➢ Tamaño promedio de píxel 5 cm.

_Ilustración 21, Mosaico generado._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)

**SERVICIOS INTOSIM LTDA. |** Soluciones en Geoinformación | Página **22** de **23**

##### 3.4 Curvas de nivel

Las curvas de nivel se generaron cada 1 metros, con curvas índices cada 5 metros. El archivo

se entrega en formato DWG, para que pueda ser utilizado en cualquier plataforma de

AutoCAD o similar. Cada curva es una polilínea con altura, lo que permite visualizar el relieve

del área de interés.

_Ilustración 22, Curvas de nivel generadas representativas._

[www.intosim.cl | contacto@intosim.cl | 051-2677230](mailto:contacto@intosim.cl)