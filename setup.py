"""
setup.py

This file is used to package and install the Python project.

It uses the `setuptools` library to define project information and
automatically install the required dependencies.

What this file does:

1. Import `setup` and `find_packages` from the setuptools library.
   - `setup` is used to configure the project.
   - `find_packages` automatically finds all Python packages in the project.

2. Open the `requirements.txt` file and read all the dependencies
   required for the project.

3. Store those dependencies in the variable `requirements`.

4. Call the `setup()` function to define the project details such as:
   - Project name
   - Version
   - Author name
   - Packages included in the project
   - Required external libraries

When someone installs this project, Python will automatically install
all the libraries listed in `requirements.txt`.

This helps in distributing and installing the project easily.
"""

from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI TRAVEL AGENT",
    version="0.1",
    author="Shubham",
    packages=find_packages(),
    install_requires = requirements,
)
