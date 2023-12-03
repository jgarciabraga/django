from django.contrib import admin
from django.urls import path
from .views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDetailView, ClienteDeleteView

urlpatterns = [
    path("add_clientes", ClienteCreateView.as_view()),
    path("list_clientes", ClienteListView.as_view(), name="list_clientes"),
    path("update_cliente/<int:pk>",
         ClienteUpdateView.as_view(), name="update_cliente"),
    path("list_cliente/<int:pk>", ClienteDetailView.as_view(), name="list_cliente"),
    path("delete_cliente/<int:pk>",
         ClienteDeleteView.as_view(), name="delete_cliente"),
]
