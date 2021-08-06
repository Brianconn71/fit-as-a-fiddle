from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home


class Test_urls(SimpleTestCase):

    def test_home_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
