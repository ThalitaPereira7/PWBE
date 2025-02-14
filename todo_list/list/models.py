from django.db import models

class Lista(models.Model):
    tarefa = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tarefa

# Create your models here.
