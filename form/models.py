from django.db import models

class CNAB(models.Model):
    tipo = models.CharField(max_length=1)
    descricao = models.CharField(max_length=30)
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
    natureza = models.CharField(max_length=7)
    sinal = models.CharField(max_length=1)