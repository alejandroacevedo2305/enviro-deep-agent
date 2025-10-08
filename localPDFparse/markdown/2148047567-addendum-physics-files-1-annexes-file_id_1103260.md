---
title: Proyecto Captacion de agua canal La Higuera
author: Eduardo Rojas
date: D:20201112100226-03'00'
language: es
type: report
pages: 29
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANÁLISIS DE ESTABILIDAD EN CONDICIÓN DE TERMINO DEL MURO DE REFUERZO DEL TRANQUE DE RELAVES
-->

# ANÁLISIS DE ESTABILIDAD EN CONDICIÓN DE TERMINO DEL MURO DE REFUERZO DEL TRANQUE DE RELAVES

MASMINING-2020-TAL1707-INF-GE-003-REVC-OFT
PROYECTO: “ DECLARACIÓN DE IMPACTO AMBIENTAL PARA

EL AUMENTO DE VIDA ÚTIL DEL PROYECTO
OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

CLIENTE: ENAMI

20 DE AGOSTO DE 2020

Cliente Señor : Víctor Olivares Pérez - Gerente Seguridad y Sustentabilidad - ENAMI.

Gerente de Proyecto: Eduardo Rojas Gómez - Gerente General - MASMINING

|Col1|Registro de EMISIÓN/REVISIÓN|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Código de<br>emisión|Revisión|Revisión|Revisión|Revisión|Revisión|Detalles de revisión|
|Código de<br>emisión|N°|Por|Revisado|Aprobado|Fecha|Fecha|
|RR|A|DL|ER|VR|14-08-2020|Revisión Interna|
|RR|A|DL|ER|VR|17-08-2020|Revisión Cliente|
|RR|B|DL|ER|VR|20-08-2020|Revisión Cliente|
|RR|C|DL|ER|VR|21-10-2020|Revisión Cliente|
||||||||
||||||||

Códigos de emisión: EC: Emitido para construcción, RD: Emitido para diseño, RF: Emitido para fabricación, RI: Emitido para

información, RP: Emitido para compra, RQ: Emitido para cotización, RR: Emitido para revisión y comentarios.
**EA: Eric Astorga; VR: Victor Rivera; DL: Damarys Lagunas; PZ: Paola Zepeda; MR: Milenko Rojo; ER: Eduardo Rojas;**

**A: Versión N° A, B, C y 0**

MASMINING
Avenida Balmaceda 417, Oficina 32, La Serena - Chile

Fono Celular +56 9 71396155 | Fijo +51 2 590140

erojas@masmining.com | [www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**INDICE**

**1** **INTRODUCCIÓN ...................................................................................................................................... 10**

**2** **OBJETIVOS................................................................................................................................................ 11**

2.1 O BJETIVO G ENERAL .................................................................................................................................. 11

2.2 O BJETIVOS E SPECÍFICOS ........................................................................................................................... 11

**3** **ALCANCE Y REFERENCIAS ................................................................................................................. 12**

3.1 A LCANCE F ÍSICO ....................................................................................................................................... 12

3.2 A LCANCES DEL D OCUMENTO .................................................................................................................... 12

3.3 U BICACIÓN G EOGRÁFICA DEL P ROYECTO ................................................................................................ 12

3.4 R EFERENCIAS ............................................................................................................................................ 13

**4** **SISTEMA DE UNIDADES Y SIMBOLOGÍA ......................................................................................... 14**

4.1 S ISTEMA DE U NIDADES ............................................................................................................................. 14

**5** **CONFIGURACIÓN GEOMETRICA DE ANÁLISIS ............................................................................ 15**

**6** **PROPIEDADES Y PARÁMETROS GEOTÉCNICOS .......................................................................... 18**

6.1 S UELO DE F UNDACIÓN .............................................................................................................................. 19

6.2 R IPIOS DE L IXIVIACIÓN ............................................................................................................................. 19

6.3 I NTERFAZ RIPIO - GEOMEMBRANA - SUELO ................................................................................................... 20

6.4 A RENA DE R ELAVES ................................................................................................................................. 20

6.5 L AMAS ...................................................................................................................................................... 21

**7** **SOLICITACIONES SISMICAS ............................................................................................................... 21**

**7.1** **A** **MENAZA** **S** **ÍSMICA** .............................................................................................................................. 21
**7.2** **C** **OEFICIENTES** **S** **ÍSMICOS** .................................................................................................................... 22

**8** **ESCENARIO DE ANÁLISIS .................................................................................................................... 23**

**8.1** **C** **ONSIDERACIONES DE ANÁLISIS** ........................................................................................................ 23

8.2 H IPÓTESIS DE CÁLCULO ............................................................................................................................ 23

**9** **METODO DE CÁLCULO ......................................................................................................................... 24**

**9.1** **A** **NÁLISIS** **E** **STÁTICO** ............................................................................................................................ 24
**9.2** **A** **NÁLISIS** **P** **SEUDO** **-** **ESTÁTICO** ............................................................................................................. 25

**9.3** **H** **ERRAMIENTA** **C** **OMPUTACIONAL** ....................................................................................................... 25

**9.4** **F** **ACTORES DE** **S** **EGURIDAD** ................................................................................................................. 25

**10** **RESULTADOS DE ANÁLISIS ................................................................................................................. 26**

**11** **CONCLUSIONES Y COMENTARIOS ................................................................................................... 34**

FIGURAS

Figura 1-1. Ubicación planta José A. Moreno; sector Planta Principal y Planta Secundaria ..10
Figura 3-1. Ubicación geográfica del Proyecto ......................................................................13

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

Figura 5-1. Ubicación de perfiles críticos en zona de estudio ................................................15
Figura 5-2. Sección de Análisis “A”, Etapa I ..........................................................................16
Figura 5-3. Sección de Análisis “B”, Etapa I ..........................................................................16
Figura 5-4. Sección de Análisis “C”, Etapa I ..........................................................................16
Figura 5-5. Sección de Análisis “D”, Etapa II .........................................................................17
Figura 5-6. Sección de Análisis “E”, Etapa II .........................................................................17
Figura 5-7. Sección de Análisis “F”, Etapa III ........................................................................17
Figura 5-8. Sección de Análisis “G”, Etapa III .......................................................................18
Figura 5-9. Sección de Análisis “H”, Etapa III ........................................................................18
Figura 6-1. Esquema representativo de materiales ...............................................................19
Figura 10-1. Resultado Estabilidad Sección A. .....................................................................27
Figura 10-2. Resultado Estabilidad Sección B. .....................................................................27
Figura 10-3. Resultado Estabilidad Sección C. Condición Estática .......................................28
Figura 10-4. Resultado Estabilidad Sección C. Condición Sísmica .......................................28
Figura 10-5. Resultado Estabilidad Sección D. Condición Estática .......................................29
Figura 10-6. Resultado Estabilidad Sección D. Condición Sísmica .......................................29
Figura 10-7. Resultado Estabilidad Sección E. Condición Estática .......................................30
Figura 10-8. Resultado Estabilidad Sección E. Condición Sísmica .......................................30
Figura 10-9. Resultado Estabilidad Sección F. Condición Estática .......................................31
Figura 10-10. Resultado Estabilidad Sección F. Condición Sísmica .....................................31
Figura 10-11. Resultado Estabilidad Sección G. Condición Estática .....................................32
Figura 10-12. Resultado Estabilidad Sección G. Condición Sísmica .....................................32
Figura 10-13. Resultado Estabilidad Sección H. Condición Estática .....................................33
Figura 10-14. Resultado Estabilidad Sección H. Condición Sísmica .....................................33

TABLAS

Tabla 2-1. Listado de Referencias ........................................................................................13

Tabla 3-1. Unidades base SI .................................................................................................14
Tabla 3-2. Unidades alternativas permitidas .........................................................................14
Tabla 6-1. Propiedades y parámetros del Suelo de Fundación .............................................19
Tabla 5-2. Propiedades y parámetros Ripios de Lixiviación ..................................................20
Tabla 6-3. Propiedades y parámetros Interfaz ......................................................................20
Tabla 5-4. Parámetros y propiedades Muro de Arena de Relaves ........................................21
Tabla 5-5. Parámetros y propiedades Lamas .......................................................................21
Tabla 6-1. Características sismo de diseño considerado ......................................................22
Tabla 10-1. Resultados estabilidad para los distintos perfiles ...............................................26

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**1** **INTRODUCCIÓN**

La Planta José A. Moreno, está ubicada en la ciudad de Taltal, a 309 Km de la ciudad de
Antofagasta, en la II Región de Antofagasta. En la actualidad mensualmente procesa del
orden de 10.000 t [i] de minerales oxidados, obteniendo como producto 200 t/mes de
Cátodos de Cobre.

Dicha Planta, comprende dos áreas denominadas; Planta Principal y Planta Secundaria,
según se muestra en la Figura 1-1 a continuación.

**Figura 1-1. Ubicación planta José A. Moreno; sector Planta Principal y Planta Secundaria**

Fuente: ENAMI, sobre Google Earth.

La situación actual en faena, aún se está desarrollando el Proyecto “ **Optimización de**
**Disposición de Ripios de Lixiviación, Planta Taltal** ”, en adelante el Proyecto Original
que fue aprobado mediante RCA N°150/2011, el cual aún no ha completado su diseño
total geométrico (en volumen) aprobado, motivo por el cual, para terminar el muro de

i t: toneladas. (Las unidades usadas en este documento se encuentran en el apartado “Sistema de Unidades y
Simbología).

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

refuerzo es necesario continuar depositando ripios, y por consecuencia extender la vida
útil del proyecto original, de tal manera de poder terminar el muro de refuerzo del
Tranque de Relaves.

El aumento de la vida útil se justifica debido a que la disposición de ripios en el muro de
refuerzo se ha realizado con un mejor nivel de compactación y una tasa de depositación
promedio anual menor a la programada en el proyecto, por lo tanto, no se ha alcanzado
a finalizar su construcción en el periodo aprobado, tanto la cota de altura como el
volumen autorizado mediante RCA N°150/2011.

En resumen, este nuevo proyecto denominado Extensión de la vida útil del Proyecto
Optimización de Disposición de Ripios de Lixiviación, Planta Taltal, busca como objetivo
principal modificar la vida útil del proyecto original de tal forma de culminar su diseño
geométrico y volumen original para de ese modo reforzar la seguridad del tranque de
Relaves en la fase de cierre.

El proyecto está siendo controlado por una empresa contratista de maquinarias, y
controlado geométrica y geotécnicamente por una segunda empresa externa. La
estadística de cada uno de los controles y mediciones topográficas generados en el
tiempo y la producción mensual, son base para los informes técnicos del presente
proyecto.

**2** **OBJETIVOS**

**2.1 Objetivo General**

El proyecto “Extensión de vida útil del Proyecto Optimización de Disposición de ripios de
lixiviación, Planta Taltal”, tiene como objetivo modificar la extensión de la vida útil del
proyecto original aprobado favorablemente por la RCA 150/2011, de tal forma de
culminar su diseño geométrico y volumen original para de ese modo reforzar la
seguridad del tranque de Relaves en la fase de cierre.

**2.2 Objetivos Específicos**

El objetivo del presente documento es analizar la estabilidad de taludes del muro de
refuerzo, considerando la depositación de ripios lixiviados hasta la condición de termino,
es decir, hasta la cota 33 m s.n.m.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**3** **ALCANCE Y REFERENCIAS**

**3.1 Alcance Físico**

El alcance de este documento comprende el muro de refuerzos del tranque de relaves,
correspondiente al Proyecto Original.

**3.2 Alcances del Documento**

Se considera la verificación de la estabilidad tanto estática como pseudo-estática del
refuerzo del muro del tranque de relaves.

El análisis corresponde a la modelación de las secciones transversales consideradas
como las más desfavorables desde el punto de vista geométrico, considerando como
principal aspecto para su elección la altura total máxima, taludes, materialidad y apoyo.

**3.3 Ubicación Geográfica del Proyecto**

El proyecto se encuentra localizado en la Provincia de Antofagasta, comuna de Taltal,
Región de Antofagasta a aproximadamente 236 Km al sur de la ciudad de Antofagasta.
Con mayor exactitud, la Planta se encuentra ubicada al noroeste de la ciudad de Taltal,
donde el Proyecto se encuentra en el sector de lixiviación secundaria y Zona de
Depósito de Residuos Masivos Mineros de la Planta, distante 1,5 Km. de la ubicación de
la Planta y de la población más cercana (Localidad de Taltal).

La ubicación geográfica se muestra en la Figura 3-1 siguiente.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 3-1. Ubicación geográfica del Proyecto**

**3.4 Referencias**

Los documentos listados a continuación, han sido usados como bibliografía en la
confección de este informe:

**Tabla 3-1. Listado de Referencias**

|Ref. N°|N° Documento|Descripción|
|---|---|---|
|1.|S/N|Análisis del Riesgo Sísmico para la Reconstrucción del Puerto<br>de Valparaíso. Sextas Jornadas Chilenas de Sismología e<br>Ingeniería Sísmica, Vol. 2. Santiago, Chile. Saragoni, R., 1993|
|2.|S/N|Earth and Rock-Fill Dams - General Design and Construction<br>Considerations by U.S. Army Corps of Engineers, July 1994|
|3.|S/N|Descripción Muro de Refuerzo, Planta Jose Antonio Moreno,<br>Taltal. ENAMI.|
|4.|S/N|“Seismic Slope Stabilty and Analysis of the Upper San<br>Fernando Dam”, James Dismuke, 2002.|

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

|Ref. N°|N° Documento|Descripción|
|---|---|---|
|5.|S/N|Proyecto Ingeniería de Detalles de Cierre Tranque de Relaves,<br>2010.|
|6.|S/N|DECLARACION DE IMPACTO AMBIENTAL, Optimización de<br>Disposición de Ripios de Lixiviación, Planta Taltal.|
|7.|PRO-CTL-280819-<br>GEO27-TAL-1072 VA|Control De Construcción Muro De Ripios Para El Refuerzo Del<br>Tranque De Relaves, Informe Mensual Julio 2020.|
|8.|MASMINING-2020-<br>TAL1707-PFL-OC-F-<br>001|Optimización Disposición de Ripios en Muro de Refuerzo del<br>Traque de Relaves - Planta José A. Moreno-ENAMI-TALTAL,<br>Plantas y Secciones.|

Durante la lectura del documento se presentan notas al pie de página, las cuales están
asociadas con bibliografía explicativa de los términos mencionados.

**4** **SISTEMA DE UNIDADES Y SIMBOLOGÍA**

**4.1 Sistema de Unidades**

El sistema de unidades a utilizar en el documento corresponderá al Sistema
Internacional de Unidades [ii] (SI). Se utilizará el punto para separar los miles y la coma
para separar los decimales.

Las unidades base, derivadas, prefijos y otros se indican en las tablas siguientes.

**Tabla 4-1. Unidades base SI**

|Medición|Unidad|Simbología|
|---|---|---|
|Longitud|Metro|m|
|Masa|Kilogramo|kg|
|Tiempo|Segundo|s|
|Superficie|Hectárea|ha|

**Tabla 4-2. Unidades alternativas permitidas**

|Medición|Unidad|Simbología|
|---|---|---|
|Masa|Tonelada métrica|t|
|Masa|Gramo|g|
|Tiempo|Minuto|min|
|Tiempo|Hora|h|

ii El Sistema Internacional de Unidades corresponde al sistema de unidades que se usa en casi todos los países del
mundo.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

|Col1|Día|d|
|---|---|---|
||Año|a|
|Temperatura|Grados Celsius|°C|
|Volumen|Litro|L|
|Volumen|Metros cúbicos|m3|

**5** **CONFIGURACIÓN GEOMETRICA DE ANÁLISIS**

En el siguiente apartado se presentan los perfiles analizados en el desarrollo de
estabilidad de taludes.

El análisis comprende un total de ocho perfiles transversales trazados en las zonas más
desfavorables desde el punto de vista geométrico considerando la depositación de ripios
lixiviados en el muro de refuerzo hasta la cota 33 m s.n.m.

A continuación, en la Figura 5-1 se muestra la ubicación en planta de los perfiles a
analizar, los perfiles de estudio son denominados desde la letra A hasta la letra H.
Mientras que, las Figuras a continuación presentan en detalle cada una de las secciones
consideradas en el estudio de estabilidad.

**Figura 5-1. Ubicación de perfiles críticos en zona de estudio**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 5-2. Sección de Análisis “A”, Etapa I**

**Figura 5-3. Sección de Análisis “B”, Etapa I**

**Figura 5-4. Sección de Análisis “C”, Etapa I**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 5-5. Sección de Análisis “D”, Etapa II**

**Figura 5-6. Sección de Análisis “E”, Etapa II**

**Figura 5-7. Sección de Análisis “F”, Etapa III**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 5-8. Sección de Análisis “G”, Etapa III**

**Figura 5-9. Sección de Análisis “H”, Etapa III**

**6** **PROPIEDADES Y PARÁMETROS GEOTÉCNICOS**

En los siguientes ítems, se entregan los parámetros geotécnicos pertenecientes a cada
uno de los materiales considerados en el presente estudio.

La Figura 6-1 muestra de manera gráfica la ubicación de los materiales que se
presentaran en los apartados a continuación.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 6-1. Esquema representativo de materiales**

**6.1 Suelo de Fundación**

En la Tabla 6-1, se indican las propiedades y parámetros geotécnicos del suelo de
fundación representativo en la zona de emplazamiento del muro de refuerzo.

Los parámetros geotécnicos adoptados para el Suelo de Fundación fueron obtenidos de
la Ref. N° 6.

**Tabla 6-1. Propiedades y parámetros del Suelo de Fundación**

|Parámetro|Valor|Unidad|Referencia|
|---|---|---|---|
|Densidad húmeda,t|2,17|t/m3|N° 6|
|Angulo de fricción,|35|grados|N° 6|
|Cohesión, c|1,00|kPa|N° 6|

**6.2 Ripios de Lixiviación**

A continuación, en la Tabla 6-2 se presentan las propiedades y parámetros geotécnicos
de los ripios de lixiviación.

Los parámetros de resistencia al corte adoptados (Angulo de Fricción Interna y
Cohesión) fueron obtenidos de la Ref. N° 6, mientras que la Densidad Húmeda de los
ripios se obtuvo de la Ref. N° 7, documento que entrega los parámetros geotécnicos
actualizados hasta Julio de 2020 de los ripios de lixiviación.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Tabla 6-2. Propiedades y parámetros Ripios de Lixiviación**

|Parámetro|Valor|Unidad|Referencia|
|---|---|---|---|
|Densidad húmeda,h|2,09|t/m3|N° 7|
|Angulo de fricción,|38|grados|N° 6|
|Cohesión, c|1,00|kPa|N° 6|

**6.3 Interfaz ripio-geomembrana-suelo**

En la Tabla 6-3, se indican las propiedades y parámetros adoptados para la interfaz
ripio-geomembrana-suelo.

**Tabla 6-3. Propiedades y parámetros Interfaz**

|Parámetro|Valor|Unidad|Referencia|
|---|---|---|---|
|Densidad húmeda,h|1,00|t/m3|N° 6|
|Angulo de fricción,|23,0|grados|N° 6|
|Cohesión, c|0,0|kPa|N° 6|

Estos parámetros fueron obtenidos de la Ref N° 6, los valores utilizados son
conservadores, debido principalmente a que el diseño propuesto para el presente
estudio considera la condición más desfavorable, que corresponde a una geomembrana
simplemente texturada en la interfaz ripio-geomembrana-suelo. Entendiéndose suelo,
como material granular, pudiendo ser arena o terreno de fundación.

Valores típicos en interfaces como la mencionada, se esperan ángulos de fricción entre
18° - 27° y cohesión nula (Andrade, 1997), siendo un valor aceptado en este tipo de
análisis 23° (Breitenbach, 2004).

**6.4 Arena de Relaves**

La Tabla 6-4 entrega los parámetros de análisis correspondientes a la Arena de Relaves,
estos parámetros fueron obtenidos a partir de la Ref. N° 6 y conforman el conocido Muro
de Arenas.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Tabla 6-4. Parámetros y propiedades Muro de Arena de Relaves**

|Parámetro|Valor|Unidad|Referencia|
|---|---|---|---|
|Densidad húmeda,h|2,00|t/m3|N° 6|
|Angulo de fricción,|33|grados|N° 6|
|Cohesión, c|0,00|kPa|N° 6|

**6.5 Lamas**

A continuación, en la Tabla 6-5, se presentan los parámetros geotécnicos
correspondientes a las lamas que conforman la cubeta del Tranque de Relaves. Estos
valores fueron obtenidos a partir de la Ref. N° 6.

**Tabla 6-5. Parámetros y propiedades Lamas**

|Parámetro|Valor|Unidad|Referencia|
|---|---|---|---|
|Densidad húmeda,h|1,40|t/m3|N° 6|
|Angulo de fricción,|25|grados|N° 6|
|Cohesión, c|0,00|kPa|N° 6|

**7** **SOLICITACIONES SISMICAS**

**7.1 Amenaza Sísmica**

La estabilidad de los taludes durante la ocurrencia de un evento sísmico se evalúa a

través de un análisis pseudo-estático, en los cuales el efecto del sismo se simula
mediante fuerzas inerciales aplicadas a la potencial cuña de deslizamiento. Estas
fuerzas, proporcionales a la masa de la cuña de deslizamiento, se definen a través de
coeficientes sísmicos.

Se ha adoptado como sismo de diseño para la evaluación de la estabilidad del refuerzo
uno terremoto tipo interplaca subductivo con una magnitud de Ritcher (Ms) de 9,0o
ubicado frente a las costas de Antofagasta. Los parámetros del sismo considerado son
los presentados en la Tabla 7-1.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Tabla 7-1. Características sismo de diseño considerado**

|Mecanismo de fractura|Costero Interplaca (Thrust)|
|---|---|
|Magnitud del sismo de diseño (Ms)|9,0°|
|Distancia Epicentral (Km)|195|
|Profundidad Focal (Km)|30|

Con la magnitud del sismo considerado, más las características presentadas en la tabla
anterior (Tabla 7-1), es posible definir la aceleración máxima que este sismo generará a
través de las relaciones de atenuación propuestas por Ruiz, S y Saragoni, R (2005) para
sismos costeros interplaca. La expresión que permite obtener la aceleración máxima (a h )
es la siguiente:

Donde,

M: Magnitud del sismo.

R: Distancia hipocentral.

A partir de esta expresión se obtiene un valor de aceleración máxima igual a h = 0,55g

**7.2 Coeficientes Sísmicos**

En la práctica habitual del análisis de estabilidad de taludes, se adopta un coeficiente
sísmico horizontal, k h, que corresponde a un porcentaje de la aceleración horizontal
máxima (a h ). Un criterio habitual es adoptar un coeficiente sísmico vertical, k v, nulo, ya
que en la práctica, éste tiene una escasa influencia sobre los factores de seguridad
finalmente calculados.

Para el caso chileno, los estudios efectuados por Saragoni indican lo siguiente:

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

En consecuencia, asumiendo las recomendaciones de Saragoni, se considera el
siguiente coeficiente sísmico (valor aproximado):

✓ Para sismo de diseño **k** **h** **= 0,27.**

**8** **ESCENARIO DE ANÁLISIS**

Para el análisis de estabilidad se consideró un único escenario de cálculo, que consiste
en la evaluación de la estabilidad de taludes considerando la depositación de ripios
hasta la cota 33 m. s.n.m en el muro de refuerzo existente.

**8.1 Consideraciones de análisis**

✓ Se considera una condición de homogeneidad e isotropía en los ripios

depositados. Los parámetros resistentes de los ripios se mantienen constantes en
profundidad, durante cada etapa de depositación.

✓ Se considera una geomembrana ubicada como interfaz entre el suelo de

fundación y ripios a disponer (interfaz ripio-geomembrana-suelo fundación), como
también, se considera una geomembrana entre el muro de arenas y el muro de
refuerzo compuesto por ripios de lixiviación, para efectos de análisis a esta
interfaz se le otorga un espesor de 0,1 m.

✓ No se ha considerado la presencia de una zona de material saturado (nivel

freático) sobre la geomembrana proyectada a nivel basal, debido al largo tiempo
de depositación que llevan los ripios en ese lugar.

**8.2 Hipótesis de cálculo**

Para el cálculo de la estabilidad, se asumieron las siguientes hipótesis:

✓ Carga estática (vertical) provocada por el peso unitario total de los materiales

involucrados en el análisis.

✓ Para la verificación de estabilidad estática o por peso propio, los parámetros de

resistencia al corte de los ripios se asocian a una condición drenada, es decir
utilizando el ángulo de fricción y cohesión.

✓ Las secciones del depósito estudiadas serán analizadas sin considerar un nivel

freático.

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**9** **METODO DE CÁLCULO**

**9.1 Análisis Estático**

El análisis estático se realiza mediante la aplicación del Método de Equilibrio Límite, el
cual consiste en considerar la condición de equilibrio para una división de la potencial
masa de deslizamiento en cierto número de dovelas o rebanadas para cada perfil
transversal en análisis. En cada dovela se equilibran las fuerzas actuantes para así
equilibrar su conjunto.

Las hipótesis básicas que considera el Método de Equilibrio Límite son:

✓ El suelo se comporta según lo estimado por el criterio de Mohr-Coulomb y la

resistencia se moviliza completa y simultáneamente.

✓ El factor de seguridad de la componente cohesiva y friccionante del material es

igual para todo el estrato que se encuentra en la superficie de deslizamiento.

✓ El proceso de obtención del resultado final se realiza primero equilibrando cada

dovela, para luego generalizarlo para toda la masa de suelo que se encuentra
sobre la superficie deslizante.

Las formulaciones tienen como base la siguiente ecuación propuesta por Fellenius
(1927), también llamada método ordinario:

Dónde :

: Resistencia a la corte movilizada.

: Esfuerzo efectivo normal en la base de la dovela.

: Cohesión.
: Ángulo de fricción interna.

: Factor de seguridad.

El método de equilibrio límite utilizado en este estudio para la determinación del FS,
corresponde al de Morgenstern-Price (1965), el cual considera las fuerzas tangenciales

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

entre rebanadas verificando simultáneamente el equilibrio de fuerzas y momentos.
Dichas fuerzas vienen dadas por la siguiente expresión:

Dónde:

: Fuerza normal entre rebanadas.

: Función senoidal.

: Porcentaje del valor de la función considerado.

**9.2 Análisis Pseudo-estático**

El análisis pseudo-estático considera los efectos sísmicos, introduciéndolos al modelo
como fuerzas constantes y aplicadas a toda la masa deslizante. La magnitud de la
fuerza es igual al peso de la masa que desliza, multiplicada por un coeficiente sísmico
de diseño k h .

**9.3 Herramienta Computacional**

Se utilizará el módulo SLOPE/W del software GeoStudio versión 2012, en condiciones
de Equilibrio Límite considerando las condiciones estáticas y sísmicas mediante el
método de Morgenstern-Price para la evaluación de la estabilidad. Por este método, se
analizan una gran cantidad de superficies potenciales de deslizamiento y determinan los
factores de seguridad asociados.

**9.4 Factores de Seguridad**

El factor de seguridad considerado como aceptable en estos casos según el coeficiente
sísmico de diseño, ha sido el propuesto por Pyque (1981), perteneciente a la banda de
valores de la investigación “Seismic Slope Stabilty and Analysis of he Upper San
Fernando Dam”. (James Dismuke, 2002).

El valor considerado es levemente superior a la unidad, por lo tanto, cada vez que la
aceleración máxima generada por un sismo sea superior al coeficiente sísmico de
seleccionado se generarían fallas intermitentes produciendo desplazamientos en la
masa de ripios. Sin embargo, como este tipo de materiales en condiciones naturales
presenta valores de parámetros resistentes elevados, los desplazamientos generados
serían aceptables, según los resultados obtenidos por las estimaciones realizadas por

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

Seed (1979) aplicando el criterio de Newmark. (Selection of Seismic Coefficients for,
Consulting Engineer, Lafayette CA. Use in Pseudo-Static Slope Stability Analyses,
Robert Pyke. 1997).

**10** **RESULTADOS DE ANÁLISIS**

El presente capítulo incluye los resultados de los factores de seguridad obtenidos para
los perfiles analizados, considerando las superficies de falla representativas para las
propiedades de los materiales involucrados y para la geometría propuesta.

En la Tabla 10-1, se indican los resultados del análisis de estabilidad estática y sísmica
(pseudo-estática) de cada perfil analizado.

**Tabla 10-1. Resultados estabilidad para los distintos perfiles**

|Perfil|Tipo de<br>Falla|Factor de Seguridad|Col4|
|---|---|---|---|
|**Perfil**|**Tipo de**<br>**Falla**|**Estático**|**Sísmico**|
|A|Global|-|-|
|B|Global|-|-|
|C|Global|2,375|1,369|
|D|Global|2,024|1,204|
|E|Global|1,950|1,178|
|F|Global|2,063|1,231|
|G|Global|2,695|1,653|
|H|Global|2,290|1,358|

A continuación, se presentan los resultados del análisis para cada perfil en condición
estática y pseudo-estatica (sísmica).

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 10-1. Resultado Estabilidad Sección A.**

**Figura 10-2. Resultado Estabilidad Sección B.**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 10-3. Resultado Estabilidad Sección C. Condición Estática**

**Figura 10-4. Resultado Estabilidad Sección C. Condición Sísmica**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 10-5. Resultado Estabilidad Sección D. Condición Estática**

**Figura 10-6. Resultado Estabilidad Sección D. Condición Sísmica**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 10-7. Resultado Estabilidad Sección E. Condición Estática**

**Figura 10-8. Resultado Estabilidad Sección E. Condición Sísmica**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 10-9. Resultado Estabilidad Sección F. Condición Estática**

**Figura 10-10. Resultado Estabilidad Sección F. Condición Sísmica**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 10-11. Resultado Estabilidad Sección G. Condición Estática**

**Figura 10-12. Resultado Estabilidad Sección G. Condición Sísmica**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**Figura 10-13. Resultado Estabilidad Sección H. Condición Estática**

**Figura 10-14. Resultado Estabilidad Sección H. Condición Sísmica**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

**11** **CONCLUSIONES Y COMENTARIOS**

Del documento se puede concluir lo siguiente:

✓ La verificación del análisis estático y pseudo-estático muestra que todas las

secciones analizadas no presentan problemas de estabilidad, debido a que los
perfiles estudiados muestran factores de seguridad mayores a los criterios de
aceptabilidad establecidos en el presente estudio.

✓ La sección A y Sección B no presentan análisis de estabilidad, ya que como se

puede observar en la Figura 5-2 y Figura 5-3, la depositación de los ripios queda
confinada por el suelo ya existente (pilas de lixiviación), por lo tanto, no se
presenta ningún talud que pueda generar algún tipo de inestabilidad.

✓ Las secciones analizadas fueron ubicadas en los sectores más desfavorables,

desde el punto de vista geométrico, considerando como principal aspecto para su
elección la altura total máxima, taludes, materialidad y apoyo.

✓ Dada las características geométricas del muro de refuerzo, se desprende que

posee características resistentes suficientes para otorgar una estabilidad acorde
con lo establecido en la normativa actualmente vigente, en función del diseño
geométrico y parámetros señalados.

✓ Dicho lo anterior, se concluye que las obras analizadas se consideran seguras

bajo solicitaciones estáticas y sísmicas, para las combinaciones de cargas,
escenarios, geometrías de diseño y control, incluidas en el presente informe.

✓ Los factores de seguridad aquí presentados son válidos sólo para las

configuraciones, propiedades geotécnicas y criterios presentados en este
documento para cada uno de los materiales indicados. Si alguno de estos
parámetros o propiedades es modificado, se debe llevar a cabo un nuevo
análisis, tanto estático como sísmico, de manera de asegurar la estabilidad de la
nueva configuración de las obras

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

PROYECTO: MASMINING-2020-TAL1707-INF-GE-003-REVA-OFT “DECLARACIÓN DE IMPACTO AMBIENTAL PARA
EL AUMENTO DE VIDA ÚTIL DEL PROYECTO OPTIMIZACIÓN DE DISPOSICIÓN DE RIPIOS DE LIXIVIACIÓN, PLANTA TALTAL ”

Atentamente,

**El Equipo de MASMINING**

**FIN DOCUMENTO**

Avenida Balmaceda 417, Oficina 32, La Serena, Chile
Fono Celular +56 9 71396155 | Fono Fijo 51 2 590140
[erojas@masmining.com | www.masmining.com](http://www.masmining.com/)

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Listado de Referencias****

| Ref. N° | N° Documento | Descripción |
| --- | --- | --- |
| 1. | S/N | Análisis del Riesgo Sísmico para la Reconstrucción del Puerto<br>de Valparaíso. Sextas Jornadas Chilenas de Sismología e<br>Ingeniería Sísmica, Vol. 2. Santiago, Chile. Saragoni, R., 1993 |
| 2. | S/N | Earth and Rock-Fill Dams - General Design and Construction<br>Considerations by U.S. Army Corps of Engineers, July 1994 |
| 3. | S/N | Descripción Muro de Refuerzo, Planta Jose Antonio Moreno,<br>Taltal. ENAMI. |
| 4. | S/N | “Seismic Slope Stabilty and Analysis of the Upper San<br>Fernando Dam”, James Dismuke, 2002. |

**Tabla 4-1.: Unidades base SI****

| Medición | Unidad | Simbología |
| --- | --- | --- |
| Longitud | Metro | m |
| Masa | Kilogramo | kg |
| Tiempo | Segundo | s |
| Superficie | Hectárea | ha |

**Tabla 4-2.: Unidades alternativas permitidas****

| Medición | Unidad | Simbología |
| --- | --- | --- |
| Masa | Tonelada métrica | t |
| Masa | Gramo | g |
| Tiempo | Minuto | min |
| Tiempo | Hora | h |

**Tabla 6-1.: Propiedades y parámetros del Suelo de Fundación****

| Parámetro | Valor | Unidad | Referencia |
| --- | --- | --- | --- |
| Densidad húmeda,t | 2,17 | t/m3 | N° 6 |
| Angulo de fricción, | 35 | grados | N° 6 |
| Cohesión, c | 1,00 | kPa | N° 6 |

**Tabla 6-2.: Propiedades y parámetros Ripios de Lixiviación****

| Parámetro | Valor | Unidad | Referencia |
| --- | --- | --- | --- |
| Densidad húmeda,h | 2,09 | t/m3 | N° 7 |
| Angulo de fricción, | 38 | grados | N° 6 |
| Cohesión, c | 1,00 | kPa | N° 6 |

**Tabla 6-3.: Propiedades y parámetros Interfaz****

| Parámetro | Valor | Unidad | Referencia |
| --- | --- | --- | --- |
| Densidad húmeda,h | 1,00 | t/m3 | N° 6 |
| Angulo de fricción, | 23,0 | grados | N° 6 |
| Cohesión, c | 0,0 | kPa | N° 6 |

**Tabla 6-4.: Parámetros y propiedades Muro de Arena de Relaves****

| Parámetro | Valor | Unidad | Referencia |
| --- | --- | --- | --- |
| Densidad húmeda,h | 2,00 | t/m3 | N° 6 |
| Angulo de fricción, | 33 | grados | N° 6 |
| Cohesión, c | 0,00 | kPa | N° 6 |

**Tabla 6-5.: Parámetros y propiedades Lamas****

| Parámetro | Valor | Unidad | Referencia |
| --- | --- | --- | --- |
| Densidad húmeda,h | 1,40 | t/m3 | N° 6 |
| Angulo de fricción, | 25 | grados | N° 6 |
| Cohesión, c | 0,00 | kPa | N° 6 |

**Tabla 7-1.: Características sismo de diseño considerado****

| Mecanismo de fractura | Costero Interplaca (Thrust) |
| --- | --- |
| Magnitud del sismo de diseño (Ms) | 9,0° |
| Distancia Epicentral (Km) | 195 |
| Profundidad Focal (Km) | 30 |

**Tabla 10-1.: Resultados estabilidad para los distintos perfiles****

| Perfil | Tipo de<br>Falla | Factor de Seguridad | Col4 |
| --- | --- | --- | --- |
| **Perfil** | **Tipo de**<br>**Falla** | **Estático** | **Sísmico** |
| A | Global | - | - |
| B | Global | - | - |
| C | Global | 2,375 | 1,369 |
| D | Global | 2,024 | 1,204 |
| E | Global | 1,950 | 1,178 |
| F | Global | 2,063 | 1,231 |
| G | Global | 2,695 | 1,653 |
| H | Global | 2,290 | 1,358 |
