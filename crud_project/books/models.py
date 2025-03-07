from django.db import models

class Book(models.Model):  
    titulo = models.CharField(max_length=200)  
    autor = models.CharField(max_length=100)  
    ano_publicacao = models.IntegerField()  
    descricao = models.TextField() 

    def __str__(self):
        return self.titulo  
    class Meta:
        verbose_name_plural = "Livros"