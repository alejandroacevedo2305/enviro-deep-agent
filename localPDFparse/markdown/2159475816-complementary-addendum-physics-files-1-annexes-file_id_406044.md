---
title: INFORME DE MODELACION DE EMISIONES ATMOSFERICAS
author: IGNACIO GOIC
date: D:20240424170140-04'00'
language: es
type: report
pages: 25
has_toc: False
has_tables: True
extraction_quality: high
---

Modernización Centro Distribución Talcahuano

**INDICE GENERAL**

**1** **INTRODUCCION** **3**

**2** **AREA DE INFLUENCIA** **4**

**3** **LINEA BASE** **6**

**4** **MODELACIÓN DE CONTAMINANTES** **8**

**4.1** **TEORIA DE LA DISPERSIÓN DE LOS CONTAMINANTES.** **8**

**4.2** **MODELO COMPUTACIONAL A UTILIZAR** **13**
**4.3** **METEOROLOGÍA** **13**

**4.4** **ANALISIS DE INCERTIDUMBRE** **14**

**4.5** **TOPOGRAFIA** **15**

**4.6** **RECEPTORES** **16**

**4.7** **DATOS DE LAS FUENTES** **17**
**4.8** **RESULTADOS DE LA MODELACIÓN** **19**

**5** **CONCLUSIONES** **25**

**6** **BIBLIOGRAFÍA** **25**

Informe de Calidad del Aire
Pág. 2

Modernización Centro Distribución Talcahuano

**1** **INTRODUCCION**

El presente proyecto denominado “Modernización Centro de Distribución Talcahuano", se localiza en
la Avenida Las Golondrinas en la parte Sur de la Comuna de Talcahuano, en la Región de Biobío.

El proyecto en evaluación consiste en un mejoramiento de las instalaciones actuales.

Figura 1. Ubicación proyecto.

Proyecto

ENAP - Refinerías.

El presente informe corresponde a la modelación de dispersión de material particulado respirable,
debido a las emisiones generadas por la operación actual, construcción y operación del proyecto.

La modelación se realizará con el modelo AERMod, tal como se menciona en la “Guía para el uso de
modelos de calidad del aire en el SEIA”, publicada por el Servicio de Evaluación Ambiental en 2012,
dado principalmente por la topografía compleja de la zona.

Informe de Calidad del Aire
Pág. 3

Modernización Centro Distribución Talcahuano

**2** **AREA DE INFLUENCIA**

De acuerdo con la definición indicada en la letra a), artículo 2, del RSEIA, el área de influencia de un
Proyecto corresponde “al área o espacio geográfico, cuyos atributos, elementos naturales o
socioculturales deben ser considerados con la finalidad de definir si el Proyecto o actividad genera o
presenta alguno de los efectos, características o circunstancias del artículo 11 de la Ley, o bien para
justificar la inexistencia de dichos efectos, características o circunstancias”.

En este marco, el área de influencia de cada componente ambiental ha considerado la superficie donde
se prevea que el Proyecto podría generar eventualmente algún “Efecto Adverso Significativo sobre la
cantidad y calidad de los recursos naturales renovables, incluidos, suelo, agua y aire”. Para definir dicha
área, se ha tenido en consideración lo siguiente:

- Las características del Proyecto;

- El emplazamiento de las partes del Proyecto, obras o acciones;

- Las etapas del Proyecto (construcción y operación);

- Las características del medio en que se emplaza el Proyecto;

- Las emisiones, efluentes o residuos generados por el Proyecto, que pudieran afectar el medio

ambiente.

Por su parte, la letra d) del artículo 18 del RSEIA, señala que el área de influencia debe ser determinada
y justificada para cada elemento afectado del medio ambiente, tomando en consideración los impactos
ambientales potencialmente significativos sobre ellos, así como el espacio geográfico en el cual se
emplazarán las partes, obras y/o acciones del Proyecto.

Particularmente para la componente Calidad del Aire y siguiendo el lineamiento de la “ _**Guía para la**_
_**Descripción de la Calidad del Aire en el Área de Influencia de Proyectos que Ingresan al SEIA**_ ”,
se determina que, dada la naturaleza de las emisiones del Proyecto, estas son de rápida dispersión y
decantamiento, y también por la geografía del área del Proyecto.

En la comuna de Talcahuano, el proyecto se encuentra en la zona Sur de la comuna adyacente a la
comuna de Hualpén. El proyecto se encuentra dentro del área del PPDA para las comunas de
Concepción Metropolitano, decretado por DS06 de 2018 del Ministerio de Medio Ambiente, que
establece situación de latencia para MP10 y Saturación para MP2.5 en norma diaria.

Los principales efectos potenciales de las actividades del Proyecto sobre la calidad del aire son el
deterioro temporal por emisiones de material particulado y gases de combustión, sobre las áreas de
trabajo durante la etapa de construcción y operación. Éstas son de carácter puntual ya que se
concentran en la zona del Proyecto que originarán la emisión de gases de combustión y material
particulado procedente del uso y tránsito de maquinaria, equipos y camiones.

Por todo lo anterior, el área de influencia se determina como un área cuadrada con el proyecto en el
centro y una arista de 20 km, de modo de incluir las rutas de los servicios durante la construcción y la
operación, tal como se muestra en la Figura 2.

Informe de Calidad del Aire
Pág. 4

Modernización Centro Distribución Talcahuano

Figura 2. Área de influencia del proyecto

Proyecto

Area de influencia

Informe de Calidad del Aire
Pág. 5

Modernización Centro Distribución Talcahuano

**3** **LINEA BASE**

La zona del proyecto esta incluida dentro del Plan de Prevención y Descontaminación Atmosférica para
las comunas de Concepción Metropolitano, establecido en el DS06 de 2018 del Ministerio de Medio
Ambiente. En este PPDA

Este PPDA, establece la condición de Latencia para MP10 y Saturación para MP2.5 en sus normas
diarias. Debido a esto se ha creado una red de estaciones de monitoreo de la calidad del aire,
principalmente para MP10 y MP2.5.

La línea base analizada corresponde al año 2021 en las estaciones de la red SINCA que están cerca
del proyecto que son: Estación Indura, Estación Junji, Estación ENAP Price y Kingston College.

Figura 3. Estaciones de red SINCA cercanas al proyecto.

La estación Kingston College, se ha utilizado como base de la preparación del PPDA y es la que
también aporta los datos de meteorología del proyecto. Las otras estaciones, cuentan con certificación
de EMRP pero solo miden parámetros de calidad del aire, principalmente MP10 y MP2.5.

Informe de Calidad del Aire
Pág. 6

Modernización Centro Distribución Talcahuano

Tabla 1.Niveles de línea base para MP10 y MP2.5 según estación de medición.

|Estación|Indura|Col3|Junji|Col5|ENAP Price|Col7|Kingston College|Col9|
|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**MP10**|**MP2.5**|**MP10**|**MP2.5**|**MP10**|**MP2.5**|**MP10**|**MP2.5**|
|**Enero**|23.61|10.00|35.00|9.13|24.48|8.58|22.48|7.44|
|**Febrero**|26.07|9.86|32.71|10.29|24.36|8.18|18.79|8.19|
|**Marzo**|29.06|11.58|28.30|12.81|26.61|9.74|22.31|9.72|
|**Abril**|25.53|12.43|31.03|17.71|22.60|10.23|21.47|12.00|
|**Mayo**|41.39|26.87|56.38|54.90|33.61|20.03|34.83|25.67|
|**Junio**|39.48|26.84|68.26|55.10|27.70|18.23|34.55|22.68|
|**Julio**|43.39|30.39|58.45|60.26|28.87|19.90|35.52|26.38|
|**Agosto**|33.55|18.81|44.61|33.52|27.83|15.73|31.86|21.14|
|**Septiembre**|25.83|10.20|33.53|20.30|21.14|9.70|21.47|11.83|
|**Octubre**|23.79|7.86|23.97|10.93|24.26|8.87|22.06|8.61|
|**Noviembre**|23.13|7.17|21.40|8.30|25.73|8.00|23.03|6.93|
|**Diciembre**<br>|32.07<br>|10.60<br>|25.27<br>|13.90<br>|45.13<br>|11.63<br>|30.80<br>|10.80<br>|
||||||||||
|**Promedio Anual**|**30.58**|**15.22**|**38.24**|**25.60**|**27.69**|**12.40**|**26.60**|**14.28**|
|**Promedio diario**|**30.73**|**15.38**|**38.17**|**26.06**|**27.78**|**12.43**|**26.74**|**14.43**|

El peor caso de línea base está dado por la estación Junji y serán estos datos los que se utilizaran para
sumar al aporte del proyecto para su comparación con la línea base.

Informe de Calidad del Aire
Pág. 7

Modernización Centro Distribución Talcahuano

**4** **MODELACIÓN DE CONTAMINANTES**

**4.1** **TEORIA DE LA DISPERSIÓN DE LOS CONTAMINANTES.**

La dispersión ocurre cuando un flujo continuo de contaminantes es liberado a la atmósfera abierta, el
cual inicialmente sube y luego el flujo es torcido, por efecto de un viento que disuelve los contaminantes
y los lleva lejos de la fuente, dispersándolo en dirección horizontal y vertical de una línea de centro
imaginaria.

Un esquema de este flujo doblado se presenta en la Figura 4, en donde h corresponde a la altura física
de la chimenea, h es la subida del flujo y H la altura efectiva del flujo disperso. Esta dispersión avanza
desde una concentración alta a una concentración baja. Provocada por diferentes factores, tales como
lo relacionado con la difusión molecular de los componentes de los gases.

**Figura 4: Esquema del efluente.**

**Fuente: Noel de Nevers, Air Pollution Control Engineering, 1995.**

Para una mejor comprensión, se debe recordar que todo flujo turbulento presenta vórtices o remolinos
en distintas direcciones, laterales y verticales, los cuales son fluctuaciones microscópicas irregulares
que al interceptar parte del flujo transforma la concentración de contaminantes en aire limpio a alguna
distancia lejos de la fuente.

Estos remolinos son debidos a influencias térmicas y mecánicas. La energía térmica está dada por la
energía del sol que es absorbida por el suelo y convertida en calor, la que es transmitida a los niveles
más bajos del aire por conducción y convección, creando así los remolinos térmicos. Los remolinos
mecánicos se deben a las fuerzas de corte producidas cuando el aire sopla a través de una superficie
áspera, como es el caso de las superficies con árboles y edificios.

Informe de Calidad del Aire
Pág. 8

Modernización Centro Distribución Talcahuano

Otra razón para el esparcimiento del flujo es el levantamiento irregular de vientos, el que ocurre en
períodos de tiempo inesperados, para lo cual es necesario para la modelación de la dispersión
considerar un período de tiempo en que el viento esté razonablemente quieto, a una velocidad
promedio, k, y dirección x. Como fue descrito por Williamson (1973), el tiempo promedio de
concentración de los contaminantes a una distancia dada, x o, está dada por la componente débil de la
fuente de viento que normalmente es distribuido en la dirección y. Obteniéndose un perfil del flujo
como se muestra en la Figura 5.

**Figura 5 Esquema del efluente instantáneamente y en una hora promedio.**

El perfil de concentración varía a lo largo del eje x, como se muestra en la Figura 6, declinando
continuamente el máximo de la concentración y aumentando el esparcimiento lateral en la dirección y

- z.

**Figura 6 Esquema de las concentraciones en función de la distancia x.**

Informe de Calidad del Aire
Pág. 9

Modernización Centro Distribución Talcahuano

Generalmente se supone que el efluente de una fuente continua tiene una distribución normal (de
Gauss) con relación a la línea central, tanto de la dirección vertical, z (medida desde el suelo), como
de la dirección perpendicular al viento, y. La base de la distribución consiste en que las distribuciones
de los componentes de la velocidad también son casi normales. Sujeta a una condición de continuidad,
la concentración está dada por (incluyendo la reflexión en el suelo).







_Q_  − _y_ 2    − ( _z_ − _H_ ) 2   − ( _z_ + _H_

= exp  2  - exp   2 + exp  2
### 2  u  2  y    2  z   2  z

  − ( _z_ − _H_ ) 2   − ( _z_ + _H_ ) 2 
  2 + exp  2 

 2  _z_   2  _z_ 



 − −

2



  − ( _z_ +

+ exp 
  2



_Q_ − _y_ − ( _z_ − _H_ ) − ( _z_ + _H_ )

exp  2  - exp   2 + exp  2
###  u 2  2  2 

2

_Q_
_C_ =

2

2









2

### 2  u z  2  y    2  z   2  z  

_y_ _z_




donde:
C = concentración lateral en puntos x,y,z, g/m [3]
Q= coeficiente de emisiones, g/s

####  y,  z = parámetros de dispersión horizontal y vertical, m (son funciones de la

distancia x y de la estabilidad de atmósfera.
u = velocidad promedio del viento en la altura de la chimenea.
y = distancia horizontal desde la línea central del flujo.
z = distancia vertical desde el nivel del terreno.
H = altura efectiva (H = h + h, donde h= altura física fuente y h = altura flujo de gases, m)

**Figura 7. Esquema sistema de coordenadas de la distribución Gaussiana en la horizontal y vertical.**

Para calcular los parámetros de dispersión horizontal y vertical se utilizan las ecuaciones dadas por:

## 

_y_

## 

_z_

## = ax b = cx d + _f_

Informe de Calidad del Aire
Pág. 10

Modernización Centro Distribución Talcahuano

Las constantes a, b, c, d y f dependen de la clase de estabilidad atmosférica y de la distancia x
expresada en km. Para obtener sus valores se tienen las tablas siguientes.

**Tabla 2. Clasificaciones** **de** **estabilidad** **atmosférica.**

|Velocidad<br>superficial de<br>Viento (a) m/s|Insolación día solar|Col3|Col4|Índice de nubosidad|Col6|
|---|---|---|---|---|---|
|**Velocidad**<br>**superficial de**<br>**Viento(a) m/s**|**Intenso(b) **|**Moderada(c) **|**Baja(d) **|**Nublado**<br>**4/8**|**Claro**<br>**3/8**|
|<2<br>2-3<br>3-5<br>5-6<br>>6|A <br>A - B<br>B <br>C <br>C|A - B(f) <br>B <br>B - C<br>C - D<br>D|B <br>C <br>C <br>D <br>D|E <br>E <br>D <br>D <br>D|F <br>F <br>E <br>D <br>D|

a. Superficie de viento medida a 10 m sobre el suelo.
b. Corresponde a día de verano despejado con sol alto (60o sobre el horizonte).
c. Corresponde a un día de verano nublado, con el sol 35-60 o sobre el horizonte.
d. corresponde a un día de verano nublado, o en la caída de la tarde, con el sol 15-35o sobre el horizonte.
e. este índice de nubosidad es definido como la fracción del cielo cubierta por nubes.
f. Para las condiciones A - B, B - C o C - D, promedio de valores obtenidos para cada uno.
A = extremadamente inestable. D = Neutra.
B = inestabilidad moderada. E = ligeramente estable.
C = ligeramente inestable. F = moderadamente estable.

**Tabla 3. Valores de constantes de curva de ajuste para calcular los coeficientes de dispersión como**
**función de la distancia de vientos débiles y estabilidad atmosférica.**

|Estabilidad|a|b*|X < 1 km|Col5|Col6|X > 1 km|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Estabilidad**|**a **|**b***|**c **|**d **|**f **|**c **|**d **|**f **|
|A|213|0.894|440.8|1.941|9.27|459.7|2.094|-9.6|
|B|156|0.894|106.6|1.149|3.30|108.2|1.098|2.0|
|C|104|0.894|61.0|0.911|0|61.0|0.911|0|
|D|68|0.894|33.2|0.725|-1.70|44.5|0.516|-13.0|
|E|50.5|0.894|22.8|0.678|-1.30|55.4|0.305|-34.0|
|F|34|0.894|14.35|0.740|-0.35|62.6|0.180|-48.6|

**Fuente: Martin, “The Change of Concentration Standard Deviation with Distance,” Journal Air Pollution**
**Control Association.**

Durante muchos años, las desviaciones normales se obtuvieron con la técnica de Sutton, que se basa
en una selección muy arbitraria de la forma matemática de las funciones de correlación de Lagrange.

#### En la actualidad, es más común el método de Pasquill - Gifford, en el cual se determinan  y y  z

como funciones de x, con gráficas empíricas (ver Figura 8 y 9). Nótese que la dependencia de las
desviaciones normales con respecto a x, varía con la “categoría de estabilidad” (de A a F) mencionadas
en las tablas anteriores.

La principal desventaja del método Pasquill-Gifford radica en que no permite una corrección por la
irregularidad del terreno; las curvas empíricas se obtuvieron con experimentos en terrenos llanos, por
lo que no se tomó en cuenta la dispersión sobre ciudades y otras regiones de superficie irregular.

Informe de Calidad del Aire
Pág. 11

Modernización Centro Distribución Talcahuano

**Figura 8 Nomogramas para la estimación de la dispersión horizontal en función de la distancia corriente**
**abajo y la categoría de estabilidad de Pasquill**

**Figura 9 Nomogramas para la estimación de la dispersión vertical en función de la distancia corriente**
**abajo y la categoría de estabilidad de Pasquill.**

Informe de Calidad del Aire
Pág. 12

Modernización Centro Distribución Talcahuano

**4.2** **MODELO COMPUTACIONAL A UTILIZAR**

La dispersión de contaminantes en la atmósfera se realiza con el modelo computacional AERMOD,
desarrollado por la US EPA (Agencia norteamericana de protección ambiental) en conjunto con
empresas privadas para determinar el impacto en la calidad del aire debido a potencial incorporación
de un proyecto. Este modelo es considerado por el Servicio de Evaluación Ambiental de Chile como
modelo predeterminado para operaciones de corto alcance (menos de 10 km) y para terrenos complejos
según se especifica en la “ **Guía para el Uso de Modelos de Calidad del Aire en el SEIA, 2012** ”. Dado
que el Proyecto se sitúa en la zona urbana del Gran Concepción la cual presenta una geografía plana
en el área de influencia, se utilizará este modelo para estimar el impacto de la dispersión de las
emisiones de MP10 y MP2.5.

AERMOD es un modelo Gaussiano de pluma en estado estacionario que simula la dispersión de los
contaminantes en el aire y su deposición; realiza sus cálculos tomando en cuenta las características
del terreno y la presencia de edificios cercanos a la fuente de emisión, los cuales pueden afectar la
dispersión de la pluma; usa datos del clima de la capa superior atmosférica. Es un modelo regulatorio
de la EPA de Estados Unidos y es considerado como el modelo de última generación.

En Chile, AERMOD está considerado como un modelo de corto alcance, según la “Guía para el uso de
modelos de calidad del aire en el SEIA” desarrollada por el Sistema de Evaluación de Impacto
Ambiental, estipula que el modelo AERMOD se debe utilizar para grillas de máximo 10 km desde la
fuente de emisión.

**4.3** **METEOROLOGÍA**

Los datos meteorológicos corresponden al año 2021 y han sido obtenidos a partir de la Estación
Kingston College, perteneciente a la Subsecretaria de Medio Ambiente, publicado en el sitio web del
[Sistema de Información Nacional de Calidad del Aire (www.sinca.mma.gob.cl).](http://www.sinca.mma.gob.c/)

Como caracterización de la meteorología, se presentan los gráficos de velocidad del viento y dos rosas
de viento correspondientes a un mes de verano (Enero) y uno de invierno (Junio).

**Figura 10. Comportamiento de la velocidad del viento.**

Informe de Calidad del Aire
Pág. 13

Modernización Centro Distribución Talcahuano

**Figura 11. Rosa de vientos para Enero y Junio.**

**4.4** **ANALISIS DE INCERTIDUMBRE**

Cualquier modelo (meteorológico o de calidad del aire) representa una aproximación a la realidad y, en
consecuencia, sus resultados tienen incertidumbres asociadas. Estas incertidumbres se expresan a
través de las diferencias entre lo estimado y las observaciones (o errores del modelo). Además, cabe
enfatizar que existe una propagación de errores desde la modelación meteorológica y la estimación de
emisiones hasta la calidad del aire, lo que resulta en una mayor incertidumbre en esta última.

Para realizar el análisis de incertidumbre se consideraron las recomendaciones establecidas en la
“ **Guía para el uso de Modelos de calidad del aire en el SEIA” elaborada por Servicio de**
**Evaluación Ambiental en 2012**, capítulo 7, que menciona que cualquier modelo representa una
aproximación a la realidad y sus resultados tienen incertidumbres asociadas, las cuales se expresan a
través de diferencias entre lo estimado y lo observado.

Un análisis de incertidumbre tiene como objetivo evaluar la capacidad de un modelo de representar
una cierta situación atmosférica. En este sentido, es importante señalar que este análisis no es ningún
juicio sobre la bondad del modelo o su usuario, sino sólo un reconocimiento de que ningún modelo es
capaz de representar la atmósfera en forma exacta y que, además, su desempeño depende de cada
situación particular.

Sin embargo, el presente proyecto no ha considerado la modelación de las variables meteorológicas,
sino que se han tomado los datos observados de una estación meteorológica con representación
poblacional existente en la zona. Por lo tanto, al no existir una modelación de la información
meteorológica, un análisis de incertidumbre no tiene razón de ser, dado que los datos observados,
utilizados en esta modelación, no se pueden comparar contra ellos mismos.

Informe de Calidad del Aire
Pág. 14

Modernización Centro Distribución Talcahuano

**4.5** **TOPOGRAFIA**

La información topográfica de cada área de emplazamiento del proyecto corresponde a proyecciones
topográficas digitales de las misiones de los transbordadores espaciales SRTM3 (Shuttle Radar
Topography Mission), con mediciones cada 30 metros.

|Figu|ra 12. Proyección top|ográfica de la zona de m|odelación.|Col5|Col6|
|---|---|---|---|---|---|
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||meters|meters|
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||Pro|yecto|||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||||
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||ns|ns|
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto||||Elevatio|Elevatio|
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto|660<br>661<br>662<br>663<br>|||676<br>677<br>Terrain|676<br>677<br>Terrain|
|660<br>661<br>662<br>663<br>664<br>665<br>666<br>667<br>668<br>669<br>670<br>671<br>672<br>673<br>674<br>675<br>676<br>677<br>UTM East [km]<br>5919<br>5920<br>5921<br>5922<br>5923<br>5924<br>5925<br>5926<br>5927<br>5928<br>5929<br>5930<br>5931<br>5932<br>5933<br>5934<br>5935<br>5936<br>5937<br>UTM North [km]<br>meters<br>Terrain Elevations<br>0<br>1<br>5<br>10<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>200<br>211<br>Proyecto|660<br>661<br>662<br>663<br>|664<br>665<br>666<br>667<br>668<br>6|69<br>670<br>671<br>672<br>673<br>674<br>675|69<br>670<br>671<br>672<br>673<br>674<br>675|69<br>670<br>671<br>672<br>673<br>674<br>675|

**Fuente: Elaboración propia a partir de datos de http://www.webgis.com/glcc.html.**

La información relacionada con el uso de suelo de la zona fue obtenida a través de los archivos Global
Land Cover Characterization (GLCC) publicados por el U.S. Geological Survey (USGS) y disponibles
en Internet para utilización abierta en proyectos de variada índole.

El escenario de modelación considera la emisión simultánea de todas las fuentes (de modo de
considerar el peor escenario), a pesar de que en la realidad la emisión proviene por etapas.

Informe de Calidad del Aire
Pág. 15

Modernización Centro Distribución Talcahuano

**4.6** **RECEPTORES**

La modelación ha considerado grillas cuadrada de receptores de 20 km (Este-Oeste) por 20 km (NorteSur) que abarca un área total de 400 km [2] .

La grilla considerada, tiene receptores cada 250 metros, de modo de hacer un análisis fino de la calidad
del aire en el área de desarrollo del Proyecto.

**Figura 13. Proyección grilla de receptores.**

Proyecto

**Fuente: Elaboración propia.**

Informe de Calidad del Aire
Pág. 16

Modernización Centro Distribución Talcahuano

**4.7** **DATOS DE LAS FUENTES**

Para el ingreso al modelo se ha considerado el peor escenario de emisión, esto es el año 2024 durante
la etapa de construcción.

**Tabla 4: Emisiones estimadas para el proyecto**

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **4.7** **DATOS DE LAS FUENTES** Para el ingreso al modelo se ha considerado el peor escenario de emisión, esto es el año 2024 durante la etapa de construcción. -->

**Tabla 4: Emisiones estimadas para el proyecto****

| Año | Fase | MP10 | MP 2,5 | CO | NO<br>X |
| --- | --- | --- | --- | --- | --- |
| **Año** | **Fase** | **ton/año** | **ton/año** | **ton/año** | **ton/año** |
| **2024** | Construcción - Interna | 0.985 | 0.308 | 2.61 | 4.91 |
| **2024** | Construcción - Camiones | 0.582 | 0.065 | 0.00 | 0.09 |
| **2024** | **Total** | **1.567** | **0.373** | **2.61** | **5.00** |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Fuente: DIA Proyecto.** Las emisiones de esta etapa de construcción consisten en actividades consecutivas en el tiempo, por lo que la modelación considera la temporalidad de la carta Gantt del proyecto. -->
<!-- FIN TABLA 4 -->


|Año|Fase|MP10|MP 2,5|CO|NO<br>X|
|---|---|---|---|---|---|
|**Año**|**Fase**|**ton/año**|**ton/año**|**ton/año**|**ton/año**|
|**2024**|Construcción - Interna|0.985|0.308|2.61|4.91|
|**2024**|Construcción - Camiones|0.582|0.065|0.00|0.09|
|**2024**|**Total**|**1.567**|**0.373**|**2.61**|**5.00**|

**Fuente: DIA Proyecto.**

Las emisiones de esta etapa de construcción consisten en actividades consecutivas en el tiempo, por
lo que la modelación considera la temporalidad de la carta Gantt del proyecto.

**Tabla 5: Cronograma etapa de construcción del proyecto**

**Fuente: DIA Proyecto.**

En el caso de la etapa de construcción, se consideran todas las actividades asociadas al sitio como
una fuente de área (movimientos de tierra, operación de maquinaria) que opera en la zona de la
modernización de la instalación actual. El área considerada para esta fuente es de 55.000 m [2 ] con un
funcionamiento de 4.160 horas por año, considerando que la construcción opera 16 horas al día (2
turnos de 8 horas diarias) por 5 días a la semana y 52 semanas por año.

**-**
**Tabla 6: Parámetros de ingreso fuente de área** **Etapa construcción (2024)**

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- modernización de la instalación actual. El área considerada para esta fuente es de 55.000 m [2 ] con un funcionamiento de 4.160 horas por año, considerando que la construcción opera 16 horas al día (2 turnos de 8 horas diarias) por 5 días a la semana y 52 semanas por año. **-** -->

**Tabla 6: Parámetros de ingreso fuente de área** **Etapa construcción (2024)****

| Parámetro | Unidad | Valor |
| --- | --- | --- |
| Superficie del proyecto | m2 | 55,000 |
| Duración de la actividad (12 meses) | s/año | 14,976,000 |
| Máxima emisión MP10 | Ton | 2.61 |
| Emisión MP10 como fuente de área | g/m2/s | 2.89 x 10-6 |
| Máxima emisión MP2.5 | Ton | 0.68 |
| Emisión MP10 como fuente de área | g/m2/s | 5.41 x 10-7 |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Fuente: Elaboración propia.** Informe de Calidad del Aire Pág. 17 -->
<!-- FIN TABLA 6 -->


|Parámetro|Unidad|Valor|
|---|---|---|
|Superficie del proyecto|m2|55,000|
|Duración de la actividad (12 meses)|s/año|14,976,000|
|Máxima emisión MP10|Ton|2.61|
|Emisión MP10 como fuente de área|g/m2/s|2.89 x 10-6|
|Máxima emisión MP2.5|Ton|0.68|
|Emisión MP10 como fuente de área|g/m2/s|5.41 x 10-7|

**Fuente: Elaboración propia.**

Informe de Calidad del Aire
Pág. 17

Modernización Centro Distribución Talcahuano

En el caso de las emisiones de los camiones en rutas hacia materiales, botaderos e insumos, estos se
modelan como fuentes lineales, considerando las distancias asociadas a cada ruta y su
correspondiente flujo de vehículos en cada ruta.

Al hacer el análisis unitario, las emisiones de las vías pavimentadas son las mismas, toda vez que al
dividir la emisión por la distancia, se llega al unitario de emisión de un camión tipo. En el caso de las
vías no pavimentadas, se tiene otro valor debido a que la emisión asociada es distinta.

**-**
**Tabla 7: Parámetros de ingreso fuente lineal** **Etapa construcción (2024)**

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Al hacer el análisis unitario, las emisiones de las vías pavimentadas son las mismas, toda vez que al dividir la emisión por la distancia, se llega al unitario de emisión de un camión tipo. En el caso de las vías no pavimentadas, se tiene otro valor debido a que la emisión asociada es distinta. **-** -->

**Tabla 7: Parámetros de ingreso fuente lineal** **Etapa construcción (2024)****

| Ruta | Longitud<br>km | MP10<br>[g/s/km] | MP 2,5<br>[g/s/km] | CO<br>[g/s/km] | NO<br>X<br>[g/s/km] |
| --- | --- | --- | --- | --- | --- |
| Hormigones | 6.22 | 2.63E-08 | 6.87E-09 | 1.14E-09 | 5.15E-08 |
| Materiales | 9.46 | 2.63E-08 | 6.87E-09 | 1.14E-09 | 5.15E-08 |
| Botadero (Pav) | 12.57 | 2.63E-08 | 6.87E-09 | 1.14E-09 | 5.15E-08 |
| Botadero (No Pav.) | 88.4 | 4.47E-05 | 4.51E-06 | 0.00E+00 | 0.00E+00 |
| RESPEL | 88.4 | 2.63E-08 | 6.87E-09 | 1.14E-09 | 5.15E-08 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Fuente: Elaboración propia.** Informe de Calidad del Aire Pág. 18 -->
<!-- FIN TABLA 7 -->


|Ruta|Longitud<br>km|MP10<br>[g/s/km]|MP 2,5<br>[g/s/km]|CO<br>[g/s/km]|NO<br>X<br>[g/s/km]|
|---|---|---|---|---|---|
|Hormigones|6.22|2.63E-08|6.87E-09|1.14E-09|5.15E-08|
|Materiales|9.46|2.63E-08|6.87E-09|1.14E-09|5.15E-08|
|Botadero (Pav)|12.57|2.63E-08|6.87E-09|1.14E-09|5.15E-08|
|Botadero (No Pav.)|88.4|4.47E-05|4.51E-06|0.00E+00|0.00E+00|
|RESPEL|88.4|2.63E-08|6.87E-09|1.14E-09|5.15E-08|

**Fuente: Elaboración propia.**

Informe de Calidad del Aire
Pág. 18

Modernización Centro Distribución Talcahuano

**4.8** **RESULTADOS DE LA MODELACIÓN**

Dada la naturaleza del proyecto, consistentes principalmente en emisión de material particulado, la
modelación se realiza para Material Particulado respirable (MP10), Material Particulado Fino (MP2.5)
tanto para las normas diarias como anuales.

Debido a que el PPDA y la línea base, principalmente están focalizados en MP10 y MP2.5, la
modelación de dispersión se realizará sobre estos contaminantes.

La siguiente tabla muestra los resultados obtenidos al ejecutar el modelo para determinar la dispersión
de material particulado en cada una de las áreas de influencia.

**Tabla 8: Resultados de modelación caso etapa de Construcción (2024)**

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- modelación de dispersión se realizará sobre estos contaminantes. La siguiente tabla muestra los resultados obtenidos al ejecutar el modelo para determinar la dispersión de material particulado en cada una de las áreas de influencia. -->

**Tabla 8: Resultados de modelación caso etapa de Construcción (2024)****

| Contaminante | Período | Aporte máx<br>[ug/m3N] | Línea Base<br>[ug/m3N] | Total<br>[ug/m3N] | Norma<br>[ug/m3N] | % respecto a<br>norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 24 hr | 1.829 | 38.17 | 40.00 | 130.0 | 1.4% |
| MP10 | Anual | 0.556 | 38.24 | 38.80 | 50.0 | 1.5% |
| MP2.5 | 24 hr | 0.776 | 26.06 | 26.83 | 50.0 | 3.0% |
| MP2.5 | Anual | 0.271 | 25.60 | 25.87 | 20.0 | 1.1% |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Cabe notar que la línea base de MP2.5 para la norma diaria, supera la norma de calidad del aire, que es la razón por lo que se ha generado el PPDA. En el caso de los receptores discretos cercanos al proyecto, se utilizarán los receptores establecidos -->
<!-- FIN TABLA 8 -->


|Contaminante|Período|Aporte máx<br>[ug/m3N]|Línea Base<br>[ug/m3N]|Total<br>[ug/m3N]|Norma<br>[ug/m3N]|% respecto a<br>norma|
|---|---|---|---|---|---|---|
|MP10|24 hr|1.829|38.17|40.00|130.0|1.4%|
|MP10|Anual|0.556|38.24|38.80|50.0|1.5%|
|MP2.5|24 hr|0.776|26.06|26.83|50.0|3.0%|
|MP2.5|Anual|0.271|25.60|25.87|20.0|1.1%|

Cabe notar que la línea base de MP2.5 para la norma diaria, supera la norma de calidad del aire, que
es la razón por lo que se ha generado el PPDA.

En el caso de los receptores discretos cercanos al proyecto, se utilizarán los receptores establecidos
en el estudio de ruido de esta DIA. El aporte en estos receptores sensibles se presenta a continuación.

**-**
**Tabla 9: Resultados de modelación caso etapa de Construcción (2024)** **Receptores discretos**

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En el caso de los receptores discretos cercanos al proyecto, se utilizarán los receptores establecidos en el estudio de ruido de esta DIA. El aporte en estos receptores sensibles se presenta a continuación. **-** -->

**Tabla 9: Resultados de modelación caso etapa de Construcción (2024)** **Receptores discretos****

| Receptores<br>discretos | UTM Este | UTM Norte | MP10-24h<br>[ug/m3N] | MP10-Anual<br>[ug/m3N] | MP2.5-24h<br>[ug/m3N] | MP2.5-Anual<br>[ug/m3N] |
| --- | --- | --- | --- | --- | --- | --- |
| **R1** | 668,979 | 5,928,138 | 1.12 | 0.3 | 0.51 | 0.14 |
| **R2** | 669,477 | 5,927,996 | 0.66 | 0.15 | 0.33 | 0.08 |
| **R3** | 669,237 | 5,928,036 | 0.90 | 0.25 | 0.45 | 0.11 |
| **R4** | 669,011 | 5,928,311 | 1.12 | 0.28 | 0.51 | 0.13 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Según el documento “Criterio de evaluación en el SEIA: impacto de emisiones en zonas saturadas por material particulado respirable MP10 y material particulado fino respirable MP2,5”. Elaborado por Servicio de Evaluación Ambiental, en Septiembre 2023, Primera edición, se establecen 2 criterios para evaluar la significancia de las emisiones. -->
<!-- FIN TABLA 9 -->


|Receptores<br>discretos|UTM Este|UTM Norte|MP10-24h<br>[ug/m3N]|MP10-Anual<br>[ug/m3N]|MP2.5-24h<br>[ug/m3N]|MP2.5-Anual<br>[ug/m3N]|
|---|---|---|---|---|---|---|
|**R1**|668,979|5,928,138|1.12|0.3|0.51|0.14|
|**R2**|669,477|5,927,996|0.66|0.15|0.33|0.08|
|**R3**|669,237|5,928,036|0.90|0.25|0.45|0.11|
|**R4**|669,011|5,928,311|1.12|0.28|0.51|0.13|

Según el documento “Criterio de evaluación en el SEIA: impacto de emisiones en zonas saturadas por
material particulado respirable MP10 y material particulado fino respirable MP2,5”. Elaborado por
Servicio de Evaluación Ambiental, en Septiembre 2023, Primera edición, se establecen 2 criterios para
evaluar la significancia de las emisiones.

En el caso de este proyecto se utiliza el criterio de un proyecto con impacto de menos de 3 años con
una etapa de construcción intensiva en emisiones de 12 meses que luego decaen en la operación, por
lo que se utilizará el criterio de la Tabla 2 del citado criterio.

Informe de Calidad del Aire
Pág. 19

Modernización Centro Distribución Talcahuano

**Tabla 10: Valores de significancia sobre receptores por menos de 3 años (12 meses)**

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Calidad del Aire Pág. 19 Modernización Centro Distribución Talcahuano -->

**Tabla 10: Valores de significancia sobre receptores por menos de 3 años (12 meses)****

| Contaminante | Periodo | Incremento concentración<br>[ug/m3N] |
| --- | --- | --- |
| MP 10 | 24 Horas | 10.00 |
| MP 10 | Anual | 3.00 |
| MP 2.5 | 24 Horas | 5.13 |
| MP 2.5 | Anual | 0.99 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Fuente** : Criterio de evaluación en el SEIA: impacto de emisiones en zonas saturadas por material particulado respirable MP10 y material particulado fino respirable MP2,5”. Servicio de Evaluación Ambiental, en Septiembre 2023. -->
<!-- FIN TABLA 10 -->


|Contaminante|Periodo|Incremento concentración<br>[ug/m3N]|
|---|---|---|
|MP 10|24 Horas|10.00|
|MP 10|Anual|3.00|
|MP 2.5|24 Horas|5.13|
|MP 2.5|Anual|0.99|

**Fuente** : Criterio de evaluación en el SEIA: impacto de emisiones en zonas saturadas por material particulado
respirable MP10 y material particulado fino respirable MP2,5”. Servicio de Evaluación Ambiental, en Septiembre
2023.

Por lo tanto, se aprecia que para ningún receptor discreto se sobre pasa el límite de significancia,
definido en los criterios de evaluación recientemente publicados.

Se presentan los gráficos de iso-concentración de cada uno de los contaminantes para cada una de
sus respectivas áreas de influencia en anexo al final del informe.

Informe de Calidad del Aire
Pág. 20

Modernización Centro Distribución Talcahuano

**Figura 14. Mapa de Iso-concetranción de MP10 en el área del proyecto - Período 24 hrs.**

Informe de Calidad del Aire
Pág. 21

Modernización Centro Distribución Talcahuano

**Figura 15. Mapa de Iso-concetranción de MP10 en el área del proyecto - Período Anual.**

Informe de Calidad del Aire
Pág. 22

Modernización Centro Distribución Talcahuano

**Figura 16. Mapa de Iso-concetranción de MP2.5 en el área del proyecto - Período 24 hrs.**

Informe de Calidad del Aire
Pág. 23

Modernización Centro Distribución Talcahuano

**Figura 17. Mapa de Iso-concetranción de MP2.5 en el área del proyecto - Período Anual.**

Informe de Calidad del Aire
Pág. 24

Modernización Centro Distribución Talcahuano

**5** **CONCLUSIONES**

Desde el punto de vista de dispersión de contaminantes se aprecia que la emisión se dispersa
rápidamente, debido a la baja energía ascendente del flujo de emisión, típico de las actividades de
movimientos de tierra, que al no tener suficiente momentum se dispersa y decae rápidamente, más aún
dada la altura a la que se encuentran las fuentes.

Los resultados de la modelación de dispersión de emisiones atmosféricas permiten confirmar e incluso
reducir el área de influencia del Proyecto, a una zona cuadrada de 2 km de arista, toda vez que, más
allá de 1 km desde la fuente, el aporte del proyecto cae por debajo del 90% del total del aporte, dejando
solo el nivel base.

Se puede apreciar en la tabla 7 y las figuras 14 a 17, que el aporte del proyecto a la calidad del aire
genera un impacto bajo con respecto a la norma de calidad en período diario o con respecto a la línea
base. Se observa que no se superará la norma de calidad de aire para Material Particulado inferior a
10 micrones (MP10), Material Particulado fino (MP2.5) y que el nivel de calidad del aire en el punto de
máximo impacto es inferior a la norma primaria de calidad de aire para Material Particulado inferior a
10 micrones, establecida en el DS12/2022 del Ministerio del Medio Ambiente y para Material Particulado
inferior a 2.5 micrones (PM2.5), establecida en el DS12 de 2011 del Ministerio de Medio Ambiente.

De acuerdo con la guía de _“Criterios de evaluación en el SEIA Impacto de emisiones en zonas_
_saturadas por material particulado respirable MP10 y material particulado fino respirable MP2.5”_, al
observar el impacto en el receptor más cercano al proyecto, este impacto está por debajo de los
umbrales de la tabla 2 de dichos criterios para los receptores dentro del predio, por lo que se concluye
que el proyecto no genera un impacto significativo.

Por lo tanto, se puede concluir que a nivel de calidad del aire el proyecto no genera un impacto
significativo, y que dado el bajo aporte y la rápida dispersión se puede confirmar el área de influencia
inicialmente considerado.

**6** **BIBLIOGRAFÍA**

1. Air Pollution Control Engineering, Noel De Nevers, 1995.
2. Guía para el uso de modelos de calidad del aire en el SEIA, Servicio de Evaluación Ambiental,
2012.
3. Guía para la Descripción de la Calidad del Aire en el Área de Influencia de Proyectos que
Ingresan al SEIA, Servicio de Evaluación Ambiental RM, 2015.
4. Atmospheric dispersion modeling compliance guide, Karl B. Schnelle & Partha R. Dey, 2000.
5. DS12/2022 Establece norma primaria de calidad ambiental para material particulado respirable
MP10, Ministerio del Medio Ambiente.

6. DS12/2011. Establece norma primaria de calidad ambiental para material particulado fino
respirable MP2.5, Ministerio del Medio Ambiente.

Informe de Calidad del Aire
Pág. 25

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Niveles de línea base para MP10 y MP2.5 según estación de medición.**

| Estación | Indura | Col3 | Junji | Col5 | ENAP Price | Col7 | Kingston College | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **MP10** | **MP2.5** | **MP10** | **MP2.5** | **MP10** | **MP2.5** | **MP10** | **MP2.5** |
| **Enero** | 23.61 | 10.00 | 35.00 | 9.13 | 24.48 | 8.58 | 22.48 | 7.44 |
| **Febrero** | 26.07 | 9.86 | 32.71 | 10.29 | 24.36 | 8.18 | 18.79 | 8.19 |
| **Marzo** | 29.06 | 11.58 | 28.30 | 12.81 | 26.61 | 9.74 | 22.31 | 9.72 |
| **Abril** | 25.53 | 12.43 | 31.03 | 17.71 | 22.60 | 10.23 | 21.47 | 12.00 |
| **Mayo** | 41.39 | 26.87 | 56.38 | 54.90 | 33.61 | 20.03 | 34.83 | 25.67 |
| **Junio** | 39.48 | 26.84 | 68.26 | 55.10 | 27.70 | 18.23 | 34.55 | 22.68 |
| **Julio** | 43.39 | 30.39 | 58.45 | 60.26 | 28.87 | 19.90 | 35.52 | 26.38 |
| **Agosto** | 33.55 | 18.81 | 44.61 | 33.52 | 27.83 | 15.73 | 31.86 | 21.14 |
| **Septiembre** | 25.83 | 10.20 | 33.53 | 20.30 | 21.14 | 9.70 | 21.47 | 11.83 |
| **Octubre** | 23.79 | 7.86 | 23.97 | 10.93 | 24.26 | 8.87 | 22.06 | 8.61 |
| **Noviembre** | 23.13 | 7.17 | 21.40 | 8.30 | 25.73 | 8.00 | 23.03 | 6.93 |
| **Diciembre**<br> | 32.07<br> | 10.60<br> | 25.27<br> | 13.90<br> | 45.13<br> | 11.63<br> | 30.80<br> | 10.80<br> |
|  |  |  |  |  |  |  |  |  |
| **Promedio Anual** | **30.58** | **15.22** | **38.24** | **25.60** | **27.69** | **12.40** | **26.60** | **14.28** |
| **Promedio diario** | **30.73** | **15.38** | **38.17** | **26.06** | **27.78** | **12.43** | **26.74** | **14.43** |

**Tabla 2.: Clasificaciones** **de** **estabilidad** **atmosférica.****

| Velocidad<br>superficial de<br>Viento (a) m/s | Insolación día solar | Col3 | Col4 | Índice de nubosidad | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Velocidad**<br>**superficial de**<br>**Viento(a) m/s** | **Intenso(b) ** | **Moderada(c) ** | **Baja(d) ** | **Nublado**<br>**4/8** | **Claro**<br>**3/8** |
| <2<br>2-3<br>3-5<br>5-6<br>>6 | A <br>A - B<br>B <br>C <br>C | A - B(f) <br>B <br>B - C<br>C - D<br>D | B <br>C <br>C <br>D <br>D | E <br>E <br>D <br>D <br>D | F <br>F <br>E <br>D <br>D |

**Tabla 3.: Valores de constantes de curva de ajuste para calcular los coeficientes de dispersión como****

| Estabilidad | a | b* | X < 1 km | Col5 | Col6 | X > 1 km | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estabilidad** | **a ** | **b*** | **c ** | **d ** | **f ** | **c ** | **d ** | **f ** |
| A | 213 | 0.894 | 440.8 | 1.941 | 9.27 | 459.7 | 2.094 | -9.6 |
| B | 156 | 0.894 | 106.6 | 1.149 | 3.30 | 108.2 | 1.098 | 2.0 |
| C | 104 | 0.894 | 61.0 | 0.911 | 0 | 61.0 | 0.911 | 0 |
| D | 68 | 0.894 | 33.2 | 0.725 | -1.70 | 44.5 | 0.516 | -13.0 |
| E | 50.5 | 0.894 | 22.8 | 0.678 | -1.30 | 55.4 | 0.305 | -34.0 |
| F | 34 | 0.894 | 14.35 | 0.740 | -0.35 | 62.6 | 0.180 | -48.6 |
