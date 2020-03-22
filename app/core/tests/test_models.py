from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_creating_user_with_email(self):
        """Test creating a new user with email is successful"""
        email = 'test@testpew.com'
        password = 'testpew123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email, 'not identical')
        self.assertTrue(user.check_password(password), 'message')

    def test_normalize_email(self):
        """Test the email for the new user is normalized"""
        email = 'test@PEWTEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower(), 'message')

    def test_new_user_valid_email(self):
        """Test creating user with no email rasis error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_super_user_is_created(self):
        """Test that super user is created"""
        user = get_user_model().objects.create_superuser(
            'testsuper@testpew.com',
            'test123'
        )

        self.assertTrue(user.is_superuser, 'message')
        self.assertTrue(user.is_staff, 'message')
