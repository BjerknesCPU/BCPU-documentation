Processing seasonal forecast
============================

This page provides documentation on how to process the seasonal forecast every month. This begins with running scripts that modify metadata so that the forecast can be provided in a C3S-like format to the Climate Futures project. 

1 Metadata processing
-------------------

Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Clone the GitHub repository with the processing scripts if you don’t have it. ::

  git clone https://github.com/BjerknesCPU/C3S-NorCPM-CF.git

Process the monthly data from NorCPM1 forecast output. The monthly data is stored in /nird/projects/NS9873K/norcpm/processed/monthly/. ::

  python h0_atm.py norcpm-cf-system1 20241115

Copy the monthly data into /nird/projects/NS9873K/DATA/SFE/cds_seasonal_forecast/monthly/monthly_mean/bccr/. ::

  ./link_SFE.sh 202412


2 Provide the forecast data to the Climate Futures project
----------------------------------------------------------

Email Silius (smvandeskog(at)nr.no) and Ole (owul(at)norceresearch.no) to let them know that the forecast is ready.
