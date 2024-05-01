from rest_framework import serializers


class GenerateSerializer(serializers.Serializer):
    template_id = serializers.IntegerField()
    filled_data = serializers.JSONField()
