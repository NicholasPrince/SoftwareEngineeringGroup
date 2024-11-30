from django.contrib import admin

# Register your models here.
from .models import Track, User

admin.site.register(User)
admin.site.register(Track)

