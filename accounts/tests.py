from django.shortcuts import reverse
from django.test import TestCase

from .models import CustomUser


class UserLoginTest(TestCase):
    def setUp(self):
        self.response_by_name = self.client.get(reverse('accounts:login'))

    def test_login_namespace_url(self):
        url = reverse('accounts:login')
        self.assertEqual(url, '/accounts/login/')

    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_url_by_name(self):
        self.assertEqual(self.response_by_name.status_code, 200)

    def test_login_template_use(self):
        self.assertTemplateUsed(self.response_by_name, 'accounts/login.html')

    def test_login_content_exist(self):
        self.assertContains(self.response_by_name, 'Login')  # Login is page title

    def test_login_user(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'uroot',
            'password': 'proot',
        })
        self.assertEqual(response.status_code, 302)


class SignUpTest(TestCase):
    def setUp(self):
        self.response_by_name = self.client.get(reverse('accounts:signup'))

    def test_signup_namespace_url(self):
        url = reverse('accounts:signup')
        self.assertEqual(url, '/accounts/signup/')

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_by_name(self):
        self.assertEqual(self.response_by_name.status_code, 200)

    def test_signup_template_use(self):
        self.assertTemplateUsed(self.response_by_name, 'accounts/signup.html')

    def test_signup_content_exist(self):
        self.assertContains(self.response_by_name, 'Sign Up')  # Sign Up is page title

    def test_signup_user(self):
        response = self.client.post(reverse('accounts:signup'), {
            'username': 'root',
            'password1': 'root_pass1234',  # The password must change from username because we have validation django
            'password2': 'root_pass1234',
            'email': 'root@gmail.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CustomUser.objects.last().username, 'root')


# class UserLogoutView(TestCase):
#     def setUp(self):
#         self.response_by_name = self.client.get(reverse('accounts:logout'))
#
#         self.user = CustomUser.objects.create_user(
#             username='root',
#             password='root_pass1234'
#         )
#
#         self.client.post(reverse('accounts:login'), {
#             'username': 'root',
#             'password': 'root_pass1234'
#         })
#
#     def test_logout_namespace_url(self):
#         url = reverse('accounts:logout')
#         self.assertEqual(url, '/accounts/logout/')
#
#     def test_logout_url(self):
#         response = self.client.get('/accounts/logout/')
#         self.assertEqual(response.status_code, 302)
#
#     def test_logout_url_by_name(self):
#         self.assertEqual(self.response_by_name.status_code, 200)
#
#     def test_logout_template_use(self):
#         self.assertTemplateUsed(self.response_by_name, 'accounts/logout.html')
