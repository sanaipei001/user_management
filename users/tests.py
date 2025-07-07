from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.profile = UserProfile.objects.create(user=self.user, bio='Test bio')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.bio, 'Test bio')

    def test_verification_token(self):
        token = self.profile.generate_verification_token()
        self.assertTrue(len(token) == 50)
        self.assertEqual(UserProfile.objects.get(user=self.user).verification_token, token)

class UserViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.profile = UserProfile.objects.create(user=self.user, bio='Test bio')  # Added UserProfile creation

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)