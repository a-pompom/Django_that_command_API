from django.db import models
import uuid

class Category(models.Model):

    class Meta:
        db_table = 'category'

    # カテゴリID 主キー
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # カテゴリ名
    category_name = models.CharField(
        max_length = 255,
        )

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)

    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)