from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from autos.models import Auto


# Create your views here.

class AutoListView(ListView):
    model = Auto


class AutoCreateView(CreateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:list")


class AutoUpdateView(UpdateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:list")


class AutoDeleteView(DeleteView):
    model = Auto
    success_url = reverse_lazy("autos:list")
