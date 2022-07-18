from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock


from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_football(self):
    # We will mock a response of 1 and test that we get football returned.
        with patch('requests.get') as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)
    def test_badminton(self):
        with patch('requests.get') as g:
            g.return_value.text = "2"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Badminton', response.data)
    def test_hockey(self):
        with patch('requests.get') as g:
            g.return_value.text = "3"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Hockey', response.data)
    def test_boxing(self):
        with patch('requests.get') as g:
            g.return_value.text = "4"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Boxing', response.data)

class Test2(TestBase):
    def test_football2(self):
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number', text='1')
            m.get('http://api:5000/get/letter', text='a')
            response = self.client.get(url_for('sport2'))
            self.assertIn(b'Football', response.data)
    def test_badminton2(self):
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number', text='1')
            m.get('http://api:5000/get/letter', text='b')
            response = self.client.get(url_for('sport2'))
            self.assertIn(b'Badminton', response.data)
    def test_hockey2(self):
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number', text='1')
            m.get('http://api:5000/get/letter', text='c')
            response = self.client.get(url_for('sport2'))
            self.assertIn(b'Hockey', response.data)
    def test_boxing2(self):
        with requests_mock.Mocker() as m:
            m.get('http://api:5000/get/number', text='1')
            m.get('http://api:5000/get/letter', text='d')
            response = self.client.get(url_for('sport2'))
            self.assertIn(b'Boxing', response.data)

    