from rest_framework import serializers

from django.contrib.auth.models import User
from visualwords.models import VisualWord

# Visual Words
class VisWordSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    class Meta:
        model = VisualWord
        
class VisWordSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualWord
        fields = ('url_img', 'url_thumb',)
        
# Users
class UserSerializer(serializers.ModelSerializer):
    creations = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='visualword-detail')
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'creations', 'groups')
