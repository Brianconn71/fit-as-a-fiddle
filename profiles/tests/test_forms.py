from django.test import TestCase, Client
from django.contrib.auth.models import User
from profiles.forms import UserProfileForm


class TestForms(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='Passwordtest'
        )
        self.form = UserProfileForm

    def test_Profile_meta_fields(self):
        form = self.form({
            "user": self.user,
            "default_phone_number": "Contact Number",
            "default_postcode": "1234",
            "default_town_or_city": "Test or test",
            "default_street_address1": "Test",
            "default_street_address2": "Test",
            "default_county": "County",
        })
        self.assertTrue(form.is_valid())

    def test_fields_are_not_required(self):
        form = self.form({})
        self.assertTrue(form.is_valid())