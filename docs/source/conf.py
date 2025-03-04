# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'Intermediate Machine Learning'
copyright = '2025, Bình Phạm'
author = 'Bình Phạm'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'nbsphinx',  # Hỗ trợ Jupyter Notebook
    'myst_parser'  # Hỗ trợ Markdown
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

master_doc = 'index'

highlight_language = 'python3'

# -- Options for EPUB output
epub_show_urls = 'footnote'
