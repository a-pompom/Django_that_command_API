from rest_framework import status, views
from rest_framework.response import Response

from django.db.models import F

from ..models.category import Category
from ..serializers.category_serializer import CategorySerializer, CategoryListSerializer

class TopView(views.APIView):

    def get(self, request, *args, **kwargs):

        category = Category.objects.all().order_by('category_name')

        serializer = CategorySerializer(instance=category, many=True)

        return Response(serializer.data, status.HTTP_200_OK)