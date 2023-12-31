from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Servidor, TarefaRealizada
from .forms import ServidorForm, TarefaRealizadaForm, SignUpForm
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
from io import BytesIO
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Paragraph
import locale, logging
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

logger = logging.getLogger(__name__)

@login_required
def home(request):
    user = request.user
    return render(request, 'servidores/home.html', {'user': user})

@login_required
def cadastrar(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            servidor = form.save(commit=False)

            pontos, gratificacao = calcular_pontos(
                form.cleaned_data['pontualidade'],
                form.cleaned_data['assiduidade'],
                form.cleaned_data['execucao_tarefas'],
                form.cleaned_data['iniciativa'],
                form.cleaned_data['atendimento_servicos']
            )
            servidor.total_pontos = pontos  
            servidor.gratificacao_pontos = gratificacao
            servidor.save()

            return redirect('cadastro_sucesso')
    else:
        form = ServidorForm()

        

    return render(request, 'servidores/cadastrar.html', {'form': form})

@login_required
def dados_servidor(request):
    servidores = Servidor.objects.all()
    
    return render(request, 'servidores/dados_servidor.html', {'servidores': servidores})

@login_required
def cadastro_sucesso(request):
    return render(request, 'servidores/cadastro_sucesso.html')


def calcular_pontos(pontualidade, assiduidade, execucao_tarefas, iniciativa, atendimento_servicos):
    pontos = 0

    pontualidade = pontualidade.lower()
    assiduidade = assiduidade.lower()
    execucao_tarefas = execucao_tarefas.lower()
    iniciativa = iniciativa.lower()
    atendimento_servicos = atendimento_servicos.lower()
    
   
    if pontualidade == "sem justificativa":
        pontos += 10
    elif pontualidade == "2 justificativas":
        pontos += 8
    elif pontualidade == "3 justificativas":
        pontos += 4
    elif pontualidade == "5 justificativas":
        pontos += 2

    
    if assiduidade == "sem faltas":
        pontos += 10
    elif assiduidade == "1 falta":
        pontos += 8
    elif assiduidade == "2 faltas":
        pontos += 4
    elif assiduidade == "3 faltas":
        pontos += 2

    

    if execucao_tarefas == "excelente":
        pontos += 30
    elif execucao_tarefas == "otimo":
        pontos += 20
    elif execucao_tarefas == "bom":
        pontos += 15
    elif execucao_tarefas == "regular":
        pontos += 10


    
    

    if iniciativa == "excelente":
        pontos += 20
    elif iniciativa == "otimo":
        pontos += 15
    elif iniciativa == "bom":
        pontos += 10
    elif iniciativa == "regular":
        pontos += 5


    

    if atendimento_servicos == "excelente":
        pontos += 30
    elif atendimento_servicos == "otimo":
        pontos += 20
    elif atendimento_servicos == "bom":
        pontos += 15
    elif atendimento_servicos == "regular":
        pontos += 10


    gratificacao = pontos * 50

    return pontos, gratificacao


@login_required
def relatorio_servidor(request, servidor_id):
    
    servidor = Servidor.objects.get(pk=servidor_id)
    print(servidor)  # Isso imprimirá os dados do servidor no console
    return render(request, 'servidores/relatorio_servidor.html', {'servidor': servidor})
    


#Logica dos calculos de pontuação total dos servidores (melhorar)
def calcular_pontos_pontualidade(pontualidade):

    pontualidade = pontualidade.lower()

    if pontualidade == "sem justificativa":
        return 10
    elif pontualidade == "2 justificativas":
        return 8
    elif pontualidade == "3 justificativas":
        return 4
    elif pontualidade == "5 justificativas":
        return 2
    else:
        return 0
    



def calcular_pontos_assiduidade(assiduidade):

    assiduidade = assiduidade.lower()

    if assiduidade == "sem faltas":
        return 10
    elif assiduidade == "1 falta":
        return 8
    elif assiduidade == "2 faltas":
        return 4
    elif assiduidade == "3 faltas":
        return 2
    else:
        return 0
    


def calcular_pontos_exec_tarefas(execucao_tarefas):

    execucao_tarefas = execucao_tarefas.lower()

    if execucao_tarefas == "excelente":
        return 30
    elif execucao_tarefas == "otimo":
        return 20
    elif execucao_tarefas == "bom":
        return 15
    elif execucao_tarefas == "regular":
        return 10
    else:
        return 0
    

def calcular_pontos_iniciativa(iniciativa):

    iniciativa = iniciativa.lower()

    if iniciativa == "excelente":
        return 20
    elif iniciativa == "otimo":
        return 15
    elif iniciativa == "bom":
        return 10
    elif iniciativa == "regular":
        return 5
    else:
        return 0
    
    


def calcular_pontos_atendimento_servicos(atendimento_servicos):

    atendimento_servicos = atendimento_servicos.lower()

    if atendimento_servicos == "excelente":
        return 30
    elif atendimento_servicos == "otimo":
        return 20
    elif atendimento_servicos == "bom":
        return 15
    elif atendimento_servicos == "regular":
        return 10
    else:
        return 0
    
    
@login_required
def relatorio_servidor(request, servidor_id):
    servidor = Servidor.objects.get(pk=servidor_id)
    
    
    pontos_pontualidade = calcular_pontos_pontualidade(servidor.pontualidade)
    pontos_assiduidade = calcular_pontos_assiduidade(servidor.assiduidade)
    pontos_exec_tarefas = calcular_pontos_exec_tarefas(servidor.execucao_tarefas)
    pontos_iniciativa = calcular_pontos_iniciativa(servidor.iniciativa)
    pontos_atendimento_servicos = calcular_pontos_atendimento_servicos(servidor.atendimento_servicos)
    
    return render(request, 'servidores/relatorio_servidor.html', {
        'servidor': servidor,
        'pontos_pontualidade': pontos_pontualidade,
        'pontos_assiduidade': pontos_assiduidade,
        'pontos_exec_tarefas': pontos_exec_tarefas,
        'pontos_iniciativa': pontos_iniciativa,
        'pontos_atendimento_servicos': pontos_atendimento_servicos,
    })



    
@login_required
def preencher_tarefas(request, servidor_id):
    servidor = Servidor.objects.get(pk=servidor_id)

    if request.method == 'POST':
        form = TarefaRealizadaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.colaborador = servidor.nome
            tarefa.diretor_coordenador = form.cleaned_data['diretor_coordenador']
            tarefa.save()
            return redirect('dados_servidor')  # Redirecione para uma página de sucesso

    else:
        form = TarefaRealizadaForm(initial={'colaborador': servidor.nome})

    return render(request, 'servidores/preencher_tarefas.html', {'form': form, 'servidor': servidor})



@login_required
def visualizar_tarefas_servidor(request, servidor_id):
    servidor = get_object_or_404(Servidor, pk=servidor_id)
    tarefas = TarefaRealizada.objects.filter(colaborador=servidor.nome)
    return render(request, 'servidores/visualizar_tarefas_servidor.html', {'servidor': servidor, 'tarefas': tarefas, 'matricula': servidor.matricula})



@login_required
def generate_pdf(request):
    
    servidores = Servidor.objects.all()

    
    buffer = BytesIO()

    
    custom_page_size = landscape(letter)
    #Ajusta margens da tabela
    doc = SimpleDocTemplate(buffer, pagesize=custom_page_size, rightMargin=50, leftMargin=20)
    elements = []

    secretaria_name = "SECRETARIA MUNICIPAL DA ECONOMIA - SEFAZ"
    secretaria_style = getSampleStyleSheet()['Title']
    secretaria_paragraph = Paragraph(secretaria_name, style=secretaria_style)

    elements.append(secretaria_paragraph)

    # Defina a largura das colunas na tabela
    col_widths = [170, 50, 50, 70, 70, 80, 70, 90, 60, 60, 70]

    # Crie uma lista de dados para a tabela
    data = []
    data.append(["Nome do Servidor", "Escala", "Mat.", "Pontualidade", "Assiduidade", "Exec. Tarefas", "Iniciativa", "At. Serviços", "Total Pontos",])

    for servidor in servidores:
        data.append([servidor.nome, servidor.escala, servidor.matricula, servidor.pontualidade, servidor.assiduidade, servidor.execucao_tarefas, servidor.iniciativa, servidor.atendimento_servicos, servidor.total_pontos])

    
    table = Table(data, colWidths=col_widths)

    # Defina estilos para cabeçalhos e células
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])



    # Ajuste o estilo de cada célula (cabeçalho e conteúdo)
    style.add('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    style.add('ALIGN', (0, 0), (-1, -1), 'CENTER')
    style.add('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
    style.add('BACKGROUND', (0, 1), (-1, -1), colors.white)
    style.add('GRID', (0, 0), (-1, -1), 1, colors.black)
    style.add('FONTSIZE', (0, 1), (-1, -1), 8)  #tamanho da fonte 
    style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3)  # Ajusta o preenchimento das células de conteúdo

    # Ajuste a altura mínima das linhas
    style.add('LEADING', (0, 1), (-1, -1), 10)

    
    table.setStyle(style)

    
    elements.append(table)
    doc.build(elements)

    
    buffer.seek(0)

    # Crie uma resposta de arquivo para o PDF gerado
    response = FileResponse(buffer, as_attachment=True, filename='Dados_Servidores.pdf')



    return response





@login_required
def generate_pdf_geral(request):
    servidores = Servidor.objects.all()
    buffer = BytesIO()

    custom_page_size = landscape(letter)
    doc = SimpleDocTemplate(buffer, pagesize=custom_page_size, rightMargin=50, leftMargin=20)
    elements = []

    info_table_data = [
        ["PREFEITURA MUNICIPAL DE MACEIÓ"],
        ["SECRETARIA MUNICIPAL DA FAZENDA"],
        ["SETOR: COORD, GERAL DE ATENDIMENTO AO CONTRIBUINTE"],
        ["COORDENADOR: TESTE"],
        ["MÊS REFERÊNCIA - teste"]
    ]
    info_table = Table(info_table_data, colWidths=[200])

    info_table.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), -280),
    ]))

    elements.append(info_table)

    secretaria_name = "SECRETARIA MUNICIPAL DA ECONOMIA - SEFAZ"
    secretaria_style = getSampleStyleSheet()['Title']
    secretaria_paragraph = Paragraph(secretaria_name, style=secretaria_style)
    elements.append(secretaria_paragraph)

    col_widths = [170, 50, 70, 70, 70, 60, 70, 90, 60]

    data = [
        ["Nome do Servidor", "Mat.", "Gratificação", "Administ", "Observação", "Escala", "V.P ATUAL", "Total Pontos", "Nº SERV"]
    ]

    for servidor in servidores:
        data.append([
            servidor.nome,
            servidor.matricula,
            servidor.gratificacao_formatada(),  # Chame o método para obter o valor real
            servidor.tipo_escala,
            servidor.tipo_modalidade,
            servidor.escala,
            servidor.calcular_valor_escala(),  # Chame o método para obter o valor real
            servidor.total_pontos,
            servidor.id
        ])

    table = Table(data, colWidths=col_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    style.add('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    style.add('ALIGN', (0, 0), (-1, -1), 'CENTER')
    style.add('TEXTCOLOR', (0, 1), (-1, -1), colors.black)
    style.add('BACKGROUND', (0, 1), (-1, -1), colors.white)
    style.add('GRID', (0, 0), (-1, -1), 1, colors.black)
    style.add('FONTSIZE', (0, 1), (-1, -1), 8)
    style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3)
    style.add('LEADING', (0, 1), (-1, -1), 10)

    table.setStyle(style)
    elements.append(table)
    doc.build(elements)

    buffer.seek(0)

    response = FileResponse(buffer, as_attachment=True, filename='Dados_Servidores_Geral.pdf')
    return response

def formatar_mes_referencia():
    
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

    
    mes_referencia = datetime.now().strftime('%B %Y')
    
    
    mes, ano = mes_referencia.split()
    
    
    mes = mes.capitalize()
    
    
    return f"{mes} de {ano}"

@login_required
def excluir_servidor(request, servidor_id):
    servidor = get_object_or_404(Servidor, pk=servidor_id)
    servidor.delete()
    return redirect('dados_servidor')


#Logica para calcular valores especificos das escalas (não funcionando)
@login_required
def dados_servidor_geral(request):
    servidor = Servidor.objects.all()
    mes_referencia = formatar_mes_referencia()
    return render(request, 'servidores/dados_servidor_geral.html', {'servidores': servidor, 'mes_referencia': mes_referencia})



def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Adicione mensagens de log para entender o que está sendo enviado para authenticate
            logger.debug(f'Username: {username}')
            logger.debug(f'Password: {password}')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
        else:
            # Adicione uma mensagem de log para identificar possíveis problemas
            logger.error(f'Formulário inválido: {form.errors}')
    else:
        form = AuthenticationForm()

    return render(request, 'servidores/login.html', {'form': form})

@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já em uso. Escolha outro.')
                return render(request, 'servidores/cadastrar_usuario.html', {'form': form})

            user = form.save()
            return redirect('cadastro_sucesso')
    else:
        form = SignUpForm()

    return render(request, 'servidores/cadastrar_usuario.html', {'form': form})

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        # Redireciona o usuário para a página home após o logout
        return redirect('home')  # Certifique-se de ter uma URL nomeada 'home' em suas configurações de URL
