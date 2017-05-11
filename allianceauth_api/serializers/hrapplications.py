from rest_framework import serializers
from hrapplications.models import Application, ApplicationForm, ApplicationComment, ApplicationQuestion, \
    ApplicationResponse


class ApplicationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationQuestion
        exclude = ()


class ApplicationFormSerializer(serializers.ModelSerializer):
    corporation_id = serializers.IntegerField(source='corp.pk')

    class Meta:
        model = ApplicationForm
        exclude = ('corp',)


class ApplicationListSerializer(serializers.ModelSerializer):
    application_id = serializers.IntegerField(source='pk')
    form_id = serializers.IntegerField(source='form.pk')
    user_id = serializers.IntegerField(source='user.pk')
    reviewer_user_id = serializers.IntegerField(source='reviewer.pk')

    class Meta:
        model = Application
        fields = ('application_id', 'form_id', 'user_id', 'reviewer_user_id')


class ApplicationSerializer(serializers.ModelSerializer):
    application_id = serializers.IntegerField(source='pk')
    form_id = serializers.IntegerField(source='form.pk')
    user_id = serializers.IntegerField(source='user.pk')
    reviewer_user_id = serializers.IntegerField(source='reviewer.pk')
    reviewer_character_id = serializers.IntegerField(source='reviewer_character.pk')

    class Meta:
        model = Application
        exclude = ('id', 'form', 'user', 'reviewer', 'reviewer_character', 'created',)


class ApplicationResponseListSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='question.pk')
    application_id = serializers.IntegerField(source='application.pk')

    class Meta:
        model = ApplicationResponse
        fields = ('question_id', 'application_id')


class ApplicationResponseSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='question.pk')
    application_id = serializers.IntegerField(source='application.pk')

    class Meta:
        model = ApplicationResponse
        fields = ('question_id', 'application_id', 'answer')


class ApplicationCommentListSerializer(serializers.ModelSerializer):
    application_id = serializers.IntegerField(source='application.pk')
    user_id = serializers.IntegerField(source='user.pk')

    class Meta:
        model = ApplicationComment
        exclude = ('created', 'text', 'application', 'user')


class ApplicationCommentSerializer(serializers.ModelSerializer):
    application_id = serializers.IntegerField(source='application.pk')
    user_id = serializers.IntegerField(source='user.pk')

    class Meta:
        model = ApplicationComment
        exclude = ('application', 'user')
