# {{cookiecutter.project_name}}

[![License {{cookiecutter.license}}](https://img.shields.io/pypi/l/{{cookiecutter.project_name}}.svg?color=green)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg?color=green)](https://pypi.org/project/{{cookiecutter.project_name}})
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}.svg?color=green)](https://python.org)
[![tests](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/workflows/tests/badge.svg)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/actions)
![Unit Tests](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/actions/workflows/test_and_deploy.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}})

{{cookiecutter.short_description}}

----------------------------------

Project description...

## Installation

You can install `{{cookiecutter.project_name}}` via [pip](https://pypi.org/project/{{cookiecutter.project_name}}/):

    pip install {{cookiecutter.project_name}}


{% if cookiecutter.github_repository_url != 'provide later' %}
To install latest development version :

    pip install git+https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}.git
{% endif %}

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [{{cookiecutter.license}}] license,
"{{cookiecutter.project_name}}" is free and open source software

## Issues

If you encounter any problems, please file an issue along with a detailed description.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
{% if cookiecutter.github_repository_url != 'provide later' %}
[file an issue]: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/issues
{% endif %}
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
