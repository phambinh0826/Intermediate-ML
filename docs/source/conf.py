# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme

# -- Project information
project = 'Intermediate Machine Learning'
copyright = '2025, Bình Phạm'
author = 'Bình Phạm'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'nbsphinx',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx_gallery.load_style',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Path to static files
html_static_path = ['_static']
html_css_files = [
    'custom.css',  # Thêm tệp custom.css của bạn vào
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
