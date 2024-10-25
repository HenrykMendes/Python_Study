from django.db import models

# Create your models here.
#criar campos models
#models.CharField: Usado para armazenar pequenas string no database
#models.TextField: É geralmente usado para armazenar qualquer arquivo de texto
#models.DecimalFiel: Campo para armazenar valores decimais
#models.InegerField: Campo para armazenar valores inteiros
class Produtos (models.Model):
    nome = models.CharField (max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return self.nome