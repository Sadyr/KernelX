from rest_framework import serializers
from apps.promotions.models import Promotion


class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ('id', 'image')