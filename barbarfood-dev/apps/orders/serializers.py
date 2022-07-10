from rest_framework import serializers

from apps.nomenclature.models import Items
from apps.orders.exceptions import ItemNotFound, CanNotAddZeroCountItem
from apps.orders.mixins import UsersessionPropertyMixin
from apps.orders.models import CartItems, Cart, Order, Delivery
from apps.users.models import UserSession, Address


class AddDeleteCartItemSerializer(UsersessionPropertyMixin, serializers.ModelSerializer):
    item_id = serializers.IntegerField(required=True)
    count = serializers.IntegerField(required=True)

    class Meta:
        model = CartItems
        fields = ('item_id', 'count', 'cart')
        extra_kwargs = {
            'cart': {'required': False}
        }

    def validate(self, attrs):
        item = Items.objects.filter(id=attrs['item_id']).first()
        if not item:
            raise ItemNotFound
        return attrs

    def create(self, validated_data):
        validated_data['cart'] = self.session.cart

        if validated_data['count'] <= 0:
            raise CanNotAddZeroCountItem
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Deleting from Cart
        if validated_data['count'] == 0:
            return instance.delete()

        return super().update(instance, validated_data)


class ItemSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source="item.id")
    name = serializers.CharField(source="item.name")
    image = serializers.CharField(source="item.image")
    price = serializers.IntegerField(source="item.price")

    class Meta:
        model = CartItems
        fields = [
            "id",
            "name",
	        "image",
            "price",
            "count"
        ]


class CartSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'items',
            'items_count',
            'items_price',
            'total_price'
        )


class AddressSerializer(serializers.ModelSerializer):
    longitude = serializers.DecimalField(max_digits=12, decimal_places=8, required=False)
    latitude = serializers.DecimalField(max_digits=12, decimal_places=8, required=False)

    class Meta:
        model = Address
        fields = (
            'id',
            'district',
            'street',
            'building',
            'is_private_home',
            'entrance',
            'floor',
            'flat',
            'longitude',
            'latitude',
        )


class BaseSessionSerializer(serializers.ModelSerializer):
    cart = CartSerializer(required=False, read_only=True)
    address = AddressSerializer(required=False, read_only=True)

    class Meta:
        model = UserSession
        fields = (
            'uuid',
            "address",
            "cart",
        )

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        data['cart'] = Cart.objects.create()
        print('created new cart')
        return data

    def create(self, validated_data):
        print(validated_data, 'this is validated data')
        session = UserSession.objects.create(**validated_data)
        return session


class UserSessionSerializer(BaseSessionSerializer):
    ...


class CreateSessionSerializer(BaseSessionSerializer):


    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return data

    def create(self, validated_data):
        session = super().create(validated_data)
        setattr(self.context.get('request'), 'session', session)
        return session


class SessionChangeSerializer(BaseSessionSerializer):

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return data

    def update(self, instance, validated_data):
        instance.save()
        instance.refresh_from_db()

        return instance


class DeliverySerializer(serializers.ModelSerializer):

    delivery_type = serializers.CharField()

    class Meta:
        model = Delivery
        fields = ("delivery_type", 'timeslot')


class OrderCreateSerializer(serializers.ModelSerializer, UsersessionPropertyMixin):

    address = serializers.CharField(write_only=True)
    delivery = DeliverySerializer(many=False, write_only=True)
    payment_type = serializers.CharField(write_only=True)

    class Meta:
        model = Order
        fields = ("delivery", "payment_type", "address")
        extra_kwargs = {
            'delivery': {'write_only': True}
        }

    def validate(self, attrs):
        print(self.context.get('session'))
        attrs['delivery'] = Delivery.objects.create(delivery_type=attrs['delivery']['delivery_type'], timeslot=attrs['delivery']['timeslot'])

        return attrs

    def create(self, validated_data):
        print('order created')

        session = self.session
        print(session)
        cart = session.cart
        print(cart, 'this is cart')
        order = Order.objects.create(delivery=validated_data['delivery'],
                                     total_price=cart.total_price, cart=cart,
                                     payment_type=validated_data['payment_type'],
                                     address=validated_data['address'])

        session.cart = Cart.objects.create()
        session.save(update_fields=['cart'])

        return order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
