from django.contrib import admin
from .models import BlogModel, user

# Register your models here.
admin.site.register(BlogModel)
admin.site.register(user)
