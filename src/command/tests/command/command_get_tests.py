from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient

import pytest
import json

from ...models.command import Command

from .command_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestGetCommandRequests:

    # テストクラスで利用するプロパティ
    #     client: APIクライアント
    #     TARGET_URL: テストで利用するAPIエンドポイント
    @pytest.fixture()
    def props(self):
        client = APIClient()
        return {
            'TARGET_URL': '/api/v1/commands/',
            'client': client
        }
    
    # 参照するオブジェクトのID要素を取得
    # Reference Object(object_id) 形式で記述されるので、固定で取得
    def get_reference_object_id(self, reference_object_str):

        start = reference_object_str.find('(') +1
        end = reference_object_str.find(')')
        
        return reference_object_str[start:end]

    def test_GETリクエストでステータスコード200が得られる(self, props, single_command):

        response = props['client'].get(props['TARGET_URL'])

        assert response.status_code == 200

    def test_GETリクエストでコマンドが読みだせる(self, props, single_command):

        response = props['client'].get(props['TARGET_URL'])

        actual = {
            'command_id': response.data[0]['command_id'],
            'command_category_id': self.get_reference_object_id(response.data[0]['command_category_id']),
            'category_id': self.get_reference_object_id(response.data[0]['category_id']),
            'command_name': response.data[0]['command_name'],
            'memo': response.data[0]['memo']
        }
        expected = {
            'command_id': single_command.command_id,
            'command_category_id': single_command.command_category_id.command_category_id,
            'category_id': single_command.category_id.category_id,
            'command_name': single_command.command_name,
            'memo': single_command.memo
        }

        assert actual == expected

    def test_GETリクエストで複数コマンドが取得できる(self, props, multiple_command):

        response = props['client'].get(props['TARGET_URL'])

        assert len(response.data) == 3
        assert len(multiple_command) == 3

    def test_GETリクエストでコマンド名が昇順でソートされる(self, props, unordered_command, ordered_command):

        response = props['client'].get(props['TARGET_URL'])

        for index, command in enumerate(ordered_command):
            actual = response.data[index]['command_name']
            expected = command.command_name

            assert actual == expected