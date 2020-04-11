from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F

from ...models.command_category import CommandCategory
from ...serializers.command_category_serializer import CommandCategorySerializer, CommandCategoryListSerializer

class CommandCategoryListView(views.APIView):
    """
    コマンドカテゴリを一覧表示するためのAPIViewクラス
        
    """

    def get(self, request, *args, **kwargs):
        """
        getリクエスト コマンドカテゴリの一覧を取得

        Parameters
        ----------
        self :  CommandCategoryView
        request : HttpRequest

        Returns
        -------
        response : JsonResponse
            コマンドカテゴリ一覧
        """

        # 視覚的に判別しやすい、という観点から、コマンドカテゴリ名昇順でソート
        command_category = CommandCategory.objects.all().order_by('command_category_name')
        serializer = CommandCategorySerializer(instance=command_category, many=True)

        return Response(serializer.data, status.HTTP_200_OK)