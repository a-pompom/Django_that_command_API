from rest_framework.test import APITestCase
from rest_framework import serializers
from rest_framework import status
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

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
            'TARGET_URL': '/api/v1/category/',
            'client': client
        }

    def test_更新処理で既存カテゴリが更新される(self, props, single_category):

        category_id = '90811bb8-00bd-46b1-839b-cab9c3b57128'
        mod_category_name = 'mod_category'

        params = {
            'category_name': mod_category_name
        }

        end_point = f"{props['TARGET_URL']}{category_id}"

        response = props['client'].post(end_point, params, format='json')

        category = get_object_or_404(Category, pk=category_id)
        print(category.category_name)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['category_name'] == mod_category_name

    def test_更新処理で空値を指定するとバリデーションエラーとなる(self, props, single_category):

        category_id = '90811bb8-00bd-46b1-839b-cab9c3b57128'
        mod_category_name = ''

        params = {
            'category_name': mod_category_name
        }

        end_point = f"{props['TARGET_URL']}{category_id}"

        response = props['client'].post(end_point, params, format='json')
        assert response.data['category_name'][0] == 'カテゴリ名を入力してください。'

    def test_更新処理で不正なカテゴリIDを指定するとバリデーションエラーとなる(self, props, single_category):

        category_id = '不正なカテゴリID'
        mod_category_name = 'category'

        params = {
            'category_name': mod_category_name
        }
        end_point = f"{props['TARGET_URL']}{category_id}"

        with pytest.raises(ValidationError):
            response = props['client'].post(end_point, params, format='json')