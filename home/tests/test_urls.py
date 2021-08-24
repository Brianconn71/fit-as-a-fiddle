from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, contact


class Test_urls(SimpleTestCase):
    '''test urls are configured correctly'''
    def test_home_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
    
    def test_contact_resolves(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)
