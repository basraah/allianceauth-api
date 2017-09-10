from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from allianceauth_api.serializers.srp import SrpFleetMainListSerializer, SrpFleetMainSerializer, SrpFleetMain
from allianceauth_api.serializers.srp import SrpUserRequestListSerializer, SrpUserRequestSerializer, SrpUserRequest


class SrpFleetMainViewSet(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = SrpFleetMain.objects.all()
    serializer_class = SrpFleetMainSerializer

    def list(self, request, *args, **kwargs):
        serializer = SrpFleetMainListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def requests(self, request, *args, **kwargs):
        serializer = SrpUserRequestListSerializer(self.get_object().srpuserrequest_set.all(), many=True)
        return Response(serializer.data)


class SrpUserRequestsViewSet(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = SrpUserRequest.objects.all()
    serializer_class = SrpUserRequestSerializer

    def list(self, request, *args, **kwargs):
        serializer = SrpUserRequestListSerializer(self.queryset, many=True)
        return Response(serializer.data)
