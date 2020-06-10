from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h2>Welcome to the Hypercar Service!<h2>")
