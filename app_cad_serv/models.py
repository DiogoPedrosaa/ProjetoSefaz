from django.db import models


class Servidor(models.Model):

    ESCALA_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    PONTUALIDADE_CHOICES = [
        ('Sem Justificativa', 'Sem Justificativa'),
        ('2 Justificativas', '2 Justificativas'),
        ('3 Justificativas', '3 Justificativas'),
        ('5 Justificativas', '5 Justificativas'),
    ]

    ASSIDUIDADE_CHOICES = [
        ('Sem Faltas', 'Sem Faltas'),
        ('1 Falta', '1 Falta'),
        ('2 Faltas', '2 Faltas'),
        ('3 Faltas', '3 Faltas'),
    ]

    EXECUCAO_TAREFAS_CHOICES = [
        ('Excelente', 'Excelente'),
        ('Otimo', 'Ótimo'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
    ]

    INICIATIVA_CHOICES = [
        ('Excelente', 'Excelente'),
        ('Otimo', 'Ótimo'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
    ]

    ATENDIMENTO_SERVICOS_CHOICES = [
        ('Excelente', 'Excelente'),
        ('Otimo', 'Ótimo'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
    ]

    TIPO_ESCALA_CHOICES = [
        ('DIRETA', 'Direta'),
        ('INDIRETA', 'Indireta'),
    ]

    nome = models.CharField(max_length=100, null=False, default='')
    escala = models.CharField(max_length=10, choices=ESCALA_CHOICES)
    tipo_escala = models.CharField(max_length=10, choices=TIPO_ESCALA_CHOICES, default='')
    matricula = models.CharField(max_length=10, null=False, default='', unique=True)
    pontualidade = models.CharField(max_length=50, choices=PONTUALIDADE_CHOICES)
    assiduidade = models.CharField(max_length=10, choices=ASSIDUIDADE_CHOICES)
    execucao_tarefas = models.CharField(max_length=10, choices=EXECUCAO_TAREFAS_CHOICES)
    iniciativa = models.CharField(max_length=10, choices=INICIATIVA_CHOICES)
    atendimento_servicos = models.CharField(max_length=10, choices=ATENDIMENTO_SERVICOS_CHOICES)
    total_pontos = models.IntegerField(default=0)
    gratificacao_pontos = models.IntegerField(default=0)

     
class TarefaRealizada(models.Model):
    colaborador = models.CharField(max_length=100)
    diretor_coordenador = models.CharField(max_length=100, null=False)
    tarefas = models.TextField()
    data = models.DateTimeField(auto_now_add=True)