# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.append(os.path.abspath("./_ext"))

"""
Sphinx documentation builder
"""

import os

# Set env flag so that we can doc functions that may otherwise not be loaded
# see for example interactive visualizations in qiskit.visualization.
os.environ["QISKIT_DOCS"] = "TRUE"

# -- Project information -----------------------------------------------------
project = "Qiskit Experiments"
copyright = "2021, Qiskit Development Team"  # pylint: disable=redefined-builtin
author = "Qiskit Development Team"

# The short X.Y version
version = "0.4"
# The full version, including alpha/beta/rc tags
release = "0.4.0"

rst_prolog = """
.. raw:: html

    <br><br><br>

.. |version| replace:: {0}
""".format(
    release
)

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}
.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. raw:: html

        <br><br><br>

    .. note::
        Run interactively in jupyter notebook.
"""


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "jupyter_sphinx",
    "sphinx_autodoc_typehints",
    "reno.sphinxext",
    "sphinx_panels",
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "autoref",
    "autodoc_experiment",
    "autodoc_analysis",
    "jupyter-execute-checkenv",
]
html_static_path = ["_static"]
templates_path = ["_templates"]
html_css_files = ["style.css", "custom.css", "gallery.css"]

nbsphinx_timeout = 360
nbsphinx_execute = os.getenv("QISKIT_DOCS_BUILD_TUTORIALS", "never")
nbsphinx_widgets_path = ""
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
nbsphinx_thumbnails = {}


# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

autosummary_generate = True

# -----------------------------------------------------------------------------
# Autodoc
# -----------------------------------------------------------------------------

autodoc_default_options = {
    "inherited-members": None,
}


# If true, figures, tables and code-blocks are automatically numbered if they
# have a caption.
numfig = True

# A dictionary mapping 'figure', 'table', 'code-block' and 'section' to
# strings that are used for format of figure numbers. As a special character,
# %s will be replaced to figure number.
numfig_format = {"table": "Table %s"}
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "colorful"

# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined), e.g. for
# py:function directives.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
# This can be handy if you document a project that consists of a single
# package. Works only for the HTML builder currently.
modindex_common_prefix = ["qiskit_experiments."]

# -- Configuration for extlinks extension ------------------------------------
# Refer to https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "qiskit_sphinx_theme"  # use the theme in subdir 'theme'

# html_sidebars = {'**': ['globaltoc.html']}
html_last_updated_fmt = "%Y/%m/%d"

html_theme_options = {
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
}


autoclass_content = 'both'
intersphinx_mapping = {
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'qiskit': ('https://qiskit.org/documentation/', None),
}


# Current scipy hosted docs are missing the object.inv file so leaving this
# commented out until the missing file is added back.
#                       'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None)}
