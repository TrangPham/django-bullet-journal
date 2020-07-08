import request

from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    def test_get_task(self):
        response = request.get(reverse("bullets-task"))
        
