from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    USUARIO_ESCOLHAS = [
        ('gest','gestor'),
        ('prof','professor')
    ]
    
    usuario = models.CharField(max_length=4, choices=USUARIO_ESCOLHAS, default='prof')
    biografia = models.TextField(max_length=200, blank=True ,null=True)
    idade = models.PositiveIntegerField(null=True,blank=True)
    telefone = models.CharField(max_length=11,null=True,blank=True)



    def __str__(self):
        return self.username


class Professor(models.Model):
    ni = models.PositiveIntegerField(unique=True)  
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()

    def __str__(self):
        return f'{self.nome} ({self.ni})'


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()  
    descricao = models.TextField()
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='disciplinas_atribuidas')

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
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reservas')
    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f'Sala {self.sala_reservada} - {self.data_inicio} a {self.data_termino}'



