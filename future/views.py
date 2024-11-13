from django.shortcuts import render

def main_content_view(request):
    return render(request, 'home.html')  # Landing page

def view_path_view(request):
    return render(request, 'view_path.html')  # View path details

def progress_view(request):
    return render(request, 'progress.html')  # Progress page

def login_view(request):
    return render(request, 'login.html')  # Login page

def register_view(request):
    return render(request, 'register.html')  # Register page
