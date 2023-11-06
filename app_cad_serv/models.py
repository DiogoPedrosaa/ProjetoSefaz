from django.db import models
from django import forms

class Servidor(models.Model):
    nome = models.CharField(max_length=100)
    escala = models.CharField(max_length=10)
    matricula = models.CharField(max_length=20)
    pontualidade = models.CharField(max_length=50)
    assiduidade = models.CharField(max_length=10)
    execucao_tarefas = models.CharField(max_length=10)
    iniciativa = models.CharField(max_length=10)
    atendimento_servicos = models.CharField(max_length=10)
    total_pontos = models.IntegerField(default=0)

     
class TarefaRealizada(models.Model):
    colaborador = models.CharField(max_length=100)
    diretor_coordenador = models.CharField(max_length=100)
    tarefas = models.TextField()
    data = models.DateTimeField(auto_now_add=True)