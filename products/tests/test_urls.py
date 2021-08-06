from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import all_products, product_details, add_product, edit_product, delete_product


class Test_urls(SimpleTestCase):

    def test_all_products_resolves(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)
    
    def test_product_details_resolves(self):
        url = reverse('product_details', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_details)
    
    def test_add_product_resolves(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)
    
    def test_edit_product_resolves(self):
        url = reverse('edit_product', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_product)
    
    def test_delete_product_resolves(self):
        url = reverse('delete_product', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_product)
