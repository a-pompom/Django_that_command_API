from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F
from django.shortcuts import get_object_or_404

from ...models.category import Category
from ...serializers.category_serializer import CategorySerializer

class CategoryDeleteView(views.APIView):
    """
    カテゴリを削除するためのAPIViewクラス
        
    """

    def delete(self, request, category_id, *args, **kwargs):
        """
        deleteリクエスト 指定されたカテゴリIDに紐づくカテゴリを削除

        Parameters
        ----------
        request : HttpRequest
        category_id: UUID

        Returns
        -------
        response : JsonResponse
            削除完了情報
        """

        category = get_object_or_404(Category, pk=category_id)

        serializer = CategorySerializer()
        serializer.delete(category)

        return Response(serializer.data, status.HTTP_200_OK)