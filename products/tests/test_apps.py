from django.test import TestCase
from products import apps


class ProductsAppTests(TestCase):

    def test_products_apps_config(self):
        """ test products app configured correctly"""

        self.assertEqual(apps.ProductsConfig.name, 'products')
