import requests
from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Arrecadador(Base):
    nome = models.CharField(max_length=255)
    cep = models.CharField(max_length=8, default='00000-000')  # Campo para armazenar o CEP
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Arrecadador'
        verbose_name_plural = 'Arrecadadores'

    def __str__(self):
        return self.nome


class Vestuario(Base):
    roupa = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Vestuario'
        verbose_name_plural = 'vestuarios'

    def __str__(self):
        return self.roupa


class Arrecadacao(Base):
    arrecadador = models.ForeignKey(Arrecadador, related_name='arrecadacoes', on_delete=models.CASCADE)
    vestuario = models.ForeignKey(Vestuario, related_name='arrecadacoes', on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=4)
    genero = models.CharField(max_length=1)
    quantidade = models.IntegerField(validators=[MaxValueValidator(999)])

    class Meta:
        verbose_name = 'Arrecadação'
        verbose_name_plural = 'Arrecadações'

    def __str__(self):
        return f'O arrecadador {self.arrecadador} arrecadou {self.quantidade} peças de {self.vestuario}'


@receiver(pre_save, sender=Arrecadador)
def preencher_endereco_por_cep(sender, instance, **kwargs):
    # Consulta o ViaCEP para obter os dados do CEP
    response = requests.get(f'http://viacep.com.br/ws/{instance.cep}/json/')
    data = response.json()

    # Atualiza os campos de bairro e cidade com os dados obtidos
    instance.bairro = data.get('bairro', '')
    instance.cidade = data.get('localidade', '')
