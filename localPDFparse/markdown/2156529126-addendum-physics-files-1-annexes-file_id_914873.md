---
title: Microsoft Word - Informe Leucayec Dispersion Farmacos
author: Rodrigo Moreno Escalona
date: D:20240611095029-04'00'
language: es
type: report
pages: 28
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME DE MODELACIÓN DE LA DISPERSIÓN DE FÁRMACOS PROYECTO: “Modificación de biomasa del cultivo de Salmón Atlántico, RCA 371/2008, CES Leucayec, Código de Centro 110860” SOLICITANTE: SALMONES CAMANCHACA S.A. EJECUTOR: IA Consultores SpA.
  - ÍNDICE DE FIGURAS
-->

# INFORME DE MODELACIÓN DE LA DISPERSIÓN DE FÁRMACOS PROYECTO: “Modificación de biomasa del cultivo de Salmón Atlántico, RCA 371/2008, CES Leucayec, Código de Centro 110860” SOLICITANTE: SALMONES CAMANCHACA S.A. EJECUTOR: IA Consultores SpA.

Junio 2024

**TABLA DE CONTENIDO**

ÍNDICE DE FIGURAS ........................................................................................................ 3

1 Introducción ............................................................................................................... 5

1.1 Objetivos .................................................................................................................... 5

1.2 Descripción del área de estudio ................................................................................. 5

2 Metodología ............................................................................................................... 9

2.1 Área de estudio .................................................................................................. 9

2.2 Modelación ....................................................................................................... 11

2.2.1 Simulaciones ................................................................................................ 11

2.2.2 Generación de Mallas ............................................................................... 12

2.2.3 Condiciones iniciales y de borde modelo hidrodinámico ........................... 13

2.2.4 Modelo de dispersión ................................................................................ 13

3 Resultados ............................................................................................................... 15

3.1 Malla ............................................................................................................. 15

3.2 Simulación hidrodinámica ............................................................................. 17

3.3 Dispersión .................................................................................................... 18

4 Cálculo de dilución ................................................................................................... 22

5 Discusión y Conclusiones ........................................................................................ 24

6 Referencias .............................................................................................................. 25

7 Anexos ..................................................................................................................... 28

P á g i n a 2 | 28

# ÍNDICE DE FIGURAS

_Figura 1. Distribución vertical de salinidad (a) y oxígeno disuelto (b) en la sección Boca_

_del Guafo - Fiordo Reloncaví_ (Silva & Vargas 2014) _._ ............................................. 6

_Figura 2. Circulación vertical de las masas de agua entre Boca del Guafo y Seno_

_Reloncaví. SAAW = Agua Subantártica, ESSW = Agua Ecuatorial Sub_

_Superficial, MSAAW = Agua Subantártica Modificada y EW = Agua Estuarina_

(Silva & Vargas 2014) _._ ............................................................................................ 7

_Figura 3. Modelo esquemático de la circulación horizontal: a) nivel superficial (0- ~30_

_m); b) nivel intermedio (~30- ~150 m), c) nivel profundo (~150 m al fondo)_

_(tomado de Silva et al., 1998)._ ................................................................................ 8

_Figura 4. Zona de estudio, se muestra la ubicación del Centro de Cultivo. Imagen_

_obtenida de Google Earth._ ...................................................................................... 9

_Figura 5. Variación de la marea (panel superior) registrado con el ADCP instalado en el_

_2019, corrientes superficiales (panel medio) y variación de la magnitud de la_

_corriente en profundidad (panel inferior)._ .............................................................. 11

_Figura 6. Flujos netos de las capas superficial, intermedia y de fondo._ ............................ 11

_Figura 7. Batimetría multihaz realizada para el estudio._ ................................................... 13

_Figura 8. Posición de las jaulas donde se liberaron las partículas virtuales._ .................... 14

_Figura 9. Transectos utilizados para analizar la dispersión en profundidad._ ..................... 15

Figura 10. Malla flexible del dominio de modelación. ....................................................... 16

Figura 11. Batimetría del modelo. .................................................................................... 16

Figura 12. Variación del nivel de la mar simulada en verano e invierno obtenida en la

posición de fondeo del ADCP de referencia. ........................................................ 17

Figura 13. Variación de la corriente superficial simulada en verano e invierno obtenida

en la posición de fondeo del ADCP de referencia. ................................................ 17

Figura 14. Validación de la variación del nivel del mar simulado con el registro de la

estación de marea de la Estación del Puerto de Melinka ...................................... 18

Figura 15. Variación de la concentración máxima de la masa suspendida en cuadratura

y sicigia. El área corresponde al periodo de emisión de las partículas virtuales

que representan los fármacos. ............................................................................. 19

P á g i n a 3 | 28

Figura 16. Variación espacial de la concentración de masa en suspensión al inicio, al

momento de presentarse la máxima concentración y al término. .......................... 20

Figura 17. Variación en los transectos en cuadratura de la concentración de masa en

suspensión al inicio, al momento de presentarse la máxima concentración y al

termino. ................................................................................................................ 21

Figura 18. Variación en los transectos en sicigia de la concentración de masa en

suspensión al inicio, al momento de presentarse la máxima concentración y al

termino. ................................................................................................................ 22

Figura 19. Frecuencia relativa de la máxima tasa de dilución de las partículas numéricas

liberadas. .............................................................................................................. 23

Figura 20. Campos de mínima dilución obtenida en las modelaciones, en superficie,

media agua y fondo. ............................................................................................. 24

P á g i n a 4 | 28

**1** **Introducción**

**1.1 Objetivos**

El presente estudio se realiza con el objetivo de obtener los campos de dilución requeridos

para el posterior estudio de determinación de la concentración de cada uno de los fármacos.

**1.2 Descripción del área de estudio**

Las aguas marítimas de la Región de los Lagos forman parte de la ecorregión Chiloense,

la cual se extiende entre la desembocadura del Río Maullín y la Península de Taitao (41

47oS). Esta ecorregión se caracteriza por presentar una condición especial de grandes

aportes de agua dulce creando un sistema único en Chiloé interior y en la intrincada red de

fiordos y canales, sumando aproximadamente 10.700 km de costa. El Mar Interior tiene por

lo tanto una mezcla de aguas marinas, estuarinas y dulces, caracterizándose además por

una circulación general vertical de dos capas.

En términos generales, las dos capas se caracterizan por una capa superficial bien

oxigenada (5-8 ml/l; 90-130% de saturación) (30-50 m de espesor) con pH alto (8.0-8.3) y

una capa profunda (75 m hasta al fondo) en la que el oxígeno disuelto, en la mayoría de los

fiordos, disminuye gradualmente a concentraciones de 3-4 ml/l (40-50% de saturación) y

los valores de pH más bajos (7.4-7.7). Se produce un fuerte gradiente vertical entre estas

dos capas, con oxígeno disuelto y pH disminuyendo rápidamente con la profundidad,

generando una oxiclina y una línea de pH de intensidad variable (Silva 2008).

La advección horizontal de aguas subantárticas bien oxigenadas adyacentes (5-6 ml/l) es

la principal fuente de oxígeno disuelto en las capas profundas del Mar Interior. El oxígeno

disuelto entrante se consume por la respiración de partículas orgánicas autóctonas y

alóctonas, a medida que el agua del océano fluye hacia las cabezas de los fiordos

continentales, alcanzando niveles casi hipóxicos (2 a 3 ml/l) o hipóxicos (<2 ml/l). A medida

que disminuye el oxígeno disuelto, las concentraciones de nutrientes aumentan hacia las

cabezas de los fiordos (de 1.6 μM PO ସ

ଷି a 2.4 μM PO ସ

ି y 16 μM NO ଷ

ି 3 y 24 μM NO ଷ

ଷି ). En

general, las condiciones de oxígeno disuelto en el Mar Interior son principalmente el

resultado de una combinación de procesos físicos y biogeoquímicos. En todos los canales

y fiordos orientales se desarrolla una zona de bajo oxígeno disuelto cerca de la cabecera

de los fiordos (<4 ml/l) como resultado de mayores entradas de materia orgánica en

P á g i n a 5 | 28

partículas alóctonas transportadas por los ríos locales. Este aporte de materia orgánica a

la capa profunda aumenta el consumo de oxígeno disuelto debido a la respiración y

sobrepasa el oxígeno suministrado por advección horizontal (Silva & Vargas 2014).

La amplia variabilidad en el régimen fluvial anual condiciona también la estratificación de la

columna de agua, específicamente su capa de agua dulce/salobre más superficial. Ello es

visible en los perfiles de columna realizados por Silva & Vargas (2014) donde queda patente

el aumento de las condiciones estuarinas a lo largo de la transecta sur-norte, con una capa

superficial de menor salinidad en el Estuario Reloncaví ( _Figura 1_ ).

_Figura 1. Distribución vertical de salinidad (a) y oxígeno disuelto (b) en la sección Boca del Guafo - Fiordo_

_Reloncaví_ (Silva & Vargas 2014) _._

También es importante destacar la ausencia de la Masa de Agua Ecuatorial Sub Superficial

(ESSW, _Figura 2)_, la que llega únicamente hasta el sur del Mar Interior. Esta masa de agua

es alta en salinidad (33.9-34.2 PSU) y muy pobre en oxígeno ((<4 ml/l; <63% saturación

O 2 .). Las masas de agua predominantes a la altura del Estuario Reloncaví son por lo tanto

la Masa de Agua Subantártica Modificada (MSAAW), a nivel de media agua y fondo, y el

agua Estuarina (EW) a nivel superficial ( _Figura 2_ ). La MSAAW corresponde a la mezcla de

Agua Subantártica (SAAW) con agua estuarina (EW), por lo que tiene un nivel de salinidad

intermedio (31 - 33 PSU). A medida que la capa profunda de MSAAW fluye en dirección a

la cabecera del Estuario de Reloncaví, su OD disminuye de 5 ml/l (75% saturación O 2 ) a 3

ml/l (Silva & Vargas 2014).

P á g i n a 6 | 28

_Figura 2. Circulación vertical de las masas de agua entre Boca del Guafo y Seno Reloncaví. SAAW = Agua_

_Subantártica, ESSW = Agua Ecuatorial Sub Superficial, MSAAW = Agua Subantártica Modificada y EW_
_= Agua Estuarina_ (Silva & Vargas 2014) _._

De acuerdo con la distribución de las características observadas, Silva _et al._ (1998)

separaron la circulación general horizontal en tres niveles que representan de manera

simple la circulación neta o residual ( _Figura 3_ ). El primero corresponde a la capa superficial

entre 0 y 20-30 m de profundidad, el segundo o intermedio entre 30 y 150 m y el tercero

desde 150 m hasta el fondo. El nivel superficial constituido por Agua Estuarina, que a

medida que se aleja de las fuentes de agua dulce hacia el océano, va aumentando su

salinidad, fluye hacia fuera del Mar Interior por el Golfo de Corcovado. El nivel intermedio

compuesto por SAAW que ingresa al golfo Corcovado por la boca del Guafo, donde es

modificada a MSAAW por su mezcla con aguas superficiales menos salinas, se bifurca en

dos ramas fluyendo una hacia el norte hasta el seno Reloncaví, y la otra hacia el sur, hasta

el estero Elefantes ( _Figura 3b_ ). En el tercer nivel, ingresa ESSW también por la boca del

Guafo, cuyo desplazamiento hacia la región interior está limitado por la topografía

submarina llegando por el sur sólo a la constricción de Meninea ( _Figura 3c_ ) y por el norte

hasta el límite sur del Mar Interior.

P á g i n a 7 | 28

_Figura 3. Modelo esquemático de la circulación horizontal: a) nivel superficial (0- ~30 m); b) nivel intermedio_

_(~30- ~150 m), c) nivel profundo (~150 m al fondo) (tomado de Silva et al., 1998)._

Al ser la alta complejidad oceanográfica uno de los principales factores dentro de la región,

es posible entender diversos procesos en la columna de agua mediante la aplicación de

modelos tridimensionales de última generación, los que basados en información

atmosférica y oceánica permiten tener una aproximación a las condiciones reales de

parámetros como: velocidad y dirección de corrientes, salinidad y temperatura en las aguas

del mar interior y estuarios de la Región de Los Lagos. Uno de los modelos hidrodinámicos

utilizados para estos efectos es MIKE 3. Este modelo obtiene soluciones numéricas de las

ecuaciones tridimensionales de Navier-Stokes, utilizando el enfoque de Reynolds, los

supuestos de Boussinesq y de presión hidrostática.

El modelo propaga las condiciones de borde oceánicas, a partir de la discretización de las

áreas geográficas y utilizando ecuaciones de conservación de masa y momentum,

considerando las variaciones de temperatura, salinidad y densidad, con un esquema

turbulento de cierre. El software de modelación utiliza contornos geográficos dinámicos en

el tiempo y en el espacio, los cuales proyecta a nuevas áreas de modelación generando

nuevos campos de datos los cuales son transformados y distribuidos tridimensionalmente

en diferentes capas verticales en la columna de agua.

P á g i n a 8 | 28

El presente estudio se enmarca en la evaluación de la dispersión de fármacos utilizados en

la industria salmonera, en específico en el CES Leucayec.

**2** **Metodología**

_**2.1**_ _**Área de estudio**_

El área de estudio ( _Figura 4_ ) se encuentra en el Archipiélago de las Guaitecas en la costa

suroeste de la Isla Leucayec al norte del Paso del Chacao

_Figura 4. Zona de estudio, se muestra la ubicación del Centro de Cultivo. Visualizador de mapas Subpesca._

La marea registrada ( _Figura 5_, panel superior) por el sensor de presión del ADCP instalado

en la zona de estudio en el año 2019, muestra un rango de marea del orden de 2.5 m

durante la sicigia y de 1.75 m durante la cuadratura. El registro de las corrientes en las

capas superficial, intermedia y de fondo ( _Figura 5_, panel intermedio) presenta corrientes

dominadas por la variación mareal, con las mayores intensidades durante la sicigia. En las

P á g i n a 9 | 28

tres capas los flujos predominantes son al sur, con algunas horas del ciclo mareal en que

se observan flujos al norte, aunque en la capa superficial son menos frecuentes,

probablemente por efecto de la acción del viento. Estos patrones se aprecian con más

claridad en la variación temporal de la magnitud en profundidad ( _Figura 5_, panel inferior) en

que se ven las bandas de mínimas y máximas corrientes, que durante los periodos de

sicigias se intensifican observándose desde la superficie al fondo. Los flujos netos ( _Figura_

_6_ ) van al S, es decir hacia el Paso del Chacao.

P á g i n a 10 | 28

_Figura 5. Variación de la marea (panel superior) registrado con el ADCP instalado en el 2019, corrientes_

_superficiales (panel medio) y variación de la magnitud de la corriente en profundidad (panel inferior)._

_Figura 6. Flujos netos de las capas superficial, intermedia y de fondo._

_**2.2**_ _**Modelación**_

Para las simulaciones de las condiciones oceanográficas y de dispersión de sustancias

emitidas en las jaulas del centro, se utilizó la suite de modelación MIKE Zero 2023©. Para

la simulación hidrodinámica se utilizó el módulo MIKE FM HD 3D de malla flexible, al que

se le acopló el módulo ECOLab con la plantilla “Simple Particle Assesment” que incluye las

variables de interés. Los detalles técnicos de los modelos MIKE FM HD 3D, ECOLab y la

plantilla se pueden revisar en

http://doc.mikepoweredbydhi.help/webhelp/2023/MIKE_FM_3D/index.htm.

_**2.2.1 Simulaciones**_

En este proyecto se evaluaron las condiciones hidrodinámicas y de dispersión en

cuadratura y sicigia en el periodo junio a agosto del 2022. Se realizaron las siguientes

simulaciones:

 - _**Hidrodinámico**_ : se simulan las condiciones oceanográficas en el periodo de

estudio. Con las primeras corridas se ajustó la malla para descartar inestabilidades

numéricas.

P á g i n a 11 | 28

 - _**Dispersión**_ : se simula la dispersión de partículas emitidas durante 12 horas a 7 m

de profundidad en cuadratura y sicigia.

**2.2.2 Generación de Mallas**

Para el estudio se preparó una malla flexible mediante el programa _Surface-water Modelling_

_System_ (SMS)© versión 13.2.16 bajo licencia _Community_ . La malla fue interpolada

utilizando para ello la información de la línea de la costa obtenida de los polígonos oficiales

de las comunas de Chile (www.ide.cl), y la información batimétrica de las cartas náuticas

del SHOA y de batimetría de la batimetría de multihaz ( _Figura 7)_ realizada para este estudio.

La malla resultante fue convertida al formato de malla de Mike mediante una rutina escrita

en Python. La malla resultante fue depurada y verificada su estabilidad mediante

simulaciones sucesivas de forma de verificar que se contaba con una malla apropiada para

el estudio.

P á g i n a 12 | 28

_Figura 7. Batimetría multihaz realizada para el estudio._

**2.2.3 Condiciones iniciales y de borde modelo hidrodinámico**

Para inicializar el modelo se consideró que el nivel del mar obtenido del modelo global

TPXO (Egbert & Erofeeva 2002), y con la misma información se generó la variación mareal

en las fronteras abiertas. Las condiciones meteorológicas horarias (vientos, presión

atmosférica, radiación solar, precipitación y evaporación) fueron obtenidas del modelo

meteorológico ERA 5 (Hersbach _et al._ 2020). Desde el modelo global HYCOM

(https://www.hycom.org) se obtuvieron las condiciones iniciales y de las fronteras (cada 3

horas) de temperatura, salinidad y corrientes horizontales (componentes u y v).

**2.2.4 Modelo de dispersión**

Para simular la dispersión de los fármacos se liberaron partículas a 7 m de profundidad en

las 18 jaulas del centro de cultivo ( _Figura 8_ ) por 12 horas en forma continua durante la

sicigia y la cuadratura. En cada paso de tiempo o iteración se libera una partícula por jaula

del centro con un flujo de masa de 0.65 [g/s]. Los resultados se presentan en superficie y

en tres transectos ( _Figura 9_ )

P á g i n a 13 | 28

_Figura 8. Posición de las jaulas donde se liberaron las partículas virtuales._

P á g i n a 14 | 28

_Figura 9. Transectos utilizados para analizar la dispersión en profundidad._

**3** **Resultados**

**3.1** **Malla**

La malla flexible final se obtuvo después de hacer simulaciones para realizar los ajustes

necesarios y corregir inestabilidades producidas por cambios batimétricos y/o distribución

de los elementos. La malla definitiva ( _Figura 10_ ) quedó configurada por 8479 nodos que

forman 14872 elementos, a la que se le interpoló la información batimétrica ( _Figura 11_ ). En

el plano vertical las simulaciones se ejecutaron con una distribución sigma de 21 niveles

utilizando los parámetros σ c = 0.1; θ = 5.0 y b = 1.0.

P á g i n a 15 | 28

_Figura 10. Malla flexible del dominio de modelación._

_Figura 11. Batimetría del modelo._

P á g i n a 16 | 28

**3.2** **Simulación hidrodinámica**

Los resultados de la simulación hidrodinámica muestran que la respuesta de la superficie

libre (marea) ( _Figura 12_ ) es coherente con la variación del nivel del mar ( _Figura 5_ ) registrada

en 2019 por el sensor de presión del ADCP instalado en la zona de estudio. También

presenta una variación de las corrientes en superficie, a las profundidades intermedias y de

fondo ( _Figura 13)_ coherente con lo registrado en el año 2019, es decir flujos determinados

principalmente por la variación mareal con flujos al sur en toda la columna de agua.

_Figura 12. Variación del nivel de la mar simulada en verano e invierno obtenida en la posición de fondeo del_

_ADCP de referencia._

_Figura 13. Variación de la corriente superficial simulada en verano e invierno obtenida en la posición de fondeo_

_del ADCP de referencia._

Para realizar la validación se utilizó la marea registrada durante el período de simulación

en la estación de marea del Puerto de Melinka perteneciente al SHOA (los datos se

 descargaron de https:// http://www.ioc sealevelmonitoring.org/). De la comparación de la

serie observada y la simulada ( _Figura 14, panel superior_ ) se puede decir que el modelo

representó apropiadamente la marea en Melinka, con las pleamares levemente más altas.

P á g i n a 17 | 28

La validación se realizó mediante el Diagrama de Taylor (Taylor 2001) de la variación del

nivel del mar horario ( _Figura 14, panel inferior_ ) Ésta permite señalar que la marea fue

levemente subestimada ya que la desviación estándar normalizada fue cercana a 1 (0.99)

y que su correlación con la marea observada fue buena (0.91). Finalmente, la raíz cuadrada

media de los errores fue de 0.42 lo que indica que aun cuando hay diferencias el modelo

hace una buena representación de la marea.

_Figura 14. Validación de la variación del nivel del mar simulado con el registro de la estación de marea de la_

_Estación del Puerto de Melinka_

**3.3** **Dispersión**

En cada periodo de la simulación se obtuvo la concentración máxima de la masa en

suspensión, registrándose la mayor concentración durante la cuadratura (213.64 mg/m [3] ).

La serie de tiempo de la máxima concentración ( _Figura 15_ ) muestra una clara relación con

la magnitud de la corriente, presentándose las mayores concentraciones con las

intensidades de las corrientes más bajas, como se observa en la cuadratura, y las menores

concentraciones con intensidades más altas (sicigia). En ambos casos al término de la

emisión de las partículas virtuales que representan los fármacos se ve cómo la

P á g i n a 18 | 28

concentración de la masa en suspensión se va reduciendo, siendo el decaimiento más

rápido durante la sicigia.

_Figura 15. Variación de la concentración máxima de la masa suspendida en cuadratura y sicigia. El área_

_corresponde al periodo de emisión de las partículas virtuales que representan los fármacos._

La variación espacial de la masa en suspensión ( _Figura 16_ ) muestra que tanto en

cuadratura como en sicigia el núcleo se concentra en torno a las jaulas del centro de cultivo,

sólo después de que se termina la emisión se puede apreciar cómo se dispersa la materia

reduciéndose su concentración. Durante la cuadratura con las corrientes menos intensas la

materia permanece más tiempo en torno al centro, lo que permite alcanzar más altas

concentraciones, en cambio en sicigia las corrientes más intensas incrementan la

dispersión y por ende reducen la concentración. Los transectos ( _Figuras 17 y 18_ ) muestran

como desde el centro la pluma de materia suspendida se dispersa al sur y al norte

principalmente por la transecta costa norte y sur en cuadratura, mientras que en sicigia por

la transecta sur.

P á g i n a 19 | 28

**Cuadratura** **Sicigia**

_Figura 16. Variación espacial de la concentración de masa en suspensión al inicio, al momento de presentarse_

_la máxima concentración y al término._

P á g i n a 20 | 28

_Figura 17. Variación en los transectos en cuadratura de la concentración de masa en suspensión al inicio, al_

_momento de presentarse la máxima concentración y al termino._

P á g i n a 21 | 28

_Figura 18. Variación en los transectos en sicigia de la concentración de masa en suspensión al inicio, al_

_momento de presentarse la máxima concentración y al termino._

**4** **Cálculo de dilución**

Con la información de la masa de cada partícula liberada en las simulaciones se obtuvo la

máxima dilución por minuto, en total se liberaron 237967 partículas que con el tiempo fueron

perdiendo masa. Obteniéndose diluciones máximas desde valores cercanos a cero hasta

un máximo de 0.0018 g/s, un promedio de 0.0011 g/s y una desviación estándar de 0.0028

P á g i n a 22 | 28

g/s, con un predominio de las tasas entre 0.001 y 0.0012 g/min (38.9% de las partículas)

(Figura 19).

_Figura 19. Frecuencia relativa de la máxima tasa de dilución de las partículas numéricas_

_liberadas._

De las modelaciones realizadas, se obtuvo el campo de concentraciones máximas en toda

el área de dispersión de las partículas, para la zona superficial, media agua y fondo. A partir

de estos tres campos de concentraciones máximas, se calculó la tasa de dilución a partir

de la máxima concentración obtenida en la modelación en el punto de emisión. Se obtienen

de esta manera 3 campos de tasa mínima de dilución, lo que corresponde a la condición

más desfavorable (ver _Figura 20_ ), para posteriormente ser aplicadas en la determinación

de la concentración de cada uno de los fármacos, estudio realizado por FOIKE Lab [1], adjunto

en este mismo anexo.

1 Evaluación de Riesgo Ecológico (ERE) para productos veterinarios utilizados en la operación del

Centro Leucayec (Código Centro 110860) en el marco de RCA 371/2008.

P á g i n a 23 | 28

|Col1|Col2|
|---|---|
||MEDIA AGUA|

_Figura 20. Campos de mínima dilución obtenida en las modelaciones, en superficie, media_

_agua y fondo._

**5** **Discusión y Conclusiones**

La comparación de los resultados del modelo hidrodinámico con los registros del ADCP del

año 2019 muestra una buena consistencia en la variación mareal y el comportamiento de

las corrientes en superficie, a media agua y en el fondo. Mientras que la validación con el

diagrama de Taylor con el registro de marea de la estación de Melinka entregó que el

modelo representa de forma realista la variación de marea. Lo que indica que la

combinación de forzante y batimetría utilizada en el modelo permiten representar la

dinámica del sistema en forma apropiada, y por ende representar adecuadamente la

dispersión de la emisión de partículas virtuales que representen la emisión de fármacos.

Los resultados de la simulación de dispersión de la materia en suspensión muestran que

tanto las concentraciones como la dispersión dependen de las corrientes, durante la

P á g i n a 24 | 28

cuadratura cuando el rango mareal es menor y las corrientes menos intensas las

concentraciones de la materia en suspensión son más altas y la dispersión menor. Lo

contrario ocurre en sicigia cuando las concentraciones disminuyen y la dispersión se

incrementa. En ambos periodos después de finalizar la emisión la materia en suspensión

declina hasta reducirse al mínimo, en todo caso cabe tener en cuenta que la simulación es

conservadora al no incluir difusión y degradación de la materia en suspensión.

**6** **Referencias**

**Artal O, O Pizarro & HH Sepúlveda.** **2019** . The impact of spring-neap tidal-stream cycles in tidal

energy assessments in the Chilean Inland Sea. Renewable Energy 139: 496-506.

<https://doi.org/10.1016/j.renene.2019.02.092>.

**Cáceres M, A Valle-Levinson & LP Atkinson.** **2003** . Observations of cross-channel structure of flow

in an energetic tidal channel. Journal of Geophysical Research 108(C4): 3114.

<https://doi.org/10.1029/2001JC000968>.

**Egbert GD & SY Erofeeva.** **2002** . Efficient inverse modeling of barotropic ocean tides. Journal of

Atmospheric and Oceanic Technology 19(2): 183-204. <https://doi.org/10.1175/1520

0426(2002)019<0183:EIMOBO>2.0.CO;2>.

**Guerra M, R Cienfuegos, J Thomson & L Suarez.** **2017** . Tidal energy resource characterization in

Chacao Channel, Chile. International Journal of Marine Energy 20: 1-16.

<https://doi.org/10.1016/j.ijome.2017.11.002>.

**Hersbach H, B Bell, P Berrisford, S Hirahara, A Horányi, J Muñoz-Sabater, J Nicolas, C Peubey,**

**R Radu, D Schepers, A Simmons, C Soci, S Abdalla, X Abellan, G Balsamo, P Bechtold,**

**G Biavati, J Bidlot, M Bonavita, G De Chiara, P Dahlgren, D Dee, M Diamantakis, R**

**Dragani, J Flemming, R Forbes, M Fuentes, A Geer, L Haimberger, S Healy, RJ Hogan, E**

**Hólm, M Janisková, S Keeley, P Laloyaux, P Lopez, C Lupu, G Radnoti, P de Rosnay, I**

**Rozum, F Vamborg, S Villaume & JN Thépaut.** **2020** . The ERA5 global reanalysis. Quarterly

Journal of the Royal Meteorological Society 146(730): 1999-2049.

<https://doi.org/10.1002/qj.3803>.

**Silva N.** **2008** . Dissolved oxygen, pH, and nutrients in the austral Chilean channels and fjords.

Progress in the oceanographic knowledge of Chilean interior waters, from Puerto Montt to Cape

Horn.: 37-43.

**Silva N, C Calvete & HA Sievers.** **1998** . Masas de agua y circulación general para algunos canales

australes chilenos entre Puerto Montt y laguna San Rafael (Crucero CIMAR-Fiordo 1). Ciencia

P á g i n a 25 | 28

y Tecnologia del Mar 21: 17-48.

**Silva N & CA Vargas.** **2014** . Hypoxia in Chilean Patagonian Fjords. Progress in Oceanography 129:

62-74. <https://doi.org/10.1016/j.pocean.2014.05.016>.

**Taylor KE.** **2001** . Summarizing multiple aspects of model performance in a single diagram. Journal

of Geophysical Research: Atmospheres 106(D7): 7183-7192.

<https://doi.org/10.1029/2000JD900719>.

P á g i n a 26 | 28

Profesionales que participaron en el estudio hidrodinámico y su evaluación:

Sergio A. Rosales

Oceanógrafo

Dr(c) en Biología y Ecología Aplicada

Matías E. Gargiulo

Biólogo Marino

P á g i n a 27 | 28

**7** **Anexos**

1. Correntometría ADCP 2019

2. Batimetría multihaz de la zona d estudio

3. Archivos de la modelación

P á g i n a 28 | 28