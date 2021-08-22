from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import cache_checkout_data, checkout, checkout_success


class Test_urls(SimpleTestCase):
    ''' test urls in checkout are configured'''
    def test_cache_checkout_data_resolves(self):
        url = reverse('cache_checkout_data')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cache_checkout_data)

    def test_checkout_resolves(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

    def test_checkout_success_resolves(self):
        url = reverse('checkout_success', args=[3])
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout_success)
