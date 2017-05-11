from rest_framework import viewsets
from rest_framework.response import Response
from allianceauth_api.serializers.optimer import OpTimerListSerializer, OpTimerSerializer, OpTimer


class OpTimerViewSet(viewsets.ModelViewSet):
    queryset = OpTimer.objects.all()
    serializer_class = OpTimerSerializer

    def list(self, request, *args, **kwargs):
        serializer = OpTimerListSerializer(self.queryset, many=True)
        return Response(serializer.data)
