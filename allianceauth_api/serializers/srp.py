from rest_framework import serializers
from srp.models import SrpFleetMain, SrpUserRequest
from allianceauth_api.serializers.eveonline import EveCharacterField


class SrpFleetMainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SrpFleetMain
        fields = ('id', 'fleet_name', 'fleet_srp_code')


class SrpFleetMainSerializer(serializers.ModelSerializer):
    fleet_commander_character_id = EveCharacterField(source='fleet_commander')
    total_cost = serializers.IntegerField(read_only=True)
    pending_requests = serializers.IntegerField(read_only=True)

    class Meta:
        model = SrpFleetMain
        exclude = ('fleet_commander',)


class SrpUserRequestListSerializer(serializers.ModelSerializer):
    character_id = EveCharacterField(source='character')

    class Meta:
        model = SrpUserRequest
        fields = ('id', 'character_id', 'srp_status')


class SrpUserRequestSerializer(SrpUserRequestListSerializer):
    fleet_id = serializers.PrimaryKeyRelatedField(source='srp_fleet_main', queryset=SrpFleetMain.objects.all())

    class Meta:
        model = SrpUserRequest
        exclude = ('srp_fleet_main',)
