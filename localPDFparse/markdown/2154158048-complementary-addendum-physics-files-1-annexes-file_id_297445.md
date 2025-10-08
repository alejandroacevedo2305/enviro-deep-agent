---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: general
pages: 4
has_toc: True
has_tables: False
extraction_quality: high
---

Declaración de Impacto Ambiental Proyecto

“Ampliación Parque Eólico Alto Baguales”

ANEXO 1.8 FICHA TÉCNICA SISTEMA DE
DETECCIÓN DE SOMBRAS

REGIÓN DE AYSÉN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO

ABRIL, 2023

**DESCRIPCIÓN TECNICA**

**SISTEMA DE DESCONEXIÓN POR SOMBRA (Shadow shutdown)**

**1** **INFORMACIÓN GENERAL**

El parpadeo periódico de la sombra es el sombreado recurrente de la luz solar directa por el
movimiento de las palas del rotor de un aerogenerador de energía eólica. La ocurrencia de este
efecto depende de las condiciones climáticas locales, alineación de la góndola según la dirección del
viento, la posición y los tiempos de funcionamiento del aerogenerador eólico.

**2** **PRINCIPIO DE FUNCIONAMIENTO**

La Desconexión por Sombra (Shadow shutdown) es una función que está integrada en el sistema de
control del aerogenerador de energía eólica y activado específicamente en cualquier aerogenerador
en eólica donde la sombra hace necesario el apagado. El sistema de desconexión no es posible
utilizarlo en múltiples aerogeneradores, por lo que cada uno tiene un sistema y es independiente.

También deben instalarse los sensores opcionalmente para medir la luminiscencia. Los sensores se
instalan en la torre o en la góndola, según el tipo de aerogenerador.

**2.1** **DETERMINACIÓN DEL TIEMPO POTENCIAL DE PROYECCIÓN DE SOMBRAS**

La función de desconexión o apagado automático se basa en un sistema calendárico, estos se
definen en intervalos contiguos y no superpuestos de una línea de tiempo subyacente, los tiempos
de inicio y finalización de la proyección de sombra a en los sitios de inmisión afectados se calculan
teniendo en cuenta los parámetros específicos del sitio, como la altura del buje, el diámetro del
rotor, coordenadas, ubicación del sitio de inmisión y su topografía.

**2.2** **MEDICIÓN DE LA LUMINISCENCIA**

El parpadeo periódico de las sombras depende de la luz solar. Según el Grupo de Trabajo Conjunto
del Gobierno Federal Alemán/Estados Federales sobre Control de Inmisiones (Bund/LänderArbeitsgemeinschaft für Immissionsschutz (LAI), es probable que las sombras parpadeen cuando la
luz del sol es superior a 120 W/m [2] en el nivel vertical a la dirección de incidencia.

El nivel de luminiscencia en una superficie de medición horizontal está influenciado por la posición
del sol y el equivalente fotométrico. Este último está determinado por la refracción y la atmósfera.

Por lo tanto, se ha desarrollado un procedimiento para que la función de apagado por sombra
evaluar el potencial de proyección de sombras en cualquier momento. Para medir la luminiscencia,
los sensores están dispuestos de manera que al menos un sensor esté en el lado soleado y uno en

el lado oscuro de la torre.

El sistema de control del aerogenerador determina los valores de la luminiscencia más alta y más
baja, es decir, la intensidad de la luz y la intensidad de la sombra, sobre la base de los valores

medidos de los sensores.

En lugar de utilizar una medida de luminiscencia intrínsecamente inexacta para determinar si es
probable que ocurra el parpadeo de la sombra, la relación entre la intensidad de la luz y la intensidad
de la sombra y la intensidad de apagado, derivada de esto.

Con una luminiscencia de 120 W/m [2], la intensidad de apagado determinada es del 36 %. Este valor
es independiente de la posición del sol. Una vez que la relación entre la intensidad de la luz y la

intensidad de la sombra cae por debajo del 36 %, la luminiscencia es superior a 120 W/m [2] . Se
produce un parpadeo de sombras.

Este valor se validó en una prueba de campo de módulos de apagado automático, además la
intensidad se puede modificar individualmente según sea necesario.

**2.3** **DESCONEXIÓN AUTOMÁTICA**

La desconexión o apagado por sombra se activa tan pronto como cae por debajo del valor
establecido dentro del plazo programado. La luminiscencia medida no se promedia. La desconexión
automática también reacciona cuando el valor cae por debajo de la intensidad de apagado definida,
aunque sea brevemente. Los tiempos de filtrado se pueden utilizar para definir un retraso en la
respuesta de la función de desconexión por sombra. Se define un parámetro durante cuánto tiempo,
en promedio, en el cual la relación de la intensidad de la luz y la intensidad de la sombra debe estar
por debajo del valor de intensidad de apagado definida para para que se active la desconexión

automática.

Si las condiciones de luz cambian, de tal manera que ya no es posible el parpadeo de la sombra, la
desconexión por sombra permanece inicialmente activa, posteriormente se desactiva y el
aerogenerador se reinicia cuando el tiempo programado ha expirado o cuando el valor de la
intensidad de apagado excede en forma constante durante un período de tiempo específico. Un
parámetro especifico es el promedio de la relación entre la intensidad de la luz y la intensidad de la
sombra y debe estar, en un intervalo de tiempo, por encima de la intensidad de apagado definida
para desactivar sistema de desconexión por sombra.

**2.4** **FUNCIONES AVANZADAS**

La desconexión por sombra también puede tener lugar sin tener en cuenta la luminiscencia. En este
caso, la desconexión del aerogenerador está controlada por tiempo de acuerdo con los marcos de
tiempo programado en el sistema de control. Esto significa que el aerogenerador también es
detenido si hay cobertura de nubes.

También posee una función de día de la semana, que permite limitar el apagado a los días
seleccionados de la semana. Esta función es útil para aerogeneradores cerca de áreas comerciales
o industriales,fincas, por ejemplo, donde no se trabaja en espacios que requieran protección los

fines de semana.

Las funciones avanzadas se pueden implementar de manera específica para sitios de inmisión

seleccionados.

**3** **SEGURIDAD**

La función de los sensores de luz se comprueba automáticamente dos veces al día durante
operación. Si los valores medidos no son plausibles, se genera un mensaje.

Ante la falla de un sensor, da como resultado la relación de sombra a la intensidad de la luz que cae
por debajo del valor de intensidad de apagado. El aerogenerador se detiene dentro del tiempo
programado y se genera un mensaje.

**4** **REGISTRO**

La activación del sistema de apagado automático se registra como un mensaje de estado por parte
del control remoto. El sistema de transmisión de datos tiene la capacidad de almacenar la data con
fecha, hora y duración del apagado. Si es necesario, se registran los datos medidos de los sensores
de luz y la proporción de sombra a luz.

La intensidad se registra como un promedio por minuto; los valores mínimo y máximo en un minuto
también se registran los intervalos y la intensidad definida de apagado.