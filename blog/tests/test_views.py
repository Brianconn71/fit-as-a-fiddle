from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.blog_url = reverse('blog')
        self.blog_post_url = reverse('blog_post', args=['sometext'])
        self.sometext = Post.objects.create(
            title='sometext',
            user=self.user,
        )


    def test_blog_GET(self):
        response = self.client.get(self.blog_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
    
    def test_blog_post_GET(self):
        response = self.client.get(self.blog_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_post.html')
    
    def test_blog_post_POST_adds_new_post(self):
        Post.objects.create(
            title=self.title1,
            user=self.user,
        )

        response = self.client.post(self.blog_post_url, {

        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(self.title1, 'banana')
