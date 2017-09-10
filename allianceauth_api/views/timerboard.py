from rest_framework import viewsets
from rest_framework.response import Response
from allianceauth_api.serializers.timerboard import TimerListSerializer, TimerSerializer, Timer


class TimerViewSet(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer

    def list(self, request, *args, **kwargs):
        serializer = TimerListSerializer(self.queryset, many=True)
        return Response(serializer.data)
