from django.db import models
from collections import deque

# Create your models here.

ticket_id_counter = 0
_current_ticket_id = -1

service_customers = {"change_oil": deque(), "inflate_tires": deque(), "diagnostic": deque()}


def _incr_ticket_id_and_get():
    global ticket_id_counter
    ticket_id_counter += 1
    return ticket_id_counter


def _calculate_min_to_wait(service):
    if service == "change_oil":
        return len(service_customers["change_oil"]) * 2
    if service == "inflate_tires":
        return len(service_customers["change_oil"]) * 2 + len(service_customers["inflate_tires"]) * 5
    if service == "diagnostic":
        return len(service_customers["change_oil"]) * 2 + len(service_customers["inflate_tires"]) * 5 + len(
            service_customers["diagnostic"]) * 30


def _add_customer_to_queue(service, ticket_id):
    service_customers[service].append(ticket_id)


def get_ticket_id_and_min_to_wait(service):
    new_id = _incr_ticket_id_and_get()
    time = _calculate_min_to_wait(service)
    _add_customer_to_queue(service, new_id)
    return [new_id, time]


def _pop_next_ticket_id_from_queue():
    if len(service_customers["change_oil"]) != 0:
        return service_customers["change_oil"].popleft()
    if len(service_customers["inflate_tires"]) != 0:
        return service_customers["inflate_tires"].popleft()
    if len(service_customers["diagnostic"]) != 0:
        return service_customers["diagnostic"].popleft()
    return -1


def process_next_ticket():
    global _current_ticket_id
    _current_ticket_id = _pop_next_ticket_id_from_queue()


def get_current_ticket_id():
    return _current_ticket_id
