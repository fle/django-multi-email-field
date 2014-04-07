from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from multi_email_field.forms import MultiEmailField as MultiEmailFormField
from multi_email_field.widgets import MultiEmailWidget


class MultiEmailFormFieldTest(SimpleTestCase):

    def test_widget(self):
        f = MultiEmailFormField()
        self.assertIsInstance(f.widget, MultiEmailWidget)

    def test_to_python(self):
        f = MultiEmailFormField()
        # Empty values
        for val in ['', None]:
            self.assertEquals([], f.to_python(val))
        # One line correct value
        val = '  foo@bar.com    '
        self.assertEquals(['foo@bar.com'], f.to_python(val))
        # Multi lines correct values (test of #0010614)
        val = 'foo@bar.com\nfoo2@bar2.com\r\nfoo3@bar3.com'
        self.assertEquals(['foo@bar.com', 'foo2@bar2.com', 'foo3@bar3.com'],
                          f.to_python(val))

    def test_validate(self):
        f = MultiEmailFormField(required=True)
        # Empty value
        val = []
        self.assertRaises(ValidationError, f.validate, val)
        # Incorrect value
        val = ['not-an-email.com']
        self.assertRaises(ValidationError, f.validate, val)
        # An incorrect value with correct values
        val = ['foo@bar.com', 'not-an-email.com', 'foo3@bar3.com']
        self.assertRaises(ValidationError, f.validate, val)
        # Should not happen (to_python do the strip)
        val = ['  foo@bar.com    ']
        self.assertRaises(ValidationError, f.validate, val)
        # Correct value
        val = ['foo@bar.com']
        f.validate(val)
