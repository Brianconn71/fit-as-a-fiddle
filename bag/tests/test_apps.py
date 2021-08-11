from django.test import TestCase
from bag import apps


class BagAppTests(TestCase):

    def test_blog_apps_config(self):
        """ test bag app configured correctly"""

        self.assertEqual(apps.BagConfig.name, 'bag')
