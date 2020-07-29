from django.test import TestCase, RequestFactory,Client
from django.urls import reverse
from django.contrib.auth.models import User
from mixer.backend.django import mixer

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.url="/accounts/login"
        self.data1 = {
            "username": "subham",
            "password1": "root"
            }
        self.data2 = {
            "username": "",
            "password1": ""
            }

    def test_view_redirect_authenticated_user_to_homepage(self):
        #User.objects.create_user(self.username,self.password)
        response=self.client.post(self.url,self.data1)
        print(response)
        self.assertRedirects(response,"/")


    def test_view_redirect_unauthenticated_user_to_login(self):
        response=self.client.post(self.url,self.data2)
        print(response)
        self.assertRedirects(response,"/accounts/login")
