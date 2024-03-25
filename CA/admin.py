from django.contrib import admin

from .models import Arrecadador, Vestuario, Arrecadacao, Tamanho


@admin.register(Arrecadador)
class ArrecadadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bairro', 'cidade', 'criacao', 'atualizacao', 'ativo')


@admin.register(Vestuario)
class VestuarioAdmin(admin.ModelAdmin):
    list_display = ('roupa', 'criacao', 'atualizacao', 'ativo')


@admin.register(Arrecadacao)
class ArecadacaoAdmin(admin.ModelAdmin):
    list_display = ('arrecadador', 'vestuario', 'tamanho', 'genero', 'quantidade', 'atualizacao', 'ativo')

@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('size', 'criacao', 'atualizacao', 'ativo')
# Register your models here.
