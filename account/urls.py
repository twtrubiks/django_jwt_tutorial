from django.contrib.auth.views import login
from django.urls import path

from account import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),

    # login logout
    path('login/', login, name='login'),
]
