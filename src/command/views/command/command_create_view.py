from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F

from ...models.command import Command
from ...serializers.command_serializer import CommandSerializer, CommandListSerializer

class CommandCreateView(views.APIView):
    """
    コマンドを登録するためのAPIViewクラス
        
    """

    def post(self, request, *args, **kwargs):
        """
        postリクエスト 入力値をもとにコマンドを新規登録

        Parameters
        ----------
        self :  CommandView
        request : HttpRequest

        Returns
        -------
        response : JsonResponse
            登録されたコマンド
        """

        serializer = CommandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)