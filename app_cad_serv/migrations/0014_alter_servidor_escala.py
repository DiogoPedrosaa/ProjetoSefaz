# Generated by Django 5.0 on 2023-12-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_serv', '0013_alter_servidor_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='escala',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10),
        ),
    ]