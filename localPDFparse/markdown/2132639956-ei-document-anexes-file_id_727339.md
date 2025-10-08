---
title: Sin título
author: María Bravo
date: D:20170717152626-04'00'
language: es
type: report
pages: 43
has_toc: False
has_tables: True
extraction_quality: high
---

|DESARROLLADO POR:|FIRMA|ÁREA|
|---|---|---|
|Ricardo Guerra||Modelación y Simulación|
|Adrián González||Modelación y Simulación|
|María José Bravo||Consultoría|

|REVISADO POR:|FIRMA|ÁREA|
|---|---|---|
|Omar Araneda||Consultoría|

|APROBADO POR:|FIRMA|ÁREA|
|---|---|---|
|Vania Zorich||Gerencia Técnica|

|REVISIÓN|TIPO DE CAMBIO|FECHA|
|---|---|---|
|V 0.1|1a revisión reporte borrador de<br>entrega al cliente|7 de julio del 2017|
|V 1.0|Versión final|17 de julio del 2017|

|ID|Fuentes (ingresada al modelo)|Col3|Fact.emisión*<br>[ou/m2s]<br>E|
|---|---|---|---|
|ID|Área|Nombre|Nombre|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12|PTRILES|Cámara de recepción (purines)<br>Cámara de recepción (RILes)<br>Ecualizador<br>DAF<br>Est. Lodos (est. cilíndrico)<br>Filtro prensa<br>Desarenador<br>Cámara de recepción<br>Tornillo prensa<br>Est. Australiano (est. cilíndrico)<br>Cámara de recepción final<br>Lombrifiltro|99,001y2 <br>15,513 <br>15,513 <br>16,281 <br>103,621 <br>103,621 <br>99,001 <br>99,001 <br>103,623 <br>20,793 <br>1,321 <br>0,401|
|13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21|Zona de<br>riego|Los Naranjos<br>Vega Grande<br>Vega Chica<br>Los Sitios 1<br>Santa Marta 1<br>Santa Marta 2<br>Santa Marta 3<br>La Isla<br>Tranque de riego|0,281 y4 <br>0,281 y4 <br>0,281 y4 <br>0,281 y4 <br>0,281 y4 <br>0,281 y4 <br>0,281 y4 <br>0,281 y4 <br>0,281 y4|

|Escenario|Modelo|
|---|---|
|E1: Situación proyectada|M1: Isolíneas de olor(a)|
|E1: Situación proyectada|M2: Perfil horario|
|E1: Situación proyectada|M3: Perfil mensual|

|País|Potencial de generación<br>de olores molestos|Criterio de<br>calidad*|
|---|---|---|
|Colombia12|Alto|3 [ouE/m3]|
|Panamá13|Alto|3 [ouE/m3]|

|Sensibilidad del<br>punto de interés/a|ID|Nombre Punto<br>Receptor Sensible<br>(RS)/b|
|---|---|---|
|Alta<br>Alta<br>Alta<br>Alta|RS 1<br>RS 2<br>RS 3<br>RS 4|Vivienda 1<br>Vivienda 2<br>Vivienda 3<br>Vivienda 4|

|Receptor sensible|Col2|Concentración máxima<br>[ou/m3]<br>E|
|---|---|---|
|Receptor sensible|Receptor sensible|Percentil 98|
|RS 1<br>RS 2<br>RS 3<br>RS 4|Vivienda 1<br>Vivienda 2<br>Vivienda 3<br>Vivienda 4|<1<br><1<br><1<br><1|

|ID|Percepción<br>de olor<br>≥3 [ou/m3]<br>E|Horas de exposición<br>de olor<br>≥3 [ou/m3]<br>E|Condición de<br>molestia<br>(Si/No)|
|---|---|---|---|
|RS 1<br>RS 2<br>RS 3<br>RS 4|x <br>x <br>x <br>x|0 <br>0 <br>0 <br>0|No<br>No<br>No<br>No|

ANTECEDENTES www.ecometrika.com

ANTECEDENTES www.ecometrika.com

|ID|Fuentes odorantes|Col3|Coordenada UTM [m]<br>(WGS-84 H19S)|Col5|
|---|---|---|---|---|
|ID|Área|Nombre|X: Este|Y: Sur|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12|PTRILES|Cámara de recepción (purines)<br>Cámara de recepción (RILes)<br>Ecualizador<br>DAF<br>Estanque lodos ( estanque cilíndrico)<br>Filtro prensa<br>Desarenador<br>Cámara de recepción<br>Tornillo prensa<br>Estanque australiano (estanque cilíndrico)<br>Cámara de recepción final<br>Lombrifiltro|283.282<br>283.302<br>283.304<br>283.312<br>283.312<br>283.316<br>283.326<br>283.329<br>283.336<br>283.347<br>283.354<br>283.389|6.261.822<br>6.261.824<br>6.261.819<br>6.261.825<br>6.261.819<br>6.261.820<br>6.261.832<br>6.261.834<br>6.261.839<br>6.261.841<br>6.261.845<br>6.261.834|
|13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21|Zona de riego|Los Naranjos<br>Vega Grande<br>Vega Chica<br>Los Sitios 1<br>Santa Marta 1<br>Santa Marta 2<br>Santa Marta 3<br>La Isla<br>Tranque de riego|283.252<br>282.764<br>282.911<br>283.200<br>282.367<br>282.254<br>282.162<br>282.007<br>283.635|6.262.093<br>6.261.882<br>6.261.682<br>6.261.846<br>6.261.356<br>6.261.530<br>6.261.806<br>6.261.971<br>6.262.076|

|ID|Fuentes odorantes|Col3|Factor de<br>emisión<br>[ou /m2s]<br>E|
|---|---|---|---|
|ID|Área|Nombre|Nombre|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21|PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>PTRILES<br>Zona de riego<br>Zona de riego<br>Zona de riego<br>Zona de riego<br>Zona de riego<br>Zona de riego<br>Zona de riego<br>Zona de riego<br>Zona de riego|Cámara de recepción (purines)<br>Cámara de recepción (RILes)<br>Ecualizador<br>DAF<br>Estanque lodos ( estanque cilíndrico)<br>Filtro prensa<br>Desarenador<br>Cámara de recepción<br>Tornillo prensa<br>Estanque australiano (estanque cilíndrico)<br>Cámara de recepción final<br>Lombrifiltro<br>Los Naranjos<br>Vega Grande<br>Vega Chica<br>Los Sitios 1<br>Santa Marta 1<br>Santa Marta 2<br>Santa Marta 3<br>La Isla<br>Tranque de riego|99,00(a)(b) <br>15,51(c) <br>15,51(c) <br>16,28(a) <br>103,62(a) <br>103,62(a) <br>99,00(a) <br>99,00(a) <br>103,62(c) <br>20,79(c) <br>1,32(a) <br>0,40(a) <br>0,28(a)(d) <br>0,28(a)(d) <br>0,28(a)(d) <br>0,28(a)(d) <br>0,28(a)(d) <br>0,28(a)(d) <br>0,28(a)(d) <br>0,28(a)(d) <br>0,28(a)(d)|

|Función|Col2|Y = 0,4418*Exp(-0,4670*X)|Col4|
|---|---|---|---|
|Mínimo|0,009|Máximo|0,277|
|Media|0,084|Desv.|0,129|
|R2|0,993|RSME|0,018|

|Función|Col2|Y = 0,3156*Exp(-0,467*X)|Col4|
|---|---|---|---|
|Mínimo|0,006|Máximo|0,198|
|Media|0,060|Desv.|0,092|
|R2|0,993|RSME|0,013|

PLAN DE TRABAJO www.ecometrika.com

|ID|Fuentes|Col3|Estado|Coordenada UTM [m]<br>(WGS-84 H19S)|Col6|
|---|---|---|---|---|---|
|ID|(ingresadas al modelo)|(ingresadas al modelo)|(ingresadas al modelo)|(ingresadas al modelo)|(ingresadas al modelo)|
|ID|Área|Nombre|Nombre|X: Este|Y: Sur|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12|PTRILES|Cámara de recepción (purines)<br>Cámara de recepción (RILes)<br>Ecualizador<br>DAF<br>Estanque lodos ( estanque cilíndrico)<br>Filtro prensa<br>Desarenador<br>Cámara de recepción<br>Tornillo prensa<br>Estanque australiano (estanque cilíndrico)<br>Cámara de recepción final<br>Lombrifiltro|Proyectada|283.282<br>283.302<br>283.304<br>283.312<br>283.312<br>283.316<br>283.326<br>283.329<br>283.336<br>283.347<br>283.354<br>283.389|6.261.822<br>6.261.824<br>6.261.819<br>6.261.825<br>6.261.819<br>6.261.820<br>6.261.832<br>6.261.834<br>6.261.839<br>6.261.841<br>6.261.845<br>6.261.834|
|13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21|Zona de<br>riego|Los Naranjos<br>Vega Grande<br>Vega Chica<br>Los Sitios 1<br>Santa Marta 1<br>Santa Marta 2<br>Santa Marta 3<br>La Isla<br>Tranque de riego|Proyectada|283.252<br>282.764<br>282.911<br>283.200<br>282.367<br>282.254<br>282.162<br>282.007<br>283.635|6.262.093<br>6.261.882<br>6.261.682<br>6.261.846<br>6.261.356<br>6.261.530<br>6.261.806<br>6.261.971<br>6.262.076|

|Fuentes<br>(ingresadas al modelo)|Col2|Col3|Altura de<br>emisión[m]<br>(desde el<br>suelo)|Largo<br>[m]<br>(del área<br>que<br>emite)|Ancho<br>[m]<br>(del área<br>que emite)|Radio<br>[m]<br>(del área<br>que<br>emite)|Área [m2]<br>(del área<br>que emite)|
|---|---|---|---|---|---|---|---|
|ID|Área|Nombre|Nombre|Nombre|Nombre|Nombre|Nombre|
|1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12|PTRILES|Cámara de recepción (purines)<br>Cámara de recepción (RILes)<br>Ecualizador<br>DAF<br>Estanque lodos ( estanque cilíndrico)<br>Filtro prensa<br>Desarenador<br>Cámara de recepción<br>Tornillo prensa<br>Estanque australiano (estanque cilíndrico)<br>Cámara de recepción final<br>Lombrifiltro|0,00<br>0,00<br>0,00<br>2,50<br>3,00<br>3,70<br>1,50<br>0,00<br>2,50<br>2,40<br>0,00<br>1,00|1,20<br>1,20<br>4,30<br>5,20<br>- <br>4,60<br>3,70<br>3,40<br>1,20<br>- <br>3,40<br>40,00|1,20<br>1,20<br>4,30<br>1,90<br>- <br>1,90<br>1,10<br>3,40<br>0,66<br>- <br>3,40<br>25,00|- <br>- <br>- <br>- <br>2,90<br>- <br>- <br>- <br>- <br>8,50<br>- <br>-|1,44<br>1,44<br>18,49<br>9,88<br>6,61<br>8,74<br>4,07<br>11,56<br>0,79<br>56,75<br>11,56<br>1.000,00|
|13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21|Zona de<br>riego|Los Naranjos<br>Vega Grande<br>Vega Chica<br>Los Sitios 1<br>Santa Marta 1<br>Santa Marta 2<br>Santa Marta 3<br>La Isla<br>Tranque de riego|0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00|* <br>* <br>* <br>* <br>* <br>* <br>* <br>* <br>*|* <br>* <br>* <br>* <br>* <br>* <br>* <br>* <br>*|-<br>-<br>- <br>- <br>- <br>- <br>- <br>- <br>-|200.000,00<br>210.000,00<br>90.000,00<br>15.000,00<br>35.000,00<br>70.000,00<br>70.000,00<br>60.000,00<br>3.600,00|

PLAN DE TRABAJO www.ecometrika.com

|Receptor de Alta<br>Sensibilidad|Tierras circundantes donde:<br> Los usuarios pueden esperar gozar de un alto nivel de comodidad; y<br> Los habitantes presentes residen en la zona continuamente, o al menos<br>por períodos extensos, como parte del patrón normal del uso de la tierra.<br>Los ejemplos pueden incluir viviendas residenciales, hospitales, escuelas,<br>centros de educación y turismo o culturales.|
|---|---|
|Receptor de<br>Sensibilidad Media|Tierras circundantes donde:<br> Los usuarios podrían esperar disfrutar de un nivel razonable de<br>amenidad, pero no sería razonable que esperaran disfrutar del mismo<br>nivel de amenidad como si se tratara de su vivienda habitual; o<br> Los habitantes no residen en la zona continuamente, o al menos, no con<br>regularidad por períodos extensos, como parte del patrón normal del<br>uso de la tierra.<br>Los ejemplos pueden incluir lugares de trabajo, locales comerciales<br>minoristas y campos de deportes o recreación.|
|Receptor de Baja<br>Sensibilidad<br>|Tierras circundantes donde:<br> No sería razonable esperar el disfrute de amenidad; o<br> Existe una exposición transitoria, donde los habitantes residen sólo por<br>períodos limitados de tiempo, como parte del patrón normal del uso de<br>la tierra.<br>Los ejemplos pueden incluir zonas industriales, granjas, caminos y<br>carreteras.<br>|

|Sensibilidad del<br>punto de interés/a|ID|Nombre Punto Receptor<br>Sensible (RS)/b|Coordenadas UTM [m]<br>(WGS84-H19S)|Col5|
|---|---|---|---|---|
|Sensibilidad del<br>punto de interés/a|ID|Nombre Punto Receptor<br>Sensible (RS)/b|X: Este|Y: Sur|
|Alta<br>Alta<br>Alta<br>Alta|RS 1<br>RS 2<br>RS 3<br>RS 4|Vivienda 1<br>Vivienda 2<br>Vivienda 3<br>Vivienda 4|283.270<br>283.694<br>283.075<br>283.823|6.261.658<br>6.261.435<br>6.261.615<br>6.262.036|

|País|Actividad|Criterio de calidad|
|---|---|---|
|Colombia64|Tratamiento y disposición de residuos|3 [ouE/m3]|
|Panamá65|Otras actividades que puedan generar olores<br>molestos con una distancia de influencia de 1,000 a<br>5,000 metros|3 [ouE/m3]|

|Área|ID|Nombre|Factor de emisión<br>[ou /m2s]<br>E|TEO [ou /s]<br>E|
|---|---|---|---|---|
|PTRILES|1|Estanque australiano (estanque cilíndrico)|20,79<br>99,00<br>103,62<br>103,62<br>99,00<br>0,40<br>15,51<br>16,28<br>99,00<br>103,62<br>15,51<br>1,32|1.180|
|PTRILES|2|Cámara de recepción|Cámara de recepción|1.144|
|PTRILES|3|Filtro prensa|Filtro prensa|906|
|PTRILES|4|Estanque lodos ( estanque cilíndrico)|Estanque lodos ( estanque cilíndrico)|684|
|PTRILES|5|Desarenador|Desarenador|403|
|PTRILES|6|Lombrifiltro|Lombrifiltro|396|
|PTRILES|7|Ecualizador|Ecualizador|287|
|PTRILES|8|DAF|DAF|161|
|PTRILES|9|Cámara de recepción (purines)|Cámara de recepción (purines)|143|
|PTRILES|10|Tornillo prensa|Tornillo prensa|82|
|PTRILES|11|Cámara de recepción (RILes)|Cámara de recepción (RILes)|22|
|PTRILES|12|Cámara de recepción final|Cámara de recepción final|15|
|PTRILES|12|Cámara de recepción final|Cámara de recepción final|**5.423**|

|Área|ID|Nombre|Factor de emisión<br>[ou /m2s]<br>E|TEO [ou /s]<br>E|
|---|---|---|---|---|
|Zona de riego|13|Vega Grande|0,28<br>0,28<br>0,28<br>0,28<br>0,28<br>0,28<br>0,28<br>0,28<br>0,28|58.212|
|Zona de riego|14|Los Naranjos|Los Naranjos|55.440|
|Zona de riego|15|Vega Chica|Vega Chica|24.948|
|Zona de riego|16|Santa Marta 2|Santa Marta 2|19.404|
|Zona de riego|17|Santa Marta 3|Santa Marta 3|19.404|
|Zona de riego|18|La Isla|La Isla|16.632|
|Zona de riego|19|Santa Marta 1|Santa Marta 1|9.702|
|Zona de riego|20|Los Sitios 1|Los Sitios 1|4.158|
|Zona de riego|21|Tranque de riego|Tranque de riego|998|
|Zona de riego|21|Tranque de riego|Tranque de riego|**208.898**|

|Escenario|Modelo|Percentil|Criterio de calidad|
|---|---|---|---|
|E1: Situación operación proyectada<br>|M1: Isolíneas de olor(*)|98|3 [ouE/m3]|
|E1: Situación operación proyectada<br>|M2: Perfil horario|M2: Perfil horario|M2: Perfil horario|
|E1: Situación operación proyectada<br>|M3: Perfil mensual|M3: Perfil mensual|M3: Perfil mensual|

|Área [ha]*|Col2|0|
|---|---|---|
|Alcance<br>[km]|N|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|
|Alcance<br>[km]|NE|NE|
|Alcance<br>[km]|E|E|
|Alcance<br>[km]|SE|SE|
|Alcance<br>[km]|S|S|
|Alcance<br>[km]|SO|SO|
|Alcance<br>[km]|O|O|
|Alcance<br>[km]|NO|NO|

RESULTADOS www.ecometrika.com

|ID|Receptor sensible|Concentración máxima [ou /m3]<br>E|Col4|
|---|---|---|---|
|ID|Receptor sensible|Percentil 99,5*|Percentil 98|
|RS 1<br>RS 2<br>RS 3<br>RS 4|Vivienda 1<br>Vivienda 2<br>Vivienda 3<br>Vivienda 4|<3<br><1<br><3<br><1|<1<br><1<br><1<br><1|

|Mes RS 1 RS 2 RS 3 RS 4|Col2|
|---|---|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|
|Total|**0 **<br>**0 **<br>**0 **<br>**0 **|

|Hora del día RS 1 RS 2 RS 3 RS 4|Col2|
|---|---|
|0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 <br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23|0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0 <br>0|
|Total|**0 **<br>**0 **<br>**0 **<br>**0 **|

|ID|Percepción de olor|Horas de<br>exposición de olor|Condición de<br>molestia|
|---|---|---|---|
|ID|≥ 3 [ouE/m3]|≥ 3 [ouE/m3]|(Si/No)|
|RS 1<br>RS 2<br>RS 3<br>RS 4|x <br>x <br>x <br>x|0 <br>0 <br>0 <br>0|No<br>No<br>No<br>No|

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|283.260,81|6.261.695,85|19 S|WGS 84|

|Col1|Rosa de vientos|Col3|Distribución de velocidad del viento|Características|
|---|---|---|---|---|
|Anual Nocturno<br>(00:00 a 6:59 horas)|||<br>21,82<br>27,63<br>33,41<br>11,90<br>3,08<br>1,01<br>0,66<br>0,12<br>0,16<br>0,20<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire predominaron desde la<br>componente NE con un 15% de la frecuencia.<br>Adicionalmente, se exhibieron vientos desde<br>ENE (9%) y NNE (8%). La intensidad del viento<br>se caracterizó por brisas de carácter muy débil.<br> <br>Velocidad promedio de viento: 1,18 [m/s].<br> <br>Frecuencia de vientos calmos: 21,82 %.|
|Anual AM<br>(7:00 a 14:59 horas)|||<br>4,06<br>13,01<br>21,55<br>12,60<br>9,36<br>10,31<br>11,00<br>10,83<br>5,98<br>1,30<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de viento predominaron desde<br>dirección OSO con un 27%. En menor<br>frecuencia, provinieron vientos desde Oeste<br>(16%) y SO (15%). Estos vientos circularon con<br>intensidades que variaron de brisa débil a<br>moderada.<br> <br>Velocidad promedio de viento: 3,38 [m/s].<br> <br>Frecuencia de vientos calmos: 4,06 %.|
|Anual PM<br>(15:00 a 23:59 horas)|||<br>4,43<br>7,95<br>19,31<br>19,73<br>13,51<br>12,17<br>10,44<br>7,29<br>3,73<br>1,43<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, las masas de aire<br>provinieron desde el OSO la mayor parte del<br>tiempo con un 25% de la frecuencia. Seguido,<br>se exhibieron vientos desde SO (18%) y SSO<br>(15%). La intensidad asociada, varió de brisas<br>débiles a moderadas.<br> <br>Velocidad promedio de viento: 3,30 [m/s].<br> <br>Frecuencia de vientos calmos: 4,43 %.|