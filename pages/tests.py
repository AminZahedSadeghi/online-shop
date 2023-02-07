from django.test import TestCase
from django.shortcuts import reverse


class HomePageTest(TestCase):
    def setUp(self):
        self.response_by_name = self.client.get(reverse('pages:home'))

    def test_namespace_url(self):
        url = reverse('pages:home')
        print(url)
        self.assertEqual(url, '/')

    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_by_name(self):
        self.assertEqual(self.response_by_name.status_code, 200)

    def test_home_page_template_use(self):
        self.assertTemplateUsed(self.response_by_name, 'home.html')


class AboutUsTest(TestCase):
    def setUp(self):
        self.response_by_name = self.client.get(reverse('pages:aboutus'))

    def test_namespace_url(self):
        url = reverse('pages:aboutus')
        self.assertEqual(url, '/aboutus/')

    def test_aboutus_page_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_url_by_name(self):
        self.assertEqual(self.response_by_name.status_code, 200)

    def test_aboutus_page_template_use(self):
        self.assertTemplateUsed(self.response_by_name, 'pages/aboutus.html')
