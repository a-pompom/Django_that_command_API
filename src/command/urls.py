from django.urls import path
from .views.category.category_list_view import CategoryListView
from .views.category.category_create_view import CategoryCreateView
from .views.category.category_update_view import CategoryUpdateView
from .views.category.category_delete_view import CategoryDeleteView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<str:category_id>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<str:category_id>', CategoryDeleteView.as_view(), name='category_delete'),
]