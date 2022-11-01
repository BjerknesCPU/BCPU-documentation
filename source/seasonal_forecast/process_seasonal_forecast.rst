Processing seasonal forecast
============================

This page provides documentation on how to process the seasonal forecast every month. This begins with running scripts that modify metadata so that the forecast can be provided in a C3S-like format to the Climate Futures project. After this, some standard plots and indices are produced, and `the website <http://ns9039k.web.sigma2.no/tbi045/seasonal_forecast/index.html>`_. is updated. 

Metadata processing
-------------------

In order to perform the metadata processing, you will need to load the shared conda environment. :: 

  source /projects/NS9039K/shared/python3env/etc/p3env.sh

Then you need a copy of the GitHub repository with the processing scripts. :: 

  git clone git@github.com:BjerknesCPU/C3S-NorCPM-CF.git

Now run h0.atm and h2.atm to process monthly and six-hourly data respectively. 
You need to modify the INPUT_GLOB and OUTPUT_DIR variables in the Input section of both files, then run. :: 

  python h0.atm 
  python h2.atm

These should produce files in your selected output directory which have modified metadata. 
These should be placed somewhere that can be accessed by Alex Lenkoski, e.g. ::

  /projects/NS9039K/www/tbi045/climate_futures/forecast/

Email Alex to let him know that the forecast is complete. 

Generating standard plots
-------------------------

In order to produce ENSO and IOD index plots, we need up-to-date ERA5 data, so update this first: :: 

  cd /projects/NS9039K/data/external/reanalysis/ECMWF/ERA5/scripts  
  python download_era5_2022.py

Convert the ERA5 data from GRIB to NetCDF, e.g. :: 

  cd /projects/NS9039K/data/external/reanalysis/ECMWF/ERA5/original/monthly_single_level/monthly_averaged_reanalysis/sst/
  cdo -f nc copy ERA5_sea_surface_temperature_202201-202209.grib ERA5_034_202201-202209.grib

Now you can run the two index plots. Make sure to update the input files first. ::

  cd C3S-NorCPM-CF
  python enso_plot.py
  python iod_plot.py 

Run the mean anomaly and quantile plotting scripts. Make sure to update the input and output locations and dates. Run twice, once for 'global' and once for 'europe' :: 

  python mean_anomaly_plots.py
  python quantile_plots.py 

This produces output plots in your specified directory. :: 

  /projects/NS9039K/www/tbi045/seasonal_forecast/plots/

Updating the website
--------------------

You need to update the index file to display the new plots on the website. :: 

  vi /projects/NS9039K/www/tbi045/seasonal_forecast/index.html

In this file, you must:

1) Add the current date to the issueListQuantile
2) Input the current date as the issueStringQuantile
3) Add the current date to the issueListAnomaly
4) Input the current date as the issueStringAnomaly
5) Add the current date as the top option in the issueSelectQuantile form

::

  <form>
  <b> Issue Date </b>
  <select id="issueSelectQuantile" onchange="updateIssueQuantile()" autocomplete="off">
  <option selected> 2022-10 </option> <!-- Replace with most recent date -->
  <option> 2022-09 </option> <!-- Add extra line for second most recent date --> 
  <option> 2022-08 </option>
  <option> 2022-07 </option>
  <option> 2022-06 </option>
  <option> 2022-05 </option>
  </select>
  </form>


6) Add the current date as the top option in the issueSelectAnomaly form

::

  <form>
  <b> Issue Date </b>
  <select id="issueSelectAnomaly" onchange="updateIssueAnomaly()" autocomplete="off">
  <option selected> 2022-10 </option> !-- Replace with most recent date -->
  <option> 2022-09 </option> !-- Add extra line for second most recent date -->
  <option> 2022-08 </option>
  <option> 2022-07 </option>
  </select>
  </form>

7) Update IOD and ENSO plot links to current date.

::

  <img id="nino34Image" src="plots/202210_enso.png" style="width:1000px"> 
  <img id="iodImage" src="plots/202210_iod.png" style="width:1000px">


Now the forecast production and processing is complete! Have a look at the forecasts `here <http://ns9039k.web.sigma2.no/tbi045/seasonal_forecast/index.html>`_.
