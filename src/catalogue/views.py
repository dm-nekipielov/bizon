from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import ListView

from catalogue.models import Category
from catalogue.tasks import mine_bitcoin, normalize_email_task


class IndexView(ListView):
    model = Category
    template_name = "index.html"


def bitcoin(request):
    mine_bitcoin.delay()
    return HttpResponse("task is started")

def normalize_email(request):
    normalize_email_task.delay(filter=dict(email__endswith=".com"))
    return HttpResponse("task is started")