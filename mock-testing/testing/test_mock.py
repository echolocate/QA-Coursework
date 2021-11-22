import requests_mock
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_football(self):
    # We will mock a response of 1 and test that we get football returned.
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number', text="1")
            m.get('http://api:5000/get/letter', text="a")
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)

        with patch('requests.get') as m:
            m.get('http://api:5000/get/number', text="1")
            m.get('http://api:5000/get/letter', text="b")
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Badminton', response.data)

        with patch('requests.get') as m:
            m.get('http://api:5000/get/number', text="1")
            m.get('http://api:5000/get/letter', text="c")
            response = self.client.get(url_for('sport'))
            self.assertIn(b'Hockey', response.data)

        with patch('requests.get') as m:
            m.get('http://api:5000/get/number', text="4")
            m.get('http://api:5000/get/letter', text="d")
            self.assertIn(b'Boxing', response.data)