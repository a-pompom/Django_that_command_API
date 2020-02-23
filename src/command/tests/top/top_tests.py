from rest_framework.test import APITestCase
from django.urls import reverse
import json

class GetTopRequests(APITestCase):

    def test_GETリクエストでステータスコード200が得られる(self):

        TARGET_URL = '/api/v1/command/'

        response = self.client.get(TARGET_URL, None, format='json')

        self.assertEqual(response.status_code, 200)