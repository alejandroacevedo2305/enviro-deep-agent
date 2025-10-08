---
title: PROYECTO DE INSTALACIÓN FOTOVOLTAICA CONECTADA A LA RED ELÉCTRICA DE BAJA TENSIÓN DE 15,75 KWP DE POTENCIA
author: PC
date: D:20231128161656-03'00'
language: es
type: invoice
pages: 17
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 3. IMPLANTACIÓN GENERAL
  - 4. OBRA CIVIL
  - 5. ESTIMACIÓN PRODUCCIÓN ENERGÉTICA.
-->

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

**ÍNDICE**

1. DESCRIPCIÓN GENERAL DEL SISTEMA...................................................................... 3

2. COMPONENTES DE LA INSTALACIÓN ........................................................................ 5

DESCRIPCION DE ELEMENTOS PRINCIPALES ......................................................... 6

CONFIGURACIÓN ............................................................................................................ 13

3. IMPLANTACIÓN GENERAL ............................................................................................ 14

4. OBRA CIVIL ........................................................................................................................ 16

5. ESTIMACIÓN PRODUCCIÓN ENERGÉTICA................................................................. 17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 2/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

**1.** **DESCRIPCIÓN GENERAL DEL SISTEMA**

_Ilustración 1 Vista de sistemas de la planta solar fv_

Los sistemas de almacenamiento conectados a red son soluciones alternativas reales a la

diversificación de producción de electricidad, y se caracterizan por ser sistemas no contaminantes

que contribuyen a reducir las emisiones de gases nocivos (CO2, SOx, NOx) a la atmósfera, utilizar

recursos locales de energía y evitar la dependencia del mercado exterior del petróleo.

Una planta de almacenamiento presenta diferentes subsistemas perfectamente diferenciados:

- **Módulos de baterías (Containers y Battery Stacks).** Los módulos de baterías se instalan

formando unas infraestructuras capaces de almacenar energía para liberarla en el momento que

sea necesario. Estos sistemas de almacenamiento se podrán cargar directamente de la red o a

través de un parque fotovoltaico adyacente.

- **Sistema de acondicionamiento de potencia (PCS)** . Para poder inyectar la corriente

almacenada en las baterías a la red eléctrica, es necesario transformarla en corriente alterna de

similares condiciones a la de la red. Esta función es realizada por unos equipos denominados

inversores, que basándose en tecnología de potencia transforman la corriente continua

procedente de los módulos en corriente alterna de la misma tensión y frecuencia que la de la

red pudiendo, de esta forma, operar la instalación fotovoltaica en paralelo con ella. Estos

Inversores trabajan de forma bidireccional, para ajustar la tensión tanto si se consume de la red

y almacenarla como si se tiene que inyectar a la red. La conexión del bloque de

almacenamiento se propone en AC coupling a un cierto nivel de tensión mínimo de hasta 23

kV.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 3/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

**Interfaz de conexión a red (EMS, Energy Management System)** . Para poder conectar la

instalación almacenamiento a la red en condiciones adecuadas de seguridad tanto para personas

como para los distintos componentes que la configuran, ésta ha de dotarse de las protecciones

y elementos de facturación y medida necesarios. El EMS será la capa de control para el

dispatching de energía del storage hacia la red o las consignas locales establecidas para atender

los servicios de energía disponibles. Este EMS Estará interconectado con el Control de planta

global de la planta (PPC o SCADA de Planta) FC Tabernas de forma que existe una

coordinación adecuada entre la parte solar fotovoltaica y la parte de almacenamiento de

energía. A nivel de control local del sistema de almacenamiento, está el BMS que ofrecerá

todas las señales necesarias para el control y operación de la energía almacenada en baterías.

El BMS, el PPC y el EMS estará interconectados y coordinados debidamente. Existirán

equipos de medida que permitan monitorizar y controlar los flujos de energía tomados de la

red y transferidos a la red por parte del sistema de almacenamiento.

_Ilustración 2 Esquema general del control de la Planta y EMS_

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 4/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

**2.** **COMPONENTES DE LA INSTALACIÓN**

La potencia del sistema de almacenamiento será de hasta 30 MW y capacidad de hasta 5 horas,

ofreciendo hasta 150 MWh. La tecnología para instalar será de Ion Litio con química LFP. El

layout de la planta de almacenamiento se proyectará con contenedores de 40 pies, un recinto para

equipos de MT y Servicios Auxiliares y otro recinto de control.

El proyecto permitirá consumir y evacuar energía para la planta de almacenamiento. Se compartirá

infraestructura de la parte fotovoltaica.

La planta de almacenamiento deberá tener:

 - Cableado e interconexiones.

 - SKIDs para PCS adecuados para el almacenamiento (Bidireccionales).

 - Sistemas para alojar las Baterías, su sistema de control y refrigeración.

La configuración preliminar adoptada tendrá en consideración la solución técnica aportada por

GRENERGY. **No obstante, esta solución no es vinculante y puede verse modificada a lo largo**

**de la ejecución del proyecto** .

La configuración preliminar elegida tiene las siguientes características:

|Tecnología|Ión-Litio|
|---|---|
|**Tensión**|Hasta 33 kV|
|**Rango de ciclos**|1-1.5|
|**Pot. Máx BESS**|30 MW|
|**Capacidad Máx.**|150 MWh<br>|
|**Acoplamiento**|AC~~1~~|
|**Solución Modular**|Container 40’|

_Tabla 1- Configuración Sist. Almacenamiento_

1 Esta solución puede verse modificada a una solución DC.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 5/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

**DESCRIPCION DE ELEMENTOS PRINCIPALES**

 - **Full Skid InverterStation**

_Ilustración 3 Datasheet SKID InverterStation3430FSK_

El SKID es la parte encargada de albergar los inversores y de transformar la corriente alterna a la
tensión de evacuación. El SKID cuenta con un transformador BT/MT, transformador de SSAA y
celdas de MT.

Se trata de una solución SKID que puede contener hasta 4 inversores. Para esta solución se ha
escogido 4 inversores con una potencia de transformación de 5,145 MVA @ 30o. Será capaz de
transformar hasta 33 kV (según configuración del proyecto).

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 6/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

|Col1|Transformador BT/MT<br>4 inversores Ingecon15<br>Transformador SSAA|Col3|Col4|
|---|---|---|---|
||Transformador BT/MT<br>Transformador SSAA<br>4 inversores Ingecon15|4 inversores Ingecon15|00TLB578|
|Celdas MT||||

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 7/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

 - **Ingecon Sun 1500 Vdc B Series Inverter.**

_Ilustración 5 Datasheet Inversores Ingecon1500TLB578_

Los inversores son los encargados en transformar la corriente continua proveniente de las baterías
en corriente alterna.

Se ha optado por una solución de cuatro inversores centrales de exterior.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 8/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

_Ilustración 6 Inversor Ingecon1500TLB57. (Referencial)_

_Ilustración 7 Esquema Inversor Ingecon1500TLB578. (Referencial)_

Para la conversión de la corriente continua liberada por las baterías en corriente alterna de las mismas

características (tensión y frecuencia) que la de la red se utilizará un equipo denominado inversor.

La suma de la potencia nominal de los inversores coincidirá con la potencia nominal de

almacenamiento.

Los inversores cumplen con los requerimientos técnicos y de seguridad necesarios para su

interconexión a la red de baja tensión, así como con las directivas Internacionales sobre seguridad

eléctrica y compatibilidad electromagnética.

Las características técnicas más relevantes de estos inversores son equivalentes a los inversores

fotovoltaicos definidos en la memoria descriptiva del proyecto fotovoltaico. Además, estos inversores

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 9/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

tendrán la particularidad de ser bidireccionales. Es decir: serán capaces de transformar la corriente

continua generada en las baterías en corriente alterna para exportar a la red y de transformar la corriente

alterna proveniente de la Red o del sistema fotovoltaico en corriente continua para poder almacenar la

energía en las baterías.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 10/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

 - **Battery racks NESP250.**

Las unidades de almacenamiento modulares son los módulos de almacenamiento la cuales se

componen de celdas de baterías conectaras en serie y paralelo y cubiertas por una estructura que

las protege del exterior, a continuación, imagen referencial:

_Ilustración 8 Ejemplo Modulo de Almacenamiento_

Se dispondrán de 88 contenedores de 40’ del tipo Twin [2x20ft] (o similar) para poder almacenar las

baterías.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 11/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

_Ilustración 9 Ejemplo contenedor 40’ tipo Twin [2x20ft]_

El sistema de almacenamiento será refrigerado. Adicionalmente, las baterías tendrán un Sistema de

Gestión (BMS), que tendrá las siguientes funciones:

 - Monitorización de las condiciones de trabajo de la batería.

 - Estimación del Estado de Carga (SOC)

 - Estimación del Estado de Salud (SOH)

 - Control de Descarga

 - Control Termal

 - Alarma y Diagnosis de Fallos

 - Monitor con información

 - Balance

 - Protecciones

De igual forma el sistema global contará con un EMS (Energy Management System) para hacer el

despacho de energía conforme a los requisitos del proyecto y de los mercados de energía que se

consideren.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 12/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

**CONFIGURACIÓN**

Para esta configuración se usará 11 SKID con 4 inversores Ingecon1500TLB578 (o similar).

El grupo de Almacenamiento se compondrá en 88 contendores, Cada contendor contendrá 8 rack

que a su vez, cada rack contendrá 15 módulos de almacenamiento. Finalmente, con dicha

configuración se obtiene una **P** **storage** **= 30 MWac** con una capacidad de **150 MWh (BOL** **[2]** **).**

2 BOL: Beginning Of Life (Capacidad de la Batería al inicio de la instalación)

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 13/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

# 3. IMPLANTACIÓN GENERAL

La disposición del sistema de almacenamiento modular, correspondiente con un grupo de

conversión de potencia (PCS) y sistema de baterías se plantea de la siguiente manera:

_Ilustración 10 Esquema implantación_

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 14/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

El sistema de almacenamiento considera 11 grupos de almacenamiento como el que se muestra en

la Ilustración 10.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 15/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

# 4. OBRA CIVIL

Se describe, a continuación, la solución recomendada por fabricante asociada a la obra civil de la

instalación de almacenamiento.

Para instalar el SKID se instalará una losa de hormigón. (Ejemplo ilustración 13)

En cuanto a los contenedores que contengan las Baterías, se dispondrá una solución a base de

zapatas que mantengan en altura al bloque.

_Ilustración 11 Obra civil-Zapatas_

Se estudiará también la incorporación de una losa de hormigón donde los contenedores o las

zapatas se apoyen.

_Ilustración 12 Obra civil - losa_

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 16/17

SOLUCIÓN PRELIMINAR ALMACENAMIENTO

# 5. ESTIMACIÓN PRODUCCIÓN ENERGÉTICA.

La conexión del sistema de almacenamiento con la instalación fotovoltaica es en AC coupling.

Se estima que las baterías trabajen en un rango de operación de entre **1 y 1,5 ciclos diarios** .

Se estiman unas pérdidas (1 −η ) del 15% a considerar:

 - Pérdidas en la línea de evacuación

 - Pérdidas PCS

 - RTE

Se reservan 5 días al año para mantenimiento fuera de operación.

La batería descargará durante 5 horas. El horario de operación diario tiene que ser aún definido.

E BESS (GWh) = P BESS ∙h∙(1 −η) ∙nociclos∙ [días operación]

año

Se estima una producción anual mínima de **130 GWh.**

Esta energía será exportada a la Red mediante el sistema de almacenamiento. La energía

almacenada podrá venir de la Instalación Fotovoltaica o de la Red.

La energía se almacenará en el sistema de almacenamiento preferentemente durante horario diurno

para poder aprovechar al máximo el excedente generado por el proyecto solar.

La energía almacenada se descargará cuando no se registre recurso solar. Se elegirá el rango

horario desde las 18:00 hasta las 22:59 horas.

Esta configuración puede verse variada a lo largo de la consecución del proyecto.

SOLUCIÓN PRELIMINAR ALMACENAMIENTO PARA PROYECTO **GRAN TENO** Página 17/17