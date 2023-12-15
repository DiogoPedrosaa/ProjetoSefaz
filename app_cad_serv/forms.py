from django import forms
from .models import Servidor, TarefaRealizada
from django.core.validators import MinLengthValidator, ValidationError

class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ['nome', 'escala', 'tipo_escala', 'matricula', 'pontualidade', 'assiduidade', 'execucao_tarefas', 'iniciativa', 'atendimento_servicos', 'tipo_modalidade']
        labels = {
            'execucao_tarefas': 'Execução de Tarefas',
            'atendimento_servicos': 'Atendimento de Serviços',
        }
    


class TarefaRealizadaForm(forms.ModelForm):
    class Meta:
        model = TarefaRealizada
        fields = ['diretor_coordenador', 'tarefas']
        labels = {
            'diretor_coordenador': 'Diretor/Coordenador',
        }

    def clean_tarefas(self):
        tarefas = self.cleaned_data.get('tarefas')
        if len(tarefas) < 15:
            raise ValidationError('O campo tarefas deve ter no mínimo 15 caracteres.')
        return tarefas