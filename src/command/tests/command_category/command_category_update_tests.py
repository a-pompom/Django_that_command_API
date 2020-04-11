from rest_framework.test import APITestCase
from rest_framework import serializers
from rest_framework import status
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from rest_framework.test import APIClient

import pytest
import json

from ...models.command_category import CommandCategory

from .command_category_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestUpdateCommandCategoryRequests:

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

    def get_end_point(self, props, command_category_id):
        return f"{props['TARGET_URL']}{command_category_id}"

    def test_更新処理で既存カテゴリが更新される(self, props, single_command_category):

        command_category_id = '90811bb8-00bd-46b1-839b-cab9c3b57130'
        mod_category_name = 'mod_command_category'

        params = {
            'command_category_name': mod_category_name
        }

        end_point = self.get_end_point(props, command_category_id)

        response = props['client'].post(end_point, params, format='json')

        command_category = get_object_or_404(CommandCategory, pk=command_category_id)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['command_category_name'] == mod_category_name

    def test_更新処理で空値を指定するとバリデーションエラーとなる(self, props, single_command_category):

        command_category_id = '90811bb8-00bd-46b1-839b-cab9c3b57130'
        mod_category_name = ''

        params = {
            'command_category_name': mod_category_name
        }

        end_point = self.get_end_point(props, command_category_id)

        response = props['client'].post(end_point, params, format='json')

        assert response.data['command_category_name'][0] == 'コマンドカテゴリ名を入力してください。'

    def test_更新処理で不正なコマンドカテゴリIDを指定するとバリデーションエラーとなる(self, props, single_command_category):

        command_category_id = '不正なコマンドカテゴリID'
        mod_command_category_name = 'command_category'

        params = {
            'command_category_name': mod_command_category_name
        }

        end_point = self.get_end_point(props, command_category_id)

        with pytest.raises(ValidationError):
            response = props['client'].post(end_point, params, format='json')