
from django.urls import path
from app_cad_serv import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cadastrar/', views.cadastrar, name = 'cadastrar'),
    path('dados_servidor/', views.dados_servidor, name='dados_servidor'),
    path('cadastrar/cadastro_sucesso.html', views.cadastro_sucesso, name = 'cadastro_sucesso'),
    path('relatorio_servidor/<int:servidor_id>/', views.relatorio_servidor, name='relatorio_servidor'),
    path('preencher-tarefas/<int:servidor_id>/', views.preencher_tarefas, name='preencher_tarefas'),
    path('visualizar-tarefas/<int:servidor_id>/', views.visualizar_tarefas_servidor, name='visualizar_tarefas_servidor'),
    path('download_pdf/', views.generate_pdf, name='download_pdf'),
    path('excluir_servidor/<int:servidor_id>/', views.excluir_servidor, name='excluir_servidor'),
    path('dados_servidor_geral/', views.dados_servidor_geral, name='dados_servidor_geral'),
]
