# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="rframe",
    version="0.1.2",
    description="Top-level package for rframe.",
    python_requires=">=3.8",
    project_urls={"homepage": "https://github.com/jmosbacher/rframe"},
    author="Yossi Mosbacher",
    author_email="joe.mosbacher@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["rframe = rframe.cli:main"]},
    packages=["rframe", "rframe.indexers", "rframe.indexes"],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        "click",
        "pandas==1.*,>=1.4.0",
        "pydantic==1.*,>=1.9.0",
        "toolz==0.*,>=0.11.2",
    ],
    extras_require={
        "dev": [
            "bumpversion",
            "coverage",
            "flake8",
            "invoke==1.*,>=1.6.0",
            "isort",
            "nbsphinx",
            "pylint",
            "pytest",
            "sphinx",
            "sphinx-material",
            "tox",
            "yapf",
        ]
    },
)
