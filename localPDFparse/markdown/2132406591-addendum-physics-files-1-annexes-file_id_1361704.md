---
title: Sin título
author: Desconocido
date: D:20170930160617-03'00'
language: es
type: general
pages: 5
has_toc: False
has_tables: False
extraction_quality: high
---

**Especificaciones Técnicas de Red de Monitoreo**

**Introducción:**

Se requiere monitorear el caudal de los caudales en el marco “Las Delicias”
próximo a la ubicación de la casa de máquinas de la central hidroeléctrica en
proyecto y también los caudales que pasan por la tubería que va a la central
hidroeléctrica de 1,9 metros de diámetro y al mismo tiempo la medición del caudal
en la regla del canal Rafaelino. Adicionalmente se debe medir el caudal en el
estero Machali.

Para los canales se ha propuesto construir una sección de aforo con cámara de
aquietamiento, donde se instalaría un sensor de presión de tipo industrial. En la
tubería de la central se propone utilizar un sensor ultrasónico instalado en las
paredes externas del tubo. Todos los sensores trabajan en el rango 4-20 mA.

A continuación se indican las especificaciones de los sensores.

**Sensores de presión**

Los sensores de presión de tipo industrial LEEG modelo LMP638, son
compensados con la presión atmosférica para entregar una precisión de 0,25% a
full escala. Los sensores se instalan de acuerdo a la altura máxima del agua que
llega la barrera de la cámara de aquietamiento, ya que soportan máximo 1,5 veces
la altura de máxima de trabajo.

Estos sensores trabajan en corriente continua con voltajes entre 12 y 30 volts,
para proporcionar una corriente de 4-20 mA o 0 a 5 volts.

La temperatura de trabajo es entre -10°C y 70°C. La influencia de la temperatura
es de 0,02% full escala /°C.

La clase de protección del sensor es IP68 y los terminales IP67.

Vibración soporta 20g, y de 20 a 5.000 Hz.

Soporta golpes de 100g, 11 msegundos.

Material del sensor acero inoxidable 304 o 316.

Vida útil mayor a 1x10 [8 ] ciclos de presión.

**Sensor de caudal por efecto doppler**

Para la tubería que alimenta la central y la tubería de descarga se utilizaría
sensores de efecto doppler para medir el caudal, donde mediante dos
transductores piezo eléctricos en la parte externa del tubo son fijados mediante
unas abrazaderas, evitando intervenir el tubo. Las características técnicas de los
sensores Dynameters modelo DMDFB son las siguientes:

Precisión: 0,5% a 2% full escala

Diámetro del tubo: < 4000 mm

Rango de velocidad del flujo: desde 0,05 a 12 metros/seg

Contenido de partículas: Contenido de material reflectante >100 ppm, y al menos
el 20% del material reflectante debe ser > 100 micrones.

Transmisor

Alimentación: 100 a 240 VAC 50 Hz; 24 Volt DC.

Corriente salida: 4-20 mA, relay totalizador y alarma

Temperatura en el transductor: -40°C a 250°C

Display: 2 líneas de 8 caracteres

Tiempo de respuesta: 0 a 99 segundos, seleccionable

Transductor

Rango de medida: 0,05 a 12 metros/seg

Tipo: Abrazadera

Temperatura líquido: -40°C a 121°C, estándar.

Largo del cable: Hasta 300 metros

Material de la caja: Acero inoxidable

Clase de protección: IP65 y opcional IP68 para bajo el agua.

Los sensores se conectan a una RTU marca ICL modelo Spectra diseñados para
trabajar con paneles solares de baja potencia y en el punto central en la casa de
máquinas se conecta a otra RTU modelo Rubicon con su radio que integra todas
las señales de los sensores y los deja en un logger para ser transmitidos a la red
SCADA o a Internet mediante varios tipos de protocolos, entre ellos TCP/IP. Se
utiliza generalmente el protocolo DNP3.

Estación remota Diagrama de la RTU SPECTRA

La unidades de telemetría Spectra están equipadas con puerto serial I/O, Ethernet,
una radio celular 3G o inalámbrica en 900 MHz u otra banda de frecuencia, data
logging y alarmas.

Entradas analógicas: 6 entradas I/O, con 16 bits de resolución; 4-20 mA o 0 a 5
VoltDC

Entradas digitales: 2 I/O

Conectividad: Ethernet MODBUS TCP/IP UDP;SDX, HTTP, TFTP

Serial MODBUS RTU, SDX, DF1, SMS

Seguridad: Interna mediante el Sistema operativo, encriptación en la
comunicación, administración de la seguridad por el
administrador.

Logging: Cada un minuto

Alimentación: Solar, controlador solar o 12 0 24 volt DC

Rango de temperatura: -40°C a 70°C con 95% de humedad

La RTU master RUBICON de ICL tiene más potencialidades que las unidades
Spectra.

Controlador RUBICOM

Las especificaciones técnicas son las siguientes:

Puertos: 1 Ethernet; 3 Serial RS232 o RS485, 2 USB

Entradas analógicas: 4 Universal; 2 analógicas 4-20 mA

Entradas digitales: 20

Salidas digitales (relay): 10

Conectividad: DNP3; MODBUS TCP/IP UDP, Ethernet, SDX, FTP, E-mail, Telnet,

HTTP.

En serial maneja MODBUS RTU, MODBUS ASCII, DF1, DNP3, DFA Open link,
NMEA 12, HART, SMS

Data logging: OSV, XML, FREEFORM definido por el usuario, alarmas, hasta 100
muestras por segundo.

Historial: Hasta un año. Resolución hasta 1 segundo.

HMIs: En páginas web, interfase de texto con el usuario, mensaje de texto, panel
LCD. Configurable en ambiente WEB.

Esta unidad interactúa con el sistema SCADA de la central o ella misma es la que
toma el control del SCADA. Mediante acceso por Internet los canalistas pueden

tener acceso a los caudales de cada aforador de los canales, generalmente cada
2 minutos.

Las estaciones de telemetría no son invasivas ya que se instalan en monopostes
metálicos de 12 metros, similar al de una luminaria, con la excepción del aforador
en el estero Machalí que requiere sobrepasar el bosque en altura. Se ha estimado
una altura de 18 metros para instalar la antena directiva yagi.