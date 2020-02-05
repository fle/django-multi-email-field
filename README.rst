|build| |coverage| |pypi|

Field and widget to store a list of e-mail addresses in a `Django <https://www.djangoproject.com>`_ project.

It provides:

* A form field and a form widget to edit a list of e-mails in a Django form;
* A model field to store the captured list of e-mails;

==================
COMPATIBILITY
==================

* Python 2.7 and 3.5+
* Django 1.8+, 2.0+ and 3.0+

==================
INSTALL
==================

For now:

::

    pip install django-multi-email-field

==================
USAGE
==================

* Add ``multi_email_field`` to your ``INSTALLED_APPS``:

::

    # settings.py
    INSTALLED_APPS = (
    ...
    'multi_email_field',
    )

* Use the provided form field and widget:

::

    # forms.py
    from django import forms
    from multi_email_field.forms import MultiEmailField

    class SendMessageForm(forms.Form):
        emails = MultiEmailField()

==================
IN YOUR MODELS
==================

If you want to store a list of e-mails, you can use this:

::

    from django.db import models
    from multi_email_field.fields import MultiEmailField

    class ContactModel(models.Model):
        emails = MultiEmailField()


==================
AUTHORS
==================

    * Created by `Florent Lebreton <https://github.com/fle/>`_
    * Maintained by `Makina Corpus <https://github.com/makinacorpus/>`_

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. |coverage| image:: https://coveralls.io/repos/github/fle/django-multi-email-field/badge.svg?branch=master
    :target: https://coveralls.io/github/fle/django-multi-email-field?branch=master
.. |pypi| image:: https://pypip.in/v/django-multi-email-field/badge.png
    :target: https://crate.io/packages/django-multi-email-field/
.. |build| image:: https://travis-ci.org/fle/django-multi-email-field.svg?branch=master
    :target: https://travis-ci.org/fle/django-multi-email-field
.. _makinacom:  http://www.makina-corpus.com
