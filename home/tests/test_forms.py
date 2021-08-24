from django.test import TestCase, Client
from home.forms import ContactForm


class TestForms(TestCase):
    """ test profiles forms configured correctly"""
    def test_contact_Form_valid_data(self):
        form = ContactForm(data={
            'subject': 'test title',
            'email': 'test@test.com',
            'message': 'test'
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        form = ContactForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
