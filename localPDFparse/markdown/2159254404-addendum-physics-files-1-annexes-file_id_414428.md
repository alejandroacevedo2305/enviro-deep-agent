---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 98
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DECLARACIÓN DE IMPACTO AMBIENTAL PISCICULTURA SAN PABLO DESARROLLOS ACUÍCOLAS SAN PABLO APÉNDICE I: MANUAL DE OPERACIÓN Y MANTENCIÓN SIGMA 980
-->

##### DESARROLLOS ACUÍCOLAS SAN PABLO

# DECLARACIÓN DE IMPACTO AMBIENTAL PISCICULTURA SAN PABLO DESARROLLOS ACUÍCOLAS SAN PABLO APÉNDICE I: MANUAL DE OPERACIÓN Y MANTENCIÓN SIGMA 980

##### Fecha: Mayo, 2023

Pág. 1 de 141 Declaración de Impacto Ambiental - Proyecto Piscicultura San Pablo

1

#### MEDIDOR ULTRASONICO DE FLUJO PERMANENTE

## SIGMA 980 MANUAL DE OPERACIÓN Y MANTENCION

_Manual de Operación y Mantención Sigma 980-1_

2

### TABLA DE CONTENIDOS

MEDIDOR DE FLUJO SIGMA 980

CONSEJOS PARA UN RAPIDO INICIO

Instalación

Programación

COMO CONTACTAR A SIGMA

Soporte Técnico Ilimitado

GARANTIA

SEGURIDAD Y ENTRADA A ESPACIOS REDUCIDOS

Procedimientos de seguridad que se deben tener presentes al entrar a los

espacios reducidos

UBICACIONES PELIGROSAS

ESPECIFICACIONES DEL DISEÑO

Medidor Integral de pH - Temperatura / ORP

Medidor integral de temperatural

Medidor Integral de Oxígeno Disuelto

Medidor Integral de Conductividad

Calibrador de entrada de Aguas Lluvias

Canales análogos de entrada

Salidas 4-20 mA

Totalizador Mecánicos

Modem

_Manual de Operación y Mantención Sigma 980-1_

3

CAPITULO II - INSTALACION Y CONEXIÒN

Montaje del Controlador del equipo SIGMA 980

Instalación en Placa de Soporte

Instalación en consola Mural

Instalación en Panel

SENSOR ULTRASONICO

Cómo Colgar el Sensor Ultrasónico desde el cable

Cómo montar el Sensor Ultrasónico en la Consola

Guía para una instalación apropiada del sensor

Distancia mínima hasta el líquido (banda muerta)

Distancia máxima desde el líquido

Rango invisible

Angulo de radiación

Tabla de referencia de la difusión de la radiación ultrasónica

Guía para evitar potenciales dificultades de ubicación

SONDA DE VELOCIDAD / SONDA SUMERGIDA DE NIVEL Y VELOCIDAD

Principios del funcionamiento

Selección del lugar

Recomendación de lugares apropiados para la ubicación de la sonda

Bandas de montaje de la sonda

Guía referencial para el montaje del hardware

_Manual de Operación y Mantención Sigma 980-1_

4

Envoltura de la banda

Sedimento

Instalación de la sonda en la tubería

Cómo manejarse en lugares complejos

Dirección de la velocidad

Aguas arriba (normal)

Aguas abajo

Siempre positivo

Corte de velocidad / Velocidad por defecto

SONDA SUMERGIDA DE PROFUNDIDAD /VELOCIDAD

Principios del funcionamiento

Calibración de la sonda sumergida de profundidad

Desecante de la sonda sumergida de profundidad /velocidad

Determinación del nivel actual de agua

Conexión del controlador del equipo SIGMA 980

_Manual de Operación y Mantención Sigma 980-1_

5

##### CAPITULO I

_Introducción al equipo SIGMA 980_

_Consejos para un inicio rápido_

- _Cómo comunicarse con SIGMA_

_Importante información de seguridad_

_Especificaciones de diseño_

##### INTRODUCCIÒN

Este manual ha sido diseñado para proporcionar un conocimiento completo del

Medidor Ultrasónico de Flujo Sigma 980 para su óptimo manejo y mantención. Se

recomienda la lectura previa de este manual antes de comenzar a operar el

equipo.

_**MEDIDOR DE FLUJO SIGMA 980**_

El Medidor de Flujo SIGMA 980 está capacitado para realizar la medición y

registro de flujo en canales abiertos. Además, el equipo SIGMA 980 también

puede medir y registrar en forma simultánea otros parámetros adicionales. Tales

como:

pH

Temperatura

- Nivel

Velocidad (solo versiones AV)

Caída de aguas lluvias

Siete entradas análogas (Voltaje y/o corriente)

_Manual de Operación y Mantención Sigma 980-1_

6

El Medidor de Ultrasónico de Flujo SIGMA 980 proporciona una exacta medición

de flujos en canal abierto sin tener contacto con el líquido.

El sensor ultrasónico debe ser dispuesto sobre el canal. El sensor ultrasónico del

medidor de flujo emite una secuencia de ondas de sonido hacia la superficie el

líquido, las que rebotan hacia la faz del sensor siendo registradas por el Medidor

de Flujo SIGMA 980. El tiempo que tarda cada pulsación en cubrir el trayecto

desde el sensor a la superficie del agua y regresar al sensor, se utiliza para

calcular el nivel de agua del canal.

En la mayoría de los casos, cuando se realiza la medición de flujo con el equipo

SIGMA 980 ultrasónicos, se utiliza en forma conjunta con dispositivos primarios de

medición (canaletas, vertederos, u otros dispositivos de geometría conocida). El

Medidor de Flujo SIGMA 980 mide y registra el nivel de flujo basándose en el

rango del nivel de flujo con relación al dispositivo primario utilizando las

ecuaciones incorporadas al equipo SIGMA 980.

Los cuatro parámetros de operación más importantes - intensidad de la pulsación,

la amplitud de la pulsación, sensibilidad del detector, y frecuencia - son

controlados constantemente por un microprocesador para optimizar las

condiciones.

Por medio del software de análisis InSight el usuario puede rescatar datos,

programar el sistema en forma remota, revisar el estado de los parámetros

almacenados en tiempo real, y manejar otros datos vía conexión RS232 o modem

opcional.

_Manual de Operación y Mantención Sigma 980-1_

7

**DISPLAY GRAFICO**

La pantalla iluminada del visor es de fácil lectura con un modo de texto de 8 líneas

por 40 caracteres. El visor de registro de cristal líquido le permite una rápida

revisión en terreno de los datos históricos almacenados incluyendo informes

resumidos y gráficos.

**CONTROL DE SEÑALES**

El equipo Medidor de Flujo SIGMA 980, además de su alta capacidad para

almacenar datos, está capacitado para controlar dos dispositivos externos con una

conexión de salida de 4 - 20 mA, permitiendo el uso de un muestreador de aguas

residuales externo, registrando el camino de muestreo y almacenando las fechas y

horas de muestreo controlados mediante 4 dispositivos externos con relés

N.O./N.C.

**COMUNICACIONES**

El Medidor de Flujo SIGMA 980 tiene un puerto de comunicaciones serial RS-232

y un módem externo para la transferencia de datos. Las actualizaciones del

programa interno incorporado al equipo son realizadas en terreno mediante uso

del puerto RS-232 que con la tecnología "Flash Memory" realiza un chequeo

periódico del estado del programa.

_Manual de Operación y Mantención Sigma 980-1_

8

**CONSEJOS PARA INSTALACIÓN RÁPIDA**

_**PELIGRO: Este instrumento debe ser instalado por personal técnico**_

_**capacitado para asegurar el cumplimiento con todos los códigos eléctricos y**_

_**de seguridad aplicables.**_

_**Desembalaje Del Instrumento**_

_Remover el equipo Sigma 980 del empaque y verificar si existe algún daño_

_aparente. Si el embalaje se encuentra dañado contactar inmediatamente al_

_proveedor local._

_**Aplicaciones Nema 4X**_

_Para mantener las características NEMA4X del equipo se deberá utilizar conduits_

_sellados o dispositivos tipo sello (no suministrados). Los equipos son embarcados_

_con tapas provisorias en las perforaciones. Estas tapas no son aceptables_

_durante la operación, por lo tanto el usuario deberá cubrir las perforaciones que no_

_se utilicen. Ver Figura 4._

_Se debe tener especial cuidado en la selección de las tapas, ya que estas sellarán_

_la pared de la carcaza. Existen en el mercado tapas estándar para proteger las_

_características NEMA 4X, es posible encontrarlas en las tiendas especializadas de_

_artículos eléctricos._

_Manual de Operación y Mantención Sigma 980-1_

9

**Instalación**

_**Paso 1 - Montaje del controlador**_

El controlador puede ser montado en una pared o en una baranda de soporte de

acuerdo a las condiciones del lugar. Se recomienda instalar el sensor con el panel

frontal hacia el norte para evitar el reflejo solar.

a) Montaje Mural

Instalar el Caudalímetro Sigma 980 utilizando las barras de montaje que vienen

con la unidad, ver Figura 7. Estas barras asegurarán la buena instalación del

instrumento. Utilizar 4 tornillos de 1⁄4 - 20. Ver Figura 8.

b) Montaje en barandas

Utilizar el kit de montaje suministrado.

Determinar si los soportes serán dispuestos en forma horizontal o vertical,

dependiendo de la dirección de la baranda. (Ver Figura 9).

Ajustar las fijaciones en las 4 perforaciones detrás del instrumento. Ver

Figura 7.

Deslizar las bandas ajustables de cada soporte. Ajustar a la medida de la

baranda y asegurar las bandas con los tornillos.

_Manual de Operación y Mantención Sigma 980-1_

10

_**Paso 2 - Instalación de las sondas**_

Las sondas de nivel y velocidad pueden ser instaladas en los sitios dispuestos

para ellas en el Medidor de Caudal. Las sondas de pH deben mantenerse

húmedas siempre. Ver capítulo 2 - Detalles para la instalación apropiada de las

sondas.

_**Paso 3 - Conexión de los sensores**_

Para la realizar la conexión de los sensores y otras interfaces se debe tener

presente que todas las fuentes de poder AC estén en posición apagado para evitar

golpes de corriente al realizar las conexiones.

_Manual de Operación y Mantención Sigma 980-1_

11

**PROGRAMACION**

_**Paso 1 - Fijación Hora y Fecha**_

Desde el Menú Principal ir a Opciones e ingresar la hora y fecha correctos.

_**Paso 2 - Configuración**_

Ingresar nuevamente al Menú Principal y seleccionar CONFIGURAR y siga todos

los ítemes del Menú, configurando de acuerdo a cada uno de sus requerimientos.

Unidades de Flujo (Gal/min, Mgal/día, Pie [3] /seg, etc.), usados en el despliegue

de datos de flujo.

Unidades de Nivel (pulgadas, pies, etc.)

Dispositivo Primario (Vertedero, canaleta, Formula de Manning, Area

Velocidad, etc.)

Camino de Muestreo (Intervalo de flujo opcional para realizar un muestreo de

acuerdo a las proporciones del rango de flujo).

_**Paso 3 - Opciones Avanzadas**_

Revisar los ítemes contenidos en el menú OPCIONES AVANZADAS y configurar

de acuerdo a los requerimientos. La CALIBRACIÓN, REGISTRO DE DATOS y

SISTEMA TOTALIZADOR son opciones que siempre deberían ser revisados:

Se debe ejecutar la Calibración en la mayoría de los sensores cuando son

instalados por primera vez, siguiendo la secuencia de indicaciones. (Para

mayores detalles Ver Capítulo Mantención ).

_Manual de Operación y Mantención Sigma 980-1_

12

Los canales de registro de datos deben estar disponibles si se desea guardar

los datos en la memoria. Se debe seleccionar los canales que se desea grabar

y seleccionar el intervalo de grabación.

El Totalizador debe ser configurado de acuerdo a un factor de escala aceptable

para los rangos de flujo de cada lugar. La selección de un factor de escala

muy bajo puede ocasionar una actividad totalizadora rápida no recomendada.

_**Paso 4 - Ajuste de Nivel**_

Hacer coincidir el nivel desplegado con el nivel real del canal (el nivel o "cabezal"

que esta _contribuyendo al flujo_, para el Area Velocidad: ingrese la distancia desde

la superficie del agua hasta el fondo de la tubería), usar la tecla AJUSTE DE

NIVEL del panel delantero. Realizar una medición física del nivel del canal e

ingresar el numero utilizando el teclado numérico.

**IMPORTANTE**

**Al terminar la operación, ¡No olvidar presionar la tecla EJECUTAR, para**

**comenzar a ejecutar el programa!, la palabra "EN EJECUCIÒN" se**

**desplegará en la esquina inferior izquierda del visor.**

_**Paso 5 - Revisión del programa**_

Es muy importante realizar una revisión del programa mediante el uso de las

selecciones del menú SISTEMA/REVISION DE TODOS LOS ITEMES (ALL ITEM

REVIEW) antes de dejar el sitio de muestreo para asegurarse de que todo está

debidamente programado de acuerdo a los requerimientos. Tampoco se debe

_Manual de Operación y Mantención Sigma 980-1_

13

olvidar revisar la Pantalla de Estado para asegurarse de que todos los canales en

uso están registrando de acuerdo a lo esperado.

**GARANTIA EN CASO DE FALLAS DEL EQUIPO**

Si se produce algún problema con su producto SIGMA dentro de un año a contar

de la fecha de embarque, HACH lo reparará sin trámites ni demora sin costos de

transporte para el cliente.

Para esta finalidad es importante que embale cuidadosamente el equipo adquirido

preferentemente en su envase original, y embárquelo vía UPS cuando sea posible.

**Nota:**

**Es importante que incluya junto a la unidad dañada una descripción del**

**problema, nombre, dirección y número de teléfono del remitente.**

**Al final de este manual se ha incluido un formulario para saber cómo obtener**

**un número de autorización de la devolución.**

_Manual de Operación y Mantención Sigma 980-1_

14

**SEGURIDAD Y ENTRADA A ESPACIOS REDUCIDOS**

**IMPORTANTE:**

**Es necesario haber recibido un entrenamiento adicional antes de comenzar**

**con las pruebas para pre-entrada, ventilación, procedimientos de entrada,**

**evacuación/rescate y las prácticas de trabajo seguro que eviten correr riesgo**

**vital innecesario durante el trabajo en espacios reducidos.**

**Los consejos que se presentan a continuación están dirigidos a los**

**usuarios de equipos Medidores de Flujo SIGMA 980 con el fin de**

**proporcionarles una breve descripción de los riesgos y peligros asociados**

**con la entrada a espacios reducidos.**

La última norma dictada por la OSHA respecto al CFR 1910.146 "Solicitud de

Permiso para Espacios Reducidos" se convirtió en Ley en Abril de 1993. Este

nuevo estándar rige en 250.000 zonas industriales en los Estados Unidos y fue

creado para proteger la salud y seguridad de los trabajadores en espacios

reducidos.

_**Definición de un Espacio Reducido**_

Un espacio reducido es un lugar o sitio cerrado que tiene o presenta en forma

potencial una o más de las siguientes condiciones:

Una atmósfera con menos de 19.5% de oxígeno y/o más de 10 ppm de Sulfato

de hidrógeno (H [2] S).

_Manual de Operación y Mantención Sigma 980-1_

15

Una atmósfera que puede ser inflamable o explosiva debido a los gases,

vapores, bruma, polvo o fibras.

Materiales tóxicos que al contacto o inhalación podrían causar daño, deterioro

de la salud o la muerte.

Los espacios reducidos no están diseñados para ser ocupados por personas.

Tienen un acceso restringido y tienen peligros o riesgos potenciales.

Entre los sitios denominados espacios reducidos podemos encontrar: Pozos,

chimeneas, cañerías, tanques, bóvedas con interruptores u otros lugares

similares.

**Procedimientos de Seguridad que se deben seguir antes de acceder a un**

**Espacio Reducido:**

1.- Inspeccionar previamente todo el equipo de seguridad antes de iniciar cada

operación.

2.- Revisar la calibración de todos los detectores de gas antes de su uso.

3.- Verificar la posibilidad de explosiones de oxígeno, gas y sulfato de

hidrógenos antes y durante el acceso a cualquier espacio reducido. Revisar

completamente las tres zonas del espacio reducido (parte superior, media e

inferior). No entre si alguna de las pruebas ha resultado positiva. Si suena la

alarma de gas mientras está dentro del espacio salga inmediatamente.

4.- Utilice zapatos de seguridad con punta de acero y use las herramientas

apropiadas para sacar la tapa del pozo. Al interior del pozo utilice el equipo de

seguridad adecuado, casco de seguridad, antiparras, y guantes apropiados.

_Manual de Operación y Mantención Sigma 980-1_

16

5.- Optimice las condiciones de ventilación antes y durante la entrada.

6.- Tome precauciones con respecto a su peso corporal y el peso que pueden

resistir los escalones o zonas de acceso al espacio reducido, ya que, debido a

las malas condiciones de iluminación no es posible inspeccionar su estado, es

probable que se encuentren corroídos o sueltos.

7.- Use cuerdas de vida para rescate, arneses con asiento y arneses de pecho

apropiados.

8.- Cuando una persona se encuentra inspeccionando un pozo, es importante

que haya al menos dos personas resguardando el ingreso y al menos tres

personas cuando son dos personas las que acceden al pozo.

9.- No permanezca más de 45 minutos en un pozo sin tomar una pausa fuera

de éste.

10.- No descienda a una alcantarilla combinada o de descarga (36"/91 cm)

durante o inmediatamente después de una lluvia. Debido a que los flujos de

agua combinados favorecen un piso resbaloso y podrían hacerlo caer en una

posición que dificulte su reincorporación y por ende su salida de la alcantarilla.

11.- No realice ningún trabajo en un camino o calle sin un conocimiento

adecuado del control de tráfico. Cuando requiera trabajar en un terreno con alto

flujo vehicular, es importante estar alerta y usar el equipo de señalización

adecuado para trabajos en camino (conos, barreras, etc.).

12.- Mantenga el área de trabajo libre de escombros y herramientas que

pudieran caer dentro del pozo. La caída de objetos podría ser mortal.

_Manual de Operación y Mantención Sigma 980-1_

17

13.- Infórmese a cerca de los lugares de emergencia más cercanos al lugar de

trabajo (hospitales, centros asistenciales o unidades de emergencia).

_**LUGARES PELIGROSOS**_

**ADVERTENCIA:**

**EL MEDIDOR DE FLUJO SIGMA 980 NO ESTA HABILITADO PARA**

**TRABAJAR EN LUGARES PELIGROSOS CONFORME A LO ESTIPULADO EN**

**EL CODIGO NACIONAL DE ELECTRICIDAD.**

**REQUERIMIENTOS DE LA COMISIÓN FEDERAL DE COMUNICACIÓN**

1.- La Comisión Federal de Comunicación ha establecido un reglamento que

permite el la conexión directa de esta unidad a la línea telefónica. Utilizando

enchufes de conexión estandarizados para este tipo de conexión. Este equipo no

debe ser usado en líneas de uso público o con monedas.

2.- Si el equipo no está funcionando correctamente, es posible que ocasiones

problemas en la línea telefónica, esta unidad debería ser desconectada hasta que

se determine el origen del problema y hasta que el problema sea solucionado. De

lo contrario la compañía telefónica correspondiente desconectará el servicio en

forma temporal.

3.- La compañía telefónica puede realizar cambios en sus operaciones y

procedimientos técnicos; este tipo de cambios podría afectar la compatibilidad o el

uso del equipo. Es importante que la compañía telefónica mantenga a sus

usuarios informados de los cambios a realizar.

_Manual de Operación y Mantención Sigma 980-1_

18

4.- Si la compañía telefónica solicita información a cerca de los equipos que

están conectados a sus líneas, infórmelos:

a) El número telefónico al que está conectado el equipo.

b) El valor equivalente del ring (1.4B)

c) El enchufe de conexión USOC que se requiere (RJ11C), y

d) El número de Registro de la Comisión Federal de Comunicaciones.

Los ítemes (b) y (d) se encuentran indicados en la etiqueta. El valor equivalente

del ring (REN) se usa para determinar el número de unidades que pueden ser

conectadas en su línea telefónica. En la mayoría de las zonas, la suma de RENs

de todos las unidades conectadas a cualquier línea no debería exceder las 5. Si

se instalaran más unidades podrían no funcionar correctamente.

_**SOLICITUDES DE SERVICIO**_

5.- En caso de que el equipo falle, todas las reparaciones deberían ser

ejecutadas por nuestra compañía o representante autorizado. La solicitud de

servicio técnico es de responsabilidad de nuestros usuarios. Si necesita

contactarnos hágalo a.

ECOPRENEUR CHILE S.A.

Av. Eliodoro Yañez 2245, Providencia

Santiago - Chile

Tel: (56-2) 205.1040

_Manual de Operación y Mantención Sigma 980-1_

19

**SENSOR ULTRASONICO**

**Precisión :** Rango de 0,03 pies sobre 2 pies al cambio de cabezal, @ 20°C, al

aire, objetivo ideal, 25 mts de cable.

**Rango:** La distancia mínima entre el sensor y el líquido es de un mínimo de

11,5 pulgadas (38 cms) y la distancia máxima es de 10,7 pies, con un objetivo

ideal de @ 20° C, al aire con 25 metros de cable.

**Intervalo:** 0 - 29 pies (0 - 8,84 m)

**Rango de temperatura de Operación:** -20 a 50°C (-4 °F a 122 oF)

**Material:** Gabinete de PVC con una ventana acústica de PVC

**Cable:** coaxial RG-62 au

**Largo del Cable:** Largo estándar de 7,6 m. contacte a su proveedor si requiere

cable de mayor extensión.

**Especificación del Cristal:** 75KHz

**Abertura Angulo del Haz:** + 12° (-10dB)

**Dimensiones del transductor:** 12,7 cm x 5,7 cm (5.0”H x 2,25”D)

_Manual de Operación y Mantención Sigma 980-1_

20

**OPCIONES DE INSTALACION DE FABRICA**

**MEDIDOR DE FLUJO SIGMA 980**

**Velocidad de Medición:**

Método : Principio Doppler ultrasónico

Tipo de transductor : Cristales piezoeléctricos dobles de 1 MHz

Profundidad mínima requerida

Para Medición de velocidad : 8 pulg. (2 cm)

Rango Fluctuación : -5 a 20 pies/s (-1,52 a 6,10 m/s)

Estabilidad Cero : <.05 pies/s (.015 m/s)

Precisión : + 2% de lectura

Temperatura de operación: 0 a 140oF (-18 a 60oC)

**Nivel de Medición: (sin alineación ni histéresis)**

Nivel de Medición estándar: -.018 a 11.5 pies + .023 pies (.005 m a 3.5 m +

.007 m)

Nivel de Medición extendido: -.018 a 34.6 pies + .07 pies (.005 a 10.5 m +

.021m)

Nivel Máximo permitido: 3x sobre presión

Rango de Temperatura

de operación : 32 a 160 oF (0 a 71oC)

Rango de Compensación

de Temperatura : 32 a 86oF (0 a 30oC)

Temperatura de Error : .018 a 11.5 pies + .004 pies/oF (.005 m a 3.5

m + .0022 m/oC)

_Manual de Operación y Mantención Sigma 980-1_

21

Máxima de Error

Compensación del rango

de Temperatura por grado

de cambio : .018 a 34.6 pies + .012 pies/oF (.018 a 10.5 m +

.006 m/oC)

Velocidad de error

en profundidad : 0 a 10 pies/s (0 a 3.05 m/s) = .085% en lectura

Toma de aire : La presión atmosférica de referencia está

protegida con desecante.

Cable : Sensor de uretano con respiradero

Largo del cable : Estándar 25' (7,6m) - Máximo 250' (76 m)

**Medidor Integral de pH**

**Control /Registro:** Campo seleccionable para registrar pH

Temperatura independiente del flujo o en conjunto con el flujo, además controla la

recolección de muestras en respuesta al valor de los puntos de referencia

alto/bajo.

**Intervalos de grabación:** 1,2,3,5,6,10,12,15,20,30 y 60 minutos

**Gabinete :** NEMA 4X con etiqueta listada en terminal

**Sonda de pH** **:** Compensación de temperatura; cuerpo de plástico ABS

resistente a los impactos; combinación de electrodos con

conexión de Teflón ® poroso.

**Rango de Medición:** 0 a 176oF (-14 a 80oC)

**Dimensiones :** Diámetro 0.75" x Largo 6" con .75"

_Manual de Operación y Mantención Sigma 980-1_

22

Hasta el final del cable

(1.9 cm x 15.2 cm con 1.9 cm hasta el final del

cable)

**ESPECIFICACIONES DEL DISEÑO**

**CONTROLADOR DEL MEDIDOR DE FLUJO SIGMA 980**

**Dimensiones** **:** Alto 14,62" x ancho 11,88" x diámetro 8,26"

(16.2 cm x 27.9 cm x 14.3 cm)

**Gabinete** **:** NEMA 4X, IP66 con tapa frontal, resistente a los

rayos UV

**Cubierta del Gabinete** **:** NEMA 4x,IP66

**Rango de temperatura de**

**Operación** **:** -20 a 50°C (-4 a 122°F)

**Temperatura de**

**Almacenamiento** **:** -20 a 70oC (-40 a 158 oF)

**Especificaciones Eléctricas**

Requerimientos de energía: 100-230 VAC, 50/60 Hz, monofásico, 15W max

(0.25 amp max)

Voltaje : 100 a 230 VAC (*)

(*) VAC : Voltios de corriente alterna

Categoría de instalación : II

Conexión Eléctrica : Siete 0.5 pulg. Hub, uno 1.0 pulg. hub

Salida muestreador : 15 V dc, 100 mA a 500 ms de duración

_Manual de Operación y Mantención Sigma 980-1_

23

**Visor Gráfico:**

Pantalla iluminada de cristal líquido de fácil lectura con un modo de texto de 8

líneas por 40 caracteres en código ASCII, 64 puntos por 240 puntos en modo para

gráficos. Dimensiones: 1,5" de alto por 5" de ancho (3.8 cm x 12.7 cm); despliega

Niveles v/s Tiempo, Precipitaciones v/s Tiempo, pH, ORP, Temperatura, Oxígeno

Disuelto, Conductividad v/s tiempo. Marcas importantes durante el muestreo,

señales de alarma. Condiciones del indicador de Alarma.

**Teclado:** Conmutador de membrana sellada con 19 posiciones; 4 teclas

digitales, con funciones definidas por el visor.

**Totalizadores:** Programa Totalizador de 8 dígitos reseteables y 8 dígitos no

reseteables.

**Precisión Tiempo Base:** + 1 segundo por día.

**Unidades de Medición:**

Nivel: Pulgadas, metros, centímetros, pies

Flujo: Galones por segundo, galones por minuto, galones por hora, litros

por segundo, litros por minuto, litros por hora, miles de galones por día, acre-pie

por día, pies cúbicos por segundo, pies cúbicos por minuto, pies cúbicos por hora,

pies cúbicos por día, centímetros por segundo, centímetros por minuto,

centímetros por hora, centímetros por día.

Flujo Totalizado: Galones, pies cúbicos, acre-pie, litros, metros cúbicos.

- pie cúbico, galón, metro cúbico, litro, acre-pie.

_Manual de Operación y Mantención Sigma 980-1_

24

**Dispositivos Primarios:**

_Canaletas :_ Parshall, Palmer Bowlus, Leopold-Lagco, H, HL, HS,

Trapezoidal.

_Vertederos:_ V-Notch, (22.5 - 120o), sin contracción rectangular, Thel -mar,

Cipolletti compuesta.

_Formula de Manning_ : Canales redondos, Canales en U, canales Rectangulares,

canales trapezoidales.

_Boquilla de Flujo:_ Kennison, Parabólica, Tubería California.

**Registro de Datos:**

La ubicación de la memoria dinámica permite el uso de la memoria en uno o varios

canales; así como también seleccionar el registro o finalización del archivo de

datos almacenados. Con 18.432 puntos de datos estándar. Memoria de

estadísticas diarias disponible hasta por 32 días.

**Salida de 4 - 20 mA :**

Dos señales de salida disponibles, una Salida estándar, y una de campo integral

opcional de salida asignable. Con aislación óptica, con una resistencia de hasta

1.000 Ohm de carga por cada salida; con un 1% libre de errores del sistema.

**Salida del muestreador:**

Pulso 12 VDC (*) 100 mA máximo a 500 ms de duración.

(*) Voltios de corriente continua.

_Manual de Operación y Mantención Sigma 980-1_

25

**Comunicaciones:**

Conexión serial a computadora compatible con IBM a 18.2k baud con software de

análisis de datos Sigma. Módem opcional.

**Relés de Alarma:**

Cuatro relés de alarma integrados, 10 amp "form C" asignables al usuario para

algún canal de datos interno o externo.

**Salidas de 4-20 mA:**

Dos salidas de campo asignables integrados (Uno estándar y el otro opcional),

Con aislación óptica, con una resistencia de hasta 1.000 Ohm de carga por cada

salida; con un 1% libre de errores del sistema.

**Totalizador mecánico:**

Totalizador mecánico no reiniciable con 6 dígitos separados . Con unidades

seleccionables; galones, litros, pies cúbicos, metros cúbicos, acre-pie.

**Módem:**

Módem de 14.400, V.32 bis, con protocolo celular MNP10-EC, Comprensión de

datos MNP5 de V.42 bis, corrección de errores MNP2-4.

**Entrada de Medidor de Aguas Lluvias:**

Puede ser usado con el Balde de Puntera del Medidor de Aguas Lluvias Sigma;

el medidor de flujo se puede iniciar en base al campo seleccionable del

promedio de aguas lluvias. El medidor de flujo registra los datos de las

precipitaciones.

_Manual de Operación y Mantención Sigma 980-1_

26

**Canales de Entrada Análogos para registro de datos**

El equipo Sigma 980 tiene hasta 7 canales adicionales de registro de datos desde

fuentes externas.

La medición de flujo puede iniciarse una vez seleccionada la tasa de aguas

lluvias en terreno.

El flujómetro registra los datos de aguas lluvias.

Cable protegido de 100 pies de largo máximo

Cada gota =0.25mm (0.01 pulg.) de lluvia

_Manual de Operación y Mantención Sigma 980-1_

27

**CAPITULO 2**

_**INSTALACION Y CONEXIÓN**_

El Medidor de Flujo SIGMA 980 se encuentra ubicado dentro de un gabinete

hermético hecho de material termoplástico de alta resistencia, fabricado con una

ingeniería de última generación. La parte mecánica del equipo en su totalidad

está hecha de materiales altamente resistentes a la corrosión, permitiendo su

manipulación en terrenos escarpados y en condiciones adversas.

Todos los controles se encuentran dispuestos en el panel frontal del equipo de

manera que sean de fácil acceso y se encuentran protegidos por una cubierta

sellada transparente. El equipo está habilitado para ser montado en una consola

mural, en una placa de montaje Sigma o panel.

El equipo SIGMA 980 tiene dispuestos en la base del gabinete ocho conectores

protegidos herméticamente para proveer de energía a las conexiones de interface

de accesorios externos.

**MONTAJE DEL CONTROLADOR DEL EQUIPO SIGMA 980**

El gabinete del Equipo SIGMA 980 contiene cuatro barras de apoyo, dos a cada

lado del gabinete, cada barra de apoyo tiene una rosca en la que se inserta un

perno 10-32 que atraviesa completamente cada barra. Estos facilitan el montaje

en la consola mural, en una placa de montaje Sigma o panel.

_Manual de Operación y Mantención Sigma 980-1_

28

**MONTAJE EN CONSOLA MURAL**

El montaje del Equipo SIGMA 980 con dispositivo de montaje PN5084 se ejecuta

como se muestra a continuación:

**SENSOR ULTRASONICO**

El Medidor Ultrasónico SIGMA 980 está equipado con una avanzada tecnología de

señales ultrasónicas de proceso para minimizar los efectos de los factores

ambientales. Sin embargo, la elección de un sitio apropiado puede facilitar

enormemente el buen funcionamiento del sistema.

Es posible conseguir una medición con un mínimo margen de error si se elige la

zona de muestreo considerando las siguientes características:

Ubicar el sensor ultrasónico en el punto de medición a la altura de caída de

agua apropiado para éste dispositivo primario. (Ver el Apéndice C Ubicación

de dispositivos primarios para la medición).

Ubique el sensor ultrasónico sobre el centro del flujo del caudal donde haya el

mínimo de turbulencia. Realice el montaje del sensor en un sitio estable y

seguro utilizando cualquiera de los siguientes métodos.

_Manual de Operación y Mantención Sigma 980-1_

29

**Cómo Montar el equipo SIGMA 980 en una Consola Mural**

Para realizar el montaje del equipo SIGMA 980 a una consola mural es necesario

adquirir la parte No 5093. Esta consola proporciona una alternativa estable y

segura para montar el equipo en una pared o panel como se muestra a

continuación:

**Cómo Montar el equipo SIGMA 980 en un Panel**

Prepare la superficie del panel e instale el equipo SIGMA 980 con cuatro pernos

10-32 como se muestra a continuación.

**Rango Invisible**

El equipo SIGMA 980 está equipado con la ventaja de Rango Invisible (ajustable

a la banda muerta), para evitar ecos falsos desde la parte superior de las paredes

del canal, laderas o escalones, etc. (ver dibujo).

El Rango Invisible se establece mediante la calibración del medidor ultrasónico en

la sección Opciones Avanzadas. Para más detalles ver Capítulo de

Programación.

_Manual de Operación y Mantención Sigma 980-1_

30

#### Guía para la Apropiada Instalación del Sensor

**Distancia Mínima desde el Líquido (Banda Muerta)**

Por ejemplo, si se usa el sensor ultrasónico de 50 KHz la Banda Muerta estaría

situada a menos de 15 pulgadas (38 cm), para mejores resultados ubique el

sensor a unas 15 pulgadas (38 cm), desde el nivel de agua más alto esperado.

El sensor es sensible a cualquier cosa que esté próxima a la banda muerta y

dejará de registrar el nivel cuando la distancia sea inferior a la requerida como

mínimo. Las alarmas de error se suscitan cuando las señales del sensor pierden

el contacto mínimo requerido respecto a la banda muerta.

**Inmersión del Sensor**

A pesar de que el sensor está sellado y no se daña si se sumerge eventualmente

(por caída) a una profundidad de 6 pies (15,24 cm), evite la inmersión del sensor.

Debido a que el equipo SIGMA 980 percibe los sonidos relativamente débiles del

eco de retorno, un sensor impermeabilizado no podrá detectar el eco

correctamente y podría no ser capaz de ejecutar una medición exacta. Por lo

tanto, es importante mantener la cara del sensor libre de acumulaciones de grasa

y suciedad.

_Manual de Operación y Mantención Sigma 980-1_

31

**Abertura del Angulo del Haz**

El ángulo de abertura del haz de sonido que emana de la base del sensor

ultrasónico se dispersa fuera del ángulo de 12o a medida que se aleja del sensor.

Esto se traduce a que si usted instala el sensor a mucha altura sobre un canal

angosto el haz de sonido puede ser más amplio que el canal cuando éste lo

alcance. Este fenómeno puede producir ecos falsos desde la parte superior de las

paredes del canal en lugar de producirlos desde la superficie del agua.

El dibujo y la tabla que se muestran a continuación muestra cómo se expande el

rango de radiación a una altura de 30 pies (9.1m), con un sensor de 50 kHz.

El sensor debe estar montado idealmente de manera que todo el haz caiga dentro

del canal y no choque con ningún objeto que pueda proyectarse dentro del canal

como por ejemplo, las paredes laterales.

Los retornos falsos no deseados provenientes de los laterales del canal se pueden

eliminar con el aumento del Rango Invisible (ajustando la banda muerta), bajando

el sensor, o con una combinación apropiada de ambos en un sitio dado.

Los retornos no deseados que resultan de las proyecciones dentro del canal

pueden ser eliminados mediante la reubicación del sensor a un lugar donde la

señal no tenga contacto con ninguna parte del cono del haz. Esto se puede

complementar cambiando el sensor a una ubicación más baja (en la parte más

angosta del haz), o trasladando horizontalmente el sensor a un sitio donde el cono

no pueda ser tocado por ningún objeto. Así mismo, el Rango Invisible puede ser

ajustado de manera que la proyección esté dirigida al rango invisible y de esta

forma ser ignorado.

En el capítulo de Programación encontrará mayores detalles para ajustar el Rango

Invisible.

_Manual de Operación y Mantención Sigma 980-1_

32

El ancho máximo de abertura del haz se puede calcular como 0.20 por la distancia

del sensor.

**GUIA DE DIFICULTADES DE UBICACIÓN**

_Corrientes de convección_

Los componentes de convección entre el sensor y el objetivo cambiará la

velocidad de la señal de sonido. Si se presentan estas condiciones, es preferible

instalar una defensa o pantalla alrededor del haz de sonido para eliminar la

variación de temperatura debido a las corrientes de convección. El sistema está

diseñado con un promedio de rutinas para ayudar a solucionar este problema.

La impedancia acústica de la espuma y el aceite es baja en relación con el aire.

Gracias a que el equipo SIGMA 980 está diseñado con un esquema AGC (Control

Automático de Ganancia), es posible reducir el impacto de estos factores, se

recomienda que se seleccione otros lugares que no presenten estas anomalías.

_Turbulencia_

Con las rutinas de señales de proceso avanzadas incorporadas al equipo SIGMA

980, es posible obtener un informe preciso de los objetivos con 4 - 6 pulgadas

(10.16 - 15.24 cm) de turbulencia.

_Obstrucciones_

Por medio del uso de la Banda Muerta (Rango Invisible), ajustable del equipo

SIGMA 980 es posible seleccionar los objetivos más allá de las obstrucciones

periféricas. Al establecer esta zona de exclusión, se debe procurar realizar una

fijación del Rango Invisible más alto que el nivel máximo esperado.

_Manual de Operación y Mantención Sigma 980-1_

33

_Temperatura_

El equipo SIGMA 980 está equipado con un compensador de temperatura para los

lugares con condiciones ambientales normales. La temperatura constante de este

de este sensor es de aproximadamente 100 minutos. Es por ésto que durante la

instalación es preciso asegurarse de que el sensor haya alcanzado una

temperatura estable para 100 antes de la calibración.

_Tiempo de Respuesta_

El equipo SIGMA 980 ha sido diseñado para resolver pequeñas variaciones del

nivel en períodos de 5 - 10 segundos. Este corto tiempo de respuesta permite la

detección de niveles tan reducidos como 0.2 pulgadas (5 mm) en 5 minutos como

podría suceder en condiciones anormales.

_Registro de Eventos_

Las ventajas del Registro de Eventos del equipo SIGMA 980 se pueden

seleccionar en el Menú de Opciones Avanzadas. Los eventos registrados por el

sistema ultrasónico incluyen: Pérdida de eco, señal del transductor y término del

intervalo de retardo del RS485.

_Pérdida de eco_

Es normal que el equipo informe pérdida temporal de eco debido a las condiciones

ambientales mencionadas anteriormente. El equipo SIGMA 980 determinará si la

intensidad del sonido está bajo los valores recomendados y automáticamente

iniciará mediciones para entregar una lectura exacta. Si la pérdida de eco

sobrepasa las 2 por hora, se debe revisar las condiciones del lugar de muestreo

_Manual de Operación y Mantención Sigma 980-1_

34

para confirmar si el problema ha sido provocado por la luz solar o golpes de calor

provocados por la interface de condiciones del agua.

_Señales del Transductor_

Las señales del transductor pueden ocurrir si el sensor está operando dentro de la

banda muerta. La señal del transductor se produce cuando éste no ha podido

finalizar la transmisión de una pulsación de sonido cuando retornó el eco. Las

señales del transductor pueden ser eliminadas permitiendo una distancia

suficiente entre el sensor y el objetivo.

_Intervalo RS485_

Este autodiagnóstico de verificación realiza pruebas para confirmar la integridad

de los cables para las conexiones de los sensores ultrasónicos remotos.

_Radiación Solar_

La lectura del visor de cristal líquido se puede dificultar si el medidor está instalado

con el visor mirando en forma directa hacia la luz solar . Debido a esto último,

se recomienda en lo posible realizar la instalación del medidor lejos del alcance

de la luz del sol. Más aún, si se presentan condiciones de radiación ecuatorial es

recomendable mantener la cubierta protectora cerrada hasta que el muestreo haya

finalizado para prolongar la vida útil del visor y el teclado.

_Manual de Operación y Mantención Sigma 980-1_

35

**ELECCION DEL SITIO DE MUESTREO**

##### IMPORTANTE:

**La correcta elección del sitio de muestreo es decisiva para obtener un**

**óptimo monitoreo de velocidad.**

Para obtener un muestreo libre de errores y un funcionamiento eficaz del equipo

SIGMA 980 recomendamos seguir las indicaciones detalladas a continuación.

**Christian Doppler (1903 -1853)**

El llamado Efecto Doppler lleva ese nombre gracias a Christian Doppler, quien

describió el cambio aparente que se produce en la frecuencia de las ondas de

sonido cuando la fuente y el observador están en movimiento relativo con respecto

al otro, haciendo que la frecuencia se intensifique cuando la fuente y el observador

se aproximan y que disminuya cuando se distancian.

Se recomienda la elección de un terreno de muestreo con un flujo de

características normales, en lo posible libre de turbulencias. Las turbulencias

pueden dificultar la detección del promedio de velocidad del flujo del caudal. Los

obstáculos, caídas verticales de agua, torceduras y codos en las tuberías pueden

provocar algún grado de turbulencia limitando la capacidad de detectar la

velocidad en forma exacta.

_Manual de Operación y Mantención Sigma 980-1_

36

**RECOMENDACIONES PARA LA UBICACIÓN DE LOS SENSORES EN**

**LUGARES DE MUESTREO DE CARACTERISTICAS APROPIADAS.**

_Desembocaduras_

Ubique el sensor a por lo menos 5x del nivel máximo de caudal esperado desde

la desembocadura.

_Caídas Verticales en el Piso del Canal_

Ubique el sensor a por lo menos 5x del nivel máximo de aguas-arriba esperado

desde la caida vertical.

Ubique el sensor a por lo menos 10x del nivel máximo de aguas-abajo esperado

desde la caida vertical.

_Codos, Curvas Cerradas y Conexiones “Y”_

Ubique el sensor a por lo menos 5x del nivel máximo de aguas-arriba esperado

desde conexión “Y”.

Ubique el sensor a por lo menos 10x del nivel máximo de aguas-abajo esperado

desde la desembocadura.

**BANDAS DE MONTAJE DEL SENSOR**

Las Bandas de Montaje y Anillos de Montaje de Sensores SIGMA están diseñados

para instalar los sensores de Velocidad y Sondas Sumergidas de Velocidad en

tuberías circulares. Las Bandas de Montaje tienen incorporados broches de

presión de variados tamaños y son de fácil ensamblaje en terreno.

_Manual de Operación y Mantención Sigma 980-1_

37

Los Anillos de Montaje SIGMA vienen pre-perforados para un montaje directo del

sensor al anillo.

**IMPORTANTE:**

Asegúrese de que la instalación de las bandas y anillos se realice tan pronto sea

posible para evitar bajas en el caudal o turbulencias al final de la tubería.

_Manual de Operación y Mantención Sigma 980-1_

38

**Enfrentando Lugares Difíciles**

Algunos sitios suelen ser más complicados para el monitor, debido a las

condiciones deficientes del terreno (Ver instalación se sensor de Area/velocidad

mencionada anteriormente). El sentido de las partículas del flujo del caudal así

como la velocidad de éstas influyen en la recepción de las señales de la sonda. Si

existiera una turbulencia excesiva cerca del lugar de medición ésta podría dificultar

que la sonda determine el promedio de velocidad de caudal. Los equipos SIGMA

poseen varias ventajas incomparables para ayudar a solucionar estos problemas

de terreno.

**Velocidad de Dirección**

Al programar las sondas de velocidad se debe seleccionar la opción Velocidad de

Dirección, allí existen tres opciones: Aguas-arriba (normal), Aguas-abajo y

siempre positivo.

**Aguas-arriba (Normal)**

Esta opción se utiliza para los lugares de medición con un promedio de velocidad

consistente y con un nivel de turbulencia medio o bajo. El flujo del caudal debería

idealmente correr en forma relativamente recta por el lugar de monitoreo.

Instale la sonda en la tubería, mirando hacia el flujo, de manera que el flujo entre

en el área de medición.

_Manual de Operación y Mantención Sigma 980-1_

39

**Aguas-abajo**

Esta opción permite localizar el sensor en el sector aguas-abajo del sitio de

medición (donde el flujo del caudal sale), coloque la sonda en la opción aguas

debajo como se hizo anteriormente con la opción aguas-arriba (normal).

Esta opción es muy útil en lugares donde existe más de un flujo de caudal simple

y en caso de que se desee medir el flujo combinado de todo el caudal con un

mismo sector de salida.

Ubique la sonda hacia atrás (ver figura), de esta forma se podrá leer en forma

opuesta al flujo de caudal a monitorear. Cuando programe la medición realícelo

seleccionando la opción aguas abajo, de esta forma el equipo registrará

electrónicamente la señal de medición en forma inversa para mostrar el sentido

del flujo actual.

**Siempre Positivo**

Las condiciones de turbulencia extrema pueden hacer más difícil la detección

apropiada del sentido del flujo debido a la acción de mezclado que producen las

aguas muy turbulentas. Haciendo rebotar las partículas dentro del flujo

(especialmente en la superficie del caudal), pueden ser lanzadas violentamente

en diferentes direcciones al mismo tiempo, incluso aunque el volumen del caudal

se mueva en la misma dirección. La magnitud de la velocidad en estos casos es

habitualmente consistente, no obstante la acción que proviene de las partículas

mueve el flujo en dirección positiva (la misma dirección que el flujo del caudal), a

su vez mezclan las partículas que vienen en sentido negativo (opuesto a la

dirección del flujo del caudal), lo que ocasiona dificultades para determinar la

dirección del flujo.

_Manual de Operación y Mantención Sigma 980-1_

40

El seleccionar la opción Siempre positivo para ejecutar la programación, provoca

que todas las lecturas sean almacenadas como positivas, sin relación con la

dirección de la señal de medición. Esta opción no debiera seleccionarse para

lugares donde los flujos son normalmente negativos, como ocurre con los efectos

de las mareas en las desembocaduras del océano.

**Velocidad de Corte / Velocidad de Omisión**

La Velocidad de Corte compensa velocidades muy bajas y aguas demasiado

limpias en caso de que se presenten en los lugares de muestreo. Esta

combinación de condiciones únicas complica el monitoreo, debido a que el agua

demasiado limpia puede contener pocas partículas reflectantes, y las velocidades

muy bajas por lo general implican que existe poca o casi ninguna turbulencia

adicional a las burbujas de aire que son arrastradas al flujo del caudal (lo que

también contribuye a la formación de buenos objetivos reflectantes).

El sistema de velocidad de corte permite ingresar el un valor de velocidad por

defecto, que se activa cuando se alcanza el punto de fijación del sistema de

Velocidad de corte. El equipo SIGMA 980 mantiene el valor por defecto cuando se

presenta una velocidad de valor inferior, en lugar de informar muestras de

velocidad erróneas.

_Consejos Importantes para la instalación del Sensor._

- No instale más de una sonda a la vez en tuberías de diámetro inferior a 24

pulgadas (61 cm). La Instalación de varias sondas a la vez puede ocasionar

turbulencias y/o acelerar los flujos cercanos a las sondas lo que afectaría las

mediciones de cada una de ellas obteniendo velocidades falsas o provocando

resultados cero en los registros.

_Manual de Operación y Mantención Sigma 980-1_

41

Instale el sensor lo más cerca posible del fondo de la tubería para obtener una

medición más exacta de niveles y velocidades bajas.

No monitorear los flujos del pozo en forma directa, ya que se podrían ver

afectados los resultados de las mediciones de profundidad, además de

provocar turbulencias entre el canal y el fondo. La posición más óptima es de

3 a 5 veces el diámetro/altura del desagüe aguas arriba desde el fondo.

- Realice el monitoreo en sitios lo más alejados posible de las convergencias de

flujo para evitar la interferencia entre flujos combinados.

Evite realizar mediciones en lugares que tengan obstáculos (como rocas,

piedras, uniones de cañerías, válvulas, etc.), frente a la instalación de la sonda

especialmente en las tuberías de entre 2 y 4 pulgadas de diámetro, ya que

estas podrían contribuir a las turbulencias y generar flujos de altas velocidades

en el sector más próximo a la obstrucción.

Evite los sitios que tengan un movimiento de flujo lento, debido a que éstos

facilitan la acumulación de barro y sedimento en el fondo del canal. El exceso

de sedimentación acumulada alrededor de la sonda puede provocar la

inhibición de la señal doppler y disminuir la exactitud de las mediciones, así

como también afectar la exactitud en las mediciones de profundidad.

- Evite los sitios que tengan flujos rápidos y profundos debido a que éstos pueden

hacer la instalación de la sonda difícil y/o peligrosa.

Evite los sitios con altas velocidades y poca profundidad, ya que el rociado

violento de agua y la turbulencia excesiva pueden afectar las mediciones de la

sonda obteniendo datos inexactos.

_Manual de Operación y Mantención Sigma 980-1_

42

### Sonda Sumergida de Velocidad

**Principio de Operación**

La Sonda Sumergida de Velocidad SIGMA 980 mide la velocidad para calcular

flujos en canales abiertos con el sistema de medición Doppler. Una pequeña

sonda que incorpora un transductor y un sensor de velocidad que se ajustan al

flujo del caudal. El equipo SIGMA 980 realiza la lectura de la presión del agua y

convierte estas señales en unidades de nivel. El equipo SIGMA 980, además

calcula la zona húmeda del flujo del caudal considerando por completo la forma de

éste. El área húmeda se multiplica por la velocidad detectada en el flujo.

La sección de la sonda sumergida de velocidad que se sume en el agua, utiliza un

transductor de presión para medir la profundidad del agua en que está inmerso el

sensor. El transductor de presión contiene un diafragma que entra en contacto

con el líquido. La cantidad de desviación detectada por el diafragma es

proporcional a la presión ejercida contra el diafragma, la que a su vez es

proporcional a la profundidad del agua en que se encuentra la sonda.

_**El desecante debe ser cambiado cuando éste se torna de color rosado, en**_

_**ese momento el desecante ya ha perdido sus propiedades absorbentes de**_

_**humedad. La sonda puede sufrir graves daños si el desecante no se**_

_**mantiene en forma apropiada.**_

Asegúrese de que el tubo de vinil está debidamente conectado a las dos

fijaciones durante la instalación o limpieza de la sonda, de lo contrario podría

permitir el paso de flujo y humedad o bloquear la presión de los transductores del

_Manual de Operación y Mantención Sigma 980-1_

43

puerto de referencia. Esto podría provocar lecturas erróneas y podría acarrear

problemas de falla en la sonda.

Cuando reemplace el desecante asegurese de que los o-rings estén libres de

suciedad antes de reinstalarlos al final de la tapa.

Remueva la tapa inferior para reemplazar el desecante. La tapa se tira con un

leve giro alternativo.

**Se recomienda que durante la instalación del desecante se ubique la sonda**

**de manera adecuada para evitar que el cartucho de desecante se caiga o se**

**derrame su contenido.**

**El cartucho de desecante está diseñado con un filtro hidrofóbico en la tapa**

**inferior. Cabe señalar que este accesorio no es indispensable para la**

**operación del sensor. Sin embargo se ha implementado con la finalidad de**

**proteger el filtro de la grasa incorporada al sensor durante la inmersión o**

**condiciones de sobrecarga.**

_Manual de Operación y Mantención Sigma 980-1_

44

### Fijación del Nivel del Caudal

Cada vez que el sensor de nivel se instala o se traslada se debe realizar una

medición física del nivel del caudal e ingresar la cifra al equipo SIGMA 980 usando

el menú Ajuste de Nivel. Presionar la tecla de Ajuste de Nivel que se encuentra en

el panel frontal del equipo para entrar en el menú de Ajuste de Nivel.

Para ejecutar esta función, mida cuidadosamente desde la superficie del agua

hasta el fondo de la tubería (‘A como muestra la figura), luego reste esta cifra al

diámetro de la tubería (‘C como muestra la figura). Este método no causa

perturbación en el flujo del caudal, lo contrario provocaría efectos en la medición.

(mantenga su huincha de medir o regla limpia). Repetir este proceso para todas

las instalaciones de sensores de nivel.

**CONEXIÒN DE CABLES DEL CONTROLADOR SIGMA 980**

**120-VAC y 230-VAC (europeos) Las conexiones del terminal de bloqueo**

**principal del controlador.**

#### ADVERTENCIA

**Los terminales 120-VAC ó 230-VAC presentan peligro de descargas**

**eléctricas que pueden tener serios daños personales o incluso la muerte.**

**Tome las precauciones necesarias al entrar en contacto con estos**

**terminales y al conectarlos a la red de energía para prevenir accidentes.**

#### IMPORTANTE

**La identificación del terminal impresa en la placa adherida a cada equipo**

**980, o la pieza reemplazable del tablero de circuitos prevalece en todos los**

**casos.**

_Manual de Operación y Mantención Sigma 980-1_

45

**Notas**

Para la conexión de dispositivos externos se han habilitado entradas de poder

de +14VDC a +22VDC. El total de corriente disponible para ambos enchufes

combinados es de 500 m ADC (máximo).

El color de referencia es aplicable a todas las instalaciones estándar de

cableado de equipos y accesorios SIGMA.

### Canalización de cableado

El gabinete del equipo SIGMA 980 contiene ocho conductos de cableado ubicados

a lo largo de la orilla del fondo del gabinete. Los dos conductos de 1" NPT y seis

de 1/2" NPT proporcionan un fácil acceso a todos los cables de energía, control

y comunicaciones de la sonda.

Se recomienda que la unión de las tres piezas del conducto (como se muestra en

la ilustración), cuando se utiliza el controlador unido a un conducto rígido. Esto

permite una remoción más fácil del controlador.

##### Rápida conexión de adaptadores para conductos

Existen adaptadores para conductos y receptáculos de agua incorporados al

equipo SIGMA 980 . Estos convierten las fijaciones de los conductos en dos

enchufes de rápida desconexión y receptores de configuración. Estos permiten

una rápida conexión del campo a un computador Laptop u otros sensores. Los

receptores vienen con una capa protectora de goma en la tapa.

_Manual de Operación y Mantención Sigma 980-1_

46

#### DESCRIPCIONES DE LOS TERMINALES DE SEÑALES DE BLOQUEO

**ENTRADA PRINCIPAL DE ENERGIA A/C**

### _ATENCION_ PELIGRO ALTO VOLTAJE

**DESCONECTE LA ENERGÍA PRINCIPAL Y DESENCHUFE LOS CABLES DE**

**CONTACTO PARA DESCONECTAR LAS ENTRADAS DE ENERGÍA ANTES DE**

**PROCEDER A LA REVISIÓN DEL DISPOSITIVO DE LO CONTRARIO PODRÍA**

**CAUSAR GOLPES DE CORRIENTE, QUEMADURAS Y LA MUERTE.**

**LOS TERMINALES DE ENERGÍA PROVEERAN UNA CORRIENTE**

**COMBINADA DE +14 A +22 VOLTIOS DC A 0.5A**

**Importante:**

**Este aviso se encuentra también dentro del sector en que se ubica el**

**controlador. Antes de abrir el gabinete, asegúrese de dejar todos los**

**circuitos desconectados o desenchufados, o bloqueados.**

Existe una etiqueta adhesiva en el equipo SIGMA 980 que identifica el correcto

suministro de energía para cada medidor en particular. Conecte su equipo con el

nivel de voltaje requerido según cada número de partida detallado en la parte de

Especificaciones de Diseño de este Manual.

_Manual de Operación y Mantención Sigma 980-1_

47

Con el gabinete del Medidor de Flujo abierto y las referida conexiones del terminal

de bloqueo que se encuentran al interior conecte las líneas de energía como se

indica.

La línea interna de energía A/C está provista de un fusible de 1/2 amper. La

energía A/C individual debería estar provista de una vía con circuito de seguridad

conectado a tierra.

### Relés (4)

Los contactos de Relés son del tipo "Form C" y tienen una frecuencia de 10

amperes @ 120 VAC o 5 amperes @ 250 VAC. Los contactos Normalmente

abierto (NA), Normalmente cerrado (NC), se encuentran disponibles. Los

contactos Normalmente abiertos se cierran al activarse la alarma. Los contactos

Normalmente Cerrados se abren a la activación de la alarma.

### Conexiones de corriente de 4-20 mA

Existen dos salidas de 4-20 mA en cada canal en forma independiente (nivel, flujo,

pH, etc...). Ver el Capítulo de Programación para mayores detalles a cerca de la

asignación de canales.

La resistencia máxima de carga de cada canal es de 1000 ohms

La salida de voltaje es de 24 VDC sin carga

Estas salidas están aisladas entre el medidor de flujo y la salida de 4-20 mA a

2500 VAC y entre las dos salidas 4-20mA a 1500 VAC.

_Manual de Operación y Mantención Sigma 980-1_

48

**Totalizador Mecánico**

La opción de seis dígitos del totalizador mecánico (PN8560), es de conducción

solenoide y no es reseteable . Se convierte en un panel NEMA 4X /incluye

montaje en panel mural.

_Manual de Operación y Mantención Sigma 980-1_

49

**MUESTREADOR**

Esta función permite que la interface del medidor de flujo SIGMA 980 trabaje en conjunto con un muestreador de aguas

residuales SIGMA.

|SEÑAL|DESCRIPCION|COLOR<br>CABLE SIGMA|
|---|---|---|
|Partida|Se usa para "activar" el muestreador de aguas residuales cuando hay un punto de fijación, de manera<br>que comience su programa de muestreo. Esta línea es flotante y se activa a tierra (mediante un<br>transistor), para completar el período en que se produce el punto de fijación. +14 a 22VDC @ 100 mA<br>(máx.). El muestreador y el medidor de flujo deben compartir una misma señal a tierra.|Negro|
|Salida de<br>Pulso|Señal del muestreador que se usa seleccionando un monto de flujo acumulado. La salida de corriente de<br>100 m ADC (máx.) @ + 12vdc, la duración del pulso es de 500 ms. El muestreador y el medidor de flujo<br>deben compartir una misma señal a tierra.|Amarillo|
|Entrada<br>Número<br>de<br>Botella|Esta señal se recibe de un muestreador de aguas residuales SIGMA y se usa en conjunto con la señal de<br>Entrada de Evento. Este indica al medidor de flujo cuál botella se usó al tomar la muestra.<br>Esta información aparecerá en la impresión de datos (en la sección "Hora y fecha de muestra") cuando<br>se descarga usando la Unidad de Transferencia de datos o el Software Sigma.|Verde|
|Entrada<br>de<br>Eventos|Esta señal se recibe desde un muestreador de aguas residuales SIGMA y significa que se ha recogido<br>una muestra. La información de la muestra aparecerá en la impresión de datos cuando se descargue la<br>información mediante la Unidad de Transferencia de Datos o el Software SIGMA.|Rojo|
|Tierra|Común|Azul|

_Manual de Operación y Mantención Sigma 980-1_

50

### RS485

La interfase RS485 se usa para comunicarse con las opciones del Sensor Remoto

SIGMA. Este puerto usa un protocolo de comunicaciones de solo debería ser

usado por interfases remotas SIGMA.

### RS232

El puerto serial RS232 se usa para comunicarse con el medidor de flujo desde un

dispositivo externo tal como una Unidad de Trasferencia de Datos SIGMA (DTU) o

la conexión directa del serial a un computador personal que utilice el Software

SIGMA.

Este puerto se puede configurar para comunicarse a 1200, 2400, 4800, 9600 ó

19200 baud.

Nota: Las conexiones de energía de +14VDC a +22VDC (enchufes de 31 y 39),

son proporcionados para la conexión de dispositivos externos. La corriente total

disponible de ambos enchufes combinados es de 500m ADC (máx.).

Los cables RS232 están habitualmente limitados a 50 pies pero se pueden instalar

con éxito a sobre 500 pies. En condiciones de ruido bajo. En general, como el

rango de baud va decreciendo, el largo del cable puede también ir disminuyendo.

Manual de Operación y Mantención Sigma 980-1

51

#### Sensor Ultrasónico de Nivel

Esta entrada es para la instalación del sensor de nivel ultrasónico Sigma de 50

kHz (PN4030).

Para mayores detalles a cerca de la instalación del sensor ultrasónico de nivel

ver la sección titulada "Instalación del Sensor Ultrasónico", al comienzo de este

capítulo.

Tipo de cable: RG-62 A/U 93 ohm coaxial

Largo máximo del cable: 850 pies (259 m.)

Conectar la sonda de Temperatura RTD a los conectores de 50 y 53.

Esta parte de la caja de entradas de pH/ORP se usa para la opción de sonda de

temperatura de RTD estándar . Esta entrada solo puede ser usada si el pH o ORP

no están en uso, debido a que éstos comparten el mismo circuito de temperatura.

### Instalación de la Sonda de pH

IMPORTANTE: Ubicar la sonda de pH de manera que siempre permanezca

húmeda. Las sondas de pH pueden dañarse gravemente o pueden destruirse

completamente si se permite que se sequen. La sonda debe estar completamente

sumergida para funcionar sin dañarse.

La sonda debe ser instalada usando la tubería NPT de 3/4" incorporada.

Manual de Operación y Mantención Sigma 980-1

52

### Cableado de la Sonda de pH

A continuación se muestra el interior de la caja de pre-amplificación con el

cableado de la sonda de pH (ver figura). Hasta que la sonda de pH registre los

datos se debe compensar la variación de la temperatura. Hay un sensor de

temperatura incorporado a cada electrodo de pH.

Interfase de pre-amplificación de la caja de conexión P.N. 3323

La sonda de pH consta de dos set de cables, tres cables para la sonda de pH y

dos para la sonda de temperatura, como se muestra en la figura anterior. Se debe

juntar el cable transparente con el tornillo al terminal marcado "Vidrio" (Glass).

### Entrada de Aguas Lluvias

Esta entrada está diseñada para instalar un balde receptor externo de aguas

lluvias tal como el receptor de aguas lluvias American Sigma Modelo #2149. A

medida que se junta el agua lluvia en el embudo de 8 pulgadas (20.32 cm) de

diámetro, es enviado directo a uno de los costados de los baldes de inclinación. A

medida que cada balde se llena cada balde instalado se rebalsa y vací su

contenido el fondo del recolector de aguas lluvias . La inclinación de cada balde

produce solo un contacto de cierre en el medidor de lluvia, el que retorna enviando

pulsaciones de 12 VDC en un conector C al conector del colector de aguas lluvias.

Cada pulsación representa .01 pulgada (0.254 mm), de lluvia.

Manual de Operación y Mantención Sigma 980-1

53

### Módem

Esta conexión es para la interconexión del módem interno opcional con una línea

telefónica estándar

El módem del equipo SIGMA 980 posee fusibles de auto-reinicio en sus líneas

para realizar una interrupción cuando hay una alza de energía antes de que ocurra

algún daño al equipo. Los fusibles re-inician el equipo automáticamente mientras

se restauran las comunicaciones sin necesidad de solicitar el servicio.

### Señales sumergidas de Nivel

La identificación del terminal y el nombre de las señales se entrega en la tabla de

las conexiones de bloqueo del terminal que se detalla al principio de este capítulo.

La entrada de señales del sensor de Area Velocidad consta de señales que se

transmiten y se reciben y un conductor de referencia para cada una de ellas. Una

sonda sumergida de nivel comunica a los dos conductores. Un Voltaje DC de 12

22 voltios es suministrado a través de dos terminales en el terminal de bloqueo

de Area Velocidad.

Manual de Operación y Mantención Sigma 980-1

54

### CAPITULO 3 PROGRAMACION

El equipo SIGMA 980 es de fácil programación para cumplir con las necesidades

específicas del usuario. "Programación ", significa responder preguntas simples

respecto de los dispositivos primarios, unidades de medición y otras funciones que

se hayan seleccionado. Cuando se realiza una programación, se debe "ejecutar"

las selecciones de la programa que se ha realizado. Presionando la tecla de

función EJECUTAR/DETENER para ejecutar un programa o volver a tomar el que

está detenido momentáneamente. Para detener el programa se debe presionar la

misma tecla.

Cuando un programa está en ejecución, se activan los siguientes ítemes (si han

sido habilitados durante la programación:

Registro de Datos

- Salidas 4-20 mA

- Control de Muestreo

- Revisión de Alarma

**Cuando un programa se detiene ocurre lo siguiente:**

El registro de datos continua con el último valor registrado

Las salidas 4-20 mA permanecen sin cambios

- El control de muestreo se deshabilita

- Se deshabilita la revisión de la alarma

Manual de Operación y Mantención Sigma 980-1

55

**Cuando un programa está Completo o Listo para comenzar sucede lo**

**siguiente:**

No hay registro de datos

- Las salidas 4-20 mA mantienen su último valor

No hay interconexión de muestreo

No hay revisión de alarma

**El estado del programa cambia cuando el Programa está completo.**

Un programa ha estado detenido por más de tres horas

Se completa la memoria de registro.

Si un programa se ha detenido (y no se hizo cambios a la definición del programa

mientras se detuvo), presionar la tecla EJECUTAR para que el programa solicite

confirmación si desea reiniciar el programa previamente iniciado (y retener todos

los datos registrados), o comenzar desde el Principio (y borrar todos los datos

registrados).

IMPORTANTE:

Cuando seleccione "Comenzar desde el Principio", todos los datos almacenados

serán borrados de la memoria. Si se requiere guardar los datos registrados

asegúrese de que los datos han sido guardados en su DTU o computador

personal antes de presionar "Comenzar desde el Principio". Una vez que los datos

se han borrado no podrá recuperarlos.

Manual de Operación y Mantención Sigma 980-1

56

**DESPLIEGUE DE FUNCIONES Y CONTROLES EN EL PANEL FRONTAL**

El equipo SIGMA 980 utiliza un panel frontal para desplegar los programas de

medición de flujo. Este panel consta de un teclado y un visor de cristal Líquido

(LCD).

**TECLADO**

Las teclas (soft keys) están ubicadas a la izquierda y a la derecha del panel.

Estas no tienen etiquetas. Se llaman "Soft keys" porque su función está

determinada por un software. La información que aparece en el visor de cristal

líquido informa la función que ejecuta cada una de las teclas. Las funciones

cambian dependiendo del menú que se seleccione. Las etiquetas o funciones de

cada tecla aparecen en el visor y apuntan con una línea recta a la tecla que debe

ser presionada para cada acción, como se muestra en el dibujo. En algunos

casos durante los pasos de programación el equipo solicitará seleccionar un ítem

de cada lista. Las teclas de función de la derecha cambiarán presionando las

flechas que indican "arriba" y "abajo". Estas permiten subir o bajar en la lista de

selecciones. Una vez que se elija la función ésta se iluminará, presionando

"seleccionar" el ítem quedará fijado.

Manual de Operación y Mantención Sigma 980-1

57

**Menú Principal**

Presionando la tecla "Menú Principal" inmediatamente aparecerá éste en el visor.

El menú principal es el inicio para cualquier punto de programación. La tecla del

"Menú Principal" debe ser presionada todas las veces que requiera el programa.

En caso de que alguna opción no sea aceptada el equipo volverá al Menú

Principal.

**Tecla de Ajuste de Nivel**

Presionando la tecla "Ajuste de Nivel" el equipo estará habilitado para ajustar el

nivel del medidor de flujo para registrar combinando el nivel del caudal del canal

a medir. Se debe tomar la medida física del nivel del canal cuidadosamente (se

refiere al nivel que contribuye al flujo), e ingresar el valor. Es importante

asegurarse de que la medición haya sido correcta realizando la prueba dos veces

antes de dejar el lugar de medición para obtener una medición exacta.

El nivel del caudal registrado se muestra en el visor para su información.

IMPORTANTE:

El nivel registrado debe ser revisado y ajustado, si se requiere cuando se hayan

hecho cambios en el controlador o cuando se haya cambiado la ubicación del

sensor de nivel.

Manual de Operación y Mantención Sigma 980-1

58

**Barras de Estado**

A lo largo del extremo inferior del visor hay una banda negra llamada Barra de

Estado, esta barra indica la hora y fecha en la esquina superior izquierda del visor

y el nombre del menú que está en ejecución actualmente en la esquina superior

derecha. A lo largo del borde inferior del visor hay otra barra de estado cuya

función cambia dependiendo de la función que se esté ejecutando.

La barra de estado que se encuentra en la esquina inferior izquierda, indica si el

programa está completo, ejecutándose, detenido, o listo para comenzar. Si no es

necesaria durante las etapas de programación ésta desaparecerá para permitir

desplegar una mayor cantidad de información en el visor.

En la esquina inferior derecha parpadeará cualquier condición del sistema de

alarma, tales como: alarma del transductor, pérdida del eco, etc. En el Capítulo

Cuatro - Programación - en la Sección Alarmas encontrará una lista de posibles

alarmas.

La barra de estado también ayuda a recopilar la información válida cuando se

completan ciertas informaciones de programación. Por ejemplo, cuando se

selecciona una unidad de medición desde el Menú Unidades de Nivel, la barra de

estado indica que las elecciones válidas son: cms, pies, pulgadas o metros).

**Luces de Estado de las Alarmas**

La condición de cada relé de alarma interna se muestra mediante las Luces de

Estado de las Alarmas. Las luces de estado parpadean cuando se activan las

alarmas mediante el cierre de los relés.

Manual de Operación y Mantención Sigma 980-1

59

**Teclado Numérico**

El teclado numérico con dígitos del 1 al 9 y teclas +, - y decimal. Está habilitado

para permitir ingresar cambios numéricos a entradas tales como: fecha, hora,

intervalos, etc.

Cuando se entra o se cambia un dato numérico, se tiene la oportunidad de

seleccionar diversos números en el visor o borrar los ya existentes y digitar otros

nuevos. Cuando se reemplazan los números existentes, cada número a

reemplazar parpadea intermitentemente antes de ser reemplazado. En forma

alternativa se puede borrar todos los números que parpadean en el visor

presionando la tecla "Borrar", para luego digitar los nuevos números en cada

espacio parpadeante. Además, el teclado numérico permite presionar otras

teclas en instancias en que se está presionando cualquier tecla de función.

**Menú Principal**

Al conectar el medidor de flujo a la fuente de poder C/A y encenderlo, se ejecuta

un diagnóstico de auto-análisis que despliega el último menú mostrado antes de

que la unidad fuera apagada. Presionando la tecla Menú Principal se podrá

desplegar el Menú Principal en el visor nuevamente. El Menú Principal es el

punto de partida para todas las operaciones de programación que se desee

ejecutar en el medidor de flujo SIGMA 980.

Manual de Operación y Mantención Sigma 980-1

60

En el Menú Principal se presentan las siguientes funciones:

- Despliegue de Datos - Muestra los gráficos y tablas con la información

registrada en el equipo.

- Programación - Menú de programación básica

- Opciones - Menús de programación avanzada

- Estado - Despliegue de la hora y fecha actual

**Menú de Despliegue de Datos**

La tecla de Despliegue de Datos permite ver los datos en varias formas, se

pueden ver los datos dispuestos en una tabla o desplegados en un gráfico, como

se muestra en la figura.

Además, los datos se pueden presentar en informes tabulados, en los que se

puede visualizar los datos desde el principio hasta el final, o desde un punto

específico del muestreo. Cuando se visualiza un gráfico, se puede desplegar un

período de 24 horas, y mediante un zoom fijado en una porción específica del

período de 24 horas se puede ver con mayor detalle un punto detallado del

muestreo, o es posible centrarse en un punto de tiempo específico dentro del

gráfico.

Presionando la tecla Despliegue de Datos desde el Menú Principal, es posible

desplegar una lista de los canales registrados, así como también, un historial de

muestreo (si se conecta el equipo a un muestreador de aguas residuales SIGMA).

Manual de Operación y Mantención Sigma 980-1

61

Al seleccionar el canal deseado en el menú de opciones mediante las flechas

arriba y abajo éste se iluminará para posteriormente fijarlo presionando la tecla

Seleccionar.

CONSEJO:

Antes de visualizar los datos muestreados en un gráfico es importante guardar

previamente los datos en el medidor de flujo SIGMA 980.

IMPORTANTE:

Solo los canales que han sido grabados están disponibles en la lista de selección.

Ver la sección titulada Almacenamiento de Datos para mayor información a cerca

de cómo disponer de los datos guardados.

Seleccionar el formato en que se requiera visualizar los datos: tabla, gráfico,

resumen, etc... presionando la tecla Seleccionar una vez iluminada la elección.

(ver figura).

**Despliegue de Datos en una Tabla**

Seleccionar la opción Desplegar Tabla desde el menú que muestra la figura

anterior, que contiene las siguientes opciones:

Ver desde el Principio

- Ver desde el Final

- Ver desde Fecha/ Hora

Manual de Operación y Mantención Sigma 980-1

62

_**Ver desde el principio:**_

Seleccionando la opción Ver desde el Principio se visualiza los datos del canal

seleccionado comenzando por el primer dato ingresado en la memoria del equipo.

Utilizar las flechas arriba y abajo para situarse en el sitio deseado. (ver figura)

Presionando la tecla Volver se vuelve nuevamente al Menú previo.

_**Ver desde el final**_

Al presionar la tecla Ver desde el final se despliegan los datos del canal

seleccionado para visualizar desde el último dato almacenado en la memoria del

equipo.

_**Ver desde Fecha/Hora**_

Esta opción permite ver los datos por fecha u hora de ingreso de los datos del

canal seleccionado a elección del usuario. Al seleccionar Ver desde Fecha/Hora,

se visualizará en el visor los datos que se desee de acuerdo a la fecha u hora

ingresada en la opción mediante el teclado numérico. El teclado además le

permite seleccionar mes y cambiar de a.m. a p.m.

Después de completar la fecha y hora deseados presionar la tecla Aceptar,

entonces el equipo SIGMA 980 desplegará una tabla comenzando por la fecha y

hora estipulada por el usuario. Las flechas arriba y abajo, permiten avanzar o

retroceder en la pantalla a través de los datos visualizados. Al presionar la tecla

Volver, se regresa al menú anterior.

Manual de Operación y Mantención Sigma 980-1

63

**Despliegue de Datos en Gráfico**

Por medio de la selección Despliegue de Datos en Gráfico es posible visualizar

los datos ingresados en tres tipos de gráfico diferentes:

- Gráfico del Día

Gráfico en un Punto del Tiempo

- Gráfico Parcial del Día

_**Gráfico del Día**_

La selección del Gráfico del Día permite desplegar los datos de una fecha

específica. Los datos de dicha fecha se grafican desde la media noche del día

anterior hasta la media noche del día siguiente.

Ingresar la fecha deseada mediante el uso del teclado numérico y luego presionar

Aceptar con la tecla de programación para visualizar el gráfico de ese día.

_**Gráfico en un Punto del Tiempo**_

Al seleccionar Gráfico en un Punto del Tiempo, se puede desplegar los datos de

una fecha y hora determinadas. El gráfico comprende datos de tres horas antes

de esa misma fecha y los desplegará de manera que el centro del gráfico sea el

punto en el tiempo seleccionado.

Ingresar la fecha y hora deseada (mediante las teclas de programación dispuestas

para cambiar de a.m. a p.m. y viceversa), y luego presione la tecla Aceptar para

visualizar el gráfico.

Manual de Operación y Mantención Sigma 980-1

64

_**Gráfico Parcial del Día**_

Al seleccionar la opción Gráfico Parcial del Día, se puede hacer un acercamiento

de una parte de los datos registrados.

Ingresar la hora y fecha de inicio deseada y la hora y fecha final, además de las

horas que se desea graficar. Las teclas de programación dispuestas para

cambiar de a.m. a p.m. y viceversa permiten además seleccionar el mes.

Presionar la tecla Aceptar para desplegar en un gráfico la porción de datos

ingresados.

**Cursor de Datos**

Como se muestra en la ilustración hay una línea vertical pespunteada en el centro

del gráfico visualizado, el Cursor de Datos puede deslizarse a la izquierda o a la

derecha mediante las flechas dispuestas para ello en el teclado numérico. La

fecha, la hora, los valores de los datos y las unidades de medición que se

encuentran en la intersección del Cursor de Datos se despliegan a través de la

parte superior del gráfico en la barra de estado.

_**Movimiento del Cursor con el Teclado Numérico**_

Además del uso de las teclas con flechas para mover el cursor, se puede utilizar el

Teclado Numérico para deslizar el cursor rápidamente a través del gráfico

desplegado en el visor. Desde la tecla cero hasta la nueve (0 - 9), representan un

porcentaje de una escala completa. Presionando un valor numérico desde el

teclado es posible deslizarse dentro del gráfico desplegado saltando de número en

número. Por ejemplo: si presiona 0 el cursor se moverá rápidamente hacia la

Manual de Operación y Mantención Sigma 980-1

65

izquierda hasta la posición 0 del gráfico, presionando la tecla 5 el cursor se

moverá hasta la mitad o el 50% del gráfico desplegado en el visor.

Presionando la tecla 9 el cursor se moverá hasta el final del gráfico o el 90% del

él.

De esta manera se puede mover rápidamente el cursor dentro del área de interés

dentro del gráfico. Además, del uso de las teclas numéricas de flechas izquierda

y derecha para situarse en el área de datos deseada.

_**Barra de Estado**_

Situada a través de la parte superior de cada gráfico, la barra de estado muestra

la fecha, hora, valor y unidad de medición para los datos que se encuentran en la

intersección del cursor. Mediante la ubicación del cursor en la Barra de Estado

es posible eliminar los ejes X o Y para permitir una visión más amplia del área

graficada.

_**Tecla Próximo Canal**_

Presionando la tecla Próximo Canal es posible ubicarse en la parte superior

izquierda del visor para que los datos del canal siguientes se desplieguen en la

pantalla (en forma de gráfico o tabla).

Por ejemplo, si el equipo SIGMA 980 almacena el nivel, flujo, pH y nivel

recientes, al presionar la tecla Próximo Canal será posible visualizar los datos en

un gráfico y si se presiona nuevamente la tecla Próximo Canal será posible

visualizar los datos de flujo, si se presiona nuevamente se visualizarán los datos

de nivel, etc., si se presiona nuevamente se vuelve al principio. De este modo es

posible seleccionar el período de interés y el ciclo que se requiere visualizar de

Manual de Operación y Mantención Sigma 980-1

66

cada canal para realizar una rápida sucesión para comparar los datos

desplegados.

Cada gráfico cubre un período de tiempo seleccionado previamente para

visualizar el gráfico inicial. Presionando la tecla Retornar podrá regresar un nivel

en el menú. Entonces es posible seleccionar un nuevo período de tiempo para

graficar.

**Notas Importantes a cerca de los Gráficos**

El equipo SIGMA 980 puede desplegar un gráfico que contenga un máximo de

180 puntos individuales. Debido a que en un período de 24 horas puede

contener tantos puntos como 1.440 (Considerando un minuto de intervalo de

grabación, leyendo uno cada un minuto), sería posible diagramar cada punto de

datos en el gráfico.

Esto significa que el total de puntos de datos para un período que está siendo

graficado se promedian a un máximo de 180 puntos requeridos por el gráfico.

Estos 180 puntos de datos son promediados posteriormente y desplegados en el

gráfico.

Cuando se grafica más de tres horas de datos (o más de 180 minutos), se debe

promediar los puntos de datos. Cuando se grafica un día parcial de tres horas o

menos, todos los puntos de datos se grafican sin promediarlos previamente.

Cuando se visualiza un gráfico que se ha promediado (cualquier gráfico de más de

180 puntos de datos), podría ser necesario hacer un acercamiento del área de

interés (usando la opción GRAFICO DE DIA PARCIAL), antes que todos los

puntos de datos individuales sean desplegados.

Manual de Operación y Mantención Sigma 980-1

67

**Despliegue de Resumen**

Al seleccionar la opción Despliegue de Resumen desde el menú de Despliegue

de Datos se puede seleccionar las siguientes opciones:

- Resumen Diario

Resumen por Hora

- Otro Intervalo

Se despliegan en el visor los valores Mínimo, máximo, promedio y totales según

se requiera.

_**Resumen Diario**_

Seleccionar la fecha de inicio para desplegar los datos. Esta será el primer punto

de dato mostrado en la tabla. Cada hilera representa un día de medianoche a

medianoche.

--DATE-- --MIN-- --MAX-- --PROMMAY12 12.123 29.832 20.977

MAY13 15.125 55.812 35.468

MAY14 10.526 18.139 14.332

Manual de Operación y Mantención Sigma 980-1

68

_**Resumen por Hora**_

Seleccionar la fecha y hora de inicio para desplegar los datos. Estas pueden ser

el primer punto de dato mostrado en la tabla. Cada hilera representa una hora,

desde el inicio de cada hora.

FECHA: 12-MAY-97

--TIME-- --MIN-- --MAX-- --PROM10:00am 12.123 29.832 20.977

11:00am 15.125 55.812 35.468

12:00am 10.526 18.139 14.332

_**Otro Intervalo**_

Seleccionar el número de minutos a resumir (desde uno a sesenta minutos), y el

inicio de tiempo y fecha para desplegar los datos. Esto debería ser el primer punto

de datos a mostrar en la tabla. Cada hilera representa un intervalo.

FECHA: 12-MAY-97

--DATE-- --MIN-- --MAX-- --PROM10:00am 12.123 29.832 20.977

10:05am 15.125 55.812 35.468

10:10am 10.526 18.139 14.332

Posteriormente el resumen de los intervalos será promediado. En otras palabras

el período comprendido entre las 10:00 a las 10:04 se muestra a las 10:00.

Manual de Operación y Mantención Sigma 980-1

69

**PANTALLA DE ESTADO**

En el Menú de Estado se encuentran las siguientes opciones:

DESPLIEGUE CORTO - Despliegue de los datos en tiempo real usando el

tamaño de carácter estándar 1/8 pulg. (3.2 mm)

DESPLIEGUE AMPLIO - Despliegue amplio de los datos en tiempo real, de

fácil lectura, usando el tamaño de carácter 1/2 pulgada (12.7 mm).

CONFIGURACIÒN AMPLIA - Configuración amplia de la Pantalla de Estado.

- RETORNAR - Retornar al menú anterior.

**Despliegue Corto de la Pantalla de Estado**

Las flechas de desplazamiento aparecerán cerca de las teclas del lado derecho si

existe más información disponible.

**Despliegue Amplio de la Pantalla de Estado**

Cuando el auto despliegue de la Pantalla de Estado está disponible, el

desplazamiento se ejecuta en forma automática si hay más de una página de

información de estado disponible.

Manual de Operación y Mantención Sigma 980-1

70

**Configuración Amplia del Menú de la Pantalla de Estado**

**Auto-Despliegue del Estado**

Cuando está habilitada esta opción, ésta realiza un amplio despliegue automático

del ciclo de todos los canales disponibles, cada 15 segundos, se despliegan dos

canales a la vez. Esta opción además hace que el despliegue (no importa en cuál

menú se esté), se convierta en un despliegue amplio de estado después de 30

segundos de inactividad. (sin que se presione alguna tecla).

**Despliegue del Totalizador**

La opción Despliegue del Totalizador al final del lado derecho de la Pantalla

amplia de estado (como se muestra en la figura anterior). El totalizador se

configura en el menú de Opciones Avanzadas descrito al final de este capítulo.

**Selección de Entradas**

Seleccionar los canales que se incluyen en el despliegue amplio de pantalla de

estado.

**MENU DE CONFIGURACION**

La configuración es el primer paso cuando se prepara el equipo SIGMA 980 para

su funcionamiento. Aquí es donde se le ingresa al Medidor de Flujo toda la

información que necesita para realizar las tareas básicas de medición de nivel y de

flujo.

Manual de Operación y Mantención Sigma 980-1

71

Antes que el medidor de flujo SIGMA 980 inicie su funcionamiento es importante

ingresar todos los detalles a cerca del lugar de muestreo (dispositivo primario), y

sus preferencias para el despliegue de las mediciones que se tomen. La primera

de las tres opciones son simplemente tres formas convenientes de ver la misma

información configurada y explicada en detalle en las siguientes secciones.

**Revisión de todos los Itemes.** Esta opción permite mirar pero no tocar. Es

posible mirar a través del programa de definición de CONFIGURACIÓN y OPCION

sin preocuparse de cambiar en forma accidental un parámetro importante. El uso

de esta selección permite verificar que el programa está configurado

correctamente antes de dejar el lugar de muestreo.

**Modificar Todos los Itemes.** Esta opción guía paso a paso todas las secuencias

del programa. Para una programación o para una instalación en un lugar nuevo,

esta selección es la más indicada. Con esta elección no se perderá ningún paso

importante para la programación del equipo.

**Modificar Temas Seleccionados** . Esta opción permite modificar un solo paso

del programa sin necesidad de buscar a través de todo el menú. Esta selección

es muy útil para aquellos usuarios con experiencia y que saben en forma exacta

cuáles son sus necesidades para realizar algún cambio y donde encontrarlo.

**LOGIN** . Esta opción permite grabar números de cuatro dígitos, con una memoria

automática de hora/fecha, en el almacenaje de eventos. Esto se realiza mediante

el ingreso de un número distintivo u otro identificador numérico, entonces es

posible deducir cuando el personal de servicio visita el lugar de muestreo.

**Revisión de Todos los Itemes**

Del Menú Principal:

Manual de Operación y Mantención Sigma 980-1

72

CONFIGURACIÓN: REVISIÓN DE TODOS LOS ITEMES

Esta opción permite revisar toda la configuración de la programación ingresada al

equipo para asegurarse de que todos los ítemes seleccionados han sido

ejecutados en la manera correcta. Es recomendable revisar siempre la

configuración en la pantalla antes de dejar el lugar de muestreo para asegurarse

de que los pasos se han seguido correctamente y que ninguno se ha perdido

durante la programación.

Todas las opciones de programación se despliegan en el visor, así como también

el estado de todos los canales de registro. Debido a que esta información puede

ocupar más de una pantalla, mediante la tecla flecha abajo se puede ver el resto

de la información desplegada en la lista de selecciones. Cuando se ilumine la

selección deseada se debe presionar la tecla Seleccionar para abrir el menú de

configuración de ese ítem.

A continuación de detalla una completa descripción paso a paso de la Modificación

de los Itemes Seleccionados y de la Modificación de Todos los Itemes desde la

lista de selecciones.

**Unidades de Flujo**

Del Menú Principal:
**CONFIGURACION:** **MODIFICAR LOS ITEMES SELECCIONADOS:**

**UNIDADES DE FLUJO**

Seleccionar las unidades de medida que se usarán cuando se desplieguen las
lecturas de flujo.

Estas unidades de flujo se usarán siempre que se lea un flujo desplegado o
registrado. Las diferentes unidades de flujo pueden ser seleccionadas en la
sección de programación de Circuito de Muestreo.

Manual de Operación y Mantención Sigma 980-1

73

Las Opciones son:

|GPS|GALONES POR SEGUNDO|CFC|PIES CUBICOS POR SEGUNDO|
|---|---|---|---|
|GPM|GALONES POR MINUTO|CFM|PIES CUBICOS POR MINUTO|
|GPH<br>|GALONES POR HORA<br>|CFH<br>|PIES CUBICOS POR HORA<br>|
|~~MGD~~<br>|~~MILLONES DE GALONES POR DIA~~<br>|~~CFD~~<br>|~~PIES CUBICOS POR DIA~~<br> <br>|
|~~LPS~~|~~LITROS POR SEGUNDO~~|~~CMS~~|~~METROS CUBICOS POR SEGUNDO~~|
|LPM<br>|LITROS POR MINUTO<br>|CMM<br>|METROS CUBICOS POR MINUTO<br>|
|~~LPH~~|~~LITROS POR HORA~~|~~CMH~~|~~METROS CUBICOS POR HORA~~|
|AFD|ACRE-PIE POR DIA|CMD|METROS CUBICOS POR DIA|

Presionando la tecla Cambio Elección es posible seleccionar cada unidad de

medición (como se muestra en la tabla). Presionando la tecla Aceptar se fija la

selección de la opción desplegada.

**Unidades de Nivel**

Del Menú Principal:

**CONFIGURAR:** **MODIFICAR LOS ITEMES SELECCIOANDOS:**

**UNIDADES DE NIVEL**

Seleccionar las unidades de medición usando el despliegue de lectura de nivel.

Estas unidades de medición se usan cuando se despliega o se registra una

medición de nivel.

Manual de Operación y Mantención Sigma 980-1

74

Las opciones son:

|Pulg.|Pulgadas|
|---|---|
|P|Pies|
|Cm|Centímetros|
|M|Metros|

Presionando la tecla de Cambio Elección es posible ingresar cada unidad de

medición requerida. Cuando la opción se despliegue en el visor presionar la tecla

Aceptar para entrar la selección.

**Dispositivo Primario**

Del Menú Principal

**CONFIGURACIÓN:** **MODIFICAR ITEMES SELECCIONADOS**

**DISPOSITIVO PRIMARIO**

Seleccionar el elemento primario deseado e ingresar los parámetros de tamaño

adecuados para dicho Dispositivo Primario.

Presionando la tecla Cambio Elección se desplegarán en el visor todas las

opciones de Dispositivos Primarios disponibles. Al encontrar la selección

requerida presionar la tecla Aceptar para fijar la selección. Después de realizar la

selección, se debe ingresar los detalles relacionados con el dispositivo primario

seleccionado. Las tablas expresadas a continuación muestran el detalle de los

tamaños requeridos para cada uno de los Dispositivos Primarios. Esta

información debe ser ingresada una vez realizada la selección del Dispositivo

Primario a utilizar.

Manual de Operación y Mantención Sigma 980-1

75

**Dispositivos Primarios de Apoyo**

|Vertederos|Col2|
|---|---|
|Cipolletti|Ancho cresta en pulgadas o centímetros (12" a 960" ó 30.48 a<br>2438.4 cm)|
|Rectangular con contracción|Ancho cresta en pulgadas o centímetros (12" a 960" ó 30.48 a<br>2438.4 cm)|
|Rectangular sin contracción|Ancho cresta en pulgadas o centímetros (12" a 960" ó 30.48 a<br>2438.4 cm)|
|Thel -mar|Medida en pulgadas (6,8, 10, 12 ó 15")|
|Vertedero Triangular o de aforo en<br>"V"|Angulo de triángulo en grados (22.5o a 120o|
|Vertedero compuesto de aforo en "V"|Angulo de triángulo en grados 22.5o a 120o), profundidad en<br>pulgadas. Ancho rectangular en pulgadas 0" a 120" (0 a 304<br>cm), con o sin contracción.|

**Canaletas**

|Parshall|Medida canaleta en pulgadas<br>(1,2,3,6,9,12,24,36,48,60,72,84,96,108,120, ó 144")|
|---|---|
|Trapezoidal|Medida de Canaleta (60o S, 60oL, 60oXL, 45o 2", 45o 12")|
|Tipo H|Medida Canaleta en pies: .5,.8,1.0, 1.5, 2.0, 2.5, 3.0, ó 4.5')|
|Tipo HL|Medida Canaleta en pies: 4.9' (una sola medida)|
|Tipo HS|Medida Canaleta en pies (.4, .6, .8, ó 1.0')|
|Leopold-Lagco|Medida Canaleta en pulgadas (4,6,8,10,15,18,21,24,27,30,36,42,48,60,66 ó<br>72")|
|Palmer - Bowlus<br>|Medida Canaleta en pulgadas (4,6,8,10,12,15,18,21,24,27,30,36,42,48,60 ó<br>72")|

Manual de Operación y Mantención Sigma 980-1

76

|Otros Surtidor, Cañería California|Medidas del surtidor en pulgadas (2" a 36")|
|---|---|
|~~**Surtidor, Cañería California**~~<br>|~~**Medidas del surtidor en pulgadas (2" a 36")**~~<br>|
|~~**Ecuación de Energía**~~<br>|~~**Entrar Variables K**~~**1**~~**, K**~~**2**~~**, n**~~**1**~~** & n**~~**2** <br>**(Q = K1, Hn1 + K2 Hn2 **<br>**K1 (0 a 999.99), K2 (+/- 0 a 9999.99) n1 & n2 (1 a 9.99)**<br>|
|~~**Altura caída de agua v/s flujo**~~<br>**(se entregan dos tablas de**<br>**caída v/s flujo) (*)**<br>|~~**Entre hasta dos tablas de hasta 100 puntos de altura de caída**~~<br>**de agua v/s flujo definido por el usuario.**<br>**Altura caída: 0 a 99.99 en pies o cm.**<br>**Flujo: 0 a 9999.99 en cualquier unidad deseada.**<br>|
|~~**Formula Manning**~~<br>|~~**Entrar coeficiente del diámetro de la cañería, pendiente,**~~<br>**coeficiente de aspereza.**<br>**Diámetro cañería : 4 a 240 pulg. Ó 101 a 6096 cm.**<br>**% pendiente: .001 a 1.00 [1 unidad x 100 unidades = .01**<br>**pendiente]**<br>**Ejemplo: 1 mt de declinación cada 100 metros sería = .01**<br>**pendiente**<br>**Aspereza: ver tabla coeficiente de aspereza en el capítulo 7.**<br>|
|~~**Area Velocidad**~~<br>|~~**Cañería Circular: entrar diámetro**~~<br>**Cañería : 4 a 240 pulg. (10 a 610 cm)**<br>**Canal rectangular: entrar ancho, 4 a 999.99 pulg. (10 a 2540**<br>**cm)**<br>**Canal en forma de U: entrar ancho del canal**<br>**4 a 999.99 pulg. ( 10 a 2540 cm)**<br>|
|~~**Nivel v/s Area Velocidad (se**~~<br>**entregan dos tablas de nivel**<br>**v/s área) (*)**<br>|~~**Entrar hasta dos tablas de hasta 100 puntos de área definidos**~~<br>**por el usuario. (Nivel: 0 a 99.99 en pies, pulgadas, metros o**<br>**centímetros)**<br>**(Area: 1 a 99999.99 en pies cuadrados, pulg. Cuadradas,**<br>**metros o cm cuadrados)**|

- Las tablas de Altura de caída de agua v/s flujo y Nivel v/s Area se rellenan con los datos

obtenidos por el usuario. La tabla de datos se puede obtener de los datos históricos, cálculos

matemáticos o mediciones físicas del canal con el otro dispositivo. La forma irregular de los

canales pueden requerir una serie de manuales de cálculo de áreas húmedas.

Manual de Operación y Mantención Sigma 980-1

77

**PROGRAMA DE BLOQUEO**

Del Menú Principal:

CONFIGURACION: MODIFICACION DE LOS ITEMES SELECCIONADOS:

PROGRAMA DE BLOQUEO

Al habilitar el Programa de Bloqueo, se proporciona una "Clave" secreta de

protección que evitará que el personal no autorizado trabaje sobre los datos del

Medidor de Flujo SIGMA 980.

Cuando se habilita el Programa de Bloqueo, y un usuario trata de realizar un

cambio en el programa, un aviso en la pantalla le pedirá al operador que ingrese la

clave. El operador deberá entonces ingresar el número 9800 y presionar la tecla

Aceptar.

**CIRCUITO DE MUESTREO**

Desde el Menú Principal:

CONFIGURACION: MODIFICAR ITEMES SELECCIONADOS

CIRCUITO DE MUESTREO

El Medidor de Flujo SIGMA 980 tiene la capacidad de recorrer un elemento

externo (tal como un muestreador de aguas residuales o un grabador de

diagramas), en proporción al flujo. La señal de recorrido es una pulsación de 12

VDC @ 100 mDC que dura 500 ms. Está en pin "C" de la interface de conexión

del MUESTRADOR.

Manual de Operación y Mantención Sigma 980-1

78

Después de seleccionar el Circuito de Muestreo, se debe ingresar el intervalo

entre pulsaciones y seleccionar una unidad de medida de flujo. En el ejemplo, se

ha seleccionado una pulsación cada 500 galones del Circuito de Muestreo.

Si se desea cambiar la unidad de medición de flujo (solamente para el Circuito de

Muestreo), solo se debe presionar la tecla de programación Cambio de Unidades

hasta que la unidad deseada aparezca en la pantalla, luego presionar la tecla de

programación Aceptar para almacenar los cambios.

Las Unidades de flujo disponible para el Circuito de Muestreo son:

|GAL|Galones|
|---|---|
|LTR<br>|Litros|
|M~~3~~|Metros Cúbicos|
|AF|Acre-pies|
|AF|Pies Cúbicos|

**IDENTIFICACION DEL LUGAR**

Del Menú Principal:

PROGRAMACIÓN: MODIFICACIÓN DE LOS ITEMES SELECCIONADOS

IDENTIFICACION DEL LUGAR

Ingresar una identificación del lugar con hasta 8 dígitos. Esta identificación

aparecerá en la impresión de todos los datos para ayudar a la identificación de la

fuente de datos.

Esta característica es especialmente útil cuando se monitorea sitios múltiples

utilizando solo un medidor de flujo o si se juntan las lecturas de datos de varios

Manual de Operación y Mantención Sigma 980-1

79

medidores de flujo. Ingresar el número de identificación del lugar elegido y luego

presionar la tecla Aceptar para fijar la entrada.

**Unidades de Flujo Totales**

Del Menú Principal:

CONFIGURACIÓN: MODIFICAR ITEMES SELECCIONADOS

UNIDADES DE FLUJO TOTALES

Seleccionar las unidades de medición de flujo totales cuando se visualicen en el

visor las lecturas de flujos totales.

Estas unidades de medida se usarán cada vez que se visualice las lecturas o

éstas se registren.

Las Unidades disponibles son:

|GAL|Galones|
|---|---|
|LTR<br>|Litros|
|M~~3~~|Metros Cúbicos|
|AF|Acre-pies|
|CF|Pies Cúbicos|

Mediante la presión de la tecla de programación Cambio de Elección que

despliega cada una de las unidades de flujo de su elección. Cuando la elección

deseada se ilumine, presionar la tecla de programación Aceptar para fijar la

selección.

Manual de Operación y Mantención Sigma 980-1

80

**Dirección de Velocidad**

_(Es aplicable solo cuando se registra velocidad)_

Del Menú Principal:

CONFIGURACIÓN: MODIFICAR LOS ITEMES SELECCIONADOS

DIRECCION DE VELOCIDAD

La ventaja de Dirección de Velocidad permite adaptar una cantidad de sitios

difíciles donde no se puede medir la velocidad de otra forma adecuadamente.

Existen tres elecciones posibles:

Aguas Arriba (normal)

Aguas Abajo

Siempre Positivo

**Aguas Arriba (Normal)**

Esta selección se ejecuta para el promedio de sitios de medición con velocidades

medianamente consistentes y de una turbulencia baja o media. La corriente de

flujo debería idealmente viajar en forma directa a través del sitio sin caídas o giros

cerca del punto de medición. Colocar el sensor en la tubería, de frente al flujo

donde el flujo de corriente entra al área de medición, tal como se muestra en la

figura.

1.- Pozo

2.- Sensor de Velocidad / Posición Normal (aguas arriba)

3.- Flujo

Manual de Operación y Mantención Sigma 980-1

81

**Aguas Abajo**

Esta selección permite ubicar el sensor al lado del punto de medición Aguas Abajo

(donde la corriente del flujo sale), dirigiendo el sensor en la dirección de aguas

abajo más que hacia la corriente normal, es decir, dirección aguas arriba. Esta

opción es muy útil en lugares en que hay más de un flujo de corriente de entrada a

un lugar y se desea medir flujos combinados de todas las corrientes en un solo

punto de salida.

De esta manera, al colocar el sensor "hacia atrás", (ver la figura), hará que la

lectura de la dirección de velocidad sea la contraria al flujo real de la corriente. Al

seleccionar Aguas abajo cuando el programa, del equipo SIGMA 980 revierte en

forma electrónica las señales de medidas para mostrar la dirección real del flujo.

1.- Pozo

2.- Sensor de velocidad /posición Aguas abajo

3.- Flujo

**Siempre Positivo**

El seleccionar Siempre positivo al programar, provoca que todas las lecturas sean

registradas como positivas, no importando la dirección de la señal.

Las condiciones de extrema turbulencia pueden dificultar la detección de la

dirección real del flujo, debido a la acción mista de las aguas demasiado

turbulentas.

Manual de Operación y Mantención Sigma 980-1

82

Las partículas reflectoras en el flujo del caudal, (especialmente, cerca de la

corriente de superficie), pueden moverse en varias direcciones distintas al mismo

tiempo, aunque el volumen de la corriente se mueva en la misma dirección

constantemente. La magnitud de la velocidad es generalmente consistente en

esos casos, sin embargo, los reflejos provenientes de las partículas que se

mueven en dirección positiva (la misma dirección del flujo del caudal), están tan

mezcladas con aquellas que vienen de las partículas que se mueven en dirección

negativa (dirección opuesta al flujo del caudal), lo que hace difícil determinar su

dirección real.

Esta elección no se debe seleccionar para lugares donde normalmente se

producen flujos negativos, tales como los afectados por las mareas.

**Unidades de Velocidad**

(Sólo se aplica cuando se registra velocidad)

Del Menú Principal:

**CONFIGURACION:** **MODIFICACION DE LOS ITEMES SELECCIONADOS**

**UNIDADES DE MEDICION**

Seleccionar las unidades de velocidad al desplegar la lectura de velocidad.

|Las opciones son:|Col2|
|---|---|
|FPS|Pies por Segundo|
|M/S|Metros por Segundo|

Manual de Operación y Mantención Sigma 980-1

83

**Velocidad de Corte / Velocidad de Omisión**

(Solo aplicable al realizar registro de velocidad)

La Velocidad de Corte compensa velocidades muy bajas y aguas demasiado

limpias en caso de que se presenten en los lugares de muestreo. Esta

combinación de condiciones únicas complica el monitoreo, debido a que el agua

demasiado limpia puede contener pocas partículas reflectantes, y las velocidades

muy bajas por lo general implican que existe poca o casi ninguna turbulencia

adicional a las burbujas de aire que son arrastradas al flujo del caudal (lo que

también contribuye a la formación de buenos objetivos reflectantes).

El sistema de velocidad de corte permite ingresar el un valor de velocidad por

defecto, que se activa cuando se alcanza el punto de fijación del sistema de

Velocidad de corte. El equipo SIGMA 980 mantiene el valor por defecto cuando se

presenta una velocidad de valor inferior, en lugar de informar muestras de

velocidad erróneas.

Por ejemplo:

Velocidad de Interrupción : .20 fps

Velocidad de omisión : 0 fps

Si la velocidad es menor que .20 fps, el equipo SIGMA 980 almacenará el valor de

cero fps hasta que la velocidad aumente sobre los .20 fps.

Velocidad de Interrupción : .20 fps

Velocidad de omisión: .20 fps

Manual de Operación y Mantención Sigma 980-1

84

Si la velocidad es menor que .20 fps, el equipo SIGMA 980 almacenará el valor de

.20 fps hasta que la velocidad aumente sobre los .20 fps.

**OPCIONES**

Al seleccionar el menú Opciones del Menú Principal se desplegará el Menú de

Opciones como se muestra a continuación:

Este menú permite:

Ajustar la Hora y Fecha para indicar el tiempo real en el reloj del equipo

SIGMA 980

Programar el Menú de Opciones Avanzadas del Medidor de Flujo SIGMA 980

- Seleccionar un nivel diferente del sensor

**Fijación de Fecha y Hora**

Del Menú Principal:

**OPCIONES: FECHA /HORA**

Al seleccionar la selección Fecha/Hora, se visualizará en el visor los datos

necesarios para ajustar la hora y fecha real en el reloj del equipo SIGMA 980.

Comenzar ingresando las horas y los minutos, para ello utilice el teclado numérico

ingrese los números en el espacio iluminado por el cursor. Utilice las teclas +

(más) ó - (menos) para cambiar de AM a PM y agregar el mes para la fecha

deseada. Presionar la tecla Borrar para eliminar todos los campos numéricos si

se ha cometido un error y se requiere ingresar un número diferente. Cuando esté

completo, presione la tecla de programación Aceptar para grabar sus cambios.

Manual de Operación y Mantención Sigma 980-1

85

**Sensor de Nivel**

Del Menú Principal:

**OPCIONES:** **SENSOR DE NIVEL**

Esta opción permite seleccionar entre un sensor ultrasónico de nivel o una sonda

sumergida de nivel. Solo se puede utilizar un sensor de nivel a la vez. Para las

unidades equipadas con las opciones de Area/Velocidad esta opción se refiere a

la unidad de nivel de la sonda sumergida Area/velocidad.

**OPCIONES AVANZADAS**

Del Menú Principal

OPCIONES : OPCIONES AVANZADAS

Este menú consiste en una lista de opciones avanzadas de programación. Se

debe utilizar las teclas de programación Flecha Arriba y Flecha Abajo para

destacar la elección requerida, luego presionar la tecla de Seleccionar para

trabajar con dicho ítem.

_El Menú de Opciones Avanzadas incluye los siguientes ítemes:_

Salidas 4-20 (opcional)

Alarmas (opcional)

- Calibración

- Sistema de Comunicación

Registro de Datos

Diagnósticos

Totalizador de Flujo

Lenguaje

Manual de Operación y Mantención Sigma 980-1

86

- Punto Referencia de Muestreo

Aguas Lluvias

**Salidas de 4-20 mA - (Opcional)**

Del Menú Principal:

OPCIONES: OPCIONES AVANZADAS SALIDAS DE 4-20 MA

Las salidas de 4-20 mA incluidas en el Medidor de Flujo SIGMA 980 una estándar

y la segunda opcional que se encuentran disponibles en el equipo SIGMA 980

pueden ser asignadas a otros equipos de proceso, como por ejemplo; un

muestreador de aguas residuales en proporción al rango del flujo.

Ambas salidas de 4-20 mA aisladas incluidas en el Medidor de Flujo SIGMA 980

son únicas y pueden ser asignadas no solo al flujo sin que a cualquier otro canal

disponible (excepto de aguas lluvias).

1.- Primero, la salida habilitada de 4-20 mA (o si se desea desconectar)

2.- Luego tomar cualquier salida, ya sea A o B (si están instaladas). Utilizar las

teclas flecha arriba o flecha abajo para seleccionar las salidas.

3.- Después, seleccionar un canal para asignar las salidas. Presionar la tecla

Cambiar Elección para moverse dentro de los nombres de los canales

desplegados. Cuando se elija el canal deseado presionar la tecla Aceptar para

fijar la selección del canal. Si se desea, además se puede deshabilitar o

desconectar la salida.

Manual de Operación y Mantención Sigma 980-1

87

4.- Ingresar un valor de canal al valor de corriente 4 mA. Es decir, ingresar el

valor de la entrada que se requiere para generar 4 mA de salida de corriente.

Este valor generalmente es cero, sin embargo, puede fijarse el valor que se desee.

5.- Repita el paso 4 para la salida de corriente de nivel de 20 mA.

**ALARMAS**

Del Menú Principal:

**OPCIONES :** **OPCIONES AVANZADAS**

**ALARMAS**

Cuando una alarma se activa se acciona la confección de un INFORME VIA

MODEM (a un computador personal), y/o activar un relé. Las alarmas pueden ser

programadas para activarse basándose en muchas condiciones (batería

descargada, poca memoria, señal del transductor, etc.)

_Informe Vía Módem_

Esta opción activa un sistema de Informe Vía Módem cuando se acciona una

alarma. Ver la Configuración de Comunicaciones, para mayores detalles a cerca

de la configuración del módem para enviar informes a un computador personal

ver al final de este capítulo.

_Relés_

Esta opción permite que el equipo SIGMA 980 active cuatro relés internos cuando

se presenta una alarma.

Manual de Operación y Mantención Sigma 980-1

88

_Descripciones de Alarma_

Existen dos tipos de alarma. Alarmas de Problemas y Fijación de puntos de

alarma.

- Alarmas de Problemas

Se activan cuando se produce una situación problemática, como por ejemplo

cerrar un relé cuando la memoria está próxima a llenarse.

Fijación de Puntos de Alarma

Fijar los puntos a alcanzar (tanto el punto alto como el bajo o ambos), antes de

iniciar una acción, por ejemplo cerrar un relé cuando el agua exceda las 24" (60

cm) o se encuentre por debajo de las 4" (10 cm).

Cada relé de alarma está provisto de contactos SPDT (Form C). Los contactos de

alarma son del rango de los 10 Amp @ 120 VAC o 5 amps @ 240 VAC

(resistencia de carga). Las alarmas están provistas de contactos _normalmente_

_abiertos_, _normalmente cerrados_ y _comunes._ Se pueden habilitar varias alarmas

al mismo tiempo y se pueden asignar a diferentes condiciones de problema

mediante relés individuales o se pueden asignar todas las condiciones de

problemas al mismo relé.

Manual de Operación y Mantención Sigma 980-1

89

_Alarmas de Problemas_

Para programar una Alarma de Problema se debe primero que todo, seleccionar

una acción que active la alarma cuando esta acción se presente. (informada vía

módem o programada con relés), luego seleccionar una de las condiciones de

problemas indicadas a continuación:

|Condiciones de<br>Problema|Causa|
|---|---|
|~~Batería principal baja~~|~~El voltaje de la energía principal está bajo el nivel aceptable~~|
|Batería de Memoria|La batería de litio de la memoria interna se encuentra con voltaje<br>bajo. Reemplazar la batería para evitar pérdida de programación<br>o datos.|
|Me moria de Registro baja|La memoria de registro libre es de menos del 20%|
|Memoria de Registro llena|La memoria de registro está totalmente llena.|
|Pérdida de Eco Ultrasónico<br>(Se envió una pulsación<br>de sonido y el eco de<br>retorno no fue recibido)|El eco ha estado temporalmente defectuoso debido a un cambio<br>en las condiciones del terreno, como por ejemplo: desechos<br>flotantes, espuma en el canal, viento, etc...|
|Señal del transductor|El transductor está operando fuera de la banda muerta. Puede<br>haber ocurrido por la instalación deficiente del transductor (sin<br>aislación, vibración de la banda de montaje).|
|Falla Ultrasónica|El transductor no está enchufado. El cable está dañado. El sensor<br>térmico del transductor está dañado.|
|Interrupción RS485|Problemas con las comunicaciones entre el medidor de flujo, la<br>CPU o un sensor ultrasónico remoto o de velocidad. También<br>puede indicar una apertura del sensor térmico.|
|Falla del Módem|El Módem I.C. o el tablero de circuito del Módem ha fallado.|

Manual de Operación y Mantención Sigma 980-1

90

**Fijar Puntos de Referencia de Alarmas**

La fijación de puntos de Referencia de Alarmas se activa cuando se alcanza los

rangos altos y/o bajos definidos por el usuario. Para programar la Fijación de

Punto de Referencia de Alarma, primero se debe habilitar una de las condiciones

de problema, luego seleccionar una acción que active la alarma cuando esta

acción se presente. (Informada vía módem o fijación de relé), luego seleccione el

punto de referencia (nivel alto, nivel bajo, cambio en el rango del flujo, etc...), en el

ejemplo que se muestra a continuación se ha fijado el punto de referencia de

alarma en un punto bajo de pH 6.9.

_BANDA MUERTA_

Después de completar la fijación del punto de referencia el equipo solicitará el

ingreso del valor de Banda Muerta. Esta Banda Muerta, es el área situada entre la

"activación" y "desactivación" de la alarma.

En el ejemplo de pH anterior, la Banda Muerta estaba fijada a .10 pH. Cuando el

pH alcanzó el punto 6.9 (la línea punteada inferior), la alarma se desconectó, pero

ésta no retornó a la posición apagado hasta que el nivel de pH vuelvió a tener las

características de 7.00. Esta diferencia es la fijación llamada Banda Muerta y

debería ser fijado de acuerdo a las características del ítem medido. El propósito

de la fijación de Banda Muerta es evitar el accionamiento de los relés de la alarma

cuando los valores de activación y desactivación están demasiado próximos.

Estas pequeñas fluctuaciones ocurren cuando la medición es realizada muy cerca

de la línea del punto, esto podría hacer que la alarma se active y se desactive muy

rápidamente.

Manual de Operación y Mantención Sigma 980-1

91

**Calibración**

Del Menú Principal:

**OPCIONES:** **OPCIONES AVANZADAS**

**CALIBRACIÓN**

Calibración de la Sonda Sumergida, Sensor Ultrasónico, ORP, pH, Temperatura y

salidas 4-20 mA se ejecutan mediante la selección de este Menú. No se requieren

ajustes mecánicos.

**Es importante tener en cuenta que todos los valores de calibración son**

**configurados en la fábrica las fallas podrían aparecer al iniciar la rutina de**

**calibración. Debido a esto no se aconseja probar la calibración por medio de**

**modificaciones al menú de calibraciones para probar si los ajustes fueron**

**realizados en forma correcta. Se debe correr el programa y tomar las**

**medidas de manera normal para verificar que la calibración fue exitosa.**

**Calibración del Sensor de Velocidad**

El Sensor de Velocidad no se requiere calibración. La transmisión de la frecuencia

está fijada con un generador de frecuencia que es controlado por cristal de cuarzo

de alta precisión y no necesita ajustarse.

Manual de Operación y Mantención Sigma 980-1

92

**Calibración de la Sonda Sumergida de Velocidad**

Del Menú Principal:

**OPCIONES:** **OPCIONES AVANZADAS**

**CALIBRACION: SONDA SUMERGIDA**

Equipo necesario:

Balde con agua - Sensor de Area Velocidad & Medidor de Flujo - Regla

La calibración de la Sonda Sumergida de Velocidad destaca al equipo SIGMA 980

por la característica única de cada sonda en particular. Además, la calibración

compensa cualquier corriente de aire en la salida del sensor que puede ocurrir en

períodos de tiempo más largos a medida que el material del sensor tiene más

tiempo (seis meses o más).

La Sonda Sumergida es un transductor a presión que contiene un diafragma de

acero inoxidable. A medida que aumenta la presión de agua (con una altura de

caída en aumento del flujo de la corriente), el diafragma de deflecta, o es

empujado contra el estado sólido del aparato llamado deformímetro (medidor de

deformación). Este medidor convierte la presión contra el diafragma en voltaje. A

medida que aumenta la altura de caída (el nivel) del flujo de la corriente, de igual

manera aumenta el voltaje proveniente de la Sonda Sumergida. El voltaje se lee

en el microprocesador del equipo SIGMA 980 a intervalos regulares y

transformado en un número que representa el nivel en el flujo de la corriente. La

lectura del nivel puede por lo tanto, ser convertida por el equipo SIGMA 980 en un

rango de flujo basado en la lectura realizada por el circuito de velocidad.

Manual de Operación y Mantención Sigma 980-1

93

_Procedimiento de Calibración_

_**Paso 1.- "Ubicar la Sonda Sumergida de Velocidad en posición horizontal**_

_**en una superficie plana"**_

Ubicar la sonda con la cara del sensor tocando la superficie de piso (la parte en

forma de plato con orificios), plana sobre la superficie a utilizar y presionar una

tecla.

_**Paso 2.- "Ubicar el sensor en el líquido, con la cara del sensor mirando**_

_**hacia arriba y golpeando levemente la superficie para remover las burbujas**_

_**de aire"**_

Ubicar la sonda en la parte superior baja del balde y golpear suavemente la

superficie del plato para remover las posibles burbujas de aire que se encuentren

bajo el plato. Si estas burbujas no son removidas es posible que se reciban

lecturas de nivel incorrectas desde el sensor durante la calibración.

_**Paso 3.- "Sumergir la Sonda a una Profundidad Conocida"**_

Ubicar la sonda a una profundidad de 6 pulgadas del nivel del agua en posición

horizontal como se muestra en la figura. Es importante asegurarse de que la

superficie del agua esté calma y que la sonda se encuentre estable y sin

movimiento alrededor. Luego presionar cualquier tecla para continuar.

Medir la profundidad desde el fondo del balde desde la superficie del agua (D 1 ) e

ingresar el valor utilizando el teclado numérico. Presionar la tecla Aceptar para

continuar. Con este procedimiento la calibración de la Sonda Sumergida de

Velocidad ha sido completada.

Manual de Operación y Mantención Sigma 980-1

94

**Calibración del Sensor Ultrasónico**

Del Menú Principal :

**OPCIONES:** **OPCIONES AVANZADAS**

**CALIBRACION: SENSOR ULTRASONICO**

La calibración del sensor ultrasónico se debe realizar una vez al año o cada vez

que se instale el sensor en otro punto de muestreo o en un medidor diferente.

Este menú tiene dos opciones:

_Calibración Ultrasónica_ : Calibrar el transductor del sensor de temperatura

incorporado y ajustar el nivel de lectura en un canal húmedo o seco.

_Rango Invisible_ : Ajuste la extensión de la Banda Muerta para eliminar los ecos

falsos.

**IMPORTANTE:**

El transductor de temperatura debe estar a la misma temperatura que el aire de

temperatura ambiente del lugar de muestreo antes de la calibración para obtener

resultados óptimos.

Toma alrededor de unos cien minutos que el sensor llegue al punto de equilibrio

total con la temperatura ambiental del lugar de muestreo.

Manual de Operación y Mantención Sigma 980-1

95

**Calibración Ultrasónica**

Ingresar la temperatura ambiente del lugar donde será ubicado el sensor. Es

importante asegurarse de que el sensor tenga el tiempo suficiente para lograr el

equilibrio con la temperatura ambiente.

**Constante de Tiempo de Temperatura**

La velocidad del sonido del aire cambia con la temperatura del aire. El sensor

ultrasónico está equipado con una compensación de temperatura para ayudar a

eliminar los efectos de las variaciones de la temperatura en condiciones normales

del lugar de muestreo. La constante de tiempo del transductor ultrasónico es de

100 minutos.

**Método de Calibración**

Ajustar el nivel de la corriente del agua mediante uno de los dos métodos

recomendados: Profundidad del líquido o Altura del sensor. Ingresar además, el

Rango Invisible (o ajustar la Banda Muerta), lo que permite que el transductor

ignore los reflejos de las obstrucciones entre el sensor y la superficie del agua,

como las laderas, paredes del canal, etc. Cada método tiene sus ventajas y

desventajas, la elección del método más apropiado depende de las condiciones

del lugar de muestreo. La calibración de profundidad del líquido requiere del

ingreso de la "Altura de caída del Agua" o la profundidad del líquido en el canal

que contribuye al flujo".

Manual de Operación y Mantención Sigma 980-1

96

**Profundidad del Líquido**

La calibración de la profundidad del líquido se utiliza principalmente cuando hay un

acceso seguro al dispositivo primario para realizar una medición física de la

profundidad del líquido y del agua que fluye. (el canal no está seco).

Al seleccionar el método Profundidad del Líquido ingresará al nuevo nivel. La

pantalla desplegará la lectura del nivel actual como referencia. Se debe tomar la

medición física de la profundidad del líquido (cabeza) e ingresar el valor (es

primordial asegurarse de que se ha ingresado el valor en las unidades mostradas),

presionar la tecla Aceptar al finalizar.

Este método es el más común y el más exacto al igual que presionar la tecla de

Ajuste de Nivel en el panel frontal.

**Altura del Sensor**

La Calibración de la Altura del Sensor es usada generalmente cuando las

condiciones de acceso al dispositivo primario son difíciles (espacios reducidos

para ingresar al pozo) o cuando no hay líquido fluyendo en el canal. La Altura del

sensor requiere del ingreso de la distancia entre la cara del sensor ultrasónico y el

punto de flujo cero en el dispositivo primario. El punto de flujo cero de un

elemento primario es el nivel en que cesa el flujo. En una tubería redonda el punto

de flujo cero, es típicamente el de la solera o el fondo de la tubería. En un

vertedero triangular o de aforo en V, el punto de flujo cero estaría cuando el líquido

detrás del vertedero se nivela con el fondo de la "V" (todavía quedaría líquido

detrás de la placa del vertedero, pero éste no estaría contribuyendo al flujo).

Manual de Operación y Mantención Sigma 980-1

97

La parte superior del visor despliega en forma instantánea la distancia de medición

tomada desde el transductor a la referencia ingresada. Se debe tomar la medida

física de la distancia e ingresar el valor (en las unidades de medición que se

muestran en el visor). Presionar la tecla Aceptar cuando se finalice.

**Rango Invisible**

El equipo SIGMA 980 viene equipado con un Rango Invisible (banda muerta

ajustable), para evitar falsos ecos desde la parte superior de las paredes del canal,

los escalones de las escalas, los anaqueles, etc... (ver dibujo). La distancia

seleccionable la define el usuario y es invisible para el medidor de flujo. Solo los

objetos que se encuentran más allá del Rango Invisible pueden ser detectados.

Al seleccionar el Rango Invisible desde el menú de calibración del sensor

ultrasónico, se ingresa rápidamente la distancia desde el extremo del Rango

Invisible. La distancia debe ser mayor que la mínima de la banda muerta de 15"

(38 cm), Se debe cuidar de no tomar Rangos Invisibles que se extiendan hasta

donde se haya una unión o traslapo del nivel más alto esperado en el canal. Se

debería dejar entre el Rango Invisible y el nivel esperado más alto un espacio de

al menos 2" (5.08 cm).

**IMPORTANTE:**

**REVISAR SIEMPRE EL AJUSTE DE NIVEL CUANDO SE REINSTALE EL**

**MEDIDOR DE FLUJO SEGUIDO DE UN NIVEL DE CALIBRACIÓN** .

Manual de Operación y Mantención Sigma 980-1