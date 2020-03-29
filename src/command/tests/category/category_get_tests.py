from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient

import pytest
import json

from ...models.category import Category

from .category_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestGetCategoryRequests:

    # テストクラスで利用するプロパティ
    #     client: APIクライアント
    #     TARGET_URL: テストで利用するAPIエンドポイント
    @pytest.fixture()
    def props(self):
        client = APIClient()
        return {
            'TARGET_URL': '/api/v1/categories/',
            'client': client
        }

    def test_GETリクエストでステータスコード200が得られる(self, props, single_category):

        response = props['client'].get(props['TARGET_URL'])

        assert response.status_code == 200

    def test_GETリクエストでカテゴリが読みだせる(self, props, single_category):

        response = props['client'].get(props['TARGET_URL'])

        actual = {'category_id': response.data[0]['category_id'], 'category_name': response.data[0]['category_name']}
        expected = {'category_id': single_category.category_id, 'category_name': single_category.category_name}

        assert actual == expected

    def test_GETリクエストで複数カテゴリが取得できる(self, props, multiple_categories):

        response = props['client'].get(props['TARGET_URL'])

        assert len(response.data) == 2
        assert len(multiple_categories) == 2

    def test_GETリクエストでカテゴリ名が昇順でソートされる(self, props, unordered_categories, ordered_categories):

        response = props['client'].get(props['TARGET_URL'])

        for index, category in enumerate(ordered_categories):
            actual = response.data[index]['category_name']
            expected = category.category_name

            assert actual == expected