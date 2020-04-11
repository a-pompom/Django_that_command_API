from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient

import pytest
import json

from ...models.category import Category
from ...models.command_category import CommandCategory

from .command_category_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestGetCommandCategoryRequests:

    # テストクラスで利用するプロパティ
    #     client: APIクライアント
    #     TARGET_URL: テストで利用するAPIエンドポイント
    @pytest.fixture()
    def props(self):
        client = APIClient()
        return {
            'TARGET_URL': '/api/v1/command_categories/',
            'client': client
        }
    
    # 参照するオブジェクトのID要素を取得
    # Reference Object(object_id) 形式で記述されるので、固定で取得
    def get_reference_object_id(self, reference_object_str):

        start = reference_object_str.find('(') +1
        end = reference_object_str.find(')')
        
        return reference_object_str[start:end]

    def test_GETリクエストでステータスコード200が得られる(self, props, single_command_category):

        response = props['client'].get(props['TARGET_URL'])

        assert response.status_code == 200

    def test_GETリクエストでコマンドカテゴリが読みだせる(self, props, single_command_category):

        response = props['client'].get(props['TARGET_URL'])

        actual = {
            'command_category_id': response.data[0]['command_category_id'],
            'category_id': self.get_reference_object_id(response.data[0]['category_id']),
            'command_category_name': response.data[0]['command_category_name']
        }
        expected = {
            'command_category_id': single_command_category.command_category_id,
            'category_id': single_command_category.category_id.category_id,
            'command_category_name': single_command_category.command_category_name
        }

        assert actual == expected

    def test_GETリクエストで複数コマンドカテゴリが取得できる(self, props, multiple_command_categories):

        response = props['client'].get(props['TARGET_URL'])

        assert len(response.data) == 3
        assert len(multiple_command_categories) == 3

    def test_GETリクエストでコマンドカテゴリ名が昇順でソートされる(self, props, unordered_command_categories, ordered_command_categories):

        response = props['client'].get(props['TARGET_URL'])

        for index, command_category in enumerate(ordered_command_categories):
            actual = response.data[index]['command_category_name']
            expected = command_category.command_category_name

            assert actual == expected