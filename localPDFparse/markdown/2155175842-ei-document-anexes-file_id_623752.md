---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: general
pages: 9
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Módulo de Efecto de Sombra Intermitente
-->

## APÉNDICE 3 MÓDULO DE SOMBRA INTERMITENTE

### Documentación General

# Módulo de Efecto de Sombra Intermitente

N° de Documento: K0815_051312_SP

Idioma: SP-español

 - Traducción al español del documento traducido del inglés del documento original

K0815_051312_DE, rev. 05) Esta es una traducción del inglés. En caso de duda, prevalece el texto en alemán.

Copyright ©2020 Nordex Energy Sociedad Limitada

Este documento, incluyendo cualquier presentación de su contenido en su totalidad o en parte, es la

propiedad intelectual de Nordex Energy S.A. La información contenida en este documento está

dirigida exclusivamente a los empleados de Nordex y a los empleados de y subcontratistas de Nordex

Energy S.A., Nordex SE y sus empresas afiliadas, tal y como se definen en el artículo 15 y siguientes

de la Ley de Sociedades Anónimas alemana (AktG) y nunca (ni siquiera en extractos) debe ser

divulgado a terceros.

Todos los derechos están reservados.

Cualquier divulgación, duplicación, traducción o cualquier otro uso de este documento o de partes

de este, ya sea en forma impresa, manuscrita, electrónica o de otro tipo, sin la sin la aprobación

explícita de Nordex Energy S.A. está prohibida.

© 2020 Nordex Energy S.A., Hamburgo

Dirección del fabricante según la Directiva de Máquinas:

Nordex Energy S.A.

Langenhorner Chaussee 600

22419 Hamburgo

Alemania

Teléfono: +49 (0)40 300 30 -1000

Fax: +49 (0)40 300 30 - 1101

info@nordex-online.com

[http://www.nordex-online.com](http://www.nordex-online.com/)

2/8

### Validez:

|Generación de la Turbina|Serie del Producto|Producto|
|---|---|---|
|Gamma|K08 Gamma|N90/2500<br>N100/2500<br>N117/2400|
|Delta|K08 Delta|N100/3300<br>N117/3000<br>N117/3000 controlled<br>N117/3600<br>N131/3000<br>N131/3000 controlled<br>N131/3300<br>N131/3600<br>N131/3900|
|Delta|Delta4000|N133/4.8,<br>N149/4.0-4.5,<br>N149/5.X,<br>N163/5.X|

3/8

### Tabla de Contenido:

**1.** **Introducción** ............................................................................................................................ 5

**2.** **Monitoreo de la sombra intermitente** .............................................................................. 5

**3.** **Principio funcional** ................................................................................................................ 5

**4.** **Registro** ..................................................................................................................................... 6

4.1. Configuración ....................................................................................................................... 6

4.2. Calendario de paradas .......................................................................................................... 6

**5.** **Componentes del Hardware** ................................................................................................ 6

**6.** **Unidad Central** ....................................................................................................................... 6

**7.** **Sensor de luz** ............................................................................................................................ 6

**8.** **Interfaz de las turbinas eólicas** ........................................................................................... 7

4/8

### 1. Introducción

La rotación de los álabes del rotor de una turbina eólica provoca una sombra intermitente

periódica durante las horas de luz del sol. Esto puede provocar una situación molesta en los

edificios circundantes y puede contribuir a crear prejuicios contra las turbinas eólicas en el

público en general. Para conceder protección a los habitantes cercanos a los parques eólicos,

las autoridades de control de emisiones han emitido normas diseñadas para limitar los

periodos del efecto de sombra intermitente a un nivel tolerable. Para conseguirlo, se

establece la instalación de un dispositivo de control que detendrá el aerogenerador que esté

causando el efecto de sombra intermitente cuando se supere la duración permitida. El

módulo de efecto de sombra intermitente SWM-V4.0 brinda la solución técnica para cumplir

con las restricciones oficiales. Registra todos los eventos de efecto de sombra parpadeante en

un archivo de registro.

### 2. Monitoreo de la sombra intermitente

El Módulo de sombra intermitente SWM-V4.0 puede monitorear la exposición del efecto de

sombra intermitente en hasta 2000 edificios (puntos de emisión). Se pueden incluir hasta

100 turbinas eólicas.

Se puede definir un nivel de exposición al efecto de sombra intermitente aceptable para un

día y para un periodo de tiempo en el año para cada edificio. Se puede suprimir el monitoreo

de determinados días de la semana (por ejemplo, los sábados y domingos para los locales

comerciales). Cuando se supera el nivel máximo de exposición al efecto de sombra

intermitente, el aerogenerador que causa el parpadeo de la sombra se apagará mientras dure

la caída de la sombra. Se registrarán todos los sucesos y desactivaciones del parpadeo de la

sombra.

### 3. Principio funcional

Por medio de un sensor de luz se mide la intensidad de la luz solar en las cuatro direcciones.

Sobre la base de estos resultados, el módulo de sombra intermitente puede evaluar si los

efectos de la sombra pueden o no producirse de forma general en las condiciones de

iluminación existentes. En paralelo, la unidad central calcula continuamente si uno de los

edificios que hay que proteger será alcanzado o no por la sombra del rotor de una turbina

eólica debido a la posición actual del sol. La unidad central de procesamiento comprueba si

el aerogenerador está funcionando o no y evalúa la posición del rotor en relación con el sol.

Si detecta sombra intermitente en uno de los edificios, los contadores diarios y anuales

respectivos serán incrementados. Cuando se supera el nivel máximo de exposición al efecto

de sombra intermitente, el aerogenerador que causa el parpadeo de la sombra se apagará

mientras dure la caída de la sombra.

El aerogenerador también puede detenerse cuando está en baja potencia, aunque el nivel

máximo permitido de exposición al efecto de sombra intermitente permitido no haya sido

excedido. Así, el presupuesto anual disponible para el funcionamiento a alta potencia de la

turbina eólica no será utilizado innecesariamente. El límite de potencia a partir del cual se

realizará una desconexión prematura puede establecerse individualmente para cada

aerogenerador.

5/8

### 4. Registro

4.1. Configuración

La configuración del módulo de sombra intermitente contiene todos los datos específicos del

proyecto. Allí, entre otros, se almacena la información de emplazamiento, de la estructura de la

turbina eólica y de los edificios a proteger y se define la duración máxima permitida del parpadeo

de la sombra.

4.2. Calendario de paradas

Se puede generar un calendario de paradas para detener las turbinas eólicas durante un periodo

de tiempo determinado. Para estas paradas también se puede considerar si la sombra intermitente

es posible en lo absoluto bajo las condiciones de luz en vigor. El calendario de paradas puede

contener hasta 40.000 paradas.

### 5. Componentes del Hardware

El módulo de sombra intermitente SWM-V4.0 consta de una unidad central y al menos un sensor

de luz, los adicionales son opcionales. El sensor de luz lleva integrado un módulo GPS que se

utiliza para el registro de la hora y la determinación de la posición de la TE. El sensor de luz se

monta en el techo de la góndola con un soporte de sensor.

### 6. Unidad Central

La unidad central del módulo sombra intermitente SWM-V4.0 está alojada en una cabina de

control separada (generación del sistema gamma), integrada en el _Topbox_ o incorporada en la

caja _CSB_ de la subestación de MT (generación del sistema delta). Se requiere 1 unidad central por

parque eólico.

**Funciones de la unidad central:**

 - Cálculo de los periodos de efecto de sombra intermitente en los edificios a monitorear.

 - Consultar los sensores de luz.

 - Comunicación con las turbinas eólicas del parque a través de una interfaz de red.

 - Detención del aerogenerador que provoca el efecto de sombra intermitente por haber

superado el nivel de exposición al parpadeo de la sombra permitido

 - Registro de todos los eventos y paradas de las turbinas eólicas.

### 7. Sensor de luz

El sensor de luz se monta en el techo de la góndola de un aerogenerador perteneciente al parque

eólico mediante un soporte. El sensor de luz se comunica con la unidad central del módulo de

sombra intermitente por medio de TCP/IP a través de la red existente.

6/8

### 8. Interfaz de las turbinas eólicas

La unidad central se comunica con los aerogeneradores a través de una interfaz de red. Este funciona

como un cliente con respecto a las interfaces del servidor, que residen en el software de control de

funcionamiento de los aerogeneradores. El sistema de control de los aerogeneradores transfiere

todos los datos relevantes a la unidad central de procesamiento del SWM a través de la LAN y del

protocolo de datos Modbus TCP. Los comandos de partida/parada se transmiten desde la unidad

central del SWM a cada uno de los aerogeneradores a través de la LAN (Modbus TCP). Tras la consulta

y procesamiento de los datos, los comandos de parada, las alarmas y otros mensajes de estado se

transmiten a cada uno de los aerogeneradores.

7/8

Copyright ©2020 Nordex Energy Sociedad Limitada