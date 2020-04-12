from rest_framework.test import APITestCase
from django.urls import reverse
from django.http import Http404

from rest_framework.test import APIClient
from django.shortcuts import get_object_or_404

import pytest
import json

from ...models.command import Command

from .command_fixture import *

@pytest.mark.django_db(transaction=False) # transaction=Falseでテストコード実行で利用したDBトランザクションをコミットしないよう設定
class TestDeleteCommandRequests:

    # テストクラスで利用するプロパティ
    #     client: APIクライアント
    #     TARGET_URL: テストで利用するAPIエンドポイント
    @pytest.fixture()
    def props(self):
        client = APIClient()
        return {
            'TARGET_URL': '/api/v1/command/delete/',
            'client': client
        }

    def get_end_point(self, props, command_id):
        return f"{props['TARGET_URL']}{command_id}"

    def test_Delete処理で既存コマンドが削除される(self, props, single_command):

        command_id = '90811bb8-00bd-46b1-839b-cab9c3b57130'
        end_point = self.get_end_point(props, command_id)

        response = props['client'].delete(end_point, format='json')

        # DB上から実際に削除されたか検証するため、読み出しを行う
        with pytest.raises(Http404):
            get_object_or_404(Command, pk=command_id)

    def test_Delete処理で対象のレコードのみが削除される(self, props, multiple_command):

        command_id = 'f0811bb8-00bd-46b1-839b-cab9c3b57130'
        end_point = self.get_end_point(props, command_id)

        response = props['client'].delete(end_point, format='json')

        with pytest.raises(Http404):
            get_object_or_404(Command, pk=command_id)

        # DB上のレコードが1件のみ削除され、かつ、削除対象は指定したIDと結びつくものとなること
        assert Command.objects.all().count() == 2
        assert get_object_or_404(Command, pk='e0811bb8-00bd-46b1-839b-cab9c3b57130')
        assert get_object_or_404(Command, pk='d0811bb8-00bd-46b1-839b-cab9c3b57130')