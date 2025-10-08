---
title: Microsoft Word - Anexo 12.8. Manual Operacion RecVoil V0.docx
author: Desconocido
date: D:20200623021000Z00'00'
language: es
type: manual
pages: 23
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PLANTA DE VALORIZACION DE ACEITES
-->

## ADENDA DECLARACIÓN DE IMPACTO AMBIENTAL
### Proyecto “Planta de Recuperación y Valorización de Aceites Usados”

#### Anexo No 12.8. Manual de Operación RecVoil Recuperación y Valorización de Aceites S.A. Junio 2020

# PLANTA DE VALORIZACION DE ACEITES

## MANUAL DE OPERACIÓN Y MANTENIMIENTO

### 2020

© Derechos Reservados 2019

Dirección de proyectos
Departamento de ingeniería y desarrollo.
Cali, Valle del Cauca, Colombia Tel:3126805138

La reproducción total o parcial de este documento podrá efectuarse mediante la autorización
expresa de la Dirección general del departamento de proyectos TERMACOL SAS dándole el crédito
correspondiente.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

#### C ONTENIDO

ADVERTENCIAS DE SEGURIDAD .......................................................................................................................... 4

RESUMEN DEL SISTEMA ...................................................................................................................................... 6

COMPONENTES PRINCIPALES ......................................................................................................................... 7

Evaporador 1 ............................................................................................................................................... 7

Evaporador 2 ............................................................................................................................................... 7

Intercambiador de calor HE1 ...................................................................................................................... 7

Intercambiador de calor HE2 ...................................................................................................................... 7

Intercambiador de calor HE3 ...................................................................................................................... 8

Intercambiador de calor HE4 ...................................................................................................................... 8

Torre de enfriamiento ................................................................................................................................ 8

Caldera para aceite térmico ........................................................................................................................ 8

Torre de vacío ............................................................................................................................................. 8

Compresor .................................................................................................................................................. 8

LISTADO DE EQUIPOS Y UBICACIÓN ............................................................................................................... 9

SISTEMA ELÉCTRICO E INSTRUMENTACIÓN ................................................................................................. 10

Operación del Sistema .............................................................................................................................. 11

Evaporador 1 ............................................................................................................................................. 11

Evaporador 2 ............................................................................................................................................. 12

Evaporador de Pelicula (TWEF) ................................................................................................................. 12

Torre de Vacio ........................................................................................................................................... 13

Depurador de Gases (SCRUBBER) ............................................................................................................. 13

Tanques De Recoleccion ........................................................................................................................... 14

Tablero de control general ....................................................................................................................... 14

Conexión eléctrica .................................................................................................................................... 15

OPERACIÓN DEL EQUIPO .................................................................................................................................. 16

ENCENDIDO Y APAGADO .............................................................................................................................. 16

FALLAS Y ALARMAS ....................................................................................................................................... 19

GUÍA DE MANTENIMIENTO .............................................................................................................................. 21

PLAN DE VERIFICACION .................................................................................................................................... 21

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

#### ADVERTENCIAS DE SEGURIDAD

**NOTA:**

Esta sección se ocupa de las advertencias de seguridad generales aplicables a la unidad. La seguridad es
primordial y es la última responsabilidad del usuario final. Es su responsabilidad de entender los códigos y
requerimientos de la planta cuando se realiza la instalación y uso. Siga los códigos y reglamentos locales y
nacionales apropiadas.

ALTA TEMPERATURA

 - Temperaturas superiores a 260 °C dentro de los evaporadores y TWEF, requieren atencion
prioritaria por parte del personal operativo.

 - Temperaturas superiores a 300 °C en las tuberias de aceite termico y boiler, requieren atencion
prioritaria por parte del personal operativo.

 - El cuidado se debe tener cuidado de no tocar las superficies calientes.

ALTA PRESIÓN

 - Presión positiva superior a 3 psig en el evaporador 1, requiere atencion prioritaria por parte del
personal operativo.

 - Asegurarse que las válvulas de alivio de seguridad están orientadas correctamente.

 - Llevar lentes de seguridad.

RUIDO

 - Niveles de ruido por encima de 68 dB, requieren atencion prioritaria por parte del personal de

mantenimiento.

 - Debe usarse protección auditiva.

RIESGO DE CAÍDA

 - A la PVAU se accede mediante una plataforma elevada. Se debe tener cuidado con el equilibrio.

 - Una escalera se usa para acceder a los equipos. Se debe tener cuidado al usar esta escalera.

RIESGO DE DESCARGA ELÉCTRICA

 - Existe alto voltaje dentro de los componentes dentro del panel de control.

 - Sistema de alimentación cuando se requieren trabajos de mantenimiento eléctrico o cheques.

LUCES INDICADORAS

 - Estar al tanto de lo que indica el estado de alarma de luz o mensajes.

 - La unidad debe ser operado solamente por personal que haya recibido entrenamiento y esté
perfectamente enterado de los procedimientos de operación tal como se establece en este manual.

PRECAUCIONES GENERALES Y DIRECTRICES AL USAR ESTE EQUIPO

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

- La unidad sólo puede ser operada por personal calificado y que usan equipo de protección personal
(EPP).

- Tenga en cuenta todas las advertencias sobre los equipos eléctricos.

- Cuando sea necesario, eliminar cualquier obstrucción en la entrada de aire para permitir el flujo. No
cubrir las rejillas de ventilación.

- Nunca debe introducir el enchufe en una toma de corriente sin un contacto a tierra de protección.
La protección de tierra no debe verse comprometida mediante el uso de un cable de extensión sin

una tierra.

- Durante la operación, configuración y reparación del equipo de adsorción, se debe evitar aplicar
voltajes externos (ej.: soldadura) en este caso, si el acceso es absolutamente necesario en estas
condiciones, entonces el trabajo sólo debe ser realizada por personal adecuadamente calificado
que sean plenamente conscientes de los peligros presentes. Sin embargo, se recomienda que la
unidad de PLC debe ser apagada y desenchufada antes de realizar cualquier procedimiento de

mantenimiento.

- Al reemplazar fusibles defectuosos hay que asegurar que los reemplazos son el tipo y clasificación
correcta. El uso de fusibles temporales / indebidos y / o cortocircuitos en los portafusibles son
peligrosos tanto para el instrumento / máquina y el usuario final. Esto debe ser estrictamente

evitado.

- En caso de sospecha de daño, la unidad siempre debe ser retirada de uso y cortar paso de

corriente.

- Llame al servicio técnico en caso de sospecha de daños en el equipo.

- La limpieza de elementos electrónicos y de instrumentación debe realizarse con un paño sin pelusa,
utilizando un limpiador adecuado, evitando limpiadores cáusticos y disolventes.

- Asegúrese siempre de que el cable de alimentación no tenga sus conductores dañados o expuestos.

- Un cable dañado podría resultar en comprometer la seguridad del usuario.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

#### RESUMEN DEL SISTEMA

El aceite lubricante usado o residual se genera en la industria en su mayoría debido a que se usa en motores
y equipos de combustión interna. Estos aceites tienen un tiempo de uso determinado, una vez terminado
dicho tiempo debe sustituirse en su totalidad. El aceite lubricante se convierte en no apto para uso por dos
razones principales, la primera es debido a una acumulación de contaminantes y la segunda es debido a
cambios químicos en el mismo, los principales contaminantes en los aceites son los productos de
combustión, abrasivos, productos de oxidación y remanentes de aditivos agotados.

El proceso de valorización y aprovechamiento del aceite lubricante usado esencialmente incluye remover
todos estos contaminantes y restaurar la base lubricante a una condición inicial de materia prima, que
permita recuperar la base lubricante como materia prima para la elaboración de nuevos aceites lubricantes.
El diagrama de equipos, líneas e instrumentación es el presentado en la Figura 1.

**FIGURA 1. P&ID PLANTA DE VALORIZACIÓN DE ACEITE LUBRICANTE USADO.**

La valorización y recuperación de los aceites lubricantes usados se realiza mediante tecnologías de
destilación a presiones de vacío, este sistema se compone principalmente de tres equipos (Evaporador 1,
Evaporador 2 y un evaporador de película por barrido de trayecto corto o _TWEF_ por sus siglas en inglés).
Este equipo es modular y se soporta en skids (Módulos estructurales que contienen todos los elementos
mecánicos, hidráulicos y eléctricos, necesarios para el funcionamiento de todo el sistema) construidos
principalmente en tubo cuadrado de dimensiones 150 mm X 150 mm y espesor de 10 mm, con plataformas
en malla galvanizada antideslizante T-125, iluminación con lámparas anti-explosión, al igual que todos los
equipos eléctricos que componen el sistema.

La planta de valorización de aceite lubricante usado funciona en dos fases principales distintas, la fase de
separación a presión atmosférica y la fase de separación a presión de vacío.

 - Fase de separación a presión atmosférica: Consiste en separar (mediante evaporación) del aceite
lubricante usado trazas de humedad (que no deberá ser mayor a un 5% del volumen total del aceite
lubricante usado ingresado al proceso) y componentes nafténicos o disolvente denominado nafta.
En esta fase se emplea el Evaporador 1 y el intercambiador de calor HE1, se eleva la temperatura
del aceite alrededor de 250 °C y se recircula a presión atmosférica durante determinado tiempo

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

garantizando una evaporación de los componentes mencionados anteriormente. Los componentes
separados con condensados posteriormente en los intercambiadores de calor HE2 y HE3, mientras
que lo que queda de aceite lubricante usado pasa a la siguiente fase del proceso.

 - Fase de separación a presión de vacío: Después de haber separado agua y nafta del aceite
lubricante usado, este último ingresa al Evaporador 2, allí se somete a presión de vacío (-14 psig
aproximadamente), y se eleva su temperatura alrededor de los 260 °C, bajo estas condiciones es
posible evaporar el gasoil, el cual se separa y se condensa posteriormente mediante el uso del
intercambiador de calor HE4. El aceite lubricante usado que ya no tiene agua, nafta ni gasoil se
transporta hasta el TWEF, en donde finalmente se separa la base lubricante, esta se evapora en las
paredes calientes por medio de la chaqueta calefactora de este último equipo, la base lubricante se
obliga a pasar por un intercambiador de calor que se encuentra dentro del mismo TWEF para que
sea condensado finalmente; el remanente de suciedades (fondo) con materiales pesados cae por
gravedad a un compartimiento distinto dentro del TWEF y se almacena para su disposición.

##### COMPONENTES PRINCIPALES

E VAPORADOR 1

Este equipo consiste en un tanque para trabajo a presión atmosférica donde se recircula aceite lubricante
usado y se eleva su temperatura alrededor de los 250° C, a esta temperatura se evaporan el agua y la nafta o
disolvente nafténico que contenía el aceite usado, estos componentes son separados debido a su cambio de
fase y se transportan hacia los condensadores HE2 y HE3 de la Figura 1. El medio de intercambio de calor
para elevar la temperatura del aceite usado en este equipo es el intercambiador de calor HE1, que permite

la mencionada recirculación de la sustancia.

E VAPORADOR 2

Cuando es retirada el agua y la nafta, el aceite lubricante usado pasa a este equipo, donde se somete a una
presión de vacío de -14 psig aproximadamente a una temperatura de 260 °C, en esta etapa se extrae del
aceite lubricante mediante evaporación el gasoil, este componente es posteriormente transportado al

condensador HE4.

TWEF

El equipo de evaporación de película por barrido en trayecto corto opera a una presión aproximada de -14
psig, compuesto por una chaqueta calentada a 260°C, que permite la evaporación de la base lubricante
mediante la película fina que se reparte homogéneamente alrededor de la superficie interna del equipo. La
base lubricante en estado gaseoso se hace pasar a través de un intercambiador de calor, ubicado
internamente en el TWEF, donde se condensa y se almacena en un tanque de recepción posterior.

I NTERCAMBIADOR DE CALOR HE1

Intercambiador de calor que usa como sustancia de calentamiento aceite térmico (proveniente de la caldera
para aceite térmico), permite elevar la temperatura del aceite lubricante usado en la primera etapa del

proceso.

I NTERCAMBIADOR DE CALOR HE2

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

Intercambiador de calor que usa como sustancia de enfriamiento agua, permite disminuir la temperatura en
una primera instancia de los gases separados en la primera etapa (vapor de agua y nafta).

I NTERCAMBIADOR DE CALOR HE3

Intercambiador de calor que usa como sustancia de enfriamiento agua, permite disminuir la temperatura en
segunda instancia de los gases separados en la primera etapa, permitiendo su transformación a fase líquida
(vapor de agua y nafta).

I NTERCAMBIADOR DE CALOR HE4

Intercambiador de calor que usa como sustancia de enfriamiento agua, permite disminuir la temperatura del
gasoil en estado gaseoso para su transformación a fase líquida.

T ORRE DE ENFRIAMIENTO

Equipo de transferencia de calor con el ambiente, permite disminuir la temperatura del agua empleada en

los intercambiadores de calor.

C ALDERA PARA ACEITE TÉRMICO

Equipo de transferencia de calor, que opera por medio de la combustión de combustible gaseoso, sirve
como medio de calentamiento para elevar la temperatura del aceite térmico empleado en el proceso.

T ORRE DE VACÍO

Consiste en tres equipos reforzadores de vacío, permiten alcanzar la presión necesaria para operar el
Evaporador 2 y el TWEF.

C OMPRESOR

Equipo neumático de aire comprimido a alta presión, empleado para la activación de elementos de control

del sistema.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

##### LISTADO DE EQUIPOS Y UBICACIÓN

**TABLA 1. LISTADO DE QUIPOS PLANTA DE VALORIZACIÓN DE ACEITE LUBRICANTE USADO.**

|SISTEMA|EQUIPO|CANT|
|---|---|---|
|1. EVAPORADOR 1|1. EVAPORADOR|1|
|1. EVAPORADOR 1|1.1. BOMBA ALIMENTACIÓN EVAPORADOR 1 VIKING|1|
|1. EVAPORADOR 1|1.1. BOMBA ALIMENTACIÓN EVAPORADOR 1 VIKING**BACK UP**|1|
|1. EVAPORADOR 1|1.2. BOMBA PRINCIPAL EVAPORADOR 1 KSB|1|
|1. EVAPORADOR 1|1.2. BOMBA PRINCIPAL EVAPORADOR 1 KSB**BACK UP**|1|
|1. EVAPORADOR 1|1.3. INTERCAMBIADOR EVAPORADOR 1|1|
|1. EVAPORADOR 1|1.3. INTERCAMBIADOR EVAPORADOR 1**BACK UP**|1|
|1. EVAPORADOR 1|1.4. COLUMNA EMPACADA SOBRE EVAPORADOR 1|1|
|1. EVAPORADOR 1|1.5. INTERCAMBIADOR DE CALOR DE NAFTA 1|1|
|1. EVAPORADOR 1|1.6. INTERCAMBIADOR DE CALOR DE NAFTA 2|1|
|1. EVAPORADOR 1|1.7. DECANTER NAFTA Y AGUA|1|
|2. EVAPORADOR 2|2. EVAPORADOR 2|1|
|2. EVAPORADOR 2|2.1. COLUMNA EMPACADA SOBRE EVAPORADOR 2|1|
|2. EVAPORADOR 2|2.2. INTERCAMBIADOR DE CALOR GAS OIL|1|
|2. EVAPORADOR 2|2.3. TANQUE GAS OIL|1|
|2. EVAPORADOR 2|2.4. BOMBA GAS OIL VIKING|1|
|3. TWFE|5. TWFE|1|
|3. TWFE|3.1. REDUCTOR TWFE|1|
|3. TWFE|3.2. TANQUE PLO|1|
|3. TWFE|3.3. BOMBA PLO VIKING|1|
|3. TWFE|3.3 BOMBA PLO VIKING**BACK UP**|1|
|3. TWFE|3.4. TANQUE FONDO|1|
|3. TWFE|3.5. BOMBA FONDO VIKING|1|
|3. TWFE|3.5. BOMBA FONDO VIKING**BACK UP**||
|4. TORRE DE VACIO|4.1. BOMBA DE VACIO TRAVAINI|1|
|4. TORRE DE VACIO|4.1. BOMBA DE VACIO TRAVAINI**BACK UP**|1|
|4. TORRE DE VACIO|4.2. BOMBA DE VACIO BOOSTER 2000|1|
|4. TORRE DE VACIO|4.2. BOMBA DE VACIO BOOSTER 2000**BACK UP**|1|
|4. TORRE DE VACIO|4.3. BOMBA DE VACIO BOOSTER 540|1|
|4. TORRE DE VACIO|4.3. BOMBA DE VACIO BOOSTER 540**BACK UP**|1|
|5. SCRUBBER|5. SCRUBBER|1|
|5. SCRUBBER|5.1. BOMBA RECIRCULACION SCRUBBER|1|
|6. CALDERAS ACEITE TÉRMICO|6.1. BOILER THERMOPAC|1|
|6. CALDERAS ACEITE TÉRMICO|6.1. BOILER THERMOPAC**BACK UP**|1|
|6. CALDERAS ACEITE TÉRMICO|6.2. MOTOR BLOWER BOILER|1|
|6. CALDERAS ACEITE TÉRMICO|6.2. MOTOR BLOWER BOILER**BACK UP**|1|
|6. CALDERAS ACEITE TÉRMICO|6.3. LÍNEA DE GAS NATURAL|1|
|6. CALDERAS ACEITE TÉRMICO|6.4. BOMBA ACEITE TÉRMICO SIHI|1|
|6. CALDERAS ACEITE TÉRMICO|6.4. BOMBA ACEITE TÉRMICO SIHI** BACK UP**|1|
|10. TORRE DE ENFRIAMIENTO|TORRE DE ENFRIAMIENTO ADVANCE PVT LTD|1|
|10. TORRE DE ENFRIAMIENTO|MOTOR TORRE DE ENFRIAMIENTO|1|
|11. COMPRESOR DE AIRE|COMPRESOR DE TORNILLO|1|
|11. COMPRESOR DE AIRE|COMPRESOR DE TORNILLO**BACK UP**|1|
|13. SISTEMA DE CONTROL|TABLERO DE CONTROL DE PROCESOS CON|-|
|13. SISTEMA DE CONTROL|VISUALIZACIÓN HMI Y REMOTA|VISUALIZACIÓN HMI Y REMOTA|

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

##### SISTEMA ELÉCTRICO E INSTRUMENTACIÓN

El sistema eléctrico está diseñado para controlar cada una de las variables de forma segura, permitiendo el
ajuste de estas en cada etapa del proceso; para ello se integra un autómata programable (PLC) con un
sistema Scada, en el primero, se agrupan todas las entradas de campo, las cuales son analizadas y tratadas
según la lógica desarrollada, luego se generan señales de salida para controlar cada elemento de forma
independiente.
La operación se lleva acabo de manera automática durante todo el proceso, aunque de ser necesario es
posible cambiar a modo manual, para actividades de revisión y mantenimiento.
Se cuenta con un sistema de registro tanto de las variables de proceso como de los eventos de falla que se
puedan presentar en el sistema, facilitando la identificación de estos por medio de mensajes en pantalla y

una alarma sonora.

Para un mejor entendimiento se ha separado el sistema en zonas con los elementos que las componen:

 - BOILER - (CALDERA)

 - EVAPORADOR 1

 - EVAPORADOR 2

 - EVAPORADOR DE PELÍCULA - (TWFE)

 - TORRE DE VACIO

 - DEPURADOR DE GASES - (SCRUBBER)

**FIGURA 2. HMI EQUIPO DE PVAU.**

A continuacion se detallan las condiciones de operación del sistema, los enclavamientos de seguridad y
control del proceso; también se dan las indicaciones de como operar el sistema Scada para supervisión y
manejo de las variables.
Se incluye una descripción de los componentes y su secuencia de operación tanto para el inicio como para la
finalización del proceso.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

##### O PERACIÓN DEL S ISTEMA

CALDERA - (BOILER)

**FIGURA 11. HMI EQUIPO DE PVAU.**

Cuenta con un tablero de control independiente, en el cual se interconectan las señales de encendido,
confirmación y falla al PLC, para ser visualizadas en el Scada.
Para encenderla se debe presionar en el botón ON con esto iniciará la secuencia de arranque del quemador.
Para apagar presione el botón OFF, detendrá la combustión y el proceso de calentamiento.
Se podrán visualizar las temperaturas y señales de confirmación de encendido o falla mediante animaciones
gráficas.

E VAPORADOR 1

Este sistema está compuesto por los siguientes elementos, Bomba de Alimentación Principal,
Intercambiador de Calor, tanque de expansión, bomba de recirculación y condensador.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

En esta sección se puede editar la consigna de temperatura a la que operará el Flash Tank, para hacerlo haga
clic en el recuadro blanco y escriba el valor deseado, luego oprima enter.
Se puede observar la animación de los niveles, el estado de las bombas y los porcentajes de apertura de las
válvulas proporcionales.

E VAPORADOR 2

Esta etapa la componen: el evaporador, el condensador y tanque de almacenamiento de Gasoil.
Se puede editar la consigna de temperatura del evaporador desde pantalla, para hacerlo de clic en el
recuadro blanco, escriba el valor deseado y presione enter.
Se puede observar las animaciones de nivel, valores de temperatura y porcentajes de apertura de las
válvulas proporcionales.

E VAPORADOR DE P ELICULA (TWEF)

Compuesto por: Evaporador TWFE y tanques de almacenamiento de Residuo y PLO
La velocidad del TWFE es regula por un inversor de frecuencia controlado por el PLC, es posible editarla,
para hacerlo haga clic en el recuadro amarillo, escriba el valor deseado en Hz y presione enter.
Se puede también regular la tasa de alimentación al TWFE, para hacerlo, de clic en el recuadro blanco,
escriba un valor entre 0 y 100% y presione enter.
En pantalla se pueden observar las variables de temperatura, presión de vacío, porcentaje de apertura de
válvulas, velocidad de giro y presión de agua de enfriamiento.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

T ORRE DE V ACIO

Este sistema está compuesto por una bomba de vacío principal y dos auxiliares (Booster), las cuales ayudan
a mantener una presión negativa en los tanques, también se encuentra, un intercambiador para
refrigeración.
Se puede editar la velocidad de las bombas, para hacerlo de clic en el recuadro amarillo, escriba un valor
entre 0 y 60 Hz, luego presione enter.

D EPURADOR DE G ASES (SCRUBBER)

Aquí se encuentra: Tanque scrubber, boquillas de aspersión y bomba de recirculación.
En este sistema no se tienen parámetros editables, solo se visualizan las variables de temperatura, nivel de
agua y estado de las bombas.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

T ANQUES D E R ECOLECCION

Son cada uno de tanques que se utilizan para recolectar los subproductos derivados del proceso, tales como:
Agua-Nafta, Gasoil, PLO, Residuo.
El parámetro que se edita en esta zona es la consigna de temperatura del residuo, para hacerlo de clic en el
recuadro blanco, escriba el valor deseado y presione enter.
También, se pueden visualizar las variables de temperatura, niveles y porcentaje de apertura de las válvulas
proporcionales.

T ABLERO DE CONTROL GENERAL

C OMPONENTES EXTERNOS

**FIGURA 3. TABLERO DE CONTROL GENERAL EQUIPO DE ADSORCIÓN ADS-40.**

1. Monitor de fases, vigila los niveles de tensión de la acometida principal trifásica.
2. Panel HMI, interfaz visual para la operación del equipo.
3. Panel de encendido, se ubica el selector de encendido general, la parada de emergencia y pilotos

indicadores.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

C OMPONENTES INTERNOS

**FIGURA 4. COMPONENETES INTERNOS DE LTABLERO DE CONTROL GENERAL.**

1. Interruptor automático principal, totalizador.
2. Barraje trifásico.
3. Interruptores automáticos control.

4. Transformador de control.

5. Interruptores automáticos fuerza.

6. Contactores resistencias.

7. Guardamotores.

8. Variador de frecuencia soplador para vacío.

9. Variador de frecuencia Bomba.

10. Módulos de expansión PLC.

11. Borneras entradas 24VDC.

12. Borneras portafusibles salidas 110 VAC.
13. Regulador de tensión.

C ONEXIÓN ELÉCTRICA

Este equipo está diseñado para ser conectado a 440 V, 60 Hz, 3 fases, 4 hilos, fuente de alimentación de 100
amperios.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

#### OPERACIÓN DEL EQUIPO

##### ENCENDIDO Y APAGADO

Para energizar el sistema realice la siguiente secuencia:

1. Verificar que los tanques de Aceite Lubricante Usado, que van a hacer usados, estén llenos.
2. Drenar el agua de los tanques.
3. Verificar que las válvulas de salida están completamente abiertas.
4. Verificar que los filtros de cubo y los filtros magnéticos estén limpios.
5. Verificar que el nivel de agua en la Cuenca de la torre de enfriamiento está por arriba del nivel mínimo.
6. Verificar que la válvula de entrada de agua de la torre de enfriamiento está totalmente abierta.
7. Verificar que las válvulas del circuito de enfriamiento en el circuito principal están abiertas.
8. Inicie la bomba de agua de enfriamiento.

9. Iniciar ventilador de torre de enfriamiento.

10. Verificar que el nivel del fluido térmico en el tanque de expansión está por encima del mínimo.
11. Depure aproximadamente dos (2) Kg de nitrógeno en el tanque de expansión.
12. Verificar que todas las válvulas en el circuito del fluido térmico están abiertas.

13. Inicie la bomba de fluido térmico.

14. Inicialmente, verificar que la presión de salida y entrada de la bomba están en 5 y 2 Bar

respectivamente.
15. Permita que el fluido térmico circule por aproximadamente veinte (20) minutes.
16. Inicie el quemador.
17. Ajuste los puntos de referencia / _SET POINTS/_ de la salida y los controladores de retorno de temperatura

como lo requiera el proceso.
18. Verificar que las válvulas en el circuito de aire comprimido están abiertas.
19. Inicie el compresor y mantenga la presión.
20. Verificar que los discos de la bomba de vacío se mueven libremente rotando en forma manual la correa.

Evite usar el botón pulsador para este propósito.
21. Inicie la bomba de alimentación de ALU (Aceite Lubricante Usado) y Verificar que el nivel del primer

flash tank se mantiene apropiadamente.
22. Inicia el panel de control PLC principal en modo auto. La secuencia de operaciones lógica es como sigue:

1. Bomba Flash No.1...

2. Inicia bomba de alimentación de nivel bajo de bomba flash
3. Inicia bomba de bajo nivel de bomba flash
4. Después de segundos el interruptor de presión detecta la presión y si la presión no aumenta, la

bomba se detiene...

5. Bomba de alimentación de alto nivel de tanque flash 1 se detiene

6. Bomba flash No. 2 inicia.

7. Bomba flash en nivel bajo de tanque flash 2 se detiene.
8. Inicia bomba flash nivel bien en flash tank 2...

9. Después de segundos el interruptor de presión detecta la presión y si la presión no aumenta, la

bomba flash 2 se detiene...

10. Cuando el nivel del diésel sube en el tanque flash No. 2, el controlador proporcional de tipo

flotador opera la válvula de control, el aceite diésel pasa a través del enfriador de diésel y va
hacia el tanque de almacenamiento...
11. Cuando el nivel en el tanque flash No. 2 alcance el alto nivel, la bomba de alimentación de ALU

y la bomba flash se detienen...

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

12. Cuando el nivel en el tanque flash No. 1 cae, la bomba de alimentación inicia. El controlador de

nivel neumático controla la válvula proporcionalmente dependiendo del nivel...
13. Si el interruptor proporcional de nivel falla, el interruptor de nivel alto entra en acción y apaga

la bomba de alimentación de ALU...

14. El flujo de aceite es monitoreado por el flujómetro...
15. La bomba caustica inicia cinco (5) segundos después que la bomba de alimentación inicia.
16. La válvula de control neumática en la línea de entrada del fluido térmico de IC1 /HE1/ (fluido

térmico al intercambiador de calor de ALU) abre y el calentamiento se lleva a cabo
proporcionalmente por la temperatura establecida.
17. La válvula neumática del El IC2 (fluido térmico al intercambiador de calor de aceite diésel)

también abre y el calentamiento se lleva a cabo proporcionalmente por la temperatura

establecida.

18. Si la presión aumenta en el tanque flash N0.1, el interruptor de presión apaga la planta...
19. El sensor de temperatura en la columna No.1 indica temperatura de vapor.
20. El interruptor de presión diferencial instalado en la columna No.1 es un seguro contra los

nudos en la columna. Si en la columna se hacen nudos, el interruptor de presión diferencial
apaga la planta...
21. El interruptor de presión diferencial en la columna No.2 sirve para el mismo propósito que el

interruptor de la columna No.1...
22. El sensor de temperatura en la columna No.3 brinda indicación de temperatura de vapor e

inicia el reflujo del diésel proporcionalmente para mantener la temperatura en la columna 1...
23. El sensor de temperatura de la salida del sub-enfriador asegura que la temperatura no exceda

60oC...

24. El receptor separa nafta y agua por diferencia de densidad...
25. La válvula de control en el tanque flash No.1 abre cuando la temperatura alcanza el punto

establecido y lleva el aceite al evaporador con la bobina calentadora interna...
26. El aceite ligero se evapora en el evaporador y es condensado en un condensador externo...
27. Cuando la temperatura aumenta en el evaporador, la válvula de control de flujo abre y el

aceite pasa al evaporador de películas por barrido...
28. Si el nivel aumenta en el evaporador con bobina de calentamiento interna, el interruptor

flotador de alto nivel cierra la válvula de flujo de control entre el evaporador y el tanque flash

No.1...

29. El aceite esta ahora libre de agua y gasoil y listo para el procesamiento en la plataforma de

destilación (Proceso Final) ...
30. En este punto, Verificar que:

22.1.30.1. Las válvulas de fluido térmico están abiertas y el fluido térmico está circulando en
las chaquetas del evaporador de películas por barrido...

22.1.30.2. La bomba de vacío ha iniciado...

31. Las operaciones que toman lugar en el proceso final son las siguientes:
32. Cuando el nivel de vacío alcanza 700 mm Hg, el impulsador de vacío No.1 inicia...
33. Cuando el nivel de vacío alcanza 755 mm Hg, el impulsador de vacío No.2 inicia...
34. La planta de enfriamiento inicia y mantiene la temperatura establecida en el congelador que

congela los gases no condensables y VOC desde la planta, antes de que los gases entren la
bomba de vacío...

35. Ahora el evaporador de película por barrido está bajo vacío completo...
36. El flujo de aceite desde el evaporador (con bobina de calentamiento interno) al evaporador de

película por barrido es monitoreado y controlado por el flujómetro...
37. El agitador inicia y las cuchillas de barrido crea películas de aceite fino en el cabezote interno

de la superficie del evaporador...
38. El aceite lubricante empieza a destilar, los vapores fluyen radialmente hacia adentro; pasa a

través de un separador de arrastre y se condensa en un condensador interno y el producto

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

fluye hacia abajo las tuberías del condensador y afuera del evaporador y es recogido en el
receptor de aceite lubricante procesado...
39. El carbón sin quemar forma un residuo y fluye desde fuera de la salida del evaporador y se

recoge en el receptor de residuos...
40. Los vapores/gases no condensados se expulsan por la salida vacía...
41. La bomba del receptor de aceite lubricante procesado se ejecuta continuamente...
42. Cuando el nivel de aceite lubricante procesado sube, el controlador de nivel neumático

magnético proporcionalmente abre la válvula y el aceite va hacia el tanque principal de
almacenamiento de aceite lubricante procesado...
43. Si el interruptor de nivel neumático falla, el nivel aumenta y el interruptor de nivel alto del

receptor del aceite lubricante procesado para el agitador de película por barrido y cierra la

válvula de control de alimentación de aceite lubricante...

44. De igual manera, el gasoil del evaporador (con bobina calentadora interna) recoge en el

receptor de gasoil y cuando el nivel aumente, la válvula de control magnético neumática
proporcionalmente abre la válvula de control y el aceite va hacia el tanque principal de gasoil...
45. Si el interruptor de nivel neumático falla, el nivel aumenta y el interruptor de alto nivel en el

receptor de gasoil cierra la válvula de control del alimentador de vapor y válvula de control de
flujo de fluido térmico...
46. La bomba de receptor de residuo inicia cuando el interruptor de nivel medio detecta el nivel y

envía el residuo al tanque de almacenamiento de residuo.
47. Si el interruptor de nivel medio falla, el interruptor superior en el receptor de residuos cierra la

válvula de control de alimentación de aceite lubricante y detiene el agitador de películas por

barrido.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

##### FALLAS Y ALARMAS

**TABLA 2. POSIBLES FALLAS Y ALARMAS DE LA PLANTA DE APROVECHAMIENTO DE ACEITES.**

|EVENTO|CAUSA|SOLUCIÓN|
|---|---|---|
|~~Quemador caldera no enciende~~<br>|~~Señal de encendido no activada.~~<br>Baja presión combustible.<br>Electrodo en mal estado.<br>Sensor de llama averiado.<br>|~~De clic en el botón ON en la sección~~<br>boiler del Scada.<br>Verifique<br>si<br>hay<br>presión<br>de<br>combustible en el sistema.<br>Abra<br>la<br>válvula<br>manual<br>de<br>combustible.<br>Limpie<br>el<br>electrodo,<br>verifique<br>presencia de chispa.<br>Limpie sensor UV.<br>|
|~~Bomba no enciende~~|~~Modo de operación no seleccionado.~~<br>Protección térmica disparada.<br>Falla variador de frecuencia.<br>Falla de cableado.|~~Ubique el selector en un modo de~~<br>operación, automático o manual.<br>Verifique el estado del guardamotor.<br>Verifique el estado del variador de<br>frecuencia.<br>Reinicie el variador de frecuencia.<br>Revise el estado de los cables de<br>alimentación al motor.|
|Válvulas proporcionales no operan|Modo de operación no seleccionado.<br>Niveles al máximo.<br>Temperatura elevada.<br>Falta suministro de aire comprimido.<br>Falla de cableado.|Ubique el selector en un modo de<br>operación, automático o manual.<br>Baje los niveles de llenado en los<br>tanques.<br>Espere<br>a <br>que<br>la<br>temperatura<br>descienda por debajo de la consigna.<br>Verifique<br>la<br>presión<br>de<br>aire<br>comprimido.|
|Presión de vació no llega al nivel de<br>operación.|Bombas de vacío en falla o apagadas.<br>Fuga en tuberías.<br>Sensor en mal estado.|Encienda la bomba de vacío y los<br>Booster.<br>Reinicie los variadores de frecuencia<br>de las bombas.<br>Revise el estado de las tuberías del<br>sistema.<br>Revise la operación del transductor<br>de presión.|
|Temperatura no incrementa.|Caldera apagada.<br>Válvulas manuales cerradas.<br>Válvulas proporcionales cerradas.<br>Sensor de temperatura averiado.|Encienda la caldera para iniciar<br>calentamiento.<br>Abra las válvulas manuales del<br>sistema.<br>Verifique la operación de las válvulas<br>proporcionales.<br>Verifique el estado del trasmisor de<br>temperatura.|
|No se controla nivel de llenado|Sensor de nivel averiado.<br>Válvula proporcional en mal estado.<br>|Verifique el funcionamiento y la<br>señal del transmisor de nivel.<br>Ajuste la escala del transmisor de<br>nivel.<br>Revise la operación y sello de la<br>válvula proporcional.<br> <br>|

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

|Col1|Col2|Col3|
|---|---|---|
|Producto no ingresa al sistema.|Bomba de alimentación apagada.<br>Válvula manual de alimentación<br>cerrada.<br>Tanque de alimentación vacío.<br>Falla de nivel.|Encienda la bomba de alimentación<br>principal.<br>Abra<br>la<br>válvula<br>manual<br>de<br>alimentación.<br>Verifique el nivel del tanque de<br>alimentación.<br>Verifique<br>la<br>operación<br>de<br>los<br>sensores de nivel.|
|Alta temperatura en condensadores.|Falta de agua de refrigeración.<br>Tubería obstruida.<br>Sensor de temperatura averiado.|Encienda<br>las<br>bombas<br>de<br>recirculación<br>de<br>agua<br>de<br>enfriamiento.<br>Abra las válvulas manuales en el<br>sistema de recirculación de agua.<br>Verifique el estado del transductor<br>de temperatura.|
|Baja presión de aire comprimido.<br>|Compresor apagado.<br>Válvulas manuales cerradas.<br>Falla en sensor de presión.<br>|Encienda el compresor y revise el<br>funcionamiento.<br>Abra las válvulas manuales del<br>sistema neumático.<br>Verifique la operación del sensor de<br>presión.|

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

#### GUÍA DE MANTENIMIENTO

- VER ANEXO PLAN DE MANTENIMIENTO PREVENTIVO (PMP)

#### PLAN DE VERIFICACION

El plan de verificacion abarca los pasos seguir para garantizar una condicion segura de operación.

##### TOMA DE MUESTRA

- Siga las instrucciones del procedimiento “TOMA DE MUESTRA”, la humedad de la materia prima a
recibir no debe superar el 4% v/v.

- Si la humedad de la materia prima es mayor, y la humedad de los tanques 1,2 y 3 es menor al 4%, se
podría recibir la materia prima, haciendo trasiego entre tanques, siempre y cuando se garantice que la
humedad resultante sea de máximo 4% v/v.

- Siga las instrucciones del procedimiento “CARGUE Y DESCARGUE DE VEHICULOS”

##### ANTES DE INICIAR

1. Verificar que los tanques de Aceite Lubricante Usado, que van a hacer usados, estén llenos.
2. Drenar el agua de los tanques.
3. Verificar nuevamente humedad de materias primas (deberá ser menor al 4% v/v).
4. Verificar que las válvulas de salida están completamente abiertas.
5. Verificar que los filtros de cubo y los filtros magnéticos estén limpios.
6. Verificar que el nivel de agua en la Cuenca de la torre de enfriamiento está por arriba del nivel mínimo.
7. Verificar que la válvula de entrada de agua de la torre de enfriamiento está totalmente abierta.
8. Verificar que las válvulas del circuito de enfriamiento en el circuito principal están abiertas.
9. Inicie la bomba de agua de enfriamiento.

10. Iniciar ventilador de torre de enfriamiento.

11. Verificar que el nivel del fluido térmico en el tanque de expansión está por encima del mínimo.
12. Depure aproximadamente dos (2) Kg de nitrógeno en el tanque de expansión.
13. Verificar que todas las válvulas en el circuito del fluido térmico están abiertas.

14. Inicie la bomba de fluido térmico.

15. Inicialmente, verificar que la presión de salida y entrada de la bomba están en 5 y 2 Bar

respectivamente.
16. Permita que el fluido térmico circule por aproximadamente veinte (20) minutes.
17. Inicie el quemador.
18. Ajuste los puntos de referencia / _SET POINTS/_ de la salida y los controladores de retorno de temperatura

como lo requiera el proceso.
19. Verificar que las válvulas en el circuito de aire comprimido están abiertas.
20. Inicie el compresor y mantenga la presión.
21. Verificar que los discos de la bomba de vacío se mueven libremente rotando en forma manual la correa.

Evite usar el botón pulsador para este propósito.
22. Inicie la bomba de alimentación de Aceite Lubricante Usado y Verificar que el nivel del primer

evaporador se mantiene apropiadamente.
23. Inicia el panel de control PLC principal en modo auto.

|Col1|MANUAL DE OPERACIÓN<br>Y MANTENIMIENTO|Código: TM-MMO-20.01-02-V1|
|---|---|---|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|**Fecha actualización**|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|15/01/2020|
|<br>|**MANUAL DE OPERACIÓN**<br>**Y MANTENIMIENTO**|Página**4** de**42**|

##### DURANTE EL PROCESO

1. Verificar temperatura de gasoil no supere los 70oC.
2. Verificar temperatura de tk decanter que almacena nafta no supere los 70oC.
3. Verificar en la mirilla de la tubería del gasoil que el material pasa libremente a tanque.
4. Verificar que las reglas de nivel (backup y ppal) DE EVAPORADOR 1, EVAPORADOR 2, estén

registrando la misma medida.
5. Verificar presión en tanque evaporador 1, no debe sobrepasar los 3 psi, si sobrepasa esta presión,

la válvula de seguridad se activa dirigiendo los gases al scrubber.
6. Verificar que los tanques de Aceite Lubricante Usado estén llenos.
7. Drenar el agua de los tanques.
8. Verificar nuevamente humedad de materias primas (deberá ser menor al 4% v/v).
9. Verificar que las válvulas de salida están completamente abiertas.
10. Verificar que los filtros de cubo y los filtros magnéticos estén limpios.
11. Verificar que el nivel de agua en la Cuenca de la torre de enfriamiento está por arriba del nivel

mínimo.

12. Verificar que la válvula de entrada de agua de la torre de enfriamiento está totalmente abierta.
13. Verificar que las válvulas del circuito de enfriamiento en el circuito principal están abiertas.
14. Verificar funcionamiento de bomba de agua de torre de enfriamiento.
15. Verificar que el nivel del fluido térmico en el tanque de expansión está por encima del mínimo.
16. Verificar que todas las válvulas en el circuito del fluido térmico están abiertas.
17. Verificar que las válvulas en el circuito de aire comprimido están abiertas.

18. Verificar funcionamiento de la torre de vacío.

##### AL FINALIZAR EL PROCESO.

1. Verificar apagado de la bomba de alimentación de materias primas a evaporador 1.
2. Verificar presión de agua en líneas de enfriamiento, este debe estar entre 40 y 60 psi.
3. Verificar apagado de quemador en boilers.
4. Verificar que la bomba de recirculación de aceite termico siga funcionando hasta que la

temperatura del aceite térmico iguale o sea ligeramente mayor a la temperatura ambiente.
5. Verificar que las temperaturas del proceso estén disminuyendo.
6. Verificar que el nivel de agua en la torre de enfriamiento está por arriba del nivel mínimo.
7. Verificar que la válvula de entrada de agua de la torre de enfriamiento está totalmente abierta.
8. Verificar que las válvulas del circuito de enfriamiento en el circuito principal están abiertas.
9. Verificar funcionamiento de bomba de agua de torre de enfriamiento.
10. Verificar que todas las válvulas en el circuito del fluido térmico están abiertas.
11. Verificar que las válvulas en el circuito de aire comprimido están abiertas.

12. Verificar funcionamiento de la torre de vacío.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: LISTADO DE QUIPOS PLANTA DE VALORIZACIÓN DE ACEITE LUBRICANTE USADO.****

| SISTEMA | EQUIPO | CANT |
| --- | --- | --- |
| 1. EVAPORADOR 1 | 1. EVAPORADOR | 1 |
| 1. EVAPORADOR 1 | 1.1. BOMBA ALIMENTACIÓN EVAPORADOR 1 VIKING | 1 |
| 1. EVAPORADOR 1 | 1.1. BOMBA ALIMENTACIÓN EVAPORADOR 1 VIKING**BACK UP** | 1 |
| 1. EVAPORADOR 1 | 1.2. BOMBA PRINCIPAL EVAPORADOR 1 KSB | 1 |
| 1. EVAPORADOR 1 | 1.2. BOMBA PRINCIPAL EVAPORADOR 1 KSB**BACK UP** | 1 |
| 1. EVAPORADOR 1 | 1.3. INTERCAMBIADOR EVAPORADOR 1 | 1 |
| 1. EVAPORADOR 1 | 1.3. INTERCAMBIADOR EVAPORADOR 1**BACK UP** | 1 |
| 1. EVAPORADOR 1 | 1.4. COLUMNA EMPACADA SOBRE EVAPORADOR 1 | 1 |
| 1. EVAPORADOR 1 | 1.5. INTERCAMBIADOR DE CALOR DE NAFTA 1 | 1 |
| 1. EVAPORADOR 1 | 1.6. INTERCAMBIADOR DE CALOR DE NAFTA 2 | 1 |
| 1. EVAPORADOR 1 | 1.7. DECANTER NAFTA Y AGUA | 1 |
| 2. EVAPORADOR 2 | 2. EVAPORADOR 2 | 1 |
| 2. EVAPORADOR 2 | 2.1. COLUMNA EMPACADA SOBRE EVAPORADOR 2 | 1 |
| 2. EVAPORADOR 2 | 2.2. INTERCAMBIADOR DE CALOR GAS OIL | 1 |
| 2. EVAPORADOR 2 | 2.3. TANQUE GAS OIL | 1 |
| 2. EVAPORADOR 2 | 2.4. BOMBA GAS OIL VIKING | 1 |
| 3. TWFE | 5. TWFE | 1 |
| 3. TWFE | 3.1. REDUCTOR TWFE | 1 |
| 3. TWFE | 3.2. TANQUE PLO | 1 |
| 3. TWFE | 3.3. BOMBA PLO VIKING | 1 |
| 3. TWFE | 3.3 BOMBA PLO VIKING**BACK UP** | 1 |
| 3. TWFE | 3.4. TANQUE FONDO | 1 |
| 3. TWFE | 3.5. BOMBA FONDO VIKING | 1 |
| 3. TWFE | 3.5. BOMBA FONDO VIKING**BACK UP** |  |
| 4. TORRE DE VACIO | 4.1. BOMBA DE VACIO TRAVAINI | 1 |
| 4. TORRE DE VACIO | 4.1. BOMBA DE VACIO TRAVAINI**BACK UP** | 1 |
| 4. TORRE DE VACIO | 4.2. BOMBA DE VACIO BOOSTER 2000 | 1 |
| 4. TORRE DE VACIO | 4.2. BOMBA DE VACIO BOOSTER 2000**BACK UP** | 1 |
| 4. TORRE DE VACIO | 4.3. BOMBA DE VACIO BOOSTER 540 | 1 |
| 4. TORRE DE VACIO | 4.3. BOMBA DE VACIO BOOSTER 540**BACK UP** | 1 |
| 5. SCRUBBER | 5. SCRUBBER | 1 |
| 5. SCRUBBER | 5.1. BOMBA RECIRCULACION SCRUBBER | 1 |
| 6. CALDERAS ACEITE TÉRMICO | 6.1. BOILER THERMOPAC | 1 |
| 6. CALDERAS ACEITE TÉRMICO | 6.1. BOILER THERMOPAC**BACK UP** | 1 |
| 6. CALDERAS ACEITE TÉRMICO | 6.2. MOTOR BLOWER BOILER | 1 |
| 6. CALDERAS ACEITE TÉRMICO | 6.2. MOTOR BLOWER BOILER**BACK UP** | 1 |
| 6. CALDERAS ACEITE TÉRMICO | 6.3. LÍNEA DE GAS NATURAL | 1 |
| 6. CALDERAS ACEITE TÉRMICO | 6.4. BOMBA ACEITE TÉRMICO SIHI | 1 |
| 6. CALDERAS ACEITE TÉRMICO | 6.4. BOMBA ACEITE TÉRMICO SIHI** BACK UP** | 1 |
| 10. TORRE DE ENFRIAMIENTO | TORRE DE ENFRIAMIENTO ADVANCE PVT LTD | 1 |
| 10. TORRE DE ENFRIAMIENTO | MOTOR TORRE DE ENFRIAMIENTO | 1 |
| 11. COMPRESOR DE AIRE | COMPRESOR DE TORNILLO | 1 |
| 11. COMPRESOR DE AIRE | COMPRESOR DE TORNILLO**BACK UP** | 1 |
| 13. SISTEMA DE CONTROL | TABLERO DE CONTROL DE PROCESOS CON | - |
| 13. SISTEMA DE CONTROL | VISUALIZACIÓN HMI Y REMOTA | VISUALIZACIÓN HMI Y REMOTA |

**Tabla 2.: POSIBLES FALLAS Y ALARMAS DE LA PLANTA DE APROVECHAMIENTO DE ACEITES.****

| EVENTO | CAUSA | SOLUCIÓN |
| --- | --- | --- |
| ~~Quemador caldera no enciende~~<br> | ~~Señal de encendido no activada.~~<br>Baja presión combustible.<br>Electrodo en mal estado.<br>Sensor de llama averiado.<br> | ~~De clic en el botón ON en la sección~~<br>boiler del Scada.<br>Verifique<br>si<br>hay<br>presión<br>de<br>combustible en el sistema.<br>Abra<br>la<br>válvula<br>manual<br>de<br>combustible.<br>Limpie<br>el<br>electrodo,<br>verifique<br>presencia de chispa.<br>Limpie sensor UV.<br> |
| ~~Bomba no enciende~~ | ~~Modo de operación no seleccionado.~~<br>Protección térmica disparada.<br>Falla variador de frecuencia.<br>Falla de cableado. | ~~Ubique el selector en un modo de~~<br>operación, automático o manual.<br>Verifique el estado del guardamotor.<br>Verifique el estado del variador de<br>frecuencia.<br>Reinicie el variador de frecuencia.<br>Revise el estado de los cables de<br>alimentación al motor. |
| Válvulas proporcionales no operan | Modo de operación no seleccionado.<br>Niveles al máximo.<br>Temperatura elevada.<br>Falta suministro de aire comprimido.<br>Falla de cableado. | Ubique el selector en un modo de<br>operación, automático o manual.<br>Baje los niveles de llenado en los<br>tanques.<br>Espere<br>a <br>que<br>la<br>temperatura<br>descienda por debajo de la consigna.<br>Verifique<br>la<br>presión<br>de<br>aire<br>comprimido. |
| Presión de vació no llega al nivel de<br>operación. | Bombas de vacío en falla o apagadas.<br>Fuga en tuberías.<br>Sensor en mal estado. | Encienda la bomba de vacío y los<br>Booster.<br>Reinicie los variadores de frecuencia<br>de las bombas.<br>Revise el estado de las tuberías del<br>sistema.<br>Revise la operación del transductor<br>de presión. |
| Temperatura no incrementa. | Caldera apagada.<br>Válvulas manuales cerradas.<br>Válvulas proporcionales cerradas.<br>Sensor de temperatura averiado. | Encienda la caldera para iniciar<br>calentamiento.<br>Abra las válvulas manuales del<br>sistema.<br>Verifique la operación de las válvulas<br>proporcionales.<br>Verifique el estado del trasmisor de<br>temperatura. |
| No se controla nivel de llenado | Sensor de nivel averiado.<br>Válvula proporcional en mal estado.<br> | Verifique el funcionamiento y la<br>señal del transmisor de nivel.<br>Ajuste la escala del transmisor de<br>nivel.<br>Revise la operación y sello de la<br>válvula proporcional.<br> <br> |
