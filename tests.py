from typing import List
import unittest
import requests


class TestUserApi(unittest.TestCase):

    BASE_URL = 'http://127.0.0.1:5000'

    def setUp(self):
        self.session = requests.session()

    def test_user_list(self):
        path = '/users'
        url = self.BASE_URL + path
        response = self.session.get(url)
        data = response.json()
        self.assertIn("users", data)
        users = data['users']
        self.assertIsInstance(users, list)

    def test_user_create(self):
        path = '/users'
        url = self.BASE_URL + path
        data = {
            "name": "Jackson",
            "job_title": "PM",
        }
        response = self.session.post(url, data)
        self.assertEqual(response.status_code, 201)
        print(response.json())
        self.assertEqual(response.json(), data)


if __name__ == '__main__':
    unittest.main()
