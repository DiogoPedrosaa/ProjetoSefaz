# Generated by Django 4.2.7 on 2023-11-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0008_servidor_assiduidade_servidor_atendimento_servicos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='assiduidade',
            field=models.CharField(choices=[('sem faltas', 'Sem Faltas'), ('1 falta', '1 Falta'), ('2 faltas', '2 Faltas'), ('3 faltas', '3 Faltas')], max_length=10),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='atendimento_servicos',
            field=models.CharField(choices=[('excelente', 'Excelente'), ('otimo', 'Ótimo'), ('bom', 'Bom'), ('regular', 'Regular')], max_length=10),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='execucao_tarefas',
            field=models.CharField(choices=[('excelente', 'Excelente'), ('otimo', 'Ótimo'), ('bom', 'Bom'), ('regular', 'Regular')], max_length=10),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='iniciativa',
            field=models.CharField(choices=[('excelente', 'Excelente'), ('otimo', 'Ótimo'), ('bom', 'Bom'), ('regular', 'Regular')], max_length=10),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='pontualidade',
            field=models.CharField(choices=[('sem justificativa', 'Sem Justificativa'), ('2 justificativas', '2 Justificativas'), ('3 justificativas', '3 Justificativas'), ('5 justificativas', '5 Justificativas')], max_length=50),
        ),
    ]