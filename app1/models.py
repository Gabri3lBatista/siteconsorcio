from django.db import models
from stdimage import StdImageField
from django.core.validators import MaxValueValidator, MinValueValidator
import random

# Create your models here.
class Carro(models.Model):
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    imagem = StdImageField('imagem', upload_to='carros', variations={'thumb': (100, 100)})
    def  __str__(self):
        #self é como o this em java.
        return "{} {}".format(self.marca, self.modelo)

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    email = models.CharField('Email', max_length=100)
    telefone = models.CharField(max_length=11)
    modelo_desejado = models.ForeignKey(Carro, on_delete=models.CASCADE)
    parcelas = models.IntegerField(validators = [MinValueValidator(36), MaxValueValidator(180)])
    def  __str__(self):
        #self é como o this em java.
        return "{} {}".format(self.nome, self.sobrenome)

class Sorteio(models.Model):
    vencedor = models.ForeignKey(Cliente, on_delete=models.CASCADE, editable=False, null=True)
    data = models.DateField()
    modelo = models.ForeignKey(Carro, on_delete=models.CASCADE)
    def  __str__(self):
        #self é como o this em java.
        return "{} - {} {}".format(self.data, self.modelo.marca, self.modelo.modelo)
