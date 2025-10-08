---
title: PROYECTO PARQUE LLANOS DEL SOL
author: ENIETO
date: D:20240625122158-04'00'
language: es
type: report
pages: 35
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Memoria Hidráulica
-->

## PROYECTO PARQUE FOTOVOLTAICO LLANOS DEL SOL

#### _APÉNDICE 03_ _MEMORIA MODELACIÓN_ _HIDRÁULICA - PAS 157_

_Junio, 2024_

**Hoja de control de calidad**

Documento MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

**Proyecto** **PROYECTO PARQUE FOTOVOLTAICO LLANOS DEL SOL**

Código SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA

Autores: Firma: CRM JTP JTP DMJ

Fecha: 22/04/2024 30/05/2024 19/06/2024 25/06/2024

Verificado Firma: CNU CNU CNU CNU

Fecha: 22/04/2024 30/05/2024 19/06/2024 25/06/2024

Cliente Llanos del Sol SpA

Notas

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 2 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

### Índice

Hoja de control de calidad ............................................................................................................................................................ 2

Índice ............................................................................................................................................................................................ 3

Memoria Hidráulica ...................................................................................................................................................................... 6

1. Introducción ............................................................................................................................................................................ 6

1.1 Emplazamiento ................................................................................................................................................................. 6

2. Antecedentes ........................................................................................................................................................................... 7

2.1 Hidrología ......................................................................................................................................................................... 7

3. Modelación Hidráulica ........................................................................................................................................................... 9

3.1 Dominio Computacional ................................................................................................................................................... 9

3.2 Características Geométricas del Modelo ........................................................................................................................... 9

3.3 Coeficiente de Rugosidad ................................................................................................................................................. 9

3.4 Condiciones de contorno................................................................................................................................................. 12

3.5 Parámetros de obras propuestas ...................................................................................................................................... 14

4. Resultados de Modelación .................................................................................................................................................... 15

4.1 Resultados de modelamiento hidráulico sin proyecto - TR 100 ..................................................................................... 15

4.2. Resultados de modelamiento hidráulico sin proyecto - TR 150 ............................................................................... 17

**4.3. Resultados de modelamiento hidráulico con proyecto - TR 100** ............................................................................. 19

**4.4. Resultados de modelamiento hidráulico con proyecto - TR 150** ............................................................................. 22

4.5 Situación CP en descarga del canal perimetral ............................................................................................................... 25

5. Diseño de obras ...................................................................................................................................................................... 32

6. Conclusiones y Comentarios .................................................................................................................................................. 34

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 3 de 34

### Índice de Tablas

Tabla No 1 Caudal líquido de cuencas aportantes. ........................................................................................................................ 8
Tabla No 2 Caudal detrítico de cuencas aportantes. ...................................................................................................................... 8
Tabla No 3 Coeficientes de Rugosidad. ...................................................................................................................................... 12
Tabla No 4 Datos cuencas aportantes. ......................................................................................................................................... 13
Tabla No 5 Caudales líquidos y detríticos. .................................................................................................................................. 13

Tabla No 6 Caudales del modelo. ................................................................................................................................................ 13

Tabla No 7 Caudales del parque para el modelo. ........................................................................................................................ 14

Tabla No 8 Velocidades Máximas Admisibles. ........................................................................................................................... 15

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 4 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

### Índice de Figuras

Figura No 1 Emplazamiento del Parque Llanos del Sol. ............................................................................................................... 6
Figura No 2 Emplazamiento canal perimetral. ............................................................................................................................. 7
Figura No 3 Cuencas aportantes al proyecto. ................................................................................................................................ 7
Figura No 4 Características de geometría de modelo hidráulico. .................................................................................................. 9
Figura No 5 Visita de campo - material de la quebrada Guatacondo. ......................................................................................... 10
Figura No 6 Cobertura de suelo de la zona de estudio. ............................................................................................................... 11
Figura No 7 Condición de contorno del dominio computacional. ............................................................................................... 12
Figura No 8 Tirante de agua en el dominio hidráulico para un TR 100. ..................................................................................... 15
Figura No 9 Tirante de agua en el límite del parque solar para un TR 100. ................................................................................ 16
Figura No 10 Velocidad en el dominio hidráulico para un TR 100. ............................................................................................ 16
Figura No 11 Velocidad en el límite de la planta solar para un TR 100. ..................................................................................... 17
Figura No 12 Tirante de agua en el dominio hidráulico para un TR 150. ................................................................................... 17
Figura No 13 Tirante de agua en el límite de la planta solar para un TR 150.............................................................................. 18
Figura No 14 Velocidad en el dominio hidráulico para un TR 150. ............................................................................................ 18
Figura No 15 Velocidad en el límite de la planta solar para un TR 150. ..................................................................................... 19
Figura No 16 Tirante de agua en el dominio hidráulico para un TR 100. ................................................................................... 19
Figura No 17 Tirante de agua en el límite del parque solar para un TR 100. .............................................................................. 20
Figura No 18 Eje hidráulico en el canal perimetral del parque solar para un TR 100. ................................................................ 20
Figura No 19 Velocidad en el dominio hidráulico para un TR 100. ............................................................................................ 21
Figura No 20 Velocidad en el límite de la planta solar para un TR 100. ..................................................................................... 21
Figura No 21 Velocidad en el canal perimetral de la planta solar para un TR 100. .................................................................... 22
Figura No 22 Tirante de agua en el dominio hidráulico para un TR 150. ................................................................................... 22
Figura No 23 Tirante de agua en el límite de la planta solar para un TR 150.............................................................................. 23
Figura No 24 Eje hidráulico en el canal perimetral de la planta solar para un TR 150. ............................................................. 23
Figura No 25 Velocidad en el dominio hidráulico para un TR 150. ............................................................................................ 24
Figura No 26 Velocidad en el límite de la planta solar para un TR 150. ..................................................................................... 24
Figura No 27 Velocidad en el canal perimetral de la planta solar para un TR 150. .................................................................... 25
Figura No 28 Eje hidráulico en el perfil longitudinal de descarga. ............................................................................................. 25
Figura No 29 Velocidad en el perfil longitudinal de descarga..................................................................................................... 26
Figura No 30 Velocidad en el perfil longitudinal de la defensa fluvial. Arriba modelo sin proyecto y abajo con proyecto. ...... 27
Figura No 31 Tirante de agua en el perfil longitudinal de la defensa fluvial en sector aguas arriba. .......................................... 28
Figura No 32 Tirante de agua en el perfil longitudinal de la defensa fluvial en sector aguas abajo. ........................................... 29
Figura No 33 Velocidad en el perfil longitudinal de la defensa fluvial en sector aguas arriba. ................................................... 30
Figura No 34 Velocidad en el perfil longitudinal de la defensa fluvial en sector aguas abajo. ................................................... 31
Figura No 35 Sección de descarga. Vista en planta (arriba) y sección longitudinal (abajo). ....................................................... 32
Figura No 36 Corte Transversal Canal Perimetral. ...................................................................................................................... 33
Figura No 37 Defensa fluvial en sector norte del parque. ........................................................................................................... 33

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 5 de 34

# Memoria Hidráulica

**1.** **Introducción**

El presente documento corresponde a la modelación hidráulica de la obra de descarga del canal perimetral incluido en el PAS
155, así como también, a la defensa fluvial emplazada en la ribera del cauce principal de la cuenca Guatacondo. Lo anterior se
realiza en el marco del cumplimiento con el Permiso Ambiental Sectorial (PAS) 157 para el proyecto Parque Fotovoltaico
Llanos del Sol. La finalidad del presente estudio es definir el diseño de las obras permitiendo el flujo de la escorrentía que se
forma en las quebradas durante eventos de precipitación.

La modelación se realiza mediante el software HEC-RAS V6.4.1, en este informe se presentan los parámetros empleados en la
modelación del acueducto proyectado, en función a las áreas aportantes en base al estudio hidrológico del presente estudio

incluido en el documento “SP1150-LLANOS-PAS157-AN-02-SP-HIDROLOGIA”.

**1.1 Emplazamiento**

El proyecto Parque Fotovoltaico Llanos del Sol se emplaza en la comuna de Pozo Almonte, provincia del Tamarugal, Región
de Tarapacá a unos 180 kilómetros al sureste de la ciudad de Iquique. En la Figura N°1 se presenta la ubicación del proyecto.

_Figura No 1 Emplazamiento del Parque Llanos del Sol._

_Fuente: Elaboración Propia._

En la Figura No2 se muestran las obras proyectadas y su ubicación respecto al área del Proyecto. Se presenta, en particular, la
obra de descarga y la defensa fluvial relativa al PAS 157.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 6 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

_Figura No 2 Emplazamiento canal perimetral._

_Fuente: Elaboración Propia._

En la imagen anterior se muestran distintas obras de las cuales el canal perimetral pertenece al PAS 155, y la defensa fluvial o
pretil y la descarga al presente PAS 157

**2.** **Antecedentes**

**2.1 Hidrología**

Como base para la modelación hidráulica del Proyecto se utiliza lo desarrollado en el estudio de hidrología, la cual se muestra
en el Apéndice 02 “SP1150-LLANOS-PAS155-AN-02-SP-HIDROLOGIA”. En el estudio se determinan los parámetros
morfológicos de las dos cuencas con influencia directa en la zona de desarrollo del proyecto, las que se muestran a continuación.

_Figura No 3 Cuencas aportantes al proyecto._

_Fuente: Elaboración Propia._

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 7 de 34

Con el propósito de considerar el efecto producto del arrastre de sedimentos, los caudales determinados en el estudio hidrológico
(ver tabla N°1) fueron amplificados considerando una concentración volumétrica de material detrítico de acuerdo a lo
establecido en la “Guías Metodológicas para Presentación y Revisión Técnica de Proyectos de Modificación de Cauces
Naturales y Artificiales” de la Dirección General de Aguas, donde se establece la siguiente expresión:

Q l
Q d = 1 −C v

Donde:

Q d : Caudal detrítico (m [3] /s)
Q l : Caudal líquido (m [3] /s)
C v : Concentración en volumen de sólidos

Considerando una concentración volumétrica del 40%, en función a las recomendaciones establecidas en el citado documento,
se determinan los caudales detríticos presentados en la

**2** 50,46 1,54

**5** 111,38 3,38

**10** 171,08 5,23

**25** 260,46 7,54

**50** 301,38 8,46

**100** 478,31 11,38

**150** 726,00 14,92

**200** 1051,54 17,23

Tabla No 2.

Se consideran aportes que pudieran afectar el parque las cuencas Guatacondo y S/N:

**2** 32,80 1,00

**5** 72,40 2,20

**10** 111,20 3,40

**25** 169,30 4,90

**50** 195,90 5,50

**100** 310,90 7,40

**150** 471,90 9,70

**200** 683,50 11,20

_Tabla No 1 Caudal líquido de cuencas aportantes._

_Fuente: Elaboración Propia._

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 8 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

**2** 50,46 1,54

**5** 111,38 3,38

**10** 171,08 5,23

**25** 260,46 7,54

**50** 301,38 8,46

**100** 478,31 11,38

**150** 726,00 14,92

**200** 1051,54 17,23

_Tabla No 2 Caudal detrítico de cuencas aportantes._

_Fuente: Elaboración Propia._

**3.** **Modelación Hidráulica**

Para la modelación hidráulica de las obras se realizó mediante el software de libre acceso HEC-RAS V.6.4.1 desarrollado por
el US Corp Engineers.

**3.1 Dominio Computacional**

El dominio computacional se definió en función a la disponibilidad la topografía compartida por el cliente, la misma que pasó
por un control de calidad exhaustivo a fin de minimizar los errores de convergencia del modelo hidráulico.

**3.2 Características Geométricas del Modelo**

Las características de la geometría del dominio computacional estuvieron definidas por generación de la malla computacional,
condiciones hidrológicas y condiciones de contorno. La malla utilizada fue de tipo rectangular de 40 m en todo el dominio y
con refinamientos de los cauces principales mediante líneas de rotura con mallas tipo octogonales de 1 m y gradación de 5 m
para un mejor reacondicionamiento al empalmar con las mallas de 40 m.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 9 de 34

_Figura No 4 Características de geometría de modelo hidráulico._

_Fuente: Elaboración Propia._

La misma malla computacional se utiliza para el modelo con proyecto. Para la geometría del canal perimetral se utilizó el
levantamiento topográfico digital disponible, estableciendo pendientes representativas en función a las pendientes existentes en
el terreno, con el fin de minimizar movimientos de tierra como cortes de terreno requeridos. En cuanto a la sección transversal
del canal, se establece de forma preliminar una sección trapecial con 1,5 m. de base y talud 1:1 (H:V).

**3.3 Coeficiente de Rugosidad**

Para la obtención de unos valores lo más aproximados a la realidad se recopiló una extensa información fotográfica del cauce.
Se aprecia en la visita, que los suelos del parque están compuestos en su mayoría por materiales arenosos de composición gruesa
en superficie y compuestos además de una matriz de limos arcillosos de baja plasticidad aparente (Ver Figura No 5), esta
composición a medida que se profundiza va tomando mayor compacidad y, por ende, una menor capacidad de infiltración. El
material identificado en los suelos del parque y alrededores otorga una compacidad media, además se evidencia que los suelos
han sufrido efecto de compactación hidráulica, posiblemente por eventos de tormenta e inundación presentes en el parque.
Además, no se ha evidenciado ningún tipo de vegetación (suelo desnudo).

_Figura No 5 Visita de campo - material de la quebrada Guatacondo._

_Fuente: Elaboración Propia._

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 10 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

En concreto, se ha utilizado la clasificación de tramos fluviales propuesta por Cowan, que permite, mediante una sencilla
formulación, obtener el número de rugosidad de Manning. De esta forma:

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) ∗m 5

Donde:

`o` n 0 depende del material que conforma el lecho
`o` n 1 depende del grado de irregularidad del lecho
`o` n 2 depende del tipo de variación de la sección transversal
`o` n 3 depende del efecto relativo de obstrucciones
`o` n 4 depende de tipo de vegetación existente
`o` m 5 es función de la cantidad de meandros

En el siguiente cuadro se muestra los valores de los coeficientes de la formulación de Cowan.

De acuerdo con el cuadro se ha formulado y obtenido el coeficiente de rugosidad característico para la quebrada en estudio.

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) ∗m 5

n= (0.020 + 0.005 + 0.000 + 0.000 + 0.005) ∗1.000 = 0.030

Asimismo, de manera complementaria, el manual del usuario del HEC-RAS también sugiere valores de Manning para
diferentes coberturas de suelo. El manual presenta los siguientes valores referenciales:

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 11 de 34

Para la verificación del tipo de cobertura de suelo se utilizó la base de datos mundial de la ESA (European Space Agency):

 https://viewer.esa [worldcover.org/worldcover/](https://viewer.esa-worldcover.org/worldcover/)

_Figura No 6 Cobertura de suelo de la zona de estudio._

_Fuente: Elaboración Propia._

A partir del tipo de cobertura de suelo y las tablas sugeridas por el Manual de HEC-RAS se estima un valor medio de coeficiente
de rugosidad de Manning de 0,027. Finalmente, se optó por utilizar el valor más conservado **n= 0.03** obtenido a partir de la
formulación de Cowan y validado con la tabla del Manual de HEC-RAS.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 12 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

Para las obras proyectadas se consideran los siguientes coeficientes de rugosidad de Manning (n):

**Materialidad** **n**

**Hormigón** 0,015

**Geotextil** 0,020

_Tabla No 3 Coeficientes de Rugosidad._

_Fuente: Elaboración Propia._
**3.4 Condiciones de contorno**

Para el cálculo del eje hidráulico se deben imponer condiciones de borde para que el programa pueda resolver las ecuaciones
del modelo, se deben definir las condiciones de flujo aguas abajo y aguas arriba ya que no se tiene claridad del tipo de
escurrimiento que se dará en la quebrada.

Las condiciones de borde más utilizadas que se pueden definir en los dos casos mencionados son las siguientes:

 Hidrograma de entrada: esto define un caudal que entra al modelo en función del tiempo.

 Escurrimiento con altura normal: esto supone que en la sección de control hay flujo normal o uniforme con
pendiente de fondo igual a la pendiente de la línea de energía (fuerzas resistentes al flujo iguales a las fuerzas
motrices).

 Curva de descarga: en este caso se tiene una curva que asocia un caudal en la sección con una altura de
escurrimiento.

En la Figura No 7 se muestra dominio computacional y las condiciones de contorno del modelo hidráulico.

_Figura No 7 Condición de contorno del dominio computacional._

_Fuente: Elaboración Propia._

**3.4.1 Condiciones de contorno aguas arriba**

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 13 de 34

Debido a la geomorfología del cauce se optó por considerar dos condiciones de contorno de a fin de representar de mejor manera
el comportamiento hidrodinámico del cauce. En cada condición de contorno se ingresó la mitad del hidrograma estimado en el
estudio hidrológico.

Se maximizan los caudales al utilizar la totalidad del caudal de cuenca Guatacondo para el flujo en condición 1 y 2, y se considera
una parte del flujo de la quebrada S/N para el canal perimetral con las siguientes características:

_Tabla No 4 Datos cuencas aportantes._
_Fuente: Estudio Hidrológico SP1150-LLANOS-PAS157-AN-02-SP-HIDROLOGIA._

Los caudales máximos estimados para periodos de retorno de 100 años y 150 años son los siguientes en cada cuenca:

**100** 471,90 9,70 786,50 16,17

**150** 587,60 10,60 979,33 17,67

_Tabla No 5 Caudales líquidos y detríticos._
_Fuente: Estudio Hidrológico SP1150-LLANOS-PAS157-AN-02-SP-HIDROLOGIA._

Se estima un caudal detrítico con la siguiente expresión de la “Guía Metodológica para Proyectos de Modificación de Cauces”
de la DGA (2016):

Q detr = 1 −CQ liq v

Donde:

Q detr : Caudal sólido más caudal líquido (m [3] /s).
Q liq : Caudal líquido (m [3] /s).
C v : Concentración en volumen de sólidos (%), valor de 0,40.

Los caudales máximos del hidrograma utilizado en el modelo de condición de contorno 1 y 2 corresponde al caudal de
Guatacondo, y la condición 3 corresponde al flujo de la quebrada S/N. Se muestran en la siguiente tabla:

**100** 471,90 9,70

**150** 587,60 10,60

_Tabla No 6 Caudales del modelo._

_Fuente: Elaboración Propia._

En el Proyecto se determinaron 3 condiciones de contorno con entrada de flujo al modelo, la correspondiente condición de
contorno 3 se emplaza dentro del parque en la divisoria natural de aguas, con el objetivo de desarrollar la obra de canal que
corresponde al PAS 155 al ser una canalización con caudal superior a 2 m [3] /s .

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 14 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

Los caudales considerados para la elaboración del modelo del canal perimetral del parque se determinaron en función a las áreas
tributarias de la quebrada S/N definida en el estudio hidrológico. Para el canal perimetral que se desarrolla a partir de la condición
de contorno 3 corresponde un 32% del área. En base a lo anterior, los caudales de modelación para los caudales asociados a
crecidas con periodos de retorno de 100 y 150 años corresponden a los siguientes:

**100** 3,10

**150** 3,58

_Tabla No 7 Caudales del parque para el modelo._

_Fuente: Elaboración Propia._

**3.4.2 Condiciones contorno aguas abajo**

Como condición aguas abajo se configuró el software con la opción de altura normal el cual requiere de la pendiente del terreno,
para este caso se ingresó el valor de 0,001 m/m obtenido a partir de la topografía.

**3.5 Parámetros de obras propuestas**

**3.5.1 Revancha**

La revancha corresponde a la altura libre entre la cota de borde de un canal y la superficie del agua. No hay criterios
universalmente aceptados para el cálculo de revanchas en canales y en general es necesario hacer consideraciones sobre el tipo
de canal y del modo de operación de éstos.

Según acápite 3.705.205 Manual de Carreteras Vol. 3, la revancha de la sección debe ser suficiente para evitar que las
fluctuaciones del nivel de agua o las ondas del canal sobrepasen sus bordes. Se recomienda considerar revanchas entre 5% y
30% de la altura de escurrimiento (h n ), con un mínimo de revancha de 20 cm. De esta manera para escurrimiento normal se

tiene:

1.05h n ≤H Canal ≤1.30h n

Por otro lado, para canales con flujos de alta velocidad, con régimen de escurrimiento supercrítico, como lo es el canal perimetral
del presente proyecto, se usará la recomendación del US Bureau of Reclamation, que para estimar la revancha (r h ) considera
las alturas de escurrimiento (h) y las velocidades (v). La expresión es:

3

r h = 0.6 + 0.037 ∗v∗√h

Donde:

 - _v_ : Velocidad de escurrimiento en m/s

 - _h_ : Altura de escurrimiento en m

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 15 de 34

**3.5.2 Velocidad**

La máxima velocidad de escurrimiento aceptable en el canal, es aquella que no provocará erosión en el fondo ni en las paredes
laterales del canal. Para el presente estudio se determinan los siguientes valores de tolerancia.

**Hormigón** 3,50

**Geotextil** 5,00

**Tierra** 1,50

_Tabla No 8 Velocidades Máximas Admisibles._

_Fuente: Elaboración Propia._

**4.** **Resultados de Modelación**

```
 -
```

**4.1 Resultados de modelamiento hidráulico sin proyecto** **TR 100**

**4.1.1. Tirante en el dominio hidráulico**

En el dominio hidráulico el tirante de agua oscila entre 0,01 m y 1,77 m.

Figura No 8 Tirante de agua en el dominio hidráulico para un TR 100.

Fuente: Elaboración Propia.

Se muestra en la Figura No8 el tirante de aguas máxima en el dominio del modelo y se indican las quebradas IGM en líneas de
color rojo. Se visualizan aportaciones de caudal desde el borde norte del Proyecto hacia la quebrada IGM Guatacondo, que será
contenido por un pretil en el borde norte del parque.

En el sector del Proyecto se estima que el flujo se comporta de forma bien distribuida, sin presencia de un cauce definido. Aún
así, se ingresa una aportación de caudal de forma puntual para mostrar el caso más desfavorable y proyectar un canal de sección

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 16 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

fija capaz de portear el caudal de diseño con periodo de retorno 100 años. En el sector este se proyecta un canal perimetral con
una aportación de aguas a la quebrada S/N con caudal superior a 2 m [3] /s.

**4.1.2. Tirante en la zona de interés**

El tirante de agua en el límite con el parque solar alcanza un valor máximo de 0,27 m para caudales con periodo de retorno 100

años.

Figura No 9 Tirante de agua en el límite del parque solar para un TR 100.

Fuente: Elaboración Propia.

**4.1.3. Velocidad en el dominio hidráulico**

En el dominio hidráulico la velocidad oscila entre 0,1 m/s y 2,82 m/s.

Figura No 10 Velocidad en el dominio hidráulico para un TR 100.

Fuente: Elaboración Propia _._

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 17 de 34

**4.1.4. Velocidad en la zona de interés**

La velocidad máxima en el límite de la planta solar alcanza un valor máximo de 1,11 m/s.

Figura No 11 Velocidad en el límite de la planta solar para un TR 100.

Fuente: Elaboración Propia.

```
 -
```

**4.2.** **Resultados de modelamiento hidráulico sin proyecto** **TR 150**

**4.2.1.** **Tirante en el dominio hidráulico**

En el dominio hidráulico el tirante de agua oscila entre 0,01 m y 1,84 m.

Figura No 12 Tirante de agua en el dominio hidráulico para un TR 150.

Fuente: Elaboración Propia.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 18 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

**4.2.2.** **Tirante en la Zona de Interés**

El tirante de agua en el límite con el parque solar alcanza un valor máximo de 0,27 m para caudales con periodo de retorno 150

años.

Figura No 13 Tirante de agua en el límite de la planta solar para un TR 150.

Fuente: Elaboración Propia.

**4.2.3.** **Velocidad en el dominio hidráulico**

En el dominio hidráulico la velocidad oscila entre 0,1 m y 3,18 m/s.

Figura No 14 Velocidad en el dominio hidráulico para un TR 150.

Fuente: Elaboración Propia _._

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 19 de 34

**4.2.4.** **Velocidad en la Zona de Interés**

La velocidad máxima en el límite de la planta solar alcanza un valor máximo de 1,08 m/s.

Figura No 15 Velocidad en el límite de la planta solar para un TR 150.

Fuente: Elaboración Propia.

```
 -
```

**4.3. Resultados de modelamiento hidráulico con proyecto** **TR 100**

**4.3.1. Tirante en el dominio hidráulico**

En el dominio hidráulico el tirante de agua oscila entre 0,01 m y 1,77 m.

Figura No 16 Tirante de agua en el dominio hidráulico para un TR 100.

Fuente: Elaboración Propia.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 20 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

Se muestra en la Figura No16 el tirante de aguas máxima en el dominio del modelo y se indican las quebradas IGM en líneas de
color rojo. Se visualizan aportaciones de caudal desde el borde este del Proyecto hacia la quebrada IGM Sin Nombre. En este
sector se proyecta un canal perimetral con una aportación de aguas a la quebrada con caudal superior a 2 m [3] /s. Además, se
visualizan aportaciones de caudal desde el borde norte del Proyecto hacia la quebrada IGM Guatacondo que será contenido por
un pretil en el borde norte del parque.

**4.3.2. Tirante en la zona de interés**

El tirante de agua en el límite con el parque solar alcanza un valor máximo de 0,42 m para caudales con periodo de retorno 100

años.

Figura No 17 Tirante de agua en el límite del parque solar para un TR 100.

Fuente: Elaboración Propia.

En el canal perimetral se presenta una altura máxima al inicio de 1,53 m y estabilizándose en el resto del canal en valores entre
0,56 y 0,84 m hasta la descarga que se produce una altura de 0,75 m. Se considera que la altura al inicio del canal no se ajusta a
la realidad debido a que en el caso modelado se ingresa el total de caudal al inicio del canal, la condición más desfavorable,
pero que en la realidad el flujo ingresa al canal de forma distribuida por todo el borde este del mismo y no de forma puntual en
una captación al inicio del canal.

Figura No 18 Eje hidráulico en el canal perimetral del parque solar para un TR 100.

Fuente: Elaboración Propia.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 21 de 34

**4.3.3. Velocidad en el dominio hidráulico**

En el dominio hidráulico la velocidad oscila entre 0,1 m/s y 2,93 m/s.

Figura No 19 Velocidad en el dominio hidráulico para un TR 100.

Fuente: Elaboración Propia _._

**4.3.4. Velocidad en la zona de interés**

La velocidad máxima en el límite de la planta solar alcanza un valor máximo de 2,64 m/s en el sector del pretil norte.

Figura No 20 Velocidad en el límite de la planta solar para un TR 100.

Fuente: Elaboración Propia.

En el canal perimetral se presenta una velocidad máxima al inicio de 3,33 m/s y estabilizándose en el resto del canal en valores
entre 2,81 y 1,84 m/s hasta la descarga que se produce una velocidad de 3,05 m/s. Se considera que la velocidad al inicio del
canal no se ajusta a la realidad debido a que en el caso modelado se ingresa el total de caudal al inicio del canal, la condición

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 22 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

más desfavorable, pero que en la realidad el flujo ingresa al canal de forma distribuida por todo el borde este del mismo y no de
forma puntual en una captación al inicio del canal.

Figura No 21 Velocidad en el canal perimetral de la planta solar para un TR 100.

Fuente: Elaboración Propia.

```
 -
```

**4.4. Resultados de modelamiento hidráulico con proyecto** **TR 150**

**4.4.1. Tirante en el dominio hidráulico**

En el dominio hidráulico el tirante de agua oscila entre 0,01 m y 1,84 m.

Figura No 22 Tirante de agua en el dominio hidráulico para un TR 150.

Fuente: Elaboración Propia.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 23 de 34

**4.4.2. Tirante en la zona de interés**

El tirante de agua en el límite con el parque Llanos del Sol alcanza un valor máximo de 0,43 m para caudales con periodo de

retorno 150 años.

Figura No 23 Tirante de agua en el límite de la planta solar para un TR 150.

Fuente: Elaboración Propia.

Figura No 24 Eje hidráulico en el canal perimetral de la planta solar para un TR 150.

Fuente: Elaboración Propia.

En el canal perimetral se presenta una altura máxima al inicio de 1,90 m y estabilizándose en el resto del canal en valores entre
0,60 y 0,91 m hasta la descarga que se produce una altura de 0,81 m. Se considera que la altura al inicio del canal no se ajusta a
la realidad debido a que en el caso modelado se ingresa el total de caudal al inicio del canal, la condición más desfavorable,
pero que en la realidad el flujo ingresa al canal de forma distribuida por todo el borde este del mismo y no de forma puntual en
una captación al inicio del canal.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 24 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

**4.4.3. Velocidad en el dominio hidráulico**

En el dominio hidráulico la velocidad oscila entre 0,1 m y 3,18 m/s.

Figura No 25 Velocidad en el dominio hidráulico para un TR 150.

Fuente: Elaboración Propia.

**4.4.4. Velocidad en la zona de interés**

La velocidad máxima en el límite de la planta solar alcanza un valor máximo de 2,49 m/s.

Figura No 26 Velocidad en el límite de la planta solar para un TR 150.

Fuente: Elaboración Propia.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 25 de 34

Figura No 27 Velocidad en el canal perimetral de la planta solar para un TR 150.

Fuente: Elaboración Propia.

En el canal perimetral se presenta una velocidad máxima al inicio de 3,78 m/s y estabilizándose en el resto del canal en valores
entre 1,95 y 2,97 m/s hasta la descarga que se produce una velocidad de 3,36 m/s. Se considera que la velocidad al inicio del
canal no se ajusta a la realidad debido a que en el caso modelado se ingresa el total de caudal al inicio del canal, la condición
más desfavorable, pero que en la realidad el flujo ingresa al canal de forma distribuida por todo el borde este del mismo y no de
forma puntual en una captación al inicio del canal.

4.5 Situación CP en descarga del canal perimetral

En esta sección se mostrará el comportamiento del flujo en la descarga del canal perimetral. Se excluye la condición sin proyecto
debido a que no se puede representar en este sector el flujo superficial y distribuido proveniente del borde del parque al ser,
valga la redundancia, distribuido y dirigiéndose hacia la quebrada IGM S/N a la cual descarga el canal perimetral.

Se presentan los perfiles longitudinales en el sector de la obra:

**Descarga:**

Figura No 28 Eje hidráulico en el perfil longitudinal de descarga.

Fuente: Elaboración Propia.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 26 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

En la descarga del canal perimetral se presentan alturas de 0,43 m al inicio y de 0,12 m la mínima altura a 15 m del inicio de la
descarga. Se mantiene entre valores de 0,40 a 0,23 en la mayor parte del recorrido.

En cuanto a las velocidades se muestran las velocidades máximas al inicio de la descarga con valores de 3,35 m/s, con un valor
máximo a los 7 m desde el inicio de la descarga, estabilizándose posterior a los 10 m de distancia en un rango de 1,20 m/s a
1,30 m/s.

Figura No 29 Velocidad en el perfil longitudinal de descarga.

Fuente: Elaboración Propia.

**Defensa Fluvial:**

La defensa se ubica en la totalidad del límite norte del Proyecto. Se eligen 3 sectores para el análisis de tirante de agua y
velocidad en condición sin proyecto y con proyecto. Estos sectores presentan las mayores velocidades de flujo en el límite
superior del parque (ver _Figura No 30_ ).

_En el sector aguas arriba de la defensa fluvial se peralta el flujo de 0,28 a 0,31 m con una diferencia de 0,03 m. En el sector_
_aguas abajo de la defensa fluvial no se peralta el flujo con un tirante de agua de 0,26 m. Se aprecia que el efecto de la defensa_

_en el nivel de aguas es puntual debido a la reducción del cauce en este sector, tal como se muestra en la_

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 27 de 34

Figura No 31 _y_
_Figura No 32_ .

En el sector aguas arriba de la defensa fluvial se producen velocidades de 0,92 m/s en condición sin Proyecto y de 2,39 m/s en
condición con Proyecto. En el sector aguas abajo de la defensa fluvial se producen velocidades de 1,13 m/s en condición sin
proyecto y de 1,74 m/s en condición con proyecto. Se aprecia que el efecto de la defensa en la velocidad se extiende generando
una condición de velocidades altas las que podrían socavar en los alrededores, ver _Figura No 33_ y Figura No34.

Figura No 30 Velocidad en el perfil longitudinal de la defensa fluvial. Arriba modelo sin proyecto y abajo con proyecto.

Fuente: Elaboración Propia.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 28 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

Figura No 31 Tirante de agua en el perfil longitudinal de la defensa fluvial en sector aguas arriba.

Arriba modelo sin proyecto y abajo con proyecto.

Fuente: Elaboración Propia.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 29 de 34

Figura No 32 Tirante de agua en el perfil longitudinal de la defensa fluvial en sector aguas abajo.

Arriba modelo sin proyecto y abajo con proyecto.

Fuente: Elaboración Propia.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 30 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

Figura No 33 Velocidad en el perfil longitudinal de la defensa fluvial en sector aguas arriba.

Arriba modelo sin proyecto y abajo con proyecto.

Fuente: Elaboración Propia.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 31 de 34

Figura No 34 Velocidad en el perfil longitudinal de la defensa fluvial en sector aguas abajo.

Arriba modelo sin proyecto y abajo con proyecto.

Fuente: Elaboración Propia.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 32 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

**5.** **Diseño de obras**

**Descarga:**

La descarga a terreno natural se realiza directo al cauce con una sección recubierta de mampostería de piedra en la zona de
descarga.

El detalle de sus dimensiones se indica en el plano detalle “SP1150-LLANOS-PAS157-DR-04-SP-DETALLE”.

Figura No 35 Sección de descarga. Vista en planta (arriba) y sección longitudinal (abajo).

Fuente: Elaboración Propia.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 33 de 34

**Canal Perimetral:**

La obra proyectada, tiene una sección trapecial en tierra revestido en geotextil, cuya finalidad es conducir y desviar las aguas
lluvias provenientes de quebradas naturales que se ubican aguas arriba de los deslindes del Proyecto.

El detalle de sus dimensiones se indica en el plano detalle “SP1150-LLANOS-PAS157-DR-04-SP-DETALLE”.

Figura No 36 Corte Transversal Canal Perimetral.

Fuente: Elaboración Propia.

**Defensa Fluvial:**

Figura No 37 Defensa fluvial en sector norte del parque.

Fuente: Elaboración Propia.

SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA PROYECTO PARQUE LLANOS DEL SOL
Página 34 de 34 MEMORIA MODELACIÓN HIDRÁULICA - PAS 157

**6** **. Conclusiones y Comentarios**

De acuerdo con el estudio hidráulico realizado, se obtiene lo siguiente:

 - Para las modelaciones hidráulicas se considera un caudal para diseño de T=100 años y verificación de T=150
años. Los caudales utilizados corresponden a los obtenidos en el Apéndice 02 de estudio hidrológico “SP1150LLANOS-PAS157-AN-02-SP-HIDROLOGIA”, los que fueron amplificados en un 40%, aplicando un
coeficiente para el uso de caudal detrítico.

 - Para el presente permiso se consideran además de las obras asociadas al presente PAS, las obras tramitadas
en PAS 155 (canal perimetral).

 - De acuerdo con los resultados de las modelaciones, considerando caudales para tiempos de concentración
de 100 años para el diseño y de 150 años para verificación, las obras proyectadas mantienen las condiciones
hidráulicas de escurrimiento y soportan la totalidad del caudal estimado.

 - Las alturas de aguas del canal perimetral han sido verificadas para el diseño considerando los criterios de
revancha para régimen subcrítico y supercrítico según la recomendación del US Bureau of Reclamation.

 - La totalidad de las velocidades de escurrimiento obtenidas en la modelación para el periodo de retorno T=100
años son inferiores a los 5 m/s, por lo tanto, el revestimiento es apropiado para las características del canal
perimetral proyectado y será del tipo geotextil o similar.

 - Los diseños presentados en el permiso podrán ser optimizados en fases posteriores de ingeniería.

PROYECTO PARQUE LLANOS DEL SOL SP1150-LLANOS-PAS157-AN-03-SP-HIDRAULICA
MEMORIA MODELACIÓN HIDRÁULICA - PAS 157 Página 35 de 34