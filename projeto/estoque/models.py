from django.db import models

# Create your models here.

class Produto(models.model):
    nome= models.CharField(max_length=100)
    preco= models.FloatField()
    quantidade= models.IntegerField()
    def __str__(self): return self.nome