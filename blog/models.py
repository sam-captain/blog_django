from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    views = models.IntegerField(default=0,blank=True)
    slug = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title =models.CharField(max_length=100)
    message= models.TextField()
    likes=models.IntegerField(default=0, blank=True)
    Dislike=models.IntegerField(default=0, blank=True)
    slug =models.SlugField(max_length=200)
    category= models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False)
    image_url =models.ImageField(max_length=255)
    views =models.IntegerField(default=0, blank=True)
    keywords =models.TextField(max_length=50)
    user =models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    message= models.TextField()
    user =models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    post =models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    likes=models.IntegerField(default=0, blank=True)
    Dislike=models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="Comments"

    def __str__(self):
        return self.message

class Feedback(models.Model):
    message =models.TextField()
    name =models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Seo(models.Model):
    title=models.CharField(max_length=100)
    keywords=models.TextField()
    occasion=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    
