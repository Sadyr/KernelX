from rest_framework import serializers
from apps.nomenclature.models import Category, Items


class ItemSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ("id", "name", "description", "image", "price", "tags")

    def get_tags(self, obj):
        tags = [tag.name for tag in obj.tags.all()]

        return tags

class CategorySerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "items")


class OfferedItemSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "items")


class ItemDetailSerializer(serializers.ModelSerializer):
    offered_items = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ("id", "name", "description", "image", "price", "offered_items")

    def get_offered_items(self, obj):
        category_for_cart = Category.objects.filter(is_for_cart=True)
        return CategorySerializer(category_for_cart, many=True).data