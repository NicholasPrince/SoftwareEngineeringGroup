from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_content_view, name='home'),           # Landing page
    path('path/', views.view_path_view, name='view_path'),    # View Path page
    path('progress/', views.progress_view, name='progress'),  # Progress page
    path('login/', views.login_view, name='login'),           # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logoutUser, name='logout'),         # Logout function
    
    path('content/<str:content_type>/', views.dynamic_content_view, name='dynamic_content'),
]
