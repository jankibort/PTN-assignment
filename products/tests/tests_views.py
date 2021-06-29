from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('allProducts')


    def test_all_products_GET(self):
        client = Client()

        response = client.get(reverse('allProducts'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')