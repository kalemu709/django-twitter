from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

LOGIN_URL = '/api/accounts/signin/'
LOGIN_STATUS_URL = '/api/accounts/login_status/'
LOGOUT_URL = '/api/accounts/logout/'
SIGNUP_URL = '/api/accounts/signup/'


class AccountApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self.createUser(
            username='admin',
            email='admin@jiuzhang.com',
            password='12345',
        )

    def createUser(self, username, email, password):
        return User.objects.create_user(username, email, password)

    def test_login(self):
        response = self.client.get(LOGIN_URL, {"username": "admin", "password": "12345"})
        self.assertEqual(response.status_code, 405)
        response = self.client.post(LOGIN_URL, {
            'username': 'admin',
            'password': 'wrong password',
        })
        self.assertEqual(response.status_code, 400)
        response = self.client.post(LOGIN_URL, {
            'username': 'admin',
            'password': '12345',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['logged in user'],{'username':'admin','password': '12345'})

    def test_login_status(self):
        response = self.client.get(LOGIN_STATUS_URL,{})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['user authenticated'],False)
        self.client.post(LOGIN_URL,{'username':'admin','password':'12345'})
        response =self.client.get(LOGIN_STATUS_URL,{})
        self.assertEqual(response.data['user authenticated'], True)

    def test_logout(self):
        self.client.post(LOGIN_URL, {'username': 'admin', 'password': '12345'})
        response = self.client.get(LOGIN_STATUS_URL, {})
        self.assertEqual(response.data['user authenticated'], True)
        response = self.client.post(LOGOUT_URL)
        response = self.client.get(LOGIN_STATUS_URL, {})
        self.assertEqual(response.data['user authenticated'], False)

    def test_signup(self):
        self.client.post(SIGNUP_URL,{'username':'kalemu','password':'12345','email' : 'kalemu@gmail.com'})
        response = self.client.get(LOGIN_STATUS_URL)
        self.assertEqual(response.data['user authenticated'], False)
        self.client.post(LOGIN_URL,{'username':'kalemu','password':'12345'})
        response = self.client.get(LOGIN_STATUS_URL)
        self.assertEqual(response.data['user authenticated'], True)




