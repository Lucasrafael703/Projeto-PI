from django.urls import path
from .views import soma_quantidade_arrecadacao

urlpatterns = [
    path('soma-arrecadacao/', soma_quantidade_arrecadacao, name='soma_arrecadacao'),
]
