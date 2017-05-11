from rest_framework import mixins, viewsets
from rest_framework.response import Response

from allianceauth_api.serializers.fleetactivitytracking import FatListSerializer, FatSerializer, Fat
from allianceauth_api.serializers.fleetactivitytracking import FatlinkListSerializer, FatlinkSerializer, Fatlink


class FatViewSet(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = Fat.objects.all()
    serializer_class = FatSerializer

    def list(self, request, *args, **kwargs):
        serializer = FatListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class FatlinkViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Fatlink.objects.all()
    serializer_class = FatlinkSerializer

    def list(self, request, *args, **kwargs):
        serializer = FatlinkListSerializer(self.queryset, many=True)
        return Response(serializer.data)
