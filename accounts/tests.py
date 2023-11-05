from django.test import TestCase
from django.urls import reverse


class AccountsTest(TestCase):
    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_by_url_name(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_show_signup_title_in_page(self):
        response = self.client.get(reverse('account_signup'))
        self.assertContains(response, 'Sign Up')

    def test_signup_template_use(self):
        response = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_login_page_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_by_url_name(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_show_login_title_in_page(self):
        response = self.client.get(reverse('account_login'))
        self.assertContains(response, 'Log In')

    def test_login_template_use(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'account/login.html')

    def test_logout_page_url(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response, 200)

    def test_logout_page_by_url(self):
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response, 200)

    def test_show_logout_title_in_page(self):
        response = self.client.get(reverse('account_logout'))
        self.assertContains(response, 'Log Out')
        # test failes. don't know why!
    
    def test_logout_template_use(self):
        response = self.client.get('/accounts/logout/')
        self.assertTemplateUsed(response, 'account/logout.html')