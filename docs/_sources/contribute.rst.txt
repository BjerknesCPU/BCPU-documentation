Contribute
==========

This page describes the process of contributing to this documentation. There is
a simple six step workflow described in the first section, and there are more
detailed notes on each step in case you have issues.

Six steps to contribute documentation
-------------------------------------


#. Clone the
   `BCPU-documentation <https://github.com/BjerknesCPU/BCPU-documentation>`_
   repository using git. Ideally you should clone this repository to NIRD, in
   the location /project/NS9039K/www/<user>/ where <user> is your personal
   directory (if you do not have one, create one with your name or username).

#. Make changes or add files in the source (BCPU-documentation/source)
   directory.

#. In the root directory (BCPU-documentation/) Call the command ``make github``
   which will build html files into the build/ directory and automatically
   and copy them into the docs/ directory.

#. Check your changes locally, before pushing them to GitHub.

#. Add, commit and push your changes to GitHub.

#. Check the published changes
   `online <https://bjerknescpu.github.io/BCPU-documentation/>`_
   (this can take a couple of minutes to update).

Cloning the GitHub repository
#############################

In order to clone the repository, you should run the command
```git clone git@github.com:BjerknesCPU/BCPU-documentation.git`` which will
produce a directory 'BCPU-documentation/' in the directory you are working in.
You should clone this repository to NIRD, in the location
/project/NS9039K/www/<user>/ where <user> is your personal
directory (if you do not have one, create one with your name or username).

You only need to do this step the first time you modify the documentation.

For more on cloning, see this
`page <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_.

If you have never used the organisational GitHub before, you may have to
`set up ssh keys <https://docs.github.com/en/enterprise-server@3.0/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_.

If you have issues with this step, or with access to the GitHub repository,
please contact our :doc:`internal support <../support/support>`.

Making changes to the source
############################

The 'source' refers to the files that we write, and the 'build' refers to files
that are generated from the source and displayed on the documentation site.

In this documentation, the source files are written in reStructuredText, which
is a type of markup. Writing in this format, allows the build files (html) to be
automatically generated from the source files, so we just have to worry about
writing the source files, which are stored in the source/ directory.

Here is an introduction to
`reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_
but an easy way of getting started is to copy the format of existing .rst files
in the source directory.

Create a new file with the extension .rst to add a new page to the
documentation. You can create a new directory if you want a new category of
documentation to organise your documentation within.

If you have added a new page to the documentation, you must add a link to it
in the file index.rst. For example, the following text adds a link to the 'contribute' page in the
'documentation' category::
  .. toctree::
    :maxdepth: 1
    :caption: Documentation

    documentation/contribute

Build the documentation
#######################

The documentation is built using
`Sphinx <https://www.sphinx-doc.org/en/master/>`_. In order to use Sphinx, you
will need to load an environment which contains the library. On NIRD, this is
our shared conda environment, which can be activated as follows:

.. code-block:: bash

  $ source /opt/anaconda3/etc/profile.d/conda.sh
  $ conda activate /projects/NS9039K/shared/python3env

The documentation is built by calling: ``make github`` in the root directory.
This will use the files in the source/ directory to generate html files in the
build/ directory. These are then automatically copied to the docs/ directory,
which is where the documentation is read from for the website. Of course, these
changes are not applied to our documentation website until we push back to
GitHub, but you can have a look at your changes before you make them visible to
everyone else (see next step).

Check your changes
##################

Once you have run the ``make github`` command, the built files should be
available for viewing in the docs/ directory. It is good practice to view these
files in an HTML browser before pushing them to GitHub. If you have cloned the
repository to NIRD in the /projects/NS9039K/www/<user> directory, then you can
check your changes `here <http://ns9039k.web.sigma2.no>`_.


Add, commit and push your changes
#################################

Use `git add`, `git commit` and `git push` to push your changes to the remote
repository. Once you have done this, the
`online pages <https://bjerknescpu.github.io/BCPU-documentation/>`_ should
automatically update after 1-2 minutes.
