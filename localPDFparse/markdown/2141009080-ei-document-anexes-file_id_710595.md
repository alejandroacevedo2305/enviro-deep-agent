---
title: Gerencia de Operaciones
author: Javiera Belén Vega Garrido
date: D:20180705153550Z00'00'
language: es
type: report
pages: 26
has_toc: False
has_tables: True
extraction_quality: high
---

|INFORME MODELACIÓN DE PLUMA|Col2|Col3|
|---|---|---|
|**Informe Técnico Área Acuática**|**ITLB-MP-29.88-1**|**ITLB-MP-29.88-1**|
|**Versión 2.**|** Páginas 26**|**Fecha envío: 29-09-2017 **|

|Col1|NOMBRE|CARGO|FECHA|
|---|---|---|---|
|**ELABORADO**|Alex García|Ingeniero Hidráulico|28-09-2017|
|**REVISADO**|Fernando Vergara|Jefe de Operaciones|28-09-2017|
|**APROBADO**|Alejandra Marín|Gerente Operaciones|29-09-2017|

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **2** de **26**

**ÍNDICE**

**RESUMEN EJECUTIVO ................................................................................................................ 4**
**1.** **INTRODUCCIÓN Y OBJETIVOS ............................................................................................. 4**
**2.** **ÁREA DE ESTUDIO .............................................................................................................. 7**
**3.** **HIDROLOGÍA DE CAUDALES MÍNIMOS ................................................................................ 8**

3.1 Área Aportante .................................................................................................................. 8

3.2 Disponibilidad de Información ........................................................................................... 9

3.3 Caudal Medio Anual ........................................................................................................ 11

3.4 Caudales Mínimos anuales .............................................................................................. 11

3.5 Curva de Variación Estacional .......................................................................................... 12

**4.** **MODELACIÓN HIDRÁULICA .............................................................................................. 13**

4.1 Caudales .......................................................................................................................... 13

4.2 Topografía ....................................................................................................................... 13

4.3 Coeficiente de rugosidad ................................................................................................. 16

4.4 condición de borde .......................................................................................................... 16

4.5 Resultados ....................................................................................................................... 16

**5.** **MODELACIÓN PLUMA DE DESCARGA ............................................................................... 21**

5.1 Metodología .................................................................................................................... 21

5.2 Antecedentes .................................................................................................................. 23

5.3 Resultados ....................................................................................................................... 24

**6** **CONCLUSIONES ............................................................................................................... 26**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **3** de **26**

**ÍNDICE DE FIGURAS**

Figura 1. Mapa de emplazamiento. .......................................................................................................6

Figura 2. Ubicación del proyecto. ...........................................................................................................7

Figura 3. Ubicación cuenca de interés con estación fluviométrica. .......................................................9

Figura 4. Curva de variación estacional para los caudales mínimos .....................................................12

Figura 5. Perfiles longitudinales trazados en la modelación 2D. Cauce principal (arriba), brazo sur en
análisis (abajo). Fuente: Informe Hidráulico, DSS. ................................................................................15

Figura 6. Esquema de la situación modelada. ......................................................................................15

Figura 7.Perfil longitudinal en el Río Cachapoal, aguas arriba y aguas debajo de la confluencia con el
brazo sur, para algunas situaciones modeladas. ..................................................................................16

Figura 8. Perfil longitudinal en el brazo sur del Río Cachapoal para algunas situaciones modeladas. ..17

Figura 9. Validez de las fórmulas de la constante de reaireación ........................................................22

Figura 10. OD en distintos escenarios de caudal (en m [3] /s), expresada como porcentaje de la
concentración ODsat (17°C) aguas arriba. ............................................................................................25

**ÍNDICE DE TABLAS**

Tabla 1. Ubicación cuenca de interés. Datum UTM, Huso 19. ........................................................... 8

Tabla 2. Ubicación y área aportante de estación fluviométrica y punto de interés......................... 10

Tabla 3. Disponibilidad de datos...................................................................................................... 11

Tabla 4. Caudal medio anual, mínimo y máximo del periodo. ......................................................... 11

Tabla 5. Caudal mínimo anual para distintos periodos de retorno. ................................................. 12

Tabla 6. Curva de variación estacional para los caudales mínimos ................................................. 12

Tabla 7. Condiciones hidrológicas modeladas. ................................................................................ 14

Tabla 8. Resultados modelación hidráulica condición 1. ................................................................. 18

Tabla 9. Resultados modelación hidráulica condición 6. ................................................................. 18

Tabla 10. Resultados modelación hidráulica condición 7. ............................................................... 19

Tabla 11. Resultados modelación hidráulica condición 12. ............................................................. 19

Tabla 12. Resultados modelación hidráulica condición 13. ............................................................. 20

Tabla 13. Resultados modelación hidráulica condición 18. ............................................................. 20

Tabla 14. Condiciones antecedentes de Oxígeno Disuelto y Demanda Bioquímica de Oxígeno, aguas
arriba de la descarga y en el afluente. ............................................................................................. 24

Tabla 15. OD en distintos escenarios, expresada como porcentaje de la concentración ODsat (17°C)
aguas arriba. .................................................................................................................................... 25

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **4** de **26**

**1.** **RESUMEN EJECUTIVO**

El presente informe forma parte de la Declaración de Impacto Ambiental (DIA) asociado al

proyecto de ampliación de la capacidad de la Planta de Tratamiento de Aguas Servidas (PTAS) de la

localidad de Pichidegua, Provincia del Cachapoal, perteneciente a la empresa de servicios sanitarios

Essbio S.A. y actualmente en funcionamiento.

El objetivo general del informe es determinar el caudal mínimo necesario en el brazo sur del río

Cachapoal, donde se ubica el punto de descarga de la PTAS, tal que el área de influencia de la pluma

respecto a Oxígeno Disuelto (OD) sea menor o igual a 100 m de extensión.

Se realizó un análisis hidrológico de caudales mínimos para los periodos de retorno: T=2, 5 y 10

años en el Río Cachapoal, caracterizando las condiciones más desfavorables de mezcla en el brazo de

descarga. Luego se implementó un modelo hidráulico con el software HEC-RAS para el río Cachapoal y

el brazo sur. Para evaluar la condición de mezcla se definieron 18 combinaciones que consideraron de

caudal mínimo en el río Río Cachapoal para periodos de retorno T= 2, 5 y 10 años y seis caudales por

el brazo sur de Q = 22, 50, 100, 200, 500 y 1000 l/s.

La pluma de descarga consideró la concentración de OD en cada sección transversal para los 18

escenarios hidrológicos modelados. La modelación se realizó utilizando la ecuación de Streteer y

Phelps, con las condiciones antecedentes de OD y DBO aguas arriba y en el punto de descarga.

Los resultados indican que se requiere de un caudal mínimo de 200 l/s en el brazo sur para generar

condiciones adecuadas de OD en el brazo sur.

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **5** de **26**

**2.** **INTRODUCCIÓN Y OBJETIVOS**

El presente informe forma parte de la Declaración de Impacto Ambiental (DIA) asociado al

proyecto de ampliación de la capacidad de la Planta de Tratamiento de Aguas Servidas (PTAS) de la

localidad de Pichidegua, Provincia del Cachapoal, perteneciente a la empresa de servicios sanitarios

Essbio S.A. y actualmente en funcionamiento (Figura 1).

El objetivo general del informe es determinar el caudal mínimo necesario en el brazo sur del Río

Cachapoal, donde se ubica el punto de descarga de la Planta de Tratamiento de Aguas Servidas, tal

que el área de influencia sea menor o igual a 100 m de extensión.

Para cumplir este objetivo se definieron objetivos específicos:

✓ Definir caudales mínimos con periodos de retorno: T=2, 5 y 10 años en el Río Cachapoal,

con la intención de definir las condiciones más desfavorables de mezcla en el brazo de

descarga.

✓ Definir las condiciones de mezcla considerando distintos escenarios de caudal en el brazo

sur, Q = 22, 50, 100, 200, 500 y 1000 l/s, para ello se realizará la modelación hidráulica

del sistema en estudio (Río Cachapoal considerando el cauce principal y el brazo sur).

✓ Caracterizar la pluma de descarga de Oxígeno Disuelto en distintos escenarios

hidrológicos, utilizando la ecuación de Streteer y Phelps.

Para cumplir con el objetivo se recopilaron antecedentes para el tramo de interés, secciones

transversales del cauce, condiciones hidráulicas (altura y velocidad media de escurrimiento),

parámetros bioquímicos del efluente y cuerpo receptor. Basados en los antecedentes se procedió a

modelar la pluma de descarga en toda la extensión el brazo sur del río Cachapoal, esto es 1.5 km. aguas

arriba de la confluencia con el río Cachapoal.

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **6** de **26**

**Figura 1. Mapa de emplazamiento.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **7** de **26**

**3.** **ÁREA DE ESTUDIO**

La zona de estudio está ubicada en la comuna de Pichidegua, Provincia de Cachapoal, Región del

Libertador General Bernardo O’Higgins. La descarga se emplaza en el río Cachapoal en la parte baja de

la cuenca, en una zona de carácter erosivo y depositacional, donde la geomorfología fluvial es

altamente activa, con cambios morfológicos significativos en periodos estacionales y/o anuales.

El punto de descarga se ubica en la ribera sur de la cuenca del río Cachapoal (ver Figura 2, Tabla

1). Actualmente, la PTAS de Pichidegua descarga su efluente a través de un ducto de 400 mm.

**Figura 2. Ubicación del proyecto.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **8** de **26**

**Tabla 1. Ubicación cuenca de interés. Datum UTM, Huso 19.**

**4.** **HIDROLOGÍA DE CAUDALES MÍNIMOS**

Dado que las condiciones de mezcla en el punto de descarga serán más desfavorables mientras

menor sean los caudales en el Río Cachapoal, se procede hacer un estudio de caudales mínimos en el

sistema. A continuación, se entregan antecedentes de la subcuenca asociada al punto de interés y

caracterización hidrológica de los caudales mínimos del Río Cachapoal asociada a ella.

Específicamente, caudal medio anual, caudales mínimos anuales, y curva de variación estacional para

caudales mínimos. Ello con el objetivo de definir el caudal mínimo en el brazo donde se vierte la

descarga, bajo condiciones desfavorables de caudal en el cauce principal del río Cachapoal.

**4.1** **Área Aportante**

La zona de estudio está asociada a la subcuenca definida por el punto de descarga de la Planta de

Tratamiento de Aguas Servidas en el Río Cachapoal, ubicada en la comuna de Pichidegua, Provincia de

Cachapoal, Región del Libertador General Bernardo O’Higg ins (Tabla 1).

La delimitación de la subcuenca asociada al punto de interés fue realizada a partir del modelo de

elevación (DEM) ASTER GDEM World Elevation Data (1.5 arc-second Resolution) de 32 metros de

resolución espacial, como se muestra en la

Figura **3** .

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **9** de **26**

**Figura 3. Ubicación cuenca de interés con estación fluviométrica.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **10** de **26**

**4.2** **Disponibilidad de Información**

La Dirección General de Agua cuenta con una estación fluviométrica vigente, Río Cachapoal en

Puente Arqueado (6019003-8), muy próxima al punto de interés. Por tanto, se utilizará el método de

transposición de cuencas para realizar el estudio hidrológico. La razón de áreas es 0.977 entre la zona

de estudio y la estación DGA (Tabla 2).

Se cuenta con el registro histórico de caudales instantáneos y caudales medios mensuales a partir

del año 2002 (tabla 3)

**Tabla 2. Ubicación y área aportante de estación fluviométrica y punto de interés.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **11** de **26**

**4.3** **Caudal Medio Anual**

**Tabla 3. Disponibilidad de datos.**

A partir de la estadística disponible de datos mensuales en la estación fluviométrica Río Cachapoal

en Puente Arqueado, y utilizando el método de transposición de cuencas se estimó el caudal medio

anual. Para ello se consideraron meses con más de 20 días de datos, y años con al menos 10 meses de

datos. Los resultados expuestos en la Tabla 4 donde se tiene un caudal medio anual de 80 m3/s.

**Tabla 4. Caudal medio anual, mínimo y máximo del periodo.**

**4.4** **Caudales Mínimos anuales**

A partir de la estadística disponible de datos instantáneos, y utilizando el método de transposición

de cuencas se procedió a estimar caudales mínimos mensuales, para aquellos meses que tenían

registros completos durante al menos 21 días. A partir de dicha estadística, se estimaron los caudales

mínimos anuales para diferentes periodos de retorno, considerando años con al menos 10 meses de

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **12** de **26**

datos. Los resultados expuestos en la Tabla 5, muestran el caudal mínimo anual con periodo de

retorno, T= 2, 5 y 10 años.

**Tabla 5. Caudal mínimo anual para distintos periodos de retorno** .

**4.5** **Curva de Variación Estacional**

A partir del método de transposición de cuencas se determinaron los caudales mínimos

mensuales. Se definieron las curvas de variación estacional para diferentes probabilidades de

excedencia (que sean menores) a partir de la estadística histórica disponible de caudales instantáneos

(definidos con más de 21 días de datos) (Tabla 6).

Como se aprecia en la figura 4, el Río Cachapoal en Puente Arqueado presenta sus menores

caudales mínimos mensuales en el periodo marzo-abril (debido a las precipitaciones y a los deshielos

cordilleranos remanentes). La cuenca asociada tiene un régimen pluvio-nival.

**Tabla 6. Curva de variación estacional para los caudales mínimos**

**Figura 4. Curva de variación estacional para los caudales mínimos**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **13** de **26**

**5.** **MODELACIÓN HIDRÁULICA**

La modelación hidráulica unidimensional permite describir la profundidad de un flujo con

respecto al lecho de un cauce donde el agua circula a superficie libre y en condiciones permanentes a

través de la resolución de la ecuación de energía.

Los ejes hidráulicos para el tramo de estudio fueron calculados con el software HEC-RAS 4.0.0

(Hydrologic Engineering Center-River Analysis System, US Army Corps of Engineers, USACE 2008).

Para desarrollar los modelos hidráulicos se consideraron los aspectos:

✓ Caudales

✓ Topografía

✓ Coeficiente de rugosidad

✓ Condición de borde

**5.1** **Caudales**

Con el objetivo de analizar distintos escenarios de mezcla en la zona de descarga, se evaluaron

distintas condiciones hidrológicas. Estas consideran caudales mínimos en el cauce principal con

periodos de retorno T=2, 5 y 10 años, y distintos caudales en el brazo sur, Q= 22, 50, 100, 200, 500 y

1000 l/s (ver Tabla 7).

**5.2** **Topografía**

La topografía fue extraída del Informe Hidráulico realizado por DSS. Se tienen 29 secciones

transversales con una separación aproximada de 50 m, cubriendo un tramo de 2 km en las cercanías

de la descarga (como se observa en la Figura 5).

Debido a que los perfiles transversales consideraban tanto el brazo sur como el cauce principal

del Río Cachapoal, se procedió a separar las secciones transversales de cada uno de los cauces con el

objetivo definir caudales porteados por cada cauce independientemente en el modelo hidráulico.

Finalmente, el sistema modelado se define en la Figura 6 **Figura 6** .

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **14** de **26**

**Tabla 7. Condiciones hidrológicas modeladas.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **15** de **26**

**Figura 5. Perfiles longitudinales trazados en la modelación 2D. Cauce principal (arriba), brazo sur en análisis (abajo).**

**Fuente: Informe Hidráulico, DSS.**

**Figura 6. Esquema de la situación modelada.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **16** de **26**

**5.3** **Coeficiente de rugosidad**

Teniendo en consideración la información disponible en el Informe Hidráulico de DSS, todas las

condiciones hidráulicas se modelaron utilizando un n de Manning de 0.035; coeficiente utilizado en la

calibración del modelo 2D.

**5.4** **condición de borde**

Como condición de borde se impuso altura normal de escurrimiento aguas abajo, asociado a una

pendiente de 0.00625, estimada a partir de los perfiles ubicados aguas abajo.

**5.5** **Resultados**

Se presenta el perfil longitudinal en el Río Cachapoal, aguas arriba y aguas debajo de la confluencia

con el brazo sur (Figura 7), y el perfil longitudinal en el brazo sur (Figura 8), para algunas situaciones

modeladas.

**Figura 7.Perfil longitudinal en el Río Cachapoal, aguas arriba y aguas debajo de la confluencia con el brazo sur, para**

**algunas situaciones modeladas.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **17** de **26**

**Figura 8. Perfil longitudinal en el brazo sur del Río Cachapoal para algunas situaciones modeladas.**

A continuación, se presentan las tablas de resultados de la modelación hidráulica, para las seis

condiciones de caudal que se presentan en las figuras anteriores, correspondientes a los escenarios:

1, 6, 7, 12, 13 y 18 (de acuerdo con la Tabla 7).

Los resultados indican que las condiciones hidráulicas de caudales bajos en el río Cachapoal no

afectan el comportamiento hidráulico en el brazo sur. Por lo tanto, la determinación de un caudal

mínimo que garantice una dilución adecuada en el brazo sur es condición suficiente para garantizar

una Pluma de la descarga de la PTAS Pichidegua.

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **18** de **26**

**Tabla 8. Resultados modelación hidráulica condición 1.**

**Tabla 9. Resultados modelación hidráulica condición 6.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **19** de **26**

**Tabla 10. Resultados modelación hidráulica condición 7.**

**Tabla 11. Resultados modelación hidráulica condición 12.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **20** de **26**

**Tabla 12. Resultados modelación hidráulica condición 13.**

**Tabla 13. Resultados modelación hidráulica condición 18.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **21** de **26**

**6.** **MODELACIÓN PLUMA DE DESCARGA**

**6.1** **Metodología**

Para modelar la concentración de oxígeno y demanda bioquímica de oxígeno se utilizó la ecuación

de Streeter y Phelps. Corresponde a un modelo matemático que relaciona los dos principales

mecanismos que definen el oxígeno disuelto en un cauce de agua superficial que recibe la descarga de

aguas residuales: descomposición de materia orgánica y aireación de oxígeno. Utilizando esta ecuación

se estudia la composición de la mezcla.

Primero, para definir las características de la mezcla se realizaron balances de masa.

Para definir la temperatura de la mezcla:

## Q 1 ∗T 1 + Q 2 ∗T 2 = Q 3 ∗T 3

Q1: caudal aguas arriba (m3/s)

Q2: caudal afluente (m3/s)

Q3: caudal aguas abajo (m3/s)

T1: temperatura aguas arriba (°C)

T2: temperatura afluente (°C)

T3: temperatura aguas abajo (°C)

Para definir la concentración de Oxígeno Disuelto de la mezcla:

## Q 1 ∗OD 1 + Q 2 ∗OD 2 = Q 3 ∗OD 3

Q1: caudal aguas arriba (m3/s)

Q2: caudal afluente (m3/s)

Q3: caudal aguas abajo (m3/s)

OD1: oxígeno disuelto aguas arriba (mg/L)

OD2: oxígeno disuelto afluente (mg/L)

OD3: oxígeno disuelto aguas abajo (mg/L)

Para definir la concentración de Demanda Bioquímica de la mezcla:

## Q 1 ∗DBO 1 + Q 2 ∗DBO 2 = Q 3 ∗DBO 3

Q1: caudal aguas arriba (m3/s)

Q2: caudal afluente (m3/s)

Q3: caudal aguas abajo (m3/s)

DBO1: oxígeno disuelto aguas arriba (mg/L)

DBO2: oxígeno disuelto afluente (mg/L)

DBO3: oxígeno disuelto aguas abajo (mg/L)

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **22** de **26**

A partir de las condiciones hidráulicas, altura de escurrimiento y velocidad media, definidas de la

modelación hidráulica para cada condición modelada y para cada sección transversal, se estiman las

constantes de reaireación y desoxigenación. La constante de reaireación es definida por diferentes

fórmulas, de acuerdo a las condiciones hidráulicas que se tienen en el cauce, según la Figura 9

**Figura 9. Validez de las fórmulas de la constante de reaireación**

.

O’Connor -Dobbins: Kr= 3.93 ∗V [0.5] ⁄H [1.5]
Churchill: Kr= 5.03 ∗VH⁄ [1.67]
Owens-Gibbs:Kr= 5.32 ∗V [0.67] ⁄H [1.85]

Donde:
Kr: Coeficiente de aireación (día [-1] )
V: velocidad del escurrimiento (m/s)
H: altura del escurrimiento (m)

Para definir la constante de desoxigenación, se utilizaron dos fórmulas:

Bosko (1966): K d = K 0 + n∗VH⁄, para Q >0,28 m [3] /s.
Wrigth y McDonnell (1979): K d = 39.6 ∗3.28 ∗P [−0.84], para Q ≤ 0, 28 m [3] /s.

Donde:
Kd: Coeficiente de desoxigenación a 20°C (día [-1] )
Ko: Tasa de desoxigenación base. Supuesto: 0.15
n: Coeficiente de actividad del lecho de la corriente. Supuesto: 0.35
V: velocidad del escurrimiento (m/s)
H: altura del escurrimiento (m)
P: perímetro mojado (ft)

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **23** de **26**

Ambas fórmulas estiman el coeficiente de desoxigenación para una temperatura de 20°C. Debido

que las temperaturas de la mezcla son diferentes a 20°C, se corrigieron utilizando la siguiente fórmula:

## Kd [t°C] = Kd [20°C] ∗1.35 [(t−20)]

Donde:
Kd [(t°C)] : Coeficiente de desoxigenación a una temperatura t.
Kd [(20°C)] : Coeficiente de desoxigenación a 20°C (día [-1] )
t: temperatura (°C)

Luego la tasa a la que se produce oxígeno, tasa de oxigenación, y la tasa a la que el oxígeno es

consumido (DBO), tasa de desoxigenación, se definen por:

Tasa de oxigenación = Kr*OD déficit
Tasa de desoxigenación = Kd*DBO

Donde:
Kr: Coeficiente de aireación (día [-1] )
Kd: Coeficiente de aireación (día [-1] )
DBO: Demanda bioquímica de oxígeno (mg/L)
ODdéficit: déficit de oxígeno disuelto.

El déficit de oxígeno disuelto en primera instancia se estima como la diferencia entre el

ODsaturado evaluado en la temperatura de la mezcla, con el OD en la mezcla.

Esto es:

ODdéficit = ODsat - ODmezcla

El déficit de Oxígeno Disuelto en el tiempo, estará dado por:

-
ODdéficit (t) = ODdéficit inicial + t * (Tasa de desoxigenación Tasa de oxigenación)

Luego el Oxígeno Disuelto en el tiempo, estará dado por:

OD = ODsat - ODdeficit

**6.2** **Antecedentes**

A partir del estudio de caudales mínimos en el Río Cachapoal se tienen las condiciones hidráulicas

más desfavorables para la dilución de la mezcla. De la modelación hidráulica para estas condiciones,

se han definido las condiciones hidráulicas que influencian la descomposición de materia orgánica y

aireación de oxígeno, que son la altura de escurrimiento y velocidad media de este. De esta

caracterización, se definen las constantes de aireación y descomposición a la escala del tramo de río

(en los perfiles transversales), con las que se evalúan las tasas de aireación y descomposición para

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **24** de **26**

establecer el balance de las concentraciones de Oxígeno Disuelto y Demanda Bioquímica de Oxígeno

en el área de interés. Además, se tiene la concentración de Oxígeno Disuelto y Demanda Bioquímica

de Oxígeno aguas arriba de la descarga y en la descarga (ver Tabla 14).

**Tabla 14. Condiciones antecedentes de Oxígeno Disuelto y Demanda Bioquímica de Oxígeno, aguas arriba de la descarga**

**y en la descarga.**

|Parámetros|Aguas arriba|Descarga|
|---|---|---|
|Temp (°C)|17|19|
|Oxígeno Disuelto (mg/L)|10,65|4,55|
|DBO5 (mg/L)|0|35|

**6.3** **Resultados**

Se presentan las concentraciones de Oxígeno Disuelto en cada uno de los perfiles transversales

aguas abajo de la descarga, ello expresado en porcentaje de la concentración de Oxígeno Disuelto

antes de la descarga (10.65 mg/l). Debido a que el cauce principal no influencia las condiciones

hidráulicas en el brazo sur, se observan las mismas concentraciones de oxígeno disuelto para los

caudales T=2, 5 y 10 años en el Río Cachapoal (como se muestra en la Tabla 15 y Figura 10)).

Evidentemente, en para un caudal en el brazo de 22 l/s correspondiente a "sólo descarga de

efluente" el oxígeno es consumido totalmente a 250m de la descarga. En los otros escenarios (caudales

en el brazo sur: 50, 100, 200, 500 y 1000 l/s) existe consumo de oxígeno, pero no agotamiento.

Considerando una descarga de 22 l/s, con concentración inicial 4.5 mg/l de Oxígeno Disuelto y 35 mg/l

de DBO, caudales superiores a 200 l/s en el brazo sur permitirán concentraciones de Oxígeno Disuelto

aceptables en el cuerpo receptor. Esto es, concentraciones de oxígeno disuelto superiores a 85% de la

concentración de Oxígeno Disuelto presente en el río Cachapoal aguas arriba de la descarga (10.65

mg/L) (ver Figura 10).

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **25** de **26**

**Tabla 15. OD en distintos escenarios de caudal (en m** **[3]** **/s), expresada como porcentaje de la concentración ODsat (17°C)**

**aguas arriba.**

|Q brazo|0,022|0,05|0,1|0,2|0,5|1|
|---|---|---|---|---|---|---|
|**Distancia (m)**|**Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba**|**Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba**|**Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba**|**Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba**|**Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba**|**Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba**|
|0|42,72|74,80|87,40|93,70|97,48|98,74|
|50|76,52|81,20|88,01|93,00|96,83|98,34|
|100|78,62|83,93|88,20|92,35|96,24|97,96|
|150|72,51|83,80|88,09|91,93|95,74|97,56|
|200|35,88|77,17|86,35|91,33|95,52|97,37|
|250|0,00|67,43|83,72|90,59|95,44|97,31|
|300|0,00|59,46|81,42|89,91|95,36|97,24|
|350|0,00|53,78|79,76|89,40|95,29|97,18|
|400|0,00|48,33|78,00|88,83|95,19|97,10|
|450|0,00|44,42|76,57|88,33|95,08|96,99|
|500|0,00|39,70|75,04|87,79|94,99|96,91|
|550|0,00|34,85|73,09|87,12|94,89|96,84|
|600|0,00|31,82|71,58|86,54|94,80|96,76|
|650|0,00|29,58|70,40|86,11|94,68|96,66|

**Figura 10. OD en distintos escenarios de caudal (en m** **[3]** **/s), expresada como porcentaje de la concentración ODsat (17°C)**

**aguas arriba.**

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

**ITLB-MP-29.88-1**

**Versión 2.**

Septiembre 29/ 2017
Página **26** de **26**

**7.** **CONCLUSIONES**

Los resultados indican que, si se garantiza un caudal de 200 l/s o superior en el brazo sur del río

Cachapoal, la calidad del agua, expresada como concentración de Oxígeno Disuelto, sería cercana a la

condición de saturación a 100 m de la descarga actual de la PTAS Pichidehua.

Alex García Lancaster

Ingeniero Civil, M.S.

Dr. Ciencias Ambientales

[contacto@geaambiental.cl](mailto:contacto@geaambiental.cl)

+56 41 3832613

www.geaambiental.cl

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 14.: Condiciones antecedentes de Oxígeno Disuelto y Demanda Bioquímica de Oxígeno, aguas arriba de la descarga****

| Parámetros | Aguas arriba | Descarga |
| --- | --- | --- |
| Temp (°C) | 17 | 19 |
| Oxígeno Disuelto (mg/L) | 10,65 | 4,55 |
| DBO5 (mg/L) | 0 | 35 |

**Tabla 15.: OD en distintos escenarios de caudal (en m** **[3]** **/s), expresada como porcentaje de la concentración ODsat (17°C)****

| Q brazo | 0,022 | 0,05 | 0,1 | 0,2 | 0,5 | 1 |
| --- | --- | --- | --- | --- | --- | --- |
| **Distancia (m)** | **Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba** | **Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba** | **Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba** | **Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba** | **Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba** | **Porcentaje de OD modelado respecto a ODsat(17°C) aguas arriba** |
| 0 | 42,72 | 74,80 | 87,40 | 93,70 | 97,48 | 98,74 |
| 50 | 76,52 | 81,20 | 88,01 | 93,00 | 96,83 | 98,34 |
| 100 | 78,62 | 83,93 | 88,20 | 92,35 | 96,24 | 97,96 |
| 150 | 72,51 | 83,80 | 88,09 | 91,93 | 95,74 | 97,56 |
| 200 | 35,88 | 77,17 | 86,35 | 91,33 | 95,52 | 97,37 |
| 250 | 0,00 | 67,43 | 83,72 | 90,59 | 95,44 | 97,31 |
| 300 | 0,00 | 59,46 | 81,42 | 89,91 | 95,36 | 97,24 |
| 350 | 0,00 | 53,78 | 79,76 | 89,40 | 95,29 | 97,18 |
| 400 | 0,00 | 48,33 | 78,00 | 88,83 | 95,19 | 97,10 |
| 450 | 0,00 | 44,42 | 76,57 | 88,33 | 95,08 | 96,99 |
| 500 | 0,00 | 39,70 | 75,04 | 87,79 | 94,99 | 96,91 |
| 550 | 0,00 | 34,85 | 73,09 | 87,12 | 94,89 | 96,84 |
| 600 | 0,00 | 31,82 | 71,58 | 86,54 | 94,80 | 96,76 |
| 650 | 0,00 | 29,58 | 70,40 | 86,11 | 94,68 | 96,66 |
