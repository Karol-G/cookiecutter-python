# cookiecutter-python

[Cookiecutter] template for authoring Python projects.

**NOTE: This repo is not meant to be cloned/forked directly! Please read "Getting Started" below**

## Getting Started

### Create your Python project

Install [Cookiecutter] and generate a new Python project:

```bash
pip install cookiecutter
cookiecutter https://github.com/Karol-G/cookiecutter-python
```

Cookiecutter prompts you for information regarding your project
(A new folder will be created in your current working directory):

```bash
full_name [Project Developer]: Karol Gotkowski
email [yourname@example.com]: karol.gotkowski@dkfz.de
github_username_or_organization [githubuser]: Karol-G
project_name [project-foobar]: my-project
Select github_repository_url:
1 - https://github.com/Karol-G/my-project
2 - provide later
Choose from 1, 2 [1]:
module_name [my_project]: my_project
short_description [A Python project]:
use_git_tags_for_versioning [n]:
Select license:
1 - BSD-3
2 - MIT
3 - Mozilla Public License 2.0
4 - Apache Software License 2.0
5 - GNU LGPL v3.0
6 - GNU GPL v3.0
Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]:

```

You just created a minimal Python project, complete with tests
and ready for automatic deployment!

For more detailed information on each prompt see the [prompts reference](./PROMPTS.md).

```no-highlight
my-project/
│
├── .github
│   └── workflows
│      └── test_and_deploy.yml
├── LICENSE
├── MANIFEST.in
├── my_project
│   ├── __init__.py
│   └── _tests
│       ├── __init__.py
├── pyproject.toml
├── README.md
├── setup.cfg
└── tox.ini
```

### Initialize a git repository in your package

NOTE: This is important not only for version management, but also if you want to
pip install your package locally for testing with `pip install -e .`. (because
the version of your package is managed using git tags,
[see below](#automatic-deployment-and-version-management))

```bash
cd my-project
git init
git add .
git commit -m 'initial commit'
```

### Upload it to github

1. Create a [new github repository]

2. Add your newly created github repo as a remote and push:

   ```bash
   # here, continuing with the example above...
   # but replace with your own username and repo name

   git remote add origin https://github.com/Karol-G/my-project.git
   git push -u origin main
   ```

### Monitor testing and coverage

The repository should already be setup to run your tests each time you push an
update (configuration is in `.github/workflows/test_and_deploy.yml`). You can
monitor them in the "Actions" tab of your github repository. If you're
following along, go have a look... they should be running right now!

When the tests are done, test coverage will be viewable at
[codecov.io](https://codecov.io/) (assuming your repository is public):
`https://codecov.io/gh/<your-github-username>/<your-package-name>`

You will need to enable the [codecov](https://github.com/apps/codecov) github app
for this to work. See [here](https://github.com/apps/codecov/installations/new)
to install the codecov github app and give it access to your Python project repository.

### Set up automatic deployments

Your new package is also nearly ready to automatically deploy to [PyPI]
(whenever you create a tagged release), so that your users can simply `pip install` your package. You just need to create an [API token to authenticate
with PyPi](https://pypi.org/help/#apitoken), and then add it to your github
repository:

1. If you don't already have one, [create an
   account](https://pypi.org/account/register/) at [PyPI]
2. Verify your email address with PyPI, (if you haven't already)
3. Generate an [API token](https://pypi.org/help/#apitoken) at PyPi: In your
   [account settings](https://pypi.org/manage/account/) go to the API tokens
   section and select "Add API token". Make sure to copy it somewhere safe!
4. [Create a new encrypted
   secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets)"
   in your github repository with the name "TWINE_API_KEY", and paste in your
   API token.

You are now setup for automatic deployment!

### Automatic deployment and version management

Each time you want to deploy a new version, you just need to create a tagged
commit, and push it to your main branch on github. Your package is set up to
use [setuptools_scm](https://github.com/pypa/setuptools_scm) for version
management, meaning you don't need to hard-code your version anywhere in your
package. It will be inferred from the tag each time you release.

```bash
# the tag will be used as the version string for your package
# make it meaningful: https://semver.org/
git tag -a v0.1.0 -m "v0.1.0"

# make sure to use follow-tags so that the tag also gets pushed to github
git push --follow-tags
```

> Note: as of git 2.4.1, you can set `follow-tags` as default with
> `git config --global push.followTags true`

Monitor the "actions" tab on your github repo for progress... and when the
"deploy" step is finished, your new version should be visible on pypi:

`https://pypi.org/project/<your-package-name>/`

and available for pip install with:

```bash
# for example
pip install my-project
```

### Running tests locally

Tests are automatically setup to run on github when you push to your repository.

You can run your tests locally with [pytest](https://docs.pytest.org/en/7.1.x/).
You'll need to make sure that your package is installed in your environment,
along with testing requirements (specified in the setup.cfg `extras_require` section):

```bash
pip install -e ".[testing]"
pytest
```

### Create your documentation

Documentation generation is not included in this template.
We recommend following the getting started guides for one of the following 
documentation generation tools:

1. [Sphinx]
2. [MkDocs]
3. [JupyterBook]

### Pre-commit

This template includes a default yaml configuration for [pre-commit](https://pre-commit.com/).
You may edit the config at `.pre-commit-config.yaml`

To use it run:

```bash
pip install pre-commit
pre-commit install
```

You can also have these checks run automatically for you when you push to github
by installing [pre-commit ci](https://pre-commit.ci/) on your repository.

## Features

- Installable [PyPI] package
- [tox] test suite, testing various python versions and platforms.
- `README.md` file that contains useful information about your project
- Continuous integration configuration for [github actions] that handles testing
  and deployment of tagged releases
- git-tag-based version management with [setuptools_scm]
- Optional documentation with either [Sphinx] or [MkDocs]
- Choose from several licenses, including [BSD-3], [MIT], [MPL v2.0], [Apache
  v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

## Issues

If you encounter any problems with this cookiecutter template, please [file an
issue] along with a detailed description.

## License

Distributed under the terms of the [BSD-3] license, `cookiecutter-python`
is free and open source software.
