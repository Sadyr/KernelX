from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PromotionsView,
)

router = DefaultRouter()
# router.register(CategoriesView.as_view())

urlpatterns = [
    path('promotions', PromotionsView.as_view(), name='promotion-list'),
]
