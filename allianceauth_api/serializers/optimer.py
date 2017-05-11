from rest_framework import serializers
from optimer.models import optimer as OpTimer
from allianceauth_api.serializers.eveonline import EveCharacterField


class OpTimerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpTimer
        fields = ('id', 'start',)


class OpTimerSerializer(serializers.HyperlinkedModelSerializer):
    posted_by_character_id = EveCharacterField(source='eve_character')

    class Meta:
        model = OpTimer
        exclude = ('eve_character',)
