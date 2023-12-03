from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Cliente

# Create your views here.


class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_clientes.html"
    success_url = "list_clientes"


class ClienteListView(ListView):
    model = Cliente
    template_name = "list_clientes.html"


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ("nome", "is_ativo", "email")
    template_name = "form_clientes.html"
    success_url = reverse_lazy("list_clientes")


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "list_cliente.html"
    context_object_name = "cliente"


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "delete_cliente.html"
    success_url = reverse_lazy("list_clientes")
