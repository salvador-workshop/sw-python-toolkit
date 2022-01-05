# sw-toolkit-python

Salvador Workshop's Python Toolkit

## Overview

- integration point for a variety of custom calculations
- is meant to connect those custom calculations to a server or UI
- defines a common API for different tools
- allows custom calculations to share the same base functions

## Usage

### Installation

TEST PACKAGE (TestPyPI)

`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps sw-toolkit-python-retrojusticiar`

Simple test file:

```python
from sw_dtoolkit import toolkit

toolkit.listCalcs()

toolkit.calculate(None, None)
```

### Updating Package

https://packaging.python.org/en/latest/tutorials/packaging-projects/

Make sure you have the latest version of PyPA’s build installed:

`python3 -m pip install --upgrade build`

Now run this command from the same directory where pyproject.toml is located:

`python3 -m build`

You can use twine to upload the distribution packages. You’ll need to install Twine:

`python3 -m pip install --upgrade twine`

Once installed, run Twine to upload all of the archives under dist:

`python3 -m twine upload --repository testpypi dist/*`

You will be prompted for a username and password. For the username, use `__token__`. For the password, use the token value, including the `pypi-` prefix.
