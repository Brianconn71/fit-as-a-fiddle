from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile, order_history


class Test_urls(SimpleTestCase):
    """ test profiles urls configured correctly"""
    def test_profile_resolves(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_order_history_resolves(self):
        url = reverse('order_history', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, order_history)
