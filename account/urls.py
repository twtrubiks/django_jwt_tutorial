from django.contrib.auth import views as auth_views
from django.urls import path

from account import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),

    # login logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
