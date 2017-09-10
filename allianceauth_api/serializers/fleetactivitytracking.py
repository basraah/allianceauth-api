from rest_framework import serializers
from fleetactivitytracking.models import Fat, Fatlink
from django.contrib.auth.models import User
from allianceauth_api.serializers.eveonline import EveCharacterListSerializer


class FatListSerializer(serializers.ModelSerializer):
    fat_id = serializers.IntegerField(source='pk')
    fatlink_id = serializers.IntegerField(source='fatlink.pk')
    user_id = serializers.IntegerField(source='user.pk')
    character_id = serializers.IntegerField(source='character.character_id')

    class Meta:
        model = Fat
        fields = ('fat_id', 'fatlink_id', 'user_id', 'character_id',)


class FatSerializer(serializers.ModelSerializer):
    fatlink_id = serializers.IntegerField(source='fatlink.pk')
    user_id = serializers.IntegerField(source='user.pk')
    character = EveCharacterListSerializer()

    class Meta:
        model = Fat
        exclude = ('fatlink', 'user',)


class FatlinkListSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(source='fatdatetime')
    fatlink_id = serializers.PrimaryKeyRelatedField(source='id', queryset=Fatlink.objects.all())

    class Meta:
        model = Fatlink
        fields = ('fat_link_id', 'date',)


class FatlinkSerializer(FatlinkListSerializer):
    creator_user_id = serializers.PrimaryKeyRelatedField(source='creator', queryset=User.objects.all())

    class Meta:
        model = Fatlink
        exclude = ('id', 'fatdatetime', 'creator',)
