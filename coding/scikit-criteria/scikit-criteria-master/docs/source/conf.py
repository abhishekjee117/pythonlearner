# -*- coding: utf-8 -*-
#
# Scikit-Criteria documentation build configuration file, created by
# sphinx-quickstart on Thu Aug  3 02:18:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import pathlib
import sys
import datetime as dt


# add the skcriteria source to the build path
CURRENT_PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
SKCRITERIA_PATH = CURRENT_PATH.parent.parent

sys.path.insert(0, str(SKCRITERIA_PATH))

# when we are running this build
UTC_NOW = dt.datetime.utcnow()


# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# to retrieve scikit criteria metadata
import skcriteria


# modules to mock in readthedocs
MOCK_MODULES = []


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "nbsphinx",
    "sphinxcontrib.bibtex",
    "sphinx_copybutton",
]
# =============================================================================
# EXTRA CONF
# =============================================================================

autodoc_member_order = "bysource"

# =============================================================================
# BIB TEX
# =============================================================================

bibtex_default_style = "apa"  # pybtex-apa-style

bibtex_bibfiles = ["refs.bib"]

# =============================================================================
# NUMPY DOC
# =============================================================================

numpydoc_class_members_toctree = False


# =============================================================================
# NB SPHINX
# =============================================================================

nbsphinx_execute = "never"

nbsphinx_allow_errors = True

nbsphinx_prompt_width = "0pt"

nbsphinx_prolog = """
{% set docname = "docs/source/" + env.doc2path(env.docname, base=False) %}
{% set release = "master" %}

.. |nbsp| unicode:: 0xA0
   :trim:

.. only:: html

    .. container:: binder-container

        .. nbinfo::

           Interactive online version.

           With Binder, open this notebook in an executable environment:|nbsp|

           .. image:: https://mybinder.org/badge_logo.svg
               :target: https://mybinder.org/v2/gh/quatrope/scikit-criteria/{{ release }}?filepath={{ docname }}

----


"""

nbsphinx_epilog = f"""
----

Generated by nbsphinx_ from a Jupyter_ notebook.
{UTC_NOW.isoformat()}

.. _nbsphinx: https://nbsphinx.readthedocs.io/
.. _Jupyter: https://jupyter.org/


"""


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = skcriteria.NAME
copyright = "2016-2021, Juan B. Cabral - Nadia A. Luczywo - Copyright (c) 2022, QuatroPe"


author = "Juan BC"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = skcriteria.VERSION
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'donate.html',
#     ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Scikit-Criteriadoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "Scikit-Criteria.tex",
        "Scikit-Criteria Documentation",
        "Juan BC",
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "scikit-criteria",
        "Scikit-Criteria Documentation",
        [author],
        1,
    )
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Scikit-Criteria",
        "Scikit-Criteria Documentation",
        author,
        "Scikit-Criteria",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"https://docs.python.org/": None}


# =============================================================================
# INJECT README INTO THE RESTRUCTURED TEXT
# =============================================================================

import m2r2

DYNAMIC_RST = {
    "README.md": "README.rst",
    "CHANGELOG.md": "CHANGELOG.rst",
}

for md_name, rst_name in DYNAMIC_RST.items():
    md_path = SKCRITERIA_PATH / md_name
    with open(md_path) as fp:
        readme_md = fp.read().split("<!-- BODY -->")[-1]

    rst_path = CURRENT_PATH / "_dynamic" / rst_name

    with open(rst_path, "w") as fp:
        fp.write(".. FILE AUTO GENERATED !! \n")
        fp.write(m2r2.convert(readme_md))
        print(f"{md_path} -> {rst_path} regenerated!")


# =============================================================================
# SETUP
# =============================================================================

EXPORT_CONFIG = ["GIT_HASH"]

def setup(app):
    app.add_css_file("css/skcriteria.css")
    app.add_js_file("js/skcriteria.js")
    for k, v in globals().items():
        if k in EXPORT_CONFIG:
            app.config[k] = v
