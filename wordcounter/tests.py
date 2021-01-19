from django.test import TestCase
from django.urls import reverse

class WordCounter(TestCase):
    
    def test_home_view(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"WORD COUNTER")
        self.assertTemplateUsed(response,'home.html')
    
    def test_about_view(self):
        response=self.client.get(reverse('about'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"hey! here You can counte the words of your text.")
        self.assertTemplateUsed(response,'about.html')
