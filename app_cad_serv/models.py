from django.db import models
from django.core.exceptions import ValidationError
from django.utils.formats import number_format
from django.utils.translation import gettext as _
from django.utils import formats
import locale


class Servidor(models.Model):


    def validar_nome(value):
        if any(char.isdigit() for char in value):
            raise ValidationError('O nome não pode conter números.')

    def validar_matricula(value):
        if not value.isdigit():
            raise ValidationError('A matrícula deve conter apenas números.')


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

    TIPO_MODALIDADE_CHOICES = [
        ('PRESENCIAL', 'Presencial'),
        ('REMOTO', 'Remoto'),
    ]

    def calcular_valor_escala(self):
        valores_escala_direta = {'A': 16.71, 'B': 24.98, 'C': 36.56, 'D': 50.65}
        valores_escala_indireta = {'A': 11.02, 'B': 16.71, 'C': 24.98, 'D': 36.46}

        if self.tipo_escala == 'DIRETA':
            return valores_escala_direta.get(self.escala, 0)
        elif self.tipo_escala == 'INDIRETA':
            return valores_escala_indireta.get(self.escala, 0)
        else:
            return 0
        


    def calcular_gratificacao(self):
        
        valor_escala = self.calcular_valor_escala()
        gratificacao = valor_escala * self.total_pontos
        return round(gratificacao, 2)

    def gratificacao_formatada(self):
        gratificacao = self.calcular_gratificacao()
        # Configurar a localização para o Brasil (ou sua localização desejada)
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
        formatted_gratificacao = locale.currency(gratificacao, grouping=True, symbol=None)
        return formatted_gratificacao
    
    
    nome = models.CharField(max_length=100, null=False, default='', validators=[validar_nome])
    escala = models.CharField(max_length=10, choices=ESCALA_CHOICES)
    tipo_escala = models.CharField(max_length=10, choices=TIPO_ESCALA_CHOICES, default='')
    matricula = models.CharField(max_length=10, null=False, default='', unique=True, validators=[validar_matricula])
    pontualidade = models.CharField(max_length=50, choices=PONTUALIDADE_CHOICES)
    assiduidade = models.CharField(max_length=10, choices=ASSIDUIDADE_CHOICES)
    execucao_tarefas = models.CharField(max_length=10, choices=EXECUCAO_TAREFAS_CHOICES)
    iniciativa = models.CharField(max_length=10, choices=INICIATIVA_CHOICES)
    atendimento_servicos = models.CharField(max_length=10, choices=ATENDIMENTO_SERVICOS_CHOICES)
    total_pontos = models.IntegerField(default=0)
    gratificacao_pontos = models.IntegerField(default=0)
    tipo_modalidade = models.CharField(max_length=10,choices=TIPO_MODALIDADE_CHOICES, default='')
    mes_referencia = models.CharField(max_length=20, default='')



     
class TarefaRealizada(models.Model):
    colaborador = models.CharField(max_length=100)
    diretor_coordenador = models.CharField(max_length=100, null=False)
    tarefas = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


