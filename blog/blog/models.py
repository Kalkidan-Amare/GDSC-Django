from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    body=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    class Status(models.TextChoices):
        DRAFT=('DF', 'Draft')
        PUBLISHED=('PD','Publilshed')
    
    status=models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-publish']
        indexes=[
            models.Index(fields=['-publish'])
        ]
    def __str__(self):
        return self.slug
