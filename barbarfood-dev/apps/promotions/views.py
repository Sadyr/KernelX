from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from apps.common.mixins import PublicJSONRendererMixin
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.promotions.models import Promotion
from apps.promotions.serializers import PromotionSerializer


class PromotionsView(PublicJSONRendererMixin, ListAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        return super(PromotionsView, self).list(request)