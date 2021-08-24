from django.test import TestCase
from home.models import Contact


class TestModels(TestCase):
    ''' test models are correct'''
    def test_Contact_model(self):
        contact = Contact.objects.create(
            subject="Test Subject",
            email="Test@test.com",
            message="Test Message",
        )
        self.assertEqual(str(contact), "Test Subject")
