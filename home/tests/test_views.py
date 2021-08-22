from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    '''test home views are configured correctly'''
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.home_url = reverse('home')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')