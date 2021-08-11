from django.test import TestCase
from home import apps


class HomeAppTests(TestCase):

    def test_blog_apps_config(self):
        """ test home app configured correctly"""

        self.assertEqual(apps.HomeConfig.name, 'home')
