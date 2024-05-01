import json

from rest_framework import serializers

from templates.models import Template


class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = '__all__'


class ReadTemplateSerializer(serializers.ModelSerializer):

    doc_fields = serializers.SerializerMethodField()

    class Meta:
        model = Template
        fields = '__all__'

    @classmethod
    def get_doc_fields(cls, template):
        return json.loads(template.doc_fields)
