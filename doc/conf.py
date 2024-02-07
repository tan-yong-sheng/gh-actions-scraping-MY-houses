# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'gh-actions-scraping-MY-houses'
copyright = '2024, Tan Yong Sheng'
author = 'Tan Yong Sheng'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'autoapi.extension',
]
autoapi_dirs = ['../scrape_housing_data']
#autoapi_options = [ 'members', 'undoc-members', 'show-inheritance', 
#                   'show-module-summary', 'special-members', 'imported-members']


#autoapi_template_dir = '_autoapi_templates'
#autoapi_add_toctree_entry = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']




# to skip document submodule
def skip_submodules(app, what, name, obj, skip, options):
    if what == "module":
        skip = True
    return skip
def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_submodules)