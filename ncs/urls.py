

from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from .views import HomeView, Messages, Table, dashboard, items

urlpatterns = [
    path("", HomeView.as_view(), name = 'home'),
    path("dashboard/", dashboard, name = 'dashboard'),
    path("tables", items, name = 'tables'),
    path("messages/",Messages, name = 'messages'),

]
