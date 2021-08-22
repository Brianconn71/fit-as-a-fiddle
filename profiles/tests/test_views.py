from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    """ test profiles views configured correctly"""
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.profile_url = reverse('profile')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertNotEquals(response.status_code, 200)
