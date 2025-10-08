---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 77
has_toc: False
has_tables: True
extraction_quality: high
---

Reporte:

**P5127**
**Modelación de Dispersión Odorante**
**Planta Productora de Ingredientes para la Nutrición Animal**

Compañía Contratante:

**Chilemink Sur SPA.**

Solicitante:
**Sr. Rafael Anrique M. - Gerente General**

Operación y Diseño del Servicio

ECOMETRIKA
Av. Américo Vespucio 2296 - Conchalí - Santiago - Chile

Responsables por Ecometrika

I.A. Ricardo Guerra F. I.A. Vania Zorich M., MsC.

**Noviembre 2016**

**Rev 1.0**

|DESARROLLADO POR:|FIRMA|ÁREA|
|---|---|---|
|Adrián González||Modelación y Simulación|
|Evelyn Contreras||Modelación y Simulación|
|Ricardo Guerra||Modelación y Simulación|

|REVISADO POR:|FIRMA|ÁREA|
|---|---|---|
|Omar Araneda||Consultoría|

|APROBADO POR:|FIRMA|ÁREA|
|---|---|---|
|Vania Zorich||Gerencia Técnica|

|REVISIÓN|TIPO DE CAMBIO|FECHA|
|---|---|---|
|V 0.1|1a revisión reporte borrador de<br>entrega al cliente|28 de noviembre de 2016|
|V 1.0|Versión final|15 de diciembre de 2016|

CONTROL DE CAMBIOS www.ecometrika.com

GLOSARIO www.ecometrika.com

GLOSARIO www.ecometrika.com

|Área|Fuente emisora|Factor de<br>emisión<br>[ou/m2s]<br>E|
|---|---|---|
|Edificio de procesos|Portón galpón|3,68(a)|
|Edificio de procesos|Biofiltro|0,27(a)|

|Receptor Sensible (RS)(a)|Sensibilidad(b)|Distancia al<br>perímetro de<br>la planta [km]|
|---|---|---|
|Hospital Lautaro|Alta|4,08|
|Plaza de Armas Lautaro|Media|3,21|
|Cementerio Lautaro|Media|2,40|
|Parque Isabel Riquelme|Media|2,00|
|Frente a planta Aguas Araucanía|Media|0,06|
|Cancha de tiro Vista Hermosa|Media|0,10|
|Centro deportivo INACAP|Media|3,18|
|Consultorio Pillanlelbún|Alta|7,70|

|Escenario|Modelo|
|---|---|
|E1: Situación proyectada|M1: Isolíneas de olor(*)|

RESUMEN EJECUTIVO www.ecometrika.com

|País|Potencial de generación<br>de olores molestos|Criterio de<br>calidad(*)|
|---|---|---|
|Panamá7|Alto|3 [ouE/m3]|
|Colombia8|Alto|3 [ouE/m3]|
|España Cataluña9|Alto|3 [ouE/m3]|

|Receptor sensible|Col2|Concentración<br>máxima<br>[ou/m3]<br>E|Col4|
|---|---|---|---|
|Receptor sensible|Receptor sensible|Percentil<br>99,5|Percentil<br>98|
|RS1|Hospital Lautaro|<1|<1|
|RS2|Plaza de Armas Lautaro|<1|<1|
|RS3|Cementerio Lautaro|<1|<1|
|RS4|Parque Isabel Riquelme|<1|<1|
|RS5|Frente a planta Aguas Araucanía|<1|<1|
|RS6|Cancha de tiro Vista Hermosa|<1|<1|
|RS7|Centro deportivo INACAP|<1|<1|
|RS8|Consultorio Pillanlelbún|<1|<1|

RESUMEN EJECUTIVO www.ecometrika.com

RESUMEN EJECUTIVO www.ecometrika.com

ÍNDICE www.ecometrika.com

ÍNDICE www.ecometrika.com

ANTECEDENTES www.ecometrika.com

ANTECEDENTES www.ecometrika.com

OBJETIVOS www.ecometrika.com

ALCANCES www.ecometrika.com

|Fuente<br>(ingresada al modelo)|Col2|Col3|TEO<br>[ou /h]<br>E|TEO<br>[ou /s]<br>E|Área<br>[m2]|TEO<br>[ou /m2s]<br>E|
|---|---|---|---|---|---|---|
|ID|Área|Nombre|Nombre|Nombre|Nombre|Nombre|
|1|Edificio de proceso|Portón de acceso<br>Biofiltro|2.000.000<br>143.500|556<br>40|151<br>150|3,68<br>0,27|
|2|2|2|2|2|2|2|

ALCANCES www.ecometrika.com

ALCANCES www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

|Fuente<br>(ingresada al modelo)|Col2|Col3|Estado|Ingreso al<br>modelo como<br>fuente de tipo|Coordenada de localización<br>UTM [m]|Col7|
|---|---|---|---|---|---|---|
|ID|Área|Nombre|Nombre|Nombre|X: Este|Y: Sur|
|1|Edificio de proceso|Portón de acceso<br>Biofiltro|proyectado <br>proyectado|areal <br>areal|722.799<br>722.807|5.278.567<br>5.728.587|
|2|2|2|2|2|2|2|

|Fuente<br>(ingresada al modelo)|Col2|Col3|Altura de<br>emisión[m]<br>(desde el suelo)|Largo [m]<br>(del área que<br>emite)|Ancho [m]<br>(del área que<br>emite)|
|---|---|---|---|---|---|
|ID|Área|Nombre|Nombre|Nombre|Nombre|
|1 <br>2|Edificio de proceso|Portón de acceso<br>Biofiltro|5,24<br>0,00(a)|19,44<br>15,00|7,76<br>10,00|

PLAN DE TRABAJO www.ecometrika.com

PLAN DE TRABAJO www.ecometrika.com

|Receptor de Alta<br>Sensibilidad|Tierras circundantes donde:<br> Los usuarios pueden esperar gozar de un alto nivel de comodidad; y<br> Los habitantes presentes residen en la zona continuamente, o al menos<br>por períodos extensos, como parte del patrón normal del uso de la tierra.<br>Los ejemplos pueden incluir viviendas residenciales, hospitales, escuelas,<br>centros de educación y turismo o culturales.|
|---|---|
|Receptor de<br>Sensibilidad Media|Tierras circundantes donde:<br> Los usuarios podrían esperar disfrutar de un nivel razonable de<br>amenidad, pero no sería razonable que esperaran disfrutar del mismo<br>nivel de amenidad como si se tratara de su vivienda habitual; o<br> Los habitantes no residen en la zona continuamente, o al menos, no con<br>regularidad por períodos extensos, como parte del patrón normal del<br>uso de la tierra.<br>Los ejemplos pueden incluir lugares de trabajo, locales comerciales<br>minoristas y campos de deportes o recreación.|
|Receptor de Baja<br>Sensibilidad|Tierras circundantes donde:<br> No sería razonable esperar el disfrute de amenidad; o<br> Existe una exposición transitoria, donde los habitantes residen sólo por<br>períodos limitados de tiempo, como parte del patrón normal del uso de<br>la tierra.<br>Los ejemplos pueden incluir zonas industriales, granjas, caminos y<br>carreteras.|

PLAN DE TRABAJO www.ecometrika.com

|Sensibilidad<br>del punto<br>de interés/a|Punto Receptor Sensible (RS)|Col3|Coordenadas UTM [m]<br>(WGS84-H18S)|Col5|Distancia al<br>perímetro de<br>la planta [km]|Orientación<br>respecto a la<br>instalación|
|---|---|---|---|---|---|---|
|Sensibilidad<br>del punto<br>de interés/a|Punto Receptor Sensible (RS)|Punto Receptor Sensible (RS)|Este|Sur|Sur|Sur|
|Alta|RS1|Hospital Lautaro|723.167|5.732.693|4,08|N|
|Media|RS2|Plaza de Armas Lautaro|723.573|5.731.780|3,21|N-NNE|
|Media|RS3|Cementerio Lautaro|722.515|5.730.984|2,40|N|
|Media|RS4|Parque Isabel Riquelme|723.873|5.730.427|2,00|NNE|
|Media|RS5|Frente a planta Aguas Araucanía|722.951|5.728.679|0,06|N|
|Media|RS6|Cancha de tiro Fundo Vista Hermosa|722.691|5.728.420|0,10|O|
|Media|RS7|Centre Deportivo INACAP|722.097|5.725.302|3,18|S-SSO|
|Alta<br>|RS8<br>|Consultorio Pillanlelbún<br>|721.630<br>|5.720.782<br>|7,70<br>|S-SSO|

PLAN DE TRABAJO www.ecometrika.com

|Criterio de<br>calidad|Ofensividad|Actividad|
|---|---|---|
|CP98-1hr|CP98-1hr|CP98-1hr|
|3 [ouE/m3]|Más ofensivos|Fabricación de celulosa, pesqueras y procesamiento de<br>productos del mar, sitios de disposición final de residuos,<br>plantas faenadoras de animales, refinerías de petróleo,<br>curtiembres y plantas recuperadoras de molibdeno.|
|5 [ouE/m3]|Moderadamente<br>ofensivos|Planteles y establos de crianza de animales, plantas de<br>tratamiento de aguas servidas, industria siderúrgica,<br>fabricación de inulina.|
|7 [ouE/m3]|Menos ofensivos|Cervecerías, procesadoras de café y confiterías.|

PLAN DE TRABAJO www.ecometrika.com

|País|Actividad|Potencial de<br>generación de<br>olores molestos|Criterio de<br>calidad(*)|
|---|---|---|---|
|Panamá59|Procesamiento de restos animales para la<br>elaboración de productos tales como sebo, grasa,<br>alimentos a base de hueso y proteína animal|Alto|3 [ouE/m3]|
|Colombia60|Tratamiento térmico de subproductos de animales|Alto|3 [ouE/m3]|
|España - Cataluña61|Aprovechamiento de subproductos de origen animal|Alto|3 [ouE/m3]|

PLAN DE TRABAJO www.ecometrika.com

|ID|Área|Fuente|Factor de<br>emisión<br>[ou /m2s]<br>E|TEO [ou /s]<br>E|% aporte|
|---|---|---|---|---|---|
|1|Edificio de proceso|Portón Galpón|3,68(a)|555,56|93,31%|
|2|2|Biofiltro|0,27(a)|39,86|6,69%|
|2|2|Biofiltro|0,27(a)|595,42|100,00%|

PLAN DE TRABAJO www.ecometrika.com

|Escenario|Modelo|Percentil|Criterio de calidad|
|---|---|---|---|
|E1: Situación proyectada<br>|M1: Isolíneas de olor(*) <br>|98|3 [ouE/m3]|

RESULTADOS www.ecometrika.com

RESULTADOS www.ecometrika.com

|Receptor sensible|Col2|Concentración máxima [ou /m3]<br>E|Col4|
|---|---|---|---|
|Receptor sensible|Receptor sensible|Percentil 99,5|Percentil 98|
|RS1|Hospital Lautaro|<1|<1|
|RS2|Plaza de Armas Lautaro|<1|<1|
|RS3|Cementerio Lautaro|<1|<1|
|RS4|Parque Isabel Riquelme|<1|<1|
|RS5|Frente a planta Aguas Araucanía|<1|<1|
|RS6|Cancha de tiro Vista Hermosa|<1|<1|
|RS7|Centro deportivo INACAP|<1|<1|
|RS8|Consultorio Pillanlelbún|<1|<1|

RESULTADOS www.ecometrika.com

CONCLUSIÓN www.ecometrika.com

RECOMENDACIONES www.ecometrika.com

BIBLIOGRAFÍA www.ecometrika.com

BIBLIOGRAFÍA www.ecometrika.com

ANEXO DE RESULTADOS www.ecometrika.com

ANEXO DE RESULTADOS www.ecometrika.com

ANEXO
**Meteorología**

**P5127**

**Chilemink Sur SPA**
**Planta Productora de Ingredientes para la Nutrición Animal**

GLOSARIO www.ecometrika.com

GLOSARIO www.ecometrika.com

ÍNDICE www.ecometrika.com

ÍNDICE www.ecometrika.com

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|722.807,93|5.728.556,28|18 S|WGS 84|

|Ciclo|Descripción|
|---|---|
|Anual|12 meses<br>Enero a diciembre|
|Estacional|Verano<br>22 de diciembre a 21 de marzo<br>Otoño<br>22 de marzo a 21 de junio<br>Invierno<br>22 de junio a 23 de septiembre<br>Primavera<br>24 de septiembre a 21 de diciembre|
|Horario|Nocturno<br>00:00 a 06:59<br>AM<br>07:00 a 14:59<br>PM<br>15:00 a 23:59|

ANÁLISIS METEOROLÓGICO www.ecometrika.com

|Col1|Rosa de viento|Col3|Distribución de velocidad del viento|Características|
|---|---|---|---|---|
|Anual Nocturno|||9,51<br>17,89<br>32,45<br>14,52<br>8,26<br>6,11<br>3,37<br>3,29<br>1,88<br>2,74<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>El viento provino con mayor frecuencia<br>desde dirección N (20%) y desde NNO<br>(14%). La magnitud del viento osciló<br>mayormente en el rango de 0,5 a 3 [m/s],<br>descrito a brisa débil.<br> <br>La velocidad media del viento fue de 3,21<br>[m/s].<br> <br>La frecuencia de vientos calmos exhibió un<br>9,51%.|
|Anual AM|||3,56<br>6,75<br>14,83<br>15,92<br>16,61<br>16,61<br>11,68<br>6,58<br>3,60<br>3,87<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Los campos de vientos describieron mayor<br>frecuencia desde las siguientes direcciones:<br>S (18%), SSO (18%) y N (18%). La<br>magnitud del viento fue variable, está osciló<br>mayormente en el rango de 1 a 6 [m/s]<br>exhibiendo<br>brisas<br>del<br>tipo<br>débil<br>a <br>moderada.<br> <br>El viento promedio alcanzó 2,31 [m/s].<br> <br>La frecuencia de vientos en calma fue de<br>3,56%.|
|Anual PM|||3,50<br>7,70<br>18,66<br>16,23<br>14,40<br>15,37<br>11,78<br>6,79<br>2,98<br>2,59<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Las masas de aire provinieron con mayor<br>frecuencia desde SSO (20%) y SO (18%).<br>En menor valor se reportaron vientos desde<br>N (13%). La velocidad del viento osciló<br>mayormente en el rango de 1 a 6 [m/s],<br>variando de brisa muy débil a moderada.<br> <br>La velocidad promedio fue de 3,69 [m/s].<br> <br>Los vientos en calma describieron una<br>frecuencia igual a 3,50%.|

ANÁLISIS METEOROLÓGICO www.ecometrika.com

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Verano Nocturno||||13,33<br>16,98<br>36,98<br>14,76<br>6,98<br>6,03<br>2,54<br>1,75<br>0,48<br>0,16<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Las masas de aire provinieron mayormente<br>desde dirección S (14%) y desde SSO (14%).<br>En menor medida desde NNO (10%) y N (9%)<br>La magnitud del viento osciló principalmente en<br>el rango de 1 a 2 [m/s], velocidad descrita a<br>brisa muy débil.<br> <br>El promedio de velocidad del viento alcanzó<br>1,84 [m/s].<br> <br>Los vientos en condición de calma exhibieron<br>una frecuencia de un 13,33%.|
|Verano AM||||2,36<br>3,89<br>11,53<br>16,39<br>15,00<br>22,22<br>14,58<br>9,58<br>3,47<br>0,97<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>El viento provino con mayor frecuencia desde<br>dirección SSO (30%) y desde S (26%). La<br>velocidad de las masas de aire fue variable,<br>concentrándose en el rango de 2 a 6 [m/s] y<br>siendo caracterizada a brisa moderada.<br> <br>La velocidad en promedio correspondió a 3,88<br>[m/s].<br> <br>La frecuencia de vientos calmos fue de 2,36%.|
|Verano PM||||2,47<br>4,57<br>12,35<br>10,86<br>12,72<br>17,65<br>19,63<br>14,44<br>4,44<br>0,86<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Los campos de viento describieron con mayor<br>frecuencia dirección desde SO (31%) y desde<br>SSO (29%). La magnitud del viento se<br>mantiene variable, aumentando en rango de 5<br>a 7 [m/s], descrita a brisa moderada.<br> <br>El viento promedio fue de 4,15 [m/s].<br> <br>Los vientos calmos alcanzaron una frecuencia<br>equivalente a 2,47%.|

ANÁLISIS METEOROLÓGICO www.ecometrika.com

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Otoño Nocturno||||6,21<br>16,46<br>28,26<br>14,44<br>9,78<br>6,99<br>4,66<br>4,97<br>2,95<br>5,28<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>El viento predominó desde dirección N (27%).<br>En menor valor se exhibieron masas de aire<br>desde NNO (16%) y NO (9%). La magnitud del<br>viento se concentró mayormente en intervalo<br>de 0,5 a 2 [m/s], caracterizado a brisa muy<br>débil. Se observó en menor frecuencia vientos<br>mayores a 8 [m/s].<br> <br>La velocidad promedio del viento fue de 2,83<br>[m/s].<br> <br>Los vientos calmos describieron una frecuencia<br>igual a 6,21%.|
|Otoño AM||||4,62<br>7,20<br>15,35<br>14,95<br>15,76<br>12,36<br>8,97<br>5,84<br>5,98<br>8,97<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Los campos de viento exhibieron predominio<br>desde dirección N (29%). La magnitud del<br>viento se concentró en el rango de 1 a 5 [m/s]<br>(brisa débil) y se observó un aumento del rango<br>sobre 8 [m/s] (brisa moderada).<br> <br>El promedio de velocidad de viento fue de 3,94<br>[m/s].<br> <br>La frecuencia de vientos en calma correspondió<br>a 4,62%.|
|Otoño PM||||2,78<br>8,70<br>18,36<br>16,91<br>15,10<br>14,61<br>8,21<br>5,68<br>4,59<br>5,07<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Las masas de aire provinieron principalmente<br>desde dirección N (21%), SSO (17%) y NNO<br>(11%).<br>La<br>magnitud<br>del<br>viento<br>osciló<br>mayormente en rango de 1 a 5 [m/s],<br>caracterizada a brisa débil. Se exhibió en<br>menor valor vientos superiores a 8 [m/s].<br> <br>La velocidad promedio del viento fue de 3,59<br>[m/s].<br> <br>Los vientos inferiores a 0,5 [m/s] describieron<br>una frecuencia igual a 2,78%.|

ANÁLISIS METEOROLÓGICO www.ecometrika.com

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Invierno Nocturno||||6,08<br>15,50<br>31,31<br>14,13<br>7,14<br>6,23<br>4,56<br>5,78<br>3,95<br>5,32<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>El viento predominó desde dirección N (30%),<br>en menor valor provinieron vientos desde NNO<br>(19%), NO (11%) y NNE (10%). La magnitud<br>del viento osciló mayormente en intervalo de<br>0,5 a 3 [m/s], caracterizada a brisa muy débil.<br>Se exhibió en menor valor vientos superiores a<br>8 [m/s].<br> <br>La velocidad en promedio fue de 2,85 [m/s].<br> <br>La frecuencia de vientos calmos alcanzó 6,08%.|
|Invierno AM||||4,52<br>9,84<br>19,81<br>12,50<br>13,96<br>13,56<br>11,04<br>6,38<br>3,59<br>4,79<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Las masas de aire predominaron desde<br>dirección N (31%). En una frecuencia menor, se<br>exhibieron vientos desde NNO (13%) y S<br>(13%). La magnitud del viento fue frecuente en<br>el intervalo de 1 a 5 [m/s], descrita a brisas del<br>tipo débil y moderada.<br> <br>El promedio de la velocidad fue de 3,52 [m/s].<br> <br>Los vientos en condición de calmos obtuvieron<br>una frecuencia de 4,52%.|
|Invierno PM||||3,78<br>8,87<br>26,36<br>21,99<br>12,41<br>10,76<br>6,26<br>4,26<br>1,65<br>3,66<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Se observó predominio de vientos desde<br>dirección<br>N <br>(23%).<br>Adicionalmente<br>se<br>exhibieron vientos desde NNO (11%) y SSO<br>(11%).<br>La<br>magnitud<br>del<br>viento<br>osciló<br>principalmente en el rango de 1 a 3 [m/s],<br>caracterizado a brisa muy débil.<br> <br>La velocidad promedio del viento correspondió<br>a 3,00 [m/s].<br> <br>La frecuencia de vientos calmos fue de 3,78%.|

ANÁLISIS METEOROLÓGICO www.ecometrika.com

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Primavera Nocturno||||12,68<br>22,79<br>33,39<br>14,77<br>9,15<br>5,14<br>1,61<br>0,48<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Los<br>campos<br>de<br>vientos<br>provinieron<br>principalmente<br>desde<br>las<br>siguientes<br>direcciones: SSO (13%), N (12%), S (11%) y<br>NNO<br>(11%).La<br>magnitud<br>del<br>viento<br>correspondió mayormente al intervalo de 0,5 a<br>2 [m/s], característico de brisas muy débiles.<br> <br>La velocidad media del viento fue de 1,68<br>[m/s].<br> <br>La frecuencia de vientos calmos correspondió a<br>12,68%.|
|Primavera AM||||2,67<br>5,90<br>12,36<br>20,08<br>21,91<br>18,54<br>12,22<br>4,49<br>1,26<br>0,56<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Las masas de aire se exhibieron mayormente<br>desde dirección SSO (26%) y S (21%). La<br>velocidad del viento se concentró en el intervalo<br>de 2 a 6 [m/s] con carácter de brisas muy<br>débiles a moderadas.<br> <br>La velocidad del viento fue igual a 3,42 [m/s].<br> <br>Los vientos en calma alcanzaron una frecuencia<br>de 2,67%.|
|Primavera PM||||4,99<br>8,61<br>17,23<br>14,86<br>17,48<br>18,73<br>13,36<br>2,87<br>1,25<br>0,62<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calm...<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>El viento provino con mayor frecuencia desde<br>dirección SO (29%) y SSO (23%). LA magnitud<br>del viento osciló principalmente en el intervalo<br>de 1 a 6 [m/s] con características de brisas muy<br>débiles a moderadas.<br> <br>El promedio de velocidad fue de 3,20 [m/s].<br> <br>La frecuencia de vientos en calma, correspondió<br>a 4,99%.|

ANÁLISIS METEOROLÓGICO www.ecometrika.com

www.ecometrika.com

|Ciclo|Descripción|Col3|
|---|---|---|
|Estacional|Verano<br>Otoño<br>Invierno<br>Primavera|1 de enero<br>10 de abril<br>18 de julio<br>10 de noviembre|
|Horario|Nocturno<br>AM<br>PM|00:00 a 06:59<br>07:00 a 14:59<br>15:00 a 23:59|

www.ecometrika.com

www.ecometrika.com

www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|722.807|5.728.556|18S|WGS 84|

|Porcentaje de datos válidos [%]|Col2|Col3|Col4|
|---|---|---|---|
|Mes|Velocidad del<br>viento|Dirección del<br>viento|Temperatura|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%|100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%|100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%<br>100%|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|724.627|5.714.118|18 Sur|WGS 84|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Porcentaje de datos válidos [%]|Col2|Col3|Col4|
|---|---|---|---|
|Mes|Velocidad del<br>viento|Dirección del<br>viento|Temperatura|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|86,6%<br>96,6%<br>94,9%<br>87,4%<br>94,8%<br>89,4%<br>87,9%<br>88,4%<br>91,0%<br>89,4%<br>88,1%<br>92,9%|91,8%<br>99,6%<br>99,7%<br>99,6%<br>99,7%<br>99,4%<br>99,7%<br>100,0%<br>99,9%<br>99,7%<br>99,6%<br>99,7%|99,7%<br>99,0%<br>99,9%<br>100,0%<br>100,0%<br>99,6%<br>100,0%<br>100,0%<br>99,9%<br>99,9%<br>99,6%<br>99,2%|

|Parámetro meteorológico<br>evaluado|% datos válidos|Cumple con<br>recomendación SEA<br>(>75%)|
|---|---|---|
|Velocidad del viento [m/s]<br>Dirección del viento [°]<br>Temperatura [°C]|90,57%<br>8<br>2 %<br>99,03%<br>99,73%|<br><br>|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Hora|Promedio velocidad del<br>viento [m/s]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|2,49<br>2,36<br>2,33<br>2,34<br>2,22<br>2,25<br>2,29<br>2,40<br>2,59<br>2,96<br>3,42<br>3,75<br>4,02<br>4,27<br>4,33<br>4,35<br>4,22<br>3,92<br>3,47<br>3,19<br>2,94<br>2,68<br>2,57<br>2,54|0,57<br>0,56<br>0,47<br>0,52<br>0,39<br>0,39<br>0,30<br>0,33<br>0,42<br>0,44<br>0,73<br>0,97<br>1,06<br>1,17<br>1,29<br>1,23<br>1,02<br>1,11<br>1,19<br>0,98<br>0,83<br>0,88<br>0,62<br>0,69|6,66<br>6,25<br>6,19<br>6,37<br>5,75<br>6,34<br>6,54<br>6,99<br>7,08<br>6,92<br>7,47<br>7,18<br>7,76<br>7,51<br>7,35<br>7,07<br>6,92<br>6,63<br>6,32<br>6,19<br>6,32<br>6,54<br>6,22<br>6,60|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Hora|Promedio velocidad del<br>viento [m/s]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|1,30<br>1,28<br>1,32<br>1,27<br>1,21<br>1,25<br>1,28<br>1,35<br>1,66<br>2,03<br>2,33<br>2,57<br>2,72<br>2,88<br>2,87<br>2,88<br>2,84<br>2,69<br>2,35<br>2,02<br>1,74<br>1,50<br>1,37<br>1,30|0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,11<br>0,13<br>0,33<br>0,69<br>0,81<br>0,81<br>0,69<br>0,81<br>0,61<br>0,19<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00|4,43<br>4,31<br>4,68<br>4,71<br>4,33<br>4,69<br>4,83<br>4,60<br>5,31<br>5,56<br>5,37<br>5,50<br>5,63<br>5,50<br>5,11<br>5,33<br>5,17<br>4,89<br>4,76<br>4,42<br>4,11<br>3,98<br>4,19<br>4,41|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Col1|Dirección del viento [grados]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hora<br>del día|0-20|20-40|40-60|60-80|80-100|100-120|120-140|140-160|160-180|180-200|200-220|220-240|240-260|260-280|280-300|300-320|320-340|340-360|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|57<br>53<br>56<br>57<br>58<br>72<br>65<br>61<br>52<br>70<br>52<br>57<br>45<br>30<br>31<br>26<br>33<br>29<br>29<br>34<br>34<br>36<br>39<br>51|34<br>31<br>33<br>34<br>51<br>37<br>40<br>36<br>13<br>19<br>13<br>6 <br>8 <br>8 <br>8 <br>9 <br>13<br>14<br>15<br>20<br>22<br>31<br>28<br>39|31<br>22<br>24<br>29<br>24<br>26<br>30<br>23<br>3 <br>7 <br>3 <br>2 <br>2 <br>0 <br>3 <br>3 <br>1 <br>5 <br>6 <br>18<br>21<br>19<br>27<br>31|23<br>17<br>14<br>13<br>18<br>24<br>16<br>16<br>1 <br>2 <br>1 <br>3 <br>2 <br>2 <br>1 <br>1 <br>3 <br>4 <br>4 <br>13<br>12<br>12<br>18<br>11|13<br>19<br>18<br>25<br>18<br>12<br>16<br>8 <br>0 <br>0 <br>0 <br>0 <br>2 <br>0 <br>1 <br>3 <br>1 <br>2 <br>7 <br>4 <br>9 <br>15<br>16<br>16|6 <br>12<br>22<br>19<br>19<br>14<br>10<br>10<br>0 <br>2 <br>0 <br>1 <br>1 <br>2 <br>1 <br>2 <br>2 <br>3 <br>4 <br>5 <br>11<br>18<br>12<br>11|6 <br>14<br>11<br>14<br>10<br>7 <br>9 <br>6 <br>3 <br>4 <br>3 <br>3 <br>1 <br>2 <br>0 <br>0 <br>0 <br>1 <br>2 <br>5 <br>1 <br>8 <br>13<br>6|11<br>10<br>13<br>12<br>16<br>12<br>8 <br>8 <br>3 <br>3 <br>3 <br>1 <br>3 <br>0 <br>1 <br>1 <br>3 <br>4 <br>5 <br>6 <br>12<br>7 <br>5 <br>12|8 <br>17<br>14<br>8 <br>12<br>6 <br>14<br>9 <br>6 <br>7 <br>6 <br>3 <br>5 <br>4 <br>4 <br>1 <br>3 <br>6 <br>9 <br>6 <br>12<br>11<br>8 <br>6|17<br>16<br>21<br>18<br>18<br>14<br>14<br>14<br>20<br>25<br>20<br>24<br>18<br>25<br>24<br>22<br>14<br>19<br>16<br>13<br>14<br>20<br>23<br>20|39<br>27<br>24<br>20<br>18<br>17<br>16<br>39<br>69<br>62<br>69<br>74<br>73<br>73<br>77<br>79<br>50<br>35<br>33<br>33<br>34<br>38<br>43<br>37|51<br>50<br>32<br>38<br>28<br>33<br>32<br>37<br>71<br>63<br>71<br>57<br>73<br>64<br>72<br>78<br>96<br>116<br>102<br>99<br>100<br>80<br>62<br>58|11<br>11<br>18<br>11<br>13<br>12<br>18<br>14<br>25<br>18<br>25<br>29<br>31<br>51<br>55<br>57<br>77<br>65<br>77<br>64<br>37<br>21<br>18<br>16|6 <br>7 <br>6 <br>3 <br>6 <br>9 <br>8 <br>2 <br>9 <br>8 <br>9 <br>20<br>14<br>16<br>9 <br>7 <br>7 <br>10<br>8 <br>5 <br>6 <br>8 <br>3 <br>6|6 <br>6 <br>2 <br>4 <br>8 <br>11<br>7 <br>8 <br>6 <br>9 <br>6 <br>6 <br>14<br>14<br>12<br>10<br>15<br>10<br>6 <br>5 <br>1 <br>6 <br>2 <br>5|12<br>11<br>5 <br>13<br>4 <br>9 <br>7 <br>11<br>15<br>6 <br>15<br>19<br>12<br>14<br>15<br>16<br>16<br>9 <br>9 <br>7 <br>7 <br>9 <br>4 <br>4|14<br>16<br>21<br>9 <br>9 <br>11<br>14<br>13<br>18<br>16<br>18<br>23<br>28<br>22<br>25<br>15<br>20<br>15<br>10<br>11<br>12<br>9 <br>18<br>9|20<br>26<br>31<br>38<br>35<br>39<br>41<br>50<br>51<br>44<br>51<br>37<br>33<br>38<br>26<br>35<br>11<br>18<br>23<br>17<br>20<br>17<br>26<br>27|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Col1|Dirección del viento [grados]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hora<br>Del día|0-20|20-40|40-60|60-80|80-100|100-120|120-140|140-160|160-180|180-200|200-220|220-240|240-260|260-280|280-300|300-320|320-340|340-360|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|42<br>33<br>32<br>37<br>40<br>45<br>38<br>43<br>39<br>50<br>39<br>28<br>25<br>34<br>24<br>18<br>26<br>35<br>27<br>28<br>28<br>30<br>28<br>33|15<br>18<br>20<br>13<br>24<br>17<br>23<br>27<br>19<br>12<br>19<br>19<br>8 <br>7 <br>6 <br>10<br>12<br>7 <br>9 <br>16<br>16<br>20<br>26<br>16|19<br>16<br>16<br>23<br>19<br>30<br>21<br>19<br>7 <br>13<br>7 <br>1 <br>1 <br>2 <br>1 <br>5 <br>4 <br>9 <br>13<br>8 <br>10<br>9 <br>15<br>19|26<br>31<br>45<br>47<br>47<br>32<br>46<br>32<br>2 <br>13<br>2 <br>4 <br>1 <br>1 <br>2 <br>1 <br>1 <br>4 <br>9 <br>14<br>22<br>21<br>20<br>30|26<br>34<br>35<br>32<br>34<br>39<br>34<br>21<br>1 <br>8 <br>1 <br>3 <br>1 <br>0 <br>2 <br>0 <br>3 <br>0 <br>2 <br>11<br>12<br>20<br>22<br>29|23<br>22<br>23<br>26<br>20<br>24<br>25<br>22<br>2 <br>5 <br>2 <br>2 <br>0 <br>0 <br>1 <br>1 <br>2 <br>1 <br>1 <br>4 <br>7 <br>8 <br>14<br>15|15<br>21<br>16<br>21<br>18<br>24<br>16<br>18<br>4 <br>2 <br>4 <br>5 <br>0 <br>1 <br>0 <br>4 <br>2 <br>1 <br>10<br>8 <br>7 <br>9 <br>10<br>10|22<br>16<br>21<br>15<br>15<br>14<br>9 <br>17<br>11<br>14<br>11<br>7 <br>9 <br>4 <br>3 <br>3 <br>5 <br>6 <br>4 <br>7 <br>4 <br>10<br>15<br>13|28<br>26<br>29<br>24<br>21<br>20<br>19<br>17<br>33<br>34<br>33<br>23<br>19<br>26<br>19<br>14<br>17<br>20<br>20<br>10<br>16<br>15<br>26<br>33|48<br>45<br>30<br>23<br>42<br>32<br>27<br>26<br>47<br>50<br>47<br>50<br>55<br>55<br>47<br>64<br>52<br>52<br>37<br>42<br>39<br>57<br>55<br>55|31<br>23<br>26<br>25<br>18<br>18<br>24<br>21<br>49<br>33<br>49<br>47<br>61<br>61<br>83<br>67<br>60<br>64<br>83<br>78<br>79<br>70<br>57<br>42|17<br>15<br>18<br>22<br>10<br>13<br>15<br>24<br>28<br>19<br>28<br>34<br>35<br>32<br>44<br>47<br>70<br>69<br>63<br>72<br>63<br>43<br>24<br>19|4 <br>10<br>5 <br>4 <br>8 <br>10<br>8 <br>11<br>13<br>11<br>13<br>21<br>16<br>26<br>19<br>27<br>26<br>32<br>27<br>18<br>13<br>7 <br>5 <br>6|1 <br>1 <br>3 <br>3 <br>5 <br>4 <br>4 <br>8 <br>11<br>9 <br>11<br>5 <br>14<br>16<br>16<br>18<br>13<br>9 <br>9 <br>7 <br>6 <br>1 <br>1 <br>2|3 <br>5 <br>5 <br>2 <br>7 <br>2 <br>2 <br>6 <br>5 <br>11<br>5 <br>18<br>11<br>17<br>14<br>12<br>10<br>9 <br>8 <br>5 <br>5 <br>6 <br>5 <br>5|4 <br>5 <br>3 <br>6 <br>7 <br>6 <br>10<br>6 <br>20<br>15<br>20<br>20<br>22<br>16<br>20<br>13<br>14<br>15<br>7 <br>10<br>7 <br>8 <br>6 <br>5|9 <br>14<br>12<br>14<br>7 <br>11<br>13<br>19<br>32<br>27<br>32<br>32<br>38<br>29<br>27<br>18<br>22<br>10<br>18<br>13<br>13<br>4 <br>8 <br>8|28<br>27<br>23<br>24<br>19<br>21<br>27<br>23<br>37<br>36<br>37<br>41<br>45<br>34<br>31<br>40<br>23<br>17<br>16<br>12<br>15<br>25<br>26<br>23|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Hora|Promedio de temperatura<br>[°C]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|8,86<br>8,59<br>8,38<br>8,15<br>7,96<br>7,88<br>8,12<br>9,00<br>10,51<br>12,31<br>14,00<br>15,32<br>16,28<br>16,98<br>17,16<br>16,92<br>16,14<br>14,78<br>13,22<br>11,56<br>10,65<br>9,97<br>9,49<br>9,14|3,67<br>3,47<br>3,14<br>2,74<br>2,71<br>2,63<br>2,37<br>3,28<br>3,86<br>5,44<br>6,93<br>8,30<br>9,00<br>9,18<br>9,34<br>9,30<br>8,89<br>7,77<br>6,70<br>6,20<br>5,52<br>4,96<br>4,69<br>4,12|14,17<br>13,96<br>13,55<br>13,14<br>13,06<br>12,83<br>13,19<br>14,47<br>16,93<br>18,77<br>21,32<br>23,46<br>24,98<br>25,60<br>26,23<br>25,50<br>24,31<br>22,91<br>20,42<br>17,83<br>16,13<br>15,16<br>14,56<br>14,18|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Hora|Promedio de temperatura<br>[°C]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|8,29<br>7,86<br>7,47<br>7,15<br>6,90<br>6,70<br>6,68<br>7,30<br>8,43<br>9,84<br>11,29<br>12,68<br>13,95<br>14,96<br>15,73<br>16,13<br>16,03<br>15,32<br>14,02<br>12,44<br>11,01<br>10,05<br>9,30<br>8,74|2,42<br>1,60<br>0,90<br>0,42<br>0,20<br>-0,30<br>-0,18<br>-0,43<br>0,70<br>2,02<br>3,44<br>4,90<br>6,62<br>7,62<br>8,30<br>8,52<br>8,12<br>7,62<br>6,70<br>5,90<br>5,00<br>4,12<br>3,70<br>2,86|13,37<br>13,08<br>12,60<br>12,36<br>12,18<br>12,08<br>12,08<br>12,63<br>14,13<br>16,09<br>18,50<br>20,77<br>22,62<br>23,96<br>25,30<br>25,97<br>25,86<br>24,36<br>22,66<br>20,48<br>17,60<br>15,80<br>14,66<br>13,88|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Mes|Frecuencia de<br>vientos calmos|N°<br>días|%|
|---|---|---|---|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|20<br>19<br>22<br>30<br>23<br>29<br>34<br>38<br>30<br>32<br>24<br>27|744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744|3%<br>3%<br>3%<br>4%<br>3%<br>4%<br>5%<br>5%<br>4%<br>4%<br>3%<br>4%|

|Hora|Frecuencia de<br>vientos calmos|%|
|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|12<br>16<br>21<br>17<br>25<br>32<br>42<br>36<br>26<br>23<br>6 <br>6 <br>5 <br>1 <br>3 <br>4 <br>4 <br>1 <br>5 <br>6 <br>6 <br>6 <br>16<br>9|3%<br>4%<br>6%<br>5%<br>7%<br>9%<br>12%<br>10%<br>7%<br>6%<br>2%<br>2%<br>1%<br>0%<br>1%<br>1%<br>1%<br>0%<br>1%<br>2%<br>2%<br>2%<br>4%<br>2%|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Mes|Frecuencia de<br>vientos calmos|N°<br>días|%|
|---|---|---|---|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|93<br>144<br>140<br>194<br>127<br>120<br>148<br>171<br>131<br>172<br>116<br>144|744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744|13%<br>21%<br>19%<br>27%<br>17%<br>17%<br>20%<br>23%<br>18%<br>23%<br>16%<br>19%|

|Hora|Frecuencia de<br>vientos calmos|%|
|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|125<br>129<br>133<br>134<br>139<br>119<br>122<br>106<br>78<br>42<br>19<br>9 <br>6 <br>6 <br>11<br>12<br>17<br>26<br>53<br>59<br>53<br>84<br>97<br>121|34%<br>35%<br>36%<br>37%<br>38%<br>33%<br>33%<br>29%<br>21%<br>12%<br>5%<br>2%<br>2%<br>2%<br>3%<br>3%<br>5%<br>7%<br>15%<br>16%<br>15%<br>23%<br>27%<br>33%|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Col1|Col2|Anual Nocturno|Anual AM|Anual PM|
|---|---|---|---|---|
|Pronóstico|||||
|Observado|||||

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Col1|Verano|Otoño|Invierno|Primavera|
|---|---|---|---|---|
|Pronóstico|||||
|Observado|||||

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

|Estadístico|Descripción|Fórmula|Resultado|Col5|
|---|---|---|---|---|
|Estadístico|Descripción|Fórmula|Velocidad del<br>viento [m/s]|Temperatura<br>[°C]|
|RMSE|Error medio cuadrático (Root<br>mean square Error), nos indica la<br>medida de las diferencias en<br>promedio<br>entre<br>valores<br>pronosticados y observados||1,83|2,50|
|NRMSD|Error<br>medio<br>cuadrático<br>normalizado<br>(Normalized<br>Root<br>mean square deviation) señala la<br>varianza residual entre los valores<br>pronosticados y observados||0,22|0,07|
|NMAE|Error medio absoluto normalizado<br>, toma en cuenta el peso del error<br>respecto al valor de la variable<br>medida,<br>normaliza el<br>error<br>absoluto||0,17|0,05|
|BIAS|Sesgo, proporciona información<br>sobre la tendencia del modelo a<br>sobrestimar o subestimar una<br>variable||1,26|0,95|
|Coeficiente de<br>correlación de<br>Pearson|Un índice que mide el grado de<br>relación de dos variables siempre<br>y <br>cuando<br>ambas<br>sean<br>cuantitativas.||0,76|0,91|

ANÁLISIS DE INCERTIDUMBRE www.ecometrika.com

ANÁLISIS DE RESULTADOS www.ecometrika.com

BIBLIOGRAFÍA www.ecometrika.com