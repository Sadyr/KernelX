from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserViewSerializer
from apps.common.mixins import JSONRendererMixin
