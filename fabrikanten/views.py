from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from fabrikanten.models import Fabrikanten


# Create your views here.
class FabrikantenListView(ListView):
    model = Fabrikanten


class FabrikantenCreateView(CreateView):
    model = Fabrikanten
    fields = "__all__"
    success_url = reverse_lazy("fabrikanten:list")


class FabrikantenUpdateView(UpdateView):
    model = Fabrikanten
    fields = "__all__"
    success_url = reverse_lazy("fabrikanten:list")


class FabrikantenDeleteView(DeleteView):
    model = Fabrikanten
    success_url = reverse_lazy("fabrikanten:list")
