from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F

from ...models.category import Category
from ...serializers.category_serializer import CategorySerializer, CategoryListSerializer

class CategoryListView(views.APIView):
    """
    カテゴリを一覧表示するためのAPIViewクラス
        
    """

    def get(self, request, *args, **kwargs):
        """
        getリクエスト カテゴリの一覧を取得

        Parameters
        ----------
        self :  CategoryView
        request : HttpRequest

        Returns
        -------
        response : JsonResponse
            カテゴリ一覧
        """

        # 視覚的に判別しやすい、という観点から、カテゴリ名昇順でソート
        category = Category.objects.all().order_by('category_name')
        serializer = CategorySerializer(instance=category, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

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