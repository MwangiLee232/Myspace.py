from django.db import models
from profiles.models import Profile

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    likes = models.ManyToManyField(Profile, related_name='liked_posts')
    timestamp = models.DateTimeField(auto_now_add=True)
