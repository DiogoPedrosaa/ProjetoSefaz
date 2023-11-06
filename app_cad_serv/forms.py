from django import forms
from .models import Servidor, TarefaRealizada

class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = '__all__'
        exclude = ['total_pontos']


class TarefaRealizadaForm(forms.ModelForm):
    class Meta:
        model = TarefaRealizada
        fields = ['diretor_coordenador', 'tarefas', 'colaborador']

    def __init__(self, *args, **kwargs):
        super(TarefaRealizadaForm, self).__init__(*args, **kwargs)
        self.fields['colaborador'].widget = forms.HiddenInput()