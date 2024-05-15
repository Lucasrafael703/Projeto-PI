from django.shortcuts import render
from django.db.models import Sum  # Importe Sum do módulo django.db.models
from .models import Arrecadacao

def soma_quantidade_arrecadacao(request):
    # Calcula a soma da quantidade de arrecadação
    soma = Arrecadacao.objects.aggregate(soma_quantidade=Sum('quantidade'))['soma_quantidade']
    context = {'soma_quantidade': soma}
    return render(request, 'index.html', context)
def pontos(request):
    return render(request, "pontos.html")

