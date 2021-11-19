from django.db import models
from django.db.models import constraints
# from django.db.models.fields import IntegerField

# Create your models here.

class Cliente(models.Model):
    codigo = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    nome = models.CharField(max_length=200)
    rg = models.BigIntegerField(default=0)
    cpf = models.BigIntegerField(default=0)
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    usuario = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['codigo', 'cpf', 'usuario'], name = 'cliente_unique')
        ]


class Prestador(models.Model):
    codigo = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    nome = models.CharField(max_length=200)
    insc_est = models.BigIntegerField(default=0)
    cnpj = models.BigIntegerField(default=0)
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    usuario = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['codigo', 'cnpj', 'usuario'], name = 'prestador_unique')
        ]

class Transporte(models.Model):
    codigo = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    prestador = models.ForeignKey(Prestador, related_name = 'transportes', on_delete=models.CASCADE)
    veiculo = models.CharField(max_length=200)
    capacidade = models.IntegerField(default=0)
    moveis = models.BooleanField()
    eletro = models.BooleanField()
    metais = models.BooleanField()    
    alvenaria = models.BooleanField()
    madeiramento = models.BooleanField()
    troncos = models.BooleanField()
    arbusto = models.BooleanField()
    grama = models.BooleanField()
    preco = models.DecimalField(max_digits=15, decimal_places=2)

class Contrato(models.Model):
    codigo = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    cliente = models.ForeignKey(Cliente, related_name = 'contratante', on_delete=models.CASCADE)
    transporte = models.ForeignKey(Transporte, related_name = 'contratado', on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    moveis = models.BooleanField()
    eletro = models.BooleanField()
    metais = models.BooleanField()    
    alvenaria = models.BooleanField()
    madeiramento = models.BooleanField()
    troncos = models.BooleanField()
    arbusto = models.BooleanField()
    grama = models.BooleanField()
