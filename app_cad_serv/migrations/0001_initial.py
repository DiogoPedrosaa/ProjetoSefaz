# Generated by Django 4.2.7 on 2023-11-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('escala', models.CharField(max_length=10)),
                ('matricula', models.CharField(max_length=20)),
                ('pontualidade', models.CharField(max_length=10)),
                ('assiduidade', models.CharField(max_length=10)),
                ('execucao_tarefas', models.CharField(max_length=10)),
                ('iniciativa', models.CharField(max_length=10)),
                ('atendimento_servicos', models.CharField(max_length=10)),
            ],
        ),
    ]
