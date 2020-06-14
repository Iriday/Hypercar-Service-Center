from ticket.models import get_ticket_id_and_min_to_wait, service_customers, process_next_ticket, \
    get_current_ticket_id

from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View


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


class OperatorMenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ticket/operator_menu.html",
                      context={"change_oil_queue": len(service_customers["change_oil"]),
                               "inflate_tires_queue": len(service_customers["inflate_tires"]),
                               "diagnostic_queue": len(service_customers["diagnostic"])})

    def post(self, request, *args, **kwargs):
        process_next_ticket()
        return redirect("/processing")


class NextView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ticket/next.html", context={"current_ticket_id": get_current_ticket_id()})
