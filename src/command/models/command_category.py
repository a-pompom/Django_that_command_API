from django.db import models
import uuid

from .category import Category

class CommandCategory(models.Model):

    class Meta:
        db_table = 'command_category'

    # コマンドカテゴリID
    command_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # カテゴリID
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null = False
    )

    # コマンドカテゴリ名
    command_category_name = models.CharField(max_length=255)
    
    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)

    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)