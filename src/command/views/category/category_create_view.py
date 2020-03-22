from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F

from ...models.category import Category
from ...serializers.category_serializer import CategorySerializer, CategoryListSerializer

class CategoryCreateView(views.APIView):
    """
    カテゴリを登録するためのAPIViewクラス
        
    """

    def post(self, request, *args, **kwargs):
        """
        postリクエスト 入力値をもとにカテゴリを新規登録

        Parameters
        ----------
        self :  CategoryView
        request : HttpRequest

        Returns
        -------
        response : JsonResponse
            登録されたカテゴリ
        """

        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)