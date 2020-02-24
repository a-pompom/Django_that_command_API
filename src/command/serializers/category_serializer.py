from rest_framework import serializers
from ..models.category import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    
class CategoryListSerializer(serializers.ListSerializer):
    child = CategorySerializer()