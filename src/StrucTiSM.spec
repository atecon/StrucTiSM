author = Riccardo "Jack" Lucchetti and Sven Schreiber
email = r.lucchetti@univpm.it
version = 0.7
date = 2021-11-04
description = Harvey-style Structural Time Series Models
tags = C22 C52
min-version = 2020c

lives-in-subdir="true"
data-files=examples

data-requirement = needs-time-series-data
gui-main = STSM_GUImeta
label = Structural TS
menu-attachment = MAINWIN/Model/TSModels
bundle-print = STSM_printout
bundle-plot = STSM_GUIplot
public = STSM_GUImeta STSM_GUIplot STSM_setup STSM_estimate \
       STSM_printout STSM_components STSM_fcast \
       LLT BSM
help = StrucTiSM.pdf
sample-script = StrucTiSM_sample.inp

