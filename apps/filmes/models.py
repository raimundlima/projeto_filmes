from django.db import models

# Create your models here.
class Filme(models.Model):
    id_filme = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    genero = models.TextField(max_length=50)
    ano_lancamento = models.IntegerField()
    Sinopse = models.TextField(max_length=250)
    capa = models.URLField()

    def __str__(self):
        return self.url