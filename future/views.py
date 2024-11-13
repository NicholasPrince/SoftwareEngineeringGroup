from django.shortcuts import render

def main_content_view(request):
    # Landing page (Pick Your Path page)
    return render(request, 'home.html')

def view_path_view(request):
    # Page to view the chosen path (e.g., Game Development)
    return render(request, 'view_path.html')

def progress_view(request):
    # Progress tracking page
    return render(request, 'progress.html')

def login_view(request):
    # Login page
    return render(request, 'login.html')

def register_view(request):
    # Register page
    return render(request, 'register.html')
