from django.test import TestCase
from profiles import apps


class ProfilesAppTests(TestCase):

    def test_profiles_apps_config(self):
        """ test profiles app configured correctly"""

        self.assertEqual(apps.ProfilesConfig.name, 'profiles')
