from django.urls import path, include
from . import views

urlpatterns = [
    path('items/create/', views.ItemCreate.as_view(), name='item_create'),
]
