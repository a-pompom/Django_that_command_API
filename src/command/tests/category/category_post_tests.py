from rest_framework.test import APITestCase
from django.urls import reverse

from rest_framework.test import APIClient
from django.shortcuts import get_object_or_404

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

    def test_POSTリクエストで新規カテゴリが登録される(self, props, single_category):

        params = {
            'category_name': 'post_category'
        }

        response = props['client'].post(props['TARGET_URL'], params, format='json')

        category = Category.objects.filter(category_name='post_category')

        assert response.status_code == 201
        assert category[0].category_name == params['category_name']