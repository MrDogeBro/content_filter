.. Content Filter documentation master file, created by
   sphinx-quickstart on Mon Nov  9 21:32:52 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Content Filter Documentation
============================

.. image:: https://travis-ci.com/MrDogeBro/content_filter.svg?token=K4YBJnRBuxqyhssWYMJt&branch=master
   :alt: Build Status
   :target: https://travis-ci.com/github/MrDogeBro/content_filter

.. image:: https://readthedocs.org/projects/content-filter/badge/?version=latest
   :target: https://content-filter.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/content-filter.svg
   :alt: PyPi version
   :target: https://pypi.python.org/pypi/content-filter/

.. image:: https://img.shields.io/pypi/pyversions/content-filter.svg
   :alt: PyPI pyversions
   :target: https://pypi.python.org/pypi/content-filter/

.. image:: https://img.shields.io/github/license/MrDogeBro/content_filter.svg
   :alt: License
   :target: https://github.com/MrDogeBro/content_filter/blob/master/LICENSE

Content Filter is a basic but robust content filter for python. Content Filter allows you to easily detect language in a message and offers great customizability.

Features
--------

- Ability to have different levels of filtration.
- Can ignore repeated characters and infer certain characters aliases.
- Converts non-english characters to their english equivalents such as ç to c.
- Ignores non-printing characters.
- Easily and very customizable.
- Easy to get up and running.
- No third-party dependencies.

User Guide
----------

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart
   user/usage
   user/examples

API Docs
--------

.. toctree::
   :maxdepth: 2

   api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
