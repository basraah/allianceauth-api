from rest_framework import serializers
from timerboard.models import Timer
from allianceauth_api.serializers.eveonline import EveCorporationInfoField, EveCharacterField


class TimerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ('id', 'eve_time',)


class TimerSerializer(serializers.ModelSerializer):
    posted_by_character_id = EveCharacterField(source='eve_character')
    corporation_id = EveCorporationInfoField(source='eve_corp')

    class Meta:
        model = Timer
        exclude = ('eve_corp', 'eve_character')
