from django.urls import path
from .views.category.category_list_view import CategoryListView
from .views.category.category_create_view import CategoryCreateView
from .views.category.category_update_view import CategoryUpdateView
from .views.category.category_delete_view import CategoryDeleteView

from .views.command_category.command_category_list_view import CommandCategoryListView
from .views.command_category.command_category_create_view import CommandCategoryCreateView
from .views.command_category.command_category_update_view import CommandCategoryUpdateView
from .views.command_category.command_category_delete_view import CommandCategoryDeleteView

from .views.command.command_list_view import CommandListView
from .views.command.command_create_view import CommandCreateView
from .views.command.command_update_view import CommandUpdateView
from .views.command.command_delete_view import CommandDeleteView

urlpatterns = [
    # カテゴリ
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<str:category_id>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<str:category_id>', CategoryDeleteView.as_view(), name='category_delete'),

    # コマンドカテゴリ
    path('command_categories/', CommandCategoryListView.as_view(), name='command_category_list'),
    path('command_category/', CommandCategoryCreateView.as_view(), name='command_category_create'),
    path('command_category/<str:command_category_id>', CommandCategoryUpdateView.as_view(), name='command_category_update'),
    path('command_category/delete/<str:command_category_id>', CommandCategoryDeleteView.as_view(), name='command_category_delete'),

    # コマンド
    path('commands/', CommandListView.as_view(), name='command_list'),
    path('command/', CommandCreateView.as_view(), name='command_create'),
    path('command/<str:command_id>', CommandUpdateView.as_view(), name='command_update'),
    path('command/delete/<str:command_id>', CommandDeleteView.as_view(), name='command_delete'),
]