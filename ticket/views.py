from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.conf import settings


# Create your views here.

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h2>Welcome to the Hypercar Service!<h2>")


class CustomerMenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ticket/customer_menu.html", context={"services_urls": settings.SERVICES_URLS})
