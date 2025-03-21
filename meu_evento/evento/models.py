from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=500)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome}"

# Create your models here.
