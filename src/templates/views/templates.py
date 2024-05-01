from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.templates.models import Template


class TemplatesViewSet(ViewSet):

    def list(self, request):
        templates = Template.objects.all()
        paginator = Paginator(templates, 10)

        page_obj = paginator.get_page(int(request.query_params['page']))
        return Response({
            "count": len(templates),
            "results": page_obj,
            "pages_count": paginator.num_pages
        })
