from django.contrib.auth.models import User, Group
from .models import ImageDetection
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = []
    serializers.HyperlinkedIdentityField(view_name="rest_framework:user-detail")
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group 
        fields = ['url', 'name'] 


class ImageDetectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageDetection
        fields = ["created _at", "image", "model_evaluation", "model_evaluation_dict"] 