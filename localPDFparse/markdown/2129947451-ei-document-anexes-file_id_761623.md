---
title: Sin título
author: NAZCA
date: D:20141024172357-03'00'
language: es
type: report
pages: 18
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME MODELACIÓN Y CAPACIDAD DE CARGA “SECTOR OESTE PUNTA DE PARRA, ESTERO CUPQUELAN, COMUNA DE AYSÉN, XI REGIÓN”. Solicitado por: SALMONES CUPQUELÁN S.A. OCTUBRE 2014
-->

# INFORME MODELACIÓN Y CAPACIDAD DE CARGA “SECTOR OESTE PUNTA DE PARRA, ESTERO CUPQUELAN, COMUNA DE AYSÉN, XI REGIÓN”. Solicitado por: SALMONES CUPQUELÁN S.A. OCTUBRE 2014

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

**CONTENIDO**

1. INTRODUCCIÓN ..................................................................................................................................... 3

2. METODOLOGÍA ...................................................................................................................................... 4

3. RESULTADOS.......................................................................................................................................... 8

3.1. Batimetría. ..................................................................................................................................... 8

3.2. Correntometría. ............................................................................................................................. 8

3.3. Modelación Depomod. .................................................................................................................. 9

3.3.1. Cuadratura Lunar. ...................................................................................................................... 9

3.3.2. Sicigia Lunar. ............................................................................................................................ 10

3.4. Índice de Findlay de Capacidad de Carga. ................................................................................... 14

3.4.1. Cuadratura lunar. .................................................................................................................... 14

3.4.2. Sicigia lunar. ............................................................................................................................. 14

4. DISCUSIÓN ........................................................................................................................................... 15

5. CONCLUSIÓN ....................................................................................................................................... 16

6. BIBLIOGRAFÍA ...................................................................................................................................... 17

2

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

**1.** **INTRODUCCIÓN**

La acuicultura constituye una de las actividades económicas que ha experimentado el mayor
crecimiento durante los últimos años. Sin embargo, uno de los problemas importantes que la
industria genera, es el de los fondos marinos impactados bajo los centros de cultivo (Troncoso,
2006; Brooks, 2001).

La contaminación puede definirse como “La presencia en el ambiente de sustancias, elementos,
energía o combinación de ellos, en concentraciones y permanencia superiores o inferiores,
según corresponda, a las establecidas en la legislación vigente” (Ley 19.300/1994, y sus
modificaciones), o también puede definirse como “La acción y efecto de introducir materias o
formas de energía, o introducir condiciones en el agua que, de modo directo o indirecto,
impliquen una alteración perjudicial de su calidad en relación con los usos posteriores o con su
función ecológica” definida por Silva, (1998).

En el caso específico de los cultivos acuícolas, el piso acuático actúa como resumidero de una
gran cantidad de material orgánico particulado de origen natural, el cual puede ser generado
por las comunidades biológicas que lo habitan, o ingresar a esta a través de los ríos,
escurrimiento costero superficial y subsuperficial, precipitaciones y vientos (Libes 1992, Silva
1999).

Los sedimentos tienen una importante función reguladora en el ecosistema acuático debido a la
gran capacidad de almacenaje de materia orgánica y, por lo tanto, de nutrientes. Ellos afectan
el balance de oxígeno de las aguas de fondo y permiten la renovación o liberación de nutrientes
nuevos hacia la columna de agua, lo que finalmente también afecta a la producción de
fitoplancton (Jorgensen, 1996). Por otra parte, se debe tener presente, que en los sedimentos
existe una alta tasa de metabolismo microbial, el que dependiendo de la cantidad de materia
orgánica acumulada y de la tasa de ventilación puede provocar condiciones de hipoxia o anoxia
en los sedimentos y en los estratos suprayacentes de la columna de agua (Libes, 1992; Silva,
1999).

Si el aporte de oxígeno disuelto decae o su demanda se incrementa, se producen cambios
dramáticos en la química del sedimento, en los procesos metabólicos bacterianos dominantes y
en el flujo de nutrientes hacia el agua suprayacente y en la sobrevivencia de los organismos
bentónicos. Para un lugar determinado, la profundidad de la interfase óxido-reductora, puede
cambiar a través del año, dependiendo de la tasa de sedimentación de material orgánico y de la
concentración de oxígeno del agua que se encuentra por sobre el sedimento (Jorgensen, 1996).

La cantidad de alimento sedimentable dependerá de factores tales como la velocidad de la
corriente y la profundidad de la columna de agua (Kautsky y Folke, 1989; Gowen y Bradbury,
1987; Wiesmann, et. al. 1988, Iwama, 1991).

En respuesta a esta problemática, y los requerimientos del Reglamento Ambiental para la
Acuicultura (D.S. No 320 de 2001 y sus modificaciones), que señala en su artículo 18 “ _Los_
_proyectos en sectores de agua y fondo que deban someterse al Sistema de Evaluación de_
_Impacto Ambiental, sólo obtendrán el Permiso Ambiental Sectorial cuando se determine que la_
_futura área de Sedimentación o el decil más profundo de la columna de agua, según_
_corresponda, presenta condiciones aeróbicas._

3

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

_Asimismo se señala, es responsabilidad del titular que su centro opere en niveles compatibles_
_con las capacidades de los cuerpos de aguas lacustres, fluviales y/o marítimos, para lo cual_
_deberá mantener siempre condiciones aeróbicas”._

El presente trabajo utiliza una herramienta que permite evaluar el contenido de carbono
orgánico depositado en el sedimento, producto de la actividad acuícola, relacionado a su vez
con las características hidrodinámicas, batimétricas y de producción del centro. Esta
herramienta se ambienta bajo la aplicación de Software DEPOMOD versión 2.2 y una
plataforma o software integrador Surfer Version 8.0, que facilita la visión de los resultados en 2
dimensiones. La utilidad final de esta herramienta es la evaluación del impacto ambiental en el
fondo marino, con un índice que relaciona el carbono orgánico depositado y la disponibilidad de
oxígeno en el fondo, de acuerdo a las corrientes del sector (Findlay, 1997; Gargiulo, 2007).

El presente trabajo tiene por objetivo presentar los resultados de la conjugación de variables
asociadas a la producción del centro, corrientes representativas del lugar, batimetría,
depositación de carbono orgánico al cabo de un ciclo productivo y el cálculo de un índice de
capacidad de carga.

**2.** **METODOLOGÍA**

Con el fin de obtener una evaluación del carbono orgánico depositado en sedimentos y
determinar los límites permisibles de la matriz receptora de degradar la carga generada en el
proceso productivo, se usará el modelo Depomod versión 2.2 (tomado de Cromey, 2002) y el
cálculo del índice de Impacto sobre la disponibilidad de oxígeno disuelto, a partir del modelo
propuesto por Findlay (1997).

**2.1.** **Depositación de carbono mediante modelo Depomod.**

Para poder estimar el grado de depositación y la cantidad de carbono que es generado en el
proceso productivo del presente proyecto se utilizó el programa Depomod que permite la
integración de variables productivas directamente relacionadas a éste y variables ambientales.

Dentro de estas últimas, la velocidad de corrientes y la batimetría son las más importantes ya
que la primera permite estimar la trayectoria de una partícula a medida que ésta desciende en
la columna de agua, mientras que la batimetría del sector de emplazamiento permite discriminar
si existirán puntos de acumulación de material particulado.

Los datos del proyecto que adquieren una mayor connotación para la modelación del programa
tienen relación con: i) el número de balsas-jaulas y sus dimensiones, ya que de ellas depende
el área que estará generando el aporte de partículas al medio; ii) la cantidad de alimento
suministrado durante todo el ciclo productivo para la biomasa considerada (6000 ton), iii) la
velocidad de sedimentación de las partículas y iv) humedad y digestibilidad del alimento
suministrado.

Del alimento suministrado se desprenden dos in-put de carga orgánica que caen a la matriz
receptora (fondo marino): i) el alimento no consumido, que alcanza al 1% y ii) la cantidad de
fecas que es generada por la biomasa de peces durante el ciclo productivo, alcanzando a un
15% del total de alimento ingerido.

4

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

_Valores de producción_

La tabla 2.1.1 presenta un resumen de los valores (productivos) que son ingresados al
programa Depomod, para la obtención de las tasas de aporte de carbono orgánico (calculados
en base a Cromey et al. 2002).

Tabla 2.1.1. Valores de producción para el programa Depomod.

|Item|Valor|Unidad|
|---|---|---|
|Número de jaulas|26|Un|
|Dimensiones de jaulas|30x30x20|M3|
|Cantidad de alimento|8.752,15|Ton|
|Ciclo productivo|21|meses|
|Tasa de alimentación|534|Kg/jaula/día|
|Factor de conversión|1,48||
|Biomasa|6.000|Ton|

_Variables ambientales._

Las variables ambientales consideradas en la presente modelación fueron las siguientes:

Batimetría. La medición de la profundidad fue desarrollada el día 04 de julio de 2014, mediante
un ecosonda marca Garmin, modelo GPSMap 421S, el cual tiene un transductor que permite
una medición de la profundidad hasta 350 m y un GPS que entrega la posición horizontal.

Los sondajes de profundidad fueron referidos al Datum WGS-84 y graficados en proyección
UTM. La navegación se realizó cuidando de mantener una velocidad constante no superior a
los 5 nudos y con líneas de navegación lo más cercanas posible, abarcando un área de 200
metros más allá del área de concesión. El procesamiento de la información, se realizó con
aplicaciones informáticas y de acuerdo a las Instrucciones Hidrográficas N°5 (SHOA Pub.
3105).

Correntometría. La medición de corrientes se realizó mediante un Correntómetro Perfilador
Acústico Doppler (ADCP) durante un total de 33 días, entre el día 05 de julio y 07 de agosto de
2014, contemplando períodos mareales de cuadratura y sicigia,

En la zona de estudio se instaló un correntómetro del tipo ADCP (Acustic Doppler Current
Profiler), marca Nortek modelo Aquadopp Profiler de 0,4 MHz de frecuencia. El ADCP se
programó para registrar la intensidad y dirección de la corriente cada 10 minutos, y en capas de
2,0 m de espesor en la columna de agua.
_Variables asociadas al alimento y fecas_

Para la modelación se considera una velocidad de sedimentación de las fecas de 0,032 m/s y
un tamaño promedio de 1 μm de diámetro (Cromey 2002).

5

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

La tabla 2.1.2, presenta una tabla que establece la relación entre la tasa sedimentación y el
tamaño del alimento considerado durante todo el ciclo productivo del proyecto.

Tabla 2.1.2. Calibre del pellets y velocidad de sedimentación (Cromey, 2002)

|Calibre|3mm|4mm|6mm|9mm|12mm|Total|
|---|---|---|---|---|---|---|
|Porcentaje|0,99|6,10|29,99|44,16|18,76|100,0|
|Vel. sedimentación|0,076|0,082|0,096|0,122|0,156||

Finalmente el modelo considera supuestos, los cuales se presentan la siguiente tabla.

Tabla 2.1.3. Supuestos del modelo Depomod según Cromey, 2002

|Item|Valor|Unidad|
|---|---|---|
|Contenido de agua en el alimento|9|%|
|Alimento no consumido|3|%|
|Carbono del alimento|49|%|
|Carbono en fecas|30|%|
|Digestibilidad del alimento|85|%|
|Coeficiente de dispersión (eje x)|0,1|m2/s|
|Coeficiente de dispersión (eje y)|0,1|m2/s|
|Coeficiente de dispersión (eje z)|0,001|m2/s|

Las salidas y resultados del programa Depomod se ingresan al programa Surfer Versión 8.0,
obteniendo en forma gráfica y numérica las concentraciones de carbono orgánico sedimentado
durante un año promedio (grC/m [2] /año), lo que finalmente permitirá caracterizar la matriz
receptora y diferenciar el área de influencia del proyecto.

**2.2.** **Cálculo de Indice de Findlay de Capacidad de Carga.**

Realizada la modelación descrita anteriormente, los valores de velocidad promedio de la
corriente y concentración de carbono orgánico en mmolC/m [2] /d son ingresados a una planilla
que nos permitirá, mediante el Índice de Impacto de Findlay, calcular la demanda de oxígeno en
el sedimento.

El índice en comento, diseñado por Findlay y Watling (1997), permite calcular la demanda de
oxígeno del sedimento considerando toda el COT que ha quedado depositado en la matriz
sedimentaria, pudiendo establecerse un límite de corte para clasificar un proyecto como
“ambientalmente sustentable”.

A continuación se detallan las fórmulas que serán utilizadas para establecer el Índice de
Findlay:

6

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

**1. D.O = -32,6 + 1,1 * CD**

Donde: DO= Demanda de Oxígeno
CD= Carbono depositado (mmolC/m [2] /d)

Además, el modelo también entrega la disponibilidad u oferta de oxígeno en el sedimento de
acuerdo a la siguiente fórmula.

**2. Of.O = 736,3 + 672, 6 Log * V**

Donde: Of.O= Oferta de Oxígeno
V= Velocidad de la corriente (m/s)

Teniendo la demanda de oxígeno del sedimento y el oxígeno disponible para oxidar el carbono
depositado, se obtiene el Índice de Impacto de Findlay, donde:

**3. I = Oferta de O2 / Demanda de O2.**

Finamente el Índice de Findlay establece que si:

I > 1 El proyecto tendrá un impacto ambientalmente compatible con la matriz receptora. Existe

mayor disponibilidad de oxígeno que lo demandado, impactos mínimos;

I = 1 El proyecto tendrá un impacto moderado. La disponibilidad y demanda se acercan a la

unidad.

I < 1 El proyecto tendrá un impacto ambientalmente incompatible. La demanda se encuentra

en exceso respecto de la disponibilidad de oxígeno, los sedimentos exhibirán
características anóxicas.

7

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

**3.** **RESULTADOS**

**3.1.** **Batimetría.**

En la Figura 3.1. se observa una pendiente variable aumentando la profundidad hacia el
Sureste, donde se puede llegar a 255 metros, en general las balsas se localizarían entre los
veriles de 68 a 250 metros de profundidad aproximadamente.

**Figura 3.1** . Batimetría y ubicación de los módulos de cultivo. El color rojo corresponde a la
concesión de acuicultura y ubicación de las jaulas.

**3.2.** **Correntometría.**

La velocidad de corrientes característica del área del proyecto permite estimar la trayectoria de
una partícula a medida que ésta desciende en la columna de agua, orientándose generalmente
en el sentido que tiene la dirección de la corriente. Cabe señalar, que el efecto de este forzante
se deja sentir una vez que la partícula desciende más abajo de la red pecera, ya que al interior

8

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

de esta unidad, las partículas son alteradas en su trayectoria por el efecto natatorio de los

peces.

Debido a que el sector de emplazamiento del proyecto corresponde a una zona de canales
interiores, la velocidad de las corrientes puede verse condicionada por factores tales como:
morfología del sector y el ciclo de marea. Esta última responde directamente a la influencia
lunar. En virtud de ello, se simularon dos escenarios distintos desde el punto de vista de la
dinámica de las corrientes. Un primer escenario bajo condición de cuadratura lunar (menores
velocidades de corrientes) y un segundo escenario en sicigia lunar (mayores velocidades de
corrientes).
Los resultados observados para la presente modelación nos entregaron una velocidad
promedio de la capa profunda de 7,0 cm/s en condición de cuadratura lunar y 9,7 cm/s en
sicigia lunar.

**3.3.** **Modelación Depomod.**

**3.3.1. Cuadratura Lunar.**

En una primera modelación ( _**cuadratura**_ ), el modelo Depomod v2.2, predice una tasa máxima
de carbono que alcanza a 5.797,69 gC/m [2] /año y un promedio, considerando todo el sector
depositado, de 503,11 gC/m [2] /año.

La figura 4a) muestra la distribución de las concentraciones detalladas en una escala gráfica de
colores. Se visualiza claramente que existe una aglomeración de la mayor cantidad partículas
hacia el sector norte y oeste de la ubicación de la balas jaulas. Esta área de color verde,
concentra la mayor cantidad de carbono alcanzado una extensión de 0,068 Ha (Figura 5a).

Cabe señalar que a medida que aumenta la distancia desde el sector antes mencionado, las
concentraciones comienzan a disminuir abruptamente hasta alcanzar una concentración de 1
grC/m [2] /año. El área que alberga este nivel de concentración alcanzó a 63 Ha alrededor de la
ubicación de los módulos, mostrando una figura aproximadamente elipsoidal levemente
sesgada hacia el sur, con un eje mayor de 1000 m y un eje menor de 700 m.

A continuación se presenta una estadística de los resultados de la modelación Depomod, donde
se observa la distribución de las frecuencias de la concentración de gramos de carbono
depositada dentro del área de influencia del proyecto. Cabe señalar que, tal como fue indicado,
las altas concentraciones son una componente muy reducida en la modelación total.

9

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

**Figura 2** . Resumen estadístico para la depositación de carbono en sedimento gC/m2/año en el
área total de dispersión. Condición en cuadratura lunar.

**3.3.2. Sicigia Lunar.**

En una segunda modelación ( _**sicigia**_ ) _**,**_ el modelo Depomod v2.2, predice una cantidad máxima
depositada que alcanza a 7.605,55 gC/m [2] /año y un promedio, considerando todo el sector
depositado, de 511,15 gC/m [2] /año.

La figura 4b) denota que la distribución de la máxima concentración de carbono, en la condición
de sicigia, se deposita en el sector norte oeste, al igual que en caso anterior, sin embargo, el
área de cobertura solo alcanza a 0,056 Ha (Figura 5 b)

Si se considera que la mínima concentración detectable es de aproximadamente 1 grC/m [2] /año,
la figura permite estimar que el área de cobertura total del sector del proyecto alcanzaría a 61
Ha. La configuración corresponde a una elipse que estaría levemente inclinada en una dirección
sur, respecto de la ubicación de la balas jaulas (1100 m por 700 m).

A continuación se presenta una estadística de los resultados de la modelación Depomod, donde
se observa la distribución de las frecuencias de la concentración depositada dentro del área de
influencia del proyecto, donde las altas concentraciones son una componente muy reducida en
la modelación total.

10

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén, XI**_
_**Región. Salmones Cupquelán S.A.**_

**Figura 3** . Resumen estadístico para la depositación de carbono en sedimento gC/m [2] /año en el
área total de dispersión, condición en sicigia lunar.

11

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán. Comuna de Aysén. XI Región. Salmones Cupquelán S.A.**_

**A)** Cuadratura lunar **B)** Sicigia lunar

**Figura 4** . Área de dispersión de carbono orgánico gC/m [2] /año de acuerdo a la modelación Depomod V2.2.

a) Cuadratura lunar, b) Sicigia lunar.

12

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán. Comuna de Aysén. XI Región. Salmones Cupquelán S.A.**_

**Figura 5** . Área de mayor depositación de carbono orgánico gC/m [2] /año de acuerdo a la modelación Depomod V2.2.

a) Cuadratura lunar (0,068 Ha), b) Sicigia lunar (0,056 Ha).

13

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén,**_
_**XI Región. Salmones Cupquelán S.A.**_

**3.4.** **Índice de Findlay de Capacidad de Carga.**

**3.4.1. Cuadratura lunar.**

De acuerdo a los resultados obtenidos en la modelación del programa Depomod y la
distribución de la concentración de carbono, su correspondiente transformación de
unidades y la aplicación del modelo de Findlay & Watling, 1997, permiten establecer una
demanda máxima de 924,73 mmol O 2 /m [2] /d por la fauna bentónica, y una disponibilidad de
oxígeno en el sector de 1.304,63 mmol O 2 /m [2] /d.

De esta forma, el Índice de Impacto arroja un valor que oscila entre 1,41 para la máxima
depositación y 11,28 para las depositaciones promedios (Tabla 3.4.1).

<!-- INICIO TABLA 3.4.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- en el sector de 1.399,90 mmol O 2 /m [2] /d. De esta forma, el índice de impacto arroja un valor que oscila entre 1,14 para la máxima depositación y 11,96 para las depositaciones promedios (Tabla 3.4.1). -->

**Tabla 3.4.1: ** . Resumen de resultados de la modelación.**

| Item | Valor en cuadratura | Valor en sicigia |
| --- | --- | --- |
| Corriente promedio de fondo en<br>este proyecto | 7,0 cm/s | 9,7 cm/s |
| Oferta de Oxígeno en el fondo | 1.304,63 mmol<br>O2/m2/día | 1.399,90 mmol<br>O2/m2/día |
| Depositación promedio de carbono | 503,11 gC/m2/año | 511,15 gC/m2/año |
| Demanda Oxígeno con<br>depositación promedio | 115,68 mmol O2/m2/día | 117,00 mmol O2/m2/día |
| Máxima depositación de carbono | 5.797.69 gC/m2/año | 7.605,55 gC/m2/año |
| Demanda máxima Oxígeno con<br>depositación máxima | 924,73 mmol O2/m2/día | 1.223,25 mmol<br>O2/m2/día |
| Índice de Impacto de Findlay<br>valores promedios<br> | 11,28 | 11,96 |
| Índice de Impacto de Findlay *~~1~~<br>valores máximos | 1,41 | 1,14 |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 1 I > 1, El proyecto tiene un impacto ambientalmente compatible con la capacidad del cuerpo de agua en la capa de fondo. I < 1, El proyecto tiene un impacto ambientalmente incompatible con la capacidad del cuerpo de agua en profundidad. -->
<!-- FIN TABLA 3.4.1 -->


**3.4.2. Sicigia lunar.**

Durante el período de sicigia lunar (mayores velocidades de corrientes), los resultados
obtenidos del programa Depomod y su correspondientes transformación de valores
permitieron, a través del cálculo de Findlay & Watling, 1997, obtener una demanda
máxima de 1223,25 mmol O 2 /m [2] /d por la fauna bentónica, y una disponibilidad de oxígeno
en el sector de 1.399,90 mmol O 2 /m [2] /d.

De esta forma, el índice de impacto arroja un valor que oscila entre 1,14 para la máxima
depositación y 11,96 para las depositaciones promedios (Tabla 3.4.1).

**Tabla 3.4.1** . Resumen de resultados de la modelación.

|Item|Valor en cuadratura|Valor en sicigia|
|---|---|---|
|Corriente promedio de fondo en<br>este proyecto|7,0 cm/s|9,7 cm/s|
|Oferta de Oxígeno en el fondo|1.304,63 mmol<br>O2/m2/día|1.399,90 mmol<br>O2/m2/día|
|Depositación promedio de carbono|503,11 gC/m2/año|511,15 gC/m2/año|
|Demanda Oxígeno con<br>depositación promedio|115,68 mmol O2/m2/día|117,00 mmol O2/m2/día|
|Máxima depositación de carbono|5.797.69 gC/m2/año|7.605,55 gC/m2/año|
|Demanda máxima Oxígeno con<br>depositación máxima|924,73 mmol O2/m2/día|1.223,25 mmol<br>O2/m2/día|
|Índice de Impacto de Findlay<br>valores promedios<br>|11,28|11,96|
|Índice de Impacto de Findlay *~~1~~<br>valores máximos|1,41|1,14|

1
I > 1, El proyecto tiene un impacto ambientalmente compatible con la capacidad del cuerpo de agua en la capa de fondo.
I < 1, El proyecto tiene un impacto ambientalmente incompatible con la capacidad del cuerpo de agua en profundidad.

14

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén,**_
_**XI Región. Salmones Cupquelán S.A.**_

**4.** **DISCUSIÓN**

Si bien la modelación es una aproximación matemática de los resultados que pudieran
obtenerse, los resultados entregados en el presente informe nos permiten acceder a una
idea bastante cercana al comportamiento real de la depositación bajo un escenario típico
de un ciclo productivo de salmones.

Es así, que estudios y valores informados en literatura de otras modelaciones alcanzan 3
Kg C/m [2] hasta 12 kg C/m [2] en Pérez _et. al._ 2002, bajo las balsas jaulas en mar. Corner,
2006 ha informado valores de 1,55 Kg C/m [2] /15 días para la costa oeste de Escocia, los
que son equivalentes a 37,0 Kg C/m [2] /año.

En el presente informe el máximo valor de depositación alcanza un valor de 5.797,69
gC/m [2] /año en cuadratura con un promedio de 503,11 gC/m [2] /año, en cambio en sicigia
tenemos que la depositación alcanza 7.605,55 gC/m [2] /año y un promedio de sólo 511,15
gC/m [2] /año. Si se comparan los valores obtenidos en el presente informe con aquellos
descritos en las bibliografía mencionadas, podemos observar que nuestros resultados
están por debajo de las condiciones marinas modeladas en el hemisferio norte. Este
resultado se ve probablemente favorecido por las condiciones hidrodinámicas del sector
(altas corrientes en la columna de agua), con altas profundidades lo que aumenta la
dilución de los productos sedimentados (alimento no consumido y fecas).

Las condiciones antes descritas concuerdan con lo señalado por Hevia et al. (1996), quien
menciona que en lugares con alta dinámica oceanográfica, la dispersión del material
sedimentable es mayor, generando un aumento del área de disposición de este material
lo que permite una mejor reducción del material orgánico por parte de los organismos
bentónicos.

En la mayoría de los sitios de cultivos de salmónidos alrededor del mundo, los reportes de
corrientes oscilan alrededor de 0 a 10 cm/s, esto sugiere que estos sitios pueden
experimentar significativos períodos de tiempo con poco o nada de flujo y que ellos podría
estar limitando la oferta de oxígeno. Findlay (1997) reporta que velocidades menores a
0,3 cm/s, representan un valor límite, donde se pueden observar sedimentos azoicos con
mantos de _Beggiatoa_ sp, indicativo de condiciones con baja concentración de oxígeno En
el presente trabajo en la capa profunda tenemos promedio de corrientes de 7,0 cm/s en
cuadratura y de 9,7 cm/s en sicigia, lo que potencia la oferta de oxígeno.

15

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén,**_
_**XI Región. Salmones Cupquelán S.A.**_

**5.** **CONCLUSIÓN**

El cálculo basado en las modelaciones antes mencionadas, predice que al término de un
ciclo productivo el sedimento se encontraría en _**condiciones aeróbicas**_, considerando los
escenarios de cuadratura y sicigia lunar.

Finalmente, de acuerdo a los resultados obtenidos mediante la modelación Depomod e
Índice de Impacto de Findlay, existiría un impacto ambiental sustentable de acuerdo a la
capacidad de degradación de la matriz receptora.

16

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén,**_
_**XI Región. Salmones Cupquelán S.A.**_

**6.** **BIBLIOGRAFÍA**

**Bravo, Sandra, 2006.** Evolución de la Investigación en la Industria Chilena del Salmón.

Salmociencia, 45-52.

**Brooks, Kenneth. 2001.** An evaluation of the relationship between salmon farm biomass,

organic inputs to sediments, physicochemical changes associated with those
inputs and the infaunal response - with emphasis on total sediment sulfides, total
volatile solids, and oxidationreduction potential as surrogate endpoints for
biological monitoring. The Technical Advisory Group, Care of the British Columbia
Ministry of Environment 2080-A Labieux Road Nanaimo, British Columbia Canada.

**Corner, R.A., A.J. Brooker, T.C. Telfer, L.G. Ross. 2006.** A Fully Integrated GIS-based

Model of Particulate Waste Distribution from Marine Fish-Cage Sites. Aquaculture
258, 299-311.

**Cromey, C. J.; T. D. Nickell, K. D. Black. 2002.** DEPOMOD- Modelling the Deposition

and Biological Effects of Waste Solids from Marine Cage Farms. Aquaculture 214.
211-239

**Cromey, C. J.; T. D. Nickell, K. D. Black, P. G. Provost & C.R Griffiths. 2002.**

Validation of a Fish Farm Waste Resuspension Model by Use of a Particulate
Tracer Discharged from a Point Source in a Costal Environment. Estuaries, Vol 25,
No 5, p 916-929.

**Findlay R. H. & L. Watling. 1997.** Prediction of Benthic Impact for Salmon Net-Pens

Based on the Balance of Benthic Oxygen Supply and Demand. Marine Ecology
Progress Series. Vol 155: 147-157.

**Gargiulo, M. E. 2007.** Evaluación de la Capacidad de Carga en Centros de Cultivo

mediante la Combinación de un Modelo de Dispersión (DEPOMOD) con un
Modelo Basado en el Balance de Oxígeno en Sedimento (Findlay & Watling).
Samociencia. 83-87.

**Gowen, J.R., y Bradbury, N.B., 1987.** The ecological impact of salmonid farming in

coastal waters: a review. Oceanogr. Mar. Biol. Ann. Rev., 25, 563-575.

**Hevia M., H. Rosenthal & R.J. Gowen. 1996.** Modelling Benthic Deposition under Fish

Cages. Journal Appl. Ichthyol. 12:71-74.

**Iwama, G.K. 1991.** Interactions between aquaculture and the environment. Crit. Rev.

Environ. Contr. 21.177-216.

**Jorgensen, B.B. & K. Richardson. 1996.** Eutrophication in coastal marine ecosystems.

American Geophysical Union, Coastal and Estuarine Studies 52, Washington, D.C.
ISBN o-87590-266-9. 273 p.
**Kautsky N., Folke C. 1989** . Management of coastal areas for a sustainable development

of aquaculture. Biota 5: 1-11.

**Libes S. 1992.** An introduction to marine biogeochemistry, 289 p. John Wiley & Sons, Inc.

17

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

_**Modelación y Capacidad de Carga. Sector Oeste Punta de Parra, Estero Cupquelán, Comuna de Aysén,**_
_**XI Región. Salmones Cupquelán S.A.**_

**Perez, O. M.; T.C. Telfer, M. C. M. Beveridge and L. G. Ross. 2002.** Geographical

Information Systems (GIS) as a Simple Tool to Aid Modelling of Particulate Waste
Distribution at Marine Fish Cage Sites. Estuarine, Coastal and Shelf Science. 54,
761-768.

**Silva, C., Olivari, R., y G. Yani. 1999.** Determinación de distritos de aptitud acuícola

mediante la aplicación de sistemas de información geográfica. Invest. Mar.,
Valparaíso, 27: 93-99.

**Troncoso, J.M.,Rojas, X., Millán N.,y G. Schroeder. 2006** . Recuperación de Fondos

Marinos Anaeróbicos, bajo Balsas de Cultivo de Salmones, por medio del
Tratamiento con Hidróxido de Magnesio. Salmociencia, 67-71.

**Wiesmann, D; Scheid, H; & Pfrffer, E. 1988.** Water pollution with phosphorus of dietary

origin by intensively fed rainbow trout (Salmo gairdneri Rich). Aquaculture, 69, 263270.

18

_**NAZCA**_
_**FONO CONTACTO: 65-2715568 77631606 (cel)**_

_**e-mail: asesoriasnazca@gmail.com**_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1.1.: Valores de producción para el programa Depomod.**

| Item | Valor | Unidad |
| --- | --- | --- |
| Número de jaulas | 26 | Un |
| Dimensiones de jaulas | 30x30x20 | M3 |
| Cantidad de alimento | 8.752,15 | Ton |
| Ciclo productivo | 21 | meses |
| Tasa de alimentación | 534 | Kg/jaula/día |
| Factor de conversión | 1,48 |  |
| Biomasa | 6.000 | Ton |

**Tabla 2.1.2.: Calibre del pellets y velocidad de sedimentación (Cromey, 2002)**

| Calibre | 3mm | 4mm | 6mm | 9mm | 12mm | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Porcentaje | 0,99 | 6,10 | 29,99 | 44,16 | 18,76 | 100,0 |
| Vel. sedimentación | 0,076 | 0,082 | 0,096 | 0,122 | 0,156 |  |

**Tabla 2.1.3.: Supuestos del modelo Depomod según Cromey, 2002**

| Item | Valor | Unidad |
| --- | --- | --- |
| Contenido de agua en el alimento | 9 | % |
| Alimento no consumido | 3 | % |
| Carbono del alimento | 49 | % |
| Carbono en fecas | 30 | % |
| Digestibilidad del alimento | 85 | % |
| Coeficiente de dispersión (eje x) | 0,1 | m2/s |
| Coeficiente de dispersión (eje y) | 0,1 | m2/s |
| Coeficiente de dispersión (eje z) | 0,001 | m2/s |
