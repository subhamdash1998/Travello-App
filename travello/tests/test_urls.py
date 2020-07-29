from django.urls import reverse,resolve
from django.test import TestCase


class TestUrls(TestCase):
    def test_index_url(self):
        path=reverse("index")
        assert resolve(path).view_name=="index"
    def test_home_url(self):
        path=reverse("home")
        assert resolve(path).view_name=="home"
    def test_contact_url(self):
        path=reverse("contact")
        assert resolve(path).view_name=="contact"
    def test_login_url(self):
        path=reverse("login")
        assert resolve(path).view_name=="login"
    def test_register_url(self):
        path=reverse("register")
        assert resolve(path).view_name=="register"
    def test_logout_url(self):
        path=reverse("logout")
        assert resolve(path).view_name=="logout"
