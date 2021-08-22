from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.utils import timezone

class RevampTest(TestCase):
   def setUp(self):
       self.client = Client()
   def test_index_page(self):
       url = reverse('home')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'revamp/index.html')
   def test_about_page(self):
       url = reverse('about')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'revamp/about.html')
   def test_contact_page(self):
       url = reverse('contact')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'revamp/contact.html')
   def test_pelatihan_page(self):
       url = reverse('pelatihan')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'revamp/pelatihan.html')