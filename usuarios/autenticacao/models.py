from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nome = models.CharField(max_length=30, blank=True, null=True)
    biografia = models.CharField(max_length=50, blank=True, null=True)
    idade = models.PositiveBigIntegerField(blank=True, null=True)
    telefone = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True) 
    escolaridade = models.CharField(max_length=100, blank=True, null=True)
    animais = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
