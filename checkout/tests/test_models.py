from django.test import TestCase
from checkout.models import Order, OrderLineItem
from products.models import Product
from django.contrib.auth.models import User


class TestModels(TestCase):
    ''' test models in checkout are configured'''
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.order = Order.objects.create(
            full_name="Test User"
        )

    def test_order_model(self):
        """ tests the order model """
        self.assertEqual(str(self.order), self.order.order_number)

    def test_orderlineitem_model(self):
        """ tests the orderlineitem model """

        product = Product.objects.create(
            name='Test Product',
            price=100,
            sku=123,
        )

        order_line_item = OrderLineItem.objects.create(
            order=self.order,
            product=product,
            quantity=1,
            lineitem_total=100,
        )

        self.assertEqual(str(order_line_item),
                         f"SKU 123 on order {self.order.order_number}")
