from django.test import TestCase, Client


class CarModelsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_cars_returns_models(self):
        response = self.client.get('/djangoapp/get_cars')
        self.assertEqual(response.status_code, 200)
        self.assertIn('CarModels', response.json())

    def test_home_page_serves_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dealers_page_serves_index(self):
        response = self.client.get('/dealers')
        self.assertEqual(response.status_code, 200)
