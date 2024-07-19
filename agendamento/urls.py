from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar, name='listar'),
    path('agendar/', views.agendar, name='agendar'),
    path('sucesso/', views.agendamento_sucesso, name='agendamento_sucesso'),
]
