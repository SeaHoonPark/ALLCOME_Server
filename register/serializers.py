from rest_framework.serializers import ModelSerializer
from .models import User, Wrong, Bookmark


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class WrongSerializer(ModelSerializer):
    class Meta:
        model = Wrong
        fields = '__all__'


class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
