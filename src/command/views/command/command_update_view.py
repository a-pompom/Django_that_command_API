from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F
from django.shortcuts import get_object_or_404

from ...models.command import Command
from ...serializers.command_serializer import CommandSerializer, CommandListSerializer


class CommandUpdateView(views.APIView):
    """
    コマンドを更新するためのAPIViewクラス
        
    """

    def post(self, request, command_id, *args, **kwargs):
        """
        postリクエスト 入力値をもとにコマンドを更新

        Parameters
        ----------
        self :  CommandUpdateView
        request : HttpRequest
        command_id: UUID

        Returns
        -------
        response : JsonResponse
            更新されたコマンド
        """

        command = get_object_or_404(Command, pk=command_id)

        serializer = CommandSerializer(instance=command, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)