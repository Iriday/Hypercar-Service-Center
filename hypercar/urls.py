"""hypercar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from ticket.views import WelcomeView, CustomerMenuView, GetTicketView, OperatorMenuView, NextView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', WelcomeView.as_view()),
    path('menu/', CustomerMenuView.as_view()),
    re_path('get_ticket/(?P<service>[\\w]+)', GetTicketView.as_view()),
    path("processing", OperatorMenuView.as_view()),
    path("processing/", RedirectView.as_view(url="/processing")),
    path("next", NextView.as_view()),
    path("next/", RedirectView.as_view(url="/next"))
]
