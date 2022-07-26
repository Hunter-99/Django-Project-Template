from django.views.generic.base import TemplateView

from main.models import Product

class HomePage(TemplateView):
    template_name = 'main/index.html'
    model = None
    context_object_name = ''
