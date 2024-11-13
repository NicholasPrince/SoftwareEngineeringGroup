"""
URL configuration for future project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_content_view, name='home'),         # Landing page
    path('path/', views.view_path_view, name='view_path'),  # View Path page
    path('progress/', views.progress_view, name='progress'),  # Progress page
    path('login/', views.login_view, name='login'),         # Login page
    path('register/', views.register_view, name='register'), # Register page
]
