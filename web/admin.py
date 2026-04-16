from django.contrib import admin
from .models import BlogModel, BlogComment, ContactInfo, user

# Register your models here.
admin.site.register(BlogModel)
admin.site.register(BlogComment)
admin.site.register(ContactInfo)
admin.site.register(user)
