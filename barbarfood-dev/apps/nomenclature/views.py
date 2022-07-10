from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from apps.common.mixins import PublicJSONRendererMixin
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.nomenclature.models import Category, Items
from apps.nomenclature.serializers import CategorySerializer, ItemDetailSerializer


# class ItemsView(PublicJSONRendererMixin, RetrieveAPIView):
#     queryset = None
#     serializer_class = ItemSerializer
#     filter_backends = (
#         DjangoFilterBackend,
#         OrderingFilter,
#     )
#     ordering_fields = '__all__'
#
#     def get_queryset(self):
#         query_set = self.queryset.exclude(child_category__products=None)
#         print(query_set)
#
#         return query_set
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class CategoriesView(PublicJSONRendererMixin, ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = '__all__'
    
    def list(self, request, *args, **kwargs):
        return super(CategoriesView, self).list(request)


class ItemsDetailView(PublicJSONRendererMixin, RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemDetailSerializer
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        return super(ItemsDetailView, self).get(request)
