from django.urls import path
from .views.topView import TopView

urlpatterns = [
    path('', TopView.as_view(), name='top')
]