from django.shortcuts import render, redirect
from .models import Servidor
from .forms import ServidorForm

def home(request):
    return render(request, 'servidores/home.html')

def cadastrar(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            servidor = form.save(commit=False)
            
            # Calcule os pontos com base nas respostas do formulário
            pontos = calcular_pontos(
                form.cleaned_data['pontualidade'],
                form.cleaned_data['assiduidade'],
                form.cleaned_data['execucao_tarefas'],
                form.cleaned_data['iniciativa'],
                form.cleaned_data['atendimento_servicos']
            )
            servidor.total_pontos = pontos  # Atribua os pontos ao servidor
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



from django.shortcuts import render, redirect

def entrada_dados(request):
    return render(request, 'entrada_dados.html')

def processar_dados(request):
    if request.method == 'POST':
        diretor_coordenador = request.POST['diretor_coordenador']
        nome_servidor = request.POST['nome_servidor']
        matricula_servidor = request.POST['matricula_servidor']
        tarefas_executadas = request.POST['tarefas_executadas']

        # Armazene essas informações no banco de dados ou onde preferir

        # Redirecione para a página do relatório sintético
        return redirect('relatorio_sintetico')

    return redirect('entrada_dados')

def relatorio_sintetico(request):
    # Recupere as informações do servidor e dos dados do diretor/coordenador aqui
    # Renderize a página do relatório sintético
    return render(request, 'relatorio_sintetico.html')