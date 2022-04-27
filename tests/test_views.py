from django.test import TestCase, Client
from django.urls import reverse
from userpage.models import User, Post, Comment, Like, Friendlink
import json


class TestViews(TestCase):

    def test_index_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'userpage/index.html')

    def test_index_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'userpage.html')

    def test_index_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin.html')

    def test_index_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'userpage/post.html')