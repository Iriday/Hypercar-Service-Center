from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View
from ticket.models import get_ticket_id_and_min_to_wait, service_customers
from django.conf import settings


# Create your views here.

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h2>Welcome to the Hypercar Service!<h2>")


class CustomerMenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ticket/customer_menu.html", context={"services_urls": settings.SERVICES_URLS})


class GetTicketView(View):
    def get(self, request, service, *args, **kwargs):
        if service not in service_customers:
            raise Http404
        id_, time = get_ticket_id_and_min_to_wait(service)
        return render(request, "ticket/get_ticket.html", context={"ticket_id": id_, "min_to_wait": time})
