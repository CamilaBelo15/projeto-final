from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    marca = models.CharField(max_length=100, blank=True, null=True)
    tamanho = models.CharField(max_length=50, blank=True, null=True)


class Entrada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='entradas')
    quantidade = models.IntegerField()
    data_entrada = models.DateTimeField


class Saida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='saidas')
    quantidade = models.IntegerField()
    data_saida = models.DateTimeField



