from rest_framework import serializers

from ..models.category import Category
from ..models.command_category import CommandCategory
from ..models.command import Command

class CommandSerializer(serializers.Serializer):
    """
    コマンドSerizalizer

    Attributes
    ----------
    command_id : UUID
        ID
    command_category_id : UUID
        紐づくコマンドカテゴリのID
    category_id : UUID
        紐づくカテゴリのID
    command_name : str
        コマンド名
    memo : str
        コマンドに付随するメモ

    """

    command_id = serializers.CharField(required = False)

    command_category_id = serializers.CharField(required = False)

    category_id = serializers.CharField(required = False)

    # コマンド名
    command_name = serializers.CharField(
        required = True,
        error_messages = {
            'blank': 'コマンド名を入力してください。'
        }
    )

    memo = serializers.CharField(
        required = False
    )

    def create(self, validated_data):
        """
        コマンド新規作成

        Parameters
        ----------
        validated_data : dictionary
            バリデーション済みのリクエストデータ

        Returns
        -------
        Command
            バリデーション済みのデータをもとに作成されたコマンドモデル
        """

        category = Category.objects.filter(
            category_id = validated_data['category_id']
            )[0]

        command_category = CommandCategory.objects.filter(
            command_category_id = validated_data['command_category_id']
        )[0]

        new_command = Command(
            category_id = category,
            command_category_id = command_category,
            command_name = validated_data['command_name'],
            memo = validated_data['memo'] if validated_data.get('memo') else ''
        )

        new_command.save()

        return new_command

    def update(self, instance, validated_data):
        """
        コマンド更新

        Parameters
        ----------
        instance : Command
            DBより取得した更新対象のコマンドモデル
        validated_data : dictionary
            バリデーション済みのリクエストデータ

        Returns
        -------
        Command
            バリデーション済みのデータをもとに作成された更新用のコマンド
        """
        instance.command_name = validated_data.get('command_name', instance.command_name)
        instance.memo = validated_data.get('memo', instance.memo)

        instance.save()

        return instance

    def delete(self, instance):
        """
        コマンド削除

        Parameters
        ----------
        instance : Command
            DBより取得した削除対象のコマンド
        """
        instance.delete()
    

class CommandListSerializer(serializers.ListSerializer):
    child = CommandSerializer()