from django.db import models

from multi_email_field.forms import MultiEmailField as MultiEmailFormField


class MultiEmailField(models.Field):
    description = "A multi e-mail field stored as a multi-lines text"

    __metaclass__ = models.SubfieldBase

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': MultiEmailFormField}
        defaults.update(kwargs)
        return super(MultiEmailField, self).formfield(**defaults)

    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return "\n".join(value)

    def to_python(self, value):
        if not value:
            return []
        if isinstance(value, list):
            return value
        return value.splitlines()

    def get_internal_type(self):
        return 'TextField'


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["multi_email_field.fields.MultiEmailField"])
except ImportError:
    pass
