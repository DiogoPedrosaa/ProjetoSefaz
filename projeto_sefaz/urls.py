
from django.urls import path
from app_cad_serv import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cadastrar/', views.cadastrar, name = 'cadastrar'),
    path('dados_servidor/', views.dados_servidor, name='dados_servidor'),
    path('cadastrar/cadastro_sucesso.html', views.cadastro_sucesso, name = 'cadastro_sucesso'),
    path('relatorio_servidor/<int:servidor_id>/', views.relatorio_servidor, name='relatorio_servidor'),
    path('entrada_dados/<int:servidor_id>/', views.entrada_dados, name='entrada_dados'),
    path('processar_dados/', views.processar_dados, name='processar_dados'),
    path('relatorio_sintetico/', views.relatorio_sintetico, name='relatorio_sintetico'),
]
