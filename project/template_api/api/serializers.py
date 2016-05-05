from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TemplateSnippet


class JSONSerializerField(serializers.JSONField):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        import json
        return json.loads(value)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet-detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'snippets')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TemplateSnippetDefaultSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    context = JSONSerializerField(binary=False)

    class Meta:
        model = TemplateSnippet
        read_only_fields = ('rendered', 'processed')
        fields = (
            'owner', 'created', 'code',
            'context', 'rendered',
            'engine', 'processed'
        )

