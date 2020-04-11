from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F

from ...models.command_category import CommandCategory
from ...serializers.command_category_serializer import CommandCategorySerializer, CommandCategoryListSerializer

class CommandCategoryCreateView(views.APIView):
    """
    コマンドカテゴリを登録するためのAPIViewクラス
        
    """

    def post(self, request, *args, **kwargs):
        """
        postリクエスト 入力値をもとにコマンドカテゴリを新規登録

        Parameters
        ----------
        self :  CommandCategoryView
        request : HttpRequest

        Returns
        -------
        response : JsonResponse
            登録されたコマンドカテゴリ
        """

        serializer = CommandCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)