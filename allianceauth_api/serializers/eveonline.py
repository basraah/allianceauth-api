from rest_framework import serializers
from eveonline.models import EveAllianceInfo, EveApiKeyPair, EveCharacter, EveCorporationInfo
from allianceauth_api.serializers.base import UserListSerializer


class EveAllianceInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveAllianceInfo
        fields = ('alliance_id', 'alliance_name',)


class EveAllianceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveAllianceInfo
        fields = ('alliance_id', 'alliance_name', 'alliance_ticker', 'executor_corp_id', 'is_blue',)


class EveCharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveCharacter
        fields = ('character_id', 'character_name',)


class EveCharacterSerializer(serializers.ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = EveCharacter
        fields = ('character_id', 'character_name', 'corporation_id', 'corporation_name', 'corporation_ticker',
                  'alliance_id', 'alliance_name', 'api_id', 'user',)
        lookup_field = 'character_id'


class EveCharacterField(serializers.RelatedField):
    def get_queryset(self):
        return EveCharacter.objects.all()

    def to_internal_value(self, value):
        try:
            char = EveCharacter.objects.get(character_id=value)
            return char
        except EveCharacter.DoesNotExist:
            raise serializers.ValidationError

    def to_representation(self, value):
        return value.character_id


class EveApiKeyPairListSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.pk')

    class Meta:
        model = EveApiKeyPair
        fields = ('api_id', 'user_id',)


class EveApiKeyPairSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.pk')

    class Meta:
        model = EveApiKeyPair
        fields = ('api_id', 'api_key', 'user_id', 'sso_verified',)


class EveCorporationInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveCorporationInfo
        fields = ('corporation_id', 'corporation_name')


class EveCorporationInfoSerializer(serializers.ModelSerializer):
    alliance_id = serializers.CharField(source='alliance.alliance_id')

    class Meta:
        model = EveCorporationInfo
        fields = ('corporation_id', 'corporation_name', 'corporation_ticker', 'member_count', 'is_blue',
                  'alliance_id')


class EveCorporationInfoField(serializers.RelatedField):
    def get_queryset(self):
        return EveCorporationInfo.objects.all()

    def to_internal_value(self, value):
        try:
            corp = EveCorporationInfo.objects.get(corporation_id=value)
            return corp
        except EveCorporationInfo.DoesNotExist:
            raise serializers.ValidationError

    def to_representation(self, value):
        return value.corporation_id
