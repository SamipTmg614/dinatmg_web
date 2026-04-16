from django.db import models

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    body = models.TextField(max_length=5000)

    class Meta:
        ordering = ['-date_uploaded']

    def __str__(self):
        return self.title

class user(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

