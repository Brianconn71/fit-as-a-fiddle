from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.view_bag_url = reverse('view_bag')

    def test_view_bag_GET(self):
        response = self.client.get(self.view_bag_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
