from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index),  # A rota para pagina principal chama o metodo index
    path('imagem/', imagem)
]