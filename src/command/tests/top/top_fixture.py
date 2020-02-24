from ...models.category import Category
import pytest

# 単一のカテゴリ
@pytest.fixture()
def single_category():
    return (
        Category.objects.create(category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', category_name='test_category_1_fixture')
    )

# 複数カテゴリ
@pytest.fixture()
def multiple_categories():
    return (
        Category.objects.create(category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', category_name='test_category_1_fixture'),
        Category.objects.create(category_id='90811bb8-00bd-46b1-839b-cab9c3b57129', category_name='test_category_2_fixture')
    )

# ソートされていないカテゴリ DBへ登録用
@pytest.fixture()
def unordered_categories():
    return (
        Category.objects.create(category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', category_name='x_test_category_1_fixture'),
        Category.objects.create(category_id='90811bb8-00bd-46b1-839b-cab9c3b57129', category_name='f_test_category_2_fixture'),
        Category.objects.create(category_id='90811bb8-00bd-46b1-839b-cab9c3b57130', category_name='a_test_category_2_fixture'),
        Category.objects.create(category_id='90811bb8-00bd-46b1-839b-cab9c3b57131', category_name='文字_test_category_2_fixture'),
    )

# ソート済みのカテゴリ assertionで読み出す用
@pytest.fixture()
def ordered_categories():
    return (
        Category(category_id='90811bb8-00bd-46b1-839b-cab9c3b57130', category_name='a_test_category_2_fixture'),
        Category(category_id='90811bb8-00bd-46b1-839b-cab9c3b57129', category_name='f_test_category_2_fixture'),
        Category(category_id='90811bb8-00bd-46b1-839b-cab9c3b57128', category_name='x_test_category_1_fixture'),
        Category(category_id='90811bb8-00bd-46b1-839b-cab9c3b57131', category_name='文字_test_category_2_fixture'),
    )