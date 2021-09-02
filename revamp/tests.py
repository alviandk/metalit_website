from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.messages import get_messages
from .models import Contact, Pelatihan
from .forms import ContactForm, PelatihantForm


class RevampTest(TestCase): 
  def setUp(self):
    self.client = Client()

  def test_home_page(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'revamp/home.html')

  def test_about_page(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'revamp/about.html')

  def test_contact_page(self):
    url = reverse('contact')
    data = {"name": "coba", "email": "coba@gmail.com", "message": "coba di coba"}
    response = self.client.post(url, data=data)
    self.assertEqual(response.status_code, 200)
    all_messages = [msg for msg in get_messages(response.wsgi_request)]
    self.assertEqual(all_messages[0].tags, "alert-success")
    self.assertEqual(all_messages[0].message, "pesan berhasil terkirim")
    self.assertTemplateUsed(response, 'revamp/contact.html')

  def test_course_page(self):
    url = reverse('course')
    data = {
      "nama": "coba", 
      "email": "coba@gmail.com", 
      "hp":"085677889900", 
      "study":"SMA",
      "jurusan":"TI", 
      "gender": 1, 
      "reason": "belajar"
      }
    response = self.client.post(url, data=data)
    self.assertEqual(response.status_code, 200)
    all_messages = [msg for msg in get_messages(response.wsgi_request)]
    self.assertEqual(all_messages[0].tags, "alert-success")
    self.assertEqual(all_messages[0].message, "pesan berhasil terkirim")
    self.assertTemplateUsed(response, 'revamp/course.html')

  def test_help_page(self):
    url = reverse('help')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'revamp/help.html')

  def test_privacy_policy_page(self):
    url = reverse('privacy-policy')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'revamp/privacy-policy.html')

  def test_term_conditions_page(self):
    url = reverse('term-conditions')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'revamp/term-conditions.html')