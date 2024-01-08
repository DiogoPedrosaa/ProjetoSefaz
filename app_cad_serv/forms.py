from django import forms
from .models import Servidor, TarefaRealizada
from django.core.validators import MinLengthValidator, ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

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
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, label='Nome de Usuario')

    def clean_username(self):
        username = self.cleaned_data['username']
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso. Escolha outro.')
        return username
    
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'is_superusuario']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superusuario = self.cleaned_data['is_superusuario']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        password = forms.CharField(label="Senha", widget=forms.PasswordInput)


