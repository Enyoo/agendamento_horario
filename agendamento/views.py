# agendamento/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Horario, Agendamento


def listar(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamento/lista_agendamento.html', {'agendamentos': agendamentos})

def agendamento_sucesso(request):
    return render(request, 'agendamento/sucesso.html')

@login_required
def agendar(request):
    if request.method == "POST":
        data = request.POST.get('data')
        horarios_ids = request.POST.getlist('horarios')
        usuario = request.user

        for horario_id in horarios_ids:
            horario = Horario.objects.get(id=horario_id)
            Agendamento.objects.create(usuario=usuario, horario=horario, data=data)

        return redirect('agendamento_sucesso')

    horarios = Horario.objects.all()
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamento/agendamento_form.html', {'horarios': horarios, 'agendamentos': agendamentos})
