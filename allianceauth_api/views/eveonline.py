from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from allianceauth_api.serializers.eveonline import EveAllianceInfo, EveCharacter, EveApiKeyPair, EveCorporationInfo
from allianceauth_api.serializers.eveonline import EveAllianceInfoListSerializer, EveAllianceInfoSerializer, \
    EveCharacterListSerializer, EveCharacterSerializer, EveApiKeyPairListSerializer, EveApiKeyPairSerializer, \
    EveCorporationInfoListSerializer, EveCorporationInfoSerializer

from allianceauth_api.serializers.timerboard import TimerListSerializer
from allianceauth_api.serializers.srp import SrpUserRequestListSerializer
from allianceauth_api.serializers.fleetactivitytracking import FatListSerializer


class EveAllianceInfoViewSet(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = EveAllianceInfo.objects.all()
    serializer_class = EveAllianceInfoSerializer
    lookup_field = 'alliance_id'

    def list(self, request, *args, **kwargs):
        serializer = EveAllianceInfoListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def corporations(self, request, *args, **kwargs):
        serializer = EveCorporationInfoListSerializer(self.get_object().evecorporationinfo_set.all(), many=True)
        return Response(serializer.data)


class EveCharacterViewSet(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = EveCharacter.objects.all()
    serializer_class = EveCharacterSerializer
    lookup_field = 'character_id'

    def list(self, request, *args, **kwargs):
        serializer = EveCharacterListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def srprequests(self, request, *args, **kwargs):
        serializer = SrpUserRequestListSerializer(self.get_object().srpuserrequest_set.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def fats(self, request, *args, **kwargs):
        serializer = FatListSerializer(self.get_object().fat_set.all(), many=True)
        return Response(serializer.data)


class EveApiKeyPairViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = EveApiKeyPair.objects.all()
    serializer_class = EveApiKeyPairSerializer
    lookup_field = 'api_id'

    def list(self, request, *args, **kwargs):
        serializer = EveApiKeyPairListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class EveCorporationInfoViewSet(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    queryset = EveCorporationInfo.objects.all()
    serializer_class = EveCorporationInfoSerializer
    lookup_field = 'corporation_id'

    def list(self, request, *args, **kwargs):
        serializer = EveCorporationInfoListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def timers(self, request, *args, **kwargs):
        serializer = TimerListSerializer(self.get_object().timer_set.filter(corp_timer=True), many=True)
        return Response(serializer.data)
