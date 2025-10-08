---
title: Sin título
author: lesueug
date: D:20220316155409-03'00'
language: es
type: manual
pages: 7
has_toc: False
has_tables: True
extraction_quality: high
---

**CARACTERISTICAS GENERALES DE DISEÑO - PROYECTO HYEX PRODUCCION DE**

**HIDROGENO VERDE**
**SISTEMA DE DETECCIÓN FUEGO Y GAS**

**Contenido**
1 INTRODUCCIÓN ...................................................................................................................... 2

2 NORMAS, ESTÁNDARES Y REGULACIONES ....................................................................... 2

2.1 Normativa Nacional ....................................................................................................... 2

2.2 Estándares y códigos internacionales ........................................................................... 2

3 SISTEMA DE DETECCIÓN DE FUEGO Y GAS (SDFG) ......................................................... 4

3.1 ACCIONES .................................................................................................................... 4

3.2 CARACTERÍSTICAS GENERALES .............................................................................. 4

3.3 REQUERIMIENTOS SIL ............................................................................................... 4

3.4 COMPONENTES .......................................................................................................... 5

3.4.1 DETECTORES DE FUEGO ........................................................................................... 5

3.4.2 DETECTORES DE GAS ................................................................................................ 6

3.4.3 PULSADORES MANUALES .......................................................................................... 6

4 SISTEMA INSTRUMENTADO DE SEGURIDAD (SIS) ............................................................. 7

1

**1** **INTRODUCCIÓN**

El presente documento establece los criterios generales de aplicación en el proyecto HyEx para el

diseño de detección de fugas, calor e incendio, así también como la secuencia general de actuación

del sistema de detención de emergencia (ESD por sus siglas en Inglés).

**2** **NORMAS, ESTÁNDARES Y REGULACIONES**

**2.1** **Normativa Nacional**

A continuación, se listan la normativa chilena más relevante que pudiera ser de aplicación en el

proyecto:

|Código|Título|Alcance|
|---|---|---|
|NCh 382|Terminología y clasificación<br>general de las sustancias<br>peligrosas|Especifica la terminología y clasificación<br>general de las sustancias peligrosas.|
|NCh 1377|Cilindros de Gas para uso<br>Industrial - Identificación del<br>contenido|Define la identificación del contenido en los<br>cilindros de gas para aplicaciones<br>industriales.|
|NCh 2190|Sustancias peligrosas - Marcas<br>para información de riesgos|Establece la codificación para la<br>identificación de riesgos en sustancias<br>peligrosas.|
|NCh 2369|Diseño sísmico de estructuras e<br>instalaciones industriales|Establece los requerimientos para el diseño<br>sísmicos de estructuras y aplicaciones<br>industriales.|
|NCh Elec.<br>4|Electricidad - Instalaciones de<br>consumo en baja tensión|Establece las condiciones mínimas de<br>seguridad requeridas e instalaciones<br>eléctricas de baja tensión.|
|DS 43|Reglamento de Almacenamiento<br>de Sustancias Peligrosas|Regula el almacenamiento y manejo de<br>sustancias peligrosas.|
|DS 298|Reglamenta Transporte de<br>Cargas Peligrosas por Calles y<br>Caminos|Regula el transporte de las sustancias<br>peligrosas en calles y rutas.|

**2.2** **Estándares y códigos internacionales**

El listado a continuación tiene carácter referencial y debe considerarse como no restrictive:

 - ASME American Society of Mechanical Engineers

Con atención particular a:

**-**
ASME II, Boiler and Pressure vessel code - Materials

**-**
ASME VIII div 1, Boiler and Pressure vessel code - Rules for construction of pressure

vessels

**-**
ASME B16.5, Pipe flanges and flanged fittings

**-**
ASME B31.12, Hydrogen piping and Pipelines

**-**
ASME B31.3, Process piping

 - ATEX 2014/34/EU, Equipment for Potentially Explosive Atmospheres

 - CGA H-5, Standards for Bulk Hydrogen Systems

 - ISO International Organization for Standardization

2

Con atención particular a:

**-**
ISO 10286, Gas cylinders - Terminology

**-**
ISO 834-1, Fire resistance test -- Elements of building construction -- Part 1: General

requirements

**-**
ISO 4126-1, Safety devices for protection against excessive pressure -- Part 1: Safety

valves

**-**
ISO 4126-2, Safety devices for protection against excessive pressure -- Part 2:

Bursting disc safety devices

**-**
ISO 11114-1, Gas cylinders - Compatibility of cylinder and valve materials with gas

contents - Part 1: Metallic material

**-**
ISO 14687-2, Hydrogen fuel - Product specification - Part 2: Proton exchange

membrane (PEM) fuel cell applications for road vehicles

**-**
ISO/TR 15916 Basic considerations for the safety of hydrogen systems

**-**
ISO 17268, Compressed hydrogen surface vehicle fuelling connection devices

**-**
ISO 26142, Hydrogen detection apparatus -- Stationary Applications

**-**
ISO 31000, Risk management Principles and guidelines

**-**
ISO 22734, Hydrogen Generators using Water Electrolysis Process

**-**
ISO 14687, Hydrogen Fuel Product Specification

**-**
ISO 4126, Safety Devices for Protection against Excessive Pressures

**-**
ISO 5199, Technical specification for centrifugal pumps

**-**
ISO 12944, Paints and Varnishes

**-**
ISO 13501, Fire Classification of Construction Products

**-**
ISO 14847, Rotary Positive Displacement Pumps

**-**
ISO 15761, Steel gate, Globe and Check Valves

**-**
ISO/TS 19880-1, Gaseous hydrogen - Fueling stations - Part 1

 - NFPA National Fire Protection Association

Con atención particular a:

**-**
NFPA 2, Hydrogen Technologies Code

**-**
NFPA 55, Storage, Use and Handling of Compressed gases and Cryogenic fluids in

portable and stationary Containers, Cylinders and tanks

**-**
NFPA 70, National Electric Code

**-**
NFPA 101, Life safety code

 - OSHA Occupational Safety and Health Administration

 - OSA 1910.103, Hazardous Materials - Hydrogen.

 - SAE International

Con atención particular a:

**-**
SAEJ2600, Compressed Hydrogen Surface Vehicle Fueling connection devices.

**-**
SAEJ2601, Hydrogen Refueling Standard

**-**
SAE J2719, Hydrogen fuel Quality for Fuel Cell Vehicles

 - OSHA Occupational Safety and Health Administration

Otros estándares reconocidos mundialmente y que pudieran ser de aplicación en el proyecto son:

AIEE, AISC, AISI, ANSI, API, AS, ASCE, ASTM, AWS, AZN, CGA, EN, IEC, IEEE, NEMA, NEC,

etc.

3

**3** **SISTEMA DE DETECCIÓN DE FUEGO Y GAS (SDFG)**

El SDFG es un conjunto de elementos que incluyen sensores, procesadores lógicos y elementos

de control, cuya es detectar de manera automática la presencia de gases inflames (en este caso

del hidrogeno) o fuego e iniciar una respuesta para mitigar el impacto de la liberación y generación

de fugas de hidrógeno y alertar sobre la condición detectada al personal.

**3.1** **ACCIONES Y MEDIDAS**

Para la detección de H2 en el ambiente se considerarán los siguientes límites de activación:

 - El inferior, fijado a un valor del 25 % del LEL, que lleva a los equipos de producción y de

compresión de hidrógeno a un estado de stand-by y envía además una alerta al operador de

la planta,

 - -Si la fuga supera un valor del 50 % del LEL, se activará la parada de emergencia (ESD)

mediante un relé de seguridad y alertando al operador (ver sección 4 de este documento)

Ante una detección de Fuego se genera la parada de emergencia (ESD)

El propósito general del SDFG es llevar a cabo las siguientes acciones cuando se generan fugas

de hidrógeno en la instalación:

 - Activación y visualización de alarmas en forma selectiva en la sala de control y otras áreas de

la planta.

 - Cierre automático de las válvulas asociadas al sistema de producción de hidrógeno

 - Detención automática de los sistemas de acondicionamiento de aire cuando se requiera.

 - Activación del Sistema de Detención de Emergencia (ESD) de la planta. Para mayor detalle

ver la sección 4 de este documento.

 - Activación automática del Sistema General de Alarma (SGA) de la planta.

**3.2** **CARACTERÍSTICAS GENERALES**

Todos los cables de señales de entrada y salida al SDFG los cuales serán resistentes al fuego

según la norma IEC-60331, o en su defecto a prueba de fuego.

El SDFG y el ESD serán sistemas completamente segregados uno del otro y todas las señales de

entrada deben ser diseñadas en modo falla segura.

El SDFG estará configurado con la técnica del voto instrumentado para poder filtrar falsas señales

o alarmas y evitar paros de planta innecesarios que pudieran acarrear situaciones

contraproducentes en términos de seguridad.

**3.3** **REQUERIMIENTOS SIL**

El SDFG estará diseñado de acuerdo a los requerimientos SIL (Safety Integrity Level por sus siglas

en inglés) según lo siguiente:

 - La lógica de resolución de fuego será SIL3, de acuerdo con las normas EN50402:2006 y

IEC61508:2011.

4

 - Los contactos de ingreso al panel PASCI serán SIL2.

 - Los detectores de H2 en las rejillas de ventilación del edificio de electrólisis serán del tipo

catalíticos y certificados como SIL2.

Para la detección de fuego, se podrá considerará:

 - Detección de flama de H2: detectores del tipo Multi-IR con certificación SIL2 y a prueba de

fuego.

 - Detección de flama de carbono: detectores del tipo 3IR con certificación SIL2 y a prueba de

fuego.

**3.4** **COMPONENTES**

Los componentes principales del SDFG son:

 - Dispositivos de iniciación de terreno: detectores de fuego y gas, pulsadores manuales.

 - Señales de entrada de terreo para el sistema de detección de fuego. Estas señales son

enviadas al Panel de Alarmas del Sistema Contraincendios (PASCI) ubicado en la sala de

control principal.

 - Interface con los sistemas de supresión de incendios en las salas eléctricas del tipo

NOVEC1230 o similar.

**3.4.1** **DETECTORES DE FUEGO**

En la selección final del equipamiento las siguientes tecnologías podrán ser consideradas:

3.4.1.1 Detectores de fuego en áreas abiertas

Para la detección de flama de H2 en áreas abiertas, en particular para el área de almacenamiento

de H2 y compresores:

 - IR.

 - Multi IR.

 - UV/IR.

Para otros tipos de fuego, puede utilizarse detección.

 - Ultravioleta (UV).

 - Ultravioleta/Infraroja (UV/IR).

 - Infraroja Triple (IR3).

 - Spectro múltiple (UV/Dual IR/VIS).

 - Spectro multiple triple IR (IR/IR/IR/Visible).

Para zonas no clasificadas, la siguiente tecnología de detección será considerada:

 - XP95: detección óptica de humo.

 - XP95 detección de calor.

5

 - 3IR detección de flama (por ejemplo, en transformadores eléctricos).

3.4.1.2 Detectores de incendios en edificios

Los detectores de incendios utilizados en áreas cerradas como el edificio de electrolisis serían los

siguientes:

 - Detector de calor (termostático o tasa de aumento)

 - Detector de humo óptico para:

 - Detectores combinados de calor y humo

 - Detector de llama (ver áreas abiertas y al aire libre)

El tipo de detectores se elegirá en función de la capacidad de estabilizar su sensibilidad con

respecto a la variación de presión, humedad y temperatura.

**3.4.2** **DETECTORES DE GAS**

Para la detección de H2 se consideran las siguientes tecnologías ya que serían las más adecuados

para la detección de hidrógeno y para el rango de detección requerido (LEL) son:

 - Detectores de perlas catalíticas (pellistor).

 - Detectores electroquímicos.

Los detectores de H2 se instalarán principalmente por encima del equipo de procesos y no cerca,

acorde con la altura y arquitectura del edificio para prevenir o detectar temprano una posible

acumulación de H2 en las zonas más altas, por la baja densidad del gas.

Cabe mencionar que además de la detección automática con los detectores antes mencionados,

dentro del plan de mantenimiento e inspección se realizarán campañas de detección específicas

con detectores para H2 del tipo puntual o de trayectoria abierta y siguiendo una metodología

adecuada para tal.

**3.4.3** **PULSADORES MANUALES**

El pulsador manual de alarma o estación manual es un dispositivo diseñado para ser activado en

caso de incendio, apretando un botón o tirando de una palanca, esta activación informa de

inmediato a la central de detección de incendios.

Se dispondrá de pulsadores manuales en las áreas de procesos (planta de producción hidrogeno y

almacenamiento de hidrogeno), en los puntos más accesibles al operador en las siguientes

ubicaciones:

 - En las puertas de salida de las vías de escape (área de electrolisis).

 - Salidas en otras salas del edificio de procesos.

 Área de almacenamiento de hidrógeno.

 - Compresores de alta presión.

Las ubicaciones de estos se han considerado que la distancia de viaje al más cercano sea una

distancia razonable a no más de 50 m según lo recomendado por NFPA 2. Su ubicación e

6

instalación se realizará a no más de 1,5 m de las puertas, y a una altura desde el piso entre 1,07 m

y 1,22 m de acuerdo con la normativa NFPA 72.

**4** **SISTEMA DE PARADA DE EMERGENCIA (ESD)**

Sistema de Parada de Emergencia (ESD) está basado en criterios de falla segura, el cual cumple

con las funciones de aseguramiento del proceso, aislamiento del proceso, parada de equipos,

prevención de perdida de inventario, salvaguarda de las personas y protección del medio ambiente,

mayormente cuando se generan fugas de hidrógeno. El mismo considera una lógica de

enclavamientos, el cual recibe las señales cableadas en desde los instrumentos instalados en

campo hasta el PLC de seguridad (con certificación SIL) el cual enviará automáticamente las

señales de respuesta a los elementos de acción final a fin de mantener los parámetros establecidos

para la seguridad del proceso y la planta. La instrumentación asociada al ESD deberá dar

cumplimiento además al estándar IEC 61508/61511.

El sistema de parada de emergencia llevará a condición segura la planta, a través de la ejecución

de las siguientes medidas:

 - Deteniendo los equipos de producción y compresión de hidrogeno

 - Aislando el almacenamiento de hidrógeno, venteando a la atmósfera el contenido de hidrógeno

en líneas (a través del sistema de despresurización o blowdown)

 - Barrido automático de nitrógeno a las líneas despresurizadas.

El ESD es generado mediante dos caminos:

 - Acción humana mediante un botón manual. (Pulsador manual o botón propio de la planta)

 - Detención de emergencia pre-programada. En este caso el ESD es activado automáticamente

por la alarma en los sensores de fuego y gas según una lógica de votación.

7