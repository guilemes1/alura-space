from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index)  # A rota para pagina principal chama o metodo index
]