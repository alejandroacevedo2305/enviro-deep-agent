---
title: Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague
author: Alvaro
date: D:20160509142403-03'00'
language: es
type: report
pages: 23
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modificación Proyecto Técnico Piscicultura El Peral
  - 1. Introducción
  - 2. Metodología de Modelación
  - Resultados 3.
  - 4. Conclusiones y Discusiones
-->

# Modificación Proyecto Técnico Piscicultura El Peral

### Titular: Salmones Antártica S.A.

Comuna de Los Ángeles - Región del Biobío

## Estudio de Modelación de la Dilución del Efluente y Usos de Estudio de Modelación de la Dilución del Efluente y Usos de Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero CholguagueAgua en el Cuerpo Receptor Estero CholguagueAgua en el Cuerpo Receptor Estero Cholguague

**Elaborado por:**

B I O G E A L I M I T A D A BIOGEA LIMITADA BIOGEA LIMITADA

Camilo Henríquez 301 Of. 304 - Villarrica

Fono (45) 2414 980

**[c o n t a c t o @ b i o g e a . c l](mailto:contacto@biogea.cl)**

Octubre de 2015

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

# 1. Introducción

El presente documento forma parte de los estudios que acompañan la Declaración de Impacto Ambiental
(DIA) del proyecto Modificación Proyecto Técnico Piscicultura El Peral, localizado en la Comuna de
Los Ángeles, Región del Biobío. El estudio corresponde a una modelación matemática de la dilución del
efluente del proyecto en el cuerpo receptor Estero Cholguague con el objeto de definir el área de
influencia del proyecto.

Un modelo matemático es una descripción, desde el punto de vista de las matemáticas, de un hecho o
fenómeno del mundo real. El objetivo del modelo matemático es entender ampliamente el fenómeno,
para así predecir su comportamiento en el futuro.

El comportamiento de un efluente en un cuerpo de agua es dinámico, los distintos elementos o
compuestos descargados están en permanente movimiento, ya sea por efecto del propio movimiento del
agua, o por la movilidad natural de las moléculas y partículas coloidales, aún en aguas quietas. Los
fenómenos de transporte que ocurren han sido ampliamente estudiados y han dado origen a numerosas
formulaciones matemáticas que describen su comportamiento. Hay dos conceptos que representan los
mecanismos básicos de transporte en el agua: flujo advectivo y flujo dispersivo.

El flujo advectivo se refiere al transporte de sustancias disueltas a partículas “con el agua”, es decir
mediante el arrastre que producen los desplazamientos netos del agua. El flujo dispersivo se refiere al
transporte de sustancias que ocurre independientemente de la existencia de un flujo de agua, por efecto
de la superposición de la difusión a nivel molecular y la dispersión turbulenta.

Un modelo se puede describir como una representación simplificada de la realidad en la cual sólo se
incluyen aquellos aspectos que tienen relevancia para el problema que queremos estudiar. En los modelos
matemáticos las relaciones entre las diferentes variables se reemplazan por expresiones matemáticas
simplificadas que representan el comportamiento del sistema real.

Los modelos de calidad de aguas son una herramienta adecuada para predecir la alteración de la calidad
del agua de un cuerpo hídrico causada por las actividades humanas, teniendo por finalidad determinar
las nuevas concentraciones de contaminantes del cuerpo de agua en cada punto y a lo largo del lapso de
interés cuando las condiciones de modificación y el estado primitivo son conocidos [1] . Un modelo de
calidad de aguas es confiable cuando cumple, con la condición básica de reproducir las condiciones
actuales. El núcleo de cualquier modelo de la calidad del agua son los balances de materia. La
concentración de cualquier sustancia en un punto cualquiera de un sistema natural ha de cumplir la
ecuación fundamental de conservación de la materia. Así, la ecuación diferencial que representa la
variación de concentración de un contaminante al cabo de un tiempo, que se encuentra disuelto en un

elemento diferencial de volumen, es:



∂C

∂x [) +]



∂

∂y [(E] [y]



∂C

∂y [) +]



∂

∂z [(E] [z]



∂C

∂z [) + S] [L] [+ S] [B] [+ S] [K] [ (] **[Ec. 1]** [) ]



∂C

∂t [= −]



∂

∂x [(U] [x] [C) −]



∂

∂y [(U] [y] [C) −]



∂

∂z [(U] [z] [C) +]



∂

∂x [(E] [x]



**1** **Vargas, J ( 1993)** . “Calidad del Agua en espacios Naturales” Impacto y Modelación. Departamento Ingeniería Civil,
Universidad de Concepción.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Donde **C C C** es la concentración del componente en el agua (mg/l o g/m [3] ), **ttt** es el tiempo (día), **U** **xUxUx**, **U** **yUyUy**, **U** **zUzUz**
son las velocidades advectivas longitudinales, laterales y verticales (m/d), **E** **xExEx**, **E** **yEyEy**, **E** **zEzEz** son los coeficientes
de difusión longitudinal, laterales y verticales (m [2] /d), **S** **LSLSL** es la tasa de carga directa y difusa (g/m [3] *d), **S** **BSBSB**
es la tasa de carga en la condición de borde (g/m [3] *d) y **S** **KSKSK** es la tasa de transformación cinética, positiva
si es fuente, negativa si es sumidero (g/m [3] *d).

La resolución de esta ecuación en tres dimensiones es muy compleja, por lo que, en la práctica se realizan
simplificaciones con el fin de reducir el número de dimensiones del problema. Dichas simplificaciones
se realizan en base a un correcto conocimiento de la hidrodinámica del sistema fluvial que permitirá
describir el volumen de agua hasta en tres dimensiones. Por ello, la cantidad de modelos de calidad de
las aguas es bastante considerable.

#### 1.1. Objetivos y Alcances

El objetivo del estudio de modelación es simular la dilución del efluente de Piscicultura El Peral en el
cuerpo receptor (Estero Cholguague) y determinar la concentración respeto de la distancias aguas abajo
de la descarga de los principales parámetros asociados a la actividad acuícola (Sólidos Suspendidos
Totales, Demanda Bioquímica de Oxígeno, Fósforo, Nitrógeno Total, Cloruros y Aceites y Grasas), y
evaluar los resultados conforme a los usos de aguas para los cuales se establecen criterios de calidad en

la NCh 1333.Of78 Modificada en 1987.

El modelo utilizado en el presente estudio ha sido aplicado en varios proyectos de pisciculturas evaluados
en el SEIA (Sistema de Evaluación de Impacto Ambiental) [2], con características similares tanto en los
procesos productivos como en los sistemas de tratamiento de efluentes y descarga a cuerpos de agua

fluviales.

**2** Proyecto referidos, entre otros, los siguientes:

 Modificación y Ampliación Proyecto Piscicultura Pangueco, Comuna de Melipeuco, Región de La Araucanía;

 Piscicultura Río Toltén, Comuna de Freire, Región de La Araucanía;

 Piscicultura Pitrufquén, Comuna de Pitrufquén, Región de La Araucanía;

 Aumento de Producción Piscicultura Caburgua II, Comuna de Pucón, Región de La Araucanía;

 Regularización y Ampliación Piscicultura Cherquenco, Comuna de Vilcún, Región de La Araucanía;

 Modificación y Ampliación Piscicultura Catripulli, Comuna de Curarrehue, Región de La Araucanía;

 Piscicultura Carileufu, Comuna de Pucón, Región de La Araucanía;

 Regularización y Ampliación Piscicultura Quetroleufu, Comuna de Pucón, Región de La Araucanía;

 Piscicultura El Manzano, Comuna de Melipeuco, Región de La Araucanía;

 Modificación Proyecto Técnico Piscicultura El Canelo, Comuna de Melipeuco, Región de La Araucanía.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

# 2. Metodología de Modelación

#### 2.1. Modelo Matemático

Para el caso de la modelación de cuerpos hídricos, el modelo más simple está dado por un modelo tipo
flujo pistón en estado estacionario, que considera los fenómenos de transporte de advección en el cuerpo
hídrico al cual se le asocia un término generalizado de mecanismos de eliminación de un componente
específico. El modelo matemático según Trapp & Matthies (1998) [3] está dado como sigue:



C x = C 0 ∗e



(− ~~k~~ μ [x] ~~[)]~~ **(Ec. 2)**



Dónde **C** **xCxCx** es la concentración del producto químico o componente orgánico a una distancia x aguas abajo
de la descarga (mg/L), **C** **0C0C0** es la concentración del componente en el punto de mezcla del RIL y el cuerpo
hídrico (x = 0) en mg/L, **kkk** es la constante cinética global de primer orden que representa los mecanismos
de eliminación que afecta al componente específico (día [-1] ), **xxx** es la distancia a lo largo del cuerpo hídrico,
que tiene su inicio (x = 0) en el punto de mezcla del Ril y el caudal del río (m), y **μμμ** es la velocidad lineal
promedio del cuerpo hídrico (m/s).

Este es un modelo ideal tipo flujo pistón, con perturbación de entrada tipo escalón, en estado estacionario,
esto implica que todas las variables de entradas permanecen constantes. Del balance de masa en el punto
de descarga se obtiene:

Q 0 ∗C 0 = (Q r ∗C r ) + (Q E ∗C E **)** **(Ec. 3)**

Q 0 = Q r + Q E **(Ec. 4)**

Dónde **Q** **0Q0Q0** es el caudal en el punto de mezcla (L/s), **Q** **rQrQr** es el caudal del río (L/s), **C** **rCrCr** es la concentración
del componente aguas arriba de la descarga (mg/L), **Q** **EQEQE** es el caudal del efluente (L/s) y **C** **ECECE** es la
concentración del componente en el efluente (mg/L).

#### 2.2. Parámetros estudiados

Los indicadores ambientales estudiados corresponden a los principales parámetros fisicoquímicos
controlados en la descarga de efluentes de la piscicultura, y de los cuales se tienen registros históricos.
Los parámetros estudiados son: Sólidos Suspendidos Totales (SST), Demanda Bioquímica de Oxígeno
(DBO), Fósforo (P), Nitrógeno Total (NT), Cloruros (Cl), y Aceites y Grasas (AyG).

Los estándares de calidad corresponden a normativas legales que limitan la concentración de diversos
constituyentes en el agua. En primer lugar se tiene el D.S. N° 90/2001, que establece “Norma de emisión
para la regulación de contaminantes asociados a las descargas de residuos líquidos a aguas marinas y
continentales superficiales”. No obstante, los principales estándares corresponden a la NCh409/1.0f84

**3** **Trapp, S., Matthies, M. (1998)** . “Chemodynamics and Environmental Modeling. An Introduction” Springer Verlag,
Berlin, Alemania.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

que establece requisitos de calidad del agua potable para consumo humano, y la NCh1333/Of78
modificada en 1987, que establece los requisitos de calidad del agua para diferentes usos (tales como
agua para consumo humano, agua para la bebida de animales, para riego, para recreación y estética y
para vida acuática).

El estudio de modelación utiliza información del SACEI (Sistema de Autocontrol de Establecimientos

Industriales), correspondiente a los registros históricos de los indicadores ambientales señalados
anteriormente (SST, DBO, PT, NTK, Cl, AyG) medidos en la descarga de efluentes de la Piscicultura
El Peral. El estudio también considerará los resultados del Balance de Masas del proyecto.

#### 2.3. Área de Estudio y Usos de Agua del Cuerpo Receptor

El área de estudio se ubica en el sector El Peral, aproximadamente 14 km al oriente de la ciudad de Los
Ángeles. En el escenario productivo proyectado solo se considera una descarga de efluentes tratados al
cuerpo receptor Estero Cholguagüe, en el punto de coordenadas UTM (m) Este 748.817 y Norte
5.847.648, Datum WGS 84 H18.

La Piscicultura El Peral, para el cultivo de salmónidos extrae aguas desde el Estero Cholguagüe (inserto
en la cuenca del Río Biobío, en la subcuenca del Río Duqueco) conforme a los derechos de
aprovechamiento otorgados, en tanto que el agua para consumo humano se extrae de un pozo (agua
subterránea).

El área de emplazamiento de la Piscicultura El Peral corresponde a un sector rural, la zonificación urbana
más cercana corresponde a la localidad de El Peral (2,5 a 2,7 km del proyecto). El sector presenta
actividades antrópicas predominantes, como la actividad forestal y agropecuaria, esta última hace uso de
los recursos hídricos de la cuenca (agricultura de riego) a través de los numerosos canales de riego

existentes.

El objetivo del estudio es determinar el área de influencia de la descarga de efluentes del proyecto sobre
la calidad del agua del cuerpo receptor, a partir del punto de descarga de la Piscicultura El Peral. Aguas
debajo de la piscicultura (2 km) no existen descargas industriales puntuales, no obstante, por el tipo de
uso de suelos del sector existen descargas difusas de actividades agropecuarias. Aproximadamente a 2,7
km aguas debajo de la piscicultura, el Estero Cholguagüe cruza el área urbana El Peral (según
zonificación del Plan Regulador Comunal).

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Figura 1. Sector de emplazamiento de la Piscicultura El Peral.

2.3.1. Estimación de caudales

El proyecto “Modificación Proyecto Técnico Piscicultura El Peral” cuenta con derechos de
aprovechamiento no consuntivos de aguas superficiales del Estero Cholguagüe, otorgados mediante
Resolución D.G.A. N° 21 de fecha 16 de enero de 1995, por un caudal de 650 L/s de ejercicio permanente

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

y continuo, y por un caudal de 250 L/s de ejercicio eventual y continuo. Los derechos de
aprovechamiento son restituidos 696 m aguas abajo de la captación, en el mismo Estero Cholguagüe.

El Estero Cholguagüe es tributario izquierdo del Río Duqueco (14 km aguas abajo de la descarga de
efluentes de la Piscicultura El Peral).

De acuerdo a los Expedientes DGA [4] asociados a los derechos de aprovechamiento de agua otorgados en
el Estero Cholguagüe, la caracterización de este cauce (E. Cholguagüe) indica que drena una pequeña
cuenca y recibe aportes subterráneos, recuperaciones y afluentes de vertientes. El suelo en el sector es
altamente poroso, constituido principalmente de arenas, lo cual facilita las pérdidas por infiltración de
los canales del sector, las que rápidamente forman parte de las cauces cercanos en forma de
recuperaciones, por lo que se pude decir que el Estero Cholguagüe es un cauce de recuperaciones.

El Informe Técnico del derecho de aprovechamiento de agua, Expediente ND-0802-67, disponible en la
página web de la Dirección General de Aguas [5], señala que en época de primavera-verano las aguas del
Estero Cholguagüe reciben derrames y drenajes de las áreas bajo riego en el sector. En el mismo
Expediente ND-0802-67, señala que el caudal ecológico entre los meses de abril y octubre, ambos
inclusive, es innecesario fijarlo por cuanto, por un lado, los derechos existentes aguas arriba del punto
de captación son ejercitados solo en los meses de riego, y por otro, en dichos meses ese caudal es más
que suficiente para considerarlo como caudal ecológico; también señala que de lo observado en terreno
en la época de estiaje (en los meses de noviembre a marzo), este caudal se compensa con las
recuperaciones las cuales son suficientes para preservar el equilibrio ecológico, además se comprobó con

aforos realizados.

Actualmente la Piscicultura El Peral tiene aproado por Resolución SISS N° 2068/2006, que aprueba el
Programa de Monitoreo de la Calidad del Efluente, un caudal de descarga máximo de 650 L/s. El presente
proyecto, “Modificación del Proyecto Técnico Piscicultura El Peral”, contempla aumentar el caudal de
descarga a un máximo de 900 L/s.

2.3.2. Usos de Agua del Estero Cholguague (aguas abajo de la descarga del proyecto)

Los usos de agua del cuerpo receptor (Estero Cholguagüe) fueron catastrados a través de la inspección
en terreno, a través de la consulta al Catastro Público de Aguas y a través de la revisión de los Expedientes
asociados a los derechos de aprovechamientos de aguas más cercanos al sitio del proyecto.

En la tabla 1 se resumen los puntos de captación de los derechos de aprovechamiento de agua
formalmente otorgados sobre el Estero Cholguagüe, según el Expediente CPA (Catastro Público de
Aguas), se ha medido la distancia con respecto al punto de restitución de la Piscicultura El Peral, tanto
aguas arriba como aguas abajo de este punto.

4 [Expediente ND-0802-934: http://sigedo.mop.gov.cl/Central/DireccionGeneral/RegistroUnico/ND-0802-934.PDF](http://sigedo.mop.gov.cl/Central/DireccionGeneral/RegistroUnico/ND-0802-934.PDF)

5 [http://sigedo.mop.gov.cl/Central/DireccionGeneral/RegistroUnico/ND-0802-67.PDF](http://sigedo.mop.gov.cl/Central/DireccionGeneral/RegistroUnico/ND-0802-67.PDF)

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Tabla 1. Expediente CPA derechos de aprovechamiento de agua otorgados Estero Cholguagüe.

|Expediente|N° Res.<br>DGA|Nombre peticionario|Caudal<br>(L/s)|Tipo|Coordenadas UTM captaciones|Col7|Col8|Distancia respecto<br>de la descarga<br>piscicultura|
|---|---|---|---|---|---|---|---|---|
|Expediente|N° Res.<br>DGA|Nombre peticionario|Caudal<br>(L/s)|Tipo|Este|Norte|Datum|Datum|
|ND-0802-67|302/1995|Javier Curilemu Soto|900|NC|749.463|5.847.853|WGS 84|Bocatoma Proyecto|
|ND-0802-363|258/2006|Javier Curilemu Soto|600|NC|752.000|5.849.650|PSAD56|3,4 km aguas arriba|
|ND-0802-934|256/2010|Arnoldo Videla M.|30|NC|752.050|5.849.665|PSAD56|3,5 km aguas arriba|
|ND-0802-1214|270/1989|Humberto Vallejos M.|56|C|746.858|5.847.370|WGS 84|2 km aguas abajo|

|Nombre peticionario|Caudal<br>(L/s)|Coordenadas UTM captaciones|Col4|Col5|Distancia respecto de la<br>descarga piscicultura|
|---|---|---|---|---|---|
|Nombre peticionario|Caudal<br>(L/s)|Este|Norte|Datum|Datum|
|Canal Municipal|195|749.915|5.848.144|WGS 84|1.260 m aguas arriba|
|Canal El Peral - Cholguagüe|-|748.477|5.847.528|WGS 84|320 m aguas abajo|
|Canal Santander|-|747.979|5.847.476|WGS 84|780 m aguas abajo|
|Canal El Hogar|-|747.260|5.847.495|WGS 84|1.600 m aguas abajo|











Conforme al Expediente CPA, aguas debajo de la descarga de la Piscicultura El Peral existe solo un
derecho de aprovechamiento de agua formalmente otorgado ubicado a una distancia de 2 km (distancia
no lineal, medida siguiendo el cauce del Estero), correspondiente al Canal Vallejo, cuyo uso de agua es
para riego.

Del trabajo en terreno y la revisión de la plataforma web del IDE (Infraestructura de Datos Geoespaciales,
[www.ide.cl,](http://www.ide.cl/) [www.geoportal.cl), se comprueba la existencia de otros canales de riegos derivados del](http://www.geoportal.cl/)
Estero Cholguagüe. Aguas arriba de la descarga de la piscicultura se encuentra el Canal Municipal.
Aguas debajo de la descarga de la piscicultura se encuentran el Canal Peral-Cholguagüe, Canal Santander
y el Canal El Hogar. En la tabla 2 y figura 2 se describe el emplazamiento de los canales de riego.

Tabla 2. Canales de riego derivados del Estero Cholguagüe.







El Expediente DGA ND-0802-67 [6], asociado al derecho de aprovechamiento de aguas de la Piscicultura
El Peral, señala que parte de los recursos del Estero Cholguagüe provienen del Río Laja. Los
antecedentes indican que este aporte es de 240 L/s, siendo captados 195 L/s por el Canal Municipal
(arriba de la piscicultura) y el remanente de 45 L/s se extrae aguas abajo de la restitución de la
Piscicultura El Peral, a través de los canales de riego.

Para efectos del presente estudio, se asumirá que los 45 L/s serán extraídos en el primer canal de riego
existente. También es posible asumir que estos 45 L/s conforman el caudal ecológico del Estero en el
tramo emplazado entre captación y restitución de la piscicultura.

Además, del uso para vida acuática, dados los usos de suelos, también se puede inferir que existe uso
para bebida animal en el tramo de estudio (hasta los 2 km aguas abajo de la descarga del proyecto).

6 [http://sigedo.mop.gov.cl/Central/DireccionGeneral/RegistroUnico/ND-0802-67.PDF, carilla 000041.](http://sigedo.mop.gov.cl/Central/DireccionGeneral/RegistroUnico/ND-0802-67.PDF)

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Figura 2. Emplazamiento de los derechos de aprovechamiento de agua y solicitudes en trámite.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

#### 2.4. Datos de entrada del Modelo

2.4.1. Caudal operacional del Proyecto

Actualmente, el caudal máximo de descarga de la Piscicultura El Peral es de 650 L/s. Este es el caudal
utilizado para modelar la situación actual de la Piscicultura El Peral. El caudal de Estero Cholguague, en
el punto de descarga, para efectos del estudio, será igual a la suma del caudal ecológico más el remanente
del derecho de agua (45 L/s + 250 L/s).

El caudal de efluente para la condición futura, de acuerdo a lo descrito en la Declaración de Impacto

Ambiental, será de 900 L/s. Para modelar esta condición se utilizarán los resultados del Balance de Masas

( **Anexo 9** de la DIA).

2.4.2. Caudal mínimo del cuerpo receptor

De acuerdo a lo descrito en el numeral 2.3.2, se considera un caudal ecológico de 45 L/s.

2.4.3. Concentraciones de los parámetros de estudio

Para conocer la concentración de los parámetros se cuenta con el un análisis fisicoquímico de aguas de
una muestra tomada en el Estero Cholguagüe en el sector de bocatoma (ver Informe N° 260065-01 del
Laboratorio HIDROLAB).

Tabla 3. Concentración de los indicadores, previo a la descarga de la Piscicultura El Peral.

|Parámetro|Unidad|Valor|Fuente|
|---|---|---|---|
|Nitrógeno total Kjeldahl|mg/L|1,81|Informe de Ensayo N° 260065-01|
|Fósforo Total|mg/L|0,53|Informe de Ensayo N° 260065-01|
|Cloruro|mg/L|2,18|Informe de Ensayo N° 260065-01|
|Sólidos Suspendidos Totales|mg/L|< 5,00|Informe de Ensayo N° 260065-01|
|Demanda Bioquímica de Oxígeno|mg/L|3|Informe de Ensayo N° 260065-01|
|Aceites y Grasas|mg/L|< 5,00|Informe de Ensayo N° 260065-01|

Para modelar la situación actual de descarga de efluentes de la piscicultura, se utilizan los certificados
de autocontrol obtenidos del SACEI (Sistema de Autocontrol de Establecimientos Industriales)

conformes al Programa de Monitoreo de la Calidad del Efluente de Piscicultura El Peral, aprobado por
Resolución SISS N° 2068/2006 Exenta. La información del SACEI fue analizada estadísticamente para
obtener los valores requeridos para el modelo, correspondiente a las concentraciones en el efluente de
los indicadores Aceites y Grasas, DBO, Fósforo, Nitrógeno Total Kjeldahl y Sólidos Suspendidos
Totales, previo a la descarga al cuerpo receptor.

Para efectos del estudio, se utilizará el Percentil 95 (P 95 ) como el estadístico que representa la
[concentración del efluente. El percentil es una medida de tendencia central usada en estadística que](https://es.wikipedia.org/wiki/Estad%C3%ADstica)
indica, una vez ordenados los datos de menor a mayor, el valor de la variable por debajo del cual se
[encuentra un porcentaje dado de observaciones en un grupo de observaciones. De este modo, el P](https://es.wikipedia.org/wiki/Porcentaje) 95

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

muestra que el 95% de los datos en estudio tiene un valor inferior que el P 95, por tanto los valores
superiores al P 95 solo representan el 5% de los datos y posiblemente para el caso de los registros del
SACEI se asocian a situaciones de contingencia en el tratamiento del efluente de la piscicultura, para lo
cual el proyecto ha contemplado medidas preventivas.

Para efectos de cálculo, en los casos donde los resultados están bojo los límites de detección en los

informes de autocontrol, se utilizó el valor de corte o límite de detección indicado.

Tabla 4. Análisis estadístico de los informes de autocontroles de Pisc. El Peral (2006-2015).













|Estadístico|AyG<br>(mg/L)|DBO<br>5<br>(mgO /L)<br>2|Fósforo<br>(mg/L)|NTK<br>(mg/L)|SST<br>(mg/L)|
|---|---|---|---|---|---|
|Mínimo|0,5|1,00|0,10|0,05|1,00|
|Mediana|5,00|2,60|0.20|1,75|5,00|
|Promedio|4,86|3,32|0,57|2,47|6,52|
|Máximo|25,10|21,50|21,70|29,20|110,00|
|Percentil 95|10,00|8,00|1,38|6,23|13,10|

Para modelar la situación proyectada (aumento de caudal a 900 L/s, y un sistema de tratamiento de
efluentes consistente en un sistema de filtración), se utilizarán los resultados del Balance de Masas.

Tabla 5. Resultados del balance de masa del sistema de tratamiento de Riles.















|AyG<br>(mg/L)|Cloruro<br>(mg/L)|DBO<br>5<br>(mgO /L)<br>2|Fósforo<br>(mg/L)|NTK<br>(mg/L)|SST<br>(mg/L)|
|---|---|---|---|---|---|
|0,2035|77,16|6,3271|0,1680|2,7382|3,4005|

Para determinar la concentración de Cloruro, se realiza el siguiente balance de masas. Este balance de masa
se realiza para el escenario más desfavorable, desde el punto de vista de la carga ambiental, el cual considera
la aplicación de sal en forma escalonada a una concentración del 1%, bajando el nivel de agua a la mitad
durante la aplicación de las unidades de cultivo asociadas (estanques circulares), luego se aplica oxígeno. Para
suponer el escenario más desfavorable se considera la aplicación en los estanques de mayor volumen
(estanques de cultivo de 25m [3] ) dado que la descarga de estos estanques genera el mayor volumen de agua con
el producto en solución. Para el balance de masa se consideran las siguientes condiciones:

 El empleo de sal será en forma escalonada, considerándose un máximo de tres estanques a tratar en
forma simultánea. De requerirse el tratamiento en el resto de unidades de cultivo, está será una vez
evacuados los estanques del primer tratamiento.

 La concentración indicada para cada tratamiento se alcanza en la mitad del volumen máximo del

estanque.

 Cumplido el periodo de tratamiento, se completa la capacidad máxima útil del estanque con agua.

 - Luego se aplica una tasa de recambio de agua de 1,5h [-1] .

 El tratamiento con sal se aplica a un máximo de 3 estanques a la vez.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Tabla 6. Aplicación de Sal a estanques de mayor volumen.

|N°<br>Estanques|Capacidad<br>útil<br>individual|N°<br>Estanques<br>tratados<br>simultáneos|Nivel<br>medio de<br>agua|Tasa<br>recambio<br>agua|Dosificación<br>sal|Cantidad<br>de sal<br>usada|Concentración<br>sal en los<br>estanques|
|---|---|---|---|---|---|---|---|
|40|63,6 m3|3|12,5 m3|1,5h-1|1%|375 kg|10 g/L|



















En base a la tabla anterior, se determina una concentración de sal en los estanques de 10 g/L
(Cuc: 10.000 mg/L).

Para determinar la concentración de descarga de sal de las cuatro unidades de cultivo en tratamiento, se tiene:

 - Cuc: Concentración de sal de descarga de las unidades de cultivo en tratamiento de sal (mg/L).

 Quc: Caudal de descarga de las unidades de cultivo en tratamiento de sal (L/s).

 Cef: Concentración de sal del efluente final o descarga de la piscicultura al cuerpo receptor (mg/L).

 Qef: Caudal operacional total de la piscicultura (900 L/s).

Cefluente= [Cuc∗Quc]

Qef



1h
∗
1m [3] 3.600s []]



= 77,16 mg/L



[m]

1,5h [∗1.000L] 1m [3]



Cef=



10.000 [m][g]

[ L



[g] []][ ∗ ] [[][37,5] [m] [3]

L 1,5h



[900 [L] s []]



2.4.4. Constantes de decaimiento

Para la obtención de las constantes de decaimiento requeridas por el modelo, se utilizó la información
bibliográfica y la información aportada por otros estudios similares existente en el SEIA. La velocidad
del flujo de agua del Estero Cholguague se determinó mediante aforo directo en el sector descarga, y
corresponde a 0,8211 m/s.

Tabla 7. Constante cinéticas utilizadas en la simulación.

|Parámetros|Constante|Fuente|
|---|---|---|
|Cloruro|0,0032|SEIA7|
|Demanda Bioquímica de Oxígeno|0,1350|Metcalf (1998)|
|Fósforo Total|0,009|Quenzer (1998)|
|Nitrógeno|0,0220|Quenzer (1998)|
|Sólidos Suspendidos Totales|0,1450|Metcalf (1998)|
|Aceites y Grasas|0,1450|Metcalf (1998)|

7 Regularización Piscicultura Río Las Marcas, Región de Los Lagos, aprobada por RCA N° 101/2015 (Informe adjunto
en Anexo 7 de la Adenda 1).

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

# Resultados 3.

#### 3.1. Modelación de la dilución actual del efluente de Piscicultura El Peral

En la tabla 8 se detallan los datos de entrada del modelo, utilizados para estudiar la dilución del
efluente generado por Piscicultura El Peral en su condición actual.

Tabla 8. Datos de entrada para la modelación, condición actual.

|Parámetros|Unidad|AyG|DBO<br>5|PT|NT|SST|
|---|---|---|---|---|---|---|
|Qo|m3/s|0,695|0,695|0,695|0,695|0,695|
|QCanal|m3/s|0,045|0,045|0,045|0,045|0,045|
|Qr|m3/s|0,045|0,045|0,045|0,045|0,045|
|Qe|m3/s|0,650|0,650|0,650|0,650|0,650|
|Co|mg/L|9,68|7,68|1,33|5,94|12,58|
|Cr|mg/L|5,00|3,00|0,53|1,81|5,00|
|Ce (Perc95)|mg/L|10,00|8,00|1,38|6,23|13,10|
|μ|m/s|0,900|0,900|0,900|0,900|0,900|
|k|-|0,1450|0,1350|0,0010|0,0220|0,1450|

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Tabla 9. Resultados de la modelación, condición actual.

BIOGEA LIMITADA

|x (m)|AyG|DBO<br>5|Fósforo|NTK|SST|
|---|---|---|---|---|---|
|0|9,6763|7,6763|1,3250|5,9438|12,5755|
|1|8,2364|6,6070|1,3118|5,8003|10,7043|
|2|7,0108|5,6867|1,2987|5,6602|9,1114|
|3|5,9676|4,8946|1,2858|5,5235|7,7556|
|4|5,0796|4,2128|1,2730|5,3901|6,6016|
|5|4,3237|3,6260|1,2603|5,2600|5,6192|
|6|3,6804|3,1209|1,2478|5,1330|4,7831|
|7|3,1327|2,6862|1,2354|5,0090|4,0714|
|8|2,6666|2,3120|1,2231|4,8881|3,4655|
|9|2,2698|1,9900|1,2109|4,7700|2,9498|
|10|1,9320|1,7128|1,1989|4,6548|2,5109|
|20|0,3858|0,3822|1,0848|3,6454|0,5013|
|30|0,0770|0,0853|0,9816|2,8548|0,1001|
|40|0,0154|0,0190|0,8881|2,2357|0,0200|
|50|0,0031|0,0042|0,8036|1,7509|0,0040|
|60|0,0006|0,0009|0,7272|1,3712|0,0008|
|70|0,0001|0,0002|0,6580|1,0738|0,0002|
|80|0,0000|0,0000|0,5953|0,8410|0,0000|
|90|0,0000|0,0000|0,5387|0,6586|0,0000|
|100|0,0000|0,0000|0,4874|0,5158|0,0000|
|120|0,0000|0,0000|0,3991|0,3163|0,0000|
|130|0,0000|0,0000|0,3611|0,2477|0,0000|
|140|0,0000|0,0000|0,3267|0,1940|0,0000|
|150|0,0000|0,0000|0,2956|0,1519|0,0000|
|160|0,0000|0,0000|0,2675|0,1190|0,0000|
|170|0,0000|0,0000|0,2420|0,0932|0,0000|
|180|0,0000|0,0000|0,2190|0,0730|0,0000|
|190|0,0000|0,0000|0,1982|0,0571|0,0000|
|200|0,0000|0,0000|0,1793|0,0448|0,0000|
|220|0,0000|0,0000|0,1468|0,0274|0,0000|
|240|0,0000|0,0000|0,1202|0,0168|0,0000|
|260|0,0000|0,0000|0,0984|0,0103|0,0000|
|280|0,0000|0,0000|0,0806|0,0063|0,0000|
|300|0,0000|0,0000|0,0660|0,0039|0,0000|
|320|0,0000|0,0000|0,0540|0,0024|0,0000|
|321|0,0000|0,0000|0,0557|0,0024|0,0000|
|325|0,0000|0,0000|0,0535|0,0022|0,0000|
|330|0,0000|0,0000|0,0509|0,0020|0,0000|
|340|0,0000|0,0000|0,0461|0,0015|0,0000|

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

|350|0,0000|0,0000|0,0417|0,0012|0,0000|
|---|---|---|---|---|---|
|360|0,0000|0,0000|0,0377|0,0009|0,0000|
|370|0,0000|0,0000|0,0341|0,0007|0,0000|
|380|0,0000|0,0000|0,0309|0,0006|0,0000|
|400|0,0000|0,0000|0,0253|0,0004|0,0000|
|440|0,0000|0,0000|0,0169|0,0001|0,0000|
|480|0,0000|0,0000|0,0114|0,0000|0,0000|
|520|0,0000|0,0000|0,0076|0,0000|0,0000|
|560|0,0000|0,0000|0,0051|0,0000|0,0000|
|600|0,0000|0,0000|0,0034|0,0000|0,0000|
|650|0,0000|0,0000|0,0021|0,0000|0,0000|
|700|0,0000|0,0000|0,0013|0,0000|0,0000|
|750|0,0000|0,0000|0,0008|0,0000|0,0000|
|800|0,0000|0,0000|0,0005|0,0000|0,0000|
|850|0,0000|0,0000|0,0003|0,0000|0,0000|
|900|0,0000|0,0000|0,0002|0,0000|0,0000|
|1000|0,0000|0,0000|0,0001|0,0000|0,0000|

A continuación se muestran los resultados en forma gráfica.

Gráfico 1. Resultados de la modelación, condición actual.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

#### 3.2. Simulación de la dilución del efluente para el escenario proyectado “Modificación Proyecto Técnico Piscicultura El Peral”

Para simular el escenario proyectado, los resultados del Balance de Masa ( **Anexo 9** de la DIA) y el

balance de masa de Cloruros descrito en el numeral 2.4.3.

Tabla 10. Datos de entrada para la simulación de la situación proyectada de Piscicultura El Peral.

|Parámetros|Unidad|AyG|Cloruro|DBO<br>5|PT|NT|SST|
|---|---|---|---|---|---|---|---|
|Qo|m3/s|0,945|0,945|0,945|0,945|0,945|0,945|
|QCanal|m3/s|0,045|0,045|0,045|0,045|0,045|0,045|
|Qr|m3/s|0,045|0,045|0,045|0,045|0,045|0,045|
|Qe|m3/s|0,900|0,900|0,900|0,900|0,900|0,900|
|Co|mg/L|0,4316|73,5895|6,1687|0,1852|2,6940|3,4767|
|Cr|mg/L|5,00|2,18|3,00|0,53|1,81|5,00|
|Ce (Perc95)|mg/L|0,2032|77,1600|6,3271|0,1680|2,7382|3,4005|
|μ|m/s|0,900|0,900|0,900|0,900|0,900|0,900|
|k|-|0,1450|0,0032|0,1350|0,0010|0,0220|0,1450|

Tabla 11. Datos de entrada simulación de dilución del efluente de Piscicultura El Peral.

BIOGEA LIMITADA

|x (m)|AyG|Cloruro|DBO<br>5|Fósforo|NTK|SST|
|---|---|---|---|---|---|---|
|0|0,4316|73,5895|6,1687|0,1852|2,6940|3,4767|
|1|0,3674|73,3283|5,3094|0,1834|2,6289|2,9593|
|2|0,3127|73,0681|4,5699|0,1816|2,5655|2,5190|
|3|0,2662|72,8087|3,9333|0,1798|2,5035|2,1441|
|4|0,2266|72,5503|3,3854|0,1780|2,4431|1,8251|
|5|0,1929|72,2928|2,9139|0,1762|2,3841|1,5535|
|6|0,1642|72,0362|2,5080|0,1745|2,3265|1,3223|
|7|0,1397|71,7806|2,1586|0,1727|2,2703|1,1256|
|8|0,1189|71,5258|1,8580|0,1710|2,2155|0,9581|
|9|0,1012|71,2719|1,5992|0,1693|2,1620|0,8155|
|10|0,0862|71,0190|1,3764|0,1676|2,1098|0,6942|
|20|0,0172|68,5382|0,3071|0,1517|1,6523|0,1386|
|30|0,0034|66,1441|0,0685|0,1372|1,2939|0,0277|
|40|0,0007|63,8336|0,0153|0,1242|1,0133|0,0055|
|50|0,0001|61,6039|0,0034|0,1124|0,7936|0,0011|
|60|0,0000|59,4520|0,0008|0,1017|0,6215|0,0002|
|70|0,0000|57,3753|0,0002|0,0920|0,4867|0,0000|
|80|0,0000|55,3711|0,0000|0,0832|0,3812|0,0000|
|90|0,0000|53,4370|0,0000|0,0753|0,2985|0,0000|

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

BIOGEA LIMITADA

|100|0,0000|51,5704|0,0000|0,0681|0,2338|0,0000|
|---|---|---|---|---|---|---|
|110|0,0000|49,7690|0,0000|0,0617|0,1831|0,0000|
|120|0,0000|48,0305|0,0000|0,0558|0,1434|0,0000|
|130|0,0000|46,3527|0,0000|0,0505|0,1123|0,0000|
|140|0,0000|44,7336|0,0000|0,0457|0,0879|0,0000|
|150|0,0000|43,1710|0,0000|0,0413|0,0689|0,0000|
|160|0,0000|41,6630|0,0000|0,0374|0,0539|0,0000|
|170|0,0000|40,2077|0,0000|0,0338|0,0422|0,0000|
|180|0,0000|38,8032|0,0000|0,0306|0,0331|0,0000|
|190|0,0000|37,4478|0,0000|0,0277|0,0259|0,0000|
|200|0,0000|36,1397|0,0000|0,0251|0,0203|0,0000|
|220|0,0000|33,6590|0,0000|0,0205|0,0124|0,0000|
|240|0,0000|31,3486|0,0000|0,0168|0,0076|0,0000|
|260|0,0000|29,1968|0,0000|0,0138|0,0047|0,0000|
|280|0,0000|27,1927|0,0000|0,0113|0,0029|0,0000|
|300|0,0000|25,3261|0,0000|0,0092|0,0018|0,0000|
|320|0,0000|23,5877|0,0000|0,0076|0,0011|0,0000|
|321|0,0000|24,6444|0,0000|0,0068|0,0011|0,0000|
|325|0,0000|24,2963|0,0000|0,0065|0,0010|0,0000|
|330|0,0000|23,8682|0,0000|0,0062|0,0009|0,0000|
|340|0,0000|23,0345|0,0000|0,0056|0,0007|0,0000|
|350|0,0000|22,2299|0,0000|0,0051|0,0005|0,0000|
|360|0,0000|21,4534|0,0000|0,0046|0,0004|0,0000|
|370|0,0000|20,7040|0,0000|0,0042|0,0003|0,0000|
|380|0,0000|19,9808|0,0000|0,0038|0,0003|0,0000|
|390|0,0000|19,2828|0,0000|0,0034|0,0002|0,0000|
|400|0,0000|18,6093|0,0000|0,0031|0,0002|0,0000|
|440|0,0000|16,1422|0,0000|0,0021|0,0001|0,0000|
|480|0,0000|14,0022|0,0000|0,0014|0,0000|0,0000|
|520|0,0000|12,1459|0,0000|0,0009|0,0000|0,0000|
|560|0,0000|10,5357|0,0000|0,0006|0,0000|0,0000|
|600|0,0000|9,1390|0,0000|0,0004|0,0000|0,0000|
|650|0,0000|7,6505|0,0000|0,0003|0,0000|0,0000|
|700|0,0000|6,4044|0,0000|0,0002|0,0000|0,0000|
|750|0,0000|5,3613|0,0000|0,0001|0,0000|0,0000|
|800|0,0000|4,4881|0,0000|0,0001|0,0000|0,0000|
|850|0,0000|3,7571|0,0000|0,0000|0,0000|0,0000|
|900|0,0000|3,1452|0,0000|0,0000|0,0000|0,0000|
|1000|0,0000|2,2041|0,0000|0,0000|0,0000|0,0000|
|1004|0,0000|2,1730|0,0000|0,0000|0,0000|0,0000|

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

A continuación se muestran los resultados en forma gráfica.

Gráfico 2. Evolución dilución del parámetro AyG, DBO 5, P, NTK y SST.

Gráfico 3. Evolución dilución del parámetro Cloruro.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

# 4. Conclusiones y Discusiones

Actualmente la Piscicultura El Peral se encuentra en operación y cuenta con un Programa de Monitoreo
de la Calidad del Efluente que genera, aprobado por la Superintendencia de Servicios Sanitarios mediante
Res. Exenta N° 2860/2006. Los estándares definidos por el programa de monitoreo conforme al D.S. N°
90/2001, son los límites máximos siguientes: 50 mg/L para Aceites y Grasas, 300 mgO 2 /L para DBO 5,
75 mg/L para Nitrógeno Total, 15 mg/L Fósforo Total, y 300 mg/L para los Sólidos Suspendidos Totales.
El programa de monitoreo no define estándar para el cloruro, no obstante, se incluye este parámetro en

la modelación.

Otros estándares que pueden aplicarse al estudio para evaluar la calidad del agua son la NCh 409, NCh
1333, los estándares de la OMS (Organización Mundial de la Salud), la “Guía CONAMA para el
establecimiento de las Normas Secundarias de Calidad Ambiental para aguas continentales superficiales
y marinas”, entre otros antecedentes bibliográficos que definen condiciones óptimas de calidad del agua.

La NCh 409 que establece requisitos fisicoquímicos, radiactivos y bacteriológicos del agua potable para
consumo humano, define límites máximos de 250 mg/L para el Cloruro; para el pH define un rango de
6 a 8,5 en agua para consumo humano. Según antecedentes bibliográficos, el efluente generado en el
cultivo de peces no debiera presentar Coliformes fecales [8], por lo cual no se ha considerado este
parámetro. La NCh 1333 define un límite máximo de 200 mg/L para el Cloruro en el agua para uso en
riego; para aguas de uso recreacional con contacto directo, define un límite de 5 mg/L para Aceites
flotantes y Grasas, y de 10 mg/L para Aceites y Grasas emulsificadas; para el pH define un rango de 6,5
a 8,3 en aguas con uso recreacional con contacto directo, y de 6 a 9 para vida acuática. Las Directrices
de la OMS para la calidad del agua potable, establecidas en Génova (1993), son el punto de referencia
internacional para el establecimiento de estándares y seguridad del agua potable [9] . En ella se definen un
estándar de 250 mg/L para el Cloruro y 50 mg/L para el Nitrógeno Total.

El fósforo en el agua no se considera tóxico para los humanos y los animales, sin embargo, puede tener
efectos indirectos a través de la eutrofización de los cuerpos de agua superficiales, que implica el
crecimiento explosivo de algas y el posterior abatimiento de oxígeno debido a la descomposición de
éstas cuando mueren (Carpenter _et al._, 1998; UN-WWAP, 2006). Respecto de la DBO, se considera que
el agua con muy buena calidad presenta niveles de 1 a 2 mg/L, y aceptable con niveles de 3 a 5 mg/L;
presentando mala calidad con niveles de DBO por sobre los 5 mg/L.

La Guía CONAMA para el establecimiento de las normas secundarias de calidad ambiental para aguas
continentales superficiales y marinas (2004), define cuatro categorías de calidad de agua:

a) **Excepcional** : Indica un agua de mejor calidad que la Clase 1, que por su extraordinaria pureza

y escasez, forma parte única del patrimonio ambiental de la república. Esta calidad es adecuada
también para la conservación de las comunidades acuáticas y demás usos definidos cuyos
requerimientos de calidad sean inferiores a esta Clase.

8 Guía de Aplicación de Lodos de Piscicultura en suelos. 2009. Elaborado por ECOING LTDA., por encargo del Servicio
Agrícola y Ganadero.

9 [http://www.lenntech.es/estandares-calidad-agua-oms.htm](http://www.lenntech.es/estandares-calidad-agua-oms.htm)

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

b) **Clase 1** : Muy buena calidad. Indica un agua adecuada para la protección y conservación de las

comunidades acuáticas, el riego irrestricto y para los usos comprendidos en las Clases 2 y 3.

c) **Clase 2** : Buena calidad. Indica un agua adecuada para el desarrollo de la acuicultura, de la pesca

deportiva y recreativa, y para los usos comprendidos en la Clase 3.

d) **Clase 3** : Regular calidad. Indica un agua adecuada para bebida de animales y para el riego

restringido.

Las clases de calidad comprendidas entre la Clase Excepcional y la Clase 3, son aptas para la captación
de agua para potabilizarla, según el tratamiento que se utilice. La Guía define los valores máximos y
mínimos de concentraciones siguientes:

 Aceites y Grasas: < 4 mg/L para la clase de excepción, 5 mg/L para la clase 1 y 2, y 10 mg/L
para la clase 3.

 Cloruro: < 80 mg/L para la clase de excepción, 100 mg/L para la clase 1, 150 mg/L para la clase
2, y 200 mg/L para la clase 3.

 Demanda Bioquímica de Oxígeno: < 2 mg/L para la clase de excepción, 5 mg/L para la clase 1,
10 mg/L para la clase 2, y 20 mg/L para la clase 3.

 Sólidos Suspendidos Totales: < 24 mg/L para la clase de excepción, 30 mg/L para la clase 1, 50
mg/L para la clase 2, y 80 mg/L para la clase 3.

 pH: define un rango de 6,5 - 8,5 para todas las clases.

Es importante destacar que la modelación se realiza suponiendo que las dos corrientes (efluente y caudal
del río) experimentan mezclado completo y que se cumple el principio de conservación de la masa.

Los resultados de la modelación de la dilución del efluente generado por la Piscicultura El Peral, la cual
utilizó como datos de entrada, la información del SACEI de este centro (tabla 4 y 9, y gráfico 1), y la
simulación de la condición proyectada, utilizando los resultados del balance de masa del sistema de
tratamiento de efluentes (numeral 2.4.3, tablas 11 y gráficos 2 y 3), muestran que los indicadores
ambientales estudiados (AyG, Cl, DBO 5, PT, NT y SST ) cumplen con los estándares de calidad
definidos por el D.S. N° 90/2001, la Normas Chilenas 409, la NCh 1333, la OMS y en la Guía CONAMA
(2004), en los puntos donde se han identificados usos de agua identificados en las tablas 1 y 2 y figuras
2 y 3.

No obstante, el principal estándar para determinar el área de influencia del proyecto, corresponde a la
caracterización inicial del agua del Estero Cholguague aguas arriba de la descarga (Informe de Ensayo
N° 260065-01). La condición inicial del agua se midió en la bocatoma de la piscicultura, y entregó las
siguientes concentraciones: <5mg/L para Aceites y Grasas, 2,18mg/L para Cloruros, 3mg/L para la DBO,
0,53mg/L para el fósforo total, 1,81 mg/L para el Nitrógeno Kjeldahl, y < 5 mg/L para los sólidos
suspendidos totales. Para el escenario productivo y de tratamiento de efluentes actual, esta calidad inicial
se recupera, aguas abajo de la descarga de efluentes de la piscicultura, previo a los 200 metros iniciales.

Para la condición proyectada, se contemplan mejoras en el sistema de tratamiento de efluentes, con la
incorporación de un sistema de filtración (filtros rotatorios con mallas de 90 micras). Conforme a la
simulación, para este escenario productivo y de tratamiento de efluentes, la calidad inicial se recupera,
aguas abajo de la descarga de efluentes de la piscicultura, previo a los 200 metros iniciales para los

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

parámetros Aceites y Grasas, DBO 5, Nitrógeno, Fósforo total y Sólidos Suspendidos Totales, en tanto
que el Cloruro recupera la condición medida en la bocatoma a 1.004 metros aguas abajo de la descarga.
No obstante, se debe tener en consideración, que el Cloruro se encuentra bajo los límites máximos
definidos por la OMS, la Guía de CONAMA y la NCh 1.333.

En consecuencia, el área de influencia para el escenario proyectado, en términos de calidad del agua,
alcanza una distancia de 200 metros aguas abajo de la descarga de efluentes, para los parámetros Aceites
y Grasas, DBO 5, Nitrógeno, Fósforo total y Sólidos Suspendidos Totales, y de 1.004m para el parámetro

Cloruro.

Para resguardar los usos de agua del cuerpo receptor, se propone efectuar un monitoreo fisicoquímico
según NCh 1.333, en periodo de estiaje, de los parámetros asociados a los usos de agua existentes: riego,
vida acuática y recreacional con contacto directo, además de un monitoreo de la fauna íctica, en periodo
de estiaje. Estos programas de monitoreos se detallan en el Capítulo 7 de la Declaración de Impacto
Ambiental del proyecto “Modificación Proyecto Técnico Piscicultura El Peral”.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Anexos 1. Informe de Ensayo N° 260065-01.

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

Estudio de Modelación de la Dilución del Efluente y Usos de Agua en el Cuerpo Receptor Estero Cholguague

Modificación Proyecto Técnico Piscicultura El Peral, Comuna de Los Ángeles - Región del Biobío

Anexos 2. Informes SACEI Piscicultura El Peral 2005-2015 (planillas solo en formato digital, Excel).

Anexo 3. Consulta Expediente CPA

BIOGEA LIMITADA

  [e-mail: contacto@biogea.cl](mailto:contacto@biogea.cl)

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Expediente CPA derechos de aprovechamiento de agua otorgados Estero Cholguagüe.**

| Expediente | N° Res.<br>DGA | Nombre peticionario | Caudal<br>(L/s) | Tipo | Coordenadas UTM captaciones | Col7 | Col8 | Distancia respecto<br>de la descarga<br>piscicultura |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Expediente | N° Res.<br>DGA | Nombre peticionario | Caudal<br>(L/s) | Tipo | Este | Norte | Datum | Datum |
| ND-0802-67 | 302/1995 | Javier Curilemu Soto | 900 | NC | 749.463 | 5.847.853 | WGS 84 | Bocatoma Proyecto |
| ND-0802-363 | 258/2006 | Javier Curilemu Soto | 600 | NC | 752.000 | 5.849.650 | PSAD56 | 3,4 km aguas arriba |
| ND-0802-934 | 256/2010 | Arnoldo Videla M. | 30 | NC | 752.050 | 5.849.665 | PSAD56 | 3,5 km aguas arriba |
| ND-0802-1214 | 270/1989 | Humberto Vallejos M. | 56 | C | 746.858 | 5.847.370 | WGS 84 | 2 km aguas abajo |

**Tabla 3.: Concentración de los indicadores, previo a la descarga de la Piscicultura El Peral.**

| Parámetro | Unidad | Valor | Fuente |
| --- | --- | --- | --- |
| Nitrógeno total Kjeldahl | mg/L | 1,81 | Informe de Ensayo N° 260065-01 |
| Fósforo Total | mg/L | 0,53 | Informe de Ensayo N° 260065-01 |
| Cloruro | mg/L | 2,18 | Informe de Ensayo N° 260065-01 |
| Sólidos Suspendidos Totales | mg/L | < 5,00 | Informe de Ensayo N° 260065-01 |
| Demanda Bioquímica de Oxígeno | mg/L | 3 | Informe de Ensayo N° 260065-01 |
| Aceites y Grasas | mg/L | < 5,00 | Informe de Ensayo N° 260065-01 |

**Tabla 6.: Aplicación de Sal a estanques de mayor volumen.**

| N°<br>Estanques | Capacidad<br>útil<br>individual | N°<br>Estanques<br>tratados<br>simultáneos | Nivel<br>medio de<br>agua | Tasa<br>recambio<br>agua | Dosificación<br>sal | Cantidad<br>de sal<br>usada | Concentración<br>sal en los<br>estanques |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 63,6 m3 | 3 | 12,5 m3 | 1,5h-1 | 1% | 375 kg | 10 g/L |

**Tabla 7.: Constante cinéticas utilizadas en la simulación.**

| Parámetros | Constante | Fuente |
| --- | --- | --- |
| Cloruro | 0,0032 | SEIA7 |
| Demanda Bioquímica de Oxígeno | 0,1350 | Metcalf (1998) |
| Fósforo Total | 0,009 | Quenzer (1998) |
| Nitrógeno | 0,0220 | Quenzer (1998) |
| Sólidos Suspendidos Totales | 0,1450 | Metcalf (1998) |
| Aceites y Grasas | 0,1450 | Metcalf (1998) |

**Tabla 8.: Datos de entrada para la modelación, condición actual.**

| Parámetros | Unidad | AyG | DBO<br>5 | PT | NT | SST |
| --- | --- | --- | --- | --- | --- | --- |
| Qo | m3/s | 0,695 | 0,695 | 0,695 | 0,695 | 0,695 |
| QCanal | m3/s | 0,045 | 0,045 | 0,045 | 0,045 | 0,045 |
| Qr | m3/s | 0,045 | 0,045 | 0,045 | 0,045 | 0,045 |
| Qe | m3/s | 0,650 | 0,650 | 0,650 | 0,650 | 0,650 |
| Co | mg/L | 9,68 | 7,68 | 1,33 | 5,94 | 12,58 |
| Cr | mg/L | 5,00 | 3,00 | 0,53 | 1,81 | 5,00 |
| Ce (Perc95) | mg/L | 10,00 | 8,00 | 1,38 | 6,23 | 13,10 |
| μ | m/s | 0,900 | 0,900 | 0,900 | 0,900 | 0,900 |
| k | - | 0,1450 | 0,1350 | 0,0010 | 0,0220 | 0,1450 |

**Tabla 9.: Resultados de la modelación, condición actual.**

| x (m) | AyG | DBO<br>5 | Fósforo | NTK | SST |
| --- | --- | --- | --- | --- | --- |
| 0 | 9,6763 | 7,6763 | 1,3250 | 5,9438 | 12,5755 |
| 1 | 8,2364 | 6,6070 | 1,3118 | 5,8003 | 10,7043 |
| 2 | 7,0108 | 5,6867 | 1,2987 | 5,6602 | 9,1114 |
| 3 | 5,9676 | 4,8946 | 1,2858 | 5,5235 | 7,7556 |
| 4 | 5,0796 | 4,2128 | 1,2730 | 5,3901 | 6,6016 |
| 5 | 4,3237 | 3,6260 | 1,2603 | 5,2600 | 5,6192 |
| 6 | 3,6804 | 3,1209 | 1,2478 | 5,1330 | 4,7831 |
| 7 | 3,1327 | 2,6862 | 1,2354 | 5,0090 | 4,0714 |
| 8 | 2,6666 | 2,3120 | 1,2231 | 4,8881 | 3,4655 |
| 9 | 2,2698 | 1,9900 | 1,2109 | 4,7700 | 2,9498 |
| 10 | 1,9320 | 1,7128 | 1,1989 | 4,6548 | 2,5109 |
| 20 | 0,3858 | 0,3822 | 1,0848 | 3,6454 | 0,5013 |
| 30 | 0,0770 | 0,0853 | 0,9816 | 2,8548 | 0,1001 |
| 40 | 0,0154 | 0,0190 | 0,8881 | 2,2357 | 0,0200 |
| 50 | 0,0031 | 0,0042 | 0,8036 | 1,7509 | 0,0040 |
| 60 | 0,0006 | 0,0009 | 0,7272 | 1,3712 | 0,0008 |
| 70 | 0,0001 | 0,0002 | 0,6580 | 1,0738 | 0,0002 |
| 80 | 0,0000 | 0,0000 | 0,5953 | 0,8410 | 0,0000 |
| 90 | 0,0000 | 0,0000 | 0,5387 | 0,6586 | 0,0000 |
| 100 | 0,0000 | 0,0000 | 0,4874 | 0,5158 | 0,0000 |
| 120 | 0,0000 | 0,0000 | 0,3991 | 0,3163 | 0,0000 |
| 130 | 0,0000 | 0,0000 | 0,3611 | 0,2477 | 0,0000 |
| 140 | 0,0000 | 0,0000 | 0,3267 | 0,1940 | 0,0000 |
| 150 | 0,0000 | 0,0000 | 0,2956 | 0,1519 | 0,0000 |
| 160 | 0,0000 | 0,0000 | 0,2675 | 0,1190 | 0,0000 |
| 170 | 0,0000 | 0,0000 | 0,2420 | 0,0932 | 0,0000 |
| 180 | 0,0000 | 0,0000 | 0,2190 | 0,0730 | 0,0000 |
| 190 | 0,0000 | 0,0000 | 0,1982 | 0,0571 | 0,0000 |
| 200 | 0,0000 | 0,0000 | 0,1793 | 0,0448 | 0,0000 |
| 220 | 0,0000 | 0,0000 | 0,1468 | 0,0274 | 0,0000 |
| 240 | 0,0000 | 0,0000 | 0,1202 | 0,0168 | 0,0000 |
| 260 | 0,0000 | 0,0000 | 0,0984 | 0,0103 | 0,0000 |
| 280 | 0,0000 | 0,0000 | 0,0806 | 0,0063 | 0,0000 |
| 300 | 0,0000 | 0,0000 | 0,0660 | 0,0039 | 0,0000 |
| 320 | 0,0000 | 0,0000 | 0,0540 | 0,0024 | 0,0000 |
| 321 | 0,0000 | 0,0000 | 0,0557 | 0,0024 | 0,0000 |
| 325 | 0,0000 | 0,0000 | 0,0535 | 0,0022 | 0,0000 |
| 330 | 0,0000 | 0,0000 | 0,0509 | 0,0020 | 0,0000 |
| 340 | 0,0000 | 0,0000 | 0,0461 | 0,0015 | 0,0000 |

**Tabla 10.: Datos de entrada para la simulación de la situación proyectada de Piscicultura El Peral.**

| Parámetros | Unidad | AyG | Cloruro | DBO<br>5 | PT | NT | SST |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Qo | m3/s | 0,945 | 0,945 | 0,945 | 0,945 | 0,945 | 0,945 |
| QCanal | m3/s | 0,045 | 0,045 | 0,045 | 0,045 | 0,045 | 0,045 |
| Qr | m3/s | 0,045 | 0,045 | 0,045 | 0,045 | 0,045 | 0,045 |
| Qe | m3/s | 0,900 | 0,900 | 0,900 | 0,900 | 0,900 | 0,900 |
| Co | mg/L | 0,4316 | 73,5895 | 6,1687 | 0,1852 | 2,6940 | 3,4767 |
| Cr | mg/L | 5,00 | 2,18 | 3,00 | 0,53 | 1,81 | 5,00 |
| Ce (Perc95) | mg/L | 0,2032 | 77,1600 | 6,3271 | 0,1680 | 2,7382 | 3,4005 |
| μ | m/s | 0,900 | 0,900 | 0,900 | 0,900 | 0,900 | 0,900 |
| k | - | 0,1450 | 0,0032 | 0,1350 | 0,0010 | 0,0220 | 0,1450 |

**Tabla 11.: Datos de entrada simulación de dilución del efluente de Piscicultura El Peral.**

| x (m) | AyG | Cloruro | DBO<br>5 | Fósforo | NTK | SST |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0,4316 | 73,5895 | 6,1687 | 0,1852 | 2,6940 | 3,4767 |
| 1 | 0,3674 | 73,3283 | 5,3094 | 0,1834 | 2,6289 | 2,9593 |
| 2 | 0,3127 | 73,0681 | 4,5699 | 0,1816 | 2,5655 | 2,5190 |
| 3 | 0,2662 | 72,8087 | 3,9333 | 0,1798 | 2,5035 | 2,1441 |
| 4 | 0,2266 | 72,5503 | 3,3854 | 0,1780 | 2,4431 | 1,8251 |
| 5 | 0,1929 | 72,2928 | 2,9139 | 0,1762 | 2,3841 | 1,5535 |
| 6 | 0,1642 | 72,0362 | 2,5080 | 0,1745 | 2,3265 | 1,3223 |
| 7 | 0,1397 | 71,7806 | 2,1586 | 0,1727 | 2,2703 | 1,1256 |
| 8 | 0,1189 | 71,5258 | 1,8580 | 0,1710 | 2,2155 | 0,9581 |
| 9 | 0,1012 | 71,2719 | 1,5992 | 0,1693 | 2,1620 | 0,8155 |
| 10 | 0,0862 | 71,0190 | 1,3764 | 0,1676 | 2,1098 | 0,6942 |
| 20 | 0,0172 | 68,5382 | 0,3071 | 0,1517 | 1,6523 | 0,1386 |
| 30 | 0,0034 | 66,1441 | 0,0685 | 0,1372 | 1,2939 | 0,0277 |
| 40 | 0,0007 | 63,8336 | 0,0153 | 0,1242 | 1,0133 | 0,0055 |
| 50 | 0,0001 | 61,6039 | 0,0034 | 0,1124 | 0,7936 | 0,0011 |
| 60 | 0,0000 | 59,4520 | 0,0008 | 0,1017 | 0,6215 | 0,0002 |
| 70 | 0,0000 | 57,3753 | 0,0002 | 0,0920 | 0,4867 | 0,0000 |
| 80 | 0,0000 | 55,3711 | 0,0000 | 0,0832 | 0,3812 | 0,0000 |
| 90 | 0,0000 | 53,4370 | 0,0000 | 0,0753 | 0,2985 | 0,0000 |
