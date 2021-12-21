from django.urls import path
from . import views

urlpatterns = [
    # Вход
    path('', views.signin, name='signin'),
    # Выход
    path('logout', views.logout_view, name='logout'),
    # Регистрация
    path('register', views.register, name='register'),
]