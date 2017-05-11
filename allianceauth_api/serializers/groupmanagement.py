from rest_framework import serializers
from groupmanagement.models import AuthGroup, GroupRequest
from allianceauth_api.serializers.eveonline import EveCharacterListSerializer


class GroupRequestListSerializer(serializers.ModelSerializer):
    group_request_id = serializers.IntegerField(source='pk')
    group_id = serializers.IntegerField(source='group.pk')
    user_id = serializers.IntegerField(source='user.pk')

    class Meta:
        model = GroupRequest
        fields = ('group_request_id', 'group_id', 'user_id', 'leave_request',)


class GroupRequestSerializer(serializers.ModelSerializer):
    group_request_id = serializers.IntegerField(source='pk')
    group_id = serializers.IntegerField(source='group.pk')
    user_id = serializers.IntegerField(source='user.pk')
    main_character = EveCharacterListSerializer(source='main_char')

    class Meta:
        model = GroupRequest
        fields = ('group_request_id', 'group_id', 'user_id', 'leave_request', 'status', 'main_character')


class AuthGroupSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(source='group.pk')

    class Meta:
        model = AuthGroup
        fields = ('group_id', 'internal', 'hidden', 'open', 'public', 'description')
