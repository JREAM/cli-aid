# Development

Resource for PIP: [https://packaging.python.org/distributing/](https://packaging.python.org/distributing/)

Sample PIP Project: [https://github.com/pypa/sampleproject](https://github.com/pypa/sampleproject)

Fav. PIP Example: [https://github.com/dbcli/mycli](https://github.com/dbcli/mycli) - a helper/refresh would be nice

# Working in Development Mode

https://packaging.python.org/distributing/#working-in-development-mode

-e --editable
pip install -e .

pip install -e . --no-deps


# Compiling
```
python setup.py sdist
or ?
python setup.py bdist_wheel --universal
```

# For PyPi
Need account and `~/.pypirc`:

```
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = <username>
password = <password>
```

> You can leave out the password line if you use twine with its -p PASSWORD argument or prefer to simply enter your password when prompted.

# Registering Project

https://packaging.python.org/distributing/#register-your-project
