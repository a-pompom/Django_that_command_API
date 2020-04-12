from rest_framework.test import APITestCase
from rest_framework import serializers
from rest_framework import status
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from rest_framework.test import APIClient

import pytest
import json

from ...models.command import Command

from .command_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestUpdateCommandRequests:

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

    def get_end_point(self, props, command_id):
        return f"{props['TARGET_URL']}{command_id}"

    def test_更新処理で既存コマンドが更新される(self, props, single_command):

        command_id = '90811bb8-00bd-46b1-839b-cab9c3b57130'
        mod_command_name = 'mod_command'

        params = {
            'command_name': mod_command_name
        }

        end_point = self.get_end_point(props, command_id)

        response = props['client'].post(end_point, params, format='json')

        command = get_object_or_404(Command, pk=command_id)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['command_name'] == mod_command_name

    def test_更新処理で空値を指定するとバリデーションエラーとなる(self, props, single_command):

        command_id = '90811bb8-00bd-46b1-839b-cab9c3b57130'
        mod_command_name = ''

        params = {
            'command_name': mod_command_name
        }

        end_point = self.get_end_point(props, command_id)

        response = props['client'].post(end_point, params, format='json')

        assert response.data['command_name'][0] == 'コマンド名を入力してください。'

    def test_更新処理で不正なコマンドカテゴリIDを指定するとバリデーションエラーとなる(self, props, single_command):

        command_id = '不正なコマンドカテゴリID'
        mod_command_name = 'command'

        params = {
            'command_name': mod_command_name
        }

        end_point = self.get_end_point(props, command_id)

        with pytest.raises(ValidationError):
            response = props['client'].post(end_point, params, format='json')