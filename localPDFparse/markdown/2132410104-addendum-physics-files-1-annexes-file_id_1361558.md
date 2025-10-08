---
title: INFORME
author: MS
date: D:20160621172040-04'00'
language: es
type: manual
pages: 6
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MANUAL DE OPERACIÓN BASICO Cliente: ESSBIO S.A. Proyecto: “Diseño de Ingeniería de Detalles Aumento de Capacidad PTAS Santa Cruz, Región de O ́Higgins”
-->

**MS343-0IN-003A**

**Rev. 0**
Pág. 1/6

Originador: HTS

# MANUAL DE OPERACIÓN BASICO Cliente: ESSBIO S.A. Proyecto: “Diseño de Ingeniería de Detalles Aumento de Capacidad PTAS Santa Cruz, Región de O ́Higgins”

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
|0|HTS|HTS|BMS|PARA CONSTRUCCION|
|**Rev.**|**POR**|**REVISÓ**|**APROBÓ**|**Notas**|

Anibal Pinto 817

Piso 4
Concepción

Fono: 041-2246979
Email: contacto@millanyseguel.cl

www.millanyseguel.cl

**MS343-0IN-003A**

**Rev. 0**
Pág. 2/6

**TABLA DE CONTENIDO**

1. GENERAL. ........................................................................................................... 3

2. OPERACIONES DE LA PTAS.............................................................................. 3

2.1. TRATAMIENTO PRIMARIO ................................................................................. 3

2.2. TRATAMIENTO SECUNDARIO........................................................................... 4

2.3. SISTEMA DE CLORACION.................................................................................. 5

2.4. DESHIDRATADO DE LODOS.............................................................................. 5

2.5. CAMARA DE CONTACTO ................................................................................... 6

Anibal Pinto 817

Piso 4
Concepción

Fono: 041-2246979
Email: contacto@millanyseguel.cl

www.millanyseguel.cl

**MS343-0IN-003A**

**Rev. 0**
Pág. 3/6

**1. GENERAL.**

El presente manual de operación básico tiene por objetivo describir la operación habitual

de la planta en términos generales. La operación específica de cada equipo

corresponde a su respectivo manual de operación o a información proporcionada por el

proveedor..

**2. OPERACIONES DE LA PTAS**

**2.1. TRATAMIENTO PRIMARIO**

Los afluentes de las dos PEAS deben estar siempre alineados al canal de entrada de la

PTAS. Desde la PTAS no se controla nada al respecto. En los despliegues de

información en el PLC de la planta aparecen los estatus de las bombas de las PEAS,

pero con indicación de falla de comunicación.

La reja automática RAF-001 debe estar siempre en automático, sin compuertas que

interfieran el flujo hacia ella. Se debe asegurar la disponibilidad de agua para el

compactador TOR-001 y que el contenedor de residuos esté con capacidad suficiente.

Con motivo del aumento de capacidad, tanto el tornillo TOR-001 como el desarenador

SEP-001 tiene suministro normal con agua de servicio, desde los nuevos filtros

floculadotes.

En canal paralelo, y sin compuertas que interfieran el flujo, debe estar disponible y

limpia la reja manual RMG-001, que solo actúa en caso de falla de la reja automática, o

bien por que por motivos de mantención ha sido dejada fuera de servicio, y su flujo ha

sido desviado con una compuerta.

El desarenador SEP-001 debe operar en forma automática, asegurando el suministro de

aire desde los sopladores, y de agua de servicio.

De la misma forma, el lavador de arena debe estar en automático, asegurando que el

contenedor de arenas tenga capacidad de recepción.

Anibal Pinto 817

Piso 4
Concepción

Fono: 041-2246979
Email: contacto@millanyseguel.cl

www.millanyseguel.cl

**MS343-0IN-003A**

**Rev. 0**
Pág. 4/6

Se debe verificar la disponibilidad de medidor de flujo FI-01, puesto que su correcta

medición aporta como señal al cálculo del aire que deben suministrar los sopladores, y

también forma parte de las mediciones que deben quedar en registro.

**2.2. TRATAMIENTO SECUNDARIO**

El reactor debe ser vigilado permanentemente, en orden a mantener en buen estado las

cadenas de difusores que se encuentran ancladas desde el manifold de aire por un

lado, y de muertos de concreto por el otro. Visualmente se puede verificar el movimiento

de las mangueras, y puntos de afloramiento anormal de aire, lo que puede dar lugar a

retirar y revisar el estado del sistema de difusores.

Los sopladores deben estar en automático, donde para asegurar que el control opere en

forma eficiente y efectiva, se debe vigilar el buen funcionamiento del medidor de

oxígeno disuelto AI-01 y de la medición de flujo afluente FI-01. El operador debe revisar

semanalmente los odómetros de los motores de los sopladores, para ir alternando el

uso de cada uno, de forma tal que el conteo de horas asegure el desgaste homogéneo.

Los dos sedimentadores SED-001 y SED-002 deben operar en paralelo, asegurando

que sus respectivas compuertas en la salida del reactor VCM-007 y VCM-008 estén

correctamente abiertas, y así el flujo se divida en forma igualitaria a cada sedimentador.

Los puentes barredores BAR-001 y BAR-002 deben estar siempre en servicio,

aportando espumas al pozo de espumas, donde la bomba BBA-003 debe estar siempre

en automático, operando en una banda de alto y bajo nivel.

Las bombas de recirculación BBA-004, BBA-005 y BBA-006 deben estar en automático,

con control de flujo con set point de tasa de recirculación. Este parámetro debe ser

ingresado por el operador, en un rango normal de 50% a 150%, siendo lo normal un

valor de 100%, con respecto al flujo de afluente FI-01.

El operador debe revisar semanalmente los odómetros de los motores, para ir

alternando el uso de cada uno, de forma tal que el conteo de horas asegure el desgaste

homogéneo.

Anibal Pinto 817

Piso 4
Concepción

Fono: 041-2246979
Email: contacto@millanyseguel.cl

www.millanyseguel.cl

**MS343-0IN-003A**

**Rev. 0**
Pág. 5/6

**2.3. SISTEMA DE CLORACION**

El sistema de cloración debe estar siempre en servicio, y es absolutamente simétrico,

en configuración 1+1.

Para asegurar esto, se debe verificar la disponibilidad de agua potable y de la bomba

Booster que eleva la presión a los inyectores.

En el HMI se encontrará disponible la abertura de dosificación de cloro y falla del

sistema.

El controlador de cloración, que es un equipo autónomo diseñado para la aplicación,

debe tener la medición de flujo del FI-04 y de la medición de cloro residual AI-02. Con

estos argumentos, mas el set point de cloro residual que debe ingresar el operador, se

genera la señal de cantidad de cloro a agregar en el equipo dosificador Siemens V-10K.

El rango normal de cloración debería ser entre 5 y 10 ppm, mientras que el cloro

residual debería estar en el rango de 1 a 5 ppm.

El operador debe vigilar diariamente el inventario de cloro, revisando los sensores de

peso WI-01 y WI-02, con especial cuidado en que un cilindro debe estar lleno (recién

repuesto) y el otro en servicio. Se sugiere incorporar un indicador que permita proyectar

cuanto tiempo queda de suministro del cilindro en servicio, a la tasa promedio diaria de

flujo del FI-04.

El proyecto introduce una nueva bomba, la BBA-007. Su función es generar un

flujo de muestreo para el medidor de cloro residual. Esta medición es

permanente, por lo que dicha bomba debe estar siempre en servicio, sin

modificaciones en su condición de operación.

**2.4. DESHIDRATADO DE LODOS**

La línea de lodos no se modifica respecto a sus equipos que la componen.

Sin embargo, dado que en el nuevo escenario el sistema de impulsión WAS es nuevo e

independiente del RAS, existirá una presión significativamente mayor disponible para

Anibal Pinto 817

Piso 4
Concepción

Fono: 041-2246979
Email: contacto@millanyseguel.cl

www.millanyseguel.cl

**MS343-0IN-003A**

**Rev. 0**
Pág. 6/6

operar, lo que se traduce en que se podrá modular con precisión el flujo de lodos

mediante ajuste manual de la válvula bajo el mezclador.

Por otro lado, se espera que la densidad del lodo aumente notablemente, por lo que se

deberán realizar mediciones que permitan realizar un ajuste en la dosificación de

polímero.

**2.5. CAMARA DE CONTACTO**

La cámara de contacto es de doble paso, simétrica. Su diseño responde a atender los

tiempos de residencia hidráulica en condiciones de previsión, por lo que no corresponde

realizar ajustes a su operación. Notar que siempre debe operar con los dos canales en

servicio.

Anibal Pinto 817

Piso 4
Concepción

Fono: 041-2246979
Email: contacto@millanyseguel.cl

www.millanyseguel.cl