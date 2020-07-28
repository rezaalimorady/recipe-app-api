from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_useer_with_email_successfull(self):
        """test creating user with email successfull"""
        email = 'test@test.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_emai_normalize(self):
        """test email is normalize for new user"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'retere')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test create user with invalid email get error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '2222')

    def test_create_new_superuser(self):
        """test create new super user """
        user = get_user_model().objects.create_superuser('test@test.com', 'password123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_stuff)
