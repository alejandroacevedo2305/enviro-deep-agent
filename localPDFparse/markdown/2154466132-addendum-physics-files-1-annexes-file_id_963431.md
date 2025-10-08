---
title: Template Procedimiento
author: GUADALUPE BRAVO CASTANEDA
date: D:20220805165314-04'00'
language: es
type: report
pages: 6
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Contenido 1. Objetivo ..................................................................................................................... 2 2. Alcance ....................................................................................................................... 2 3. Definiciones ............................................................................................................... 2 4. Responsabilidades ..................................................................................................... 3 5. Descripción ................................................................................................................ 3 6. Diagrama de flujo ...................................................................................................... 4 7. Documentos auxiliares .............................................................................................. 6 8. Referencia .................................................................................................................. 6 9. Anexos ....................................................................................................................... 6 10. Aprobación ................................................................................................................ 6 11. Actualizaciones .......................................................................................................... 6
-->

# Contenido 1. Objetivo ..................................................................................................................... 2 2. Alcance ....................................................................................................................... 2 3. Definiciones ............................................................................................................... 2 4. Responsabilidades ..................................................................................................... 3 5. Descripción ................................................................................................................ 3 6. Diagrama de flujo ...................................................................................................... 4 7. Documentos auxiliares .............................................................................................. 6 8. Referencia .................................................................................................................. 6 9. Anexos ....................................................................................................................... 6 10. Aprobación ................................................................................................................ 6 11. Actualizaciones .......................................................................................................... 6

1

**1.** **Objetivo**

Establecer los lineamientos de mantenimiento preventivo como estrategia para conservar la operatividad
y confiabilidad de los equipos, maquinarias e instalaciones según su diseño y función. Su fin último es
garantizar la seguridad de los colaboradores, velar por la calidad, legalidad, seguridad alimentaria y
continuidad del negocio reduciendo interrupciones de producción por fallas de maquinaria.

**2.** **Alcance**

Aplica para la ejecución del mantenimiento preventivo en los activos (equipos, maquinarias e instalaciones)
de todas las líneas de producción de Ideal SA.

**3.** **Definiciones**

**Activo:** es un bien propiedad de la empresa y que es utilizado por el negocio como medio para producción
y gestión. Dentro de estos se incluyen equipos, maquinarias, instalaciones, edificios, entre otros.

**MAXIMO:** software desarrollado por IBM para la gestión de activos y del mantenimiento.

**Mantenimiento Preventivo (MP):** estrategia para garantizar la operación normal de los activos. Esta se
deriva de un programa de Mantenimiento Preventivo el cual puede ser modificado y/o ajustado en base a
un análisis estadístico y a las necesidades de confiabilidad propias de la operación.

**Rutina:** actividad de mantenimiento que considera tareas rutinarias específicas y bien definidas que se
realizan sistemáticamente con frecuencias cortas para asegurar condiciones en los activos.

**Orden de Trabajo (OT):** documento fundamental para la gestión de los trabajos de mantenimiento. Se
compone de un plan de trabajo, plan de seguridad, fechas de programación y ejecución, responsabilidad,
e información relativa al activo, ubicación y supervisor. Se puede generar dentro del MAXIMO.

**Plan de trabajo:** relación de tareas y tiempos que sirven como guía para la ejecución de la Orden de
Trabajo. Este plan se configura en el Sistema MAXIMO.

**Plan de seguridad:** serie de precauciones y/o acciones que se deben tener en cuenta antes, durante y
después de intervenir un activo. Este plan se configura en el Sistema MAXIMO.

**Trabajo resultante:** actividad pendiente que se deriva de la ejecución de una OT (rutina, mantenimiento
preventivo, mantenimiento correctivo, etc.) y que, por condiciones insuficientes: disponibilidad refacciones,
tiempos parada, personal técnico, condiciones de operación, etc no puede ser resuelto de inmediato.

**Requisición de Compra (MX):** solicitud formal de compra de refacciones, materiales o servicios. Es
generada en MAXIMO por el técnico y autorizada por el Supervisor de Mantenimiento. Luego este último
puede generar requisición a los compradores funcionales para su autorización por Jefe/Gerente del área.

**Lubricación:** se refiere a la aplicación, cambio y/o reposición de lubricante en los mecanismos o piezas
mecánicas en contacto directo, su objetivo es disminuir el desgaste y facilitar el movimiento de las piezas.

**Instalaciones:** activos que comprenden pisos, techos y paredes de la planta de producción.

**Frecuencia del mantenimiento:** estándar que establece fechas para programar las órdenes de trabajo.
Puede definirse en base a tiempo entre OT o a un parámetro del equipo (horas operación, medición calidad
aceite, vibraciones, etc). Se basa en el riesgo, experiencia e historial de fallas de activos.

_*Para equipos nuevos: se toma en cuenta la ficha técnica del proveedor y/o recomendaciones del mismo._

2

**4.** **Responsabilidades**

**Técnico de Mantenimiento:** es responsable de la ejecución y registro documental de la OT (MAXIMO y
documento físico) asegurando los criterios de seguridad del personal, inocuidad de los productos y
confiabilidad de los activos. En caso de existir trabajos resultantes es responsable de solicitar los
materiales necesarios, realizar el trabajo y/o garantizar el cierre de los pendientes.

**Administrativo de Mantenimiento:** genera las OT, da seguimiento al plan de mantenimiento preventivo
en coordinación con los Supervisores de Mantenimiento, resguarda los registros físicos de las actividades
de mantenimiento, genera reportes de indicadores para evaluación de la gestión del mantenimiento y da
apoyo como usuario clave en la capacitación del sistema MAXIMO para toda el área de Mantenimiento.

**Supervisor de Mantenimiento:** elabora y actualiza el plan de mantenimiento preventivo de su área,
asegura la ejecución del plan de MP coordinando los recursos y el personal necesario, evalúa la calidad
del MP e implementa acciones para asegurar la seguridad del personal, inocuidad del producto,
continuidad del negocio y mejora en indicadores (IPFM, %MP, %Costo y %Eficiencia). Su labor es
balancear el costo de mantener contra la seguridad, inocuidad y confiabilidad de los activos.

**Jefe/Gerente de Mantenimiento:** asegurar la disponibilidad óptima de los recursos, personal y plan de
formación para ejecutar la estrategia de mantenimiento preventivo, implementar el modelo de gestión de
activos de Grupo Bimbo en el departamento y asegurar la eficiencia en uso de los recursos (ZBB).

**5.** **Descripción**

Para el desarrollo del mantenimiento preventivo se deberá seguir el siguiente proceso:

 - El administrativo de mantenimiento genera la orden de trabajo (OT), según frecuencia de
mantenimiento establecida en el Programa de Mantenimiento Preventivo.

 - El supervisor de mantenimiento, recibe la orden de trabajo (OT) a través del sistema MAXIMO, y
se asigna a Técnico correspondiente para cada área.

 - El técnico deberá ingresar a MAXIMO, en el sistema encontrará un listado de órdenes de trabajo
y las actividades que tiene que realizar, durante la semana.

 - El técnico verifica la condición de los activos, según ello realizará la requisición de compra (MX) a
través del Sistema MAXIMO de las herramientas, refacciones y/o materiales que necesitará. El
supervisor y/o el técnico coordina la disponibilidad de los equipos, para la intervención, con el
supervisor de producción de la línea, y verifica la existencia de lo solicitado en la MX.

 - Posteriormente el técnico realiza las actividades asignadas en la OT, aplicando el plan de
seguridad, seguridad de alimentos y técnicas correctivas.

 - En caso que el técnico no concluya el mantenimiento, se origina el trabajo resultante que se realiza
según el procedimiento de Ejecución del Mantenimiento Correctivo.

 - En caso que el técnico concluya su labor sin ningún inconveniente, verifica que sus herramientas
(pernos, tornillería, otros) estén completas, también verificará el estado de los plásticos duros del
equipo y/o maquinaria (en caso aplique). Si el mantenimiento preventivo realizado lo requiere, el
mecánico informa a Seguridad de Alimentos y al supervisor de producción con el fin de liberar el
activo de acuerdo con el procedimiento para liberar sanitariamente los equipos.

3

 - El supervisor de mantenimiento supervisa los trabajos realizados de Mantenimiento Preventivo,
audita su calidad y cierra la orden de trabajo en el Sistema MAXIMO.

**NOTA:**

 - Todas las herramientas y/o equipos que ingresan al área deben estar en óptimas condiciones de
uso. El supervisor encargado es el responsable de validar estas condiciones, si no se cumplan las
condiciones, realizar acciones correctivas para cumplir con dichas condiciones.

 - Se realizará la liberación en caso de que lo requiera cuando el mantenimiento se haya realizado a
una parte en contacto directo con el equipo.

**RUTINA DE LUBRICACIÓN:**

La lubricación es un mantenimiento preventivo que se realiza a los equipos y/o maquinarias, con el
propósito de evitar que las piezas de estos se degasten, esta actividad es ejecutada por el mecánico según
el Programa de Rutina de Lubricación Semanal. Para la rutina de lubricación el Administrativo de
Mantenimiento genera la orden de trabajo (OT), según frecuencia establecida en el Programa de Rutina
de Lubricación Semanal. Como es un mantenimiento preventivo, se procede según los pasos descritos
anteriormente.

**6.** **Diagrama de flujo**

|Responsables|Flujo de trabajo|Referencias|
|---|---|---|
|Administrativo<br>Mantenimiento<br>Supervisor<br>Mantenimiento<br>Técnico<br>Técnico|INICIO<br>Generar la orden de trabajo (OT) segúnla frecuencia<br>establecida en el_Programa de Mantenimiento_<br>Recibir la OT a través de MAXIMO, mediante este se<br>asigna el técnico que ejecutará el trabajo<br>Revisar en el Sistema MAXIMO las actividades que<br>tiene asignadas para la semana<br>Verificar la condición de los activos que requieren<br>mantenimiento preventivo<br>1|Programa de<br>Mantto<br>preventivo de<br>planta|

4

|Responsables|Flujo de trabajo|Referencias|
|---|---|---|
|Técnico<br>Supervisor de<br>Mantto y/o Técnico<br>con Supervisor<br>de produccion<br>Técnico<br>Técnico<br>Técnico<br>Técnico<br>Técnico<br>Técnico<br>Técnico<br>Técnico<br>Seguridad<br>alimentos<br>Técnico<br>Supervisor<br>Mantenimiento|¿Cuenta con herramientas,<br>refacciones y/o materiales<br>que necesita?<br>Generar la Requisición de Compra (MX)<br>de lo que necesita en MAXIMO<br>Coordinar la disponibilidad de los<br>equipos para la revisión con el<br>área de Producción<br>SI<br>NO<br>Verificar la entrega de<br>lo solicitado en la MX<br>Realizar actividades<br>asignadas en la OT<br>¿se logró<br>completar<br>el MP?<br>SI<br>NO<br>Se origina un trabajo resultante<br>Se procede según procedimiento de<br>Mantenimiento Correctivo (MC)<br>1<br>Verificarque las herramientas<br>estan completas<br>¿se requiere que<br>sanidad libere el<br>equipo?<br>SI<br>NO<br>Supervisar los<br>trabajos realizados<br>Informar a sanidad para<br>higienizar y liberar el equipo<br>Liberación sanitaria<br>Documentar trabajos en MAXIMO<br>Cierra los trabajos en MAXIMO<br>FIN|Procedimiento<br>Ejecución<br>Mantenimiento<br>Correctivo<br>Aviso de trabajo<br>Procedimiento<br>para liberar<br>sanitariamente<br>los equipos|

5

**7.** **Documentos auxiliares**

 - Programa de Mantenimiento Preventivo de planta.

 - Formato de Avisos de planta (PR-REIDE010).

**8.** **Referencia**

 - Procedimiento para Ejecución del Mantenimiento Correctivo (BCL-MAN-PRMIS03).

 - Procedimiento para liberar sanitariamente los equipos.

**9.** **Anexos**

N/A

**10.** **Aprobación**

Este procedimiento fue aprobado por los siguientes representantes de Grupo Bimbo:

|Versión: 1|Col2|
|---|---|
|**Realizado por:**Arquímedes Quintana|**Aprobado por:**Julio Humberto Agüero|
|**Fecha:**30 de octubre de 2019|**Fecha:**30 de octubre de 2019|

**11.** **Actualizaciones**

|Revisión / historia de la revisión|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Versión**|**Fecha de**<br>**revisión**|**Actualizado**<br>**por**|**Aprobado por**|**Cambios** <br>**principales**|
|**1 **|||||

6