from django.urls import path
from .views.topView import TopView

urlpatterns = [
    path('category/', TopView.as_view(), name='top')
]