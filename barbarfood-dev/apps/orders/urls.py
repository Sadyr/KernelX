from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


from .views import (
    AddDeleteCartView,
    UserSessionView,
    CreateOrderView
)

router = DefaultRouter()
# router.register(CategoriesView.as_view())

urlpatterns = [
    path('cart/', AddDeleteCartView.as_view(), name='add-cart'),
    path('actualize/', UserSessionView.as_view(), name='session-actualize'),
    path('order/', CreateOrderView.as_view(), name="create-order")
    path('add/',views.add, name='add'),

]
