from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LogoutViewTests(TestCase):
    def test_logout_redirects_to_login_page(self):
        user = get_user_model().objects.create_user(username='tester', password='12345')
        self.client.force_login(user)

        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('login'))
