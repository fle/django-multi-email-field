Field and widget to store a list of e-mail addresses in a `Django <https://www.djangoproject.com>`_ projects.

It provides:

* A form field and a form widget to edit a list of e-mails in a Django form;
* A model field to store the captured list of e-mails;

==================
COMPATIBILITY
==================

* Python 2.7/3.3/3.4/3.5
* Django 1.8/1.9/1.10

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

* Use provided form field and widget:

::

    # forms.py
    from django import forms
    from multi_email_field.forms import MultiEmailField

    class SendMessageForm(forms.Form):
        emails = MultiEmailField()

==================
IN YOUR MODELS
==================

If you wan to store list of e-mails, you can use this:

::

    from django.db import models
    from multi_email_field.fields import MultiEmailField

    class ContactModel(models.Model):
        emails = MultiEmailField()


==================
AUTHORS
==================

    * Florent Lebreton <florent.lebreton@makina-corpus.com>

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

