from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from .authentication import AuthServicesInfoSerializer


class UserListSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id')

    class Meta:
        model = User
        fields = ('user_id', 'username')


class GroupListSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(source='id')

    class Meta:
        model = Group
        fields = ('group_id', 'name')


class PermissionListSerializer(serializers.ModelSerializer):
    permission_id = serializers.IntegerField(source='id')

    class Meta:
        model = Permission
        fields = ('permission_id', 'codename')


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id')
    authservicesinfo = AuthServicesInfoSerializer()

    class Meta:
        model = User
        fields = ('user_id', 'username', 'is_staff', 'is_active', 'authservicesinfo')


class GroupSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(source='id')

    class Meta:
        model = Group
        fields = ('group_id', 'name')


class PermissionSerializer(serializers.ModelSerializer):
    permission_id = serializers.IntegerField(source='id')

    class Meta:
        model = Permission
        fields = ('permission_id', 'name', 'codename')
