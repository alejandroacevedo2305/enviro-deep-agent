---
title: Sin título
author: Desconocido
date: D:20190801164253
language: en
type: general
pages: 9
has_toc: False
has_tables: True
extraction_quality: high
---

|INPUT GROUP: 0 -- Input and Output File Names|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|PUFLST|CALPUFF output list file (CALPUFF.LST)|CALPUFF.LST|
|CONDAT|CALPUFF output concentration file (CONC.DAT)|CONC.DAT|
|DFDAT|CALPUFF output dry deposition flux file (DFLX.DAT)|DFLX.DAT|
|WFDAT|CALPUFF output wet deposition flux file (WFLX.DAT)|WFLX.DAT|
|LCFILES|Lower case file names (T = lower case, F = upper case)|F|
|NMETDOM|Number of CALMET.DAT domains|1|
|NMETDAT|Number of CALMET.DAT input files|4|
|NPTDAT|Number of PTEMARB.DAT input files|0|
|NARDAT|Number of BAEMARB.DAT input files|0|
|NVOLDAT|Number of VOLEMARB.DAT input files|0|
|NFLDAT|Number of FLEMARB.DAT input files|0|
|NRDDAT|Number of RDEMARB.DAT input files|0|
|NLNDAT|Number of LNEMARB.DAT input files|0|
|METDAT|CALMET gridded meteorological data file (CALMET.DAT)|CALMET_2017-12-3<br>1-00-0000-2018-04-0<br>2-00-0000.DAT|
|METDAT|CALMET gridded meteorological data file (CALMET.DAT)|CALMET_2018-04-0<br>2-00-0000-2018-07-0<br>2-00-0000.DAT|
|METDAT|CALMET gridded meteorological data file (CALMET.DAT)|CALMET_2018-07-0<br>2-00-0000-2018-10-0<br>2-00-0000.DAT|
|METDAT|CALMET gridded meteorological data file (CALMET.DAT)|CALMET_2018-10-0<br>2-00-0000-2019-01-0<br>1-20-0000.DAT|

|INPUT GROUP: 1 -- General Run Control Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|METRUN|Run all periods in met data file? (0 = no, 1 = yes)|0|
|IBYR|Starting year|2017|
|IBMO|Starting month|12|
|IBDY|Starting day|31|
|IBHR|Starting hour|0|
|IBMIN|Starting minute|0|
|IBSEC|Starting second|0|
|IEYR|Ending year|2019|
|IEMO|Ending month|1|
|IEDY|Ending day|1|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 1 of 9

|INPUT GROUP: 1 -- General Run Control Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|IEHR|Ending hour|19|
|IEMIN|Ending minute|0|
|IESEC|Ending second|0|
|ABTZ|Base time zone|UTC-0400|
|NSECDT|Length of modeling time-step (seconds)|3600|
|NSPEC|Number of chemical species modeled|4|
|NSE|Number of chemical species to be emitted|4|
|ITEST|Stop run after SETUP phase (1 = stop, 2 = run)|2|
|MRESTART|Control option to read and/or write model restart data|0|
|NRESPD|Number of periods in restart output cycle|0|
|METFM|Meteorological data format (1 = CALMET, 2 = ISC, 3 = AUSPLUME, 4 =<br>CTDM, 5 = AERMET)|1|
|MPRFFM|Meteorological profile data format (1 = CTDM, 2 = AERMET)|1|
|AVET|Averaging time (minutes)|60|
|PGTIME|PG Averaging time (minutes)|60|
|IOUTU|Output units for binary output files (1 = mass, 2 = odour, 3 = radiation)|1|

|INPUT GROUP: 2 -- Technical Options|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|MGAUSS|Near field vertical distribution (0 = uniform, 1 = Gaussian)|1|
|MCTADJ|Terrain adjustment method (0 = none, 1 = ISC-type, 2 = CALPUFF-type, 3<br>= partial plume path)|3|
|MCTSG|Model subgrid-scale complex terrain? (0 = no, 1 = yes)|0|
|MSLUG|Near-field puffs modeled as elongated slugs? (0 = no, 1 = yes)|0|
|MTRANS|Model transitional plume rise? (0 = no, 1 = yes)|1|
|MTIP|Apply stack tip downwash to point sources? (0 = no, 1 = yes)|1|
|MRISE|Plume rise module for point sources (1 = Briggs, 2 = numerical)|1|
|MTIP_FL|Apply stack tip downwash to flare sources? (0 = no, 1 = yes)|0|
|MRISE_FL|Plume rise module for flare sources (1 = Briggs, 2 = numerical)|2|
|MBDW|Building downwash method (1 = ISC, 2 = PRIME)|1|
|MSHEAR|Treat vertical wind shear? (0 = no, 1 = yes)|0|
|MSPLIT|Puff splitting allowed? (0 = no, 1 = yes)|0|
|MCHEM|Chemical transformation method (0 = not modeled, 1 = MESOPUFF II, 2 =<br>User-specified, 3 = RIVAD/ARM3, 4 = MESOPUFF II for OH, 5 = half-life, 6<br>= RIVAD w/ISORROPIA, 7 = RIVAD w/ISORROPIA CalTech SOA)|0|
|MAQCHEM|Model aqueous phase transformation? (0 = no, 1 = yes)|0|
|MLWC|Liquid water content flag|1|
|MWET|Model wet removal? (0 = no, 1 = yes)|1|
|MDRY|Model dry deposition? (0 = no, 1 = yes)|1|
|MTILT|Model gravitational settling (plume tilt)? (0 = no, 1 = yes)|0|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 2 of 9

|INPUT GROUP: 2 -- Technical Options|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|MDISP|Dispersion coefficient calculation method (1= PROFILE.DAT, 2 = Internally,<br>3 = PG/MP, 4 = MESOPUFF II, 5 = CTDM)|3|
|MTURBVW|Turbulence characterization method (only if MDISP = 1 or 5)|3|
|MDISP2|Missing dispersion coefficients method (only if MDISP = 1 or 5)|3|
|MTAULY|Sigma-y Lagrangian timescale method|0|
|MTAUADV|Advective-decay timescale for turbulence (seconds)|0|
|MCTURB|Turbulence method (1 = CALPUFF, 2 = AERMOD)|1|
|MROUGH|PG sigma-y and sigma-z surface roughness adjustment? (0 = no, 1 = yes)|0|
|MPARTL|Model partial plume penetration for point sources? (0 = no, 1 = yes)<br>|1|
|MPARTLBA|~~Model partial plume penetration for buoyant area sources? (0 = no, 1 =~~<br>|0|
|MTINV|~~yes)~~<br>Strength of temperature inversion provided in PROFILE.DAT? (0 = no -<br>compute from default gradients, 1 = yes)|0|
|MPDF|PDF used for dispersion under convective conditions? (0 = no, 1 = yes)|0|
|MSGTIBL|Sub-grid TIBL module for shoreline? (0 = no, 1 = yes)|0|
|MBCON|Boundary conditions modeled? (0 = no, 1 = use BCON.DAT, 2 = use<br>CONC.DAT)|0|
|MSOURCE|Save individual source contributions? (0 = no, 1 = yes)|0|
|MFOG|Enable FOG model output? (0 = no, 1 = yes - PLUME mode, 2 = yes -<br>RECEPTOR mode)|0|
|MREG|Regulatory checks (0 = no checks, 1 = USE PA LRT checks)|0|

|INPUT GROUP: 3 -- Species List|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|CSPEC|Species included in model run|PM10|
|CSPEC|Species included in model run|PM2.5|
|CSPEC|Species included in model run|CO|
|CSPEC|Species included in model run|NOX|

|INPUT GROUP: 4 -- Map Projection and Grid Control Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|PMAP|Map projection system|UTM|
|FEAST|False easting at projection origin (km)|0.0|
|FNORTH|False northing at projection origin (km)|0.0|
|IUTMZN|UTM zone (1 to 60)|19|
|UTMHEM|Hemisphere (N = northern, S = southern)|S|
|RLAT0|Latitude of projection origin (decimal degrees)|0.00N|
|RLON0|Longitude of projection origin (decimal degrees)|0.00E|
|XLAT1|1st standard parallel latitude (decimal degrees)|30S|
|XLAT2|2nd standard parallel latitude (decimal degrees)|60S|
|DATUM|Datum-region for the coordinates|WGS-84|
|NX|Meteorological grid - number of X grid cells|30|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 3 of 9

|INPUT GROUP: 4 -- Map Projection and Grid Control Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NY|Meteorological grid - number of Y grid cells|30|
|NZ|Meteorological grid - number of vertical layers|10|
|DGRIDKM|Meteorological grid spacing (km)|1|
|ZFACE|Meteorological grid - vertical cell face heights (m)|0.0, 20.0, 40.0, 80.0,<br>160.0, 320.0, 640.0,<br>1200.0, 2000.0,<br>3000.0, 4000.0|
|XORIGKM|Meteorological grid - X coordinate for SW corner (km)|342.9720|
|YORIGKM|Meteorological grid - Y coordinate for SW corner (km)|6196.5340|
|IBCOMP|Computational grid - X index of lower left corner|1|
|JBCOMP|Computational grid - Y index of lower left corner|1|
|IECOMP|Computational grid - X index of upper right corner|30|
|JECOMP|Computational grid - Y index of upper right corner|30|
|LSAMP|Use sampling grid (gridded receptors) (T = true, F = false)|T|
|IBSAMP|Sampling grid - X index of lower left corner|1|
|JBSAMP|Sampling grid - Y index of lower left corner|1|
|IESAMP|Sampling grid - X index of upper right corner|30|
|JESAMP|Sampling grid - Y index of upper right corner|30|
|MESHDN|Sampling grid - nesting factor|1|

|INPUT GROUP: 5 -- Output Options|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|ICON|Output concentrations to CONC.DAT? (0 = no, 1 = yes)|1|
|IDRY|Output dry deposition fluxes to DFLX.DAT? (0 = no, 1 = yes)|1|
|IWET|Output wet deposition fluxes to WFLX.DAT? (0 = no, 1 = yes)|1|
|IT2D|Output 2D temperature data? (0 = no, 1 = yes)|0|
|IRHO|Output 2D density data? (0 = no, 1 = yes)|0|
|IVIS|Output relative humidity data? (0 = no, 1 = yes)|0|
|LCOMPRS|Use data compression in output file (T = true, F = false)|T|
|IQAPLOT|Create QA output files suitable for plotting? (0 = no, 1 = yes)|1|
|IPFTRAK|Output puff tracking data? (0 = no, 1 = yes use timestep, 2 = yes use<br>sampling step)|0|
|IMFLX|Output mass flux across specific boundaries? (0 = no, 1 = yes)|0|
|IMBAL|Output mass balance for each species? (0 = no, 1 = yes)|0|
|INRISE|Output plume rise data? (0 = no, 1 = yes)|0|
|ICPRT|Print concentrations? (0 = no, 1 = yes)|0|
|IDPRT|Print dry deposition fluxes? (0 = no, 1 = yes)|0|
|IWPRT|Print wet deposition fluxes? (0 = no, 1 = yes)|0|
|ICFRQ|Concentration print interval (timesteps)|1|
|IDFRQ|Dry deposition flux print interval (timesteps)|1|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 4 of 9

|INPUT GROUP: 5 -- Output Options|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|IWFRQ|Wet deposition flux print interval (timesteps)|1|
|IPRTU|Units for line printer output (e.g., 3 = ug/m**3 - ug/m**2/s, 5 = odor units)|3|
|IMESG|Message tracking run progress on screen (0 = no, 1 and 2 = yes)|2|
|LDEBUG|Enable debug output? (0 = no, 1 = yes)|F|
|IPFDEB|First puff to track in debug output|1|
|NPFDEB|Number of puffs to track in debug output|1000|
|NN1|Starting meteorological period in debug output|1|
|NN2|Ending meteorological period in debug output|10|

|INPUT GROUP: 6 -- Subgrid Scale Complex Terrain Inputs|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NHILL|Number of terrain features|0|
|NCTREC|Number of special complex terrain receptors|0|
|MHILL|Terrain and CTSG receptor data format (1= CTDM, 2 = OPTHILL)|2|
|XHILL2M|Horizontal dimension conversion factor to meters|1.0|
|ZHILL2M|Vertical dimension conversion factor to meters|1.0|
|XCTDMKM|X origin of CTDM system relative to CALPUFF system (km)|0.0|
|YCTDMKM|Y origin of CTDM system relative to CALPUFF system (km)|0.0|

|INPUT GROUP: 9 -- Miscellaneous Dry Deposition Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|RCUTR|Reference cuticle resistance (s/cm)|30|
|RGR|Reference ground resistance (s/cm)|10|
|REACTR|Reference pollutant reactivity|8|
|NINT|Number of particle size intervals for effective particle deposition velocity|9|
|IVEG|Vegetation state in unirrigated areas (1 = active and unstressed, 2 = active<br>and stressed, 3 = inactive)|1|

|INPUT GROUP: 11 -- Chemistry Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|MOZ|Ozone background input option (0 = monthly, 1 = hourly from OZONE.DAT)|1|
|BCKO3|Monthly ozone concentrations (ppb)|80.00, 80.00, 80.00,<br>80.00, 80.00, 80.00,<br>80.00, 80.00, 80.00,<br>80.00, 80.00, 80.00|
|MNH3|Ammonia background input option (0 = monthly, 1 = from NH3Z.DAT)|0|
|MAVGNH3|Ammonia vertical averaging option (0 = no average, 1 = average over<br>vertical extent of puff)|1|
|BCKNH3|Monthly ammonia concentrations (ppb)|10.00, 10.00, 10.00,<br>10.00, 10.00, 10.00,<br>10.00, 10.00, 10.00,<br>10.00, 10.00, 10.00|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 5 of 9

|INPUT GROUP: 11 -- Chemistry Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|RNITE1|Nighttime SO2 loss rate (%/hr)|0.2|
|RNITE2|Nighttime NOx loss rate (%/hr)|2|
|RNITE3|Nighttime HNO3 loss rate (%/hr)|2|
|MH2O2|H2O2 background input option (0 = monthly, 1 = hourly from H2O2.DAT)|1|
|BCKH2O2|Monthly H2O2 concentrations (ppb)|1.00, 1.00, 1.00, 1.00,<br>1.00, 1.00, 1.00, 1.00,<br>1.00, 1.00, 1.00, 1.00|
|RH_ISRP|Minimum relative humidity for ISORROPIA|50.0|
|SO4_ISRP|Minimum SO4 for ISORROPIA|0.4|
|BCKPMF|SOA background fine particulate (ug/m**3)|1.00, 1.00, 1.00, 1.00,<br>1.00, 1.00, 1.00, 1.00,<br>1.00, 1.00, 1.00, 1.00|
|OFRAC|SOA organic fine particulate fraction|0.15, 0.15, 0.20, 0.20,<br>0.20, 0.20, 0.20, 0.20,<br>0.20, 0.20, 0.20, 0.15|
|VCNX|SOA VOC/NOX ratio|50.00, 50.00, 50.00,<br>50.00, 50.00, 50.00,<br>50.00, 50.00, 50.00,<br>50.00, 50.00, 50.00|
|NDECAY|Half-life decay blocks|0|

|INPUT GROUP: 12 -- Misc. Dispersion and Computational Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|SYTDEP|Horizontal puff size for time-dependent sigma equations (m)|550|
|MHFTSZ|Use Heffter equation for sigma-z? (0 = no, 1 = yes)|0|
|JSUP|PG stability class above mixed layer|5|
|CONK1|Vertical dispersion constant - stable conditions|0.01|
|CONK2|Vertical dispersion constant - neutral/unstable conditions|0.1|
|TBD|Downwash scheme transition point option (<0 = Huber-Snyder, 1.5 =<br>Schulman-Scire, 0.5 = ISC)|0.5|
|IURB1|Beginning land use category for which urban dispersion is assumed|10|
|IURB2|Ending land use category for which urban dispersion is assumed|19|
|ILANDUIN|Land use category for modeling domain|20|
|Z0IN|Roughness length for modeling domain (m)|.25|
|XLAIIN|Leaf area index for modeling domain|3.0|
|ELEVIN|Elevation above sea level (m)|.0|
|XLATIN|Meteorological station latitude (deg)|-999.0|
|XLONIN|Meteorological station longitude (deg)|-999.0|
|ANEMHT|Anemometer height (m)|10.0|
|ISIGMAV|Lateral turbulence format (0 = read sigma-theta, 1 = read sigma-v)|1|
|IMIXCTDM|Mixing heights read option (0 = predicted, 1 = observed)|0|
|XMXLEN|Slug length (met grid units)|1|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 6 of 9

|INPUT GROUP: 12 -- Misc. Dispersion and Computational Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|XSAMLEN|Maximum travel distance of a puff/slug (met grid units)|1|
|MXNEW|Maximum number of slugs/puffs release from one source during one time<br>step|99|
|MXSAM|Maximum number of sampling steps for one puff/slug during one time step|99|
|NCOUNT|Number of iterations used when computing the transport wind for a<br>sampling step that includes gradual rise|2|
|SYMIN|Minimum sigma-y for a new puff/slug (m)|1|
|SZMIN|Minimum sigma-z for a new puff/slug (m)|1|
|SZCAP_M|Maximum sigma-z allowed to avoid numerical problem in calculating virtual<br>time or distance (m)|5000000|
|SVMIN|Minimum turbulence velocities sigma-v (m/s)|0.5, 0.5, 0.5, 0.5, 0.5,<br>0.5, 0.37, 0.37, 0.37,<br>0.37, 0.37, 0.37|
|SWMIN|Minimum turbulence velocities sigma-w (m/s)|0.2, 0.12, 0.08, 0.06,<br>0.03, 0.016, 0.2, 0.12,<br>0.08, 0.06, 0.03,<br>0.016|
|CDIV|Divergence criterion for dw/dz across puff (1/s)|0, 0|
|NLUTIBL|TIBL module search radius (met grid cells)|4|
|WSCALM|Minimum wind speed allowed for non-calm conditions (m/s)|0.5|
|XMAXZI|Maximum mixing height (m)|3000|
|XMINZI|Minimum mixing height (m)|50|
|TKCAT|Emissions scale-factors temperature categories (K)|265., 270., 275., 280.,<br>285., 290., 295., 300.,<br>305., 310., 315.|
|PLX0|Wind speed profile exponent for stability classes 1 to 6|0.07, 0.07, 0.1, 0.15,<br>0.35, 0.55|
|PTG0|Potential temperature gradient for stable classes E and F (deg K/m)|0.02, 0.035|
|PPC|Plume path coefficient for stability classes 1 to 6|0.5, 0.5, 0.5, 0.5,<br>0.35, 0.35|
|SL2PF|Slug-to-puff transition criterion factor (sigma-y/slug length)|10|
|FCLIP|Hard-clipping factor for slugs (0.0 = no extrapolation)|0|
|NSPLIT|Number of puffs created from vertical splitting|3|
|IRESPLIT|Hour for puff re-split|0,0,0,0,0,0,0,0,0,0,0,0<br>,0,0,0,0,0,1,0,0,0,0,0,<br>0|
|ZISPLIT|Minimum mixing height for splitting (m)|100|
|ROLDMAX|Mixing height ratio for splitting|0.25|
|NSPLITH|Number of puffs created from horizontal splitting|5|
|SYSPLITH|Minimum sigma-y (met grid cells)|1|
|SHSPLITH|Minimum puff elongation rate (SYSPLITH/hr)|2|
|CNSPLITH|Minimum concentration (g/m**3)|0|
|EPSSLUG|Fractional convergence criterion for numerical SLUG sampling integration|0.0001|
|EPSAREA|Fractional convergence criterion for numerical AREA source integration|1E-006|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 7 of 9

|INPUT GROUP: 12 -- Misc. Dispersion and Computational Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|DSRISE|Trajectory step-length for numerical rise integration (m)|1.0|
|HTMINBC|Minimum boundary condition puff height (m)|500|
|RSAMPBC|Receptor search radius for boundary condition puffs (km)|10|
|MDEPBC|Near-surface depletion adjustment to concentration (0 = no, 1 = yes)|1|

|INPUT GROUP: 13 -- Point Source Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NPT1|Number of point sources|0|
|IPTU|Units used for point source emissions (e.g., 1 = g/s)|1|
|NSPT1|Number of source-species combinations with variable emission scaling<br>factors|0|
|NPT2|Number of point sources in PTEMARB.DAT file(s)|0|

|INPUT GROUP: 14 -- Area Source Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NAR1|Number of polygon area sources|23|
|IARU|Units used for area source emissions (e.g., 1 = g/m**2/s)|7|
|NSAR1|Number of source-species combinations with variable emission scaling<br>factors|0|
|NAR2|Number of buoyant polygon area sources in BAEMARB.DAT file(s)|0|

|INPUT GROUP: 15 -- Line Source Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NLN2|Number of buoyant line sources in LNEMARB.DAT file|0|
|NLINES|Number of buoyant line sources|0|
|ILNU|Units used for line source emissions (e.g., 1 = g/s)|1|
|NSLN1|Number of source-species combinations with variable emission scaling<br>factors|0|
|NLRISE|Number of distances at which transitional rise is computed|6|

|INPUT GROUP: 16 -- Volume Source Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NVL1|Number of volume sources|0|
|IVLU|Units used for volume source emissions (e.g., 1 = g/s)|1|
|NSVL1|Number of source-species combinations with variable emission scaling<br>factors|0|
|NVL2|Number of volume sources in VOLEMARB.DAT file(s)|0|

|INPUT GROUP: 17 -- FLARE Source Control Parameters (variable emissions file)|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NFL2|Number of flare sources defined in FLEMARB.DAT file(s)|0|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 8 of 9

|INPUT GROUP: 18 -- Road Emissions Parameters|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NRD1|Number of road-links sources|0|
|NRD2|Number of road-links in RDEMARB.DAT file|0|
|NSFRDS|Number of road-links and species combinations with variable emission-rate<br>scale-factors|0|

|INPUT GROUP: 19 -- Emission Rate Scale-Factor Tables|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NSFTAB|Number of emission scale-factor tables|0|

|INPUT GROUP: 20 -- Non-gridded (Discrete) Receptor Information|Col2|Col3|
|---|---|---|
|**Parameter**|**Description**|**Value**|
|NREC|Number of discrete receptors (non-gridded receptors)|3|
|NRGRP|Number of receptor group names|0|

CALPUFF View Version 8.5.0 by Lakes Environmental Software 01/08/2019 Page 9 of 9