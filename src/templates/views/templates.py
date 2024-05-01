from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from templates.models import Template
from templates.serializers.template import TemplateSerializer, ReadTemplateSerializer


class TemplatesViewSet(ViewSet):

    def create(self, request):
        serializer = TemplateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(ReadTemplateSerializer(serializer.save()).data)

    def list(self, request):
        templates = Template.objects.all()
        paginator = Paginator(templates, 10)

        page_obj = paginator.get_page(int(request.query_params['page']))
        return Response({
            "count": len(templates),
            "results": ReadTemplateSerializer(list(page_obj.object_list), many=True).data,
            "pages_count": paginator.num_pages
        })
