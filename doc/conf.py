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
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

extensions.append('sphinx.ext.todo')
extensions.append('sphinx.ext.intersphinx')
extensions.append('sphinx.ext.mathjax')
extensions.append('sphinx.ext.viewcode')
extensions.append('sphinx.ext.graphviz')
extensions.append('sphinx.ext.coverage')
extensions.append('sphinx.ext.napoleon')
extensions.append('sphinx_autodoc_typehints')
extensions.append('nbsphinx')


autosummary_generate = True
autoclass_content = 'both'
html_show_sourcelink = False
autodoc_inherit_docstrings = True
set_type_checking_flag = True
autodoc_default_flags = ['members']
