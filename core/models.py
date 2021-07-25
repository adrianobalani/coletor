# -*- Mode: Python; coding: utf-8 -*-

from django.db import models

# Create your models here.

class Upload(models.Model):
    pass

 

class Registro(models.Model):
    comprador = models.CharField("Comprador", max_length = 150)
    descricao = models.CharField("Descrição", max_length = 150)
    preco = models.IntegerField("Preço")
    quantidade = models.IntegerField("Quantidade")
    endereco = models.CharField("Endereço", max_length = 150)
    fornecedor = models.CharField("Fornecedor", max_length = 150)
    
