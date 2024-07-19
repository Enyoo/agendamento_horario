from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agendamento.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # URL de login
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL de logout
]
