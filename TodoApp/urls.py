"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TodoApp import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('pending', views.pending, name='pending'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('delete_all_task', views.delete_all_task, name='delete_all_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),

    ]
