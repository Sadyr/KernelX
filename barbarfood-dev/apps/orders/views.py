from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from apps.common.mixins import PublicJSONRendererMixin
from .mixins import PublicSessionJSONRendererMixin
from .permissions import get_user_session
from .serializers import (
    AddDeleteCartItemSerializer,
    UserSessionSerializer,
    CreateSessionSerializer,
    SessionChangeSerializer,
    OrderCreateSerializer,
    OrderSerializer
)
from apps.orders.models import CartItems, Order
from ..users.models import UserSession
from .decorators import add_session


class SessionResponseViewMixin(PublicSessionJSONRendererMixin):
    serializer_class = UserSessionSerializer

    def perform_response(self, request):
        request.session.refresh_from_db()
        serializer = self.get_serializer(request.session)
        return Response(serializer.data)


class CartItemsView(GenericAPIView):
    queryset = CartItems.objects.all()

    def get_object(self):
        obj = self.request.session.cart.cart_items\
            .filter(item_id=self.request.data.get('item_id')).first()
        print(obj, 'this is obj')
        if obj is not None:
            return obj
        else:
            return None


class AddDeleteCartView(SessionResponseViewMixin, CartItemsView):

    def post(self, request):
        serializer = AddDeleteCartItemSerializer(
            instance=self.get_object(),
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(request, 'this is request')
            return self.perform_response(request)


class UserSessionView(PublicJSONRendererMixin, GenericAPIView):
    queryset = UserSession.objects.all()
    serializer_class = UserSessionSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSessionSerializer
        elif self.request.method == 'POST':
            return CreateSessionSerializer

    @add_session(raise_exception=True)
    def get(self, request):
        serializer = self.get_serializer(request.session)
        return Response(serializer.data)

    def post(self, request):
        if request.session_uuid:
            session = get_user_session(request.session_uuid)
            serializer = SessionChangeSerializer(instance=session, data=request.data, context={'request': request})
        else:
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)


class CreateOrderView(PublicSessionJSONRendererMixin, GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        elif self.request.method == 'POST':
            return OrderCreateSerializer

    @add_session(raise_exception=True)
    def get(self, request):
        serializer = self.get_serializer(request.session)
        return Response(serializer.data)

    def post(self, request):
        if request.session_uuid:
            print(request.session_uuid)
            session = get_user_session(request.session_uuid)
            print(session)
            serializer = OrderCreateSerializer(data=request.data, context={'request': request, 'session': session})
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            print('saving serializer')
            serializer.save()

        return Response(serializer.data)
def add(request):
    return HttpResponse('Hello')

