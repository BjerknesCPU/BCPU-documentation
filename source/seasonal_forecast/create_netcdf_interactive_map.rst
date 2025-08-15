Create NetCDF data for interactive maps 
==================

After the latest forecast is ready, save post-processing data as NetCDF files.



Load the shared conda environment on NIRD. ::

  source /nird/projects/NS9039K/shared/py3env/py3env3.bash

Save post-processing data as NetCDF files.

Precipitaion: ::

  python save_probability_prec.py 202412

2-meter temperature: ::

  python save_probability_2mt.py 202412

The interactive maps are automatically updated once a month (http://norcpm-ai.uib.no/). If someting goes wrong, contact Eurico (Eurico.Filho(at)uib.no).
