from django.test import TestCase
from products.models import Category, Product
from django.contrib.auth.models import User


class TestModels(TestCase):
    '''tests models in product app'''
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category",
        )
        self.product = Product.objects.create(
            sku=1,
            name="tests item",
            description="test description",
            price="11.99",
            image="testimg.jpg",
            category=self.category,
        )

    def test_category_model(self):
        """ tests category model"""
        self.assertEqual(str(self.category), "test_category")

    def test_product_model(self):
        """ tests Product model"""
        self.assertEqual(str(self.product), "tests item")
