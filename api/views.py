from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

# Models
from django.contrib.auth.models import User
from visualwords.models import VisualWord

# Serializers
from .serializers import UserSerializer, VisWordSerializer

# Custom Permissions
from api.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class VisWordViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly,)
    queryset = VisualWord.objects.all()
    serializer_class = VisWordSerializer

