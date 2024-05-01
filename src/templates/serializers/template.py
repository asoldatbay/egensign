from rest_framework import serializers

from templates.models import Template


class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = '__all__'


class ReadTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = '__all__'
