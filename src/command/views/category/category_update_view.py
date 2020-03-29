from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F
from django.shortcuts import get_object_or_404

from ...models.category import Category
from ...serializers.category_serializer import CategorySerializer

class CategoryUpdateView(views.APIView):
    """
    カテゴリを更新するためのAPIViewクラス
        
    """

    def post(self, request, category_id, *args, **kwargs):
        """
        postリクエスト 入力値をもとにカテゴリを更新

        Parameters
        ----------
        self :  CategoryUpdateView
        request : HttpRequest
        category_id: UUID

        Returns
        -------
        response : JsonResponse
            更新されたカテゴリ
        """

        category = get_object_or_404(Category, pk=category_id)

        serializer = CategorySerializer(instance=category, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)