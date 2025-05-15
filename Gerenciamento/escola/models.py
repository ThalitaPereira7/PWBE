from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    REQUIRED_FIELDS = ['data_nascimento', 'data_contratacao']
    ni = models.IntegerField(max_length=100,blank=True, null=True)  
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, related_name='professor_disciplina', null=True, blank=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()


    def __str__(self):
        return self.username
    
class Disciplina(models.Model):

    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()  
    descricao = models.TextField()
    professor_responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='disciplinas_atribuidas')

    def __str__(self):
        return self.nome


class ReservaAmbiente(models.Model):
    PERIODO_CHOICES = [
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite'),
    ]

    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=10, choices=PERIODO_CHOICES)
    sala_reservada = models.CharField(max_length=50)
    professor_responsavel = models.ManyToManyField(Usuario, related_name='reservas')
    disciplina_associada = models.ManyToManyField(Disciplina, related_name='reservas')

    def __str__(self):
        return f'Sala {self.sala_reservada} - {self.data_inicio} a {self.data_termino}'



