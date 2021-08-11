from django.test import TestCase
from checkout import apps


class CheckoutAppTests(TestCase):

    def test_blog_apps_config(self):
        """ test checkout app configured correctly"""

        self.assertEqual(apps.CheckoutConfig.name, 'checkout')
