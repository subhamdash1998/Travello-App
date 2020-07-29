from django.test import TestCase
from mixer.backend.django import mixer

class TestModels(TestCase):

    def test_destination_having_name(self):
        destination=mixer.blend('travello.Destination',name="defined place")
        assert destination.is_having_name == True

    def test_destination_not_having_name(self):
        destination=mixer.blend('travello.Destination',name="")
        assert destination.is_having_name == False 

    def test_destination_having_price(self):
        destination=mixer.blend('travello.Destination',price=100)
        assert destination.is_having_price == True 

    def test_destination_not_having_price(self):
        destination=mixer.blend('travello.Destination',price=0)
        assert destination.is_having_price == False 