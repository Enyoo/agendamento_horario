from django.db import models
from django.contrib.auth.models import User

class Horario(models.Model):
    horario = models.TimeField()

    def __str__(self):
        return str(self.horario)

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"{self.usuario} - {self.horario} em {self.data}"
