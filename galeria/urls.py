from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),  # A rota para pagina principal chama o metodo index
    path('imagem/', imagem, name='imagem'),
]