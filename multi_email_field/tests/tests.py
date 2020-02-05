from pyquery import PyQuery as pq

from django import forms
from django.core.exceptions import ValidationError
from django.test import SimpleTestCase, TestCase

from multi_email_field.forms import MultiEmailField as MultiEmailFormField
from multi_email_field.tests.models import TestModel
from multi_email_field.widgets import MultiEmailWidget


class MultiEmailFormTest(SimpleTestCase):
    def test__form(self):
        class TestForm(forms.Form):
            f = MultiEmailFormField()

        form = TestForm(initial={'f': ['foo@foo.fr', 'bar@bar.fr']})
        output = form.as_p()
        self.assertEqual(1, len(pq('textarea', output)))
        # The template-based widget add a line-return
        value = pq('textarea', output).text()
        self.assertEqual(
            value.lstrip(),
            'foo@foo.fr\nbar@bar.fr'
        )


class MultiEmailModelFormTest(TestCase):
    def test__model_form(self):
        class TestModelForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = forms.ALL_FIELDS

        form = TestModelForm()
        self.assertIsInstance(form.fields['f'].widget, MultiEmailWidget)

        form = TestModelForm(data={'f': 'foo@foo.fr\nbar@bar.fr'})
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertEqual(instance.f, ['foo@foo.fr', 'bar@bar.fr'])

        form = TestModelForm(instance=instance)
        output = form.as_p()
        self.assertEqual(1, len(pq('textarea', output)))
        # The template-based widget add a line-return
        value = pq('textarea', output).text()
        self.assertEqual(
            value.lstrip(),
            'foo@foo.fr\nbar@bar.fr',
        )


class MultiEmailFormFieldTest(SimpleTestCase):

    def test__widget(self):
        f = MultiEmailFormField()
        self.assertIsInstance(f.widget, MultiEmailWidget)

    def test__to_python(self):
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

    def test__validate(self):
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


class MultiEmailWidgetTest(SimpleTestCase):

    def test__prep_value__empty(self):
        w = MultiEmailWidget()
        value = w.prep_value('')
        self.assertEqual(value, '')

    def test__prep_value__string(self):
        w = MultiEmailWidget()
        value = w.prep_value('foo@foo.fr\nbar@bar.fr')
        self.assertEqual(value, 'foo@foo.fr\nbar@bar.fr')

    def test__prep_value__list(self):
        w = MultiEmailWidget()
        value = w.prep_value(['foo@foo.fr', 'bar@bar.fr'])
        self.assertEqual(value, 'foo@foo.fr\nbar@bar.fr')

    def test__prep_value__raise(self):
        w = MultiEmailWidget()
        self.assertRaises(ValidationError, w.prep_value, 42)

    def test__render(self):
        w = MultiEmailWidget()
        output = w.render('test', ['foo@foo.fr', 'bar@bar.fr'])
        self.assertEqual(1, len(pq('textarea', output)))
        # The template-based widget add a line-return
        value = pq('textarea', output).text()
        self.assertEqual(
            value.lstrip(),
            'foo@foo.fr\nbar@bar.fr'
        )
