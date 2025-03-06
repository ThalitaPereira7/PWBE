from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.TextField()
    ano = models.IntegerField()
   

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Livros"

# Create your models here.
