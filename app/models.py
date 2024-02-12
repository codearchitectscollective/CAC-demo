from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.contrib.auth.models import User

class AuthUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(6)])
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usernames
    class Meta:
        app_label = 'app'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Trending(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trending_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='trending_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='trending_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Featured(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='news_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='news_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    image = models.ImageField(default='default.png', upload_to='User_Profile_images/')
    
    def __str__(self):
        return f'{self.user.username} Profile' 
    
