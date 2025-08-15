Generate forecast plots 
=======================

This page provides documentation on how to generate forecast plots. 

1 Arctic sea ice forecast
-------------------

How to compute the Arctic sea ice area 
^^^^^^^^^^^^^^^^^^^

The forecast plot shows the observed sea ice area for the last 6 months and forecasted sea ice area for the next 6 months.
The observed sea ice area is computed from the OISST ver2.1/ver2 which can be obtaind from the NOAA (ver2.1: https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/; ver2: https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2/access/avhrr-only/).
The OISST ver2.1 is available since 1981/09/01 and the OISST ver2 is available between 1981/09/01 - 2020/04/26.
If the ver2.1 data is missing, you need to use the ver2 data or interpolate the missing data. 

The sea ice area is a sum of grid cell areas multiplied by the ice concentration: 

Sea ice area = Σ grid cell area × ice concentration [%].  

The grid cell area which has at least 15% sea ice concentration in the Northern Hemisphere is chosen.
The climatology of Arctic sea ice area needs to be calculated, relative to the 1993–2016, for both model output and OISST.
The climatology is used to calibrate the forecast.


Compute climatology 
^^^^^^^^^^^^^^^^^^^
Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Clone the GitHub repository with the processing scripts if you don’t have it. ::

  git clone https://github.com/BjerknesCPU/C3S-NorCPM-CF.git

Compute forecasted sea ice area, ensemble means, standard deviation, 10 percentile, 90 percentile, and save results as CSV file. ::

  python read_netcdf_ice.py 199301 201612

Compute climatology of daily sea ice area, relative to the 1993–2016 for 12 periods (Jan-Jun, Feb-Jul, ..., Dec-May) and save results as CSV file. ::

  python calculate_clm_mdl.py

Download the OISST Ver2.1/Ver.2 from NOAA online server (OISST version needs to be set in the script). ::

  python download_oisst.py 199301 201612

Compute observed sea ice area and save results as CSV file (OISST version needs to be set in the script). ::

  python read_oisst_ice.py 199301 201612

Merge OISST Ver2.1 and Ver2 because there is missing data in ver2.1. Treat outliers, interpolate missing data and save results as CSV file. ::

  python merge_oisst_ice.py 1993 2016

Compute climatology of daily sea ice area, relative to the 1993–2016 for 12 periods (Jan-Jun, Feb-Jul, ..., Dec-May) and save results as CSV file. ::

  python calculate_clm_seaice_oisst.py


Plot sea ice forecast
^^^^^^^^^^^^^^^^^^^
Once the latest model output from NorCPM forecast simulation is ready, run the following scripts to compute Arctic sea ice area.

Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Compute forecasted sea ice area, ensemble means, standard deviation, 10 percentile, 90 percentile, and save results as CSV file. ::

  python read_netcdf_ice.py 202412

Download the OISST Ver2.1/Ver.2 from NOAA online server (OISST version needs to be set in the script). ::

  python download_oisst.py 202411 202412

Compute observed sea ice area and save results as CSV file (OISST version needs to be set in the script). ::

  python read_oisst_ice.py 202411 202412

Merge OISST Ver2.1 and Ver2 because there is missing data in ver2.1. Treat outliers, interpolate missing data and save results as CSV file. ::

  python merge_oisst_ice.py 2024 2025

Plot Arctic sea ice forecast with observations (OISST) and save figure as png file. ::

  python plot_seaice_oisst_mdl.py 202412


2 Probability of 2m temperature
-------------------


How to compute probability of 2-meter temperature
^^^^^^^^^^^^^^^^^^^
The forecast plot shows probability of 2-meter temperature.
First, compute climatology (median) of 2-meter temperature, relative to the 1993–2016 for each month, each grid, each lead month (LM1-LM6).
Then, count number of ensemble members that exceed the climatology and calculate percentage.


Compute climatology
^^^^^^^^^^^^^^^^^^^
Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Clone the GitHub repository with the processing scripts if you don’t have it. ::

  git clone https://github.com/BjerknesCPU/C3S-NorCPM-CF.git

Compute climatology (median) of 2-meter temperature, relative to the 1993–2016 for each month, each grid, each lead month. ::

  python calculate_clm_2m_temp.py


Plot 2m temperature probability map
^^^^^^^^^^^^^^^^^^^
Once the latest post-processed data from NorCPM forecast simulation is ready, run the following scripts to plot probability of 2-meter temperature. ::

  python plot_probability_2mt.py 202412


Plot seasonal 2m temperature probability map
^^^^^^^^^^^^^^^^^^^
Plot seasonal probability of 2-meter temperature. ::

  python plot_seasonal_probability_2mt.py 202412



3 Probability of precipitation
-------------------

How to compute probability of precipitation
^^^^^^^^^^^^^^^^^^^
The forecast plot shows probability of precipitation.
First, compute climatology (median) of precipitation, relative to the 1993–2016 for each month, each grid, each lead month (LM1-LM6).
Then, count number of ensemble members that exceed climatology and calculate percentage.


Compute climatology
^^^^^^^^^^^^^^^^^^^
Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Clone the GitHub repository with the processing scripts if you don’t have it. ::

  git clone https://github.com/BjerknesCPU/C3S-NorCPM-CF.git

Compute climatology (median) of precipitation, relative to the 1993–2016 for each month, each grid, each lead month. ::

  python calculate_clm_precipitation.py



Plot precipitation probability map
^^^^^^^^^^^^^^^^^^^
Once the latest post-processed data from NorCPM forecast simulation is ready, run the following scripts to plot probability of precipitation. ::

  python plot_probability_prec.py 202412


Plot seasonal precipitation probability map
^^^^^^^^^^^^^^^^^^^
Plot seasonal probability of precipitation. ::

  python plot_seasonal_probability_prec.py 202412





4 ENSO forecast
-------------------

How to compute Nino 3.4 index
^^^^^^^^^^^^^^^^^^^

The Nino 3.4 index is used to define El Nino and La Nina events.
The forecast plot shows the observed Nino 3.4 index for the last 6 months and forecasted Nino 3.4 index for the next 6 months.
The Nino 3.4 index is the sea surface temperature anomaly in the Nino 3.4 region (5N-5S, 120W-170W).
When the  Niño 3.4 SSTs exceed +/- 0.5 C degree, the El Ninoor La Nina events are defined. 

The observed sea surface temperature is computed from the OISST ver2.1/ver2 which can be obtaind from the NOAA (ver2.1: https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/; ver2: https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2/access/avhrr-only/).


Compute climatology
^^^^^^^^^^^^^^^^^^^
Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Clone the GitHub repository with the processing scripts if you don’t have it. ::

  git clone https://github.com/BjerknesCPU/C3S-NorCPM-CF.git

Compute climatology of sea surface temperature, relative to the 1993–2016 for each month, each grid, each lead month. ::

  python calculate_clm_sst_mdl.py

Download the OISST Ver2.1/Ver.2 from NOAA online server (OISST version needs to be set in the script). ::

  python download_oisst.py 199301 201612

Run Python scripts to compute monthly mean of OISST and calculate horizontal interpolation (grid size: 0.25 degree -> 1 degree).
This script needs "python-cdo" and "pynco" packages.
Recommend creating the conda environment with these packages.

Deactivate the shared conda environment. ::

  conda deactivate

Create a new conda environment with packages. ::

  conda create --name <ENV_NAME> --channel conda-forge numpy pandas python-cdo pynco xarray netcdf4 python=3.11

Activate the conda environment. ::

  conda activate <ENV_NAME>

Run the script to compute monthly mean of OISST and calculate horizontal interpolation. ::

  python interpolate_oisst.py 202412

Compute climatology of OISST, relative to the 1993–2016 for each month, each grid, each lead month.

Deactivate the shared conda environment. ::

  conda deactivate

Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Compute climatology of OISST. ::

  python calculate_clm_oisst.py


Plot ENSO forecast
^^^^^^^^^^^^^^^^^^^
Once the latest OISST data is ready at online server, run the following scripts to download the data and compute monthly mean of OISST. 

Download the OISST Ver2.1 from NOAA online server. ::

  python download_oisst.py 202410 202411

Run Python scripts to compute monthly mean of OISST and calculate horizontal interpolation (grod size: 0.25 degree -> 1 degree).
This script needs "python-cdo" and "pynco" packages.
Recommend creating the conda environment with these packages.
This step can be skipped if the new conda environment has been already created.

Deactivate the shared conda environment. ::

  conda deactivate

Create a new conda environment with packages. ::

  conda create --name <ENV_NAME> --channel conda-forge numpy pandas python-cdo pynco xarray netcdf4 python=3.11

Activate the conda environment. ::

  conda activate <ENV_NAME>

Run the script to compute monthly mean of OISST and calculate horizontal interpolation. ::

  python interpolate_oisst.py 202412

Plot ENSO forecasts with observations. ::

  plot_enso_oisst.py 202412
