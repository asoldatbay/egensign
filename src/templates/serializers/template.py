from rest_framework import serializers

from src.templates.models import Template


class ReadTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = '__all__'
