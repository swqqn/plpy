# README

Django utilities for Postgres PL/Python

#### Installation

PL/Python, therefore django-plpy requires Postgres plugin for plpython3u. Most of the distributions provide it in their repositories, here is how you install it on Ubuntu:

```
apt-get -y install postgresql-plpython3-10
```

Mind the PostgreSQL version at the end.

Install django-plpy with pip

```
pip install django-plpy
```

Add it to INSTALLED\_APPS

```python
INSTALLED_APPS = [
    ...,
    "django_plpy",
    ...,
]
```

Migrate

```
./manage.py migrate
```

Check if your local python environment is compatible with your Postgres python interpreter.

```shell
./manage.py checkenv
```
