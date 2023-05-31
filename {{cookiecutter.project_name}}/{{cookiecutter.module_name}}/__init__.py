{% if cookiecutter.use_git_tags_for_versioning == 'y' %}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{% else -%}
__version__ = "0.0.1"
{% endif -%}