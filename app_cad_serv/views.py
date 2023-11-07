from django.shortcuts import render, redirect, get_object_or_404
from .models import Servidor, TarefaRealizada
from .forms import ServidorForm, TarefaRealizadaForm
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
from io import BytesIO
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Paragraph







def home(request):
    return render(request, 'servidores/home.html')

def cadastrar(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            servidor = form.save(commit=False)
            
            
            pontos = calcular_pontos(
                form.cleaned_data['pontualidade'],
                form.cleaned_data['assiduidade'],
                form.cleaned_data['execucao_tarefas'],
                form.cleaned_data['iniciativa'],
                form.cleaned_data['atendimento_servicos']
            )
            servidor.total_pontos = pontos  
            servidor.save()

            return redirect('cadastro_sucesso')
    else:
        form = ServidorForm()

    return render(request, 'servidores/cadastrar.html', {'form': form})


def dados_servidor(request):
    servidores = Servidor.objects.all()
    return render(request, 'servidores/dados_servidor.html', {'servidores': servidores})


def cadastro_sucesso(request):
    return render(request, 'servidores/cadastro_sucesso.html')


def calcular_pontos(pontualidade, assiduidade, execucao_tarefas, iniciativa, atendimento_servicos):
    pontos = 0

    pontualidade = pontualidade.lower()
    assiduidade = assiduidade.lower()
    execucao_tarefas = execucao_tarefas.lower()
    iniciativa = iniciativa.lower()
    atendimento_servicos = atendimento_servicos.lower()
    
    # Calcular pontos para a pontualidade
    if pontualidade == "sem justificativa":
        pontos += 10
    elif pontualidade == "2 justificativas":
        pontos += 8
    elif pontualidade == "3 justificativas":
        pontos += 4
    elif pontualidade == "5 justificativas":
        pontos += 2

    # Calcular pontos para a assiduidade
    if assiduidade == "sem faltas":
        pontos += 10
    elif assiduidade == "1 falta":
        pontos += 8
    elif assiduidade == "2 faltas":
        pontos += 4
    elif assiduidade == "3 faltas":
        pontos += 2

    # Calcular pontos para execução de tarefas

    if execucao_tarefas == "excelente":
        pontos += 30
    elif execucao_tarefas == "otimo":
        pontos += 20
    elif execucao_tarefas == "bom":
        pontos += 15
    elif execucao_tarefas == "regular":
        pontos += 10


    # Calcular pontos para iniciativa
    

    if iniciativa == "excelente":
        pontos += 20
    elif iniciativa == "otimo":
        pontos += 15
    elif iniciativa == "bom":
        pontos += 10
    elif iniciativa == "regular":
        pontos += 5


    # Calcular pontos para atendimentos de serviço 

    if atendimento_servicos == "excelente":
        pontos += 30
    elif atendimento_servicos == "otimo":
        pontos += 20
    elif atendimento_servicos == "bom":
        pontos += 15
    elif atendimento_servicos == "regular":
        pontos += 10
   

    return pontos


def relatorio_servidor(request, servidor_id):
    
    servidor = Servidor.objects.get(pk=servidor_id)
    print(servidor)  # Isso imprimirá os dados do servidor no console
    return render(request, 'servidores/relatorio_servidor.html', {'servidor': servidor})
    


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
    
    

def relatorio_servidor(request, servidor_id):
    servidor = Servidor.objects.get(pk=servidor_id)
    
    # Calcule os pontos para cada categoria usando as funções correspondentes
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



def visualizar_tarefas_servidor(request, servidor_id):
    servidor = get_object_or_404(Servidor, pk=servidor_id)
    tarefas = TarefaRealizada.objects.filter(colaborador=servidor.nome)
    return render(request, 'servidores/visualizar_tarefas_servidor.html', {'servidor': servidor, 'tarefas': tarefas, 'matricula': servidor.matricula})



def generate_pdf(request):
    # Busque os dados que deseja incluir no PDF (por exemplo, servidores)
    servidores = Servidor.objects.all()

    # Crie um objeto BytesIO para armazenar o PDF em memória
    buffer = BytesIO()

    # Crie o documento PDF
    custom_page_size = landscape(letter)
    doc = SimpleDocTemplate(buffer, pagesize=custom_page_size)
    elements = []

    # Defina a largura das colunas na tabela
    col_widths = [170, 50, 50, 70, 70, 80, 70, 90, 60]

    # Crie uma lista de dados para a tabela
    data = []
    data.append(["Nome do Servidor", "Escala", "Mat.", "Pontualidade", "Assiduidade", "Exec. Tarefas", "Iniciativa", "At. Serviços", "Total Pontos"])

    for servidor in servidores:
        data.append([servidor.nome, servidor.escala, servidor.matricula, servidor.pontualidade, servidor.assiduidade, servidor.execucao_tarefas, servidor.iniciativa, servidor.atendimento_servicos, servidor.total_pontos])

    # Crie a tabela e defina seu estilo
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
    style.add('FONTSIZE', (0, 1), (-1, -1), 10)  # Altere o tamanho da fonte para 10
    style.add('BOTTOMPADDING', (0, 1), (-1, -1), 3)  # Ajuste o preenchimento das células de conteúdo

    # Ajuste a altura mínima das linhas
    style.add('LEADING', (0, 1), (-1, -1), 10)

    
    table.setStyle(style)

    
    elements.append(table)
    doc.build(elements)

    
    buffer.seek(0)

    # Crie uma resposta de arquivo para o PDF gerado
    response = FileResponse(buffer, as_attachment=True, filename='example.pdf')



    return response