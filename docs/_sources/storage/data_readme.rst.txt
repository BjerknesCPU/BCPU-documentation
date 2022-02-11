README files
============

README files are files which contain information about the data or software
that they are located with. In the NS9039K data structure, there are
README.json files, which provide metadata on the datasets which we store.

When adding or modiying a directory in the /projects/NS9039K/data directory,
make sure to add or update the README.json file. If you need to add a new
README.json, please copy an existing README and update the fields, or save the
following text into a file called 'README.json' and edit as required::

  {
      "isDataset": true,
      "isCollection": false,

      "title": "ERA Interim",
      "version": null,
      "description": "A global atmospheric reanalysis produced by ECMWF, it has been superseded by the ERA5 reanalysis.",
      "ownerEmail": "tarkan.bilge@uib.no",

      "publicationType": null,
      "publicationDOI": null,

      "locationPoint": null,
      "locationBox": "name=Global; eastlimit=0; westlimit=359.25; northlimit=90; southlimit=-90",

      "timePeriod": "start=1979-01-01; end=2019-08-31",

      "dataSource": "https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim",
      "history": {
                    "2020-09-01" : "Data downloaded.",
                    "2020-09-20" : "Converted GRIB files to NetCDF format."
      }
  }


Fields
------

**isDataset**: ``true`` if the directory is a 'dataset' as defined by
the :doc:`storage structure <storage_structure>`, otherwise ``false``.

**isCollection**: ``true`` if the directory is a 'collection' of datasets
or of more collections, as defined in the
:doc:`storage structure <storage_structure>`, otherwise ``false``.

**title**: string which briefly describes the collection or dataset, e.g.
``"CMIP6"`` or ``"ERA5"``.

**version**: version of the dataset if known, otherwise ``null``.

**description**: a description of the collection or dataset.

**ownerEmail**: the email address of the owner of the dataset.

**publicationType**: only relevant for data which has an internal publication
associated with it. ``null`` if no publication. Otherwise one of the following:
``"Published"``, ``"Accepted"``, ``"Preparation"``, ``"Conference"``,
``"Other presentation"``.

**publicationDOI**: DOI of above publication, or ``null``.

**locationPoint**: the location of the data if it is point-based rather than
gridded. Use this
`format <https://www.dublincore.org/specifications/dublin-core/dcmi-point/>`_.

**locationBox**: the latitude-longitude or depth box of the data in this
`format <https://www.dublincore.org/specifications/dublin-core/dcmi-box/>`_.

**timePeriod**: the time period of the data as a string in this
`format <https://www.dublincore.org/specifications/dublin-core/dcmi-period/>`_.

**dataSource**: URL of data source as a string.

**history**: history of the data collection or dataset with dates. If new data
is added, or data is modified or processed, update the history with a brief
description of the action.

.. note::

  The README files have the extension .json, and are written as JSON files. JSON
  is a data interchange format which easily allows us to write metadata into a
  text file and then read it with scripts.
