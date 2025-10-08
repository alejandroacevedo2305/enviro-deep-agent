---
title: SITRANS F M MAG 5100 W
author: Siemens AG
date: D:20110318085900+01'00'
language: es
type: report
pages: 68
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Introducción 1
  - Indicaciones de seguridad 2
  - Descripción 3
  - Instalación y montaje 4
  - Conexión 5
  - Servicio y mantenimiento 6
  - Localización de fallos/Preguntas frecuentes 7
  - Datos técnicos 8
  - Tabla 8- 1 Datos técnicos
-->

Caudalímetros electromagnéticos

**SITRANS F M MAG 5100 W**

Instrucciones de servicio • 11/2010

SITRANS F

Caudalímetros electromagnéticos

SITRANS F M MAG 5100 W Conexión

Instrucciones de servicio

Sensor electromagnético tipo SITRANS F M MAG
5100 W para su uso con transmisores de los tipos
SITRANS F M MAG 5000/6000/6000I

11/2010

A5E03376529-01

[Notas jurídicas ]

Filosofía en la señalización de advertencias y peligros

Este manual contiene las informaciones necesarias para la seguridad personal así como para la prevención de
daños materiales. Las informaciones para su seguridad personal están resaltadas con un triángulo de
advertencia; las informaciones para evitar únicamente daños materiales no llevan dicho triángulo. De acuerdo al
grado de peligro las consignas se representan, de mayor a menor peligro, como sigue.

Si se dan varios niveles de peligro se usa siempre la consigna de seguridad más estricta en cada caso. Si en una
consigna de seguridad con triángulo de advertencia se alarma de posibles daños personales, la misma consigna
puede contener también una advertencia sobre posibles daños materiales.

Personal cualificado

El producto/sistema tratado en esta documentación sólo deberá ser manejado o manipulado por personal
cualificado para la tarea encomendada y observando lo indicado en la documentación correspondiente a la
misma, particularmente las consignas de seguridad y advertencias en ella incluidas. Debido a su formación y
experiencia, el personal cualificado está en condiciones de reconocer riesgos resultantes del manejo o
manipulación de dichos productos/sistemas y de evitar posibles peligros.

Uso previsto o de los productos de Siemens

Considere lo siguiente:

Marcas registradas

Todos los nombres marcados con ® son marcas registradas de Siemens AG. Los restantes nombres y
designaciones contenidos en el presente documento pueden ser marcas registradas cuya utilización por terceros
para sus propios fines puede violar los derechos de sus titulares.

Exención de responsabilidad

Hemos comprobado la concordancia del contenido de esta publicación con el hardware y el software descritos.
Sin embargo, como es imposible excluir desviaciones, no podemos hacernos responsable de la plena
concordancia. El contenido de esta publicación se revisa periódicamente; si es necesario, las posibles las
correcciones se incluyen en la siguiente edición.

Siemens AG Referencia del documento: A5E03376529 Copyright © Siemens AG 2010.
Industry Sector P 03/2011 Sujeto a cambios sin previo aviso

Postfach 48 48
90026 NÜRNBERG

ALEMANIA

Índice

1 Introducción............................................................................................................................................... 5

1.1 Elementos suministrados...............................................................................................................5

1.2 Historia...........................................................................................................................................5

1.3 Más información.............................................................................................................................6

2 Indicaciones de seguridad ......................................................................................................................... 7

2.1 Leyes y directivas ..........................................................................................................................7

2.2 Instalación en áreas con peligro de explosión...............................................................................9

2.3 Certificados ..................................................................................................................................10

3 Descripción.............................................................................................................................................. 11

3.1 Componentes del sistema ...........................................................................................................11

3.2 Principio de funcionamiento.........................................................................................................13

4 Instalación y montaje............................................................................................................................... 15

4.1 Precauciones de seguridad para la instalación ...........................................................................15

4.2 Determinación de una ubicación..................................................................................................16

4.3 Orientación del sensor.................................................................................................................18

4.4 Montaje ........................................................................................................................................19

4.5 Conexión equipotencial................................................................................................................21

5 Conexión ................................................................................................................................................. 23

5.1 Instalación remota........................................................................................................................24

5.2 Verificación de la instalación........................................................................................................26

5.3 Revestimiento ..............................................................................................................................26

5.4 Enterramiento directo...................................................................................................................28

6 Servicio y mantenimiento......................................................................................................................... 29

6.1 Mantenimiento..............................................................................................................................29

6.2 Recalibración ...............................................................................................................................29

6.3 Transporte y almacenamiento .....................................................................................................29

6.4 Reparación de la unidad..............................................................................................................30

6.5 Asistencia técnica ........................................................................................................................30

6.6 Procedimientos de devolución.....................................................................................................31

7 Localización de fallos/Preguntas frecuentes............................................................................................ 33

7.1 Comprobación del sensor............................................................................................................33

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 3

Índice

7.2 Fluctuación de los valores de proceso........................................................................................ 35

8 Datos técnicos ......................................................................................................................................... 37

8.1 MAG 5100 W............................................................................................................................... 37

8.2 Datos del cable ........................................................................................................................... 40

8.3 Efecto de la temperatura sobre la presión de servicio................................................................ 42

8.4 Conductividad del líquido del proceso ........................................................................................ 43

8.5 Selección del revestimiento ........................................................................................................ 44

8.6 Selección del electrodo............................................................................................................... 44

8.7 Nomogramas de caudal.............................................................................................................. 45

8.8 Dimensiones y peso.................................................................................................................... 47

A Anexo ...................................................................................................................................................... 51

A.1 Dimensiones de las contrabridas (métricas)............................................................................... 51

A.2 Configuración de fábrica ............................................................................................................. 53

A.3 Resistencia de la bobina............................................................................................................. 55

A.4 Pedido ......................................................................................................................................... 57

Glosario ................................................................................................................................................... 59

Índice alfabético....................................................................................................................................... 63

SITRANS F M MAG 5100 W

4 Instrucciones de servicio, 11/2010, A5E03376529-01

# Introducción 1

Estas instrucciones contienen toda la información que usted necesita para utilizar este
dispositivo.

Las instrucciones están dirigidas a las personas que realizan la instalación mecánica del
dispositivo, conectándolo electrónicamente, configurando los parámetros y llevando a cabo
la puesta en marcha inicial, así como para los ingenieros de servicio y mantenimiento.

Nota

Incumbe al cliente asegurarse que las instrucciones y directivas contenidas en este manual
sean leídas, entendidas y seguidas por el personal concernido antes de que se instale el
dispositivo.

## 1.1 Elementos suministrados

 - SITRANS F M MAG 5100 W

 - Informe de calibración

 - CD con documentación del SITRANS F M

 - Guía de inicio rápido

## 1.2 Historia

El contenido de estas instrucciones se revisa periódicamente y las correcciones se incluyen
en las ediciones posteriores. Estamos abiertos a cualquier sugerencia que suponga una
mejora.

La siguiente tabla muestra los cambios más importantes registrados en la documentación en
comparación con cada una de las versiones anteriores.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 5

Introducción

1.3 Más información

|Edición|Observaciones|
|---|---|
|11/2010|Actualizaciones menores|
|07/2010|Primera edición<br>Sustituye a la parte MAG 5100 W del manual SITRANS F M (A5E02435647) y las<br>instrucciones MAG 5100 W (A5E00718677)|

## 1.3 Más información

El contenido de estas instrucciones de servicio no altera ningún acuerdo, compromiso o
relación comercial existente o previo ni debe considerarse parte de los mismos. Todas las
obligaciones por parte de Siemens AG figuran en el contrato de compraventa
correspondiente, en el que se incluyen también, íntegra y exclusivamente, las condiciones
de garantía aplicables. Ninguna afirmación contenida aquí modifica la garantía existente o
da lugar a garantías nuevas.

Información del producto en Internet

Las Instrucciones de utilización están disponibles en el CD-ROM entregado junto con el
dispositivo, así como en Internet, en la página principal de Siemens, donde también se
puede encontrar más información sobre la gama de caudalímetros SITRANS F:

[Información del producto en Internet (http://www.siemens.com/flowdocumentation)](http://www.siemens.com/flowdocumentation)

Persona de contacto de ámbito mundial

Si necesita más información o tiene algún problema concreto no cubierto suficientemente en
las instrucciones de servicio, póngase en contacto con su persona de contacto. Puede
encontrar los datos de contacto para su persona de contacto local a través de Internet:

[Persona de contacto local (http://www.automation.siemens.com/partner)](http://www.automation.siemens.com/partner)

Consulte también

Asistencia técnica (Página 30)

SITRANS F M MAG 5100 W

6 Instrucciones de servicio, 11/2010, A5E03376529-01

# Indicaciones de seguridad 2

Nota

No se permiten alteraciones en el producto, incluyendo su apertura o reparaciones
inadecuadas del mismo.

Si no se cumple este requisito, la marca CE y la garantía del fabricante quedarán anuladas.

## 2.1 Leyes y directivas

Requisitos generales

La instalación del equipo debe cumplir con las normas nacionales.

Estándares de seguridad para los instrumentos

El dispositivo ha sido comprobado en la fábrica, basándose en los requisitos de seguridad.
Para mantener este estado durante la vida esperada del dispositivo, deben cumplirse los
requisitos descritos en estas instrucciones de servicio.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 7

Indicaciones de seguridad

2.1 Leyes y directivas

Equipo con la marca CE

Todos los contadores muestran o bien una marca CE o una marca CE seguida de 200, p. ej.

 - CE200: indica que el producto es conforme con:

- DEP 97/23/CE

- DBT 2006/95/CE

- CEM 2004/108/CE

 - CE: indica que el producto es conforme con:

- DBT 2006/95/CE

- CEM 2004/108/CE

Conformidad con la directiva de equipos a presión

La "directiva de equipos a presión" (DEP) es obligatoria para todos los equipos a presión
que se venden dentro de la UE y la Asociación Europea de Libre Comercio (EFTA).

Los productos de Siemens Flow Instruments cumplen la DEP conforme a las tablas que se
incluyen a continuación.

Tabla 2- 1 MAG 5100 W (7ME6580 sólo DN15 ... 600 (1⁄2" ... 24"))

|mm de brida|PN 10|PN 16|PN 40|150 lb|300 lb|
|---|---|---|---|---|---|
|15|N/A|N/A|SEP|SEP|N/A|
|25|N/A|N/A|SEP|SEP|N/A|
|40|N/A|N/A|SEP|SEP|N/A|
|50|N/A|SEP|N/A|SEP|N/A|
|65|N/A|SEP|N/A|SEP|N/A|
|80|N/A|SEP|N/A|SEP|N/A|
|100|SEP|SEP|N/A|SEP|N/A|
|125|N/A|SEP|N/A|DEP|N/A|
|150|N/A|DEP|N/A|DEP|N/A|
|200|SEP|DEP|N/A|DEP|N/A|
|250|DBT|DEP|N/A|DEP|N/A|
|300|DBT|DEP|N/A|DEP|N/A|
|350|DBT|DEP|N/A|DEP|N/A|
|400|DBT|DEP|N/A|DEP|N/A|
|450|DBT|DEP|N/A|DEP|N/A|
|500|DBT|DEP|N/A|DEP|N/A|
|600|DBT|DEP|N/A|DEP|N/A|
|700|DBT|DEP*|N/A|N/A|DEP|
|750|N/A|N/A|N/A|N/A|DEP|
|800|DBT|DEP*|N/A|N/A|DEP|
|900|DBT|DEP*|N/A|N/A|DEP|
|1000|DBT|DEP*|N/A|N/A|DEP|

SITRANS F M MAG 5100 W

8 Instrucciones de servicio, 11/2010, A5E03376529-01

Indicaciones de seguridad

2.2 Instalación en áreas con peligro de explosión

|1050|N/A|N/A|N/A|N/A|DEP|
|---|---|---|---|---|---|
|1100|N/A|N/A|N/A|N/A|DEP|
|1200|DBT|DEP*|N/A|N/A|DEP|

Las abreviaturas de la tabla significan lo siguiente:

|DEP|Producto cubierto por la directiva DEP y sólo disponible como totalmente conforme<br>con DEP|
|---|---|
|DEP*|Producto cubierto por la directiva DEP pero disponible como conforme o no<br>conforme con DEP|
|SEP|Excluido de la directiva DEP bajo la categoría Sound Engineering Practice (buenas<br>prácticas de ingeniería)|
|DBT|Excluido de la directiva DEP bajo la directiva de baja tensión|

## 2.2 Instalación en áreas con peligro de explosión

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 9

Indicaciones de seguridad

2.3 Certificados

Homologaciones para áreas con peligro de explosión

El dispositivo está homologado para uso en área con peligro de explosión y tiene las
siguientes homologaciones:

 - MAG 5100 W DN 15 ... 1200: FM / CSA Clase I, Div. 2

## 2.3 Certificados

Los certificados se encuentran a disposición en Internet y en la documentación incluida en el
CD-ROM suministrado con el dispositivo.

Consulte también

Datos técnicos (Página 37)

## Certificados en Internet (http://www.siemens.com/processinstrumentation/certificates)

SITRANS F M MAG 5100 W

10 Instrucciones de servicio, 11/2010, A5E03376529-01

# Descripción 3

Los sensores de caudal electromagnéticos SITRANS F M se utilizan principalmente en los
siguientes campos:

 - Industria de procesos

 - Industria química

 - Siderurgia

 - Minería

 - Suministro de agua

 - Generación y distribución de energía

 - Petróleo y gas / industria de procesamiento de hidrocarburos

 - Agua y aguas residuales

 - Pulpa y papel

## 3.1 Componentes del sistema

El sistema de caudalímetro SITRANS F M USM II incluye:

 - Transmisor (tipos: SITRANS F M MAG 5000/6000 o MAG 6000 I)

 - Sensor (tipos: SITRANS F M MAG 1100/1100F, MAG 3100/3100 P o MAG 5100 W)

 - Módulo de comunicación (opcional) (tipos: HART, PROFIBUS PA/DP, MODBUS RTU RS
485, Foundation Fieldbus H1, Devicenet)

 - Unidad de memoria SENSORPROM

Soluciones de comunicación

El rango de módulos adicionales del SITRANS F USM II, incluye actualmente HART,
Foundation Fieldbus, MODBUS RTU RS 485, PROFIBUS PA / DP y Devicenet, todos son
compatibles con el transmisor SITRANS F M MAG 6000.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 11

Descripción

3.1 Componentes del sistema

La caja y las bridas del sensor SITRANS F M MAG 5100 W han sido diseñadas en acero al
carbono y la caja de terminales en poliamida reforzada con fibra de vidrio. La tubería de
medida está fabricada en acero inoxidable (AISI 304) y los revestimientos se encuentran
disponibles en goma dura NBR, goma dura de ebonita o EPDM, lo que otorga al sensor una
gran resistencia frente a un amplio rango de sustancias químicas. Los electrodos han sido
fabricados con Hastelloy.

MAG 5100W DN15 ... 40 MAG 5100W DN50 ... 300 MAG 5100W DN350 ... 1200

(7ME6520)

MAG 5100W DN25 ... 2000

(7ME6580)

MAG 5100W, instalación
compacta con MAG
5000/6000 IP67

MAG 5100W, instalación
compacta con MAG 6000 I

Los sensores cuentan con una amplia gama de homologaciones, consulte los Datos
técnicos (Página 37).

SITRANS F M MAG 5100 W

12 Instrucciones de servicio, 11/2010, A5E03376529-01

Descripción

3.2 Principio de funcionamiento

## 3.2 Principio de funcionamiento

El principio de medición de caudal se basa en la ley de Faraday de la inducción
electromagnética.

|Col1|Col2|&DX|
|---|---|---|
||||

|&DPSRPDJQ«WLFR<br>O|Col2|Col3|
|---|---|---|
||||
|O|||
||||
||||

U i = Cuando un conductor eléctrico de longitud L se mueve a velocidad v
perpendicularmente a las líneas de flujo, a través de un campo magnético de intensidad B,
se induce una tensión Ui en los extremos del conductor

U i = L x B x v

 - Ui = Tensión inducida

 - L = Longitud del conductor = Diámetro interior de la tubería = k 1

 - B = Intensidad del campo magnético = k 2

 - v = Velocidad del conductor (medio)

 - k = k 1 x k 2

Ui = k x v, la señal del electrodo es directamente proporcional a la velocidad del fluido

## Principio de funcionamiento

El módulo de corriente de las bobinas genera una corriente pulsante magnetizante que
activa las bobinas del sensor. La corriente se vigila y corrige permanentemente. Un circuito
de autovigilancia registra los errores o fallos de cable.

Un circuito de entrada amplifica la señal de tensión inducida proporcional al flujo proveniente
de los electrodos. La impedancia de entrada es extremadamente alta: >10 [14] Ω permiten
medir el caudal de fluidos con una conductividad mínima de 5 μS/cm. Los errores de
medición producidos por la capacitancia del cable quedan excluidos gracias al apantallado
activo del cable.

El procesador digital de señales convierte la señal analógica de flujo en una señal digital y
suprime los ruidos del electrodo mediante un filtro digital. Cualquier inexactitud del
transmisor, como resultado de derivas a largo plazo y de temperatura, se vigila y compensa
continuamente a través del circuito de autovigilancia. La conversión de señal analógica a
digital tiene lugar en un ASIC de ruido ultra bajo, con una resolución de señal de 23 bits.
Esto permite prescindir de una conmutación de rango. Por lo tanto, el rango dinámico del
transmisor no es rebasado por una rangeabilidad de mínimo 3000:1.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 13

Descripción

3.2 Principio de funcionamiento

SITRANS F M MAG 5100 W

14 Instrucciones de servicio, 11/2010, A5E03376529-01

# Instalación y montaje 4

Los medidores de caudal SITRANS F con un grado de protección mínimo de la caja
IP67/NEMA 4X son idóneos para instalaciones interiores y exteriores.

 - Asegúrese de que las especificaciones de presión y temperatura indicadas en la placa
de características / etiqueta del dispositivo no serán excedidas.

## 4.1 Precauciones de seguridad para la instalación

 - Asegúrese de que los esfuerzos y cargas ocasionados por sismos, el tráfico, vientos
fuertes y daños por incendio, si es pertinente, sean tomados en cuenta durante la
instalación.

 - Asegúrese que el medidor de caudal es instalado de tal manera que no actúe como un
foco de los esfuerzos en la tubería. Las cargas externas no son tomadas en cuenta en el
diseño del medidor de caudal.

 - Proporcione protección adecuada para minimizar cualquier riesgo de contacto con
superficies calientes.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 15

Instalación y montaje

4.2 Determinación de una ubicación

## 4.2 Determinación de una ubicación

 - Ubicar el caudalímetro en tubos en "U" si la tubería está sólo parcialmente llena o tiene
una salida libre

Figura 4-1 Instalación correcta dentro de un tubo en "U"

 - Evite las siguientes instalacionesInstalación en el punto más alto del sistema de tubería

- Instalación en tubos verticales con una salida libre

Figura 4-2 Instalación correcta con tubos llenos

Figura 4-3 Instalación correcta en el punto inferior del sistema delante de la salida

Condiciones de entrada y salida

Para conseguir una medida precisa de caudal es esencial contar con longitudes rectas de
tubos de entrada y salida, así como una cierta distancia a las bombas y las válvulas.

También es importante centrar el caudalímetro con respecto a las bridas y juntas del tubo.

SITRANS F M MAG 5100 W

16 Instrucciones de servicio, 11/2010, A5E03376529-01

Instalación y montaje

4.2 Determinación de una ubicación

Figura 4-4 Condiciones de entrada y salida

Instalación en tubos de grandes dimensiones

El caudalímetro se puede instalar entre dos reductores (p. ej. DIN 28545). A 8° intervienen
las siguientes curvas de pérdida de presión. Estas curvas son aplicables al agua.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 17

Instalación y montaje

4.3 Orientación del sensor

Ejemplo:

Un caudal de 3 m/s (V) en un sensor con una reducción de diámetro de DN 100 a DN 80
(d 1 /d 2 = 0,8) produce una caída de presión de 2,9 mbar.

## 4.3 Orientación del sensor

El sensor funciona en todas las orientaciones, no obstante, Siemens recomienda lo
siguiente:

 - Instalación vertical con un flujo ascendente

Figura 4-5 Orientación vertical, caudal ascendente

SITRANS F M MAG 5100 W

18 Instrucciones de servicio, 11/2010, A5E03376529-01

Instalación y montaje

4.4 Montaje

 - Instalación horizontal con la caja de terminales hacia arriba o hacia abajo

Figura 4-6 Instalación horizontal, diversas posiciones de la caja de terminales

## 4.4 Montaje

 - Instale el sensor en tuberías rígidas para soportar el peso del contador.

 - Centre axialmente las tuberías de conexión para evitar perfiles de flujo con turbulencias.

 - Utilice juntas adecuadas conforme al tipo de revestimiento

Figura 4-7 Instalación correcta con juntas

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 19

Instalación y montaje

4.4 Montaje

Vibraciones

Evite vibraciones fuertes.

Figura 4-8 Evite las vibraciones

Pares

Apriete los tornillos conforme a los valores de par indicados debajo

Figura 4-9 Valores de par

SITRANS F M MAG 5100 W

20 Instrucciones de servicio, 11/2010, A5E03376529-01

Instalación y montaje

4.5 Conexión equipotencial

Tabla 4- 1 Pares máximos permitidos

|DN|Col2|PN 10|Col4|PN 16|Col6|PN 40|Col8|Clase 150|Col10|AWWA|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|mm|Pulga<br>das|Nm|F/lbs|Nm|F/lbs|Nm|F/lbs|Nm|F/lbs|Nm|F/lbs|
|15|1⁄2|N/A|N/A|N/A|N/A|10|7|6|5|N/A|N/A|
|25|1"|N/A|N/A|N/A|N/A|10|7|7|5|N/A|N/A|
|40|11⁄2"|N/A|N/A|N/A|N/A|16|12|9|7|N/A|N/A|
|50|2"|N/A|N/A|N/A|N/A|N/A|N/A|25|18|N/A|N/A|
|65|21⁄2"|N/A|N/A|25/25|18/18|N/A|N/A|25|18|N/A|N/A|
|80|3"|N/A|N/A|25/25|18/18|N/A|N/A|34|25|N/A|N/A|
|100|4"|N/A|N/A|25/25|18/18|N/A|N/A|26|19|N/A|N/A|
|125|5"|N/A|N/A|29/32|21/24|N/A|N/A|42|31|N/A|N/A|
|150|6"|N/A|N/A|50/50|37/37|N/A|N/A|57|42|N/A|N/A|
|200|8"|50/50|37/37|50/52|37/38|N/A|N/A|88|65|N/A|N/A|
|250|10"|50/50|37/37|82/88|61/65|N/A|N/A|99|73|N/A|N/A|
|300|12"|57/62|42/46|111/117|82/86|N/A|N/A|132|97|N/A|N/A|
|350|14"|60/60|44/44|120/120|89/89|N/A|N/A|225|166|N/A|N/A|
|400|16"|88/88|65/65|170/170|125/125|N/A|N/A|210|155|N/A|N/A|
|450|18"|92/92|68/68|170/170|125/125|N/A|N/A|220|162|N/A|N/A|
|500|20"|103/103|76/76|230/230|170/170|N/A|N/A|200|148|N/A|N/A|
|600|24"|161/161|119/119|350/350|258/258|N/A|N/A|280|207|N/A|N/A|
|700|28"|200/200|148/148|304/304|224/224|N/A|N/A|N/A|N/A|200|148|
|750|30"|N/A|N/A|N/A|N/A|N/A|N/A|N/A|N/A|240|177|
|800|32"|274/274|202/202|386/380|285/285|N/A|N/A|N/A|N/A|260|192|
|900|36"|288/288|213/213|408/408|301/301|N/A|N/A|N/A|N/A|240|177|
|1000|40"|382/382|282/282|546/546|403/403|N/A|N/A|N/A|N/A|280|207|
|1050|42"|N/A|N/A|N/A|N/A|N/A|N/A|N/A|N/A|280|207|
|1100|44"|N/A|N/A|N/A|N/A|N/A|N/A|N/A|N/A|290|214|
|1200|48"|395/395|292/292|731/731|539/538|N/A|N/A|N/A|N/A|310|229|
|1400|54"|-/503|-/317|-/736|-/543|N/A|N/A|N/A|N/A|528|389|
|1600|66"|-/684|-/505|-/913|-/674|N/A|N/A|N/A|N/A|698|515|
|1800|72"|-/771|-/569|-/937|-/692|N/A|N/A|N/A|N/A|700|516|
|2000|78"|-/867|-/640|-/1128|-/832|N/A|N/A|N/A|N/A|890|656|

## 4.5 Conexión equipotencial

Para obtener resultados óptimos del sistema de medida, el sensor debe contar con el mismo
potencial eléctrico que el líquido que se desea medir.

Esto se consigue mediante electrodos de puesta a tierra integrados.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 21

Instalación y montaje

4.5 Conexión equipotencial

Figura 4-10 Conexión equipotencial mediante electrodos de puesta a tierra

Tubería con protección catódica

Es preciso prestar especial atención a los sistemas con protección catódica

Figura 4-11 Protección catódica

 - Aísle el sensor de las tuberías con protección catódica utilizando pernos con aislamiento.

 - Utilice cable de derivación entre la brida y la contrabrida

SITRANS F M MAG 5100 W

22 Instrucciones de servicio, 11/2010, A5E03376529-01

# Conexión 5

A continuación se incluye una breve descripción sobre la forma de conectar un sensor
montado a distancia a un transmisor del tipo SITRANS F M MAG 5000 / 6000 o MAG 6000 I.
Para obtener información adicional, p. ej. acerca del cableado de la alimentación y las
salidas, consulte las Instrucciones de servicio para los transmisores correspondientes.

Antes de la conexión

 - Compruebe que los números de serie del sensor y la unidad SENSORPROM®
coinciden.

Especificaciones del cable

 - Para instalar el sensor, utilice únicamente cables con al menos el mismo grado de
protección que éste.

 - La longitud del cable desde el racor hasta los terminales debe ser la más corta posible.
Se deben evitar los bucles de los cables en la caja de terminales.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 23

Conexión

5.1 Instalación remota

 - Para garantizar el grado de protección IP 67, utilice cables con las especificaciones
requeridas.

Consulte también

Datos del cable (Página 40)

## 5.1 Instalación remota

1. Desatornille y retire la tapa de la caja de terminales.

SITRANS F M MAG 5100 W

24 Instrucciones de servicio, 11/2010, A5E03376529-01

Conexión

5.1 Instalación remota

2. Retire la unidad SENSORPROM [®] del sensor e instálela sobre la placa de conexiones del
transmisor, consulte las Instrucciones de servicio correspondientes del transmisor.

3. Utilice prensaestopas NPT 1⁄2" o M20 para los cables de alimentación y de salida.

4. Introduzca y conecte los cables de electrodos y de bobinas como aparece abajo.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 25

Conexión

5.2 Verificación de la instalación

5. Apriete bien los prensaestopas del cable para obtener un sellado óptimo.

## 5.2 Verificación de la instalación

El contador está ahora preparado para iniciar el funcionamiento normal; en referencia a la
puesta en servicio y la configuración de los parámetros, consulte el manual del transmisor
correspondiente.

Antes de poner en marcha la unidad debe comprobarse que:

 - El dispositivo se ha instalado y conectado según lo indicado en las directrices incluidas
en el capítulo 4 Instalación/Montaje (Página 15) y 5 Conexión (Página 23)

## 5.3 Revestimiento

Si el sensor se encuentra enterrado o sumergido de forma permanente, la caja de
terminales debe ser encapsulada mediante gel dieléctrico de silicona (no tóxico,
transparente y autorreparable)

 - Mezcle bien los dos componentes del kit de revestimiento y viértalos en la caja de
terminales.

 - Permita que fragüe durante aproximadamente 24 horas a unos 25°C (77°F). El tiempo de
fraguado aumenta un 100% por cada -10°C (-18°F).

SITRANS F M MAG 5100 W

26 Instrucciones de servicio, 11/2010, A5E03376529-01

Conexión

5.3 Revestimiento

Orientación horizontal Orientación vertical

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 27

Conexión

5.4 Enterramiento directo

## 5.4 Enterramiento directo

Recomendaciones para enterrar directamente el sensor remoto:

 - Compruebe si el recubrimiento de pintura muestra algún daño visible.

 - Utilice conductos de protección.

 - Proteja el sensor con grava de carbón granza como mínimo 3000 mm en torno al sensor.
Esto proporciona algo de drenaje y también evita la formación de aglomeraciones de
tierra en el sensor. También ayuda a localizar el sensor en caso de que sea necesario

excavar.

## Figura 5-1 Enterramiento directo del sensor

SITRANS F M MAG 5100 W

28 Instrucciones de servicio, 11/2010, A5E03376529-01

# Servicio y mantenimiento 6

## 6.1 Mantenimiento

El dispositivo no requiere mantenimiento, sin embargo, se debe realizar una inspección
periódica según las directivas y normas pertinentes.

Una inspección puede incluir la comprobación de:

 - Condiciones ambientales

 - la integridad de sellado de las conexiones de procesos, entradas de cable y tornillos de
la cubierta

 - la fiabilidad de la fuente de alimentación, protección de iluminación y puestas a tierra

## 6.2 Recalibración

Siemens A/S Flow Instruments ofrece un servicio de recalibrado del sensor. Las siguientes
calibraciones son ofrecidas de forma general:

 - calibración de par combinado estándar

Nota

Para la recalibración, la unidad de memoria siempre debe devolverse junto con el sensor

## 6.3 Transporte y almacenamiento

El sensor es una pieza frágil. Los impactos y golpes pueden
provocar la falta de precisión en las mediciones. Por lo tanto,
durante el transporte, el equipo debe estar colocado en la caja de
transporte suministrada por Siemens Flow Instruments. Si no fuera
posible, el embalaje alternativo del sensor debe ser capaz de
soportar los riesgos del transporte.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 29

Servicio y mantenimiento

6.4 Reparación de la unidad

Manipulación

Figura 6-1 Manipulación del sensor

## 6.4 Reparación de la unidad

Nota

Siemens Flow Instruments define los sensores como productos no reparables.

## 6.5 Asistencia técnica

Si tiene cualquier pregunta técnica acerca del dispositivo descrito en estas Instrucciones de
servicio y no encuentra las respuestas correctas, puede contactar con la Asistencia Técnica:

 - A través de la Internet usando la Solicitud de asistencia:

[Solicitud de asistencia (http://www.siemens.com/automation/support-request)](http://www.siemens.com/automation/support-request)

 - Por teléfono:

-
Europa: +49 (0)911 895 7222

- América: +1 423 262 5710

- Asia Pacífico: +86 10 6475 7575

Más información acerca de nuestra asistencia técnica está disponible en la Internet en
## Asistencia técnica (http://support.automation.siemens.com/WW/view/es/16604318)

SITRANS F M MAG 5100 W

30 Instrucciones de servicio, 11/2010, A5E03376529-01

Servicio y mantenimiento

6.6 Procedimientos de devolución

Servicio y Asistencia en la Internet

Además de nuestra documentación, ponemos a su disposición una base de conocimientos
completa en la Internet en:

[Servicio y asistencia (http://www.siemens.com/automation/service&support)](http://www.siemens.com/automation/service&support)

Ahí encontrará:

 - La información más reciente sobre los productos, FAQs (Preguntas frecuentes), consejos
y astucias.

 - Nuestro boletín de noticias, que le brinda la más reciente información acerca de nuestros
productos.

 - Un administrador de conocimientos, para hallar los documentos adecuados para usted.

 - Nuestro tablón de anuncios, donde usuarios y especialistas comparten sus
conocimientos a nivel mundial.

 - Puede hallar a su socio de contacto local para Automatización industrial y Tecnología de
mecanismos de transmisión en nuestra base de datos de socios.

 - Encontrará información sobre el servicio más próximo, reparaciones, repuestos, y mucho
más bajo la sección "Servicios".

Asistencia complementaria

Por favor contacte con su representante y oficinas Siemens locales si tiene preguntas
adicionales acerca del dispositivo.

Halle su socio de contacto en:

[Persona de contacto local (http://www.automation.siemens.com/partner)](http://www.automation.siemens.com/partner)

## 6.6 Procedimientos de devolución

Adjunte el albarán y la nota de transmisión para devolución junto con el formulario de
declaración de descontaminación que se encuentra fuera del embalaje, en una bolsa de
documentos transparente bien sujetada.

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 31

Servicio y mantenimiento

6.6 Procedimientos de devolución

Formularios requeridos

 - Albarán

 - Nota de transmisión para devolución con la siguientes información

[Nota de transmisión (http://support.automation.siemens.com/WW/view/es/16604370)](http://support.automation.siemens.com/WW/view/es/16604370)

-
producto (número de pedido)

-
cantidad de aparatos o piezas de repuesto devueltas

- motivo de la devolución

 - Declaración de Descontaminación

Declaración de descontaminación
[(http://pia.khe.siemens.com/efiles/feldg/files/Service/declaration_of_decontamination_en.](http://pia.khe.siemens.com/efiles/feldg/files/Service/declaration_of_decontamination_en.pdf)
[pdf)](http://pia.khe.siemens.com/efiles/feldg/files/Service/declaration_of_decontamination_en.pdf)

Con esta declaración se certifica que los productos/repuestos devueltos han sido
cuidadosamente limpiados y no presentan residuos.

Si se ha utilizado el aparato con productos tóxicos, cáusticos, inflamables o peligrosos
para el agua, limpiarlo antes de devolverlo mediante enjuague o neutralización.
Asegurarse que no haya sustancias peligrosas en las cavidades. Después, controlar dos
veces el aparato para asegurarse que esté completamente limpio.

No revisaremos el aparato ni los repuestos a menos que la declaración de
descontaminación confirme su descontaminación apropiada. Los envíos sin una
declaración de descontaminación serán limpiados profesionalmente por cuenta de usted
antes de continuar con los siguientes pasos.

Se puede encontrar los formularios en Internet y en el CD entregado con el aparato.

SITRANS F M MAG 5100 W

32 Instrucciones de servicio, 11/2010, A5E03376529-01

# Localización de fallos/Preguntas frecuentes 7

## 7.1 Comprobación del sensor

Requisitos

Para comprobar los sensores SITRANS F M se necesitan los siguientes instrumentos de

ensayo:

 - Medidor digital/multímetro

 - Megaóhmetro

 - (medidor de bobina móvil)

## Comprobación del sensor

Desconecte el transmisor del sensor o sáquelo de la posición remota antes de realizar las
siguientes comprobaciones.

Comprobación de la resistencia de la bobina

 - Mida la resistencia de la bobina entre los números de conexión 85 y 86 utilizando un
medidor digital.
La resistencia debe situarse alrededor de 100 ohmios ±10 ohmios. (Consulte la Tabla de
resistencias de la bobina)

Una lectura baja puede indicar la presencia de humedad dentro de la caja de la bobina o un
cortocircuito en las espiras de la bobina.

Una lectura elevada indicaría un circuito abierto en la bobina.

Comprobación del aislamiento de la bobina

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 33

Localización de fallos/Preguntas frecuentes

7.1 Comprobación del sensor

 - Coloque el megaóhmetro entre el número de conexión 85 y el cuerpo del sensor.
La resistencia debería superar los 20 megohmios.

Una lectura baja del megaóhmetro indicaría que el aislamiento de la bobina está
disminuyendo. Normalmente, esto es debido a la penetración de líquido en la caja de la
bobina.

Los sensores con una resistencia de aislamiento hasta 1 megohmio pueden funcionar aún
de forma satisfactoria pero esto no está garantizado.

Comprobación de la resistencia de los electrodos

 - Mida la resistencia del electrodo entre las conexiones 82 y cero mediante un medidor de
bobina móvil.
Con el sensor lleno de líquido, la resistencia debe situarse entre 5Kohmios y 50Kohmios.
Si el sensor se encuentra vacío, el valor de resistencia será infinito.

 - Repita las mediciones de la resistencia entre las conexiones 83 y cero.
Los resultados deberían ser idénticos.

Si el valor de resistencia es bajo en este caso, puede existir un cortocircuito en los
electrodos o el cableado (en caso de un transmisor montado a distancia). Como alternativa,
puede haber penetrado agua o humedad en la caja de terminales.

Si el valor de resistencia es elevado y la tubería se encuentra completamente llena de
líquido, compruebe lo siguiente:

1. El líquido es conductor eléctrico.

2. Los electrodos no se encuentran recubiertos de grasa o incrustación.

3. El circuito del electrodo no se encuentra abierto

4. El transmisor montado a distancia cuenta con un cable de 3 hilos con un blindaje
completo y continuo desde el sensor hasta el transmisor, incluidas las cajas de conexión
y los rieles de los terminales dentro de los paneles.

5. El blindaje se encuentra conectado al cero o al terminal de tierra (PE) en el sensor.

SITRANS F M MAG 5100 W

34 Instrucciones de servicio, 11/2010, A5E03376529-01

Localización de fallos/Preguntas frecuentes

7.2 Fluctuación de los valores de proceso

## 7.2 Fluctuación de los valores de proceso

Pregunta

¿Por qué fluctúan los valores de proceso mostrados cuando se mueve el cable del
electrodo?

Respuesta

Existen diversas causas para la fluctuación de los valores del proceso:

 - Incrustaciones en los electrodosLimpie los electrodos.

 - Cable de electrodo defectuosoSustituya el cable

 - Conexión de cable incorrectaConecte el cable del electrodo (82, 83, 0 y blindaje) conforme a las instrucciones del
capítulo Conexión (Página 23)

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 35

Localización de fallos/Preguntas frecuentes

7.2 Fluctuación de los valores de proceso

SITRANS F M MAG 5100 W

36 Instrucciones de servicio, 11/2010, A5E03376529-01

# Datos técnicos 8

## 8.1 MAG 5100 W

# Tabla 8- 1 Datos técnicos

Versión MAG 5100W (7ME6520) MAG 5100W (7ME6580)

Característica del producto Principalmente para el mercado

europeo

Revestimiento EPDM o NBR

Diseño y tamaño nominal Sensor cónico:

 - DN 15 ... 300 (1⁄2" ... 12")

Sensor de diámetro interior completo:

 - DN 350 ... 1200 (14" ... 48")

Principio de medición Inducción electromagnética

Principalmente para el mercado no

europeo

Revestimiento de ebonita

Sensor de diámetro interior completo:

- DN 25 ... 2000 (1" ... 78")

DN 25 ... 65 (1" ... 21⁄2"):

- 12,5 Hz / 15 Hz

DN 80 ... 150 (3" ... 6"):

- 6,25 Hz / 7,5 Hz

DN 200 ... 1200 (8" ... 48"):

- 3,125 Hz / 3,75 Hz

DN 1400 ... 2000 (54" ... 78"):

- 1,5625 Hz / 1,875 Hz

Frecuencia de excitación

(Red de alimentación: 50 Hz/60 Hz)

SITRANS F M MAG 5100 W

DN 15 ... 65 (1⁄2" ... 21⁄2"):

- 12,5 Hz / 15 Hz

DN 80 ... 150 (3" ... 6"):

- 6,25 Hz / 7,5 Hz

DN 200 ... 300 (8" ... 12"):

- 3,125 Hz / 3,75 Hz

DN 350 ... 1200 (14" ... 48"):

- 1,5625 Hz / 1,875 Hz

Instrucciones de servicio, 11/2010, A5E03376529-01 37

Datos técnicos

8.1 MAG 5100 W

Tabla 8- 2 Conexiones del proceso

Versión MAG 5100W (7ME6520) MAG 5100W (7ME6580)

EN 1092-1 PN 10 (145 psi):

 - DN 200 ... 300 (8" ... 12")
Bridas de caras planas

PN 10 (145 psi):

 - DN 350 ... 1200 (14" ... 48")

Bridas de caras en relieve

PN 16 (232 psi):

 - DN 50 ... 300 (2" ... 12")
Bridas de caras planas

PN 16 (232 psi):

 - DN 350 ... 1200 (14" ... 48")

Bridas de caras en relieve

PN 40 (580 psi):

 - DN 15 ... 40 (1⁄2" ... 11⁄2")
Bridas de caras planas

Cara en relieve

(EN 1092-1, DIN 3501 y BS4504 tienen
las mismas dimensiones de contacto)

PN 16 (87 psi):

- DN 1400 ... 2000 (54" ... 78")

PN 10 (145 psi):

- DN 200 ... 2000 (8" ... 78")

PN16 (232 psi):

- DN 65 ... 600 (21⁄2" ... 24")

PN 40 (580 psi):

- DN 25 ... 50 (1" ... 2")

ANSI B16.5 Clase 150 lb: 1⁄2" ... 24" Clase 150 lb: 1" ... 24"

AWWA C-207 Clase D:

 - 28" ... 48", bridas de caras planas

AS4087 PN 16 (230 psi):

 - DN 50 ... 1200 (2" ... 48")

Clase D:

- 28" ... 78", bridas de caras planas

PN 16 (230 psi):

- DN 50 ... 1200 (2" ... 48")

JIS B 2220:2004 - K10 (1" ... 24")

Tabla 8- 3 Condiciones de servicio

Versión MAG 5100W (7ME6520) MAG 5100W (7ME6580)

Temperatura ambiente

- Sensor

- Con transmisor compacto

-40 ... +70 °C (-40 ... +158 °F) -40 ... +70 °C (-40 ... +158 °F)

MAG 5000/6000 -20 ... +60 °C (-4 ... +140 °F) -20 ... +60 °C (-4 ... +140 °F)

MAG 6000 I -20 ... +60 °C (-4 ... +140 °F) -20 ... +60 °C (-4 ... +140 °F)

Presión de funcionamiento [bar abs.] [1] DN 15 ... 40 (1⁄2" ... 11⁄2")

0.01 ... 40 bar (0,15 ... 580 psi)

DN 50 ... 300 (2" ... 12")

0.03 ... 20 bar (0,44 ... 290 psi)

DN 350 ... 1200 (14" ... 48")

0.01 ... 16 bar (0,15 ... 232 psi)

Grado de protección de la caja

Estándar IP67 a EN 60529 / NEMA 4X/6 (1
mH 2 O durante 30 minutos)

DN 25 ... 50 (1" ... 2")

0.01 ... 40 bar (0,15 ... 580 psi)

DN 65 ... 1200 (21⁄2" ... 48")

0.01 ... 16 bar (0,15 ... 232 psi)

DN 1400 ... 2000 (54" ... 78")

0.01 ... 10 bar (0,15 ... 145 psi)

IP67 a EN 60529 / NEMA 4X/6 (1
mH 2 O durante 30 minutos)

SITRANS F M MAG 5100 W

38 Instrucciones de servicio, 11/2010, A5E03376529-01

Datos técnicos

8.1 MAG 5100 W

Versión MAG 5100W (7ME6520) MAG 5100W (7ME6580)

Opcional IP68 a EN 60529 / NEMA 6P (10 mH 2 O
continuamente)

IP68 a EN 60529 / NEMA 6P (10 mH 2 O
continuamente)

Categoría de corrosión C4 conforme a ISO 12944-2 C4 conforme a ISO 12944-2

Caída de presión DN 15 y 25 (1⁄2" y 1"):

 - Máx. 20 mbar (0,29 psi) a 1 m/s (3
ft/s)

DN 40 ... 300 (11⁄2" ... 12"):

 - Máx. 25 mbar (0,36 psi) a 3 m/s
(10ft/s)

DN 350 ... 1200 (14" ... 48"):

 - Insignificante

Insignificante

Presión de ensayo 1,5 x PN (donde proceda) 1,5 x PN (donde proceda)

Carga mecánica (vibración) 18 ... 1000 Hz aleatorio en las
direcciones x,y, z durante 2 horas
conforme a EN 60068-2-36

Sensor: 3,17 g

Sensor con transmisor MAG 5000/6000

compacto montado: 3,17 g

Sensor con transmisor MAG 6000 I

compacto montado: 1,14 g

Temperatura del líquido del proceso

18 ... 1000 Hz aleatorio en las

direcciones x,y, z durante 2 horas
conforme a EN 60068-2-36

Sensor: 3,17 g

Sensor con transmisor MAG 5000/6000

compacto montado: 3,17 g

Sensor con transmisor MAG 6000 I

compacto montado: 1,14 g

NBR -10 ... +70 °C (14 ... 158 °F)

EPDM -10 ... +70 °C (14 ... 158 °F)

EPDM (MI-001) +0.1 ... +30 °C (32 ... 76 °C)

Ebonita - -10 ... +70 °C (14 ... 158 °F)

CEM CEM 2004/108/CE CEM 2004/108/CE

La presión máxima de funcionamiento disminuye al aumentar la temperatura de funcionamiento

Tabla 8- 4 Diseño

Versión MAG 5100W (7ME6520) MAG 5100W (7ME6580)

Material de la caja y de la brida Acero al carbono con recubrimiento de
epoxi bicomponente resistente a la
corrosión (mín. 150 μm)

Categoría de corrosión C4 conforme a
ISO 12944-2

Acero al carbono ASTM A 105 con

recubrimiento de epoxi bicomponente
resistente a la corrosión (mín. 150 μm)

Tubería de medición AISI 304 (1.4301) AISI 304 (1.4301)

Electrodos Hastelloy Hastelloy

Electrodos de puesta a tierra (estándar Hastelloy Hastelloy

Caja de conexión Poliamida reforzada con fibra de vidrio Poliamida reforzada con fibra de vidrio

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 39

Datos técnicos

8.2 Datos del cable

Tabla 8- 5 Certificados y homologaciones

Versión MAG 5100W (7ME6520) MAG 5100W (7ME6580)

Calibración DN 15 ... 300:

Calibración estándar de la producción,
el informe de calibración se suministra

con el sensor

Transferencia de custodia (sólo con
MAG 5000/6000 CT)

- Punto cero, 2 x 25 % y 2 x 90 %

DN 350 ... 1200:

- Punto cero, 1 x 25 % y 1 x 90 %

Homologación de patrón OIML R 49
agua fría (Dinamarca y Alemania):

- DN 50 ... 300 (2" ... 12")

MI 001 agua fría (UE):

- DN 50 ... 300 (2" ... 12")

Homologación para agua potable Revestimiento EPDM:

 - Estándar ANSI/NSF 61 (agua fría,
EE.UU.)

 - WRAS (WRc, BS6920 agua fría,
GB)

 - ACS (F)

 - DVGW W270 (D)

 - Belgaqua (NBR)

Revestimiento NBR:

 - Estándar ANSI/NSF 61 (agua fría,
EE.UU., sólo bridas ANSI y AWWA)

Otras homologaciones - MCERTS

 - PED - 97/23 EC [1)], CRN

 - FM Clase 1, Div 2

 - CSA Clase 1, Div 2

Punto cero, 2 x 25 % y 2 x 90 %

- Estándar NSF/ANSI 61 (agua fría,
EE.UU.)

- WRAS (WRc, BS6920 agua fría,
GB)

- PED - 97/23 CE [1) ] (sólo < DN 600 (<
24"))

- FM Clase 1, Div 2

- CSA Clase 1, Div 2

1) : para tamaños superiores a 600 mm (24") en PN 16, conformidad con PED disponible como opción con coste
adicional. La unidad básica dispone de homologación DBT (directiva de baja tensión) y CEM.

## 8.2 Datos del cable

Descripción

|Cable para electrodo o bobina estándar|Col2|
|---|---|
|Cable para electrodo, doble apantallado||
|Kit de cables con cable de bobinas estándar y cable de<br>electrodos con apantallado doble (también disponible como<br>cable de bajo ruido para sensor MAG 1100)||

SITRANS F M MAG 5100 W

40 Instrucciones de servicio, 11/2010, A5E03376529-01

Aplicaciones estándar

Tabla 8- 6 Datos técnicos, cables de aplicación estándar

Datos técnicos

8.2 Datos del cable

Cable de bobinas Cable de

electrodos

estándar

Datos básicos

Resistencia máx. del lazo

N.o de hilos 2 3

Sección mínima 0,5 mm [2] 0,2 mm [2]

Apantallado Sí Sí

Capacitancia máx. N/A 350 pF/m

Temperatura del medio:

< 100 °C 40 Ω N/A

- 200 °C 6 Ω N/A

Prensaestopas del cable en Prensaestopas M20x1,5 - Cable ø 5 ... 13 mm (0,20 ... 0,51 pulgadas)
el sensor y el transmisor Prensaestopas 1⁄2 NPT - cable ø 5 ... 9 mm (0,20 ... 0,35 pulgadas)

Aplicaciones especiales, p. ej. baja conductividad o ruido eléctrico

Tabla 8- 7 Datos técnicos, cables de aplicación especial

Cable de bobinas Cable de electrodos

especial

Datos básicos

No de hilos 3 3

Sección 1.5 mm [2] 0.25 mm [2]

Apantallado Sí Doble

Código de colores Marrón, azul, negro Marrón, azul, negro

Color exterior Gris Gris

Diámetro ext. 7.8 mm 8.1 mm

Conductor Flexible CU Flexible CU

Material aislante PVC PVC

Temperatura ambiente Instalación flexible -5 ... +70°C -5 ... +70°C

(23 ... 158°F) (23 ... 158°F)

Instalación no flexible -30 ... +70°C

(-22 ... 158°F)

-30 ... +70°C

(-22 ... 158°F)

Parámetros del cable

SITRANS F M MAG 5100 W

Capacidad 161.50 pF/m N/A

Inductancia 0.583 μH/m N/A

L/R 43.83 þH/Ω N/A

Instrucciones de servicio, 11/2010, A5E03376529-01 41

Datos técnicos

8.3 Efecto de la temperatura sobre la presión de servicio

## 8.3 Efecto de la temperatura sobre la presión de servicio Efecto de la temperatura sobre la presión de servicio.

Tabla 8- 8 Medidas métricas (presión en bar)

|Especificacion<br>es de las<br>bridas|Clasif. de las<br>bridas|Temperatura (°C)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Especificacion<br>es de las<br>bridas|Clasif. de las<br>bridas|-5|10|50|90|
|Tamaños DN25 ... 2000|Tamaños DN25 ... 2000|Tamaños DN25 ... 2000|Tamaños DN25 ... 2000|Tamaños DN25 ... 2000|Tamaños DN25 ... 2000|
|EN 1092-1|PN 10|10.0|10.0|9.7|9.4|
|EN 1092-1|PN 16|16.0|16.0|15.5|15.1|
|EN 1092-1|PN 40|40.0|40.0|38.7|37.7|
|ANSI B16.5|150 lb|19.7|19.7|19.3|18.0|
|AWWA C-207|Clase D|10.3|10.3|10.3|10.3|
|Tamaños DN 15 ... 300 (sólo referencia 7ME6520)|Tamaños DN 15 ... 300 (sólo referencia 7ME6520)|Tamaños DN 15 ... 300 (sólo referencia 7ME6520)|Tamaños DN 15 ... 300 (sólo referencia 7ME6520)|Tamaños DN 15 ... 300 (sólo referencia 7ME6520)|Tamaños DN 15 ... 300 (sólo referencia 7ME6520)|
|EN 1092-1|PN 10|10.0|10.0|10.0|8.2|
|EN 1092-1|PN 16|10.0|16.0|16.0|13.2|
|EN 1092-1|PN 40|40.0|40.0|38.7|37.7|
|ANSI B16.5|150 lb|10.0|19.7|19.7|16.2|

Tabla 8- 9 Medidas imperiales (presión en psi)

|Especificacion<br>es de las<br>bridas|Clasif. de las<br>bridas|Temperatura (°F)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Especificacion<br>es de las<br>bridas|Clasif. de las<br>bridas|23|50|120|200|
|Tamaños 1" ... 78"|Tamaños 1" ... 78"|Tamaños 1" ... 78"|Tamaños 1" ... 78"|Tamaños 1" ... 78"|Tamaños 1" ... 78"|
|EN 1092-1|PN 10|145|145|141|136|
|EN 1092-1|PN 16|232|232|225|219|
|EN 1092-1|PN 40|580|580|561|547|
|ANSI B16.5|150 lb|286|286|280|261|
|AWWA C-207|Clase D|150|150|150|150l|
|Tamaños 1⁄2"... 12" (sólo referencia 7ME6520)|Tamaños 1⁄2"... 12" (sólo referencia 7ME6520)|Tamaños 1⁄2"... 12" (sólo referencia 7ME6520)|Tamaños 1⁄2"... 12" (sólo referencia 7ME6520)|Tamaños 1⁄2"... 12" (sólo referencia 7ME6520)|Tamaños 1⁄2"... 12" (sólo referencia 7ME6520)|
|EN 1092-1|PN 10|145|145|145|119|
|EN 1092-1|PN 16|145|232|232|191|
|ANSI B16.5|150 lb|145|286|286|235|

SITRANS F M MAG 5100 W

42 Instrucciones de servicio, 11/2010, A5E03376529-01

Datos técnicos

8.4 Conductividad del líquido del proceso

## 8.4 Conductividad del líquido del proceso

Instalación compacta

Líquidos con una conductividad eléctrica ≥ 5 μS/cm.

Instalación remota

Standard cable

[μS/cm]

300

200

Conductivity
of medium

Conductivity
of medium

100

5

5 100 200 300 [m]

150 300 600 900 [ft]

Cabel length

Special cable

[μS/cm]

50

40

30

20

10

5

50 100 200 300 400 500 [m]

150 300 600 900 1200 1500 [ft]

Cable length

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 43

Datos técnicos

8.5 Selección del revestimiento

## 8.5 Selección del revestimiento

|Revestimiento|Aplicaciones|
|---|---|
|EPDM|Aplicaciones para agua potable (no hidrocarburos)|
|Ebonita|Aplicaciones para agua potable, aplicaciones para aguas<br>residuales y algunas aplicaciones químicas|
|NBR|Uso general. Agua potable, agua salina|

|elección del electrodo|Col2|
|---|---|
|Electrodos||
|Hastelloy C|Preferente para la industria del agua y aguas residuales,<br>química, de alimentos y bebidas, así como farmacéutica|

SITRANS F M MAG 5100 W

44 Instrucciones de servicio, 11/2010, A5E03376529-01

Datos técnicos

8.7 Nomogramas de caudal

## 8.7 Nomogramas de caudal

Nomograma de caudal (DN 2 ... DN 2000)

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 45

Datos técnicos

8.7 Nomogramas de caudal

Nomograma de caudal (DN [1] / 12 " ... DN 78")

Las tablas muestran la relación entre la velocidad de flujo v, la cantidad de flujo Q y la
dimensión del sensor DN.

Pautas para la selección del sensor

Rango mínimo de medición: 0 ... 0,25 m/s (0 ... 0,8 ft/s)

Rango máximo de medición: 0 ... 10 m/s (0 ... ft/s)

Normalmente, el tamaño del sensor se selecciona de tal manera que la velocidad nominal
de flujo v quede dentro del rango de medición 1 ... 3 m/s (1 ... 15 ft/s).

SITRANS F M MAG 5100 W

46 Instrucciones de servicio, 11/2010, A5E03376529-01

Datos técnicos

8.8 Dimensiones y peso

Fórmula de cálculo de la velocidad de flujo:

(medidas métricas)

1273.24 x Q [l/s] 353.68 x Q [m [3] /h]
V = [m/s] or V = [m/s]
DN [2 ] [mm] DN [2 ] [mm]

(medidas imperiales)

0.408 x Q [GPM] 283.67 x Q [MGD]
V = [ft/s] or V = [ft/s]
(Pipe ID) [2 ] [inch] (Pipe ID) [2 ] [inch]

## 8.8 Dimensiones y peso

[0 
 [0 [0

ರ137

/ /

|Col1| <br> | <br>0<br><br>$|
|---|---|---|
|/<br><br>$|/<br><br>$|/<br><br>$|

|Col1|<br>0<br>|
|---|---|
|$|$|
|$|$|

Figura 8-1 MAG 5100 W con MAG 6000 I / MAG 6000 I Ex d


 





|$|0<br>ರ13|
|---|---|
|<br>$<br>||

Figura 8-2 MAG 5100 W con MAG 5000 / 6000

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 47

Datos técnicos

8.8 Dimensiones y peso

Dimensiones

|Tabla 8- 10 Tamaño nominal A|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Tamaño nominal|Tamaño nominal|A|A|A|A|
|Tamaño nominal|Tamaño nominal|Referencia<br>7ME6520, revestimiento NBR o EPDM|Referencia<br>7ME6520, revestimiento NBR o EPDM|Referencia<br>7ME6580, revestimiento de ebonita|Referencia<br>7ME6580, revestimiento de ebonita|
|mm|pulgadas|mm|pulgadas|mm|pulgadas|
|15|1⁄2|177|7|-|-|
|25|1|187|7.4|187|7.4|
|40|11⁄2|202|8|197|7.8|
|50|2|188|7.4|205|8.1|
|65|21⁄2|194|7.6|212|8.3|
|80|3|200|7.9|222|8.7|
|100|4|207|8.1|242|9.5|
|125|5|217|8.5|255|10.0|
|150|6|232|9.1|276|10.9|
|200|8|257|10.1|304|12.0|
|250|10|284|11.2|332|13.1|
|300|12|310|12.2|357|14.1|
|350|14|382|15.0|362|14.3|
|400|16|407|16.0|387|15.2|
|450|18|438|17.2|418|16.5|
|500|20|463|18.2|443|17.4|
|600|24|514|20.2|494|19.4|
|700|28|564|22.2|544|21.4|
|750|30|591|23.3|571|22.5|
|800|32|616|24.3|606|23.9|
|900|36|663|26.1|653|25.7|
|1000|40|714|28.1|704|27.7|
|1050|42|714|28.1|704|27.7|
|1100|44|765|30.1|755|29.7|
|1200|48|820|32.3|810|31.9|
|1400|54|N/D|N/D|925|36.4|
|1500|60|N/D|N/D|972|38.2|
|1600|66|N/D|N/D|1025|40.4|
|1800|72|N/D|N/D|1123|44.2|
|2000|78|N/D|N/D|1223|48.1|

SITRANS F M MAG 5100 W

48 Instrucciones de servicio, 11/2010, A5E03376529-01

Datos técnicos

8.8 Dimensiones y peso

Tabla 8- 11 Tamaño nominal L

|Tamaño<br>nominal|Col2|L|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tamaño<br>nominal|Tamaño<br>nominal|PN 10|PN 10|PN 16|PN 16|PN 16<br>No DEP|PN 16<br>No DEP|PN 40|PN 40|Clase 150<br>AWWA|Clase 150<br>AWWA|AS / JIS10K|AS / JIS10K|
|mm|pul-<br>gadas|mm|pul-<br>gadas|mm|pul-<br>gadas|mm|pulgadas|mm|pulgadas|mm|pulgadas|mm|pulga-<br>das|
|15|1⁄2|N/D|N/D|N/D|N/D|N/D|N/D|200|7.9|200|7.9|N/D|N/D|
|25|1|N/D|N/D|N/D|N/D|N/D|N/D|200|7.9|200|7.9|200|7.9|
|40|11⁄2|N/D|N/D|N/D|N/D|N/D|N/D|200|7.9|200|7.9|200|7.9|
|50|2|N/D|N/D|200|7.9|N/D|N/D|N/D|N/D|200|7.9|200|7.9|
|65|21⁄2|N/D|N/D|200|7.9|N/D|N/D|N/D|N/D|200|7.9|200|7.9|
|80|3|N/D|N/D|200|7.9|N/D|N/D|N/D|N/D|200|7.9|200|7.9|
|100|4|N/D|N/D|250|9.8|N/D|N/D|N/D|N/D|250|9.8|250|9.8|
|125|5|N/D|N/D|250|9.8|N/D|N/D|N/D|N/D|250|9.8|2501)|9.81)|
|150|6|N/D|N/D|300|11.8|N/D|N/D|N/D|N/D|300|11.8|300|11.8|
|200|8|350|13.8|350|13.8|N/D|N/D|N/D|N/D|350|13.8|350|13.8|
|250|10|450|17.7|450|17.7|N/D|N/D|N/D|N/D|450|17.7|450|17.7|
|300|12|500|19.7|500|19.7|N/D|N/D|N/D|N/D|500|19.7|500|19.7|
|350|14|550|21.7|550|21.7|N/D|N/D|N/D|N/D|550|21.7|550|21.7|
|400|16|600|23.6|600|23.6|N/D|N/D|N/D|N/D|600|23.6|N/D|23.6|
|450|18|600|23.6|600|23.6|N/D|N/D|N/D|N/D|600|23.6|600|23.6|
|500|20|600|23.6|600|23.6|N/D|N/D|N/D|N/D|600|23.6|600|23.6|
|600|24|600|23.6|600|23.6|N/D|N/D|N/D|N/D|600|23.6|600|23.6|
|700|28|700|27.6|700|27.6|N/D|N/D|N/D|N/D|700|27.6|7002)|27.62)|
|750|30|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|750|29.5|7502)|N/D|
|800|32|800|31.5|800|31.5|N/D|N/D|N/D|N/D|800|31.5|8002)|31.52)|
|900|36|900|35.4|900|35.4|N/D|N/D|N/D|N/D|900|35.4|9002)|35.42)|
|1000|40|1000|39.4|1000|39.4|N/D|N/D|N/D|N/D|1000|39.4|10002)|39.42)|
|1050|42|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|1000|39.4|N/D|N/D|
|1100|44|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|1100|43.3|N/D|N/D|
|1200|48|1200|47.2|1200|47.2|N/D|N/D|N/D|N/D|1200|47.2|12002)|47.22)|
|1400|54|1400|55.1|N/D|N/D|1400|55.1|N/D|N/D|1200|47.2|N/D|N/D|
|1500|60|1500|59.1|N/D|N/D|1500|59.1|N/D|N/D|1200|47.2|N/D|N/D|
|1600|66|1600|63.0|N/D|N/D|1600|63.0|N/D|N/D|1200|47.2|N/D|N/D|
|1800|72|1800|70.9|N/D|N/D|1800|70.9|N/D|N/D|1200|47.2|N/D|N/D|
|2000|78|2000|78.7|N/D|N/D|2000|78.7|N/D|N/D|1200|47.2|N/D|N/D|

1) No disponible con brida AS

2) No disponible con brida JIS 10K

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 49

Datos técnicos

8.8 Dimensiones y peso

Peso

Tabla 8- 12 Peso

|Tamaño<br>nominal|Col2|Referencia<br>7ME6520|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Referencia<br>7ME6580|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tamaño<br>nominal|Tamaño<br>nominal|PN 10|PN 10|PN 16|PN 16|PN 40|PN 40|Clase 150 /<br>AWWA|Clase 150 /<br>AWWA|AS|AS|PN / ANSI /<br>AWWA / AS|PN / ANSI /<br>AWWA / AS|
|mm|pulga-<br>das|kg|libras|kg|libras|kg|libras|kg|libras|kg|libras|kg|libras|
|15|1⁄2|N/D|N/D|N/D|N/D|4|9|4|9|N/D|N/D|-|-|
|25|1|N/D|N/D|N/D|N/D|6|12|5|11|N/D|N/D|5|11|
|40|11⁄2|N/D|N/D|N/D|N/D|8|18|7|15|N/D|N/D|8|17|
|50|2|N/D|N/D|9|20|N/D|N/D|8|20|N/D|N/D|9|20|
|65|21⁄2|N/D|N/D|10.7|24|N/D|N/D|11|24|N/D|N/D|11|24|
|80|3|N/D|N/D|11.6|26|N/D|N/D|13|28|N/D|N/D|12|24|
|100|4|N/D|N/D|15.2|33|N/D|N/D|19|41|N/D|N/D|16|35|
|125|5|N/D|N/D|20.4|45|N/D|N/D|24|52|N/D|N/D|19|42|
|150|6|N/D|N/D|26|57|N/D|N/D|29|64|N/D|N/D|27|60|
|200|8|48|106|48|106|N/D|N/D|56|124|N/D|N/D|40|68|
|250|10|64|141|69|152|N/D|N/D|79|174|N/D|N/D|60|132|
|300|12|76|167|86|189|N/D|N/D|110|243|N/D|N/D|80|176|
|350|14|104|229|125|274|N/D|N/D|139|307|N/D|N/D|110|242|
|400|16|119|263|143|314|N/D|N/D|159|351|N/D|N/D|125|275|
|450|18|136|299|173|381|N/D|N/D|182|400|N/D|N/D|175|385|
|500|20|163|359|223|491|N/D|N/D|225|495|N/D|N/D|200|440|
|600|24|236|519|338|744|N/D|N/D|320|704|N/D|N/D|187|633|
|700|28|270|595|314|692|N/D|N/D|273|602|320|70|330|728|
|750|30|N/D|N/D|N/D|N/D|N/D|N/D|329|725|N/D|N/D|360|794|
|800|32|346|763|396|873|N/D|N/D|365|804|428|944|450|992|
|900|36|432|951|474|1043|N/D|N/D|495|1089|618|1362|53|1168|
|1000|40|513|1130|600|1321|N/D|N/D|583|1282|636|1399|66|1455|
|1050|42|N/D|N/D|N/D|N/D|N/D|N/D|687|1512|N/D|N/D|N/D|N/D|
|1100|44|N/D|N/D|N/D|N/D|N/D|N/D|763|1680|N/D|N/D|1140|2513|
|1200|48|643|1415|885|1948|N/D|N/D|861|1896|813|1789|1180|2601|
|1400|54|1592|3510|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|1600|3528|
|1500|60|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|2460|5423|
|1600|66|2110|4652|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|2525|5566|
|1800|72|2560|5644|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|2930|6460|
|2000|78|3640|8025|N/D|N/D|N/D|N/D|N/D|N/D|N/D|N/D|3665|8080|

SITRANS F M MAG 5100 W

50 Instrucciones de servicio, 11/2010, A5E03376529-01

### Anexo A

A.1 Dimensiones de las contrabridas (métricas)

Figura A-1 Dimensiones de las contrabridas

Tabla A- 1 Dimensiones de las contrabridas (métricas)

|Col1|Dimensiones (mm)|Col3|Col4|Col5|Unión con pernos|Col7|
|---|---|---|---|---|---|---|
|mm|D|PCD<br>T||B|Orificios|Pernos|
|PN10|PN10|PN10|PN10|PN10|PN10|PN10|
|200|340|295<br>24||22|8|M20|
|250|395|350<br>26||22|12|M20|
|300|445|400<br>26||22|12|M20|
|350|505|460<br>28||22|16|M20|
|400|565|515<br>32||26|16|M24|
|450|615|565<br>36||26|20|M24|
|500|670|620<br>38||26|20|M24|
|600|780|725<br>42||3|20|M27|
|700|895|840<br>30||30|24|M27|
|800|1015|950<br>32||33|24|M30|
|900|1115|1050<br>34||33|28|M30|
|1000|1230|1160<br>34||36|28|M33|
|1200|1455|1380<br>38||39|32|M36|
|PN16|PN16|PN16|PN16|PN16|PN16|PN16|
|50|165|125<br>19||18|4|M16|
|65|185|145<br>20||18|8|M16|
|80|200|160<br>20||18|8|M16|
|100|220|180<br>22||18|8|M16|
|125|250|210<br>22||18|8|M16|
|150|285|240<br>24||22|8|M20|
|200|340|295<br>26||22|12|M20|

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 51

Anexo

A.1 Dimensiones de las contrabridas (métricas)

|Col1|Dimensiones (mm)|Col3|Col4|Col5|Unión con pernos|Col7|
|---|---|---|---|---|---|---|
|mm|D|PCD|T|B|Orificios|Pernos|
|250|405|355|29|26|12|M24|
|300|460|410|32|26|12|M24|
|350|520|470|35|26|16|M24|
|400|580|525|38|30|16|M27|
|450|640|585|42|30|20|M27|
|500|715|650|46|33|20|M30|
|600|840|770|52|36|20|M33|
|700|910|840|36|36|24|M33|
|800|1025|950|38|39|24|M36|
|900|1125|1050|40|39|28|M36|
|1000|1255|1170|42|42|28|M39|
|1200|1485|1390|48|48|32|M45|
|PN40|PN40|PN40|PN40|PN40|PN40|PN40|
|15|95|65|14|14|4|M12|
|25|115|85|16|14|4|M16|
|40|150|110|18|18|4|M16|
|150 lb|150 lb|150 lb|150 lb|150 lb|150 lb|150 lb|
|15|89|60|12|16|4|M12|
|25|108|79|16|16|4|M16|
|40|127|98|18|16|4|M16|
|50|152|121|19|19|4|M16|
|65|178|140|22|19|4|M16|
|80|190|152|24|19|4|M16|
|100|229|191|24|19|8|M16|
|125|254|216|24|22|8|M20|
|150|279|241|25|22|8|M20|
|200|343|298|29|22|8|M20|
|250|406|362|30|25|12|M24|
|300|483|432|32|25|12|M24|
|350|533|476|35|28|12|M27|
|400|597|540|36.5|28|16|M27|
|450|635|578|40|32|16|M30|
|500|699|635|43|32|20|M30|
|600|813|749|48|35|20|M33|
|AWWA|AWWA|AWWA|AWWA|AWWA|AWWA|AWWA|
|700|927|864|33|35|28|M33|
|750|984|914|35|35|28|M33|
|800|1060|978|38|41|28|M39|
|900|1168|1068|41|41|32|M39|
|1000|1289|1200|41|41|36|M39|

SITRANS F M MAG 5100 W

52 Instrucciones de servicio, 11/2010, A5E03376529-01

Anexo

A.2 Configuración de fábrica

|Col1|Dimensiones (mm)|Col3|Col4|Col5|Unión con pernos|Col7|
|---|---|---|---|---|---|---|
|mm|D|PCD|T|B|Orificios|Pernos|
|1050|1346|1257|44|41|36|M39|
|1200|1511|1422|48|41|44|M39|

A.2 Configuración de fábrica

Configuración de fábrica dependiente de las dimensiones

Tabla A- 2 Versión de 50 Hz

|DN|Col2|Col3|Qmax|Col5|Col6|Col7|Unidad|Volumen/<br>impulso|Unidad<br>de<br>impul-<br>so|Unidad<br>del<br>totaliza-<br>dor|
|---|---|---|---|---|---|---|---|---|---|---|
|DN|DN||Referencia 7ME6520|Referencia 7ME6520|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|
|mm|Pulga<br>das|Config.<br>fábrica|Mín.|Máx.|Mín.|Máx.|||||
|15|1⁄2|2000|159|6361|-|-|l/h|1|l|l|
|25|1|5000|441|17671|441|17671|l/h|10|l|l|
|40|11⁄2|12|1.1|45|1.1|45|m3/h|10|l|l|
|50|2|20|1.7|63|1.7|70|m3/h|10|l|l|
|65|21⁄2|30|2.9|100|2.9|119|m3/h|100|l|l|
|80|3|50|4.0|160|4.5|180|m3/h|100|l|l|
|100|4|120|6.2|250|7|282|m3/h|100|l|l|
|125|5|180|10.0|400|11|441|m3/h|100|l|m3|
|150|6|250|15.7|629|15.9|636|m3/h|100|l|m3|
|200|8|400|24.9|997|28.2|1130|m3/h|1|m3|m3|
|250|10|700|40.0|1600|44.1|1767|m3/h|1|m3|m3|
|300|12|1000|62.5|2500|63.6|2544|m3/h|1|m3|m3|
|350|14|1200|86.5|3463|86.5|3463|m3/h|1|m3|m3|
|400|16|1800|113|4523|113|4523|m3/h|1|m3|m3|
|450|18|2000|143.1|5725|143.1|5725|m3/h|1|m3|m3|
|500|20|3000|176.7|7068|176.7|7068|m3/h|1|m3|m3|
|600|24|4000|254.4|10178|254.4|10178|m3/h|10|m3|m3|
|700|28|5000|346.3|13854|346.3|13854|m3/h|10|m3|m3|
|750|30|6000|397.6|15904|397.6|15904|m3/h|10|m3|m3|
|800|32|7000|452.3|18095|452.3|18095|m3/h|10|m3|m3|
|900|36|9000|572.5|22902|572.5|22902|m3/h|10|m3|m3|
|1000|40|12000|706.8|28274|706.8|28274|m3/h|10|m3|m3|
|1050|42|12000|706.8|28274|706.8|28274|m3/h|10|m3|m3|
|1100|44|14000|855.2|34211|855.2|34211|m3/h|10|m3|m3|

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 53

Anexo

A.2 Configuración de fábrica

|DN|Col2|Col3|Qmax|Col5|Col6|Col7|Unidad|Volumen/<br>impulso|Unidad<br>de<br>impul-<br>so|Unidad<br>del<br>totaliza-<br>dor|
|---|---|---|---|---|---|---|---|---|---|---|
|DN|DN||Referencia 7ME6520|Referencia 7ME6520|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|
|1200|48|15000|1017.8|40715|1017.8|40715|m3/h|10|m3|m3|
|1400|54|25000|-|-|1385.4|55417|m3/h|10|m3|m3|
|1500|60|30000|-|-|1590.4|63617|m3/h|10|m3|m3|
|1600|66|35000|-|-|1809.5|72382|m3/h|10|m3|m3|
|1800|72|40000|-|-|2290.2|91608|m3/h|10|m3|m3|
|2000|78|45000|-|-|2827.4|113097|m3/h|10|m3|m3|

Tabla A- 3 Versión de 60 Hz

|DN|Col2|Col3|Qmax|Col5|Col6|Col7|Unidad|Volumen/<br>impulso|Unidad<br>de<br>impulso|Unidad<br>del<br>totaliza-<br>dor|
|---|---|---|---|---|---|---|---|---|---|---|
|DN|DN||Referencia 7ME6520|Referencia 7ME6520|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|
|mm|Pulga<br>das|Config.<br>fábrica|Mín.|Máx.|Mín.|Máx.|||||
|15|1⁄2|9|0.7|28|-|-|US GPM|1|US G|US G|
|25|1|22|1.9|77.8|1.9|77.8|US GPM|1|US G|US G|
|40|11⁄2|52|4.9|199.1|4.9|199.1|US GPM|1|US G|US G|
|50|2|88|6.9|277.2|7.7|311.2|US GPM|1|US G|US G|
|65|21⁄2|132|11.0|440.2|13.1|525.9|US GPM|1|US G|US G|
|80|3|220|17.6|705.1|19.9|796.7|US GPM|1|US G|US MG|
|100|4|528|27.5|1101|31.1|1244.8|US GPM|1|US G|US MG|
|125|5|793|44.0|1762.2|48.6|1945.1|US GPM|1|US G|US MG|
|150|6|1101|69.3|2772.9|70|2800.9|US GPM|1|US G|US MG|
|200|8|1761|109.7|4391.9|124.4|4979.5|US GPM|1|US G|US MG|
|250|10|3082|176.1|7045.2|194.5|7780.5|US GPM|1|US G|US MG|
|300|12|4402|275.1|11007.8|280|11203.9|US GPM|1|US G|US MG|
|350|14|5283|381.2|15249.7|381.2|15249.7|US GPM|1|US G|US MG|
|400|16|7925|497.9|19918.1|497.9|19918.1|US GPM|1|US G|US MG|
|450|18|8806|630.2|25208.8|630.2|25208.8|US GPM|1|US G|US MG|
|500|20|13209|778|31122|778|31122|US GPM|1|US G|US MG|
|600|24|17611|1120.3|44815.7|1120.3|44815.7|US GPM|10|US G|US MG|
|700|28|19812|1524.9|60999.1|1524.9|60999.1|US GPM|10|US G|US MG|
|750|30|22014|1750.6|70024.5|1750.6|70024.5|US GPM|10|US G|US MG|
|800|32|30820|1991.8|79672.4|1991.8|79672.4|US GPM|10|US G|US MG|
|900|36|39626|2522.8|100835.3|2522.8|100835.3|US GPM|10|US G|US MG|
|1000|40|52834|3112.2|124488.1|3112.2|124488.1|US GPM|10|US G|US MG|
|1050|42|52834|3431.2|137248.1|3431.2|137248.1|US GPM|10|US G|US MG|
|1100|44|61640|3765.7|150630.6|3765.7|150630.6|US GPM|10|US G|US MG|
|1200|48|66043|4481|179262.9|4481|179262.9|US GPM|10|US G|US MG|

SITRANS F M MAG 5100 W

54 Instrucciones de servicio, 11/2010, A5E03376529-01

Anexo

A.3 Resistencia de la bobina

|DN|Col2|Col3|Qmax|Col5|Col6|Col7|Unidad|Volumen/<br>impulso|Unidad<br>de<br>impulso|Unidad<br>del<br>totaliza-<br>dor|
|---|---|---|---|---|---|---|---|---|---|---|
|DN|DN||Referencia 7ME6520|Referencia 7ME6520|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|Referencia 7ME6580|
|1400|54|110072|-|-|6099.9|243993.7|US GPM|1000|US G|US MG|
|1500|60|132086|-|-|7002.4|280098.3|US GPM|1000|US G|US MG|
|1600|66|154100|-|-|7967.2|318689.6|US GPM|1000|US G|US MG|
|1800|72|176115|-|-|10083.5|403341.5|US GPM|1000|US G|US MG|
|2000|78|198129|-|-|12448.8|497952.5|US GPM|1000|US G|US MG|

A.3 Resistencia de la bobina

Tabla A- 4 Resistencia de la bobina

|Col1|Col2|MAG 1100, MAG 1100F|Col4|MAG 3100, MAG 3100P,<br>MAG 5100 W<br>(Referencia 7ME6580)|Col6|MAG 5100 W<br>(Referencia 7ME6520)|Col8|
|---|---|---|---|---|---|---|---|
|DN|Pulgadas|Resistencia|Tolerancia|Resistencia|Tolerancia|Resistencia|Tolerancia|
|2|1/12|104 Ω|+/− 5|104||||
|3|1/8|104 Ω|+/− 5|104||||
|6|1/4|99 Ω|+/− 17|104||||
|10|3/8|99 Ω|+/− 17|104||||
|151)|1/2|91 Ω|+/− 9|104||||
|25|1|91 Ω|+/− 17|104|+/− 2|104|+/− 10|
|40|11/2|91 Ω|+/− 9|92|+/− 2|92|+/− 10|
|50|2|91 Ω|+/− 9|92|+/− 2|119.4|+/− 10|
|65|21/2|99 Ω|+/− 17|100|+/− 2|127|+/− 10|
|80|3|91 Ω|+/− 17|94|+/− 2|126|+/− 10|
|100|4|91 Ω|+/− 9|92|+/− 2|125|+/− 10|
|125|5|92|+/− 2|126|+/− 10|||
|150|6|94|+/− 2|116|+/− 10|||
|200|8|90|+/− 2|109|+/− 10|||
|250|10|92|+/− 2|104|+/− 10|||
|300|12|100|+/− 2|108|+/− 10|||
|350|14|112|+/− 2|100|+/− 6|||
|400|16|100|+/− 4|100|+/− 6|||
|450|18|108|+/− 4|100|+/− 6|||
|500|20|122|+/− 4|100|+/− 6|||
|600|24|115|+/− 4|98|+/− 6|||
|700|28|128|+/− 4|98|+/− 6|||
|750|30|133||||||
|800|32|128|+/− 4|98|+/− 6|||

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 55

Anexo

A.3 Resistencia de la bobina

|Col1|Col2|MAG 1100, MAG 1100F|Col4|MAG 3100, MAG 3100P,<br>MAG 5100 W<br>(Referencia 7ME6580)|Col6|MAG 5100 W<br>(Referencia 7ME6520)|Col8|
|---|---|---|---|---|---|---|---|
|900|36|131|+/− 4|98|+/− 6|||
|1000|40|131|+/− 4|88|+/− 6|||
|1100|44|126||||||
|1200|48|130|+/− 4|88|+/− 6|||
|1400|54|130||||||
|1500|60|124||||||
|1600|66|133||||||
|1800|72|133||||||
|2000|78|147||||||

1) En el MAG 1100 DN 15 fabricado a partir de mayo de 1999, la resistencia de la bobina debe ser de 86 ohmios, +8/−4

ohmios.

Repuestos

|Descripción|Col2|
|---|---|
|Prensaestopas de cable, 2 unids.<br>M20<br> <br> <br> <br> <br>1⁄2" NPT|<br> <br> <br> <br>|
|Tornillos de sellado para el sensor/transmisor, 2 unids.|<br> <br>|

SITRANS F M MAG 5100 W

56 Instrucciones de servicio, 11/2010, A5E03376529-01

Anexo

A.4 Pedido

|Descripción|Col2|
|---|---|
|Caja de terminales, en poliamida, incluida tapa<br>M20<br>1⁄2" NPT||
|Tapa de la caja de terminales, en poliamida|<br> <br>|
|Caja de terminales, en acero inoxidable, incluida tapa<br>M20<br>1⁄2" NPT|<br> <br>|
|Kit de revestimiento para la caja de terminales de los<br>sensores MAG para I<br>P68/NEMA 6P (no para EX)|<br> <br> <br> <br> <br>|

A.4 Pedido

Para asegurar que los datos sobre pedidos que usted está usando no están obsoletos, los
más recientes datos sobre pedidos siempre están disponibles en la Internet: Catálogos de
[process instrumentation (http://www.siemens.com/processinstrumentation/catalogs)](http://www.siemens.com/processinstrumentation/catalogs)

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 57

Anexo

A.4 Pedido

SITRANS F M MAG 5100 W

58 Instrucciones de servicio, 11/2010, A5E03376529-01

Glosario

ASIC

DBT

EMC

HART

IP

El Circuito integrado específico de la aplicación (Application-Specific Integrated Circuit) es
un circuito integrado (CI) personalizado para un uso concreto, en lugar de para un uso
general.

La Directiva de Baja Tensión es una directiva de la UE destinada a asegurar que el equipo
eléctrico proporciona un nivel elevado de protección para ciudadanos europeos dentro de
determinados valores límite de tensión. La directiva cubre el equipo eléctrico con una
tensión entre 50 y 1000 V para corriente alterna y entre 75 y 1500 V para corriente continua.
Los rangos de tensión se refieren a la tensión de la entrada o salida eléctrica, no a las
tensiones que pueden aparecer dentro del equipo.

La Compatibilidad electromagnética (EMC) es la rama de las ciencias eléctricas que estudia
la generación, propagación y recepción no intencionada de energía electromagnética en
referencia a los efectos no deseados (Interferencia electromagnética o EMI) que dicha
energía pueda provocar. El objetivo de la EMC es el funcionamiento correcto, en el mismo
entorno electromagnético, de diferentes equipos que utilicen los fenómenos
electromagnéticos y evitar cualquier efecto de interferencia.

La comunicación HART es un protocolo de comunicación bidireccional de carácter industrial
que se utiliza para establecer una comunicación entre instrumentos de campo inteligentes y
sistemas anfitriones (host). HART es el estándar mundial para instrumentación de procesos
y la mayoría de los dispositivos de este tipo instalados en fábricas de todo el mundo es
compatible con el sistema HART. La tecnología HART es fácil de utilizar y muy fiable

Un número IP (Protección de entrada) se utiliza para especificar la protección
medioambiental de receptáculos para equipos eléctricos. Estas clasificaciones se
determinan mediante pruebas específicas. El número IP se compone de dos números, el
primero se refiere a la protección contra objetos sólidos y el segundo contra líquidos. Cuanto
mayor es el número, mejor será la protección. Por ejemplo, en IP67, el primer número (6)
significa que el dispositivo está totalmente protegido contra el polvo, y el segundo número
(7) significa que está protegido contra el efecto de la inmersión entre 15 cm y 1 m

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 59

Glosario

MID

MODBUS

NAMUR

PED

PROFIBUS

SENSORPROM

La directiva de instrumentos de medida (2004/22/CE) es una directiva de la Unión Europea
encaminada a crear un mercado común para los instrumentos de medida en todos los
países de la UE. Los contadores que disponen de una homologación MID pueden utilizarse
en todos los países de la UE.

MODBUS es un protocolo de comunicación en serie previsto para su uso con controladores
lógicos programables (PLC). MODBUS permite la comunicación entre muchos dispositivos
conectados a la misma red, por ejemplo, un sistema que mide la temperatura y la humedad,
y que comunica los resultados a un ordenador. MODBUS se utiliza a menudo para conectar
un ordenador de supervisión con una unidad de terminal remoto (RTU) en sistemas de
control y de adquisición de datos.

Normenarbeitsgemeinschaft für Meß- und Regeltechnik in der Chemischen Industrie
(NAMUR). NAMUR es un grupo que representa los intereses de la industria química, que
crea los estándares para instrumentos y dispositivos eléctricos utilizados en plantas
industriales.

La Directiva sobre equipos de presión (97/23/CE) es el marco legislativo en Europa para los
equipos sometidos a riesgos de presión. Se adoptó por el Parlamento Europeo y el Consejo
Europeo en mayo de 1997 y ha sido obligatoria en la Unión Europea desde mayo de 2002.

PROFIBUS (Process Field Bus - Bus de campo de procesos) es un sistema de bus abierto,
independiente del proveedor, basado en la norma alemana DIN 19 245. Se trata de un
estándar para la comunicación de buses de campo en la tecnología de automatización y no
debe confundirse con el estándar PROFINET para Ethernet industrial. PROFIBUS-PA
(Automatización de procesos) es una de las tres variantes de PROFIBUS compatibles con el
resto. PROFIBUS-DP (Periferia descentralizada)

Todos los datos/configuraciones relacionados con los sensores guardados en una EPROM.
La tecnología SENSORPROM configura de forma automática el transmisor durante la
puesta en marcha de la unidad proporcionando datos de calibración, tamaño de los tubos,
tipo de sensor y ajustes de salida. El SENSORPROM almacena de forma automática
valores o configuraciones modificados por los usuarios y reprograma automáticamente
cualquier transmisor nuevo sin pérdida de precisión.

SITRANS F M MAG 5100 W

60 Instrucciones de servicio, 11/2010, A5E03376529-01

Tasa de bajada

USM

Glosario

La "tasa de bajada" es un término de medición de caudal que indica el intervalo de un
medidor de caudal específico, o tipo de medidor, que es capaz de medir con una precisión
aceptable. También se conoce como capacidad de alcance. Si un flujo de gas que debe
medirse se espera que varía entre 100 000 m3 por día y 1 000 000 m3 por día, la aplicación
tiene una tasa de bajada de 10:1. Por lo tanto, el medidor requiere una tasa de bajada de al
menos 10:1.

USM II es una plataforma de comunicación. El concepto USM II de Siemens permite el
acoplamiento de módulos de buses añadidos sin pérdida de funcionalidad:

1. Todos los módulos pueden acoplarse como sistemas "plug & play" reales

2. El módulo y el transmisor se configuran de forma automática a través del
SENSORPROM

SITRANS F M MAG 5100 W

Instrucciones de servicio, 11/2010, A5E03376529-01 61

Glosario

SITRANS F M MAG 5100 W

62 Instrucciones de servicio, 11/2010, A5E03376529-01

Índice alfabético

A

Aislamiento del cable, 24
Aplicaciones, 11
Área con peligro de explosión

Homologaciones, 10
Asistencia, 31

B

Burbujas de aire / gas, 18

C

Cableado, (Consulte Conexión eléctrica)
Compatibilidad de materiales, 7
Componentes del sistema, 11
Comprobación de la resistencia de la bobina, 33
Comprobación de la resistencia de los electrodos, 34
Comprobación del aislamiento de la bobina, 33
Comprobación del sensor, 33
Condiciones de entrada / salida, 16
Conexión eléctrica

Especificaciones del cable, 23
Instalaciones remotas, 24
Instrucciones de seguridad, 23
Conexión equipotencial, 22
Conformidad, 7

D

Descontaminación, 31
Detección de tubería vacía, 19
Dimensiones, 48
Dimensiones de las contrabridas, 51
Directiva de equipos a presión, 8

E

Elementos suministrados, 5
Enterramiento directo, 28
Especificaciones del cable, 23, 40

SITRANS F M MAG 5100 W

F

FAQ

Fluctuación de los valores de proceso, 35

H

Historia de la documentación, 5

I

Indicaciones de seguridad, 7
Instalación

dentro de un tubo en "U", 16
Instrucciones de seguridad, 15
Interior/exterior, 15
Montaje del sensor, 19
Remota, 24
Tubos con una salida libre, 16
Tubos de grandes dimensiones, 17
Ubicación en el sistema, 16
Instrucciones de seguridad

Conexión eléctrica, 23
Instalación, 15
Internet

Asistencia, 31
Flowdocumentation, 6
Persona para contacto, 6, 31
Introducción, 5

L

Leyes y directivas, 7
Línea directa, 30
Línea directa de Asistencia al Cliente, 30
Líquido del proceso

Conductividad, 43
Líquidos abrasivos, 18

M

Mantenimiento, 29
Módulos adicionales, (Consulte el módulo de
comunicación)
Módulos de comunicación, 11

Instrucciones de servicio, 11/2010, A5E03376529-01 63

Índice alfabético

Montaje, (Consulte Instalación)

O

Orientación del sensor, 18

P

Persona para contacto, 6
Peso, 50
Presión

Instrucciones de seguridad, 15
Principio de funcionamiento, 13
Principio de medición, 13
Procedimientos de devolución, 31
Protección catódica, 22

R

Recalibración, 29
Red de alimentación, 23
Reparación, 30
Revestimiento, 26

S

Seguridad

Estándares de seguridad para los instrumentos, 7
Servicio, 30, 31

T

Terminal del conductor de protección, 24
Tierra de protección, 24
Transportes, 29
Tubos horizontales

Instalación en, 19
Tubos verticales

Instalación en, 18

V

Valores de par, 20
Vibraciones, 20

SITRANS F M MAG 5100 W

64 Instrucciones de servicio, 11/2010, A5E03376529-01

**Para más informacion**

**www.siemens.com/flow**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-: 1 MAG 5100 W (7ME6580 sólo DN15 ... 600 (1⁄2" ... 24"))**

| mm de brida | PN 10 | PN 16 | PN 40 | 150 lb | 300 lb |
| --- | --- | --- | --- | --- | --- |
| 15 | N/A | N/A | SEP | SEP | N/A |
| 25 | N/A | N/A | SEP | SEP | N/A |
| 40 | N/A | N/A | SEP | SEP | N/A |
| 50 | N/A | SEP | N/A | SEP | N/A |
| 65 | N/A | SEP | N/A | SEP | N/A |
| 80 | N/A | SEP | N/A | SEP | N/A |
| 100 | SEP | SEP | N/A | SEP | N/A |
| 125 | N/A | SEP | N/A | DEP | N/A |
| 150 | N/A | DEP | N/A | DEP | N/A |
| 200 | SEP | DEP | N/A | DEP | N/A |
| 250 | DBT | DEP | N/A | DEP | N/A |
| 300 | DBT | DEP | N/A | DEP | N/A |
| 350 | DBT | DEP | N/A | DEP | N/A |
| 400 | DBT | DEP | N/A | DEP | N/A |
| 450 | DBT | DEP | N/A | DEP | N/A |
| 500 | DBT | DEP | N/A | DEP | N/A |
| 600 | DBT | DEP | N/A | DEP | N/A |
| 700 | DBT | DEP* | N/A | N/A | DEP |
| 750 | N/A | N/A | N/A | N/A | DEP |
| 800 | DBT | DEP* | N/A | N/A | DEP |
| 900 | DBT | DEP* | N/A | N/A | DEP |
| 1000 | DBT | DEP* | N/A | N/A | DEP |

**Tabla 4-: 1 Pares máximos permitidos**

| DN | Col2 | PN 10 | Col4 | PN 16 | Col6 | PN 40 | Col8 | Clase 150 | Col10 | AWWA | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mm | Pulga<br>das | Nm | F/lbs | Nm | F/lbs | Nm | F/lbs | Nm | F/lbs | Nm | F/lbs |
| 15 | 1⁄2 | N/A | N/A | N/A | N/A | 10 | 7 | 6 | 5 | N/A | N/A |
| 25 | 1" | N/A | N/A | N/A | N/A | 10 | 7 | 7 | 5 | N/A | N/A |
| 40 | 11⁄2" | N/A | N/A | N/A | N/A | 16 | 12 | 9 | 7 | N/A | N/A |
| 50 | 2" | N/A | N/A | N/A | N/A | N/A | N/A | 25 | 18 | N/A | N/A |
| 65 | 21⁄2" | N/A | N/A | 25/25 | 18/18 | N/A | N/A | 25 | 18 | N/A | N/A |
| 80 | 3" | N/A | N/A | 25/25 | 18/18 | N/A | N/A | 34 | 25 | N/A | N/A |
| 100 | 4" | N/A | N/A | 25/25 | 18/18 | N/A | N/A | 26 | 19 | N/A | N/A |
| 125 | 5" | N/A | N/A | 29/32 | 21/24 | N/A | N/A | 42 | 31 | N/A | N/A |
| 150 | 6" | N/A | N/A | 50/50 | 37/37 | N/A | N/A | 57 | 42 | N/A | N/A |
| 200 | 8" | 50/50 | 37/37 | 50/52 | 37/38 | N/A | N/A | 88 | 65 | N/A | N/A |
| 250 | 10" | 50/50 | 37/37 | 82/88 | 61/65 | N/A | N/A | 99 | 73 | N/A | N/A |
| 300 | 12" | 57/62 | 42/46 | 111/117 | 82/86 | N/A | N/A | 132 | 97 | N/A | N/A |
| 350 | 14" | 60/60 | 44/44 | 120/120 | 89/89 | N/A | N/A | 225 | 166 | N/A | N/A |
| 400 | 16" | 88/88 | 65/65 | 170/170 | 125/125 | N/A | N/A | 210 | 155 | N/A | N/A |
| 450 | 18" | 92/92 | 68/68 | 170/170 | 125/125 | N/A | N/A | 220 | 162 | N/A | N/A |
| 500 | 20" | 103/103 | 76/76 | 230/230 | 170/170 | N/A | N/A | 200 | 148 | N/A | N/A |
| 600 | 24" | 161/161 | 119/119 | 350/350 | 258/258 | N/A | N/A | 280 | 207 | N/A | N/A |
| 700 | 28" | 200/200 | 148/148 | 304/304 | 224/224 | N/A | N/A | N/A | N/A | 200 | 148 |
| 750 | 30" | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 240 | 177 |
| 800 | 32" | 274/274 | 202/202 | 386/380 | 285/285 | N/A | N/A | N/A | N/A | 260 | 192 |
| 900 | 36" | 288/288 | 213/213 | 408/408 | 301/301 | N/A | N/A | N/A | N/A | 240 | 177 |
| 1000 | 40" | 382/382 | 282/282 | 546/546 | 403/403 | N/A | N/A | N/A | N/A | 280 | 207 |
| 1050 | 42" | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 280 | 207 |
| 1100 | 44" | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 290 | 214 |
| 1200 | 48" | 395/395 | 292/292 | 731/731 | 539/538 | N/A | N/A | N/A | N/A | 310 | 229 |
| 1400 | 54" | -/503 | -/317 | -/736 | -/543 | N/A | N/A | N/A | N/A | 528 | 389 |
| 1600 | 66" | -/684 | -/505 | -/913 | -/674 | N/A | N/A | N/A | N/A | 698 | 515 |
| 1800 | 72" | -/771 | -/569 | -/937 | -/692 | N/A | N/A | N/A | N/A | 700 | 516 |
| 2000 | 78" | -/867 | -/640 | -/1128 | -/832 | N/A | N/A | N/A | N/A | 890 | 656 |

**Tabla 8-: 12 Peso**

| Tamaño<br>nominal | Col2 | Referencia<br>7ME6520 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Referencia<br>7ME6580 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tamaño<br>nominal | Tamaño<br>nominal | PN 10 | PN 10 | PN 16 | PN 16 | PN 40 | PN 40 | Clase 150 /<br>AWWA | Clase 150 /<br>AWWA | AS | AS | PN / ANSI /<br>AWWA / AS | PN / ANSI /<br>AWWA / AS |
| mm | pulga-<br>das | kg | libras | kg | libras | kg | libras | kg | libras | kg | libras | kg | libras |
| 15 | 1⁄2 | N/D | N/D | N/D | N/D | 4 | 9 | 4 | 9 | N/D | N/D | - | - |
| 25 | 1 | N/D | N/D | N/D | N/D | 6 | 12 | 5 | 11 | N/D | N/D | 5 | 11 |
| 40 | 11⁄2 | N/D | N/D | N/D | N/D | 8 | 18 | 7 | 15 | N/D | N/D | 8 | 17 |
| 50 | 2 | N/D | N/D | 9 | 20 | N/D | N/D | 8 | 20 | N/D | N/D | 9 | 20 |
| 65 | 21⁄2 | N/D | N/D | 10.7 | 24 | N/D | N/D | 11 | 24 | N/D | N/D | 11 | 24 |
| 80 | 3 | N/D | N/D | 11.6 | 26 | N/D | N/D | 13 | 28 | N/D | N/D | 12 | 24 |
| 100 | 4 | N/D | N/D | 15.2 | 33 | N/D | N/D | 19 | 41 | N/D | N/D | 16 | 35 |
| 125 | 5 | N/D | N/D | 20.4 | 45 | N/D | N/D | 24 | 52 | N/D | N/D | 19 | 42 |
| 150 | 6 | N/D | N/D | 26 | 57 | N/D | N/D | 29 | 64 | N/D | N/D | 27 | 60 |
| 200 | 8 | 48 | 106 | 48 | 106 | N/D | N/D | 56 | 124 | N/D | N/D | 40 | 68 |
| 250 | 10 | 64 | 141 | 69 | 152 | N/D | N/D | 79 | 174 | N/D | N/D | 60 | 132 |
| 300 | 12 | 76 | 167 | 86 | 189 | N/D | N/D | 110 | 243 | N/D | N/D | 80 | 176 |
| 350 | 14 | 104 | 229 | 125 | 274 | N/D | N/D | 139 | 307 | N/D | N/D | 110 | 242 |
| 400 | 16 | 119 | 263 | 143 | 314 | N/D | N/D | 159 | 351 | N/D | N/D | 125 | 275 |
| 450 | 18 | 136 | 299 | 173 | 381 | N/D | N/D | 182 | 400 | N/D | N/D | 175 | 385 |
| 500 | 20 | 163 | 359 | 223 | 491 | N/D | N/D | 225 | 495 | N/D | N/D | 200 | 440 |
| 600 | 24 | 236 | 519 | 338 | 744 | N/D | N/D | 320 | 704 | N/D | N/D | 187 | 633 |
| 700 | 28 | 270 | 595 | 314 | 692 | N/D | N/D | 273 | 602 | 320 | 70 | 330 | 728 |
| 750 | 30 | N/D | N/D | N/D | N/D | N/D | N/D | 329 | 725 | N/D | N/D | 360 | 794 |
| 800 | 32 | 346 | 763 | 396 | 873 | N/D | N/D | 365 | 804 | 428 | 944 | 450 | 992 |
| 900 | 36 | 432 | 951 | 474 | 1043 | N/D | N/D | 495 | 1089 | 618 | 1362 | 53 | 1168 |
| 1000 | 40 | 513 | 1130 | 600 | 1321 | N/D | N/D | 583 | 1282 | 636 | 1399 | 66 | 1455 |
| 1050 | 42 | N/D | N/D | N/D | N/D | N/D | N/D | 687 | 1512 | N/D | N/D | N/D | N/D |
| 1100 | 44 | N/D | N/D | N/D | N/D | N/D | N/D | 763 | 1680 | N/D | N/D | 1140 | 2513 |
| 1200 | 48 | 643 | 1415 | 885 | 1948 | N/D | N/D | 861 | 1896 | 813 | 1789 | 1180 | 2601 |
| 1400 | 54 | 1592 | 3510 | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | 1600 | 3528 |
| 1500 | 60 | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | 2460 | 5423 |
| 1600 | 66 | 2110 | 4652 | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | 2525 | 5566 |
| 1800 | 72 | 2560 | 5644 | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | 2930 | 6460 |
| 2000 | 78 | 3640 | 8025 | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | 3665 | 8080 |
