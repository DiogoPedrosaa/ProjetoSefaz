from django.db import models

class Servidor(models.Model):
    nome = models.CharField(max_length=100, null=False, default='')
    escala = models.CharField(max_length=10, null=False, default='')
    matricula = models.CharField(max_length=20, null=False, default='')
    pontualidade = models.CharField(max_length=50, null=False, default='')
    assiduidade = models.CharField(max_length=10, null=False, default='')
    execucao_tarefas = models.CharField(max_length=10, null=False, default='')
    iniciativa = models.CharField(max_length=10, null=False, default='')
    atendimento_servicos = models.CharField(max_length=10, null=False, default='')
    total_pontos = models.IntegerField(default=0)


    
    ESCALA_CHOICES = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ]
    
    PONTUALIDADE_CHOICES = [
        ('sem justificativa', 'Sem Justificativa'),
        ('2 justificativas', '2 Justificativas'),
        ('3 justificativas', '3 Justificativas'),
        ('5 justificativas', '5 Justificativas'),
    ]

    ASSIDUIDADE_CHOICES = [
        ('sem faltas', 'Sem Faltas'),
        ('1 falta', '1 Falta'),
        ('2 faltas', '2 Faltas'),
        ('3 faltas', '3 Faltas'),
    ]

    EXECUCAO_TAREFAS_CHOICES = [
        ('excelente', 'Excelente'),
        ('otimo', 'Ótimo'),
        ('bom', 'Bom'),
        ('regular', 'Regular'),
    ]

    INICIATIVA_CHOICES = [
        ('excelente', 'Excelente'),
        ('otimo', 'Ótimo'),
        ('bom', 'Bom'),
        ('regular', 'Regular'),
    ]

    ATENDIMENTO_SERVICOS_CHOICES = [
        ('excelente', 'Excelente'),
        ('otimo', 'Ótimo'),
        ('bom', 'Bom'),
        ('regular', 'Regular'),
    ]

    escala = models.CharField(max_length=50, choices=ESCALA_CHOICES)
    pontualidade = models.CharField(max_length=50, choices=PONTUALIDADE_CHOICES)
    assiduidade = models.CharField(max_length=10, choices=ASSIDUIDADE_CHOICES)
    execucao_tarefas = models.CharField(max_length=10, choices=EXECUCAO_TAREFAS_CHOICES)
    iniciativa = models.CharField(max_length=10, choices=INICIATIVA_CHOICES)
    atendimento_servicos = models.CharField(max_length=10, choices=ATENDIMENTO_SERVICOS_CHOICES)

    total_pontos = models.IntegerField(default=0)

     
class TarefaRealizada(models.Model):
    colaborador = models.CharField(max_length=100)
    diretor_coordenador = models.CharField(max_length=100, null=False)
    tarefas = models.TextField()
    data = models.DateTimeField(auto_now_add=True)