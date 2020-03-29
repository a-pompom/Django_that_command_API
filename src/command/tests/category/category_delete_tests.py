from rest_framework.test import APITestCase
from django.urls import reverse
from django.http import Http404

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
            'TARGET_URL': '/api/v1/category/delete/',
            'client': client
        }

    def get_end_point(self, props, category_id):
        return f"{props['TARGET_URL']}{category_id}"

    def test_Delete処理で既存カテゴリが削除される(self, props, single_category):

        category_id = '90811bb8-00bd-46b1-839b-cab9c3b57128'
        end_point = self.get_end_point(props, category_id)

        response = props['client'].delete(end_point, format='json')

        with pytest.raises(Http404):
            get_object_or_404(Category, pk=category_id)

    def test_Delete処理で対象のレコードのみが削除される(self, props, multiple_categories):

        category_id = '90811bb8-00bd-46b1-839b-cab9c3b57128'
        end_point = self.get_end_point(props, category_id)

        response = props['client'].delete(end_point, format='json')

        with pytest.raises(Http404):
            get_object_or_404(Category, pk=category_id)

        # DB上のレコードが1件のみ削除され、かつ、削除対象は指定したIDと結びつくものとなること
        assert Category.objects.all().count() == 1
        assert get_object_or_404(Category, pk='90811bb8-00bd-46b1-839b-cab9c3b57129')