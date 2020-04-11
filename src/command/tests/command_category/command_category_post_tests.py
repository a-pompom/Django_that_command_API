from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient
from django.shortcuts import get_object_or_404

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
            'TARGET_URL': '/api/v1/command_category/',
            'client': client
        }

    def test_POSTリクエストで新規コマンドカテゴリが登録される(self, props, single_command_category):

        params = {
            'category_id': single_command_category.category_id.category_id,
            'command_category_name': 'post_command_category'
        }

        response = props['client'].post(props['TARGET_URL'], params, format='json')

        command_category = CommandCategory.objects.filter(command_category_name='post_command_category')

        assert response.status_code == 201
        assert command_category[0].command_category_name == params['command_category_name']