# Configuration file for the Sphinx documentation builder for Read the Docs integration
import os
import sys
import yaml

# -- Project information -----------------------------------------------------
project = 'DISCOVER'
copyright = '2023, Community'
author = 'Community'

# Define version based on branch name
if 'READTHEDOCS' in os.environ:
    version = os.environ.get('READTHEDOCS_VERSION', 'latest')
    if version == 'latest':
        version = 'dev'  # You can map branch names to display names
else:
    version = 'local'

release = version

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_tags',
    'myst_nb',
    'sphinx_external_toc',
    'sphinx_book_theme',
]

# Use MyST for markdown parsing
source_suffix = {
    '.md': 'myst',
}

# The master toctree document
master_doc = 'index'

# List of patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_logo = '_static/logo-light.png'  # Update when you move to images folder

# Theme options
html_theme_options = {
    "repository_url": "https://github.com/numfocus/DISCOVER-Cookbook/",
    "use_repository_button": True,
    "use_issues_button": True,
}

# -- MyST Configuration ------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# Tags extension configuration
tags_create_tags = True
tags_extension = ["md"]

# Load the external TOC
from sphinx_external_toc.parsing import parse_toc_file
if os.path.exists("_toc.yml"):
    external_toc = parse_toc_file("_toc.yml")
    if external_toc:
        suppress_warnings = ["etoc.toctree"]