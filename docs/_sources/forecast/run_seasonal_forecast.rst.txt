Running the seasonal forecast
=============================

This page provides documentation on how to run the NorCPM seasonal forecast. 

Update the data for assimilation
--------------------------------

.. note::

  NOAA SST data is changing from OISST to OISSTv2.1 for the December 2022 forecast. 
  Some of these instructions will change during this transition.  

Before running the analysis to the present date, new observational data must be downloaded.

Update the temperature and salinity profile data. ::

  cd /cluster/shared/noresm/norcpm/Obs/TEM/EN422/
  ./Update_profile.sh

Take a note of the most recent final and preliminary files. 

For example: :: 
  
  EN.4.2.2.f.profiles.g10.202207.nc
  EN.4.2.2.p.profiles.g10.202208.nc

Run the analysis
----------------

Move into your analysis directory, and modify the start date (e.g. 2022-12-15-00000) in your settings file. :: 

  cd /cluster/projects/nn9039k/people/tbi045/NorCPM/analysis/setting/
  vi default_setting_VCF.sh

Check if the correct restart files for your start date exist in your run directory. :: 

  ls /cluster/work/users/tbi045/noresm/norcpm-cf-system1_assim_19811115/norcpm-cf-system1_assim_19811115_mem01/run/

If they do not, then you need to copy them over. :: 

  vi /cluster/projects/nn9039k/people/tbi045/NorCPM/analysis/script_pot/mv_rst_from_archive_to_run.sh

To run the analysis, make sure that you load the correct environments. :: 

  conda deactivate
  source /cluster/projects/nn9039k/people/tbi045/NorCPM/analysis/load_envs.sh
  sbatch submit_reanalysis_VCF.sh
 

Run the prediction
------------------

Move into prediction directory. :: 

  cd /cluster/projects/nn9039k/people/tbi045/NorCPM/prediction/use_cases/

Create a new case .in file and change the date (two places in file) e.g. :: 

  cp norcpm-cf-system1_hindcast1_20221015.in norcpm-cf-system1_hindcast1_<date>.in
  
Create a template, create and ensemble and submit the prediction. ::

  ./create_template.sh use_cases/norcpm-cf-system1_hindcast1_<date>.in
  ./create_ensemble.sh use_cases/norcpm-cf-system1_hindcast1_<date>.in
  ./submit_ensemble.sh use_cases/norcpm-cf-system1_hindcast1_<date>.in


Clearing up
-----------

Run mergediag.sh (modify the directory name in the file). :: 

  cd /cluster/projects/nn9039k/people/tbi045/NorCPM/tools
  vi mergediag.sh
  sbatch mergediag.sh

This produces a merged directory in the archive (takes some time) e.g. :: 

  /cluster/work/users/tbi045/archive/norcpm-cf-system1_hindcast1_20220915/norcpm-cf-system1_hindcast1_20220915_mem01-60

Copy forecast files to NIRD, using scp or rsync from above directory. e.g. ::

  cd /cluster/work/users/tbi045/archive/norcpm-cf-system1_hindcast1_20220915/
  scp --r norcpm-cf-system1_hindcast1_20220915_mem01-60/ $USER@login1-trd.nird.sigma2.no:/projects/NS9039K/shared/ClimateFutures/new/ 

Delete restart files that will not be needed anymore. You need to determine which restart files you will need next month. 
The analysis next month should start from the last 'final' assimilation files that were used, so in this example, if temperature and salinity profiles were noted down as: :: 

  EN.4.2.2.f.profiles.g10.202207.nc
  EN.4.2.2.p.profiles.g10.202208.nc

Then the analysis will continue from 202207, so keep these restart files, with care, remove any others e.g. :: 

  rm -rf /norcpm-cf-system1_assim_19811115_mem??/rest/2022-04-15-00000/

Compress files. ::

   cd /cluster/projects/nn9039k/people/tbi045/NorCPM/tools
   sbatch fanf_noresm2netcdf4.pbs

Move analysis files to NIRD. :: 

  cd /projects/NS9039K/shared/tbi045/scripts/
  ./Transfer_reana.sh

Check the files on NIRD, and this concludes generation of the forecast. For steps on processing the output, please see the separate documentation page. 
