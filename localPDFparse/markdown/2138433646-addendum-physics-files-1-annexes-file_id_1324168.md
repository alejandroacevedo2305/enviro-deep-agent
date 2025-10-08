---
title: Assessment of PM dry deposition on solar energy harvesting systems: Measurement-model comparison
author: Liza Boyle
date: D:20160305130145+05'30'
language: en
type: academic_paper
pages: 13
has_toc: True
has_tables: False
extraction_quality: high
keywords: [Jian Wang]
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. Background and motivation
  - 2. Methods
  - PM 10 D [m] V [10] 10 [ ¡] ¡ [ 2] 2 [:] : [5] 5 [ C] C [ m] V 2 [2] : [:] 5 [5] ; [3]
  - 3. Results and discussion
  - 4. Conclusions
  - Acknowledgments
  - Funding
  - References
-->

**Aerosol Science and Technology**

**[ISSN: 0278-6826 (Print) 1521-7388 (Online) Journal homepage: http://www.tandfonline.com/loi/uast20](http://www.tandfonline.com/loi/uast20)**

**Assessment of PM dry deposition on solar**
**energy harvesting systems: Measurement-model**
**comparison**

**Liza Boyle, Holly Flinchpaugh & Michael Hannigan**

**To cite this article:** Liza Boyle, Holly Flinchpaugh & Michael Hannigan (2016) Assessment of PM
dry deposition on solar energy harvesting systems: Measurement-model comparison, Aerosol
[Science and Technology, 50:4, 380-391, DOI: 10.1080/02786826.2016.1153797](http://www.tandfonline.com/action/showCitFormats?doi=10.1080/02786826.2016.1153797)

**To link to this article:** [https://doi.org/10.1080/02786826.2016.1153797](https://doi.org/10.1080/02786826.2016.1153797)

Accepted author version posted online: 18
Feb 2016.
Published online: 18 Feb 2016.

[Submit your article to this journal](http://www.tandfonline.com/action/authorSubmission?journalCode=uast20&show=instructions)

Article views: 253

[View related articles](http://www.tandfonline.com/doi/mlt/10.1080/02786826.2016.1153797)

[View Crossmark data](http://crossmark.crossref.org/dialog/?doi=10.1080/02786826.2016.1153797&domain=pdf&date_stamp=2016-02-18)

[Citing articles: 3 View citing articles](http://www.tandfonline.com/doi/citedby/10.1080/02786826.2016.1153797#tabModule)

Full Terms & Conditions of access and use can be found at
[http://www.tandfonline.com/action/journalInformation?journalCode=uast20](http://www.tandfonline.com/action/journalInformation?journalCode=uast20)

AEROSOL SCIENCE AND TECHNOLOGY

2016, VOL. 50, NO. 4, 380-391
[http://dx.doi.org/10.1080/02786826.2016.1153797](http://dx.doi.org/10.1080/02786826.2016.1153797)

Assessment of PM dry deposition on solar energy harvesting systems:

-
Measurement model comparison

Liza Boyle, Holly Flinchpaugh, and Michael Hannigan

Department of Mechanical Engineering, University of Colorado, Boulder, Colorado, USA

ABSTRACT
Soiling of solar energy systems, or the accumulation of particulate matter on their surface, can cause
significant losses in energy conversion efficiency. However, predicting these losses is still not done,
as no methods exist. Field measurements of mass accumulation and airborne PM 10 were conducted
for more than one year at two sites in the Front Range of Colorado with the objective of developing
soiling prediction models. For this study, only dry deposition was examined. The two sites, despite
having different PM 10 concentrations, have indistinguishable average effective deposition velocities
of 2 cm/s, although a large spread in the data was noted. These results are similar to results found in
other deposition studies. The observed effective deposition velocities indicate that coarse particles
are a dominant player in mass accumulation, and sampled airborne size distributions support this
hypothesis. Using a model to calculate dry deposition yielded better agreement with deposition
than a simple average deposition velocity data fit. This model combined with other research and
models can be used for estimating average soiling rates and is most useful over long time scales
especially months to years or longer.

ARTICLE HISTORY
Received 5 August 2015
Accepted 24 January 2016

EDITOR

Jian Wang

# 1. Background and motivation

The number of solar energy installations is growing rapidly
(REN21 2012). This renewable energy has the potential to
significantly reduce emissions from energy generation and
provide electricity in remote and harsh environments.To
improve feasibility assessment for solar energy harvesting,
solar energy harvesting models need to more accurately
predict energy output. These models are improving; however, soiling is still a process that is not well understood
and thus poorly implemented in these models. Soiling, or
the loss of energy from dust or particulate matter (PM)
deposition on the panels, can reduce energy production
significantly. Previous studies have found soiling losses
between less than 1% (Hottel and Woertz 1942) and more
than 88% (Garg 1974), and soiling rates (loss of energy
over time) between 0.1% per day (Garc  ıa et al. 2011) and
5% per day (Sayigh 1978). These large variations in losses
can be attributed to location and meteorology, but generalization in the field has not been done.
Several previous studies have related the mass of
deposited PM with the loss in solar energy. One study
by Hegazy (2001) found a very clear relationship
between the mass of deposited particles and the

transmission reduction, regardless of angle of deployment (Hegazy 2001), which led to the development of
the equation:

Dt D 34:37erf  0:17v [0][:][8473]  ; [1]

where Dt is the transmission loss caused by deposited
particles in percent, and v is the dust deposition density (the mass of dust deposited per square meter) in
g/m [2] . This relationship is shown to be valid between
0 and 10 g/m [2] of accumulated dust, and may apply
to more highly soiled samples. More research is
needed to ensure that the transmission loss is generalizable to other locations, although a previous study
has examined this (Boyle et al. 2015). Using this type
of equation could result in much better predictions of
energy loses due to soiling, but requires an estimate
of the mass of deposited PM.
To understand the fate and transport of atmospheric
PM, particularly those that can potentially impact
human health, climate, or ecosystem health, researchers
have been exploring the deposition process. Previous
studies on deposition have found that for dry deposition
the mass of PM deposited is related to ambient concen

CONTACT Liza Boyle Liza.Boyle@Colorado.edu Department of Mechanical Engineering, University of Colorado, 1111 Engineering Drive, UCB 427,
Boulder, CO 80309, USA.

Color versions of one or more of the figures in the article can be found online at www.tandfonline.com/uast.

© 2016 American Association for Aerosol Research

tration of PM by the dry deposition velocity

m accumulated D v d  PM; [2]

where v d is the deposition velocity, PM is the mass
concentration of PM in the ambient air, and m accumulated
is the mass flux of deposited particles (mass per area per
time). Deposition velocity is affected by wind speed, surface properties, particle size, and a number of other factors that make it difficult to calculate theoretically;
however, it is generally considered a useful tool for
understanding deposition (Seinfeld and Pandis 2006).
Previous ambient studies have shown that larger particles, often over 10 mm in aerodynamic diameter, are
the dominant contributor to deposited mass (Lin et al.
1994). Field and laboratory experiments have found a
wide range of deposition velocities for particles; a snapshot of those studies that focused on larger-size particles
is shown in Table 1. Deposition velocities range from
0.17 cm/s (Davidson et al. 1985) to 21 cm/s (Fang et al.
2014). This large range of deposition velocities is a result
of varying surface geometry, meteorological conditions,
surrounding environment, size of depositing particles,
and atmospheric stability.
Most deposition studies use greased or protected surfaces to prevent particle bounce. However for solar

AEROSOL SCIENCE AND TECHNOLOGY 381

energy applications, where a particle can be resuspended,
it is important to only collect particles that remain
deposited over a long duration. A handful of studies
have considered smooth surfaces, where particle bounce
or resuspension is allowed. A study by Goossens considered dust accumulation on several surfaces and found

good agreement between the mass accumulated on a
glass and metal surface in a wind tunnel (Goossens
2005). The results were also similar to a water surface,
which indicates that geometry is more important than
the surface composition.
Many models have been developed to predict deposition. Models are typically semi-empirical. The model
developed by Zhang et al. (2001) is used in this article
and employs a theoretical framework that separates the
deposition process into several process steps. Each term
that represents a process step is then calculated by a fit
from deposition data. This model has seen good agreement with actual deposition in the past (Zhang et al.
2001).
In this work we examine the deposition of particles on
glass plates similar to those used as photovoltaic (PV)
panel cover plates at two different sites in the Front
Range of Colorado when samples were collected for two
to five weeks. Additionally, we compare the observed
deposition with ambient concentrations and modeled

Table 1. Summary of deposition velocities found in other studies examining coarse particulates.

Deposition
Location surface Orientation Date Deposition velocity Size range Notes Source

New York Greased

microscope
slides

New York Greased

microscope
slides

Placed on 1962- 5 cm/s 20 mm Ragweed pollen Raynor (1974)
ground 1964

Placed on 1962- 12 cm/s 32-35 mm Timothy pollen Raynor (1974)
ground 1964

Champaign, Teflon plate Horizontal and June 0.17-0.42 cm/s All Only sulfate Davidson et al. (1985)
Illinois stationary 1982

Champaign, Petri dish Horizontal and June 0.18-0.61 cm/s All Only sulfate Davidson et al. (1985)
Illinois stationary 1982

South Greased Horizontal July-Sep. 11.7 cm/s >1 mm Noll et al. (1988)
Chicago Mylar wind vane 1986

South Greased Upside-down July-Sep. 4.2 cm/s >1 mm Noll et al. (1988)
Chicago Mylar wind vane 1986

Chicago Greased Horizontal July-Aug. 5.3 cm/s PM 10 Holsen et al. (1993)
area Mylar wind vane 1991

Chicago Greased Horizontal July-Aug. 5.7 cm/s Coarse PM Holsen et al. (1993)
area Mylar wind vane 1991

Around Lake Greased Horizontal Dec. 1993 to 0.2-12 cm/s Coarse PM Metals only Yi et al. (2001)
Michigan Mylar wind vane Oct. 1995

Bursa, Greased Horizontal Oct. 2002 to 2.3-11 cm/s TSP Metals only Tasdemir and
Turkey Mylar wind vane June 2003 Kural (2005)
Taiwan, near Greased Horizontal Sep.-Dec. 2.3-11.7 cm/s TSP Fang et al. (2007)
an Airport Mylar wind vane 2005

Berlin Beaker Horizontal Dec. 2007 to 0.4-1.3 cm/s PM 10 Used Sb as a Langner et al. (2011)
wind vane July 2009 tracer for PM 10

Taiwan, near PVC Horizontal June-Nov. 0.95-7.92 cm/s TSP Fang et al. (2014)
a Harbor wind vane 2013

Taiwan, near PVC Horizontal June-Nov. 1.8-21.4 cm/s TSP Fang et al. (2014)
an Airport wind vane 2013

382 L. BOYLE ET AL.

deposition results. The goal of this work is to collect a
large dataset for evaluating ambient PM concentrations
and dry deposition to improve PV soiling models.

# 2. Methods

## 2.1. General approach

Ambient PM and PM deposition samples were collected
simultaneously at two different locations in the Front
Range of Colorado. Ambient PM was collected using a
dichotomous filter sampler such that particles with aerodynamic diameter between 2.5 and 10 mm (PM 10-2.5 ) are
separated from particles with aerodynamic diameter less
than 2.5 mm (PM 2.5 ). Deposition samples were collected
on glass substrates similar to those used as covers for PV
panels. Additional meteorological data were collected at
both sites by other organizations: the Air Pollution Control Division of the Colorado Department of Public
Health and the Environment (CDPHE) at the Commerce
City site, and the National Oceanic and Atmospheric
Administration (NOAA) at the Erie site.
The first sampling location was in Commerce City,
Colorado, on the roof of a one-storey elementary
school in a mixed industrial and residential area

10 km North of downtown Denver, Colorado. This
site had several notable particulate matter sources
nearby including an open gravel pit mine, and the
intersection of Interstates 25, 76, and 270, and U.S.
Highway 36. This site was co-located with a CDPHE
PM sampling location (AQS ID: 080010006). The second sampling location was in Erie, Colorado, at the
base of the Boulder Atmospheric Observatory tower
in a rural and agricultural area 30 km North of
downtown Denver. This site was surrounded by active
farmland and native grasslands, with one freeway
passing 2 km to the east. More information about
these two sites was presented previously (Boyle et al.
2015).

## 2.2. Airborne particulate matter

Ambient PM 10-2.5 and PM 2.5 were collected using
dichotomous filter samplers located at both field
sites; additionally, the combined PM 10 is examined
in detail here. One of these samplers is shown in the
right side of Figure 1. These filter samplers pulled
50 L/min of air through a PM 10 inlet. This flow is
then passed through a virtual impactor that splits
the flow into a 48 L/min PM 2.5 channel, and a
2 L/m PM 10-2.5 channel. Both flows are then split,
with half going through a Teflon filter (47 mm, 2
mm pore size, Pall Gelman Teflo) and the other half

Figure 1. The experimental setup at the Erie site. On the left is
the deposition setup, and on the right is the dichotomous filter
sampler.

going through a quartz fiber filter (47 mm, Pall Gelman Tissuequartz). Flow rates through each of the
four filters were measured by flow totalizers as well
as being controlled by critical orifices downstream.
These filter samplers are described in more detail
elsewhere (Clements et al. 2014). The filters werechanged every 3 10 days, typically 7 days, at the
Commerce City site and 3-25 days, typically
14 days, at the Erie site to ensure that there were no
flow restrictions caused by pressure drop due to
heavily loaded filters. The filter samplers were run
continuously between filter changings. Additionally,
filters were always changed at the same time as the
deposition plates to ensure that the filters were collecting the same ambient PM that the plates were
exposed to. The Teflon filters were weighed before
and after deployment following the procedures
described previously (Dutton et al. 2009). The Teflon
filters were allowed to equilibrate in a temperature
and relative humidity controlled chamber for 24 h
prior to being weighed at least twice on a LabServe
model BP210D microbalance with an accuracy of 10
mg. If the difference in masses between the first two
weights was more than 30 mg the filter was weighed
a third time, and the mass was taken as the average
of the closest two masses. Before and after deployment, the filters were stored in pre-cleaned petri
dishes (Pall Life Sciences 50mm sterile petri dishes
part number 25388-606) in a freezer ¡18 [] C § 7 [] C.
PM 10 concentrations were found by

# PM 10 D [m] V [10] 10 [ ¡] ¡ [ 2] 2 [:] : [5] 5 [ C] C [ m] V 2 [2] : [:] 5 [5] ; [3]

where m 10 ¡ 2.5 and m 2.5 are the masses of the particles
in the coarse and fine channels, respectively, and
V 10 ¡ 2.5 and V 2.5 are the volumes of air passed through

the coarse and fine channels, respectively. PM 2.5 concentrations are found by

AEROSOL SCIENCE AND TECHNOLOGY 383

the plates to be significantly greater than the noise of the
measurement. The deposition deployment structure is
shown on the left side of Figure 1.
For more than a year of sampling at the Commerce City location deposited PM samples were collected without a roof covering the samples. While in
this time period there was never an entire sampling
period without rain, there were several with minimal,
or rain that occurred very early in the sampling
period. All of the samples without a roof collected
close to or less than the same amount of mass accu
mulated on the covered samples (within measurement
uncertainty when more mass was collected on the
uncovered samples). From this analysis it was determined that the roof was causing a negligible effect on
the dry deposition of particulates, and sampling continued with the roof.

Two types of glass plates were used, one a tempered
glass and one a low iron glass coated with a transparent
conductive oxide; no difference in deposited mass was
observed between the two types of plates (Boyle et al.
2015). The tempered glass samples typically weighed
around 117 g, and the low iron glass samples typically
weighed around 79 g. The plates were thoroughly
cleaned, and stored in cleaned glass petri dishes with aluminum foil covers. The same petri dish was used for preand post-deployment storage. Nitrile gloves were always
worn when handling glass deposition samples to reduce
contamination and care was taken not to disturb the

exposed surfaces of the plates. After deployment samples
were stored in the same freezer as the filters, until they
had been post-weighed.
Masses of samples were found by weighing the samples before and after deployment using the same method
as the Teflon filters. Mass accumulation was found by
subtracting the post masses from the pre masses, correcting for noise in the scale by subtracting the difference in
the simultaneously weighed control samples as described
in previous work (Boyle et al. 2015). The mass accumulation rate was calculated by

_
m accumulated D [m] A [accumulated] plate Dt ; [5]

where _m accumulated is the rate of mass accumulated per
unit surface area, m accumulated is the mass accumulated
on the plate, A plate is the area of the plate, and Dt is the
length of time the plates were deployed. More information on weighing and deposition sample procedure are
presented elsewhere (Boyle et al. 2015).
In this work, an effective deposition velocity is calculated. This is found by rearranging Equation (2), and

PM 2:5 D

## m 2:5 1 C [V] [10] V 2 [¡] :5 [ 2][:][5]

:

: [4]
V 10 ¡ 2:5 C V 2:5

## 1  C [V] [10] V 2 [¡] :5 [ 2][:][5] 

The correction factor in the numerator of Equation (4)
is to account for the fine mass that is deposited on the
coarse filter due to the nature of the virtual impactor.
Analysis of blank samples and controls showed no systematic mass variation, and therefore these masses
were not used for correcting the masses calculated
by Equations (3) and (4). Although both Teflon and
quartz filters were collected, only data from the Teflon
filters are presented here. The quartz samples were collected for analysis of organic material, while Teflon filters were collected for gravimetric analysis and metals
analysis. Chemical analysis, including organic analysis,
has not yet been done and is not presented in this
work, only gravimetric analysis of filters is presented
here.

Airborne particulate samples began being collected in
July of 2012 at the Commerce City site and December of
2012 for the Erie site. Sampling continued until May of
2014 at the Commerce City site, and until March of 2014
at the Erie site.

For examining effects of higher time resolution averaging, hourly PM 10 measurements were used. These data
were collected by the Colorado Department of Public
Health and the Environment (CDPHE) at a monitoring
site in Welby Colorado (AQS ID: 080013001), approximately 1.5 km northwest of the Commerce City site.

## 2.3. Deposited PM and effective deposition velocity

PM deposition samples were collected in the same locations as ambient PM concentrations. Glass samples
10 cm x 10 cm were deployed at 0 [] and 40 [], and a field
blank was carried with each set of plates to observe contamination from handling, transportation, and storage.
A few early samples were deployed at 180 [] at the Commerce City site, but stopped being deployed after it was
found that no appreciable mass accumulation was occurring. The samples were covered by a roof to prevent
effects of precipitation. The roof is to allow for only the
consideration of dry deposition, and not wet deposition.
The roofs were placed 45 cm above the samples to allow
for as much natural air flow as possible without getting
precipitation on the samples. Samples were deployed for
between one and five weeks, with the typical deployment
being two weeks at the Commerce City site and four
weeks at the Erie site. The deployment is longer at the
Erie site to ensure that enough mass has deposited on

384 L. BOYLE ET AL.

using the PM 10 as a surrogate for total airborne PM,

v effective D [m][_] [accumulation] ; [6]
PM 10

where v effective is the effective deposition velocity, and
appropriate unit conversions are added, so that effective
deposition velocity is presented in cm/s in this work.
Since we use PM 10 to represent all the PM, v effective is
biased high.
Sampling of deposited particulates at the Commerce
City site began in August of 2011 and continued to June
of 2014. It was nearly a year later that ambient PM samples began being collected at the Commerce City site,
and effective deposition velocity calculations did not
begin until then. At the Erie site deposited particulate
sampling began in November of 2012 and continued
until May of 2014. During the vast majority of sampling
at the Erie site, both airborne and deposited PM samples
were being collected.

## 2.4. Deposition model

To better understand the utility of deposition theory for
estimating solar panel soiling, we used the PM deposition
model described by Zhang et al. (2001) to compare to the
measured PM deposition rates. This model was chosen
because it has been shown to be effective, its ease of
application, and because it allows for particle bounce.
This model needs ambient PM concentrations including
PM size distribution, surface characteristics, and meteorological parameters as inputs. This model uses the original structure developed by Slinn (1982):

1
v d D v g C R a C R s ; [7]

where v g is the gravitational settling velocity and R a and
R s are the aerodynamic resistance and surface resistance,
respectively. This is a resistance model of deposition,
which examines the processes necessary for deposition
and attempts to quantify them individually. The aerodynamic resistance is calculated as

R a D [lnz] ð [R] [=][z] [0] Þ ¡ C H ; [8]
ku 

where z R is the height at which deposition is being calculated, taken at 5 m here, z 0 is the roughness length, a
value of 1 m was used corresponding to an urban environment, C H is the stability function, k is the Von Karman constant, and u  is the friction velocity. A simplified

stability was used based only on wind speed, where wind
speed above 5 m/s was considered unstable, between
3 m/s and 5 m/s was considered neutral, and below
3 m/s was considered stable. The corresponding stability
functions from Businger et al. (1971) were used. Friction
velocity is calculated by

ð [h] [r] Þ
u  D ~~[k][u]~~ [x] [9]
lnhð r =z 0 Þ [;]

where ~~u~~ x ðh r Þ is the wind speed at the reference height, h r .
The wind speed in this work was collected at 10 m.
The surface resistance is calculated by

1
R s D 3u  Eð B C E IM ÞR 1 ; [10]

where E B and E IM are the collection efficiencies for Brownian diffusion and impaction, respectively, and R 1 is the
percentage of particles that stay deposited on the surface.
All of these factors have empirical fits from data collected
in different experiments. Collection by interception is
not included in the model used here due to the smooth

surface of the solar collector. E B is calculated by

E B D Sc [¡][ g] ; [11]

where Sc is the Schmidt Number, and g is a parameter
based on land use; a value of 0.56 is used here for the
urban environment. E IM is calculated by

E IM D 10 [¡][ 3][=][St] ; [12]

where St is the Stokes number. This is based on a fit for a
smooth collector (Slinn 1982). Finally R 1 is calculated by

R 1 D exp ¡ St [¡][ 1][=][2] ; [13]
 

from Slinn (1982).
Values for PM 10 were obtained from the dichotomous
filter samplers simultaneously deployed at the sites. Values for temperature and wind speed were obtained from
CDPHE at the Commerce City site and NOAA for the
Erie site. The data from CDPHE are hourly averaged,
and for use in modeling these values are averaged again
to correspond to the time that glass coupons were
deployed. Data from NOAA are 1-min averaged; these
data are again averaged to get one value for the time that
corresponding glass coupons were deployed. At the
Commerce City site, this data is publicly available at:
[http://www.colorado.gov/airquality/report. At the Erie](http://www.colorado.gov/airquality/report)
[site, this data is publicly available at: http://www.esrl.](http://www.esrl.noaa.gov/psd/technology/bao/)

[noaa.gov/psd/technology/bao/. In this work we used the](http://www.esrl.noaa.gov/psd/technology/bao/)
fit by Slinn (1982) for the collection efficiency, since the
glass coupons represent a smooth surface. For simplicity
only deposition samples deployed at 0 [] were considered
in comparisons of modeled and experimental mass
accumulation.

## 2.5. Airborne PM size distributions

Airborne size distribution information was collected at

the Commerce City site following the collection of deposition samples. A TSI Aerodynamic Particle Sizer (APS)
Spectrometer (Model 3321) was deployed for a severalweek period in the Spring of 2015 beginning 30th April
and continuing through 21st May. During this time the
weather was especially rainy, with nearly daily rain showers. Because of the consistent rain, the data are likely
skewed slightly from typical size distributions in the
area. Data were not collected for several days during this
time period due to computer failure. Over this time, a
total of 902 size distribution measurements were taken.

Each sample was a 20-s averaged size distribution. Size
distributions were collected and saved every 15 min
while the system was operational. This instrument samples particle sizes from 0.5 mm to 20 mm in diameter by
observing the time of flight of particles in an accelerating
airflow. A lab calibration check of the instrument showed
an uncertainty of 0.1 mm in particle diameter.
The median shape of these size distributions, as well
as the size distributions individually, were used in modeling of particle deposition. When this was done, the size
distribution was scaled to match ambient concentrations

based on the corresponding PM 10 measurement.

# 3. Results and discussion

## 3.1. Deposition

Mass accumulation rate (or deposition) values were collected over more than two years at the Commerce City
site and more than one year at the the Erie site. The time
series of these values is show in in Figure 2. Figure 2 differentiates the two sites as well as the 0 [], 40 [], 180 [], and
field blanks. From this figure, we can see that the Commerce City site (abbreviated CC) in general has higher
mass accumulation rates. Additionally, the 0 [] plates
show higher mass accumulation rates than the 40 [] plates.
The 180 [] plates are nearly indistinguishable from the
field blanks indicating that the main method of deposition is gravitational settling and not diffusion. This is
reasonable as the majority of mass is in larger sizes of
particles that deposit almost exclusively by gravitational
settling. Small particles, which are preferentially removed

AEROSOL SCIENCE AND TECHNOLOGY 385

Figure 2. Plot of mass accumulation on the glass deposition
plates. The samples are grouped by location and orientation to
highlight the differences that location and angle of deployment
have on mass accumulation. Note that only mass accumulations
above zero are shown here, many blank and 180 [] samples have
negative mass accumulation and are not presented in this figure.

via diffusion, may be depositing on the 180 [] plates but
do not have appreciable mass even with significantly longer deployment times (up to two months).
Summary statistics for mass accumulation rates are
shown in Table 2. The highest values were seen in Commerce City where deposition values between 0.01 and
0.12 g/m [2] /day were observed for horizontally deployed
plates, and between 0.01 and 0.08 g/m [2] /day for the 40 []

plates. Lower mass accumulation rates were seen at the
Erie site where deposition values between 0.005 and 0.06
g/m [2] /day for 0 [] plates and 0.005 and 0.02 g/m [2] /day for
40 [] plates were observed. These are similar to results
found by Holsen et al. (1993) outside Chicago, and lower
than those seen by Fang et al. (2007) in Taiwan. This is a
likely indication of the respective concentrations of airborne particulates, since these two studies saw similar
values for deposition velocity (see Table 1).

## 3.2. Effective deposition velocity

Deposition theory indicates that ambient PM concentrations and deposition are related by deposition velocity,
Equation (2). Comparing PM 10 concentrations with
deposition rates yields Figure 3. Despite the wide spread
in the data seen in Figure 3, the range of deposition
velocities that were observed between the two sites were

comparable. At the Commerce City site the range of
effective deposition velocity values was 0.52-5.7 cm/s
(174 samples) with a mean of 2.14 cm/s, and at the Erie
site the range of effective deposition velocity values is
0.61-4.0 cm/s (40 samples) with a mean of 2.12 cm/s.
The results for effective deposition velocity are

386 L. BOYLE ET AL.

Table 2. Summary of mass accumulation data collected in this study.

Mass Effective
accumulation rate deposition velocity

Number Mean (§ STD) Number Mean (§ STD)
Location Position of samples mg/m [2] /day of samples cm/s

Commerce 0 [] 174 43.2 (17.8) 134 2.14 (1.03)
City 40 [] 66 44.3 (15.8) 48 2.42 (1.13)
Erie 0 [] 40 20.0 (11.6) 33 2.12 (1.05)
40 [] 10 13.0 (5.6) 10 1.40 (0.58)

summarized in Table 2. While the range of effective
deposition velocities at the Commerce City site was
slightly larger, the mean effective deposition velocity at
both sites were not statistically significantly different (p
= 0.92). Additionally, the variances of the two distributions are not statistically significantly different (p = 0.86).
There were many more samples collected at the Commerce City site because sampling started earlier at that
location and there were two deposition setups in Commerce City to assess measurement uncertainty (Boyle
et al. 2015), thus doubling the number of samples collected. Additionally, the higher PM concentration allows
samples to be collected more often.
The range in deposition velocities was also compared
for the various deployment angles (0 [], 40 [], 180 [], and
field blanks). A box and whiskers plot of these data are
shown in Figure 4. The median deposition velocity for
both 180 [] samples and the field blanks is near zero, supporting the previous results that significant deposition is
not being caused by diffusion of small particles. The large
spread in the effective deposition velocity values particularly for the 180 [] plates may be caused by compounding

Figure 3. Comparison of ambient PM 10 and mass accumulation
for the two sites in this study. A trend line shows a similar relationship between the two sites, which are statistically not
differentiable.

of uncertainty in PM concentrations as these samples
were deployed longer, and the similar uncertainty in
mass as the field blanks. The 0 [] and 40 [] samples have
very similar deposition velocities, despite the 40 [] samples
having been tilted. This may be due to particles depositing by impaction during wind events, or may be a result
of the uncertainties in mass accumulation and PM 10

concentrations.

These values for effective deposition velocity were
similar to values previously observed, particularly for
those studies that focus on larger particles (see Table 1).
The range of effective deposition velocities seen in this
work spans more than an order of magnitude, which
makes generalization difficult; however, the similarity
between the two sites in this study, and other studies, has
some positive implications. If the similarity in deposition
velocities to smooth horizontal surfaces is minimally
effected by airborne particle distributions, meteorology,
and surrounding environment, than a first-order estimate of mass accumulation on PV panels may be relatively easy, and accomplished with only knowledge of
the relationship with PM 10 concentrations.
When exploring the linear relationship between mass
accumulation on the surface and airborne PM 10

Figure 4. A comparison of the deposition velocities for plates
deployed at different angles. The data from both sites are combined in this box and whiskers plot.

concentrations, PM 10 concentrations accounted for 9%
of the variability in mass accumulation. More of the variability can be accounted for by adding additional variables to this linear model, including temperature and
wind speed. When using all three of these variables, 26%
of the variability can be accounted for. Neither PM 2.5 nor
relative humidity were significant predictors of mass
accumulation. Adding temperature and wind speed does
improve the predictions of mass accumulation; however,
this model has been built and tuned to the data collected

here. Section 3.4 provides a better estimate of mass accumulation with these same variables without tuning to
this specific dataset.
One reason that PM 10 may be a poor predictor of
mass accumulation is that particles larger than 10 mm
in aerodynamic diameter can deposit but are not
counted in the PM 10 measurement. PM 10 can be a
poor predictor of total airborne particulates. This is
likely one of the driving factors in the variability of
the effective deposition velocity and the spread in
Figure 3.

## 3.3. Airborne PM size distributions

Several days of size distribution data are shown in
Figure 5. The frequent rainstorms are easily observable
as the concentrations of coarse particles decrease drastically. There are also periods without rain, where we can
see the quick rise in particle concentrations. The particle concentrations are not very stable, with the size distributions varying widely over even relatively short time
scales (hour to hour for example) especially with the
effects of precipitation. The median size distribution
and interquartile range data show a clear single mode
distribution in coarse particulates, see Figure 6.

Figure 5. Size distributions collected for five days at the Commerce City site in May 2015. Frequent rainstorms are easily noted
by the significantly lower PM concentrations. The APS used in
this study samples particles up to 20 mm in aerodynamic
diameter.

AEROSOL SCIENCE AND TECHNOLOGY 387

Figure 6. Variability in the size distributions collected in Spring of
2015 at the Commerce City site. The histogram is the median size
distribution, and the two dotted lines represent where the 25th
and 75th quartile distributions would be.

Figure 5 shows that the size distribution can be highly
variable with time and that using a single size distribution may not accurately represent the true conditions
over long (in this case multi-week) time scales. Precipitation especially can affect the shape of the size distribution. The peak in coarse PM occurs around 14 mm,
although the variability in this is quite high. Figure 6
shows the median normalized size distribution and the

middle 25-75% quartiles. Size distributions were normalized so that the total mass in each size distribution

was equal to one (the mass in each bin divided by the
total mass in that sample). The median and quartiles are
for each size bin individually across all of the samples
and do not represent specific normalized size distributions, but represent how much of the airborne mass is
typically in each of these bins. The lack of larger particles
in the lower quartile is likely caused by the persistent
precipitation that scavenged the larger particles, and may
not be typical for the Front Range area. Figure 6 also
indicates that there are likely larger particles that were
not sampled by the APS, as seen by the shape of the
distribution.

To use these size distribution data in modeling deposition, the median size distribution was used as timeaveraged size distribution of the particles, and the
median size distribution was shown to match deposition
results better than the mean size distribution. This was

shown by running a comparison between deposition calculated every hour and every two weeks. Hourly averaged meteorological data were combined with
bootstrapped size distributions to calculate a theoretical
deposition for every hour over two weeks. This hourly
deposition was summed and compared with the

388 L. BOYLE ET AL.

deposition calculated using two-week averaged meteorological data, combined with mean and median size distributions. Using this method with several years of
meteorological data, the median size distribution was
shown to better predict the hourly summed size deposition results than the mean size distribution. The PM 10
concentration that was collected with the dichotomous
filter sampler was used as a scalar to multiply the normalized size distribution to get an average size distribution for the period of deployment of the plates.

## 3.4. Comparison between observations and model

Figure 7b shows the comparison between actual mass
accumulation and modeled mass deposition, using the
model developed by Zhang and collaborators (see Section 2.4) and using the median size distribution collected
with the APS. These data have an R [2] value of 0.32, and
smaller spread than the PM 10 versus mass accumulation
plot (Figure 3) (p = 0.46). This indicates that this model
does a better job of estimating mass accumulation than
employing a single effective deposition velocity. The
model does a good job of getting the right order of magnitude fit to the data and a regression of the data forced
through the origin gives a slope of 1. Although the model
makes a good first-order approximation of deposition,
there is still noticeable spread in the data of 0.018 g/m [2] /
day.

Figure 7a shows the results of the same model as
above but instead of using 52 size bins corresponding to
the size bins of the APS, the model uses only two size
bins one for PM 2.5 and one for PM 10-2.5 . This model
does almost as well as the model with 52 size bins
(R [2] = 0.31), with less information. Not only is this likely

the better model tested in this study, but also it shows
that the same accuracy can be achieved with relatively
rudimentary ambient size distribution information, as
with a more specific size distribution. Both PM 10 and
PM 2.5 data are widely available in the US through the
Environmental Protection Agency, and this model could
easily be applied with this level of accuracy in many locations across the US.

Figure 7 shows similar magnitudes for results of both
the 2-bin and 52-bin models, despite the 52-bin model
including particles between 10 and 20 mm in diameter
that are not included in the 2-bin model. This is most

likely due to both models using the same mass of particles, just distributed between the bins differently. The
52-bin model has larger particles, but the total particle
mass is still the same, so the model finds less deposition
of the smaller particles. Additionally, the 2-bin model
uses simultaneously collected PM 2.5 and PM 10, so that
more or fewer smaller particles may be represented in
the model--compared with the 52-bin model that has
one constant size distribution.

Previous research has found that long time-averages
for deposition significantly reduce the accuracy of model
results and the relationship between ambient PM and
deposition (Noll and Fang 1989). In an attempt to
understand if this is a driver for the spread between
modeled and predicted results, a theoretical study was
conducted. Real hourly PM 10, temperature, and wind
speed data from the CDPHE were used to model deposition every hour over two week increments. Additionally,
the size distributions collected with the APS were boot
straped for these hourly calculations, choosing one size
distribution at random for every hour. Then the median
size distribution from the bootstrap population and the

Figure 7. Comparison of mass accumulation and modeled mass deposition for the Commerce City site. Particulate concentrations were
collected from the dichotomous filter sampler, and meteorological data averaged over the glass coupon deployment from data available
from the CDPHE. Plot (a) shows the model using size bins corresponding to the APS size bins, and plot (b) shows results using a simple
2-bin model with the PM 10-2.5 and PM 2.5 collected from the dichotomous filter sampler.

AEROSOL SCIENCE AND TECHNOLOGY 389

Table 3. Summary of deposition model sensitivities given as the average percentage change in mass of particle dry deposition. Mean
values for the range of input found in this experiment as well as the range of values observed are presented.

Increase 10% Increase 5% Decrease 5% Decrease 10%
Mean (Range) % Mean (Range) % Mean (Range) % Mean (Range) %

Wind speed 0.8 (¡3.8 to 4.8) 0.2 (¡2.6 to 2.7) ¡1.3 (¡3.3 to 2.0) ¡3.0 (¡7.2 to 4.7)
Temperature 1.7 (¡3.0 to 5.7) 1.0 (¡1.4 to 2.9) ¡1.1 (¡2.9 to 1.1) ¡2.4 (¡5.7 to 1.8)
Particle size 1.60 (¡1.9 to 6.0) 0.80 (¡1.2 to 3.1) ¡0.90 (¡3.5 to 1.7) ¡2.10 (¡7.4 to 3.9)
PM 10 10 (10 to 10) 5 (5 to 5) ¡5 (¡5 to ¡5) ¡10 (¡10 to ¡10)

averaged PM 10, temperature, and wind speed data were
used to calculate total deposition over the two week
period and the deposition results were compared. The
spread in the results was 0.005 g/m [2] /day. As such, high
time averaging was not able to fully explain the differences observed between modeled and observed deposition
results in this experiment.
Another possible explanation for the spread is in the
measurement uncertainty in calculating mass accumulation, caused by uncertainty in mass, time, and area measurements. This uncertainty has previously been shown to
be on the order of 0.01 g/m [2] /day (Boyle et al. 2015).
The uncertainty caused by lower time resolution and
measurement uncertainty accounts for roughly twothirds of the difference between modeled and observed

deposition. The remainder of the unexplained variance
likely originates from model ”inaccuracies” or inability
of the model to fully capture real world deposition processes, meteorological variable uncertainties that are not
examined here, and size distribution uncertainties.
Another likely source of uncertainty in this approach is
not accounting for particulates larger than 10 or 20 mm
in aerodynamic diameter. These larger particles are in
the atmosphere and depositing, but are not being
included in the measurements of airborne particulates or
the calculations of deposition. Previous experiments on
solar energy systems have seen a peak in deposited size
distributions around 20 mm (Roth and Anaya 1980; Biryukov 1996; Cabanillas and Mungu  ıa 2011), indicating
that these larger particles are present and significant.
A sensitivity analysis of the model was conducted,
examining the sensitivity to temperature, wind speed,
PM 10, and particle size (increasing or decreasing the size
of each particle by the given percentage). For each
parameter, the other parameters were kept constant
while the parameter of interest was increased and
decreased by 5 and 10% for all the samples in the dataset.
The numerical output from this sensitivity analysis is
shown in Table 3. The model was found to be most sen
sitive to PM 10, with any change in the input of PM concentration giving an equal percent change in the output.
All the other parameters were less sensitive. Temperature
and particle size had similar sensitivities, with every percent change in the input in these parameters causing a

0.2% change in the modeled mass accumulation with
wide variability across the input parameter space noted.
Finally, wind speed was the most variably sensitive
parameter with every percent increase in wind speed
causing a 0.06% increase in mass accumulation and every
percent decrease in wind speed causing a 0.3% decrease
in mass accumulation, and wide spread in this relationship was again noted across the input parameter space.

# 4. Conclusions

An average effective deposition velocity of 2 cm/s was
observed at both sites in this study but an order of magnitude spread is observed in effective deposition velocity
over the entire sampling campaign. A more complex
model did a better job of predicting mass deposition but
required temperature, wind speed, and size distribution
data. All methods showed significant spread in the deposition results when compared with experimental deposition; however, these results represent a significant step
forward in modeling soiling losses for solar energy.
Because soiling happens over long time scales (months
to years), an average effective deposition velocity is useful
even if there is high variability on shorter time scales. For
solar energy harvesting modeling, short-term variability
is driven by clouds and temperature, which dominate
any effects that might be seen from soiling. However,
monthly and yearly output of a system can be greatly
affected by soiling, and being able to predict these losses
can significantly improve estimates of how much energy
a PV system will produce over its lifetime, which dictates
the payback period. The accuracy in predicting deposition achieved in this study is likely not useful for understanding short-term fate of airborne species, or high
precision calculations of deposition.
Being able to predict mass accumulation on PV panels, or other solar energy harvesting devices, could
improve prediction of energy loss due to soiling when
paired with other study results and models. Here results
are presented that indicate that mass deposition is related
to ambient concentrations, even over periods of time
greater than a week. This means that using readily available PM 10 data, and easily implemented deposition models, even as simple as a constant effective deposition

390 L. BOYLE ET AL.

velocity, soiling losses could begin to be predicted at sites
anywhere in the country or the world. Both the simple
and more complex model are sensitive to PM 10 concentration inputs, and high-quality data for this parameter
are necessary for accurately predicting mass accumulation. The more complex model was less sensitive to wind
speed, temperature, and particle sizes indicating that
lower quality data (from more distant stations, or with
higher uncertainty) may be used in these parameters.

# Acknowledgments

The authors thank the Air Pollution Control Division of the
Colorado Department of Public Health and the Environment
for generously sharing data, especially Bradley Rink for his
continued help with data from CDPHE. Additionally, the
authors thank the Physical Sciences Division of the National
Oceanic and Atmospheric Administration for sharing data collected at the BAO Tower, and Daniel Wolfe and Bruce Bartram
for their support with sampling and instrument monitoring at
the BAO Tower.

# Funding

This material is based upon the work supported by the
National Science Foundation Graduate Research Fellowship
Program under Grant No. DGE 1144083.

# References

Biryukov, S. A. (1996). Degradation of Optical Properties of
Solar Collectors Due to the Ambient Dust Deposition as a
Function of Particle Size. J. Aerosol Sci., 27(Suppl 1):S37S38.
Boyle, L., Flinchpaugh, H., and Hannigan, M. P. (2015). Natural Soiling of Photovoltaic Cover Plates and the Impact on
Transmission. Renew. Energ., 77:166-173.
Businger, J. A., Wyngaard, J. C., Izumi, Y., and Bradley, E. F.
(1971). Flux-Profile Relationships in the Atmospheric Surface Layer. J. Atmos. Sci., 28(2):181-189.
Cabanillas, R. E., and Mungu  ıa, H. (2011). Dust Accumulation
Effect on Efficiency of Si Photovoltaic Modules. J. Renew.
Sustain. Energ., 3(4):043114.
Clements, N., Eav, J., Xie, M., Hannigan, M. P., Miller, S. L.,
Navidi, W., Peel, J. L., Schauer, J. J., Shafer, M. M., and Milford, J. B. (2014). Concentrations and Source Insights for
Trace Elements in Fine and Coarse Particulate Matter.

Atmos. Environ., 89:373-381.
Davidson, C. I., Lindberg, S. E., Schmidt, J. A., Cartwright, L.
G., and Landis, L. R. (1985). Dry Deposition of Sulfate ontoSurrogate Surfaces. J. Geophys. Res.: Atmos., 90(D1):2123
2130.
Dutton, S. J., Schauer, J. J., Vedal, S., and Hannigan, M. P.
(2009). PM2.5 Characterization for Time Series Studies:
Pointwise Uncertainty Estimation and Bulk Speciation
Methods Applied in Denver. Atmos. Environ., 43(5):
1136-1146.

Fang, G.-C., Chiang, H.-C., Chen, Y.-C., Xiao, Y.-F., and
Zhuang, Y.-J. (2014). Particulates and Metallic Elements
Monitoring at Two Sampling Sites (Harbor, Airport) in Taiwan. Environ. Forens., 15(4):296-305.
Fang, G.-C., Wu, Y.-S., Lee, W.-J., Chou, T.-Y., and Lin, I.-C.
(2007). Ambient Air Particulates, Metallic Elements, Dry
Deposition and Concentrations at Taichung Airport, Taiwan. Atmos. Res., 84(3):280-289.
Garc  ıa, M., Marroyo, L., Lorenzo, E., and P  erez, M. (2011).
Soiling and Other Optical Losses in Solar-Tracking PV
Plants in Navarra. Prog. Photovolt. Res. Appl., 19(2):211217.
Garg, H. (1974). Effect of Dirt on Transparent Covers in
Flat-Plate Solar Energy Collectors. Solar Energ., 15
(4):299-302.
Goossens, D. (2005). Quantification of the Dry Aeolian Deposition of Dust on Horizontal Surfaces: An Experimental
Comparison of Theory and Measurements. Sedimentology,
52(4):859-873.
Hegazy, A. A. (2001). Effect of Dust Accumulation on Solar
Transmittance through Glass Covers of Plate-Type Collectors. Renew. Energ., 22(4):525-540.
Holsen, T. M., Noll, K. E., Fang, G. C., Lee, W. J., Lin, J.
M., and Keeler, G. J. (1993). Dry Deposition and Particle Size Distributions Measured during the Lake Michigan Urban Air Toxics Study. Environ. Sci. Technol., 27
(7):1327-1333.
Hottel, H., and Woertz, B. (1942). Performance of Flat-Plate
Solar-Heat Collectors. Trans. ASME, 64:91-104.
Langner, M., Kull, M., and Endlicher, W. R. (2011). Determination of PM10 Deposition Based on Antimony Flux to
Selected Urban Surfaces. Environ. Pollut., 159(8-9):20282034.
Lin, J. J., Noll, K. E., and Holsen, T. M. (1994). Dry Deposition Velocities as a Function of Particle Size in the
Ambient Atmosphere. Aerosol Sci. Technol., 20(3):
239-252.
Noll, K. E., and Fang, K. Y. P. (1989). Development of a Dry
Deposition Model for Atmospheric Coarse Particles. Atmos.
Environ. (1967), 23(3):585-594.
Noll, K. E., Fang, K. Y. P., and Watkins, L. A. (1988). Characterization of the Deposition of Particles from the Atmosphere to a Flat Plate. Atmos. Environ. (1967), 22(7):1461
1468.
Raynor, G. S. (1974). Experimental Studies of Pollen Deposition to Vegetated Surfaces. In Atmosphere-Surface
Exchange of Particulate and Gaseous Pollutants, UN
Food and Agriculture Organization, Richland, WA, pp.
264-279.
REN21 (2012). Renewables 2012: Global Status Report. Renewable Energy Policy Network for the 21st Century (REN21),
Paris.
Roth, E. P., and Anaya, A. J. (1980). The Effect of Natural
Soiling and Cleaning on the Size Distribution of Particles Deposited on Glass Mirrors. J. Solar Energ. Eng.,
102(4):248.
Sayigh, A. A. M. (1978). Effect of Dust on Flat Plate Collectors,
in Sun, Mankind’s Future Source of Energy: Proceedings of
the International Solar Energy Congress, New Delhi, India,
January 16-21, 1978, volume 2. Pergamon Press, Elmsford,
NY, pp. 960-964.

Seinfeld, J. H., and Pandis, S. N. (2006). Atmospheric Chemistry
and Physics: From Air Pollution to Climate Change. 2nd ed.
Wiley Interscience, Hoboken, NJ.
Slinn, W. G. N. (1982). Predictions for Particle Deposition to Vegetative Canopies. Atmos. Environ. (1967), 16(7):1785-1794.
Tasdemir, Y., and Kural, C. (2005). Atmospheric Dry Deposition Fluxes of Trace Elements Measured in Bursa, Turkey.
Environ. Pollut., 138(3):462-472.

AEROSOL SCIENCE AND TECHNOLOGY 391

Yi, S.-M., Shahin, U., Sivadechathep, J., Sofuoglu, S. C., and
Holsen, T. M. (2001). Overall Elemental Dry Deposition
Velocities Measured around Lake Michigan. Atmos. Environ., 35(6):1133-1140.
Zhang, L., Gong, S., Padro, J., and Barrie, L. (2001). A SizeSegregated Particle Dry Deposition Scheme for an
Atmospheric Aerosol Module. Atmos. Environ., 35
(3):549-560.