from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F
from django.shortcuts import get_object_or_404

from ...models.command_category import CommandCategory
from ...serializers.command_category_serializer import CommandCategorySerializer, CommandCategoryListSerializer

class CommandCategoryDeleteView(views.APIView):
    """
    コマンドカテゴリを削除するためのAPIViewクラス
        
    """

    def delete(self, request, command_category_id, *args, **kwargs):
        """
        deleteリクエスト 指定されたコマンドカテゴリIDに紐づくカテゴリを削除

        Parameters
        ----------
        request : HttpRequest
        command_category_id: UUID

        Returns
        -------
        response : JsonResponse
            削除完了情報
        """

        command_category = get_object_or_404(CommandCategory, pk=command_category_id)

        serializer = CommandCategorySerializer()
        serializer.delete(command_category)

        return Response(serializer.data, status.HTTP_200_OK)