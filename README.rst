=============================
django-collectform
=============================

.. image:: https://badge.fury.io/py/django-collectform.png
    :target: https://badge.fury.io/py/django-collectform

.. image:: https://travis-ci.org/nagyv/django-collectform.png?branch=master
    :target: https://travis-ci.org/nagyv/django-collectform

.. image:: https://coveralls.io/repos/nagyv/django-collectform/badge.png?branch=master
    :target: https://coveralls.io/r/nagyv/django-collectform?branch=master

A simple app that collects data from a form, and sends it out to managers.

Documentation
-------------

The full documentation is at https://django-collectform.readthedocs.org.

Quickstart
----------

Install django-collectform::

    pip install django-collectform

Then use it in a project::

    import collectform

Features
--------

* Required setting: `COLLECTFORM_RELATED_MODEL` used by `ContentTypeManager.get_by_natural_key`
