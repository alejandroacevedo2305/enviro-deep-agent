---
title: 1
author: fgall
date: D:20200908090912-03'00'
language: es
type: report
pages: 8
has_toc: False
has_tables: True
extraction_quality: high
keywords: [PROCEDIMIENTO]
---

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

|Registro de Modificaciones|Col2|Col3|Col4|
|---|---|---|---|
|No Versión|Fecha|Motivo de la modificación|Páginas elaboradas o modificadas|
|002|Haga clic o<br>pulse aquí para<br>escribir texto.|Haga clic o pulse aquí para escribir texto.|Haga clic o pulse aquí para escribir<br>texto.|
|003|Haga clic o<br>pulse aquí para<br>escribir texto.|Haga clic o pulse aquí para escribir texto.|Haga clic o pulse aquí para escribir<br>texto.|

Página 1 de 8

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

**1.** **OBJETIVO**

El objetivo este procedimiento es definir la forma de planificar las actividades de mantenimiento, de modo que permita
priorizar las ordenes de trabajo de los activos críticos de las Plantas, Oficinas y la Flota Granel, considerando: los niveles
de riesgos de los equipos, los resultados del análisis de los incidentes de funcionamiento, las probabilidades y
consecuencias de sus eventuales fallas, los planes de inversión (reposición o reemplazo) y la gestión de repuestos. [i]

**2.** **ALCANCE**

Aplica a los activos e instalación asociados a la infraestructura productiva directa que se encuentran en los sitios del Grupo
Abastible y en la cadena de suministro de distribución de GL hasta el límite de responsabilidad del Grupo Abastible.

|DEFINICIONES|Col2|
|---|---|
|**GL**|Gas Licuado del Petróleo|
|**Orden de Mantenimiento**|Orden de Trabajo del módulo PM de SAP que permite planificar actividades de<br>mantenimiento incorporando el equipo donde se realizará, los materiales y<br>repuestos, el personal y los costos involucrados.|
|**PM02**|Orden de Mantenimiento relacionada con equipos de Plantas y Oficinas.|
|**FLG02**|Orden de Mantenimiento con la Flota Granel.|
|**ZPM2**|Orden de Mantenimiento relacionada con Redes Contra Incendios.|
|**Sistema GO**|Sistema de Gestión Operacional orientado al mejoramiento continuo de la<br>gestión de operaciones.|
|**Tarjetas GO**|La siguiente herramienta tiene como principal objetivo garantizar un sistema<br>eficiente de reportes de anomalías en condiciones de trabajo, sean de<br>seguridad, operativas, máquinas, etc. También permiten registrar y hacer<br>gestión de las solicitudes operacionales. Existen tarjetas rojas, amarillas y<br>azules.<br>La resolución de las tarjetas rojas corresponde a mantenimiento y también las<br>tarjetas amarillas (seguridad) que le sean directamente asignadas.<br>|

i Los contenidos de este documento abarcan los entregables relacionados con los puntos 3.2.2.2, 3.2.2.4 y 3.2.5.2 del
documento del **Elemento 7 Integridad Mecánica y Confiabilidad del modelo OIEM** y específicamente al entregable
denominado: “Procedimiento para priorización de ordenes de trabajo, investigación de malos actores y gestión de
repuestos”.

Página 2 de 8

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

|MTBF|Tiempo Medio entre Fallas.|
|---|---|
|**MTTR**|Tiempo Medio de Reparación.|
|**RESERVA**|En SAP corresponde a una orden por equipo o material de almacén o bodega,<br>que se utilizará en una fecha próxima.|

**4.** **FLUJOGRAMA DE INFORMACION**

Página 3 de 8

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

**5.** **ROLES Y RESPONSABILIDADES**

|Subgerente de Mantenimiento<br>Plantas y Oficinas|Responsable del mantenimiento de equipos e infraestructura productiva de Plantas y<br>Oficinas|
|---|---|
|**Jefe de Planificación y**<br>**Confiabilidad**|Responsable del proceso de planificación del mantenimiento de equipos e<br>infraestructura productiva de plantas, además del proceso de mejora continua<br>mediante la eliminación de Pérdidas.|
|**Equipo de Mantenedores**|Jefaturas, coordinadores, supervisores, mecánicos y eléctricos responsables de la<br>ejecución de los planes de mantenimiento.|
|**Planificador de Mantenimiento**|Responsable de preparar paquetes semanales de tareas de mantenimiento con<br>horizonte de 12 semanas, considerando la estrategia definida para cada tipo de equipo<br>y de realizar las coordinaciones necesarias para asegurar que se disponga del stock<br>de repuestos en bodega para la ejecución de los trabajos programados.|
|**Programador de Mantenimiento**|Responsable de entregar los programas semanales con horizonte 1 semana, generar<br>Ordenes de Mantenimiento, Carga de HH, asignar tiempos de ejecución reservar<br>repuestos y asegurar la disponibilidad de los equipos con producción y distribución.|
|**Ingeniero de Confiabilidad**|Mejorar los planes de mantenimiento preventivo incorporando los hallazgos de los<br>análisis de las fallas y reducir los costos de la actividad, sin sacrificar la confiabilidad e<br>integridad mecánica.|

**6.** **DESCRIPCIÓN**

|6.1|Planificación de las Actividades de Mantenimiento de Activos Fijos.|Responsable|
|---|---|---|
||6.1.1. Las actividades de mantenimiento de los activos fijos se planifican con un<br>horizonte de 12 semanas.<br>6.1.2. La planificación de las actividades se realiza considerando:<br>• <br>Mantenimiento Preventivo Equipos de Planta PM02.<br>• <br>Mantenimiento Preventivo Flota Granel FLG02.<br>• <br>Mantenimiento Red Contra Incendio ZPM2<br>6.1.2.2 Las recomendaciones del análisis de incidentes ocurridos con anterioridad<br>(Avisos).<br>6.1.2.3 Los recursos asignados en el presupuesto de cada año.<br>6.1.2.4 Los avisos generados por las tarjetas rojas del sistema GO.<br>6.1.2.5 Las tarjetas Amarillas del Sistema GO asignadas específicamente a<br>mantenimiento.|Jefe de<br>Planificación y<br>Confiabilidad|

Página 4 de 8

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

|6.2|Elaboración del Plan de Mantenimiento de 12 semanas|Responsable|
|---|---|---|
||6.2.1 Distribuye las actividades de mantenimiento en cada una de las 12 semanas.|Jefe de<br>Planificación y<br>Confiabilidad<br> <br>Planificador de<br>Mantenimiento<br>|
|**6.3**|**Generar reserva de repuestos, componentes y materiales**|**Responsable**|
||6.3.1 Generar reserva de materiales y repuestos a Bodega para cubrir las<br>necesidades de las próximas 12 semanas, chequear con bodega eventuales quiebres<br>de stock y pedidos en curso para asegurar que para la realización de las actividades<br>se contará con los materiales necesarios.<br> <br>6.3.2 Participar en el proceso de compra de repuestos anuales de exportación, junto<br>con la ejecución del mantenimiento y compras generales.<br>|Planificador de<br>Mantenimiento<br> <br>Programador de<br>Mantenimiento<br>|
|**6.4**|**Priorización de las Ordenes de Mantenimiento **|**Responsable**|
||Para la elaboración del Plan de 12 semanas considerará las siguientes reglas de<br>priorización:<br>6.4.1 Las actividades de mantenimiento que correspondan a equipos críticos tendrán<br>prioridad 1, tal como lo establece el procedimiento de equipos críticos.<br>6.4.2 Las ordenes de mantenimiento correctivo, preventivo o predictivo relacionadas<br>con equipos críticos, deben tener prioridad 1<br>6.4.3 Las actividades de mantenimiento de equipos críticos solo pueden ser<br>modificadas hasta en un 20% del intervalo de llamada, con un tope de treinta días.<br>Fuera de esta tolerancia el área de planificación deberá obtener aprobación escrita<br>mediante el procedimiento de aplazamiento.<br>6.4.4 Los avisos correctivos y sintomáticos que correspondan a equipos críticos<br>deben ser resueltos en un plazo no mayor a 14 días.<br>6.4.5 Las ordenes de mantenimiento preventivo o correctivo, para equipos que no<br>fueron identificados como equipos críticos, deben tener prioridad 2.|Planificador de<br>Mantenimiento<br> <br>Programador de<br>Mantenimiento<br>|
|<br>** 6.5**|**Reunión de Programación semanal**|**Responsable**|
||6.5.1 Enviará semanalmente el Programa de mantenimiento de la semana +1 y el<br>pre-programa de la semana +2, el que será revisado y validado en la reunión de<br>programación (jueves de cada semana).<br>La reunión de Programación tendrá los siguientes objetivos:|Programador de<br>Mantenimiento<br>|

Página 5 de 8

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

|Col1|• Verificar el cumplimiento de las actividades programadas para la semana<br>(-1).<br>• Priorizar los avisos que se generaron en la semana anterior (-1).<br>• Establecer las fechas de ejecución de las actividades incorporadas en los<br>ítems de imprevistos.<br>• Aprobar el plan para la semana +1.<br>• Entregar a la ejecución del mantenimiento el pre-programa de la semana<br>(+2)|Equipo de<br>Mantenimiento|
|---|---|---|
|<br>**6.6**|**Análisis de Incidentes**|**Responsable **|
||6.6.1 Todos aquellos eventos de pérdida de contención serán analizados por el área<br>de confiabilidad a fin de determinar la causa raíz y contramedidas necesarias para<br>evitar la recurrencia, mediante un análisis de Falla (ADF).<br>6.6.2 Los hallazgos obtenidos en las inspecciones preventivas deben generar un<br>aviso subsecuente de reparación que puede ser inmediato o programado.<br>6.6.3 En ambos casos, la información se debe utilizar en el análisis de la efectividad<br>de las inspecciones y si es necesario realizar mejoras en dicho plan o migrar a otra<br>estrategia de mantenimiento.<br>6.6.4 Todo incidente de pérdida de contención que implique potencialmente una falla<br>de algún componente será analizado por el área de mantenimiento a fin de dar<br>soporte técnico a la investigación.<br>|Ingeniero de<br>Confiabilidad<br> <br>|
|**6.7**|**Inversión**|**Responsable**|
||6.7.1 El área de confiabilidad deberá tener información de aplicación de los planes<br>de mantenimiento, para tomar decisiones respecto de sus costos, para adoptar<br>decisiones de reemplazo cuando corresponda.<br>6.7.2 Por ello todas las intervenciones en los equipos deber ser capturado mediante<br>una Orden de Mantenimiento en SAP y registrar los costos asociados a la mantención<br>de dicho activo.<br>6.7.3 Anualmente, evaluará los costos de mantenimiento vs el valor residual del activo<br>y evaluará el costo/beneficio de la sustitución de activos. A la hora de implementar<br>mejoras en los planes de mantenimiento se debe tener presente el beneficio costo, a<br>fin de proponer en lo posible mejoras con B/C mayores a 1, salvo en los casos en<br>que el reemplazo corresponda a una mejora en la seguridad.<br>6.7.4 Para priorizar las decisiones de reemplazo se utilizarán los indicadores MTBF<br>y MTTR .|Ingeniero de<br>Confiabilidad<br>|

Página 6 de 8

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

|6.8|Gestión de repuestos|Responsable|
|---|---|---|
||6.8.1 Actualizar los repuestos requeridos en mantenimientos preventivos<br>garantizando que estos se encuentren en stock en la bodega de materiales.<br>6.8.2 Verificar periódicamente que el stock de los repuestos a ser utilizado en plan de<br>10 semanas se encuentre disponible.<br>6.8.3 Verificar que los repuestos se mantengan con el parámetro de reposición<br>automática requerido MRP.<br>6.8.4 Revisar los principales costos de mantenimiento, en lo que ha repuestos se<br>refiere, a fin de buscar oportunidades de mejora.|Planificador de<br>Mantenimiento<br> <br>Programador de<br>Mantenimiento<br>|

**7.** **EXCEPCIONES - ACTIVIDADES DE CONTINGENCIA**

No aplica

**8.** **RIESGO**

|Riesgo: Desabastecimiento de repuestos para equipos críticos|Col2|Col3|Col4|
|---|---|---|---|
|Control: Participar colaborativamente y monitorear la compra de repuestos anuales de exportación|Control: Participar colaborativamente y monitorear la compra de repuestos anuales de exportación|Control: Participar colaborativamente y monitorear la compra de repuestos anuales de exportación|Control: Participar colaborativamente y monitorear la compra de repuestos anuales de exportación|
|Frecuencia|Tipo|Clasificación|Responsable|
|Anual|Preventivo|Manual|Jefe de Planificación|

|Riesgo: Falla de equipos críticos por planes de mantenimiento incorrectos|Col2|Col3|Col4|
|---|---|---|---|
|Control: Verificar activamente la frecuencia y las actividades de mantenimiento para la integridad de los equipos críticos|Control: Verificar activamente la frecuencia y las actividades de mantenimiento para la integridad de los equipos críticos|Control: Verificar activamente la frecuencia y las actividades de mantenimiento para la integridad de los equipos críticos|Control: Verificar activamente la frecuencia y las actividades de mantenimiento para la integridad de los equipos críticos|
|Frecuencia|Tipo|Clasificación|Responsable|
|Anual|Preventivo|Manual|Jefe de Planificación|

Página 7 de 8

|Col1|PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO|Versión|1|
|---|---|---|---|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Fecha Elaboración<br>|03-09-2020|
||PROCEDIMIENTO DE<br>PLANIFICACIÓN DE LAS<br>ACTIVIDADES DE MANTENIMIENTO<br> <br> <br>|Código|ABA-MAN-ZZZ-<br>0000|

**9.** **INDICADORES DE PROCESO**

|Nombre del indicador:|Col2|
|---|---|
|Proceso que mide:||
|Objetivo:||
|Fórmula:||
|Unidad de medida:||
|Responsable:||
|Frecuencia||
|Criterio de evaluación:||

**10.** **REFERENCIAS**

**-**
Guidelines for Asset Integrity Management 2018

|11. REGISTROS|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Nombre del registro|Nombre del registro|Código o<br>número del<br>registro|Custodia temporal|Custodia temporal|Custodia temporal|Custodia definitiva|Custodia definitiva|Custodia definitiva|
|Nombre del registro|Nombre del registro|Código o<br>número del<br>registro|Responsable|Tiempo de<br>conservación|Lugar de<br>almacenamiento|Responsable|Tiempo de<br>conservación|Lugar de<br>almacenamiento|
|1.|||||||||
|2.|||||||||
|3.|||||||||

12. **ANEXOS**

No Aplica

Página 8 de 8