from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F
from django.shortcuts import get_object_or_404

from ...models.command import Command
from ...serializers.command_serializer import CommandSerializer, CommandListSerializer

class CommandDeleteView(views.APIView):
    """
    コマンドを削除するためのAPIViewクラス
        
    """

    def delete(self, request, command_id, *args, **kwargs):
        """
        deleteリクエスト 指定されたコマンドIDに紐づくコマンドを削除

        Parameters
        ----------
        request : HttpRequest
        command_id: UUID

        Returns
        -------
        response : JsonResponse
            削除完了情報
        """

        command = get_object_or_404(Command, pk=command_id)

        serializer = CommandSerializer()
        serializer.delete(command)

        return Response(serializer.data, status.HTTP_200_OK)