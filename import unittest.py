import unittest
from main import app

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_cities_spain(self):
        response = self.app.get('/cities/Spain')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Country not found"})

if __name__ == '__main__':
    unittest.main()