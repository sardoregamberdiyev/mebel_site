from rest_framework import serializers

from tg.models import TgUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = '__all__'

