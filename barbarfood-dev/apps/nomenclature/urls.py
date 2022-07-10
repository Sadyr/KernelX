from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriesView,
    ItemsDetailView
)

router = DefaultRouter()
# router.register(CategoriesView.as_view())

urlpatterns = [
    path('categories', CategoriesView.as_view(), name='category-list'),
    path('items/<int:pk>/', ItemsDetailView.as_view(), name='get-item')
]
