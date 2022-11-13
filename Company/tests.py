from django.test import TestCase , Client
from django.urls import reverse


# Create your tests here.
class TestViews(TestCase):
    
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('assets'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset.html')
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'logout.html')
    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('addEmployee'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'addEmployee.html')
