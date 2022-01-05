""" Configuration file for the Sphinx documentation builder. """

# =============================================================================
# Imports
# =============================================================================

import os
import sys

# =============================================================================
# Project information
# =============================================================================

project = 'BCPU-documentation'
copyright = '2021, BCPU'
author = 'tarkan.bilge@uib.no'

release = '0.1'
version = '0.1.0'

# =============================================================================
# Path configuration
# =============================================================================

# The paths to directories containing code should be inserted here
# if autodocumentation via Sphinx is desired.
relative_path = '../../'
sys.path.insert(0, os.path.abspath(relative_path))


# =============================================================================
# General configuration
# =============================================================================

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
numfig = True
# =============================================================================
# Options for HTML output
# =============================================================================

html_theme = 'sphinx_rtd_theme'

# =============================================================================
# Options for EPUB output
# =============================================================================

epub_show_urls = 'footnote'
