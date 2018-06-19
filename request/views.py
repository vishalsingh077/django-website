from django.shortcuts import render
from django.views import generic
from .models import Request

class requests_view(generic.ListView):
    template_name = "request/requests_page.html"
    context_object_name = 'all_requests'

    def get_queryset(self):
        return Request.objects.all()


class request_detail_view(generic.DetailView):
    model = Request
    template_name = "request/request_detail_page.html"


