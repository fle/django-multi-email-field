import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="django-multi-email-field",
    version="0.6.2",
    author="Florent Lebreton",
    author_email="florent.lebreton@makina-corpus.com",
    url="https://github.com/fle/django-multi-email-field",
    description="Provides a model field and a form field to manage list of e-mails",
    long_description=open(os.path.join(here, "README.rst")).read()
    + "\n\n"
    + open(os.path.join(here, "CHANGES")).read(),
    license="LGPL, see LICENSE file.",
    install_requires=["Django"],
    packages=find_packages(),
    extras_require={
        "dev": ["django", "pyquery", "coverage", "black", "ruff"],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Topic :: Utilities",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
