from django.test import TestCase, RequestFactory,Client
from django.urls import reverse
from django.contrib.auth.models import User
from mixer.backend.django import mixer
#from rest_framework import status

class TestViews(TestCase):
    def setUp(self):
       # self.username="subham111"
       # self.password="valid_password1"
        self.client=Client()
        self.url="http://127.0.0.1:8000/accounts/login"
        

    def test_view_redirect_authenticated_user_to_homepage(self):
        #User.objects.create_user(self.username,self.password)
        data = {
            "username": "subham",
            "password1": "root"
            }
        response=self.client.post(self.url,data)
        print(response)
        self.assertRedirects(response,"/")


    """def test_view_redirect_unauthenticated_user_to_login(self):
        print(self.url)
        response=self.client.post(self.url)
        print(response)
        self.assertRedirects(response,reverse("login"))"""


"""
ef test_special_days_post(self):
        data = json.dumps({
            "title": "api test1",
            "date": "{}-{}-{}".format(str(self.year),str(self.month),str(self.day)),
            "repeat_every_year": True
            })
        response = self.client.post('/api/customers/{}/channels/{}/special-days/'.format(self.customer_id,os.environ['TEST_CHANNEL_ID']), data, content_type='application/json',  HTTP_AUTHORIZATION='JWT ' + self.access_token)
        self.assertEquals(response.status"""