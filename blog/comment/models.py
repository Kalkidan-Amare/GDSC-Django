from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    content=models.TextField()
    created_time=models.DateTimeField(default=timezone.now)
    modified_time=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"comment {self.id}"