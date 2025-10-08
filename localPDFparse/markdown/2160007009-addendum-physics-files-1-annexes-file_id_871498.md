---
title: Apéndice 4.pdf
author: Matías De La Parra
date: D:20240405102528-03'00'
language: es
type: general
pages: 5
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - APÉNDICE 4
-->

# APÉNDICE 4

## PARAMETRIZACIÓN WRF

### _Cliente:_

A continuación, se presentan los resultados de las configuraciones utilizadas y la descripción de
los dominios correspondientes al servicio de “Modelación Meteorológica con WRF del año 2022
para la Zona de Union, Dominio de 100 x 100 km”.

 - Periodo de simulación: 00:00:00_01-01-2022 - 00:00:00_01-01-2023 (UTC-04).

 - Resolución horizontal dominio interior: 1.0 km.

 - Extensión horizontal del dominio interior: 105 x 105 km.

 - Centro Dominio: -40.215, -73.039.

 - Proyección: Lambert Conformal Conic (LCC)

 - True Lat 1: -36.340

 - True Lat 2: -44.116

 - Datum: NWS-84

En la siguiente se presentan el dominio de modelación con su resolución y usos de suelo:

La configuración del modelo WRF utilizada se corresponde con las siguientes
parametrizaciones:

&time_control
run_days = 0,
run_hours = 0,
run_minutes = 0,
run_seconds = 0,
start_year = 2022, 2022, 2022,
start_month = 01, 01, 01,
start_day = 01, 01, 01,
start_hour = 00, 00, 00,
end_year = 2023, 2023, 2023,
end_month = 01, 01, 01,
end_day = 01, 01, 01,
end_hour = 04, 04, 04,
interval_seconds = 21600
input_from_file = .true.,.true.,.true.,
history_interval = 60, 60, 60,
frames_per_outfile = 24, 24, 24,
restart = .false.,
restart_interval = 1440,
io_form_history = 2
io_form_restart = 2
io_form_input = 2
io_form_boundary = 2

/

&domains

time_step = 40,
time_step_fract_num = 0,
time_step_fract_den = 1,
max_dom = 3,
e_we = 93, 97, 106,
e_sn = 93, 97, 106,
e_vert = 44, 44, 44,
p_top_requested = 5000,
num_metgrid_levels = 34,
num_metgrid_soil_levels = 4,
dx = 9000, 3000, 1000,

dy = 9000, 3000, 1000,
grid_id = 1, 2, 3,
parent_id = 0, 1, 2,
i_parent_start = 1, 31, 31,
j_parent_start = 1, 31, 31,

parent_grid_ratio = 1, 3, 3,
parent_time_step_ratio = 1, 3, 3,
feedback = 1,
smooth_option = 0,
eta_levels = 0.000000, 0.051578, 0.101822, 0.150735, 0.198315, 0.244562,
0.289477, 0.333059, 0.375309, 0.416226, 0.455810, 0.494062, 0.530982, 0.566569, 0.600823,

0.633745, 0.665334, 0.695591, 0.724515, 0.752107, 0.778366, 0.803292, 0.826886, 0.849148,

0.870076, 0.889673, 0.907937, 0.923302, 0.937101, 0.949333, 0.960000, 0.969101, 0.976635,

0.982603, 0.987005, 0.989841, 0.991111, 0.992381, 0.993651, 0.994921, 0.996190, 0.997460,

0.998730, 1.000000,

use_adaptive_time_step = .true.,
step_to_output_time = .true.,
target_cfl = 2.2, 2.2, 2.2,
starting_time_step = 5,
max_time_step = 15,
min_time_step = 1,
max_step_increase_pct = 2,
use_surface = .false.,
force_sfc_in_vinterp = 0,

/

&physics
mp_physics = 3, 3, 3,
ra_lw_physics = 1, 1, 1,
ra_sw_physics = 1, 1, 1,
radt = 12, 12, 12,
sf_sfclay_physics = 4, 4, 4,
sf_surface_physics = 1, 1, 1,
bl_pbl_physics = 4, 4, 4,
bldt = 0, 0, 0,

cu_physics = 2, 2, 2,
cudt = 5, 5, 5,

isfflx = 1,

ifsnow = 0,

icloud = 1,
surface_input_source = 1,
num_soil_layers = 5,
sf_urban_physics = 0, 0, 0,
maxiens = 1,

maxens = 3,

maxens2 = 3,

maxens3 = 16,

ensdim = 144,

num_land_cat = 21,

/

&fdda

/

&dynamics
w_damping = 1,
diff_opt = 1,
km_opt = 4,
diff_6th_opt = 0, 0, 0,
diff_6th_factor = 0.120000, 0.120000, 0.120000,
base_temp = 290,
damp_opt = 0,
zdamp = 5000, 5000, 5000,
moist_adv_opt = 1, 1, 1,
scalar_adv_opt = 1, 1, 1,

/

&bdy_control
spec_bdy_width = 5,
spec_zone = 1,
relax_zone = 4,
specified = .true., .false., .false.,
nested = .false., .true., .true.,

/

&grib2

/

&namelist_quilt
nio_tasks_per_group = 0,
nio_groups = 1,
/

Sin otro particular,

Dr Fabio Carrera Chapela

Director Técnico

AQOM Ltda.