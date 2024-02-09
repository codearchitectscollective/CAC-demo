from django.db import models
from django.core.validators import MinLengthValidator

class AuthUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(6)])
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usernames
    class Meta:
        app_label = 'app'