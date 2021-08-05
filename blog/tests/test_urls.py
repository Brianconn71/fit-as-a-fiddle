from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import blog, blog_post, add_blog_post, edit_blog_post, delete_blog_post, delete_comment


class Test_urls(SimpleTestCase):

    def test_blog_resolves(self):
        url = reverse('blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog)
    
    def test_blog_post_resolves(self):
        url = reverse('blog_post', args=['some-text'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog_post)
    
    # def test_adjust_bag_resolves(self):
    #     url = reverse('adjust_bag', args=[2])
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, adjust_bag)
    
    # def test_remove_from_bag_resolves(self):
    #     url = reverse('remove_from_bag', args=[2])
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func, remove_from_bag

