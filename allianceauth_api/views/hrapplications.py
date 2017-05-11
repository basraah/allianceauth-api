from rest_framework import viewsets, mixins
from rest_framework.response import Response
from allianceauth_api.serializers.hrapplications import *


class ApplicationQuestionViewSet(mixins.RetrieveModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    queryset = ApplicationQuestion.objects.all()
    serializer_class = ApplicationQuestionSerializer


class ApplicationFormViewSet(mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer


class ApplicationViewSet(mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def list(self, request, *args, **kwargs):
        serializer = ApplicationListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ApplicationResponseViewSet(mixins.RetrieveModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    queryset = ApplicationResponse.objects.all()
    serializer_class = ApplicationResponseSerializer

    def list(self, request, *args, **kwargs):
        serializer = ApplicationResponseListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ApplicationCommentViewSet(mixins.RetrieveModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    queryset = ApplicationComment.objects.all()
    serializer_class = ApplicationCommentSerializer

    def list(self, request, *args, **kwargs):
        serializer = ApplicationCommentListSerializer(self.queryset, many=True)
        return Response(serializer.data)
