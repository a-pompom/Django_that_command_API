from django.urls import path
from .views.categoryView import CategoryView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category')
]