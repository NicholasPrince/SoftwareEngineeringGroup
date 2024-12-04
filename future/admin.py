from django.contrib import admin
from .models import Track, User, Path, Video, Resource, Project

# Register your models here
admin.site.register(User)
admin.site.register(Track)
admin.site.register(Path)
admin.site.register(Video)
admin.site.register(Resource)
admin.site.register(Project)
