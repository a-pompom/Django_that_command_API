from rest_framework import serializers
from ..models.command_category import CommandCategory

class CommandCategorySerializer(serializers.Serializer):
    """
    コマンドカテゴリSerizalizer

    Attributes
    ----------
    command_category_id : UUID
        ID
    category_id : UUID
        紐づくカテゴリのID
    category_name : str
        コマンドカテゴリ名

    """

    command_category_id = serializers.CharField(required = False)

    # コマンドカテゴリID
    category_id = serializers.CharField(required = False)

    # コマンドカテゴリ名
    command_category_name = serializers.CharField(
        required = True,
        error_messages = {
            'blank': 'コマンドカテゴリ名を入力してください。'
        }
    )

    def create(self, validated_data):
        """
        コマンドカテゴリ新規作成

        Parameters
        ----------
        validated_data : dictionary
            バリデーション済みのリクエストデータ

        Returns
        -------
        CommandCategory
            バリデーション済みのデータをもとに作成されたCommandCategoryModel
        """

        # validated_dataのディクショナリを名前付き引数に展開
        new_command_category = CommandCategory(**validated_data)
        new_command_category.save()

        return new_command_category

    def update(self, instance, validated_data):
        """
        コマンドカテゴリ更新

        Parameters
        ----------
        instance : CommandCategory
            DBより取得した更新対象のコマンドカテゴリモデル
        validated_data : dictionary
            バリデーション済みのリクエストデータ

        Returns
        -------
        CommandCategory
            バリデーション済みのデータをもとに作成された更新用のコマンドカテゴリ
        """
        instance.command_category_name = validated_data.get('command_category_name', instance.command_category_name)

        instance.save()

        return instance

    def delete(self, instance):
        """
        コマンドカテゴリ削除

        Parameters
        ----------
        instance : CommandCategory
            DBより取得した削除対象のコマンドカテゴリ
        """
        instance.delete()
    

class CommandCategoryListSerializer(serializers.ListSerializer):
    child = CommandCategorySerializer()