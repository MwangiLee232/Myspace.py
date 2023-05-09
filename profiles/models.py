from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
