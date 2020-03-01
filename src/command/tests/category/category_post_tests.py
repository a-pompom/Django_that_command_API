from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient

import pytest
import json

from ...models.category import Category

from .category_get_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestGetCategoryRequests:

    # テストクラスで利用するプロパティ
    #     client: APIクライアント
    #     TARGET_URL: テストで利用するAPIエンドポイント
    @pytest.fixture()
    def props(self):
        client = APIClient()
        return {
            'TARGET_URL': '/api/v1/category/',
            'client': client
        }

    def test_POSTリクエストでステータスコード201が得られる(self, props, single_category):

        params = {
            'category_id': '90811bb8-00bd-46b1-839b-cab9c3b571903',
            'category_name': 'post_category'
        }

        response = props['client'].post(props['TARGET_URL'], params, format='json')

        print(response.data)

        assert response.status_code == 201