from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from django.contrib.messages import get_messages
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.checkout_url = reverse('checkout')

    def test_checkout_GET(self):
        response = self.client.get(self.checkout_url)
        
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You currently have no bag items")
    
    # def test_blog_post_GET(self):
    #     response = self.client.get(self.blog_post_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blog_post.html')

    #     Post.objects.create(
    #         title=self.title1,
    #         user=self.user,
    #     )

    #     response = self.client.post(self.blog_post_url, {

    #     })

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(self.title1, 'banana')
