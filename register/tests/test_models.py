from django.test import TestCase
from register.models import CustomUser


def create_custom_user(username, email):
    """ Create user for test model CustomUser """

    return CustomUser.objects.create_user(username=username, email=email)


class CustomUserModelTestCase(TestCase):
    def setUp(self):
        """ Set up non-modified obj used by all test """
        self.user = create_custom_user(username='babcool', email='bab.cool@test.com')
        self.custom_user = {
            'username': self.user.username,
            'username_label': self.user._meta.get_field('username').verbose_name,
            'email': self.user.email,
            'email_label': self.user._meta.get_field('email').verbose_name,
            'limit': self.user.limit,
            'limit_label': self.user._meta.get_field('limit').verbose_name,
            'genre': self.user.genre,
            'genre_label': self.user._meta.get_field('genre').verbose_name,
        }

    def test_label_and_result_username(self):
        """ test field username label and result """
        self.assertEqual(self.custom_user['username_label'], 'nom d’utilisateur')
        self.assertEqual(self.custom_user['username'], 'babcool')

    def test_label_and_result_email(self):
        """ test field email label and result """
        self.assertEqual(self.custom_user['email_label'], 'adresse électronique')
        self.assertEqual(self.custom_user['email'], 'bab.cool@test.com')

    def test_label_and_result_limit(self):
        """ test field limit label and result in default value """
        self.assertEqual(self.custom_user['limit_label'], 'limit')
        self.assertEqual(self.custom_user['limit'], 1)

    def test_label_and_result_genre(self):
        """ test field genre label and result in default value """
        self.assertEqual(self.custom_user['genre_label'], 'genre')
        self.assertEqual(self.custom_user['genre'], 'O')
