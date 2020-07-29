from django.test import TestCase,Client
from django.urls import reverse


class TestViewsRegister(TestCase):
    def setUp(self):
        self.client=Client()
        self.url="http://127.0.0.1:8000/accounts/register"
        self.data1 = {
        "first_name":"Nabin",
        "last_name":"Kumar",
        "username":"nabin",
        "password1":"nabin",
        "password2":"nabin",
        "email":"nabin@gamil.com",
        }
        self.data2 = {
        "first_name":"Nabin",
        "last_name":"Kumar",
        "username":"nabin",
        "password1":"na",
        "password2":"nagjvh",
        "email":"nabin@gamil.com",
        }
    def test_check_user_details_for_valid_redirect_to_loginpage(self):
        response=self.client.post(self.url,self.data1)
        print(response)
        self.assertRedirects(response,"/accounts/login")
    
    def test_check_user_details_for_invalid_password_redirect_to_register_page(self):
        response=self.client.post(self.url,self.data2)
        print(response)
        self.assertRedirects(response,"/accounts/register")

