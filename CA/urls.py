from django.urls import path
from .views import soma_quantidade_arrecadacao
from .views import pontos

urlpatterns = [
    path('index/', soma_quantidade_arrecadacao, name='soma_arrecadacao'),
    path('', soma_quantidade_arrecadacao, name=''),
    path('pontos/', pontos, name='pontos'),
]
