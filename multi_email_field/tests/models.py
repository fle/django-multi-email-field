from django.db import models

from multi_email_field.fields import MultiEmailField


class TestModel(models.Model):
    f = MultiEmailField(null=True, blank=True)
