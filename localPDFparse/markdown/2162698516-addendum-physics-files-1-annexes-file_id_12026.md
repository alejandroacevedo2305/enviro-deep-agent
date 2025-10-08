---
title: Sin título
author: Administrator
date: D:20250113151919-06'00'
language: es
type: manual
pages: 29
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 08 Memoria Técnica Baterias BESS
-->

# Anexo 08 Memoria Técnica Baterias BESS

## Tabla de contenidos

**1 Visión general** **...............................................................................................................................................** **2**

1.1 Escenarios de aplicación ................................................................................................................... 2

**2 Diseño del sistema** **......................................................................................................................................** **3**

2.1 Configuración del sistema ................................................................................................................. 3

2.2 Lista de equipos del sistema (alcance de suministro) .................................................................. 3

**3 Sistema PCS** **.................................................................................................................................................** **5**

3.1 Diagrama de circuito .......................................................................................................................... 5

3.2 Especificaciones técnicas ................................................................................................................. 5

**4 Sistema de batería** **.......................................................................................................................................** **8**

4.1 Celda de batería ................................................................................................................................. 8

4.2 Módulo de batería .............................................................................................................................. 8

4.3 Bastidor de baterías ........................................................................................................................... 9

4.4 Unidad de contenedor de batería .................................................................................................. 10

**5 Sistema de comunicación** **.......................................................................................................................** **11**

5.1 Introducción ....................................................................................................................................... 11

5.2 Funcionalidad BMS .......................................................................................................................... 11

5.3 Funcionalidad de CSU ..................................................................................................................... 13

**6 Introducción al sistema y equipos auxiliares** **....................................................................................** **15**

6.1 Especificación del contenedor ........................................................................................................ 15

6.2 Sistema de refrigeración líquida + refrigeración por aire ........................................................... 16

6.3 Sistema de extinción de incendios ................................................................................................ 16

6.3.1 Sistema de extinción de incendios por medios gaseosos .............................................. 17

6.3.2 Sistema de extinción de incendios de agua ...................................................................... 17

**7 Dibujo** **...........................................................................................................................................................** **18**

7.1 Dibujo del contenedor de la batería ............................................................................................... 18

**8 Curvas de degradación** **............................................................................................................................** **19**

1

## 1 Visión general

El sistema de almacenamiento de energía de batería a gran escala incluye el sistema de batería y el

sistema PCS. El sistema de baterías consta de un subsistema de control y embalaje de baterías, un

subsistema de distribución de energía, un subsistema de refrigeración y un subsistema de extinción de

incendios. El sistema PCS incluye PCS de cadena, transformador de MT, RMU, transformador auxiliar,

etc.

### 1.1 Escenarios de aplicación

Desde la perspectiva de toda la red eléctrica, los escenarios de aplicación de BESS se pueden dividir en

tres partes principales: lado de la generación de energía, lado de la transmisión y distribución y lado del

usuario final. Para el lado de la generación de energía, incluida la regulación de picos de potencia, la

operación dinámica auxiliar, la modulación de frecuencia del sistema y la conexión a la red de energía

renovable. Por el lado de la transmisión y la distribución, se utiliza principalmente para aliviar la congestión

y el aplazamiento de la red y para mejorar la calidad de la red. El almacenamiento de energía del lado del

usuario final se utiliza principalmente para el autoconsumo, el arbitraje de propagación pico-valle, la

gestión de la capacidad y la electricidad y para mejorar la fiabilidad del suministro de energía.

Fig.1-1: Descripción general de la aplicación BESS de alta relevancia

2

## 2 Diseño del sistema
### 2.1 Configuración del sistema

La solución propuesta cuenta con 6 unidades de estación de MT de 3,44MW con PCS y 24 unidades de

contenedor de batería de 3,44MWh con una potencia total de 20,64 MW/82,56 MWh para el inicio de la

vida útil. Cada contenedor de baterías tiene baterías LFP 384S10P con una capacidad de 3440 kWh,

sistema de refrigeración líquida + refrigeración por aire, sistema de extinción de incendios y otros

dispositivos auxiliares en su interior. El sistema PCS consta de 16 juegos de PCS de cadena inteligente

EBI 215K, transformador de MT de 3440 kVA y RMU.

La configuración detallada del sistema se muestra en la siguiente imagen,

Fig.2-1: Configuración del sistema (como referencia)
### 2.2 Lista de equipos del sistema (alcance de suministro)

Tabla 2-1: Lista de equipos BESS de X20,64 MW/82,56 MWh _CATL_0,25C

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La configuración detallada del sistema se muestra en la siguiente imagen, Fig.2-1: Configuración del sistema (como referencia) ### 2.2 Lista de equipos del sistema (alcance de suministro) -->

**Tabla 2-1: Lista de equipos BESS de X20,64 MW/82,56 MWh _CATL_0,25C**

| No. | Artículo | Especificació<br>n | Qty | Uni<br>dad | Coment<br>ario |
| --- | --- | --- | --- | --- | --- |
| **1 ** | **Unidad de**<br>**batería** |  | **24** | **Pc** | **Cada sistema consta de 1.1 ~ 1.4.** |
| 1.1 | LFP -Batería | 3440kWh | 1 | Pc | - Baterías 384S10P 3.2V 280Ah CATL LFP<br>- BMS<br>- Cables para la conexión del módulo.<br>- La descarga y la carga deben ser menores o<br>iguales a 0,25 °C. |
| 1.2 | SG de CC |  | 10 | Pc | - Voltaje nominal de CC : 1500V<br>- Seccionador + fusible<br>- BCU |
| 1.3 | Caja de<br>conexiones de<br>CC |  | 1 | Pc | - Voltaje nominal de CC : 1500V<br>- Seccionador + fusible |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- 3 4 -->
<!-- FIN TABLA 2-1 -->


|No.|Artículo|Especificació<br>n|Qty|Uni<br>dad|Coment<br>ario|
|---|---|---|---|---|---|
|**1 **|**Unidad de**<br>**batería**||**24**|**Pc**|**Cada sistema consta de 1.1 ~ 1.4.**|
|1.1|LFP -Batería|3440kWh|1|Pc|- Baterías 384S10P 3.2V 280Ah CATL LFP<br>- BMS<br>- Cables para la conexión del módulo.<br>- La descarga y la carga deben ser menores o<br>iguales a 0,25 °C.|
|1.2|SG de CC||10|Pc|- Voltaje nominal de CC : 1500V<br>- Seccionador + fusible<br>- BCU|
|1.3|Caja de<br>conexiones de<br>CC||1|Pc|- Voltaje nominal de CC : 1500V<br>- Seccionador + fusible|

3

4

|2|Estación de<br>MT|Col3|6|pone<br>r|Cada sistema consta de 2.1 ~ 2.3.|
|---|---|---|---|---|---|
|2.1|Inversor de<br>almacenamiento|EBI 215|16|Pc|- Rango de voltaje de CC: 1000 ~ 1500 V.<br>- Salida de CA 215KVA, 690Vac, 50Hz<br>- IP 66 87kg|
|2.2|Transformador<br>de MT||1|Pc|- Transformador de aceite 3440kVA|
|2.3|RMU||1|Pc|- 23 kV DCV<br>- 630A|
|**3 **|**EMS**||**1 **|**pone**<br>**r **||
|**4 **|**GORDO**<br>**Inspección**||**1 **|**pone**<br>**r **|- Billete aéreo de ida y vuelta para un<br>pueblo<br>- 10 días en total incluyendo<br>comidas y alojamiento para un<br>pueblo|
|**5 **|**Servici**<br>**o in**<br>**situ**||**1 **|**pone**<br>**r **|- Billete aéreo de ida y vuelta para dos<br>personas<br>- 120 persona*día en total|

NOTAS:

1. El suministro y la instalación de cables entre el contenedor PCS y el contenedor de baterías están

excluidos del alcance de SOFAR.

2. La inspección FAT es opcional.

5

## 3 Sistema PCS

El sistema PCS ofrece conexión eléctrica entre la red y las baterías. Invierte la CC de las baterías a la CA

cuando se descarga, mientras que convierte la CA de la red a la CC mientras se carga.

Fig.3-1: Vista de elevación del sistema PCS

(Referencia)

### 3.1 Diagrama de circuito

El sistema PCS proporciona una interfaz entre la red y las baterías para realizar la carga y descarga del

ESS de la batería.

Fig.3-2: Circuito principal del sistema PCS (como referencia)

Este producto adopta dispositivos de potencia IGBT avanzados y tecnología de control digital, optimizando

el rendimiento del control y mejorando la confiabilidad. El diseño de la estructura modular hace que la

instalación y el mantenimiento sean convenientes.

### 3.2 Especificaciones técnicas

Tabla 3-1: Parámetros técnicos del sistema PCS

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- instalación y el mantenimiento sean convenientes. ### 3.2 Especificaciones técnicas -->

**Tabla 3-1: Parámetros técnicos del sistema PCS**

| Lado de CC | Col2 |
| --- | --- |
| **Tensión CC máx.** | 1500 V |
| **Tensión CC mín.** | 1000V |
| **Rango de voltaje de CC para potencia**<br>**nominal** | 1000-1500 V |
| **Corriente continua máx.** | 968A*2 |
| **No de entradas de CC** | 4 |
| **Lado de CA**<br>**(rejilla)** | **Lado de CA**<br>**(rejilla)** |
| **Potencia de salida de CA** | 1725*2 kVA @ 45 °C |
| **Tensión nominal de CA** | 690V |
| **Rango de voltaje de CA** | 586,5 - 759 V |
| **Frecuencia nominal de la red**<br>**/ Rango de frecuencia**<br>**de la red** | 50 Hz / 45 - 55 Hz, 60 Hz / 55 - 65 Hz |
| **Corriente alterna THD** | < 3 % (a potencia nominal) |
| **Factor de potencia a potencia**<br>**nominal / Factor de potencia**<br>**ajustable** | > 0,99 / 1 adelantado - 1 rezagado |
| **Potencia reactiva ajustable** | -100% - 100% |
| **Fases de inyección / Fases de**<br>**conexión** | 3/3 |
| **Lado de CA (fuera**<br>**de la red)** | **Lado de CA (fuera**<br>**de la red)** |
| **Voltaje de CA nominal del puerto del**<br>**inversor** | 690V |
| **Rango de voltaje de CA del puerto del**<br>**inversor** | 586,5 - 759 V |
| **Distorsión de voltaje de CA** | < 3 % (carga lineal) |
| **Componente de voltaje de CC** | <0.5% Un (carga de equilibrio lineal) |
| **Capacidad de carga desequilibrada** | 100% |

<!-- Estadísticas: 20 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 7 8 -->
<!-- FIN TABLA 3-1 -->


6

|Lado de CC|Col2|
|---|---|
|**Tensión CC máx.**|1500 V|
|**Tensión CC mín.**|1000V|
|**Rango de voltaje de CC para potencia**<br>**nominal**|1000-1500 V|
|**Corriente continua máx.**|968A*2|
|**No de entradas de CC**|4|
|**Lado de CA**<br>**(rejilla)**|**Lado de CA**<br>**(rejilla)**|
|**Potencia de salida de CA**|1725*2 kVA @ 45 °C|
|**Tensión nominal de CA**|690V|
|**Rango de voltaje de CA**|586,5 - 759 V|
|**Frecuencia nominal de la red**<br>**/ Rango de frecuencia**<br>**de la red**|50 Hz / 45 - 55 Hz, 60 Hz / 55 - 65 Hz|
|**Corriente alterna THD**|< 3 % (a potencia nominal)|
|**Factor de potencia a potencia**<br>**nominal / Factor de potencia**<br>**ajustable**|> 0,99 / 1 adelantado - 1 rezagado|
|**Potencia reactiva ajustable**|-100% - 100%|
|**Fases de inyección / Fases de**<br>**conexión**|3/3|
|**Lado de CA (fuera**<br>**de la red)**|**Lado de CA (fuera**<br>**de la red)**|
|**Voltaje de CA nominal del puerto del**<br>**inversor**|690V|
|**Rango de voltaje de CA del puerto del**<br>**inversor**|586,5 - 759 V|
|**Distorsión de voltaje de CA**|< 3 % (carga lineal)|
|**Componente de voltaje de CC**|<0.5% Un (carga de equilibrio lineal)|
|**Capacidad de carga desequilibrada**|100%|

7

8

|Datos Generales|Col2|
|---|---|
|**Grado de protección**|IP54 (Inversor: IP66)|
|**Rango de temperatura ambiente de**<br>**funcionamiento**|De -35 a 60 °C (> 45 °C de reducción de<br>potencia)|
|**Rango de humedad relativa admisible**|0 - 100 %|
|**Método de enfriamiento**|Refrigeración por aire forzado con<br>control de temperatura|
|**Altitud máxima de funcionamiento**|4000 m (>2000 m de descenso)|
|**Monitor**|LED, WEB HMI|
|**Comunicación**|RS485, CAN, Ethernet|
|**Conformidad**|CE, IEC 62477-1|
|**Compatibilidad con la red**|L/HVRT, control de potencia activa y reactiva y control de<br>velocidad de rampa de potencia,|

NOTAS:

1. El PCS es capaz de exportar/importar potencia reactiva a PF de 0 y puede trabajar en los 4

cuadrantes con un factor de potencia de unidad y rezagado

2. La potencia nominal Pn para el sistema PCS es de 3450kW.

9

## 4 Sistema de batería

### 4.1 Celda de batería

|Muestr<br>a|Artículo|Col3|Especificación|
|---|---|---|---|
||Tipo de batería|Tipo de batería|LFP|
||Dimensión de la celda, ancho x<br>profundo x alto [mm]<br>(sin poste)|Dimensión de la celda, ancho x<br>profundo x alto [mm]<br>(sin poste)|173.9×71.7×207.2|
||Peso (kg)|Peso (kg)|5.4±0.3|
||Capacidad nominal [Ah] (@ 25 °C, 0.5p)|Capacidad nominal [Ah] (@ 25 °C, 0.5p)|280|
||Energía de diseño normativo<br>[Wh] (@ 25 °C, 0.5p)|Energía de diseño normativo<br>[Wh] (@ 25 °C, 0.5p)|896|
||Densidad E|Gravimétrico<br>[Wh/kg]|167|
||Densidad E|Volumétrico [Wh/L]|352|
||Voltaje|Máx. [V]|3.65|
||Voltaje|Nominal [V]|3.2|
||Voltaje|Mín. [V]|2.5|

### 4.2 Módulo de batería

Tabla 4-1 Especificación de la celda de la batería

Tabla 4-2 Especificación del módulo de batería

|Muestr<br>a|Artículo|Col3|Especificación|
|---|---|---|---|
||Configuració<br>n|Configuració<br>n|1P48S|
||Energía de diseño normal [kWh]<br>(@ 25 °C, 0.5p)|Energía de diseño normal [kWh]<br>(@ 25 °C, 0.5p)|43.008|
||Potencia[kW]|Continuo<br>(CHG/DCHG)|21.504 (0.5P)|
||Voltaje nominal (V)|Voltaje nominal (V)|153.6|

10

|Col1|Voltaje de funcionamiento (V)|120~172.8|
|---|---|---|
||Dimensión (W×D×H)|1050 * 765 * 245<br>mm|

11

|Col1|Peso (kg)|≤310kg|
|---|---|---|
||Método de enfriamiento|Refrigeración<br>líquida|
||Método de extinción de<br>incendios|Extinción de<br>incendios a<br>nivel de celda<br>(Perfluoruro)|
||Nivel de protección|IP67|
||Temperatura de trabajo|-30 °C ~ 55 °C|
||Estándares y<br>Certificaciones|IEC62619、UL1973、<br>UN38.3|

### 4.3 Bastidor de baterías

Tabla 4-3 Especificación del bastidor de baterías

|Muestr<br>a|Artículo|Especificación|
|---|---|---|
||Configuración|1P384S|
||Componente<br>clave|8 Módulo|
||Capacidad<br>nominal|280 Ah|
||Energía nominal|344.064 kWh|
||Tensión nominal|1,228.8 Vdc|
||Tarifa C|≤0.5P|
||Voltaje de<br>funcionamiento|960~1,401.6 Vdc|

12

### 4.4 Unidad de contenedor de batería

Cada contenedor de baterías tiene baterías LFP 384S10P con una capacidad de 3440 kWh, sistema de

refrigeración líquida + refrigeración por aire, sistema de extinción de incendios y otros dispositivos

auxiliares en su interior.

Tabla 4-4 Especificación de la unidad de contenedor de bater í a

|Muestr<br>a|Artículo|Especificación|
|---|---|---|
||Capacidad nominal (BOL)|3,44 MWh|
||Rango de voltaje de trabajo|960~1401.6V|
||Tasa de carga y descarga|≤0.5P|
||Temperatura<br>ambiente de<br>funcionamiento|-30 °C ~ 55 °C|
||Método de enfriamiento|Refrigeración por aire + refrigeración<br>líquida|
||Método de extinción de<br>incendios|Extinción de incendios con gas<br>perfluorado (nivel de celda y nivel de<br>cabina) + extinción de incendios con<br>agua de respaldo<br>+ Emisión de gases combustibles +<br>Diseño de venteo de explosión|
||Grado de protección|IP55|
||Grado anticorrosión|C4(C5 opcional)|
||Dimensiones (W*D*H)|6058 * 2438 * 2896 milímetros|
||Peso|~34 T|
||Estándares y<br>Certificaciones|IEC62619/UL1973/UL9540A/UN3536|

13

## 5 Sistema de comunicación

### 5.1 Introducción

El sistema de comunicación BESS realiza el monitoreo de la batería y el sistema PCS, el sistema de

enfriamiento, el monitoreo y control de FFS y otros equipos auxiliares, la asignación de energía entre

subsistemas, la protección y la gestión de alarmas, el equilibrio del subsistema.

El sistema de comunicación BESS consta de tres partes principales.

➢ EMS _ monitoreo y control de nivel de subestación

➢ Monitoreo y control de estaciones de PC y MT

➢ BMS _ Monitoreo y control de baterías y otros subsistemas de monitoreo y

control La arquitectura del sistema de comunicación de la siguiente manera :

Fig.5-1: Topología de comunicación del sistema

### 5.2 Funcionalidad BMS

El sistema BMS incluye 3 niveles: nivel de módulo BMU, BCU a nivel de rack incluido en SG y CMU a

nivel de sistema.

Tabla 5-1: Funcionalidad BMS multinivel

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- El sistema BMS incluye 3 niveles: nivel de módulo BMU, BCU a nivel de rack incluido en SG y CMU a nivel de sistema. -->

**Tabla 5-1: Funcionalidad BMS multinivel**

| Categoría de función | Col2 | Elemento de función | Descripción |
| --- | --- | --- | --- |
| **BMU** | Muestreo | Recogida de la tensión de la<br>batería | Recogida de la tensión de la<br>batería |
| **BMU** | Muestreo | Colección de temperatura del<br>módulo | Recopile la temperatura del<br>módulo. |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 14 15 -->
<!-- FIN TABLA 5-1 -->


|Categoría de función|Col2|Elemento de función|Descripción|
|---|---|---|---|
|**BMU**|Muestreo|Recogida de la tensión de la<br>batería|Recogida de la tensión de la<br>batería|
|**BMU**|Muestreo|Colección de temperatura del<br>módulo|Recopile la temperatura del<br>módulo.|

14

15

|Col1|Gestión de<br>la energía|Equilibrado de la batería|Equilibrado pasivo|
|---|---|---|---|
||Estimación del<br>estado|Estimación del SOC|Estimación del estado de carga<br>de la batería|
||Estimación del<br>estado|Estimación de SOH|Estimación del estado de salud<br>de la batería|
||Comunicación|Comunicación|Comunícate con BCU|
|**BCU**|Muestreo|Colección actual|Recogida de corriente de rack|
|**BCU**|Muestreo|Recopilación de tensión|Recogida de tensión de rack|
|**BCU**|Muestreo|Muestreo de resistencia de<br>aislamiento|Muestree la resistencia de<br>aislamiento del<br>bastidor|
|**BCU**|Muestreo|Colección de temperatura de la<br>placa CMU|Recopile la temperatura de la<br>CMU.|
|**BCU**|Muestreo|Recopilación de voltaje de<br>trabajo de CMU|Recoger la tensión de<br>alimentación para CMU|
|**BCU**|Estimación del<br>estado|Estimación del SOC|Estimación del estado de carga<br>de la batería|
|**BCU**|Estimación del<br>estado|Estimación de SOH|Estimación del estado de salud<br>de la batería|
|**BCU**|Diagnóstico de<br>averías|Diagnóstico de fallos del<br>sistema|Diagnóstico relacionado con la<br>seguridad, por ejemplo,<br>sobrecarga, sobredescarga,<br>sobrecorriente y<br>sobretemperatura.|
|**BCU**|Diagnóstico de<br>averías|Diagnóstico de fallas de BMS|Por ejemplo, diagnosticar el<br>estado del circuito de muestra,<br>el estado del fusible, el estado<br>del contactor y el estado de<br>comunicación|
|**BCU**|Gestión de<br>la energía|Control de carga y descarga|Gestione la carga/descarga a<br>través del control del<br>contactor|
|**BCU**|Gestión de<br>la energía|Carga-descarga Control de<br>potencia|Calcule la corriente o<br>potencia máxima de<br>acuerdo con el SOC y la|

16

|Col1|Col2|Col3|temperatura.|
|---|---|---|---|
||Gestión de la <br>información|Comunicación|Comunícate con CMU y BMU|
||Gestión de la <br>información|Registro de datos|Registre las fallas y la<br>información clave del<br>sistema|

17

|Col1|Col2|Exportación de datos|Exportación de los datos<br>registrados por la CMU|
|---|---|---|---|
|**CMU**|Función base|Comunicación|Comunícate con CSU, FSS,<br>sistema de enfriamiento,<br>medidor|
|**CMU**|Función base|Gestión térmica|Asegurar la estrategia<br>térmica para el<br>sistema de<br>enfriamiento|
|**CMU**|Función base|Procesamiento de datos|Tratar los datos obtenidos del<br>BCU|
|**CMU**|Función base|Actualización de software|Actualización en línea|
|**CMU**|Función base|Registro de fallos|Registre las fallas a nivel del<br>sistema|
|**CMU**|Función base|Registro de datos|Registre los datos de operación en<br>tiempo real|
|**CMU**|Función base|Entrada/Salida Digital|Grabación de señales de E/S<br>digitales en tiempo real|

### 5.3 Funcionalidad de CSU

Tabla 5-2: Funcionalidad de la CSU

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**CMU**|Función base|Registro de datos|Registre los datos de operación en<br>tiempo real| |**CMU**|Función base|Entrada/Salida Digital|Grabación de señales de E/S<br>digitales en tiempo real| ### 5.3 Funcionalidad de CSU -->

**Tabla 5-2: Funcionalidad de la CSU**

| Categoría de función | Col2 | Elemento de función | Descripción |
| --- | --- | --- | --- |
| **CSU** | Función base | Comunicación | Comunícate con CMU, PCS, MV<br>unidad de control de<br>estación, EMS |
| **CSU** | Función base | Actualización de software | Actualización en línea |
| **CSU** | Función base | Registro de fallos | Registre las fallas a nivel del<br>sistema |
| **CSU** | Función base | Registro de datos | Registre los datos de operación en<br>tiempo real |
| **CSU** | Gestión de<br>la energía | Equilibrado del sistema de<br>baterías | Control de equilibrado |
| **CSU** | Control | Control PCS | Controle el arranque y apagado<br>de PCS y la coordinación<br>de PCS |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 18 Figura 5-1: Estructura del sistema de comunicación -->
<!-- FIN TABLA 5-2 -->


|Categoría de función|Col2|Elemento de función|Descripción|
|---|---|---|---|
|**CSU**|Función base|Comunicación|Comunícate con CMU, PCS, MV<br>unidad de control de<br>estación, EMS|
|**CSU**|Función base|Actualización de software|Actualización en línea|
|**CSU**|Función base|Registro de fallos|Registre las fallas a nivel del<br>sistema|
|**CSU**|Función base|Registro de datos|Registre los datos de operación en<br>tiempo real|
|**CSU**|Gestión de<br>la energía|Equilibrado del sistema de<br>baterías|Control de equilibrado|
|**CSU**|Control|Control PCS|Controle el arranque y apagado<br>de PCS y la coordinación<br>de PCS|

18

Figura 5-1: Estructura del sistema de comunicación

19

## 6 Introducción al sistema y equipos auxiliares
### 6.1 Especificación del contenedor

Tabla 6-1: Especificaciones del contenedor

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 19 ## 6 Introducción al sistema y equipos auxiliares ### 6.1 Especificación del contenedor -->

**Tabla 6-1: Especificaciones del contenedor**

| Artículo | Especificación |
| --- | --- |
| Dimensiones de la unidad PCS (W *<br>H * D) | 2 * 2790 x 2110 x 980 mm |
| Dimensiones de la unidad de batería<br>(W * H * D) | 6058 * 2438 * 2896 mm |
| Peso de la unidad PCS | 2 * 1500Kg |
| Peso de la unidad de batería | 34.000 Kg |
| Rango de temperatura de<br>funcionamiento | -30 ~ 55 °C (> 45°Cde reducción de<br>potencia) |
| Humedad relativa | 100% |
| Altitud máx. de trabajo | 1000 m (estándar) / >1000 m (opcional) |
| Grado de protección | IP55 |
| Grado de anticorrosión | C4 |
| Concepto de refrigeración de la<br>unidad de batería | Refrigeración líquida + refrigeración por<br>aire |
| Concepto de refrigeración de la<br>unidad PCS | Refrigeración por aire forzado con<br>control de temperatura |

<!-- Estadísticas: 11 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 20 ### 6.2 Sistema de refrigeración líquida + refrigeración por aire -->
<!-- FIN TABLA 6-1 -->


|Artículo|Especificación|
|---|---|
|Dimensiones de la unidad PCS (W *<br>H * D)|2 * 2790 x 2110 x 980 mm|
|Dimensiones de la unidad de batería<br>(W * H * D)|6058 * 2438 * 2896 mm|
|Peso de la unidad PCS|2 * 1500Kg|
|Peso de la unidad de batería|34.000 Kg|
|Rango de temperatura de<br>funcionamiento|-30 ~ 55 °C (> 45°Cde reducción de<br>potencia)|
|Humedad relativa|100%|
|Altitud máx. de trabajo|1000 m (estándar) / >1000 m (opcional)|
|Grado de protección|IP55|
|Grado de anticorrosión|C4|
|Concepto de refrigeración de la<br>unidad de batería|Refrigeración líquida + refrigeración por<br>aire|
|Concepto de refrigeración de la<br>unidad PCS|Refrigeración por aire forzado con<br>control de temperatura|

20

### 6.2 Sistema de refrigeración líquida + refrigeración por aire

El sistema utiliza un sistema de refrigeración líquida + refrigeración por aire para la disipación de calor y

puede utilizarse en un entorno de -30 a 55 °C.

El principal método de enfriamiento de la batería es la refrigeración líquida, que es una tecnología que

utiliza un líquido como refrigerante para eliminar el calor de las partes calentadas. Tiene buena

homogeneidad de temperatura y bajo consumo de energía. El sistema de refrigeración líquida se compone

principalmente de tuberías, bombas, intercambiadores de calor y compresores. El refrigerante del sistema

es etilenglicol.

Fig.6-1 Vista superior del sistema de

refrigeración

Fig.6-3 Vista en perspectiva del sistema

de refrigeración

Fig.6-2 Vista frontal del sistema de

refrigeración

Fig.6-4 Tubo de enfriamiento a nivel de

paquete

Como el sistema de refrigeración líquida siempre cumple con los problemas de condensación, SOFAR

adopta la refrigeración por aire para reducir la temperatura interna del contenedor y la humildad del aire,

lo que hace posible la anticondensación.

Fig.6-5 Unidad fancoil

### 6.3 Sistema de extinción de incendios

El FFS consiste en la extinción de incendios con gas perfluorohexanona y la extinción de incendios con

agua de respaldo. El gabinete BESS está equipado con control de incendios, sistema de supresión de

21

gas, sistema de extinción de incendios de agua, detector de humo, detector de temperatura y detector de

gas combustible. El sistema es detectado por equipos de detección de gases combustibles, detectores de

humo, detectores de temperatura, etc.

Cuando se detecta una anomalía, el host del controlador de incendios dará una alarma de incendio,
controlará el

22

Válvula solenoide para iniciar el sistema de extinción de incendios para extinguir el fuego y realizar el

control lógico correspondiente con el sistema de batería de control de comunicación CMU.

Fig.6-6 Descripción general del SFS Fig.6-7 Diagrama de tuberías

**6.3.1** **Sistema de extinción de incendios por medios gaseosos**

El sistema de extinción de incendios de gas está compuesto por un controlador de alarma contra

incendios, un detector de humo, un detector de temperatura, un sensor compuesto, una alarma de sonido

y luz, un indicador de descarga de gas, un botón manual de arranque/parada de emergencia, una botella

de almacenamiento de agente de extinción de incendios, un dispositivo de accionamiento

electromagnético, una señal de presión, un gasoducto y un rociador. El sistema de extinción de incendios

de gas se realiza en el nivel de la celda de la batería y en el nivel del contenedor.

Fig.6-8 Diagrama de tubería de gas a nivel de
contenedor

**6.3.2** **Sistema de extinción de incendios de agua**

Fig.6-9 Diagrama de tubería de gas a
nivel de celda

El sistema de extinción de incendios de agua consta de juntas de fuego de agua, tuberías y boquillas.

23

Fig.6-10 Tubería de extinción de incendios de agua

24

## 7 Dibujo
### 7.1 Dibujo del contenedor de la batería

Fig.7-1 Dimensión del contenedor de la batería

Fig.7-2 Dimensión del contenedor de la batería ( puerta abierta )

25

## 8 Curvas de degradación

1. La suposición de temperatura dentro de los contenedores es constante para cada caso y es igual

a 25±5 ° C, 1 ciclo por día, tasa de 0.25 C, 50% de SOC en reposo, 95% de DOD.

2. El "0" en Year Blank es para respetar el punto de tiempo "COD". Definición de COD: De FAT a

SAT no será más de 3 meses.

3. En la tabla de cálculo se han tenido en cuenta varias pérdidas.

4. El EOL del BESS es cuando los tiempos de ciclo son 7000 o el SOH del sistema de baterías es

del 70%, que llega en primer lugar.

|Tipo de<br>batería|Enfriamiento|Almacenamient<br>o máximo<br>Temperatura|Tasa P|Ciclo<br>/día|DOD|RSOC|
|---|---|---|---|---|---|---|
|CATL LFP<br>280 Ah|Líquido +<br>Aire<br>enfriamien<br>to|40°C|0.5|1|95%|50%|
|Transporte y<br>almacena<br>miento<br>atenuación|Eficiencia<br>de carga<br>PCS|Eficiencia de<br>descarga de<br>PCS|LV DC<br>Pérdi<br>da<br>de<br>cabl<br>e|VI AC<br>Pérdi<br>da<br>de<br>cabl<br>e|MV<br>Eficiencia<br>del<br>transformad<br>or|Pérdida<br>de<br>cable<br>de MT|
|99.70%<br>(3 meses)|97.83%|98.24%|99.90%|99.90%|99%|99.60%|

Tabla 8.1: Curva de degradación de la capacidad de la batería

<!-- INICIO TABLA 8.1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---|---| |CATL LFP<br>280 Ah|Líquido +<br>Aire<br>enfriamien<br>to|40°C|0.5|1|95%|50%| |Transporte y<br>almacena<br>miento<br>atenuación|Eficiencia<br>de carga<br>PCS|Eficiencia de<br>descarga de<br>PCS|LV DC<br>Pérdi<br>da<br>de<br>cabl<br>e|VI AC<br>Pérdi<br>da<br>de<br>cabl<br>e|MV<br>Eficiencia<br>del<br>transformad<br>or|Pérdida<br>de<br>cable<br>de MT| |99.70%<br>(3 meses)|97.83%|98.24%|99.90%|99.90%|99%|99.60%| -->

**Tabla 8.1: Curva de degradación de la capacidad de la batería**

| Año | Tiempo de<br>ciclo | SOH |
| --- | --- | --- |
| 0 | 0 | 100.00% |
| 1 | 365 | 93.36% |
| 2 | 730 | 91.37% |
| 3 | 1095 | 89.45% |
| 4 | 1460 | 87.69% |
| 5 | 1825 | 86.19% |
| 6 | 2190 | 84.84% |
| 7 | 2555 | 83.56% |
| 8 | 2920 | 82.26% |
| 9 | 3285 | 80.86% |
| 10 | 3650 | 79.69% |
| 11 | 4015 | 78.64% |

<!-- Estadísticas: 12 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 26 |12|4380|77.58%| |---|---|---| -->
<!-- FIN TABLA 8.1 -->


|Año|Tiempo de<br>ciclo|SOH|
|---|---|---|
|0|0|100.00%|
|1|365|93.36%|
|2|730|91.37%|
|3|1095|89.45%|
|4|1460|87.69%|
|5|1825|86.19%|
|6|2190|84.84%|
|7|2555|83.56%|
|8|2920|82.26%|
|9|3285|80.86%|
|10|3650|79.69%|
|11|4015|78.64%|

26

|12|4380|77.58%|
|---|---|---|
|13|4745|76.53%|
|14|5110|75.47%|
|15|5475|74.42%|

27

|16|5840|73.36%|
|---|---|---|
|17|6205|72.31%|
|18|6570|71.25%|
|19|6935|70.19%|
|20|7000|70.00%|

28

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1: Especificación de la celda de la batería**

| Muestr<br>a | Artículo | Col3 | Especificación |
| --- | --- | --- | --- |
|  | Configuració<br>n | Configuració<br>n | 1P48S |
|  | Energía de diseño normal [kWh]<br>(@ 25 °C, 0.5p) | Energía de diseño normal [kWh]<br>(@ 25 °C, 0.5p) | 43.008 |
|  | Potencia[kW] | Continuo<br>(CHG/DCHG) | 21.504 (0.5P) |
|  | Voltaje nominal (V) | Voltaje nominal (V) | 153.6 |

**Tabla 4-3: Especificación del bastidor de baterías**

| Muestr<br>a | Artículo | Especificación |
| --- | --- | --- |
|  | Configuración | 1P384S |
|  | Componente<br>clave | 8 Módulo |
|  | Capacidad<br>nominal | 280 Ah |
|  | Energía nominal | 344.064 kWh |
|  | Tensión nominal | 1,228.8 Vdc |
|  | Tarifa C | ≤0.5P |
|  | Voltaje de<br>funcionamiento | 960~1,401.6 Vdc |

**Tabla 4-4: Especificación de la unidad de contenedor de bater í a**

| Muestr<br>a | Artículo | Especificación |
| --- | --- | --- |
|  | Capacidad nominal (BOL) | 3,44 MWh |
|  | Rango de voltaje de trabajo | 960~1401.6V |
|  | Tasa de carga y descarga | ≤0.5P |
|  | Temperatura<br>ambiente de<br>funcionamiento | -30 °C ~ 55 °C |
|  | Método de enfriamiento | Refrigeración por aire + refrigeración<br>líquida |
|  | Método de extinción de<br>incendios | Extinción de incendios con gas<br>perfluorado (nivel de celda y nivel de<br>cabina) + extinción de incendios con<br>agua de respaldo<br>+ Emisión de gases combustibles +<br>Diseño de venteo de explosión |
|  | Grado de protección | IP55 |
|  | Grado anticorrosión | C4(C5 opcional) |
|  | Dimensiones (W*D*H) | 6058 * 2438 * 2896 milímetros |
|  | Peso | ~34 T |
|  | Estándares y<br>Certificaciones | IEC62619/UL1973/UL9540A/UN3536 |
