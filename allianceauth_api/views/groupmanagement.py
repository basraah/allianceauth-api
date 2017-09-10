from rest_framework import viewsets, mixins
from rest_framework.response import Response
from allianceauth_api.serializers.groupmanagement import AuthGroupSerializer, AuthGroup
from allianceauth_api.serializers.groupmanagement import GroupRequestSerializer, GroupRequestListSerializer, \
    GroupRequest


class GroupRequestViewSet(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = GroupRequest.objects.all()
    serializer_class = GroupRequestSerializer

    def list(self, request, *args, **kwargs):
        serializer = GroupRequestListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class AuthGroupViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer
