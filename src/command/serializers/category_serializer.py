from rest_framework import serializers
from ..models.category import Category

class CategorySerializer(serializers.Serializer):
    """
    カテゴリSerizalizer

    Attributes
    ----------
    category_id : UUID
        ID
    category_name : str
        カテゴリ名

    """

    # カテゴリID
    category_id = serializers.CharField(required = False)

    # カテゴリ名
    category_name = serializers.CharField(
        required = True,
        error_messages = {
            'blank': 'カテゴリ名を入力してください。'
        }
    )

    def create(self, validated_data):
        """
        カテゴリ新規作成

        Parameters
        ----------
        validated_data : dictionary
            バリデーション済みのリクエストデータ

        Returns
        -------
        Category
            バリデーション済みのデータをもとに作成されたCategoryModel
        """

        # validated_dataのディクショナリを名前付き引数に展開
        new_category = Category(**validated_data)
        new_category.save()

        return new_category

    def update(self, instance, validated_data):
        """
        カテゴリ更新

        Parameters
        ----------
        instance : Category
            DBより取得した更新対象のカテゴリModel
        validated_data : dictionary
            バリデーション済みのリクエストデータ

        Returns
        -------
        Category
            バリデーション済みのデータをもとに作成された更新用のカテゴリModel
        """
        instance.category_name = validated_data.get('category_name', instance.category_name)

        instance.save()

        return instance

    def delete(self, instance):
        """
        カテゴリ削除

        Parameters
        ----------
        instance : Category
            DBより取得した削除対象のカテゴリModel
        """
        instance.delete()
    

class CategoryListSerializer(serializers.ListSerializer):
    child = CategorySerializer()