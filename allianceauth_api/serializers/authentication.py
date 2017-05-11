from rest_framework import serializers
from authentication.models import AuthServicesInfo


class AuthServicesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthServicesInfo
        fields = ('main_char_id', 'state')
