from django.db import models
from django.contrib.auth.models  import User


class Categoria(models.Model):
    nome = models.CharField(max_length=30)


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.FloatField(default=0)
    preco = models.FloatField(default=0)
    ativo = models.BooleanField(default=False)


class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)
    quantidade = models.FloatField(null=False)
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
