from django.shortcuts import resolve_url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import index, new

class TestUrls(SimpleTestCase):

    def test_all_products_url_is_resolved(self):
        url = reverse('allProducts')
        self.assertEquals(resolve(url).func, index)

    def test_new_products_url_is_resolved(self):
        url = reverse('newProducts')
        self.assertEquals(resolve(url).func, new)