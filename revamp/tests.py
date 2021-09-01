from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from .models import Contact, Pelatihan
from .forms import ContactForm, PelatihantForm
from django.contrib.messages import get_messages

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
    response = self.client.post(url, data={"name": "coba", "email": "coba@gmail.com", "message": "coba di coba"})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'revamp/contact.html')

  def test_course_page(self):
    url = reverse('course')
    response = self.client.post(url, data={
      "name": "coba", "email": "coba@gmail.com", 
      "hp":"085677889900", "study":"SMA", "jurusan":"TI", 
      "gender": 1, "reason": "belajar"})
    self.assertEqual(response.status_code, 200)
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

