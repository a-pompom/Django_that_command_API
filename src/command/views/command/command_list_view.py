from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F

from ...models.command import Command
from ...serializers.command_serializer import CommandSerializer, CommandListSerializer

class CommandListView(views.APIView):
    """
    コマンドを一覧表示するためのAPIViewクラス
        
    """

    def get(self, request, *args, **kwargs):
        """
        getリクエスト コマンドの一覧を取得

        Parameters
        ----------
        self :  CommandListView
        request : HttpRequest

        Returns
        -------
        response : JsonResponse
            コマンド一覧
        """

        # 視覚的に判別しやすい、という観点から、コマンド名昇順でソート
        command = Command.objects.all().order_by('command_name')
        serializer = CommandSerializer(instance=command, many=True)

        return Response(serializer.data, status.HTTP_200_OK)