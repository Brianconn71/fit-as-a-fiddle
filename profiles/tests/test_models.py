from django.test import TestCase
from profiles.models import UserProfile
from django.contrib.auth.models import User


class TestModels(TestCase):
    """ test profiles model configured correctly"""
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = UserProfile.objects.get(
            user=self.user,
        )

    def test_userprofile_model(self):
        self.client.login(username='testuser', password='testpassword')

        self.assertEquals(str(self.profile), 'testuser')
