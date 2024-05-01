from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet

from documents.serializers.generate import GenerateSerializer
from documents.services.convertapi import ConvertAPIService
from templates.dispatcher import dispatcher
from templates.models import Template
from templates.scripts.base_script import BaseScript


class GenerateViewSet(ViewSet):

    def create(self, request):

        generate_serializer = GenerateSerializer(data=request.data)
        generate_serializer.is_valid(raise_exception=True)

        template = get_object_or_404(Template, id=generate_serializer.validated_data["template_id"])
        script_class: BaseScript = dispatcher.get_script_class(template)

        file64, file_type = script_class().preview(request)

        convert_response, file_type = ConvertAPIService.docx_to_pdf(file64)

        return HttpResponse(convert_response["Files"][0]["FileData"], content_type=file_type)
