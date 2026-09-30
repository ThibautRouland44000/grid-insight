from rest_framework.test import APITestCase


class TestConnection(APITestCase):
    def test_connection_back_front(self):
        response=self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")