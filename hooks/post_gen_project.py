#!/usr/bin/env python

import logging
import os
import shutil
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("post_gen_project")

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ALL_TEMP_FOLDERS = ["licenses"]



def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        shutil.rmtree(folder, ignore_errors=True)


def remove_unrequested_plugin_examples():
    module = "{{ cookiecutter.module_name }}"
    {% for key, value in cookiecutter.items() %}
    {% if key.startswith('include_') and key.endswith("_plugin") and value != 'y' %}
    name = "{{ key }}".replace("include_", "").replace("_plugin", "")
    remove_file(f"src/{module}/_{name}.py")
    remove_file(f"src/{module}/_tests/test_{name}.py")
    logger.debug(f"removing {module}/_{name}.py")
    {% endif %}
    {% endfor %}


if __name__ == "__main__":
    remove_temp_folders(ALL_TEMP_FOLDERS)
    remove_unrequested_plugin_examples()

    msg = ''
    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
    except Exception:
        pass
{% if cookiecutter.install_precommit == 'y' %}
    # try to install and update pre-commit
    try:
        print("install pre-commit ...")
        subprocess.run(["pip", "install", "pre-commit"], stdout=subprocess.DEVNULL)
        print("updating pre-commit...")
        subprocess.run(["pre-commit", "autoupdate"], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "add", "."])
        subprocess.run(["pre-commit", "run", "black", "-a"], capture_output=True)
    except Exception:
        pass
{% endif %}
    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        msg += """
Your project template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
   (this is also important for version control!)

     cd {{ cookiecutter.project_name }}
     git init -b main
     git add .
     git commit -m 'initial commit'

     # you probably want to install your new package into your environment
     pip install -e ."""
    else:
        msg +="""
Your project template is ready!  Next steps:

1. `cd` into your new directory

     cd {{ cookiecutter.project_name }}
     # you probably want to install your new package into your env
     pip install -e ."""

{% if cookiecutter.install_precommit == 'y' %}
    # try to install and update pre-commit
    # installing after commit to avoid problem with comments in setup.cfg.
    try:
        print("install pre-commit hook...")
        subprocess.run(["pre-commit", "install"])
    except Exception:
        pass
{% endif %}

{% if cookiecutter.github_repository_url != 'provide later' %}
    msg += """
2. Create a github repository with the name '{{ cookiecutter.project_name }}':
   https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_name }}.git

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_name }}.git
     git push -u origin main

4. The following default URLs have been added to `setup.cfg`:

    Bug Tracker = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/issues
    Documentation = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}#README.md
    Source Code = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}
    User Support = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_name}}/issues

    You may wish to change these before publishing your project!"""

{% else %}
    msg += """
2. Create a github repository for your project:
   https://github.com/new

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/your-repo-username/your-repo-name.git
     git push -u origin main

   Don't forget to add this url to setup.cfg!

     [metadata]
     url = https://github.com/your-repo-username/your-repo-name.git

4. Consider adding additional links for documentation and user support to setup.cfg
   using the project_urls key e.g.

    [metadata]
    project_urls =
        Bug Tracker = https://github.com/your-repo-username/your-repo-name/issues
        Documentation = https://github.com/your-repo-username/your-repo-name#README.md
        Source Code = https://github.com/your-repo-username/your-repo-name
        User Support = https://github.com/your-repo-username/your-repo-name/issues"""
{% endif %}
    msg += """
5. Read the README for more info: https://github.com/Karol-G/cookiecutter-python
"""

    print(msg)
