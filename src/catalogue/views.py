from django.views.generic import ListView

from catalogue.models import Category


class IndexView(ListView):
    model = Category
    template_name = "index.html"
