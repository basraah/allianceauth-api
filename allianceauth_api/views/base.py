from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from allianceauth_api.serializers.base import User, Group, Permission
from allianceauth_api.serializers.base import UserListSerializer, GroupListSerializer, PermissionListSerializer
from allianceauth_api.serializers.base import UserSerializer, GroupSerializer, PermissionSerializer

from allianceauth_api.serializers.eveonline import EveCharacterListSerializer, EveApiKeyPairListSerializer
from allianceauth_api.serializers.groupmanagement import AuthGroupSerializer
from allianceauth_api.serializers.fleetactivitytracking import FatlinkListSerializer, FatListSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def characters(self, request, *args, **kwargs):
        serializer = EveCharacterListSerializer(self.get_object().evecharacter_set.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def apikeys(self, request, *args, **kwargs):
        serializer = EveApiKeyPairListSerializer(self.get_object().eveapikeypair_set.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def groups(self, request, *args, **kwargs):
        serializer = GroupListSerializer(self.get_object().groups.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def permissions(self, request, *args, **kwargs):
        serializer = PermissionListSerializer(self.get_object().user_permissions.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def fats(self, request, *args, **kwargs):
        serializer = FatListSerializer(self.get_object().fat_set.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def fatlinks(self, request, *args, **kwargs):
        serializer = FatlinkListSerializer(self.get_object().fatlink_set.all(), many=True)
        return Response(serializer.data)


class GroupViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request, *args, **kwargs):
        serializer = GroupListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def users(self, request, *args, **kwargs):
        serializer = UserListSerializer(self.get_object().user_set.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def permissions(self, request, *args, **kwargs):
        serializer = PermissionListSerializer(self.get_object().permissions.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def authgroup(self, request, *args, **kwargs):
        serializer = AuthGroupSerializer(self.get_object().authgroup)
        return Response(serializer.data)


class PermissionViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def list(self, request, *args, **kwargs):
        serializer = PermissionListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def users(self, request, *args, **kwargs):
        serializer = UserListSerializer(self.get_object().user_set.all(), many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def groups(self, request, *args, **kwargs):
        serializer = GroupListSerializer(self.get_object().group_set.all(), many=True)
        return Response(serializer.data)
