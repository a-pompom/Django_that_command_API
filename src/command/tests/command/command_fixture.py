from ...models.category import Category
from ...models.command_category import CommandCategory
from ...models.command import Command

import pytest

# 単一のコマンド
@pytest.fixture()
def single_command():

    category = Category.objects.create(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
        category_name='test_category_1_fixture'
    )
    command_category = CommandCategory.objects.create(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
        category_id = category,
        command_category_name='test_command_category_1_fixture'
    )
    return (
        Command.objects.create(
            command_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category,
            command_category_id = command_category,
            command_name='test_command_1_fixture',
            memo='the memo'
        )
    )

# 複数コマンド
@pytest.fixture()
def multiple_command():
    category1 = Category.objects.create(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
        category_name='test_category_1_fixture'
    )
    command_category1 = CommandCategory.objects.create(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57128',
        category_id = category1,
        command_category_name='test_command_category_1_fixture'
    )

    category2 = Category.objects.create(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57129', 
        category_name='test_category_2_fixture'
    )
    command_category2 = CommandCategory.objects.create(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57129',
        category_id = category2,
        command_category_name='test_command_category_2_fixture'
    )

    category3 = Category.objects.create(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57130', 
        category_name='test_category_3_fixture'
    )
    command_category3 = CommandCategory.objects.create(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
        category_id = category3,
        command_category_name='test_command_category_3_fixture'
    )

    return (
        Command.objects.create(
            command_id='f0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category1,
            command_category_id = command_category1,
            command_name='test_command_1_fixture',
            memo='メモ'
        ),
        Command.objects.create(
            command_id='e0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category2,
            command_category_id = command_category2,
            command_name='test_command_2_fixture',
            memo=''
        ),
        Command.objects.create(
            command_id='d0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category3,
            command_category_id = command_category3,
            command_name='test_command_3_fixture'
        ),
    )

# ソートされていないコマンド DBへ登録用
@pytest.fixture()
def unordered_command():
    category1 = Category.objects.create(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
        category_name='test_category_1_fixture'
    )
    command_category1 = CommandCategory.objects.create(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57128',
        category_id = category1,
        command_category_name='test_command_category_1_fixture'
    )

    category2 = Category.objects.create(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57129', 
        category_name='test_category_2_fixture'
    )
    command_category2 = CommandCategory.objects.create(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57129',
        category_id = category2,
        command_category_name='test_command_category_2_fixture'
    )

    category3 = Category.objects.create(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57130', 
        category_name='test_category_3_fixture'
    )
    command_category3 = CommandCategory.objects.create(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
        category_id = category3,
        command_category_name='test_command_category_3_fixture'
    )

    return (
        Command.objects.create(
            command_id='f0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category1,
            command_category_id = command_category1,
            command_name='日本語コマンド'
        ),
        Command.objects.create(
            command_id='e0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category2,
            command_category_id = command_category2,
            command_name='the command'
        ),
        Command.objects.create(
            command_id='d0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category3,
            command_category_id = command_category3,
            command_name='01command'
        ),
    )

# ソート済みのコマンド assertionで読み出す用
@pytest.fixture()
def ordered_command():
    category1 = Category(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', 
        category_name='test_category_1_fixture'
    )
    command_category1 = CommandCategory(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57128',
        category_id = category1,
        command_category_name='test_command_category_1_fixture'
    )

    category2 = Category(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57129', 
        category_name='test_category_2_fixture'
    )
    command_category2 = CommandCategory(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57129',
        category_id = category2,
        command_category_name='test_command_category_2_fixture'
    )

    category3 = Category(
        category_id='90811bb8-00bd-46b1-839b-cab9c3b57130', 
        category_name='test_category_3_fixture'
    )
    command_category3 = CommandCategory(
        command_category_id='90811bb8-00bd-46b1-839b-cab9c3b57130',
        category_id = category3,
        command_category_name='test_command_category_3_fixture'
    )

    return (
        Command(
            command_id='d0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category3,
            command_category_id = command_category3,
            command_name='01command'
        ),
        Command(
            command_id='e0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category2,
            command_category_id = command_category2,
            command_name='the command'
        ),
        Command(
            command_id='f0811bb8-00bd-46b1-839b-cab9c3b57130',
            category_id = category1,
            command_category_id = command_category1,
            command_name='日本語コマンド'
        ),
    )