from django.template.response import TemplateResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'


def two_forms_both_must_pass(request):
    return TemplateResponse(request, 'two_forms.html')