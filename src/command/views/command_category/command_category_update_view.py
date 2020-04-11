from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F
from django.shortcuts import get_object_or_404

from ...models.command_category import CommandCategory
from ...serializers.command_category_serializer import CommandCategorySerializer, CommandCategoryListSerializer


class CommandCategoryUpdateView(views.APIView):
    """
    コマンドカテゴリを更新するためのAPIViewクラス
        
    """

    def post(self, request, command_category_id, *args, **kwargs):
        """
        postリクエスト 入力値をもとにコマンドカテゴリを更新

        Parameters
        ----------
        self :  CommandCategoryUpdateView
        request : HttpRequest
        command_category_id: UUID

        Returns
        -------
        response : JsonResponse
            更新されたコマンドカテゴリ
        """

        command_category = get_object_or_404(CommandCategory, pk=command_category_id)

        serializer = CommandCategorySerializer(instance=command_category, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)