from django.test import TestCase , Client
from django.urls import reverse 
from .views import addAsset, assign
# Create your tests here.
class TestViews(TestCase):
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('addAsset'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'addAsset.html')
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('asset_assign'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'assign.html')