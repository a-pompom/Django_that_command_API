from ...models.category import Category
from ...models.command_category import CommandCategory
import pytest

# 単一のコマンドカテゴリ
@pytest.fixture()
def single_command_category():
    return (
        CommandCategory.objects.create(
            command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category.objects.create(
                category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='test_category_1_fixture'
            ),
            command_category_name='test_command_category_1_fixture'
        )
    )

# 複数コマンドカテゴリ
@pytest.fixture()
def multiple_command_categories():
    return (
        CommandCategory.objects.create(
            command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category.objects.create(
                category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='test_category_1_fixture'
            ),
            command_category_name='test_command_category_1_fixture'
        ),

        CommandCategory.objects.create(
            command_category_id='00811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category.objects.create(
                category_id='00811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='test_category_2_fixture'
            ),
            command_category_name='test_command_category_2_fixture'
        ),

        CommandCategory.objects.create(
            command_category_id='10811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category.objects.create(
                category_id='10811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='test_category_3_fixture'
            ),
            command_category_name='test_command_category_3_fixture'
        )
    )

# ソートされていないコマンドカテゴリ DBへ登録用
@pytest.fixture()
def unordered_command_categories():
    return (
        CommandCategory.objects.create(
            command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category.objects.create(
                category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='日本語カテゴリ'
            ),
            command_category_name='日本語コマンドカテゴリ'
        ),

        CommandCategory.objects.create(
            command_category_id='00811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category.objects.create(
                category_id='00811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='Git'
            ),
            command_category_name='Commit'
        ),

        CommandCategory.objects.create(
            command_category_id='10811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category.objects.create(
                category_id='10811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='arrow function() => {}'
            ),
            command_category_name='arrow function () => {}'
        )
    )

# ソート済みのカテゴリ assertionで読み出す用
@pytest.fixture()
def ordered_command_categories():
    return (
        CommandCategory(
            command_category_id='10811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category(
                category_id='10811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='arrow function() => {}'
            ),
            command_category_name='arrow function () => {}'
        ),
        CommandCategory(
            command_category_id='00811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category(
                category_id='00811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='Git'
            ),
            command_category_name='Commit'
        ),
        CommandCategory(
            command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = Category(
                category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
                category_name='日本語カテゴリ'
            ),
            command_category_name='日本語コマンドカテゴリ'
        ),
    )