from django.db import models
import uuid

from .category import Category
from .command_category import CommandCategory

class Command(models.Model):

    class Meta:
        db_table = 'command'

    # コマンドID 主キー
    command_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # カテゴリID
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null = False
    )

    # コマンドカテゴリID
    command_category_id = models.ForeignKey(
        CommandCategory,
        on_delete=models.CASCADE,
        null = False
    )

    # コマンド名
    command_name = models.CharField(max_length=255)

    # メモ
    memo = models.TextField(blank=False)

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)

    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)