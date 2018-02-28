from django.test import TestCase
from django.test.client import Client, RequestFactory

from datetime import date
import json

from user.factories import UserProfileFactory, UserAuthFactory


class TestEventResource(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_auth = UserAuthFactory(username="user", password="pass", email="user@gmail.com")
        self.user_auth.save()
        self.user = UserProfileFactory(user_auth = self.user_auth, phone = '0123456789', city = 'Eind')
        self.user.save()

    def test_successfully_created_event(self):
        self.client.login(username="user", password="pass")
        event = {
        'name': 'Rock and Roll',
        'category': 'BBQ',
        'event_date': str(date.today())
        }
        response = self.client.post('/event/create/', json.dumps(event),
         content_type='application/json')
        self.assertEqual(response.status_code, 200)
