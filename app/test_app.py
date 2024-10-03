#app/test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.post('/login', data = dict(username = "admin", password = "password123"))
        self.assertIn(b'Login successful!', response.data)

if __name__ == '__main__':
    unittest.main()