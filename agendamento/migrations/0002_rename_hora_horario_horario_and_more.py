# Generated by Django 5.0.7 on 2024-07-19 18:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("agendamento", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="horario",
            old_name="hora",
            new_name="horario",
        ),
        migrations.RemoveField(
            model_name="horario",
            name="dia_semana",
        ),
    ]
