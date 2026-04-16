from django.db import models
from django.utils.text import slugify

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    body = models.TextField(max_length=5000)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-date_uploaded']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while BlogModel.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class BlogComment(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.name}"


class ContactInfo(models.Model):
    page_title = models.CharField(max_length=100, default="Let’s talk")
    intro_text = models.TextField(
        default="Reach out if you want to discuss school operations, student support, or a new campus project."
    )
    email = models.EmailField(default="deena.admin@gmail.com")
    phone = models.CharField(max_length=30, default="+1 (000) 123-4567")
    whatsapp_number = models.CharField(max_length=20, default="10001234567")
    whatsapp_label = models.CharField(max_length=50, default="WhatsApp")
    whatsapp_help_text = models.CharField(max_length=80, default="Chat instantly")
    instagram_url = models.URLField(default="https://www.instagram.com")
    linkedin_url = models.URLField(default="https://www.linkedin.com")
    youtube_url = models.URLField(default="https://www.youtube.com")

    class Meta:
        verbose_name = "Contact info"
        verbose_name_plural = "Contact info"

    def __str__(self):
        return self.page_title

class user(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

