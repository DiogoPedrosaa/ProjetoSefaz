# Generated by Django 5.0 on 2023-12-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0015_servidor_gratificacao_pontos'),
    ]

    operations = [
        migrations.AddField(
            model_name='servidor',
            name='tipo_escala',
            field=models.CharField(choices=[('DIRETA', 'Direta'), ('INDIRETA', 'Indireta')], default='', max_length=10),
        ),
    ]
