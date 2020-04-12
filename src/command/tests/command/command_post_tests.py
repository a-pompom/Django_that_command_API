from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient
from django.shortcuts import get_object_or_404

import pytest
import json

from ...models.command import Command

from .command_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestPostCommandRequests:

    # テストクラスで利用するプロパティ
    #     client: APIクライアント
    #     TARGET_URL: テストで利用するAPIエンドポイント
    @pytest.fixture()
    def props(self):
        client = APIClient()
        return {
            'TARGET_URL': '/api/v1/command/',
            'client': client
        }

    def test_POSTリクエストで新規コマンドが登録される(self, props, single_command):

        params = {
            'category_id': single_command.category_id.category_id,
            'command_category_id': single_command.command_category_id.command_category_id,
            'command_name': 'post_command'
        }

        response = props['client'].post(props['TARGET_URL'], params, format='json')

        command = Command.objects.filter(command_name='post_command')

        assert response.status_code == 201
        assert command[0].command_name == params['command_name']