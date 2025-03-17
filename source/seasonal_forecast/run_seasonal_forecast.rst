Running the seasonal forecast
=============================

This page provides documentation on how to run the NorCPM seasonal forecast. In general there are four steps to this process: 

1. Update the input data for assimilation 
2. Run forward the analysis to the present day, using new observational data 
3. Run the prediction 
4. Post-processing 

The forecast should always be provided on the evening of the 14th of the month, as our collaborators need it on the 15th. 

The Met Office provides monthly updates to EN4.2.2. observational temperature and salinity profiles, and these updates happen on the 9th-17th of each month. If this update can be included into the assimilation then this is good, as it gives us an additional month of temperature and salinity data to assimilate. You can check when the last update was on the Met Office `site <https://www.metoffice.gov.uk/hadobs/en4/download-en4-2-2.html>`_ (see bottom of page, or look at file links). I would recommend running the analysis on the 12th/13th of the month. It takes ~3 hours to run. I would then recommend running the prediction on the 12/13th, this takes ~2 hours. The post processing takes another ~2 hours. Therefore, if there are no issues the whole workflow takes around 1 working day, but doing this on the 12/13th allows for potential issues (e.g. machine instability) to be addressed. It is important to keep an eye out for Betzy downtime announcements in the week preceding the 15th to ensure there is no significant disruption.


1 Update the data for assimilation
------------------------------------
The first step in running the seasonal forecast is to update the observational data that is assimilated into the analysis. The steps below show how it is done for the forecast initialized in December 2024 on Betzy. 


1. Update the temperature and salinity profile data

  ::
  cd /cluster/projects/nn9039k/inputdata/obs/TEM/EN422

Download the temperature and salinity profiles from the UK Met Office (https://www.metoffice.gov.uk/hadobs/en4/download-en4-2-2.html). ::

  ./retrieveEN4.sh


2. Update NOAA OISST ver.2.1 data for the two previous months
If the daily OISST data server (https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/) is available: ::

  cd /cluster/projects/nn9039k/inputdata/obs/SST/NOAA/hires

Download daily OISST high resolution data from NOAA. ::
  
  ./download_oisst_hires.sh 2024 10 2024 11

Load the shared conda environment on Betzy. ::

  source /cluster/projects/nn9039k/people/pgchiu/conda/py3env.sh

Finally, compute monthly mean. ::

  ./interpolate_oisst_hires.sh 2024 10 2024 11


.. note::

  Alternatively, if the daily OISST data is not available: 
  Download the yearly OISST high resolution data from the server (https://psl.noaa.gov/thredds/catalog/Datasets/noaa.oisst.v2.highres/catalog.html). ::

    cd /cluster/projects/nn9039k/inputdata/obs/SST/NOAA/hires_v2

  Download the yearly OISST data. ::

    ./download_oisst_hires_v2.sh 2024

  After the yearly OISST high resolution data is downloaded, the daily data needs to be extracted.
  Load the shared conda environment. ::

    source /cluster/projects/nn9039k/people/pgchiu/conda/py3env.sh

  Run a python script to extract daily OISST from one yearly NetCFD file. ::

    python extract_daily_oisst.py 202410 202411

  Finally, compute monthly mean. ::

    ./interpolate_oisst_hires_v2.sh 2024 10 2024 11 


Now the SST, temperature and salinity profiles are updated. 

When it comes to running the analysis, it is important to note that some of the temperature and salinity profiles are initially uploaded by the Met Office as ‘preliminary’, and then are replaced later by ‘final’ files. 

Similarly, daily OISST high resolution data are initially uploaded by NOAA as ‘preliminary’ (e.g., oisst-avhrr-v02r01.20241031_preliminary.nc), and then are replaced later by final’ files (e.g., oisst-avhrr-v02r01.20241031.nc). 

We always want to run the analysis with the best possible data, which means that each month, we will re-run the part of the analysis that used ‘preliminary’ data last month. This means that it is important to keep track of what the latest observational files are each month. 

Note that the data servers are sometimes unavailable due to maintenance downtime or capacity problems. You need to try again later. 



2 Install NorCPM forecast system
----------------------------------
Create a personal folder in nn9039k on Betzy. ::

  mkdir -p /cluster/projects/nn9039k/people/$USER 
  cd /cluster/projects/nn9039k/people/$USER 

Download the code with git clone. ::

  git clone ssh://git@github.com/NorESMhub/NorCPM.git norcpm-cf  


3 Create workflow script
--------------------------
We recommend creating a workflow Shell Script under norcpm-cf/setup/noresm1 so that you don’t need to change arguments or edit the setup files whenever you run simulations. ::

  cd /cluster/projects/nn9039k/people/$USER/norcpm-cf/setup/noresm1 

Copy the code below into the workflow script.

**workflow_seasonal_forecast.sh:** ::

  #!/bin/sh -e 
  : ${INIDATE_ANALYSIS:=2024-08-15} #<--change the date!!! e.g., 2024-08-15 for Dec forecast 
  : ${INIDATE_FORECAST:=2024-11-15} #<--change the date!! e.g., 2024-11-15 for Dec forecast 
  : ${CHMOD_DATE:=20241115} #<--change the date!! e.g., 20241115 for Dec forecast 
  : ${SETTING_FILE_ANALYSIS:=norcpm-cf-system1_assim_19811115_continue20240815.sh} 
  : ${SETTING_FILE_FORECAST:=norcpm-cf-system1_hindcast_20230415.sh} 
  : ${ACCOUNT:=nn9873k} # nn9873k: Climate Futures; nn9039k: BCPU 

  export INIDATE_ANALYSIS INIDATE_FORECAST CHMOD_DATE SETTING_FILE_ANALYSIS SETTING_FILE_FORECAST ACCOUNT 

  ### Analysis experiment ### 

  if [[ $1 && $1 == "create_analysis" ]] 
  then 
      	echo create analysis experiment 
    	./create_ensemble.sh $SETTING_FILE_ANALYSIS REF_DATES=$INIDATE_ANALYSIS 
  fi 

  if [[ $1 && $1 == "run_analysis_stage1" ]] # propagate NorCPM for 3 months (skip first assimilation) 
  then 
    	echo submit analysis experiment stage 1 
    	./submit_ensemble.sh $SETTING_FILE_ANALYSIS ACCOUNT=$ACCOUNT RESTART=2 SKIP_ASSIM_START=1 SKIP_ASSIM_FIRST=1 
  fi 

  if [[ $1 && $1 == "run_analysis_stage2" ]] # propagate NorCPM for another month, only assimilating SST 
  then 
    	echo submit analysis experiment stage 2 
    	./submit_ensemble.sh $SETTING_FILE_ANALYSIS WALLTIME='01:00:00' ACCOUNT=$ACCOUNT RESTART=0 SKIP_ASSIM_START=0 SKIP_ASSIM_FIRST=0 OBSLIST=SST PRODUCERLIST=NOAA REF_PERIODLIST=1982-2016 COMBINE_ASSIM=1 
  fi 

  if [[ $1 && $1 == "backup_analysis" ]] 
  then 
    	echo backup analysis 
    	rsync -uav /cluster/work/users/$USER/archive/norcpm-cf-system1_assim/norcpm-cf-system1_assim_19811115 /nird/datalake/NS9873K/norcpm/raw/norcpm-cf-system1/norcpm-cf-system1_assim/ 
  fi 


  ### Prediction ### 

  if [[ $1 && $1 == "setup_forecast" ]] 
  then 
    	echo create forecast 
    	./create_ensemble.sh $SETTING_FILE_FORECAST START_DATE=$INIDATE_FORECAST REF_DATES=$INIDATE_FORECAST 
  fi 

  if [[ $1 && $1 == "run_forecast" ]] 
  then 
    	echo run forecast 
    	./submit_ensemble.sh $SETTING_FILE_FORECAST START_DATE=$INIDATE_FORECAST REF_DATES=$INIDATE_FORECAST ACCOUNT=$ACCOUNT 
  fi 

  if [[ $1 && $1 == "merge_forecast" ]] 
  then 
    	echo merge forecast 
    	sbatch ../../tools/mergediag/mergediag.betzy.sh /cluster/work/users/$USER/archive/norcpm-cf-system1_hindcast/norcpm-cf-system1_hindcast_`echo $INIDATE_FORECAST | sed 's/-//g'` 
  fi 

  if [[ $1 && $1 == "backup_forecast" ]] 
  then 
    	echo backup forecast 
    	mkdir -p /nird/datalake/NS9873K/norcpm/raw/norcpm-cf-system1/norcpm-cf-system1_hindcast/norcpm-cf-system1_hindcast_`echo $INIDATE_FORECAST | sed 's/-//g'` 
    	rsync --info=progress2 -uav /cluster/work/users/$USER/archive/norcpm-cf-system1_hindcast/norcpm-cf-system1_hindcast_`echo $INIDATE_FORECAST | sed 's/-//g'`/norcpm-cf-system1_hindcast_`echo $INIDATE_FORECAST | sed 's/-//g'`_mem01-60 /nird/datalake/NS9873K/norcpm/raw/norcpm-cf-system1/norcpm-cf-system1_hindcast/norcpm-cf-system1_hindcast_`echo $INIDATE_FORECAST | sed 's/-//g'`/ 
    	chmod -R go+rx /nird/datalake/NS9873K/norcpm/raw/norcpm-cf-system1/norcpm-cf-system1_hindcast/norcpm-cf-system1_hindcast_$CHMOD_DATE 
  fi 


.. note::
  Note that **INIDATE_ANALYSIS**, **INIDATE_FORECAST**, **CHMOD_DATE** need to be updated in the script before you start a new experiment in the next month. 



4 Create analysis experiment (if not exist)
---------------------------------------------
**Under construction. Sorry!!**


5 Run the analysis
--------------------
**Under construction. Sorry!!**


6 Backup output from the analysis
-----------------------------------
**Under construction. Sorry!!**


7 Create prediction
---------------------
**Under construction. Sorry!!**


8 Run the prediction
----------------------
**Under construction. Sorry!!**


9 Merge output from the prediction
------------------------------------
**Under construction. Sorry!!**


10 Backup output from the prediction
--------------------------------------
**Under construction. Sorry!!**
