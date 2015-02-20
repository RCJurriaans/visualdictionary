from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, VisWordViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'words', VisWordViewSet)

urlpatterns = patterns('',
    (r'^', include(router.urls)),
    (r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)






