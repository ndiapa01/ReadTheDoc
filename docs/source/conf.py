# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'TestSphinx'
copyright = '2020, Ndiaye pape ilo, Somfy Group'
author = 'pape ilo'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#import custom css theme
# had to install sphinx_rtd_theme uwing pip
extensions = ["sphinx_rtd_theme"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# define the main page name here
master_doc = 'index'

# define here html pages that you want to generate when builing the document
man_pages = [
    (master_doc,'Requirements','Continuous_Documentation','Revisions_Management',[author],1)
]
# add a logo to your document
html_logo = '_static/images/SomfyH&B.png'
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# use recommonmark for extensions
extensions = ['recommonmark']



html_theme = "sphinx_rtd_theme"